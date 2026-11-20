# Review pack: Feeling anxious or panicky

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
| [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | 2026-11-19 |  | Page last reviewed: 5 September 2023 |
| [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/) | 2026-11-19 |  | Page last reviewed: 13 July 2026 |
| [Generalised anxiety disorder in adults: symptoms](https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder-gad/) | 2026-11-19 |  | Page last reviewed: 22 October 2024 |
| [Panic disorder](https://www.nhs.uk/mental-health/conditions/panic-disorder/) | 2026-11-18 |  | Page last reviewed: 22 August 2023 |
| [Post-traumatic stress disorder: symptoms](https://www.nhs.uk/mental-health/conditions/ptsd-post-traumatic-stress-disorder/) | 2026-11-19 |  | Page last reviewed: 8 April 2026 |
| [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | 2026-11-19 |  |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | 2026-11-19 |  | Page last reviewed: 24 April 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Poisoning](https://www.nhs.uk/conditions/poisoning/) | 2026-11-19 |  | Page last reviewed: 12 June 2025 |

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

## Feeling anxious or panicky red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ax_cannot_keep_safe`<br>Anxious and cannot keep themselves or someone else safe right now | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_ax_overdose`<br>Anxious and has taken an overdose or swallowed something harmful | "Taken an overdose, or swallowed something harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_ax_fainted`<br>Anxious or panicky and has passed out (fainted)<br>**Note:** Clinical knowledge: a panic attack can make you feel faint, but rarely makes you pass out. Passing out can mean a heart rhythm problem or a blood clot in the lung. The Panic disorder page warns that its symptoms can also be signs of other conditions. | "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Feeling anxious or panicky red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ax_harm_others`<br>Anxious with thoughts of harming someone else<br>**Note:** Clinical knowledge. If they feel they cannot keep someone safe, the emergency rule applies. | "Thoughts of harming someone else" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | **AI judgement, needs clinical review** | |
| `rf_ax_believes_untrue`<br>Anxious and believing things that others say are not true, such as being watched or followed<br>**Note:** The Psychosis page says people with delusions often feel frightened and distressed. Making it urgent is AI judgement. | "Believes things that others say are not true" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | |
| `rf_ax_withdrawal`<br>Anxious after stopping or cutting down alcohol, or a drug or medicine they rely on, in the last few days<br>**Note:** Source difference: the Alcohol misuse page says see a GP (non-urgent) for withdrawal symptoms such as anxiety, but also that it can be very dangerous to stop drinking suddenly if you are dependent, and to get medical help. Clinical knowledge: fits and severe withdrawal usually start 1 to 3 days after stopping, so same-day advice is used. Soft. | "Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111, today* | **AI judgement, needs clinical review** | |

## Feeling anxious or panicky: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ax_struggling`<br>Struggling to cope with anxiety, fear or panic | "Struggling to cope with anxiety, fear or panic" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/) | |
| `or_ax_gad`<br>Worried or anxious about lots of things, most days, for 6 months or more (possible generalised anxiety) | "Worried or anxious about lots of things, most days, for 6 months or more" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Generalised anxiety disorder in adults: symptoms](https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder-gad/) | |
| `or_ax_panic`<br>Sudden attacks of panic or fear that keep happening (possible panic disorder) | "Keeps having sudden attacks of panic" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Panic disorder](https://www.nhs.uk/mental-health/conditions/panic-disorder/) | |
| `or_ax_ptsd`<br>Reliving a frightening event in flashbacks or nightmares (possible post-traumatic stress) | "Reliving a frightening event in flashbacks or nightmares" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Post-traumatic stress disorder: symptoms](https://www.nhs.uk/mental-health/conditions/ptsd-post-traumatic-stress-disorder/) | |
| `or_ax_low_mood`<br>Anxious, with a low mood for more than 2 weeks | "Low mood most of the day, nearly every day, for more than 2 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | |

## Default outcome

Used when no rule fires.

- **Feeling anxious, with nothing that needs more help: self-help first**
- Outcome: Self-manageable, Self-care, No appointment needed. *Anxiety often gets better with self-help. See a GP if you are struggling to cope.*
- Source: [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/)
- **Note:** The Anxiety, fear and panic page gives self-help and says to see a GP if you are struggling to cope or self-help is not working. Self-care as the default is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feeling anxious, worried or panicky | Have you been feeling anxious, worried, frightened or panicky? |  | [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Taken an overdose, or swallowed something harmful | In the last few days, have you taken an overdose of a medicine or a drug, or swallowed something harmful? Answer yes even if you feel well. |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Thoughts of harming someone else | Have you had thoughts of harming someone else? This includes thoughts of harming a baby or child. |  | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| Believes things that others say are not true | Do you believe things that other people say are not true? For example, that someone is watching you or trying to harm you, or that you have special powers. | 2073000 | [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | |
| Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days | In the last few days, have you stopped or cut down drinking alcohol? Or stopped a drug or medicine you rely on? |  | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |
| Struggling to cope with anxiety, fear or panic | Are you struggling to cope with the anxiety, or is it stopping you doing everyday things? |  | [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/) | |
| Worried or anxious about lots of things, most days, for 6 months or more | Have you felt worried or anxious about lots of different things, on most days, for 6 months or more? |  | [Generalised anxiety disorder in adults: symptoms](https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder-gad/) | |
| Keeps having sudden attacks of panic | Do you keep having sudden attacks of panic or fear, for no clear reason? |  | [Panic disorder](https://www.nhs.uk/mental-health/conditions/panic-disorder/) | |
| Reliving a frightening event in flashbacks or nightmares | Did something very frightening or upsetting happen to you? Do you keep living it again in flashbacks or bad dreams? |  | [Post-traumatic stress disorder: symptoms](https://www.nhs.uk/mental-health/conditions/ptsd-post-traumatic-stress-disorder/) | |
| Low mood most of the day, nearly every day, for more than 2 weeks | Have you felt low for most of the day, nearly every day, for more than 2 weeks? |  | [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | |

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

### `advice_anxiety_gp`

**What to do:** See a GP. Anxiety and panic can get better with treatment, such as talking therapies.

**Look out for:**
- Chest pain, or difficulty breathing that does not settle
- Thoughts of ending your life or harming yourself

**Get more help when:**
- Call 999 if you have chest pain that does not go away, or you pass out
- Call 999 or go to A&E if you have badly hurt yourself or taken an overdose. Do the same if you feel you cannot keep yourself safe.
- If you need help today, call NHS 111 and choose option 2. Call Samaritans free on 116 123 if you need to talk.

**Where to go:** Make an appointment with a GP. If you are 18 or over, you can also refer yourself to an NHS talking therapies service.

**What you can do yourself:**
- During a panic attack, stay where you are, breathe slowly and deeply, and remind yourself it will pass
- Cut down on caffeine and alcohol, and stop smoking
- Try to be active most days, and try slow breathing to help you calm down

Source: [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/), [Panic disorder](https://www.nhs.uk/mental-health/conditions/panic-disorder/), [Generalised anxiety disorder in adults: symptoms](https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder-gad/), [Post-traumatic stress disorder: symptoms](https://www.nhs.uk/mental-health/conditions/ptsd-post-traumatic-stress-disorder/)

### `advice_anxiety_self_care`

**What to do:** Anxiety and panic are common, and often get better with self-help. A panic attack is frightening, but it is not dangerous.

**Look out for:**
- Struggling to cope, or anxiety stopping you doing everyday things
- Panic attacks that keep happening
- Chest pain, or passing out

**Get more help when:**
- See a GP if you are struggling to cope, or self-help is not working
- Call 999 if you have chest pain that does not go away, or you pass out
- If you have thoughts of harming yourself, call Samaritans free on 116 123, or call NHS 111 and choose option 2. Call 999 if your life is in danger.

**Where to go:** No appointment needed now. If you are 18 or over, you can refer yourself to an NHS talking therapies service.

**What you can do yourself:**
- During a panic attack, stay where you are, breathe slowly and deeply, and remind yourself it will pass
- Cut down on caffeine and alcohol, and stop smoking
- Try to be active most days, and try slow breathing to help you calm down
- Talk to someone you trust about what is worrying you

Source: [Anxiety, fear and panic](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/anxiety-fear-panic/), [Panic disorder](https://www.nhs.uk/mental-health/conditions/panic-disorder/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ax_fainted`: Clinical knowledge: a panic attack can make you feel faint, but rarely makes you pass out. Passing out can mean a heart rhythm problem or a blood clot in the lung. The Panic disorder page warns that its symptoms can also be signs of other conditions.
- `rf_ax_harm_others`: Clinical knowledge. If they feel they cannot keep someone safe, the emergency rule applies.
- `rf_ax_believes_untrue`: The Psychosis page says people with delusions often feel frightened and distressed. Making it urgent is AI judgement.
- `rf_ax_withdrawal`: Source difference: the Alcohol misuse page says see a GP (non-urgent) for withdrawal symptoms such as anxiety, but also that it can be very dangerous to stop drinking suddenly if you are dependent, and to get medical help. Clinical knowledge: fits and severe withdrawal usually start 1 to 3 days after stopping, so same-day advice is used. Soft.
- `feeling_anxious default outcome`: The Anxiety, fear and panic page gives self-help and says to see a GP if you are struggling to cope or self-help is not working. Self-care as the default is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anxiety or panic attack | 48694002 | common | Sudden rush of intense fear or panic: strongly supports; Pain triggered by worry or stress: strongly supports; Tingling or pins and needles in the fingers or around the mouth: supports; Breathing very fast: supports; Heart beating very fast: supports; Heart racing, slow, skipping or fluttering: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Short of breath: supports |
| Alcohol dependence (finding it hard to control drinking) | 66590003 | rare | Drinks a lot of alcohol: strongly supports; Finds it hard to stop or cut down: strongly supports; Feeling low, sad or depressed: supports; Feeling anxious, worried or panicky: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports |
| Alcohol withdrawal (symptoms after stopping or cutting down drinking) | 191480000 | rare | Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days: strongly supports; Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep: strongly supports; Drinks a lot of alcohol: strongly supports; Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feeling anxious, worried or panicky: supports; Hearing, seeing or feeling things that other people do not: supports; Shaking or trembling (tremor): supports; Has had a seizure (fit): supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Generalised anxiety (worrying about lots of things, most days) | 21897009 | uncommon | Worried or anxious about lots of things, most days, for 6 months or more: strongly supports; Worry that is hard to control: strongly supports; On edge, irritable or easily startled: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feels very tired: supports; Feeling anxious, worried or panicky: supports |
| Postnatal depression (depression after having a baby) | 58703003 | very rare | Difficult feelings about the baby, or finding it hard to bond: strongly supports; Feels worthless or very guilty: strongly supports; Low mood most of the day, nearly every day, for more than 2 weeks: supports; Lost interest or enjoyment in things: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports |
| Psychosis (losing touch with what is real) | 69322001 | rare | Believes things that others say are not true: strongly supports; Hearing, seeing or feeling things that other people do not: strongly supports; Muddled thoughts or speech that is hard to follow: supports; Voices telling them to harm themselves or someone else: supports; Withdrawn from friends and family: supports; Hardly slept for 2 nights or more: supports |
| Post-traumatic stress (PTSD) | 47505003 | uncommon | Reliving a frightening event in flashbacks or nightmares: strongly supports; Avoids people, places or things that bring back memories of an event: strongly supports; On edge, irritable or easily startled: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports |
| Stress, worry or low mood, or a reaction to grief or a difficult life event |  | common | Something very upsetting happened recently: strongly supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports; Going through a stressful time or big life change: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Problems remembering things: supports; Very sleepy or falling asleep during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
