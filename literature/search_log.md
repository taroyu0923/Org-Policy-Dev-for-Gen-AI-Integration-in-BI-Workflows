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

## S3 — Frequency-ranked snowball gap-fill **[PLANNED — not yet run]**

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

## S4 — Methods literature **[PLANNED — not yet run]**

Chapter 3 currently has no methodological citations from the corpus. Clusters A–E supply method *warrants* (Nahar's revealed-preference principle; Ackerman's network-sampling limitations; Papagiannidis's research agenda) but no methods foundation. Targeted additions required, 3–5 sources:

| Need | Likely source |
|---|---|
| Reflexive thematic analysis | Braun & Clarke |
| Critical incident technique | Flanagan (1954), and a modern methodological treatment |
| Embedded / multiple-case design | Yin, or Eisenhardt |
| Qualitative rigour and trustworthiness criteria | Lincoln & Guba, or a contemporary equivalent |

Not a cluster; a short targeted search, logged here as S4 when run.

---

## Log conventions

Each subsequent search adds a numbered section recording: date, database, exact query string, filters, hits, screened, kept, and rejected-with-reason. Snowball entries record the citing note as the source of the lead.
