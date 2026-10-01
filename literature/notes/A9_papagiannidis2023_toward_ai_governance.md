# [A9] Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) — Toward AI Governance: Identifying Best Practices and Potential Barriers and Outcomes

**Bib key:** `papagiannidis2023towardaigov` *(corrected Oct 1, 2026; was `papagiannidis2023towardaig`, not a key in references.bib)*
**Verification status:** Title/authors confirmed from notebook title page (Sep 11, 2026); DOI 10.1007/s10796-022-10251-y as printed. Distinct from `responsibleaigovreview` (Papagiannidis, Mikalef & Conboy 2025, JSIS) already in the corpus — different paper, different co-authors, different venue; no key collision.
**Cluster:** A — Systematic reviews / empirical AI governance studies
**Note version:** v2.4 (compiled Sep 11, 2026) — S3 gap-fill

---

## 1. WHY
Organizations struggle to realize performance gains from AI due to technical complexity, unmanaged risk, and adoption barriers including employee resistance; gap in unifying IT/data governance into an empirical framework linking AI governance to firm performance. *Location: Abstract p.123; Intro pp.123-124; Sec.2.2 p.125.*

## 2. HOW
Exploratory qualitative comparative multi-case study. Semi-structured interviews plus secondary documents. Sample: 3 Norwegian energy firms (200/530/100 employees), 15 respondents. NVivo coding across 3 rounds. Cross-sectional, incorporating 2020 data. *Location: Sec.3 p.126; Sec.3.1-3.2 pp.126-127; Sec.3.3 p.128; Sec.5.3 p.138.*

## 3. WHAT
- Three-dimensional governance framework: Structural/Procedural/Relational. *(Sec.4.2, pp.130-133; Fig.1 p.135)*
- Enablers/Inhibitors typology. *(Sec.4.2.4, p.134)*
- Value realization: 20-30% maintenance-cost reduction attributed to governance maturity. *(Sec.4.2.5, p.135)*
- Domain-expert leadership identified as critical success factor. *(Sec.4.2.3, p.134)*

## 4. DEFINITION
Cites Butcher & Beridze (2019): AI governance "can be characterized as a variety of tools, solutions, and levers that influence AI development and applications" (Intro p.123). Authors' own framing: governance is "not seen as a process but as a set of important aspects...to ensure that the main challenges are overcome successfully" *(Sec.5.1, p.138)*.

## 5. CITABLE
Pre-GenAI, managerial/architectural focus, but includes direct frontline-worker quotes.
- "allow an operator to make changes to the decision, what you often see is that the performance gets much worse." — Respondent 6, Company A *(Sec.4.2.3, p.134)*
- "the end-users had to follow the AI suggestions intuitively and use their domain knowledge to fill gaps that AI was not capable of." *(Sec.4.2.1, p.133)*
- "employees who refused to use the new technologies as they did not trust the results or even oppose the change... End-users had unrealistic expectations" *(Sec.4.1.2, p.131)*
- "AI governance requires continuous adaptation and modification as new data emerges or conditions change" *(Sec.5.1, pp.137-138)*

## 6. AUTHORS/YEAR/VENUE
Emmanouil Papagiannidis, Ida Merete Enholm, Christian Dremel, Patrick Mikalef, John Krogstie. 2023 (online 20 Apr 2022). *Information Systems Frontiers*, 25, pp.123–141. DOI: 10.1007/s10796-022-10251-y.

## 7. INTERVIEW VALUE
HIGH — direct empirical multi-case study with actual respondent quotes usable near-verbatim as protocol anchors, and a full appendix protocol (p.139).
- **Policy Encounter & Interpretation:** governance-tension framing between operator autonomy and model authority (Sec.4.2.3, p.134); appendix interview questions (p.139).
- **Implementation & Change Mgmt:** power/Tableau/Grafana/Excel-adjacent dashboard tooling context (Table 1, p.127); domain-expert leadership requirement (Sec.4.2.3, p.134).
- **Organizational Adaptation Dynamics:** continuous-adaptation requirement quote (Sec.5.1, pp.137-138); employee resistance/unrealistic-expectations dynamic (Sec.4.1.2, p.131).

## 8. SNOWBALL
Not separately re-harvested this pass beyond what is captured in the CITABLE/WORKING-TIER sections; the paper's own reference base overlaps with A8 (Mäntymäki), A12 (Tallon), and the structural/procedural/relational typology shared with A12 and E2.

## 9. LIMITATIONS
Not separately itemized in the harvested excerpt beyond the cross-sectional/2020-data-recency caveat noted in §2 (Sec.5.3, p.138).

## 10. BI LINK
Table 1 (p.127) explicitly names Power BI, Tableau and Grafana dashboards as the analytical tooling context; strong direct BI link, one of the strongest in this batch.

## 11. WORKING-TIER RECEPTION
> **Recoded Sep 30, 2026 (PDF-verified, Albert approved): PARTIAL, not substantive.** Respondents were selected for "a key position in the firm, for example, managers and leading developers" who "have contributed to the overall development of AI" (Sec.3.2, p.127; Table 2: CAIO, developers, ML engineers, heads of AI/analytics, one data analyst, one data scientist). End-user resistance is reported by developers ("Another challenge that the developers faced came from employees who refused…", p.131), i.e. second hand, as in A12. Point (d) below ("implying an active feedback/adaptation channel") is an inference, not in the paper. Tally unaffected (partial ≠ absence). Original text kept below for the record.

~~Substantive — one of the four empirically strongest sources in this S3 batch.~~ (a) Policy/model output reaches operators directly via dashboard tooling and domain-expert-mediated interpretation (Table 1 p.127; Sec.4.2.1 p.133). (b) Gap: operator manual overrides of the model degrade performance, evidencing a practice/design mismatch (Sec.4.2.3, p.134). (c) Attitudes: explicit employee resistance and distrust — "employees who refused to use the new technologies as they did not trust the results or even oppose the change" (Sec.4.1.2, p.131). (d) Domain experts hold real influence — "domain expert leadership" is named a critical success factor, implying an active feedback/adaptation channel (Sec.4.2.3, p.134). (e) Not explicitly detailed for edge cases outside governance scope, but the "continuous adaptation" framing implies ad hoc local handling (Sec.5.1, pp.137-138).

## Albert's Questions
None yet — pending Albert's own notebook questions before compile lock.
