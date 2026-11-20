"""Checks the evaluation harness itself, using made-up cases written here.

These tests never read the real vignettes in vignettes/. Those are written by a
separate session and must stay unseen by the session that writes the content.
"""

import copy
import random

import pytest
import yaml

import harness.vignette as vignette_module
from engine.runner import run_case
from harness.baseline import run_baseline
from harness.evaluate import evaluate_set
from harness.patient import build_case, make_answerer, play, what_is_true
from harness.report import render_disagreements, render_set_report
from harness.scoring import score_case
from harness.vignette import Vignette, check_vignette
from scale import consistent, rounds

QUOTE_999 = {"page": "chest_pain.txt", "quote": "you get pain that spreads to your left or right arm"}
QUOTE_SELF_CARE = {"page": "sore_throat.txt", "quote": "They normally get better by themselves within a week"}


def chest_pain_emergency() -> dict:
    return copy.deepcopy(_CHEST_PAIN_EMERGENCY)


def sore_throat_self_care() -> dict:
    return copy.deepcopy(_SORE_THROAT_SELF_CARE)


_CHEST_PAIN_EMERGENCY = {
        "id": "test_cp_emergency",
        "status": "AI-drafted, not clinically approved",
        "authored_by": "test",
        "presenting": ["chest_pain"],
        "summary": "Chest pain spreading to the arm.",
        "opening_statement": "My chest hurts and it is going down my arm.",
        "findings": {"present": ["cp_present_now", "cp_spreads"], "absent": ["sweating", "fainted"], "unknown": []},
        "context": {"basic": {"age": 60, "sex": "male"}, "full": {"age": 60, "sex": "male"}},
        "expected": {"acuity": "emergency", "level_of_care": "emergency_ambulance", "timeframe": "now"},
        "minimum_safe_acuity": "emergency",
        "red_flags": [{"description": "Pain spreading to the arm", "findings": ["cp_spreads"],
                       "minimum_acuity": "emergency", "source": QUOTE_999}],
        "safety_netting_should_cover": [{"point": "Call 999", "any_of": ["999"]}],
        "source": {"expected_outcome": QUOTE_999, "minimum_safe_acuity": QUOTE_999},
        "variants": [{"id": "test_cp_emergency_v1", "style": "says it all up front",
                      "opening_statement": "Chest pain going down my arm.", "volunteered": ["cp_spreads"]}],
}

_SORE_THROAT_SELF_CARE = {
        "id": "test_st_self_care",
        "status": "AI-drafted, not clinically approved",
        "authored_by": "test",
        "presenting": ["sore_throat"],
        "summary": "Two days of a mild sore throat.",
        "opening_statement": "I have had a sore throat for a couple of days.",
        "findings": {"present": [], "absent": ["very_high_temperature", "worried_about_symptoms"], "unknown": []},
        "context": {"basic": {"age": 30}, "full": {"age": 30}},
        "expected": {"acuity": "self_manageable", "level_of_care": "self_care", "timeframe": "not_needed"},
        "minimum_safe_acuity": "self_manageable",
        "safety_netting_should_cover": [{"point": "See a GP if it lasts over a week", "any_of": ["week"]}],
        "source": {"expected_outcome": QUOTE_SELF_CARE, "minimum_safe_acuity": QUOTE_SELF_CARE},
}


def test_good_vignette_passes_the_checks(kb):
    assert check_vignette(Vignette.model_validate(chest_pain_emergency()), kb) == []


@pytest.mark.parametrize("change, message", [
    (lambda v: v["source"]["expected_outcome"].update(quote="this sentence is not on the page at all"), "not found word for word"),
    (lambda v: v["findings"]["present"].append("made_up_finding"), "not on the question list"),
    (lambda v: v.update(status="clinically approved"), "status must be exactly"),
    (lambda v: v.update(minimum_safe_acuity="self_manageable", expected={**v["expected"], "acuity": "routine"})
     or v.update(minimum_safe_acuity="emergency"), "less urgent than minimum_safe_acuity"),
    (lambda v: v["findings"]["absent"].append("cp_spreads"), "appears more than once"),
])
def test_bad_vignette_is_refused(kb, change, message):
    data = chest_pain_emergency()
    data["red_flags"] = []
    change(data)
    problems = check_vignette(Vignette.model_validate(data), kb)
    assert any(message in problem for problem in problems), problems


def test_simulated_patient_says_no_to_anything_not_mentioned(kb):
    vignette = Vignette.model_validate(chest_pain_emergency())
    answer = make_answerer(what_is_true(kb, vignette))
    assert answer({"kind": "single", "id": "cp_spreads"}) == "yes"
    assert answer({"kind": "single", "id": "sweating"}) == "no"            # stated negative
    assert answer({"kind": "single", "id": "coughing_up_blood"}) == "no"   # not mentioned
    stressed = make_answerer(what_is_true(kb, vignette), unmentioned="not_sure")
    assert stressed({"kind": "single", "id": "coughing_up_blood"}) == "not_sure"
    assert stressed({"kind": "single", "id": "sweating"}) == "no"          # a stated negative stays "no"


def test_scoring_passes_a_case_the_engine_gets_right(kb):
    vignette = Vignette.model_validate(chest_pain_emergency())
    score = score_case(kb, vignette, play(kb, vignette))
    assert score["gates"]["red_flags_passed"] and score["gates"]["not_below_minimum_safe"]
    assert all(score["agreement"].values())
    assert score["acuity_levels_above_expected"] == 0
    assert score["interactions_before_first_red_flag"] == 2
    assert all(point["covered"] for point in score["safety_netting"]["points"])


def test_under_triage_fails_the_gate(kb):
    # The vignette says this must be an emergency, but nothing the patient says triggers one.
    data = chest_pain_emergency()
    data["findings"] = {"present": [], "absent": ["cp_present_now", "cp_spreads"], "unknown": []}
    data["red_flags"] = []
    vignette = Vignette.model_validate(data)
    score = score_case(kb, vignette, play(kb, vignette))
    assert score["gates"]["not_below_minimum_safe"] is False
    assert score["acuity_levels_above_expected"] < 0


def test_red_flag_with_no_matching_question_is_scored_on_recognition_not_the_gate(kb):
    data = chest_pain_emergency()
    data["red_flags"] = [{"description": "A danger sign the question list cannot express", "findings": [],
                          "minimum_acuity": "emergency", "source": QUOTE_999}]
    vignette = Vignette.model_validate(data)
    score = score_case(kb, vignette, play(kb, vignette))
    assert score["gates"]["red_flags"][0]["recognition"] == "no question covers this red flag"
    assert score["gates"]["red_flags_passed"] is True   # the patient was still escalated enough


def test_red_flag_gate_fails_when_the_patient_is_not_escalated_enough(kb):
    data = chest_pain_emergency()
    data["findings"] = {"present": [], "absent": ["cp_present_now", "cp_spreads"], "unknown": []}
    data["red_flags"] = [{"description": "A danger sign the question list cannot express", "findings": [],
                          "minimum_acuity": "emergency", "source": QUOTE_999}]
    vignette = Vignette.model_validate(data)
    score = score_case(kb, vignette, play(kb, vignette))
    assert score["gates"]["red_flags_passed"] is False

def test_over_triage_is_a_score_not_a_gate(kb):
    data = sore_throat_self_care()
    data["findings"]["present"] = ["worried_about_symptoms"]
    data["findings"]["absent"] = ["very_high_temperature"]
    vignette = Vignette.model_validate(data)
    score = score_case(kb, vignette, play(kb, vignette))
    assert score["acuity_levels_above_expected"] > 0
    assert score["gates"]["not_below_minimum_safe"] is True


def test_volunteering_findings_up_front_does_not_change_the_outcome(kb):
    vignette = Vignette.model_validate(chest_pain_emergency())
    base = play(kb, vignette)
    volunteered = play(kb, vignette, volunteered=["cp_spreads"])
    assert volunteered["outcome"] == base["outcome"]
    assert volunteered["burden"]["interactions"] <= base["burden"]["interactions"]


def test_baseline_reaches_the_same_outcome_as_the_engine_with_more_questions(rules_only_kb):
    kb = rules_only_kb
    rng = random.Random(7)
    module_findings = {m.presenting_finding for m in kb.modules.values()}
    others = [f for f in kb.findings if f not in module_findings and kb.findings[f].kind != "context"]
    more_questions = total = 0
    for presenting in (["chest_pain"], ["sore_throat"]):
        for _ in range(rounds(150)):
            answers = consistent(kb, {f: ("yes" if rng.random() < 0.08 else "no") for f in others}, presenting)
            total += 1
            case = {"presenting": presenting, "answers": answers, "otherwise": "no"}
            engine = run_case(kb, case)
            baseline = run_baseline(kb, {"presenting": presenting}, make_answerer(answers))
            assert baseline["outcome"] == engine["outcome"]
            more_questions += baseline["burden"]["interactions"] > engine["burden"]["interactions"]
    assert more_questions > 0.8 * total  # the baseline nearly always asks more


def test_whole_set_runs_and_reports(kb, tmp_path, monkeypatch):
    (tmp_path / "dev").mkdir()
    for data in (chest_pain_emergency(), sore_throat_self_care()):
        (tmp_path / "dev" / f"{data['id']}.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    (tmp_path / "dev" / "broken.yaml").write_text("id: broken\n", encoding="utf-8")
    monkeypatch.setattr(vignette_module, "VIGNETTE_DIR", tmp_path)

    results = evaluate_set(kb, "dev")
    summary = results["summary"]
    assert summary["cases"] == 2
    assert "broken.yaml" in results["file_problems"]            # reported, and left out of the run
    assert summary["gates"]["red_flags_passed"] == summary["gates"]["red_flags_total"] == 1
    assert summary["gates"]["cases_below_minimum_safe"] == []
    assert summary["consistency"]["repeats_identical"] == 2
    assert all(row["same_outcome"] for row in results["baseline"])
    assert all(row["same_outcome"] for row in results["variants"])

    report = render_set_report(results)
    assert "## Gates" in report and "AI-drafted and not clinically approved" in report
    assert "No disagreements" in render_disagreements([results])


def test_built_case_never_contains_the_expected_outcome(kb):
    """The engine must only be told what a patient could know, never the answer."""
    case = build_case(Vignette.model_validate(chest_pain_emergency()))
    assert set(case) <= {"presenting", "context", "opening_findings"}
