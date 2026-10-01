# [D6] Lu, Zhu, Xu, Whittle, Zowghi & Jacquet (2024) — Responsible AI Pattern Catalogue: A Collection of Best Practices for AI Governance and Engineering

**Bib key:** `lu2024raipatterns` *(corrected Oct 1, 2026; the earlier header said `lu2024raipatterncatalogue`, which is not in the bib)*
**Verification status:** Title, authors, venue and DOI confirmed against the PDF: *ACM Computing Surveys* 56(7), Art. 173, April 2024, 35 pp., DOI 10.1145/3626234. **Content rebuilt from the PDF on Oct 1, 2026.** The text layer covers all 35 pages; the figures on pp. 173:2, 173:6 and 173:7 and the figure/table pages 173:22 and 173:28 were checked by OCR. Pages below are printed pages (173:N).
**Cluster:** D — Responsible AI adoption / engineering practice
**Note version:** v2.4, compiled Sep 11, 2026 (S3); **rewritten Oct 1, 2026** — see `planning/d6_pdf_check_2026-10-01.md`

> ⚠ **History.** The Sep 11 note's §3, §4, §5, §7, §8, §9 and §11 were taken from a NotebookLM answer (Query 2) that invented the paper's structure. It had an "AI Ethics Champion" pattern, a "Continuous AI Ethics/Governance Checks" pattern, a "Product Management Patterns" section, escalation to a champion, and a "living catalogue" discussion. **None of these is in the PDF**: "champion" has 0 hits in the text and the OCR. Of the five snowball items, only Amershi et al. (2019) is in the reference list; Morley et al. (2020), Ozmen Garibay et al. (2023), Vakkuri et al. (2020) and Rakova et al. (2021) are not. Query 1 (`_raw/D6.md` §1–6) was accurate and is the basis of §1–6 below. **Never cite D6 for champions, conduits or escalation.**

---

## 1. WHY
High-level AI ethics principles give technology-neutral direction, but "without further best practice guidance, practitioners are left with nothing much beyond truisms" (Sec. 1, pp. 173:1–2). Existing work concentrates on algorithm-level fixes for a narrow set of principles (fairness, privacy), while ethical issues arise across the lifecycle and across AI, non-AI and data components. The authors propose patterns as reusable, system-level solutions (Sec. 1, pp. 173:2–3).

## 2. HOW
Systematic multivocal literature review (MLR): academic literature (Kitchenham & Charters guideline) plus grey literature (Garousi et al. guideline). Searched ACM DL, IEEE Xplore, ScienceDirect, SpringerLink and Google Scholar, plus Google Search for grey literature, up to 31 July 2022. 4,470 academic + 2,595 grey items screened down to a final **205 academic + 69 grey (274)** (Sec. 2, pp. 173:3–5). One researcher screened; a second checked a random sample (Sec. 7, p. 173:29). **No fieldwork of its own.**

## 3. WHAT
A catalogue in three groups (Fig. 1, p. 173:2; Fig. 4, p. 173:7):
- **§3 Governance patterns** (multi-level; pp. 173:5–15):
  - industry level: RAI regulation, regulatory sandbox, building code, RAI standard, maturity model, certification, trust mark, independent oversight;
  - organisation level: leadership commitment, **ethics committee**, code of ethics, ethical risk assessment, standardised reporting, role-level accountability contract, RAI software bill of materials, ethics training;
  - team level: customised agile process, tight coupling of AI and non-AI development, diverse team, **stakeholder engagement**, continuous documentation using templates, FMEA, fault tree analysis, verifiable claims.
- **§4 Process patterns** (pp. 173:15–21), by stage:
  - requirements;
  - design;
  - implementation, e.g. RAI governance of/via APIs;
  - testing;
  - operation, e.g. continuous deployment for RAI (§4.5.1) and extensible, adaptive and dynamic ethical risk assessment (§4.5.2).
- **§5 Product patterns** (pp. 173:21–27), by layer: supply chain, system, operation infrastructure.
- §6 Related work (p. 173:27–29) · §7 Threats to validity (p. 173:29) · §8 Conclusion (pp. 173:29–30).
- **Stakeholders** in three levels: industry, organisation and team (Fig. 3, p. 173:6). The organisation level includes board members, executives, managers and employees.

## 4. DEFINITION
"The governance for RAI systems can be defined as the structures and processes that are employed to ensure that the development and use of AI systems meet AI ethics principles." (Sec. 3, p. 173:5)
"Employees are individuals who are hired by an organization to perform work for the organization and expected to adhere to RAI principles in their work." (Sec. 3, p. 173:7)

## 5. CITABLE
- Ethics committee: an AI governance body "established to develop standard processes for decision making, as well as to approve and monitor AI projects"; it "provides feedback and guidance to the project team after reviewing the proposal" (§3.2.2, p. 173:10). The feedback flows **down**, proposal by proposal.
- Code of ethics: "A code of ethics provides employees with the same concrete rules on developing AI systems, but it relies on individuals to do the right thing with limited monitoring and enforcement." (§3.2.3, pp. 173:10–11)
- Ethics training "may only offer a subset of knowledge and skills within limited time" (§3.2.8, p. 173:12).
- Stakeholder engagement through "interviews, online and offline meetings, project planning/review, participatory design workshops, and crowd sourcing" (§3.3.4, pp. 173:13–14). These are stakeholders of an AI system, not staff influencing governance.
- Assess behaviour "before deploying AI systems in the real world" (p. 173:18; used in 2.1).
Check each quote against the PDF again before use.

## 6. AUTHORS/YEAR/VENUE
Qinghua Lu, Liming Zhu, Xiwei Xu, Jon Whittle, Didar Zowghi, Aurelie Jacquet. 2024 (accepted 26 Sep 2023). *ACM Computing Surveys* 56(7), Article 173, 35 pp. https://doi.org/10.1145/3626234

## 7. INTERVIEW VALUE
Moderate, as **vocabulary for what a rule-setting organisation may have in place**, not as evidence of how staff meet it. Patterns a BI practitioner could encounter:
- code of ethics (p. 173:10);
- ethics training (p. 173:12);
- an ethics committee approving projects (p. 173:10);
- continuous documentation templates (§3.3.5);
- ethical risk assessment (§3.2.4).
Useful when coding the **procedural** and **structural** practices participants name. It has no account of reception and no upward channel.

## 8. SNOWBALL
Checked in the reference list (pp. 173:30–35):
1. Amershi et al. (2019), *Software engineering for machine learning: A case study*, ICSE-SEIP — **present** (ref. [6]).
2. Schiff, Rakova et al. (2020), *Principles to practices for responsible AI: Closing the gap*, arXiv:2006.04707 — present (ref. [99]); a lead only.
3. ~~Vakkuri et al. (2020), "Implementing ethics in AI"~~ — **not in the list** (Vakkuri appears only as a co-author of Halme et al. 2021, ref. [43]).
4. ~~Rakova et al. (2021), "Where responsible AI meets reality"~~ — **not in the list** (D7 is not cited by D6).
5. ~~Morley et al. (2020)~~ and ~~Ozmen Garibay et al. (2023)~~ — **not in the list**.

## 9. LIMITATIONS
Self-stated (Sec. 7 "Threats to validity", p. 173:29):
1. RAI is loosely defined; synonyms were added to the search string.
2. Solutions designed for a single principle may have been missed; all principles were added as search terms.
3. One researcher screened; a second checked a random sample.
The authors also plan to "validate the utility, usability, and effectiveness of the pattern catalogue … in industrial projects" (p. 173:30), so the catalogue is **not yet validated**. *(The Sep 11 note's limitations "not exhaustive" and "community validation" are not in the paper.)*

## 10. BI LINK
None. "Business intelligence", "BI" and "data warehousing" are absent. The catalogue addresses developing and operating AI systems, not using a generative AI tool in analytical work.

## 11. WORKING-TIER RECEPTION
**Documented absence** *(recoded Oct 1, 2026 from "substantive but secondary"; Albert approved; tally 22–24 → 23–25 of 36)*. Prescriptive throughout and drawn from literature; no account of how staff receive governance.
- (a) **Policy reach:** employees are stakeholders "expected to adhere" (p. 173:7). Rules travel through a code of ethics, ethics training and committee feedback on proposals (pp. 173:10–12). All prescribed.
- (b) **Gaps:** prescriptive drawbacks only. The code of ethics has "limited monitoring and enforcement" (p. 173:11); training covers a subset (p. 173:12). Agile methods "largely neglect the AI ethics principles" (§3.3.1, p. 173:13).
- (c) **Attitudes:** none reported.
- (d) **Channels to influence policy:** none. The only feedback flows down (committee → project team, p. 173:10).
- (e) **Silence and edge cases:** none.

## Albert's Questions
None recorded.
