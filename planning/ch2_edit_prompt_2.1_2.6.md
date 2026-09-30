# Edit pass — Chapter 2 sections 2.1 and 2.6 (v1 → v1.1)

**Created:** Sep 30, 2026 | **Model:** Opus (thesis prose) | **Input:** `planning/ch2_review_2026-09-30.md`
**Scope:** revise the two existing drafts only. No new sources, no new claims, no structural change.

## Files

- `chapters/ch2/2.1_how_rules_arrive.md` (v1, 1,094 words)
- `chapters/ch2/2.6_lens_and_gap.md` (v1, 661 words)
- `chapters/ch2/README.md` (status table)

## Edits

| # | Where | Edit |
|---|---|---|
| E1 | Both sections, every citation | **Narrative citations where the author is named in the sentence.** Replace `Mäntymäki et al. call it "…" [@mantymaki2022definingaigov, p. 604]` with `@mantymaki2022definingaigov [p. 604] call it "…"` (renders "Mäntymäki et al. (2022, p. 604) call it…"). Keep bracketed `[@key, p. N]` only where the author is **not** named in the sentence. Do not name an author in the sentence *and* in the brackets. |
| E2 | 2.6 ¶1–2 (and anywhere else) | **Disambiguate Papagiannidis.** `papagiannidis2023towardaigov` = Papagiannidis et al. (2023), the three-firm study; `responsibleaigovreview` = Papagiannidis, Mikalef & Conboy (2025), the review. With narrative citations (E1) the year appears automatically — check every "Papagiannidis et al." in the text is tied to the right key, and that a reader can tell the study from the review ("their 2023 field study", "the 2025 review"). |
| E3 | 2.1 ¶1, last sentence | **Widen the definition of "rule".** Replace "In this study, a *rule* is any statement by the organisation of what BI practitioners may or may not do with generative AI, however it is conveyed." with: *"In this study, a rule is any expectation, written or unwritten, about what BI practitioners may or may not do with generative AI, however it reaches them: a document, a ruling on a request, a blocked tool or a colleague's advice."* Minor wording changes allowed; keep "written or unwritten" and the four forms. |
| E4 | 2.1 ¶2 | **De-catalogue.** Same sources, same claims, regrouped into three moves with fewer "X says… Y says…" transitions: (a) general and data governance place rule-making above the practitioner (Mäntymäki, Abraham, Lu, Ismail); (b) GenAI frameworks state the cascade outright (Joshi, Lee — preprints, supplementary); (c) practitioners appear as the governed (Batool, Birkstedt), then the closing point that the cascade is prescribed, not observed (61 of 68 conceptual). Keep every citation and page; do not add or drop a source. |
| E5 | 2.1 ¶2 | **Secondary source.** "the parameters are set by legislation, organizational norms and clients" is Birkstedt et al. summarising Orr and Davis (2020). Attribute it: e.g. "Birkstedt et al., summarising Orr and Davis (2020), note that practitioners implement ethics while 'the parameters are set by…'". Do **not** add Orr and Davis to `references.bib` or cite them directly — the thesis has not read that paper. |
| E6 | `chapters/ch2/README.md` | **Log the forward dependency.** Add a "Dependencies" note: 2.6 ¶4 says "the distinction 2.3 left open" — **2.3 must raise, as an open question, whether a given use began before any rule existed or continued around one.** Also note: B9 confirmed positive by Albert (Sep 30), so 2.6's tally (22–24 of 36, 61–67%) stands. **Update the README targets** to the revised budget (Sep 30): 2.2 1,100 · 2.3 1,100 · 2.4 1,000 · 2.5 1,250 · total **6,250**. |

**Not to change:** the tally figures in 2.6; any quote's wording or page (all checked against the PDFs on Sep 30); the prescribed/observed framing; the section headings; the order of paragraphs other than within 2.1 ¶2.

## Rules carried over from `planning/ch2_writing_session_prompt.md`

- Every citation key must exist in `literature/references.bib`; preprints stay supplementary.
- If an edit changes a quote's surrounding sentence, the quote itself stays verbatim.
- Style: claim first, UK spelling, no throat-clearing, at most two em dashes per page, avoid the listed AI-typical words.
- Word count stays within ±10% of target (2.1: 990–1,210; 2.6: 630–770).

## Procedure

1. Read `planning/ch2_review_2026-09-30.md`, then both drafts.
2. **Show Albert the revised 2.1 ¶1 last sentence and the regrouped 2.1 ¶2 first** (E3, E4) and wait for approval.
3. Apply E1–E6.
4. Report: word counts before/after; a list of every citation changed from bracketed to narrative; confirmation that no quote wording or page changed (diff the quoted strings); citation keys checked against `references.bib`.
5. Bump both drafts' header comment to **v1.1, Sep 30, 2026** with a one-line change note, update the README table, and re-list `chapters/ch2/`.

## Delivery

Write into the repo via the file-commit tools (the Cowork shell cannot mount the folders). Do not commit or push.

---

## Copy-paste prompt

```
Read planning/ch2_edit_prompt_2.1_2.6.md in my repo, then planning/ch2_review_2026-09-30.md,
then chapters/ch2/2.1_how_rules_arrive.md and chapters/ch2/2.6_lens_and_gap.md.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo). The
Cowork shell cannot mount my folders -- use the file listing/staging/commit tools. Do not commit
or push; I push myself.

Task: apply edits E1-E6 from the prompt file to 2.1 and 2.6 (v1 -> v1.1). This is a revision
pass only -- no new sources, no new claims, no change to quotes, pages, tally figures or headings.

FIRST show me the new last sentence of 2.1 paragraph 1 (definition of "rule") and the regrouped
2.1 paragraph 2, and WAIT for my approval. Then apply everything.

When done: word counts before/after (2.1 must stay 990-1,210; 2.6 630-770), the list of citations
you changed to narrative form, confirmation that every quoted string is unchanged, citation keys
checked against literature/references.bib. Update chapters/ch2/README.md (including the
2.3 dependency note) and re-list chapters/ch2/.
```
