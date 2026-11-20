"""Command line for the adaptive triage exemplar. NOT FOR CLINICAL USE.

    python triage.py check                 check the knowledge base loads cleanly
    python triage.py run examples/FILE     run one example case and show the outcome
    python triage.py ask                   answer the questions yourself
    python triage.py evaluate              run the development test cases and write a report
    python triage.py evaluate holdout      run the holdout test cases (only at the end of a wave)
    python triage.py evaluate external     run the published vignette sets
    python triage.py review-pack           write the review pack for each presenting symptom
    python triage.py coverage              report coverage against the NHS Symptoms A to Z list
    python triage.py sweep                 rerun the development cases at several levels of caution
    python triage.py snomed-search "term"  find SNOMED CT concepts in the NHS browser (content building)
    python triage.py snomed-add CODE       check a SNOMED CT code and add it to the log (content building)
    python triage.py fetch-source ID URL "Title"   save a dated snapshot of a page and log it (content building)
    python triage.py selftest              check each condition can be recognised from its own card
    python triage.py export-questions      write the question list that vignette authors may see
"""

import argparse
import json
import sys
from pathlib import Path

from engine import DISCLAIMER
from engine.kb import KnowledgeBaseError, load_knowledge_base
from engine.report import describe
from engine.runner import load_case, run_case
from engine.session import run
from engine.trace import write_trace


def command_check(kb, args) -> None:
    rules = len(kb.universal.rules) + sum(len(m.red_flags) + len(m.outcome_rules) for m in kb.modules.values())
    print(f"Knowledge base {kb.settings.kb_version} loaded with no problems ({kb.settings.status}).")
    print(f"  Entry symptoms: {', '.join(m.name for m in kb.modules.values())}")
    print(f"  Findings:   {len(kb.findings)}")
    print(f"  Rules:      {rules}")
    print(f"  Conditions: {len(kb.conditions)}")
    print(f"  Sources:    {len(kb.sources)}")
    from engine.kb import network_warnings
    warnings = network_warnings(kb)
    print(f"  Network warnings: {len(warnings)}")
    for warning in warnings:
        print(f"    - {warning}")
    from statistics import median
    from engine.plain_language import patient_facing_texts, reading_grade
    grades = [reading_grade(text) for _, text in patient_facing_texts(kb)]
    print(f"  Reading level of patient text: median US school grade {median(grades):.1f} "
          f"(about reading age {median(grades) + 5:.0f}; the aim is 9 to 11)")


def command_run(kb, args) -> None:
    record = run_case(kb, load_case(args.case))
    if not args.no_trace:
        write_trace(record)
    print(json.dumps(record, indent=2, ensure_ascii=False) if args.json else describe(record))


def command_ask(kb, args) -> None:
    print(DISCLAIMER, "\n")
    modules = list(kb.modules.values())
    print("What is the main problem? Type the numbers that apply, separated by commas.")
    for number, module in enumerate(modules, start=1):
        print(f"  {number}. {module.name}")
    print("  0. Something else")
    picked = _numbers(input("> "), len(modules))
    presenting = [modules[n - 1].presenting_finding for n in picked] or ["something_else"]

    age_text = input("Age in years (press Enter to skip): ").strip()
    case = {"presenting": presenting, "context": {"age": int(age_text)} if age_text.isdigit() else {}}

    answers: list[dict] = []
    while True:
        step = run(kb, case, answers)
        if step["status"] == "outcome":
            break
        question = step["question"]
        print(f"\nQuestion {question['number']}: {question['text']}")
        if question["kind"] == "single":
            reply = ""
            while reply not in ("y", "n", "?"):
                reply = input("  y = yes, n = no, ? = not sure > ").strip().lower()
            answer = {"y": "yes", "n": "no", "?": "not_sure"}[reply]
        else:
            for number, option in enumerate(question["options"], start=1):
                print(f"  {number}. {option['text']}")
            reply = input("  Type the numbers that apply, 0 for none, ? for not sure > ").strip()
            if reply == "?":
                answer = "not_sure"
            else:
                answer = [question["options"][n - 1]["finding"] for n in _numbers(reply, len(question["options"]))]
        answers.append({"question_id": question["id"], "answer": answer})

    record = step["record"]
    if not args.no_trace:
        write_trace(record)
    print("\n" + describe(record))


def command_evaluate(kb, args) -> None:
    from harness.evaluate import evaluate_external, evaluate_set
    from harness.report import render_disagreements, render_external_report, render_set_report

    reports = Path(__file__).resolve().parent / "reports"
    reports.mkdir(exist_ok=True)
    if args.set == "external":
        results = evaluate_external(kb)
        text = render_external_report(results)
    else:
        results = evaluate_set(kb, args.set)
        text = render_set_report(results)
    (reports / f"{args.set}_results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    report_file = reports / f"{args.set}_report.md"
    report_file.write_text(text, encoding="utf-8")

    # Keep the disagreements log in step with the latest dev and holdout runs.
    saved = [json.loads(path.read_text(encoding="utf-8")) for path in
             (reports / "dev_results.json", reports / "holdout_results.json") if path.exists()]
    review = Path(__file__).resolve().parent / "review"
    (review / "disagreements.md").write_text(render_disagreements(saved), encoding="utf-8")

    if args.set == "external":
        cases = results["cases"]
        print(f"{len(cases)} published vignettes run, {sum(c['covered'] for c in cases)} within current coverage.")
    elif results["summary"]["cases"]:
        summary = results["summary"]
        gates = summary["gates"]
        total = summary["cases"]
        print(f"{total} cases run from the {args.set} set.")
        print(f"  GATE red flags detected and escalated: {gates['red_flags_passed']} of {gates['red_flags_total']}")
        print(f"  GATE not below minimum safe urgency:   {total - len(gates['cases_below_minimum_safe'])} of {total}")
        print(f"  Acuity matches expected:               {summary['agreement']['acuity']} of {total}")
        print(f"  Over-triage:                           {summary['over_triage']['cases']} of {total}")
        print(f"  Interactions per case (mean):          {summary['burden']['interactions_mean']}")
    else:
        print(f"No valid vignettes found in the {args.set} set.")
    if results["file_problems"]:
        print(f"  {len(results['file_problems'])} vignette files had problems and were left out.")
    print(f"Report written to {report_file.relative_to(Path.cwd()) if report_file.is_relative_to(Path.cwd()) else report_file}")


def command_review_pack(kb, args) -> None:
    from harness.review_pack import write_review_packs
    for path in write_review_packs(kb):
        print(f"Wrote {path.name}")


def command_coverage(kb, args) -> None:
    from harness.coverage import render_coverage_report
    reports = Path(__file__).resolve().parent / "reports"
    reports.mkdir(exist_ok=True)
    text = render_coverage_report(kb)
    (reports / "coverage_report.md").write_text(text, encoding="utf-8")
    print("\n".join(text.splitlines()[2:8]))
    print("Report written to reports/coverage_report.md")


def command_sweep(kb, args) -> None:
    from harness.sweep import run_sweep
    reports = Path(__file__).resolve().parent / "reports"
    reports.mkdir(exist_ok=True)
    text = run_sweep("dev")
    (reports / "sweep_report.md").write_text(text, encoding="utf-8")
    print("\n".join(line for line in text.splitlines() if line.startswith("|")))
    print("Report written to reports/sweep_report.md")


def command_snomed_search(kb, args) -> None:
    from pipeline.snomed import search
    for match in search(" ".join(args.term)):
        print(f"{match['code']:>18}  {match['name']}")


def command_snomed_add(kb, args) -> None:
    from pipeline.snomed import add_to_log
    result = add_to_log(args.code, args.log)
    where = f"sources/snomed_codes/{args.log}.yaml" if args.log else "sources/snomed_codes.yaml"
    status = "already in the log" if result["already_logged"] else f"added to {where}"
    print(f"{result['code']}  {result['name']}: {status}")


def command_fetch_source(kb, args) -> None:
    from pipeline.fetch import fetch
    print(f"Saved {fetch(args.id, args.url, args.title, log=args.log)}")


def command_selftest(kb, args) -> None:
    from pipeline.selftest import run_selftests
    results = run_selftests(kb)
    failed = [r for r in results if not (r["recognised"] and r["urgent_enough"])]
    for r in failed:
        problems = ([] if r["recognised"] else [f"ranked {r['rank'] or 'not listed'}"]) + \
                   ([] if r["urgent_enough"] else [f"outcome {r['outcome']}, needs {r['needed']}"])
        print(f"  {r['condition']} (from {r['entry']}): " + "; ".join(problems))
    print(f"{len(results) - len(failed)} of {len(results)} condition self-tests passed.")
    if failed:
        sys.exit(1)


def command_export_questions(kb, args) -> None:
    from harness.authoring import export_authoring_files
    for path in export_authoring_files(kb):
        print(f"Wrote {path.name}")


def _numbers(text: str, highest: int) -> list[int]:
    """Read '1, 3' as [1, 3]. Anything out of range is ignored."""
    found = []
    for part in text.replace(" ", "").split(","):
        if part.isdigit() and 1 <= int(part) <= highest and int(part) not in found:
            found.append(int(part))
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description="Adaptive triage exemplar. NOT FOR CLINICAL USE.")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("check", help="check the knowledge base loads cleanly")

    run_parser = commands.add_parser("run", help="run one example case")
    run_parser.add_argument("case", help="path to a case file, for example examples/chest_pain_emergency.yaml")
    run_parser.add_argument("--json", action="store_true", help="print the full JSON record")
    run_parser.add_argument("--no-trace", action="store_true", help="do not write a trace file")

    ask_parser = commands.add_parser("ask", help="answer the questions yourself")
    ask_parser.add_argument("--no-trace", action="store_true", help="do not write a trace file")

    evaluate_parser = commands.add_parser("evaluate", help="run a set of test cases and write a report")
    evaluate_parser.add_argument("set", nargs="?", default="dev", choices=["dev", "holdout", "external"])
    commands.add_parser("review-pack", help="write the review pack for each presenting symptom")
    commands.add_parser("export-questions", help="write the question list that vignette authors may see")
    commands.add_parser("coverage", help="report coverage against the NHS Symptoms A to Z list")
    commands.add_parser("sweep", help="rerun the development cases at several levels of caution")
    search_parser = commands.add_parser("snomed-search", help="find SNOMED CT concepts in the NHS browser")
    search_parser.add_argument("term", nargs="+")
    add_parser = commands.add_parser("snomed-add", help="check a SNOMED CT code and add it to the log")
    add_parser.add_argument("code")
    add_parser.add_argument("--log", help="body system: write to sources/snomed_codes/<log>.yaml")
    fetch_parser = commands.add_parser("fetch-source", help="save a dated snapshot of a page and log it")
    fetch_parser.add_argument("--log", help="body system: write to sources/source_logs/<log>.yaml")
    fetch_parser.add_argument("id")
    fetch_parser.add_argument("url")
    fetch_parser.add_argument("title")
    commands.add_parser("selftest", help="check each condition can be recognised from its own card")
    serve_parser = commands.add_parser("serve", help="start the API and demo page on this computer")
    serve_parser.add_argument("--port", type=int, default=8000)

    args = parser.parse_args()
    if args.command == "serve":
        # Listens on this computer only (127.0.0.1). The engine itself makes no network calls.
        import uvicorn
        print(f"Demo page: http://127.0.0.1:{args.port}   API docs: http://127.0.0.1:{args.port}/docs")
        uvicorn.run("api.server:app", host="127.0.0.1", port=args.port)
        return
    if args.command in ("snomed-search", "snomed-add", "fetch-source"):
        # Content-building tools work even while the knowledge base is being edited.
        {"snomed-search": command_snomed_search, "snomed-add": command_snomed_add,
         "fetch-source": command_fetch_source}[args.command](None, args)
        return
    try:
        kb = load_knowledge_base()
    except KnowledgeBaseError as error:
        sys.exit(f"{error}")
    {"check": command_check, "run": command_run, "ask": command_ask, "evaluate": command_evaluate,
     "review-pack": command_review_pack, "export-questions": command_export_questions,
     "coverage": command_coverage, "sweep": command_sweep,
     "snomed-search": command_snomed_search, "snomed-add": command_snomed_add,
     "fetch-source": command_fetch_source, "selftest": command_selftest}[args.command](kb, args)


if __name__ == "__main__":
    main()
