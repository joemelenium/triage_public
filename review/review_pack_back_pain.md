# Review pack: Back pain

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
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | 2026-11-18 |  | Page last reviewed: 14 August 2026 |
| [Abdominal aortic aneurysm](https://www.nhs.uk/conditions/abdominal-aortic-aneurysm/) | 2026-11-19 |  | Page last reviewed: 14 June 2023 |
| [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | 2026-11-19 |  | Page last reviewed: 29 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Whiplash](https://www.nhs.uk/conditions/whiplash/) | 2026-11-19 |  | Page last reviewed: 19 August 2026 |
| [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | 2026-11-18 |  | Page last reviewed: 13 June 2024 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sciatica](https://www.nhs.uk/conditions/sciatica/) | 2026-11-19 |  | Page last reviewed: 03 December 2024 |
| [Slipped disc](https://www.nhs.uk/conditions/slipped-disc/) | 2026-11-19 |  | Page last reviewed: 24 April 2024 |
| [Falls](https://www.nhs.uk/conditions/falls/) | 2026-11-19 |  | Page last reviewed: 06 March 2025 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |

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

## Back pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to you right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_back_cauda_equina`<br>Back pain with signs of pressure on the nerves at the bottom of the spine: symptoms in both legs, numbness around the genitals or bottom, new problems peeing or pooing, or changes during sex<br>**Note:** Signs of cauda equina syndrome. The Sciatica and Slipped disc pages give the same advice. This needs treatment in hospital within hours to prevent lasting damage. | "Pain, tingling, weakness or numbness in both legs" OR "Numb or no feeling around the genitals or bottom" OR "New problems peeing or pooing" OR "Changes in feeling or function during sex" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_back_chest_pain`<br>Back pain with chest pain<br>**Note:** A yes to chest pain also brings in the chest pain entry symptom and its red flags. | "Chest pain" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_back_serious_accident`<br>Back pain that started after a serious accident, such as a car crash or a fall from a height | "A serious accident, such as a car crash or a fall from a height" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_back_tearing_pain`<br>Sudden, severe chest or back pain that feels like something tearing inside<br>**Note:** A sign of a tear in the body's main blood vessel (aortic dissection). The same rule is used for chest pain. | "Sudden severe chest or back pain, like something tearing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | |
| `rf_back_sudden_tummy_pain`<br>Back pain with sudden, very bad tummy pain<br>**Note:** The Abdominal aortic aneurysm page says call 999 for sudden, severe pain in the tummy or back, which could be a swollen main blood vessel bursting. | "Sudden, very bad pain in the tummy as well as the back" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Abdominal aortic aneurysm](https://www.nhs.uk/conditions/abdominal-aortic-aneurysm/) | |
| `rf_back_sudden_severe_older`<br>Severe back pain that started suddenly in someone aged 65 or over<br>**Note:** Source difference: the Abdominal aortic aneurysm page says call 999 for sudden, severe back pain. The Back pain page says urgent GP or 111 for severe pain that starts suddenly. The more urgent is used for people aged 65 or over, where a burst aneurysm is a real possibility. Marked soft and limited by age: AI judgement, needs clinical review. The firm urgent rule below still applies. | "Severe pain" AND "Pain started suddenly" AND "Aged 65 or over" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Abdominal aortic aneurysm](https://www.nhs.uk/conditions/abdominal-aortic-aneurysm/) | |

## Back pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to you? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_back_unwell_temperature`<br>Back pain with a high temperature, feeling hot, cold or shivery, or feeling generally unwell<br>**Note:** Could be an infection in the spine or kidney. The Slipped disc page says see a GP for back pain with a high temperature; the Back pain page says urgent. The more urgent is used. | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_back_severe_sudden_or_worsening`<br>Severe back pain that started suddenly, or back pain that is getting worse quickly | ("Severe pain" AND "Pain started suddenly") OR "Pain getting worse quickly" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `rf_back_leg_weakness`<br>Back pain with weakness in a leg, or a foot that drags<br>**Note:** Weakness from a trapped nerve needs checking the same day, as it may need an urgent scan. Weakness in both legs is caught by the emergency rule. The Sciatica page says A&E for weakness in both legs that is severe or getting worse. | "Weakness in one or both legs, or a foot that drags" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |
| `rf_back_cancer_history`<br>Back pain in someone who has or has had cancer, with pain that is severe, worse at night, worse when coughing or in the upper back<br>**Note:** Cancer that has spread to the spine can press on the spinal cord. Finding it before the legs become weak gives the best outcome. AI judgement, needs clinical review. | "Has cancer, or is having treatment for cancer" AND ("Severe pain" OR "Pain worse at night, or not better with rest" OR "Pain worse when coughing, sneezing or pooing" OR "Pain in the upper back") | Urgent (help today)<br>Urgent care<br>Today<br>*Contact your cancer team or get help from NHS 111 today* | **AI judgement, needs clinical review** | |
| `rf_back_injury_thin_bones`<br>Back pain after a fall or injury in someone aged 65 or over, or with thin bones or long-term steroid tablets<br>**Note:** The Osteoporosis page says get urgent help after a recent fall or injury if the pain is not getting better, as a bone in the spine may be broken. Applying it to anyone 65 or over is AI judgement. | "Started after an injury, fall or accident" AND ("Aged 65 or over" OR "Thin bones (osteoporosis), or long-term steroid tablets") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | |

## Back pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_back_cancer_signs`<br>Back pain with weight loss, or in someone who has or has had cancer<br>**Note:** The Back pain page says see a GP for back pain with weight loss. Within a few days, not 'no fixed time', is AI judgement because it can be a sign of cancer. | "Losing weight without trying" OR "Has cancer, or is having treatment for cancer" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within a few days* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `or_back_gp_warning_signs`<br>Back pain with a lump or change of shape, pain worse at night or not better with rest, pain worse when coughing, sneezing or pooing, or pain in the upper back | "A lump or swelling in the back, or the back has changed shape" OR "Pain worse at night, or not better with rest" OR "Pain worse when coughing, sneezing or pooing" OR "Pain in the upper back" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `or_back_not_improving`<br>Back pain that has not improved after a few weeks, or is stopping day-to-day activities<br>**Note:** Firm: the page says see a GP for these whatever the cause, including ordinary back strain. Split from the worried rule below after the development cases. | "Pain for 2 weeks or more, not getting better" OR "Pain stopping usual activities or affecting sleep" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| `or_back_worried`<br>Worried about back pain, or struggling to cope | "Worried about symptoms" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Default outcome

Used when no rule fires.

- **Back pain with nothing that needs more help: it usually gets better on its own within a few weeks**
- Outcome: Self-manageable, Self-care, No appointment needed. *Back pain usually gets better within a few weeks*
- Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Back pain | Do you have back pain? | 161891005 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Pain, tingling, weakness or numbness in both legs | Do you have pain, tingling, weakness or numbness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| New problems peeing or pooing | Have you had new problems peeing or pooing? For example, finding it hard to start peeing, not being able to pee, or peeing or pooing yourself. |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Changes in feeling or function during sex | Have you noticed a change in how your penis or vagina feels during sex? Or are you suddenly unable to get or keep an erection, or to orgasm? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Chest pain | Do you have pain or discomfort in your chest? | 29857009 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| A serious accident, such as a car crash or a fall from a height | Was it a serious accident, such as a car crash, or a fall from higher than 1 metre or down 5 or more stairs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Sudden severe chest or back pain, like something tearing | Did severe pain in your chest or back start suddenly, and feel like something is tearing inside? |  | [Costochondritis](https://www.nhs.uk/conditions/costochondritis/) | |
| Sudden, very bad pain in the tummy as well as the back | As well as the back pain, did very bad pain in your tummy come on suddenly? |  | [Abdominal aortic aneurysm](https://www.nhs.uk/conditions/abdominal-aortic-aneurysm/) | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Aged 65 or over | Is the person who is unwell aged 65 or over? |  | **AI judgement, needs clinical review** | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pain getting worse quickly | Is the pain getting worse quickly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Weakness in one or both legs, or a foot that drags | Do you have weakness in one or both legs, or does your foot drag or slap when you walk? |  | [Whiplash](https://www.nhs.uk/conditions/whiplash/) | |
| Has cancer, or is having treatment for cancer | Do you have cancer, or are you having treatment for cancer? |  | **AI judgement, needs clinical review** | |
| Pain worse at night, or not better with rest | Is the pain worse at night, or does it not get better when you rest? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain worse when coughing, sneezing or pooing | Is the pain worse when you cough, sneeze or poo? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain in the upper back | Do you have pain in your upper back? | 279038004 | [Coughing up blood](https://www.nhs.uk/symptoms/coughing-up-blood/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Thin bones (osteoporosis), or long-term steroid tablets | Do you have thin, weak bones (osteoporosis)? Or have you taken steroid tablets for 3 months or more? |  | [Osteoporosis](https://www.nhs.uk/conditions/osteoporosis/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| A lump or swelling in the back, or the back has changed shape | Is there a lump or swelling in your back, or has your back changed shape? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
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

### `advice_spinal_nerve_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of pressure on the nerves at the bottom of the spine (cauda equina syndrome). This needs treatment in hospital as soon as possible.

**Look out for:**
- Numbness around your genitals or bottom getting worse
- Not being able to pee, or not being able to control when you pee or poo
- Weakness or numbness in both legs

**Get more help when:**
- Do not wait to see if it gets better. Go now, even at night.

**Where to go:** Go to A&E now, or call 999. Do not drive yourself. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/), [Sciatica](https://www.nhs.uk/conditions/sciatica/), [Slipped disc](https://www.nhs.uk/conditions/slipped-disc/)

### `advice_back_pain_999`

**What to do:** Call 999 now. Back pain with chest pain, or sudden very bad pain in your back or tummy, can be a sign of a heart attack or a problem with the main blood vessel in the body.

**Look out for:**
- Feeling faint, or passing out
- Skin turning pale, grey or sweaty
- Being short of breath

**Get more help when:**
- Call 999 again if things get worse before help arrives
- If the person stops responding and stops breathing, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Do not drive yourself to A&E. Stay with someone until help arrives.

Source: [Abdominal aortic aneurysm](https://www.nhs.uk/conditions/abdominal-aortic-aneurysm/), [Back pain](https://www.nhs.uk/conditions/back-pain/), [Heart attack](https://www.nhs.uk/conditions/heart-attack/)

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

### `advice_back_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today.

**Look out for:**
- Numbness around your genitals or bottom
- Problems peeing or pooing
- Pain, tingling, weakness or numbness in both legs

**Get more help when:**
- Call 999 or go to A&E if you get any of these, or chest pain

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Keep moving gently if you can
- Take painkillers such as ibuprofen if they are right for you

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_back_pain_cancer_urgent`

**What to do:** Contact your cancer team, or get help from NHS 111 today. New back pain in someone who has had cancer needs checking quickly, in case the cancer has spread to the spine.

**Look out for:**
- Weakness, numbness or heaviness in your legs
- Problems walking
- Problems peeing or pooing

**Get more help when:**
- Call 999 or go to A&E if your legs become weak or numb, or you cannot control when you pee or poo

**Where to go:** Call your cancer team's helpline if you have one. If not, call 111 or use 111 online.

Source: **AI judgement, needs clinical review**, [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_msk_gp_soon`

**What to do:** See a GP within a few days. Back pain with weight loss, or in someone who has had cancer, needs checking.

**Look out for:**
- Weakness or numbness in your legs
- Problems peeing or pooing
- Pain in your upper back, or pain that wakes you at night

**Get more help when:**
- Call 999 or go to A&E if you go numb around your genitals or bottom. Do the same if you have problems peeing or pooing, or both legs feel weak.
- Contact your cancer team or 111 if your pain gets much worse

**Where to go:** Ask your GP surgery for an appointment in the next few days.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_back_pain_gp`

**What to do:** See a GP. In many areas you can also refer yourself to a physiotherapist without seeing a GP first.

**Look out for:**
- Numbness around your genitals or bottom
- Problems peeing or pooing
- Pain, tingling, weakness or numbness in both legs
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if you go numb around your genitals or bottom. Do the same if you have problems peeing or pooing, or pain, tingling or weakness in both legs.
- Get an urgent GP appointment or help from 111 if you feel hot, cold or shivery, or the pain gets worse quickly

**Where to go:** Contact your GP surgery, or look for an NHS service for back and joint problems you can refer yourself to.

**What you can do yourself:**
- Stay active and keep doing your daily activities if you can
- Take ibuprofen if it is right for you. Paracetamol on its own is not recommended for back pain.
- Do not stay in bed for long periods

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

### `advice_back_pain_self_care`

**What to do:** Back pain usually gets better on its own within a few weeks. Stay active and ease the pain yourself.

**Look out for:**
- Numbness around your genitals or bottom
- Problems peeing or pooing
- Pain, tingling, weakness or numbness in both legs
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if you go numb around your genitals or bottom. Do the same if you have problems peeing or pooing, or pain, tingling or weakness in both legs.
- See a GP if it has not improved after a few weeks, or it is stopping you doing your usual activities

**Where to go:** You do not need to see anyone now. A pharmacist can help you choose a painkiller.

**What you can do yourself:**
- Stay active and try to carry on with your daily activities
- Take ibuprofen if it is right for you. Paracetamol on its own is not recommended for back pain.
- Use an ice pack or a heat pack wrapped in a tea towel
- Try back stretches. Walking, swimming, yoga or pilates can also help.
- Do not stay in bed for long periods

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_back_cauda_equina`: Signs of cauda equina syndrome. The Sciatica and Slipped disc pages give the same advice. This needs treatment in hospital within hours to prevent lasting damage.
- `rf_back_chest_pain`: A yes to chest pain also brings in the chest pain entry symptom and its red flags.
- `rf_back_tearing_pain`: A sign of a tear in the body's main blood vessel (aortic dissection). The same rule is used for chest pain.
- `rf_back_sudden_tummy_pain`: The Abdominal aortic aneurysm page says call 999 for sudden, severe pain in the tummy or back, which could be a swollen main blood vessel bursting.
- `rf_back_sudden_severe_older`: Source difference: the Abdominal aortic aneurysm page says call 999 for sudden, severe back pain. The Back pain page says urgent GP or 111 for severe pain that starts suddenly. The more urgent is used for people aged 65 or over, where a burst aneurysm is a real possibility. Marked soft and limited by age: AI judgement, needs clinical review. The firm urgent rule below still applies.
- `rf_back_unwell_temperature`: Could be an infection in the spine or kidney. The Slipped disc page says see a GP for back pain with a high temperature; the Back pain page says urgent. The more urgent is used.
- `rf_back_leg_weakness`: Weakness from a trapped nerve needs checking the same day, as it may need an urgent scan. Weakness in both legs is caught by the emergency rule. The Sciatica page says A&E for weakness in both legs that is severe or getting worse.
- `rf_back_cancer_history`: Cancer that has spread to the spine can press on the spinal cord. Finding it before the legs become weak gives the best outcome. AI judgement, needs clinical review.
- `rf_back_injury_thin_bones`: The Osteoporosis page says get urgent help after a recent fall or injury if the pain is not getting better, as a bone in the spine may be broken. Applying it to anyone 65 or over is AI judgement.
- `or_back_cancer_signs`: The Back pain page says see a GP for back pain with weight loss. Within a few days, not 'no fixed time', is AI judgement because it can be a sign of cancer.
- `or_back_not_improving`: Firm: the page says see a GP for these whatever the cause, including ordinary back strain. Split from the worried rule below after the development cases.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Ankylosing spondylitis (a long-term stiff, sore spine) | 9631008 | uncommon | Stiff for more than 30 minutes after waking: strongly supports; Stiffness and pain get better with exercise, not with rest: strongly supports; Pain on and off for more than 3 months: strongly supports; Pain worse at night, or not better with rest: supports; Red or bloodshot eye: supports |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Back strain or non-specific back pain (a pulled muscle, or pain with no single clear cause) |  | very common | Started after lifting, bending, twisting or an awkward movement: strongly supports; Pain worse when moving, easier when resting: strongly supports; Pain in the lower back: strongly supports; Pain stopping usual activities or affecting sleep: supports |
| A broken bone in the spine from thin bones (osteoporosis) | 11311601000119109 | rare | Pain started suddenly: strongly supports; Severe pain: supports; Started after an injury, fall or accident: supports; A lump or swelling in the back, or the back has changed shape: supports |
| Sciatica (a trapped nerve causing pain down the leg), often from a slipped disc | 23056005 | common | Pain spreads from the back or bottom down the leg: strongly supports; Numbness, tingling or pins and needles in the leg or foot: strongly supports; Pain worse when coughing, sneezing or pooing: supports; Pain in the lower back: supports; Started after lifting, bending, twisting or an awkward movement: supports; Weakness in one or both legs, or a foot that drags: supports |
| Cancer affecting the spine | 94602001 | rare | Pain worse at night, or not better with rest: strongly supports; Losing weight without trying: supports; Pain in the upper back: supports; A lump or swelling in the back, or the back has changed shape: supports |
| Pressure on the spinal cord (spinal cord compression) | 71286001 | rare | Weakness in one or both legs, or a foot that drags: strongly supports; New problems walking, with balance, or doing fiddly tasks: strongly supports; Pain, tingling, weakness or numbness in both legs: supports; New problems peeing or pooing: supports; Pain in the upper back: supports; Pain worse at night, or not better with rest: supports; Weak arm or hand, or a weak grip: supports; Pain worse when coughing, sneezing or pooing: supports |
| An infection in the spine, such as a spinal abscess (a pocket of pus) or an infected disc |  | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Feels cold to the touch, or shivery: supports; Pain worse at night, or not better with rest: supports; Severe pain: supports |
| A serious injury to the spine or spinal cord, such as a broken neck or back |  | very rare | A serious accident, such as a car crash or a fall from a height: strongly supports; Started after an injury, fall or accident: strongly supports; Numb, tingling or no feeling below the injury: supports; Pain, tingling, weakness or numbness in both legs: supports; Severe pain: supports; Electric shock feeling in the neck or back, into the arms or legs: supports |
| Narrowing of the spine that presses on nerves (spinal stenosis) | 18347007 | rare | Pain spreads from the back or bottom down the leg: strongly supports; Pain comes on with exercise or walking, and goes with rest: strongly supports; Numbness, tingling or pins and needles in the leg or foot: supports; Pain on and off for more than 3 months: supports |
| A burst swelling in the main blood vessel in the tummy (aortic aneurysm) | 14336007 | very rare | Stomach ache that started suddenly and is severe: strongly supports; Tummy pain that spreads to the back: strongly supports; Sudden, very bad pain in the tummy as well as the back: strongly supports; Feels light-headed: supports; Passed out (fainted): supports; Cold, clammy and pale skin: supports; A pulsing feeling in the tummy: supports; Told they have a swelling in the main blood vessel in the tummy (abdominal aortic aneurysm): supports; Smokes, or has smoked in the past: supports |
| Kidney infection | 45816000 | rare | Pain in the back or side, just under the ribs: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Pain, burning or stinging when peeing: supports; Feels cold to the touch, or shivery: supports; Feels sick or has been sick: supports; Peeing more often than usual: supports; Being sick: supports; Feels very unwell: supports |
| Kidney stones | 95570007 | uncommon | Pain in the back or side, just under the ribs: strongly supports; Cramping tummy pain that comes and goes in waves: strongly supports; Blood in pee: supports; Severe stomach ache: supports; Feeling sick (nausea): supports; Being sick: supports; Severe pain in the side or back that comes in waves: strongly supports; Pain spreads down to the groin: strongly supports; Feels sick or has been sick: supports; Has had kidney stones before: supports; Peeing more often than usual: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
