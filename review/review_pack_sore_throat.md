# Review pack: Sore throat

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
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Laryngeal (larynx) cancer: symptoms](https://www.nhs.uk/conditions/laryngeal-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 1 September 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Mouth cancer: symptoms](https://www.nhs.uk/conditions/mouth-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 10 November 2026 |
| [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/) | 2026-11-19 |  | Page last reviewed: 11 March 2024 |

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

## Sore throat red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to you right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_st_breathing_or_swallowing`<br>Sore throat with difficulty breathing or being unable to swallow | "Difficulty breathing" OR "Unable to swallow" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_drooling`<br>Sore throat with drooling, which can be a sign of not being able to swallow | "Drooling" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_stridor`<br>Sore throat with a high-pitched sound when breathing | "High-pitched sound when breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_severe_and_worsening`<br>Sore throat with severe symptoms that are getting worse quickly | "Severe symptoms getting worse quickly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_quinsy_signs`<br>Sore throat with swelling inside the mouth and throat, difficulty speaking or difficulty opening the mouth | "Swelling inside the mouth and throat" OR "Difficulty speaking" OR "Difficulty opening the mouth" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |

## Sore throat red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to you? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_st_high_temperature`<br>Sore throat with a very high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get advice from 111 now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_dehydration`<br>Sore throat with signs of dehydration | "Signs of dehydration" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get advice from 111 now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_weakened_immune_system`<br>Sore throat in someone with a weakened immune system | "Weakened immune system" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get advice from 111 now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_st_pus_on_tonsils`<br>Sore throat with pus-filled spots on the tonsils | "Pus-filled spots on the tonsils" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| `rf_st_too_painful_to_eat_or_drink`<br>Sore throat so painful it is difficult to eat or drink | "Throat so painful it is difficult to eat or drink" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |

## Sore throat: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_st_worried`<br>Sore throat and worried about the symptoms<br>**Note:** Taken directly from the source, but likely to over-triage: many people using a triage tool would say they are worried. Needs a clinical decision on whether to keep, reword or remove. | "Worried about symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get advice from 111 now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `or_st_over_a_week`<br>Sore throat that has not improved after a week | "Sore throat not improved after a week" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `or_st_frequent`<br>Often gets sore throats | "Often gets sore throats" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `or_st_lump_or_ulcer`<br>Sore throat with a lump in the mouth or neck, or a mouth ulcer lasting more than 3 weeks | "Lump in the mouth or neck" OR "Mouth ulcer lasting more than 3 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `or_st_hoarse_3_weeks`<br>Sore throat with a hoarse or croaky voice that has lasted more than 3 weeks<br>**Note:** Added in the ear, nose and throat batch. The Laryngeal cancer and Mouth cancer pages say see a GP for a hoarse voice that does not go away. | "Hoarse voice for more than 3 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Laryngeal (larynx) cancer: symptoms](https://www.nhs.uk/conditions/laryngeal-cancer/symptoms/) | |
| `or_st_child_under_5_needs_help`<br>Child under 5 who needs help for a sore throat | "Wants help with the sore throat" AND "Under 5 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `or_st_pharmacy_help`<br>Adult or child aged 5 or over who needs help for a sore throat | "Wants help with the sore throat" AND NOT "Under 5 years old" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*See a pharmacist. The source gives no fixed time.* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

## Default outcome

Used when no rule fires.

- **Sore throat with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Sore throats normally get better by themselves within a week*
- Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Sore throat | Do you have a sore throat? | 267102003 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Drooling | Are you drooling? This can be a sign of not being able to swallow. | 62718007 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| High-pitched sound when breathing | Are you making a high-pitched sound when you breathe? | 70407001 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Severe symptoms getting worse quickly | Are your symptoms severe and getting worse quickly? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swelling inside the mouth and throat | Do you have swelling inside your mouth and throat? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Difficulty opening the mouth | Are you finding it hard to open your mouth? | 87866006 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pus-filled spots on the tonsils | Do you have pus-filled spots on your tonsils, at the back of your throat? | 301791008 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Throat so painful it is difficult to eat or drink | Is your throat so painful that it is difficult to eat or drink? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Sore throat not improved after a week | Have you had the sore throat for more than a week without it getting better? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Often gets sore throats | Do you often get sore throats? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Lump in the mouth or neck | Do you have a lump in your mouth or neck? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Mouth ulcer lasting more than 3 weeks | Do you have a mouth ulcer that has lasted more than 3 weeks? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Hoarse voice for more than 3 weeks | Has your voice been hoarse or croaky for more than 3 weeks? |  | [Laryngeal (larynx) cancer: symptoms](https://www.nhs.uk/conditions/laryngeal-cancer/symptoms/) | |
| Wants help with the sore throat | Would you like help with your sore throat, such as advice on treatments? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_sore_throat_emergency`

**What to do:** Call 999 or go to A&E now.

**Look out for:**
- Difficulty breathing
- Not being able to swallow, or drooling
- A high-pitched sound when breathing
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

### `advice_sore_throat_urgent`

**What to do:** Ask for an urgent GP appointment or get advice from 111 now. You can call 111 or use 111 online.

**Look out for:**
- Difficulty breathing, or a high-pitched sound when you breathe
- Not being able to swallow, or drooling
- Severe symptoms that are getting worse quickly
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- Call 999 or go to A&E now if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 999 or go to A&E if you get any of the signs above.

**What you can do yourself:**
- Drink plenty of water
- Eat cool or soft foods
- Rest

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

### `advice_sore_throat_gp`

**What to do:** See a GP about your sore throat.

**Look out for:**
- A very high temperature, or feeling hot, cold or shivery
- Signs of dehydration, such as peeing less than usual or dark, strong-smelling pee
- Difficulty breathing, not being able to swallow, drooling, or a high-pitched sound when you breathe
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get a very high temperature, or you are worried. Do the same if you are peeing less than usual. This can be a sign of dehydration.
- Get help from NHS 111 if you get pus-filled spots on your tonsils, at the back of your throat. Do the same if your throat is so sore it is hard to eat or drink.
- Call 999 or go to A&E now if you find it hard to breathe, speak or open your mouth. Do the same if you cannot swallow, are drooling, or are quickly getting much worse.

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Gargle with warm, salty water (children should not try this)
- Drink plenty of water
- Eat cool or soft foods
- Avoid smoking or smoky places
- Rest

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

### `advice_sore_throat_gp_lump_or_ulcer`

**What to do:** See a GP about the lump or the mouth ulcer, as well as your sore throat.

**Look out for:**
- A very high temperature, or feeling hot, cold or shivery
- Signs of dehydration, such as peeing less than usual or dark, strong-smelling pee
- Difficulty breathing, not being able to swallow, drooling, or a high-pitched sound when you breathe
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get a very high temperature, or you are worried. Do the same if you are peeing less than usual. This can be a sign of dehydration.
- Get help from NHS 111 if you get pus-filled spots on your tonsils, at the back of your throat. Do the same if your throat is so sore it is hard to eat or drink.
- Call 999 or go to A&E now if you find it hard to breathe, speak or open your mouth. Do the same if you cannot swallow, are drooling, or are quickly getting much worse.

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Gargle with warm, salty water (children should not try this)
- Drink plenty of water
- Eat cool or soft foods
- Avoid smoking or smoky places
- Rest

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

### `advice_mouth_lump_gp`

**What to do:** See a GP or dentist about the ulcer, patch, lump or hoarse voice. Most are not serious, but it is important to get them checked, because finding cancer early makes it easier to treat.

**Look out for:**
- Difficulty swallowing or speaking
- A lump in your neck
- Losing weight without trying

**Get more help when:**
- Ask for an urgent GP appointment or get help from 111 if you find it very hard to swallow
- Call 999 or go to A&E if you cannot swallow at all or find it hard to breathe

**Where to go:** Make an appointment with a GP or dentist.

**What you can do yourself:**
- Do not smoke, and cut down on alcohol
- Use a soft toothbrush and avoid spicy or very hot food if your mouth is sore

Source: [Mouth cancer: symptoms](https://www.nhs.uk/conditions/mouth-cancer/symptoms/), [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/), [Laryngeal (larynx) cancer: symptoms](https://www.nhs.uk/conditions/laryngeal-cancer/symptoms/)

### `advice_sore_throat_pharmacy`

**What to do:** See a pharmacist. They can suggest treatments, give advice, and give antibiotics if you need them.

**Look out for:**
- A sore throat that does not improve after a week
- A very high temperature, or feeling hot, cold or shivery
- Difficulty breathing, not being able to swallow, drooling, or a high-pitched sound when you breathe
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- See a GP if your sore throat does not improve after a week
- Ask for an urgent GP appointment or call 111 if you get a very high temperature, or you are worried. Do the same if you are peeing less than usual. This can be a sign of dehydration.
- Get help from NHS 111 if you get pus-filled spots on your tonsils, at the back of your throat. Do the same if your throat is so sore it is hard to eat or drink.
- Call 999 or go to A&E now if you find it hard to breathe, speak or open your mouth. Do the same if you cannot swallow, are drooling, or are quickly getting much worse.

**Where to go:** Go to a pharmacy. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Gargle with warm, salty water (children should not try this)
- Drink plenty of water
- Eat cool or soft foods
- Avoid smoking or smoky places
- Suck ice cubes, ice lollies or hard sweets. Do not give young children anything small and hard to suck, because they could choke.
- Rest
- Some medicines are not safe for everyone, for example if you are pregnant. Check the leaflet or ask the pharmacist before taking them.

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

### `advice_sore_throat_self_care`

**What to do:** You can treat this yourself. Sore throats usually get better by themselves within a week.

**Look out for:**
- A sore throat that does not improve after a week
- A very high temperature, or feeling hot, cold or shivery
- Difficulty breathing, not being able to swallow, drooling, or a high-pitched sound when you breathe
- Swelling inside your mouth and throat. Or finding it hard to speak or open your mouth.

**Get more help when:**
- See a pharmacist if you would like help with your sore throat
- See a GP if your sore throat does not improve after a week, or you often get sore throats
- Ask for an urgent GP appointment or call 111 if you get a very high temperature, or you are worried. Do the same if you are peeing less than usual. This can be a sign of dehydration.
- Get help from NHS 111 if you get pus-filled spots on your tonsils, at the back of your throat. Do the same if your throat is so sore it is hard to eat or drink.
- Call 999 or go to A&E now if you find it hard to breathe, speak or open your mouth. Do the same if you cannot swallow, are drooling, or are quickly getting much worse.

**Where to go:** You do not need an appointment now. A pharmacist can help if you need it. For urgent help call 111 or use 111 online. In an emergency call 999 or go to A&E.

**What you can do yourself:**
- Gargle with warm, salty water (children should not try this)
- Drink plenty of water
- Eat cool or soft foods
- Avoid smoking or smoky places
- Suck ice cubes, ice lollies or hard sweets. Do not give young children anything small and hard to suck, because they could choke.
- Rest

Source: [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `or_st_worried`: Taken directly from the source, but likely to over-triage: many people using a triage tool would say they are worried. Needs a clinical decision on whether to keep, reword or remove.
- `or_st_hoarse_3_weeks`: Added in the ear, nose and throat batch. The Laryngeal cancer and Mouth cancer pages say see a GP for a hoarse voice that does not go away.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| COVID-19 | 840539006 | uncommon | Lost or changed sense of smell or taste: supports; Very high temperature, or feels hot, cold or shivery: supports; Dry cough: supports; Aching body: supports; Feels very tired: supports; Blocked or runny nose: supports |
| Flu | 6142004 | uncommon | Very high temperature, or feels hot, cold or shivery: strongly supports; Aching body: strongly supports; Feels very tired: supports; Dry cough: supports; Feels very unwell: supports |
| Hay fever (an allergy to pollen) | 21719001 | uncommon | Itchy, watery eyes and sneezing: strongly supports; Symptoms come on around pollen, dust, mould or animals: strongly supports; Blocked or runny nose: strongly supports; Has eczema, hay fever or a food allergy: supports; Dry cough: supports |
| Phlegm (mucus) from the nose dripping down the throat, or sinusitis (swollen sinuses in the face) |  | uncommon | Phlegm dripping down the back of the throat from the nose: strongly supports; Blocked or runny nose: strongly supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Cough worse at night: supports; Cough for 3 weeks or more: supports; Green or yellow phlegm from the nose: supports; Lost or changed sense of smell or taste: supports |
| Epiglottitis (swelling of the flap at the back of the throat that covers the windpipe) | 80384002 | rare | High-pitched sound when breathing: strongly supports; Drooling: strongly supports; Unable to swallow: supports; Difficulty breathing: supports; Very high temperature, or feels hot, cold or shivery: supports; Hoarse voice: supports; Child wants to sit up rather than lie down: supports |
| Glandular fever (a virus that causes a sore throat, swollen glands and tiredness) | 271558008 | uncommon | Feels very tired: strongly supports; Swollen glands in the neck: strongly supports; Sore throat not improved after a week: supports; Very high temperature, or feels hot, cold or shivery: supports; Lump in the mouth or neck: supports; Swollen glands in the armpit or groin: supports; Aching body: supports |
| Quinsy (a pocket of pus next to a tonsil, at the back of the throat) | 15033003 | rare | Severe symptoms getting worse quickly: strongly supports; Difficulty opening the mouth: strongly supports; Difficulty speaking: supports; Unable to swallow: supports; Drooling: supports; Swelling inside the mouth and throat: supports; Difficulty breathing: supports; Earache: supports |
| Strep throat (a bacterial throat infection) | 43878008 | uncommon | Pus-filled spots on the tonsils: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Swollen glands in the neck: supports; Cough or runny nose: argues against |
| Cancer of the throat or voice box |  | rare | Hoarse voice for more than 3 weeks: strongly supports; Lump in the mouth or neck: strongly supports; Sore throat not improved after a week: supports; Earache: supports; Losing weight without trying: supports |
| Tonsillitis (infected tonsils at the back of the throat) | 90176007 | common | Pus-filled spots on the tonsils: supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Often gets sore throats: supports; Lump in the mouth or neck: supports; Swollen glands in the neck: supports; Feels very tired: supports; Cough or runny nose: argues against |
| Sore throat from a virus, such as a cold or flu | 1532007 | very common | Cough or runny nose: strongly supports; Blocked or runny nose: supports; Hoarse voice: supports; Aching body: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Sore throat not improved after a week: argues against; Pus-filled spots on the tonsils: argues against; Unable to swallow: strongly argues against; Difficulty opening the mouth: strongly argues against |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
