"""Published vignette sets: their format, checks and scoring.

These were written by other people, so they are an outside check. They use
coarser triage categories than this project, so only a coarse comparison is
made, and results are reported separately as a sense check.
"""

from pathlib import Path
from typing import Literal

import yaml
from pydantic import ValidationError

from engine.kb import KnowledgeBase
from harness.vignette import VIGNETTE_DIR, Findings, Strict

# How this project's acuity levels line up with the coarse published categories.
COARSE = {
    "emergency": "emergency",
    "urgent": "non_emergency",
    "soon": "non_emergency",
    "routine": "non_emergency",
    "self_manageable": "self_care",
}
COARSE_ORDER = ["emergency", "non_emergency", "self_care"]  # most urgent first


class ExternalVignette(Strict):
    id: str
    set: str
    status: str
    citation: str
    licence: str
    original_text: str = ""      # not stored: see sources/external_vignette_sets.md
    original_diagnosis: str = ""
    original_triage_label: str
    original_triage: Literal["emergency", "non_emergency", "self_care"]
    presenting_text: str
    presenting: list[str] = []
    age: float | None = None
    sex: Literal["female", "male"] | None = None
    findings: Findings
    conversion_notes: str = ""


def load_external() -> tuple[list[ExternalVignette], dict[str, list[str]]]:
    """Load the published vignettes. Returns (vignettes, problems by file)."""
    vignettes, problems = [], {}
    for path in sorted((VIGNETTE_DIR / "external").glob("*.yaml")):
        try:
            with open(path, encoding="utf-8") as handle:
                vignettes.append(ExternalVignette.model_validate(yaml.safe_load(handle)))
        except (ValidationError, yaml.YAMLError) as error:
            problems[path.name] = [str(error).splitlines()[0]]
    return vignettes, problems


def check_external(vignette: ExternalVignette, kb: KnowledgeBase, path: Path | None = None) -> list[str]:
    problems = []
    if path is not None and path.stem != vignette.id:
        problems.append(f"file name '{path.name}' does not match id '{vignette.id}'")
    for group in ("present", "absent", "unknown"):
        for finding_id in getattr(vignette.findings, group):
            if finding_id not in kb.findings:
                problems.append(f"findings.{group}: '{finding_id}' is not on the question list")
    for finding_id in vignette.presenting:
        if finding_id not in kb.findings or kb.findings[finding_id].kind != "presenting":
            problems.append(f"presenting: '{finding_id}' is not a presenting symptom on the question list")
    if not vignette.licence.strip() or not vignette.citation.strip():
        problems.append("citation and licence are required")
    return problems
