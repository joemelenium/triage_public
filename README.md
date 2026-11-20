# Adaptive triage exemplar

**Not for clinical use. Not medical advice.** This is a personal, standalone
demonstration project for testing how triage engines can be evaluated. It is
not an NHS product, is not affiliated with or endorsed by the NHS or any
organisation, and has no links to NHS systems. All clinical content, advice
and test cases are AI-drafted and fictional, and have **not** been clinically
reviewed. Do not use it to make decisions about anyone's health. For a real
concern, call 999 in an emergency or use 111 (in the UK).

## What this is

A small triage engine built to be a comparator in triage evaluations. It asks
a patient questions, works out how urgent the need is, recommends a level of
care and a timeframe, and gives safety-netting advice.

How it decides:

- **It is a mock-up of a condition-based triage engine**, built to see how
  that kind of engine performs in an evaluation. It is never for clinical use.
- **Firm rules set a floor.** Red flags and other sourced rules come from a
  published page ("chest pain that spreads to the arm: call 999"). The outcome
  never goes below a firm rule that applies.
- **Likely conditions decide the level above that floor.** The engine estimates
  how likely each possible condition is. A few rules are marked "soft", and
  those and the default outcome can be raised or lowered by the conditions.
- **Risk balance through danger classes.** Each possible condition is critical,
  serious, moderate or minor, by how bad a miss would be. A small chance of a
  critical condition is acted on; a minor one must be likely before it counts.
  An outcome is only lowered when something the patient said points to a
  milder cause, and never below a floor the source sets.
- **The likelihoods come from a Bayesian network** (noisy-OR): several
  conditions can be present at once, and evidence for one can explain away a
  symptom that points to another. A simpler single-cause method is available
  as a setting for comparison.
- **The likelihoods are AI best-judgement estimates**, labelled as such.
- **A "rules only" setting** in `knowledge_base/settings.yaml` switches the
  conditions off, so the two methods can be compared.
- **"Not sure" is never treated as "no".** If a rule cannot be ruled out, the
  engine chooses the more urgent outcome and says so.
- **No LLM is involved.** The engine makes no network calls and gives the same
  result every time for the same answers.
- **Plain language is checked.** Patient text must follow the NHS "A to Z of
  NHS health writing" (for example "high temperature", not "fever"), and any
  medical word with no everyday alternative must be explained where it
  appears. The rules are in `knowledge_base/plain_language.yaml`, and the
  engine refuses to load content that breaks them.
- **Coded output.** Findings and possible conditions carry a SNOMED CT code
  where one has been checked. Possible conditions are ranked, but they are
  reasoning aids, not a diagnosis.

It covers all 129 pages of the NHS website's Symptoms A to Z, as 140 main
symptoms and 508 possible conditions. Anything else gets a cautious "not
covered" outcome after an emergency red-flag check.

The original project brief is not published. Choices made along the way are
in [DECISIONS.md](DECISIONS.md), where "the brief" and "the owner" refer to
that brief and the project's owner.

## Set-up (once)

You need Python 3.11 or later. Then, from this folder:

```bash
pip install -r requirements.txt
```

## Run one case

```bash
python triage.py run examples/chest_pain_emergency.yaml
```

This prints the outcome, why it was reached, the red flags found, the advice,
and every question with the reason it was asked. Add `--json` to see the full
record. Other examples are in the `examples/` folder.

## Answer the questions yourself

```bash
python triage.py ask
```

## Check the knowledge base

```bash
python triage.py check
```

This loads every clinical file and stops with a clear message if anything has
no source, refers to something that does not exist, or uses a value that is
not in the settings file.

## Run the tests

```bash
python -m pytest
```

The tests prove, among other things, that the same case always gives the same
record, that the most urgent outcome stops the questions at once, that "not
sure" raises the outcome, and that patient context is never asked for again.

Some tests make up hundreds of random patients. By default they run a quarter
of their full count, so the whole suite takes about an hour on a small
machine (4 cores), most of it in `test_design_properties.py`. Running each
test file in its own process is faster. For a thorough run on a bigger
server:

```bash
TRIAGE_TEST_SCALE=100 python -m pytest
```

Speed is never a reason to simplify the engine's reasoning (DECISIONS 145):
if it is slow, it can run on a bigger machine.

## Run the evaluation

```bash
python triage.py evaluate
```

This runs every development test case through the engine and writes a
one-page report to `reports/dev_report.md`. The report gives the two safety
gates first (red flags, and never below the minimum safe urgency), then the
scores, the comparison with a fixed-order baseline, a "not sure" stress test,
and every failure case by case.

Two other sets can be run:

```bash
python triage.py evaluate holdout
```

```bash
python triage.py evaluate external
```

The holdout set is run only at the end of a wave, and the content is never
tuned against it. The external set is the published vignettes, as an outside
sense check.

Every case where the engine and a test case differ is logged, with both
sources, in `review/disagreements.md` for clinical review. Neither side is
changed to force agreement.

**Read the results with care.** The test cases are AI-drafted and not
clinically approved. They were written by a separate session that saw only
the source pages, the format and the list of questions, never the engine's
rules. That reduces the risk of the engine being tested against itself. It
does not remove it.

## Run the risk setting sweep

```bash
python triage.py sweep
```

This reruns the development cases with conditions switched off and at four
levels of caution, and shows how over-triage, question count and the spread of
outcomes move. The report is `reports/sweep_report.md`.

## Report coverage

```bash
python triage.py coverage
```

This reports how many pages on the NHS website Symptoms A to Z are handled by
a module, and how many are returned as "not covered".

## Produce the review packs

```bash
python triage.py review-pack
```

This writes one readable document per presenting symptom to `review/`, for a
clinician: the red flags, rules, questions as worded, advice, sources, and
everything marked as AI judgement.

## Start the demo and the API

```bash
python triage.py serve
```

Then open http://127.0.0.1:8000 in a browser for the demo page: give an age,
sex and main symptom, answer the questions, and see the result with its
advice, the reasons for it and the possible causes. It runs on your computer
only; nothing anyone enters is stored or sent anywhere.

The same server gives an API in the common shape of condition-based triage
engine APIs, so an evaluation designed for such an engine can call this mock
with little change. Interactive documentation is at http://127.0.0.1:8000/docs.

| Call | What it does |
| --- | --- |
| `POST /diagnosis` | The next question and the likely conditions so far. `should_stop` is true when the interview is over. |
| `POST /triage` | The triage level (`emergency_ambulance`, `emergency`, `consultation_24`, `consultation`, `self_care`), with the outcome, advice and reasons in `extras`. |
| `GET /search?phrase=` | Find a main symptom by name or everyday words. |
| `GET /symptoms`, `GET /conditions` | Everything that can be evidence, and every condition. |
| `GET /info` | Versions and counts. |

Both POST calls take the same body. Like those APIs, it keeps nothing
between calls: send all the evidence each time.

```json
{"sex": "female", "age": {"value": 30},
 "evidence": [{"id": "sore_throat", "choice_id": "present", "source": "initial"},
              {"id": "very_high_temperature", "choice_id": "absent"}]}
```

`choice_id` is `present`, `absent` or `unknown`. Evidence marked `"source":
"initial"` is what the person said at the start (at least one main symptom),
and `"predefined"` is known history. Everything else answers the engine's
questions. Ids are this engine's own. The tests check that
answering through the API gives exactly the same outcome, after the same
questions, as answering the engine directly.

There is no language layer (reading the person's own words): the owner
decided to leave it out for now (DECISIONS 177).

## What is in each folder

| Folder | What it holds |
| --- | --- |
| `knowledge_base/` | All clinical content, as plain text (YAML) files a clinician can read and correct. |
| `engine/` | The triage logic. It contains no clinical content. |
| `api/` | The API and the demo page (`python triage.py serve`). |
| `harness/` | The evaluation: simulated patient, scoring, baseline and reports. |
| `vignettes/` | Test cases: `dev/`, `holdout/`, and `external/` for published sets. Written separately from the content. |
| `reports/` | The latest run report for each set. |
| `examples/` | Example cases for trying the engine. They are not evaluation cases. |
| `sources/` | The source log, and text snapshots of the pages the content was drafted from. |
| `tests/` | Automatic checks. |
| `review/` | A readable pack per symptom, points of judgement, and the disagreements log. |
| `docs/` | Background context for the project. |

Inside `knowledge_base/`:

| File | What it holds |
| --- | --- |
| `settings.yaml` | The scales, danger classes, question limit and probability bands. |
| `observations/` | Everything the engine can ask or know (symptoms, history, context), one file per body system. Observations can have a parent ("severe headache" under "headache"). |
| `conditions/` | One card per possible condition, in a folder per body system: how common it is, how dangerous, which observations go with it, and which entry symptoms make it a candidate. |
| `entry_symptoms/` | One file per main symptom: its sourced red flags, other rules, checklists and default outcome. |
| `red_flags.yaml` | Red flags checked in every session, whatever the symptom. |
| `advice/` | Safety-netting and self-care text for each outcome, one file per body system. |
| `plain_language.yaml` | Words to avoid and medical words that must be explained. |

Together the observations and condition cards form one network, like the
condition-based engines this is modelled on. A condition can belong to several
entry symptoms. See `docs/design_condition_network.md` for where this is going.

## How a session runs

1. Start with what is already known: the presenting symptom and any patient context.
2. Fill in what follows from what is known: a "yes" to an observation means
   "yes" to its parent, a "no" to a parent means "no" to everything under it,
   and observations for the other sex do not apply.
3. Ask one "do any of these apply?" question covering the emergency red flags
   for everyone, then one for each presenting symptom. If the outcome reaches
   the most urgent there is (an ambulance), stop at once. If it reaches "999 or
   A&E", ask only the emergency questions that could still make it an
   ambulance, then stop.
4. Check the remaining red flags, most serious first. All of them are checked,
   and they never count against the question limit.
5. Ask other questions one at a time: first those that could raise the outcome
   through a sourced rule, then those most likely to change how likely a
   dangerous condition is. A parent is always asked before its children.
6. Stop when no remaining question is likely to change the outcome, or at the
   question limit (20). Every question asked has a reason code and a reason in
   plain words.

The record also gives a five-level summary (ambulance, emergency department,
see a doctor within 24 hours, see a doctor, self-care) with a root cause, in
the shape condition-based engines use, for side-by-side comparison.

## How to add content

A main symptom:

1. Read the source pages and add each one to `sources/source_log.yaml`.
2. Add any new observations to the right file in `knowledge_base/observations/`.
3. Add any new advice to `knowledge_base/advice/<body system>.yaml`.
4. Copy `knowledge_base/entry_symptoms/sore_throat.yaml` and fill in the red
   flags, other rules, checklists and default outcome. Every item needs a source.

A condition:

1. Copy a card in `knowledge_base/conditions/` into the right body-system
   folder. The file name must be the condition's id.
2. List its `entry_symptoms`, how common it is, its danger class, and the
   observations that go with it.

Then run `python triage.py check`, then `python -m pytest`. New content should
also get an independent check against its sources and separately written test
cases.

After changing any question, run `python triage.py export-questions` so that
vignette authors see the current list.

## Where this has got to

Build order from the original project brief (not published):

1. Plan: done.
2. **Skeleton: done.** Engine, settings and chest pain and sore throat content,
   working from the command line, with a trace and a determinism test.
3. **Harness: done.** Test cases written separately, simulated patient,
   scoring, fixed-order baseline, run reports, published vignette sets, and
   the review packs.
Then a new plan, in `docs/design_condition_network.md`, to grow this into a
full condition network like the engines it is modelled on:

1. **Network engine: done.** One shared network of observations (with a
   hierarchy) and condition cards, moved across from the old per-symptom
   modules with behaviour unchanged.
2. **Tools for building content at scale: done.** Page snapshots, SNOMED CT
   checks, self-tests, coverage, and per-body-system files so systems can be
   built in parallel and merged (`pipeline/`).
3. **Pilot body system (chest and breathing): done**, then checked
   independently and fixed.
4. **All ten body systems: built and merged.** Now 508 conditions, 1,248
   observations, 1,572 rules, covering all 129 pages of the NHS website
   Symptoms A to Z. Each system was drafted by its own agent, then merged
   into one network with duplicates reconciled (DECISIONS 146 to 150).
5. **Independent test cases, fix-up rounds and one fresh holdout run: done.**
   394 cases (280 development, 114 holdout). Both safety gates pass on both
   sets. Fixes are in DECISIONS 151 to 172.
6. **Interfaces: done.** An API in the common shape and a local demo page
   (`python triage.py serve`). The language layer is left out for now.

## Latest results

Knowledge base 0.4.0: 508 conditions, 1,248 observations, 1,572 rules,
covering all 129 pages of the NHS website Symptoms A to Z. Condition-based
method with danger classes, noisy-OR network inference. Full reports are in
`reports/`.

| | Development (280 cases) | Holdout (114 cases, run once) |
| --- | --- | --- |
| Gate: red flags escalated | **Pass**, 216 of 216 | **Pass**, 83 of 83 |
| Gate: never below minimum safe urgency | **Pass**, 280 of 280 | **Pass**, 114 of 114 |
| Over-triage | 28 of 280 (10%) | 20 of 114 (18%) |
| For reference, "always 999" over-triage | 208 of 280 (74%) | 82 of 114 (72%) |
| Acuity matches expected | 247 of 280, 88% (95% range 84% to 92%) | 89 of 114, 78% (70% to 85%) |
| Less urgent than expected (but not below minimum safe) | 5 | 5 |
| Interactions per case (mean) | 9.4 | 8.9 |
| Items read per case: engine, ask-everything baseline | 28.7, 40.9 | 27.0, 38.0 |
| Condition self-tests (each card recognised in the top 3) | 1,284 of 1,286 | |

The gates alone can be passed by sending everyone to 999, so read them next
to over-triage. The holdout set was run once, at the end, after all the
fixes, and nothing was tuned against it. It scores lower on exact acuity
than the development set, which is expected: the development set was used to
find and fix problems. The two self-test near-misses are rare cancers that
rank 4th and 5th behind much more common harmless causes of the same signs,
which is realistic; their outcomes are still urgent enough.

These cases are AI-drafted and not clinically approved, so the results show
how the engine behaves. They are not evidence that it is clinically safe.
Many differences on exact acuity are differences of mapping (for example
"see a GP" as routine against "soon"), logged in `review/disagreements.md`.

Run times on a small machine (4 cores): development set about 7 minutes,
holdout about 2 minutes, full test
suite about an hour.

## Sources and licence

Clinical content is adapted from the NHS website (nhs.uk). It contains public
sector information licensed under the
[Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
The content has been adapted. It should not be attributed to the NHS website,
it does not imply endorsement, and it no longer carries the NHS website's
clinical approval. Every source is listed in `sources/source_log.yaml`.
