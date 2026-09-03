# [I8] Moss et al. — Controlling Context: Generative AI at Work in Integrated Circuit Design and Other High-Precision Domains

**Bib key:** `moss_controllingcontext`
**Verification status:** Compiled from NotebookLM analysis of user-provided PDF (Sep 3, 2026) — Cluster Interview set (interview-design/methodology references).
**Cluster:** Interview — Interview Protocol Design & Methodology References
**Note version:** v2.2 (compiled Sep 3, 2026)

---

## 1. WHY
GenAI is rapidly adopted in high-stakes, high-precision engineering workflows like IC design (pp. 1–2), but its statistical "hallucination"-prone nature raises questions about whether professionals in precision-demanding industries can maintain vigilance and safely rely on it (pp. 1, 3–4). Rather than focusing solely on model accuracy — a metric that often fails to capture organizational needs (pp. 5–6) — the study investigates how early adopters manage inaccuracies, what non-accuracy difficulties they face, and how they recover from "troublesome" encounters (p. 7).

## 2. HOW
Empirical qualitative study, semi-structured interview protocol (pp. 5–7). 17 interviews (n=17): 10 hardware engineers, 7 software engineers. Participants were mid-career/senior "intensive users" of internal GenAI tools — defined as generating >500,000 output tokens in the prior 30 days (pp. 5–7). Videoconference recordings, transcribed and turn-formatted via custom Python script; open coding with thematic grouping in MAXQDA (pp. 6–7). Conducted ~6 months after the firm's secure internal GenAI tools (some RAG-based) went live.

## 3. WHAT
- **Finding 1**: accuracy concerns are secondary/orthogonal to "trouble" from a mismatch between general-purpose models and highly constrained task contexts (pp. 2–3).
- **Finding 2**: engineers trust GenAI outputs because existing QA structures (validation, code review, unit testing) act as a safety net (p. 9).
- **Typology of "Trouble"**: table parsing (n=11), too-generic outputs (n=9), company-jargon misinterpretation (n=6), numerical-operation failure (n=6), hallucination (n=5), tone mismatch (n=4) (pp. 9–11; Table 2).
- **Repair and Recovery Framework**: Atomizing the Work, Iteration, Making Explicit, Organizational Workflows (pp. 11–13; Table 2).
- **Trouble-to-System-Elements Matrix**: maps trouble types to Pipeline, Features, Grounding (pp. 13–16; Table 3).

## 4. DEFINITION
- **Trouble**: "any difficulty or inconvenience users experience when interacting with a GenAI tool such that they A) must return to the interface and prompt the GenAI to refine its output, B) must edit or alter the output to make use of it, C) can articulate a way in which the output is suboptimal..., or D) resort to other, non-GenAI tools..." (Introduction, p. 2); condensed: "Trouble... is defined as anything needing repair and recovery." (Section 4, p. 7)
- **Controlling Context**: repair work arising from "the gap between the general-purpose nature of these tools... and the particular context in which they are brought to bear on concrete engineering problems" (p. 2); "Attempts to control the context of that conversation, whether new or old, are crucial for engineers' management of expectations around GenAI outputs." (Section 4.3.4, p. 13)

## 5. CITABLE
> "...it is not GenAI that hardware and software engineers need accuracy from, it is the overall sociotechnical system — the checks and rechecks, the documentation practices, and the testing systems — around the engineers that needs to be oriented toward accuracy, precision, reliability, and dependability." (Section 4.1, p. 9)

> "Additionally, organizations need to ensure novice engineers have pathways to gain the professional experience needed effectively supervise GenAI tools." (Section 6.1, p. 17)

> "A significant implication of the research presented above is that code review, pair programming, unit testing, etc. retain their importance and may even be more important as GenAI use grows." (Section 6.1, p. 17)

## 6. AUTHORS/YEAR/VENUE
Emanuel Moss, Elizabeth Watkins, Christopher Persaud, Passant Karunaratne, Dawn Nafus (Intel Labs / Intel, USA). No year/venue/DOI printed on layout (ACM Journal/CSCW-style formatting; references extend to 2025).

## 7. INTERVIEW VALUE
Paper contains an actual **Appendix A interview protocol (pp. 23–24)**.

**Policy Framework Development**
- "How important is accuracy in GenAI outputs, for you? ... What do you look for in an output to judge its accuracy?" (Appendix A, p. 23)
- "In the output, which bit is the worst for it to potentially have gotten wrong? What are the stakes if it's wrong?" (Appendix A, p. 23)
- "Are there any parts of your job role you can never imagine using these tools for?" (Appendix A, p. 24)

**Implementation & Change Management**
- "Would you please describe how you use GenAI tools, in your role? Could you give some concrete examples?" / "What makes a 'good' output for these tasks?" (Appendix A, p. 23)
- "Can you tell me about the worst — or a particularly bad — response you have gotten from these tools? What was bad about it? Were you able to navigate that response to still accomplish your task? How?" (Appendix A, p. 23)
- "What, precisely, do you do with outputs from GenAI tools? Do you copy-paste into another application? Do you record outputs somewhere other than the tool interface?" (Appendix A, p. 24)

**Organizational Adaptation Dynamics**
- "Has your approach to prompting changed over time, as your familiarity with these tools has increased?" (Appendix A, p. 24)
- "What are some roadblocks that make these tools more trouble to use than they might otherwise be?" (Appendix A, p. 24)
- "Which parts of your job role have changed the most since these tools became available?" (Appendix A, p. 24)

## 8. SNOWBALL
1. Makarius, E. E., et al. (2020). "Rising with the machines: A sociotechnical framework for bringing artificial intelligence into the organization." *Journal of Business Research*, 120, 262–273 (References, p. 20) — sociotechnical AI-adoption framework.
2. Brynjolfsson, E., Li, D., & Raymond, L. (2023). *Generative AI at Work*, NBER Working Paper w31161 (p. 21) — economic/operational impact data on workflows and worker skill distribution.
3. Noy, S., & Zhang, W. (2023). "Experimental evidence on the productivity effects of generative artificial intelligence." *Science*, 381(6654), 187–192 (p. 21) — productivity-shift evidence for KPI/performance-management policy.
4. Perry, N., et al. (2023). "Do users write more insecure code with AI assistants?" ACM CCS 2023, 2785–2799 (p. 21) — security vulnerabilities from generative coding assistants, relevant to BI/database query risk-governance.
5. Lee, H.-P. (Hank), et al. (2025). "The Impact of Generative AI on Critical Thinking..." ACM CHI 2025 (p. 23) — cognitive-offloading/overconfidence evidence supporting human-in-the-loop review requirements.

## 9. LIMITATIONS
- Domain specificity: findings mapped to IC designers/internal tools are highly specific; extending to other high-precision domains needs further comparative analysis (Section 1, p. 3; Section 5, p. 13).
- Uncertainty exposition omitted: "A full exposition on uncertainty in generative AI tools is beyond the scope of this paper" (Section 6.2, p. 17).
- Unevaluated RLHF contribution: "additional work is needed to assess the extent to which the trouble experienced by engineers can be attributed to RLHF." (Section 6.3, p. 18)

## 10. BI LINK
"Business intelligence," "data warehousing," "decision-support" are entirely absent. "Analytics"/"analytic" appears only in methodological/conceptual senses (qualitative coding categories; "analytical purchase over the 'sociotechnical gaps'," Section 7, p. 19) — no corporate BI platform discussion.

## Albert's Questions
Turn 2 in this notebook returned an empty response from NotebookLM (technical dropout); Albert re-sent the identical Query 2 prompt as Turn 3, which the model answered fully (content above draws on Turn 1 + Turn 3). No additional follow-up questions beyond the standard Query 1/Query 2 pair.
