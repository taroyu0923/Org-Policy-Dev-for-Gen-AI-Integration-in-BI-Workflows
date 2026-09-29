# Thesis Pipeline — Session Handoff State

**Canonical location:** `planning/Pipeline_State.md` in the repo. The Claude-project copy is a mirror.
**Last updated:** Sep 29, 2026 — S5 add-reference pass compiled (B9, E5, E6, G1, G2, G3; all PDF-verified). Earlier: Sep 11, 2026 — S3 gap-fill run (15 new sources, 14 kept); 35-note filename retrofit to cluster-numbered IDs (`A1`…, `I1`…) completed; §11 harvest complete; §12 pass specified; template v2.4 standalone; planning docs migrating into version control.

**Read before continuing:** this file → `planning/query_template_v2.4.md` → `planning/LitReview_Process_v2.md` → `research-design/` → `literature/search_log.md`.

---

## Where the project actually is

| Stream | State |
|---|---|
| Literature — governance corpus | **36 compiled governance notes, 35 usable** (Mitchell excluded; +B9 from S5). Plus **5 non-governance context/anchor notes** outside the §11 denominator: E5, E6 (Ch.1 BI context) and Cluster G, G1–G3 (Ch.2 theory anchors). Before S5: Clusters A 11, B 8 → **9 with B9**, C 7, D 7, E 4 → **6 with E5/E6**, **new G 3** — up from A6/B6/C3/D5/E1 after the Sep 11 S3 gap-fill (15 new sources, 14 kept, 1 excluded). Filenames retrofitted from `<letter>_<author><year>_<slug>.md` to cluster-numbered `<ID>_<author><year>_<slug>.md` (e.g. `A1_batool2024...`) — old-named files still present in `literature/notes/`, pending Albert's manual `git rm` |
| Literature — methodology corpus | **14 compiled notes**, renamed from `Interview_I<n>_<slug>.md` to `I<n>_<slug>.md` (Sep 11), ten-section format, §12 not yet run |
| `references.bib` | **64 entries** (58 + 6 from S5); the six S5 entries are now PDF-verified and no longer `TODO-verify` (G3's DOI is from the publisher page, tagged `doi-not-in-pdf`). **17 still `TODO-verify` and formally uncitable**, 13 of them the interview-design cluster |
| §11 working-tier harvest | **DONE (Sep 4)** — see the finding below |
| §12 protocol-craft harvest | **Specified, not run** — `planning/section12_protocol_craft_prompt.md` |
| Interview design | Protocol **v0.97**; sample confirmed at 14 participants / 9 orgs / 6 jurisdictions |
| Ethics | ⏳ **IN PROGRESS** — determination not yet received. **Blocks recruitment** |
| Chapter drafting | Not started |

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

## S5 add-reference pass (Sep 29, 2026) — results

**§11 tally, two figures, not merged.**
- **Before B9:** documented absence in **23 of 35** governance notes. Derived from the Sep 4 harvest (14 of 20) plus the 15 S3 notes' §11 verdict lines (nine documented absence: A8, A10, A11, A12, B8, C9, E2, E3, E4; three substantive or partial with data: A9, C10, D7; C7 partial; D6 substantive-secondary; C8 normative with no field data). Sensitivity: **22–24 of 35** depending on how A12, B8 and C8 are read. ⚠ Read off the verdict lines by this session, not re-verified against the full §11 texts; consistent with the "22–24 of 35" range in `planning/s5_addref_prompt.md`.
- **After B9:** **23 of 36** (range 22–24 of 36). B9 is counted as a **positive** (working-tier data via the survey and executive testimony), with sub-question (d), practitioner channels to influence policy, a documented absence. That classification is Albert's call; if read as a partial, the tally is unchanged at 23 of 36 because it is still not a documented absence.
- E5, E6, G1, G2, G3 are **not in either figure** (v2.4-T, no §11).

**B9 scoop-or-position verdict: POSITION, not scoop.** B9 is the first source in the corpus with primary empirical data on unauthorised AI use, so claim K5's "no source observes shadow use directly" now holds only within the other 35 notes. It observes bypass through executive testimony and awareness items at population level. It has no BI unit of analysis (respondent roles "ranging from analysts to senior managers", no role or sector split), no critical incidents, no separation of use *before* a rule existed from use *around* an existing rule (K11 vs K5), and no measure of upward feedback. Its own limitations state that the findings "may underrepresent challenges faced by mid-level managers or employees". Cite B9's interview count as eight and flag the abstract's "10" (internal inconsistency). Do not cite the "official tools as misaligned" sentence as a Silic finding; it is Walters (2021).

**Verification findings that change how the notes may be used** (details in each `_raw/<ID>.md`):
- NotebookLM errors were found in all six, including a fabricated attribution (B9), wrong proposition number and count (G3), a spliced quote (G2), policy framing not in the paper (E6), and altered quotes (G1). **Never quote a NotebookLM answer without checking the PDF page.**
- E6 and E5 contain no policy or rules content; G2 states no limitations of its own review; G1 states none; G3 has no printed DOI.

**Corpus counts after S5.** Governance corpus 35 → **36** notes (B9). Cluster B 9 entries / 8 notes; Cluster E 6 notes (E1–E4 governance, E5–E6 context); **Cluster G = 3** (new). Bib 64 entries, TODO-verify 17.

**Claims map.** `planning/ch2_claims_map_2026-09-29.md` not edited. K5's line "No source in the corpus observes shadow use directly" needs a B9 exception before Chapter 2 is drafted.

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
5. **S4 methods foundation** — reflexive TA (Braun & Clarke), critical incident technique (Flanagan), embedded case design (Yin/Eisenhardt). Note `castillomontoya2016ipr` (IPR framework) is already held and verified.
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

Full draft end-Nov; **hard deadline Dec 15**. Word budget 18–24k: intro 10%, lit review 27%, method 15%, findings 25%, discussion 18%, conclusion 5% — the review is the section most likely to over-run and starve findings. Markdown + pandoc `[@key]` now, LaTeX in Nov. Interviews Sep–Oct.

**Model assignment:** Fable = orchestration/QA; Opus = synthesis, drafting, method, review; Sonnet = search, citation-check, mechanical loops; Haiku = filing; NotebookLM = reading. Escalate one tier after two failed QA passes.

**Per-reference truth lives ONLY in `references.bib`** (amendment A4). This file summarises; it never holds per-reference status. `literature/reference_list.md` is a generated audit view.

## Infrastructure

- **NotebookLM:** stale auth → `nlm login`; missing `nlm` → `pip install --upgrade notebooklm-mcp-cli`. MCP queries do **not** persist to the UI chat history — accepted for §11/§12 only, with repo-side provenance blocks as the mitigation. v1 combined notebook `f05b434b-adac-4c5d-b352-a584435095f3` — keep or delete, Albert's call.
- **Repo (system of record):** `D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows`. Albert pushes manually; cloud git push is proxy-blocked, don't retry.
- **Source PDFs:** `D:\Master\Thesis\Thesis Content`. New references: PDF here first, then the pipeline — never NotebookLM-only.
