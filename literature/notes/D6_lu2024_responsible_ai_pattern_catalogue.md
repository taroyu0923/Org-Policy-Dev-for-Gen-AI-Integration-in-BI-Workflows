# [D6] Lu, Zhu, Xu, Whittle, Zowghi & Jacquet (2024) — Responsible AI Pattern Catalogue: A Collection of Best Practices for AI Governance and Engineering

**Bib key:** `lu2024raipatterncatalogue`
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.1145/3626234 as printed, *ACM Computing Surveys* 56(7), Art.173. Query 1 raw content was recovered/rewritten this session after an earlier truncated capture; full content re-verified against the persisted notebook output before this note was compiled.
**Cluster:** D — Responsible AI adoption / engineering practice
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill

---

## 1. WHY
See raw file `literature/_raw/D6_q1.md` for the full recovered WHY/HOW/WHAT statement — the pattern catalogue addresses the same principles-to-practice translation gap named across Cluster A, at the software-engineering-pattern level rather than the organizational-policy level.

## 2. HOW
Multivocal literature review (academic + grey literature: practitioner blogs, industry case studies, standards documents) synthesizing responsible-AI practices into a structured pattern catalogue.

## 3. WHAT
Three pattern categories: Multi-level Governance Patterns, Process Patterns, and Product Patterns. *(Sec.4)* Notable named patterns: "Continuous AI Ethics/Governance Checks" (Sec.5, Product Management Patterns), "AI Ethics Champion" role (Sec.5).

## 4. DEFINITION
Governance quote per raw file: engineering-level codification of ethical principles into checklists, roles, and process checkpoints (Sec.5.1).

## 5. CITABLE
- Code-of-ethics/employee-reliance quote: employees are expected to consult and apply codified ethical guidelines in daily engineering decisions. *(Sec.5.1)*
- Continuous-deployment pattern requiring governance re-checks at each release cycle. *(Sec.5.3, Process Patterns)*

## 6. AUTHORS/YEAR/VENUE
Qinghua Lu, Liming Zhu, Xiwei Xu, Jon Whittle, Didar Zowghi, Aurelie Jacquet. 2024. *ACM Computing Surveys*, 56(7), Art.173. DOI: 10.1145/3626234.

## 7. INTERVIEW VALUE
HIGH — concrete pattern catalogue directly usable as an interview coding frame:
- **Policy Encounter & Interpretation:** "Continuous AI Ethics/Governance Checks" pattern requiring teams to consult governance criteria at defined workflow checkpoints (Sec.5, Product Management Patterns); "AI Ethics Champion" role as a policy-interpretation intermediary (Sec.5).
- **Implementation & Change Mgmt:** three pattern categories map to implementation mechanisms (Sec.4); code-of-ethics/employee-reliance pattern (Sec.5.1); continuous-deployment governance re-checks (Sec.5.3).
- **Organizational Adaptation Dynamics:** catalogue framed as a "living" collection meant to adapt as practice matures (Sec.6, Discussion); tension between agile/rapid iteration and governance checkpoint overhead noted (Sec.5, Process Patterns discussion).

## 8. SNOWBALL
1. Morley, Floridi, Kinsey & Elhalal (2020), "From What to How..." — direct precedent for translating principles into concrete tools/patterns.
2. Vakkuri, Kemell, Kultanen & Abrahamsson (2020), "Implementing Ethics in AI: Initial results of an industrial multiple case study" — empirical industrial case study directly relevant to working-tier reception.
3. Rakova, Yang, Cramer & Chowdhury (2021), "Where Responsible AI Meets Reality" — same source as D7 in this corpus.
4. Ozmen Garibay et al. (2023), "Six Human-Centered Artificial Intelligence Grand Challenges" — broader human-centered AI governance framing.
5. Amershi et al. (2019), "Software Engineering for Machine Learning: A Case Study" — foundational ML-engineering practice patterns underlying several catalogue entries.

## 9. LIMITATIONS
1. Patterns synthesized from literature/grey/practitioner sources rather than original field interviews — not primary empirical data on practitioner reception, though it draws on such sources.
2. Authors acknowledge the catalogue is not exhaustive and requires ongoing community validation.
3. Patterns presented at a general/cross-industry level, not validated for any specific sector such as BI/reporting.

## 10. BI LINK
No explicit "business intelligence," "BI," or "data warehousing" terminology found. "Decision support"/"decision-making" appear generically regarding AI system outputs, not specifically BI tooling. The software-engineering/ML-lifecycle framing is broadly transferable to BI/analytics engineering contexts but not sector-specific.

## 11. WORKING-TIER RECEPTION
Substantive but secondary — catalogue synthesizes others' findings rather than reporting original fieldwork. (a) Policy reaches engineering teams via codified patterns — checklists, champion roles, checkpoint processes (Sec.5). (b) Tension between governance checkpoints and continuous-deployment/agile velocity explicitly named (Sec.5.3). (c) Attitudes not directly reported from original interviews, though cited empirical sources (e.g., Vakkuri et al.) are noted as documenting practitioner skepticism/resistance. (d) "AI Ethics Champion" pattern explicitly proposed as a two-way feedback conduit between governance bodies and engineering teams (Sec.5). (e) Catalogue recommends escalation to the champion role/governance board when patterns don't clearly apply — prescriptive guidance, not observed practice. Useful as a coding frame/vocabulary source, but working-tier content is secondhand (drawn from cited empirical studies) rather than original data.

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
