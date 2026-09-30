# analysis/

Rolling analysis during fieldwork (Oct 5–19, 2026) and thematic analysis afterwards (~Nov 7).
Created Sep 29, 2026.

## ⚠ What lives where

| Material | Where | Why |
|---|---|---|
| Recordings, transcripts, consent forms | **Aalto OneDrive** only | Privacy notice §7: data stored only in Aalto's Microsoft 365 environment |
| **Filled** contact summaries, familiarisation memos, interview log, coded transcripts | **Aalto OneDrive** only — suggested folder `Thesis-Interviews/` (below) | They contain interview content. Pseudonymised is still personal data |
| **Templates** and the **codebook** (definitions, no interview content) | This repo, `analysis/templates/` | No participant data |
| Anonymised findings drafts | `chapters/`, later | Only after the anonymisation rules in `sampling_frame.md` §6 are applied |

**Never commit a filled template.** `analysis/working/` is gitignored as a safety net, but the working copies belong in OneDrive, not in the repo folder.

**AI rule (privacy notice §7):** no AI tool sees interview content. The codebook may be worked on with AI only while every example in it is an anonymised paraphrase (no names, organisations, teams, products, dates, or verbatim quotes).

## Suggested OneDrive layout

```
Thesis-Interviews/
  00_consent/            signed forms (separate from transcripts)
  01_recordings/         delete after transcription check
  02_transcripts/        P01.docx … P14.docx
  03_contact_summaries/  P01_contact.md …      ← within 24h
  04_memos/              P01_memo.md …         ← within 48h
  05_coding/
  interview_log.md       one line per interview
  key.xlsx               participant number ↔ name (password-protected, kept apart from everything else)
```

## Per interview

| When | What | Template |
|---|---|---|
| Before | Fill "what I knew beforehand" (reflexivity) | `familiarisation_memo_template.md` §0 |
| Within 24h | Contact summary (protocol §9) | `contact_summary_template.md` |
| Within 48h | Familiarisation memo | `familiarisation_memo_template.md` |
| Same day as memo | One log line; new code candidates → codebook "candidates" table (anonymised paraphrase only) | `interview_log_template.md`, `codebook_v0.md` |

## Files

- `templates/contact_summary_template.md`
- `templates/familiarisation_memo_template.md`
- `templates/interview_log_template.md`
- `templates/codebook_v0.md`
