"""Design properties found by an independent review, kept as permanent tests.

Each test is a principle the engine must always keep, checked either on the
specific patient that once broke it or on many made-up patients.
"""

import random

import pytest

from engine.outcome import assess
from engine.runner import run_case
from scale import rounds

B = {"presenting": ["chest_pain"], "otherwise": "no"}


def acuity(kb, case):
    return kb.acuity_rank[run_case(kb, case)["outcome"]["acuity"]]   # 0 is most urgent


def danger_findings(kb):
    """Findings that are red flags, or that point to a critical or serious condition."""
    flags = {f for rule in kb.universal.rules for f in _ids(rule.when)}
    for module in kb.modules.values():
        for rule in module.red_flags:
            flags |= _ids(rule.when)
    for condition in kb.conditions.values():
        if condition.danger in ("critical", "serious"):
            flags |= {f for f, band in condition.findings.items() if band in ("supports", "strongly_supports")}
    # Only findings that point to danger and to nothing milder count: a finding that also
    # points to a milder cause can rightly explain a patient and lower the outcome.
    milder = {f for c in kb.conditions.values() if c.danger in ("moderate", "minor")
              for f, band in c.findings.items() if band in ("supports", "strongly_supports")}
    # Background history (such as "diagnosed with angina") is not a danger sign in itself.
    history = {f for f, finding in kb.findings.items() if finding.kind in ("history", "context")}
    return sorted(flags - milder - history)


def _ids(expression):
    from engine.kb import findings_in
    return set(findings_in(expression))


@pytest.mark.parametrize("presenting", [["chest_pain"], ["sore_throat"], ["chest_pain", "sore_throat"]],
                         ids=["chest pain", "sore throat", "both"])
def test_adding_a_danger_sign_never_lowers_the_outcome(any_method_kb, presenting):
    kb = any_method_kb
    rng = random.Random(31)
    danger = danger_findings(kb)
    others = [f for f in kb.findings if kb.findings[f].kind not in ("presenting", "context")]
    for _ in range(rounds(120)):
        # A few true signs, so outcomes spread across all levels (with many, nearly every
        # made-up patient already needs 999 and nothing could be lowered).
        true_signs = set(rng.sample(others, 4))
        answers = {f: ("yes" if f in true_signs else "no") for f in others}
        # The patient mentions everything that is true at the start, as a real patient
        # describing their symptoms would. This tests the decision logic. (If a second
        # main symptom is neither mentioned nor asked about, its warning signs cannot be
        # found: a limit of any engine that asks adaptively. See DECISIONS 141.)
        def case_for(truth):
            return {"presenting": presenting, "context": {"age": age},
                    "opening_findings": {f: a for f, a in truth.items() if a == "yes"},
                    "answers": truth, "otherwise": "no"}
        age = rng.choice([8, 30, 61])
        case = case_for(answers)
        before = acuity(kb, case)
        # What the patient needs with every answer known. Asking stops when no single
        # answer is likely to change the outcome, so with fewer answers the engine can
        # end up more cautious than this. A danger sign may remove that extra caution
        # (by leading to more questions), but must never take the outcome below it.
        needed = kb.acuity_rank[assess(kb, everything_known(kb, answers, presenting, age)).outcome.acuity]
        for finding in rng.sample(danger, 4):
            if answers.get(finding) == "yes":
                continue
            after = acuity(kb, case_for({**answers, finding: "yes"}))
            assert after <= max(before, needed), f"adding '{finding}' lowered the outcome: {answers}"


def everything_known(kb, answers, presenting, age):
    """Every answer known, as the patient would give it, with the patient's age.
    A yes is also a yes to every general observation above it, as in the engine."""
    from engine.kb import general_ones
    truth = {**{f: "no" for f in kb.findings}, **answers,
             **{f.id: ("yes" if f.age_range.contains(age) else "no") for f in kb.findings.values() if f.age_range},
             **{f: "yes" for f in presenting}}
    waiting = [f for f, a in truth.items() if a == "yes"]
    while waiting:
        for parent in general_ones(kb.findings[waiting.pop()]):
            if truth.get(parent) != "yes":
                truth[parent] = "yes"
                waiting.append(parent)
    return truth


def test_a_second_symptom_does_not_dilute_the_first(any_method_kb):
    kb = any_method_kb
    alone = {**B, "context": {"age": 61, "findings": {"has_angina": "no"}}, "answers": {"cp_on_exertion": "yes"}}
    both = {**alone, "presenting": ["chest_pain", "sore_throat"]}
    assert acuity(kb, both) <= acuity(kb, alone)


def test_one_symptoms_conditions_cannot_lower_another_symptoms_rule(any_method_kb):
    kb = any_method_kb
    case = {"presenting": ["chest_pain", "sore_throat"], "otherwise": "no",
            "answers": {"cp_present_now": "yes", "cough_or_runny_nose": "yes"}}
    assert run_case(kb, case)["outcome"]["acuity"] == "emergency"


def test_the_floor_holds_even_with_a_known_diagnosis(any_method_kb):
    kb = any_method_kb
    case = {**B, "context": {"age": 61, "findings": {"has_angina": "yes"}},
            "opening_findings": {"cp_present_now": "yes"}, "answers": {"cp_after_eating": "yes"}}
    assert kb.acuity_rank[run_case(kb, case)["outcome"]["acuity"]] <= kb.acuity_rank["routine"]


def test_not_sure_about_a_diagnosis_does_not_jam_the_engine(any_method_kb):
    kb = any_method_kb
    record = run_case(kb, {**B, "context": {"findings": {"has_angina": "not_sure"}}})
    assert len(record["questions_asked"]) > 2
    assert record["outcome"]["level_of_care"] != "emergency_ambulance"


def test_a_rule_held_out_of_caution_is_never_lowered(any_method_kb):
    kb = any_method_kb
    case = {**B, "context": {"age": 30, "findings": {"has_angina": "no"}},
            "answers": {"cp_present_now": "not_sure", "cp_after_injury_or_exercise": "yes"}}
    assert run_case(kb, case)["outcome"]["acuity"] == "emergency"


def test_red_flag_checks_are_never_cut_off_by_the_question_limit(any_method_kb):
    kb = any_method_kb
    # "Not sure" to every checklist means each red flag is asked on its own, which is many questions.
    case = {"presenting": ["chest_pain", "sore_throat"], "context": {"age": 40}, "otherwise": "no", "answers": {}}
    from engine.session import run
    answers = []
    while True:
        step = run(kb, case, answers)
        if step["status"] == "outcome":
            break
        question = step["question"]
        answers.append({"question_id": question["id"], "answer": "not_sure" if question["kind"] == "screen" else "no"})
    record = step["record"]
    assert record["outcome"]["level_of_care"] != "emergency_ambulance"   # nothing was left unchecked
    assert record["red_flags_found"] == []


def test_a_symptom_with_no_module_keeps_its_cautious_default_alongside_a_covered_one(any_method_kb):
    kb = any_method_kb
    case = {"presenting": ["a_symptom_this_tool_does_not_cover", "chest_pain"], "context": {"age": 30}, "otherwise": "no"}
    assert acuity(kb, case) <= kb.acuity_rank[kb.settings.not_covered.outcome.acuity]


def test_children_are_not_asked_adult_questions(any_method_kb):
    kb = any_method_kb
    record = run_case(kb, {**B, "context": {"age": 4}})
    assert not {q["id"] for q in record["questions_asked"]} & {"heart_risk_factors", "family_heart_history"}


def test_questions_that_cannot_change_anything_are_not_asked(kb):
    # A firm urgent rule has fired. Glandular fever needs less than that, so asking about it is pointless.
    record = run_case(kb, {"presenting": ["sore_throat"], "context": {"age": 30},
                           "answers": {"very_high_temperature": "yes"}, "otherwise": "no"})
    assert not {q["id"] for q in record["questions_asked"]} & {"very_tired", "swollen_neck_glands"}


def test_a_lowered_outcome_is_always_explained_as_ai_judgement(kb):
    record = run_case(kb, {**B, "context": {"age": 61, "findings": {"has_angina": "no"}},
                           "opening_findings": {"cp_present_now": "yes"},
                           "answers": {"cp_after_injury_or_exercise": "yes"}})
    assert record["conditions"]["lowered"]
    assert record["conditions"]["lowered"][0]["source"] == "AI judgement"
    assert "lowered" in record["rationale"]


def test_a_gated_question_does_not_apply_when_its_gate_is_no(any_method_kb):
    kb = any_method_kb
    case = {**B, "context": {"age": 61, "findings": {"has_angina": "no"}}}
    record = run_case(kb, case)
    absent = {f["id"]: f["from"] for f in record["findings"]["absent"]}
    assert absent["angina_worse_than_usual"].startswith("does not apply")
    assert record["caution"]["drove_outcome"] is False


def test_a_question_that_does_not_apply_is_not_evidence(kb):
    from engine.likelihood import condition_likelihoods
    module = [kb.modules["chest_pain"]]
    known = {"chest_pain": "yes", "has_angina": "no", "cp_on_exertion": "yes"}
    assert condition_likelihoods(kb, module, {**known, "angina_worse_than_usual": "no"}) == \
        condition_likelihoods(kb, module, known)


def test_evidence_that_points_equally_to_danger_cannot_explain_a_patient_away(kb):
    # Ongoing chest pain with a family history of heart disease. Family history points to
    # angina, but just as much to a heart attack, so it must not lower the outcome.
    case = {**B, "context": {"age": 61, "findings": {"has_angina": "no"}},
            "opening_findings": {"cp_present_now": "yes"}, "answers": {"family_heart_history": "yes"}}
    assert run_case(kb, case)["outcome"]["acuity"] == "emergency"
