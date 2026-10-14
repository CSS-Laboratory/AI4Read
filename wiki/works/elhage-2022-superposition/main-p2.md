---
id: elhage-2022-superposition/main-p2
work: elhage-2022-superposition
unit: part 2/2 — from "Superposition in a Privileged Basis" to the appendices
pages: unknown (HTML; cited by section heading)
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 22
pipeline_version: 0.1
---
# Toy Models of Superposition, part 2: privileged basis, computation, strategy, discussion, appendices

## L0 — One line
Once neurons impose a privileged basis (axes that matter), toy networks show neurons that hold one feature (monosemantic) or several (polysemantic) and can compute absolute value in superposition (more features than neurons); the authors argue superposition is closely tied to enumerating all features, which they see as a promising tool for safety claims.

## L1 — The gist (≤ 120 words)
Part 1 studied superposition without a privileged basis. This part adds a ReLU hidden layer and asks whether features align with neurons and whether computation can happen in superposition. Answers: neurons shift from monosemantic to polysemantic as sparsity rises, and, once features are sparse enough, a model computing abs(x) uses superposition, including an "asymmetric" motif. The authors then argue that "solving superposition" (enumerating features) is a promising route to safety-relevant interpretability, and compare three routes: superposition-free models, overcomplete-basis recovery, hybrids. They then relate the work to real models, open questions, related fields and outside comments. Appendices cover nonlinear compression and a compressed-sensing lower bound.

**Prerequisites:** ReLU networks; privileged basis (a basis whose axes matter, e.g. neurons); monosemantic vs polysemantic neuron (one feature vs several); superposition (more features than dimensions or neurons); overcomplete basis (more feature directions than dimensions); the part-1 toy model (sparse features $x$, hidden dimension $m<n$, interference); dot products and rotations; basic sparse coding idea.

## L2 — Key ideas
- A ReLU on the hidden layer gives a privileged basis, so $W$ can be read directly as feature→neuron weights. Neurons shift from monosemantic to polysemantic as sparsity increases (§ "Superposition in a Privileged Basis").
- The simple ReLU-hidden toy model is weak: it can "simulate identity", avoiding the ReLU through positive biases or by averaging many features (§ "Limitations…").
- A model that must compute $\text{abs}(x)$ cannot avoid its ReLUs. At high sparsity it still approximately computes abs for more features than neurons, so computation can occur in superposition (§ "Computation in Superposition").
- Asymmetric superposition plus inhibition turns positive interference (which could greatly raise the loss) into negative interference with limited consequences (§ "The Asymmetric Superposition Motif").
- Strategic claim: the ability to enumerate all features is linked to "solving superposition". Three routes exist (no-superposition models, overcomplete basis, hybrids), and each is hard for competitive models (§ "The Strategic Picture").
- Phase changes give some hope that superposition could be removed entirely, not just reduced (§ "Additional Considerations").
- The toy model's predictions are consistent with observed polysemanticity, to the authors' knowledge (InceptionV1 depth trend, early MLP neurons). Geometry and learning dynamics are much less certain to transfer (§ "Discussion").
- Compressed-sensing lower bounds can be read as an upper bound on superposition in the toy model: the number of features is linear in $m$, modulated by sparsity (§ "Compressed Sensing"; appendix).

## L3 — Walkthrough

### Superposition in a Privileged Basis
**Setup.** Part 1's model had no privileged basis: for any orthogonal $O$, $W'=OW$ gives an identical model because $(OW)^T(OW)=W^TW$ (§ "Superposition in a Privileged Basis"). The authors also want representations where neurons impose a privileged basis (transformer MLP layers, conv-net neurons). They focus on adding an activation function to the hidden layer (L1 regularization is the other option they name) (same §). The "ReLU hidden layer" model:

$$h=\text{ReLU}(Wx),\qquad x'=\text{ReLU}(W^Th+b)$$

It is trained on the same data. $W$ is now directly interpretable as a map from features to basis-aligned neurons (same §).

*Intuition note.* Without a ReLU, any rotation of the hidden space is invisible to the loss, so individual coordinates carry no special meaning. With a ReLU, coordinates matter, so asking which neuron holds which feature becomes a real question.

**Visualizing in terms of neurons.** A per-neuron stacked bar plot shows each column of $W$. Each rectangle is one weight (height = absolute value, colour = feature, negatives below the axis). Polysemantic neurons are those with more than one weight (§ "Visualizing Superposition in Terms of Neurons").

**Experiment.** $n=10$, $m=5$, $I^i=0.75^i$, varying sparsity. For each model shown, 1000 models were trained and the lowest-loss one is displayed. Ranges of sparsity exist where the optimum has the same weight configuration across all models (same §).

**Result.** There is a shift from monosemantic to polysemantic neurons as sparsity increases. Both kinds can coexist in one model. The authors say it looks like a neuron-level phase change, though they note it is unclear how to formalize this. Features typically correspond to sets of neurons. Neurons go from monosemantic, to a few features, to gradually more. How much of this generalizes to real models is unclear (same §).

*Intuition note.* In dense regimes a neuron can just be a feature. As features get rarer, sharing a neuron costs little interference, so neurons take on several features.

**Limitation: simulating identity.** The ReLU hidden layer has no useful role here, and the model avoids it if it can. With a bias it sets all biases positive, so neurons act linearly. Without a bias but with enough features, it simulates a bias by averaging over many features. The model uses the ReLU only if forced (§ "Limitations of The ReLU Hidden Layer Toy Model…").

### Computation in Superposition
**Idea.** Input and output layers stand for a hypothetical disentangled model. The smaller hidden layer stands for the observed model, which might use superposition. The model must compute a simple nonlinear function, so it must use the hidden nonlinearity (§ "Computation in Superposition"). The target is $y=\text{abs}(x)$, and a simple ReLU implementation exists:

$$\text{abs}(x)=\text{ReLU}(x)+\text{ReLU}(-x)$$

**Setup.** Each $x_i$ is 0 with probability $S_i$; otherwise it is uniform on $[-1,1]$. Target $y=\text{abs}(x)$. Weights are no longer tied:

$$h=\text{ReLU}(W_1x),\qquad y'=\text{ReLU}(W_2h+b)$$

The loss is still mean squared error weighted by feature importance $I_i$ (§ "Experiment Setup"). Because of the ReLU and untied weights, one cannot simply study $W_2^TW_1$ or columns of $W_1$. The authors plan to visualize neurons instead. Each hidden unit can be rescaled (row of $W_1$ by $\alpha$, column of $W_2$ by $\alpha^{-1}$) without changing the model. Plots normalize so each unit's largest $W_1$ weight has magnitude 1 (§ "Basic Results").

**Basic result ($n=3$, $m=6$).** Without superposition, abs of one feature needs two neurons. The trained model builds for each $x_i$ a "positive side" neuron $\text{ReLU}(x_i)$ and a "negative side" neuron $\text{ReLU}(-x_i)$ and adds them (§ "Basic Results").

**Superposition vs sparsity ($n=100$, $m=40$, $I_i=0.8^i$).** In the dense regime each neuron represents one feature and feature values can be read off neuron activations. Once features are sparse enough, the model represents more features than neurons. So neural networks can perform computation on data held in superposition (§ "Superposition vs Sparsity"). Losses across sparsity levels are not comparable, because changing sparsity changes the task (same §).

*Intuition note.* Dense: one feature per neuron pair. Sparse: neurons are shared and the computation is only approximated (plausibly tolerable because features seldom co-occur). The ReLUs are still doing the abs computation, not being bypassed.

**Qualitative echoes of real networks** (§ "Superposition vs Sparsity"):
- In some regimes many neurons encode pure features while a subset are highly polysemantic. Neurons for the most important features (left of the plot) tend to be monosemantic. The authors compare this to vision-model layers with "mostly pure" feature neurons.
- Many neurons have one "primary" feature (large weight) plus "secondary" features (smaller weights). The largest activations track the primary feature; lower activations are more polysemantic. The authors say this matches findings about language-model neurons, calling the match "only suggestive".

### The Asymmetric Superposition Motif
The authors work through a model with limited superposition. Most weights implement abs in the usual way. A few neurons form two instances of **asymmetric superposition and inhibition**, each with two neurons (§ "The Asymmetric Superposition Motif"):
- *Neuron 1 (asymmetric superposition).* In ordinary superposition one stores features with equal-magnitude weights (e.g. $W=[1,-1]$) and reads out with equal weights ($[1,1]$). In asymmetric superposition one stores them with different magnitudes (e.g. $[2,-\tfrac12]$) and reads out with reciprocal weights ($[\tfrac12,2]$). One feature then interferes heavily with the other, but not the reverse.
- *Neuron 2 (inhibition).* It strongly inhibits the feature where positive interference would occur. This converts positive interference (potentially large loss) into negative interference (limited effect because of the output ReLU).

A few remaining weights are unexplained; the authors believe they are effectively small conditional biases (same §).

### The Strategic Picture of Superposition
The interest is partly pragmatic: superposition is linked to using interpretability for claims about AI safety (§ "The Strategic Picture of Superposition").

**Safety, interpretability and "solving superposition".** The authors want confidence that models never do behaviors such as "deliberately deceive". A promising tool would be the ability to enumerate over all features, a universal quantifier over the units of computation. A footnote says it may be possible to build more subtle claims, such as that all features of deceptive behavior do not participate in particular circuits. It might also address "unknown unknowns". A footnote notes that showing no "deception feature" exists is not the goal, since the authors expect models that represent the world to represent unsavory behaviors (§ "Safety, Interpretability, & 'Solving Superposition'").

Link to superposition:
- With a privileged basis and no superposition, enumerating features means enumerating neurons.
- Superposition also makes it harder to find interpretable directions without a privileged basis. Without superposition one could try something like Gram–Schmidt (find an interpretable direction, remove it, repeat); with superposition you cannot simply remove a direction, even a known feature direction.
- Conversely, if one can enumerate features, compressed sensing using the feature directions can (with high probability) "unfold" superposed activations into a larger non-superposed model.

A "solution to superposition" is any method that enumerates features, equivalently unfolds activations. The authors say it is equivalent to, or necessary for, several other properties:
- **Decomposing activation space** into independently understandable components, like variables in program memory.
- **Describing activations in pure features** (e.g. a dog-head activation as floppy ear, golden fur, snout).
- **Understanding weights (circuit analysis)**, where weights can typically be understood only when they connect understandable, non-polysemantic units.
- **Basic methods become unreliable.** Cosine similarity to known deceptive examples can mislead, because unrelated features get positive dot products.

**Three ways out.** (1) Create models without superposition. (2) Find an overcomplete basis describing how features are represented. (3) Hybrids that change models to make a second-stage analysis easier. The authors' sense is that all are possible if one does not need a competitive model (they believe so for the toy models) and that all look very difficult for serious networks and large language models. A "bright spot": results suggest superposition and polysemanticity are phases with sharp transitions, so a regime without them may exist for every model. The question is whether the cost is too high (§ "Three Ways Out").

**Approach 1: models without superposition.**
- In toy models, add an L1 term $\lambda\|h\|_1$ on hidden activations. This removes superposition at the price of higher loss, and can be read as killing features below an importance threshold (§ "Approach 1").
- Models likely benefit substantially from superposition. The sparser features are, the more can be packed per neuron. An example is that language models know people with modest public presence, who presumably occur less than once in a million tokens (same §).
- A superposition model with $n$ neurons likely matches a monosemantic model with $kn$ neurons. But flops, not neurons, are the fundamental constraint, and in common architectures the two correspond strictly.
- **Mixture of Experts (MoE)** breaks this link. Neurons are grouped in experts that activate rarely, so the model has $k\times$ more neurons at similar flops if only $1/k$ activate, in blocks. The authors' preliminary comparison (loss reduction per activation frequency) seems to suggest superposition is not optimal when only active neurons cost flops, though it asymptotically becomes as good as dedicated dimensions. They expect MoE models to have less superposition because MoE uses up the gap between neuron sparsity and feature sparsity. They stress that MoE is an example showing superposition-free competitive models remain plausible, not a recommendation.

**Approach 2: overcomplete basis (sparse coding / dictionary learning).** Given hidden activations $H\sim[d,m]$ over $d$ stimuli and $n$ assumed features, find $A\sim[d,n]$ (sparse) and $B\sim[n,m]$ (§ "Approach 2", footnote). Advantage: model performance is untouched. Difficulties:
- The number of features is not known.
- "Virtual neurons" are not part of the model's surface structure.
- Engineering scale: perhaps millions of neurons by billions of tokens, factored with a thousand or more times as many features.
- Interference no longer pushes toward less superposition, since training has already baked it in.

**Approach 3: hybrids.** One can probably reduce superposition a little at no performance cost (e.g. L1 without architecture change): the loss derivative with respect to the amount of superposition should be zero at the model's chosen level, so a margin exists. Alternatively, architecture changes might make overcomplete bases easier to find (§ "Approach 3").

**Additional considerations.**
- *Phase changes as cause for hope:* if superposition is a phase, a regime exists where it totally disappears.
- *A superposition-free model, even a non-performant one,* would be a ground truth for studying superposition in normal models. The research risk is mainly in making performant ones.
- *Local bases are not enough:* local orthogonal bases for co-occurring features help on narrow sub-distributions. Safety claims need accounts valid on the full distribution and off-distribution.

*Intuition note.* If each feature has a direction in a space with fewer dimensions than features, you cannot read features off coordinates. A "solution" means recovering the feature list, either by building models that never mix features or by decoding them afterwards.

### Discussion
**Does superposition exist in real models?** Best validation is consistency with observed polysemanticity (§ "To What Extent Does Superposition Exist in Real Models?"):
- Polysemantic neurons exist (they form in the third model).
- Clean and polysemantic neurons coexist in one layer.
- InceptionV1 has more polysemantic neurons in later layers. Natural explanation: higher-level features are rarer, so sparser. The model predicts superposition rises with sparsity.
- In the authors' experience, early transformer MLP neurons are often extremely polysemantic. If the first MLP layer's goal is to separate interpretations of a token (e.g. "die" in English/German/Dutch/Afrikaans), such features would be very sparse and the toy model would predict much polysemanticity.

The authors' intuition: superposition, monosemantic vs polysemantic neurons, and perhaps the link to adversarial examples likely generalize. Geometry and learning-dynamics results are "much more uncertain".

**Open questions** (§ "Open Questions"), summarized: a statistical test for superposition; how to control whether it occurs (L1 on activations, adversarial training, activation function — judged the most important question); closed-form solutions (Saxe et al. for linear nets; partial progress for $n=2$, $m=1$); realism of toy models; estimating real models' importance and sparsity curves; whether scale removes superposition; most principled definitions; how much understanding the interpretable fraction gives; how many features fit in superposition (compressed sensing bounds); link of phase changes to compressed sensing; link to non-robust features (Goh); which computations can be done in superposition; effect of correlated or anti-correlated features; whether models use nonlinear representations.

### Related Work
- **Interpretable features and superposition history** (§ "Related Work"): Arora et al. suggested word embeddings of multi-sense words may superpose sense vectors, and proposed sparse "atoms of discourse". Cheung et al.'s "model level" superposition (multiple independent models in one parameter set) can be seen as feature-level superposition of highly correlated sets of features.
- **Disentanglement:** it aims to impose a strong privileged basis on rotationally invariant representations. For neurons the basis is privileged by default, so polysemanticity is an anomaly and superposition a hypothesis explaining it. If superposition is true, it may be a reason disentanglement is hard, since many sparse, individually unimportant features may collectively matter. A footnote: Gaussian latent priors might force superposition, because sums of many sparse variables look Gaussian.
- **Compressed sensing:** differences listed (§ "Compressed Sensing"): the toy model uses a single layer, not arbitrary algorithms; sparsity is a zero-probability, not a count of non-zeros; it learns its embedding matrix instead of needing an incoherent one; features have unequal importance. In various settings an $n$-dimensional $k$-sparse vector can be recovered from an $m$-dimensional projection if and only if $m=\Omega(k\log(n/k))$. With $k=O((1-S)n)$ this becomes $m=\Omega(-n(1-S)\log(1-S))$. So the number of features is linear in $m$, modulated by sparsity. The authors read $-\log(1-S)$ as surprisal times the expected number of non-zeros. They note the bounds allow superposition to rise sharply with sparsity, and hope that is a proof artifact. Compressed sensing also shows sharp phase changes (in the large-dimension limit), and the parallel is "suspicious", though not obviously linked.
- **Sparse coding:** probably the most natural mathematical form of "solving superposition". Sharkey et al. had preliminary success extracting features from toy-model superposition with a sparse autoencoder.
- **Neural coding:** the authors separate *decomposability* (independent features coded separately) from *superposition* (more features than neurons, with interference if features co-occur). A decomposable linear code with orthogonal feature vectors can be fully distributed (every neuron polysemantic) and yet have no more features than dimensions, i.e. no superposition. They stress feature co-occurrence as central. Their absolute-value result suggests codes under moderate compression can still support computation. They also say they do not engage with the binding problem.
- **Additional connections:** vector symbolic architectures and hyperdimensional computing; frames (the "Mercedes-Benz Frame" is equivalent to the triangular geometry sometimes observed).

### Comments & Replications (outside voices)
- **Sachan (Redwood):** replicated the plots in two earlier sections plus one geometry plot; phase diagrams differ by activation function.
- **McGrath (DeepMind):** solves the expected loss exactly for $n=2$, $m=1$ (ignoring biases) by writing sparse inputs with delta functions and replacing the ReLU with a domain restriction: $\int_D\text{ReLU}(f(x))\,dx=\int_{D\cap f(x)>0}f(x)\,dx$. He finds a new "confused feature" phase $W_1\simeq W_2\simeq\tfrac1{\sqrt2}$ at low sparsity with both features important, with no correlation needed. Some loss surfaces have two minima. The transition between the minima of his Figures 1a and 1b is continuous (explaining the "blurry" region of the phase diagram), while the antipodal-to-confused transition appears discontinuous.
- **Wu & Mossing, Becker-Kahn, Hobbhahn:** replications of basic results.
- **Jermyn, Hubinger, Schiefer:** report ways to engineer monosemanticity in toy models, suggesting that, at least in some limits, monosemanticity may not cost performance.
- **Henighan & Olah:** more feature "pressure" and longer training seem to give cleaner polytope structure.
- **Sharkey et al.:** a one-layer sparse autoencoder with an L1 penalty recovered toy ground-truth features almost exactly. Results on a small language model were inconclusive.
- **Nanda:** the Othello-GPT board state is linearly represented as "my colour" vs "opponent's colour". Chris Olah had predicted a linear representation under a different feature set, so he reads this as a natural experiment supporting the linear representation hypothesis.
- **Zhang:** feature dimensionality $D_i=\frac{\|W_i\|^2}{\sum_j(\hat W_i\cdot W_j)^2}$ relates to the leverage score of row $W_i$ of an $n\times d$ matrix:
$$\tau_i=\max_{\|x\|_2=1}\frac{\langle W_i,x\rangle^2}{\sum_{j=1}^n\langle W_j,x\rangle^2}$$
The denominator equals $\|Wx\|_2^2$. A row orthogonal to all others has $\tau_i=1$. Leverage scores sum to the rank ($d$ for full-rank tall matrices). If the vectors are in isotropic position (variance $\langle W_j,x\rangle^2\approx1$ in every direction), the best $x$ is $W_i$ itself and $\tau_i$ recovers $D_i$. This explains why the $D_i$ roughly sum to $d$ when features are packed efficiently.

### Appendix: Nonlinear Compression
Models are unlikely to use nonlinear compression pervasively, for three reasons: the model must decompress before computing (most computation is linear); such schemes need fine-tuned approximations of discontinuities and are hard to learn; and they probably need enough neurons that the benefit over superposition is small (§ "Nonlinear Compression"). Example: compress two $[0,1)$ values $x,y$ into one:
$$t=\frac{\lfloor Zx\rfloor+y}{Z}$$
It quantizes $x$ with integer $Z$ so the precision of $t$ is split between $x$ and $y$. The floor and fmod discontinuities can be replaced by steep linear segments of width $\epsilon$. Even with $\epsilon$ as large as 0.1 and $Z$ as small as 3, it beats linear compression (picking one dimension or averaging) on dense uniform data in MSE. By the authors' count (each line segment takes two neurons), ReLU networks need 12 neurons per $Z$ segment, so it only starts to beat linear compression at a combined 36 neurons for compression and decompression. They suspect scaling favors superposition, but call this just intuition. Nonlinear directions could still be reverse-engineered like other circuits.

### Appendix: Compressed sensing lower bound
Let $T(x)=\text{ReLU}(W_2W_1x-b)$ with $W_1\in\mathbb R^{m\times n}$, $W_2\in\mathbb R^{n\times m}$ (§ "Connection between compressed sensing lower bounds and the toy model").

**Theorem 1.** If the toy model recovers all $x$ with $\|T(x)-x\|_2\le\varepsilon$ for sufficiently small $\varepsilon$, and $W_1$ has the $(\delta,k)$ restricted isometry property, then $m=\Omega(k\log(n/k))$.

**Lemma 1.** Under these conditions, a compressed sensing algorithm $f(y):\mathbb R^m\to\mathbb R^n$ exists for the measurement matrix $W_1$. *Proof sketch (as given):* (1) compute $\tilde x=\text{ReLU}(W_2y-b)=T(x)$, so $\|T(x)-x\|_2\le\varepsilon$; (2) keep only the $k$ largest entries to get $\tilde x'$; (3) solve $\min_{x'}\|x'-\tilde x'\|$ subject to $W_1x'=y$, which is convex since the supports match. If $\varepsilon$ is smaller than the $(k+1)$th largest entry of $x$, $\tilde x$ and the nearest $k$-sparse vector to $x$ share a support, so the solution is the nearest $k$-sparse vector. Approximation factor 1.

**Theorem 2** (Do Ba, Indyk, Price, Woodruff, Cor. 3.1). For a measurement matrix with the restricted isometry property, a sparse-recovery algorithm with $\|x-\hat x\|_1\le C(k)\min_{\|x'\|_0\le k}\|x-x'\|_1$ and $C(k)=O(1)$ exists only if $m=\Omega(k\log(n/k))$. Theorem 1 follows from Lemma 1 and Theorem 2.

*Intuition note.* If the toy autoencoder recovers sparse inputs, it is a (weak) compressed-sensing decoder. Known lower bounds on measurement count then cap how many features $m$ dimensions can hold.

## Toy example (ours, not from the text)
*Abs by two ReLUs.* One feature, $x=-0.6$. Neuron A $=\text{ReLU}(x)=\text{ReLU}(-0.6)=0$. Neuron B $=\text{ReLU}(-x)=\text{ReLU}(0.6)=0.6$. Output $=0+0.6=0.6=\text{abs}(-0.6)$. For $x=0.6$: A $=0.6$, B $=0$, output $0.6$. So $n=3$ features need $2\times3=6$ neurons without superposition, matching the paper's $m=6$.

*Why positive interference hurts more.* Suppose feature 2 is truly 0 and another feature leaks into its output pre-activation. If the leak is $+0.4$: output $\text{ReLU}(0.4)=0.4$, squared error $0.16$. If the leak is $-0.4$: output $\text{ReLU}(-0.4)=0$, squared error $0$. Inhibition aims to turn the first case into the second.

## Concepts
- [[superposition]] — more features than dimensions or neurons, at cost of interference when features co-occur (§ "Theories of Neural Coding…")
- [[polysemantic-monosemantic]] — a neuron with more than one weight/feature vs one dedicated to one feature (§ "Visualizing Superposition in Terms of Neurons")
- [[privileged-basis]] (new) — a basis whose axes matter, e.g. because activation functions act per neuron, unlike rotation-invariant embeddings (§ "Superposition in a Privileged Basis")
- [[computation-in-superposition]] (new) — computing a nonlinear function (abs) on features stored in superposition (§ "Computation in Superposition")
- [[asymmetric-superposition]] (new) — unequal stored weights with reciprocal readout, plus inhibition, to make interference negative (§ "The Asymmetric Superposition Motif")
- [[solving-superposition]] (new) — any method enabling feature enumeration/unfolding activations (§ "Safety, Interpretability…")
- [[sparse-autoencoder]] — dictionary learning on activations to find overcomplete feature directions (§ "Approach 2"; Sharkey comment)
- [[mixture-of-experts]] (new) — neurons grouped in blocks that rarely activate, so more neurons per flop (§ "Approach 1")
- [[compressed-sensing]] (new) — recovering sparse vectors from low-dimensional projections; lower bounds can be read as an upper bound on superposition in the toy model (§ "Compressed Sensing")
- [[leverage-score]] (new) — maximal share of $\|Wx\|^2$ a row can contribute; sums to rank (Zhang comment)
- [[decomposability-vs-superposition]] (new) — independent features coded separately vs more features than neurons (§ "Theories of Neural Coding…")

## Canonical instances
- [[abs-toy-model]] — $n=3$, $m=6$ abs model; $n=100$, $m=40$ model showing computation in superposition (§ "Basic Results", "Superposition vs Sparsity")
- [[inceptionv1-polysemanticity]] — polysemantic fraction rises with depth, consistent with sparser high-level features (§ "To What Extent…")
- [[othello-gpt]] — linear "my colour/opponent's colour" board representation (Nanda comment)
- [[early-mlp-die-example]] — first-layer MLP neurons, which would be polysemantic if their job is to separate senses of "die" (§ "To What Extent…")

## Bridges (candidates)
- [structural-analogy] Asymmetric superposition and inhibition ↔ error-control design: turning costly error into clipped error via the output nonlinearity.
- [same-math] Toy-model recovery bound ↔ compressed sensing: $m=\Omega(k\log(n/k))$ (the paper's appendix applies the theorem).
- [same-math] Feature dimensionality $D_i$ ↔ numerical linear algebra: leverage score, roughly equal when the vectors are in isotropic position (Zhang's argument).
- [structural-analogy] Overcomplete feature dictionaries ↔ sparse coding in neuroscience (used in the reverse direction).
- [structural-analogy] Mixture of Experts ↔ neuron sparsity exploited as free flops, competing with superposition.

## Questions this raises
- Does the abs-model's computation in superposition extend to other function classes, and which need sparse structure?
- Can an L1 penalty or a different activation move real models out of the superposition phase without large loss?
- How many features can real models hold, given the sparsity-modulated bound?
- Do features inferred by sparse autoencoders match what a superposition-free ground-truth model would show?

## Reading notes
- The part starts at the heading "Superposition in a Privileged Basis" and ends with the proof of Theorem 1 in the appendix on compressed-sensing lower bounds (after Nonlinear Compression). It includes Related Work, Comments & Replications, Acknowledgments, Author Contributions and Citation Information (skimmed).
- Source is HTML with no page numbers; citations use section headings. Figures and interactive plots were absent, so figure descriptions come from the surrounding text only.
- Appendix writes $T(x)=\text{ReLU}(W_2W_1x-b)$ (minus $b$); the main text writes $+b$. The appendix calls $W_1$ the $m\times n$ projection; Theorem 2 as printed uses a "$k\times n$" matrix with $m$ in the conclusion.
- The "if and only if" for compressed-sensing recovery is stated by the authors for various compressed-sensing settings.
- External comments are voiced by their own authors, not by the paper's authors (Henighan & Olah's comment is by two of the paper's authors); Sharkey's results are described as preliminary, and Nanda describes a separate blog post.
