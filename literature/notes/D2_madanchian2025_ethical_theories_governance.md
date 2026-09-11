# [D2] Madanchian & Taherdoost (2025) — Ethical Theories, Governance Models, and Strategic Frameworks for Responsible AI Adoption

**Bib key:** `ethicaltheoriesgovmodels2025`
**Verification status:** Verified from PDF (Sep 2, 2026) — DOI 10.3389/frai.2025.1619029, published 16 July 2025.
**Cluster:** D — Responsible AI Adoption & Implementation
**Note version:** v2.2 (compiled Sep 2, 2026)

---

## 1. WHY
~70% of companies report minimal impact from AI adoption; only 13% of data science projects reach production. A severe translational gap exists between abstract academic ethical AI principles and industrial implementation. The study proposes an integrated framework aligning ethical theories, corporate governance, and performance outcomes.
*Location: Section 1, pp.1–2.*

## 2. HOW
Comprehensive literature review, synthesis and conceptual framework design — not a newly registered database search but a synthesis building on major meta-analyses: Jobin et al.'s 84 responsible-AI standards, Hagendorff's 22 AI ethical principles, Corrêa et al.'s meta-analysis of 200 global governance regulations. Scope spans classical philosophy (Bentham 1789, Kant, Mill 1861) through corporate guidelines/regulations 2017–2025.
*Location: Section 1, pp.1–2; Section 2, p.2.*

## 3. WHAT
- Comparative Ethical Overview (Table 1): utilitarianism, deontology, virtue ethics mapped to AI accountability. *(pp.2–3)*
- Interrelation Layer Model (Fig.2): Ethical Theories → Governance Models (CSR, stakeholder theory, risk management) → Practical Tools. *(p.4)*
- Ethical Risk Assessment Process (Fig.3): risk identification → evaluation (likelihood/impact) → mitigation → monitoring. *(p.6)*
- Ethical Decision-Making Models Synthesis (Table 2): nine-step comparison of behavioral/quantitative models. *(pp.5–6)*
- Industrial AI Risk Management Framework (Table 3). *(pp.6–7)*
- Ethical Development Paradigms (Table 4): Embedded Ethics (EE), Human-in-the-loop (HITL), Socio-technical approaches. *(pp.8–9)*

## 4. DEFINITION
"The term 'responsible AI governance' refers to the systems put in place by businesses to deal with the moral questions raised by AI." *(Section 2.2, p.2)*

## 5. CITABLE
- "A crucial translational gap that needs to be closed is highlighted by the discrepancy between the ethical AI concepts developed in academic literature and their actual use in industrial settings (Borg, 2022)." *(Section 1, p.2)*
- "Although traditional enterprise risk management (ERM) frameworks offer structure, they are too static for the dynamic and unpredictable nature of AI." *(Section 3.2, p.6)*
- "The adoption of responsible AI is significantly influenced by organizational culture, and leadership is a key component in creating an atmosphere where moral principles are given priority." *(Section 4, p.9)*

## 6. AUTHORS/YEAR/VENUE
Mitra Madanchian, Hamed Taherdoost. 2025. *Frontiers in Artificial Intelligence*, 8:1619029. DOI: 10.3389/frai.2025.1619029.

## 7. INTERVIEW VALUE
Purely conceptual; no empirical instruments. Mapped constructs:
- **Policy Framework Development:** Jobin et al.'s five convergent ethical tenets (p.2) → how does the org operationalize transparency/fairness/non-maleficence/responsibility/privacy in GenAI/LLM policy? Utilitarianism vs. deontology mapping (pp.2–3) → how are utilitarian value-maximization goals balanced against deontological privacy constraints?
- **Implementation & Change Management:** Pant et al. (2024)'s five experiential categories — awareness, perception, need, difficulty, approach (p.9, cited) → what difficulties do developers face moving from abstract policy to daily GenAI testing/deployment? Embedded Ethics vs. HITL (pp.8–9) → does the org embed ethicists in workflows or use human-governed review checkpoints?
- **Organizational Adaptation Dynamics:** Static ERM vs. AI-specific dynamic risk governance (p.6) → how has risk assessment evolved to catch model drift/algorithmic discrimination? Stakeholder fragmentation (p.8, cited) → how are conflicting priorities among developers, regulators, and users reconciled?

## 8. SNOWBALL
1. Schneider, Abraham, Meske & Vom Brocke (2023), *Artificial intelligence governance for businesses*, Inf. Syst. Manag. 40, 229–249. DOI 10.1080/10580530.2022.2085825.
2. Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022), *Putting AI ethics into practice: the hourglass model of organizational AI governance*, arXiv:2206.00335.
3. Zhang, Chan, Yan & Bose (2022), *Towards risk-aware artificial intelligence and machine learning systems: an overview*, Decision Support Systems 159:113800. DOI 10.1016/j.dss.2022.113800 — published in a premier BI/DSS journal.
4. Duan, Edwards & Dwivedi (2019), *Artificial intelligence for decision making in the era of big data*, Int. J. Inf. Manag. 48, 63–71. DOI 10.1016/j.ijinfomgt.2019.01.021.
5. Jobin, Ienca & Vayena (2019), *The global landscape of AI ethics guidelines*, Nat. Mach. Intell. 1, 389–399. DOI 10.1038/s42256-019-0088-2 — foundational 84-standard taxonomy.

## 9. LIMITATIONS
The authors do not state self-limitations regarding their own review/framework. Section 3.5 ("Limitations of existing responsible AI frameworks") critiques the *broader literature* instead: existing frameworks suffer from a "lack of appropriate evaluation mechanisms" and a "tendency to codify the agendas of powerful stakeholders rather than the interest of the broader public." *(Section 3.5, p.8)*

## 10. BI LINK
"Business intelligence"/"data warehousing" entirely absent from the body. Analytics/decision-support connections:
- "Predictive analytics ethics covers topics such as discriminatory decisions and contextually relevant insight." (Section 3.1, p.4)
- "...the Liverpool Football Club example demonstrates how human expertise and data analytics might come together to help bring about a sustained competitive advantage... (Lichtenthaler, 2020)." (Section 4, p.10)
- Zhang et al. (2022), published in *Decision Support Systems*, cited to justify "Scope clarification" and "Safety & reliability" steps in the industrial risk framework (Table 3, pp.6–7).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `cfdae1e1-4906-49f1-8e19-e8c7c49066b5` ("[D2] Madanchian2025 — Ethical Theories & Governance Models"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Partial.** This is a literature review (not primary empirical research), but it explicitly names a practitioner-level "translational gap" more directly than most Cluster A/B/C sources.

(a) Training/documentation described only as design recommendations: Meta's "responsible AI seminars" (Section 4, cited case) and various toolkits/maturity models developers "can use" (Section 3.1). No informal channels mentioned.

(b) The review states plainly: "practitioners frequently struggle to use these frameworks effectively, revealing a deficit in tools and knowledge" (Section 4); a "crucial translational gap" exists "between the ethical AI concepts developed in academic literature and their actual use in industrial settings" (Section 1); most frameworks focus on reporting/compliance and so "risk overlooking the day-to-day application of ethical principles in practice" (Section 3.5).

(c) No empirical attitude data (skepticism, workarounds, shadow use) — documented absence on this sub-point specifically. The review does cite a typology of "practitioners' experiences with ethics in AI" — awareness, perception, need, difficulty, approach (Section 3.1, citing Pant et al. 2024) — but without primary quotes.

(d) "Encouraging employees to raise ethical and bias issues" is named as a marker of ethical culture (Section 2.3), but the review also notes governance guidelines tend to "codify the agendas of powerful stakeholders rather than the interest of the broader public" (Section 3.5) — i.e. structurally top-down, with no evidence of practitioner-side use of any channel.

(e) Documented absence — not addressed.

## Albert's Questions
None beyond the standard Query 1 / Query 2 pair.
