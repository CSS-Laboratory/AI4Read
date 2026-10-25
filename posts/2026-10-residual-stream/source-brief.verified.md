---
id: 2026-10-residual-stream/source-brief.verified
type: source-brief
stage: S2
verified: 2026-10-25
verified_by: independent S2 fact-checker (fresh agent; did not write the S1 brief)
verified_from: posts/2026-10-residual-stream/source-brief.md (S1, unchanged on disk)
method: >-
  (1) All 164 labelled quotes Q[...] re-matched by script against the cited .txt line span,
  twice: whitespace-collapsed exact substring, and letters-and-digits only (NFKC, lowercased);
  word counts recomputed (split on whitespace). Result 164/164 found in span, counts right, none over 25 words.
  (2) Every quote and every quoted fragment in claim, trap and tension lines (611 fragments) re-matched
  against the VISIBLE text of the saved .html (HTML comments, scripts and styles removed), to catch text
  that is in the file but not on the published page. Result: 3 Olah quotes are hidden (unit 1).
  (3) Every cited line and section read in the .txt (and the .html where the text layer is damaged);
  claims, numbers, hedges and referents compared by hand; quoted fragments not found verbatim listed.
  (4) Every toy number recomputed with numpy. All match.
  (5) Every absence claim (UNSEEN, "nowhere", "only") re-searched with grep over all three .txt files.
  (6) Every Elhage citation mapped to its section heading and compared with Kunhao's scope (kunhao-input.md).
s2_result: "14/14 units checked, 0 unchecked. Tags: 0 OK, 14 FIXED, 0 DROP (items inside units dropped and marked). UNSEEN block re-searched. 10 topic-card notes checked. Findings 1 critical, 9 major, 24 minor: see review/s2-check.md."
post: "What Is a Hidden State? The Residual Stream, Read and Written"
post_number: 03
lenses: [linear-algebra, information-theory]
built_from:
  - posts/2026-10-residual-stream/sources/olah-2020-zoom-in.txt
  - posts/2026-10-residual-stream/sources/elhage-2021-framework.txt
  - posts/2026-10-residual-stream/sources/nanda-2022-glossary.txt
  - (checked against the .html copies only where the .txt layer was unclear: olah-2020-zoom-in.html, nanda-2022-glossary.html)
  - (inputs read for scope, not as sources: topic-card.md, kunhao-input.md)
date: 2026-10-25
grounding: Every unit was read in the saved copy (status SEEN). No digest, no memory. Anything not visible in those files is UNSEEN. The original logit-lens post is not saved and is a gap, not a source. The technical flags T1-T14 of the topic card are not source facts; they are listed at the end.
---

# Source brief: "What Is a Hidden State? The Residual Stream, Read and Written"

**Citations and the page/line-offset note.**
- All three sources are web pages, so there are no page numbers. A location is the **section heading as it appears in the saved page** plus **L = the line number in the saved `.txt`** (1-based; lines 1-2 are the SOURCE and ACCESSED header). Line numbers here match the topic card's.
- **Footnotes are inlined** into the paragraph at their anchor with no separator (Elhage L155, L157-158, L162, L166-172; Olah L174-184, L474, L510). **S2:** Olah L174-184 is the Schwann figure and its caption, not footnotes; Olah's inlined footnotes are at L474 and L510. A sentence can therefore be split by a footnote, so a quote that spans the footnote is not given; the parts on either side are quoted separately and labelled.
- **Quotes are verbatim and machine-checked** against the `.txt` (substring match after collapsing whitespace) on 2026-10-25. **S2 re-check:** 164/164 labelled quotes found in their cited span (exact after whitespace collapse, and letters-and-digits only); all word counts right; none over 25 words. Three of them are not on the published page (unit 1). Curly quotes and apostrophes are kept as in the source (Olah and Nanda use "“ ” ’"; Elhage mixes straight and curly). A quote label `Q[source:Lstart-Lend, N w]` gives the lines and the word count (at most 25).
- **The text layer drops figures, inline code and some math.** Known gaps, all confirmed in the `.html` too: Nanda L207 and L257 (sentences cut off mid-way), L1391 and L1410 and L1417 (a formula missing: "The logits of a model are ."), L1424 (the logit-lens entry is corrupted), L1383 (the name of the TransformerLens fold flag is missing). Olah's glossary formula at L669 reads "n1Wn2T" in the text; the HTML shows it is n&#8321; W n&#8322;&#7511; (n-one, W, n-two transposed). **S2:** the HTML writes it with tags, `<i>n<sub>1</sub>Wn<sub>2</sub><sup>T</sup></i>`, not character entities; the reading n₁ W n₂ᵀ is right. More damaged Nanda lines, the same in text and HTML: L626 ("2L Transformer is equivalent to"), L833, L854 (cut off), L955 ("can be thought of ."), L1167 ("a linear map () ... (size )"), L1172 ("($$$$ is elementwise multiplication)"), and L1383 lacks two names, not one ("If the flag is True in or (defaults to True)"). Elhage's equations appear as raw LaTeX.
- Leftover HTML comment marks ("-->") sit in the Olah text at L30, L69, L77, L107, L150, L255, L269, L285, L287 and others; ignore them.
- **S2 (critical, see unit 1): do not ignore them.** A "-->" can close an HTML comment whose text is in the file but **not rendered on the published page**. After removing `<!-- -->` blocks from the saved HTML, these Olah text-layer lines are not on the page: **L147-148, L249-254, L265, L267, L287, L455, L658**. Elhage L303 is likewise hidden; no Nanda line is. Never cite a hidden line.
- Hedges are copied from the sources: keep them. "Ours" marks our own reasoning or toy numbers.

**Status tags.** SEEN = read in the saved copy. UNSEEN = not visible in the saved copies (listed at the end).

**Firmness verbs (WRITING section 9).** *asserts* = no hedge; *predicts* = forecast, no hedge; *imagines / supposes / asks* = hedged; *concedes / proposes* = own limits and remedies. Olah's three claims are *offered as deliberately speculative claims* (L220); in the units below each of their lines is sorted by firmness.

## Traps for the whole post [FIXED]
1. **Three vintages, three scopes.** Olah et al. (2020): a vision network, InceptionV1 (L258). Elhage et al. (2021): attention-only transformers with two layers or fewer, no biases, layer norm ignored, larger models not attempted (L98, L102, L140-142). Nanda (2022): a personal, opinionated glossary, "mostly a description of how GPT-2 works" (L569). None of them says anything about Qwen3, Llama 3, Gemma 3 or Mistral, about base versus instruct models, or about post-training effects on representations.
2. **"Hidden state" is not in any source.** "hidden state" and "hidden_state" occur nowhere. Two near-misses: Nanda L612 lists `hidden_size` as an alias of `d_model` (the width of the residual stream), and Nanda L405 uses "hidden layer" for the *internal activations of an MLP*, which is a different object. **S2:** more near-misses: Olah L538 ("they learn similar representations at hidden layers"), Nanda L415 ("the part of an MLP hidden layer"), Nanda L723 ("one hidden layer network"). The conclusion stands. The post cannot cite a source for "hidden state = residual stream"; it needs the notebooks (T1-T5).
3. **Four meanings of "embedding".** (a) Elhage: the residual stream vectors "are often called the embedding" (L155, L893). (b) Nanda: the first layer, a lookup table giving the starting vector of the stream (L667). (c) Nanda: "Writing is an embedding" (L1002), meaning a low-rank subspace placed into the big space. (d) Nanda L586: "embedded tokens plus the positional embedding". Reserve "embedding" for the first vector x0 (our choice) and say "stream" elsewhere.
4. **Two meanings of "layer".** Nanda: "a transformer layer actually contains two layers, an attention layer and an MLP layer" (L577), and his `n_layers` counts blocks (L625); his L579 "after layer n" is not tied to either. Elhage x^n is "at layer n" (L893) with "residual block" = attention layer + MLP layer (L148). The post says "after k blocks" (ours).
5. **Three senses of "projection"**: a linear map into a smaller space (Elhage L148), the number x.v for a fixed v (Nanda L1415), and the closest point on a line (not used by any source here). **S2:** narrow this: Nanda's PCA entry (L1551) does remove "the component in the $$v$$ direction" (formula printed malformed, x -> x - (x.v)/|v|). No source uses the closest-point sense for the residual stream. See units 6, 11.
6. **"Circuit" and "superposition" are not the electrical and signal-processing words.** Olah L205-207 defines circuit as a subgraph of features and weighted edges; Nanda L377 as a computational subgraph whose nodes are components. Olah L508 and Nanda L269 mean packing more features than dimensions.
7. **The corrupted logit-lens entry.** Nanda L1424 is unreadable after "layer $k"; quote only the intact lines L1425-1432 and treat the original as a gap (unit 13).
8. **The sources disagree about firmness, even inside one source.** Nanda calls "features as directions" a hypothesis (L199) but states "Features are the fundamental building block of models" flat (L135) and says "What token is this" and "what position is this in" "are represented as separate directions in the residual stream" with no hedge (L1096). Olah offers the same idea as a "deliberately speculative" claim. Report each at its own firmness.
9. **Toy numbers are ours.** W9 (stream of width 2, six points) is a teaching toy; it shows what a statement means, not that a language model behaves that way.

---

## A. Olah et al. (2020), "Zoom In: An Introduction to Circuits" (Distill) [SEEN]

### 1. [FIXED] Claim 1, "Features": features are directions
**Where.** § Three Speculative Claims, L188-198 (the claim box) and L220-224 (the status of the claims); § Claim 1: Features, L226-269; Glossary, "Direction" L678-679, "Feature" L693-694, "Representation" L710-711.

**Claim, sorted by firmness.**
- *Strongest unhedged wording (in the claim box):* the claim itself, and "These features can be rigorously studied and understood." (L200). The box has no hedge inside it.
- *Hedges that surround it:* the three claims are "deliberately speculative" (L220); they are "both" empirical claims and "normative claims about how it's useful to understand them" (L186); "if true" they could found a new field (L223-224); "The community is divided on whether this is true" (L232); ~~part of the claim is "trivially true" (L265);~~ **S2: DROP — L265 is inside an HTML comment, not on the published page;** the evidence is from InceptionV1 and the authors "believe" it holds generally (L258-259).
- *What "direction" means here:* "a linear combination of neurons in a layer" (L194; again L679, with "Equivalently, a vector in the representation of a layer"). The page gives no unit-length or sign convention.
- *What the evidence supports:* (S2: keep the lead-in "have led us to believe", L242) "the typical case is that neurons (or in some cases, other directions ...) are understandable" (L242). The detailed evidence (seven arguments, L293-339) is about **curve detectors**, which are single neurons. For higher-level features some of the tests "become a lot of effort" (L374).
- *Verbs for the post:* Olah et al. **offer** Claim 1 as a speculative claim; they **believe** the typical case is understandable neurons; they **concede** the community is divided ~~and that part of the claim is trivially true~~ (S2: dropped, hidden text). S2 balance: the strongest unhedged evidence line is L273, "Curve detecting neurons can be found in every non-trivial vision model we’ve carefully examined."

**Quotes (verbatim, at most 25 words).**
- Q[olah:192-193, 12w]: "Features are the fundamental unit of neural networks. They correspond to directions."
- Q[olah:194, 12w]: "By “direction” we mean a linear combination of neurons in a layer."
- Q[olah:200, 8w]: "These features can be rigorously studied and understood."
- Q[olah:186, 25w]: "They are intended both as empirical claims about the nature of neural networks, and also as normative claims about how it’s useful to understand them."
- Q[olah:220, 5w]: "These claims are deliberately speculative."
- Q[olah:223-224, 15w]: "if true, they could form the basis of a new “zoomed in” field of interpretability"
- Q[olah:232, 9w]: "The community is divided on whether this is true."
- Q[olah:242, 21w]: "the typical case is that neurons (or in some cases, other directions in the vector space of neuron activations) are understandable"
  - **S2 [FIXED]:** quoted alone this drops the belief verb. Report it as "have led us to believe the typical case is that neurons ... are understandable" (L242), or keep "believe" in the reporting sentence.
- ~~Q[olah:265, 7w]: "Part of this claim is trivially true."~~ **S2: DROP** (commented out of the published HTML).
- ~~Q[olah:265, 18w]: "The interesting part of the claim is that they can, with sufficient effort, be rigorously studied and understood."~~ **S2: DROP** (same).
- **S2 replacement (visible):** Q[olah:229, 11w]: "They correspond to directions. They can be rigorously studied and understood."
- **S2 addition (balance):** Q[olah:273, 14w]: "Curve detecting neurons can be found in every non-trivial vision model we’ve carefully examined."
- Q[olah:258-259, 15w]: "We will take our examples from InceptionV1 for now, but believe these claims hold generally"
- Q[olah:694, 19w]: "A scalar function of the input. In this essay, neural network features are directions, and often simply individual neurons."
- ~~Q[olah:252, 15w]: "For us, the way out of the curse of dimensionality is features being individually understandable."~~ **S2: DROP** (L249-254 are commented out of the published HTML).

**Numbers and equations.** No equation. In symbols (ours, restating L194): a direction is v = c1 n1 + c2 n2 + ... + ck nk, a weighted sum of the k neurons n of one layer. Evidence counts: seven arguments for curve detectors (L293); curve detectors in layer mixed3b with a radius "of around 60 pixels" (L276); "thousands of hours of studying individual neurons" (L242).

**Traps.**
- "Direction" here is a vision-layer notion defined on neurons; the residual stream has no neurons (unit 8). Writing "Olah shows that concepts are directions in a language model's stream" is wrong twice: scope and firmness.
- ~~The claim has a trivially true part (directions include single neurons, L265) and an interesting part (they can be rigorously studied). Only the second part is a bet.~~ **S2: DROP** (rests on hidden L265). Visible support for "directions include single neurons": glossary L679, "A direction can be an individual neuron (which is a basis direction of the vector space)".
- Olah's glossary "feature" is "a scalar function of the input" (L694); Nanda's is "a property of an input to the model" (L104). Different words, not the same definition.
- The strong evidence statement ("we think the evidence is quite strong", L291) is about curve detectors, not features in general.
- Do not add "unit length" or "up to sign" to Olah's definition. That is our usage (topic card section 4) and must be labelled so.

**Tensions.** ~~Nanda L254-259: "features as neurons" is "at best only slightly true for transformers" (he is answering exactly this kind of claim).~~ **S2 [FIXED, major]:** Nanda L259 in full: "There is a decent amount of empirical evidence that this is mostly true of Inceptionv1, but this seems at best only slightly true for transformers." He agrees for the vision model and doubts transformers; "he is answering this claim" is our inference, drop it. Elhage L793: MLP neurons in transformers were "much harder to develop hypotheses for" in practice (S2: § Additional Intuition, MLP Layers, outside Kunhao's Elhage scope; use only if he widens it). Elhage L852: it "doesn't really make sense" to look at neurons of the residual stream. Nanda L135 states "features are the fundamental building block" flat, where Olah hedges.

**Toy idea (W9-C).** The calm points (3,1), (4,2), (5,3) and the urgent points (1,3), (2,4), (3,5) overlap at 3 along either coordinate axis, so no single coordinate reads the group. Along u = (-1, 1)/sqrt2, which is -x/sqrt2 + y/sqrt2, a linear combination of the two coordinates, every calm point scores -1.414 and every urgent point +1.414 (checked by code). That is L194's definition of a direction in the smallest case. The blind direction at 45 degrees (identical score sets) shows a direction can also hide the group. Call the axes "coordinates", not "neurons" (Nanda L736). Toy numbers, ours; nothing here says a language model stores "calm" this way.

### 2. [FIXED] Claim 2, "Circuits": features are connected by weights
**Where.** § Three Speculative Claims, L202-211; § Claim 2: Circuits, L400-410; Circuit 1 L413-455; Circuit 2 L457-490; § Interpretability as a Natural Science L606-637; Glossary, "Circuit" L667-669.

**Claim, sorted by firmness.**
- *Strongest unhedged wording:* "Features are connected by weights, forming circuits." (L204); "These circuits can also be rigorously studied and understood." (L211); and, in the body, "You can literally read meaningful algorithms off of the weights." (L409).
- *Hedges:* "deliberately speculative" (L220); L409 is preceded by "how tractable and meaningful these circuits **seem** to be"; many "smaller weights we don't understand the role of" remain in the curve circuit (L320); the test by editing weights is a plan, not a result: "we plan to return to it ... including testing our theory of the circuit by editing the weights" (L490); circuits are "much smaller in scope than overall model behavior" (L635).
- *The sentence nearest to "behaviours are circuits"* is hedged three ways: "it seems like, with sufficient effort, statements about model behavior could be broken down into statements about circuits" (L636), then "If so, perhaps circuits could act as a kind of epistemic foundation" (L637).
- *S2 balance:* add the unhedged L634, "In fact, for small enough circuits, statements about their behavior become questions of mathematical reasoning."
- *Verbs:* they **offer** the claim as speculative; they **find** that circuits "seem" tractable; they **propose** that edit-prediction is the test (L633); they **suppose** that behaviour could be broken into circuits.

**Quotes.**
- Q[olah:204, 7w]: "Features are connected by weights, forming circuits."
- Q[olah:205, 10w]: "A “circuit” is a computational subgraph of a neural network."
- Q[olah:211, 9w]: "These circuits can also be rigorously studied and understood."
- Q[olah:409, 17w]: "The remarkable thing is how tractable and meaningful these circuits seem to be as objects of study."
- Q[olah:409, 10w]: "You can literally read meaningful algorithms off of the weights."
- Q[olah:208, 22w]: "Often, we study quite small circuits — say with less than a dozen features — but they can also be much larger."
- Q[olah:426, 22w]: "We think it’s often useful to view this as a single low-rank weight matrix, but this technically does ignore one ReLU non-linearity."
- Q[olah:320, 12w]: "although there are many smaller weights we don’t understand the role of"
- Q[olah:490, 11w]: "including testing our theory of the circuit by editing the weights"
- Q[olah:633, 25w]: "They’re very much falsifiable: for example, if you understand a circuit, you should be able to predict what will change if you edit the weights."
- Q[olah:636, 19w]: "But it seems like, with sufficient effort, statements about model behavior could be broken down into statements about circuits."
- Q[olah:637, 14w]: "If so, perhaps circuits could act as a kind of epistemic foundation for interpretability."
- Q[olah:668, 16w]: "A subgraph of a neural network. Nodes correspond to neurons or directions (linear combinations of neurons)."

**Numbers and equations.** Edge weight in the glossary (L669): "n1Wn2T" if the nodes are linear combinations, i.e. n1 W n2-transposed for directions n1, n2 (HTML). A 5x5 convolution gives a 5x5 weight set per pair (L425). Curve circuit spans two layers; the dog-head circuit spans four (L459), with "three layers" of mirrored pathways (L463). Circuits of "less than a dozen features" (L208).

**Traps.**
- A circuit is built from *already identified features* (L409: "once you understand what features they're connecting together"). Identify the features first, then read the weights.
- The worked evidence is curve detection and dog-head detection in a vision model. Olah gives no example of a behaviour such as refusal, trust or expertise; the sentence at L636 is the closest and is a hope.
- The "edit the weights" test is stated as a standard (L633). In the saved text no such test is reported; L490 says it is planned.
- "Circuit" has a different definition in Nanda (nodes are components, unit 12 tensions) and the wiki node is mostly electrical (T12).
- The weights shown multiply out a 1x1 and a larger convolution and "technically ignore one ReLU" (L426): even the vision circuits are an approximation. **S2:** not verbatim; the source says "this technically does ignore one ReLU non-linearity" (L426).

**Tensions.** Nanda L136: "Circuit is also a fairly fuzzy and poorly defined term." Nanda L377-387 (credited to Redwood Research): nodes are heads and neurons, edges are the part of a later node's input that comes from an earlier node's output; attention heads are "larger than neurons" and are not features. Elhage L98 limits its circuit results to attention-only models of two layers or fewer.

**Toy idea (W9-B).** Treat each writer's output and the reader's input vector r = (1, 2) as an "edge": the weight from writer to reader is their dot product. x0: 5; a1 = (2,-1): 0; f1 = (-1,1): 1; a2 = (3,-2): -1; total 5, checked by code. The edge from a1 to r is zero, so r "does not hear" a1. This is the same shape as Olah's n1 W n2^T for directions (a number for each pair), in its smallest case. Ours; it illustrates the *form* of a weighted edge, not any claim about real circuits. **S2:** Olah's glossary edges join nodes "in adjacent layers" (L669); W9-B links x0 and block-1 writers to a block-2 reader through the stream, which Olah's definition does not cover. Say "like an edge weight", not "an Olah edge".

### 3. [FIXED] Claim 3, "Universality": analogous features and circuits form across models and tasks
**Where.** § Three Speculative Claims, L213-215; § Claim 3: Universality, L527-604; Glossary, "Universal Feature" L707-708; references on convergent learning and representation similarity, L536-539, L780-782.

**Claim, sorted by firmness.**
- *Strongest unhedged wording:* the claim box (L215): "Analogous features and circuits form across models and tasks." No hedge inside the box.
- *Hedges:* "deliberately speculative" (L220). The authors say prior work "seems highly suggestive, but there are alternative explanations" (L540). Their own evidence is "only ... anecdotal" (L547), they "have not yet invested enough in the comparative study" (L548), and from "a couple low-level features" (L549) they "suspect that the universality hypothesis is likely true, but further work will be needed" (L587). They add that, unlike Claims 1 and 2, universality "wouldn't be completely fatal to circuits research if this claim turned out to be false" (L602), and distinguish a strong form ("periodic table of visual features"), "in between worlds", and "mostly false" (L604).
- *Verbs:* they **offer** the claim as speculative; they **suspect** it is likely true; they **concede** the evidence is anecdotal.

**Quotes.**
- Q[olah:215, 9w]: "Analogous features and circuits form across models and tasks."
- Q[olah:531, 20w]: "It’s a widely accepted fact that the first layer of vision models trained on natural images will learn Gabor filters."
- Q[olah:540, 14w]: "This work seems highly suggestive, but there are alternative explanations to analogous features forming."
- Q[olah:547, 10w]: "Unfortunately, the only evidence we can offer today is anecdotal"
- Q[olah:549, 18w]: "we have observed that a couple low-level features seem to form across a variety of vision model architectures"
- Q[olah:587, 14w]: "These results have led us to suspect that the universality hypothesis is likely true,"
- Q[olah:587, 22w]: "further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule"
- Q[olah:602, 21w]: "Unlike the first two claims, it wouldn’t be completely fatal to circuits research if this claim turned out to be false."
- Q[olah:604, 19w]: "If it was true in the strongest sense, one could imagine a kind of “periodic table of visual features”"

(The two L587 quotes are one sentence; quote both parts together or neither: the second part is the turn.)

**Numbers and equations.** None. The evidence is two feature families (curve detectors, high-low frequency detectors) shown under four model headings each (AlexNet, InceptionV1, VGG19, ResNetV2-50; headings only, L551-585).

**Traps.**
- The text at L549 names "AlexNet, InceptionV1, InceptionV3, and residual networks", but the figure headings (L553-585) name AlexNet, InceptionV1, VGG19 and ResNetV2-50. The figures themselves are not in the text layer (UNSEEN), so do not list architectures beyond what L549 says.
- "Universality" is about *different models or tasks*. Olah says nothing here (nor anywhere in the saved text) about one model before and after fine-tuning; the words fine-tuning, post-training and RLHF do not occur.
- The "convergent learning" and "representation similarity" work is cited by title only (L536-539; references L780-782 include SVCCA and "Similarity of neural network representations revisited"); its content is UNSEEN. **S2 [FIXED]:** not "by title only": Olah gives a one-line summary, "different neural networks can develop highly correlated neurons" (L536) and "they learn similar representations at hidden layers" (L538), then judges it "highly suggestive" with "alternative explanations" (L540). The papers' own content is UNSEEN. "Representation similarity" is our phrase, not the source's.
- Claim 3 is the only one flagged as non-fatal if false (L602). Do not rank the three claims as equally supported.
- **S2 balance:** Olah's strongest unhedged evidence line is L273, "Curve detecting neurons can be found in every non-trivial vision model we’ve carefully examined." Report it next to "only ... anecdotal" (L547).

**Tensions.** Nanda L156-159 defines universality as a hypothesis about *circuits* and calls the bolder version "(and IMO probably false)". ~~Elhage L568 reports "analogous attention heads and circuits in large models" but defers the evidence to a forthcoming paper (UNSEEN here).~~ **S2: DROP (scope, major).** L568 is about induction heads in large models (§ Where Does This Leave Us?), which Kunhao excluded.

**Toy idea (W9, E5).** Make "model B" model A with every vector rotated by 90 degrees, (x, y) -> (-y, x), including r. Coordinates differ, but the four read-shares (5, 0, 1, -1) are unchanged, and the best probe direction rotates with the points: calm (3,1) -> (-1,3), and u = (-1,1)/sqrt2 -> (-1,-1)/sqrt2, score still -1.414. So "analogous" can only mean "the same up to a rotation of the stream", never "the same coordinates". Ours; this is a reason to compare dot products, not a result about real models.

### 4. [FIXED] Polysemantic neurons and superposition (the vision-network version)
**Where.** § Polysemantic Neurons, L377-398; § Circuit 3: Cars in Superposition, L492-510 (footnote inline at L510); Glossary, "Polysemantic Feature" L699-702, "Pure Feature" L704-705.

**Claim, sorted by firmness.**
- *Asserted:* "Neural networks often contain 'polysemantic neurons'" (L382, with the example neuron 4e:55: cat faces, fronts of cars, cat legs, L383-385); they are "a major challenge for the circuits agenda" (L391); "five" meanings times "five" meanings gives "25 connections" (L392); in Circuit 3 "the model had a 'pure neuron' and then mixed it up with other features" (L506); "We call this phenomenon superposition." (L508).
- *Hedged:* polysemantic neurons "seem to result from" superposition, "presumably to pack more features into the limited number of neurons" (L398); the circuit "suggests ... in some sense, deliberate" (L506); "We believe superposition allows the model to use fewer neurons" (L510); resolution is a hope: "perhaps by 'unfolding' a network" (L393-394).
- *Condition that the explanation needs:* "As long as cars and dogs don't co-occur" (L510).
- *The geometry footnote* (L510) is a one-line aside with no proof.

**Quotes.**
- Q[olah:382, 12w]: "Neural networks often contain “polysemantic neurons” that respond to multiple unrelated inputs."
- Q[olah:391, 21w]: "Despite this, polysemantic neurons are a major challenge for the circuits agenda, significantly limiting our ability to reason about neural networks."
- Q[olah:392, 24w]: "If one neuron with five different meanings connects to another neuron with five different meanings, that’s effectively 25 connections that can’t be considered individually."
- Q[olah:398, 10w]: "they seem to result from a phenomenon we call “superposition”"
- Q[olah:398, 14w]: "presumably to pack more features into the limited number of neurons it has available"
- Q[olah:506, 11w]: "This circuit suggests that polysemantic neurons are, in some sense, deliberate."
- Q[olah:510, 16w]: "We believe superposition allows the model to use fewer neurons, conserving them for more important tasks."
- Q[olah:510, 20w]: "As long as cars and dogs don’t co-occur, the model can accurately retrieve the dog feature in a later layer"
- Q[olah:510, 13w]: "which only allow for n orthogonal vectors, but exponentially many almost orthogonal vectors"

**Numbers and equations.** 5 x 5 = 25 connections (L392, checked). n orthogonal vectors versus "exponentially many almost orthogonal vectors" (footnote, L510; no formula in the page). No other numbers.

**Traps.**
- A polysemantic neuron is defined relative to the **neuron basis** (L700). **S2 [FIXED]:** L700 defines a polysemantic *feature* ("responds to multiple unrelated latent variables, such as the cat/car neuron"); it does not mention a basis. Olah's examples are neurons (L382). "Relative to the neuron basis" is our reading; label it so. Nanda L299 says polysemanticity "isn't used to refer to bottleneck dimensions, because there's no privileged basis to be polysemantic in". The residual stream therefore has no polysemantic neurons; the stream-level question is Nanda's "bottleneck dimension superposition" (unit 7).
- Olah's explanation is conditional on features not co-occurring (L510). Keep the condition.
- Olah's own Claim 1 notes that other directions are more useful "especially when neurons are 'polysemantic'" (L196-197): superposition is the reason the "direction, not neuron" wording exists. **S2:** ours; L196-197 names polysemantic neurons, not superposition, and gives no reason for the wording.
- The geometric footnote is not a derived result here. Per the card, the post poses it and does not use it as a result.

**Tensions.** Nanda L269-276: with superposition there "cannot be an interpretable basis", and reading features by projection means they "cannot all be orthogonal, so we cannot perfectly recover each feature". Nanda L309: "problems with many sparse, unimportant features will show significant superposition" (sparsity, a condition Olah shares with "don't co-occur").

**Toy idea (extends W9; ours).** Three features written along three directions at 0, 120 and 240 degrees in the 2-D stream. A stream that carries only feature 1 with strength 1 reads (1.000, -0.500, -0.500) on the three directions (checked by code): the other two readers hear interference although nothing was written for them. Two features can be orthogonal in 2-D; three cannot. This is the *question* for a later post, not an answer; the sources here give no capacity number.

---

## B. Elhage et al. (2021), "A Mathematical Framework for Transformer Circuits" (Transformer Circuits Thread) [SEEN]
Scope set by Kunhao: only the residual stream, virtual weights and no privileged basis; the attention-head algebra and induction heads are not used. Unit 9 reaches into the appendix on layer normalization because the topic card (section 11) asks for it as a fold-out; drop it if the fold-out is dropped.

### 5. [FIXED] The stream is a sum, and a "communication channel"
**Where.** § High-Level Architecture, L146-148; § Virtual Weights and the Residual Stream as a Communication Channel, L150-158 (the stream passage is L155); § Summary of Results, Conceptual Take-Aways, L120, L126; § Model Simplifications, L138-142; Notation, L893; scope statements at L95-102 and L564-572.

**Claim, sorted by firmness.**
- *Asserts (definition and framing):* "The residual stream is simply the sum of the output of all the previous layers and the original embedding." (L155). Layers "read" and "write" (L148). They "generally think of the residual stream as a communication channel, since it doesn't do any processing itself" (L155). All components "communicate with each other by reading and writing to different subspaces of the residual stream" (L126).
- *Hedged or belief:* they "prefer" the stream wording because it emphasises "the residual nature (which we believe to be important)"; and "we believe the residual stream often dedicates subspaces to tokens other than the present token" (L155).
- *Own limits (concedes):* (S2 addition) they "attempt to take initial, very preliminary steps towards reverse-engineering transformers" (L98); the paper studies "transformers with two layers or less which have only attention blocks" (L98); "We don't attempt to apply to our insights to larger models in this first paper" (L102); the MLP portions "have been much harder to get traction on" (L140); "we can probably only understand a small portion of large language models this way" (L570). They also **avoid** the stream as an object: "our decision to avoid directly investigating the residual stream" (L635).
- *Their stated aim (L95):* to reverse engineer transformers "similar to how a programmer might try to reverse engineer complicated binaries".

**Quotes.**
- Q[elhage:155, 19w]: "The residual stream is simply the sum of the output of all the previous layers and the original embedding."
- Q[elhage:155, 24w]: "We generally think of the residual stream as a communication channel, since it doesn't do any processing itself and all layers communicate through it."
- Q[elhage:155, 11w]: "In transformers, the residual stream vectors are often called the “embedding.”"
- Q[elhage:155, 20w]: "the residual stream often dedicates subspaces to tokens other than the present token, breaking the intuitions the embedding terminology suggests"
- Q[elhage:148, 12w]: "“read” their input from the residual stream (by performing a linear projection)"
- Q[elhage:148, 14w]: "“write” their result to the residual stream by adding a linear projection back in"
- Q[elhage:126, 15w]: "communicate with each other by reading and writing to different subspaces of the residual stream"
- Q[elhage:98, 17w]: "in this paper we will study transformers with two layers or less which have only attention blocks"
- Q[elhage:102, 15w]: "We don’t attempt to apply to our insights to larger models in this first paper"
- Q[elhage:102, 14w]: "continues to be at least partially relevant for much larger and more realistic models"
- Q[elhage:95, 16w]: "similar to how a programmer might try to reverse engineer complicated binaries into human-readable source code"
- Q[elhage:570, 14w]: "we can probably only understand a small portion of large language models this way"
- Q[elhage:635, 9w]: "our decision to avoid directly investigating the residual stream"

(L102: the limit and the hope are in one sentence; the second quote carries the hopeful half. Both are about a forthcoming paper that is not in the saved sources.)

**Numbers and equations.** In words: x_final = x_embedding + sum of all earlier writes (ours, restating L155; the page gives it in words only). Notation: "x^n ... 'Residual stream' or 'embedding' vectors of model at layer n (one vector per context token) [activation, not privileged basis]" (L893). GPT-3 "has 96 layers and alternates attention blocks with MLP blocks" (L98). The toy models have d_model = n_heads x d_head, typically 12 x 64 (L1005), which is 768 (our arithmetic). (S2: L1005 is § Model Details, outside the scope; not needed by the post.)

**Traps.**
- "Embedding" and "layer": see traps 3 and 4. Elhage's x^n is the stream "at layer n", but a block has two sub-layers; the text does not say which of the 2k+1 states along k blocks is x^n.
- The sum is exact in the idealised model. Elhage drops biases (L142) and layer norm (L142, L158 note); his models put position outside the stream (L860, L1008), unlike GPT-2 (unit 10).
- "Communication channel" is Elhage's phrase for "it does no processing, all layers communicate through it" (L155). **S2:** that is a paraphrase in quotation marks; the words are "since it doesn't do any processing itself and all layers communicate through it" (L155). It is not Shannon's noisy channel; no noise, capacity or code is mentioned.
- Elhage chose *not* to study the stream directly (L635; also L594: the stream "isn't actually the fundamental object to study"). Cite that choice next to the sum. **S2:** cite the in-scope L170 ("rather than studying it directly") instead of the Related Work lines, unless Kunhao widens the scope.
- The paper's evidence is toy attention-only models; MLP layers are called "a major weakness of our work" (L140).

**Tensions.** Nanda L579 gives the same sum in terms of "layer n" and then calls the skip-connection reading "less helpful" (L580-581); Nanda calls the stream "the central object of a transformer" (L1408), Elhage the opposite (L594, L635). **S2:** L594 is hedged ("Our approach could be seen as ... deciding"), and L594 and L635 are in § Related Work, outside Kunhao's Elhage scope; L170 (in scope) gives the same choice: they will study communication "in terms of virtual weights, rather than studying it directly". Cite L170. ~~Elhage's stream carries information "about tokens other than the present token" (L155)~~ **S2 [FIXED, major]:** Elhage says "we believe the residual stream often dedicates subspaces to tokens other than the present token" (L155): a belief, "often", and "dedicates subspaces to", not "carries information about". At that firmness it still clashes with reading a vector at position t as "about token t".

**Toy idea (W9-A).** x0 = (1,2); a1 = (2,-1), f1 = (-1,1); a2 = (3,-2), f2 = (-1,2). Running sum: (3,1) -> (2,2) -> (5,0) -> (4,2), and x0 + a1 + f1 + a2 + f2 = (4,2) (checked by code). Say "after 2 blocks" and state the order (attention first, then MLP; Elhage L148, Nanda L588-590). Norms 2.236, 2.828, 4.472 are descriptive only.

### 6. [FIXED] Read = a linear map in, write = a linear map added back; virtual weights
**Where.** § High-Level Architecture, L148; § Virtual Weights and the Residual Stream as a Communication Channel, L157-158 and the sub-heading "Virtual Weights", L160-162; § Summary of Results, L121-122; Additional Intuition, § MLP Layers L788-805 (example of a virtual weight, L803). **S2:** L803 does not use the words "virtual weight"; calling W^m_I W_E one is our reading. § MLP Layers is outside Kunhao's named sections: use only with his OK.

**Claim, sorted by firmness.**
- *Asserts, for the idealised model:* "The residual stream has a deeply linear structure." (L157). "Every layer performs an arbitrary linear transformation to 'read in' information from the residual stream at the start" and "another arbitrary linear transformation before adding to 'write' its output" (L158). The linear stream is "very unusual among neural network architectures" (L157).
- *Virtual weights (asserts):* "one can think of implicit 'virtual weights' directly connecting any pair of layers" by "multiplying out their interactions through the residual stream" (L162); they "are the product of the output weights of one layer with the input weights [footnote] of another" (S2: an inlined footnote splits this; quote the two parts separately, as the brief's own rule says) and "describe the extent to which a later layer reads in the information written by a previous layer" (L162).
- *Limits:* the footnote at L158 "ignores the layer normalization at the start of each layer" and handles it "up to a constant scalar" (unit 9); for attention layers there are three input weights (W_Q, W_K, W_V) and the text simplifies "for simplicity and generality" (L162 note); the clean statement is for the attention-only case ("linear if one freezes the attention patterns", L121) (S2: L121 is about end-to-end paths of attention-only models; the stream's linear structure at L157-158 is stated for transformers generally, with the norm footnote); with MLPs "the presence of the GeLU activation means we can't linearize through MLP layers" (L790).

**Quotes.**
- Q[elhage:157, 8w]: "The residual stream has a deeply linear structure."
- Q[elhage:158, 18w]: "Every layer performs an arbitrary linear transformation to "read in" information from the residual stream at the start,"
- Q[elhage:162, 20w]: "one can think of implicit "virtual weights" directly connecting any pair of layers (even those separated by many other layers)"
- Q[elhage:162, 17w]: "These virtual weights are the product of the output weights of one layer with the input weights"
- Q[elhage:162, 18w]: "and describe the extent to which a later layer reads in the information written by a previous layer"
- Q[elhage:803, 17w]: "W^m_I W_E tells us how much different tokens encourage or inhibit this neuron through the residual stream"
- Q[elhage:122, 8w]: "Transformers have an enormous amount of linear structure."

(L162: the first and the second quotes are separated in the source by a footnote that is inlined between "input weights" and "of another"; "(ie. W_{I}^2W_{O}^1)" follows the footnote.)

**Numbers and equations.** Virtual weight: W_I^2 W_O^1, the input weights of layer 2 times the output weights of layer 1 (raw LaTeX at L162). Shape check from the notation table (L959-964), ours: W_I^m is [d_mlp, d_model] and W_O^m is [d_model, d_mlp], so W_I^2 W_O^1 is [d_mlp2, d_mlp1]: it takes layer 1's hidden activations to layer 2's pre-activations. ~~Attention-head output as a sum: W_O^H [r1; r2; ...] = sum_i W_O^{h_i} r^{h_i} (L181).~~ **S2: DROP (scope, major):** L181 is § Attention Heads are Independent and Additive, the attention-head algebra Kunhao excluded.

**Traps.**
- Virtual weights are *matrix products*. Linearity of the stream is what lets a read split over writers; it does not make the layers linear (MLPs, softmax, norm).
- "Read ... by performing a linear projection" (L148) is Elhage's wording; Nanda writes "Reading is a projection" (L1000). Same idea; see trap 5.
- A write *adds* (L148: "adding a linear projection back in"). It never replaces.
- The topic card's W9-B calls the read-split "a virtual weight in its smallest case". More exactly, W9-B is the additive split of a read (Nanda L1408); the virtual weight is the weight-level product. Label the toy "ours".

**Tensions.** Elhage calls the stream "completely linear" (L157) with the norm folded away (L158); Nanda puts a non-linear step in front of *every* read (L685, L702). Both are right about different idealisations; say which is used.

**Toy idea (W9-B).** Writer output vector o = a1 = (2,-1) and reader input vector r = (1,2): r.o = 0; for r' = (1,0): 2; for r'' = (0,1): -1 (our arithmetic). These are the entries of a "virtual weight" matrix in the 1x1 case. **S2:** this contradicts the trap above. It holds only if (ours) a1 is read as the output-weight vector of a one-neuron writer whose activation is 1; as written in W9, a1 is an activation, so r.a1 is a read-share, not a weight product. Pick one reading and label it ours. The read of the whole stream splits over writers: r.x0 = 5, r.a1 = 0, r.f1 = 1, r.a2 = -1, sum 5 = r.(5,0).

### 7. [FIXED] Subspaces, bandwidth, "memory management" (the information-theory question)
**Where.** Elhage § Subspaces and Residual Stream Bandwidth, L164-172 (footnotes inline at L168 and L172); § Activation Properties (bottleneck activations), L855; Nanda § Toy Model of Superposition, L269-289, and § Transformer Basics, L583; Olah L510 (see unit 4).

**Claim, sorted by firmness.**
- *Asserts:* the stream is "a high-dimensional vector space" in which layers "can send different information to different layers by storing it in different subspaces" (L166); "Once added, information persists in a subspace unless another layer actively deletes it" (L168).
- *Frames by analogy (scare quotes in the source):* dimensions "become something like 'memory' or 'bandwidth'" (L168).
- *Expects (hedged):* "It seems like we should expect residual stream bandwidth to be in very high demand!" (L170). Bottleneck activations are "unusually challenging to interpret" (L170).
- *Hedged evidence:* "we've seen hints that some MLP neurons and attention heads may perform a kind of 'memory management' role" (L172); some MLP neurons "have very negative cosine similarity between their input and output weights, which may indicate deleting information" (L172 note). Deletion could also be conditional (L172 note).
- *Measured (footnote):* PCA found token embeddings and unembeddings "concentrated in a relatively small fraction of the overall dimensions" for large models (L168 note).
- *Nanda's version:* the stream is "shared bandwidth/shared memory" (L583); with ~50,000 tokens and 768 dimensions "there almost has to be more features than dimensions, and thus superposition" (L280); in a bottleneck dimension it is "just used for 'storage'" (L282). **S2:** L282 opens with "Intuitively"; keep it. L278 says the two kinds of superposition are "terms invented by me".

**Quotes.**
- Q[elhage:166, 14w]: "layers can send different information to different layers by storing it in different subspaces"
- Q[elhage:166, 20w]: "In small models, it may be hundreds of dimensions; in large models it can go into the tens of thousands."
- Q[elhage:168, 13w]: "Once added, information persists in a subspace unless another layer actively deletes it."
- Q[elhage:168, 11w]: "dimensions of the residual stream become something like "memory" or "bandwidth""
- Q[elhage:168, 18w]: "the spectrum quickly decayed, with the embeddings/unembeddings being concentrated in a relatively small fraction of the overall dimensions"
- Q[elhage:170, 17w]: "Just a single MLP layer typically has four times more neurons than the residual stream has dimensions."
- Q[elhage:170, 4w]: "somehow communicating in superposition!"
- Q[elhage:172, 18w]: "we've seen hints that some MLP neurons and attention heads may perform a kind of "memory management" role"
- Q[nanda:583, 15w]: "The residual stream can be thought of as a shared bandwidth/shared memory of the transformer"
- Q[nanda:280, 12w]: "there almost has to be more features than dimensions, and thus superposition."
- Q[nanda:269, 15w]: "is when a model represents more than n features in an n dimensional activation space."
- Q[nanda:287, 23w]: "the only interference to care about is when projecting onto a feature direction is other features with non-zero dot product with that direction"

**Numbers and equations.** Hundreds to "tens of thousands" of dimensions (L166); heads work on subspaces "often 64 or 128 dimensions" (L166); ~~d_head/d_model "around 1/10 to 1/100" (L417);~~ **S2: DROP (scope, major):** L417 is § Three Kinds of Composition (attention-head algebra, excluded), and the source hedges it, "might vary from around 1/10 to 1/100"; one MLP has 4x as many neurons as the stream has dimensions (L170); the illustration "at layer 25 of a 50 layer transformer, the residual stream has 100 times more neurons as it has dimensions before it" (L170), which is 25 MLPs x 4 (our check, and a hypothetical, not a measured model). GPT-2 Small: d_model 768 (Nanda L611), vocabulary "about 50,000" (Nanda L640). Nanda's interference statement (L287): reading feature direction d picks up other features f with f.d != 0.

**Traps.**
- "Bandwidth" in Elhage counts dimensions and is in scare quotes; it is not a rate in Hertz and no capacity is computed. No source here gives any information-theoretic quantity (rate, capacity, interference bound). Lens 2 is a question the post poses, not a result.
- The "100 times" is an illustration for a hypothetical 50-layer model.
- "Hints", "may", "potentially" govern the memory-management paragraph; persistence is asserted, deletion mechanisms are not.
- Nanda's L280 is a counting argument over tokens, hedged with "almost has to"; it is not a measurement of features. Elhage's PCA footnote (L168) is a different measurement (embeddings use a small fraction of the dimensions).
- The conditions on superposition are sparsity (Nanda L309) and non-co-occurrence (Olah L510). **S2:** L309 is Nanda's summary of "Anthropic’s Toy Model of Superposition paper" (L301), not his own result; attribute it so.

**Tensions.** Nanda L282 says bottleneck superposition is for "storage" and not expected to do computation, while Elhage L170 pictures MLP layers "communicating in superposition". Nanda L583 says the stream is "the only way that information can move between layers"; attention is the only thing that moves information between *positions* (Nanda L601).

**Toy idea (W9, d = 2).** Two writers in disjoint subspaces do not interfere: write (3,0) on the x-axis and (0,-2) on the y-axis, and the two coordinate reads return 3 and -2 exactly (ours). A third writer along (1,1)/sqrt2 leaks into both reads. Cancellation in W9-A: f2 = (-1,2) puts +2 in y and undoes the -2 that a2 put there, which is "memory management" in miniature (but f2 is not -a2 = (-3,2); only the y part cancels).

### 8. [FIXED] No privileged basis
**Where.** Elhage L158 (the statement), L581 (consequence), § Activation Properties, L848-855, Notation table L883-957 (each activation tagged "privileged basis" or "not privileged basis"); Nanda § Representations of Features & Superposition, L228-262 (L234-245 definitions), L247-252 (bottleneck), L736 (no stream neurons), L957-958 (low-rank intermediate).

**Claim, sorted by firmness.**
- *Asserts (Elhage, idealised linear stream):* "the residual stream doesn't have a 'privileged basis'; we could rotate it by rotating all the matrices interacting with it, without changing model behavior" (L158). In a transformer "the only vectors with privileged bases are tokens, attention patterns and MLP activations" (L850).
- *Consequence, with a remedy (concedes, proposes):* it "doesn't really make sense to look at the 'neurons' ... of activations like the residual stream", but "This isn't to say that there aren't ways to study them" (L852). Also a cost: "the lack of a privileged basis removes some options for studying it" and an opportunity: "we can expand through it" (L581).
- *Nanda asserts the same with a caveat:* "all bases are non-privileged by default"; "Operations like addition, matrix multiplication, dot products, etc are unchanged under any change of basis" (L242-243); the stream is a bottleneck with "no non-linearities involved", so it "has no privileged basis (ish)" (L251); "there's no such thing as a residual stream neuron" (L736). Caveat: "the standard basis is always slightly privileged. Floating point representations and Adam inherently privilege the standard basis" (L245).
- *Definition (Nanda):* "A privileged basis is a meaningful basis for a vector space" (L234); it needs to be interpretable *a priori* from the architecture (L235), and is not the same as an interpretable basis.

**Quotes.**
- Q[elhage:158, 13w]: "One basic consequence is that the residual stream doesn't have a "privileged basis";"
- Q[elhage:158, 16w]: "we could rotate it by rotating all the matrices interacting with it, without changing model behavior"
- Q[elhage:850, 16w]: "In a transformer, the only vectors with privileged bases are tokens, attention patterns and MLP activations."
- Q[elhage:852, 19w]: "it doesn't really make sense to look at the "neurons" (ie. basis dimensions) of activations like the residual stream"
- Q[elhage:852, 11w]: "This isn't to say that there aren't ways to study them;"
- Q[elhage:581, 12w]: "the lack of a privileged basis removes some options for studying it"
- Q[nanda:234, 11w]: "A privileged basis is a meaningful basis for a vector space."
- Q[nanda:242, 23w]: "actually all bases are non-privileged by default - vector spaces are a geometric object, and there’s no intrinsic meaning to any particular basis."
- Q[nanda:243, 15w]: "Operations like addition, matrix multiplication, dot products, etc are unchanged under any change of basis."
- Q[nanda:245, 7w]: "the standard basis is always slightly privileged."
- Q[nanda:245, 17w]: "Floating point representations and Adam inherently privilege the standard basis, and are not the same under rotation."
- Q[nanda:249, 13w]: "many layers read and write from it, but each operation is purely linear"
- Q[nanda:736, 18w]: "there’s no such thing as a residual stream neuron, head neuron, key neuron, query neuron, value neuron, etc."

**Numbers and equations.** For an orthogonal change of basis R, (Rr).(Rx) = r.x (ours; the standard fact behind Nanda L243). The notation table tags the stream x^n, attention output h(x) and MLP output m(x) as "not privileged basis", and MLP activations a^m, attention patterns A^h, one-hot tokens t and logits T as "privileged basis" (L883-957).

**Traps.**
- "Privileged" is not "interpretable" (Nanda L234-235). A basis can be interpretable without being privileged.
- Elhage's invariance is shown for the linear picture (S2: "asserted", not "shown": one sentence at L158, no derivation; Nanda L243 gives the reason); the sources do not say whether it survives the norm layer in a real model (Elhage folds the norm "up to a constant scalar", L158; Nanda L702 says part of it is non-linear). Treat it as exact only for the idealised stream, and note Nanda's L245 caveat. The check on real models, if wanted, is a notebook job (not in the sources).
- An MLP's *neuron* basis is privileged (ReLU/GELU act coordinate-wise, Nanda L240); rotating the stream does not rotate that basis. E5 rotates only the stream's reads.
- Do not read a single coordinate ("dimension 17 of the hidden state") as a feature; this is exactly the analysis L852 says does not make sense.

**Tensions.** Olah's "neurons" make sense where there is a ReLU: Nanda L262 notes every activation in a convnet "is immediately after a ReLU", which is not true of the transformer's stream. Elhage's "without changing model behavior" is exact (S2: "exact" is ours; Elhage asserts it for the idealised linear stream); Nanda's "slightly privileged" (L245) is a leakage note. S2 scope note: L581 is § Related Work, Circuits; its privileged-basis sentence is on topic, the rest of the section is not.

**Toy idea (W9-C, E5).** Rotate the whole toy by 90 degrees. Calm (3,1), (4,2), (5,3) become (-1,3), (-2,4), (-3,5); the probe u = (-1,1)/sqrt2 becomes (-1,-1)/sqrt2; the score of (-1,3) is ((-1)(-1) + 3(-1))/sqrt2 = -1.414 as before. "Coordinate 2" meant something before the rotation and a different thing after; the group separation did not change (our arithmetic, checked by code).

### 9. [FIXED] Layer normalization: Elhage's fold and Nanda's placement
**Where.** Elhage § Model Simplifications, L142; the L158 footnote; § Technical Details, § Handling Layer Normalization, L1013-1023 (outside Kunhao's three named sections, see the note above). **S2 (scope, minor):** the Elhage appendix lines (L1013-1023) stay out of the post unless Kunhao confirms the fold-out; the card's approval did not change his Elhage scope. L142 (limits) and the L158 footnote are in scope. The Nanda parts are unaffected. Nanda § Transformer Components, "LayerNorm" L685-702, "Unembedding" L704-705, § Misc transformer words, "RMSNorm" L824-829, "Post-LayerNorm" L872-875, § Techniques, "Linearizing LayerNorm" L1377-1378 and "Folding LayerNorm" L1380-1383.

**Claim, sorted by firmness.**
- *Elhage (asserts, with a stated cost):* "Our transformer models apply layer normalization every time they read off from the residual stream." (L1015). "Subtracting off the average activation is a fixed linear transformation"; normalizing by variance "multiplies the vector by a scalar", which "commutes with all the other operations in a path", so everything but the normalization can be folded into adjacent parameters and the scale treated as "a variable reweighting of the set of path terms" (L1019). Cost: "paths going through different sets of layers aren't easily comparable" (L1019).
- *Nanda (asserts):* the norm is applied "whenever the residual stream is input into a layer (ie before the attention, MLP and unembedding layers)" (L685); of its four steps (subtract the mean, divide by the standard deviation, scale, translate) the division "is non-linear (but the other 3 are linear)" (L702); the unembedding has a norm in front (L705). RMSNorm is a "variant of LayerNorm" without centering or translating (L824-825). In post-LayerNorm models the norm is applied "when writing to the residual stream (ie at layer output)" and "I basically don't see this done anymore, but BERT did it" (L872-873). "LayerNorm is almost linear" (L1378).
- *Folding (Nanda):* merge the learned scale and translate "into the weights and bias of the linear layer immediately after the LayerNorm" (L1380), done in TransformerLens "into any layer that reads from the residual stream" (L1383).

**Quotes.**
- Q[elhage:142, 5w]: "We also ignore layer normalization."
- Q[elhage:158, 11w]: "This ignores the layer normalization at the start of each layer,"
- Q[elhage:158, 14w]: "but up to a constant scalar, the layer normalization is a constant affine transformation"
- Q[elhage:1015, 15w]: "Our transformer models apply layer normalization every time they read off from the residual stream."
- Q[elhage:1019, 10w]: "subtracting off the average activation is a fixed linear transformation"
- Q[elhage:1019, 23w]: "Normalizing by variance multiplies the vector by a scalar, and multiplying by a scalar commutes with all the other operations in a path."
- Q[nanda:685, 18w]: "used whenever the residual stream is input into a layer (ie before the attention, MLP and unembedding layers)"
- Q[nanda:702, 17w]: "In particular, the “divide by the standard deviation” step is non-linear (but the other 3 are linear)."
- Q[nanda:705, 14w]: "A LayerNorm is applied between reading the residual stream and applying the unembed map."
- Q[nanda:824, 20w]: "A variant of LayerNorm which sets the vector to have norm 1 and then scales each element by learned weights"
- Q[nanda:872, 20w]: "Post-LayerNorm models apply LayerNorm when writing to the residual stream (ie at layer output) not reading (ie at layer input)."
- Q[nanda:1378, 5w]: "Fortunately, LayerNorm is almost linear."
- Q[nanda:1380, 22w]: "merge the learned LayerNorm parameters to scale and translate into the weights and bias of the linear layer immediately after the LayerNorm"
- Q[nanda:1383, 12w]: "They get folded into any layer that reads from the residual stream"

**Numbers and equations.** Four steps (Nanda L686-693): centre, divide by standard deviation, scale, translate; "2*d_model learned parameters per LayerNorm layer" (L700). Folding identity as printed (L1381): (x (x) w_l + b_l) W + b = x (w (x) W) + (b_l W + b). Note Nanda's gloss "(x) meaning elementwise addition" at L1381 looks like a slip for elementwise multiplication; do not repeat it. Elhage's x-by-scalar remark is the reason the division matters: LN(2x) = LN(x), not 2 LN(x) (ours; Nanda L1378 gives the test "what happens as we double the input vector").

**Traps.**
- In pre-LayerNorm models the norm sits on the *read*, not on the *add*, so the stream stays a plain sum of writes (Nanda L579-594 with L685). In post-LayerNorm models what is added has passed through the norm (L872). **S2:** the last sentence is our gloss. Nanda says only that the norm is applied "when writing to the residual stream (ie at layer output)" (L872); whether it acts on the layer output or on the sum is not stated. Quote his words. Which one a model uses decides what a "write" is (T2).
- Do not cite Elhage L1019 for "layer norm is not linear": Elhage never says that outright; he treats the division as a scalar re-weighting. Cite Nanda L702.
- Nanda L1378 is garbled: "The centering, scaling and normalising are literally linear, while the normalisation is not" lists normalising twice. Use L702.
- RMSNorm: Nanda gives only an informal description ("norm 1"), says Gopher uses it (L827), and calls it "just a simpler (and thus easier to interpret) version of LayerNorm that works as well" (L829, his belief). The exact formula and which model families use it are UNSEEN.
- The fold flag's name is missing in both the text and the HTML (L1383), and the "centring of weights that write to the stream" mentioned in the card (T6) is not in either source.
- "Standard deviation": population or sample? Not stated (UNSEEN). The doubling test does not depend on it.

**Tensions.** Elhage: affine up to a scalar, fold it away (L158, L1019). Nanda: non-linear in one step, "almost linear" overall, fold only the learned scale and translate and keep "centering and normalising" (L1380). Nanda L816: the attention-only models ~~in TransformerLens~~ (S2: L816 says "A transformer variant studied in A Mathematical Framework") still have a norm before attention and unembed, whereas Elhage's analysis ignores it (Elhage L1015 says his models do apply it).

**Toy idea (W9 stream x2 = (4,2); ours, optional fold-out).** Subtract the mean (3): (1,-1). Divide by the standard deviation (population: 1): (1,-1). Double the input to (8,4): mean 6, centred (2,-2), standard deviation 2, result (1,-1) again, not (2,-2). So the read r.LN(x) loses the stream's size: for r = (1,2) it gives -1 for both x2 and 2 x2, while r.x doubles from 8 to 16. With the sample standard deviation both results are (0.707,-0.707); the invariance is the same. Scale and translate parameters are left at identity. Toy, convention unspecified in the sources.

---

## C. Nanda (2022), "A Comprehensive Mechanistic Interpretability Explainer & Glossary" [SEEN]
A personal, opinionated explainer ("I frequently go on long tangents", L79). Saved as "a janky HTML dump" of a Dynalist original (L58); the Dynalist original is not saved.

### 10. [FIXED] The stream by Nanda: after n layers, one per position, plus sizes and position schemes
**Where.** § Transformer Basics, L566-635 (the stream passage L576-601; hyperparameters L610-635); § Transformer Components, "Embedding" L667, "Positional information/embedding" L670-683, "Unembedding" L704-710, special tokens L655-665; § Misc transformer words, "Decoder-only" L831-837; § General, L405 ("hidden layer").

**Claim, sorted by firmness.**
- *Asserts:* "The residual stream after layer n is the sum of the embedding and the outputs of all layers up to layer n" and is "the input to layer n+1" (L579); at the start it is "the embedded tokens plus the positional embedding" (L586), the first attention layer's output is added, then the first MLP's (L588-590); the unembedding maps the final stream to logits (L594); input and output of each layer "live in the same space" (L596; S2: source "has the same dimension and lives in the same space"); "there is a separate residual stream for each position in the sequence" (L598); attention layers "are the only layers that can move information between token positions" (L601); the stream at position k "can only be a function of the first k tokens" in a decoder-only model (L831).
- *Opinion, labelled as such:* reading the stream as a series of skip connections is "a less helpful way to think about things", because "the skip connection conveys far more information than the output of any individual layer" (L580-581).
- *Scope:* "This is mostly a description of how GPT-2 works - there are many variants, but they're all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM" (L569). Nothing on the model families in Kunhao's work.
- *Position:* GPT-2 adds "learned, absolute positional embeddings" into the stream (L671); "Rotary/RoPE ... doesn't add anything in to the residual stream" (L679, with "(and I hate it)").
- *Library-style names:* `d_model` "Aka embedding_size or hidden_size" (L611-612).

**Quotes.**
- Q[nanda:579, 22w]: "The residual stream after layer n is the sum of the embedding and the outputs of all layers up to layer n"
- Q[nanda:577, 15w]: "Confusingly, a transformer layer actually contains two layers, an attention layer and an MLP layer."
- Q[nanda:586, 18w]: "At the start of the model, the residual stream consists of the embedded tokens plus the positional embedding"
- Q[nanda:598, 13w]: "Importantly, there is a separate residual stream for each position in the sequence."
- Q[nanda:601, 13w]: "Attention layers are the only layers that can move information between token positions"
- Q[nanda:581, 14w]: "the skip connection conveys far more information than the output of any individual layer"
- Q[nanda:569, 12w]: "they’re all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM"
- Q[nanda:671, 23w]: "there is a learned lookup table mapping each position to a vector of length d_model that is added in to the residual stream"
- Q[nanda:679, 23w]: "Rotary/RoPE is a popular method today (and I hate it), it’s a relative method and doesn’t add anything in to the residual stream."
- Q[nanda:612, 4w]: "Aka embedding_size or hidden_size"
- Q[nanda:405, 10w]: "A hidden layer refers to one of the internal activations"
- Q[nanda:659, 5w]: "GPT-2 and GPT-Neo were not."
- Q[nanda:665, 17w]: "padding is at the end, and heads can only attend backwards, so you just ignore the padding"
- Q[nanda:707, 8w]: "in my opinion is wildly unprincipled and annoying"

(L659: the sentence is about models trained *with* a BOS token: "OPT, and all of the toy and SoLU models in TransformerLens were trained with this, GPT-2 and GPT-Neo were not." L707 is Nanda's verdict on tying embed and unembed, which "Often models will" do (L707); "GPT-2 does this, GPT-Neo does not, GPT-3 does not" (L710).)

**Numbers and equations.** GPT-2 Small: d_model 768 (L611), d_mlp 3072 (L614; "almost always set to 4 * d_model", L617: 4 x 768 = 3072, our check), d_head 64 (L619), n_heads 12 (L622), n_layers 12 (L625); n_heads x d_head = d_model (L623); vocabulary "normally about 50,000 tokens" (L640). One logit vector per position; the logits at position k predict token k+1 (L603).

**Traps.**
- "Layer n" is ambiguous (trap 4): L579 does not say whether the n-th block's MLP is included. The post says "after k blocks".
- Between blocks there are other states: the MLP reads the stream *after* the attention write (L588-590). "The stream after k blocks" is one of 2k+1 states (our count from L586-590).
- "Hidden" appears only as `hidden_size` (L612) and as "hidden layer" for MLP-internal activations (L405). Neither says that a library's "hidden state" is the stream.
- One vector per position: "the hidden state of a sentence" has no meaning in these sources (L598-601); pooling across positions is a further operation they do not discuss.
- GPT-2 was trained without a BOS token (L659); the saved text says nothing on the padding side of any library, only that for generative models "padding is at the end" (L665).
- The generalisation to other models is Nanda's opinion (L569) and covers GPT-style models up to 2022.

**Tensions.** ~~Nanda L580-581 against Elhage L148 on whether to read the stream as a series of skip connections.~~ **S2: DROP (major).** There is no such tension: "skip connection" does not occur in Elhage, L148 does not use that framing, and Elhage also prefers "the residual stream terminology" (L155). Both take the stream view. Elhage's own models put position outside the stream (Elhage L860, L1008: "adding sinusoidal embeddings immediately before multiplying by W_Q and W_K"), unlike GPT-2 (Nanda L671); Elhage names this difference (L857-862). (S2: correct, but L857-862 and L1008 are outside Kunhao's Elhage scope; the post can make the point from Nanda L671 and L679 alone.) Nanda L583 says information moves between layers only through the stream, and L601 that only attention moves it between positions.

**Toy idea (W9, two positions; ours).** Two copies of W9-A, one per token position, each with its own embedding. The MLP writes (f1, f2) at a position depend only on that position's own stream. The only coupling is an attention write at position 2 that copies something derived from position 1's stream. Nothing else crosses. No new numbers are needed for the brief.

### 11. [FIXED] "Reading is a projection; writing is an embedding"; direct logit attribution
**Where.** § A Mathematical Framework for Transformer Circuits, "Composition" L993-1002; § Transformer Components, "A transformer neuron" L727-734; § Mechanistic Interpretability Techniques, "Direct Logit Attribution" L1405-1422; Elhage L148 (same idea).

**Claim, sorted by firmness.**
- *Asserts:* "We can think of a component as reading in its input from the residual stream and writing out its output to the residual stream. Note that these operations are not opposites!" (L997-998). "Reading is a projection, the residual stream is dotted with each input vector of the relevant matrix." (L1000). "Writing is an embedding, it adds on its output. This can only go to a specific low rank subspace" (L1002).
- *Direct logit attribution (asserts):* "any linear function of the residual stream can be perfectly decomposed into the contribution of each layer of the transformer" (L1408); for a single position this "is equivalent to projecting onto a direction in residual stream space" (L1412); "Projecting means 'map x -> x . v for some fixed vector v'. Projecting is sometimes specifically used when v is a unit vector" (L1415, math as printed).
- *Caution (his own):* LayerNorm "is approximately a linear map" (L1410), so the decomposition uses an approximation; log probabilities are not linear (L1417, formula missing in the text layer).
- *Neurons:* a transformer neuron's input and output weights "are d_model length vectors, and correspond to directions in the residual stream" (L728); "we interpret the neuron output as its contribution to the residual stream" (L734).

**Quotes.**
- Q[nanda:997, 24w]: "We can think of a component as reading in its input from the residual stream and writing out its output to the residual stream."
- Q[nanda:998, 7w]: "Note that these operations are not opposites!"
- Q[nanda:1000, 17w]: "Reading is a projection, the residual stream is dotted with each input vector of the relevant matrix."
- Q[nanda:1000, 17w]: "every vector in the residual stream contributes (unless it’s orthogonal), though some contribute much more than others"
- Q[nanda:1002, 9w]: "Writing is an embedding, it adds on its output."
- Q[nanda:1002, 18w]: "This can only go to a specific low rank subspace, spanned by the output vectors of the matrix."
- Q[nanda:1408, 20w]: "any linear function of the residual stream can be perfectly decomposed into the contribution of each layer of the transformer"
- Q[nanda:1410, 13w]: "The Unembed is a linear map, and LayerNorm is approximately a linear map"
- Q[nanda:1412, 12w]: "this is equivalent to projecting onto a direction in residual stream space"
- Q[nanda:1415, 11w]: "Projecting is sometimes specifically used when $v$ is a unit vector."
- Q[nanda:728, 13w]: "Note that both of these are d_model length vectors, and correspond to directions"
- Q[nanda:734, 13w]: "So we interpret the neuron output as its contribution to the residual stream"

**Numbers and equations.** Projection as printed (L1415): x -> x . v for a fixed vector v. MLP as a sum of neurons (L995): n W_out = sum_i n_i W_out,i, where n = GELU(x W_in) (raw LaTeX in the text). In the post's notation (ours): score s = u . x; read split s = u.x0 + u.a1 + u.f1 + ...; write x -> x + v.

**Traps.**
- "Projection" has (at least) the two senses of trap 5; Nanda's default is the *number* x.v, with the unit-vector case only "sometimes".
- "Embedding" in "Writing is an embedding" is the mathematical sense (a small space placed inside a big one), not the token embedding.
- "Not opposites": reading along u does not recover what a writer put along u unless the other writers are orthogonal to u. That is why the read in W9-B has a zero term and a negative term.
- The decomposition is exact for *linear* functions of the stream. Anything after the norm, or log-probabilities, is an approximation or needs linearising (L1417, L1425).
- Nothing in this entry says that *adding* a vector changes behaviour; "writing adds" is the algebra only (unit 14).

**Tensions.** Elhage L148 says "linear projection"; Nanda says the read is "dotted with each input vector"; same operation. ~~Nanda's L1415 ("not necessarily a unit vector")~~ **S2 [FIXED, major]:** those words are not in any source. L1415 says "for some fixed vector $v$" and "Projecting is sometimes specifically used when $v$ is a unit vector." Contrast that with the post's choice of a unit u (ours).

**Toy idea (W9-C).** Score s = u.x. Steering adds v: s(x + v) = s(x) + u.v for every point, whatever x is. With u = (-1,1)/sqrt2 and v = 2u: every score rises by 2 (calm -1.414 -> 0.586, urgent 1.414 -> 3.414); with v = 2(1,1)/sqrt2 the change is 0 (checked by code). That is "writing adds" in the smallest case, and it is affine (a translation), not linear, in x. Arithmetic only: no source here says steering moves behaviour.

### 12. [FIXED] "Features as directions", feature definitions, and probing
**Where.** § General, L85-182 ("feature" L104-135); § Representations of Features & Superposition, L184-264 ("Features as directions" L199-205, scalar vs binary L207-221, "Features as neurons" L254-262); § Non-MI Techniques, "Probing" L1586-1587 and "TCAV" L1593-1598; § Induction Circuits, L1096.

**Claim, sorted by firmness.**
- *Defines as a hypothesis:* "Features as directions is the hypothesis that features are represented in the model as directions in activation space." (L199). It is "a much more specific claim than the fuzzy notion that 'model's internal activations represent features'" (L202).
- *Gives an intuition, not evidence:* the main thing a model can do is linear algebra, so "if a later layer wants to access a feature it can project onto that feature's direction" (L200); "If, specifically, features are directions ..., then the function to recover a feature from activations would be projecting onto that feature's direction" (L203); "Ideally the feature directions would be orthogonal" (L203).
- *Admits the limits:* ~~in practice the description "is pretty imprecise" (L216);~~ **S2 [FIXED, major]:** L216 ("In practice, this is a pretty imprecise description.") refers to the binary-versus-continuous description of features (L207-215), not to features as directions; use it only for that point. With superposition they "cannot all be orthogonal, so we cannot perfectly recover each feature" (L275); features as neurons is "probably not entirely true" and "at best only slightly true for transformers" (L257-259; L257 is cut off in the text layer). **S2 [FIXED, major]:** keep the first half of L259: "There is a decent amount of empirical evidence that this is mostly true of Inceptionv1".
- *Probing (asserts a definition, hedges the meaning):* a probe is "a 1D linear map ... corresponding to a direction in activation space, which likely corresponds to that feature" (L1587).
- *Elsewhere flat:* "Features are the fundamental building block of models" (L135); "'What token is this' and 'what position is this in' are represented as separate directions in the residual stream" (L1096).
- *Feature definition:* "a property of an input to the model, or some subset of that input", "a fuzzy and non-rigorous idea" (L104-105).

**Quotes.**
- Q[nanda:104, 17w]: "A feature is a property of an input to the model, or some subset of that input"
- Q[nanda:135, 15w]: "Features are the fundamental building block of models - the model’s internal activations represent features"
- Q[nanda:199, 18w]: "Features as directions is the hypothesis that features are represented in the model as directions in activation space."
- Q[nanda:200, 12w]: "the main thing a model is capable of doing is linear algebra"
- Q[nanda:200, 16w]: "if a later layer wants to access a feature it can project onto that feature’s direction"
- Q[nanda:202, 19w]: "Note that this is a much more specific claim than the fuzzy notion that “model’s internal activations represent features”."
- Q[nanda:203, 24w]: "If, specifically, features are directions in activation space, then the function to recover a feature from activations would be projecting onto that feature’s direction."
- Q[nanda:203, 17w]: "Ideally the feature directions would be orthogonal, so that they can be perfectly recovered with a projection."
- Q[nanda:259, 9w]: "this seems at best only slightly true for transformers"
  - **S2:** quote the whole sentence (25 w): "There is a decent amount of empirical evidence that this is mostly true of Inceptionv1, but this seems at best only slightly true for transformers."
- **S2 addition (balance, L200, 11w):** "features as directions is an extremely natural way to represent things"
- Q[nanda:1586, 15w]: "Probing: A technique for identifying directions in network activation space that correspond to a concept/feature."
- Q[nanda:1587, 20w]: "giving a 1D linear map (a probe), corresponding to a direction in activation space, which likely corresponds to that feature"
- Q[nanda:1096, 19w]: "“What token is this” and “what position is this in” are represented as separate directions in the residual stream"

**Numbers and equations.** None needed. A probe is a map x -> u.x trained on labelled activations "on a specific activation (eg the output of layer 5)" (L1587; the layer is an example).

**Traps.**
- Two sentences are cut off in the text layer (L207 "That is, it matters whether the feature" and L257 "The only reason this is even somewhat plausible is that neuron activations."). Do not quote around or complete them.
- The intuition for directions is an argument from what models do (matrix multiplication), not a measurement (L200). Say "Nanda's intuition".
- A probe returns a direction that separates the labelled sets; the source says it "likely corresponds" to the feature (L1587). Whether the *model uses* that direction is not addressed here (the see-versus-do point is ours; strands 2-3).
- Nanda's firmness varies (trap 8): quote L199 for "hypothesis", and L135 and L1096 only with a note that they are stated without a hedge.
- "Feature" has three definitions across the sources (Olah L694, Nanda L104, Elhage uses none). **S2:** two definitions; Elhage gives none.

**Tensions.** Olah (Claim 1): directions are linear combinations of neurons in a layer, evidence mostly single neurons (L242). Nanda: directions in activation space (L199), neurons "at best only slightly" (L259). Elhage never says "feature directions"; he writes of "subspaces" the layers read and write (L126, L166). Nanda's example at L1096 (token identity and position as separate directions) is the only concrete stream-direction claim in the three sources, in the induction context, unhedged and without evidence in the glossary.

**Toy idea (W9-C).** Margin of the best gap between the two groups by probe angle (checked): 0 at 0, 90 and 180 degrees; 0.695 at 100 and 170; 2.000 at 120 and 150; 2.828 at 135; -2.828 (identical score sets) at 45. The probe is a direction found by us; the two groups are labels we gave. "Probe accuracy" is not claimed.

---

## D. Cross-source units

### 13. [FIXED] The logit lens (the original post is a gap)
**Where.** Elhage § Related Work, "The Logit Lens", L589-594; Elhage § Related Work, "Bertology Generally", L631-635; Nanda § Mechanistic Interpretability Techniques, "Logit lens" L1424-1438 (entry corrupted), "Direct Logit Attribution" L1405-1422.

**Gap.** The post that introduced the logit lens (by the LessWrong user Nostalgebraist) is **not** among the saved sources. The saved Nanda HTML links it as https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens (link read from the saved HTML; the page itself is UNSEEN). Elhage and Nanda give secondhand accounts.

**Claim, sorted by firmness.**
- **S2 (scope, minor):** the Elhage lines in this unit (L589-594, L629-635) are § Related Work, outside Kunhao's Elhage scope (he took the logit lens from Nanda). Use them only with his OK; the post can rest on the intact Nanda lines.
- *Elhage (describes, no hedge):* (S2: there are hedges, "to look at how model predictions evolve in some sense", L592, and "could be seen as", L594) since the stream "is iteratively refined, one can apply the unembedding matrix to earlier stages of the residual stream" (L592), "essentially look at W_U x_i". Elhage then declares a different stance: "deciding that the residual stream isn't actually the fundamental object to study" (L594).
- *Nanda (asserts):* the lens applies "the final layer norm, and unembed, and log_softmax, rather than linearizing anything" (L1425); "The key finding is that, often, the model has become confident in the correct next token before the final layer, and each layer incrementally improves and refines that confidence" (L1427); this "is evidence for thinking about transformers as having the central object of the residual stream, that each layer incrementally updates" (L1428); "layer normally means block" (L1430); and it is "equivalent to zero ablating layers" after the chosen one (L1432).
- *Hedged:* "often" (L1427); "evidence for thinking about" (L1428).
- *Corrupted:* the entry's first sentence reads "A technique where we take the residual stream after layer $kper-token loss." (L1424).

**Quotes.**
- Q[elhage:592, 20w]: "since the residual stream is iteratively refined, one can apply the unembedding matrix to earlier stages of the residual stream"
- Q[elhage:594, 12w]: "deciding that the residual stream isn't actually the fundamental object to study"
- Q[elhage:632, 22w]: "using probing methods to explore the linguistic properties at various stages of BERTs residual stream, referred to as embeddings in that literature"
- Q[nanda:1424, 14w]: "Logit lens: A technique where we take the residual stream after layer $kper-token loss."
- Q[nanda:1425, 15w]: "we normally apply the final layer norm, and unembed, and log_softmax, rather than linearizing anything"
- Q[nanda:1427, 15w]: "often, the model has become confident in the correct next token before the final layer"
- Q[nanda:1427, 8w]: "each layer incrementally improves and refines that confidence"
- Q[nanda:1428, 21w]: "This is evidence for thinking about transformers as having the central object of the residual stream, that each layer incrementally updates."
- Q[nanda:1430, 13w]: "Here layer normally means block, not attention/MLP layer, though the same idea works."
- Q[nanda:1432, 7w]: "This is equivalent to zero ablating layers"

(L1427: the two parts are one sentence; quote both. L1424 is quoted to show the corruption, not as a definition.)

**Numbers and equations.** Elhage: W_U x_i (L592), no norm. Nanda's pipeline (L1425), in our notation: lens(x_k) = log_softmax(W_U LN_f(x_k)), with LN_f the final norm. This expansion is **ours**, restating the intact words; the original definition is UNSEEN. The zero-ablation index range is printed as "k+1 ... n_layers-1" (L1432, math as printed).

**Traps.**
- The definition is unreadable in the saved copy, in both the text and the HTML. Use only intact lines.
- Two versions: Elhage's (no norm) and Nanda's (with the final norm and log_softmax). State which one a notebook uses.
- "The key finding" is Nanda's summary of someone else's result; the post should say "as Nanda describes it".
- It describes a pattern in an intermediate vector's unembedding; the sources do not claim it shows the intermediate stream "means" a next-token guess, only that it fits the stream-as-refined-sum picture (L1428).
- Nanda L1428 and Elhage L594 disagree about the stream's rank as an object of study. Elhage also lists probing "stages of BERT's residual stream" as a different, "top-down" line of work he does not follow (L632-635).

**Tensions.** Elhage: study the sum's parts, not the stream (L594, L635). Nanda: the stream is "the central object" (L1408, L1428). The post sits on Nanda's side for its reads, which is Kunhao's situation, and should say Elhage chose otherwise.

**Toy idea (W9, ours).** A 3-token unembedding with rows at 0, 120 and 240 degrees, applied without a norm (Elhage's version) to the running stream: x0 = (1,2) gives logits (1.000, 1.232, -2.232); x1 = (2,2) gives (2.000, 0.732, -2.732); x2 = (4,2) gives (4.000, -0.268, -3.732) (checked by code). The leading token flips from B to A after block 1 and stays: a picture of "confident before the last layer". Toy rows and numbers invented; no claim about fidelity of any real lens.

### 14. [FIXED] Editing, steering, post-training: what the sources define, and what they leave out
This unit is a map of a gap, because clauses 1, 6, 9 of the lens sentence (topic card section 3b) depend on it.

**Where.** Nanda § General, "Intervening on or editing an activation" L147-148; § Training, "Fine-tuning" L905-906, "RLHF" L908-910; § Mechanistic Interpretability Techniques, "Ablation" L1361-1375, "Activation Patching" L1442-1458, "Causal Tracing" L1458; § Non-MI Techniques, "ROME" L1578-1581; § Tooling L1603; Elhage L535-536; Olah L490, L633.

**Claim, sorted by firmness.**
- *Defined (asserts):* intervening on an activation means to "run the network, then ... stop it once it's computed an activation, edit or replace that activation, and then resume running the model" (L147); pruning a neuron sets its activation to zero (L148); activation patching "replaces (patches) an activation with that same activation on input B" (L1442); ROME edits "the memory of a network" by adding "a rank one matrix to the output weights" of an MLP layer (L1578-1579); TransformerLens lets you "cache all of their activations, and intervene on them" (L1603).
- *Cautions about interventions (his own):* zero ablation "is arguably unprincipled, because the model may be using that part as a bias term" (L1365); mean ablation "may still throw the model off the manifold of 'normal activations'" (L1368); after an ablation a "backup name mover head in a later layer will change its behaviour to compensate" (L1375).
- *Fine-tuning and RLHF are defined only as training procedures* (L905-908): "Taking a pretrained model, and training it on a more specific task", and RLHF as "a special form of fine-tuning". Nothing in the saved texts says what they change inside a model.
- *Olah:* the test of understanding a circuit is to "predict what will change if you edit the weights" (L633); the authors plan such a test (L490).
- ~~*Elhage:* an experimental recipe replaces a head's output before it is added into the stream, e.g. with zeros (L535-536).~~ **S2: DROP (scope, major):** L535-536 is § Term Importance Analysis, in the induction-head part Kunhao excluded.

**Quotes.**
- Q[nanda:147, 24w]: "to run the network, then to stop it once it’s computed an activation, edit or replace that activation, and then resume running the model"
- Q[nanda:1442, 17w]: "runs the model on input A, replaces (patches) an activation with that same activation on input B"
- Q[nanda:1365, 16w]: "This is arguably unprincipled, because the model may be using that part as a bias term"
- Q[nanda:1368, 15w]: "but imperfectly, as it may still throw the model off the manifold of “normal activations”"
- Q[nanda:1375, 15w]: "a backup name mover head in a later layer will change its behaviour to compensate"
- Q[nanda:905, 13w]: "Fine-tuning: Taking a pretrained model, and training it on a more specific task."
- Q[nanda:908, 16w]: "Reinforcement Learning from Human Feedback (RLHF) is a special form of fine-tuning large, pre-trained language models."
- Q[nanda:1603, 9w]: "cache all of their activations, and intervene on them"
- Q[olah:633, 25w]: "They’re very much falsifiable: for example, if you understand a circuit, you should be able to predict what will change if you edit the weights."
- ~~Q[elhage:535, 24w]: "instead of adding attention head outputs to residual stream, save the output, and then replace it with a zero tensor of the same shape"~~ **S2: DROP** (scope, as above; the quote itself is verbatim).

**Numbers and equations.** None. (Zero-ablation of layers k+1... in the logit lens is in unit 13.)

**Traps.**
- **Steering, activation addition and "steering vector" do not occur in any of the three sources.** Adding a vector to the stream is, in the algebra, "one more write" (unit 11), but that it changes behaviour as intended is not a claim of any source. Mark it UNSEEN.
- "Edit" in these sources means replace, zero or patch an activation, or change weights. Adding a chosen vector is a different intervention (ours). **S2:** one additive intervention is in the sources: causal tracing "add[s] significant noise to their token embeddings" (Nanda L1458). That is random noise on the embeddings, not a chosen direction, so the point stands in its narrower form.
- Nanda's cautions (L1365-1375) concern ablation. Applying them to additive steering is our analogy, to be labelled so.
- Nothing links fine-tuning or RLHF to the stream, to directions, or to what is represented (topic card clause 6, R2). Keep it out of the lens.

**Tensions.** Olah L633 treats an edit-prediction test as the mark of understanding; Nanda L1375 reports a compensation effect that makes a naive edit-prediction wrong (S2: "makes ... wrong" is ours; Nanda reports only the compensation, in GPT-2 Small's IOI task, for zero or mean ablation). ~~Elhage L535-536 describes replacing a head's contribution *before* it is added, which is the same "write" the post treats algebraically.~~ (S2: dropped, scope.)

**Toy idea.** No new toy for post-training (keep it out). For steering reuse W9-C unit 11. For "intervention changes more than the edited part", W9 has no feedback; do not invent one.

---

## Not in the sources, to be shown by the notebooks [UNSEEN — re-searched by S2]
**S2:** every absence below was re-searched with grep over the three `.txt` files ("hidden state", "hidden_state", "output_hidden", "steer", "activation addition", "fine-tun", "RLHF", "post-train", "Qwen", "Llama", "Gemma", "Mistral", "instruct", "bus", "skip connection", "standard deviation"). All confirmed absent, with three notes: (1) "Mistral" occurs once, Nanda L1676, as Stanford CRFM's "Mistral library" for training, not the model family; (2) T9 cites Elhage L226, which is attention-head algebra (out of scope); L121 is enough; (3) the "Dynalist" link in the saved page points to https://neelnanda.io/glossary, the URL that redirected to the saved page itself (see the SOURCE header), so it does not reach the Dynalist original.
The topic card's flags T1-T14 are not source facts. For each: what the three saved sources do give (if anything), then what the notebook must settle. Nothing below may enter the post from memory.

| Flag | What the sources give | What is left to show |
|---|---|---|
| T1 Hugging Face `hidden_states` indexing | Nothing. `hidden_size` only as an alias of `d_model` (Nanda L612). | Which index is the embedding; whether entry l+1 is the output of block l; whether the last entry has the final norm applied. |
| T2 Norm placement and type in the model families | Pre-LN is defined (Nanda L685, L705), post-LN is defined (L872, "BERT did it"), RMSNorm is described informally (L824-829, used by Gopher). Elhage drops the norm (L142). Nothing on Qwen3, Llama 3, Gemma 3, Mistral. | Module tree and decoder-layer code of the models used; whether anything sits between a sub-layer and the add. |
| T3 Embedding scaling and tying | Tying exists and is "often" done; GPT-2 ties, GPT-Neo and GPT-3 do not (Nanda L707-710). Nothing on scaling. | `hidden_states[0]` against the embedding lookup; `tie_word_embeddings`. |
| T4 Position information | GPT-2 adds learned absolute position into the stream (Nanda L671); rotary adds nothing (L679); Elhage's models keep position out of the stream (L860). | What "embedding" contains in each model used. |
| T5 One stream per position; padding and BOS | One stream per position (Nanda L598); attention is the only mover (L601); GPT-2 trained without BOS (L659); "padding is at the end" for generative models (L665). | Which position index is meant; padding side and BOS in the library; tokens printed. |
| T6 TransformerLens hook names and weight processing | TransformerLens exists for caching and intervening (Nanda L1357, L1603); LN folding exists and folds into the next linear layer's weights (L1380-1383); the flag name is lost. Nothing on `resid_pre`, `attn_out`, `mlp_out`, `resid_post`, and nothing on centring weights. | Hook names; TL against Hugging Face GPT-2 with and without weight processing. |
| T7 Numerical tolerance | Nothing, except Nanda's remark that floating point privileges the standard basis (L245). | Float32 errors on CPU. |
| T8 Logit lens details | Elhage L592 (no norm); Nanda L1425-1432 (intact lines). Definition corrupted (L1424). Original post not saved. | Final norm plus unembedding reproduces the model's logits; lens with and without the norm. |
| T9 "Linear" senses | Read is linear (Elhage L148; Nanda L1000, L1415); the norm's division is non-linear (Nanda L702); attention is linear only if patterns are frozen (Elhage L121, L226). "Affine" for steering is **not** in the sources. | score(h + alpha u) - score(h) = alpha; cosine similarity is not additive. |
| T10 Norm growth and outliers | Nothing. | Plot per layer and per position; describe only. |
| T11 Model numbers (hidden size, number of blocks) | GPT-2 Small only: 768, 12, 12, 64 (Nanda L611-625). | Print from `config` for each model. The post's "4096" is Kunhao's own example. |
| T12 Wiki name collisions | Superposition and circuit senses: Olah L205, L508; Nanda L269, L377. | A wiki task, not a source one. |
| T13 The bus metaphor | No source uses "bus". "Communication channel" (Elhage L155), "shared bandwidth/shared memory" (Nanda L583). | Say what the metaphor leaves out (one writer at a time, addresses) from the algebra, not from a source. |
| T14 Source scope | Stated in the sources (see Traps 1). | Say it in the post where each is first cited. |

**Other things the sources do not give** (all UNSEEN):
- The original logit-lens post, and the Dynalist original of Nanda's glossary.
- The body of Nanda's logit-lens entry (L1424), the sentences cut at L207 and L257, the formulas missing at L1391, L1410, L1417, and the name of the fold flag at L1383.
- Anything on "hidden state", `output_hidden_states`, steering, activation addition, steering vectors, or what fine-tuning or RLHF change inside a model.
- Anything on Qwen3, Llama 3, Gemma 3, Mistral, or on base versus instruct checkpoints.
- The exact RMSNorm formula; the standard-deviation convention in LayerNorm; whether the no-privileged-basis argument survives a real model's norm.
- Elhage's forthcoming paper (L102, L568: "analogous attention heads and circuits in large models"), the content of the "convergent learning" and similarity papers Olah cites (L536-539, L780-782), and the figures in all three pages (they are absent from the text layer).

## Notes on the topic card, found while reading the sources [CHECKED by S2]
**S2:** the section has ten numbered notes (the S2 task said nine); all ten are checked. Verdict after each.
1. **RMSNorm is in the glossary.** Card T2 and section 12 say the sources do not mention RMSNorm and propose fetching the RMSNorm paper. Nanda L824-829 has a (rough) entry. The paper is still needed for the exact formula. **S2 verdict: brief right, card wrong** (T2 says the sources "do not mention RMSNorm"; Nanda L824-829 does). Small slip: only T2 says that; §12 proposes the fetch.
2. **Layer norm is "not linear" in Nanda L702, not in Elhage L1019.** Card clause 10 cites Elhage L1019 for it; Elhage describes the division as a scalar re-weighting and never says "non-linear". **S2 verdict: brief right.** Elhage L1019: "everything except for normalizing by variance, layer normalization applies a fixed affine transformation"; the division "multiplies the vector by a scalar". "Not linear" is Nanda L702.
3. **"Hidden" is not absent.** Card clause 7 says "hidden state" does not occur in any source (true), but `hidden_size` (Nanda L612) and "hidden layer" for MLP-internal activations (Nanda L405) do, and the second can mislead. **S2 verdict: both right.** The card's sentence is true; the brief's addition is correct but incomplete (also Olah L538, Nanda L415, L723).
4. **Cancellation is at Elhage L172, not L168.** Guess-first question 2 cites L168 (persistence); "reading in information and writing out the negative version" and the hedges ("hints", "may") are at L172. **S2 verdict: brief right.** L168 asserts persistence with no hedge; the negative-version deletion and its hedges are at L172.
5. **The glossary has more than one damaged entry.** Card T14 says "at least one corrupted entry". The damage includes L207, L257, L1391, L1410, L1417, L1424, and the fold flag at L1383, and the sentence at L1378 is garbled. **S2 verdict: brief right** (the card understates); the brief's list is still short: add L626, L833, L854, L955, L1167, L1172.
6. **TransformerLens weight processing is partly sourced.** Card T6 treats folding as a memory suspicion. Nanda L1380-1383 supports folding the learned scale and translate into the next linear layer; centring of write weights is not mentioned. **S2 verdict: brief right.** L1380 merges the learned scale and translate into the next linear layer; L1383 says TransformerLens folds them by default (flag names missing). Nothing on centring in either source.
7. **The virtual-weight label on W9-B is loose.** W9-B is the additive split of a read; the virtual weight is a matrix product (Elhage L162). Say so in the post, or call W9-B "who hears whom" only. **S2 verdict: brief right in substance.** The label holds only if a1 is read as a one-neuron writer's output weights with activation 1 (ours). The brief's own unit 6 toy said the opposite; fixed there.
8. **"Direction" in the card (unit vector up to sign) is ours.** Olah L194 and L679 do not say it; Nanda L1415 allows any fixed v and says "sometimes" unit. **S2 verdict: brief right.** No unit-length or sign convention in Olah or Nanda. The card puts it in the "sense the post uses" column, so it needs only an "ours" label.
9. **No-privileged-basis and the norm.** Card E5 and Lens 1 treat rotation invariance as simply true; the sources prove it for the idealised stream (Elhage L158) and Nanda adds "slightly privileged" (L245). Keep E5 as a statement about reads in the toy. **S2 verdict: brief right in substance, one word too strong:** the sources do not "prove" it; Elhage asserts it in one sentence (L158), Nanda gives the reason (L243) and the caveat (L245).
10. **Clause 5 is stronger than Olah.** "Behaviours are circuits" goes beyond the hedged L636-637; the card already reframes it, and this brief supports that. **S2 verdict: brief right, and so is the card** (clause 5 row and R3 already reframe it).

## Unit index
1 Olah Claim 1 (features, directions) · 2 Olah Claim 2 (circuits) · 3 Olah Claim 3 (universality) · 4 Olah polysemantic neurons and superposition · 5 Elhage stream as a sum and communication channel · 6 Elhage read/write, linear structure, virtual weights · 7 Elhage subspaces, bandwidth, memory management (with Nanda on bottleneck superposition) · 8 No privileged basis (Elhage and Nanda) · 9 Layer normalization (Elhage fold, Nanda placement) · 10 Nanda: stream after n layers, one per position, sizes, position schemes · 11 Nanda: reading is a projection, writing is an embedding, direct logit attribution · 12 Nanda: features as directions, feature definitions, probing · 13 The logit lens (Elhage and Nanda; original post a gap) · 14 Editing, steering, post-training: what is defined and what is missing.

---

## Writer-must-not-use list (S2, 2026-10-25)
The writer must not use any of the following in the post, the audio script, the exercises or the English pack. Each item has an S2 note in the unit named.
1. **Hidden Olah text.** Olah L147-148, L249-254, L265, L267, L287, L455, L658 are commented out of the published page. In particular, do not use "Part of this claim is trivially true", "The interesting part of the claim ...", "For us, the way out of the curse of dimensionality ...", or the "trivially true part / interesting part" split (unit 1).
2. **"not necessarily a unit vector"** as Nanda's words. They are not in any source (unit 11).
3. **Nanda L216 ("a pretty imprecise description") as a limit of features as directions.** It is about binary versus continuous features (unit 12).
4. **Half of Nanda L259.** Do not use "at best only slightly true for transformers" without "mostly true of Inceptionv1", and do not say Nanda is answering or rejecting Olah (units 1, 12).
5. **A Nanda-versus-Elhage disagreement about skip connections.** There is none (unit 10).
6. **Elhage L155 without its hedge.** Not "Elhage's stream carries information about other tokens"; it is "we believe ... often dedicates subspaces to tokens other than the present token" (unit 5).
7. **Excluded Elhage material** (attention-head algebra, induction heads): L181, L417, L535-536, L568, L226. Do not use.
8. **Elhage outside Kunhao's named sections**, unless he widens the scope: L589-594 and L629-635 (Related Work: logit lens, Bertology), L788-807 (MLP Layers), L857-868 and L1004-1008 (positional mechanism, model details), L1013-1023 (layer-norm appendix). In scope: L144-172 (High-Level Architecture through Subspaces and Residual Stream Bandwidth), L846-855 (Activation Properties: privileged basis, bottleneck), the notation rows L883-965, the privileged-basis sentence at L581, and the limit statements L95-102, L136-142, L562-572, used only to state limits.
9. **Quoted paraphrases presented as quotes:** "technically ignore one ReLU", "live in the same space", "is pretty imprecise", "it does no processing, all layers communicate through it", "about tokens other than the present token", "representation similarity". Use the exact source words given in the S2 notes, or paraphrase without quotation marks.
10. **Damaged lines as text:** Nanda L1424 as a definition of the logit lens; L1378's "The centering, scaling and normalising are literally linear, while the normalisation is not"; completions of L207, L257, L626, L833, L854, L955; the missing formulas at L1391, L1410, L1417, L1167, L1172; any name for the fold flag (L1383).
11. **Nanda's "⊗ meaning elementwise addition" (L1381)** as printed.
12. **Firmness upgrades:** "Elhage proves/shows" or "exactly" for no privileged basis (say "asserts, for the idealised linear stream", L158); Olah's three claims as findings (they are "deliberately speculative", L220); Olah L242 without "have led us to believe"; Nanda L282 without "Intuitively"; Nanda L309 as Nanda's own result (it summarises Anthropic's Toy Model paper, L301).
13. **Our glosses as source claims:** "unit vector up to sign" as Olah's or Nanda's definition; "a polysemantic neuron is defined relative to the neuron basis" as Olah's words; "post-LN: what is added has passed through the norm" as Nanda's; "makes a naive edit-prediction wrong" as Nanda's; W9-B as "an Olah edge" or, unlabelled, as "a virtual weight"; L803 as an Elhage "virtual weight".
14. **Anything from the UNSEEN block as a source fact:** hidden state = residual stream; `output_hidden_states` indexing; steering or activation addition changing behaviour; what fine-tuning or RLHF change inside a model; facts about Qwen3, Llama 3, Gemma 3, Mistral models, base versus instruct; the RMSNorm formula; the standard-deviation convention; the contents of the logit-lens post, Elhage's forthcoming paper, or the papers Olah cites. "Mistral" at Nanda L1676 is a training library, not the model family.
