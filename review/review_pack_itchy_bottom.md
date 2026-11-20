# Review pack: Itchy bottom

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
| [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | 2026-11-19 |  | Page last reviewed: 03 October 2023 |
| [Threadworms](https://www.nhs.uk/conditions/threadworms/) | 2026-11-19 |  | Page last reviewed: 01 December 2023 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [Flu](https://www.nhs.uk/conditions/flu/) | 2026-11-18 |  | Page last reviewed: 03 February 2026 |
| [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | 2026-11-19 |  | Page last reviewed: 27 October 2025 |
| [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | 2026-11-19 |  | Page last reviewed: 15 August 2024 |
| [Piles (haemorrhoids)](https://www.nhs.uk/conditions/piles-haemorrhoids/) | 2026-11-19 |  | Page last reviewed: 01 April 2026 |
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

## Itchy bottom red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_ib_black_poo`<br>Itchy bottom with black or dark red poo<br>**Note:** Source difference: the Itchy bottom page says see a GP (non-urgent) for blood in poo that might be dark red or black. The Bleeding from the bottom page says an urgent GP appointment or 111 for black or dark red poo. The more urgent is used. | "Black, sticky poo, or dark red poo" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |

## Itchy bottom: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_ib_worms_young_or_pregnant`<br>Possible threadworms in a child under 2, or in someone pregnant or breastfeeding: see a GP, midwife or health visitor instead of a pharmacist<br>**Note:** The page says children under 2 and pregnant or breastfeeding women need to see a GP, midwife or health visitor for threadworms. 'Gave birth in the last 6 weeks' stands in for breastfeeding. | ("Tiny white worms like pieces of thread" OR "Itchy bottom worse at night") AND ("Under 2 years old" OR "Pregnant, or gave birth in the last 6 weeks") | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP, midwife or health visitor. The source gives no fixed time.* | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| `or_ib_gp`<br>Itchy bottom that is not going away or keeps coming back, with pain, bleeding, leaking, changes in pooing, itching elsewhere, or a change around the bottom | "Itchy bottom not going away, or keeps coming back" OR "Pain in the bottom (anus)" OR "Bleeding from the bottom, or blood in poo" OR "Cannot control when you poo" OR "Changes in pooing for 3 weeks or more" OR "Itchy skin on other parts of the body too" OR "A lump in or around the bottom" | Routine (help needed, timing not critical)<br>General practice<br>No fixed time given in the source<br>*See a GP. The source gives no fixed time.* | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| `or_ib_threadworms`<br>Itchy bottom that is worse at night, or tiny white worms like thread: possible threadworms | "Tiny white worms like pieces of thread" OR "Itchy bottom worse at night" | Routine (help needed, timing not critical)<br>Community pharmacy<br>No fixed time given in the source<br>*See a pharmacist. The source gives no fixed time.* | [Threadworms](https://www.nhs.uk/conditions/threadworms/) | |

## Default outcome

Used when no rule fires.

- **Itchy bottom with nothing that needs more help: things you can do to ease it, and a pharmacist can help**
- Outcome: Self-manageable, Self-care, No appointment needed. *Get medical help if the itching does not stop*
- Source: [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Itchy bottom | Do you have an itchy bottom (anus)? | 90446007 | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Black, sticky poo, or dark red poo | Is your poo black and sticky, or dark red? Iron tablets can turn poo dark, but black sticky poo can be a sign of bleeding. |  | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Tiny white worms like pieces of thread | Are the worms tiny, white and like pieces of thread? They may be seen in poo or around the bottom, often at night. |  | [Threadworms](https://www.nhs.uk/conditions/threadworms/) | |
| Itchy bottom worse at night | Is the itching worse at night? |  | [Threadworms](https://www.nhs.uk/conditions/threadworms/) | |
| Under 2 years old | Is the person who is unwell under 2 years old? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Pregnant, or gave birth in the last 6 weeks | Are you pregnant, or have you given birth in the last 6 weeks? |  | [Flu](https://www.nhs.uk/conditions/flu/) | |
| Itchy bottom not going away, or keeps coming back | Is the itching not going away, or does it keep coming back? Or has a cream from a pharmacy not helped after 1 week? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| Pain in the bottom (anus) | Do you have pain in or around your bottom (anus)? | 68653001 | [Anal pain](https://www.nhs.uk/symptoms/anal-pain/) | |
| Bleeding from the bottom, or blood in poo | Have you had bleeding from your bottom, or blood in your poo? This includes blood on the toilet paper, red streaks on your poo, or pink water in the toilet. | 12063002 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Cannot control when you poo | Are you unable to control when you poo? For example, poo leaks out, or you cannot get to the toilet in time. | 72042002 | [Bowel incontinence](https://www.nhs.uk/conditions/bowel-incontinence/) | |
| Changes in pooing for 3 weeks or more | For 3 weeks or more, has your poo changed in a way that is not usual for you? For example, it is softer, thinner or runnier, you poo more often, or you are constipated. | 88111009 | [Bleeding from the bottom (rectal bleeding)](https://www.nhs.uk/symptoms/bleeding-from-the-bottom-rectal-bleeding/) | |
| Itchy skin on other parts of the body too | Is your skin itchy on other parts of your body too? |  | [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/) | |
| A lump in or around the bottom | Can you feel a lump in or around your bottom (anus)? |  | [Piles (haemorrhoids)](https://www.nhs.uk/conditions/piles-haemorrhoids/) | |

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

### `advice_itchy_bottom_gp`

**What to do:** See a GP about your itchy bottom. They will try to find the cause and may prescribe a cream or medicine.

**Look out for:**
- Blood in your poo that is dark red or black
- Bleeding or leaking from your bottom
- Pain in your bottom

**Get more help when:**
- Ask for an urgent GP appointment or call 111 if your poo is black or dark red
- Tell the GP straight away if a cream or medicine makes the itching worse

**Where to go:** Make an appointment with a GP. A sexual health clinic can also help if you think it might be from a sexually transmitted infection. For urgent help call 111.

**What you can do yourself:**
- Wash gently with water or unscented soap, and pat dry
- Wear loose cotton underwear, and do not scratch

Source: [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/)

### `advice_itchy_bottom_pharmacy`

**What to do:** See a pharmacist. An itchy bottom that is worse at night, or tiny white worms like thread, is probably threadworms. A pharmacist can give medicine to treat them.

**Look out for:**
- Itching that does not go away after treatment
- Pain or bleeding from your bottom

**Get more help when:**
- See a GP if the itching does not go away, or for a child under 2 or someone pregnant or breastfeeding

**Where to go:** Go to a pharmacy. You can ask for a private area to talk. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Everyone in your home should be treated, even if they do not have symptoms
- Wash your hands and scrub under your nails often, most of all after the toilet and before you eat
- Keep nails short, and wash bedding and towels on a hot wash

Source: [Threadworms](https://www.nhs.uk/conditions/threadworms/), [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/)

### `advice_itchy_bottom_self_care`

**What to do:** You can often ease an itchy bottom yourself. A pharmacist can suggest creams that help.

**Look out for:**
- Itching that does not go away or keeps coming back
- Pain, bleeding or leaking from your bottom
- Tiny white worms in your poo, or itching that is worse at night

**Get more help when:**
- See a pharmacist if you think it might be threadworms
- See a GP if the itching does not go away, or a steroid cream has not helped after 1 week

**Where to go:** You do not need an appointment now. A pharmacist can give advice. For urgent help call 111 or use 111 online.

**What you can do yourself:**
- Gently wash and dry your bottom after pooing and before bed. Pat it dry, do not rub.
- Wear loose cotton underwear, and avoid scented soaps and bubble bath
- Do not scratch. Keep your nails short.
- Eat plenty of fibre so you do not get constipated
- Do not use steroid creams for longer than 1 week

Source: [Anus (itchy)](https://www.nhs.uk/symptoms/itchy-anus/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_ib_black_poo`: Source difference: the Itchy bottom page says see a GP (non-urgent) for blood in poo that might be dark red or black. The Bleeding from the bottom page says an urgent GP appointment or 111 for black or dark red poo. The more urgent is used.
- `or_ib_worms_young_or_pregnant`: The page says children under 2 and pregnant or breastfeeding women need to see a GP, midwife or health visitor for threadworms. 'Gave birth in the last 6 weeks' stands in for breastfeeding.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Skin irritation around the bottom |  | very common | Itchy skin on other parts of the body too: supports; Diarrhoea: supports; Cannot control when you poo: supports |
| Piles (swollen blood vessels in and around the bottom) | 70153002 | common | Bright red blood on the toilet paper or on the outside of the poo: strongly supports; A lump in or around the bottom: strongly supports; Itchy bottom: supports; Pain in the bottom (anus): supports; Pain when pooing: supports; Constipation: supports; Bleeding from the bottom, or blood in poo: supports |
| Threadworms | 266162007 | common | Tiny white worms like pieces of thread: strongly supports; Itchy bottom worse at night: strongly supports; Others nearby have the same symptoms: supports; Itchy bottom: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
