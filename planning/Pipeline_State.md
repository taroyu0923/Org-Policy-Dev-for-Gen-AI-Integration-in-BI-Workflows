# Thesis Pipeline — Session Handoff State

**Canonical location:** `planning/Pipeline_State.md` in the repo. The Claude-project copy is a mirror.
**Last updated:** Oct 2, 2026 — **S6 sensemaking add-reference pass compiled (G4–G10; Cluster G 3 → 10)**; earlier: Oct 1, 2026 — **Chapter 1 drafted (v1, 1,977 words) + supervisor sheet**; **§11 tally final under R1: 28–29 of 36 (78–81%)**; S3 spot-check + phase 2 done; page fixes in 14 notes; 8 bib-key headers fixed; S1 partly reconstructed. Earlier Oct 1: **D6 recoded to documented absence; §11 tally now 23–25 of 36 (64–69%)**; S3 §11 spot-check briefed. Earlier Oct 1: 2.5 drafted (v1); §2.5 writing brief (`planning/ch2_2.5_writing_prompt.md`) with a PDF pre-check of its sources: **C10 checked**, **D6 champion content not in the PDF**, several note pages corrected; 25,000-word budget restored again. Earlier: Oct 1 — Chapter 3 drafted except 3.3 and reviewed (`planning/ch3_review_2026-10-01.md`). Sep 30 — S4 methods foundation (Cluster M). Sep 29 — S5 add-reference pass (B9, E5, E6, G1, G2, G3; all PDF-verified). Sep 11 — S3 gap-fill; cluster-numbered filenames; §11 harvest; template v2.4.

**Read before continuing:** this file → `planning/query_template_v2.4.md` → `planning/LitReview_Process_v2.md` → `research-design/` → `literature/search_log.md`.

---

## Where the project actually is

| Stream | State |
|---|---|
| Literature — governance corpus | **36 compiled governance notes, 35 usable** (Mitchell excluded; +B9 from S5). Plus **12 non-governance context/anchor notes** outside the §11 denominator (S6 added seven): E5, E6 (Ch.1 BI context) and Cluster G, G1–G10 (Ch.2 theory anchors; G4–G10 are the sensemaking lens, §2.6). Before S5: Clusters A 11, B 8 → **9 with B9**, C 7, D 7, E 4 → **6 with E5/E6**, **new G 3** — up from A6/B6/C3/D5/E1 after the Sep 11 S3 gap-fill (15 new sources, 14 kept, 1 excluded). Filenames retrofitted from `<letter>_<author><year>_<slug>.md` to cluster-numbered `<ID>_<author><year>_<slug>.md` (e.g. `A1_batool2024...`) — old-named files still present in `literature/notes/`, pending Albert's manual `git rm` |
| Literature — methodology corpus | **14 compiled notes**, renamed from `Interview_I<n>_<slug>.md` to `I<n>_<slug>.md` (Sep 11), ten-section format, §12 not yet run |
| `references.bib` | **84 entries** after S6 (`grep -c '^@'` gave 77 before S6, so the 64 in the S5 text below predates the S4 and interview-design additions; S6 added 7); the six S5 entries are now PDF-verified and no longer `TODO-verify` (G3's DOI is from the publisher page, tagged `doi-not-in-pdf`). **17 still `TODO-verify` and formally uncitable**, 13 of them the interview-design cluster |
| §11 working-tier harvest | **DONE (Sep 4)** — see the finding below |
| §12 protocol-craft harvest | **Specified, not run** — `planning/section12_protocol_craft_prompt.md` |
| Interview design | Protocol **v0.98** (+C1a, D2a, E3a); sample 14 participants / 9 orgs / **5 countries** (corrected Oct 1; was "6 jurisdictions") |
| Ethics | Supervisor confirmed no ethical review required (Sep 11 log D7); **`ethics_determination_note.md` §5 (date, evidence) deferred to the supervisor meeting**. Consent pack (privacy notice v0.9, info sheet + consent form v0.98) to be sent by Albert before Oct 5 |
| Chapter drafting | **Ch1 (Oct 1):** all six sections drafted v1 (1,977 excl. citations / 2,000), outline + supervisor sheet `planning/ch1_outline_draft_2026-10-01.md` approved; 1 PENDING marker. **Ch2:** 2.1 v1.1 (1,085), 2.6 v1.3 (669) drafted; 2.5 v1.1 (1,211 excl. citations), reviewed by Albert; 2.2–2.4 after the Shopee interviews. **Ch3:** 3.1, 3.2, 3.4–3.7 drafted and reviewed (~2,607 + Table 3.1); 3.3 after the pilot. See `chapters/ch1/README.md`, `chapters/ch2/README.md`, `chapters/ch3/README.md` |

---

## 🔑 The §11 finding (Sep 4) — the most important result so far

One query was appended to all 20 usable governance notes, asking what each source says about how governance is *experienced* by the people doing analytical work. Verdicts, read off each §11's own opening line:

| Verdict | n | Sources |
|---|---|---|
| Substantive | 4 | Joshi, Lee, Ackerman, **Nahar** — the only one observing practice directly |
| Partial | 2 | Madanchian, Papagiannidis — reviews that *name* the gap without studying it |
| Documented absence | **14** | All of Cluster A, four of six in B, all of C, and Khandan (E) |

> **14 of 20 governance sources contain no account of how anyone below management experiences governance.**

This resolves the framing question that was open for three sessions. The engagement gap is **named but barely studied** — Papagiannidis states that responsible-AI adherence is "generally deprioritized or considered an ancillary task"; Batool's own SLR flags the working tier as understudied; Nahar observed it and nobody else did. It is a genuine hole, not a live literature this thesis would be joining.

⚠ **Denominator discipline.** That statistic holds only because those 20 were selected as the *governance* literature. **§11 must never be run on the `Interview_I*` cluster** — method-craft papers would return false nulls, empirical practitioner studies guaranteed positives. Methodology sources run §12 instead (template variant v2.4-M).

⚠ The classification above was read off verdict lines by the Opus session, not taken from the harvest agent's own summary table. Cross-check if that table is still available.

---

## Word budget decision (Oct 2, 2026, Albert)

Chapters 2 and 3 may run over their budgets (after the sensemaking edits: 2.1 1,176 · 2.5 1,430 · 2.6 1,005 · 3.4 792). No trimming now; the 25,000 total is rebalanced when Chapters 4–6 are planned.

## S6 add-reference pass (Oct 2, 2026) — sensemaking sources

- **Why:** Albert adopted sensemaking as a **second lens** (Ch.2 §2.6) on the supervisor's suggestion, Oct 2, 2026. Sources: the supervisor's suggestion plus Balasooriya & Sedera (2026)'s reference list.
- **Done:** seven PDFs → NotebookLM (one notebook each), Step 0 ID table approved by Albert, v2.4-T for all (Query 2 = §7–§10 + §13 THESIS ANCHOR; **no §11, no §12**). Notes `G4`–`G10` compiled; raw answers plus a "Verification against the PDF" section in `literature/_raw/G4.md … G10.md`; seven bib entries; `search_log.md` §S6; `reference_list.md` regenerated (Cluster G 10 entries).
- **Counts:** Cluster G **3 → 10**. Governance corpus **unchanged at 36**. **§11 tally unchanged at 28–29 of 36 (78–81%)**; G4–G10 are outside the denominator.
- **Sources:** G4 Weick, Sutcliffe & Obstfeld 2005; G5 Maitlis & Christianson 2014; G6 Gioia & Chittipeddi 1991; G7 Balogun & Johnson 2005 (**OCR only, no text layer**); G8 Balasooriya & Sedera 2026; G9 Balogun & Johnson 2004; G10 Rouleau 2005. G7 and G9 are the same case (not independent). G6 and G9 print no DOI; G10's DOI is a watermark only; Crossref was not reachable.
- **NotebookLM errors found (never quote its answers unchecked):** wrong page numbers throughout; "eight properties" for Weick et al. (paper has seven headed properties); G7's span (12 months, actually about 16); the G5 typology is Maitlis 2005's; a "hold-out informant" in G6 not in the PDF. G8's "Weick and Weick (1995)" is a paper error and is not reproduced; Weick (1995) the book was not added.
- **Do not attribute this thesis's own terms** (working rule, carriers/recipients, receiving end) to these authors. They write "change recipients", "sensegiving", "schemata".
- **Albert's own notebook questions:** none were recorded in any of the seven notebooks at compile time (chat histories empty). Add them to §"Albert's Questions" in each note if you have them.
- **Open:** G7, G8 and G10 first-page titles were read; Orchestration review Oct 2: all quotes re-checked against the PDFs; G8 issue 6 confirmed in the PDF download stamp; G6 and G9 DOIs added from Crossref. Chapters not edited. Nothing committed or pushed.

## S5 add-reference pass (Sep 29, 2026) — results

**§11 tally, two figures, not merged.**
- **Before B9:** documented absence in **23 of 35** governance notes. Derived from the Sep 4 harvest (14 of 20) plus the 15 S3 notes' §11 verdict lines (nine documented absence: A8, A10, A11, A12, B8, C9, E2, E3, E4; three substantive or partial with data: A9, C10, D7; C7 partial; D6 substantive-secondary; C8 normative with no field data). Sensitivity: **22–24 of 35** depending on how A12, B8 and C8 are read. ⚠ Read off the verdict lines by this session, not re-verified against the full §11 texts; consistent with the "22–24 of 35" range in `planning/s5_addref_prompt.md`.
- **After B9:** **23 of 36** (range 22–24 of 36). **Superseded Oct 1, 2026 → 24 of 36, range 23–25 (64–69%)** after D6 recoded to documented absence against the PDF (see "D6 recode" below). B9 is counted as a **positive** (working-tier data via the survey and executive testimony), with sub-question (d), practitioner channels to influence policy, a documented absence. **Confirmed positive by Albert (Sep 30, 2026).** Chapter 2 §2.6 used 22–24 of 36 (61–67%) until Oct 1; **now 23–25 of 36 (64–69%)** (2.6 v1.2).
- E5, E6, G1, G2, G3 are **not in either figure** (v2.4-T, no §11).

**B9 scoop-or-position verdict: POSITION, not scoop.** B9 is the first source in the corpus with primary empirical data on unauthorised AI use, so claim K5's "no source observes shadow use directly" now holds only within the other 35 notes. It observes bypass through executive testimony and awareness items at population level. It has no BI unit of analysis (respondent roles "ranging from analysts to senior managers", no role or sector split), no critical incidents, no separation of use *before* a rule existed from use *around* an existing rule (K11 vs K5), and no measure of upward feedback. Its own limitations state that the findings "may underrepresent challenges faced by mid-level managers or employees". Cite B9's interview count as eight and flag the abstract's "10" (internal inconsistency). Do not cite the "official tools as misaligned" sentence as a Silic finding; it is Walters (2021).

**Verification findings that change how the notes may be used** (details in each `_raw/<ID>.md`):
- NotebookLM errors were found in all six, including a fabricated attribution (B9), wrong proposition number and count (G3), a spliced quote (G2), policy framing not in the paper (E6), and altered quotes (G1). **Never quote a NotebookLM answer without checking the PDF page.**
- E6 and E5 contain no policy or rules content; G2 states no limitations of its own review; G1 states none; G3 has no printed DOI.

**Corpus counts after S5.** Governance corpus 35 → **36** notes (B9). Cluster B 9 entries / 8 notes; Cluster E 6 notes (E1–E4 governance, E5–E6 context); **Cluster G = 3** (new). Bib 64 entries, TODO-verify 17.

**Claims map.** `planning/ch2_claims_map_2026-09-29.md` not edited. K5's line "No source in the corpus observes shadow use directly" needs a B9 exception before Chapter 2 is drafted.

---

## §2.5 source pre-check (Oct 1, 2026) — results

Orchestration session, pdftotext on the staged PDFs, while writing the §2.5 brief. Pages are printed pages. Leads for the writing session, not a sign-off per quote.

- **C10 Asatiani — PDF-checked for its 2.5 use.** The feedback loop is observed but at **system level**: user and data-scientist feedback adjusts the AI application at set review intervals (p. 275); caseworkers tune thresholds (p. 273); dialogue with caseworkers "the difficult part" (p. 274). Printed page = PDF page + 258 (the note's pages are article-relative). Not a channel to change usage rules. The note's "no workarounds" is not a located quote. The open item "C10 not PDF-verified" is closed for 2.5; the §11 verdict text itself was not re-read.
- **D6 Lu 2024 — RESOLVED Oct 1 (Albert approved).** Full PDF check (`planning/d6_pdf_check_2026-10-01.md`: text layer all 35 pp. + OCR of all figures): no champion, conduit, escalation, "Continuous AI Ethics/Governance Checks" pattern or "Product Management Patterns" section; the note's §3–5, §7–9, §11 came from a NotebookLM Query 2 that invented the paper's structure (Query 1 was accurate). **§11 recoded substantive-secondary → documented absence** (prescriptive only; the only feedback flows down, committee → project team, p. 173:10). **Tally 22–24 → 23–25 of 36 (64–69%)**; 2.6 ¶2 updated (v1.2). Range composition aligned to 2.6/3.7: the two conceptual audit papers **C7 and C8** (the older "A12, B8, C8" wording above is superseded). D6 removed from K8/K9 in the claims map; kept for 2.1 (verified) and, in 2.4, only as a case-by-case approval body (p. 173:10). Note rewritten from the PDF. **Pattern:** D7 and D6 (both S3, Sep 11) had invented Query-2 content → §11 spot-check of the other S3 notes briefed in `planning/s3_section11_spotcheck_prompt.md`.
- **G2 Morrison:** "lateral voice" does not occur in the PDF; Morrison restricts voice to upward (p. 80). The protocol (§E3a) and codebook attribute "lateral voice" to G2; keep the code, but do not cite Morrison for the term.
- **Note page errors:** B1 Taeihagh "iteratively responding" p. 7 and "red teaming…" p. 8 (note: p. 6); B5 Weinberg feedback loops pp. 9, 12 (note: p. 8); B8 Janssen "governance should also evolve" p. 44 (note: p. 43). D5 Ackerman's 9% is only in Fig. 7 (text: "least selected", p. 14). B4 "slow, rigid, or absent" not found in the PDF.

---

## §11 tally — FINAL under rule R1 (Oct 1, 2026, Albert approved)

**28–29 of 36 governance sources (78–81%)** contain no account of how staff below the rule-setting level receive AI governance.
- Not-absence (7): A9, B6, B9, C10, D4, D5, D7.
- Range: A12 (information governance, executive-reported).
- Every verdict was PDF-checked: S3 notes line by line; Sep 4 batch by method-signal scan, with the six not-absences read in full.
- Recodes: B4, D1, D2, C7, C8, D6 → absence; C10 → partial.
- Applied to 2.6 ¶2 (v1.3), 3.7 ¶2, READMEs and notes.
- **This supersedes every earlier figure in this file (14/20, 22–24, 23–25).**
- C7 re-checked on the publisher PDF (Oct 1): verdict unchanged.

## S3 §11 spot-check (Oct 1, 2026) — results (decision taken: R1, see above)

Log: `planning/s3_section11_spotcheck_2026-10-01.md`. The 12 remaining S3 notes were checked against their PDFs (C7 by OCR: its PDF is an image-only browser print-out).
- **Proposed recodes:** C7 partial → **documented absence** (its one practitioner finding is cited from Vakkuri et al. 2019); C8 → **documented absence** (normative framework, hypothetical worked example); C10 substantive → **partial** (no tally effect). **A12 contested**: executive-reported user data, but on *information* governance (2013), not AI. The other 8 absences are confirmed.
- **Consequence:** the 2.6/3.7 explanation of the range ("two conceptual audit papers", C7/C8) no longer holds. Recount: **25–26 of 36 (69–72%)** under the verdicts as they now stand.
- **Rule decision needed:**
  - **R1** — not-absence only with *data* on staff reception of AI governance (applied to A9, D6, C7, C8). Recommended. Needs a **phase 2** PDF check of the Sep 4 not-absences B4, B6, D4, D5, D1, D2; B4, D1 and D2 are likely absences under R1, giving ~28–29 of 36.
  - **R2** — "names the gap" counts as partial (the Sep 4 practice). Under R2, A8 and A10 become partial, giving ~23–24 of 36.
- **2.6 ¶2 and 3.7 ¶2 are not changed** until the rule is decided (and phase 2 is run under R1).
- **Also found:** claims map K6 should drop C8 (an over-reading); E2 has two quotes not in the PDF (the "research agenda" gap statement does not exist); 8 S3 notes had header bib keys that are not in `references.bib` (fixed Oct 1).

## Note fixes (Oct 1, 2026) — applied

- **PDF page-check blocks** added to 14 notes: A8, A10, A12, B1, B4, B5, B8, C7, C8, C10, D1, D5, E2, G2. Each block gives the printed-page offset, the corrected pages, quotes not in the PDF, and the proposed §11 verdict where one changes.
- **Bib-key headers corrected** in A8, A9, A10, A12, C9, D7, E3, E4, so that every note's key matches `references.bib`.
- **`literature/search_log.md` S1:** databases and strings partially reconstructed from Research Plan §2.4. These are the planned sources, not a record of S1; ⚠ Albert to confirm before 3.7's `[FILL]` is replaced.

---

## Established findings for the synthesis memos

1. **BI gap — 21/21** on the literal terms, but state it precisely: *the literature increasingly gestures at analytics contexts but no study takes the BI workflow as its unit of analysis.* Absence of the term is the evidence; absence of the unit of analysis is the gap. Papagiannidis cites analytics literature; Khandan is built on predictive analytics. Do not overclaim "nobody mentions analytics."
2. **Working-tier absence — 14/20.** See above.
3. **Tier convergence, four independent sources:** Batool 5-level (A1 §4.2 p.14), Joshi strategic/tactical/operational (B4 p.2), Lee L1/L2/L3 (B6 §4.1 pp.7–8), NTT DATA via Ismail (A3 §4.3 p.129). None observes the bottom of the hierarchy empirically.
4. **Lifecycle convergence:** Batool "When", Joshi 6-stage, Weinberg 4-phase, Xue & Pang 4-stage. The three interview phases compress this — grounded, not invented.
5. **Engagement gap — fourth convergence:** `responsibleaigovreview` p.1; `stickystories2025` §2.1 p.4; `agenticaiperceptions2025` §3.8 p.13; `ethicaltheoriesgovmodels2025` §1 p.2.
6. **Almost no organizational-level empirical work.** Only Lee (8 projects, 2 interview rounds; 28 companies) and Nahar (single-org field study) did fieldwork. Papagiannidis self-states "lack of empirical testing" (p.15) — a top-journal invitation addressed to a study like this.
7. **Exploitable tension:** Cluster A proposes static comprehensive architectures; B and D push adaptive/emergent. Luna self-states "static snapshot"; Weinberg self-states longitudinal studies needed.
8. **Instrument assets:** Lee's 245-question bank; Ismail's five-topic architecture; Luna's three-cycle coding method and Covered/Partial/Not rubric; Nahar's six-indicator reflection scheme and two-month follow-up items; Papagiannidis's Table 5 research questions; **Mökander & Floridi's full Appendix 1 protocol, verbatim with page locations, in `Interview_I9`**.
9. **Load-bearing risks:** Priyanshu (CMU course paper), Ozman (low-tier, no self-limitations), C1 and C3 (grey-tagged). Supplementary use only.

---

## Design decisions in force

**Theory spine:** Papagiannidis, Mikalef & Conboy (JSIS 2025) — structural / procedural / relational practices + Antecedents–Practices–Effects, after Tallon, Ramirez & Short (2013, *JMIS*). Chosen because it is processual (fits *evolution*), sits in an IS lineage, and **relational practices are what the working tier can actually observe**. Luna's H-GenAIGF retained as coding instrument and jurisdictional comparator.

**Reframed to the working tier.** No participant authored a GenAI policy, so the study is an account of how policy is *encountered, interpreted and adapted* by people producing analytical outputs, and whether that adaptation feeds back upward. Phase 3's upward-feedback items become the central test. Interview Phase 1 renamed **Policy Encounter & Interpretation**.

**Sampling — embedded multiple-case**, two strata never pooled. Depth: Shopee TW (n=4, three levels, zh-TW, likeliest document source, highest confidentiality risk) and Smartly FI (n=3). Breadth: Toyota TW, Delivery Hero TW, JPMorgan US, Twipe BE, Roku US, Amazon JP, Nordea FI. Evidence tiers: 1–2 document-anchored cases used to *assess recall quality* in the interview-only cases.

**BI-forcing:** critical-incident anchor, bounded three-type menu, each process-traced with the same four questions. Warranted by Nahar's revealed-preference method (§6.1.5, p.18); the risk it avoids is named by Ackerman (§2.3, p.4).

**Language:** English master, interpreted live, except core items fixed bilingually in `wording_card_bilingual.md`. Albert translates himself; verification is pilot-based, not independent back-translation. Pilot with #5 or #6 (Chinese-speaking breadth participant) so no depth informant is spent.

**Coding:** hybrid. Papagiannidis spine; three phases and Luna's constituents secondary; inductive for everything BI-specific. **No a priori code may be the answer to the RQ.** Nahar's engagement profiles are a discussion-stage comparison only — adopting them wholesale reduces the contribution to "it also applies in Taiwan and Finland."

**Confidentiality:** the risk is *inside* Shopee. Report Depth A by tier without persistent pseudonyms. **Recruitment template A (individual) for all 14** — several participants are under NDA; do not approach employers unprompted.

**Lit chapter structure — ADOPTED Sep 29, 2026 (Albert):** loop structure, a Plan 1 funnel ordered by the findings sequence — 2.1 how rules are assumed to arrive · 2.2 practice first / unclear rules · 2.3 asking or acting (bypass explanations) · 2.4 rulings and intermediaries · 2.5 does anything go up · 2.6 lens and gap; ~5,400 words. Plan 3 (cluster-mirroring) rejected: the claims Chapter 5 needs each span 2–4 clusters. BI-work context moved to Chapter 1. Spec: `planning/ch2_outline_draft_2026-09-29.md` (v2); claims: `planning/ch2_claims_map_2026-09-29.md`.

---

## Outstanding, in order

1. **⏳ Ethics determination** — in progress, blocks recruitment. Draft supervisor email: `research-design/ethics_determination_note.md` §4. Privacy notice (Aalto template) still outstanding.
2. **§12 protocol-craft pass + bib backfill + doc migration** — one Sonnet session, `planning/section12_protocol_craft_prompt.md` Parts A, B and C.
3. **Structure and interview-framework discussion** (Opus) — now unblocked by the §11 finding.
4. **~~S3 gap-fill~~ DONE (Sep 11)** — 15 frequency-ranked targets in `literature/search_log.md`; 14 kept (Rakova et al. 2021 included — closest published study to the reframed design), `algobiasbianalytics2025` excluded. Cluster loading landed as planned: +4 into C, +3 into E.
5. ~~**S4 methods foundation**~~ **DONE Sep 30, 2026** — new **Cluster M** (11 notes, all PDF-checked): M1 Braun & Clarke 2006, M2 Braun & Clarke 2021, M3 Fereday & Muir-Cochrane 2006, M4 Gremler 2004 (replaces Flanagan, cited only "as cited in Gremler"), M5 Butterfield et al. 2005, M6 Baxter & Jack 2008 (replaces Yin), M7 Nowell et al. 2017, M8 Malterud et al. 2016, M9 Temple & Young 2004, M10 Corbin Dwyer & Buckle 2009, M11 Eisenhardt & Graebner 2007. **Analysis label decided: codebook thematic analysis, not reflexive TA** (M2 note, decision block). Interview-design group I1–I14 also verified Sep 30 (metadata only; content still NotebookLM-compiled). Chapter 3 methods foundation: in place.
6. **Title-line spot-check** across all 35 notes against PDFs — triggered by the Mitchell metadata failure (amendment A2).
7. **S1 reconstruction** — databases and query strings from the research plan §2.4.
8. Synthesis memos A–E → `literature/cluster-memos/` (still empty).
9. Protocol pilot in Mandarin → v1.0. Cluster F when PDFs arrive.
10. **Rolling-coding discipline** — familiarization memo within 48h of each interview, one log line per interview in `analysis/`. Named the #1 schedule risk in the Sep 1 verification and still unimplemented.

## Open questions for Albert

- Amazon (#13, Business Operations) — confirm against the inclusion criterion and assign a tier.
- Optional: five Ackerman Likert items pre-interview would give one comparable structured datum across all 14 for a case table. Cheap — but does it prime the incident narrative?
- Cluster F contents.
- ~~`algobiasbianalytics2025` (E1) is tagged as the closest topical match to the thesis and is unverifiable ResearchGate content — verify or exclude; do not leave in limbo.~~ **RESOLVED (Sep 11, 2026): excluded**, same grounds as A2/B2/Mitchell. It no longer holds an E-slot — `E1` now = Khandan (2025), `E2`–`E4` = the three new S3 Cluster-E sources (Abraham 2019, Janssen 2020, Zhang 2022).

## Standing constraints

Full draft end-Nov; **hard deadline Dec 15**. **Word budget revised Sep 30, 2026 (Albert): target 25,000 words** (≈62 body pages at ~400 words/page, TNR 12, 1.5 spacing, + ~7 pages references ≈ 70; Aalto general guideline 60–100 pages — confirm with supervisor whether references/appendices count). Split: intro 8% (2,000) · lit review 25% (6,250) · method 12% (3,000) · findings 32% (8,000) · discussion 17% (4,250) · conclusion 6% (1,500). **Oct 1:** Chapter 3 allowed to run to ~3,350 (Albert); the ~350 over is taken from findings and discussion. *(Restored Oct 1: this revision had been lost when the file was overwritten from an older copy during the S4 pass. **Lost again and restored a second time Oct 1 (orchestration session, §2.5 brief):** the repo copy on disk still had the 18–24k line although the Claude-project mirror had the restore. Before editing this file, check this paragraph is present.)* Markdown + pandoc `[@key]` now, LaTeX in Nov. Interviews Oct 5–19.

**Model assignment:** Fable = orchestration/QA; Opus = synthesis, drafting, method, review; Sonnet = search, citation-check, mechanical loops; Haiku = filing; NotebookLM = reading. Escalate one tier after two failed QA passes.

**Per-reference truth lives ONLY in `references.bib`** (amendment A4). This file summarises; it never holds per-reference status. `literature/reference_list.md` is a generated audit view.

## Infrastructure

- **NotebookLM:** stale auth → `nlm login`; missing `nlm` → `pip install --upgrade notebooklm-mcp-cli`. MCP queries do **not** persist to the UI chat history — accepted for §11/§12 only, with repo-side provenance blocks as the mitigation. v1 combined notebook `f05b434b-adac-4c5d-b352-a584435095f3` — keep or delete, Albert's call.
- **Repo (system of record):** `D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows`. Albert pushes manually; cloud git push is proxy-blocked, don't retry.
- **Source PDFs:** `D:\Master\Thesis\Thesis Content`. New references: PDF here first, then the pipeline — never NotebookLM-only.
