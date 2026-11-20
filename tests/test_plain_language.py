"""Checks that text a patient sees is in plain language."""

from statistics import median

from engine.kb import DEFAULT_SOURCE_LOG, KnowledgeBaseError, load_knowledge_base
import re

from engine.plain_language import (MAX_GRADE_LIMIT, MEDIAN_GRADE_LIMIT, MIN_WORDS_FOR_MAX, patient_facing_texts,
                                   reading_grade)
from test_knowledge_base import broken_copy

import pytest


def test_reading_level_is_low_enough(kb):
    grades = [(reading_grade(text), where, text) for where, text in patient_facing_texts(kb)]
    assert median(grade for grade, _, _ in grades) <= MEDIAN_GRADE_LIMIT
    too_hard = [f"{where}: grade {grade:.1f}: {text}" for grade, where, text in grades
                if grade > MAX_GRADE_LIMIT and len(re.findall(r"[A-Za-z']+", text)) >= MIN_WORDS_FOR_MAX]
    assert not too_hard, "\n".join(too_hard)


def test_an_unexplained_medical_word_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "observations/ear_nose_throat.yaml", 'question: "Do you have a sore throat?"',
                       'question: "Do you have pharyngitis or a sore throat? Is there stridor?"')
    with pytest.raises(KnowledgeBaseError, match="uses 'stridor' without explaining it"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_a_word_the_nhs_a_to_z_says_to_avoid_is_refused(tmp_path):
    copy = broken_copy(tmp_path, "observations/ear_nose_throat.yaml", 'question: "Do you have a sore throat?"',
                       'question: "Do you have a sore throat and a fever?"')
    with pytest.raises(KnowledgeBaseError, match="uses 'fever'. The NHS A to Z of health writing says to use 'high temperature'"):
        load_knowledge_base(copy, DEFAULT_SOURCE_LOG)


def test_an_avoided_word_is_allowed_alongside_the_plain_one(tmp_path):
    copy = broken_copy(tmp_path, "observations/ear_nose_throat.yaml", 'question: "Do you have a sore throat?"',
                       'question: "Do you have a sore throat, or are you feeling sick (nausea)?"')
    load_knowledge_base(copy, DEFAULT_SOURCE_LOG)   # no error
