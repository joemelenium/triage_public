# Review pack: Dry mouth

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
| [Dehydration](https://www.nhs.uk/conditions/dehydration/) | 2026-11-19 |  | Page last reviewed: 01 May 2026 |
| [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | 2026-11-19 |  | Page last reviewed: 29 November 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | 2026-11-19 |  | Page last reviewed: 16 May 2023 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Type 2 diabetes](https://www.nhs.uk/conditions/type-2-diabetes/) | 2026-11-19 |  |  |

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

## Dry mouth red flags: Emergency (help now)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dm_high_blood_sugar`<br>Very thirsty or fruity breath, with feeling sick or being sick, feeling very unwell, or breathing very fast<br>**Note:** Clinical knowledge: these can be signs of diabetic ketoacidosis, a life-threatening problem caused by very high blood sugar. | (("Feeling very thirsty all the time" AND "Peeing more often than usual") OR "Breath smells fruity") AND ("Feels sick or has been sick" OR "Feels very unwell" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Dry mouth red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dm_dehydration`<br>Dry mouth with signs of dehydration, such as peeing less or dark pee | "Signs of dehydration" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| `rf_dm_fruity_breath`<br>Dry mouth with breath that smells fruity, like pear drops<br>**Note:** Clinical knowledge: fruity breath can be an early sign of high blood sugar with ketones. | "Breath smells fruity" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today. If you have diabetes, check your blood sugar and ketones if you can.* | **AI judgement, needs clinical review** | |

## Dry mouth: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_dm_hard_to_eat_or_talk`<br>Dry mouth that makes it hard to talk or eat | "Mouth so dry it is hard to talk or eat" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| `or_dm_few_weeks`<br>Dry mouth not better after a few weeks of home or pharmacy treatment | "Dry mouth not better after a few weeks of self-care" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| `or_dm_mouth_sore_or_patches`<br>Dry mouth with a painful, red, swollen or bleeding mouth, or sore white patches | "Mouth painful, red, swollen or bleeding" OR "White patches on the tongue or inside the mouth" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| `or_dm_taste`<br>Dry mouth with problems with taste that are not going away | "Lost or changed sense of smell or taste" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| `or_dm_medicine`<br>Dry mouth that may be caused by a prescribed medicine | "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Do not stop the medicine without advice.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| `or_dm_other_symptoms`<br>Dry mouth with other symptoms, such as peeing a lot or dry eyes | ("Feeling very thirsty all the time" AND "Peeing more often than usual") OR "Dry eyes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |

## Default outcome

Used when no rule fires.

- **Dry mouth with nothing that needs more help: try things to ease it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *A dry mouth is rarely a sign of anything serious. A pharmacist can help.*
- Source: [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Dry mouth | Does your mouth feel dry a lot of the time? | 87715008 | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Mouth so dry it is hard to talk or eat | Is your mouth so dry that it is hard to talk or eat, or are you struggling to eat regularly? |  | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| Dry mouth not better after a few weeks of self-care | Is your mouth still dry after trying home or pharmacy treatments for a few weeks? |  | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| Mouth painful, red, swollen or bleeding | Is your mouth painful, red, swollen or bleeding? |  | [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/) | |
| White patches on the tongue or inside the mouth | Do you have white patches on your tongue or inside your mouth? |  | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| Lost or changed sense of smell or taste | Have you lost your sense of smell or taste, or has it changed? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Dry eyes | Do your eyes feel dry? | 162290004 | [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | |

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

### `advice_high_blood_sugar_ae`

**What to do:** Go to A&E now, or call 999. These can be signs of very high blood sugar with ketones (diabetic ketoacidosis, caused by a lack of insulin), which needs treatment in hospital.

**Look out for:**
- Breathing that is very fast or deep
- Feeling confused or very sleepy
- Being sick, or tummy pain

**Get more help when:**
- Call 999 if the person is confused, very sleepy or passes out

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- If you have diabetes, keep taking your insulin and check your blood sugar and ketones if you can

Source: **AI judgement, needs clinical review**, [Type 2 diabetes](https://www.nhs.uk/conditions/type-2-diabetes/)

### `advice_dehydration_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. These can be signs of serious dehydration (not having enough water in the body) that needs treatment.

**Look out for:**
- Skin, lips or tongue turning blue, grey, pale or blotchy
- Skin that feels cold, or lots of quick breaths
- Becoming confused, or sleepier than usual or hard to wake
- Feeling dizzy when you stand up, and it does not go away
- Breathing quickly, or a fast heartbeat

**Get more help when:**
- Call 999 or go to A&E if your skin, lips or tongue turn blue, grey or blotchy. Do the same if you feel cold, confused or hard to wake.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 if you need advice for a child under 5. In an emergency call 999.

**What you can do yourself:**
- Keep drinking. If you feel sick, start with small sips and slowly drink more.
- A pharmacist can suggest rehydration drinks. These put back the sugar and salts you have lost.
- Keep breastfeeding or giving formula to a baby, in small amounts more often. Do not make formula weaker.

Source: [Dehydration](https://www.nhs.uk/conditions/dehydration/)

### `advice_possible_high_blood_sugar_urgent`

**What to do:** Get help from NHS 111 today. Breath that smells fruity can be a sign of high blood sugar. If you have diabetes, check your blood sugar and ketones if you can.

**Look out for:**
- Feeling very thirsty and peeing a lot
- Being sick, or tummy pain
- Breathing very fast, or feeling confused or very sleepy

**Get more help when:**
- Go to A&E or call 999 if you get any of the last two signs above

**Where to go:** Call 111 or use 111 online today. If you have diabetes, follow the advice from your diabetes team.

**What you can do yourself:**
- Drink plenty of water
- Do not stop taking any diabetes medicine or insulin

Source: **AI judgement, needs clinical review**, [Type 2 diabetes](https://www.nhs.uk/conditions/type-2-diabetes/)

### `advice_dry_mouth_gp`

**What to do:** See a GP. They can check what is causing your dry mouth and suggest treatment. Do not stop a prescribed medicine without getting advice first.

**Look out for:**
- Feeling very thirsty and peeing a lot, mainly if you also feel sick or very unwell
- Peeing less than usual, or dark pee
- Sore white patches, or a painful, red, swollen or bleeding mouth

**Get more help when:**
- Get help from 111 today if you are peeing less than usual or your breath smells fruity
- Go to A&E if you are very thirsty and also being sick, breathing fast or feeling very unwell

**Where to go:** Make an appointment with a GP. A pharmacist can suggest gels, sprays or lozenges while you wait.

**What you can do yourself:**
- Sip cold water often, and keep water by your bed at night
- Chew sugar-free gum or suck sugar-free sweets
- Brush your teeth twice a day, as a dry mouth makes tooth decay more likely
- Do not drink lots of alcohol, caffeine or fizzy drinks, and do not smoke

Source: [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/)

### `advice_dry_mouth_self_care`

**What to do:** A dry mouth is rarely a sign of anything serious. There are things you can do to ease it yourself. A pharmacist can help.

**Look out for:**
- A dry mouth that makes it hard to talk or eat
- A mouth that is still dry after a few weeks of trying things to help
- Sore white patches, or a painful, red, swollen or bleeding mouth
- Needing to pee a lot, or dry eyes

**Get more help when:**
- See a GP if you get any of the signs above, or think a medicine is causing it
- Get help from 111 today if you are peeing less than usual or have dark pee

**Where to go:** You do not need an appointment now. A pharmacist can suggest gels, sprays or lozenges.

**What you can do yourself:**
- Sip cold water often, and keep water by your bed at night
- Suck ice cubes, or chew sugar-free gum
- Use lip balm if your lips are dry too
- Do not drink lots of alcohol, caffeine or fizzy drinks, and do not smoke

Source: [Dry mouth](https://www.nhs.uk/symptoms/dry-mouth/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_dm_high_blood_sugar`: Clinical knowledge: these can be signs of diabetic ketoacidosis, a life-threatening problem caused by very high blood sugar.
- `rf_dm_fruity_breath`: Clinical knowledge: fruity breath can be an early sign of high blood sugar with ketones.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Dry mouth from breathing through the mouth, for example because of a blocked nose | 77329001 | common | Breathes through the mouth, or sleeps with the mouth open: strongly supports; Blocked or runny nose: supports; Snoring: supports |
| Mouth thrush (a fungal infection that causes white patches in the mouth) | 79740000 | common | White patches that wipe off, leaving red spots: strongly supports; White patches on the tongue or inside the mouth: strongly supports; Sore cracks at the corners of the mouth: supports; Mouth painful, red, swollen or bleeding: supports; Bad taste in the mouth: supports; Dry mouth: supports |
| A stone or infection in a spit gland (salivary gland) | 28826002 | uncommon | Swelling under the jaw or tongue that gets worse when eating: strongly supports; Dry mouth: supports; Bad taste in the mouth: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Sjogren's syndrome (a condition that causes dry eyes and a dry mouth) | 83901003 | rare | Dry eyes: strongly supports; Dry mouth not better after a few weeks of self-care: supports; Feels very tired: supports; Aching body: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Mild dehydration (not having enough water in the body) |  | very common | Diarrhoea, or being sick: strongly supports; Feeling very thirsty all the time: strongly supports; Unwell after being in the heat or exercising hard: supports; Feels light-headed: supports; Signs of dehydration: strongly supports; Making much less pee than usual: supports; Feels sick or has been sick: supports; Feels very tired: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
