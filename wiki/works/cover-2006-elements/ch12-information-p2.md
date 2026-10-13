---
id: cover-2006-elements/ch12-information-p2
work: cover-2006-elements
unit: "12 Information Theory and Statistics (part 2/3): §§12.6–12.9 (to Lemma 12.9.1)"
pages: 297–318
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Conditional limit theorem, hypothesis testing, Stein's lemma and the Chernoff bound

## L0 — One line
Conditioned on a rare event, i.i.d. samples look like draws from the distribution P* in the event set that is closest to the source in relative entropy, and the best error exponents in hypothesis testing are relative entropies to that kind of closest point.

## L1 — The gist (≤ 120 words)
Question: if i.i.d. data fall into a rare, convex set E of types, what do the data look like, and how well can two hypotheses be told apart? Answer: a "Pythagorean" inequality for relative entropy is the key step in showing that, given the rare event, the first few samples behave as i.i.d. draws from P*, the member of E closest to the source Q. For testing, the likelihood-ratio test is optimal (Neyman–Pearson). With one error fixed, the best exponent of the other is D(P1‖P2) (Stein's lemma). For Bayesian total error it is the Chernoff information. This matters because it turns testing and rare-event questions into relative-entropy geometry on the simplex of types.

**Prerequisites:** relative entropy and its convexity; types (a type is the empirical distribution of a sample; the simplex is the set of all distributions on the alphabet) and Sanov's theorem (earlier in ch. 12: number of types ≤ (n+1)^{|𝒳|}, probability of a type class ≐ 2^{-nD}); strong law of large numbers; Lagrange multipliers; basic conditional probability.

## L2 — Key ideas
- **Pythagorean inequality.** For closed convex E not containing Q, with P* the member of E closest to Q (smallest D(·‖Q)), D(P‖Q) ≥ D(P‖P*) + D(P*‖Q) for all P∈E. So D behaves, in this sense, like squared Euclidean distance, and if Pₙ∈E with D(Pₙ‖Q)→D(P*‖Q), then D(Pₙ‖P*)→0 (pp. 297–299).
- **L₁ lemma (Lemma 12.6.1).** D(P₁‖P₂) ≥ ‖P₁−P₂‖₁²/(2 ln 2), where ‖P₁−P₂‖₁ is the sum of the absolute differences of the two distributions; so convergence in relative entropy implies convergence in L₁ (pp. 299–301).
- **Conditional limit theorem.** Given P_{Xⁿ}∈E, Pr(X₁=a | ·)→P*(a) in probability. For fixed m, the first m samples become asymptotically i.i.d. P*. It fails for m=n (pp. 301–304).
- **Neyman–Pearson.** Here α is the probability of wrongly rejecting P₁ and β the probability of wrongly accepting P₁ when P₂ is true. The likelihood-ratio test compares P₁(x)/P₂(x) with a threshold T. Among tests with α ≤ α*, it minimises β (i.e. any other test with α ≤ α* has β ≥ β*). It is equivalent to comparing D(Pₓⁿ‖P₂) − D(Pₓⁿ‖P₁) with a threshold (pp. 305–308).
- **Error exponents via Sanov.** The point of the decision boundary closest to P₂ has the form P_λ ∝ P₁^λ P₂^{1−λ}, and the two error exponents are relative entropies to that point. The curve traced by P_λ is a geodesic (a curve of 'straight-line' type) in the simplex (pp. 308–309).
- **Stein's lemma.** With α_n < ε, the best β_n decays as 2^{-nD(P₁‖P₂)} to first order in the exponent (limit n→∞, then ε→0) (pp. 309–311).
- **Chernoff information.** For Bayesian error the best exponent is C(P₁,P₂)=D(P_λ*‖P₁)=D(P_λ*‖P₂). It does not depend on the non-zero priors (pp. 312–315).
- **Examples.** A mistaken Gaussian test leaves N(0,σ²)-shaped data. A mixed football strategy can beat both pure strategies for a rare large gain (pp. 316–318).

## L3 — Walkthrough

### 12.6 The conditional limit theorem (pp. 297–304)

**Recap.** The probability of a set of types under Q is a sum of type-class probabilities. It is bounded by the largest term times a polynomial number of terms. So it is $2^{-nD^*}$ to first order in the exponent, with $D^*=\min_{P\in E}D(P\|Q)$ \tag{12.120} (p. 297). The goal now is to show that the total probability of types far from P* is negligible (p. 297).

**Theorem 12.6.1 (Pythagorean).** Let E ⊂ 𝒫 be closed and convex, Q ∉ E, and $D(P^*\|Q)=\min_{P\in E}D(P\|Q)$ \tag{12.121}. Then
$$D(P\|Q)\ge D(P\|P^*)+D(P^*\|Q)\quad\text{for all }P\in E.\tag{12.122}$$
(pp. 297–298)

*Proof.* Take P∈E and set $P_\lambda=\lambda P+(1-\lambda)P^*$ \tag{12.123}. Then $P_\lambda\in E$ for $0\le\lambda\le1$ by convexity, and $P_\lambda\to P^*$ as λ→0. Since $P^*$ minimises D along this path, the derivative at λ=0 is ≥ 0. With $D_\lambda=\sum P_\lambda\log\frac{P_\lambda}{Q}$ \tag{12.124},
$$\frac{dD_\lambda}{d\lambda}=\sum\Big((P(x)-P^*(x))\log\frac{P_\lambda(x)}{Q(x)}+(P(x)-P^*(x))\Big).\tag{12.125}$$
At λ=0 the second term vanishes because ΣP=ΣP*=1. Then
$$0\le\Big(\frac{dD_\lambda}{d\lambda}\Big)_{\lambda=0}=\sum(P-P^*)\log\frac{P^*}{Q}=\sum P\log\frac{P^*}{Q}-\sum P^*\log\frac{P^*}{Q}$$
$$=\sum P\log\frac{P}{Q}\frac{P^*}{P}-\sum P^*\log\frac{P^*}{Q}=D(P\|Q)-D(P\|P^*)-D(P^*\|Q).$$
This is (12.126)–(12.130). (p. 298)

*Note (author).* If $P_n\in E$ and $D(P_n\|Q)\to D(P^*\|Q)$, then $D(P_n\|P^*)\to0$ (p. 298). The Euclidean analogue: for A outside a convex set, B the nearest point and C any other point, angle ABC is obtuse, so $l_{AC}^2\ge l_{AB}^2+l_{BC}^2$ (p. 299, Fig. 12.5).

> **Intuition note.** Relative entropy is not a metric, but projecting Q onto a convex set behaves like projecting a point onto a convex set in the plane. Going from Q to any P∈E "via P*" is shorter than going directly. So if P∈E is almost as far from Q as P* is, then D(P‖P*) must be small, i.e. P is close to P* in relative entropy.

**Definition (L₁ / variational distance).** $\|P_1-P_2\|_1=\sum_{a}|P_1(a)-P_2(a)|$ \tag{12.131}. With $A=\{x:P_1(x)>P_2(x)\}$:
$$\|P_1-P_2\|_1=\sum_A(P_1-P_2)+\sum_{A^c}(P_2-P_1)=P_1(A)-P_2(A)+1-P_2(A)-1+P_1(A)=2(P_1(A)-P_2(A)).\tag{12.132–12.136}$$
Also $\max_{B\subseteq\mathcal X}(P_1(B)-P_2(B))=P_1(A)-P_2(A)=\|P_1-P_2\|_1/2$ \tag{12.137}. The left side is the *variational distance* (pp. 299–300).

**Lemma 12.6.1.** $D(P_1\|P_2)\ge\frac{1}{2\ln2}\|P_1-P_2\|_1^2$ \tag{12.138} (p. 300).

*Proof.* Binary case, p ≥ q: show $p\log\frac pq+(1-p)\log\frac{1-p}{1-q}\ge\frac{4}{2\ln2}(p-q)^2$ \tag{12.139}. Let g(p,q) be the left side minus the right side \tag{12.140}. Then
$$\frac{dg}{dq}=-\frac{p}{q\ln2}+\frac{1-p}{(1-q)\ln2}-\frac{4}{2\ln2}2(q-p)=\frac{q-p}{q(1-q)\ln2}-\frac{4}{\ln2}(q-p)\le0,$$
as in (12.141)–(12.143). This holds because q(1−q) ≤ ¼ and q ≤ p. Since g(p,p)=0, g(p,q) ≥ 0 for q ≤ p. General case: let A={x:P₁(x)>P₂(x)} \tag{12.144}, let Y=φ(X) be the indicator of A, and let P̂₁, P̂₂ be the induced distributions of Y. By the data processing inequality for relative entropy (proved like the mutual-information version),
$$D(P_1\|P_2)\ge D(\hat P_1\|\hat P_2)\ge\frac{4}{2\ln2}(P_1(A)-P_2(A))^2=\frac1{2\ln2}\|P_1-P_2\|_1^2,$$
using (12.137) (12.145–12.147). (pp. 300–301)

**Proof outline of the main theorem** (p. 301). Types in E are split into those about as far from Q as P* and those a distance 2δ farther. The farther set has exponentially smaller probability, so the first set has conditional probability →1. The Pythagorean theorem then shows its members are close to P*.

**Theorem 12.6.2 (Conditional limit theorem).** Let E be closed and convex in 𝒫, Q∉E, X₁,…,Xₙ i.i.d. ∼ Q, and P* achieve $\min_{P\in E}D(P\|Q)$. Then
$$\Pr(X_1=a\mid P_{X^n}\in E)\to P^*(a)\ \text{in probability as }n\to\infty.\tag{12.148}$$
(p. 301)

*Proof* (pp. 302–304). Define $S_t=\{P:D(P\|Q)\le t\}$ \tag{12.151}. These sets are convex because D is convex in P. Let $D^*=D(P^*\|Q)=\min_{P\in E}D(P\|Q)$ \tag{12.152}. P* is unique because D is strictly convex. Define $A=S_{D^*+2\delta}\cap E$ \tag{12.153} and $B=E-S_{D^*+2\delta}\cap E$ \tag{12.154}, so A∪B=E. Using the type-class bound $Q^n(T(P))\le 2^{-nD(P\|Q)}$ and the polynomial number of types:
$$Q^n(B)=\sum_{P\in E\cap\mathcal P_n:\,D(P\|Q)>D^*+2\delta}Q^n(T(P))\le\sum 2^{-nD(P\|Q)}\le\sum 2^{-n(D^*+2\delta)}\le(n+1)^{|\mathcal X|}2^{-n(D^*+2\delta)}.\tag{12.155–12.158}$$
For the lower bound, for n large enough there is at least one type in $S_{D^*+\delta}\cap E\cap\mathcal P_n$. Hence
$$Q^n(A)\ge Q^n(S_{D^*+\delta}\cap E)\ge\frac1{(n+1)^{|\mathcal X|}}2^{-n(D^*+\delta)}.\tag{12.159–12.162}$$
Then, for n large,
$$\Pr(P_{X^n}\in B\mid P_{X^n}\in E)=\frac{Q^n(B\cap E)}{Q^n(E)}\le\frac{Q^n(B)}{Q^n(A)}\le(n+1)^{2|\mathcal X|}2^{-n\delta}\to0.\tag{12.163–12.166}$$
So the conditional probability of A tends to 1. For P∈A, $D(P\|Q)\le D^*+2\delta$ \tag{12.167}. The Pythagorean theorem gives $D(P\|P^*)+D(P^*\|Q)\le D^*+2\delta$ \tag{12.168}, hence $D(P\|P^*)\le2\delta$ \tag{12.169}. Therefore $\Pr(D(P_{X^n}\|P^*)\le2\delta\mid P_{X^n}\in E)\to1$ \tag{12.170}. By Lemma 12.6.1 this gives small L₁ distance, so $\max_a|P_{X^n}(a)-P^*(a)|$ is small. Thus $\Pr(|P_{X^n}(a)-P^*(a)|\ge\epsilon\mid E)\to0$, which is (12.171).

*Extension.* For fixed m, $\Pr(X_1=a_1,\dots,X_m=a_m\mid P_{X^n}\in E)\to\prod_{i=1}^mP^*(a_i)$ in probability \tag{12.172}. This is not true for m=n, because of end effects: given the type, the last elements are determined by the others. So the first few elements are asymptotically independent with common distribution P* (p. 304).

> **Intuition note.** Conditioning on a rare event does not make the sample "weird" everywhere. The cheapest way to realise the event is for the empirical distribution to sit at the closest allowed type P*. The individual samples then look like independent draws from P*.

**Example 12.6.1** (p. 301). For $E=\{P:\sum P(a)a^2\ge\alpha\}$, $\Pr\{X_1=a\mid\frac1n\sum X_i^2\ge\alpha\}\to P^*(a)$ \tag{12.149}, with
$$P^*(a)=Q(a)\frac{e^{\lambda a^2}}{\sum_aQ(a)e^{\lambda a^2}},\tag{12.150}$$
and λ chosen so that $\sum P^*(a)a^2=\alpha$. The author describes this as a normalised product of Q and the maximum-entropy pmf, which here is Gaussian.

**Example 12.6.2** (p. 304). For n fair dice with total exceeding 4n, take $E=\{P:\sum P(a)a\ge4\}$. Then the first die shows a with probability ≈ P*(a) (p. 304), where
$$P^*(x)=\frac{2^{\lambda x}}{\sum_{i=1}^62^{\lambda i}},\quad \sum iP^*(i)=4.\tag{12.173}$$
The first few dice behave as if drawn independently from this exponential-type distribution (p. 304).

### 12.7 Hypothesis testing (pp. 304–309)

**Setup.** X₁,…,Xₙ i.i.d. ∼ Q. H₁: Q=P₁; H₂: Q=P₂. A test g is specified by the set A where g=1 (accept H₁). Errors:
$$\alpha=\Pr(g=2\mid H_1)=P_1^n(A^c),\qquad\beta=\Pr(g=1\mid H_2)=P_2^n(A).\tag{12.174–12.175}$$
Both cannot be minimised together, so one is minimised subject to a constraint on the other (p. 305).

**Theorem 12.7.1 (Neyman–Pearson).** For T ≥ 0 let $A_n(T)=\{x:\frac{P_1(x)}{P_2(x)}>T\}$ \tag{12.176}, with $\alpha^*=P_1^n(A_n^c(T))$ and $\beta^*=P_2^n(A_n(T))$ \tag{12.177}. If B is any other decision region with errors α, β, and α ≤ α*, then β ≥ β* (pp. 305–306).

*Proof.* Let A=A_n(T), and let φ_A, φ_B be indicators. For all x, $[\phi_A(x)-\phi_B(x)][P_1(x)-TP_2(x)]\ge0$ \tag{12.178}. This is checked separately for x∈A and x∉A. Summing over x,
$$0\le\sum(\phi_AP_1-T\phi_AP_2-P_1\phi_B+TP_2\phi_B)=\sum_A(P_1-TP_2)-\sum_B(P_1-TP_2)$$
$$=(1-\alpha^*)-T\beta^*-(1-\alpha)+T\beta=T(\beta-\beta^*)-(\alpha^*-\alpha).$$
This is (12.179)–(12.182). The author concludes "since T ≥ 0". (added step) If α ≤ α*, then α*−α ≥ 0, so T(β−β*) ≥ α*−α ≥ 0, and for T>0 this gives β ≥ β*. (p. 306)

So the optimum test is the **likelihood ratio test** $\frac{P_1(X_1,\dots,X_n)}{P_2(X_1,\dots,X_n)}>T$ \tag{12.183} (p. 306).

*Gaussian example.* For f₁=𝒩(1,σ²), f₂=𝒩(−1,σ²):
$$\frac{f_1(X^n)}{f_2(X^n)}=\frac{\prod\frac1{\sqrt{2\pi\sigma^2}}e^{-(X_i-1)^2/2\sigma^2}}{\prod\frac1{\sqrt{2\pi\sigma^2}}e^{-(X_i+1)^2/2\sigma^2}}=e^{2\sum X_i/\sigma^2}=e^{2n\bar X_n/\sigma^2}.\tag{12.184–12.186}$$
So the test compares the sample mean $\bar X_n$ with a threshold. Equal error probabilities need T=1 (p. 307, Fig. 12.7).

**Test in terms of types.** The log-likelihood ratio is
$$L=\log\frac{P_1(X^n)}{P_2(X^n)}=\sum_i\log\frac{P_1(X_i)}{P_2(X_i)}=\sum_a nP_{X^n}(a)\log\frac{P_1(a)}{P_2(a)}=\sum_a nP_{X^n}(a)\log\frac{P_1(a)}{P_2(a)}\frac{P_{X^n}(a)}{P_{X^n}(a)}$$
$$=\sum_a nP_{X^n}(a)\log\frac{P_{X^n}(a)}{P_2(a)}-\sum_a nP_{X^n}(a)\log\frac{P_{X^n}(a)}{P_1(a)}=nD(P_{X^n}\|P_2)-nD(P_{X^n}\|P_1).$$
These are (12.187)–(12.192). So the test is equivalent to $D(P_{X^n}\|P_2)-D(P_{X^n}\|P_1)>\frac1n\log T$ \tag{12.194}. The boundary is the set of types with a constant difference of distances, the analogue of a perpendicular bisector (p. 308, Fig. 12.8).

**Choosing the threshold (informal, via Sanov).** Let B be the set where H₁ is accepted. Then $\alpha_n=P_1^n(P_{X^n}\in B^c)\doteq2^{-nD(P_1^*\|P_1)}$, where $P_1^*$ is the closest element of B^c (convex) to P₁ \tag{12.195–12.196}. Similarly $\beta_n\doteq2^{-nD(P_2^*\|P_2)}$, with $P_2^*$ the closest element of B to P₂ \tag{12.197} (p. 308). To find $P_2^*$, minimise D(P‖P₂) subject to $D(P\|P_2)-D(P\|P_1)=\frac1n\log T$ by Lagrange multipliers:
$$J(P)=\sum P\log\frac P{P_2}+\lambda\sum P\log\frac{P_1}{P_2}+\nu\sum P.\tag{12.198}$$
Setting the derivative to zero gives $\log\frac{P(x)}{P_2(x)}+1+\lambda\log\frac{P_1(x)}{P_2(x)}+\nu=0$ \tag{12.199}. Hence
$$P_2^*=P_{\lambda^*}=\frac{P_1^\lambda(x)P_2^{1-\lambda}(x)}{\sum_aP_1^\lambda(a)P_2^{1-\lambda}(a)}.\tag{12.200}$$
By symmetry $P_1^*=P_2^*$, so the exponents are $D(P^*\|P_1)$ and $D(P^*\|P_2)$. As λ→1, P_λ→P₁; as λ→0, P_λ→P₂. The curve of P_λ is a geodesic in the simplex, a normalised convex combination taken in the exponent (p. 309).

> **Intuition note.** Optimal testing is nearest-neighbour classification of the empirical type, using relative entropy as the "distance". The two error exponents are the distances from the two hypotheses to the decision boundary.

### 12.8 Stein's lemma (pp. 309–311)

**Theorem 12.8.1.** Let X₁,…,Xₙ i.i.d. ∼ Q, test Q=P₁ vs Q=P₂ with $D(P_1\|P_2)<\infty$, acceptance region $A_n\subseteq\mathcal X^n$ for H₁, and $\alpha_n=P_1^n(A_n^c)$, $\beta_n=P_2^n(A_n)$ \tag{12.201}. For 0<ε<½ define $\beta_n^\epsilon=\min_{A_n\subseteq\mathcal X^n,\ \alpha_n<\epsilon}\beta_n$ \tag{12.202}. Then
$$\lim_{\epsilon\to0}\lim_{n\to\infty}\frac1n\log\beta_n^\epsilon=-D(P_1\|P_2).\tag{12.203}$$
(p. 309)

*Proof* (pp. 310–311). Write D=D(P₁‖P₂) and define
$$A_n=\Big\{x\in\mathcal X^n:2^{n(D-\delta)}\le\frac{P_1(x)}{P_2(x)}\le2^{n(D+\delta)}\Big\}.\tag{12.204}$$
1. $P_1^n(A_n)=P_1^n\big(\frac1n\sum\log\frac{P_1(X_i)}{P_2(X_i)}\in(D-\delta,D+\delta)\big)\to1$ by the strong law of large numbers, since $D=E_{P_1}\log\frac{P_1(X)}{P_2(X)}$ (12.205–12.206). So for large n, α_n < ε.
2. $P_2^n(A_n)=\sum_{A_n}P_2\le\sum_{A_n}P_1 2^{-n(D-\delta)}=2^{-n(D-\delta)}(1-\alpha_n)$ (12.207–12.210). Similarly $P_2^n(A_n)\ge2^{-n(D+\delta)}(1-\alpha_n)$ \tag{12.211}. Hence $-D-\delta+\frac{\log(1-\alpha_n)}n\le\frac1n\log\beta_n\le-D+\delta+\frac{\log(1-\alpha_n)}n$ (12.212–12.213), and so (letting δ→0) $\lim\lim\frac1n\log\beta_n=-D$ \tag{12.214}.
3. *No other sequence does better.* Let B_n have $\alpha_{n,B_n}=P_1^n(B_n^c)<\epsilon$ and $\beta_{n,B_n}=P_2^n(B_n)$. Then
$$\beta_{n,B_n}\ge P_2^n(A_n\cap B_n)=\sum_{A_n\cap B_n}P_2\ge2^{-n(D+\delta)}\sum_{A_n\cap B_n}P_1\ge(1-\alpha_n-\alpha_{n,B_n})2^{-n(D+\delta)}.$$
This is (12.215)–(12.219). The last step is the union bound: $P_1(A_n\cap B_n)=1-P_1(A_n^c\cup B_n^c)\ge1-P_1(A_n^c)-P_1(B_n^c)$ (12.220–12.223). Hence $\frac1n\log\beta_{n,B_n}\ge-D-\delta+\frac{\log(1-\alpha_n-\alpha_{n,B_n})}n$ \tag{12.224} (printed with a minus sign before the log term; see Reading notes). Since δ>0 is arbitrary, $\lim\lim\frac1n\log\beta_{n,B_n}\ge-D(P_1\|P_2)$ \tag{12.225}. So A_n is asymptotically optimal and the best exponent is D(P₁‖P₂).

> **Intuition note.** If you tolerate any fixed small false-rejection rate, the other error can still shrink exponentially. The rate is the relative entropy D(P₁‖P₂): how surprising P₁'s typical data look to someone believing P₂.

### 12.9 Chernoff bound (pp. 312–318)

**Bayesian setup.** Hypotheses Q=P₁ with prior π₁ and Q=P₂ with prior π₂. Overall error $P_e^{(n)}=\pi_1\alpha_n+\pi_2\beta_n$ \tag{12.226}, and $D^*=\lim_{n}\min_{A_n}-\frac1n\log P_e^{(n)}$ \tag{12.227} (p. 312). The approach of Stein's lemma lacks symmetry between the two errors (p. 312).

**Theorem 12.9.1 (Chernoff).** The best achievable exponent is
$$D^*=D(P_{\lambda^*}\|P_1)=D(P_{\lambda^*}\|P_2),\tag{12.228}$$
with $P_\lambda=\frac{P_1^\lambda(x)P_2^{1-\lambda}(x)}{\sum_aP_1^\lambda(a)P_2^{1-\lambda}(a)}$ \tag{12.229}, and λ* the λ with $D(P_{\lambda^*}\|P_1)=D(P_{\lambda^*}\|P_2)$ \tag{12.230} (p. 312).

*Proof* (pp. 312–313). The optimal test is a likelihood-ratio test, which divides the simplex into a region A (hypothesis 1) and its complement (Fig. 12.9). By the argument before (12.200), the closest point of A^c to P₁ lies on the boundary of A and has the form (12.229). P_λ is also the point of A closest to P₂. By Sanov, $\alpha_n\doteq2^{-nD(P_{\lambda^*}\|P_1)}$ \tag{12.232} and $\beta_n\doteq2^{-nD(P_{\lambda^*}\|P_2)}$ \tag{12.233}. Then
$$P_e\doteq\pi_12^{-nD(P_\lambda\|P_1)}+\pi_22^{-nD(P_\lambda\|P_2)}\doteq2^{-n\min\{D(P_\lambda\|P_1),D(P_\lambda\|P_2)\}},\tag{12.234}$$
since the worst exponent dominates. The text (p. 313) says $D(P_\lambda\|P_1)$ increases with λ and $D(P_\lambda\|P_2)$ decreases with λ, but Fig. 12.10 (p. 314) plots the opposite (the first falls, the second rises; see Reading notes). Either way one is monotone up and the other down, so the maximum over λ of the minimum is attained where the two are equal:
$$D(P_\lambda\|P_1)=D(P_\lambda\|P_2)\triangleq C(P_1,P_2),\tag{12.235}$$
the **Chernoff information**, the highest achievable exponent.

**Standard definition.** $C(P_1,P_2)=-\min_{0\le\lambda\le1}\log\big(\sum_xP_1^\lambda(x)P_2^{1-\lambda}(x)\big)$ \tag{12.236}. The author leaves the algebraic equivalence with (12.235) as an exercise (p. 314).

**Usual derivation of the bound** (pp. 314–315). The maximum a posteriori rule minimises Bayesian error. Its region for H₁ is $A=\{x:\frac{\pi_1P_1(x)}{\pi_2P_2(x)}>1\}$ \tag{12.237}. Then
$$P_e=\pi_1\alpha_n+\pi_2\beta_n=\sum_{A^c}\pi_1P_1+\sum_A\pi_2P_2=\sum\min\{\pi_1P_1,\pi_2P_2\}.\tag{12.238–12.240}$$
For positive a, b: $\min\{a,b\}\le a^\lambda b^{1-\lambda}$ for all 0≤λ≤1 \tag{12.241}. Hence $P_e\le\sum(\pi_1P_1)^\lambda(\pi_2P_2)^{1-\lambda}\le\sum P_1^\lambda P_2^{1-\lambda}$ (12.242–12.244). For i.i.d. observations, $P_k(\mathbf x)=\prod P_k(x_i)$:
$$P_e^{(n)}\le\sum\pi_1^\lambda\pi_2^{1-\lambda}\prod_iP_1^\lambda(x_i)P_2^{1-\lambda}(x_i)=\pi_1^\lambda\pi_2^{1-\lambda}\prod_i\sum P_1^\lambda P_2^{1-\lambda}\overset{(a)}\le\Big(\sum P_1^\lambda P_2^{1-\lambda}\Big)^n,$$
where (a) uses π₁, π₂ ≤ 1 (12.245–12.248). So $\frac1n\log P_e^{(n)}\le\log\sum P_1^\lambda(x)P_2^{1-\lambda}(x)$ \tag{12.249}. Minimising over λ gives the Chernoff bound, so the exponent is no better than C(P₁,P₂). Achievability follows from Theorem 12.9.1.

**Priors wash out.** The exponent does not depend on π₁, π₂ as long as both are non-zero. The optimal rule is $\frac{\pi_1P_1(X^n)}{\pi_2P_2(X^n)}\gtrless1$ \tag{12.250}. In log form, $\frac1n\log\frac{\pi_1}{\pi_2}+\frac1n\sum\log\frac{P_1(X_i)}{P_2(X_i)}\gtrless0$ \tag{12.251}. The second term tends to D(P₁‖P₂) or −D(P₂‖P₁), according to which hypothesis is true. The first term tends to 0 (p. 315).

> **Intuition note.** With many samples the data outweigh any fixed prior. The error exponent is set by the point on the geodesic between P₁ and P₂ that is equally far (in relative entropy) from both.

**Example 12.9.1 (baseball, then Gaussian abstraction)** (p. 316). Major leaguers average 260, minor leaguers 240, both with standard deviation 15. A group of 100 players (league chosen at random) averages above 250 and is judged major, but is actually minor. The author states that the batting averages in this group will have mean 250 and standard deviation 15, by the conditional limit theorem. Abstraction: f₁=𝒩(1,σ²), f₂=𝒩(−1,σ²). The Bayes test is "accept f₁ if $\frac1n\sum X_i>0$". Suppose we err by saying f₁ when f₂ is true. Candidate guesses (author's, listed to be rejected or qualified):
- A (½,½) mix of the two normals: plausible but incorrect.
- Xᵢ ≈ 0 for all i: very unlikely, although $\bar X_n$ close to 0 is conditionally likely.
- The correct answer comes from the theorem: the conditional distribution is close to f*, the distribution in A closest to f₂. By symmetry this is λ=½ in (12.229):
$$f^*(x)=\frac{\big(\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-1)^2}{2\sigma^2}}\big)^{1/2}\big(\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{(x+1)^2}{2\sigma^2}}\big)^{1/2}}{\int(\cdots)}=\frac{\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2+1}{2\sigma^2}}}{\int\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2+1}{2\sigma^2}}dx}=\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2}{2\sigma^2}}=\mathcal N(0,\sigma^2).$$
This is (12.252)–(12.255). A mistaken normal population keeps its normal shape and variance but has a different mean. Apparently, the author says, this rare event does not result from bizarre-looking data (p. 317).

**Example 12.9.2 (football)** (pp. 317–318). The score is directly related to the yards gained (the author's simplification). Running gives a few yards with high probability; passing gives huge gains with low probability (Fig. 12.11). Late in the game the trailing team has n plays left and needs l yards, with l much larger than n times the expected gain per play. The aim is $\Pr\{\sum_{i=1}^nZ_i\ge n\alpha\}$ (as printed), with $E=\{P:\sum_aP(a)a\ge\alpha\}$ \tag{12.256}. Pure passing wins with probability $2^{-nD(P_1^*\|P_1)}$, and pure running with $2^{-nD(P_2^*\|P_2)}$ (Sanov). With the mixture $P_\lambda=\lambda P_1+(1-\lambda)P_2$, the probability is $2^{-nD(P_\lambda^*\|P_\lambda)}$. The author states that a mixture can do better than either pure strategy, "as can be shown by example" (no numbers given) (p. 318).

**Lemma 12.9.1 (Chernoff bound, special Markov inequality).** Let Y be any random variable with moment generating function $\psi(s)=Ee^{sY}$ \tag{12.257}. The statement begins "for all s ≥ 0" and is cut off at the end of these pages (p. 318).

## Toy example (ours)
Source Q = fair coin on {0,1}. Event set E={P: P(1) ≥ 0.8}, closed and convex. D(P‖Q) grows as P(1) moves away from ½, so P*(1)=0.8 and P* is the closest member of E.

*Conditional limit, n=10.* Condition on at least 8 ones among 10 tosses. Sequences: 8 ones: C(10,8)=45; 9 ones: 10; 10 ones: 1; total 56. The number with X₁=1 is 45·(8/10)=36, plus 10·(9/10)=9, plus 1, which is 46. So Pr(X₁=1 | event)=46/56≈0.821, close to P*(1)=0.8. (For n=5 and "at least 4 ones": (4+1)/(5+1)=0.833.)

*Pythagorean check* with P(1)=0.9 (in E), in bits:
- D(P‖Q)=0.9·log₂1.8+0.1·log₂0.2=0.9(0.8480)+0.1(−2.3219)≈0.5311.
- D(P‖P*)=0.9·log₂(0.9/0.8)+0.1·log₂(0.1/0.2)=0.9(0.1699)−0.1≈0.0529.
- D(P*‖Q)=0.8·log₂1.6+0.2·log₂0.4=0.8(0.6781)+0.2(−1.3219)≈0.2781.
- Sum: 0.0529+0.2781=0.3310 ≤ 0.5311, as (12.122) requires.

## Concepts
- [[relative-entropy-kl-divergence]] — D(P‖Q); here used as a "squared-distance-like" quantity on the simplex of types (p. 297)
- [[pythagorean-theorem-relative-entropy]] (new) — D(P‖Q) ≥ D(P‖P*)+D(P*‖Q) for P in a closed convex set E with P* the minimiser (p. 298)
- [[l1-distance-variational-distance]] (new) — ‖P₁−P₂‖₁; half of it equals max_B(P₁(B)−P₂(B)) (p. 299)
- [[pinsker-inequality]] (new) — D ≥ ‖·‖₁²/(2 ln 2) (p. 300)
- [[data-processing-inequality]] — quantising a distribution cannot increase relative entropy (p. 300)
- [[conditional-limit-theorem]] (new) — given P_{Xⁿ}∈E, the first few samples are asymptotically i.i.d. P* (p. 301)
- [[maximum-entropy-principle]] — the theorem is called a strengthening of it; P* has the MaxEnt form (p. 301)
- [[exponential-family]] — P*(a) ∝ Q(a)e^{λa²} and P_λ ∝ P₁^λP₂^{1−λ} are exponential tilts (pp. 301, 309)
- [[neyman-pearson-lemma]] (new) — the likelihood-ratio test minimises β given α ≤ α* (p. 305)
- [[likelihood-ratio-test]] (new) — compare P₁(x)/P₂(x) with T; equals a difference of relative-entropy distances of the sample type (p. 307)
- [[stein-lemma]] (new) — with α_n<ε, the best exponent of β_n is D(P₁‖P₂) (p. 309)
- [[chernoff-information]] (new) — C(P₁,P₂)=D(P_λ*‖P₁)=D(P_λ*‖P₂)=−min_λ log Σ P₁^λP₂^{1−λ}; the best Bayesian exponent (pp. 312–314)
- [[sanov-theorem-types]] (new) — probability of a set of types ≐ 2^{−nD*}; used here, stated earlier in the chapter (pp. 297, 308)

## Canonical instances
- [[dice-conditional-limit]] — n fair dice with sum > 4n; first die ≈ P*(x) ∝ 2^{λx} (p. 304)
- [[gaussian-mean-test]] — 𝒩(1,σ²) vs 𝒩(−1,σ²); the test thresholds the sample mean (p. 306)
- [[baseball-misclassification]] — conditional on a mistaken test, data stay normal with the same variance (p. 316)
- [[football-mixed-strategy]] — mixing run and pass can beat both pure strategies for a rare large gain (p. 318)

## Bridges (candidates)
- [structural-analogy] Pythagorean inequality for D ↔ Euclidean geometry: projection onto a convex set gives an obtuse angle, so $l_{AC}^2\ge l_{AB}^2+l_{BC}^2$ — stated by the author as a analogy (p. 299).
- [same-math] P*(a) ∝ Q(a)e^{λf(a)} (Example 12.6.1) ↔ statistical mechanics/exponential families: the same Gibbs-type tilt of a base measure.
- [structural-analogy] Chernoff information ↔ Bayesian decision theory: priors are "washed out" at large n as data dominate.
- [structural-analogy] Decision boundary D(P‖P₂)−D(P‖P₁)=const ↔ classification: a nearest-prototype rule with relative entropy as distance.

## Questions this raises
- Without convexity of E, does the conditional limit theorem still hold, or does P* fail to be unique?
- How does the Chernoff exponent compare numerically with the Stein exponent D(P₁‖P₂) for the same pair?
- For what pairs of strategies is a mixture P_λ strictly better in the football example, and how is the best λ found?
- What does the Chernoff bound lemma (Lemma 12.9.1) conclude, and how does it connect to the exponent in (12.236)?

## Reading notes
- **Part boundaries.** Starts at §12.6 (p. 297) and ends at p. 318, partway through Lemma 12.9.1: the inequality of the lemma itself is cut off at the end of the pages given and is not in this unit.
- **Edition.** The PDF is the 1991 first edition, not the 2nd edition named in the metadata, so section content and numbering may differ from the 2006 edition. Page offset: printed = pdf − 22.
- **OCR.** The text layer is garbled in many equations; I checked them against the images. The p. 317 running header is read as "22.9" in the text layer; the image shows 12.9.
- **Likely misprints in the source (what the images show).**
  - After (12.200), the condition is printed as $D(P_{\lambda^*}\|P_1)-D(P_{\lambda^*}\|P_2)=\frac{\log T}n$. By my check, the constraint stated on p. 308 for (12.198) is $D(P_\lambda\|P_2)-D(P_\lambda\|P_1)=\frac1n\log T$, the opposite sign.
  - (12.224) prints "−log(1−α_n−α_{n,B_n})/n". From (12.219) this term should enter with a plus sign. It tends to 0 either way.
  - (12.231) is printed as "> T"; by (12.194) the threshold should be (1/n) log T.
  - The Neyman–Pearson proof says "since T ≥ 0"; the final step needs T>0.
  - On p. 313 the text says D(P_λ‖P₁) increases with λ and D(P_λ‖P₂) decreases, but Fig. 12.10 (p. 314) plots D(P_λ‖P₁) falling and D(P_λ‖P₂) rising, consistent with P_λ→P₁ as λ→1 (p. 309). The max–min argument works either way.
- **Exercise.** The only exercise mentioned is the equivalence of (12.235) and (12.236), left to the reader (p. 314). No solutions are printed.
