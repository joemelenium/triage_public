# Review pack: Bleeding from the bottom (rectal bleeding)

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
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | 2026-11-19 |  | Page last reviewed: 12 August 2025 |
| [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | 2026-11-19 |  | Page last reviewed: 10 June 2025 |
| [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | 2026-11-19 |  | Page last reviewed: 20 October 2026 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | 2026-11-19 |  | Page last reviewed: 18 August 2025 |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
| [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Hernia](https://www.nhs.uk/conditions/hernia/) | 2026-11-19 |  | Page last reviewed: 19 May 2026 |
| [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | 2026-11-18 | 2024-03-08 |  |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Sepsis](https://www.nhs.uk/conditions/sepsis/) | 2026-11-18 |  | Page last reviewed: 14 May 2026 |

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

## Bleeding from the bottom (rectal bleeding) red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_rb_heavy`<br>Bleeding non-stop, or a lot of blood: the toilet water turns red or there are large clots | "Heavy or non-stop bleeding from the bottom" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| `rf_rb_faint`<br>Bleeding from the bottom with passing out, or cold, clammy skin<br>**Note:** Clinical knowledge: these can be signs of losing a lot of blood. The Vomiting blood page gives the same signs as reasons for 999 or A&E. Firm: a likely small tear or piles does not explain passing out or cold, clammy skin. Feeling light-headed, the weak part, is a separate soft rule below. | "Passed out (fainted)" OR "Cold, clammy and pale skin" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | **AI judgement, needs clinical review** | |
| `rf_rb_light_headed`<br>Bleeding from the bottom with feeling light-headed<br>**Note:** Clinical knowledge: feeling light-headed can be a sign of losing a lot of blood, but often has another cause. | "Feels light-headed" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E or call 999* | **AI judgement, needs clinical review** | |
| `rf_rb_vomiting_blood`<br>Bleeding from the bottom and vomiting blood<br>**Note:** The Stomach ulcer page says 999 or A&E for vomiting blood or black, sticky poo. | "Being sick with blood in it (vomiting blood)" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/) | |
| `rf_rb_child_screaming_bouts`<br>A young child with blood in their poo and bouts of screaming with knees pulled up, pale or floppy in between: possible intussusception<br>**Note:** Clinical knowledge: blood and slime in the poo (like redcurrant jelly) with bouts of screaming is a sign of part of the bowel sliding into itself. | "Under 5 years old" AND "Young child with bouts of screaming and knees drawn up, pale or floppy between bouts" | Emergency (help now)<br>Emergency department<br>Now<br>*Go to A&E now, or call 999* | **AI judgement, needs clinical review** | |

## Bleeding from the bottom (rectal bleeding) red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_rb_black_poo`<br>Black or dark red poo<br>**Note:** With a stomach ache, the Stomach ache page says 999 or A&E for black and sticky poo, which the stomach ache rules apply. | "Black, sticky poo, or dark red poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| `rf_rb_bloody_diarrhoea`<br>Bloody diarrhoea | "Diarrhoea" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| `rf_rb_baby`<br>A baby under 1 with blood in their poo<br>**Note:** The Reflux in babies page says an urgent GP appointment or 111 for a baby with blood in their poo. | "Under 1 year old" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or call NHS 111* | [Acid reflux in babies](https://www.nhs.uk/conditions/reflux-in-babies/) | |
| `rf_rb_stomach_ache`<br>Blood in poo with a stomach ache<br>**Note:** Source difference: the Stomach ache page says an urgent GP appointment or 111 for a stomach ache with blood in the poo. The Bleeding from the bottom page says see a GP (non-urgent) for pain or a lump in the tummy. The more urgent is used, marked soft: pain when pooing from a small tear can be explained. | "Stomach ache" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |

## Bleeding from the bottom (rectal bleeding): other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_rb_child`<br>A child with blood in their poo | "Under 16 years old" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| `or_rb_3_weeks`<br>Blood in poo for 3 weeks, or poo softer, thinner or longer than usual for 3 weeks | "Blood in poo for 3 weeks or more" OR "Changes in pooing for 3 weeks or more" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| `or_rb_other_signs`<br>Bleeding from the bottom with a lot of pain around the bottom, a lump in the tummy, being more tired than usual, or losing weight | "Severe pain in the bottom" OR "A lump or swelling in the tummy or groin" OR "Feels very tired" OR "Losing weight without trying" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

## Default outcome

Used when no rule fires.

- **A small amount of bleeding from the bottom with nothing that needs more urgent help: a GP can check it**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/)
- **Note:** The page says a small amount of one-off bleeding is not usually serious, but a GP can check, because bleeding can sometimes be a sign of bowel cancer. Not a floor: likely piles can lower it to a pharmacist.

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Heavy or non-stop bleeding from the bottom | Are you bleeding non-stop from your bottom, or is there a lot of blood? For example, the toilet water turns red or you see large blood clots. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Passed out (fainted) | Have you passed out (fainted)? | 271594007 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Cold, clammy and pale skin | Is your skin cold, clammy and pale? |  | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Being sick with blood in it (vomiting blood) | Have you been sick with blood in it (vomiting blood)? It can be bright red, dark brown or black, or look like coffee granules. | 8765009 | [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Young child with bouts of screaming and knees drawn up, pale or floppy between bouts | Does your child have sudden bouts of screaming or crying with their knees pulled up to their chest, every 15 to 20 minutes? Do they go pale, quiet or floppy in between? |  | **AI judgement, needs clinical review** | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Diarrhoea | Do you have diarrhoea? This means passing watery or runny poo more often than usual. | 62315008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |
| Under 1 year old | Is the person who is unwell a baby under 1 year old? |  | **AI judgement, needs clinical review** | |
| Stomach ache | Do you have a stomach ache (pain in your tummy)? | 21522001 | [Stomach ache](https://www.nhs.uk/symptoms/stomach-ache/) | |
| Under 16 years old | Is the person who is unwell under 16 years old? |  | **AI judgement, needs clinical review** | |
| Blood in poo for 3 weeks or more | Have you had blood in your poo for 3 weeks or more? |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Changes in pooing for 3 weeks or more | For 3 weeks or more, has your poo changed in a way that is not usual for you? For example, it is softer, thinner or runnier, you poo more often, or you are constipated. | 88111009 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Severe pain in the bottom | Is the pain in your bottom severe? |  | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| A lump or swelling in the tummy or groin | Do you have a lump or swelling in your tummy or groin? It may go away when you lie down. |  | [Hernia](https://www.nhs.uk/conditions/hernia/) | |
| Feels very tired | Do you feel very tired? |  | [Tonsillitis](https://www.nhs.uk/conditions/tonsillitis/) | |
| Losing weight without trying | Are you losing weight without trying? | 422868009 | [Cough](https://www.nhs.uk/symptoms/cough/) | |

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

### `advice_vomiting_blood_ae`

**What to do:** Call 999 or go to A&E now. Being sick with blood can be a sign of bleeding in your stomach or food pipe. It needs to be checked in hospital straight away.

**Look out for:**
- Feeling faint or dizzy, or passing out
- Cold, clammy, pale skin, or fast or shallow breathing
- Black, sticky poo

**Get more help when:**
- Call 999 if you get worse, keep being sick with blood, or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance. Bring any medicines you take.

**What you can do yourself:**
- Do not eat or drink anything until a doctor has checked you
- If you can, keep a sample or a photo of the sick to show the doctor

Source: [Vomiting blood](https://www.nhs.uk/symptoms/vomiting-blood/), [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Stomach ulcer](https://www.nhs.uk/conditions/stomach-ulcer/)

### `advice_child_tummy_emergency`

**What to do:** Call 999 or go to A&E now. Your child needs to be checked in hospital straight away.

**Look out for:**
- Your child becoming more sleepy, floppy or hard to wake
- Blue, grey, pale or blotchy skin, lips or tongue
- Green sick, or blood in their poo

**Get more help when:**
- Call 999 if your child gets worse or you cannot get to A&E safely
- Trust your instincts. If you think something is seriously wrong, get help straight away.

**Where to go:** Call 999 or go to A&E. Do not drive if you are on your own with your child. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Do not give your child anything to eat until a doctor has checked them

Source: [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/), [Sepsis](https://www.nhs.uk/conditions/sepsis/)

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

### `advice_rectal_bleeding_gp`

**What to do:** See a GP. A small amount of bleeding is not usually serious, but a GP can check what is causing it. Bleeding is sometimes a sign of bowel cancer, which is easier to treat if found early.

**Look out for:**
- Black or dark red poo, or bloody diarrhoea
- Bleeding that will not stop, or a lot of blood
- Feeling faint or dizzy

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your poo is black or dark red, or you have bloody diarrhoea
- Go to A&E or call 999 if you are bleeding non-stop or there is a lot of blood

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Eat plenty of fibre and drink lots of fluids to keep your poo soft
- Do not push too hard when you poo

Source: [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_rb_faint`: Clinical knowledge: these can be signs of losing a lot of blood. The Vomiting blood page gives the same signs as reasons for 999 or A&E. Firm: a likely small tear or piles does not explain passing out or cold, clammy skin. Feeling light-headed, the weak part, is a separate soft rule below.
- `rf_rb_light_headed`: Clinical knowledge: feeling light-headed can be a sign of losing a lot of blood, but often has another cause.
- `rf_rb_vomiting_blood`: The Stomach ulcer page says 999 or A&E for vomiting blood or black, sticky poo.
- `rf_rb_child_screaming_bouts`: Clinical knowledge: blood and slime in the poo (like redcurrant jelly) with bouts of screaming is a sign of part of the bowel sliding into itself.
- `rf_rb_black_poo`: With a stomach ache, the Stomach ache page says 999 or A&E for black and sticky poo, which the stomach ache rules apply.
- `rf_rb_baby`: The Reflux in babies page says an urgent GP appointment or 111 for a baby with blood in their poo.
- `rf_rb_stomach_ache`: Source difference: the Stomach ache page says an urgent GP appointment or 111 for a stomach ache with blood in the poo. The Bleeding from the bottom page says see a GP (non-urgent) for pain or a lump in the tummy. The more urgent is used, marked soft: pain when pooing from a small tear can be explained.
- `bleeding_from_bottom default outcome`: The page says a small amount of one-off bleeding is not usually serious, but a GP can check, because bleeding can sometimes be a sign of bowel cancer. Not a floor: likely piles can lower it to a pharmacist.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| An abscess or fistula near the bottom (a pocket of pus, or a small tunnel to the skin) |  | uncommon | Constant throbbing pain, swelling or pus near the bottom: strongly supports; Severe pain in the bottom: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Pain in the bottom (anus): supports |
| A small tear in the skin of the bottom (anal fissure) | 30037006 | common | Pain when pooing: strongly supports; Bright red blood on the toilet paper or on the outside of the poo: strongly supports; Hard, dry or lumpy poo, or straining: supports; Constipation: supports; Pain in the bottom (anus): supports; Bleeding from the bottom, or blood in poo: supports |
| Bleeding from the stomach or food pipe, for example from an ulcer | 37372002 | uncommon | Black, sticky poo, or dark red poo: strongly supports; Being sick with blood in it (vomiting blood): strongly supports; A lot of blood, or still being sick with blood: supports; Feels light-headed: supports; Passed out (fainted): supports; Cold, clammy and pale skin: supports; Stomach ache: supports; Feels very unwell: supports |
| Bowel cancer warning signs | 1286877004 | rare | Blood in poo for 3 weeks or more: strongly supports; Changes in pooing for 3 weeks or more: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Bleeding from the bottom, or blood in poo: supports |
| Cows' milk allergy in a baby | 782555009 | very rare | Has eczema, hay fever or a food allergy: strongly supports; Raised, itchy or swollen rash (hives): supports; Diarrhoea: supports; Bleeding from the bottom, or blood in poo: supports; Baby coughing, gulping or unsettled during feeds: supports; Baby not gaining weight, or losing weight: supports |
| Diverticulitis (infected pouches in the bowel wall) | 307496006 | rare | Pain in the lower left side of the tummy: strongly supports; Very high temperature, or feels hot, cold or shivery: strongly supports; Stomach ache gradually getting worse: supports; Constipation: supports; Diarrhoea: supports; Bleeding from the bottom, or blood in poo: supports; Slime (mucus) in poo: supports |
| Crohn's or ulcerative colitis (long-term swelling of the gut) | 24526004 | rare | Diarrhoea for more than 7 days: strongly supports; Bleeding from the bottom, or blood in poo: strongly supports; Slime (mucus) in poo: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Cramping tummy pain that comes and goes in waves: supports; Diarrhoea: supports; Changes in pooing for 3 weeks or more: supports |
| The bowel sliding into itself in a child (intussusception) | 49723003 | very rare | Young child with bouts of screaming and knees drawn up, pale or floppy between bouts: strongly supports; Being sick: strongly supports; Bleeding from the bottom, or blood in poo: supports; Slime (mucus) in poo: supports; Child limp, floppy, hard to wake or not responding as usual: supports; Cramping tummy pain that comes and goes in waves: supports |
| Piles (swollen blood vessels in and around the bottom) | 70153002 | common | Bright red blood on the toilet paper or on the outside of the poo: strongly supports; A lump in or around the bottom: strongly supports; Itchy bottom: supports; Pain in the bottom (anus): supports; Pain when pooing: supports; Constipation: supports; Bleeding from the bottom, or blood in poo: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
