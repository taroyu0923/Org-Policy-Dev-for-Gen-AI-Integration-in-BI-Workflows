# [B6] Lee, Perera, Liu, Xia, Lu, Zhu, Salvado & Whittle (2024) — Responsible AI Question Bank: A Comprehensive Tool for AI Risk Assessment

**Bib key:** `lee2024questionbank` | **Verification:** verified-arxiv (arXiv:2408.11820) | **Cluster:** B | **Note version:** v2

---

## 1. WHY
Rapid enterprise AI adoption has created urgent need for RAI governance, yet only 10% of companies have publicly announced RAI policies (Section 1, p. 1–2). Existing risk frameworks stay high-level/abstract, failing to bridge policy goals with operational software-engineering practice across stakeholders and lifecycle stages, and lack integration between low-level technical controls and executive governance — causing siloed, fragmented risk assessments (Section 1–2, p. 1–3).

## 2. HOW
Five-phase mixed-methods study: SLR, reference-framework synthesis, iterative question-bank development, empirical evaluation via two case studies, 2022–2024 (Section 3, p. 4–5). Databases: ACM DL, IEEE Xplore, ScienceDirect, SpringerLink, Google Scholar + grey literature via Google Search — 10,988 academic papers + 3,160 grey-lit items retrieved; snowballing → 63 studies; 16 grey-lit frameworks synthesized (Section 3.1, p. 4–5). Reference frameworks: NIST AI RMF, EU ALTAI, Canada AIA, Australia NSW AI Assurance Framework, Microsoft RAI Impact Assessment Guide → 382 questions → 293 consolidated (Section 3.1–3.2, p. 4–5). EU AI Act (25 reqs → 10 Qs) + ISO/IEC 42001:2023 (30 reqs → 22 Qs) → final **245-question bank** (Section 3.4, p. 5). Case Study I: 8 research AI projects, 2 interview rounds (Section 3.3/5.1, p. 5, 13–14). Case Study II: 28 companies, ESG-AI investor framework, 42 tailored questions (Section 3.3/5.2, p. 5, 14–15).

## 3. WHAT
- **RAI Question Bank**: 245 questions, 26 main categories, 65 sub-categories, 8 core AI ethics principles (Section 4.1, p. 6–8).
- **Three-tier lifecycle model**: Level 1 (C-level) / Level 2 (project/line managers) / Level 3 (technical practitioners) mapped to 7 lifecycle stages (Section 4.1, p. 7–8).
- **Regulatory compliance scoring**: 21 EU AI Act requirements mapped to checklist items → weighted compliance score (Section 6.1, p. 16–17).
- **AI agent/foundation-model risk framework**: 5 RAI architectural plugins (Continuous Risk Assessor, Black Box Recorder, Explainer, Multimodal Guardrail, AIBOM Registry) + 8 model-evaluation requirements (Section 6.2, p. 17–19).
- **ESG-AI deep-dive toolkit**: 42-question matrix linking AI principles to 12 ESG investment topics (Section 5.2, p. 14–15).

## 4. DEFINITION
> "RAI is the practice of designing AI systems that deliver positive outcomes for individuals, groups, and society, while minimizing risks." (Section 1, p. 2)

## 5. CITABLE
1. "A recent report found that while many companies view AI as a promising technology and actively pursue AI opportunities, only 10% of those surveyed have publicly announced their Responsible AI (RAI) policies." (Section 1, p. 2)
2. "Advanced AI, including generative AI and foundation models (e.g., LLMs such as GPT-4), presents significant challenges due to its complexity, scale, and potential for misuse... Effective risk management for these systems requires transparency, accountability, and rigorous evaluation processes." (Section 2, p. 3)
3. "A key advancement of this study is the integration of a systematic approach that links lower-level risk questions to higher-level ones... ensuring a cohesive evaluation process across different levels of the organization." (Section 1, p. 2)

## 6. AUTHORS / YEAR / VENUE
Sung Une Lee, Harsha Perera, Yue Liu, Boming Xia, Qinghua Lu, Liming Zhu, Olivier Salvado, Jon Whittle — Data61, CSIRO, Australia; 2024 (study conducted 2022–2024); no DOI printed; arXiv:2408.11820.

## 7. INTERVIEW VALUE
Contains **actual reusable assessment questions** (not just constructs):
- **Policy Framework Development**: accountability structuring — "Does the company have designated responsibility for AI and RAI within the organisation?" and "Does the company have an accountability framework to ensure that AI related roles and responsibilities are clearly defined?" (Table 2, p. 14). Vendor/third-party model vetting: "Does the model provider conduct ongoing risk assessment and treatment?" and "Does the model provider assess the quality of the data sources used for training?" (Table 5, p. 19). Oversight-process question: "Do you define, assess, and document processes for human oversight in accordance with organizational policies?" (Fig. 5, p. 28).
- **Implementation & Change Management**: translation across tiers — Level 2: "Do you design the AI system with interpretability in mind from the start?" → Level 3: "Do you research and try to use the simplest and most interpretable model possible for the AI system?" (Section 4.1, p. 7–8). Risk-register instrument: risk ID, category, description, causes, mitigation, owner (Section 5.1, p. 13). Agentic guardrail question: "Does the agent monitor and control adversarial inputs, harmful or undesirable outputs to users and other components?" (Table 4, p. 18).
- **Organizational Adaptation Dynamics**: "Is there a mechanism to capture feedback by users of the system and enable user contestability?" and "Is there a recourse process planned or established for clients that wish to challenge the decision?" (Fig. 10, p. 33). Finding on early-stage limits: "projects at the inception phase may have a limited understanding of model accuracy" (Section 5.1, p. 14). Knowledge-siloing barrier: in commercial settings "individuals may only have knowledge specific to their roles" (Section 5.1, p. 14).

## 8. SNOWBALL
- NIST — AI RMF Generative AI Profile (2024).
- AI Verify Foundation (2024) — Singapore Model AI Governance Framework for Generative AI.
- ISO/IEC 42001:2023 — AI management system standard.
- Lu, Zhu, Xu, Xing, Harrer, Whittle (2023) — Reference architecture for foundation-model-based agents (arXiv:2311.13148).
- Zhang, Xia, Liu, Xu, Hoang, Xing, Staples, Lu, Zhu (2024) — Privacy and copyright protection in GenAI: a lifecycle perspective (IEEE/ACM AIEng-SE4AI).

## 9. LIMITATIONS (self-stated)
- Reliance on yes/no questions risks a "checkbox mentality" (low-quality artifacts/processes) if not carefully managed (Section 1, p. 2).
- Evidence-based quality metrics not yet applied to the entire 245-question bank due to scale (Section 5.2, p. 15).
- Inception-stage projects have limited model-accuracy understanding, affecting reliability/safety evaluation (Section 5.1, p. 14).
- Commercial-project auditing constrained by role-specific knowledge silos vs. flat research-team knowledge sharing (Section 5.1, p. 14).
- Question volume can feel excessive for lower-risk projects (Section 5.1, p. 14).

## 10. BI LINK
"Business intelligence"/"data warehousing"/"decision-support" absent from main text; "analytics" appears only in a bibliography title. Strong implicit link via "AI-based decision-making systems":
- "With the increasing reliance on AI-based decision-making systems in recent years, there is a growing demand for ethical AI, which is often perceived as requiring human oversight of automation..." (Section 4.3, p. 9)
- "AI-based decision-making is inherently complex and often operates at scale, making it difficult for stakeholders to access the decision process and raise objections..." (Section 4.8, p. 11)
- "...questionnaire to identify and mitigate risks associated with automated decision systems..." (Section 2, p. 3)

---
## Albert's Questions
Albert asked a follow-up in this notebook's own thread requesting the same content in Traditional Chinese (Taiwan usage) — not a substantive research question, so no additional Q&A content beyond the bilingual sections 7–10 answer already folded into this note above (turn 3 of the chat: "完成英文版本後，請另外提供一份繁體中文（台灣用語）版本..."). No other independent questions were asked in this notebook.
