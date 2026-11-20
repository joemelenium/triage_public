"""Loads the knowledge base (the YAML files) and checks it before anything runs.

Why check on load: a typo in a clinical file should stop the engine with a
clear message, not quietly change a triage outcome.

The classes below describe the shape each YAML file must have. Any field name
not listed here is rejected, so spelling mistakes are caught.
"""

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KB_DIR = REPO_ROOT / "knowledge_base"
DEFAULT_SOURCE_LOG = REPO_ROOT / "sources" / "source_log.yaml"
SNOMED_LOG_NAME = "snomed_codes.yaml"   # sits beside the source log

# Items with no published source carry this marker instead of a source id.
AI_JUDGEMENT = "ai_judgement"
AI_JUDGEMENT_LABEL = "AI judgement, needs clinical review"


class KnowledgeBaseError(Exception):
    """Raised when the knowledge base is missing something or is inconsistent."""


class Strict(BaseModel):
    # "forbid" means an unknown field name is an error, not silently ignored.
    model_config = ConfigDict(extra="forbid")


# ---- settings.yaml ---------------------------------------------------------

class Level(Strict):
    id: str
    label: str


class Outcome(Strict):
    acuity: str
    level_of_care: str
    timeframe: str
    timeframe_detail: str = ""

    def key(self) -> tuple[str, str, str]:
        """The three fields that make two outcomes the same or different."""
        return (self.acuity, self.level_of_care, self.timeframe)


class NotCovered(Strict):
    outcome: Outcome
    advice: str
    source: str
    note: str = ""


class DangerClass(Strict):
    possible: float
    likely: float
    weight: float


class ConditionOutcome(Strict):
    level_of_care: str
    timeframe: str
    advice: str


class Settings(Strict):
    kb_version: str
    status: str
    acuity: list[Level]
    level_of_care: list[Level]
    timeframe: list[Level]
    question_limit: int
    not_covered: NotCovered
    prevalence_bands: dict[str, float]
    support_bands: dict[str, float]
    background_chance: float
    other_cause_prevalence: float
    outcome_method: Literal["rules_and_conditions", "rules_only"]
    inference_method: Literal["single_cause", "noisy_or"] = "single_cause"
    danger_classes: dict[str, DangerClass]
    condition_outcomes: dict[str, ConditionOutcome]
    unknown_cause_threshold: float
    min_likelihood_to_explain: float
    min_risk_shift_to_ask: float
    max_condition_questions: int


# ---- observations/*.yaml (findings) ----------------------------------------

class AgeRange(Strict):
    """An age band in years. min is included, below is not: {below: 5} means under 5."""
    min: float | None = None
    below: float | None = None

    def contains(self, age: float) -> bool:
        return (self.min is None or age >= self.min) and (self.below is None or age < self.below)


RELATIONS = ("duration", "severity", "character", "exacerbating_factor", "diminishing_factor", "location", "radiation")
SERIOUSNESS = ("serious", "emergency", "emergency_ambulance")


class Finding(Strict):
    """An observation: anything the engine can know about a patient."""
    id: str
    label: str                      # short name used in traces and reports
    question: str                   # the plain-English question put to the patient
    question_carer: str = ""        # the question when someone answers for another person
    checklist_text: str = ""        # a short form, used as one line of a "do any of these apply?" checklist
    kind: Literal["presenting", "symptom", "history", "context"]
    parent: str | None = None       # a more general observation this one belongs to
    relation: Literal[RELATIONS] | None = None   # how it relates to its parent
    # Other general observations this one is also part of. A "yes" here means "yes"
    # to each of them, and a "no" to any of them means "no" here. Only `parent` decides
    # which question is asked first. ("Vomiting" is part of "diarrhoea or vomiting"
    # and of "feeling sick or vomiting".)
    also_part_of: list[str] = []
    sex: Literal["female", "male"] | None = None # only applies to one sex
    seriousness: Literal[SERIOUSNESS] | None = None  # an alarming sign, where a source names it
    body_system: str = ""           # set from the file it is in
    phrases: list[str] = []         # everyday phrases, for the language layer later
    snomed: str = ""                # SNOMED CT code, only if listed as checked in sources/snomed_codes.yaml
    group: str | None = None        # related findings share a group so evidence is not counted twice
    age_range: AgeRange | None = None  # if set, the answer is worked out from the patient's age
    asked_only_if: str | None = None   # only ask this after a "yes" to that finding (for example a diagnosis)
    source: str


# ---- rules (used in red_flags.yaml and in each module) ----------------------

class Rule(Strict):
    id: str
    description: str
    when: Any                       # which findings make the rule fire (see logic.py)
    outcome: Outcome
    advice: str
    source: str
    note: str = ""
    soft: bool = False              # True: the conditions that look likely may lower this rule's outcome


class Screen(Strict):
    """Several red-flag findings asked together as one 'do any of these apply?' question."""
    id: str
    level: str                      # the acuity level this screen checks for
    question: str
    findings: list[str]         # each finding carries its own source


class UniversalRedFlags(Strict):
    screen: Screen
    rules: list[Rule]


# ---- entry_symptoms/*.yaml (called modules in the code) ---------------------

class DefaultOutcome(Strict):
    description: str
    outcome: Outcome
    advice: str
    source: str
    note: str = ""
    # True when the source says everyone with this symptom should get at least this
    # level of care. Likely conditions can then never take the outcome below it.
    floor: bool = False


class DefaultException(Strict):
    """A case where a different outcome replaces the module's default outcome.

    Rules can only raise an outcome above the default. An exception is the one
    way to go below it, for a specific, sourced situation.
    """
    id: str
    description: str
    when: Any
    outcome: Outcome
    advice: str
    source: str
    note: str = ""


class Module(Strict):
    """An entry symptom: the sourced rules, checklists and default for one main symptom.

    (Called a "module" in the code for historical reasons.) Which conditions are
    candidates is not listed here: each condition card says which entry symptoms
    it belongs to, and the list below is filled in when the network loads.
    """
    id: str
    name: str
    presenting_finding: str
    status: str
    screens: list[Screen] = []
    red_flags: list[Rule] = []
    outcome_rules: list[Rule] = []
    default: DefaultOutcome
    default_exceptions: list[DefaultException] = []
    conditions: list[str] = []      # filled in from the condition cards
    also_covers: list[str] = []     # source ids of other Symptoms A to Z pages this entry symptom covers


# ---- conditions/<body system>/<id>.yaml (condition cards) ------------------

class PrevalenceWhen(Strict):
    finding: str
    prevalence: str
    also: list[str] = []    # other findings that must also be "yes" for this to apply


class Condition(Strict):
    """A condition card: one possible cause, and how it links to observations."""
    id: str
    body_system: str
    entry_symptoms: list[str]       # main symptoms that make this condition a candidate
    key_findings: list[str] = []    # observations to ask about if this condition becomes probable
    name: str                       # the everyday name
    medical_name: str = ""          # the medical name, where it differs
    snomed: str = ""                # SNOMED CT code, only if listed as checked in sources/snomed_codes.yaml
    acuity_needed: str              # the level of care this condition would need
    danger: str                     # how bad it would be to miss it: a class in settings.yaml
    # A finding meaning the patient already has a diagnosis of this condition. A known,
    # managed condition does not on its own raise the outcome: the rules about it
    # getting worse do that.
    diagnosed_by: str | None = None
    # The level of care this condition needs, when it is not the usual one for its
    # acuity (for example a dentist for a tooth abscess).
    level_of_care: str | None = None
    prevalence: str
    prevalence_when: list[PrevalenceWhen] = []
    # Only for one sex (for example ovarian torsion). Ruled out when the patient is the other.
    sex: Literal["female", "male"] | None = None
    findings: dict[str, str] = {}   # finding id -> support band
    source: str
    informed_by: list[str] = []


# ---- advice.yaml -------------------------------------------------------------

class Advice(Strict):
    id: str
    what_to_do: str
    look_out_for: list[str]
    get_more_help_when: list[str]
    where_to_go: str
    self_care: list[str] = []
    source: str
    also_informed_by: list[str] = []


# ---- sources/source_log.yaml ---------------------------------------------------

class Source(Strict):
    id: str
    title: str
    url: str
    accessed: str
    page_last_reviewed: str = ""
    licence: str
    used_for: str
    note: str = ""


class AvoidedWord(Strict):
    """A word the NHS A to Z of health writing tells writers to avoid."""
    term: str
    use_instead: str
    unless_with: list[str] = []


class PlainLanguageTerm(Strict):
    """A medical word that must be explained wherever a patient sees it."""
    term: str
    plain: str
    explained_by: list[str]
    explained_in: str | None = None


class SnomedCode(Strict):
    """One SNOMED CT code that has been checked against a named terminology source."""
    code: str
    name: str = ""                  # the concept's fully specified name, if recorded (left out of public copies)
    checked_against: str
    checked_on: str


def general_ones(finding) -> list[str]:
    """Every more general observation this one is part of: its parent, then any others."""
    return ([finding.parent] if finding.parent else []) + list(finding.also_part_of)


class KnowledgeBase:
    """Everything the engine needs, loaded and checked."""

    def __init__(self, settings, findings, universal, modules, conditions, advice, sources, snomed_codes=(),
                 glossary=()):
        self.settings: Settings = settings
        self.findings: dict[str, Finding] = {f.id: f for f in findings}
        self.universal: UniversalRedFlags = universal
        self.modules: dict[str, Module] = {m.id: m for m in modules}
        self.conditions: dict[str, Condition] = {c.id: c for c in conditions}
        self.advice: dict[str, Advice] = {a.id: a for a in advice}
        self.sources: dict[str, Source] = {s.id: s for s in sources}
        self.snomed: dict[str, SnomedCode] = {c.code: c for c in snomed_codes}
        self.glossary: list[PlainLanguageTerm] = list(glossary)
        self.avoided: list[AvoidedWord] = []
        # Position in each scale. 0 is the most urgent or most intensive.
        self.acuity_rank = {level.id: i for i, level in enumerate(settings.acuity)}
        self.care_rank = {level.id: i for i, level in enumerate(settings.level_of_care)}

    def to_ask_for(self, finding_id: str, known: dict[str, str]) -> str | None:
        """The question to ask in order to learn about this observation, or None if none can be asked.

        Usually the observation itself. But a child (such as "severe headache")
        waits for its parent ("headache"), and a question gated on another answer
        waits for that answer, so in those cases the parent or gate is asked first.
        """
        seen = set()
        current = finding_id
        while current not in seen:
            seen.add(current)
            finding = self.findings[current]
            parent = finding.parent
            if parent and parent not in known:
                current = parent          # ask about the more general observation first
                continue
            if parent and known.get(parent) == "no":
                return None               # does not apply
            gate = finding.asked_only_if
            if gate and gate not in known and self.findings[gate].age_range is None:
                current = gate            # ask the gating question first
                continue
            if current in known or not self.askable(current, known):
                return None
            return current
        return None

    def askable(self, finding_id: str, known: dict[str, str]) -> bool:
        """Whether a question may be asked yet. Some only make sense after a "yes" to another.

        "No" blocks it. "Yes" or "not sure" allow it: "not sure" must never block a
        question the way "no" does. If the other has not been asked yet, wait for it,
        unless it is worked out from the age and no age was given, in which case ask.
        """
        needed = self.findings[finding_id].asked_only_if
        if needed is None:
            return True
        answer = known.get(needed)
        if answer == "no":
            return False
        if answer in ("yes", "not_sure"):
            return True
        return self.findings[needed].age_range is not None

    def urgency(self, outcome: Outcome) -> tuple[int, int]:
        """A sortable measure of urgency. Smaller means more urgent."""
        return (self.acuity_rank[outcome.acuity], self.care_rank[outcome.level_of_care])

    def source_details(self, source_id: str) -> dict:
        """What to show for a source: title and link, or the AI judgement marker."""
        if source_id == AI_JUDGEMENT:
            return {"id": AI_JUDGEMENT, "title": AI_JUDGEMENT_LABEL}
        source = self.sources[source_id]
        return {"id": source.id, "title": source.title, "url": source.url, "accessed": source.accessed}


def _read_yaml(path: Path):
    if not path.exists():
        raise KnowledgeBaseError(f"Missing file: {path}")
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _parse(model, data, path: Path):
    """Turn YAML data into a checked object, with a readable message on failure."""
    try:
        return model.model_validate(data)
    except ValidationError as error:
        lines = [f"  {'.'.join(str(p) for p in e['loc'])}: {e['msg']}" for e in error.errors()]
        raise KnowledgeBaseError(f"Problem in {path.name}:\n" + "\n".join(lines)) from None


def findings_in(expression) -> list[str]:
    """Every finding id mentioned in a rule's 'when'."""
    if isinstance(expression, str):
        return [expression]
    if isinstance(expression, dict) and len(expression) == 1:
        key, value = next(iter(expression.items()))
        if key in ("all", "any") and isinstance(value, list):
            return [f for item in value for f in findings_in(item)]
        if key == "not":
            return findings_in(value)
    raise KnowledgeBaseError(f"Cannot read rule condition: {expression!r}. Use a finding id, all, any or not.")


def load_knowledge_base(kb_dir: Path = DEFAULT_KB_DIR, source_log: Path = DEFAULT_SOURCE_LOG) -> KnowledgeBase:
    kb_dir = Path(kb_dir)
    settings = _parse(Settings, _read_yaml(kb_dir / "settings.yaml"), kb_dir / "settings.yaml")
    # Observations: one file per body system, together one network.
    findings = []
    for path in sorted((kb_dir / "observations").glob("*.yaml")):
        for item in _read_yaml(path) or []:
            finding = _parse(Finding, item, path)
            finding.body_system = path.stem
            findings.append(finding)
    if not findings:
        raise KnowledgeBaseError(f"No observations found in {kb_dir / 'observations'}")
    universal = _parse(UniversalRedFlags, _read_yaml(kb_dir / "red_flags.yaml"), kb_dir / "red_flags.yaml")
    # Condition cards: one file each, in a folder per body system. Loaded in path order.
    conditions = []
    for path in sorted((kb_dir / "conditions").glob("*/*.yaml")):
        card = _parse(Condition, _read_yaml(path), path)
        if card.id != path.stem:
            raise KnowledgeBaseError(f"Condition card {path.name} has id '{card.id}'. The file name must match the id.")
        if card.body_system != path.parent.name:
            raise KnowledgeBaseError(f"Condition card {path.name} says body_system '{card.body_system}' "
                                     f"but is in folder '{path.parent.name}'")
        conditions.append(card)
    # Advice: one file per body system in advice/ (and an older single advice.yaml if present).
    advice = []
    for path in [kb_dir / "advice.yaml"] * (kb_dir / "advice.yaml").exists() + sorted((kb_dir / "advice").glob("*.yaml")):
        advice += [_parse(Advice, item, path) for item in (_read_yaml(path) or [])]
    # Sources: the main log, plus one log per body system in source_logs/ beside it.
    source_files = [Path(source_log)] + sorted((Path(source_log).parent / "source_logs").glob("*.yaml"))
    sources = [_parse(Source, item, path) for path in source_files for item in (_read_yaml(path) or [])]
    # Modules are loaded in file-name order so the order never depends on the computer.
    modules = [_parse(Module, _read_yaml(path), path) for path in sorted((kb_dir / "entry_symptoms").glob("*.yaml"))]
    # Each entry symptom's candidate conditions come from the condition cards.
    for module in modules:
        module.conditions = [c.id for c in conditions if module.presenting_finding in c.entry_symptoms]

    # SNOMED CT codes that have been checked. A code not listed here may not be used.
    # The main log, plus one log per body system in snomed_codes/ beside it.
    snomed_files = [Path(source_log).parent / SNOMED_LOG_NAME] * (Path(source_log).parent / SNOMED_LOG_NAME).exists()
    snomed_files += sorted((Path(source_log).parent / "snomed_codes").glob("*.yaml"))
    snomed_codes = []
    for path in snomed_files:
        for item in _read_yaml(path) or []:
            code = _parse(SnomedCode, item, path)
            if not any(existing.code == code.code for existing in snomed_codes):
                snomed_codes.append(code)

    glossary_file = kb_dir / "plain_language.yaml"
    rules = (_read_yaml(glossary_file) or {}) if glossary_file.exists() else {}
    glossary = [_parse(PlainLanguageTerm, item, glossary_file) for item in rules.get("explain", [])]
    avoided = [_parse(AvoidedWord, item, glossary_file) for item in rules.get("avoid", [])]

    kb = KnowledgeBase(settings, findings, universal, modules, conditions, advice, sources, snomed_codes, glossary)
    kb.avoided = avoided
    problems = _check(kb, findings, modules, conditions, advice, sources)
    if problems:
        raise KnowledgeBaseError("The knowledge base has problems:\n" + "\n".join(f"  - {p}" for p in problems))
    return kb


def _check(kb: KnowledgeBase, findings, modules, conditions, advice, sources) -> list[str]:
    """Cross-checks between files. Returns a list of problems (empty if all is well)."""
    problems: list[str] = []
    settings = kb.settings
    timeframes = {level.id for level in settings.timeframe}

    def check_unique(items, what):  # noqa: E306
        seen = set()
        for item in items:
            if item.id in seen:
                problems.append(f"{what} id '{item.id}' is used more than once")
            seen.add(item.id)

    def check_source(source_id, where):
        if not source_id:
            problems.append(f"{where} has no source")
        elif source_id != AI_JUDGEMENT and source_id not in kb.sources:
            problems.append(f"{where} cites unknown source '{source_id}'")

    def check_outcome(outcome: Outcome, where):
        if outcome.acuity not in kb.acuity_rank:
            problems.append(f"{where} uses acuity '{outcome.acuity}', which is not in settings.yaml")
        if outcome.level_of_care not in kb.care_rank:
            problems.append(f"{where} uses level of care '{outcome.level_of_care}', which is not in settings.yaml")
        if outcome.timeframe not in timeframes:
            problems.append(f"{where} uses timeframe '{outcome.timeframe}', which is not in settings.yaml")

    def check_findings(ids, where):
        for finding_id in ids:
            if finding_id not in kb.findings:
                problems.append(f"{where} refers to unknown finding '{finding_id}'")

    def check_advice(advice_id, where):
        if advice_id not in kb.advice:
            problems.append(f"{where} refers to unknown advice '{advice_id}'")

    def check_rule(rule: Rule, where):
        where = f"{where} rule '{rule.id}'"
        check_source(rule.source, where)
        check_outcome(rule.outcome, where)
        check_advice(rule.advice, where)
        try:
            check_findings(findings_in(rule.when), where)
        except KnowledgeBaseError as error:
            problems.append(f"{where}: {error}")

    def check_screen(screen: Screen, where):
        if screen.level not in kb.acuity_rank:
            problems.append(f"{where} screen '{screen.id}' uses acuity '{screen.level}', which is not in settings.yaml")
        check_findings(screen.findings, f"{where} screen '{screen.id}'")

    all_rules = list(kb.universal.rules) + [r for m in modules
                                            for r in m.red_flags + m.outcome_rules + m.default_exceptions]
    check_unique(findings, "Finding")
    check_unique(modules, "Module")
    check_unique(conditions, "Condition")
    check_unique(advice, "Advice")
    check_unique(sources, "Source")
    check_unique(all_rules, "Rule")
    check_unique([kb.universal.screen] + [s for m in modules for s in m.screens], "Screen")

    for finding in findings:
        check_source(finding.source, f"Finding '{finding.id}'")
        if finding.asked_only_if:
            check_findings([finding.asked_only_if], f"Finding '{finding.id}' asked_only_if")
        if finding.parent:
            check_findings([finding.parent], f"Finding '{finding.id}' parent")
            if not finding.relation:
                problems.append(f"Finding '{finding.id}' has a parent but no relation")
        elif finding.relation:
            problems.append(f"Finding '{finding.id}' has a relation but no parent")
        check_findings(finding.also_part_of, f"Finding '{finding.id}' also_part_of")
        if finding.id in finding.also_part_of or finding.parent in finding.also_part_of:
            problems.append(f"Finding '{finding.id}' lists itself or its parent in also_part_of")
    # The hierarchy must not loop back on itself.
    for finding in findings:
        seen, current = {finding.id}, finding.parent
        while current and current in kb.findings:
            if current in seen:
                problems.append(f"Finding '{finding.id}' is part of a loop of parents")
                break
            seen.add(current)
            current = kb.findings[current].parent

    # Plain language: a medical word a patient sees must be explained in the same text.
    from .plain_language import unexplained_terms
    for entry in kb.glossary:
        if entry.explained_in:
            check_findings([entry.explained_in], f"Plain language term '{entry.term}'")
    for finding in findings:
        skip = [e.term for e in kb.glossary if e.explained_in and e.explained_in == finding.asked_only_if]
        for text in (finding.question, finding.question_carer, finding.checklist_text):
            for term in unexplained_terms(text, kb.glossary, skip):
                problems.append(f"Question '{finding.id}' uses '{term}' without explaining it in plain words")
    for screen in [kb.universal.screen] + [s for m in modules for s in m.screens]:
        for term in unexplained_terms(screen.question, kb.glossary):
            problems.append(f"Screen '{screen.id}' uses '{term}' without explaining it in plain words")
    for item in advice:
        whole = " ".join([item.what_to_do, item.where_to_go] + item.look_out_for + item.get_more_help_when + item.self_care)
        for term in unexplained_terms(whole, kb.glossary):
            problems.append(f"Advice '{item.id}' uses '{term}' without explaining it in plain words anywhere in the entry")
    for condition in conditions:
        for term in unexplained_terms(condition.name, kb.glossary):
            problems.append(f"Condition '{condition.id}' name uses '{term}' without explaining it in plain words")

    # Words the NHS A to Z of health writing says to avoid, in any text a patient sees.
    from .plain_language import avoided_words, patient_facing_texts
    for where, text in patient_facing_texts(kb):
        for word in avoided_words(text, kb.avoided):
            problems.append(f"The {where} uses '{word.term}'. The NHS A to Z of health writing says to use "
                            f"'{word.use_instead}' instead: \"{text}\"")
    # A SNOMED CT code may only be used if it is in the log of checked codes. This stops invented codes.
    for item, what in [(f, "Finding") for f in findings] + [(c, "Condition") for c in conditions]:
        if item.snomed and item.snomed not in kb.snomed:
            problems.append(f"{what} '{item.id}' uses SNOMED CT code '{item.snomed}', which is not in the log of checked codes")

    check_screen(kb.universal.screen, "Universal")
    for rule in kb.universal.rules:
        check_rule(rule, "Universal")

    check_outcome(settings.not_covered.outcome, "Settings not_covered")
    check_advice(settings.not_covered.advice, "Settings not_covered")
    check_source(settings.not_covered.source, "Settings not_covered")
    for name, danger in settings.danger_classes.items():
        if not 0 <= danger.possible <= danger.likely <= 1:
            problems.append(f"Danger class '{name}': 'possible' must be between 0 and 'likely', and 'likely' at most 1")
    for level in kb.acuity_rank:
        if level not in settings.condition_outcomes:
            problems.append(f"Acuity '{level}' has no entry in condition_outcomes")
    for level, entry in settings.condition_outcomes.items():
        check_outcome(Outcome(acuity=level, level_of_care=entry.level_of_care, timeframe=entry.timeframe),
                      f"Settings condition_outcomes '{level}'")
        check_advice(entry.advice, f"Settings condition_outcomes '{level}'")

    for module in modules:
        where = f"Module '{module.id}'"
        check_findings([module.presenting_finding], where)
        for screen in module.screens:
            check_screen(screen, where)
        for source_id in module.also_covers:
            check_source(source_id, f"{where} also_covers")
        for rule in module.red_flags + module.outcome_rules + module.default_exceptions:
            check_rule(rule, where)
        check_source(module.default.source, f"{where} default outcome")
        check_outcome(module.default.outcome, f"{where} default outcome")
        check_advice(module.default.advice, f"{where} default outcome")

    # ---- The network as a whole ------------------------------------------------------
    presenting_with_entry = {m.presenting_finding for m in modules}
    for module in modules:
        if not module.conditions:
            problems.append(f"Entry symptom '{module.id}' has no condition cards, so likely conditions can never apply")
    codes: dict[str, str] = {}
    for item in list(findings) + list(conditions):
        if item.snomed:
            other = codes.get(item.snomed)
            if other and not (isinstance(item, Condition) and other.startswith("finding:")
                              and kb.conditions.get(item.id) and kb.conditions[item.id].diagnosed_by == other.split(":", 1)[1]):
                problems.append(f"SNOMED CT code {item.snomed} is used by both {other} and "
                                f"{'condition' if isinstance(item, Condition) else 'finding'}:{item.id}. Each concept should appear once.")
            codes.setdefault(item.snomed, f"{'condition' if isinstance(item, Condition) else 'finding'}:{item.id}")
    for condition in conditions:
        where = f"Condition '{condition.id}'"
        if not condition.entry_symptoms:
            problems.append(f"{where} has no entry symptoms, so it can never be a candidate")
        for entry in condition.entry_symptoms:
            if entry not in presenting_with_entry:
                problems.append(f"{where} lists entry symptom '{entry}', which has no file in entry_symptoms/")
        check_findings(condition.key_findings, where)
        check_source(condition.source, where)
        for source_id in condition.informed_by:
            check_source(source_id, where)
        if condition.level_of_care and condition.level_of_care not in kb.care_rank:
            problems.append(f"{where} uses level of care '{condition.level_of_care}', which is not in settings.yaml")
        if condition.danger not in settings.danger_classes:
            problems.append(f"{where} uses danger class '{condition.danger}', which is not in settings.yaml")
        if condition.acuity_needed not in kb.acuity_rank:
            problems.append(f"{where} uses acuity '{condition.acuity_needed}', which is not in settings.yaml")
        for band in [condition.prevalence] + [p.prevalence for p in condition.prevalence_when]:
            if band not in settings.prevalence_bands:
                problems.append(f"{where} uses prevalence band '{band}', which is not in settings.yaml")
        check_findings([f for p in condition.prevalence_when for f in [p.finding, *p.also]], where)
        if condition.diagnosed_by:
            check_findings([condition.diagnosed_by], where)
        check_findings(condition.findings.keys(), where)
        for finding_id in condition.findings:
            if finding_id in kb.findings and kb.findings[finding_id].kind == "context":
                problems.append(f"{where} links '{finding_id}' as evidence. Age and sex set the starting chance "
                                f"(prevalence_when) or limit the card to one sex (sex), but are not evidence")
        for band in condition.findings.values():
            if band not in settings.support_bands:
                problems.append(f"{where} uses support band '{band}', which is not in settings.yaml")

    for item in advice:
        where = f"Advice '{item.id}'"
        check_source(item.source, where)
        for source_id in item.also_informed_by:
            check_source(source_id, where)

    return problems


def network_warnings(kb: KnowledgeBase) -> list[str]:
    """Things in the network worth looking at, which do not stop it loading."""
    from .kb import findings_in as _ids
    used: set[str] = set()
    for rule in kb.universal.rules:
        used |= set(_ids(rule.when))
    used |= set(kb.universal.screen.findings)
    for module in kb.modules.values():
        used.add(module.presenting_finding)
        for rule in module.red_flags + module.outcome_rules + module.default_exceptions:
            used |= set(_ids(rule.when))
        for screen in module.screens:
            used |= set(screen.findings)
    for condition in kb.conditions.values():
        used |= set(condition.findings) | set(condition.key_findings) | {f for p in condition.prevalence_when for f in [p.finding, *p.also]}
        if condition.diagnosed_by:
            used.add(condition.diagnosed_by)
    for finding in kb.findings.values():
        if finding.parent:
            used.add(finding.parent)
        used |= set(finding.also_part_of)
        if finding.asked_only_if:
            used.add(finding.asked_only_if)
    warnings = [f"Observation '{f}' is not used by any rule, checklist or condition card"
                for f in kb.findings if f not in used and f != "presenting_not_covered"]
    for condition in kb.conditions.values():
        links = [f for f, band in condition.findings.items() if band in ("supports", "strongly_supports")]
        if len(links) < 2:
            warnings.append(f"Condition '{condition.id}' has fewer than 2 observations pointing to it, "
                            f"so it is hard to tell apart from others")
    return warnings
