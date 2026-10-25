---
name: post03-verify-1
stage: S5, round 1
checker: independent fact-checker (fresh agent; did not write the post)
date: 2026-10-25
checked: src/content.html (text, widget configs, fold-outs, recall, sources), audio-script.md, english/english.json
evidence: source-brief.verified.md (units 1-15, S2 notes, writer-must-not-use list); sources/*.txt (line numbers are file lines, as in the brief); sources/mackay-2003-mac.txt; notebook/results.md and the executed cells of notebook/01_bus_gpt2.ipynb and 02_bus_my_model.ipynb; check.mjs; topic-card.md
independence: self-review.md not read; numbers.md read only after this pass was complete (no disagreement with it)
---

# S5 verify, round 1: post 03

Severity follows rubric §A. Locations give the section id and the content.html line. Source lines are lines of the saved `.txt` files.

## Critical

None.

## Major

### V1-01 · major · the short answer says the sources give no language-model test, but Elhage has circuit results in small attention-only transformers
- **Where.** `#answer`, l. 372: "For language models the three sources give no test, so we hold all three as bets." Audio `answer`, l. 132: the same.
- **Evidence.** The post itself, `#bets` l. 182: "Elhage and colleagues limit their circuit results to transformers “with two layers or less which have only attention blocks”". Elhage L98: "in this paper we will study transformers with two layers or less which have only attention blocks"; L100: "we find that specific attention heads that we term “induction heads” can explain in-context learning in these small models".
- **Problem.** As written, the sentence is false for bet 2. The three sources do include circuit work on (toy, attention-only) language models. Kunhao's scope keeps that work out of the post, but it does not make the sentence true. The section contradicts `#bets`.
- **Fix.** "For language models, the only evidence in the three sources is circuits in attention-only transformers of two layers or fewer (Elhage et al., outside this post's scope); no source tests bet 1 or bet 3 on a language model, so we hold all three as bets."

### V1-02 · major · "compare lists from two models by dot products" does not follow from the rotation argument
- **Where.** `#answer` l. 371: "Compare lists from two models by dot products, not coordinates, because the stream has no privileged basis". `#work` l. 462: "Compare lists by dot products, not by coordinates: a rotation changes every coordinate and no dot product (section 6)." Audio `answer` l. 130 and `work` l. 189. English item "to rest on the assumption that" (english.json l. 101): "Comparing two models by dot products rests on the assumption that the stream has no privileged basis".
- **Evidence.** The post's own argument (`#dir`, l. 316–317 and l. 335, labelled ours) proves \((Rr)\cdot(Rx)=r\cdot x\): the dot products *within* model A equal those *within* model B = RA. A dot product *across* the models, \(x_A\cdot x_B = x_A\cdot Rx_A\), is not invariant and changes with R. Elhage L158 asserts only that one model's stream can be rotated "by rotating all the matrices interacting with it"; it says nothing about two different models.
- **Problem.** A reader who compares base and instruct models will read "compare lists from two models by dot products" as "take dot products between the two models' vectors". The rotation argument shows that this is the one comparison that does *not* survive a change of basis. The intended point (compare each model's own table of dot products) is not stated, so our reasoning reads as false. "Because the stream has no privileged basis" also overreaches: the no-privileged-basis assertion concerns one model.
- **Fix.** In all four places: "Compare two models through each model's own dot products (for example, the table of dot products between prompts), not through coordinates and not through dot products taken across the two models; a rotation of one model changes every coordinate and every cross-model dot product, but none of that model's own dot products (ours)." In the English sentence: "Comparing two models through their own tables of dot products rests on the assumption that …".

### V1-03 · major · notebook claim: the reason given for the exact 0.0 in the real-stream read split is not supported and does not describe the code
- **Where.** `#rw` l. 250: "The difference is exactly 0.0 because the shares are added in the model’s own order: the toy’s arithmetic, nothing more." Audio `rw` l. 92: the same.
- **Evidence.** results.md row 49: "7.211561 and 7.211561 (difference 0.0)". The row gives no reason. The tautology explanation in row 8 is for notebook 01 rows 2–6 ("the check adds the same float32 tensors in the same order as the model code"). Notebook 02 cell [11] computes `u @ h` (one 768-term dot product of the model's own stream) against `torch.stack([u @ w for w in writes]).sum()` (13 dot products, then a sum). This is a different sequence of float operations, not the model's additions repeated. Row 51 of the same notebook gives −5.72e−6 for the same kind of read-linearity check.
- **Problem.** The post transfers the bit-exact-tautology explanation to a check where it does not apply. results.md does not say why this difference is 0.0 (it may be a rounding coincidence). The lead's rule is that notebook claims say only what results.md supports.
- **Fix.** "The two agree to all printed digits (difference 0.0 in this run). A similar check in the same notebook, u·(x₁ + x₂) against u·x₁ + u·x₂, differs by −5.72e−6: float32 rounding. Either way it is the toy's arithmetic, nothing more." Make the same change in the audio.

### V1-04 · major · recall question 8 relies on another post and on no source
- **Where.** `#recall` l. 482: "In attention, why divide the scores by \(\sqrt{d_k}\)? … Large scores push the softmax into regions with tiny gradients, the authors suspect". Audio `recall` l. 228–230.
- **Evidence.** \(q\), \(k\), \(d_k\), softmax and "attention scores" are defined nowhere in the post. "The authors" are not named. No source in the Sources list covers the question: a grep of all saved sources finds no \(\sqrt{d_k}\) scaling argument. The material is in another AI4Read post (`posts/2026-10-llm-next-word/src/content.html` l. 266–268). WRITING §0: "Never cite or rely on another post"; CHARTER §9: every citation verified against a real source.
- **Problem.** An unsourced claim is attributed to unnamed authors, and the question depends on a post the reader may not have read. Spaced review may repeat earlier material, but the post must still define the terms and cite the source.
- **Fix.** Replace it with a recall question on this post's own material (e.g. "Why is the library's last hidden state not a stream vector?"). Or define q, k, \(d_k\) and softmax in the question and add the attention paper to the Sources list with the section and footnote that say "We suspect" and give the variance argument.

## Minor

### V1-05 · minor · "two circuits": Olah presents three
- **Where.** `#bets` l. 182: "The evidence is two circuits in a vision network". Audio `bets` l. 75: the same.
- **Evidence.** Olah has three circuit sections: L413 "## Circuit 1: Curve Detectors", L457 "## Circuit 2: Oriented Dog Head Detection", L492 "## Circuit 3: Cars in Superposition".
- **Fix.** "The evidence is a few hand-studied circuits in vision networks (curve detectors, dog heads, and a car/dog superposition circuit)."

### V1-06 · minor · Olah L587 is cut before its turn and joined to L547 with "but"
- **Where.** `#bets` l. 186: "The authors suspect it is “likely true”, but “the only evidence we can offer today is anecdotal”". Fold-out l. 211: "Suspects: “likely true”." Audio `bets` l. 77.
- **Evidence.** Olah L587, one sentence: "These results have led us to suspect that the universality hypothesis is likely true, but further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule." The brief, unit 3: "quote both parts together or neither: the second part is the turn." L547 ("Unfortunately, the only evidence we can offer today is anecdotal") is a separate passage that comes 40 lines earlier. WRITING §9: never cut before the turn; never join two passages with "but".
- **Fix.** "They concede that “the only evidence we can offer today is anecdotal” and conclude that they “suspect that the universality hypothesis is likely true, but further work will be needed …” (L587)." Use the full L587 wording in the fold-out too.

### V1-07 · minor · two scope quotes end with a full stop where the source sentence goes on to generalise (balance)
- **Where.** `#bets` trap, l. 189: "“We don’t attempt to apply to our insights to larger models in this first paper.”" and "“mostly a description of how GPT-2 works”". Audio `bets` l. 79.
- **Evidence.** Elhage L102 continues: "…in this first paper, but in a forthcoming paper, we will show that … continues to be at least partially relevant for much larger and more realistic models". Nanda L569 continues: "- there are many variants, but they’re all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM".
- **Problem.** Both authors look narrower than they claim to be. The full stop inside the Elhage quote says the sentence ends there, and it does not.
- **Fix.** Drop the full stop inside the quote and add one clause each: "(they promise a forthcoming paper, not among our sources, on larger models)" and "(he adds that the variants are “all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM”)". The point about Qwen3 and the other current models still stands.

### V1-08 · minor · the coordinate-wise reason is Nanda's, not Elhage's
- **Where.** `#dir` l. 333: "The neurons of an MLP are different, because the MLP’s curve acts on each coordinate separately <cite Elhage 2021, § Activation Properties>".
- **Evidence.** Elhage L850: "A privileged basis occurs when some aspect of a model’s architecture encourages neural network features to align with basis dimensions, for example because of a sparse activation function such as ReLU." Nanda L240: "in the standard basis a ReLU acts on each coordinate independently". "The MLP's curve" is also never defined.
- **Fix.** Cite Nanda 2022, § Representations of Features, for "acts on each coordinate independently". Or keep Elhage and use his words ("encourages features to align with basis dimensions … such as ReLU"). Say "the MLP's activation function (its non-linear curve)".

### V1-09 · minor · wrong section for fine-tuning and RLHF
- **Where.** `#work` l. 466: "The sources define fine-tuning and RLHF only as training procedures … <cite Nanda 2022, § General>".
- **Evidence.** Nanda L905 ("Fine-tuning: …") and L908 ("RLHF …") sit under "## Training" (L881), not "## General" (L85).
- **Fix.** Cite "Nanda 2022, § Training".

### V1-10 · minor · "Libraries do not say “residual stream”" is too broad
- **Where.** `#sum` l. 151.
- **Evidence.** TransformerLens, used in notebook 01, names its hooks `hook_resid_pre`, `hook_resid_mid` and `hook_resid_post` (results.md L5), and the post itself calls it "TransformerLens’s stream" (l. 156).
- **Fix.** "Hugging Face transformers does not say “residual stream” …".

### V1-11 · minor · short answer (a): "independent record" overstates, and the largest relative difference leaves one out
- **Where.** `#answer` l. 370: "The largest relative differences were 7.8e−7 against an independent record of the stream and 1.03e−6 with the writes added in another order." Audio `answer` l. 128.
- **Evidence.** results.md L1: TransformerBridge "returns raw HF weights by default; activations and logits match HF". It is a second library's record of the same Hugging Face modules, not an independent implementation. Row 43: consecutive `hidden_states` differences against the hooked writes give "max rel 6.2e−6", larger than both figures quoted (numbers.md notes that this row was dropped for length).
- **Fix.** "… 7.8e−7 against TransformerLens's record of the stream and 1.03e−6 with the writes added in another order (the differences of consecutive library entries agree with the writes to 6.2e−6, also rounding)." Or drop "largest".

### V1-12 · minor · "Position 0 … is far larger": not after 12 blocks
- **Where.** `#turn` l. 424: "Position 0, the start token, is far larger: 10.3, then 3155.5 after 11 blocks, then 417.4 after 12."
- **Evidence.** results.md row 9 (median, ordinary positions, 12 blocks) 472.4; row 10 (position 0, 12 blocks) 417.4; row 11 ratio 0.88.
- **Fix.** "Position 0, the start token, is far larger at most depths (10.3, then 3155.5 after 11 blocks), but after 12 blocks it is 417.4, slightly below the others." The audio ("and then drops at the end") is fine.

### V1-13 · minor · logit lens: Nanda's "normally" dropped
- **Where.** `#box-lens` l. 353: "As Nanda describes it …, it applies “the final layer norm, and unembed, and log_softmax”."
- **Evidence.** Nanda L1425: "we normally apply the final layer norm, and unembed, and log_softmax, rather than linearizing anything."
- **Fix.** "… it normally applies “the final layer norm, and unembed, and log_softmax”."

### V1-14 · minor · Elhage's plan is reported as a practice
- **Where.** `#lens-linalg` l. 382: "Elhage and colleagues pull apart the streams of communication “in terms of virtual weights, rather than studying it directly”". Audio `lens-linalg` l. 141.
- **Evidence.** Elhage L170: "This is a major reason why we will try to pull apart the different streams of communication … in terms of virtual weights, rather than studying it directly." It is also given as a consequence of the bandwidth problem.
- **Fix.** "Elhage and colleagues say they “will try to pull apart” the streams of communication “in terms of virtual weights, rather than studying it directly”, because the stream is a bottleneck."

### V1-15 · minor · the term box drops the last-entry limit
- **Where.** `#sum` term box, l. 164: "the test above lets us treat the last two as equal in GPT-2 small."
- **Evidence.** The post at l. 159 and results.md rows 42 and 44: the last entry is final-normed (relative difference 0.986).
- **Fix.** "… as equal in GPT-2 small for entries 0 to 11 (the last entry is final-normed)."

### V1-16 · minor · "their evidence is a vision network": Claim 3's evidence spans several
- **Where.** `#answer` l. 372; audio l. 132.
- **Evidence.** Olah L549: "we have observed that a couple low-level features seem to form across a variety of vision model architectures" (L549 names AlexNet, InceptionV1, InceptionV3 and residual networks).
- **Fix.** "… and their evidence comes from vision networks, mostly InceptionV1."

### V1-17 · minor · fold-out quotes without a citation
- **Where.** `#box-firmness` l. 204–205: the "Supposes" and "Proposes and plans" bullets have no cite. The L633 quote ("if you understand a circuit, you should be able to predict …") is cited nowhere in the post.
- **Evidence.** Olah L633, L636–637, § Interpretability as a Natural Science.
- **Fix.** Add the cite "Olah 2020, § Interpretability as a Natural Science" to both bullets.

### V1-18 · minor · Sources: no URL for Elhage, and one notebook number cited only to library code
- **Where.** `#sources` l. 493 (Elhage entry); `#turn` l. 424, item (3), "maximum relative difference 1.09e−6", cited only to "TransformerLens, transformer_bridge.py, 548–560".
- **Evidence.** The saved copy's header: "SOURCE: https://transformer-circuits.pub/2021/framework/index.html". CHARTER §9 asks for a URL or DOI. The 1.09e−6 is results.md row 27 (notebook 01, cell [11]); the TL lines support only the defaults (L2).
- **Fix.** Add the URL to the Elhage entry. Add "Notebook 01, reference run" to item (3).

### V1-19 · minor · audio: small drifts from the page
- **Where and evidence.**
  - Audio `hook` l. 10: "The small model GPT-2 has seven hundred and sixty-eight numbers". The page says GPT-2 small; GPT-2 has larger sizes, and Nanda L611 says "768 in GPT-2 Small".
  - Audio `hook` l. 12: "People do three things with such lists." This drops the page's label "(our summary of common practice)".
  - Audio `bets` l. 73: "a decent amount of empirical evidence for Inceptionv1". Nanda L259 says "that this is mostly true of Inceptionv1"; "mostly true" is the strength being reported.
- **Fix.** Say "GPT-2 small has …". Add "that is our summary of common practice". Say "evidence that this is mostly true of Inceptionv1".

### V1-20 · minor · English pack: "to a first approximation" puts a hedge on an exact sum
- **Where.** english.json l. 31: "To a first approximation, a block adds two vectors to the stream …". Loop, l. 257: "To a first approximation, the residual stream is a running sum".
- **Evidence.** The post (l. 130, l. 158) says the sum is exact bookkeeping, checked to rounding in GPT-2 small. Even in Gemma 3 a block adds two vectors; the vectors are the normed outputs (l. 160).
- **Fix.** Use a true approximate case, e.g. "To a first approximation, a norm before the read is a linear step; only its division is not." Or reword: "Leaving out the norm for now, the residual stream is a running sum …" (the norm acts on the reads, not on the sum, so even this needs care). Simplest: move the expression to the norm fold-out idea.

### V1-21 · minor · English pack: two sentences claim more than the post
- **Where and evidence.**
  - Loop l. 257: "results do not simply carry over to a trained Qwen3 or Llama". The post says only that these models were not run (l. 160). results.md, "What could not be verified" 1: "Expect the structure (rows 54–67) to hold, since it depends on the code, not the weights." The Qwen3, Llama and Mistral code has the same pre-norm pattern (l. 160).
  - english.json l. 203: "Should the additivity check fail, the identity does not hold for that model." The post's condition is "an additivity error above rounding with the hooks placed correctly" (l. 370). In the tiny Gemma 3 the guessed hooks fail and the norm hooks pass (l. 160).
- **Fix.** "… and results may not simply carry over to a trained Qwen3 or Llama, which we did not run." "Should the additivity check fail with the hooks placed correctly, the identity does not hold for that model."

## Checked and found correct

- **Quotes.** Every quotation in content.html (about 110 strings) was matched by script against the saved `.txt` sources, whitespace-collapsed and then letters-and-digits only. All were found. None is over 25 words. None comes from the hidden Olah lines (L147–148, 249–254, 265, 267, 287, 455, 658) or hidden Elhage L303. Section attributions were checked against the `##` headings; all are right except V1-08 and V1-09. Referents checked: Olah L232 "this" (understandable features), Nanda L288 "this" (neuron superposition being harder), Nanda L1365 (zero ablation), Elhage L170 "somehow communicating in superposition!" (the hypothetical 50-layer stream; the post's "picture" keeps it hypothetical).
- **Writer-must-not-use list.** Items 1–15 are not used: no hidden Olah text; no "not necessarily a unit vector"; L216 not used; L259 quoted in full; no skip-connection tension; L155 hedge not needed; no excluded Elhage lines (L181, L417, L535–536, L568, L226); no out-of-scope Elhage sections; no quoted paraphrases; no damaged lines; no firmness upgrades (no privileged basis is "asserted, for an idealised linear stream"; L242 keeps "led us to believe"; Nanda L287 keeps "as an intuition"); W9-B is "like an edge weight (ours)", not an Olah edge; no "bandwidth vs Shannon" contrast.
- **Elhage scope.** Every Elhage citation is in High-Level Architecture, Communication Channel, Virtual Weights, Subspaces and Residual Stream Bandwidth, Activation Properties, or the limit statements (L98, L102, L142). Virtual weights appear only through L170.
- **Steering.** No sentence claims a behavioural effect. "Steering" and "activation addition" are stated to be absent from the sources (confirmed by grep). The notebook result is called "arithmetic, not behaviour".
- **Notebook numbers** (results.md rows): 768/12 (row 9 config, Nanda L611, L625); 2,048 (cell [13] config); 0.0 tautology with the row 8 explanation (rows 2–6); 4.27e−4 / 1.03e−6 and epsilon 1.19e−7 (row 7); 4.88e−4 / 7.8e−7 (row 23); last entry 0.0 vs 0.986 (rows 44–45); index convention (rows 41, L10–L12); Gemma 3 9.7 vs 0.0 and √d scaling (rows 56, 58–60, L17–L18); Qwen3, Llama and Mistral line numbers (L15, L19); 7.211561 and 13 shares (row 49); steering 0 for all five α (row 50, cell [12] output checked); cosine 0.1318 vs 1.0935 (row 53); norm profile (rows 9–10); logit-lens 0.0 / 834.6 and ranks (rows 13–14, 17, 20); compatibility mode 1.09e−6 (row 27); environment versions (results.md header). Full-size Qwen3, Llama, Gemma and Mistral are correctly reported as not run, everywhere they are mentioned.
- **Toy numbers**, rerun in Python: the running sum; shares 5, 0, 1, −1 and the edge case 2, −1, 1, −2; cancellation; the cloud, u, ±1.414, the margin table (−4, −2.828, 0, 2, 2.828 under the post's stated definition), the blind probe at 45°; steering 0.586 / 3.414 and the sideways push; E1–E5; rotation shares at 45°, 90° and 180°; norm toy (−1, −1, 8, 16); logit-lens toy rows; three-feature reads (1, −0.5, −0.5; all three on gives 0); the open-question matrix. `check.mjs`: 7/7 widget configs OK, and the readouts match the text. Presets (best and blind probe, push along and sideways, rotations, three features) were recomputed by hand and match.
- **MacKay.** Exercise 15.18 on p. 237: all quotes verbatim. Described as an exercise set-up, with no capacity or theorem claim. "No noise" and "cannot hear the output" kept. The link is labelled a structural analogy (ours), and the disanalogies are stated.
- **Standalone and Discipline.** Apart from V1-04, the post mentions and relies on no other AI4Read post ("↻ will come back in later posts" names none). No Discipline data, models, prompts or results appear. The base/instruct point is an untested working assumption.
- **"Ours" labels.** Present on the bank-balance picture, the bus trap, the unit-length convention, "like an edge weight", seeing versus doing, cashing in bet 3, the MacKay link, the three-feature toy, the open-question matrix, and the short answer as a whole.
- **English pack.** Apart from V1-02, V1-20 and V1-21, the example sentences restate the post (bear out, pin down, face value, case in point, hold up, at pains to, fall out of, matter of convention, firm ground, in lockstep, hinge on, tantamount to, the patterns, the fixes and the tips) and add no claims.

## Counts

- Critical: 0
- Major: 4 (V1-01, V1-02, V1-03, V1-04)
- Minor: 17 (V1-05 to V1-21)
