"""Runs a triage session and builds the output record.

The engine keeps nothing between turns. Each call is given the case (presenting
symptoms and any patient context) plus all the answers so far, and works
everything out again from the start. Because the engine is deterministic, this
always gives the same result, and it means nothing a person enters has to be
stored anywhere.
"""

import time

from . import DISCLAIMER, ENGINE_VERSION
from .five_level import five_level_summary
from .kb import AI_JUDGEMENT_LABEL, KnowledgeBase, findings_in, general_ones
from .likelihood import OTHER, condition_likelihoods
from .logic import ANSWERS, NO, NOT_SURE, YES
from .outcome import FIRED, NOT_COVERED_FINDING, OPEN, STUCK, assess, is_emergency, is_more_urgent, modules_in_play
from .questions import next_question, non_red_flag_count


def tidy_answer(value):
    """YAML reads a bare yes/no as true/false. Turn those back into words."""
    if value is True:
        return YES
    if value is False:
        return NO
    return value


def start(kb: KnowledgeBase, case: dict):
    """Record what is known before any question is asked.

    Returns (known, origin, not_recognised):
      known           finding id -> yes / no / not_sure
      origin          finding id -> where the information came from
      not_recognised  presenting symptoms the knowledge base does not know
    """
    known: dict[str, str] = {}
    origin: dict[str, str] = {}
    not_recognised: list[str] = []

    for presenting in case.get("presenting", []):
        if presenting in kb.findings:
            known[presenting] = YES
            origin[presenting] = "opening statement"
        else:
            not_recognised.append(presenting)
    if not_recognised:
        known[NOT_COVERED_FINDING] = YES
        origin[NOT_COVERED_FINDING] = "opening statement"

    # Anything else the patient volunteers at the start, before being asked.
    for finding_id, answer in (case.get("opening_findings") or {}).items():
        answer = tidy_answer(answer)
        if finding_id not in kb.findings:
            raise ValueError(f"Opening statement mentions unknown finding '{finding_id}'")
        if answer not in ANSWERS:
            raise ValueError(f"Opening statement gives '{answer}' for '{finding_id}'. Use yes, no or not_sure.")
        known[finding_id] = answer
        origin[finding_id] = "opening statement"

    context = case.get("context") or {}
    for finding_id, answer in (context.get("findings") or {}).items():
        answer = tidy_answer(answer)
        if finding_id not in kb.findings:
            raise ValueError(f"Patient context mentions unknown finding '{finding_id}'")
        if answer not in ANSWERS:
            raise ValueError(f"Patient context gives '{answer}' for '{finding_id}'. Use yes, no or not_sure.")
        known[finding_id] = answer
        origin[finding_id] = "context"

    # Some findings (such as "under 5 years old") are worked out from the age.
    age = context.get("age")
    if age is not None:
        for finding in kb.findings.values():
            if finding.age_range:
                known[finding.id] = YES if finding.age_range.contains(age) else NO
                origin[finding.id] = "context"

    sex = context.get("sex")
    if sex in ("female", "male"):
        for option in ("female", "male"):
            if f"sex_{option}" in kb.findings:
                known[f"sex_{option}"] = YES if sex == option else NO
                origin[f"sex_{option}"] = "context"

    propagate(kb, known, origin, sex)
    return known, origin, not_recognised


def propagate(kb: KnowledgeBase, known: dict[str, str], origin: dict[str, str], sex: str | None = None) -> None:
    """Fill in what follows from what is known, so it is never asked.

    - a "yes" to an observation means "yes" to its parent ("severe headache" means "headache")
    - a "no" to an observation means "no" to everything under it
    - an observation for the other sex does not apply, so it is "no"
    - a question gated on another answer does not apply when that answer is "no"
    """
    changed = True
    while changed:
        changed = False
        for finding in kb.findings.values():
            answer = known.get(finding.id)
            for parent in general_ones(finding):
                if answer == YES and parent not in known:
                    known[parent], origin[parent] = YES, f"implied by '{finding.id}'"
                    changed = True
                if known.get(parent) == NO and finding.id not in known:
                    known[finding.id], origin[finding.id] = NO, f"implied by '{parent}'"
                    answer = NO
                    changed = True
            if sex and finding.sex and finding.sex != sex and finding.id not in known:
                known[finding.id], origin[finding.id] = NO, "does not apply to this sex"
                changed = True
            # A question only asked after a "yes" to another does not apply when that
            # answer is "no", so it is "no" too (never left unknown, which would look
            # like missing information).
            gate = finding.asked_only_if
            if gate and known.get(gate) == NO and finding.id not in known:
                known[finding.id], origin[finding.id] = NO, f"does not apply ('{gate}' is no)"
                changed = True


def apply_answer(question: dict, answer, known: dict[str, str], origin: dict[str, str]) -> None:
    """Record the patient's answer to a question."""
    option_ids = [option["finding"] for option in question["options"]]
    answer = tidy_answer(answer)

    if question["kind"] == "single":
        if answer not in ANSWERS:
            raise ValueError(f"Answer to '{question['id']}' must be yes, no or not_sure, not {answer!r}")
        known[option_ids[0]] = answer
        origin[option_ids[0]] = "patient"
        return

    # A screen. "not_sure" for the whole list records nothing, so each item
    # will then be asked on its own. Otherwise the answer says which items apply.
    if answer == NOT_SURE:
        return
    if answer in ("none", NO) or answer is None:
        answer = {}
    if isinstance(answer, list):
        answer = {finding_id: YES for finding_id in answer}
    if not isinstance(answer, dict):
        raise ValueError(f"Answer to screen '{question['id']}' must be a list of the items that apply, 'none' or 'not_sure'")
    for finding_id, value in answer.items():
        if finding_id not in option_ids:
            raise ValueError(f"'{finding_id}' is not one of the items in screen '{question['id']}'")
    for finding_id in option_ids:
        value = tidy_answer(answer.get(finding_id, NO))  # anything not ticked is a "no"
        if value not in ANSWERS:
            raise ValueError(f"Answer for '{finding_id}' must be yes, no or not_sure, not {value!r}")
        known[finding_id] = value
        origin[finding_id] = "patient"


def run(kb: KnowledgeBase, case: dict, answers: list[dict], answer_next=None) -> dict:
    """Work through the answers so far, then return the next question or the outcome.

    answers is a list of {"question_id": ..., "answer": ...} in the order asked.
    Returns {"status": "question", ...} or {"status": "outcome", "record": ...}.

    answer_next(question) is optional. If given, it answers each new question as it
    is asked, so a whole case runs in one pass instead of being replayed after every
    answer. The result is the same either way.
    """
    answers = list(answers)
    started = time.perf_counter()
    known, origin, not_recognised = start(kb, case)
    asked: list[dict] = []

    while True:
        assessment = assess(kb, known)
        question = next_question(kb, known, [a["id"] for a in asked], assessment,
                                 respondent=case.get("respondent", "patient"))
        if question is None:
            break
        if len(asked) >= len(answers) and answer_next is not None:
            answers.append({"question_id": question["id"], "answer": answer_next({"number": len(asked) + 1, **question})})
        if len(asked) >= len(answers):
            emergency_found = any(s.red_flag and s.state == FIRED and is_emergency(kb, s.rule.outcome)
                                  for s in assessment.rules)
            return {"status": "question", "question": {"number": len(asked) + 1, **question}, "asked_so_far": asked,
                    "possible_causes": list_possible_causes(kb, known), "emergency_evidence_found": emergency_found}

        given = answers[len(asked)]
        if given["question_id"] != question["id"]:
            raise ValueError(f"Answer {len(asked) + 1} is for '{given['question_id']}' but the engine asked '{question['id']}'")
        apply_answer(question, given["answer"], known, origin)
        propagate(kb, known, origin, (case.get("context") or {}).get("sex"))
        after = assess(kb, known)
        asked.append({
            "number": len(asked) + 1,
            "id": question["id"],
            "kind": question["kind"],
            "text": question["text"],
            "reason": question["reason"],
            "reason_code": question.get("reason_code", ""),
            "items_shown": len(question["options"]),
            "words_read": len(question["text"].split()) + (sum(len(o["text"].split()) for o in question["options"])
                                                           if question["kind"] == "screen" else 0),
            "answer": tidy_answer(given["answer"]),
            "outcome_before": _short(assessment.outcome),
            "outcome_after": _short(after.outcome),
            "changed_outcome": assessment.outcome.key() != after.outcome.key(),
        })

    if len(answers) > len(asked):
        raise ValueError("More answers were given than questions asked")

    record = build_record(kb, case, known, origin, not_recognised, asked)
    record["timing"] = {"total_ms": round((time.perf_counter() - started) * 1000, 2)}
    return {"status": "outcome", "record": record}


def list_possible_causes(kb: KnowledgeBase, known: dict[str, str]) -> list[dict]:
    """Possible causes, most likely first: each symptom's conditions weighed separately, then listed together."""
    modules = modules_in_play(kb, known)
    likelihoods: dict[str, float] = {}
    for module in modules:
        for condition_id, chance in condition_likelihoods(kb, [module], known).items():
            likelihoods[condition_id] = max(likelihoods.get(condition_id, 0.0), chance)
    causes = sorted(likelihoods.items(), key=lambda item: -item[1])  # sorted() keeps file order on ties

    def cause_entry(condition_id, likelihood):
        if condition_id == OTHER:
            return {"id": condition_id, "name": "Something not on the list", "common_name": "Something not on the list",
                    "likelihood": round(likelihood, 2), "acuity_needed": None, "snomed": ""}
        condition = kb.conditions[condition_id]
        return {"id": condition_id, "name": condition.medical_name or condition.name, "common_name": condition.name,
                "likelihood": round(likelihood, 2), "acuity_needed": condition.acuity_needed, "snomed": condition.snomed}

    return [cause_entry(condition_id, likelihood) for condition_id, likelihood in causes]


def _short(outcome) -> dict:
    return {"acuity": outcome.acuity, "level_of_care": outcome.level_of_care}


def _label(kb: KnowledgeBase, scale: str, level_id: str) -> str:
    return next(level.label for level in getattr(kb.settings, scale) if level.id == level_id)


def build_record(kb: KnowledgeBase, case: dict, known, origin, not_recognised, asked) -> dict:
    # If the question limit cut the session short, anything still unsettled
    # counts as missing information and is treated cautiously.
    so_far = assess(kb, known)
    still_to_ask = any(s.state == OPEN and (s.red_flag or is_more_urgent(kb, s.rule.outcome, so_far.stop_outcome))
                       for s in so_far.rules)
    limit_reached = (non_red_flag_count(kb, [a["id"] for a in asked]) >= kb.settings.question_limit
                     and not is_emergency(kb, so_far.stop_outcome) and still_to_ask)
    final = assess(kb, known, final=limit_reached)
    decided = final.decided_by
    outcome = decided.outcome
    modules = modules_in_play(kb, known)

    if is_emergency(kb, final.stop_outcome):
        stopped_because = "An emergency outcome was reached, and nothing left to ask could make it more urgent."
    elif limit_reached:
        stopped_because = "The question limit was reached."
    else:
        stopped_because = "No remaining question was likely to change the outcome."

    def finding_entry(finding_id):
        return {"id": finding_id, "label": kb.findings[finding_id].label,
                "snomed": kb.findings[finding_id].snomed, "from": origin[finding_id]}

    red_flags = [{
        "rule": s.rule.id,
        "description": s.rule.description,
        "acuity": s.rule.outcome.acuity,
        "level_of_care": s.rule.outcome.level_of_care,
        "source": kb.source_details(s.rule.source),
        # The findings that make up this red flag, each with its SNOMED CT code where one has been checked.
        "findings": [{"id": f, "label": kb.findings[f].label, "snomed": kb.findings[f].snomed}
                     for f in findings_in(s.rule.when) if known.get(f) == YES],
    } for s in final.rules if s.red_flag and s.state == FIRED]

    # Red flags that could not be ruled out because information was missing.
    unsettled_flags = [{
        "rule": s.rule.id,
        "description": s.rule.description,
        "acuity": s.rule.outcome.acuity,
    } for s in final.rules if s.red_flag and s.state == STUCK]

    possible_causes = list_possible_causes(kb, known)

    advice = kb.advice[decided.advice]

    # Would the outcome be different without the patient context?
    context_ids = [f for f in known if origin[f] == "context"]
    without_context = {f: a for f, a in known.items() if f not in context_ids}
    outcome_with = assess(kb, known, ignore_missing=True).outcome
    outcome_without = assess(kb, without_context, ignore_missing=True).outcome

    record = {
        "disclaimer": DISCLAIMER,
        "case": {"presenting": case.get("presenting", []), "context": case.get("context") or {}},
        "outcome": {
            "acuity": outcome.acuity,
            "acuity_label": _label(kb, "acuity", outcome.acuity),
            "level_of_care": outcome.level_of_care,
            "level_of_care_label": _label(kb, "level_of_care", outcome.level_of_care),
            "timeframe": outcome.timeframe,
            "timeframe_label": _label(kb, "timeframe", outcome.timeframe),
            "timeframe_detail": outcome.timeframe_detail,
            "covered": final.covered,
        },
        "decided_by": {
            "overruled": ({"id": decided.overruled.id, "description": decided.overruled.description,
                           "outcome": _short(decided.overruled.outcome),
                           "source": kb.source_details(decided.overruled.source)} if decided.overruled else None),
            "kind": decided.kind,
            "id": decided.id,
            "description": decided.description,
            "source": kb.source_details(decided.source),
            "note": decided.note,
        },
        # Whether the conditions that look likely raised the outcome above what the rules alone give.
        "conditions": {
            "raised_the_outcome": decided.kind == "likely_condition" and kb.urgency(outcome) < kb.urgency(final.rule_outcome),
            "lowered_the_outcome": kb.urgency(outcome) > kb.urgency(final.rule_outcome),
            # Each soft rule or default that likely conditions lowered, and why. Listed even
            # when something else (such as a floor) then decided the outcome.
            "lowered": [{"rule": c.overruled.id, "rule_outcome": _short(c.overruled.outcome),
                         "lowered_to": c.outcome.acuity, "why": c.description, "source": "AI judgement"}
                        for c in final.lowered if kb.urgency(c.overruled.outcome) < kb.urgency(outcome)],
            "outcome_from_rules_alone": _short(final.rule_outcome),
            "method": kb.settings.outcome_method,
        },
        "red_flags_found": red_flags,
        "findings": {
            "present": [finding_entry(f) for f, a in known.items() if a == YES],
            "absent": [finding_entry(f) for f, a in known.items() if a == NO],
            "unknown": [finding_entry(f) for f, a in known.items() if a == NOT_SURE],
        },
        "possible_causes": {
            "label": "Ranked most likely first. Not a diagnosis. Likelihoods are AI estimates. They can raise or lower the outcome, above the floor set by firm rules.",
            "causes": possible_causes,
        },
        "advice": {
            "what_to_do": advice.what_to_do,
            "look_out_for": advice.look_out_for,
            "get_more_help_when": advice.get_more_help_when,
            "where_to_go": advice.where_to_go,
            "self_care": advice.self_care,
            "source": kb.source_details(advice.source),
        },
        "would_change_outcome": _what_would_change(kb, known, origin, final.outcome),
        "questions_asked": asked,
        # Interaction burden: how many times the patient was asked something,
        # and how many separate items they had to read across those questions.
        "burden": {"interactions": len(asked), "items_shown": sum(a["items_shown"] for a in asked),
                   "words_read": sum(a["words_read"] for a in asked)},
        "stopped_because": stopped_because,
        "caution": {
            "drove_outcome": decided.cautious,
            "missing_information": [kb.findings[f].label for f in decided.missing],
            "red_flags_not_ruled_out": unsettled_flags,
            "question_limit_reached": limit_reached,
        },
        "context": {
            "provided": [finding_entry(f) for f in context_ids],
            "changed_outcome": outcome_with.key() != outcome_without.key(),
            "outcome_without_context": _short(outcome_without),
        },
        "not_covered": {
            "presenting_not_recognised": not_recognised,
            "no_module_for_presentation": not final.covered,
        },
        "versions": {
            "engine": ENGINE_VERSION,
            "knowledge_base": kb.settings.kb_version,
            "knowledge_base_status": kb.settings.status,
            "mode": "structured",
        },
    }
    record["rationale"] = _rationale(kb, record, decided)
    record["five_level_triage"] = five_level_summary(kb, record)

    return record


def _what_would_change(kb: KnowledgeBase, known, origin, outcome) -> list[dict]:
    """For each answer given, would a different answer have changed the outcome?"""
    changes = []
    for finding_id, answer in known.items():
        if origin[finding_id] == "opening statement":
            continue  # the presenting symptom itself is not in question
        for other in (YES, NO):
            if other == answer:
                continue
            new_outcome = assess(kb, {**known, finding_id: other}).outcome
            if new_outcome.key() != outcome.key():
                changes.append({
                    "finding": finding_id,
                    "label": kb.findings[finding_id].label,
                    "answer_given": answer,
                    "if_answer_had_been": other,
                    "outcome_would_be": _short(new_outcome),
                    "note": "Based on the other answers as given. More questions might then have been asked.",
                })
    return changes


def _rationale(kb: KnowledgeBase, record: dict, decided) -> str:
    """A plain-English explanation of the outcome."""
    outcome = record["outcome"]
    parts = [f"Outcome: {outcome['acuity_label']}, {outcome['level_of_care_label'].lower()}, "
             f"timeframe: {outcome['timeframe_label'].lower()}."]

    source = record["decided_by"]["source"]["title"]
    if decided.kind == "not_covered":
        parts.append("This tool has no module for this presenting symptom. No emergency red flag was found, "
                     "so it gave a cautious standard outcome. It did not guess.")
    elif decided.kind == "module_default" and record["conditions"]["lowered"]:
        item = record["conditions"]["lowered"][0]
        parts.append(f"A rule would have given {item['rule_outcome']['acuity']}, but it was lowered: {item['why']} "
                     f"This rests on AI estimates. The outcome cannot go below the floor for this symptom, so this "
                     f"applies: {decided.description} (source: {source}).")
    elif decided.kind == "module_default":
        parts.append(f"No rule for a more urgent outcome applied, so the standard outcome was used: "
                     f"{decided.description} (source: {source}).")
    elif decided.kind == "lowered_by_conditions":
        parts.append(f"A rule would have given a more urgent outcome, but a likely milder cause explains the "
                     f"symptoms: {decided.description} This rests on AI estimates of how likely each cause is.")
    elif decided.kind == "likely_condition":
        parts.append(f"The level was set by the conditions that look likely: {decided.description}. "
                     f"The rules alone would have given {record['conditions']['outcome_from_rules_alone']['acuity']}. "
                     f"These likelihoods are estimates.")
    elif decided.kind == "default_exception":
        parts.append(f"No rule for a more urgent outcome applied, and this applied in place of the standard "
                     f"outcome: {decided.description} (source: {source}).")
    elif decided.cautious:
        missing = ", ".join(record["caution"]["missing_information"]) or "some answers"
        parts.append(f"Information was missing ({missing}), so this rule could not be ruled out: "
                     f"{decided.description} (source: {source}). To be safe, the more urgent outcome was chosen.")
    else:
        parts.append(f"This rule applied: {decided.description} (source: {source}).")

    if decided.kind not in ("lowered_by_conditions", "module_default") and record["conditions"]["lowered"]:
        for item in record["conditions"]["lowered"]:
            parts.append(f"A rule would have given {item['rule_outcome']['acuity']}, but it was lowered: {item['why']} "
                         f"This rests on AI estimates.")
    if record["caution"]["question_limit_reached"]:
        parts.append("The question limit was reached before every relevant question was asked.")

    # What would have changed the outcome. Answers of "yes" or "not sure" are
    # named first, because they are what the outcome rests on.
    changes = record["would_change_outcome"]
    rests_on = [c for c in changes if c["answer_given"] != NO]
    answered_no = [c for c in changes if c["answer_given"] == NO]
    if rests_on:
        examples = [f"'{c['label']}' had been {c['if_answer_had_been'].replace('_', ' ')} "
                    f"({c['outcome_would_be']['acuity']})" for c in rests_on[:3]]
        parts.append("The outcome would have been different if " + "; or if ".join(examples) + ".")
    if answered_no:
        parts.append(f"A yes to any of {len(answered_no)} items answered no would also have changed the outcome, "
                     f"for example '{answered_no[0]['label']}'.")
    if not changes:
        parts.append("No single different answer would have changed this outcome.")

    if record["context"]["provided"]:
        if record["context"]["changed_outcome"]:
            parts.append("Patient context changed the outcome.")
        else:
            parts.append("Patient context was used but did not change the outcome.")
    return " ".join(parts)
