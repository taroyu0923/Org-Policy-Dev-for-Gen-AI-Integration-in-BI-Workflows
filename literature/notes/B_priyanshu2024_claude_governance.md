# [B7] Priyanshu, Maurya & Hong (2024) — AI Governance and Accountability: An Analysis of Anthropic's Claude

**Bib key:** `priyanshu2024claude` | **Verification:** verified-arxiv (arXiv:2407.01557) | **Cluster:** B | **Note version:** v2
**Quality caution:** CMU course paper — NOT peer-reviewed; cite only as illustrative vendor-accountability case study.

---

## 1. WHY
As foundation models like Claude shape decision-making, information dissemination, and human interaction at scale (Section 1, p. 1), widespread deployment and commercial partnerships (AWS, Zoom, BCG) affect individuals often without their knowledge (Section 1, p. 1). Study addresses the gap between Anthropic's safety-centric branding and its actual accountability mechanisms, privacy disclosures, and Constitutional-AI-encoded biases (Section 1, p. 1).

## 2. HOW
Qualitative policy evaluation, threat analysis, case study (Section 1, p. 1). Maps Claude's practices onto **NIST AI RMF** (Govern/Map/Manage/Measure) and the **EU AI Act** risk tiers (Limited/High/Unacceptable) (Section 5–7, p. 4–6). Evaluated: Anthropic's Privacy Policy, Responsible Scaling Policy, Terms of Service, Acceptable Use Policy; the Constitutional AI (CAI) paradigm vs. a public "Polis"-survey-derived constitution (~1,000 respondents); external benchmarks (Stanford Foundation Model Transparency Index, BBQ bias benchmark) (Section 4–5, p. 1–6). Time span: 2022 (BBQ benchmark) to April 2024.

## 3. WHAT
- Anthropic ranks **36%** on Stanford's Foundation Model Transparency Index — severe opacity on training-data and device-data disclosures (Section 5.1, Fig. 7, p. 4).
- Governance/accountability deficit: corporate policies emphasize "responsibility" but lack enforceable "accountability" mechanisms (Section 6.1, p. 5).
- Third-party risk offloading: data protection deferred to cloud partners' (Google, Amazon) own policies (Section 6.1–6.2, p. 5).
- Constitutional AI limitation: static, "one-size-fits-all" ethical principles risk suppressing diverse cultural perspectives and perpetuating pre-encoded biases (Section 5.1.1, p. 5).
- **AI Safety Levels (ASL-1 to ASL-4+)** typology mapping capability thresholds to escalating safety/alignment/security protocols (Section 6, Fig. 9, p. 5).
- Three-pronged mitigation framework proposed: (1) multi-metric privacy disclosures (Accessibility/Time/Comprehension), (2) external benchmarking for hallucination/bias (HaluEval, R-Judge), (3) verifiable data-deletion/model-unlearning processes (Section 8, p. 6).

## 4. DEFINITION
> "These challenges motivate the need for AI governance — the processes, policies, and practices aimed at ensuring the responsible development, deployment, and use of AI systems." (Section 1, p. 1)

## 5. CITABLE
1. "The policies lack a defined accountability structure, emphasizing responsibility without clear accountability." (Section 6.1, p. 5)
2. "Despite Anthropic's repeated emphasis on Trust and Safety and data protection, they often defer to their partners' policies, leaving users to decipher whether data usage is permitted." (Section 6.1, p. 5)
3. "While well-intentioned, the Constitutional AI model's one-size-fits-all approach may inadvertently perpetuate biases encoded into its fixed framework, highlighting the need for a more dynamic, inclusive, and contextually aware ethical paradigm..." (Section 5.1.1, p. 5)

## 6. AUTHORS / YEAR / VENUE
Aman Priyanshu, Yash Maurya, Zuofei Hong — Privacy Engineering, School of Computer Science, Carnegie Mellon University; 2024 (SCS AI Governance course, Prof. Norman Sadeh); no DOI printed; arXiv:2407.01557.

## 7. INTERVIEW VALUE
- **Policy Framework Development**: accountability-vs-responsibility split — "How does your GenAI policy distinguish ethical responsibility from contractual/legal accountability for erroneous or biased BI outputs?" (Section 6.1, p. 5). Overlapping third-party/cloud-partner policy dependency audit questions (Section 6.1, p. 5).
- **Implementation & Change Management**: instrument — Accessibility/Time/Comprehension metrics and "Comprehension Surveys" for testing policy transparency uptake (Section 8.1.1–8.1.2, p. 6). Benchmarking criteria — factual-grounding BLEU scores for hallucination, statistical parity/group diversity/equalized odds for bias (Section 8.2.1, p. 6).
- **Organizational Adaptation Dynamics**: verifiable model-unlearning/data-deletion instrument (Section 8.3.1, p. 6). Central-vs-local adaptation of rigid "one-size-fits-all" AI constitutions to regional/cultural norms (Section 5.1.1, p. 5).

## 8. SNOWBALL
- Mäntymäki, Minkkinen, Birkstedt, Viljanen (2022) — Defining organizational AI governance (*AI and Ethics* 2(4)).
- Birkstedt, Minkkinen, Tandon, Mäntymäki (2023) — AI governance: themes, knowledge gaps, future agendas (*Internet Research* 33(7)).
- Papagiannidis, Enholm, Dremel, Mikalef, Krogstie (2023) — Toward AI governance: best practices/barriers/outcomes (*Information Systems Frontiers* 25(1)).
- Raji, Smart, White, Mitchell, Gebru, Hutchinson, Smith-Loud, Theron, Barnes (2020) — Closing the AI accountability gap: end-to-end internal algorithmic auditing framework.
- NIST — AI Risk Management Framework (2024).

## 9. LIMITATIONS (self-stated, Section 11, p. 7)
- "The analysis focuses primarily on Anthropic's Claude and may not fully capture the diverse range of AI systems and their unique governance challenges."
- "The proposed mitigation strategies, while promising, require further validation and real-world implementation to assess their effectiveness and potential unintended consequences."

## 10. BI LINK
"Business intelligence"/"analytics"/"data warehousing" absent, but decision-support/reporting language present:
1. "AI has become an integral part of modern society, pervading diverse domains from complex computational tasks and generating reports to mass communication, hiring decisions, and marketing efforts." (Section 1, p. 1)
2. "...their impact expands across numerous spheres, shaping decision-making processes, information dissemination, and human interactions on an unprecedented scale." (Section 1, p. 1)
3. "These LLMs are crucial as they underpin many AI systems, influencing outcomes and decision-making processes in areas that directly affect individuals and societies." (Section 1, p. 1)
4. Literature review references "complex medical decision-making scenarios" for Claude evaluation (Section 3, p. 3).


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `38493d87-2ef0-4533-9904-abd4d8c07a78` ("[B7] Priyanshu2024 — Claude Governance Analysis"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Documented absence.** This policy analysis of Anthropic's Claude against NIST AI RMF and the EU AI Act evaluates corporate-level policy design only; it contains no data on how technical staff experience or respond to governance. It cites the wider literature's own acknowledgment of "limited understanding of AI governance implementation... and insufficient operationalization of processes" (Section 3, Literature Review) and recommends that risk-metric evaluation involve "internal experts who did not serve as front-line developers for the system" (Section 6.4, NIST "MEASURE") — a policy design recommendation, not an observation of practitioner behaviour.

---
## Albert's Questions
*(none asked in this notebook beyond the standard two-query sequence)*
