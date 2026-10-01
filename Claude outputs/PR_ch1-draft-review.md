# Chapter 1 (Introduction) drafted and reviewed; supervisor outline sheet

Branch: `ch1-draft-review` → `main`

## Summary

Chapter 1 is drafted in full (1.1–1.6, about 1,980 words against a 2,000 target). It follows the writing brief and a supervisor-facing outline, with a paragraph plan approved by Albert for every section. The orchestration session then reviewed the chapter against the PDFs, and Albert's two review decisions are applied. The chapter is ready to show the supervisor together with the outline sheet.

## Added

- **`planning/ch1_writing_session_prompt.md`:** two-stage brief (outline + supervisor sheet, then paragraph plan → draft per section), with pre-checked source leads.
- **`planning/ch1_outline_draft_2026-10-01.md`:** supervisor sheet:
  - working title + three candidates matching RQ v2.1;
  - RQ v2.1;
  - chapter map with budgets and status;
  - Chapter 1 outline;
  - eight questions for the supervisor: page count, title, required structure, Ch3 length, ethics confirmation, AI-use rule, gap figure and coding rule, governance-vs-adoption framing.
- **`chapters/ch1/`:**

  | § | File | Words |
  |---|---|---|
  | 1.1 | `1.1_genai_in_bi_work.md` (BI context, GenAI shifts the analyst's task) | 535 |
  | 1.2 | `1.2_rules_and_practice.md` (rules arrive; shadow IT) | 341 |
  | 1.3 | `1.3_problem.md` (governance seen only from above; 28 or 29 of 36) | 274 |
  | 1.4 | `1.4_aim_rqs.md` (aim, RQ v2.1, BI practitioner definition, verbatim) | 324 |
  | 1.5 | `1.5_approach_scope.md` (approach, three scope limits, governance not adoption) | 299 |
  | 1.6 | `1.6_contribution_structure.md` (three intended contributions, chapter roadmap) | 204 |

  - `README.md` (status, sources, dependencies, open markers, change log).

- **`README.md` (project):**
  - Chapter 1 status and the `chapters/ch1/` folder added.
  - Ch2 updated: 2.5 v1.1 reviewed, 2.6 v1.3.
  - Proposed title noted next to the registered one.
  - Note fixes and the S1 reconstruction ticked off.
  - Supervisor-meeting item points to the question list.

## Review (orchestration, Oct 1)

- **21/21 direct quotes** found on the cited printed pages: E5 Ain, E6 Gu, B1 Taeihagh and D1 Papagiannidis by pdftotext; G1 Haag & Eckhardt (p. 469) and B9 Silic (p. 11) by OCR.
- **7 citation keys**, all in `references.bib` and all verified peer-reviewed; no preprints.
- RQ v2.1 and the BI practitioner definition are verbatim. The tally matches 2.6 v1.3.
- No em dashes, no style-list hits, no organisation names, no interview data.
- **Changes applied:**
  - **1.1 v1.1:** sector list removed from the motivation sentence ("across several industries"). Together with 3.5 and the case labels it could have let a reader map cases to the author's former employers (Albert).
  - **1.2 v1.1:** Taeihagh p. 3 quote shortened (the source sentence has a subject–verb slip).
  - **1.3 v1.1:** governance definition cited `[@mantymaki2022definingaigov, pp. 604–605]` (paraphrase, PDF-checked; still no direct quote) (Albert).
  - **1.6 v1.1:** contribution (iii) worded as an aim.
  - Supervisor sheet: chapter map updated (Ch1 drafted); AI-use question kept as in the current Chapter 3 version (Albert).

## Dependencies recorded

- 1.4 ¶4 = 3.2 ¶1: the BI practitioner definition is verbatim in both. Change both together.
- 1.3 ¶2 restates the 2.6 tally; update with 2.6 ¶2 and 3.7 ¶2 if it changes.
- 2.2 refers back to 1.2 for the shadow IT definition.
- 1.5 ¶1 `[PENDING: interviews Oct 5–19]`. Check against 3.3 after the pilot.

## Check before merging

- [ ] Supervisor sheet reads well on its own (no organisation names).
- [ ] 1.1 ¶4 motivation sentence acceptable as revised.
- [ ] Only the files listed here are staged (line-ending-only changes excluded).

## Still open (not in this PR)

- Supervisor meeting (questions in the sheet).
- Consent pack and pilot before Oct 5.
- 3.3 after the pilot.
- 2.2–2.4 after the depth-case interviews.
- Pandoc render test at build (`--citeproc` not available on this machine).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01PHVGEHLC9jnxhPm5Zkk6we
