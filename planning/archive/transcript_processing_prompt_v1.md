# Transcript processing brief — clean-up, then draft translation (zh-TW → EN)

**Created:** Nov 18, 2026 (orchestration session). **Applies to:** every Mandarin interview, one participant per run.
**Rule (supervisor, Oct 6; consent form v1.1; 3.6):** only **de-identified** transcripts go into any AI tool. Recordings never leave Teams. Every AI output is checked by Albert; coding decisions stay his. Each run gets one row in the AI use log.
**Decision (Albert, Nov 18):** a full draft English translation of each de-identified transcript is made as a reading aid, side by side with the Mandarin. Coding stays in Mandarin. Chapter 3.5 (and possibly 3.6) need one sentence updated — **paragraph plan for Albert's approval, not done yet.**

---

## Albert, before each run (by hand)

1. Make the de-identified copy from the Teams transcript: participant name, colleagues, organisation and parent company, teams, products and internal tool names, locations below country level, exact dates (→ "early 2024"). Speaker labels → `R:` (researcher) and `P:` (participant). File name `P<nn>_deid.docx` (or `.vtt` / `.txt`).
2. Put it **alone** in a de-identified-only folder (for example `...\Thesis-Interviews\02_transcripts\deid\`). Never put identifiable files in that folder.
3. Tick the de-identification checklist in the AI use log (`analysis/templates/ai_use_log_template.md`).
4. Start a new session and paste the prompt below, with the folder path and participant number filled in.

---

## Prompt for the sub-agent (copy from here)

```
Task: clean up and then draft-translate ONE de-identified interview transcript for my
master's thesis. Folder (connect only this folder; request access once if needed):
<DEID_FOLDER_PATH>   Participant: P<nn>   Language: Taiwanese Mandarin (zh-TW)

Read first: research-design/wording_card_bilingual.md (fixed EN/zh-TW wording of the
interview questions) in my repo D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows,
only if that folder is already connected. Do not edit anything in the repo.

RULES
- This transcript is already de-identified. If you still find a name of a person,
  organisation, team, product or an exact date, STOP: do not continue, and report the
  line numbers only (do not repeat the identifier).
- Work only in the connected folder. Never overwrite the source file; write new files
  beside it. Do not upload anything anywhere. Do not delete anything.
- You have no recording. Never invent words. Where the text is garbled or a word is
  uncertain, keep your best reading and mark it [? …] so I can check it against the
  recording in Teams.

STEP 1 – Clean-up (Mandarin, verbatim)  → P<nn>_deid_clean.md
- One turn per paragraph, labelled R: / P:, with the Teams timestamp kept at the start
  of each turn (e.g. [00:12:31]).
- Fix only: obvious speech-recognition errors where the intended word is clear from
  context (mark each fix inline as {原:錯字→改:正字} so I can review it), punctuation,
  merged or split turns, and Simplified→Traditional characters if Teams produced any.
- Keep the participant's own wording, hesitations that change meaning, code-switching
  into English, and repetitions. Remove only pure fillers (嗯, 呃) when they carry no
  meaning. Do not summarise, smooth or correct the participant's grammar.
- Where the researcher read a fixed question, replace a garbled version with the exact
  wording-card text and mark it {fixed wording}.

STEP 2 – Draft translation  → P<nn>_deid_bilingual.md
- A two-column Markdown table per turn: | Time | Speaker | 中文 (clean) | English (draft) |
- Translate faithfully and literally enough to keep meaning and hedges ("可能", "好像",
  "應該" → "maybe", "seems", "should/probably"); keep uncertainty, keep the speaker's
  register; no added explanations. Keep English terms the participant used in English.
- Workplace terms: keep a glossary at the end (中文 term → English used), and use it
  consistently. Mark any phrase you could translate two ways as [alt: …].
- Fixed questions: use the English wording from the wording card.
- Head the file with: "DRAFT machine-assisted translation of a de-identified transcript.
  Not checked by the researcher. Not for quotation until checked against the Mandarin."

STEP 3 – Report back (no transcript content in the report beyond what is needed):
- file names written; number of turns; number of {原→改} fixes; number of [? …] and
  [alt: …] marks; glossary size; anything that stopped you.
- One suggested AI-use-log row: date, tool (model name), material ("P<nn>_deid,
  full transcript"), purpose ("transcription clean-up; draft translation"), output kept
  (draft files), how to check ("Albert: [? …] and {原→改} against the Teams recording;
  translation spot-check").
```

---

## Albert, after each run

1. Check every `[? …]` and `{原→改}` against the Teams recording; accept or correct. Then remove the marks in your own final copy `P<nn>_deid_final.md`.
2. Spot-check the translation (at least the incident section B and Section E). Any passage you may quote in the thesis: check it fully and decide the final English yourself (3.5).
3. Add the row to the AI use log (OneDrive), with how you checked it.
4. Code in Mandarin (ATLAS.ti); use the English column only as a reading aid.
5. Nothing from these files goes into the repo or to the orchestration session; if you want help, send only the de-identified contact summary.
