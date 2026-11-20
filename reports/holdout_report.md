# Run report: holdout set

Run 2026-11-19. Engine 0.7.0, knowledge base 0.4.0 (AI-drafted, not clinically reviewed), commit b1fd386, method: rules_and_conditions. 114 cases. Structured mode, no LLM.

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
| **This engine** | **PASS** 83 of 83 (100%) | **PASS** 114 of 114 (100%) | 114 of 114 | 20 of 114 (18%) |
| Always 999, asks nothing | | | 114 of 114 | 82 of 114 (72%) |
| Always self-care, asks nothing | | | 26 of 114 | 0 of 114 (0%) |

With this few cases the true rates could differ: red flags escalated 95% range 96% to 100%; not below minimum safe 95% range 97% to 100%.

**Red-flag recognition** (a score, not a gate): did the engine find and name each red flag, as well as escalate? found but not named as a red flag: 4; missed: 3; not asked: already at an outcome this urgent: 33; recognised: 43.

**Ambulance cases not given an ambulance** (a score, not a gate, because many sources say "999 or A&E" together): cg_h07, en_h02, hb_h02, mh_h01, mh_h02, st_h18.

## Scores

| Measure | Result |
| --- | --- |
| Acuity matches expected | 89 of 114 (78%), 95% range 70% to 85% |
| Level of care matches expected | 81 of 114 (71%) |
| Timeframe matches expected | 89 of 114 (78%) |
| All three match | 71 of 114 (62%) |
| Over-triage (more urgent than expected) | 20 of 114 (18%): 14 by 1 level, 3 by 2 levels, 3 by 3 levels |
| Less urgent than expected | 5 cases, of which 5 still at or above minimum safe |
| Items read per case (each checklist line counts) | mean 27.0 |
| Words read per case | mean 296, most 754 |
| Interactions per case (a checklist counts as one) | mean 8.9, median 8.0, most 31 |
| Interactions before the first red flag was found | mean 2.3 |
| Safety-netting: all three parts present | 114 of 114 (100%) |
| Safety-netting: points the vignette asked for | 218 of 250 (87%) (a word check only, needs human judgement) |
| Safety-netting: same word check if every case got one fixed advice text | 197 of 250 (79%) (best single text: advice_dizziness_gp). The gap to the line above is what tailoring adds. |
| Advice length | median 125.0 words |
| Consistency: identical record on repeat | 114 of 114 (100%) |
| Consistency: same patient, volunteering more or less up front, gives the same outcome | 44 of 47 (94%). Reworded wording is not tested: that needs the language layer. |
| Context tests: context led to an outcome at least as close to expected, and safe | 8 of 8 (100%), of which closer: 0 |
| Coverage: handled by a module | 114 of 114 (100%) |
| Outcome driven by caution (missing information) | 3 cases |

## Outcome profile

Over-triage has a cost at scale, so the spread of outcomes matters as well as the gates.

| Level of care | Engine | Expected |
| --- | --- | --- |
| emergency ambulance | 20 | 22 |
| emergency department | 19 | 10 |
| urgent care | 25 | 12 |
| general practice | 28 | 43 |
| dental | 0 | 0 |
| community pharmacy | 4 | 8 |
| self care | 18 | 19 |

| Acuity | Engine | Expected |
| --- | --- | --- |
| emergency | 39 | 32 |
| urgent | 26 | 24 |
| soon | 6 | 13 |
| routine | 25 | 21 |
| self manageable | 18 | 24 |

## Comparators

**Fixed-order baseline.** A stand-in, not any real triage system. It uses the same rules but asks every question one at a time in file order.

- Same outcome as the engine: 82 of 114 (72%)
- Items read per case: engine 27.0, baseline 38.0
- Words read per case: engine 296, baseline 589
- Interactions per case (a checklist counts as one, so this flatters the engine): engine 8.9, baseline 38.0
- Different outcome in bj_h03: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_h01: engine self_manageable / self_care / not_needed, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in cg_h02: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_h04: engine soon / general_practice / few_days, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_h05: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_h06: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in cg_h08: engine routine / general_practice / no_fixed_time, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in cp_h23: engine urgent / urgent_care / today, baseline routine / general_practice / no_fixed_time. The engine stopped before a question that would have changed it.
- Different outcome in en_h01: engine emergency / emergency_department / now, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in gn_h03: engine soon / general_practice / few_days, baseline urgent / urgent_care / today. The engine stopped before a question that would have changed it.
- Different outcome in gn_h04: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_h04: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mh_h06: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_h04: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in mix_h05: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sb_h03: engine urgent / urgent_care / today, baseline emergency / emergency_ambulance / now. The engine stopped before a question that would have changed it.
- Different outcome in sk_h03: engine routine / community_pharmacy / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h02: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h03: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h04: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h06: engine emergency / emergency_ambulance / now, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h07: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in sob_h08: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_h19: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_h20: engine self_manageable / self_care / not_needed, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_h22: engine routine / community_pharmacy / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_h23: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in st_h24: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in um_h02: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wh_h02: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_h04: engine urgent / urgent_care / today, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.
- Different outcome in wz_h06: engine routine / general_practice / no_fixed_time, baseline emergency / emergency_department / now. The engine stopped before a question that would have changed it.

**LLM-only baseline.** Not built. No LLM provider has been agreed.

**Risk setting sweep.** See `reports/sweep_report.md`, written by `python triage.py sweep`.

## Patient context

- Interactions per case with no context: 10.8, basic: 9.0, full: 8.9
- Cases where full context changed the acuity compared with none: 2
  - bj_h03: with no context soon, with full context self_manageable, not a context test
  - sob_h03: with no context emergency, with full context urgent, not a context test
  - cg_h05: with no context routine (chosen out of caution, because information was missing), with full context routine, expected more urgent (as expected)
  - cp_h21: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)
  - hb_h03: with no context emergency (chosen out of caution, because information was missing), with full context emergency, expected same (as expected)
  - mh_h01: with no context emergency, with full context emergency, expected same (as expected)
  - mix_h05: with no context urgent, with full context urgent, expected same (as expected)
  - pal_h04: with no context emergency, with full context emergency, expected same (as expected)
  - sb_h02: with no context urgent, with full context urgent, expected same (as expected)
  - st_h24: with no context urgent (chosen out of caution, because information was missing), with full context urgent, expected more urgent (as expected)

## "Not sure" stress test

Reported separately. Here the simulated patient answers "not sure" to anything the vignette does not mention, where the main run answers "no". It shows how much the outcomes rest on unstated negatives.

- No outcome below minimum safe urgency: 114 of 114 (100%)
- Red flags gate passed: 114 of 114 (100%) cases
- More urgent than expected: 82 of 114 (72%)
- Outcome driven by caution: 107 of 114 (94%)
- Emergency outcomes: 114 of 114 (100%)
- Interactions per case: 1.0

## Failures, case by case

| Case | What | Expected | Engine gave | Decided by |
| --- | --- | --- | --- | --- |
| bj_h02 | red flag "Snap at the back of the heel and cannot stand on tiptoe (possible Achilles tendon rupture)" escalated but missed | urgent / urgent_care / today | urgent / urgent_care / today | rf_foot_injury_signs (Ankle pain) |
| bj_h04 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | limp_default (Limping in children) |
| bj_h05 | advice does not mention: Mention the statin to the GP | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_cramp_gp (Leg cramps) |
| bn_h02 | over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact NHS 111 today | urgent / urgent_care / today | emergency / emergency_ambulance / now | rf_pn_weakness (Paralysis) |
| bn_h04 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | or_dz_keeps_coming_back (Dizziness) |
| bn_h05 | over-triage by 1 level | routine / general_practice / no_fixed_time | soon / general_practice / few_days | or_sl_driving (AI judgement, needs clinical review) |
| cg_h02 | level of care differs | self_manageable / community_pharmacy / not_needed | self_manageable / self_care / not_needed | cough_default (Cough) |
| cg_h03 | over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact NHS 111 today | urgent / urgent_care / today | emergency / emergency_ambulance / now | rf_sob_chest_pain (Chest pain) |
| cg_h04 | red flag "Asthma attack in the last day, now recovered" escalated but found but not named as a red flag | soon / general_practice / few_days | soon / general_practice / few_days | or_cough_asthma_attack_recovered (Asthma) |
| cg_h07 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_cough_stridor (Sore throat) |
| cp_h20 | advice does not mention: A pharmacist can advise on heartburn medicines | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | chest_pain_default (Chest pain) |
| cp_h22 | over-triage by 1 level<br>advice does not mention: Ask for an urgent GP appointment or contact NHS 111 | urgent / general_practice / today | emergency / emergency_department / now | rf_cp_present_now (Pulmonary embolism) |
| cp_h23 | over-triage by 2 levels | routine / general_practice / no_fixed_time | urgent / urgent_care / today | rf_cp_sharp_or_stabbing (Pericarditis) |
| cp_h24 | over-triage by 2 levels<br>advice does not mention: See a pharmacist within 3 days of the rash appearing; Get urgent help if the rash spreads to the eye or nose or vision changes | soon / community_pharmacy / few_days | emergency / emergency_department / now | rf_cp_present_now (Pulmonary embolism) |
| en_h02 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sw_cannot_swallow (Glandular fever) |
| en_h03 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_ea_child_under_2_both_ears (Earache) |
| ey_h02 | red flag "Red, sticky eyes in a baby less than 1 month old" escalated but missed | urgent / urgent_care / today | urgent / urgent_care / today | rf_re_newborn (Red eye) |
| ey_h03 | advice does not mention: Not to drive with double vision | soon / general_practice / few_days | soon / general_practice / few_days | likely_condition_soon (AI judgement, needs clinical review) |
| gn_h03 | red flag "Weight loss with loss of appetite" escalated but found but not named as a red flag | soon / general_practice / few_days | soon / general_practice / few_days | or_wl_with_other_symptoms (Unintentional weight loss) |
| gn_h04 | advice does not mention: Get help sooner if weight loss or a high temperature develops | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | irregular_periods_default (Irregular periods) |
| gn_h05 | over-triage by 2 levels<br>advice does not mention: See a GP | routine / general_practice / no_fixed_time | urgent / urgent_care / today | rf_cy_fingers_toes (Blue or grey skin or lips (cyanosis)) |
| gn_h06 | over-triage by 3 levels | self_manageable / self_care / not_needed | urgent / urgent_care / today | dehydration_default (Dehydration) |
| hb_h02 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_hb_with_breathing_heart_or_pain (Coughing up blood) |
| hb_h03 | red flag "Coughing up small spots or streaks of blood" escalated but found but not named as a red flag<br>over-triage by 1 level<br>advice does not mention: Get an urgent GP appointment or contact 111 today | urgent / urgent_care / today | emergency / emergency_department / now | rf_hb_clot_risk (AI judgement, needs clinical review) |
| mh_h01 | level of care differs<br>advice does not mention: Call 999 if he has a fit | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_sudden_confusion (Shortness of breath) |
| mh_h02 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_hs_cannot_keep_safe (Where to get urgent help for mental health) |
| mh_h03 | level of care differs<br>advice does not mention: Reassure that this can happen with sight loss and is not a mental illness | urgent / general_practice / today | urgent / urgent_care / today | hearing_or_seeing_things_default (Charles Bonnet syndrome) |
| mh_h04 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | or_sh_self_harmed (Where to get help for self-harm) |
| mix_h01 | level of care differs | emergency / emergency_department / now | emergency / emergency_ambulance / now | rf_sob_chest_pain (Chest pain) |
| mix_h02 | over-triage by 1 level<br>advice does not mention: Ask for an urgent GP appointment or contact NHS 111 | urgent / general_practice / today | emergency / emergency_department / now | rf_hb_with_high_temperature (Pneumonia) |
| mix_h04 | advice does not mention: Do not give aspirin to children under 16 | self_manageable / self_care / not_needed | self_manageable / self_care / not_needed | cough_default (Cough) |
| mix_h05 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_sob_copd_flare_up (COPD) |
| pal_h02 | advice does not mention: Avoid exercise until checked | urgent / urgent_care / today | urgent / urgent_care / today | rf_palp_stopped_with_symptoms (Heart palpitations) |
| sb_h02 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_rb_black_poo (Bleeding from the bottom (rectal bleeding)) |
| sb_h03 | over-triage by 1 level<br>advice does not mention: Give plenty of fluids and fibre; Get a regular toilet routine and stay calm | soon / general_practice / few_days | urgent / urgent_care / today | rf_sa_blood_in_poo (Stomach ache) |
| sb_h05 | over-triage by 1 level | self_manageable / community_pharmacy / not_needed | routine / community_pharmacy / no_fixed_time | or_ib_threadworms (Threadworms) |
| sk_h02 | over-triage by 1 level<br>advice does not mention: Urgent GP or midwife appointment, or 111 | urgent / general_practice / today | emergency / emergency_department / now | rf_ja_newborn_first_day (Newborn jaundice) |
| sk_h03 | less urgent than expected by 1 level<br>advice does not mention: Impetigo is very infectious: keep him off school and do not share towels | soon / community_pharmacy / few_days | routine / community_pharmacy / no_fixed_time | rash_default (Rashes in babies and children) |
| sob_h03 | level of care differs<br>advice does not mention: Rest and drink plenty of fluids | urgent / general_practice / today | urgent / urgent_care / today | rf_sob_high_temperature (Pneumonia) |
| sob_h06 | level of care differs | emergency / emergency_department / now | emergency / emergency_ambulance / now | rf_ht_child_breathing (Fever in children) |
| sob_h07 | over-triage by 1 level | soon / general_practice / few_days | urgent / urgent_care / today | rf_sob_more_than_usual (Bronchiectasis) |
| sob_h08 | over-triage by 3 levels<br>advice does not mention: Self-help for breathlessness | self_manageable / self_care / not_needed | urgent / urgent_care / today | rf_cough_short_of_breath (Cough) |
| st_h18 | level of care differs | emergency / emergency_ambulance / now | emergency / emergency_department / now | rf_st_drooling (Sore throat) |
| st_h19 | advice does not mention: Do not give honey to a baby under 12 months | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | or_st_child_under_5_needs_help (Sore throat) |
| st_h21 | over-triage by 3 levels<br>advice does not mention: See a pharmacist for pain relief or lozenges | self_manageable / community_pharmacy / not_needed | urgent / urgent_care / today | rf_st_pus_on_tonsils (Tonsillitis) |
| st_h22 | over-triage by 1 level<br>advice does not mention: Do not give aspirin to children under 16 | self_manageable / community_pharmacy / not_needed | routine / community_pharmacy / no_fixed_time | or_st_pharmacy_help (Sore throat) |
| st_h23 | advice does not mention: Do not give aspirin to under-16s | urgent / urgent_care / today | urgent / urgent_care / today | rf_st_pus_on_tonsils (Tonsillitis) |
| st_h24 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_st_weakened_immune_system (Sore throat) |
| um_h02 | red flag "Possible urine infection in a child aged 15 or younger with a high temperature" escalated but missed<br>level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_pp_temperature (Urinary tract infections (UTIs)) |
| um_h03 | over-triage by 1 level<br>advice does not mention: See a pharmacist, who can give UTI treatment; Paracetamol and fluids | soon / community_pharmacy / no_fixed_time | urgent / community_pharmacy / today | likely_condition_urgent (AI judgement, needs clinical review) |
| um_h04 | advice does not mention: Do not try to diagnose it yourself | routine / general_practice / no_fixed_time | routine / general_practice / no_fixed_time | penis_lumps_and_spots_default (Penis lumps and spots) |
| wh_h01 | advice does not mention: Possible miscarriage, handled kindly | emergency / emergency_ambulance / now | emergency / emergency_ambulance / now | rf_bip_heavy (Vaginal bleeding in pregnancy) |
| wh_h02 | level of care differs | urgent / general_practice / today | urgent / urgent_care / today | rf_bp_high_temperature (Breast pain) |
| wh_h04 | less urgent than expected by 1 level | soon / general_practice / few_days | routine / general_practice / no_fixed_time | vaginal_discharge_default (Vaginal discharge) |
| wh_h05 | red flag "Hard breast lump with dimpled skin: possible breast cancer" escalated but found but not named as a red flag<br>over-triage by 1 level | routine / general_practice / no_fixed_time | soon / general_practice / few_days | likely_condition_soon (AI judgement, needs clinical review) |
| wz_h04 | level of care differs<br>advice does not mention: Drink plenty of fluids and rest | urgent / general_practice / today | urgent / urgent_care / today | likely_condition_urgent (AI judgement, needs clinical review) |
| wz_h06 | over-triage by 1 level<br>advice does not mention: Rest, fluids, painkillers; a pharmacist can suggest cough medicines | self_manageable / community_pharmacy / not_needed | routine / general_practice / no_fixed_time | wheezing_default (Asthma) |
| cp_h23_v1 | variant gave a different outcome from its base case | urgent / urgent_care / today | routine / general_practice / no_fixed_time | |
| cp_h23_v2 | variant gave a different outcome from its base case | urgent / urgent_care / today | routine / general_practice / no_fixed_time | |
| mh_h03_v1 | variant gave a different outcome from its base case | urgent / urgent_care / today | routine / general_practice / no_fixed_time | |
