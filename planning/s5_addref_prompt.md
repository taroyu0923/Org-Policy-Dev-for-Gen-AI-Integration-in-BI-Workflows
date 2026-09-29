# S5 Add-Reference Pass — process the 6 targeted-search PDFs

**Purpose:** run the 6 sources from search S5 through Literature Review Process v2: verify against PDF and publisher, create one NotebookLM notebook each, run the queries below, write raw answers and notes into the repo.
**Model:** Sonnet. **Created:** Sep 29, 2026. **Status:** not yet run.
**Prerequisite reading:** `planning/query_template_v2.4.md`, `planning/naming_convention.md`, `planning/ch2_targeted_search_2026-09-29.md`, `planning/ch2_claims_map_2026-09-29.md`, `literature/search_log.md` §S5.
**Precedent to follow:** `Claude outputs/s3_gapfill_prompt-1.md` (S3 pass). Everything there about delivery, persistence and Step 0 applies here; the differences are listed below.

---

## The 6 sources — proposed IDs (a plan, not a record)

Bib entries **already exist** in `literature/references.bib` (added Sep 29, status `TODO-verify`). Update them in place after verification; do not add duplicates.

| Proposed ID | Bib key | Source | Group folder | Variant |
|---|---|---|---|---|
| **B9** | `silic2025shadowai` | Silic, Silic & Kind-Trüller (2025), *Strategic Change*, 10.1002/jsc.2682 | `Group B/` | **v2.4 full, with §11** — **PROCESS FIRST** |
| E5 | `ain2019bisuccess` | Ain, Vaia, DeLone & Waheed (2019), *Decision Support Systems* 125, 113113 | `Group E/` | **v2.4-T** (§13, no §11) |
| E6 | `gu2024analystsverify` | Gu, Shang, Althoff, Wang & Drucker (2024), CHI '24, 1–22 | `Group E/` | **v2.4-T** |
| G1 | `haag2017shadowit` | Haag & Eckhardt (2017), *BISE* 59(6), 469–473 | `Group G/` (**new folder**) | **v2.4-T** |
| G2 | `morrison2023voicesilence` | Morrison (2023), *Annual Review of Org. Psych. & Org. Behavior* 10, 79–107 | `Group G/` | **v2.4-T** |
| G3 | `dutton1993issueselling` | Dutton & Ashford (1993), *Academy of Management Review* 18(3), 397–428 | `Group G/` | **v2.4-T** |

**Cluster G is new:** "Organisation theory anchors (non-AI)". Next free numbers checked Sep 29: B9 (B1, B3–B8 exist; B2 retired), E5–E6 (E1–E4 exist), G1–G3 (none exist). Re-check `literature/notes/` and bib keywords for collisions before writing.

**Known metadata gaps:** B9 has no volume, issue or pages in Crossref (online-first, June 24, 2025) — take them from the PDF or the publisher page, or record "advance online publication". G3's volume and pages came from BibBase, not Crossref — confirm against the PDF.

## ⚠ Why two variants — the §11 denominator

The §11 tally (22–24 of 35 governance sources show documented absence) only means something because the denominator is the governance literature.

- **B9 is governance literature** (organisational governance of GenAI / Shadow AI). It gets full v2.4 including §11. Report the tally as **before (35) and after (36)**, never merged silently.
- **E5, E6, G1, G2, G3 are not governance literature.** They are Chapter 1 context (E5, E6) and Chapter 2 theory anchors (G1–G3). Running §11 on them would add false nulls to the denominator. Note: `query_template_v2.4.md` says Clusters A–F run §11 — **this pass overrides that for E5 and E6**, and G is outside A–F. Record the override in each note's header.

## Variant v2.4-T — for E5, E6, G1, G2, G3

- **Query 1:** §1–§6 exactly as in `query_template_v2.4.md`, plus the zh-TW summary.
- **Query 2:** §7, §8, §9, §10 as in v2.4, then **§13 THESIS ANCHOR** below instead of §11. Do not run §11 or §12.

**§13 THESIS ANCHOR — query wording (send as written, with the source's focus line filled in):**

```
§13 THESIS ANCHOR. This source will be used as a [ROLE] in a master's thesis on how
business-intelligence practitioners encounter and act on their organisation's rules for
generative AI. Focus: [FOCUS].
Answer only from the document, each point with section and page:
(a) The source's own definition(s) of the focal concept — quote verbatim.
(b) Its main claims or propositions about the focus — quote or closely paraphrase, marked which.
(c) Mechanisms, conditions or antecedents it names that make the phenomenon more or less likely.
(d) Its evidence base: empirical or conceptual; if empirical, sample, roles, setting, method.
(e) Limitations the authors state themselves — quote verbatim. If none are stated, write
"none stated". Do not infer or supply limitations.
If the document does not address a point, say "not addressed". Do not use outside knowledge.
```

| ID | [ROLE] | [FOCUS] |
|---|---|---|
| E5 | Chapter 1 context source | what business intelligence is; who BI users are and what they produce; BI system use and success factors; anything about governance, rules or policy for BI |
| E6 | Chapter 1 context source | how analysts understand and verify AI-assisted analyses; what they check; where verification fails; any organisational rules or norms mentioned |
| G1 | Chapter 2 theory anchor (following or getting around rules) | definition of shadow IT; why employees use it; consequences; how organisations respond to it |
| G2 | Chapter 2 theory anchor (whether concerns travel upward) | definitions of employee voice and silence; antecedents of speaking up or staying silent (especially manager response and perceived efficacy); upward vs other directions; outcomes |
| G3 | Chapter 2 theory anchor (whether concerns travel upward) | definition of issue selling; when employees sell issues to top management; the moves or packaging they use; contextual conditions that favour or block it |

## B9 first — scoop-or-position report before the rest

B9 may already report empirically what the thesis hoped to show for claim K5 (bypass of AI rules). After B9's two queries, **stop and report to Albert** before touching the other five:

1. Sample: n, roles, sectors, countries. **Are BI / analytical / data roles included, and are they reported separately?**
2. Method: survey items vs interviews; does anything trace a *specific incident* (as the thesis protocol does), or is it self-reported frequency and attitude?
3. The definition of "governance drift zones" — verbatim, with page.
4. What is **observed** (reported behaviour, cases) vs **asserted** (recommendations)?
5. Does it distinguish use *before* any rule existed from use *around* an existing rule? (The thesis now treats these as two different claims, K11 and K5.)
6. Your call: **scoop** (same population and question) or **position** (state the specific difference) — and the one sentence Chapter 2 would use.

## ⚠ Fabrication guard (D7 precedent)

In S3, the compiled D7 note contained a limitations section and a typology **that do not exist in the paper**. Therefore:

- §9 and §13(e) limitations: **verbatim quotes only**, each checked against the PDF page before it enters a note. "None stated" is an acceptable answer.
- Any typology, framework name or count in §3 or §13 must be findable in the PDF at the cited page. If NotebookLM returns something you cannot locate, drop it and say so in the note.
- §6 metadata from NotebookLM is a claim, not verification — check it against the publisher page.

## Delivery and persistence (same rules as S3)

- Outputs go **into the repo** at exact paths: `literature/notes/<ID>_<firstauthor><year>_<slug>.md`, `literature/_raw/<ID>.md`, `literature/references.bib`, `literature/search_log.md` (append per-source verification lines under the existing **§S5**), `literature/reference_list.md`, `planning/Pipeline_State.md`. No zips, no downloads.
- **The Cowork shell cannot mount the repo.** Use the file listing / staging / commit tools. Evidence of delivery = a re-listing of the target folders showing the new files with sizes and times (Albert runs `git status` himself). Do not commit or push.
- `_raw/<ID>.md`: write Q1 the moment it returns, append Q2 the moment it returns. Compile only from these files. MCP queries do not persist in NotebookLM's chat history.
- Do not delegate querying to a subagent that returns content.
- **Step 0:** before writing, ask each notebook to state its source's printed title and authors, match to the PDFs in `Group B/`, `Group E/`, `Group G/`, and send Albert the ID table for approval.

## Naming (from `naming_convention.md`)

Suggested filenames — confirm slugs against the printed titles:

```
B9_silic2025_shadow_it_to_shadow_ai.md
E5_ain2019_bi_adoption_success_slr.md
E6_gu2024_analysts_verify_ai_analyses.md
G1_haag2017_shadow_it.md
G2_morrison2023_employee_voice_silence.md
G3_dutton1993_selling_issues_top_management.md
```

Notebook names: `[B9] Silic2025 — From Shadow IT to Shadow AI` style, one PDF per notebook.

## After compile

- `references.bib`: update the six existing entries — status, verification method and date, quality tier, filled volume/pages. Remove `TODO-verify` only when checked against the PDF.
- `reference_list.md`: move entries from ❓ to ✅ as verified; update summary counts.
- `Pipeline_State.md`: corpus counts (governance 35 → 36 with B9; new Cluster G = 3; E = 6), §11 tally before/after B9, and the B9 scoop-or-position verdict.

---

## Copy-paste prompt for the Sonnet session

```
Read planning/s5_addref_prompt.md in my repo first, then planning/query_template_v2.4.md,
planning/naming_convention.md and planning/ch2_targeted_search_2026-09-29.md. Use
"Claude outputs/s3_gapfill_prompt-1.md" as the precedent for process -- the S5 prompt file lists
what differs.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). The Cowork shell cannot mount my folders -- use the
file listing/staging/commit tools. NotebookLM is available via the notebook MCP; if auth is
stale I'll run `nlm login`. Do not commit or push; I push myself.

The 6 PDFs are in Group B (B9), Group E (E5, E6) and a new Group G folder (G1-G3).

STEP 0: create one notebook per PDF, ask each notebook for its source's printed title and
authors, match them to the PDFs, and send me the ID table for approval BEFORE writing anything.
The IDs in the prompt file are a plan, not a record.

Process B9 (Silic et al. 2025) FIRST with full template v2.4 including section 11, then STOP and
give me the scoop-or-position report described in the prompt file before doing the other five.

E5, E6, G1, G2, G3 use variant v2.4-T: Query 1 as normal, Query 2 = sections 7-10 then
section 13 THESIS ANCHOR with the per-source focus line from the prompt file. Do NOT run
section 11 on them -- they are not governance literature and must not enter the section 11
denominator.

Write every answer to literature/_raw/<ID>.md the moment it returns (Q1 written, Q2 appended).
Limitations and typologies: verbatim quotes only, each checked against the PDF page -- "none
stated" is fine. Do not supply anything you cannot find in the PDF.

Then PAUSE -- I will ask my own questions in each notebook before you compile.

When I say "compile": write the six notes, update the six existing bib entries in place (no
duplicates), append per-source lines under S5 in literature/search_log.md, regenerate
literature/reference_list.md, update planning/Pipeline_State.md with the section 11 tally
before (35) and after (36) B9 as two figures. Finish by re-listing literature/notes/ and
literature/_raw/ so I can see the files landed.
```
