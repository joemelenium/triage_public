# Review pack: Numbness of the face

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
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Shingles](https://www.nhs.uk/conditions/shingles/) | 2026-11-18 |  | Page last reviewed: 23 November 2023 |
| [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | 2026-11-19 |  | Page last reviewed: 17 July 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |
| [Transient ischaemic attack (TIA)](https://www.nhs.uk/conditions/transient-ischaemic-attack-tia/) | 2026-11-19 |  | Page last reviewed: 28 June 2023 |
| [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/) | 2026-11-19 |  | Page last reviewed: 04 July 2023 |

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

## Numbness of the face red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fn_stroke_signs`<br>Face numbness with weakness, difficulty speaking, loss of vision, trouble balancing, or numbness down one side: possible stroke<br>**Note:** The Paralysis page also says call 999 for weakness with not being able to feel part of the face. | "Weakness, or cannot move part of the body (paralysis)" OR "Difficulty speaking" OR "Cannot see out of 1 or both eyes, or a large part of the sight is missing" OR "Finding it hard to balance or walk" OR "Numbness or tingling that came on suddenly on one side of the body" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_fn_headache_sudden`<br>Face numbness with a headache that came on suddenly and is extremely painful | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_fn_sudden_ae`<br>Numbness in the face that came on suddenly<br>**Note:** Clinical knowledge: sudden numbness in the face alone can be a stroke or mini-stroke. It can also come with a migraine or a panic attack, so this is soft, with the urgent rule below as its floor. | "Numbness in the face that came on suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Numbness of the face red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_fn_sudden`<br>Numbness in the face that came on suddenly<br>**Note:** AI judgement: the floor under the soft emergency rule above. | "Numbness in the face that came on suddenly" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 today* | **AI judgement, needs clinical review** | |
| `rf_fn_shingles_eye`<br>A shingles rash on or near the eye or nose, or changes to vision | "Tingling, pain or a rash of blisters on one side of the body" AND "Shingles rash on or near the eye or nose, or changes to vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Shingles](https://www.nhs.uk/conditions/shingles/) | |

## Numbness of the face: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Numbness of the face with nothing that needs more urgent help: see a GP to find the cause**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: **AI judgement, needs clinical review**
- **Note:** AI judgement: numbness in the face that has not gone away should be checked by a GP. The Paralysis page lists a face that is numb or tingles all the time as a sign of paralysis.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Numbness or tingling in the face | Is part of your face numb or tingling, or does it have less feeling than usual? | 309557009 | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Weakness, or cannot move part of the body (paralysis) | Do you have weakness in your face or body, or are you unable to move part of your body? | 44695005 | [Paralysis](https://www.nhs.uk/symptoms/paralysis/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Finding it hard to balance or walk | Are you finding it hard to balance or walk, or are you falling over? | 22631008 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Numbness or tingling that came on suddenly on one side of the body | Did the numbness or tingling come on suddenly, on one side of your body? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Numbness in the face that came on suddenly | Did the numbness in your face come on suddenly? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Tingling, pain or a rash of blisters on one side of the body | Do you have a tingling or painful patch of skin, or a rash of blisters, on one side of your body only? |  | [Shingles](https://www.nhs.uk/conditions/shingles/) | |
| Shingles rash on or near the eye or nose, or changes to vision | Is the rash or painful patch on or near your eye or nose? Or have you noticed any changes to your vision? |  | [Shingles](https://www.nhs.uk/conditions/shingles/) | |

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

### `advice_face_numbness_ae`

**What to do:** Go to A&E now, or call 999. Numbness in the face that comes on suddenly can be a sign of a stroke or mini-stroke.

**Look out for:**
- One side of the face drooping, weakness in an arm, or slurred speech
- Loss of sight, or trouble balancing

**Get more help when:**
- Call 999 straight away if you get any of the signs above, even if they go away

**Where to go:** Go to A&E or call 999. Do not drive yourself to A&E.

Source: **AI judgement, needs clinical review**, [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/), [Transient ischaemic attack (TIA)](https://www.nhs.uk/conditions/transient-ischaemic-attack-tia/)

### `advice_face_numbness_urgent`

**What to do:** Get help from NHS 111 today. Numbness in the face that came on suddenly should be checked today.

**Look out for:**
- One side of the face drooping, weakness in an arm, or slurred speech
- Loss of sight, or trouble balancing

**Get more help when:**
- Call 999 straight away if you get any of the signs above

**Where to go:** Call 111 or use 111 online. In an emergency call 999.

Source: **AI judgement, needs clinical review**, [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/)

### `advice_shingles_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Shingles near the eye or nose, or with changes to your vision, needs checking quickly to protect your sight.

**Look out for:**
- Your eye becoming more red or painful
- Your vision getting worse
- The rash spreading, or you feeling very unwell

**Get more help when:**
- Medicine for shingles works best if you start it within 3 days of the rash appearing
- Call 999 if you get sudden chest pain. Call 999 if pain spreads to your arm, neck, jaw or back.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Take paracetamol to help with the pain
- Keep the rash clean and dry, and wear loose clothing
- Do not share towels. Keep away from babies and people who are pregnant until the blisters dry.

Source: [Shingles](https://www.nhs.uk/conditions/shingles/)

### `advice_face_numbness_gp`

**What to do:** See a GP about the numbness in your face. They can find out what is causing it.

**Look out for:**
- One side of the face drooping, weakness in an arm, or slurred speech
- A rash of blisters on your face
- The numbness spreading, or getting worse

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your face becomes weak, or you get a rash near your eye
- Call 999 if you get any signs of a stroke

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

Source: **AI judgement, needs clinical review**, [Paralysis](https://www.nhs.uk/symptoms/paralysis/), [Bell's palsy](https://www.nhs.uk/conditions/bells-palsy/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_fn_stroke_signs`: The Paralysis page also says call 999 for weakness with not being able to feel part of the face.
- `rf_fn_sudden_ae`: Clinical knowledge: sudden numbness in the face alone can be a stroke or mini-stroke. It can also come with a migraine or a panic attack, so this is soft, with the urgent rule below as its floor.
- `rf_fn_sudden`: AI judgement: the floor under the soft emergency rule above.
- `face_numbness default outcome`: AI judgement: numbness in the face that has not gone away should be checked by a GP. The Paralysis page lists a face that is numb or tingles all the time as a sign of paralysis.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bell's palsy (weakness on one side of the face) | 193093009 | uncommon | One side of the face weak or drooping: strongly supports; Pain behind the ear, or a change in taste, with face weakness: strongly supports; Signs of a stroke: supports; Weakness on one side of the face or body: supports; Numbness or tingling in the face: supports |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Multiple sclerosis (MS) warning signs | 24700007 | rare | Tingling or numbness in different parts of the body at different times: strongly supports; Change in sight or loss of vision: supports; Weakness that comes and goes: supports; Feels very tired: supports; Finding it hard to balance or walk: supports; Numbness or tingling in the face: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Mini-stroke (transient ischaemic attack, TIA) | 266257000 | rare | Signs of a stroke: strongly supports; Weakness that comes and goes: strongly supports; Weakness that came on suddenly: supports; Weakness on one side of the face or body: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Difficulty speaking: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Shingles (an infection that causes a painful rash on one side of the body) | 4740000 | rare | Tingling, pain or a rash of blisters on one side of the body: strongly supports; Chest pain is there now: supports; Chest pain is sharp or stabbing: supports; Pain in the upper back: supports; Blisters or fluid-filled spots: supports; Shingles rash on or near the eye or nose, or changes to vision: supports; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
