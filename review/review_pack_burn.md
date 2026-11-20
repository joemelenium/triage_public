# Review pack: Burn or scald

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
| [Acid and chemical burns](https://www.nhs.uk/conditions/acid-and-chemical-burns/) | 2026-11-19 |  | Page last reviewed: 05 June 2024 |
| [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | 2026-11-19 |  | Page last reviewed: 31 March 2026 |
| [Tetanus](https://www.nhs.uk/conditions/tetanus/) | 2026-11-19 |  | Page last reviewed: 03 September 2026 |
| [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | 2026-11-19 |  | Page last reviewed: 18 April 2024 |
| [Sunburn](https://www.nhs.uk/conditions/sunburn/) | 2026-11-19 |  | Page last reviewed: 24 November 2025 |
| [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | 2026-11-19 |  | Page last reviewed: 28 May 2024 |
| [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | 2026-11-18 |  | Page last reviewed: 21 March 2023 |
| [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | 2026-11-19 |  | Page last reviewed: 26 February 2026 |
| [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | 2026-11-18 | 2024-04-08 |  |
| [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | 2026-11-18 | 2026-10-15 |  |
| [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | 2026-11-18 | 2023-08-08 | The page's own review date (August 2026) had passed when accessed. |
| [Cough](https://www.nhs.uk/symptoms/cough/) | 2026-11-18 |  | Page last reviewed: 08 December 2023 |
| [When to call 999](https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/) | 2026-11-18 | 2023-02-03 | The page's own review date (February 2026) had passed when accessed. |
| [Necrotising fasciitis](https://www.nhs.uk/conditions/necrotising-fasciitis/) | 2026-11-19 |  | Page last reviewed: 02 February 2026 |

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

## Burn or scald red flags: Emergency (help now)

Most of these are asked together as one question: *"Do any of these apply right now? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bu_chemical`<br>A burn caused by an acid or chemical<br>**Note:** Source difference: the Burns and scalds page says call 999 or go to A&E. The Acid and chemical burns page says call 999. The more urgent is used. | "Burn caused by an acid or chemical" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | [Acid and chemical burns](https://www.nhs.uk/conditions/acid-and-chemical-burns/) | |
| `rf_bu_smoke`<br>Breathed in smoke or hot fumes, or burns or soot around the mouth or nose<br>**Note:** Clinical knowledge: hot smoke can burn the airway, which can swell over the next hours and block breathing. | "Breathed in smoke or hot fumes, or burns around the mouth or nose" | Emergency (help now)<br>Emergency ambulance<br>Now<br>*Call 999* | **AI judgement, needs clinical review** | |
| `rf_bu_large_deep_or_site`<br>A burn that is very large or deep, or on the face, genitals or bottom | "Burn that is large or deep" OR "Burn on the face, genitals or bottom" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| `rf_bu_electricity`<br>A burn caused by electricity | "Burn caused by electricity" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| `rf_bu_tetanus_signs`<br>A burn with a stiff jaw, painful muscle spasms or difficulty swallowing | "Stiff jaw or painful muscle spasms" | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E* | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| `rf_bu_infected_unwell`<br>A burn that is painful, hot and swollen, with a high temperature and a fast heartbeat or feeling dizzy, or very unwell and getting worse | "Seems very unwell and getting worse, or feels something is seriously wrong" OR ("Swollen area is red or hot to touch" AND "Very high temperature, or feels hot, cold or shivery" AND ("Heart beating very fast" OR "Feels light-headed")) | Emergency (help now)<br>Emergency department<br>Now<br>*Call 999 or go to A&E now* | [Cellulitis](https://www.nhs.uk/conditions/cellulitis/) | |

## Burn or scald red flags: Urgent (help today)

Most of these are asked together as one question: *"Do any of these apply? Choose all that apply."*

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `rf_bu_sunburn_blistered_or_unwell`<br>Sunburn that is blistered or swollen, or with a high temperature, feeling very unwell, dizzy or sick | "Sunburn" AND ("Burn or sunburn has blistered or is swollen" OR "Very high temperature, or feels hot, cold or shivery" OR "Feels very unwell" OR "Feels light-headed" OR "Feels sick or has been sick") | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sunburn](https://www.nhs.uk/conditions/sunburn/) | |
| `rf_bu_child_sunburn`<br>A baby or young child with sunburn | "Sunburn" AND "Under 5 years old" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Sunburn](https://www.nhs.uk/conditions/sunburn/) | |
| `rf_bu_young_child_blistered`<br>A burn or scald in a child under 5 that has blistered<br>**Note:** AI judgement: blistered burns in young children are often deeper than they look, and burns in children can be a sign that they need more care. The Burns and scalds page says call 111 for a child under 5 if you are not sure what to do. | "Under 5 years old" AND "Burn or sunburn has blistered or is swollen" AND NOT "Sunburn" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | **AI judgement, needs clinical review** | |
| `rf_bu_hands_feet_joint`<br>A blistered burn on the hands, feet or over a joint<br>**Note:** AI judgement: blistered burns on the hands, feet or joints can scar and stop the joint moving well, so they are usually checked by a nurse or doctor. | "Burn on the hands, feet or over a joint" AND "Burn or sunburn has blistered or is swollen" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111 now* | **AI judgement, needs clinical review** | |
| `rf_bu_infection`<br>A burn that has become painful, hot and swollen, or with a high temperature<br>**Note:** The Tetanus page says an urgent GP appointment or 111 for a burn that is hot or swollen, or with a high temperature. | "Swollen area is red or hot to touch" OR "Very high temperature, or feels hot, cold or shivery" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| `rf_bu_tetanus`<br>A burn in someone not fully vaccinated against tetanus, or not sure | "Not fully vaccinated against tetanus, or not sure" AND NOT "Sunburn" | Urgent (help today)<br>Urgent care<br>Today<br>*Ask for an urgent GP appointment or get help from NHS 111* | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |

## Burn or scald: other rules

These are asked one at a time, and only if the answer could raise the outcome.

| Rule | Fires when | Outcome | Source | OK? |
| --- | --- | --- | --- | --- |
| `or_bu_worried`<br>A burn or scald and not sure what to do | "Worried about symptoms" | Urgent (help today)<br>Urgent care<br>Today<br>*Get help from NHS 111* | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |

## Default outcome

Used when no rule fires.

- **A small burn or scald with nothing that needs more help: cool it and treat it yourself**
- Outcome: Self-manageable, Self-care, No appointment needed. *Small burns can often be treated at home and take around 2 weeks to heal*
- Source: [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/)

## Questions as worded

The SNOMED CT column shows the concept each question has been matched to, where one fits. The match is AI judgement, checked only for the concept's name. Blank means no single concept fits.

| Short name | Question put to the patient | SNOMED CT | Source | OK? |
| --- | --- | --- | --- | --- |
| Burn or scald | Do you have a burn or scald? | 284196006 | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| Signs of a stroke | Do you think you are having a stroke, or have you had signs of a stroke in the last 24 hours, even if they have now stopped? The main signs are: one side of the face drooping, not being able to lift both arms and keep them up, or slurred or confused speech. Other signs include weakness or numbness down one side of the body, and blurred vision or loss of sight. |  | [Symptoms of a stroke](https://www.nhs.uk/conditions/stroke/symptoms/) | |
| Severe difficulty breathing | Are you having severe difficulty breathing? This means gasping, choking or not being able to get words out. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Lips or skin pale, blue or grey | Are your lips or skin pale, blue or grey? On brown or black skin this may be easier to see on the palms of the hands. |  | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Passed out and not responding normally | Has the person who is unwell passed out and is not responding as normal? | 422768004 | [Heart attack](https://www.nhs.uk/conditions/heart-attack/) | |
| Suddenly confused | Do you feel suddenly confused? | 130987000 | [Confusion (sudden)](https://www.nhs.uk/symptoms/confusion/) | |
| Bleeding that cannot be stopped | Do you have bleeding that you cannot stop, or blood coming out in spurts? |  | [Cuts and grazes](https://www.nhs.uk/conditions/cuts-and-grazes/) | |
| Serious self-harm or about to self-harm | Have you seriously harmed yourself, for example by taking an overdose? Or do you feel you may be about to harm yourself? |  | [Help for suicidal thoughts](https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts/) | |
| Burn caused by an acid or chemical | Was the burn caused by an acid or chemical, such as bleach or drain cleaner? | 426284001 | [Acid and chemical burns](https://www.nhs.uk/conditions/acid-and-chemical-burns/) | |
| Breathed in smoke or hot fumes, or burns around the mouth or nose | Did you breathe in smoke or hot fumes, for example in a fire? Or are there burns or black soot around the mouth or nose? |  | **AI judgement, needs clinical review** | |
| Burn that is large or deep | Is the burn large or deep? For example, bigger than the palm of the hand, or the skin looks white, brown, black or leathery. | 403192003 | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| Burn on the face, genitals or bottom | Is the burn on the face, genitals or bottom? |  | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| Burn caused by electricity | Was the burn caused by electricity? |  | [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | |
| Stiff jaw or painful muscle spasms | Do you have a stiff jaw that makes it hard to open your mouth, or painful muscle spasms or stiffness? |  | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| Seems very unwell and getting worse, or feels something is seriously wrong | Do you seem very unwell and are getting worse? Or do you feel something is seriously wrong? |  | [COVID-19 symptoms and what to do](https://www.nhs.uk/conditions/covid-19/covid-19-symptoms-and-what-to-do/) | |
| Swollen area is red or hot to touch | Is the swollen area red, or does it feel hot to touch? Redness may be harder to see on brown or black skin. |  | [Ankles (swollen)](https://www.nhs.uk/conditions/oedema/) | |
| Very high temperature, or feels hot, cold or shivery | Do you have a very high temperature, or do you feel hot, cold or shivery? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Heart beating very fast | Is your heart beating very fast? | 3424008 | [Pulmonary embolism](https://www.nhs.uk/conditions/pulmonary-embolism/) | |
| Feels light-headed | Do you feel light-headed? | 386705008 | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Sunburn | Is it sunburn, from too much sun? | 403194002 | [Sunburn](https://www.nhs.uk/conditions/sunburn/) | |
| Burn or sunburn has blistered or is swollen | Has the burn blistered, or is it swollen? |  | [Sunburn](https://www.nhs.uk/conditions/sunburn/) | |
| Feels very unwell | Do you feel very unwell? |  | [Cough](https://www.nhs.uk/symptoms/cough/) | |
| Feels sick or has been sick | Do you feel sick, or have you been sick? |  | [Chest pain](https://www.nhs.uk/symptoms/chest-pain/) | |
| Under 5 years old | Is the person who is unwell under 5 years old? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |
| Burn on the hands, feet or over a joint | Is the burn on the hands or feet, or over a joint such as the knee or elbow? |  | **AI judgement, needs clinical review** | |
| Not fully vaccinated against tetanus, or not sure | Have you missed any tetanus jabs? Or are you not sure if you have had them all? |  | [Tetanus](https://www.nhs.uk/conditions/tetanus/) | |
| Worried about symptoms | Are you worried about your symptoms? |  | [Sore throat](https://www.nhs.uk/symptoms/sore-throat/) | |

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

### `advice_burn_999`

**What to do:** Call 999 now. This burn needs checking and treating in hospital straight away.

**Look out for:**
- A hoarse voice, coughing or noisy breathing after breathing in smoke
- Difficulty breathing
- Feeling faint or confused

**Get more help when:**
- Call 999 again if the person gets worse before help arrives

**Where to go:** Call 999. Do not drive to A&E.

**What you can do yourself:**
- For a chemical burn, wear gloves. Take off any clothes with the chemical on them. Brush off dry chemicals. Then rinse the skin with lots of cool running water for about an hour.
- Do not put anything on the burn, such as creams or other chemicals

Source: [Acid and chemical burns](https://www.nhs.uk/conditions/acid-and-chemical-burns/), [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/)

### `advice_burn_ae`

**What to do:** Call 999 or go to A&E now. A large or deep burn, a burn on the face, genitals or bottom, or a burn from electricity needs checking in hospital.

**Look out for:**
- Difficulty breathing
- Feeling faint, cold or shivery

**Get more help when:**
- Call 999 if the person gets worse or cannot get to A&E safely

**Where to go:** Call 999 or go to A&E. Do not drive to A&E. Ask someone to drive you or call 999 and ask for an ambulance.

**What you can do yourself:**
- Hold the burn under cool running water for 20 minutes
- Remove clothing or jewellery near the burn, but not anything stuck to it
- Lay cling film over the burn once it has cooled. Do not wrap it around.

Source: [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/)

### `advice_tetanus_emergency`

**What to do:** Call 999 or go to A&E now. A stiff jaw or painful muscle spasms after a wound or burn can be tetanus, which needs treatment in hospital straight away.

**Look out for:**
- Difficulty breathing or swallowing
- A fast heartbeat, or a seizure (fit)

**Get more help when:**
- Call 999 if the person gets worse

**Where to go:** Call 999 or go to A&E. Do not drive yourself.

Source: [Tetanus](https://www.nhs.uk/conditions/tetanus/)

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

### `advice_sunburn_urgent`

**What to do:** Ask for an urgent GP appointment or get help from NHS 111 today. Severe sunburn can lead to heat exhaustion or heatstroke, which can be very serious.

**Look out for:**
- Feeling very hot, confused, or not sweating even though you are hot
- Fast breathing, or a fit
- Not responding

**Get more help when:**
- Call 999 if someone is confused, has a fit, or is not responding

**Where to go:** Ask your GP surgery for an urgent appointment, or call 111 or use 111 online. Call 111 for a child under 5.

**What you can do yourself:**
- Get out of the sun, and cool the skin with a cool shower or damp towel
- Drink plenty of water
- Do not burst blisters, and do not put ice on sunburnt skin

Source: [Sunburn](https://www.nhs.uk/conditions/sunburn/)

### `advice_burn_urgent`

**What to do:** Get help from NHS 111 today. The burn or scald needs checking by a nurse or doctor.

**Look out for:**
- The burn becoming red, hot, swollen or more painful
- Pus or a bad smell
- A high temperature, or feeling hot, cold or shivery

**Get more help when:**
- Call 999 or go to A&E if the burn turns out to be large or deep, or the person feels very unwell

**Where to go:** Call 111 or use 111 online, or ask your GP surgery for an urgent appointment. Call 111 for a child under 5.

**What you can do yourself:**
- Hold the burn under cool running water for 20 minutes, as soon as possible
- Cover it loosely with cling film. Do not use creams, butter or sticky plasters.
- Do not burst any blisters

Source: [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/), [Tetanus](https://www.nhs.uk/conditions/tetanus/)

### `advice_burn_self_care`

**What to do:** Small burns and scalds can often be treated at home, and take around 2 weeks to heal.

**Look out for:**
- The burn becoming red, hot, swollen or more painful, or leaking pus
- A high temperature
- The burn not healing after 2 weeks

**Get more help when:**
- Call 111 if the burn looks infected or you are not sure what to do
- Call 999 or go to A&E if the burn is large or deep, or on the face, genitals or bottom

**Where to go:** Treat it yourself at home. A pharmacist can advise on dressings and moisturisers.

**What you can do yourself:**
- Hold the burn under cool running water for 20 minutes, as soon as possible
- Take paracetamol or ibuprofen for the pain
- Do not put creams, oils or butter on it, do not use sticky plasters, and do not burst blisters

Source: [Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/)

## AI judgement and open points

Everything below rests on AI judgement, not on a direct statement in a source.

### Rules and defaults with a note

- `rf_sudden_confusion`: The source lists this for people who are short of breath. Checking it in every session is AI judgement, needs clinical review.
- `rf_bu_chemical`: Source difference: the Burns and scalds page says call 999 or go to A&E. The Acid and chemical burns page says call 999. The more urgent is used.
- `rf_bu_smoke`: Clinical knowledge: hot smoke can burn the airway, which can swell over the next hours and block breathing.
- `rf_bu_young_child_blistered`: AI judgement: blistered burns in young children are often deeper than they look, and burns in children can be a sign that they need more care. The Burns and scalds page says call 111 for a child under 5 if you are not sure what to do.
- `rf_bu_hands_feet_joint`: AI judgement: blistered burns on the hands, feet or joints can scar and stop the joint moving well, so they are usually checked by a nurse or doctor.
- `rf_bu_infection`: The Tetanus page says an urgent GP appointment or 111 for a burn that is hot or swollen, or with a high temperature.

### How source wording was turned into outcomes

The mapping from wording such as "See a GP" to the acuity, level of care and timeframe scales is AI judgement. It is written at the top of `knowledge_base/settings.yaml` and in `review/wave0_points_for_clinical_review.md`.

### Possible causes (used only to choose which question to ask next)

How common each cause is, and how strongly each finding points to it, are all AI estimates. They never set an outcome and are never shown to a patient as a diagnosis.

| Possible cause | SNOMED CT | How common | Findings that point towards or away from it |
| --- | --- | --- | --- |
| Cellulitis (an infection of the deeper layers of the skin) | 128045006 | uncommon | Swollen area is red or hot to touch: strongly supports; Redness or swelling spreading: supports; Very high temperature, or feels hot, cold or shivery: supports; Pus or fluid leaking: supports; A cut, bite, graze or broken skin near the swelling: supports; Swelling is severe, painful or came on suddenly: supports; Pain or swelling in one leg: supports |
| Small burn or scald |  | very common | Small burn, smaller than the palm of the hand: strongly supports; Burn or sunburn has blistered or is swollen: supports |
| Necrotising fasciitis (a rare, very serious deep skin infection) | 52486002 | very rare | Pain much worse than you would expect: strongly supports; Swollen area is red or hot to touch: strongly supports; Black, purple or grey patches or blisters near a wound or red area: supports; Very high temperature, or feels hot, cold or shivery: supports; Feels very unwell: supports; Seems very unwell and getting worse, or feels something is seriously wrong: supports; Heart beating very fast: supports; Feels sick or has been sick: supports |
| Serious burn (large, deep, chemical or electrical) |  | uncommon | Burn that is large or deep: strongly supports; Burn on the face, genitals or bottom: supports; Burn caused by an acid or chemical: supports; Burn caused by electricity: supports; Breathed in smoke or hot fumes, or burns around the mouth or nose: supports |
| Sunburn |  | rare | Sunburn: strongly supports; Burn or sunburn has blistered or is swollen: supports |
| Tetanus (a rare, serious infection from a dirty wound) | 76902006 | very rare | Stiff jaw or painful muscle spasms: strongly supports; Wound has soil, pus or body fluids in it, or is still dirty after cleaning: supports; Not fully vaccinated against tetanus, or not sure: supports; Unable to swallow: supports |
| Infected wound or burn | 76844004 | uncommon | Swollen area is red or hot to touch: strongly supports; Pus or fluid leaking: strongly supports; Very high temperature, or feels hot, cold or shivery: supports; Wound has soil, pus or body fluids in it, or is still dirty after cleaning: supports |

## Reviewer

- Name and role:
- Date:
- Overall: approved / approved with changes / not approved
- Comments:
