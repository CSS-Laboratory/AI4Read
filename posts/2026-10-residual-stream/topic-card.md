---
name: post03-topic-card
description: S0 topic card for post 03 (interpretability strand 1, "the lens"). Maps every clause of Kunhao's lens sentence to the three saved sources, marks GAPs and technical flags, and proposes lenses, toy world, interactives, exercises and notebooks. Stops at the S0 gate.
date: 2026-10-25
status: proposed to Kunhao; no S1 work until he says go
slug: 2026-10-residual-stream
---

# Post 03 · topic card (S0)

**Proposed title:** *What Is a Hidden State? The Residual Stream, Read and Written*
Alternative: *A Transformer You Can Read: the residual stream as a shared sum*. The word "bus" stays in the text as our metaphor (§6, T13), not in the claim.

**Decisions (Kunhao, 2026-10-25, 16:36 JST). The card is approved; S1 may start.**
1. **"Strand 2" = an eigen-decomposition post.** Kunhao: eigen-decomposition "is worthy to dive into first". The next post (04) is on eigen-decomposition; the canon's *Directions* strand (probing) follows it. Post 03 still contains no eigen-decomposition; its open question points to post 04 (§9).
2. **Post-training clause:** kept out of the lens and stated as an untested working assumption for the *Diffs* strand (R2).
3. **Lenses:** two (linear algebra, information theory). "A probe observes, steering intervenes" is a one-paragraph limit inside Lens 1.
4. **Interactive:** Kunhao prefers the original design (drag the direction) if it is not hard and works on the site. The meta-manager builds a `vec2d` widget (draggable arrows, kept in sync with sliders for keyboard use), tested under the site's strict CSP. If it fails the render tests, the slider version in §8 is the fallback.
5. **Title:** approved as proposed.

---

## 1. The question

**For a high-school reader.** A language model turns every word into a list of numbers and keeps editing that list as it reads. If we stop it halfway and copy the list, what exactly have we copied, and what can we do with it?

**Research version.** (a) Is the "hidden state at layer L" that a library returns the same object as the residual stream at that layer (the token's embedding plus everything earlier attention and MLP blocks added), in the models used in representation analysis? (b) If so, are reading it with a probe, and adding a vector to it, exact vector operations on that stream? (c) Which parts of the "lens" (features as directions, behaviours as circuits, post-training as re-wiring) do the founding sources support, and which stay bets?

**One-line preview after the hook (draft):** "Short version: the vector is a running sum of what every earlier layer wrote; reading it along a direction is a dot product; steering it is adding a vector; and whether a concept *is* a direction is a bet, not a fact."

**Short answer to be earned (ours, provisional; WRITING §0):**
- *Identity.* For a decoder-only transformer with the norm before each block, the hidden state at layer L at one token position is the residual stream there: embedding plus all writes before L. Checked numerically on the model used; never assumed (T1–T5).
- *Operations.* A probe reads one number per direction (a dot product). Steering writes (adds a vector; this is a translation, so affine, not linear). Both are exact in the algebra. What they *mean* depends on a bet.
- *Bets.* The three "Zoom In" claims are the authors' own "deliberately speculative" claims, argued from a vision network. The language-model evidence is not in these three sources.
- *What would change our mind:* the additivity check failing for a model with the hooks placed correctly; or, in later posts, evidence that concept directions are not stable under the intervention tests.

## 2. Why it matters for Kunhao's 3C research (3 lines)
- **Computation.** Probing, similarity analysis and steering are used across his representation work; each is a statement about a vector whose identity has not been fixed. This post fixes it, in the model's own terms.
- **Communication.** A prime or frame added to a model is, in the canon's bridge, a write along a direction (candidate bridge, strand 3). The post only supplies the algebra for it.
- **Collaboration.** None in this post.

## 3. What the post will and will not claim

### 3a. Claims made by people (WRITING §0, §9: exact words, firmness, where, what the post tests)
Line numbers are for the saved `.txt` copies in `posts/2026-10-residual-stream/sources/` (checker use). The web pages have no page numbers; cite by section heading.

| Source (section) | What they say (short quote or paraphrase) | Firmness | The post |
|---|---|---|---|
| Olah et al. 2020, "Three Speculative Claims", L190–195 | "Features are the fundamental unit of neural networks. They correspond to directions." Direction = "a linear combination of neurons in a layer". | Offered as claim; "deliberately speculative" (L220); also normative ("how it's useful to understand them", L186) | States as a bet. Does not test it. |
| Olah, Claim 2, L202–203, L409 | "Features are connected by weights, forming circuits." Weights can be read like an algorithm ("tractable and meaningful"). | Claim; evidence is hand-studied examples | Bet. |
| Olah, Claim 3, L213–215, L587 | "Analogous features and circuits form across models and tasks." They *suspect* it is likely true; more work needed. | Hedged | Bet. Not used for the lens. |
| Olah, scope, L258 | Examples come from InceptionV1, a vision network; they "believe these claims hold generally". | Belief | Say plainly it is a vision article. |
| Elhage et al. 2021, "Virtual Weights and the Residual Stream…", L155 | "The residual stream is simply the sum of the output of all the previous layers and the original embedding." Think of it as a "communication channel". | Asserted (definition and framing) | Used as the base of the sum picture. |
| Elhage, same, L158 | Layers "read in" by a linear map and "write" by adding a linear map back. No privileged basis: rotating all matrices leaves behaviour unchanged. | Asserted, for the idealised model (LN ignored, L142) | Used. Ladder in 2-D (E5). |
| Elhage, scope, L98, L102, L142 | Analysis is of transformers "with two layers or less which have only attention blocks"; no biases; layer norm ignored; larger models not attempted in this paper. | Stated limits | Quote the limits wherever we lean on the paper. |
| Elhage, "Subspaces and Residual Stream Bandwidth", L166–172 | Dimensions behave "something like memory or bandwidth"; "information persists in a subspace unless another layer actively deletes it"; some neurons/heads "may" do memory management. | Mixed: persistence asserted; deletion hedged | Used for the information lens and for cancellation. |
| Nanda 2022 (glossary), "Transformer Overview", L579–599 | "The residual stream after layer n is the sum of the embedding and the outputs of all layers up to layer n." "A separate residual stream for each position." | Asserted (personal explainer, opinionated) | Used. |
| Nanda, "Reading is a projection…", L1000–1002 | Reading = "the residual stream is dotted with each input vector of the relevant matrix"; writing "adds on its output"; "these operations are not opposites". | Asserted | Used; sense of "projection" pinned in §4. |
| Nanda, "Features as directions", L199–203 | "Features as directions is the hypothesis that features are represented in the model as directions in activation space." Recovering a feature would be "projecting onto that feature's direction". | Hypothesis, with an intuition (the model mostly does linear algebra) | Bet. The intuition is Nanda's, not evidence. |

### 3b. Kunhao's lens sentence, clause by clause (status: SUPPORTED / HYPOTHESIS / PARTIAL / GAP)

| # | Clause | Where the three sources speak to it | Status | What the post does |
|---|---|---|---|---|
| 1 | "A transformer is a computation you can read and edit." | *Read:* Olah L409 (weights read as algorithms, in vision circuits); Elhage L95 (aim: reverse-engineer, "like a programmer" with binaries). *Edit:* Nanda L147 defines intervening on an activation; Nanda L1356–1357 points to TransformerLens for editing. | PARTIAL. Ambition and definition are sourced; that edits do what we intend is not. | State as the programme's ambition (their word, hedged). Edits-that-work is strand 3. |
| 2 | "The residual stream is a shared bus: each layer reads from it and writes back into it." | Elhage L155, L158 ("communication channel"; every layer reads by a linear map and writes by adding). Nanda L583 ("shared bandwidth/shared memory"), L1000–1002. | SUPPORTED. "Bus" is our metaphor (canon marks it `metaphor`); no source uses the word. | Keep the words *stream* and *channel* for the sources; say what the bus picture gets wrong (T13). Per-position streams (T5). |
| 3 | "The stream at layer L is the embedding plus every attention and MLP output before L." | Elhage L155; Nanda L579, L586–590 (GPT-2 style, incl. position embedding). | SUPPORTED for the architecture they describe (norm before each block, Nanda L685). **Not** sourced for Qwen3, Llama 3, Gemma 3, Mistral. | Earned by the 2-D sum, then verified in the notebooks on real models (T1–T4). |
| 4 | "Concepts tend to live as directions." | Olah Claim 1 (speculative, vision). Nanda L199–203 (hypothesis). Elhage speaks of *subspaces* (L126, L166), not concept directions. | HYPOTHESIS only. The three sources give a definition and an intuition. **GAP: language-model evidence.** | State as a bet. Do not test it. Later source: `park-2024-linear-representation`, `marks-2024-geometry-of-truth` (strand 2). Name them as "next", no claims about their content. |
| 5 | "Behaviours are circuits that read and write directions." | Circuit = features plus weighted edges (Olah L202–211, glossary L668); components read and write the stream (Nanda L997–1002); circuit as a computational subgraph (Nanda L372–385). Elhage finds circuits only in attention-only models of two layers or fewer (L98). | PARTIAL. Circuits that read/write the stream: supported as a way of describing small algorithms. **GAP: "behaviours"** (refusal, trust, expertise) as circuits: none of the three says this. | Reframe (a bet we do not test): "Some small algorithms in small models have been described as circuits that read and write subspaces; whether a behaviour studied in social science is such a circuit is open." Later: `wang-2023-ioi`, `arditi-2024-refusal-direction`, `lindsey-2025-biology` (strands 3–4). |
| 6 | "Post-training mostly rewires which directions get read out, not what is represented." | Nanda L905–910 defines fine-tuning and RLHF only. Nothing on what they change. | **GAP. Unsupported.** Canon summaries (unread, so treat as unverified) point both ways: `jain-2024-safety-finetuning` (small transform on a preserved representation); `lindsey-2025-biology` (a "harmful request" feature assembled during fine-tuning); `minder-2025-chat-crosscoders` (chat-tuning adds concepts). | Do **not** put it in the lens. One sentence in §8 of the post, labelled "a working assumption of the reader's, untested here; strand 6 tests it". Reframed as a bet, it reads: "same architecture means the same stream space, but whether coordinates and directions carry over from base to instruct is an assumption." |
| 7 | (Phenomenon) "Every hidden-state read is a read of the residual stream at one layer." | Not in the three sources. The word "hidden state" does not occur in any of them. Elhage L632 notes the probing literature calls the same vectors "embeddings". | **GAP (source).** Earned only by the numerical check in notebook 02 plus the installed library code (T1–T3). | State as: "In the pre-norm models we checked, the vector `output_hidden_states` returns at index L equals…" with the notebook's numbers. |
| 8 | (Phenomenon) "A probe is a projection onto a direction." | Nanda L1586–1587 (a probe is a trained 1-D linear map "corresponding to a direction"); L199–203 (recovering a feature by projecting). | SUPPORTED as definition, conditional on clause 4. | Dot-product ladder in 2-D. A probe's accuracy is not in scope (strand 2). |
| 9 | (Phenomenon) "Steering adds a primed direction." | **Not in the three sources** (no entry for steering or activation addition). | **GAP.** The *algebra* follows from "writing adds" (Nanda L1002) and is labelled ours. That steering changes behaviour is strand 3. | Teach steering as one more write, in 2-D. Later: `turner-2024-activation-addition`, `panickssery-2024-caa`. |
| 10 | (Phenomenon) "Everything I do (probe, compare, steer) is a linear operation." | Elhage L121: "linear if one freezes the attention patterns" (attention-only models). Elhage L1019: layer norm is not linear. | **Needs correction.** Probe = linear read plus a threshold. Steering = translation (affine, `wiki/concepts/affine-function.md`: linear only if the constant is 0). Cosine similarity divides by norms (nonlinear). The stream's *bookkeeping* is additive; the layers' internal computation is not linear. | See T9 and the three senses of "linear" in §4. |

## 4. Threshold words and their senses (WRITING §0)

| Word | Sense the post uses and tests | Senses it does not use |
|---|---|---|
| **hidden state** | The vector returned for one token position at the boundary after L blocks; the post tests whether it equals the residual stream there. | "The model's belief", "the sentence's meaning", "a summary of the whole prompt". |
| **residual stream** | The running sum at one token position (embedding + all writes so far). One stream per position (Nanda L598). Also called "embedding" in the probing literature (Elhage L155, L632). | The skip connection alone (Nanda L580–581 discusses this reading). |
| **layer** | "After L blocks"; block = one attention sub-layer + one MLP sub-layer. Nanda notes the usage clash (L577). The post says *block* and *sub-layer*. | Layer = attention or MLP alone. Index base (0 or 1) is settled by the notebook (T1). |
| **read** | *Inside the model:* a component takes the stream as input through linear maps, i.e. dot products with its input vectors (Nanda L1000). | *Our instruments* (copying a hidden state out): called "read out" or "extract" in the post, never plain "read". |
| **write** | A component *adds* a vector to the stream (Nanda L1002). Never overwrites. | Replace, assign. |
| **direction** | A unit vector up to sign; "the score along u" = u·x. In the stream there are no neurons (Nanda L736). | Olah's "linear combination of neurons in a layer" (L194) is the same idea for vision layers; the post says so once, as our translation. |
| **linear** | (i) The stream is a **sum** of writes. (ii) A **read** is linear in the stream. (iii) A **concept is linearly readable** (a bet). Steering is *affine*. | "The model is linear" (false: MLPs, attention weights, norms are not). |
| **projection** | (a) the number u·x for unit u (the post's default); (b) the vector (u·x)u (closest point on the line, `wiki/concepts/projection.md`). Nanda's "reading is a projection" means a set of dot products, i.e. a linear map (L1000); Elhage writes "linear projection" for the same (L148). | "Projection" as the closest-point operator only. |
| **feature / concept** | *Feature* = a scalar the model could compute from the input (Olah glossary, L694). *Concept* = a human label (calm, urgent). Whether a concept is a feature is a bet. | Using the two as synonyms. |
| **circuit** | A subgraph of features/components and the weights between them (Olah L668, Nanda L372). | Electrical circuits (`wiki/concepts/circuit.md` is full of them, T12). |
| **superposition** | Only the model-side phenomenon of packing more features than dimensions, and only as a question for strand 5. | The linear-algebra "superposition principle" f(αx+βy)=αf(x)+βf(y) and Cover's "superposition coding" (both sit under `wiki/concepts/superposition.md`, T12). For stream sums the post says "adding", never "superposing". |
| **bus** | Our metaphor for a shared medium everyone writes to and reads from. | A hardware bus with one writer at a time. T13. |

At most **one term box**: "Residual stream (also: hidden state, embedding)". Everything else is defined in the sentence where it first appears.

## 5. Technical flags (not covered by the three sources; verify, do not state from memory)

Each item: the issue, why the post or a notebook depends on it, and the resolution. None may enter the post unless the notebook output or a saved source shows it.

| ID | Issue | Resolution |
|---|---|---|
| T1 | **How Hugging Face `hidden_states` line up with block outputs.** Which index is the embedding; whether `hidden_states[l+1]` is the output of block l (after the residual add); whether the last entry has the final norm applied. Not in any of the three sources. | Notebook 02 prints the lengths, then tests `hidden_states[l+1] - hidden_states[l]` against the hooked attention and MLP outputs for every l, in float32. Read the installed modeling file for the exact version and save the relevant lines in `sources/` with the version number. A mismatch at the last index is a result to explain, not hide. |
| T2 | **Norm placement and type in the four families.** The sources describe LayerNorm applied at layer input ("pre-LN", Nanda L685; "post-LN… BERT", L872) and Elhage ignores it (L142). Nanda's glossary has a one-line RMSNorm entry ("A variant of LayerNorm", L824–829; S2 note 1); the details of the formula are not in the sources. The families in Kunhao's work may use a different norm, and Gemma 3 may add norms around sub-layer outputs (suspicion from memory only). If a norm sits between a sub-layer and the add, the vector *added* to the stream is not the module's raw output, and a hook on the module would give a wrong "write". | Print the module tree and the decoder-layer source; place hooks by reading it; let the additivity check decide. Do not describe RMSNorm in the post unless its definition is fetched (T-source list in §12). |
| T3 | **Embedding scaling and tying.** Whether `hidden_states[0]` equals the embedding-table lookup or is scaled; whether the unembedding is tied to it (Nanda L707 says models *may* tie). | Compare `hidden_states[0]` with `embed_tokens(ids)`; print `tie_word_embeddings`. |
| T4 | **Position information.** GPT-2 adds a learned position vector into the stream (Nanda L586, L671); rotary models "don't add anything in to the residual stream" (Nanda L679). So "embedding" in clause 3 means different things. | Say "token embedding (plus a position embedding in GPT-2)". Check by T3's test. |
| T5 | **One stream per position.** "A 4096-number vector from layer 20" needs a position (last real token? mean over tokens?). Padding side and a possible BOS token change which index is "last". Nanda L598–601: only attention moves information between positions. Pooling over positions is a further operation. | Notebook 02 takes an explicit position index, prints the tokens, and states the padding side. The post never speaks of "the hidden state of a sentence". |
| T6 | **TransformerLens hook names and weight processing.** `resid_pre`, `attn_out`, `mlp_out`, `resid_post` and "resid_post = resid_pre + attn_out + mlp_out" are TransformerLens conventions, not in the three sources (Nanda names only `pre/mid/post/mlp_out` for a toy MLP, L1170–1177). TransformerLens may also rewrite weights on loading (suspicion from memory: folding the norm, centring the weights that write to the stream). If so, its stream differs from Hugging Face's for the *same* GPT-2. | Fetch the TransformerLens docs (canon lists them as an uncatalogued supplement). In notebook 01 compare TL's `resid_post` with HF GPT-2 `hidden_states`, with and without weight processing; report the difference and its direction. |
| T7 | **Numerical tolerance.** "Equals" means equal up to rounding. Half-precision or MPS runs will not match to the same digits. | Do equality checks in float32 on CPU; print max absolute and relative error (relative to the stream's norm); choose the tolerance after seeing the float32 error, not before. |
| T8 | **Logit lens details.** The definition in Nanda's entry is **corrupted in the saved page** ("…after layer $kper-token loss", txt L1424; the HTML has the same gap). Intact parts: the lens normally applies the final norm, unembeds, then log-softmax (L1425); "layer normally means block" (L1430); equivalent to zero-ablating later blocks (L1432); the "key finding" (L1427). Elhage's version is W_U·x with the norm ignored (L589–593). | Use Elhage L589–593 and the intact Nanda lines; fetch the original post by nostalgebraist (linked in the saved glossary HTML) and the Dynalist original. In notebook 01 check that applying the final norm and unembedding to the last block's stream reproduces the model's logits; show the earlier layers with and without the norm. Describe results; do not claim the lens is faithful. |
| T9 | **"Linear" overclaim** (clause 10). | See §4. Test in the notebook: score(h + αu) − score(h) = α for unit u (affine shift), and that cosine similarity is not additive. Arithmetic only, no behavioural claim. |
| T10 | **Norm growth and outliers.** The notebooks plot the stream's norm by layer and by position. The sources say nothing about how it should look, and a first-token or special-token position may behave differently (suspicion from memory). | Plot per position; describe what is seen; offer no explanation. |
| T11 | **Model numbers** (hidden size, number of blocks, the "4096"). | Printed from `config` in the notebook. The post states only the toy's numbers and, as Kunhao's own example, "4096". |
| T12 | **Wiki name collisions.** `superposition` mixes linearity (Boyd) and Cover's superposition coding with Elhage's feature packing; `circuit` is mostly electrical; `projection` is the closest-point sense; `residual-stream` is grounded only in `geva-2021-ffn/main` and `kaplan-2020-scaling/main` (not in Elhage 2021); `feature-steering` and `circuit` have no digest. | Digest the three sources just in time (Kunhao's instruction) and split or alias the nodes (§13). Candidate only. |
| T13 | **The bus metaphor misleads in one way.** A hardware bus has one writer at a time and addresses; the stream has all writers adding at once, with no addresses, and readers see a *mix* (Nanda L1000). Also, no noise: the sum is exact. | A short trap box; Lens 2 says what the metaphor leaves out. |
| T14 | **Source scope.** Olah: a vision network. Elhage: attention-only, two layers or fewer, no norm, no biases, larger models explicitly not attempted. Nanda: a personal, opinionated explainer ("in my opinion is wildly unprincipled", L707) whose saved copy has at least one corrupted entry. All three predate the models in Kunhao's work; nothing on post-training. | Say it in the post when each is first cited. |

## 6. Lenses (two, as Kunhao asked; a third considered)

### Lens 1 · Linear algebra
- **Canon / wiki:** `canon/linear-algebra.md` (`boyd-2018-vmls`, `strang-2023-introduction`, `deisenroth-2020-mml`; optional viewing `sanderson-2016-essence`). Nodes: `wiki/concepts/vector.md`, `linear-combination.md`, `dot-inner-product.md` (alias `dot-product.md`), `projection.md`, `orthogonality.md`, `norm.md`, `linear-map.md`, `affine-function.md`, `basis.md`, `change-of-basis.md`, `subspace.md`, `privileged-basis.md`. Digests: `wiki/works/boyd-2018-vmls/ch01-vectors.md`, `ch02-linear.md`, `ch03-norm.md`; `strang-2023-introduction/ch01-vectors.md`, `ch04-orthogonality-p1.md`; `deisenroth-2020-mml/ch03-analytic.md`.
- **Link type:** *same-math.* The stream is a sum of vectors; a read is a dot product; a write is vector addition; steering is a translation. (Caveat: only the bookkeeping, not the sub-layers.)
- **What only this lens shows:** exactness. It turns "the hidden state" into something we can add up and check, shows that a read decomposes over writers (the "who hears whom" number, W9-B), and explains *no privileged basis* as invariance of dot products under rotation (Elhage L158; E5).
- **What it does not explain:** why the model's concepts would be directions at all; anything about the nonlinear parts (MLP activations, attention weights, norm). One paragraph of limits, including: a probe is a read, so a high score shows information is present, not that the model uses it (the *see vs do* point; `wiki/concepts/do-operator.md`; full treatment in strands 2–3).

### Lens 2 · Information theory
- **Canon / wiki:** `canon/information-theory.md` (`shannon-1948-mathematical`, `cover-2006-elements`, `mackay-2003-information`). Nodes: `wiki/concepts/multiple-access-channel.md` (MacKay p. 237: several transmitters, one receiver, a noiseless adder), `capacity-region.md`, `channel-capacity.md`, `noisy-channel.md`, `mutual-information.md`. Digests: `wiki/works/mackay-2003-information/ch15-further.md`, `cover-2006-elements/ch14-network-p1.md`.
- **Link types:** *structural analogy* for "one noiseless adder, many writers, one reader" (the multiple-access channel with output = sum of inputs). *Metaphor* for "bus" and "bandwidth" (canon bridge: `metaphor`). Elhage's "bandwidth" counts dimensions; Shannon's bandwidth is a rate in Hertz.
- **What only this lens shows:** the *question about limits*. d dimensions, many things to say: how many separate messages can one reader recover if interference is tolerated? Sourced set-up: Elhage L170 (an MLP has about four times more neurons than the stream has dimensions; "communicating in superposition"); Nanda L280 (50,000 tokens, 768 dimensions: "almost has to be more features than dimensions"); Olah L510 footnote (n orthogonal vectors, exponentially many almost orthogonal ones: we pose this, we do not use it as a result).
- **What it does not explain:** the stream is noise-free and deterministic, so no capacity can be computed and no code is involved. Superposition is **posed as a question only**; the answer is strand 5.

### Considered, not proposed
- *Causal inference (see vs do)* would show that a probe observes and steering intervenes. Real, but it rests on strands 2–3 and none of the three sources. Kept as the one-paragraph limit in Lens 1 (default). Say yes if you want it as a full third lens (about 300 words, `do-operator.md`).
- *Control theory* (steering as an additive control input on a state; canon bridge `structural-analogy`) belongs to strand 3.
- *Communication theory* (bus ↔ Shannon–Weaver, canon `metaphor`) is already inside Lens 2.

## 7. Hook, guesses, running toy world

**Hook (generic, second person; no Discipline data or prompts; the person is the hint, WRITING §0).** You run a sentence through a language model, stop it at layer 20, and copy out a list of 4096 numbers. You train a classifier on lists like this, compare lists from two models, and add a list to another list to push the model one way. All three steps treat the list as something definite. What is it? Open with this, in plain words, then the one-line preview.

**Guess first (answer options similar in length; right answer not the longest).**
1. *What is the copied list?* (A) The model's answer so far. (B) The sum of what every earlier layer wrote, starting from the word's own vector. (C) The output of layer 20 alone. (D) A summary of the whole sentence. Right: (B), with the per-position and norm caveats.
2. *Layer 3 writes (−2, −2) into a stream that holds (2, 2). What can layer 4 read?* (A) Nothing, the stream is empty. (B) Only layer 3's vector. (C) The sum, (0, 0), so nothing of either vector. (D) Whichever vector arrived first. Right: (C). Sets up cancellation (Elhage L168, hedged).
3. *Add the same vector v to every point of a cloud. A probe scores each point by one dot product. By how much does each score change?* (A) By the same amount for every point. (B) More for points far from the origin. (C) Only for points near the probe line. (D) It depends on each point's length. Right: (A), by u·v.

**Running toy world W9 · The two-dimensional bus (to add to `toyworlds.md`; numbers checked by code, 2026-10-25; the stream here is 2-D, "toy numbers, ours").**

*W9-A, the sum (2 blocks, d = 2).* Embedding x₀ = (1, 2). Block 1 writes a₁ = (2, −1) (attention) and f₁ = (−1, 1) (MLP). Block 2 writes a₂ = (3, −2) and f₂ = (−1, 2).
- x₀ = (1, 2), norm 2.236.
- After a₁: (3, 1). After f₁: x₁ = (2, 2), norm 2.828.
- After a₂: (5, 0). After f₂: x₂ = (4, 2), norm 4.472.
- Check: x₂ = x₀ + a₁ + f₁ + a₂ + f₂ = (4, 2). Cancellation: f₂ writes +2 in y, undoing the −2 that a₂ wrote.

*W9-B, who hears whom.* The MLP in block 2 has one neuron whose input vector is r = (1, 2). It reads the stream after a₂, (5, 0): r·(5, 0) = 5. The read splits over writers: x₀ gives 5, a₁ gives 0, f₁ gives 1, a₂ gives −1; total 5. a₁ is in the stream but this neuron hears none of it, because a₁·r = 0. (Elhage's "virtual weight", L162, in its smallest case; true here because nothing nonlinear sits between the writes and the read.)

*W9-C, the cloud.* Six prompts' streams at one layer, two groups.
- "Calm": (3, 1), (4, 2), (5, 3). "Urgent": (1, 3), (2, 4), (3, 5). (The calm point (4, 2) is x₂ from W9-A.)
- Probe direction u at angle φ: u = (cos φ, sin φ); score s = u·x.
- Along the x-axis (φ = 0): calm 3, 4, 5; urgent 1, 2, 3. They touch at 3. Along y (φ = 90°): calm 1, 2, 3; urgent 3, 4, 5. They touch at 3. No single coordinate separates the groups.
- Along u = (−1, 1)/√2 (φ = 135°): every calm point scores −1.414 and every urgent point +1.414, a margin of 2.828. Along (1, 1)/√2 (φ = 45°) the two groups have identical scores (4, 6, 8 over √2): the probe is blind.
- Margin (best gap between the groups) by φ: 0 at 0°, 90°, 180°; 0.695 at 100° and 170°; 2.000 at 120° and 150°; 2.828 at 135°; −2.828 at 45°.
- Steering: add v = α(cos ψ, sin ψ) to every point. The score of every point changes by u·v = α cos(φ − ψ). With φ = ψ = 135°, α = 2: calm scores −1.414 → 0.586 (the probe now calls calm points urgent), urgent → 3.414. With ψ = 45°, φ = 135°: shift 0, though every point moved by α.
- Direction matches the sources: the axes (neurons) do not isolate the concept, a direction does (Nanda L242, L736; Elhage L158). Steering results are arithmetic only (not evidence that behaviour changes).

Notation to add to `notation.md`: x_ℓ (stream after ℓ blocks, x₀ = embedding), a_ℓ, f_ℓ (attention and MLP writes of block ℓ), r (a reader's input vector), u (unit direction), s = u·x (score), v and α (steering vector and strength), φ, ψ (angles), d (stream width). Avoids θ, m, A, G (taken by earlier posts) and `e` (a constant in the widget language).

## 8. Interactives (component library `site/ai4read/components/`)

1. **Bus diagram → `diagram` with `steps` and `"preview": true`.** Seven nodes at most (labels of two words or fewer): `Embed`, `Attn 1`, `MLP 1`, `Attn 2`, `MLP 2`, `Unembed`, and the stream band. Writes are solid arrows into the band, reads dashed arrows out. Five steps, each revealing one writer and setting the readout to W9-A's running sum ("stream so far = x₀ + a₁ + f₁ …" with the numbers above). Vertical layout recommended for 375 px. *Difference from the input:* the library has no "tap a layer" (only `cascade` has tap); Next/Back replaces it. A `stepper` table under it can hold the same rows (the reader adds the vectors by hand first, WRITING §2).
2. **2-D projection and steering toy → `vec2d` (new widget, built by the meta-manager; Kunhao's decision 4).** The reader drags the probe arrow u (angle φ) and the steering arrow v (angle ψ, length α) over the six W9-C points; sliders for φ, ψ and α stay under the canvas for keyboard and screen-reader use, and dragging moves the sliders. The probe line through the origin and each point's foot on it are drawn; the readout gives the six scores, the margin and u·v. Equal x/y scale is built in, so angles look right. Presets for the edge cases: "axis only" (φ = 0), "best probe" (φ = 135°), "blind probe" (φ = 45°), "steer along" (φ = ψ = 135°, α = 2), "steer sideways" (φ = 135°, ψ = 45°, α = 2). The writer uses the config format in `site/ai4read/components/README.md` (§ `vec2d`) and copies from `gallery.html`. **Fallback** if `vec2d` fails the render tests: the same toy as a `plot` with three sliders (`phi` 0–180°, `psi` 0–180°, `alpha` 0–3), six `points`, the probe line as a curve (`sin(phi*pi/180)/cos(phi*pi/180)*x`), `height` ≈ 340 and equal x/y ranges.
3. Optional third, small: the W9-B read-split as a `lab` or `stepper` (four writers, one reader r).

## 9. Exercises (4 + 1) and the open question

Hand-computable, with the hint and a folded solution (WRITING §6). Every answer below is checked by code.
- **E1 · Add.** With W9-A, compute x₁ and x₂, then check x₂ = x₀ + a₁ + f₁ + a₂ + f₂. Variation: what must f₂ be for block 2 to leave the stream unchanged? (f₂ = −a₂ = (−3, 2).)
- **E2 · Who hears whom.** Compute r·x₀, r·a₁, r·f₁, r·a₂ for r = (1, 2); show they add to r·(5, 0) = 5. Which writer is inaudible, and why?
- **E3 · Project.** Score the six points on (1, 0), (0, 1) and (−1, 1)/√2. Which direction leaves a gap? Which direction gives all six the same score pattern in both groups?
- **E4 · Steer.** Add v = (−2, 2) to every point. Show each score on u = (−1, 1)/√2 rises by u·v = 2.828. Then add v = (2, 2): the score change is 0. Which probe angle would see it?
- **E5 · Rotate (no privileged basis).** Rotate every vector by 90° ((x, y) → (−y, x)), including r. Show the four read-shares (5, 0, 1, −1) are unchanged. What does that say about "coordinate 2 of the stream"?
- **Open question for post 04, eigen-decomposition (not answered in the post).** Suppose, as a toy assumption (ours; real blocks are not linear), that what a block reads and writes back amounts to one matrix M acting on the stream. Take the 2-D toy map M = [[2, 1], [1, 2]]. It turns (1, 0) into (2, 1): a new direction. But it sends (1, 1) to (3, 3) and (1, −1) to (1, −1): those two directions are only stretched, by 3 and by 1. Are there always such directions? And if the stream has no privileged basis, could the directions a map only stretches be the "natural axes" that the coordinates do not give us? (Numbers checked by code. Wiki: `wiki/concepts/eigenvector-eigenvalue.md`, `wiki/concepts/matrix-as-transformation.md`. The inner-product question drafted earlier, ⟨a, b⟩ = 2a₁b₁ + a₂b₂, is kept for the *Directions* post.)

## 10. Notebooks (`posts/2026-10-residual-stream/notebook/`)

Both run offline once the models are present (`local_files_only`), print library versions, end with blank exercise cells (E1–E5 in code form).

**01_bus_gpt2.ipynb (TransformerLens, GPT-2 small; ARENA 1.1–1.2 scope only).**
1. Load; print n_layers and d_model from the config. 2. Cache one forward pass on a short prompt. 3. For every block: `resid_post − (resid_pre + attn_out + mlp_out)`, max absolute and relative error, float32 on CPU (T7). 4. Telescoping: the stream after block L equals the embedding(s) plus all earlier writes. 5. Norm of the stream by layer and by position (T10; describe only). 6. Logit lens by layer: with and without the final norm; check the last block reproduces the model's logits (T8). 7. W9 in numpy: reproduce every toy number. 8. TL vs Hugging Face GPT-2 comparison (T6). 9. Blank exercises.
**Out of scope:** induction-head search, attention-head algebra (strand 4), patching beyond a one-line mention, SAEs, eigen-decomposition.

**02_bus_my_model.ipynb (plain Hugging Face + hooks).**
`MODEL_PATH` parameter; default Qwen3-1.7B-Base if it loads, else GPT-2 small. 1. Print the module tree, config (hidden size, number of blocks, norm type, tying, positional scheme) and the decoder-layer source lines (T2, T3, T4). 2. `output_hidden_states=True`; compare `hidden_states[0]` with the embedding lookup (T3). 3. Forward hooks on the attention and MLP modules found by inspection, not by assumed names (T2). 4. Per-block additivity test against `hidden_states` (T1), with a clear report of where it fails. 5. The last entry versus the final norm (T1). 6. Take an explicit position and layer; show the vector equals embedding plus the hooked writes (T5). 7. Arithmetic on a real stream: score along a random unit direction, and the shift under h + αu equals α (T9). No difference-of-prompts vector (that is strand 3). 8. Blank exercises.
**Not reproduced:** any Discipline prompt, data, probe or result. For CI without downloads, test the code path on a tiny randomly initialised model built from the config.

## 11. Outline and length (main text ≤ 7,500 words; target about 6,600)

| § | Content | Words |
|---|---|---|
| 1 | Hook, one-line preview | 300 |
| 2 | Guess first (3 questions, answers folded) | 250 |
| 3 | From words to vectors; add two vectors by hand; the bus diagram; the stream is a sum; one stream per position; hidden state = stream (earned by notebook numbers); term box | 1,400 |
| 4 | Reads and writes: the dot-product ladder in 2-D; who hears whom (virtual weight); cancellation; the 2-D probe/steer widget; no privileged basis | 1,500 |
| 5 | The three Zoom In claims, as bets (what each says, firmness, vision scope, what each would mean for the stream, what we test: only the algebra) | 900 |
| 6 | **Short answer** (boxed), then Lens 1 and Lens 2 with link types and limits; the superposition question | 1,500 |
| 7 | Your turn: notebooks, E1–E5, open question | 350 |
| 8 | Where this shows up in your work: read, compare, write; what each licenses; the post-training clause as an untested working assumption | 450 |
| 9 | Recall (5–8; reuse earlier-post questions without naming them), Sources | 350 |

Fold-outs (not counted): (1) why a norm before a block barely changes what a block can read (Elhage L1013–1021: mean-centring is a fixed linear map; scaling commutes), a "Look inside"; (2) Olah's full claims with the Schwann comparison. Audio: standard, chapters match sections, "AI4Read from CSS Lab".

## 12. Sources

**Saved for offline checking (URL and access date at the top of each file):** `sources/olah-2020-zoom-in.txt` (+.html), `elhage-2021-framework.txt`, `nanda-2022-glossary.txt` (the glossary's `.txt` and `.html` both carry the corrupted logit-lens line, T8).

**Knowledge base used** (digests are `grounding: primary-text`, `verified: repaired`, i.e. model-verified, no independent audit recorded; every claim is rechecked at write time, Charter §9):
- Linear algebra: `wiki/concepts/{vector, linear-combination, dot-inner-product, dot-product (alias), inner-product, projection, orthogonality, norm, cosine-similarity, linear-map, affine-function, basis, change-of-basis, subspace}.md`; `wiki/works/boyd-2018-vmls/ch01-vectors.md`, `ch02-linear.md`, `ch03-norm.md`; `strang-2023-introduction/ch01-vectors.md`, `ch04-orthogonality-p1.md`; `deisenroth-2020-mml/ch03-analytic.md`.
- LLM: `wiki/concepts/{residual-stream, residual-connection, privileged-basis, layer-normalization, word-embedding, superposition, circuit, feature-steering}.md`; `wiki/works/geva-2021-ffn/main.md` (residual stream, p. 5490), `prince-2023-udl/ch11-residual.md` (p. 189), `ch12-transformers.md`, `vaswani-2017-transformer/main.md`, `elhage-2022-superposition/main-p1.md` (privileged basis, for the strand-5 question only).
- Information theory: `wiki/concepts/{multiple-access-channel, capacity-region, channel-capacity, noisy-channel, mutual-information, superposition-coding}.md`; `wiki/works/mackay-2003-information/ch15-further.md`, `cover-2006-elements/ch14-network-p1.md`.
- Optional see/do paragraph: `wiki/concepts/do-operator.md`, `wiki/works/pearl-2009-causality/main.md`.
- Canon files: `canon/interpretability.md` (Scope, strand 1, concept spine, bridges, reading path), `canon/llm.md` (`elhage-2021-circuits`).

**Not in the knowledge base (searched):** any digest of the three sources; nodes for hidden state, logit lens, linear probe, unembedding, direction, steering vector, hook, activation.

**Gaps and what to do** (free and legal sources only):
| Gap | Fetch or ask |
|---|---|
| Hugging Face library semantics and decoder-layer code for the model families (T1–T4) | The installed `transformers` package source on Kunhao's Mac, saved by file and version into `sources/`; Hugging Face documentation page for `output_hidden_states`. |
| TransformerLens hook names and weight processing (T6) | TransformerLens documentation (open source; canon lists it as an uncatalogued supplement). Save with URL and date. |
| Logit lens definition (T8) | nostalgebraist's original post (the link is in the saved glossary HTML) and the Dynalist original of the glossary (link in the saved page). |
| RMSNorm definition, only if the post names it (T2) | The original RMSNorm paper on arXiv (identifier to be confirmed at fetch). Otherwise the post says "a normalisation". |
| Language-model evidence for directions, circuits, post-training (clauses 4–6) | Not needed for the post (bets, pointers only). Strand sources: `park-2024`, `marks-2024` (clause 4); `wang-2023-ioi`, `arditi-2024` (clause 5); `jain-2024`, `lindsey-2024-crosscoders`, `minder-2025` (clause 6). All free in `canon/free-manifest-interpretability.json`; digest before any claim about their content. |
| ARENA 1.1–1.2 | Used only for notebook scope; no claim in the post rests on it. |

## 13. Wiki and graph (candidates only, per Kunhao)
New nodes after the just-in-time digests: `hidden-state`, `logit-lens`, `linear-probe`, `unembedding`, `direction`, `steering-vector`, `activation-space`. Update `residual-stream` with Elhage 2021 and Nanda; give `circuit` and `superposition` an interpretability sense apart from the electrical and linearity senses (T12). Proposed bridges, all marked **candidate**: residual-stream sum ↔ `vector` / `linear-combination` [same-math]; read ↔ `dot-inner-product` / `projection` [same-math]; write ↔ vector addition [same-math]; steering ↔ `affine-function` [same-math]; no privileged basis ↔ `change-of-basis` [same-math]; stream ↔ `multiple-access-channel` [structural-analogy]; "bus" ↔ Shannon–Weaver channel [metaphor]; probe vs steer ↔ `do-operator` [structural-analogy].

## 14. Risks and corrections to the input; English; gate

- **R1. "Strand 2" (resolved 2026-10-25).** Kunhao chose eigen-decomposition as the next post (04), before the canon's *Directions* strand. Post 03 has no eigen-decomposition; the open question (§9) points to post 04.
- **R2. Clause 6 (post-training).** Unsupported by the three sources; the canon summaries disagree with each other; it is also the clause a reader would take as a result. Keep it out of the lens.
- **R3. Clause 5 ("behaviours are circuits").** The sources give small algorithms in small or vision models, not behaviours such as refusal or trust.
- **R4. "Everything is a linear operation."** Steering is affine, cosine similarity is nonlinear, and the layers are not linear (T9).
- **R5. "Hidden state = residual stream"** is the bridge of the whole post and is in none of the sources. It stands on notebook evidence and library code only (T1–T5).
- **R6. Nanda entries.** "hook": not in the glossary (only `HookedTransformer`). "logit lens": present but corrupted in the saved copy. "activation" (L399) and "residual stream" are intact; "direction" has no entry of its own (content under "Features as directions", L199, and "Activation space", L400).
- **R7. Hook paragraph.** "I pull a 4096-number vector out of layer 20" is first-person and about your pipeline. The post uses it as a generic second-person hook (WRITING §0); nothing from Discipline appears.
- **R8. Opening line of the lens** ("bus") is sourced only as a metaphor, and a bus has one writer at a time (T13).
- **R9. Canon commit:** done by the meta-manager on 2026-10-25 (commit 971703a, "canon: add interpretability field (34 items, 7 strands)"); the manifest has 34 entries, matching your count.
- **English.** The post's prose stays plain (B2 reader, WRITING §1). English study material is a separate C1–C2 pack for Margin (WRITING §8, v0.8); `english-gloss.json` and a B2-level gloss are not part of this post.

**Gate: passed.** Kunhao said go on 2026-10-25 with the decisions at the top of this card. S1 (source brief, at least 8 units, from the saved copies and the library, marking anything unseen as `UNSEEN`). Suggested S1 units: (1) Olah claims 1–3 with hedges; (2) Olah polysemantic and superposition passages; (3) Elhage stream as sum and channel; (4) virtual weights; (5) subspaces and bandwidth; (6) no privileged basis and layer norm folding; (7) Nanda reading as projection and writing; (8) Nanda features as directions, privileged basis, bottleneck superposition; (9) Nanda per-position streams, positional schemes, LN placement; (10) logit lens (Elhage + Nanda; the original logit-lens post is not in the canon or the saved sources, so it is a gap, not a source).
