# Review pack: Double vision

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
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | 2026-11-19 |  | Page last reviewed: 18 August 2023 |
| [Myasthenia gravis](https://www.nhs.uk/conditions/myasthenia-gravis/) | 2026-11-19 |  | Page last reviewed: 13 September 2023 |
| [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | 2026-11-19 |  | Page last reviewed: 26 June 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | 2026-11-19 |  | Page last reviewed: 17 November 2023 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | 2026-11-19 |  | Page last reviewed: 21 April 2023 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/) | 2026-11-19 |  | Page last reviewed: 14 August 2023 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |

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

## Double vision red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dv_headache_or_pupil`<br>Double vision with a severe headache, or an enlarged pupil | "Very painful headache" OR "1 pupil bigger than the other" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_dv_head_injury`<br>Double vision after a head injury<br>**Note:** The Head injury page says call 999 for problems with vision after a head injury. | "Head injury in the last month" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_dv_eye_injury`<br>Double vision after an injury to the eye<br>**Note:** The Eye injuries page says go to A&E or call 999 for any changes to your sight after an eye injury. | "Injured eye, or something hit the eye" OR "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_dv_eyelid_dropped`<br>Double vision with an eyelid that has suddenly started drooping<br>**Note:** The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time. Clinical knowledge: with double vision this can be a nerve to the eye being pressed on, for example by a brain aneurysm. Soft, because myasthenia gravis also causes this and is less urgent. | "Eyelid started drooping suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |
| `rf_dv_speech_swallow_breathing`<br>Double vision with difficulty speaking, swallowing or breathing<br>**Note:** The Myasthenia gravis page says severe breathing or swallowing difficulties may need urgent hospital treatment. Slurred speech is also a stroke sign (Stroke symptoms page). Combining them is AI judgement. | "Difficulty speaking" OR "Unable to swallow" OR "Difficulty breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Myasthenia gravis](https://www.nhs.uk/conditions/myasthenia-gravis/) | |
| `rf_dv_sudden_unsteady`<br>Double vision that started suddenly, with dizziness or being unsteady: possible stroke<br>**Note:** Clinical knowledge: sudden double vision with dizziness or unsteadiness can be a stroke at the back of the brain, which the face, arm and speech signs miss. | "Double vision started suddenly" AND "Dizzy or off-balance" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |
| `rf_dv_gca`<br>Double vision with pain at the temples or scalp, or jaw pain when eating: possible giant cell arteritis<br>**Note:** Source difference: the Cluster headaches page says an urgent GP appointment or 111 for a severe headache with jaw pain and double vision (signs of temporal arteritis). Clinical knowledge: sight symptoms in giant cell arteritis need same-day hospital care. Soft, with the firm urgent rule below as its floor. | "Jaw pain when eating, or a sore or tender scalp or temple" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_dv_bulging_infection`<br>Double vision with a swollen eyelid or a bulging eye that has just started: possible infection or swelling behind the eye<br>**Note:** The Bulging eyes page says call 999 or go to A&E if the eyes have started bulging with vision changes. The swollen eyelid part is AI judgement from the Cellulitis page. | ("Swollen eyelid" AND ("Hard or painful to move the eye" OR "Very high temperature, or feels hot, cold or shivery")) OR "Bulging has just started" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |

## Double vision red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_dv_sudden`<br>Double vision that started suddenly | "Double vision started suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_dv_eye_pain`<br>Eye pain and double vision | "Eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_dv_gca_urgent`<br>Double vision with pain at the temples or jaw pain when eating | "Jaw pain when eating, or a sore or tender scalp or temple" | Urgent (help today)<br>Urgent care<br>Today<br>*Get an urgent GP appointment or call 111* | [Cluster headaches](https://www.nhs.uk/conditions/cluster-headaches/) | |

## Double vision: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Double vision with nothing that needs more urgent help: get it checked, even if it comes and goes**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *Go to an optician or see a GP. No fixed time is given.*
- Source: [Double vision](https://www.nhs.uk/symptoms/double-vision/)
- **Note:** An optician has no level of its own in settings.yaml, so general practice (routine) is used, and the advice names the optician.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| 1 pupil bigger than the other | Is 1 pupil (the black circle in the middle of the eye) bigger than the other? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Chemical or other harmful liquid in the eye | Has a chemical or other harmful liquid got in your eye? For example, bleach, oven cleaner, cement or plaster. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Eyelid started drooping suddenly | Did the eyelid start drooping suddenly, in the last few days? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Double vision started suddenly | Did the double vision start suddenly? |  | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Dizzy or off-balance | Do you feel dizzy or off-balance, or like you or the room is spinning? | 404640003 | [Dizziness](https://www.nhs.uk/symptoms/dizziness/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Swollen eyelid | Is your eyelid swollen? |  | [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/) | |
| Hard or painful to move the eye | Is it hard to move your eye, or does it not move as far as the other eye? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Bulging has just started | Has the bulging just started, in the last few days? |  | [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |

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

### `advice_double_vision_ae`

**What to do:** Call 999 or go to A&E now. Double vision with these symptoms can be a sign of a serious problem in the brain or nerves.

**Look out for:**
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech
- Difficulty breathing or swallowing
- Feeling very sleepy or confused

**Get more help when:**
- Call 999 straight away if you get any signs of a stroke or find it hard to breathe

**Where to go:** Call 999 or go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: [Double vision](https://www.nhs.uk/symptoms/double-vision/), [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/), [Myasthenia gravis](https://www.nhs.uk/conditions/myasthenia-gravis/)

### `advice_eye_injury_ae`

**What to do:** Go to A&E now, or call 999. An injury like this needs to be checked in hospital to protect your sight.

**Look out for:**
- Changes to your sight
- Blood or pus coming from your eye
- Feeling or being sick

**Get more help when:**
- Call 999 if you cannot get to A&E safely, or if there is heavy bleeding

**Where to go:** Go to A&E. Some areas have an eye casualty (an emergency eye department) you may be sent to. Do not drive yourself. Ask someone to drive you or call 999.

**What you can do yourself:**
- Do not try to remove anything that has pierced your eye or is stuck in it
- Do not rub or press on your eye
- If you can, cover the eye loosely with something clean, such as a paper cup taped in place
- Do not wear contact lenses

Source: [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/), [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/)

### `advice_gca_emergency`

**What to do:** Go to A&E now, or call 999. Pain at the side of the head or in the jaw with changes to your sight can be giant cell arteritis (swollen blood vessels in the head). It needs treatment today to protect your sight.

**Look out for:**
- Losing sight in 1 or both eyes, even for a short time
- Double vision
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Call 999 if you lose your sight or get any signs of a stroke

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/)

### `advice_eye_infection_spreading`

**What to do:** Go to A&E now, or call 999. Your answers suggest an infection that may be spreading behind the eye. This is very serious and needs treatment in hospital.

**Look out for:**
- Your eye bulging or becoming harder to move
- Changes to your sight
- Feeling very unwell, confused, dizzy or faint
- Cold, clammy or pale skin

**Get more help when:**
- Call 999 if you get worse quickly or cannot get to A&E safely

**Where to go:** Go to A&E. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/), [Bulging eyes (exophthalmos)](https://www.nhs.uk/symptoms/bulging-eyes/), [Eyelid problems](https://www.nhs.uk/symptoms/eyelid-problems/)

### `advice_double_vision_urgent`

**What to do:** Ask for an urgent GP appointment or call 111 today. Double vision that starts suddenly, or comes with eye pain, needs to be checked quickly.

**Look out for:**
- A severe headache
- 1 pupil (the black circle in the middle of the eye) getting bigger than the other
- A drooping eyelid
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Call 999 or go to A&E if you get a severe headache or signs of a stroke. Also if 1 pupil (the black circle in the middle of the eye) gets bigger.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Do not drive while you have double vision.

Source: [Double vision](https://www.nhs.uk/symptoms/double-vision/)

### `advice_gca_urgent`

**What to do:** Ask for an urgent GP appointment or call 111 today. Pain at the side of the head or scalp, or jaw pain when eating, can be giant cell arteritis (swollen blood vessels in the head). It needs treatment quickly.

**Look out for:**
- Any change to your sight, such as blurring, double vision or losing sight in 1 eye
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Go to A&E or call 999 if your sight changes, even for a short time

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

Source: [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/)

### `advice_double_vision_gp`

**What to do:** Go to an optician or see a GP to get your double vision checked, even if it comes and goes.

**Look out for:**
- Double vision that gets worse or starts suddenly
- Eye pain
- A severe headache, or 1 pupil (the black circle in the middle of the eye) bigger than the other

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if the double vision gets worse or you get eye pain
- Call 999 or go to A&E if you get a severe headache or signs of a stroke

**Where to go:** Book a sight test with an optician, or make an appointment with a GP. You must stop driving and tell the DVLA if you are told you have double vision.

**What you can do yourself:**
- Try covering 1 eye at a time to see if the double vision goes away. Tell the optician or GP what you find.

Source: [Double vision](https://www.nhs.uk/symptoms/double-vision/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_dv_head_injury`: The Head injury page says call 999 for problems with vision after a head injury.
- `rf_dv_eye_injury`: The Eye injuries page says go to A&E or call 999 for any changes to your sight after an eye injury.
- `rf_dv_eyelid_dropped`: The Cluster headaches page says call 999 or go to A&E for an eyelid drooping for the first time. Clinical knowledge: with double vision this can be a nerve to the eye being pressed on, for example by a brain aneurysm. Soft, because myasthenia gravis also causes this and is less urgent.
- `rf_dv_speech_swallow_breathing`: The Myasthenia gravis page says severe breathing or swallowing difficulties may need urgent hospital treatment. Slurred speech is also a stroke sign (Stroke symptoms page). Combining them is AI judgement.
- `rf_dv_sudden_unsteady`: Clinical knowledge: sudden double vision with dizziness or unsteadiness can be a stroke at the back of the brain, which the face, arm and speech signs miss.
- `rf_dv_gca`: Source difference: the Cluster headaches page says an urgent GP appointment or 111 for a severe headache with jaw pain and double vision (signs of temporal arteritis). Clinical knowledge: sight symptoms in giant cell arteritis need same-day hospital care. Soft, with the firm urgent rule below as its floor.
- `rf_dv_bulging_infection`: The Bulging eyes page says call 999 or go to A&E if the eyes have started bulging with vision changes. The swollen eyelid part is AI judgement from the Cellulitis page.
- `double_vision default outcome`: An optician has no level of its own in settings.yaml, so general practice (routine) is used, and the advice names the optician.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Swollen blood vessels in the head (temporal arteritis) | 414341000 | rare | Jaw pain when eating, or a sore or tender scalp or temple: strongly supports; Change in sight or loss of vision: supports; Headache feels different from usual headaches: supports; Feels very tired: supports; Aching body: supports; Losing weight without trying: supports; Headache: strongly supports; Double vision: supports; Feels very unwell: supports; Pain and stiffness in both shoulders or both hips, worst in the morning: supports; Lost the sight in 1 eye for a short time, then it came back: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Serious injury from a blow to the eye (bleeding inside the eye or a broken eye socket) |  | very rare | Hit in the eye by something blunt: strongly supports; Injured eye, or something hit the eye: strongly supports; Double vision: supports; Hard or painful to move the eye: supports; Severe eye pain: supports; Feels sick or has been sick: supports; Change in sight or loss of vision: supports |
| A swelling in a blood vessel in the brain (brain aneurysm) pressing on a nerve to the eye | 783421002 | very rare | 1 pupil bigger than the other: strongly supports; Eyelid started drooping suddenly: strongly supports; Double vision started suddenly: strongly supports; Eye pain: supports; Headache: supports; Very painful headache: supports |
| Cataracts (the lens inside the eye becomes cloudy) | 193570009 | uncommon | Sight getting worse slowly, over months or years: strongly supports; Blurred, cloudy or misty sight: strongly supports; Glowing rings (halos) around lights: supports; Harder to see at night or in dim light: supports; Colours look faded or washed out: supports; Double vision stays when 1 eye is covered: supports; Has diabetes: supports; Smokes, or has smoked in the past: supports |
| Dry eye (the eyes do not make enough tears, or the tears dry up too quickly) | 46152009 | uncommon | Dry eyes: strongly supports; Gritty, scratchy or burning feeling in the eye: strongly supports; Both eyes affected: supports; Wears contact lenses: supports; Long time at screens, or in dry, air-conditioned or heated rooms: supports; Itchy eyes: supports; Watering eyes: supports; Itchy, sore or crusty eyelid edges: supports; Double vision stays when 1 eye is covered: supports |
| A weak nerve to the eye muscles, often linked to diabetes or high blood pressure |  | rare | Double vision started suddenly: strongly supports; Double vision goes when either eye is covered: strongly supports; Eye pain: supports; Upper eyelid droops: supports; Has diabetes: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports |
| Myasthenia gravis (muscles that get weak and tired, often in the eyelids and eyes first) | 91637004 | rare | Drooping eyelid or double vision worse when tired: strongly supports; Upper eyelid droops: strongly supports; Difficulty speaking: supports; Double vision: supports; Double vision goes when either eye is covered: supports |
| Needing glasses or a new prescription (short sight, long sight or astigmatism) | 39021009 | common | Hard to see far away or close up, clear at other distances: strongly supports; Sight getting worse slowly, over months or years: strongly supports; Headache: supports; Double vision stays when 1 eye is covered: supports; 1 eye turns in, out, up or down: supports |
| Infection behind the eye (orbital cellulitis) | 194005002 | very rare | Swollen eyelid that is red, hot, painful, tender or blistered: strongly supports; Hard or painful to move the eye: strongly supports; Swollen eyelid: strongly supports; Bulging eyes: supports; Eye hurts more when moving it: supports; Very high temperature, or feels hot, cold or shivery: supports; Change in sight or loss of vision: supports; Pain or tenderness around the cheeks, eyes or forehead: supports; Feels very unwell: supports |
| Squint (the eyes point in different directions) | 22066006 | rare | 1 eye turns in, out, up or down: strongly supports; Double vision goes when either eye is covered: supports; Double vision: supports; Hard to see far away or close up, clear at other distances: supports |
| Stroke or mini-stroke (TIA) affecting the sight |  | very rare | Suddenly lost the same side of the sight in both eyes: strongly supports; Lost the sight in 1 eye for a short time, then it came back: strongly supports; Sight changed suddenly: strongly supports; Difficulty speaking: supports; Dizzy or off-balance: supports; Double vision started suddenly: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports |
| Thyroid eye problems (swelling behind the eyes linked to a thyroid condition) | 276177000 | rare | Has a thyroid problem, such as an overactive thyroid: strongly supports; Bulging eyes: strongly supports; Both eyes affected: supports; Hard to close the eye fully: supports; Gritty, scratchy or burning feeling in the eye: supports; Double vision: supports; Swollen eyelid: supports; Smokes, or has smoked in the past: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
