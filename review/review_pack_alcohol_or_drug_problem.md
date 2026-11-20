# Review pack: Problems with alcohol or drugs

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
| [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | 2026-11-19 |  | Page last reviewed: 04 June 2026 |
| [Poisoning](https://www.nhs.uk/conditions/poisoning/) | 2026-11-19 |  | Page last reviewed: 12 June 2025 |
| [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | 2026-11-19 |  | Page last reviewed: 24 April 2026 |
| [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | 2026-11-19 |  | Page last reviewed: 23 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Drug addiction: getting help](https://www.nhs.uk/live-well/addiction-support/drug-addiction-getting-help/) | 2026-11-19 |  | Page last reviewed: 13 February 2023 |

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

## Problems with alcohol or drugs red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ad_alcohol_poisoning`<br>Signs of alcohol poisoning | "Signs of alcohol poisoning" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| `rf_ad_slow_breathing`<br>Breathing very slowly, or with long gaps between breaths<br>**Note:** Also a sign of an overdose of heroin or another opioid (AI judgement). | "Breathing slowly or unevenly" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| `rf_ad_drowsy`<br>Very sleepy or hard to wake after alcohol or a drug<br>**Note:** The Poisoning page lists feeling sleepy as a symptom of poisoning, and the Alcohol poisoning page says call 999 if someone loses consciousness. Treating being hard to wake as a 999 sign is AI judgement. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| `rf_ad_fit`<br>Has had a seizure (fit) | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| `rf_ad_overdose`<br>Has taken an overdose or swallowed something harmful | "Taken an overdose, or swallowed something harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| `rf_ad_drug_reaction`<br>Very unwell after taking a drug | "Very unwell after taking a drug" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| `rf_ad_severe_withdrawal`<br>Signs of severe alcohol withdrawal | "Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| `rf_ad_cannot_keep_safe`<br>Cannot keep themselves or someone else safe right now | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |

## Problems with alcohol or drugs red flags: Urgent (help today)

Most of these are asked together as one question: *"These questions help us find the right help. Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ad_stopped_after_severe_withdrawal`<br>Stopped or cut down drinking in the last few days, and has had fits or severe withdrawal before<br>**Note:** Clinical knowledge: someone who has had fits or severe withdrawal before is more likely to have them again, so needs medical help with stopping straight away. The Alcohol misuse page says it can be very dangerous to stop suddenly if you are dependent. | "Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days" AND "Has had a fit or seen or heard things when stopping drinking before" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |
| `rf_ad_withdrawal_symptoms`<br>Withdrawal symptoms after stopping or cutting down in the last few days<br>**Note:** Source difference: the Alcohol misuse page says see a GP (non-urgent) for withdrawal symptoms such as anxiety, sweating or feeling sick. Clinical knowledge: fits and severe withdrawal usually start 1 to 3 days after stopping, so same-day advice is used. Soft. | "Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days" AND "Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |

## Problems with alcohol or drugs: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Worried about alcohol or drug use, with no sign of danger now**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP or a local alcohol or drug support service. The source gives no fixed time.*
- Source: [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/)
- **Note:** The Drug addiction page also says a GP is a good place to start, or a local drug service directly.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Worried about alcohol or drug use | Are you worried about how much alcohol you drink, or about drug use? Or have you had problems after drinking or taking a drug? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Signs of alcohol poisoning | Has the person had a lot to drink? Are they now very confused, sleepy or being sick? Or can they not stand up, or have they wet or soiled themselves? |  | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| Breathing slowly or unevenly | Is the person breathing very slowly, or with long gaps between breaths? |  | [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Taken an overdose, or swallowed something harmful | In the last few days, have you taken an overdose of a medicine or a drug, or swallowed something harmful? Answer yes even if you feel well. |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Very unwell after taking a drug | Since taking a drug, do you feel very unwell? For example, very hot, a racing heart, chest pain, being sick a lot, or very confused. |  | [Poisoning](https://www.nhs.uk/conditions/poisoning/) | |
| Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things | After stopping or cutting down drinking, are you shaking so much that others can see it? Or very restless, upset or confused, or seeing or hearing things that are not there? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days | In the last few days, have you stopped or cut down drinking alcohol? Or stopped a drug or medicine you rely on? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Has had a fit or seen or heard things when stopping drinking before | When you stopped drinking in the past, did you have a fit, or see or hear things that were not there? |  | **AI judgement, needs clinical review** | |
| Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep | Since you stopped or cut down, have you been shaking, sweating, anxious, feeling sick or not able to sleep? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |

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

### `advice_alcohol_poisoning_999`

**What to do:** Call 999 now. This could be alcohol poisoning or an overdose, which can stop someone breathing.

**Look out for:**
- Keep checking the person is breathing properly
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person gets worse before help arrives
- Later, for support with drinking or drug use, see a GP. If you are struggling, call Samaritans free on 116 123, or NHS 111 and choose option 2.

**Where to go:** Call 999. Do not drive them to A&E yourself. Stay with them until help arrives.

**What you can do yourself:**
- Stay with them, because they could choke on their own sick or stop breathing
- Sit them up if they are awake. If they have passed out, put them on their side (the recovery position) and check they are breathing.
- Keep them warm. Do not give them more alcohol, food, coffee or a cold shower, and do not try to make them sick.

Source: [Alcohol poisoning](https://www.nhs.uk/conditions/alcohol-poisoning/)

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

### `advice_withdrawal_urgent`

**What to do:** Ask your GP surgery for an urgent appointment, or call NHS 111, today. Stopping alcohol (or some medicines) suddenly can be dangerous if your body has got used to it. A doctor can help you stop safely.

**Look out for:**
- Shaking so much that others can see it
- Feeling very restless, upset or confused
- Seeing, hearing or feeling things that are not there
- A fit (seizure)

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above
- If you feel low or have thoughts of harming yourself, call Samaritans free on 116 123, or call NHS 111 and choose option 2 for mental health
- Call 999 or go to A&E if someone has seriously hurt themselves or taken an overdose

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online, today. Do not stay alone if you can avoid it.

**What you can do yourself:**
- Get medical help before you stop drinking completely
- Drink plenty of water or other soft drinks
- Ask someone to stay with you

Source: [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/)

### `advice_alcohol_drugs_gp`

**What to do:** See a GP or a local alcohol or drug support service. You are entitled to help, the same as for any other health problem.

**Look out for:**
- Shaking, sweating, anxiety or feeling sick when you stop or cut down
- Seeing or hearing things that are not there, or a fit, after stopping

**Get more help when:**
- Get medical help before you stop drinking if you get withdrawal symptoms. Stopping suddenly can be dangerous.
- Call 999 or go to A&E for severe withdrawal: shaking badly, confusion, seeing things, or a fit
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or NHS 111 and choose option 2. Call 999 if your life is in danger.

**Where to go:** Make an appointment with a GP, or contact a local alcohol or drug service yourself. The Frank helpline (0300 123 6600) can help you find support.

**What you can do yourself:**
- Keep a diary of how much you drink or use
- Tell people you trust that you want to cut down, so they can help
- Do not stop drinking suddenly if you drink heavily every day. Get advice first.

Source: [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/), [Drug addiction: getting help](https://www.nhs.uk/live-well/addiction-support/drug-addiction-getting-help/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ad_slow_breathing`: Also a sign of an overdose of heroin or another opioid (AI judgement).
- `rf_ad_drowsy`: The Poisoning page lists feeling sleepy as a symptom of poisoning, and the Alcohol poisoning page says call 999 if someone loses consciousness. Treating being hard to wake as a 999 sign is AI judgement.
- `rf_ad_stopped_after_severe_withdrawal`: Clinical knowledge: someone who has had fits or severe withdrawal before is more likely to have them again, so needs medical help with stopping straight away. The Alcohol misuse page says it can be very dangerous to stop suddenly if you are dependent.
- `rf_ad_withdrawal_symptoms`: Source difference: the Alcohol misuse page says see a GP (non-urgent) for withdrawal symptoms such as anxiety, sweating or feeling sick. Clinical knowledge: fits and severe withdrawal usually start 1 to 3 days after stopping, so same-day advice is used. Soft.
- `alcohol_or_drug_problem default outcome`: The Drug addiction page also says a GP is a good place to start, or a local drug service directly.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Alcohol dependence (finding it hard to control drinking) | 66590003 | rare | Drinks a lot of alcohol: strongly supports; Finds it hard to stop or cut down: strongly supports; Feeling low, sad or depressed: supports; Feeling anxious, worried or panicky: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports |
| Alcohol poisoning | 1149333003 | very rare | Signs of alcohol poisoning: strongly supports; So drowsy they are hard to wake or cannot stay awake: strongly supports; Breathing slowly or unevenly: supports; Feels sick or has been sick: supports; Has had a seizure (fit): supports |
| Alcohol withdrawal (symptoms after stopping or cutting down drinking) | 191480000 | rare | Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days: strongly supports; Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep: strongly supports; Drinks a lot of alcohol: strongly supports; Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feeling anxious, worried or panicky: supports; Hearing, seeing or feeling things that other people do not: supports; Shaking or trembling (tremor): supports; Has had a seizure (fit): supports |
| Drug dependence (finding it hard to control drug use) |  | common | Takes a drug most days: strongly supports; Finds it hard to stop or cut down: strongly supports; Has taken a drug in the last few days: supports; Feeling low, sad or depressed: supports; Feeling anxious, worried or panicky: supports |
| An overdose, or poisoning from a medicine or drug | 1149222004 | very rare | Taken an overdose, or swallowed something harmful: strongly supports; Very unwell after taking a drug: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Breathing slowly or unevenly: supports; Feels sick or has been sick: supports; Heart beating very fast: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
