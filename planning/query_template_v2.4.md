# NotebookLM Query Template v2.4 — amendments to v2.2

**Date:** Sep 2, 2026 | **Supersedes:** the v2.2 template in `claude/LitReview_Process_v2.md` §"Standard query template"
**Applies to:** all references processed from now on — Cluster F, the S3 gap-fill targets, and any new source. Existing notes are amended by the §11 harvest pass only (see `section11_harvest_prompt.md`).

## Why v2.4

v2.2 was written for a top-down study of how organizations *develop* GenAI policy. The thesis has been reframed to the **analytical working tier**: the confirmed sample contains no policy author, so the study is an account of how policy is *encountered, interpreted and adapted* by the people who do the analytical work, and whether that adaptation feeds back upward.

Auditing the ten sections against that reframing: **seven are framing-neutral** (§1 WHY, §2 HOW, §3 WHAT, §4 DEFINITION, §6 AUTHORS, §9 LIMITATIONS, §10 BI LINK) and are unchanged. Three carry the top-down framing and are revised below, plus one new section.

---

## §5 CITABLE — revised scope

Replace the scope clause. Was:

> the 2–3 most citable claims for a thesis on how organizations **develop and evolve** generative-AI policy/governance frameworks in business-intelligence contexts

Now:

> 5. CITABLE — the 2–3 most citable claims for a thesis on how organizational generative-AI policy is **encountered, interpreted, enacted and adapted by the people who produce analytical and reporting outputs**, and whether their adaptation feeds back into the policy (exact quotes + section + page). Where the source only speaks to policy design from the executive or standards-setting side, say so and give the most citable claim it does offer.

## §7 INTERVIEW VALUE — revised phase 1

Phase 1 is renamed. Phases 2 and 3 keep their labels; they already work from the receiving end.

| Was | Now |
|---|---|
| Policy Framework Development | **Policy Encounter & Interpretation** |
| Implementation & Change Management | Implementation & Change Management *(unchanged)* |
| Organizational Adaptation Dynamics | Organizational Adaptation Dynamics *(unchanged)* |

**Phase 1 now means:** how policy arrived at the working tier, through what channel, how it was learned, what it was understood to require, and what it left undefined — not how it was authored.

> ⚠ **Mapping note for the 21 existing notes.** Their §7 content is labelled "Policy Framework Development" under the old, authoring-side meaning. That content is not wrong — constructs such as Lee's L3 technical-practitioner tier or Joshi's Shadow AI are receiving-end material sitting under a top-down heading. When drafting, read those Phase 1 entries as *encounter* material and re-file anything that is genuinely authoring-side into chapter background rather than the protocol.

## §8 SNOWBALL — revised relevance filter

Was: *"references … most relevant to organizational GenAI policy/governance development in BI contexts."*

Now:

> 8. SNOWBALL — list up to 5 references cited in this paper that appear most relevant to **how organizational AI/GenAI governance is experienced, enacted or contested by practitioners** in analytical, reporting or BI work — and, secondarily, to organizational governance development in those contexts. Give each citation exactly as printed in the reference list (with its location) plus one line on why it matters for this thesis.

> The v2.2 wording has been steering the snowball harvest toward top-down sources across 21 notes. The S3 gap-fill list partially corrects this (Rakova 2021 in particular), but expect the existing §8 lists to under-represent practitioner-side literature.

## §11 WORKING-TIER RECEPTION — new, run in Query 2

Full wording, procedure and provenance requirements: `planning/section11_harvest_prompt.md`. In the standard run for new references it is appended to Query 2, after §10.

Key rule, repeated here because it is easy to lose: **if a source says nothing about the working tier, the answer must say so plainly.** Documented absences aggregate into a corpus-level claim, in the same way §10 produced the 21/21 finding on literal BI terms. An answer padded with executive-level material to avoid an empty response destroys that claim.

---

## Query structure under v2.4

**Query 1 — core analysis:** §1–§6 (§5 revised) + zh-TW summary. Unchanged otherwise.
**Query 2 — evaluation & harvesting:** §7 (Phase 1 renamed), §8 (revised), §9, §10, **§11 (new)**.

## Downstream routing (unchanged except §11)

§7 → interview-protocol derivation, tagged by phase. §8 → gap-fill agent for DOI verification and Albert's keep/reject call, and into `search_log.md` as snowball entries. §9 → critique sentences in each chapter section. §10 → the Chapter 7 gap argument. **§11 → the working-tier reception argument and the engagement-gap analysis; its absence counts are evidence in their own right and are tallied across the corpus.**
