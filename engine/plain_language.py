"""Checks that text a patient sees is in plain language.

Three checks:
  - avoided words: words the NHS "A to Z of NHS health writing" tells writers to
    avoid, such as "fever" (use "high temperature") or "risk" (use "chance")
  - medical words: a word listed under "explain" in knowledge_base/plain_language.yaml
    may only be used where the same text also explains it
  The first two are checked when the knowledge base loads, so they cannot be forgotten.
  - reading level: an estimate of the school grade needed to read each piece
    of text (reported by "python triage.py check" and tested)

Aim, from the brief: a reading age of 9 to 11, which is roughly US school
grade 4 to 6. The NHS service manual's health literacy guide recommends using
readability scores only to help prioritise, and testing with users instead. So
the reading level here is a rough guard, not proof that text is easy to use.
"""

import re

# Reading level limits, as US school grades. The median is the aim; the maximum
# catches any single question or line that is much too hard. The formula is not
# reliable on very short phrases (a two-word name can score as university level),
# so the maximum is only applied to text of at least MIN_WORDS_FOR_MAX words.
MEDIAN_GRADE_LIMIT = 6.0
MAX_GRADE_LIMIT = 9.0
MIN_WORDS_FOR_MAX = 10


def _contains_term(text: str, term: str) -> bool:
    return re.search(r"\b" + re.escape(term.lower()), text.lower()) is not None


def unexplained_terms(text: str, glossary, skip_terms=()) -> list[str]:
    """Medical words used in this text without a plain explanation alongside them."""
    lowered = text.lower()
    return [entry.term for entry in glossary
            if entry.term not in skip_terms and _contains_term(text, entry.term)
            and not any(phrase.lower() in lowered for phrase in entry.explained_by)]


def avoided_words(text: str, avoided) -> list:
    """Words in this text that the NHS A to Z of health writing says to avoid."""
    lowered = text.lower()
    return [word for word in avoided
            if re.search(r"\b" + re.escape(word.term.lower()) + r"\b", lowered)
            and not any(phrase.lower() in lowered for phrase in word.unless_with)]


def _syllables(word: str) -> int:
    word = word.lower()
    count = len(re.findall(r"[aeiouy]+", word))
    if word.endswith("e") and not word.endswith(("le", "ee")) and count > 1:
        count -= 1
    return max(count, 1)


def reading_grade(text: str) -> float:
    """Flesch-Kincaid grade: roughly the US school year needed to read the text.

    A rough measure. Short, common words and short sentences give a low grade.
    """
    words = re.findall(r"[A-Za-z']+", text)
    if not words:
        return 0.0
    sentences = max(len(re.findall(r"[.!?]+", text)), 1)
    return 0.39 * len(words) / sentences + 11.8 * sum(map(_syllables, words)) / len(words) - 15.59


def patient_facing_texts(kb) -> list[tuple[str, str]]:
    """Every piece of text a patient sees, as (where it is, the text)."""
    texts = [(f"question '{f.id}'", f.question) for f in kb.findings.values()]
    texts += [(f"carer question '{f.id}'", f.question_carer) for f in kb.findings.values() if f.question_carer]
    texts += [(f"checklist line '{f.id}'", f.checklist_text) for f in kb.findings.values() if f.checklist_text]
    texts += [(f"screen '{s.id}'", s.question)
              for s in [kb.universal.screen] + [s for m in kb.modules.values() for s in m.screens]]
    for advice in kb.advice.values():
        lines = [advice.what_to_do, advice.where_to_go] + advice.look_out_for + advice.get_more_help_when + advice.self_care
        texts += [(f"advice '{advice.id}'", line) for line in lines]
    texts += [(f"condition name '{c.id}'", c.name) for c in kb.conditions.values()]
    return texts
