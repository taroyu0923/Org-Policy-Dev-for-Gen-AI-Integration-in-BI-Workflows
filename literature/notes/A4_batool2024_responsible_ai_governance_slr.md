# [A4] Batool, Zowghi & Bano (2024) — Responsible AI Governance: A Systematic Literature Review

**Bib key:** `batool2024rai` | **Verification:** verified-arxiv (arXiv:2401.10896) | **Cluster:** A | **Note version:** v2

---

## 1. WHY
Escalating AI risks (bias, transparency, fairness) vs. an implementation gap — many governance solutions exist but their real-world effectiveness is unclear (Abstract, p. 1; Section 1, p. 1–2). Literature over-indexes on governance mechanisms ("how") while neglecting who holds accountability ("who"), at what lifecycle stage oversight occurs ("when"), and the human dimension (Section 1, p. 2; Section 3.1.1, p. 3–4; Section 5, p. 8).

## 2. HOW
SLR per Kitchenham et al., spanning empirical (n=19) and non-empirical (n=42) studies (Section 2, p. 2–3; Fig. 4, p. 4). Databases: Google Scholar, Scopus, ScienceDirect, IEEE Xplore, ACM Digital Library (Section 2, p. 2). Time span 2013–2023; query `((AI OR artificial intelligence) AND (governance))` (Section 2, p. 2). 2,918 papers → 225 screened → **61 final articles** (Section 2, p. 2; Fig. 1, p. 2).

## 3. WHAT
- **3W1H framework**: Who / What (4 pillars) / When (4 lifecycle stages) / How (Section 1, p. 2; Section 3.1, p. 3).
- **5 governance levels**: Team / Organization / Industry / National / International (Section 3.2, p. 5; Fig. 7–8, p. 5–6).
- Organization-level dominant (19/61 studies) but only 4/19 answer all 3W1H questions (Section 3.2, p. 5; Fig. 8, p. 6).
- 20/61 studies focus only on "how"; only 5/61 answer all 3W1H; zero evaluate the "human" pillar (Section 3.1.1, p. 3–4; Section 5, p. 8).
- Domain concentration: healthcare (10), robotics (3); 25 studies unspecified domain (Section 4 RQ2, p. 7; Fig. 9, p. 7).

## 4. DEFINITION
> "AI governance can be understood as encompassing a set of regulations, methods, procedures, and technological mechanisms utilized to guarantee that an organisation's utilization of AI technologies is consistent with its strategies, goals, and principles." (Section 1, p. 1)
> "Responsible AI governance" = "establishment of structures and procedures at various levels — team, organisation, and industry — to make sure the development and implementation of AI systems adhere to ethical principles..." (Section 1, p. 2)

## 5. CITABLE
1. Definition above (Section 1, p. 1).
2. "Out of these 19 organisational-level governance, only 4 ... had answers to all questions in 3W1H... the remaining 15 studies do not offer complete solutions." (Section 3.2, p. 5)
3. "There are a significant number of studies (20 out of 61) focused on answering the question of 'how' AI should be governed... while neglecting other aspects such as 'who' should be responsible... and 'at what stage'..." (Section 3.1.1, p. 3)

## 6. AUTHORS / YEAR / VENUE
Amna Batool, Didar Zowghi, Muneera Bano — CSIRO's Data61, Melbourne, Australia. No journal/DOI printed on manuscript header; arXiv:2401.10896.

## 7. INTERVIEW VALUE
- **Policy Framework Development**: 3W1H as a structuring checklist; paper's own reflective question — "If an organisation is not sure exactly what they need to govern — data, systems, processes, or humans — how can such an organisation reduce bias, establish accountability, fairness, transparency, etc.?" (Section 3.1.1, p. 4).
- **Implementation & Change Management**: lifecycle-stage ("When") probes — are governance checks continuous or gated at initial/design/development/deployment stages? (Section 3.1, p. 3)
- **Organizational Adaptation Dynamics**: multi-level stakeholder alignment — team vs. org-wide committee coordination (Section 3.2, p. 5; Fig. 7, p. 5).

## 8. SNOWBALL
- Mäntymäki et al. (2022) — Hourglass Model (arXiv:2206.00335).
- Sidorova & Saeed (2022) — stakeholder enfranchisement in AI governance decisions.
- Roger Clarke (2019) — Principles and business processes for responsible AI (*Computer Law & Security Review* 35(4)).
- Lu et al. (2022) — Responsible AI Pattern Catalogue (ACM Computing Surveys).
- Agbese et al. (2023) — ECCOLA + GARP extension (information governance link).

## 9. LIMITATIONS
- Excludes grey literature/white papers/company frameworks — flagged as future work (Section 5, p. 8).
- English-only, 2013–2023, five named databases only (Section 2, p. 2).
- Book chapters, reports, documentary articles excluded (Section 2, p. 2).
- Scope extended to non-empirical/secondary studies due to scarcity of empirical primary research (Section 2, p. 2).

## 10. BI LINK
"Business intelligence"/"data warehousing" absent. Related: "Big Data Algorithmic Systems (BDAS)" data-governance model (Table 2, p. 6); "promote fair and transparent AI decision-making" (Section 3.1, p. 3); "Decision-Makers" as key stakeholders (Fig. 7, p. 5); rule-based decision-making frameworks (Table 1, p. 5; Fig. 8, p. 6).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `35b3a3f4-287b-4a8d-b319-6f5f72c3d868` ("[A4] Batool2024 — Responsible AI Governance SLR"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Documented absence.** This SLR of 61 papers explicitly identifies the working tier as a gap in the literature itself, rather than reporting on it: "not a single study out of 61 has mentioned the human pillar to be considered to be governed" (Section 3.1.1, p. 3–4 — page confirmed by cross-check against this note's own §1–§10 verification pass; the re-query sent 2026-09-04 to confirm the page found that the raw text NotebookLM holds for this source carries no page markers of its own). It defines "operational AI practitioners" theoretically as those doing "day-to-day technical implementation" (Section 3.1) and concludes the field lacks human-centricity (Section 4, RQ3: Limitations and Challenges), but supplies no practitioner-level findings, instruments, or interview material of its own.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
