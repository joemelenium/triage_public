# Review pack: Vision loss or a change in sight

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
| [Transient ischaemic attack (TIA)](https://www.nhs.uk/conditions/transient-ischaemic-attack-tia/) | 2026-11-19 |  | Page last reviewed: 28 June 2023 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Double vision](https://www.nhs.uk/symptoms/double-vision/) | 2026-11-19 |  | Page last reviewed: 12 January 2024 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | 2026-11-19 |  | Page last reviewed: 12 March 2026 |
| [Detached retina (retinal detachment)](https://www.nhs.uk/conditions/detached-retina-retinal-detachment/) | 2026-11-19 |  | Page last reviewed: 04 August 2023 |
| [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | 2026-11-19 |  | Page last reviewed: 21 October 2025 |
| [Diabetic retinopathy](https://www.nhs.uk/conditions/diabetic-retinopathy/) | 2026-11-19 |  | Page last reviewed: 17 July 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Red eye](https://www.nhs.uk/symptoms/red-eye/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Uveitis](https://www.nhs.uk/conditions/uveitis/) | 2026-11-19 |  | Page last reviewed: 20 March 2024 |
| [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | 2026-11-19 |  | Page last reviewed: 20 June 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Age-related macular degeneration (AMD)](https://www.nhs.uk/conditions/age-related-macular-degeneration-amd/) | 2026-11-19 |  | Page last reviewed: 22 January 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Dry eyes](https://www.nhs.uk/symptoms/dry-eyes/) | 2026-11-19 |  | Page last reviewed: 06 January 2025 |
| [Giant cell arteritis](https://www.nhs.uk/conditions/temporal-arteritis/) | 2026-11-19 |  | Page last reviewed: 14 August 2023 |
| [Cataracts](https://www.nhs.uk/conditions/cataracts/) | 2026-11-19 |  | Page last reviewed: 12 March 2025 |

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

## Vision loss or a change in sight red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_vl_half_vision`<br>Suddenly lost the same side of the sight in both eyes: possible stroke<br>**Note:** The Stroke symptoms page lists sudden loss of sight as a stroke sign. Losing the same half in both eyes is the typical pattern of a stroke (AI judgement). | "Suddenly lost the same side of the sight in both eyes" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 now* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_vl_brief_loss`<br>Lost the sight in 1 eye for a short time, then it came back: possible mini-stroke (TIA)<br>**Note:** The TIA page says call 999 for stroke signs even if they go away, and the Stroke symptoms page lists loss of sight. Applying this to sight loss in 1 eye that came back is AI reading. Soft, because a migraine aura can look like this; giant cell arteritis and stroke cards keep it at emergency if they are likely. | "Lost the sight in 1 eye for a short time, then it came back" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999, even if your sight has come back* | [Transient ischaemic attack (TIA)](https://www.nhs.uk/conditions/transient-ischaemic-attack-tia/) | |
| `rf_vl_sudden_loss`<br>Suddenly cannot see out of 1 or both eyes | "Cannot see out of 1 or both eyes, or a large part of the sight is missing" AND "Sight changed suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999 now* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_sudden_severe_pain`<br>Sudden severe eye pain | "Eye pain or other eye symptoms started suddenly" AND "Severe eye pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999 now* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_headache_or_pupil`<br>Blurred or double vision with a severe headache, or with 1 pupil bigger than the other<br>**Note:** The Migraine page says call 999 if you lose your vision or have blurred or double vision with a headache attack. The Brain aneurysm page says call 999 for a sudden extremely painful headache with blurred vision. | "Very painful headache" OR "1 pupil bigger than the other" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| `rf_vl_head_injury`<br>Problems with the sight after a head injury | "Head injury in the last month" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_vl_eye_injury`<br>Any change to the sight after an eye injury | "Injured eye, or something hit the eye" OR "Chemical or other harmful liquid in the eye" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| `rf_vl_after_surgery`<br>Changes to the sight after eye surgery or treatment in the last 4 weeks<br>**Note:** The Detached retina page says go to A&E if blurriness gets worse after surgery. The Eye pain page says call 999 or go to A&E for loss of vision after eye surgery or treatment in the last 4 weeks. | "Eye surgery or eye treatment in the last 4 weeks" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E, or call the eye unit that treated you* | [Detached retina (retinal detachment)](https://www.nhs.uk/conditions/detached-retina-retinal-detachment/) | |
| `rf_vl_lenses_and_pain`<br>Wears contact lenses, with eye pain and vision loss | "Wears contact lenses" AND "Eye pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go straight to A&E. Take your lenses out.* | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| `rf_vl_gca`<br>Changes to the sight with pain at the temples or scalp, or jaw pain when eating: possible giant cell arteritis<br>**Note:** Clinical knowledge: giant cell arteritis with sight symptoms can cause permanent blindness within hours. The Giant cell arteritis page says an urgent GP appointment, and a same-day appointment with an eye specialist at a hospital if there are vision problems. Treated as emergency; firm, because missing it can mean blindness in both eyes. | "Jaw pain when eating, or a sore or tender scalp or temple" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Vision loss or a change in sight red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_vl_sudden_or_days`<br>Sight that changed suddenly, or got worse over a few days<br>**Note:** The page says urgent for changes such as blurred vision. Applying it to new changes, and 'see an optician' to slow changes, is a reading of the page. The Diabetic retinopathy page says urgent if your eyesight suddenly gets worse. | "Sight changed suddenly" OR "Sight got worse over a few days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111. An optician may also be able to see you today.* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_curtain_or_flashes`<br>A dark shadow moving across the sight, or seeing flashing lights or shapes | "Dark curtain or shadow across the sight" OR "Floaters or flashes in the eyes" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or optician appointment, or get help from NHS 111* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_pain_or_light`<br>Changes in sight with pain in 1 or both eyes, or eyes painful in bright light | "Eye pain" OR "Bright lights hurt the eyes or are bothering you" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_double`<br>Double vision with other changes in sight<br>**Note:** Source difference: the Vision loss page lists double vision as urgent. The Double vision page says see an optician or GP unless it started suddenly or comes with eye pain. Soft; the double vision entry symptom's own rules also apply. | "Double vision" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| `rf_vl_diabetes_blurred`<br>Diabetes and blurred vision | "Has diabetes" AND "Blurred, cloudy or misty sight" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Diabetic retinopathy](https://www.nhs.uk/conditions/diabetic-retinopathy/) | |

## Vision loss or a change in sight: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_vl_distorted`<br>The middle of the sight is distorted, so straight lines look wavy: possible macular degeneration<br>**Note:** Clinical knowledge: new distortion can be the 'wet' type of macular degeneration, which is treated with injections and should be seen within days. The AMD page says vision can get worse quickly over weeks. An optician has no level of its own, so general practice is used. | "Middle of the sight distorted, straight lines look wavy" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See an optician within a few days* | **AI judgement, needs clinical review** | |
| `or_vl_diabetes`<br>Diabetes and eyesight getting worse over time, or harder to see in low light | "Has diabetes" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*Contact a GP, your diabetes care team or an optician* | [Diabetic retinopathy](https://www.nhs.uk/conditions/diabetic-retinopathy/) | |

## Default outcome

Used when no rule fires.

- **A change in sight with nothing that needs more urgent help: get your sight checked**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See an optician for a sight test. No fixed time is given.*
- Source: [Vision loss](https://www.nhs.uk/conditions/vision-loss/)
- **Note:** The page says see an optician if you think you may have vision loss. An optician has no level of its own in settings.yaml, so general practice (routine) is used, and the advice names the optician.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Suddenly lost the same side of the sight in both eyes | Have you suddenly lost the same side (left or right) of what you see, in both eyes? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Lost the sight in 1 eye for a short time, then it came back | Did you lose the sight in 1 eye for a few seconds or minutes, like a curtain coming down, and then it came back? |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Cannot see out of 1 or both eyes, or a large part of the sight is missing | Have you lost the sight in 1 or both eyes, or in a large part of what you see? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Sight changed suddenly | Did the change in your sight come on suddenly, over seconds, minutes or hours? |  | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Eye pain or other eye symptoms started suddenly | Did the pain or other eye symptoms start suddenly, over minutes or a few hours? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Severe eye pain | Is the pain in your eye severe? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| 1 pupil bigger than the other | Is 1 pupil (the black circle in the middle of the eye) bigger than the other? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Head injury in the last month | Have you hit your head, or had an injury to your head, in the last month? | 82271004 | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| Injured eye, or something hit the eye | Have you injured your eye, or has something hit it? |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Chemical or other harmful liquid in the eye | Has a chemical or other harmful liquid got in your eye? For example, bleach, oven cleaner, cement or plaster. |  | [Eye injuries](https://www.nhs.uk/conditions/eye-injuries/) | |
| Eye surgery or eye treatment in the last 4 weeks | Have you had eye surgery or eye treatment, such as an injection in the eye, in the last 4 weeks? |  | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Wears contact lenses | Do you wear contact lenses? |  | [Red eye](https://www.nhs.uk/symptoms/red-eye/) | |
| Eye pain | Do you have pain in or around your eye? It may be felt behind, inside or around the eye. | 41652007 | [Eye pain](https://www.nhs.uk/symptoms/eye-pain/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Sight got worse over a few days | Has your sight got worse over a few days? |  | [Uveitis](https://www.nhs.uk/conditions/uveitis/) | |
| Dark curtain or shadow across the sight | Is there a dark curtain or shadow moving across your sight, or blocking part of it? |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Floaters or flashes in the eyes | Are you seeing floaters or flashes? Floaters are small dark dots, lines, rings or cobwebs that drift across your sight. Flashes are sudden flashes of light. |  | [Eye floaters and flashes](https://www.nhs.uk/symptoms/floaters-and-flashes-in-the-eyes/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Double vision | Do you see 2 of things when you look at 1 object (double vision), even if it comes and goes? | 24982008 | [Double vision](https://www.nhs.uk/symptoms/double-vision/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Blurred, cloudy or misty sight | Is your sight blurred, cloudy or misty? | 111516008 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Middle of the sight distorted, straight lines look wavy | Is the middle of your sight blurred or distorted, so straight lines look wavy or bent? |  | [Age-related macular degeneration (AMD)](https://www.nhs.uk/conditions/age-related-macular-degeneration-amd/) | |

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

### `advice_vision_urgent`

**What to do:** Get your sight checked today. Ask your GP surgery for an urgent appointment or call 111. Many opticians can also see you the same day.

**Look out for:**
- Suddenly not being able to see out of 1 or both eyes
- Sudden severe eye pain
- Signs of a stroke, such as a face drooping on one side, weak arms or slurred speech

**Get more help when:**
- Go to A&E or call 999 if you suddenly cannot see, or get sudden severe eye pain
- Call 999 if you get any signs of a stroke

**Where to go:** Ask your GP surgery for an urgent appointment, call 111 or use 111 online, or ask an optician if they can see you today. Do not drive until your sight has been checked.

Source: [Vision loss](https://www.nhs.uk/conditions/vision-loss/)

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

### `advice_vision_soon`

**What to do:** Get your sight checked by an optician in the next few days. Wavy or bent lines in the middle of your sight can be a sign of macular degeneration, which may need treatment soon.

**Look out for:**
- Your sight getting worse quickly
- A dark patch or blank spot in the middle of your sight

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your sight gets worse quickly
- Go to A&E or call 999 if you suddenly cannot see

**Where to go:** Book an appointment with an optician for the next few days, or see a GP. For urgent help call 111 or use 111 online.

Source: **AI judgement, needs clinical review**, [Age-related macular degeneration (AMD)](https://www.nhs.uk/conditions/age-related-macular-degeneration-amd/), [Vision loss](https://www.nhs.uk/conditions/vision-loss/)

### `advice_vision_optician`

**What to do:** Get your sight checked by an optician. Finding a cause early may help stop your sight getting worse.

**Look out for:**
- Your sight getting worse quickly
- A dark shadow moving across your sight
- Flashing lights or new floaters
- Pain in 1 or both eyes

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your sight changes quickly, or you get eye pain or flashing lights
- Go to A&E or call 999 if you suddenly cannot see

**Where to go:** Book a sight test with an optician. Some people can get free NHS sight tests. If you have diabetes, you can also contact your GP or diabetes care team.

Source: [Vision loss](https://www.nhs.uk/conditions/vision-loss/), [Diabetic retinopathy](https://www.nhs.uk/conditions/diabetic-retinopathy/), [Cataracts](https://www.nhs.uk/conditions/cataracts/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_vl_half_vision`: The Stroke symptoms page lists sudden loss of sight as a stroke sign. Losing the same half in both eyes is the typical pattern of a stroke (AI judgement).
- `rf_vl_brief_loss`: The TIA page says call 999 for stroke signs even if they go away, and the Stroke symptoms page lists loss of sight. Applying this to sight loss in 1 eye that came back is AI reading. Soft, because a migraine aura can look like this; giant cell arteritis and stroke cards keep it at emergency if they are likely.
- `rf_vl_headache_or_pupil`: The Migraine page says call 999 if you lose your vision or have blurred or double vision with a headache attack. The Brain aneurysm page says call 999 for a sudden extremely painful headache with blurred vision.
- `rf_vl_after_surgery`: The Detached retina page says go to A&E if blurriness gets worse after surgery. The Eye pain page says call 999 or go to A&E for loss of vision after eye surgery or treatment in the last 4 weeks.
- `rf_vl_gca`: Clinical knowledge: giant cell arteritis with sight symptoms can cause permanent blindness within hours. The Giant cell arteritis page says an urgent GP appointment, and a same-day appointment with an eye specialist at a hospital if there are vision problems. Treated as emergency; firm, because missing it can mean blindness in both eyes.
- `rf_vl_sudden_or_days`: The page says urgent for changes such as blurred vision. Applying it to new changes, and 'see an optician' to slow changes, is a reading of the page. The Diabetic retinopathy page says urgent if your eyesight suddenly gets worse.
- `rf_vl_double`: Source difference: the Vision loss page lists double vision as urgent. The Double vision page says see an optician or GP unless it started suddenly or comes with eye pain. Soft; the double vision entry symptom's own rules also apply.
- `or_vl_distorted`: Clinical knowledge: new distortion can be the 'wet' type of macular degeneration, which is treated with injections and should be seen within days. The AMD page says vision can get worse quickly over weeks. An optician has no level of its own, so general practice is used.
- `sight_lost default outcome`: The page says see an optician if you think you may have vision loss. An optician has no level of its own in settings.yaml, so general practice (routine) is used, and the advice names the optician.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Swollen blood vessels in the head (temporal arteritis) | 414341000 | rare | Jaw pain when eating, or a sore or tender scalp or temple: strongly supports; Change in sight or loss of vision: supports; Headache feels different from usual headaches: supports; Feels very tired: supports; Aching body: supports; Losing weight without trying: supports; Headache: strongly supports; Double vision: supports; Feels very unwell: supports; Pain and stiffness in both shoulders or both hips, worst in the morning: supports; Lost the sight in 1 eye for a short time, then it came back: supports; Cannot see out of 1 or both eyes, or a large part of the sight is missing: supports |
| Migraine | 37796009 | common | Throbbing headache, often on one side, worse when moving: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; Feels sick or has been sick: supports; Being sick: supports; Warning signs such as zigzag lines or flashing lights: strongly supports; Headache: strongly supports; Gets headaches regularly: supports; Both eyes affected: supports |
| Sudden glaucoma (a quick build-up of pressure inside the eye) |  | rare | Severe eye pain: strongly supports; Glowing rings (halos) around lights: strongly supports; Headache: strongly supports; Feels sick or has been sick: strongly supports; Very painful headache: supports; Blurred, cloudy or misty sight: supports; White of the eye very red: supports; Front of the eye looks cloudy, or has a white spot: supports; Eye pain or other eye symptoms started suddenly: supports; Red or bloodshot eye: supports |
| Serious injury from a blow to the eye (bleeding inside the eye or a broken eye socket) |  | very rare | Hit in the eye by something blunt: strongly supports; Injured eye, or something hit the eye: strongly supports; Double vision: supports; Hard or painful to move the eye: supports; Severe eye pain: supports; Feels sick or has been sick: supports; Change in sight or loss of vision: supports |
| Cataracts (the lens inside the eye becomes cloudy) | 193570009 | uncommon | Sight getting worse slowly, over months or years: strongly supports; Blurred, cloudy or misty sight: strongly supports; Glowing rings (halos) around lights: supports; Harder to see at night or in dim light: supports; Colours look faded or washed out: supports; Double vision stays when 1 eye is covered: supports; Has diabetes: supports; Smokes, or has smoked in the past: supports |
| Eye damage from diabetes (diabetic retinopathy) | 4855003 | rare | Has diabetes: strongly supports; Blurred, cloudy or misty sight: supports; Sight getting worse slowly, over months or years: supports; Harder to see at night or in dim light: supports; Floaters or flashes in the eyes: supports |
| Eye cancer |  | very rare | A dark patch on the eye that is getting bigger: strongly supports; Blurred, cloudy or misty sight: supports; Dark curtain or shadow across the sight: supports; Floaters or flashes in the eyes: supports |
| Eye stroke (a blocked blood vessel at the back of the eye) | 38742007 | very rare | Cannot see out of 1 or both eyes, or a large part of the sight is missing: strongly supports; Sight changed suddenly: strongly supports; Change in sight in 1 eye only: strongly supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Lost the sight in 1 eye for a short time, then it came back: supports |
| Infection inside the eye after surgery or an injection in the eye | 1847009 | very rare | Eye surgery or eye treatment in the last 4 weeks: strongly supports; Severe eye pain: strongly supports; Change in sight or loss of vision: strongly supports; Red or bloodshot eye: supports; Sticky discharge (pus) from the eye: supports |
| Keratitis or an eye ulcer (a sore on the clear front of the eye), often from contact lenses | 5888003 | rare | Wears contact lenses: strongly supports; Front of the eye looks cloudy, or has a white spot: strongly supports; Eye pain: strongly supports; Bright lights hurt the eyes or are bothering you: supports; Red or bloodshot eye: supports; Watering eyes: supports; Blurred, cloudy or misty sight: supports; Feels like something is in the eye: supports |
| Macular degeneration (AMD), which blurs the middle of your sight as you age | 267718000 | rare | Middle of the sight distorted, straight lines look wavy: strongly supports; Blurred, cloudy or misty sight: supports; Change in sight in 1 eye only: supports; Sight getting worse slowly, over months or years: supports; Sight got worse over a few days: supports; Smokes, or has smoked in the past: supports |
| Needing glasses or a new prescription (short sight, long sight or astigmatism) | 39021009 | common | Hard to see far away or close up, clear at other distances: strongly supports; Sight getting worse slowly, over months or years: strongly supports; Headache: supports; Double vision stays when 1 eye is covered: supports; 1 eye turns in, out, up or down: supports |
| Glaucoma that comes on slowly (damage to the nerve at the back of the eye) | 77075001 | rare | Losing sight at the edges: strongly supports; Sight getting worse slowly, over months or years: strongly supports; Parent, brother or sister with glaucoma: supports; Has diabetes: supports; Short-sighted: supports |
| Optic neuritis (swelling of the nerve at the back of the eye) | 66760008 | rare | Eye hurts more when moving it: strongly supports; Sight got worse over a few days: strongly supports; Colours look faded or washed out: strongly supports; Eye pain: supports; Change in sight in 1 eye only: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports |
| A cut through the eye, or something inside the eye |  | very rare | Something sharp cut or pierced the eye: strongly supports; Something hit the eye at high speed: strongly supports; Injured eye, or something hit the eye: strongly supports; Change in sight or loss of vision: supports; Eye pain: supports |
| Detached retina (the thin layer at the back of the eye coming loose) | 42059000 | uncommon | Dark curtain or shadow across the sight: strongly supports; Floaters or flashes that are new, sudden, or suddenly more: strongly supports; Floaters or flashes in the eyes: strongly supports; Blurred, cloudy or misty sight: supports; Sight changed suddenly: supports; Short-sighted: supports; Eye surgery or eye treatment in the last 4 weeks: supports; Injured eye, or something hit the eye: supports |
| A blocked vein at the back of the eye (retinal vein occlusion) | 1237532002 | very rare | Sight changed suddenly: strongly supports; Blurred, cloudy or misty sight: strongly supports; Change in sight in 1 eye only: strongly supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports; Has diabetes: supports |
| Squint (the eyes point in different directions) | 22066006 | rare | 1 eye turns in, out, up or down: strongly supports; Double vision goes when either eye is covered: supports; Double vision: supports; Hard to see far away or close up, clear at other distances: supports |
| Stroke or mini-stroke (TIA) affecting the sight |  | very rare | Suddenly lost the same side of the sight in both eyes: strongly supports; Lost the sight in 1 eye for a short time, then it came back: strongly supports; Sight changed suddenly: strongly supports; Difficulty speaking: supports; Dizzy or off-balance: supports; Double vision started suddenly: supports; Smokes, or has high blood pressure, diabetes or high cholesterol: supports |
| Iritis or uveitis (swelling inside the eye that makes it red, sore and hurt in bright light) | 128473001 | rare | Bright lights hurt the eyes or are bothering you: strongly supports; Redness worst in a ring around the coloured part of the eye: strongly supports; Red or bloodshot eye: strongly supports; Eye pain: strongly supports; Deep, boring ache in the eye: supports; Blurred, cloudy or misty sight: supports; Has a condition such as ankylosing spondylitis, rheumatoid arthritis, Crohn's, lupus or MS: supports; Floaters or flashes in the eyes: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
