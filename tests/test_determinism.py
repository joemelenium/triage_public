"""Proves the engine is deterministic: the same case always gives the same record."""

import json

import pytest

from conftest import EXAMPLES
from engine.runner import load_case, run_case


def without_timing(record: dict) -> str:
    """The record as text, leaving out how long it took (the only thing allowed to vary)."""
    return json.dumps({k: v for k, v in record.items() if k != "timing"}, sort_keys=True)


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.stem)
def test_same_case_gives_identical_record_every_time(kb, path):
    case = load_case(path)
    first = without_timing(run_case(kb, case))
    for _ in range(5):
        assert without_timing(run_case(kb, case)) == first


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.stem)
def test_reloading_the_knowledge_base_changes_nothing(kb, path):
    from engine.kb import load_knowledge_base
    case = load_case(path)
    assert without_timing(run_case(load_knowledge_base(), case)) == without_timing(run_case(kb, case))
