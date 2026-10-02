# Search Log (PRISMA-lite)

Required by amendment A1 (`claude/LitReview_Process_v2.md`). **No reference enters the corpus without a line in this log.** The methodology chapter cites this file.

**Maintained by:** Liu Yu-Shu (Albert) | **Opened:** Sep 2, 2026

---

## S1 — Original corpus compilation (reconstructed)

| Field | Value |
|---|---|
| Date | July 1, 2026 |
| Method | Web-search compilation (not a structured database query) |
| Databases | **Not recorded for S1 itself.** Partial reconstruction (Oct 1, 2026): the plan written at the end of S1 (`Literature_Review_and_Research_Method_Plan.md` v1, July 2026, §2.4 "Search Strategy Going Forward") names Google Scholar, ScienceDirect, arXiv, AIS eLibrary and ResearchGate. These are the *intended* sources for further searching; whether S1 used all of them is ⚠ **Albert to confirm** |
| Query strings | **Not recorded for S1 itself.** Plan §2.4 lists four core strings: `"generative AI" AND governance AND organization` · `"AI policy" AND "business intelligence"` · `algorithmic accountability AND corporate governance` · `responsible AI adoption AND qualitative`; plus backward snowballing from the five 5/5-rated sources and forward citation search on Przegalinska et al. (2025) and Marvi et al. (2025). ⚠ Same caveat: planned strings, not a record of S1 |
| Hits | 29 sources compiled in six clusters (A 7, B 7, C 6, D 6, E 2, F 1; plan §2.3 "Source Inventory"); 43 bib entries after cluster expansion |
| Kept | Clusters A–F as originally scoped |
| Rejected | Not recorded at the time |

> ⚠ **Known weakness, to be stated in Chapter 3.** This search was not protocol-driven, and its record is partial. It is the origin of the corpus-quality skew identified in risk R3: over-representation of 2024–25 preprints and low-tier venues. Subsequent passes (S2 onward) are protocol-driven and fully logged. Chapter 3 must present S1 honestly as a convenience compilation rather than a systematic search, with S2 as the corrective.

## S2 — Verification and exclusion pass

| Field | Value |
|---|---|
| Dates | Sep 1–2, 2026 |
| Method | DOI/arXiv resolution per Process v2 step 1; venue and indexing checks via Crossref, arXiv API, SCImago, ISSN Portal, publisher records |
| Assessed | All Cluster A–E entries |
| Outcome | 21 usable notes; 3 excluded; 2 grey-tagged |

**Excluded**

| Key | Source | Ground |
|---|---|---|
| `aigovslr2024rg` | A#2, AI Governance SLR (ResearchGate misc) | Not available/reliable; no findable author or venue |
| `govgenai2025amcis` | B#2, Governance of Generative AI (AMCIS 2025) | Author list not locatable |
| `employeeexperiences2025` | D#3, Mitchell (2025), Preprints.org | Non-peer-reviewed; no self-limitations; §8/§10 unverified; **pipeline produced fabricated metadata** — NotebookLM asserted "Sapienza University of Rome" twice, Preprints.org record lists no affiliation (verified Sep 2, 2026) |

**Grey-tagged (background support only, never load-bearing, never sole citation)**

| Key | Source | Ground |
|---|---|---|
| `corpgovageai2025` | C#1, Ganesh et al. (2025), JISEM | SCImago: coverage 2019–2024, "Discontinued in Scopus as of 2024"; this article postdates it; no DOI; no self-stated limitations |
| `aigovalgoacc2026` | C#3, Judijanto et al. (2026), INJOSS | Garuda/aggregator indexing only, not Scopus or WoS; no DOI; corpus size undisclosed; no self-stated limitations |

## S3 — Frequency-ranked snowball gap-fill **[RUN — Sep 11, 2026]**

**Rationale.** Across the 21 compiled notes, the §8 SNOWBALL lists converge on a small set of sources that are consistently published in stronger venues than the corpus itself — particularly in Cluster C, where the references outrank the citing papers. Ranking by how many notes independently name a source gives a corpus-internal signal of the field's core, and simultaneously addresses three defects: Cluster C's collapse to one usable source, Cluster E's single low-tier member, and the missing theoretical lineage behind the chosen spine.

**Method.** Extract §8 entries from all 21 notes; rank by independent citing-note count; resolve DOI/arXiv per Process v2 step 1; Albert makes keep/reject calls; kept items enter the v2 notebook pipeline. Model: Sonnet.

**Inclusion criteria.** (a) Peer-reviewed journal or top-tier conference, or a standards body / national institution; (b) addresses organizational AI or data governance, responsible-AI practice, or IT-governance theory; (c) resolvable DOI or stable identifier.
**Exclusion criteria.** Venues discontinued from Scopus; national-index-only journals; non-peer-reviewed items without a compelling unique contribution; sources already in the corpus.

### Target list

| # | Hits | Source | Venue | Purpose |
|---|---|---|---|---|
| 1 | 4 | Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022) — Defining organizational AI governance / hourglass model | AI and Ethics 2(4); arXiv:2206.00335 | Core definition; ethics-to-practice translation |
| 2 | 3 | Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) — Toward AI governance | Information Systems Frontiers 25(1) | Core; distinct from the JSIS 2025 paper already held |
| 3 | 3 | Lu, Zhu, Xu, Whittle, Zowghi & Jacquet — Responsible AI Pattern Catalogue | ACM Computing Surveys 56(7) | Engineering-level governance patterns |
| 4 | 3 | Mökander, Morley, Taddeo & Floridi (2021) — Ethics-based auditing of automated decision-making systems | Science and Engineering Ethics 27(4) | **Cluster C rebuild** |
| 5 | 2 | **Rakova, Yang, Cramer & Chowdhury (2021) — Where Responsible AI Meets Reality: Practitioner Perspectives** | PACM HCI 5(CSCW1) | **PRIORITY — nearest existing study to the reframed working-tier design; determines whether this thesis is scooped or positioned** |
| 6 | 2 | Birkstedt, Minkkinen, Tandon & Mäntymäki (2023) — AI governance: themes, knowledge gaps, future agendas | Internet Research 33(7) | Core |
| 7 | 2 | Ashok, Madan, Joha & Sivarajah (2022) — Ethical framework for AI and digital technologies | Int. J. Information Management 62 | Core |
| 8 | 2 | Raji et al. (2020) — Closing the AI accountability gap: internal algorithmic auditing | FAT* 2020 | **Cluster C rebuild** |
| 9 | 1 | Shrestha, Ben-Menahem & von Krogh (2019) — Organizational decision-making structures in the age of AI | California Management Review 61(4) | **Cluster C rebuild**; decision-structure link |
| 10 | 1 | Asatiani et al. (2020) — Challenges of explaining black-box AI systems | MIS Quarterly Executive 19(4) | **Cluster C rebuild** |
| 11 | 1 | Tallon, Ramirez & Short (2013) — The information artifact in IT governance | J. Management Information Systems 30 | **Theoretical lineage of the structural/procedural/relational spine** |
| 12 | 1 | Abraham, Schneider & vom Brocke (2019) — Data governance: a conceptual framework | Int. J. Information Management 49 | **Cluster E rebuild** |
| 13 | 1 | Janssen, Brous, Estevez, Barbosa & Janowski (2020) — Data governance: organizing data for trustworthy AI | Government Information Quarterly 37 | **Cluster E rebuild** |
| 14 | 1 | Zhang, Chan, Yan & Bose (2022) — Towards risk-aware AI and ML systems | **Decision Support Systems** 159 | **Cluster E rebuild — genuine BI-family venue** |
| 15 | — | Janssen (2025) — Responsible governance of generative AI: a CAS conceptualization | Policy and Society 44(1) | Previously flagged; possibly closest paper to the original RQ |

**Also carried forward (previously flagged, not yet resolved):** Ulnicane (2025); Khanal, Zhang & Taeihagh (2025); Kongsten & Kathirgamadas (2024, NTNU MSc). And from A3/Ismail: Alan Turing Institute (Leslie et al. 2024, CARE/ACT), Government of Hong Kong SAR (2024, Ethical AI Framework), Barus et al. (2025) — ⚠ bibliographic details not confirmed in the captured transcript; verify against the Ismail2025 PDF reference list before treating as targets.

### S3 outcome (Sep 11, 2026)

All 15 target-list items were resolved via NotebookLM notebook_query (Q1+Q2 protocol) against the source PDF and assigned cluster IDs. **14 kept, notes compiled and committed to `literature/notes/`; raw Q1+Q2 harvest merged into `literature/_raw/<ID>.md`.** `references.bib` updated with all 14 entries (quality tier: all peer-reviewed journal/conference, no grey-tier flags — a marked improvement over S1/S2 corpus quality).

| ID | Bib key | Source | Kept? |
|---|---|---|---|
| A8 | `mantymaki2022definingaigov` | Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022) | ✅ |
| A9 | `papagiannidis2023towardaigov` | Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) | ✅ |
| A10 | `birkstedt2023themesgaps` | Birkstedt, Minkkinen, Tandon & Mäntymäki (2023) | ✅ |
| A11 | `ashok2022ethicalframework` | Ashok, Madan, Joha & Sivarajah (2022) | ✅ |
| A12 | `tallon2013informationartifact` | Tallon, Ramirez & Short (2013) | ✅ |
| B8 | `janssen2025responsiblegenai` | Janssen (2025) | ✅ |
| C7 | `mokander2021auditing` | Mökander, Morley, Taddeo & Floridi (2021) | ✅ |
| C8 | `raji2020closingaccgap` | Raji et al. (2020) | ✅ |
| C9 | `shrestha2019decisionmaking` | Shrestha, Ben-Menahem & von Krogh (2019) | ✅ |
| C10 | `asatiani2020blackbox` | Asatiani et al. (2020) | ✅ |
| D6 | `lu2024raipatterns` | Lu, Zhu, Xu, Whittle, Zowghi & Jacquet (2024) | ✅ |
| D7 | `rakova2021practitionerperspectives` | Rakova, Yang, Cramer & Chowdhury (2021) | ✅ |
| E2 | `abraham2019datagovframework` | Abraham, Schneider & vom Brocke (2019) | ✅ |
| E3 | `janssen2020trustworthyai` | Janssen, Brous, Estevez, Barbosa & Janowski (2020) | ✅ |
| E4 | `zhang2022riskawareai` | Zhang, Chan, Yan & Bose (2022) | ✅ |

**Note on E-cluster renumbering.** With E2–E4 now filled by the S3 rebuild, the E-cluster ID scheme was reset: `E1` = Khandan (2025) (the pre-existing single member, previously numbered informally as "the only entry"), `E2` = Abraham (2019), `E3` = Janssen (2020), `E4` = Zhang (2022). `algobiasbianalytics2025` — previously flagged as the closest topical match but unverifiable ResearchGate content — is formally **EXCLUDED** (see `references.bib`) and is not assigned an E-cluster slot; it is not renumbered into this scheme.

**Cluster totals after S3:** A 11 (6 retained + 5 new), B 8 (7 retained + 1 new), C 7 (3 retained + 4 new — Cluster C rebuild target achieved), D 7 (5 retained + 2 new), E 4 (1 retained + 3 new, plus 1 excluded).

## S4 — Methods foundation for Chapter 3 **[RUN Sep 30, 2026; COMPILED Sep 30, 2026]**

**Trigger:** Chapter 3 had one citable methods source (Castillo-Montoya, I1). The 14 Cluster I sources are interview-design *precedents*, not a methods foundation.
**Method:** targeted search for canonical sources on each method choice the thesis already makes (protocol v0.98, codebook v0, sampling frame); metadata checked on Crossref Sep 30 (books: publisher record). Not systematic — canonical anchors are known in advance; the search confirms bibliographic details.
**New cluster M — Methods foundation.** Outside the §11 denominator.

| Proposed ID | Source | Crossref | Ch.3 job | Priority |
|---|---|---|---|---|
| M1 | Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa | ✓ | Thematic analysis — phases | Must |
| M2 | Braun, V., & Clarke, V. (2021). One size fits all? What counts as quality practice in (reflexive) thematic analysis? *Qualitative Research in Psychology, 18*(3), 328–352. https://doi.org/10.1080/14780887.2020.1769238 | ✓ (online 2020) | **Decides the TA label**: coding-reliability vs codebook vs reflexive. The thesis uses an a priori spine + inductive codes — check which family that is | **Must — read first** |
| M3 | Fereday, J., & Muir-Cochrane, E. (2006). Demonstrating rigor using thematic analysis: A hybrid approach of inductive and deductive coding and theme development. *International Journal of Qualitative Methods, 5*(1), 80–92. https://doi.org/10.1177/160940690600500107 | ✓ | Hybrid deductive + inductive coding = codebook v0 design | Must |
| M4 | Flanagan, J. C. (1954). The critical incident technique. *Psychological Bulletin, 51*(4), 327–358. https://doi.org/10.1037/h0061470 | ✓ | Origin of the incident anchor (Section B) | Must |
| M5 | Butterfield, L. D., Borgen, W. A., Amundson, N. E., & Maglio, A.-S. T. (2005). Fifty years of the critical incident technique: 1954–2004 and beyond. *Qualitative Research, 5*(4), 475–497. https://doi.org/10.1177/1468794105056924 | ✓ | CIT as used in qualitative interviewing today | Must |
| M6 | Yin, R. K. (2018). *Case study research and applications: Design and methods* (6th ed.). SAGE. ISBN 978-1-5063-3616-9 | book (publisher record) | Embedded multiple-case design; depth vs breadth strata | Must — **book: need library e-book chapters** |
| M7 | Nowell, L. S., Norris, J. M., White, D. E., & Moules, N. J. (2017). Thematic analysis: Striving to meet the trustworthiness criteria. *International Journal of Qualitative Methods, 16*(1). https://doi.org/10.1177/1609406917733847 | ✓ | Trustworthiness (Lincoln & Guba criteria applied to TA) | Must |
| M8 | Malterud, K., Siersma, V. D., & Guassora, A. D. (2016). Sample size in qualitative interview studies: Guided by information power. *Qualitative Health Research, 26*(13), 1753–1760. https://doi.org/10.1177/1049732315617444 | ✓ | Justifies n = 14 without "saturation" | Must |
| M9 | Temple, B., & Young, A. (2004). Qualitative research and translation dilemmas. *Qualitative Research, 4*(2), 161–178. https://doi.org/10.1177/1468794104044430 | ✓ | Bilingual researcher-as-translator; fixed-wording card | Should |
| M10 | Dwyer, S. C., & Buckle, J. L. (2009). The space between: On being an insider-outsider in qualitative research. *International Journal of Qualitative Methods, 8*(1), 54–63. https://doi.org/10.1177/160940690900800105 | ✓ | Reflexivity: participants are personal contacts / former colleagues | Should |

**Considered, not taken:** Eisenhardt (1989) — theory-building from cases, not needed alongside Yin (Crossref rate-limited, not rechecked); Lincoln & Guba (1985) *Naturalistic Inquiry* — book, reached through M7; Braun & Clarke (2022) *Thematic Analysis: A Practical Guide* — book; take only if M2 leaves the label unresolved.

**Substitutions (Sep 30, 2026, Albert):** PDFs for M4 and M6 not accessible.
- **M4 Flanagan (1954) → Gremler, D. D. (2004).** The critical incident technique in service research. *Journal of Service Research, 7*(1), 65–89. https://doi.org/10.1177/1094670504266138 (Crossref ✓). Flanagan cited only as "Flanagan (1954, as cited in Gremler, 2004)" and not listed in the references.
- **M6 Yin (2018) → Baxter, P., & Jack, S. (2008).** Qualitative case study methodology: Study design and implementation for novice researchers. *The Qualitative Report, 13*(4), 544–559. https://doi.org/10.46743/2160-3715/2008.1573 (Crossref ✓; Crossref year 2015 = DOI registration), **plus M11 Eisenhardt, K. M., & Graebner, M. E. (2007).** Theory building from cases: Opportunities and challenges. *Academy of Management Journal, 50*(1), 25–32. https://doi.org/10.5465/amj.2007.24160888 (Crossref ✓). Known weakness: "embedded multiple-case design" is Yin's term; the thesis reaches it through Baxter & Jack.

**PDF verification, compile (Sep 30, 2026).** All 11 PDFs read from `Thesis Content/Group M/`, one NotebookLM notebook each, variant v2.4-T (Query 1; Query 2 = §7–§10 + §13 with (f); no §11, no §12). Quotes string-matched to the PDF text; printed pages used, not NotebookLM's. Notes in `literature/notes/`, raw answers and verification logs in `literature/_raw/`.

| ID | Result of the PDF check |
|---|---|
| M1 Braun & Clarke 2006 | ✅ DOI. Metadata confirmed. Fixed NotebookLM misquotes (Ryan & Bernard "after analysis", p.86; "a simple thematic analysis", p.97; "disjuncture" passage pp.85–86; Table 2 typo "all each theme" kept as [sic]). |
| M2 Braun & Clarke 2021 | ✅ DOI. Metadata confirmed. **Label decision: codebook TA, not reflexive TA** (a priori spine, codebook, solo coding with re-coding after an interval, supervisor sample check). NotebookLM's claim about a priori codes plus re-coding was dropped as not in the paper; the paper has no limitations section, only self-caveats. |
| M3 Fereday & Muir-Cochrane 2006 | ✅ PDF+venue. **No DOI printed** (`doi-not-in-pdf`). "Article 7" is not in the PDF. Pages = PDF page + 79. |
| M4 Gremler 2004 | ✅ DOI. Scan with no text layer; all 25 pages OCR'd, quotes located by word-sequence similarity. Two Bitner definitions kept separate (pp.66, 75); "27 publications" was wrong (27 conference papers); Flanagan "described", not "defined" (p.76). |
| M5 Butterfield et al. 2005 | ✅ DOI. **DOI is …056924** (NotebookLM gave …056922). Text layer degraded; matched on letters only. Inclusion-criteria quote uses the PDF wording (p.488); McLeod quote prints "qualification" [sic]. |
| M6 Baxter & Jack 2008 | ✅ DOI. Yin is cited there as Yin (2003) with one reference entry (3rd ed., p.558); Yin's typology may only be cited "as cited in Baxter & Jack". |
| M7 Nowell et al. 2017 | ✅ DOI. Printed page = PDF page. **Bib gained `pages = {1--13}`**; the PDF prints "Volume 16: 1–13" and no issue number (issue 1 is from Crossref). |
| M8 Malterud et al. 2016 | ✅ DOI. Implications passage p.1759 (not p.1760); the paper gives no minimum N. |
| M9 Temple & Young 2004 | ✅ DOI. Text layer degraded; matched on letters only. Researcher/translator passage p.168. |
| M10 Corbin Dwyer & Buckle 2009 | ✅ PDF+venue. **No DOI printed.** Albert replaced the first M10 PDF (a different paper) and the note was re-run on the correct one. Author form normalised to "Corbin Dwyer, Sonya" in the bib. No corpus or time span stated (NotebookLM's 1984–2007 was dropped). |
| M11 Eisenhardt & Graebner 2007 | ✅ PDF+venue. **No DOI printed.** NotebookLM's pages were one page early throughout; the (f) sampling quote is reordered in NotebookLM's version (PDF: "so too are cases sampled…"). The "MUST DO / MUST AVOID" framing is NotebookLM's. |

**Result:** 11 of 11 verified and compiled; `TODO-verify` removed from all eleven bib entries. `flanagan1954cit` and `yin2018casestudy` stay NOT OBTAINED. Eisenhardt & Graebner (M11) was added Sep 30 as the multiple-case source alongside M6 (it was "considered, not taken" above, before Yin was lost). No notebooks were created for Flanagan or Yin.

## S5 — Targeted add-reference pass: Chapter 1 BI context and Chapter 2 theory anchors **[RUN Sep 29, 2026; COMPILED Sep 29, 2026]**

*Entry added Oct 1, 2026 (retrospective, from `planning/ch2_targeted_search_2026-09-29.md`, `planning/s5_addref_prompt.md` and `planning/Pipeline_State.md`). The pass was run and compiled on Sep 29 but not logged here at the time.*

| Field | Value |
|---|---|
| Date | Sep 29, 2026 |
| Trigger | Chapter 1 needed BI-context sources; Chapter 2 (loop structure, adopted Sep 29) needed theory anchors for bypass (2.2) and upward voice (2.3); claim K5 needed a check for empirical Shadow AI studies outside the corpus |
| Method | Targeted web search (not a database query); metadata checked against Crossref (`api.crossref.org/works/<DOI>`), except G3 (DOI from the publisher page; Crossref rate-limited). Exact query strings were not recorded |
| Candidates listed | 6 targets + 3 candidates seen |
| Kept | 6 (all PDF-verified and compiled, Sep 29) |
| Rejected | *Digital shadow AI risk theory (DART)*, Technological Forecasting & Social Change (2026) — not screened (held in reserve if B9 proved thin); practitioner blogs and vendor reports on shadow AI — not academic; IAEME / low-tier "GenAI for BI" papers — venue |

| ID | Bib key | Source | Role | Variant |
|---|---|---|---|---|
| B9 | `silic2025shadowai` | Silic, Silic & Kind-Trüller (2025), *Strategic Change*, 10.1002/jsc.2682 | Governance literature; K5 scoop-or-position check (verdict: **position**) | v2.4 full, **with §11** (denominator 35 → 36) |
| E5 | `ain2019bisuccess` | Ain, Vaia, DeLone & Waheed (2019), *Decision Support Systems* 125, 113113 | Ch.1 BI context | v2.4-T (no §11) |
| E6 | `gu2024analystsverify` | Gu, Shang, Althoff, Wang & Drucker (2024), CHI '24, 1–22 | Ch.1 BI context | v2.4-T |
| G1 | `haag2017shadowit` | Haag & Eckhardt (2017), *BISE* 59(6), 469–473 | Ch.2 anchor (shadow IT) | v2.4-T |
| G2 | `morrison2023voicesilence` | Morrison (2023), *Annual Review of Org. Psych. & Org. Behavior* 10, 79–107 | Ch.2 anchor (voice and silence) | v2.4-T |
| G3 | `dutton1993issueselling` | Dutton & Ashford (1993), *Academy of Management Review* 18(3), 397–428 | Ch.2 anchor (issue selling) | v2.4-T; no DOI printed in the PDF |

**PDF verification (Sep 29).** Every quote, typology and page checked against the PDF (B9 and G3 by OCR). NotebookLM errors found in all six: a fabricated attribution (B9), wrong proposition number and count (G3), a spliced quote (G2), policy framing not in the paper (E6), altered quotes (G1). B9 is internally inconsistent on its interview count (abstract/introduction ten, body and Table 1 eight; cite eight). `TODO-verify` removed from all six bib entries. New **Cluster G — organisation theory anchors (non-AI)**. Bib total 64.

**§11 tally after S5:** documented absence in 22–24 of 36 governance notes (B9 counted positive; confirmed by Albert Sep 29–30). E5, E6 and G1–G3 are outside the denominator.

---

## S6 — Supervisor-suggested sensemaking sources **[RUN Oct 2, 2026; COMPILED Oct 2, 2026]**

| Field | Value |
|---|---|
| Date | Oct 2, 2026 |
| Source of leads | Supervisor's suggestion of sensemaking as a second lens, plus the reference list of Balasooriya & Sedera (2026). The sensemaking lens was adopted on the supervisor's suggestion on Oct 2, 2026. Not a database query; no query strings |
| Method | Seven PDFs supplied by Albert (`Thesis Content/Group G`); one NotebookLM notebook per PDF; printed title and authors matched to the plan's IDs in a Step 0 table that Albert approved before anything was written. The plan's IDs and metadata were treated as claims, not records |
| Variant | v2.4-T for all seven: Query 1 = §1–§6 plus zh-TW summary; Query 2 = §7–§10 then §13 THESIS ANCHOR. **§11 and §12 not run** |
| Kept | 7 of 7 (PDF-verified and compiled) |
| Rejected | None. Weick (1995), the book, was deliberately not added (not in hand; the plan lists the 2005 article). |

| ID | Bib key | Source | Role | Verification |
|---|---|---|---|---|
| G4 | `weick2005organizing` | Weick, Sutcliffe & Obstfeld (2005), *Organization Science* 16(4), 409–421 | Sensemaking, the construct | Text layer; DOI printed. No limitations section; three passing caveats |
| G5 | `maitlis2014sensemaking` | Maitlis & Christianson (2014), *Academy of Management Annals* 8(1), 57–125 | Review of the field | Text layer; DOI printed (10.1080/…, not the plan's 10.5465/…). Scope bounds pp.59–60 |
| G6 | `gioia1991sensemaking` | Gioia & Chittipeddi (1991), *SMJ* 12(6), 433–448 | Sensegiving; stakeholder feedback | JSTOR two-column scan read with `pdftotext -raw`; no DOI printed. Three self-stated caveats (pp.435–436, 444, 445) |
| G7 | `balogun2005changerecipient` | Balogun & Johnson (2005), *Organization Studies* 26(11), 1573–1601 | Change recipients' lateral sensemaking | **No text layer; OCR (tesseract 4.1.1), quotes checked in OCR text only.** DOI printed. One scope caveat p.1597 |
| G8 | `balasooriya2026sensemaking` | Balasooriya & Sedera (2026), *Business Strategy and the Environment* 35(6), 7916–7931 | Sensemaking applied to AI integration | Text layer; DOI printed; issue number from the notebook. Two stated limitations p.7926. The paper's "Weick and Weick (1995)" is an error and was not reproduced |
| G9 | `balogun2004restructuring` | Balogun & Johnson (2004), *AMJ* 47(4), 523–549 | Middle managers' schema change | Text layer; no DOI printed. Four stated limitations p.546 |
| G10 | `rouleau2005micropractices` | Rouleau (2005), *JMS* 42(7), 1413–1441 | Micro-practices of sensemaking and sensegiving | Text layer; DOI is a watermark only. Three stated limitations pp.1436, 1438 |

**PDF verification (Oct 2).** Every quote, limitation and typology was matched to the PDF text; printed page = PDF page + 408 (G4), 56 (G5), 431 (G6), 1572 (G7), 7915 (G8), 522 (G9), 1412 (G10). NotebookLM errors found: wrong page numbers in several of the seven answers; an "eight properties" claim for Weick et al. (the paper has seven headed properties); a 12-month span for G7 (the paper tracks about 16 months, March 1993 to July 1994); the guided/fragmented/restricted/minimal typology attributed to G5 (it is Maitlis 2005, reported by G5); a "hold-out informant" in G6 that is not in the PDF; unchecked data-corpus page counts for G9 (not used). Two of my own first-pass verification entries were corrected after a re-check (G6 and G7 do state caveats). G7 and G9 draw on the same case and are not independent. Crossref was not reachable from the session, so no DOI was taken from outside a PDF.

**Orchestration review (Oct 2, 2026):** quotes in all seven notes re-checked against the PDFs (G7 by fresh OCR of pp.1574, 1595–1597); all found. Corrections: G6 DOI 10.1002/smj.4250120604 and G9 DOI 10.2307/20159600 added from Crossref (not printed in the PDFs); G8 issue 6 confirmed in the PDF download stamp; G4 "naïve" as printed.

**§11 tally after S6:** unchanged at 28–29 of 36 (78–81%) under R1. G4–G10 are outside the denominator. Governance corpus unchanged at 36. Cluster G: 3 → 10. Bib total 84.

---

## Log conventions

Each subsequent search adds a numbered section recording: date, database, exact query string, filters, hits, screened, kept, and rejected-with-reason. Snowball entries record the citing note as the source of the lead.
