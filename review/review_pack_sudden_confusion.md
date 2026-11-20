# Review pack: Sudden confusion

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
| [Meningitis](https://www.nhs.uk/conditions/meningitis/) | 2026-11-19 |  | Page last reviewed: 12 June 2026 |
| [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | 2026-11-19 |  | Page last reviewed: 29 May 2025 |
| [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | 2026-11-19 |  | Page last reviewed: 16 December 2025 |
| [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | 2026-11-19 |  | Page last reviewed: 03 August 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Headaches](https://www.nhs.uk/symptoms/headaches/) | 2026-11-19 |  | Page last reviewed: 17 April 2024 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
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

## Sudden confusion red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_cf_stroke`<br>Sudden confusion with numbness or weakness, or difficulty speaking: possible stroke | "Numbness or weakness in the face, arms or legs" OR "Difficulty speaking" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| `rf_cf_headache_sudden`<br>Sudden confusion with a headache that came on suddenly and is extremely painful | "Headache that came on suddenly and is extremely painful" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| `rf_cf_rash`<br>Sudden confusion with a rash that does not fade when pressed: possible meningitis or sepsis<br>**Note:** The Meningitis and Sepsis pages say call 999 or go to A&E for each sign. Sending an ambulance when both are present, rather than going to A&E, is AI judgement: the person may get worse quickly and should not travel without help. | "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_cf_stiff_neck`<br>Sudden confusion with a stiff neck: possible meningitis | "Stiff neck" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Meningitis](https://www.nhs.uk/conditions/meningitis/) | |
| `rf_cf_drowsy`<br>Sudden confusion and very drowsy or hard to keep awake<br>**Note:** Clinical knowledge: confusion with drowsiness means the brain is not working normally and the person may stop responding. The Head injury page says call 999 for someone who cannot stay awake. | "So drowsy they are hard to wake or cannot stay awake" OR "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_cf_head_injury`<br>Sudden confusion after a head injury in the last 3 months<br>**Note:** The Head injury page says call 999 for problems with understanding after a head injury. Applying it to a head injury in the last 3 months, not only a recent one, is AI judgement: bleeding can build up slowly, especially in older people. | "Head injury in the last 3 months" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/) | |
| `rf_cf_others_unwell`<br>Sudden confusion, and others at home or pets unwell too: possible carbon monoxide poisoning | "Others at home, or pets, unwell with similar symptoms" | Emergency (help now)<br>Emergency department<br>Now<br>*Get into fresh air, then call 999 or go to A&E* | [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/) | |
| `rf_cf_low_sugar`<br>Sudden confusion in someone with diabetes who has signs of low blood sugar<br>**Note:** The Low blood sugar page says call 999 if someone with a very low blood sugar is not responding normally and a glucagon injection is not available or has not worked. | "Has diabetes" AND "Signs of low blood sugar in someone with diabetes" | Emergency (help now)<br>Emergency department<br>Now<br>*Give something sugary if they can swallow safely. Call 999 if they do not get better quickly or stop responding normally.* | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

## Sudden confusion: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Sudden confusion: get medical help immediately**
- Outcome: Emergency (help now), Emergency department, Now. *Go to A&E or call 999*
- Source: [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numbness or weakness in the face, arms or legs | Do you have numbness or weakness in your face, arms or legs? |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Difficulty speaking | Are you finding it hard to speak? | 286378009 | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Headache that came on suddenly and is extremely painful | Did the headache come on suddenly, and is it extremely painful? For example, the worst headache you have ever had, at its worst within a few minutes. | 95660002 | [Subarachnoid haemorrhage](https://www.nhs.uk/conditions/subarachnoid-haemorrhage/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Stiff neck | Do you have a stiff neck, so it is hard or painful to bend your head forward towards your chest? | 161882006 | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Head injury in the last 3 months | Have you hit your head, or had a head injury, in the last 3 months? For example, from a fall or accident. |  | [Headaches](https://www.nhs.uk/symptoms/headaches/) | |
| Others at home, or pets, unwell with similar symptoms | Are other people you live with, or your pets, unwell with similar symptoms? |  | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Has diabetes | Do you have diabetes? | 73211009 | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Signs of low blood sugar in someone with diabetes | Is your blood sugar below 4, or do you feel shaky, sweaty, hungry or muddled, like when your sugar is low? |  | [Low blood sugar (hypoglycaemia)](https://www.nhs.uk/conditions/low-blood-sugar-hypoglycaemia/) | |

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

### `advice_confusion_999`

**What to do:** Call 999 now. Sudden confusion with these signs needs treatment in hospital straight away.

**Look out for:**
- The person stops responding, or their breathing changes
- A seizure (fit)

**Get more help when:**
- If they stop responding and are not breathing properly, start CPR: press hard and fast in the middle of their chest. The 999 call handler will tell you how.

**Where to go:** Call 999. Do not drive them to A&E yourself. Stay with the person until help arrives.

**What you can do yourself:**
- Stay with the person. Tell them who you are and where they are, and keep reassuring them.
- Make a note of any medicines they take

Source: [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/), [Head injury and concussion](https://www.nhs.uk/conditions/head-injury-and-concussion/)

### `advice_carbon_monoxide_emergency`

**What to do:** Get everyone outside into fresh air, then call 999 or go to A&E now. This could be carbon monoxide poisoning, from a poisonous gas you cannot see or smell.

**Look out for:**
- Anyone passing out or finding it hard to breathe
- Others in the home becoming confused or very sleepy

**Get more help when:**
- Call 999 if anyone gets worse or cannot get to A&E safely
- If you think an appliance is leaking gas, call the free National Gas Helpline on 0800 111 999

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Do not go back into the building until you have got advice.

Source: [Carbon monoxide poisoning](https://www.nhs.uk/conditions/carbon-monoxide-poisoning/), [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/)

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

### `advice_confusion_ae`

**What to do:** Go to A&E or call 999 now. Many causes of sudden confusion need to be checked and treated as soon as possible.

**Look out for:**
- Signs of a stroke: one side of the face drooping, weakness in an arm, or slurred speech
- Very drowsy or hard to wake
- A seizure (fit)

**Get more help when:**
- Call 999 if the person gets worse or you cannot get them to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines they take.

**What you can do yourself:**
- Stay with the person. Tell them who you are and where they are, and keep reassuring them.
- Use simple words and short sentences. Do not ask lots of questions.
- Do not stop them moving around, unless they are in danger

Source: [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_cf_rash`: The Meningitis and Sepsis pages say call 999 or go to A&E for each sign. Sending an ambulance when both are present, rather than going to A&E, is AI judgement: the person may get worse quickly and should not travel without help.
- `rf_cf_drowsy`: Clinical knowledge: confusion with drowsiness means the brain is not working normally and the person may stop responding. The Head injury page says call 999 for someone who cannot stay awake.
- `rf_cf_head_injury`: The Head injury page says call 999 for problems with understanding after a head injury. Applying it to a head injury in the last 3 months, not only a recent one, is AI judgement: bleeding can build up slowly, especially in older people.
- `rf_cf_low_sugar`: The Low blood sugar page says call 999 if someone with a very low blood sugar is not responding normally and a glucagon injection is not available or has not worked.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Poisoning by carbon monoxide, a gas from a faulty boiler, fire or car | 17383000 | rare | Others at home, or pets, unwell with similar symptoms: strongly supports; Better when away from home, worse on returning: strongly supports; Headache: strongly supports; Dizzy or off-balance: supports; Feels sick or has been sick: supports |
| Sudden confusion from an illness, such as an infection | 2776000 | common | Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Started a new medicine or changed a dose in the last few weeks: supports; Signs of dehydration: supports; So drowsy they are hard to wake or cannot stay awake: supports; Cough: supports; Suddenly confused: strongly supports; Came on suddenly, over hours or a few days: strongly supports; Recent infection, or started a new medicine: supports |
| Encephalitis (swelling of the brain) | 45170000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Suddenly confused: strongly supports; Changes in personality or behaviour: supports; Has had a seizure (fit): supports; Difficulty speaking: supports; So drowsy they are hard to wake or cannot stay awake: supports; Headache: supports; Weakness, or cannot move part of the body (paralysis): supports |
| Low blood sugar (hypoglycaemia, a hypo) | 302866003 | rare | Has diabetes: strongly supports; Signs of low blood sugar in someone with diabetes: strongly supports; Feels sweaty: supports; Shaking or trembling (tremor): supports; Feels light-headed: supports; Suddenly confused: supports; Tingling or pins and needles in the fingers or around the mouth: supports; Heart racing, slow, skipping or fluttering: supports |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| Stroke | 230690007 | rare | Signs of a stroke: strongly supports; Weakness that came on suddenly: strongly supports; Weakness on one side of the face or body: strongly supports; Weakness, or cannot move part of the body (paralysis): strongly supports; Difficulty speaking: supports; Numbness or tingling that came on suddenly on one side of the body: supports; Numbness in the face that came on suddenly: supports; Change in sight or loss of vision: supports; Finding it hard to balance or walk: supports; Suddenly confused: supports |
| Bleeding on the brain (subarachnoid haemorrhage) | 21454007 | rare | Headache that came on suddenly and is extremely painful: strongly supports; Headache: strongly supports; Stiff neck: supports; Being sick: supports; Bright lights hurt the eyes or are bothering you: supports; So drowsy they are hard to wake or cannot stay awake: supports; Passed out (fainted): supports; Has had a seizure (fit): supports; Suddenly confused: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Side effect of a medicine | 62014003 | uncommon | Started a new medicine or changed a dose in the last few weeks: strongly supports; Dizzy when standing or sitting up quickly: supports; So drowsy they are hard to wake or cannot stay awake: supports; Feels light-headed: supports; Takes a medicine that can cause constipation: supports; Taking antibiotics now, or took them recently: supports; Feeling sick (nausea): supports; Diarrhoea: supports; Takes antidepressants or blood pressure medicine: supports; Uses hormonal contraception: supports; Used erection medicine, a penis injection, cannabis or cocaine: supports; Recently had food, drink or medicine that can change pee: supports; Has cancer, or is having treatment for cancer: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
