# File Naming Convention — literature notes and raw harvests

**Status:** canonical. Applies to every new reference from Sep 11, 2026 onward, and to the retrofit of existing notes.
**Location:** `planning/naming_convention.md` in the repo. Project copy is a mirror.

---

## The rule

```
literature/notes/<ID>_<firstauthor><year>_<slug>.md
literature/_raw/<ID>.md
```

| Part | Rule |
|---|---|
| `ID` | Cluster letter + number, no zero padding — `A1`, `A12`, `B8`, `C10`, `D7`, `E4`, `I14`. Must match the `[ID]` in the note's own H1 heading and the cluster tag in `references.bib`. |
| `firstauthor` | **First author's surname only.** Lowercase, ASCII-folded (`Ustahaliloğlu` → `ustahaliloglu`, `Mökander` → `mokander`, `Kästner` → `kastner`). Retain an internal hyphen **only** for a genuine compound surname (`castillo-montoya`). Institutional authors use a short recognisable form (`nist`, `oecd`). |
| `year` | Four digits, matching the year the thesis will cite. Omit only if the source is genuinely undated, and record why in the `references.bib` note field. |
| `slug` | Two to five distinctive words from the title, lowercase, underscores. Not the full title, not generic filler. |

Everything lowercase except the `ID`. Words separated by `_`; the only hyphens permitted are inside a compound surname.

**Examples**

```
A1_batool2024_ai_governance_slr.md
A4_batool2024_responsible_ai_governance_slr.md
A6_agarwal2025_five_layer_framework.md
B6_lee2024_rai_question_bank.md
C7_mokander2021_ethics_based_auditing.md
D7_rakova2021_responsible_ai_meets_reality.md
I9_mokander2022_ethics_based_auditing_industry.md
```

## Why each part exists

**The ID is not decoration.** Without it, the ID↔paper mapping cannot be read from a directory listing, and every session has to open files to learn it. That gap is what allowed a gap-fill run to drift into inventing "D8" and "E5" before anyone noticed. With the ID in the filename, `ls literature/notes/` *is* the mapping table.

**The slug is load-bearing, not cosmetic.** Two collisions already exist in this corpus:

- Batool 2024 appears twice — A1 (*Research Square*) and A4 (*arXiv*), same first author, same year. Only the slug separates them.
- Mökander appears twice — C7 (2021, *Science and Engineering Ethics*) and I9 (2022, the AstraZeneca industry case study). Here the year separates them, and the slug keeps them readable.

Never shorten a slug to the point where two entries could collapse into the same name.

**First author only.** The previous convention joined author surnames with hyphens, which made `castillo-montoya` (one person, compound surname), `mokander-floridi` (two authors) and `xie-li-cheng` (three authors) indistinguishable. Co-authors belong in `references.bib`, not in a filename.

**ASCII-folding** keeps filenames portable across Windows, git and pandoc. The full diacritics stay in the bib entry and in the note's §6, which is what the thesis actually renders.

## Raw harvest files

```
literature/_raw/<ID>.md
```

One file per reference, matching the note's ID. Query 1 written the moment it returns; Query 2 **appended** the moment it returns. Never assembled at the end — the point is that each half reaches disk before the next query is sent.

The file opens with the notebook ID, the notebook's confirmed source title, and a timestamp; each answer is preceded by the exact query text sent. Since MCP-driven queries do not persist to NotebookLM's chat history, `_raw/` is the provenance trail that replaces it.

## Assigning a new ID

1. The cluster letter comes from the source's cluster, not from where its PDF happens to sit.
2. The number is the next free integer **in that cluster's note sequence**, checked against *both* `literature/notes/` filenames and `references.bib` keywords.
3. Numbers of excluded sources are **retired, never reused** — A2, B2 and D3 are permanently spent.
4. Report the proposed ID to Albert before creating the notebook or writing the file.

✅ **Cluster E resolved (Albert's decision, Sep 11, 2026).** `algobiasbianalytics2025` — the unverifiable ResearchGate entry previously occupying bib `E1` — is **EXCLUDED** on the same grounds as A2, B2 and Mitchell: not available or reliable enough to verify. The entry stays in `references.bib` marked `EXCLUDED` with reason and date, and is never cited. The E sequence is therefore: **E1 = Khandan (2025)**, **E2 = Abraham et al. (2019)**, **E3 = Janssen et al. (2020)**, **E4 = Zhang et al. (2022)**. Note numbering and bib numbering now agree.

## Retrofitting existing files

Existing notes predate this convention: governance notes carry a cluster letter but no number (`A_agarwal2025_…`), and interview notes use `Interview_I<n>_` with three different tail formats (author+year, author+topic, author only).

To retrofit — **do not guess**:

1. For each note, read its own H1 `[ID]` and its §6 AUTHORS/YEAR/VENUE to derive `firstauthor` and `year`. These are the note's own recorded values; do not infer from the existing filename, which is exactly what this convention exists to stop.
2. Keep the existing slug wherever it already satisfies the rule — most do.
3. Produce the full rename table and **get Albert's approval before executing**.
4. Execute with `git mv` so history follows the file.
5. Update every reference to a renamed path — at minimum the Mitchell exclusion banner and the `Interview_I*` glob in `section12_protocol_craft_prompt.md`, which becomes `I*_`.

## Scope

This convention covers `literature/notes/` and `literature/_raw/`. It does not apply to `planning/`, `research-design/`, `chapters/` or `analysis/`, which are named by function rather than by source.
