# Review pack: Yellow skin or eyes (jaundice)

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
| [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | 2026-11-19 |  | Page last reviewed: 24 March 2026 |
| [Gallstones](https://www.nhs.uk/conditions/gallstones/) | 2026-11-19 |  | Page last reviewed: 11 August 2025 |
| [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/) | 2026-11-19 |  | Page last reviewed: 04 August 2025 |
| [Jaundice](https://www.nhs.uk/conditions/jaundice/) | 2026-11-19 |  | Page last reviewed: 22 January 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | 2026-11-18 |  | Page last reviewed: 06 August 2026 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Hepatitis](https://www.nhs.uk/conditions/hepatitis/) | 2026-11-19 |  | Page last reviewed: 31 December 2025 |
| [Pancreatic cancer: symptoms](https://www.nhs.uk/conditions/pancreatic-cancer/symptoms/) | 2026-11-19 |  | Page last reviewed: 9 June 2023 |

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

## Yellow skin or eyes (jaundice) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ja_newborn_first_day`<br>Jaundice in a baby less than 24 hours old | "Baby less than 24 hours old" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| `rf_ja_baby_unwell`<br>A baby with jaundice who is sleepier than usual or hard to wake, floppy or stiff, not feeding, or having jerking movements<br>**Note:** The page says 'not feeding'. The question asks about feeding much less than usual, which is used to be cautious. | "Under 1 year old" AND ("Child limp, floppy, hard to wake or not responding as usual" OR "Baby or young child feeding or eating much less than usual" OR "Has had a seizure (fit)") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| `rf_ja_baby_temperature`<br>A baby with jaundice who has a high or low temperature, feels hot or cold to the touch, or is shivering | "Under 1 year old" AND ("Baby with a high temperature for their age" OR "Very high temperature, or feels hot, cold or shivery" OR "Feels cold to the touch, or shivery") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| `rf_ja_baby_no_wet_nappies_or_breathing`<br>A baby with jaundice with no wet nappies, or difficulty breathing or breathing very fast | "Under 1 year old" AND ("No pee for 12 hours or more" OR "Difficulty breathing" OR "Breathing very fast") | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| `rf_ja_with_tummy_pain`<br>Yellow skin or eyes with tummy pain (possible gallstone blocking the bile duct)<br>**Note:** The Gallstones page says call 999 or go to A&E for yellow skin or eyes in someone with gallstone pain. Applying it to any tummy pain with jaundice is AI judgement, to be cautious. | NOT "Under 1 year old" AND "Stomach ache" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Gallstones](https://www.nhs.uk/conditions/gallstones/) | |
| `rf_ja_with_high_temperature`<br>Yellow skin or eyes with a very high temperature, or feeling hot, cold or shivery<br>**Note:** The Gallstones page says call 999 or go to A&E for a very high temperature or feeling hot, cold or shivery. With jaundice this can mean an infected bile duct. Soft, because a viral hepatitis can also cause a high temperature and needs urgent, not emergency, care. | NOT "Under 1 year old" AND "Very high temperature, or feels hot, cold or shivery" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Gallstones](https://www.nhs.uk/conditions/gallstones/) | |
| `rf_ja_seriously_unwell`<br>Yellow skin or eyes and very unwell and getting worse<br>**Note:** Clinical knowledge: jaundice with being very unwell can mean liver failure or a severe infection. | "Seems very unwell and getting worse, or feels something is seriously wrong" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | **AI judgement, needs clinical review** | |

## Yellow skin or eyes (jaundice) red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ja_baby_over_24_hours`<br>A baby over 24 hours old who may have jaundice, or whose jaundice is not getting better, or with dark pee or pale poo | "Under 1 year old" AND NOT "Baby less than 24 hours old" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP or midwife appointment, or call NHS 111* | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| `rf_ja_gilberts_worse`<br>Gilbert's syndrome with yellowing worse than usual, or not gone within a few days | "Diagnosed with Gilbert's syndrome" AND "Yellowing worse than usual, or not going away within a few days" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/) | |
| `rf_ja_new_jaundice`<br>New yellow skin or yellow whites of the eyes, not already known to be Gilbert's syndrome<br>**Note:** The Jaundice, Hepatitis and Pancreatic cancer pages all say an urgent GP appointment or 111 for yellow skin or eyes. | NOT "Under 1 year old" AND NOT "Diagnosed with Gilbert's syndrome" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |

## Yellow skin or eyes (jaundice): other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Known Gilbert's syndrome with yellowing that is no worse than usual**
- Outcome: Self-manageable, Self-care, No appointment needed. *No treatment needed for Gilbert's syndrome*
- Source: [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/)
- **Note:** Every other case of yellow skin or eyes is caught by the firm urgent rules above, so this default is only reached by someone already diagnosed with Gilbert's syndrome whose yellowing is as usual.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Yellow skin or yellow whites of the eyes (jaundice) | Have your skin or the whites of your eyes turned yellow? | 18165001 | [Jaundice](https://www.nhs.uk/conditions/jaundice/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Baby less than 24 hours old | Is the baby less than 24 hours old? |  | [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Has had a seizure (fit) | Have you had a seizure (fit)? | 91175000 | [Whooping cough](https://www.nhs.uk/conditions/whooping-cough/) | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels cold to the touch, or shivery | Do you feel cold to the touch, or are you shivering or shivery? This can happen even without a high temperature. |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Breathing very fast | Are you breathing very fast? | 271823003 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Diagnosed with Gilbert's syndrome | Has a doctor told you that you have Gilbert's syndrome? This is a common, usually harmless condition that can make the skin go slightly yellow at times. |  | [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/) | |
| Yellowing worse than usual, or not going away within a few days | Is the yellowing worse than usual, or has it not gone away within a few days? |  | [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/) | |

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

### `advice_baby_jaundice_emergency`

**What to do:** Call 999 or go to A&E now. Your baby has jaundice (yellow skin or yellow whites of the eyes) with signs that they need to be seen in hospital straight away.

**Look out for:**
- Your baby being very sleepy, hard to wake, floppy or stiff
- Jerking or twitching movements
- Not feeding, or no wet nappies

**Get more help when:**
- Call 999 if your baby gets worse while you are on your way

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance.

Source: [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/)

### `advice_jaundice_emergency`

**What to do:** Call 999 or go to A&E now. Yellow skin or eyes with tummy pain, a very high temperature or feeling very unwell can mean a blocked or infected bile duct, or a serious liver problem.

**Look out for:**
- Being confused, very sleepy or hard to wake
- Being sick, or blood in your sick or poo
- Feeling hot, cold or shivery

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Gallstones](https://www.nhs.uk/conditions/gallstones/), [Jaundice](https://www.nhs.uk/conditions/jaundice/)

### `advice_baby_jaundice_urgent`

**What to do:** Ask for an urgent GP or midwife appointment, or call NHS 111 today. Jaundice is common in newborn babies and is usually harmless, but your baby needs a check to see if they need treatment.

**Look out for:**
- Dark yellow or brown pee, or pale, creamy poo. Keep a sample of poo to show the midwife or doctor.
- Your baby becoming sleepier than usual, hard to wake, or not feeding
- A high temperature, or feeling cold, or no wet nappies

**Get more help when:**
- Call 999 or go to A&E if your baby is floppy or stiff, or has jerking movements. Do the same if they are not feeding or have no wet nappies.

**Where to go:** Contact your midwife or GP surgery for an urgent appointment, or call 111.

**What you can do yourself:**
- Feed your baby often, around 8 to 12 times a day. If they are sleepy, wake them for feeds.

Source: [Newborn jaundice](https://www.nhs.uk/conditions/jaundice-in-babies/)

### `advice_jaundice_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Yellow skin or yellow whites of the eyes (jaundice) can be a sign of something serious, such as a liver problem, and needs checking today.

**Look out for:**
- Tummy pain, especially under the ribs on the right
- A very high temperature, or feeling hot, cold or shivery
- Being confused or very sleepy

**Get more help when:**
- Call 999 or go to A&E if you get tummy pain, a very high temperature, or become confused

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5.

**What you can do yourself:**
- Do not drink alcohol until you have been checked

Source: [Jaundice](https://www.nhs.uk/conditions/jaundice/), [Hepatitis](https://www.nhs.uk/conditions/hepatitis/), [Pancreatic cancer: symptoms](https://www.nhs.uk/conditions/pancreatic-cancer/symptoms/), [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/)

### `advice_gilberts_self_care`

**What to do:** Yellowing that comes and goes with Gilbert's syndrome does not usually need treatment.

**Look out for:**
- Yellowing that is worse than usual, or does not go away within a few days
- Itchy skin, dark pee or pale poo, which Gilbert's syndrome does not usually cause

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if the yellowing is worse than usual or lasts more than a few days

**Where to go:** No appointment needed. Speak to a GP or pharmacist before taking new medicines.

**What you can do yourself:**
- Try to avoid things that set it off. For example, too little sleep, not drinking enough, alcohol or too much exercise.

Source: [Gilbert's syndrome](https://www.nhs.uk/conditions/gilberts-syndrome/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ja_baby_unwell`: The page says 'not feeding'. The question asks about feeding much less than usual, which is used to be cautious.
- `rf_ja_with_tummy_pain`: The Gallstones page says call 999 or go to A&E for yellow skin or eyes in someone with gallstone pain. Applying it to any tummy pain with jaundice is AI judgement, to be cautious.
- `rf_ja_with_high_temperature`: The Gallstones page says call 999 or go to A&E for a very high temperature or feeling hot, cold or shivery. With jaundice this can mean an infected bile duct. Soft, because a viral hepatitis can also cause a high temperature and needs urgent, not emergency, care.
- `rf_ja_seriously_unwell`: Clinical knowledge: jaundice with being very unwell can mean liver failure or a severe infection.
- `rf_ja_new_jaundice`: The Jaundice, Hepatitis and Pancreatic cancer pages all say an urgent GP appointment or 111 for yellow skin or eyes.
- `yellow_skin_or_eyes default outcome`: Every other case of yellow skin or eyes is caught by the firm urgent rules above, so this default is only reached by someone already diagnosed with Gilbert's syndrome whose yellowing is as usual.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Infection of the bile duct (cholangitis) | 6215006 | very rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Pain in the upper right of the tummy, just under the ribs: strongly supports; Feels cold to the touch, or shivery: supports; Feels very unwell: supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Yellow skin or yellow whites of the eyes (jaundice): strongly supports |
| Gallstone blocking the bile duct (the tube that carries bile from the liver) | 59848001 | rare | Pain in the upper right of the tummy, just under the ribs: strongly supports; Feels sick or has been sick: supports; Pale poo and dark pee: strongly supports; Yellow skin or yellow whites of the eyes (jaundice): strongly supports |
| Yellow or orange skin from eating a lot of carrots or similar foods |  | rare | Skin looks yellow or orange, but the whites of the eyes are still white: strongly supports; Eats a lot of carrots, sweet potatoes or other orange foods: supports |
| A liver problem in pregnancy that causes itching (ICP) | 235888006 | very rare | Itchy palms or soles in pregnancy: strongly supports; Itching worse at night: supports; Itching all over the body, without a rash: supports; Pale poo and dark pee: supports; Severe itching, for example keeping you awake: supports |
| Gilbert's syndrome (a harmless cause of yellow skin) | 27503000 | uncommon | Mild yellowing that comes and goes, for example when ill, tired or not eating: strongly supports; Feels very tired: supports |
| Hepatitis (a swollen liver, from a virus or alcohol) | 37871000 | uncommon | Feels very tired: supports; Feels sick or has been sick: supports; Pale poo and dark pee: supports; Aching body: supports; Very high temperature, or feels hot, cold or shivery: supports; Pain in the upper right of the tummy, just under the ribs: supports; Drinks a lot of alcohol: supports |
| Jaundice (yellow skin or yellow whites of the eyes) in a newborn baby | 387712008 | very rare | Baby or young child feeding or eating much less than usual: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Pale poo and dark pee: supports |
| Cancer of the pancreas or bile duct | 372142002 | very rare | Losing weight without trying: strongly supports; Pale poo and dark pee: supports; Feels very tired: supports; Itchy skin: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
