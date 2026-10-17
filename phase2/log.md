# Phase 2 run log

One block per stage. Token counts come from the agent results (all subagent tokens, including cache reads), and durations are wall-clock. These numbers set the cost estimate for 2b.

## Post 02 · 2026-10-ai-finance (T2, topic input)
| Stage | Agent (model) | Tokens | Time | Result |
|---|---|---|---|---|
| pre-S0 research: Harari claims | general-purpose (Opus) | 180,948 | 24.2 min | 20 claims (15 V, 4 S, 1 U), 6 critiques; machine transcripts of BIS 2024 and WEF 2026 audio. Meta-manager spot-check: key 10-year quotes confirmed. |
| pre-S0 KB survey | Explore (Opus) | 182,755 | 7.8 min | lenses with audit status, wiki nodes, gaps, post-01 hooks |
| S0 topic card | planner (Sonnet 5.5) | 136,365 | 3.5 min | 5 sub-claims, 4 lenses, 3 interactives, 3 decisions. Meta-review: pass with 5 edits (home-field evidence section, iterate-toy framing, Arora step, Lens 4 focus, W5). Numbers rechecked: all correct. |
| S1 source brief | planner (Sonnet 5.5) | 338,951 | 32.4 min | 42 units: 25 seen at source, 12 from digests needing a source check, 5 unseen; 19 traps; 13 findings that correct the card (no evidence yet for (a); Harari's "complicated" means data volume; Arora's caveats; Ashby gives 3 levers; FSB URL fixed; the FCIC records a correlation error). |
