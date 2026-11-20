"""Estimates how likely each possible condition is, given what is known.

Every number used here is AI judgement. This engine is a mock-up for testing an
evaluation, never for clinical use.

Two methods, chosen by "inference_method" in settings.yaml:

single_cause
  Naive Bayes over the candidate conditions plus "something not on the list".
  It assumes exactly one of them explains the symptoms, so the likelihoods add
  up to 1. Simple and robust.

noisy_or
  A Bayesian network of the kind used for medical diagnosis networks, and the
  closest published equivalent to the "modified Bayesian networks" that
  condition-based engines describe. Each condition is present or not, with its
  own starting chance, so several can be present at once. Each condition that
  is present can cause an observation, with the strength on its card, and every
  observation also has a small chance of happening for no listed reason (the
  "leak"). Evidence for one condition can "explain away" an observation and so
  make another condition less likely. Likelihoods are each condition's own
  chance and do not add up to 1. "Something not on the list" is the chance that
  none of the listed conditions is present.

  The calculation is exact (the "Quickscore" method), so results are the same
  every time. Its cost doubles with each "yes" answer that bears on the
  conditions, so at most MAX_POSITIVE of those are used (the strongest).

  Limitation: in this method a link can only make an observation MORE likely.
  A link marked "argues against" is ignored here. Content that needs that
  meaning should link the condition to the opposite observation instead.
"""

import math

import numpy as np

MAX_POSITIVE = 14

from .kb import KnowledgeBase, Module
from .logic import NO, YES

OTHER = "other_cause"  # stands for "something not on the list"


def _chance_given_cause(kb: KnowledgeBase, condition_id: str, finding_id: str) -> float:
    """How often someone with this cause would say yes to this finding."""
    if condition_id == OTHER:
        return kb.settings.background_chance
    band = kb.conditions[condition_id].findings.get(finding_id)
    return kb.settings.support_bands[band] if band else kb.settings.background_chance


def _prior(kb: KnowledgeBase, condition_id: str, known: dict[str, str]) -> float:
    """How common the cause is, allowing for things like age."""
    if condition_id == OTHER:
        return kb.settings.other_cause_prevalence
    condition = kb.conditions[condition_id]
    bands = kb.settings.prevalence_bands
    band = condition.prevalence
    for override in condition.prevalence_when:
        needed = [override.finding, *override.also]
        answers = [known.get(f) for f in needed]
        if all(a == YES for a in answers):
            band = override.prevalence
            break  # first match wins, so the order in the file is the tie-break
        unknown_age = [a is None and kb.findings[f].age_range is not None for f, a in zip(needed, answers)]
        if any(unknown_age) and all(a == YES or u for a, u in zip(answers, unknown_age)):
            # No age was given. Use whichever starting chance is higher, to be cautious.
            if bands[override.prevalence] > bands[band]:
                band = override.prevalence
    return bands[band]


def condition_likelihoods(kb: KnowledgeBase, modules: list[Module], known: dict[str, str]) -> dict[str, float]:
    """Return {condition id: likelihood}, plus OTHER. Order is fixed by the files.

    Results are remembered, because choosing a question asks the same thing many
    times. The answer depends only on the method, the symptoms and the answers, so
    a remembered result is always the same as a fresh one.
    """
    # Within an entry symptom, its own main symptom is not evidence: everyone being
    # assessed for breathlessness is breathless, and the starting chances on the
    # cards are already "among people with this symptom". Counting it again would
    # inflate every condition linked to it. It can still set the STARTING chance
    # (a card's "prevalence_when"), so asthma can start common among people who
    # wheeze but uncommon among people who cough.
    own = {m.presenting_finding for m in modules}
    evidence = {f: a for f, a in known.items() if f not in own}
    cache = kb.__dict__.setdefault("_likelihood_cache", {})
    key = (kb.settings.inference_method, tuple(m.id for m in modules), tuple(sorted(known.items())))
    if key not in cache:
        if len(cache) > 50000:
            cache.clear()
        method = _noisy_or if kb.settings.inference_method == "noisy_or" else _single_cause
        cache[key] = method(kb, modules, evidence, known)
    return dict(cache[key])


def _applies(kb: KnowledgeBase, finding_id: str, known: dict[str, str]) -> bool:
    """False for a question that does not apply to this patient, because its gate was
    answered "no". Its "no" settles rules, but it is not evidence about any condition."""
    gate = kb.findings[finding_id].asked_only_if if finding_id in kb.findings else None
    return not (gate and known.get(gate) == NO)


def _candidates(kb: KnowledgeBase, modules: list[Module], known: dict[str, str]) -> list[str]:
    """The conditions in play. A card for one sex is left out when the patient is the other."""
    other_sex = {"female": "sex_male", "male": "sex_female"}
    condition_ids: list[str] = []
    for module in modules:
        for condition_id in module.conditions:
            sex = kb.conditions[condition_id].sex
            if sex and known.get(other_sex[sex]) == YES:
                continue
            if condition_id not in condition_ids:
                condition_ids.append(condition_id)
    return condition_ids


def _strength(kb: KnowledgeBase, condition_id: str, finding_id: str) -> float:
    """noisy_or: the chance this condition, if present, causes this observation. 0 if not linked."""
    band = kb.conditions[condition_id].findings.get(finding_id)
    if band in ("supports", "strongly_supports"):
        return kb.settings.support_bands[band]
    return 0.0


def _noisy_or(kb: KnowledgeBase, modules: list[Module], known: dict[str, str], everything: dict[str, str]) -> dict[str, float]:
    """known: the evidence. everything: all answers, used for starting chances."""
    conditions = _candidates(kb, modules, everything)
    if not conditions:
        return {OTHER: 1.0}
    leak = kb.settings.background_chance
    priors = {c: min(_prior(kb, c, everything), 0.95) for c in conditions}
    strength = {c: {f: _strength(kb, c, f) for f in kb.conditions[c].findings} for c in conditions}

    # Evidence: answered observations linked to at least one candidate. Others only
    # multiply every possibility by the same amount, so they cannot change anything.
    linked = {f for c in conditions for f, q in strength[c].items() if q > 0}
    answered = [(f, a) for f, a in known.items() if a in (YES, NO) and f in linked and _applies(kb, f, known)]
    # Related observations are one piece of evidence: per group keep one, a "yes" over a "no".
    chosen: dict[str, tuple[str, str]] = {}
    evidence: list[tuple[str, str]] = []
    for finding_id, answer in answered:
        group = kb.findings[finding_id].group
        if group is None:
            evidence.append((finding_id, answer))
            continue
        weight = sum(strength[c].get(finding_id, 0.0) for c in conditions)
        current = chosen.get(group)
        if current is None:
            chosen[group] = (finding_id, answer, weight)
        else:
            _, current_answer, current_weight = current
            better = (answer == YES and current_answer == NO) or (answer == current_answer and weight > current_weight)
            if better:
                chosen[group] = (finding_id, answer, weight)
    evidence += [(f, a) for f, a, _ in chosen.values()]

    positives = [f for f, a in evidence if a == YES]
    negatives = [f for f, a in evidence if a == NO]
    if len(positives) > MAX_POSITIVE:
        # Keep the strongest, in a fixed order, so the cost stays bounded.
        positives = sorted(positives, key=lambda f: (-max(strength[c].get(f, 0.0) for c in conditions), f))[:MAX_POSITIVE]

    # Quickscore: sum over every subset of the "yes" observations, with alternating
    # signs. Each row of these tables is one subset (numbered by bitmask), each
    # column one condition, so all subsets are worked out together.
    n = len(positives)
    masks = np.arange(1 << n)
    absent = np.ones((1 << n, len(conditions)))     # chance a condition causes none of the subset
    for j, f in enumerate(positives):
        in_subset = ((masks >> j) & 1).astype(bool)
        absent[in_subset] *= [1.0 - strength[c].get(f, 0.0) for c in conditions]
    for f in negatives:                               # the "no" answers are in every term
        absent *= [1.0 - strength[c].get(f, 0.0) for c in conditions]
    size = np.array([bin(m).count("1") for m in masks])
    sign = np.where(size % 2, -1.0, 1.0)
    prior = np.array([priors[c] for c in conditions])
    factors = prior * absent
    base = (1.0 - prior) + factors                    # never 0, as starting chances are at most 0.95
    everyone = sign * (1.0 - leak) ** (size + len(negatives)) * np.prod(base, axis=1)
    total = float(everyone.sum())
    with_condition = dict(zip(conditions, (everyone[:, None] / base * factors).sum(axis=0).tolist()))
    if total <= 0:
        return {**{c: priors[c] for c in conditions}, OTHER: 0.0}

    result = {c: max(0.0, min(1.0, with_condition[c] / total)) for c in conditions}
    # Chance that none of the listed conditions is present.
    none_present = math.prod(1.0 - priors[c] for c in conditions) * (leak ** len(positives)) * ((1.0 - leak) ** len(negatives))
    result[OTHER] = max(0.0, min(1.0, none_present / total))
    return result


def _single_cause(kb: KnowledgeBase, modules: list[Module], known: dict[str, str], everything: dict[str, str]) -> dict[str, float]:
    """Naive Bayes: exactly one of the candidates (or something not on the list) is the cause."""
    condition_ids = _candidates(kb, modules, everything) + [OTHER]

    background = kb.settings.background_chance
    weights: dict[str, float] = {}
    for condition_id in condition_ids:
        weight = _prior(kb, condition_id, everything)
        strongest_yes: dict[str, float] = {}
        strongest_no: dict[str, float] = {}
        for finding_id, answer in known.items():
            if answer not in (YES, NO) or finding_id not in kb.findings or not _applies(kb, finding_id, known):
                continue  # "not sure", or a question that does not apply, tells us nothing
            chance = _chance_given_cause(kb, condition_id, finding_id)
            # How much more (or less) likely this answer is with this cause than in general.
            ratio = chance / background if answer == YES else (1 - chance) / (1 - background)
            group = kb.findings[finding_id].group
            if group is None:
                weight *= ratio
            else:
                # Related findings are one piece of evidence, not several. Keep only the
                # strongest one in each group. A "yes" always beats a "no" in the same
                # group, so a "no" to one question cannot cancel a "yes" to a related one.
                store = strongest_yes if answer == YES else strongest_no
                previous = store.get(group, 1.0)
                if abs(math.log(ratio)) > abs(math.log(previous)):
                    store[group] = ratio
        for group, ratio in strongest_no.items():
            weight *= strongest_yes.get(group, ratio)
        for group, ratio in strongest_yes.items():
            if group not in strongest_no:
                weight *= ratio
        weights[condition_id] = weight

    total = sum(weights.values())
    return {condition_id: weight / total for condition_id, weight in weights.items()}


def chance_of_yes(kb: KnowledgeBase, likelihoods: dict[str, float], finding_id: str) -> float:
    """Estimated chance the patient would answer yes to a finding, given what is known."""
    if kb.settings.inference_method == "noisy_or":
        # Yes unless the leak and every condition that might be present all fail to cause it.
        no_chance = 1.0 - kb.settings.background_chance
        for condition_id, likelihood in likelihoods.items():
            if condition_id != OTHER:
                no_chance *= 1.0 - likelihood * _strength(kb, condition_id, finding_id)
        return 1.0 - no_chance
    return sum(likelihood * _chance_given_cause(kb, condition_id, finding_id)
               for condition_id, likelihood in likelihoods.items())
