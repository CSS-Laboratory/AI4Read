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
