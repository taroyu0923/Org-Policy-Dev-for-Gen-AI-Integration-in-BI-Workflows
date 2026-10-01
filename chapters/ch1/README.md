# Chapter 1 — Introduction (drafts)

Outline: `planning/ch1_outline_draft_2026-10-01.md` (**approved by Albert, Oct 1, 2026**). Brief: `planning/ch1_writing_session_prompt.md`.
Status: **all six sections drafted (v1), Oct 1, 2026.** Budget: 8% of 25,000 = **2,000 words** (±10%: 1,800–2,200). Each section: paragraph plan approved by Albert before drafting.

## Decisions (Albert, Oct 1, 2026)

- Personal motivation stated in Chapter 1 (1.1 ¶4: four to five years in BI-related roles; ad tech, manufacturing, e-commerce platforms, fintech, supply chain; start-ups to large companies). Positionality stays in 3.5.
- 1.5 and 1.6 kept separate.
- No market-context sentence on GenAI features in BI tools (no verified source); Gu et al. carry the point.
- 1.3 uses no direct quote: Mäntymäki et al. (p. 607) and Papagiannidis et al. 2025 (p. 14) are already quoted in 2.6.

## Status

| § | File | Heading | Status | Words excl. / incl. citations (target) | Last updated |
|---|---|---|---|---|---|
| 1.1 | `1.1_genai_in_bi_work.md` | Generative AI arrives in business intelligence work | Draft v1 | 535 / 555 (550) | Oct 1, 2026 |
| 1.2 | `1.2_rules_and_practice.md` | Rules arrive, and practice may already be there | Draft v1 | 341 / 345 (350) | Oct 1, 2026 |
| 1.3 | `1.3_problem.md` | The problem: governance seen only from above | Draft v1 | 274 / 274 (300) | Oct 1, 2026 |
| 1.4 | `1.4_aim_rqs.md` | Aim and research questions | Draft v1 | 324 (300; incl. RQ list labels) | Oct 1, 2026 |
| 1.5 | `1.5_approach_scope.md` | Approach and scope | Draft v1 | 299 excl. citation and marker / 302 incl. (300) | Oct 1, 2026 |
| 1.6 | `1.6_contribution_structure.md` | Intended contribution and thesis structure | Draft v1 | 204 (200) | Oct 1, 2026 |
| | | | **Total** | **1,977 excl. citations and markers / 2,004 incl. (2,000)** | |

## Sources used

**1.1** — `ain2019bisuccess` (pp. 1, 4, 8, 10), `gu2024analystsverify` (pp. 1, 8, 11). Both ✅, peer-reviewed. All 14 direct quotes string-matched against the PDF text on the cited printed page (E6 p. 11 by eye: the PDF prints a footnote mark "a" after "conclusions"). Citation numbers inside quoted sentences dropped (E5 pp. 1, 10; E6 p. 1).

**1.2** — `taeihagh2025govgenai` (pp. 2, 3, 4), `responsibleaigovreview` (p. 7), `haag2017shadowit` (p. 469), `silic2025shadowai` (p. 11, attributed to the executives' account). All ✅, peer-reviewed. All 7 direct quotes matched on the cited printed page (Haag and Silic by OCR of image-only PDFs).

**1.3** — one citation, no quotes: `mantymaki2022definingaigov` (pp. 604–605, paraphrase; added Oct 1 after review). Cross-references: 2.1 (cascade, prescription), 2.6 (tally as count only, "28 or 29 of 36"; percentage stays in 2.6; carriers vs recipients), 1.2 (executive-reported bypass).

**1.4** — no citations. RQ v2.1 verbatim (structure discussion log); BI practitioner definition verbatim, identical to 3.2 ¶1 (repeat kept, Albert Oct 1). Cross-references: 2.1 (rule), 3.2 (definition clauses), 3.4 (threshold, not stated).

**1.5** — `ain2019bisuccess` (no page; whole-work reference back to 1.1, Albert Oct 1). Otherwise cross-references: 3.1, 3.2, 3.3, 3.4, 2.1 (lifecycle models), 2.6 (lens), 1.1, 1.2.

**1.6** — no citations; contribution stated as aims (point iii, the lens from the receiving end, kept as an aim; Albert Oct 1). Chapter descriptions follow the outline's chapter map.

## Chapter-level check (Oct 1, 2026)

- 7 keys cited (after the 1.3 v1.1 citation; `mantymaki2022definingaigov` ✅), all in `references.bib` and all ✅ peer-reviewed in `reference_list.md`: `ain2019bisuccess`, `gu2024analystsverify`, `taeihagh2025govgenai`, `responsibleaigovreview`, `haag2017shadowit`, `silic2025shadowai`. No preprints.
- 21 direct quotes (1.1: 14; 1.2: 7), each matched on the cited printed page: E5 pp. 1, 4, 8, 10; E6 pp. 1, 8, 11; B1 pp. 2, 3, 4; D1 p. 7 (pdftotext); G1 p. 469 and B9 p. 11 (OCR).
- No quote shared with 2.1, 2.5 or 2.6 (A8 p. 607, D1 p. 14, B1 p. 7 deliberately not used).
- 0 em dashes; no style-list hits; no organisation names; no interview data.
- Pandoc render **not tested**: pandoc 2.9 on this machine lacks `--citeproc` and `pandoc-citeproc`. Test at build.

## Open markers

- **1.5 ¶1** `[PENDING: interviews Oct 5–19]` — remove after fieldwork; also check that "traced through the same questions" and "bounded menu" still match 3.3 after the pilot (protocol v1.0).

## Dependencies

- 1.5 ¶1 refers to **Section 3.3** (not yet drafted; after the pilot) for the incident menu and trace questions.

- **1.4 ¶4 and 3.2 ¶1 carry the BI practitioner definition word for word.** Any change to the wording must be made in both (and in `README.md` at the repo root).

- **1.3 ¶2 restates the 2.6 tally as a count (28 or 29 of 36).** If the §11 tally changes again, update 2.6 ¶2, 3.7 ¶2 **and 1.3 ¶2** (and outline §1 summary).

- 1.1 ¶1 points to the BI practitioner definition in **1.4**; ¶4 to **1.2** and **3.5** (positionality). Do not repeat the background sentence in 3.5 at length.
- **2.2 must refer back to 1.2 for the shadow IT definition** (Albert, Oct 1: verbatim definition kept in 1.2; 2.2 does not quote it again).
- 1.2 ¶3 leaves open whether use began before a rule or continued around one, pointing to 2.2 and 2.3 (same distinction as the 2.3 → 2.6 ¶4 dependency in `chapters/ch2/README.md`).

## Conventions

As `chapters/ch2/README.md`: pandoc keys from `literature/references.bib`; narrative `@key [p. N]`, parenthetical `[@key, p. N]`; pages are printed pages; word counts "excl. citations" count narrative author names as words and drop bracketed citations.

## Change log

- **Orchestration review (Oct 1, 2026).**
  - **Checks:** 21/21 direct quotes found on the cited printed pages (E5, E6, B1, D1 by pdftotext; G1 p. 469 and B9 p. 11 by OCR). 6 keys, all in the bib. 0 em dashes; no organisation names; RQ v2.1 and the BI practitioner definition verbatim; tally consistent with 2.6 v1.3.
  - **Applied:** 1.2 v1.1 (Taeihagh p. 3 quote shortened; the source sentence has a grammatical slip); 1.6 v1.1 (point iii "aims to apply"); outline chapter map → Ch1 drafted.
  - **Decided (Albert, Oct 1):** (1) 1.1 v1.1, sector list removed ("across several industries"); (2) 1.3 v1.1, definition cited `[@mantymaki2022definingaigov, pp. 604–605]` (paraphrase, PDF-checked); (3) supervisor-sheet Q6 AI-use wording kept as in the current Chapter 3 version.

- **1.6 v1 (Oct 1, 2026)** — drafted from the approved plan. Chapter 1 complete in draft (v1, all six sections).

- **1.5 v1 (Oct 1, 2026)** — drafted from the approved plan.

- **1.4 v1 (Oct 1, 2026)** — drafted from the approved plan; trimmed 344 → 324.

- **1.3 v1 (Oct 1, 2026)** — drafted from the approved plan; count without percentage.

- **1.2 v1 (Oct 1, 2026)** — drafted from the approved plan; shadow IT definition verbatim (2.2 refers back).

- **1.1 v1 (Oct 1, 2026)** — drafted from the approved plan; two sentences added after the first count (460 → 535) to reach the budget, both from the same sources (E5 p. 10; E6 p. 1).
