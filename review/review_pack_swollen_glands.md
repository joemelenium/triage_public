# Review pack: Swollen glands

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
| [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/) | 2026-11-19 |  | Page last reviewed: 20 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | 2026-11-19 |  | Page last reviewed: 29 September 2023 |
| [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | 2026-11-19 |  | Page last reviewed: 13 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | 2026-11-18 |  | Page last reviewed: 10 September 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Hodgkin lymphoma: symptoms](https://www.nhs.uk/conditions/hodgkin-lymphoma/symptoms/) | 2026-11-19 |  | Page last reviewed: 14 October 2025 |

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

## Swollen glands red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sg_cannot_swallow`<br>Swollen glands and cannot swallow, even your own spit<br>**Note:** The Glandular fever page says call 999. The Sore throat page says call 999 or go to A&E. | "Unable to swallow" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/) | |
| `rf_sg_drooling`<br>Swollen glands with drooling, which can be a sign of not being able to swallow | "Drooling" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_sg_stridor`<br>Swollen glands with a high-pitched sound when breathing | "High-pitched sound when breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_sg_neck_swelling_spreading`<br>Swelling in the neck or under the tongue, or a lot of swelling in the mouth | "Swelling in the neck or under the tongue, or a lot of swelling in the mouth" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |

## Swollen glands red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sg_swallowing_or_breathing`<br>Swollen glands and finding it very difficult to swallow, or difficulty breathing | "Problems swallowing" OR "Difficulty breathing" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `rf_sg_child_bruising`<br>A child with swollen glands who is bruising or bleeding easily, or for no reason | "Under 16 years old" AND "Bruising or bleeding easily, or for no reason" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call 111* | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |

## Swollen glands: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sg_over_a_week`<br>Swollen glands getting bigger, or not gone down within 1 week | "Glands getting bigger, or not gone down after 1 week" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `or_sg_hard_or_fixed`<br>Swollen glands that feel hard or do not move when pressed | "Glands feel hard, or do not move when pressed" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `or_sg_sweats_or_temperature`<br>Swollen glands with night sweats or a very high temperature | "Night sweats" OR "Very high temperature, or feels hot, cold or shivery" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `or_sg_no_other_illness`<br>Swollen glands with no other signs of illness or infection | "Swollen glands with no other signs of being ill" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `or_sg_collarbone`<br>Swollen glands just above or below the collarbone | "Swollen glands just above or below the collarbone" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| `or_sg_bruising`<br>Swollen glands and bruising or bleeding easily | "Bruising or bleeding easily, or for no reason" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |

## Default outcome

Used when no rule fires.

- **Swollen glands with nothing that needs more help: they usually go down by themselves within 1 to 2 weeks**
- Outcome: Self-manageable, Self-care, No appointment needed. *Swollen glands from an infection usually get better by themselves within 1 to 2 weeks*
- Source: [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Swollen glands | Do you have swollen glands? They feel like lumps in the neck, under the chin, in the armpits or in the groin. | 30746006 | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Drooling | Are you drooling? This can be a sign of not being able to swallow. | 62718007 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| High-pitched sound when breathing | Are you making a high-pitched sound when you breathe? | 70407001 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swelling in the neck or under the tongue, or a lot of swelling in the mouth | Is there swelling in your neck or under your tongue, or a lot of swelling inside your mouth? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Bruising or bleeding easily, or for no reason | Have you been bruising or bleeding easily, or for no reason? | 424131007 | [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/) | |
| Glands getting bigger, or not gone down after 1 week | Are the swollen glands getting bigger, or have they not gone down after 1 week? |  | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| Glands feel hard, or do not move when pressed | Do the swollen glands feel hard, or do they stay still when you press them? |  | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| Night sweats | Do you have night sweats, where you wake up very sweaty? | 42984000 | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swollen glands with no other signs of being ill | Have your glands swollen up without any other signs of being ill, such as a cold or sore throat? |  | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |
| Swollen glands just above or below the collarbone | Are the swollen glands just above or below your collarbone? |  | [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/) | |

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

### `advice_mouth_throat_ae`

**What to do:** Call 999 or go to A&E now. Swelling in the mouth or neck can make it hard to breathe.

**Look out for:**
- Difficulty breathing, or a high-pitched sound when breathing
- Not being able to swallow, even your own spit, or drooling
- Swelling that is spreading in the neck, under the tongue or around the eye

**Get more help when:**
- Call 999 if breathing gets harder or you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Sit up and lean forward if that makes breathing easier

Source: [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/), [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/)

### `advice_glands_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Call 111 if you need advice for a child under 5.

**Look out for:**
- Not being able to swallow, even your own spit, or drooling
- Severe difficulty breathing, or a high-pitched sound when breathing
- Swelling spreading in the neck or under the tongue

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.

Source: [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/), [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/), [Acute lymphoblastic leukaemia: symptoms](https://www.nhs.uk/conditions/acute-lymphoblastic-leukaemia/symptoms/)

### `advice_glands_gp`

**What to do:** See a GP. Swollen glands are usually caused by an infection, but they can check for other causes.

**Look out for:**
- Finding it very difficult to swallow, or difficulty breathing
- Bruising or bleeding easily
- Glands that keep getting bigger

**Get more help when:**
- Ask for an urgent GP appointment or get help from 111 if it gets very hard to swallow or breathe
- Call 999 or go to A&E if you cannot swallow at all, are drooling, or have severe difficulty breathing

**Where to go:** Make an appointment with a GP.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.

Source: [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/), [Hodgkin lymphoma: symptoms](https://www.nhs.uk/conditions/hodgkin-lymphoma/symptoms/)

### `advice_glands_self_care`

**What to do:** Swollen glands are usually a sign that the body is fighting an infection. They usually go down by themselves within 1 to 2 weeks.

**Look out for:**
- Glands that are getting bigger, or have not gone down after 1 week
- Glands that feel hard, or do not move when you press them
- Night sweats, or a very high temperature
- Finding it very difficult to swallow, or difficulty breathing

**Get more help when:**
- See a GP if you get any of the first three signs above
- Ask for an urgent GP appointment or get help from 111 if it gets very hard to swallow or breathe
- Call 999 or go to A&E if you cannot swallow at all or are drooling

**Where to go:** You do not need an appointment now. A pharmacist can advise on painkillers.

**What you can do yourself:**
- Rest and drink plenty of fluids
- Take painkillers such as paracetamol or ibuprofen. Do not give aspirin to a child under 16.

Source: [Swollen glands](https://www.nhs.uk/symptoms/swollen-glands/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sg_cannot_swallow`: The Glandular fever page says call 999. The Sore throat page says call 999 or go to A&E.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Dental abscess (a pocket of pus in a tooth or gum) | 299709002 | common | Intense, throbbing tooth or gum pain: strongly supports; Swollen face, cheek or jaw: strongly supports; Toothache: strongly supports; Bad taste in the mouth: supports; Tooth hurts when biting or chewing: supports; Very high temperature, or feels hot, cold or shivery: supports; Swollen glands in the neck: supports; Sharp tooth pain with hot, cold or sweet things: supports |
| Glandular fever (a virus that causes a sore throat, swollen glands and tiredness) | 271558008 | uncommon | Feels very tired: strongly supports; Swollen glands in the neck: strongly supports; Sore throat not improved after a week: supports; Very high temperature, or feels hot, cold or shivery: supports; Lump in the mouth or neck: supports; Swollen glands in the armpit or groin: supports; Aching body: supports |
| Leukaemia (a cancer of the blood) | 91855006 | rare | Bruising or bleeding easily, or for no reason: strongly supports; Skin paler than usual for weeks or longer: supports; Feels very tired: supports; Very high temperature, or feels hot, cold or shivery: supports; Night sweats: supports; Losing weight without trying: supports |
| Mouth cancer | 363505006 | rare | Mouth ulcer lasting more than 3 weeks: strongly supports; Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks: strongly supports; Lump in the mouth or neck: supports; Losing weight without trying: supports; Hoarse voice for more than 3 weeks: supports |
| Mumps (a virus that causes painful swelling at the side of the face) | 36989005 | rare | Swelling on the side of the face, in front of and below the ear: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Aching body: supports; Feels very tired: supports; Earache: supports |
| A stone or infection in a spit gland (salivary gland) | 28826002 | uncommon | Swelling under the jaw or tongue that gets worse when eating: strongly supports; Dry mouth: supports; Bad taste in the mouth: supports; Very high temperature, or feels hot, cold or shivery: supports |
| A serious infection spreading from a tooth into the face or neck |  | rare | Swelling in the neck or under the tongue, or a lot of swelling in the mouth: strongly supports; Swollen face, cheek or jaw: strongly supports; Swelling, redness or pain around the eye: supports; Difficulty opening the mouth: supports; Very high temperature, or feels hot, cold or shivery: supports; Problems swallowing: supports; Difficulty breathing: supports |
| Swollen glands from a common infection, such as a cold or throat infection | 445718006 | very common | Cold, flu, COVID-19 or a similar illness in the last few weeks: strongly supports; Sore throat: supports; Blocked or runny nose: supports; Earache: supports; Swollen glands in the neck: supports |
| Cancer of the throat or voice box |  | rare | Hoarse voice for more than 3 weeks: strongly supports; Lump in the mouth or neck: strongly supports; Sore throat not improved after a week: supports; Earache: supports; Losing weight without trying: supports |
| Tonsillitis (infected tonsils at the back of the throat) | 90176007 | common | Pus-filled spots on the tonsils: supports; Very high temperature, or feels hot, cold or shivery: supports; Throat so painful it is difficult to eat or drink: supports; Often gets sore throats: supports; Lump in the mouth or neck: supports; Swollen glands in the neck: supports; Feels very tired: supports; Cough or runny nose: argues against |
| Lymphoma (a cancer of the lymph glands) | 118600007 | rare | A painless lump or swelling in the neck, armpit or groin: strongly supports; Night sweats: strongly supports; Losing weight without trying: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports; Swollen gland is painless: strongly supports; Glands getting bigger, or not gone down after 1 week: strongly supports; Glands feel hard, or do not move when pressed: supports; Swollen glands with no other signs of being ill: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
