---
id: chain-rule
type: concept
fields: [information-theory, bayesian, linear-algebra]
fields_strong: [information-theory, bayesian, linear-algebra]
n_sources: 22
n_works: 8
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, cover-2006-elements/ch02-entropy, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch09-differential, cover-2006-elements/ch11-maximum, cover-2006-elements/ch15-information, cover-2006-elements/ch16-inequalities, jaynes-1957-information/main, mackay-2003-information/ch08-dependent, pierce-1980-introduction/ch08-noisy, polyanskiy-2025-information/ch02-entropy, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch09-entropy, polyanskiy-2025-information/ch10-random, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch34-lower, shannon-1948-mathematical/main-p1, stone-2022-information/appf-rules, stone-2022-information/ch06-mutual]
raw_ids: [chain rule]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# chain-rule

## Canon spine entry

- **chain rule** (information-theory): H(X,Y) = H(X) + H(Y|X); uncertainty adds up step by step (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (pp. 16, 21–23): $H(X_1..X_n)=\sum H(X_i|X_{i-1}..X_1)$; analogues for $I$ and $D$
- [[cover-2006-elements/ch05-data-p2]] (p. 115): $H(Y,X)=H(X)+H(Y|X)$ used in Theorem 5.12.3
- [[cover-2006-elements/ch09-differential]] (p. 232): $h(X_1..X_n)=\sum h(X_i|X_{<i})$
- [[cover-2006-elements/ch11-maximum]] (p. 275): used with "conditioning reduces entropy" in Burg's proof
- [[cover-2006-elements/ch15-information]] (p. 469): $W^*(\mathbf X_1,\dots,\mathbf X_n)=\sum W^*(\mathbf X_i|\text{past})$
- [[cover-2006-elements/ch16-inequalities]] (p. 483): $H(X_1..X_n)=\sum H(X_i|\text{past})\le\sum H(X_i)$
- [[jaynes-1957-information/main]] (p. 630): Jaynes's composition law (A-1), the grouping property of uncertainty, used to single out the entropy form
- [[mackay-2003-information/ch08-dependent]] (p. 139): $H(X,Y)=H(X)+H(Y|X)$, from the product rule; also $h(x,y)=h(x)+h(y|x)$ [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch08-noisy]] (p. 154): relations 8.6 and 8.7
- [[polyanskiy-2025-information/ch02-entropy]] (p. 12): $H(X^n)=\sum H(X_i|X^{i-1})\le\sum H(X_i)$
- [[polyanskiy-2025-information/ch03-divergence]] (p. 32): here the divergence version, $D(P_{X,Y}\|Q_{X,Y})=D(P_{Y|X}\|Q_{Y|X}|P_X)+D(P_X\|Q_X)$ [as `chain rule`]
- [[polyanskiy-2025-information/ch04-mutual]] (p. 51–52): Kolmogorov identities for I; full form for $I(X^n;Y)$ [as `chain rule`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 68–69): used in proofs of Thm 4.1 and 4.3
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 109): used to turn $H(X^n)$ into a sum of conditional entropies
- [[polyanskiy-2025-information/ch09-entropy]] (pp. 158, 163): $H(X_1..X_n)=\sum H(X_i|X^{i-1})$, used in exact and random-order form
- [[polyanskiy-2025-information/ch10-random]] (p. 171): used to show $h$ is a fixed point of $T$
- [[polyanskiy-2025-information/ch25-channel]] (pp. 446, 450): mutual-information chain rule; divergence chain rule (2.26) in Lemma 23.6
- [[polyanskiy-2025-information/ch34-lower]] (p. 599): used to sum per-coordinate information in (31.7) [as `chain rule`]
- [[shannon-1948-mathematical/main-p1]] (p. 12): $H(x,y)=H(x)+H_x(y)$
- [[stone-2022-information/appf-rules]] (p. 265): $H(X,Y)=H(X)+H(Y|X)$ [as `chain rule`]
- [[stone-2022-information/ch06-mutual]] (p. 150): H(X,Y) = H(X)+H(Y|X) = H(Y)+H(X|Y) [as `chain rule`]

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 447): $Df(z)=Dg(h(z))Dh(z)$ for $f=g\circ h$ [new]

## Instances that use it

- [[card-suit-update]] — running example for the desiderata and the chain rule — from [[murphy-2023-pml2/ch05-information-p1]]
- [[bregman-theorem]] — permanent bound via random-order chain rule — from [[polyanskiy-2025-information/ch09-entropy]]

## Candidate bridges

- [same-math] chain rule $Df=Dg\,Dh$ ↔ linear-algebra: matrix multiplication as composition — the Jacobian of a composition is the product of Jacobians. — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → linear-algebra)
- [same-math] Chain rule as $Dh=Df\cdot Dg$ ↔ calculus/optimization: gradient of f(Ax+b) is $A^T\nabla f$ — the same Jacobian product. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other:optimization)
- [structural-analogy] Successive decoding and subtraction ↔ chain rule decomposition $I(X_1,X_2;Y)=I(X_2;Y)+I(X_1;Y|X_2)$ — each corner is a chain-rule ordering (p. 396). — from [[cover-2006-elements/ch14-network-p2]] (information-theory → unspecified)
- [structural-analogy] $W^*$ chain rule and "conditioning increases $W$" ↔ information theory: chain rule for $H$ and "conditioning reduces $H$" — formally parallel, with $W$ called the dual of $H$ (p. 470). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [structural-analogy] Cesàro-mean proof of $W^*_\infty$ ↔ entropy rate of stationary processes: parallel limit structure, since the chain rule for $W$ is formally that of $H$ (p. 470). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [structural-analogy] Chain rule as product of Jacobians ↔ matrix multiplication as composition: neighbouring dimensions must match (p. 148). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [same-math] Survival as product of conditional survivals ↔ probability: chain rule of conditional probability — the hazard product is that rule applied to $D_1,D_2,\dots$ — from [[hernan-2020-whatif/ch17-causal]] (bayesian → other:probability)
- [same-math] Composition law (A-1) ↔ information-theory: chain rule $H(X,Y)=H(X)+H(Y|X)$ — the grouping property is the chain rule for a coarse variable and the conditional given it. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [same-math] Product of elasticities $e = e_p\times e_d$ ↔ calculus: chain rule applied to proportional (log) derivatives. — from [[keynes-1936-general/ch21-theory]] (economics-finance → other:mathematics)
- [structural-analogy] Entropy decomposition (2.43) ↔ information-theory: chain rule $H(X,Y)=H(X)+H(Y\mid X)$ — information revealed in stages. — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [structural-analogy] Slepian–Wolf rate conditions ↔ information theory: chain rule $H(A,B)=H(A)+H(B|A)$ — the corner point with B sent as plain text has sum rate $H(B)+H(A|B)=H(A,B)$ (the chain rule is not on these pages). — from [[mackay-2003-information/ch15-further]] (information-theory → information-theory)
- [structural-analogy] evidence as a product of on-line predictions (28.18) ↔ information-theory: chain rule for entropy and cumulative log-loss — a joint probability factorizes step by step — from [[mackay-2003-information/ch28-model]] (information-theory → information-theory)
- [structural-analogy] Bayesian posterior as the KL-minimizing constrained update ↔ Bayes' theorem: the text says Bayes' rule alone is a trivial chain-rule identity, while the KL view gives a principle for updating (§5.1.7). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [same-math] Prequential log-loss $\sum_t\log \hat p_{t|t-1}$ ↔ Marginal likelihood (evidence): chain-rule decomposition into one-step-ahead predictive terms (p. 763). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [structural-analogy] p(x,y) = p(x)p_x(y) ↔ information-theory: chain rule for entropy — both build a pair in steps. — from [[pierce-1980-introduction/app-mathematical]] (information-theory → information-theory)
- [same-math] Peres' fixed-point identity $2h=h(2p\bar p)+\dots$ ↔ chain rule of entropy: the identity is derived by applying the chain rule (p. 171). — from [[polyanskiy-2025-information/ch10-random]] (information-theory → information-theory)
- [same-math] autoregressive factorisation (Eq. 12.15) ↔ probability: chain rule, since the product of next-token conditionals p(x_t | x_<t) is the chain rule applied to the token sequence — from [[prince-2023-udl/ch12-transformers]] (llm → other:probability)
- [same-math] Eq. (1) factorization ↔ probability theory: chain rule of probability — the product of conditionals is exactly the chain rule applied in sequence order. — from [[radford-2019-gpt2/main]] (llm → other:probability)
- [structural-analogy] Eq. 1 ↔ information-theory: weighted sum of entropies — resembles the chain-rule split (the weights sum to $1+q_\curvearrowright$, not 1, so it is not literally the chain rule) of a path into "which module" and "which node given module". — from [[rosvall-2008-maps/main-p1]] (information-theory → information-theory)
- [structural-analogy] Conditioning on $y_{\text{past}}$ ↔ information theory: chain rule / conditional mutual information — only information not already supplied by $y$'s own history counts. — from [[stone-2022-information/ch09-transfer]] (information-theory → information-theory)
- [same-math] Chain-rule product of Jacobians ↔ linear-algebra: matrix multiplication as composition — each ∂F_k/∂F_{k−1} is a matrix and the whole is their product. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
