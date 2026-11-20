"""Works out the triage outcome.

The outcome is the most urgent of three things:

  1. FIRM: red flags and other firm rules that fired, any rule that cannot be
     settled because information is missing (when unsure, go up), a default that
     the source makes a floor, and the cautious default for a symptom this tool
     does not cover.
  2. RAISED: for each presenting symptom, the level its likely conditions call
     for (see condition_level.py).
  3. SOFT: soft rules and ordinary defaults. Each is kept as it is, unless a
     milder condition for the same symptom explains the patient, in which case
     it is lowered to the level that condition needs.

Because the outcome is the most urgent of these, adding a danger sign can raise
it but cannot lower it. Lowering only ever replaces a soft rule, and never goes
below anything firm or anything the likely conditions call for.

In "rules_only" mode, only 1 and 3 (unlowered) are used.
"""

from dataclasses import dataclass, field

from .condition_level import condition_based_level, describe
from .kb import AI_JUDGEMENT, KnowledgeBase, Module, Outcome, Rule
from .likelihood import condition_likelihoods
from .logic import NOT_SURE, YES, evaluate, open_findings

# A finding the session adds when a main symptom has no module.
NOT_COVERED_FINDING = "presenting_not_covered"
from .kb import findings_in

FIRED = "fired"            # the rule's condition is met
RULED_OUT = "ruled_out"    # the rule's condition is not met
OPEN = "open"              # cannot tell yet, and there are still questions that would settle it
STUCK = "stuck"            # cannot tell, and nothing more can be asked (for example "not sure")


@dataclass
class RuleStatus:
    rule: Rule
    module: Module | None      # None for the universal red flags
    red_flag: bool
    state: str
    open: list[str] = field(default_factory=list)   # findings still to ask about


@dataclass
class Candidate:
    """Something that could set the outcome: a rule, or a default."""
    kind: str                  # red_flag, outcome_rule, module_default or not_covered
    id: str
    description: str
    outcome: Outcome
    advice: str
    source: str
    note: str = ""
    cautious: bool = False     # True when chosen because information was missing
    soft: bool = False         # True when the conditions that look likely may lower it
    missing: list[str] = field(default_factory=list)
    module_id: str | None = None          # the symptom this belongs to (None for universal)
    overruled: "Candidate | None" = None  # for a lowered outcome: the rule or default it replaced


@dataclass
class Assessment:
    rules: list[RuleStatus]
    decided_by: Candidate
    covered: bool              # False when no module covers the presenting symptom
    # Exceptions to a default that cannot be settled yet: (module, exception, findings still to ask)
    open_exceptions: list[tuple] = field(default_factory=list)
    # What the rules alone give, before likely conditions are taken into account.
    rule_decided_by: Candidate | None = None

    # The outcome that the patient's own answers firmly establish. This is what
    # decides when to stop asking. A soft rule does not count: likely conditions
    # may still lower it, so more questions are worth asking.
    stop_outcome: Outcome | None = None
    # Soft rules or defaults that likely conditions lowered, whether or not the lowered
    # version ended up deciding the outcome. Kept so the record can always say so.
    lowered: list = field(default_factory=list)

    @property
    def rule_outcome(self) -> Outcome:
        return (self.rule_decided_by or self.decided_by).outcome

    @property
    def outcome(self) -> Outcome:
        return self.decided_by.outcome


def modules_in_play(kb: KnowledgeBase, known: dict[str, str]) -> list[Module]:
    """Every module whose presenting symptom the patient has. There can be several."""
    return [m for m in kb.modules.values() if known.get(m.presenting_finding) == YES]


def assess(kb: KnowledgeBase, known: dict[str, str], final: bool = False, ignore_missing: bool = False) -> Assessment:
    """Work out the outcome from what is known so far.

    final=True          the session is ending, so any rule still unsettled counts
                        as missing information and is treated cautiously.
    ignore_missing=True only count rules that have definitely fired. Used to
                        compare outcomes with and without patient context.
    """
    modules = modules_in_play(kb, known)

    # Gather every rule that applies, in a fixed order: universal first, then each module.
    listed: list[tuple[Rule, Module | None, bool]] = [(rule, None, True) for rule in kb.universal.rules]
    for module in modules:
        listed += [(rule, module, True) for rule in module.red_flags]
        listed += [(rule, module, False) for rule in module.outcome_rules]

    statuses: list[RuleStatus] = []
    for rule, module, red_flag in listed:
        result = evaluate(rule.when, known)
        if result is True:
            statuses.append(RuleStatus(rule, module, red_flag, FIRED))
        elif result is False:
            statuses.append(RuleStatus(rule, module, red_flag, RULED_OUT))
        else:
            # Only findings that may be asked now count as open. A question that only
            # makes sense after a "yes" to another (for example a diagnosis) waits for it.
            still_open = _askable_open(kb, rule.when, known)
            state = OPEN if (still_open and not final) else STUCK
            statuses.append(RuleStatus(rule, module, red_flag, state, still_open))

    candidates: list[Candidate] = []
    for status in statuses:
        if status.state == FIRED or (status.state == STUCK and not ignore_missing):
            rule = status.rule
            missing = []
            if status.state == STUCK:
                missing = [f for f in findings_in(rule.when) if known.get(f, NOT_SURE) == NOT_SURE]
            candidates.append(Candidate(
                kind="red_flag" if status.red_flag else "outcome_rule",
                id=rule.id, description=rule.description, outcome=rule.outcome,
                advice=rule.advice, source=rule.source, note=rule.note,
                cautious=status.state == STUCK, missing=missing, soft=rule.soft,
                module_id=status.module.id if status.module else None,
            ))

    open_exceptions: list[tuple] = []
    for module in modules:
        # The default outcome, unless a sourced exception to it definitely applies.
        # An exception only applies when no rule for this symptom has fired: it describes
        # a patient for whom nothing else is going on. An exception that cannot be
        # settled is not applied: when unsure, stay higher.
        any_fired = any(s.state == FIRED and s.module is module for s in statuses)
        chosen = None
        for exception in ([] if any_fired else module.default_exceptions):
            result = evaluate(exception.when, known)
            if result is True:
                chosen = exception
                break
            if result is None:
                still_open = _askable_open(kb, exception.when, known)
                if still_open:
                    open_exceptions.append((module, exception, still_open))
        if chosen:
            candidates.append(Candidate("default_exception", chosen.id, chosen.description,
                                        chosen.outcome, chosen.advice, chosen.source, chosen.note, soft=True,
                                        module_id=module.id))
        else:
            default = module.default
            # A default is "soft" (likely conditions may lower it) unless the source makes it a floor.
            candidates.append(Candidate("module_default", f"{module.id}_default", default.description,
                                        default.outcome, default.advice, default.source, default.note,
                                        soft=not default.floor, module_id=module.id))

    # A main symptom this tool does not cover keeps its cautious default, even when
    # another symptom that is covered comes with it.
    if not modules or known.get(NOT_COVERED_FINDING) == YES:
        fallback = kb.settings.not_covered
        candidates.append(Candidate("not_covered", "not_covered", "A main symptom that this tool does not cover",
                                    fallback.outcome, fallback.advice, fallback.source, fallback.note))

    by_rules = _most_urgent(kb, candidates)
    # What the patient's answers firmly establish: everything except what likely
    # conditions could still lower. A rule held only out of caution counts as firm,
    # because missing information cannot be explained away.
    firm = [c for c in candidates if not c.soft or c.cautious]
    least = Outcome(acuity=kb.settings.acuity[-1].id, level_of_care=kb.settings.level_of_care[-1].id,
                    timeframe=kb.settings.timeframe[-1].id)
    firm_outcome = _most_urgent(kb, firm).outcome if firm else least

    if not modules or kb.settings.outcome_method != "rules_and_conditions":
        return Assessment(statuses, by_rules, covered=bool(modules), open_exceptions=open_exceptions,
                          rule_decided_by=by_rules, stop_outcome=by_rules.outcome)

    # ---- Likely conditions, worked out separately for each symptom ---------------
    # Two symptoms can have two different causes, so each symptom's possible
    # conditions are weighed on their own, and can only lower that symptom's rules.
    in_fired_rules = {f for s in statuses if s.state == FIRED for f in findings_in(s.rule.when)}
    raised: list[Candidate] = []
    lowerable: dict[str, list[tuple]] = {}
    for module in modules:
        likelihoods = condition_likelihoods(kb, [module], known)
        level = condition_based_level(kb, likelihoods, known)
        entry = kb.settings.condition_outcomes[level["acuity"]]
        care = entry.level_of_care
        if level["band"] == "likely" and level["conditions"]:
            # A condition that needs a particular kind of care (such as a dentist) says so on its card.
            care = kb.conditions[level["conditions"][0][0]].level_of_care or care
        raised.append(Candidate(
            kind="likely_condition", id=f"likely_condition_{level['acuity']}", description=describe(kb, level),
            outcome=Outcome(acuity=level["acuity"], level_of_care=care, timeframe=entry.timeframe,
                            timeframe_detail="Set by the conditions that look likely"),
            advice=entry.advice, source=AI_JUDGEMENT, module_id=module.id,
            note="Likelihoods and danger classes are AI estimates. This engine is a mock-up and is not for clinical use."))

        # The milder conditions that actually explain this patient: likely enough, and
        # pointed to by something the patient said yes to. A string of "no" answers is
        # not enough, and the finding that triggered a rule cannot also explain it away.
        # If the cause is probably something not on the list, nothing is explained.
        if level["unknown"] >= kb.settings.unknown_cause_threshold:
            continue
        # The evidence must also be DISTINGUISHING: it must point to the milder
        # condition more than to any condition here that needs more urgent care.
        # A finding that points just as much to something dangerous (for example a
        # family history of heart disease, which points to angina and to a heart
        # attack) cannot be used to explain the patient towards the milder one.
        def strength(condition_id, finding_id):
            band = kb.conditions[condition_id].findings.get(finding_id)
            return kb.settings.support_bands[band] if band in ("supports", "strongly_supports") else 0.0

        def distinguishing(condition_id, finding_id):
            needed = kb.acuity_rank[kb.conditions[condition_id].acuity_needed]
            mine = strength(condition_id, finding_id)
            return all(strength(other, finding_id) < mine for other in module.conditions
                       if other != condition_id and kb.acuity_rank[kb.conditions[other].acuity_needed] < needed)

        lowerable[module.id] = [
            (condition_id, finding_id) for condition_id, chance in likelihoods.items()
            if condition_id in kb.conditions and chance >= kb.settings.min_likelihood_to_explain
            for finding_id, band in kb.conditions[condition_id].findings.items()
            if known.get(finding_id) == YES and finding_id not in in_fired_rules
            and band in ("supports", "strongly_supports") and distinguishing(condition_id, finding_id)]

    # ---- Soft rules and defaults: lowered only on their own evidence ---------------
    pool = list(firm) + raised
    for candidate in candidates:
        if not candidate.soft or candidate.cautious:
            continue
        # Explaining conditions for this candidate's own symptom that need less than it does.
        explaining = [(c, f) for c, f in lowerable.get(candidate.module_id, [])
                      if kb.acuity_rank[kb.conditions[c].acuity_needed] > kb.acuity_rank[candidate.outcome.acuity]]
        if not explaining:
            pool.append(candidate)
            continue
        # Lower only as far as the most urgent of the explaining conditions needs.
        condition_id, finding_id = min(explaining, key=lambda cf: kb.acuity_rank[kb.conditions[cf[0]].acuity_needed])
        target = kb.conditions[condition_id].acuity_needed
        entry = kb.settings.condition_outcomes[target]
        pool.append(Candidate(
            kind="lowered_by_conditions", id=f"lowered_{candidate.id}",
            description=(f"\"{candidate.description}\" would give {candidate.outcome.acuity}, but it is explained by "
                         f"{kb.conditions[condition_id].name}, because the patient said yes to "
                         f"\"{kb.findings[finding_id].label}\". So the outcome is {target}."),
            outcome=Outcome(acuity=target, level_of_care=entry.level_of_care, timeframe=entry.timeframe,
                            timeframe_detail="Set by a likely milder cause"),
            advice=entry.advice, source=AI_JUDGEMENT, module_id=candidate.module_id, overruled=candidate,
            note="Lowered by likely conditions. Likelihoods are AI estimates. Not for clinical use."))

    return Assessment(statuses, _most_urgent(kb, pool), covered=True, open_exceptions=open_exceptions,
                      rule_decided_by=by_rules, stop_outcome=firm_outcome,
                      lowered=[c for c in pool if c.kind == "lowered_by_conditions"])


def _askable_open(kb: KnowledgeBase, expression, known: dict[str, str]) -> list[str]:
    """The questions that could still settle a rule, in order. A child observation is
    represented by its parent, and a gated question by its gate, until those are known."""
    result: list[str] = []
    for finding_id in open_findings(expression, known):
        to_ask = kb.to_ask_for(finding_id, known)
        if to_ask and to_ask not in result:
            result.append(to_ask)
    return result


def _most_urgent(kb: KnowledgeBase, options: list[Candidate]) -> Candidate:
    """Most urgent wins. Ties: sourced before AI judgement, definite before cautious, then file order."""
    order = sorted(range(len(options)), key=lambda i: (kb.urgency(options[i].outcome),
                                                       options[i].source == AI_JUDGEMENT, options[i].cautious, i))
    return options[order[0]]


def is_more_urgent(kb: KnowledgeBase, a: Outcome, b: Outcome) -> bool:
    return kb.urgency(a) < kb.urgency(b)


def is_emergency(kb: KnowledgeBase, outcome: Outcome) -> bool:
    """True when the outcome is at the top of the acuity scale."""
    return kb.acuity_rank[outcome.acuity] == 0
