import re, sys

NOTES_DIR = "."

entries = {
"A_agarwal2025_five_layer_framework.md": {
"id": "cb98c7ce-000d-4c8f-a30a-87c9709502e3",
"name": "[A6] Agarwal2025 — Five-Layer AI Governance Framework",
"body": """**Documented absence.** This source is a conceptual/policy-design proposal (a five-layer AI governance framework) validated by two case studies; it contains no empirical data, interview material, or findings on how practitioners experience governance. It treats developers only as abstract stakeholders: "developers often perform self-assessments, these lack independent validation" (Section 4.5, p. 8); SME "accessible training initiatives" appear only as a forward-looking policy recommendation, not observed practice (Section 6.2, p. 11). No practitioner attitudes, workarounds, feedback channels, or gap-handling behaviour are described anywhere in the text."""
},
"A_batool2024_ai_governance_slr.md": {
"id": "15a35a40-81af-49cb-b56f-aaf7553bf0ab",
"name": "[A1] Batool2024 — AI Governance SLR",
"body": """**Documented absence.** This SLR structurally defines "Operational AI practitioners" only as an object of oversight under its "who is being governed" 4W1H category (Section 4.1, p. 9), classified at "Team level" governance with examples such as faculty staff, IT firm managers, and healthcare providers governed by administrators/committees (Section 4.1.1, p. 10–11, Table 2). It contains no data on how these practitioners actually receive, interpret, resist, or work around governance — the review's own scope is limited to who governs whom, not how it is experienced."""
},
"A_batool2024_responsible_ai_governance_slr.md": {
"id": "35b3a3f4-287b-4a8d-b319-6f5f72c3d868",
"name": "[A4] Batool2024 — Responsible AI Governance SLR",
"body": """**Documented absence.** This SLR of 61 papers explicitly identifies the working tier as a gap in the literature itself, rather than reporting on it: "not a single study out of 61 has mentioned the human pillar to be considered to be governed" (Section 3.1.1). It defines "operational AI practitioners" theoretically as those doing "day-to-day technical implementation" (Section 3.1) and concludes the field lacks human-centricity (Section 4, RQ3: Limitations and Challenges), but supplies no practitioner-level findings, instruments, or interview material of its own."""
},
"A_ferjani2025_navigating_responsible_ai.md": {
"id": "05a5b20a-24d0-4fdc-856e-7f6f26b36432",
"name": "[A5] Ferjani2025 — Navigating Responsible AI / Co-Governance",
"body": """**Documented absence.** This macro-level systematic review (75 studies, "Governance Galaxy" framework, projecting scenarios to 2035) discusses an "implementation gap" and "disconnect between ethical frameworks and operational practices" only in structural terms — e.g. proposing "governance boards with technical representation" and "ethics-engineering collaboration processes" as design recommendations (Section on operationalizing the framework). It contains no empirical account of how technical staff actually encounter, interpret, or resist governance, and no practitioner-facing instruments or interview questions."""
},
"A_ismail2025_ethical_governance_frameworks.md": {
"id": "bcd97ea1-6d26-4e3d-994a-ba1db179122c",
"name": "[A3] Ismail2025 — Ethical & Governance Frameworks SLR",
"body": """**Documented absence.** This SLR covers macro-level governmental and corporate frameworks — e.g. NTT DATA's three-tier model including "AI literacy training to foster an ethics culture" (Section 3.4, p. 126–127) and the EU AI Act's conformity-assessment mandates for developers (Section 4.1, p. 127) — but only as structural design features, never as something practitioners are shown experiencing. The only ground-level attitudinal material in the source concerns university students, not professional practitioners: Barus et al.'s study on student views of GenAI regulation, where "students demanded models of co-governance" (Section 4.4, p. 129). No professional-practitioner reception, workaround, or feedback-channel evidence is present."""
},
}

for fname, info in entries.items():
    path = fname
    with open(path, "r", encoding="utf-8") as f:
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
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK: {fname}")
