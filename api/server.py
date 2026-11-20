"""The local web server: the API and the demo page.

NOT FOR CLINICAL USE. A demonstration and proof of concept only.

Start it with:  python3 triage.py serve
Then open http://127.0.0.1:8000 for the demo page, or /docs for the API.

It listens on this computer only. The engine makes no network calls, and
nothing anyone enters is stored: each request is worked out and forgotten.
"""

from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from engine import ENGINE_VERSION
from engine.kb import load_knowledge_base

from . import interview as api

KB = load_knowledge_base()
PAGE = Path(__file__).parent / "static" / "index.html"

app = FastAPI(
    title="Triage engine mock (not for clinical use)",
    version=ENGINE_VERSION,
    description="A mock of a condition-based triage engine, in the common shape of condition-based engine APIs, for testing "
                "an evaluation design. " + api.DISCLAIMER,
)


class Age(BaseModel):
    value: float
    unit: Literal["year", "month"] = "year"


class Evidence(BaseModel):
    id: str
    choice_id: Literal["present", "absent", "unknown"]
    source: str | None = None   # "initial" for what the person said at the start


class InterviewRequest(BaseModel):
    sex: Literal["female", "male"]
    age: Age
    evidence: list[Evidence]
    extras: dict = {}            # {"respondent": "carer"} when someone answers for another person


def _call(function, request: InterviewRequest) -> dict:
    try:
        return function(KB, request.model_dump())
    except api.BadRequest as problem:
        raise HTTPException(status_code=400, detail=str(problem))


@app.get("/", include_in_schema=False)
def demo_page():
    return FileResponse(PAGE)


@app.get("/info")
def info():
    return {"engine_version": ENGINE_VERSION, "knowledge_base_version": KB.settings.kb_version,
            "conditions_count": len(KB.conditions), "symptoms_count": len(api.symptoms(KB)),
            "entry_symptoms_count": len(KB.modules), "disclaimer": api.DISCLAIMER}


@app.get("/search")
def search(phrase: str, max_results: int = 8):
    """Main symptoms whose name or everyday wording matches the phrase."""
    return api.search(KB, phrase, max_results)


@app.get("/symptoms")
def symptoms(entry: bool = False):
    """Every observation that can be evidence. entry=true lists only the main symptoms."""
    return api.symptoms(KB, entry_only=entry)


@app.get("/symptoms/{symptom_id}")
def symptom(symptom_id: str):
    if symptom_id not in KB.findings:
        raise HTTPException(status_code=404, detail=f"No symptom '{symptom_id}'")
    return api._finding(KB, symptom_id)


@app.get("/conditions")
def conditions():
    return api.conditions(KB)


@app.get("/conditions/{condition_id}")
def condition(condition_id: str):
    if condition_id not in KB.conditions:
        raise HTTPException(status_code=404, detail=f"No condition '{condition_id}'")
    return api.condition(KB, condition_id)


@app.post("/diagnosis")
def diagnosis(request: InterviewRequest):
    """The next question, and the likely conditions so far. should_stop is true when the interview is over."""
    return _call(api.diagnosis, request)


@app.post("/triage")
def triage(request: InterviewRequest):
    """The triage level (five levels, from emergency_ambulance to self_care), with the outcome, advice and reasons."""
    return _call(api.triage, request)
