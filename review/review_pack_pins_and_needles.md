# Review pack: Pins and needles

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
| [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | 2026-11-19 |  | Page last reviewed: 17 July 2023 |
| [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | 2026-11-19 |  | Page last reviewed: 12 August 2024 |
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | 2026-11-19 |  | Page last reviewed: 04 January 2024 |
| [Peripheral neuropathy](https://www.nhs.uk/conditions/peripheral-neuropathy/) | 2026-11-19 |  | Page last reviewed: 10 October 2022 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
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

## Pins and needles red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pn_sudden_one_side`<br>Numbness or tingling that came on suddenly on one side of the body: possible stroke<br>**Note:** The Stroke page lists weakness or numbness down one side of the body as a sign of a stroke. | "Numbness or tingling that came on suddenly on one side of the body" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_pn_speech_or_face`<br>Pins and needles with difficulty speaking, or sudden numbness in the face: possible stroke | "Difficulty speaking" OR "Numbness in the face that came on suddenly" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_pn_weakness`<br>Pins and needles or numbness with weakness<br>**Note:** Same as the weakness rule: the Paralysis page says call 999 for weakness with numbness and tingling. Soft because slowly worsening numbness and weakness from nerve damage is common and needs a GP, not an ambulance. The weakness entry symptom also applies once weakness is reported. | "Weakness, or cannot move part of the body (paralysis)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| `rf_pn_legs_bladder_bowel`<br>Numbness or weakness in both legs with problems controlling pee or poo, or numbness around the bottom<br>**Note:** Clinical knowledge: signs of cauda equina syndrome or spinal cord pressure. See the weakness entry symptom. | "Numbness or weakness in both legs" AND ("New problems peeing or pooing" OR "Numb or no feeling around the genitals or bottom") | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_pn_spreading_ae`<br>Tingling or weakness that started in the feet or hands and is spreading up the body: possible Guillain-Barre syndrome<br>**Note:** Same as the weakness rule. The Guillain-Barre syndrome page says an urgent GP appointment or 111. | "Tingling or weakness starting in the feet or hands and spreading over days" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now* | **AI judgement, needs clinical review** | |

## Pins and needles red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_pn_spreading`<br>Tingling or weakness spreading up from the feet or hands | "Tingling or weakness starting in the feet or hands and spreading over days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | |
| `rf_pn_low_sugar`<br>Diabetes and signs of low blood sugar (a hypo), which can cause tingling lips | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Urgent (help today)<br>Urgent care<br>Today<br>*Treat the low blood sugar now. If it does not improve, get help from NHS 111, or call 999 if the person becomes drowsy or confused.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Pins and needles: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_pn_constant`<br>Pins and needles all the time | "Pins and needles all the time" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| `or_pn_keeps_coming_back`<br>Pins and needles that keep coming back | "Pins and needles that keep coming back" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| `or_pn_both_feet_or_hands`<br>Numbness or tingling in both feet or both hands (possible nerve damage) | "Tingling or numbness in both feet or both hands that came on slowly" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Peripheral neuropathy](https://www.nhs.uk/conditions/peripheral-neuropathy/) | |
| `or_pn_different_places`<br>Pins and needles in different parts of the body | "Tingling or numbness in different parts of the body at different times" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |

## Default outcome

Used when no rule fires.

- **Pins and needles with nothing that needs more help: usually from pressure, and goes in a few minutes**
- Outcome: Self-manageable, Self-care, No appointment needed. *Pins and needles usually stop within a few minutes*
- Source: [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Pins and needles, tingling or numbness | Do you have pins and needles, tingling or numbness in part of your body, such as your hands, arms, legs or feet? | 62507009 | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numbness or tingling that came on suddenly on one side of the body | Did the numbness or tingling come on suddenly, on one side of your body? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Numbness in the face that came on suddenly | Did the numbness in your face come on suddenly? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Weakness, or cannot move part of the body (paralysis) | Do you have weakness in your face or body, or are you unable to move part of your body? | 44695005 | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| New problems peeing or pooing | Have you had new problems peeing or pooing? For example, finding it hard to start peeing, not being able to pee, or peeing or pooing yourself. |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Tingling or weakness starting in the feet or hands and spreading over days | Did tingling or weakness start in your feet or hands, and has it spread up your arms or legs over hours or days? |  | [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |
| Pins and needles all the time | Do you have the pins and needles all the time? |  | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| Pins and needles that keep coming back | Do the pins and needles keep coming back? |  | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |
| Tingling or numbness in both feet or both hands that came on slowly | Is the tingling or numbness in both feet or both hands, and has it come on slowly? |  | [Peripheral neuropathy](https://www.nhs.uk/conditions/peripheral-neuropathy/) | |
| Tingling or numbness in different parts of the body at different times | Do you get the tingling or numbness in different parts of your body at different times? |  | [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/) | |

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

### `advice_weakness_999`

**What to do:** Call 999 now. This could be a sign of something serious, such as a stroke or an injury to the spine, that needs treatment in hospital straight away.

**Look out for:**
- Difficulty breathing or swallowing
- Weakness spreading, or getting worse

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. If the person has hurt their neck or back, do not move them unless they are in danger.

Source: [Paralysis](https://www.nhs.uk/symptoms/paralysis/)

### `advice_weakness_ae`

**What to do:** Go to A&E now, or call 999. These symptoms need to be checked in hospital today.

**Look out for:**
- Difficulty breathing or swallowing
- Weakness spreading up your body, or getting worse
- Not being able to pee

**Get more help when:**
- Call 999 if you get any of the signs above or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive yourself. Bring any medicines you take.

Source: **AI judgement, needs clinical review**, [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/), [Paralysis](https://www.nhs.uk/symptoms/paralysis/)

### `advice_weakness_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Weakness or tingling that is spreading needs to be checked today.

**Look out for:**
- Difficulty breathing or swallowing
- A drooping face, or trouble speaking
- Weakness spreading quickly, or not being able to walk

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

Source: [Guillain-Barre syndrome](https://www.nhs.uk/conditions/guillain-barre-syndrome/)

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

### `advice_pins_needles_gp`

**What to do:** See a GP about your pins and needles. They can find out what is causing it.

**Look out for:**
- Numbness or weakness that comes on suddenly, mostly if it is on one side of the body
- Tingling or weakness spreading up your arms or legs
- A cut or sore on your foot that is not healing

**Get more help when:**
- Call 999 if numbness or weakness comes on suddenly, or you have trouble speaking

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- If you have diabetes, check your feet every day for cuts and sores

Source: [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/), [Peripheral neuropathy](https://www.nhs.uk/conditions/peripheral-neuropathy/)

### `advice_pins_needles_self_care`

**What to do:** Pins and needles usually stop within a few minutes, when the weight is taken off that part of your body.

**Look out for:**
- Pins and needles that do not go away, or keep coming back
- Numbness or weakness that comes on suddenly

**Get more help when:**
- See a GP if you constantly have pins and needles or it keeps coming back
- Call 999 if numbness or weakness comes on suddenly, mostly on one side. Or if you find it hard to speak.

**Where to go:** You do not need an appointment now. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Move about and change position to take the pressure off

Source: [Pins and needles](https://www.nhs.uk/symptoms/pins-and-needles/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_pn_sudden_one_side`: The Stroke page lists weakness or numbness down one side of the body as a sign of a stroke.
- `rf_pn_weakness`: Same as the weakness rule: the Paralysis page says call 999 for weakness with numbness and tingling. Soft because slowly worsening numbness and weakness from nerve damage is common and needs a GP, not an ambulance. The weakness entry symptom also applies once weakness is reported.
- `rf_pn_legs_bladder_bowel`: Clinical knowledge: signs of cauda equina syndrome or spinal cord pressure. See the weakness entry symptom.
- `rf_pn_spreading_ae`: Same as the weakness rule. The Guillain-Barre syndrome page says an urgent GP appointment or 111.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Carpal tunnel syndrome (a squashed nerve in the wrist) | 57406009 | uncommon | Pins and needles, tingling or numbness in the arm, hand or fingers: strongly supports; Hand pain or tingling worse at night: strongly supports; Weak arm or hand, or a weak grip: supports; Pain in the wrist: supports; Pain in the palm of the hand: supports; Started after more activity than usual, or doing the same movement many times: supports |
| Sciatica (a trapped nerve causing pain down the leg), often from a slipped disc | 23056005 | common | Pain spreads from the back or bottom down the leg: strongly supports; Numbness, tingling or pins and needles in the leg or foot: strongly supports; Pain worse when coughing, sneezing or pooing: supports; Pain in the lower back: supports; Started after lifting, bending, twisting or an awkward movement: supports; Weakness in one or both legs, or a foot that drags: supports |
| Guillain-Barre syndrome (a rare condition that attacks the nerves) | 40956001 | rare | Tingling or weakness starting in the feet or hands and spreading over days: strongly supports; Tingling or numbness in both feet or both hands that came on slowly: supports; Finding it hard to balance or walk: supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Difficulty breathing: supports; Unable to swallow: supports; Burning, stabbing or shooting pains in the feet or hands: supports |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Multiple sclerosis (MS) warning signs | 24700007 | rare | Tingling or numbness in different parts of the body at different times: strongly supports; Change in sight or loss of vision: supports; Weakness that comes and goes: supports; Feels very tired: supports; Finding it hard to balance or walk: supports; Numbness or tingling in the face: supports |
| Nerve damage in the hands or feet (peripheral neuropathy) | 302226006 | common | Tingling or numbness in both feet or both hands that came on slowly: strongly supports; Burning, stabbing or shooting pains in the feet or hands: strongly supports; Pins and needles all the time: supports; Finding it hard to balance or walk: supports |
| Pins and needles from pressure, such as sitting on a leg |  | very common | Pins and needles after sitting or lying on that part, that goes within minutes: strongly supports; Pins and needles, tingling or numbness in the arm, hand or fingers: supports; Numbness, tingling or pins and needles in the leg or foot: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Mini-stroke (transient ischaemic attack, TIA) | 266257000 | rare | Signs of a stroke: strongly supports; Weakness that comes and goes: strongly supports; Weakness that came on suddenly: supports; Weakness on one side of the face or body: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Difficulty speaking: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Lack of vitamin B12 or folate | 190634004 | uncommon | Feels very tired: strongly supports; Skin paler than usual for weeks or longer: supports; Tingling or numbness in both feet or both hands that came on slowly: supports; Vegan diet without vitamin B12, or a stomach or bowel condition: supports; Pins and needles, tingling or numbness: supports; Problems remembering things: supports |
| Anxiety or panic attack | 48694002 | common | Sudden rush of intense fear or panic: strongly supports; Pain triggered by worry or stress: strongly supports; Tingling or pins and needles in the fingers or around the mouth: supports; Breathing very fast: supports; Heart beating very fast: supports; Heart racing, slow, skipping or fluttering: strongly supports; Feels sweaty: supports; Feels light-headed: supports; Short of breath: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
