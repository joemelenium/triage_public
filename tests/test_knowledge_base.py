"""Checks that a broken knowledge base is refused with a clear message."""

import shutil

import pytest

from engine.kb import DEFAULT_KB_DIR, DEFAULT_SOURCE_LOG, KnowledgeBaseError, load_knowledge_base


def broken_copy(tmp_path, file_name: str, old: str, new: str):
    """Copy the knowledge base, change one piece of text, and return the copy's folder."""
    copy = tmp_path / "knowledge_base"
    shutil.copytree(DEFAULT_KB_DIR, copy)
    path = copy / file_name
    text = path.read_text(encoding="utf-8")
    assert old in text, f"test set-up: '{old}' not found in {file_name}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return copy


def test_real_knowledge_base_loads(kb):
    assert {"chest_pain", "sore_throat"} <= set(kb.modules)


def test_every_rule_and_default_has_advice_with_all_three_safety_netting_parts(kb):
    for advice in kb.advice.values():
        assert advice.look_out_for and advice.get_more_help_when and advice.where_to_go, advice.id


def test_item_with_unknown_source_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "entry_symptoms/sore_throat.yaml", "source: nhs_tonsillitis", "source: made_up_source")
    with pytest.raises(KnowledgeBaseError, match="unknown source 'made_up_source'"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_item_with_no_source_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "entry_symptoms/sore_throat.yaml", "    source: nhs_tonsillitis\n", "")
    with pytest.raises(KnowledgeBaseError, match="source"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_rule_using_unknown_finding_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "entry_symptoms/chest_pain.yaml", "when: cp_spreads", "when: no_such_finding")
    with pytest.raises(KnowledgeBaseError, match="unknown finding 'no_such_finding'"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_value_not_in_settings_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "entry_symptoms/chest_pain.yaml", "acuity: routine", "acuity: whenever")
    with pytest.raises(KnowledgeBaseError, match="acuity 'whenever', which is not in settings.yaml"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_misspelt_field_name_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "observations/ear_nose_throat.yaml", "  question: \"Do you have a sore throat?\"",
                       "  queston: \"Do you have a sore throat?\"")
    with pytest.raises(KnowledgeBaseError, match="ear_nose_throat.yaml"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_snomed_code_that_has_not_been_checked_is_refused(tmp_path):
    # Only codes listed in sources/snomed_codes.yaml may be used. This stops invented codes.
    copy = broken_copy(tmp_path, "observations/chest_and_heart.yaml", 'snomed: "29857009"', 'snomed: "123456789"')
    with pytest.raises(KnowledgeBaseError, match="not in the log of checked codes"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_every_snomed_code_in_use_was_checked_and_logged(kb):
    used = [f.snomed for f in kb.findings.values() if f.snomed] + [c.snomed for c in kb.conditions.values() if c.snomed]
    assert used and all(code in kb.snomed for code in used)
