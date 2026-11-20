# Review pack: Blue or grey skin or lips

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
| [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | 2026-11-19 |  | Page last reviewed: 04 October 2023 |
| [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | 2026-11-19 |  | Page last reviewed: 6 August 2026 |
| [Raynaud's](https://www.nhs.uk/conditions/raynauds/) | 2026-11-19 |  | Page last reviewed: 20 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
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

## Blue or grey skin or lips red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cy_lips_or_face`<br>Blue or grey colour on the lips, tongue or face that came on suddenly | "Lips, tongue or face suddenly turned blue or grey" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| `rf_cy_breathing_or_chest`<br>Blue or grey skin with difficulty breathing or chest pain | "Difficulty breathing" OR "Chest pain" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| `rf_cy_dizzy`<br>Blue or grey skin and feeling dizzy or confused<br>**Note:** Confusion is caught in every session by the universal red flag. | "Feels light-headed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| `rf_cy_cold_painful_limb`<br>An arm or leg suddenly cold, pale or blue, and painful or numb: possible blood clot blocking its blood supply<br>**Note:** Clinical knowledge: a limb that suddenly loses its blood supply needs surgery within hours. The Cyanosis page names a blood clot that stops the blood supply to a limb as a cause, without its own action. | "An arm or leg suddenly cold, pale or blue and painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_cy_child_floppy`<br>A child with blue or grey skin who is floppy, hard to wake or not responding as usual | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_cy_breathless`<br>Blue or grey skin and short of breath<br>**Note:** The page says call 999 for blue or grey skin with difficulty breathing. Mild breathlessness with cold, blue fingers is less clear, so 999 or A&E is used. | "Short of breath" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |

## Blue or grey skin or lips red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cy_fingers_toes`<br>Fingers, toes, hands or feet blue or grey: possible circulation problem<br>**Note:** Soft, so that a typical attack of Raynaud's (fingers white then blue in the cold, then red as they warm up) can be lowered to a routine GP appointment. | "Only the fingers, toes, hands or feet are blue or grey" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |

## Blue or grey skin or lips: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_cy_raynauds_pattern`<br>Fingers or toes turn white or blue in the cold, then red as they warm up | "Fingers or toes turn white or blue in the cold, then red as they warm" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Raynaud's](https://www.nhs.uk/conditions/raynauds/) | |

## Default outcome

Used when no rule fires.

- **Blue or grey skin: get medical help**
- Outcome: Urgent (help today), Urgent care, Today. *Get help from NHS 111*
- Source: [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/)
- **Note:** The page says get medical help immediately for symptoms of cyanosis. Soft, so that a typical Raynaud's attack can be lowered.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Skin, lips, fingers or toes look blue or grey | Has your skin, lips, tongue, fingers or toes turned blue or grey? On brown or black skin this may be easier to see on the palms, soles of the feet, lips, gums or inside the eyelids. | 3415004 | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, tongue or face suddenly turned blue or grey | Has the blue or grey colour come on suddenly on the lips, tongue or face? On brown or black skin this may be easier to see on the lips, gums or inside the eyelids. |  | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| An arm or leg suddenly cold, pale or blue and painful | Has one arm or leg suddenly become cold, pale or blue, and painful or numb? |  | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Only the fingers, toes, hands or feet are blue or grey | Is the blue or grey colour only on the fingers, toes, hands or feet? |  | [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/) | |
| Fingers or toes turn white or blue in the cold, then red as they warm | Do your fingers or toes turn white, then blue, when you are cold or stressed, and then red when they warm up again? |  | [Raynaud's](https://www.nhs.uk/conditions/raynauds/) | |

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

### `advice_cyanosis_999`

**What to do:** Call 999 now. Blue or grey skin or lips with these signs means the body may not be getting enough oxygen or blood, which is a serious problem.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person gets worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/)

### `advice_cyanosis_urgent`

**What to do:** Get help from NHS 111 now. Blue or grey fingers, toes, hands or feet can be a sign of a problem with blood flow.

**Look out for:**
- Blue or grey colour spreading to the lips, tongue or face
- Difficulty breathing or chest pain
- Feeling confused or dizzy
- An arm or leg that is cold, pale and painful

**Get more help when:**
- Call 999 if you get any of the signs above

**Where to go:** Call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Warm up slowly if you have been in the cold
- Take off any tight clothing or jewellery

Source: [Blue or grey skin or lips (cyanosis)](https://www.nhs.uk/symptoms/blue-skin-or-lips-cyanosis/)

### `advice_raynauds_gp`

**What to do:** See a GP. Fingers or toes that change colour in the cold are often caused by Raynaud's, which is usually harmless but should be checked.

**Look out for:**
- Symptoms only on one side of the body
- Joint pain, skin rashes or muscle weakness
- Sores on your fingers or toes that do not heal

**Get more help when:**
- Call 111 if your fingers or toes stay blue or grey, or do not warm up
- Call 999 if your lips or face turn blue or grey, or an arm or leg goes cold, pale and painful

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep your home warm, and wear warm clothes, gloves and socks in cold weather
- Exercise regularly to help your blood flow
- Try to stop smoking

Source: [Raynaud's](https://www.nhs.uk/conditions/raynauds/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cy_dizzy`: Confusion is caught in every session by the universal red flag.
- `rf_cy_cold_painful_limb`: Clinical knowledge: a limb that suddenly loses its blood supply needs surgery within hours. The Cyanosis page names a blood clot that stops the blood supply to a limb as a cause, without its own action.
- `rf_cy_breathless`: The page says call 999 for blue or grey skin with difficulty breathing. Mild breathlessness with cold, blue fingers is less clear, so 999 or A&E is used.
- `rf_cy_fingers_toes`: Soft, so that a typical attack of Raynaud's (fingers white then blue in the cold, then red as they warm up) can be lowered to a routine GP appointment.
- `blue_or_grey_skin default outcome`: The page says get medical help immediately for symptoms of cyanosis. Soft, so that a typical Raynaud's attack can be lowered.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A sudden loss of blood supply to an arm or leg |  | rare | Arm, hand, leg or foot cold, pale, blue or grey: strongly supports; Pain started suddenly: supports; Severe pain: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Weakness in one or both legs, or a foot that drags: supports; An arm or leg suddenly cold, pale or blue and painful: strongly supports; Only the fingers, toes, hands or feet are blue or grey: supports; Pain or swelling in one leg: supports |
| Asthma (a long-term condition that makes the airways narrow), or an asthma attack | 195967001 | uncommon | Wheezing comes and goes, often worse at night or early morning: strongly supports; Wheezing brought on by exercise or cold air: supports; Symptoms come on around pollen, dust, mould or animals: supports; Cough worse at night: supports; Has eczema, hay fever or a food allergy: supports; Chest feels tight or squeezed: supports |
| Bronchiolitis (a chest infection that babies get) | 4120002 | rare | Blocked or runny nose: strongly supports; Cough: supports; Wheezing: supports; Breathing very fast: supports; Baby or young child feeding or eating much less than usual: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Pneumonia (an infection deep in the lungs) | 233604007 | uncommon | Cough: strongly supports; Short of breath: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Chest pain worse when breathing in: supports; Yellow or green phlegm: supports; Aching body: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Heart failure (the heart cannot pump blood as well as it should), or a flare of it | 84114007 | rare | Short of breath: strongly supports; Out of breath doing everyday things: strongly supports; Short of breath when lying flat: strongly supports; Swollen feet, ankles or legs: supports; Suddenly put on weight: supports; Heart failure symptoms worse than usual: supports; Frothy pink phlegm: supports; Cough worse at night: supports; Feels very tired: supports |
| Blood clot in the lung (pulmonary embolism) | 59282003 | rare | Short of breath: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: strongly supports; Chest pain worse when breathing in: strongly supports; Breathing very fast: supports; Heart beating very fast: supports; Pain or swelling in one leg: supports; Coughing up blood: supports; Chest pain is there now: strongly supports |
| Raynaud's (fingers and toes change colour in the cold because of narrowed blood vessels) | 266261006 | common | Fingers or toes turn white or blue in the cold, then red as they warm: strongly supports; Only the fingers, toes, hands or feet are blue or grey: strongly supports; Feeling cold all the time: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
