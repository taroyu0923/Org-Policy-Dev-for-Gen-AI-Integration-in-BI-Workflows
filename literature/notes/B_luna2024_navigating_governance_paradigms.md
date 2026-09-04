# [B3] Luna, Tan, Xie & Jiang (2024) — Navigating Governance Paradigms: A Cross-Regional Comparative Study of Generative AI Governance Processes & Principles

**Bib key:** `luna2024paradigms` | **Verification:** verified-arxiv (arXiv:2408.16771); accepted AAAI/ACM AIES 2024 | **Cluster:** B | **Priority read** | **Note version:** v2

---

## 1. WHY
GenAI advances faster than global policy can track, leaving organizations to navigate a "convoluted nature of governance approaches" (p. 1, 4). Critical lack of standardized, consistent, actionable provisions across regions (p. 1). Motivation: build a Harmonized GenAI Governance Framework (H-GenAIGF) to give a collective view of global approaches and help policymakers/developers/industry identify gaps (p. 1, 2).

## 2. HOW
Empirical policy analysis + cross-regional comparative study + industry case study (p. 1, 4). Corpus: 15 government documents (2–459 pages) from EU, US, China, Canada, UK, Singapore (p. 1, 3), plus academic papers. Coverage up to early 2024. Adapted WEF taxonomy into 5 paradigms (risk-based, rule-based, principle-based, outcome-based, mixed) (p. 3). Manual "three-cycle consideration" coding into 4 constituents, 15 processes, 25 sub-processes (p. 3–4). Validation case study: applied H-GenAIGF to ChatGPT 3.5/4 (p. 3–4, 8).

## 3. WHAT
- **H-GenAIGF**: 4 constituents (Data, Model, Content Generation, Ethics) × 15 processes × 25 sub-processes × 9 principles (Transparency, Fairness, Integrity, Accountability, Auditability, Interoperability, Sustainability, Privacy, Responsiveness) (p. 4–5).
- Risk-based governance most comprehensive: EU 92%, US 75% coverage; principle-based (Canada 31%) and outcome-based (UK 21.8%) lag badly (p. 6, 9).
- Only "Ethical Alignment & Human Rights" aligns across all six regions — global fragmentation (p. 1, 5).
- China: >80% coverage on Data constituent but only 10% on ongoing Model governance (p. 6, 9).
- ChatGPT case study reveals gaps in model transparency, data-sourcing auditability, content moderation (p. 8).

## 4. DEFINITION
> Processes: "the primary categories of activities within GenAI governance." Sub-processes: "actions" under each process providing "a detailed view of how to address adherence." Principles: "essential fundamentals that drive governance adherence." (Section Methodology, p. 3)
> H-GenAIGF: "a Harmonized GenAI Framework... based on the current governance approaches of six regions... four constituents, fifteen processes, twenty-five sub-processes, and nine principles..." (Abstract, p. 1)

## 5. CITABLE
1. "Processes coverage by ChatGPT demonstrates that the H-GenAIGF could be generalized to industry examples. Matching company's policies to the processes, the 'minimum' required coverage can be executed..." (Case Study, p. 8)
2. "...many developers, AI providers and/or end users may find navigating the convoluted nature of governance approaches burdensome. Thus, the need for a harmonized framework to understand the processes of GenAI governance becomes essential." (H-GenAIGF, p. 4)
3. "...the lack of transparency in model processes could undermine trust and hinder the verification of compliance with ethical standards and legal frameworks, posing challenges in accountability, interoperability, and auditability..." (Case Study, p. 8)

## 6. AUTHORS / YEAR / VENUE
Jose Luna, Ivan Tan, Xiaofei Xie, Lingxiao Jiang — Singapore Management University; accepted AAAI/ACM AIES 2024; no DOI printed; arXiv:2408.16771.

## 7. INTERVIEW VALUE
- **Policy Framework Development**: 4-constituent taxonomy as a completeness checklist — "How does your policy distribute oversight across Data, Model, Content Generation, and Ethics?" (p. 3–4). Data-sourcing/consent probes under the Data constituent (p. 4).
- **Implementation & Change Management**: principle-to-process mapping and "minimum required coverage" concept — how are Transparency/Auditability/Interoperability turned into technical parameters? (p. 8–9). Quantitative evaluation instrument usable as a scoring rubric: "Covered (✓)... Partially Covered (-)... Not Covered ( )" (Cross-Regional Comparison, p. 6).
- **Organizational Adaptation Dynamics**: cross-jurisdiction paradigm fragmentation — how do BI pipelines adapt operating across risk-based vs. outcome-based regimes? (p. 4, 6). Model-drift monitoring and feedback mechanisms (p. 6).
- Analytical instrument for qualitative coding: the paper's own "three-cycle consideration" method (first analyst extracts, second reviews, third resolves disagreement) (p. 4) — directly reusable for this thesis's own interview-transcript coding.

## 8. SNOWBALL
- Birkstedt, Minkkinen, Tandon, Mäntymäki (2023) — AI governance: themes, knowledge gaps (*Internet Research* 33(7)).
- Mökander, Axente, Casolari, Floridi (2022) — Conformity assessments and post-market monitoring under the EU AI Act (*Minds and Machines* 32(2)).
- Ashok, Madan, Joha, Sivarajah (2022) — Ethical framework for AI and digital technologies (*Intl J. Information Management* 62).
- Chen, Wu, Wang (2023) — AI fairness in data management and analytics (*Applied Sciences* 13(18)) — direct BI/analytics fairness link.
- Laux, Wachter, Mittelstadt (2024) — standardisation/ethical disclosure pathways under the EU AI Act (*Computer Law & Security Review* 53).

## 9. LIMITATIONS (self-stated, Section "Limitations & Improvements," p. 9)
- Static snapshot — does not cover unseen future governance approaches (e.g., Japan's then-in-development GenAI rules).
- No expert-survey validation of the 15 processes/25 sub-processes yet.
- Governing principles not yet evaluated separately/quantitatively (no auditability metrics).
- Case study limited to a single company (OpenAI/ChatGPT); accessing internal policies for scoring is hard due to low transparency.

## 10. BI LINK
"Business intelligence"/"data warehousing"/"decision-support" absent from body text. Related mentions: "...enabling applications that range from content creation to decision-making processes, deeply influencing industries." (Introduction, p. 2); "Operational Integration refers to the seamless incorporation of AI models into existing technological infrastructures and business processes." (Model, p. 4). "Analytics" appears only in reference titles (Chen et al. 2023; Hutt et al., Learning Analytics and Knowledge Conf.).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `71b7253a-1fa7-4e74-9de1-044e99b0fc6f` ("[B3] Luna2024 — Navigating Governance Paradigms"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Documented absence.** This cross-regional comparative study (H-GenAIGF framework) operates strictly at the macro (country-level regulation) and corporate-public (ChatGPT compliance) levels; it contains no internal organizational or practitioner-experience data. The only developer-adjacent mentions are conceptual: standards should "spread a culture of safety and responsibility among AI developers" (Related Work / Academic Research for Governance, p. 2), and "many developers, AI providers and/or end users may find navigating the convoluted nature of governance approaches burdensome" (H-GenAIGF introduction, p. 4). No practitioner attitudes, workaround behaviour, or feedback channels are documented.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
