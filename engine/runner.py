"""Runs a whole case automatically, answering each question from a case file.

A case file lists what the patient would say. Example:

    description: "Adult with chest pain spreading to the arm"
    presenting: [chest_pain]
    context:
      age: 58
      findings: {has_angina: yes}
    answers:
      cp_spreads: yes
    otherwise: no        # the answer to anything not listed

This is a small stand-in for the simulated patient that the evaluation
harness will use.
"""

from pathlib import Path

import yaml

from .kb import KnowledgeBase
from .logic import NO
from .session import run, tidy_answer


def load_case(path) -> dict:
    with open(Path(path), encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def answer_for(question: dict, case: dict):
    """Look up the case's answer to a question."""
    answers = case.get("answers") or {}
    otherwise = tidy_answer(case.get("otherwise", NO))
    if question["kind"] == "single":
        return tidy_answer(answers.get(question["id"], otherwise))
    # A screen: give an answer for every item listed.
    return {option["finding"]: tidy_answer(answers.get(option["finding"], otherwise))
            for option in question["options"]}


def run_case(kb: KnowledgeBase, case: dict) -> dict:
    """Run a case from start to finish and return the output record."""
    return run(kb, case, [], answer_next=lambda question: answer_for(question, case))["record"]
