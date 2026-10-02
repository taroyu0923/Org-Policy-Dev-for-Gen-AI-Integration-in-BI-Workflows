# S6 Add-Reference Pass — sensemaking sources (supervisor-suggested)

**Purpose:** run the 7 sensemaking PDFs now in `Group G/` through Literature Review Process v2. For each one: verify it against the PDF and the publisher, create one NotebookLM notebook, run the queries below, then write raw answers, notes and bib entries into the repo.
**Model:** Sonnet. **Created:** Oct 2, 2026 (orchestration session). **Status:** not yet run.
**Why:** on Oct 2, 2026 the supervisor (Yong Liu) suggested organisational sensemaking theory and sent Balasooriya & Sedera (2026). Albert agreed to add sensemaking as a **second lens** for Chapter 2.6:
- the structural / procedural / relational typology describes *what* governance reaches practitioners;
- sensemaking describes *how* they read it and act on it;
- sensegiving describes *what goes back up*.
**Prerequisite reading:** `planning/s5_addref_prompt.md` (**the precedent: same process, same v2.4-T variant**), `planning/query_template_v2.4.md`, `planning/naming_convention.md`, `literature/search_log.md` §S5.

---

## The 7 sources — proposed IDs (a plan, not a record)

**No bib entries exist yet** (checked Oct 2). Add new entries; check for key collisions first.

| Proposed ID | Proposed bib key | Source (to be confirmed against the PDF) | PDF in `Group G/` | Priority |
|---|---|---|---|---|
| G4 | `weick2005sensemaking` | Weick, Sutcliffe & Obstfeld (2005), *Organization Science* 16(4), 409–421, 10.1287/orsc.1050.0133 | `Organizing and the Process of Sensemaking.pdf` | Must |
| G5 | `maitlis2014sensemaking` | Maitlis & Christianson (2014), *Academy of Management Annals* 8(1), 57–125, 10.5465/19416520.2014.873177 | `Sensemaking in Organizations - Taking Stock and Moving Forward.pdf` | Must |
| G6 | `gioia1991sensegiving` | Gioia & Chittipeddi (1991), *Strategic Management Journal* 12(6), 433–448, 10.1002/smj.4250120604 | `Sensemaking and sensegiving in strategic change initiation.pdf` | Must |
| G7 | `balogun2005recipient` | Balogun & Johnson (2005), *Organization Studies* 26(11), 1573–1601 | `From Intended Strategies to Unintended Outcomes - ….pdf` | Must |
| G8 | `balasooriya2026sensemakingai` | Balasooriya & Sedera (2026), *Business Strategy and the Environment* 35, 7916–7931, 10.1002/bse.70571 | `Bus Strat Env - 2026 - Balasooriya - ….pdf` | Must (supervisor's paper) |
| G9 | `balogun2004middlemanager` | Balogun & Johnson (2004), *Academy of Management Journal* 47(4), 523–549 | `Organizational Restructuring and Middle Manager Sensemaking.pdf` | Optional |
| G10 | `rouleau2005microsensemaking` | Rouleau (2005), *Journal of Management Studies* 42(7), 1413–1441 | `Micro-Practices of Strategic Sensemaking and Sensegiving - ….pdf` | Optional |

Volumes, pages and DOIs above come from memory and web search. **They are claims until checked against the PDF and the publisher page.** Next free numbers: G4 onward (G1–G3 exist). Re-check `literature/notes/` before writing.

**Order:** Must first (G4 → G8), then Optional (G9, G10). If time runs short, stop after G8 and report.

**Not in this pass:** Weick (1995), *Sensemaking in Organizations* (book). Albert does not have it, so G4 and G5 carry Weick's ideas. Do not cite the book from secondary mentions.

## Known PDF issues (checked Oct 2)

- **G7 Balogun & Johnson 2005 has NO text layer** (29 pages; pdftotext returns 0 words). OCR it (tesseract, 300 dpi) before checking any quote. If NotebookLM cannot read it, record that in `_raw/G7.md` and work from the OCR text.
- **G4's PDF metadata title is junk** ("C:JFORSC-4ORSC0133.DVI"). Use the printed title.
- **G5 is 70 pages.** It is a single review article, not a book. Its page offset needs care.
- **G8 is already partly checked** (orchestration session, Oct 2). Printed page = PDF page + 7915.
  - 10 interviews, CEOs / directors / managers, two Australian manufacturing firms: Table 1, p. 7920.
  - Sensemaking as "sensitizing concept", "interpret, frame, and act upon the ambiguities": p. 7923.
  - Limitation "potentially overlooking the tensions, failures, or resistance": p. 7926.
  - ⚠ G8 cites "Weick and Weick (1995)". This is a citation error in the paper; do not reproduce it.

## Variant — v2.4-T for all seven (as G1–G3 in S5)

These are **theory anchors, not governance literature**. Do **NOT** run §11; they stay outside the §11 denominator. The tally is settled at 28–29 of 36 and must not change.

- **Query 1:** §1–§6 exactly as in `query_template_v2.4.md`, plus the zh-TW summary.
- **Query 2:** §7–§10 as in v2.4, then **§13 THESIS ANCHOR**. Use the wording in `s5_addref_prompt.md`, with the [ROLE] and [FOCUS] below.

| ID | [ROLE] | [FOCUS] |
|---|---|---|
| G4 | Chapter 2.6 theory anchor (second lens: sensemaking) | definition of sensemaking; cues, ambiguity and plausibility; how sensemaking turns into action; the link between organising and sensemaking |
| G5 | Chapter 2.6 theory anchor (review of the sensemaking field) | definitions of sensemaking and sensegiving; triggers (ambiguity, uncertainty, violated expectations); who makes sense (leaders, middle managers, employees); prospective vs retrospective sensemaking; research gaps the authors name |
| G6 | Chapter 2.5 / 2.6 theory anchor (sensegiving, the upward half) | definitions of sensemaking and sensegiving; how sense is given and received during strategic change; the four phases; the role of those below top management |
| G7 | Chapter 2.6 theory anchor (change recipients) | how change recipients make sense of intended change; lateral (peer) sensemaking; how intended and unintended outcomes arise; the role of conversation, rumour and stories |
| G8 | Chapter 2.6 example (sensemaking applied to AI integration) | how sensemaking is used as a sensitising concept for AI integration; the four strategies; the sample (who was interviewed); stated limitations |
| G9 | Chapter 2.6 theory anchor (middle managers as recipients) | how middle managers make sense of change imposed from above; social processes (conversation, peers); schema change; the move from top-down to lateral sensemaking |
| G10 | Chapter 2.5 / 2.6 theory anchor (interpreting and passing on change) | how middle managers interpret change and sell it on; micro-practices of sensemaking and sensegiving; tacit knowledge; the link to issue selling |

## ⚠ Fabrication guard (D7 / D6 precedent)

Compiled notes have contained content that is not in the paper (D7: an invented limitations section and typology; D6: an invented champion pattern). Therefore:

- §9 and §13(e) limitations: **verbatim quotes only**, each checked against the PDF page. "None stated" is a valid answer.
- Every typology, phase model, framework name or count must be findable in the PDF at the cited page. Example: Gioia & Chittipeddi's phases. Drop anything you cannot locate, and say so in the note.
- §6 metadata from NotebookLM is a claim, not verification. Check it against the publisher page.
- Do not attribute this study's own terms to these authors, as happened with "lateral voice" and Morrison in G2. Terms to watch: "working rule", "carriers / recipients", "receiving end".

## Delivery and persistence (same as S5)

- **Outputs go into the repo** at exact paths:
  - `literature/notes/<ID>_<firstauthor><year>_<slug>.md`
  - `literature/_raw/<ID>.md`
  - `literature/references.bib` (new entries)
  - `literature/search_log.md` (new section **§S6 — Supervisor-suggested sensemaking sources**, after §S5)
  - `literature/reference_list.md`
  - `planning/Pipeline_State.md`
- **No zips and no downloads.** Do not commit or push; Albert pushes himself.
- `_raw/<ID>.md`: write Q1 the moment it returns, and append Q2 the moment it returns. Compile only from these files.
- Do not delegate querying to a subagent that returns content.
- **Step 0:** before writing, ask each notebook for its source's printed title and authors, match each to its PDF, and send Albert the ID table for approval.

## Naming

Suggested filenames; confirm the slugs against the printed titles:

```
G4_weick2005_organizing_process_sensemaking.md
G5_maitlis2014_sensemaking_taking_stock.md
G6_gioia1991_sensemaking_sensegiving_strategic_change.md
G7_balogun2005_change_recipient_sensemaking.md
G8_balasooriya2026_sensemaking_ai_sustainability.md
G9_balogun2004_middle_manager_sensemaking.md
G10_rouleau2005_micropractices_sensemaking_sensegiving.md
```

Notebook names follow the `[G4] Weick2005 — Organizing and the Process of Sensemaking` style, with one PDF per notebook.

## After compile

- **`references.bib`:** new entries with status, verification method and date, and quality tier (all peer-reviewed journal articles). Mark ✅ only when checked against the PDF.
- **`reference_list.md`:** regenerate and update the summary counts.
- **`Pipeline_State.md`:**
  - Cluster G = 3 → 10 (or 8 if the optional pair is skipped).
  - Governance corpus unchanged at 36; §11 tally unchanged.
  - Add a line recording the decision: sensemaking is the second lens (supervisor, Oct 2).
- **`search_log.md` §S6:** source = supervisor suggestion plus Balasooriya's reference list (Gioia & Chittipeddi and Maitlis are cited there); date; seven PDFs; per-source verification lines.
- **Do not edit any chapter.** The 2.6 and 3.4 text is drafted in a later session, after the supervisor meeting.

---

## Copy-paste prompt for the Sonnet session

```
Read planning/s6_addref_prompt.md in my repo first, then planning/s5_addref_prompt.md (the
precedent -- same process), planning/query_template_v2.4.md and planning/naming_convention.md.

Setup: connect "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" (repo) and
"D:\Master\Thesis\Thesis Content" (PDFs). Use the device shell where it can mount the folders;
otherwise use the file listing/staging/commit tools. NotebookLM is available via the notebook
MCP; if auth is stale I'll run `nlm login`. Do not commit or push; I push myself.

The 7 sensemaking PDFs are in "Thesis Content\Group G" (G1-G3 already exist; new IDs start at G4).

STEP 0: create one notebook per PDF, ask each notebook for its source's printed title and
authors, match them to the PDFs, and send me the ID table for approval BEFORE writing anything.
The IDs and metadata in the prompt file are a plan, not a record.

All seven use variant v2.4-T: Query 1 as normal, Query 2 = sections 7-10 then section 13
THESIS ANCHOR with the per-source focus line from the prompt file. Do NOT run section 11 --
these are theory anchors, outside the section 11 denominator; the tally (28-29 of 36) must not
change. Order: G4-G8 first, then G9-G10.

G7 (Balogun & Johnson 2005) has no text layer -- OCR it before checking any quote.

Write every answer to literature/_raw/<ID>.md the moment it returns (Q1 written, Q2 appended).
Limitations, typologies and phase models: verbatim, each checked against the PDF page -- "none
stated" is fine. Do not attribute this thesis's own terms (working rule, carriers/recipients) to
these authors. Do not supply anything you cannot find in the PDF.

Then PAUSE -- I will ask my own questions in each notebook before you compile.

When I say "compile": write the notes, add the new bib entries (no duplicates), add a section
S6 to literature/search_log.md, regenerate literature/reference_list.md, update
planning/Pipeline_State.md (Cluster G count; governance corpus and section 11 tally unchanged;
sensemaking adopted as second lens on supervisor's suggestion, Oct 2). Do not edit any chapter.
Finish by re-listing literature/notes/ and literature/_raw/ so I can see the files landed.
```
