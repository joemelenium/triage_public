"""Fixed-order baseline: a STAND-IN comparator, not any real triage system.

It uses the same knowledge base and the same rules as the engine, but asks
every question for the presenting symptom one at a time, in the order the
files list them. It only stops early once an emergency outcome cannot get
any more urgent.

Comparing it with the engine isolates what adaptive questioning adds. In
"rules_only" mode both must reach the same outcome. In "rules_and_conditions"
mode the engine stops once no answer is likely to change the outcome, so the
baseline, which asks everything, can occasionally end somewhere different.
Those cases are listed in the report.
"""

from engine.kb import KnowledgeBase, findings_in
from engine.outcome import OPEN, assess, is_emergency, is_more_urgent, modules_in_play
from engine.session import apply_answer, build_record, start


def question_order(kb: KnowledgeBase, known: dict[str, str]) -> list[str]:
    """Every finding used by a rule in play, in file order: universal first, then each module."""
    rules = list(kb.universal.rules)
    for module in modules_in_play(kb, known):
        rules += module.red_flags + module.outcome_rules + module.default_exceptions
    order: list[str] = []
    for rule in rules:
        for finding_id in findings_in(rule.when):
            if finding_id not in order:
                order.append(finding_id)
    # When likely conditions can raise the outcome, ask everything about them too.
    if kb.settings.outcome_method == "rules_and_conditions":
        for module in modules_in_play(kb, known):
            for condition_id in module.conditions:
                for finding_id in kb.conditions[condition_id].findings:
                    if finding_id not in order:
                        order.append(finding_id)
    return order


def run_baseline(kb: KnowledgeBase, case: dict, answer) -> dict:
    """Ask everything in fixed order and return a record in the same shape as the engine's."""
    known, origin, not_recognised = start(kb, case)
    asked: list[dict] = []
    for finding_id in question_order(kb, known):
        before = assess(kb, known)
        # The one safety rule kept: after an emergency, stop as soon as nothing
        # left could raise the outcome further.
        if is_emergency(kb, before.stop_outcome) and not any(
                s.state == OPEN and is_more_urgent(kb, s.rule.outcome, before.stop_outcome) for s in before.rules):
            break
        if finding_id in known or not kb.askable(finding_id, known):
            continue  # never ask again for something known, or something that does not apply
        question = {
            "id": finding_id, "kind": "single", "text": kb.findings[finding_id].question,
            "options": [{"finding": finding_id, "text": kb.findings[finding_id].question}],
            "reason": "Fixed-order baseline: asks every question in the order the files list them.",
        }
        given = answer(question)
        apply_answer(question, given, known, origin)
        after = assess(kb, known)
        asked.append({
            "number": len(asked) + 1, "id": finding_id, "kind": "single", "text": question["text"],
            "reason": question["reason"], "items_shown": 1, "answer": given,
            "words_read": len(question["text"].split()),
            "outcome_before": {"acuity": before.outcome.acuity, "level_of_care": before.outcome.level_of_care},
            "outcome_after": {"acuity": after.outcome.acuity, "level_of_care": after.outcome.level_of_care},
            "changed_outcome": before.outcome.key() != after.outcome.key(),
        })
    record = build_record(kb, case, known, origin, not_recognised, asked)
    record["versions"]["mode"] = "fixed-order baseline (stand-in)"
    return record
