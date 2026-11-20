# Review pack: Cut, graze or wound

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
| [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | 2026-11-19 |  | Page last reviewed: 02 February 2026 |
| [Tetanus](https://www.nhs.uk/conditions/tetanus/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | 2026-11-19 |  | Page last reviewed: 17 July 2026 |
| [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |

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

## Cut, graze or wound red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wo_large_deep_or_stuck`<br>A very large or deep wound, or something stuck in it | "Wound very large or deep" OR "Something stuck in the wound, such as glass" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_numb_or_cannot_move`<br>Lost feeling near the wound, or trouble moving it | "Loss of feeling near the wound, or trouble moving the area" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_face_or_palm`<br>A bad cut on the face or the palm of the hand | "Bad cut on the face or palm of the hand" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_deep_infection`<br>A wound much more painful than expected, or black, purple or grey patches or blisters near it | "Pain much worse than you would expect" OR "Black, purple or grey patches or blisters near a wound or red area" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| `rf_wo_unwell_after_wound`<br>A wound or red, swollen skin with a high temperature and muscle aches, a fast heartbeat or feeling dizzy, or very unwell and getting worse<br>**Note:** The Necrotising fasciitis page says call 999 or go to A&E for a wound with a high temperature, headache, tiredness and muscle aches, or a fast or pounding heartbeat or dizziness. | "Seems very unwell and getting worse, or feels something is seriously wrong" OR ("Very high temperature, or feels hot, cold or shivery" AND ("Aching body" OR "Heart beating very fast" OR "Feels light-headed")) | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| `rf_wo_tetanus_signs`<br>A wound with a stiff jaw, painful muscle spasms or stiffness | "Stiff jaw or painful muscle spasms" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| `rf_wo_snake`<br>Bitten by a snake | "Bitten by a snake" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | |
| `rf_wo_large_bite`<br>A large or deep bite | "Bitten by an animal or a person" AND "Cut longer than about 5cm (2 inches)" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E* | [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/) | |

## Cut, graze or wound red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_wo_dirty`<br>A wound with soil, pus or body fluids in it, or still dirty after cleaning | "Wound has soil, pus or body fluids in it, or is still dirty after cleaning" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_over_5cm`<br>A cut larger than around 5cm (2 inches) | "Cut longer than about 5cm (2 inches)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_infected`<br>A cut that is swollen, red and getting more painful, or with pus coming out | "Swollen area is red or hot to touch" OR "Pus or fluid leaking" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_unwell`<br>A cut and feeling generally unwell or a high temperature | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_bite_person_or_wild`<br>Bitten by a person, or a wild or stray animal, or any animal abroad<br>**Note:** The Cuts and grazes page names a person or a wild or stray animal. Including any animal bite abroad is AI judgement, because of rabies in some countries. | "Bitten by a person, or by a wild or stray animal (including abroad)" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| `rf_wo_bite_site`<br>A bite on the hands, feet, face or head | "Bite on the hands, feet, face or head" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/) | |
| `rf_wo_tetanus`<br>A wound in someone not fully vaccinated against tetanus, or not sure | "Not fully vaccinated against tetanus, or not sure" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| `rf_wo_gaping`<br>A cut whose edges gape apart and may need closing<br>**Note:** AI judgement: a cut that gapes may need stitches, strips or glue, which work best within a few hours. | "Edges of the cut gape apart" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111, or go to an urgent treatment centre* | **AI judgement, needs clinical review** | |

## Cut, graze or wound: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **A small cut or graze with nothing that needs more help: clean it, cover it and treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Most cuts and grazes can be treated at home and start to heal in a few days*
- Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Cut, graze, bite wound or other wound | Do you have a cut, graze or other wound, including a bite from an animal or person? | 262526004 | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Wound very large or deep | Is the wound very large or deep? For example, you can see fat, muscle or bone, or the edges gape open. | 262562003 | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Something stuck in the wound, such as glass | Is there something stuck in the wound, such as a piece of glass? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Loss of feeling near the wound, or trouble moving the area | Have you lost feeling near the wound, or do you have trouble moving the area, such as a finger? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Bad cut on the face or palm of the hand | Is it a bad cut on the face or the palm of the hand? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Pain much worse than you would expect | Is the pain much worse than you would expect, for example from a small cut or a red patch of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Black, purple or grey patches or blisters near a wound or red area | Are there black, purple or grey patches, or blisters, near a wound or a red or swollen area of skin? |  | [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Aching body | Does your body ache all over? | 68962001 | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Stiff jaw or painful muscle spasms | Do you have a stiff jaw that makes it hard to open your mouth, or painful muscle spasms or stiffness? |  | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| Bitten by a snake | Have you been bitten by a snake? | 283840005 | [Snake bites](https://www.nhs.uk/conditions/snake-bites/) | |
| Bitten by an animal or a person | Was the wound caused by a bite from an animal or a person? | 424685008 | [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/) | |
| Cut longer than about 5cm (2 inches) | Is the cut longer than about 5cm (2 inches)? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Wound has soil, pus or body fluids in it, or is still dirty after cleaning | Does the wound have soil, pus or body fluids in it, or is it still dirty after cleaning it? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Pus or fluid leaking | Is pus or fluid leaking from it? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Bitten by a person, or by a wild or stray animal (including abroad) | Were you bitten by a person, or by a wild or stray animal, or by any animal abroad? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Bite on the hands, feet, face or head | Is the bite on the hands, feet, face or head? |  | [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/) | |
| Not fully vaccinated against tetanus, or not sure | Have you missed any tetanus jabs? Or are you not sure if you have had them all? |  | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| Edges of the cut gape apart | Do the edges of the cut gape apart, so they do not stay together on their own? |  | **AI judgement, needs clinical review** | |

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

### `advice_wound_ae`

**What to do:** Call 999 or go to A&E now. The wound needs checking and treating in hospital.

**Look out for:**
- Bleeding that will not stop, or blood spurting out
- Feeling faint or dizzy

**Get more help when:**
- Call 999 if you cannot stop the bleeding or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Press firmly on the wound with a bandage or a clean, folded cloth
- If something is stuck in the wound, do not take it out. Press on either side of it.
- Raise the injured part if you can. If part of a finger or ear has come off, wrap it in clean tissue, put it in a plastic bag, and keep it on ice.

Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/), [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/)

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

### `advice_tetanus_emergency`

**What to do:** Call 999 or go to A&E now. A stiff jaw or painful muscle spasms after a wound or burn can be tetanus, which needs treatment in hospital straight away.

**Look out for:**
- Difficulty breathing or swallowing
- A fast heartbeat, or a seizure (fit)

**Get more help when:**
- Call 999 if the person gets worse

**Where to go:** Call 999 or go to A&E. Do not drive yourself.

Source: [Tetanus](https://www.nhs.uk/conditions/tetanus/)

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

### `advice_wound_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. The wound may need cleaning, closing, antibiotics or a tetanus injection.

**Look out for:**
- The wound getting more red, swollen or painful, or pus coming out
- A high temperature, or feeling generally unwell
- Pain much worse than you would expect, or dark patches near the wound

**Get more help when:**
- Call 999 or go to A&E if the pain is much worse than you would expect, or you feel very unwell. Do the same if you get a stiff jaw or muscle spasms.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. An urgent treatment centre may also be able to help.

**What you can do yourself:**
- Rinse the wound with tap water, pat it dry and cover it with a clean dressing
- Take paracetamol or ibuprofen if it hurts. Do not give aspirin to children under 16.

Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/), [Tetanus](https://www.nhs.uk/conditions/tetanus/)

### `advice_bite_wound_urgent`

**What to do:** Get help from NHS 111 or ask for an urgent GP appointment today. Bites from people and animals often get infected and may need antibiotics. A bite abroad may need treatment to prevent rabies.

**Look out for:**
- The bite becoming hot, swollen, red or more painful
- Fluid leaking, or an unpleasant smell
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Go to A&E if the wound is large or deep, or you cannot stop the bleeding

**Where to go:** Call 111 or use 111 online, or ask your GP surgery for an urgent appointment.

**What you can do yourself:**
- Clean the bite straight away under warm running water for a few minutes
- Gently squeeze it to make it bleed a little, unless it is already bleeding a lot
- Cover it with a clean dressing

Source: [Animal and human bites](https://www.nhs.uk/conditions/animal-and-human-bites/)

### `advice_wound_self_care`

**What to do:** You can treat a small cut or graze yourself. Stop any bleeding, clean the wound and cover it with a plaster or dressing.

**Look out for:**
- The cut becoming swollen, red and more painful, or pus coming out
- A high temperature, or feeling unwell
- Losing feeling near the wound, or trouble moving it

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if the wound looks infected. Do the same if you are not sure you have had all your tetanus jabs.
- Call 999 or go to A&E if you cannot stop the bleeding

**Where to go:** Treat it yourself at home.

**What you can do yourself:**
- Wash your hands, then rinse the wound with tap water or use sterile wipes
- Pat it dry and cover it with a plaster or dressing. Keep it clean and dry.
- Take paracetamol or ibuprofen if it hurts. Do not give aspirin to children under 16.

Source: [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_wo_unwell_after_wound`: The Necrotising fasciitis page says call 999 or go to A&E for a wound with a high temperature, headache, tiredness and muscle aches, or a fast or pounding heartbeat or dizziness.
- `rf_wo_bite_person_or_wild`: The Cuts and grazes page names a person or a wild or stray animal. Including any animal bite abroad is AI judgement, because of rabies in some countries.
- `rf_wo_gaping`: AI judgement: a cut that gapes may need stitches, strips or glue, which work best within a few hours.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Bite from an animal or person |  | rare | Bitten by an animal or a person: strongly supports; Bite on the hands, feet, face or head: supports; Bitten by a person, or by a wild or stray animal (including abroad): supports; Swollen area is red or hot to touch: supports |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Small cut or graze |  | very common | Small, shallow cut or graze: strongly supports; Bleeding has stopped, or stops with pressing: supports |
| Necrotising fasciitis (a rare, very serious deep skin infection) | 52486002 | very rare | Pain much worse than you would expect: strongly supports; Swollen area is red or hot to touch: strongly supports; Black, purple or grey patches or blisters near a wound or red area: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Heart beating very fast: supports; Feels sick or has been sick: supports |
| Cut damaging a nerve or tendon | 240037007 | rare | Loss of feeling near the wound, or trouble moving the area: strongly supports; Bad cut on the face or palm of the hand: supports; Wound very large or deep: supports |
| Tetanus (a rare, serious infection from a dirty wound) | 76902006 | very rare | Stiff jaw or painful muscle spasms: strongly supports; Wound has soil, pus or body fluids in it, or is still dirty after cleaning: supports; Not fully vaccinated against tetanus, or not sure: supports; Unable to swallow: supports |
| Infected wound or burn | 76844004 | uncommon | Swollen area is red or hot to touch: strongly supports; Pus or fluid leaking: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Wound has soil, pus or body fluids in it, or is still dirty after cleaning: supports |
| Cut that needs closing with stitches, strips or glue | 312608009 | common | Cut longer than about 5cm (2 inches): strongly supports; Edges of the cut gape apart: strongly supports; Wound very large or deep: supports; Bad cut on the face or palm of the hand: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
