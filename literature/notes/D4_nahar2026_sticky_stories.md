# [D4] Nahar et al. (2026, CHI'26) — "I Don't Think RAI Applies to My Model": Engaging Non-champions with Sticky Stories for Responsible AI Work

**Bib key:** `stickystories2025`
**Verification status:** Verified from PDF (Sep 2, 2026) — arXiv:2509.22858 (unchanged eprint); full author list added.
**Cluster:** D — Responsible AI Adoption & Implementation
**Note version:** v2.2 (compiled Sep 2, 2026)

---

## 1. WHY
Traditional Responsible AI (RAI) tools — checklists, impact-assessment templates, rigid audit processes — engage only intrinsically-motivated "RAI champions" while failing to reach the broader majority of "non-champions," who dismiss governance mechanisms as tedious administrative hurdles. Non-champions view AI ethics as abstract/peripheral, producing an "engagement gap" where mandatory RAI assessments are completed superficially just to "check the box." The research designs an intervention to trigger "deep engagement" and genuine critical reflection among skeptical/indifferent developers.
*Location: Section 1, p.2–3.*

## 2. HOW (3-phase mixed-methods design)
- **Phase I — Formative field study** (Section 3.1, pp.6–7): qualitative/ethnographic field study in one large tech org mandating RAI. 22+ hours of observation, 50+ pages of field notes; shadowed 3 governance meetings (Apr–May 2023), 8 product team meetings (Jul–Oct 2023), 4 developer-governance working sessions (Aug–Nov 2023); plus 2 informal chats and 5 semi-structured interviews (2 governance champions, 3 data scientists).
- **Story generation & offline evaluation** (Section 5.1, pp.13–16): 15 diverse AI scenarios sampled from online ML case databases; 240 stories total (120 LLM-generated "sticky stories" via K-means clustering + GPT-4o-mini refinement loop; 120 zero-shot length-matched "baseline stories"). Late-2025 offline evaluation; 3 independent human annotators, Cohen's Kappa 0.478–1.000 vs. LLM-as-judge.
- **Phase II — User study** (Section 6.1, pp.16–20): mixed within/between-subject design. 29 practitioners recruited after filtering 291 screening responses to oversample non-champions and control self-selection bias. Participants analyzed their own production models under two fairness goals. Two-month follow-up survey for longitudinal impact.

## 3. WHAT
- "Engagement Gap" framework — social/organizational barriers causing practitioners to dismiss or "check the box" on mandated ethics templates. *(Section 3.2, pp.7–8)*
- "Sticky Stories" design principles: Surprisingness, Concreteness, Severity, Relevance, Diversity. *(Section 4.1, pp.9–10)*
- Compound AI Story Generation Pipeline — 8-step LLM system combining prompt engineering, demographic tailoring, K-means clustering, evaluator-generator refinement. *(Section 4.2, pp.11–12)*
- Six behavioral indicators of critical reflection: challenging assumptions, exploring multiple perspectives, connecting to wider systems, expressing surprise, iterative thinking, planning intentional change. *(Section 4.1/Table 1, p.10)*
- Sticky stories vs. baseline: ~3x (+207%) more time spent on harm identification; 4.5x more unique harm categories; 3.5x more subcategories identified. *(Section 6.4.1–6.4.2, pp.21–22)*
- Practitioner Engagement Profiles typology: Resistors, Indifferents, Followers, Learners, Champions. *(Section 6.4.5, pp.25–28)*

## 4. DEFINITION
- **Deep Engagement:** "more than just ticking boxes or going through the motions—it involves practitioners critically reflecting on potential harms, considering trade-offs thoughtfully, and retrospecting on their past experiences." *(Section 1, p.3)*
- **RAI Champion:** "...a term used by organizations such as Microsoft as a role title...to refer to both self-motivated advocates and formally designated and trained RAI roles." *(Section 2, p.4)*
- **Non-Champions:** "...the majority of practitioners—non-champions, those without prior motivation or formal RAI roles—and whether they would meaningfully engage with these resources or integrate them into their work." *(Section 1, p.2)*

## 5. CITABLE
- "...multiple studies warn that RAI processes risk becoming bureaucratic 'check-the-box' exercises rather than reflective, substantive practices... RAI documentation is often reduced to a compliance task, while fairness and explainability evaluations can become performative practices, sometimes criticized as ethics washing." *(Section 2.1, p.4)*
- "This underscores how carefully designed and actively supported governance mechanisms still require practitioner buy-in." *(Section 3.2, p.8)*
- "...sticky stories could be particularly effective if incorporated directly into practitioners' regular harm assessment workflows—such as embedding them within checklists or model cards—so they serve as recurring prompts rather than one-off interventions... bridging the gap between immediate engagement and sustained behavioral change." *(Section 7, p.28)*

## 6. AUTHORS/YEAR/VENUE
Nadia Nahar, Chenyang Yang, Yanxin Chen, Wesley Hanwen Deng, Ken Holstein, Motahhare Eslami, Christian Kästner (Carnegie Mellon University). 2026. *Proceedings of CHI Conference on Human Factors in Computing Systems (CHI'26)*, ACM. arXiv:2509.22858 (preprint eprint; DOI placeholder in manuscript).

## 7. INTERVIEW VALUE
- **Policy Framework Development:** "Stated vs. revealed preferences" gap (Section 6.1.5, p.18) → interview design should ask behavioral rather than attitudinal questions: "...we ask questions about behaviors rather than ask about preferences, focusing on revealed preferences..." Practitioner Engagement Profiles (Resistors/Indifferents/Followers/Learners/Champions, pp.25–28) → classify departments' policy readiness.
- **Implementation & Change Management:** Six-indicator critical-reflection coding scheme (Table 1, p.10) can be used as an interview/transcript coding rubric. Direct study prompts quotable: "What are your thoughts as you read this?" and a prompt probing "how the task influenced their understanding of fairness-related harms and whether they intended to take any concrete actions..." (Section 6.1.5, p.18).
- **Organizational Adaptation Dynamics:** Two-month follow-up questions directly reusable: "Have you reacted to or done anything based on the findings from our session...?" and "Have you had any discussions—positive or negative—about responsible AI with your peers since the session?" (Section 6.1.5, p.18). Transition trajectory model for Resistors: "Outright dismissal → Skepticism → Recognition of overlooked risks → Reframing as RAI-relevant issues" (Section 6.4.5, p.25).

## 8. SNOWBALL
1. Balayn, Yurrita, Yang & Gadiraju (2023), *"Fairness toolkits, A checkbox culture?"*, AAAI/ACM AIES 2023, 482–495. (References, p.29)
2. Madaio, Stark, Wortman Vaughan & Wallach (2020), *Co-Designing Checklists to Understand Organizational Challenges and Opportunities around Fairness in AI*, CHI 2020, 1–14. (p.30)
3. Raji et al. (2020), *Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing*, FAT* 2020, 33–44. (p.31)
4. Rakova, Yang, Cramer & Chowdhury (2021), *Where Responsible AI meets Reality: Practitioner Perspectives on Enablers for shifting Organizational Practices*, PACM HCI 5(CSCW1), 1–13. (p.31)
5. Rismani et al. (2023), *From Plane Crashes to Algorithmic Harm: Applicability of Safety Engineering Frameworks for Responsible ML*, CHI 2023, 1–18. (p.31)

## 9. LIMITATIONS (self-stated, across 3 phases)
**Formative study** (Section 3.1, p.6): shadowing limited to meetings, excluding day-to-day/informal work; recording prohibited (notes prioritized synthesis over verbatim); researcher interpretation bias; single-organization setting limits generalization.
**Story generation/offline eval** (Section 5.1.4, p.15): LLM-as-judge bias; coarse binary (0/1) rubrics miss nuance; only 15 curated scenarios limits external validity.
**User study** (Section 6.3, pp.20–21): short-term focus only; modest sample (n=29); social-desirability/selection/researcher interpretation biases; no-story control always administered first (order-effect confound); think-aloud protocol may inflate engagement; time-spent/harm-count are imperfect proxies for deep reasoning; real-project heterogeneity may mask/mimic effects; single researcher-facilitated exposure rather than repeated day-to-day integration.

## 10. BI LINK
"Business intelligence," "data warehousing," "decision-support" entirely absent. Adjacent mentions:
- "...15 scenarios (e.g., voice assistants, image search, email monitoring, and demand forecasting) for our evaluation." (Section 5.1.1, p.13)
- "...in-distribution data evaluation, out-of-distribution data evaluation, model red-teaming, and responsible AI auditing (e.g., fairness)." (Section 6.1.1, p.17)
- Reference [12] to an "analyticsvidhya.com" case-study portal. (Section 7, p.31)


## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `c1a59eb5-9232-49fe-82b8-d64267e38bf3` ("[D4] Nahar2025 — Sticky Stories for RAI Non-Champions"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

**Substantive — the richest working-tier evidence in the corpus.** Field study combining shadowing, baseline testing, and a two-month follow-up survey; directly designed around the reception question this pass targets.

(a) **Policy reach:** Formal channels include RAI assessment templates, training modules, and audit gates (Section 3.2, p. 8; Section 2.3, p. 5); governance-team members "providing active coaching, clearly explaining RAI goals and processes... proactively monitored progress, clarified doubts" (Section 3.2, p. 8) — in some orgs enforced via "mandatory harm assessment, governance teams, and formal review processes" (Section 6.4.5, p. 27).

(b) **Policy–practice gap — directly observed, not inferred:** researchers shadowed "a data scientist completing a system design template [who] skipped sections on fairness and validation, focusing only on tracing data sources that supported her immediate task" (Section 3.2, p. 8); in project meetings "RAI topics were virtually absent, mentioned only once in passing, and consistently treated as low-risk compared to client deadlines" (Section 3.2, p. 8); one team "completed the templates retrospectively solely to demonstrate compliance to clients... RAI was seen as extra paperwork rather than a tool for identifying or managing ethical risks" (Section 3.2, p. 8).

(c) **Attitudes:** Explicit check-the-box and dismissal quotes. Developer P17: "I don't really believe in it, to be honest. In my area of research, the societal harms are very low... that has nothing to do with code generation" (Section 6.4.5, p. 26). Practitioners "completed only minimal tasks to 'check-the-box' when directly asked by their managers and resisting prescribed processes" (Section 3.2, p. 8); P3 asked to "just copy and paste" a prior scenario rather than engage (Section 6.4.5, p. 26). No shadow-AI/covert-workaround behaviour documented — resistance is passive omission and retrospective box-ticking, not evasion.

(d) **Feedback channels:** Documented absence — no channel for practitioners to influence policy is described; governance is designed entirely by a separate "governance champions" group (Section 1, p. 3) while data scientists are passive recipients.

(e) **Uncovered situations:** Practitioners default to assuming no ethical concern exists rather than seeking guidance — e.g. "when a project did not directly involve gender or race, practitioners overlooked and dismissed other important risks... entirely without deliberation" (Section 3.2, p. 7–8); one data scientist asked about RAI concerns "immediately responded, 'there are no responsible AI concerns for this project,' without further reflection" (Section 3.2, p. 7).

Instruments: pre-screening survey (Section 6.1.1, p. 17), post-study reflection questions and two-month follow-up survey items including "Have you reacted to or done anything based on the findings from our session...?" (Section 6.1.5, p. 18).

## Albert's Questions
None beyond the standard Query 1 / Query 2 pair.
