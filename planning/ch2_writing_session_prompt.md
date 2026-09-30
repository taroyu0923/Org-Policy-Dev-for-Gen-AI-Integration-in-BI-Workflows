# Chapter 2 Writing Session — brief

**Purpose:** draft Chapter 2 (literature review) section by section, following the adopted loop structure.
**Model:** Opus (thesis prose — per `planning/Thesis_Agent_Team_Workflow_Plan.md`). **Created:** Sep 29, 2026.
**One section per session** is the default. Order: **2.1 → 2.6 → 2.5 → (after the Shopee interviews) 2.2 → 2.3 → 2.4.**

---

## Read first (in this order)

1. `planning/session_handoff_2026-09-29.md` — state of the project
2. `planning/ch2_outline_draft_2026-09-29.md` (v2, **adopted**) — sections, claims, sources, word targets
3. `planning/ch2_claims_map_2026-09-29.md` — claims K1–K11, P1–P3, the loop, B9 positioning, Presc./Obs. tags
4. `literature/reference_list.md` + `literature/references.bib` — citable status of every source
5. The notes in `literature/notes/` for the section being drafted (the outline lists them)
6. `planning/s3_postcheck_2026-09-11.md` §3 — the PDF-verified reading of D7 Rakova

## Settled — do not reopen

RQ v2.1; the "BI practitioners" definition; the Shopee threshold; the loop structure of Chapter 2; BI-work context sits in Chapter 1, not here.

## Source rules (hard)

- **Cite only entries marked ✅ in `reference_list.md`.** ❓ TODO-VERIFY and ⛔ EXCLUDED entries are uncitable. If a needed source is not ✅, stop and tell Albert.
- **A9 Papagiannidis 2023 and C10 Asatiani 2020:** their §11 "substantive" verdicts are not PDF-verified. Do not rely on them until checked against the PDF (in `D:\Master\Thesis\Thesis Content\Group A` / `Group C`).
- **D7 Rakova 2021:** the note's §7, §9 and §11 contain content not in the paper. Use only `s3_postcheck_2026-09-11.md` §3 or the PDF itself.
- **B9 Silic 2025:** 8 executive interviews (not 10 — the abstract is inconsistent); the §11 verdict is pending Albert. Say "eight".
- **Every direct quotation** is checked against the PDF page before it goes into the draft. A note's quote is a lead, not verification. If it cannot be found, paraphrase with the section reference or drop it.
- **No new sources** without a logged search in `literature/search_log.md` and Albert's approval.
- Citation syntax: pandoc `[@key, p. N]`, keys exactly as in `references.bib`.

## Argument rules

- **Synthesise by claim, not by paper.** Each paragraph opens with a claim about the literature, then the sources; never "Author X (year) found… Author Y (year) found…" in sequence.
- **Keep the Presc./Obs. distinction visible.** Say when the literature *asserts or prescribes* something and when it *observed* it in fieldwork. This distinction carries the gap argument.
- **Headings are questions the literature answers or fails to answer.** The loop orders the chapter; it is not presented as a finding.
- **No interview data, and no hypotheses stated as findings.** P2 (bypass as continued habit), "rulings not the document" and the loop's fork are *raised as open questions* in 2.3–2.5, never asserted. Albert's expectations are hypotheses.
- **Positioning sentences** follow the claims map: carrier vs recipient (D7, D4); survey vs incident-traced, executive vs practitioner account (B9); BI never the unit of analysis.
- **No interview content ever enters this session** (privacy notice §7). If Albert pastes any, stop and remind him.

## Style

Academic register, UK spelling, first person sparingly ("this study"). Claim first; no throat-clearing openers ("In this section…"). Vary paragraph length. At most two em dashes per page. Avoid: delve, crucial, pivotal, landscape, tapestry, "it is important to note", "plays a vital role". Define a term once, then use it consistently (BI practitioners, working rule, ruling, intermediary).

## Procedure per section

1. **Paragraph plan first.** For the section being drafted, produce a table: paragraph → claim → sources (bib keys + pages) → Presc./Obs. → words. **Send it to Albert and wait for approval.**
2. **Draft** to the word target ±10% (outline v2): 2.1 = 1,100 · 2.2 = 1,100 · 2.3 = 1,100 · 2.4 = 1,000 · 2.5 = 1,250 · 2.6 = 700 (revised Sep 30: chapter total 6,250 of a 25,000-word thesis).
3. **Self-check and report:**
   - word count;
   - every `[@key]` exists in `references.bib` and is ✅;
   - every quote PDF-checked (list page and PDF file);
   - any claim you could not support — listed, not smoothed over;
   - writing-quality pass against the style list above.
4. **Write** to `chapters/ch2/2.N_<slug>.md` in the repo (e.g. `chapters/ch2/2.1_how_rules_arrive.md`). Update `chapters/ch2/README.md` with section status and word counts.
5. **Log** decisions made while drafting in `planning/session_handoff_2026-09-29.md` (append) — do not edit the adopted outline without Albert's approval.

## Delivery

- Outputs go **into the repo** at exact paths via the file-commit tools; the Cowork shell cannot mount the folders. Finish by re-listing `chapters/ch2/` as evidence. No zips or downloads.
- Do not commit or push — Albert does.

---

## Copy-paste prompt for the new session

```
Read planning/ch2_writing_session_prompt.md in my repo first, then the files it lists under
"Read first", in that order.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). The Cowork shell cannot mount my folders -- use the
file listing/staging/commit tools. Do not commit or push; I push myself.

Task this session: draft Section [2.1 / 2.6 / 2.5 / ...] of Chapter 2, following the adopted
outline v2 (planning/ch2_outline_draft_2026-09-29.md) and the claims map.

Do not reopen RQ v2.1, the BI practitioner definition, the Shopee threshold or the Chapter 2
structure.

STEP 1: send me the paragraph plan (paragraph -> claim -> bib keys + pages -> prescribed or
observed -> words) and WAIT for my approval before drafting.

Cite only sources marked verified in literature/reference_list.md. Check every direct quote
against the PDF page before using it. Do not rely on A9 or C10 until they are PDF-verified, and
for D7 Rakova use only the PDF or planning/s3_postcheck_2026-09-11.md section 3 -- not the
note's sections 7, 9 or 11.

Synthesise by claim, not paper by paper. Keep visible what the literature prescribes versus what
it observed. Raise my hypotheses (bypass as continued habit, rulings not the document, the
ask/act-now fork) only as open questions -- never as findings. No interview data in this chapter.

When the draft is done: report word count, a citation check against references.bib, the quotes
you checked with their pages, and any claim you could not support. Write the section to
chapters/ch2/2.N_<slug>.md, update chapters/ch2/README.md, and finish by re-listing chapters/ch2/.
```
