"""Risk setting sweep: reruns a set of cases at several levels of caution.

The danger class lines say how likely a condition must be before it changes
the outcome. Lower lines mean more caution. This sweep shows the
trade-off: more caution costs more over-triage and more questions.
"""

from statistics import mean

from engine.kb import load_knowledge_base
from harness.patient import play
from harness.scoring import score_case
from harness.vignette import check_vignette, load_vignette, vignette_files

# (label, outcome method, number the thresholds are multiplied by)
SETTINGS = [
    ("Rules only (conditions switched off)", "rules_only", 1.0, None),
    ("Single-cause method instead of the network", "rules_and_conditions", 1.0, "single_cause"),
    ("Less cautious (lines doubled)", "rules_and_conditions", 2.0, None),
    ("As set in settings.yaml", "rules_and_conditions", 1.0, None),
    ("More cautious (lines halved)", "rules_and_conditions", 0.5, None),
    ("Much more cautious (lines quartered)", "rules_and_conditions", 0.25, None),
]


def run_sweep(set_name: str = "dev") -> str:
    base = load_knowledge_base()
    vignettes = []
    for path in vignette_files(set_name):
        try:
            vignette = load_vignette(path)
        except ValueError:
            continue
        if not check_vignette(vignette, base, path):
            vignettes.append(vignette)

    care_levels = [level.id for level in base.settings.level_of_care]
    lines = [f"# Risk setting sweep: {set_name} set", "",
             f"Knowledge base {base.settings.kb_version}. {len(vignettes)} cases.", "",
             "The danger class lines say how likely a condition must be before it changes the outcome. "
             "Each row reruns the same cases at a different level of caution.", "",
             "The cases are AI-drafted and not clinically approved, and the likelihoods are AI estimates. Not for clinical use.", "",
             "| Setting | Below minimum safe | Red flags gate failed | Acuity matches | Over-triage | Raised by conditions | Lowered by conditions | Items read per case |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    profiles = []
    for label, method, factor, inference in SETTINGS:
        kb = load_knowledge_base()
        kb.settings.outcome_method = method
        if inference:
            kb.settings.inference_method = inference
        for danger in kb.settings.danger_classes.values():
            danger.possible = min(1.0, danger.possible * factor)
            danger.likely = min(1.0, danger.likely * factor)
        records = [play(kb, vignette) for vignette in vignettes]
        scores = [score_case(kb, vignette, record) for vignette, record in zip(vignettes, records)]
        total = len(scores)
        lines.append(
            f"| {label} | {sum(not s['gates']['not_below_minimum_safe'] for s in scores)} | "
            f"{sum(not s['gates']['red_flags_passed'] for s in scores)} | "
            f"{sum(s['agreement']['acuity'] for s in scores)} of {total} | "
            f"{sum(s['acuity_levels_above_expected'] > 0 for s in scores)} of {total} | "
            f"{sum(r['conditions']['raised_the_outcome'] for r in records)} | "
            f"{sum(r['conditions']['lowered_the_outcome'] for r in records)} | "
            f"{round(mean(s['items_shown'] for s in scores), 1)} |")
        profiles.append((label, [sum(s["actual"]["level_of_care"] == level for s in scores) for level in care_levels]))

    lines += ["", "## Outcome profile at each setting", "",
              "| Setting | " + " | ".join(level.replace("_", " ") for level in care_levels) + " |",
              "| --- |" + " --- |" * len(care_levels)]
    lines += [f"| {label} | " + " | ".join(str(count) for count in counts) + " |" for label, counts in profiles]
    return "\n".join(lines) + "\n"
