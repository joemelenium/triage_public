# Review pack: Excessive daytime sleepiness

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
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | 2026-11-19 |  | Page last reviewed: 16 December 2025 |
| [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | 2026-11-19 |  | Page last reviewed: 23 June 2023 |
| [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/) | 2026-11-19 |  | Page last reviewed: 11 May 2026 |
| [Narcolepsy](https://www.nhs.uk/conditions/narcolepsy/) | 2026-11-19 |  | Page last reviewed: 9 September 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Snoring](https://www.nhs.uk/symptoms/snoring/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Broken nose](https://www.nhs.uk/conditions/broken-nose/) | 2026-11-19 |  | Page last reviewed: 17 August 2023 |
| [Tinnitus](https://www.nhs.uk/conditions/tinnitus/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |

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

## Excessive daytime sleepiness red flags: Emergency (help now)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sl_head_injury`<br>Sleepiness after a head injury in the last 3 months<br>**Note:** The Head injury page says call 999 for someone who cannot stay awake after a head injury. A&E for sleepiness up to 3 months after a head injury is AI judgement. | "Head injury in the last 3 months" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |

## Excessive daytime sleepiness red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sl_sudden`<br>Much sleepier than usual, starting suddenly in the last few days<br>**Note:** Clinical knowledge: new, sudden sleepiness can be a sign of an illness that needs checking quickly. The page gives no urgency for this. If the person is hard to wake or confused, the universal red flags apply. | "Much sleepier than usual, starting suddenly in the last few days" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_sl_others_unwell`<br>Sleepiness, and others at home or pets unwell too: possible carbon monoxide poisoning | "Others at home, or pets, unwell with similar symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Go outside into fresh air, then call NHS 111 now* | [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | |

## Excessive daytime sleepiness: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_sl_driving`<br>Fallen asleep, or nearly, while driving<br>**Note:** AI judgement: falling asleep at the wheel is dangerous to the person and others. The page says you may need to tell the DVLA if you are diagnosed with excessive sleepiness. | "Fallen asleep, or nearly, while driving" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP in the next few days. Do not drive until you have been checked.* | **AI judgement, needs clinical review** | |
| `or_sl_falls_asleep`<br>Falls asleep suddenly during the day | "Falls asleep suddenly without warning" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| `or_sl_affecting_life`<br>Sleepiness affecting life | "Sleepiness affecting life, such as work, school or driving" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| `or_sl_breathing_in_sleep`<br>Loud snoring, or breathing that stops and starts while asleep | "Breathing stops and starts during sleep, or gasping or choking noises" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/) | |
| `or_sl_muscle_weakness`<br>Muscles suddenly going weak with laughter, anger or surprise | "Muscles suddenly go weak when laughing, angry or surprised" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Narcolepsy](https://www.nhs.uk/conditions/narcolepsy/) | |

## Default outcome

Used when no rule fires.

- **Often very sleepy during the day: see a GP to find the cause**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/)
- **Note:** The page says see a GP if you often fall asleep during the day. Not a floor: likely conditions such as simply not getting enough sleep can lower it to self-care.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Very sleepy or falling asleep during the day | Do you often feel very sleepy, or keep falling asleep, during the day? | 1367959007 | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Much sleepier than usual, starting suddenly in the last few days | Did the sleepiness start suddenly in the last few days, so you are much sleepier than usual? |  | **AI judgement, needs clinical review** | |
| Head injury in the last 3 months | Have you hit your head, or had a head injury, in the last 3 months? For example, from a fall or accident. |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Others at home, or pets, unwell with similar symptoms | Are other people you live with, or your pets, unwell with similar symptoms? |  | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Fallen asleep, or nearly, while driving | Have you fallen asleep, or nearly fallen asleep, while driving? |  | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| Falls asleep suddenly without warning | Do you fall asleep suddenly, without warning, even when you are busy? |  | [Narcolepsy](https://www.nhs.uk/conditions/narcolepsy/) | |
| Sleepiness affecting life, such as work, school or driving | Is the sleepiness affecting your life, such as work, school or driving? |  | [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/) | |
| Breathing stops and starts during sleep, or gasping or choking noises | Does your breathing stop and start while you sleep, or do you make gasping or choking noises? Someone else may have noticed this. |  | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| Muscles suddenly go weak when laughing, angry or surprised | Do your muscles suddenly go weak when you laugh, or feel angry or surprised? |  | [Narcolepsy](https://www.nhs.uk/conditions/narcolepsy/) | |

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

### `advice_sleepiness_urgent`

**What to do:** Get help from NHS 111 or ask for an urgent GP appointment today. Sleepiness that starts suddenly should be checked today.

**Look out for:**
- Being very hard to wake, or confused
- A headache, being sick, or a stiff neck

**Get more help when:**
- Call 999 if the person cannot be woken, or is confused

**Where to go:** Call 111 or use 111 online, or ask your GP surgery for an urgent appointment. In an emergency call 999.

**What you can do yourself:**
- Do not drive while you feel sleepy

Source: **AI judgement, needs clinical review**, [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/)

### `advice_head_injury_ae`

**What to do:** Go to A&E now. After a head injury, you need to be checked in hospital for bleeding inside the head.

**Look out for:**
- Getting drowsy or hard to wake
- Being sick, or a headache that gets worse
- Confusion, or trouble walking or speaking
- Clear fluid or blood coming from the ear or nose
- Passing out, a seizure (fit), or problems speaking

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself if you have hit your head. Ask someone to take you, or call 999. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/), [Broken nose](https://www.nhs.uk/conditions/broken-nose/), [Tinnitus](https://www.nhs.uk/conditions/tinnitus/)

### `advice_carbon_monoxide`

**What to do:** Go outside into fresh air now, then call NHS 111. Other people being unwell too can be a sign of carbon monoxide, a poisonous gas from faulty boilers, cookers, fires or engines.

**Look out for:**
- Finding it hard to breathe
- Sudden confusion, feeling weak, or chest or muscle pain
- Anyone passing out

**Get more help when:**
- Call 999 or go to A&E if anyone has any of the signs above
- If you think an appliance is leaking gas, call the free National Gas Helpline on 0800 111 999

**Where to go:** Call 111 or use 111 online. In an emergency call 999. Do not go back inside until you have got advice.

**What you can do yourself:**
- Stop using any boiler, cooker or heater you think may be the cause, if you can do it safely
- Get a carbon monoxide alarm for each room with a gas, oil, coal or wood appliance

Source: [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/)

### `advice_sleepiness_gp`

**What to do:** See a GP about your sleepiness. They can look for causes, such as a sleep problem, a medicine or your mood.

**Look out for:**
- Falling asleep while driving or doing something dangerous
- Sleepiness that comes on suddenly

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you become much sleepier quite suddenly

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Do not drive if you feel sleepy. You may need to tell the DVLA if you are diagnosed with a sleep problem.
- Go to bed at the same time every night
- Avoid alcohol and caffeine
- If you can, ask someone to watch your sleep for snoring or pauses in breathing

Source: [Excessive daytime sleepiness (hypersomnia)](https://www.nhs.uk/conditions/excessive-daytime-sleepiness-hypersomnia/), [Sleep apnoea](https://www.nhs.uk/conditions/sleep-apnoea/), [Narcolepsy](https://www.nhs.uk/conditions/narcolepsy/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sl_sudden`: Clinical knowledge: new, sudden sleepiness can be a sign of an illness that needs checking quickly. The page gives no urgency for this. If the person is hard to wake or confused, the universal red flags apply.
- `rf_sl_head_injury`: The Head injury page says call 999 for someone who cannot stay awake after a head injury. A&E for sleepiness up to 3 months after a head injury is AI judgement.
- `or_sl_driving`: AI judgement: falling asleep at the wheel is dangerous to the person and others. The page says you may need to tell the DVLA if you are diagnosed with excessive sleepiness.
- `daytime_sleepiness default outcome`: The page says see a GP if you often fall asleep during the day. Not a floor: likely conditions such as simply not getting enough sleep can lower it to self-care.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Narcolepsy (you fall asleep suddenly, without warning) | 60380001 | rare | Falls asleep suddenly without warning: strongly supports; Muscles suddenly go weak when laughing, angry or surprised: strongly supports; Trouble sleeping (insomnia): supports |
| Not getting enough sleep | 248256006 | very common | Getting less sleep than needed: strongly supports; Feels very tired: supports; Having a lot of caffeine or alcohol: supports |
| Restless legs syndrome | 32914008 | uncommon | Strong urge to move the legs, mostly in the evening or at night: strongly supports; Trouble sleeping (insomnia): supports; Skin paler than usual for weeks or longer: supports |
| Sleep apnoea (breathing that stops and starts during sleep) | 78275009 | common | Breathing stops and starts during sleep, or gasping or choking noises: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Sleepiness affecting life, such as work, school or driving: supports; Tired for a few weeks or more, without knowing why: supports; Very sleepy or falling asleep during the day: strongly supports; Snoring: strongly supports; Overweight: supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |
| Stress, worry or low mood, or a reaction to grief or a difficult life event |  | common | Something very upsetting happened recently: strongly supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports; Going through a stressful time or big life change: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Problems remembering things: supports; Very sleepy or falling asleep during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
