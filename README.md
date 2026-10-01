# Organizational Policy Development for Generative AI Integration in BI Workflows
**A Qualitative Analysis of Governance Framework Evolution** *(registered title; proposed replacement for discussion with the supervisor: **Governance Seen from Below: How BI Practitioners Encounter, Interpret and Act on Their Organisations' Rules for Generative AI**; see `planning/ch1_outline_draft_2026-10-01.md`)*

MSc Business Analytics thesis — Liu Yu-Shu (Albert), Aalto University.

Organisations adopting generative AI in business intelligence (BI) work govern it through rules: policy documents, rulings on requests, blocked tools and colleagues' advice. The governance literature describes those rules from the top down, through published frameworks, and almost never observes the people they land on. This thesis studies the receiving end, through interviews anchored in specific incidents with BI practitioners in nine organisations.

## Research question (v2.1, adopted Sep 2026)

- **Main:** How do BI practitioners encounter, interpret and act on their organisation's rules for generative AI use?
- **SQ1 (downward):** What happens when they use, or try to use, GenAI in their analytical work, and how do the rules shape what they do next?
- **SQ2 (upward):** Do their requests or concerns travel upward to whoever decides the rules, and what comes back?

**BI practitioners** are people who produce, maintain or directly supervise analytical outputs that others use to make decisions, and who neither set their organisation's GenAI rules nor hold a formal responsible-AI or AI-governance role. Evolution of policy is **not** promised by the RQ. It becomes a findings strand only if a threshold fixed before the interviews is met (`planning/structure_discussion_log_2026-09-11.md`).

## Repo layout

```
planning/            Pipeline_State.md (canonical state), session handoffs, outlines,
                     claims map, writing briefs, review logs, PDF-check logs
literature/
  notes/             One Markdown note per source, cluster-numbered ID:
                     <ID>_<author><year>_<slug>.md  (e.g. A1_batool2024_...)
                     Governance A–E: v2.4, §1–§11 (§11 = working-tier reception)
                     Theory anchors G1–G3 · Methods M1–M11 · Interview design I1–I14
  _raw/              Verbatim NotebookLM outputs + PDF verification logs
  cluster-memos/     Synthesis memos (empty)
  references.bib     BibTeX — single source of truth for per-reference status
  reference_list.md  Generated audit view of references.bib
  search_log.md      Search passes S1–S5: queries, dates, hits, kept/rejected
research-design/     Protocol, wording card, consent pack, privacy notice, sampling frame,
                     ethics note, pilot debrief template
chapters/            Thesis chapters in Markdown (pandoc [@key]); LaTeX in November
  ch1/               Introduction — README tracks status, word counts, sources, dependencies
  ch2/               Literature review — README tracks status, word counts, sources
  ch3/               Method — README tracks status and open [FILL]/[PENDING] markers
analysis/            Codebook v0 and templates only; filled templates live on Aalto OneDrive
interviews/          Fieldwork outputs (gitignored)
latex/               Aalto template + converted output
Claude outputs/      PR descriptions and session outputs
```

### `research-design/`

| File | Purpose |
|---|---|
| `interview_protocol_v0.98.md` | Semi-structured guide aligned to RQ v2.1: critical-incident anchor, three phases, tier branches, C1a / D2a / E3a probes; v1.0 after the pilot |
| `wording_card_bilingual.md` | Fixed EN / 繁中 wording for the core items |
| `pilot_debrief.md` | Template for the pilot → protocol v1.0 |
| `sampling_frame.md` | Cases, tiers, inclusion criterion, sequencing, confidentiality rules |
| `participant_information_sheet.md`, `consent_form.md`, `privacy_notice.md` | Consent pack (consent is the legal basis; document access and quotation are separate permissions) |
| `recruitment_email.md` | Contact and scheduling templates |
| `ethics_determination_note.md` | Aalto ethical-review criteria; supervisor confirmed no review required (§5 to be filled) |

## Design at a glance

- **Embedded multiple-case design**, 14 participants in 9 organisations across 5 countries, recruited from the researcher's professional network.
  - **Depth stratum:** two organisations, 7 participants across tiers.
  - **Breadth stratum:** 7 single-informant cases.
  - The two strata are analysed separately and never pooled.
- **Reporting:** cases are reported only by case label (sector and country), never by organisation name. See `chapters/ch3/README.md`.
- **Critical-incident anchor:** a bounded three-type menu, each incident process-traced with the same four questions.
- **Analysis:** codebook thematic analysis.
  - A priori spine: the structural / procedural / relational practice typology (Papagiannidis et al., 2025; after Tallon et al., 2013).
  - Inductive codes for everything BI-specific.
  - The ask / act-now loop is a sensitising lens, not a set of codes.
  - Re-coding and supervisor review are consistency checks, not reliability measures.
- **Languages:** English and Taiwanese Mandarin; core items are fixed in both.

## Conventions

- **Citations:** pandoc `[@key, p. N]`; narrative `@key [p. N]` when the author is named. `references.bib` is the only place per-reference status is recorded. Cite ✅ entries only; preprints are supplementary.
- **Verification:** NotebookLM answers are leads, not evidence. Every quote and page is checked against the PDF before it enters a chapter. Two notes (D7, D6) were found to contain NotebookLM content that is not in the paper, so the §11 verdicts of the S3 notes are being re-checked against the PDFs.
- **Truthfulness markers:** `[PENDING: …]` for steps not yet done, `[FILL: …]` for unknown numbers, `[CHECK: …]` for open rules.
- **Literature queries:** template v2.4 (`planning/query_template_v2.4.md`).

## Privacy and anonymity

- No participant data enters this repository; interview content never goes into any AI tool. Teams transcription on the Aalto account is the only exception.
- Consent forms, recordings, transcripts and filled analysis templates live on Aalto storage only.
- Organisations are never named in chapters.
- `.gitignore` covers `interviews/transcripts/` and the participant-data paths; source PDFs are not redistributed.

## Status

*Updated Oct 1, 2026. Detail: `planning/Pipeline_State.md` and `planning/session_handoff_2026-10-01.md`.*

**Word budget:** 25,000 words. Intro 2,000 · literature review 6,250 · method 3,000 (allowed to run to ~3,350) · findings 8,000 · discussion 4,250 · conclusion 1,500.

**Chapters**
- [x] **Ch1 drafted and reviewed:** 1.1–1.6, ≈1,980 of 2,000 words (Oct 1); 21/21 quotes PDF-checked. Supervisor sheet: `planning/ch1_outline_draft_2026-10-01.md`
- [x] **Ch2:** outline v2 adopted (a loop structure following how a rule is expected to travel). Claims map K1–K11.
- [x] **Ch2 drafted:** 2.1 v1.1 (1,085 words) · 2.5 v1.1 (1,211, reviewed; 32/32 quotes PDF-checked) · 2.6 v1.3 (669) — ≈2,965 of 6,250
- [ ] **Ch2 remaining:** 2.2–2.4, after the depth-case interviews
- [x] **Ch3:** 3.1, 3.2, 3.4–3.7 drafted and reviewed (~2,607 words + Table 3.1)
- [ ] **Ch3 remaining:** 3.3, after the pilot. `[FILL]` / `[PENDING]` markers to be completed after fieldwork.
- [ ] Ch4–Ch6 after analysis · title revision (supervisor)

**Literature**
- [x] **Corpus:** 36 governance notes (Clusters A–E plus B9) · theory anchors G1–G3 · methods M1–M11 (PDF-checked) · interview design I1–I14 (verified)
- [x] **Working-tier screening (§11):** **28–29 of 36 governance sources (78–81%)** contain no account of how staff below the rule-setting level receive AI governance.
  - Updated Oct 1: every verdict PDF-checked under coding rule R1 (data on staff reception of AI governance only); `planning/s3_section11_spotcheck_2026-10-01.md`.
- [x] **§11 verdicts PDF-checked (S3 + phase 2), rule R1** — Oct 1
- [x] **Note fixes (Oct 1):** PDF page-check blocks in 14 notes; 8 bib-key headers corrected; C7 publisher PDF in place
- [x] **S1 search** partly reconstructed from the Research Plan §2.4 (planned sources; to confirm)
- [ ] §12 protocol-craft pass on I1–I14 (after the pilot) · cluster memos

**Design and fieldwork**
- [x] RQ v2.1, BI practitioner definition, evolution threshold (Sep 29) · protocol v0.98 · codebook v0 · privacy notice v0.9
- [ ] **Consent pack** sent to all participants, by Oct 5
- [ ] **Pilot** (Mandarin, breadth participant) → protocol v1.0
- [ ] **Supervisor meeting:** ethics note §5, AI-use rule for 3.7, page count, title, Ch3 length, coding rule R1 (questions in `planning/ch1_outline_draft_2026-10-01.md` §4)
- [ ] **Interviews Oct 5–19:** familiarisation memo within 48 hours of each interview
- [ ] **Analysis** ~Nov 7 · **full draft** end of November · **hard deadline** Dec 15

## Working notes

`planning/Pipeline_State.md` is the canonical project state; the Claude project holds mirrors of it and of the handoff. Every orchestration session starts from the newest `planning/session_handoff_*.md`. This repo is the system of record for what the thesis cites and contains.
