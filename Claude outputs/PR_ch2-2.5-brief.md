# Chapter 2 §2.5 writing brief, source pre-check, budget restored

Branch: `ch2-2.5-brief` → `main` (branched from `ch3-drafts-review`; merge that PR first)

## Summary

This PR adds a writing brief for Section 2.5, *Does anything go up?* (1,250 words). It is the one Chapter 2 section that fieldwork does not block. The brief is waiting for Albert's approval, and no prose has been drafted. While writing the brief, the sources were pre-checked against the PDFs; the check turned up one source whose note content is not in the paper. The 25,000-word budget, lost again from the repo copy of `Pipeline_State.md`, is restored.

## Added

- **`planning/ch2_2.5_writing_prompt.md`** follows the format of `ch2_writing_session_prompt.md`: files to read first, settled items and a suggested six-paragraph skeleton.
  - Skeleton: K7 prescribed → loops observed only on systems → absent channels → champions (K8) → voice/silence and issue selling → open SQ2 questions.
  - A source pre-check table gives printed pages for each source.
  - It also sets the source and argument rules, the procedure (paragraph plan first, then wait) and a copy-paste prompt.

## Source pre-check (pdftotext on 13 PDFs)

- **C10 Asatiani is checked for its use in 2.5.** Its feedback loop is observed, but at system level: user feedback adjusts the AI application (p. 275), not the usage rules. Printed page = PDF page + 258.
- **⚠ The D6 Lu "AI Ethics Champion" pattern is not in the PDF.** "Champion" occurs zero times in the text, so the note's §3, §7 and §11(d–e) are NotebookLM content.
  - D6 is dropped from 2.5.
  - Open for Albert: K8/K9, the 2.4 source list and D6's §11 verdict. The §11 tally was **not** changed.
- **G2 Morrison** does not use the term "lateral voice"; she restricts voice to upward voice (p. 80).
- **Note page errors:** B1 pp. 7–8 (the note says p. 6) · B5 p. 9 (p. 8) · B8 p. 44 (p. 43) · D5's 9% appears only in Fig. 7.

## Updated

- **`planning/Pipeline_State.md`:**
  - The 25,000-word budget is restored a second time. The repo copy still had "18–24k"; the Claude-project mirror had the restore.
  - "Chapter drafting" and "Ethics" rows are updated.
  - A new section, "§2.5 source pre-check", is added.
- **`planning/session_handoff_2026-10-01.md`:** the state table, open items and next steps are updated, and a session log is appended.
- **`chapters/ch2/README.md`:** the 2.5 row now reads "Brief ready", and a D6 caution is added.

## Check before merging

- [ ] The budget paragraph in `Pipeline_State.md` reads 25,000 (Standing constraints).
- [ ] The 2.5 brief is approved, or the requested changes are noted.
- [ ] No interview content and no organisation names in the diff.

## Still open (not in this PR)

- Drafting 2.5 (writing session, after approval) and reviewing the draft.
- The D6 decision (§11 re-read; K8/K9; the 2.4 list).
- Fixing the page errors in the B1, B5 and B8 notes.
- Everything listed in the handoff §6: consent pack, pilot, supervisor meeting, I7/I10 PDFs.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01PHVGEHLC9jnxhPm5Zkk6we
