# Review pack: Limping in children

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
| [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | 2026-11-19 |  | Page last reviewed: 23 January 2025 |
| [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | 2026-11-19 |  | Page last reviewed: 03 April 2024 |
| [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/) | 2026-11-19 |  | Page last reviewed: 16 August 2023 |
| [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | 2026-11-19 |  | Page last reviewed: 11 June 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | 2026-11-19 |  | Page last reviewed: 20 November 2025 |
| [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | 2026-11-19 |  | Page last reviewed: 23 April 2024 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [Back pain](https://www.nhs.uk/conditions/back-pain/) | 2026-11-19 |  | Page last reviewed: 05 March 2026 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | 2026-11-19 |  | Page last reviewed: 5 November 2025 |
| [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |

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

## Limping in children red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_limp_cannot_bear_weight`<br>A child who cannot put any weight on their leg<br>**Note:** The Irritable hip page says urgent GP or 111 for this. The more urgent is used. | "Cannot walk or put weight on the leg" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_limp_misshapen`<br>The leg has changed shape or is pointing at an odd angle | "Changed shape, or pointing at an odd angle" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_limp_unwell_fever`<br>A child with a limp who feels generally unwell, with a high temperature or feeling hot, cold or shivery<br>**Note:** Could be an infected joint or bone, which needs treatment within hours. | "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_limp_tummy_pain`<br>A child with a limp and severe pain in the lower part of the tummy<br>**Note:** Could be appendicitis, or in boys a twisted testicle. | "Severe pain in the lower tummy" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_limp_worse`<br>A child whose limp or pain is getting worse | "Pain getting worse quickly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| `rf_limp_sudden_pain`<br>A child with sudden pain in the hip, knee or thigh<br>**Note:** Source difference: the Limping in children page says 999 or A&E. The Irritable hip page says urgent GP or 111 for sudden pain in the hip, thigh or knee. The more urgent is used, marked soft so a likely irritable hip in a well child can lower it to urgent. | "Pain started suddenly" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |

## Limping in children red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_limp_hip_thigh_knee_pain`<br>A limping child with pain in the hip, groin, thigh or knee<br>**Note:** A yes to hip pain also brings in the hip pain entry symptom. | "Hip pain" OR "Pain in the groin, thigh or knee" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | |
| `rf_limp_hot_swelling`<br>Pain, swelling and warmth over a bone or joint<br>**Note:** Could be an infected bone or joint. | "Swollen area is red or hot to touch" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Osteomyelitis](https://www.nhs.uk/conditions/osteomyelitis/) | |
| `rf_limp_injury`<br>A leg injury that is badly swollen, or may be broken | "Thinks a bone may be broken" OR ("Started after an injury, fall or accident" AND "Badly swollen, or swelled up very quickly") | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111, or go to an urgent treatment centre* | [Broken leg](https://www.nhs.uk/conditions/broken-leg/) | |

## Limping in children: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_limp_serious_signs`<br>A limping child with a lump on a bone, weight loss, or pain at night or at rest<br>**Note:** The page lists these as possible signs of cancer, such as leukaemia. Within a few days is AI judgement. | "A lump or swelling on a bone" OR "Losing weight without trying" OR "Pain worse at night, or not better with rest" | Soon (help within a few days)<br>General practice<br>Within a few days<br>*See a GP within a few days* | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |

## Default outcome

Used when no rule fires.

- **A child with a limp and no obvious cause: see a GP to find out what is causing it**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)
- **Note:** The page says a limp with no obvious cause should always be checked by a GP. Not a floor: a limp from a small injury or a blister can be looked after at home.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Limping | Are you limping? | 16973004 | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Cannot walk or put weight on the leg | Are you unable to walk, or to put any weight on your leg? | 285674009 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Changed shape, or pointing at an odd angle | Has the painful area changed shape, or is it pointing at an odd angle? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Severe pain in the lower tummy | Do you have severe pain in the lower part of your tummy? |  | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| Pain getting worse quickly | Is the pain getting worse quickly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Pain started suddenly | Did the pain start suddenly? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Hip pain | Do you have pain in your hip? | 49218002 | [Hip pain in adults](https://www.nhs.uk/symptoms/hip-pain/) | |
| Pain in the groin, thigh or knee | Is there pain in the groin, thigh or knee? In children, hip problems are often felt there. |  | [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Thinks a bone may be broken | Do you think you might have broken a bone? |  | [Wrist pain](https://www.nhs.uk/symptoms/hand-pain/wrist-pain/) | |
| Started after an injury, fall or accident | Did this start after an injury, a fall or an accident? |  | [Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) | |
| Badly swollen, or swelled up very quickly | Is it badly swollen, or did it swell up very quickly? |  | [Knee pain](https://www.nhs.uk/symptoms/knee-pain/) | |
| A lump or swelling on a bone | Is there a lump or swelling on a bone, for example on the leg? |  | [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Pain worse at night, or not better with rest | Is the pain worse at night, or does it not get better when you rest? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

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

### `advice_child_limp_emergency`

**What to do:** Call 999 or go to A&E now. Your child needs to be checked in hospital. It could be an infected joint or bone, a broken bone, or a hip problem that needs treatment quickly.

**Look out for:**
- Your child getting more unwell, sleepy or floppy
- A rash that does not fade when you press a glass against it
- Pain getting worse

**Get more help when:**
- Call 999 if your child is very unwell or you cannot get to A&E

**Where to go:** Go to A&E now, or call 999. Do not drive if you are upset. Bring any medicines your child takes.

**What you can do yourself:**
- Do not let your child walk on the painful leg
- Do not give them anything to eat until a doctor has checked them, in case they need an operation

Source: [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/), [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/), [Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/)

### `advice_child_hip_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Hip pain or a limp in a child needs to be checked the same day, as it could be a sign of something serious.

**Look out for:**
- A high temperature, or your child feeling hot, cold or shivery
- Not being able to put any weight on the leg
- The pain getting worse

**Get more help when:**
- Call 999 or go to A&E if your child gets a high temperature or seems very unwell. Do the same if they cannot put any weight on their leg.

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online.

**What you can do yourself:**
- Let your child rest their leg
- Give children's paracetamol or ibuprofen for the pain

Source: [Hip pain in children (irritable hip)](https://www.nhs.uk/symptoms/hip-pain-children-irritable-hip/), [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)

### `advice_child_limp_injury_urgent`

**What to do:** Get help from NHS 111 or go to an urgent treatment centre today. Your child may have a broken bone and may need an X-ray.

**Look out for:**
- The leg changing shape, or going cold, pale or blue
- Your child not being able to put any weight on the leg

**Get more help when:**
- Call 999 or go to A&E if the leg changes shape or your child cannot put any weight on it

**Where to go:** Call 111 or use 111 online, or go to an urgent treatment centre.

**What you can do yourself:**
- Keep the leg still and raised on a pillow
- Put an ice pack wrapped in a towel on it
- Give children's paracetamol for the pain

Source: [Broken leg](https://www.nhs.uk/conditions/broken-leg/), [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)

### `advice_child_limp_soon`

**What to do:** See a GP within a few days. A limp with a lump on a bone, weight loss, or pain at night needs to be checked.

**Look out for:**
- Your child getting more tired, pale or bruising easily
- A high temperature
- Not being able to put weight on the leg

**Get more help when:**
- Call 999 or go to A&E if your child cannot put weight on their leg, or seems unwell with a high temperature

**Where to go:** Ask your GP surgery for an appointment in the next few days.

Source: [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)

### `advice_child_limp_gp`

**What to do:** See a GP. A limp with no obvious cause should always be checked.

**Look out for:**
- Sudden pain in the hip, knee or thigh
- Not being able to put any weight on the leg
- A high temperature, or your child feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if your child gets sudden pain or cannot put weight on their leg. Do the same if they get worse, or seem unwell with a high temperature.

**Where to go:** Contact your GP surgery.

**What you can do yourself:**
- If your child is in pain, give them a children's painkiller

Source: [Limping in children](https://www.nhs.uk/symptoms/limp-in-children/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_limp_cannot_bear_weight`: The Irritable hip page says urgent GP or 111 for this. The more urgent is used.
- `rf_limp_unwell_fever`: Could be an infected joint or bone, which needs treatment within hours.
- `rf_limp_tummy_pain`: Could be appendicitis, or in boys a twisted testicle.
- `rf_limp_sudden_pain`: Source difference: the Limping in children page says 999 or A&E. The Irritable hip page says urgent GP or 111 for sudden pain in the hip, thigh or knee. The more urgent is used, marked soft so a likely irritable hip in a well child can lower it to urgent.
- `rf_limp_hip_thigh_knee_pain`: A yes to hip pain also brings in the hip pain entry symptom.
- `rf_limp_hot_swelling`: Could be an infected bone or joint.
- `or_limp_serious_signs`: The page lists these as possible signs of cancer, such as leukaemia. Within a few days is AI judgement.
- `limp default outcome`: The page says a limp with no obvious cause should always be checked by a GP. Not a floor: a limp from a small injury or a blister can be looked after at home.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| A rare cancer affecting the bones or blood, such as leukaemia (a cancer of the blood) |  | rare | Pain worse at night, or not better with rest: strongly supports; A lump or swelling on a bone: supports; Losing weight without trying: supports; Feels very tired: supports; Feels very unwell: supports |
| A broken bone (fracture), such as a broken wrist, ankle, finger, toe or collarbone | 125605004 | uncommon | Started after an injury, fall or accident: strongly supports; Very painful to press on the bone: strongly supports; Heard or felt a snap, crack or pop at the time of injury: supports; Swelling of the painful area: supports; Bruising: supports; Cannot walk or put weight on the leg: supports; Cannot move the painful joint or limb, or hold things: supports; Thinks a bone may be broken: supports; Feels faint, dizzy or sick from the pain: supports |
| Irritable hip (a short-lived swelling of the hip joint in children) | 301864002 | rare | Limping: strongly supports; Cold, flu, COVID-19 or a similar illness in the last few weeks: supports; Pain started suddenly: supports; Pain in the groin, thigh or knee: supports; Hip pain: supports |
| Juvenile arthritis (long-term joint swelling in children) | 410502007 | rare | Swelling of the painful area: strongly supports; Stiff for more than 30 minutes after waking: strongly supports; Pain for 2 weeks or more, not getting better: supports; Pain in several joints: supports |
| Osteomyelitis (an infection in a bone) | 60168000 | rare | Very high temperature, or feels hot, cold or shivery: strongly supports; Swollen area is red or hot to touch: supports; Skin over the painful area has changed colour: supports; Feels very unwell: supports; Pain worse at night, or not better with rest: supports; Child not using an arm, holding it still: supports; Cannot walk or put weight on the leg: supports |
| Perthes (a problem with the blood supply to the top of the thigh bone in children) | 111255008 | rare | Limping: strongly supports; Pain in the groin, thigh or knee: strongly supports; Pain for 2 weeks or more, not getting better: supports; Cannot move the painful joint or limb, or hold things: supports |
| Septic arthritis (an infection in a joint) | 372939007 | rare | Swollen area is red or hot to touch: strongly supports; Swelling of the painful area: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Cannot move the painful joint or limb, or hold things: supports; Cannot walk or put weight on the leg: supports; Severe pain: supports; Skin over the painful area has changed colour: supports; Pain in just one joint: supports |
| A slipped growth plate at the top of the thigh bone (slipped upper femoral epiphysis) | 26460006 | rare | Pain in the groin, thigh or knee: strongly supports; Limping: strongly supports; Leg looks shorter, or foot turned outwards: supports; Pain for 2 weeks or more, not getting better: supports; Cannot walk or put weight on the leg: supports |
| A sprain or strain (a stretched or torn ligament or muscle) |  | common | Twisted, rolled or overstretched it: strongly supports; Started after an injury, fall or accident: strongly supports; Swelling of the painful area: supports; Bruising: supports; Started after more activity than usual, or doing the same movement many times: supports; Pain worse when moving, easier when resting: supports; Pain in the ankle: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
