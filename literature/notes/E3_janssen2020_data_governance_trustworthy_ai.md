# [E3] Janssen, Brous, Estevez, Barbosa & Janowski (2020) — Data Governance: Organizing Data for Trustworthy Artificial Intelligence

**Bib key:** `janssen2020datagovtrustworthy`
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.1016/j.giq.2020.101493 as printed. Note: shares surname "Janssen" with B8 (Marijn Janssen 2025) but is a distinct 5-author paper — no bib-key collision (`janssen2020datagovtrustworthy` vs. `janssen2025responsiblegenai`).
**Cluster:** E — BI / data governance
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill

---

## 1. WHY
BDAS (Big Data Algorithmic Systems) increasingly make consequential decisions; multi-source/dynamic data without oversight risks systemic bias, unlawful decisions, financial/social harm; organizational efforts prioritize AI experimentation over data governance. *Location: Sec.1, pp.1-2; Sec.2, p.2.*

## 2. HOW
Conceptual study, structural synthesis, framework development. No empirical dataset/sample/database search/time span; synthesizes IT governance, public administration, data quality, AI ethics literature into a 13-principle framework. *Location: Abstract p.1; Sec.5, pp.6-7.*

## 3. WHAT
- Tripartite data-governance typology: planning & control / organizational / risk-based. *(Sec.3, p.3, Fig.1)*
- System-level governance model linking regulation, input quality, algorithmic processing, output sampling, appeals. *(Sec.4.1, p.4, Fig.2)*
- Data Stewardship & Base Registry foundation. *(Sec.4.2, p.5)*
- Trusted Data Sharing Framework incl. Self-Sovereign Identity. *(Sec.4.3, pp.5-6)*
- 13 Data Governance Design Principles. *(Sec.5, pp.6-7, Table 1)*

## 4. DEFINITION
"Organizations and their personnel defining, applying and monitoring the patterns of rules and authorities for directing the proper functioning of, and ensuring the accountability for, the entire life-cycle of data and algorithms within and across organizations." *(Sec.1, p.2; also Sec.2 p.2, Sec.5 p.6)*

## 5. CITABLE
Executive/structural/standards-setting side, but offers behavioral/feedback claims.
- "Specifically, people are essential in these systems...thus data governance should provide incentives and sanctions to stimulate desirable behaviour of the persons involved in collecting, managing and using data." *(Sec.1, p.2)*
- "...the decision-making authority is hidden from the user directly affected by the outcomes, public officers become merely mediators rather than decision-makers, and automated public services become 'hidden bureaucrat'..." *(Sec.4.1, p.4)*
- "Such appeals can be used to scrutinize and further improve the BDAS." / "Incentives including monetary rewards could be offered for uncovering errors...Such incentives are used in the bug bounty programmes..." *(Sec.4.1, p.5; Sec.5, pp.6-7, Table 1)*

## 6. AUTHORS/YEAR/VENUE
Marijn Janssen, Paul Brous, Elsa Estevez, Luís S. Barbosa, Tomasz Janowski. 2020 (online 21 June 2020). *Government Information Quarterly*, Vol.37, Issue 4, Art.101493. DOI: 10.1016/j.giq.2020.101493.

## 7. INTERVIEW VALUE
Moderate — conceptual/design-science paper bridging data governance to AI trustworthiness, no original interviews but AI-specific constructs directly relevant:
- **Policy Encounter & Interpretation:** links data-governance principles (accountability, transparency, quality) to AI-specific trust requirements (Sec.3, Framework); governance "arrangements" as the operationalization point (Sec.3.2).
- **Implementation & Change Mgmt:** governance structures spanning the full AI data lifecycle (Sec.3.3); accountability mechanisms when AI decisions are contested (Sec.4).
- **Organizational Adaptation Dynamics:** frames data governance for AI as requiring continuous adaptation as systems evolve post-deployment (Sec.4, Discussion).

## 8. SNOWBALL
1. Floridi et al. (2018), "AI4People—An Ethical Framework for a Good AI Society" — shared foundational ethics-framework source with A11.
2. Khatri & Brown (2010), "Designing data governance," *CACM* 53(1) — foundational governance-domain framework, shared with A12/E2.
3. Janssen & van den Hoven (2015), "Big and Open Linked Data (BOLD) in government..." — prior work by overlapping authors on transparency/accountability tension.
4. Floridi & Cowls (2019), "A Unified Framework of Five Principles for AI in Society" — trustworthy-AI principle synthesis.
5. Mittelstadt, Allo, Taddeo, Wachter & Floridi (2016), "The ethics of algorithms: Mapping the debate" — foundational algorithmic-ethics mapping.

## 9. LIMITATIONS
1. Conceptual/design-oriented paper — proposes a framework rather than reporting empirical field data on organizational practice. *(Sec.1, Introduction)*
2. No discussion of how the proposed governance arrangements are actually received, interpreted, or resisted by working-tier staff.
3. Framework generic to "AI" broadly rather than GenAI or BI-specific.

## 10. BI LINK
No explicit "business intelligence" or "BI" terminology found. "Decision-making" appears generically regarding AI system outputs and their trustworthiness implications (Sec.1-2), not specifically BI tooling. Data-governance domain overlaps conceptually with BI data-quality/data-warehouse governance but the paper does not make this link explicit.

## 11. WORKING-TIER RECEPTION
Documented absence. Conceptual design-science framework paper with no empirical data on practitioner/working-tier reception. (a)-(e) all absent — no data on how governance arrangements are communicated to, interpreted by, resisted by, or adapted by working-tier employees; the contribution is at the level of framework design and macro-level accountability structures. Confirmed absence finding for the working-tier tally.

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
