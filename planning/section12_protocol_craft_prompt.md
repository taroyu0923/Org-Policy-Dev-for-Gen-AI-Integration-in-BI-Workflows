# §12 Protocol Craft — harvest pass (interview-methodology cluster)

**Purpose:** append one new section (§12) to each of the 14 `Interview_I*` notes, harvesting **how these studies were run** — sampling, recruitment, protocol construction, conduct, consent, analysis and trustworthiness — as opposed to what they asked about.
**Model:** Sonnet. **Created:** Sep 4, 2026. **Status:** not yet run.
**Also in scope:** the `references.bib` backfill for this cluster (see Part B). Same 14 sources, same session.

---

## Part A — the §12 harvest

### Why this cluster gets §12 and NOT §11

§11 WORKING-TIER RECEPTION must **not** be run on `Interview_I1–I14`. The §11 harvest produced a corpus-level statistic — *14 of 20 governance sources contain no account of how anyone below management experiences governance* — and that number is only meaningful because those twenty were selected as the **governance literature**: a sample with every opportunity to describe reception that did not.

The interview cluster was selected on the opposite criterion. Running §11 across it corrupts the count in both directions at once:

- **Method-craft sources** (I1 Castillo-Montoya, I2 the IPR worked example, I3 the ECU/Ithaka guide) are not about AI governance at all. A "documented absence" from a paper on interview protocol refinement is a **false null** and would pad the numerator with out-of-scope sources.
- **Empirical practitioner studies** (I9, I10, I13, I14 and others) return substantive material *by construction* — they were chosen because they study practitioners. Guaranteed positives dilute the claim.

**Rule: the §11 denominator stays at 20. This cluster is a separate corpus with a separate job.**

### What §12 must not duplicate

Already captured in these notes, do not re-ask:

| Section | Already covers |
|---|---|
| §2 HOW | Study type, duration, sample size, data sources, software (e.g. I9: 12-month case study, 18 semi-structured interviews, participant observation, NVivo) |
| §7 INTERVIEW VALUE | The questions themselves, mapped to the three phases — often verbatim with locations (I9 reproduces Mökander & Floridi's full Appendix 1 protocol) |
| §9 LIMITATIONS | Self-stated limitations of the study |

§12's territory is the **procedure between design and findings**: how participants were obtained, how the instrument was built and tested, how sessions were conducted, and how the analysis was made defensible.

### The query

Send verbatim to each notebook, substituting the source filename.

```
Continuing with ONLY the source "<filename>", same location rules (section name + page number for every point):

12. PROTOCOL CRAFT — Based ONLY on this source: what does it document about HOW the study was actually carried out, as opposed to what it asked or what it found? Do not repeat the study design, sample size or self-stated limitations already covered elsewhere. Cover, where the source contains them:
(a) RECRUITMENT AND ACCESS — how participants were found and approached; gatekeepers, organizational permission, referral or snowball routes; incentives; refusal or drop-out;
(b) SAMPLING LOGIC — how the number and mix of participants was justified; any saturation claim and how it was assessed; how multiple organizations, sites, or hierarchical levels were handled;
(c) PROTOCOL CONSTRUCTION — how the interview guide was built, piloted or refined; question sequencing and rationale; probe technique; explicit wording rules (e.g. avoiding "why", avoiding leading or judgemental phrasing); mapping of questions to research questions;
(d) CONDUCT — interview length, mode (in person, video, phone), single or repeated rounds, recording and transcription practice, language(s) used and any translation or back-translation procedure;
(e) CONSENT AND CONFIDENTIALITY — consent process; how participant and employer anonymity was protected; handling of confidential or commercially sensitive material; ethics approval route;
(f) ANALYSIS PROCEDURE — coding approach and named method; who coded; software; any intercoder agreement or reliability measure and its value;
(g) TRUSTWORTHINESS — member checking, triangulation, audit trail, reflexivity statements, or any other rigour claim, and how it was operationalized;
(h) TRANSFERABLE METHOD LESSONS — anything the authors say about what was difficult, what they would change, or what a researcher replicating this should watch for.

Quote procedures verbatim with location wherever the wording matters. If the source does not document a given item, say so for that item rather than inferring — a protocol paper that omits its analysis procedure is itself a useful observation. If the source is a methodological or instrument-design paper rather than an empirical study, answer for what it PRESCRIBES rather than what it did, and say which.
```

**Note the two closing instructions.** Item-level absences must be reported, not inferred around; and the method-craft papers (I1, I2, I3) need the prescriptive framing or the answer will be nonsense.

### Procedure

1. `notebook_list` to map notebooks to the 14 `Interview_I*` notes.
2. Send the §12 query to each of the **14** notebooks via `notebook_query`.
3. Append the answer to each note as `## 12. PROTOCOL CRAFT`, placed after §11 if present, otherwise after §10, and before "Albert's Questions".
4. Open every §12 with the provenance block:

```markdown
## 12. PROTOCOL CRAFT
> *Harvested <DATE> via MCP `notebook_query` to notebook `<notebook_id>` ("<notebook name>"). Query: §12 as specified in `planning/section12_protocol_craft_prompt.md`. ⚠ MCP queries do not persist to NotebookLM chat history — this note is the sole record of the exchange.*
```

5. Apply the **Unclear-point resolution rule (v2.3)**: one targeted re-query for any point lacking a clear section+page location; mark anything still ungrounded `⚠ UNRESOLVED — not confirmed in source` and report it.
6. Do **not** modify §1–§11 of any note. Do not recompile. Do not create notebooks. Do not run §11 on this cluster.

### Reporting back to Albert

A cross-source table, rows = the 14 sources, columns = (a)–(h), cells = documented / partial / not documented. That table is the Chapter 3 evidence map: it shows at a glance which methodological choices have precedent in the literature and which this thesis has to defend unsupported.

Then, separately, the four things Chapter 3 most needs precedent for — flag which sources supply each:

1. **Bilingual interviewing** — any study conducting interviews in more than one language, and how it handled translation, back-translation and the language of coding. (Six of Albert's fourteen interviews are in Taiwanese Mandarin; his current plan is researcher translation with pilot-based verification and coding in the original language. He needs precedent or a documented departure.)
2. **Multi-organization designs with uneven informant depth** — studies mixing single-informant sites with multi-informant sites, and how they justified analysing them together or separately. (Albert's design has two depth cases and seven breadth cases.)
3. **Employer-sensitive material** — how studies protected organizational as well as personal identity, and handled NDA-bound or commercially confidential content. (I9 is likely rich here: an industry case study with a funding dependency it discloses openly.)
4. **Small-n justification** — how studies with roughly 10–30 participants argued sufficiency, and whether they claimed saturation or explicitly declined to.

Finally: flag any source whose analysis procedure is **not** documented. Those are the ones Albert should not cite as method precedent no matter how relevant their topic.

---

## Part B — `references.bib` backfill for this cluster

**Problem.** Thirteen of the fourteen `interview-design` entries are still marked `TODO-verify: authors` (and in several cases year, venue or volume), yet all fourteen notes exist and carry author names. The PDFs were verified during compilation and the bib was never updated. This breaks **amendment A4** — `references.bib` is the single source of truth for per-reference status — and it means the entire methods cluster is formally uncitable, which blocks Chapter 3.

**Task.** For each of the 14, using the compiled note's §6 AUTHORS/YEAR/VENUE and the PDF:

1. Resolve the DOI or arXiv ID. Nine carry arXiv IDs already, so this is largely an arXiv API lookup.
2. Confirm authors, year, venue, volume and pages against the publisher or arXiv record — **not** against the note alone. §6 output is a claim to be checked, never verified metadata (see the metadata-fidelity warning in `claude/LitReview_Process_v2.md`; the Mitchell exclusion is why this rule exists).
3. Check venue standing for any journal source (SCImago for Scopus coverage and discontinuation, ISSN Portal, national indexes) and assign a quality tier.
4. Update the entry: complete metadata, `note` field recording verification method and date, `keywords` carrying the quality tier.
5. Add a line per source to `literature/search_log.md` under a new pass **S5 — interview-methodology cluster verification**.
6. Regenerate `literature/reference_list.md` from the updated bib.

Flag to Albert any source that cannot be resolved, rather than guessing — the A2/B2/Mitchell precedent applies.

---

## Copy-paste prompt for the Sonnet session

```
Read planning/section12_protocol_craft_prompt.md, planning/query_template_v2.4.md,
claude/LitReview_Process_v2.md and claude/Pipeline_State.md in this project, then run
BOTH parts of the §12 pass.

Setup: connect to my folder "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows".
NotebookLM is available via the notebook MCP; if auth is stale I'll run `nlm login`.

PART A — §12 Protocol Craft harvest across all 14 Interview_I*.md notes in literature/notes/.
Send the query via MCP notebook_query. Append each answer as a new section 12, after section 11
if present else after section 10, before "Albert's Questions", opening with the provenance block
from the prompt file. Do NOT touch sections 1-11, do NOT recompile, and do NOT run section 11 on
this cluster — that would corrupt the 14-of-20 absence statistic from the governance corpus.

Apply the Unclear-point resolution rule (v2.3): re-query once for any point lacking a clear
section+page location; mark anything still ungrounded as UNRESOLVED and tell me.

PART B — backfill literature/references.bib for the same 14 sources: resolve DOI/arXiv, verify
authors/year/venue/volume/pages against the publisher or arXiv record (NOT against the note),
check venue standing, assign quality tiers, record verification method and date in the note field.
Add a pass "S5 - interview-methodology cluster verification" to literature/search_log.md with a
line per source. Then regenerate literature/reference_list.md from the updated bib.

Report back: the (a)-(h) coverage table across the 14 sources; the four precedent questions listed
in the prompt file (bilingual interviewing, multi-organization uneven depth, employer-sensitive
material, small-n justification); any source whose analysis procedure is undocumented; and any
reference that could not be resolved.

Also delete the leftover scripts in literature/notes/_to_delete/ if you can, or tell me they are
still there.

Do not commit; I push to GitHub myself.
```
