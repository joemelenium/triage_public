"""An API in the common shape of condition-based triage engine APIs, over this engine.

NOT FOR CLINICAL USE. A demonstration and proof of concept only.

Why this shape: an evaluation designed for a commercial condition-based engine
can then call this mock, or a real engine, with little change.
Only the published shape is copied (field names and levels); no content is
taken from any product. Ids are this engine's own (for example "chest_pain").

How it works. Like those APIs, this one keeps nothing between calls: the caller
sends all the evidence each time. The engine is stateless and deterministic, so
each call replays the interview from the start, answering each question the
engine asks from the evidence. The first question the evidence cannot answer is
the next question. When there is none, the interview is over.

Evidence "source":
  initial      what the person said at the start. Initial evidence that is a
               main symptom (an entry symptom) starts that symptom's questions.
  predefined   known before the interview (history and risk factors)
  (anything else, or none)  an answer to a question the engine asked
"""

from engine.kb import KnowledgeBase
from engine.logic import NO, NOT_SURE, YES
from engine.session import run

CHOICES = {"present": YES, "absent": NO, "unknown": NOT_SURE}
CHOICE_LABELS = [{"id": "present", "label": "Yes"}, {"id": "absent", "label": "No"},
                 {"id": "unknown", "label": "Don't know"}]
DISCLAIMER = ("Demonstration only. Not for clinical use and not medical advice. Content is AI-drafted and "
              "has not been clinically reviewed. For a real concern, call 999 in an emergency or use 111.")


class BadRequest(ValueError):
    """The request cannot be used. The message says why, in plain words."""


class _NeedsAsking(Exception):
    """The engine asked a question the evidence does not answer yet."""


def to_case(kb: KnowledgeBase, request: dict) -> tuple[dict, dict[str, str]]:
    """Turn a request into the engine's case, plus the answers to questions."""
    sex = request.get("sex")
    if sex not in ("female", "male"):
        raise BadRequest("'sex' must be 'female' or 'male'")
    age = request.get("age") or {}
    if not isinstance(age, dict) or not isinstance(age.get("value"), (int, float)) or age["value"] < 0:
        raise BadRequest("'age' must look like {\"value\": 30} (in years), or {\"value\": 8, \"unit\": \"month\"}")
    years = age["value"] / 12 if age.get("unit") == "month" else age["value"]

    presenting, opening, answers = [], {}, {}
    for item in request.get("evidence") or []:
        finding_id, choice = item.get("id"), item.get("choice_id")
        if finding_id not in kb.findings:
            raise BadRequest(f"Unknown evidence id '{finding_id}'. GET /symptoms lists them.")
        if choice not in CHOICES:
            raise BadRequest(f"'choice_id' for '{finding_id}' must be present, absent or unknown")
        answer = CHOICES[choice]
        if item.get("source") in ("initial", "predefined"):
            if item.get("source") == "initial" and answer == YES and finding_id in _entry_findings(kb):
                presenting.append(finding_id)
            else:
                opening[finding_id] = answer
        else:
            answers[finding_id] = answer
    if not presenting:
        raise BadRequest("Give at least one main symptom as initial evidence that is present. "
                         "GET /symptoms?entry=true lists them.")

    case = {"presenting": presenting, "opening_findings": opening, "context": {"age": years, "sex": sex}}
    respondent = (request.get("extras") or {}).get("respondent")
    if respondent in ("patient", "carer"):
        case["respondent"] = respondent
    return case, answers


def interview(kb: KnowledgeBase, request: dict) -> dict:
    """Replay the interview from the evidence. Returns the engine's result:
    {"status": "question", ...} with the next question, or {"status": "outcome", "record": ...}."""
    case, answers = to_case(kb, request)
    given = []

    def answer_from_evidence(question):
        ids = [option["finding"] for option in question["options"]]
        if question["kind"] == "single" and ids[0] in answers:
            answer = answers[ids[0]]
        elif question["kind"] != "single" and all(f in answers for f in ids):
            answer = {f: answers[f] for f in ids}
        else:
            raise _NeedsAsking(question)
        given.append({"question_id": question["id"], "answer": answer})
        return answer

    try:
        return run(kb, case, [], answer_next=answer_from_evidence)
    except _NeedsAsking:
        # Replay with the answers given so far: the engine then returns the next
        # question, with the likely conditions so far.
        return run(kb, case, given)


def diagnosis(kb: KnowledgeBase, request: dict) -> dict:
    """POST /diagnosis: the next question and the likely conditions so far."""
    result = interview(kb, request)
    if result["status"] == "question":
        causes, emergency = result["possible_causes"], result["emergency_evidence_found"]
        question = _question(kb, result["question"], request)
    else:
        record = result["record"]
        causes, question = record["possible_causes"]["causes"], None
        emergency = any(flag["acuity"] == "emergency" for flag in record["red_flags_found"])
    return {
        "question": question,
        "conditions": _conditions(causes),
        "extras": {},
        "has_emergency_evidence": emergency,
        "should_stop": question is None,
        "disclaimer": DISCLAIMER,
    }


def triage(kb: KnowledgeBase, request: dict) -> dict:
    """POST /triage: the triage level, for the evidence so far.

    If questions are still to be asked, the level is given from what is known now
    and "interview_finished" is false: the engine treats anything not yet asked as
    missing, so the level may be lower or higher than at the end."""
    result = interview(kb, request)
    finished = result["status"] == "outcome"
    if not finished:
        # Finish the interview with "unknown" for everything not yet answered, as the
        # engine would for a person who stops answering.
        case, answers = to_case(kb, request)

        def answer_or_unknown(question):
            ids = [option["finding"] for option in question["options"]]
            if question["kind"] == "single":
                return answers.get(ids[0], NOT_SURE)
            return {f: answers.get(f, NOT_SURE) for f in ids}

        result = run(kb, case, [], answer_next=answer_or_unknown)
    record = result["record"]
    summary = record["five_level_triage"]
    return {
        "triage_level": summary["triage_level"],
        "root_cause": summary["root_cause"],
        "serious": [{"id": s["id"], "name": s["label"], "common_name": s["label"],
                     "is_emergency": s["seriousness"] == "emergency"} for s in summary["serious"]],
        "teleconsultation_applicable": summary["triage_level"] in ("consultation", "self_care"),
        "interview_finished": finished,
        "extras": {
            "outcome": record["outcome"],
            "advice": record["advice"],
            "rationale": record["rationale"],
            "decided_by": record["decided_by"],
            "red_flags_found": record["red_flags_found"],
            "conditions": _conditions(record["possible_causes"]["causes"]),
        },
        "disclaimer": DISCLAIMER,
    }


def symptoms(kb: KnowledgeBase, entry_only: bool = False) -> list[dict]:
    """GET /symptoms: every observation that can be evidence."""
    entry = _entry_findings(kb)
    return [_finding(kb, f.id) for f in kb.findings.values()
            if f.kind != "context" and (not entry_only or f.id in entry)]


def search(kb: KnowledgeBase, phrase: str, max_results: int = 8) -> list[dict]:
    """GET /search: main symptoms whose name or everyday wording matches the phrase."""
    words = phrase.lower().split()
    if not words:
        return []
    matches = []
    for module in kb.modules.values():
        finding = kb.findings[module.presenting_finding]
        text = " ".join([module.name, finding.label, *finding.phrases]).lower()
        if all(word in text for word in words):
            # Names that start with the phrase come first.
            matches.append((not module.name.lower().startswith(phrase.lower()), module.name, finding.id))
    return [{"id": finding_id, "label": name} for _, name, finding_id in sorted(matches)[:max_results]]


def conditions(kb: KnowledgeBase) -> list[dict]:
    """GET /conditions: every condition card."""
    return [condition(kb, condition_id) for condition_id in kb.conditions]


def condition(kb: KnowledgeBase, condition_id: str) -> dict:
    card = kb.conditions[condition_id]
    return {"id": card.id, "name": card.medical_name or card.name, "common_name": card.name,
            "snomed": card.snomed, "acuity_needed": card.acuity_needed, "danger": card.danger,
            "prevalence": card.prevalence, "sex_filter": card.sex or "both"}


def _entry_findings(kb: KnowledgeBase) -> set[str]:
    return {module.presenting_finding for module in kb.modules.values()}


def _finding(kb: KnowledgeBase, finding_id: str) -> dict:
    finding = kb.findings[finding_id]
    return {"id": finding.id, "name": finding.label, "common_name": finding.label,
            "question": finding.question, "snomed": finding.snomed,
            "type": "risk_factor" if finding.kind == "history" else "symptom",
            "is_entry_symptom": finding.id in _entry_findings(kb)}


def _question(kb: KnowledgeBase, question: dict, request: dict) -> dict:
    if question["kind"] == "single":
        finding_id = question["options"][0]["finding"]
        items = [{"id": finding_id, "name": kb.findings[finding_id].label, "choices": CHOICE_LABELS}]
        kind = "single"
    else:
        items = [{"id": option["finding"], "name": option["text"], "choices": CHOICE_LABELS}
                 for option in question["options"]]
        kind = "group_multiple"
    return {"type": kind, "text": question["text"], "items": items,
            "extras": {"question_id": question["id"], "reason": question["reason"]}}


def _conditions(causes: list[dict]) -> list[dict]:
    return [{"id": c["id"], "name": c["name"], "common_name": c["common_name"], "probability": c["likelihood"]}
            for c in causes if c["id"] != "other_cause"]
