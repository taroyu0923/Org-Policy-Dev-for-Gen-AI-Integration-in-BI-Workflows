entries = {
"B_joshi2025_responsible_genai_governance.md": {
"id": "31d0ce0d-17be-440a-bcb5-4c4dfd652dda",
"name": "[B4] Joshi2025 — Responsible Governance of GenAI",
"body": """**Substantive.** This white paper (literature review + industry roundtable) is prescriptive rather than empirical, but describes working-tier reception in more operational detail than any other Cluster A/B source.

(a) **Policy reach:** Practitioners sit at the "Operational Level" (functional managers, data scientists, developers), executing governance set at Strategic/Tactical levels (Section IV.A, Levels of Execution). Policy reaches them via "GenAI and Data Literacy/Education" training designed to prevent misuse such as "uploading confidential content into GenAI tools like ChatGPT" (Section IV.D.1, Core Foundational Pillars); continuous SOP training (Section IV.D.2); and role-specific "Role-Based Training Modules... tailored to technical staff" covering ethics, compliance and technical risk (Section V.C, Step 3: Training and Up-skilling). Governance is also embedded directly in workflow tooling — risk matrices, decision-support templates, lifecycle checkpoints, and "Sandbox Testing Environments" for controlled experimentation (Section II.B.2; Section IV.C).

(b) **Policy–practice gap:** The paper names "Shadow AI" as its central gap — "the use of unauthorized AI models outside organizational oversight," where "employees or teams may develop and deploy AI tools independently, bypassing any established governance controls" (Section I.C.2, Key Governance Challenges). It notes employees "frequently use external tools for sensitive tasks like writing code or processing proprietary data" (Section IV.D.1) and states plainly that "many organizations struggle with the practical implementation of GenAI governance because existing frameworks lack industry-specific guidance" (Section II.B.2).

(c) **Practitioner attitudes:** The framework acknowledges a risk that compliance is experienced as a "burdensome process" if not smoothly integrated (Section II.B.2), and that teams bypass formal controls "when formal channels are slow, rigid, or absent" (Section I.C.2; Section III.E, Vendor and Third-Party Management). No empirical skepticism/compliance data is presented — these are the paper's own stated risks, not observed findings.

(d) **Feedback channels:** The paper prescribes a "Bidirectional Approach: Top-Down and Bottom-Up Governance" (Section IV.C) with "Continuous Feedback Loops" (regular meetings between technical teams and executive governance committees) and sandbox environments feeding findings back to strategy (Section IV.C), plus a stated aim to "empower individuals to report concerns or initiate changes themselves" (Section IV.D.2). These are recommended structural channels; the source gives no evidence of whether or how often they are actually used.

(e) **Uncovered situations:** The source implies practitioners resort to external, unauthorized GenAI tools when internal tooling does not meet an immediate need (Section IV.D.1) — the "Shadow AI" behaviour again — and prescribes internal sandbox environments as the intended alternative."""
},
"B_lee2024_rai_question_bank.md": {
"id": "8372f623-a93c-4a10-81ad-90dd28af73af",
"name": "[B6] Lee2024 — Responsible AI Question Bank",
"body": """**Substantive.** This source reports an actual empirical case study (8 scientific research projects, PR1–PR8; two rounds of 1.5-hour structured interviews, 2023) using the RAI Question Bank as both instrument and governance-translation tool — the richest working-tier material found in Clusters A/B.

(a) **Policy reach:** The RAI Question Bank operationalizes regulation/standards (EU AI Act, ISO/IEC 42001:2023) into a tiered instrument. Level 3 questions specifically target "practitioners who require a detailed understanding of the technical and operational aspects of AI risk assessment," e.g. "Do you research and try to use the simplest and most interpretable model possible for the AI system?" (question-levels section). In practice, governance reached practitioners via a risk-register template and structured interviews (Section 3.3, Case Study).

(b) **Policy–practice gap:** Cites an industry finding that only 10% of surveyed companies have publicly announced RAI policies. The case study itself found "Accountability emerges as the principle with the highest combined medium to high risk... mainly to do with missing a proper responsible distribution documentation and lack of traceability within projects," and significant transparency gaps from "insufficient clarity in explaining AI outcomes" (case-study results/discussion section). One project lead "had not considered the risks associated with third-party university agreements on intellectual property ownership... until prompted by the RAI Question Bank questions" (case-study discussion).

(c) **Practitioner attitudes:** The authors explicitly flag a "checkbox mentality" risk from yes/no question formats if not paired with evidence requirements (discussion of question design). Practitioners pushed back on the tool directly: "the number of questions in the RAI Question Bank sometimes seemed excessive relative to the level of completeness needed for the assessment," and argued a full questionnaire suits only mission-critical systems, not lower-risk projects (feedback-and-improvement section). No workaround/shadow-use behaviour is reported.

(d) **Feedback channels — actually used:** Unlike other Cluster A/B sources, this is a channel practitioners visibly used, not just a design proposal. Practitioner feedback from the case study directly reshaped the instrument: questions were remapped to specific lifecycle stages (planning through deployment) so only relevant items are asked (Section on stage mapping); the question bank was restructured to add principle-level questions and rewrite technical terms into more accessible language following a second case study (ESG-AI investor framework). This is project-level co-design of a research instrument, not evidence of a standing corporate channel to change organizational policy.

(e) **Uncovered situations:** Early-stage projects lacked the performance data needed to answer questions about system accuracy/reliability (discussion of practical challenges). The source also flags that practitioners in typical commercial/open-source settings are often siloed to role-specific knowledge, unlike the flat-hierarchy research teams in this case study who could answer across all three question levels — the tool mitigates this by filtering questions by development stage and role (discussion of practical challenges)."""
},
}

for fname, info in entries.items():
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    marker = "\n---\n## Albert's Questions"
    if marker not in content:
        print(f"MARKER NOT FOUND: {fname}")
        continue
    section = f"""

## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `{info['id']}` ("{info['name']}"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

{info['body']}
"""
    new_content = content.replace(marker, section + "\n---\n## Albert's Questions", 1)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK: {fname}")
