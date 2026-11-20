# Review pack: Coughing up blood

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
| [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | 2026-11-18 |  | Page last reviewed: 13 June 2024 |
| [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | 2026-11-18 |  | Page last reviewed: 17 July 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
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

## Coughing up blood red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hb_more_than_streaks`<br>Coughing up more than just a few spots or streaks of blood<br>**Note:** The Bronchiectasis and Pleurisy pages give the same advice. | "Coughing up more than a few spots or streaks of blood" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| `rf_hb_with_breathing_heart_or_pain`<br>Coughing up blood and finding it hard to breathe, a very fast heartbeat, or pain in the chest or upper back<br>**Note:** The page says 'finding it hard to breathe'. Including feeling short of breath is AI judgement, since the two are hard to tell apart and both can mean a blood clot in the lung. | "Difficulty breathing" OR "Short of breath" OR "Heart beating very fast" OR "Chest pain" OR "Pain in the upper back" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E immediately* | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| `rf_hb_with_high_temperature`<br>Coughing up blood with a high temperature<br>**Note:** Source difference: the Pneumonia, Flu and COVID-19 pages say call 999 or go to A&E if you start coughing up blood with those illnesses. The Coughing up blood, Bronchitis and Chest infection pages say an urgent or routine GP appointment for a few streaks. Using a high temperature to mark those illnesses is AI judgement. The more urgent is used, marked soft. | "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | |
| `rf_hb_clot_risk`<br>Coughing up blood in someone more likely to have a blood clot: leg pain or swelling, recent operation or not moving about, long journey, a clot before, pregnancy, or cancer<br>**Note:** Clinical knowledge: coughing up blood with any of these makes a blood clot in the lung (pulmonary embolism) more likely, which needs checking in hospital the same day. The Pulmonary embolism page lists leg pain and swelling as a clot symptom, and advises moving about on long journeys. | "Pain or swelling in one leg" OR "Operation, hospital stay or long time not moving, in the last 3 months" OR "Long journey of 4 hours or more in the last 4 weeks" OR "Has had a blood clot before" OR "Pregnant, or gave birth in the last 6 weeks" OR "Has cancer, or is having treatment for cancer" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Coughing up blood: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Coughing up a few spots, flecks or streaks of blood, with nothing that needs more urgent help**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/)
- **Note:** The Chest infection page says see a GP (non-urgent) for blood-stained phlegm with a chest infection. The Coughing up blood page is used, as the page for the symptom itself.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Coughing up blood | Are you coughing up blood? | 66857006 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Coughing up more than a few spots or streaks of blood | Are you coughing up more than just a few spots or streaks of blood? |  | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Pain in the upper back | Do you have pain in your upper back? | 279038004 | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Pain or swelling in one leg | Do you have pain or swelling in one of your legs? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Operation, hospital stay or long time not moving, in the last 3 months | In the last 3 months, have you had an operation or been in hospital? Or have you been unable to move about much, for example after an injury? |  | **AI judgement, needs clinical review** | |
| Long journey of 4 hours or more in the last 4 weeks | In the last 4 weeks, have you been on a long journey of 4 hours or more? For example, a flight or car journey. |  | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Has had a blood clot before | Have you had a blood clot before, in your leg or lungs? |  | **AI judgement, needs clinical review** | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Has cancer, or is having treatment for cancer | Do you have cancer, or are you having treatment for cancer? |  | **AI judgement, needs clinical review** | |

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

### `advice_coughing_blood_ae`

**What to do:** Call 999 or go to A&E now. This could be a sign of a serious problem, such as a blood clot in the lung (pulmonary embolism).

**Look out for:**
- Coughing up more blood
- Severe difficulty breathing, such as gasping or not being able to get words out
- Lips or skin turning pale, blue or grey
- Passing out

**Get more help when:**
- Call 999 straight away if you get any of the signs above, or you get worse while you wait

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/), [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/)

### `advice_coughing_blood_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Coughing up blood can have many causes, and it is important to get it checked as soon as possible.

**Look out for:**
- Coughing up more than just a few spots or streaks of blood
- Finding it hard to breathe
- A very fast heartbeat
- Pain in your chest or upper back

**Get more help when:**
- Call 999 or go to A&E now if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999 or go to A&E. Do not drive to A&E.

Source: [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hb_more_than_streaks`: The Bronchiectasis and Pleurisy pages give the same advice.
- `rf_hb_with_breathing_heart_or_pain`: The page says 'finding it hard to breathe'. Including feeling short of breath is AI judgement, since the two are hard to tell apart and both can mean a blood clot in the lung.
- `rf_hb_with_high_temperature`: Source difference: the Pneumonia, Flu and COVID-19 pages say call 999 or go to A&E if you start coughing up blood with those illnesses. The Coughing up blood, Bronchitis and Chest infection pages say an urgent or routine GP appointment for a few streaks. Using a high temperature to mark those illnesses is AI judgement. The more urgent is used, marked soft.
- `rf_hb_clot_risk`: Clinical knowledge: coughing up blood with any of these makes a blood clot in the lung (pulmonary embolism) more likely, which needs checking in hospital the same day. The Pulmonary embolism page lists leg pain and swelling as a clot symptom, and advises moving about on long journeys.
- `coughing_up_blood default outcome`: The Chest infection page says see a GP (non-urgent) for blood-stained phlegm with a chest infection. The Coughing up blood page is used, as the page for the symptom itself.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bronchiectasis (damaged airways in the lungs that make a lot of phlegm) | 12295008 | very rare | Coughs up a lot of phlegm every day: strongly supports; Coughing up phlegm: strongly supports; Cough for 3 weeks or more: strongly supports; Keeps getting chest infections, or one that is not getting better: strongly supports; Wheezing: supports; Feels very tired: supports; Coughing up blood: supports; More short of breath than usual, with a long-term lung or heart condition: supports |
| Chest infection that may need treatment from a GP | 50417007 | common | Cough: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Coughing up phlegm: strongly supports; Yellow or green phlegm: strongly supports; Symptoms getting worse, or not getting better after about a week: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Very high temperature, or feels hot, cold or shivery: supports; Chest pain worse when breathing in: supports; Short of breath: supports |
| Lung cancer | 363358000 | very rare | Smokes, or has smoked in the past: strongly supports; Cough for 3 weeks or more: strongly supports; Losing weight without trying: supports; Coughing up blood: supports; Keeps getting chest infections, or one that is not getting better: supports; Hoarse voice: supports; Fingertips wider or rounder, with nails curving over (clubbing): supports; Feels very tired: supports; Short of breath: supports |
| Pneumonia (an infection deep in the lungs) | 233604007 | uncommon | Cough: strongly supports; Short of breath: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Chest pain worse when breathing in: supports; Yellow or green phlegm: supports; Aching body: supports |
| Tuberculosis (TB), an infection that usually affects the lungs | 154283005 | very rare | Cough for 3 weeks or more: strongly supports; Night sweats: strongly supports; Close contact with TB, or lived where TB is common: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Very high temperature, or feels hot, cold or shivery: supports; Coughing up blood: supports |
| Heart failure (the heart cannot pump blood as well as it should), or a flare of it | 84114007 | rare | Short of breath: strongly supports; Out of breath doing everyday things: strongly supports; Short of breath when lying flat: strongly supports; Swollen feet, ankles or legs: supports; Suddenly put on weight: supports; Heart failure symptoms worse than usual: supports; Frothy pink phlegm: supports; Cough worse at night: supports; Feels very tired: supports |
| Blood clot in the lung (pulmonary embolism) | 59282003 | rare | Short of breath: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: strongly supports; Chest pain worse when breathing in: strongly supports; Breathing very fast: supports; Heart beating very fast: supports; Pain or swelling in one leg: supports; Coughing up blood: supports; Chest pain is there now: strongly supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
