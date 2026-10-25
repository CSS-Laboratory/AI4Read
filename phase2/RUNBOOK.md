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

**Post folder:** `posts/<yyyy-mm-slug>/` with `post.json` (title, short, num, date, summary, cite regex → key). Build with `node site/ai4read/build-post.mjs posts/<slug> [--site]`. It combines the shared template (`site/ai4read/template/`: style, annotation sidebar, audio player, guesses, citation pop-overs) with the component library. Web sources the writer relies on are saved as text in `posts/<slug>/sources/` with their URL and access date, so the checker can verify them without the network.

**Commands**
- Widget numbers: `node site/ai4read/components/check.mjs posts/<slug>/src/content.html`.
- Render: `node site/ai4read/build-post.mjs posts/<slug> --site`, then `node site/ai4read/dev/mock-server.mjs 8799 &` and `node site/ai4read/components/test.mjs /ai4read/<slug>/ --base http://127.0.0.1:8799`. Also test the standalone (artifact) page, whose scripts are inline: `node site/ai4read/components/test.mjs posts/<slug>/index.html --inline`. Both must PASS before publishing (2026-10-18: the artifact page had silently lost its widgets because an inlined script contained `</script>`).
- Audio: `/tmp/ttsenv/bin/python scripts/tts_post.py posts/<slug>`. This tags the MP3s automatically.

**Log** (`phase2/log.md`, one block per stage): the agent and model, its tokens and duration (from the agent result), the gate result, and the number of findings. These numbers set the 2b cost estimate.

**Independence rules**
- The checker never sees the writer's self-review before its own pass.
- The critic never sees the writer's self-score.
- The meta-manager audits the post in full once every three posts, and always for the first post of the pipeline (post 02).

**Review hygiene (2026-10-18).** Do not regenerate `src/content.html` while checkers are reading it: edit the template, and regenerate only after every agent of the round has reported. Otherwise findings point at two versions.

**Lessons from post 03 (2026-10-25).**
- Saving web sources: strip HTML comments (and scripts) before writing the `.txt`; the S1 planner quoted text that was commented out of the published page.
- The writer never edits `source-brief.verified.md` or `notebook/results.md`; facts it needs go to `requests.md`. If it does, the meta-manager marks the edit UNVERIFIED and the next checker verifies or strikes it.
- `response-N.md` must quote the new audio line for every audio fix; checkers compare the claim with `audio-script.md` (a round-1 response claimed audio fixes that were not made).
- Notebook builders state the denominator of every relative error in `results.md`.
- A gate missed after round 3 by a single, local finding: the meta-manager corrects any pipeline file at fault (here `results.md`), a fresh writer makes a targeted fix pass, and fresh checkers (facts and pedagogy) re-check the diff (`verify-3c.md`, `critic-3c.md`).
