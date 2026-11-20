"""Turns an output record into text a person can read on screen."""


def describe(record: dict) -> str:
    outcome = record["outcome"]
    advice = record["advice"]
    lines = [
        "=" * 72,
        record["disclaimer"],
        "=" * 72,
        "",
        "OUTCOME",
        f"  Acuity:        {outcome['acuity_label']}",
        f"  Level of care: {outcome['level_of_care_label']}",
        f"  Timeframe:     {outcome['timeframe_label']}"
        + (f" ({outcome['timeframe_detail']})" if outcome["timeframe_detail"] else ""),
    ]
    if not outcome["covered"]:
        lines.append("  NOT COVERED: no module handles this presenting symptom.")

    lines += ["", "WHY", f"  {record['rationale']}"]
    if record["decided_by"]["note"]:
        lines.append(f"  Note: {record['decided_by']['note']}")

    lines += ["", "RED FLAGS FOUND"]
    if record["red_flags_found"]:
        for flag in record["red_flags_found"]:
            lines.append(f"  - {flag['description']} [{flag['rule']}; source: {flag['source']['title']}]")
    else:
        lines.append("  None")

    caution = record["caution"]
    if caution["drove_outcome"] or caution["red_flags_not_ruled_out"]:
        lines += ["", "CAUTION"]
        if caution["drove_outcome"]:
            lines.append("  Missing information drove this outcome: " + ", ".join(caution["missing_information"]))
        for flag in caution["red_flags_not_ruled_out"]:
            lines.append(f"  Could not rule out: {flag['description']}")

    lines += ["", "ADVICE", f"  {advice['what_to_do']}", "  Look out for:"]
    lines += [f"    - {item}" for item in advice["look_out_for"]]
    lines.append("  Get more help when:")
    lines += [f"    - {item}" for item in advice["get_more_help_when"]]
    lines.append(f"  Where to go: {advice['where_to_go']}")
    if advice["self_care"]:
        lines.append("  What you can do yourself:")
        lines += [f"    - {item}" for item in advice["self_care"]]
    lines.append(f"  (Advice adapted from: {advice['source']['title']})")

    lines += ["", f"QUESTIONS ASKED ({len(record['questions_asked'])})"]
    for question in record["questions_asked"]:
        lines.append(f"  {question['number']}. {question['text']}")
        lines.append(f"     Answer: {_show_answer(question['answer'])}")
        lines.append(f"     Why asked: {question['reason']}")
        if question["changed_outcome"]:
            lines.append(f"     Changed the outcome: {question['outcome_before']['acuity']} -> {question['outcome_after']['acuity']}")
    lines.append(f"  Stopped because: {record['stopped_because']}")

    causes = record["possible_causes"]["causes"]
    if causes:
        lines += ["", "POSSIBLE CAUSES", f"  ({record['possible_causes']['label']})"]
        for cause in causes[:5]:
            code = f" [SNOMED CT {cause['snomed']}]" if cause["snomed"] else ""
            lines.append(f"  - {cause['common_name']}: about {round(cause['likelihood'] * 100)}%{code}")

    versions = record["versions"]
    lines += ["", f"Engine {versions['engine']}, knowledge base {versions['knowledge_base']} "
                  f"({versions['knowledge_base_status']}), mode: {versions['mode']}"]
    return "\n".join(lines)


def _show_answer(answer) -> str:
    if isinstance(answer, dict):
        chosen = [finding for finding, value in answer.items() if value == "yes"]
        unsure = [finding for finding, value in answer.items() if value == "not_sure"]
        text = ", ".join(chosen) if chosen else "none of these"
        return text + (f" (not sure about: {', '.join(unsure)})" if unsure else "")
    if isinstance(answer, list):
        return ", ".join(answer) if answer else "none of these"
    return str(answer).replace("_", " ")
