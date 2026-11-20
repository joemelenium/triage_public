# Run report: development set

Run 2026-11-19. Engine 0.7.0, knowledge base 0.4.0 (AI-drafted, not clinically reviewed), commit d58a2bb, method: rules_and_conditions. 280 cases. Structured mode, no LLM.

> **Read this first.** These test cases are AI-drafted and not clinically approved.
> They were written in a separate session that saw only the source pages, the
> vignette format and the list of questions. It did not see the engine's rules
> or outcomes. That reduces the risk of the engine being tested against itself.
> It does not remove it: the content and the cases were both drafted by AI from
> the same pages. Treat these results as a check on how the engine behaves, not
> as evidence that it is clinically safe. Not for clinical use.

## Gates, read with over-triage

A failure on either gate is not offset by a good score elsewhere. But the gates alone can be passed by sending everyone to 999, so they are always shown next to over-triage, and next to what two useless engines would score.

| | Red flags escalated | Not below minimum safe | Both gates, by case | Over-triage |
| --- | --- | --- | --- | --- |
| **This engine** | **PASS** 216 of 216 (100%) | **PASS** 280 of 280 (100%) | 280 of 280 | 28 of 280 (10%) |
| Always 999, asks nothing | | | 280 of 280 | 208 of 280 (74%) |
| Always self-care, asks nothing | | | 51 of 280 | 0 of 280 (0%) |

With this few cases the true rates could differ: red flags escalated 95% range 98% to 100%; not below minimum safe 95% range 99% to 100%.

**Red-flag recognition** (a score, not a gate): did the engine find and name each red flag, as well as escalate? found but not named as a red flag: 13; missed: 12; not asked: already at an outcome this urgent: 44; recognised: 147.

**Ambulance cases not given an ambulance** (a score, not a gate, because many sources say "999 or A&E" together): cg_d03, cg_d07, cg_d16, gn_d02, gn_d03, gn_d04, hb_d03, hb_d08, mh_d02, mh_d03, sb_d01, sk_d01, sob_d04, sob_d05, sob_d06, sob_d07, sob_d16, wh_d01, wz_d12.

## Scores

| Measure | Result |
| --- | --- |
| Acuity matches expected | 247 of 280 (88%), 95% range 84% to 92% |
| Level of care matches expected | 205 of 280 (73%) |
| Timeframe matches expected | 247 of 280 (88%) |
| All three match | 196 of 280 (70%) |
| Over-triage (more urgent than expected) | 28 of 280 (10%): 22 by 1 level, 4 by 2 levels, 2 by 3 levels |
| Less urgent than expected | 5 cases, of which 5 still at or above minimum safe |
| Items read per case (each checklist line counts) | mean 28.7 |
| Words read per case | mean 315, most 947 |
| Interactions per case (a checklist counts as one) | mean 9.4, median 8.0, most 43 |
| Interactions before the first red flag was found | mean 2.4 |
| Safety-netting: all three parts present | 280 of 280 (100%) |
| Safety-netting: points the vignette asked for | 603 of 649 (93%) (a word check only, needs human judgement) |
| Safety-netting: same word check if every case got one fixed advice text | 506 of 649 (78%) (best single text: advice_dizziness_gp). The gap to the line above is what tailoring adds. |
| Advice length | median 129.0 words |
| Consistency: identical record on repeat | 280 of 280 (100%) |
| Consistency: same patient, volunteering more or less up front, gives the same outcome | 177 of 183 (97%). Reworded wording is not tested: that needs the language layer. |
| Context tests: context led to an outcome at least as close to expected, and safe | 22 of 22 (100%), of which closer: 3 |
| Coverage: handled by a module | 280 of 280 (100%) |
| Outcome driven by caution (missing information) | 5 cases |

## Outcome profile

Over-triage has a cost at scale, so the spread of outcomes matters as well as the gates.

| Level of care | Engine | Expected |
| --- | --- | --- |
| emergency ambulance | 35 | 49 |
| emergency department | 50 | 23 |
| urgent care | 73 | 44 |
| general practice | 75 | 111 |
| dental | 1 | 1 |
| community pharmacy | 7 | 13 |
| self care | 39 | 39 |

| Acuity | Engine | Expected |
| --- | --- | --- |
| emergency | 85 | 72 |
| urgent | 74 | 80 |
| soon | 10 | 12 |
| routine | 72 | 72 |
| self manageable | 39 | 44 |

## Comparators

**Fixed-order baseline.** A stand-in, not any real triage system. It uses the same rules but asks every question one at a time in file order.

- Same outcome as the engine: 195 of 280 (70%)
- Items read per case: engine 28.7, baseline 40.9
- Words read per case: engine 315, baseline 622
- Interactions per case (a checklist counts as one, so this flatters the engine): engine 9.4, baseline 40.9
- Different outcome in bj_d06: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d07: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d08: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d09: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d12: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d13: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bj_d14: engine self_manageable / self_care / not_needed, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in bn_d05: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in bn_d14: engine self_manageable / self_care / not_needed, baseline routine / general_practice / no_fixed_time. The engine stopped before a question that would have changed it.
- Different outcome in cg_d01: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d02: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d04: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d05: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d06: engine soon / general_practice / few_days, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d08: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d09: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d10: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d12: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d13: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d14: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_d15: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cp_h11: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in en_d05: engine urgent / dental / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in en_d14: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in ey_d04: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in ey_d07: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in ey_d13: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d02: engine emergency / emergency_department / now, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d04: engine emergency / emergency_department / now, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d05: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d06: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d11: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d12: engine routine / general_practice / no_fixed_time, baseline self_manageable / self_care / not_needed. The engine stopped before a question that would have changed it.
- Different outcome in gn_d13: engine self_manageable / self_care / not_needed, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in gn_d14: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in hb_d01: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in hb_d02: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in hb_d06: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in hb_d07: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_d04: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_d08: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_d13: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_d14: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_d01: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_d04: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_d07: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_d08: engine routine / general_practice / no_fixed_time, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in mix_d09: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_d10: engine soon / general_practice / few_days, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in pal_d07: engine routine / general_practice / no_fixed_time, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in pal_d09: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d04: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d06: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d07: engine emergency / emergency_department / now, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in sb_d08: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d09: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d11: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d12: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_d13: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sk_d08: engine soon / community_pharmacy / few_days, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d02: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d03: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d08: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d10: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d12: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d14: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_d15: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d08: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d18: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d19: engine routine / community_pharmacy / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d20: engine routine / community_pharmacy / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d21: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d23: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_d24: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in um_d06: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in um_d09: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wh_d05: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wh_d08: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wh_d11: engine routine / general_practice / no_fixed_time, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in wz_d01: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_d02: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_d03: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_d07: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_d08: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_d11: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.

**LLM-only baseline.** Not built. No LLM provider has been agreed.

**Risk setting sweep.** See `reports/sweep_report.md`, written by `python triage.py sweep`.

## Patient context

- Interactions per case with no context: 11.0, basic: 9.5, full: 9.4
- Cases where full context changed the acuity compared with none: 12
  - bn_d14: with no context routine, with full context self_manageable, not a context test
  - cg_d13: with no context soon, with full context routine, not a context test
  - cp_d02: with no context soon, with full context routine, not a context test
  - cp_d06: with no context urgent (chosen out of caution, because information was missing), with full context self_manageable, expected less urgent (as expected)
  - cp_d07: with no context urgent, with full context routine, not a context test
  - cp_d14: with no context urgent, with full context routine, not a context test
  - cp_h10: with no context urgent, with full context routine, not a context test
  - gn_d11: with no context self_manageable, with full context routine, expected more urgent (as expected)
  - mh_d14: with no context routine, with full context self_manageable, not a context test
  - sk_d14: with no context urgent (chosen out of caution, because information was missing), with full context self_manageable, expected less urgent (as expected)
  - sob_d02: with no context routine, with full context urgent, not a context test
  - sob_d15: with no context urgent, with full context routine, not a context test
  - bj_d13: with no context routine (chosen out of caution, because information was missing), with full context routine, expected more urgent (as expected)
  - bn_d06: with no context emergency (chosen out of caution, because information was missing), with full context emergency, expected more urgent (as expected)
  - cg_d14: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)
  - cp_d15: with no context emergency (chosen out of caution, because information was missing), with full context emergency, expected more urgent (as expected)
  - cp_h14: with no context emergency (chosen out of caution, because information was missing), with full context emergency, expected more urgent (as expected)
  - cp_h16: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected same (as expected)
  - hb_d05: with no context emergency, with full context emergency, expected same (as expected)
  - mh_d05: with no context urgent, with full context urgent, expected same (as expected)
  - pal_d05: with no context routine (chosen out of caution, because information was missing), with full context routine, expected more urgent (as expected)
  - pal_d11: with no context routine (chosen out of caution, because information was missing), with full context routine, expected more urgent (as expected)
  - sob_d08: with no context urgent, with full context urgent, expected more urgent (as expected)
  - sob_d12: with no context urgent, with full context urgent, expected same (as expected)
  - st_d06: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)
  - st_d07: with no context emergency, with full context emergency, expected same (as expected)
  - st_h11: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)
  - um_d08: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)
  - wh_d09: with no context soon, with full context soon, expected same (as expected)
  - wz_d05: with no context urgent, with full context urgent, expected more urgent (as expected)
  - wz_d07: with no context routine, with full context routine, expected more urgent (as expected)

## "Not sure" stress test

Reported separately. Here the simulated patient answers "not sure" to anything the vignette does not mention, where the main run answers "no". It shows how much the outcomes rest on unstated negatives.

- No outcome below minimum safe urgency: 280 of 280 (100%)
- Red flags gate passed: 280 of 280 (100%) cases
- More urgent than expected: 199 of 280 (71%)
- Outcome driven by caution: 252 of 280 (90%)
- Emergency outcomes: 265 of 280 (95%)
- Interactions per case: 1.7

## Failures, case by case

| Case | What | Expected | Engine gave | Decided by |
| --- | --- | --- | --- | --- |
| bj_d08 | level of care differs<br>advice does not mention: Get help immediately if a new headache, scalp tenderness, jaw pain when eating, or sight problems start | urgent / general_practice / today | urgent / urgent_care / today | rf_shoulder_severe (Shoulder pain) |
| bj_d09 | over-triage by 1 level | soon / general_practice / few_days | urgent / urgent_care / today | rf_foot_severe_or_faint (Ankle pain) |
| bj_d14 | advice does not mention: Painkillers and heat or cold packs, keep the neck moving | self_manageable / self_care / not_needed | self_manageable / self_care / not_needed | neck_pain_default (Neck pain) |
| bn_d04 | advice does not mention: Stay with her and reassure her | emergency / emergency_department / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| bn_d06 | over-triage by 1 level<br>advice does not mention: Contact NHS 111 now | urgent / urgent_care / today | emergency / emergency_department / now | rf_hi_blood_thinners_ae (AI judgement, needs clinical review) |
| bn_d08 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | fainting_default (Fainting) |
| bn_d11 | advice does not mention: Not to drive when feeling sleepy | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_in_months (Insomnia) |
| cg_d03 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sob_child_struggling (Shortness of breath) |
| cg_d04 | red flag "Persistent cough with weight loss and a hoarse voice in a smoker" escalated but missed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_cough_symptoms_worse (Chest infection) |
| cg_d06 | red flag "Asthma attack in the last day, now recovered" escalated but found but not named as a red flag | soon / general_practice / few_days | soon / general_practice / few_days | or_cough_asthma_attack_recovered (Asthma) |
| cg_d07 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| cg_d11 | advice does not mention: Keep using the reliever inhaler while waiting, up to the maximum dose; Sit up straight and try to stay calm | emergency / emergency_ambulance / now | emergency / emergency_ambulance / now | rf_severe_breathing_difficulty (Heart attack) |
| cg_d13 | red flag "Long cough with night sweats and weight loss, and TB risk" escalated but missed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_cough_symptoms_worse (Chest infection) |
| cg_d15 | level of care differs | self_manageable / community_pharmacy / not_needed | self_manageable / self_care / not_needed | cough_default (Cough) |
| cg_d16 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_cough_blotchy_skin (Sepsis) |
| cp_d09 | over-triage by 1 level<br>advice does not mention: Get help from NHS 111 today | urgent / urgent_care / today | emergency / emergency_ambulance / now | rf_cp_spreads (Angina) |
| cp_d11 | over-triage by 3 levels<br>advice does not mention: See a GP | routine / general_practice / no_fixed_time | emergency / emergency_department / now | rf_cp_present_now (Pulmonary embolism) |
| cp_d14 | advice does not mention: A pharmacist can help with the sore throat | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | chest_pain_default (Chest pain) |
| cp_d16 | over-triage by 1 level<br>advice does not mention: Ask for an urgent GP appointment or get help from NHS 111 | urgent / general_practice / today | emergency / emergency_department / now | rf_hb_with_breathing_heart_or_pain (Coughing up blood) |
| cp_d18 | over-triage by 2 levels<br>advice does not mention: See a GP | routine / general_practice / no_fixed_time | urgent / urgent_care / today | rf_cp_comes_and_goes (Angina) |
| cp_d19 | over-triage by 1 level | routine / general_practice / no_fixed_time | soon / general_practice / few_days | likely_condition_soon (AI judgement, needs clinical review) |
| cp_d20 | over-triage by 2 levels | routine / general_practice / no_fixed_time | urgent / urgent_care / today | rf_cp_worse_breathing_in (Pulmonary embolism) |
| cp_h11 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_st_high_temperature (Sore throat) |
| cp_h16 | over-triage by 2 levels | routine / general_practice / no_fixed_time | urgent / urgent_care / today | likely_condition_urgent (AI judgement, needs clinical review) |
| en_d03 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_ea_discharge (Earache) |
| en_d04 | red flag "Swallowing getting harder over weeks with weight loss" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | swallowing_problems_default (Dysphagia (swallowing problems)) |
| en_d06 | less urgent than expected by 1 level | soon / community_pharmacy / few_days | routine / community_pharmacy / no_fixed_time | or_bn_sinusitis_pharmacy (Sinusitis) |
| en_d09 | red flag "Red or white patch in the mouth for more than 3 weeks (possible mouth cancer)" escalated but missed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_to_white_patches (Sore or white tongue) |
| en_d13 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_tn_pulsing (Tinnitus) |
| ey_d08 | less urgent than expected by 1 level<br>advice does not mention: Clean the eyelids with cooled boiled water and cotton wool | soon / general_practice / few_days | routine / general_practice / no_fixed_time | or_re_child_under_2 (Red eye) |
| ey_d10 | over-triage by 1 level | routine / general_practice / no_fixed_time | soon / general_practice / few_days | bulging_eyes_default (Bulging eyes (exophthalmos)) |
| ey_d13 | level of care differs | self_manageable / community_pharmacy / not_needed | self_manageable / self_care / not_needed | dry_eyes_default (Dry eyes) |
| ey_d14 | over-triage by 1 level<br>advice does not mention: See a GP if not cleared up within 7 days | self_manageable / community_pharmacy / not_needed | routine / general_practice / no_fixed_time | or_re_sticky (Red eye) |
| gn_d01 | advice does not mention: Keep checking the child while waiting for help | emergency / emergency_ambulance / now | emergency / emergency_ambulance / now | rf_ht_child_meningitis_signs (Fever in children) |
| gn_d02 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| gn_d03 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_bb_floppy_or_not_responding (Is your baby or toddler seriously ill?) |
| gn_d04 | level of care differs<br>advice does not mention: Do not give paracetamol to a baby under 2 months without advice | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_ht_baby_high_temperature (Sepsis) |
| gn_d05 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_ht_not_getting_better (Fever in adults) |
| gn_d06 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_dh_dizzy_standing (Dehydration) |
| gn_d07 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | swollen_arms_default (Swollen arms and hands (oedema)) |
| gn_d08 | red flag "Thirst, peeing more, tiredness and weight loss (possible type 1 diabetes)" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_th_type_1_diabetes (Type 1 diabetes: symptoms) |
| gn_d09 | red flag "Unintentional weight loss with night sweats" escalated but found but not named as a red flag | soon / general_practice / few_days | soon / general_practice / few_days | or_ns_with_weight_loss (Unintentional weight loss) |
| gn_d12 | over-triage by 1 level | self_manageable / self_care / not_needed | routine / general_practice / no_fixed_time | baby_unsettled_default (Colic) |
| gn_d13 | advice does not mention: Paracetamol or ibuprofen if uncomfortable | self_manageable / self_care / not_needed | self_manageable / self_care / not_needed | blocked_or_runny_nose_default (Common cold) |
| hb_d02 | red flag "Long-lasting cough with weight loss in a smoker" escalated but missed | urgent / urgent_care / today | urgent / urgent_care / today | rf_cough_coughing_up_blood (Cough) |
| hb_d03 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_hb_more_than_streaks (Coughing up blood) |
| hb_d04 | over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact 111 today | urgent / urgent_care / today | emergency / emergency_department / now | rf_hb_with_high_temperature (Pneumonia) |
| hb_d05 | red flag "Coughing up small spots or streaks of blood" escalated but found but not named as a red flag<br>over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact 111 today | urgent / urgent_care / today | emergency / emergency_department / now | rf_hb_clot_risk (AI judgement, needs clinical review) |
| hb_d08 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_hb_more_than_streaks (Coughing up blood) |
| hb_d09 | over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact 111 today | urgent / urgent_care / today | emergency / emergency_department / now | rf_hb_with_breathing_heart_or_pain (Coughing up blood) |
| mh_d02 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sh_plan (Help for suicidal thoughts) |
| mh_d03 | level of care differs<br>advice does not mention: Stay with him; Tell the medical team what was taken | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| mh_d04 | red flag "Suicidal thoughts getting stronger or more frequent" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_sh_suicidal_thoughts (Help for suicidal thoughts) |
| mh_d05 | red flag "New hallucinations and delusions (possible psychosis)" escalated but found but not named as a red flag | urgent / urgent_care / today | urgent / urgent_care / today | hearing_or_seeing_things_default (Charles Bonnet syndrome) |
| mh_d06 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_ag_psychosis_or_mania (Bipolar disorder: symptoms) |
| mh_d07 | red flag "Rapid, large weight loss" escalated but found but not named as a red flag | soon / general_practice / few_days | soon / general_practice / few_days | or_ep_weight_loss (Anorexia: symptoms) |
| mh_d14 | advice does not mention: Get help if it lasts beyond 2 weeks or gets worse | self_manageable / self_care / not_needed | self_manageable / self_care / not_needed | feeling_anxious_default (Anxiety, fear and panic) |
| mix_d04 | red flag "Breathless when lying down and with everyday activity" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_sob_lying_flat (Heart failure) |
| mix_d05 | over-triage by 1 level<br>advice does not mention: Ask the GP surgery for an urgent appointment or contact NHS 111 | urgent / general_practice / today | emergency / emergency_ambulance / now | rf_sob_chest_pain (Chest pain) |
| mix_d06 | over-triage by 1 level<br>advice does not mention: Ask for an urgent GP appointment or contact NHS 111 | urgent / general_practice / today | emergency / emergency_ambulance / now | rf_sob_chest_pain (Chest pain) |
| mix_d07 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_cough_croup (Croup) |
| pal_d06 | advice does not mention: Talking therapies can be self-referred | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_palp_keep_coming_back (Heart palpitations) |
| pal_d07 | advice does not mention: A blood test may be needed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_palp_keep_coming_back (Heart palpitations) |
| sb_d01 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_rb_vomiting_blood (Stomach ulcer) |
| sb_d04 | advice does not mention: Keep drinking fluids | urgent / urgent_care / today | urgent / urgent_care / today | rf_rb_bloody_diarrhoea (Bleeding from the bottom (rectal bleeding)) |
| sb_d05 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_br_urgent_signs (Acid reflux in babies) |
| sb_d07 | over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or call 111 | urgent / general_practice / today | emergency / emergency_department / now | rf_dv_vomiting_blood (Being sick) |
| sb_d08 | red flag "Signs of dehydration in an older person" escalated but found but not named as a red flag<br>over-triage by 1 level<br>advice does not mention: Diarrhoea for more than 7 days needs help | soon / community_pharmacy / no_fixed_time | urgent / urgent_care / today | dehydration_default (Dehydration) |
| sb_d10 | red flag "Blood in poo for 3 weeks, with a change in pooing and weight loss: possible bowel cancer" escalated but found but not named as a red flag<br>over-triage by 1 level<br>advice does not mention: Get urgent help if poo turns black or dark red | routine / general_practice / no_fixed_time | soon / general_practice / few_days | likely_condition_soon (AI judgement, needs clinical review) |
| sb_d11 | red flag "Bloating that does not go away, with weight loss: possible ovarian cancer" escalated but found but not named as a red flag | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_bl_gp (Bloating) |
| sb_d12 | advice does not mention: Do not get cross with the child | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | soiling_default (Soiling (child pooing their pants)) |
| sb_d14 | level of care differs | self_manageable / community_pharmacy / not_needed | self_manageable / self_care / not_needed | indigestion_default (Indigestion) |
| sk_d01 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_ra_non_fading (Meningitis) |
| sk_d04 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_it_jaundice (Jaundice) |
| sk_d05 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_bi_cellulitis (Cellulitis) |
| sk_d07 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_eh_sudden_change (Excessive hair growth (hirsutism)) |
| sk_d09 | red flag "Dark area under a nail without an injury (possible melanoma)" escalated but found but not named as a red flag | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_na_gp (Nail problems) |
| sob_d02 | over-triage by 2 levels | routine / general_practice / no_fixed_time | urgent / urgent_care / today | rf_hp_breathless_or_palpitations (AI judgement, needs clinical review) |
| sob_d03 | over-triage by 1 level<br>advice does not mention: Self-care for breathlessness (sit upright, slow breathing, cooler room) | self_manageable / self_care / not_needed | routine / general_practice / no_fixed_time | breathlessness_default (Shortness of breath) |
| sob_d04 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sob_sudden (Pulmonary embolism) |
| sob_d05 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sob_chest_tight_or_heavy_no_asthma (Shortness of breath) |
| sob_d06 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sob_child_struggling (Shortness of breath) |
| sob_d07 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| sob_d08 | level of care differs<br>advice does not mention: Weigh herself; sudden weight gain matters | urgent / general_practice / today | urgent / urgent_care / today | rf_sob_lying_flat (Heart failure) |
| sob_d09 | over-triage by 3 levels<br>advice does not mention: See a GP, or refer herself to a talking therapies service | routine / general_practice / no_fixed_time | emergency / emergency_department / now | rf_sob_sudden (Pulmonary embolism) |
| sob_d10 | level of care differs<br>advice does not mention: Get help sooner if coughing up frothy pink phlegm or sudden weight gain | urgent / general_practice / today | urgent / urgent_care / today | rf_sl_breathless (Heart failure) |
| sob_d11 | over-triage by 1 level<br>advice does not mention: Urgent GP appointment or NHS 111; Painkillers such as paracetamol or ibuprofen; do not smoke | urgent / general_practice / today | emergency / emergency_ambulance / now | rf_sob_chest_pain (Chest pain) |
| sob_d12 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_sob_copd_flare_up (COPD) |
| sob_d16 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sob_sepsis_signs (Sepsis) |
| st_d15 | red flag "A lump in the neck together with a sore throat" escalated but found but not named as a red flag | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_st_over_a_week (Sore throat) |
| st_h12 | level of care differs | emergency / emergency_department / now | emergency / emergency_ambulance / now | rf_lips_or_skin_blue_grey (Heart attack) |
| st_h13 | red flag "A mouth ulcer that has lasted more than 3 weeks, together with a sore throat" escalated but found but not named as a red flag | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_st_lump_or_ulcer (Sore throat) |
| um_d04 | red flag "Blood in pee, even without pain: possible cancer" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | blood_in_urine_default (Blood in urine) |
| um_d06 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | or_ht_pain_back_or_side (Kidney infection) |
| um_d07 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_tp_lump_or_change (Pain in testicles) |
| um_d08 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_pp_higher_chance (Urinary tract infections (UTIs)) |
| um_d09 | red flag "Hard lump in the testicle: possible testicular cancer" escalated but missed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | testicle_lumps_and_swellings_default (Testicle lumps and swellings) |
| wh_d01 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_mp_ectopic_burst_signs (Ectopic pregnancy) |
| wh_d04 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_perp_painkillers_not_helping (Menstrual pain) |
| wh_d05 | red flag "Missed period, unusual bleeding and tummy pain: possible ectopic pregnancy" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_bb_missed_period_and_pain (Bleeding between periods or after sex) |
| wh_d07 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | vaginal_discharge_default (Vaginal discharge) |
| wh_d09 | red flag "Bleeding after the menopause, which can be a sign of cancer" escalated but found but not named as a red flag<br>over-triage by 1 level | routine / general_practice / no_fixed_time | soon / general_practice / few_days | bleeding_after_menopause_default (Bleeding after the menopause) |
| wh_d10 | red flag "Bloodstained nipple discharge" escalated but missed | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | nipple_discharge_default (Nipple discharge) |
| wz_d02 | over-triage by 1 level<br>advice does not mention: Rest, fluids, painkillers; antibiotics not needed for a viral infection; A pharmacist can recommend cough medicines | self_manageable / community_pharmacy / not_needed | routine / general_practice / no_fixed_time | wheezing_default (Asthma) |
| wz_d03 | over-triage by 1 level<br>advice does not mention: Keep him upright, smaller feeds more often, check on him regularly including at night | self_manageable / self_care / not_needed | routine / general_practice / no_fixed_time | wheezing_default (Asthma) |
| wz_d04 | over-triage by 1 level<br>advice does not mention: Urgent GP appointment or call 111; Smaller feeds more often | urgent / general_practice / today | emergency / emergency_department / now | rf_wh_young_child_not_peeing (Sepsis) |
| wz_d05 | level of care differs<br>advice does not mention: Get help urgently if more short of breath than usual | urgent / general_practice / today | urgent / urgent_care / today | rf_cough_copd_flare_up (COPD) |
| wz_d07 | less urgent than expected by 2 levels<br>advice does not mention: Rest and fluids | urgent / general_practice / today | routine / general_practice / no_fixed_time | wheezing_default (Asthma) |
| wz_d08 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_cough_croup (Croup) |
| wz_d11 | advice does not mention: Reduce pollen exposure | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_cough_symptoms_worse (Chest infection) |
| wz_d12 | red flag "Shivering uncontrollably with an infection" escalated but found but not named as a red flag<br>level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_ht_breathing_very_fast (Sepsis) |
| cg_d13_v1 | variant gave a different outcome from its base case | routine / general_practice / no_fixed_time | soon / general_practice / few_days | |
| cg_d15_v1 | variant gave a different outcome from its base case | self_manageable / self_care / not_needed | routine / community_pharmacy / no_fixed_time | |
| gn_d12_v1 | variant gave a different outcome from its base case | routine / general_practice / no_fixed_time | self_manageable / self_care / not_needed | |
| sk_d01_v1 | variant gave a different outcome from its base case | emergency / emergency_department / now | emergency / emergency_ambulance / now | |
| sob_d06_v2 | variant gave a different outcome from its base case | emergency / emergency_department / now | emergency / emergency_ambulance / now | |
| st_d23_v1 | variant gave a different outcome from its base case | routine / general_practice / no_fixed_time | soon / general_practice / few_days | |
