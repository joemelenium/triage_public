# Review pack: Fainting

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
| [Fainting](https://www.nhs.uk/symptoms/fainting/) | 2026-11-18 |  | Page last reviewed: 17 August 2026 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | 2026-11-18 |  | Page last reviewed: 17 March 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |

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

## Fainting red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fa_not_recovered`<br>Has not fully recovered after fainting, or has difficulty speaking or moving | "Not fully recovered after fainting, or trouble speaking or moving" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_slow_to_wake`<br>Could not be woken up within 1 minute | "Could not be woken within 1 minute" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_chest_pain_or_palpitations`<br>Fainted with chest pain, or a pounding, fluttering or irregular heartbeat<br>**Note:** Source difference: the Heart palpitations page says an urgent GP appointment or 111 for palpitations with fainting that have stopped. The Fainting page says call 999. The more urgent is used. | "Chest pain" OR "Heart racing, slow, skipping or fluttering" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_injured`<br>Seriously hurt before or after fainting | "Seriously hurt when they passed out, fell or had a seizure" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_shaking`<br>Shaking or jerking (a seizure or fit) with the faint<br>**Note:** A few jerks during a common faint are usual and can look like a seizure. The source still says call 999, so this is kept firm. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_exercise`<br>Fainted while exercising | "Fainted while exercising" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_lying_down`<br>Fainted while lying down | "Fainted while lying down" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| `rf_fa_headache_sudden`<br>Fainted with a headache that came on suddenly and is extremely painful<br>**Note:** The Subarachnoid haemorrhage page lists fainting as a symptom. | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_fa_short_of_breath`<br>Fainted and short of breath<br>**Note:** Clinical knowledge: fainting with breathlessness can be a blood clot in the lung or a heart problem. The breathlessness entry symptom also applies once this is reported. | "Short of breath" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Fainting red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fa_no_warning`<br>Fainted with no warning at all<br>**Note:** Clinical knowledge: fainting with no warning is more likely to have a heart cause. The Fainting page gives no urgency for this. | "Fainted with no warning at all" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_fa_heart_condition`<br>Fainted, and has a heart condition<br>**Note:** Clinical knowledge: fainting in someone with a heart condition needs checking the same day. The Fainting page lists heart problems as a cause. | "Has a heart condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_fa_family_sudden_death`<br>Fainted, and a family member died suddenly under 40 or has an inherited heart condition<br>**Note:** Clinical knowledge: some heart rhythm problems run in families and first show as fainting. | "Family member died suddenly under 40, or has an inherited heart condition" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | **AI judgement, needs clinical review** | |
| `rf_fa_low_sugar`<br>Diabetes and signs of low blood sugar (a hypo) | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Treat the low blood sugar now. If it does not improve, get help from NHS 111, or call 999 if the person becomes drowsy or confused.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Fainting: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_fa_more_than_once`<br>Fainted more than once recently | "Fainted more than once recently" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. You must tell the DVLA if you faint regularly and you drive.* | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |

## Default outcome

Used when no rule fires.

- **Fainted, with nothing that needs more urgent help: see a GP to find the cause**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Fainting](https://www.nhs.uk/symptoms/fainting/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Not fully recovered after fainting, or trouble speaking or moving | Since they fainted, is the person still not back to how they were? Or do they find it hard to speak or move? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Could not be woken within 1 minute | When the person fainted, did it take longer than 1 minute to wake them? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Heart racing, slow, skipping or fluttering | Does your heart feel like it is racing, going too slowly, skipping a beat or fluttering? | 80313002 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Seriously hurt when they passed out, fell or had a seizure | Were you seriously hurt when you passed out, fell or had a seizure? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Fainted while exercising | Did you faint while you were exercising or being very active? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Fainted while lying down | Did you faint while you were lying down? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Short of breath | Do you feel short of breath? | 267036007 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Fainted with no warning at all | Did you pass out with no warning at all? For example, no feeling dizzy, hot or sick first. |  | **AI judgement, needs clinical review** | |
| Has a heart condition | Has a doctor told you that you have a heart condition? For example, heart failure, a heart valve problem or a heart rhythm problem. |  | [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/) | |
| Family member died suddenly under 40, or has an inherited heart condition | Has anyone in your family died suddenly when they were under 40? Or been told they have a heart problem that runs in the family? |  | **AI judgement, needs clinical review** | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |
| Fainted more than once recently | Have you fainted more than once recently? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |

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

### `advice_fainting_999`

**What to do:** Call 999 now. Fainting with these signs can be caused by a problem with the heart or brain, and needs checking in hospital straight away.

**Look out for:**
- Not breathing, or not responding
- Chest pain, or a pounding or irregular heartbeat

**Get more help when:**
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.
- Call 999 again if the person gets worse

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- Lay the person on their back and raise their legs, if they are breathing well
- If they are pregnant, lay them on their side instead

Source: [Fainting](https://www.nhs.uk/symptoms/fainting/)

### `advice_headache_999`

**What to do:** Call 999 now. A sudden, extremely painful headache can be a sign of bleeding on the brain. This needs treatment in hospital straight away.

**Look out for:**
- The person becoming drowsy, confused or hard to wake
- A seizure (fit)
- One side of the face drooping, weakness in an arm, or slurred speech

**Get more help when:**
- Call 999 again if the person gets worse before help arrives
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

Source: [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Migraine](https://www.nhs.uk/conditions/migraine/)

### `advice_fainting_ae`

**What to do:** Go to A&E now, or call 999. Fainting with these symptoms needs to be checked in hospital today.

**Look out for:**
- Chest pain, or finding it harder to breathe
- Fainting again

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive yourself. Bring any medicines you take.

Source: [Fainting](https://www.nhs.uk/symptoms/fainting/), [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/)

### `advice_fainting_urgent`

**What to do:** Get help from NHS 111 or ask for an urgent GP appointment today. The cause of your faint should be checked today, in case it is a heart problem.

**Look out for:**
- Fainting again, especially during exercise or while lying down
- Chest pain, or a pounding, fluttering or irregular heartbeat

**Get more help when:**
- Call 999 if you get any of the signs above

**Where to go:** Call 111 or use 111 online, or ask your GP surgery for an urgent appointment. In an emergency call 999.

**What you can do yourself:**
- Do not drive until you have been checked
- If you feel faint, lie down with your legs raised

Source: [Fainting](https://www.nhs.uk/symptoms/fainting/), [Heart palpitations](https://www.nhs.uk/symptoms/heart-palpitations/)

### `advice_low_blood_sugar`

**What to do:** Treat the low blood sugar now. Have something sugary straight away, such as a small glass of fruit juice or a sugary fizzy drink, or glucose tablets. Check your blood sugar again after 10 to 15 minutes.

**Look out for:**
- Blood sugar still below 4 after treating it twice
- Getting confused, very drowsy or hard to wake
- A seizure (fit)

**Get more help when:**
- Once you feel better, eat something like biscuits or a sandwich to keep your sugar up
- Get help from NHS 111 or your diabetes team if it does not get better, or you keep having hypos
- Call 999 if the person stops responding as usual or has a seizure. Do not give them food or drink if they are not fully awake.

**Where to go:** Treat it yourself first. For help call 111 or use 111 online, or contact your diabetes team. In an emergency call 999.

**What you can do yourself:**
- Always carry something sugary with you
- Do not drive for at least 45 minutes after your blood sugar is back to normal

Source: [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/)

### `advice_fainting_gp`

**What to do:** See a GP. Fainting is not usually serious, but it is important to get checked to find out what caused it.

**Look out for:**
- Fainting while exercising or lying down
- Chest pain, or a pounding, fluttering or irregular heartbeat
- Not recovering fully, or difficulty speaking or moving

**Get more help when:**
- Call 999 if you faint again with any of the signs above

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- If you feel faint, lie down with your legs raised. If you cannot, sit with your head between your knees.
- Drink some water. Cross your legs while standing, or clench your fists.
- You must tell the DVLA if you faint regularly and you drive

Source: [Fainting](https://www.nhs.uk/symptoms/fainting/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_fa_chest_pain_or_palpitations`: Source difference: the Heart palpitations page says an urgent GP appointment or 111 for palpitations with fainting that have stopped. The Fainting page says call 999. The more urgent is used.
- `rf_fa_shaking`: A few jerks during a common faint are usual and can look like a seizure. The source still says call 999, so this is kept firm.
- `rf_fa_headache_sudden`: The Subarachnoid haemorrhage page lists fainting as a symptom.
- `rf_fa_short_of_breath`: Clinical knowledge: fainting with breathlessness can be a blood clot in the lung or a heart problem. The breathlessness entry symptom also applies once this is reported.
- `rf_fa_no_warning`: Clinical knowledge: fainting with no warning is more likely to have a heart cause. The Fainting page gives no urgency for this.
- `rf_fa_heart_condition`: Clinical knowledge: fainting in someone with a heart condition needs checking the same day. The Fainting page lists heart problems as a cause.
- `rf_fa_family_sudden_death`: Clinical knowledge: some heart rhythm problems run in families and first show as fainting.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Low blood pressure when standing up (postural hypotension) | 28651003 | common | Dizzy when standing or sitting up quickly: strongly supports; Fainted just after standing up: supports; Feels light-headed: supports; Started a new medicine or changed a dose in the last few weeks: supports; Signs of dehydration: supports |
| Low blood sugar (hypoglycaemia, a hypo) | 302866003 | rare | Has diabetes: strongly supports; Signs of low blood sugar in someone with diabetes: strongly supports; Feels sweaty: supports; Shaking or trembling (tremor): supports; Feels light-headed: supports; Suddenly confused: supports; Tingling or pins and needles in the fingers or around the mouth: supports; Heart racing, slow, skipping or fluttering: supports |
| Bleeding on the brain (subarachnoid haemorrhage) | 21454007 | rare | Headache that came on suddenly and is extremely painful: strongly supports; Headache: strongly supports; Stiff neck: supports; Being sick: supports; Bright lights hurt the eyes or are bothering you: supports; So drowsy they are hard to wake or cannot stay awake: supports; Passed out (fainted): supports; Has had a seizure (fit): supports; Suddenly confused: supports |
| Common faint (vasovagal syncope) | 398665005 | very common | Fainted after standing a long time, heat, a shock, pain or the sight of blood: strongly supports; Felt dizzy, sweaty, hot or sick just before fainting: strongly supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feels light-headed: supports |
| A dangerous heart rhythm (very fast or very slow) or another heart problem that can cause fainting | 698247007 | very rare | Passed out (fainted): strongly supports; Heart beating very slowly: strongly supports; Heart beating very fast: supports; Heart racing, pounding or fluttering right now: supports; Feels light-headed: supports; Chest pain: supports; Short of breath: supports; Heart racing or fluttering comes on during exercise: supports; Has a heart condition: supports; Close relative had a heart attack or angina before 60: supports; Fainted while exercising: strongly supports; Heart racing, slow, skipping or fluttering: strongly supports; Fainted with no warning at all: strongly supports; Fainted while lying down: supports; Family member died suddenly under 40, or has an inherited heart condition: supports |
| Blood clot in the lung (pulmonary embolism) | 59282003 | rare | Short of breath: strongly supports; Breathlessness came on suddenly, or suddenly got much worse: strongly supports; Chest pain worse when breathing in: strongly supports; Breathing very fast: supports; Heart beating very fast: supports; Pain or swelling in one leg: supports; Coughing up blood: supports; Chest pain is there now: strongly supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
