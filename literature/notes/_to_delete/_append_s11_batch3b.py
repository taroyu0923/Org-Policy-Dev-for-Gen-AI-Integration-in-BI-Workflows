entries = {
"C_ganesh2025_corporate_governance_ai.md": {
"id": "97f0637f-429f-4a96-a4ee-a43904bf4dcd",
"name": "[C1] Ganesh2025 — Corporate Governance in the Age of AI",
"body": """**Documented absence.** This conceptual/prescriptive paper addresses governance from an executive/board perspective. It recommends internal training and quarterly "feedback sessions" for employees (Section 6, Table 4, p. 1145) and a "Shared Accountability Model" mapping developers to algorithm design (Section 3, Diagram 1, p. 1143), but reports no empirical data on whether these mechanisms function, and no practitioner attitudes, workarounds, or gap-handling behaviour — these are prescribed structures, not observations."""
},
"C_judijanto2026_algorithmic_accountability.md": {
"id": "b2aae7e7-e968-416e-bf2d-02927da5e192",
"name": "[C3] Judijanto2026 — AI-Governance & Algorithmic Accountability",
"body": """**Documented absence.** This is a normative legal literature review; it contains no empirical or organizational data on practitioner experience. Its closest developer-related content concerns technical opacity as an inherent property of "black-box" systems — decision logic is "difficult to trace, even for their developers" (Section: The Challenge of Algorithmic Transparency in Black-Box Systems, p. 14/16) — and a legal-liability discussion assigning "proportional" responsibility to developers, users, and policymakers (Section: Legal Liability for Autonomous Decisions, p. 21-22). Neither concerns how governance is actually received or acted on by practitioners."""
},
"C_ustahaliloglu2025_ai_corporate_governance.md": {
"id": "59baf06b-c124-410b-a6f8-3c6a2b43d5e0",
"name": "[C2] Ustahaliloglu2025 — AI in Corporate Governance",
"body": """**Documented absence.** This qualitative document-analysis study addresses AI governance from legal, board, and shareholder perspectives. It recommends that "businesses should fund ongoing AI ethics training for staff members who participate in decision-making" (Section 6.2, p. 131) and notes generalized organizational "skepticism over its maturity and actual application" (Section 1, p. 123-124), but neither is practitioner-level empirical evidence — no interviews, attitudes, workarounds, or feedback-channel use are documented anywhere in the source."""
},
}

for fname, info in entries.items():
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    marker = "\n## Albert's Questions"
    if marker not in content:
        print(f"MARKER NOT FOUND: {fname}")
        continue
    section = f"""

## 11. WORKING-TIER RECEPTION
> *Harvested 2026-09-04 via MCP `notebook_query` to notebook `{info['id']}` ("{info['name']}"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*

{info['body']}
"""
    new_content = content.replace(marker, section + "\n## Albert's Questions", 1)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK: {fname}")
