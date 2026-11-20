# Review pack: Insect bite or sting

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
| [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | 2026-11-19 |  | Page last reviewed: 01 October 2026 |
| [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | 2026-11-19 |  | Page last reviewed: 17 July 2026 |
| [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | 2026-11-19 |  | Page last reviewed: 02 February 2026 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Lyme disease](https://www.nhs.uk/conditions/lyme-disease/) | 2026-11-19 |  | Page last reviewed: 03 June 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | 2026-11-19 |  | Page last reviewed: 13 October 2026 |
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

## Insect bite or sting red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bi_allergic_swelling`<br>Bite or sting with lips, mouth, throat or tongue suddenly swollen, throat tight or struggling to swallow | "Lips, mouth, tongue or throat suddenly swollen" OR "Throat feels tight" OR "Unable to swallow" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_breathing`<br>Bite or sting with breathing very fast or struggling to breathe | "Difficulty breathing" OR "Breathing very fast" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_child_floppy`<br>A child who is limp, floppy or not responding as usual after a bite or sting | "Under 16 years old" AND "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_confused_or_drowsy`<br>Feeling very confused or drowsy, which can be a serious allergic reaction<br>**Note:** The page says call 999 if you suddenly become very confused, drowsy or dizzy. Confusion is also checked for everyone, but that check gives A&E, not an ambulance. | "Suddenly confused" OR "So drowsy they are hard to wake or cannot stay awake" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_dizzy_with_rash`<br>Bite or sting with feeling dizzy or light-headed and a raised, itchy rash<br>**Note:** The page says call 999 if you feel very confused, drowsy or dizzy, and may also have a raised, itchy rash. Feeling dizzy alone after a sting is an urgent rule below. | "Feels light-headed" AND "Raised, itchy or swollen rash (hives)" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_snake`<br>Bitten by a snake | "Bitten by a snake" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | |
| `rf_bi_deep_infection`<br>Bite with pain much worse than expected, or black, purple or grey patches nearby | "Pain much worse than you would expect" OR "Black, purple or grey patches or blisters near a wound or red area" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| `rf_bi_cellulitis_unwell`<br>A painful, hot, swollen bite with a high temperature and a fast heartbeat or feeling dizzy | "Swollen area is red or hot to touch" AND "Very high temperature, or feels hot, cold or shivery" AND ("Heart beating very fast" OR "Feels light-headed") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Insect bite or sting red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bi_urgent_signs`<br>Stung in the mouth, throat or near the eyes, stung more than once, or had a serious allergic reaction to a sting before | "Stung or bitten in the mouth or throat, or near the eyes" OR "Stung more than once" OR "Had a severe allergic reaction before" | Urgent (help today)<br>Urgent care<br>Today<br>*Get an urgent GP appointment or help from NHS 111* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_dizzy_or_sick`<br>Bite or sting with feeling dizzy or light-headed, or tummy pain and being sick | "Feels light-headed" OR ("Stomach ache" AND "Feels sick or has been sick") | Urgent (help today)<br>Urgent care<br>Today<br>*Get an urgent GP appointment or help from NHS 111* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_high_temperature`<br>Bite or sting with a high temperature<br>**Note:** The page says a high temperature and swollen glands. Using a high temperature alone is AI judgement, to be cautious. | "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Get an urgent GP appointment or help from NHS 111* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_worse`<br>Bite or sting symptoms getting worse or not getting better | "Symptoms getting worse, or not getting better after about a week" | Urgent (help today)<br>Urgent care<br>Today<br>*Get an urgent GP appointment or help from NHS 111* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `rf_bi_cellulitis`<br>A bite that has become painful, hot and swollen, with the redness spreading | "Swollen area is red or hot to touch" AND "Redness or swelling spreading" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |
| `rf_bi_tick_unwell_or_rash`<br>A tick bite, or time where ticks live, with flu-like symptoms or a round or oval rash<br>**Note:** Source difference: the Insect bites page says see a GP. The Lyme disease page says an urgent GP appointment or 111. The more urgent is used. | "Bitten by a tick, or been in grassy or wooded areas with ticks, in the last 3 months" AND ("Round or oval rash, like a bullseye, after a tick bite" OR "Very high temperature, or feels hot, cold or shivery" OR "Aching body") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Lyme disease](https://www.nhs.uk/conditions/lyme-disease/) | |
| `rf_bi_raised_rash`<br>A raised, itchy rash spreading away from the bite or sting (a wider allergic reaction)<br>**Note:** AI judgement: hives away from the sting is a wider allergic reaction that can get worse. A 'yes' also brings in the hives entry symptom's own rules. | "Raised, itchy or swollen rash (hives)" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | **AI judgement, needs clinical review** | |

## Insect bite or sting: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bi_baby`<br>A baby under 1 with an insect bite or sting | "Under 1 year old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| `or_bi_pharmacy`<br>A bite or sting that is red, hot, painful, swollen or leaking pus (possibly infected) | "Swollen area is red or hot to touch" OR "Pus or fluid leaking" OR "Large swelling around the bite or sting, spreading over a few days" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*See a pharmacist. They can give antibiotics if it is infected.* | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |

## Default outcome

Used when no rule fires.

- **An insect bite or sting with nothing that needs more help: treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Bites and stings usually get better in a few days*
- Source: [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Insect bite or sting | Have you been bitten or stung by an insect, such as a bee, wasp, mosquito or tick? | 276433004 | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Throat feels tight | Does your throat feel tight or closed up? | 247323005 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| So drowsy they are hard to wake or cannot stay awake | Is the person who is unwell so drowsy that they are hard to wake, or cannot stay awake? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Raised, itchy or swollen rash (hives) | Do you have a raised, itchy or swollen rash? | 126485001 | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Bitten by a snake | Have you been bitten by a snake? | 283840005 | [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | |
| Pain much worse than you would expect | Is the pain much worse than you would expect, for example from a small cut or a red patch of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Black, purple or grey patches or blisters near a wound or red area | Are there black, purple or grey patches, or blisters, near a wound or a red or swollen area of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Stung or bitten in the mouth or throat, or near the eyes | Were you stung or bitten in the mouth or throat, or near the eyes? |  | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| Stung more than once | Were you stung more than once? |  | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| Had a severe allergic reaction before | Have you had a severe allergic reaction (anaphylaxis) before? For example, to a sting, a food or a medicine. |  | [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Symptoms getting worse, or not getting better after about a week | Are your symptoms getting worse? Or have they not started to get better after about a week? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Redness or swelling spreading | Is the redness or swelling spreading? |  | [Skin abscess](https://www.nhs.uk/conditions/skin-abscess/) | |
| Bitten by a tick, or been in grassy or wooded areas with ticks, in the last 3 months | In the last 3 months, have you been bitten by a tick, or spent time in grassy or wooded areas where ticks live? | 95898004 | [Lyme disease](https://www.nhs.uk/conditions/lyme-disease/) | |
| Round or oval rash, like a bullseye, after a tick bite | Do you have a round or oval rash that may look like a bullseye on a dartboard? On brown or black skin it may look like a bruise. |  | [Lyme disease](https://www.nhs.uk/conditions/lyme-disease/) | |
| Aching body | Does your body ache all over? | 68962001 | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Pus or fluid leaking | Is pus or fluid leaking from it? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Large swelling around the bite or sting, spreading over a few days | Has a large area around the bite or sting become swollen, for example bigger than the palm of your hand? |  | **AI judgement, needs clinical review** | |

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

### `advice_anaphylaxis_999`

**What to do:** Call 999 now and say you think it is anaphylaxis, a severe allergic reaction. Use an adrenaline auto-injector (such as an EpiPen) straight away if you have one.

**Look out for:**
- Swelling of the lips, mouth, tongue or throat
- Struggling to breathe, or very wheezy
- Skin, tongue or lips turning blue, grey or pale
- Feeling faint, very confused or drowsy

**Get more help when:**
- If you are no better after 5 minutes, use a second auto-injector if you have one
- Call 999 again if the person gets worse or stops responding

**Where to go:** Call 999 for an ambulance. Do not drive to A&E. Stay with the person until help arrives.

**What you can do yourself:**
- Lie down. You can raise your legs. If you are struggling to breathe, sit up slowly.
- If you are pregnant, lie on your left side
- If you were stung by an insect, try to remove the sting if it is still in the skin
- Do not stand or walk at any time, even if you feel better

Source: [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/)

### `advice_snake_bite_emergency`

**What to do:** Call 999 or go to A&E now. Most snake bites in the UK are not serious, but you must get medical help.

**Look out for:**
- Swelling spreading from the bite
- Feeling sick, faint or dizzy
- Swelling of the lips, mouth or throat, or difficulty breathing

**Get more help when:**
- Call 999 if the person gets worse

**Where to go:** Call 999 or go to A&E. Do not drive yourself.

**What you can do yourself:**
- Stay calm and keep the bitten part of the body as still as you can
- Do not try to suck out the poison, and do not put a tight band around the limb

Source: [Snake bites](https://www.nhs.uk/conditions/snake-bites/)

### `advice_skin_infection_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of a serious skin infection that is spreading, which can be life-threatening.

**Look out for:**
- Pain much worse than you would expect
- Black, purple or grey patches or blisters on the skin
- Feeling dizzy or faint, confused, or a fast heartbeat

**Get more help when:**
- Call 999 if the person gets worse, becomes confused or stops responding

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/), [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

### `advice_bite_urgent`

**What to do:** Get an urgent GP appointment or help from NHS 111 today. The bite or sting needs checking.

**Look out for:**
- Swelling of the lips, mouth, throat or tongue
- Breathing very fast or struggling to breathe
- Feeling very confused, drowsy or dizzy

**Get more help when:**
- Call 999 if you get any of these signs. Use an adrenaline auto-injector if you have one.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5.

**What you can do yourself:**
- Remove a sting by scraping it sideways with a fingernail or bank card
- Wash the area with soap and water, and hold a cold, wet cloth on it

Source: [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/)

### `advice_skin_infection_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Painful, hot, swollen skin can be a skin infection called cellulitis. Early treatment with antibiotics can stop it becoming more serious.

**Look out for:**
- The redness or swelling spreading
- A very high temperature, or feeling hot, cold or shivery
- A fast heartbeat, fast breathing, or feeling dizzy or faint
- Purple patches on the skin, or cold, clammy, pale skin

**Get more help when:**
- Call 999 or go to A&E if you get any of these signs, or become confused
- Contact your GP if you do not start to feel better 2 to 3 days after starting antibiotics

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Raise the affected area on a pillow or chair to reduce swelling
- Take paracetamol or ibuprofen for the pain
- Drink plenty of fluids

Source: [Cellulitis](https://www.nhs.uk/conditions/cellulitis/)

### `advice_tick_bite_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. A round or oval rash or flu-like symptoms after a tick bite can be an infection spread by ticks, which is easier to treat early with antibiotics.

**Look out for:**
- A rash that spreads, or looks like a bullseye
- A high temperature, a headache, aches and pains, or feeling tired

**Get more help when:**
- Ask for help again if you get pain and swelling in your joints, numbness, or heart problems in the weeks after

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Tell them if you have been in forests or grassy areas.

**What you can do yourself:**
- If the tick is still there, remove it with fine-tipped tweezers or a tick tool, close to the skin. Pull slowly upwards.
- Clean the bite with antiseptic or soap and water

Source: [Lyme disease](https://www.nhs.uk/conditions/lyme-disease/)

### `advice_bite_gp`

**What to do:** See a GP about the bite or sting. The source gives no fixed time.

**Look out for:**
- The area getting more red, hot, swollen or painful
- A high temperature, or the baby seeming unwell

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if symptoms get worse
- Call 999 if the baby's lips or mouth swell, or they struggle to breathe

**Where to go:** Book an appointment with your GP surgery.

Source: [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/)

### `advice_bite_pharmacy`

**What to do:** See a pharmacist. They can suggest antihistamines and steroid creams, and can give antibiotics if the bite or sting is infected.

**Look out for:**
- Redness or swelling spreading
- A high temperature, or feeling unwell
- Symptoms getting worse

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if symptoms get worse or you get a high temperature
- Call 999 if your lips, mouth or throat swell, or you struggle to breathe

**Where to go:** Go to a pharmacy. You do not need an appointment.

**What you can do yourself:**
- Wash the area with soap and water
- Hold an ice pack wrapped in a cloth on it for up to 20 minutes, and keep it raised if you can
- Do not scratch

Source: [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/)

### `advice_bite_self_care`

**What to do:** You can usually treat an insect bite or sting yourself. It should get better in a few days.

**Look out for:**
- The area becoming red, hot, painful or swollen, or leaking pus
- A round or oval rash like a bullseye after a tick bite
- Feeling unwell, or a high temperature

**Get more help when:**
- See a pharmacist if it looks infected
- Ask for an urgent GP appointment or call 111 if symptoms get worse
- Call 999 if your lips, mouth or throat swell, or you struggle to breathe

**Where to go:** Treat it yourself at home. A pharmacy can help.

**What you can do yourself:**
- Remove a sting or tick if it is still in the skin, then wash the area with soap and water
- Hold an ice pack wrapped in a cloth on it for up to 20 minutes
- A pharmacist can suggest tablets or creams to help the itch. Do not scratch.

Source: [Insect bites and stings](https://www.nhs.uk/conditions/insect-bites-and-stings/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bi_confused_or_drowsy`: The page says call 999 if you suddenly become very confused, drowsy or dizzy. Confusion is also checked for everyone, but that check gives A&E, not an ambulance.
- `rf_bi_dizzy_with_rash`: The page says call 999 if you feel very confused, drowsy or dizzy, and may also have a raised, itchy rash. Feeling dizzy alone after a sting is an urgent rule below.
- `rf_bi_high_temperature`: The page says a high temperature and swollen glands. Using a high temperature alone is AI judgement, to be cautious.
- `rf_bi_tick_unwell_or_rash`: Source difference: the Insect bites page says see a GP. The Lyme disease page says an urgent GP appointment or 111. The more urgent is used.
- `rf_bi_raised_rash`: AI judgement: hives away from the sting is a wider allergic reaction that can get worse. A 'yes' also brings in the hives entry symptom's own rules.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Reaction to an insect bite or sting |  | very common | Small, itchy or painful swollen lump where bitten or stung: strongly supports; Large swelling around the bite or sting, spreading over a few days: supports |
| Infection from a tick bite (Lyme), which can cause a bullseye rash | 23502006 | rare | Round or oval rash, like a bullseye, after a tick bite: strongly supports; Bitten by a tick, or been in grassy or wooded areas with ticks, in the last 3 months: strongly supports; Aching body: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very tired: supports |
| Necrotising fasciitis (a rare, very serious deep skin infection) | 52486002 | very rare | Pain much worse than you would expect: strongly supports; Swollen area is red or hot to touch: strongly supports; Black, purple or grey patches or blisters near a wound or red area: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Heart beating very fast: supports; Feels sick or has been sick: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
