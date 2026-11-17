# Session handoff — orchestration session (Oct 9 – Nov 18, 2026)

**Replaces as entry point:** `planning/session_handoff_2026-10-14.md` (keep it; its setup notes and logs are still the record).
**Role of the next session:** orchestration. Plans, reviews, verifies, writes prompts for sub-agent sessions, keeps the pipeline files current. Chapter prose is drafted only from paragraph plans that Albert has approved.
**Discussion style (project instruction, Nov 2026):** use ASD-STE100 Simplified Technical English when you talk with Albert: short sentences, active voice, one instruction per sentence. Thesis prose still follows `planning/writing_style_albert.md`.

> **Facts this session could not confirm** are marked `[FILL: …]`. Ask Albert for them in the first reply.

---

## 1. Setup (every session)

- Repo: `D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows` · PDFs: `D:\Master\Thesis\Thesis Content`. Both mount under `$HOME/mnt/<folder>` in the device shell. If the shell reports no connected folder, request access to both folders once.
- **Edit in place** with a python read-modify-write: normalise to `\n`, assert each old string occurs exactly once, write CRLF back if the file had it. About 110 files differ from git only in line endings; never stage them. Real changes: `git diff --ignore-cr-at-eol --numstat | awk '$1!=0||$2!=0'`.
- **Git:** use `git --no-optional-locks` (or `GIT_OPTIONAL_LOCKS=0`). Even `git status` / `git diff` from the VM can leave `.git/index.lock`, which the VM cannot delete. If it appears, `mv` it to `.git/stale-index-lock-claude-<date>` and tell Albert to `Remove-Item` it. **Never commit or push.** Give Albert PowerShell commands plus a PR summary; he can save it as `Claude outputs/PR_<branch>.md` and use `gh pr create --body-file`.
- **Google Docs:** the Docs/Drive connectors work. Large `read_doc` results are saved to a file (parse with jq/python). Use `replaceAllText` for text changes; append tables with the google-workspace `docs_index.py new-table` helper; guard batches with `requiredRevisionId`.
- **Claude project mirrors** to sync after edits (stage from the device, copy into `/home/claude/...`, then `project_write` with `local_path`): `claude/Pipeline_State.md`, `claude/reference_list.md`, `claude/search_log.md`, this handoff.
- Google Docs in use (Albert's Aalto Drive; not shared unless he shares them):
  - Interview design for the supervisor `10Td0AGzztzLABq5Xd6tJF_H93Vxfv3pQ097byz5Gxr0` (v1.0; §7 = changes after the pilot; three `[CHECK: page]` mappings: Lee C2, Ismail D2, Taeihagh E2)
  - Interview script (zh-TW / EN) + pilot recording sheet `1_E0uYYHJFvls7iMPQ48Wa6ExH3U0rzUldkxUUGTDGcA` (script tab = v1.0)
  - Thesis draft `1_ShrfnvgnrN42wpNL78w4Sq0u7rLwCDHMNF-Z8JuLSw` — **still lacks the Oct 6–22 Ch3 edits (incl. 3.3)**
  - Interview materials `1S0kiLKyfHAUymXI6Q_QH3OIb1fnvtBDcKE7sZhSvTQo` — **still has the old consent pack**
  - Backup folder "Thesis interview kit – backup (protocol v1.0, Oct 2026)" — `[FILL: confirm Albert ran the backup prompt]`

## 2. Read first (in order)

1. This file (§3–§7)
2. `planning/Pipeline_State.md` — **stale: last updated Oct 14.** Update it first (task 1 in §7).
3. `planning/writing_style_albert.md`
4. `chapters/ch3/README.md` · `chapters/ch2/README.md` · `chapters/ch1/README.md`
5. `research-design/interview_protocol_v1.0.md` · `research-design/wording_card_bilingual.md` v1.3
6. `planning/transcript_processing_prompt.md` **v2** (Nov 18) · `analysis/README.md` · `analysis/templates/`
7. Claude project doc `claude/research-design/research_plan_seminar_2026-10-28.md` (research plan for the seminar)
8. `literature/reference_list.md` — only when a citation question comes up

## 3. Settled — do not reopen

Everything in the Oct 6 and Oct 14 handoffs §3, plus:
- **Pilot is not data**; it used v0.98. **Protocol v1.0** (45–60 min; A4, C3, D1, D4, E4, E5 cut; one incident by default; documents in a separate optional call). **E3a fixed wording** (card v1.3 §6d).
- **Depth A threshold** unchanged: a within-case rule, not a comparison between organisations. Depth B has no threshold.
- **Chapter 3 is fully drafted** (3.1–3.7, ≈4,150 words; budget 3,000; overrun accepted, offset in Chapters 4–6).
- **Coding tool: ATLAS.ti desktop** (Aalto licence via download.aalto.fi; personal account with the @aalto.fi address). **AI coding features off.** Desktop only, not ATLAS.ti Web. Backups of the project to OneDrive. *3.4 `[FILL: coding software]` is not yet filled — see §7.*
- **Transcripts:** only de-identified copies go into AI tools; each use is logged. **Full draft English translation** of each de-identified transcript as a reading aid (Albert, Nov 18); coding stays in Mandarin. Process: `planning/transcript_processing_prompt.md` v2 (sub-agent; clean-up → draft translation → Albert checks against the Teams recording → "approve" → finalise).
- `interviews/transcripts/` is git-ignored (commit 45d5bce).

## 4. Hard rules

Unchanged (Oct 6 handoff §5): only de-identified interview material in any AI tool (this one included; if identifiable content is pasted, stop and remind Albert); no organisation names in chapters; `[PENDING]` / `[FILL]` / `[CHECK]` markers; verified sources only, every quote checked on the printed PDF page; paragraph plans approved before any chapter edit; never commit or push. **Never read transcripts, translations or filled templates in the orchestration session**; at most the de-identified contact summary or the sub-agent's counts.

## 5. Where things stand (Nov 18)

| Area | Status |
|---|---|
| Ch1 | Drafted (≈2,105 words). 1.5 ¶1 marker still `[PENDING: interviews Oct 5–19]` (shortening proposed, not approved yet) |
| Ch2 | 2.1, 2.5, 2.6 drafted (≈3,610 / 6,250). **2.2–2.4 now unblocked as soon as the depth-case interviews are done** |
| Ch3 | Fully drafted. 3.3 v1.1 (Oct 22, PR #19). Only fieldwork markers remain, plus four closable ones (§7) |
| Ch4–6 | Not started; after analysis |
| Fieldwork | `[FILL: interviews done / planned]` (seminar prep, Nov 4: "5 of 6 interviews done"). First transcript (P01) processed with the brief; v2 written from it |
| Seminar | Research plan presented (deck `Claude outputs/Research_Plan_Presentation.pptx`, discussant prep `Claude outputs/Discussant_QA_Prep.md`, Nov 4). `[FILL: feedback from the discussant / supervisor]` |
| Title | Proposed new title in the research plan ("Governance Seen from Below …"); `[FILL: supervisor's decision]` |
| Other | `Claude outputs/Prompt_Audit_2026-11-13.md` (audit of user-level Claude skills; outside the thesis) |
| Git | `main` = ce51134 (PR #21). Untracked, not in git: 3 files in `Claude outputs/`, `Research_Plan_Presentation.pptx` and the Aalto `.dotx` at the root, `Claude outputs/PR_transcript-prompt-v2.md`. **This handoff is uncommitted** |

## 6. Open problems to solve early

1. **Data location (privacy).** De-identified transcripts are in the repo folder on D: (`interviews/transcripts/de-id transcripts/`, git-ignored). The consent form and 3.6 say data are stored on Aalto OneDrive. Recommended: move the folder to Aalto OneDrive and connect that folder for the sub-agent (the signed consent text cannot change). If Albert keeps D:, 3.6 and `analysis/README.md` must change. Also confirm raw Teams transcripts (with names) are on OneDrive only.
2. **3.5 / 3.6 vs the full translation.** 3.5 says only quoted passages were translated; 3.6 says AI drafts translations "of Mandarin passages". Paragraph plan needed (one sentence each) for Albert's approval.
3. **Pace.** Full draft due end of November; hard deadline **Dec 15**. Analysis, 2.2–2.4 and Ch4–6 are all still ahead.

## 7. Next-step options for the orchestration session

1. **Update `Pipeline_State.md`** to Nov 18 (fieldwork, seminar, transcript process, ATLAS.ti, data-location issue) and sync the project mirrors.
2. **Close four Ch3/Ch1 markers** (Albert's answers needed): Breadth 6 `[FILL: tier]` (3.2); `[FILL: coding software]` → "ATLAS.ti [FILL: version], under Aalto University's licence" (3.4) plus half a sentence in 3.6 on the desktop project and OneDrive backups; 3.7 S1 option (a) confirm reconstruction or (b) state the record is partial; 1.5 ¶1 → `[PENDING: interviews]`. 3.6 `[PENDING: form sent…]` / `[PENDING: consent obtained]` can close once all consents are in.
3. **Paragraph plan for the 3.5 / 3.6 translation sentences** (§6.2).
4. **ATLAS.ti set-up kit:** codebook import spreadsheet from `analysis/templates/codebook_v0.md` (code groups STR / PRO / REL, phases, `INC_`, `SQ2_`; definitions and include/exclude rules as comments; sensemaking stays in memos, not codes) and a one-page set-up checklist. Ask Albert for the ATLAS.ti version first.
5. **Analysis plan and Ch4 outline** once all interviews are transcribed: within-case first, strata apart, Code-Document Table for the coverage matrix; Depth A threshold outcome.
6. **Ch2 2.2–2.4** writing briefs (dependencies in `chapters/ch2/README.md`).
7. Update the Google Docs (thesis draft with the Oct 6–22 Ch3 text; interview materials with form v1.1, consent email, preparation note, protocol v1.0).
8. Resolve the three `[CHECK: page]` items in the supervisor design doc.

---

## Copy-paste prompt for the new session

```
This is the orchestration session for my master thesis. Read
planning/session_handoff_2026-11-18.md in my repo first, then the files it lists under
"Read first", in that order.

Setup: my repo "D:\Master\Org-Policy-Dev-for-Gen-AI-Integration-in-BI-Workflows" and
"D:\Master\Thesis\Thesis Content" (PDFs) are connected; the device shell mounts them under
$HOME/mnt/. Edit in place there, keep CRLF line endings, use git --no-optional-locks,
never commit or push (I push myself). Talk with me in ASD-STE100 Simplified Technical English.

Do not reopen anything under "Settled". Follow the hard rules: only de-identified interview
material in any AI tool, never read transcripts in this session, no organisation names in
chapters, PENDING/FILL/CHECK markers, verified sources only with quotes checked against the
PDF page, and paragraph plans approved before any chapter edit.

When you have read everything, confirm in a few lines: what is done, what is blocked on me
(including the [FILL] facts in the handoff), the open problems in section 6, and the
next-step options in section 7. Then wait for my choice.
```

---

## Log — orchestration session, Oct 9 – Nov 18

**Oct 9:** TENK p. 9 checked (M12 ✅; CHECK removed from 3.6). Ethics note §5 location filled. AI use log template, consent email, recruitment banner, pilot runbook, participant preparation note. Google Docs: interview script + recording sheet; interview design document for the supervisor (questions → theory → verified references; Ackerman p. 5 and Nahar p. 18 checked).
**Oct 12–14:** Supervisor reply (too many questions; announce documents; threshold question; seminar may be booked). Pilot: clear, over 60 min → pilot only. Protocol v1.0, wording card v1.3, preparation note and consent email updated; design doc and script tab updated. PRs #16–#18 (incl. Pipeline_State and the Oct 14 handoff).
**Oct 17–22:** 3.3 sources PDF-checked (Castillo-Montoya pp. 812, 824, 827; Gremler pp. 66, 76 by OCR; Butterfield pp. 478, 480–481). Writing brief `planning/ch3_3.3_writing_prompt.md`; 3.3 drafted by a sub-agent; review: six wording fixes, 3.6 permission wording, 3.1 marker (approved). PRs #19–#20. Chapter 3 fully drafted.
**Oct 23–26:** ATLAS.ti options (Aalto licence; desktop; AI off; no Claude connector exists). Interview file checklist; backup-to-Drive prompt for a sub-agent.
**Nov 18:** Transcript processing brief v1 → v2 after P01 (Albert); full draft translation decided; PR #21 merged. This handoff written (uncommitted).
