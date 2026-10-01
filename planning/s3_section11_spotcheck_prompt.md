# S3 §11 spot-check — brief

**Purpose:** check the §11 WORKING-TIER RECEPTION verdicts of the S3 notes against their PDFs, so that the Chapter 2 tally (2.6 ¶2: **23–25 of 36, 64–69%**) rests on PDF-verified verdicts rather than NotebookLM answers.
**Model:** Opus. Recoding a verdict is a judgement call; quote matching alone is not enough. **Created:** Oct 1, 2026 (orchestration session). **One session**, about 12 notes.
**Why now:** two of the S3 notes (Sep 11 gap-fill) had invented Query-2 content (§7–§11) while their Query-1 content (§1–§6) was accurate:
- **D7 Rakova:** invented limitations and readiness model (`planning/s3_postcheck_2026-09-11.md` §3).
- **D6 Lu:** invented champion pattern and section structure (`planning/d6_pdf_check_2026-10-01.md`). D6 was recoded to documented absence on Oct 1, which moved the tally from 22–24 to 23–25.

The same failure in any other S3 note would make the tally wrong in a way an examiner can check. Chapter 3.7 already states that every quotation, page and metadata item was checked against the PDF; this pass makes that true for the §11 verdicts.

---

## Read first (in this order)

1. `planning/session_handoff_2026-10-01.md` — hard rules (sources, truthfulness)
2. `planning/d6_pdf_check_2026-10-01.md` — **the worked example**: method, claim-by-claim table, §11 re-read, verdict
3. `planning/section11_harvest_prompt.md` — the §11 question (sub-questions a–e) and the verdict vocabulary
4. `planning/Pipeline_State.md` — sections "S5 add-reference pass" and "§2.5 source pre-check": how the tally is built and which notes sit where
5. `chapters/ch2/2.6_lens_and_gap.md` ¶2 and `chapters/ch3/3.7_literature_review_method.md` ¶2 — how the tally and its range are stated (the range = **C7 and C8**, two conceptual audit papers that could be coded either way)

## Settled — do not reopen

RQ v2.1; the §11 question and its three-value vocabulary (substantive / partial / documented absence); the denominator (36 governance notes; Cluster M, I, G, E5 and E6 outside it); B9 positive; A9 partial (PDF-checked Sep 30); D6 documented absence (Oct 1); D7's reading in s3_postcheck §3.

## Scope

| ID | Note file | PDF (`D:\Master\Thesis\Thesis Content\`) | Current §11 verdict (Pipeline_State) | Priority |
|---|---|---|---|---|
| C10 | `C10_asatiani2020_explaining_blackbox_ai.md` | `Group C\Challenges of Explaining the Behavior of Black-Box AI Systems.pdf` | substantive | **1**. Not-absence; only its 2.5 use is checked (printed = PDF + 258) |
| C7 | `C7_mokander2021_ethics_based_auditing.md` | `Group C\Ethics-Based Auditing of Automated Decision-Making Systems.pdf` | partial (contested, defines the range) | **1** |
| C8 | `C8_raji2020_closing_ai_accountability_gap.md` | `Group C\Closing the AI accountability gap - …pdf` | normative, no field data (contested, defines the range) | **1** |
| A12 | `A12_tallon2013_information_artifact_it_governance.md` | `Group A\The Information Artifact in IT Governance - …pdf` | absence (once named as range-relevant) | **1** |
| B8 | `B8_janssen2025_responsible_governance_genai.md` | `Group B\Responsible governance of generative AI - …pdf` | absence (once named as range-relevant) | **1** |
| A8 | `A8_mantymaki2022_defining_organizational_ai_governance.md` | `Group A\Defining organizational AI governance.pdf` | absence | 2 |
| A10 | `A10_birkstedt2023_ai_governance_themes_gaps.md` | `Group A\AI Governance - Themes, Knowledge Gaps, Future Agendas.pdf` | absence | 2 |
| A11 | `A11_ashok2022_ethical_framework_ai_digital.md` | `Group A\Ethical Framework for AI and Digital Technologies.pdf` | absence | 2 |
| C9 | `C9_shrestha2019_organizational_decision_making.md` | `Group C\Organizational Decision-Making Structures in the Age of AI.pdf` | absence | 2 |
| E2 | `E2_abraham2019_data_governance_conceptual_framework.md` | `Group E\Data governance - A conceptual framework, …pdf` | absence | 2. Known bad quote in §7/§11 ("the actual behavior of individuals" is not in the PDF) |
| E3 | `E3_janssen2020_data_governance_trustworthy_ai.md` | `Group E\Data governance - Organizing data for trustworthy Artificial Intelligence.pdf` | absence | 2 |
| E4 | `E4_zhang2022_risk_aware_ai_ml_systems.md` | `Group E\Towards risk-aware artificial intelligence and machine learning systems - An overview.pdf` | absence | 2 |

**Why the priority order:**
- **Not-absence verdicts first.** If invented content propped one up (as with D6), the tally rises.
- **The contested pair next.** C7 and C8 define the range.
- **A12 and B8** were once named as range-relevant.
- **Absence verdicts last.** They fail in the other direction (a missed positive), which is less likely, but they still need checking.

**Out of scope (log as a possible phase 2, do not run):** the 20 notes of the original Sep 4 harvest (Clusters A1–A7, B1–B7, C1–C3, D1–D5, E1). Their verdicts were read off by the Sep 4 session and are also NotebookLM-derived. Recommend a phase 2 if this pass finds a second recode.

## Procedure per note

1. **Stage** the note, its `_raw/<ID>.md` and the PDF. Extract text with `pdftotext` (raw and `-layout`; two-column layouts break phrases). If a page has no text layer, OCR it (tesseract, 300 dpi). Check figure images by OCR when a claim may sit in a figure. Establish the **printed-page offset** and record it.
2. **Claim table.** For every specific claim in §11 (a–e), and in §3, §5, §7 and §9 where §11 depends on them, search the PDF for the quoted phrase, then key terms:
   - ✅ found on the stated page;
   - ⚠ found, wrong page or reworded;
   - ❌ not in the PDF.
   Also check the §8 snowball items against the reference list. Do **not** search note claims only by surname; check the full title (lesson from the D6 log).
3. **§11 re-read.** Independently of the note, read the parts of the paper that bear on sub-questions a–e (method section, findings, discussion, limitations). Answer each in one line with printed pages. Distinguish *observed* (fieldwork data about staff) from *prescribed* (recommendations, frameworks, literature synthesis). Data reported second hand by managers counts as partial at most, as A9 was coded.
4. **Verdict.** Confirm, or propose a recode, with the evidence that decides it. Apply the same standard used for D6 and A9: **substantive** = the paper reports data on how staff below the rule-setting level receive governance; **partial** = second-hand or very thin data, or the gap is named without study; **documented absence** = prescriptive or design-level only.
5. **Do not edit any note, 2.6, Pipeline_State or the claims map yet.** Write findings to the log (below), report to Albert, and wait. After Albert approves, apply recodes to each note's §11 with a history line, as in the rewritten D6 note.

## Output

`planning/s3_section11_spotcheck_<date>.md`:
- **Summary table:** ID · verdict before → after · decisive evidence (page) · number of ❌ claims · note repair needed (y/n).
- **Per-note block:** offset; claim table; §11 re-read (a–e); verdict reasoning.
- **Tally consequence:** the new point estimate and range out of 36, with percentages rounded to whole numbers, and the exact replacement sentence for 2.6 ¶2 if anything changes. Say whether the "two conceptual audit papers" range still holds (C7, C8), or whether the range has to be restated.
- **Pattern:** whether the failure is confined to Query-2 content, as in D6 and D7. This decides whether phase 2 is needed.

## Hard rules

- No interview content. No new sources. NotebookLM answers are leads, never evidence.
- No verdict changes on the strength of a note or NotebookLM alone; the PDF decides.
- `[UNRESOLVED]` for anything the PDF cannot settle (e.g. a scanned page OCR cannot read). Never smooth it over.
- Re-stage a file before editing it. Never commit or push with git; Albert pushes.

## Delivery

Write the log into the repo with the file-commit tools and re-list `planning/` as evidence. Finish with the summary table and the tally consequence in the reply.

---

## Copy-paste prompt for the new session

```
Read planning/s3_section11_spotcheck_prompt.md in my repo first, then the files it lists under
"Read first", in that order.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). The Cowork shell cannot mount my folders -- use the
file listing/staging/commit tools. Do not commit or push; I push myself.

Task: PDF-check the section 11 working-tier verdicts of the 12 S3 notes in the brief's scope
table, in priority order (C10, C7, C8, A12, B8 first). Use planning/d6_pdf_check_2026-10-01.md
as the worked example. For each note: claim table against the PDF (found / wrong page /
not in PDF), independent re-read for sub-questions a-e with printed pages, verdict confirm or
proposed recode.

Do not edit notes, chapters, Pipeline_State or the claims map. Write the log to
planning/s3_section11_spotcheck_<date>.md, report the summary table and the tally consequence
(new range out of 36, and the replacement sentence for 2.6 paragraph 2 if it changes), and WAIT
for my approval before applying any recode.

NotebookLM content is a lead, never evidence; the PDF decides. Mark anything the PDF cannot
settle as [UNRESOLVED].
```
