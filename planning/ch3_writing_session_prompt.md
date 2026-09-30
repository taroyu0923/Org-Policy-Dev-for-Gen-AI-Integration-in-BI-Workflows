# Chapter 3 Writing Session — brief

**Purpose:** draft Chapter 3 (Method) section by section, following the adopted outline.
**Model:** Opus (thesis prose). **Created:** Oct 1, 2026.
**One or two sections per session.** Order: **3.1 → 3.4 → 3.5 → 3.6 → 3.7 → 3.2**, then **3.3 after the pilot**. `[FILL]` markers are completed after fieldwork (Oct 5–19).

---

## Read first (in this order)

1. `planning/ch3_outline_draft_2026-10-01.md` (**adopted**) — sections, content, sources, word targets
2. `planning/Pipeline_State.md` — current state and settled decisions
3. `literature/notes/M2_braun2021_one_size_fits_all.md` — **the analysis-label decision block** (codebook thematic analysis)
4. The notes for the section being drafted (Cluster M; I1, I2; A12, D1; B9 for 3.1)
5. The design documents the section describes:
   - 3.1 / 3.2: `research-design/sampling_frame.md`, `planning/structure_discussion_log_2026-09-11.md` (RQ v2.1, BI practitioner definition, Shopee threshold)
   - 3.3: `research-design/interview_protocol_v0.98.md`, `wording_card_bilingual.md`, `pilot_debrief.md`
   - 3.4 / 3.5: protocol §9–§10, `analysis/templates/codebook_v0.md`, `analysis/README.md`
   - 3.6: `ethics_determination_note.md`, `privacy_notice.md`, `consent_form.md`, `participant_information_sheet.md`
   - 3.7: `literature/search_log.md`, `planning/query_template_v2.4.md`, `planning/section11_harvest_prompt.md`, `planning/s3_postcheck_2026-09-11.md`, `chapters/ch2/2.6_lens_and_gap.md` ¶2
6. `literature/reference_list.md` + `literature/references.bib` — citable status

## Settled — do not reopen

RQ v2.1; the BI practitioner definition; the Shopee evolution threshold; the Chapter 2 structure; **the analysis label (codebook thematic analysis)**; the 25,000-word budget.

## Hard rules

**Anonymity (information sheet and consent form promise it).**
- **Never name a participant's organisation** — not Shopee, Smartly, Toyota, Delivery Hero, JPMorgan, Twipe, Roku, Amazon or Nordea. Describe cases by sector, approximate size and jurisdiction (e.g. "Depth case A: a regional e-commerce platform, Taiwan, four participants"). Agree the case labels with Albert in the paragraph plan.
- No job title precise enough to identify a person in a small team. Report tiers, not titles, for the depth cases (sampling frame §6).

**Truthfulness about what has happened.**
- Chapter 3 is written in the past tense, but **fieldwork has not happened yet**. Every sentence about a step not yet completed (pilot, interviews, transcription, coding, re-coding, supervisor check, member checking) ends with a marker `[PENDING: <what to confirm>]`. Every number not yet known is `[FILL: …]`. Never state as done what has not been done.
- Describe **what was actually done**, not generic procedure (Braun & Clarke 2021, Table 1 Item 11).

**Analysis label.** Use "codebook thematic analysis" throughout. Never call it reflexive TA. Never say themes "emerged". The a priori structural / procedural / relational spine is a **starting frame, not the themes**. Re-coding after an interval and the supervisor's sample review are **consistency checks, not reliability measures**. No inter-rater reliability.

**Sources.**
- Cite only ✅ entries in `reference_list.md`; preprints supplementary only.
- **Flanagan:** only as "Flanagan (1954, as cited in Gremler, 2004)" — `[@gremler2004cit]` in the brackets; Flanagan is **not** in the bib as citable and not in the reference list.
- **Yin:** not cited. The design typology (single/multiple, holistic/embedded) is cited to **Baxter & Jack (2008)** as *their account of* Yin's typology.
- M10 renders as **Corbin Dwyer & Buckle (2009)**.
- I7 (Xie) and I10 (Vu): no page numbers until the published PDFs are in hand.
- Every direct quote checked against the PDF page. I-cluster notes are NotebookLM-compiled and not content-checked — treat their quotes as leads only.
- No new sources without a logged search and Albert's approval.

**No interview content, ever** (privacy notice §7). If Albert pastes any, stop and remind him.

**AI-use disclosure (3.7).** State what AI tools did in the literature process (NotebookLM as reading aid; Claude for planning, drafting support and verification; every quote and page checked against PDFs) and that no AI touched interview content. **Do not invent Aalto's rules** — insert `[CHECK: Aalto / programme guidance on AI use in theses]` for Albert to confirm.

**Style.** Academic register, UK spelling, first person allowed sparingly for researcher decisions ("I piloted…" or "the researcher piloted…" — ask Albert which, once, and keep it consistent). Claim first; no throat-clearing; vary paragraph length; at most two em dashes per page; avoid delve, crucial, pivotal, landscape, "it is important to note". Citations in pandoc form; narrative form `@key [p. N]` when the author is named in the sentence.

## Procedure per section

1. **Paragraph plan first:** paragraph → what it states → design document it describes → sources (bib keys + pages) → `[PENDING]`/`[FILL]` items → words. **Send it to Albert and wait for approval.**
2. **Draft** to the target ±10%: 3.1 = 400 · 3.2 = 500 · 3.3 = 650 · 3.4 = 650 · 3.5 = 400 · 3.6 = 300 · 3.7 = 250 (total 3,150).
3. **Self-check and report:** word count; every `[@key]` exists and is ✅; quotes checked with pages; a list of all `[PENDING]` and `[FILL]` markers; an anonymity check (no organisation names, no identifying titles); style pass.
4. **Write** to `chapters/ch3/3.N_<slug>.md`; create/update `chapters/ch3/README.md` (status table, word counts, open markers, dependencies). In 3.7, note that it resolves 2.6's `Section [3.X]`; update `chapters/ch2/README.md` dependency line to point to 3.7.
5. Append decisions made while drafting to `planning/session_handoff_2026-09-29.md`. Do not edit the adopted outline without approval.

## Delivery

Write into the repo via the file-commit tools (the Cowork shell cannot mount the folders); finish by re-listing `chapters/ch3/`. Do not commit or push.

---

## Copy-paste prompt for the new session

```
Read planning/ch3_writing_session_prompt.md in my repo first, then the files it lists under
"Read first", in that order.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). The Cowork shell cannot mount my folders -- use the
file listing/staging/commit tools. Do not commit or push; I push myself.

Task this session: draft Section [3.1 / 3.4 / 3.5 / 3.6 / 3.7 / 3.2] of Chapter 3, following the
adopted outline planning/ch3_outline_draft_2026-10-01.md.

Do not reopen RQ v2.1, the BI practitioner definition, the Shopee threshold, the analysis label
(codebook thematic analysis) or the word budget.

STEP 1: send me the paragraph plan (paragraph -> what it states -> design document -> bib keys +
pages -> PENDING/FILL items -> words) and WAIT for my approval before drafting. Propose the
anonymised case labels in the plan.

Never name a participant's organisation or give an identifying job title. Fieldwork has not
happened yet: write in the past tense, but mark every not-yet-completed step [PENDING: ...] and
every unknown number [FILL: ...]. Never state as done what has not been done.

Call the analysis codebook thematic analysis; never reflexive TA; never "themes emerged"; the
a priori spine is a starting frame; re-coding and the supervisor check are consistency checks,
not reliability. Cite Flanagan only as "Flanagan (1954, as cited in Gremler, 2004)"; do not cite
Yin -- use Baxter & Jack (2008) for the design typology. Cite only verified sources; check every
quote against the PDF page. No interview content.

When the draft is done: word count, citation check against references.bib, quotes checked with
pages, the list of PENDING/FILL markers, and an anonymity check. Write the section to
chapters/ch3/3.N_<slug>.md, create/update chapters/ch3/README.md, and re-list chapters/ch3/.
```
