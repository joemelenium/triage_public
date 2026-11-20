# Review pack: Weakness or paralysis

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
| [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | 2026-11-19 |  | Page last reviewed: 17 July 2023 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | 2026-11-19 |  | Page last reviewed: 12 August 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | 2026-11-19 |  | Page last reviewed: 04 July 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | 2026-11-19 |  | Page last reviewed: 04 January 2024 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |

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

## Weakness or paralysis red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wk_sudden`<br>Weakness or paralysis that happened suddenly | "Weakness that came on suddenly" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_wk_one_side`<br>Weakness that affects one side of the face or body, or one arm<br>**Note:** The Bell's palsy page also says call 999 for a face drooping on one side, because it can be a stroke. | "Weakness on one side of the face or body" OR "One side of the face weak or drooping" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_wk_after_injury`<br>Weakness or paralysis after an injury to the head, neck or back | "Weakness after an injury to the head, neck or back" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999. Do not move the person if they have hurt their neck or back, unless they are in danger.* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_wk_speech_breathing_swallowing`<br>Weakness that causes problems with speech, breathing or swallowing | "Difficulty speaking" OR "Difficulty breathing" OR "Unable to swallow" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_wk_numb_and_tingling`<br>Weakness, and cannot feel part of the face or body, with tingling<br>**Note:** Taken from the Paralysis page. Marked soft because numbness and tingling with weakness that has come on slowly, for example from nerve damage in diabetes or multiple sclerosis, is common and is sent to a GP by the same page. Sudden weakness is sent to 999 by a firm rule above. | "Numbness or tingling in the face" OR "Pins and needles, tingling or numbness" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_wk_headache_sudden`<br>Weakness with a headache that came on suddenly and is extremely painful | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_wk_legs_bladder_bowel`<br>Numbness or weakness in both legs with problems controlling pee or poo, or numbness around the bottom<br>**Note:** Clinical knowledge: these are signs of pressure on the spinal cord or on the nerves at the bottom of the spine (cauda equina syndrome), which needs an emergency operation. The NHS page for cauda equina syndrome belongs to the bones, joints and muscles batch. | "Numbness or weakness in both legs" AND ("New problems peeing or pooing" OR "Numb or no feeling around the genitals or bottom") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_wk_spreading_ae`<br>Tingling or weakness that started in the feet or hands and is spreading up the body: possible Guillain-Barre syndrome<br>**Note:** Source difference: the Guillain-Barre syndrome page says an urgent GP appointment or 111 if you think you have it. A&E is AI judgement because the weakness can spread to the breathing muscles within hours. Soft, with the urgent rule below as its floor. | "Tingling or weakness starting in the feet or hands and spreading over days" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |

## Weakness or paralysis red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wk_spreading`<br>Tingling or weakness spreading up from the feet or hands | "Tingling or weakness starting in the feet or hands and spreading over days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | |

## Weakness or paralysis: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_wk_gradual`<br>Weakness that started gradually or is getting slowly worse | "Weakness that started gradually or is slowly getting worse" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `or_wk_comes_and_goes`<br>Weakness that comes and goes | "Weakness that comes and goes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |

## Default outcome

Used when no rule fires.

- **Weakness with nothing that needs more urgent help: see a GP to find the cause**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Paralysis](https://www.nhs.uk/symptoms/paralysis/)
- **Note:** The page sends weakness that started gradually, is getting worse or comes and goes to a GP, and sudden weakness to 999. A GP as the floor for everyone with weakness is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Weakness, or cannot move part of the body (paralysis) | Do you have weakness in your face or body, or are you unable to move part of your body? | 44695005 | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Weakness that came on suddenly | Did the weakness come on suddenly, over minutes or hours? |  | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Weakness on one side of the face or body | Is the weakness on one side of your body, or one side of your face? |  | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| One side of the face weak or drooping | Is one side of your face weak or drooping? For example, your eye will not close or the corner of your mouth droops. | 95666008 | [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | |
| Weakness after an injury to the head, neck or back | Did the weakness start after an injury to your head, neck or back? |  | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Numbness or tingling in the face | Is part of your face numb or tingling, or does it have less feeling than usual? | 309557009 | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Pins and needles, tingling or numbness | Do you have pins and needles, tingling or numbness in part of your body, such as your hands, arms, legs or feet? | 62507009 | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| New problems peeing or pooing | Have you had new problems peeing or pooing? For example, finding it hard to start peeing, not being able to pee, or peeing or pooing yourself. |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Tingling or weakness starting in the feet or hands and spreading over days | Did tingling or weakness start in your feet or hands, and has it spread up your arms or legs over hours or days? |  | [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | |
| Weakness that started gradually or is slowly getting worse | Did the weakness start gradually, or has it been slowly getting worse over weeks or months? |  | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Weakness that comes and goes | Does the weakness come and go? |  | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |

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

### `advice_weakness_999`

**What to do:** Call 999 now. This could be a sign of something serious, such as a stroke or an injury to the spine, that needs treatment in hospital straight away.

**Look out for:**
- Difficulty breathing or swallowing
- Weakness spreading, or getting worse

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. If the person has hurt their neck or back, do not move them unless they are in danger.

Source: [Paralysis](https://www.nhs.uk/symptoms/paralysis/)

### `advice_headache_999`

**What to do:** Call 999 now. A sudden, extremely painful headache can be a sign of bleeding on the brain. This needs treatment in hospital straight away.

**Look out for:**
- The person becoming drowsy, confused or hard to wake
- A seizure (fit)
- One side of the face drooping, weakness in an arm, or slurred speech

**Get more help when:**
- Call 999 again if the person gets worse before help arrives
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Migraine](https://www.nhs.uk/conditions/migraine/)

### `advice_weakness_ae`

**What to do:** Go to A&E now, or call 999. These symptoms need to be checked in hospital today.

**Look out for:**
- Difficulty breathing or swallowing
- Weakness spreading up your body, or getting worse
- Not being able to pee

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive yourself. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/), [Paralysis](https://www.nhs.uk/symptoms/paralysis/)

### `advice_weakness_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Weakness or tingling that is spreading needs to be checked today.

**Look out for:**
- Difficulty breathing or swallowing
- A drooping face, or trouble speaking
- Weakness spreading quickly, or not being able to walk

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/)

### `advice_weakness_gp`

**What to do:** See a GP about the weakness. They can find out what is causing it and what treatment may help.

**Look out for:**
- Weakness that comes on suddenly
- Weakness on one side of your face or body, or trouble speaking
- Difficulty breathing or swallowing

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if it is getting worse quickly
- Call 999 if you get any of the signs above

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

Source: [Paralysis](https://www.nhs.uk/symptoms/paralysis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_wk_one_side`: The Bell's palsy page also says call 999 for a face drooping on one side, because it can be a stroke.
- `rf_wk_numb_and_tingling`: Taken from the Paralysis page. Marked soft because numbness and tingling with weakness that has come on slowly, for example from nerve damage in diabetes or multiple sclerosis, is common and is sent to a GP by the same page. Sudden weakness is sent to 999 by a firm rule above.
- `rf_wk_legs_bladder_bowel`: Clinical knowledge: these are signs of pressure on the spinal cord or on the nerves at the bottom of the spine (cauda equina syndrome), which needs an emergency operation. The NHS page for cauda equina syndrome belongs to the bones, joints and muscles batch.
- `rf_wk_spreading_ae`: Source difference: the Guillain-Barre syndrome page says an urgent GP appointment or 111 if you think you have it. A&E is AI judgement because the weakness can spread to the breathing muscles within hours. Soft, with the urgent rule below as its floor.
- `weakness_or_paralysis default outcome`: The page sends weakness that started gradually, is getting worse or comes and goes to a GP, and sudden weakness to 999. A GP as the floor for everyone with weakness is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bell's palsy (weakness on one side of the face) | 193093009 | uncommon | One side of the face weak or drooping: strongly supports; Pain behind the ear, or a change in taste, with face weakness: strongly supports; Signs of a stroke: supports; Weakness on one side of the face or body: supports; Numbness or tingling in the face: supports |
| Brain tumour warning signs | 126952004 | rare | Headache getting worse over days or weeks: strongly supports; Headache wakes them at night, or is worst on waking: supports; Changes in personality or behaviour: supports; Being sick: supports; Has had a seizure (fit): supports; Weakness that started gradually or is slowly getting worse: supports; Headache feels different from usual headaches: supports; Change in sight or loss of vision: supports |
| Guillain-Barre syndrome (a rare condition that attacks the nerves) | 40956001 | rare | Tingling or weakness starting in the feet or hands and spreading over days: strongly supports; Tingling or numbness in both feet or both hands that came on slowly: supports; Finding it hard to balance or walk: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Difficulty breathing: supports; Unable to swallow: supports; Burning, stabbing or shooting pains in the feet or hands: supports |
| Motor neurone condition (MND) warning signs | 37340000 | rare | The twitching area feels weak or stiff: strongly supports; Weakness that started gradually or is slowly getting worse: strongly supports; Twitching in more than one place: supports; Twitch lasting more than 2 weeks: supports |
| Multiple sclerosis (MS) warning signs | 24700007 | rare | Tingling or numbness in different parts of the body at different times: strongly supports; Change in sight or loss of vision: supports; Weakness that comes and goes: supports; Feels very tired: supports; Finding it hard to balance or walk: supports; Numbness or tingling in the face: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Mini-stroke (transient ischaemic attack, TIA) | 266257000 | rare | Signs of a stroke: strongly supports; Weakness that comes and goes: strongly supports; Weakness that came on suddenly: supports; Weakness on one side of the face or body: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Difficulty speaking: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
