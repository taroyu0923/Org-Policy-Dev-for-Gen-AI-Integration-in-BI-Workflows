# Supervisor meeting (Oct 6): consent form on supervisor's template, ethics & integrity section, AI on de-identified data

## Why
At the Oct 6 meeting my supervisor confirmed that this master's thesis needs no ethical review or prior approval: interviews can start once each participant has consented on his template. He approved AI tools on de-identified data only, accepted a sample below 14 and a partial Depth A, and asked for a short section on research ethics and research integrity in the thesis.

## What changed

### Consent and ethics records
- **New:** `research-design/Consent_form_interview_v1.1.docx` — one merged form on the supervisor's template: study information, Teams recording, AI tools on de-identified transcripts only (recordings stay in Teams), deletion on thesis completion, six optional Yes/No permissions, consent by signature or email reply.
- `ethics_determination_note.md` §5 filled (Oct 6 decision, AI condition, consent route).
- `participant_information_sheet.md`, `consent_form.md`, `privacy_notice.md` marked **superseded** (kept for the record).

### Chapter 3
- **3.6 v1.3** retitled *Research ethics and research integrity*: Aalto guidance and the TENK 2023 code (applies to master's theses, p. 9), no review needed (Oct 6), consent process, data protection, AI on de-identified data with checking and an AI use log, integrity paragraph. ≈640 words (budget 300; overrun accepted for Ch3).
- **3.2 v1.2**: a smaller sample is acceptable; adequacy judged by information power; any shortfall reported.
- **3.4 v1.3**: Depth A threshold extended to three or fewer participants, fixed before any Depth A interview.
- **3.5**: one sentence — AI may draft a translation from the de-identified transcript; final wording is mine.
- **3.7**: "No AI tool processed interview content" replaced by a pointer to 3.6.
- `chapters/ch3/README.md`: status and open markers.

### Literature
- **S7 / M12** `tenk2023ri` — Finnish National Board on Research Integrity TENK (2023), *The Finnish Code of Conduct for Research Integrity…* (Publications of TENK 4/2023). Added to `references.bib`, `reference_list.md` (⏳ PDF pending) and `search_log.md` §S7.

### AI rule and records
- Old rule "no interview content into any AI tool" replaced in `README.md`, `analysis/README.md`, `codebook_v0.md` and `familiarisation_memo_template.md`.
- `README.md` status updated to Oct 6; `Pipeline_State.md` has an Oct 6 decisions section; new `planning/session_handoff_2026-10-06.md`.
- `Claude outputs/PR_style-s6-sensemaking.md`: one line (README mention) left over from the previous PR.

## Not in this PR
- Google Docs (thesis draft, interview materials) not yet updated.
- TENK PDF not yet saved locally; `[CHECK: tenk2023ri p. 9 against the PDF]` stays in 3.6.
- Protocol v0.98 unchanged until the pilot.

## Checks
- Consent form rendered to PDF: 2 pages, layout checked.
- No quotes added or changed in Chapter 3; existing quotes, keys and pages untouched.
- `tenk2023ri` renders with pandoc citeproc.
- No organisation names in chapters.
