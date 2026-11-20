"""Checks that stopping early never changes the outcome (rules-only mode).

In "rules_and_conditions" mode the engine stops when no answer is LIKELY to
change the outcome, which cannot be exact. That mode is tested in
test_condition_method.py.

The engine stops asking when no remaining question could change the outcome.
This test makes up many patients at random, and for each one compares:
  - the outcome the engine reached, asking only the questions it chose
  - the outcome the rules give when every single answer is known
They must match in full: acuity, level of care and timeframe. That includes
emergencies, where the engine keeps asking only until the outcome cannot get
any more urgent.

The random numbers use a fixed seed, so the test itself is repeatable. The
engine uses no randomness.
"""

import random

import pytest

from engine.outcome import assess
from engine.runner import run_case
from scale import consistent, rounds


@pytest.mark.parametrize("presenting", [["chest_pain"], ["sore_throat"], ["chest_pain", "sore_throat"]],
                         ids=["chest pain", "sore throat", "both"])
def test_early_stopping_never_changes_the_outcome(rules_only_kb, presenting):
    kb = rules_only_kb
    rng = random.Random(2026)
    module_findings = {m.presenting_finding for m in kb.modules.values()}
    others = [f for f in kb.findings if f not in module_findings and kb.findings[f].kind != "context"]

    for _ in range(rounds(400)):
        # A made-up patient: each finding is present about one time in eight.
        answers = consistent(kb, {f: ("yes" if rng.random() < 0.125 else "no") for f in others}, presenting)
        case = {"presenting": presenting, "answers": answers, "otherwise": "no"}
        record = run_case(kb, case)

        # Every question answered: as the patient would, "no" to anything not listed.
        everything_known = {**{f: "no" for f in kb.findings}, **answers,
                            **{f: ("yes" if f in presenting else "no") for f in module_findings}}
        full = assess(kb, everything_known).outcome

        assert record["outcome"]["acuity"] == full.acuity, answers
        assert record["outcome"]["level_of_care"] == full.level_of_care, answers
        assert record["outcome"]["timeframe"] == full.timeframe, answers
        assert record["caution"]["drove_outcome"] is False
        assert len(record["questions_asked"]) <= kb.settings.question_limit
