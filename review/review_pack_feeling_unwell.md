# Review pack: Feeling generally unwell

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
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | 2026-11-19 |  | Page last reviewed: 03 January 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
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

## Feeling generally unwell red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_gu_sepsis_skin_or_rash`<br>Unwell with blotchy skin, or a rash that does not fade when pressed: possible sepsis or meningitis | "Blotchy or mottled skin" OR "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_gu_drowsy`<br>Unwell and so drowsy they are hard to wake or cannot stay awake, or a child who is floppy or not responding as usual | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_gu_stiff_neck`<br>Unwell with a stiff neck: possible meningitis | "Stiff neck" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_gu_fast_breathing_with_infection`<br>Unwell and breathing very fast, with a high temperature or feeling very unwell: possible sepsis<br>**Note:** As in the breathlessness rule, requiring a high temperature or feeling very unwell is AI judgement, so that fast breathing from a panic attack is not sent to A&E on its own. | "Breathing very fast" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_gu_cold_skin`<br>Unwell, with hands and feet or skin unusually cold or clammy<br>**Note:** The Sepsis page says call 999 or go to A&E for feeling cold to the touch. Soft, as in the breathlessness rule. | "Hands and feet, or skin, unusually cold to touch" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_gu_seriously_unwell`<br>Very unwell and getting worse, or feels something is seriously wrong<br>**Note:** The Sepsis page says trust your instincts. Soft, as in the cough and breathlessness rules. | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Feeling generally unwell red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_gu_fast_breathing`<br>Unwell and breathing very fast<br>**Note:** AI judgement, as in the breathlessness rule. With a high temperature or feeling very unwell the emergency rule above applies. | "Breathing very fast" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | **AI judgement, needs clinical review** | |
| `rf_gu_not_peed`<br>Unwell and no pee for 12 hours or more<br>**Note:** For children under 5 the dehydration and high temperature rules send this to A&E, as the Sepsis page says. | "No pee for 12 hours or more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | |
| `rf_gu_cannot_keep_fluids_down`<br>Unwell and cannot keep fluids down<br>**Note:** Clinical knowledge: someone who cannot keep fluids down will soon lack water in the body, and it can be a sign of diabetic ketoacidosis. | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Feeling generally unwell: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_gu_feels_very_unwell`<br>Feels very unwell<br>**Note:** AI judgement: feeling very unwell without a clear cause should be checked the same day. Soft, so that likely flu or a viral illness can lower it. | "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | **AI judgement, needs clinical review** | |
| `or_gu_not_getting_better`<br>Unwell and getting worse, or not getting better after about a week | "Symptoms getting worse, or not getting better after about a week" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **Feeling generally unwell with nothing that needs more help: see a GP if it does not settle**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP if you are not getting better. The source gives no fixed time.*
- Source: **AI judgement, needs clinical review**
- **Note:** AI judgement. Soft: a likely viral illness lowers it to self-care.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feeling generally unwell | Do you feel generally unwell, without one main symptom? |  | **AI judgement, needs clinical review** | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Hands and feet, or skin, unusually cold to touch | Are your hands and feet, or your skin, unusually cold to touch, or cold and damp (clammy)? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Symptoms getting worse, or not getting better after about a week | Are your symptoms getting worse? Or have they not started to get better after about a week? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |

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

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

### `advice_meningitis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of meningitis (an infection of the layers around the brain) or sepsis (a life-threatening reaction to an infection). They need treatment in hospital straight away.

**Look out for:**
- A rash that does not fade when you press a glass against it. On brown or black skin, check paler areas such as the palms of the hands.
- Being very sleepy, confused or hard to wake
- A seizure (fit)
- In a baby: being floppy, not feeding, or a high-pitched cry
- Skin, lips or tongue turning blue, grey, pale or blotchy

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Do not wait for a rash. Get help if you are worried, even if there is no rash.
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive yourself to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Meningitis](https://www.nhs.uk/conditions/meningitis/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_unwell_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment, or call 111 or use 111 online.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue turning blue, grey, pale or blotchy, or a rash that does not fade when pressed
- Becoming confused, very sleepy or hard to wake
- Not peeing all day

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_unwell_gp`

**What to do:** See a GP if you are not getting better, or you are worried. Most short illnesses get better on their own.

**Look out for:**
- A high temperature, or feeling hot, cold or shivery
- Pain when peeing, or not peeing much
- Feeling very thirsty, or losing weight
- Getting worse instead of better

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you feel very unwell or get worse
- Call 999 or go to A&E if you are breathing very fast, have blotchy skin, or become very sleepy or confused
- Call 999 or go to A&E for a rash that does not fade when you press a glass on it

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Rest and drink plenty of fluids

Source: **AI judgement, needs clinical review**, [Sepsis](https://www.nhs.uk/conditions/sepsis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_gu_fast_breathing_with_infection`: As in the breathlessness rule, requiring a high temperature or feeling very unwell is AI judgement, so that fast breathing from a panic attack is not sent to A&E on its own.
- `rf_gu_cold_skin`: The Sepsis page says call 999 or go to A&E for feeling cold to the touch. Soft, as in the breathlessness rule.
- `rf_gu_seriously_unwell`: The Sepsis page says trust your instincts. Soft, as in the cough and breathlessness rules.
- `rf_gu_fast_breathing`: AI judgement, as in the breathlessness rule. With a high temperature or feeling very unwell the emergency rule above applies.
- `rf_gu_not_peed`: For children under 5 the dehydration and high temperature rules send this to A&E, as the Sepsis page says.
- `rf_gu_cannot_keep_fluids_down`: Clinical knowledge: someone who cannot keep fluids down will soon lack water in the body, and it can be a sign of diabetic ketoacidosis.
- `or_gu_feels_very_unwell`: AI judgement: feeling very unwell without a clear cause should be checked the same day. Soft, so that likely flu or a viral illness can lower it.
- `feeling_unwell default outcome`: AI judgement. Soft: a likely viral illness lowers it to self-care.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| COVID-19 | 840539006 | uncommon | Lost or changed sense of smell or taste: supports; Very high temperature, or feels hot, cold or shivery: supports; Dry cough: supports; Aching body: supports; Feels very tired: supports; Blocked or runny nose: supports |
| Flu | 6142004 | uncommon | Very high temperature, or feels hot, cold or shivery: strongly supports; Aching body: strongly supports; Feels very tired: supports; Dry cough: supports; Feels very unwell: supports |
| Pneumonia (an infection deep in the lungs) | 233604007 | uncommon | Cough: strongly supports; Short of breath: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Coughing up yellow or green phlegm, or a high temperature: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Chest pain worse when breathing in: supports; Yellow or green phlegm: supports; Aching body: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Diabetic ketoacidosis (DKA). This is when a lack of insulin makes you very ill. | 420422005 | rare | Breath smells fruity: strongly supports; Breathing faster and more deeply than usual: strongly supports; Blood sugar high and not coming down, or ketones raised: strongly supports; Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Keeps being sick and cannot keep fluids down: supports; Stomach ache: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Being sick: strongly supports; High ketones, or high blood sugar that insulin is not bringing down: strongly supports; Breathing very fast: supports; Losing weight without trying: supports; Feels very tired: supports |
| Heat exhaustion | 95868006 | uncommon | Unwell after being in the heat or exercising hard: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Feels sick or has been sick: supports; Feeling very thirsty all the time: supports; Feels very tired: supports; Signs of dehydration: supports |
| Heatstroke (the body overheating dangerously) | 52072009 | rare | Unwell after being in the heat or exercising hard: strongly supports; Hot skin that is not sweating: strongly supports; Still unwell after 30 minutes of cooling down: strongly supports; Suddenly confused: supports; Has had a seizure (fit): supports; Breathing very fast: supports; Heart beating very fast: supports |
| Malaria (an infection spread by mosquito bites) | 61462000 | rare | Been to a country where malaria is found in the last year: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels cold to the touch, or shivery: supports; Aching body: supports; Feels sick or has been sick: supports; Very painful headache: supports; Diarrhoea, or being sick: supports |
| Serious dehydration (not having enough water in the body) |  | uncommon | Keeps being sick and cannot keep fluids down: strongly supports; Dizzy when standing up, and it does not go away: strongly supports; No pee for 12 hours or more: strongly supports; Heart beating very fast: supports; Child with dry nappies, sunken eyes or no tears: supports; Baby's soft spot on top of the head sinks inwards: supports; Diarrhoea, or being sick: supports; Feels very tired: supports; Child limp, floppy, hard to wake or not responding as usual: supports |
| Viral infection (such as a cold, a tummy bug or another virus) | 34014006 | common | Blocked or runny nose: strongly supports; Aching body: supports; Cough: supports; Diarrhoea, or being sick: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
