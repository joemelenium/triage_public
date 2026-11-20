# Review pack: Worms in humans

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
| [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | 2026-11-19 |  | Page last reviewed: 20 November 2023 |
| [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | 2026-11-19 |  | Page last reviewed: 03 October 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Threadworms](https://www.nhs.uk/conditions/threadworms/) | 2026-11-19 |  | Page last reviewed: 01 December 2023 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
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

## Worms in humans: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_worms_other_types`<br>A large worm, a piece of worm or eggs, a worm-shaped rash, sickness, diarrhoea or stomach ache for more than 2 weeks, or weight loss: possible roundworm, hookworm or tapeworm | "A large worm, a piece of worm or worm eggs" OR "Red, itchy, worm-shaped rash on the skin" OR "Being sick, diarrhoea or stomach ache for more than 2 weeks" OR "Losing weight without trying" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. Tell them if you have been abroad in the last 2 years.* | [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | |
| `or_worms_threadworms_young_or_pregnant`<br>Possible threadworms in a child under 2, or in someone pregnant or breastfeeding | ("Tiny white worms like pieces of thread" OR "Itchy bottom worse at night") AND ("Under 2 years old" OR "Pregnant, or gave birth in the last 6 weeks") | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, midwife or health visitor. The source gives no fixed time.* | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |

## Default outcome

Used when no rule fires.

- **Small white worms like thread, or itching around the bottom: probably threadworms, which a pharmacist can treat**
- Outcome: Routine (help needed, timing not critical), Community pharmacy, No fixed time given in the source. *See a pharmacist. The source gives no fixed time.*
- Source: [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/)
- **Note:** Threadworms are by far the commonest worms in the UK, so a pharmacist is the default. Other worms go to a GP by the rule above.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Has seen worms, or thinks they have worms | Have you seen worms in your poo or around your bottom, or do you think you have worms? |  | [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| A large worm, a piece of worm or worm eggs | Have you found a large worm, a piece of a worm, or worm eggs in your poo? |  | [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | |
| Red, itchy, worm-shaped rash on the skin | Do you have a red, itchy rash on your skin that is shaped like a worm? |  | [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | |
| Being sick, diarrhoea or stomach ache for more than 2 weeks | Have you been sick, had diarrhoea or had a stomach ache for more than 2 weeks? |  | [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Tiny white worms like pieces of thread | Are the worms tiny, white and like pieces of thread? They may be seen in poo or around the bottom, often at night. |  | [Threadworms](https://www.nhs.uk/conditions/threadworms/) | |
| Itchy bottom worse at night | Is the itching worse at night? |  | [Threadworms](https://www.nhs.uk/conditions/threadworms/) | |
| Under 2 years old | Is the person who is unwell under 2 years old? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |

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

### `advice_worms_gp`

**What to do:** See a GP. They will check what type of worm it is and prescribe medicine to kill the worms. Tell them if you have been abroad in the last 2 years.

**Look out for:**
- Symptoms that do not get better 2 weeks after treatment
- Still passing live worms in your poo

**Get more help when:**
- Go back to the GP if your symptoms do not get better in 2 weeks

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Wash your hands after the toilet and before eating or preparing food
- The people you live with may also need to be treated

Source: [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/)

### `advice_worms_pharmacy`

**What to do:** See a pharmacist. Small white worms like pieces of thread, or itching around the bottom at night, are probably threadworms. They are common and a pharmacist can treat them.

**Look out for:**
- A large worm, a piece of worm, or worm eggs in your poo
- A red, itchy rash shaped like a worm
- Being sick, diarrhoea or a stomach ache for more than 2 weeks, or losing weight

**Get more help when:**
- See a GP if you get any of the signs above, or symptoms are not better after 2 weeks of treatment
- A child under 2 should see a GP or health visitor, not a pharmacist. So should you if you are pregnant or breastfeeding.

**Where to go:** Go to a pharmacy. You do not need an appointment. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Everyone you live with may need treatment too
- Wash your hands after the toilet and before eating or preparing food
- Wash bedding and towels on a hot wash

Source: [Hookworm](https://www.nhs.uk/symptoms/worms-in-humans/), [Threadworms](https://www.nhs.uk/conditions/threadworms/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `worms default outcome`: Threadworms are by far the commonest worms in the UK, so a pharmacist is the default. Other worms go to a GP by the rule above.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Other worm infections, such as roundworm, tapeworm or hookworm | 27601005 | uncommon | A large worm, a piece of worm or worm eggs: strongly supports; Has been abroad in the last 2 years: strongly supports; Red, itchy, worm-shaped rash on the skin: supports; Being sick, diarrhoea or stomach ache for more than 2 weeks: supports; Losing weight without trying: supports |
| Threadworms | 266162007 | common | Tiny white worms like pieces of thread: strongly supports; Itchy bottom worse at night: strongly supports; Others nearby have the same symptoms: supports; Itchy bottom: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
