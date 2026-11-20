# Review pack: Sore or white tongue

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
| [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | 2026-11-19 |  | Page last reviewed: 16 May 2023 |
| [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/) | 2026-11-19 |  | Page last reviewed: 11 March 2024 |
| [Mouth cancer: symptoms](https://www.nhs.uk/conditions/mouth-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 10 November 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Oral thrush (mouth thrush)](https://www.nhs.uk/conditions/oral-thrush-mouth-thrush/) | 2026-11-19 |  | Page last reviewed: 09 October 2026 |
| [Laryngeal (larynx) cancer: symptoms](https://www.nhs.uk/conditions/laryngeal-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 1 September 2025 |

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

## Sore or white tongue red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_to_allergic_swelling`<br>Lips, mouth, tongue or throat suddenly swollen | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_to_throat_tight`<br>Sore tongue with the throat feeling tight or closed up | "Throat feels tight" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |

## Sore or white tongue: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_to_pain_not_going`<br>Tongue pain or itching that does not go away or gets worse | "Tongue pain or itching that is not going away, or is getting worse" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or dentist. The source gives no fixed time.* | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| `or_to_white_patches`<br>White patches on the tongue | "White patches on the tongue or inside the mouth" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or dentist. The source gives no fixed time.* | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| `or_to_ulcer_unusual`<br>A mouth ulcer that is unusual, bleeding, or getting more painful and red | "Mouth ulcer that is unusual, bleeding or getting more painful" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a dentist or GP. The source gives no fixed time.* | [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/) | |
| `or_to_ulcer_or_patch_3_weeks`<br>A mouth ulcer, red or white patch, or lump that has lasted more than 3 weeks | "Mouth ulcer lasting more than 3 weeks" OR "Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or dentist. The source gives no fixed time.* | [Mouth cancer: symptoms](https://www.nhs.uk/conditions/mouth-cancer/symptoms/) | |

## Default outcome

Used when no rule fires.

- **Sore or white tongue with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *A sore or white tongue is not usually serious. A pharmacist can help.*
- Source: [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Sore or white tongue | Is your tongue sore, or does it look white or patchy? |  | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Tongue pain or itching that is not going away, or is getting worse | Has the pain or itching in your tongue gone on for a long time, or is it getting worse? |  | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| White patches on the tongue or inside the mouth | Do you have white patches on your tongue or inside your mouth? |  | [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/) | |
| Mouth ulcer that is unusual, bleeding or getting more painful | Is the ulcer bigger than usual or near the back of your throat, or is it bleeding or getting more painful and red? |  | [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/) | |
| Mouth ulcer lasting more than 3 weeks | Do you have a mouth ulcer that has lasted more than 3 weeks? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks | Do you have a red or white patch, or a lump, in your mouth or on your lip that has not gone after 3 weeks? |  | [Mouth cancer: symptoms](https://www.nhs.uk/conditions/mouth-cancer/symptoms/) | |

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

### `advice_tongue_gp_or_dentist`

**What to do:** See a GP or dentist. They can check the cause, such as mouth thrush or a patch that needs testing.

**Look out for:**
- A mouth ulcer or patch that lasts more than 3 weeks
- Pain or difficulty swallowing
- Lips, tongue or throat suddenly swelling

**Get more help when:**
- Call 999 if your tongue or throat suddenly swells or you find it hard to breathe
- Ask for an urgent GP appointment or get help from 111 if you find it very hard to swallow

**Where to go:** Make an appointment with a GP or dentist. A pharmacist can suggest treatments for pain while you wait.

**What you can do yourself:**
- Use a soft toothbrush, and brush or scrape your tongue gently
- Drink cool drinks through a straw
- Take paracetamol or ibuprofen for pain
- Avoid spicy, acidic or hot food and drink, smoking and alcohol

Source: [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/), [Mouth ulcers](https://www.nhs.uk/conditions/mouth-ulcers/), [Oral thrush (mouth thrush)](https://www.nhs.uk/conditions/oral-thrush-mouth-thrush/)

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

### `advice_tongue_self_care`

**What to do:** A sore or white tongue is not usually serious and is often easily treated. A pharmacist can help.

**Look out for:**
- Pain or itching that does not go away or gets worse
- White patches on your tongue
- A mouth ulcer that lasts more than 3 weeks

**Get more help when:**
- See a GP or dentist if you get any of the signs above
- Call 999 if your tongue or throat suddenly swells or you find it hard to breathe

**Where to go:** You do not need an appointment now. A pharmacist can tell you if you need to see a GP or dentist.

**What you can do yourself:**
- Use a soft toothbrush, and brush or scrape your tongue gently
- Drink cool drinks through a straw
- Take paracetamol or ibuprofen for pain
- Avoid spicy, acidic or hot food and drink, smoking and alcohol

Source: [Sore or white tongue](https://www.nhs.uk/symptoms/sore-or-white-tongue/)

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
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Geographic tongue (harmless patches on the tongue that look like a map) | 59032001 | uncommon | Red patches with a pale edge on the tongue that move around: strongly supports; White patches on the tongue or inside the mouth: supports; Tongue pain or itching that is not going away, or is getting worse: supports |
| Leukoplakia (white patches in the mouth that do not rub off) | 414603003 | uncommon | White patches that stay when rubbed: strongly supports; White patches on the tongue or inside the mouth: strongly supports; Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks: supports |
| Mouth cancer | 363505006 | rare | Mouth ulcer lasting more than 3 weeks: strongly supports; Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks: strongly supports; Lump in the mouth or neck: supports; Losing weight without trying: supports; Hoarse voice for more than 3 weeks: supports |
| Mouth thrush (a fungal infection that causes white patches in the mouth) | 79740000 | common | White patches that wipe off, leaving red spots: strongly supports; White patches on the tongue or inside the mouth: strongly supports; Sore cracks at the corners of the mouth: supports; Mouth painful, red, swollen or bleeding: supports; Bad taste in the mouth: supports; Dry mouth: supports |
| Mouth ulcers | 426965005 | common | Painful sores (ulcers) in the mouth: strongly supports; Feeling anxious, worried or panicky: supports; Bit or burnt the tongue: supports; Mouth painful, red, swollen or bleeding: supports |
| Sore tongue from a bite or a burn | 282783001 | common | Bit or burnt the tongue: strongly supports; Painful sores (ulcers) in the mouth: supports; Mouth painful, red, swollen or bleeding: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
