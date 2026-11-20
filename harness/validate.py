"""Checks every vignette file and prints any problems.

    python -m harness.validate              check the dev and holdout sets
    python -m harness.validate dev          check one set

It prints file names and what is wrong with each. It never runs the triage
engine, so it tells an author nothing about how the engine would handle a case.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # also works as "python3 harness/validate.py"

from engine.kb import KnowledgeBaseError, load_knowledge_base
from harness.vignette import check_folder, vignette_files


def main() -> None:
    set_names = tuple(sys.argv[1:]) or ("dev", "holdout")
    try:
        kb = load_knowledge_base()
    except (KnowledgeBaseError, Exception):
        # Never print the details: test-case authors run this, and the details
        # would show them knowledge base content.
        print("The checker cannot run right now because the engine's files are being changed. Try again in a few minutes.")
        sys.exit(2)
    report = check_folder(kb, set_names)
    total = sum(len(vignette_files(name)) for name in set_names)
    for label, problems in report.items():
        print(label)
        for problem in problems:
            print(f"  - {problem}")
    print(f"{total} vignette files checked, {len(report)} with problems.")
    sys.exit(1 if report else 0)


if __name__ == "__main__":
    main()
