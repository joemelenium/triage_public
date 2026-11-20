# Review pack: Seizure (fit)

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
| [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | 2026-11-19 |  | Page last reviewed: 19 December 2023 |
| [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | 2026-11-19 |  | Page last reviewed: 04 September 2025 |
| [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | 2026-11-19 |  | Page last reviewed: 21 June 2023 |
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Epilepsy](https://www.nhs.uk/conditions/epilepsy/) | 2026-11-19 |  | Page last reviewed: 06 March 2025 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Fainting](https://www.nhs.uk/symptoms/fainting/) | 2026-11-18 |  | Page last reviewed: 17 August 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
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

## Seizure (fit) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sz_first`<br>The first time someone has had a seizure<br>**Note:** The Epilepsy page says the same. The Febrile seizures page says call 999 or go to A&E for a child's first febrile seizure. The more urgent is used. | "First ever seizure" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| `rf_sz_long`<br>A seizure lasting more than 5 minutes, or longer than usual for the person | "Seizure lasting more than 5 minutes, or longer than usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| `rf_sz_not_recovered`<br>Not waking up fully, or several seizures without waking up in between | "Not woken up fully, or another seizure without waking in between" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| `rf_sz_injured`<br>Seriously injured during the seizure | "Seriously hurt when they passed out, fell or had a seizure" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| `rf_sz_breathing`<br>Difficulty breathing after the seizure | "Difficulty breathing" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999 and ask for an ambulance* | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| `rf_sz_headache_sudden`<br>A seizure with a headache that came on suddenly and is extremely painful | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_sz_more_than_one`<br>More than one seizure in 24 hours<br>**Note:** Source difference: the Febrile seizures page says call 999 or go to A&E for more than 1 seizure in 24 hours. The Epilepsy page says call 999 for 3 or more in 24 hours. The Febrile seizures threshold is used for everyone, which is AI judgement for adults. | "More than one seizure in 24 hours" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| `rf_sz_one_side`<br>Stiffness or jerking on only one side of the body | "Stiffness or jerking on only one side of the body" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| `rf_sz_sleepy_after`<br>Much sleepier than usual for more than 1 hour after the seizure stopped | "Much sleepier than usual for more than 1 hour after the seizure" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| `rf_sz_rash_or_stiff_neck`<br>A seizure with a rash that does not fade when pressed, or a stiff neck: possible meningitis | "Rash that does not fade when pressed" OR "Stiff neck" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_sz_head_injury`<br>A seizure after a head injury in the last 3 months<br>**Note:** The Head injury page says call 999 for a fit after a recent head injury; that entry symptom applies too when the injury was in the last month. The Headaches page says 999 or A&E for a headache after a head injury in the last 3 months. | "Head injury in the last 3 months" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| `rf_sz_low_sugar`<br>A seizure in someone with diabetes who has signs of low blood sugar<br>**Note:** The Low blood sugar page lists a seizure as a sign of severe low blood sugar, and says call 999 if someone is not responding normally and glucagon is not available or has not worked. | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999. Do not give food or drink unless they are fully awake and can swallow safely.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Seizure (fit) red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sz_high_temperature`<br>A seizure with a high temperature<br>**Note:** The Febrile seizures page says it is important to get medical help if a child has a seizure. A first febrile seizure is sent to 999 by the rule above. The encephalitis and meningitis condition cards can raise this for an adult. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 or an urgent GP appointment today* | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| `rf_sz_after_long_gap`<br>Epilepsy, and a seizure after a long time without any | "Diagnosed with epilepsy" AND "A seizure after a long time without any" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Epilepsy](https://www.nhs.uk/conditions/epilepsy/) | |

## Seizure (fit): other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **A seizure that has stopped, with full recovery and nothing that needs an ambulance: get checked today**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Epilepsy](https://www.nhs.uk/conditions/epilepsy/)
- **Note:** The Epilepsy page says an urgent GP appointment or 111 if you think you may have had a first seizure and did not go to hospital. Using it for every seizure that does not need an ambulance is AI judgement. A floor, with the exception below for someone with epilepsy having one of their usual seizures.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| First ever seizure | Is this the first time you have ever had a seizure (fit)? |  | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| Seizure lasting more than 5 minutes, or longer than usual | Did the seizure last more than 5 minutes, or longer than is usual for the person? |  | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| Not woken up fully, or another seizure without waking in between | Is the person still not fully awake after the seizure? Or have they had another seizure without waking up in between? |  | [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/) | |
| Seriously hurt when they passed out, fell or had a seizure | Were you seriously hurt when you passed out, fell or had a seizure? |  | [Fainting](https://www.nhs.uk/symptoms/fainting/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| More than one seizure in 24 hours | Has the person had more than one seizure in the last 24 hours? |  | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| Stiffness or jerking on only one side of the body | During the seizure, was the stiffness or jerking only on one side of the body? |  | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| Much sleepier than usual for more than 1 hour after the seizure | Has the person been much sleepier than usual for more than 1 hour since the seizure stopped? |  | [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Head injury in the last 3 months | Have you hit your head, or had a head injury, in the last 3 months? For example, from a fall or accident. |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Diagnosed with epilepsy | Has a doctor told you that you have epilepsy? |  | [Epilepsy](https://www.nhs.uk/conditions/epilepsy/) | |
| A seizure after a long time without any | Is this the first seizure the person has had after a long time without any? |  | [Epilepsy](https://www.nhs.uk/conditions/epilepsy/) | |

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

### `advice_seizure_999`

**What to do:** Call 999 and ask for an ambulance.

**Look out for:**
- The seizure lasting more than 5 minutes
- Another seizure without waking up in between
- Difficulty breathing

**Get more help when:**
- Call 999 again if things get worse before help arrives

**Where to go:** Call 999. The person you speak to will tell you what to do.

**What you can do yourself:**
- Only move them if they are in danger. Cushion their head.
- Do not put anything in their mouth, including your fingers
- When the jerking stops, turn them on their side. Stay with them and talk calmly.
- Note the time the seizure starts and stops

Source: [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/), [Epilepsy](https://www.nhs.uk/conditions/epilepsy/)

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

### `advice_seizure_ae`

**What to do:** Call 999 or go to A&E now. A seizure like this needs to be checked in hospital today.

**Look out for:**
- Another seizure
- Difficulty breathing
- Not waking up fully

**Get more help when:**
- Do not take the person to A&E if they are still having a seizure or are not fully awake. Call 999 instead.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines they take.

**What you can do yourself:**
- Put the person on their side and stay with them
- Do not give them food or drink until they have fully recovered

Source: [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/), [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/)

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

### `advice_low_blood_sugar_emergency`

**What to do:** If the person is awake and can swallow safely, give them something sugary now, such as fruit juice or a sugary fizzy drink. Call 999 if they do not get better quickly, or stop responding as usual.

**Look out for:**
- Not responding, or very drowsy
- A seizure (fit)

**Get more help when:**
- If they are not fully awake, do not give food or drink. Put them on their side and call 999.
- Give a glucagon injection if one is available and you know how to use it

**Where to go:** Call 999 or go to A&E. Stay with the person until they have fully recovered or help arrives.

Source: [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/), [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/)

### `advice_seizure_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Anyone who has had a seizure needs to be checked to find out what caused it.

**Look out for:**
- Another seizure
- A seizure that lasts more than 5 minutes
- Not waking up fully, or difficulty breathing

**Get more help when:**
- Call 999 if there is another seizure, or any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5. In an emergency call 999.

**What you can do yourself:**
- Write down what happened before, during and after the seizure, and how long it lasted. A video can help the doctor.
- Do not drive until a doctor says it is safe
- For a child with a high temperature, do not try to cool them by undressing them or sponging them with cold water

Source: [Epilepsy](https://www.nhs.uk/conditions/epilepsy/), [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/), [Fits (seizures)](https://www.nhs.uk/symptoms/what-to-do-if-someone-has-a-seizure-fit/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sz_first`: The Epilepsy page says the same. The Febrile seizures page says call 999 or go to A&E for a child's first febrile seizure. The more urgent is used.
- `rf_sz_more_than_one`: Source difference: the Febrile seizures page says call 999 or go to A&E for more than 1 seizure in 24 hours. The Epilepsy page says call 999 for 3 or more in 24 hours. The Febrile seizures threshold is used for everyone, which is AI judgement for adults.
- `rf_sz_head_injury`: The Head injury page says call 999 for a fit after a recent head injury; that entry symptom applies too when the injury was in the last month. The Headaches page says 999 or A&E for a headache after a head injury in the last 3 months.
- `rf_sz_low_sugar`: The Low blood sugar page lists a seizure as a sign of severe low blood sugar, and says call 999 if someone is not responding normally and glucagon is not available or has not worked.
- `rf_sz_high_temperature`: The Febrile seizures page says it is important to get medical help if a child has a seizure. A first febrile seizure is sent to 999 by the rule above. The encephalitis and meningitis condition cards can raise this for an adult.
- `seizure default outcome`: The Epilepsy page says an urgent GP appointment or 111 if you think you may have had a first seizure and did not go to hospital. Using it for every seizure that does not need an ambulance is AI judgement. A floor, with the exception below for someone with epilepsy having one of their usual seizures.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Brain tumour warning signs | 126952004 | rare | Headache getting worse over days or weeks: strongly supports; Headache wakes them at night, or is worst on waking: supports; Changes in personality or behaviour: supports; Being sick: supports; Has had a seizure (fit): supports; Weakness that started gradually or is slowly getting worse: supports; Headache feels different from usual headaches: supports; Change in sight or loss of vision: supports |
| Encephalitis (swelling of the brain) | 45170000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Suddenly confused: strongly supports; Changes in personality or behaviour: supports; Has had a seizure (fit): supports; Difficulty speaking: supports; So drowsy they are hard to wake or cannot stay awake: supports; Headache: supports; Weakness, or cannot move part of the body (paralysis): supports |
| Epilepsy (a condition that causes repeated seizures) | 84757009 | common | Bit their tongue or wet themselves during the seizure: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Suddenly confused: supports; More than one seizure in 24 hours: supports; Fainted with no warning at all: supports |
| Seizure caused by a high temperature in a young child (febrile seizure) | 41497008 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Blocked or runny nose: supports; Cough: supports |
| Low blood sugar (hypoglycaemia, a hypo) | 302866003 | rare | Has diabetes: strongly supports; Signs of low blood sugar in someone with diabetes: strongly supports; Feels sweaty: supports; Shaking or trembling (tremor): supports; Feels light-headed: supports; Suddenly confused: supports; Tingling or pins and needles in the fingers or around the mouth: supports; Heart racing, slow, skipping or fluttering: supports |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| Bleeding on the brain (subarachnoid haemorrhage) | 21454007 | rare | Headache that came on suddenly and is extremely painful: strongly supports; Headache: strongly supports; Stiff neck: supports; Being sick: supports; Bright lights hurt the eyes or are bothering you: supports; So drowsy they are hard to wake or cannot stay awake: supports; Passed out (fainted): supports; Has had a seizure (fit): supports; Suddenly confused: supports |
| Common faint (vasovagal syncope) | 398665005 | very common | Fainted after standing a long time, heat, a shock, pain or the sight of blood: strongly supports; Felt dizzy, sweaty, hot or sick just before fainting: strongly supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feels light-headed: supports |
| Alcohol withdrawal (symptoms after stopping or cutting down drinking) | 191480000 | rare | Stopped or cut down alcohol, or a drug or medicine they rely on, in the last few days: strongly supports; Withdrawal symptoms: shaking, sweating, anxiety, feeling sick or poor sleep: strongly supports; Drinks a lot of alcohol: strongly supports; Severe withdrawal: shaking that others can see, very restless or upset, confused, or seeing or hearing things: supports; Feels sweaty: supports; Feels sick or has been sick: supports; Feeling anxious, worried or panicky: supports; Hearing, seeing or feeling things that other people do not: supports; Shaking or trembling (tremor): supports; Has had a seizure (fit): supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
