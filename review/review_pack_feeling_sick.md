# Review pack: Feeling sick (nausea)

**Status: AI-drafted, not clinically reviewed. Not for clinical use.**

Knowledge base version 0.4.0. Generated from the knowledge base by `python triage.py review-pack`. Do not edit by hand: change the knowledge base files and generate it again.

## What we are asking you to check

This content was drafted by AI from the published pages listed below. Please check:

1. Is any red flag for this symptom **missing**?
2. Is each rule's **urgency and level of care** right?
3. Is each **question** clear, and does it mean what the source means?
4. Is the **advice** right, specific enough, and safe?
5. For each item under "AI judgement and open points": keep, change or remove?

Mark the "OK?" column, or write comments against the rule id.

## How the engine uses this

- Each rule says: when these findings are present, the outcome is **at least** this.
- The most urgent rule that fires wins. If none fires, the default outcome is used.
- Red flags are always all checked. After an emergency outcome, the engine only asks what could still raise it to the most urgent outcome (an ambulance), then stops.
- "Not sure" is never treated as "no". If a rule cannot be ruled out, the more urgent outcome is chosen.

## Sources

| Page | Accessed | Page last reviewed | Note |
| --- | --- | --- | --- |
| [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | 2026-11-18 | 2024-09-12 |  |
| [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | 2026-11-18 | 2026-03-31 |  |
| [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | 2026-11-18 | 2024-01-30 |  |
| [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | 2026-11-18 | 2026-04-02 |  |
| [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | 2026-11-18 | 2024-04-26 |  |
| [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Jaundice](https://www.nhs.uk/conditions/jaundice/) | 2026-11-19 |  | Page last reviewed: 22 January 2024 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Gastritis](https://www.nhs.uk/conditions/gastritis/) | 2026-11-19 |  | Page last reviewed: 05 August 2026 |
| [Indigestion](https://www.nhs.uk/conditions/indigestion/) | 2026-11-19 |  | Page last reviewed: 05 May 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | 2026-11-19 |  | Page last reviewed: 16 October 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Appendicitis](https://www.nhs.uk/conditions/appendicitis/) | 2026-11-19 |  | Page last reviewed: 09 August 2024 |

Content adapted from these pages contains public sector information licensed under the Open Government Licence v3.0. Adapted text no longer carries the original clinical approval.

## Red flags checked for everyone

Asked as one question: *"First, do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_stroke_signs`<br>Signs of a stroke now or in the last 24 hours | "Signs of a stroke" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_severe_breathing_difficulty`<br>Severe difficulty breathing: gasping, choking or not able to get words out | "Severe difficulty breathing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_lips_or_skin_blue_grey`<br>Lips or skin pale, blue or grey | "Lips or skin pale, blue or grey" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_passed_out`<br>Passed out and not responding normally | "Passed out and not responding normally" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| `rf_sudden_confusion`<br>Suddenly confused<br>**Note:** The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review. | "Suddenly confused" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| `rf_heavy_bleeding`<br>Bleeding that cannot be stopped, or blood coming out in spurts | "Bleeding that cannot be stopped" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_serious_self_harm`<br>Has seriously self-harmed, or feels about to self-harm | "Serious self-harm or about to self-harm" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |

## Feeling sick (nausea) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fs_heart_attack_signs`<br>Suddenly feeling sick with chest pain that feels tight or heavy, pain spreading to the arms, back, neck or jaw, or shortness of breath: possible heart attack<br>**Note:** Any chest pain also brings in the chest pain rules. | "Chest feels tight or squeezed" OR "Chest feels heavy" OR "Pain spreads to arm, neck, jaw, shoulder, stomach or back" OR "Short of breath" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| `rf_fs_meningitis_signs`<br>Feeling sick with a stiff neck, or pain when looking at bright lights<br>**Note:** The Diarrhoea and vomiting page gives this for being sick. Applying it to feeling sick without being sick is AI judgement. | "Stiff neck" OR "Bright lights hurt the eyes or are bothering you" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_fs_sudden_headache`<br>Feeling sick with a sudden, severe headache<br>**Note:** As above: applying it to feeling sick is AI judgement. | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_fs_sudden_tummy_ache`<br>Feeling sick with a sudden, severe tummy ache | "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| `rf_fs_swallowed_poison`<br>Feeling sick after possibly swallowing something poisonous or harmful | "May have swallowed something poisonous or harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E. Take the packet or container with you.* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_fs_dka_ketones`<br>Diabetes, with high ketones or a high blood sugar that insulin is not bringing down | "Has diabetes" AND "High ketones, or high blood sugar that insulin is not bringing down" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_fs_dka_signs`<br>Very thirsty and peeing a lot, with fruity breath or very fast breathing: possible diabetic ketoacidosis | ("Feeling very thirsty all the time" AND "Peeing more often than usual") AND ("Breath smells fruity" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |

## Feeling sick (nausea) red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fs_yellow_skin`<br>Feeling sick with yellow skin or yellow whites of the eyes | "Yellow skin or yellow whites of the eyes (jaundice)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| `rf_fs_kidney_infection`<br>Feeling sick with pain in the side or back under the ribs, and a high temperature: possible kidney infection | "Pain in the back or side, just under the ribs" AND "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | |
| `rf_fs_thirsty_peeing`<br>Very thirsty and peeing much more than usual: possible diabetes<br>**Note:** Clinical knowledge: feeling sick with thirst and peeing more can be a sign of high blood sugar. It needs a blood sugar test the same day. | "Feeling very thirsty all the time" AND "Peeing more often than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_fs_diabetes`<br>Diabetes, and feeling sick<br>**Note:** The page says call the diabetes team or 111 if you have diabetes, feel unwell and your ketones are slightly high. Without a ketone reading, feeling sick is taken as a reason to check. A reading of the source, so soft. | "Has diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Check your blood sugar and ketones if you can. Call your diabetes care team now or get help from NHS 111.* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_fs_full_quickly`<br>Feeling sick and full after eating only a little<br>**Note:** The Gastritis and Stomach ulcer pages say an urgent GP appointment or 111 for feeling full after a small meal with their symptoms. These can be signs of something more serious. | "Feels full after eating only a little" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Gastritis](https://www.nhs.uk/conditions/gastritis/) | |
| `rf_fs_swallowing`<br>Feeling sick, and it is hard or painful to swallow | "Problems swallowing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Gastritis](https://www.nhs.uk/conditions/gastritis/) | |

## Feeling sick (nausea): other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_fs_few_days`<br>Feeling sick for more than a few days without getting better | "Feeling sick for more than a few days" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Call 111 for advice if you cannot see a GP.* | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| `or_fs_often`<br>Often feels sick (it keeps coming back) | "Often feels sick" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Call 111 for advice if you cannot see a GP.* | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| `or_fs_weight_loss`<br>Feeling sick and losing weight without trying<br>**Note:** The Gastritis page says an urgent GP appointment or 111 for weight loss with its symptoms. Likely conditions can raise it. | "Losing weight without trying" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Indigestion](https://www.nhs.uk/conditions/indigestion/) | |

## Default outcome

Used when no rule fires.

- **Feeling sick with nothing that needs more help: try things that may help at home**
- Outcome: Self-manageable, Self-care, No appointment needed. *Feeling sick usually goes away on its own*
- Source: [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feeling sick (nausea) | Do you feel sick (nausea)? | 422587007 | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chest feels tight or squeezed | Does your chest feel tight, or like it is being squeezed? | 23924001 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Chest feels heavy | Does your chest feel heavy? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Pain spreads to arm, neck, jaw, shoulder, stomach or back | Does the pain spread to your left or right arm, or to your neck, jaw, shoulder, stomach or back? | 10000006 | [Angina](https://www.nhs.uk/conditions/angina/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| May have swallowed something poisonous or harmful | Could you have swallowed something poisonous? For example, a cleaning product, a plant, or someone else's medicine. Or a button battery or magnets? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| High ketones, or high blood sugar that insulin is not bringing down | Have you tested your ketones and they are high (over 3mmol/L in blood, or over 2+ in pee)? Or is your blood sugar high and your insulin is not bringing it down? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Yellow skin or yellow whites of the eyes (jaundice) | Have your skin or the whites of your eyes turned yellow? | 18165001 | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| Pain in the back or side, just under the ribs | Do you have pain in your back or side, just under the ribs? | 271857006 | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels full after eating only a little | Do you feel full after eating only a small amount of food? |  | [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Feeling sick for more than a few days | Have you felt sick for more than a few days without it getting better? |  | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| Often feels sick | Do you often feel sick? For example, it keeps coming back over weeks or months. |  | [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |

## Advice given with each outcome

### `advice_stroke`

**What to do:** Call 999 now. You may be having a stroke, or may have had one.

**Look out for:**
- One side of the face drooping
- Not being able to lift both arms and keep them up
- Slurred or confused speech
- Signs of a stroke can stop after a short time. Get help straight away even if they have stopped.

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/)

### `advice_breathing_emergency`

**What to do:** Call 999 now.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes
- Call 999 again if you move to a different place

**Where to go:** Call 999. Do not drive yourself to A&E. Stay with the person until help arrives.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/)

### `advice_sudden_confusion`

**What to do:** Call 999 or go to A&E now.

**Look out for:**
- Severe difficulty breathing, such as gasping, choking or not being able to get words out
- Lips or skin turning very pale, blue or grey

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/)

### `advice_heavy_bleeding`

**What to do:** Call 999 or go to A&E now.

**Look out for:**
- Blood that comes out in spurts and is bright red and hard to control
- Blood coming through the bandage or cloth. If it does, put another one on top and keep pressing.

**Get more help when:**
- Call 999 if you cannot stop the bleeding or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Press firmly on the wound with a bandage or a clean, folded cloth
- If something is stuck in the wound, do not take it out. Press on either side of it.
- If the wound is on a hand or arm, raise it above your head. If it is on a leg, lie down and raise it above the level of your heart.

Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/)

### `advice_self_harm`

**What to do:** Call 999 for an ambulance or go straight to A&E. Or ask someone else to call 999 or take you to A&E.

**Look out for:**
- Feeling that you may be about to harm yourself

**Get more help when:**
- If your life is in danger, call 999 now
- If you need someone to talk to, call Samaritans on 116 123 at any time, or text SHOUT to 85258

**Where to go:** Call 999 or go straight to A&E. Try to be around other people and get yourself to a safe place.

Source: [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

### `advice_feeling_sick_999`

**What to do:** Call 999 now. Feeling sick with chest pain, chest tightness or shortness of breath could be a heart attack.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- Sit and rest while you wait for help
- Take aspirin (300mg) if you have any, unless you are allergic to it

Source: [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/)

### `advice_dv_ae`

**What to do:** Call 999 or go to A&E now. This needs to be checked in hospital straight away.

**Look out for:**
- Being very sleepy, confused or not responding as usual
- Blue, grey, pale or blotchy skin, lips or tongue
- Finding it hard to breathe

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. If you may have swallowed something harmful, bring the packet or container.

**What you can do yourself:**
- If you have swallowed something harmful, do not try to make yourself sick

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/)

### `advice_stomach_ache_ae`

**What to do:** Call 999 or go to A&E now. Your tummy pain needs to be checked in hospital straight away.

**Look out for:**
- Pain getting worse, or spreading across your tummy
- Feeling faint, passing out, or cold, clammy, pale skin
- Being sick with blood, or green sick

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat anything until a doctor has checked you. Small sips of water are fine.
- Do not take ibuprofen or aspirin. They can make some tummy problems worse.

Source: [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/), [Appendicitis](https://www.nhs.uk/conditions/appendicitis/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

### `advice_dka_ae`

**What to do:** Call 999 or go to A&E now. These can be signs of diabetic ketoacidosis (DKA), a serious problem caused by a lack of insulin. It needs treatment in hospital straight away.

**Look out for:**
- Being sick, and not able to keep fluids down
- Feeling very sleepy or confused
- Breathing deeply or fast

**Get more help when:**
- Call 999 if the person gets worse, is hard to wake, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive. Bring your insulin, your blood sugar meter and any other medicines you take.

**What you can do yourself:**
- Keep taking your insulin. Do not stop it, even if you are not eating.
- Keep having sips of water

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/)

### `advice_feeling_sick_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Feeling sick with your other symptoms should be checked today.

**Look out for:**
- Being sick with blood, or green sick
- A sudden, severe tummy ache or headache
- Chest pain, or feeling short of breath

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Take regular sips of a cold drink
- Eat small meals when you feel able to

Source: [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/), [Jaundice](https://www.nhs.uk/conditions/jaundice/), [Gastritis](https://www.nhs.uk/conditions/gastritis/)

### `advice_dka_urgent`

**What to do:** Call your diabetes care team now, or get help from NHS 111. Being unwell or being sick when you have diabetes can quickly make your blood sugar and ketones go up.

**Look out for:**
- Ketones over 3mmol/L in your blood, or over 2+ in your pee
- Feeling very thirsty and peeing a lot, or breath that smells fruity
- Feeling very sleepy or confused, or breathing fast

**Get more help when:**
- Call 999 or go to A&E if your ketones are high, or you get any of the signs above

**Where to go:** Call your diabetes care team, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Check your blood sugar and ketones more often, as your diabetes team has told you
- Keep taking your insulin, and drink plenty of sugar-free fluids
- Follow your sick day rules if you have them

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/)

### `advice_feeling_sick_gp`

**What to do:** See a GP. They can look for the cause of your sick feeling and suggest treatments. Call 111 for advice if you cannot see a GP.

**Look out for:**
- Being sick and not able to keep fluids down
- Losing weight without trying
- Yellow skin or yellow whites of the eyes

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 if you suddenly feel sick and have chest pain or shortness of breath

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Get plenty of fresh air, and take regular sips of a cold drink
- Eat smaller meals more often, and avoid hot, fried or greasy food

Source: [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/)

### `advice_feeling_sick_self_care`

**What to do:** Feeling sick usually goes away on its own. There are things you can try that might help.

**Look out for:**
- Being sick, and signs of dehydration (not having enough water in the body), such as peeing less
- A stomach ache, or a high temperature
- Feeling sick for more than a few days

**Get more help when:**
- See a GP if you do not feel better in a few days, or it keeps coming back
- Call 999 if you suddenly feel sick and have chest pain that feels tight or heavy. Do the same if pain spreads to your arms, back, neck or jaw, or you are short of breath.

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Get plenty of fresh air, and distract yourself, for example with music or a film
- Take regular sips of a cold drink, or try ginger or peppermint tea
- Eat smaller meals more often, and do not lie down soon after eating
- Do not eat or cook strong-smelling, hot, fried or greasy food

Source: [Feeling sick (nausea)](https://www.nhs.uk/symptoms/feeling-sick-nausea/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_fs_heart_attack_signs`: Any chest pain also brings in the chest pain rules.
- `rf_fs_meningitis_signs`: The Diarrhoea and vomiting page gives this for being sick. Applying it to feeling sick without being sick is AI judgement.
- `rf_fs_sudden_headache`: As above: applying it to feeling sick is AI judgement.
- `rf_fs_thirsty_peeing`: Clinical knowledge: feeling sick with thirst and peeing more can be a sign of high blood sugar. It needs a blood sugar test the same day.
- `rf_fs_diabetes`: The page says call the diabetes team or 111 if you have diabetes, feel unwell and your ketones are slightly high. Without a ketone reading, feeling sick is taken as a reason to check. A reading of the source, so soft.
- `rf_fs_full_quickly`: The Gastritis and Stomach ulcer pages say an urgent GP appointment or 111 for feeling full after a small meal with their symptoms. These can be signs of something more serious.
- `or_fs_weight_loss`: The Gastritis page says an urgent GP appointment or 111 for weight loss with its symptoms. Likely conditions can raise it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Diabetic ketoacidosis (DKA). This is when a lack of insulin makes you very ill. | 420422005 | rare | Breath smells fruity: strongly supports; Breathing faster and more deeply than usual: strongly supports; Blood sugar high and not coming down, or ketones raised: strongly supports; Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Keeps being sick and cannot keep fluids down: supports; Stomach ache: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Being sick: strongly supports; High ketones, or high blood sugar that insulin is not bringing down: strongly supports; Breathing very fast: supports; Losing weight without trying: supports; Feels very tired: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Appendicitis (a swollen appendix, a pouch on the bowel) | 74400008 | uncommon | Pain started around the belly button and moved to the lower right: strongly supports; Pain in the lower right side of the tummy: strongly supports; Tummy pain worse when moving, coughing or going over bumps: strongly supports; Not feeling hungry, or eating much less than usual: strongly supports; Stomach ache: strongly supports; Stomach ache gradually getting worse: supports; Feeling sick (nausea): supports; Being sick: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Food poisoning | 75258004 | common | Started after eating food that may have been off, or others who ate it are ill: strongly supports; Diarrhoea: strongly supports; Being sick: strongly supports; Others nearby have the same symptoms: supports; Cramping tummy pain that comes and goes in waves: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Gallstones (small stones in the gallbladder that can cause attacks of pain) | 235919008 | uncommon | Pain in the upper right of the tummy, just under the ribs: strongly supports; Tummy pain that comes on after eating, especially fatty food: strongly supports; Severe stomach ache: supports; Tummy pain that spreads to the back: supports; Feeling sick (nausea): supports; Being sick: supports |
| Gastritis (swelling of the stomach lining) | 4556007 | uncommon | Pain in the upper middle of the tummy, below the breastbone: strongly supports; Indigestion or heartburn: strongly supports; Feeling sick (nausea): supports; Tummy pain that comes on after eating, especially fatty food: supports; Not feeling hungry, or eating much less than usual: supports; Heartburn or a sour taste in the mouth: supports |
| Stomach bug (gastroenteritis) | 69776003 | very common | Diarrhoea: strongly supports; Being sick: strongly supports; Others nearby have the same symptoms: supports; Cramping tummy pain that comes and goes in waves: supports; Very high temperature, or feels hot, cold or shivery: supports; Feeling sick (nausea): supports |
| Liver problems (such as liver damage from alcohol) | 235856003 | rare | Yellow skin or yellow whites of the eyes (jaundice): strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Not feeling hungry, or eating much less than usual: supports; Feels very tired: supports; Losing weight without trying: supports; Feels sick or has been sick: supports; Swollen feet, ankles or legs: supports; Pale poo and dark pee: strongly supports; Pain in the upper right of the tummy, just under the ribs: supports; Drinks a lot of alcohol: supports; Feeling sick (nausea): supports; Itchy skin on other parts of the body too: supports |
| Motion sickness (travel sickness) | 37031009 | uncommon | Started while travelling by car, boat, plane or on a ride: strongly supports; Feels light-headed: supports; Being sick: supports |
| Sickness in pregnancy (morning sickness) | 51885006 | uncommon | Pregnant, or could be pregnant: strongly supports; Pregnant, or gave birth in the last 6 weeks: supports; Being sick: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |
| Severe sickness in pregnancy (hyperemesis gravidarum) | 14094001 | rare | Keeps being sick and cannot keep fluids down: strongly supports; Pregnant, or could be pregnant: strongly supports; Feels sick or has been sick: strongly supports; Signs of dehydration: strongly supports; Losing weight without trying: supports; Feels light-headed: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
