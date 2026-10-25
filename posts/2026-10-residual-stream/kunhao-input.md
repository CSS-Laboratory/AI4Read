Post 03 — "The lens": the residual stream as a bus

Context
- A new field was added to the canon on 2026-10-25: canon/interpretability.md
  (34 items, 7 strands). catalog.json was regenerated and
  canon/free-manifest-interpretability.json lists the free downloads. Nothing
  is committed yet; review the diff, then commit it as "canon: add
  interpretability field (34 items, 7 strands)".
- Post 03 is strand 1 of that field. The next six posts will follow strands
  2–7, one per post, as described in the "Reading path (AI4Read posts)"
  section at the end of the file. Read that section first.

Start as usual
Read CLAUDE.md, CHARTER.md, WRITING.md, learner/state.md, phase2/RUNBOOK.md,
phase2/rubric.md, phase2/log.md, then the newest post folder, then
canon/interpretability.md (Scope, strand "The lens", Concept spine, Bridges,
Reading path). Run phase2/assemble.py to build the role prompts. Follow the
phase-2 runbook stage by stage (S0–S9) with fresh agents per role.

The phenomenon the post opens from (Kunhao's own work)
In the Discipline project (separate repo; do not touch it), I read the hidden
states of open models (Gemma 3, Qwen3, Llama 3, Mistral; base and instruct
checkpoints) at a chosen layer for prompts about "an expert in {discipline}",
train linear probes for trust pillars on those states, compare base and
instruct with representational similarity analysis, and steer the model by
adding "primed" directions. I have done all of this without ever saying what a
hidden state IS in the model's own terms. Post 03 should give me that: every
"hidden state read" I take is a read of the residual stream at one layer, and
everything I do to it (probe, compare, steer) is a linear operation on that
stream.

The lens the post must leave the reader with
A transformer is a computation you can read and edit. The residual stream is a
shared bus: each layer reads from it and writes back into it, and the stream
at layer L is the sum of the embedding plus every attention and MLP output
before L. Concepts tend to live as directions in that bus; behaviours are
circuits that read and write those directions; post-training mostly rewires
which directions get read out, not what is represented. The post must earn
this sentence by sentence, from high-school knowledge, never skipping a step,
with the math written out (vectors, sums, projections; no eigen-decomposition
yet, that is strand 2).

Sources (digest just-in-time, per DIGEST_SPEC, with subscription subagents —
the Vertex budget is at its cap)
- olah-2020-zoom-in (Distill) — the three claims: features, circuits,
  universality.
- elhage-2021-circuits (LLM canon; transformer-circuits.pub/2021/framework) —
  only the sections on the residual stream as a communication channel, virtual
  weights, and "no privileged basis". Skip the attention-head algebra and
  induction heads; they belong to strand 4.
- nanda-2022-glossary — the entries for residual stream, logit lens, hook,
  activation, direction. Save the page text into posts/<slug>/sources/ with
  URL and access date so the checker can verify offline.
Do not add facts from memory; every claim in the post carries a source and
page/section reference as the spec requires.

Post structure (adapt the standard template)
1. Open with my phenomenon in plain words: "I pull a 4096-number vector out of
   layer 20. What is it?"
2. Build the bus picture from scratch: tokens → embedding vector → each block
   adds a vector → the running sum. Make the reader add two small vectors by
   hand before any diagram.
3. The three claims from Zoom In, stated as bets, not facts.
4. Reads and writes as projections: what a probe sees, what steering adds.
   Keep to 2-D examples with numbers.
5. Close by re-reading the phenomenon through two foundation lenses:
   linear algebra (the stream is a vector sum; a probe is a projection onto a
   direction; steering is translation) and information theory (one channel,
   many writers, limited dimensions — set up superposition as the question
   for strand 5 without answering it).
6. Exercises: 3–5, hand-computable, plus one open question for strand 2.

Interactive components
- A residual-stream bus diagram: layers along the top, the stream as one
  horizontal band, each layer drawing an arrow in and an arrow out; tapping a
  layer shows "stream so far = embedding + Σ outputs".
- A 2-D toy: a few activation points, one draggable direction, live
  projection values; a second mode that adds a vector to every point
  (steering). This toy is the running toy world for strands 2–7; add it to
  toyworlds.md.

Notebook (posts/<slug>/notebook/)
Two notebooks, both runnable on my Mac without network once models are
present:
- 01_bus_gpt2.ipynb — TransformerLens on GPT-2 small (ARENA 1.1–1.2 scope
  only): cache one forward pass, verify numerically that resid_post at layer L
  equals resid_pre plus attn_out plus mlp_out, plot the norm of the stream by
  layer, run the logit lens by layer. No induction-head hunt; that is strand 4.
- 02_bus_my_model.ipynb — the same decomposition on one of my local models
  with plain Hugging Face hooks (output_hidden_states plus forward hooks on
  the attention and MLP outputs), so I can see that my Discipline "hidden
  state read" is the same object. Parameterise model path; default to
  Qwen3-1.7B-Base if it loads, else GPT-2 small. Do not reproduce any
  Discipline data or results.
Each notebook ends with the exercise cells left blank for me.

Wiki and graph
Add the strand-1 concepts from the concept spine (residual stream read/write,
direction, projection, logit lens, no privileged basis) as nodes, and link
them with same-math edges to the existing linear-algebra nodes for vector
addition, projection and change of basis. Propose bridges only; mark them
candidate.

Learner and standards
Calibrate to learner/state.md; reuse what worked (interactive mechanisms over
prose; definitions in the main text, one term box at most). English at B2
with some C1; gloss new terms in english-gloss.json. Audio script as usual,
loopable, tagged "AI4Read from CSS Lab".

Gates
Stop after S0 and show me the topic card for approval before S1. Apply the
S5 gate exactly (0 critical, 0 major, every criterion ≥ 4, ≤ 3 rounds). After
S7, publish the draft artifact per RESUME §2.7 (db, sample, downloads) and
give me the link. Back up after the milestone per RESUME §3, and append to
phase2/log.md. If a step needs something that is not in the repo or the
library, say what is missing rather than inventing it.