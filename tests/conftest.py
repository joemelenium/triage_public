"""Shared set-up for the tests."""

import sys
from pathlib import Path

import pytest

# Let the tests import the engine without installing anything.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from engine.kb import load_knowledge_base  # noqa: E402
from engine.runner import load_case  # noqa: E402

EXAMPLES = sorted((REPO_ROOT / "examples").glob("*.yaml"))


@pytest.fixture(scope="session")
def kb():
    return load_knowledge_base()


@pytest.fixture(scope="session", params=["single_cause", "noisy_or"])
def any_method_kb(request):
    """The knowledge base with each inference method in turn, for tests that must hold for both."""
    kb = load_knowledge_base()
    kb.settings.inference_method = request.param
    return kb


@pytest.fixture(scope="session")
def rules_only_kb():
    """The same knowledge base with likely conditions switched off, so only sourced rules decide."""
    kb = load_knowledge_base()
    kb.settings.outcome_method = "rules_only"
    return kb


@pytest.fixture
def example():
    """Load an example case by name, for example example('sore_throat_self_care')."""
    return lambda name: load_case(REPO_ROOT / "examples" / f"{name}.yaml")
