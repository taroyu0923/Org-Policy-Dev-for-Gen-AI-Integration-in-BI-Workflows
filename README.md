# Organizational Policy Development for Generative AI Integration in BI Workflows
**A Qualitative Analysis of Governance Framework Evolution**

MSc Business Analytics thesis — Liu Yu-Shu (Albert), Aalto University.

Organizations adopting generative AI in business intelligence (BI) workflows face a governance gap: existing research covers AI implementation effectiveness and published governance frameworks, but not how organizations actually develop and evolve internal policy to manage GenAI in analytical work. This thesis investigates that gap qualitatively, through interviews with practitioners who produce and maintain analytical outputs.

**Framing (rev. Sep 2, 2026).** The confirmed sample contains no policy author, so the study is positioned as an account of how GenAI policy is **encountered, interpreted and adapted at the analytical working tier** — and whether that adaptation feeds back upward. The literature theorises the tier hierarchy from the top down out of published documents and never observes its bottom empirically; this study supplies that half. See `research-design/sampling_frame.md` §3.

## Repo layout

```
planning/            Pipeline state (canonical), query template v2.4, agent task
                     prompts (§11, §12), session post-checks and decision logs
literature/
  notes/             One Markdown note per source, cluster-numbered ID:
                     <ID>_<author><year>_<slug>.md  (e.g. A1_batool2024_...)
                     Governance notes A–E: v2.4, §1–§10 + §11 working-tier reception
                     Methodology notes I1–I14: v2.4-M, §1–§10 (+ §12 protocol craft, pending)
  _raw/              Verbatim NotebookLM query outputs (S3 sources onward)
  cluster-memos/     Synthesis memos (empty — structure being settled)
  references.bib     BibTeX — single source of truth for per-reference status
                     (verification result, note version, read-mark, quality tier)
  reference_list.md  Generated audit view of references.bib
  search_log.md      PRISMA-lite search protocol — every query, date, hits, kept/rejected
research-design/     Empirical-stage instruments and governance documents (see below)
chapters/            Thesis chapters in Markdown; converted to LaTeX in November
interviews/          Fieldwork outputs only — transcripts and logs (gitignored)
analysis/            Thematic coding artifacts (rolling coding: memo within 48h per interview)
latex/               Aalto template + converted output
```

### `research-design/` — the empirical stage

| File | Purpose |
|---|---|
| `README.md` | Stage overview, design summary, open items |
| `sampling_frame.md` | Cases, tier assignments, inclusion criterion, sequencing, confidentiality and employer-permission rules |
| `interview_protocol_v0.98.md` | Semi-structured guide (aligned to RQ v2.1; v0.97 kept for history): three phases with tier branches, critical-incident anchor; every question source-tagged to `literature/notes/` |
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
- **Coding** — hybrid: a priori spine is Papagiannidis's structural/procedural/relational typology (JSIS 2025, after Tallon et al. 2013); three phases and Luna's constituents secondary; inductive for everything BI-workflow-specific.
- **Interview phases** — Policy Encounter & Interpretation / Implementation & Change Management / Organizational Adaptation Dynamics.
- **Languages** — English and Taiwanese Mandarin; core items fixed in both, remaining probes rendered live.

## Conventions

- **Literature queries:** template **v2.4** (`planning/query_template_v2.4.md`) — 11 sections. Supersedes the v2.2 template. Any new reference, snowball pull or cluster extension uses v2.4.
- **Citations:** pandoc `[@key]` syntax throughout; `references.bib` is the only place per-reference status is recorded.
- **Provenance:** every point in a literature note carries its location in the original (section + page). Unlocatable points are marked `(location unverified)` or `⚠ UNRESOLVED`, and excluded from memos and drafts.
- **Quality tiers:** peer-reviewed journal > peer-reviewed conference > preprint > grey. Preprints and grey literature are supplementary only; chapters lean on peer-reviewed anchors.
- **Excluded sources** stay in `references.bib` marked `EXCLUDED` for the record, and are never cited.

## Privacy

Participant data never enters this repository. Signed consent forms, recordings and identifiable transcripts live on Aalto encrypted storage only. `.gitignore` covers `interviews/transcripts/` and the participant-data paths under `research-design/`; source PDFs are not redistributed.

## Status

*Updated Sep 28, 2026.*

**Literature**
- [x] Repo scaffold + `references.bib` — 58 entries; 18 still carry a `TODO-verify` note (formally uncitable)
- [x] Clusters A–E compiled — **35 usable governance notes** (A11, B7, C7, D7, E4; D3 Mitchell excluded)
- [x] Interview-methodology cluster compiled — 14 notes (I1–I14)
- [x] Verification pass: Mitchell excluded; JISEM and INJOSS papers grey-tagged (Sep 2)
- [x] `literature/search_log.md` — S1–S3 recorded, S4 planned
- [x] §11 working-tier reception harvest — original 20 (Sep 4) + 15 S3 notes (Sep 11). Tally: **14/20 → 22–24/35** documented absence (`planning/s3_postcheck_2026-09-11.md`)
- [x] S3 frequency-ranked snowball gap-fill — 15 sources added (Sep 11)
- [ ] S3 note fixes — D7 Rakova §7/§9/§11 contain content not in the paper; PDF-verify A9 and C10 §11; normalise §11 verdict openers
- [ ] §12 protocol-craft pass on I1–I14 + bib backfill (`planning/section12_protocol_craft_prompt.md`)
- [ ] Naming retrofit for interview notes (slugs/years missing on 14 files); `git rm` `literature/notes/_to_delete/`
- [ ] S1 search reconstruction — databases and query strings from Research Plan §2.4
- [ ] S4 methods literature (reflexive TA, critical incident technique, embedded case design)
- [ ] Screen three post-corpus novelty candidates for the RQ (`planning/structure_discussion_log_2026-09-11.md`)
- [ ] Cluster F when PDFs arrive

**Design & structure**
- [x] Research-design stage: sampling frame, ethics and consent pack (Sep 2); protocol **v0.98** + wording card v1.1 (Sep 29)
- [x] Ethical-review determination — supervisor confirmed **no review required** (record in `ethics_determination_note.md` §5)
- [ ] **Privacy notice** (Aalto template) + ethics note §5 — by Oct 1, required before first interview
- [x] Research question v2 adopted Sep 20 (`planning/structure_discussion_log_2026-09-11.md`)
- [ ] Title revision to match RQ v2
- [x] "BI practitioners" defined; Shopee evolution threshold (Q3) set — Sep 29
- [ ] Chapter 2 structure (Plan 1 argument funnel vs Plan 3 cluster-mirroring)
- [x] Protocol changes from Sep 11 log (B3a ruling→rule probe, escalation probe, #13 tenure floor) + align to RQ v2.1 — v0.98 (Sep 29)
- [ ] Pilot in Mandarin (#5 or #6) → protocol v1.0 — by Oct 3
- [ ] Cluster memos → lit review drafted (original target Sep 8 — missed)

**Fieldwork & writing**
- [ ] Recruitment — started Sep 11
- [ ] Interviews — **rescheduled Oct 5 – Oct 19**; Shopee first, then Smartly, breadth as capacity allows
- [ ] Rolling coding discipline in `analysis/` — not yet implemented
- [ ] Thematic analysis complete (target ~Nov 7, was Oct 31)
- [ ] Full draft (end Nov) — hard deadline Dec 15

## Working notes

Session state, decisions and handoff context live in the Claude project (`claude/Pipeline_State.md`, `claude/LitReview_Process_v2.md`, `claude/research-design/`), not in this repo. This repo is the system of record for what the thesis actually cites and contains.
