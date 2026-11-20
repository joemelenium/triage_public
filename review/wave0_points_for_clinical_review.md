# Wave 0: points for clinical review

**Status: AI-drafted, not clinically reviewed. Not for clinical use.**

This is a short list of the judgement calls behind the chest pain and sore
throat content. It is not the full review pack. The full pack (every red flag,
rule, question and piece of advice, as worded, with sources) is produced in
the next build step.

Source pages are listed in `sources/source_log.yaml`, with text snapshots in
`sources/nhs_uk/`.

## 1. How source wording was turned into outcomes

| NHS website wording | Acuity | Level of care | Timeframe |
| --- | --- | --- | --- |
| Call 999 | Emergency | Emergency ambulance | Now |
| Call 999 or go to A&E | Emergency | Emergency department | Now |
| Ask for an urgent GP appointment or get help from 111 | Urgent | Urgent care | Today |
| See a GP (labelled "non-urgent" on the site) | Routine | General practice | No fixed time |
| See a pharmacist | Routine | Community pharmacy | No fixed time |
| Self-care advice only | Self-manageable | Self-care | No appointment needed |

Questions for a reviewer:

- Is "See a GP" best read as **routine**, or as **soon** (within a few days)?
  The source gives no time. Nothing in Wave 0 currently produces "soon".
- Is "Call 999 or go to A&E" best read as emergency department, with the
  ambulance as a way of getting there?

## 2. Where two source pages disagree

### 2a. Chest pain: does any chest pain need 999 or A&E?

The Pulmonary embolism page says to call 999 or go to A&E if "you feel pain in
your chest or upper back". The Chest pain page says to call 999 for specific
signs, and to see a GP for pain that comes and goes or has gone away.

**Working answer, chosen to be pragmatic:** both pages are followed.

- Pain that is there now: emergency, emergency department (999 or A&E).
- Pain that comes and goes: urgent (111), from the Angina page.
- Pain that has stopped, with no red flag: routine, general practice.

**For a reviewer:** this will over-triage people whose ongoing pain is plainly
not serious, such as a pulled muscle that still hurts. Is "there now" the right
dividing line? Should pain that stopped only recently be treated more urgently
than "routine"?

### 2b. Resolved by using the more urgent advice

This may over-triage.

| Finding (with chest pain) | Page A | Page B | Used |
| --- | --- | --- | --- |
| Feeling sick or being sick | Chest pain: call 999 | Heart attack: call 111 | 999 |
| Heart beating very fast | Pulmonary embolism: 999 or A&E | Heart attack: call 111 for a racing heart | 999 or A&E |
| Pain that comes and goes | Angina: get help from 111 | Chest pain: see a GP | 111 (urgent) |

## 3. Rules that rest on an AI reading of the source

- **Chest pain worse when breathing in: urgent.** The Pulmonary embolism page
  lists it as a symptom that needs urgent medical help. The Chest pain page
  links it to a chest strain or chest infection and gives no urgency.
- **Chest pain with pain or swelling in one leg: urgent.** The Shortness of
  breath page says to contact 111 for this. The Pulmonary embolism page lists
  it as a sign of a blood clot. Applying it to chest pain without
  breathlessness is the AI reading.
- **Sudden confusion: emergency, checked in every session.** The source lists
  it for people who are short of breath. Checking it for everyone is the AI
  reading.

## 4. A sourced rule that is likely to over-triage

- **Sore throat and "worried about your symptoms": urgent.** This is taken
  directly from the Sore throat page. Many people using a triage tool would say
  yes. Keep, reword or remove?

## 5. Judgement calls raised by the independent check

An independent check compared the drafted content with the source pages. Its
definite defects were fixed (see DECISIONS.md, items 25 to 29). It also raised
these, which need a clinician:

- **"Heart beating very fast" (999 or A&E) and "heart racing" (111)** are hard
  for a patient to tell apart, so most people with palpitations and chest pain
  will be sent to A&E.
- **"Finding it hard to speak"** will catch simple hoarseness and send it to A&E.
  The source means it as a sign of quinsy.
- **Aspirin advice for chest pain.** The source gives it for a suspected heart
  attack. The drafted advice says so, but has no warning about children under
  16, because the Heart attack page has none.
- **A child under 5 with a sore throat whose carer says they do not want help**
  gets the self-care outcome.
- **"Any other symptoms you're worried about"** is a reason for urgent advice on
  the Pulmonary embolism page. There is no matching chest pain rule.

## 6. Things the test-case authors could not express

The sessions that wrote the test cases saw the source pages and the list of
questions, and reported where the questions could not describe something the
pages mention. Two were fixed (a "heavy" chest, and how difficulty breathing
looks in a child). The rest are listed here for a reviewer to decide whether
any should become a question or a rule.

Chest pain:

- Pain brought on by effort, cold or stress and eased by rest, in someone who
  has not been diagnosed with angina.
- Breathlessness that came on suddenly, as distinct from ordinary breathlessness.
- Pain in the upper back; swelling or colour change in an arm; a recent long
  journey or hospital stay.
- The causes table on the Chest pain page: pain after eating, after injury or
  on movement, triggered by worry, with coloured mucus, with a blistering rash,
  or worse lying down.
- How long an episode lasted.
- Heart risk factors: smoking, blood pressure, cholesterol, family history, weight.
- Signs of a stroke are one combined question, so a partial or less common
  sign cannot be given on its own.

Sore throat:

- Child-specific signs: limp or floppy, or the child form of sudden confusion.
- Whether drooling in an infant is new or ordinary teething.
- A mild temperature, as distinct from a very high one or feeling shivery.
- Swollen glands, as distinct from a lump.
- A sore throat that has improved but not gone after a week.
- Painful swallowing short of being unable to swallow; a hoarse voice as
  distinct from difficulty speaking.
- Pregnancy (for the medicine advice) and smoking.
- What counts as "often" getting sore throats.

## 7. Known gaps

- **Safeguarding** is not screened. The working levels of care have no route
  for a non-medical safety need.
- **Thoughts of suicide without immediate risk** are not screened. Only serious
  self-harm, or feeling about to self-harm, is treated as an emergency.
- **Children.** Questions are worded for an adult answering for themselves. The
  sources give some different signs for children (for example for breathing
  difficulty). These are not yet included.
- **Pregnancy, frail older adults and people with a weakened immune system**
  are planned for a later wave, apart from the one sore throat rule on a
  weakened immune system.

## 8. Everything about possible causes is AI judgement

The condition cards in `knowledge_base/conditions/` hold how common each possible cause is and
how strongly each finding points to it. None of it is sourced. It is used only
to choose which question to ask next. It never sets an outcome and is never
shown as a diagnosis.

## 9. Source pages past their own review date when accessed

- Chest pain (review was due August 2026)
- When to call 999, and When to go to A&E (review was due February 2026)
