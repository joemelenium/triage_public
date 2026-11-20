# Review pack: Pelvic pain

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
| [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | 2026-11-19 |  | Page last reviewed: 24 November 2025 |
| [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | 2026-11-19 |  | Page last reviewed: 17 December 2025 |
| [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | 2026-11-19 |  | Page last reviewed: 15 February 2024 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Constipation](https://www.nhs.uk/conditions/constipation/) | 2026-11-19 |  | Page last reviewed: 26 October 2023 |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | 2026-11-19 |  | Page last reviewed: 13 August 2024 |
| [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Bloating](https://www.nhs.uk/symptoms/bloating/) | 2026-11-19 |  | Page last reviewed: 21 January 2026 |
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

## Pelvic pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pp_severe_or_worsening`<br>Pelvic pain that is severe, getting worse, or hurts when moving or touching the area<br>**Note:** A sharp, sudden and very bad pain is included from the Ectopic pregnancy and Pelvic inflammatory disease pages, which give the same advice. | "Pelvic pain that is severe, getting worse, or hurts when moving or touched" OR "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_faint_or_dizzy`<br>Pelvic pain with feeling faint, dizzy or light-headed, or passing out | "Feels light-headed" OR "Passed out (fainted)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_shoulder_tip`<br>Pelvic pain with pain in the tip of the shoulder | "Pain in the tip of the shoulder" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_difficulty_breathing`<br>Pelvic pain with difficulty breathing | "Difficulty breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_heavy_bleeding`<br>Pelvic pain with heavy bleeding from the vagina | "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_infection_signs`<br>Pelvic pain with a very high temperature and unusual discharge, or feeling very unwell: possible pelvic infection<br>**Note:** Source difference: the Pelvic inflammatory disease page says call 999 or go to A&E for symptoms of PID with a very high temperature or feeling sick. The Pelvic pain page says get help from 111 for pelvic pain with a high temperature. The more urgent is used for pain with unusual discharge or feeling unwell, marked soft. | "Very high temperature, or feels hot, cold or shivery" AND ("Vaginal discharge that is unusual" OR "Feels very unwell" OR "Feels sick or has been sick") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |

## Pelvic pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pp_may_be_pregnant`<br>Pelvic pain in someone who is or may be pregnant<br>**Note:** The Ectopic pregnancy page gives the same advice for tummy pain in someone who might be pregnant, even with a negative test. | "Pregnant, or could be pregnant" OR "Pregnant (a positive test, or told by a midwife or doctor)" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111. If you are 20 weeks pregnant or more, contact your midwife or maternity unit.* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_high_temperature`<br>Pelvic pain with a very high temperature, or feeling hot, cold or shivery | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_sick`<br>Pelvic pain with feeling sick or being sick, or diarrhoea and vomiting | "Feels sick or has been sick" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_peeing_or_pooing`<br>Pelvic pain with difficulty peeing or pooing, blood in pee or poo, or pain when peeing | ("Hard to start peeing, or a weak or stop-start flow" OR "Constipation") OR ("Blood in pee" OR "Bleeding from the bottom, or blood in poo") OR "Pain, burning or stinging when peeing" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_discharge_or_bleeding`<br>Pelvic pain with unusual discharge, fluid or bleeding from the vagina | "Vaginal discharge that is unusual" OR "Vaginal bleeding between periods or after sex" OR "Fluid leaking from the vagina" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_pp_peeing_more`<br>Pelvic pain and needing to pee more than usual<br>**Note:** Taken from the Pelvic pain page ('pain when peeing or need to pee more than usual'). Soft, because needing to pee more often on its own is also a symptom of slow-growing causes such as fibroids, which need a GP, not urgent care. AI reading. | "Peeing more often than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |

## Pelvic pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_pp_keeps_coming_back`<br>Pelvic pain that comes and goes or does not go away | "Tummy or pelvic pain that keeps coming back or does not go away" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `or_pp_ovarian_cancer_signs`<br>Pelvic pain with bloating, feeling full quickly, weight loss, or bowel changes that do not go away | "Bloated regularly, or it does not go away" OR "Feels full quickly or has no appetite" OR "Losing weight without trying" OR "Changes in pooing for 3 weeks or more" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `or_pp_pain_during_sex`<br>Pelvic pain with pain during or after sex | "Pain deep inside during or after sex" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |

## Default outcome

Used when no rule fires.

- **Pelvic pain with nothing that needs more urgent help: see a GP if worried, and do not self-diagnose**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/)
- **Note:** Not a floor: the page says see a GP if worried. Period pain or ovulation pain that is clearly likely may lower this to self-care.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Pelvic pain (pain low down in the tummy) | Do you have pain low down in your tummy, between your hips (your pelvis)? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Pelvic pain that is severe, getting worse, or hurts when moving or touched | Is the pain severe or getting worse? Or does it hurt when you move or touch the area? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Pain in the tip of the shoulder | Do you have pain in the tip of your shoulder, where your arm meets your shoulder? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Vaginal discharge that is unusual | Do you have vaginal discharge that is unusual for you? For example, it has changed colour, smell or texture, or there is more than usual. | 271939006 | [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Pregnant, or could be pregnant | Are you pregnant, or could you be? For example, your period is late, or you have had sex without contraception since your last period. |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Pregnant (a positive test, or told by a midwife or doctor) | Are you pregnant? Answer yes if you have had a positive pregnancy test, or a midwife or doctor has told you. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Hard to start peeing, or a weak or stop-start flow | Is it hard to start peeing, do you have to strain, or is your flow weak or stop-start? | 162128006 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Constipation | Are you constipated? This means pooing less often than usual, or finding it hard to poo. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Vaginal bleeding between periods or after sex | Are you bleeding from your vagina between periods or after sex? |  | [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | |
| Fluid leaking from the vagina | Is fluid leaking or gushing from your vagina? It could be your waters breaking. |  | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |
| Peeing more often than usual | Are you peeing more often than usual, especially at night? | 28442001 | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Tummy or pelvic pain that keeps coming back or does not go away | Does the pain keep coming back, or has it not gone away? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Bloated regularly, or it does not go away | Have you felt bloated, or had a swollen tummy, most days, or on and off for 3 weeks or more? Or does it not go away, even when you change what you eat? |  | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Feels full quickly or has no appetite | Do you feel full quickly when you eat, or have you lost your appetite? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Changes in pooing for 3 weeks or more | For 3 weeks or more, has your poo changed in a way that is not usual for you? For example, it is softer, thinner or runnier, you poo more often, or you are constipated. | 88111009 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Pain deep inside during or after sex | Do you get pain deep inside during or after sex? | 247419003 | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |

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

### `advice_pelvic_pain_emergency`

**What to do:** Call 999 or go to A&E now. Pelvic pain with these signs can mean something serious that needs treatment straight away.

**Look out for:**
- Feeling faint, dizzy or light-headed, or passing out
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina
- Pain that gets worse very quickly

**Get more help when:**
- Call 999 if you pass out, feel very faint, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/)

### `advice_pid_emergency`

**What to do:** Go to A&E now, or call 999. Pelvic pain with a high temperature or feeling very unwell can be a serious infection of the womb, tubes or ovaries. It needs treatment straight away.

**Look out for:**
- Feeling very unwell, or getting worse quickly
- Feeling dizzy or faint
- Being sick and not able to keep fluids down

**Get more help when:**
- Call 999 if you feel faint, confused or very unwell, or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/)

### `advice_possible_ectopic_urgent`

**What to do:** Get help today. Ask for an urgent GP appointment or call NHS 111. Tummy pain or unusual bleeding when you could be pregnant needs checking as soon as possible. It could be an ectopic pregnancy, where a pregnancy grows outside the womb.

**Look out for:**
- A sharp, sudden and very bad pain in your tummy
- Feeling very dizzy or faint, or passing out
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina

**Get more help when:**
- Call 999 or go to A&E straight away if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. If you are under the care of an early pregnancy unit or maternity unit, you can call them.

**What you can do yourself:**
- Do a pregnancy test if you have not done one, but get help even if it is negative

Source: [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/), [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/)

### `advice_pelvic_pain_urgent`

**What to do:** Get help from NHS 111 today. Your pelvic pain needs to be checked soon.

**Look out for:**
- The pain becoming severe or getting worse, or hurting when you move
- Feeling faint, dizzy or light-headed
- Pain in the tip of your shoulder
- Heavy bleeding from your vagina

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs
- If you are 20 weeks pregnant or more, contact your midwife or maternity unit

**Where to go:** Call 111 or use 111 online. You can also ask your GP surgery for an urgent appointment.

**What you can do yourself:**
- You can take paracetamol for the pain while you wait

Source: [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/)

### `advice_pelvic_pain_gp`

**What to do:** See a GP about your pelvic pain. Do not try to work out the cause yourself. Many things can cause it, and a GP can help find out what it is.

**Look out for:**
- The pain becoming severe or getting worse
- A high temperature, or feeling hot, cold or shivery
- Unusual discharge or bleeding from your vagina
- Pain when you pee, or blood in your pee or poo

**Get more help when:**
- Get help from 111 if you get any of these signs, or you think you may be pregnant
- Call 999 or go to A&E if the pain is severe, you feel faint or dizzy, or you have pain in the tip of your shoulder

**Where to go:** Ask your GP surgery for an appointment. The source gives no fixed time. For a possible sexually transmitted infection, you can also go to a sexual health clinic.

**What you can do yourself:**
- Take paracetamol or ibuprofen for the pain
- A hot water bottle or heat pad on your tummy can help
- Keep a note of when the pain happens, to share with the GP

Source: [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_pp_severe_or_worsening`: A sharp, sudden and very bad pain is included from the Ectopic pregnancy and Pelvic inflammatory disease pages, which give the same advice.
- `rf_pp_infection_signs`: Source difference: the Pelvic inflammatory disease page says call 999 or go to A&E for symptoms of PID with a very high temperature or feeling sick. The Pelvic pain page says get help from 111 for pelvic pain with a high temperature. The more urgent is used for pain with unusual discharge or feeling unwell, marked soft.
- `rf_pp_may_be_pregnant`: The Ectopic pregnancy page gives the same advice for tummy pain in someone who might be pregnant, even with a negative test.
- `rf_pp_peeing_more`: Taken from the Pelvic pain page ('pain when peeing or need to pee more than usual'). Soft, because needing to pee more often on its own is also a symptom of slow-growing causes such as fibroids, which need a GP, not urgent care. AI reading.
- `pelvic_pain default outcome`: Not a floor: the page says see a GP if worried. Period pain or ovulation pain that is clearly likely may lower this to self-care.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Appendicitis (a swollen appendix, a pouch on the bowel) | 74400008 | uncommon | Pain started around the belly button and moved to the lower right: strongly supports; Pain in the lower right side of the tummy: strongly supports; Tummy pain worse when moving, coughing or going over bumps: strongly supports; Not feeling hungry, or eating much less than usual: strongly supports; Stomach ache: strongly supports; Stomach ache gradually getting worse: supports; Feeling sick (nausea): supports; Being sick: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Hernia (a lump where part of the gut pushes through a weak spot in the tummy wall) |  | uncommon | A lump or swelling in the tummy or groin: strongly supports; Tummy pain worse when moving, coughing or going over bumps: supports; Pain low down in the tummy, below the belly button: supports; A bulge in the groin that may go down into the scrotum: strongly supports; Dull, dragging ache, worse when standing: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |
| Prostatitis (a swollen, painful prostate, usually from an infection) | 9713002 | rare | Pain between the testicles and bottom: strongly supports; Pain when ejaculating (coming): supports; Pain, burning or stinging when peeing: supports; Hard to start peeing, or a weak or stop-start flow: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels cold to the touch, or shivery: supports |
| Sexually transmitted infection (STI), such as chlamydia or gonorrhoea | 8098009 | uncommon | Discharge from the penis: strongly supports; Sex without a condom with a new partner in the last 3 months: strongly supports; Pain, burning or stinging when peeing: supports; Tip of the penis red, swollen, itchy or sore: supports; A sexual partner has a sexually transmitted infection: strongly supports; Discharge is green, yellow or frothy: supports; Bleeding after sex: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |
| Ectopic pregnancy (a pregnancy growing outside the womb) | 34801009 | very rare | Pain low down on one side of the tummy: strongly supports; Pelvic pain (pain low down in the tummy): strongly supports; Vaginal bleeding between periods or after sex: supports; Missed or late period: supports; Stomach pain in pregnancy: supports; Vaginal bleeding in pregnancy: supports; Pregnant, or could be pregnant: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: supports; Pain in the tip of the shoulder: supports; Feels light-headed: supports; Passed out (fainted): supports; Pain when pooing: supports |
| Endometriosis (tissue like the lining of the womb growing in other places) | 129103003 | uncommon | Period pain stops usual daily activities: strongly supports; Tummy or pelvic pain that keeps coming back or does not go away: strongly supports; Period pain: strongly supports; Pain deep inside during or after sex: supports; Pain when pooing: supports; Feels very tired: supports; Struggling to get pregnant: supports; Pelvic pain (pain low down in the tummy): supports |
| Fibroids (non-cancerous growths in or around the womb) | 95315005 | uncommon | Heavy periods: strongly supports; Passing blood clots bigger than a 10p coin: supports; Peeing more often than usual: supports; Bloated regularly, or it does not go away: supports; Pain in the lower back: supports; Pain deep inside during or after sex: supports; Periods last more than 7 days: supports; Period pain: supports |
| Miscarriage (loss of a pregnancy before 24 weeks) | 17369002 | very rare | Pink, grey or white lumps coming from the vagina: strongly supports; Vaginal bleeding in pregnancy: strongly supports; Stomach pain in pregnancy: supports; Heavy bleeding from the vagina: supports; Vaginal bleeding between periods or after sex: supports; Pelvic pain (pain low down in the tummy): supports; Missed or late period: supports |
| Ovulation pain (pain when an egg is released, between periods) | 43548008 | uncommon | Pain low down on one side of the tummy: strongly supports; Ovulation pain (pain midway between periods): strongly supports; The pain switches sides from month to month: supports; The pain lasts from a few minutes to 2 days: supports |
| Ovarian cancer | 363443007 | very rare | Bloated regularly, or it does not go away: strongly supports; Feels full quickly or has no appetite: strongly supports; Peeing more often than usual: supports; Losing weight without trying: supports; Feels very tired: supports; Changes in pooing for 3 weeks or more: supports; Pelvic pain (pain low down in the tummy): supports; Feels full after eating only a little: supports; Pain low down in the tummy, below the belly button: supports |
| Ovarian cyst (a fluid-filled sac on an ovary) |  | uncommon | Pain low down on one side of the tummy: strongly supports; Pain deep inside during or after sex: supports; Bloated regularly, or it does not go away: supports; Peeing more often than usual: supports; Hard to start peeing, or a weak or stop-start flow: supports; Constipation: supports; Periods have changed: irregular, heavier, more painful or stopped: supports |
| Twisted ovary (ovarian torsion), or a burst ovarian cyst | 13595002 | very rare | Stomach ache that started suddenly and is severe: strongly supports; Pain low down on one side of the tummy: strongly supports; Feels sick or has been sick: strongly supports; Pelvic pain that is severe, getting worse, or hurts when moving or touched: supports; Feels light-headed: supports; Pain low down in the tummy, below the belly button: strongly supports; Being sick: supports; Feeling sick (nausea): supports |
| Pelvic infection (infection of the womb, tubes or ovaries) | 198130006 | rare | Pelvic pain (pain low down in the tummy): strongly supports; Vaginal discharge that is unusual: supports; Pain deep inside during or after sex: supports; Very high temperature, or feels hot, cold or shivery: supports; Vaginal bleeding between periods or after sex: supports; Sex without a condom with a new partner in the last 3 months: supports; A sexual partner has a sexually transmitted infection: supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: strongly supports; Pain, burning or stinging when peeing: supports; Feels very unwell: supports |
| Period pain (cramps from the womb tightening during a period) | 65754002 | common | Pain starts just before or at the start of a period and lasts up to 3 days: strongly supports; Period pain: strongly supports; Period cramps spread to the back and thighs: supports; Periods started in the last 2 years: supports; Tummy pain that comes with periods: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Cramping tummy pain that comes and goes in waves: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
