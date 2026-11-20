"""Writes the files a vignette author is allowed to see.

A vignette author must not read the knowledge base, because the rules and
outcomes would let them write cases the engine is bound to pass. But they do
need to know which questions exist, so that the simulated patient can answer
them. This script writes out only that:

  question_list.yaml   each question's id, short label, wording and kind
  scales.yaml          the allowed values for acuity, level of care and timeframe

Nothing about rules, outcomes, red flags, advice or possible causes is included.
"""

from pathlib import Path

import yaml

from engine.kb import KnowledgeBase, general_ones

AUTHORING_DIR = Path(__file__).resolve().parent / "vignette_authoring"


def export_authoring_files(kb: KnowledgeBase, folder: Path = AUTHORING_DIR) -> list[Path]:
    folder.mkdir(parents=True, exist_ok=True)

    questions = []
    for f in kb.findings.values():
        if f.age_range or f.kind == "context" or f.id == "presenting_not_covered":
            continue  # age and sex are given in context, not asked
        entry = {"id": f.id, "label": f.label, "question": f.question, "kind": f.kind}
        if f.parent or f.also_part_of:
            parts = general_ones(f)
            entry["part_of"] = parts[0] if len(parts) == 1 else parts   # a more specific version of that question
        if f.asked_only_if:
            entry["only_asked_if_yes_to"] = f.asked_only_if
        questions.append(entry)
    question_file = folder / "question_list.yaml"
    question_file.write_text(
        "# Every question the engine is able to ask. Generated: do not edit by hand.\n"
        "# 'presenting' questions are main symptoms. The others are asked afterwards.\n"
        "# Questions about age and sex are left out: they come from the patient's context.\n"
        "# 'part_of' means this is a more specific version of another question (a 'barking cough'\n"
        "# is part of 'cough'). If it is present, the general one is present too.\n"
        + yaml.safe_dump(questions, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8")

    scales = {name: [{"id": level.id, "label": level.label} for level in getattr(kb.settings, name)]
              for name in ("acuity", "level_of_care", "timeframe")}
    scales_file = folder / "scales.yaml"
    scales_file.write_text(
        "# The allowed outcome values. Generated: do not edit by hand.\n"
        "# Each list runs from most urgent or most intensive to least.\n"
        + yaml.safe_dump(scales, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8")
    return [question_file, scales_file]
