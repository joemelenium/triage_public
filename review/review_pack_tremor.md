# Review pack: Tremor or shaking hands

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
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | 2026-11-19 |  | Page last reviewed: 14 November 2023 |
| [Parkinson's disease](https://www.nhs.uk/conditions/parkinsons-disease/) | 2026-11-19 |  | Page last reviewed: 03 November 2022 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |

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

## Tremor or shaking hands red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tr_sepsis`<br>Shivering or shaking, with feeling very unwell or breathing very fast: possible sepsis<br>**Note:** Same reading as the breathlessness rule. Someone may describe the shivering of a high temperature as shaking. The Sepsis page says call 999 or go to A&E for an adult who is shivery. Requiring feeling very unwell or breathing very fast is AI judgement. | "Feels cold to the touch, or shivery" AND ("Feels very unwell" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Tremor or shaking hands red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tr_low_sugar`<br>Diabetes and signs of low blood sugar (a hypo) | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Treat the low blood sugar now. If it does not improve, get help from NHS 111, or call 999 if the person becomes drowsy or confused.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Tremor or shaking hands: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_tr_getting_worse`<br>A tremor that is getting worse over time | "Tremor getting worse over time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |
| `or_tr_daily_life`<br>A tremor that is affecting daily activities | "Tremor affecting daily activities" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |
| `or_tr_slow_or_stiff`<br>A tremor with movements becoming slower or stiffer | "Movements becoming slower or stiffer" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Parkinson's disease](https://www.nhs.uk/conditions/parkinsons-disease/) | |
| `or_tr_new_medicine`<br>A tremor that started after a new medicine | "Started a new medicine or changed a dose in the last few weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Do not stop a prescribed medicine without advice.* | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |

## Default outcome

Used when no rule fires.

- **A mild tremor with nothing that needs more help: often more noticeable with stress, tiredness or caffeine**
- Outcome: Self-manageable, Self-care, No appointment needed. *A slight tremor is normal. See a GP if it gets worse or affects your daily life.*
- Source: [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Shaking or trembling (tremor) | Do you have shaking or trembling that you cannot control, for example in your hands? | 26079004 | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Feels cold to the touch, or shivery | Do you feel cold to the touch, or are you shivering or shivery? This can happen even without a high temperature. |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |
| Tremor getting worse over time | Is the shaking getting worse over time? |  | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |
| Tremor affecting daily activities | Does the shaking make it hard to do things like eat, drink or write? |  | [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/) | |
| Movements becoming slower or stiffer | Have your movements become slower or stiffer? For example, when walking, getting dressed or writing. |  | [Parkinson's disease](https://www.nhs.uk/conditions/parkinsons-disease/) | |
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

### `advice_low_blood_sugar`

**What to do:** Treat the low blood sugar now. Have something sugary straight away, such as a small glass of fruit juice or a sugary fizzy drink, or glucose tablets. Check your blood sugar again after 10 to 15 minutes.

**Look out for:**
- Blood sugar still below 4 after treating it twice
- Getting confused, very drowsy or hard to wake
- A seizure (fit)

**Get more help when:**
- Once you feel better, eat something like biscuits or a sandwich to keep your sugar up
- Get help from NHS 111 or your diabetes team if it does not get better, or you keep having hypos
- Call 999 if the person stops responding as usual or has a seizure. Do not give them food or drink if they are not fully awake.

**Where to go:** Treat it yourself first. For help call 111 or use 111 online, or contact your diabetes team. In an emergency call 999.

**What you can do yourself:**
- Always carry something sugary with you
- Do not drive for at least 45 minutes after your blood sugar is back to normal

Source: [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/)

### `advice_tremor_gp`

**What to do:** See a GP about your tremor. They can check what is causing it, and treatment may help.

**Look out for:**
- The shaking getting worse, or spreading
- Movements getting slower or stiffer

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if it starts suddenly and you feel very unwell

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Cut down on caffeine and alcohol
- Do not stop taking a prescribed medicine without talking to a doctor first

Source: [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/), [Parkinson's disease](https://www.nhs.uk/conditions/parkinsons-disease/)

### `advice_tremor_self_care`

**What to do:** A slight tremor is normal. It is often more noticeable when you are stressed, tired, cold, or after caffeine, alcohol or smoking.

**Look out for:**
- The shaking getting worse over time
- The shaking making it hard to eat or write

**Get more help when:**
- See a GP if your tremor is getting worse or affecting your daily life

**Where to go:** You do not need an appointment now. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Cut down on tea, coffee, cola and energy drinks
- Try to relax and get enough sleep

Source: [Essential tremor](https://www.nhs.uk/symptoms/tremor-or-shaking-hands/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_tr_sepsis`: Same reading as the breathlessness rule. Someone may describe the shivering of a high temperature as shaking. The Sepsis page says call 999 or go to A&E for an adult who is shivery. Requiring feeling very unwell or breathing very fast is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Essential tremor (shaking hands that often runs in families) | 609558009 | common | Shaking worst when holding the hands out or using them: strongly supports; Close family member also has a tremor: supports; Tremor getting worse over time: supports; Tremor affecting daily activities: supports |
| Low blood sugar (hypoglycaemia, a hypo) | 302866003 | rare | Has diabetes: strongly supports; Signs of low blood sugar in someone with diabetes: strongly supports; Feels sweaty: supports; Shaking or trembling (tremor): supports; Feels light-headed: supports; Suddenly confused: supports; Tingling or pins and needles in the fingers or around the mouth: supports; Heart racing, slow, skipping or fluttering: supports |
| Parkinson's | 49049000 | uncommon | Shaking worst when the hand is resting, often on one side: strongly supports; Movements becoming slower or stiffer: strongly supports; Finding it hard to balance or walk: supports; Tremor getting worse over time: supports |
| Shaking from stress, tiredness, caffeine or alcohol |  | very common | Shaking worse with stress, tiredness, caffeine, alcohol or smoking: strongly supports; Having a lot of caffeine or alcohol: supports; Going through a stressful time or big life change: supports; Sudden rush of intense fear or panic: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Overactive thyroid (the thyroid gland in the neck makes too much hormone) | 34486009 | rare | Feeling restless, shaky or too hot all the time: strongly supports; Losing weight without trying: strongly supports; Heart racing, slow, skipping or fluttering: supports; Feels sweaty: supports; Feels very tired: supports; Night sweats: supports; Heart beating very fast: supports; Swelling at the front of the neck: supports; Feeling anxious, worried or panicky: supports; Shaking or trembling (tremor): supports |
| Alcohol withdrawal (symptoms after stopping or cutting down drinking) | 191480000 | rare | Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days: strongly supports; Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep: strongly supports; Drinks a lot of alcohol: strongly supports; Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feeling anxious, worried or panicky: supports; Hearing, seeing or feeling things that other people do not: supports; Shaking or trembling (tremor): supports; Has had a seizure (fit): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
