# S3 Gap-Fill — process the 15 snowball PDFs

**Purpose:** run all 15 frequency-ranked snowball sources through Literature Review Process v2 under **query template v2.4** — verify, create one NotebookLM notebook each, run the two-query template, and log every source in `literature/search_log.md` as pass S3.
**Model:** Sonnet. **Created:** Sep 10, 2026 (updated same day — the full set of 15 is now in place). **Status:** not yet run.
**Prerequisite reading:** `planning/query_template_v2.4.md` (the complete standalone template), `planning/LitReview_Process_v2.md`, `planning/Pipeline_State.md`.

---

## Why these 15

They were selected by ranking the §8 SNOWBALL lists across all 21 governance notes by how many notes independently cite each source. In Cluster C the references consistently outrank the papers citing them, and Clusters C and E cannot currently carry a chapter section — C has one fully usable source plus two grey-tagged, E has one low-tier source. Cluster loading below is therefore deliberate: **5 into A, 4 into C, 3 into E, 2 into D, 1 into B**.

⚠ These are **v2.4 governance sources**: Query 2 ends with **§11 WORKING-TIER RECEPTION**, not §12. §12 is for the interview-methodology cluster only.

## The files — already in place

All under `D:\Master\Thesis\Thesis Content\`, filed into the Group folders.

| Proposed ID | PDF (folder / filename) | Source | Venue |
|---|---|---|---|
| A8 | `Group A/Defining organizational AI governance.pdf` | Mäntymäki, Minkkinen, Birkstedt & Viljanen (2022) | *AI and Ethics* 2(4) — DOI 10.1007/s43681-022-00143-x ✅ confirmed |
| A9 | `Group A/Toward AI Governance - Identifying Best Practices and Potential Barriers and Outcomes.pdf` | Papagiannidis, Enholm, Dremel, Mikalef & Krogstie (2023) | *Information Systems Frontiers* 25(1) |
| A10 | `Group A/AI Governance - Themes, Knowledge Gaps, Future Agendas.pdf` | Birkstedt, Minkkinen, Tandon & Mäntymäki (2023) | *Internet Research* 33(7) |
| A11 | `Group A/Ethical Framework for AI and Digital Technologies.pdf` | Ashok, Madan, Joha & Sivarajah (2022) | *Int. J. Information Management* 62 |
| A12 | `Group A/The Information Artifact in IT Governance - Toward a Theory of Information Governance.pdf` | Tallon, Ramirez & Short (2013) | *J. Management Information Systems* 30 — **theoretical lineage of the thesis spine** |
| C7 | `Group C/Ethics-Based Auditing of Automated Decision-Making Systems.pdf` | Mökander, Morley, Taddeo & Floridi (2021) | *Science and Engineering Ethics* 27(4) |
| C8 | `Group C/Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf` | Raji et al. (2020) | FAT* 2020 |
| C9 | `Group C/Organizational Decision-Making Structures in the Age of AI.pdf` | Shrestha, Ben-Menahem & von Krogh (2019) | *California Management Review* 61(4) |
| C10 | `Group C/Challenges of Explaining the Behavior of Black-Box AI Systems.pdf` | Asatiani et al. (2020) | *MIS Quarterly Executive* 19(4) |
| D6 | `Group D/Responsible AI Pattern Catalogue - A Collection of Best.pdf` | Lu, Zhu, Xu, Whittle, Zowghi & Jacquet | *ACM Computing Surveys* 56(7) |
| D7 | `Group D/Where Responsible AI Meets Reality-Practitioner Perspectives.pdf` | Rakova, Yang, Cramer & Chowdhury (2021) | *PACM HCI* 5(CSCW1) — DOI 10.1145/3449081 ✅ confirmed. **PROCESS FIRST** |
| E2 | `Group E/Data governance - A conceptual framework, structured review, and research agenda.pdf` | Abraham, Schneider & vom Brocke (2019) | *Int. J. Information Management* 49 |
| E3 | `Group E/Data governance - Organizing data for trustworthy Artificial Intelligence.pdf` | Janssen, Brous, Estevez, Barbosa & Janowski (2020) | *Government Information Quarterly* 37 |
| E4 | `Group E/Towards risk-aware artificial intelligence and machine learning systems - An overview.pdf` | Zhang, Chan, Yan & Bose (2022) | ***Decision Support Systems*** 159 — genuine BI-family venue |
| B8 | `Group B/Responsible governance of generative AI - conceptualizing GenAI as complex adaptive systems.pdf` | Janssen (2025) | *Policy and Society* 44(1), 38–51 — open access, https://academic.oup.com/policyandsociety/article/44/1/38/7965776 |

⚠ **B8 author check.** Earlier notes recorded this as "Janssen 2025" (single author), surfaced as a snowball lead from `taeihagh2025govgenai`. Verify the full author list against the Oxford Academic article page before writing the bib entry — do not carry the single-author assumption forward. It was flagged in `Pipeline_State.md` as *"possibly the closest paper to the original RQ"*, so its §7 and §11 answers matter more than most.

### ID assignment — verify before using

The proposed IDs above skip gaps deliberately: A2 and B2 are excluded, D3 (Mitchell) is excluded, and bib keys `algoopacity`, `algoacccrosscultural2026`, `algoaccliability2025` occupy Cluster C conceptually without having notes. B8 continues the B note sequence (B1, B3–B7 exist; B2 is excluded). **Before creating notebooks, check both `literature/notes/` filenames and `references.bib` keywords for collisions, and report the final ID mapping to Albert.** Note-numbering and bib-entry numbering have drifted apart in Cluster E in particular (the note labelled `[E1]` is Khandan, while bib `E1` is the unverified `algobiasbianalytics2025`) — flag this rather than silently renumbering.

## Procedure — per source

1. **Verify.** Resolve DOI or arXiv ID; confirm title, authors and year against the **publisher record**, not the PDF alone. Then check **venue standing** (SCImago for Scopus coverage and any discontinuation, ISSN Portal, national indexes where relevant) and assign a quality tier. No verification, no notebook. Flag anything unresolvable to Albert rather than guessing — the A2 / B2 / Mitchell precedent applies.
2. **Create one NotebookLM notebook per reference**, named `[A8] Mantymaki2022 — Defining Organizational AI Governance` style, with only that PDF as source. File it into the `Thesis ref summary` set (or per-cluster collections).
3. **Run template v2.4**, two queries in the same chat, exactly as written in `planning/query_template_v2.4.md`:
   - Query 1 → §1–§6 (§5 in its v2.4 practitioner-encounter wording) + the zh-TW summary.
   - Query 2 → §7 (Phase 1 = **Policy Encounter & Interpretation**), §8 (v2.4 practitioner-first scope), §9, §10, **§11 WORKING-TIER RECEPTION**.
   - Do **not** use v2.2 wording. Do **not** run §12 on these.
   - Every point carries section + page. Apply the **Unclear-point resolution rule (v2.3)**.
   - ⚠ Treat §6 output as a claim to verify, never as verified metadata.
4. **Route §8 output** into `literature/search_log.md` as snowball leads — do not create notebooks for them without Albert's keep decision.
5. **Then PAUSE.** Tell Albert the notebooks are ready; he asks his own extra questions before compilation.

## On compilation (after Albert says "compile")

- Export each notebook's full chat; write one note per reference to `literature/notes/` in v2.4 format (11 sections, every point location-tagged, plus an "Albert's Questions" section).
- Update `references.bib`: complete metadata, verification method and date in `note`, quality tier in `keywords`.
- Add pass **S3** to `literature/search_log.md` with a line per source: date, how verified, venue standing, kept/rejected with reason, and the citing notes that surfaced it as a snowball lead.
- Regenerate `literature/reference_list.md`.
- Update `planning/Pipeline_State.md` — corpus counts, cluster health table, and the §11 tally.

### ⚠ The §11 tally must be reported separately

The current headline finding is **14 of 20 governance sources contain no account of how anyone below management experiences governance**. These 15 new sources change that denominator, taking the governance corpus to 35. Report the new split as *both* figures — the original 20-source corpus and the expanded 35-source corpus — and do **not** silently merge them. Rakova (D7) in particular is a practitioner-perspectives study and will almost certainly come back substantive; that is informative, not a problem, but it must be visible as a change rather than buried in a new total.

Note also that these 15 were selected **because** other papers cite them — a corpus assembled by snowballing from sources that mostly ignore the working tier is not a random sample, and if the absence rate stays high across them that is a stronger result than the original 14/20, not merely a repeated one. Say which way it moved.

## Housekeeping in `Thesis Content`

Report these to Albert; do not delete without his say-so:

- `Defining Organizational AI Governance.pdf` exists **twice** — at the folder root and in `Group A/`, same size. The root copy is a duplicate.
- `~$re_AI_Governance_Reference_List.docx` is a Word lock/temp artefact.
- `references.bib` and `Literature_Review_and_Research_Method_Plan.md` sit at the `Thesis Content` root as **stale copies** — the repo versions are canonical (amendment A4). The root `references.bib` is older than the repo's and must not be edited or used.

## Copy-paste prompt for the Sonnet session

```
Read planning/s3_gapfill_prompt.md, planning/query_template_v2.4.md,
planning/LitReview_Process_v2.md and planning/Pipeline_State.md in my repo, then run the
S3 gap-fill pass for the 15 new snowball PDFs.

Setup: connect to my folders "D:\Master\Thesis\Thesis Content" (PDFs) and
"D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo clone).
NotebookLM is available via the notebook MCP; if auth is stale I'll run `nlm login`.

The 15 files and their proposed IDs are listed in the prompt file. Process
"Group D/Where Responsible AI Meets Reality-Practitioner Perspectives.pdf" (Rakova et al. 2021)
FIRST and tell me what it contains before doing the rest -- it is the closest published study to
my reframed working-tier design and I need to know whether it scoops or positions my thesis.

For each source: verify DOI/arXiv against the publisher record AND check venue indexing standing,
then create one NotebookLM notebook per reference filed into 'Thesis ref summary', then run
template v2.4 as two queries in the same chat -- Query 2 ends with section 11 WORKING-TIER
RECEPTION, NOT section 12. Do not use the v2.2 wording. Every point carries section + page.

Before creating notebooks, check literature/notes/ and references.bib for ID collisions and
report the final ID mapping to me.

Then PAUSE -- do not compile. I will ask my own extra questions in each notebook first.

When I say "compile": write one v2.4 note per reference to literature/notes/, update
references.bib with verified metadata and quality tiers, add pass S3 to literature/search_log.md
with a line per source, regenerate literature/reference_list.md, and update
planning/Pipeline_State.md. Report the section 11 tally as TWO figures -- the original 20-source
corpus and the expanded 35-source corpus -- do not merge them silently, and say which way the
absence rate moved.

Also verify the author list for B8 (Janssen 2025, Policy and Society) against the Oxford Academic
article page -- my earlier notes assumed a single author and that may be wrong.

Also report the housekeeping items you find in Thesis Content; don't delete anything.

Do not commit; I push to GitHub myself.
```
