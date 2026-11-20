# Design: a full condition network

Draft for the owner, 18 November 2026. Not yet agreed. Not for clinical use.

## 1. The aim

Turn the engine into a decent proxy for a commercial condition-based triage
engine, covering the full range of conditions a triage service sees, so it
can be used to learn how engines of that kind behave under evaluation.

It is a mock-up. It will never be used clinically. Where no better figure
exists, AI best judgement is used and labelled as such. The aim is a sound
design and realistic behaviour, not clinical precision.

What is matched is the general **architecture** of such engines, as described
in public developer documentation. No product's medical content is used.

## 2. How condition-based engines are typically built

- **Scale:** many hundreds of conditions and a few thousand symptoms and risk
  factors, written by doctors over many years.
- **Three kinds of concept:** symptoms, risk factors and conditions, in one
  shared network. Any symptom can be the starting point.
- **Symptoms form a hierarchy.** Each child has one parent and a relation to it:
  duration, severity, character, exacerbating factor, diminishing factor,
  location or radiation. Reporting a child adds its parent. A parent reported
  absent stops questions about its children. Each symptom has a question for
  the patient and one for a third person (a carer), and a sex filter.
- **Risk factors** (chronic conditions, lifestyle, places, events) change the
  starting likelihood of conditions. Age and sex are added automatically.
- **Conditions** have a prevalence band (very rare, rare, moderate, common),
  acuteness (acute, chronic and so on), severity (mild, moderate, severe),
  categories, and optionally an ICD-10 code and a triage level.
- **The interview** is stateless: the caller sends all evidence each turn. Each
  answer is present, absent or unknown. The engine returns the next question,
  a ranked list of conditions, whether there is emergency evidence, and a
  recommendation to stop.
- **Why a question was asked** is explained with a code: most statistically
  useful; a rule set by medical experts; a key symptom of a probable
  condition; an observation required for a probable condition; a risk factor
  that could change things a lot; or the most important observation related
  to what was just said.
- **Triage** gives five levels (ambulance, emergency department, see a doctor
  within 24 hours, see a doctor, self-care) and a root cause (emergency
  evidence present, serious evidence present, emergency condition likely or
  possible, consultation condition likely, self-care sufficient, diagnosis
  unknown). It uses both likely conditions and alarming symptoms, and "triage
  tuples" can raise the level when two findings appear together.

## 3. Where we are, and the gap

| | A typical commercial engine | This engine today |
| --- | --- | --- |
| Structure | One shared network | One module per main symptom |
| Conditions | Many hundreds | 13 |
| Symptoms and risk factors | A few thousand | 61 |
| Symptom hierarchy | Yes | No (flat yes/no questions) |
| Question types | Yes/no, choose one, choose any | Yes/no, choose any (checklists) |
| Conditions shared across symptoms | Yes | No |
| Third-person questions (for carers) | Yes | No |
| Why a question was asked | Coded | Free text |
| Triage from conditions and alarming symptoms | Yes | Yes |
| Sourced red-flag floor (NHS pages) | Rules set by experts | Yes, firm rules |

Much of the engine's reasoning already matches (danger-based triage, firm
rules, lowering with evidence, stateless sessions). The main changes are the
knowledge structure and the scale of content.

## 4. Architecture

### 4.1 One knowledge network

Replace the per-symptom modules with one network of concepts and links.

**Observations** (symptoms and risk factors), one file per body system:

- id, plain label, question for the patient, question for a carer
- kind: symptom or risk factor
- parent and relation (for example "severe headache" is a child of "headache",
  relation: severity)
- filters: sex, age range
- seriousness: normal, serious, emergency or emergency-ambulance, from the NHS
  page that names it. This replaces hand-built red-flag lists.
- SNOMED CT code, checked and logged
- source

**Conditions**, one card per condition, in folders by body system:

- id, plain name, medical name, SNOMED CT code
- body system and categories
- prevalence band by age band and sex
- acuteness and severity, which give the danger class and the acuity needed
- the observations that go with it, each with how often it is present (a band),
  and which are **key** (ask if the condition is probable) or **must-ask**
- risk factors that make it more likely, each with a strength band
- source: the NHS condition page, plus any research cited

**Rules**, which stay as the firm floor:

- red flags and other rules from NHS pages, as now
- **combinations** (sometimes called tuples): two findings together that
  raise the level, for example a head injury and blood-thinning medicine
- defaults by entry symptom, where the source sets one (for example "get
  medical advice" for any chest pain)

### 4.2 Inference

- **A single main cause**, with a "something not on the list" option, as now.
  This is a standard choice for symptom checkers. It assumes one condition
  explains the symptoms. It handles two unrelated problems poorly, which
  matters less for triage than for diagnosis.
- **Only conditions linked to the evidence are scored**, so the work grows
  with the size of the case, not the size of the network.
- **The hierarchy is used in reasoning.** A child symptom implies its parent. A
  parent reported absent rules out its children.
- **Related findings count as one piece of evidence**, as now.
- Kept behind one small interface, so a different method (for example one
  that allows several causes at once) can be tried later and compared.

### 4.3 Triage

Kept as now: the outcome is the most urgent of firm rules, the level the
likely conditions call for (by danger class), and soft rules each lowered only
on their own evidence. Added:

- **Seriousness of observations.** Any serious or emergency observation
  reported sets a floor, as "emergency evidence" does in such engines.
- **Combinations**, as above.
- **A five-level output alongside ours, in the common shape:** the five-level triage, the
  root cause code, and the list of serious evidence. This makes side-by-side
  comparison with condition-based engines direct.

### 4.4 The interview

- **Any symptom can be the starting point.** No modules.
- **Three question types:** yes/no; choose one (for example how long it has
  lasted, using the hierarchy's duration children); choose any (checklists).
- **Red-flag checklists are generated,** not hand-built. They are made from the
  serious and emergency observations linked to the conditions in play, most
  serious first, and kept short. This also addresses the reading burden found
  in the last review: a checklist only shows items relevant to this patient.
- **Next question:** first any red-flag checks, then key and must-ask
  observations of probable conditions, then the observation most likely to
  change the triage outcome (weighted by danger, as now).
- **Every question carries a reason code**, as such engines give, plus plain
  words.
- **Stopping:** when no answer is likely to change the outcome, or at the
  limit (red flags excepted).
- **Carer mode:** questions in the third person when someone answers for
  another person.

### 4.5 Performance

With hundreds of conditions, the engine needs indexes (observation to
conditions, condition to observations) and caching within a turn. A target of
under 200 milliseconds per turn on a laptop is realistic. Determinism stays a
fixed rule.

## 5. Building the content with AI

### 5.1 Scope

- **Conditions:** start from the NHS website Health A to Z (about 1,000 pages,
  Open Government Licence). Keep the conditions a triage service would see.
  Expect 600 to 900.
- **Symptoms:** the NHS Symptoms A to Z (129 pages) gives the entry points.
  Further observations come from the condition pages.
- **Body systems** organise the work, about 12 batches: chest and heart;
  breathing; ear, nose and throat; stomach and bowel; urinary; skin; bones,
  joints and muscles; brain and nerves; eyes; mental health; women's health
  and pregnancy; children and babies; infections and general.

### 5.2 The pipeline for each batch

1. **Fetch and snapshot** the NHS pages, and log them.
2. **Draft** the condition cards and observations: separate AI agents work in
   parallel, each on a few conditions. Every field is sourced, or marked AI
   judgement.
3. **Check SNOMED codes** by script against the NHS SNOMED CT browser. Only
   logged codes are accepted (as now).
4. **Machine validation** when the network loads:
   - references and bands are valid
   - plain-language rules are met
   - the network makes sense: no orphan observations; every condition reachable
     from at least one entry symptom; every serious observation has a question;
     no duplicate concepts (same SNOMED code)
5. **Independent check:** a separate agent compares each card with its source
   page, looking for missed red flags and wrong urgency.
6. **Self-tests:** a textbook patient built from each card should rank that
   condition highly and get at least the urgency it needs. This is circular,
   but it cheaply catches broken links.
7. **Independent test cases** (section 6).
8. **Review pack** for the batch.

### 5.3 The hardest part: the numbers

How common each condition is, and how strongly each symptom points to it, are
the weakest part. The NHS pages give almost none of them. The approach:

- coarse bands, never precise figures
- anchored to public UK data where it exists and its licence allows (for
  example published hospital and GP activity statistics), cited
- otherwise AI best judgement, labelled
- **calibration:** the evaluation shows where the engine is systematically off
  (for example a condition ranked too low across many cases), and the bands are
  adjusted against the development cases only, never the holdout set

## 6. Testing and validation

### 6.1 Layers

| Layer | What it checks | When it runs |
| --- | --- | --- |
| Engine properties | Determinism, adding danger never lowers, floors hold, red flags never cut off, "not sure" never blocks, hierarchy logic | Every change |
| Network validation | References, bands, sources, SNOMED, plain language, network sense | Every load |
| Self-tests | Each condition recognisable from its own card | Every content change |
| Independent test cases | Triage gates and scores | Each batch; holdout once per release |
| Diagnostic ranking | Is the right condition in the top 3? Is a must-not-miss condition in the top 5? | With the test cases, reported separately, never a gate |
| Published sets | Outside sense check | Each release |
| Comparators | Rules only, ask-everything, LLM-only (once a provider is agreed) | Each release |
| Stress runs | Noisy patient, few negatives stated, "not sure", carers, ages | Each release |
| Clinical review | Sampled | As reviewers allow |

### 6.2 Independent test cases at scale

- **Engine-agnostic format:** plain facts plus SNOMED codes, not this engine's
  question ids. A separate adapter maps facts to an engine's questions; a fact
  with no match is "not stated", not "no". This lets other engines be run on
  the same cases, which is the point of the evaluation.
- **About 3 per condition plus every entry symptom**, so 2,000 to 3,000 in all.
  They are written by separate agents that see only the NHS pages and the
  format, never the network.
- **Each case states its key findings and critical negatives,** so the route
  can be scored: did the engine ask what mattered?
- **The holdout set is fixed when written** and run once per release.
- **Independence is limited:** the same AI writes content and cases. External
  sets and, later, cases from a different model or from people are the
  checks on that. Every report says so.

### 6.3 Regression and releases

- Every change runs the full suite.
- A **difference report** lists every case whose outcome changed and why.
- Releases are versioned. Reports are stamped with the date, versions and
  commit (as now).

### 6.4 Clinical review

Reviewing 900 cards in full is not realistic without a team. Proposed:

- review all **critical** conditions and all red flags first
- then a random sample from each body system
- record review status on each card
- report which outcomes rest on unreviewed content

## 7. Build plan

| Phase | What | Done when |
| --- | --- | --- |
| 1. Engine | Rebuild the engine on the network model, with today's two symptoms moved across | All current tests pass and outcomes match today's |
| 2. Tools | Card format, validators, SNOMED checker, network checks, generated checklists and review packs, engine-agnostic case format and adapter | One condition can go through the whole pipeline |
| 3. Pilot | One body system (chest and breathing: about 40 conditions, 8 entry symptoms), end to end | Gates and scores reported; cost and time per condition measured |
| 4. Scale | The other body systems in batches, agents in parallel | Each batch passes its gates and has a review pack |
| 5. Interfaces | Five-level output, API, demo page, language layer | The evaluation harness can drive it turn by turn |

The pilot is the key step. It shows what each condition really costs in time
and checking, before committing to all of them.

## 8. Decisions for the owner

1. **Replace the per-symptom modules with one network** (a major brief
   change). Recommended.
2. **Keep the NHS-sourced red flags as a firm floor.** Recommended: it is
   close to the "rules set by medical experts" and "emergency evidence" of
   such engines, and it keeps the engine safe while the numbers are rough.
3. **Allow published research and public statistics** as sources for the
   numbers, with citations, alongside AI judgement.
4. **Relax the rule that new content waits for a clinician** to review a Wave 0
   pack. At this scale it would stop the build. Instead: review status is
   recorded per card and reported.
5. **The single-main-cause model** as the starting point. Recommended.
6. **Cost:** this is a large amount of AI work: thousands of drafting,
   checking and case-writing runs. The pilot will measure it before the
   rest is started.

## Sources

- Public developer documentation of commercial condition-based triage engines
  (accessed 18 November 2026)
