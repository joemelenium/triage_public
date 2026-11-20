# Review pack: Smelly urine

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
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | 2026-11-19 |  | Page last reviewed: 16 October 2023 |
| [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 10 February 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |

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

## Smelly urine red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_su_drowsy`<br>Smelly pee and very drowsy, hard to wake or finding it hard to speak<br>**Note:** The Smelly urine page says an urgent GP appointment or 111 for feeling confused or agitated. The UTI page says 999 or A&E for confused, drowsy or difficulty speaking. The more urgent is used. Sudden confusion is in the universal red flags. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_su_sepsis_skin`<br>Smelly pee with blotchy skin, or a rash that does not fade when pressed: possible sepsis | "Blotchy or mottled skin" OR "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_su_sepsis_breathing`<br>Breathing very fast, with a high or very low temperature or shivering: possible sepsis<br>**Note:** Requiring a high or very low temperature is AI judgement, so that fast breathing from worry is not sent to A&E on its own. | "Breathing very fast" AND ("Very high temperature, or feels hot, cold or shivery" OR "Very low temperature (below 36C)") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_su_diabetes_emergency`<br>Very thirsty, with being sick, fast deep breathing or fruity-smelling breath: possible diabetic ketoacidosis | "Feeling very thirsty all the time" AND ("Being sick" OR "Breathing faster and more deeply than usual" OR "Breath smells fruity") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Smelly urine red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_su_urgent_signs`<br>Smelly pee with blood in it, lower tummy pain, or pain in the back under the ribs | "Blood in pee" OR "Pain low down in the tummy, below the belly button" OR "Pain in the back or side, just under the ribs" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| `rf_su_unwell_or_temperature`<br>Smelly pee and feeling unwell, a very high or very low temperature, or feeling hot, cold or shivery<br>**Note:** The page says 'you feel tired and unwell'. The existing question about feeling very unwell is used. | "Feels very unwell" OR "Very high temperature, or feels hot, cold or shivery" OR "Very low temperature (below 36C)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| `rf_su_thirsty_weight_loss`<br>Very thirsty, and losing weight or very tired: possible diabetes<br>**Note:** The Type 1 diabetes page says an urgent GP appointment or 111 if you think you have it. The Type 2 diabetes page says see a GP. The more urgent is used, marked soft. The Smelly urine page says type 2 diabetes can cause smelly pee. | "Feeling very thirsty all the time" AND ("Losing weight without trying" OR "Feels very tired") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Smelly urine: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_su_uti_signs`<br>Smelly pee and needing to pee suddenly, more often or at night, pain or burning when peeing, or cloudy pee<br>**Note:** The UTI page sends women aged 16 to 64 who are not pregnant to a pharmacist instead. The pain when peeing entry symptom applies once those signs are reported, with its own rules. | "Peeing more often than usual" OR "Getting up in the night to pee" OR "Pain, burning or stinging when peeing" OR "Cloudy pee" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| `or_su_thirsty`<br>Smelly pee and very thirsty all the time: possible diabetes | "Feeling very thirsty all the time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/) | |

## Default outcome

Used when no rule fires.

- **Smelly pee with nothing else that needs help: drink more and see if it settles**
- Outcome: Self-manageable, Self-care, No appointment needed. *Smelly pee on its own is not usually a cause for concern*
- Source: [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Smelly pee | Does your pee smell stronger or worse than usual? | 278017001 | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Very low temperature (below 36C) | Is your temperature very low, below 36C? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Pain low down in the tummy, below the belly button | Is the pain low down in your tummy, below your belly button? | 54586004 | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Pain in the back or side, just under the ribs | Do you have pain in your back or side, just under the ribs? | 271857006 | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Getting up in the night to pee | Do you get up in the night to pee more than you used to? | 139394000 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Cloudy pee | Is your pee cloudy? | 7766007 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |

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

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

### `advice_diabetes_emergency`

**What to do:** Call 999 or go to A&E now. Being very thirsty with being sick, deep fast breathing or fruity-smelling breath can be signs of diabetic ketoacidosis. This is when a lack of insulin makes the blood harmful, and it can be life-threatening.

**Look out for:**
- Feeling very sleepy or confused
- Tummy pain
- Breathing that is faster and deeper than usual

**Get more help when:**
- Call 999 if the person becomes very sleepy, confused or hard to wake

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_uti_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You may have a urine infection that needs checking today, or an infection that could spread to the kidneys.

**Look out for:**
- A high temperature, or feeling hot, cold or shivery
- Pain in your back or side, just under the ribs
- Feeling or being sick
- Not having a pee all day

**Get more help when:**
- Call 999 or go to A&E if you feel confused, very drowsy or find it hard to speak
- Call 999 or go to A&E if your skin becomes blotchy or very pale. These can be signs of sepsis, a life-threatening reaction to an infection.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Take paracetamol for pain or a high temperature
- Rest and drink enough fluids so that your pee is pale
- Avoid fruit juice, coffee and alcohol, which can irritate the bladder

Source: [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/), [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/), [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/)

### `advice_diabetes_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Peeing more, being very thirsty, tired or losing weight can be signs of diabetes. A quick finger-prick test can check this.

**Look out for:**
- Being sick, or tummy pain
- Breathing faster and more deeply than usual
- Breath that smells fruity, like pear drops
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 or go to A&E if any of these happen, or if symptoms get worse quickly

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Bring a sample of pee if you can.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_smelly_urine_gp`

**What to do:** See a GP. Smelly pee with needing to pee often, pain or cloudy pee can be a urine infection. If you are a woman aged 16 to 64 and not pregnant, a pharmacist can also help.

**Look out for:**
- Blood in your pee
- Pain in your lower tummy, or in your back under the ribs
- A high or very low temperature, or feeling hot, cold or shivery

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if you feel confused, very drowsy or find it hard to speak

**Where to go:** Make an appointment with a GP, or see a pharmacist. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Drink plenty of fluids, especially water

Source: [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/)

### `advice_diabetes_gp`

**What to do:** See a GP. Being very thirsty and peeing more can be signs of diabetes. A blood test can check this.

**Look out for:**
- Losing weight without trying
- Feeling very tired
- Being sick, or breathing faster and more deeply than usual

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you lose weight or feel very tired
- Call 999 or go to A&E if you are being sick, breathing fast and deeply, or feel very sleepy

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

Source: [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/)

### `advice_smelly_urine_self_care`

**What to do:** You can look after this yourself. Smelly pee on its own is not usually a cause for concern. It is often from not drinking enough, or from food, coffee or vitamins.

**Look out for:**
- Pain or burning when you pee, or needing to pee more often
- Cloudy pee or blood in your pee
- A high temperature, or pain in your back or side

**Get more help when:**
- See a GP or pharmacist if you get pain when peeing, need to pee more often, or have cloudy pee
- Ask for an urgent GP appointment or call 111 if you have blood in your pee, a high temperature or back pain

**Where to go:** You do not need an appointment now. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Drink plenty of water, so you pee often and do not feel thirsty
- Drink more in hot weather and when exercising
- Do not eat a lot of garlic or asparagus, or take more than 10mg of vitamin B6 a day

Source: [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_su_drowsy`: The Smelly urine page says an urgent GP appointment or 111 for feeling confused or agitated. The UTI page says 999 or A&E for confused, drowsy or difficulty speaking. The more urgent is used. Sudden confusion is in the universal red flags.
- `rf_su_sepsis_breathing`: Requiring a high or very low temperature is AI judgement, so that fast breathing from worry is not sent to A&E on its own.
- `rf_su_unwell_or_temperature`: The page says 'you feel tired and unwell'. The existing question about feeling very unwell is used.
- `rf_su_thirsty_weight_loss`: The Type 1 diabetes page says an urgent GP appointment or 111 if you think you have it. The Type 2 diabetes page says see a GP. The more urgent is used, marked soft. The Smelly urine page says type 2 diabetes can cause smelly pee.
- `or_su_uti_signs`: The UTI page sends women aged 16 to 64 who are not pregnant to a pharmacist instead. The pain when peeing entry symptom applies once those signs are reported, with its own rules.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Mild dehydration (not having enough water in the body) |  | very common | Diarrhoea, or being sick: strongly supports; Feeling very thirsty all the time: strongly supports; Unwell after being in the heat or exercising hard: supports; Feels light-headed: supports; Signs of dehydration: strongly supports; Making much less pee than usual: supports; Feels sick or has been sick: supports; Feels very tired: supports |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |
| Pee changed for a harmless reason, such as food, a medicine or a period |  | common | Recently had food, drink or medicine that can change pee: strongly supports; Started a new medicine or changed a dose in the last few weeks: supports; On a period, or bleeding from the vagina: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
