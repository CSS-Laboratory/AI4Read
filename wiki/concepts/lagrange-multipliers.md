---
id: lagrange-multipliers
type: concept
fields: [linear-algebra, control-theory]
n_sources: 3
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch16-constrained, liberzon-2012-calculus/ch01-introduction]
generated_by: build_kg.py
---

# lagrange-multipliers

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 448): Lagrangian $L(x,z)=h(x)+g(x)^Tz$ for equality constraints [new]
- [[boyd-2018-vmls/ch16-constrained]] (p. 344): extra variables $z$ whose Lagrangian conditions give necessary optimality conditions [new]

### control-theory

- [[liberzon-2012-calculus/ch01-introduction]] (p. 11): coefficients $\lambda_i^*$ in (1.25); regular point assumed [new]

## Candidate bridges

- [structural-analogy] Ex. 71, $\lambda=f_N'(c)$ ↔ optimization: a Lagrange multiplier as the marginal value (shadow price) of the resource. — from [[bellman-1957-dp/ch01-i-p3]] (control-theory → other)
- [structural-analogy] $f'(x)=-k$ as "price" of stock, with derivatives as Lagrange multipliers (p. 162) ↔ control-theory: costates / shadow prices in the Pontryagin principle — both give the marginal value of the state. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [structural-analogy] Lagrange multipliers $\hat z$ ↔ economics: shadow prices of constraints — $\hat z$ measures how the constraint "costs" the objective (our reading; not stated in the unit). — from [[boyd-2018-vmls/ch16-constrained]] (linear-algebra → economics-finance)
- [structural-analogy] Neyman–Pearson ε-constraint ↔ constrained optimisation with a Lagrange multiplier: the threshold plays the multiplier's role. — from [[jaynes-2003-probability/ch14-simple]] (information-theory → other)
- [structural-analogy] Lagrange multiplier / augmented cost $\ell$ ↔ control theory: costates (shadow prices) in the maximum principle — the book says $\ell$ "will reappear in various forms" (p. 13); the costate link is canon, not stated in this unit — from [[liberzon-2012-calculus/ch01-introduction]] (control-theory → control-theory)
- [structural-analogy] adjoint vector $p^*$ ↔ Lagrange multipliers: both enforce a dynamic constraint inside the cost, and the text says $p$ is "reminiscent of" $\lambda$ but not identical (pp. 73, 75) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → other)
- [structural-analogy] Costate $p^*$ and abnormal multiplier $p_0^*$ ↔ calculus of variations: Lagrange multipliers and $\lambda_0^*$ (§2.5), which the author points to (p. 82). — from [[liberzon-2012-calculus/ch04-maximum-p1]] (control-theory → other)
- [structural-analogy] Lagrange multiplier = ∂(min cost)/∂b ↔ economics: shadow price of a resource — a price of relaxing a constraint (outside this unit). — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → economics-finance)
