"""Self-tests: can each condition card be recognised from its own contents?

For each condition, a "textbook patient" is built from the card: its entry
symptom, and yes to the observations the card says point most strongly to it,
no to everything else. The engine should then list that condition among the
top three, and give an outcome at least as urgent as the condition needs.

This is circular (the patient comes from the card itself), so passing proves
little. Failing is useful: it shows broken links, a card too weak to stand out,
or a rule that hides the condition.
"""

import multiprocessing
import os

from engine.kb import KnowledgeBase
from engine.likelihood import OTHER
from engine.runner import run_case

STRONG = ("strongly_supports", "supports")


# A typical age for a condition, from the age bands its card says make it more common.
AGE_FOR_BAND = {"age_under_1_month": 0.05, "age_under_3_months": 0.15, "age_under_6_months": 0.3, "age_under_1": 0.5,
                "age_under_2": 1, "age_under_5": 2, "age_under_16": 10, "age_40_or_over": 50, "age_45_or_over": 58,
                "age_65_or_over": 72}


def _typical_age(kb: KnowledgeBase, card) -> float:
    """The age band that raises the card's starting chance the most, else 35.
    A band that LOWERS it (for example "very rare under 16") is not a typical age."""
    chance = kb.settings.prevalence_bands
    raising = [p for p in card.prevalence_when
               if p.finding in AGE_FOR_BAND and chance[p.prevalence] > chance[card.prevalence]]
    best = max(raising, key=lambda p: chance[p.prevalence], default=None)  # max() keeps the first on a tie
    return AGE_FOR_BAND[best.finding] if best else 35


def textbook_patient(kb: KnowledgeBase, condition_id: str, entry: str) -> dict:
    """A patient with this condition's strongest features, which they mention up front.

    Volunteering them tests whether the CARD is recognisable, separately from
    whether the engine chooses to ask about them. A specific feature brings its
    general one with it, and any question it is gated on is answered yes.
    """
    card = kb.conditions[condition_id]
    pointing = sorted((f for f, band in card.findings.items() if band in STRONG and f in kb.findings),
                      key=lambda f: (card.findings[f] != "strongly_supports", f))[:4]
    volunteered: dict[str, str] = {}
    for finding_id in pointing:
        current = finding_id
        while current:
            volunteered[current] = "yes"
            finding = kb.findings[current]
            if finding.asked_only_if and kb.findings[finding.asked_only_if].age_range is None:
                volunteered[finding.asked_only_if] = "yes"
            current = finding.parent
    volunteered.pop(entry, None)
    if card.diagnosed_by:
        volunteered[card.diagnosed_by] = "no"   # test recognition of a new case, not a known one
    return {"presenting": [entry], "context": {"age": _typical_age(kb, card)},
            "opening_findings": volunteered, "otherwise": "no"}


def _one_selftest(kb: KnowledgeBase, condition_id: str, entry: str) -> dict:
    card = kb.conditions[condition_id]
    record = run_case(kb, textbook_patient(kb, condition_id, entry))
    # Rank among the entry symptom's own conditions. Other symptoms the patient
    # mentions bring in their own causes (back pain brings in back strain), which
    # say nothing about whether this card is recognisable.
    own = {c for m in kb.modules.values() if m.presenting_finding == entry for c in m.conditions}
    listed = [c["id"] for c in record["possible_causes"]["causes"] if c["id"] != OTHER and c["id"] in own]
    rank = listed.index(condition_id) + 1 if condition_id in listed else None
    urgent_enough = kb.acuity_rank[record["outcome"]["acuity"]] <= kb.acuity_rank[card.acuity_needed]
    return {"condition": condition_id, "entry": entry, "rank": rank,
            "recognised": rank is not None and rank <= 3, "urgent_enough": urgent_enough,
            "outcome": record["outcome"]["acuity"], "needed": card.acuity_needed}


_WORKER_KB = None


def _worker(job):
    return _one_selftest(_WORKER_KB, *job)


def run_selftests(kb: KnowledgeBase, workers: int | None = None) -> list[dict]:
    """Run every condition's self-test, spread over the computer's processors.
    Results come back in the same fixed order however many processors are used."""
    global _WORKER_KB
    jobs = [(condition_id, entry) for condition_id, card in kb.conditions.items() for entry in card.entry_symptoms]
    workers = workers or os.cpu_count() or 1
    if workers == 1:
        return [_one_selftest(kb, *job) for job in jobs]
    _WORKER_KB = kb  # shared with the worker processes when they start
    with multiprocessing.get_context("fork").Pool(workers) as pool:
        return pool.map(_worker, jobs, chunksize=8)
