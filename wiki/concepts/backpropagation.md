---
id: backpropagation
type: concept
fields: [linear-algebra, control-theory, information-theory, llm]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch05-vector, mackay-2003-information/ch44-supervised, prince-2023-udl/ch07-gradients, strang-2023-introduction/ch09-linear, strang-2023-introduction/ch10-learning, sutton-2018-rl/ch09-policy-p2]
generated_by: build_kg.py
---

# backpropagation

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch05-vector]] (p. 159): efficient gradient of a loss through a layered composition, reusing partial products [new]
- [[strang-2023-introduction/ch09-linear]] (p. 349–350): reverse-mode chain rule: vector×matrix products from the loss back to layer j, with reuse [new]
- [[strang-2023-introduction/ch10-learning]] (pp. 371, 373–374): named as the algorithm and chain-rule subroutine for weights [new]

### control-theory

- [[sutton-2018-rl/ch09-policy-p2]] (p. 225): forward and backward passes giving a gradient estimate per weight [new]

### information-theory

- [[mackay-2003-information/ch44-supervised]] (p. 528): chain-rule algorithm that computes the gradient of $E_D$ efficiently [new]

### llm

- [[prince-2023-udl/ch07-gradients]] (p. 97): algorithm computing all parameter gradients by a forward pass storing activations, then a backward pass reusing partial derivatives [new]

## Instances that use it

- [[sin-exp-cos-toy-model]] — eight-parameter scalar model used to derive backpropagation — from [[prince-2023-udl/ch07-gradients]]
- [[pytorch-training-loop-fig7-8]] — short code example in which `loss.backward()` hides backpropagation — from [[prince-2023-udl/ch07-gradients]]

## Candidate bridges

- [structural-analogy] Backpropagation ↔ principle of optimality / dynamic programming: the author says they are closely related. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [structural-analogy] Covariant costate propagating backward ↔ backpropagation of gradients (canon link; not stated in this unit). — from [[liberzon-2012-calculus/ch07-advanced]] (control-theory → unspecified)
- [same-math] Reverse-mode AD on circuits ↔ neural networks: backpropagation — the text states they are the same algorithm (p. 270) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other)
- [structural-analogy] Backpropagation's reuse of partial products ↔ dynamic programming: sharing sub-results across overlapping computations. — from [[prince-2023-udl/ch07-gradients]] (llm → control-theory)
- [same-math] Jacobian ∂y/∂x = Aᵀ for y = Ax ↔ backpropagation through a linear layer: the same transpose-of-weights rule. — from [[prince-2023-udl/ch22-mathematics]] (llm → other)
