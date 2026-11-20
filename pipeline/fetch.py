"""Fetch a public web page, save a dated plain-text snapshot, and add it to the source log.

A content-building tool, not part of the engine. Pages are read a few at a time.

    python triage.py fetch-source nhs_asthma https://www.nhs.uk/conditions/asthma/ "Asthma"
"""

import html
import re
import time
import urllib.request
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOTS = ROOT / "sources" / "nhs_uk"
SOURCE_LOG = ROOT / "sources" / "source_log.yaml"
POLITE_PAUSE = 3  # seconds between requests


def _plain_text(page: str) -> str:
    """The main content of a page as plain text: headings, paragraphs and list items."""
    main = re.search(r"<main.*?</main>", page, re.S)
    page = main.group(0) if main else page
    page = re.sub(r"<(script|style|nav|footer|svg)[^>]*>.*?</\1>", "", page, flags=re.S)
    page = re.sub(r"<li[^>]*>", "\n-   ", page)
    page = re.sub(r"</(p|h[1-6]|li|div|section|tr)>", "\n", page)
    page = re.sub(r"<br\s*/?>", "\n", page)
    text = html.unescape(re.sub(r"<[^>]+>", "", page))
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    out, blank = [], False
    for line in lines:
        if line in ("", "-"):
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(line)
            blank = False
    return "\n".join(out).strip() + "\n"


def fetch(source_id: str, url: str, title: str, used_for: str = "Content drafting", log: str | None = None) -> Path:
    if not re.fullmatch(r"[a-z0-9_]+", source_id):
        raise ValueError("The source id must be lower case letters, numbers and underscores")
    request = urllib.request.Request(url, headers={"User-Agent": "triage-exemplar-content-tool"})
    with urllib.request.urlopen(request, timeout=30) as response:
        final_url, page = response.geturl(), response.read().decode("utf-8", errors="replace")
    time.sleep(POLITE_PAUSE)
    today = date.today().isoformat()
    reviewed = re.search(r"Page last reviewed:\s*([0-9]{1,2} \w+ [0-9]{4})", page)
    snapshot = SNAPSHOTS / f"{source_id.removeprefix('nhs_')}.txt"
    snapshot.write_text(
        f"Source: {final_url}\nAccessed: {today}\n"
        "Licence: Contains public sector information licensed under the Open Government Licence v3.0.\n"
        "Note: Plain-text snapshot kept for traceability. Not the live page.\n----\n" + _plain_text(page),
        encoding="utf-8")
    # A per-body-system log (sources/source_logs/<log>.yaml) lets parallel builds avoid editing the same file.
    target = SOURCE_LOG if not log else SOURCE_LOG.parent / "source_logs" / f"{log}.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    for path in [SOURCE_LOG] + sorted((SOURCE_LOG.parent / "source_logs").glob("*.yaml")):
        existing += yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not any(entry["id"] == source_id for entry in existing):
        entry = {"id": source_id, "title": title, "url": final_url, "accessed": today, "licence": "OGL v3.0",
                 "used_for": used_for}
        if reviewed:
            entry["note"] = f"Page last reviewed: {reviewed.group(1)}"
        with open(target, "a", encoding="utf-8") as handle:
            handle.write("\n" + yaml.safe_dump([entry], sort_keys=False, allow_unicode=True))
    return snapshot
