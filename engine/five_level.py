"""A five-level summary of the outcome, in the shape condition-based engines use.

Condition-based triage engines commonly describe their result as one of five
levels, with a "root cause" saying what drove it and a list of the alarming
evidence found. Giving the same summary here makes side-by-side comparison with
such engines direct. The names describe the published shape; no content is
taken from any product. The mapping from this engine's scales is AI judgement.
"""

from .kb import KnowledgeBase

# Five levels, most urgent first.
LEVELS = ("emergency_ambulance", "emergency", "consultation_24", "consultation", "self_care")


def five_level_summary(kb: KnowledgeBase, record: dict) -> dict:
    outcome = record["outcome"]
    acuity, care = outcome["acuity"], outcome["level_of_care"]
    if acuity == "emergency":
        level = "emergency_ambulance" if care == "emergency_ambulance" else "emergency"
    elif acuity == "urgent":
        level = "consultation_24"
    elif acuity in ("soon", "routine"):
        level = "consultation"
    else:
        level = "self_care"

    decided = record["decided_by"]["kind"]
    if not outcome["covered"] and decided == "not_covered":
        root = "diagnosis_unknown"
    elif decided == "red_flag":
        root = "emergency_evidence_present" if acuity == "emergency" else "serious_evidence_present"
    elif decided == "likely_condition":
        band = record["decided_by"]["description"]
        if acuity == "emergency":
            root = "emergency_condition_possible" if " is possible " in band else "emergency_condition_likely"
        elif acuity == "self_manageable":
            root = "self_care_sufficient"
        else:
            root = "consultation_condition_likely"
    elif acuity == "self_manageable":
        root = "self_care_sufficient"
    else:
        root = "rule_applied"   # a sourced rule or default that is not a red flag

    serious = []
    for flag in record["red_flags_found"]:
        for finding in flag.get("findings", []):
            if finding["id"] not in [s["id"] for s in serious]:
                serious.append({"id": finding["id"], "label": finding["label"], "snomed": finding["snomed"],
                                "seriousness": "emergency" if flag["acuity"] == "emergency" else "serious"})
    for entry in record["findings"]["present"]:
        seriousness = kb.findings[entry["id"]].seriousness
        if seriousness and entry["id"] not in [s["id"] for s in serious]:
            serious.append({"id": entry["id"], "label": entry["label"], "snomed": entry["snomed"],
                            "seriousness": seriousness})
    return {"triage_level": level, "root_cause": root, "serious": serious,
            "note": "A summary in the five-level shape condition-based engines use. The mapping is AI judgement."}
