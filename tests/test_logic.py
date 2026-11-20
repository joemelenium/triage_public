"""Checks the yes / no / unknown logic that rules are built on."""

from engine.logic import evaluate, open_findings


def test_not_sure_is_unknown_never_no():
    assert evaluate("a", {"a": "yes"}) is True
    assert evaluate("a", {"a": "no"}) is False
    assert evaluate("a", {"a": "not_sure"}) is None
    assert evaluate("a", {}) is None


def test_all_any_not():
    assert evaluate({"all": ["a", "b"]}, {"a": "yes", "b": "yes"}) is True
    assert evaluate({"all": ["a", "b"]}, {"a": "no"}) is False          # one "no" rules it out
    assert evaluate({"all": ["a", "b"]}, {"a": "yes"}) is None          # still need b
    assert evaluate({"any": ["a", "b"]}, {"a": "yes"}) is True          # one "yes" is enough
    assert evaluate({"any": ["a", "b"]}, {"a": "no"}) is None           # still need b
    assert evaluate({"any": ["a", "b"]}, {"a": "no", "b": "no"}) is False
    assert evaluate({"not": "a"}, {"a": "no"}) is True
    assert evaluate({"not": "a"}, {"a": "not_sure"}) is None


def test_open_findings_only_lists_what_could_still_matter():
    assert open_findings({"all": ["a", "b"]}, {}) == ["a", "b"]
    assert open_findings({"all": ["a", "b"]}, {"a": "no"}) == []        # already ruled out
    assert open_findings({"any": ["a", "b"]}, {"a": "yes"}) == []       # already met
    assert open_findings({"all": ["a", "b"]}, {"a": "not_sure"}) == ["b"]  # cannot re-ask a
    assert open_findings("a", {"a": "not_sure"}) == []
