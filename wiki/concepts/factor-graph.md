---
id: factor-graph
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 5
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch26-exact, mackay-2003-information/ch47-low, mackay-2003-information/ch49-repeat, murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch09-message]
generated_by: build_kg.py
---

# factor-graph

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch26-exact]] (p. 335): bipartite graph: variable nodes, factor nodes, edge if the factor depends on the variable [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch47-low]] (p. 558): graph of variable and check/factor nodes for $P(\mathbf t)$, $P(\mathbf t\mid\mathbf r)$ or $P(\mathbf n,\mathbf z)$ [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch49-repeat]] (p. 583): graph of variable nodes and constraint factors representing the prior over codewords [new; work fields: information-theory, bayesian]

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p3]] (pp. 202–204): bipartite or Forney graph displaying a function's factorization [new]
- [[murphy-2023-pml2/ch09-message]] (pp. 418, 425): bipartite graph of variables and factors; carries higher-order potentials and parity constraints (pp. 418, 425) (new)

## Instances that use it

- [[burglar-alarm-network]] — Exercise 26.8, as a factor graph — from [[mackay-2003-information/ch26-exact]]
- [[turbo-rate-third-factor-graph]] — Fig. 48.9: two long trellises sharing the source bits — from [[mackay-2003-information/ch48-convolutional]]
- [[ldpc-turbocode-lbp]] — LDPC factor graphs and LBP decoding — from [[murphy-2023-pml2/ch09-message]]

## Candidate bridges

- [same-math] Sum–product decoding ↔ bayesian: belief propagation on a factor graph, computing marginal posteriors exactly on trees — the text itself gives the name belief propagation (p. 557). — from [[mackay-2003-information/ch47-low]] (information-theory → bayesian)
- [structural-analogy] Factor graph of the prior over codewords with channel likelihoods multiplied in ↔ bayesian: posterior ∝ prior × likelihood; sum–product computes marginal beliefs. — from [[mackay-2003-information/ch49-repeat]] (information-theory → bayesian)
- [structural-analogy] Peeling decoder with certain/uncertain messages ↔ bayesian: belief propagation on a factor graph — the text calls it sum–product with extreme messages. — from [[mackay-2003-information/ch50-digital]] (information-theory → bayesian)
- [metaphor] Forney factor graph ↔ circuit or neural-network diagram: signals flow along edges, modified by nodes. — from [[murphy-2023-pml2/ch04-graphical-p3]] (bayesian → other:circuit-or-neural-network)
