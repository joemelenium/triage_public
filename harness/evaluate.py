"""Runs a whole set of vignettes and gathers the results.

For each set it does:
  main run        every case, full context, "no" to anything not mentioned
  baseline        the fixed-order stand-in, on the same cases
  consistency     each case repeated, and each variant (the same patient volunteering
                  more or less up front; reworded wording needs a language layer)
  context         each case with no, basic and full context
  stress test     "not sure" to anything not mentioned (reported separately)
"""

import json
import math
import subprocess
from collections import Counter
from datetime import datetime, timezone
from statistics import mean, median

from engine.kb import KnowledgeBase
from engine.logic import NOT_SURE
from engine.session import run
from harness.baseline import run_baseline
from harness.external import COARSE, COARSE_ORDER, check_external, load_external
from harness.patient import build_case, make_answerer, play, what_is_true
from harness.scoring import score_case
from harness.vignette import VIGNETTE_DIR, check_vignette, load_vignette, vignette_files

REPEATS = 3


def wilson(passed: int, total: int) -> tuple[float, float]:
    """95% range for a proportion (Wilson method). With small numbers the range is wide."""
    if not total:
        return (0.0, 1.0)
    z, p = 1.96, passed / total
    centre = (p + z * z / (2 * total)) / (1 + z * z / total)
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / (1 + z * z / total)
    return (round(max(0.0, centre - half), 3), round(min(1.0, centre + half), 3))


def run_stamp(kb: KnowledgeBase) -> dict:
    """When and on what this run was made, so results can be traced."""
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                                cwd=VIGNETTE_DIR.parent, timeout=10).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True,
                                    cwd=VIGNETTE_DIR.parent, timeout=10).stdout.strip())
    except (OSError, subprocess.SubprocessError):
        commit, dirty = "unknown", False
    from engine import ENGINE_VERSION
    return {"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "engine": ENGINE_VERSION,
            "knowledge_base": kb.settings.kb_version, "git_commit": commit + (" (with uncommitted changes)" if dirty else ""),
            "outcome_method": kb.settings.outcome_method}


def _reference_scores(kb: KnowledgeBase, vignettes, records) -> dict:
    """What two useless engines would score. The gates must be read against these.

    "always 999": everyone gets an ambulance, nothing asked.
    "always self-care": everyone is told to look after themselves, nothing asked.
    """
    results = {}
    for name, acuity, care, timeframe in (("always_999", "emergency", "emergency_ambulance", "now"),
                                          ("always_self_care", "self_manageable", "self_care", "not_needed")):
        gates_passed = over = 0
        for vignette, record in zip(vignettes, records):
            fake = json.loads(json.dumps(record))
            fake["outcome"].update(acuity=acuity, level_of_care=care, timeframe=timeframe)
            fake["findings"]["present"] = []
            fake["red_flags_found"] = []
            fake["questions_asked"] = []
            fake["stopped_because"] = "An emergency outcome was reached." if acuity == "emergency" else "Nothing asked."
            score = score_case(kb, vignette, fake)
            gates_passed += score["gates"]["red_flags_passed"] and score["gates"]["not_below_minimum_safe"]
            over += score["acuity_levels_above_expected"] > 0
        results[name] = {"both_gates_passed": gates_passed, "over_triage": over}
    return results


def _best_fixed_advice(kb: KnowledgeBase, vignettes) -> dict:
    """The safety-netting word check, if every case were given the same piece of advice.

    The best single advice entry shows how much of the score needs no tailoring at all.
    """
    best_id, best = None, -1
    total = sum(len(v.safety_netting_should_cover) for v in vignettes)
    for advice in kb.advice.values():
        text = " ".join([advice.what_to_do, advice.where_to_go] + advice.look_out_for
                        + advice.get_more_help_when + advice.self_care).lower()
        covered = sum(any(w.lower() in text for w in p.any_of) for v in vignettes for p in v.safety_netting_should_cover)
        if covered > best:
            best_id, best = advice.id, covered
    return {"advice": best_id, "points_covered": best, "points_total": total}


def _same(record_a: dict, record_b: dict) -> bool:
    """Two records are identical apart from how long they took."""
    strip = lambda r: json.dumps({k: v for k, v in r.items() if k != "timing"}, sort_keys=True)
    return strip(record_a) == strip(record_b)


def _outcome(record: dict) -> tuple:
    return (record["outcome"]["acuity"], record["outcome"]["level_of_care"], record["outcome"]["timeframe"])


def evaluate_set(kb: KnowledgeBase, set_name: str) -> dict:
    vignettes, file_problems = [], {}
    for path in vignette_files(set_name):
        try:
            vignette = load_vignette(path)
            problems = check_vignette(vignette, kb, path)
        except Exception as error:  # an unreadable file is reported, not allowed to stop the run
            problems, vignette = [f"cannot be read: {error}"], None
        if problems:
            file_problems[path.name] = problems
        else:
            vignettes.append(vignette)

    rank = kb.acuity_rank
    cases, baseline_rows, variant_rows, context_rows, stress_rows = [], [], [], [], []
    records = []
    repeats_identical = 0

    for vignette in vignettes:
        record = play(kb, vignette)
        records.append(record)
        score = score_case(kb, vignette, record)
        cases.append(score)

        # Consistency: the same case again must give exactly the same record.
        if all(_same(play(kb, vignette), record) for _ in range(REPEATS)):
            repeats_identical += 1

        # Consistency: the same patient volunteering a different amount up front.
        for variant in vignette.variants:
            variant_record = play(kb, vignette, volunteered=variant.volunteered)
            variant_rows.append({"case": vignette.id, "variant": variant.id,
                                 "same_outcome": _outcome(variant_record) == _outcome(record),
                                 "outcome": _outcome(variant_record), "base_outcome": _outcome(record),
                                 "interactions": variant_record["burden"]["interactions"]})

        # Fixed-order baseline on the same case.
        baseline = run_baseline(kb, build_case(vignette), make_answerer(what_is_true(kb, vignette)))
        baseline_rows.append({"case": vignette.id, "same_outcome": _outcome(baseline) == _outcome(record),
                              "engine_outcome": _outcome(record), "baseline_outcome": _outcome(baseline),
                              "engine_interactions": record["burden"]["interactions"],
                              "baseline_interactions": baseline["burden"]["interactions"],
                              "engine_items": record["burden"]["items_shown"],
                              "baseline_items": baseline["burden"]["items_shown"],
                              "engine_words": record["burden"]["words_read"],
                              "baseline_words": baseline["burden"]["words_read"]})

        # Context: the same case with nothing, a little and everything known in advance.
        layers = {layer: play(kb, vignette, layer=layer) for layer in ("none", "basic")}
        layers["full"] = record
        none_rank, full_rank = rank[layers["none"]["outcome"]["acuity"]], rank[record["outcome"]["acuity"]]
        direction = "same" if full_rank == none_rank else ("more_urgent" if full_rank < none_rank else "less_urgent")
        row = {"case": vignette.id,
               "acuity": {layer: layers[layer]["outcome"]["acuity"] for layer in ("none", "basic", "full")},
               "interactions": {layer: layers[layer]["burden"]["interactions"] for layer in ("none", "basic", "full")},
               "caution": {layer: layers[layer]["caution"]["drove_outcome"] for layer in ("none", "basic", "full")},
               "direction": direction, "is_context_test": vignette.context_test is not None}
        if vignette.context_test:
            # Did knowing the context lead to a better decision? Better means closer to the
            # expected acuity, and never below the minimum safe. Moving the way the author
            # guessed is not required: an engine that was already cautious without the
            # context should not be marked down for that.
            expected_rank = rank[vignette.expected.acuity]
            safe = full_rank <= rank[vignette.minimum_safe_acuity]
            row["expected_direction"] = vignette.context_test.expected_direction
            row["distance_without"] = abs(none_rank - expected_rank)
            row["distance_with"] = abs(full_rank - expected_rank)
            row["as_expected"] = safe and row["distance_with"] <= row["distance_without"]
            row["improved"] = safe and row["distance_with"] < row["distance_without"]
        context_rows.append(row)

        # Stress test: "not sure" to anything the vignette does not mention.
        stressed = play(kb, vignette, unmentioned=NOT_SURE)
        stressed_score = score_case(kb, vignette, stressed)
        stress_rows.append({"case": vignette.id, "acuity": stressed["outcome"]["acuity"],
                            "not_below_minimum_safe": stressed_score["gates"]["not_below_minimum_safe"],
                            "red_flags_passed": stressed_score["gates"]["red_flags_passed"],
                            "levels_above_expected": stressed_score["acuity_levels_above_expected"],
                            "caution_drove_outcome": stressed["caution"]["drove_outcome"],
                            "interactions": stressed["burden"]["interactions"]})

    return {
        "set": set_name,
        "versions": {"knowledge_base": kb.settings.kb_version, "knowledge_base_status": kb.settings.status},
        "file_problems": file_problems,
        "cases": cases,
        "summary": _summarise(kb, cases, repeats_identical),
        "stamp": run_stamp(kb),
        "reference": _reference_scores(kb, vignettes, records) if vignettes else {},
        "fixed_advice": _best_fixed_advice(kb, vignettes) if vignettes else {},
        "baseline": baseline_rows,
        "variants": variant_rows,
        "context": context_rows,
        "stress": stress_rows,
    }


def _summarise(kb: KnowledgeBase, cases: list[dict], repeats_identical: int) -> dict:
    total = len(cases)
    if not total:
        return {"cases": 0}
    flags = [flag for case in cases for flag in case["gates"]["red_flags"]]
    over = [c["acuity_levels_above_expected"] for c in cases if c["acuity_levels_above_expected"] > 0]
    under = [c for c in cases if c["acuity_levels_above_expected"] < 0]
    before_flag = [c["interactions_before_first_red_flag"] for c in cases if c["interactions_before_first_red_flag"] is not None]
    points = [p for c in cases for p in c["safety_netting"]["points"]]
    care_order = [level.id for level in kb.settings.level_of_care]
    acuity_order = [level.id for level in kb.settings.acuity]
    return {
        "cases": total,
        "gates": {
            "red_flags_total": len(flags),
            "red_flags_passed": sum(f["passed"] for f in flags),
            "cases_with_red_flags": sum(1 for c in cases if c["gates"]["red_flags"]),
            "cases_failing_red_flags": [c["id"] for c in cases if not c["gates"]["red_flags_passed"]],
            "cases_below_minimum_safe": [c["id"] for c in cases if not c["gates"]["not_below_minimum_safe"]],
            "red_flags_range": wilson(sum(f["passed"] for f in flags), len(flags)),
            "not_below_minimum_range": wilson(total - sum(not c["gates"]["not_below_minimum_safe"] for c in cases), total),
        },
        "recognition": dict(Counter(f["recognition"] for f in flags)),
        "ambulance_cases_not_given_ambulance": [c["id"] for c in cases if c["ambulance_case_not_given_ambulance"]],
        "agreement": {
            "acuity": sum(c["agreement"]["acuity"] for c in cases),
            "level_of_care": sum(c["agreement"]["level_of_care"] for c in cases),
            "timeframe": sum(c["agreement"]["timeframe"] for c in cases),
            "all_three": sum(all(c["agreement"].values()) for c in cases),
            "acuity_range": wilson(sum(c["agreement"]["acuity"] for c in cases), total),
        },
        "over_triage": {"cases": len(over), "by_levels": dict(sorted(Counter(over).items()))},
        "less_urgent_than_expected": {"cases": len(under),
                                      "of_which_still_safe": sum(c["gates"]["not_below_minimum_safe"] for c in under)},
        "burden": {
            "interactions_mean": round(mean(c["interactions"] for c in cases), 1),
            "interactions_median": median(c["interactions"] for c in cases),
            "interactions_max": max(c["interactions"] for c in cases),
            "items_shown_mean": round(mean(c["items_shown"] for c in cases), 1),
            "words_read_mean": round(mean(c["words_read"] for c in cases)),
            "words_read_max": max(c["words_read"] for c in cases),
            "advice_words_median": median(c["advice_words"] for c in cases),
            "before_first_red_flag_mean": round(mean(before_flag), 1) if before_flag else None,
        },
        "safety_netting": {
            "three_parts_present": sum(c["safety_netting"]["three_parts_present"] for c in cases),
            "points_total": len(points),
            "points_covered": sum(p["covered"] for p in points),
        },
        "consistency": {"repeats_identical": repeats_identical},
        "coverage": {"handled_by_a_module": sum(c["covered"] for c in cases)},
        "caution_drove_outcome": sum(c["caution_drove_outcome"] for c in cases),
        "outcome_profile": {
            "engine_level_of_care": {level: sum(c["actual"]["level_of_care"] == level for c in cases) for level in care_order},
            "expected_level_of_care": {level: sum(c["expected"]["level_of_care"] == level for c in cases) for level in care_order},
            "engine_acuity": {level: sum(c["actual"]["acuity"] == level for c in cases) for level in acuity_order},
            "expected_acuity": {level: sum(c["expected"]["acuity"] == level for c in cases) for level in acuity_order},
        },
    }


def evaluate_external(kb: KnowledgeBase) -> dict:
    """Run the published vignette sets. Only a coarse comparison is possible."""
    vignettes, file_problems = load_external()
    rows = []
    for vignette in vignettes:
        problems = check_external(vignette, kb, VIGNETTE_DIR / "external" / f"{vignette.id}.yaml")
        if problems:
            file_problems[f"{vignette.id}.yaml"] = problems
            continue
        truth = {**{f: "yes" for f in vignette.findings.present}, **{f: "no" for f in vignette.findings.absent},
                 **{f: NOT_SURE for f in vignette.findings.unknown}}
        context = {key: value for key, value in (("age", vignette.age), ("sex", vignette.sex)) if value is not None}
        case = {"presenting": vignette.presenting or [vignette.presenting_text], "context": context}
        answer = make_answerer(truth)
        record = run(kb, case, [], answer_next=answer)["record"]
        engine_coarse = COARSE[record["outcome"]["acuity"]]
        difference = COARSE_ORDER.index(vignette.original_triage) - COARSE_ORDER.index(engine_coarse)
        rows.append({
            "id": vignette.id, "set": vignette.set, "presenting_text": vignette.presenting_text,
            "covered": record["outcome"]["covered"],
            "published": vignette.original_triage, "engine": engine_coarse,
            "engine_acuity": record["outcome"]["acuity"], "engine_level_of_care": record["outcome"]["level_of_care"],
            "agrees": difference == 0,
            # Positive: the engine was more urgent than the published category. Negative: less urgent.
            "categories_above_published": difference,
            "red_flags_found": [flag["rule"] for flag in record["red_flags_found"]],
            "decided_by": record["decided_by"]["id"],
            "interactions": record["burden"]["interactions"],
        })
    return {"set": "external", "versions": {"knowledge_base": kb.settings.kb_version},
            "file_problems": file_problems, "cases": rows}
