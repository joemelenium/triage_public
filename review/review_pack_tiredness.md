# Review pack: Tiredness or fatigue

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
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | 2026-11-19 |  | Page last reviewed: 02 June 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | 2026-11-19 |  | Page last reviewed: 29 July 2026 |
| [Snoring](https://www.nhs.uk/symptoms/snoring/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
| [ME/CFS](https://www.nhs.uk/conditions/chronic-fatigue-syndrome-cfs/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Heart failure](https://www.nhs.uk/conditions/heart-failure/) | 2026-11-18 |  | Page last reviewed: 26 June 2026 |
| [Pneumonia](https://www.nhs.uk/conditions/pneumonia/) | 2026-11-18 |  | Page last reviewed: 17 July 2026 |

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

## Tiredness or fatigue red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tired_drowsy`<br>So drowsy they are hard to wake or cannot stay awake, or a child who is floppy or not responding as usual<br>**Note:** Being sleepier than usual or hard to wake is a sign of sepsis, and of diabetic ketoacidosis on the Type 1 diabetes page. Applying it to tiredness is AI judgement: it is the line between being tired and being dangerously drowsy. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_tired_ketoacidosis_signs`<br>Tired, with breath that smells fruity or breathing faster and more deeply than usual: possible diabetic ketoacidosis | "Breath smells fruity" OR "Breathing faster and more deeply than usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |

## Tiredness or fatigue red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tired_breathless_at_rest`<br>Tired and short of breath even when resting<br>**Note:** Same as the breathlessness rule. Breathlessness at rest with tiredness can be severe anaemia or heart failure. | "Short of breath at rest" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_tired_type_1_diabetes`<br>Tired, very thirsty and peeing more, in a child or with weight loss: possible type 1 diabetes<br>**Note:** The Type 1 diabetes page says an urgent GP appointment or 111 if you think you or your child has type 1 diabetes, and lists the 4 Ts: toilet, thirsty, tired, thinner. Requiring a child or weight loss, so that an adult more likely to have type 2 diabetes gets a routine appointment, is AI judgement. | "Feeling very thirsty all the time" AND "Peeing more often than usual" AND ("Under 16 years old" OR "Losing weight without trying") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Tiredness or fatigue: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_tired_for_weeks`<br>Tired for a few weeks or more, without knowing why | "Tired for a few weeks or more, without knowing why" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |
| `or_tired_affects_daily_life`<br>Tiredness that affects daily life | "Tiredness affects daily life" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |
| `or_tired_other_symptoms`<br>Tired with other symptoms: weight loss, low mood, or gasping or choking noises in sleep<br>**Note:** The ME/CFS sign (extreme tiredness for 3 months, worse after activity) is added from the conditions table on the same page. | "Losing weight without trying" OR "Feeling low, sad or depressed" OR "Breathing stops and starts during sleep, or gasping or choking noises" OR "Extreme tiredness for months, worse after activity" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |
| `or_tired_thirsty_peeing`<br>Tired, very thirsty and peeing more than usual: possible diabetes | "Feeling very thirsty all the time" AND "Peeing more often than usual" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |

## Default outcome

Used when no rule fires.

- **Tiredness with nothing that needs more help: try the self-help advice first**
- Outcome: Self-manageable, Self-care, No appointment needed. *It's normal to feel tired sometimes. See a GP if it goes on for a few weeks.*
- Source: [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Short of breath at rest | Are you short of breath even when you are sitting still or resting? | 161941007 | **AI judgement, needs clinical review** | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Tired for a few weeks or more, without knowing why | Have you felt tired for a few weeks or more, and you are not sure why? |  | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |
| Tiredness affects daily life | Is the tiredness stopping you doing your usual things, such as work, school or looking after yourself? |  | [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/) | |
| Feeling low, sad or depressed | Have you been feeling low, sad, hopeless or depressed? | 366979004 | [Low mood, sadness and depression](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/feelings-and-symptoms/low-mood-sadness-depression/) | |
| Breathing stops and starts during sleep, or gasping or choking noises | Does your breathing stop and start while you sleep, or do you make gasping or choking noises? Someone else may have noticed this. |  | [Snoring](https://www.nhs.uk/symptoms/snoring/) | |
| Extreme tiredness for months, worse after activity | Have you been very tired for 3 months or more? Does it get much worse after you do things, and make it hard to think or remember? |  | [ME/CFS](https://www.nhs.uk/conditions/chronic-fatigue-syndrome-cfs/) | |

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

### `advice_unwell_emergency`

**What to do:** Call 999 or go to A&E now. Being very sleepy or hard to wake can be a sign of a serious illness, such as sepsis (a life-threatening reaction to an infection).

**Look out for:**
- Not responding, or becoming confused
- Breathing very fast
- Skin, lips or tongue turning blue, grey, pale or blotchy

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_ketoacidosis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of diabetic ketoacidosis, a life-threatening problem from a lack of insulin. It can happen to people who do not know they have diabetes.

**Look out for:**
- Becoming confused, very sleepy or hard to wake
- Breathing that gets faster and deeper
- Being sick again and again

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines and insulin you take.

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/), [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_breathless_urgent`

**What to do:** Get help from NHS 111 or ask for an urgent GP appointment today. You can call 111 or use 111 online.

**Look out for:**
- Breathing problems that come on suddenly or suddenly get much worse
- Being so short of breath you cannot say a short sentence
- Your chest feeling tight or heavy, or pain spreading to your arms, back, neck or jaw
- Lips or skin turning very pale, blue or grey, or feeling suddenly confused

**Get more help when:**
- Call 999 or go to A&E now if you get any of the signs above

**Where to go:** Call 111 or use 111 online today, or ask your GP surgery for an urgent appointment. In an emergency call 999 or go to A&E. Do not drive to A&E.

**What you can do yourself:**
- Sit upright to help your breathing
- If you have a reliever inhaler, use it as your care team told you

Source: [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/), [Heart failure](https://www.nhs.uk/conditions/heart-failure/), [Pneumonia](https://www.nhs.uk/conditions/pneumonia/)

### `advice_type_1_diabetes_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Being very thirsty, peeing more, feeling tired and losing weight can be signs of type 1 diabetes, which needs treatment quickly.

**Look out for:**
- Tummy pain, or feeling or being sick
- Breath that smells fruity, like pear drops or nail polish remover
- Breathing faster and more deeply than usual
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 or go to A&E if you or your child get any of the signs above, or get worse quickly

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. It can help to take a sample of pee with you. In an emergency call 999.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_tiredness_gp`

**What to do:** See a GP. They can check for causes of tiredness, for example with blood tests for anaemia, diabetes or thyroid problems.

**Look out for:**
- Losing weight without trying
- Feeling very low, or thoughts of harming yourself
- Being very thirsty and peeing more than usual

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you are very thirsty, peeing more and losing weight
- If you have thoughts of harming yourself, call 111 and choose the mental health option, or call Samaritans on 116 123. Call 999 if your life is in danger.

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Try to go to bed and get up at the same times, and aim for 6 to 9 hours of sleep
- Eat a healthy diet and exercise regularly
- Do not drink too much alcohol, and do not smoke

Source: [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/)

### `advice_tiredness_self_care`

**What to do:** It is normal to feel tired sometimes. Try these things for a few weeks. See a GP if you are still tired and do not know why.

**Look out for:**
- Tiredness that lasts a few weeks or affects your daily life
- Weight loss, low mood, or being told you make gasping or choking noises in your sleep
- Being very thirsty and peeing more than usual

**Get more help when:**
- See a GP if you get any of the signs above
- Call 999 or go to A&E if you become very sleepy or hard to wake

**Where to go:** You do not need an appointment now. See a GP if it does not get better.

**What you can do yourself:**
- Try to stick to the same sleep times and aim for 6 to 9 hours of sleep
- Relax for a couple of hours before bed, and avoid screens in the hour before sleep
- Have a healthy diet and exercise regularly
- Do not drink too much alcohol, and avoid caffeine before bed

Source: [Tiredness and fatigue](https://www.nhs.uk/symptoms/tiredness-and-fatigue/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_tired_drowsy`: Being sleepier than usual or hard to wake is a sign of sepsis, and of diabetic ketoacidosis on the Type 1 diabetes page. Applying it to tiredness is AI judgement: it is the line between being tired and being dangerously drowsy.
- `rf_tired_breathless_at_rest`: Same as the breathlessness rule. Breathlessness at rest with tiredness can be severe anaemia or heart failure.
- `rf_tired_type_1_diabetes`: The Type 1 diabetes page says an urgent GP appointment or 111 if you think you or your child has type 1 diabetes, and lists the 4 Ts: toilet, thirsty, tired, thinner. Requiring a child or weight loss, so that an adult more likely to have type 2 diabetes gets a routine appointment, is AI judgement.
- `or_tired_other_symptoms`: The ME/CFS sign (extreme tiredness for 3 months, worse after activity) is added from the conditions table on the same page.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sleep apnoea (breathing that stops and starts during sleep) | 78275009 | common | Breathing stops and starts during sleep, or gasping or choking noises: strongly supports; Feels very tired: supports; Trouble sleeping (insomnia): supports; Sleepiness affecting life, such as work, school or driving: supports; Tired for a few weeks or more, without knowing why: supports; Very sleepy or falling asleep during the day: strongly supports; Snoring: strongly supports; Overweight: supports |
| Iron deficiency anaemia (too few red blood cells, from a lack of iron) | 87522002 | rare | Skin paler than usual for weeks or longer: strongly supports; Feels very tired: strongly supports; Out of breath doing everyday things: supports; Breathlessness has come on slowly over weeks or months: supports; Heart racing, slow, skipping or fluttering: supports; Nails curve inwards like a spoon: supports |
| Kidney problems (the kidneys not working as well as they should) | 709044004 | rare | Swelling in other parts of the body too, such as the face or tummy: strongly supports; Feels very tired: supports; Swollen feet, ankles or legs: supports; Peeing more often than usual: supports; Feels sick or has been sick: supports |
| ME or CFS (long-term tiredness that gets worse after activity) | 52702003 | rare | Extreme tiredness for months, worse after activity: strongly supports; Tiredness affects daily life: strongly supports; Tired for a few weeks or more, without knowing why: strongly supports; Trouble sleeping (insomnia): supports; Aching body: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports |
| Overactive thyroid (the thyroid gland in the neck makes too much hormone) | 34486009 | rare | Feeling restless, shaky or too hot all the time: strongly supports; Losing weight without trying: strongly supports; Heart racing, slow, skipping or fluttering: supports; Feels sweaty: supports; Feels very tired: supports; Night sweats: supports; Heart beating very fast: supports; Swelling at the front of the neck: supports; Feeling anxious, worried or panicky: supports; Shaking or trembling (tremor): supports |
| Tiredness from lack of sleep, stress, lifestyle or a medicine |  | very common | Trouble sleeping (insomnia): strongly supports; Going through a stressful time or big life change: strongly supports; Drinks a lot of alcohol: supports; Started a new medicine or changed a dose in the last few weeks: supports |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |
| Underactive thyroid (the thyroid gland in the neck makes too little hormone) | 40930008 | rare | Feeling cold all the time: strongly supports; Put on weight without meaning to: supports; Feeling low, sad or depressed: supports; Feels very tired: supports; Swelling in other parts of the body too, such as the face or tummy: supports; Swollen feet, ankles or legs: supports |
| Viral infection (such as a cold, a tummy bug or another virus) | 34014006 | common | Blocked or runny nose: strongly supports; Aching body: supports; Cough: supports; Diarrhoea, or being sick: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports |
| Depression | 35489007 | uncommon | Low mood most of the day, nearly every day, for more than 2 weeks: strongly supports; Lost interest or enjoyment in things: strongly supports; Feels hopeless, or that things will never get better: supports; Feels worthless or very guilty: supports; Sleep has changed: hard to sleep, waking early, or sleeping much more: supports; Eating much more or less than usual: supports; Feels very tired: supports; Feeling low, sad or depressed: strongly supports; Withdrawn from friends and family: supports; Trouble sleeping (insomnia): supports; Not feeling hungry, or eating much less than usual: supports; Losing weight without trying: supports; Going through a stressful time or big life change: supports |
| Liver problems (such as liver damage from alcohol) | 235856003 | rare | Yellow skin or yellow whites of the eyes (jaundice): strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Not feeling hungry, or eating much less than usual: supports; Feels very tired: supports; Losing weight without trying: supports; Feels sick or has been sick: supports; Swollen feet, ankles or legs: supports; Pale poo and dark pee: strongly supports; Pain in the upper right of the tummy, just under the ribs: supports; Drinks a lot of alcohol: supports; Feeling sick (nausea): supports; Itchy skin on other parts of the body too: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
