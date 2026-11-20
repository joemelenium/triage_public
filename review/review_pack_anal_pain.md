# Review pack: Anal pain

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
| [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Piles (haemorrhoids)](https://www.nhs.uk/conditions/piles-haemorrhoids/) | 2026-11-19 |  | Page last reviewed: 01 April 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
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

## Anal pain red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ap_heavy_bleeding`<br>Bleeding non-stop from the bottom, or a lot of blood | "Heavy or non-stop bleeding from the bottom" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |

## Anal pain red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ap_severe_with_temperature`<br>Severe pain in the bottom with a high temperature, or feeling hot, cold or shivery | "Severe pain in the bottom" AND "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| `rf_ap_abscess_signs`<br>Constant throbbing pain near the bottom, with a red swelling or pus, and a high temperature: possible abscess<br>**Note:** The Anal pain page lists constant throbbing pain, pus and a high temperature as signs of an abscess, and says urgent for severe pain with a high temperature. | "Constant throbbing pain, swelling or pus near the bottom" AND "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| `rf_ap_black_poo`<br>Black or dark red poo | "Black, sticky poo, or dark red poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| `rf_ap_piles_with_temperature`<br>Pain in the bottom with a lump, and a high temperature or pus: possibly infected piles | "A lump in or around the bottom" AND ("Very high temperature, or feels hot, cold or shivery" OR "Constant throbbing pain, swelling or pus near the bottom") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Piles (haemorrhoids)](https://www.nhs.uk/conditions/piles-haemorrhoids/) | |

## Anal pain: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ap_gp`<br>Severe pain, pain not better after a few days, a throbbing swelling, or blood in poo or bleeding from the bottom<br>**Note:** A throbbing swelling with pus is not on the page's list for a GP. Adding it is AI judgement: an abscess needs to be drained. | "Severe pain in the bottom" OR "Bottom pain not better after a few days" OR "Constant throbbing pain, swelling or pus near the bottom" OR "Bleeding from the bottom, or blood in poo" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |

## Default outcome

Used when no rule fires.

- **Pain in the bottom with nothing that needs more help: things you can do to ease it, and a pharmacist can help**
- Outcome: Self-manageable, Self-care, No appointment needed. *See a GP if it does not get better after a few days*
- Source: [Anal pain](https://www.nhs.uk/symptoms/anal-pain/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Pain in the bottom (anus) | Do you have pain in or around your bottom (anus)? | 68653001 | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Heavy or non-stop bleeding from the bottom | Are you bleeding non-stop from your bottom, or is there a lot of blood? For example, the toilet water turns red or you see large blood clots. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Severe pain in the bottom | Is the pain in your bottom severe? |  | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Constant throbbing pain, swelling or pus near the bottom | Do you have a constant, throbbing pain near your bottom, with a red swelling or pus? |  | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| A lump in or around the bottom | Can you feel a lump in or around your bottom (anus)? |  | [Piles (haemorrhoids)](https://www.nhs.uk/conditions/piles-haemorrhoids/) | |
| Bottom pain not better after a few days | Has the pain in your bottom not got better after a few days? |  | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

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

### `advice_rectal_bleeding_ae`

**What to do:** Go to A&E or call 999 now. You are losing a lot of blood from your bottom and need to be checked in hospital straight away.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Cold, clammy, pale skin

**Get more help when:**
- Call 999 if you get worse or cannot get to A&E safely

**Where to go:** Go to A&E or call 999. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Lie down if you feel faint

Source: [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/)

### `advice_anal_pain_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Severe pain in your bottom with a high temperature can be a sign of an infection, such as an abscess (a pocket of pus).

**Look out for:**
- Bleeding that will not stop, or a lot of blood from your bottom
- Feeling very unwell, or hot, cold and shivery

**Get more help when:**
- Go to A&E or call 999 if you are bleeding non-stop or there is a lot of blood

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Take paracetamol for the pain
- A warm bath can ease the pain

Source: [Anal pain](https://www.nhs.uk/symptoms/anal-pain/)

### `advice_rectal_bleeding_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Black or dark red poo, or blood with diarrhoea, should be checked today.

**Look out for:**
- Bleeding that will not stop, or a lot of blood: the toilet water turns red or you see large clots
- Feeling faint or dizzy
- Being sick with blood

**Get more help when:**
- Go to A&E or call 999 if you get any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Iron tablets and dark foods like liquorice or blueberries can turn poo dark. Tell the doctor if you have had them.

Source: [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/)

### `advice_anal_pain_gp`

**What to do:** See a GP about the pain in your bottom. Do not feel embarrassed. It is a common problem that they are used to treating.

**Look out for:**
- A high temperature, or feeling hot, cold or shivery
- Black or dark red poo
- A lot of blood from your bottom

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if you get severe pain with a high temperature, or black or dark red poo
- Go to A&E or call 999 if you are bleeding non-stop or there is a lot of blood

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink lots of fluids and eat more fibre to keep your poo soft
- Take paracetamol, and try a warm bath

Source: [Anal pain](https://www.nhs.uk/symptoms/anal-pain/)

### `advice_anal_pain_self_care`

**What to do:** There are things you can do to ease pain in your bottom. A pharmacist can recommend creams, painkillers or medicines that help you poo.

**Look out for:**
- Severe pain, or pain that does not get better after a few days
- Blood in your poo or bleeding from your bottom
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- See a GP if the pain is severe, does not improve after a few days, or you have blood in your poo
- Ask for an urgent GP appointment or call 111 if you have severe pain and a high temperature, or black or dark red poo
- Go to A&E or call 999 if you are bleeding non-stop or there is a lot of blood

**Where to go:** You do not need an appointment now. A pharmacist can give advice in a private area. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Drink lots of fluids and eat more fibre to keep your poo soft
- Wipe your bottom with damp toilet paper, and do not scratch
- Take paracetamol, and try a warm bath
- Put an ice pack wrapped in a towel on the area for up to 20 minutes, every 2 to 3 hours
- Do not push too hard when you poo, and do not ignore the urge to go

Source: [Anal pain](https://www.nhs.uk/symptoms/anal-pain/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ap_abscess_signs`: The Anal pain page lists constant throbbing pain, pus and a high temperature as signs of an abscess, and says urgent for severe pain with a high temperature.
- `or_ap_gp`: A throbbing swelling with pus is not on the page's list for a GP. Adding it is AI judgement: an abscess needs to be drained.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| An abscess or fistula near the bottom (a pocket of pus, or a small tunnel to the skin) |  | uncommon | Constant throbbing pain, swelling or pus near the bottom: strongly supports; Severe pain in the bottom: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Pain in the bottom (anus): supports |
| A small tear in the skin of the bottom (anal fissure) | 30037006 | common | Pain when pooing: strongly supports; Bright red blood on the toilet paper or on the outside of the poo: strongly supports; Hard, dry or lumpy poo, or straining: supports; Constipation: supports; Pain in the bottom (anus): supports; Bleeding from the bottom, or blood in poo: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Piles (swollen blood vessels in and around the bottom) | 70153002 | common | Bright red blood on the toilet paper or on the outside of the poo: strongly supports; A lump in or around the bottom: strongly supports; Itchy bottom: supports; Pain in the bottom (anus): supports; Pain when pooing: supports; Constipation: supports; Bleeding from the bottom, or blood in poo: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
