# [B4] Joshi, Hassani, Gandhi & Hartman (2025) — Approaches to Responsible Governance of GenAI in Organizations

**Bib key:** `joshi2025resai` | **Verification:** verified-arxiv (arXiv:2504.17044); IEEE ISTAS 2025 | **Cluster:** B | **Priority read** | **Note version:** v2

---

## 1. WHY
Traditional AI governance frameworks focus on predictive modeling/structured data analysis, inadequate for GenAI's unpredictable, dynamic, hard-to-validate content generation (Section I-B, p. 1). Rapid GenAI/agentic adoption introduces misinformation, embedded bias, IP disputes, and "Shadow AI" (unauthorized employee use) — demanding adaptive, multi-layered oversight (Section I-B–I-C, p. 1–2).

## 2. HOW
Conceptual policy framework + qualitative synthesis of global governance literature with industry perspective (p. 1). Comparative review of **10 leading global frameworks** (NIST AI RMF, ISO/IEC 42001, Singapore Model AI Governance Framework, Alan Turing SSAFE-D) plus the MIT AI Risk Repository (1,600+ risks) (p. 2–3, 6). Weekly roundtable discussions with industry experts to validate recommendations (p. 1).

## 3. WHAT
- **Layered execution model**: Strategic (C-level/Board) → Tactical (business unit leads) → Operational (developers/data scientists) (p. 2).
- **4 risk quadrants**: Ethical, Operational/Technological, Data Privacy & Security, Legal & Regulatory (p. 1–2).
- **4 Core Pillars**: Ethical Practices, Data Governance/Privacy, GenAI Literacy/Education, Use Case Evaluation/Sandboxing — supported by 10 operational elements (p. 5–6).
- **Bidirectional governance**: top-down strategic roadmaps + bottom-up sandbox/engineering feedback (p. 6–7).
- **Six-stage GenAI lifecycle model**: Ideation → Data Collection → Model Dev/Testing (TEVV) → Deployment → Post-Deployment Monitoring (concept drift) → Retirement (p. 6–8).
- **Three-step implementation plan**: (1) Map existing risk frameworks (GenAI Risk Mapping Tool from MIT repository), (2) incorporate mitigation strategies (risk matrices), (3) training/up-skilling (p. 6–8).

## 4. DEFINITION
> "GenAI governance is a structured framework of policies and practices that guides the responsible development, deployment, and oversight of AI systems." (Section I-A, p. 1)

## 5. CITABLE
1. "Unlike static compliance measures, responsible GenAI governance is an adaptive strategy that integrates AI applications, whether developed internally or acquired, into an organization's long-term goals, ethical standards, and regulatory obligations." (Section I-A, p. 1)
2. "Conventional AI primarily focuses on predictive modeling and structured data analysis, while GenAI operates in more unpredictable and dynamic contexts, often generating content that is difficult to validate or control." (Section I-B, p. 1)
3. "The GenAI Risk Mapping tool serves as the critical link, transforming theoretical risk identification into targeted strategies for effective management..." (Section V-B.1, p. 7)

## 6. AUTHORS / YEAR / VENUE
Himanshu Joshi, Shabnam Hassani, Dhari Gandhi (Vector Institute for AI, Toronto), Lucas Hartman (Western University, London, Canada); 2025; IEEE International Symposium on Technology and Society (ISTAS 2025); no DOI printed.

## 7. INTERVIEW VALUE
- **Policy Framework Development**: strategic-level ownership — who co-designs high-level GenAI ethics with advisory councils vs. relying solely on IT/risk committees? (p. 1–2). Data-minimization vs. GenAI data-volume tension (p. 5–6). Pre-/post-deployment risk-categorization logic (Risk Mapping Tool) (p. 5).
- **Implementation & Change Management**: how do tactical leads convert executive policy into operational practice? (p. 2). TEVV isolation from early experimentation (p. 6, Section IV). Sandboxing to channel innovation and curb Shadow AI (p. 5–6).
- **Organizational Adaptation Dynamics**: mechanisms linking sandbox/engineering feedback to C-level strategy revision (p. 6–7). Emergence of a Chief AI Officer (CAIO) role distinct from CDO/CTO/CISO (p. 6–7). SME vs. large-enterprise scaling of the pillars (p. 6–7).

## 8. SNOWBALL
- NIST — AI RMF Generative AI Profile (NIST AI 600-1, 2024) — DOI 10.6028/NIST.AI.600-1.
- AI Verify Foundation (2024) — Singapore Model AI Governance Framework for Generative AI.
- Slattery et al. (2024) — The AI Risk Repository (MIT FutureTech).
- Smith et al. (2025) — Responsible Use of Generative AI: Playbook for PMs and Business Leaders (UC Berkeley / RE-AI).
- Vector Institute (2025) — Principles in Action Playbook.

## 9. LIMITATIONS
Authors **do not state limitations of their own framework/methodology**. They only discuss gaps in *existing external* frameworks (lack of operational-risk granularity, sector adaptability, accountability clarity, and unresolved third-party/vendor risk).

## 10. BI LINK
Literal terms absent, but explicit "structured data analysis" and "decision-support systems" mentions appear:
1. "Conventional AI primarily focuses on predictive modeling and structured data analysis, while GenAI operates in more unpredictable and dynamic contexts..." (Section I-B, p. 1)
2. "...GenAI and agentic technologies have transformed industries by enabling automation, creative content generation, and complex decision-support systems." (Section I-B, p. 1)
3. "...the potential for automation and decision-making support is immense, these systems also pose complex governance challenges..." (Section I-C, p. 1)
4. "Developing decision-support tools, such as risk matrices and GenAI lifecycle governance checkpoints, to aid AI risk evaluation..." (Section II-B.2, p. 3)
5. "GenAI's use in automated decision-making and content generation could lead to misinformation or procedural injustices..." (Section II-B.4, p. 4)


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `31d0ce0d-17be-440a-bcb5-4c4dfd652dda` ("[B4] Joshi2025 — Responsible Governance of GenAI"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Substantive.** This white paper (literature review + industry roundtable) is prescriptive rather than empirical, but describes working-tier reception in more operational detail than any other Cluster A/B source.

(a) **Policy reach:** Practitioners sit at the "Operational Level" (functional managers, data scientists, developers), executing governance set at Strategic/Tactical levels (Section IV.A, Levels of Execution). Policy reaches them via "GenAI and Data Literacy/Education" training designed to prevent misuse such as "uploading confidential content into GenAI tools like ChatGPT" (Section IV.D.1, Core Foundational Pillars); continuous SOP training (Section IV.D.2); and role-specific "Role-Based Training Modules... tailored to technical staff" covering ethics, compliance and technical risk (Section V.C, Step 3: Training and Up-skilling). Governance is also embedded directly in workflow tooling — risk matrices, decision-support templates, lifecycle checkpoints, and "Sandbox Testing Environments" for controlled experimentation (Section II.B.2; Section IV.C).

(b) **Policy–practice gap:** The paper names "Shadow AI" as its central gap — "the use of unauthorized AI models outside organizational oversight," where "employees or teams may develop and deploy AI tools independently, bypassing any established governance controls" (Section I.C.2, Key Governance Challenges). It notes employees "frequently use external tools for sensitive tasks like writing code or processing proprietary data" (Section IV.D.1) and states plainly that "many organizations struggle with the practical implementation of GenAI governance because existing frameworks lack industry-specific guidance" (Section II.B.2).

(c) **Practitioner attitudes:** The framework acknowledges a risk that compliance is experienced as a "burdensome process" if not smoothly integrated (Section II.B.2), and that teams bypass formal controls "when formal channels are slow, rigid, or absent" (Section I.C.2; Section III.E, Vendor and Third-Party Management). No empirical skepticism/compliance data is presented — these are the paper's own stated risks, not observed findings.

(d) **Feedback channels:** The paper prescribes a "Bidirectional Approach: Top-Down and Bottom-Up Governance" (Section IV.C) with "Continuous Feedback Loops" (regular meetings between technical teams and executive governance committees) and sandbox environments feeding findings back to strategy (Section IV.C), plus a stated aim to "empower individuals to report concerns or initiate changes themselves" (Section IV.D.2). These are recommended structural channels; the source gives no evidence of whether or how often they are actually used.

(e) **Uncovered situations:** The source implies practitioners resort to external, unauthorized GenAI tools when internal tooling does not meet an immediate need (Section IV.D.1) — the "Shadow AI" behaviour again — and prescribes internal sandbox environments as the intended alternative.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
