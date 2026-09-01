# Thesis Agent Team & Workflow Plan

**Thesis:** Organizational Policy Development for Generative AI Integration in BI Workflows
**Author:** Liu Yu-Shu (Albert) — MSc Business Analytics, Aalto University
**Version:** v1, Sep 1, 2026
**Companion doc:** `Literature_Review_and_Research_Method_Plan.md` (timeline, clusters, method)

---

## 1. Design Principles

- **Fable is the planner and orchestrator.** The main Claude session (Fable) does chapter planning, task breakdown, quality gates, and all final editorial judgment. It delegates bulk work to sub-agents and NotebookLM, and never lets an agent's output reach a chapter draft without a verification pass.
- **NotebookLM is the source-grounded reading layer.** Every summary, quote, or claim about one of the 29 sources comes from NotebookLM queries against the uploaded PDFs — not from an LLM's memory. This is the main defense against hallucinated citations.
- **You stay the scholar.** Agents summarize, synthesize, and draft; you read the 5/5-priority papers yourself, approve every chapter, and mark sources as human-read (`/ars-mark-read`) so the pipeline knows which claims are verified.
- **Markdown first, LaTeX last.** All drafting happens in Markdown (project docs + GitHub repo). Conversion to LaTeX (Aalto template) happens once, in the Nov formatting phase, via `/ars-format-convert` / pandoc.

---

## 2. Agent Roster

| # | Role | Who / tool | What it does | When |
|---|------|-----------|--------------|------|
| 0 | **Orchestrator & planner** | **Fable** (main session) | Chapter-by-chapter planning (`/ars-plan`), task breakdown, dispatching agents, merging outputs, quality gate before anything is committed | Continuous |
| 1 | **Reading & summarization layer** | **NotebookLM** (via notebook MCP) | Holds all source PDFs; produces per-source structured summaries (WHY/HOW/WHAT), answers cross-source questions ("how do these 7 papers define AI governance?"), pulls exact quotes with source grounding | Per cluster, Sep 1–15 |
| 2 | **Gap-fill search agent** | general-purpose agent + WebSearch / arXiv lookup | Targeted searches for the known gaps (Sec. 2.5 of the plan): BI-specific governance, EU AI Act compliance, Nordic/Finnish context; returns candidate papers with relevance ratings for your approval | Sep 9–15 window |
| 3 | **Synthesis agent** | ARS `synthesis_agent` | Integrates NotebookLM cluster notes across sources: convergences, conflicts, and the research-gap map that becomes Chapter 7 (Synthesis) | After each cluster's notes exist |
| 4 | **Methodology architect** | ARS `research_architect_agent` | Sanity-checks the method chapter and helps derive the interview protocol from lit findings (IPR framework, Sec. 3.3) | Sep 2–8 window |
| 5 | **Writer / compiler** | ARS `report_compiler_agent` (or `/ars-lit-review` mode) | Turns synthesis notes into APA-7 chapter drafts in Markdown | Per chapter |
| 6 | **Reviewer panel** | `/ars-reviewer` | Simulated peer review (EIC + 3 reviewers + devil's advocate) on the full lit review draft before it goes to your supervisor | Sep 15 + Nov revision phase |
| 7 | **Citation QA** | `/ars-citation-check` | Verifies every in-text citation against the reference list and flags unverifiable claims | Before each supervisor handoff |

Agents 2–7 already exist (ARS plugin + built-in agents) — nothing needs to be built; this doc defines how they're sequenced.

---

## 3. NotebookLM Setup

**Prerequisite:** run `nlm login` in a terminal on your computer (the current NotebookLM login has expired). After that, Fable can drive NotebookLM directly from this session.

**Structure — one notebook, all clusters:** `MSc Thesis — AI Governance Literature` with all 29 sources (well under NotebookLM's source limit). One notebook lets cross-cluster questions work ("compare Cluster A definitions with Cluster E's BI framing"). Prefix source titles with their cluster letter (`[A] AMCIS 2025 — The Governance of Generative AI`) so query results are traceable.

**Standard queries per source** (Fable runs these, saves answers as Markdown notes in the repo):

1. WHY — research problem and motivation
2. HOW — method/design (esp. for Cluster D qualitative studies: sample size, interview approach — feeds your method chapter)
3. WHAT — key findings and framework/typology proposed
4. Definition extracted — how the paper defines AI governance / GenAI governance
5. Relevance hook — the one to two sentences of this paper that your thesis will actually cite, with exact quote

**Cross-cluster queries** (feed the synthesis agent): definitional convergence/divergence; what each cluster says about *policy development process* vs. outcomes; where BI/analytics contexts appear at all.

---

## 4. The Per-Cluster Pipeline (repeatable loop)

```
PDFs → NotebookLM notebook → per-source notes (WHY/HOW/WHAT/definition/quote)
     → you read the 5/5-priority papers yourself → /ars-mark-read
     → synthesis_agent: cluster memo (convergence, conflicts, gap contribution)
     → report_compiler_agent: chapter section draft (Markdown, APA 7)
     → Fable QA gate: every claim traced to a note; no orphan citations
     → your edit pass → commit to GitHub + update project doc
```

Once the loop runs for Clusters A+B, C–F reuse it unchanged. The reviewer panel (`/ars-reviewer`) and `/ars-citation-check` run once on the assembled full draft (Sep 15 target), not per section.

---

## 5. GitHub Repo Structure

Repo: `msc-thesis-ai-governance` (private). Proposed layout:

```
/README.md                  ← project overview + status
/planning/                  ← this doc + the lit review & method plan (synced from Claude project)
/literature/
  /notes/                   ← one .md per source (NotebookLM-derived, cluster-prefixed filenames)
  /cluster-memos/           ← synthesis memos A–F
  references.bib            ← BibTeX from day one (so LaTeX conversion is painless)
/chapters/                  ← ch1-introduction.md … ch-litreview sections, method chapter
/interviews/
  /protocol/                ← IPR-framework protocol drafts
  /transcripts/             ← ⚠ gitignored or anonymized only — consent/GDPR
/analysis/                  ← thematic coding artifacts (rolling coding from Sep 22)
/latex/                     ← Aalto template + converted output (Nov)
.gitignore                  ← transcripts, PDFs (copyright), scratch
```

Conventions: commit per work session with message `[cluster-A] draft definitions section`; the Claude project remains the planning/decision log, GitHub is the canonical home of content. **Interview transcripts and raw PDFs never go to GitHub** (privacy + copyright) — notes and drafts do.

Start `references.bib` now, not in November: each source gets a BibTeX key when its note file is created (e.g., `przegalinska2025`), and Markdown drafts cite with `[@przegalinska2025]` (pandoc syntax) so `md → LaTeX` conversion keeps citations intact automatically.

---

## 6. Mapping to the Timeline

| Window (from method plan) | Agent activity |
|---|---|
| **Sep 1–8** (Clusters A+B → C+D) | Set up NotebookLM notebook + repo; run reading layer on A+B; synthesis + draft A+B sections; `research_architect_agent` starts interview protocol from findings |
| **Sep 9–15** | Gap-fill search agent (BI, EU AI Act, Nordic); reading layer on C–F; assemble full lit review draft; `/ars-reviewer` + `/ars-citation-check` pass |
| **Sep 15 – Oct 15** (interviews) | Agents mostly idle on lit; Fable assists rolling thematic coding after each interview; monthly currency re-search (per plan Sec. 2.4) can run as a scheduled task |
| **Nov** | Writer/compiler for findings & discussion; reviewer panel on full draft; LaTeX conversion |
| **Dec 1–15** | `/ars-citation-check` final pass; formatting; submission |

---

## 7. What Fable Needs From You (before the loop can start)

1. **Run `nlm login`** on your computer to restore NotebookLM access.
2. **Tell me where the 29 PDFs are** — a folder on your computer (connect it via "Add folder" in the desktop app), Google Drive, or already uploaded to a NotebookLM notebook.
3. **GitHub**: repo name confirmation, and whether you'll create it or want the structure delivered as a zip to push yourself.
4. **The two .docx reference lists** (`Core_AI_Governance_Reference_List.docx`, `Interview_Design_Reference_List.docx`) — attach or put in the connected folder, so `references.bib` can be generated from them.
