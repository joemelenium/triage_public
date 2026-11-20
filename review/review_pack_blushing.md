# Review pack: Blushing

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
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Rosacea](https://www.nhs.uk/conditions/rosacea/) | 2026-11-19 |  | Page last reviewed: 17 March 2023 |
| [Blushing](https://www.nhs.uk/symptoms/blushing/) | 2026-11-19 |  | Page last reviewed: 25 July 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Menopause](https://www.nhs.uk/conditions/menopause-and-perimenopause/) | 2026-11-19 |  |  |
| [Overactive thyroid (hyperthyroidism)](https://www.nhs.uk/conditions/overactive-thyroid-hyperthyroidism/) | 2026-11-19 |  | Page last reviewed: 11 April 2023 |
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

## Blushing red flags: Emergency (help now)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bl_allergic_swelling`<br>Sudden flushing with swelling of the lips, mouth, tongue or throat<br>**Note:** Clinical knowledge: sudden flushing can be part of a severe allergic reaction. | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |

## Blushing red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bl_rosacea_eye`<br>A red face with a painful, red or gritty eye, sensitivity to light or blurred vision | "Eye painful, red, gritty or sensitive to light, or blurred vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Rosacea](https://www.nhs.uk/conditions/rosacea/) | |

## Blushing: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_blushing_gp`<br>Blushing affecting everyday life, or that may be caused by a medicine or a medical condition<br>**Note:** The Blushing page says see a GP if it affects everyday life, or might be caused by a medical condition (such as rosacea, the menopause or an overactive thyroid) or a medicine. | "Affecting daily life, mood or self-esteem" OR "Started a new medicine or changed a dose in the last few weeks" OR "Face red most of the time, with small blood vessels or spots" OR "Hot flushes" OR "Swelling at the front of the neck" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Blushing](https://www.nhs.uk/symptoms/blushing/) | |

## Default outcome

Used when no rule fires.

- **Blushing with nothing that needs a GP: things you can do yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *No appointment needed*
- Source: [Blushing](https://www.nhs.uk/symptoms/blushing/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Blushing or a red face | Do you blush, or does your face go red, a lot? | 271812002 | [Blushing](https://www.nhs.uk/symptoms/blushing/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Eye painful, red, gritty or sensitive to light, or blurred vision | Is your eye painful, red or gritty, or sensitive to light? Or is your vision blurred? |  | [Rosacea](https://www.nhs.uk/conditions/rosacea/) | |
| Affecting daily life, mood or self-esteem | Is it affecting your daily life, your mood or how you feel about yourself? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Face red most of the time, with small blood vessels or spots | Is your face red most of the time, with small blood vessels showing, or small red spots? |  | [Rosacea](https://www.nhs.uk/conditions/rosacea/) | |
| Hot flushes | Do you get hot flushes? These are sudden feelings of heat in your face, neck or chest. |  | [Menopause](https://www.nhs.uk/conditions/menopause-and-perimenopause/) | |
| Swelling at the front of the neck | Do you have a swelling at the front of your neck? |  | [Overactive thyroid (hyperthyroidism)](https://www.nhs.uk/conditions/overactive-thyroid-hyperthyroidism/) | |

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

### `advice_anaphylaxis_999`

**What to do:** Call 999 now and say you think it is anaphylaxis, a severe allergic reaction. Use an adrenaline auto-injector (such as an EpiPen) straight away if you have one.

**Look out for:**
- Swelling of the lips, mouth, tongue or throat
- Struggling to breathe, or very wheezy
- Skin, tongue or lips turning blue, grey or pale
- Feeling faint, very confused or drowsy

**Get more help when:**
- If you are no better after 5 minutes, use a second auto-injector if you have one
- Call 999 again if the person gets worse or stops responding

**Where to go:** Call 999 for an ambulance. Do not drive to A&E. Stay with the person until help arrives.

**What you can do yourself:**
- Lie down. You can raise your legs. If you are struggling to breathe, sit up slowly.
- If you are pregnant, lie on your left side
- If you were stung by an insect, try to remove the sting if it is still in the skin
- Do not stand or walk at any time, even if you feel better

Source: [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/)

### `advice_rosacea_eye_urgent`

**What to do:** Ask for an urgent GP appointment or call NHS 111 today. A painful, red or gritty eye with a red face can mean the eye is affected, which can be serious if not treated quickly.

**Look out for:**
- Your vision getting worse
- The eye becoming more painful, or bright light hurting it

**Get more help when:**
- Go to A&E if you suddenly lose sight, or the eye pain is severe

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

Source: [Rosacea](https://www.nhs.uk/conditions/rosacea/)

### `advice_blushing_gp`

**What to do:** See a GP about your blushing. The source gives no fixed time. Treatment depends on the cause, such as rosacea, the menopause, an overactive thyroid or a medicine.

**Look out for:**
- A painful, red or gritty eye, or blurred vision
- Swelling in your neck, or a fast heartbeat

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your eye becomes painful or your vision is blurred

**Where to go:** Book an appointment with your GP surgery.

**What you can do yourself:**
- Keep cool by taking off a layer of clothing and drinking water
- Avoid spicy food, alcohol and hot drinks if they make you blush

Source: [Blushing](https://www.nhs.uk/symptoms/blushing/), [Rosacea](https://www.nhs.uk/conditions/rosacea/)

### `advice_blushing_self_care`

**What to do:** Blushing is common, and is often caused by feeling embarrassed, hot or anxious. There are things you can do to help.

**Look out for:**
- Blushing affecting your everyday life
- A red face most of the time, with small blood vessels or spots
- Hot flushes, or a swelling in the neck

**Get more help when:**
- See a GP if any of these happen, or you think a medicine may be causing it

**Where to go:** No appointment needed.

**What you can do yourself:**
- Keep cool by taking off a layer of clothing and drinking water
- Make-up that reduces redness can help in stressful situations
- Avoid spicy food, alcohol and hot drinks if they make you blush

Source: [Blushing](https://www.nhs.uk/symptoms/blushing/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bl_allergic_swelling`: Clinical knowledge: sudden flushing can be part of a severe allergic reaction.
- `or_blushing_gp`: The Blushing page says see a GP if it affects everyday life, or might be caused by a medical condition (such as rosacea, the menopause or an overactive thyroid) or a medicine.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Overactive thyroid (the thyroid gland in the neck makes too much hormone) | 34486009 | rare | Feeling restless, shaky or too hot all the time: strongly supports; Losing weight without trying: strongly supports; Heart racing, slow, skipping or fluttering: supports; Feels sweaty: supports; Feels very tired: supports; Night sweats: supports; Heart beating very fast: supports; Swelling at the front of the neck: supports; Feeling anxious, worried or panicky: supports; Shaking or trembling (tremor): supports |
| Blushing from embarrassment, heat or anxiety |  | very common | Blushing when embarrassed, anxious or hot: strongly supports; Feeling anxious, worried or panicky: supports |
| Rosacea (a long-term skin condition that makes the face red) | 398909004 | common | Face red most of the time, with small blood vessels or spots: strongly supports; Eye painful, red, gritty or sensitive to light, or blurred vision: supports; Rash is sore or painful: supports |
| Perimenopause or menopause (when periods change and then stop) | 289903006 | uncommon | Hot flushes: strongly supports; Trouble sleeping (insomnia): supports; Feeling low, sad or depressed: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports; Feels very tired: supports; Night sweats: supports; Vaginal dryness: supports; Irregular periods: supports; Periods stopped for 12 months or more (the menopause): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
