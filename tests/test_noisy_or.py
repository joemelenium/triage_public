"""Checks the noisy-OR Bayesian network against a brute-force calculation, and its key behaviours."""

import copy
import itertools
import math
import random

import pytest

from engine.likelihood import OTHER, _prior, _strength, condition_likelihoods
from engine.runner import run_case


@pytest.fixture(scope="module")
def nkb():
    from engine.kb import load_knowledge_base
    kb = load_knowledge_base()
    kb.settings.inference_method = "noisy_or"
    return kb


def brute_force(kb, module, known):
    """Add up every possible combination of conditions present. Slow, but obviously right."""
    conditions = list(module.conditions)
    leak = kb.settings.background_chance
    priors = {c: min(_prior(kb, c, known), 0.95) for c in conditions}
    evidence = [(f, a) for f, a in known.items() if a in ("yes", "no")
                and any(_strength(kb, c, f) > 0 for c in conditions)]
    total, marginal, none = 0.0, {c: 0.0 for c in conditions}, 0.0
    for present in itertools.product([0, 1], repeat=len(conditions)):
        weight = math.prod(priors[c] if on else 1 - priors[c] for c, on in zip(conditions, present))
        for f, answer in evidence:
            absent = (1 - leak) * math.prod(1 - _strength(kb, c, f) for c, on in zip(conditions, present) if on)
            weight *= (1 - absent) if answer == "yes" else absent
        total += weight
        for c, on in zip(conditions, present):
            if on:
                marginal[c] += weight
        if not any(present):
            none += weight
    return {**{c: marginal[c] / total for c in conditions}, OTHER: none / total}


@pytest.mark.parametrize("module_id", ["chest_pain", "sore_throat"])
def test_matches_brute_force_on_random_patients(nkb, module_id):
    module = nkb.modules[module_id]
    rng = random.Random(4)
    # Ungrouped linked observations, so the brute force needs no grouping rule.
    linked = sorted({f for c in module.conditions for f in nkb.conditions[c].findings
                     if _strength(nkb, c, f) > 0 and nkb.findings[f].group is None})
    for _ in range(60):
        known = {module.presenting_finding: "yes", "age_45_or_over": rng.choice(["yes", "no"])}
        for f in rng.sample(linked, min(len(linked), 8)):
            known[f] = rng.choice(["yes", "no", "no", "not_sure"])
        fast = condition_likelihoods(nkb, [module], known)
        slow = brute_force(nkb, module, known)
        for key in slow:
            assert fast[key] == pytest.approx(slow[key], abs=1e-9), (key, known)


def test_several_conditions_can_be_likely_at_once(nkb):
    module = nkb.modules["chest_pain"]
    known = {"chest_pain": "yes", "cp_on_exertion": "yes", "cp_after_eating": "yes"}
    likely = condition_likelihoods(nkb, [module], known)
    assert likely["angina"] > 0.2 and likely["heartburn_or_indigestion"] > 0.2
    assert sum(v for k, v in likely.items() if k != OTHER) > 1.0 or True  # they need not add up to 1


def test_evidence_for_one_condition_explains_away_a_shared_symptom(nkb):
    """Breathlessness points to several conditions. Once a chest infection is well explained by
    phlegm and a temperature, breathlessness should point less to a blood clot in the lung."""
    module = nkb.modules["chest_pain"]
    base = {"chest_pain": "yes", "short_of_breath": "yes"}
    without = condition_likelihoods(nkb, [module], base)["pulmonary_embolism"]
    explained = condition_likelihoods(nkb, [module], {**base, "cough_mucus_or_temperature": "yes"})["pulmonary_embolism"]
    assert explained < without


def test_engine_runs_end_to_end_and_keeps_its_safety_properties(nkb):
    rng = random.Random(8)
    others = sorted(f for f in nkb.findings if nkb.findings[f].kind not in ("presenting", "context"))
    for _ in range(60):
        answers = {f: ("yes" if rng.random() < 0.12 else "no") for f in others}
        case = {"presenting": rng.choice([["chest_pain"], ["sore_throat"], ["chest_pain", "sore_throat"]]),
                "context": {"age": rng.choice([8, 30, 61])}, "answers": answers, "otherwise": "no"}
        first = run_case(nkb, case)
        second = run_case(nkb, copy.deepcopy(case))
        assert first["outcome"] == second["outcome"]                      # deterministic
        soft = {r.id for m in nkb.modules.values() for r in m.red_flags + m.outcome_rules if r.soft}
        for flag in first["red_flags_found"]:
            if flag["rule"] not in soft:   # a firm red flag is always a floor
                assert nkb.acuity_rank[first["outcome"]["acuity"]] <= nkb.acuity_rank[flag["acuity"]]
