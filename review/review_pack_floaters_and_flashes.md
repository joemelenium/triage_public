# Review pack: Floaters and flashes in the eyes

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
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Migraine](https://www.nhs.uk/conditions/migraine/) | 2026-11-19 |  | Page last reviewed: 10 March 2026 |
| [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | 2026-11-19 |  | Page last reviewed: 20 June 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Detached retina (retinal detachment)](https://www.nhs.uk/conditions/detached-retina-retinal-detachment/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |

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

## Floaters and flashes in the eyes red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ff_sight_lost`<br>Floaters or flashes and cannot see out of 1 or both eyes<br>**Note:** The Vision loss page says go to A&E or call 999 if you suddenly cannot see from 1 or both eyes. | "Cannot see out of 1 or both eyes, or a large part of the sight is missing" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999 now* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_ff_head_injury`<br>Flashes or floaters after a head injury<br>**Note:** The Head injury page says call 999 for problems with vision after hitting your head. | "Head injury in the last month" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_ff_headache`<br>Flashing lights with a severe headache<br>**Note:** The Migraine page says call 999 for a headache that came on suddenly and is extremely painful, or with loss of vision. The Brain aneurysm page says the same. Applying it to flashes with a severe headache is AI reading. Soft, because a usual migraine aura with a headache is common. | "Very painful headache" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Migraine](https://www.nhs.uk/conditions/migraine/) | |

## Floaters and flashes in the eyes red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ff_new_or_sudden`<br>Floaters or flashes for the first time, that started suddenly, or that have suddenly increased<br>**Note:** The Detached retina page says the same. | "Floaters or flashes that are new, sudden, or suddenly more" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent optician appointment, or get help from NHS 111* | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| `rf_ff_curtain`<br>A dark curtain or shadow moving across the sight | "Dark curtain or shadow across the sight" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent optician appointment, or get help from NHS 111* | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| `rf_ff_blurred_or_pain`<br>Floaters or flashes with blurred vision or eye pain | "Blurred, cloudy or misty sight" OR "Eye pain" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent optician appointment, or get help from NHS 111* | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| `rf_ff_after_surgery_or_injury`<br>Floaters that started after eye surgery or an eye injury | "Eye surgery or eye treatment in the last 4 weeks" OR "Injured eye, or something hit the eye" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent optician appointment, or get help from NHS 111* | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |

## Floaters and flashes in the eyes: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ff_zigzag`<br>Zigzag or shimmering lights that spread and go within an hour: possible migraine aura<br>**Note:** Clinical knowledge: these are typical of a migraine aura. A first aura, or a change in a usual one, should be checked by a GP. The Migraine page says urgent if an aura lasts longer than 1 hour. | "Warning signs such as zigzag lines or flashing lights" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. No fixed time is given.* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **Floaters or flashes you have had for a long time, that are not getting worse, with sight not affected: usually harmless**
- Outcome: Self-manageable, Self-care, No appointment needed. *Floaters you have had for a long time are usually harmless*
- Source: [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/)
- **Note:** Only reached when the floaters or flashes are not new, not sudden and not increasing, with no curtain, blurring or pain. The page says these are usually harmless.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Floaters or flashes in the eyes | Are you seeing floaters or flashes? Floaters are small dark dots, lines, rings or cobwebs that drift across your sight. Flashes are sudden flashes of light. |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Floaters or flashes that are new, sudden, or suddenly more | Are the floaters or flashes new, did they start suddenly, or has the number of them suddenly gone up? |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Dark curtain or shadow across the sight | Is there a dark curtain or shadow moving across your sight, or blocking part of it? |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Blurred, cloudy or misty sight | Is your sight blurred, cloudy or misty? | 111516008 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Eye surgery or eye treatment in the last 4 weeks | Have you had eye surgery or eye treatment, such as an injection in the eye, in the last 4 weeks? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Warning signs such as zigzag lines or flashing lights | Before or during it, do you get warning signs that last less than an hour? For example, seeing zigzag lines or flashing lights, or tingling that spreads. |  | [Migraine](https://www.nhs.uk/conditions/migraine/) | |

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

### `advice_eye_emergency`

**What to do:** Go to A&E or call 999 now. Your eye symptoms need to be checked in hospital straight away to protect your sight.

**Look out for:**
- Your sight getting worse
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech
- Pain getting worse, or feeling or being sick

**Get more help when:**
- Call 999 if you get any signs of a stroke, or you cannot get to A&E safely

**Where to go:** Go to A&E. If there is an eye casualty (an emergency eye department) near you, the 111 service or A&E may send you there. Do not drive yourself. Ask someone to drive you or call 999. Bring any medicines you take.

**What you can do yourself:**
- Do not rub your eye
- If you wear contact lenses, take them out and bring them with you

Source: [Red eye](https://www.nhs.uk/symptoms/red-eye/), [Eye pain](https://www.nhs.uk/symptoms/eye-pain/), [Vision loss](https://www.nhs.uk/conditions/vision-loss/), [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/)

### `advice_head_injury_eyes_999`

**What to do:** Call 999 now. Problems with your sight after a head injury need to be checked in hospital straight away.

**Look out for:**
- Being sick, feeling very sleepy, or being hard to wake
- A fit (seizure)
- Clear fluid coming from the ears or nose

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself to A&E. Stay with someone until help arrives.

Source: [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_floaters_urgent`

**What to do:** Get your eyes checked today. Ask an optician for an urgent appointment, or call 111. New or sudden floaters, flashes or a shadow can be a sign of a problem at the back of the eye that needs treating quickly.

**Look out for:**
- A dark curtain or shadow moving across your sight
- Your sight getting blurred, or getting worse
- Many more floaters or flashes

**Get more help when:**
- Go to A&E or call 999 if you suddenly cannot see

**Where to go:** Ask an optician for an urgent appointment today, or call 111 or use 111 online. They may send you to an eye department in hospital. Do not drive until your eyes have been checked.

Source: [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/), [Detached retina (retinal detachment)](https://www.nhs.uk/conditions/detached-retina-retinal-detachment/)

### `advice_migraine_aura_gp`

**What to do:** See a GP. Zigzag or shimmering lights that spread and then go within an hour are often a migraine aura, but a first one should be checked.

**Look out for:**
- Lights or blind spots lasting longer than 1 hour
- Weakness, numbness or problems speaking
- A sudden, very bad headache

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if the lights last longer than 1 hour
- Call 999 if you lose your sight, or get weakness on 1 side, problems speaking or a sudden very bad headache

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

Source: [Migraine](https://www.nhs.uk/conditions/migraine/)

### `advice_floaters_self_care`

**What to do:** Floaters or flashes you have had for a long time, that are not getting worse, are usually harmless. You often get used to them.

**Look out for:**
- New floaters, or a sudden increase in floaters or flashes
- A dark curtain or shadow moving across your sight
- Blurred vision or eye pain

**Get more help when:**
- Ask an optician for an urgent appointment or call 111 if you get any of these
- Go to A&E or call 999 if you suddenly cannot see

**Where to go:** You do not need an appointment now. Keep having regular sight tests with an optician.

Source: [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ff_sight_lost`: The Vision loss page says go to A&E or call 999 if you suddenly cannot see from 1 or both eyes.
- `rf_ff_head_injury`: The Head injury page says call 999 for problems with vision after hitting your head.
- `rf_ff_headache`: The Migraine page says call 999 for a headache that came on suddenly and is extremely painful, or with loss of vision. The Brain aneurysm page says the same. Applying it to flashes with a severe headache is AI reading. Soft, because a usual migraine aura with a headache is common.
- `rf_ff_new_or_sudden`: The Detached retina page says the same.
- `or_ff_zigzag`: Clinical knowledge: these are typical of a migraine aura. A first aura, or a change in a usual one, should be checked by a GP. The Migraine page says urgent if an aura lasts longer than 1 hour.
- `floaters_and_flashes default outcome`: Only reached when the floaters or flashes are not new, not sudden and not increasing, with no curtain, blurring or pain. The page says these are usually harmless.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Eye damage from diabetes (diabetic retinopathy) | 4855003 | rare | Has diabetes: strongly supports; Blurred, cloudy or misty sight: supports; Sight getting worse slowly, over months or years: supports; Harder to see at night or in dim light: supports; Floaters or flashes in the eyes: supports |
| Eye cancer |  | very rare | A dark patch on the eye that is getting bigger: strongly supports; Blurred, cloudy or misty sight: supports; Dark curtain or shadow across the sight: supports; Floaters or flashes in the eyes: supports |
| Long-standing floaters that are harmless | 15013002 | very common | Same floaters for a long time, with no change: strongly supports; Floaters or flashes in the eyes: strongly supports; Short-sighted: supports; Both eyes affected: supports |
| The jelly inside the eye shrinking and pulling away, a common cause of new floaters | 247081001 | common | Floaters or flashes that are new, sudden, or suddenly more: strongly supports; Floaters or flashes in the eyes: strongly supports; Short-sighted: supports; Eye surgery or eye treatment in the last 4 weeks: supports |
| Detached retina (the thin layer at the back of the eye coming loose) | 42059000 | uncommon | Dark curtain or shadow across the sight: strongly supports; Floaters or flashes that are new, sudden, or suddenly more: strongly supports; Floaters or flashes in the eyes: strongly supports; Blurred, cloudy or misty sight: supports; Sight changed suddenly: supports; Short-sighted: supports; Eye surgery or eye treatment in the last 4 weeks: supports; Injured eye, or something hit the eye: supports |
| Iritis or uveitis (swelling inside the eye that makes it red, sore and hurt in bright light) | 128473001 | rare | Bright lights hurt the eyes or are bothering you: strongly supports; Redness worst in a ring around the coloured part of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: strongly supports; Deep, boring ache in the eye: supports; Blurred, cloudy or misty sight: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Floaters or flashes in the eyes: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
