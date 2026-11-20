# Review pack: Insomnia

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
| [Insomnia](https://www.nhs.uk/conditions/insomnia/) | 2026-11-19 |  | Page last reviewed: 19 March 2024 |
| [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/) | 2026-11-19 |  | Page last reviewed: 11 May 2026 |
| [Restless legs syndrome](https://www.nhs.uk/conditions/restless-legs-syndrome/) | 2026-11-19 |  | Page last reviewed: 22 September 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Snoring](https://www.nhs.uk/symptoms/snoring/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
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

## Insomnia: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_in_months`<br>Trouble sleeping for months | "Trouble sleeping for 3 months or more" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| `or_in_hard_to_cope`<br>Insomnia making it hard to cope with daily life | "Lack of sleep making daily life hard to cope with" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| `or_in_habits_not_helped`<br>Changing sleeping habits has not helped | "Changing sleeping habits has not helped" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| `or_in_breathing_in_sleep`<br>Loud snoring, or breathing that stops and starts while asleep | "Breathing stops and starts during sleep, or gasping or choking noises" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/) | |
| `or_in_restless_legs`<br>Restless legs stopping you sleeping<br>**Note:** The Restless legs syndrome page says see a GP if it is stopping you sleeping. | "Strong urge to move the legs, mostly in the evening or at night" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Restless legs syndrome](https://www.nhs.uk/conditions/restless-legs-syndrome/) | |

## Default outcome

Used when no rule fires.

- **Trouble sleeping with nothing that needs more help: it usually gets better by changing sleeping habits**
- Outcome: Self-manageable, Self-care, No appointment needed. *Insomnia usually gets better by changing your sleeping habits. A pharmacist can also help.*
- Source: [Insomnia](https://www.nhs.uk/conditions/insomnia/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Trouble sleeping (insomnia) | Do you regularly have trouble getting to sleep, staying asleep, or wake up too early? | 301345002 | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Trouble sleeping for 3 months or more | Have you had trouble sleeping for 3 months or more? |  | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| Lack of sleep making daily life hard to cope with | Is the lack of sleep making it hard for you to cope with daily life? |  | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| Changing sleeping habits has not helped | Have you tried changing your sleeping habits, and it has not helped? |  | [Insomnia](https://www.nhs.uk/conditions/insomnia/) | |
| Breathing stops and starts during sleep, or gasping or choking noises | Does your breathing stop and start while you sleep, or do you make gasping or choking noises? Someone else may have noticed this. |  | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| Strong urge to move the legs, mostly in the evening or at night | Do you get a strong need to move your legs, with odd feelings in them? Is it mostly in the evening or at night? |  | [Restless legs syndrome](https://www.nhs.uk/conditions/restless-legs-syndrome/) | |

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

### `advice_insomnia_gp`

**What to do:** See a GP about your trouble sleeping. They can help find the cause and suggest treatment, such as talking therapy for sleep.

**Look out for:**
- Feeling very low, or having thoughts of harming yourself
- Snoring loudly or stopping breathing in your sleep

**Get more help when:**
- If you are having thoughts of harming yourself, call 111, or Samaritans on 116 123, at any time

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Go to bed only when you are sleepy, and get up at the same time every day
- Do not drink alcohol, tea or coffee for 6 hours before bed
- Do not use screens right before bed

Source: [Insomnia](https://www.nhs.uk/conditions/insomnia/), [Restless legs syndrome](https://www.nhs.uk/conditions/restless-legs-syndrome/), [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/)

### `advice_insomnia_self_care`

**What to do:** Insomnia usually gets better by changing your sleeping habits. A pharmacist can also give advice.

**Look out for:**
- Trouble sleeping that goes on for months
- Not being able to cope with daily life because of lack of sleep

**Get more help when:**
- See a GP if changing your sleeping habits has not helped
- If you are having thoughts of harming yourself, call 111, or Samaritans on 116 123, at any time

**Where to go:** You do not need an appointment now. A pharmacist can help. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Go to bed only when you are sleepy, and get up at the same time every day
- Relax for at least 1 hour before bed, for example with a bath or a book
- Keep your bedroom dark and quiet
- Do not have alcohol, tea or coffee for 6 hours before bed, or a big meal late at night
- Do not nap during the day, and do not drive if you feel sleepy

Source: [Insomnia](https://www.nhs.uk/conditions/insomnia/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `or_in_restless_legs`: The Restless legs syndrome page says see a GP if it is stopping you sleeping.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Insomnia from stress, worry or sleep habits | 193462001 | very common | Having a lot of caffeine or alcohol: supports; Going through a stressful time or big life change: supports; Feels very tired: supports; Trouble sleeping for 3 months or more: supports |
| Restless legs syndrome | 32914008 | uncommon | Strong urge to move the legs, mostly in the evening or at night: strongly supports; Trouble sleeping (insomnia): supports; Skin paler than usual for weeks or longer: supports |
| Sleep apnoea (breathing that stops and starts during sleep) | 78275009 | common | Breathing stops and starts during sleep, or gasping or choking noises: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Sleepiness affecting life, such as work, school or driving: supports; Tired for a few weeks or more, without knowing why: supports; Very sleepy or falling asleep during the day: strongly supports; Snoring: strongly supports; Overweight: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Stress, worry or low mood, or a reaction to grief or a difficult life event |  | common | Something very upsetting happened recently: strongly supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports; Going through a stressful time or big life change: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Problems remembering things: supports; Very sleepy or falling asleep during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
