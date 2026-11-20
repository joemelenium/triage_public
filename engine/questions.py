"""Chooses the next question, or decides that no more are needed.

The order is:
  1. Red flags, most serious level first. At each level:
       - screens: one "do any of these apply?" question covering several red flags
       - then any single red-flag questions left over (for example ones that
         only apply to people with a known condition)
     Every red flag is checked, because each one must be detected.
  2. Other questions, one at a time, and only if the answer could raise the
     outcome. The one most likely to change the outcome is asked first.
     Then questions that help tell the possible conditions apart, while one is
     likely enough to change the outcome.
     Then, if the default outcome still stands, any question that decides a
     sourced exception to that default (which would lower the outcome).
  3. Stop when no remaining question could change the outcome.

After an emergency outcome:
  - if it is already the most urgent outcome there is (an ambulance), the engine
    asks nothing further
  - otherwise it asks only the emergency red-flag questions that could still
    raise the outcome to the most urgent one, then stops
"""

from .kb import KnowledgeBase, findings_in
from .likelihood import OTHER, chance_of_yes, condition_likelihoods
from .logic import NO, YES
from .outcome import OPEN, Assessment, assess, is_emergency, is_more_urgent, modules_in_play


def next_question(kb: KnowledgeBase, known: dict[str, str], asked_ids: list[str], assessment: Assessment,
                  respondent: str = "patient") -> dict | None:
    """Return the next question as a dictionary, or None to stop.

    respondent is "patient" or "carer". For a carer, questions use the carer wording where there is one.
    """
    question = _next_question(kb, known, asked_ids, assessment)
    # Carer wording replaces a full question asked on its own. Checklist lines are
    # written so they read the same for a patient or a carer, so they stay as they are.
    if question and respondent == "carer" and question["kind"] == "single":
        carer = kb.findings[question["id"]].question_carer
        if carer:
            question["text"] = question["options"][0]["text"] = carer
    return question


# Why a question was asked, as a short code (modelled on the reason codes that
# condition-based engines publish), alongside the plain-words reason.
RED_FLAG_SCREEN = "red_flag_screen"     # a checklist of alarming signs
RED_FLAG = "red_flag"                   # a single alarming sign that must be checked
CHECKLIST = "checklist"                 # several signs that each lead to a GP or other non-urgent care
RULE = "rule"                           # needed to decide a sourced rule
CONDITION = "condition"                 # most likely to change how likely a dangerous condition is
DEFAULT_EXCEPTION = "default_exception" # could lower the outcome through a sourced exception


def _next_question(kb: KnowledgeBase, known: dict[str, str], asked_ids: list[str], assessment: Assessment) -> dict | None:
    # "Emergency" here means one firmly shown by the patient's own answers. An
    # emergency that is only suspected from likely conditions, or that comes from a
    # soft rule, does not stop the questions: more answers are exactly what is
    # needed to confirm it or rule it out.
    emergency = is_emergency(kb, assessment.stop_outcome)
    if emergency and kb.urgency(assessment.stop_outcome) == (0, 0):
        return None  # already the most urgent outcome there is: never ask more

    modules = modules_in_play(kb, known)
    likelihoods = _combined_likelihoods(kb, modules, known)

    # ---- 1. Red flags, most serious level first -------------------------------
    # Screens not yet asked that still have something to ask about.
    screens = [(kb.universal.screen, "everyone")] + [(s, m.name.lower()) for m in modules for s in m.screens]
    all_pending = [(screen, who) for screen, who in screens
                   if screen.id not in asked_ids
                   and any(f not in known and kb.askable(f, known) for f in screen.findings)]
    # Checklists below the red-flag levels wait until after the red flags (part 2).
    pending_screens = [(screen, who) for screen, who in all_pending if is_red_flag_level(kb, screen.level)]
    # Red-flag rules that still need an answer.
    open_flags = [s for s in assessment.rules if s.red_flag and s.state == OPEN]

    if emergency:
        # Help is needed now. Only ask what could still raise the outcome, for
        # example from "go to A&E" to "call 999 for an ambulance". Nothing else.
        open_flags = [s for s in open_flags if is_more_urgent(kb, s.rule.outcome, assessment.stop_outcome)]
        could_raise = {f for s in open_flags for f in s.open}
        pending_screens = [(screen, who) for screen, who in pending_screens
                           if any(f in could_raise for f in screen.findings)]
        if not open_flags and not pending_screens:
            return None

    levels = [kb.acuity_rank[screen.level] for screen, _ in pending_screens]
    levels += [kb.acuity_rank[s.rule.outcome.acuity] for s in open_flags]
    if levels:
        top = min(levels)  # 0 is the most urgent level

        for screen, who in pending_screens:
            if kb.acuity_rank[screen.level] == top:
                remaining = [f for f in screen.findings if f not in known and kb.askable(f, known)]
                return {
                    "id": screen.id,
                    "kind": "screen",
                    "reason_code": RED_FLAG_SCREEN,
                    "text": screen.question,
                    # Short lines in a checklist, so there is less to read. The full question is
                    # used when an observation is asked on its own.
                    "options": [{"finding": f, "text": kb.findings[f].checklist_text or kb.findings[f].question}
                                for f in remaining],
                    "reason": f"Red-flag screen for {who} ({screen.level} level): every red flag must be checked, "
                              f"so they are asked together to keep the number of questions down.",
                }

        # No screen left at this level, so ask single red-flag questions.
        # For each rule, ask about its first unanswered finding. Rules are written
        # so that the first finding is the natural one to ask first.
        choices = _first_open_findings([s for s in open_flags if kb.acuity_rank[s.rule.outcome.acuity] == top])
        finding_id, status = max(choices, key=lambda c: chance_of_yes(kb, likelihoods, c[0]))
        chance = chance_of_yes(kb, likelihoods, finding_id)
        where = status.module.name.lower() if status.module else "everyone"
        return _single(kb, finding_id, RED_FLAG,
                       f"Red-flag check for {where}: needed to decide \"{status.rule.description}\" "
                       f"({status.rule.outcome.acuity}). Of the red-flag questions left at this level, "
                       f"it is the most likely to be yes (about {_percent(chance)}).")

    if emergency:
        return None  # after an emergency, only the red-flag questions above are ever asked

    # The question limit applies from here. Red-flag questions above never count
    # against it: every red flag must be checked, and there are only so many.
    if non_red_flag_count(kb, asked_ids) >= kb.settings.question_limit:
        return None

    # ---- 2. Other questions, only for rules that could raise the outcome --------
    # A checklist of non-urgent signs (for example "see a GP" signs) is one
    # question instead of several, so it comes first, if it could still raise
    # the outcome.
    for screen, who in all_pending:
        if not is_red_flag_level(kb, screen.level) and \
                kb.acuity_rank[screen.level] < kb.acuity_rank[assessment.stop_outcome.acuity]:
            remaining = [f for f in screen.findings if f not in known and kb.askable(f, known)]
            return {
                "id": screen.id,
                "kind": "screen",
                "reason_code": CHECKLIST,
                "text": screen.question,
                "options": [{"finding": f, "text": kb.findings[f].checklist_text or kb.findings[f].question}
                            for f in remaining],
                "reason": f"Checklist for {who} ({screen.level} level): each of these would change the advice, "
                          f"so they are asked together to keep the number of questions down.",
            }

    useful = [s for s in assessment.rules
              if not s.red_flag and s.state == OPEN and is_more_urgent(kb, s.rule.outcome, assessment.stop_outcome)]
    if not useful:
        # No rule could raise the outcome. Next, ask about possible conditions,
        # if an answer is likely enough to change the outcome.
        question = _condition_question(kb, known, asked_ids, modules, likelihoods, assessment)
        if question:
            return question
        # Nothing could raise the outcome. If the default outcome decided it, check
        # whether a sourced exception to that default applies, which would lower it.
        for module, exception, still_open in assessment.open_exceptions:
            if assessment.decided_by.id == f"{module.id}_default" and \
                    is_more_urgent(kb, assessment.outcome, exception.outcome):
                return _single(kb, still_open[0], DEFAULT_EXCEPTION,
                               f"This could lower the outcome. It helps decide \"{exception.description}\" "
                               f"({exception.outcome.acuity}).")
        return None  # 3. nothing left could change the outcome

    def score(choice):
        finding_id, status = choice
        chance = chance_of_yes(kb, likelihoods, finding_id)
        changes_if_yes = assess(kb, {**known, finding_id: YES}).outcome.key() != assessment.outcome.key()
        changes_if_no = assess(kb, {**known, finding_id: NO}).outcome.key() != assessment.outcome.key()
        chance_of_change = chance * changes_if_yes + (1 - chance) * changes_if_no
        # Highest chance of change first. Ties go to the more serious rule.
        # max() keeps the earliest item on a full tie, so the file order decides.
        urgency = kb.urgency(status.rule.outcome)
        return (chance_of_change, -urgency[0], -urgency[1])

    choices = _first_open_findings(useful)
    finding_id, status = max(choices, key=score)
    return _single(kb, finding_id, RULE,
                   f"Of the questions left, this is the most likely to change the outcome "
                   f"(about {_percent(score((finding_id, status))[0])} chance). "
                   f"It helps decide \"{status.rule.description}\" ({status.rule.outcome.acuity}).")


def _condition_question(kb, known, asked_ids, modules, likelihoods, assessment) -> dict | None:
    """The best question for telling the possible conditions apart, if one is worth asking.

    A question is worth asking if a yes or a no would noticeably move the amount
    of serious illness in play, up or down. The one expected to move it most is
    asked first.
    """
    if kb.settings.outcome_method != "rules_and_conditions":
        return None

    # Each main symptom has its own allowance of condition questions, so one symptom
    # cannot use up the questions another needs. The overall question limit still applies.
    candidates: list[str] = []
    for module in modules:
        own = [f for c in module.conditions for f in kb.conditions[c].findings]
        already = sum(1 for asked in asked_ids if asked in own and not _used_by_a_rule(kb, modules, asked))
        if already >= kb.settings.max_condition_questions:
            continue
        for finding_id in own:
            if finding_id not in candidates:
                candidates.append(finding_id)
    if not candidates:
        return None

    classes = kb.settings.danger_classes
    floor_rank = kb.acuity_rank[assessment.stop_outcome.acuity]

    def risk(with_known) -> float:
        """How much danger is in play that could still matter.

        Each condition's likelihood times its danger class weight, worked out for
        each symptom separately. Only conditions that would need more than the
        outcome the answers already guarantee are counted: learning more about a
        condition that could not change the outcome is not worth a question.
        """
        total = 0.0
        for module in modules:
            for condition_id, chance in condition_likelihoods(kb, [module], with_known).items():
                if condition_id == OTHER:
                    continue
                condition = kb.conditions[condition_id]
                if kb.acuity_rank[condition.acuity_needed] < floor_rank:
                    total += chance * classes[condition.danger].weight
        return total

    now = risk(known)
    best, best_shift = None, 0.0
    askable_candidates: list[str] = []
    for finding_id in candidates:
        to_ask = kb.to_ask_for(finding_id, known)
        if to_ask and to_ask not in askable_candidates:
            askable_candidates.append(to_ask)
    for finding_id in askable_candidates:
        shift_if_yes = abs(risk({**known, finding_id: YES}) - now)
        shift_if_no = abs(risk({**known, finding_id: NO}) - now)
        # An answer that would change the outcome outright always counts.
        if assess(kb, {**known, finding_id: YES}).outcome.key() != assessment.outcome.key():
            shift_if_yes += 1.0
        if assess(kb, {**known, finding_id: NO}).outcome.key() != assessment.outcome.key():
            shift_if_no += 1.0
        if max(shift_if_yes, shift_if_no) < kb.settings.min_risk_shift_to_ask:
            continue
        chance = chance_of_yes(kb, likelihoods, finding_id)
        expected_shift = chance * shift_if_yes + (1 - chance) * shift_if_no
        if expected_shift > best_shift:  # ">" keeps the earliest on a tie, so file order decides
            best, best_shift = finding_id, expected_shift
    if best is None:
        return None
    return _single(kb, best, CONDITION,
                   "This helps tell the possible conditions apart. The answer could make a serious condition "
                   "noticeably more or less likely.")


def red_flag_question_ids(kb: KnowledgeBase) -> set[str]:
    """Checklists, and observations used by any red-flag rule. Asking these never counts towards the limit."""
    ids = {kb.universal.screen.id}
    for rule in kb.universal.rules:
        ids |= set(findings_in(rule.when))
    for module in kb.modules.values():
        ids |= {s.id for s in module.screens if is_red_flag_level(kb, s.level)}
        for rule in module.red_flags:
            ids |= set(findings_in(rule.when))
    return ids


def is_red_flag_level(kb: KnowledgeBase, level: str) -> bool:
    """Emergency and urgent checklists are red-flag screens. Lower ones are ordinary questions."""
    return kb.acuity_rank[level] <= kb.acuity_rank["urgent"]


def non_red_flag_count(kb: KnowledgeBase, asked_ids) -> int:
    red_flag_ids = red_flag_question_ids(kb)
    return sum(1 for asked in asked_ids if asked not in red_flag_ids)


def _combined_likelihoods(kb, modules, known) -> dict[str, float]:
    """Each symptom's conditions are weighed separately. For choosing questions, take
    the highest likelihood any symptom gives each condition."""
    combined: dict[str, float] = {}
    for module in modules:
        for condition_id, chance in condition_likelihoods(kb, [module], known).items():
            combined[condition_id] = max(combined.get(condition_id, 0.0), chance)
    return combined


def _used_by_a_rule(kb, modules, finding_id) -> bool:
    rules = list(kb.universal.rules)
    for module in modules:
        rules += module.red_flags + module.outcome_rules + module.default_exceptions
    return any(finding_id in findings_in(rule.when) for rule in rules)


def _first_open_findings(statuses) -> list[tuple]:
    """One (finding, rule status) pair per finding, in file order."""
    choices, seen = [], set()
    for status in statuses:
        finding_id = status.open[0]
        if finding_id not in seen:
            seen.add(finding_id)
            choices.append((finding_id, status))
    return choices


def _single(kb: KnowledgeBase, finding_id: str, reason_code: str, reason: str) -> dict:
    return {
        "id": finding_id,
        "kind": "single",
        "reason_code": reason_code,
        "text": kb.findings[finding_id].question,
        "options": [{"finding": finding_id, "text": kb.findings[finding_id].question}],
        "reason": reason,
    }


def _percent(value: float) -> str:
    return f"{round(value * 100)}%"
