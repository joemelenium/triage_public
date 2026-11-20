# Review pack: Baby not feeding or unsettled

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
| [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | 2026-11-19 |  | Page last reviewed: 6 August 2026 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | 2026-11-19 |  | Page last reviewed: 03 January 2024 |
| [Dehydration](https://www.nhs.uk/conditions/dehydration/) | 2026-11-19 |  | Page last reviewed: 01 May 2026 |
| [Colic](https://www.nhs.uk/conditions/colic/) | 2026-11-19 |  | Page last reviewed: 26 April 2022 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | 2026-11-19 |  | Page last reviewed: 10 June 2025 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/) | 2026-11-19 |  | Page last reviewed: 21 June 2023 |

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

## Baby not feeding or unsettled red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to your baby right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bb_floppy_or_not_responding`<br>A baby who is floppy, hard to wake, or not responding as usual | "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_cry`<br>A baby with a weak, high-pitched or continuous cry, or a cry that does not sound like their usual cry<br>**Note:** The Colic page also says go to A&E or call 999 for a weak or high-pitched cry, or one that does not sound like their usual cry. | "Child extremely agitated, crying and will not stop, or a weak or high-pitched cry" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_not_feeding_at_all`<br>A baby who has stopped feeding, or is not interested in anything around them | "Child not interested in feeding or anything around them" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_bb_breathing`<br>A baby struggling to breathe, grunting, or breathing very fast | "Difficulty breathing" OR "Breathing very fast" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_skin_or_rash`<br>A baby with blotchy skin, cold or clammy skin, or a rash that does not fade when pressed | "Blotchy or mottled skin" OR "Hands and feet, or skin, unusually cold to touch" OR "Rash that does not fade when pressed" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_fit`<br>A baby who is having or has had a fit (seizure)<br>**Note:** The page says call 999 or go to A&E. An ambulance is used because the Febrile seizures page says not to take a child to A&E while they are still having a fit. | "Has had a seizure (fit)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_high_temperature`<br>A baby under 3 months with 38C or more, or 3 to 6 months with 39C or more | "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_not_peed`<br>A baby who has not had a pee (a wet nappy) for 12 hours | "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| `rf_bb_green_sick_or_blood_in_poo`<br>A baby being sick green, or with blood in their poo: possible blocked or twisted bowel<br>**Note:** Clinical knowledge: green sick (bile) or blood in the poo of a baby who is unsettled can be a blocked or twisted bowel, which needs surgery. The stomach and bowel body system owns those pages. | "Baby being sick green, or blood in their poo" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_bb_bulging_soft_spot`<br>A baby with a bulging soft spot on top of the head<br>**Note:** Clinical knowledge: a bulging soft spot in an unwell baby can be a sign of meningitis. | "Baby's soft spot on top of the head bulging" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Baby not feeding or unsettled red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to your baby? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bb_feeding_much_less`<br>A baby feeding much less than usual<br>**Note:** The Bronchiolitis page says an urgent GP appointment or 111 for a baby feeding much less than usual. Applying it to every baby who is not feeding is AI judgement. | "Baby or young child feeding or eating much less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 or ask for an urgent GP appointment* | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| `rf_bb_high_temperature_any`<br>A baby with a high temperature, or thought to have one<br>**Note:** The Fever in children page says call 111 for a baby under 6 months who has, or seems to have, a high temperature. Applying it to every baby under 1 who is also unsettled or not feeding is AI judgement. The high temperature rules also apply. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 now* | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| `rf_bb_keeps_being_sick`<br>A baby who keeps being sick and cannot keep feeds down<br>**Note:** Clinical knowledge: a baby who keeps being sick can quickly lack water in the body. Forceful sick after every feed in the first weeks can also be a narrowing at the stomach outlet. | "Keeps being sick and cannot keep fluids down" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 or ask for an urgent GP appointment* | **AI judgement, needs clinical review** | |
| `rf_bb_dehydration`<br>A baby with dry nappies, sunken eyes, no tears or a sunken soft spot | "Child with dry nappies, sunken eyes or no tears" OR "Baby's soft spot on top of the head sinks inwards" | Urgent (help today)<br>Urgent care<br>Today<br>*Call 111 or ask for an urgent GP appointment* | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |

## Baby not feeding or unsettled: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bb_not_gaining_weight`<br>A baby who is not putting on weight as expected | "Baby not gaining weight, or losing weight" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP or call 111. The source gives no fixed time.* | [Colic](https://www.nhs.uk/conditions/colic/) | |

## Default outcome

Used when no rule fires.

- **A baby who is unsettled or not feeding well, with no sign of serious illness: see a GP or health visitor if you are worried**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP or call 111 if you are worried. The source gives no fixed time.*
- Source: [Colic](https://www.nhs.uk/conditions/colic/)
- **Note:** The Colic page says call 111 or see a GP (non-urgent) if you are worried about your baby's crying. Soft: likely colic lowers it to self-care with advice.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Baby not feeding well, or unsettled | Is your baby not feeding well, or more unsettled or crying more than usual? |  | [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Child extremely agitated, crying and will not stop, or a weak or high-pitched cry | Is the child extremely agitated or crying and will not stop? Or do they have a weak, high-pitched cry that does not sound like their usual cry? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Child not interested in feeding or anything around them | Has the child stopped feeding? Or have they lost all interest in what is going on around them? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Hands and feet, or skin, unusually cold to touch | Are your hands and feet, or your skin, unusually cold to touch, or cold and damp (clammy)? |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Rash that does not fade when pressed | Do you have a rash that does not fade when you press a glass against it? | 400991008 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Baby being sick green, or blood in their poo | Is your baby being sick green (bright green or dark green), or is there blood in their poo? |  | **AI judgement, needs clinical review** | |
| Baby's soft spot on top of the head bulging | Is the soft spot on top of your baby's head (fontanelle) bulging or tight? |  | **AI judgement, needs clinical review** | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Child with dry nappies, sunken eyes or no tears | Does the child have signs of not having enough water in their body? For example, dry nappies, sunken eyes, or no tears when crying. |  | [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/) | |
| Baby's soft spot on top of the head sinks inwards | Has the soft spot on top of your baby's head (fontanelle) sunk inwards? | 8381001 | [Dehydration](https://www.nhs.uk/conditions/dehydration/) | |
| Baby not gaining weight, or losing weight | Is your baby not gaining weight, or losing weight? | 36440009 | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |

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

### `advice_baby_emergency`

**What to do:** Call 999 or go to A&E now. Your baby has a sign of serious illness and needs to be checked in hospital straight away.

**Look out for:**
- Your baby becoming floppy, very sleepy or hard to wake
- Breathing that gets harder, with grunting or the tummy sucking in
- Skin, lips or tongue turning blue, grey, pale or blotchy
- A fit (seizure)
- Green sick, or no wet nappy

**Get more help when:**
- Call 999 if your baby gets worse or you cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Ask someone to drive you so you can watch your baby, or call 999. Bring your baby's red book if you have it.

Source: [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/), [Sepsis](https://www.nhs.uk/conditions/sepsis/), [Colic](https://www.nhs.uk/conditions/colic/), [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/)

### `advice_febrile_fit_999`

**What to do:** Call 999 now. Your child has had a fit (seizure) with a high temperature.

**Look out for:**
- A fit that lasts more than 5 minutes
- Difficulty breathing
- Stiffness or twitching on only one side of the body
- Being much sleepier than usual for more than an hour after the fit stops

**Get more help when:**
- Call 999 again if your child has another fit, or gets worse before help arrives

**Where to go:** Call 999. Do not take your child to A&E yourself while they are still having a fit or are not responding.

**What you can do yourself:**
- Put your child on their side on a soft surface, away from anything that could hurt them
- Do not put anything in their mouth
- Stay with them and note how long the fit lasts

Source: [Febrile seizures](https://www.nhs.uk/conditions/febrile-seizures/), [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/)

### `advice_fever_baby_emergency`

**What to do:** Call 999 or go to A&E now. A baby this young with a high temperature needs to be checked in hospital straight away, even if they seem otherwise well.

**Look out for:**
- Your baby becoming floppy, very sleepy or hard to wake
- A weak, high-pitched or continuous cry
- Not feeding, or a dry nappy for 12 hours
- Skin, lips or tongue turning blue, grey, pale or blotchy, or a rash that does not fade when you press a glass on it

**Get more help when:**
- Call 999 if your baby gets worse or you cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive yourself if you need to watch your baby. Ask someone to drive you or call 999.

**What you can do yourself:**
- Keep breastfeeding or giving feeds if your baby will take them
- Do not give medicine for the temperature unless a doctor says so

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [Fever in children](https://www.nhs.uk/symptoms/fever-in-children/), [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/)

### `advice_baby_urgent`

**What to do:** Call 111 now, or ask for an urgent GP appointment. Your baby needs to be checked today.

**Look out for:**
- A weak, high-pitched cry, or a cry that does not sound like their usual cry
- Being floppy, very sleepy or hard to wake
- Breathing very fast, or grunting
- A dry nappy for 12 hours
- Being sick green, or blood in their poo

**Get more help when:**
- Call 999 or go to A&E if your baby gets any of the signs above
- Trust your instincts. If you think something is seriously wrong, call 999.

**Where to go:** Call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep offering feeds little and often. Keep breastfeeding, or give formula as usual. Do not make formula weaker.

Source: [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/), [Dehydration](https://www.nhs.uk/conditions/dehydration/), [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/)

### `advice_baby_gp`

**What to do:** Your answers do not show signs of serious illness. See a GP or your health visitor if you are worried about your baby's crying or feeding, or they are not putting on weight.

**Look out for:**
- A weak, high-pitched cry, or a cry that does not sound like their usual cry
- Feeding much less than usual, or fewer wet nappies
- A high temperature
- Being sick green, or blood in their poo

**Get more help when:**
- Call 111 if your baby is feeding much less, has a high temperature, or you are worried
- Call 999 or go to A&E if your baby is floppy, hard to wake, or has a weak or high-pitched cry
- If you are finding it hard to cope, talk to your health visitor or GP, or call 111

**Where to go:** Make an appointment with a GP, or talk to your health visitor. For urgent help call 111. In an emergency call 999.

**What you can do yourself:**
- Hold or cuddle your baby when they are crying, and try gently rocking them or a warm bath
- Hold your baby upright during feeds, and wind them after feeds
- If you feel you cannot cope, put your baby somewhere safe, such as their cot, and take a few minutes for yourself

Source: [Colic](https://www.nhs.uk/conditions/colic/), [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bb_cry`: The Colic page also says go to A&E or call 999 for a weak or high-pitched cry, or one that does not sound like their usual cry.
- `rf_bb_fit`: The page says call 999 or go to A&E. An ambulance is used because the Febrile seizures page says not to take a child to A&E while they are still having a fit.
- `rf_bb_green_sick_or_blood_in_poo`: Clinical knowledge: green sick (bile) or blood in the poo of a baby who is unsettled can be a blocked or twisted bowel, which needs surgery. The stomach and bowel body system owns those pages.
- `rf_bb_bulging_soft_spot`: Clinical knowledge: a bulging soft spot in an unwell baby can be a sign of meningitis.
- `rf_bb_feeding_much_less`: The Bronchiolitis page says an urgent GP appointment or 111 for a baby feeding much less than usual. Applying it to every baby who is not feeding is AI judgement.
- `rf_bb_high_temperature_any`: The Fever in children page says call 111 for a baby under 6 months who has, or seems to have, a high temperature. Applying it to every baby under 1 who is also unsettled or not feeding is AI judgement. The high temperature rules also apply.
- `rf_bb_keeps_being_sick`: Clinical knowledge: a baby who keeps being sick can quickly lack water in the body. Forceful sick after every feed in the first weeks can also be a narrowing at the stomach outlet.
- `baby_unsettled default outcome`: The Colic page says call 111 or see a GP (non-urgent) if you are worried about your baby's crying. Soft: likely colic lowers it to self-care with advice.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Meningitis (an infection of the layers around the brain) | 7180009 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Stiff neck: strongly supports; Headache: strongly supports; Rash that does not fade when pressed: strongly supports; Bright lights hurt the eyes or are bothering you: strongly supports; So drowsy they are hard to wake or cannot stay awake: supports; Being sick: supports; Very painful headache: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Feels sick or has been sick: supports; Hands and feet, or skin, unusually cold to touch: supports; Has had a seizure (fit): supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Baby's soft spot on top of the head bulging: supports; Feels very unwell: strongly supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Blotchy or mottled skin: supports |
| Bronchiolitis (a chest infection that babies get) | 4120002 | rare | Blocked or runny nose: strongly supports; Cough: supports; Wheezing: supports; Breathing very fast: supports; Baby or young child feeding or eating much less than usual: supports; Very high temperature, or feels hot, cold or shivery: supports |
| Sepsis (a life-threatening reaction to an infection) | 91302008 | rare | Seems very unwell and getting worse, or feels something is seriously wrong: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Breathing very fast: supports; Feels cold to the touch, or shivery: supports; Blotchy or mottled skin: supports; Suddenly confused: supports; No pee for 12 hours or more: supports; So drowsy they are hard to wake or cannot stay awake: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not interested in feeding or anything around them: supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Hands and feet, or skin, unusually cold to touch: supports; Rash that does not fade when pressed: supports; Very low temperature (below 36C): supports |
| Serious infection in a young baby (such as a blood, kidney or brain infection) |  | very rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Baby or young child feeding or eating much less than usual: strongly supports; Child extremely agitated, crying and will not stop, or a weak or high-pitched cry: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Child not their usual self, or not wanting to eat, and the carer is worried: supports; Blotchy or mottled skin: supports |
| Serious dehydration (not having enough water in the body) |  | uncommon | Keeps being sick and cannot keep fluids down: strongly supports; Dizzy when standing up, and it does not go away: strongly supports; No pee for 12 hours or more: strongly supports; Heart beating very fast: supports; Child with dry nappies, sunken eyes or no tears: supports; Baby's soft spot on top of the head sinks inwards: supports; Diarrhoea, or being sick: supports; Feels very tired: supports; Child limp, floppy, hard to wake or not responding as usual: supports |
| Viral infection (such as a cold, a tummy bug or another virus) | 34014006 | common | Blocked or runny nose: strongly supports; Aching body: supports; Cough: supports; Diarrhoea, or being sick: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports |
| Colic (a baby crying a lot for no clear reason) | 35363006 | very rare | Baby crying a lot and hard to settle: strongly supports; Baby will not stop crying and is very distressed: supports; Baby cries a lot, often in the evening, but feeds and grows well: strongly supports |
| Urine infection (urinary tract infection, UTI) | 68566005 | uncommon | Pain, burning or stinging when peeing: strongly supports; Peeing more often than usual: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels sick or has been sick: supports; Suddenly confused: supports; Pain low down in the tummy, below the belly button: supports; Blood in pee: supports; Cloudy pee: supports; Smelly pee: supports; Also wets during the day: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
