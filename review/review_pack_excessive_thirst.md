# Review pack: Feeling very thirsty

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
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
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

## Feeling very thirsty red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_th_ketoacidosis_signs`<br>Very thirsty with breath that smells fruity, breathing faster and more deeply, or very sleepy: possible diabetic ketoacidosis | "Breath smells fruity" OR "Breathing faster and more deeply than usual" OR "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_th_peeing_more_and_sick`<br>Very thirsty and peeing more, with tummy pain or feeling or being sick: possible diabetic ketoacidosis<br>**Note:** The Type 1 diabetes page says call 999 or go to A&E for peeing more and very thirsty with stomach pain or being sick. Soft, because a urine infection or a tummy bug can give the same answers; diabetic ketoacidosis itself, if likely, keeps the outcome at emergency. | "Peeing more often than usual" AND ("Feels sick or has been sick" OR "Stomach ache") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Feeling very thirsty red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_th_high_sugar_or_ketones`<br>Diabetes, with blood sugar high and not coming down, or ketones raised<br>**Note:** The page says call 999 or go to A&E for ketones over 3mmol/L in the blood; the engine does not ask for the number, so the emergency signs above are used for that. | "Blood sugar high and not coming down, or ketones raised" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your diabetes care team now or get help from NHS 111* | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| `rf_th_type_1_diabetes`<br>Very thirsty and peeing more, in a child or with weight loss: possible type 1 diabetes<br>**Note:** Requiring a child or weight loss is AI judgement, as in the tiredness rule. | "Peeing more often than usual" AND ("Under 16 years old" OR "Losing weight without trying") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Feeling very thirsty: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_th_peeing_more`<br>Very thirsty and needing to pee often | "Peeing more often than usual" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| `or_th_not_better`<br>Still very thirsty after drinking more fluids for several days | "Still very thirsty after drinking more for several days" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| `or_th_pregnant`<br>Very thirsty and pregnant<br>**Note:** The page says see a GP if you are pregnant. The observation also covers having given birth in the last 6 weeks; using it here is AI judgement. | "Pregnant, or gave birth in the last 6 weeks" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or your midwife. The source gives no fixed time.* | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |

## Default outcome

Used when no rule fires.

- **Thirst with nothing that needs more help: drink more fluids and avoid alcohol and caffeine**
- Outcome: Self-manageable, Self-care, No appointment needed. *See a GP if drinking more for several days has not helped*
- Source: [Excessive thirst](https://www.nhs.uk/symptoms/thirst/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Blood sugar high and not coming down, or ketones raised | Is your blood sugar high and not coming down with your usual treatment, or are your ketones raised? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Still very thirsty after drinking more for several days | Have you been drinking more fluids for several days, but you are still very thirsty? |  | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |

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

### `advice_high_blood_sugar_urgent`

**What to do:** Call your diabetes care team now, or get help from NHS 111. Follow your sick day rules if you have them.

**Look out for:**
- Breath that smells fruity, like pear drops or nail polish remover
- Breathing faster and more deeply than usual
- Tummy pain, or being sick
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above, or your ketones are very high

**Where to go:** Call your diabetes care team, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep checking your blood sugar and ketones as your care team told you
- Keep drinking sugar-free fluids
- Do not stop taking your insulin

Source: [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/)

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

### `advice_thirst_gp`

**What to do:** See a GP. They can check what is making you so thirsty, for example diabetes or a medicine you take.

**Look out for:**
- Peeing much more than usual, especially at night
- Losing weight without trying
- Feeling very tired

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you also lose weight, or a child has these symptoms
- Call 999 or go to A&E if you are being sick, have tummy pain, fruity-smelling breath, or feel very sleepy or confused

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink more fluids, especially water
- Cut down on alcohol and caffeine

Source: [Excessive thirst](https://www.nhs.uk/symptoms/thirst/), [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_thirst_self_care`

**What to do:** Most thirst means you need to drink more. Drink more fluids and avoid alcohol and caffeine to see if it helps.

**Look out for:**
- Still being very thirsty after drinking more for several days
- Needing to pee much more often
- Signs of not having enough water in the body: dark yellow, strong-smelling pee, peeing less, or feeling dizzy

**Get more help when:**
- See a GP if drinking more for several days has not helped, you need to pee often, or you are pregnant
- Call 999 or go to A&E if you are very thirsty and being sick, have tummy pain or fruity breath, or feel very sleepy

**Where to go:** You do not need an appointment now. See a GP if it does not get better. In an emergency call 999.

**What you can do yourself:**
- Drink enough so your pee is a pale colour
- Drink more in hot weather, after exercise, or if you have been sick or have diarrhoea
- Eat less salty or spicy food

Source: [Excessive thirst](https://www.nhs.uk/symptoms/thirst/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_th_peeing_more_and_sick`: The Type 1 diabetes page says call 999 or go to A&E for peeing more and very thirsty with stomach pain or being sick. Soft, because a urine infection or a tummy bug can give the same answers; diabetic ketoacidosis itself, if likely, keeps the outcome at emergency.
- `rf_th_high_sugar_or_ketones`: The page says call 999 or go to A&E for ketones over 3mmol/L in the blood; the engine does not ask for the number, so the emergency signs above are used for that.
- `rf_th_type_1_diabetes`: Requiring a child or weight loss is AI judgement, as in the tiredness rule.
- `or_th_pregnant`: The page says see a GP if you are pregnant. The observation also covers having given birth in the last 6 weeks; using it here is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Diabetic ketoacidosis (DKA). This is when a lack of insulin makes you very ill. | 420422005 | rare | Breath smells fruity: strongly supports; Breathing faster and more deeply than usual: strongly supports; Blood sugar high and not coming down, or ketones raised: strongly supports; Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Keeps being sick and cannot keep fluids down: supports; Stomach ache: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Being sick: strongly supports; High ketones, or high blood sugar that insulin is not bringing down: strongly supports; Breathing very fast: supports; Losing weight without trying: supports; Feels very tired: supports |
| Mild dehydration (not having enough water in the body) |  | very common | Diarrhoea, or being sick: strongly supports; Feeling very thirsty all the time: strongly supports; Unwell after being in the heat or exercising hard: supports; Feels light-headed: supports; Signs of dehydration: strongly supports; Making much less pee than usual: supports; Feels sick or has been sick: supports; Feels very tired: supports |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
