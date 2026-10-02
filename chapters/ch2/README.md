# Chapter 2 — Literature review (drafts)

Structure: outline v2 (loop structure), **adopted** Sep 29, 2026 — `planning/ch2_outline_draft_2026-09-29.md`. Claims: `planning/ch2_claims_map_2026-09-29.md`. Session brief: `planning/ch2_writing_session_prompt.md`.
Writing order: 2.1 → 2.6 → 2.5 → (after the Shopee interviews) 2.2 → 2.3 → 2.4.

| § | File | Heading | Status | Words (target ±10%) | Last updated |
|---|---|---|---|---|---|
| 2.1 | `2.1_how_rules_arrive.md` | How does the literature assume rules arrive? | **Draft v1.1** (edit pass E1–E5) — awaiting Albert's review | 1,085 excl. citations / 1,134 incl. (1,100) | Sep 30, 2026 |
| 2.2 | — | When practice comes first, and when rules are unclear | Not started (after Shopee interviews) | — (1,100) | — |
| 2.3 | — | Asking or acting: explanations of bypass | Not started (after Shopee interviews) | — (1,100) | — |
| 2.4 | — | Rulings and the people in between | Not started (after Shopee interviews) | — (1,000) | — |
| 2.5 | `2.5_does_anything_go_up.md` | Does anything go up? | **Draft v1.1** — reviewed by Albert (Oct 1); orchestration recheck: 32/32 quotes verified, 3 paraphrases tightened | 1,204 excl. citations / 1,256 incl. (1,250) | Oct 1, 2026 |
| 2.6 | `2.6_lens_and_gap.md` | What lens does the literature offer, and what does it leave unstudied? | **Draft v1.1** (edit pass E1–E2) — awaiting Albert's review | 669 excl. citations / 687 incl. (700) | Sep 30, 2026 |
| | | | **Total** | **2,958 / 6,250** (budget revised Sep 30: 25,000-word thesis) | |

## Dependencies

- **Chapter 1 (Oct 1, 2026):** 1.2 quotes the shadow IT definition verbatim (`haag2017shadowit`, p. 469). **2.2 refers back to Section 1.2 for it and does not quote it again** (Albert). 1.1 carries the BI-work context (E5, E6); 2.2–2.4 should not restate it. 1.3 ¶2 restates the 2.6 tally as a count ("28 or 29 of 36"); if the tally changes, update 1.3 too.

- **2.3 must raise, as an open question, whether a given use began before any rule existed or continued around one.** 2.6 ¶4 ends: "which is the distinction 2.3 left open". If 2.3 does not raise it, edit 2.6 ¶4.
- ~~2.6 ¶2 placeholder `Section [3.X]`~~ **Resolved Oct 1, 2026 → Section 3.7** (`chapters/ch3/3.7_literature_review_method.md` ¶2 describes the screening question, verdict vocabulary and why the count is a range). If 3.7 is renumbered, update 2.6 ¶2.
- **Tally (2.6 ¶2): 28–29 of 36 governance sources (78–81%)** since Oct 1, 2026, under coding rule R1 after the S3 spot-check and phase 2 (`planning/s3_section11_spotcheck_2026-10-01.md`); range = A12. Before that: 23–25 of 36 — D6 Lu recoded substantive-secondary → documented absence after a PDF check (`planning/d6_pdf_check_2026-10-01.md`; Albert approved). Was 22–24 (61–67%). B9 positive (Sep 29–30) and A9 partial (Sep 30) unchanged. The range = two conceptual audit papers, C7 and C8 (as 3.7 states). **If any further §11 verdict changes (S3 spot-check, `planning/s3_section11_spotcheck_prompt.md`), update 2.6 ¶2 again.**
- **2.5 brief (Oct 1, 2026):** D6 `lu2024raipatterns` is **not** to be cited for champions or upward feedback (no "champion" in the PDF); 2.5 does not restate the §11 tally or the carrier/recipient sampling argument (both in 2.6).
- Bib: `abraham2019datagovframework` renders the surname as "Brocke" (particle "vom" not protected). Check with `apa.csl` at build; fix in the bib if needed (e.g. `{vom Brocke}, Jan`).
- **2.5 (Oct 1, 2026):** ¶3 describes the non-champion study (D4) without restating 2.6's carrier/recipient argument; ¶4 ends with one sentence noting that D7's evidence concerns initiatives participants had taken on. If 2.6 ¶3 changes, re-read 2.5 ¶4 for overlap.
- **2.5 ¶6** asks whether issue selling (theorised for middle managers) applies to analysts without managerial standing. Chapter 5 should return to it if the data allow.

## Conventions

- Citations: pandoc keys as in `literature/references.bib`. **Narrative** `@key [p. N]` when the author is named in the sentence (renders "Author et al. (2022, p. N)"); **parenthetical** `[@key, p. N]` otherwise; `[-@key, p. N]` for a second locator in the same sentence. Never name an author in the sentence and in the brackets. APA 7 is applied at build: `pandoc --citeproc --bibliography literature/references.bib --csl apa.csl` (`apa.csl` from the Zotero style repository, not yet in the repo).
- Secondary citations in APA form, source not added to the bib: `[Orr & Davis, 2020, as cited in @birkstedt2023themesgaps, p. 147]`.
- Papagiannidis: `papagiannidis2023towardaigov` = the 2023 three-firm field study; `responsibleaigovreview` = the 2025 review (Papagiannidis, Mikalef & Conboy). Refer to them in prose as "field study" / "review".
- Word counts "excl. citations" count narrative author names as words and drop brackets and years. Pages are the pages printed in the PDF, not the note's page references (several notes are off by 1–3 pages; see the 2.1 log in `planning/session_handoff_2026-09-29.md`).
- Sources without printed page numbers are cited by section (e.g. `[@joshi2025resai, sec. IV.A]`).
- Preprints (arXiv; Research Square for `batool2024aigov`) are supplementary only; each claim is carried by a peer-reviewed source.
- Every direct quote is checked against the PDF before it enters a draft.
- No interview data in this chapter. The loop and Albert's hypotheses (P2, rulings as the working rule, the ask/act-now fork) appear only as open questions.

## Change log

- **2.5 v1.1 (Oct 1, 2026)** — recheck: 32/32 direct quotes found on the cited printed pages (G3 and B9 by OCR); 14 keys all in the bib; 1,211 words excl. citations; 0 em dashes; no style-list hits. Three paraphrases tightened (C10 p. 273, D7 p. 7:11, D4 p. 3). Consistent with the R1 tally (D1 used only as naming the gap; B4 flagged as a preprint and as prescription).
- **v1.3 (Oct 1, 2026)** — 2.6 ¶2 tally → 28–29 (78–81%), "receive AI governance", range sentence now names the information-governance study (A12); 3.7 ¶2 states the R1 rule and the new range reason. No other text changed.
- **v1.2 (Oct 1, 2026)** — 2.6 ¶2 tally 22–24 (61–67%) → 23–25 (64–69%) after the D6 recode. No other text changed.
- **v1.1 (Sep 30, 2026)** — edit pass from `planning/ch2_edit_prompt_2.1_2.6.md` (review `planning/ch2_review_2026-09-30.md`): E1 narrative citations (both); E2 Papagiannidis 2023/2025 disambiguated (2.6); E3 *rule* widened to written or unwritten (2.1 ¶1); E4 2.1 ¶2 regrouped; E5 Orr & Davis marked as secondary citation in APA form (2.1 ¶2); E6 this README. No quote, page, tally, source or heading changed.

## 2.1 — sources used

Carrying (peer-reviewed): `mantymaki2022definingaigov`, `birkstedt2023themesgaps`, `abraham2019datagovframework`, `lu2024raipatterns`, `ismail2025frameworks`, `tallon2013informationartifact`, `responsibleaigovreview`, `rakova2021practitionerperspectives` (PDF only).
Supplementary (preprint): `joshi2025resai`, `lee2024questionbank`, `batool2024aigov`, `batool2024rai`, `agarwal2025fivelayer`, `luna2024paradigms`, `weinberg2025faigmoe`.
Not used: A9, C10 (not PDF-verified), B9 (belongs to 2.2/2.3/2.6).

## 2.6 — sources used

Carrying (peer-reviewed): `tallon2013informationartifact`, `abraham2019datagovframework`, `papagiannidis2023towardaigov` (PDF-verified Sep 30; §11 recoded partial), `responsibleaigovreview`, `birkstedt2023themesgaps`, `mantymaki2022definingaigov`, `rakova2021practitionerperspectives` (PDF only), `silic2025shadowai`.
Supplementary (preprint): `stickystories2025` (flagged in text as a preprint accepted at CHI 2026).
Cross-reference: `Section 3.7` for the §11 screening method (resolved Oct 1, 2026).

## 2.5 — sources used

Carrying (peer-reviewed): `janssen2025responsiblegenai` (p. 44, system-level feedback), `taeihagh2025govgenai` (p. 7, regulation-level), `abraham2019datagovframework` (p. 430, escalation), `responsibleaigovreview` (pp. 11, 14), `asatiani2020blackbox` (pp. 273–275, system-level loop), `silic2025shadowai` (p. 12, one sentence), `rakova2021practitionerperspectives` (pp. 7:11, 7:14; PDF only), `morrison2023voicesilence` (pp. 80, 85, 90, 94, 99), `dutton1993issueselling` (pp. 398, 404, 409, 410, 414, 421).
Supplementary (preprint): `joshi2025resai` (secs. IV.C, IV.D), `weinberg2025faigmoe` (p. 9), `lee2024questionbank` (p. 14), `stickystories2025` (p. 3; flagged in text as a preprint accepted at CHI 2026), `agenticaiperceptions2025` (pp. 4, 14; flagged as a small preprint survey).
Not cited: `lu2024raipatterns` (no "champion" in the PDF), B6 p. 33, D5's 9% (figure only), the G2 snowball (Detert & Edmondson; Dutton et al. 2001: not in the bib).

## Style pass (Oct 1, 2026)

2.1 v1.2, 2.5 v1.2 and 2.6 v1.4 restyled to Albert's voice (`planning/writing_style_albert.md`). First-person stance 2–3 times per section at the author's own readings (not at reports of sources); connectors; semicolon chains split; closing summaries. No quote, page, key, tally or claim strength changed.
- **Checks:** direct quotes identical (2.1: 23; 2.5: 32; 2.6: 19), key–page pairs identical, markers identical, 0 em dashes. Two citations repeated where a sentence was split so that each quote keeps its page (2.5 ¶4 `rakova2021practitionerperspectives` p. 7:11; no new pages).
- **Words excl. citations (before → after):** 2.1 1,081 → 1,128 · 2.5 1,219 → 1,290 · 2.6 675 → 706. **Drafted total ≈ 3,124 / 6,250.** These counts supersede the table above.

## Sensemaking lens (Oct 2, 2026)

Brief: `planning/sensemaking_edit_prompt.md` (E1–E5 for this chapter). Paragraph plan approved by Albert Oct 2. **Albert's decisions:** edits made in place now (not held back until after the 6 October supervisor meeting); **no trims**: Chapters 2 and 3 may exceed their targets, to be offset in Chapters 4–6; Balasooriya & Sedera cited for the term "sensitizing concept" with the contrast that they used it to build themes; Rouleau's sensegiving described as aimed at clients.

The typology stays the spine. Sensemaking is a second, sensitising lens, not a set of codes. G4–G10 are outside the §11 denominator; the tally (28–29 of 36) is unchanged.

| § | Version | Edit | Words excl. citations (before → after) | Quotes added (all re-checked on the printed PDF page) | Citations added |
|---|---|---|---|---|---|
| 2.6 | v1.4 → v1.5 | E1 ¶1 second lens; E3 ¶2 Balasooriya & Sedera (outside the 36); E2 ¶3 change-recipient research | 706 → ≈ 973 (target 700) | 7: G4 p. 409; G5 p. 70; G6 p. 442; G8 p. 7926; G5 p. 78; G9 p. 546 (×2) | `weick2005organizing`, `maitlis2014sensemaking`, `gioia1991sensemaking` (pp. 442, 443), `balasooriya2026sensemaking` (pp. 7920, 7926), `balogun2004restructuring` (p. 546) |
| 2.5 | v1.2 → v1.3 | E4 ¶5 sensegiving as the third explanation; "neither body of work" → "none of the three bodies of work" | 1,290 → ≈ 1,426 (target 1,250) | 2: G6 p. 443; G6 p. 433 | `gioia1991sensemaking` (pp. 433, 442, 443), `rouleau2005micropractices` (pp. 1428–1429, 1435) |
| 2.1 | v1.2 → v1.3 | E5 last ¶ one sentence on lateral, informal interpretation | 1,128 → ≈ 1,175 (target 1,100) | 1: G7 p. 1574 (checked against the printed page image, not only OCR) | `balogun2005changerecipient` (p. 1574), `balogun2004restructuring` (pp. 524, 526) |

- **Drafted total ≈ 3,574 / 6,250** (2.1 + 2.5 + 2.6); remaining for 2.2–2.4: ≈ 2,676 against a planned 3,200. Supersedes the earlier totals.
- **G7 and G9 are one case** (a recently privatised UK utility, G9 p. 526). 2.1 introduces it as "one case … reported in two papers"; 2.6 ¶3 refers back to "the restructuring case introduced in Section 2.1". If E5 in 2.1 is ever removed, re-word 2.6 ¶3.
- **No quote shared between sections:** G6 p. 442 is quoted in 2.6 and paraphrased in 2.5; G6 p. 443 is quoted in 2.5 and paraphrased in 2.6.
- **Forward reference:** 2.5 ¶5 points to Section 2.6 for the second lens. Not attributed to the authors: "working rule", "carriers / recipients", "receiving end"; the sources' own words ("change recipients", "sensegiving") are used inside quotes.
- Checks: 0 em dashes; first-person count in 2.6 unchanged (two); bib keys all present and ✅ in `reference_list.md`.
- **Figure 2.1:** the "2.6 Lens" strip still names only the typology. Redraw in the orchestration session.

### 2.6 / 2.5 / 2.1 — sources added (S6, cluster G, peer-reviewed)

`weick2005organizing` (G4), `maitlis2014sensemaking` (G5), `gioia1991sensemaking` (G6), `balogun2005changerecipient` (G7, OCR PDF; printed page checked), `balasooriya2026sensemaking` (G8), `balogun2004restructuring` (G9), `rouleau2005micropractices` (G10).

## Dependency: notes for 2.2–2.4 (sensemaking; record only, not drafted)

Written after the depth-case interviews. From `planning/sensemaking_edit_prompt.md`:

- **2.2 (practice first, unclear rules):** an unclear rule is a sensemaking trigger, a cue with ambiguous meaning (G5 p. 70; already quoted in 2.6 ¶1, so paraphrase in 2.2). Rules "can never cover every circumstance" (G4 p. 418) is Weick et al. **quoting Hughes et al.**: cite it as a secondary quotation or not at all.
- **2.3 (ask or act):** acting can come before the interpretation is settled (G4 on action, p. 412). Plausibility over accuracy (G4 p. 415; 3.4 already cites p. 415 for the memos).
- **2.4 (rulings, intermediaries):** a ruling as sensegiving from above; peers as the lateral sensemaking route (G7, G9: one case, cite together; G7 p. 1574 is already quoted in 2.1). A working rule as an enacted, plausible reading (the term "working rule" is this thesis's, not the sources').
- Rouleau's micro-practices are aimed at clients (pp. 1428–1429): do not use them as evidence of upward sensegiving in 2.4.
