# Review pack: Tailbone (coccyx) pain

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
| [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | 2026-11-19 |  | Page last reviewed: 6 June 2025 |
| [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sciatica](https://www.nhs.uk/conditions/sciatica/) | 2026-11-19 |  | Page last reviewed: 03 December 2024 |
| [Slipped disc](https://www.nhs.uk/conditions/slipped-disc/) | 2026-11-19 |  | Page last reviewed: 24 April 2024 |

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

## Tailbone (coccyx) pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tail_cauda_equina`<br>Tailbone pain with numbness around the genitals or bottom, new problems peeing or pooing, or symptoms in both legs<br>**Note:** The Back pain page gives these as emergency signs. Applying them to tailbone pain is AI judgement: the nerves at the bottom of the spine run close by. | "Numb or no feeling around the genitals or bottom" OR "New problems peeing or pooing" OR "Pain, tingling, weakness or numbness in both legs" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Tailbone (coccyx) pain red flags: Urgent (help today)

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_tail_abscess`<br>A painful lump near the top of the crease of the bottom, with a high temperature, red skin, pus, or severe pain<br>**Note:** Could be an infected pocket of pus (pilonidal abscess), which may need draining. AI judgement, needs clinical review. | "Painful lump, swelling or hole in the skin near the top of the crease of the bottom" AND ("Very high temperature, or feels hot, cold or shivery" OR "Skin over the painful area has changed colour" OR "Pus or blood leaking from a lump" OR "Severe pain") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | **AI judgement, needs clinical review** | |

## Tailbone (coccyx) pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_tail_gp`<br>Tailbone pain not better after a few weeks, affecting daily activities, or with a high temperature<br>**Note:** The page says see a GP for a high temperature with tailbone pain and pain in another area, such as the tummy or lower back. | "Pain for 2 weeks or more, not getting better" OR "Pain stopping usual activities or affecting sleep" OR "Very high temperature, or feels hot, cold or shivery" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, or refer yourself to a physiotherapist where you can* | [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/) | |
| `or_tail_lump`<br>A lump or small hole in the skin near the top of the crease of the bottom | "Painful lump, swelling or hole in the skin near the top of the crease of the bottom" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP* | **AI judgement, needs clinical review** | |

## Default outcome

Used when no rule fires.

- **Tailbone pain with nothing that needs more help: ease it yourself, it may take a few weeks**
- Outcome: Self-manageable, Self-care, No appointment needed. *Tailbone pain may improve after a few weeks*
- Source: [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Tailbone pain | Do you have pain at the base of your spine, near the top of your bottom (your tailbone)? | 34789001 | [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| New problems peeing or pooing | Have you had new problems peeing or pooing? For example, finding it hard to start peeing, not being able to pee, or peeing or pooing yourself. |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain, tingling, weakness or numbness in both legs | Do you have pain, tingling, weakness or numbness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Painful lump, swelling or hole in the skin near the top of the crease of the bottom | Is there a painful lump, swelling or small hole in the skin near the top of the crease of your bottom? |  | **AI judgement, needs clinical review** | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Skin over the painful area has changed colour | Has the skin over the painful area changed colour, for example gone red or purple? This may be harder to see on brown or black skin. |  | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Pus or blood leaking from a lump | Is pus or blood leaking from the lump? |  | **AI judgement, needs clinical review** | |
| Severe pain | Is the pain severe? Severe pain is there all the time and so bad it is hard to think, talk or sleep. |  | [Thumb pain](https://www.nhs.uk/symptoms/hand-pain/thumb-pain/) | |
| Pain for 2 weeks or more, not getting better | Have you had the pain for 2 weeks or more, and it has not got better with treatment at home? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |
| Pain stopping usual activities or affecting sleep | Is the pain stopping you doing your usual activities, or affecting your sleep? |  | [Joint pain](https://www.nhs.uk/symptoms/joint-pain/) | |

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

### `advice_tailbone_lump_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A painful, red lump near the top of your bottom can be an abscess (a pocket of pus) that may need draining.

**Look out for:**
- Redness or swelling spreading
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if you feel very unwell or confused

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Keep the area clean and dry
- Do not squeeze the lump

Source: **AI judgement, needs clinical review**, [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/)

### `advice_tailbone_gp`

**What to do:** See a GP. In many areas you can also refer yourself to a physiotherapist without seeing a GP first.

**Look out for:**
- Numbness around your genitals or bottom
- Problems peeing or pooing
- A painful, red lump near the top of your bottom

**Get more help when:**
- Call 999 or go to A&E if you get numbness around your genitals or bottom, or problems peeing or pooing

**Where to go:** Contact your GP surgery, or look for an NHS service for back and joint problems you can refer yourself to.

**What you can do yourself:**
- Use a special coccyx cushion when sitting
- Take ibuprofen if it is right for you

Source: [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/)

### `advice_tailbone_self_care`

**What to do:** Tailbone pain may get better after a few weeks. You can ease it yourself.

**Look out for:**
- Numbness around your genitals or bottom
- Problems peeing or pooing
- A painful lump near the top of your bottom, or a high temperature

**Get more help when:**
- Call 999 or go to A&E if you get numbness around your genitals or bottom, or problems peeing or pooing
- See a GP if it has not improved after a few weeks, or it is affecting your daily life

**Where to go:** You do not need to see anyone now. A pharmacist can help with painkillers and laxatives.

**What you can do yourself:**
- Sit up straight with your lower back supported, and use a special coccyx cushion
- Lie on your side to take pressure off your tailbone
- Use ibuprofen, and an ice pack or heat pack wrapped in a towel
- Use a laxative (a medicine that helps you poo) to soften your poo if the pain is worse when pooing
- Do not sit for a long time

Source: [Coccyx pain](https://www.nhs.uk/conditions/tailbone-coccyx-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_tail_cauda_equina`: The Back pain page gives these as emergency signs. Applying them to tailbone pain is AI judgement: the nerves at the bottom of the spine run close by.
- `rf_tail_abscess`: Could be an infected pocket of pus (pilonidal abscess), which may need draining. AI judgement, needs clinical review.
- `or_tail_gp`: The page says see a GP for a high temperature with tailbone pain and pain in another area, such as the tummy or lower back.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Tailbone pain from a bruise, strain or childbirth (coccydynia) |  | very common | Pain worse when sitting, or going from sitting to standing: strongly supports; Started after an injury, fall or accident: supports; Pregnant, or gave birth in the last 6 weeks: supports |
| Pilonidal abscess (a pocket of pus near the top of the buttocks) | 431709001 | uncommon | Painful lump, swelling or hole in the skin near the top of the crease of the bottom: strongly supports; Pus or blood leaking from a lump: supports; Skin over the painful area has changed colour: supports; Very high temperature, or feels hot, cold or shivery: supports; Severe pain: supports |
| An infection in the spine, such as a spinal abscess (a pocket of pus) or an infected disc |  | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Feels very unwell: supports; Feels cold to the touch, or shivery: supports; Pain worse at night, or not better with rest: supports; Severe pain: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
