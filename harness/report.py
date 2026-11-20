"""Turns evaluation results into a readable page (Markdown)."""

from statistics import mean

SET_TITLES = {"dev": "development set", "holdout": "holdout set"}

CAVEAT = """> **Read this first.** These test cases are AI-drafted and not clinically approved.
> They were written in a separate session that saw only the source pages, the
> vignette format and the list of questions. It did not see the engine's rules
> or outcomes. That reduces the risk of the engine being tested against itself.
> It does not remove it: the content and the cases were both drafted by AI from
> the same pages. Treat these results as a check on how the engine behaves, not
> as evidence that it is clinically safe. Not for clinical use."""


def _share(part: int, whole: int) -> str:
    return f"{part} of {whole}" + (f" ({round(100 * part / whole)}%)" if whole else "")


def _range(r) -> str:
    return f"95% range {round(100 * r[0])}% to {round(100 * r[1])}%"


def _triple(outcome) -> str:
    values = outcome.values() if isinstance(outcome, dict) else outcome
    return " / ".join(str(v) for v in values)


def render_set_report(results: dict) -> str:
    title = SET_TITLES.get(results["set"], results["set"])
    summary, cases = results["summary"], results["cases"]
    versions = results["versions"]
    stamp = results.get("stamp", {})
    lines = [f"# Run report: {title}", "",
             f"Run {stamp.get('date', '?')}. Engine {stamp.get('engine', '?')}, knowledge base "
             f"{versions['knowledge_base']} ({versions['knowledge_base_status']}), commit {stamp.get('git_commit', '?')}, "
             f"method: {stamp.get('outcome_method', '?')}. {summary['cases']} cases. Structured mode, no LLM.", "", CAVEAT, ""]
    if not summary["cases"]:
        lines += ["No valid vignettes were found in this set.", ""]
        return "\n".join(lines + _file_problems(results))

    total, gates = summary["cases"], summary["gates"]
    flags_ok = gates["red_flags_passed"] == gates["red_flags_total"]
    minimum_ok = not gates["cases_below_minimum_safe"]

    over_cases = summary["over_triage"]["cases"]
    reference = results.get("reference", {})
    lines += ["## Gates, read with over-triage", "",
              "A failure on either gate is not offset by a good score elsewhere. But the gates alone can be passed "
              "by sending everyone to 999, so they are always shown next to over-triage, and next to what two "
              "useless engines would score.", "",
              "| | Red flags escalated | Not below minimum safe | Both gates, by case | Over-triage |", "| --- | --- | --- | --- | --- |",
              f"| **This engine** | **{'PASS' if flags_ok else 'FAIL'}** {_share(gates['red_flags_passed'], gates['red_flags_total'])} "
              f"| **{'PASS' if minimum_ok else 'FAIL'}** {_share(total - len(gates['cases_below_minimum_safe']), total)} "
              f"| {total - len(set(gates['cases_failing_red_flags']) | set(gates['cases_below_minimum_safe']))} of {total} "
              f"| {_share(over_cases, total)} |"]
    for name, label in (("always_999", "Always 999, asks nothing"), ("always_self_care", "Always self-care, asks nothing")):
        if name in reference:
            lines.append(f"| {label} | | | {reference[name]['both_gates_passed']} of {total} | {_share(reference[name]['over_triage'], total)} |")
    lines += ["",
              f"With this few cases the true rates could differ: red flags escalated {_range(gates['red_flags_range'])}; "
              f"not below minimum safe {_range(gates['not_below_minimum_range'])}.", ""]
    recognition = summary.get("recognition", {})
    if recognition:
        lines += ["**Red-flag recognition** (a score, not a gate): did the engine find and name each red flag, as "
                  "well as escalate? " + "; ".join(f"{name}: {count}" for name, count in sorted(recognition.items())) + ".", ""]
    if summary.get("ambulance_cases_not_given_ambulance"):
        lines += ["**Ambulance cases not given an ambulance** (a score, not a gate, because many sources say \"999 or "
                  "A&E\" together): " + ", ".join(summary["ambulance_cases_not_given_ambulance"]) + ".", ""]

    agreement, burden, netting = summary["agreement"], summary["burden"], summary["safety_netting"]
    over, under = summary["over_triage"], summary["less_urgent_than_expected"]
    variants, context_tests = results["variants"], [r for r in results["context"] if r["is_context_test"]]
    by_levels = ", ".join(f"{count} by {levels} level{'s' if levels > 1 else ''}" for levels, count in over["by_levels"].items())
    lines += ["## Scores", "", "| Measure | Result |", "| --- | --- |",
              f"| Acuity matches expected | {_share(agreement['acuity'], total)}, {_range(agreement['acuity_range'])} |",
              f"| Level of care matches expected | {_share(agreement['level_of_care'], total)} |",
              f"| Timeframe matches expected | {_share(agreement['timeframe'], total)} |",
              f"| All three match | {_share(agreement['all_three'], total)} |",
              f"| Over-triage (more urgent than expected) | {_share(over['cases'], total)}" + (f": {by_levels}" if by_levels else "") + " |",
              f"| Less urgent than expected | {under['cases']} cases, of which {under['of_which_still_safe']} still at or above minimum safe |",
              f"| Items read per case (each checklist line counts) | mean {burden['items_shown_mean']} |",
              f"| Words read per case | mean {burden['words_read_mean']}, most {burden['words_read_max']} |",
              f"| Interactions per case (a checklist counts as one) | mean {burden['interactions_mean']}, median {burden['interactions_median']}, most {burden['interactions_max']} |",
              f"| Interactions before the first red flag was found | "
              + (f"mean {burden['before_first_red_flag_mean']}" if burden['before_first_red_flag_mean'] is not None else "no red-flag cases") + " |",
              f"| Safety-netting: all three parts present | {_share(netting['three_parts_present'], total)} |",
              f"| Safety-netting: points the vignette asked for | {_share(netting['points_covered'], netting['points_total'])} "
              f"(a word check only, needs human judgement) |",
              (f"| Safety-netting: same word check if every case got one fixed advice text | "
               f"{_share(results['fixed_advice']['points_covered'], results['fixed_advice']['points_total'])} "
               f"(best single text: {results['fixed_advice']['advice']}). The gap to the line above is what tailoring adds. |"
               if results.get("fixed_advice") else "| | |"),
              f"| Advice length | median {burden['advice_words_median']} words |",
              f"| Consistency: identical record on repeat | {_share(summary['consistency']['repeats_identical'], total)} |",
              f"| Consistency: same patient, volunteering more or less up front, gives the same outcome | "
              f"{_share(sum(v['same_outcome'] for v in variants), len(variants))}. Reworded wording is not tested: that needs the language layer. |",
              f"| Context tests: context led to an outcome at least as close to expected, and safe | "
              f"{_share(sum(r['as_expected'] for r in context_tests), len(context_tests))}, of which closer: "
              f"{sum(r.get('improved', False) for r in context_tests)} |",
              f"| Coverage: handled by a module | {_share(summary['coverage']['handled_by_a_module'], total)} |",
              f"| Outcome driven by caution (missing information) | {summary['caution_drove_outcome']} cases |", ""]

    profile = summary["outcome_profile"]
    lines += ["## Outcome profile", "",
              "Over-triage has a cost at scale, so the spread of outcomes matters as well as the gates.", "",
              "| Level of care | Engine | Expected |", "| --- | --- | --- |"]
    lines += [f"| {level.replace('_', ' ')} | {profile['engine_level_of_care'][level]} | {profile['expected_level_of_care'][level]} |"
              for level in profile["engine_level_of_care"]]
    lines += ["", "| Acuity | Engine | Expected |", "| --- | --- | --- |"]
    lines += [f"| {level.replace('_', ' ')} | {profile['engine_acuity'][level]} | {profile['expected_acuity'][level]} |"
              for level in profile["engine_acuity"]]

    baseline = results["baseline"]
    different = [row for row in baseline if not row["same_outcome"]]
    lines += ["", "## Comparators", "",
              "**Fixed-order baseline.** A stand-in, not any real triage system. It uses the same rules but asks every "
              "question one at a time in file order.", "",
              f"- Same outcome as the engine: {_share(len(baseline) - len(different), len(baseline))}",
              f"- Items read per case: engine {round(mean(r['engine_items'] for r in baseline), 1)}, "
              f"baseline {round(mean(r['baseline_items'] for r in baseline), 1)}",
              f"- Words read per case: engine {round(mean(r['engine_words'] for r in baseline))}, "
              f"baseline {round(mean(r['baseline_words'] for r in baseline))}",
              f"- Interactions per case (a checklist counts as one, so this flatters the engine): "
              f"engine {round(mean(r['engine_interactions'] for r in baseline), 1)}, "
              f"baseline {round(mean(r['baseline_interactions'] for r in baseline), 1)}"]
    lines += [f"- Different outcome in {row['case']}: engine {_triple(row['engine_outcome'])}, "
              f"baseline {_triple(row['baseline_outcome'])}. The engine stopped before a question that would have changed it." for row in different]
    lines += ["", "**LLM-only baseline.** Not built. No LLM provider has been agreed.", "",
              "**Risk setting sweep.** See `reports/sweep_report.md`, written by `python triage.py sweep`.", ""]

    context = results["context"]
    lines += ["## Patient context", "",
              f"- Interactions per case with no context: {round(mean(r['interactions']['none'] for r in context), 1)}, "
              f"basic: {round(mean(r['interactions']['basic'] for r in context), 1)}, "
              f"full: {round(mean(r['interactions']['full'] for r in context), 1)}"]
    changed = [r for r in context if r["direction"] != "same"]
    lines.append(f"- Cases where full context changed the acuity compared with none: {len(changed)}")
    for row in changed + [r for r in context_tests if r not in changed]:
        expected = f", expected {row['expected_direction'].replace('_', ' ')}" if row["is_context_test"] else ", not a context test"
        verdict = "" if not row["is_context_test"] else (" (as expected)" if row["as_expected"] else " (**not as expected**)")
        guess = " (chosen out of caution, because information was missing)"
        lines.append(f"  - {row['case']}: with no context {row['acuity']['none']}{guess if row['caution']['none'] else ''}, "
                     f"with full context {row['acuity']['full']}{guess if row['caution']['full'] else ''}{expected}{verdict}")

    stress = results["stress"]
    lines += ["", "## \"Not sure\" stress test", "",
              "Reported separately. Here the simulated patient answers \"not sure\" to anything the vignette does not "
              "mention, where the main run answers \"no\". It shows how much the outcomes rest on unstated negatives.", "",
              f"- No outcome below minimum safe urgency: {_share(sum(r['not_below_minimum_safe'] for r in stress), len(stress))}",
              f"- Red flags gate passed: {_share(sum(r['red_flags_passed'] for r in stress), len(stress))} cases",
              f"- More urgent than expected: {_share(sum(r['levels_above_expected'] > 0 for r in stress), len(stress))}",
              f"- Outcome driven by caution: {_share(sum(r['caution_drove_outcome'] for r in stress), len(stress))}",
              f"- Emergency outcomes: {_share(sum(r['acuity'] == 'emergency' for r in stress), len(stress))}",
              f"- Interactions per case: {round(mean(r['interactions'] for r in stress), 1)}", ""]

    lines += ["## Failures, case by case", ""]
    failures = _failures(cases, variants)
    if failures:
        lines += ["| Case | What | Expected | Engine gave | Decided by |", "| --- | --- | --- | --- | --- |"] + failures
    else:
        lines.append("None.")
    lines.append("")
    return "\n".join(lines + _file_problems(results))


def _failures(cases: list[dict], variants: list[dict]) -> list[str]:
    rows = []
    for case in cases:
        what = []
        if not case["gates"]["not_below_minimum_safe"]:
            what.append(f"**GATE: below minimum safe urgency ({case['minimum_safe_acuity']})**")
        for flag in case["gates"]["red_flags"]:
            if not flag["passed"]:
                what.append(f"**GATE: red flag \"{flag['description']}\" not escalated ({flag['recognition']})**")
            elif flag["recognition"] not in ("recognised", "not asked: already at an outcome this urgent"):
                what.append(f"red flag \"{flag['description']}\" escalated but {flag['recognition']}")
        levels = case["acuity_levels_above_expected"]
        if levels > 0:
            what.append(f"over-triage by {levels} level{'s' if levels > 1 else ''}")
        elif levels < 0:
            what.append(f"less urgent than expected by {-levels} level{'s' if levels < -1 else ''}")
        if levels == 0 and not case["agreement"]["level_of_care"]:
            what.append("level of care differs")
        if levels == 0 and case["agreement"]["level_of_care"] and not case["agreement"]["timeframe"]:
            what.append("timeframe differs")
        missing = [p["point"] for p in case["safety_netting"]["points"] if not p["covered"]]
        if missing:
            what.append("advice does not mention: " + "; ".join(missing))
        if not case["covered"]:
            what.append("not covered by a module")
        if what:
            rows.append(f"| {case['id']} | {'<br>'.join(what)} | {_triple(case['expected'])} | {_triple(case['actual'])} | "
                        f"{case['decided_by']['id']} ({case['decided_by']['source']}) |")
    for variant in variants:
        if not variant["same_outcome"]:
            rows.append(f"| {variant['variant']} | variant gave a different outcome from its base case | "
                        f"{_triple(variant['base_outcome'])} | {_triple(variant['outcome'])} | |")
    return rows


def _file_problems(results: dict) -> list[str]:
    if not results["file_problems"]:
        return []
    lines = ["## Vignette files with problems", "", "These files were left out of the run.", ""]
    for name, problems in results["file_problems"].items():
        lines += [f"- {name}: " + "; ".join(problems)]
    return lines + [""]


def render_external_report(results: dict) -> str:
    rows = results["cases"]
    lines = ["# Run report: published vignette sets", "",
             f"Knowledge base {results['versions']['knowledge_base']}. {len(rows)} published vignettes. Structured mode, no LLM.", "",
             "> **A sense check only.** These vignettes were written by other people for other purposes. They use "
             "coarser triage categories than this project, and some come from outside the UK. The published text was "
             "mapped onto this project's question list by AI, which loses detail. Not for clinical use.", ""]
    if not rows:
        lines += ["No published vignettes are available in `vignettes/external/`. See "
                  "`sources/external_vignette_sets.md` for the licence and availability checks.", ""]
        return "\n".join(lines + _file_problems(results))

    for set_name in sorted({row["set"] for row in rows}):
        subset = [row for row in rows if row["set"] == set_name]
        covered = [row for row in subset if row["covered"]]
        uncovered = [row for row in subset if not row["covered"]]
        lines += [f"## {set_name}", "",
                  f"{len(subset)} vignettes: {len(covered)} within current coverage, {len(uncovered)} outside it.", "",
                  "### Within current coverage", ""]
        if covered:
            lines += [f"- Same coarse category as published: {_share(sum(r['agrees'] for r in covered), len(covered))}",
                      f"- More urgent than published: {sum(r['categories_above_published'] > 0 for r in covered)}",
                      f"- **Less urgent than published: {sum(r['categories_above_published'] < 0 for r in covered)}**", "",
                      "| Case | Complaint | Published | Engine | Engine outcome | Decided by |", "| --- | --- | --- | --- | --- | --- |"]
            lines += [f"| {r['id']} | {r['presenting_text']} | {r['published'].replace('_', ' ')} | {r['engine'].replace('_', ' ')} | "
                      f"{r['engine_acuity']} / {r['engine_level_of_care']} | {r['decided_by']} |" for r in covered]
        else:
            lines.append("None.")
        lines += ["", "### Outside current coverage: a test of the \"not covered\" behaviour", "",
                  "The engine should say it does not cover these, run the universal red-flag screen, and give a "
                  "cautious default. It should never guess.", ""]
        if uncovered:
            emergencies = [r for r in uncovered if r["published"] == "emergency"]
            lines += [f"- Returned as \"not covered\": {_share(len(uncovered), len(uncovered))}",
                      f"- Published as emergencies: {len(emergencies)}. Of these, the universal red-flag screen raised "
                      f"an emergency in {sum(r['engine'] == 'emergency' for r in emergencies)}. **The other "
                      f"{sum(r['engine'] != 'emergency' for r in emergencies)} received the cautious default, which is "
                      f"less urgent than published.** This is the limit of covering only a few presenting symptoms.",
                      f"- Published as self-care: {sum(r['published'] == 'self_care' for r in uncovered)}. "
                      f"All received the cautious default, which is over-triage by design.",
                      f"- Engine outcomes: " + ", ".join(
                          f"{acuity} {sum(r['engine_acuity'] == acuity for r in uncovered)}"
                          for acuity in sorted({r['engine_acuity'] for r in uncovered})), ""]
        else:
            lines += ["None.", ""]
    return "\n".join(lines + _file_problems(results))


def render_disagreements(result_sets: list[dict]) -> str:
    """The disagreements log: every case where the engine and a vignette differ, with both sources."""
    lines = ["# Disagreements between the engine and the vignettes", "",
             "Generated by `python triage.py evaluate`. Do not edit by hand.", "",
             "Each entry is a case where the engine's outcome differs from the vignette's expected outcome, or a gate "
             "failed. Neither side is changed to force agreement. Each entry is for clinical review. The knowledge "
             "base is changed only where the source clearly supports the vignette.", "",
             "Both the content and the cases are AI-drafted and not clinically approved.", ""]
    count = 0
    for results in result_sets:
        title = SET_TITLES.get(results["set"], results["set"])
        for case in results["cases"]:
            gate_failed = not case["gates"]["not_below_minimum_safe"] or not case["gates"]["red_flags_passed"]
            if all(case["agreement"].values()) and not gate_failed:
                continue
            count += 1
            differs = [name.replace("_", " ") for name, same in case["agreement"].items() if not same]
            lines += [f"## {case['id']} ({title})", ""]
            if gate_failed:
                lines.append("- **A gate failed.** See the run report for this set.")
            if differs:
                lines.append(f"- Differs on: {', '.join(differs)}")
            lines += [f"- Vignette expects: {_triple(case['expected'])} (minimum safe acuity: {case['minimum_safe_acuity']})",
                      f"  - Source: {case['vignette_source']['page']}: \"{case['vignette_source']['quote']}\"",
                      f"- Engine gave: {_triple(case['actual'])}",
                      f"  - Decided by: {case['decided_by']['id']}: {case['decided_by']['description']}",
                      f"  - Source: {case['decided_by']['source']}",
                      "- Status: open, for clinical review", ""]
    if not count:
        lines.append("No disagreements in the latest runs.")
    return "\n".join(lines) + "\n"
