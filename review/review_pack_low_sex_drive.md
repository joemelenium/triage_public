# Review pack: Low sex drive (loss of libido)

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
| [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | 2026-11-19 |  | Page last reviewed: 26 May 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Irregular periods](https://www.nhs.uk/symptoms/irregular-periods/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | 2026-11-19 |  | Page last reviewed: 29 July 2026 |
| [The male menopause](https://www.nhs.uk/conditions/male-menopause/) | 2026-11-19 |  | Page last reviewed: 13 October 2022 |
| [Menopause](https://www.nhs.uk/conditions/menopause-and-perimenopause/) | 2026-11-19 |  |  |
| [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
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

## Low sex drive (loss of libido): other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ls_worried`<br>Worried about a low sex drive, or it is affecting life or a relationship | "Worried about low sex drive" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| `or_ls_medicine`<br>Taking a medicine or hormonal contraception that may be affecting sex drive | "Started a new medicine or changed a dose in the last few weeks" OR "Takes antidepressants or blood pressure medicine" OR "Uses hormonal contraception" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Do not stop a prescribed medicine or contraception without talking to them.* | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| `or_ls_after_baby`<br>Sex drive has not come back since having a baby | "Sex drive has not come back since having a baby" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| `or_ls_low_mood_or_hormones`<br>Low sex drive with feeling low or hopeless, or signs of low testosterone<br>**Note:** The page lists depression and lower hormone levels as causes. The Male menopause page says see a GP for these symptoms. | "Feeling low, sad or depressed" OR "Less muscle, more fat on the tummy or chest, or low energy and mood swings" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| `or_ls_menopause`<br>Low sex drive with hot flushes or periods changing or stopping: possible menopause<br>**Note:** The page lists lower hormone levels during the menopause as a cause, treated with HRT from a GP. Sending everyone with these signs to a GP is a reading of that. | "Hot flushes" OR "Periods have changed: irregular, heavier, more painful or stopped" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |

## Default outcome

Used when no rule fires.

- **Low sex drive with nothing that needs help now**
- Outcome: Self-manageable, Self-care, No appointment needed. *See a GP if you are worried about it*
- Source: [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Low sex drive | Have you lost interest in sex, or has your sex drive gone down? |  | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Worried about low sex drive | Are you worried about your low sex drive, or is it affecting your life or relationship? |  | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Takes antidepressants or blood pressure medicine | Do you take antidepressants, or medicine for high blood pressure? |  | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| Uses hormonal contraception | Do you use hormonal contraception? For example, the pill, the implant, the injection or a hormonal coil (IUS). |  | [Irregular periods](https://www.nhs.uk/symptoms/irregular-periods/) | |
| Sex drive has not come back since having a baby | Has your sex drive not come back since having a baby? |  | [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/) | |
| Feeling low, sad or depressed | Have you been feeling low, sad, hopeless or depressed? | 366979004 | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |
| Less muscle, more fat on the tummy or chest, or low energy and mood swings | Have you noticed less muscle, more fat around your tummy or chest, or low energy and mood swings? |  | [The male menopause](https://www.nhs.uk/conditions/male-menopause/) | |
| Hot flushes | Do you get hot flushes? These are sudden feelings of heat in your face, neck or chest. |  | [Menopause](https://www.nhs.uk/conditions/menopause-and-perimenopause/) | |
| Periods have changed: irregular, heavier, more painful or stopped | Have your periods changed? For example, they have become irregular, heavier or more painful, or they have stopped. |  | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |

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

### `advice_low_sex_drive_gp`

**What to do:** See a GP. Treating the cause should help your sex drive. A GP can check your medicines, hormones and mood.

**Look out for:**
- Feeling low or hopeless most of the time
- Thoughts of harming yourself

**Get more help when:**
- If you are struggling with how you feel, call Samaritans on 116 123 at any time, or call 111 and choose the mental health option
- Call 999 or go to A&E if you feel you may harm yourself

**Where to go:** Make an appointment with a GP.

**What you can do yourself:**
- Do not stop a medicine or your contraception without talking to a doctor first
- Cut down on alcohol

Source: [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/), [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

### `advice_low_sex_drive_self_care`

**What to do:** You can look after this yourself for now. Sex drive often goes up and down with stress, tiredness and relationships.

**Look out for:**
- Feeling low or hopeless
- Being worried about it, or it affecting your relationship

**Get more help when:**
- See a GP if you are worried, or think a medicine may be the cause
- If you are struggling with how you feel, call Samaritans on 116 123 at any time

**Where to go:** You do not need an appointment now. See a GP if you are worried.

**What you can do yourself:**
- Talk to your partner about it, if you have one
- Cut down on alcohol, and try to reduce stress

Source: [Low sex drive (loss of libido)](https://www.nhs.uk/symptoms/loss-of-libido/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `or_ls_low_mood_or_hormones`: The page lists depression and lower hormone levels as causes. The Male menopause page says see a GP for these symptoms.
- `or_ls_menopause`: The page lists lower hormone levels during the menopause as a cause, treated with HRT from a GP. Sending everyone with these signs to a GP is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Low testosterone (male hormone) | 48723006 | uncommon | Less muscle, more fat on the tummy or chest, or low energy and mood swings: strongly supports; Feels very tired: supports; Feeling low, sad or depressed: supports; Low sex drive: supports |
| Stress, tiredness, alcohol or relationship problems |  | common | Going through a stressful time or big life change: strongly supports; Problems in a relationship: supports; Still gets erections at other times, such as on waking: supports; Drinks a lot of alcohol: supports |
| Perimenopause or menopause (when periods change and then stop) | 289903006 | uncommon | Hot flushes: strongly supports; Trouble sleeping (insomnia): supports; Feeling low, sad or depressed: supports; Periods have changed: irregular, heavier, more painful or stopped: strongly supports; Feels very tired: supports; Night sweats: supports; Vaginal dryness: supports; Irregular periods: supports; Periods stopped for 12 months or more (the menopause): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
