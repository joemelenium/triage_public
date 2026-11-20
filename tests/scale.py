"""How many random patients the property tests try.

The default is a quarter of the full count, so the suite runs in reasonable time
on a small machine. For a thorough run (for example on a bigger server):

    TRIAGE_TEST_SCALE=100 python3 -m pytest
"""

import os

SCALE = int(os.environ.get("TRIAGE_TEST_SCALE", "25"))


def rounds(full: int) -> int:
    """The number of rounds to run, out of the full count."""
    return max(5, full * SCALE // 100)


def consistent(kb, answers: dict, presenting: list) -> dict:
    """Make a random made-up patient possible: a "yes" means "yes" to its general
    observations too, and nothing is true under a main symptom the patient does not have."""
    from engine.kb import general_ones
    module_findings = {m.presenting_finding for m in kb.modules.values()}

    def all_general(finding_id):
        """Every general observation above this one, all the way up."""
        found, waiting = set(), [finding_id]
        while waiting:
            for parent in general_ones(kb.findings[waiting.pop()]):
                if parent not in found:
                    found.add(parent)
                    waiting.append(parent)
        return found

    truth = dict(answers)
    for finding_id, answer in answers.items():
        if answer != "yes":
            continue
        above = all_general(finding_id)
        if above & (module_findings - set(presenting)):
            truth[finding_id] = "no"          # under a main symptom they do not have
        else:
            truth.update({parent: "yes" for parent in above - module_findings})
    return truth
