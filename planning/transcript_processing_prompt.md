# Transcript processing brief — clean-up, then translation (zh-TW → EN)

**Version:** v2, Nov 18, 2026 — revised after the P01 run. v1 is in `planning/archive/transcript_processing_prompt_v1.md`.
**Applies to:** every Mandarin interview, one participant per run.
**Rule (supervisor, Oct 6; consent form v1.1; 3.6):** only **de-identified** transcripts go into any AI tool. Recordings never leave Teams. Every AI output is checked by Albert; coding decisions stay his. Each run gets one row in the AI use log.
**Decision (Albert, Nov 18):** a full English translation of each de-identified transcript is made as a reading aid, side by side with the Mandarin. Coding stays in Mandarin. Chapter 3.5 (and possibly 3.6) need one sentence updated — **paragraph plan for Albert's approval, not done yet.**

**What changed from v1 (lessons from P01):** Teams speaker labels and the title/date header are replaced automatically, not a stop · public third-party software names may stay · a term list makes speech-recognition fixes certain · the wording card and a shared glossary sit in the transcript folder · rules for protocol notes, split/merged turns and missing timestamps · a fixed format for uncertain words · a check list in the first report · a finalisation step after Albert's approval · a `.gitignore` check.

---

## Albert, before each run (by hand)

1. **Make the de-identified copy** from the Teams transcript. Remove or replace: names of the participant and of colleagues; the employer and parent company; team names; **internal** tool or product names; locations below country level; exact dates (→ "early 2024").
   - **May stay** (decided for P01): names of public third-party software (for example Claude, Jira, Confluence, Bitbucket, Slack, DeepSeek, OpenSearch); company size; job roles; quarter-level timing (for example "Q1 next year").
   - Speaker labels and the meeting title/date header: the sub-agent replaces these (see the prompt). You can leave them.
2. **File name** `P<nn>_deid.docx` (or `.vtt` / `.txt`). No name in the file name. Also check the Word file properties (author, last modified by).
3. **Folder:** put it in the de-identified-only folder:
   `D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows\interviews\transcripts\de-id transcripts\`
   That folder also holds three non-identifying reference files (make them once, reuse them for every participant):
   - `_wording_card_bilingual.md` — copy of `research-design/wording_card_bilingual.md`
   - `_term_list.md` — tools, systems and English terms that participants are likely to say (one per line). Add new ones after each run.
   - `_glossary_shared.md` — the workplace-term glossary (中文 → English). Start from the P01 glossary; the sub-agent extends it.
4. **Git check:** `interviews/transcripts/` must be in `.gitignore` (done on Nov 18, commit 45d5bce). Never `git add .` without checking.
5. Tick the de-identification checklist in the AI use log (`analysis/templates/ai_use_log_template.md`).
6. Start a new session and paste the prompt below, with the participant fields filled in.

---

## Prompt for the sub-agent (copy from here)

```
Task: clean up and then translate ONE de-identified interview transcript for my
master's thesis.

Folder (connect only this folder; request access once if it is not connected):
D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows\interviews\transcripts\de-id transcripts
Participant: P<nn>   Language: Taiwanese Mandarin (zh-TW)   Location: <country>
Industry: <industry>
Questions were asked in: <Mandarin | English | mixed>. If the transcript already contains
English protocol text that I pasted in, keep it as it is.

Reference files in the same folder (read them first; do not edit the wording card or
the term list):
- _wording_card_bilingual.md  — fixed EN/zh-TW wording of the interview questions
- _term_list.md               — expected tool names and English terms
- _glossary_shared.md         — glossary from earlier participants; reuse it
If a reference file is missing, say so and continue without it.

Discussion and reports: use ASD-STE100 Simplified Technical English.

STEP 0 – Pre-check (before you read the transcript text)
- The file name must match P<nn>_deid*. If it contains a name, or does not look like an
  interview transcript, STOP and report.
- Check the file metadata (author, last modified by). Report a name there, but do not
  stop for it: the source file stays local.
- Do not open embedded images. Report how many there are.

AUTOMATIC REPLACEMENTS (do these; do not stop for them; do not repeat the removed text)
- Teams speaker labels: researcher → R, participant → P.
- Remove the Teams meeting title, the date/time line and "started transcription" lines.
  Keep the recorded length.

RULES
- STOP before any further step if the speech itself (not the speaker labels or header)
  contains: a name of a person, the employer or its parent company, a team, an internal
  tool or product, a location below country level, or an exact date. Report only the
  line numbers (count paragraphs from the top of the file) and the category. Do not
  repeat the identifier.
- These may stay and are not a stop: public third-party software names, company size,
  job roles, quarter-level timing. List them in the report so I can decide.
- Work only in the connected folder. Never overwrite the source file; write new files
  beside it. Do not upload anything anywhere (no chat file cards, no project docs, no
  artifacts). Do not delete anything.
- You have no recording. Never invent words.

STEP 1 – Clean-up (Mandarin, verbatim) → P<nn>_deid_clean.md
- One turn per paragraph: [hh:mm:ss] R: … / [hh:mm:ss] P: …
- Consecutive segments by the same speaker are one turn: join them and keep each later
  segment's timestamp inline, e.g. "… [00:08:10] …".
- An answer merged into the researcher's turn: split it out. If it has no timestamp,
  label it [no timestamp in source — after hh:mm:ss].
- Fix only: obvious speech-recognition errors, punctuation, wrongly merged or split
  turns, Simplified→Traditional characters.
  - Clear fix: {原:錯字→改:正字}. Use _term_list.md: a misheard tool name that matches a
    listed term is a clear fix (e.g. cloud/clouding → Claude, conference → Confluence).
  - Uncertain, with a likely reading: [? likely（原：ASR text）]
  - Uncertain, no likely reading: [? ASR text]
- Keep the participant's own wording, meaningful hesitations, English words they used,
  and repetitions. Remove pure fillers (嗯, 呃, 啊) that carry no meaning. Do not
  summarise, smooth or correct grammar.
- Researcher protocol notes inside the transcript (question labels such as
  "B2 — …", "6a. Escalation probe (new v1.1)", interviewer instructions such as
  "Never ask…"): keep them inside square brackets, unchanged.
- Fixed questions: where the researcher read a fixed question and Teams garbled it,
  replace it with the exact wording-card text and mark it {fixed wording}.
- File header: source file name, recorded length, the speaker codes, the marking
  conventions, and the status line "Not yet checked by the researcher."

STEP 2 – Translation → P<nn>_deid_bilingual.md
- First line: "DRAFT machine-assisted translation of a de-identified transcript. Not
  checked by the researcher. Not for quotation until checked against the Mandarin."
- Table: | Time | Speaker | 中文 (clean) | English (draft) | — one row per turn.
- Build the 中文 column from P<nn>_deid_clean.md by script, so that it is identical to
  the clean file. Do not retype it.
- Translate faithfully; keep hedges and uncertainty (可能 → maybe, 好像 → seems,
  應該 → should/probably), keep the speaker's register, add no explanations, keep English
  terms the participant used in English. Fixed questions: wording-card English.
- [? …] in the Mandarin: carry the mark into the English.
- Mark any phrase with two plausible translations as [alt: …].
- Glossary at the end (中文 → English used), applied consistently. Reuse every term from
  _glossary_shared.md with the same English. List new terms separately so I can add
  them to the shared glossary.

STEP 3 – Report back (no transcript content beyond what is needed)
- Files written; number of turns (R / P); counts of {原→改} fixes, [? …] marks,
  [alt: …] marks, missing timestamps; glossary size (reused / new). Count only marks in
  the transcript body, not the examples in the file header.
- Anything that stopped you; the metadata and image findings; the "may stay" items.
- A CHECK LIST for the Teams recording, in this order, with timestamps:
  1. meaning-critical [? …] items (they change who, what, yes/no, or which tool)
  2. other [? …] items
  3. missing timestamps
  4. all {原→改} fixes, grouped by turn (quick spot-check)
- One suggested AI-use-log row: date · tool (model name) · material "P<nn>_deid, full
  transcript" · purpose "transcription clean-up; draft translation" · output kept (the
  two draft files) · how to check "Albert checks [? …] and {原→改} against the Teams
  recording; translation spot-check".

STEP 4 – Apply my corrections (repeat until I approve)
- I will send verified wording from the Teams recording. My verified wording replaces the
  ASR text as I wrote it. Still remove pure fillers. Keep my round-bracket notes as notes.
- If my correction keeps a word that looks like a speech-recognition error, keep your
  fix mark and ask me once.
- If a correction is ambiguous (for example it repeats text that is in another turn),
  ask before you change anything.
- After each round: update both files (the 中文 column again by script), and report the
  open items only.

STEP 5 – Finalise (only after I write "approve")
- Clean file: write the approved fixes into the text, remove the {原→改} marks, and add a
  table at the end: | Time | Source (ASR) | Corrected |. Replace the status line with
  "Checked by the researcher against the Teams recording, <date>."
- Bilingual file (only after I approve the translation): replace the DRAFT line with
  "Machine-assisted translation of a de-identified transcript. Checked and approved by
  the researcher on <date>." Remove "draft" from the title and the table header.
  Keep the [alt: …] marks unless I say to remove them.
- Write the new glossary terms to _glossary_shared.md and new tool names to the list in
  your report (I add them to _term_list.md myself).
- Give the final AI-use-log row.
```

---

## Albert, after each run

1. Check the items in the sub-agent's check list against the Teams recording. Send the verified wording back in the same session (Step 4).
2. Spot-check the translation (at least the incident section B and Section E). Any passage you may quote in the thesis: check it fully and decide the final English yourself (3.5).
3. Write "approve" (Step 5). The final files are `P<nn>_deid_clean.md` and `P<nn>_deid_bilingual.md`.
4. Add new tool names to `_term_list.md`.
5. Add the row to the AI use log (OneDrive), with how you checked it.
6. Code in Mandarin (ATLAS.ti); use the English column only as a reading aid.
7. Nothing from these files goes into the repo or to the orchestration session; if you want help, send only the de-identified contact summary.
