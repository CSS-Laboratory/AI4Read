---
id: 2026-10-residual-stream/outline
type: outline
stage: S3
post_number: 03
slug: 2026-10-residual-stream
title: "What Is a Hidden State? The Residual Stream, Read and Written"
short: "The Residual Stream"
author: AI4Read writer (fresh agent)
date: 2026-10-25
inputs: [topic-card.md (approved, Decisions 2026-10-25), kunhao-input.md, source-brief.verified.md, components/README.md + gallery.html, post-01 content.html (markup only)]
main_text_budget: "6,630 words planned (cap 7,500; target about 6,600)"
status: outline for the S3 gate; no S4 text written
---

# Post 03 · Outline (S3)

Conventions in this file. "Unit n" = unit n of `source-brief.verified.md`; "Ln" = line in the saved `.txt` (checker use only: the post cites by the section heading of the saved page, because the sources are web pages). "Slot Rn" = a place for a number from `notebook/results.md`; no value is written here (see §9). "Ours" = our reasoning or toy numbers. Toy numbers are from `toyworlds.md` W9 (proposed below) and were re-run by me in numpy on 2026-10-25; the S4 writer re-runs them through `check.mjs`.

## 0. The plan in one table

| # | id (`data-ch`) | Section | Words | Widgets | Guess answer | Brief units |
|---|---|---|---|---|---|---|
| 1 | hook | The list in the middle (hook + one-line preview) | 300 | none | | 5, 10 |
| 2 | guess | Make three predictions | 250 | none | | |
| 3 | sum | The stream is a running sum | 1,250 | `stepper` sum-table; `diagram` bus (5 steps, preview); `diagram` positions | g1 | 5, 10, 9 |
| 4 | bets | Three bets, held lightly | 650 | none (fold-out F1) | | 1, 2, 3, 12 |
| 5 | rw | Reads and writes | 900 | `lab` read-split | g2 | 6, 7, 11, 2 |
| 6 | dir | Probe and push: directions in a toy cloud | 900 | `vec2d` probe-push; `lab` rotate | g3 | 1, 8, 11, 12, 14, 3 |
| 7 | answer | Short answer (boxed) | 350 | none | | all |
| 8 | lens-linalg | Lens 1 · Linear algebra | 550 | none (reuses §5–6 figures by description only) | | 6, 8, 11, 12 |
| 9 | lens-info | Lens 2 · Information theory | 380 | `lab` three-features | | 4, 7, 5 |
| 10 | turn | Your turn: notebooks, five exercises, one open question | 420 | none | | 9, 13 (as fold-out) |
| 11 | work | Where this shows up in your work | 330 | none (three cards) | | 14, 12 |
| 12 | recall | Test yourself | 350 | none | | |
| – | sources | Sources | not counted | | | |
| | | **Total main text** | **6,630** | 7 widgets + 2 static diagrams in fold-outs | | |

Fold-outs (not counted): F1 *Look inside: Olah's three claims, sorted by firmness*; F2 *Look inside: a norm before every read*; F3 *Look inside: the logit lens is one more read*. The audio only says each exists.

**Mapping to CHARTER §5.** Item 1 = §1; item 2 = §2; item 3 (phenomenon in its home field) = §3–§6, because the "home field" mechanism of a hidden state is the 2-D arithmetic itself, so the math ladder (item 5) and the interactives (item 6) are built into §3, §5 and §6 rather than set apart; item 4 (lenses) = §7–§9, which re-read the whole phenomenon; items 7–9 = §10–§12; item 11 = Sources. Item 10 (English) is not part of the post (WRITING §8, v0.8).

**Deviation to flag (for the meta-manager).** Topic-card §11 puts the three bets after reads and writes. The task message and Kunhao's spec put them before ("the bus picture, Olah's three claims as bets, reads and writes as projections"). I follow the spec. The bets section needs nothing from later sections (a direction is first met there as a plain-words recipe, with an instance), and §5 and §6 each end by cashing in one bet in numbers. If you prefer the card's order, swap §4 with §5–§6 and move the three "cash-in" sentences into §4; word counts do not change.

## 1. Decisions applied (topic card, 2026-10-25)

1. Two lenses (linear algebra, information theory). "A probe observes, steering intervenes" is one paragraph inside Lens 1 (§8).
2. The post-training clause stays out of the lens. One sentence in §11, labelled "a working assumption, untested here".
3. The open question points toward eigen-decomposition. The text does not name or number another post (WRITING §0); it only says the question is left open.
4. The 2-D toy is `vec2d` (copied from `cfg-vec2d` in the gallery). Fallback: the card's `plot` version if `vec2d` fails the render test.
5. Title as proposed. "Bus" is our metaphor and lives in §3 with a trap box. Sources' words are *stream*, *channel*, *shared bandwidth/shared memory*.
6. S2 corrections honoured throughout (see §10 of this file for the checklist).

## 2. Terms, in the order they first appear (each defined in the sentence where it first appears)

hidden state, token, vector, dimension (the number of entries), embedding (we reserve the word for the starting vector x₀; trap 3), block and sub-layer (attention, MLP; trap 4), stream, bus (ours), position, write, read (inside the model) vs read out (our instrument), norm (a normalisation step; no formula beyond the toy in F2), feature, direction (our plain-words recipe first, Olah's wording quoted in §4), circuit, universality, dot product, orthogonal, length and unit vector, score, probe, margin, steering, translation vs affine vs linear, privileged basis, superposition (model-side sense only; for sums the post says "adds"). One **term box** only: *Residual stream (also: hidden state, embedding)*, in §3. Everything else is defined in-sentence (WRITING §3).

---

## 3. Section plans

### §1 hook · 300 words · audio chapter `hook`

**Purpose.** Make the reader want the answer to "what is that list?" and give them the picture of a running balance before any vocabulary.

**Content.**
- P1 (puzzle, second person, generic; no Discipline data or prompts): stop a language model partway, copy out a list of 4,096 numbers (the length depends on the model). Then three things people do with such lists: train a small classifier on them, compare lists from two models, add one list to another to push the model. All three treat the list as something definite. What is it?
- P2 (everyday picture, labelled a metaphor): a bank balance on the 20th is the opening balance plus every deposit and withdrawal since. From the balance alone you cannot tell which transaction was which, but you can add them up, and a later withdrawal can undo an earlier deposit.
- P3: the model's list behaves like a balance with thousands of accounts at once; parts of the model add to it and none overwrites. This is our picture; the post tests how far it holds.
- P4 one-line preview (ours, drafted): "Short version: the list is a running sum of what every earlier part of the model wrote; reading it along a direction is a dot product; steering it is adding a vector; and whether a concept *is* a direction is a bet, not a fact." Then two sentences: the post checks the first claim on real models with notebooks, and none of the three sources it rests on speaks about the model families people use today.
- The person is not the subject (WRITING §0): no "Kunhao reads…", no model families named as his work.

**Ladders.** None (no new concept; the balance is the instance for §3's sum).
**Brief units.** Unit 5 (sum, "communication channel") only as a preview; unit 10 (scope).
**Check at S4.** Five-number rule: one number (4,096), the rest in words.

### §2 guess · 250 words · audio chapter `guess`

**Purpose.** Commit the reader before the answers. Options are equal in length; the right answer is never the longest (WRITING §5). Each question carries `data-answer-in`.

**g1** (`data-answer-in="sum"`). You stop a model after block 20 and copy the list for one word. What is the list?
- A. The model's answer so far, stored as a list of numbers.
- B. A running sum: the word's own vector plus each block's additions. **(right)**
- C. The output of block 20 alone, with nothing from before it.
- D. A summary of the whole sentence, one list for all the words.
The reveal (in §3) says B holds for the models in the notebook, with the per-position and norm caveats and slot R2–R5.

**g2** (`data-answer-in="rw"`). Block 3 writes (−2, −2) into a stream that already holds (2, 2). What can a later block read?
- A. Both vectors, as two separate items, in order of arrival.
- B. Only (−2, −2), because the newest write replaces the old one.
- C. Only the sum, (0, 0): neither vector can be read back. **(right)**
- D. Only (2, 2), because the first write is kept for good.
Distractor B is the "overwrite" misconception; D is the "first one wins" misconception.

**g3** (`data-answer-in="dir"`). A probe gives each point a score: multiply its two coordinates by two fixed numbers and add. Now add the same vector v to every point of a cloud. By how much does each score change?
- A. By the same amount for every point. **(right)**
- B. More for points far from the origin.
- C. Only for points near the probe line.
- D. It depends on each point's length.
(The term "dot product" is not used before §5; the question describes it in words.)

**Units.** 7 (cancellation, hedged), 11, 14 (for the reveals only).

---

### §3 sum · 1,250 words · audio chapter `sum`

**Purpose.** Earn clause 3 of the lens ("the stream at layer L is the embedding plus every attention and MLP output before L") and the bridge claim "hidden state = stream" (clause 7), with every step small enough for a strong 17-year-old.

**Sub-parts and budget.**

| Part | Words | Content |
|---|---|---|
| 3.1 From words to lists | 150 | A token is a word or word piece. The model first looks up one list of numbers per token (Nanda, "Embedding": a lookup table giving the stream's starting vector). A list of n numbers is a vector with n dimensions; draw it as an arrow. Real sizes: GPT-2 small has 768 entries per list and 12 blocks (Nanda, Transformer Basics); other models' sizes come from slot R1, never from memory. GPT-2 adds a learned position vector too; rotary-position models do not add one (Nanda, Positional embedding). Our toy uses 2 numbers. |
| 3.2 Add two vectors by hand | 150 | Ladder L1 below. A prompt "do this on paper before you scroll", then the answer. |
| 3.3 What a block does: it writes by adding | 250 | A block is two sub-layers in order, attention then MLP (Nanda: "confusingly, a transformer layer actually contains two layers"; we say *block* and *sub-layer*). Plain-words roles, labelled ours: attention is the sub-layer that can bring in information from earlier words; the MLP works on one word's list at a time (Nanda: attention layers "are the only layers that can move information between token positions"). Each sub-layer looks at the stream, computes a vector, and adds it. It never overwrites (Elhage: layers "write" by "adding a linear projection back in"). W9-A walked through in words; the reader taps `stepper` and `diagram` (see Widgets). |
| 3.4 The pattern and the formula | 200 | Ladder L2 below. |
| 3.5 One stream per position | 150 | Ladder L3 below. |
| 3.6 Is the hidden state the stream? | 200 | Ladder L4 below. Includes the term box. |
| 3.7 Trap box: what the bus picture gets wrong | 100 | See below. |

**Ladder L1 · adding vectors.**
1. Instance: attention 1 wants to add the vector (2, −1) to a stream holding (1, 2).
2. Question: what does the stream hold afterwards?
3. Mechanism in words: add the first numbers together, add the second numbers together.
4. Numbers: 1 + 2 = 3 and 2 + (−1) = 1, so (3, 1). Swapping the order gives the same (2+1, −1+2) = (3, 1).
5. Formula: (a, b) + (c, d) = (a + c, b + d); read aloud "first plus first, second plus second". Same rule for 4,096 entries.
6. Check: the stepper's first move shows (3, 1), which the reader already has.
7. Limits: only lists of the same length can be added; the toy has 2 entries so you can draw it.

**Ladder L2 · the running sum (the central concept).**
1. Instance (W9-A, toy, ours): embedding x₀ = (1, 2); block 1 writes attention a₁ = (2, −1) and MLP f₁ = (−1, 1); block 2 writes a₂ = (3, −2) and f₂ = (−1, 2).
2. Question: what does the stream hold after block 2?
3. In words: start from x₀, add the writes one at a time, in the order they happen.
4. Numbers (the stepper): (1,2) → (3,1) → (2,2) → (5,0) → (4,2). At most five numbers per paragraph: the table carries them.
5. Formula: x_k = x₀ + (a₁ + f₁) + … + (a_k + f_k). "The stream after k blocks is the embedding plus every write up to block k." Matches Elhage ("simply the sum of the output of all the previous layers and the original embedding") and Nanda ("after layer n … sum of the embedding and the outputs of all layers up to layer n"); we say "after k blocks" (trap 4).
6. Check: x₀ + a₁ + f₁ + a₂ + f₂ = (1+2−1+3−1, 2−1+1−2+2) = (4, 2), the same as the running total. The `diagram` ends on (4, 2).
7. What it means and does not: the sum is bookkeeping. It says what is in the stream, not what any writer meant. Edge case shown in step 5: f₂'s y-part (+2) undoes the −2 that a₂ put there; writes can cancel because they add. A block's stream has 2k+1 states along k blocks (the MLP looks at the stream after the attention write): "after k blocks" names one of them. Elhage's models drop biases and the norm (Model Simplifications); say so once.

**Ladder L3 · one stream per position.**
1. Instance: the two-word input "red car": the model keeps one list for "red" and one for "car" at every depth.
2. Question: can the list at "car" see "red"?
3. In words: the MLP write at a position depends only on that position's list. Only attention can copy something from another position's list, and in a decoder-only model only from earlier positions (Nanda, Transformer Basics; Decoder-only). So there is no such thing as "the hidden state of a sentence"; a pooled summary is a further operation.
4. Numbers: none beyond "2 positions × 2 numbers"; the `diagram` positions shows 2 columns and one dashed arrow (attention) from position 1 to position 2.
5. Formula: none; the sum of L2 holds at each position separately.
6. Check: notebook prints the tokens and the position index it takes (slot R6).
7. Limits: Elhage believes the stream "often dedicates subspaces to tokens other than the present token" (hedged: "we believe … often"), so the vector at position t need not be "about token t" only. Nanda's sentence on padding is not needed.

**Ladder L4 · hidden state = stream (the bridge; in none of the three sources, trap 2).**
1. Instance: the hook's list at block 20.
2. Question: is the list a library hands you the same vector as x₂₀ above?
3. In words (the test, ours): run a model; copy the list at the boundary after block k; separately record the starting vector and every write inside the blocks; add them; compare. Difference at the level of rounding means "same vector". Do it in float32 on CPU (T7).
4. Numbers: slots R1–R6 from `results.md`: which models; list length; index convention; max absolute and relative error of the additivity per model; whether the last entry has the final norm applied; the position index. **Nothing is written here.** If the last entry differs, the text says so and explains it from the code lines the notebook saved (T1).
5. Formula: "returned list at k" = x_k, stated as "equal up to rounding at one position".
6. Check: the notebook's own printout, quoted exactly from `results.md`, plus W9 reproduced in numpy.
7. Limits: pre-norm models only, as checked; the families in the reader's work (Llama 3, Gemma 3, Mistral) are not claimed unless `results.md` covers them; the post says "re-run notebook 02 with your model path". Where the norm sits matters: in the pre-norm design Nanda describes, the norm acts when a block *reads* (before attention, MLP and unembedding), so the stream stays a plain sum; in post-norm models, "LayerNorm … when writing to the residual stream (ie at layer output)", which changes what a write is. Quote Nanda's words only (unit 9 trap). If `results.md` reports an extra norm around a sub-layer output in any model, say that the "write" is then the normalised output.

**Term box (one only).** *Term · Residual stream (also: hidden state, embedding).* Definition in two sentences; the three names: Elhage says the stream vectors "are often called the 'embedding'" and the probing literature calls them embeddings; libraries say *hidden state* (none of the three sources uses the phrase; Nanda's `hidden_size` is an alias of the stream's width); Nanda's *hidden layer* means something else (an MLP's internal activations). Why it matters: we test equality instead of assuming it.

**Trap box · the bus picture (T13).** A hardware bus has one writer at a time and addresses. The stream has every writer adding at once, no addresses, and a reader sees a mix (Nanda: reading takes dot products with the whole stream). Nothing is lost to noise; the sum is exact. Elhage's phrase is "communication channel … since it doesn't do any processing itself and all layers communicate through it": quote the exact words, not "does no processing".

**Widgets.**
- `stepper` **sum-table** (id `sum-table`). Head: ["after", "adds", "stream"]. Rows from the numpy run: start (embedding) → (1, 2); + attention 1 (2, −1) → (3, 1); + MLP 1 (−1, 1) → (2, 2); + attention 2 (3, −2) → (5, 0); + MLP 2 (−1, 2) → (4, 2). The reader first adds by hand (instruction in the paragraph), then taps Next to check. Notes: one per row; the last note names the cancellation.
- `diagram` **bus** (id `bus`, `"preview": true`, vertical layout for 375 px). Nodes (7, labels of two words or fewer): `Embed`, `Attn 1`, `MLP 1`, `Attn 2`, `MLP 2`, `Unembed`, and a tall `Stream` band (kind `hl`). Solid arrows = write (into the band); dashed arrows = look (out of the band). Six steps; step text gives the running sum (same numbers as the stepper). The reader presses Next to watch each writer join. Edge case in step 5: the +2 undoes the −2. The `Unembed` node only looks (reads), previewing §5 and F3.
- `diagram` **positions** (id `positions`, no steps, small). Nodes: `Word 1`, `Word 2`, `Stream 1`, `Stream 2`. Solid arrows Word→Stream; one dashed arrow `Stream 1 → Stream 2` labelled `attention`; no arrow back. The reader sees that only attention crosses columns.
- Numbers: the stepper rows and the diagram step texts are the same six vectors from the numpy run; record in `numbers.md`. Norms (2.236, 2.828, 4.472) are not used in the text.

**Edge cases that teach.** Cancellation (step 5). The 2k+1 states.

**Guess answer.** g1 reveal here: B with caveats; the reveal cites the notebook numbers by slot.

**Units.** 5 (sum, channel, limits; L155, L148, L142, L98/L102 for scope), 10 (L579, L586–590, L598–601, L611–612, L625, L667, L671, L679, L831), 9 (L685, L872 for norm placement only), 14 (none).
**Verbs.** Elhage *asserts* the sum (L155), *believes* the subspace point; Nanda *asserts*, and his skip-connection remark is an *opinion* (do not use it as a disagreement with Elhage: writer-must-not-use #5).

---

### §4 bets · 650 words · audio chapter `bets`

**Purpose.** State Olah et al.'s three claims as bets, with their firmness and scope, and say what we do with them: nothing is tested here; the next two sections build the algebra that lets us say what each bet would mean for the stream. Short account of the authors (WRITING §0: the person is a hint; the full list of lines goes to F1).

**Content (about 110 words per bet, plus 100 intro, 120 scope box, 100 closing).**
- **Intro (100).** The lens a reader would like to hold has three ideas: concepts live as directions, behaviours are circuits, the same things recur across models. Olah et al. (a vision-network article) *offer* them as claims and call them "deliberately speculative". We treat each as a bet.
- **Bet 1 · features are directions.** The claim, quoted: "Features are the fundamental unit of neural networks. They correspond to directions." Their gloss: "a linear combination of neurons in a layer". Plain-words instance (before any dot product): in a layer with two neurons, "second minus first, scaled" is a direction. Our translation, labelled ours: the stream has no neurons (Nanda: "no such thing as a residual stream neuron"), so for the stream a direction means a weighted mix of its coordinates, an arrow. *Feature* is used as the sources do: a scalar the model could compute from the input (Olah glossary) or a property of an input (Nanda); a *concept* is our human label ("calm"). Firmness: Olah *offer* it, *believe* the typical case is understandable (with the lead-in "have led us to believe"), *concede* "The community is divided on whether this is true"; the strongest evidence line is "Curve detecting neurons can be found in every non-trivial vision model we've carefully examined" (single neurons, not general features). Nanda calls "features as directions" a hypothesis, backs it with an intuition ("the main thing a model is capable of doing is linear algebra"), and writes that the neuron version is "mostly true of Inceptionv1, but … at best only slightly true for transformers" (quote the whole sentence, writer-must-not-use #4). For language models: no evidence in these sources (clause 4 GAP). What it would mean for the stream: a concept's strength is a dot product (§6). Cash-in at the end of §6.
- **Bet 2 · features are connected by weights, forming circuits.** Quote "Features are connected by weights, forming circuits." Define circuit in-sentence (a computational subgraph: features and the weighted connections between them; not an electrical circuit). Unhedged: "You can literally read meaningful algorithms off of the weights" and "for small enough circuits, statements about their behavior become questions of mathematical reasoning". Hedged: that behaviour could be broken down into circuits is "it seems like, with sufficient effort"; "perhaps circuits could act as a kind of epistemic foundation". Evidence: curve and dog-head circuits in a vision network; their test (predict what an edit to the weights will change) is a plan, not a reported result. Elhage reports circuits only for attention-only models of at most two layers. "Behaviours such as refusal or trust are circuits" is in none of the three sources (clause 5 GAP); Olah's L636 is the nearest and is a hope. What it would mean for the stream: an edge is a number for each (writer, reader) pair. Cash-in in §5 (W9-B), said as "like an edge weight", not an Olah edge (S2).
- **Bet 3 · analogous features and circuits form across models and tasks.** Quote the claim. *Suspect* "likely true"; evidence "only … anecdotal"; the one claim that "wouldn't be completely fatal to circuits research" if false. Do not rank the three as equally supported. Nothing here or elsewhere in the sources about one model before and after fine-tuning (keep out; §11 states the untested assumption). What it would mean for the stream: "analogous" can only mean "the same up to a rotation of the stream", never "the same coordinates". Cash-in in §6 (rotate widget).
- **Scope trap box (120).** Three vintages: Olah 2020, a vision network (InceptionV1); Elhage 2021, attention-only transformers of at most two layers, no biases, norm ignored, larger models not attempted; Nanda 2022, a personal, opinionated glossary "mostly a description of how GPT-2 works". None says anything about Qwen3, Llama 3, Gemma 3 or Mistral, base versus instruct, or post-training. Say it here, where each is first cited (T14).
- **Closing (100).** What we do with the bets: Sections 5 and 6 are algebra, exact in a toy; they say what each bet would claim, not whether it is true.

**Ladders.** The bets are claims, not derivations. Each concept (feature, direction, circuit, universality) gets an instance and a plain-words reading here; its numbers arrive in §5–§6 (the callbacks). No step of §4 needs a later section.
**Widgets.** None (a table of three bets would be wide; the text and F1 carry it). **F1** is a fold-out: for each claim, the strongest unhedged line and the hedged lines, sorted by firmness with the matching verbs, plus Nanda's flat statements (L135, L1096) "stated without a hedge".
**Units.** 1 (without L265, L252, L147–148), 2, 3 (without Elhage L568), 12, 8 (for L736 only), 10 (scope), 5 (scope).

---

### §5 rw · 900 words · audio chapter `rw`

**Purpose.** Reads and writes as dot products and additions, in 2-D, with numbers; who hears whom; cancellation; what "linear" does and does not cover.

**Sub-parts.**

| Part | Words | Content |
|---|---|---|
| 5.1 A read is a weighted look | 150 | Ladder L5 |
| 5.2 Who hears whom | 250 | Ladder L6 + `lab` read-split + orthogonality |
| 5.3 A write adds | 100 | Ladder L7 first half |
| 5.4 Cancellation | 120 | Ladder L7 second half; g2 reveal |
| 5.5 Cash-in for bet 2 | 60 | "like an edge weight" |
| 5.6 What "linear" covers here | 100 | senses (i) and (ii); block internals not linear |
| captions and the widget instruction | 120 | |

**Ladder L5 · a read is a dot product.**
1. Instance (toy, ours): a reader inside the model (one neuron of block 2's MLP) has an input vector r = (1, 2). It looks at the stream after attention 2, which holds (5, 0).
2. Question: what single number does it get?
3. In words: multiply matching entries and add. r says how much to care about each coordinate: r = (1, 0) would read only the first coordinate; r = (0, 1) only the second; (1, 2) takes one part of the first and two parts of the second. Nanda's sentence: "Reading is a projection, the residual stream is dotted with each input vector of the relevant matrix"; Elhage says layers "read" by "performing a linear projection".
4. Numbers: r · (5, 0) = 1·5 + 2·0 = 5. For r = (0, 1): 0·5 + 1·0 = 0.
5. Formula: r · x = r₁x₁ + r₂x₂ (read aloud "first times first plus second times second"). Same rule for 4,096 entries. Name: *dot product*.
6. Check: r = (1, 0) gives 5, the first coordinate, as it should.
7. Limits: the post uses *read* only for what a component does inside the model; copying a list out is "read out" or "extract" (threshold word). Pin the senses of *projection*: Nanda's default is the number x·v (sometimes with unit v); the vector (u·x)u is the closest point on the line. We call u·x the **score** and say which one is meant each time (the widget draws both).

**Ladder L6 · a read splits over the writers.**
1. Instance (W9-B, ours): the same reader r = (1, 2) looks at (5, 0). Which writer does it hear?
2. Question: how much of the 5 came from each writer?
3. In words: the stream is a sum of writers, and a dot product of a sum is the sum of the dot products. So take r · each writer.
4. Numbers: r·x₀ = 5; r·a₁ = 2 − 2 = 0; r·f₁ = −1 + 2 = 1; r·a₂ = 3 − 4 = −1; total 5 + 0 + 1 − 1 = 5, the same as r·(5, 0).
5. Formula: r · x = r · x₀ + r · (writes). One line, symbols read aloud.
6. Check: the total 5 equals the direct read 5.
7. Meaning and limits. *Orthogonal* means dot product zero: a₁ is in the stream, yet r hears none of it (Nanda: "every vector in the residual stream contributes (unless it's orthogonal)"). *Not opposites* (Nanda): reading along r does not recover what a writer put along r unless the other writers are orthogonal to r; here a₂ is heard negatively. Elhage's *virtual weights* ("multiplying out their interactions through the residual stream") are this same split at the level of weight matrices; W9-B is only the additive split of a read (S2 note 7; label "ours"). The split holds because nothing nonlinear sits between the writes and the read; a norm in front of the read (F2) changes the numbers by a scale and a shift, which Elhage handles "up to a constant scalar" for the idealised model.
Edge case: reader (0, 1) hears 2, −1, 1, −2 (loud parts) and a total of 0: the parts cancel, which is §5.4.

**Ladder L7 · a write adds; writes cancel.**
1. Instance: MLP 2 writes f₂ = (−1, 2) into a stream holding (5, 0).
2. Question: what is there afterwards, and what became of attention 2's write (3, −2)?
3. In words: nothing is replaced. (5, 0) + (−1, 2) = (4, 2). The y-part of a₂ (−2) and the y-part of f₂ (+2) sum to zero, so the y-part of a₂ is no longer visible in the stream, though a₂'s x-part (3) remains. A writer with one output vector can only move the stream along that line (Nanda: "a specific low rank subspace, spanned by the output vectors").
4. Numbers: g2's toy: (2, 2) + (−2, −2) = (0, 0); every reader gets 0 from it, whatever its input vector. Exercise E1 variation: f₂ = −a₂ = (−3, 2) wipes block 2's contribution.
5. Formula: x + w + (−w) = x.
6. Check: g2 answer C; (0, 0) read by r = (1, 2) is 0.
7. Limits (hedged exactly): Elhage asserts "Once added, information persists in a subspace unless another layer actively deletes it"; that real heads or neurons delete is only a hint ("we've seen hints that some MLP neurons and attention heads may perform a kind of 'memory management' role"). Our toy shows that cancellation is possible by arithmetic, not that models do it.

**5.5 Cash-in for bet 2.** The W9-B table is a number for every (writer, reader) pair, which is the shape of a weighted edge: "like an edge weight" (Olah's edges join nodes in adjacent layers, so not "an Olah edge"). Whether behaviours are circuits stays a bet.

**5.6 What "linear" covers here.** Sense (i): the stream is a *sum* of writes. Sense (ii): a *read* is linear in the stream (it splits over the writers). Sense (iii), "a concept is linearly readable", is a bet (§6, §8). The layers' own computation is not linear: Nanda says the "divide by the standard deviation" step of the norm "is non-linear", and Elhage says "the presence of the GeLU activation means we can't linearize through MLP layers" (that line is in the MLP section, outside Kunhao's Elhage scope: use only if the meta-manager clears it; otherwise cite Nanda L702 alone).

**Widget · `lab` read-split** (id `read-split`).
- Params (2 sliders): `r1`, `r2`, −3 to 3, step 1, defaults 1 and 2.
- Constants: x₀, a₁, f₁, a₂ as numbers. Derived: the four dot products and their sum, and `direct = r·(5,0)`.
- `table`: head ["writer", "vector", "r · writer"], four rows plus total; `bars`: the four shares, highlight the largest. `readout`: "total = {total} ; direct read of (5, 0) = {direct}".
- Reader does: slide r and watch which writers are heard; find a reader that cannot hear a₁.
- Presets: "r = (1, 2)" (the text's example); "x only (1, 0)"; "y only (0, 1)" (parts 2, −1, 1, −2, total 0: loud parts, silent total); "along a₂ (3, −2)".
- Every number in the text comes from `check.mjs`.

**Guess answer.** g2 reveal here (C), after 5.4.
**Units.** 11 (L997–1002, L1000), 6 (L148, L157–158, L162, L121 not needed), 7 (L168, L172; L166), 2 (for the cash-in), 9 (L702 only), 8 (L243 for dot-product invariance, used in §6).
**Five-number rule.** 5.2 puts the four shares in the lab's table and names them in prose at most twice.

---

### §6 dir · 900 words · audio chapter `dir`

**Purpose.** Probe = read along a chosen direction; steering = one more write by hand; no privileged basis = why we compare by dot products. Cash in bets 1 and 3.

**Sub-parts.**

| Part | Words | Content |
|---|---|---|
| 6.1 A cloud of streams | 150 | Setup W9-C; why coordinates fail |
| 6.2 Score along a direction | 300 | Ladder L8 (length, unit vector, angle, score, margin, probe) + cash-in bet 1 |
| 6.3 Steering | 220 | Ladder L9; g3 reveal |
| 6.4 Rotate everything | 200 | Ladder L10 + rotate widget + cash-in bet 3 |
| widget instruction/captions | 30 | |

**Ladder L8 · a direction and its score (the probe).**
1. Instance (W9-C, toy, ours): six streams at one depth, from prompts we label "calm" ((3,1), (4,2), (5,3)) and "urgent" ((1,3), (2,4), (3,5)). The calm point (4, 2) is x₂ from §3.
2. Question: can one number per point tell the groups apart?
3. In words: first try the coordinates. Along x the groups run 3, 4, 5 and 1, 2, 3; along y they run 1, 2, 3 and 3, 4, 5. Each pair overlaps at 3, so no single coordinate separates them. Now turn a reading arrow. A **direction** (our unit convention; Olah/Nanda give none) is an arrow of length 1; its score for a point is the dot product. Length of a vector (a,b) is √(a²+b²); dividing (−1, 1) by its length √2 = 1.414 gives u = (−0.707, 0.707) "second minus first, scaled".
4. Numbers: u = (−1, 1)/√2: every calm point scores −1.414, every urgent point +1.414; margin (lowest urgent score minus highest calm score) 2.828. Along (1, 1)/√2 (45°): the groups get the same three scores, 2.828, 4.243, 5.657 (blind probe). Margins by angle from `check.mjs` (0 at 0°/90°/180°, 0.695 at 100° and 170°, 2.000 at 120° and 150°, 2.828 at 135°).
5. Formula: s = u · x = x₁ cos φ + x₂ sin φ, where φ is the angle of u from the x-axis ("the cosine of the angle times the first, plus the sine times the second").
6. Check: x = (4, 2), φ = 135°: 4·(−0.707) + 2·0.707 = −1.414, as the table says.
7. Meaning and limits. A **probe** is a read whose direction was fitted on labelled examples; Nanda defines it as "a 1D linear map … corresponding to a direction in activation space, which likely corresponds to that feature" ("likely": keep). Our toy's direction is found by turning an arrow; the labels are ours; no accuracy is claimed. A high score shows that the information is present along that direction; it does not show that the model uses it (the observe-versus-intervene point, developed in §8). Translation of Olah's wording, ours: his "linear combination of neurons in a layer" is here a weighted mix of coordinates: −1/√2 of the first plus 1/√2 of the second.
**Cash-in for bet 1.** "If concepts were directions, this is what it would look like: one turn of an arrow separates the groups. Nothing in this toy shows that a language model stores 'calm' this way."

**Ladder L9 · steering is a translation.**
1. Instance: add v = 2u to every point, where u = (−1, 1)/√2 (so v = (−1.414, 1.414)).
2. Question: what happens to the six scores?
3. In words: the dot product of a sum is the sum of dot products, so every score moves by u · v, whatever the point.
4. Numbers: u·v = 2.000; calm scores −1.414 → 0.586; urgent 1.414 → 3.414. With v = 2(1, 1)/√2, pushed sideways, u·v = 0 and nothing moves although every point moved.
5. Formula: s(x + v) = s(x) + u · v. This is a **translation**: it is *affine* (a linear step plus a constant), not *linear*, because a linear map sends the zero vector to zero and adding v sends it to v.
6. Check: both numbers above; E4 repeats it.
7. Limits. This is arithmetic. "Steering", "activation addition" and "steering vector" are in none of the three sources (unit 14, trap 1): that adding a vector changes behaviour as intended is not claimed here, and we do not borrow Nanda's cautions about ablation as if they were findings about addition (they concern removing a part; "applying them to steering is our analogy"). Nanda defines intervening on an activation as to "stop it once it's computed an activation, edit or replace that activation, and then resume running the model". Say once that a write by hand is one such edit.
**Guess answer.** g3 reveal here (A).

**Ladder L10 · no privileged basis.**
1. Instance: rotate the whole toy by 90°: (x, y) → (−y, x), including r. x₂ = (4, 2) becomes (−2, 4); r = (1, 2) becomes (−2, 1).
2. Question: what changed for the reader?
3. In words: the coordinates of every vector changed; every angle and length stayed; so every dot product stayed.
4. Numbers: the four shares are 5, 0, 1, −1 before, and after (e.g. the total: (−2,1)·(0,5) = 5, and the first share: (−2,1)·(−2,1) = 5). Coordinate 2 of x₂ was 2, now 4.
5. Formula: (Rr) · (Rx) = r · x for a rotation R (ours, textbook arithmetic; the sources' reason is Nanda's "Operations like addition, matrix multiplication, dot products, etc are unchanged under any change of basis").
6. Check: the `lab` rotate slider at 90° shows the same four shares.
7. Meaning and limits. Elhage *asserts*, for the idealised linear stream, that the stream "doesn't have a 'privileged basis'; we could rotate it by rotating all the matrices interacting with it, without changing model behavior". Nanda adds the caveat "the standard basis is always slightly privileged" (floating point and Adam). The MLP's neuron coordinates *are* privileged (the nonlinearity acts coordinate by coordinate); the rotation here is for the stream's reads. Elhage: "it doesn't really make sense to look at the 'neurons' … of activations like the residual stream", and "This isn't to say that there aren't ways to study them". Consequence for work: never read "dimension 17" as a feature; compare vectors by dot products. Whether the invariance survives a real model's norm is not in the sources (a notebook question; do not claim).
**Cash-in for bet 3.** Let "model B" be model A rotated: the coordinates differ, every dot product is the same. So "analogous" can only mean "the same up to a rotation of the stream" (ours; the toy gives a reason to compare dot products, not a result about real models).

**Widgets.**
- `vec2d` **probe-push** (id `probe-push`), copied from `cfg-vec2d` in the gallery without changing the geometry: x range −3..7, y range −2..7; params `phi` (0..180, step 1), `psi` (0..180), `alpha` (0..3, step 0.1); `probe` with `feet: true`; `shift` with `trail: true`; six points (group 0 blue = calm, group 1 red = urgent); vectors `u` (drag angle `phi`) and `v` (drag angle `psi`, length `alpha`); `derived.margin`; the `readout`; presets "axis only", "best probe", "blind probe", "push along", "push sideways". Title ends "(toy, ours)". The caption keeps the gallery's edge case (at 45° the groups get the same three scores). Reader does: drag the blue arrow until the groups separate, then drag the red arrow and watch every score move by the same amount. Three sliders (≤ 4). The `scale: 3` on u is a drawing choice and is said in the caption.
- `lab` **rotate** (id `rotate`). One param `rot` ("rotate the whole toy"), 0 to 360, step 5, default 0, symbol ω (θ is taken in notation.md). Derived: rotated x₂ coordinates; rotated r; the four shares. `readout`: "x₂ = ({x2x:.2f}, {x2y:.2f}) ; shares = {s0:.2f}, {s1:.2f}, {s2:.2f}, {s3:.2f} ; total = {tot:.2f}". Presets: 0°, 45°, 90°, 180°. Edge case: shares stay put for every ω while coordinate 2 moves.
- Fallback for `vec2d`: the card's `plot` version (`phi`, `psi`, `alpha` sliders, six points, probe line curve, height ≈ 340, equal axes). Decide after `test.mjs`.
**Units.** 1 (L194, L679 for single-neuron directions; glossary), 12 (L199–203, L1586–1587, L259 whole sentence), 8 (L158, L242–245, L250/L249, L736, L852), 11 (L1412, L1415, L1000), 14 (L147; unit trap 1), 3 (cash-in for bet 3 uses the claim only).
**Five-number rule.** 6.2: coordinates sit in the widget's readout; the margin table lives in the widget readout, not in prose.

---

### §7 answer · 350 words · audio chapter `answer`

**Purpose.** Boxed **Short answer** (WRITING §0): one paragraph for each part of the question, a verdict labelled ours, and what would change it. Threshold words pinned: *is* (numerically equal up to float rounding, one position, one block boundary), *hidden state* (the list the library hands back), *linear* (the three senses), *operation* (arithmetic, not behaviour).

**Skeleton (ours, with slots; the S4 writer fills R-slots from `results.md` and from nothing else).**
- **Identity (about 120 words).** Verdict: in the pre-norm models we checked [R1: names], the list a library returns at the boundary after k blocks, for one position, equals the embedding plus every write before it, up to rounding [R3: max abs and relative error]. Exceptions found [R2/R4: last entry, other]. This rests on the notebooks and the installed code; none of the three sources uses the words "hidden state" (trap 2). What would change our mind: an additivity error above rounding for correctly placed hooks, or an extra norm between a sub-layer and the add in a model you use.
- **Operations (about 110 words).** Verdict: a probe is a dot product; steering is a translation; a comparison of lists should use dot products (no privileged basis). All three are exact arithmetic. What a score means, or whether a push changes behaviour, the algebra does not say and the sources do not say (steering is absent from them). What would change it: nothing in this post; it is the subject of reading that tests interventions.
- **Bets (about 100 words).** Verdict: all three of Olah's claims are "deliberately speculative"; the evidence is a vision network; the language-model evidence is not in these three sources. We hold concept-as-direction, behaviour-as-circuit and cross-model analogy as bets, in that order of how much the toy lets us say. What would change it: tests of the bets on language models, in later reading.

**Units.** all; verbs as in each unit.

---

### §8 lens-linalg · 550 words · audio chapter `lens-linalg`

**Link type.** *same-math*: stream = sum of vectors; read = dot product; write = vector addition; steering = translation; no privileged basis = invariance of dot products under rotation. Caveat in the same sentence: only the bookkeeping is the same maths; the sub-layers are not linear.
**What only this lens shows.** Exactness: the hidden state becomes something you can add up and check; a read splits over writers (W9-B); "which coordinate?" is the wrong question (rotate); a push moves every score by the same amount.
**What it does not explain.** Why concepts would be directions at all (bet 1); anything nonlinear (MLP activations, attention weights, the norm's division). The three senses of linear in one short list: (i) the stream is a sum; (ii) a read is linear in the stream; (iii) "a concept is linearly readable" is a bet; steering is affine; cosine similarity divides by two lengths, so it is not additive (the arithmetic check in the notebook, slot R7).
**The see-versus-do paragraph (one paragraph, ours).** A probe observes a read of the stream; steering writes into it. A high probe score shows information is present, not that downstream readers use that direction. This is the difference between seeing and doing; the full treatment needs tests this post does not run. No source here addresses it directly; Nanda's cautions about ablation (zero ablation "is arguably unprincipled, because the model may be using that part as a bias term") concern removing parts and are cited only as a reminder that edits can mislead.
**Connection to Kunhao's research (3C).** Computation: probing, similarity analysis and steering are three statements about one vector; this lens fixes what the vector is and which operations are exact. (No Discipline data, prompts or results.)
**Stands alone.** No reference to another post; terms re-introduced.
**Widgets.** None new; the section points back to the `vec2d` and `read-split` figures by description only ("the arrow you turned").
**Units.** 6, 8, 11, 12, 14; 9 (L702).

---

### §9 lens-info · 380 words · audio chapter `lens-info`

**Link types.** *structural analogy* (ours) for "many writers add into one shared vector and one reader sees only the sum"; *metaphor* for "bus" and "bandwidth". Elhage's "bandwidth" counts dimensions and is in scare quotes ("dimensions of the residual stream become something like 'memory' or 'bandwidth'"); no rate or capacity is computed here. **Request Q1 (see `requests.md`)**: a verified unit for the multiple-access channel (several senders, one receiver, output = sum of inputs). Until it arrives, the S4 writer states the analogy as ours and uses no textbook result.
**What only this lens shows.** The question about limits: d dimensions, many things to say; how many separate messages can one reader recover if some interference is tolerated? Sourced set-up only: Elhage (a single MLP layer "typically has four times more neurons than the residual stream has dimensions", "somehow communicating in superposition!"); Nanda (about 50,000 tokens and 768 dimensions: "there almost has to be more features than dimensions, and thus superposition", a counting argument, hedged by "almost"); Nanda's definition: more than n features in n dimensions; Olah's footnote ("n orthogonal vectors, but exponentially many almost orthogonal vectors"), posed, not used as a result; Olah's condition ("As long as cars and dogs don't co-occur") and Nanda's summary of Anthropic's toy-model paper (sparsity; attribute it so).
**Ladder L11 · interference (the toy, ours).**
1. Instance: three features written along three directions at 0°, 120° and 240° in a 2-D stream, g₁ = (1, 0), g₂ = (−0.5, 0.866), g₃ = (−0.5, −0.866). Only feature 1, strength 1, is written.
2. Question: what do the three readers (the same three vectors) hear?
3. In words: each reader takes a dot product with the stream (§5). Readers 2 and 3 are not orthogonal to g₁, so they hear something nobody wrote for them.
4. Numbers: stream (1, 0); reads 1.000, −0.500, −0.500. Two features, strengths (1, 1, 0): reads 0.5, 0.5, −1.0. All three at strength 1: the stream is (0, 0) and the reads are 0, 0, 0, the same as writing nothing.
5. Formula: read j = c_j − ½ (the other two strengths added), for these three directions (derived in the exercise-sized aside: g_j · g_j = 1, g_j · g_k = −½).
6. Check: (1, 0, 0) → 1 − ½(0+0) = 1 and −½ and −½.
7. Meaning and limits. In 2-D two orthogonal directions are free of interference, three are not. This is the question for a later reading, not an answer: the sources here give no capacity number. The stream in the toy is exact, with no noise, so no channel capacity is defined; no code is used. For stream sums the post says "adds", not "superposes", to keep apart the model-side sense of *superposition* (Nanda L269 definition) from the linear-algebra and coding senses.
**Connection to research (3C).** Computation: if features are packed in superposition, a single probe direction may pick up several features at once; any claim that a probe isolates a concept must say what else is on the same line.
**Widget · `lab` three-features** (id `three-features`). Params `c1`, `c2`, `c3` (0 to 1, step 0.5). Derived: stream coordinates and the three reads. `bars`: the three reads (max 1.5). `readout`: stream and reads. Presets: "feature 1 only", "features 1 and 2", "all three" (the zero stream), "nothing". Title ends "(toy, ours)". Reader does: switch features on and see what the others hear; find a setting that looks exactly like silence.
**Units.** 7 (L166–172, L168 note not needed), 4 (L382, L398, L510), 5 (L155), 10 (L583); Nanda L269–287 as listed.
**Edge case that teaches.** All three on equals none on.

---

### §10 turn · 420 words · audio chapter `turn`

**Purpose.** Run on the reader's machine; hand-computable exercises; the open question.

**Content.**
- **Notebooks (about 90 words).** `01_bus_gpt2.ipynb` (GPT-2 small; TransformerLens): per-block additivity error (max absolute, max relative; slot R3), the stream's norm by depth and position (describe only; slot R-norm), the logit lens with and without the final norm and a check that the last block reproduces the model's logits (slot R-lens), W9 reproduced in numpy. `02_bus_my_model.ipynb` (plain Hugging Face + hooks; `MODEL_PATH`): module tree and decoder-layer lines, the index convention of `hidden_states`, the additivity test for the model you choose, and the arithmetic score-shift check. "What to look for" quotes `results.md` numbers verbatim. Both end with blank exercise cells. Neither uses any Discipline data.
- **Exercises (E1–E5, about 40 words each in the box, hint and solution folded).**
  - **E1 Add.** With W9-A compute x₁ and x₂, check x₂ = x₀ + a₁ + f₁ + a₂ + f₂; then find f₂ so that block 2 leaves the stream unchanged. Solution: x₁ = (2, 2); x₂ = (4, 2); f₂ = −a₂ = (−3, 2).
  - **E2 Who hears whom.** r = (1, 2): compute r·x₀, r·a₁, r·f₁, r·a₂, show they add to r·(5, 0) = 5; which writer is inaudible and why? Solution: 5, 0, 1, −1; a₁ is orthogonal to r.
  - **E3 Project.** Score the six points on (1, 0), (0, 1) and (−1, 1)/√2. Which leaves a gap? Which direction gives both groups the same scores? Solution: first two touch at 3; the third gives ∓1.414 (margin 2.828); (1, 1)/√2 gives 2.828, 4.243, 5.657 for both groups.
  - **E4 Steer.** Add v = (−2, 2) to every point; show each score on u = (−1, 1)/√2 rises by u·v = 2.828. Then add v = (2, 2): change 0. Which probe angle would see that second push? Solution: u·v = 4/√2 = 2.828 for the first; 0 for the second; a probe at 45°, (1, 1)/√2, sees it (change 2.828).
  - **E5 Rotate.** Rotate everything by 90°, (x, y) → (−y, x), including r. Show the four shares 5, 0, 1, −1 are unchanged. What does that say about "coordinate 2 of the stream"? Solution: (−2,1)·(0,5) = 5 etc.; coordinate 2 of x₂ goes from 2 to 4, so "coordinate 2" has no meaning of its own.
  All answers re-run by code (`numbers.md`).
- **Transfer challenge (about 60 words).** Take any direction you have used (for instance, the weight vector of a trained probe). Write one sentence each: at which depth and which position it was read; whether a norm stood between that stream and the probe; what a shift of length α along it would add to every score; and which of these four you can settle by arithmetic and which need a behavioural test.
- **Open question (about 80 words; leads toward eigen-decomposition; no post is named).** Suppose, as a toy assumption (ours; real blocks are not linear), that what a block does to the stream is one matrix M = [[2, 1], [1, 2]]. It turns (1, 0) into (2, 1), a new direction. But it sends (1, 1) to (3, 3) and (1, −1) to (1, −1): only stretched, by 3 and by 1. Are there always such directions? And if the stream has no privileged basis, could the directions a map only stretches be the natural axes that the coordinates do not give us? Left open.
**Units.** 9 and 13 are used only in F2 and F3; this section cites none. `results.md` slots as above.

---

### §11 work · 330 words · audio chapter `work`

**Purpose.** Tie to 3C (WRITING §0: the post is about the question, not about a person). Three cards in post 01's `.cards3` markup.
- **Computation · Read: probing.** What a probe score licenses: information is present along a direction (the observe-not-do point); the sources' words "likely corresponds". State layer, position and norm placement with every probe result. Re-run notebook 02 on your own model path; claim the identity only where its additivity check passes.
- **Computation · Compare and write: similarity and steering.** Compare lists by dot products, not coordinates (no privileged basis, ω widget). A steering vector is a translation; the score shift is u·v whatever the data. What it does to behaviour is a separate, empirical question (not in these sources).
- **Communication · Framing and priming (candidate bridge, labelled).** In the algebra, a prime or frame added to a model is one more write along a direction. The post supplies only that algebra; whether a frame behaves like a direction is a bet of the same kind as bet 1.
- **Collaboration.** None here; say so in one line.
- **One sentence, labelled "a working assumption, untested here".** A tempting assumption is that a base model and its instruction-tuned version share the same stream space and directions. The three sources define fine-tuning and RLHF only as training procedures (Nanda: "Taking a pretrained model, and training it on a more specific task"; RLHF "a special form of fine-tuning") and say nothing about what they change inside a model; testing it is later work.
**Units.** 14 (L905, L908 only), 12 (L1586–1587), 8, 11.

---

### §12 recall · 350 words · audio chapter `recall`

Eight cards (`details.card`), 35–45 words each, answers folded. ↻ marks one card that reappears later.
1. In one line, what is the list a library returns at block k, and what did the notebook check? (answer with slot R-numbers.)
2. Block 3 writes (−2, −2) into a stream holding (2, 2). What can a later block read, and which two sentences from the sources are hedged on whether real models do this?
3. Why does a read split over the writers, and when does a writer go unheard? (W9-B.)
4. In the cloud, why does no single coordinate separate calm from urgent, and what does the blind probe show?
5. A push v moves every score by what? Why is it affine, not linear?
6. What does "no privileged basis" license you to do, and what does it not cover (MLP neurons, floating point)?
7. Which of Olah's three claims is the only one flagged as non-fatal if false, and how firm is each?
8. ↻ (spaced review, reused verbatim from an earlier post's recall list, no name given): a dot-product question, candidate "In attention, why divide the scores by √d_k?" or, as a second candidate, "N = 10, ρ = 0.9: what is N_eff?" The S4 writer takes the card text from that post unchanged, so it stays self-contained.
**Units.** none new.

---

## 4. Fold-outs (not counted; the audio only mentions them)

**F1 · Look inside: Olah's three claims, sorted by firmness.** For each claim: the claim box wording; the strongest unhedged lines (Claim 1: "These features can be rigorously studied and understood."; L273 on curve detectors; Claim 2: L409, L634; Claim 3: the box); the hedges (L186, L220, L232, L242 with "have led us to believe", L547, L587, L636–637); the verbs (*offer, believe, concede, find, propose, suppose, suspect*); the scope line (L258). Nanda's flat statements (L135, L1096) with the note that they carry no hedge. Never L147–148, L249–254, L265, L267, L287, L455, L658 (hidden on the page). One notation, no new toy.

**F2 · Look inside: a norm before every read.** Nanda: the norm "is used whenever the residual stream is input into a layer (ie before the attention, MLP and unembedding layers)"; its "divide by the standard deviation" step "is non-linear (but the other 3 are linear)"; post-norm models differ (quote only his words). Elhage (idealised model): "up to a constant scalar, the layer normalization is a constant affine transformation". Toy (ours, population standard deviation, convention unspecified in the sources, scale and translate left at identity): x₂ = (4, 2): mean 3, centred (1, −1), standard deviation 1, result (1, −1). Double the stream to (8, 4): mean 6, centred (2, −2), standard deviation 2, result (1, −1) again, not (2, −2). So the read r·LN(x) cannot see the stream's size: for r = (1, 2) it gives −1 for both, while r·x doubles from 8 to 16. Not Elhage's appendix (outside scope). Worked-numbers table (2 rows), no widget; numbers recorded in `numbers.md`.

**F3 · Look inside: the logit lens is one more read.** Nanda's intact lines only: the lens applies "the final layer norm, and unembed, and log_softmax", "often, the model has become confident in the correct next token before the final layer", "This is evidence for thinking about transformers as having the central object of the residual stream" (his reading), and it is "equivalent to zero ablating layers" after the chosen one; "as Nanda describes it"; the original post is a gap (unit 13), his definition line is corrupted and is not quoted. Toy (ours; invented rows; the norm skipped): three-token unembedding with rows at 0°, 120°, 240° applied to the running stream: x₀ = (1, 2) gives (1.000, 1.232, −2.232); x₁ = (2, 2) gives (2.000, 0.732, −2.732); x₂ = (4, 2) gives (4.000, −0.268, −3.732): the leading token flips from the second to the first after block 1 and stays. Point: the last step of a model is a set of reads, one dot product per token. Notebook slot R-lens for the real check. No claim that the lens is faithful. Elhage's version (no norm, L592) is outside his named scope: say "without the norm" only about our toy.

---

## 5. Audio chapters (match section ids; `audio-script.md` at S4)

| # | Chapter id | Title | Approx. spoken words | Notes |
|---|---|---|---|---|
| 1 | hook | The list in the middle | 280 | Starts "Welcome to AI4Read from CSS Lab." One-line preview spoken. |
| 2 | guess | Three predictions | 230 | Options read aloud; pause cue between question and options. |
| 3 | sum | The stream is a running sum | 1,100 | Numbers spoken as "one, two" pairs; the bus diagram described in one sentence; the identity check stated with the notebook numbers in words; recap. |
| 4 | bets | Three bets | 560 | Verbs kept (offer, suspect). Recap lists the three bets and their firmness. |
| 5 | rw | Reads and writes | 800 | "r dot x equals first times first plus second times second." Cancellation example spoken. Recap. |
| 6 | dir | Probe and push | 800 | Angles spoken in degrees; the blind probe; "s of x plus v equals s of x plus u dot v." Recap. |
| 7 | answer | Short answer | 300 | Three verdicts and what would change them. |
| 8 | lens-linalg | Lens 1: linear algebra | 480 | Link type and limits spoken; the three senses of linear. |
| 9 | lens-info | Lens 2: information theory | 330 | The three-feature example spoken; "all three on equals none on". |
| 10 | turn | Your turn | 330 | Notebooks described, no code read; the open question spoken in full. |
| 11 | work | In your work | 280 | |
| 12 | recall | Test yourself | 300 | Questions read, pause, answers. |

Fold-outs F1–F3: one sentence each ("There is a fold-out on …"). Every chapter ends with a recap. Formulas spoken in words. Widgets are described, not read.

---

## 6. Text to add to `toyworlds.md` (the meta-manager adds it)

```
## W9 · The two-dimensional bus (post 03)
- A stream of width 2 ("toy numbers, ours"). One position, two blocks. Order inside a block: attention, then MLP.
- W9-A, the sum: embedding x0 = (1, 2). Block 1 writes a1 = (2, -1) (attention) and f1 = (-1, 1) (MLP). Block 2 writes a2 = (3, -2) and f2 = (-1, 2).
  Running stream: (1, 2) -> (3, 1) -> x1 = (2, 2) -> (5, 0) -> x2 = (4, 2). Norms 2.236, 2.828, 4.472 (descriptive only). x2 = x0 + a1 + f1 + a2 + f2.
  Cancellation: f2 puts +2 in y and undoes the -2 that a2 put there (f2 is not -a2 = (-3, 2); only the y part cancels).
- W9-B, who hears whom (the additive split of a read; not a "virtual weight", which is a weight-matrix product): reader input vector r = (1, 2) reads the stream after a2, (5, 0): r.x0 = 5, r.a1 = 0, r.f1 = 1, r.a2 = -1; total 5 = r.(5, 0). Reader (0, 1): 2, -1, 1, -2; total 0. a1 is in the stream but r hears none of it (a1.r = 0).
- W9-C, the cloud: six streams at one depth. "Calm" (3,1), (4,2), (5,3); "urgent" (1,3), (2,4), (3,5). Probe u = (cos phi, sin phi); score s = u.x.
  Along x: calm 3, 4, 5; urgent 1, 2, 3. Along y: calm 1, 2, 3; urgent 3, 4, 5. Both overlap at 3.
  phi = 135 deg: calm -1.414 (all three), urgent +1.414; margin 2.828. phi = 45 deg: both groups 2.828, 4.243, 5.657 (blind). Margin by phi: 0 at 0/90/180; 0.695 at 100 and 170; 2.000 at 120 and 150; 2.828 at 135; -2.828 at 45.
  Steering: add v to every point; every score changes by u.v. With phi = 135, v = 2u: u.v = 2.000, calm -1.414 -> 0.586, urgent 1.414 -> 3.414. With v = 2(1,1)/sqrt2 (psi = 45): u.v = 0.
- W9-D, rotation (no privileged basis): rotate every vector by 90 deg, (x, y) -> (-y, x), including r. x2 = (4, 2) -> (-2, 4); r = (1, 2) -> (-2, 1). The four read shares stay 5, 0, 1, -1.
- W9-E, three features in two dimensions: feature directions g1 = (1, 0), g2 = (-0.5, 0.866), g3 = (-0.5, -0.866) (0, 120, 240 deg). Strengths (1, 0, 0): stream (1, 0); reads 1.000, -0.500, -0.500. (1, 1, 0): reads 0.5, 0.5, -1.0. (1, 1, 1): stream (0, 0), reads 0, 0, 0.
- W9-F, a toy unembedding: three rows at 0, 120, 240 deg (no norm). Logits at x0 (1.000, 1.232, -2.232); at x1 (2.000, 0.732, -2.732); at x2 (4.000, -0.268, -3.732). The leading token changes after block 1 and stays.
- W9-G, a norm on the read (toy): subtract the mean, divide by the (population) standard deviation: (4, 2) -> (1, -1); (8, 4) -> (1, -1).
- Open-question map (not a toy of the post): M = [[2, 1], [1, 2]]: (1,0) -> (2,1); (1,1) -> (3,3); (1,-1) -> (1,-1).
- Reuse for: dot products and projections, probing, steering, change of basis, interference/superposition, eigen-decomposition, circuits (weighted edges), control (additive input on a state).
```

**Notation to add to `notation.md`.** x_k (stream after k blocks; x₀ = the starting vector, "the embedding"); a_k, f_k (attention and MLP writes of block k); r (a reader's input vector); u (unit direction, angle φ); s = u·x (score); v (steering vector, angle ψ, length α); ω (rotation angle; θ is already the hidden concept); d (stream width); g_j and c_j (feature directions and strengths in the interference toy); M (the open-question matrix). Avoided: θ, m, A, G, ρ, λ, κ, p, q; widget ids avoid the constant `e`. "Block" = one attention sub-layer plus one MLP sub-layer; "after k blocks" is our wording (sources' "layer n" is ambiguous).

---

## 7. Candidate wiki nodes and bridges (candidates only; nothing is created here)

**New nodes** (after just-in-time digests of the three sources): `hidden-state`, `logit-lens`, `linear-probe`, `unembedding`, `direction`, `steering-vector`, `activation-space`. **Updates:** `residual-stream` (add Elhage 2021 and Nanda 2022 grounding; the node is grounded only in `geva-2021-ffn/main` and `kaplan-2020-scaling/main`); `privileged-basis`; `circuit` and `superposition` each need an interpretability sense apart from the electrical and the linearity/coding senses; `feature-steering` has no digest.

**Bridges, all marked `candidate`:**
- residual-stream sum ↔ `vector`, `linear-combination` [same-math]
- read ↔ `dot-inner-product`, `projection` [same-math] (pin the sense: score vs closest point)
- write ↔ vector addition [same-math]
- steering ↔ `affine-function` [same-math]
- no privileged basis ↔ `change-of-basis` [same-math]
- W9-B (read split) ↔ weighted edge in `circuit` [structural-analogy]
- stream ↔ `multiple-access-channel` [structural-analogy] (pending request Q1)
- "bus"/"bandwidth" ↔ Shannon–Weaver channel [metaphor]
- probe vs steer ↔ `do-operator` [structural-analogy]
- Elhage (study the writes, not the stream) versus Nanda (the stream is the central object) [contradicts, a difference of method, not of fact]
- `special-case-of`: probe ⊂ linear read; `historical-influence`: none claimed.

---

## 8. Result slots (filled from `notebook/results.md` at S4; none invented here)

R1 models used, with hidden size, number of blocks, norm type, tie flag, position scheme (T2–T4, T11). R2 length of `hidden_states` and what each index is (T1). R3 per-block additivity: max absolute and relative error, float32 CPU, per model (T7). R4 the last entry versus the final norm (T1). R5 `hidden_states[0]` versus the embedding lookup (T3). R6 the tokens printed and the position index; padding side (T5). R7 the score-shift check score(h + αu) − score(h) = α and the cosine non-additivity check (T9). R-norm the stream's norm by depth and position, described not explained (T10). R-lens whether the final norm plus the unembedding reproduces the logits and the lens with and without the norm (T8). R-TL the TransformerLens versus Hugging Face comparison for GPT-2 (T6), used only if `results.md` gives a clear difference. If any slot has no number by S4, the sentence is dropped, not filled.

Where slots land: §1 (none), §3.6 (R1–R6), §7 identity (R1–R4), §8 (R7), §10 (all as "what to look for"), F3 (R-lens).

## 9. Widget list with checks (S4 will paste `check.mjs` output)

| Widget | Type | Sliders | Edge case | Numbers in text from `check.mjs` |
|---|---|---|---|---|
| sum-table | `stepper` | none | last row (cancellation note) | five stream vectors |
| bus | `diagram` (steps, preview) | none | step 5 | same vectors (step text) |
| positions | `diagram` | none | no arrow back | none |
| read-split | `lab` | 2 | y-only reader: loud parts, silent total | shares 5, 0, 1, −1; total 5; y-only: 2, −1, 1, −2; 0 |
| probe-push | `vec2d` | 3 | blind probe 45°; push sideways | scores, margins (0.695, 2.000, 2.828), u·v (2.000, 0) |
| rotate | `lab` | 1 | shares constant at every ω | coordinates of x₂ (−2, 4 at 90°) and shares |
| three-features | `lab` | 3 | all three on = zero stream | reads 1/−0.5/−0.5; 0.5/0.5/−1; 0/0/0 |

Fold-out tables (F2, F3): numbers from numpy, recorded in `numbers.md`.

## 10. Compliance checklist (what the outline already honours)

- Only brief units; every person-claim sorted by firmness with matching verbs; Olah's strongest unhedged lines next to the hedged ones; Olah L242 always with "have led us to believe"; Nanda L259 whole; Nanda L282/L309 not used as Nanda's own results.
- Not used: Olah L147–148, L249–254, L265, L267, L287, L455, L658; Elhage L181, L417, L535–536, L568, L226; Elhage Related Work (L589–594, L629–635) and appendix L1013–1023, MLP section L788–807, unless the meta-manager widens the scope; the Schwann comparison (no brief unit); "not necessarily a unit vector"; any skip-connection disagreement; any damaged Nanda line as text.
- Quoted paraphrases are avoided: "technically ignore one ReLU", "live in the same space", "about tokens other than the present token", "it does no processing" are not quoted; exact words or no quotation marks.
- Own glosses labelled ours: unit length/angle convention; "direction = weighted mix of coordinates" for the stream; polysemantic/neuron-basis remarks (not used); post-LN effect on a write (only Nanda's words); W9-B as "like an edge weight".
- Hidden state = stream, steering, post-training, RMSNorm formula, standard-deviation convention, and anything on Qwen3/Llama 3/Gemma 3/Mistral: only from `results.md` or flagged as untested.
- Textbook mathematics (dot product, length, unit vector, rotation preserves dot products, cos/sin) is stated with worked numbers, labelled ours, not attributed to a source; every number is re-run.
- Standalone: no reference to another post; the open question names no post; spaced-review cards are copied unchanged and unnamed.
- Phone: ≤ 4 sliders per widget (max 3), ≤ 7 diagram nodes, labels of two words or fewer; display math for long formulas; five-number rule per paragraph.

## 11. Self-score against the rubric (criteria 2, 4, 5)

**Round 1 findings, and what I changed.**
1. g1's right answer (B) was the longest option and g2's right answer (C) was the longest; rewritten so all four options have equal length and the misconceptions (overwrite; first wins; answer-so-far; whole-sentence summary) are serious.
2. g3 used "dot product" before it is defined; reworded to describe the operation in words.
3. Bets before reads (Kunhao's order) would send the reader to later sections for "direction"; fixed with a plain-words instance in §4 and a "cash-in" sentence at the end of §5 and §6 for each bet.
4. Positions (a mechanism) had text only; added the small `positions` diagram.
5. "No privileged basis" and "interference" had no figure; added the `rotate` and `three-features` labs, each with an edge case.
6. Lens 2 leaned on a textbook result that is not in the brief; added Request Q1 and a fallback that uses no textbook claim.
7. The hidden-state identity, the bridge of the post, had a ladder with no numbers; added the result slots R1–R6 and the rule that an unfilled slot drops the sentence.
8. A "virtual weight" label on W9-B would be wrong (S2 note 7); relabelled as "the additive split of a read".

**Round 2 scores (per section).**

| Section | C2 ladder | C4 lenses/insight | C5 illustrations |
|---|---|---|---|
| 1 hook | n/a (no concept) | 4 | n/a |
| 2 guess | n/a | n/a | n/a |
| 3 sum | 5 (L1–L4 full; L4's numbers arrive at S4) | 4 | 5 (stepper, bus, positions) |
| 4 bets | 4 (claims, not derivations; terms get instance + plain reading, numbers in §5–§6) | 4 | 4 (text and F1 only; a 3-row table would be wide) |
| 5 rw | 5 (L5–L7 full, explicit checks) | 4 | 5 (read-split with edge preset) |
| 6 dir | 5 (L8–L10 full, explicit checks) | 5 (cash-ins for bets 1 and 3) | 5 (vec2d, rotate; conditional on `vec2d` passing `test.mjs`, else 4 with the fallback) |
| 7 answer | n/a | 5 (verdict ours, what would change it, per part) | n/a |
| 8 lens-linalg | n/a | 5 (link type, what it adds, what it does not explain, observe-vs-do, 3C) | 4 (no new figure; points back to earlier ones) |
| 9 lens-info | 5 (L11 full) | 4 (link type depends on Q1; fallback keeps it honest) | 5 (three-features, zero-stream edge) |
| 10–12 | n/a | 4 (3C tie, no Discipline data) | n/a |

**Post-level minimums (the gate uses the minimum over sections).** Criterion 2 = **4** (the weakest section is §4, which states claims and holds the numbers for later). Criterion 4 = **4** (the weakest are §1, §3 and §9; §9 depends on Q1). Criterion 5 = **4** (§4 text-only and §8 reuses figures; **5** everywhere a mechanism is drawn). All three are at or above 4. What would lift any of them to 5 is in the fold-outs plan: nothing else is needed for the gate.

**Risks the pedagogy critic is likely to raise.** (a) §3 is dense (seven sub-parts in 1,250 words): the stepper and the diagrams carry the numbers so the prose stays short; (b) §6 has the heaviest load (unit vectors, angles, margin, steering, rotation in 900 words): the vec2d readout carries the scores, and the margin table stays in the widget; (c) the two uses of "projection": decided in 5.1 and used consistently; (d) Lens 2 can read as a promise without payoff: it is a question by design (card decision), with the payoff stated as "for a later reading".

## 12. Requests

One request is written to `requests.md` (Q1: a verified unit on the multiple-access channel). No other fact outside the brief is needed to write around. The notebook numbers (slots R1–R7, R-norm, R-lens) come from `notebook/results.md` before S4; the outline does not wait on them.
