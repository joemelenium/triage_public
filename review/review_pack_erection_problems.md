# Review pack: Erection problems (erectile dysfunction)

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
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | 2026-11-19 |  | Page last reviewed: 28 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [The male menopause](https://www.nhs.uk/conditions/male-menopause/) | 2026-11-19 |  | Page last reviewed: 13 October 2022 |
| [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | 2026-11-19 |  | Page last reviewed: 29 July 2026 |
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

## Erection problems (erectile dysfunction) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ep_nerve_signs`<br>Erection problems with numbness around the genitals or bottom, or new weakness or numbness in both legs: possible cauda equina syndrome<br>**Note:** The Back pain page gives these with back pain. Applying them without back pain is AI judgement. | "Numb or no feeling around the genitals or bottom" OR "Numbness or weakness in both legs" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_ep_sudden_with_back_pain`<br>Erection problems that started suddenly, with back pain<br>**Note:** The Back pain page says call 999 or go to A&E for back pain with not being able to get or keep an erection. Requiring the erection problems to be new and sudden is an AI reading, so that long-standing erection problems in someone with back ache are not sent to A&E. | "Erection problems started suddenly in the last few days" AND "Back pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Erection problems (erectile dysfunction): other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ep_keep_happening`<br>Erection problems that keep happening | "Erection problems keep happening" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or go to a sexual health clinic. The source gives no fixed time.* | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |
| `or_ep_health_condition`<br>Erection problems in someone who smokes or has high blood pressure, diabetes or high cholesterol<br>**Note:** The page says erection problems may be caused by these conditions and might be a sign of a health condition that can be treated. | "Smokes, or has high blood pressure, diabetes or high cholesterol" OR "Has diabetes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |
| `or_ep_medicine`<br>Erection problems after starting or changing a medicine | "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Do not stop a prescribed medicine without talking to them.* | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |
| `or_ep_hormones_or_mood`<br>Erection problems with signs of low testosterone, or feeling low or hopeless<br>**Note:** The page lists depression and hormone problems as causes. The Male menopause page says see a GP for these symptoms. | "Less muscle, more fat on the tummy or chest, or low energy and mood swings" OR "Feeling low, sad or depressed" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |

## Default outcome

Used when no rule fires.

- **Erection problems now and then, with nothing else that needs help**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most men sometimes fail to get or keep an erection. See a GP if it keeps happening.*
- Source: [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Problems getting or keeping an erection | Do you have problems getting an erection, or keeping it for long enough to have sex? | 860914002 | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Erection problems started suddenly in the last few days | Did the erection problems start suddenly, in the last few days? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Back pain | Do you have back pain? | 161891005 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Erection problems keep happening | Do the erection problems keep happening, most times you try to have sex? |  | [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/) | |
| Smokes, or has high blood pressure, diabetes or high cholesterol | Do you smoke, or have high blood pressure, diabetes or high cholesterol? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Started a new medicine or changed a dose in the last few weeks | Have you started a new medicine, or changed the dose of one, in the last few weeks? |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Less muscle, more fat on the tummy or chest, or low energy and mood swings | Have you noticed less muscle, more fat around your tummy or chest, or low energy and mood swings? |  | [The male menopause](https://www.nhs.uk/conditions/male-menopause/) | |
| Feeling low, sad or depressed | Have you been feeling low, sad, hopeless or depressed? | 366979004 | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |

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

### `advice_back_nerves_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs that the nerves at the bottom of the spine are being squashed (cauda equina syndrome). This needs treatment in hospital straight away to prevent lasting damage.

**Look out for:**
- Numbness around your genitals or bottom getting worse
- Not being able to pee, or leaking pee or poo
- Weakness in your legs getting worse

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_erection_gp`

**What to do:** See a GP or go to a sexual health clinic. Erection problems that keep happening can be a sign of a health condition that can be treated, such as high blood pressure or diabetes.

**Look out for:**
- Chest pain when you are active
- Numbness around your genitals or bottom

**Get more help when:**
- Call 999 if you get chest pain that does not go away
- Call 999 or go to A&E if you get numbness around your genitals or bottom, or weakness in both legs

**Where to go:** Make an appointment with a GP, or go to a sexual health clinic.

**What you can do yourself:**
- Do not stop a prescribed medicine without talking to a doctor
- Stop smoking, and do not drink more than 14 units of alcohol a week
- Exercise and eat a healthy diet

Source: [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/)

### `advice_erection_self_care`

**What to do:** You can look after this yourself. Most men sometimes fail to get or keep an erection. It is usually from stress, tiredness or too much alcohol.

**Look out for:**
- Erection problems that keep happening

**Get more help when:**
- See a GP or go to a sexual health clinic if it keeps happening

**Where to go:** You do not need an appointment now. See a GP or sexual health clinic if it keeps happening.

**What you can do yourself:**
- Try to reduce stress
- Stop smoking, and do not drink more than 14 units of alcohol a week
- Lose weight if you need to, and exercise every day

Source: [Erectile dysfunction (impotence)](https://www.nhs.uk/conditions/erection-problems-erectile-dysfunction/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ep_nerve_signs`: The Back pain page gives these with back pain. Applying them without back pain is AI judgement.
- `rf_ep_sudden_with_back_pain`: The Back pain page says call 999 or go to A&E for back pain with not being able to get or keep an erection. Requiring the erection problems to be new and sudden is an AI reading, so that long-standing erection problems in someone with back ache are not sent to A&E.
- `or_ep_health_condition`: The page says erection problems may be caused by these conditions and might be a sign of a health condition that can be treated.
- `or_ep_hormones_or_mood`: The page lists depression and hormone problems as causes. The Male menopause page says see a GP for these symptoms.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Erection problems from narrow blood vessels or diabetes |  | common | Erection problems keep happening: strongly supports; Smokes, or has high blood pressure, diabetes or high cholesterol: strongly supports; Has diabetes: supports; Smokes, or has smoked in the past: supports |
| Low testosterone (male hormone) | 48723006 | uncommon | Less muscle, more fat on the tummy or chest, or low energy and mood swings: strongly supports; Feels very tired: supports; Feeling low, sad or depressed: supports; Low sex drive: supports |
| Prostate cancer | 399068003 | very rare | Hard to start peeing, or a weak or stop-start flow: supports; Getting up in the night to pee: supports; Losing weight without trying: strongly supports; Back pain: supports; Blood in semen: supports; Blood in pee: supports |
| Stress, tiredness, alcohol or relationship problems |  | common | Going through a stressful time or big life change: strongly supports; Problems in a relationship: supports; Still gets erections at other times, such as on waking: supports; Drinks a lot of alcohol: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
