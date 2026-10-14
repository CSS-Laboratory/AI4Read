---
id: elhage-2022-superposition/main-p1
work: elhage-2022-superposition
unit: "Toy Models of Superposition, part 1/2 (introduction through Relationship to Adversarial Robustness)"
pages: "HTML, no page numbers; cited by section heading"
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Toy Models of Superposition (part 1/2)

## L0 — One line
In small ReLU networks trained on sparse synthetic features, the model stores more features than it has dimensions as almost-orthogonal directions, accepting some interference, and the way it does this follows a phase diagram and regular geometric shapes.

## L1 — The gist (≤ 120 words)
Why do some neurons match clean features while others respond to many unrelated ones? The authors train tiny networks that compress $n$ sparse features into $m<n$ dimensions and reconstruct them. A linear model keeps only the top-$m$ features (like PCA). Adding a ReLU at the output lets the model keep extra features in superposition, because sparsity makes interference rare and the ReLU filters it. Which strategy wins changes sharply (a phase change) with sparsity and importance. The stored features form geometric shapes such as antipodal pairs, triangles and pentagons. Superposition can also make the model more vulnerable to adversarial attacks. This matters for interpretability: it offers an explanation for polysemantic neurons (neurons that respond to several unrelated features).

**Prerequisites:** matrices and transposes; dot products and norms; ReLU; mean squared error; probability of sparse inputs; the idea of a basis.

## L2 — Key ideas (5–10 bullets)
- Features are treated as directions in activation space, and superposition means more features than dimensions (the paper's formal criterion: $W^TW$ not invertible). It competes with a privileged basis (a basis made special by the architecture, e.g. an activation function), which encourages features to line up with neurons. (§ "The Superposition Hypothesis", § "Summary: A Hierarchy of Feature Properties")
- In a ReLU-output toy model, superposition appears as sparsity rises. A linear model never shows it. (§ "Basic Results")
- The loss balances feature benefit against interference. On 1-sparse inputs (one active feature), negative interference is free, and under simplifying assumptions the interference term is vaguely like a generalized Thomson problem (spreading points on a sphere). (§ "Mathematical Understanding")
- Whether the extra feature is dropped, superposed or given a dedicated dimension appears to change sharply (discontinuously) with importance and sparsity. (§ "Superposition as a Phase Change")
- Uniform superposition gives fractional feature dimensionalities (the fraction of a dimension a feature gets: ½, ⅔, ¾, ⅖, ⅜) that correspond to uniform polytopes (shapes such as triangles and tetrahedra). So superposition is not just one thing. (§ "The Geometry of Superposition")
- Changes in importance or sparsity deform the polytopes smoothly until they snap. Correlated features prefer orthogonality, then proximity, then collapse into a principal component. Anti-correlated features prefer to interfere, especially negatively. (§ "Non-Uniform Superposition")
- In the toy models, learning appears to involve discrete jumps and, in some cases, sequences of simple geometric transformations; the authors suspect smooth loss curves in larger models may hide many small jumps. (§ "Superposition and Learning Dynamics")
- Superposition can make the model more vulnerable to adversarial attack, and in the authors' test vulnerability closely tracks features per dimension. (§ "Relationship to Adversarial Robustness")

## L3 — Walkthrough

### Introduction
- The question: why do neurons sometimes align with features and sometimes not? It seems rare in large language models (§ "Intro").
- Method: small ReLU networks, synthetic sparse features. **Superposition** means representing more features than dimensions. With sparse features it compresses beyond a linear model, at the cost of "interference" that needs nonlinear filtering (§ "Intro").
- The five-features-in-two-dimensions example. With dense features the model learns an orthogonal basis of the two most important features, like PCA. Sparse features change this (§ "Intro").
- The authors say that, at least in certain limited cases, models can compute while in superposition (they say they will show simple absolute-value circuits). The authors hypothesize that real networks may be noisily simulating larger, highly sparse networks (§ "Intro").
- Contribution as claimed: a direct demonstration, in a fairly natural setup, that superposition can be the "ground truth" of a model. They also offer a theory with a phase diagram, and they report geometric structure (§ "Intro").
- They also report preliminary evidence that superposition may be linked to adversarial examples and grokking, say it might suggest a theory for mixture-of-experts performance, and mention a phenomenon qualitatively similar to the fractional quantum Hall effect (§ "Intro").
- Key results, with the caveat that the toy models are simple ReLU networks and it is very unclear what generalizes to real networks (§ "Key Results From Our Toy Models"):
  - superposition occurs;
  - both monosemantic and polysemantic neurons form;
  - some computation is possible in superposition;
  - a phase change governs it;
  - features organize into digons, triangles, pentagons and tetrahedrons.

### Definitions and Motivation
- **Linear representation hypothesis**, split into two properties (§ "Definitions and Motivation"):
  - *Decomposability*: representations can be described by independently understandable features.
  - *Linearity*: features are represented by directions.
- The authors hypothesize two opposing forces that decide whether features match neurons. A *privileged basis* encourages alignment with neurons. *Superposition* pushes features away from neurons (§ "Definitions and Motivation").
- The authors say they know of no earlier unambiguous demonstration of feature superposition (§ "Definitions and Motivation").
- **Empirical phenomena** motivating the picture (§ "Empirical Phenomena"):
  - word-embedding arithmetic, V("king") − V("man") + V("woman") = V("queen");
  - similar results in GAN latent spaces;
  - interpretable neurons;
  - universality across networks;
  - polysemantic neurons.
- **What is a feature?** Three working definitions are considered (§ "What are Features?"):
  - *Arbitrary functions of the input.* The authors say this does not quite fit: features seem special and identifiable. cat and car are features; cat+car and cat−car look like mixtures.
  - *Interpretable properties.* The authors say it is important to allow features humans may not understand.
  - *Properties that a sufficiently large model reliably dedicates a neuron to.* The authors wrote the paper with this definition in mind. They call it slightly circular, and it has an epsilon-delta flavour. Arbitrarily large models can still have a large fraction of features in superposition, but any given feature should eventually get a dedicated neuron if the importance curve is not flat.
  - They say they are not overly attached to it and that it is probably important not to attach to a definition prematurely.
- **Features as directions.** A representation is linear if each feature $f_i$ has a direction $W_i$, and active features $x_{f_1}, x_{f_2},\dots$ are represented as $x_{f_1}W_{f_1}+x_{f_2}W_{f_2}+\dots$. The features themselves are almost certainly nonlinear functions of the input. Only the map from features to activations is linear (§ "Features as Directions").
  - Three benefits: it is the natural output of template-matching neurons; features are linearly accessible to the next layer; it may give statistical efficiency through non-local generalization (§ "Features as Directions").
  - Nonlinear representations are possible with several layers, but the authors think they are generally inefficient (§ "Features as Directions").
- **Privileged vs non-privileged basis.** A random linear map $M$ on a word embedding, with $M^{-1}$ applied to the following weights, gives an identical model with different basis dimensions. So the basis is non-privileged (§ "Privileged vs Non-privileged Bases").
  - Activation functions break this symmetry and make basis directions "neurons".
  - A privileged basis does not guarantee that features are basis-aligned. It is only a minimal condition for asking whether a neuron is interpretable to make sense (§ "Privileged vs Non-privileged Bases").
- **Superposition hypothesis.** The superposition hypothesis, offered as one explanation for polysemantic neurons, says networks behave as if they want to represent more features than they have neurons (§ "The Superposition Hypothesis").
  - Supporting maths: $\exp(n)$ almost-orthogonal vectors fit in $n$ dimensions (Johnson–Lindenstrauss). Compressed sensing: a sparse vector can often be recovered from a lower-dimensional projection.
  - Features are almost-orthogonal directions, so one active feature looks like others slightly active. Sparsity cuts this interference cost, and nonlinear activations can filter small noise. Superposition can also occur without a privileged basis, since it only means more features than dimensions.
- **Hierarchy** of four properties (§ "Summary: A Hierarchy of Feature Properties"):
  1. Decomposability.
  2. Linearity.
  3. Superposition vs non-superposition: a linear representation exhibits superposition if $W^TW$ is not invertible, and does not if $W^TW$ is invertible.
  4. Basis-aligned: all $W_i$ are one-hot (partially aligned: all sparse). This requires a privileged basis.
  - The first two are hypothesized to be widespread. The latter two properties (non-superposition and basis alignment) are believed to occur only sometimes.

*Intuition note:* A layer's "directions" can be crowded. If features are rarely on together, many can share a few dimensions, because collisions are rare and small leftover noise can be cut off.

### Demonstrating Superposition
**Setup.** Project $x\in\mathbb R^n$ to $h\in\mathbb R^m$ and recover it. This can be viewed as an autoencoder (§ "Experiment Setup").

Synthetic features are built on three assumptions (§ "The Feature Vector (x)"):
- **Sparsity:** many natural features rarely occur.
- **More features than neurons.**
- **Varying importance.**

Each $x_i$ has sparsity $S_i$ and importance $I_i$. $x_i=0$ with probability $S_i$, otherwise $x_i$ is uniform on $[0,1]$. The uniform choice is arbitrary. The authors focus on the case where all $S_i=S$.

Two models differ only in the last activation (§ "The Model"). The shapes are $W\in\mathbb R^{m\times n}$, $x\in\mathbb R^n$, $h\in\mathbb R^m$, $b\in\mathbb R^n$.

$$h=Wx,\qquad x'=W^Th+b=W^TWx+b \quad\text{(linear)}$$
$$x'=\mathrm{ReLU}(W^Th+b)=\mathrm{ReLU}(W^TWx+b)\quad\text{(ReLU output)}$$

- Column $W_i$ is the direction for feature $i$.
- Using $W^T$ to decode avoids ambiguity. It is principled because $W^T=W^{-1}$ for orthonormal $W$. $W$ cannot be literally orthonormal, but the authors' compressed-sensing intuition is that it will be almost orthonormal (in the sense of Candes and Tao), and they say it works empirically (§ "Why these models?").
- The bias lets unrepresented features sit at their expected value. A negative bias also helps discard small noise.

Loss: importance-weighted squared error,
$$L=\sum_x\sum_i I_i\,(x_i-x'_i)^2.$$

**Basic results** (§ "Basic Results"):
- Diagnostics: $\|W_i\|$ says whether feature $i$ is represented. $\sum_{j\ne i}(\hat W_i\cdot W_j)^2$ says how much it shares a dimension. This quantity is 0 if orthogonal to all others. A value $\ge1$ means other features can activate $W_i$ as strongly as feature $i$ itself.
- Setting $n=20$, $m=5$, $I_i=0.7^i$: the linear model always learns the top-$m$ features, like top principal components.
- The ReLU model matches this on dense features ($1-S=1.0$). As sparsity rises, superposition emerges: less important features first, then the more important ones. It starts with antipodal pairs (one vector exactly the negative of the other) and moves to other geometries.
- With $m=20$, $n=80$, $I_i=0.9^i$, the picture is essentially a rescaled version of the first.

*Intuition note:* A linear model has no way to discard interference, so it spends its dimensions on the best features. The ReLU can zero out small wrong signals, which makes it affordable to share dimensions.

### Mathematical Understanding
- **Linear case.** Following Saxe et al., with $x'=W^TWx$ and Gaussian $x$, two forces compete: feature benefit (representing more features lowers loss) and interference (representing more than fits orthogonally raises it) (§ "Mathematical Understanding"). The text layer does not contain the loss equation.
  - The interference term $\sum_{i\ne j}|W_i\cdot W_j|^2$ is the $L^2$ norm of the same vector whose $L^\infty$ norm is the compressed-sensing coherence $\max_{i\ne j}|W_i\cdot W_j|$.
  - The authors say that this interference makes it never worthwhile for a linear model to represent more features than it has dimensions. The authors say this can be proved by setting the gradient to zero or by consulting Saxe et al.
- **ReLU case.** The goal is
  $$L=\int_x\|I(x-\mathrm{ReLU}(W^TWx+b))\|^2\,d\mathbf p(x).$$
  - By the binomial expansion of $((1-S)+S)^n$:
  $$L=(1-S)^nL_n+\dots+(1-S)S^{n-1}L_1+S^nL_0,$$
  where $L_k$ is the loss on $k$-sparse inputs.
  - As $S\to1$, $L_1$ and $L_0$ dominate. $L_0$ is a penalty on positive biases, $\sum_i\mathrm{ReLU}(b_i)^2$. The text layer omits the equation for $L_1$, the loss on 1-sparse vectors.
  - Thomson analogy: assume uniform importance, a fixed number of features with $\|W_i\|=1$ and the rest 0, and $b_i=0$. Then feature benefit is constant and the interference term becomes a generalized Thomson problem, though the authors call the resemblance only vague. This means packing points on a sphere with an unusual energy function.
  - On 1-sparse inputs ReLU makes negative interference free. A negative bias can turn small positive interference into effectively negative interference.
  - Less sparse inputs add compounding interference. Features often organize into sparse interference graphs, which makes $L_1$ matter more.

*Intuition note:* Each represented feature earns loss reduction. Each non-orthogonal pair costs interference when one feature's activity leaks into another's output, and sparsity makes this rare. In the 1-sparse case, ReLU makes negative overlap free.

### Superposition as a Phase Change
- Three outcomes per feature: not learned, learned in superposition, or given a dedicated dimension. "Phase change" here means a discontinuous change, not the technical infinite-size sense (§ "Superposition as a Phase Change").
- **2 features, 1 dimension.** The first feature has importance 1.0. The second's importance varies from 0.1 to 10 and sparsity from 1.0 to 0.01. Ten models are trained per point, and the highest-loss model is discarded.
  - Theory compares three weight settings:
    - $W=[1,0]$ ignores the extra feature.
    - $W=[0,1]$ gives the extra feature a dedicated dimension and drops the first.
    - $W=[1,-1]$ is antipodal superposition. It loses the ability to represent $[1,1]$.
  - Sparsity is necessary for superposition and interacts with relative importance.
  - There appears to be a real phase change in both the empirical and theoretical diagrams. In the theory it is first-order: the loss curves cross, giving a discontinuity in the derivative of the optimal loss.
- **3 features, 2 dimensions.** Four solutions are labelled by the direction $W$ ignores: $W\perp[0,0,1]$, $W\perp[1,0,0]$, $W\perp[0,1,1]$ (extra feature paired antipodally with one other) and $W\perp[1,1,0]$ (the other two superposed, the extra one dedicated). Joint superposition $W\perp[1,1,1]$ is not considered.
- These diagrams hide richer structure (§ "Superposition as a Phase Change").

### The Geometry of Superposition
The authors say the structure seems almost too elegant, and they think there is a good chance it is at least partly idiosyncratic to the toy model (§ "The Geometry of Superposition").

**Uniform superposition.** All features have equal importance (set to 1 without loss of generality) and equal sparsity, and are independent. Here $n=400$, $m=30$. What matters is $n\gg m$, and doubling $m$ doubles the features learned (§ "Uniform Superposition").
- $\|W\|_F^2$ roughly counts features learned, since $\|W_i\|^2\simeq1$ if represented and $\simeq0$ if not. It is basis-independent. Define $D^*=m/\|W\|_F^2$, the "dimensions per feature".
- $D^*$ is "sticky" at 1 and ½, very vaguely like the fractional quantum Hall effect. On inspection, the ½ plateau seems to correspond to antipodal pairs.

**Feature dimensionality** (§ "Feature Dimensionality"):
$$D_i=\frac{\|W_i\|^2}{\sum_j(\hat W_i\cdot W_j)^2}$$
- The numerator is how much feature $i$ is represented. The denominator is how many features share its dimension. An antipodal pair gives $D=1/(1+1)=1/2$. An unlearned feature gives 0.
- Dimensionalities seem to sum to the number of embedding dimensions when packing is efficient.
- Per-feature scatter plots show many more sticky points. Everything strictly between 0 and 1 is superposition, so superposition is not just one thing. The analogy is ice, which has many phases.

**Why these shapes** (§ "Why these geometric structures?"):
- Observed lines: ¾ tetrahedron, ⅔ triangle, ½ antipodal pair, ⅖ pentagon, ⅜ square antiprism, 0 not learned. A line at 1 is expected but hidden in the dense regime, where basis directions are indistinguishable from others.
- Several are Thomson-problem solutions. Each learned feature is a point on an $m$-dimensional sphere.
- Uniform polyhedra give single lines. Non-uniform ones show split lines. For example, instead of ⅗ for a triangular bipyramid, ⅔ (triangle) and ½ (antipodes) co-occur.
- Many Thomson solutions are *tegum products* of smaller uniform polytopes (two polytopes embedded in orthogonal subspaces). Subgraphs in the feature-geometry graph are disconnected if and only if they lie in different tegum factors. The authors expect dimensionality to follow the factor polytopes.
- This may explain why 3D solutions appear: higher-dimensional solutions may be tegum products of 1D, 2D and 3D ones. There is no interference across tegum factors, which the model may prefer.

**Polytopes and low-rank matrices** (§ "Aside: Polytopes and Low-Rank Matrices"):
- Matrices $W^TW$ are symmetric, positive-definite (as the source says), low-rank. If $W^TW$ has rank $m$, then $W$ is $m\times n$ and its columns are $n$ points in $m$-space. The source writes "$n\times m$", which is the transpose convention. Off-diagonals are driven by the geometry of the points.
- Strategies for superposition correspond exactly to polytopes. For instance, three features in 2D correspond to a triangle, and an equilateral triangle is the natural optimum for equal features.
- Conversely, characterize a matrix by the directions $W$ does not represent. Start with basis vectors and project onto the space orthogonal to those directions. $W\perp(1,1,1)$ gives a triangle. $W\perp(1,1,1,\dots)$ gives a regular $n$-simplex, described as, in some sense, the minimal possible superposition. For equally important and sparse features, the best direction to ignore is the fully dense vector.

*Intuition note:* "Where do I put $n$ points in a small space so they overlap as little as possible?" is a geometry puzzle. Its good answers are symmetric shapes, and each shape has a fixed share of a dimension per point.

**Non-uniform superposition.** The authors say they lack a comprehensive theory and only list phenomena (§ "Non-Uniform Superposition"):
- Varying importance or sparsity deforms polytopes smoothly until a critical point, where they snap to another polytope.
- Correlated features prefer orthogonality, often in different tegum factors. If they cannot be orthogonal, they prefer to be side by side. Sometimes they merge into a single feature.
- Anti-correlated features prefer the same tegum factor when superposition is needed, with negative interference, ideally antipodal.

*Perturbing a single feature* ($n=5$, $m=2$, $I=1$, density $1-S=0.05$) (§ "Perturbing a Single Feature"):
- The uniform case is a regular pentagon. A denser feature repels the others and gets more room. A sparser one takes less room and the others push toward it.
- If it is sparse enough, the pentagon collapses to a pair of digons with the sparse point at zero. The loss curves of the two geometries cross, which confirms a first-order phase change.
- Pentagon points lie off the unit circle because a slight negative bias cuts positive interference, and weights compensate with $\|W_i\|=1/(1-b_i)$. Distance from the circle mainly reflects positive interference.
- Reimplementation note: optimizing with $m=2$ is harder than with $m=3$. Clean results needed several fits per model, keeping the lowest loss.

*Correlated and anticorrelated features* (§ "Correlated and Anticorrelated Features"):
- A correlated set shares one zero/non-zero draw. The nonzero values are drawn separately. In an anticorrelated set, the whole set is zero with probability $S$. Otherwise exactly one randomly chosen member is drawn uniformly from $[0,1]$ and the rest are 0.
- Order of preference for correlated features: orthogonal in separate tegum factors; else close together (positive over negative interference); else collapse to their principal component. Anti-correlated features prefer to interfere, especially negatively.
- *Local almost-orthogonal bases:* in a larger model with two correlated sets, each set is nearly orthogonal in isolation even though the whole model is in superposition. If this holds in real networks, a "local non-superposition" assumption might justify tools like PCA on sub-distributions.
- *Collapse:* if the model has capacity to represent only one of two correlated features $a,b$, it represents their principal component $(a+b)/\sqrt2$ and ignores $(a-b)/\sqrt2$. In an experiment with six features in three correlated pairs, the very sparse regime shows a hexagon with correlated features side by side. As sparsity falls, features collapse into principal components, and in very dense regimes the solution equals PCA.
- The authors suggest PCA and superposition are complementary strategies: correlation favours PCA, sparsity favours superposition.

### Superposition and Learning Dynamics
The authors say they can give only a brief detour (§ "Superposition and Learning Dynamics").
- **Phenomenon 1, energy-level jumps.** In the uniform setup, where features converge to digons, feature dimensionalities jump between values and swap places. The loss drops suddenly at each jump (small at the first, larger at the second). The authors suspect that smooth loss decreases in larger models may consist of many small jumps. They cite induction-head phase changes, modular arithmetic phase changes and grokking as related (§ "Phenomenon 1").
- **Phenomenon 2, geometric transformations.** With $m=3$ the features form visible polyhedra. For $n=6$ features as two correlated sets of three, learning goes through distinct regimes, each a simple geometric transformation visible in the loss curve (§ "Phenomenon 2").
  - The figure describing steps A–C is not in the text. The text does say the final octahedron has features from different sets in antipodal pairs.
  - It seems to be a strong attractor, but there appear to be a few trajectories that differ at step C. Which one occurs presumably depends on the geometry nearest to where step B ends.
- The model first learns a linear PCA solution and then a better nonlinear one. This is likely the same mechanism as in prior findings that two-layer networks first learn a linear approximation. A second related finding concerns hierarchical features, where embedding vectors "split". It focuses on topology rather than geometry.

### Relationship to Adversarial Robustness
- Without superposition, $(W^TW)_0=(1,0,0,0,\dots)$. With superposition it is like $(1,\epsilon,-\epsilon,\epsilon,\dots)$. The $\epsilon$ entries are interference and give an adversary a route to attack the most important feature. This may hold even with infinite data (§ "Relationship to Adversarial Robustness").
- Test: $L^2$ attacks with maximum norm 0.1 of the average input norm. Gradient-descent attacks were difficult on extremely sparse inputs, where ReLU neurons are in the zero regime 99% of the time, effectively due to gradient masking. So the authors used the analytic optimal $L^2$ attack for each feature, $\lambda\,(W^TW)_i/\|(W^TW)_i\|_2$, and took the most harmful one.
- Result: vulnerability rises sharply as superposition forms (by $>3\times$) and closely tracks features per dimension (the reciprocal of dimensionality).
- The authors are hesitant to say how far superposition explains adversarial examples in practice, since other theories exist. A "superposition maximalist" view would predict:
  - that adversarial examples exist;
  - that robust models perform worse, because they would need to represent fewer features;
  - that more robust models might be more interpretable;
  - that adversarial examples transfer (the authors say it could arguably predict this), if feature arrangement is heavily influenced by which features are correlated or anti-correlated.
- Adversarial training against the analytic attack on a random feature reduced superposition, but removing it fully needed attacks of 80% of the input $L^2$ norm. The authors did not pursue this.

## Toy example (ours, not from the text)
Take $n=2$ features, $m=1$ dimension, $b=0$, antipodal $W=[1,\,-1]$ (a $1\times2$ matrix). Then $W^TW=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$.
- Input $x=(0.8,0)$: $h=1(0.8)+(-1)(0)=0.8$. $W^Th=(0.8,-0.8)$. After ReLU, $x'=(0.8,0)$. Error 0.
- Input $x=(0,0.8)$: $h=-0.8$. $W^Th=(-0.8,0.8)$. After ReLU, $x'=(0,0.8)$. Error 0.
- Input $x=(0.8,0.5)$ (both active): $h=0.3$. $W^Th=(0.3,-0.3)$. After ReLU, $x'=(0.3,0)$. Squared errors $0.5^2+0.5^2=0.5$ (with $I_i=1$).
- Compare $W=[1,0]$ (drops feature 2). On $(0,0.8)$ it gives $x'=(0,0)$ and error $0.8^2=0.64$. On $(0.8,0.5)$ it gives $x'=(0.8,0)$ and error $0.25$.
So with sparse inputs, where at most one feature is on at a time, antipodal superposition stores both features at zero error. If both are on, it errs more than $[1,0]$ does. Sparser data therefore favours superposition, which is the trade the paper studies.

## Concepts
- [[superposition]] — more features than dimensions, stored as almost-orthogonal directions; $W^TW$ not invertible (§ "Summary: A Hierarchy of Feature Properties")
- [[polysemantic-monosemantic]] — a neuron responding to many unrelated features versus one feature (§ "Intro")
- [[linear-representation-hypothesis]] (new) — features as directions; decomposability plus linearity (§ "Definitions and Motivation")
- [[privileged-basis]] (new) — basis directions made special by the architecture, e.g. an activation function; these are called neurons (§ "Privileged vs Non-privileged Bases")
- [[feature-sparsity-importance]] (new) — each synthetic feature is zero with probability $S_i$ and has weight $I_i$ in the loss (§ "The Feature Vector (x)")
- [[interference]] (new) — a feature's activity appearing as small activity in others because directions are non-orthogonal (§ "The Superposition Hypothesis")
- [[feature-dimensionality]] (new) — $D_i=\|W_i\|^2/\sum_j(\hat W_i\cdot W_j)^2$, the fraction of a dimension a feature gets (§ "Feature Dimensionality")
- [[thomson-problem]] (new) — packing points on a sphere with an energy function; under simplifying assumptions the model's 1-sparse interference term is vaguely like a generalized version (§ "Mathematical Understanding")
- [[tegum-product]] (new) — polytopes embedded in orthogonal subspaces; no interference across factors (§ "Why these geometric structures?")
- [[phase-change]] (new) — here a discontinuous change of optimal strategy, shown by crossing loss curves (§ "Superposition as a Phase Change")
- [[sparse-recovery]] (new; link to compressed sensing) — sparse vectors can often be recovered from low-dimensional projections (§ "The Superposition Hypothesis")

## Canonical instances
- [[relu-output-toy-model]] — $x'=\mathrm{ReLU}(W^TWx+b)$, a very simple model that does show superposition (§ "The Model (x → x')")
- [[word-embedding-arithmetic]] — king − man + woman = queen as evidence for directions (§ "Empirical Phenomena")
- [[antipodal-pair]] — two features in one dimension with $D=½$ (§ "Feature Dimensionality")
- [[polytope-feature-geometries]] — digon, triangle, tetrahedron, pentagon, square antiprism (§ "Why these geometric structures?")
- [[pca-superposition-tradeoff]] — correlated features collapsing to $(a+b)/\sqrt2$ (§ "Collapsing of Correlated Features")
- [[adversarial-vulnerability-from-interference]] — $\epsilon$ off-diagonal terms exploited by attacks (§ "Relationship to Adversarial Robustness")

## Bridges (candidates)
- [same-math] Linear-model interference $\sum_{i\ne j}|W_i\cdot W_j|^2$ ↔ compressed sensing: coherence $\max_{i\ne j}|W_i\cdot W_j|$ — the $L^2$ and $L^\infty$ norms of the same off-diagonal vector.
- [structural-analogy] Antipodal two-feature code in one dimension ↔ sparse recovery: a sparse input is recovered after a nonlinear filter.
- [structural-analogy] Layout of features on a sphere ↔ chemistry: Thomson problem — the same packing energy structure, with a different energy function.
- [metaphor] Sticky plateaus in $D^*$ ↔ physics: fractional quantum Hall effect — the authors call it only a vague resemblance.
- [structural-analogy] Discrete jumps in feature dimensionality during training ↔ phase changes such as induction-head formation and grokking.
- [metaphor] Many phases of superposition ↔ many phases of ice.

## Questions this raises
- Do real language-model features show the same polytope geometry, or is it specific to this uniform toy setup?
- How can feature directions be recovered in practice when a layer is in superposition? (Other work is referenced but not covered in this part.)
- Can the "local non-superposition" idea be tested on real correlated feature groups?
- How much of adversarial vulnerability in real models comes from superposition rather than other causes?

## Reading notes
- This is part 1 of 2. It starts at the title and abstract-style introduction and ends with the final paragraph of "Relationship to Adversarial Robustness" (adversarial training at 80% input $L^2$ norm). Later sections are not covered.
- The source is HTML with no page numbers and no page images were provided, so citations use section headings. The metadata asked for (pdf N), but none exists.
- Figures, interactive diagrams, citations and some displayed equations are missing from the text layer. The Saxe-style linear loss equation and the $L_1$ equation are absent, so they are not reproduced. The step A–C descriptions of the $n=6$, $m=3$ learning example are also missing.
- Inconsistencies in the source: the model is written $\mathrm{ReLU}(W^TWx+b)$ in "The Model" but $\mathrm{ReLU}(W^TWx-b)$ in "Superposition as a Phase Change". "Polytopes and Low-Rank Matrices" writes $W$ as "$n\times m$", while $h=Wx$ implies $m\times n$. A typo "$W_J$" appears in a footnote on coherence.
- The source uses both "digon" and "antipodal pair"; these pages do not explicitly say they are the same thing.
