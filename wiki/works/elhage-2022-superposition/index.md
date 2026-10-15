---
id: elhage-2022-superposition/index
work: elhage-2022-superposition
type: work-map
units: [elhage-2022-superposition/main-p1, elhage-2022-superposition/main-p2]
---

# Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., et al., & Olah, C. (2022). *Toy Models of Superposition*. Transformer Circuits Thread (Anthropic). arXiv:2209.10652.

## In one paragraph
Why do some neurons match clean features while others respond to many unrelated ones? The authors train tiny ReLU networks that squeeze sparse features into fewer dimensions. A linear model keeps only the most important features, like PCA. A model with a ReLU can store extra features as almost-orthogonal directions ("superposition"). It accepts a little interference, which sparsity makes rare and the ReLU filters. Which strategy wins changes sharply, like a phase change, with sparsity and importance. The stored features form regular shapes such as antipodal pairs, triangles and pentagons. When neurons impose a privileged basis, they become polysemantic as sparsity rises, and the network can even compute in superposition. This offers an explanation for polysemantic neurons. The authors also argue that "solving superposition", meaning enumerating all features, is a promising route to safety-relevant interpretability.

## The path through the work
- [[elhage-2022-superposition/main-p1]] — In small ReLU networks trained on sparse synthetic features, the model stores more features than it has dimensions as almost-orthogonal directions, accepting some interference, and the way it does this follows a phase diagram and regular geometric shapes.
- [[elhage-2022-superposition/main-p2]] — Once neurons impose a privileged basis (axes that matter), toy networks show neurons that hold one feature (monosemantic) or several (polysemantic) and can compute absolute value in superposition (more features than neurons); the authors argue superposition is closely tied to enumerating all features, which they see as a promising tool for safety claims.

## Big ideas across units
- **Superposition versus a privileged basis.** Features are directions, and superposition means more features than dimensions. Part 1 studies it without a privileged basis. Part 2 adds a ReLU hidden layer so that features can align with neurons. Units: main-p1, main-p2.
- **Sparsity drives superposition.** A linear model never shows superposition. With a ReLU, it appears as sparsity rises. In part 2, neurons shift from monosemantic to polysemantic as sparsity increases. Units: main-p1, main-p2.
- **Interference as the price.** The loss balances feature benefit against interference. In part 2, asymmetric superposition plus inhibition turns harmful positive interference into negative interference with limited consequences. Units: main-p1, main-p2.
- **Phase changes.** Whether a feature is dropped, superposed or given its own dimension changes sharply with importance and sparsity. Part 2 notes that phase changes give some hope that superposition could be removed entirely. Units: main-p1, main-p2.
- **Geometry of features.** Uniform superposition gives fractional dimensionalities that match uniform polytopes. Polytopes deform smoothly under changes and then snap. Correlated and anti-correlated features behave differently. Unit: main-p1 (part 2 says geometry is much less certain to transfer to real models).
- **Polysemantic neurons explained.** Superposition accounts for polysemanticity. Part 2 says the toy predictions are consistent with observed polysemanticity in real models. Units: main-p1, main-p2.
- **Computation in superposition.** A network that must compute abs(x) cannot avoid its ReLUs, yet at high sparsity it still computes it for more features than neurons. Unit: main-p2.
- **Enumerating features as a safety tool.** "Solving superposition" is linked to enumerating all features. Three routes exist (no-superposition models, overcomplete basis, hybrids), and each is hard. Compressed-sensing bounds limit how many features can be superposed. Unit: main-p2.

## How to read it
- **Essential:** main-p1. It covers the background, the demonstration of superposition, the phase change and the geometry, which are the focus areas in the catalog entry.
- **Next:** main-p2 depends on main-p1. Its prerequisites include the part-1 toy model (sparse features, hidden dimension m < n, interference). Read it for the privileged-basis results, computation in superposition and the strategic argument.
- **Can be skipped on a first pass:** the adversarial-robustness and learning-dynamics sections of main-p1, and the related work, outside comments and appendices (nonlinear compression, compressed-sensing bound) of main-p2. The units do not rank these sections, so this follows the catalog's focus list.

## Concepts introduced
- [[superposition]] — main-p1
- [[polysemantic-monosemantic]] — main-p1
- [[linear-representation-hypothesis]] — main-p1
- [[privileged-basis]] — main-p1
- [[feature-sparsity-importance]] — main-p1
- [[interference]] — main-p1
- [[feature-dimensionality]] — main-p1
- [[thomson-problem]] — main-p1
- [[tegum-product]] — main-p1
- [[phase-change]] — main-p1
- [[sparse-recovery]] — main-p1
- [[computation-in-superposition]] — main-p2
- [[asymmetric-superposition]] — main-p2
- [[solving-superposition]] — main-p2
- [[sparse-autoencoder]] — main-p2
- [[mixture-of-experts]] — main-p2
- [[compressed-sensing]] — main-p2
- [[leverage-score]] — main-p2
- [[decomposability-vs-superposition]] — main-p2
