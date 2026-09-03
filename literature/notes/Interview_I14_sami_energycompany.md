# [I14] Sami et al. — Identifying and Prioritizing Generative AI Use Cases in an Organization: An Industrial Case Study (Energy Company)

**Bib key:** `sami_energycompany`
**Verification status:** Compiled from NotebookLM analysis of user-provided PDF (Sep 3, 2026) — Cluster Interview set (interview-design/methodology references).
**Cluster:** Interview — Interview Protocol Design & Methodology References
**Note version:** v2.2 (compiled Sep 3, 2026)

---

## 1. WHY
GenAI/LLMs are moving from experimentation to strategic adoption, but existing literature is predominantly restricted to technical capabilities or individual productivity gains (p. 1). There is a critical shortage of empirical insight into how organizations — particularly in the safety-critical, knowledge-intensive energy sector — practically identify, prioritize, and integrate GenAI into complex, multi-departmental business routines (Section 1, p. 1).

## 2. HOW
Single embedded case study of a mid-sized Nordic energy company (p. 3). Data: semi-structured group interviews, direct observations (field notes), internal documents (pp. 5–8). **16 group interviews** (~24 hrs recorded), **15 senior professionals** (technical, operational, trading, managerial, governance domains), **9 organizational units** (OF1–OF9) (pp. 5–9, 11). Thematic analysis on **8 fully transcribed interviews** → 166 raw quotations, 125 unique codes (pp. 9–10). Pilot cases used a vector database (LangChain/LangGraph agentic frameworks) evaluated with BERTScore (p. 16). 4-week embedded on-site research, March–April 2025 (p. 8).

## 3. WHAT
- **Typology of 41 AI use cases** across 9 departments in 6 categories: Reporting, RAG-based search, Predictive Maintenance, Anomaly Detection, Budgeting/Forecasting, Uncategorized (pp. 9–11).
- Visual taxonomy mapping 41 use cases to departmental workflows (Figure 2, pp. 10–12).
- **Five thematic adoption challenges**: Manual/Repetitive Work; Forecasting/Predictive Analytics; Data Fragmentation/Integration; Compliance/Validation; Organizational/Infrastructure Readiness (pp. 10, 13–15).
- **Prioritization Framework** (Table 5, pp. 12–13): business importance, ease of implementation, organizational value — reporting use cases ranked highest priority.
- Two agentic pilots: "Email Clone" system (0.89 BERTScore) and autonomous RAG chatbot (pp. 15–17).
- **Three-step phased adoption path**: (1) data-interface improvement, (2) assistive/reporting tools with human approval, (3) extension to forecasting/monitoring once data governance matures (Section 5.2, p. 18).

## 4. DEFINITION
No standalone quantitative governance variable; governance is conceptualized through **"workflow-fit"** and **"human-in-the-loop supervision"**:
- Workflow-Fit: "alignment between a new technology and existing work practices can often matter more than the technology's standalone capability" (Introduction, p. 1).
- Human-in-the-Loop: "A key design feature of the system is the integration of human-in-the-loop supervision. Rather than sending responses automatically, the generated emails are presented to a human operator for verification. The human can review, edit, and update the generated content before final approval. This design ensures reliability, accountability, and compliance with organizational standards..." (Section 4.2.1 Pilot Case 1, p. 16)

## 5. CITABLE
> "Existing literature argues that, in early-stage GenAI adoption, alignment between a new technology and existing work practices can often matter more than the technology's standalone capability." (Introduction, p. 1)

> "The findings suggest that the main issue is not the absence of possible use cases, but the fit between new tools and current work practices. ... Many identified use cases are feasible only if organisations first reduce data silos and improve system interfaces." (Section 5.1, pp. 17–18)

> "They expected support for checking and detection, but they did not argue for removing humans from the decision loop. This helps explain why gradual adoption and assistive use were preferred over full automation." (Section 5.1, p. 18)

## 6. AUTHORS/YEAR/VENUE
Malik Abdul Sami, Zeeshan Rasheed, Meri Olenius, Muhammad Waseem, Kai-Kristian Kemell, Jussi Rasku, Pekka Abrahamsson. Faculty of Information Technology and Communication Science, Tampere University, Finland. No printed publication year (data collected March–April 2025, references extend to 2026, indicating a 2026 manuscript/preprint). Supported by Research Council of Finland, project SYNTHETICA. No DOI printed.

## 7. INTERVIEW VALUE
Contains an explicit **Table 2 interview-question set (Section 3.2, p. 8)**.

**Policy Framework Development**
- Prioritization/value-governance instrument: use-case evaluation by business importance, implementation ease, organizational value (Table 5, pp. 12–13).
- "What concerns or hesitations do you have about AI adoption?" (Section 3.2, Table 2, p. 8)
- Human-control/actionability probe: "How should AI outputs be presented so they are actionable for your team?" (Table 2, p. 8)

**Implementation & Change Management**
- "What are the main challenges your department faces in day-to-day operations?" / "Which tasks or processes consume the most time or resources?" / "How are these challenges currently addressed (manual methods, tools, workarounds)?" (Table 2, p. 8)
- Opportunity-identification: "Where do you see opportunities for AI or automation to improve efficiency?" (Table 2, p. 8)

**Organizational Adaptation Dynamics**
- Cross-departmental dynamics: "How do these challenges impact collaboration with other departments?" / "Which challenges in your department also occur across other units?" (Table 2, p. 8)
- Role-evolution (supervisor vs. doer): "Are there areas where human errors often occur that AI could help reduce?" (Table 2, p. 8)

## 8. SNOWBALL
1. Russo, D. (2024). "Navigating the complexity of generative ai adoption in software engineering." *ACM Transactions on Software Engineering and Methodology*, 33(5), 1–50 (Ref 1, p. 23) — workflow-compatibility-driven adoption, not standard TAM metrics.
2. Jöhnk, J., Weißert, M., & Wyrtki, K. (2021). "Ready or not, ai comes—an interview study of organizational ai readiness factors." *Business & Information Systems Engineering*, 63(1), 5–20 (Ref 15, p. 25) — standardized organizational AI-readiness taxonomy.
3. Saarikallio, M., Kemell, K.-K., & Abrahamsson, P. (2026). "Towards ai transformation in software engineering - selecting generative ai use cases." SSRN (Ref 18, p. 24) — use-case selection criteria as a BI risk-governance tool.
4. Brehme, L., Dornauer, B., Ströhle, T., Ehrhart, M., & Breu, R. (2025). "Retrieval-augmented generation in industry: An interview study on use cases, requirements, challenges, and evaluation." arXiv:2508.14066 (Ref 21, p. 24) — RAG deployment governance hurdles (data quality, human-in-the-loop evaluation).
5. Uren, V., & Edwards, J. S. (2023). "Technology readiness and the organizational journey towards ai adoption: An empirical study." *International Journal of Information Management*, 68, 102588 (Ref 24, p. 26) — technology-readiness mapped to organizational adoption journey.

## 9. LIMITATIONS
- Single-case external validity: findings limited to one mid-sized Nordic energy enterprise; no benchmarking performed (p. 17-ish region, per Discussion/Limitations).
- Interpretive bias: coding/thematic analysis conducted primarily by the first two authors.
- Under-representation of junior staff: a senior contact scheduled interviewees, prioritizing senior staff/department leads, risking selection bias and reduced openness on sensitive issues.
- Incomplete transcription: only 8 of 16 group interviews were audio-recorded/transcribed; remaining 8 relied on researcher notes, limiting coding granularity.
- No baseline of prior AI knowledge assessed among participants.
- BERTScore metric applied only to the email pilot, not to the overall qualitative findings.

## 10. BI LINK
The exact phrase "Business Intelligence"/"data warehousing" does not appear, but the study is deeply situated in BI-equivalent territory (predictive analytics, decision support, data-driven planning):
- "AI has long been used in organisations for tasks such as automation, process optimisation, and decision support." (Section 1, p. 1)
- "These technologies have the potential not only to enhance specific tasks but also to reshape organisational processes by enabling automation and agentic capabilities that support autonomous decision-making." (Section 1, p. 1)
- "The role of the researcher during the interviews was to steer the discussion towards AI and data-driven decisionmaking..." (Section 3.2, p. 7)
- "The presence of forecasting activities across multiple units indicates that predictive analytics is a central requirement in the organisation, particularly for long term planning and operational decision making." (Section 4.1, p. 11)
- "Across all OF [Organisational Functions], AI and LLM based use cases focus on routine automation, data integration, and decision support." (Section 4.1, pp. 11–12)
- "These tasks remain manual because information is distributed across units and systems, and because employees still carry responsibility for validation before outputs can be used in operational or managerial decisions." (Section 5.1, p. 17)

## Albert's Questions
None beyond the standard Query 1 / Query 2 pair.
