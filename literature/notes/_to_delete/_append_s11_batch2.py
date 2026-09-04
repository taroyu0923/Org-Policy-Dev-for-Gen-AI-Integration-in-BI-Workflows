entries = {
"A_ozman2025_ai_governance_platforms.md": {
"id": "dbb27525-4b97-485b-a7b6-ff1a68d3d4eb",
"name": "[A7] Ozman2025 — AI Governance Platforms SLR",
"body": """**Documented absence.** This SLR of AI governance platform architectures contains no empirical or qualitative material on practitioner reception. The only near-adjacent findings are structural: a cited empirical study calls for "increased training in AI governance for healthcare professionals to foster better AI adoption" (Appendix 1 Summary Table, p. 89), and the review notes "resistance from stakeholders" only as a generalized organizational barrier to platform adoption, not a practitioner-level behaviour (Section 5, Discussion, p. 82)."""
},
"B_luna2024_navigating_governance_paradigms.md": {
"id": "71b7253a-1fa7-4e74-9de1-044e99b0fc6f",
"name": "[B3] Luna2024 — Navigating Governance Paradigms",
"body": """**Documented absence.** This cross-regional comparative study (H-GenAIGF framework) operates strictly at the macro (country-level regulation) and corporate-public (ChatGPT compliance) levels; it contains no internal organizational or practitioner-experience data. The only developer-adjacent mentions are conceptual: standards should "spread a culture of safety and responsibility among AI developers" (Related Work / Academic Research for Governance, p. 2), and "many developers, AI providers and/or end users may find navigating the convoluted nature of governance approaches burdensome" (H-GenAIGF introduction, p. 4). No practitioner attitudes, workaround behaviour, or feedback channels are documented."""
},
"B_priyanshu2024_claude_governance.md": {
"id": "38493d87-2ef0-4533-9904-abd4d8c07a78",
"name": "[B7] Priyanshu2024 — Claude Governance Analysis",
"body": """**Documented absence.** This policy analysis of Anthropic's Claude against NIST AI RMF and the EU AI Act evaluates corporate-level policy design only; it contains no data on how technical staff experience or respond to governance. It cites the wider literature's own acknowledgment of "limited understanding of AI governance implementation... and insufficient operationalization of processes" (Section 3, Literature Review) and recommends that risk-metric evaluation involve "internal experts who did not serve as front-line developers for the system" (Section 6.4, NIST "MEASURE") — a policy design recommendation, not an observation of practitioner behaviour."""
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
