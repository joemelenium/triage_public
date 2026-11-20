"""Works out whether a rule's condition is met, not met, or cannot yet be told.

A rule's "when" is written in the YAML files as one of:

    chest_pain                      a finding id: true if the patient has it
    {all: [a, b]}                   true if every item is true
    {any: [a, b]}                   true if at least one item is true
    {not: a}                        true if the item is false

Why three answers and not two: "not sure" must never be treated as "no".
So every check returns True, False or None, where None means "unknown".
"""

YES = "yes"
NO = "no"
NOT_SURE = "not_sure"
ANSWERS = (YES, NO, NOT_SURE)


def evaluate(expression, known: dict[str, str]):
    """Return True, False or None (unknown) for a rule condition.

    `known` maps finding id -> "yes", "no" or "not_sure".
    A finding that has not been asked about is simply missing from `known`.
    """
    if isinstance(expression, str):
        answer = known.get(expression)
        if answer == YES:
            return True
        if answer == NO:
            return False
        return None  # not asked yet, or the patient said "not sure"

    key, value = next(iter(expression.items()))
    if key == "not":
        result = evaluate(value, known)
        return None if result is None else not result

    results = [evaluate(item, known) for item in value]
    if key == "all":
        if any(r is False for r in results):
            return False  # one "no" is enough to rule it out
        return None if any(r is None for r in results) else True
    # key == "any"
    if any(r is True for r in results):
        return True  # one "yes" is enough
    return None if any(r is None for r in results) else False


def open_findings(expression, known: dict[str, str]) -> list[str]:
    """Findings not yet asked about that could still settle this condition.

    Returns an empty list when the condition is already settled, or when the
    only gaps are "not sure" answers (which cannot be asked again).
    """
    if isinstance(expression, str):
        return [] if expression in known else [expression]

    key, value = next(iter(expression.items()))
    if key == "not":
        return open_findings(value, known)

    results = [evaluate(item, known) for item in value]
    settled = any(r is False for r in results) if key == "all" else any(r is True for r in results)
    if settled:
        return []
    found: list[str] = []
    for item, result in zip(value, results):
        if result is None:
            for finding_id in open_findings(item, known):
                if finding_id not in found:
                    found.append(finding_id)
    return found
