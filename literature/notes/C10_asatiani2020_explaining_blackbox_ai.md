# [C10] Asatiani, Malo, Nagbøl, Penttinen, Rinta-Kahila & Salovaara (2020) — Challenges of Explaining the Behavior of Black-Box AI Systems

**Bib key:** `asatiani2020blackbox`
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI not printed on the paper itself (venue: *MIS Quarterly Executive* 19(4)). Confirmed same day against the AIS eLibrary record (aisel.aisnet.org/misqe/vol19/iss4/7) — no DOI exists for this article; "no DOI" is the correct final status, not an unresolved lookup.
**Cluster:** C — Corporate governance / algorithmic accountability (public-sector case)
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill


> **PDF page check (Oct 1, 2026).** Checked against the PDF in `D:\Master\Thesis\Thesis Content`; printed pages. These override page numbers and quotes below. Log: `planning/s3_section11_spotcheck_2026-10-01.md` (or the session log named). §11 verdict changes, if any, wait for Albert's decision on the coding rule.
>
> Offset: *MISQE* 19(4); printed = PDF page + 258. The note's pages are article-relative — use journal pages: caseworker "David", handover "package of management consultancy training…" **p. 266** · "control tower" / "mute a model or change the threshold" (team leader) **p. 273** · Recommendation 4, "the difficult part has been to get the dialogue with the case workers" **p. 274** · review intervals "collecting feedback from application users and from data scientists" **p. 275**. "No workarounds" is not a located statement. §11: proposed **partial** (first-hand but thin; about controls on an in-house AI application) — not-absence either way.

---

## 1. WHY
Black-box AI decisions are inscrutable even to programmers; regulatory (GDPR right-to-explanation), ethical (bias), and safety pressures demand explainability, especially in public sector. Core RQ: "How can organizations reconcile the growing demands for explanations of how AI-based algorithmic decisions are made with their desire to leverage AI to maximize business performance?" *Location: Sec. "Organizations Need to Be Able to Explain...", pp.1-3; RQ p.2.*

## 2. HOW
Qualitative single case study (action design research) — Danish Business Authority (DBA) Machine Learning Lab. Aug 2018–Jan 2020, 4 iterative phases; author field observations from Sept 2017. 18 semi-structured interviews (13 informants), 153,195 words transcribed; field diary; document analysis of the Virk platform (~809,000 companies). *Location: Appendix A, pp.14-16; Sec. "ML Applications at DBA" pp.5-6.*

## 3. WHAT
- Six Elements of an Intelligent AI Agent (model, goals, training data, input data, output data, environment). *(Fig.1, pp.3-5)*
- Six-dimension managerial explainability framework. *(Table 1, pp.5-7)*
- Managerial control mechanisms over AI capacity. *(Figs.2-6, pp.7-11)*
- 4 strategic recommendations. *(pp.11-13)*

## 4. DEFINITION
"the ability to explain the rationale or logic behind algorithmic decisions to human stakeholders. IS researchers and academics refer to this area as the 'explainability' of black-box AI algorithms." *(p.2)*

## 5. CITABLE
Managerial policy design + case-worker enactment/feedback.
- "The ability to mute a model or change the threshold has been a major cultural factor in [the] business adoption of this technology." *(Sec. Dimension 6, p.10)*
- "This practice involves collecting feedback from application users and from data scientists on the algorithms' operation, with the functionality being adjusted accordingly." *(Concluding Comments, p.14)*
- "I think the difficult part has been to get the dialogue with the case workers, who see the world in a different way..." *(Sec. Recommendation 4, p.13)*
- "Acquiring the ability to explain thus requires a managerial solution; however, there is a scarcity of such solutions." *(p.2)*

## 6. AUTHORS/YEAR/VENUE
Aleksandre Asatiani, Pekka Malo, Per Rådberg Nagbøl, Esko Penttinen, Tapani Rinta-Kahila, Antti Salovaara. 2020. *MIS Quarterly Executive*. DOI not printed on paper.

## 7. INTERVIEW VALUE
HIGH — empirical single case study (Danish Business Authority), quoted diagnostic instruments across all 3 phases:
- **Policy Encounter & Interpretation:** "Is this level of complexity necessary for achieving the required functionality?"; "Could sufficient performance be obtained by means of a simpler alternative?" (Fig.3); environment-boundary questions (Fig.6).
- **Implementation & Change Mgmt:** onboarding via management consultancy training/capacity-building/documentation (caseworker "David"); "control tower" threshold-tuning/muting agency (team leader "Jason": "The ability to mute a model or change the threshold has been a major cultural factor..."); output-verification questions (Fig.5).
- **Organizational Adaptation Dynamics:** data/concept drift tension (caseworker "Daniel": "we had a case years ago where there were a lot of bakeries that committed a lot of fraud, but now it doesn't make sense to look for bakeries anymore..."); cross-functional dialogue (data scientist "Mark").

## 8. SNOWBALL
1. Martin (2019), "Designing Ethical Algorithms," *MISQE* 18(2), 129-142 (fn.5) — managerial accountability for embedding automated decisions into workflows.
2. Desai & Kroll (2017), "Trust but Verify: A Guide to Algorithms and the Law," *Harvard J. Law & Tech* 31(1) (fn.11) — human-in-the-loop oversight/contestability principles.
3. Robbins (2019), "AI and the Path to Envelopment...," *AI & Society* 35, 391-400 (fn.20) — deliberately constraining AI capacity to preserve managerial control.
4. UK/NZ Serious Fraud Office (2020), "The Use of Artificial Intelligence to Combat Public Sector Fraud: Professional Guidance" (fn.6) — practical public-sector substitution of strategic-priority explanations for technical ones.
5. Russell & Norvig (2010), *Artificial Intelligence: A Modern Approach*, 3rd ed. (fn.7) — foundational intelligent-agent model underlying governance-boundary design.

## 9. LIMITATIONS
1. Public-sector specificity — "Private-sector businesses may not feel they have as compelling a need to make their AI systems explainable..." *(Concluding Comments)*.
2. Single qualitative case-study scope (DBA only).
3. Cost burden of mandatory human verification. *(Recommendation 1)*
4. Adaptiveness-vs-explainability tradeoff of offline batch training. *(Recommendation 3)*

## 10. BI LINK
Decision-support explicit — "Private and public businesses and organizations are deploying AI applications to process vast quantities of data and support decision making" (Intro); author bio references "business analytics" (About the Authors, Pekka Malo); case handles structured financial reporting data (XBRL) at scale. "Business intelligence" and "data warehousing" terms themselves absent.

## 11. WORKING-TIER RECEPTION
> **§11 verdict under coding rule R1 (Oct 1, 2026, Albert approved; PDF-checked, `planning/s3_section11_spotcheck_2026-10-01.md`):** **partial** (was substantive; not-absence either way). First-hand caseworker voices, but about controls on an in-house AI application.

Strong substantive content — one of the four empirically strongest sources in this S3 batch. (a) Policy reaches caseworkers via structured onboarding packages, interactive "control tower" tooling, and cross-functional workshops. (b) No reported policy-violation gaps; only a communication/perspective gap between developers and caseworkers, and caseworker requests for more proactive drift detection. (c) High compliance/acceptance attributed to giving caseworkers threshold-control agency; no evidence of skepticism, check-the-box behavior, workarounds, or shadow use reported. (d) Practitioners influence design by specifying business requirements upfront, tuning thresholds in production, participating in co-design workshops, and periodic feedback reviews. (e) Edge cases (low-confidence outputs) revert to formal human fallback/manual verification by design — no informal workarounds documented. Explicit absence-of-resistance is itself noted as a finding tied to the public-sector, highly structured context.

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
