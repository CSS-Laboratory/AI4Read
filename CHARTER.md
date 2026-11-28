---
name: ai4read-charter
description: Operating charter for AI4Read — read at the start of every session that touches this project.
updated: 2026-11-28 (Four Layers template, weekly field series, website blogs, English packs retired)
---

# AI4Read — Project Charter

## 1. Mission

Build **intuition and sense** — not just knowledge — for Kunhao Yang's work as a computational social scientist and for his life as a foreign resident in Japan. Facts are cheap in the GenAI era; the ability to *see a problem from the right angle*, transfer classic instances to new situations, and ask insightful questions is not. That ability comes from deep, systematic, cross-disciplinary reading **plus active practice**.

Since 2026-11-28 the posts are also **public blogs** on khyang-lab.org, for Kunhao and for other readers. Their shared aim is a **computational-social-science imagination**, in the sense of C. Wright Mills' *The Sociological Imagination* (1959): the quality of mind that moves between a personal trouble and a public issue, between one perspective and another, and between the smallest mechanism and the structure of a whole society. Each post builds intuition for one important idea of a field, and then turns it into questions about society.

## 2. Learner profile (calibrate every output to this)

- Assistant professor, computational social science (Shibaura Institute of Technology, Japan). Research "3C": **Collaboration** (network science, online innovation), **Communication** (crisis/risk communication, framing, climate misinformation, conspiracy theories), **Computation** (explainable representation learning, LLM surrogate labeling, cross-lingual LLM safety, social simulation).
- Uses Python daily. Runs code on his own computer.
- Trilingual (Chinese, Japanese, English). Uses AI4Read posts **also to learn how to talk about science in English**.
- **Assume only high-school knowledge** of every topic. Climb step by step to graduate level. Never skip a step, including math.
- Reads and discusses **on a phone**. Also listens to posts as **loopable audio**.

## 3. Structure: two layers, twelve fields

### Foundation layer (the lenses)
| Field | Strands in scope |
|---|---|
| Information theory | Shannon theory (entropy, mutual information, coding, capacity, rate–distortion), KL / cross-entropy, MDL & Kolmogorov complexity, max-entropy (Jaynes) |
| Bayesian theory & modeling | Probability as logic, inference, hierarchical models, Bayesian workflow, computation, Bayesian cognition; **causal inference** (Pearl, Rubin) as a strand |
| Analytic philosophy | Philosophy of language (meaning, reference, speech acts, implicature), epistemology, philosophy of science, logic basics |
| Communication theory | Craig's seven traditions as the map; Shannon–Weaver; media effects (agenda setting, framing, spiral of silence, cultivation, two-step flow, diffusion); public sphere & systems theory; risk communication |
| Linear algebra | Vectors, spaces, linear maps, eigen/SVD, projections; geometric intuition; applications (PCA, PageRank, spectral graphs, embeddings) |
| Theory of mind | (a) philosophy of mind (intentional stance, theory-theory vs simulation), (b) developmental psychology (false-belief tasks), (c) computational ToM (Bayesian inverse planning, RSA), (d) the LLM-ToM debate |
| Decision & game theory | Expected utility, subjective probability, prospect theory, Nash equilibrium, common knowledge, focal points, conventions, level-k reasoning, cooperation, mechanism design |
| Control theory & cybernetics | Feedback and stability, cybernetics and requisite variety, state-space models, Kalman filtering, controllability/observability, optimal control and dynamic programming, reinforcement learning as control, control in biology, cognition and society (homeostasis, thermostatic public, policy rules). Boundary: nonlinear dynamics itself lives in complex systems |

### Application layer (the phenomena)
Complex systems · Large language models · Economics & finance · Political science.

**Weekly series, one field at a time (since 2026-11-28).** The posts walk through the fields one by one: a series of about 4–7 weekly posts climbs one field's concept spine (`canon/<field>.md`), then the next field starts. The plan lives in `series/` (`series/README.md` gives the field order; `series/<field>.md` gives the posts). Kunhao may add an extra post on his own topic in any week. Every post still **starts from a phenomenon** and **ends by re-reading it through other fields** (Four Layers, §5).

## 4. Workflow

1. **Canon catalog** (`canon/<field>.md`): verified bibliography per field, tiered core / deep / reference, with access notes. Plus a *concept spine*, *canonical instances*, and *bridges*.
2. **Library** (Google Drive `AI4Read/library/<field>/`): source PDFs. Free legal copies fetched by Claude; others supplied by Kunhao.
3. **Just-in-time digests**: a work is digested chapter-by-chapter *when a topic needs it*, from the actual text, into `wiki/works/`. No mass pre-digestion.
4. **Knowledge graph** (`wiki/`): concept, instance, person, phenomenon, question nodes, linked with typed edges.
5. **Series post** (weekly): blog with interactive explainer, audio, exercises. Written and checked in Claude Code (`phase2/RUNBOOK.md`).
6. **Discussion** on the phone → **notes** (`notes/`) → learner state update → new links in the graph.
7. **Publish** on khyang-lab.org as a blog post: English text and English audio public; Chinese text and Chinese audio for Kunhao only (§7).
8. **Paper card** (weekly): one recent paper from top CSS venues, short format, expandable into a full post.

## 5. Post template: the Four Layers (since 2026-11-28)

Every post explains **one core idea** in four layers, in order, never skipping one, each going one level deeper (Jakob Schwichtenberg's "four layers of understanding", *A Physics Travel Guide*). Most readers find technical material hard because they skip the early layers and land in formulas and jargon. Then the post turns the idea toward society. WRITING §1a gives the rules for each layer.

0. **Title as a question, and a one-line preview** of the answer (WRITING §0).
1. **Motivation: why should we care?** No new concepts yet. Before this idea, how did people handle this kind of problem, and what hurt: too expensive, too slow, impossible to measure, or a strange, counterintuitive phenomenon? What urgent problem does the idea solve? The layer ends with **Guess first**, a prediction prompt.
2. **Intuition: the café version.** **No formulas, symbols, abbreviations or unexplained jargon.** One everyday or engineering scene that is *structurally isomorphic* to the core mechanism, told in full: why the old way goes wrong, and which rule the idea changes to fix it. The reader leaves with a complete mental map.
3. **Concrete: the smallest real example.** Drop the analogy and return to the field's own setting. Work one tiny input → output example with numbers you can do by hand. Show only the essential equations, rules or algorithm steps, and map **every term** to a part of the layer-2 scene: what it does and which data it turns into what. Give the key numbers before and after the crucial change. Each new concept climbs the ladder (WRITING §2). The interactive explainer and the Python notebook live here.
4. **Abstract: the principle, its relatives and its limits.**
   - (a) **What it really is**: once the task is stripped away, what the method does mathematically, in information terms, or as a system mechanism.
   - (b) **The same idea elsewhere**: classic ideas in other fields that say the same thing. These are the lenses; each states its link type (same-math / structural analogy / metaphor) and what it adds.
   - (c) **Failure boundaries (required)**: the hidden assumptions, and when the idea fails, gives biased results or cannot replace the old approach. Say where the layer-2 analogy breaks.
5. **The CSS imagination.** Turn the idea into questions about society, with Mills' moves (WRITING §1b). Link a personal trouble to a public issue; look through another discipline's eyes; push to the extremes and invert the scale; compare cases and periods. End with 1–2 open research questions and the tie-in to Kunhao's 3C research.
6. **Your turn**: a Python notebook (run on Kunhao's computer) and one transfer challenge.
7. **Recall questions**: 5–8. Some reappear in later posts as spaced review, without naming the earlier post.
8. **Sources**: verified only.

**The layers connect.** Layer 3's equations echo layer 2's scene; layer 4 grows out of layer 3's mechanism; layer 5 starts from layer 4's limits. Plain, restrained language: no praise, no boilerplate. Where the source is unpublished or the evidence is thin, say so.

*Retired:* the "How to say it in English" section (left the post on 2026-10-25), and the separate C1–C2 English packs for Margin (stopped on 2026-11-28, when Kunhao ended the English-learning project). Old packs stay in `site/mewiki/packs/` as history.

Paper cards: claim → method → key figure → lenses (1–2) → what to doubt → one question for Kunhao. ~10-minute read.

## 6. Style guide

- English at **B2 level, some C1**. Short sentences. Define every technical term at first use.
- **Intuition before formalism**, always. Concrete example → pattern → formula → general theory.
- **Toy data ladders**: small numbers you can compute by hand (e.g., a 4-word language, a village of 5 voters, a 2×2 matrix).
- **Canonical toy worlds** (`toyworlds.md`) may be reused across posts so connections become visible, but **every post stands alone**: it re-introduces each toy, term and result it uses, and never cites another post (WRITING §0).
- One notation across the whole project: `notation.md`. Logs are base 2 (bits) unless stated.
- Mobile first: no wide tables, formulas broken into short lines, every figure readable at 375 px.

## 7. Audio and languages

- Each post has an **English audio script** written *for the ear* (not a reading of the page): formulas spoken in words, figures described, recaps at section ends.
- Audio is split into **chapters** matching post sections, so a single section can be looped.
- Player: loop post / loop section, speed 0.75–1.5×, lock-screen controls, offline.
- Source mark: every audio file says and carries “AI4Read from CSS Lab” (spoken intro + MP3 metadata; see WRITING.md §8b).
- **Who sees what (2026-11-28).** Public readers get the English text and the English audio. **Only Kunhao** (signed in) gets the **Chinese text** (a faithful translation of the post) and the **Chinese audio**. Ask-Claude, notes and annotations are owner-only too, so public readers cannot run up Vertex costs.

## 8. Wiki schema

```
wiki/
  concepts/     one concept per file (entropy, eigenvector, common-knowledge…)
  instances/    canonical examples (monty-hall, sally-anne, shannon-guessing-game…)
  works/        digests of books/papers, chapter-level, with page refs
  people/       thinkers (short)
  phenomena/    application-layer phenomena (polarization, hallucination, bubbles…)
  questions/    open questions Kunhao or Claude raised
```

Frontmatter (all nodes): `id, type, fields[], level (HS/UG/grad), sources[], grounding, links[]`.

**Link types** (always state one):
- `same-math` — identical mathematical structure
- `structural-analogy` — same shape of argument, different math
- `metaphor` — inspiring, not a proof
- `special-case-of`, `uses-method`, `contradicts`, `historical-influence`

Wikilinks `[[id]]` throughout (Obsidian-compatible).

## 9. Source & citation policy

- Every digest carries `grounding: primary-text | secondary | unverified`. Only `primary-text` digests may support claims in posts without a caveat.
- Every citation in a post is verified against a real source (URL/DOI). No unverifiable citations.
- Free access only from legal sources (author, publisher OA, arXiv, university repositories, OCW, SEP; archive.org only for public-domain works). **Never** shadow libraries.
- Digests are in our own words with page references; no long quotations.
- Digests are **verified maps, not guaranteed truth**: after model verification, audits find ≈ 0.5 subtle error per unit (mostly hedges and voice; math is near-perfect). Every claim used in a post is re-checked against the source page when the post is written. Public posts follow normal academic quoting norms and disclose AI assistance.

## 10. Quality gate (before a post reaches Kunhao)

- Every numerical example and derivation is checked by running code.
- An independent reviewer agent (not the author) checks: correctness, skipped steps, level jumps, link-type honesty, English level.
- Mobile render check at phone width.

## 11. Learner state

`learner/state.md` — what Kunhao has understood, open confusions, his questions and ideas, preferred examples. Updated after every discussion; read before writing every post.

## 12. Cadence & venues

- Series post: **weekly** (series plan in `series/`), plus an occasional extra post on Kunhao's topic. Paper card: weekly (scheduled scan, Monday morning JST).
- Venues (editable): Nature Human Behaviour, PNAS, PNAS Nexus, Science Advances, Nature Computational Science, EPJ Data Science, Journal of Computational Social Science, Journal of Communication, Political Analysis, APSR; ICWSM, CSCW, WWW, IC2S2, ACL/EMNLP (CSS & society tracks).

## 13. Infrastructure map

| Piece | Where |
|---|---|
| Canonical knowledge base (wiki, canon, posts, notes) | GitHub private repo `CSS-Laboratory/ai4read` |
| Source library (PDFs) | Google Drive `My Drive/Book/AI4Read/library/` (no git inside Drive) |
| Blog (posts + audio) | khyang-lab.org blog, built from this repo (`site/ai4read/`) and deployed by Kunhao's website agent. English public; Chinese text and audio, notes and Ask-Claude owner-only behind Cloudflare Access (since 2026-11-28; the separate /ai4read page is retired) |
| Writing and checking | Claude Code on Kunhao's Mac (`~/code/AI4Read`), with fresh subagents as independent checkers (`phase2/RUNBOOK.md`); before 2026-11-28, the claude.ai "Claude Work" setup |
| Audio synthesis | English: Kokoro-82M open-source TTS (ONNX), run locally; MP3 per section; no cloud credentials. Chinese: Google Gemini-TTS, run by Kunhao under his own sign-in (WRITING §8b) |
| Discussion | Claude app on the phone, AI4Read project; each post section has a "Discuss" button that copies a ready prompt (post id + section) |
| Canon data | `canon/<field>.md` (human-readable) → `canon/catalog.json` via `scripts/parse_canon.py` |
| Public posts | khyang-lab.org blog (tags, keyword and tag search, sorting) |
