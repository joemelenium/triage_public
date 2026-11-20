# Review pack: Snoring

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
| [Snoring](https://www.nhs.uk/symptoms/snoring/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | 2026-11-19 |  | Page last reviewed: 23 June 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/) | 2026-11-19 |  | Page last reviewed: 11 May 2026 |

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

## Snoring: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sn_breathing_stops`<br>Snoring with breathing that stops and starts, or gasping or choking noises, during sleep | "Breathing stops and starts during sleep, or gasping or choking noises" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| `or_sn_sleepy`<br>Snoring and feeling very sleepy during the day | "Very sleepy or falling asleep during the day" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| `or_sn_big_impact`<br>Snoring that has a big impact on life, or is not helped by lifestyle changes | "Snoring has a big impact, or has not helped with changes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |

## Default outcome

Used when no rule fires.

- **Snoring with nothing that needs more help: try lifestyle changes**
- Outcome: Self-manageable, Self-care, No appointment needed. *Snoring is not usually caused by anything serious. Simple changes can help.*
- Source: [Snoring](https://www.nhs.uk/symptoms/snoring/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Snoring | Do you snore? | 72863001 | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Breathing stops and starts during sleep, or gasping or choking noises | Does your breathing stop and start while you sleep, or do you make gasping or choking noises? Someone else may have noticed this. |  | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| Very sleepy or falling asleep during the day | Do you often feel very sleepy, or keep falling asleep, during the day? | 1367959007 | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| Snoring has a big impact, or has not helped with changes | Is your snoring having a big impact on your life or your partner's, or not helped by changes like sleeping on your side? |  | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |

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

### `advice_snoring_gp`

**What to do:** See a GP. You may have sleep apnoea, where your breathing stops and starts while you sleep. It can be serious if it is not treated.

**Look out for:**
- Feeling so sleepy in the day that you nod off
- Waking up with a headache, or finding it hard to concentrate

**Get more help when:**
- Do not drive if you feel sleepy. Tell the GP if you have nodded off while driving.
- Call 999 if someone stops breathing and does not start again

**Where to go:** Make an appointment with a GP. It can help to bring someone who has seen you sleep.

**What you can do yourself:**
- Try to lose weight if you are overweight
- Sleep on your side
- Do not smoke, drink too much alcohol, or take sleeping pills

Source: [Snoring](https://www.nhs.uk/symptoms/snoring/), [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/)

### `advice_snoring_self_care`

**What to do:** Snoring is very common and is not usually caused by anything serious. Simple changes can help.

**Look out for:**
- Breathing that stops and starts while you sleep, or gasping or choking noises
- Feeling very sleepy during the day
- Snoring that has a big impact on your life or your partner's

**Get more help when:**
- See a GP if you get any of the signs above, or changes do not help

**Where to go:** You do not need an appointment now.

**What you can do yourself:**
- Try to lose weight if you are overweight
- Sleep on your side. A special pillow can help.
- Do not smoke, drink too much alcohol, or take sleeping pills

Source: [Snoring](https://www.nhs.uk/symptoms/snoring/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sleep apnoea (breathing that stops and starts during sleep) | 78275009 | common | Breathing stops and starts during sleep, or gasping or choking noises: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Sleepiness affecting life, such as work, school or driving: supports; Tired for a few weeks or more, without knowing why: supports; Very sleepy or falling asleep during the day: strongly supports; Snoring: strongly supports; Overweight: supports |
| Allergic rhinitis (a nose allergy, often all year) | 446096008 | common | Blocked or runny nose: strongly supports; Itchy, watery eyes and sneezing: strongly supports; Nose symptoms all year round: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Has eczema, hay fever or a food allergy: supports; Blocked or runny nose for more than 3 weeks: supports |
| Large tonsils or adenoids in a child (glands at the back of the throat and nose) | 66622006 | uncommon | Breathes through the mouth, or sleeps with the mouth open: strongly supports; Often gets sore throats: supports; Breathing stops and starts during sleep, or gasping or choking noises: supports; Blocked or runny nose: supports |
| Nasal polyps (soft, harmless growths inside the nose) | 736500007 | uncommon | Blocked or runny nose: strongly supports; Lost or changed sense of smell or taste: strongly supports; Blocked or runny nose for more than 3 weeks: strongly supports; Phlegm dripping down the back of the throat from the nose: supports; Snoring: supports; Sense of smell faded slowly over months or years: supports |
| Snoring that is not caused by a health problem |  | very common | Snoring worse after alcohol or when sleeping on the back: strongly supports; Blocked or runny nose: supports; Breathes through the mouth, or sleeps with the mouth open: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
