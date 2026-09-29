# S3 post-check — §11 tally, §11 coverage, D7 Rakova

**Date:** Sep 11, 2026 | **Session:** Opus, structure/interview-framework discussion (pre-discussion checks)
**Method:** §11 verdict read from every governance note in `literature/notes/` and cross-checked against `literature/_raw/` for the 15 S3 sources. D7 read in full from the PDF (arXiv v4, 23 pp.). Verdicts below are this session's reading of the verdict lines — not the harvest agent's own table.

---

## 1. §11 tally

### Original corpus (20 usable) — re-read, unchanged

| Verdict | n | Notes |
|---|---|---|
| Documented absence | 14 | A1, A3, A4, A5, A6, A7, B1, B3, B5, B7, C1, C2, C3, E1 |
| Partial | 2 | D1, D2 |
| Substantive | 4 | B4, B6, D4, D5 |

### S3 additions (15) — verdict lines are NOT in the standard vocabulary; normalised here

| Verdict | n | Notes |
|---|---|---|
| Documented absence | 8 | A8, A10, A11, B8, C9, E2, E3, E4 |
| Contested | 2 | **C7** (raw: "substantive conceptual material"; note downgraded to "documented-absence-leaning" at compile) · **C8** ("no empirical field data, but substantive conceptual coverage") |
| Partial | 2 | A12 (executive-reported, second hand) · D6 (secondary synthesis) |
| Substantive | 3 | A9, C10, D7 |

### Headline figures

| Corpus | Absence | Rate |
|---|---|---|
| Original 20 | 14 / 20 | 70% |
| S3 15 alone | 8–10 / 15 | 53–67% |
| **Full 35** | **22–24 / 35** | **63–69%** |

Coding consistency: B4 Joshi (prescriptive white paper, no fieldwork) was coded *substantive* in the original pass; C8 has the same profile. Under a strict "empirical account required" rule applied to both passes: original 15/20 (75%), full 25/35 (71%).

**Direction:** down, modestly (70% → 63–69%; 75% → 71% under the strict rule). **Holds — not an artefact of the first search.** The S3 set was snowballed from a gap-naming corpus and deliberately included the closest analogue, which should enrich positives; the rate stayed above half anyway.

**What did change:** the empirical end. "Nahar observed it and nobody else did" (Pipeline_State) is no longer true — Rakova 2021 (D7), Asatiani 2020 (C10) and Papagiannidis 2023 (A9) all report practitioner-level data. The defensible claim is now about proportion *and* about who was sampled, not about sole occupancy.

## 2. §11 coverage on the 15 S3 notes

All 15 have a §11, and each has a matching §11 answer in `_raw/<ID>.md` (run inline in Query 2 per template v2.4). None missing. Defects:

- **Verdict vocabulary not enforced** — 7 of 15 lack a clean `substantive / partial / documented absence` opener (A9, A12, B8, C7, C8, C10, D6, D7).
- **C7 verdict changed at compile** without a note of why (raw substantive-conceptual → note absence-leaning).
- **C10** — no section/page locations anywhere in §11 (v2.3 unclear-point rule not applied); raw refers to "Query 1 §11 in prior pass", which Query 1 does not contain.
- **D7** — section references in §11 are wrong against the PDF (see §3).
- A9 and C10 substantive verdicts are **unverified against PDFs**; given D7, check before either carries weight.

Housekeeping: on disk there are 36 governance notes (A11 B7 C7 D7 E4), 35 usable. Pipeline_State says B 8 / 34 usable. No old-named note files remain in `literature/notes/`.

## 3. D7 Rakova et al. (2021) — scoop or position

### The compiled note contains fabricated content

- **§9 LIMITATIONS is invented.** The paper has no limitations section. The quoted "may not generalize to smaller organizations or those without dedicated responsible AI teams or roles" does not appear in the text. Items 2–4 are also not self-stated.
- **§7** "three-tiered organizational readiness model (proactive/reactive/exploratory)" is not in the paper; the actual scheme is prevalent / emerging / aspirational (§4.1, Table 2, p.7:10). The listed "enablers framework" is not the paper's.
- **§11** section mapping is shifted: §4.3 is "How do we measure success?", not channels; "informal channels argued more effective than formal ones" is not stated anywhere.
- The prior "position, not scoop" determination rested on the invented limitation, and per Albert was never delivered.

### What the paper actually is

26 semi-structured interviews, 19 organisations, late 2019; 21/26 US; convenience + snowball. Recruitment criterion (3): "were some aspects of their work related to the field of responsible AI" (§3.0.1, p.7:7). 15/26 held official RAI roles, 11/26 volunteered time for it (§4.1, p.7:9). Roles include Legal, Policy, HR, Marketing. Pre-GenAI; object is fairness/RAI work, not a usage policy. Analysis: affinity diagramming. Four organisational questions × prevalent/emerging/aspirational (Table 2, p.7:10). Full protocol in Appendix A (pp.7:21–7:23).

### Overlap (the part that is already taken)

- Upward feedback is already reported: volunteer-led bias investigations catalysed full-time teams (§4.2.1, p.7:11); "proactive champions organizing grassroots actions and internal advocacy with leadership have made responsible AI a company-wide priority" (§4.2.2, p.7:11).
- "individuals rather than organizational processes or structures remain the engine of proactive practices" (§4.2.2, p.7:11); ad hoc work on personal values, information spread through personal relationships (§4.5.1, p.7:15).
- Evolution framed as transitions between practice states, theorised through Orlikowski and Meyerson's tempered radicals (§1, §2.2.1, §6).
- Working-tier voice exists: data-science volunteer, "More senior people are making the decisions… People weren't open for scrutinization." (§4.4.1, p.7:14).

### Verdict

**Positions, does not scoop — on a different ground than the note gave.** Rakova sampled governance's *carriers*: people who had opted into responsible-AI work. Albert's inclusion criterion selects people who produce analytical outputs, unselected on RAI engagement — governance's *recipients*. Nahar (D4) studied non-champions in one organisation; Rakova studied champions across nineteen. Ordinary analysts encountering a written GenAI usage policy sit between them and are unstudied in this corpus.

"They didn't study BI" alone is weak — an examiner reads it as a population swap. The carrier/recipient distinction is the defensible one. If the thesis headline becomes "working-tier adaptation feeds governance upward", Rakova got there first for champions, and the thesis must say what differs when the adapters are not champions.

## Proposed actions (not yet applied)

1. Rewrite D7 §7, §9, §11 against the PDF; mark removed items in the note's history.
2. PDF-verify A9 and C10 §11 before either is cited as substantive.
3. Normalise S3 verdict openers; record the C7 decision.
4. Update Pipeline_State: counts (36/35, B 7), the tally range, and strike "nobody else observed it".
