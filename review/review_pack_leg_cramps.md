# Review pack: Leg cramps

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
| [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | 2026-11-19 |  | Page last reviewed: 30 April 2026 |
| [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/) | 2026-11-19 |  | Page last reviewed: 01 December 2023 |
| [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |

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

## Leg cramps red flags: Emergency (help now)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cramp_cold_leg`<br>Leg or foot cold, pale, white, blue or grey<br>**Note:** A painful, cold, pale leg can mean the blood supply is suddenly blocked, which needs treatment within hours. AI judgement, needs clinical review. | "Arm, hand, leg or foot cold, pale, blue or grey" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | **AI judgement, needs clinical review** | |
| `rf_cramp_dvt_breathless`<br>Signs of a blood clot in the leg with shortness of breath or chest pain | "One leg swollen, warm and painful, often in the calf" AND ("Short of breath" OR "Chest pain") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |

## Leg cramps red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cramp_dvt`<br>Signs of a blood clot in the leg: one leg swollen, warm and painful, usually in the calf<br>**Note:** Calf pain from a blood clot can be mistaken for cramp. | "One leg swollen, warm and painful, often in the calf" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |

## Leg cramps: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_cramp_gp`<br>Leg cramps that disturb sleep, last longer than 10 minutes, or come with numbness or swelling in the legs | "Pain stopping usual activities or affecting sleep" OR "Cramps lasting more than 10 minutes" OR "Numbness or swelling in the legs as well as cramps" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP* | [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/) | |
| `or_cramp_walking_pain`<br>Pain in the calf, thigh or bottom when walking that goes away after resting<br>**Note:** Can be narrowed arteries in the legs (peripheral arterial disease) rather than cramp. | "Pain comes on with exercise or walking, and goes with rest" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP* | [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | |

## Default outcome

Used when no rule fires.

- **Leg cramps with nothing that needs more help: they are usually harmless**
- Outcome: Self-manageable, Self-care, No appointment needed. *Leg cramps are common and usually harmless*
- Source: [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Leg cramps | Do you get cramp in your leg? Cramp is when a muscle suddenly tightens and hurts. | 449917004 | [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Arm, hand, leg or foot cold, pale, blue or grey | Is your arm, hand, leg or foot on the painful side cold to touch, or has it turned pale, white, blue or grey? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| One leg swollen, warm and painful, often in the calf | Is one of your legs swollen, warm and painful, usually in the calf? The skin may look red or darker, and the veins may look swollen. |  | [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Cramps lasting more than 10 minutes | Do the cramps last longer than 10 minutes? |  | [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/) | |
| Numbness or swelling in the legs as well as cramps | As well as the cramps, do you have numbness or swelling in your legs? |  | [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/) | |
| Pain comes on with exercise or walking, and goes with rest | Does the pain come on when you exercise or walk, and go away after a few minutes of rest? |  | [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/) | |

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

### `advice_limb_blood_supply_emergency`

**What to do:** Call 999 or go to A&E now. A cold, pale, blue or grey arm or leg can mean its blood supply is blocked. It needs treatment within hours.

**Look out for:**
- The arm or leg getting colder or more pale
- Numbness or weakness getting worse
- Pain getting much worse

**Get more help when:**
- Call 999 if you cannot get to A&E quickly

**Where to go:** Go to A&E now, or call 999. Do not drive yourself.

**What you can do yourself:**
- Do not rub the arm or leg or put heat on it
- Take off anything tight, such as rings or a tight bandage

Source: [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/), [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/)

### `advice_dvt_emergency`

**What to do:** Call 999 or go to A&E now. A blood clot in the leg may have moved to your lungs. This can be life-threatening.

**Look out for:**
- Breathing getting harder
- Chest pain getting worse
- Coughing up blood, or feeling faint

**Get more help when:**
- Call 999 if you collapse, or your breathing gets much worse

**Where to go:** Go to A&E now, or call 999. Do not drive yourself. Bring any medicines you take.

Source: [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/)

### `advice_dvt_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A swollen, warm, painful leg can be a blood clot in a vein (DVT). It needs treatment to stop it moving to the lungs.

**Look out for:**
- Feeling short of breath
- Chest pain, especially when breathing in
- Coughing up blood

**Get more help when:**
- Call 999 or go to A&E if you get short of breath or have chest pain

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you are pregnant, you can also call your maternity unit.

**What you can do yourself:**
- Do not rub or massage the leg

Source: [Deep vein thrombosis (DVT)](https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/)

### `advice_leg_cramps_gp`

**What to do:** See a GP. They will look for the cause of your leg cramps or leg pain.

**Look out for:**
- One leg becoming swollen, warm and painful
- Your leg or foot going cold, pale or blue
- Sores on your feet or legs that do not heal

**Get more help when:**
- Get an urgent GP appointment or help from 111 if one leg becomes swollen, warm and painful
- Call 999 or go to A&E if you also feel short of breath or have chest pain

**Where to go:** Contact your GP surgery.

**What you can do yourself:**
- Stretch your calf muscles regularly, especially before bed
- If you smoke, stopping will help the blood flow in your legs

Source: [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/), [Peripheral arterial disease (PAD)](https://www.nhs.uk/conditions/peripheral-arterial-disease-pad/)

### `advice_leg_cramps_self_care`

**What to do:** Leg cramps are common and usually harmless. They can be eased with stretching.

**Look out for:**
- One leg becoming swollen, warm and painful
- Cramps that last longer than 10 minutes
- Numbness or swelling in your legs

**Get more help when:**
- Get an urgent GP appointment or help from 111 if one leg becomes swollen, warm and painful
- See a GP if cramps disturb your sleep, last longer than 10 minutes, or come with numbness or swelling

**Where to go:** You do not need to see anyone now.

**What you can do yourself:**
- During a cramp, stretch and rub the muscle, or stand up and put your weight on that leg
- Stretch your calf muscles against a wall for 5 minutes, 3 times a day, the last time just before bed
- Drink lots of water, most of all when you exercise or it is hot
- Paracetamol or ibuprofen can ease soreness after a cramp

Source: [Leg cramps](https://www.nhs.uk/conditions/leg-cramps/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cramp_cold_leg`: A painful, cold, pale leg can mean the blood supply is suddenly blocked, which needs treatment within hours. AI judgement, needs clinical review.
- `rf_cramp_dvt`: Calf pain from a blood clot can be mistaken for cramp.
- `or_cramp_walking_pain`: Can be narrowed arteries in the legs (peripheral arterial disease) rather than cramp.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A sudden loss of blood supply to an arm or leg |  | rare | Arm, hand, leg or foot cold, pale, blue or grey: strongly supports; Pain started suddenly: supports; Severe pain: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Weakness in one or both legs, or a foot that drags: supports; An arm or leg suddenly cold, pale or blue and painful: strongly supports; Only the fingers, toes, hands or feet are blue or grey: supports; Pain or swelling in one leg: supports |
| Cramp from exercise, heat or not drinking enough |  | common | Cramps during or after exercise, or in hot weather: strongly supports; Signs of dehydration: supports; Started after more activity than usual, or doing the same movement many times: supports |
| Leg cramps with no clear cause (common and harmless) |  | very common | Cramps mostly at night or when resting: strongly supports; Pain stopping usual activities or affecting sleep: supports |
| Cramp caused by a medicine, such as a statin or water tablets |  | uncommon | Takes a statin, or water tablets: strongly supports; Aching body: supports; Cramps mostly at night or when resting: supports |
| Narrowed arteries in the legs, which reduce the blood flow | 840580004 | rare | Pain comes on with exercise or walking, and goes with rest: strongly supports; A wound or sore on the foot or leg that is not healing: supports; Pain worse at night, or not better with rest: supports; Numbness, tingling or pins and needles in the leg or foot: supports |
| Leg cramps in pregnancy |  | rare | Pregnant, or gave birth in the last 6 weeks: strongly supports; Cramps mostly at night or when resting: supports |
| Blood clot in a vein, usually in the leg (deep vein thrombosis, DVT) | 128053003 | uncommon | Pain or swelling in one leg: strongly supports; Swelling is severe, painful or came on suddenly: supports; Swollen area is red or hot to touch: supports; One leg swollen, warm and painful, often in the calf: strongly supports; Swelling of the painful area: supports; Skin over the painful area has changed colour: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
