# Organizational Policy Development for Generative AI Integration in BI Workflows
**A Qualitative Analysis of Governance Framework Evolution**

MSc Business Analytics thesis — Liu Yu-Shu (Albert), Aalto University.

Organizations adopting generative AI in business intelligence (BI) workflows face a governance gap: existing research covers AI implementation effectiveness and published governance frameworks, but not how organizations actually develop and evolve internal policy to manage GenAI in analytical work. This thesis investigates that gap qualitatively, through interviews with practitioners who produce and maintain analytical outputs.

**Framing (rev. Sep 2, 2026).** The confirmed sample contains no policy author, so the study is positioned as an account of how GenAI policy is **encountered, interpreted and adapted at the analytical working tier** — and whether that adaptation feeds back upward. The literature theorises the tier hierarchy from the top down out of published documents and never observes its bottom empirically; this study supplies that half. See `research-design/sampling_frame.md` §3.

## Repo layout

```
planning/            Research plan, agent team & workflow plan (synced from the Claude project)
literature/
  notes/             One Markdown note per source; cluster-prefixed (A_..., B_..., ...)
                     v2 format: 10 sections, every point tagged section + page
  cluster-memos/     Synthesis memos per cluster (A–F)
  references.bib     BibTeX — single source of truth for per-reference status
                     (verification result, note version, read-mark, quality tier)
  search_log.md      PRISMA-lite search protocol — every query, date, hits, kept/rejected
research-design/     Empirical-stage instruments and governance documents (see below)
chapters/            Thesis chapters in Markdown; converted to LaTeX in November
interviews/          Fieldwork outputs only — transcripts and logs (gitignored)
analysis/            Thematic coding artifacts (rolling coding from Sep 22)
latex/               Aalto template + converted output
```

### `research-design/` — the empirical stage

| File | Purpose |
|---|---|
| `README.md` | Stage overview, design summary, open items |
| `sampling_frame.md` | Cases, tier assignments, inclusion criterion, sequencing, confidentiality and employer-permission rules |
| `interview_protocol_v0.95.md` | Semi-structured guide: three phases with tier branches, critical-incident anchor; every question source-tagged to `literature/notes/` |
| `wording_card_bilingual.md` | Fixed EN / 繁中 wording for the core items — read as written, not improvised |
| `participant_information_sheet.md` | Given to participants before consent |
| `consent_form.md` | Signed consent; document *access* and *quotation* permissions are separate items |
| `recruitment_email.md` | First contact, gatekeeper, referral and scheduling templates |
| `ethics_determination_note.md` | Assessment against Aalto's ethical-review criteria + supervisor request |

> `research-design/` supersedes the earlier `interviews/protocol/` placeholder. Instruments and governance documents live here; `interviews/` now holds fieldwork outputs only.

## Design at a glance

**Embedded multiple-case**, n = 14 across 9 organizations and 6 jurisdictions.

- **Depth stratum** — Shopee TW (n=4, operational → senior tactical) and Smartly FI (n=3). Within-case triangulation across tiers.
- **Breadth stratum** — 7 single informants (Toyota, Delivery Hero, JPMorgan Chase, Twipe, Roku, Amazon, Nordea). Cross-case variation.
- **Evidence tiers** — 1–2 document-anchored cases whose chronology is process-traced, used to assess recall quality in the interview-only cases.
- **BI-forcing** — critical-incident anchor with a bounded three-type menu, each process-traced with the same four questions.
- **Coding** — hybrid: a priori frame (three phases; tier as case attribute; Luna's four constituents as seed codes), inductive for everything BI-workflow-specific.
- **Languages** — English and Taiwanese Mandarin; core items fixed in both, remaining probes rendered live.

## Conventions

- **Citations:** pandoc `[@key]` syntax throughout; `references.bib` is the only place per-reference status is recorded.
- **Provenance:** every point in a literature note carries its location in the original (section + page). Unlocatable points are marked `(location unverified)` or `⚠ UNRESOLVED`, and excluded from memos and drafts.
- **Quality tiers:** peer-reviewed journal > peer-reviewed conference > preprint > grey. Preprints and grey literature are supplementary only; chapters lean on peer-reviewed anchors.
- **Excluded sources** stay in `references.bib` marked `EXCLUDED` for the record, and are never cited.

## Privacy

Participant data never enters this repository. Signed consent forms, recordings and identifiable transcripts live on Aalto encrypted storage only. `.gitignore` covers `interviews/transcripts/` and the participant-data paths under `research-design/`; source PDFs are not redistributed.

## Status

- [x] Repo scaffold + `references.bib` (43 sources, cluster-tagged)
- [x] Clusters A+B compiled under Lit Review Process v2 — 12 notes, 10-section format (Sep 2)
- [x] Research-design stage: protocol v0.95, sampling frame, ethics and consent pack (Sep 2)
- [ ] `literature/search_log.md` reconstructed (PRISMA-lite; required before further sources are added)
- [ ] Cluster memos A+B → lit review sections 1–2 drafted (target Sep 8)
- [ ] Ethical-review determination obtained in writing — **blocks recruitment**
- [ ] Clusters C–F + gap-fill (target Sep 15); method sources still absent
- [ ] Protocol piloted in Mandarin → v1.0
- [ ] Interviews (Sep 15 – Oct 15) — depth cases first
- [ ] Thematic analysis complete (Oct 31)
- [ ] Full draft (end Nov) — hard deadline mid-Dec

## Working notes

Session state, decisions and handoff context live in the Claude project (`claude/Pipeline_State.md`, `claude/LitReview_Process_v2.md`, `claude/research-design/`), not in this repo. This repo is the system of record for what the thesis actually cites and contains.
