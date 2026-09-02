# Interview Protocol v0.95

**Study:** Organizational Policy Development for Generative AI Integration in Business Intelligence Workflows: A Qualitative Analysis of Governance Framework Evolution
**Researcher:** Liu Yu-Shu (Albert) | **Draft:** Sep 2, 2026 (rev. after participant list confirmed) | **Status:** not yet piloted

**Companion files (read together):** `sampling_frame.md` (cases, tiers, sequencing, confidentiality rules) and `wording_card_bilingual.md` (fixed EN/zh-TW wording for the core items).

> **Reframing note (Sep 2).** The confirmed sample contains no strategic-tier informant — no participant authored a GenAI policy. The study is therefore positioned as an account of how organizational GenAI policy is **encountered, interpreted and adapted at the analytical working tier**, and whether that adaptation feeds back upward. Sections C–E are unchanged in content, but their weight shifts: Phase 1 (C) now reconstructs how policy *arrived* rather than how it was authored, and Phase 3's upward-feedback items (E2, E3) become the central test. See `sampling_frame.md` §3.

> **Language (Sep 2).** Delivered in English and interpreted live for participants #1–6, EXCEPT the items fixed in `wording_card_bilingual.md` — the purpose statement, incident menu, four process-trace questions and confidence probes — which are read as written in both languages. Improvising those destroys comparability in the core section and cannot be repaired afterwards.

**Target duration:** 60-75 min. **Format:** remote, semi-structured, recorded with consent.

---

## 0. Design logic (for the methods chapter, not for participants)

**Three phases** (the protocol's spine) are a compression of the lifecycle convergence in the corpus: Batool's "When" dimension (`batool2024aigov` §4.1 p.8-9; `batool2024rai` §3.1 p.3), Joshi's six-stage GenAI lifecycle (`joshi2025resai` p.6-8), Weinberg's four-phase FAIGMOE model (`weinberg2025faigmoe` §3.3 p.7-8), and Xue & Pang's four-stage anticipatory continuum (via `ismail2025frameworks` §4.2 p.128).

**Three tiers** (strategic / tactical / operational) are a case attribute, not a code. Four independent sources converge on this vertical: Joshi p.2; Lee L1/L2/L3 (`lee2024questionbank` §4.1 p.7-8); Batool's 5-level typology (`batool2024aigov` §4.2 p.14); NTT DATA's strategy/organization/lifecycle tiers (`ismail2025frameworks` §4.3 p.129). No paper in Clusters A+B observes this vertical empirically inside a firm — that gap is what the depth stratum is for.

**One instrument, tier-branched probes.** Everyone gets the same phases and the same incident anchor so cross-tier answers are comparable; probes differ in altitude. Modelled on Lee's own tier-descending pairs, e.g. L2 "Do you design the AI system with interpretability in mind from the start?" -> L3 "Do you research and try to use the simplest and most interpretable model possible?" (`lee2024questionbank` §4.1 p.7-8).

**Critical-incident anchor.** Opening with an abstract policy question yields the corporate line in generic AI-ethics vocabulary. Anchoring on a concrete BI artifact or event keeps the conversation inside the workflow. A bounded menu of three incident *types* preserves comparability when the specific incidents differ.

**Timeline uncertainty is data.** Where a participant cannot date a change or name who made it, record the uncertainty rather than pressing. The corpus assumes governance is documented, staged and layered (`agarwal2025fivelayer` §3 p.3-5; `luna2024paradigms` p.4-5). If practitioners experience it as undated and unattributed, that mismatch is a finding.

---

## 1. Opening (5 min)

*Not recorded until consent is confirmed on tape.*

1. Thank you. Introduce self, programme, supervisor.
2. Purpose in one sentence: "I'm studying how organizations actually develop and change their policies for using generative AI in reporting and analytics work — not what the policy says, but how it got there and how it has changed."
3. Confirm: information sheet read; consent form signed; questions about it.
4. Confirm on record: recording OK; can stop or skip anything; can withdraw; anonymised at organization level as well as personal level.
5. "There are no right answers, and I'm not evaluating your organization's compliance. I'm interested in how things actually work."

**Start recording. Restate consent question on tape.**

---

## 2. Section A — Role and context (5 min)

- A1. Can you describe your role and what a typical week looks like?
- A2. Where does generative AI touch your work, if at all? *(Probe for concrete: which tools, which tasks — drafting summaries, writing queries, explaining a dashboard, generating commentary on a report.)*
- A3. Roughly when did GenAI tools first appear in your team's work? Was that formal or informal at first?
- A4. Who in the organization would you say "owns" the rules about using these tools?

> Tier note — A4 is the first triangulation point. Strategic informants tend to name a committee; operational informants often name a person, a wiki page, or nobody. Divergence here is a finding, not an inconsistency to resolve.
> Source: `batool2024aigov` §4.1 p.8-9 (the "who is governing" question); `batool2024rai` §3.1.1 p.4 ("If an organisation is not sure exactly what they need to govern...").

---

## 3. Section B — Incident anchor (20 min) **[core section]**

**Read the menu aloud — fixed wording, both languages: `wording_card_bilingual.md` §4–5.** "I'd like to spend most of our time on one concrete situation rather than on the policy in the abstract. Three kinds of situations tend to come up — could you pick whichever you have a real example of?"

- **(i) A refused or restricted use.** Someone wanted to use a GenAI tool for something in a report or analysis, and it wasn't allowed, or had to be done differently.
- **(ii) An output that couldn't be used as it was.** A figure, a summary, a query, or a piece of commentary that turned out to be wrong, unverifiable, or needed rework before it could go into a deliverable.
- **(iii) A use that got approved.** A tool or a way of working that went from "someone was trying it" to "this is how we do it."

> Wording discipline: never say "hallucination," "violation," "breach," or "mistake." (ii) asks the participant to describe normal work, not to confess. Type (iii) is the easiest to answer and is a good fallback if the participant hesitates at (i) and (ii).

**Then process-trace it with the same four questions, whichever type they chose — fixed wording, `wording_card_bilingual.md` §6:**

- B1. **What happened?** Walk me through it from the beginning. *(Probe: which report/dashboard/dataset; who was involved; what was the deadline pressure.)*
- B2. **What rule existed at the time?** Was there anything written down? Did people know about it? How did you find out what was allowed?
- B3. **What changed afterwards?** Did anything about how you work change? Was anything written, announced, or added to a tool? Or did it just... settle?
- B4. **Who decided?** Who made the call, and who else had to agree? Did it go anywhere above/below your level?

**Confidence probes (ask after B3/B4, lightly):**
- "Roughly when was that — month, quarter, or is it hard to pin down?"
- "Is that written somewhere, or is it more that people know it?"

> Record the participant's *confidence* in dating and attribution as a coded attribute (`high / approximate / cannot say`). See design logic above.

**If time and rapport allow, take a second incident of a different type.**

Sources: incident types derived from the risk typologies in `taeihagh2025govgenai` Table 1 p.2-4 (hallucination/inaccuracy; sensitive-information risk) and `joshi2025resai` §I-B p.1-2 (Shadow AI, unauthorized use); the "output that could not be used" type targets the decision-support language present across the corpus (`joshi2025resai` §I-B p.1; `weinberg2025faigmoe` §3.4 p.9; `lee2024questionbank` §4.3 p.9) where literal BI terms are absent in all 12 notes.

---

## 4. Section C — Phase 1: Policy Framework Development (10 min)

- C1. How did the current rules on GenAI come about? Where did the first version come from — copied from somewhere, written internally, imposed from a parent company?
- C2. Who was in the room when it was written? Was anyone who actually builds or uses reports involved?
- C3. What was it trying to prevent? What worried people most?
- C4. Is there anything in it that's specific to analytics or reporting work, as opposed to general company-wide AI rules?

**Tier branches**

| Tier | Additional probe |
|---|---|
| Strategic | How did you reconcile the pressure to adopt with the risk position? Did any external requirement (customer, auditor, regulator, parent company) set the floor? |
| Tactical | When the policy arrived at your team, what did you have to interpret or fill in yourself? |
| Operational | How did you first learn what you were and weren't allowed to do? Training, a document, a colleague, or trial and error? |

Sources: C1-C2 from the participatory co-design and strategy-tier constructs in `ismail2025frameworks` §3.4 p.127, §4.2 p.128, §4.3 p.129; C2 also from `lee2024questionbank` Table 2 p.14 ("Does the company have designated responsibility for AI and RAI within the organisation?" and the accountability-framework item), adapted from closed to open form; C4 is the study's own BI-specific extension — no corpus source, inductive by design.

---

## 5. Section D — Phase 2: Implementation & Change Management (10 min)

- D1. How did the rules actually reach people? What made them stick, or not?
- D2. Are there technical controls, or is it mostly guidance people are trusted to follow? *(Probe: approved tool list, blocked services, data restrictions on what can go into a prompt, review before publishing.)*
- D3. What's the gap between what the policy says and what people actually do under deadline?
- D4. Has anyone been in a position where following the rule would have made the work impossible? What happened?

**Tier branches**

| Tier | Additional probe |
|---|---|
| Strategic | How do you know whether it's being followed? What would tell you it wasn't? |
| Tactical | What have you had to decide yourself because the policy didn't cover it? |
| Operational | When you're unsure whether something's allowed, what do you actually do? |

Sources: D2 from the technical-safeguard constructs in `ismail2025frameworks` §6.4 p.133-134 (prompt checks, data controls) and `joshi2025resai` p.5-6 (sandboxing, Shadow AI); D3-D4 target the implementation gap that is the shared WHY across `batool2024rai` §1 p.1-2, `ferjani2025cogov` §1 p.4727, `agarwal2025fivelayer` §1 p.2, `ozman2025platforms` §1.1 p.78; D1 informed by `lee2024questionbank` §5.1 p.14 on role-specific knowledge silos.

---

## 6. Section E — Phase 3: Organizational Adaptation Dynamics (10 min)

- E1. How have the rules changed since the first version? Can you walk me through the changes?
- E2. What triggers a change — an incident, a new tool, a new regulation, someone new arriving?
- E3. Is there a route for someone doing the work to say "this rule doesn't make sense"? Has it ever been used?
- E4. Has the work itself changed — what analysts do day to day, what skills matter now?
- E5. Where do you expect the rules to go next? What's still unresolved?

**Tier branches**

| Tier | Additional probe |
|---|---|
| Strategic | Do you review this on a schedule, or only when something forces it? |
| Tactical | Does what your team learns ever make it back up into the policy? Through what channel? |
| Operational | Has anything you or a colleague raised ever changed a rule? |

Sources: E2-E3 target adaptive/bidirectional governance — `joshi2025resai` p.6-7 (bottom-up sandbox feedback into strategic roadmaps), `taeihagh2025govgenai` p.6 (adaptive governance; "red teaming, impact assessment, and internal auditing need to become routine"), `weinberg2025faigmoe` §3.3 p.8 (non-linear feedback loops); E3 also adapts `lee2024questionbank` Fig.10 p.33 ("Is there a mechanism to capture feedback by users of the system and enable user contestability?"); E4 from `ismail2025frameworks` §5.5 p.132 (labour shifts, analysts to prompt validators) and `taeihagh2025govgenai` p.16.

---

## 7. Section F — Document walkthrough (10 min) **[document-anchored cases only]**

*Only where prior permission for document access has been granted. Documents are consulted, never reproduced or quoted in the thesis.*

- F1. Can we look at the current version together? *(Ask the participant to screen-share or describe; do not request a copy unless publication permission was granted.)*
- F2. What's the revision history — how many versions, and when? *(Record dates and version numbers only.)*
- F3. For each change we can see: what prompted it?
- F4. Is there anything in here that's never actually been applied?

> Metadata extraction target: version number, date, and a one-line description of what changed. This is the temporal spine that the interview-only cases lack, and it is what allows recall in the unanchored cases to be assessed.

---

## 8. Section G — Closing (5 min)

- G1. Is there anything I should have asked and didn't?
- G2. Is there anyone else here whose view on this would be different from yours? *(Depth-stratum recruitment route. Ask especially of participants #3 and #4 — the Shopee Assistant Manager and OPS BI Lead are the only realistic route to a policy owner, which would complete Depth A's vertical. See `sampling_frame.md` §3.)*
- G3. Would you be willing to look at a short summary of what I understood, to check I've got it right? *(Member checking.)*
- Thank you; restate anonymisation; confirm withdrawal window and contact.

**Stop recording.**

---

## 9. Immediately after each interview (researcher only)

Write a one-page contact summary within 24h: setting, incident type(s) chosen, tier, dating confidence, anything the recording won't capture, and any new code candidate that didn't fit the a priori frame.

## 10. Analysis notes

- **Seed codes (a priori):** three phases; Luna's four constituents — Data, Model, Content Generation, Ethics (`luna2024paradigms` p.4-5); accountability vs. responsibility split (`priyanshu2024claude` §6.1 p.5 — illustrative only, low-tier source).
- **Inductive space:** everything BI-workflow-specific. No a priori code may be the answer to the RQ; if the findings are simply "we found Data, Model, Content and Ethics governance," the study has confirmed Luna rather than extended him.
- **Case attributes (not codes):** tier; sector; size; document-anchored y/n; dating confidence.
- **Reliability procedure:** Luna's three-cycle consideration — first pass extracts, second reviews, third resolves disagreement (`luna2024paradigms` p.4). Adapt to a solo-researcher version (coding, re-coding after an interval, and supervisor spot-check of a sample) and state the adaptation honestly in Chapter 3.
- **Cross-case display:** a coverage matrix in the spirit of Luna's rubric — Covered / Partially covered / Not covered (`luna2024paradigms` p.6) — applied to organizations x phases rather than regions x processes.

## 11. Known weaknesses of this draft

1. No methodological citations yet (no qualitative-methods literature in Clusters A+B). Chapter 3 needs 6-8 method sources or a dedicated cluster.
2. Language resolved (Sep 2): English master + interpreted delivery, with core items fixed bilingually. Back-translation of the fixed items still outstanding.
2b. Tenure floor: participants #7, #12 and #14 (1–2 yr) joined after GenAI adoption and may have no evolution memory. Do not press Section E with them — use them for the sedimented state (what they found on arrival, how they learned it).
3. Not piloted. Section B is the section most likely to over-run.
4. Sections C-E may be too many questions for 30 minutes combined; expect to cut on the basis of the pilot, preserving B.
