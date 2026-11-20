# Review pack: Swallowing problems

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
| [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | 2026-11-18 |  | Page last reviewed: 21 June 2023 |
| [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/) | 2026-11-19 |  | Page last reviewed: 20 December 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | 2026-11-19 |  | Page last reviewed: 18 March 2026 |
| [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | 2026-11-19 |  | Page last reviewed: 26 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
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

## Swallowing problems red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_sw_allergic_swelling`<br>Lips, mouth, tongue or throat suddenly swollen | "Lips, mouth, tongue or throat suddenly swollen" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| `rf_sw_cannot_swallow`<br>Cannot swallow at all, even your own spit<br>**Note:** The Glandular fever page says call 999 if you cannot swallow, including your own spit. The Sore throat page says call 999 or go to A&E. Food stuck in the food pipe needs removing in hospital. | "Unable to swallow" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/) | |
| `rf_sw_stridor`<br>Problems swallowing with a high-pitched sound when breathing | "High-pitched sound when breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_sw_battery_or_sharp`<br>Swallowed a button battery, a magnet, or something sharp<br>**Note:** Clinical knowledge: a swallowed button battery can burn through the food pipe within hours, and magnets and sharp objects can cause serious damage. They need checking in hospital straight away. | "Swallowed a button battery, magnet or something sharp" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |
| `rf_sw_neck_swelling`<br>Swelling in the neck or under the tongue, or a lot of swelling in the mouth | "Swelling in the neck or under the tongue, or a lot of swelling in the mouth" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| `rf_sw_drooling`<br>Problems swallowing with drooling<br>**Note:** The Sore throat page says call 999 or go to A&E for drooling. The Dysphagia page lists drooling as a sign of long-term swallowing problems, which need an urgent GP appointment. Marked soft, so that a likely long-term cause, such as a past stroke, can lower it to urgent. | "Drooling" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| `rf_sw_breathing`<br>Problems swallowing with difficulty breathing<br>**Note:** The Sore throat page says call 999 or go to A&E for difficulty breathing. The Dysphagia page says an urgent GP appointment or 111 for being short of breath after eating or drinking, and the Laryngeal cancer page says contact 111 for difficulty breathing. The more urgent is used, marked soft. | "Difficulty breathing" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

## Swallowing problems: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Problems swallowing: get checked today**
- Outcome: Urgent (help today), Urgent care, Today. *Ask for an urgent GP appointment or get help from NHS 111*
- Source: [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Problems swallowing | Do you have problems swallowing? For example, food or drink gets stuck, or you cough or choke when you eat or drink. | 40739000 | [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Lips, mouth, tongue or throat suddenly swollen | Have your lips, mouth, tongue or throat suddenly become swollen? |  | [Anaphylaxis](https://www.nhs.uk/conditions/anaphylaxis/) | |
| Unable to swallow | Are you unable to swallow? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| High-pitched sound when breathing | Are you making a high-pitched sound when you breathe? | 70407001 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Swallowed a button battery, magnet or something sharp | Has a button battery, a magnet, or something sharp like a bone or pin been swallowed? |  | **AI judgement, needs clinical review** | |
| Swelling in the neck or under the tongue, or a lot of swelling in the mouth | Is there swelling in your neck or under your tongue, or a lot of swelling inside your mouth? |  | [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/) | |
| Drooling | Are you drooling? This can be a sign of not being able to swallow. | 62718007 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Difficulty breathing | Are you finding it hard to breathe? In a child, this can look like grunting noises, or the stomach sucking in under the ribs. | 230145002 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_swallowing_ae`

**What to do:** Call 999 or go to A&E now. Something may be stuck in the throat or food pipe, or the throat may be swelling.

**Look out for:**
- Difficulty breathing, choking, or a high-pitched sound when breathing
- Not being able to swallow, even your own spit
- Lips, tongue or throat swelling

**Get more help when:**
- Call 999 straight away if breathing gets harder, or the person cannot speak or cough

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. If a battery or magnet was swallowed, take the packet with you.

**What you can do yourself:**
- Do not try to eat or drink anything more
- Do not try to make yourself sick

Source: [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/), [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/)

### `advice_mouth_throat_ae`

**What to do:** Call 999 or go to A&E now. Swelling in the mouth or neck can make it hard to breathe.

**Look out for:**
- Difficulty breathing, or a high-pitched sound when breathing
- Not being able to swallow, even your own spit, or drooling
- Swelling that is spreading in the neck, under the tongue or around the eye

**Get more help when:**
- Call 999 if breathing gets harder or you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Sit up and lean forward if that makes breathing easier

Source: [Dental abscess](https://www.nhs.uk/conditions/dental-abscess/), [Sore throat](https://www.nhs.uk/symptoms/sore-throat/), [Glandular fever](https://www.nhs.uk/conditions/glandular-fever/)

### `advice_swallowing_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Problems swallowing should always be checked. You can call 111 or use 111 online.

**Look out for:**
- Not being able to swallow at all, even your own spit, or drooling
- Difficulty breathing, or a high-pitched sound when breathing
- Food stuck in the throat or chest that will not go down

**Get more help when:**
- Call 999 or go to A&E if you get any of the signs above
- Call 999 if you get signs of a stroke, such as the face drooping, weak arms or slurred speech

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Eat slowly, take small mouthfuls, and sit upright when you eat and drink
- Soft foods may be easier to swallow until you have been checked

Source: [Dysphagia (swallowing problems)](https://www.nhs.uk/symptoms/swallowing-problems-dysphagia/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_sw_cannot_swallow`: The Glandular fever page says call 999 if you cannot swallow, including your own spit. The Sore throat page says call 999 or go to A&E. Food stuck in the food pipe needs removing in hospital.
- `rf_sw_battery_or_sharp`: Clinical knowledge: a swallowed button battery can burn through the food pipe within hours, and magnets and sharp objects can cause serious damage. They need checking in hospital straight away.
- `rf_sw_drooling`: The Sore throat page says call 999 or go to A&E for drooling. The Dysphagia page lists drooling as a sign of long-term swallowing problems, which need an urgent GP appointment. Marked soft, so that a likely long-term cause, such as a past stroke, can lower it to urgent.
- `rf_sw_breathing`: The Sore throat page says call 999 or go to A&E for difficulty breathing. The Dysphagia page says an urgent GP appointment or 111 for being short of breath after eating or drinking, and the Laryngeal cancer page says contact 111 for difficulty breathing. The more urgent is used, marked soft.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Anaphylaxis (a severe allergic reaction) | 39579001 | rare | Started soon after a food, medicine or insect sting: strongly supports; Lips, mouth, tongue or throat suddenly swollen: strongly supports; Throat feels tight: supports; Raised, itchy or swollen rash (hives): supports; Feels light-headed: supports; Breathing very fast: supports; Wheezing: supports; Has eczema, hay fever or a food allergy: supports; Had a severe allergic reaction before: supports |
| Heartburn or indigestion | 162031009 | uncommon | Heartburn or a sour taste in the mouth: strongly supports; Pain starts after eating: strongly supports; Chest pain comes and goes: supports; Cough worse at night: supports; Feels sick or has been sick: supports; Pain spreads to arm, neck, jaw, shoulder, stomach or back: argues against; Pain comes on with activity, stress or cold, and eases with rest: argues against; Feels sweaty: argues against |
| Achalasia (the food pipe cannot relax to let food into the stomach) | 45564002 | rare | Brings food or milk back up: strongly supports; Swallowing getting harder over weeks or months: strongly supports; Food sticks in the chest, behind the breastbone: supports; Losing weight without trying: supports; Coughs or chokes when eating or drinking: supports |
| Allergy swelling of the food pipe (eosinophilic oesophagitis) | 235599003 | uncommon | Food sticks in the chest, behind the breastbone: strongly supports; Feels like something is stuck in the throat or food pipe after eating: supports; Heartburn or a sour taste in the mouth: supports |
| Epiglottitis (swelling of the flap at the back of the throat that covers the windpipe) | 80384002 | rare | High-pitched sound when breathing: strongly supports; Drooling: strongly supports; Unable to swallow: supports; Difficulty breathing: supports; Very high temperature, or feels hot, cold or shivery: supports; Hoarse voice: supports; Child wants to sit up rather than lie down: supports |
| A feeling of a lump in the throat with nothing actually stuck | 267103008 | common | Feels like a lump in the throat, though food goes down normally: strongly supports; Feeling anxious, worried or panicky: supports; Heartburn or a sour taste in the mouth: supports; Phlegm dripping down the back of the throat from the nose: supports |
| Mouth cancer | 363505006 | rare | Mouth ulcer lasting more than 3 weeks: strongly supports; Red or white patch, or a lump, in the mouth or on the lip for more than 3 weeks: strongly supports; Lump in the mouth or neck: supports; Losing weight without trying: supports; Hoarse voice for more than 3 weeks: supports |
| Cancer of the food pipe | 363402007 | rare | Swallowing getting harder over weeks or months: strongly supports; Food sticks in the chest, behind the breastbone: strongly supports; Losing weight without trying: supports; Heartburn or a sour taste in the mouth: supports; Hoarse voice: supports; Feels very tired: supports |
| Food or an object stuck in the throat or food pipe | 47609003 | rare | Unable to swallow: strongly supports; Feels like something is stuck in the throat or food pipe after eating: strongly supports; Drooling: supports; Swallowed a button battery, magnet or something sharp: supports; Food sticks in the chest, behind the breastbone: supports |
| A serious infection spreading from a tooth into the face or neck |  | rare | Swelling in the neck or under the tongue, or a lot of swelling in the mouth: strongly supports; Swollen face, cheek or jaw: strongly supports; Swelling, redness or pain around the eye: supports; Difficulty opening the mouth: supports; Very high temperature, or feels hot, cold or shivery: supports; Problems swallowing: supports; Difficulty breathing: supports |
| Swallowing problems from a condition that affects the brain or nerves, such as a past stroke |  | common | Coughs or chokes when eating or drinking: strongly supports; Wet, gurgly voice after eating or drinking: strongly supports; Keeps getting chest infections, or one that is not getting better: supports; Drooling: supports |
| Cancer of the throat or voice box |  | rare | Hoarse voice for more than 3 weeks: strongly supports; Lump in the mouth or neck: strongly supports; Sore throat not improved after a week: supports; Earache: supports; Losing weight without trying: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
