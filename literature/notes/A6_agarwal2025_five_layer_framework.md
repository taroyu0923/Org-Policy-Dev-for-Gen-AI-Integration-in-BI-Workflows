# [A6] Agarwal & Nene (2025) — A Five-Layer Framework for AI Governance: Integrating Regulation, Standards, and Certification

**Bib key:** `agarwal2025fivelayer` | **Verification:** verified-arxiv (arXiv:2509.11332) | **Cluster:** A | **Note version:** v2

---

## 1. WHY
High-level regulations (EU AI Act, NIST AI RMF) set broad ethical mandates but lack granular procedural guidance, evaluation methodologies, benchmarks, and tools for operational enforcement across sectors (Abstract, p. 1; Section 1, p. 1–2). Gap causes inconsistent evaluation, compliance uncertainty, and erosion of trust (Section 1, p. 1–2).

## 2. HOW
Conceptual framework design + policy analysis, validated by two qualitative case studies (Section 1–2, p. 1–2). Analyzed EU AI Act, OECD, UNESCO recommendations; technical standards (ISO/IEC 42001, ISO/IEC TR 24027, ISO/IEC TS 4213, IEEE 7001-2021, IEEE 3129-2023, India TEC TSFARAIS); open-source toolkits (ART, AI Fairness 360, Fairlearn, What-if, Aequitas, Nishpaksh); incident repositories (AIID, AIAAIC). 2 case studies; ~15+ standards; 5+ toolkits; literature/standards span 2017–2025 (Abstract p. 1; Section 4–5, p. 6–11).

## 3. WHAT
- **Five-Layer Governance Framework**: L1 Laws/regulations/policies → L2 Standards → L3 Standardized assessment procedures → L4 Standardized assessment tools/metrics → L5 Certification ecosystem (Section 3, p. 3–5).
- Multi-actor ownership: Governments (L1), Standards bodies (L2/L3), Academia/Industry (L4), Developers/Auditors (L5) (Section 3 & 6.3, p. 4, 12).
- Case Study 1 (AI fairness): validated across EU AI Act, ISO/IEC, India TSFARAIS, Nishpaksh tool; global gap in independent third-party fairness certification (Section 4, p. 6–9).
- Case Study 2 (AI incident reporting): governance void at all five layers — no legal mandate, no taxonomy, no severity procedures, no automated tools, no certification incentive (Section 5, p. 9–11).

## 4. DEFINITION
> "AI governance refers to a structured approach that spans regulatory frameworks, technical standards, assessment methodologies, and certification mechanisms to ensure AI systems are robust, trustworthy, and accountable." (Section 1, p. 2)

## 5. CITABLE
1. "While these frameworks provide crucial guidelines and risk management strategies for AI, they do not provide the detailed procedural guidance necessary for consistent implementation across various sectors and applications." (Section 1, p. 2)
2. "The strength of the five-layer framework lies in its ability to provide increasingly detailed guidance as one moves down the layers while simultaneously narrowing the focus to specific aspects of AI governance." (Section 1, p. 2)
3. "The assessment procedures to check for requirements may need programming or writing software code. Not every organization has the expertise or resources for this purpose..." (Section 3.4, p. 5)

## 6. AUTHORS / YEAR / VENUE
Avinash Agarwal (Department of Telecommunications, India), Manisha J. Nene (Defence Institute of Advanced Technology, India); 2025; working paper/manuscript; no DOI printed; arXiv:2509.11332.

## 7. INTERVIEW VALUE
- **Policy Framework Development**: L1→L2 policy-to-standard gap — "How does your org translate high-level regulatory guidance into concrete internal benchmarks?" (Section 1, p. 2; Section 4.1, p. 6). Multi-actor ownership question: who owns which layer internally? (Table 1, p. 4; Section 6.3, p. 11–12).
- **Implementation & Change Management**: L3/L4 code-dependency barrier — do teams write custom code or use pre-built toolkits (Fairlearn, AIF360)? (Section 3.4, p. 5). AI incident classification/taxonomy practices (Section 5.2–5.3, p. 10).
- **Organizational Adaptation Dynamics**: compliance-burden/resource asymmetry esp. SMEs (Section 6.2, p. 11); self- vs. third-party certification trust (Section 4.5, p. 8–9).
- Instruments referenced: TSFARAIS self-assessment questionnaire (Section 4.2, p. 7); IEEE CertifAIEd assessment criteria (Section 4.5, p. 8–9).

## 8. SNOWBALL
- Mökander, Schuett, Kirk, Floridi (2024) — Auditing LLMs: a three-layered approach (AI and Ethics 4(4)).
- Papagiannidis, Enholm, Dremel, Mikalef, Krogstie (2023) — Toward AI governance (Information Systems Frontiers 25(1)).
- Wirtz, Weyerer, Sturm (2020) — Dark Sides of AI: integrated governance framework (Intl J. Public Administration 43(9)).
- de Almeida, dos Santos, Farias (2021) — AI regulation: a framework for governance (Ethics and Information Technology 23(3)).
- Turri & Dzombak (2023) — AI incident documentation practices (AIES 2023).

## 9. LIMITATIONS
- TSFARAIS standard currently limited to tabular data + supervised learning (Section 4.2, p. 7).
- Global fairness-certification ecosystems immature/fragmented; regional initiatives still early-stage (Section 4.5, p. 8–9).
- SMEs disproportionately burdened by compliance costs (Section 6.2, p. 11).
- Weak regional enforcement, no multilateral harmonization; EU AI Act is region-specific (Section 6.2, p. 11; Section 6.5, p. 12).

## 10. BI LINK
"Business intelligence"/"analytics"/"data warehousing" absent. Related: ISO/IEC TR 24027 addresses bias "particularly in AI-aided decision-making" (Section 4.2, p. 7); EU AI Act promotes transparency "to enable scrutiny of AI decision-making processes" (Section 4.1, p. 6); incidents arise from "biased decision-making" (Section 5, p. 9).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `cb98c7ce-000d-4c8f-a30a-87c9709502e3` ("[A6] Agarwal2025 — Five-Layer AI Governance Framework"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Documented absence.** This source is a conceptual/policy-design proposal (a five-layer AI governance framework) validated by two case studies; it contains no empirical data, interview material, or findings on how practitioners experience governance. It treats developers only as abstract stakeholders: "developers often perform self-assessments, these lack independent validation" (Section 4.5, p. 8); SME "accessible training initiatives" appear only as a forward-looking policy recommendation, not observed practice (Section 6.2, p. 11). No practitioner attitudes, workarounds, feedback channels, or gap-handling behaviour are described anywhere in the text.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
