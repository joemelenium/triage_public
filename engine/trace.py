"""Writes a trace of each session as JSON lines (one JSON object per line).

Traces are local logs for inspecting how the engine reached an outcome. They
are not committed to the repository, and trace writing is switched off in any
hosted demo so that nothing a visitor enters is stored.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from .kb import REPO_ROOT

DEFAULT_TRACE_FILE = REPO_ROOT / "traces" / "sessions.jsonl"


def write_trace(record: dict, trace_file: Path = DEFAULT_TRACE_FILE) -> Path:
    """Add one session to the trace file: a line per question, then the outcome."""
    trace_file = Path(trace_file)
    trace_file.parent.mkdir(parents=True, exist_ok=True)
    # The session id is a timestamp. It is made here, outside the engine, so the
    # engine's own output stays identical from run to run.
    session = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")

    lines = [{"session": session, "event": "start", "case": record["case"], "versions": record["versions"]}]
    for question in record["questions_asked"]:
        lines.append({"session": session, "event": "question", **question})
    lines.append({"session": session, "event": "outcome", "record": record})

    with open(trace_file, "a", encoding="utf-8") as handle:
        for line in lines:
            handle.write(json.dumps(line, ensure_ascii=False) + "\n")
    return trace_file
