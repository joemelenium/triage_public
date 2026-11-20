"""Scores one engine record against one vignette.

Two things are GATES. A failure on either is not offset by anything else:
  - every red flag in the case is ESCALATED: the outcome is at least as urgent
    as the red flag needs
  - the outcome is never below the minimum safe urgency

Gates alone can be passed by sending everyone to 999, so the report always
shows over-triage next to them.

Everything else is a score, including red-flag RECOGNITION: whether the engine
actually found and named the red flag, as opposed to reaching a safe outcome
some other way.
"""

from engine.kb import KnowledgeBase
from harness.vignette import Vignette


def score_case(kb: KnowledgeBase, vignette: Vignette, record: dict) -> dict:
    rank = kb.acuity_rank  # 0 is the most urgent
    outcome = record["outcome"]
    actual_rank = rank[outcome["acuity"]]
    expected_rank = rank[vignette.expected.acuity]
    present = {entry["id"] for entry in record["findings"]["present"]}
    reached_emergency = actual_rank == 0

    # ---- Gate: red flags --------------------------------------------------------
    flags = []
    named = {f["id"] for flag in record["red_flags_found"] for f in flag.get("findings", [])}
    for flag in vignette.red_flags:
        # Gate: is the outcome at least as urgent as this red flag needs? That is what
        # matters for the patient, however the engine got there.
        escalated = actual_rank <= rank[flag.minimum_acuity]
        # Score: did the engine recognise it? It must have established the findings, and
        # named a red flag built on them, unless it had already stopped at an outcome as
        # urgent as this flag needs (it must stop then, so it cannot be blamed).
        if not flag.findings:
            recognition = "no question covers this red flag"
        elif all(f in present for f in flag.findings) and (named & set(flag.findings)):
            recognition = "recognised"
        elif all(f in present for f in flag.findings):
            recognition = "found but not named as a red flag"
        elif escalated and record["stopped_because"].startswith("An emergency"):
            recognition = "not asked: already at an outcome this urgent"
        else:
            recognition = "missed"
        flags.append({"description": flag.description, "recognition": recognition, "escalated": escalated,
                      "passed": escalated})

    # ---- Gate: minimum safe urgency ----------------------------------------------
    not_below_minimum = actual_rank <= rank[vignette.minimum_safe_acuity]

    # ---- How many interactions before the first red flag was found ---------------
    flag_findings = {f for flag in vignette.red_flags for f in flag.findings}
    before_first_flag = None
    if flag_findings:
        if any(entry["id"] in flag_findings and entry["from"] != "patient" for entry in record["findings"]["present"]):
            before_first_flag = 0  # known from context or the opening statement
        else:
            for question in record["questions_asked"]:
                answer = question["answer"]
                said_yes = {f for f, value in answer.items() if value == "yes"} if isinstance(answer, dict) \
                    else ({question["id"]} if answer == "yes" else set())
                if said_yes & flag_findings:
                    before_first_flag = question["number"]
                    break

    # ---- Safety-netting ------------------------------------------------------------
    advice = record["advice"]
    advice_text = " ".join([advice["what_to_do"], advice["where_to_go"]] + advice["look_out_for"]
                           + advice["get_more_help_when"] + advice["self_care"]).lower()
    points = [{"point": p.point, "covered": any(word.lower() in advice_text for word in p.any_of)}
              for p in vignette.safety_netting_should_cover]
    words_of_advice = len(advice_text.split())

    # ---- Interaction burden in common units ------------------------------------------
    # "Questions" means different things for different engines (a checklist of 11 items
    # is one question here). Items and words read can be compared across engines.
    words_read = sum(len(q["text"].split()) for q in record["questions_asked"])
    words_read += sum(len(option.split()) for q in record["questions_asked"] if q["kind"] == "screen"
                      for option in q.get("option_texts", []))

    return {
        "id": vignette.id,
        "presenting": vignette.presenting,
        "atypical": vignette.atypical,
        "expected": vignette.expected.model_dump(),
        "minimum_safe_acuity": vignette.minimum_safe_acuity,
        "actual": {"acuity": outcome["acuity"], "level_of_care": outcome["level_of_care"], "timeframe": outcome["timeframe"]},
        "decided_by": {"id": record["decided_by"]["id"], "description": record["decided_by"]["description"],
                       "source": record["decided_by"]["source"]["title"]},
        "gates": {
            "red_flags": flags,
            "red_flags_passed": all(f["passed"] for f in flags),
            "not_below_minimum_safe": not_below_minimum,
        },
        # Not a gate (many sources say "999 or A&E" together), but worth seeing: a case
        # that needs an ambulance sent to make its own way to A&E.
        "ambulance_case_not_given_ambulance": (vignette.expected.level_of_care == "emergency_ambulance"
                                               and outcome["level_of_care"] != "emergency_ambulance"),
        "agreement": {
            "acuity": outcome["acuity"] == vignette.expected.acuity,
            "level_of_care": outcome["level_of_care"] == vignette.expected.level_of_care,
            "timeframe": outcome["timeframe"] == vignette.expected.timeframe,
        },
        # Positive: the engine was more urgent than expected (over-triage), by this many levels.
        # Negative: less urgent than expected.
        "acuity_levels_above_expected": expected_rank - actual_rank,
        "interactions": record["burden"]["interactions"],
        "items_shown": record["burden"]["items_shown"],
        "words_read": record["burden"].get("words_read", words_read),
        "advice_words": words_of_advice,
        "interactions_before_first_red_flag": before_first_flag,
        "safety_netting": {
            "three_parts_present": bool(advice["look_out_for"] and advice["get_more_help_when"] and advice["where_to_go"]),
            "points": points,
        },
        "covered": outcome["covered"],
        "caution_drove_outcome": record["caution"]["drove_outcome"],
        "vignette_source": vignette.source.expected_outcome.model_dump(),
    }
