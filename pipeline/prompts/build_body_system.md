# Instructions: building one body system

You are building one body system of a mock triage engine modelled on
commercial condition-based engines. It is a demonstration and proof of
concept for testing an evaluation. It will NEVER be used clinically. The aim
is a capable, realistic engine: use your full clinical knowledge as well as
the NHS source pages.

You are working in your own copy of the repository. Other agents are building
other body systems at the same time in their own copies. Your work will be
merged with theirs, so keep to your own files as described below.

## Read first

1. `pipeline/prompts/draft_conditions.md`: the general drafting instructions.
   Follow them, including the "Do not" list, except that you DO commit at the
   end (see "Finish").
2. `README.md`, `knowledge_base/settings.yaml`, `knowledge_base/conditions/README.md`,
   and `DECISIONS.md` items 100 onwards.
3. The chest and breathing pilot, which is the model to copy: all of
   `knowledge_base/observations/`, `knowledge_base/entry_symptoms/`,
   `knowledge_base/conditions/chest_and_heart/` and `.../breathing/`, and
   `knowledge_base/advice/`.
4. Your batch in `pipeline/batches.yaml`.

## What to build

1. **Sources.** The NHS Symptoms A to Z pages are already saved in
   `sources/nhs_uk/`. Fetch the NHS condition pages you need:
   `python3 triage.py fetch-source --log <your body system> ID URL "Title"`
   (it pauses between pages). Some pages do not exist: use clinical
   knowledge for those and mark the item `ai_judgement`.

2. **Observations** in `knowledge_base/observations/<your body system>.yaml`.
   Reuse observations from other files wherever they fit (never duplicate a
   concept). Add what you need, with parents and relations (duration,
   severity, character, location, radiation, what makes it worse or better),
   short `checklist_text`, `seriousness` for alarming signs, `question_carer`
   where a parent may answer for a child, `sex` and `asked_only_if` where
   they apply. If you truly need a new observation that belongs to another
   body system or to `general.yaml`, put it in YOUR file anyway and say so in
   your report: the merge will move it.

3. **Entry symptom files**, one per entry symptom in your batch, in
   `knowledge_base/entry_symptoms/`. For each: the red flags and urgent rules
   (NHS page plus clinical knowledge, including the must-not-miss causes), an
   emergency-level checklist and an urgent-level checklist of the most
   important 6 to 10 items, other outcome rules, a default outcome (with
   `floor: true` where everyone with the symptom should get at least that
   care), `soft: true` on rules where sources disagree or that rest on a
   reading of the source, and `also_covers: [source ids]` listing any other
   Symptoms A to Z pages this entry symptom covers (for example foot pain
   covering heel pain). Every Symptoms A to Z page in your batch must be
   covered.

4. **Condition cards** in `knowledge_base/conditions/<your body system>/`, one
   file each. Include the conditions in your batch list, any others a triage
   service commonly sees for your entry symptoms, and every life-threatening
   cause that must not be missed. Existing cards in other body systems can be
   reused: add your entry symptoms to their `entry_symptoms` list. Each card:
   at least 4, ideally 5 to 8, linked observations including at least two
   that tell it apart from look-alikes; realistic `prevalence` among people
   with each entry symptom; `danger` and `acuity_needed`; risk factors in
   `prevalence_when` rather than `findings`; `diagnosed_by` where there is a
   question for already having it.

5. **Advice** in `knowledge_base/advice/<your body system>.yaml` for every
   outcome you use: what to do, what to look out for, when to get more help,
   where to go.

6. **SNOMED CT:** `python3 triage.py snomed-search "term"`, then
   `python3 triage.py snomed-add --log <your body system> CODE`. Pause between
   lookups; the browser sometimes errors, so retry once, then leave it out.

## Rules to remember

- Levels of care are in `settings.yaml`. There is a `dental` level for tooth
  and gum problems. There is no mental health crisis level: use the emergency
  department or urgent care, with advice naming crisis lines.
- Plain language is enforced when the network loads
  (`knowledge_base/plain_language.yaml`). Add words to its `explain` list if
  your body system needs them, with plain explanations.
- An entry symptom's own main symptom is not evidence within it, so set
  `prevalence` as the realistic share of people with that symptom. A card with
  several entry symptoms can set a different starting chance for each with
  `prevalence_when` on the entry symptom's main observation (first match wins,
  so put age bands that should override it first).
- Starting chance bands: very_common, common, uncommon, rare, very_rare. Use
  `very_rare` for serious diseases that are only plausible with a telling sign,
  and raise them with `prevalence_when` on that sign (for example a cough for 3
  weeks or more). This keeps them from driving questions in ordinary cases.
- Group an entry symptom's "see a GP" signs into one checklist: a screen with
  `level: routine` (asked after the red flags, only when it could still raise
  the outcome). Keep each checklist to 4 to 8 items.
- Never copy NICE, CKS or BNF text. Never use real patient data.
- Never read `vignettes/` or `reports/`.

## Check

- `python3 triage.py check` must load with no problems. Look at its warnings
  and wire in observations you added but did not use.
- `python3 triage.py selftest`: every condition you added should pass.
- `python3 triage.py coverage`: every page in your batch should be covered.
- `python3 -m pytest -q` must pass. Do not change engine code or tests. If a
  test fails because of content, fix the content, or describe the failure in
  your report.

## Finish

Commit your work in your copy of the repository with a clear message (for
example "Build <body system>: N entry symptoms, M conditions"). Then report,
in under 600 words: entry symptoms built and the Symptoms A to Z pages each
covers; conditions added (name, danger, acuity, one line each, grouped);
observations you put in your file that belong elsewhere; anything you were
unsure of; and the final `check`, `selftest`, `coverage` and test result lines.
