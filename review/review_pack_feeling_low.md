# Review pack: Feeling low or depressed

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
| [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | 2026-11-19 |  |  |
| [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | 2026-11-19 |  | Page last reviewed: 29 July 2026 |
| [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | 2026-11-19 |  | Page last reviewed: 28 October 2024 |
| [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | 2026-11-19 |  | Page last reviewed: 24 April 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | 2026-11-19 |  | Page last reviewed: 5 September 2023 |
| [Liver disease](https://www.nhs.uk/conditions/liver-disease/) | 2026-11-19 |  | Page last reviewed: 09 August 2023 |
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

## Feeling low or depressed red flags: Emergency (help now)

Most of these are asked together as one question: *"Thank you for telling us how you feel. Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_lm_cannot_keep_safe`<br>Feeling low and cannot keep themselves or someone else safe right now | "Cannot keep themselves or someone else safe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| `rf_lm_overdose`<br>Feeling low and has taken an overdose or swallowed something harmful<br>**Note:** The universal red flag for serious self-harm also asks about an overdose. This question adds 'even if you feel well', because some overdoses (for example paracetamol) cause no symptoms at first. | "Taken an overdose, or swallowed something harmful" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| `rf_lm_serious_injury`<br>Feeling low and has a serious injury from self-harm | "Serious injury from self-harm: deep, bleeding a lot, or a bad burn" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 for an ambulance or go straight to A&E* | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |

## Feeling low or depressed red flags: Urgent (help today)

Most of these are asked together as one question: *"These questions help us find the right help for you. Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_lm_harm_others`<br>Feeling low with thoughts of harming someone else, including a baby or child<br>**Note:** The Postnatal depression page lists thoughts of harming your baby as a symptom and points to urgent help. Making it urgent same-day help for anyone is AI judgement. If they feel they cannot keep someone safe, the emergency rule applies. | "Thoughts of harming someone else" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| `rf_lm_psychosis_signs`<br>Feeling low and believing things that others say are not true<br>**Note:** The Depression page says a few people with severe depression have symptoms of psychosis. Making it urgent is AI judgement, in line with the urgent advice for hallucinations on the Charles Bonnet syndrome page. | "Believes things that others say are not true" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | |
| `rf_lm_high_mood`<br>Feeling low, and also very high, excited or overactive now (a mixed or changing mood)<br>**Note:** Clinical knowledge: a high and low mood together, or a mood swinging quickly, can be a mixed state in bipolar, when the chance of acting on suicidal thoughts is higher. The Bipolar disorder page points to urgent help. | "Feeling very high or full of energy, with racing thoughts or little sleep" | Urgent (help today)<br>Urgent care<br>Today<br>*Call NHS 111 and choose the mental health option (option 2), or ask your GP surgery for an urgent appointment today* | **AI judgement, needs clinical review** | |
| `rf_lm_not_eating_drinking`<br>Feeling low and has stopped eating or drinking, or cannot look after themselves<br>**Note:** Clinical knowledge: severe depression with not eating or drinking can quickly harm physical health and needs same-day assessment. | "Stopped eating or drinking, or stopped looking after themselves" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask your GP surgery for an urgent appointment, or call NHS 111 and choose the mental health option (option 2), today* | **AI judgement, needs clinical review** | |

## Feeling low or depressed: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_lm_postnatal`<br>Low mood for more than 2 weeks, or struggling to cope, after having a baby in the last year<br>**Note:** The page says feeling low for a few days after the birth (the baby blues) is very common and usually goes within 2 weeks, but to get help if it carries on, gets worse, or you are struggling to cope. | "Had a baby in the last 12 months" AND ("Low mood most of the day, nearly every day, for more than 2 weeks" OR "Struggling to cope with the low mood") | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*Speak to your GP, midwife or health visitor. The source gives no fixed time.* | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| `or_lm_over_2_weeks`<br>Low mood for most of the day, nearly every day, for more than 2 weeks | "Low mood most of the day, nearly every day, for more than 2 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | |
| `or_lm_struggling`<br>Struggling to cope with a low mood | "Struggling to cope with the low mood" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |
| `or_lm_high_mood_spells`<br>Low mood in someone who has had spells of a very high mood (possible bipolar) | "Has had spells of a very high mood for days at a time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | |
| `or_lm_drinking`<br>Low mood and drinking a lot of alcohol most days | "Drinks a lot of alcohol" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or an alcohol support service. The source gives no fixed time.* | [Alcohol misuse](https://www.nhs.uk/conditions/alcohol-use-disorder/) | |

## Default outcome

Used when no rule fires.

- **Feeling low, with nothing that needs more help: self-help first**
- Outcome: Self-manageable, Self-care, No appointment needed. *A low mood often gets better after a few days or weeks. Try self-help, and see a GP if it lasts more than 2 weeks.*
- Source: [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/)
- **Note:** The Low mood page gives self-help and says to see a GP if a low mood lasts more than 2 weeks or you are struggling to cope. Self-care as the default is a reading of that.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feeling low, sad or depressed | Have you been feeling low, sad, hopeless or depressed? | 366979004 | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot keep themselves or someone else safe | Do you feel that you cannot keep yourself, or someone else, safe right now? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Taken an overdose, or swallowed something harmful | In the last few days, have you taken an overdose of a medicine or a drug, or swallowed something harmful? Answer yes even if you feel well. |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Serious injury from self-harm: deep, bleeding a lot, or a bad burn | Have you hurt yourself and the injury is deep, gaping open or bleeding a lot? Or have you burned yourself badly? |  | [Where to get urgent help for mental health](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) | |
| Thoughts of harming someone else | Have you had thoughts of harming someone else? This includes thoughts of harming a baby or child. |  | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| Believes things that others say are not true | Do you believe things that other people say are not true? For example, that someone is watching you or trying to harm you, or that you have special powers. | 2073000 | [Psychosis: symptoms](https://www.nhs.uk/mental-health/conditions/psychosis/symptoms/) | |
| Feeling very high or full of energy, with racing thoughts or little sleep | Do you feel very high, excited or full of energy? For example, your thoughts race, you talk fast, or you need much less sleep. |  | [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | |
| Stopped eating or drinking, or stopped looking after themselves | Have you stopped eating or drinking, or stopped being able to look after yourself? |  | **AI judgement, needs clinical review** | |
| Had a baby in the last 12 months | Have you had a baby in the last 12 months? Answer yes if you gave birth, or your partner did. |  | [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/) | |
| Low mood most of the day, nearly every day, for more than 2 weeks | Have you felt low for most of the day, nearly every day, for more than 2 weeks? |  | [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/) | |
| Struggling to cope with the low mood | Are you struggling to cope with day-to-day life? For example, work, school, family, or looking after yourself. |  | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |
| Has had spells of a very high mood for days at a time | Have you ever had spells of feeling very high, excited or full of energy for days at a time? For example, needing little sleep or doing risky things. |  | [Bipolar disorder: symptoms](https://www.nhs.uk/mental-health/conditions/bipolar-disorder/) | |
| Drinks a lot of alcohol | Do you usually drink more than 14 units of alcohol a week, or have you drunk a lot in the last few days? 14 units is about 6 pints of beer or 6 medium glasses of wine. |  | [Liver disease](https://www.nhs.uk/conditions/liver-disease/) | |

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

### `advice_low_mood_postnatal_gp`

**What to do:** Speak to your GP, midwife or health visitor. You may have postnatal depression, which is common after having a baby. It usually gets better with treatment.

**Look out for:**
- Thoughts of ending your life, or of harming yourself or your baby
- Hearing or seeing things that are not there, or feeling very confused

**Get more help when:**
- Call 999 or go to A&E if you feel you cannot keep yourself or your baby safe. Do the same if you have badly hurt yourself or taken an overdose.
- If you need help today, call NHS 111 and choose option 2 for mental health. Call Samaritans free on 116 123, day or night.

**Where to go:** Contact your GP, midwife or health visitor. If you are 18 or over, you can also refer yourself to an NHS talking therapies service.

**What you can do yourself:**
- Talk to your partner, family or friends about how you feel, and accept help
- Rest when you can, eat regular meals and get some exercise
- Asking for help does not mean your baby will be taken away. Your care team will support you.

Source: [Postnatal depression: symptoms](https://www.nhs.uk/mental-health/conditions/postnatal-depression/)

### `advice_low_mood_gp`

**What to do:** See a GP. Depression and low mood can get better with the right treatment, such as talking therapies.

**Look out for:**
- Thoughts of ending your life or harming yourself
- Not being able to eat, drink or look after yourself

**Get more help when:**
- Call 999 or go to A&E if you have badly hurt yourself or taken an overdose. Do the same if you feel you cannot keep yourself safe.
- If you need help today, call NHS 111 and choose option 2 for mental health
- Call Samaritans free on 116 123, day or night, if you need to talk. Or text SHOUT to 85258.

**Where to go:** Make an appointment with a GP. If you are 18 or over, you can also refer yourself to an NHS talking therapies service.

**What you can do yourself:**
- Talk to someone you trust about how you feel
- Try to keep active and spend time outside
- Try to keep to a regular sleep pattern and eat regular meals
- Cut down on alcohol, as it can make a low mood worse

Source: [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/), [Depression in adults](https://www.nhs.uk/mental-health/conditions/depression-in-adults/)

### `advice_low_mood_self_care`

**What to do:** A low mood often gets better after a few days or weeks. There are things you can try yourself to help.

**Look out for:**
- Feeling low for most of the day, nearly every day, for more than 2 weeks
- Struggling to cope with day-to-day life
- Thoughts of ending your life or harming yourself

**Get more help when:**
- See a GP if your low mood lasts more than 2 weeks, or things you try are not helping
- Call 999 or go to A&E if you have badly hurt yourself or taken an overdose. Do the same if you feel you cannot keep yourself safe.
- If you need to talk, call Samaritans free on 116 123, day or night, or call NHS 111 and choose option 2 for mental health

**Where to go:** No appointment needed now. If you are 18 or over, you can refer yourself to an NHS talking therapies service.

**What you can do yourself:**
- Talk to someone you trust about how you feel
- Try to keep active, and do things you usually enjoy
- Try to keep to a regular sleep pattern and eat regular meals
- Cut down on alcohol, as it can make a low mood worse

Source: [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_lm_overdose`: The universal red flag for serious self-harm also asks about an overdose. This question adds 'even if you feel well', because some overdoses (for example paracetamol) cause no symptoms at first.
- `rf_lm_harm_others`: The Postnatal depression page lists thoughts of harming your baby as a symptom and points to urgent help. Making it urgent same-day help for anyone is AI judgement. If they feel they cannot keep someone safe, the emergency rule applies.
- `rf_lm_psychosis_signs`: The Depression page says a few people with severe depression have symptoms of psychosis. Making it urgent is AI judgement, in line with the urgent advice for hallucinations on the Charles Bonnet syndrome page.
- `rf_lm_high_mood`: Clinical knowledge: a high and low mood together, or a mood swinging quickly, can be a mixed state in bipolar, when the chance of acting on suicidal thoughts is higher. The Bipolar disorder page points to urgent help.
- `rf_lm_not_eating_drinking`: Clinical knowledge: severe depression with not eating or drinking can quickly harm physical health and needs same-day assessment.
- `or_lm_postnatal`: The page says feeling low for a few days after the birth (the baby blues) is very common and usually goes within 2 weeks, but to get help if it carries on, gets worse, or you are struggling to cope.
- `feeling_low default outcome`: The Low mood page gives self-help and says to see a GP if a low mood lasts more than 2 weeks or you are struggling to cope. Self-care as the default is a reading of that.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Alcohol dependence (finding it hard to control drinking) | 66590003 | rare | Drinks a lot of alcohol: strongly supports; Finds it hard to stop or cut down: strongly supports; Feeling low, sad or depressed: supports; Feeling anxious, worried or panicky: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports |
| Anorexia (eating very little to keep weight low) | 56882008 | very rare | Eating very little or skipping meals to control weight: strongly supports; Very afraid of putting on weight: strongly supports; Lost a lot of weight quickly, or very underweight: strongly supports; Exercising too much to control weight: supports; So weak it is hard to stand up, climb stairs or get up from sitting: supports |
| Bipolar (mood swings between very high and very low), in a low spell | 13746004 | rare | Has had spells of a very high mood for days at a time: strongly supports; Lost interest or enjoyment in things: supports; Feels hopeless, or that things will never get better: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Generalised anxiety (worrying about lots of things, most days) | 21897009 | uncommon | Worried or anxious about lots of things, most days, for 6 months or more: strongly supports; Worry that is hard to control: strongly supports; On edge, irritable or easily startled: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feels very tired: supports; Feeling anxious, worried or panicky: supports |
| Postnatal depression (depression after having a baby) | 58703003 | very rare | Difficult feelings about the baby, or finding it hard to bond: strongly supports; Feels worthless or very guilty: strongly supports; Low mood most of the day, nearly every day, for more than 2 weeks: supports; Lost interest or enjoyment in things: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports |
| Psychosis (losing touch with what is real) | 69322001 | rare | Believes things that others say are not true: strongly supports; Hearing, seeing or feeling things that other people do not: strongly supports; Muddled thoughts or speech that is hard to follow: supports; Voices telling them to harm themselves or someone else: supports; Withdrawn from friends and family: supports; Hardly slept for 2 nights or more: supports |
| Post-traumatic stress (PTSD) | 47505003 | uncommon | Reliving a frightening event in flashbacks or nightmares: strongly supports; Avoids people, places or things that bring back memories of an event: strongly supports; On edge, irritable or easily startled: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports |
| Self-harm (hurting yourself on purpose) | 248062006 | rare | Has harmed themselves on purpose: strongly supports; Self-harm happening more often or getting more serious: supports; Self-harm wound may be infected: supports; Serious injury from self-harm: deep, bleeding a lot, or a bad burn: supports; Feels worthless or very guilty: supports |
| Stress, worry or low mood, or a reaction to grief or a difficult life event |  | common | Something very upsetting happened recently: strongly supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Feeling anxious, worried or panicky: supports; Feeling low, sad or depressed: supports; Going through a stressful time or big life change: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Problems remembering things: supports; Very sleepy or falling asleep during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
