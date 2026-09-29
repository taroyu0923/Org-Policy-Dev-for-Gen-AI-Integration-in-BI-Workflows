# Structure & Interview-Framework Discussion — Decision Log

**Date:** Sep 11, 2026 | **Session:** Opus, plan mode (Socratic) | **Companion:** `s3_postcheck_2026-09-11.md`
**Status:** in progress — RQ not yet written. Entries are Albert's own positions unless marked *(Claude flag)*.

---

## Decided

| # | Decision | Consequence |
|---|---|---|
| D1 | **Protagonist = the analyst / individual contributor**, not the policy | Current title no longer fits; Section B (incident) and C–D carry findings; E becomes one possible ending, not the central test |
| D2 | **Title will change** | New title waits on the RQ |
| D3 | **Primary: governance seen from below (all 14). Secondary: whether/how governance moves upward — open question, null allowed** | Secondary is asked in every case (E3), not only at Shopee; phrased "whether, and through what routes" |
| D4 | **Shopee is the depth case for evolution**, but its structure is a finding, not a lens | Do not code other cases with Shopee categories (local screening / regional escalation / rulings); ask neutrally elsewhere ("When unsure, who decides?") |
| D5 | **Smartly contributes** external (EU) compliance as rule source + broader roles (DE, EM) | *(Claude flag)* Jurisdiction and role type confounded; name in Ch.3; breadth cases (Nordea = EU + analyst; Toyota/Delivery Hero = TW + analyst) partly separate them |
| D6 | **#13 Amazon: Amazon-only case**, breadth, operational, tenure floor (at Amazon 2025–26) | Past employers (Shopee, Accenture, Klook) only as comparison background; any Shopee detail volunteered is not used in Depth A. Confirm current role meets inclusion criterion |
| D7 | **Ethics: supervisor confirmed no ethical review required** | Recruitment under way. Before first interview: consent form + **privacy notice (still outstanding)**. Fill `ethics_determination_note.md` §5 (date, who, evidence) |
| D8 | **No unofficial testing interviews with Shopee #1–4** | Allowed: feasibility question (can you discuss the 2023 policy / Q4 2024 rollout; is there a document?) and a dry run with a non-participant |

## Case facts supplied by Albert (expected, not yet interview evidence)

- Shopee timeline: pre-AI work (2018) → **first GenAI policy 2023** (restricting company data in AI tools) → **AI tool integrated into process Q4 2024**. Intermediate rule changes inferred, not known.
- Shopee local BI is **first stop for data requests**; would check against the 2023 rule, refuse or modify requests. **Final decision: Regional BI** (sometimes local CEO). Local BI = first screen, not final gatekeeper.
- **No participant sits in Regional BI.** What comes back depends on impact; usually Y/N or explanation.
- Data platform admins/developers likely receive policy information earlier — not in sample (G2 route only).

## Design changes to make before the pilot

1. **B3 probe** (ruling → working rule): "Did you have to ask Regional again the next time, or did you already know?" — add to protocol + wording card.
2. **Escalation probe** in B/E: what went up, what came back (Y/N / explanation / rule / nothing).
3. Add **#13** to the tenure-floor note (protocol §11 item 2b).
4. **Limitations:** view from below — no decision-maker interviewed at Shopee; evolution reconstructed from what came back down.
5. **Chapter 2 candidate thread:** intermediaries in governance — A10 Birkstedt ("little discussion of [analytics translators'] roles in AIG", §5.1.2 p.155); D6 Lu champion conduit (prescriptive); D7 Rakova workshop channels between levels (§5.0.3 p.7:17).

## RQ drafts

**v0**
- Main: What is individual contributors' reflection on AI governance framework change?
- SQ1: Is current BI workflow blocked or limited-implemented due to the company's AI governance framework?
- SQ2: Does any individual contributor's opinion move upward to executive or policy level? What is the impact?

Albert's revisions: "reflection" = what they did when rules affected their work; SQ1 → status (approved / blocked / still in discussion); SQ2 → result, not impact.

**v1**
- Main: What is individual contributors' behavior on AI governance framework change?
- SQ1: What is the status and situation for AI tools implemented into the company's current BI workflow? How does the company's AI governance framework influence this process?
- SQ2: Does any individual contributor's request move upward to executive or policy level? What is the result after this process?

*(Claude flags on v1)* SQs do not cover the main question's everyday behaviour; "framework change" unanswerable for #7 #12 #13 #14 and presupposes a framework; SQ1 as company inventory conflicts with NDA / personal-capacity clause; "executive or policy level" misses Shopee's Regional BI route. Open questions for v2: where behaviour sits; "rules as encountered" for newcomers; SQ1 as own experience (replace "status").

Q2d answer: high-impact requests also return yes/no → evolution at Shopee most likely visible as practice sedimentation (rulings → "we just know now"), not documented framework versions.

**v2 — ADOPTED (Sep 20, 2026)**
- **Main:** How do individual contributors in BI work encounter, interpret and act on their organisation's rules for generative AI use?
- **SQ1 (downward):** What happens when they use, or try to use, GenAI in their analytical work, and how do the rules shape what they do next?
- **SQ2 (upward):** Do their requests or concerns travel upward to whoever decides the rules, and what comes back?

Why this shape: behaviour sits in the main question; SQ1/SQ2 split it by direction. Answerable by all 14 (no reliance on recalling change); "rules… written or unwritten" avoids presupposing a framework; SQ1 anchored in the participant's own work (no company inventory → no NDA conflict); "whoever decides" covers Shopee's Regional BI and the local CEO. Maps to the spine: SQ1 → structural/procedural practices, SQ2 → relational.

Consequences: evolution is no longer promised by the RQ — it becomes a findings strand where evidence supports it (Q3 threshold still to set). Title must follow the RQ. "Individual contributor" still needs Albert's own definition; the distinction from Rakova (participants have not opted into RAI work) belongs there.

## Q3 — Shopee evolution threshold (Sep 29, 2026)

Albert's expectation: all 4 Shopee participants will independently describe the same change between the 2023 policy and the Q4 2024 rollout.

**Rule (fixed before the first Shopee interview):**
- **Met** — ≥3 of 4 independently describe the same change with a rough date and a named trigger → evolution becomes a findings section; may appear in the title.
- **Partial** — 2 of 4, or accounts agree on the change but not on date/trigger → reported as a contested/partial account; not in the title.
- **Backup (not met)** — <2 of 4 → evolution reported as what BI practitioners could and could not see of change (practice sedimentation: rulings → "we just know now"); title promises encounter and response only.

Independence safeguards: schedule the four Shopee interviews close together; ask each participant not to discuss the interview with colleagues until all four are done; do not mention what others said.

## "Individual contributor" — draft definition (Sep 29, 2026)

Albert: "individual contribution in an organization is the direct work output, performance, or value that a single person delivers through their own personal effort, without the responsibility of managing other employees."

*(Claude flags)* (1) Defines the contribution, not the person — rephrase as a person. (2) "Without managing others" excludes #3 (Assistant Manager, DS), #4 (Lead, OPS BI & Payment), #9 (Engineering Manager), possibly #2 (Analyst PM) — conflicts with RQ v2 "individual contributors in BI work". (3) Missing the BI inclusion criterion and the not-opted-into-RAI distinction from Rakova. **Decision needed:** how the managers sit in the RQ.

**Decision (Sep 29): option (b) — widen; term becomes "BI practitioners".**

Working definition (draft for Albert to edit):
> **BI practitioners** are people who produce, maintain or directly supervise analytical outputs that others use to make decisions, and who neither set their organisation's rules for generative AI use nor hold a formal responsible-AI or AI-governance role.

- Clause 1 = the sampling-frame inclusion criterion (admits data engineers, planning/ops roles, first-line managers).
- Clause 2 = boundary against policy owners (Shopee Regional BI / local CEO stay outside the sample).
- Clause 3 = distinction from Rakova et al. (2021), whose participants opted into RAI work.
- Tier (operational / tactical) remains a **case attribute**; protocol tier branches unchanged.

**RQ v2.1** (term swap only)
- **Main:** How do BI practitioners encounter, interpret and act on their organisation's rules for generative AI use?
- **SQ1:** What happens when they use, or try to use, GenAI in their analytical work, and how do the rules shape what they do next?
- **SQ2:** Do their requests or concerns travel upward to whoever decides the rules, and what comes back?

## Novelty candidates to screen (titles only, not read — Sep 11 web search)

- Generative AI Uses and Risks for Knowledge Workers in a Science Organization — https://arxiv.org/html/2501.16577v1
- AI Governance as a Mediator Between Institutional Pressures and Workplace Use of Generative AI — https://link.springer.com/chapter/10.1007/978-3-032-06164-5_20
- Bringing Worker Voice into Generative AI (MIT) — https://mit-genai.pubpub.org/pub/obr01l0u/release/1

## Open

- ~~Q3~~ threshold set Sep 29 (see above)
- ~~"Individual contributor"~~ → "BI practitioners" (Sep 29); definition wording to confirm
- ~~Interview start date~~ **Rescheduled Oct 5 – Oct 19** (Albert, Sep 28)
- **Q2 (examiner)** — why governance, not adoption? (partly answered by local screening/escalation)
- Later: Ackerman Likert items; Plan 3 vs Plan 1 for Chapter 2
