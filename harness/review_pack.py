"""Builds a readable review pack for clinicians, one per presenting symptom.

The pack is generated from the knowledge base, so it always matches what the
engine actually uses. It lists the red flags, the other rules, the questions
as worded, the advice, the sources, and everything marked as AI judgement.
"""

from pathlib import Path

from engine.kb import AI_JUDGEMENT, KnowledgeBase, Module, Rule, findings_in

REVIEW_DIR = Path(__file__).resolve().parent.parent / "review"


def _label(kb: KnowledgeBase, scale: str, level_id: str) -> str:
    return next(level.label for level in getattr(kb.settings, scale) if level.id == level_id)


def _in_words(kb: KnowledgeBase, expression) -> str:
    """A rule's condition in plain words."""
    if isinstance(expression, str):
        return f"\"{kb.findings[expression].label}\""
    key, value = next(iter(expression.items()))
    if key == "not":
        return f"NOT {_in_words(kb, value)}"
    joiner = " AND " if key == "all" else " OR "
    parts = [_in_words(kb, item) for item in value]
    return joiner.join(f"({part})" if (" AND " in part or " OR " in part) else part for part in parts)


def _source(kb: KnowledgeBase, source_id: str) -> str:
    if source_id == AI_JUDGEMENT:
        return "**AI judgement, needs clinical review**"
    source = kb.sources[source_id]
    return f"[{source.title}]({source.url})"


def _rule_table(kb: KnowledgeBase, rules: list[Rule]) -> list[str]:
    if not rules:
        return ["None.", ""]
    lines = ["| Rule | Fires when | Outcome | Source | OK? |", "| --- | --- | --- | --- | --- |"]
    for rule in rules:
        outcome = (f"{_label(kb, 'acuity', rule.outcome.acuity)}<br>{_label(kb, 'level_of_care', rule.outcome.level_of_care)}"
                   f"<br>{_label(kb, 'timeframe', rule.outcome.timeframe)}"
                   + (f"<br>*{rule.outcome.timeframe_detail}*" if rule.outcome.timeframe_detail else ""))
        note = f"<br>**Note:** {rule.note}" if rule.note else ""
        lines.append(f"| `{rule.id}`<br>{rule.description}{note} | {_in_words(kb, rule.when)} | {outcome} | {_source(kb, rule.source)} | |")
    return lines + [""]


def _advice_block(kb: KnowledgeBase, advice_id: str) -> list[str]:
    advice = kb.advice[advice_id]
    lines = [f"### `{advice.id}`", "", f"**What to do:** {advice.what_to_do}", "", "**Look out for:**"]
    lines += [f"- {item}" for item in advice.look_out_for]
    lines += ["", "**Get more help when:**"] + [f"- {item}" for item in advice.get_more_help_when]
    lines += ["", f"**Where to go:** {advice.where_to_go}"]
    if advice.self_care:
        lines += ["", "**What you can do yourself:**"] + [f"- {item}" for item in advice.self_care]
    sources = ", ".join(_source(kb, s) for s in [advice.source] + advice.also_informed_by)
    return lines + ["", f"Source: {sources}", ""]


def render_review_pack(kb: KnowledgeBase, module: Module) -> str:
    rank = kb.acuity_rank
    module_rules = module.red_flags + module.outcome_rules
    finding_ids: list[str] = [module.presenting_finding]
    for rule in list(kb.universal.rules) + module_rules:
        for finding_id in findings_in(rule.when):
            if finding_id not in finding_ids:
                finding_ids.append(finding_id)
    advice_ids: list[str] = []
    for advice_id in [r.advice for r in list(kb.universal.rules) + module_rules] + [module.default.advice]:
        if advice_id not in advice_ids:
            advice_ids.append(advice_id)
    source_ids: list[str] = []
    for source_id in ([r.source for r in list(kb.universal.rules) + module_rules] + [module.default.source]
                      + [kb.findings[f].source for f in finding_ids]
                      + [s for a in advice_ids for s in [kb.advice[a].source] + kb.advice[a].also_informed_by]):
        if source_id != AI_JUDGEMENT and source_id not in source_ids:
            source_ids.append(source_id)

    lines = [
        f"# Review pack: {module.name}", "",
        f"**Status: {module.status}. Not for clinical use.**", "",
        f"Knowledge base version {kb.settings.kb_version}. Generated from the knowledge base by "
        "`python triage.py review-pack`. Do not edit by hand: change the knowledge base files and generate it again.", "",
        "## What we are asking you to check", "",
        "This content was drafted by AI from the published pages listed below. Please check:", "",
        "1. Is any red flag for this symptom **missing**?",
        "2. Is each rule's **urgency and level of care** right?",
        "3. Is each **question** clear, and does it mean what the source means?",
        "4. Is the **advice** right, specific enough, and safe?",
        "5. For each item under \"AI judgement and open points\": keep, change or remove?", "",
        "Mark the \"OK?\" column, or write comments against the rule id.", "",
        "## How the engine uses this", "",
        "- Each rule says: when these findings are present, the outcome is **at least** this.",
        "- The most urgent rule that fires wins. If none fires, the default outcome is used.",
        "- Red flags are always all checked. After an emergency outcome, the engine only asks what could still "
        "raise it to the most urgent outcome (an ambulance), then stops.",
        "- \"Not sure\" is never treated as \"no\". If a rule cannot be ruled out, the more urgent outcome is chosen.", "",
        "## Sources", "",
        "| Page | Accessed | Page last reviewed | Note |", "| --- | --- | --- | --- |",
    ]
    lines += [f"| [{kb.sources[s].title}]({kb.sources[s].url}) | {kb.sources[s].accessed} | "
              f"{kb.sources[s].page_last_reviewed} | {kb.sources[s].note} |" for s in source_ids]
    lines += ["", "Content adapted from these pages contains public sector information licensed under the Open "
                  "Government Licence v3.0. Adapted text no longer carries the original clinical approval.", ""]

    lines += ["## Red flags checked for everyone", "",
              f"Asked as one question: *\"{kb.universal.screen.question}\"*", ""]
    lines += _rule_table(kb, kb.universal.rules)

    for level in kb.settings.acuity:
        flags = [r for r in module.red_flags if r.outcome.acuity == level.id]
        if flags:
            lines += [f"## {module.name} red flags: {level.label}", ""]
            screen = next((s for s in module.screens if s.level == level.id), None)
            if screen:
                lines += [f"Most of these are asked together as one question: *\"{screen.question}\"*", ""]
            lines += _rule_table(kb, flags)

    lines += [f"## {module.name}: other rules", "",
              "These are asked one at a time, and only if the answer could raise the outcome.", ""]
    lines += _rule_table(kb, sorted(module.outcome_rules, key=lambda r: rank[r.outcome.acuity]))

    default = module.default
    lines += ["## Default outcome", "", "Used when no rule fires.", "",
              f"- **{default.description}**",
              f"- Outcome: {_label(kb, 'acuity', default.outcome.acuity)}, {_label(kb, 'level_of_care', default.outcome.level_of_care)}, "
              f"{_label(kb, 'timeframe', default.outcome.timeframe)}. *{default.outcome.timeframe_detail}*",
              f"- Source: {_source(kb, default.source)}"]
    if default.note:
        lines.append(f"- **Note:** {default.note}")

    lines += ["", "## Questions as worded", "", "The SNOMED CT column shows the concept each question has been matched to, where one fits. "
              "The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.", "",
              "| Short name | Question put to the patient | SNOMED CT | Source | OK? |", "| --- | --- | --- | --- | --- |"]
    lines += [f"| {kb.findings[f].label} | {kb.findings[f].question} | "
              + (f"{kb.findings[f].snomed} {kb.snomed[kb.findings[f].snomed].name}".strip() if kb.findings[f].snomed else "")
              + f" | {_source(kb, kb.findings[f].source)} | |" for f in finding_ids]

    lines += ["", "## Advice given with each outcome", ""]
    for advice_id in advice_ids:
        lines += _advice_block(kb, advice_id)

    lines += ["## AI judgement and open points", "",
              "Everything below rests on AI judgement, not on a direct statement in a source.", "",
              "### Rules and defaults with a note", ""]
    noted = [(r.id, r.note) for r in list(kb.universal.rules) + module_rules if r.note]
    if default.note:
        noted.append((f"{module.id} default outcome", default.note))
    lines += [f"- `{rule_id}`: {note}" for rule_id, note in noted] or ["None."]
    lines += ["", "### How source wording was turned into outcomes", "",
              "The mapping from wording such as \"See a GP\" to the acuity, level of care and timeframe scales is AI "
              "judgement. It is written at the top of `knowledge_base/settings.yaml` and in "
              "`review/wave0_points_for_clinical_review.md`.", "",
              "### Possible causes (used only to choose which question to ask next)", "",
              "How common each cause is, and how strongly each finding points to it, are all AI estimates. They never "
              "set an outcome and are never shown to a patient as a diagnosis.", "",
              "| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |", "| --- | --- | --- | --- |"]
    for condition_id in module.conditions:
        condition = kb.conditions[condition_id]
        findings = "; ".join(f"{kb.findings[f].label}: {band.replace('_', ' ')}" for f, band in condition.findings.items())
        code = f"{condition.snomed} {kb.snomed[condition.snomed].name}".strip() if condition.snomed else ""
        lines.append(f"| {condition.name} | {code} | {condition.prevalence.replace('_', ' ')} | {findings} |")

    lines += ["", "## Reviewer", "", "- Name and role:", "- Date:",
              "- Overall: approved / approved with changes / not approved", "- Comments:", ""]
    return "\n".join(lines)


def write_review_packs(kb: KnowledgeBase, folder: Path = REVIEW_DIR) -> list[Path]:
    folder.mkdir(parents=True, exist_ok=True)
    written = []
    for module in kb.modules.values():
        path = folder / f"review_pack_{module.id}.md"
        path.write_text(render_review_pack(kb, module), encoding="utf-8")
        written.append(path)
    return written
