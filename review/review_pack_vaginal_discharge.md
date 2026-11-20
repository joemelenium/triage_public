# Review pack: Vaginal discharge

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
| [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | 2026-11-19 |  | Page last reviewed: 17 December 2025 |
| [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | 2026-11-19 |  | Page last reviewed: 15 February 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | 2026-11-19 |  | Page last reviewed: 24 November 2025 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
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

## Vaginal discharge red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_vd_severe_pelvic_pain`<br>Unusual discharge with pelvic pain that is severe, getting worse, sudden, or hurts to move | "Pelvic pain that is severe, getting worse, or hurts when moving or touched" OR "Stomach ache that started suddenly and is severe" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |
| `rf_vd_faint_or_heavy_bleeding`<br>Unusual discharge with pelvic symptoms and feeling dizzy or faint, or heavy bleeding<br>**Note:** The PID page lists these for someone with PID symptoms. Applying them to anyone with unusual discharge is an AI reading, so soft. | "Passed out (fainted)" OR "Feels light-headed" OR "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |
| `rf_vd_pid_temperature_or_unwell`<br>Unusual discharge and pelvic pain, with a very high temperature, feeling sick or feeling very unwell: possible pelvic infection<br>**Note:** Source difference: the PID page says 999 or A&E for PID symptoms with a very high temperature, feeling sick or very unwell. The Pelvic pain page says get help from 111 for pelvic pain with a high temperature or feeling sick. The more urgent is used, marked soft. | "Pelvic pain (pain low down in the tummy)" AND ("Very high temperature, or feels hot, cold or shivery" OR "Feels sick or has been sick" OR "Feels very unwell") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E* | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |

## Vaginal discharge red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_vd_pelvic_pain`<br>Unusual discharge with pelvic pain: possible pelvic inflammatory disease<br>**Note:** The PID page says to get urgent help if you think you have PID symptoms. The Pelvic pain page says get help from 111 for pelvic pain with unusual discharge. | "Pelvic pain (pain low down in the tummy)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/) | |
| `rf_vd_high_temperature`<br>Unusual discharge with a very high temperature, or feeling very unwell | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_vd_pregnant`<br>Pregnant, with discharge that is unusual or fluid leaking from the vagina | "Pregnant (a positive test, or told by a midwife or doctor)" OR "Fluid leaking from the vagina" | Urgent (help today)<br>Urgent care<br>Today<br>*Call your maternity unit now, or NHS 111* | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |

## Vaginal discharge: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Discharge that has changed: get it checked by a GP, NHS 111 or a sexual health clinic**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP or go to a sexual health clinic, or get help from NHS 111. The source labels this non-urgent.*
- Source: [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/)
- **Note:** The page says 'get help from NHS 111' under a non-urgent label. Mapped to a routine GP or sexual health clinic appointment. Not a floor: discharge that is clearly a normal change can lower it.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Vaginal discharge that is unusual | Do you have vaginal discharge that is unusual for you? For example, it has changed colour, smell or texture, or there is more than usual. | 271939006 | [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Pelvic pain that is severe, getting worse, or hurts when moving or touched | Is the pain severe or getting worse? Or does it hurt when you move or touch the area? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Pelvic pain (pain low down in the tummy) | Do you have pain low down in your tummy, between your hips (your pelvis)? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pregnant (a positive test, or told by a midwife or doctor) | Are you pregnant? Answer yes if you have had a positive pregnancy test, or a midwife or doctor has told you. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Fluid leaking from the vagina | Is fluid leaking or gushing from your vagina? It could be your waters breaking. |  | [Miscarriage](https://www.nhs.uk/conditions/miscarriage/) | |

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

### `advice_discharge_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Unusual discharge with pelvic pain can be an infection of the womb, tubes or ovaries, which needs treatment soon.

**Look out for:**
- Pain that becomes severe or gets worse
- A high temperature, or feeling hot, cold or shivery
- Feeling or being sick, or feeling very unwell

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. A sexual health clinic can also help.

Source: [Pelvic inflammatory disease](https://www.nhs.uk/conditions/pelvic-inflammatory-disease-pid/)

### `advice_discharge_pregnant_urgent`

**What to do:** Call your maternity unit now. If you do not have one, or cannot reach it, call NHS 111. Discharge that is unusual for you, or fluid leaking from your vagina, needs checking in pregnancy.

**Look out for:**
- Bleeding from your vagina
- Severe tummy pain
- Your baby moving less than usual

**Get more help when:**
- Call 999 if you have severe pain or heavy bleeding, or feel faint

**Where to go:** Call your maternity unit. If you are less than 20 weeks pregnant, an early pregnancy unit may be able to help. If you cannot reach either, call 111.

Source: [Miscarriage](https://www.nhs.uk/conditions/miscarriage/)

### `advice_discharge_gp`

**What to do:** Get your discharge checked by a GP or a sexual health clinic. Do not try to work out the cause yourself. Changes in discharge can be a sign of an infection that is easy to treat.

**Look out for:**
- Pain low down in your tummy
- A high temperature
- Bleeding between periods or after sex

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get pelvic pain or a high temperature

**Where to go:** Ask your GP surgery for an appointment, call 111, or go to a sexual health clinic. Many sexual health clinics have walk-in times. The source gives no fixed time.

**What you can do yourself:**
- Wash the skin around your vagina gently with warm water and a mild soap with no perfume
- Do not use perfumed soaps, gels, deodorants or scented wipes
- Do not wash inside your vagina
- Use condoms until you have been checked

Source: [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_vd_faint_or_heavy_bleeding`: The PID page lists these for someone with PID symptoms. Applying them to anyone with unusual discharge is an AI reading, so soft.
- `rf_vd_pid_temperature_or_unwell`: Source difference: the PID page says 999 or A&E for PID symptoms with a very high temperature, feeling sick or very unwell. The Pelvic pain page says get help from 111 for pelvic pain with a high temperature or feeling sick. The more urgent is used, marked soft.
- `rf_vd_pelvic_pain`: The PID page says to get urgent help if you think you have PID symptoms. The Pelvic pain page says get help from 111 for pelvic pain with unusual discharge.
- `vaginal_discharge default outcome`: The page says 'get help from NHS 111' under a non-urgent label. Mapped to a routine GP or sexual health clinic appointment. Not a floor: discharge that is clearly a normal change can lower it.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Sexually transmitted infection (STI), such as chlamydia or gonorrhoea | 8098009 | uncommon | Discharge from the penis: strongly supports; Sex without a condom with a new partner in the last 3 months: strongly supports; Pain, burning or stinging when peeing: supports; Tip of the penis red, swollen, itchy or sore: supports; A sexual partner has a sexually transmitted infection: strongly supports; Discharge is green, yellow or frothy: supports; Bleeding after sex: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports |
| Bacterial vaginosis (a change to germs in the vagina) | 419760006 | very common | Discharge smells fishy: strongly supports; Discharge is thin and watery, white or grey: strongly supports; Sex without a condom with a new partner in the last 3 months: supports; A sexual partner has a sexually transmitted infection: supports |
| Cervical cancer (cancer of the cervix, the entrance to the womb) |  | very rare | Bleeding after sex: strongly supports; Vaginal discharge that is unusual: supports; Pain deep inside during or after sex: supports; Pain in the lower back: supports; Pelvic pain (pain low down in the tummy): supports; Bleeding between periods: supports; Vaginal bleeding after the menopause: supports |
| Harmless changes on the cervix (the entrance to the womb), such as a polyp (a small soft growth) | 79342006 | common | Bleeding after sex: strongly supports; Vaginal discharge that is unusual: supports; Vaginal bleeding between periods or after sex: supports; Uses hormonal contraception: supports |
| Normal changes in discharge, for example in pregnancy |  | common | Discharge is clear or white with no strong smell: strongly supports; Discharge changes with the monthly cycle: strongly supports; Pregnant (a positive test, or told by a midwife or doctor): supports; Uses hormonal contraception: supports |
| Pelvic infection (infection of the womb, tubes or ovaries) | 198130006 | rare | Pelvic pain (pain low down in the tummy): strongly supports; Vaginal discharge that is unusual: supports; Pain deep inside during or after sex: supports; Very high temperature, or feels hot, cold or shivery: supports; Vaginal bleeding between periods or after sex: supports; Sex without a condom with a new partner in the last 3 months: supports; A sexual partner has a sexually transmitted infection: supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: strongly supports; Pain, burning or stinging when peeing: supports; Feels very unwell: supports |
| Vaginal thrush (a common yeast infection) | 72934000 | uncommon | Discharge is thick and white, like cottage cheese: strongly supports; Itchy or sore in or around the vagina: strongly supports; Pain, burning or stinging when peeing: supports; Pain deep inside during or after sex: supports |
| Womb cancer (cancer of the lining of the womb) | 93781006 | very rare | Vaginal bleeding after the menopause: strongly supports; Periods have changed: irregular, heavier, more painful or stopped: supports; Vaginal discharge that is unusual: supports; Pelvic pain (pain low down in the tummy): supports; Pain in the lower back: supports; Pain deep inside during or after sex: supports; Losing weight without trying: supports; Bleeding between periods: supports; Heavy bleeding from the vagina: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
