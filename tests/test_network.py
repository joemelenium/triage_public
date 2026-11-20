"""Checks the network features: observation hierarchy, carer wording, sex filter,
question reason codes, the five-level summary, and network validation."""

import copy

import pytest

from engine.kb import DEFAULT_SOURCE_LOG, Finding, KnowledgeBaseError, Rule, load_knowledge_base
from engine.runner import run_case
from test_knowledge_base import broken_copy


@pytest.fixture
def kb_with_child():
    """The real network plus a made-up child observation and a rule that uses only the child."""
    kb = load_knowledge_base()
    kb.findings["very_tired_cannot_get_up"] = Finding(
        id="very_tired_cannot_get_up", label="So tired they cannot get out of bed",
        question="Are you so tired that you cannot get out of bed?", kind="symptom",
        parent="very_tired", relation="severity", source="ai_judgement")
    rule = Rule(id="test_rule_child", description="Too tired to get out of bed", when="very_tired_cannot_get_up",
                outcome={"acuity": "soon", "level_of_care": "general_practice", "timeframe": "few_days"},
                advice="advice_sore_throat_gp", source="ai_judgement")
    kb.modules["sore_throat"].outcome_rules.append(rule)
    return kb


def asked(record):
    return [q["id"] for q in record["questions_asked"]]


def test_a_child_is_never_asked_before_its_parent(kb_with_child):
    record = run_case(kb_with_child, {"presenting": ["sore_throat"], "context": {"age": 30},
                                      "answers": {"very_tired": "yes", "very_tired_cannot_get_up": "yes"}, "otherwise": "no"})
    order = asked(record)
    assert order.index("very_tired") < order.index("very_tired_cannot_get_up")
    assert record["outcome"]["acuity"] == "soon"


def test_a_no_to_the_parent_rules_out_the_child_without_asking(kb_with_child):
    record = run_case(kb_with_child, {"presenting": ["sore_throat"], "context": {"age": 30}, "otherwise": "no"})
    assert "very_tired_cannot_get_up" not in asked(record)
    absent = {f["id"]: f["from"] for f in record["findings"]["absent"]}
    assert absent.get("very_tired_cannot_get_up", "").startswith("implied by")
    assert record["caution"]["drove_outcome"] is False   # a rule that cannot apply is not "missing information"


def test_a_yes_to_the_child_implies_the_parent(kb_with_child):
    record = run_case(kb_with_child, {"presenting": ["sore_throat"], "context": {"age": 30},
                                      "opening_findings": {"very_tired_cannot_get_up": "yes"}, "otherwise": "no"})
    present = {f["id"]: f["from"] for f in record["findings"]["present"]}
    assert present["very_tired"].startswith("implied by")
    assert "very_tired" not in asked(record)


def test_carer_wording_is_used_for_questions_asked_on_their_own(kb):
    kb = copy.deepcopy(kb)
    kb.findings["has_angina"].question_carer = ("Has a doctor told them they have angina? Angina is chest pain "
                                                "caused by narrowed blood vessels to the heart.")
    from engine.session import run
    case = {"presenting": ["chest_pain"], "respondent": "carer"}
    answers = [{"question_id": "universal_emergency_screen", "answer": "none"},
               {"question_id": "chest_pain_emergency_screen", "answer": "none"}]
    step = run(kb, case, answers)
    assert step["question"]["id"] == "has_angina"
    assert step["question"]["text"].startswith("Has a doctor told them")
    # The same question for the patient themselves keeps the usual wording.
    step = run(kb, {**case, "respondent": "patient"}, answers)
    assert step["question"]["text"] == kb.findings["has_angina"].question


def test_checklists_use_short_lines(kb):
    from engine.session import run
    step = run(kb, {"presenting": ["chest_pain"]}, [])
    texts = {o["finding"]: o["text"] for o in step["question"]["options"]}
    assert texts["stroke_signs"] == kb.findings["stroke_signs"].checklist_text
    assert len(texts["stroke_signs"].split()) < len(kb.findings["stroke_signs"].question.split())

def test_an_observation_for_the_other_sex_is_never_asked(kb):
    kb = copy.deepcopy(kb)
    kb.findings["very_tired"].sex = "female"
    male = run_case(kb, {"presenting": ["sore_throat"], "context": {"age": 20, "sex": "male"},
                         "answers": {"swollen_neck_glands": "yes"}, "otherwise": "no"})
    assert "very_tired" not in asked(male)
    assert {f["id"]: f["from"] for f in male["findings"]["absent"]}["very_tired"] == "does not apply to this sex"


def test_every_question_has_a_reason_code(kb):
    record = run_case(kb, {"presenting": ["chest_pain"], "context": {"age": 61},
                           "answers": {"cp_on_exertion": "yes"}, "otherwise": "no"})
    codes = {q["reason_code"] for q in record["questions_asked"]}
    assert codes and "" not in codes
    assert "red_flag_screen" in codes and "condition" in codes


@pytest.mark.parametrize("case, level, root", [
    ({"presenting": ["chest_pain"], "answers": {"stroke_signs": "yes"}}, "emergency_ambulance", "emergency_evidence_present"),
    ({"presenting": ["sore_throat"], "context": {"age": 30}}, "self_care", "self_care_sufficient"),
    ({"presenting": ["a_symptom_this_tool_does_not_cover"]}, "consultation_24", "diagnosis_unknown"),
    ({"presenting": ["chest_pain"], "context": {"age": 61, "findings": {"has_angina": "no"}},
      "answers": {"cp_on_exertion": "yes"}}, "consultation_24", "consultation_condition_likely"),
])
def test_five_level_summary(kb, case, level, root):
    record = run_case(kb, {"otherwise": "no", **case})
    assert record["five_level_triage"]["triage_level"] == level
    assert record["five_level_triage"]["root_cause"] == root


def test_conditions_belong_to_entry_symptoms_through_their_cards(kb):
    assert "heart_attack" in kb.modules["chest_pain"].conditions
    assert "quinsy" in kb.modules["sore_throat"].conditions
    assert all(kb.conditions[c].body_system for c in kb.conditions)


def test_a_loop_of_parents_is_refused(tmp_path):
    loop = ("\n- id: loop_a\n  label: \"A\"\n  question: \"A?\"\n  kind: symptom\n  parent: loop_b\n"
            "  relation: severity\n  source: nhs_chest_pain\n"
            "\n- id: loop_b\n  label: \"B\"\n  question: \"B?\"\n  kind: symptom\n  parent: loop_a\n"
            "  relation: severity\n  source: nhs_chest_pain\n")
    copy_dir = broken_copy(tmp_path, "observations/general.yaml", "", "")   # an unchanged copy
    path = copy_dir / "observations" / "general.yaml"
    path.write_text(path.read_text().rstrip("\n") + "\n" + loop)
    with pytest.raises(KnowledgeBaseError, match="loop of parents"):
        load_knowledge_base(copy_dir, DEFAULT_SOURCE_LOG)


def test_a_condition_card_whose_file_name_does_not_match_is_refused(tmp_path):
    copy_dir = broken_copy(tmp_path, "conditions/ear_nose_throat/quinsy.yaml", "id: quinsy\n", "id: not_quinsy\n")
    with pytest.raises(KnowledgeBaseError, match="file name must match"):
        load_knowledge_base(copy_dir, DEFAULT_SOURCE_LOG)


def test_a_condition_for_an_entry_symptom_with_no_file_is_refused(tmp_path):
    copy_dir = broken_copy(tmp_path, "conditions/ear_nose_throat/quinsy.yaml",
                           "entry_symptoms: [sore_throat]", "entry_symptoms: [sore_throat, a_symptom_with_no_entry_file]")
    with pytest.raises(KnowledgeBaseError, match="no file in entry_symptoms"):
        load_knowledge_base(copy_dir, DEFAULT_SOURCE_LOG)


def test_also_part_of_works_like_a_second_parent(kb):
    """'Vomiting' is part of 'diarrhoea or vomiting' (its parent) and of 'feel sick or
    been sick' (also_part_of). A yes means yes to both; a no to either means no to it."""
    from engine.session import propagate
    known, origin = {"vomiting": "yes"}, {"vomiting": "answer"}
    propagate(kb, known, origin, None)
    assert known["diarrhoea_or_vomiting"] == "yes" and known["nausea_or_vomiting"] == "yes"
    known, origin = {"nausea_or_vomiting": "no"}, {"nausea_or_vomiting": "answer"}
    propagate(kb, known, origin, None)
    assert known["vomiting"] == "no"
