# Review pack: Bedwetting in children

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
| [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | 2026-11-19 |  | Page last reviewed: 31 October 2024 |
| [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | 2026-11-19 |  | Page last reviewed: 11 July 2025 |
| [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | 2026-11-19 |  | Page last reviewed: 11 November 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | 2026-11-19 |  | Page last reviewed: 09 November 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | 2026-11-19 |  | Page last reviewed: 08 June 2023 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | 2026-11-19 |  | Page last reviewed: 25 September 2026 |
| [Constipation](https://www.nhs.uk/conditions/constipation/) | 2026-11-19 |  | Page last reviewed: 26 October 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Kidney infection](https://www.nhs.uk/conditions/kidney-infection/) | 2026-11-19 |  | Page last reviewed: 13 February 2025 |
| [Smelly urine](https://www.nhs.uk/symptoms/smelly-urine/) | 2026-11-19 |  | Page last reviewed: 16 October 2023 |

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

## Bedwetting in children red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bw_diabetes_emergency`<br>Wetting the bed and very thirsty, with being sick, fast deep breathing or fruity-smelling breath: possible diabetic ketoacidosis | "Feeling very thirsty all the time" AND ("Being sick" OR "Breathing faster and more deeply than usual" OR "Breath smells fruity") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_bw_drowsy`<br>Very drowsy, hard to wake or finding it hard to speak<br>**Note:** The Kidney infection page lists drowsiness and wetting the bed as signs in young children. The Type 1 diabetes page says 999 or A&E for feeling sleepy or confused. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |

## Bedwetting in children red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bw_thirsty`<br>Wetting the bed and very thirsty all the time: possible type 1 diabetes<br>**Note:** The page says children may start wetting the bed because they are peeing more, and asks for an urgent GP appointment or 111 if you think your child has type 1 diabetes. | "Feeling very thirsty all the time" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_bw_weight_loss`<br>Wetting the bed and losing weight without trying<br>**Note:** AI reading of the Type 1 diabetes page (toilet, thirsty, tired, thinner). | "Losing weight without trying" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| `rf_bw_infection`<br>Wetting the bed with pain when peeing, a high temperature or blood in the pee: possible urine infection<br>**Note:** The UTI page says children with UTIs may wet the bed, and asks for an urgent GP appointment or 111 for a child aged 15 or under with a UTI. | "Pain, burning or stinging when peeing" OR "Very high temperature, or feels hot, cold or shivery" OR "Blood in pee" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |

## Bedwetting in children: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bw_again_after_dry`<br>Started wetting the bed again after being dry for more than 6 months | "Started wetting the bed again after being dry for 6 months" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| `or_bw_home_help_not_worked`<br>Tried things at home and the bedwetting keeps happening | "Bedwetting carries on after trying things at home" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| `or_bw_day_or_constipation`<br>Also wetting during the day, or constipated<br>**Note:** The page says bedwetting may be caused by constipation. Daytime wetting as a reason to see a GP is AI judgement. | "Also wets during the day" OR "Constipation" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| `or_bw_adult`<br>Bedwetting in someone aged 16 or over<br>**Note:** Clinical knowledge: bedwetting that continues or starts in adults should be checked for a bladder, prostate or other health problem. The page is about children. | "Aged 16 or over" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **Bedwetting with nothing else that needs help: things to try at home**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most children grow out of bedwetting. A GP or school nurse can give advice.*
- Source: [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Wetting the bed | Do you wet the bed at night? | 8009008 | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Feeling very thirsty all the time | Do you feel very thirsty all the time, even when you are drinking a lot? | 17173007 | [Excessive thirst](https://www.nhs.uk/symptoms/thirst/) | |
| Being sick | Have you been sick (vomiting)? | 422400008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Breathing faster and more deeply than usual | Are you breathing faster and more deeply than usual? |  | [Type 1 diabetes: symptoms](https://www.nhs.uk/conditions/type-1-diabetes/symptoms/) | |
| Breath smells fruity | Does your breath smell fruity, like pear drop sweets or nail polish remover? |  | [Diabetic ketoacidosis](https://www.nhs.uk/conditions/diabetic-ketoacidosis/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pain, burning or stinging when peeing | Do you have pain, burning or stinging when you pee? | 49650001 | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Blood in pee | Do you have blood in your pee, or think you might? It may look pink, red or dark brown. | 34436003 | [Blood in urine](https://www.nhs.uk/symptoms/blood-in-urine/) | |
| Started wetting the bed again after being dry for 6 months | Have you started wetting the bed again, after being dry at night for more than 6 months? |  | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| Bedwetting carries on after trying things at home | Have you tried things at home to help, but the bedwetting keeps happening? |  | [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/) | |
| Also wets during the day | Do you also wet yourself during the day? |  | [Urinary tract infections (UTIs)](https://www.nhs.uk/conditions/urinary-tract-infections-utis/) | |
| Constipation | Are you constipated? This means pooing less often than usual, or finding it hard to poo. |  | [Constipation](https://www.nhs.uk/conditions/constipation/) | |
| Aged 16 or over | Is the person who is unwell aged 16 or over? |  | **AI judgement, needs clinical review** | |

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

### `advice_bedwetting_gp`

**What to do:** See a GP or school nurse. They can check for a cause and suggest treatments such as a bedwetting alarm or medicine.

**Look out for:**
- Being very thirsty, losing weight or feeling very tired
- Pain when peeing, or a high temperature

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your child is very thirsty, losing weight or has pain when peeing
- Call 999 or go to A&E if your child is being sick, breathing fast and deeply, or very drowsy

**Where to go:** Make an appointment with a GP, or speak to the school nurse. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Give your child enough water during the day, and no drinks with caffeine
- Make sure they use the toilet regularly, including just before bed
- Do not punish your child. It is not their fault.

Source: [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/)

### `advice_bedwetting_self_care`

**What to do:** Bedwetting is common and most children grow out of it. There are things you can try at home. A GP or school nurse can also give advice.

**Look out for:**
- Your child starting to wet the bed again after being dry for 6 months
- Being very thirsty, losing weight or feeling very tired
- Pain when peeing, or a high temperature

**Get more help when:**
- See a GP if things you try at home do not help, or bedwetting starts again
- Ask for an urgent GP appointment or call 111 if your child is very thirsty, losing weight or has pain when peeing

**Where to go:** You do not need an appointment now. Speak to a GP or school nurse for advice.

**What you can do yourself:**
- Give your child enough water during the day, and no drinks with caffeine
- Make sure they use the toilet 4 to 7 times a day, including just before bed
- Use waterproof covers and a night light
- Do not punish your child. It is not their fault.

Source: [Bedwetting in children](https://www.nhs.uk/symptoms/bedwetting/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bw_drowsy`: The Kidney infection page lists drowsiness and wetting the bed as signs in young children. The Type 1 diabetes page says 999 or A&E for feeling sleepy or confused.
- `rf_bw_thirsty`: The page says children may start wetting the bed because they are peeing more, and asks for an urgent GP appointment or 111 if you think your child has type 1 diabetes.
- `rf_bw_weight_loss`: AI reading of the Type 1 diabetes page (toilet, thirsty, tired, thinner).
- `rf_bw_infection`: The UTI page says children with UTIs may wet the bed, and asks for an urgent GP appointment or 111 for a child aged 15 or under with a UTI.
- `or_bw_day_or_constipation`: The page says bedwetting may be caused by constipation. Daytime wetting as a reason to see a GP is AI judgement.
- `or_bw_adult`: Clinical knowledge: bedwetting that continues or starts in adults should be checked for a bladder, prostate or other health problem. The page is about children.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Type 1 diabetes (the body cannot make insulin, so blood sugar gets too high) | 46635009 | rare | Peeing more often than usual: strongly supports; Feeling very thirsty all the time: strongly supports; Losing weight without trying: strongly supports; Feels very tired: supports; Being sick: supports; Breathing faster and more deeply than usual: supports; Breath smells fruity: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Bedwetting that a child usually grows out of | 450845009 | very common | Has never been dry at night for long: strongly supports; A parent, brother or sister also wet the bed as a child: supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
