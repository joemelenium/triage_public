"""Look up SNOMED CT concepts in the NHS SNOMED CT Browser and log checked codes.

This is a content-building tool. It is not part of the engine: the engine makes
no network calls. Only codes recorded in sources/snomed_codes.yaml may be used
in the knowledge base.

    python triage.py snomed-search "chest pain"       find candidate concepts
    python triage.py snomed-add 29857009              check a code and add it to the log
"""

import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

EDITION = "uk-edition/v20260923"
BASE = f"https://termbrowser.nhs.uk/sct-browser-api/snomed/{EDITION}"
SOURCE_NAME = f"NHS SNOMED CT Browser, UK Edition {EDITION.split('/')[1]} (termbrowser.nhs.uk)"
LOG = Path(__file__).resolve().parent.parent / "sources" / "snomed_codes.yaml"


def _get(url: str):
    """Fetch JSON, retrying a few times: the browser sometimes returns a temporary error."""
    error = None
    for attempt in range(4):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except Exception as caught:  # network errors are retried, then reported
            error = caught
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Could not reach the NHS SNOMED CT Browser: {error}")


def search(term: str, limit: int = 10) -> list[dict]:
    """Active concepts whose descriptions match the term, best matches first."""
    query = urllib.parse.urlencode({"query": term, "searchMode": "partialMatching", "lang": "english",
                                    "statusFilter": "activeOnly", "skipTo": 0, "returnLimit": 25, "normalize": "true"})
    seen, results = set(), []
    for match in _get(f"{BASE}/descriptions?{query}").get("matches", []):
        if match["conceptId"] not in seen and match.get("conceptActive", True):
            seen.add(match["conceptId"])
            results.append({"code": match["conceptId"], "name": match["fsn"]})
    return results[:limit]


def concept(code: str) -> dict:
    """The concept's fully specified name and whether it is active."""
    data = _get(f"{BASE}/concepts/{code}")
    return {"code": code, "name": data.get("fullySpecifiedName") or data.get("defaultTerm"), "active": data.get("active")}


def add_to_log(code: str, log: str | None = None) -> dict:
    """Check a code in the browser and add it to the log of checked codes, if it is active.

    log: write to sources/snomed_codes/<log>.yaml, so parallel builds avoid editing the same file.
    """
    found = concept(code)
    if not found["active"]:
        raise ValueError(f"SNOMED CT {code} ({found['name']}) is not active, so it cannot be used")
    entries = []
    for path in [LOG] + sorted((LOG.parent / "snomed_codes").glob("*.yaml")):
        entries += yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if any(entry["code"] == code for entry in entries):
        return {**found, "already_logged": True}
    target = LOG if not log else LOG.parent / "snomed_codes" / f"{log}.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "a", encoding="utf-8") as handle:
        handle.write(yaml.safe_dump([{"code": code, "name": found["name"], "checked_against": SOURCE_NAME,
                                      "checked_on": date.today().isoformat()}], sort_keys=False, allow_unicode=True))
    return {**found, "already_logged": False}
