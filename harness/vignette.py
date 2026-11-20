"""The vignette (test case) format, and the checks every vignette must pass.

A vignette describes one made-up patient: what is true about them, what the
right triage outcome is, and where in the source material that outcome comes
from. The full format is explained in harness/vignette_authoring/FORMAT.md.
"""

import re
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

from engine.kb import KnowledgeBase, general_ones

REPO_ROOT = Path(__file__).resolve().parent.parent
VIGNETTE_DIR = REPO_ROOT / "vignettes"
SNAPSHOT_DIR = REPO_ROOT / "sources" / "nhs_uk"
REQUIRED_STATUS = "AI-drafted, not clinically approved"


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")  # a misspelt field name is an error


class SourceQuote(Strict):
    page: str      # file name of a snapshot in sources/nhs_uk/, for example chest_pain.txt
    quote: str     # words copied exactly from that page


class Findings(Strict):
    present: list[str]          # things that are true of the patient
    absent: list[str]           # relevant things that are NOT true (relevant negatives)
    unknown: list[str] = []     # things the patient genuinely cannot say


class ContextLayer(Strict):
    age: float | None = None
    sex: Literal["female", "male"] | None = None
    findings: dict[str, str] = {}   # things known from the patient's record


class ContextLayers(Strict):
    none: ContextLayer = ContextLayer()
    basic: ContextLayer = ContextLayer()
    full: ContextLayer = ContextLayer()


class Expected(Strict):
    acuity: str
    level_of_care: str
    timeframe: str


class RedFlag(Strict):
    description: str
    findings: list[str]         # the question-list ids that make up this red flag (empty if none fits)
    minimum_acuity: str         # the least urgent acuity that is acceptable when this red flag is present
    source: SourceQuote


class SafetyNetPoint(Strict):
    point: str                  # what the advice should say, in plain words
    any_of: list[str]           # the advice passes if it contains any one of these words or phrases


class Variant(Strict):
    """The same patient, worded differently or volunteering a different amount."""
    id: str
    style: str
    opening_statement: str
    volunteered: list[str] = []  # findings the patient mentions up front without being asked


class ContextTest(Strict):
    what_context_adds: str
    expected_direction: Literal["more_urgent", "less_urgent", "same"]  # full context compared with none


class VignetteSources(Strict):
    expected_outcome: SourceQuote
    minimum_safe_acuity: SourceQuote


class Vignette(Strict):
    id: str
    status: str
    authored_by: str
    presenting: list[str]
    summary: str
    opening_statement: str
    findings: Findings
    context: ContextLayers = ContextLayers()
    expected: Expected
    minimum_safe_acuity: str
    red_flags: list[RedFlag] = []
    safety_netting_should_cover: list[SafetyNetPoint]
    source: VignetteSources
    variants: list[Variant] = []
    context_test: ContextTest | None = None
    atypical: bool = False
    notes: str = ""


def _plain(text: str) -> str:
    """Lower-case, with curly quotes, long dashes and extra spaces flattened, so quotes can be compared."""
    for fancy, simple in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                          ("–", "-"), ("—", "-"), (" ", " ")):
        text = text.replace(fancy, simple)
    return re.sub(r"\s+", " ", text).strip().lower()


def load_vignette(path: Path) -> Vignette:
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    try:
        return Vignette.model_validate(data)
    except ValidationError as error:
        lines = [f"{'.'.join(str(p) for p in e['loc'])}: {e['msg']}" for e in error.errors()]
        raise ValueError("; ".join(lines)) from None


def vignette_files(set_name: str) -> list[Path]:
    """The vignette files in a set (dev, holdout or external), in file-name order."""
    return sorted((VIGNETTE_DIR / set_name).glob("*.yaml"))


def load_set(set_name: str) -> list[Vignette]:
    return [load_vignette(path) for path in vignette_files(set_name)]


def check_vignette(vignette: Vignette, kb: KnowledgeBase, path: Path | None = None) -> list[str]:
    """Return a list of problems with one vignette (empty if it is fine)."""
    problems: list[str] = []
    timeframes = {level.id for level in kb.settings.timeframe}

    if path is not None and path.stem != vignette.id:
        problems.append(f"file name '{path.name}' does not match id '{vignette.id}'")
    if vignette.status != REQUIRED_STATUS:
        problems.append(f"status must be exactly '{REQUIRED_STATUS}'")
    if not vignette.presenting:
        problems.append("presenting is empty")

    # Every finding must be on the question list, and in only one of the three groups.
    groups = {"present": vignette.findings.present, "absent": vignette.findings.absent, "unknown": vignette.findings.unknown}
    for group, ids in groups.items():
        for finding_id in ids:
            if finding_id not in kb.findings:
                problems.append(f"findings.{group}: '{finding_id}' is not on the question list")
    stated = [f for ids in groups.values() for f in ids]
    # A specific symptom cannot be present while its general one is absent.
    for finding_id in vignette.findings.present:
        for parent in (general_ones(kb.findings[finding_id]) if finding_id in kb.findings else []):
            if parent in vignette.findings.absent:
                problems.append(f"'{finding_id}' is present but its more general question '{parent}' is listed as absent")
    for finding_id in sorted({f for f in stated if stated.count(f) > 1}):
        problems.append(f"'{finding_id}' appears more than once across present, absent and unknown")

    for layer_name in ("none", "basic", "full"):
        layer = getattr(vignette.context, layer_name)
        for finding_id, answer in layer.findings.items():
            if finding_id not in kb.findings:
                problems.append(f"context.{layer_name}: '{finding_id}' is not on the question list")
            if answer not in ("yes", "no"):
                problems.append(f"context.{layer_name}: '{finding_id}' must be yes or no (in quotes), not {answer!r}")

    # Outcomes must use the working scales, and expected cannot be less urgent than the minimum.
    if vignette.expected.acuity not in kb.acuity_rank:
        problems.append(f"expected.acuity '{vignette.expected.acuity}' is not on the acuity scale")
    if vignette.expected.level_of_care not in kb.care_rank:
        problems.append(f"expected.level_of_care '{vignette.expected.level_of_care}' is not a level of care")
    if vignette.expected.timeframe not in timeframes:
        problems.append(f"expected.timeframe '{vignette.expected.timeframe}' is not a timeframe")
    if vignette.minimum_safe_acuity not in kb.acuity_rank:
        problems.append(f"minimum_safe_acuity '{vignette.minimum_safe_acuity}' is not on the acuity scale")
    elif vignette.expected.acuity in kb.acuity_rank and \
            kb.acuity_rank[vignette.expected.acuity] > kb.acuity_rank[vignette.minimum_safe_acuity]:
        problems.append("expected.acuity is less urgent than minimum_safe_acuity")

    for number, flag in enumerate(vignette.red_flags, start=1):
        if flag.minimum_acuity not in kb.acuity_rank:
            problems.append(f"red flag {number}: minimum_acuity '{flag.minimum_acuity}' is not on the acuity scale")
        for finding_id in flag.findings:
            if finding_id not in kb.findings:
                problems.append(f"red flag {number}: '{finding_id}' is not on the question list")
            elif finding_id not in vignette.findings.present and vignette.context.full.findings.get(finding_id) != "yes":
                problems.append(f"red flag {number}: '{finding_id}' is not listed as present in this case")
        problems += _check_quote(flag.source, f"red flag {number}")

    problems += _check_quote(vignette.source.expected_outcome, "source.expected_outcome")
    problems += _check_quote(vignette.source.minimum_safe_acuity, "source.minimum_safe_acuity")

    if not vignette.safety_netting_should_cover:
        problems.append("safety_netting_should_cover is empty")
    for point in vignette.safety_netting_should_cover:
        if not point.any_of:
            problems.append(f"safety-netting point '{point.point}' has no words to look for")

    variant_ids = [v.id for v in vignette.variants]
    if len(set(variant_ids)) != len(variant_ids):
        problems.append("two variants share an id")
    for variant in vignette.variants:
        for finding_id in variant.volunteered:
            if finding_id not in vignette.findings.present and finding_id not in vignette.findings.absent:
                problems.append(f"variant '{variant.id}' volunteers '{finding_id}', which is not in present or absent")
    return problems


def _check_quote(source: SourceQuote, where: str) -> list[str]:
    """A cited quote must really appear on the cited page. This stops invented sources."""
    page = SNAPSHOT_DIR / source.page
    if not page.exists():
        return [f"{where}: page '{source.page}' is not in sources/nhs_uk/"]
    if len(source.quote.strip()) < 15:
        return [f"{where}: the quote is too short to check"]
    if _plain(source.quote) not in _plain(page.read_text(encoding="utf-8")):
        return [f"{where}: the quote was not found word for word in {source.page}"]
    return []


def check_folder(kb: KnowledgeBase, set_names=("dev", "holdout")) -> dict[str, list[str]]:
    """Check every vignette file. Returns {file path: problems} for files with problems."""
    report: dict[str, list[str]] = {}
    seen_ids: dict[str, str] = {}
    for set_name in set_names:
        for path in vignette_files(set_name):
            label = f"{set_name}/{path.name}"
            try:
                vignette = load_vignette(path)
            except (ValueError, yaml.YAMLError) as error:
                report[label] = [f"cannot be read: {error}"]
                continue
            problems = check_vignette(vignette, kb, path)
            if vignette.id in seen_ids:
                problems.append(f"id '{vignette.id}' is also used by {seen_ids[vignette.id]}")
            seen_ids[vignette.id] = label
            if problems:
                report[label] = problems
    return report
