# Review pack: Missed or late periods

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
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/) | 2026-11-19 |  | Page last reviewed: 11 January 2023 |
| [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | 2026-11-19 |  | Page last reviewed: 24 November 2025 |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | 2026-11-19 |  | Page last reviewed: 13 August 2024 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Anal fissure](https://www.nhs.uk/conditions/anal-fissure/) | 2026-11-19 |  | Page last reviewed: 26 June 2025 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Excessive hair growth (hirsutism)](https://www.nhs.uk/symptoms/hirsutism/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Polycystic ovary syndrome](https://www.nhs.uk/conditions/polyendocrine-metabolic-ovarian-syndrome-pmos/) | 2026-11-19 |  | Page last reviewed: 30 June 2026 |
| [Irregular periods](https://www.nhs.uk/symptoms/irregular-periods/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |

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

## Missed or late periods red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_mp_ectopic_burst_signs`<br>Missed period with a sharp, sudden and very bad tummy pain, pain in the tip of the shoulder, or passing out | "Stomach ache that started suddenly and is severe" OR "Pain in the tip of the shoulder" OR "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| `rf_mp_dizzy_with_pain`<br>Missed period with tummy pain and feeling very dizzy or light-headed | "Feels light-headed" AND ("Pelvic pain (pain low down in the tummy)" OR "Pain low down on one side of the tummy") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| `rf_mp_heavy_bleeding`<br>Missed period, then very heavy bleeding: possible miscarriage<br>**Note:** The Miscarriage page says call 999 for heavy bleeding in pregnancy. Applying it to a missed period is AI judgement. | "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |

## Missed or late periods red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_mp_pain_or_bleeding`<br>Missed period with tummy pain, or with unusual bleeding: possible ectopic pregnancy<br>**Note:** The Ectopic pregnancy page: a missed period with tummy pain low down on one side, or vaginal bleeding, needs advice right away, even with a negative pregnancy test. The Vaginal bleeding between periods page gives the same advice. Heavy bleeding is included because it is vaginal bleeding too: the 999 rule for it is soft, and this keeps urgent as the floor. | "Pelvic pain (pain low down in the tummy)" OR "Pain low down on one side of the tummy" OR "Vaginal bleeding between periods or after sex" OR "Heavy bleeding from the vagina" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your GP or call NHS 111 now* | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| `rf_mp_pain_peeing_or_pooing`<br>Missed period with discomfort when peeing or pooing<br>**Note:** The Ectopic pregnancy page lists discomfort when peeing or pooing as a symptom in combination with a missed period. Soft, as a urine infection is a more common cause. | "Pain, burning or stinging when peeing" OR "Pain when pooing" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your GP or call NHS 111* | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| `rf_mp_cannot_keep_food_down`<br>Being sick many times a day and cannot keep food or drink down: possible severe sickness in pregnancy | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your GP or midwife, or call NHS 111, as soon as possible* | [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/) | |

## Missed or late periods: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_mp_three_in_a_row`<br>Missed 3 periods in a row, or periods not started by 15 | "Missed 3 periods in a row" OR "Periods have not started by the age of 15" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| `or_mp_other_symptoms`<br>Missed period with weight change, more hair on the face or body, or oily skin | "Too much hair growth (thick, dark hair on the face or body)" OR "Put on weight without meaning to" OR "Losing weight without trying" OR "Oily skin or acne (spots)" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| `or_mp_irregular`<br>Periods have become irregular | "Irregular periods" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |

## Default outcome

Used when no rule fires.

- **A missed or late period with nothing that needs more help: see a doctor just in case**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/)
- **Note:** The page says most of the time it is nothing to worry about, but see a doctor just in case. Not a floor, so a clearly likely harmless cause can lower it.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Missed or late period | Have you missed a period, or is your period late? |  | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Pain in the tip of the shoulder | Do you have pain in the tip of your shoulder, where your arm meets your shoulder? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Pelvic pain (pain low down in the tummy) | Do you have pain low down in your tummy, between your hips (your pelvis)? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Pain low down on one side of the tummy | Do you have pain low down on one side of your tummy? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Vaginal bleeding between periods or after sex | Are you bleeding from your vagina between periods or after sex? |  | [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Pain when pooing | Does it hurt when you poo? |  | [Anal fissure](https://www.nhs.uk/conditions/anal-fissure/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Missed 3 periods in a row | Have you missed 3 periods in a row? |  | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| Periods have not started by the age of 15 | Are you 15 or older and your periods have not started yet? |  | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| Too much hair growth (thick, dark hair on the face or body) | Do you have thick, dark hair growing on your face, neck, chest, tummy, lower back, bottom or thighs? | 399939002 | [Excessive hair growth (hirsutism)](https://www.nhs.uk/symptoms/hirsutism/) | |
| Put on weight without meaning to | Have you put on weight over the last few months without meaning to, or are you finding it hard to lose weight? |  | [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Oily skin or acne (spots) | Do you have oily skin or acne (spots)? |  | [Polycystic ovary syndrome](https://www.nhs.uk/conditions/polyendocrine-metabolic-ovarian-syndrome-pmos/) | |
| Irregular periods | Are your periods irregular? For example, the time between them is less than 21 days or more than 35 days, or it keeps changing. | 80182007 | [Irregular periods](https://www.nhs.uk/symptoms/irregular-periods/) | |

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

### `advice_possible_ectopic_emergency`

**What to do:** Call 999 or go to A&E now. These signs could mean an ectopic pregnancy has burst, where a pregnancy growing outside the womb splits open. This needs treatment straight away.

**Look out for:**
- Feeling very dizzy, or passing out
- Looking very pale
- Pain getting worse

**Get more help when:**
- Call 999 for an ambulance if you pass out, feel very faint, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E now. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance.

Source: [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/)

### `advice_possible_ectopic_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment or call NHS 111. Tummy pain or unusual bleeding when you could be pregnant needs checking as soon as possible. It could be an ectopic pregnancy, where a pregnancy grows outside the womb.

**Look out for:**
- A sharp, sudden and very bad pain in your tummy
- Feeling very dizzy or faint, or passing out
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina

**Get more help when:**
- Call 999 or go to A&E straight away if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you are under the care of an early pregnancy unit or maternity unit, you can call them.

**What you can do yourself:**
- Do a pregnancy test if you have not done one, but get help even if it is negative

Source: [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/), [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/)

### `advice_severe_sickness_pregnancy_urgent`

**What to do:** Contact your GP or midwife, or call NHS 111, as soon as possible today. Being sick many times a day and not keeping food or drink down can be severe sickness in pregnancy. You may need treatment to stop you losing too much water from your body.

**Look out for:**
- Peeing less than usual, or dark, strong-smelling pee
- Feeling dizzy or faint
- Blood in your sick
- Tummy pain

**Get more help when:**
- Go to A&E or call 999 if you feel very faint, pass out, or cannot keep any fluids down at all

**Where to go:** Contact your GP or midwife, or call 111 or use 111 online. If you have a maternity unit, you can call them.

**What you can do yourself:**
- Sip fluids little and often
- Do a pregnancy test if you have not done one

Source: [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/)

### `advice_missed_period_gp`

**What to do:** See a GP about your missed or late periods. It is often nothing to worry about, but a GP can check for a cause.

**Look out for:**
- Tummy pain, especially low down on one side
- Bleeding or brown watery discharge from your vagina
- Pain in the tip of your shoulder

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you could be pregnant and have tummy pain or unusual bleeding
- Call 999 or go to A&E if you get sudden, very bad tummy pain, or feel very dizzy or faint

**Where to go:** Ask your GP surgery for an appointment. The source gives no fixed time.

**What you can do yourself:**
- Do a pregnancy test if you could be pregnant
- Keep track of your periods with an app or a diary

Source: [Missed or late periods](https://www.nhs.uk/symptoms/missed-or-late-periods/), [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_mp_heavy_bleeding`: The Miscarriage page says call 999 for heavy bleeding in pregnancy. Applying it to a missed period is AI judgement.
- `rf_mp_pain_or_bleeding`: The Ectopic pregnancy page: a missed period with tummy pain low down on one side, or vaginal bleeding, needs advice right away, even with a negative pregnancy test. The Vaginal bleeding between periods page gives the same advice. Heavy bleeding is included because it is vaginal bleeding too: the 999 rule for it is soft, and this keeps urgent as the floor.
- `rf_mp_pain_peeing_or_pooing`: The Ectopic pregnancy page lists discomfort when peeing or pooing as a symptom in combination with a missed period. Soft, as a urine infection is a more common cause.
- `missed_or_late_periods default outcome`: The page says most of the time it is nothing to worry about, but see a doctor just in case. Not a floor, so a clearly likely harmless cause can lower it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bleeding or period changes caused by hormonal contraception |  | uncommon | Uses hormonal contraception: strongly supports; Started or changed hormonal contraception or HRT in the last 6 months: strongly supports; Bleeding between periods: supports; Irregular periods: supports; Missed or late period: supports |
| Pregnancy | 77386006 | rare | Pregnant, or could be pregnant: strongly supports; Missed or late period: strongly supports; Feels sick or has been sick: supports; Breast pain: supports; Feels very tired: supports; Peeing more often than usual: supports |
| Ectopic pregnancy (a pregnancy growing outside the womb) | 34801009 | very rare | Pain low down on one side of the tummy: strongly supports; Pelvic pain (pain low down in the tummy): strongly supports; Vaginal bleeding between periods or after sex: supports; Missed or late period: supports; Stomach pain in pregnancy: supports; Vaginal bleeding in pregnancy: supports; Pregnant, or could be pregnant: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: supports; Pain in the tip of the shoulder: supports; Feels light-headed: supports; Passed out (fainted): supports; Pain when pooing: supports |
| Raised levels of the hormone prolactin, from a gland problem or a medicine | 237662005 | very rare | Milky nipple discharge: strongly supports; Nipple discharge: strongly supports; Discharge from both nipples: supports; Missed or late period: supports; Irregular periods: supports; Struggling to get pregnant: supports; Change in sight or loss of vision: supports |
| Severe sickness in pregnancy (hyperemesis gravidarum) | 14094001 | rare | Keeps being sick and cannot keep fluids down: strongly supports; Pregnant, or could be pregnant: strongly supports; Feels sick or has been sick: strongly supports; Signs of dehydration: strongly supports; Losing weight without trying: supports; Feels light-headed: supports |
| Perimenopause or menopause (when periods change and then stop) | 289903006 | uncommon | Hot flushes: strongly supports; Trouble sleeping (insomnia): supports; Feeling low, sad or depressed: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports; Feels very tired: supports; Night sweats: supports; Vaginal dryness: supports; Irregular periods: supports; Periods stopped for 12 months or more (the menopause): supports |
| Miscarriage (loss of a pregnancy before 24 weeks) | 17369002 | very rare | Pink, grey or white lumps coming from the vagina: strongly supports; Vaginal bleeding in pregnancy: strongly supports; Stomach pain in pregnancy: supports; Heavy bleeding from the vagina: supports; Vaginal bleeding between periods or after sex: supports; Pelvic pain (pain low down in the tummy): supports; Missed or late period: supports |
| PCOS or PMOS (a hormone condition that affects the ovaries) | 237055002 | common | Too much hair growth (thick, dark hair on the face or body): strongly supports; Irregular periods: strongly supports; Oily skin or acne (spots): supports; Put on weight without meaning to: supports; Struggling to get pregnant: supports; Missed 3 periods in a row: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports |
| Periods not settled yet after starting (puberty) |  | rare | Periods started in the last 2 years: strongly supports; Irregular periods: supports; Missed or late period: supports; Heavy periods: supports |
| Periods changed by stress, weight change or a lot of exercise |  | common | Recent stress, big weight change, or much more exercise: strongly supports; Losing weight without trying: supports; Missed or late period: supports; Irregular periods: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
