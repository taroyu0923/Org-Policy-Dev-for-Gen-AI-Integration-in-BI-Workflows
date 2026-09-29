# Search Log (PRISMA-lite)

Required by amendment A1 (`claude/LitReview_Process_v2.md`). **No reference enters the corpus without a line in this log.** The methodology chapter cites this file.

**Maintained by:** Liu Yu-Shu (Albert) | **Opened:** Sep 2, 2026

---

## S1 — Original corpus compilation (reconstructed)

| Field | Value |
|---|---|
| Date | July 1, 2026 |
| Method | Web-search compilation (not a structured database query) |
| Databases | ⚠ **TO RECONSTRUCT** — see Research Plan §2.4 |
| Query strings | ⚠ **TO RECONSTRUCT** |
| Hits | 29 sources compiled; 43 bib entries after cluster expansion |
| Kept | Clusters A–F as originally scoped |
| Rejected | Not recorded at the time |

> ⚠ **Known weakness, to be stated in Chapter 3.** This search was not protocol-driven, and its record is partial. It is the origin of the corpus-quality skew identified in risk R3: over-representation of 2024–25 preprints and low-tier venues. Subsequent passes (S2 onward) are protocol-driven and fully logged. Chapter 3 must present S1 honestly as a convenience compilation rather than a systematic search, with S2 as the corrective.

## S2 — Verification and exclusion pass

| Field | Value |
|---|---|
| Dates | Sep 1–2, 2026 |
| Method | DOI/arXiv resolution per Process v2 step 1; venue and indexing checks via Crossref, arXiv API, SCImago, ISSN Portal, publisher records |
| Assessed | All Cluster A–E entries |
| Outcome | 21 usable notes; 3 excluded; 2 grey-tagged |

**Excluded**

| Key | Source | Ground |
|---|---|---|
| `aigovslr2024rg` | A#2, AI Governance SLR (ResearchGate misc) | Not available/reliable; no findable author or venue |
| `govgenai2025amcis` | B#2, Governance of Generative AI (AMCIS 2025) | Author list not locatable |
| `employeeexperiences2025` | D#3, Mitchell (2025), Preprints.org | Non-peer-reviewed; no self-limitations; §8/§10 unverified; **pipeline produced fabricated metadata** — NotebookLM asserted "Sapienza University of Rome" twice, Preprints.org record lists no affiliation (verified Sep 2, 2026) |

**Grey-tagged (background support only, never load-bearing, never sole citation)**

| Key | Source | Ground |
|---|---|---|
| `corpgovageai2025` | C#1, Ganesh et al. (2025), JISEM | SCImago: coverage 2019–2024, "Discontinued in Scopus as of 2024"; this article postdates it; no DOI; no self-stated limitations |
| `aigovalgoacc2026` | C#3, Judijanto et al. (2026), INJOSS | Garuda/aggregator indexing only, not Scopus or WoS; no DOI; corpus size undisclosed; no self-stated limitations |

## S3 — Frequency-ranked snowball gap-fill **[RUN — Sep 11, 2026]**

**Rationale.** Across the 21 compiled notes, the §8 SNOWBALL lists converge on a small set of sources that are consistently published in stronger venues than the corpus itself — particularly in Cluster C, where the references outrank the citing papers. Ranking by how many notes independently name a source gives a corpus-internal signal of the field's core, and simultaneously addresses three defects: Cluster C's collapse to one usable source, Cluster E's single low-tier member, and the missing theoretical lineage behind the chosen spine.

**Method.** Extract §8 entries from all 21 notes; rank by independent citing-note count; resolve DOI/arXiv per Process v2 step 1; Albert makes keep/reject calls; kept items enter the v2 notebook pipeline. Model: Sonnet.

**Inclusion criteria.** (a) Peer-reviewed journal or top-tier conference, or a standards body / national institution; (b) addresses organizational AI or data governance, responsible-AI practice, or IT-governance theory; (c) resolvable DOI or stable identifier.
**Exclusion criteria.** Venues discontinued from Scopus; national-index-only journals; non-peer-reviewed items without a compelling unique contribution; sources already in the corpus.

### Target list

| # | Hits | Source | Venue | Purpose |
|---|---|---|---|---|
| 1 | 4 | Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022) — Defining organizational AI governance / hourglass model | AI and Ethics 2(4); arXiv:2206.00335 | Core definition; ethics-to-practice translation |
| 2 | 3 | Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) — Toward AI governance | Information Systems Frontiers 25(1) | Core; distinct from the JSIS 2025 paper already held |
| 3 | 3 | Lu, Zhu, Xu, Whittle, Zowghi & Jacquet — Responsible AI Pattern Catalogue | ACM Computing Surveys 56(7) | Engineering-level governance patterns |
| 4 | 3 | Mökander, Morley, Taddeo & Floridi (2021) — Ethics-based auditing of automated decision-making systems | Science and Engineering Ethics 27(4) | **Cluster C rebuild** |
| 5 | 2 | **Rakova, Yang, Cramer & Chowdhury (2021) — Where Responsible AI Meets Reality: Practitioner Perspectives** | PACM HCI 5(CSCW1) | **PRIORITY — nearest existing study to the reframed working-tier design; determines whether this thesis is scooped or positioned** |
| 6 | 2 | Birkstedt, Minkkinen, Tandon & Mäntymäki (2023) — AI governance: themes, knowledge gaps, future agendas | Internet Research 33(7) | Core |
| 7 | 2 | Ashok, Madan, Joha & Sivarajah (2022) — Ethical framework for AI and digital technologies | Int. J. Information Management 62 | Core |
| 8 | 2 | Raji et al. (2020) — Closing the AI accountability gap: internal algorithmic auditing | FAT* 2020 | **Cluster C rebuild** |
| 9 | 1 | Shrestha, Ben-Menahem & von Krogh (2019) — Organizational decision-making structures in the age of AI | California Management Review 61(4) | **Cluster C rebuild**; decision-structure link |
| 10 | 1 | Asatiani et al. (2020) — Challenges of explaining black-box AI systems | MIS Quarterly Executive 19(4) | **Cluster C rebuild** |
| 11 | 1 | Tallon, Ramirez & Short (2013) — The information artifact in IT governance | J. Management Information Systems 30 | **Theoretical lineage of the structural/procedural/relational spine** |
| 12 | 1 | Abraham, Schneider & vom Brocke (2019) — Data governance: a conceptual framework | Int. J. Information Management 49 | **Cluster E rebuild** |
| 13 | 1 | Janssen, Brous, Estevez, Barbosa & Janowski (2020) — Data governance: organizing data for trustworthy AI | Government Information Quarterly 37 | **Cluster E rebuild** |
| 14 | 1 | Zhang, Chan, Yan & Bose (2022) — Towards risk-aware AI and ML systems | **Decision Support Systems** 159 | **Cluster E rebuild — genuine BI-family venue** |
| 15 | — | Janssen (2025) — Responsible governance of generative AI: a CAS conceptualization | Policy and Society 44(1) | Previously flagged; possibly closest paper to the original RQ |

**Also carried forward (previously flagged, not yet resolved):** Ulnicane (2025); Khanal, Zhang & Taeihagh (2025); Kongsten & Kathirgamadas (2024, NTNU MSc). And from A3/Ismail: Alan Turing Institute (Leslie et al. 2024, CARE/ACT), Government of Hong Kong SAR (2024, Ethical AI Framework), Barus et al. (2025) — ⚠ bibliographic details not confirmed in the captured transcript; verify against the Ismail2025 PDF reference list before treating as targets.

### S3 outcome (Sep 11, 2026)

All 15 target-list items were resolved via NotebookLM notebook_query (Q1+Q2 protocol) against the source PDF and assigned cluster IDs. **14 kept, notes compiled and committed to `literature/notes/`; raw Q1+Q2 harvest merged into `literature/_raw/<ID>.md`.** `references.bib` updated with all 14 entries (quality tier: all peer-reviewed journal/conference, no grey-tier flags — a marked improvement over S1/S2 corpus quality).

| ID | Bib key | Source | Kept? |
|---|---|---|---|
| A8 | `mantymaki2022definingaigov` | Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022) | ✅ |
| A9 | `papagiannidis2023towardaigov` | Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) | ✅ |
| A10 | `birkstedt2023themesgaps` | Birkstedt, Minkkinen, Tandon & Mäntymäki (2023) | ✅ |
| A11 | `ashok2022ethicalframework` | Ashok, Madan, Joha & Sivarajah (2022) | ✅ |
| A12 | `tallon2013informationartifact` | Tallon, Ramirez & Short (2013) | ✅ |
| B8 | `janssen2025responsiblegenai` | Janssen (2025) | ✅ |
| C7 | `mokander2021auditing` | Mökander, Morley, Taddeo & Floridi (2021) | ✅ |
| C8 | `raji2020closingaccgap` | Raji et al. (2020) | ✅ |
| C9 | `shrestha2019decisionmaking` | Shrestha, Ben-Menahem & von Krogh (2019) | ✅ |
| C10 | `asatiani2020blackbox` | Asatiani et al. (2020) | ✅ |
| D6 | `lu2024raipatterns` | Lu, Zhu, Xu, Whittle, Zowghi & Jacquet (2024) | ✅ |
| D7 | `rakova2021practitionerperspectives` | Rakova, Yang, Cramer & Chowdhury (2021) | ✅ |
| E2 | `abraham2019datagovframework` | Abraham, Schneider & vom Brocke (2019) | ✅ |
| E3 | `janssen2020trustworthyai` | Janssen, Brous, Estevez, Barbosa & Janowski (2020) | ✅ |
| E4 | `zhang2022riskawareai` | Zhang, Chan, Yan & Bose (2022) | ✅ |

**Note on E-cluster renumbering.** With E2–E4 now filled by the S3 rebuild, the E-cluster ID scheme was reset: `E1` = Khandan (2025) (the pre-existing single member, previously numbered informally as "the only entry"), `E2` = Abraham (2019), `E3` = Janssen (2020), `E4` = Zhang (2022). `algobiasbianalytics2025` — previously flagged as the closest topical match but unverifiable ResearchGate content — is formally **EXCLUDED** (see `references.bib`) and is not assigned an E-cluster slot; it is not renumbered into this scheme.

**Cluster totals after S3:** A 11 (6 retained + 5 new), B 8 (7 retained + 1 new), C 7 (3 retained + 4 new — Cluster C rebuild target achieved), D 7 (5 retained + 2 new), E 4 (1 retained + 3 new, plus 1 excluded).

## S4 — Methods literature **[PLANNED — not yet run]**

Chapter 3 currently has no methodological citations from the corpus. Clusters A–E supply method *warrants* (Nahar's revealed-preference principle; Ackerman's network-sampling limitations; Papagiannidis's research agenda) but no methods foundation. Targeted additions required, 3–5 sources:

| Need | Likely source |
|---|---|
| Reflexive thematic analysis | Braun & Clarke |
| Critical incident technique | Flanagan (1954), and a modern methodological treatment |
| Embedded / multiple-case design | Yin, or Eisenhardt |
| Qualitative rigour and trustworthiness criteria | Lincoln & Guba, or a contemporary equivalent |

Not a cluster; a short targeted search, logged here as S4 when run.

## S5 — Targeted search for Chapter 1 BI context and Chapter 2 theory anchors **[RUN Sep 29, 2026]**

**Trigger:** Chapter 2 outline draft (`planning/ch2_outline_draft_2026-09-29.md`) — three gaps the corpus cannot fill: BI work context (moved to Ch.1), a shadow-IT anchor for claim K5, an employee-voice / issue-selling anchor for SQ2.
**Method:** WebSearch (general web), then metadata check via Crossref API. No database filters. Not systematic — targeted anchor search.

| Query (WebSearch) | Kept |
|---|---|
| `shadow IT systematic literature review employees unauthorized IT use Haag Eckhardt` | G1 Haag & Eckhardt 2017 |
| `"shadow AI" generative AI employees unauthorized use organizations empirical study 2024 2025 journal` | B9 Silic et al. 2025 |
| `Dutton Ashford 1993 selling issues to top management Academy of Management Review doi` | G3 Dutton & Ashford 1993 |
| `Morrison employee voice and silence review Annual Review of Organizational Psychology doi` | G2 Morrison 2023 |
| `generative AI business intelligence analytics work data analysts journal article 2024 2025` | none — results low-tier (IAEME and similar) |
| `empirical study data analysts using LLMs ChatGPT in data analysis workflows interviews CHI 2024` | E6 Gu et al. 2024 |
| (snowball from A10 References p.159) | E5 Ain et al. 2019 |

**Rejected:** vendor/practitioner blogs on shadow AI (not academic); IAEME and similar low-tier "GenAI for BI" papers (venue); a DiVA student thesis on shadow AI (grey, student-level); Morrison 2014 (superseded by the 2023 review).
**Seen, not screened:** *Digital shadow AI risk theory (DART)*, Technological Forecasting & Social Change (2026) — screen if B9 proves thin.

**Finding recorded:** B9 reports empirical data on unauthorised AI use. Claim K5 ("no source observes shadow use") holds only within the 35-note corpus. Read B9 before framing K5 as a gap.

**Next (superseded):** Albert confirmed the IDs; harvest and compile completed Sep 29, 2026 (below).

### S5 outcome (Sep 29, 2026)

Six sources harvested through NotebookLM (one notebook per PDF, query template v2.4; Q1 and Q2 written to `literature/_raw/<ID>.md` as each answer returned), verified against the PDFs, then compiled. B9 ran full v2.4 including §11. E5, E6, G1, G2 and G3 ran v2.4-T (Q2 = §7–§10 then §13 THESIS ANCHOR); **§11 was not run** and none of the five enters the §11 denominator. The `TODO-verify` flag was removed from all six bib entries. Nothing was rejected at this stage. Chat history in all six notebooks was empty at compile, so no questions of Albert's own are recorded in the notes.

| ID | Bib key | Source | Kept | Verification finding worth recording |
|---|---|---|---|---|
| B9 | `silic2025shadowai` | Silic, Silic & Kind-Trüller (2025), *Strategic Change*, DOI 10.1002/jsc.2682 | ✅ | Interview count inconsistent inside the paper (10 in abstract, eight in body and Table 1). Survey items do not ask about the respondent's own bypass. One NotebookLM "finding" was the authors reporting Walters (2021). Scoop-or-position for K5: **position, not scoop**. |
| E5 | `ain2019bisuccess` | Ain, Vaia, DeLone & Waheed (2019), *Decision Support Systems* 125, 113113 | ✅ | Limitations at pp.10–11 (NotebookLM: p.9); NotebookLM's own citation numbers were embedded inside quotes. |
| E6 | `gu2024analystsverify` | Gu, Shang, Althoff, Wang & Drucker (2024), CHI '24, DOI 10.1145/3613904.3642497 | ✅ | NotebookLM added policy and governance framing the paper does not contain; one Appendix quote not findable. Single-company sample. Limitations pp.15–16. |
| G1 | `haag2017shadowit` | Haag & Eckhardt (2017), *BISE* 59(6):469–473, DOI 10.1007/s12599-017-0497-x | ✅ | Two altered quotes corrected ("employed users"; "either"). No limitations stated. |
| G2 | `morrison2023voicesilence` | Morrison (2023), *Annu. Rev. Organ. Psychol. Organ. Behav.* 10:79–107 | ✅ | A spliced quote corrected; page numbers off by one; "information redundancy" not supported by the body text; no limitations of the review stated. |
| G3 | `dutton1993issueselling` | Dutton & Ashford (1993), *AMR* 18(3):397–428 | ✅ | "Proposition 1" was really Proposition 2 (p.409); propositions number 1–17, not 16; no DOI printed in the PDF. |

**Snowball leads from §8 (not screened, no notebooks created):** from B9: D'Arcy (2011), Leonardi (2011), Silic & Back (2014), Walters (2021), Wirtz, Weyerer & Sturm (2020). From E5: Popovič (2017), Richards et al. (2017), Bischoff et al. (2015), Deng & Chi (2012), Arvidsson et al. (2014). From E6: Kandel et al. (2012), Kandogan et al. (2014), Liu, Althoff & Heer (2019/2020), Parasuraman & Manzey (2010), Zhang, Muller & Wang (2020). From G1: Fürstenau & Rothe (2014), Györy et al. (2012), **Martin et al. (2013)**, Horlach et al. (2017), Zimmermann et al. (2016). From G2: Liang et al. (2012), Detert & Edmondson (2011), Burris et al. (2017), Knoll & Redman (2016), **Dutton et al. (2001)**. From G3: Ancona & Caldwell (1988), Daft & Weick (1984), Dean (1987), Lyles & Mitroff (1980), Wooldridge & Floyd (1990). Bold = the two leads most likely to matter (Martin et al. for the K5/K11 distinction; Dutton et al. 2001 as the empirical follow-up to G3). Also seen, not screened (from the S5 search): *Digital shadow AI risk theory (DART)*, Technological Forecasting & Social Change (2026).

---

## Log conventions

Each subsequent search adds a numbered section recording: date, database, exact query string, filters, hits, screened, kept, and rejected-with-reason. Snowball entries record the citing note as the source of the lead.
