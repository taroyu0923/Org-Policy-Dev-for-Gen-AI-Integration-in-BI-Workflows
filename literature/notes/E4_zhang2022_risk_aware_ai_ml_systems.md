# [E4] Zhang, Chan, Yan & Bose (2022) — Towards Risk-Aware Artificial Intelligence and Machine Learning Systems: An Overview

**Bib key:** `zhang2022riskawareaiml`
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.1016/j.dss.2022.113800 as printed. Venue (*Decision Support Systems*) is a genuine BI-family venue per `s3_gapfill_prompt.md`.
**Cluster:** E — BI / data governance (decision-support venue)
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill

---

## 1. WHY
AI/ML adoption in risk-sensitive environments (healthcare, manufacturing, aerospace) lacks a systematic framework for reasoning about risk/uncertainty/catastrophic outcomes; aggregate accuracy metrics mask pointwise/individualized risk. *Location: Abstract p.1; Sec.1, pp.1-2.*

## 2. HOW
Systematic conceptual overview/literature synthesis. Scope: supervised AI/ML only, excludes privacy/ethics. No quantitative search protocol/corpus/time span; illustrates with case studies (Uber fatal accident, Amazon hiring bias) and benchmark datasets (COMPAS, MNIST). *Location: Sec.1, p.2; Sec.2.1.1-2.1.3, pp.3-5; Sec.3, p.8.*

## 3. WHAT
- Two-tier risk taxonomy: Data-level (bias, dataset shift, out-of-domain, adversarial attacks) / Model-level (bias, misspecification, uncertainty). *(Sec.2, pp.2-7, Fig.1, Table 1)*
- Five critical research needs. *(Sec.3, pp.8-9)*
- Technical challenges typology: black-box nature, computational burden, domain-specific conceptualization delays. *(Sec.4, pp.9-10)*
- Reliability-engineering opportunities: safety margins, reliability-based design, verification/validation. *(Sec.4, p.10)*
- Managerial/policy recommendations. *(Sec.5, p.10)*

## 4. DEFINITION
"risk refers to the occurrence probability of hazardous (or bad) outcomes in an event." *(Sec.3, p.9)* "three key elements... the failure scenario..., the probability of failure, and the economic and societal losses caused by the AI/ML system failure." *(Sec.3, p.9)*

## 5. CITABLE
Executive/standards-setting/systems-engineering side, not empirical micro-enactment.
- "Dedicated managerial capacity and resources need to be allocated to adapt the existing risk assessment and management practices in place to suit the unique needs for AI/ML development." *(Sec.5, p.10)*
- "Proper workflow and procedures need to be established to actively monitor the risk of adopting AI/ML in dynamic environments... to reduce the liability of the company." *(Sec.5, p.10)*
- "traditional model risk management (MRM) typically takes 6 to 12 weeks of review time, and it is difficult to adopt it to the fast-pace and agile iterations during the development of AI/ML models...there is a pressing need for a risk management framework that can accommodate the features specific to the risks in AI/ML systems." *(Sec.3, p.8)*

## 6. AUTHORS/YEAR/VENUE
Xiaoge Zhang, Felix T.S. Chan, Chao Yan, Indranil Bose. 2022 (online 2 May 2022). *Decision Support Systems*, Vol.159, Art.113800. DOI: 10.1016/j.dss.2022.113800.

## 7. INTERVIEW VALUE
No empirical interview instrument (conceptual/technical overview). Constructs usable:
- **Policy Encounter & Interpretation:** developer blindspots/data-bias assumptions — data bias "often overlooked by many developers and researchers" (Sec.2.1.1, p.3); open-world vs. closed-world deployment assumptions (Sec.2.1.3, p.5).
- **Implementation & Change Mgmt:** oversight gaps — Uber fatal-accident NTSB finding of "inadequate safety risk assessment procedures" (Sec.1, p.2); temporal mismatch between 6-12 week traditional MRM cycles and agile ML iteration (Sec.3, p.8).
- **Organizational Adaptation Dynamics:** domain-specific risk conceptualization via subjective human/domain-expert judgment (Sec.4, p.9); dedicated managerial resource allocation for AI risk monitoring (Sec.5, p.9).

## 8. SNOWBALL
1. Babel, Buehler, Pivonka, Richardson & Waldron, "Derisking machine learning and artificial intelligence," McKinsey Quarterly — strategic managerial de-risking guidance.
2. Nushi, Kamar & Horvitz (2018), "Towards accountable ai: Hybrid human-machine analyses for characterizing system failure," AAAI HCOMP — hybrid human-machine accountability/failure diagnosis.
3. Wiens et al. (2019), "Do no harm: a roadmap for responsible machine learning for health care," *Nat. Med.* 25(9), 1337-1340 — operational roadmap for high-stakes deployment.
4. "Amazon reportedly scraps internal AI recruiting tool that was biased against women," The Verge 2018 — organizational governance-failure/contestation case leading to tool shutdown.
5. Begoli, Bhattacharya & Kusnezov (2019), "The need for uncertainty quantification in machine-assisted medical decision making," *Nat. Mach. Intel.* 1(1), 20-23 — uncertainty quantification for actionable decision support.

## 9. LIMITATIONS
1. Scoped to supervised AI/ML only — "we focus on the types of risks that closely impact... systems that are built with supervised AI/ML models." *(Sec.1, p.2)*
2. Excludes privacy/ethics — "risks pertaining to data privacy and ethical issues are not within the scope of this paper." *(Sec.1, p.2)*
3. No unified empirical benchmark test bed exists. *(Sec.3, p.8)*

## 10. BI LINK
"Business analytics" explicitly listed as an AI/ML application domain (Sec.1, p.1); venue itself is *Decision Support Systems*; "high-stakes decision settings" and "machine-assisted decision making" used throughout (Abstract p.1; Sec.1 p.2; Sec.2.2.3 p.7). "Business intelligence"/"BI"/"data warehousing" terms themselves absent.

## 11. WORKING-TIER RECEPTION
Documented absence, explicit. (a)-(e) all explicitly absent — no policy-dissemination, practice-gap, practitioner-attitude, feedback-channel, or edge-case-handling data; only a passing note that data bias is "often overlooked by many developers and researchers" (Sec.2.1.1, p.3), which is a technical observation, not empirical practitioner-reception evidence. Confirmed absence finding for the working-tier tally.

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
