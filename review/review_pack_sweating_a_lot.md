# Review pack: Sweating too much

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
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | 2026-11-19 |  | Page last reviewed: 07 November 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Overactive thyroid (hyperthyroidism)](https://www.nhs.uk/conditions/overactive-thyroid-hyperthyroidism/) | 2026-11-19 |  | Page last reviewed: 11 April 2023 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | 2026-11-19 |  | Page last reviewed: 19 July 2023 |
| [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | 2026-11-18 |  | Page last reviewed: 10 September 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |

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

## Sweating too much red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sw_chest_pain`<br>Sweating with chest pain<br>**Note:** The Chest pain page says call 999 for chest pain with sweating. A 'yes' to chest pain also brings in the chest pain entry symptom's own rules. | "Chest pain" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| `rf_sw_seriously_unwell`<br>Sweating with feeling very unwell and getting worse | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Sweating too much red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sw_temperature_unwell`<br>Sweating with a high temperature and feeling very unwell<br>**Note:** AI judgement: sweating with a high temperature and feeling very unwell suggests an infection rather than ordinary heavy sweating. | "Very high temperature, or feels hot, cold or shivery" AND "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Sweating too much: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sw_weight_loss`<br>Sweating with losing weight without trying, a fast heartbeat or a swelling in the front of the neck<br>**Note:** AI judgement: these can be signs of an overactive thyroid, an infection or, rarely, cancer. The Excessive sweating page says see a GP if another condition may be the cause. | "Losing weight without trying" OR "Swelling at the front of the neck" OR "Heart beating very fast" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP in the next few days* | **AI judgement, needs clinical review** | |
| `or_sw_gp`<br>Sweating that is not helped by self-care, has lasted 6 months, affects daily life, happens weekly or at night, runs in the family, or may be caused by a medicine<br>**Note:** The source says see a GP if you are sweating too much and any of these apply. | "Not better after treating it yourself, or keeps coming back" OR "Sweating too much for at least 6 months" OR "Affecting daily life, mood or self-esteem" OR "Sweating too much at least once a week" OR "Night sweats" OR "Sweating too much runs in the family" OR "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | |

## Default outcome

Used when no rule fires.

- **Sweating too much with nothing that needs a GP: try self-care, and a pharmacist can help**
- Outcome: Routine (help needed, timing not critical), Community pharmacy, No fixed time given in the source. *Speak to a pharmacist. The source gives no fixed time.*
- Source: [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Sweating too much | Do you sweat a lot more than you need to, even when you are not hot or exercising? | 52613005 | [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Swelling at the front of the neck | Do you have a swelling at the front of your neck? |  | [Overactive thyroid (hyperthyroidism)](https://www.nhs.uk/conditions/overactive-thyroid-hyperthyroidism/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Not better after treating it yourself, or keeps coming back | Has it not got better after treating it yourself, or does it keep coming back? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Sweating too much for at least 6 months | Have you been sweating too much for at least 6 months? |  | [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | |
| Affecting daily life, mood or self-esteem | Is it affecting your daily life, your mood or how you feel about yourself? |  | [Itchy skin](https://www.nhs.uk/symptoms/itchy-skin/) | |
| Sweating too much at least once a week | Does the heavy sweating happen at least once a week? |  | [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | |
| Night sweats | Do you have night sweats, where you wake up very sweaty? | 42984000 | [Tuberculosis (TB)](https://www.nhs.uk/conditions/tuberculosis-tb/) | |
| Sweating too much runs in the family | Does sweating too much run in your family? |  | [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |

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

### `advice_chest_pain_999`

**What to do:** Call 999 now. You could be having a heart attack and need treatment in hospital straight away.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- If you think you or someone else is having a heart attack, do these things while you wait for help.
- Sit and rest on the floor with your knees bent and your back supported. If you cannot do this, sit on a chair.
- Take aspirin (300mg) if you have any. Do not give aspirin to someone who has an aspirin allergy.
- If you have angina (chest pain caused by narrowed blood vessels to the heart), use your spray if you have it with you. It goes under your tongue. It may be called glyceryl trinitrate or GTN.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Angina](https://www.nhs.uk/conditions/angina/)

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

### `advice_condition_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment, or call 111 or use 111 online. Your answers suggest a problem that should be checked today.

**Look out for:**
- Symptoms that get worse quickly
- Severe difficulty breathing, passing out, or signs of a stroke

**Get more help when:**
- Call 999 or go to A&E if you get suddenly worse or get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: **AI judgement, needs clinical review**

### `advice_sweating_gp_soon`

**What to do:** See a GP in the next few days. Sweating with weight loss, a fast heartbeat or a swelling in the neck can be caused by another condition, such as an overactive thyroid, that needs tests.

**Look out for:**
- Night sweats, or a high temperature
- Losing more weight
- A racing heartbeat, or chest pain

**Get more help when:**
- Call 999 if you get chest pain
- Ask for an urgent GP appointment or call 111 if you feel very unwell

**Where to go:** Make an appointment with a GP for the next few days.

Source: **AI judgement, needs clinical review**, [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/), [Overactive thyroid (hyperthyroidism)](https://www.nhs.uk/conditions/overactive-thyroid-hyperthyroidism/)

### `advice_sweating_gp`

**What to do:** See a GP about your sweating. The source gives no fixed time. They may check for another cause, and can suggest stronger treatments.

**Look out for:**
- Night sweats
- Losing weight without trying
- A racing heartbeat

**Get more help when:**
- See a GP sooner if you also lose weight without trying

**Where to go:** Book an appointment with your GP surgery. A pharmacist can suggest products in the meantime.

**What you can do yourself:**
- Wear loose clothes, and avoid tight clothes and nylon
- Change your socks at least twice a day, and wear leather shoes
- Use a strong antiperspirant instead of a deodorant

Source: [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/)

### `advice_sweating_pharmacy`

**What to do:** Speak to a pharmacist. They can suggest stronger antiperspirants, sweat shields, foot powders and gentle soap substitutes.

**Look out for:**
- Self-care not helping, or sweating lasting 6 months or more
- Sweating at night, or sweating that stops you doing everyday things

**Get more help when:**
- See a GP if any of these happen, if it runs in your family, or if you take a medicine that may cause it

**Where to go:** Go to a pharmacy. You do not need an appointment.

**What you can do yourself:**
- Wear loose clothes, and avoid tight clothes and nylon
- Avoid alcohol and spicy food if they make it worse

Source: [Excessive sweating (hyperhidrosis)](https://www.nhs.uk/conditions/excessive-sweating-hyperhidrosis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sw_chest_pain`: The Chest pain page says call 999 for chest pain with sweating. A 'yes' to chest pain also brings in the chest pain entry symptom's own rules.
- `rf_sw_temperature_unwell`: AI judgement: sweating with a high temperature and feeling very unwell suggests an infection rather than ordinary heavy sweating.
- `or_sw_weight_loss`: AI judgement: these can be signs of an overactive thyroid, an infection or, rarely, cancer. The Excessive sweating page says see a GP if another condition may be the cause.
- `or_sw_gp`: The source says see a GP if you are sweating too much and any of these apply.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Overactive thyroid (the thyroid gland in the neck makes too much hormone) | 34486009 | rare | Feeling restless, shaky or too hot all the time: strongly supports; Losing weight without trying: strongly supports; Heart racing, slow, skipping or fluttering: supports; Feels sweaty: supports; Feels very tired: supports; Night sweats: supports; Heart beating very fast: supports; Swelling at the front of the neck: supports; Feeling anxious, worried or panicky: supports; Shaking or trembling (tremor): supports |
| Hyperhidrosis (sweating more than the body needs to, with no other cause) | 312230002 | uncommon | Sweating mainly in the armpits, hands, feet or face: strongly supports; Sweating too much for at least 6 months: supports; Sweating too much runs in the family: supports; Feet sweat a lot: supports |
| Perimenopause or menopause (when periods change and then stop) | 289903006 | uncommon | Hot flushes: strongly supports; Trouble sleeping (insomnia): supports; Feeling low, sad or depressed: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports; Feels very tired: supports; Night sweats: supports; Vaginal dryness: supports; Irregular periods: supports; Periods stopped for 12 months or more (the menopause): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
