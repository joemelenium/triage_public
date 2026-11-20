# Review pack: Stomach pain in pregnancy

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
| [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | 2026-11-19 |  | Page last reviewed: 18 November 2024 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | 2026-11-19 |  | Page last reviewed: 23 March 2026 |
| [Your baby's movements](https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/) | 2026-11-19 |  | Page last reviewed: 8 July 2024 |
| [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/) | 2026-11-19 |  | Page last reviewed: 11 January 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | 2026-11-19 |  | Page last reviewed: 15 February 2024 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Signs that labour has begun](https://www.nhs.uk/pregnancy/labour-and-birth/signs-that-labour-has-begun/) | 2026-11-19 |  | Page last reviewed: 9 November 2023 |

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

## Stomach pain in pregnancy red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_spp_severe_with_bleeding`<br>Pregnant with severe tummy pain and bleeding, or heavy bleeding: possible placental abruption | "Heavy bleeding from the vagina" OR ("Severe pain" AND "Vaginal bleeding in pregnancy") | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_severe_pain`<br>Pregnant with severe tummy pain<br>**Note:** Source difference: the page says call the maternity unit straight away for severe pain, and call 999 if the pain is severe with a placental abruption. The more urgent is used, marked soft. | "Severe pain" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_shoulder_or_faint`<br>Pregnant with tummy pain and pain in the tip of the shoulder, or feeling faint, dizzy, or passing out: possible burst ectopic pregnancy or bleeding inside<br>**Note:** The Ectopic pregnancy page lists shoulder tip pain, feeling very dizzy and fainting. The Vaginal bleeding in pregnancy page says 999 for these with bleeding. | "Pain in the tip of the shoulder" OR "Passed out (fainted)" OR "Feels light-headed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| `rf_spp_fit`<br>Pregnant and has had a fit (seizure): possible eclampsia | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |

## Stomach pain in pregnancy red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_spp_bleeding`<br>Pregnant with tummy pain and vaginal bleeding or spotting | "Vaginal bleeding in pregnancy" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit straight away, or NHS 111* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_labour_signs`<br>Pregnant with tummy pain and regular cramps or tightenings, lower back pain, or fluid leaking from the vagina<br>**Note:** The Signs that labour has begun page says call urgently if your waters break, or you are less than 37 weeks pregnant and think you are in labour. | "Regular cramps or tightenings in the tummy" OR "Pain in the lower back" OR "Fluid leaking from the vagina" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit straight away, or NHS 111* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_discharge`<br>Pregnant with tummy pain and unusual discharge | "Vaginal discharge that is unusual" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit straight away, or NHS 111* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_urine`<br>Pregnant with tummy pain and pain when peeing, needing to pee more often, or pee that looks cloudy, pink, red or brown | "Pain, burning or stinging when peeing" OR "Peeing more often than usual" OR "Cloudy pee" OR "Blood in pee" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit straight away, or NHS 111* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_not_eased_by_rest`<br>Pregnant with tummy pain that is severe, or has not gone after resting for 30 to 60 minutes<br>**Note:** Severe pain (severe_pain, which a 'yes' to severe tummy pain also means) is included because it is the same sign asked another way. The 999 rule for severe pain is soft, and without this a likely mild cause could take severe pain below the page's 'call your maternity unit straight away'. | "Pain that has not gone after 30 to 60 minutes of rest" OR "Severe pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit straight away, or NHS 111* | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| `rf_spp_baby_moving_less`<br>Baby moving less than usual | "Baby moving less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your midwife or maternity unit now. Do not wait until the next day.* | [Your baby's movements](https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/) | |
| `rf_spp_pre_eclampsia`<br>Pregnant with signs of pre-eclampsia: pain below the ribs, severe headache, vision problems, sudden swelling, being sick or feeling very unwell | "Pain just below the ribs" OR "Severe headache that painkillers do not help" OR "Change in sight or loss of vision" OR "Sudden swelling of the face, hands or feet" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit now. If you cannot, call 111.* | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| `rf_spp_cannot_keep_food_down`<br>Pregnant and being sick many times a day, unable to keep food or drink down | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your midwife, GP or hospital as soon as possible* | [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/) | |

## Stomach pain in pregnancy: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Pregnant with mild tummy pain that goes away with rest or a change of position, and none of the warning signs**
- Outcome: Self-manageable, Self-care, No appointment needed. *Probably nothing to worry about. Call your maternity unit if you are worried.*
- Source: [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/)
- **Note:** The page says mild pain that goes away with rest is probably nothing to worry about. Only reached after every warning sign, including pain not eased by rest, has been checked. Likely conditions can raise it.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Stomach pain in pregnancy | Are you pregnant and have pain or cramps in your tummy? | 309737007 | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Vaginal bleeding in pregnancy | Are you pregnant and bleeding from your vagina? This includes spots of pink, red or brown blood. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Pain in the tip of the shoulder | Do you have pain in the tip of your shoulder, where your arm meets your shoulder? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Regular cramps or tightenings in the tummy | Are you having regular cramps or tightenings in your tummy, which come and go? |  | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| Pain in the lower back | Is the pain in your lower back? | 279039007 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Fluid leaking from the vagina | Is fluid leaking or gushing from your vagina? It could be your waters breaking. |  | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |
| Vaginal discharge that is unusual | Do you have vaginal discharge that is unusual for you? For example, it has changed colour, smell or texture, or there is more than usual. | 271939006 | [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Cloudy pee | Is your pee cloudy? | 7766007 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Pain that has not gone after 30 to 60 minutes of rest | Has the pain not gone away after resting for 30 to 60 minutes? |  | [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/) | |
| Baby moving less than usual | Is your baby moving less than usual? Or have the movements changed, or stopped? |  | [Your baby's movements](https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/) | |
| Pain just below the ribs | Do you have pain just below your ribs, especially on the right side? |  | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| Severe headache that painkillers do not help | Do you have a severe headache that does not go away with painkillers? |  | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Sudden swelling of the face, hands or feet | Have your face, hands or feet suddenly swollen? |  | [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |

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

### `advice_pregnancy_999`

**What to do:** Call 999 now. You need treatment straight away.

**Look out for:**
- Passing out, or feeling very faint
- Bleeding getting heavier

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself. Bring your maternity notes if you have them.

**What you can do yourself:**
- Lie down while you wait for help

Source: [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/), [Miscarriage](https://www.nhs.uk/conditions/miscarriage/), [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/)

### `advice_stomach_pain_pregnancy_urgent`

**What to do:** Call your maternity unit now. If you cannot reach it, call NHS 111. Your symptoms need to be checked today.

**Look out for:**
- Severe tummy pain, or pain that does not go away
- Bleeding from your vagina
- Your baby moving less than usual
- Feeling faint, or pain in the tip of your shoulder

**Get more help when:**
- Call 999 if the pain or bleeding is severe, or you feel faint

**Where to go:** Call your maternity unit. If you are less than 20 weeks pregnant, your GP or an early pregnancy unit may be able to help. If you cannot reach them, call 111.

Source: [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/), [Signs that labour has begun](https://www.nhs.uk/pregnancy/labour-and-birth/signs-that-labour-has-begun/), [Your baby's movements](https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/)

### `advice_baby_movements_urgent`

**What to do:** Call your midwife or maternity unit now. Do not wait until the next day, even if it is the middle of the night. They need to check your baby's movements and heartbeat.

**Look out for:**
- No movements at all
- Bleeding from your vagina, or severe tummy pain

**Get more help when:**
- Call 999 if you have heavy bleeding or severe pain

**Where to go:** Call your midwife or maternity unit. Call 111 if you cannot reach them. Do not use a home heartbeat kit to check your baby yourself.

Source: [Your baby's movements](https://www.nhs.uk/pregnancy/keeping-well/your-babys-movements/)

### `advice_pre_eclampsia_urgent`

**What to do:** Get urgent medical help now. Call your maternity unit. These can be signs of pre-eclampsia, a condition that causes high blood pressure in pregnancy. It needs checking straight away.

**Look out for:**
- A fit (seizure)
- A severe headache that does not go away, or your headache getting worse
- Blurred vision, flashing lights, or your vision getting worse
- Pain just below the ribs
- Being sick, or sudden swelling of the face, hands or feet

**Get more help when:**
- Call 999 if you have a fit, or feel very unwell

**Where to go:** Call your maternity unit. If you have recently given birth, or cannot reach your maternity unit, call 111.

Source: [Pre-eclampsia](https://www.nhs.uk/conditions/pre-eclampsia/)

### `advice_severe_sickness_pregnancy_urgent`

**What to do:** Contact your GP or midwife, or call NHS 111, as soon as possible today. Being sick many times a day and not keeping food or drink down can be severe sickness in pregnancy. You may need treatment to stop you losing too much water from your body.

**Look out for:**
- Peeing less than usual, or dark, strong-smelling pee
- Feeling dizzy or faint
- Blood in your sick
- Tummy pain

**Get more help when:**
- Go to A&E or call 999 if you feel very faint, pass out, or cannot keep any fluids down at all

**Where to go:** Contact your GP or midwife, or call 111 or use 111 online. If you have a maternity unit, you can call them.

**What you can do yourself:**
- Sip fluids little and often
- Do a pregnancy test if you have not done one

Source: [Severe vomiting in pregnancy](https://www.nhs.uk/pregnancy/complications/severe-vomiting/)

### `advice_stomach_pain_pregnancy_self_care`

**What to do:** Tummy pains are common in pregnancy. Mild pain that eases when you rest or move is usually nothing to worry about.

**Look out for:**
- Pain that is severe, or does not go away after resting for 30 to 60 minutes
- Bleeding or unusual discharge from your vagina
- Regular cramps or tightenings
- Pain when you pee, or needing to pee more often

**Get more help when:**
- Call your maternity unit straight away if you get any of these. If you cannot reach it, call 111.
- Call your maternity unit if you are worried about your pains

**Where to go:** You can look after this yourself. Mention it to your midwife at your next check.

**What you can do yourself:**
- Rest, and change position
- Drink plenty of water and eat foods with fibre, to avoid constipation
- Take paracetamol if you need to. Do not take ibuprofen in pregnancy unless a doctor tells you to.

Source: [Stomach pain in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/stomach-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_spp_severe_pain`: Source difference: the page says call the maternity unit straight away for severe pain, and call 999 if the pain is severe with a placental abruption. The more urgent is used, marked soft.
- `rf_spp_shoulder_or_faint`: The Ectopic pregnancy page lists shoulder tip pain, feeling very dizzy and fainting. The Vaginal bleeding in pregnancy page says 999 for these with bleeding.
- `rf_spp_labour_signs`: The Signs that labour has begun page says call urgently if your waters break, or you are less than 37 weeks pregnant and think you are in labour.
- `rf_spp_not_eased_by_rest`: Severe pain (severe_pain, which a 'yes' to severe tummy pain also means) is included because it is the same sign asked another way. The 999 rule for severe pain is soft, and without this a likely mild cause could take severe pain below the page's 'call your maternity unit straight away'.
- `stomach_pain_in_pregnancy default outcome`: The page says mild pain that goes away with rest is probably nothing to worry about. Only reached after every warning sign, including pain not eased by rest, has been checked. Likely conditions can raise it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Appendicitis (a swollen appendix, a pouch on the bowel) | 74400008 | uncommon | Pain started around the belly button and moved to the lower right: strongly supports; Pain in the lower right side of the tummy: strongly supports; Tummy pain worse when moving, coughing or going over bumps: strongly supports; Not feeling hungry, or eating much less than usual: strongly supports; Stomach ache: strongly supports; Stomach ache gradually getting worse: supports; Feeling sick (nausea): supports; Being sick: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |
| Ectopic pregnancy (a pregnancy growing outside the womb) | 34801009 | very rare | Pain low down on one side of the tummy: strongly supports; Pelvic pain (pain low down in the tummy): strongly supports; Vaginal bleeding between periods or after sex: supports; Missed or late period: supports; Stomach pain in pregnancy: supports; Vaginal bleeding in pregnancy: supports; Pregnant, or could be pregnant: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: supports; Pain in the tip of the shoulder: supports; Feels light-headed: supports; Passed out (fainted): supports; Pain when pooing: supports |
| Severe sickness in pregnancy (hyperemesis gravidarum) | 14094001 | rare | Keeps being sick and cannot keep fluids down: strongly supports; Pregnant, or could be pregnant: strongly supports; Feels sick or has been sick: strongly supports; Signs of dehydration: strongly supports; Losing weight without trying: supports; Feels light-headed: supports |
| Miscarriage (loss of a pregnancy before 24 weeks) | 17369002 | very rare | Pink, grey or white lumps coming from the vagina: strongly supports; Vaginal bleeding in pregnancy: strongly supports; Stomach pain in pregnancy: supports; Heavy bleeding from the vagina: supports; Vaginal bleeding between periods or after sex: supports; Pelvic pain (pain low down in the tummy): supports; Missed or late period: supports |
| Placental abruption (the placenta starts to come away from the wall of the womb) | 415105001 | very rare | Severe stomach ache: strongly supports; Tummy very painful to touch, or hard: strongly supports; Stomach pain in pregnancy: strongly supports; Vaginal bleeding in pregnancy: supports; Pain in the lower back: supports; Baby moving less than usual: supports |
| Pre-eclampsia (high blood pressure in pregnancy that can cause serious problems) | 398254007 | very rare | Pain just below the ribs: strongly supports; Severe headache that painkillers do not help: strongly supports; Change in sight or loss of vision: strongly supports; Sudden swelling of the face, hands or feet: supports; Feels sick or has been sick: supports; Feels very unwell: supports; Pregnant, or gave birth in the last 6 weeks: strongly supports; Swelling in other parts of the body too, such as the face or tummy: supports; Swelling is severe, painful or came on suddenly: supports |
| Harmless pregnancy aches: stretching ligaments, constipation or trapped wind |  | very common | Mild pain that goes away with rest or a change of position: strongly supports; Sharp cramp on one side when moving: supports; Pain low down on one side of the tummy: supports; Changes in pooing for 3 weeks or more: supports |
| Labour starting early (premature labour), or waters breaking early | 6383007 | very rare | Regular cramps or tightenings in the tummy: strongly supports; Stomach pain in pregnancy: strongly supports; Pain in the lower back: supports; Fluid leaking from the vagina: supports; Vaginal bleeding in pregnancy: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
