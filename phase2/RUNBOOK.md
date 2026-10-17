---
name: phase2-runbook
description: How the meta-manager runs one post through the phase-2 pipeline (2a: subagents on the subscription). Stages, who runs them, inputs, outputs, gates, and what to log.
date: 2026-10-17
---

# Phase 2 runbook (2a)

**Roles.** The meta-manager (Claude Opus, main session) runs the stages. It does not write post text. Each other role is a **fresh agent** with no shared context. Its system prompt is the built role prompt (`python3 phase2/assemble.py` → `phase2/prompts/build/<role>.md`), and it receives only the paths it needs.

| Stage | Agent (model) | Reads | Writes | Gate (checked by meta-manager) |
|---|---|---|---|---|
| S0 | planner (Sonnet) | Kunhao's input, KB survey | `topic-card.md` | Kunhao says go |
| S1 | planner (Sonnet) | topic card, source files in `sources/` and the library | `source-brief.md` | ≥ 8 units; each has a page and a quote |
| S2 | fact-checker (Opus) | brief, source files | `source-brief.verified.md`, `review/s2-check.md` | 0 unchecked units |
| S3 | writer (Sonnet) | card, verified brief, components | `outline.md` | rubric pre-check ≥ 4 (criteria 2, 4, 5) |
| S4 | writer (Sonnet) | outline + all above | `src/content.html`, `audio-script.md`, `english-gloss.json`, `numbers.md`, `self-review.md` | `check.mjs` passes; build passes |
| S5 | fact-checker (Opus) + critic (Sonnet) + render test | draft | `review/verify-N.md`, `review/critic-N.md` | 0 critical, 0 major, every criterion ≥ 4; ≤ 3 rounds, else meta-manager steps in |
| S5→S4 | writer (Sonnet) | findings | revised draft + `review/response-N.md` | each finding answered |
| S6 | meta-manager (scripts) | audio script, English section | MP3s (tagged "AI4Read from CSS Lab"), English pack | audio script checked like the text |
| S7 | meta-manager | build | claude.ai artifact (draft) and `site/ai4read/dist/<slug>/` | render test passes |
| S8 | writer (Sonnet) | Kunhao's notes | revisions, note answers, `rule-proposals.md` | each note closed |
| S9 | meta-manager | everything | WRITING / rubric updates (with Kunhao's OK), `learner/state.md`, `phase2/log.md` | — |

**Post folder:** `posts/<yyyy-mm-slug>/`. Copy `build.mjs` from post 01 and add the component library (`widgets.js`, `widgets.css`). Web sources the writer relies on are saved as text in `posts/<slug>/sources/` with their URL and access date, so the checker can verify them without the network.

**Commands**
- Widget numbers: `node site/ai4read/components/check.mjs posts/<slug>/src/content.html`.
- Render: `node posts/<slug>/build.mjs --site`, then `node site/ai4read/components/test.mjs site/ai4read/dist/<slug>/index.html`.
- Audio: `/tmp/ttsenv/bin/python scripts/tts_post.py posts/<slug>`. This tags the MP3s automatically.

**Log** (`phase2/log.md`, one block per stage): the agent and model, its tokens and duration (from the agent result), the gate result, and the number of findings. These numbers set the 2b cost estimate.

**Independence rules**
- The checker never sees the writer's self-review before its own pass.
- The critic never sees the writer's self-score.
- The meta-manager audits the post in full once every three posts, and always for the first post of the pipeline (post 02).
