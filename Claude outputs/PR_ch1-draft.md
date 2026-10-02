# PR: Chapter 1 drafted (v1) + outline and supervisor sheet

**Branch:** `ch1-draft` (from `main`)

## Commands

```bash
git switch -c ch1-draft
git add planning/ch1_writing_session_prompt.md planning/ch1_outline_draft_2026-10-01.md \
        chapters/ch1/ \
        chapters/ch2/README.md planning/Pipeline_State.md planning/session_handoff_2026-10-01.md \
        "Claude outputs/PR_ch1-draft.md"
git diff --cached --stat        # expect 13 files; nothing else staged
git commit -m "Chapter 1 v1 (1,977 words) + outline and supervisor sheet"
git push -u origin ch1-draft
```

Only add the files above. The other modified files in `git status` (e.g. `Claude outputs/PR_*.md`, `analysis/templates/*`, `chapters/ch2/2.1`, `2.6`) were not touched by this session; check them separately for line-ending-only changes before committing anything else.

## Summary (paste into the PR description)

**Chapter 1 (Introduction) drafted, v1: 1,977 words excl. citations (target 2,000).**

**Stage 1 — outline and supervisor sheet** (`planning/ch1_outline_draft_2026-10-01.md`, approved): working title *Governance Seen from Below: How BI Practitioners Encounter, Interpret and Act on Their Organisations' Rules for Generative AI* plus three candidates; RQ v2.1; chapter map with budgets and status; Chapter 1 outline with sources; eight questions for the supervisor (page count, title, required structure, Ch3 length, ethics confirmation, AI-use rule, R1 coding rule and gap figure, governance-vs-adoption framing).

**Stage 2 — sections** (`chapters/ch1/`, each from a paragraph plan approved before drafting):

| § | File | Words |
|---|---|---|
| 1.1 | Generative AI arrives in business intelligence work | 535 |
| 1.2 | Rules arrive, and practice may already be there | 341 |
| 1.3 | The problem: governance seen only from above | 274 |
| 1.4 | Aim and research questions | 324 |
| 1.5 | Approach and scope | 299 |
| 1.6 | Intended contribution and thesis structure | 204 |

**Checks**
- 6 citation keys, all ✅ peer-reviewed and in `references.bib`: `ain2019bisuccess`, `gu2024analystsverify`, `taeihagh2025govgenai`, `responsibleaigovreview`, `haag2017shadowit`, `silic2025shadowai`.
- 21 direct quotes, each matched on the cited printed page: E5 pp. 1, 4, 8, 10; E6 pp. 1, 8, 11; B1 pp. 2, 3, 4; D1 p. 7; G1 p. 469 (OCR); B9 p. 11 (OCR). No quote shared with Chapter 2.
- 0 em dashes, no style-list hits, no organisation names, no interview data.
- Open marker: 1.5 `[PENDING: interviews Oct 5–19]`.
- Pandoc render not tested (local pandoc 2.9 has no citeproc).

**Decisions recorded** (session handoff log): motivation sentence in 1.1; 1.5/1.6 separate; no GenAI-in-BI-tools market sentence; shadow IT definition verbatim in 1.2 (2.2 refers back); tally in 1.3 as count only; BI practitioner definition verbatim in both 1.4 and 3.2; 1.6 lens contribution kept as an aim.

**Source-lead corrections:** B9 unauthorised use is executive-reported (p. 11); B1 "sensitive information" is p. 4; E5 reporting/analytics is p. 10.

**Also changed:** `chapters/ch2/README.md` (dependency: 2.2 refers back to 1.2; 1.3 restates the tally), `planning/Pipeline_State.md` (Chapter drafting row; budget paragraph intact), `planning/session_handoff_2026-10-01.md` (Chapter 1 log; file normalised to LF like the committed copy). `planning/ch1_writing_session_prompt.md` (the brief) was untracked and is added here.
