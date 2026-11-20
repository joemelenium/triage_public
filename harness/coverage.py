"""Reports coverage against the NHS website Symptoms A to Z list.

The end goal in the brief is full coverage: every entry on that list is either
handled by a module or deliberately returned as "not covered". Today anything
without a module is returned as "not covered" after the universal red-flag
screen, so every entry is in one of those two groups. This report shows how
many are in each.
"""

from pathlib import Path

from engine.kb import REPO_ROOT, KnowledgeBase

A_TO_Z_FILE = REPO_ROOT / "sources" / "nhs_uk" / "symptoms_a_to_z.tsv"


def render_coverage_report(kb: KnowledgeBase, list_file: Path = A_TO_Z_FILE) -> str:
    entries = [line.split("\t") for line in list_file.read_text(encoding="utf-8").splitlines()
               if line and not line.startswith("#")]
    pages: dict[str, list[str]] = {}          # page address -> the entry names that lead to it
    for name, address in entries:
        pages.setdefault(address, []).append(name)

    # A module covers a page when its presenting symptom was drafted from that page.
    covered: dict[str, str] = {}
    for module in kb.modules.values():
        source_ids = [kb.findings[module.presenting_finding].source] + list(module.also_covers)
        for source_id in source_ids:
            source = kb.sources.get(source_id)
            if not source:
                continue
            for address in pages:
                if source.url.rstrip("/").endswith(address.rstrip("/")):
                    covered.setdefault(address, module.name)

    lines = ["# Coverage against the NHS website Symptoms A to Z", "",
             f"Knowledge base {kb.settings.kb_version}. List accessed 2026-11-18: {len(entries)} entries, "
             f"leading to {len(pages)} different pages (some entries are cross-references).", "",
             "| | Pages | Share |", "| --- | --- | --- |",
             f"| Handled by a module | {len(covered)} | {round(100 * len(covered) / len(pages), 1)}% |",
             f"| Deliberately returned as \"not covered\" | {len(pages) - len(covered)} | "
             f"{round(100 * (len(pages) - len(covered)) / len(pages), 1)}% |", "",
             "A presentation with no module still gets the universal red-flag screen, then a cautious default "
             "outcome that says the tool does not cover it. The engine never guesses.", "",
             "## Handled by a module", ""]
    lines += [f"- {module_name} ({address})" for address, module_name in covered.items()] or ["None."]
    lines += ["", "## Returned as \"not covered\"", ""]
    lines += [f"- {names[0]}" for address, names in pages.items() if address not in covered]
    return "\n".join(lines) + "\n"
