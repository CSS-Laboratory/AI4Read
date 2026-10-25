---
id: 2026-10-residual-stream/review/s2-check
type: fact-check
stage: S2
post: "What Is a Hidden State? The Residual Stream, Read and Written" (post 03)
checked: posts/2026-10-residual-stream/source-brief.md (S1)
output: posts/2026-10-residual-stream/source-brief.verified.md
date: 2026-10-25
checker: independent S2 fact-checker (fresh agent; did not write the brief)
counts: {critical: 1, major: 9, minor: 24}
gate: "PASS: 0 unchecked units (14/14 units, the trap block, the UNSEEN block and the 10 topic-card notes all checked)"
---

# S2 check: source brief for post 03

## Method
- **Quotes (script).** All 164 labelled quotes `Q[source:L, Nw]` were matched against the cited line span of the saved `.txt`, in two ways: (a) exact substring after collapsing whitespace, and (b) letters and digits only (NFKC, lowercased). Word counts were recomputed by splitting on whitespace. Result: 164/164 found in span by both methods; 164/164 word counts right; 0 over 25 words.
- **Visible-page check (script).** Every labelled quote and every quoted fragment in claim, trap and tension lines (611 fragments in all) was matched (letters and digits only) against the *visible* text of the saved `.html`, after removing `<!-- -->` comments, scripts and styles. This catches text that is in the file but not on the published page. Result: 3 Olah quotes are hidden (C1). Hidden text-layer lines: Olah L147-148, L249-254, L265, L267, L287, L455, L658; Elhage L303; none in Nanda.
- **Fragments not verbatim (script).** Quoted fragments in claim lines were also searched in all three `.txt` files. Every miss was read by hand. Most misses are ellipses, the brief's own phrases, or card quotes; the real misquotes are listed below.
- **Claims (by hand).** Every cited line and section was read in the `.txt`, and in the `.html` where the text layer is damaged. For each claim I compared the scope, the hedges, the referent of "this" or "it", the numbers and the firmness verb.
- **Numbers.** Every toy number in units 1-13 and the card's E-exercises was recomputed with numpy: W9-A sums and norms, W9-B read-shares, the W9-C scores and the margins at 0, 45, 90, 100, 120, 135, 150, 170 and 180 degrees, steering shifts, the 90-degree rotation, the three-direction interference, the logit-lens toy, the LayerNorm toy, the matrix M = [[2,1],[1,2]], 25x4 = 100, 4x768 = 3072, 12x64 = 768. All match.
- **Absences.** Each UNSEEN or "nowhere" claim was searched with grep over all three `.txt` files.
- **Scope.** Each Elhage citation was mapped to its section heading (`grep -n "^#"`) and compared with Kunhao's scope in `kunhao-input.md`: "only the sections on the residual stream as a communication channel, virtual weights, and 'no privileged basis'. Skip the attention-head algebra and induction heads".

## Verdict per unit
| Unit | Tag | Findings | Main evidence |
|---|---|---|---|
| Trap block | FIXED | m20, m21 | Olah L538, Nanda L415, L723 ("hidden layer"); Nanda L1551 (closest-point sense) |
| 1 Olah Claim 1 | FIXED | C1, M1, m1 | L249-254 and L265 hidden in the HTML; Nanda L259 first half dropped |
| 2 Olah Claim 2 | FIXED | m2, m3, m4 | L426 misquote; L669 "adjacent layers"; L634 unhedged line missing |
| 3 Olah Claim 3 | FIXED | M6, m5, m6 | Elhage L568 (induction heads); L536-538 summary; L273 missing |
| 4 Polysemanticity | FIXED | m7 | L700 defines a polysemantic *feature*; L196-197 |
| 5 Elhage stream = sum | FIXED | M5, m8, m9, m23 | L155 "we believe ... often dedicates subspaces"; L98 "very preliminary" |
| 6 Read/write, virtual weights | FIXED | M7, m10, m11, m12, m23 | L181 (excluded); L162 footnote split; W9-B toy versus trap |
| 7 Subspaces, bandwidth | FIXED | M8, m13 | L417 (excluded, and "might"); Nanda L282 "Intuitively", L301 |
| 8 No privileged basis | FIXED | m14, m23 | L158 asserts and does not derive; L581 is in Related Work |
| 9 Layer normalization | FIXED | m15, m23 | L1013-1023 out of scope; Nanda L816, L872 glosses |
| 10 Nanda stream | FIXED | M4, m16, m23 | no "skip connection" in Elhage; L596 "lives" |
| 11 Read/write, DLA | FIXED | M3 | "not necessarily a unit vector" is in no source |
| 12 Features as directions | FIXED | M1, M2, m17 | L216 referent; L259 half; "three definitions" |
| 13 Logit lens | FIXED | m18, m23 | Elhage L589-594, L629-635 in Related Work; L592 "in some sense" |
| 14 Editing, steering | FIXED | M9, m19 | L535-536 (induction section); Nanda L1458 adds noise |
| UNSEEN block | UNSEEN (confirmed) | m22 | "Mistral" at Nanda L1676 is a library; Dynalist link |
| Card notes 1-10 | CHECKED | m24 | 10 notes, not 9; verdicts below |

Tags: 0 OK, 14 FIXED, 0 DROP (single items inside units are dropped and marked "S2: DROP"). Unchecked units: **0**.

## Findings

### Critical (1)
**C1. Three Olah quotes and a structural claim come from text that is not on the published page.**
- Brief: unit 1, Q[olah:265, 7w] "Part of this claim is trivially true."; Q[olah:265, 18w] "The interesting part of the claim is that they can, with sufficient effort, be rigorously studied and understood."; Q[olah:252, 15w] "For us, the way out of the curse of dimensionality is features being individually understandable."; the hedge list ("part of the claim is "trivially true" (L265)"); the verb line ("concede ... that part of the claim is trivially true"); the trap "The claim has a trivially true part ... Only the second part is a bet". Root cause: brief header, "Leftover HTML comment marks ("-->") sit in the Olah text ... ignore them."
- Source: `olah-2020-zoom-in.html`. The text at txt L249-254 sits inside `<!--       <p>         Whether or not features are understandable isn't just a curiosity. ...`, and txt L265-267 inside `<!--        <p>Part of this claim is trivially true. ...`. Both blocks are commented out and do not render on distill.pub. The txt lines L255 and L269 ("-->") close them.
- Why critical: the brief cites words the published essay does not contain, and builds a firmness sorting and a trap on them.
- Fix: drop the three quotes, the hedge, the verb and the trap. Use the visible L229 instead, "They correspond to directions. They can be rigorously studied and understood.", and glossary L679 for "A direction can be an individual neuron". Never cite the hidden lines (all are listed in the verified brief's header). Done in the verified brief.

### Major (9)
**M1. Nanda L259 is cut so that he appears to reject Olah's vision claim.** (units 1 and 12)
- Brief, unit 1: "Nanda L254-259: "features as neurons" is "at best only slightly true for transformers" (he is answering exactly this kind of claim)." Unit 12 has the same half-quote.
- Source: nanda-2022-glossary.txt:259, "There is a decent amount of empirical evidence that this is mostly true of Inceptionv1, but this seems at best only slightly true for transformers."
- Fix: quote the whole sentence (25 words). Drop "he is answering exactly this kind of claim", which is our inference.

**M2. The quote at L216 is about something else.** (unit 12)
- Brief: "*Admits the limits:* in practice the description "is pretty imprecise" (L216)", listed as a limit of features as directions.
- Source: nanda:216, "In practice, this is a pretty imprecise description. Most features will be binary(-ish), but the model’s ability to tell will often be much more continuous". The referent is the binary-versus-continuous description (L207-215). The quoted words are also not verbatim (the source has "a pretty imprecise description").
- Fix: remove it from the limits of features as directions. Use it, verbatim, only for the binary-versus-continuous point.

**M3. A quotation that is in no source.** (unit 11)
- Brief, Tensions: "Nanda's L1415 ("not necessarily a unit vector") versus the post's choice of a unit u (ours)."
- Source: nanda:1415, "Projecting means “map $x \to x \cdot v$ for some fixed vector $v$. Projecting is sometimes specifically used when $v$ is a unit vector." The words "not necessarily a unit vector" occur nowhere in the three files.
- Fix: quote L1415's own words. The substance (v need not be a unit vector) stands.

**M4. An invented disagreement.** (unit 10)
- Brief, Tensions: "Nanda L580-581 against Elhage L148 on whether to read the stream as a series of skip connections."
- Source: elhage:148 describes blocks that read and write the stream and does not mention skip connections. The phrase "skip connection" does not occur in elhage-2021-framework.txt. Elhage L155 also prefers the stream view: "We prefer the residual stream terminology". Nanda:581 is the only source that weighs the skip-connection reading.
- Fix: drop the tension; both authors take the stream view.

**M5. Elhage's hedge is dropped, and a paraphrase is put in quotation marks.** (unit 5)
- Brief, Tensions: "Elhage's stream carries information "about tokens other than the present token" (L155)".
- Source: elhage:155, "we believe the residual stream often dedicates subspaces to tokens other than the present token".
- Fix: report it as Elhage's belief, with "often" and "dedicates subspaces to", quoted verbatim.

**M6. Scope: induction-head material.** (unit 3)
- Brief, Tensions: "Elhage L568 reports "analogous attention heads and circuits in large models"".
- Source: elhage:568, § Where Does This Leave Us?, "we'll find that large models form many induction heads, and that the basic building block of their construction is K-composition". Kunhao: "Skip the attention-head algebra and induction heads".
- Fix: drop the item.

**M7. Scope: attention-head algebra.** (unit 6)
- Brief, Numbers: "Attention-head output as a sum: W_O^H [r1; r2; ...] = sum_i W_O^{h_i} r^{h_i} (L181)."
- Source: elhage:181, § Attention Heads are Independent and Additive.
- Fix: drop it. The post does not need it.

**M8. Scope: attention-head algebra, with a dropped hedge.** (unit 7)
- Brief: "d_head/d_model "around 1/10 to 1/100" (L417)".
- Source: elhage:417, § Three Kinds of Composition, "typical values of d_\text{head} / d_\text{model} might vary from around 1/10 to 1/100".
- Fix: drop it (excluded section). If Kunhao restores it, keep "might vary".

**M9. Scope: the induction-head experiment.** (unit 14)
- Brief: "*Elhage:* an experimental recipe replaces a head's output ... (L535-536)", plus Q[elhage:535] and the related tension.
- Source: elhage:535-536, § Term Importance Analysis, in the induction-head part ("Algorithm for measuring marginal loss reduction of nth order terms"). The quote itself is verbatim.
- Fix: drop all three.

### Minor (24)
- **m1** (u1) Q[olah:242] begins "the typical case is that neurons ..." and drops the lead-in. Source: olah:242, "thousands of hours of studying individual neurons have led us to believe the typical case is". Fix: keep "have led us to believe".
- **m2** (u2) Brief: "technically ignore one ReLU" (L426). Source: olah:426, "this technically does ignore one ReLU non-linearity". Fix: quote it verbatim.
- **m3** (u2) The W9-B "edge" toy. Source: olah:669, "Two nodes have an edge between them if they are in adjacent layers." Fix: say "like an edge weight"; W9-B joins non-adjacent writers to a reader.
- **m4** (u2, balance) Olah's unhedged olah:634 is missing: "In fact, for small enough circuits, statements about their behavior become questions of mathematical reasoning." Fix: add it.
- **m5** (u3) Brief: the convergent-learning work is "cited by title only". Source: olah:536-538, "different neural networks can develop highly correlated neurons ... they learn similar representations at hidden layers", judged at L540. "Representation similarity" is not the source's phrase. Fix: corrected.
- **m6** (u3, balance) Olah's strongest unhedged evidence line is missing: olah:273, "Curve detecting neurons can be found in every non-trivial vision model we’ve carefully examined." Fix: add it next to "only ... anecdotal" (L547).
- **m7** (u4) Brief: "A polysemantic neuron is defined relative to the neuron basis (L700)". Source: olah:700 defines a polysemantic *feature*, "A feature that responds to multiple unrelated latent variables". Also, "superposition is the reason the "direction, not neuron" wording exists" is our inference; L196-197 names polysemantic neurons. Fix: label both as ours.
- **m8** (u5) A paraphrase in quotation marks: "it does no processing, all layers communicate through it". Source: elhage:155, "since it doesn't do any processing itself and all layers communicate through it". Fix: quote it verbatim.
- **m9** (u5) A hedge is missing from the concessions. Source: elhage:98, "we attempt to take initial, very preliminary steps towards reverse-engineering transformers". Fix: add it.
- **m10** (u6) A claim line quotes across an inlined footnote, "are the product of the output weights of one layer with the input weights of another", which breaks the brief's own rule (elhage:162: "input weightsNote that for attention layers ... of another"). Fix: quote the two parts separately.
- **m11** (u6) The unit 6 toy says the W9-B dot products "are the entries of a "virtual weight" matrix in the 1x1 case", while the unit 6 trap says W9-B is a read-split. Also, L803 is labelled "example of a virtual weight", but elhage:803 does not use the term. Fix: pick one reading of W9-B and label it ours; label L803 ours.
- **m12** (u6) Brief: "the clean statement is for the attention-only case ("linear if one freezes the attention patterns", L121)". But elhage:121 concerns end-to-end paths of attention-only models, while the stream's linearity (L157-158) is stated in general. Fix: clarified.
- **m13** (u7) Two attribution slips. The brief has "just used for 'storage'" without the source's lead-in (nanda:282, "Intuitively, bottleneck superposition is just used for “storage”"). And the sparsity condition (nanda:309) is Nanda's summary of "Anthropic’s Toy Model of Superposition paper" (nanda:301). Fix: keep "Intuitively"; attribute L309 to the paper.
- **m14** (u8 and card note 9) Firmness words. The brief has "Elhage's invariance is shown", "is exact" and "the sources prove it". Source: elhage:158 asserts it in one sentence, "we could rotate it by rotating all the matrices interacting with it, without changing model behavior". Fix: use "asserts, for the idealised linear stream".
- **m15** (u9) Two glosses. Brief: "the attention-only models in TransformerLens". Source: nanda:816, "A transformer variant studied in A Mathematical Framework". Brief: "In post-LayerNorm models what is added has passed through the norm (L872)". Nanda says only "when writing to the residual stream (ie at layer output)". Fix: quote Nanda's words.
- **m16** (u10) Brief: "live in the same space" (L596). Source: nanda:596, "has the same dimension and lives in the same space". Fix: quote it verbatim.
- **m17** (u12) Brief: ""Feature" has three definitions across the sources (Olah L694, Nanda L104, Elhage uses none)." That is two definitions. Fix: corrected.
- **m18** (u13) Brief: "*Elhage (describes, no hedge)*". Source: elhage:592, "to look at how model predictions evolve in some sense", and elhage:594, "Our approach could be seen as". Fix: note the hedges.
- **m19** (u14) Brief: "Edit in these sources means replace, zero or patch an activation, or change weights." Source: nanda:1458, causal tracing, "add significant noise to their token embeddings", which is an additive (random) intervention. Also, "makes a naive edit-prediction wrong" is ours (nanda:1375 reports only the compensation). Fix: narrowed and labelled.
- **m20** (trap block) Two absence claims, re-searched. Trap 2 lists two "hidden" near-misses; there are also olah:538 ("similar representations at hidden layers"), nanda:415 and nanda:723. Trap 5 says the closest-point sense is "not used by any source here", but nanda:1551 removes "the component in the $$v$$ direction" (PCA entry, formula malformed). Fix: lists widened; trap 5 narrowed to "not for the residual stream".
- **m21** (header) Three header errors. "Olah L174-184" is called inlined footnotes, but it is the Schwann figure and its caption. The HTML for L669 uses `<sub>`/`<sup>` tags, not `&#8321;` entities. The damaged-line list misses nanda:626, 833, 854, 955, 1167 and 1172, and L1383 lacks two names, not one. Fix: corrected in the header.
- **m22** (UNSEEN block) Two notes on absences. "Anything on ... Mistral": the word occurs at nanda:1676, "Trained during the development of their Mistral library" (Stanford CRFM), not the model family. The saved page's "Dynalist" link is https://neelnanda.io/glossary, the URL that redirected to the saved page, so it does not reach the Dynalist original. Fix: noted. All other absences are confirmed.
- **m23** (units 1, 5, 6, 8, 9, 10, 13 and T9) Elhage lines outside Kunhao's named sections, in material not explicitly excluded. They are: L793 and L788-805 (§ MLP Layers); L594 and L635 (§ Related Work); L1005 (§ Model Details); L581 (§ Related Work, Circuits: its privileged-basis sentence is on topic); L1013-1023 (§ Handling Layer Normalization appendix; the brief flags this itself); L857-862 and L1008 (positional mechanism); L589-594 and L629-635 (Related Work: logit lens, Bertology); L226 in T9 (attention-head algebra). Fix: marked in each unit; listed in the writer-must-not-use list, item 8, "unless Kunhao widens the scope". The limit statements (L95-102, L136-142, L562-572) may be used only to state limits.
- **m24** (notes section) The brief has ten numbered notes; the S2 task said nine. In note 1, only card T2 (not §12) says the sources "do not mention RMSNorm". The lists in notes 3 and 5 are incomplete. Fix: verdicts written after each note.

## Topic-card notes: verdicts
| # | Brief's note | Verdict | Evidence |
|---|---|---|---|
| 1 | RMSNorm is in the glossary | **Brief right; card wrong** | nanda:824-829 "RMSNorm aka Root Mean Square Norm: A variant of LayerNorm ..." (only card T2 says the sources do not mention it; §12 proposes the fetch) |
| 2 | "Not linear" is Nanda L702, not Elhage L1019 | **Brief right** | elhage:1019 "everything except for normalizing by variance, layer normalization applies a fixed affine transformation"; nanda:702 "the “divide by the standard deviation” step is non-linear" |
| 3 | "Hidden" is not absent | **Both right** | The card's "hidden state does not occur" is true; the brief's addition is right but incomplete (olah:538, nanda:415, nanda:723) |
| 4 | Cancellation is at L172, not L168 | **Brief right** | elhage:168 asserts persistence with no hedge; elhage:172 "hints ... may ... reading in information and writing out the negative version" |
| 5 | More than one damaged entry | **Brief right** (the card understates) | The brief's list is still short: nanda:626, 833, 854, 955, 1167, 1172 |
| 6 | TransformerLens folding is partly sourced | **Brief right** | nanda:1380, 1383 "automatically folded in"; centring appears in neither source |
| 7 | The virtual-weight label on W9-B is loose | **Brief right in substance** | elhage:162 (a weight product); it holds only if a1 is read as output weights with activation 1 (ours); the brief's own unit 6 toy said the opposite |
| 8 | "Unit vector up to sign" is ours | **Brief right** | olah:194, 679 have no unit or sign; nanda:1415 "sometimes ... unit"; the card puts it in the post's-sense column, so it needs an "ours" label only |
| 9 | Rotation invariance is not simply true | **Brief right, one word too strong** | elhage:158 asserts it (not "prove"); nanda:243 gives the reason, nanda:245 the caveat "slightly privileged" |
| 10 | Clause 5 is stronger than Olah | **Brief right; the card agrees** | olah:636-637 "it seems like ... If so, perhaps"; card clause 5 row and R3 |

No note was found where the card is right and the brief wrong.

## Checked and found correct (summary)
- All 164 quotes: verbatim, in span, at most 25 words. 161 are on the published page; the 3 that are not are C1.
- All line and section locations for the unit claims, apart from the misplacements listed above. The section headings match the saved pages.
- All toy numbers and the card's E1-E5 and open-question numbers.
- All absence claims: "hidden state", `output_hidden_states`, steering, activation addition, steering vectors, what fine-tuning or RLHF change, Qwen3, Llama 3, Gemma 3 and Mistral models, base versus instruct, "bus", the RMSNorm formula, and the standard-deviation convention. All are absent. The Nanda corruption at L1424, L1410, L1417, L1391 and L1383 is confirmed in the HTML.
- Firmness sorting for Olah's three claims (apart from C1), Elhage's assertions and hedges at L155-172, and Nanda's hypothesis, intuition and flat lines (L135, L199-203, L1096).

## Gate
0 unchecked units. **S2 gate: PASS.** All critical and major findings are corrected in `source-brief.verified.md`, which ends with a writer-must-not-use list. The Elhage scope items (M6-M9 dropped; m23 held for Kunhao) need Kunhao's decision only if he wants that material back.

## S2 addendum (2026-10-25): unit 15, MacKay on the multiple-access channel (request Q1); Q2 closed
Checker: independent fact-checker (fresh agent). Source: `sources/mackay-2003-itila.pdf` (author's on-screen PDF, fourth printing), read in `pdftotext` per page and as rendered images (PDF p. 250 at 200 and 400 dpi for figure 15.3); extract `sources/mackay-2003-mac.txt`. Printed = PDF - 12 confirmed on all three pages (236/248, 237/249, 238/250).

| Unit | Tag | Findings | Main evidence |
|---|---|---|---|
| 15 MacKay multiple-access channel | FIXED (new unit) | a1, a2, a3 | Ex. 15.18, p. 237; Fig. 15.3 and caption, p. 238; Ex. 15.19, p. 237 |

- **Quotes (script).** 15 quotes, each matched against the `pdftotext` text of its own PDF page: 13/15 exact after whitespace collapse, 15/15 letters-and-digits only (the 2 misses are R_A, R_B set as subscripts); word counts recomputed, all at most 25. Q12-Q15 (Ex. 15.19 line and caption) are split by the two-column `-layout` extract but are verbatim in the raw page text and visible in the image.
- **Figure 15.3 (read from the image).** (a) box P(y|x(A), x(B)), two inputs, one output; (b) table 0 1 / 1 2; (c) shaded "Achievable" pentagon with corners (0,0), (1,0), (1,1/2), (1/2,1), (0,1), dashed diagonal R_A + R_B = 1, dashed lines at 1/2. No units, no word "capacity". The sum 3/2 on the sloped edge is our reading (checked with exact fractions); the text states only "cannot be two bits" and "easy ... one bit", and asks whether R_A + R_B > 1.
- **a1 (request framing; major if it reached the post: scope).** Q1 says the set-up is senders "whose output is the sum of the inputs". MacKay's general channel is any P(y | x(A), x(B)) (caption 15.3a); only the "simple model system" adds. Fix: in unit 15, "MacKay's simplest example is an adder".
- **a2 (request framing; major if it reached the post: unsupported term).** Q1 asks for "one line that the topic is studied through a capacity region". On these pages "capacity region" is used only for the broadcast channel (Ex. 15.19, p. 237; p. 238); the multiple-access figure is "The achievable region". Fix: unit 15 says "achievable region" and forbids any capacity result.
- **a3 (minor).** Q1 cites p. 237 for the whole unit; the figure is on p. 238. Fix: both pages given; cite by exercise number (preface p. xi: exercise numbers unchanged across printings).
- **Traps recorded in unit 15.** Exercise in a "Further Exercises" chapter, rated [3] with no solution page; no theorem, no proof, "The answer is indicated in figure 15.3". "There is no noise." The users "cannot hear the output" (a disanalogy with layers that read the stream: ours). No neural networks on pp. 236-238, but the book has Part V "Neural networks" (p. 467), so "MacKay never mentions neural networks" would be false. Ratzer and MacKay (2003) is UNSEEN.
- **Link.** Structural analogy (ours): several writers, one additive medium, a reader who sees only the sum (output 1 = (0,1) or (1,0)). Not same-math; no rate or capacity transfers to the stream (unit 7).
- **Q2 closed.** No Shannon text on "bandwidth" is saved. Writer-must-not-use item 15 added: no contrast between Elhage's "bandwidth" and Shannon's. Note for the orchestrator: unit 7's trap line "it is not a rate in Hertz" is itself an unsourced gloss and is now covered by item 15. MacKay does define bandwidth "(measured in Hertz)" in ch. 11 (p. 178 by the index; PDF text checked), but that is MacKay, not Shannon, and was not checked as a unit; do not use it without a new S2 unit.
- **Counts for this addendum:** critical 0, major 0 in the brief (2 major-if-used in the request framing, both blocked in unit 15), minor 1. **Gate still PASS:** 15/15 units checked.
