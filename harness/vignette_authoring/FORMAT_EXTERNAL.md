# How to convert a published vignette

Published vignette sets are an outside check on the engine. They were written
by other people for other purposes, so they are reported separately from the
project's own vignettes and treated as a sense check.

The same rules apply as in `FORMAT.md`: read only the source material you are
given and this folder, never the knowledge base or anything else in the
repository, and never run the triage engine.

## Before converting anything

1. Confirm the licence of the publication from the publication itself, and
   quote the licence statement.
2. Record it in `sources/external_vignette_sets.md`: the citation, the URL,
   the date accessed, the licence, the exact licence statement, and how the
   material is used here.
3. Only convert a set if its vignettes are actually published and the licence
   allows reuse. If not, record that and stop.

## The fields

One file per published vignette, in `vignettes/external/`.

```yaml
id: semigran2015_01           # unique. Also the file name.
set: "Semigran 2015"
status: "Published vignette, converted by AI, not clinically approved in this form"
citation: "Authors. Journal Year;Volume:Pages."
licence: "CC BY-NC 4.0"

# The published wording is NOT stored in the repository. Give the vignette's
# number in the publication in conversion_notes so the original can be looked up.
original_diagnosis: "The diagnosis given in the publication, if any."
original_triage_label: "The triage category exactly as the publication words it."
original_triage: emergency    # that category mapped to one of:
                              #   emergency       emergency care needed
                              #   non_emergency   needs to be seen, but not as an emergency
                              #   self_care       can be managed without seeing anyone

presenting_text: "The main complaint in plain words, for example 'abdominal pain'."
presenting: []                # question-list ids of any PRESENTING symptoms on the list.
                              # Leave as [] if the main complaint is not on the list.

age: 55                       # as published, if given
sex: male                     # female or male, if given

findings:                     # using ids from question_list.yaml
  present: []                 # anything in the published text that matches a question
  absent: []                  # anything the published text says is NOT present
  unknown: []

conversion_notes: "Anything a reviewer should know about how the text was mapped."
```

## How to map the text

- Use only what the published text says. Do not add findings because they
  would be typical of the diagnosis.
- A finding goes in `present` only if the text clearly states it. If the text
  clearly rules it out, it goes in `absent`. Otherwise leave it out.
- Include matching findings even when the main complaint is not on the
  question list. Some questions are asked of everyone, so they still matter.
- `presenting` should list only ids whose `kind` is `presenting` in the
  question list, and only when that symptom is the patient's main complaint or
  one of them.
