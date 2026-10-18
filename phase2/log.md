# Phase 2 run log

One block per stage. Token counts come from the agent results (all subagent tokens, including cache reads), and durations are wall-clock. These numbers set the cost estimate for 2b.

## Post 02 · 2026-10-ai-finance (T2, topic input)
| Stage | Agent (model) | Tokens | Time | Result |
|---|---|---|---|---|
| pre-S0 research: Harari claims | general-purpose (Opus) | 180,948 | 24.2 min | 20 claims (15 V, 4 S, 1 U), 6 critiques; machine transcripts of BIS 2024 and WEF 2026 audio. Meta-manager spot-check: key 10-year quotes confirmed. |
| pre-S0 KB survey | Explore (Opus) | 182,755 | 7.8 min | lenses with audit status, wiki nodes, gaps, post-01 hooks |
| S0 topic card | planner (Sonnet 5.5) | 136,365 | 3.5 min | 5 sub-claims, 4 lenses, 3 interactives, 3 decisions. Meta-review: pass with 5 edits (home-field evidence section, iterate-toy framing, Arora step, Lens 4 focus, W5). Numbers rechecked: all correct. |
| S1 source brief | planner (Sonnet 5.5) | 338,951 | 32.4 min | 42 units: 25 seen at source, 12 from digests needing a source check, 5 unseen; 19 traps; 13 findings that correct the card (no evidence yet for (a); Harari's "complicated" means data volume; Arora's caveats; Ashby gives 3 levers; FSB URL fixed; the FCIC records a correlation error). |
| S2 brief check | fact-checker (Opus 5.5) | 446,866 | 28.6 min | **brief had 1 critical, 10 major, 44 minor** (S1 was Sonnet). 7 OK, 34 FIXED, 3 DROP, 2 secondary. All 10 CHECK-AT-SOURCE units checked at the page; every Harari/Skingsley quote re-transcribed (small.en and medium.en). Meta spot-check: the critical (FCIC p. 28 "the securities almost no one understood") is confirmed. Lesson: an independent Opus check before drafting is essential; Sonnet drafting of briefs drops hedges and overstates contrasts. |
| S3 outline | writer (Sonnet 5.5) | 301,035 | 15.3 min | 16 sections, about 6,700 words, 5 verified widget configs (W5 cascade, herding, 5 labs, 2 steppers), audio plan of 16 chapters. Meta-review: pass with required changes. **Major fairness issue:** S1, S2 and S3 all missed Harari's unhedged Davos thesis "anything made of words will be taken over by AI" (meta-manager re-transcribed and added it as A3b). Rule fix: a balance check was added to the fact-checker, writer and planner prompts. |
| S4 draft | writer (Sonnet 5.5, resumed S3 agent) | 385,881 cumulative (S3+S4; the counter appears cumulative) | 17.8 min | about 7,420 words, 81 citations, 31 sources, 14 widget configs OK, render PASS at 390 px; 16 audio chapters scripted (about 27 min); cut to fit 7,500 (collusion fold-out and Rung 1 dropped). |
| S5 round 1 | checker A (Opus 5.5) | 338,779 | 18.7 min | 0 critical / 7 major / 21 minor |
| S5 round 1 | checker B (Sonnet 5.5) | 352,864 | 15.1 min | 0 / 4 / 27 |
| S5 round 1 | critic (Sonnet 5.5) | 173,312 | 4.5 min | criteria 2–6: 3/3/3/3/2 (gate not met); the writer's self-score had been 4–5 |
| — | **checker comparison** | | | Both found 3 majors (Danielsson hedge, Harari capability balance, Truth Terminal liability). **Opus only:** 4 majors (FSB merge, Keynes merge, Ashby table condition, published Danielsson p. 7). **Sonnet only:** the playground answer error (Opus wrongly said "answers right"), and the Arora toy as major (Opus had it minor). Conclusion: Opus finds more misrepresentations, but neither checker alone is complete. For 2b, run **Opus as primary plus Sonnet as a second checker**, merged by union. |
| S5→S4 round 2 | writer (Sonnet 5.5, resumed) | 129,706 | 26.8 min | All 11 majors addressed; critic's structural changes made (short answer, human-centred definition, chain diagram, self-contained ladders, vocabulary). Main text 7,458 words plus 1,390 in fold-outs; 116 citations; 15/15 widgets; render PASS. |
| S5 round 2 | checker A (Opus) | 304,786 | 19.9 min | 0 / 3 / 13; all round-1 majors verified fixed; 2 response-1 claims false |
| S5 round 2 | checker B (Sonnet) | 354,160 | 19.0 min | 0 / 2 / 17; caught the "undated forecasts filed as hedged" major |
| S5 round 2 | critic (Sonnet) | 173,682 | 4.5 min | 3/3/4/4/3 |
| — | meta-manager | — | — | Harari classification oscillated between rounds, so a binding four-group table was written for round 3. New standard word counter `scripts/wordcount.py` (main text 6,548). |
| S5→S4 round 3 | writer (Sonnet 5.5, resumed) | 370,599 | 15.7 min | All majors and minors answered; Harari four-group table and summary sentence in place; chain diagram rebuilt; Lens 1 toy (6 assets, 3 products); main text 6,942 words plus 1,853 in fold-outs; 130 citations; 15/15 widgets; render PASS; 5 clipped formulas fixed. |
| S5 round 3 | checker A (Opus) | 304,977 | 16.7 min | 0 / 1 / 10 (Guardian 2024 quote cut before "humanity has never been united") |
| S5 round 3 | checker B (Sonnet) | 82,964 | 22.6 min | 0 / 2 / 15 (same Guardian major; Harari's "AI can lie" missing; "we'll need" mis-transcription) |
| S5 round 3 | critic (Sonnet) | 197,722 | 4.0 min | 4/3/4/4/3 |
| meta fix | meta-manager (Opus) | — | — | Fixed all 3 majors and the minors from both checkers, plus the critic's top changes: Lens 1 toy direction (OR-tranche: 7/4 vs 3/2), chain labels ("our order"; status in nodes), tables in Lens 3b, the variance rule, a plain CDO definition, short-answer restructure, a diagram `preview` option. Build, 15/15 widgets and render PASS; main text 7,123 words. Rule proposals in phase2/post02/rule-proposals.md. |
| S6 audio | Kokoro (local) | — | about 25 min | 16 chapters, 35.7 min; tagged "AI4Read from CSS Lab"; all.mp3 at 48 kb/s (16 MB artifact limit) |
| S7 draft publish | meta-manager | — | — | claude.ai artifact (db/sample/downloads), site dist and shelf rebuilt; English pack for Margin |

### T2 post 02: summary for the 2b decision
- **Agent calls:** 1 research, 1 survey, planner ×2 (S0, S1), Opus brief check, writer ×4 (S3, S4, two revisions + final), 3 rounds × (Opus checker + Sonnet checker + critic). About 5.0 M subagent tokens in total (sum of the reported counts, cache reads included).
- **Gate history:** checkers' major findings by round: 11 (S2 brief) → 7+4 → 3+2 → 1+2 → 0 after the meta fix. Critic minimum score by round: 2 → 3 → 3 → (meta fix).
- **Lessons:**
  1. An independent Opus check of the brief before drafting is essential.
  2. Balance errors (a person made to look more cautious or more extreme) are the most frequent kind of major finding, so the balance check is now in the prompts.
  3. The writer's self-scores were 1–2 points above the critic's every round, so self-scores must never count toward the gate.
  4. Opus and Sonnet checkers each find majors the other misses, so use both.
  5. The meta-manager still had to step in after round 3, so 2b needs the same final human-level audit, or a fourth round.

## Post 02 v2 · AI-automated society (after Kunhao's note, 2026-10-18)
| Stage | Agent (model) | Tokens | Time | Result |
|---|---|---|---|---|
| S0 v2 | Claude (writer, Opus) | — | — | topic card v2: five jobs (run, decide, check, declare, answer) |
| S1b | planner (Sonnet) | 117,035 | 30.3 min | V1–V8 from 7 new sources; 10 challenges to the thesis; flagged the Nexus file (OceanofPDF) and the mislabelled Arora file |
| — | meta-manager | — | — | Nexus file deleted and withdrawn (shadow-library policy); Drive backup rebuilt and re-verified |
| S2b | fact-checker (Opus) | — | — | 1 critical (withdrawn Nexus still cited in V8 and the traps), 2 major (IMF quote subject; Searle's "belief" bar), 20 minor; all fixed in source-brief-v2.verified.md |
