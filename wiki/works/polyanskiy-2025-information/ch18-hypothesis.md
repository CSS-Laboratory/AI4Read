---
id: polyanskiy-2025-information/ch18-hypothesis
work: polyanskiy-2025-information
unit: "Chapter 16 (printed numbering) — Hypothesis testing: error exponents (with Exercises for Part III)"
pages: 313-338
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Hypothesis testing: error exponents

## L0 — One line
With n i.i.d. samples, the best pair of error exponents (E0, E1) is traced out by tilting P toward Q (a Legendre-transform curve), and letting the tester stop adaptively enlarges the region to E0E1 ≤ D(P‖Q)D(Q‖P).

## L1 — The gist (≤ 120 words)
How fast can the Type-I and Type-II error probabilities both decay with n? For n i.i.d. samples, the upper boundary of the achievable exponent pairs is the curve E0 = ψ*_P(θ), E1 = ψ*_P(θ) − θ. Here ψ_P is the log-MGF of the log-likelihood ratio. Equivalently, E0 and E1 are the divergences of a "geometric mixture" P_λ from P and from Q. The Bayesian error exponent is the Chernoff information. If the tester may request more samples (Wald's SPRT), the region becomes E0E1 ≤ D(P‖Q)D(Q‖P) (for bounded likelihood ratios), which is much larger. The chapter sketches composite testing. It also treats testing under a communication limit, where, for independence testing, the Stein exponent is the F_I-curve.

**Prerequisites:** KL divergence; Neyman–Pearson test and the Chapter 14 bounds; log-MGF and rate function (Chapter 15); martingales and stopping times; mutual information and the data-processing inequality.

## L2 — Key ideas
- Fixed-sample optimal tradeoff: E0 = ψ*_P(θ), E1 = ψ*_P(θ) − θ, for −D(P‖Q) ≤ θ ≤ D(Q‖P). It comes from Neyman–Pearson achievability plus the strong converse plus large deviations (p. 314, 316).
- The Bayesian error exponent does not depend on the prior. It equals the Chernoff information C(P,Q) = −inf_{λ∈[0,1]} ψ_P(λ), the exponent of the best Bayesian error (p. 315).
- Geometric form: (E0, E1) = (D(P_λ‖P), D(P_λ‖Q)) along the tilted family P_λ, equivalently E1*(E0) = min over {Q′: D(Q′‖P) ≤ E0} of D(Q′‖Q). This suggests that, given an error, the empirical distribution of the sample is close to P_λ (p. 317–318).
- Sequential testing: for bounded log-likelihood ratio, the SPRT achieves any (E0, E1) with E0E1 ≤ D(P‖Q)D(Q‖P), and no sequential test achieves a pair outside this set. Exponents are measured against expected sample sizes (p. 320–324).
- Key tools of the SPRT proof are a martingale identity E_P[S_τ] = E_P[τ]D(P‖Q) and the identity dP|_{F_τ}/dQ|_{F_τ} = exp{S_τ} (p. 322–323).
- For composite hypotheses there is no explicit optimal test in general. The popular choice is the generalized likelihood-ratio test (GLRT), which thresholds the ratio of the largest likelihood over each family (p. 324).
- With a rate-R link for X, the Stein exponent (the best Type-II exponent when the Type-I error need only stay below a fixed ε < 1) for independence testing is F_I(R) = sup{I(U;Y): I(U;X) ≤ R, U→X→Y} (p. 325–327). For small rate R = k/n, the error probability is roughly 2^{−kF_I′(0)}, so it decays exponentially in the number of bits sent, not in n. The slope F_I′(0) equals η_KL, the strong data-processing (SDPI) constant (p. 328).

## L3 — Walkthrough

### 16.1 (E0, E1)-tradeoff (p. 313–317)
**Setting (p. 313).** We want tests with π_{1|0} = 1 − α ≤ exp(−nE0) and π_{0|1} = β ≤ exp(−nE1). The best tradeoff is
E1*(E0) ≜ sup{E1 : ∃n0 ∀n ≥ n0 ∃P_{Z|X^n}: α > 1 − e^{−nE0}, β < e^{−nE1}} = liminf (1/n) log 1/β_{1−exp(−nE0)}(P^n,Q^n).
Define T_k = log (dQ/dP)(X_k), iid, so log dQ^n/dP^n = Σ T_k. The log-MGF and rate function are
ψ_P(λ) = log E_P[exp(λT)], ψ*_P(θ) = sup_λ θλ − ψ_P(λ).
In the discrete case ψ_P(λ) = log Σ_x P(x)^{1−λ}Q(x)^λ (p. 314). We have ψ_P(0) = ψ_P(1) = 0, so by convexity ψ_P is finite on [0,1]. If P ≪ Q and Q ≪ P it is continuous on [0,1]. Proofs assume the log-MGF exists for all λ (p. 314).

**Theorem 16.1** (P ≪ Q, Q ≪ P). The curve
$$E_0(\theta)=\psi_P^*(\theta),\qquad E_1(\theta)=\psi_P^*(\theta)-\theta \tag{16.1}$$
for −D(P‖Q) ≤ θ ≤ D(Q‖P) is the upper boundary of the achievable (E0, E1) region (p. 314). E0(θ) is increasing and E1(θ) is decreasing in θ (Fig. 16.1, via Thm 15.6).

*Intuition note.* In Fig. 16.1, θ is the slope of a tangent line to the curve ψ_P. The two exponents are the depths of this line below zero at λ = 0 and λ = 1. Raising θ buys a smaller Type-I error at the cost of a larger Type-II error.

**Remark 16.1 (Rényi).** ψ_P(λ) = (λ−1)D_λ(Q‖P) = −λD_{1−λ}(P‖Q). Hence ψ_P < 0 on (0,1), ψ_P′(0) = −D(P‖Q) and ψ_P′(1) = D(Q‖P) (p. 314).

**Corollary 16.2 (Bayesian criterion).** Let P*_e(n) = inf over tests of π0π_{1|0} + π1π_{0|1}, with 0 < π0 < 1. Its exponent E = lim (1/n) log 1/P*_e(n) satisfies E = max_θ min(E0(θ), E1(θ)) = ψ*_P(0), regardless of the prior. This is the Chernoff information
$$\psi_P^*(0) = -\inf_{\lambda\in[0,1]}\psi_P(\lambda) = -\inf_{\lambda\in[0,1]}\log\int (dP)^{1-\lambda}(dQ)^{\lambda}\triangleq C(P,Q). \tag{16.2}$$
(p. 315). The text gives no separate proof. Since E0(0) = E1(0) = ψ*_P(0) and E0 increases while E1 decreases, the crossing is at θ = 0 (added step). From (14.19), C(P,Q) is bounded above and below by multiples of log(1 − ½H²(P,Q)), so C ≍ H²(P,Q) for small H² (p. 315; see Reading notes on signs).

**Remark 16.2 (Bhattacharyya).** Take independent, non-identical observations. Two strings x^n, x̃^n over a finite alphabet are passed through a memoryless channel P_{Y|X}. Then the Chernoff exponent is
E = −inf_{λ∈[0,1]} (1/n) Σ_t log Σ_y P_{Y|X}(y|x_t)^λ P_{Y|X}(y|x̃_t)^{1−λ} (stated as "can be shown", p. 315).
If |X| = 2 and x^n, x̃^n have equal types (compositions), λ = ½ is optimal, giving E = (1/n)d_B(x^n, x̃^n), where
$$d_B(x^n,\tilde x^n)=-\sum_{t=1}^n\log\sum_{y}\sqrt{P_{Y|X}(y|x_t)P_{Y|X}(y|\tilde x_t)}. \tag{16.3}$$
Without those two assumptions, d_B does not necessarily give the optimal exponent. One always has ¼exp(−2d_B) ≤ P*_e ≤ exp(−d_B) (p. 316).

**Proof of Theorem 16.1 (p. 316–317).** Apply large deviations to Σ T_k.
- *Achievability (Neyman–Pearson, Thm 14.11 with τ = −nθ):*
$$\pi_{1|0}=P\Big[\sum_{k=1}^n T_k\ge n\theta\Big],\quad \pi_{0|1}=Q\Big[\sum_{k=1}^n T_k<n\theta\Big]. \tag{16.4}$$
- *Strong converse (Thm 14.10 with γ = e^{−nθ}):*
$$\pi_{1|0}+e^{-n\theta}\pi_{0|1}\ge P\Big[\sum_{k=1}^n T_k\ge n\theta\Big]. \tag{16.5}$$
- Theorems 15.9 and 15.11 give, for every n, π_{1|0} ≤ exp(−nψ*_P(θ)) when θ ≥ E_P T = −D(P‖Q). They also give π_{0|1} ≤ exp(−nψ*_Q(θ)) when θ ≤ E_Q T = D(Q‖P).
- Since T = log dQ/dP, ψ_Q(λ) = log E_P[e^{(λ+1)T}] = ψ_P(λ+1). So ψ*_Q(θ) = sup_λ θλ − ψ_P(λ+1) = ψ*_P(θ) − θ. Hence the pair (16.1) is achievable.
- *Converse.* Suppose π_{1|0} = e^{−nE0} and π_{0|1} = e^{−nE1}. Combining (16.5) with the large-deviations lower bound gives, for fixed θ,
 e^{−nE0} + e^{−nθ}e^{−nE1} ≥ e^{−nψ*_P(θ)+o(n)}, so min(E0, E1+θ) ≤ ψ*_P(θ).
 That is, either E0 ≤ ψ*_P(θ) or E1 ≤ ψ*_P(θ) − θ. ∎

*Intuition note.* A likelihood-ratio test errs only when the random sum Σ T_k lands on the wrong side of nθ. That is a large-deviation event whose probability is set by the rate function. The converse shows no test can beat the likelihood-ratio test's exponents.

### 16.2 Equivalent forms (p. 317–319)
**Theorem 16.3.**
(a) The optimal exponents are, for λ ∈ [0,1],
$$E_0=D(P_\lambda\|P),\qquad E_1=D(P_\lambda\|Q), \tag{16.6}$$
where dP_λ = (dP)^{1−λ}(dQ)^λ exp{−ψ_P(λ)} is the tilting of P along T (a "geometric mixture"). It moves from P_0 = P to P_1 = Q.
(b)
$$E_1^*(E_0)=\min_{Q':\,D(Q'\|P)\le E_0}D(Q'\|Q),\qquad 0\le E_0\le D(Q\|P). \tag{16.7}$$

**Proof of (a)** (p. 317). Fix λ and set θ(λ) = E_{P_λ}[T]. By (15.8), D(P_λ‖P) = ψ*_P(θ). Then
D(P_λ‖Q) = E_{P_λ}[log (dP_λ/dP)(dP/dQ)] = D(P_λ‖P) − E_{P_λ}[T] = ψ*_P(θ) − θ.
By (15.7), as λ runs over [0,1], θ runs from −D(P‖Q) to D(Q‖P).

**Proof of (b)** (p. 317–318). Q is itself a tilting of P (λ = 1). So the families dP_λ = exp{λT − ψ_P(λ)}dP and dQ_{λ′} = exp{λ′T − ψ_Q(λ′)}dQ coincide, with Q_{λ′} = P_{λ′+1}.
- Let Q* attain the minimum in (16.7), with Q* ≠ Q, P. The other cases "should be verified separately"; a minimizing sequence is handled the same way.
- Then D(Q*‖Q) ≤ D(P‖Q), since P is feasible. Also D(Q*‖P) ≤ D(Q‖P), since E0 ≤ D(Q‖P).
- Therefore
$$E_{Q^*}[T]=E_{Q^*}\Big[\log\frac{dQ^*}{dP}\frac{dQ}{dQ^*}\Big]=D(Q^*\|P)-D(Q^*\|Q)\in[-D(P\|Q),\,D(Q\|P)]. \tag{16.8}$$
- Corollary 15.12 gives a unique P_λ with E_{P_λ}[T] = E_{Q*}[T], D(P_λ‖P) ≤ D(Q*‖P), and D(P_λ‖Q) ≤ D(Q*‖Q). So the minimization can be restricted to the tilted family, and (16.8) puts λ in [0,1]. Hence (16.7) agrees with (16.6). Footnote 4: the essential range of T is the same under P and Q because P ≪ Q and Q ≪ P. ∎

**Remark 16.3.** This point of view suggests that, for an optimal test achieving (E0, E1), conditioned on the error event (under either P or Q) the empirical distribution is close to P_λ. Example: for P = Bin(m,p) and Q = Bin(m,q), the empirical distribution of an error sample is approximately Bin(m,r) for some r = r(p,q,λ) ∈ (p,q), and not any other distribution on {0,…,m} (p. 317).

**Remark 16.4.** As λ goes 0→1, P_λ traces a path from P to Q (Fig. 16.2). It is a geometric (not arithmetic) mixture, "in essence a geodesic". E0 and E1 are its divergences from the two endpoints. Unlike Riemannian geometry, the sum of the two distances varies along it (p. 318).

*Intuition note.* To make the unlikely event "the test errs" happen, the sample must look like some other distribution. The cheapest such distribution lies on the geometric path between P and Q.

### 16.3* Sequential hypothesis testing (p. 319–324)
**Review box (p. 319).** A filtration is a nested sequence of σ-algebras. A stopping time τ takes values in ℤ₊ with {τ ≤ n} ∈ F_n. For a uniformly integrable martingale, E[M_τ] = E[M_0].

**Setup (p. 320).** In Wald's sequential setting the tester may request more observations. A sequential test is a stopping time τ with respect to F_k = σ{X_1,…,X_k}, plus a decision Z ∈ {0,1} that is F_τ-measurable. Performance:
$$\alpha=P[Z=0],\ \beta=Q[Z=0];\qquad l_0=E_P[\tau],\ l_1=E_Q[\tau]. \tag{16.9, 16.10}$$

**Motivating example (p. 320).** Take P = ½δ_0 + ½δ_1 and Q = ½δ_0 + ½δ_{−1}. Here P ⊥̸ Q, so no fixed-n test has zero error under both. But waiting for the first ±1 gives zero error with two observations in expectation under both hypotheses.

**Theorem 16.4** (bounded LLR: |log P(x)/Q(x)| ≤ c_0 for all x). Call (E0, E1) achievable if there is a test with l_0, l_1 → ∞ and π_{1|0} ≤ exp(−l_0E_0(1+o(1))), π_{0|1} ≤ exp(−l_1E_1(1+o(1))). Then achievable pairs satisfy
E0E1 ≤ D(P‖Q)D(Q‖P).
Conversely, every such pair is achieved by SPRT(A,B): τ = inf{n : S_n ≥ B or S_n ≤ −A}, with Z = 0 if S_τ ≥ B and Z = 1 if S_τ < −A, where S_n = Σ_{k≤n} log P(X_k)/Q(X_k) (p. 320–321). Fig. 16.3 shows the sequential region lies above the fixed-sample curve. The version for general (E0, E1) is from [339]; Wald's original [450] covers E0 = D(Q‖P), E1 = D(P‖Q).

**Remark 16.5.** S_n is a random walk with drift +D(P‖Q) under P and −D(Q‖P) under Q. SPRT declares P when the walk crosses B and Q when it crosses −A (p. 321).

**Proof (p. 322–324).**
*Identity 1.* If E_P[τ] < ∞, then
$$E_P[S_\tau]=E_P[\tau]D(P\|Q), \tag{16.11}$$
and similarly E_Q[S_τ] = −E_Q[τ]D(Q‖P).
- M_n = S_n − nD(P‖Q) is a martingale, so M̃_n = M_{min(τ,n)} is too, and E[M̃_n] = 0. That is, E[S_{min(τ,n)}] = E[min(τ,n)]D(P‖Q) (16.12).
- Since |S_n| ≤ nc_0, we get |S_{min(n,τ)}| ≤ τc_0. So the family is uniformly integrable and we can let n → ∞.

*Identity 2.* dP|_{F_τ}/dQ|_{F_τ} = exp{S_τ}, i.e. E_P[1_E] = E_Q[R 1_E] for all E ∈ F_τ (16.13).
- Write 1_E = Σ_n 1_{E∩{τ=n}} and use monotone convergence. It suffices to check E_P[1_{E∩{τ=n}}] = E_Q[exp{S_τ}1_{E∩{τ=n}}] (16.14).
- This holds because E ∩ {τ=n} ∈ F_n and dP|_{F_n}/dQ|_{F_n} = exp{S_n} by definition of S_n.

*Achievability.*
- By (16.13), π_{1|0} = P[S_τ ≤ −A] = E_Q[exp{S_τ}1{S_τ ≤ −A}] ≤ e^{−A}.
- Let τ_0 = inf{n : S_n ≥ B}, so τ ≤ τ_0. By (16.11) and S_{τ_0} ≤ B + c_0: l_0 = E_P[τ] ≤ E_P[S_{τ_0}]/D(P‖Q) ≤ (B + c_0)/D(P‖Q).
- Similarly π_{0|1} ≤ e^{−B} and l_1 ≤ (A + c_0)/D(Q‖P).
- Take a boundary pair E0E1 = D(P‖Q)D(Q‖P) and let x = E0/D(P‖Q) = D(Q‖P)/E1. Set A = xB and let B → ∞. Then π_{1|0} ≤ e^{−xB} ≤ e^{−xB·l_0D(P‖Q)/(B+c_0)} = e^{−l_0E_0(1+o(1))}, and similarly π_{0|1} ≤ e^{−l_1E_1(1+o(1))}.

*Converse.*
- By data processing for divergence on F_τ and (16.11):
 d(P(Z=1)‖Q(Z=1)) ≤ D(P_{F_τ}‖Q_{F_τ}) = E_P[S_τ] = l_0D(P‖Q).
- For l_0E_0, l_1E_1 large, the left side equals l_1E_1(1+o(1)). So l_1E_1 ≤ (1+o(1))l_0D(P‖Q). Likewise l_0E_0 ≤ (1+o(1))l_1D(Q‖P).
- Multiplying and letting l_0, l_1 → ∞ gives E0E1 ≤ D(P‖Q)D(Q‖P). ∎

*Intuition note.* A fixed-n test must guess even on uninformative samples. The SPRT keeps sampling until the evidence S_n is strong enough. Since D(P‖Q) is the average evidence gained per sample, the expected stopping time is about boundary/drift.

### 16.4 Composite, robust, goodness-of-fit testing (p. 324–325)
- **Composite:** H0: X_i ~ P with P ∈ 𝒫, versus H1: X_i ~ Q with Q ∈ 𝒬. Errors are worst case: 1−α = inf_P P^{⊗n}[Z=0] and β = sup_Q Q^{⊗n}[Z=0]. In general there is no explicit optimal test. The popular choice is the generalized likelihood-ratio test, which thresholds T(X^n) = sup_P P^{⊗n}(X^n) / sup_Q Q^{⊗n}(X^n). Its error-exponent optimality has both examples and counterexamples (see [469]).
- **Robust:** 𝒫 and 𝒬 are small metric balls around P and Q. There is a finite-sample optimality result by Huber (Ex. III.31). If 𝒫 and 𝒬 are Hellinger-separated, the error can be made exponentially small (Thm 32.8).
- **Zero distance** (e.g. Student t-test: 𝒫 = {N(0,σ²)}, 𝒬 = {N(μ,σ²): μ≠0}): no test has α+β < 1. Instead one seeks a statistic that is pivotal under H0 (its distribution does not depend on the choice P_0 ∈ 𝒫, at least asymptotically) and consistent (T → ∞ under any fixed Q ∈ 𝒬). Optimality is judged by the power curve.
- **Goodness-of-fit:** 𝒬 is a huge alternative set, e.g. TV(P_0, Q) > δ. For δ = 0, again α+β = 1 in the worst case. For δ > 0 it is nonparametric detection (p. 325).

### 16.5* Testing with communication constraints (p. 325–328)
**Setting.** Test (X_i,Y_i) iid ~ P_{X,Y} versus Q_{X,Y}. The statistician sees Y^n, but X^n must be compressed to W = f(X^n) ∈ {0,1}^{nR} and sent over a noiseless link (16.15, Fig. 16.5). Define V_ε(R) = sup{E : ∃n_0 ∀n≥n_0 ∃(f, P_{Z|W,Y^n}): α > 1−ε, β < e^{−nE}}. The Stein exponent in this setting is open except for the case solved in [8] (p. 325).

**Definition 16.5 (F_I-curve).** F_I(t; P_{X,Y}) ≜ sup{I(U;Y) : I(U;X) ≤ t, U → X → Y} (p. 325).

**Example 16.1** (p. 326). For X ~ Ber(1/2) and Y = BSC_δ(X), applying the MGL of Ex. I.64 gives
F_I(t) = log 2 − h(h^{-1}(log 2 − t) ∗ δ).
It is achieved by U ~ Ber(1/2) and X = BSC_p(U) with h(p) = log 2 − t. By the DPI, F_I(t) ≤ t. If X is finite, |U| ≤ |X|+1 suffices (Ex. III.32), so F_I is a finite-dimensional convex program.

**Theorem 16.6 (Ahlswede–Csiszár).** Let X, Y be finite and Q_{X,Y} = P_XP_Y (independence testing). Then V_ε(R) = F_I(R) for all ε ∈ (0,1) (p. 327). If R = 0 the test is impossible, because Y has the same marginal under both hypotheses.

*Proof.*
- *Upper bound.* By Thm 14.8, d(1−ε ‖ exp{−nV_ε}) ≤ D(P_{W,Y^n}‖Q_{W,Y^n}). Since Q_{W,Y^n} = P_WP_{Y^n}, as in (14.18), (1−ε)nE ≤ I(W;Y^n) + log 2.
- Now W → X^n → Y^n, and by tensorization (Ex. III.32), I(W;Y^n) ≤ nF_I((1/n)I(W;X^n)) ≤ nF_I(R).
- So E ≤ F_I(R)/(1−ε) + (log 2)/n for large n, hence limsup_{ε→0}V_ε ≤ F_I(R). The strong converse V_ε ≤ F_I(R) is in [8].
- *Constructive part.* Take any n_1 and W_1 = f_1(X^{n_1}) ∈ {0,1}^{n_1R}. Send n/n_1 independent frames. Then the tester sees n/n_1 iid copies of (W_1, Y^{n_1}), with D(P_{W_1,Y^{n_1}}‖Q_{W_1,Y^{n_1}}) = I(W_1;Y^{n_1}). By Thm 14.14, α ≥ 1−ε and β ≤ exp{−(n/n_1)I(W_1;Y^{n_1})}. Hence
$$V_\epsilon\ge \tilde F_I(R)\triangleq\sup_{n,W_1}\Big\{\tfrac1n I(W_1;Y^n):W_1\to X^n\to Y^n,\ W_1\in\{0,1\}^{nR}\Big\}. \tag{16.16}$$
- To show F̃_I = F_I it remains to show F̃_I(R) ≥ F_I(R). Take U → X → Y and R > I(U;X). Apply the covering lemma (Cor. 25.6) and the Markov lemma (Prop. 25.7), with A^n = X^n, B^n = U^n, X^n = Y^n. This gives encoders with W_1 → X^n → Y^n and I(W_1;Y^n) ≥ nI(U;Y) + o(n). Hence F̃_I(R+) ≥ F_I(R).
- Since F̃_I(R+) ≤ F_I(R+) = F_I(R) (Ex. III.32), F̃_I(R) = F_I(R). ∎

**Implication (p. 328).** With n huge and only k bits deliverable, R = k/n ≪ 1 and β ≈ 2^{−nF_I(k/n)} ≈ 2^{−kF_I′(0)}. The error decays exponentially in the number of communicated bits, not in the sample size. The slope F_I′(0) equals the SDPI constant η_KL(P_X, P_{Y|X}) (see (33.14)). SDPIs are "linearized versions" of F_I-curves.

*Intuition note.* Each transmitted bit can carry only a limited amount of information about Y. How much is set by the curve's initial slope, so the number of bits is the real "sample size".

### Exercises for Part III (p. 329–338)
The problem set covers the whole of Part III. Items tied to this chapter are listed under "Exercises worth doing". Statements given there include the Gaussian Stein exponent (log e/2)μ², the Gaussian tradeoff E1 = (log e/2)(μ − √(2E0))², and the Gaussian Chernoff exponent (log e/8)μ² (III.19, p. 334).

## Toy example (ours, not from the text)
Let P = (0.8, 0.2) and Q = (0.2, 0.8) on {a, b}. Use natural logs.
1. ψ_P(λ) = ln(0.8^{1−λ}0.2^λ + 0.2^{1−λ}0.8^λ). Swapping λ ↔ 1−λ leaves it unchanged. Being convex, it is minimal at λ = ½ (as in Remark 16.2's argument).
2. ψ_P(½) = ln(2·√(0.8·0.2)) = ln(2·0.4) = ln 0.8 = −0.2231. So C(P,Q) = ψ*_P(0) = 0.2231 nats (≈ 0.322 bits).
3. Check with Thm 16.3(a). P_{1/2} ∝ √(PQ) = (0.4, 0.4), so P_{1/2} = (0.5, 0.5). D(P_{1/2}‖P) = 0.5 ln(0.5/0.8) + 0.5 ln(0.5/0.2) = 0.5 ln(0.625·2.5) = 0.5 ln 1.5625 = 0.5(0.4463) = 0.2231. By symmetry D(P_{1/2}‖Q) is the same. So (E0, E1) = (0.2231, 0.2231), the λ = ½ point, where θ = E_{P_{1/2}}[T] = 0.5(−ln 4) + 0.5(ln 4) = 0.
4. Endpoints: at λ = 0, (E0, E1) = (0, D(P‖Q)), with D(P‖Q) = 0.8 ln 4 + 0.2 ln(1/4) = 0.6 ln 4 = 0.8318. At λ = 1, (0.8318, 0).
5. If sequential sampling is allowed, any (E0, E1) with E0E1 ≤ 0.8318² = 0.6919 is achievable (Thm 16.4). For example (0.8318, 0.8318) is sequentially achievable, versus only (0.2231, 0.2231) at equal exponents with a fixed sample size.

## Concepts
- [[error-exponent-tradeoff]] (new) — the best pairs (E0, E1) of decay rates of Type-I and Type-II error with n samples (p. 313–314)
- [[chernoff-information]] (new) — C(P,Q) = −inf_λ log ∫P^{1−λ}Q^λ; exponent of Bayesian error, prior-independent (p. 315)
- [[tilted-distribution]] (new) — P_λ ∝ P^{1−λ}Q^λ, the geometric mixture; its divergences from P and Q give E0 and E1 (p. 317)
- [[relative-entropy-kl-divergence]] — D(P‖Q); appears as Stein/slope quantities and as the exponents themselves (p. 314, 317)
- [[sprt]] (new) — Wald's sequential probability ratio test: stop when the LLR random walk exits (−A, B) (p. 320–321)
- [[stopping-time]] (new) — a time decided causally from the past observations, used for adaptive sample sizes (p. 319)
- [[f-i-curve]] (new) — F_I(t) = sup{I(U;Y): I(U;X) ≤ t, U→X→Y}; strengthens the DPI (p. 325–326)
- [[sdpi-constant]] (new) — η_KL, equal to the slope F_I′(0) (p. 328)
- [[data-processing-inequality]] — used in the SPRT converse and for F_I(t) ≤ t (p. 323, 326)
- [[mutual-information]] — I(W;Y^n) controls the communication-constrained exponent (p. 327)
- [[composite-hypothesis-testing]] (new) — hypotheses are families of distributions; errors are worst case (p. 324)

## Canonical instances
- [[sequential-test-delta-example]] — P = ½δ_0+½δ_1 versus Q = ½δ_0+½δ_{−1}; sequential test has zero error, fixed-n cannot (p. 320)
- [[binomial-error-event]] — typical error sample for Bin(m,p) vs Bin(m,q) looks like Bin(m,r), r ∈ (p,q) (p. 317)
- [[bsc-f-i-curve]] — F_I(t) for X ~ Ber(1/2) through BSC_δ (p. 326)
- [[student-t-test]] — composite case with zero distance between hypotheses (p. 324)
- [[independence-testing-rate-limited]] — Ahlswede–Csiszár Stein exponent F_I(R) (p. 327)

## Bridges (candidates)
- [same-math] ψ_P(λ) = −λD_{1−λ}(P‖Q) ↔ information-theory: Rényi divergence — the log-MGF of the LLR is a Rényi divergence.
- [same-math] E1*(E0) = min_{D(Q′‖P) ≤ E0} D(Q′‖Q) ↔ large deviations: Sanov-type I-projection onto a KL ball.
- [structural-analogy] SPRT random walk with two absorbing boundaries ↔ sequential analysis/optimal stopping: decide when evidence crosses a threshold.
- [structural-analogy] SDPI constant as the slope of F_I at 0 ↔ distributed inference: bits communicated replace sample size.
- [metaphor] Geometric mixture P_λ as a "geodesic" from P to Q ↔ information geometry (the text itself says "in essence").

## Questions this raises
- Why is the Bayesian exponent independent of the prior, while the (E0, E1) tradeoff is not symmetric between hypotheses?
- Does the sequential gain survive when the LLR is unbounded (Theorem 16.4 assumes |LLR| ≤ c_0)?
- Can F_I(t) be computed in closed form beyond the BSC example, and how tight is |U| ≤ |X|+1?
- When is the GLRT exponent-optimal for composite hypotheses, and when does it fail?

## Exercises worth doing
- Ex. III.17 (p. 333) — Bernoulli(1/3) vs Bernoulli(2/3): Stein exponent, explicit tradeoff curve, geodesic P_λ, Chernoff exponent; checks Thm 16.1 against 16.3 — medium
- Ex. III.19 (p. 333–334) — Gaussian shift: Stein exponent, tradeoff curve and Chernoff exponent in closed form — medium
- Ex. III.29 (p. 337) — M-ary testing: exponent is the minimum pairwise Chernoff information; does maximum likelihood also achieve it? — hard
- Ex. III.30 (p. 337–338) — P⊗Q vs Q⊗P: Stein exponent and Chernoff exponent in terms of D and Hellinger — medium
- Ex. III.32 (p. 338) — F_I-curve: tensorization, concavity, cardinality bound, strict DPI; used in Thm 16.6 — hard

## Reading notes
- Printed pages 313–338 correspond to pdf 338–363 (printed = pdf − 25). The chapter is numbered 16 in print, though the unit metadata says ch18. Pages 329–338 are "Exercises for Part III" (III.1–III.33), not chapter-specific.
- Remark 16.5 says the walk crosses "the upper boundary −A"; this should be the lower boundary.
- The Fig. 16.4 caption says the decision is Z = 1 when S_n reaches B, but the definition on p. 321 gives Z = 0 when S_τ ≥ B.
- p. 320 defines F_k = σ{X_1,…,X_n} (index mismatch).
- p. 316 says "θ ∈ [−D(P‖Q), ≤ D(Q‖P)]" (stray ≤).
- The bounds on C(P,Q) on p. 315 print log(1−½H²) with a positive sign on both sides of a quantity C ≥ 0. A minus sign seems to be missing; (14.19) is not on these pages, so I did not check this.
- The binary convolution "∗" in Example 16.1 is not defined on these pages.
- Theorem 16.6's proof writes E where V_ε is meant in places; the Corollary 16.2 proof is not given separately.
- Section 16.3 and 16.5 are starred (optional) in the source.
