"""Evaluation harness: test cases (vignettes), a simulated patient, scoring and reports.

The harness tests the engine. It contains no clinical content of its own.

IMPORTANT, to avoid circular testing:
  - Vignettes are written by a separate session that sees only the source
    pages, the vignette format and the list of questions. It never sees the
    knowledge base rules or outcomes.
  - The session that writes the knowledge base does not read the vignette
    files. It only sees what the harness reports.
"""
