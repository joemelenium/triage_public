"""Works out the level of care that the likely conditions call for.

This is the "condition-based" half of the engine, modelled on how
condition-based triage engines work. It balances risk using danger classes
(settings.yaml). Each possible condition has a class, set by how bad it would
be to miss it, and each class has two lines:

  likely    above this chance, the outcome is the level the condition needs
  possible  above this chance, the outcome is one step below that level

The lines are far lower for dangerous conditions. So a 4% chance of something
life-threatening is acted on, while a 4% chance of something minor is ignored.

Conditions in the same class that need the same level are added together, so
several small chances of something dangerous count as one bigger chance.

A condition the patient is already diagnosed with is left out. It is known and
being managed, and the rules about it getting worse decide the outcome.

Every likelihood behind this is an AI estimate. That is intended: this engine
is a mock-up for evaluation and is never for clinical use.
"""

from .kb import KnowledgeBase
from .likelihood import OTHER

LIKELY = "likely"
POSSIBLE = "possible"


def condition_based_level(kb: KnowledgeBase, likelihoods: dict[str, float], known: dict[str, str] | None = None) -> dict:
    """Return the level the conditions call for, and why.

    Returns {"acuity", "band", "danger", "chance", "conditions", "unknown"}.
    band is "likely", "possible", or None when nothing reaches a line (the level is then self-care).
    """
    least = kb.settings.acuity[-1].id
    unknown = likelihoods.get(OTHER, 0.0)

    # Group the conditions by (danger class, level needed), in file order.
    groups: dict[tuple[str, str], list[tuple[str, float]]] = {}
    for condition_id, chance in likelihoods.items():
        if condition_id == OTHER:
            continue
        condition = kb.conditions[condition_id]
        if known and condition.diagnosed_by and known.get(condition.diagnosed_by) == "yes":
            continue  # already diagnosed and managed: the rules about it getting worse decide
        groups.setdefault((condition.danger, condition.acuity_needed), []).append((condition_id, chance))

    found = []
    for (danger, needed), members in groups.items():
        lines = kb.settings.danger_classes[danger]
        total = sum(chance for _, chance in members)
        if total >= lines.likely:
            acuity, band = needed, LIKELY
        elif total >= lines.possible:
            # One step less urgent than the condition would need, but never below the least urgent level.
            acuity, band = kb.settings.acuity[min(kb.acuity_rank[needed] + 1, len(kb.settings.acuity) - 1)].id, POSSIBLE
        else:
            continue
        members = sorted(members, key=lambda item: -item[1])  # sorted() keeps file order on ties
        found.append({"acuity": acuity, "band": band, "danger": danger, "needed": needed,
                      "chance": total, "conditions": members[:3], "unknown": unknown})

    if not found:
        likely = sorted(((c, p) for c, p in likelihoods.items() if c != OTHER), key=lambda item: -item[1])[:3]
        return {"acuity": least, "band": None, "danger": None, "needed": least, "chance": 0.0,
                "conditions": likely, "unknown": unknown}

    # Most urgent wins. On a tie, a "likely" beats a "possible", then the bigger chance, then file order.
    return min(found, key=lambda f: (kb.acuity_rank[f["acuity"]], f["band"] != LIKELY, -f["chance"]))


def describe(kb: KnowledgeBase, level: dict) -> str:
    names = ", ".join(f"{kb.conditions[c].name} (about {_percent(p)})" for c, p in level["conditions"])
    if level["band"] == LIKELY:
        return (f"A {level['danger']} condition that needs {level['needed']} care is likely enough to act on "
                f"(about {_percent(level['chance'])} in total): {names}")
    if level["band"] == POSSIBLE:
        return (f"A {level['danger']} condition that would need {level['needed']} care is possible "
                f"(about {_percent(level['chance'])} in total), so the outcome is one step below that: {names}")
    return f"No condition that needs more than self-care is likely enough to act on. Most likely: {names}"


def _percent(value: float) -> str:
    return f"{value * 100:.0f}%" if value >= 0.01 else "under 1%"
