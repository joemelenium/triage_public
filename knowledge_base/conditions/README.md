# Condition cards

One file per possible condition, in a folder per body system.

NOT FOR CLINICAL USE. A demonstration and proof of concept only.

```
# Conditions: possible causes. They order the questions, and a serious one that
# is likely enough can raise the outcome (see outcome_method in settings.yaml).
# NOT FOR CLINICAL USE. AI-drafted, not clinically reviewed.
#
# EVERYTHING in this file is AI judgement and needs clinical review.
# The NHS website describes which symptoms go with which condition. It does not
# say how common conditions are or how strongly a symptom points to one. So the
# bands below are estimates, not sourced figures.
#
# This engine is a mock-up of a condition-based triage engine, so best-judgement
# estimates are used. It is never for clinical use. Conditions are never shown
# to a patient as a diagnosis.
#
# Fields:
#   prevalence       how common among people with the presenting symptom
#                    (very_common, common, uncommon, rare)
#   prevalence_when  a different band when a finding is present (for example age)
#   findings         how strongly a "yes" to each finding points to this cause
#                    (strongly_supports, supports, argues_against, strongly_argues_against)
#   acuity_needed    the level of care this condition would need
#   danger           how bad it would be to miss it: critical, serious, moderate or minor
#                    (the lines for each class are in settings.yaml)
#   diagnosed_by     a finding meaning the patient already has this diagnosis. A known,
#                    managed condition does not on its own raise the outcome.
#   informed_by      pages that describe the condition's symptoms
```

New fields:

- `body_system`: the folder it is in.
- `entry_symptoms`: the main symptoms that make this condition a candidate.
- `key_findings`: optional. Observations to ask about if this condition becomes probable.
