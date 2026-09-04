# [A1] Batool, Zowghi & Bano (2024) — AI Governance: A Systematic Literature Review

**Bib key:** `batool2024aigov` | **Verification:** verified-doi (Research Square preprint, DOI 10.21203/rs.3.rs-4784792/v1, posted Jul 24 2024) | **Cluster:** A | **Note version:** v2

---

## 1. WHY — Research Problem & Motivation
Rapid expansion of AI technology introduces growing societal, operational, and ethical risks, yet existing AI governance frameworks remain scattered and difficult for organizations to evaluate and apply effectively (Abstract, p. 2; Section 1 Introduction, p. 2, 4). Prior systematic literature reviews focus narrowly on individual sectors or single governance levels, creating a research gap for a holistic, multi-level analysis of AI governance across the entire development lifecycle (Section 2 Background and Related Work, p. 4).

## 2. HOW — Method / Design
Systematic Literature Review (SLR) following Kitchenham et al. (2009) guidelines (Section 2, p. 4; Section 3, p. 4). Databases: Scopus and Google Scholar (Section 3.2, p. 6; Table 1, p. 6). Time span: 2013–2023 (Section 3.2, p. 6). Filtering: 2,918 papers → 225 abstract-screened → 61 full-text → 28 final primary papers via expert test-retest and snowballing (quality: 20 Good, 8 Fair, 0 Poor) (Section 3.1–3.3, p. 6–7; Fig. 1, p. 5).

## 3. WHAT — Key Findings, Frameworks, Typologies
- **4W1H framework**: Who is governing / Who is being governed / What is governed (data/system) / When (pre-during-post development) / How, mapped to 4 pillars (humans, data, systems, processes) (Abstract, p. 2; Section 4.1, p. 8–9).
- **5-Level governance typology**: Team / Organization / Industry / National / International (Section 4.2, p. 14; Fig. 3, p. 15).
- 7 of 9 governance solutions found operate at the organizational level; zero at team- or national-level (Section 4.2, p. 14).
- Only 3 of 28 papers comprehensively answer all 5 "4W1H" questions across all lifecycle stages (Section 4.1.1, p. 14; Section 7, p. 17).
- Most governance tools target only one or two ethical principles (mainly fairness and privacy), not a multi-principle approach (Section 5, p. 15–16; Table 5, p. 15).

## 4. DEFINITION — Core Governance Construct
> "AI governance encompasses a set of regulations, methods, procedures, and technological mechanisms used to ensure that an organization's development and deployment of AI technologies align with its strategies, principles, and goals." (Section 1 Introduction, p. 2)
> "An AI governance framework refers to structured approaches designed to systematically guide the development, deployment, and management of artificial intelligence systems, addressing ethical, regulatory, and operational considerations." (Appendix B Terminology, p. 24)

## 5. CITABLE — Key Claims for BI/Organizational Policy Thesis
1. "AI governance encompasses a set of regulations, methods, procedures, and technological mechanisms used to ensure that an organization's development and deployment of AI technologies align with its strategies, principles, and goals." (Section 1, p. 2)
2. "In an AI ecosystem, the human pillar plays an important role, as without human involvement, data, systems, or processes cannot be governed, and all four of these pillars are key elements of governance in an AI ecosystem." (Section 4.1, p. 8)
3. "The analysis reveals a critical gap in addressing the who, what, and when aspects of AI governance in a holistic manner. Only 3 studies have provided all the answers to questions." (Section 7, p. 17)

## 6. AUTHORS / YEAR / VENUE
Amna Batool, Didar Zowghi, Muneera Bano (CSIRO's Data61); posted July 24, 2024; Research Square (SLR preprint); DOI 10.21203/rs.3.rs-4784792/v1.

## 7. INTERVIEW VALUE
No pre-formulated interview instrument in the source. Constructs usable for a semi-structured interview protocol:
- **Policy Framework Development**: 4W1H can structure baseline questions ("Who in your BI teams owns AI governance? What is prioritized — data pipelines or generated reports?") (Section 4.1, p. 8–9).
- **Implementation & Change Management**: 5-level typology and the finding that org-level governance dominates but is often incomplete — probe how policy translates operationally, and whether team-level oversight exists at all (Section 4.2, p. 14; Fig. 3, p. 15).
- **Organizational Adaptation Dynamics**: the "holistic coverage deficit" (only 3/28 studies complete) — ask how organizations close who/what/when gaps over time (Section 4.1.1, p. 14; Section 7, p. 17).

## 8. SNOWBALL
- Lu, Zhu, Xu, Whittle, Zowghi, Jacquet — *Responsible AI Pattern Catalogue* (ACM Computing Surveys, 2022) — engineering-level governance patterns.
- Mäntymäki, Minkkinen, Birkstedt, Viljanen — *Hourglass model of organizational AI governance* (arXiv:2206.00335, 2022) — ethics-to-practice translation model.
- Papagiannidis et al. (2023) — *Toward AI governance* (Information Systems Frontiers) — structural/relational/procedural governance components.
- Agbese et al. (2023) — ECCOLA extension using GARP — links AI ethics to information governance / BI data management.
- Vakkuri et al. (2021) — ECCOLA method — agile, card-based ethics implementation tool.

## 9. LIMITATIONS (self-stated)
- Search limited to Google Scholar and Scopus only (Section 6, p. 16).
- Key terms "AI regulations," "AI ethics," "AI regulatory frameworks," "AI governance models" omitted from search string (Section 6, p. 16).
- Only 2013–2023 covered; 2024 studies excluded (Section 6, p. 16).
- White papers/industry reports excluded — may miss frameworks actually in use (Section 6, p. 16).
- Generalizability limited by scope of selected studies (Section 6, p. 17).

## 10. BI LINK
"Business intelligence," "data warehousing" absent from the text. Related mentions: "promote fair and transparent AI decision-making" (Section 4.1, p. 9); a fraud-detection algorithmic-decision paper in the bibliography (Appendix A, p. 23); one reference venue titled "International Journal of Business Analytics and Security" (Appendix A, p. 23).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `15a35a40-81af-49cb-b56f-aaf7553bf0ab` ("[A1] Batool2024 — AI Governance SLR"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Documented absence.** This SLR structurally defines "Operational AI practitioners" only as an object of oversight under its "who is being governed" 4W1H category (Section 4.1, p. 9), classified at "Team level" governance with examples such as faculty staff, IT firm managers, and healthcare providers governed by administrators/committees (Section 4.1.1, p. 10–11, Table 2). It contains no data on how these practitioners actually receive, interpret, resist, or work around governance — the review's own scope is limited to who governs whom, not how it is experienced.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
