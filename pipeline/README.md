# Content pipeline

How condition content is built at scale, one body system at a time. A
demonstration and proof of concept only, never for clinical use.

The design is in `docs/design_condition_network.md`. This folder holds the
tools and the instructions given to the AI agents that do each step.

## Steps for each body system

| # | Step | Who | Tool or instructions |
| --- | --- | --- | --- |
| 1 | Choose the conditions and entry symptoms for the batch | Lead session | NHS Health A to Z and Symptoms A to Z |
| 2 | Fetch and save the source pages, a few at a time | Lead session | `python triage.py fetch-source ID URL "Title"` |
| 3 | Draft condition cards, observations, entry-symptom rules and advice | Drafting agents, in parallel, a few conditions each | `prompts/draft_conditions.md` |
| 4 | Check and log SNOMED CT codes | Drafting agents | `python triage.py snomed-search "term"`, `snomed-add CODE` |
| 5 | Validate the network | Lead session | `python triage.py check` (must load with no problems) |
| 6 | Independent check against the sources and clinical knowledge | A separate checking agent | `prompts/check_conditions.md` |
| 7 | Self-tests: each condition recognisable from its own card | Lead session | `python triage.py selftest` |
| 8 | Independent test cases | Separate case-writing agents that never see the network | `harness/vignette_authoring/FORMAT.md` |
| 9 | Evaluate, and fix what the sources or clinical knowledge clearly support | Lead session | `python triage.py evaluate` |
| 10 | Regenerate the review packs as documentation | Lead session | `python triage.py review-pack` |

## Rules that apply to every step

- **Sources:** NHS pages are the source for red flags and outcomes where they
  cover them. Published research and public statistics may be cited. The AI's
  own clinical knowledge may be used and is labelled `ai_judgement`. Licensed
  content (NICE, CKS, BNF) is never copied.
- **No real patient data**, anywhere.
- **Plain language:** the engine refuses to load text that breaks the rules in
  `knowledge_base/plain_language.yaml`.
- **Separation:** agents that write test cases never read `knowledge_base/`.
  The lead session never reads the test cases.
