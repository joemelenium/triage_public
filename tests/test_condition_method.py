"""Checks the condition-based method: likely conditions can raise the outcome."""

import random

from engine.runner import run_case
from scale import rounds


def chest_pain(age, **present):
    return {"presenting": ["chest_pain"], "context": {"age": age},
            "answers": {finding: "yes" for finding in present}, "otherwise": "no"}


def test_a_likely_serious_condition_raises_the_outcome_with_no_red_flag(kb, rules_only_kb):
    # A 60-year-old smoker whose pain came on with effort and eased with rest. No red flag fires.
    case = chest_pain(60, cp_on_exertion=True, heart_risk_factors=True)
    record = run_case(kb, case)
    assert record["red_flags_found"] == []
    assert record["outcome"]["acuity"] == "urgent"
    assert record["decided_by"]["kind"] == "likely_condition"
    assert record["conditions"]["raised_the_outcome"] is True
    assert record["conditions"]["outcome_from_rules_alone"]["acuity"] == "routine"
    assert record["possible_causes"]["causes"][0]["id"] == "angina"
    # With the method switched off, the same patient gets the rules-only outcome.
    assert run_case(rules_only_kb, case)["outcome"]["acuity"] == "routine"


def test_the_same_story_in_a_younger_patient_is_never_more_urgent_and_angina_is_less_likely(kb):
    older = run_case(kb, chest_pain(60, cp_on_exertion=True))
    younger = run_case(kb, chest_pain(30, cp_on_exertion=True))
    assert kb.acuity_rank[younger["outcome"]["acuity"]] >= kb.acuity_rank[older["outcome"]["acuity"]]
    chance = lambda r: next(c["likelihood"] for c in r["possible_causes"]["causes"] if c["id"] == "angina")
    assert chance(younger) < chance(older)


def test_a_small_chance_of_a_critical_condition_is_acted_on_but_a_small_chance_of_a_minor_one_is_not(kb):
    """The danger classes: the same small likelihood matters for a critical condition and not for a minor one."""
    from engine.condition_level import condition_based_level
    critical, minor = kb.settings.danger_classes["critical"], kb.settings.danger_classes["minor"]
    small = (critical.likely + minor.possible) / 2   # above the critical line, below the minor one
    assert critical.likely < small < minor.possible

    heart_attack = condition_based_level(kb, {"heart_attack": small, "chest_strain": 0.0, "other_cause": 1 - small})
    assert heart_attack["acuity"] == "emergency" and heart_attack["band"] == "likely"

    strain = condition_based_level(kb, {"heart_attack": 0.0, "angina": 0.0, "chest_strain": small,
                                        "other_cause": 1 - small})
    assert strain["band"] is None   # ignored


def test_a_possible_condition_gives_one_step_below_what_it_needs(kb):
    from engine.condition_level import condition_based_level
    critical = kb.settings.danger_classes["critical"]
    chance = (critical.possible + critical.likely) / 2
    level = condition_based_level(kb, {"heart_attack": chance, "other_cause": 1 - chance})
    assert level["band"] == "possible" and level["acuity"] == "urgent"   # one step below emergency


def test_several_small_chances_in_the_same_class_add_up(kb):
    from engine.condition_level import condition_based_level
    critical = kb.settings.danger_classes["critical"]
    each = critical.likely * 0.6   # each alone is below the "likely" line, together they are above it
    level = condition_based_level(kb, {"heart_attack": each, "pulmonary_embolism": each, "other_cause": 1 - 2 * each})
    assert level["band"] == "likely" and level["acuity"] == "emergency"


def test_condition_questions_are_only_asked_when_they_could_matter(kb):
    record = run_case(kb, chest_pain(60))
    asked = [q["id"] for q in record["questions_asked"]]
    assert "cp_on_exertion" in asked                 # could reveal a serious condition
    assert len(asked) <= 4 + kb.settings.max_condition_questions


def all_rules(kb):
    rules = list(kb.universal.rules)
    for module in kb.modules.values():
        rules += module.red_flags + module.outcome_rules
    return {rule.id: rule for rule in rules}


def test_likely_conditions_never_lower_the_outcome_below_a_firm_rule(kb):
    """Conditions may lower soft rules and defaults. A firm red flag is always a floor."""
    rules = all_rules(kb)
    rng = random.Random(11)
    presenting_ids = {m.presenting_finding for m in kb.modules.values()}
    others = [f for f in kb.findings if f not in presenting_ids and kb.findings[f].kind != "context"]
    lowered = 0
    for presenting in (["chest_pain"], ["sore_throat"]):
        for _ in range(rounds(150)):
            case = {"presenting": presenting, "context": {"age": rng.choice([8, 25, 50, 70])},
                    "answers": {f: ("yes" if rng.random() < 0.1 else "no") for f in others}, "otherwise": "no"}
            record = run_case(kb, case)
            for flag in record["red_flags_found"]:
                if not rules[flag["rule"]].soft:
                    assert kb.acuity_rank[record["outcome"]["acuity"]] <= kb.acuity_rank[flag["acuity"]]
            lowered += record["conditions"]["lowered_the_outcome"]
            assert len(record["questions_asked"]) <= kb.settings.question_limit
    # (Whether lowering happens depends on the random cases drawn; a specific case
    # that must be lowered is tested below.)


def test_ongoing_chest_pain_is_lowered_only_when_something_explains_it(kb):
    # Pain that is there now, after a gym session, in a 30-year-old: a pulled muscle explains it.
    explained = run_case(kb, chest_pain(30, cp_present_now=True, cp_after_injury_or_exercise=True))
    assert explained["outcome"]["acuity"] == "routine"   # lowered from emergency to the chest pain floor
    assert explained["conditions"]["lowered_the_outcome"] is True
    # The same pain with nothing to explain it stays an emergency. A run of "no" answers is not enough.
    assert run_case(kb, chest_pain(30, cp_present_now=True))["outcome"]["acuity"] == "emergency"
    # And in an older patient with risk factors it stays an emergency.
    assert run_case(kb, chest_pain(65, cp_present_now=True, heart_risk_factors=True))["outcome"]["acuity"] == "emergency"


def test_likely_conditions_never_go_below_a_default_that_is_a_floor(kb):
    # Chest pain that has stopped, started after eating: heartburn is very likely.
    # The chest pain page says to get medical advice for any chest pain, so the
    # outcome must not go below the default, however likely a minor cause is.
    case = {**chest_pain(35), "opening_findings": {"cp_after_eating": "yes"}}   # said up front
    record = run_case(kb, case)
    listed = [c["id"] for c in record["possible_causes"]["causes"] if c["id"] != "other_cause"]
    assert listed[0] == "heartburn_or_indigestion"
    assert record["outcome"]["acuity"] == "routine"
    # Ongoing pain after the gym is lowered from an emergency, but only as far as that floor.
    record = run_case(kb, chest_pain(30, cp_present_now=True, cp_after_injury_or_exercise=True))
    assert record["outcome"]["acuity"] == "routine"
    assert record["conditions"]["lowered_the_outcome"] is True


def test_a_known_diagnosis_behaving_as_usual_is_not_escalated_by_being_likely(kb):
    # Diagnosed angina, pain came on with effort and settled with rest as usual, no worse than before.
    case = {"presenting": ["chest_pain"], "context": {"age": 68, "findings": {"has_angina": "yes"}},
            "answers": {"cp_on_exertion": "yes", "cp_comes_and_goes": "yes"}, "otherwise": "no"}
    record = run_case(kb, case)
    assert record["outcome"]["acuity"] == "self_manageable"
    assert record["decided_by"]["id"] == "de_cp_stable_angina"
    # But if it is worse than usual, the sourced rule escalates it.
    case["answers"]["angina_worse_than_usual"] = "yes"
    assert run_case(kb, case)["outcome"]["acuity"] == "urgent"
