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
                     claims map, writing briefs, review logs, PDF-check logs,
                     writing_style_albert.md (voice rules for all chapter prose)
literature/
  notes/             One Markdown note per source, cluster-numbered ID:
                     <ID>_<author><year>_<slug>.md  (e.g. A1_batool2024_...)
                     Governance A–E: v2.4, §1–§11 (§11 = working-tier reception)
                     Theory anchors G1–G10 (G4–G10: sensemaking) · Methods M1–M12 ·
                     Interview design I1–I14
  _raw/              Verbatim NotebookLM outputs + PDF verification logs
  cluster-memos/     Synthesis memos (empty)
  references.bib     BibTeX — single source of truth for per-reference status
  reference_list.md  Generated audit view of references.bib
  search_log.md      Search passes S1–S7: queries, dates, hits, kept/rejected
research-design/     Protocol v1.0, wording card, consent form (supervisor template) and consent email,
                     participant preparation note, sampling frame, ethics note, pilot runbook and
                     debrief; superseded protocol v0.98 and consent pack kept for the record
chapters/            Thesis chapters in Markdown (pandoc [@key]); LaTeX in November
  ch1/               Introduction — README tracks status, word counts, sources, dependencies
  ch2/               Literature review — README tracks status, word counts, sources
  ch3/               Method — README tracks status and open [FILL]/[PENDING] markers
  figures/           Figure 2.1 (path a rule is assumed to take, two lenses), Figure 2.2 (§11 screening)
analysis/            Codebook v0, memo templates and AI use log template only; filled copies live on Aalto OneDrive
interviews/          Fieldwork outputs (gitignored)
latex/               Aalto template + converted output
Claude outputs/      PR descriptions and session outputs
```

### `research-design/`

| File | Purpose |
|---|---|
| `interview_protocol_v1.0.md` | **The interview guide in use (Oct 14, after the pilot).** 45–60 min; critical-incident anchor, three phases, C1a / D2a / E3a probes; A4, C3, D1, D4, E4, E5 cut; documents in an optional separate call |
| `interview_protocol_v0.98.md` | **Superseded Oct 14**; the version used in the pilot |
| `wording_card_bilingual.md` | Fixed EN / 繁中 wording for the core items (v1.3 adds E3a) |
| `consent_email_v1.1.md` | EN / 繁中 email sent with the consent form; consent by reply with the six Yes/No answers |
| `participant_preparation_note.md` | EN / 繁中 note sent before the interview: one concrete situation to have in mind; the optional document call |
| `pilot_runbook.md`, `pilot_debrief.md` | Pilot procedure and debrief template (pilot done; used to test the instrument only, not as data) |
| `sampling_frame.md` | Cases, tiers, inclusion criterion, sequencing, confidentiality rules |
| `Consent_form_interview_v1.1.docx` | **The consent document (Oct 6).** Supervisor's template adapted as one merged form: study information, AI use on de-identified transcripts only, retention, six optional Yes/No permissions; consent by signature or email reply |
| `participant_information_sheet.md`, `consent_form.md`, `privacy_notice.md` | **Superseded Oct 6** by the form above; kept for the record only |
| `recruitment_email.md` | Contact and scheduling templates (banner: attachment lines out of date; use `consent_email_v1.1.md`) |
| `ethics_determination_note.md` | Aalto ethical-review criteria; §5 records the Oct 6 decision: no review or prior approval required, consent on the supervisor's template, AI on de-identified data only |

## Design at a glance

- **Embedded multiple-case design**, up to 14 participants in 9 organisations across 5 countries, recruited from the researcher's professional network. Fewer is acceptable for a master's thesis (supervisor, Oct 6); adequacy is judged by information power.
  - **Depth stratum:** two organisations, 7 participants across tiers.
  - **Breadth stratum:** 7 single-informant cases.
  - The two strata are analysed separately and never pooled.
- **Reporting:** cases are reported only by case label (sector and country), never by organisation name. See `chapters/ch3/README.md`.
- **Critical-incident anchor:** a bounded three-type menu, each incident process-traced with the same four questions. Interviews last 45–60 minutes (protocol v1.0); documents are shown only in an optional separate call.
- **Analysis:** codebook thematic analysis.
  - A priori spine: the structural / procedural / relational practice typology (Papagiannidis et al., 2025; after Tallon et al., 2013).
  - Second lens (Oct 2, supervisor's suggestion): **sensemaking**, a sensitising concept that guides the memos (cue, plausible reading, who the rule was talked over with, sensegiving) and adds no codes (Weick et al., 2005; Maitlis & Christianson, 2014; Gioia & Chittipeddi, 1991).
  - Inductive codes for everything BI-specific.
  - The ask / act-now loop is a sensitising lens, not a set of codes.
  - Re-coding and supervisor review are consistency checks, not reliability measures.
- **Languages:** English and Taiwanese Mandarin; core items are fixed in both.

## Conventions

- **Citations:** pandoc `[@key, p. N]`; narrative `@key [p. N]` when the author is named. `references.bib` is the only place per-reference status is recorded. Cite ✅ entries only; preprints are supplementary.
- **Verification:** NotebookLM answers are leads, not evidence. Every quote and page is checked against the PDF before it enters a chapter. Two notes (D7, D6) were found to contain NotebookLM content that is not in the paper, so the §11 verdicts of the S3 notes are being re-checked against the PDFs.
- **Research ethics and integrity:** follows Aalto's guidance and TENK's 2023 code of conduct (`tenk2023ri`); no ethical review required (supervisor, Oct 6). Chapter 3.6 is the thesis's ethics and integrity section.
- **Truthfulness markers:** `[PENDING: …]` for steps not yet done, `[FILL: …]` for unknown numbers, `[CHECK: …]` for open rules.
- **Literature queries:** template v2.4 (`planning/query_template_v2.4.md`).

## Privacy and anonymity

- No participant data enters this repository. **Changed Oct 6, 2026:** **de-identified** transcripts may be processed with third-party AI tools (transcription check, Mandarin→English draft translation, analysis support); recordings stay in Teams on the Aalto account. Approved by the supervisor (de-identified data only) and disclosed in the consent form (`research-design/Consent_form_interview_v1.1.docx`); every AI output is checked by the researcher and logged (`analysis/templates/ai_use_log_template.md`).
- Consent forms, recordings, transcripts and filled analysis templates live on Aalto storage only.
- Organisations are never named in chapters.
- `.gitignore` covers `interviews/transcripts/` and the participant-data paths; source PDFs are not redistributed.

## Status

*Updated Oct 14, 2026. Detail: `planning/Pipeline_State.md` and `planning/session_handoff_2026-10-14.md`.*

**Word budget:** 25,000 words. Intro 2,000 · literature review 6,250 · method 3,000 · findings 8,000 · discussion 4,250 · conclusion 1,500. **Decision (Oct 2):** Chapters 2 and 3 may run over without trimming; the total is rebalanced when Chapters 4–6 are planned.

**Chapters**
- [x] **Ch1 drafted and reviewed:** 1.1–1.6, ≈2,100 words (Oct 2, after the style pass and the sensemaking touch in 1.5/1.6); quotes PDF-checked. Supervisor sheet: `planning/ch1_outline_draft_2026-10-01.md`
- [x] **Style pass (Oct 1):** all drafted sections rewritten in Albert's voice (`planning/writing_style_albert.md`); quotes, pages, keys and markers checked identical
- [x] **Ch2:** outline v2 adopted (a loop structure following how a rule is expected to travel). Claims map K1–K11.
- [x] **Ch2 drafted:** 2.1 v1.3 (1,176 words) · 2.5 v1.3 (1,430) · 2.6 v1.5 (1,005) — ≈3,610 of 6,250. Sensemaking added as the second lens (Oct 2; all new quotes PDF-checked)
- [x] **Figures:** 2.1 (rule path, two lenses) and 2.2 (screening) in `chapters/figures/`
- [ ] **Ch2 remaining:** 2.2–2.4, after the depth-case interviews
- [x] **Ch3:** 3.1, 3.2, 3.4–3.7 drafted and reviewed (3.4 v1.2 names sensemaking as a sensitising lens)
- [x] **Ch3 after the supervisor meeting (Oct 6):** 3.6 v1.3 retitled *Research ethics and research integrity* (supervisor's requirement; TENK cited) · 3.2 v1.2 smaller sample acceptable · 3.4 v1.3 Depth A threshold for three or fewer participants · 3.5 AI draft translation sentence · 3.7 AI sentence points to 3.6
- [x] **3.6 TENK check (Oct 9):** `[CHECK: tenk2023ri p. 9]` resolved against the PDF; marker removed, prose unchanged
- [ ] **Ch3 remaining:** 3.3, planned from protocol v1.0 (it must say the pilot used v0.98 and was not kept as data). `[FILL]` / `[PENDING]` markers to be completed after fieldwork.
- [ ] Ch4–Ch6 after analysis · title revision (supervisor)

**Literature**
- [x] **Corpus:** 36 governance notes (Clusters A–E plus B9) · theory anchors G1–G10 · methods M1–M11 (PDF-checked) · interview design I1–I14 (verified)
- [x] **S7 (Oct 6):** M12 `tenk2023ri` (TENK 2023 research integrity code) for 3.6. Local PDF saved to Group M; p. 9 checked Oct 9
- [x] **S6 sensemaking sources (Oct 2):** G4–G10 PDF-verified (G7 by OCR), outside the §11 denominator; Cluster G 3 → 10; `planning/s6_addref_prompt.md`
- [x] **Working-tier screening (§11):** **28–29 of 36 governance sources (78–81%)** contain no account of how staff below the rule-setting level receive AI governance.
  - Updated Oct 1: every verdict PDF-checked under coding rule R1 (data on staff reception of AI governance only); `planning/s3_section11_spotcheck_2026-10-01.md`.
- [x] **§11 verdicts PDF-checked (S3 + phase 2), rule R1** — Oct 1
- [x] **Note fixes (Oct 1):** PDF page-check blocks in 14 notes; 8 bib-key headers corrected; C7 publisher PDF in place
- [x] **S1 search** partly reconstructed from the Research Plan §2.4 (planned sources; to confirm)
- [ ] §12 protocol-craft pass on I1–I14 (after the pilot) · cluster memos

**Design and fieldwork**
- [x] RQ v2.1, BI practitioner definition, evolution threshold (Sep 29) · protocol v0.98 · codebook v0
- [x] **Templates for the pilot (Oct 2):** familiarisation memo §3a (sensemaking prompts), codebook §E, contact summary, pilot-debrief check. Protocol, wording card and consent pack unchanged until v1.0
- [x] **Supervisor contact resumed (Oct 2):** overview, thesis draft and interview materials shared as Google Docs
- [x] **Consent form v1.1 (Oct 6)** on the supervisor's template; replaces the information sheet, consent form and privacy notice
- [x] **Fieldwork kit (Oct 9):** consent email (EN / 繁中), participant preparation note, pilot runbook, AI use log template; bilingual interview script and recording sheet as a Google Doc (blank template; filled copies on OneDrive)
- [x] **Pilot done** (Mandarin, breadth participant): questions clear, over 60 minutes; **pilot only, not data**
- [x] **Supervisor feedback on the interview design (Oct 12):** design fine; many questions, likely overtime; announce the document option in advance; threshold explained
- [x] **Protocol v1.0 (Oct 14):** 45–60 min, six questions cut, documents in an optional separate call; wording card v1.3 (E3a)
- [ ] **Consent form** sent to each participant before their interview
- [x] **Supervisor meeting, Oct 6:** no ethical review or approval needed, interviews may start once consent is given · consent on his template · AI tools on de-identified data only · fewer than 14 participants acceptable, Depth A may be partial · reference structure sufficient for a master's thesis (strengthening optional, weighed against time) · thesis must include an ethics and integrity section
- [ ] **Master's thesis seminar:** present the research plan (supervisor approved booking, Oct 12; slot to book)
- [ ] **Interviews with protocol v1.0:** contact summary within 24 hours and familiarisation memo within 48 hours of each interview; AI use log kept
- [ ] **Analysis** ~Nov 7 · **full draft** end of November · **hard deadline** Dec 15

## Working notes

`planning/Pipeline_State.md` is the canonical project state; the Claude project holds mirrors of it and of the handoff. Every orchestration session starts from the newest `planning/session_handoff_*.md`. This repo is the system of record for what the thesis cites and contains.
