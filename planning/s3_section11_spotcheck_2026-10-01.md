# S3 §11 spot-check against the PDFs — log

**Date:** Oct 1, 2026 | **Session:** orchestration. The brief `planning/s3_section11_spotcheck_prompt.md` was run in this session at Albert's request.
**Method:**
- `pdftotext` (raw) on 11 PDFs.
- **C7 is image-only** (a 31-page browser print-out, header "PDF.js viewer") and was OCR'd at 200 dpi with tesseract.
- For each note: every specific §11 claim (and the §3/§5/§7 claims §11 depends on) was searched as an exact phrase and as key terms, then the method sections were re-read for data about staff below the rule-setting level.
- Pages are printed pages; the offset per PDF is given.

**Status:** ✅ **Decided and applied (Oct 1).** Albert chose **rule R1**. Phase 2 was run on the Sep 4 batch (§6), and the recodes were applied to the notes, 2.6 ¶2, 3.7 ¶2, the READMEs, the claims map (K6) and Pipeline_State.

---

## 1. Summary

| ID | Verdict before (Pipeline_State) | PDF finding | Proposed verdict | Claims not in PDF | Note repair |
|---|---|---|---|---|---|
| C10 Asatiani | substantive | Field study (DBA; interviews, observation and an assessment exercise, Appendix A pp. 275–276; interview counts per the note, not re-checked). Caseworkers are quoted: "David" on the handover "package of management consultancy training, capacity-building, documentation" (p. 266); "Daniel" on drift (p. 274). Threshold control "a major cultural factor in [the] business adoption", but that is reported by a team leader (p. 273). The object is controls on an in-house AI application, not rules on staff's AI use | **partial** (first-hand but thin, and about system controls) | "No workarounds" is not a located statement | pages → journal pages (PDF + 258) |
| C7 Mökander et al. | partial (range paper) | Conceptual. The only practitioner datum is **cited from Vakkuri et al. (2019)**: developers see ethics "as an impractical construct that is distant from the issues they face in daily work" (PDF p. 3). "Driving re-design" is one of seven prescribed criteria (PDF p. 16, "Page 16 of 30"). No data of its own | **documented absence** | — | add "datum is a citation"; PDF is a viewer print-out (get the publisher PDF) |
| C8 Raji et al. | "normative, no field data" (range paper) | Normative audit framework with a **hypothetical** worked example (smile-detection model; the "template model card", "hypothetical datasheet", PDF p. 8). Interviews and ethnography are steps the framework prescribes, not data | **documented absence** | §11(e) "practitioners default to optimizing isolated numerical metrics" over-reads a prescriptive remark ("Traditional metrics … may conceal fairness concerns", p. 8 of PDF). **Claims map K6 cites C8 for this; drop it** | note pages are article-relative (printed = PDF + 32, FAT* '20 pp. 33–44) |
| A12 Tallon et al. | absence (range-relevant) | 37 IT executives only. **Second-hand user data exists**: users "work around policies" under over-governance (p. 167); user education on "why" rules exist so users do not "circumvent" them (p. 165); "pack rat" hoarding (pp. 156, 160). All of it concerns **information governance (2013, pre-GenAI), not AI governance**. Authors: "our interviews involved IT executives rather than users" (p. 168) | **contested**: absence under a strict AI-governance reading; partial by analogy with A9 | The note's "shadow IT" is a gloss; the paper says "work around policies" | page offset PDF + 139; quotes verified |
| B8 Janssen | absence | Conceptual (complex adaptive systems). Surveys mentioned are other organisations' surveys (p. 39) | documented absence ✓ | — | pages PDF + 37 (note is one page low throughout) |
| A8 Mäntymäki et al. | absence | Definitional and positioning paper; calls for "in-depth interviews and ethnographic studies" (p. 607) | documented absence ✓ | — | p. 607 (note 608); definition p. 604 (605); "corporate governance sets the principles" p. 605 (606) |
| A10 Birkstedt et al. | absence | Literature review; names the gap: "little discussion of their roles in AIG" (p. 156); ethics documents and training whose "effectiveness is uncertain" (p. 153) | documented absence ✓ (under rule R2 below: partial, since it names the gap) | — | printed = PDF + 132: p. 153 (note 152), p. 156 (155), p. 158 (157), "checkbox ethics" p. 160 (159), principles-to-practices pp. 135–136 (134) |
| A11 Ashok et al. | absence | Conceptual synthesis. Proposes testing the model "through in-depth interviews" (p. 13) as future work | documented absence ✓ | — | — |
| C9 Shrestha et al. | absence | Conceptual essay (*California Management Review*). No data on staff | documented absence ✓ | — | printed = PDF + 65 |
| E2 Abraham et al. | absence | Structured literature review; no data on staff | documented absence ✓ | **§11(e) quote "how individuals actually engage with data governance mechanisms in practice" is not in the PDF**, and nor is the §7/§11 "the actual behavior of individuals". **The paper makes no such research-agenda call; do not cite it as a gap statement** | printed = PDF + 423; training/communication p. 430 (note 431) |
| E3 Janssen et al. | absence | Conceptual (design principles); "case study" occurs only in references | documented absence ✓ | — | — |
| E4 Zhang et al. | absence | Technical overview; "often overlooked by many developers" (p. 3) is a technical aside | documented absence ✓ | — | — |

**Pattern.** No further invented *Query-2 structure* of the D6/D7 kind was found. The failure mode here is milder but repeated:
- **over-reading:** C8(e), C7's cited datum presented as the source's own;
- **two invented quotes in E2;**
- **systematic page offsets:** article-relative or off by one.

## 2. Tally consequence

The previously stated range (2.6 ¶2 v1.2: **23–25 of 36**) assumed C7 and C8 were the only contested papers. **Both resolve to documented absence on the PDF**, so "two conceptual audit papers that could be coded either way" no longer describes the uncertainty.

**Recount of all 36 governance notes**, verdicts as they now stand:

| Group | Not-absence | Documented absence |
|---|---|---|
| Sep 4 harvest (20 notes; **not PDF-checked**) | B4 Joshi, B6 Lee, D4 Nahar, D5 Ackerman (substantive); D1, D2 (partial: reviews that *name* the gap) | 14 |
| S3 (15 notes; PDF-checked: D7 Sep 11, A9 Sep 30, D6 + these 12 Oct 1) | A9 (partial), C10 (partial), D7 (substantive); A12 contested | A8, A10, A11, B8, C7, C8, C9, D6, E2, E3, E4 = 11 (+ A12?) |
| S5 | B9 (positive) | — |
| **Total** | 10 or 9 | **25 or 26 of 36 (69–72%)** |

## 3. Decision needed: which coding rule? (the tally depends on it)

The verdict vocabulary has been applied two ways:
- **R2 (Sep 4 harvest):** "partial" includes reviews that **name** the gap without studying it (D1, D2 were coded partial for this).
- **R1 (applied to A9 on Sep 30 and to D6, C7, C8 today):** not-absence only if the source reports **data**, first- or second-hand, on how staff below the rule-setting level receive **AI** governance. Naming the gap, prescribing channels or citing another study's finding count as absence.

Under **R2**, A10 (names the gap, p. 156) and A8 (calls for interviews, p. 607) would also be partial. Under **R1**, the Sep 4 positives need re-checking:
- **B4 Joshi** is a framework with no data; its own note says the attitudes it describes are "the paper's assertions". Under R1 it is likely an absence.
- **D1 and D2** name the gap; under R1 they are absences.

**Recommendation: R1.** It is the rule 2.6 implicitly argues: "contain no account of how staff … receive governance". It is also the one an examiner can check against each paper.

R1 needs a **phase 2**: PDF-check the 6 Sep 4 not-absences (B4, B6, D4, D5, D1, D2) and spot-check the 14 Sep 4 absences. That pass is the same procedure as this log, using the PDFs already in `Group A/B/C/D/E`.

| Rule | Expected tally after phase 2 | Effect on 2.6 |
|---|---|---|
| R1 | likely **~28–29 of 36 (about four in five)**, if B4, D1 and D2 fall to absence; A12 is the open case | Stronger gap claim; the range sentence must name A12 (information governance, executive-reported), not C7/C8 |
| R2 | ~23–24 of 36 (A8 and A10 become partial; C7/C8 absence) | Near the current figure, but the rule must be stated in 3.7 ("naming the gap counts as partial") |

**Do not edit 2.6 ¶2 or 3.7 ¶2 until the rule is decided and, under R1, phase 2 is done.** Both texts currently say "two conceptual audit papers", which this check shows is no longer accurate.

## 4. Other corrections found

- **Claims map K6** cites C8 §4.3.2 for "when guidance is silent, practitioners default … to the metric". The PDF passage is prescriptive and not about practitioners' behaviour. Drop C8 from K6; K6 rests on D4 and D7.
- **Claims map K5** cites A12 p. 167 (CISO, second-hand): ✅ verified ("work around policies"; Intel CISO quote, p. 167).
- **C7 PDF** is a browser print-out without a text layer. Replace it with the publisher PDF (Springer, open access, DOI 10.1007/s11948-021-00319-4) before quoting C7 page numbers (article pages are "Page N of 30").

## 5. Per-note evidence (key passages)

- **C10:** "a package of management consultancy training, capacity-building, documentation, all these support services" (caseworker David, p. 266); "The ability to mute a model or change the threshold has been a major cultural factor in [the] business adoption of this technology" (team leader Jason, p. 273); "the difficult part has been to get the dialogue with the case workers" (data scientist Mark, p. 274); review intervals collect "feedback from application users and from data scientists" (p. 275).
- **C7:** "interviews with software developers indicate that while they consider ethics important in principle, they also view it as an impractical construct that is distant from the issues they face in daily work (Vakkuri et al., 2019)" (PDF p. 3).
- **C8:** worked example is a "hypothetical datasheet" and "template model card" (PDF p. 8); ethnographic interviews are an audit step (PDF pp. 8–9).
- **A12:** quotes at pp. 165, 167, 168 verified in full (see the D6/§2.5 session logs for p. 168).
- **E2:** searches for "individual" (3 hits, none in a research-agenda sense) and "behavio" (2 hits: "promote desirable behavior in the use of data"; "collaborative behavior" between units). No working-tier claim.


---

## 6. Phase 2 — Sep 4 batch under R1 (Oct 1, 2026)

**Rule R1 (Albert, Oct 1):** a governance source counts as giving an account only if it reports **data**, first- or second-hand, on how staff below the rule-setting level receive **AI** governance. Naming the gap, prescribing channels or citing another study's finding counts as documented absence.

**Method:**
- The 20 Sep 4 PDFs were text-extracted on Albert's computer and scanned for empirical-method signals (interview, survey, respondent, participant, case study, focus group, fieldwork).
- Hits were read in context, and the six not-absences were read in their method sections.

| ID | Before | After (R1) | Evidence |
|---|---|---|---|
| B4 Joshi | substantive | **documented absence** | Framework; no method signals. "Employees … bypassing" is the paper's assertion |
| D1 Papagiannidis 2025 | partial | **documented absence** | Review. "Interview" appears only in a reference; it names the gap (pp. 11, 14) |
| D2 Madanchian | partial | **documented absence** | Review; practitioner viewpoints come only through cited studies (e.g. Pant et al. 2024) |
| B6 Lee | substantive | **not-absence (partial)** | Case study with eight AI projects; interviews with team members; teams' feedback reshaped the instrument (PDF p. 4; pp. 14, 33) |
| D4 Nahar | substantive | **substantive** ✓ | Field study (observation, interviews) plus user study with 29 practitioners |
| D5 Ackerman | substantive | **not-absence (partial)** ✓ | Survey of 44 professionals on their organisations' RAI frameworks (pp. 6, 14) |
| 14 Sep 4 absences | absence | **absence** ✓ (signal scan) | No empirical method in any of them. B1's interview mention summarises another paper in its special issue; A6's "case studies" are global initiatives; B3's is an application to ChatGPT; A1's "focus group" is a WHO/ITU body |

⚠ The 14 Sep 4 absences were confirmed by method-signal scan plus context reading, not by a line-by-line claim table. They cannot hide a positive (no data-collection language at all), but their §1–§10 content was not re-verified.

## 7. Final tally under R1

**Not-absence (7):** A9 (partial), B6 (partial), B9 (positive), C10 (partial), D4 (substantive), D5 (partial), D7 (substantive).
**Documented absence (29):** A1, A3, A4, A5, A6, A7, A8, A10, A11, **A12 (borderline)**, B1, B3, B4, B5, B7, B8, C1, C2, C3, C7, C8, C9, D1, D2, D6, E1, E2, E3, E4.

**Tally: 28–29 of 36 (78–81%).** The range is A12: executive-reported user behaviour, on information governance rather than AI governance.

**Applied:**
- 2.6 ¶2 (v1.3): "28 or 29 (78–81%) … receive AI governance; the range reflects one study of information governance whose interviews with executives report users' behaviour at second hand".
- 3.7 ¶2: R1 stated; new reason for the range.
- READMEs updated.
- Notes: an R1 verdict line under §11 in B4, D1, D2, C7, C8, C10, A12, B6, D4, D5.
- Claims map: K6 drops C8.

## 8. C7 publisher PDF (Oct 1, 2026)

Albert replaced the image-only print-out with the Springer PDF (text layer). Re-checked: the Vakkuri-cited developer finding is on p. 3; "Driving re-design" is on p. 16; "interview" occurs only in the cited sentence. **Verdict unchanged: documented absence.** The C7 note block has been updated.
