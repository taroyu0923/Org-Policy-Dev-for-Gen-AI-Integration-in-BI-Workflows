# NotebookLM Query Template v2.4 — COMPLETE STANDALONE TEMPLATE

**Date:** Sep 4, 2026 | **Supersedes:** the v2.2 template in `claude/LitReview_Process_v2.md`
**Applies to:** every reference processed from now on — Cluster F, S3 gap-fill targets, snowball pulls, any cluster extension.

> **This file is self-contained.** Earlier revisions of it listed only the sections that changed (§5, §7, §8, §11, §12), which meant a session reading it alone did not have the wording for §1–§4, §6, §9 and §10. All twelve sections are now written out in full. Run from this file; do not reconstruct from v2.2.

---

## Which variant to run

| Source type | Variant | Query 2 ends with |
|---|---|---|
| Governance / organizational literature (Clusters A–F) | **v2.4** | §11 WORKING-TIER RECEPTION |
| Interview-methodology and instrument-design sources (Interview_I*) | **v2.4-M** | §12 PROTOCOL CRAFT (**§11 is not run**) |

**Why the split.** §11 produced a corpus-level statistic — *14 of 20 governance sources contain no account of how anyone below management experiences governance*. That number is only meaningful because those twenty were selected as the governance literature. Running §11 on methodology sources corrupts the denominator twice over: method-craft papers return false nulls (they were never about governance), and empirical practitioner studies return guaranteed positives (they were chosen for exactly that content). **The §11 denominator stays at the governance corpus.**

---

## Query 1 — core analysis (§1–§6)

> Analyze ONLY the source "<filename>". Be concise; keep quoted passages short. For EVERY point, statement, and quote, include its location in the original paper (section name + page number). Provide:
>
> 1. **WHY** — research problem and motivation (2–3 sentences, with location).
> 2. **HOW** — method/design: type of study, data, sample/corpus size, databases, time span (with locations).
> 3. **WHAT** — key findings, frameworks, or typologies proposed (one line each, each with location).
> 4. **DEFINITION** — how the paper defines its core governance construct (exact quote + section + page).
> 5. **CITABLE** — the 2–3 most citable claims for a thesis on how organizational generative-AI policy is **encountered, interpreted, enacted and adapted by the people who produce analytical and reporting outputs**, and whether their adaptation feeds back into the policy (exact quotes + section + page). Where the source only speaks to policy design from the executive or standards-setting side, say so and give the most citable claim it does offer.
> 6. **AUTHORS/YEAR/VENUE** — exactly as printed on the paper, including DOI if printed.
>
> 完成以上英文版本後，請另外提供一份簡短的繁體中文（台灣用語）摘要版本，濃縮涵蓋上述六點重點，不需逐字翻譯，但關鍵引文與頁碼位置仍需保留。

⚠ **§6 output is a claim, never verified metadata.** Check it against the publisher record or arXiv before it reaches `references.bib`. See the metadata-fidelity warning in `claude/LitReview_Process_v2.md` — this rule exists because the pipeline fabricated an author affiliation twice for one source, which is now excluded.

## Query 2 — evaluation & harvesting (§7–§10, then §11 or §12)

> Continuing with ONLY the source "<filename>", same location rules (section name + page for every point):
>
> 7. **INTERVIEW VALUE** — Based ONLY on this source: which findings, constructs, instruments, or actual questions could inform a semi-structured interview study on how organizational generative-AI policy is encountered and enacted in business (especially BI) settings? Map each item to one of these three phases: **Policy Encounter & Interpretation** / **Implementation & Change Management** / **Organizational Adaptation Dynamics**. Where the paper itself contains interview questions, assessment criteria, or instruments, quote them with location. If this source offers nothing for interview design, state that plainly.
> 8. **SNOWBALL** — List up to 5 references cited in this paper that appear most relevant to **how organizational AI/GenAI governance is experienced, enacted or contested by practitioners** in analytical, reporting or BI work — and, secondarily, to organizational governance development in those contexts. Give each citation exactly as printed in the reference list (with its location) plus one line on why it matters for this thesis.
> 9. **LIMITATIONS** — the limitations the paper states about itself (with location). Do not invent limitations the paper does not acknowledge.
> 10. **BI LINK** — does this paper mention business intelligence, analytics, data warehousing, or decision-support contexts anywhere? Quote each mention with location, or state plainly that such contexts are absent.

Then **§11** (governance sources) or **§12** (methodology sources):

> 11. **WORKING-TIER RECEPTION** — Based ONLY on this source: what does it say about how AI or generative-AI governance is *experienced, interpreted, resisted, worked around, or ignored* by the people who do the analytical and technical work — as distinct from how it is designed by executives or policy owners? Cover, where the source contains them: (a) how policy actually reaches practitioners — training, documentation, tooling, informal channels; (b) evidence of gaps between stated policy and actual practice; (c) practitioner attitudes — compliance, scepticism, check-the-box behaviour, workarounds, shadow use; (d) whether practitioners have any channel to influence or change policy, and whether it is used; (e) what practitioners do when the policy does not cover their situation. Quote any instruments, findings, or actual interview questions with their location.
>
> If this source says nothing about the working tier's experience of governance, state that plainly and explicitly. A documented absence is a finding for this study, not a failed query — do not pad the answer with material about executive-level policy design to fill the gap.

> 12. **PROTOCOL CRAFT** — Based ONLY on this source: what does it document about HOW the study was actually carried out, as opposed to what it asked or what it found? Do not repeat the study design, sample size or self-stated limitations already covered elsewhere. Cover, where the source contains them: (a) recruitment and access; (b) sampling logic and saturation; (c) protocol construction, piloting, question sequencing, probe technique, wording rules; (d) conduct — length, mode, rounds, recording, language(s) and any translation procedure; (e) consent and confidentiality, including employer anonymity and ethics route; (f) analysis procedure — coding approach, who coded, software, reliability measures; (g) trustworthiness — member checking, triangulation, audit trail, reflexivity; (h) transferable method lessons.
>
> Quote procedures verbatim with location wherever the wording matters. If the source does not document a given item, say so for that item rather than inferring. If the source is a methodological or instrument-design paper rather than an empirical study, answer for what it PRESCRIBES rather than what it did, and say which.

Full §11 and §12 procedure, provenance requirements and agent prompts: `section11_harvest_prompt.md`, `section12_protocol_craft_prompt.md`.

---

## What changed from v2.2, and why

The thesis was reframed to the **analytical working tier** — no participant in the confirmed sample authored a GenAI policy — so the study is an account of how policy is encountered, interpreted and adapted by the people who do analytical work, and whether that adaptation feeds back upward.

Auditing the original ten sections against that reframing:

| Section | Status |
|---|---|
| §1 WHY, §2 HOW, §3 WHAT, §4 DEFINITION, §6 AUTHORS, §9 LIMITATIONS, §10 BI LINK | **Unchanged** — framing-neutral extraction |
| §5 CITABLE | **Rescoped** from "how organizations develop and evolve" to how policy is encountered, interpreted, enacted and adapted by practitioners |
| §7 INTERVIEW VALUE | **Phase 1 renamed** — "Policy Framework Development" → **"Policy Encounter & Interpretation"**. Phases 2 and 3 unchanged |
| §8 SNOWBALL | **Rescoped** to practitioner-side relevance first, governance development second |
| §11 WORKING-TIER RECEPTION | **NEW** (v2.4) — governance sources only |
| §12 PROTOCOL CRAFT | **NEW** (v2.4-M) — methodology sources only |

⚠ **Known consequence.** The v2.2 §8 wording steered the snowball harvest toward top-down sources across all 21 existing notes. Expect those §8 lists to under-represent practitioner-side literature; the S3 gap-fill partially corrects this, Rakova et al. (2021) in particular.

⚠ **Mapping note for existing notes.** The 21 governance notes tag §7 material under the old Phase 1 name. That content is not wrong — constructs such as Lee's L3 technical-practitioner tier or Joshi's Shadow AI are receiving-end material under a top-down heading. Read those entries as *encounter* material; re-file genuinely authoring-side content into chapter background.

## Downstream routing

§7 → interview-protocol derivation, tagged by phase. §8 → gap-fill agent for DOI verification and Albert's keep/reject call, and into `search_log.md` as snowball entries. §9 → critique sentences in each chapter section. §10 → the Chapter 7 gap argument. §11 → the working-tier reception argument and the engagement-gap analysis; **absence counts are evidence in their own right and are tallied across the governance corpus.** §12 → Chapter 3 method precedent; the (a)–(h) coverage table shows which methodological choices have support in the literature and which must be defended unsupported.
