# [I9] Mökander & Floridi (2022) — Ethics-Based Auditing: The AstraZeneca Industry Case Study

**Bib key:** `mokander-floridi2022`
**Verification status:** Compiled from NotebookLM analysis of user-provided PDF (Sep 3, 2026) — Cluster Interview set (interview-design/methodology references).
**Cluster:** Interview — Interview Protocol Design & Methodology References
**Note version:** v2.2 (compiled Sep 3, 2026)

---

## 1. WHY
Ethics-based auditing (EBA) is championed as a mechanism to bridge abstract moral principles and applied AI practice (pp. 2–3), but "important aspects of EBA – such as the feasibility and effectiveness of different auditing procedures – have yet to be substantiated by empirical research" (Introduction, p. 2). Organizations struggle because "the industry lacks useful tools to translate abstract principles into verifiable criteria" (Section 2, p. 5), and "there is still little understanding of how organisations implement EBA and what challenges they face in the process" (Introduction, p. 3).

## 2. HOW
Longitudinal **qualitative industry case study**, 12 months (Section 5, p. 11), tracking AstraZeneca from publishing AI ethics principles (Nov 2020) to evaluating its AI audit (Q4 2021) (pp. 11–12). Embedded participant observation of weekly prep/audit meetings plus **18 semi-structured interviews** with internal managers, developers, and external auditors (pp. 11–12). NVivo-coded (p. 12). Subject: a **14-week independent external AI audit** at AstraZeneca (pp. 9–10, 23).

## 3. WHAT
- Primary hurdles are governance, not technical: "mirror classical corporate governance challenges" — standard harmonization, material-scope definition, change management (Abstract, p. 1; Introduction, p. 3).
- Risk-based material-scope classification: low/medium/high risk by human impact and autonomy; excludes standard statistical tests like T-tests (Section 6.2, pp. 14–15).
- Compliance vs. Risk Assurance typology: standardize compliance assurance uniformly; localize risk assurance per business unit (Section 6.3, p. 16).
- Process-oriented audits reduce IP friction but "fundamentally unable to produce verifiable claims about the impacts" of self-learning AI over time (Section 6.7, pp. 19–20).
- Quantitative ethical metrics are most valuable to "spark ethical deliberation and negotiate trade-offs," not to binary-classify systems as ethical (Section 6.8, p. 22).
- EBA acts as an internal-change catalyst, motivating managers to communicate guidelines ahead of the audit event (Section 6.6, pp. 18–19).

## 4. DEFINITION
**Ethics-Based Auditing (EBA)**: "a structured process whereby an entity's past or present behaviour is assessed for consistency with moral principles or norms." (Abstract, p. 1; Introduction, p. 2)

## 5. CITABLE
> "...current best practice would demand harmonising EBA procedures that aim to provide compliance assurance across business areas. In contrast, EBA procedures that aim at risk assurance should be adapted locally to reflect how respective business areas understand risk." (Section 6.3, p. 16)

> "Such procedures can verify claims about technology providers' quality management systems but are fundamentally unable to produce verifiable claims about the impacts that autonomous, self-learning AI systems that co-evolve with complex environments may have over time." (Section 6.7, p. 20)

> "...without harmonised requirements, there is a risk that potentially sensitive development projects will only be outsourced to external partners. This is akin to what Floridi (2019) has labelled 'ethics dumping'..." (Section 8 Conclusions, p. 26)

## 6. AUTHORS/YEAR/VENUE
Jakob Mökander (Oxford Internet Institute, University of Oxford) and Luciano Floridi (Oxford Internet Institute; Dept. of Legal Studies, University of Bologna). 2022. *AI Ethics*. DOI: https://doi.org/10.1007/s43681-022-00171-7

## 7. INTERVIEW VALUE
Paper includes a full **Appendix 1 semi-structured interview protocol (pp. 43–45)**.

**Policy Framework Development**
- "How do (or would) you (and your team) define AI systems?" (Q2.1, p. 43)
- "How (if at all) have you and your team been involved in drafting the [organization's] AI ethics principles and the internal AI governance framework?" (Q1.4, p. 43)
- "What do you consider to be the biggest ethical risks posed by AI systems, both from an organisational and societal perspective?" (Q2.7, p. 43)
- "What would you consider as an important D&AI Ethics principle?" (Q3.3, p. 44); "What is the value that such principles would bring to you (and to [the organization])?" (Q3.4, p. 44)

**Implementation & Change Management**
- "How does your daily work relate to the design and deployment of AI systems?" (Q1.3, p. 43)
- "How are you (and your team) currently managing ethical risks when using or developing AI systems? ... What are the existing AI and data governance processes, policies, methods, initiatives, and tools...? And how effective are they?" (Q3.1, pp. 43–44)
- "Who is accountable for decision-making regarding the design or usage of AI systems within your team? How do you ensure that the design and use of AI systems respect [the organization's] risk and compliance policies?" (Q3.5, p. 44)
- "Is there a process for measuring data and algorithmic quality – biases, accuracy, balance, etc.? If yes, who is responsible for this?" (Q3.6, p. 44)

**Organizational Adaptation Dynamics**
- "How do you see your department using AI in the next two years? What potential risks/governance factors do you think are relevant?" (Q2.8, p. 43)
- "What technical and practical constraints have you faced during the implementation of ethics-based auditing of AI systems?" (Q4.6, p. 44)
- "Is there a mechanism whereby the ethics-based auditing procedure is linked to personal accountability?" (Q4.9, p. 44)
- "How stringent and enforceable should ethics-based auditing of AI systems be, in your opinion?" (Q5.1, p. 45)

## 8. SNOWBALL
1. Brundage, M., et al. (2020). "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims." arXiv:2004.07213 (References, pp. 28–29) — blueprint for external auditing mechanisms.
2. Mittelstadt, B. (2019). "Principles alone cannot guarantee ethical AI." *Nature Machine Intelligence*, 1(11), 501–507 (p. 37) — foundational critique of principle-only governance.
3. Floridi, L. (2019). "Translating Principles into Practices of Digital Ethics: Five Risks of Being Unethical." *Philosophy and Technology*, 32(2), 185–193 (p. 31) — corporate risks of superficial ethics ("ethics dumping"/"ethics shopping").
4. Raji, I. D., et al. (2020). "Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing." FAT* 2020, 33–44 (p. 39) — operational internal-audit framework for BI data-quality/model verification.
5. Raisch, S., & Krakowski, S. (2021). "Artificial intelligence and management: The automation–augmentation paradox." *Academy of Management Review*, 46(1), 192–210 (p. 39) — where human oversight must be preserved in AI/BI policy.

## 9. LIMITATIONS
- Construct validity: "we exclusively focused on observing and describing the challenges organisations face when implementing EBA procedures, rather than identifying or measuring the effects such procedures have on the behaviour of AI systems." (Section 7, pp. 23–24)
- Confirmation-bias/replication risk (Section 7, p. 24).
- Independence/funding constraint: "JM's doctoral research is funded through an Oxford-AstraZeneca studentship. When such dependencies exist, researchers may feel pressured to produce 'positive' results..." (Section 7, p. 24)
- Generalisability/partner bias/trade secrets: "the input provided by the industry partner can be biased or contextually limited... data controllers (like AstraZeneca) have an interest in not disclosing trade secrets." (Section 7, p. 24)

## 10. BI LINK
Never uses "business intelligence" or "data warehousing" literally (a "BIKG" acronym at p. 7 stands for "biological insight knowledge graphs," not BI). But extensively discusses analytics and decision-support:
- "We are not doing any AI projects. We are, of course, doing large scale analytics, but only using statistical techniques that have long been standard practice in the industry." (Manager P5, Section 6.2, p. 14)
- "Within Commercial, sales representatives typically rely on data analytics software (like CSR systems or predictive modelling) as a means to an end... analytics within Commercial is largely decentralised." (Section 6.3, p. 15)
- Interview protocol asks: "What AI technologies are underpinning the application? I.e., predictive/diagnostic, symbolic/connectionist, fully automated/decision support etc." (Appendix 1, Q2.4, p. 43)

## Albert's Questions
Turn 1 in this notebook returned an empty response from NotebookLM (technical dropout); Albert re-sent Query 1 as Turn 2, which was answered fully, then Query 2 as Turn 3, also answered fully (content above draws on Turns 2 + 3). No additional follow-up questions beyond the standard pair.
