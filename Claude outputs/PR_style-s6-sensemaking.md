# Style pass, S6 sensemaking sources, sensemaking lens in Ch1–3, figures and memo templates

## Summary

This PR brings together the work of Oct 1–2, 2026: a style pass of all drafted sections into Albert's own voice; seven new sensemaking sources (S6, Cluster G); the sensemaking lens added to Chapters 1–3 on the supervisor's suggestion; two figures; and memo templates updated for the pilot.

### 1. Style pass (Oct 1)
- New `planning/writing_style_albert.md`: voice rules drawn from three of Albert's own papers (signposting, explicit connectors, shorter sentences, plain closing summaries, "I argue / In my view" at most 1–3 times per section in Ch1–2).
- Restyled: 1.1–1.6, 2.1, 2.5, 2.6, 3.1, 3.2 and 3.4–3.7. Every quote, page, citation key, marker, the RQ and the BI practitioner definition were checked identical before and after.

### 2. S6 add-reference pass (Oct 2): Cluster G 3 → 10
- G4 Weick, Sutcliffe & Obstfeld (2005)
- G5 Maitlis & Christianson (2014)
- G6 Gioia & Chittipeddi (1991)
- G7 Balogun & Johnson (2005), OCR only: no text layer
- G8 Balasooriya & Sedera (2026), the supervisor's paper
- G9 Balogun & Johnson (2004), same case as G7
- G10 Rouleau (2005)

How they were processed:
- Template v2.4-T (no §11), so they sit outside the denominator. **The governance corpus stays at 36, and the §11 tally stays at 28–29 of 36.**
- Notes and `_raw` files added; 7 bib entries; `search_log.md` §S6; `reference_list.md` regenerated.
- Orchestration review: every quote re-checked against the PDFs (G7 by fresh OCR).
- DOIs added from Crossref for G6 (10.1002/smj.4250120604) and G9 (10.2307/20159600).
- G8's issue number (6) confirmed from the PDF's download stamp.

### 3. Sensemaking as the second lens (Oct 2, supervisor's suggestion)
The structural / procedural / relational typology stays the spine. Sensemaking is added beside it as a sensitising lens, not as codes. Paragraph plans were approved before drafting; all new quotes were checked against the PDFs.

| Section | Change |
|---|---|
| 2.6 v1.5 | Second lens (sensemaking + sensegiving); Balasooriya & Sedera as the one sensemaking study of AI (outside the 36); change-recipient research on the "recipient" framing |
| 2.5 v1.3 | Sensegiving as a third explanation beside voice and issue selling |
| 2.1 v1.3 | Lateral, informal sensemaking among change recipients (G7/G9 cited as one case) |
| 1.5, 1.6 v1.3 | Light touch: two lenses named |
| 3.4 v1.2 | Sensemaking guides the memos and adds no codes or themes |

Words after the edits: 2.1 1,176 · 2.5 1,430 · 2.6 1,005 · 3.4 792. **Albert's decision (Oct 2): Chapters 2 and 3 may exceed their budgets; the 25,000 total is rebalanced when Chapters 4–6 are planned.**

### 4. Figures (`chapters/figures/`)
- `fig2_1_rule_path.png`: the path a rule is assumed to take (2.1 → 2.5), with a lens strip naming both lenses.
- `fig2_2_screening.png`: the 36-source screening under R1 (28 absence · 1 contested · 2 partial · 5 substantive or positive).
- The tables added in the supervisor Google Doc (Tables 1.1, 2.1, 2.2, 3.2, 3.3) exist there only; they are to be ported to the chapter markdown later.

### 5. Templates (approved Oct 2)
- **Familiarisation memo:** new §3a (cue, plausible reading, who it was talked over with) and a sensegiving line in §4.
- **Codebook v0 §E:** sensemaking named as a sensitising lens, adding no codes (change log row added).
- **Contact summary:** a "talked it over with" line.
- **Pilot debrief:** a check that decides whether v1.0 needs a follow-up question after B2, asked in Albert's own words rather than read from the wording card.
- **Unchanged before the pilot:** protocol v0.98, the wording card and the consent pack.

### Planning and records
Project `README.md` (status as of Oct 2: style pass, S6, sensemaking lens, figures, templates, supervisor meeting); `Pipeline_State.md` (S6 counts, word-budget decision), the session handoff, the chapter READMEs (word counts, sources, dependencies), and the briefs `s6_addref_prompt.md` and `sensemaking_edit_prompt.md`.

## Not in this PR
- Splitting 2.6 ¶1 into two paragraphs (suggested, no word change).
- Porting the Google Doc tables.
- Protocol v1.0 (after the pilot).
- Maitlis (2005) for the sensemaking typology (a later pass).
