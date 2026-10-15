---
id: partition-function
type: concept
fields: [bayesian, information-theory, llm, complex-systems]
fields_strong: [bayesian, information-theory, llm, complex-systems]
n_sources: 9
n_works: 5
tiers: [core, reference, deep]
grounding: digests
sources: [jaynes-1957-information/main, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch11-discrete, mackay-2003-information/ch31-ising, mackay-2003-information/ch33-variational, mackay-2003-information/ch51-appendices, murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch24-energy, rafailov-2023-dpo/main]
generated_by: build_kg.py
---

# partition-function

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 281): $Z(\lambda)=\sum_je^{-\lambda g_j}$; $Z^n$ is the generating function for multiplicities [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch11-discrete]] (p. 354, 356): $Z(\lambda)=\sum_i\exp\{-\sum\lambda_jf_j(x_i)\}$; $\log Z$ generates means, covariances and responses by differentiation [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch04-graphical-p2]] (p. 166): $Z(\boldsymbol\theta)$, the sum of the unnormalised product over all states; makes $p$ sum to 1 [new]
- [[murphy-2023-pml2/ch24-energy]] (p. 849): $Z_\theta=\int e^{-E_\theta}dx$; constant in $x$, usually intractable [new; work fields: bayesian, llm]

### information-theory

- [[jaynes-1957-information/main]] (p. 623): $Z=\sum_i e^{-\sum\lambda_k f_k(x_i)}$; $-\partial\ln Z/\partial\lambda_r=\langle f_r\rangle$ and $\partial^2\ln Z/\partial\lambda_r^2$ is the variance [new]
- [[mackay-2003-information/ch31-ising]] (pp. 400–401): $Z=\sum_{\mathbf x}e^{-\beta E}$; derivatives of $\ln Z$ give mean energy and variance [new; work fields: information-theory, bayesian, complex-systems]
- [[mackay-2003-information/ch33-variational]] (p. 422–423): Z = Σ exp(−βE); βF = −ln Z; Z̃ = e^{−βF̃} ≤ Z [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch51-appendices]] (p. 601): $Z(\beta)=\sum_x e^{-\beta E(x)}$, the normalizer of the Boltzmann distribution; $\ln Z$'s derivatives give energy variance and heat capacity [new; work fields: information-theory, bayesian]

### llm

- [[rafailov-2023-dpo/main]] (p. 4): $Z(x)=\sum_y\pi_{\text{ref}}\exp(r/\beta)$; hard to compute but cancels in pairwise preferences [new]

## Instances that use it

- [[phase-transition-partition-functions]] — relative probability of two phases is $Z_j/Z_k$; indifference where they are equal — from [[jaynes-2003-probability/ch20-model]]

## Candidate bridges

- [same-math] Partition function $Z(\lambda)$ and $u_j\propto e^{-\lambda g_j}$ ↔ statistical mechanics / exponential families: Gibbs distribution with normaliser $Z$. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (bayesian → complex-systems)
- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → other:exponential-family-theory)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (bayesian → information-theory)
- [same-math] Ratio of model evidences $p(D|M_j)/p(D|M_k)$ ↔ statistical mechanics: ratio of partition functions $Z_j/Z_k$ — both are ratios of normalisation constants of sub-problems (author, fn. 2, p. 602). — from [[jaynes-2003-probability/ch20-model]] (bayesian → complex-systems)
- [same-math] $Z(\lambda)=\sum e^{-\lambda t_i}=1$ for channel capacity ↔ statistical mechanics: canonical partition function, with $t_i$ playing the role of energy — the same exponential-weights and multiplier calculation (pp. 631–632). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → complex-systems)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity. — from [[mackay-2003-information/ch31-ising]] (information-theory → information-theory)
- [structural-analogy] Partition function $Z$ ↔ bayesian: marginal likelihood as normalizing constant — both are sums over all states or parameters that normalize an unnormalized weight. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [structural-analogy] Partition function $Z$, $A=\log Z$ ↔ statistical physics: normalizers of exponentially weighted distributions (the text only uses the name) — from [[murphy-2023-pml2/ch02-probability-p2]] (bayesian → complex-systems)
- [same-math] $\mathcal H(\Lambda)\le\inf_\lambda\lambda\Lambda+\log_2Z(\lambda)$ ↔ statistical physics/MaxEnt: partition function and Gibbs (exponential-family) form $P_\lambda\propto2^{-\lambda\,\text{cost}}$ (p. 205) — from [[polyanskiy-2025-information/ch12-variable]] (information-theory → complex-systems)
- [same-math] Optimal policy $\pi\propto\pi_{\text{ref}}\exp(r/\beta)$ (Eq. 4) ↔ statistical mechanics: a Gibbs/Boltzmann distribution (exponential tilting of a base measure), with $Z(x)$ the partition function and β a temperature. The paper uses the term partition function but does not mention physics. — from [[rafailov-2023-dpo/main]] (llm → complex-systems)
- [structural-analogy] Free energy F and annealing in β ↔ statistical physics: partition function, phase transitions (pp. 13, 15) — from [[tishby-2000-bottleneck/main]] (information-theory → complex-systems)
