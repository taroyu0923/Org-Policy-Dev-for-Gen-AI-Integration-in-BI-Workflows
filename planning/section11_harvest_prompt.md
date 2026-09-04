# §11 Working-Tier Reception — harvest pass

**Purpose:** append one new section (§11) to every compiled literature note, harvesting what each source says about how governance is *experienced by the people it lands on* — the receiving end, not the authoring end.
**Model:** Sonnet. **Created:** Sep 2, 2026. **Status:** not yet run.

## Why this exists

The v2.2 ten-question template was written for a top-down study. Three of its ten sections carry that framing (§5 CITABLE, §7 INTERVIEW VALUE, §8 SNOWBALL); the other seven are framing-neutral extraction and need no change. The thesis has since been reframed to the **analytical working tier** — no participant in the confirmed sample authored a GenAI policy — so the corpus was never systematically asked what it says about reception.

Rather than re-running ten questions across twenty notebooks, this pass adds **one** query and appends its answer as a new §11 to each existing note. §1–§10 are untouched.

**Nulls are the point.** Roughly eight sources will have real material; the rest will have none. "N of 20 sources theorise governance without describing how anyone below management experiences it" is a documented-absence claim of the same kind that §10 BI LINK produced (21/21 on the literal BI terms) — and it is only sayable if every source was asked. Do not skip notebooks you expect to come back empty.

## ⚠ Provenance note — read before running

MCP-driven queries do **not** persist to NotebookLM's visible chat history (confirmed limitation, Sep 2026). Albert's usual practice is to paste queries into the NotebookLM UI so the chat export carries the audit trail. **For this pass that is waived**, by his decision: the query is sent via MCP and the answer lands only in the local note.

Because the NotebookLM-side trail will not exist, **the repo must carry it instead**. Every §11 section written must open with the provenance block specified below. Without it this pass has no audit trail at all.

---

## The query

Send verbatim to each notebook, substituting the source filename.

```
Continuing with ONLY the source "<filename>", same location rules (section name + page number for every point):

11. WORKING-TIER RECEPTION — Based ONLY on this source: what does it say about how AI or generative-AI governance is experienced, interpreted, resisted, worked around, or ignored by the people who do the analytical and technical work — as distinct from how it is designed by executives or policy owners? Cover, where the source contains them:
(a) how policy actually reaches practitioners — training, documentation, tooling, informal channels;
(b) evidence of gaps between stated policy and actual practice;
(c) practitioner attitudes — compliance, scepticism, check-the-box behaviour, workarounds, shadow use;
(d) whether practitioners have any channel to influence or change policy, and whether it is used;
(e) what practitioners do when the policy does not cover their situation.
Quote any instruments, findings, or actual interview questions with their location.

If this source says nothing about the working tier's experience of governance, state that plainly and explicitly. A documented absence is a finding for this study, not a failed query — do not pad the answer with material about executive-level policy design to fill the gap.
```

**The final paragraph is load-bearing.** Without it the model will substitute top-down content and manufacture false positives, which would destroy the absence claim this pass exists to support.

## Procedure

1. `notebook_list` (and `collection_list`) to map notebooks to bib keys. Notebooks are named `[X#] AuthorYEAR — Short Title`.
2. For each of the **20 usable notes** in `literature/notes/` (all compiled notes except the excluded `D_mitchell2025_employee_experiences.md`), find its notebook and send the query above via `notebook_query`.
3. Append the answer to that note as a new `## 11. WORKING-TIER RECEPTION` section, placed after §10 and before the "Albert's Questions" section.
4. Open every §11 with this provenance block, filled in:

```markdown
## 11. WORKING-TIER RECEPTION
> *Harvested <DATE> via MCP `notebook_query` to notebook `<notebook_id>` ("<notebook name>"). Query: §11 as specified in `planning/section11_harvest_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*
```

5. Apply the **Unclear-point resolution rule (v2.3)**: any point that is confusing, or lacks a clear section+page location, gets one targeted re-query before the note is finalised; anything still ungrounded is marked `⚠ UNRESOLVED — not confirmed in source`, excluded from memos and drafts, and reported to Albert.
6. Where a source reports a genuine absence, write it explicitly and do not invent content:

```markdown
## 11. WORKING-TIER RECEPTION
> *(provenance block)*

**Documented absence.** This source describes governance design, standards and executive-level structures only; it contains no account of how practitioners encounter, interpret, or respond to governance. <One sentence on what it does cover instead, with location.>
```

7. Do **not** modify §1–§10 of any note. Do not recompile. Do not create notebooks.

## Reporting back to Albert

Produce a summary table: note, notebook, §11 outcome (`substantive` / `partial` / `documented absence`), and one line on what was found. Then state the headline count — *"X of 20 sources contain no account of the working tier's experience of governance"* — which is the sentence Chapter 2 will use.

Flag separately: any source that turned out to contain **reusable practitioner-facing interview questions or instruments**, since those feed the protocol directly.

## Expected yield (prediction, not instruction — record what you actually find)

Likely substantive: `stickystories2025` (Nahar — non-champions, check-the-box behaviour, engagement gap), `agenticaiperceptions2025` (Ackerman — practitioner perceptions, knowledge gaps), `lee2024questionbank` (Lee — L3 technical tier, role-specific knowledge silos), `responsibleaigovreview` (Papagiannidis — relational practices), `joshi2025resai` (Joshi — operational tier, Shadow AI), `batool2024aigov` and `batool2024rai` (Batool — team-level governance found in **zero** studies, which is itself receiving-end evidence), `weinberg2025faigmoe` (Weinberg — training, culture, adoption).

Likely absent: the policy-analysis and corporate-governance sources — `agarwal2025fivelayer`, `ferjani2025cogov`, `ozman2025platforms`, `taeihagh2025govgenai`, `luna2024paradigms`, `priyanshu2024claude`, `corpgovageai2025`, `aiincorpgov`, `aigovalgoacc2026`, `datagovstrategicdecision`, `ismail2025frameworks`, `ethicaltheoriesgovmodels2025`.

If the actual split differs sharply from this prediction, say so — it changes how the thesis is framed.

## What this pass decides

If §11 returns rich material across many sources, the "engagement gap" is a live literature this thesis joins, and it becomes context rather than headline. If it returns mostly absences, the gap is genuine and is a strong candidate for the thesis's central claim. **Do not pre-judge the answer; the count is the finding.**

---

## Copy-paste prompt for the Sonnet session

```
Read planning/section11_harvest_prompt.md, claude/LitReview_Process_v2.md and
claude/Pipeline_State.md in this project, then run the §11 Working-Tier Reception
harvest pass.

Setup: connect to my folder "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows".
NotebookLM is available via the notebook MCP; if auth is stale I'll run `nlm login`.

Run §11 against ALL 20 usable notes in literature/notes/ — every note except
D_mitchell2025_employee_experiences.md, which is excluded. Include the sources you
expect to return nothing: the absences are the point, and I need the count.

Send the query via MCP notebook_query (I accept that MCP queries don't persist to the
NotebookLM UI chat history for this pass). Append the answer to each note as a new
section 11, placed after section 10 and before "Albert's Questions", opening with the
provenance block from the prompt file. Do not touch sections 1-10 and do not recompile
any note.

Apply the Unclear-point resolution rule (v2.3): re-query once for any point lacking a
clear section+page location; mark anything still ungrounded as UNRESOLVED and tell me.

When done, give me the summary table, the headline count ("X of 20 sources contain no
account of the working tier's experience of governance"), and a separate list of any
sources containing reusable practitioner-facing interview questions or instruments.

Do not commit; I push to GitHub myself.
```
