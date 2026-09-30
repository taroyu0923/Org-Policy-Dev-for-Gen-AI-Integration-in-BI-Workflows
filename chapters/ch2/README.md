# Chapter 2 — Literature review (drafts)

Structure: outline v2 (loop structure), **adopted** Sep 29, 2026 — `planning/ch2_outline_draft_2026-09-29.md`. Claims: `planning/ch2_claims_map_2026-09-29.md`. Session brief: `planning/ch2_writing_session_prompt.md`.
Writing order: 2.1 → 2.6 → 2.5 → (after the Shopee interviews) 2.2 → 2.3 → 2.4.

| § | File | Heading | Status | Words (target ±10%) | Last updated |
|---|---|---|---|---|---|
| 2.1 | `2.1_how_rules_arrive.md` | How does the literature assume rules arrive? | **Draft v1.1** (edit pass E1–E5) — awaiting Albert's review | 1,085 excl. citations / 1,134 incl. (1,100) | Sep 30, 2026 |
| 2.2 | — | When practice comes first, and when rules are unclear | Not started (after Shopee interviews) | — (1,100) | — |
| 2.3 | — | Asking or acting: explanations of bypass | Not started (after Shopee interviews) | — (1,100) | — |
| 2.4 | — | Rulings and the people in between | Not started (after Shopee interviews) | — (1,000) | — |
| 2.5 | — | Does anything go up? | Not started (next) | — (1,250) | — |
| 2.6 | `2.6_lens_and_gap.md` | What lens does the literature offer, and what does it leave unstudied? | **Draft v1.1** (edit pass E1–E2) — awaiting Albert's review | 669 excl. citations / 687 incl. (700) | Sep 30, 2026 |
| | | | **Total** | **1,754 / 6,250** (budget revised Sep 30: 25,000-word thesis) | |

## Dependencies

- **2.3 must raise, as an open question, whether a given use began before any rule existed or continued around one.** 2.6 ¶4 ends: "which is the distinction 2.3 left open". If 2.3 does not raise it, edit 2.6 ¶4.
- 2.6 ¶2 placeholder `Section [3.X]`: Chapter 3 must describe the §11 screening (question, verdict vocabulary, why a range: C7/C8 contested).
- **B9 confirmed positive by Albert (Sep 29–30)**, so 2.6's tally stands: 22–24 of 36 governance sources (61–67%). A9 recoded partial (Sep 30) does not change it.
- Bib: `abraham2019datagovframework` renders the surname as "Brocke" (particle "vom" not protected). Check with `apa.csl` at build; fix in the bib if needed (e.g. `{vom Brocke}, Jan`).

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

- **v1.1 (Sep 30, 2026)** — edit pass from `planning/ch2_edit_prompt_2.1_2.6.md` (review `planning/ch2_review_2026-09-30.md`): E1 narrative citations (both); E2 Papagiannidis 2023/2025 disambiguated (2.6); E3 *rule* widened to written or unwritten (2.1 ¶1); E4 2.1 ¶2 regrouped; E5 Orr & Davis marked as secondary citation in APA form (2.1 ¶2); E6 this README. No quote, page, tally, source or heading changed.

## 2.1 — sources used

Carrying (peer-reviewed): `mantymaki2022definingaigov`, `birkstedt2023themesgaps`, `abraham2019datagovframework`, `lu2024raipatterns`, `ismail2025frameworks`, `tallon2013informationartifact`, `responsibleaigovreview`, `rakova2021practitionerperspectives` (PDF only).
Supplementary (preprint): `joshi2025resai`, `lee2024questionbank`, `batool2024aigov`, `batool2024rai`, `agarwal2025fivelayer`, `luna2024paradigms`, `weinberg2025faigmoe`.
Not used: A9, C10 (not PDF-verified), B9 (belongs to 2.2/2.3/2.6).

## 2.6 — sources used

Carrying (peer-reviewed): `tallon2013informationartifact`, `abraham2019datagovframework`, `papagiannidis2023towardaigov` (PDF-verified Sep 30; §11 recoded partial), `responsibleaigovreview`, `birkstedt2023themesgaps`, `mantymaki2022definingaigov`, `rakova2021practitionerperspectives` (PDF only), `silic2025shadowai`.
Supplementary (preprint): `stickystories2025` (flagged in text as a preprint accepted at CHI 2026).
Open: placeholder `Section [3.X]` for the §11 screening method (to be written in Chapter 3).
