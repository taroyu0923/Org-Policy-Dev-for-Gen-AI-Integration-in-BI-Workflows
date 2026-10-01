# Reference clean-up: S3 §11 spot-check, note page fixes, bib-key fixes, S1 partial reconstruction

Branch: `s3-spotcheck-note-fixes` → `main`

## Summary

The §11 verdicts of the 12 remaining S3 notes were checked against their PDFs (C7 by OCR). Logged page errors in 14 notes are corrected, 8 note headers that pointed to bib keys not in `references.bib` are fixed, and the S1 search record is partly reconstructed.

**No chapter text and no tally changed.** The spot-check shows that the 2.6/3.7 range explanation no longer holds; the tally waits for Albert's decision on the coding rule.

## Added

- **`planning/s3_section11_spotcheck_2026-10-01.md`**: summary table, recount, rule options and per-note evidence.
  - Proposed recodes:
    - C7 → documented absence (its practitioner finding is cited from Vakkuri et al. 2019);
    - C8 → documented absence (normative framework, hypothetical example);
    - C10 → partial.
  - A12 contested (executive-reported data on *information* governance).
  - Recount: **25–26 of 36**.
  - Rule decision: R1 (data only, recommended; needs a phase-2 check of the Sep 4 not-absences) or R2 ("names the gap" = partial).

## Changed

- **14 notes** (A8, A10, A12, B1, B4, B5, B8, C7, C8, C10, D1, D5, E2, G2): a "PDF page check (Oct 1, 2026)" block giving printed-page offsets, corrected pages, quotes not in the PDF and proposed verdicts.
  - Notable: **E2's "research agenda" gap quote is not in the paper**; **B4's "slow, rigid, or absent"** is not in the paper; **G2 has no "lateral voice"**; the **C7 PDF** is an image-only print-out (get the publisher PDF).
- **8 notes** (A8, A9, A10, A12, C9, D7, E3, E4): bib-key header corrected to match `references.bib`.
- **`literature/search_log.md`:**
  - S1 databases and strings partly reconstructed from Research Plan §2.4. These are planned sources, flagged for Albert to confirm.
  - Includes the S5 entry added Oct 1 by the Chapter 3 session, which had not been committed.
- **`planning/Pipeline_State.md`** and **`planning/session_handoff_2026-10-01.md`:** results, open decision, next steps.

## Check before merging

- [ ] Line-ending-only changes discarded (`planning/s3_postcheck_2026-09-11.md`, `research-design/README.md`, `research-design/recruitment_email.md`).
- [ ] S1 reconstruction wording acceptable (planned, not recorded).

## Still open

- Rule decision (R1/R2), then phase 2 (under R1).
- Update 2.6 ¶2, 3.7 ¶2 and the README tally.
- Claims map K6: drop C8.
- §12 pass after the pilot; cluster memos after the tally is settled.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01PHVGEHLC9jnxhPm5Zkk6we
