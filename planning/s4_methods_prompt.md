# S4 Methods Pass — process the 11 Chapter 3 method sources

**Purpose:** verify, create one NotebookLM notebook each, run the queries below, write raw answers and notes into the repo — as in S5.
**Model:** Sonnet. **Created:** Sep 30, 2026. **Status:** not yet run.
**Precedent:** `planning/s5_addref_prompt.md` (S5). Everything there on delivery, persistence, Step 0 and the fabrication guard applies. Differences are below.
**Read first:** `planning/query_template_v2.4.md`, `planning/naming_convention.md`, `literature/search_log.md` §S4, `research-design/interview_protocol_v0.98.md` §0 and §10, `analysis/templates/codebook_v0.md`.

---

## The 10 sources — proposed IDs (a plan, not a record)

Bib entries **already exist** in `literature/references.bib` (added Sep 30, `TODO-verify`). Update them in place; no duplicates. PDFs go in `D:\Master\Thesis\Thesis Content\Group M\` (**new folder**, Albert downloads via Aalto library).

| ID | Bib key | Source | Focus for §13 |
|---|---|---|---|
| **M2** | `braun2021onesize` | Braun & Clarke (2021) | **PROCESS FIRST** — see "M2 first" below |
| M1 | `braun2006thematic` | Braun & Clarke (2006) | the six phases; what a theme is; inductive vs theoretical TA; semantic vs latent |
| M3 | `fereday2006hybrid` | Fereday & Muir-Cochrane (2006) | how a priori codes and data-driven codes are combined; the codebook's role; the stages |
| M4 | `gremler2004cit` | Gremler (2004) — **replaces Flanagan** | definition of a critical incident; Flanagan's original procedure as Gremler reports it; what a CIT study should report; how CIT is used in business/service research |
| M5 | `butterfield2005cit` | Butterfield et al. (2005) | how CIT moved from task analysis to qualitative interviewing; credibility checks proposed for CIT |
| M6 | `baxter2008casestudy` | Baxter & Jack (2008) — **replaces Yin** | single vs multiple, holistic vs embedded designs; binding the case; units of analysis; how it reports Yin's typology (record which Yin edition it cites) |
| M7 | `nowell2017trustworthiness` | Nowell et al. (2017) | credibility, transferability, dependability, confirmability as applied at each TA phase; audit trail |
| M8 | `malterud2016informationpower` | Malterud et al. (2016) | the five information-power dimensions; how each moves the needed sample size |
| M9 | `temple2004translation` | Temple & Young (2004) | the researcher-as-translator position; whether and how to report translation; epistemological claims |
| M10 | `dwyer2009insider` | Dwyer & Buckle (2009) | insider vs outsider; the "space between"; what the researcher should disclose |
| M11 | `eisenhardt2007theorybuilding` | Eisenhardt & Graebner (2007) | why multiple cases; replication logic; theoretical sampling; how to present evidence across cases |

**Not obtained — do not process:** `flanagan1954cit` (cite only "as cited in Gremler, 2004"), `yin2018casestudy`. Do not create notebooks for them.

Next free IDs checked Sep 30: Cluster M does not exist yet (M1–M11 free). Cluster M = "Methods foundation", outside the §11 denominator. Re-check `literature/notes/` and bib keywords before writing.

## Variant — v2.4-T with a methods role

- **Query 1:** §1–§6 as in `query_template_v2.4.md`, plus the zh-TW summary.
- **Query 2:** §7–§10, then **§13 THESIS ANCHOR** (wording in `planning/s5_addref_prompt.md`) with **[ROLE] = "Chapter 3 method anchor"** and the focus line above. **Do not run §11** (not governance literature) **or §12** (not an interview-design precedent).
- Add to §13 one extra point for every source: **(f) What would a careful examiner expect a thesis citing this source to have done?** — answer only from the document.

## M2 first — the analysis label decision

The thesis codes with an a priori spine (structural / procedural / relational), secondary seed codes, and inductive codes, in a codebook (`analysis/templates/codebook_v0.md`), solo, with re-coding after an interval and a supervisor spot-check (protocol §10). After M2's two queries, **stop and report to Albert**:

1. How M2 distinguishes coding-reliability, codebook and reflexive TA — verbatim definitions with pages.
2. Which family the thesis's procedure falls into, judged against those definitions. Name each feature that decides it (a priori codes, codebook, re-coding for consistency, supervisor check).
3. What M2 says researchers most often get wrong when they claim reflexive TA (verbatim, with pages).
4. The one-sentence label Chapter 3 should use, and what the thesis would have to change to claim the other label instead.

Then continue with the other ten.

## Fabrication guard (same as S5)

Verbatim quotes only for definitions, limitations and anything in §13(e)–(f); each checked against the PDF page. "None stated" and "not addressed" are fine. Drop anything you cannot find in the PDF and say so.

## Naming

```
M1_braun2006_using_thematic_analysis.md
M2_braun2021_one_size_fits_all.md
M3_fereday2006_hybrid_inductive_deductive.md
M4_gremler2004_critical_incident_technique.md
M5_butterfield2005_fifty_years_cit.md
M6_baxter2008_qualitative_case_study.md
M7_nowell2017_ta_trustworthiness.md
M8_malterud2016_information_power.md
M9_temple2004_translation_dilemmas.md
M10_dwyer2009_insider_outsider.md
M11_eisenhardt2007_theory_building_cases.md
```

Notebook names: `[M2] Braun2021 — One Size Fits All` style, one PDF per notebook.

## After compile

- Update the eleven bib entries in place; remove `TODO-verify` only after the PDF check.
- `literature/reference_list.md`: move Cluster M rows to ✅ and fix the summary counts.
- `literature/search_log.md` §S4: append a verification line per source.
- `planning/Pipeline_State.md`: new Cluster M (11; Flanagan and Yin not obtained), the M2 label decision, and "Chapter 3 methods foundation: in place".
- Re-list `literature/notes/` and `literature/_raw/` as evidence. Do not commit or push.

---

## Copy-paste prompt for the Sonnet session

```
Read planning/s4_methods_prompt.md in my repo first, then planning/s5_addref_prompt.md (the
precedent), planning/query_template_v2.4.md, planning/naming_convention.md and
literature/search_log.md section S4.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). The Cowork shell cannot mount my folders -- use the
file listing/staging/commit tools. NotebookLM is available via the notebook MCP; if auth is
stale I'll run `nlm login`. Do not commit or push; I push myself.

The 11 PDFs are in a new folder Thesis Content\Group M. Flanagan and Yin were not obtained --
Gremler (M4) and Baxter & Jack + Eisenhardt & Graebner (M6, M11) replace them.

STEP 0: one notebook per PDF, ask each for its source's printed title and authors, match to the
PDFs, and send me the ID table for approval BEFORE writing anything.

Process M2 (Braun & Clarke 2021) FIRST, then STOP and give me the analysis-label report
described in the prompt file (codebook vs reflexive TA, judged against my procedure in
research-design/interview_protocol_v0.98.md section 10 and analysis/templates/codebook_v0.md).

All eleven use variant v2.4-T: Query 1 as normal, Query 2 = sections 7-10 then section 13 THESIS
ANCHOR with role "Chapter 3 method anchor", the per-source focus line, and the extra point (f).
Do NOT run section 11 or section 12.

Write every answer to literature/_raw/<ID>.md the moment it returns (Q1 written, Q2 appended).
Definitions, limitations and (e)/(f) answers: verbatim quotes only, each checked against the PDF
page. Do not supply anything you cannot find in the PDF.

Then PAUSE -- I will ask my own questions in each notebook before you compile.

When I say "compile": write the eleven notes, update the eleven existing bib entries in place, update
literature/reference_list.md, append per-source lines under S4 in literature/search_log.md,
update planning/Pipeline_State.md, and finish by re-listing literature/notes/ and literature/_raw/.
```
