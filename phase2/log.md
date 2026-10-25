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
| S2b | fact-checker (Opus) | 342,046 | 22.8 min | 1 critical (withdrawn Nexus still cited in V8 and the traps), 2 major (IMF quote subject; Searle's "belief" bar), 20 minor; all fixed in source-brief-v2.verified.md |

## 2026-10-18 · Post 02 v2 · S4 draft
- Writer: Claude (revised phase 2). Built from `src/content-v2.tpl.html` + v1 blocks (`src/fill_v2.py`, overrides in `src/v2-blocks/`). Main text 6,584 words, fold-outs 2,186.
- New: five-jobs frame, Kirilenko 2017 hook, IMF job table, Haldane–May homogeneity lab (`fact()`), May ecology fold-out lab, Searle lens (book), Lupia lens 4, short answer + verdict table + signs to watch. Dropped: info-theory lens, contracts switch, count lab, chain diagram, box-flash, Dütting, Buehler, Shannon, Akerlof, Keynes, SEP, MIT Sloan, Fox, Arora 2009 WP.
- check.mjs 15/15; render test PASS. S5 round 1 launched: Opus + Sonnet fact-checks, Sonnet critic (`review/v2-*-1*.md`).

## 2026-10-18 · Post 02 v2 · S5 rounds 1–3, audit, release
- Round 1: Opus 0/1/21, Sonnet 0/2/32, critic 3/3/3/4/3. Round 2: Opus 0/2/17, Sonnet 0/2/22, critic 4/3/4/4/3. Round 3: Opus 0/0/12, Sonnet 0/1/16, critic 4/3/4/4/3 (Lens 2b only). All fixed; post-round-3 narrow audit: Lens 2b and §13 at 4/4.
- Found and fixed a builder bug: the artifact (standalone) page lost its widgets because widgets.js contained `</script>` in a comment. test.mjs `--inline` added.
- Main text 7,468 words; audio 37.0 min re-recorded and tagged; artifact republished (version 2); site dist, shelf and English pack rebuilt; Drive backup refreshed (sources parts, bundle d7d2793 from the Mac, SHA256SUMS).
- WRITING 0.6 and 0.7.

## 2026-10-25 · English separated from posts 01 and 02
- Kunhao: publish the blog without the English part; English must be C1 or C2. Both posts now end at Recall/Sources; English audio chapters removed; post 01 hook/home re-recorded with the "AI4Read from CSS Lab" intro. Artifacts republished (post 01 v10, post 02 v3).
- New C1–C2 packs (post 01: 27 items; post 02: 28 items) from `posts/<slug>/english/english.json`; `english_pack.py` rewritten with level/offset validation; loop audio for Margin. Independent check: round 1 2/11/27, round 2 0/2/9, all fixed.
- Prompts for the website and Margin agents; handoffs updated; WRITING 0.8; CHARTER and writer prompt updated.

## 2026-10-25 · Post 03 (interpretability strand 1, "the lens") · S0
- Canon committed: interpretability field (34 items, 7 strands), 971703a. Sources saved with URL and access date (Olah 2020, Elhage 2021, Nanda glossary; glossary moved to neelnanda.io/mechanistic-interpretability/glossary; its logit-lens entry is corrupted in the saved copy).
- S0 planner (Sonnet, fresh agent): topic card written; 319k tokens, 12.4 min. GAPs: post-training clause unsupported; "behaviours are circuits" partial; "concepts are directions" a hypothesis (vision evidence only); hidden state = residual stream in no source (notebook evidence); steering not in the three sources. 14 technical flags (HF hidden_states, norms, embedding scaling, positions, TransformerLens weight processing, tolerance, logit lens).
- Gate: waiting for Kunhao.

## Post 03 · S0 gate passed (2026-10-25 16:36 JST)
- Kunhao's decisions: strand 2 = eigen-decomposition post (04, before *Directions*; canon reading path updated), post-training clause out of the lens, two lenses, draggable widget preferred → meta-manager built `vec2d` (component library; gallery render test PASS), title approved.

## Post 03 · S1 source brief
- planner (Sonnet, fresh agent): `source-brief.md`, 14 units, 161 quotes machine-checked verbatim (≤ 25 words); 114k tokens, 14.9 min. Gate: ≥ 8 units with location and quote: PASS.
- UNSEEN list: original logit-lens post, Nanda logit-lens body (corrupted), some missing math lines, RMSNorm formula, steering, "hidden state", model families, base vs instruct, figures.
- 9 notes on the topic card (e.g. T2: Nanda does have an RMSNorm entry; W9-B is not a virtual weight; "unit vector" is ours). Passed to S2.
- Notebooks: a fresh agent (Opus) builds and runs `01_bus_gpt2.ipynb` and `02_bus_my_model.ipynb` in parallel (results.md for the writer).

## Post 03 · S2 fact-check
- fact-checker (Opus, fresh agent): `source-brief.verified.md`, `review/s2-check.md`; 319k tokens, 14.6 min. 1 critical (three Olah quotes from text commented out of the published HTML), 9 major (cut Nanda quote, misread Nanda L216, "unit vector" in no source, an invented tension, a dropped Elhage hedge, four uses of Elhage material outside Kunhao's scope), 24 minor. All fixed in the verified brief; 164 quotes verbatim. Gate (0 unchecked units): PASS.
- Topic card T2 corrected (Nanda has an RMSNorm entry).

## Post 03 · notebooks
- notebook builder (Opus, fresh agent): `01_bus_gpt2.ipynb` (TransformerLens 4.3.0, also tested on 3.9), `02_bus_my_model.ipynb` (HF hooks; GPT-2 full run, tiny random Qwen3 from its config, tiny Gemma 3), executed offline; `results.md` (67 results, 19 library-source citations); 289k tokens, 27.5 min.
- Key: in-model additivity bit-exact (same float32 adds; reordering gives 1.03e-6 rel); HF `hidden_states[k]` = TL raw stream (k = 0..11, rel 7.8e-7); the last HF entry is final-normed; logit lens with ln_final reproduces logits exactly. TL 4 removed HookedTransformer (card T6 sharpened); Gemma 3 norms sit on sub-layer outputs before the add (T2 confirmed). Meta-manager spot-checked the transformers source lines for hidden_states.

## Post 03 · S3 outline (+ S2 addendum)
- writer (Sonnet, fresh agent): `outline.md`, 12 sections, 6,630 words planned, 7 widgets (incl. vec2d); self-scores 4/4/4 on criteria 2, 4, 5 (gate PASS); 240k tokens, 8.9 min. Bets placed before reads/writes as in Kunhao's spec.
- Request Q1 (multiple-access channel): meta-manager fetched MacKay 2003 (free author PDF); fact-checker (Opus, fresh) added unit 15 (p. 237, fig. 15.3); 148k tokens, 4.8 min. Q2 (Shannon "bandwidth") not sourced: contrast banned.
- Meta-manager: W9 re-run in numpy; the outline's margin at phi = 0 was wrong (-4, not 0); corrected in toyworlds.md and passed to S4.

## Post 03 · S4 draft and S5 round 1
- writer (Sonnet, fresh): draft 7,358 words main text, 7 widgets; check.mjs 7/7, build 0 unmapped, test.mjs --inline PASS; site render test PASS (meta-manager); 317k tokens, 32.3 min.
- S5 r1: fact-checker Opus (verify-1: 0 crit, 4 major, 17 minor; 292k, 10.2 min), fact-checker Sonnet (verify-1b: 0/3/22; 280k, 9.7 min), critic Sonnet (critic-1: 0/9/18; C2 3, C3 3, C4 4, C5 3, C6 3; 206k, 7.6 min). Gate: FAIL → S5→S4 revision.
- S5→S4 r1 (writer, Sonnet, fresh): 73 findings answered (70 changed, 1 partial, 2 outside the post folder); 7,498 words; 178k tokens, 22.2 min. Meta-manager: vec2d hit area 46 px (critic m18), opt-in signed bars (critic m4).
- S5 round 2 launched (Opus + Sonnet checkers, Sonnet critic, all fresh).
- S5 r2: verify-2 (Opus) 0/1/16, 293k, 9.7 min; verify-2b (Sonnet) 0/1/16; critic-2 (Sonnet) 0/3/16, C2 4, C3 3, C4 4, C5 4, C6 3, 275k, 9.1 min. Gate: FAIL. Note: response-1 claimed audio changes that were not made (V1B-m14) — the r2 reviser must diff the audio.
