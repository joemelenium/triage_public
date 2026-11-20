# Review pack: Ovulation pain

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
| [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/) | 2026-11-19 |  | Page last reviewed: 17 July 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | 2026-11-19 |  | Page last reviewed: 23 August 2022 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | 2026-11-19 |  | Page last reviewed: 17 February 2026 |
| [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | 2026-11-19 |  | Page last reviewed: 15 February 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Bleeding between periods or after sex](https://www.nhs.uk/symptoms/vaginal-bleeding-between-periods-or-after-sex/) | 2026-11-19 |  | Page last reviewed: 13 August 2024 |

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

## Ovulation pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ov_sudden_severe_or_shoulder`<br>One-sided tummy pain that is sharp, sudden and very bad, or with pain in the tip of the shoulder<br>**Note:** AI reading: the Pelvic pain and Ectopic pregnancy pages' emergency signs, applied to ovulation-type pain. | "Stomach ache that started suddenly and is severe" OR "Pain in the tip of the shoulder" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| `rf_ov_faint_or_bleeding`<br>One-sided tummy pain with passing out, feeling faint or dizzy, or heavy bleeding from the vagina | "Passed out (fainted)" OR "Feels light-headed" OR "Heavy bleeding from the vagina" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |

## Ovulation pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ov_severe_not_helped`<br>Tummy pain that is severe and painkillers have not helped | "Severe pain, or worse than usual, and painkillers have not helped" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/) | |
| `rf_ov_may_be_pregnant`<br>Tummy pain and may be pregnant | "Pregnant, or could be pregnant" OR "Pregnant (a positive test, or told by a midwife or doctor)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/) | |
| `rf_ov_keeps_coming_back`<br>Tummy pain that keeps coming back<br>**Note:** Taken directly from the source, but ovulation pain comes back each month by its nature, so this would send most people to urgent care. Soft, so likely ovulation pain can lower it. Needs clinical review. | "Tummy or pelvic pain that keeps coming back or does not go away" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/) | |
| `rf_ov_temperature_sick_or_discharge`<br>One-sided tummy pain with a high temperature, feeling sick, or unusual discharge<br>**Note:** The Pelvic pain page's urgent signs, applied to ovulation-type pain. The Ovarian cyst page also says pain with feeling sick needs urgent help. | "Very high temperature, or feels hot, cold or shivery" OR "Feels sick or has been sick" OR "Vaginal discharge that is unusual" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |

## Ovulation pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Ovulation pain with nothing that needs more help: ease it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Ovulation pain usually lasts a short time and is nothing to worry about*
- Source: [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Ovulation pain (pain midway between periods) | Do you get pain on one side, low in your tummy, about 2 weeks before your period? This is when an egg is released (ovulation). |  | [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Stomach ache that started suddenly and is severe | Did the pain in your tummy start suddenly, and is it severe? Severe pain is there all the time and is so bad it is hard to think or talk. |  | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Pain in the tip of the shoulder | Do you have pain in the tip of your shoulder, where your arm meets your shoulder? |  | [Ectopic pregnancy](https://www.nhs.uk/conditions/ectopic-pregnancy/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heavy bleeding from the vagina | Are you bleeding heavily from your vagina? For example, soaking a pad soon after putting it on, or passing large clots. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Severe pain, or worse than usual, and painkillers have not helped | Is the pain severe or worse than usual, and have painkillers not helped? |  | [Menstrual pain](https://www.nhs.uk/symptoms/period-pain/) | |
| Pregnant, or could be pregnant | Are you pregnant, or could you be? For example, your period is late, or you have had sex without contraception since your last period. |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Pregnant (a positive test, or told by a midwife or doctor) | Are you pregnant? Answer yes if you have had a positive pregnancy test, or a midwife or doctor has told you. |  | [Vaginal bleeding in pregnancy](https://www.nhs.uk/pregnancy/common-symptoms/vaginal-bleeding/) | |
| Tummy or pelvic pain that keeps coming back or does not go away | Does the pain keep coming back, or has it not gone away? |  | [Pelvic pain](https://www.nhs.uk/symptoms/pelvic-pain/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Vaginal discharge that is unusual | Do you have vaginal discharge that is unusual for you? For example, it has changed colour, smell or texture, or there is more than usual. | 271939006 | [Vaginal discharge](https://www.nhs.uk/symptoms/vaginal-discharge/) | |

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

### `advice_ovulation_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Tummy pain that is severe, keeps coming back, or happens when you could be pregnant needs checking.

**Look out for:**
- A sharp, sudden and very bad pain in your tummy
- Feeling faint or dizzy, or passing out
- Pain in the tip of your shoulder

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

Source: [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/)

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

### `advice_ovulation_pain_self_care`

**What to do:** Ovulation pain is common and is usually nothing to worry about. It happens when an egg is released, about 2 weeks before your period, and usually lasts a short time.

**Look out for:**
- Pain that is severe and painkillers do not help
- Pain that keeps coming back or does not go away
- Pain when you could be pregnant

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get any of these

**Where to go:** You can look after this yourself. A pharmacist can give advice on painkillers.

**What you can do yourself:**
- Have a warm bath
- Take paracetamol or ibuprofen as the packet says

Source: [Ovulation pain](https://www.nhs.uk/symptoms/ovulation-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ov_sudden_severe_or_shoulder`: AI reading: the Pelvic pain and Ectopic pregnancy pages' emergency signs, applied to ovulation-type pain.
- `rf_ov_keeps_coming_back`: Taken directly from the source, but ovulation pain comes back each month by its nature, so this would send most people to urgent care. Soft, so likely ovulation pain can lower it. Needs clinical review.
- `rf_ov_temperature_sick_or_discharge`: The Pelvic pain page's urgent signs, applied to ovulation-type pain. The Ovarian cyst page also says pain with feeling sick needs urgent help.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Ectopic pregnancy (a pregnancy growing outside the womb) | 34801009 | very rare | Pain low down on one side of the tummy: strongly supports; Pelvic pain (pain low down in the tummy): strongly supports; Vaginal bleeding between periods or after sex: supports; Missed or late period: supports; Stomach pain in pregnancy: supports; Vaginal bleeding in pregnancy: supports; Pregnant, or could be pregnant: strongly supports; Pain low down in the tummy, below the belly button: strongly supports; Unusual bleeding or discharge from the vagina: supports; Pain in the tip of the shoulder: supports; Feels light-headed: supports; Passed out (fainted): supports; Pain when pooing: supports |
| Endometriosis (tissue like the lining of the womb growing in other places) | 129103003 | uncommon | Period pain stops usual daily activities: strongly supports; Tummy or pelvic pain that keeps coming back or does not go away: strongly supports; Period pain: strongly supports; Pain deep inside during or after sex: supports; Pain when pooing: supports; Feels very tired: supports; Struggling to get pregnant: supports; Pelvic pain (pain low down in the tummy): supports |
| Ovulation pain (pain when an egg is released, between periods) | 43548008 | uncommon | Pain low down on one side of the tummy: strongly supports; Ovulation pain (pain midway between periods): strongly supports; The pain switches sides from month to month: supports; The pain lasts from a few minutes to 2 days: supports |
| Ovarian cyst (a fluid-filled sac on an ovary) |  | uncommon | Pain low down on one side of the tummy: strongly supports; Pain deep inside during or after sex: supports; Bloated regularly, or it does not go away: supports; Peeing more often than usual: supports; Hard to start peeing, or a weak or stop-start flow: supports; Constipation: supports; Periods have changed: irregular, heavier, more painful or stopped: supports |
| Twisted ovary (ovarian torsion), or a burst ovarian cyst | 13595002 | very rare | Stomach ache that started suddenly and is severe: strongly supports; Pain low down on one side of the tummy: strongly supports; Feels sick or has been sick: strongly supports; Pelvic pain that is severe, getting worse, or hurts when moving or touched: supports; Feels light-headed: supports; Pain low down in the tummy, below the belly button: strongly supports; Being sick: supports; Feeling sick (nausea): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
