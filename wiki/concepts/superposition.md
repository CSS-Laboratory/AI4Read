---
id: superposition
type: concept
fields: [linear-algebra, llm]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch08-linear, elhage-2022-superposition/main-p1, elhage-2022-superposition/main-p2]
canon_spine: llm
generated_by: build_kg.py
---

# superposition

## Canon spine entry

- **superposition** (llm): representing more features than dimensions using nearly orthogonal directions (grad)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch02-linear]] (p. 30): $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$; the defining property of linearity [new]
- [[boyd-2018-vmls/ch08-linear]] (pp. 147, 150): property (8.1); for affine functions it holds when $\alpha+\beta=1$ [new]

### llm

- [[elhage-2022-superposition/main-p1]] (§ "Summary: A Hierarchy of Feature Properties"): more features than dimensions, stored as almost-orthogonal directions; $W^TW$ not invertible
- [[elhage-2022-superposition/main-p2]] (§ "Theories of Neural Coding…"): more features than dimensions or neurons, at cost of interference when features co-occur

## Instances that use it

- [[max-function-not-linear]] — counterexample to superposition for $\max$ — from [[boyd-2018-vmls/ch02-linear]]
- [[spanish-dutch-speaker]] — superposition beats time-sharing: 21 vs 20 bits/s — from [[cover-2006-elements/ch14-network-p3]]
- [[relu-output-toy-model]] — $x'=\mathrm{ReLU}(W^TWx+b)$, a very simple model that does show superposition (§ "The Model (x → x')") — from [[elhage-2022-superposition/main-p1]]
- [[pca-superposition-tradeoff]] — correlated features collapsing to $(a+b)/\sqrt2$ — from [[elhage-2022-superposition/main-p1]]
- [[abs-toy-model]] — $n=3$, $m=6$ abs model; $n=100$, $m=40$ model showing computation in superposition — from [[elhage-2022-superposition/main-p2]]
- [[hilbert-13th-problem]] — impossibility of superposition by entropy comparison — from [[polyanskiy-2025-information/ch30-metric]]

## Candidate bridges

- [metaphor] Superposition clouds and satellites ↔ layered media coding such as HDTV on top of regular TV (p. 419). — from [[cover-2006-elements/ch14-network-p3]] (information-theory → unspecified)
- [metaphor] Many phases of superposition ↔ many phases of ice. — from [[elhage-2022-superposition/main-p1]] (llm → unspecified)
- [structural-analogy] Asymmetric superposition and inhibition ↔ error-control design: turning costly error into clipped error via the output nonlinearity. — from [[elhage-2022-superposition/main-p2]] (llm → control-theory)
- [structural-analogy] Mixture of Experts ↔ neuron sparsity exploited as free flops, competing with superposition. — from [[elhage-2022-superposition/main-p2]] (llm → unspecified)
