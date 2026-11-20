# Review pack: Bad breath

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
| [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | 2026-11-19 |  | Page last reviewed: 20 April 2026 |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | 2026-11-19 |  | Page last reviewed: 05 June 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Dental pain](https://www.nhs.uk/symptoms/toothache/) | 2026-11-19 |  | Page last reviewed: 01 July 2024 |
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

## Bad breath red flags: Emergency (help now)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bb_high_blood_sugar`<br>Breath that smells fruity, with being very thirsty, feeling sick or being sick, or feeling very unwell<br>**Note:** Clinical knowledge: fruity breath with thirst, being sick or feeling very unwell can be a sign of diabetic ketoacidosis, a life-threatening problem caused by very high blood sugar. | "Breath smells fruity" AND (("Feeling very thirsty all the time" AND "Peeing more often than usual") OR "Feels sick or has been sick" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Bad breath red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bb_fruity_breath`<br>Breath that smells fruity, like pear drops<br>**Note:** Clinical knowledge: fruity breath can be an early sign of high blood sugar with ketones. It can also come from dieting or fasting. | "Breath smells fruity" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today. If you have diabetes, check your blood sugar and ketones if you can.* | **AI judgement, needs clinical review** | |
| `rf_bb_gums_very_sore`<br>Very sore and swollen gums, or teeth becoming loose or falling out | "Gums very sore and swollen, or teeth loose or falling out" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| `rf_bb_face_swollen`<br>Bad breath with a swollen face, cheek or jaw | "Swollen face, cheek or jaw" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |

## Bad breath: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bb_few_weeks`<br>Bad breath that has not gone after a few weeks of cleaning the teeth, tongue and gums well | "Bad breath not gone after a few weeks of cleaning teeth well" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | |
| `or_bb_gums`<br>Bad breath with painful, bleeding or swollen gums | "Gums painful, swollen or bleeding" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | |
| `or_bb_toothache`<br>Bad breath with toothache or wobbly adult teeth | "Toothache" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | |

## Default outcome

Used when no rule fires.

- **Bad breath with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Bad breath can usually be treated by keeping your teeth, tongue and mouth clean*
- Source: [Bad breath](https://www.nhs.uk/symptoms/bad-breath/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Bad breath | Do you have bad breath? | 79879001 | [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Gums very sore and swollen, or teeth loose or falling out | Are your gums very sore and swollen, or are teeth becoming loose or falling out? |  | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| Swollen face, cheek or jaw | Is your face, cheek or jaw swollen? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Bad breath not gone after a few weeks of cleaning teeth well | Has your bad breath not gone away after a few weeks of cleaning your teeth, tongue and gums well? |  | [Bad breath](https://www.nhs.uk/symptoms/bad-breath/) | |
| Gums painful, swollen or bleeding | Are your gums painful, swollen or red, or do they bleed when you brush your teeth? |  | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| Toothache | Do you have toothache, or pain in your teeth, gums or jaw? | 27355003 | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |

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

### `advice_dentist_urgent`

**What to do:** Ask for an urgent dentist appointment today. Do not go to a GP, as they cannot give dental treatment.

**Look out for:**
- Swelling spreading to the eye or neck
- Finding it hard to breathe, swallow, speak or open your mouth
- Problems with your eyesight

**Get more help when:**
- Go to A&E or call 999 if you get any of the signs above
- If you cannot get an urgent dentist appointment, call 111 or use 111 online

**Where to go:** Call your dentist. If they are closed, their answerphone may tell you what to do. If you do not have a dentist, call 111 or use 111 online, or find a dentist and ask for an emergency appointment.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Eat soft foods and try not to chew on the sore side
- Rinse your mouth with warm salt water (children should not do this)

Source: [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/), [Dental pain](https://www.nhs.uk/symptoms/toothache/), [Gum disease](https://www.nhs.uk/conditions/gum-disease/)

### `advice_bad_breath_dentist`

**What to do:** See a dentist. Bad breath and sore or bleeding gums are often caused by gum problems or tooth decay, which a dentist can treat.

**Look out for:**
- Very sore and swollen gums, or teeth becoming loose
- A swollen face or jaw, or a throbbing toothache

**Get more help when:**
- Ask for an urgent dentist appointment if you get any of the signs above
- Go to A&E if swelling spreads to your eye or neck, or you find it hard to breathe or swallow

**Where to go:** Make an appointment with a dentist. If you do not have one, find a dentist near you or call 111.

**What you can do yourself:**
- Brush your teeth and gums twice a day for 2 minutes with fluoride toothpaste
- Clean between your teeth with floss or small brushes once a day
- Clean your tongue once a day with a tongue scraper
- Do not smoke

Source: [Bad breath](https://www.nhs.uk/symptoms/bad-breath/), [Gum disease](https://www.nhs.uk/conditions/gum-disease/)

### `advice_bad_breath_self_care`

**What to do:** Bad breath is very common. You can usually treat it yourself by keeping your teeth, tongue and mouth clean.

**Look out for:**
- Bad breath that does not go away after a few weeks of treating it yourself
- Painful, bleeding or swollen gums
- Toothache, or wobbly adult teeth

**Get more help when:**
- See a dentist if you get any of the signs above
- Get help from 111 if your breath smells fruity, like pear drops, especially if you feel very thirsty or unwell

**Where to go:** You do not need an appointment now. Have regular dental check-ups.

**What you can do yourself:**
- Brush your teeth and gums twice a day for 2 minutes with fluoride toothpaste
- Clean between your teeth and clean your tongue once a day
- Use sugar-free mints or gum after strong-smelling food and drinks
- Do not smoke, and do not drink too much alcohol

Source: [Bad breath](https://www.nhs.uk/symptoms/bad-breath/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bb_high_blood_sugar`: Clinical knowledge: fruity breath with thirst, being sick or feeling very unwell can be a sign of diabetic ketoacidosis, a life-threatening problem caused by very high blood sugar.
- `rf_bb_fruity_breath`: Clinical knowledge: fruity breath can be an early sign of high blood sugar with ketones. It can also come from dieting or fasting.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Bad breath from food, smoking or not cleaning the teeth and tongue enough |  | very common | Bad breath after strong-smelling food or drink: strongly supports; Smokes, or has smoked in the past: supports; White patches on the tongue or inside the mouth: supports |
| Dental abscess (a pocket of pus in a tooth or gum) | 299709002 | common | Intense, throbbing tooth or gum pain: strongly supports; Swollen face, cheek or jaw: strongly supports; Toothache: strongly supports; Bad taste in the mouth: supports; Tooth hurts when biting or chewing: supports; Very high temperature, or feels hot, cold or shivery: supports; Swollen glands in the neck: supports; Sharp tooth pain with hot, cold or sweet things: supports |
| Dry socket (pain a few days after a tooth is taken out, when the healing blood clot is lost) | 61804006 | rare | Had a tooth taken out in the last 2 weeks: strongly supports; Intense, throbbing tooth or gum pain: supports; Bad taste in the mouth: supports; Bad breath: supports; Toothache not going away with painkillers: supports |
| Gum infection, with sore, swollen or bleeding gums | 2556008 | common | Gums painful, swollen or bleeding: strongly supports; Bad breath: supports; Bad taste in the mouth: supports; Gums very sore and swollen, or teeth loose or falling out: supports; Metallic taste in the mouth: supports |
| Tonsil stones (small lumps that form on the tonsils at the back of the throat) |  | uncommon | Small white or yellow lumps at the back of the throat: strongly supports; Often gets sore throats: supports; Bad taste in the mouth: supports; Sore throat: supports |
| Tonsillitis (infected tonsils at the back of the throat) | 90176007 | common | Pus-filled spots on the tonsils: supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Often gets sore throats: supports; Lump in the mouth or neck: supports; Swollen glands in the neck: supports; Feels very tired: supports; Cough or runny nose: argues against |
| Tooth decay (a hole in a tooth) | 80967001 | very common | Hole, or white, brown or black spots, on a tooth: strongly supports; Sharp tooth pain with hot, cold or sweet things: strongly supports; Toothache: strongly supports; Toothache for more than 2 days: supports; Bad breath: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
