# Review pack: Bowel incontinence

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
| [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | 2026-11-19 |  | Page last reviewed: 15 August 2024 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | 2026-11-19 |  | Page last reviewed: 08 April 2025 |
| [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | 2026-11-19 |  | Page last reviewed: 12 April 2023 |
| [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | 2026-11-19 |  | Page last reviewed: 21 December 2023 |
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

## Bowel incontinence red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bi_nerve_signs`<br>Loss of bowel control with loss of feeling around the bottom or genitals, weakness or numbness in both legs, or not able to pee<br>**Note:** The Back pain page says 999 or A&E for back pain with these signs, or with pooing yourself. Applying them without back pain is AI judgement. | "Numb or no feeling around the genitals or bottom" OR "Numbness or weakness in both legs" OR "Not able to pee at all for several hours" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |

## Bowel incontinence red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bi_black_poo`<br>Black or dark red poo | "Black, sticky poo, or dark red poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | |
| `rf_bi_bloody_diarrhoea`<br>Bloody diarrhoea | "Bleeding from the bottom, or blood in poo" AND "Diarrhoea" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | |

## Bowel incontinence: other rules

These are asked one at a time, and only if the answer could raise the outcome.

None.

## Default outcome

Used when no rule fires.

- **Cannot control when you poo: see a GP, as there are treatments that can help**
- Outcome: Routine (help needed, timing not critical), General practice, No fixed time given in the source. *See a GP. The source gives no fixed time.*
- Source: [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Cannot control when you poo | Are you unable to control when you poo? For example, poo leaks out, or you cannot get to the toilet in time. | 72042002 | [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Numb or no feeling around the genitals or bottom | Have you lost feeling, or got numbness, around your genitals or your bottom (anus)? For example, you cannot feel the toilet paper when you wipe. | 449813001 | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Numbness or weakness in both legs | Do you have numbness, tingling or weakness in both legs? |  | [Back pain](https://www.nhs.uk/conditions/back-pain/) | |
| Not able to pee at all for several hours | Have you not been able to pee at all, not even a little, for 6 hours or more? |  | [Benign prostate enlargement](https://www.nhs.uk/conditions/enlarged-prostate/) | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Diarrhoea | Do you have diarrhoea? This means passing watery or runny poo more often than usual. | 62315008 | [Being sick](https://www.nhs.uk/symptoms/diarrhoea-and-vomiting/) | |

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

### `advice_nerve_emergency`

**What to do:** Call 999 or go to A&E now. Losing control of your bowels or bladder, with numbness around your bottom or weak legs, can mean pressure on the nerves at the base of the spine. It needs treatment within hours to prevent lasting damage.

**Look out for:**
- The numbness or weakness getting worse
- Not being able to pee

**Get more help when:**
- Call 999 if you cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive. Ask someone to drive you or call 999 and ask for an ambulance.

Source: [Back pain](https://www.nhs.uk/conditions/back-pain/)

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

### `advice_bowel_incontinence_gp`

**What to do:** See a GP. There are treatments that can help with bowel incontinence. Try not to be embarrassed. The doctor will be used to talking about it.

**Look out for:**
- Numbness around your bottom or genitals, or weakness in both legs
- Black or dark red poo, or bloody diarrhoea

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your poo is black or dark red, or you have bloody diarrhoea
- Call 999 or go to A&E if you have numbness around your bottom or genitals, weak legs, or cannot pee

**Where to go:** Make an appointment with a GP. For urgent help call 111 or use 111 online. In an emergency call 999.

**What you can do yourself:**
- Keep a diary of your symptoms and what you eat and drink
- Try to poo at regular times, such as after meals, and do not strain
- Wear clothes that are easy to take off, and plan an easy route to the toilet
- NHS talking therapies can help. So can charities, such as Bladder and Bowel UK.

Source: [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bi_nerve_signs`: The Back pain page says 999 or A&E for back pain with these signs, or with pooing yourself. Applying them without back pain is AI judgement.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cauda equina syndrome (pressure on the nerves at the bottom of the spine) | 192970008 | rare | Numb or no feeling around the genitals or bottom: strongly supports; New problems peeing or pooing: strongly supports; Pain, tingling, weakness or numbness in both legs: strongly supports; Changes in feeling or function during sex: supports; Pain spreads from the back or bottom down the leg: supports; Weakness in one or both legs, or a foot that drags: supports; Numbness, tingling or pins and needles in the leg or foot: supports; Numbness or weakness in both legs: strongly supports; Not able to pee at all for several hours: supports; Cannot control when you poo: supports; Back pain: strongly supports |
| Bowel cancer warning signs | 1286877004 | rare | Blood in poo for 3 weeks or more: strongly supports; Changes in pooing for 3 weeks or more: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Bleeding from the bottom, or blood in poo: supports |
| Constipation | 14760008 | common | Constipation: strongly supports; Hard, dry or lumpy poo, or straining: strongly supports; A child regularly pooing their pants (soiling): strongly supports; Pain when pooing: supports; Tummy pain eases after pooing or farting: supports; Bloating: supports; Takes a medicine that can cause constipation: supports; Often constipated: supports; Stomach ache: supports; Also wets during the day: supports |
| Crohn's or ulcerative colitis (long-term swelling of the gut) | 24526004 | rare | Diarrhoea for more than 7 days: strongly supports; Bleeding from the bottom, or blood in poo: strongly supports; Slime (mucus) in poo: strongly supports; Losing weight without trying: supports; Feels very tired: supports; Cramping tummy pain that comes and goes in waves: supports; Diarrhoea: supports; Changes in pooing for 3 weeks or more: supports |
| Irritable bowel syndrome (IBS) | 10743008 | common | Tummy pain eases after pooing or farting: strongly supports; Stomach ache that does not go away or keeps coming back: strongly supports; Pooing changes between diarrhoea and constipation: strongly supports; Bloating: strongly supports; Cramping tummy pain that comes and goes in waves: supports; Slime (mucus) in poo: supports; Farting a lot, or smelly farts: supports; Diarrhoea: supports; Constipation: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
