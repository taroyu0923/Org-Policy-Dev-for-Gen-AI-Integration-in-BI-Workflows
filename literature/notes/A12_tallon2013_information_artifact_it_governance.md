# [A12] Tallon, Ramirez & Short (2013) — The Information Artifact in IT Governance: Toward a Theory of Information Governance

**Bib key:** `tallon2013informationartifact` *(corrected Oct 1, 2026; was `tallon2013infoartifact`, not a key in references.bib)*
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.2753/MIS0742-1222300306 as printed. Flagged in `s3_gapfill_prompt.md` as "theoretical lineage of the thesis spine" — pairs with the Papagiannidis/Mikalef/Conboy (2025) structural/procedural/relational spine already adopted (see Pipeline_State "Design decisions in force").
**Cluster:** A — Theoretical lineage / IT-information governance (pre-AI)
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill


> **PDF page check (Oct 1, 2026).** Checked against the PDF in `D:\Master\Thesis\Thesis Content`; printed pages. These override page numbers and quotes below. Log: `planning/s3_section11_spotcheck_2026-10-01.md` (or the session log named). §11 verdict changes, if any, wait for Albert's decision on the coding rule.
>
> Offset: printed = PDF page + 139. Verified: sample of IT executives (p. 142); "pack rat" (pp. 156, 160); Johns Hopkins (pp. 160, 162, 166); user education so users do not "trivialize, circumvent, or ignore the rules" (p. 165); over-governance "motivating users to work around policies" and Intel CISO quote (p. 167); "our interviews involved IT executives rather than users" (p. 168). ⚠ The paper does **not** say "shadow IT" (the note's gloss). §11: second-hand, executive-reported user data about **information** governance (pre-GenAI) — contested between absence and partial; Albert to decide.

---

## 1. WHY
Traditional IT governance literature focuses on physical IT artifacts (hardware/software), neglecting nonphysical "information artifacts" amid exponential data growth. *Location: Abstract pp.141-142; Intro pp.142-144.*

## 2. HOW
Qualitative field interview study for theory building. 37 senior executives, 30 organizations, 17 industries. Interviews late 2008–June 2009. NVivo coding (open/axial/selective) across 14 nodes. *Location: pp.151-155; Appendix pp.176-177.*

## 3. WHAT
- Nomological framework of information governance (antecedents → practices → performance). *(Fig.1, p.168)*
- Three-part typology: structural, procedural, relational practices. *(pp.160-165, Table 6)*
- Dual antecedents (6 enablers, 3 inhibitors). *(pp.158-160, Table 5)*
- Curvilinear performance / over-governance risk. *(pp.166-167)*

## 4. DEFINITION
"...we define information governance as a collection of capabilities or practices for the creation, capture, valuation, storage, usage, control, access, archival, and deletion of information over its life cycle." *(Intro, p.142)*

## 5. CITABLE
Executive/C-suite perspective; interviewed CIOs/CISOs/CTOs, not end-users.
- "If we just focus on protection, we will over-control and constrain and then we'll generate actually more risk since people will go around the controls...you drive the business to create." — CISO, Intel *(p.167)*
- "Researchers...act independently when it comes to storage environments...it's more of a cultural discussion, it's control...very protective and very possessive of their environment." — CTO, Johns Hopkins *(p.160)*
- "You have to have a governance framework in place...We need to know the policy trade-offs — it's a constant negotiation." — CIO, Visa *(p.165)*

## 6. AUTHORS/YEAR/VENUE
Paul P. Tallon, Ronald V. Ramirez, James E. Short. 2013/2014 (Winter 2013–14). *Journal of Management Information Systems*, Vol.30, No.3, pp.141–177. DOI: 10.2753/MIS0742-1222300306.

## 7. INTERVIEW VALUE
HIGH — empirical multi-case study with a full Generic Interview Protocol appendix (pp.176-177). Note: predates AI/GenAI; foundational information-governance constructs transfer directly.
- **Policy Encounter & Interpretation:** "What policies have you enacted to manage information?"; "Who sets and monitors these policies?"; "Do you have specific data retention policies?" (Appendix p.176); "Protect to enable" framing (CISO, Intel, p.167); policy-ownership shift from IT to legal/business (CIO, Alaska Air, p.162).
- **Implementation & Change Mgmt:** "How do you classify data over its useful economic life?"; "Who is responsible for data migration between storage tiers?" (Appendix p.177); pack-rat culture as inhibiting antecedent (p.160); user education on storage cost/utilization (Table 6, p.166).
- **Organizational Adaptation Dynamics:** "What do you see as the major business opportunities and challenges arising from growth in data/information?" (Appendix p.177); curvilinear over-governance hazard — "like a kid running with scissors" (CISO, Intel, p.167).

## 8. SNOWBALL
1. Khatri & Brown (2010), "Designing data governance", *CACM* 53(1), 148-152 (References p.174, ref.18) — foundational 5-domain data-governance framework.
2. Kooper, Maes & Roos Lindgreen (2011), "On the governance of information...", *IJIM* 31(3), 195-200 (References p.175, ref.23) — sensemaking perspective on competing-interest governance negotiation.
3. Weber, Otto & Österle (2009), "One size does not fit all: A contingency approach to data governance", *JDIQ* 1(1), 1-27 (References p.176, ref.51) — contingency dynamics for BI/analytical units.
4. Watson, Fuller & Ariyachandra (2004), "Data warehouse governance: Best practices at Blue Cross and Blue Shield of North Carolina", *Decision Support Systems* 38(3), 435-450 (References p.176, ref.50) — governance specifically within BI/data-warehousing.
5. Peterson (2004), "Crafting information technology governance", *Info Systems Mgmt* 21(4), 7-22 (References p.175, ref.32) — originates the structural/procedural/relational tripartite framework used throughout.

## 9. LIMITATIONS
1. "our sample of 30 organizations is small and unrepresentative... concern as to the generalizability" *(pp.171-172)*.
2. Executive-only interviewees, excluding end-users/stewards — "It would have been useful to interview business managers... application owners, or data stewards" *(p.172)*; also: "our interviews involved IT executives rather than users, it may be difficult to find this inflection point without speaking with users who are likely to be most disadvantaged" *(p.168)*.
3. Cross-sectional, not longitudinal *(p.172)*.
4. Cannot causally link governance to firm-level financial performance *(p.172)*.

## 10. BI LINK
Extensive explicit mentions — "business intelligence tools and related IT dashboards modeled on the balanced scorecard collect IT performance metrics" (p.148); repeated "analytics" mentions (pp.159, 163-164, 167, 172); data warehouse governance discussion citing Watson et al. (Table 1, p.146); decision-support/decision-making throughout (pp.142, 156, 167).

## 11. WORKING-TIER RECEPTION
Explicit methodological limitation is itself the key finding — sample was 37 C-suite/senior IT executives only, no working-tier practitioners interviewed (p.142, 152). Authors explicitly acknowledge: "our interviews did not reveal a sense of resentment among users... but as our interviews involved IT executives rather than users, it may be difficult to find this inflection point without speaking with users" (p.168). Despite this, executive reports surface substantive working-tier dynamics at second hand: (a) policy reaches users via mandatory storage-cost education and "why" framing to prevent circumvention (pp.165-166); (b) gaps — "pack rat" hoarding behavior undermining retention policy (p.160), researcher territorial resistance to central IT control at Johns Hopkins (p.160); (c) attitudes — over-governance explicitly described as driving shadow IT/workarounds (p.167); (d) shared oversight/joint governance arrangements, user ownership/stewardship rights (pp.163, 166); (e) flagged by the paper itself as a gap for future user-level research (p.172). Second-hand/executive-reported, not directly observed — a genuine but qualified working-tier data point.

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
