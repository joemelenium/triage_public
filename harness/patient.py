"""The simulated patient: answers the engine's questions from a vignette.

It answers:
  yes       to anything the vignette lists as present
  no        to anything the vignette lists as absent
  not sure  to anything the vignette lists as unknown
  no        to anything the vignette does not mention

A separate stress test changes the last line to "not sure".
"""

from engine.kb import KnowledgeBase, general_ones
from engine.logic import NO, NOT_SURE, YES
from engine.session import run
from harness.vignette import Vignette


def what_is_true(kb: KnowledgeBase, vignette: Vignette) -> dict[str, str]:
    """Everything the patient could say about themselves, as finding id -> answer."""
    truth: dict[str, str] = {}

    # History in the patient's record is true of them, so they can say it if asked.
    truth.update(vignette.context.full.findings)

    # The patient knows their own age, even when the engine was not told it.
    age = vignette.context.full.age if vignette.context.full.age is not None else vignette.context.basic.age
    if age is not None:
        for finding in kb.findings.values():
            if finding.age_range:
                truth[finding.id] = YES if finding.age_range.contains(age) else NO

    truth.update({f: YES for f in vignette.findings.present})
    truth.update({f: NO for f in vignette.findings.absent})
    # "Unknown" wins over the record: the record may know it, but this patient cannot say it.
    truth.update({f: NOT_SURE for f in vignette.findings.unknown})
    # Someone with a more specific symptom has the general one too: a "barking cough"
    # is a cough. So a "yes" to a child observation means "yes" to its parent.
    changed = True
    while changed:
        changed = False
        for finding_id, answer in list(truth.items()):
            parents = general_ones(kb.findings[finding_id]) if finding_id in kb.findings else []
            for parent in parents:
                if answer == YES and truth.get(parent) != YES:
                    truth[parent] = YES
                    changed = True
    return truth


def build_case(vignette: Vignette, layer: str = "full", volunteered=()) -> dict:
    """What the engine is told before any question: presenting symptoms, context and anything volunteered."""
    context = getattr(vignette.context, layer)
    case = {
        "presenting": list(vignette.presenting),
        "context": {key: value for key, value in
                    (("age", context.age), ("sex", context.sex), ("findings", dict(context.findings)))
                    if value not in (None, {})},
    }
    if volunteered:
        case["opening_findings"] = {f: (YES if f in vignette.findings.present else NO) for f in volunteered}
    return case


def make_answerer(truth: dict[str, str], unmentioned: str = NO):
    """Return a function that answers any question the engine asks."""
    def answer(question: dict):
        if question["kind"] == "single":
            return truth.get(question["id"], unmentioned)
        return {option["finding"]: truth.get(option["finding"], unmentioned) for option in question["options"]}
    return answer


def play(kb: KnowledgeBase, vignette: Vignette, layer: str = "full", unmentioned: str = NO, volunteered=()) -> dict:
    """Run one vignette through the engine and return the output record."""
    case = build_case(vignette, layer, volunteered)
    answer = make_answerer(what_is_true(kb, vignette), unmentioned)
    return run(kb, case, [], answer_next=answer)["record"]
