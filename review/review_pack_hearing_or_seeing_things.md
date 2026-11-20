# Review pack: Hearing or seeing things that others do not

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
| [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | 2026-11-19 |  | Page last reviewed: 23 October 2026 |
| [Poisoning](https://www.nhs.uk/conditions/poisoning/) | 2026-11-19 |  | Page last reviewed: 12 June 2025 |
| [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | 2026-11-19 |  | Page last reviewed: 04 June 2026 |
| [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | 2026-11-19 |  | Page last reviewed: 24 April 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Postpartum psychosis](https://www.nhs.uk/mental-health/conditions/post-partum-psychosis/) | 2026-11-19 |  | Page last reviewed: 18 October 2023 |
| [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | 2026-11-19 |  | Page last reviewed: 28 October 2024 |
| [Charles Bonnet syndrome](https://www.nhs.uk/conditions/charles-bonnet-syndrome/) | 2026-11-19 |  | Page last reviewed: 17 June 2026 |
| [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | 2026-11-19 |  | Page last reviewed: 5 September 2023 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
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

## Hearing or seeing things that others do not red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hs_cannot_keep_safe`<br>Hearing or seeing things and cannot keep themselves or someone else safe | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_hs_voices_harm`<br>Voices telling them to harm themselves or someone else<br>**Note:** Clinical knowledge: voices telling someone to harm themselves or others need assessment now. The Postpartum psychosis page says go to A&E or call 999 if there may be danger of harm. | "Voices telling them to harm themselves or someone else" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_hs_overdose`<br>Hearing or seeing things after an overdose, or after swallowing something harmful | "Taken an overdose, or swallowed something harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| `rf_hs_drug_reaction`<br>Hearing or seeing things and very unwell after taking a drug | "Very unwell after taking a drug" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| `rf_hs_fit`<br>Hearing or seeing things, and has had a seizure (fit)<br>**Note:** The Alcohol poisoning and Poisoning pages say call 999 after a seizure. The Alcohol misuse page lists a seizure as a sign of severe withdrawal. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| `rf_hs_drowsy`<br>Hearing or seeing things and very sleepy or hard to wake<br>**Note:** Clinical knowledge: drowsiness with hallucinations suggests sudden confusion (delirium) or poisoning, which the Confusion and Poisoning pages say need A&E or 999. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_hs_severe_withdrawal`<br>Signs of severe alcohol withdrawal | "Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| `rf_hs_after_stopping`<br>Hearing or seeing things after stopping or cutting down alcohol, or a drug or medicine they rely on<br>**Note:** The Alcohol misuse page lists seeing, hearing or feeling things that are not there after stopping drinking as severe withdrawal (999 or A&E). Applying it to stopping other drugs or medicines someone relies on (for example sleeping tablets) is AI judgement. | "Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| `rf_hs_high_temperature`<br>Hearing or seeing things with a very high temperature, or feeling hot, cold or shivery<br>**Note:** Clinical knowledge: hallucinations with a high temperature suggest an infection causing sudden confusion (delirium). The Confusion page lists seeing or hearing things as a sign of confusion, and an infection as a common cause. | "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_hs_sudden_older`<br>Hearing or seeing things that came on suddenly, in someone aged 65 or over<br>**Note:** The Confusion page lists seeing or hearing things that are not there as a sign of confusion, and says go to A&E or call 999 if someone suddenly becomes confused. Reading new hallucinations in an older person as possible sudden confusion is AI judgement. | "Came on suddenly, over hours or a few days" AND "Aged 65 or over" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |

## Hearing or seeing things that others do not red flags: Urgent (help today)

Most of these are asked together as one question: *"These questions help us find the right help. Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_hs_after_birth`<br>Hearing or seeing things while pregnant or within 6 weeks of giving birth (possible postpartum psychosis)<br>**Note:** The page says postpartum psychosis is a medical emergency, to see a GP immediately and ask for an assessment the same day, and to go to A&E or call 999 if there is danger of harm. Including pregnancy is AI judgement. | "Pregnant, or gave birth in the last 6 weeks" | Urgent (help today)<br>Urgent care<br>Today<br>*See a GP straight away and ask for an urgent assessment today. Call 111 if you cannot. Call 999 or go to A&E if anyone may be in danger.* | [Postpartum psychosis](https://www.nhs.uk/mental-health/conditions/post-partum-psychosis/) | |
| `rf_hs_high_mood`<br>Hearing or seeing things with a very high, excited or overactive mood (possible mania) | "Feeling very high or full of energy, with racing thoughts or little sleep" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | |
| `rf_hs_drug_use`<br>Hearing or seeing things after taking a drug in the last few days<br>**Note:** Clinical knowledge: drugs such as cannabis, cocaine, ketamine or speed can cause psychosis. If the person is very unwell, the emergency rule applies. | "Has taken a drug in the last few days" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 today* | **AI judgement, needs clinical review** | |

## Hearing or seeing things that others do not: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Hearing or seeing things, with no sign of immediate danger: get help today to rule out serious causes**
- Outcome: Urgent (help today), Urgent care, Today. *Ask your GP surgery for an urgent appointment, or call NHS 111 and choose the mental health option (option 2), today*
- Source: [Charles Bonnet syndrome](https://www.nhs.uk/conditions/charles-bonnet-syndrome/)
- **Note:** The Charles Bonnet syndrome page says ask for an urgent GP appointment or get help from 111 if you or someone else have hallucinations, to rule out more serious conditions. Not a floor: a clearly harmless pattern can lower it.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Hearing, seeing or feeling things that other people do not | Have you been hearing, seeing or feeling things that other people do not? For example, hearing voices when no one is there. | 7011001 | [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Voices telling them to harm themselves or someone else | Are the voices telling you to harm yourself or someone else? |  | **AI judgement, needs clinical review** | |
| Taken an overdose, or swallowed something harmful | In the last few days, have you taken an overdose of a medicine or a drug, or swallowed something harmful? Answer yes even if you feel well. |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Very unwell after taking a drug | Since taking a drug, do you feel very unwell? For example, very hot, a racing heart, chest pain, being sick a lot, or very confused. |  | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things | After stopping or cutting down drinking, are you shaking so much that others can see it? Or very restless, upset or confused, or seeing or hearing things that are not there? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days | In the last few days, have you stopped or cut down drinking alcohol? Or stopped a drug or medicine you rely on? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Came on suddenly, over hours or a few days | Did this come on suddenly, over a few hours or days? |  | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Feeling very high or full of energy, with racing thoughts or little sleep | Do you feel very high, excited or full of energy? For example, your thoughts race, you talk fast, or you need much less sleep. |  | [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | |
| Has taken a drug in the last few days | In the last few days, have you taken a drug such as cannabis, cocaine, ecstasy, ketamine or speed? |  | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |

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

### `advice_mh_cannot_keep_safe`

**What to do:** Call 999 or go to A&E now. A mental health emergency is as serious as a physical one. You will not be wasting anyone's time.

**Look out for:**
- Feeling that you may act on thoughts of ending your life or harming yourself
- Feeling that you cannot keep yourself or someone else safe

**Get more help when:**
- Call 999 now if you have seriously hurt yourself or taken an overdose
- While you wait, call Samaritans free on 116 123, day or night. Or text SHOUT to 85258.
- If you have a crisis team, you can also call them

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to take you, or call 999 for an ambulance. If you can, stay with other people and move away from anything you could use to harm yourself.

**What you can do yourself:**
- Try to get to a safe place, like a friend's house, and be around other people
- Stay away from alcohol and drug use, and from anything you could use to harm yourself
- Focus on getting through the next few minutes and hours, not the future

Source: [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/), [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/)

### `advice_mh_overdose_or_injury`

**What to do:** Call 999 for an ambulance or go straight to A&E now, even if you feel well. Some overdoses do not cause symptoms for hours or days, but can still be very harmful.

**Look out for:**
- Feeling very sleepy, being sick, or breathing slowly
- Bleeding that will not stop, or blood coming out in spurts

**Get more help when:**
- Call 999 now if the person stops responding or stops breathing
- If you need someone to talk to, call Samaritans free on 116 123, day or night. Or text SHOUT to 85258.

**Where to go:** Call 999 or go straight to A&E. Do not drive yourself. Take any medicine packets or containers with you, so staff know what was taken.

**What you can do yourself:**
- Do not try to make yourself sick
- For a wound that is bleeding, press firmly on it with a clean cloth
- Do not eat or drink anything until you have been checked, unless a doctor says you can

Source: [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/), [Poisoning](https://www.nhs.uk/conditions/poisoning/), [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/)

### `advice_poisoning_ae`

**What to do:** Call 999 or go to A&E now. A bad reaction to a drug can be very serious, and can get worse quickly.

**Look out for:**
- Very high temperature, a racing heart or chest pain
- Very sleepy, hard to wake, or breathing slowly
- A fit (seizure)

**Get more help when:**
- Call 999 now if the person stops responding or stops breathing. Start CPR: press hard and fast in the middle of their chest.
- If you are struggling, call Samaritans free on 116 123, or call NHS 111 and choose option 2 for mental health

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Take some of the drug or its packaging with you if you can, so staff know what was taken.

**What you can do yourself:**
- Do not try to make yourself sick
- If the person is very hot, move them somewhere cool and give small sips of water if they are awake
- If they pass out but are breathing, put them on their side (the recovery position)

Source: [Poisoning](https://www.nhs.uk/conditions/poisoning/)

### `advice_mh_physical_cause_ae`

**What to do:** Call 999 or go to A&E now. This could be caused by a physical illness that needs checking straight away, such as an infection, a reaction to a medicine or drug, or a problem with the heart.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 if things get worse, or you cannot get to A&E safely
- If you are struggling with your mental health, call Samaritans free on 116 123, or call NHS 111 and choose option 2

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- If you are with someone who is confused, stay with them, tell them who you are and where they are, and keep reassuring them
- Use simple words and short sentences

Source: [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/), [Poisoning](https://www.nhs.uk/conditions/poisoning/)

### `advice_withdrawal_ae`

**What to do:** Call 999 or go to A&E now. These are signs of severe withdrawal after stopping drinking, which can be life-threatening.

**Look out for:**
- A fit (seizure)
- Becoming very confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person has a fit, stops responding, or you cannot get to A&E safely
- If you are struggling with your mental health, call Samaritans free on 116 123, or call NHS 111 and choose option 2

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Stay with the person. Do not leave them alone.

Source: [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/)

### `advice_postpartum_psychosis_urgent`

**What to do:** See a GP straight away and ask for an urgent assessment today. This can be a serious illness after having a baby, called postpartum psychosis, where you lose touch with what is real. It can get worse quickly, but most people recover fully with treatment.

**Look out for:**
- Hearing or seeing things that are not there
- Believing things that are not true
- Feeling very high, very low, or very confused
- Thoughts of harming yourself or your baby

**Get more help when:**
- Go to A&E or call 999 if you think anyone may be in danger of harm, including the baby
- Call 999 or go to A&E if someone has seriously hurt themselves or taken an overdose
- Call NHS 111 and choose option 2 for mental health if you cannot speak to a GP. Call Samaritans free on 116 123 if you need to talk.

**Where to go:** Contact your GP straight away. If you cannot, call 111. Your midwife or health visitor can also help. If you have a crisis team, call them.

**What you can do yourself:**
- Do not stay alone with the baby. Ask a partner, family member or friend to stay with you.
- The person may not realise they are ill. Family and friends may need to get help for them.

Source: [Postpartum psychosis](https://www.nhs.uk/mental-health/conditions/post-partum-psychosis/)

### `advice_mh_urgent`

**What to do:** Get urgent help for your mental health today. Call NHS 111 and choose option 2 for mental health, or ask your GP surgery for an urgent appointment.

**Look out for:**
- Thoughts of ending your life or harming yourself
- Feeling you cannot keep yourself or someone else safe
- Hearing voices that tell you to harm yourself or others

**Get more help when:**
- Call 999 or go to A&E now if a life is in danger. This includes if someone has badly hurt themselves or taken an overdose. Or if you cannot keep yourself or others safe.
- Call Samaritans free on 116 123, day or night, if you need to talk. Or text SHOUT to 85258.

**Where to go:** Call NHS 111 and choose option 2, use 111 online, or ask your GP surgery for an urgent appointment today. If you have a crisis team, call them.

**What you can do yourself:**
- Tell someone you trust how you are feeling, and try to be around other people
- Stay away from alcohol and drug use

Source: [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/)

### `advice_hallucinations_urgent`

**What to do:** Ask your GP surgery for an urgent appointment, or call NHS 111 and choose option 2 for mental health, today. Seeing or hearing things that others do not needs checking to rule out serious causes.

**Look out for:**
- Suddenly becoming confused, very sleepy or hard to wake
- A very high temperature, or feeling hot, cold or shivery
- Voices telling you to harm yourself or someone else
- Believing that people are trying to harm you

**Get more help when:**
- Call 999 or go to A&E if someone suddenly becomes confused, has a fit, or cannot be kept safe
- Call 999 or go to A&E if someone has seriously hurt themselves or taken an overdose
- Call Samaritans free on 116 123, day or night, if you need to talk

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 and choose option 2, or use 111 online, today.

**What you can do yourself:**
- Try to stay with someone you trust
- Stay away from alcohol and drug use, as they can make this worse
- Make a list of any medicines you take, to show the doctor

Source: [Charles Bonnet syndrome](https://www.nhs.uk/conditions/charles-bonnet-syndrome/), [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/), [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_hs_voices_harm`: Clinical knowledge: voices telling someone to harm themselves or others need assessment now. The Postpartum psychosis page says go to A&E or call 999 if there may be danger of harm.
- `rf_hs_fit`: The Alcohol poisoning and Poisoning pages say call 999 after a seizure. The Alcohol misuse page lists a seizure as a sign of severe withdrawal.
- `rf_hs_drowsy`: Clinical knowledge: drowsiness with hallucinations suggests sudden confusion (delirium) or poisoning, which the Confusion and Poisoning pages say need A&E or 999.
- `rf_hs_after_stopping`: The Alcohol misuse page lists seeing, hearing or feeling things that are not there after stopping drinking as severe withdrawal (999 or A&E). Applying it to stopping other drugs or medicines someone relies on (for example sleeping tablets) is AI judgement.
- `rf_hs_high_temperature`: Clinical knowledge: hallucinations with a high temperature suggest an infection causing sudden confusion (delirium). The Confusion page lists seeing or hearing things as a sign of confusion, and an infection as a common cause.
- `rf_hs_sudden_older`: The Confusion page lists seeing or hearing things that are not there as a sign of confusion, and says go to A&E or call 999 if someone suddenly becomes confused. Reading new hallucinations in an older person as possible sudden confusion is AI judgement.
- `rf_hs_after_birth`: The page says postpartum psychosis is a medical emergency, to see a GP immediately and ask for an assessment the same day, and to go to A&E or call 999 if there is danger of harm. Including pregnancy is AI judgement.
- `rf_hs_drug_use`: Clinical knowledge: drugs such as cannabis, cocaine, ketamine or speed can cause psychosis. If the person is very unwell, the emergency rule applies.
- `hearing_or_seeing_things default outcome`: The Charles Bonnet syndrome page says ask for an urgent GP appointment or get help from 111 if you or someone else have hallucinations, to rule out more serious conditions. Not a floor: a clearly harmless pattern can lower it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sudden confusion from an illness, such as an infection | 2776000 | common | Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Started a new medicine or changed a dose in the last few weeks: supports; Signs of dehydration: supports; So drowsy they are hard to wake or cannot stay awake: supports; Cough: supports; Suddenly confused: strongly supports; Came on suddenly, over hours or a few days: strongly supports; Recent infection, or started a new medicine: supports |
| Alcohol withdrawal (symptoms after stopping or cutting down drinking) | 191480000 | rare | Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days: strongly supports; Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep: strongly supports; Drinks a lot of alcohol: strongly supports; Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feeling anxious, worried or panicky: supports; Hearing, seeing or feeling things that other people do not: supports; Shaking or trembling (tremor): supports; Has had a seizure (fit): supports |
| Seeing or hearing things for a harmless reason, such as when falling asleep, after a loss, or with poor sight |  | common | Only sees or hears things when falling asleep or waking up: strongly supports; Knows that what they see or hear is not real: strongly supports; Poor sight for a long time: supports; Something very upsetting happened recently: supports |
| Mania (a very high mood, often part of bipolar, where mood swings between very high and very low) | 231494001 | uncommon | Feeling very high or full of energy, with racing thoughts or little sleep: strongly supports; Doing risky things that are not like them: strongly supports; Hardly slept for 2 nights or more: supports; Muddled thoughts or speech that is hard to follow: supports; Believes things that others say are not true: supports; Aggressive, violent or threatening: supports |
| An overdose, or poisoning from a medicine or drug | 1149222004 | very rare | Taken an overdose, or swallowed something harmful: strongly supports; Very unwell after taking a drug: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Breathing slowly or unevenly: supports; Feels sick or has been sick: supports; Heart beating very fast: supports |
| Postpartum psychosis (losing touch with what is real, soon after giving birth) | 18260003 | rare | Pregnant, or gave birth in the last 6 weeks: strongly supports; Hearing, seeing or feeling things that other people do not: strongly supports; Feeling very high or full of energy, with racing thoughts or little sleep: strongly supports; Believes things that others say are not true: supports; Hardly slept for 2 nights or more: supports; Muddled thoughts or speech that is hard to follow: supports; Suddenly confused: supports |
| Psychosis (losing touch with what is real) | 69322001 | rare | Believes things that others say are not true: strongly supports; Hearing, seeing or feeling things that other people do not: strongly supports; Muddled thoughts or speech that is hard to follow: supports; Voices telling them to harm themselves or someone else: supports; Withdrawn from friends and family: supports; Hardly slept for 2 nights or more: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
