"""Checks the fixed safety rules in the brief (section 3 and 4.3)."""

import copy
from pathlib import Path

import pytest

from conftest import EXAMPLES, REPO_ROOT
from engine.kb import load_knowledge_base
from engine.runner import load_case, run_case
from engine.session import run
from scale import rounds


def questions(record) -> list[str]:
    return [q["id"] for q in record["questions_asked"]]


def test_emergency_red_flag_stops_the_session_at_once(kb, example):
    record = run_case(kb, example("chest_pain_emergency"))
    assert record["outcome"]["acuity"] == "emergency"
    # The flag was found in the chest pain emergency screen. Nothing was asked after it.
    assert questions(record)[-1] == "chest_pain_emergency_screen"
    assert record["questions_asked"][-1]["outcome_after"]["acuity"] == "emergency"


def test_non_emergency_red_flag_does_not_stop_the_red_flag_screen(kb, example):
    # Two urgent red flags are present. Both must be found, not just the first.
    case = example("chest_pain_comes_and_goes")
    case["answers"]["cp_on_exertion"] = "yes"   # the comes-and-goes rule needs an angina-like sign (DECISIONS 140)
    case["answers"]["leg_pain_or_swelling"] = "yes"
    record = run_case(kb, case)
    found = {flag["rule"] for flag in record["red_flags_found"]}
    assert {"rf_cp_comes_and_goes", "rf_cp_leg_pain_or_swelling"} <= found
    assert kb.acuity_rank[record["outcome"]["acuity"]] <= kb.acuity_rank["urgent"]


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.stem)
def test_outcome_is_never_below_a_red_flag_that_fired(kb, path):
    # A firm red flag is a floor. (A rule marked "soft" may be lowered by likely conditions.)
    soft = {r.id for m in kb.modules.values() for r in m.red_flags + m.outcome_rules if r.soft}
    record = run_case(kb, load_case(path))
    for flag in record["red_flags_found"]:
        if flag["rule"] not in soft:
            assert kb.acuity_rank[record["outcome"]["acuity"]] <= kb.acuity_rank[flag["acuity"]]


def test_not_sure_is_treated_as_unknown_and_handled_cautiously(kb, example):
    unsure = run_case(kb, example("sore_throat_not_sure"))
    assert unsure["outcome"]["acuity"] == "urgent"
    assert unsure["caution"]["drove_outcome"] is True
    assert unsure["findings"]["unknown"][0]["id"] == "very_high_temperature"

    # The same case with a clear "no" is self-care, so "not sure" was not read as "no".
    sure = example("sore_throat_not_sure")
    sure["answers"]["very_high_temperature"] = "no"
    assert run_case(kb, sure)["outcome"]["acuity"] == "self_manageable"


def test_not_sure_to_a_whole_screen_means_each_item_is_asked_on_its_own(kb):
    case = {"presenting": ["sore_throat"], "context": {"age": 30}}
    answers = [{"question_id": "universal_emergency_screen", "answer": "not_sure"},
               # The other emergency screen comes next. Then the universal items one by one.
               {"question_id": "sore_throat_emergency_screen", "answer": "none"}]
    step = run(kb, case, answers)
    assert step["status"] == "question"
    assert step["question"]["kind"] == "single"
    assert step["question"]["id"] in kb.universal.screen.findings


def test_context_is_never_asked_again_and_its_effect_is_reported(kb, example):
    record = run_case(kb, example("chest_pain_angina_context"))
    asked_about = {option for q in record["questions_asked"] for option in ([q["id"]] if q["kind"] == "single" else q["answer"])}
    assert "has_angina" not in asked_about
    assert record["context"]["changed_outcome"] is True

    record = run_case(kb, example("sore_throat_weakened_immune_context"))
    assert record["outcome"]["acuity"] == "urgent"
    assert record["context"]["changed_outcome"] is True


def test_presentation_with_no_module_is_reported_as_not_covered(kb, example):
    record = run_case(kb, example("not_covered"))
    assert record["outcome"]["covered"] is False
    assert record["not_covered"]["presenting_not_recognised"] == ["ankle_injury"]
    assert questions(record) == ["universal_emergency_screen"]  # the universal screen still ran


def test_not_covered_still_catches_a_universal_red_flag(kb, example):
    case = example("not_covered")
    case["answers"] = {"stroke_signs": "yes"}
    record = run_case(kb, case)
    assert record["outcome"]["acuity"] == "emergency"
    assert record["red_flags_found"][0]["rule"] == "rf_stroke_signs"


def test_several_presenting_symptoms_are_all_used(kb, example):
    record = run_case(kb, example("chest_pain_and_sore_throat"))
    asked = questions(record)
    assert "chest_pain_emergency_screen" in asked and "sore_throat_emergency_screen" in asked
    assert record["outcome"]["acuity"] == "urgent"


def test_question_limit_ends_the_session_cautiously(example):
    from engine.questions import non_red_flag_count
    limited = load_knowledge_base()
    limited.settings.question_limit = 1
    record = run_case(limited, example("sore_throat_self_care"))
    asked = [q["id"] for q in record["questions_asked"]]
    # Red-flag questions never count towards the limit; everything else stops at it.
    assert non_red_flag_count(limited, asked) == 1
    assert record["caution"]["question_limit_reached"] is True
    # Unanswered rules count as missing information, so the outcome goes up, not down.
    assert limited.acuity_rank[record["outcome"]["acuity"]] < limited.acuity_rank["self_manageable"]
    assert record["caution"]["drove_outcome"] is True

def test_engine_keeps_nothing_between_turns(kb, example):
    """Replaying the same answers one turn at a time gives the same questions."""
    case = example("sore_throat_pharmacy")
    record = run_case(kb, case)
    answers = [{"question_id": q["id"], "answer": q["answer"]} for q in record["questions_asked"]]
    for turn in range(len(answers)):
        step = run(kb, copy.deepcopy(case), answers[:turn])
        assert step["status"] == "question"
        assert step["question"]["id"] == answers[turn]["question_id"]


def test_every_outcome_has_three_separate_fields_and_sourced_advice(kb):
    for path in EXAMPLES:
        record = run_case(kb, load_case(path))
        assert record["outcome"]["acuity"] and record["outcome"]["level_of_care"] and record["outcome"]["timeframe"]
        assert record["advice"]["look_out_for"] and record["advice"]["get_more_help_when"] and record["advice"]["where_to_go"]
        assert record["advice"]["source"]["id"]


def test_engine_has_no_network_or_random_code():
    """The engine must make no network calls and use no randomness."""
    banned = ("import requests", "import urllib", "import socket", "import http", "import random", "import secrets", "uuid")
    for path in Path(REPO_ROOT / "engine").glob("*.py"):
        text = path.read_text(encoding="utf-8")
        for word in banned:
            assert word not in text, f"{path.name} contains '{word}'"


def test_after_an_a_and_e_emergency_only_questions_that_could_mean_an_ambulance_are_asked(kb):
    # The patient volunteers that their chest feels heavy. That alone firmly means "999 or A&E".
    # The engine must still ask the chest pain emergency screen, because an answer there
    # could raise the outcome to "call 999 for an ambulance". It must ask nothing else.
    case = {"presenting": ["chest_pain"], "opening_findings": {"cp_heavy": "yes"},
            "answers": {"cp_spreads": "yes"}, "otherwise": "no"}
    record = run_case(kb, case)
    assert record["outcome"]["level_of_care"] == "emergency_ambulance"
    asked = questions(record)
    assert "chest_pain_emergency_screen" in asked
    assert "chest_pain_urgent_screen" not in asked

    # With no ambulance-level sign, it stays "999 or A&E" and stops after the emergency questions.
    record = run_case(kb, {**case, "answers": {}})
    assert record["outcome"]["level_of_care"] == "emergency_department"
    assert "chest_pain_urgent_screen" not in questions(record)


def test_the_most_urgent_outcome_still_stops_at_once(kb):
    # Signs of a stroke mean an ambulance. Nothing more is asked, not even about the chest pain.
    record = run_case(kb, {"presenting": ["chest_pain"], "answers": {"stroke_signs": "yes"}, "otherwise": "no"})
    assert questions(record) == ["universal_emergency_screen"]
    assert record["outcome"]["level_of_care"] == "emergency_ambulance"


def test_a_question_that_only_applies_after_a_diagnosis_is_never_asked_without_it(kb):
    # Someone who says they have NOT been diagnosed with angina must never be asked
    # "Is your angina worse than before?". Try many made-up patients.
    import random
    rng = random.Random(5)
    others = [f for f in kb.findings if kb.findings[f].kind not in ("presenting", "context")]
    for _ in range(rounds(200)):
        answers = {f: ("yes" if rng.random() < 0.15 else "no") for f in others}
        answers["has_angina"] = "no"
        record = run_case(kb, {"presenting": ["chest_pain"], "context": {"age": rng.choice([30, 60])},
                               "answers": answers, "otherwise": "no"})
        asked = {q["id"] for q in record["questions_asked"]}
        asked |= {f for q in record["questions_asked"] if isinstance(q["answer"], dict) for f in q["answer"]}
        assert not asked & {"angina_worse_than_usual", "angina_pain_not_settling"}
