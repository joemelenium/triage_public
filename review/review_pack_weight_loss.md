# Review pack: Unintentional weight loss

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
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/) | 2026-11-19 |  | Page last reviewed: 28 July 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Jaundice](https://www.nhs.uk/conditions/jaundice/) | 2026-11-19 |  | Page last reviewed: 22 January 2024 |
| [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | 2026-11-18 |  | Page last reviewed: 10 September 2026 |
| [Hodgkin lymphoma: symptoms](https://www.nhs.uk/conditions/hodgkin-lymphoma/symptoms/) | 2026-11-19 |  | Page last reviewed: 14 October 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Liver disease](https://www.nhs.uk/conditions/liver-disease/) | 2026-11-19 |  | Page last reviewed: 09 August 2023 |
| [Cancer symptoms](https://www.nhs.uk/conditions/cancer/) | 2026-11-19 |  | Page last reviewed: 27 May 2025 |
| [Night sweats](https://www.nhs.uk/symptoms/night-sweats/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |

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

## Unintentional weight loss red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wl_ketoacidosis_signs`<br>Weight loss with breath that smells fruity or breathing faster and more deeply than usual: possible diabetic ketoacidosis | "Breath smells fruity" OR "Breathing faster and more deeply than usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_wl_drowsy`<br>Weight loss and so drowsy they are hard to wake or cannot stay awake<br>**Note:** The Type 1 diabetes page says call 999 or go to A&E for feeling sleepy or confused with the symptoms of diabetes. Applying it to anyone losing weight is AI judgement. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_wl_thirsty_and_being_sick`<br>Weight loss, very thirsty and peeing more, and being sick: possible diabetic ketoacidosis | "Feeling very thirsty all the time" AND "Peeing more often than usual" AND "Keeps being sick and cannot keep fluids down" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Unintentional weight loss red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wl_type_1_diabetes`<br>Weight loss with feeling very thirsty and peeing more: possible type 1 diabetes<br>**Note:** Three of the 4 Ts (toilet, thirsty, thinner). The page says an urgent GP appointment or 111 if you think you have type 1 diabetes. | "Feeling very thirsty all the time" AND "Peeing more often than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_wl_yellow_skin`<br>Weight loss with yellow skin or yellow whites of the eyes<br>**Note:** Clinical knowledge: new yellowing of the skin or eyes (jaundice) with weight loss can be a blocked bile duct or cancer of the pancreas or liver and should be checked the same day. The skin and hair body system owns the jaundice page. | "Yellow skin or yellow whites of the eyes (jaundice)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Unintentional weight loss: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_wl_with_other_symptoms`<br>Weight loss with other symptoms, such as night sweats, a lump, losing your appetite, or losing a lot of weight quickly<br>**Note:** The page says it is important to see a GP as soon as possible if you have weight loss and other symptoms. 'As soon as possible' is mapped to soon. Which symptoms count is AI judgement. | "Night sweats" OR "A painless lump or swelling in the neck, armpit or groin" OR "Not feeling hungry, or eating much less than usual" OR "Lost a lot of weight quickly" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP as soon as possible* | [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/) | |

## Default outcome

Used when no rule fires.

- **Losing weight without trying: see a GP just in case**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/)
- **Note:** The page says to see a GP just in case, so likely conditions can never take the outcome below this.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Yellow skin or yellow whites of the eyes (jaundice) | Have your skin or the whites of your eyes turned yellow? | 18165001 | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| Night sweats | Do you have night sweats, where you wake up very sweaty? | 42984000 | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| A painless lump or swelling in the neck, armpit or groin | Do you have a painless lump or swelling in your neck, armpit or groin that has lasted more than 2 weeks? |  | [Hodgkin lymphoma: symptoms](https://www.nhs.uk/conditions/hodgkin-lymphoma/symptoms/) | |
| Not feeling hungry, or eating much less than usual | Have you lost your appetite, or are you eating much less than usual? | 79890006 | [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/) | |
| Lost a lot of weight quickly | Have you lost a lot of weight in the last few months, such as a stone (6kg) or more, or your clothes no longer fit? |  | **AI judgement, needs clinical review** | |

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

### `advice_ketoacidosis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of diabetic ketoacidosis, a life-threatening problem from a lack of insulin. It can happen to people who do not know they have diabetes.

**Look out for:**
- Becoming confused, very sleepy or hard to wake
- Breathing that gets faster and deeper
- Being sick again and again

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines and insulin you take.

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/), [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_type_1_diabetes_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Being very thirsty, peeing more, feeling tired and losing weight can be signs of type 1 diabetes, which needs treatment quickly.

**Look out for:**
- Tummy pain, or feeling or being sick
- Breath that smells fruity, like pear drops or nail polish remover
- Breathing faster and more deeply than usual
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 or go to A&E if you or your child get any of the signs above, or get worse quickly

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. It can help to take a sample of pee with you. In an emergency call 999.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_weight_loss_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Weight loss with yellow skin or eyes needs to be checked quickly.

**Look out for:**
- Pale poo or dark pee
- Tummy pain, or a high temperature with shivering
- Feeling confused or very sleepy

**Get more help when:**
- Call 999 or go to A&E if you get severe tummy pain, or become confused or very sleepy

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: **AI judgement, needs clinical review**, [Liver disease](https://www.nhs.uk/conditions/liver-disease/)

### `advice_weight_loss_soon`

**What to do:** See a GP as soon as possible, ideally in the next few days. Weight loss or night sweats with other symptoms should be checked early, so that any cause is found and treated sooner.

**Look out for:**
- Losing weight faster
- New symptoms, such as a lump, coughing up blood, or yellow skin or eyes

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get worse before you are seen
- Call 999 or go to A&E in an emergency

**Where to go:** Make an appointment with a GP in the next few days. For urgent help call 111 or use 111 online.

Source: [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/), [Cancer symptoms](https://www.nhs.uk/conditions/cancer/), [Night sweats](https://www.nhs.uk/symptoms/night-sweats/)

### `advice_weight_loss_gp`

**What to do:** See a GP. Losing weight without trying should be checked, just in case.

**Look out for:**
- Other symptoms, such as night sweats, a lump, losing your appetite, or losing a lot of weight quickly
- Being very thirsty and peeing more than usual
- Yellow skin or eyes

**Get more help when:**
- See a GP as soon as possible if you get other symptoms
- Ask for an urgent GP appointment or call 111 if you are very thirsty and peeing more, or your skin or eyes turn yellow

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

Source: [Unintentional weight loss](https://www.nhs.uk/symptoms/unintentional-weight-loss/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_wl_drowsy`: The Type 1 diabetes page says call 999 or go to A&E for feeling sleepy or confused with the symptoms of diabetes. Applying it to anyone losing weight is AI judgement.
- `rf_wl_type_1_diabetes`: Three of the 4 Ts (toilet, thirsty, thinner). The page says an urgent GP appointment or 111 if you think you have type 1 diabetes.
- `rf_wl_yellow_skin`: Clinical knowledge: new yellowing of the skin or eyes (jaundice) with weight loss can be a blocked bile duct or cancer of the pancreas or liver and should be checked the same day. The skin and hair body system owns the jaundice page.
- `or_wl_with_other_symptoms`: The page says it is important to see a GP as soon as possible if you have weight loss and other symptoms. 'As soon as possible' is mapped to soon. Which symptoms count is AI judgement.
- `weight_loss default outcome`: The page says to see a GP just in case, so likely conditions can never take the outcome below this.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Lung cancer | 363358000 | very rare | Smokes, or has smoked in the past: strongly supports; Cough for 3 weeks or more: strongly supports; Losing weight without trying: supports; Coughing up blood: supports; Keeps getting chest infections, or one that is not getting better: supports; Hoarse voice: supports; Fingertips wider or rounder, with nails curving over (clubbing): supports; Feels very tired: supports; Short of breath: supports |
| Tuberculosis (TB), an infection that usually affects the lungs | 154283005 | very rare | Cough for 3 weeks or more: strongly supports; Night sweats: strongly supports; Close contact with TB, or lived where TB is common: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Very high temperature, or feels hot, cold or shivery: supports; Coughing up blood: supports |
| Cancer | 363346000 | rare | Lost a lot of weight quickly: strongly supports; Not feeling hungry, or eating much less than usual: supports; Feels very tired: supports; A painless lump or swelling in the neck, armpit or groin: supports; Night sweats: supports; Losing weight without trying: supports; Yellow skin or yellow whites of the eyes (jaundice): supports; Smokes, or has smoked in the past: supports |
| HIV (a virus that makes it harder to fight infection) | 86406008 | rare | Might have been exposed to HIV: strongly supports; Losing weight without trying: supports; Night sweats: supports; Very high temperature, or feels hot, cold or shivery: supports; A painless lump or swelling in the neck, armpit or groin: supports; Rash or spots on the skin: supports |
| Lymphoma (a cancer of the lymph glands) | 118600007 | rare | A painless lump or swelling in the neck, armpit or groin: strongly supports; Night sweats: strongly supports; Losing weight without trying: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports; Swollen gland is painless: strongly supports; Glands getting bigger, or not gone down after 1 week: strongly supports; Glands feel hard, or do not move when pressed: supports; Swollen glands with no other signs of being ill: supports |
| Overactive thyroid (the thyroid gland in the neck makes too much hormone) | 34486009 | rare | Feeling restless, shaky or too hot all the time: strongly supports; Losing weight without trying: strongly supports; Heart racing, slow, skipping or fluttering: supports; Feels sweaty: supports; Feels very tired: supports; Night sweats: supports; Heart beating very fast: supports; Swelling at the front of the neck: supports; Feeling anxious, worried or panicky: supports; Shaking or trembling (tremor): supports |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Liver problems (such as liver damage from alcohol) | 235856003 | rare | Yellow skin or yellow whites of the eyes (jaundice): strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Not feeling hungry, or eating much less than usual: supports; Feels very tired: supports; Losing weight without trying: supports; Feels sick or has been sick: supports; Swollen feet, ankles or legs: supports; Pale poo and dark pee: strongly supports; Pain in the upper right of the tummy, just under the ribs: supports; Drinks a lot of alcohol: supports; Feeling sick (nausea): supports; Itchy skin on other parts of the body too: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
