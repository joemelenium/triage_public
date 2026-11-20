# External vignette sets

Published vignette sets used, or considered, as an outside sense check on the
triage engine. They were written by other people for other purposes. Results on
them are reported separately from the project's own vignettes.

This is a personal, non-commercial project. Not for clinical use.

All access below was on **2026-11-18**. Licences were read from the
publications themselves and are quoted exactly. Nothing here is taken from
NICE, CKS or BNF.

| Set | Licence found | Vignettes obtained | Converted |
|---|---|---|---|
| 1. Semigran 2015 (45 vignettes) | CC BY-NC 4.0 (article) | Yes, all 45 | Yes, 45 files |
| 2. El-Osta 2022 (139 RCGP vignettes) | CC BY-NC 4.0 (article) | **No. Not published with the paper** | No |

---

## 1. Semigran 2015

**Citation.** Semigran HL, Linder JA, Gidengil C, Mehrotra A. Evaluation of
symptom checkers for self diagnosis and triage: audit study. BMJ
2015;351:h3480. doi:10.1136/bmj.h3480. PMID 26157077. PMCID PMC4496786.

**URLs used.**

- PubMed Central article page: <https://pmc.ncbi.nlm.nih.gov/articles/PMC4496786/>.
  From here this address returned a reCAPTCHA challenge page instead of the
  article, so the page itself could not be read. The challenge was not worked
  around.
- The same PubMed Central record (version PMC4496786.2), read through NCBI's
  public E-utilities service, which is where the licence statement below was
  taken from:
  <https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4496786>
- The supplementary file, from Europe PMC's public web service (Europe PMC
  mirrors the PubMed Central record):
  <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4496786/supplementaryFiles>.
  This returns a zip holding one file, `semh025489.ww1_default.pdf`
  ("Appendix: supplementary information", 19 pages, 737,973 bytes, SHA-256
  `5ab6ab7bf6f9b282cea56f1101bf497625ec1300131a2a7a166fb6f21bfa6558`). The file
  name is the one given in the PubMed Central record.
- The publisher's site (bmj.com) was not used. It returns 403 from here.

**Date accessed.** 2026-11-18.

**Licence.** CC BY-NC 4.0 (Creative Commons Attribution Non Commercial 4.0).

**Licence statement, quoted exactly from the PubMed Central record.**

> This is an Open Access article distributed in accordance with the Creative
> Commons Attribution Non Commercial (CC BY-NC 4.0) license, which permits
> others to distribute, remix, adapt, build upon this work non-commercially,
> and license their derivative works on different terms, provided the original
> work is properly cited and the use is non-commercial. See:
> http://creativecommons.org/licenses/by-nc/4.0/.

Copyright statement in the same record: "© Semigran et al 2015".

**Were the vignettes obtained?** Yes. All 45 are in Supplemental Table 2 of the
appendix ("The 45 standardized patient vignettes used to judge the symptom
checkers’ accuracy and their condensed formats"), in three groups of 15:
"Requires emergent care", "Requires non-emergent care" and "Self-care
appropriate". Each row gives a diagnosis, the vignette, and a simplified
version that the authors typed into the symptom checkers.

**Two things about the licence that are not settled, stated plainly.**

1. The licence statement is the article's. The appendix PDF carries no licence
   statement of its own. The PubMed Central record lists it under "Extra
   material supplied by the author". It is treated here as part of the article.
2. The authors did not write most of the vignettes. The appendix says they were
   "gathered from several sources" and lists them: Epocrates (2014); an NYU
   Medical Grand Rounds clinical vignette (Lue, 2012); Halm and Teirstein,
   N Engl J Med 2002;347:2039-2045; Plantz and Adler (eds), NMS Emergency
   Medicine (1998); Gidengil et al. (listed as "In review"); Sirovich et al.,
   Arch Intern Med 2005;165:2252-2256; and Boroughs et al., "Telephone Triage:
   Help Is Just a Call Away" (nurse.com). Whether the article's CC BY-NC
   licence covers wording that came from those sources was **not confirmed**
   from the publication, one way or the other. Each converted file names the
   source the publication gives for that vignette.

The article also says: "Data sharing: No additional data available."

**How the material is used here.** As an outside sense check on the triage
engine, reported separately from the project's own vignettes. Non-commercial.
non-commercial. Attribution is carried in every file (`citation`, `licence`,
`set`). The published wording is copied unchanged into `original_text`; all
other fields are this project's own additions, and every file is marked
"Published vignette, converted by AI, not clinically approved in this form".

**What was converted.** 45 files, `vignettes/external/semigran2015_01.yaml` to
`semigran2015_45.yaml`, numbered in the published order (01-15 emergent, 16-30
non-emergent, 31-45 self-care).

- `original_text` is the "Vignette" column, taken from the PDF by program and
  not retyped. It was checked against a second reading of the PDF with a
  different tool: 42 of 45 match exactly (ignoring spaces). In the other three
  (04, 43, 44) the diagnosis label is printed over the first few characters of
  the vignette in the PDF; those openings were checked by hand, character by
  character. The "Simplified (added symptoms)" column is not copied.
- A few vignette cells end with a remark by the study authors (for example a
  Centor score, or "in study 50% recommended physician visit"). These are part
  of the published cell and are kept. The file's notes say so.
- Triage mapping:

  | Published heading | `original_triage` |
  |---|---|
  | Requires emergent care | `emergency` |
  | Requires non-emergent care | `non_emergency` |
  | Self-care appropriate | `self_care` |

  The article describes the three groups as vignettes "for which emergent care
  is required", "for which non-emergent care is reasonable", and "for which a
  medical visit is generally unnecessary and self care is sufficient". When
  scoring symptom checkers it counted advice "to call an ambulance, go to the
  emergency department, or see a general practitioner immediately" as emergent,
  and advice "to stay at home or go to a pharmacy" as self care.
- Presenting symptom on the question list: 8 of 45. Chest pain in 3 (06 heart
  attack, 12 pulmonary embolism, 28 shingles). Sore throat in 5 (17, 18, 24,
  34, 44). The other 37 have `presenting: []` and a plain-words
  `presenting_text`.
- Findings use only ids from `harness/vignette_authoring/question_list.yaml`,
  and only where the text states or rules out the finding. `unknown` is left
  empty throughout. Choices that a reviewer may want to look at:
  - Fever. The question asks about "a very high temperature, or ... hot, cold
    or shivery". It is marked present when the text states a fever that is not
    described as low-grade, or chills, rigors or feeling hot (14 files); left
    out when the fever is described as low-grade or measured below 38.0 C
    (04, 21, 27, 45); absent when fever is explicitly ruled out (8 files).
  - "Shortness of breath" and "dyspnea" are mapped to `short_of_breath` only,
    not also to `difficulty_breathing`.
  - Examination values such as a fast heart rate are not turned into symptoms.
    Enlarged neck lymph nodes are not mapped to `lump_in_mouth_or_neck`.
  - "Otherwise healthy" or "no significant past medical history" is mapped to
    `weakened_immune_system` absent (6 files).
  - Two patients are infants. Age is recorded in years as a number: 1.5 for
    "18-month-old" (16) and 0.42 for "5-month-old" (40).
  - In 15 (tetanus) the vignette says 63 years and the simplified column says
    65. The vignette's 63 is used.
- The vignettes are American and were written for clinicians. Many include
  examination findings and test results that a member of the public could not
  report. Most are not about chest pain or sore throat.

---

## 2. El-Osta 2022 (RCGP vignettes)

**Citation.** El-Osta A, Webber I, Alaa A, Bagkeris E, Mian S, Taghavi Azar
Sharabiani M, Majeed A. What is the suitability of clinical vignettes in
benchmarking the performance of online symptom checkers? An audit study. BMJ
Open 2022;12:e053566. doi:10.1136/bmjopen-2021-053566. PMID 35477872. PMCID
PMC9047920. (A correction, BMJ Open 2022;12:e053566corr1, PMCID PMC9296873,
retracts one sentence of the Discussion and does not concern the vignettes.)

**URLs used.**

- Finding the PubMed Central copy:
  <https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=10.1136%2Fbmjopen-2021-053566%5Bdoi%5D&retmode=json>
  and
  <https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id=12551931,9296873,9047920&retmode=json>
- The PubMed Central record (PMC9047920), read through E-utilities:
  <https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9047920>
- The correction (PMC9296873):
  <https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9296873>
- The supplementary files, from Europe PMC:
  <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9047920/supplementaryFiles>
- The article's page on the PubMed Central website would be
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC9047920/>. It was not requested,
  because the PubMed Central website answered the first set's page with a
  reCAPTCHA challenge. bmjopen.bmj.com was not used (403 from here).

**Date accessed.** 2026-11-18.

**Licence.** CC BY-NC 4.0 (Creative Commons Attribution Non Commercial 4.0).

**Licence statement, quoted exactly from the PubMed Central record.**

> This is an open access article distributed in accordance with the Creative
> Commons Attribution Non Commercial (CC BY-NC 4.0) license, which permits
> others to distribute, remix, adapt, build upon this work non-commercially,
> and license their derivative works on different terms, provided the original
> work is properly cited, appropriate credit is given, any changes made
> indicated, and the use is non-commercial. See:
> http://creativecommons.org/licenses/by-nc/4.0/.

Copyright statement in the same record: "© Author(s) (or their employer(s))
2022. Re-use permitted under CC BY-NC. No commercial re-use. See rights and
permissions. Published by BMJ."

**Were the vignettes obtained?** **No. The 139 vignettes are not published
with the paper.**

- The only supplementary data file, `bmjopen-2021-053566supp001.pdf` (3 pages),
  holds five tables of scoring patterns and agreement statistics. It contains
  no vignette text and no per-vignette triage categories.
- The paper's data availability statement reads, in full: "No data are
  available."
- The published peer review file shows a reviewer asking for the vignettes to
  be supplied as a supplement. They were not added. The authors' reply quotes
  one vignette as an example. That single example was not converted.
- The other files attached to the record are the figures, the reviewer
  comments and the authors' draft manuscript. None holds the set of vignettes.
- The paper's Table 1 gives only counts: 139 vignettes across 18 subcategories
  of clinical care, with RCGP triage recommendations of self-care 22, seek
  primary care 85 (in 14 days 29, in 48 hours 28, in 12 hours 28) and seek
  urgent care 32 (attend emergency 17, call ambulance 15).

**How the material is used here.** It is not used. Nothing was converted and
no vignettes were reconstructed from memory or from the paper's description.
The licence of the article is confirmed, but that does not help, because the
vignettes themselves are not in the article or its supplements. Using this set
would mean getting the vignettes from the authors or from the RCGP, with their
terms.

---

## What is stored in this repository

Decision made after the conversion above (see DECISIONS.md):

- **The published wording of the vignettes is not stored.** The project brief
  says not to copy text from journal papers, and it is not confirmed that the
  article's licence covers wording the authors gathered from third parties.
- **What is stored for each vignette:** its number in the publication, the
  published diagnosis and triage category, a few words describing the main
  complaint, the age and sex, and which questions on this project's question
  list the published text answers. These are facts about the published case,
  not its wording.
- To read a vignette in full, use the supplementary appendix of the cited
  article.
