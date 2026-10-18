---
name: ai4read-charter
description: Operating charter for AI4Read — read at the start of every session that touches this project.
updated: 2026-10-11
---

# AI4Read — Project Charter

## 1. Mission

Build **intuition and sense** — not just knowledge — for Kunhao Yang's work as a computational social scientist and for his life as a foreign resident in Japan. Facts are cheap in the GenAI era; the ability to *see a problem from the right angle*, transfer classic instances to new situations, and ask insightful questions is not. That ability comes from deep, systematic, cross-disciplinary reading **plus active practice**.

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

Every weekly topic **starts from a phenomenon** (application layer, a recent paper, or Kunhao's own question) and **ends by re-reading it through foundational lenses**.

## 4. Workflow

1. **Canon catalog** (`canon/<field>.md`): verified bibliography per field, tiered core / deep / reference, with access notes. Plus a *concept spine*, *canonical instances*, and *bridges*.
2. **Library** (Google Drive `AI4Read/library/<field>/`): source PDFs. Free legal copies fetched by Claude; others supplied by Kunhao.
3. **Just-in-time digests**: a work is digested chapter-by-chapter *when a topic needs it*, from the actual text, into `wiki/works/`. No mass pre-digestion.
4. **Knowledge graph** (`wiki/`): concept, instance, person, phenomenon, question nodes, linked with typed edges.
5. **Topic post** (every 1–2 weeks): blog with interactive explainer + audio + exercises.
6. **Discussion** on the phone → **notes** (`notes/`) → learner state update → new links in the graph.
7. **Public post** (optional): polished version on khyang-lab.org.
8. **Paper card** (weekly): one recent paper from top CSS venues, short format, expandable into a full post.

## 5. Post template (topic posts)

1. **Hook** — a story, puzzle, or everyday phenomenon. Build the intuitive picture first.
2. **Guess first** — a prediction prompt before any answer.
3. **The phenomenon in its home field** — application-layer details.
4. **Through the lenses** — re-read the premise/mechanism from 2–4 foundational fields. State the link type (same-math / structural analogy / metaphor).
5. **The math ladder** — from high-school level to graduate level, step by step, with toy data at each rung. No skipped steps.
6. **Interactive explainer** — sliders/simulations that run on a phone.
7. **Your turn** — a Python notebook (run on Kunhao's computer) and one transfer challenge.
8. **Where this shows up in your work** — tie-in to the 3C research.
9. **Recall questions** — 5–8; some reappear in later posts (spaced review, without naming the earlier post).
10. **How to say it in English** — 6–10 useful phrases/collocations from the post (B2–C1), collapsible.
11. **Sources** — verified only.

Paper cards: claim → method → key figure → lenses (1–2) → what to doubt → one question for Kunhao. ~10-minute read.

## 6. Style guide

- English at **B2 level, some C1**. Short sentences. Define every technical term at first use.
- **Intuition before formalism**, always. Concrete example → pattern → formula → general theory.
- **Toy data ladders**: small numbers you can compute by hand (e.g., a 4-word language, a village of 5 voters, a 2×2 matrix).
- **Canonical toy worlds** (`toyworlds.md`) may be reused across posts so connections become visible, but **every post stands alone**: it re-introduces each toy, term and result it uses, and never cites another post (WRITING §0).
- One notation across the whole project: `notation.md`. Logs are base 2 (bits) unless stated.
- Mobile first: no wide tables, formulas broken into short lines, every figure readable at 375 px.

## 7. Audio

- Each post has an **audio script** written *for the ear* (not a reading of the page): formulas spoken in words, figures described, recaps at section ends.
- Audio is split into **chapters** matching post sections, so a single section can be looped.
- Player: loop post / loop section, speed 0.75–1.5×, lock-screen controls, offline.
- Source mark: every audio file says and carries “AI4Read from CSS Lab” (spoken intro + MP3 metadata; see WRITING.md §8b).

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

- Topic post: every 1–2 weeks. Paper card: weekly (scheduled scan, Monday morning JST).
- Venues (editable): Nature Human Behaviour, PNAS, PNAS Nexus, Science Advances, Nature Computational Science, EPJ Data Science, Journal of Computational Social Science, Journal of Communication, Political Analysis, APSR; ICWSM, CSCW, WWW, IC2S2, ACL/EMNLP (CSS & society tracks).

## 13. Infrastructure map

| Piece | Where |
|---|---|
| Canonical knowledge base (wiki, canon, posts, notes) | GitHub private repo `CSS-Laboratory/ai4read` |
| Source library (PDFs) | Google Drive `My Drive/Book/AI4Read/library/` (no git inside Drive) |
| Private reader (posts + audio) | Phone-first installable web app (PWA) on Cloudflare Pages, built from this repo, behind Cloudflare Access email login (planned; first posts as private Claude artifacts) |
| Audio synthesis | Kokoro-82M open-source TTS (ONNX), run in Claude's workspace; MP3 per section; no cloud credentials needed |
| Discussion | Claude app on the phone, AI4Read project; each post section has a "Discuss" button that copies a ready prompt (post id + section) |
| Canon data | `canon/<field>.md` (human-readable) → `canon/catalog.json` via `scripts/parse_canon.py` |
| Public posts | khyang-lab.org |
