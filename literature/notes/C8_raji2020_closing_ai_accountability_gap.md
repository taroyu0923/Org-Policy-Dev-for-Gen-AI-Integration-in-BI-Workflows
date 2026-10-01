# [C8] Raji, Smart, White, Mitchell, Gebru, Hutchinson, Smith-Loud, Theron & Barnes (2020) — Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing

**Bib key:** `raji2020closingaccgap`
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.1145/3351095.3372873 as printed.
**Cluster:** C — Corporate governance / algorithmic accountability
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill


> **PDF page check (Oct 1, 2026).** Checked against the PDF in `D:\Master\Thesis\Thesis Content`; printed pages. These override page numbers and quotes below. Log: `planning/s3_section11_spotcheck_2026-10-01.md` (or the session log named). §11 verdict changes, if any, wait for Albert's decision on the coding rule.
>
> Offset: FAT* '20 pp. 33–44; printed ≈ PDF page + 32 (check by eye; columns cross pages). The note's pages are article-relative. "box-ticking" p. 36. The worked example is **hypothetical** ("template model card", "hypothetical datasheet"); interviews/ethnography are prescribed audit steps. ⚠ §11(e) "practitioners default to optimizing isolated numerical metrics" over-reads a prescriptive remark — do not use (claims map K6 to be corrected). §11: proposed **documented absence**.

---

## 1. WHY
Deployed AI systems are audited externally only after harm occurs; internal teams lack structured pre-deployment methods to trace ethical failure modes. *Location: Abstract p.1; Sec.1 pp.1-2; Sec.2.3 p.2.*

## 2. HOW
Conceptual framework development + comparative qualitative review of safety-critical auditing practices (aerospace, medical devices, finance), validated via 2 hypothetical case studies (child-abuse screening tool; smile-detection photo booth using the CelebA 202,599-image dataset). *Location: Sec.1 p.2; Sec.3 pp.3-5; Sec.4 p.6.*

## 3. WHAT
- SMACTR framework — 5 stages: Scoping, Mapping, Artifact Collection, Testing, Reflection. *(Abstract p.1; Sec.4 p.6)*
- Cross-industry tool adaptation (checklists, traceability, FMEA, design controls, ADHF). *(Sec.3.1-3.2 pp.3-4; Sec.4.6.3 p.11)*
- Internal-external audit complementarity ("transparency trail"). *(Sec.2.4 pp.2-3; Sec.4.1 p.7)*
- Ethical governance vs. technical QA distinction. *(Sec.2 p.2)*
- Procedural justice for legitimizing hard deployment decisions. *(Sec.1 p.2; Sec.2.3 p.2; Sec.4.6 pp.11-12)*

## 4. DEFINITION
"we present internal algorithmic audits as a mechanism to check that the engineering processes involved in AI system creation and deployment meet declared ethical expectations and standards, such as organizational AI principles." *(Sec.1, p.2)*. Accountability: "the state of being responsible or answerable for a system, its behavior and its potential impacts" *(Sec.2, p.2)*.

## 5. CITABLE
Top-down framework-design side, but includes practitioner-translation claims.
- "the AI industry lacks proven methods to translate principles into practice, and AI principles have been criticized for being vague and providing little to no means of accountability." *(Sec.2.2, p.2)*
- "bottom-up decentralized decision making can lead to failures in complex sociotechnical systems. Each local decision may be correct in the limited context in which it was made, but can lead to problems when these decisions and organizational behaviors interact." *(Sec.4.3.2, p.8)*
- "because auditors are employees of the organization and communicate their findings primarily to an internal audience, there is opportunity to leverage these audit outcomes for recommendations of structural organizational changes..." *(Sec.2.4, p.3)*

## 6. AUTHORS/YEAR/VENUE
Inioluwa Deborah Raji, Andrew Smart, Rebecca N. White, Margaret Mitchell, Timnit Gebru, Ben Hutchinson, Jamila Smith-Loud, Daniel Theron, Parker Barnes. 2020. FAT* '20, Jan 27–30, 2020, Barcelona. ACM. DOI: 10.1145/3351095.3372873.

## 7. INTERVIEW VALUE
Normative design proposal, not empirical, but rich instruments/probes:
- **Policy Encounter & Interpretation:** avoid box-ticking — "It is good practice to avoid yes/no questions to reduce the risk that the checklist becomes a box-ticking activity, for example by asking designers and engineers to describe their processes for assessing ethical risk" (Sec.3.1.1, p.4); Datasheets-for-Datasets provenance questions (Sec.4.4.2, p.9).
- **Implementation & Change Mgmt:** advocates semi-structured interviews/ethnographic fieldwork to uncover audit workflows (Sec.4.3.2, p.8); FMEA gathering practitioner knowledge of foreseeable failures (Sec.3.1.3, p.5).
- **Organizational Adaptation Dynamics:** designer vs. user mental-model disconnect construct — "Large gaps between the intended and actual uses of algorithms have been found in contexts such as criminal justice and web journalism" (Sec.4.6.1, p.10).

## 8. SNOWBALL
1. Christin (2017), "Algorithms in practice: Comparing web journalism and criminal justice," *Big Data & Society* 4(2) (References p.11) — empirical sociology of practitioner algorithm negotiation/resistance.
2. Holstein, Vaughan, Daumé, Dudík & Wallach (2018), "Improving fairness in machine learning systems: What do industry practitioners need?" arXiv (References p.11) — direct investigation of practitioner needs/organizational hurdles.
3. Selbst, Boyd, Friedler, Venkatasubramanian & Vertesi (2019), "Fairness and abstraction in sociotechnical systems," FAT* (References p.12) — abstraction errors by technical workers isolated from deployment context.
4. Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji & Gebru (2019), "Model cards for model reporting," FAT* (References p.12) — practitioner-facing documentation instrument.
5. Sculley, Holt, Golovin, Davydov, Phillips, Ebner, Chaudhary & Young (2014), "Machine learning: The high interest credit card of technical debt" (References p.12) — technical debt/entanglement experienced by engineers maintaining production ML.

## 9. LIMITATIONS
1. Auditor bias/lack of full independence — "Internal auditors necessarily share an organizational interest with the target of the audit" *(Sec.5, p.10)*.
2. Audits are not monolithic/objective, risk becoming "reputation management" *(Sec.5, pp.10-11)*.
3. Insufficient without external regulatory checks *(Sec.5, p.11)*.
4. Audit process "necessarily boring, slow, meticulous and methodical—antithetical to the typical rapid development pace for AI technology" *(Sec.1, p.1)*.
5. Lacks standardized model-development template/process guidelines *(Sec.3.4, p.6)*.
6. Scope excludes criteria for what to audit and why *(Sec.4.1, pp.6-7)*.

## 10. BI LINK
"Business intelligence"/"BI"/"data warehousing"/"analytics" as an enterprise domain all absent. Decision-support present in general terms: "...in addition to providing decision support to design mitigations..." (Sec.1, p.1); one reference title mentions "decision making" (References p.11).

## 11. WORKING-TIER RECEPTION
> **§11 verdict under coding rule R1 (Oct 1, 2026, Albert approved; PDF-checked, `planning/s3_section11_spotcheck_2026-10-01.md`):** **documented absence**. Normative framework with a hypothetical worked example.

Normative framework, no empirical field data, but substantive conceptual coverage. (a) Policy reaches technical teams via structured engineering artifacts — PRDs, Model Cards, Datasheets, Design Checklists (Sec.4.2 p.7; Sec.4.4 pp.8-9); AI principles are criticized as "vague and providing little to no means of accountability" (Sec.2.2, pp.2-3). (b) Gaps: designer/user mental-model disconnects (Sec.4.6.1, p.10); bottom-up decentralized local decisions interacting to cause system-level failures (Sec.4.3.2, p.8). (c) Attitudes: explicit box-ticking risk named (Sec.3.1.1, p.4); audit skepticism/dismissal risk (Sec.2.3, p.3); no empirical data on workarounds/shadow use. (d) Engineering teams co-develop mitigation plans and participate in ethnographic interviews within the proposed framework (Sec.4.6, p.9; Sec.4.3.2, p.8) — but no empirical evidence these channels exist in current practice. (e) Practitioners default to optimizing isolated numerical metrics, obscuring fairness/social risk when guidance is silent (Sec.4.3.2, p.8); auditors retroactively co-construct missing documentation with engineers (Sec.3.4, p.6).

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
