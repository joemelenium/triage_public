# How to write a vignette

A vignette is one made-up patient, used to test a triage engine. Synthetic
only. Never base one on a real person.

## Rules for the author

These rules exist so that the test cases are independent of the thing being
tested. Please follow them exactly.

1. **You may read only two places:** the source page snapshots in
   `sources/nhs_uk/*.txt`, and this folder (`harness/vignette_authoring/`).
2. **Do not read anything else in the repository.** In particular not
   `knowledge_base/`, `engine/`, `examples/`, `review/`, `reports/`, `tests/`,
   `DECISIONS.md`, `README.md`, `sources/source_log.yaml`, or vignette files
   written by anyone else.
3. **Do not run the triage engine** (`triage.py`) on anything. You may run the
   format checker: `python3 -m harness.validate dev holdout`.
4. **Take every expected outcome from the source pages**, not from what you
   think a triage tool would do. Quote the words that support it.
5. **Do not invent** statistics, quotes or clinical facts that are not in the
   source pages.

## What you are given

- `sources/nhs_uk/*.txt`: the source pages. Treat these as the only authority.
- `question_list.yaml`: every question the engine is able to ask, each with an
  id. You describe your patient using these ids. The list does not tell you
  what the engine does with the answers.
- `scales.yaml`: the allowed values for acuity, level of care and timeframe.

## How the patient is simulated

A script plays the patient. When the engine asks a question:

- it answers **yes** to anything in `findings.present`
- it answers **no** to anything in `findings.absent`
- it answers **not sure** to anything in `findings.unknown`
- it answers **no** to anything you did not mention at all

So you must state the **relevant negatives**: the findings that matter for
this case and are absent. A separate stress test answers "not sure" to
everything you did not mention, so a case with too few stated negatives will
look much worse there.

Age-based questions (such as "under 5 years old") are answered from the
patient's age, so you do not list those.

Some questions are a more specific version of another (`part_of` in the
question list): for example a barking cough is part of "cough". If you list a
specific one as present, the general one counts as present too. Never list a
specific one as present and its general one as absent.

## The fields

```yaml
id: cp_d01                    # unique. Also the file name: cp_d01.yaml
status: "AI-drafted, not clinically approved"     # exactly this text
authored_by: "AI, in a session separate from the knowledge base"

presenting: [chest_pain]      # the main symptom or symptoms, as question-list ids

summary: "One or two sentences describing the patient and the story."

opening_statement: "What the patient would first say, in their own words."

findings:
  present: [id_one, id_two]         # true of this patient
  absent: [id_three, id_four]       # relevant things that are NOT true
  unknown: []                       # things this patient genuinely could not say

context:                      # what is known about the patient before any question
  none: {}                    # nothing known
  basic: {age: 58, sex: male}
  full:                       # basic, plus anything from the patient's record
    age: 58
    sex: male
    findings: {some_history_id: "yes"}     # "yes" or "no", in quotes

expected:                     # the right outcome when everything above is known
  acuity: emergency
  level_of_care: emergency_ambulance
  timeframe: now

minimum_safe_acuity: emergency   # the LEAST urgent acuity that would still be safe

red_flags:                    # danger signs present in this case. Leave as [] if none.
  - description: "Plain words for the danger sign"
    findings: [id_one]        # the ids that make it up. Use [] if no question fits, and say so in notes.
    minimum_acuity: emergency # the least urgent acuity acceptable when this sign is present
    source: {page: chest_pain.txt, quote: "words copied exactly from the page"}

safety_netting_should_cover:  # what good advice for this patient must mention
  - point: "Call 999"
    any_of: ["999"]           # the advice passes this point if it contains any of these
  - point: "Not to drive themselves to hospital"
    any_of: ["do not drive", "don't drive"]

source:
  expected_outcome: {page: chest_pain.txt, quote: "words copied exactly from the page"}
  minimum_safe_acuity: {page: chest_pain.txt, quote: "words copied exactly from the page"}

variants:                     # optional: the same patient, said differently
  - id: cp_d01_v1
    style: "brief and anxious"
    opening_statement: "Different words for the same story."
    volunteered: [id_one]     # findings they mention up front, from present or absent
  - id: cp_d01_v2
    style: "long and rambling, mentions lots up front"
    opening_statement: "..."
    volunteered: [id_one, id_two, id_three]

context_test:                 # optional: only for cases built to test use of context
  what_context_adds: "What the record knows that the patient does not say"
  expected_direction: more_urgent    # effect of full context compared with none:
                                     # more_urgent, less_urgent or same

atypical: false               # true if this is an unusual way for the problem to present
notes: ""                     # anything a reviewer should know, including source differences
```

The ids above (`id_one` and so on) are placeholders. Use real ids from
`question_list.yaml`.

## Getting the outcome right

- **expected** is the outcome the source material supports for this patient.
  Pick the acuity, level of care and timeframe from `scales.yaml` that best
  match the source's own advice, and quote that advice.
- **minimum_safe_acuity** is the least urgent acuity that would still be
  acceptable. It can be the same as the expected acuity. It can never be more
  urgent than it.
- **If two source pages give different advice for the same situation**, use
  your judgement, and write both in `notes` with the page names.
- **Quotes must be copied exactly** from the page (a phrase or a sentence is
  enough, at least 15 characters). The checker confirms each quote appears on
  the page you name, and rejects the file if it does not.
- If a danger sign in the sources cannot be expressed with any question on the
  list, still include it in `red_flags` with `findings: []`, and explain in
  `notes`. That is useful: it shows where the question list is thin.

## Context tests

Most patients can answer questions about their own history, so context usually
changes nothing. A context test is a case where the **record knows something
the patient does not say**. Put the finding in `findings.unknown`, and give the
real answer in `context.full.findings`. Then say which way the outcome should
move when the full context is available.

## Variants

A variant is the same patient and the same facts, expressed differently:
different words, a different manner, or volunteering more or less at the
start. The expected outcome is unchanged. `volunteered` lists the findings
mentioned up front, each of which must be in `present` or `absent`.

## What makes a good set

- Cases at every acuity level the sources support, not just the dramatic ones.
- Red-flag cases, including ones where the danger sign is easy to miss.
- Atypical presentations.
- Mild, ordinary cases, where over-triage would be the mistake.
- Some cases with more than one finding present.
- A few cases where the patient is genuinely not sure of something.
- Plain, realistic opening statements in everyday language.

## Development and holdout sets

Decide which set each case belongs to **when you create it**, not afterwards.
About one case in three goes in the holdout set. Both sets should cover the
full range of acuity levels. Development cases go in `vignettes/dev/` and
holdout cases in `vignettes/holdout/`.
