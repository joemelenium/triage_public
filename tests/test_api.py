"""Checks the API gives exactly what the engine gives.

The API keeps nothing between calls and replays the interview from the evidence
each time, so a person answering through the API must reach the same outcome,
after the same questions, as the same person answering the engine directly.
"""

import random

import pytest

from api import interview as api
from conftest import EXAMPLES
from engine.runner import load_case, run_case
from scale import consistent, rounds

CHOICE = {"yes": "present", "no": "absent", "not_sure": "unknown", True: "present", False: "absent"}


def through_the_api(kb, case: dict, sex: str) -> tuple[dict, int]:
    """Answer the API's questions as the case says, as a client would. Returns the
    triage reply and the number of questions asked."""
    truth = case.get("answers") or {}
    otherwise = CHOICE[case.get("otherwise", "no")]
    evidence = [{"id": f, "choice_id": "present", "source": "initial"} for f in case["presenting"]]
    evidence += [{"id": f, "choice_id": CHOICE[a], "source": "initial"} for f, a in (case.get("opening_findings") or {}).items()]
    evidence += [{"id": f, "choice_id": CHOICE[a], "source": "predefined"}
                 for f, a in ((case.get("context") or {}).get("findings") or {}).items()]
    request = {"sex": sex, "age": {"value": (case.get("context") or {}).get("age", 30)}, "evidence": evidence}
    for asked in range(100):
        reply = api.diagnosis(kb, request)
        if reply["should_stop"]:
            return api.triage(kb, request), asked
        for item in reply["question"]["items"]:
            answer = CHOICE[truth[item["id"]]] if item["id"] in truth else otherwise
            request["evidence"].append({"id": item["id"], "choice_id": answer})
    raise AssertionError("the interview never ended")


def directly(kb, case: dict, sex: str) -> dict:
    context = {"age": 30, **(case.get("context") or {}), "sex": sex}
    return run_case(kb, {**case, "context": context})


@pytest.mark.parametrize("path", [p for p in EXAMPLES if p.stem != "not_covered"], ids=lambda p: p.stem)
def test_each_example_gives_the_same_outcome_through_the_api(kb, path):
    case = load_case(path)
    for sex in ("female", "male"):
        reply, asked = through_the_api(kb, case, sex)
        record = directly(kb, case, sex)
        assert reply["interview_finished"]
        assert reply["extras"]["outcome"] == record["outcome"]
        assert reply["triage_level"] == record["five_level_triage"]["triage_level"]
        assert asked == len(record["questions_asked"])


def test_random_patients_give_the_same_outcome_through_the_api(kb):
    rng = random.Random(7)
    modules = sorted(kb.modules.values(), key=lambda m: m.id)
    for _ in range(rounds(40)):
        module = rng.choice(modules)
        presenting = [module.presenting_finding]
        others = [f for f in kb.findings if kb.findings[f].kind not in ("presenting", "context")]
        answers = consistent(kb, {f: "yes" for f in rng.sample(others, 3)}, presenting)
        case = {"presenting": presenting, "context": {"age": rng.choice([4, 30, 70])}, "answers": answers, "otherwise": "no"}
        sex = rng.choice(["female", "male"])
        reply, asked = through_the_api(kb, case, sex)
        record = directly(kb, case, sex)
        assert reply["extras"]["outcome"] == record["outcome"], (module.id, answers)
        assert asked == len(record["questions_asked"]), (module.id, answers)


def test_triage_part_way_through_says_the_interview_is_not_finished(kb):
    request = {"sex": "female", "age": {"value": 30},
               "evidence": [{"id": "sore_throat", "choice_id": "present", "source": "initial"}]}
    reply = api.triage(kb, request)
    assert reply["interview_finished"] is False
    assert reply["triage_level"] in ("emergency_ambulance", "emergency", "consultation_24", "consultation", "self_care")


@pytest.mark.parametrize("request_body, problem", [
    ({"sex": "other", "age": {"value": 30}, "evidence": []}, "sex"),
    ({"sex": "female", "age": {}, "evidence": []}, "age"),
    ({"sex": "female", "age": {"value": 30}, "evidence": [{"id": "no_such_thing", "choice_id": "present"}]}, "Unknown evidence"),
    ({"sex": "female", "age": {"value": 30}, "evidence": [{"id": "sore_throat", "choice_id": "maybe", "source": "initial"}]}, "choice_id"),
    ({"sex": "female", "age": {"value": 30}, "evidence": []}, "main symptom"),
], ids=["sex", "age", "unknown id", "choice", "no main symptom"])
def test_a_bad_request_is_refused_with_a_plain_reason(kb, request_body, problem):
    with pytest.raises(api.BadRequest, match=problem):
        api.diagnosis(kb, request_body)


def test_the_server_answers(kb):
    from fastapi.testclient import TestClient
    from api.server import app
    client = TestClient(app)
    assert client.get("/info").json()["conditions_count"] == len(kb.conditions)
    assert {"id": "sore_throat", "label": "Sore throat"} in client.get("/search", params={"phrase": "sore"}).json()
    body = {"sex": "male", "age": {"value": 40}, "evidence": [{"id": "chest_pain", "choice_id": "present", "source": "initial"}]}
    reply = client.post("/diagnosis", json=body).json()
    assert reply["question"]["items"] and reply["should_stop"] is False
    refused = client.post("/diagnosis", json={**body, "evidence": [{"id": "x", "choice_id": "present", "source": "initial"}]})
    assert refused.status_code == 400 and "Unknown evidence" in refused.json()["detail"]
    assert client.get("/").status_code == 200
