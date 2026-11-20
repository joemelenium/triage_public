# Review pack: Pain when peeing, or peeing more often

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
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | 2026-11-19 |  | Page last reviewed: 19 February 2024 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Urinary incontinence: symptoms](https://www.nhs.uk/conditions/urinary-incontinence/symptoms/) | 2026-11-19 |  | Page last reviewed: 15 June 2023 |
| [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 10 February 2025 |
| [Non-gonococcal urethritis](https://www.nhs.uk/conditions/urethritis/) | 2026-11-19 |  | Page last reviewed: 10 May 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | 2026-11-19 |  | Page last reviewed: 16 October 2023 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/) | 2026-11-19 |  | Page last reviewed: 16 December 2024 |
| [Syphilis](https://www.nhs.uk/conditions/syphilis/) | 2026-11-19 |  | Page last reviewed: 17 March 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Chlamydia](https://www.nhs.uk/conditions/chlamydia/) | 2026-11-19 |  | Page last reviewed: 24 October 2024 |

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

## Pain when peeing, or peeing more often red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pp_drowsy`<br>Signs of a urine infection and very drowsy, hard to wake or finding it hard to speak<br>**Note:** Sudden confusion is in the universal red flags. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_sepsis_skin`<br>Blotchy skin, or a rash that does not fade when pressed: possible sepsis<br>**Note:** The Prostatitis page lists these as 999 signs of sepsis. The Sepsis page gives the same advice. | "Blotchy or mottled skin" OR "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Prostatitis](https://www.nhs.uk/conditions/prostatitis/) | |
| `rf_pp_sepsis_breathing`<br>Breathing very fast, with a high or very low temperature or shivering: possible sepsis<br>**Note:** Requiring a high or very low temperature is AI judgement, so that fast breathing from worry is not sent to A&E on its own. | "Breathing very fast" AND ("Very high temperature, or feels hot, cold or shivery" OR "Very low temperature (below 36C)") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_pp_diabetes_emergency`<br>Peeing more and very thirsty, with being sick, fast deep breathing or fruity-smelling breath: possible diabetic ketoacidosis | "Feeling very thirsty all the time" AND ("Being sick" OR "Breathing faster and more deeply than usual" OR "Breath smells fruity") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Pain when peeing, or peeing more often red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pp_temperature`<br>A very high or very low temperature, or feeling hot, cold or shivery: possible kidney infection | "Very high temperature, or feels hot, cold or shivery" OR "Very low temperature (below 36C)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_loin_pain`<br>Pain in the back, just under the ribs: possible kidney infection or kidney stone<br>**Note:** The Kidney infection and Kidney stones pages give the same advice. | "Pain in the back or side, just under the ribs" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_lower_tummy_pain`<br>Pain in the lower tummy<br>**Note:** The UTI page lists lower tummy pain as a reason for an urgent appointment, as a possible sign of kidney infection. It is also a common sign of a simple bladder infection, so it is marked soft: a likely bladder infection with nothing else can lower it. | "Pain low down in the tummy, below the belly button" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_blood_in_pee`<br>Blood in the pee<br>**Note:** The blood in urine entry symptom also applies once this is reported. | "Blood in pee" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_cannot_pee`<br>Unable to pee<br>**Note:** The unable to pee entry symptom also applies once this is reported, with its own emergency rules. | "Unable to pee" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| `rf_pp_not_better`<br>Symptoms getting worse quickly, or not better within 2 days of starting treatment | "Getting worse quickly, or not better within 2 days of treatment" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_higher_chance`<br>Signs of a urine infection in someone more likely to get seriously ill: pregnant, diabetes, a catheter, repeated urine infections, or a weakened immune system<br>**Note:** The page says pregnant. The existing question also covers giving birth in the last 6 weeks, which is more cautious. | "Pregnant, or gave birth in the last 6 weeks" OR "Has diabetes" OR "Has a urinary catheter" OR "Keeps getting urine infections" OR "Weakened immune system" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_age_or_sex`<br>Signs of a urine infection in a child aged 15 or under, someone aged 65 or over, or a man<br>**Note:** The page also includes trans and non-binary people assigned male at birth, which the male question is meant to cover. | "Under 16 years old" OR "Aged 65 or over" OR "Male" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| `rf_pp_thirsty_weight_loss`<br>Peeing more and very thirsty, with weight loss or feeling very tired: possible diabetes<br>**Note:** The Type 1 diabetes page says urgent; the Type 2 diabetes page says see a GP. The more urgent is used, marked soft. | "Feeling very thirsty all the time" AND ("Losing weight without trying" OR "Feels very tired") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |

## Pain when peeing, or peeing more often: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_pp_prostate_signs`<br>Difficulty peeing, a weak flow, not emptying the bladder, or getting up at night to pee | "Hard to start peeing, or a weak or stop-start flow" OR "Bladder does not feel empty after peeing, or dribbling afterwards" OR "Getting up in the night to pee" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| `or_pp_long_term`<br>Peeing problems that have gone on for months<br>**Note:** The page says it is a good idea to see a GP about bladder problems such as needing to pee urgently or often. | "Peeing problems for months or longer" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Urinary incontinence: symptoms](https://www.nhs.uk/conditions/urinary-incontinence/symptoms/) | |
| `or_pp_thirsty`<br>Peeing more and very thirsty all the time: possible diabetes | "Feeling very thirsty all the time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/) | |
| `or_pp_sti`<br>Possible sexually transmitted infection: discharge from the penis, sex without a condom with a new partner, or a partner with an STI<br>**Note:** There is no sexual health clinic level of care; general practice is used, and the advice names sexual health clinics. | "Discharge from the penis" OR "Sex without a condom with a new partner in the last 3 months" OR "A sexual partner has a sexually transmitted infection" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*Go to a sexual health clinic or see a GP. The source gives no fixed time.* | [Non-gonococcal urethritis](https://www.nhs.uk/conditions/urethritis/) | |

## Default outcome

Used when no rule fires.

- **Signs of a urine infection with nothing that needs more help: see a pharmacist**
- Outcome: Routine (help needed, timing not critical), Community pharmacy, No fixed time given in the source. *See a pharmacist. They can give the same medicines as a GP for a UTI.*
- Source: [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/)
- **Note:** The page sends women and girls aged 16 to 64 who are not pregnant to a pharmacist. Everyone else is caught by the urgent rules above (men, children, 65 or over, pregnant).

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Pain when peeing, or peeing more often | Does it hurt or burn when you pee, or do you need to pee more often than usual? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Very low temperature (below 36C) | Is your temperature very low, below 36C? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| Pain in the back or side, just under the ribs | Do you have pain in your back or side, just under the ribs? | 271857006 | [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | |
| Pain low down in the tummy, below the belly button | Is the pain low down in your tummy, below your belly button? | 54586004 | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Unable to pee | Are you unable to pee, or can you only pass a few drops, even though you need to go? | 102835006 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Getting worse quickly, or not better within 2 days of treatment | Are your symptoms getting worse quickly? Or have they not got better within 2 days of starting treatment? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Has a urinary catheter | Do you have a catheter? This is a tube in your bladder that drains your pee. |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Keeps getting urine infections | Have you had 2 urine infections in the last 6 months, or 3 in the last year? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Weakened immune system | Is your body less able to fight infection than usual? For example, because of diabetes, or treatment for cancer. | 370388006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Male | Is the person who is unwell male? |  | **AI judgement, needs clinical review** | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Hard to start peeing, or a weak or stop-start flow | Is it hard to start peeing, do you have to strain, or is your flow weak or stop-start? | 162128006 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Bladder does not feel empty after peeing, or dribbling afterwards | Do you feel your bladder has not fully emptied after you pee, or do you dribble pee afterwards? | 249288007 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Getting up in the night to pee | Do you get up in the night to pee more than you used to? | 139394000 | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Peeing problems for months or longer | Have these problems with peeing been going on for months or longer? |  | [Urinary incontinence: symptoms](https://www.nhs.uk/conditions/urinary-incontinence/symptoms/) | |
| Discharge from the penis | Is there any discharge (fluid) coming from the tip of your penis, or from under the foreskin? | 9957009 | [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/) | |
| Sex without a condom with a new partner in the last 3 months | In the last 3 months, have you had sex without a condom with a new partner? |  | [Syphilis](https://www.nhs.uk/conditions/syphilis/) | |
| A sexual partner has a sexually transmitted infection | Has a sexual partner told you they have a sexually transmitted infection (STI)? |  | [Syphilis](https://www.nhs.uk/conditions/syphilis/) | |

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

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

### `advice_diabetes_emergency`

**What to do:** Call 999 or go to A&E now. Being very thirsty with being sick, deep fast breathing or fruity-smelling breath can be signs of diabetic ketoacidosis. This is when a lack of insulin makes the blood harmful, and it can be life-threatening.

**Look out for:**
- Feeling very sleepy or confused
- Tummy pain
- Breathing that is faster and deeper than usual

**Get more help when:**
- Call 999 if the person becomes very sleepy, confused or hard to wake

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_uti_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. You may have a urine infection that needs checking today, or an infection that could spread to the kidneys.

**Look out for:**
- A high temperature, or feeling hot, cold or shivery
- Pain in your back or side, just under the ribs
- Feeling or being sick
- Not having a pee all day

**Get more help when:**
- Call 999 or go to A&E if you feel confused, very drowsy or find it hard to speak
- Call 999 or go to A&E if your skin becomes blotchy or very pale. These can be signs of sepsis, a life-threatening reaction to an infection.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Take paracetamol for pain or a high temperature
- Rest and drink enough fluids so that your pee is pale
- Avoid fruit juice, coffee and alcohol, which can irritate the bladder

Source: [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/), [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/), [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/)

### `advice_cannot_pee_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 now. Not being able to pee needs checking today.

**Look out for:**
- Pain or swelling in your lower tummy
- A high temperature, or feeling hot, cold or shivery
- Numbness around your genitals or bottom, or weakness in your legs

**Get more help when:**
- Go to A&E if your lower tummy becomes painful or swollen and you still cannot pee
- Call 999 or go to A&E if you get numbness around your genitals or bottom, or weakness in both legs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Try sitting in a warm bath and relaxing to see if you can pee

Source: [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/), [Prostatitis](https://www.nhs.uk/conditions/prostatitis/)

### `advice_diabetes_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Peeing more, being very thirsty, tired or losing weight can be signs of diabetes. A quick finger-prick test can check this.

**Look out for:**
- Being sick, or tummy pain
- Breathing faster and more deeply than usual
- Breath that smells fruity, like pear drops
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 or go to A&E if any of these happen, or if symptoms get worse quickly

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Bring a sample of pee if you can.

Source: [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/)

### `advice_peeing_gp`

**What to do:** See a GP. Problems such as a weak flow, needing to pee often or getting up at night should be checked, but it is not urgent. Try not to be embarrassed.

**Look out for:**
- Not being able to pee at all
- Blood in your pee
- Pain when peeing

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Go to A&E if you cannot pee and your lower tummy is painful or swollen

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Cut down on alcohol and caffeine
- Drink less before bed, but enough during the day
- Eat enough fibre to avoid constipation

Source: [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/)

### `advice_diabetes_gp`

**What to do:** See a GP. Being very thirsty and peeing more can be signs of diabetes. A blood test can check this.

**Look out for:**
- Losing weight without trying
- Feeling very tired
- Being sick, or breathing faster and more deeply than usual

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you lose weight or feel very tired
- Call 999 or go to A&E if you are being sick, breathing fast and deeply, or feel very sleepy

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

Source: [Type 2 diabetes: symptoms](https://www.nhs.uk/conditions/type-2-diabetes/symptoms/)

### `advice_sexual_health_clinic`

**What to do:** Go to a sexual health clinic or see a GP. You may have a sexually transmitted infection (STI). Tests are free and treatment is quick.

**Look out for:**
- Pain or swelling in your testicles
- A high temperature, or pain in your joints
- A rash, or sore, red eyes

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Go to A&E straight away if you get sudden, severe pain in a testicle

**Where to go:** Go to a sexual health clinic. Many offer walk-in sessions. Or make an appointment with a GP.

**What you can do yourself:**
- Do not have sex until you have been tested and treated
- Tell recent sexual partners so they can be tested. The clinic can help with this.

Source: [Non-gonococcal urethritis](https://www.nhs.uk/conditions/urethritis/), [Chlamydia](https://www.nhs.uk/conditions/chlamydia/), [Gonorrhoea](https://www.nhs.uk/conditions/gonorrhoea/)

### `advice_uti_pharmacy`

**What to do:** See a pharmacist. They can check your symptoms and give the same medicines as a GP for a urine infection (UTI).

**Look out for:**
- A high temperature, or feeling hot, cold or shivery
- Pain in your back or side, just under the ribs
- Blood in your pee
- Symptoms getting worse, or not better within 2 days of starting treatment

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of the signs above
- Call 999 or go to A&E if you feel confused, very drowsy or find it hard to speak

**Where to go:** Go to a pharmacy. You do not need an appointment. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Take paracetamol for pain
- Rest and drink enough fluids so that your pee is pale
- Avoid fruit juice, coffee and alcohol, which can irritate the bladder

Source: [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_pp_drowsy`: Sudden confusion is in the universal red flags.
- `rf_pp_sepsis_skin`: The Prostatitis page lists these as 999 signs of sepsis. The Sepsis page gives the same advice.
- `rf_pp_sepsis_breathing`: Requiring a high or very low temperature is AI judgement, so that fast breathing from worry is not sent to A&E on its own.
- `rf_pp_loin_pain`: The Kidney infection and Kidney stones pages give the same advice.
- `rf_pp_lower_tummy_pain`: The UTI page lists lower tummy pain as a reason for an urgent appointment, as a possible sign of kidney infection. It is also a common sign of a simple bladder infection, so it is marked soft: a likely bladder infection with nothing else can lower it.
- `rf_pp_blood_in_pee`: The blood in urine entry symptom also applies once this is reported.
- `rf_pp_cannot_pee`: The unable to pee entry symptom also applies once this is reported, with its own emergency rules.
- `rf_pp_higher_chance`: The page says pregnant. The existing question also covers giving birth in the last 6 weeks, which is more cautious.
- `rf_pp_age_or_sex`: The page also includes trans and non-binary people assigned male at birth, which the male question is meant to cover.
- `rf_pp_thirsty_weight_loss`: The Type 1 diabetes page says urgent; the Type 2 diabetes page says see a GP. The more urgent is used, marked soft.
- `or_pp_long_term`: The page says it is a good idea to see a GP about bladder problems such as needing to pee urgently or often.
- `or_pp_sti`: There is no sexual health clinic level of care; general practice is used, and the advice names sexual health clinics.
- `painful_or_frequent_peeing default outcome`: The page sends women and girls aged 16 to 64 who are not pregnant to a pharmacist. Everyone else is caught by the urgent rules above (men, children, 65 or over, pregnant).

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Type 2 diabetes (high blood sugar that builds up slowly) | 44054006 | uncommon | Feeling very thirsty all the time: strongly supports; Peeing more often than usual: strongly supports; Feels very tired: supports; Still very thirsty after drinking more for several days: supports; Getting up in the night to pee: supports; Losing weight without trying: supports; Breath smells fruity: supports |
| Enlarged prostate | 266569009 | uncommon | Hard to start peeing, or a weak or stop-start flow: strongly supports; Bladder does not feel empty after peeing, or dribbling afterwards: strongly supports; Getting up in the night to pee: strongly supports; Peeing problems for months or longer: supports; Peeing more often than usual: supports |
| Genital herpes | 33839006 | common | Small painful blisters or sores around the genitals: strongly supports; Pain, burning or stinging when peeing: supports; Sex without a condom with a new partner in the last 3 months: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |
| Overactive bladder (urge incontinence) | 786457000 | common | Sudden strong need to pee, and leaks before reaching the toilet: strongly supports; Peeing more often than usual: strongly supports; Peeing problems for months or longer: strongly supports; Getting up in the night to pee: supports |
| Prostate cancer | 399068003 | very rare | Hard to start peeing, or a weak or stop-start flow: supports; Getting up in the night to pee: supports; Losing weight without trying: strongly supports; Back pain: supports; Blood in semen: supports; Blood in pee: supports |
| Prostatitis (a swollen, painful prostate, usually from an infection) | 9713002 | rare | Pain between the testicles and bottom: strongly supports; Pain when ejaculating (coming): supports; Pain, burning or stinging when peeing: supports; Hard to start peeing, or a weak or stop-start flow: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels cold to the touch, or shivery: supports |
| Sexually transmitted infection (STI), such as chlamydia or gonorrhoea | 8098009 | uncommon | Discharge from the penis: strongly supports; Sex without a condom with a new partner in the last 3 months: strongly supports; Pain, burning or stinging when peeing: supports; Tip of the penis red, swollen, itchy or sore: supports; A sexual partner has a sexually transmitted infection: strongly supports; Discharge is green, yellow or frothy: supports; Bleeding after sex: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
