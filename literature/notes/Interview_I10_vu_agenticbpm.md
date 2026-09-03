# [I10] Vu et al. — Agentic Business Process Management: Practitioner Perspectives on Agent Governance

**Bib key:** `vu_agenticbpm`
**Verification status:** Compiled from NotebookLM analysis of user-provided PDF (Sep 3, 2026) — Cluster Interview set (interview-design/methodology references).
**Cluster:** Interview — Interview Protocol Design & Methodology References
**Note version:** v2.2 (compiled Sep 3, 2026)

---

## 1. WHY
Growing interest in GenAI/LLM-based agents drives organizations to deploy them (pp. 1–2), but the "stochastic (probabilistic) nature of LLMs raises critical concerns regarding how to govern the artifacts, decisions, and behaviors they produce" (p. 2). The research problem: how organizations can responsibly integrate and govern highly autonomous AI agents in business processes, given that practitioners' expectations, perceived risks, and even definitions of "agents" remain poorly understood (Abstract, p. 1; Introduction, p. 2).

## 2. HOW
Qualitative research design, qualitative content analysis (pp. 6–7). **22 semi-structured interviews** with BPM/automation practitioners: consultants (9), application owners (5), Center of Excellence experts (3), IT architects (2), process analysts (1), consulting managers (1), senior AI program managers (1) (p. 6). Countries: Germany (12), India (7), Austria (1), Malaysia (1), Australia (1); industries include Professional Services, Manufacturing, Telecommunications. Sessions 60–90 min (p. 6). No database search — primary empirical interview study.

## 3. WHAT
- **"BPM for Agents" paradigm shift**: from agents assisting traditional BPM ("Agents for BPM") to BPM governing/coordinating autonomous multi-agent systems ("BPM for Agents") (Section 2.4, pp. 4–5, Fig. 1).
- Benefits/risks typology: efficiency, compliance, scalability, data quality vs. AI bias, over-reliance, cybersecurity, job displacement, unauthorized decision-making (Section 4, p. 8, Fig. 3).
- Use-case/requirements mapping: master data maintenance, supply chain optimization, process monitoring vs. audit logs, access control, security, training, fallback systems (Section 4, pp. 8–10, Fig. 4).
- Liability framework: practitioners place primary responsibility for agent failures on the deploying organization, then developers/app owners (Section 4, p. 11, Fig. 5).
- **Six ABPM Adoption Recommendations**: Business Context, Operational Guardrails, Human-Agent Collaboration, Customization, Risk Management, Adoption (Section 5, pp. 11–12).
- Traditional BPM realignment: balance human-agent roles, define human involvement (peer vs. supervisor), adapt static→dynamic process structures, new governance performance metrics (Section 5, p. 12).

## 4. DEFINITION
**Agentic Business Process Management (ABPM)**: "describes i) the deployment and execution of autonomous software agents to achieve business process goals and ii) the application of agent-based abstractions for the process-oriented design and analysis of autonomous software agents." (Section 2.4, Definition 1, p. 5). Informal framing earlier: "governed introduction of AI agents into business processes" (Section 2, p. 4).

## 5. CITABLE
> "...rethinking BPM as a means to govern and coordinate agent-based systems ('BPM for Agents'). This distinction is crucial: while the former reflects the application of agents in traditional BPM contexts, the latter positions BPM as a discipline that adapts and evolves to meet the challenges posed by autonomous, self-adaptive multi-agent systems (MAS)." (Section 2.4, pp. 4–5)

> "Agentic AI introduces new dynamics—autonomy, adaptability, and self-learning—that challenge traditional BPM principles centered on structure, control, and standardization." (Section 7 Conclusion, p. 13)

> "'If it's routine, the decision itself should be documented. The more complex the task, the more I want to see how the process was developed.'" (Section 4 Results, p. 10)

> "'[The agent] would basically replace an FTE; let's just put it that way; you also have to provide it with the same framework that the employee would be confronted with because what would the employee do if they encounter difficulties?'" (Section 4 Results, p. 9)

## 6. AUTHORS/YEAR/VENUE
Hoang Vu (SAP, Germany), Nataliia Klievtsova (Technical University of Munich), Henrik Leopold (Kühne Logistics University), Stefanie Rinderle-Ma (TU Munich), Timotheus Kampik (SAP / Umeå University). No year printed (references extend to 2025); Springer LNCS-style layout, no DOI printed.

## 7. INTERVIEW VALUE
Paper's constructs/frameworks are directly mappable, but the **complete verbatim interview guide is not appended** (explicitly stated in transcript).

**Policy Framework Development**
- Benefits/risks taxonomy including "bias from flawed training data, over-reliance leading to diminished human judgment, and lack of transparency" (Section 4, p. 8) — baseline for what policy must address.
- Derived diagnostic question: "How does your policy framework account for the stochastic (probabilistic) nature of LLM agents, and what guardrails have you drafted to prevent unauthorized decision-making?" (derived from p. 8; Section 5, p. 11)

**Implementation & Change Management**
- Roll-out requirements: audit logs, access control, security, process integration, employee training (Section 4, p. 9, Fig. 4).
- Derived question: "What employee training protocols and process-reversion (fallback) systems are mandated by your implementation policies before AI agents are integrated into production?" (derived from p. 9; Section 5, p. 12)

**Organizational Adaptation Dynamics**
- "BPM Realignment Action Plan": redefining whether humans collaborate with agents as "peers" or "supervisors with selective intervention" (Section 5, p. 12).
- Derived question: "As AI agents transition from executing static tasks to driving dynamic, self-adaptive workflows, how is your organization redefining the reporting hierarchy between human workers and autonomous agents?" (derived from p. 12)
- Explicit statement: interviews "investigated the participants' understanding, expectations, and concerns related to agentic AI's autonomy, adaptability, human collaboration, and governance" (Section 3 Methodology, p. 6) — but no raw question list is provided in the source.

## 8. SNOWBALL
1. Dumas, M., et al. (2023). "AI-augmented business process management systems: A research manifesto." *ACM Trans. Manag. Inf. Syst.* 14(1) (Ref 1, p. 14) — theoretical vision for AI-augmented BPM systems supporting enterprise analysis/decision-support.
2. Berti, A., et al. (2024). "Re-thinking process mining in the ai-based agents era." arXiv:2408.07720 (Ref 2, p. 14) — LLM agents in process mining, a core BI/analytics pillar.
3. Haase, J., et al. (2024). "Interdisciplinary directions for researching the effects of robotic process automation and large language models on business processes." *Communications of the AIS*, 54 (Ref 3, p. 14) — compliance/ethical/organizational implications of LLMs in workflows.
4. Kampik, T., et al. (2024). "Large process models: A vision for business process management in the age of generative ai." *KI - Künstliche Intelligenz* (Ref 4, p. 14) — neural+symbolic AI vision for process design.
5. Rosemann, M., et al. (2024). "Business process management in the age of ai – three essential drifts." *Information Systems and e-Business Management*, 22 (Ref 5, p. 15) — organizational "drifts" for mapping policy evolution.

## 9. LIMITATIONS
- Small, homogeneous sample: "relatively small and predominantly drawn from experts at selected multinational organizations, which may not fully represent the diversity of experiences across various industries or among smaller enterprises." (Section 6, p. 12)
- Formative-concept problem: "the concept of agentic AI remains in its formative stage, as participants employed varied terminology and frameworks, making it difficult to develop a standardized definition." (Section 6, p. 12)
- No practical experience among interviewees: "none of the participants reported to have actual practical experience with agentic AI"; "the limited adoption and practical experience with this technology constrain the interpretation of the interview results." (Section 4, p. 7; Section 6, p. 12)

## 10. BI LINK
Never uses exact terms "Business Intelligence" or "Data Warehousing," but extensively discusses analytics/decision-support/dashboards:
- "...much of the current literature focuses on using LLMs from a conversational perspective—for tasks such as process understanding, information retrieval, and decision support—primarily addressing specific phases like discovery, analysis, and monitoring." (Section 2.3, p. 4)
- "Key applications include process monitoring to detect inefficiencies and suggest improvements, and predictive analytics to forecast trends and provide actionable insights... master data maintenance, user administration, root cause analysis, and decision support through dashboards." (Section 4, pp. 8–9)
- "Participants agreed that although agentic AI can autonomously handle low-stakes decisions, it should serve as a decision-support tool for complex process scenarios, ensuring human involvement to maintain accuracy and accountability." (Section 4, p. 10)
- "Organizations should develop governance frameworks that track the impact of agents on process efficiency, decision quality, and broader organizational outcomes." (Section 5, p. 12)

## Albert's Questions
None beyond the standard Query 1 / Query 2 pair.
