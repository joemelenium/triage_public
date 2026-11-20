# Instructions: drafting condition content

You are drafting content for a mock triage engine modelled on commercial
condition-based engines. It is a demonstration and proof of concept for
testing an evaluation. It will never be used clinically. The aim is a capable,
realistic engine, so use good clinical knowledge.

## What you are given

- A body system and a list of conditions and entry symptoms to draft.
- Saved source pages in `sources/nhs_uk/`.
- The current network in `knowledge_base/`. Read `README.md` first, then the
  existing files, so you reuse observations rather than duplicate them.

## What to write

1. **Condition cards**, one file each: `knowledge_base/conditions/<body system>/<id>.yaml`.
   Copy the shape of an existing card. For each condition give:
   - `name` in plain words first (with the medical term in brackets if useful),
     and `medical_name` if it differs.
   - `entry_symptoms`: every main symptom that should make it a candidate.
     A condition can belong to several.
   - `acuity_needed`: the level of care it needs (from `settings.yaml`).
   - `danger`: critical (life-threatening if missed), serious (real harm if
     missed or delayed), moderate (needs seeing, little harm from a short
     delay) or minor (usually gets better on its own).
   - `prevalence` among people presenting with its entry symptom, as a band,
     and `prevalence_when` for age, sex or risk factors that change it.
   - `findings`: the observations that go with it, each with how often someone
     with the condition has it (`strongly_supports` about 80%, `supports` about
     50%). Include enough to tell it apart from look-alikes: aim for at least
     four. Use `argues_against` sparingly: the default inference method ignores
     it, so prefer linking to the opposite observation.
   - `key_findings`: the observations most worth asking about if it becomes
     probable.
   - `diagnosed_by` if there is an observation for already having the diagnosis.
   - `snomed`, checked with the SNOMED tool (see below).
   - `source`: a source id if a page or paper backs the card, otherwise
     `ai_judgement`. `informed_by`: the pages you read.

2. **Observations** in `knowledge_base/observations/<body system>.yaml`, only
   where none already exists. Each needs a plain `label`, a `question` for the
   patient, a short `checklist_text` if it may appear in a checklist, and a
   `source`. Use `parent` and `relation` for a more specific version of an
   existing observation (for example severity or duration). Set `seriousness`
   where a source names it as an alarming sign. Add `question_carer` where the
   question reads oddly when answered for someone else. Use `sex` and
   `asked_only_if` where they apply.

3. **Entry symptom files** in `knowledge_base/entry_symptoms/` for any new main
   symptom: the red flags and other rules from the NHS page, the checklists
   (emergency level first), the default outcome (`floor: true` if the source
   says everyone with this symptom should get at least that care), and soft
   rules where sources disagree or a rule rests on a reading of the source.
   Copy the shape of `sore_throat.yaml`.

4. **Advice** in `knowledge_base/advice/<body system>.yaml` for any new outcome: what to do,
   what to look out for, when to get more help, where to go.

## Checking your work

- SNOMED CT: `python triage.py snomed-search "term"` to find a concept, then
  `python triage.py snomed-add CODE` to check and log it. Use a code only when
  the concept means the same as the observation or condition. Never type a
  code from memory without checking it.
- `python triage.py check` must load with no problems. Fix every problem it
  reports. Look at its warnings too.
- `python triage.py selftest` should pass for your conditions.

## Do not

- Read anything in `vignettes/` or `reports/`.
- Copy text from NICE, CKS or the BNF.
- Change engine code, settings, or content outside your batch, except to reuse
  or extend shared observations.
- Commit. Report back what you added, anything you were unsure of, and any
  warning you could not resolve.
