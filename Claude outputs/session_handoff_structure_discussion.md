# Session Handoff — literature structure & interview framework

**Written:** Sep 11, 2026, at the end of a long session. **For:** a fresh Opus session.
**Purpose:** the literature-gathering phase is complete. The next conversation is the design discussion that has been deferred behind it for two weeks.

---

## Copy-paste opening prompt

```
Read planning/Pipeline_State.md, planning/naming_convention.md, planning/query_template_v2.4.md
and research-design/ in my repo before we start.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). Note: the Cowork shell currently cannot mount my
folders (Windows update, Sep 8) -- use the file listing/staging/commit tools instead of bash.

The S3 gap-fill is finished: 50 compiled notes now exist (35 governance + 14 interview-methodology,
with D3 Mitchell excluded). Before we discuss anything, do these three checks and report:

1. Tally section 11 across the governance corpus. Read each note's section 11 verdict line only
   (substantive / partial / documented absence). Report TWO figures, not one: the original
   20-source corpus, and the full 35-source corpus -- and say which way the absence rate moved.
   The earlier headline was "14 of 20 sources contain no account of how anyone below management
   experiences governance". The 15 new sources were snowballed FROM that corpus, so they are not
   an independent sample -- if the rate holds anyway that is a stronger result, if it collapses
   the original figure was an artefact of my first search. Say which.
2. Confirm section 11 was actually run on all 15 new notes. If any is missing, list them.
3. Read D7 (Rakova 2021) in full and tell me whether it scoops or positions my thesis. It is the
   closest published study to my reframed working-tier design and I have never had a straight
   answer on it.

Then: lit-review mode + socratic mode. I want to settle the literature review structure and the
interview framework. Ask me questions; don't just produce a plan.
```

---

## State as of this handoff

| Stream | State |
|---|---|
| Governance corpus | **35 notes** (A×11, B×7, C×7, D×7, E×4), D3 Mitchell excluded → 34 usable |
| Methodology corpus | **14 notes** (I1–I14), §12 protocol-craft pass **not yet run** |
| `_raw/` | 15 files for the S3 sources; earlier notes have no raw trail |
| `references.bib` | Updated by the S3 session — **verify the 19 previously-uncitable entries were backfilled** |
| §11 harvest | Run on the original 20. **Status on the new 15 unconfirmed** |
| §12 harvest | Specified (`planning/section12_protocol_craft_prompt.md`), not run |
| Interview design | Protocol **v0.97**, sample confirmed at 14 participants / 9 orgs / 6 jurisdictions |
| Ethics | ⏳ **IN PROGRESS** — blocks recruitment |
| Chapters | Not started. Cluster memos folder still empty |

## Loose ends from the retrofit

The naming convention (`planning/naming_convention.md`) was applied to governance notes correctly. Interview notes are **half-migrated**:

- **Missing slugs** — `I1_castillo-montoya2016`, `I2_shoozan2024`, `I5_freeman2025`, `I6_meng2026`, `I8_moss2026`, `I9_mokander2022`, `I11_leibowicz2025`, `I12_hogemann2025`, `I13_zhi2025` are author+year only. The convention requires a 2–5 word slug.
- **Missing years** — `I3_ecu-ithakasr`, `I4_murtuza`, `I7_xie`, `I10_vu_agenticbpm`, `I14_sami_energycompany`. Take the year from each note's §6; if genuinely undated, record why in the bib.
- `literature/notes/_to_delete/` still holds six leftover `_append_s11_*.py` scripts (tracked in git — needs `git rm -r`).

Low priority. Finish it when the §12 pass runs, since that session touches these files anyway.

## Decisions in force — do not relitigate without reason

- **Theory spine:** Papagiannidis, Mikalef & Conboy (JSIS 2025) — structural / procedural / relational + Antecedents–Practices–Effects, after Tallon et al. (2013, *JMIS*, now held as A12). Luna's H-GenAIGF demoted to coding instrument and jurisdictional comparator.
- **Reframed to the working tier.** No participant authored a policy, so the study is how policy is *encountered, interpreted and adapted* by people producing analytical outputs, and whether that feeds back upward. Interview Phase 1 is **Policy Encounter & Interpretation**.
- **Sampling:** embedded multiple-case. Depth = Shopee TW (n=4, three levels, zh-TW) and Smartly FI (n=3). Breadth = 7 singletons. Two strata, never pooled. Document-anchored cases assess recall quality in the others.
- **BI-forcing:** critical-incident anchor, three-type menu, four process-trace questions. Warranted by Nahar's revealed-preference method.
- **Language:** English master, interpreted live, core items fixed bilingually; researcher translation, pilot-verified.
- **Coding:** hybrid. No a priori code may be the answer to the RQ.
- **Excluded and never cited:** `aigovslr2024rg` (A2), `govgenai2025amcis` (B2), `employeeexperiences2025` (D3 Mitchell), `algobiasbianalytics2025` (old E1). **Grey-tier, never load-bearing:** C1 Ganesh (JISEM, discontinued from Scopus 2024), C3 Judijanto (national index only).

## The open question the discussion must settle

**Is the engagement gap the thesis, or context for a thesis about evolution?**

Four independent sources in four venues say governance exists and fails to engage those it governs — Papagiannidis (*"deprioritized or considered an ancillary task"*), Nahar (*"check-the-box exercises"*), Ackerman (86% say frameworks need enhancement), Madanchian (the translational gap). The §11 harvest then showed almost nobody has looked: the gap is named, not studied. Albert's 14 participants are exactly the people it is about.

That is a sharper thesis than "how policy evolves" — but it is a different one, and only one can be the headline. This has been open for three sessions and should be closed before Chapter 2 is structured.

## Second structural question

**Cluster-mirroring (Plan 3) is now the wrong chapter architecture** and the decision to use it predates the current corpus. It was chosen when C and E were thin; the gap-fill has changed the balance — C now has 7 notes and E has 4. Re-examine Plan 3 vs Plan 1 (argument funnel) against the corpus as it actually stands, not as it stood on Sep 2. The claim-sentence headers bought as an option make the switch cheap.

## Also unresolved

- Amazon (participant #13, Business Operations) — confirm against the inclusion criterion and assign a tier.
- Optional pre-interview Likert items (from Ackerman) for a comparable case table — worth it, or does it prime the incident narrative?
- Cluster F PDFs not yet arrived.
- **Rolling-coding discipline** — familiarization memo within 48h of each interview, one log line per interview in `analysis/`. Named the #1 schedule risk on Sep 1 and still unimplemented.

## Standing constraints

Full draft end-November; **hard deadline Dec 15**. Word budget 18–24k: intro 10%, lit review 27%, method 15%, findings 25%, discussion 18%, conclusion 5% — the review is the section most likely to over-run and starve findings. Interviews Sep–Oct, blocked on ethics.

## Process rules that have already been violated once each

- **§6 AUTHORS/YEAR/VENUE output is a claim, never verified metadata.** Check against the publisher record. Two fabrications have occurred: NotebookLM inventing an affiliation for Mitchell, and a session asserting B8's authors were "already verified" when they were not.
- **Repetition is not verification.** The Mitchell affiliation was asserted twice and was wrong both times.
- **Agreement with a planning document is not verification against a source.** An ID mapping was once "confirmed" by reconciling against a plan file rather than against the notebooks.
- **MCP queries do not persist to NotebookLM chat history.** Never plan a compile step around exporting chat for MCP-sent queries; `_raw/` is the trail.
- **Write outputs into the repo, never hand back a download**, and show `git status --short` as evidence rather than claiming success.
