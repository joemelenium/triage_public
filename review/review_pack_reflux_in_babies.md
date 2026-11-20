# Review pack: Reflux in babies

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
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Colic](https://www.nhs.uk/conditions/colic/) | 2026-11-19 |  | Page last reviewed: 26 April 2022 |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |
| [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | 2026-11-19 |  | Page last reviewed: 10 June 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Bloating](https://www.nhs.uk/symptoms/bloating/) | 2026-11-19 |  | Page last reviewed: 21 January 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | 2026-11-18 |  | Page last reviewed: 19 February 2026 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Is your baby or toddler seriously ill?](https://www.nhs.uk/baby/health/when-to-get-urgent-medical-help-for-babies-and-children-under-5/) | 2026-11-19 |  | Page last reviewed: 6 August 2026 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |

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

## Reflux in babies red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply to your baby right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_br_green_vomit`<br>A baby being sick, with green or yellow-green sick: possible twisted or blocked bowel<br>**Note:** Source difference: the Reflux in babies page says an urgent GP appointment or 111 for green or yellow sick. The Diarrhoea and vomiting page says 999 or A&E for yellow-green or green sick in children. The more urgent is used. | "Green or yellow-green sick" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_br_floppy`<br>A baby who is limp, floppy, hard to wake or not responding as usual | "Child limp, floppy, hard to wake or not responding as usual" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| `rf_br_weak_cry`<br>A baby with a weak or high-pitched cry, or a cry not like their usual one | "Baby has a weak or high-pitched cry, or a cry not like their usual one" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | [Colic](https://www.nhs.uk/conditions/colic/) | |
| `rf_br_high_temperature`<br>A baby under 3 months with 38C or more, or 3 to 6 months with 39C or more | "Baby with a high temperature for their age" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_br_no_wet_nappy`<br>A baby with a dry nappy for 12 hours or more | "No pee for 12 hours or more" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| `rf_br_blotchy`<br>A baby with blotchy or mottled skin | "Blotchy or mottled skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |

## Reflux in babies red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply to your baby? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_br_urgent_signs`<br>A baby with blood in their sick or poo, forceful (projectile) sick, a swollen or tender tummy, a high temperature, being sick so often they cannot keep feeds down, diarrhoea for over a week, signs of dehydration, crying and very distressed, or refusing feeds | "Being sick with blood in it (vomiting blood)" OR "Being sick with great force (projectile)" OR "Bleeding from the bottom, or blood in poo" OR "Tummy looks swollen or much bigger than usual" OR "Very high temperature, or feels hot, cold or shivery" OR "Keeps being sick and cannot keep fluids down" OR "Diarrhoea for more than 7 days" OR "Signs of dehydration" OR "Baby will not stop crying and is very distressed" OR "Baby or young child feeding or eating much less than usual" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |

## Reflux in babies: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_br_gp`<br>Reflux not improving after trying things to ease it, starting after 6 months old, still there after 1 year, or a baby not gaining weight | "Reflux not improving after trying things to ease it" OR "Reflux started after 6 months old, or still there after 1 year" OR "Baby not gaining weight, or losing weight" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |

## Default outcome

Used when no rule fires.

- **A baby bringing up a little milk who is otherwise happy, healthy and gaining weight: reflux usually gets better on its own**
- Outcome: Self-manageable, Self-care, No appointment needed. *A health visitor can give advice and support*
- Source: [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Baby bringing up milk or being sick during or after feeds | Is your baby bringing up milk, or being sick, during or shortly after feeds? |  | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Green or yellow-green sick | Have you been sick, and was the sick green or yellow-green? | 71419002 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Child limp, floppy, hard to wake or not responding as usual | Is the person who is unwell limp, floppy, much sleepier than usual or hard to wake? Or not responding like they usually do? |  | [Shortness of breath](https://www.nhs.uk/symptoms/shortness-of-breath/) | |
| Baby has a weak or high-pitched cry, or a cry not like their usual one | Does your baby have a weak or high-pitched cry, or a cry that does not sound like their usual cry? |  | [Colic](https://www.nhs.uk/conditions/colic/) | |
| Baby with a high temperature for their age | Is the baby under 3 months old with a temperature of 38C or higher? Or 3 to 6 months old with a temperature of 39C or higher? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| No pee for 12 hours or more | Have you not had a pee for 12 hours or more? |  | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Blotchy or mottled skin | Is your skin blotchy or mottled? On brown or black skin, this may be easier to see on the palms of the hands or soles of the feet. | 406128001 | [Sepsis](https://www.nhs.uk/conditions/sepsis/) | |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Being sick with great force (projectile) | Has your baby been sick with much more force than usual, so that it shoots out (projectile)? | 8579004 | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Tummy looks swollen or much bigger than usual | Does your tummy look swollen, or much bigger than usual? | 60728008 | [Bloating](https://www.nhs.uk/symptoms/bloating/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Keeps being sick and cannot keep fluids down | Do you keep being sick, so that you cannot keep any drinks down? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Diarrhoea for more than 7 days | Have you had diarrhoea for more than 7 days? |  | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Signs of dehydration | Do you have signs of dehydration, such as peeing less than usual or dark, strong-smelling pee? | 34095006 | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Baby will not stop crying and is very distressed | Will your baby not stop crying, and do they seem very distressed? |  | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
| Baby or young child feeding or eating much less than usual | Is the child feeding or eating much less than usual? | 299698007 | [Bronchiolitis](https://www.nhs.uk/conditions/bronchiolitis/) | |
| Reflux not improving after trying things to ease it | Is your baby's reflux not getting better after trying things to ease it, such as holding them upright after feeds? |  | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
| Reflux started after 6 months old, or still there after 1 year | Did the reflux start after your baby was 6 months old? Or is your child over 1 and still bringing up feeds? |  | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
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

### `advice_sepsis_emergency`

**What to do:** Call 999 or go to A&E now. These can be signs of sepsis, a life-threatening reaction to an infection. It needs treatment in hospital straight away.

**Look out for:**
- Breathing very fast, or finding it hard to breathe
- Skin, lips or tongue that are blue, grey, pale or blotchy
- A rash that does not fade when you press a glass against it
- Being confused, very sleepy or hard to wake

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

Source: [Sepsis](https://www.nhs.uk/conditions/sepsis/), [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/)

### `advice_baby_reflux_urgent`

**What to do:** Ask for an urgent GP appointment or call NHS 111 today. Your baby should be checked today.

**Look out for:**
- Green or yellow sick
- Your baby becoming floppy, very sleepy or hard to wake
- A weak or high-pitched cry
- Fewer wet nappies, or no wet nappy for 12 hours

**Get more help when:**
- Call 999 or go to A&E if your baby gets any of the signs above

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep offering breast or bottle feeds, little and often

Source: [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/)

### `advice_baby_reflux_gp`

**What to do:** See a GP about your baby's reflux. They may check for a cows' milk allergy and suggest treatments.

**Look out for:**
- Green or yellow sick, or blood in sick or poo
- Being sick with much more force than usual
- Refusing feeds, or fewer wet nappies. These can be signs of dehydration, not having enough water in the body.

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your baby gets any of the signs above
- Call 999 or go to A&E if your baby is floppy, hard to wake, or has green sick

**Where to go:** Make an appointment with a GP. A health visitor can also give advice. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Hold your baby upright during feeds and for as long as you can after
- Burp your baby regularly during feeds

Source: [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/)

### `advice_baby_reflux_self_care`

**What to do:** It is very common for a baby to bring up a little milk during or after feeds. Your baby does not usually need to see a doctor, as long as they are happy, healthy and gaining weight.

**Look out for:**
- Green or yellow sick, or blood in sick or poo
- Being sick with much more force than usual, or not keeping feeds down
- Refusing feeds, not gaining weight, or crying and very distressed

**Get more help when:**
- See a GP if your baby is not getting better, is not gaining weight, or still has reflux after age 1
- Ask for an urgent GP appointment or call 111 if your baby gets any of the signs above
- Call 999 or go to A&E if your baby is floppy, hard to wake, or has green sick

**Where to go:** You do not need an appointment now. A health visitor can give advice and support. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Hold your baby upright during feeds and for as long as you can after
- Burp your baby regularly during feeds
- Always put your baby to sleep flat on their back. Do not raise the head of the cot.
- Ask a health visitor about feeding positions

Source: [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_br_green_vomit`: Source difference: the Reflux in babies page says an urgent GP appointment or 111 for green or yellow sick. The Diarrhoea and vomiting page says 999 or A&E for yellow-green or green sick in children. The more urgent is used.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Colic (a baby crying a lot for no clear reason) | 35363006 | very rare | Baby crying a lot and hard to settle: strongly supports; Baby will not stop crying and is very distressed: supports; Baby cries a lot, often in the evening, but feeds and grows well: strongly supports |
| Cows' milk allergy in a baby | 782555009 | very rare | Has eczema, hay fever or a food allergy: strongly supports; Raised, itchy or swollen rash (hives): supports; Diarrhoea: supports; Bleeding from the bottom, or blood in poo: supports; Baby coughing, gulping or unsettled during feeds: supports; Baby not gaining weight, or losing weight: supports |
| A narrowed stomach outlet in a baby (pyloric stenosis) | 48644003 | very rare | Being sick with great force (projectile): strongly supports; Baby seems hungry straight after being sick: strongly supports; Baby not gaining weight, or losing weight: supports; Signs of dehydration: supports |
| Reflux in a baby (bringing up milk after feeds) |  | rare | Baby coughing, gulping or unsettled during feeds: strongly supports; Baby crying a lot and hard to settle: supports |
| A twisted bowel in a baby (malrotation with volvulus) | 458422009 | very rare | Green or yellow-green sick: strongly supports; Tummy looks swollen or much bigger than usual: strongly supports; Bleeding from the bottom, or blood in poo: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Baby will not stop crying and is very distressed: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
