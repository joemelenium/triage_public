# Review pack: Toothache

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
| [Dental pain](https://www.nhs.uk/symptoms/toothache/) | 2026-11-19 |  | Page last reviewed: 01 July 2024 |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Knocked-out tooth](https://www.nhs.uk/conditions/knocked-out-tooth/) | 2026-11-19 |  | Page last reviewed: 06 February 2025 |
| [Wisdom tooth removal](https://www.nhs.uk/tests-and-treatments/wisdom-tooth-removal/) | 2026-11-19 |  | Page last reviewed: 12 June 2024 |
| [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | 2026-11-19 |  | Page last reviewed: 20 April 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |

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

## Toothache red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_th_heart_signs`<br>Jaw or tooth pain that comes on with activity, or with a tight chest, sweating or feeling sick<br>**Note:** Clinical knowledge: pain from the heart can be felt in the jaw or teeth. The Heart attack and Chest pain pages say call 999 for pain that spreads to the jaw with feeling sweaty, sick or short of breath. | "Jaw or tooth pain that comes on with activity, or with chest tightness, sweating or feeling sick" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_th_eye_or_neck_swelling`<br>Toothache with swelling around the eye or in the neck | "Swelling, redness or pain around the eye" OR "Swelling in the neck or under the tongue, or a lot of swelling in the mouth" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| `rf_th_breathe_swallow_speak`<br>Toothache and finding it hard to breathe, swallow or speak<br>**Note:** The Toothache page says go to A&E if swelling in the mouth or neck makes it hard to breathe, swallow or speak. The Dental abscess page says call 999 or go to A&E for any of these. | "Difficulty breathing" OR "Problems swallowing" OR "Difficulty speaking" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_th_vision`<br>Toothache with sudden problems with eyesight | "Sight changed suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_th_opening_mouth`<br>Toothache and finding it hard to open the mouth<br>**Note:** Source difference: the Dental abscess page says call 999 or go to A&E if you are finding it hard to open your mouth. The jaw joint (TMD) page says an urgent GP appointment or 111 for difficulty opening the mouth fully. The more urgent is used, marked soft. | "Difficulty opening the mouth" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |

## Toothache red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_th_face_swollen`<br>Toothache with a swollen face, cheek or jaw<br>**Note:** Source difference: the Toothache page says see a dentist (not urgent) if your cheek or jaw is swollen. The Dental abscess page says ask for an urgent dentist appointment if you think you have an abscess. The more urgent is used, marked soft. | "Swollen face, cheek or jaw" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_th_high_temperature`<br>Toothache with a high temperature<br>**Note:** Source difference: the Toothache page says see a dentist (not urgent) for toothache with a high temperature. The Dental abscess page lists a high temperature as a sign of an abscess, which needs an urgent dentist appointment. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_th_throbbing`<br>Intense, throbbing toothache that keeps you awake<br>**Note:** AI reading of the Dental abscess page, which lists intense toothache as the main sign of an abscess and says ask for an urgent dentist appointment if you think you have one. | "Intense, throbbing tooth or gum pain" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_th_knocked_out`<br>An adult tooth has been knocked out | "Adult tooth knocked out" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an emergency dentist appointment as soon as possible. If you cannot get one, call 111.* | [Knocked-out tooth](https://www.nhs.uk/conditions/knocked-out-tooth/) | |
| `rf_th_bleeding_after_tooth_out`<br>Bleeding that does not stop where a tooth was taken out | "Had a tooth taken out in the last 2 weeks" AND "Bleeding that will not stop where a tooth was taken out" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment, or get help from NHS 111* | [Wisdom tooth removal](https://www.nhs.uk/tests-and-treatments/wisdom-tooth-removal/) | |
| `rf_th_gums_very_sore`<br>Very sore and swollen gums, or teeth becoming loose or falling out | "Gums very sore and swollen, or teeth loose or falling out" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment. If you cannot get one, call 111.* | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| `rf_th_feels_unwell`<br>Toothache and feeling very unwell<br>**Note:** The Wisdom tooth removal page says ask for an urgent dentist appointment or get help from 111 for pain with a high temperature or feeling unwell. | "Feels very unwell" | Urgent (help today)<br>Dentist<br>Today<br>*Ask for an urgent dentist appointment, or get help from NHS 111* | [Wisdom tooth removal](https://www.nhs.uk/tests-and-treatments/wisdom-tooth-removal/) | |

## Toothache: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_th_over_2_days`<br>Toothache that lasts more than 2 days | "Toothache for more than 2 days" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| `or_th_painkillers`<br>Toothache that does not go away with painkillers | "Toothache not going away with painkillers" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| `or_th_biting_gums_taste`<br>Toothache with pain when biting, red gums, or a bad taste in the mouth | "Tooth hurts when biting or chewing" OR "Gums painful, swollen or bleeding" OR "Bad taste in the mouth" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| `or_th_broken_tooth`<br>A cracked or broken tooth, or a filling that has come out<br>**Note:** The Toothache page lists a cracked tooth or a loose or broken filling as a cause of toothache. Seeing a dentist for it is an AI reading. | "Tooth cracked or broken, or a filling has come out" | Routine (help needed, timing not critical)<br>Dentist<br>No fixed time given in the source<br>*See a dentist. The source gives no fixed time.* | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |

## Default outcome

Used when no rule fires.

- **Toothache for 2 days or less with nothing that needs more help: ease it while you wait**
- Outcome: Self-manageable, Self-care, No appointment needed. *Ease the pain yourself. See a dentist if it lasts more than 2 days.*
- Source: [Dental pain](https://www.nhs.uk/symptoms/toothache/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Toothache | Do you have toothache, or pain in your teeth, gums or jaw? | 27355003 | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Jaw or tooth pain that comes on with activity, or with chest tightness, sweating or feeling sick | Does the pain in your jaw or teeth come on when you are active, or with a tight chest, sweating or feeling sick? |  | **AI judgement, needs clinical review** | |
| Swelling, redness or pain around the eye | Is the skin around your eye swollen, red or painful, or is your eyelid swelling shut? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Swelling in the neck or under the tongue, or a lot of swelling in the mouth | Is there swelling in your neck or under your tongue, or a lot of swelling inside your mouth? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Sight changed suddenly | Did the change in your sight come on suddenly, over seconds, minutes or hours? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Difficulty opening the mouth | Are you finding it hard to open your mouth? | 87866006 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Swollen face, cheek or jaw | Is your face, cheek or jaw swollen? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Intense, throbbing tooth or gum pain | Is it an intense, throbbing pain that keeps you awake? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Adult tooth knocked out | Has an adult tooth been knocked out? |  | [Knocked-out tooth](https://www.nhs.uk/conditions/knocked-out-tooth/) | |
| Had a tooth taken out in the last 2 weeks | Have you had a tooth taken out in the last 2 weeks? |  | [Wisdom tooth removal](https://www.nhs.uk/tests-and-treatments/wisdom-tooth-removal/) | |
| Bleeding that will not stop where a tooth was taken out | Is the place where the tooth was taken out still bleeding, and it will not stop? |  | [Wisdom tooth removal](https://www.nhs.uk/tests-and-treatments/wisdom-tooth-removal/) | |
| Gums very sore and swollen, or teeth loose or falling out | Are your gums very sore and swollen, or are teeth becoming loose or falling out? |  | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Toothache for more than 2 days | Have you had the toothache for more than 2 days? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Toothache not going away with painkillers | Is the pain not going away when you take painkillers? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Tooth hurts when biting or chewing | Does it hurt when you bite or chew? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Gums painful, swollen or bleeding | Are your gums painful, swollen or red, or do they bleed when you brush your teeth? |  | [Gum disease](https://www.nhs.uk/conditions/gum-disease/) | |
| Bad taste in the mouth | Do you have a bad or unpleasant taste in your mouth? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |
| Tooth cracked or broken, or a filling has come out | Is a tooth cracked, chipped or broken, or has a filling come out? |  | [Dental pain](https://www.nhs.uk/symptoms/toothache/) | |

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

### `advice_chest_pain_999`

**What to do:** Call 999 now. You could be having a heart attack and need treatment in hospital straight away.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- If you think you or someone else is having a heart attack, do these things while you wait for help.
- Sit and rest on the floor with your knees bent and your back supported. If you cannot do this, sit on a chair.
- Take aspirin (300mg) if you have any. Do not give aspirin to someone who has an aspirin allergy.
- If you have angina (chest pain caused by narrowed blood vessels to the heart), use your spray if you have it with you. It goes under your tongue. It may be called glyceryl trinitrate or GTN.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Angina](https://www.nhs.uk/conditions/angina/)

### `advice_toothache_ae`

**What to do:** Go to A&E now, or call 999. An infection from a tooth may be spreading. Swelling in the mouth or neck can make it hard to breathe.

**Look out for:**
- Swelling that is spreading to the eye or neck
- Finding it harder to breathe, swallow or speak
- Problems with your eyesight

**Get more help when:**
- Call 999 if breathing gets harder or you cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Dental pain](https://www.nhs.uk/symptoms/toothache/), [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/)

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

### `advice_knocked_out_tooth`

**What to do:** Ask for an emergency dentist appointment as soon as you can. Do this even if you cannot find the tooth.

**Look out for:**
- Bleeding that will not stop
- A head injury, such as feeling sick, sleepy or confused
- Swelling that makes it hard to breathe or swallow

**Get more help when:**
- Go to A&E if you hit your head or the bleeding will not stop
- If you cannot get an emergency dentist appointment, call 111

**Where to go:** Call your dentist. If they are closed, their answerphone may tell you what to do. If you do not have a dentist, call 111 or find a dentist and ask for an emergency appointment.

**What you can do yourself:**
- Hold the tooth by the top part, not the root, and rinse it briefly in milk or water if it is dirty
- Push an adult tooth gently back into place and bite on a clean cloth to hold it
- If you cannot put it back, keep it in milk or spit. Do not put a baby tooth back in.

Source: [Knocked-out tooth](https://www.nhs.uk/conditions/knocked-out-tooth/)

### `advice_toothache_dentist`

**What to do:** See a dentist. They can treat the cause of the pain and stop it getting worse. Do not go to a GP, as they cannot give dental treatment.

**Look out for:**
- Your face, cheek or jaw becoming swollen
- A high temperature, or an intense, throbbing pain
- Swelling around the eye or in the neck, or finding it hard to breathe, swallow or speak

**Get more help when:**
- Ask for an urgent dentist appointment if your face swells or you get a high temperature
- Go to A&E if swelling spreads to your eye or neck, or you find it hard to breathe, swallow or speak

**Where to go:** Make an appointment with a dentist. If you do not have one, call 111 or find a dentist near you.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Use a pain-relieving gel for your mouth
- Eat soft foods and avoid foods that are sweet, very hot or very cold
- Use a soft toothbrush and do not floss around the sore tooth

Source: [Dental pain](https://www.nhs.uk/symptoms/toothache/)

### `advice_toothache_self_care`

**What to do:** There are things you can do to ease toothache. See a dentist if it lasts more than 2 days.

**Look out for:**
- Toothache lasting more than 2 days, or not helped by painkillers
- A high temperature, pain when you bite, red gums or a bad taste in your mouth
- Your cheek or jaw becoming swollen

**Get more help when:**
- See a dentist if you get any of the first two signs above
- Ask for an urgent dentist appointment if your face or jaw swells
- Go to A&E if swelling spreads to your eye or neck, or you find it hard to breathe, swallow or speak

**Where to go:** You do not need an appointment yet. A pharmacist can advise on painkillers. If you need a dentist and do not have one, call 111.

**What you can do yourself:**
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.
- Use a pain-relieving gel for your mouth
- Rinse your mouth with warm salt water (children should not do this)
- Eat soft foods, and avoid foods that are sweet, very hot or very cold
- Do not smoke

Source: [Dental pain](https://www.nhs.uk/symptoms/toothache/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_th_heart_signs`: Clinical knowledge: pain from the heart can be felt in the jaw or teeth. The Heart attack and Chest pain pages say call 999 for pain that spreads to the jaw with feeling sweaty, sick or short of breath.
- `rf_th_breathe_swallow_speak`: The Toothache page says go to A&E if swelling in the mouth or neck makes it hard to breathe, swallow or speak. The Dental abscess page says call 999 or go to A&E for any of these.
- `rf_th_opening_mouth`: Source difference: the Dental abscess page says call 999 or go to A&E if you are finding it hard to open your mouth. The jaw joint (TMD) page says an urgent GP appointment or 111 for difficulty opening the mouth fully. The more urgent is used, marked soft.
- `rf_th_face_swollen`: Source difference: the Toothache page says see a dentist (not urgent) if your cheek or jaw is swollen. The Dental abscess page says ask for an urgent dentist appointment if you think you have an abscess. The more urgent is used, marked soft.
- `rf_th_high_temperature`: Source difference: the Toothache page says see a dentist (not urgent) for toothache with a high temperature. The Dental abscess page lists a high temperature as a sign of an abscess, which needs an urgent dentist appointment.
- `rf_th_throbbing`: AI reading of the Dental abscess page, which lists intense toothache as the main sign of an abscess and says ask for an urgent dentist appointment if you think you have one.
- `rf_th_feels_unwell`: The Wisdom tooth removal page says ask for an urgent dentist appointment or get help from 111 for pain with a high temperature or feeling unwell.
- `or_th_broken_tooth`: The Toothache page lists a cracked tooth or a loose or broken filling as a cause of toothache. Seeing a dentist for it is an AI reading.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Teeth grinding linked to stress or sleep | 191983006 | common | Feeling anxious, worried or panicky: strongly supports; Teeth grinding or jaw clenching: strongly supports; Teeth worn down, chipped or more sensitive than before: supports; Jaw aching, clicking, popping or locking: supports; Drinks a lot of alcohol: supports |
| Cracked or broken tooth, or a lost filling | 109747007 | common | Tooth cracked or broken, or a filling has come out: strongly supports; Tooth hurts when biting or chewing: strongly supports; Sharp tooth pain with hot, cold or sweet things: supports; Teeth grinding or jaw clenching: supports |
| Dental abscess (a pocket of pus in a tooth or gum) | 299709002 | common | Intense, throbbing tooth or gum pain: strongly supports; Swollen face, cheek or jaw: strongly supports; Toothache: strongly supports; Bad taste in the mouth: supports; Tooth hurts when biting or chewing: supports; Very high temperature, or feels hot, cold or shivery: supports; Swollen glands in the neck: supports; Sharp tooth pain with hot, cold or sweet things: supports |
| Dry socket (pain a few days after a tooth is taken out, when the healing blood clot is lost) | 61804006 | rare | Had a tooth taken out in the last 2 weeks: strongly supports; Intense, throbbing tooth or gum pain: supports; Bad taste in the mouth: supports; Bad breath: supports; Toothache not going away with painkillers: supports |
| Gum infection, with sore, swollen or bleeding gums | 2556008 | common | Gums painful, swollen or bleeding: strongly supports; Bad breath: supports; Bad taste in the mouth: supports; Gums very sore and swollen, or teeth loose or falling out: supports; Metallic taste in the mouth: supports |
| Jaw joint problem (pain and clicking in the joint just in front of the ear) |  | uncommon | Jaw aching, clicking, popping or locking: strongly supports; Teeth grinding or jaw clenching: supports; Feeling anxious, worried or panicky: supports; Jaw locking, or too painful to eat or drink: supports; Earache: supports |
| Sensitive teeth (a short, sharp pain from hot, cold or sweet things) | 13468005 | common | Sharp tooth pain with hot, cold or sweet things: strongly supports; Teeth worn down, chipped or more sensitive than before: supports; Teeth grinding or jaw clenching: supports; Gums painful, swollen or bleeding: supports |
| A serious infection spreading from a tooth into the face or neck |  | rare | Swelling in the neck or under the tongue, or a lot of swelling in the mouth: strongly supports; Swollen face, cheek or jaw: strongly supports; Swelling, redness or pain around the eye: supports; Difficulty opening the mouth: supports; Very high temperature, or feels hot, cold or shivery: supports; Problems swallowing: supports; Difficulty breathing: supports |
| Teething (a baby's tooth coming through) | 8004003 | rare | Signs of teething in a baby or young child: strongly supports; Young child rubbing or pulling their ear: supports; Young child irritable, restless or off their food: supports; Gums painful, swollen or bleeding: supports |
| Tooth decay (a hole in a tooth) | 80967001 | very common | Hole, or white, brown or black spots, on a tooth: strongly supports; Sharp tooth pain with hot, cold or sweet things: strongly supports; Toothache: strongly supports; Toothache for more than 2 days: supports; Bad breath: supports |
| Infection around a wisdom tooth that is coming through | 22240003 | uncommon | Pain at the very back of the mouth, where a wisdom tooth is coming through: strongly supports; Bad taste in the mouth: supports; Difficulty opening the mouth: supports; Gums painful, swollen or bleeding: supports; Swollen glands in the neck: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
