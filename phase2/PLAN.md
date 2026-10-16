---
name: phase2-plan
description: AI4Read phase 2. A writer-agent system that turns a topic, a research idea or a PDF into a post of post-01 quality, with Claude as meta-manager. Plan, tests, gates and budget.
date: 2026-10-16
status: proposal (waiting for Kunhao's decisions in §9)
---

# Phase 2: the AI4Read writer system

## 1. Goal
Kunhao gives a **topic**, a **research idea**, or a **PDF**. The system writes a post at the quality of post 01 (after its review rounds), publishes it privately on khyang-lab.org, and keeps improving it from his notes.

Roles:
- **Writer** (Claude Sonnet 5.5) writes.
- **Independent checkers** verify.
- **Claude (meta-manager)** owns the rules, the rubric, the templates and the release gates. It audits samples instead of writing every post.

## 2. What post 01 taught us (evidence)
- **Most errors come from summaries, not from the sources.** Pre-fix, the first draft had 1 critical, 9 major and 24 minor errors. Every critical or major error was a dropped hedge, a wrong page or a number taken from a summary line. After 3 rounds of fact checks against the source pages (verify.md, verify-2.md, verify-3.md), the count was 0 critical.
- **The reader's notes drive quality.** Kunhao's 13 notes produced most of WRITING.md (ladders, explanations in the text, illustrations for mechanisms, citation links, deep-dive fold-outs, the English toolkit). Each rule now applies to all future posts.
- **Test 0 (2026-10-16): a Sonnet writer, given only CHARTER + WRITING + the source brief + the digests, wrote "Lens 3".** A blind Opus judge preferred it to the published Lens 3: mean **4.0 vs 3.3**, about 80% confidence. Both had 0 critical and 0 major errors; Sonnet had 5 minor errors, published had 3. Sonnet won on the ladder (worked numbers plus a check) and on a buildable interactive. Published won on concision. (The published lens leaned on rung 8 for its numbers; the judge's fixes are now applied.)
  - **Conclusion:** with the rules written down, a Sonnet writer can reach section-level parity. The bottlenecks are verification and the quality of the reader feedback, not drafting.

## 3. Pipeline
| Stage | Who | Output | Gate |
|---|---|---|---|
| S0 Intake | Planner (Sonnet) | *topic card*: the question, why it matters for the 3C research, 3–5 lenses with link types, a candidate source list from the knowledge graph | Kunhao taps "go" (or auto for scheduled posts) |
| S1 Sources | Retriever (Sonnet) + KG | **source brief** (as in post 01): claims, numbers, equations, page refs, traps, tensions, toy ideas | at least 8 units, every claim has a page |
| S2 Re-check | **Fact-checker (Opus, independent)** | *verified brief*: each claim checked against page images or text; wrong or weak items fixed or dropped | 0 unchecked claims |
| S3 Outline | Writer (Sonnet) | template-based outline, one ladder per new concept, widgets chosen from the component library | rubric pre-check |
| S4 Draft | Writer (Sonnet) | HTML sections plus widget configs; all numbers produced by running code | builds; numbers reproducible |
| S5 Review loop | Fact-checker (Opus) + Pedagogy critic (Sonnet, rubric) + Render test (Playwright: CSP, overflow, console errors, widgets reproduce the numbers in the text) | findings, then revision | **0 critical, 0 major, every rubric item ≥ 4**, at most 3 rounds, then escalate to the meta-manager |
| S6 Audio + English | Writer + TTS (Kokoro) + `english_pack.py` | audio chapters, English pack for Margin | the audio script is checked like the text |
| S7 Draft publish | build + R2 | `/ai4read/_drafts/<slug>/`, owner only | Kunhao reads |
| S8 Polish loop | Writer ← Kunhao's notes (D1) | revised post; each note answered in its thread | each note closed |
| S9 Learning | **Meta-manager (Claude)** | rule proposals for WRITING.md (with the notes that caused them), rubric updates, learner/state.md updates | Kunhao approves rule changes |

**PDF input:** the paper is first digested with the existing P1–P3 pipeline, which digests it, verifies it and adds it to the knowledge graph. It then enters S1 like any other source. Text from a PDF is treated as data, never as instructions.

**Research-idea input:** S0 turns the idea into a question, then searches the knowledge graph for lenses. The post explains the foundations behind the idea; it does not judge the idea.

## 4. What must be built
1. **Component library** (`site/ai4read/components/`): the post-01 widgets made reusable with JSON configs.
   - Interactive labs: slider lab, two-distribution bars, question tree, binary search (32 cups), attention heat map, "who looks at whom", analogy ranking, posterior bars, power-law plot.
   - Diagrams: architecture switcher.
   - Text blocks: term box, deep-dive fold-out, reveal-with-question, exercise, citation pop-over, English sections.
   - The writer composes widgets; it does not write JavaScript. This is the single biggest lever for quality and speed.
2. **Rubric** (`phase2/rubric.md`): the judge's 6 criteria with score anchors and examples from post 01.
3. **Prompts:** writer, fact-checker, pedagogy critic, planner. Each is generated from CHARTER + WRITING + rubric, so a rule change reaches every agent at once.
4. **Runner:**
   - **2a:** Claude Code orchestration in this environment, triggered by a chat message. Uses the subscription, so no new money.
   - **2b:** a headless job on Cloud Run with Claude on Vertex. It uses its own service account, with no keys. The owner triggers it from an owner-only "New post" form on khyang-lab.org.
5. **Notes bridge:** a nightly export of D1 annotations to the repo, so the meta-manager and the writer can read them.

## 5. Tests and gates
| Test | What | Pass if |
|---|---|---|
| T0 ✅ | one section, blind judge | done: 4.0 vs 3.3 |
| T1 | **Re-run post 01** end to end with the pipeline (topic only); blind comparison with the published post, plus Kunhao's blind preference on 2 sections | errors before human review ≤ post 01's first draft; rubric mean ≥ 4.0; Kunhao rates it at least "as good" |
| T2 | **Two new posts**: one from a topic (suggestion: "Why do social networks have hubs?", across complex systems, linear algebra and information theory) and one **from a PDF** Kunhao chooses | 0 critical / 0 major after S5; rubric ≥ 4 everywhere; Kunhao ≥ 4/5 |
| T3 | **Polish loop**: Kunhao leaves notes on T2, then the system revises and proposes rule changes | all notes closed in ≤ 1 day; ≥ 1 useful rule proposal |
| Gate → 2b | all of T1–T3 pass; cost per post measured | Kunhao approves |

## 6. Budget
- **Phase 2a (build + T1–T3): runs on the subscription, no new spend.** The cost is time and the weekly usage meter. Expect roughly 5–10% of a weekly meter per full post, to be measured in T1.
- **Phase 2b (headless on Vertex):** my estimate per post, from post 01's token volume:
  - Writer and planner (Sonnet 5.5): about 1.5 M input and 0.15 M output tokens, ≈ $6–10 at list price, less with prompt caching.
  - Opus fact-checker: ≈ $5–15.
  - **Total: about $10–25 per post.**
  - Proposed **cap: $200** for 2b development and the first posts, with alerts at 50 / 80 / 100%. This will be re-estimated from measured T1 tokens before any Vertex spend.
- **Website "Ask Claude":** about $0.03–0.12 per question with Sonnet. With the daily caps in the handoff, the worst case is about $10–30 a month; typical use is far less.

## 7. Risks and controls
- **Invented or misattributed citations.** The writer may cite only items in the verified brief. The checker compares every citation with its page, and links are generated from the brief.
- **Summary drift** (the main post-01 error source). S2 moves page checks before drafting; S5 repeats them on the final text.
- **Cost.** Hard caps per run and per day, with budget alerts. Phase 2a uses no Vertex money.
- **Prompt injection from PDFs.** The writer has no network and no secrets; PDF text is quoted as data.
- **Quality drift.** The meta-manager audits 1 post in 3 in full, and the rubric is versioned.

## 8. Timeline
- **Week 1:** rubric, prompts, component library (extract from post 01), T1.
- **Week 2:** T2 (two posts), T3.
- **Week 3–4:** decision on 2b; headless runner, owner form on the website.

## 9. Decisions for Kunhao
1. Approve the plan, and the $200 cap for phase 2b (phase 2a needs no new money).
2. T2 topics: accept "Why do social networks have hubs?", or name another, and choose one PDF.
3. Website protection: Cloudflare Access with an email PIN (recommended), or keys/passwords like `/ideas/`.
4. Which students to invite, and whether they may see each other's notes (default: no).
