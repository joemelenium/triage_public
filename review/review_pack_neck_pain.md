# Review pack: Neck pain

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
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | 2026-11-19 |  | Page last reviewed: 02 August 2023 |
| [Falls](https://www.nhs.uk/conditions/falls/) | 2026-11-19 |  | Page last reviewed: 06 March 2025 |
| [Whiplash](https://www.nhs.uk/conditions/whiplash/) | 2026-11-19 |  | Page last reviewed: 19 August 2026 |
| [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | 2026-11-19 |  | Page last reviewed: 23 April 2023 |
| [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | 2026-11-19 |  | Page last reviewed: 27 April 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | 2026-11-18 |  | Page last reviewed: 13 June 2024 |
| [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | 2026-11-19 |  | Page last reviewed: 28 August 2025 |
| [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | 2026-11-19 |  | Page last reviewed: 12 June 2023 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Angina](https://www.nhs.uk/conditions/angina/) | 2026-11-18 | 2025-03-18 |  |

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

## Neck pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to you right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_neck_meningitis_signs`<br>Stiff neck with a high temperature, a very painful headache, or finding it hard to look at bright lights<br>**Note:** Possible meningitis. Neck pain is one of the entry symptoms on the meningitis card. | "Stiff neck" AND ("Very high temperature, or feels hot, cold or shivery" OR "Very painful headache" OR "Bright lights hurt the eyes or are bothering you") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_neck_rash`<br>Neck pain or stiffness with a rash that does not fade when a glass is pressed on it<br>**Note:** The Meningitis page says call 999 or go to A&E. The Sepsis page says call 999 for a rash that does not fade. The more urgent is used. | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_neck_sudden_headache`<br>Neck pain with a sudden, very bad headache<br>**Note:** Could be bleeding on the brain or a tear in an artery in the neck. AI judgement, needs clinical review. The brain and nerves body system will hold the headache rules. | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_neck_spinal_cord`<br>Neck pain with new problems walking or with balance, sudden clumsiness, or loss of bladder or bowel control<br>**Note:** Signs of pressure on the spinal cord in the neck. | "New problems walking, with balance, or doing fiddly tasks" OR "New problems peeing or pooing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| `rf_neck_serious_accident`<br>Neck pain after a serious accident, such as a car crash or a fall from a height<br>**Note:** The Falls page says call 999 if someone has fallen and may have injured their head, back or neck. Applying it to any serious accident is AI judgement. | "A serious accident, such as a car crash or a fall from a height" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999. Keep still and do not move your neck.* | [Falls](https://www.nhs.uk/conditions/falls/) | |
| `rf_neck_chest_pain`<br>Neck or jaw pain with chest pain<br>**Note:** Heart attack pain can spread to the neck and jaw. A yes to chest pain also brings in the chest pain entry symptom. | "Chest pain" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |

## Neck pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to you? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_neck_weakness`<br>Neck pain with weakness or heaviness in the arms or legs | "Weak arm or hand, or a weak grip" OR "Weakness in one or both legs, or a foot that drags" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| `rf_neck_injury_nerve_signs`<br>Neck injury with an electric shock feeling, or severe pain despite painkillers<br>**Note:** Could be damage to the nerves in the neck. Do not drive or cycle until checked. | "Electric shock feeling in the neck or back, into the arms or legs" OR ("Started after an injury, fall or accident" AND "Severe pain") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Whiplash](https://www.nhs.uk/conditions/whiplash/) | |
| `rf_neck_severe_sudden_or_worsening`<br>Severe neck pain that started suddenly, or neck pain getting worse quickly | ("Severe pain" AND "Pain started suddenly") OR "Pain getting worse quickly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| `rf_neck_arm_tingling`<br>Neck pain with pins and needles or numbness in an arm or hand<br>**Note:** Source difference: the Cervical spondylosis page says urgent GP or 111 for pins and needles in an arm with neck pain. The Neck pain page says see a GP. The more urgent is used, marked soft so a likely trapped nerve can lower it. | "Pins and needles, tingling or numbness in the arm, hand or fingers" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| `rf_neck_between_shoulder_blades`<br>Neck pain with pain between the shoulder blades<br>**Note:** The Back pain page gives see a GP for pain between the shoulders. Marked soft: AI judgement, needs clinical review. | "Pain in the upper back" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| `rf_neck_giant_cell_arteritis`<br>Neck or shoulder pain with a new headache, a tender scalp, jaw pain when eating or problems with sight<br>**Note:** Signs of inflamed blood vessels in the head (giant cell arteritis), which can cause blindness or a stroke if not treated quickly. | "Jaw pain when eating, or a sore or tender scalp or temple" OR "Change in sight or loss of vision" OR "Headache feels different from usual headaches" | Urgent (help today)<br>Urgent care<br>Today<br>*Contact a GP now, or get help from NHS 111* | [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/) | |
| `rf_neck_temperature`<br>Neck pain with a high temperature, or feeling hot, cold or shivery<br>**Note:** Could be an infection in the neck or spine. Meningitis signs are caught by the emergency rule. AI judgement, needs clinical review. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Neck pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_neck_gp`<br>Neck pain that has not gone away after a few weeks, or painkillers have not worked<br>**Note:** Firm: the page says see a GP for these whatever the cause. Split from the worried rule below. | "Pain for 2 weeks or more, not getting better" OR "Painkillers have not helped" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| `or_neck_worried`<br>Worried about neck pain | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |

## Default outcome

Used when no rule fires.

- **Neck pain with nothing that needs more help: it usually gets better within a few weeks**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most neck pain gets better within a few weeks*
- Source: [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Neck pain or stiff neck | Do you have pain or stiffness in your neck? | 81680005 | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Very painful headache | Do you have a very painful headache, worse than any you usually get? |  | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| Bright lights hurt the eyes or are bothering you | Do bright lights hurt your eyes, or bother you much more than usual? | 409668002 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| New problems walking, with balance, or doing fiddly tasks | Have you got new problems walking or with your balance? Or sudden clumsiness with tasks like doing up buttons? |  | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| New problems peeing or pooing | Have you had new problems peeing or pooing? For example, finding it hard to start peeing, not being able to pee, or peeing or pooing yourself. |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| A serious accident, such as a car crash or a fall from a height | Was it a serious accident, such as a car crash, or a fall from higher than 1 metre or down 5 or more stairs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Weak arm or hand, or a weak grip | Does your arm or hand feel weak or heavy, or is your grip weak? |  | [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/) | |
| Weakness in one or both legs, or a foot that drags | Do you have weakness in one or both legs, or does your foot drag or slap when you walk? |  | [Whiplash](https://www.nhs.uk/conditions/whiplash/) | |
| Electric shock feeling in the neck or back, into the arms or legs | Do you get a sudden electric shock feeling in your neck or back, which may go into your arms or legs? |  | [Whiplash](https://www.nhs.uk/conditions/whiplash/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain getting worse quickly | Is the pain getting worse quickly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pins and needles, tingling or numbness in the arm, hand or fingers | Do you have pins and needles, tingling or numbness in your arm, hand or fingers? |  | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Pain in the upper back | Do you have pain in your upper back? | 279038004 | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| Jaw pain when eating, or a sore or tender scalp or temple | Do you have pain in your jaw when eating, or is your scalp or the side of your head (temple) sore or tender to touch? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Change in sight or loss of vision | Has your sight changed or got worse, in a way that does not clear when you blink? For example, it is blurred, cloudy or wavy, you see flashing lights, or you cannot see part of what you usually see. | 63102001 | [Vision loss](https://www.nhs.uk/conditions/vision-loss/) | |
| Headache feels different from usual headaches | Does this headache feel different from the headaches you usually get? |  | [Brain tumours](https://www.nhs.uk/conditions/brain-tumours/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Painkillers have not helped | Have painkillers like paracetamol or ibuprofen not helped? |  | [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_meningitis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of meningitis (an infection of the layers around the brain) or sepsis (a life-threatening reaction to an infection). They need treatment in hospital straight away.

**Look out for:**
- A rash that does not fade when you press a glass against it. On brown or black skin, check paler areas such as the palms of the hands.
- Being very sleepy, confused or hard to wake
- A seizure (fit)
- In a baby: being floppy, not feeding, or a high-pitched cry
- Skin, lips or tongue turning blue, grey, pale or blotchy

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Do not wait for a rash. Get help if you are worried, even if there is no rash.
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive yourself to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Meningitis](https://www.nhs.uk/conditions/meningitis/), [Headaches](https://www.nhs.uk/symptoms/headaches/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

### `advice_neck_pain_999`

**What to do:** Call 999 now. These can be signs of pressure on the spinal cord, or bleeding on the brain.

**Look out for:**
- Weakness or numbness getting worse
- Face drooping, slurred speech or not being able to lift both arms
- Being very sleepy or confused

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. Do not drive yourself.

Source: [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/), [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/)

### `advice_spinal_injury_emergency`

**What to do:** Call 999 or go to A&E now. The spine may be injured after a serious accident.

**Look out for:**
- Numbness, tingling or weakness in the arms or legs
- Problems peeing or pooing
- Being sick, very sleepy or confused after hitting the head

**Get more help when:**
- Call 999 straight away if the neck or back may be hurt. Do not move the person unless they are in danger.

**Where to go:** Call 999 for an ambulance if the neck or back may be hurt. Otherwise go to A&E. Do not drive yourself.

**What you can do yourself:**
- Keep still and keep the head and neck in line with the body
- Do not try to sit up or walk if your neck or back hurts after a serious accident

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/), [Falls](https://www.nhs.uk/conditions/falls/), [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_chest_pain_999`

**What to do:** Call 999 now. You could be having a heart attack and need treatment in hospital straight away.

**Look out for:**
- Keep checking that the person is still responding and breathing
- If they stop responding and stop breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Get more help when:**
- Call 999 again if the person's condition changes

**Where to go:** Call 999. Do not drive yourself to A&E. The person you speak to at 999 will tell you what to do.

**What you can do yourself:**
- If you think you or someone else is having a heart attack, do these things while you wait for help.
- Sit and rest on the floor with your knees bent and your back supported. If you cannot do this, sit on a chair.
- Take aspirin (300mg) if you have any. Do not give aspirin to someone who has an aspirin allergy.
- If you have angina (chest pain caused by narrowed blood vessels to the heart), use your spray if you have it with you. It goes under your tongue. It may be called glyceryl trinitrate or GTN.

Source: [Heart attack](https://www.nhs.uk/conditions/heart-attack/), [Chest pain](https://www.nhs.uk/symptoms/chest-pain/), [Angina](https://www.nhs.uk/conditions/angina/)

### `advice_neck_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. This could be a trapped nerve or another problem in the neck.

**Look out for:**
- New problems walking, or clumsy hands
- Losing control of your bladder or bowels
- A stiff neck with a high temperature, a very bad headache or a rash

**Get more help when:**
- Call 999 if you get problems walking, lose control of your bladder or bowels, or have a sudden, very bad headache

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Do not drive or cycle until you have been checked
- Take paracetamol or ibuprofen for the pain

Source: [Cervical spondylosis](https://www.nhs.uk/conditions/cervical-spondylosis/), [Whiplash](https://www.nhs.uk/conditions/whiplash/)

### `advice_giant_cell_arteritis_urgent`

**What to do:** Contact a GP straight away, or get help from NHS 111 today. A new headache, a tender scalp, jaw pain when eating, or sight problems can be inflamed blood vessels in the head (giant cell arteritis). Without quick treatment it can cause blindness or a stroke.

**Look out for:**
- Any loss of sight, or double vision
- Signs of a stroke: face drooping, not being able to lift both arms, or slurred speech

**Get more help when:**
- Call 999 or go to A&E if you lose any sight, or have signs of a stroke

**Where to go:** Contact your GP surgery now, or call 111 or use 111 online.

Source: [Polymyalgia rheumatica](https://www.nhs.uk/conditions/polymyalgia-rheumatica/)

### `advice_neck_pain_gp`

**What to do:** See a GP. In many areas you can also refer yourself to a physiotherapist without seeing a GP first.

**Look out for:**
- Pins and needles, numbness or weakness in your arms
- A stiff neck with a high temperature or a very bad headache

**Get more help when:**
- Get an urgent GP appointment or help from 111 if your arms or legs feel weak or heavy
- Call 999 or go to A&E if you have a stiff neck with a high temperature and cannot look at bright lights

**Where to go:** Contact your GP surgery, or look for an NHS service for back and joint problems you can refer yourself to.

**What you can do yourself:**
- Keep your neck moving. Do not wear a neck collar unless a doctor tells you to.
- Use a low, firm pillow

Source: [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/)

### `advice_neck_pain_self_care`

**What to do:** Most neck pain gets better within a few weeks. You can ease it yourself.

**Look out for:**
- Pins and needles, numbness or weakness in your arms
- A stiff neck with a high temperature, a very bad headache, or bright lights hurting your eyes

**Get more help when:**
- Call 999 or go to A&E if you have a stiff neck with a high temperature or a very bad headache
- See a GP if it does not go away after a few weeks, or painkillers do not help

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers.

**What you can do yourself:**
- Take painkillers. Or rub a painkilling gel on your neck.
- Put a pack of frozen peas wrapped in a tea towel on your neck for 5 minutes, 3 times a day. Or use a hot water bottle wrapped in a tea towel.
- Use a low, firm pillow and try gentle neck exercises
- Do not wear a neck collar, and do not drive or cycle if you cannot turn your neck

Source: [Neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_neck_meningitis_signs`: Possible meningitis. Neck pain is one of the entry symptoms on the meningitis card.
- `rf_neck_rash`: The Meningitis page says call 999 or go to A&E. The Sepsis page says call 999 for a rash that does not fade. The more urgent is used.
- `rf_neck_sudden_headache`: Could be bleeding on the brain or a tear in an artery in the neck. AI judgement, needs clinical review. The brain and nerves body system will hold the headache rules.
- `rf_neck_spinal_cord`: Signs of pressure on the spinal cord in the neck.
- `rf_neck_serious_accident`: The Falls page says call 999 if someone has fallen and may have injured their head, back or neck. Applying it to any serious accident is AI judgement.
- `rf_neck_chest_pain`: Heart attack pain can spread to the neck and jaw. A yes to chest pain also brings in the chest pain entry symptom.
- `rf_neck_injury_nerve_signs`: Could be damage to the nerves in the neck. Do not drive or cycle until checked.
- `rf_neck_arm_tingling`: Source difference: the Cervical spondylosis page says urgent GP or 111 for pins and needles in an arm with neck pain. The Neck pain page says see a GP. The more urgent is used, marked soft so a likely trapped nerve can lower it.
- `rf_neck_between_shoulder_blades`: The Back pain page gives see a GP for pain between the shoulders. Marked soft: AI judgement, needs clinical review.
- `rf_neck_giant_cell_arteritis`: Signs of inflamed blood vessels in the head (giant cell arteritis), which can cause blindness or a stroke if not treated quickly.
- `rf_neck_temperature`: Could be an infection in the neck or spine. Meningitis signs are caught by the emergency rule. AI judgement, needs clinical review.
- `or_neck_gp`: Firm: the page says see a GP for these whatever the cause. Split from the worried rule below.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A tear in an artery in the neck, which can cause a stroke |  | very rare | Headache that came on suddenly and is extremely painful: strongly supports; Signs of a stroke: strongly supports; Pain started suddenly: supports; Head suddenly jolted, for example in a car crash: supports |
| Neck pain from age-related wear of the neck bones (cervical spondylosis) | 387800004 | uncommon | Pain on and off for more than 3 months: strongly supports; Pain worse when moving, easier when resting: supports; Stiff for more than 30 minutes after waking: supports; Pain getting worse, or keeps coming back: supports |
| Neck strain or a stiff neck from posture or sleeping awkwardly | 360450007 | very common | Neck stiff after sleeping awkwardly or sitting for a long time: strongly supports; Pain worse when moving, easier when resting: supports; Started after lifting, bending, twisting or an awkward movement: supports |
| Polymyalgia rheumatica (stiff, sore shoulders and hips) | 65323003 | rare | Pain and stiffness in both shoulders or both hips, worst in the morning: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Feels very tired: supports; Losing weight without trying: supports; Jaw pain when eating, or a sore or tender scalp or temple: supports |
| Pressure on the spinal cord (spinal cord compression) | 71286001 | rare | Weakness in one or both legs, or a foot that drags: strongly supports; New problems walking, with balance, or doing fiddly tasks: strongly supports; Pain, tingling, weakness or numbness in both legs: supports; New problems peeing or pooing: supports; Pain in the upper back: supports; Pain worse at night, or not better with rest: supports; Weak arm or hand, or a weak grip: supports; Pain worse when coughing, sneezing or pooing: supports |
| An infection in the spine, such as a spinal abscess (a pocket of pus) or an infected disc |  | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Feels cold to the touch, or shivery: supports; Pain worse at night, or not better with rest: supports; Severe pain: supports |
| A serious injury to the spine or spinal cord, such as a broken neck or back |  | very rare | A serious accident, such as a car crash or a fall from a height: strongly supports; Started after an injury, fall or accident: strongly supports; Numb, tingling or no feeling below the injury: supports; Pain, tingling, weakness or numbness in both legs: supports; Severe pain: supports; Electric shock feeling in the neck or back, into the arms or legs: supports |
| A trapped nerve in the neck, causing pain or tingling down the arm | 54404000 | uncommon | Pain spreads from the neck or shoulder down the arm: strongly supports; Pins and needles, tingling or numbness in the arm, hand or fingers: strongly supports; Weak arm or hand, or a weak grip: supports; Pins and needles all the time: supports |
| Whiplash (a neck injury from the head being jolted) | 39848009 | uncommon | Head suddenly jolted, for example in a car crash: strongly supports; Started after an injury, fall or accident: strongly supports; Pain worse when moving, easier when resting: supports |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
