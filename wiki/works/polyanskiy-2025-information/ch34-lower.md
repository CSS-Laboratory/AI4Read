---
id: polyanskiy-2025-information/ch34-lower
work: polyanskiy-2025-information
unit: "Chapter 31 — Lower bounds via reduction to hypothesis testing (listed in the metadata as ch34-lower)"
pages: 594-601
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Lower bounds via reduction to hypothesis testing

## L0 — One line
Minimax risk is at least the minimax risk on a well-chosen finite subfamily (two points, a hypercube, or a packing), and on that subfamily estimation is at least as hard as testing, which total variation or Fano's inequality can control.

## L1 — The gist (≤ 120 words)
How can we prove that no estimator can beat a given error, without asymptotics or smoothness? Restrict the parameter space to a subfamily Θ′, since R*(Θ) ≥ R*(Θ′). Then show that the hypotheses in Θ′ cannot be told apart reliably. Le Cam uses two points and TV (total variation distance). Assouad uses a hypercube and per-coordinate TV. Fano uses a packing and a bound on mutual information. Le Cam gives the right rate in one dimension but cannot see dimension. Assouad recovers d/n for squared error. Fano with a tight packing recovers the √(log d / n) rate for sup-norm loss in the Gaussian model, where Assouad and volume-based Fano give only 1/√n.

**Prerequisites:** minimax risk and Bayes risk; total variation and Hellinger distance; KL divergence and mutual information; Fano's inequality; packing numbers; Gaussian location model.

## L2 — Key ideas
- For any subfamily Θ′ ⊂ Θ, R*(Θ) ≥ R*(Θ′), so a lower bound proved on a well-chosen Θ′ is a lower bound for Θ. The three methods choose a two-point set, a hypercube and a packing (p. 594).
- Le Cam: for a loss with the α-triangle inequality, risk ≥ ℓ(θ0,θ1)/(2α) · (1 − TV(P_θ0, P_θ1)) (Thm 31.1, p. 594). It gives lower bounds of order 1/n for locally quadratic models and 1/n² for Unif(0,θ) (p. 596).
- Le Cam is stuck in high dimension: for the d-dimensional Gaussian model its best bound equals the 1-D bound, c/n, while the true risk is d/n (p. 596–597).
- Assouad: on a hypercube with ℓ(θ_b,θ_b′) ≥ β d_H(b,b′), risk ≥ (βd/4α)(1 − max TV over adjacent vertices) (Thm 31.2, p. 597). It gives d/n for squared error, but only 1/√n for the ℓ∞ loss (p. 598).
- A slightly weaker version of Assouad also follows from the mutual information method, by bounding I(b^d;X) away from d log 2 using adjacent-vertex TV (Sec. 31.3, pp. 598–599).
- Fano: P[d(θ,θ̂) ≥ ε/2] ≥ 1 − (C(T)+log 2)/log M(T,d,ε), where C(T) is channel capacity, which equals the KL radius (Thm 31.3, pp. 599–600).
- Fano with a volume-based packing gives d^{1/q}/√n for ℓq loss. For q = ∞ this misses √(log d / n), and a tight packing bound repairs it (pp. 600–601).

## L3 — Walkthrough

**Chapter intro (p. 594).** The three methods are less tied to mean-squared error than Chapter 29 and apply in nonasymptotic, nonparametric and high-dimensional settings. All three use R*(Θ) ≥ R*(Θ′). Le Cam is perhaps the easiest to evaluate but is frequently loose in high dimension. Assouad and Fano reduce to testing many hypotheses. All three follow from the mutual information method (MIM, Chapter 30) with different priors. Their constants are looser than MIM's, so they are ineffective for certain problems such as "better than chance" estimation (p. 594).

### 31.1 Le Cam's two-point method

**Theorem 31.1.** Assume ℓ(θ,θ)=0 and the α-triangle inequality (α > 0):
$$\ell(\theta_0,\theta_1)\le \alpha\big(\ell(\theta_0,\theta)+\ell(\theta_1,\theta)\big).\tag{31.1}$$
Then
$$\inf_{\hat\theta}\sup_{\theta\in\Theta}\mathbb E_\theta\,\ell(\theta,\hat\theta)\ \ge\ \sup_{\theta_0,\theta_1\in\Theta}\frac{\ell(\theta_0,\theta_1)}{2\alpha}\big(1-\mathrm{TV}(P_{\theta_0},P_{\theta_1})\big).\tag{31.2}$$

Proof (p. 595):
1. Fix θ0, θ1. Turn any estimator θ̂ into a randomized test θ̃. It outputs θ0 with probability ℓ(θ1,θ̂)/(ℓ(θ0,θ̂)+ℓ(θ1,θ̂)), and θ1 with probability ℓ(θ0,θ̂)/(ℓ(θ0,θ̂)+ℓ(θ1,θ̂)).
2. Then $\mathbb E_{\theta_0}\ell(\tilde\theta,\theta_0)=\ell(\theta_0,\theta_1)\,\mathbb E_{\theta_0}\big[\ell(\theta_0,\hat\theta)/(\ell(\theta_0,\hat\theta)+\ell(\theta_1,\hat\theta))\big]$.
3. (added step) By (31.1), ℓ(θ0,θ1)/(ℓ(θ0,θ̂)+ℓ(θ1,θ̂)) ≤ α. Hence $\mathbb E_{\theta_0}\ell(\tilde\theta,\theta_0)\le\alpha\,\mathbb E_{\theta_0}\ell(\hat\theta,\theta_0)$. The same holds for θ1. (The page prints this step with "≥ (1/α)E[ℓ(θ̂,θ0)]"; see Reading notes.)
4. Take the prior π = ½(δ_θ0 + δ_θ1). Then $\mathbb E_\pi\ell(\hat\theta,\theta)\ge \frac{\ell(\theta_0,\theta_1)}{\alpha}\mathbb P[\tilde\theta\ne\theta]\ge\frac{\ell(\theta_0,\theta_1)}{2\alpha}(1-\mathrm{TV})$. The last step is the minimum average error of binary testing (Theorem 7.7) (p. 595).

*Intuition note.* An estimator that is accurate on both of two hypotheses would give a good test. So if the two data distributions overlap a lot, the estimator must err by an amount of order of the separation ℓ(θ0,θ1).

**Remark 31.1 (p. 595).**
- The bound (31.2) is tight up to constants for binary testing with Hamming loss (α=1): the two sides can coincide, for example in the Gaussian location model.
- For quadratic loss ‖θ−θ̂‖² we have α=2. If TV=0, the best guess is the midpoint (θ0+θ1)/2, which explains the constant ¼.
- With prior π, the Bayes estimator is the posterior mean (θ0 dP0 + θ1 dP1)/(dP0+dP1). Its risk is
$$R^*_\pi=\frac{\|\theta_0-\theta_1\|^2}{2}\int\frac{dP_0\,dP_1}{dP_0+dP_1}=\frac{\|\theta_0-\theta_1\|^2}{4}\big(1-\mathrm{LC}(P_0,P_1)\big)\ge\frac{\|\theta_0-\theta_1\|^2}{4}\big(1-\mathrm{TV}\big),$$
where $\mathrm{LC}=\int\frac{(dP_0-dP_1)^2}{dP_0+dP_1}$ is the Le Cam divergence (7.7), and LC ≤ TV.

**Example 31.1 (pp. 595–596).** One-dimensional Gaussian location model (GLM) with n samples. The sufficient statistic X̄ gives {N(θ,1/n)}. Then
$$R^*\ge\sup_{\theta_0,\theta_1}\tfrac14|\theta_0-\theta_1|^2\{1-\mathrm{TV}(N(\theta_0,\tfrac1n),N(\theta_1,\tfrac1n))\}\overset{(a)}{=}\frac1{4n}\sup_{s>0}s^2(1-\mathrm{TV}(\mathcal N(0,1),\mathcal N(s,1)))\overset{(b)}{=}\frac cn,\tag{31.3}$$
- Step (a) uses shift and scale invariance of TV.
- Step (b) uses TV(N(0,1),N(s,1)) = 2Φ(s/2) − 1 (7.40), with c ≈ 0.083.
- The exact minimax risk is 1/n (Example 28.2), so the method is rate-optimal here (p. 596).

**Locally quadratic models (p. 596).** Suppose H²(P_θ0, P_{θ0+t}) ≍ t² as t → 0 (31.4). Take θ0 in the interior and θ1 = θ0 + 1/√n, so H²(P_θ0,P_θ1) = Θ(1/n). Theorem 7.8 gives TV(P_θ0^{⊗n}, P_θ1^{⊗n}) ≤ 1 − c, and so Ω(1/n) squared-error risk. Corollary 32.12 later shows this behaviour also guarantees achievability of 1/n (p. 596).

**Example 31.2 (p. 596).** For Unif(0,θ), H²(Unif(0,1),Unif(0,1+t)) = 2(1 − 1/√(1+t)) ≍ t. This gives an Ω(1/n²) lower bound. The estimator max{X_i} (the MLE) achieves that rate. The empirical mean achieves only 1/n.

**Example 31.3 (pp. 596–597).** d-dimensional GLM, reduced model {N(θ, I_d/n)}. The exact minimax risk is d/n (Example 28.2). Two-point bound with α=2:
$$R^*\ge\sup_\theta\frac1{4n}\|\theta\|_2^2\{1-\mathrm{TV}(N(0,I_d),N(\theta,I_d))\}=\frac1{4n}\sup_{s>0}s^2(1-\mathrm{TV}(\mathcal N(0,1),\mathcal N(s,1))).$$
By rotation invariance, TV(N(0,I_d), N(θ,I_d)) = TV(N(0,1), N(‖θ‖,1)). So the best two-point bound in d dimensions equals the 1-D bound, and does not grow with d (p. 597).

For functionals T(θ) of a high-dimensional parameter, Le Cam can be much more effective and sometimes optimal. It then needs composite hypotheses and well-chosen priors (Exercise VI.14) (p. 597).

*Intuition note.* A two-point family perturbs one direction only. The other d−1 coordinates are never tested, so the dimension cannot show up in the bound.

### 31.2 Assouad's lemma

**Theorem 31.2.** Assume the α-triangle inequality (31.1). Suppose Θ ⊃ Θ′ = {θ_b : b ∈ {0,1}^d} with ℓ(θ_b,θ_b′) ≥ β d_H(b,b′) for some β > 0. Then
$$\inf_{\hat\theta}\sup_{\theta}\mathbb E_\theta\ell(\theta,\hat\theta)\ge\frac{\beta d}{4\alpha}\Big(1-\max_{d_H(b,b')=1}\mathrm{TV}(P_{\theta_b},P_{\theta_{b'}})\Big).\tag{31.5}$$

Proof (pp. 597–598):
1. Use the uniform prior on Θ′. Define b̂ ∈ argmin_b ℓ(θ̂,θ_b).
2. For any b, β d_H(b̂,b) ≤ ℓ(θ_b̂,θ_b) ≤ α(ℓ(θ_b̂,θ̂)+ℓ(θ̂,θ_b)) ≤ 2α ℓ(θ̂,θ_b).
3. Hence $\mathbb E\ell(\hat\theta,\theta_b)\ge\frac{\beta}{2\alpha}\mathbb E\,d_H(\hat b,b)=\frac{\beta}{2\alpha}\sum_{i=1}^d\mathbb P[\hat b_i\ne b_i]\ge\frac{\beta}{4\alpha}\sum_i\big(1-\mathrm{TV}(P_{X|b_i=0},P_{X|b_i=1})\big)$, using Theorem 7.7.
4. Each $P_{X|b_i=a}$ is the average of $P_{\theta_b}$ over the $2^{d-1}$ vertices with $b_i=a$ (Bayes rule). By convexity of TV (Theorem 7.5), TV(P_{X|b_i=0},P_{X|b_i=1}) ≤ max_{d_H(b,b′)=1} TV(P_θb,P_θb′) (p. 598).

*Intuition note.* Estimating θ_b means testing d separate coordinate bits. Each bit costs a constant error if its two neighbouring hypotheses overlap, so the total error grows like d.

**Example 31.4 (p. 598).** GLM with θ_b = εb, so ‖θ_b − θ_b′‖₂² = ε² d_H(b,b′).
- Squared loss: R* ≥ (ε²d/4){1 − TV(N(0,1/n), N(ε,1/n))}, using (7.11), since adjacent vertices differ in one coordinate. With ε = 1/√n and TV's scale invariance, R* ≳ d/n.
- Loss ‖·‖∞: ‖θ_b − θ_b′‖∞ ≥ (ε/d) d_H(b,b′). Assouad then gives only R* ≳ 1/√n, independent of d. The truth is ≍ √(log d / n) (Corollary 28.8). Fano's method addresses this.

### 31.3 Assouad's lemma from the mutual information method (pp. 598–599)
Let b^d be i.i.d. Ber(½).
1. Rate–distortion for the Bernoulli source (Section 26.1.1): for any b̂^d and τ > 0 there is τ′ > 0 such that
$$I(b^d;X)\le d(1-\tau)\log 2\ \Longrightarrow\ \mathbb E[d_H(\hat b^d,b^d)]\ge d\tau',\qquad \tau\log 2=h(\tau').\tag{31.6}$$
2. By independence of the b_i, $I(b_i;X|b^{i-1})=I(b_i;X,b^{i-1})\le I(b_i;X,b_{\setminus i})=I(b_i;X|b_{\setminus i})$.
3. The chain rule, then (31.8), give
$$I(b^d;X)=\sum_i I(b_i;X|b^{i-1})\le\sum_i I(b_i;X|b_{\setminus i})\le d\log2\max_{d_H(b,b')=1}\mathrm{TV}(P_{X|b^d=b},P_{X|b^d=b'}).\tag{31.7}$$
Here (31.8) says I(B;X) ≤ TV(P_{X|B=0},P_{X|B=1}) log 2 for B ~ Ber(½). It follows from (7.39), because 2I(B;X) = JS(P_{X|B=0},P_{X|B=1}).
4. Combining (31.6) and (31.7) gives the MIM version of Assouad, with f(t) as printed on p. 599:
$$\inf_{\hat\theta}\sup_\theta\mathbb E_\theta\ell(\theta,\hat\theta)\ge\frac{\beta d}{4\alpha}f\Big(\max_{d_H(\theta,\theta')=1}\mathrm{TV}(P_\theta,P_{\theta'})\Big),\quad f(t)\triangleq h^{-1}\Big(\tfrac{(1-t)\log2}{2}\Big).\tag{31.9}$$
Here h⁻¹ : [0, log 2] → [0, ½] is the inverse of the binary entropy function.

(31.9) is slightly weaker than (31.5). When the pairwise TV is bounded away from one by a constant, as in Example 31.4, the two differ by a constant factor only. Summary: Assouad bounds I(b^d;X) away from d bits using distances between adjacent hypotheses (p. 599).

### 31.4 Fano's method
Assume the loss is a metric d. An ε-packing is a finite set of parameters with minimum separation ε. The impossibility of testing is often shown by Fano's inequality (Corollary 3.13) (p. 599).

**Theorem 31.3.** For any T ⊂ Θ and ε > 0,
$$\mathbb P\Big[d(\theta,\hat\theta)\ge\frac\epsilon2\Big]\ge1-\frac{C(T)+\log2}{\log M(T,d,\epsilon)},\tag{31.10}$$
where C(T) ≜ sup I(θ;X) is the capacity of the channel θ → X with inputs in T, the supremum being over priors on T, and M is the packing number. Consequently
$$\inf_{\hat\theta}\sup_\theta\mathbb E_\theta[d(\theta,\hat\theta)^r]\ge\sup_{T\subset\Theta,\epsilon>0}\Big(\frac\epsilon2\Big)^r\Big(1-\frac{C(T)+\log2}{\log M(T,d,\epsilon)}\Big).\tag{31.11}$$

Proof of (31.10) (p. 600):
1. Take an ε-packing {θ_1,…,θ_M} ⊂ T, put θ uniform on it, and X ~ P_θ.
2. Round θ̂ to θ̃ = argmin d(θ̂, ·) over the packing. By the triangle inequality d(θ,θ̃) ≤ 2d(θ,θ̂), so P[θ ≠ θ̃] ≤ P[d(θ,θ̂) ≥ ε/2] (the page prints θ̃ in the second term; see Reading notes). The bound in (31.10) then follows from the next step.
3. Fano gives P[θ ≠ θ̃] ≥ 1 − (I(θ;X)+log 2)/log M, and I(θ;X) ≤ C(T).

Capacity C(T) equals the KL radius inf_Q sup_{θ∈T} D(P_θ‖Q) (Theorem 5.9). So any choice of Q upper-bounds C(T) (p. 600).

*Intuition note.* If the data carry fewer than log M bits about which of M well-separated points was drawn, then a test, and hence an estimator, must err often. The data's information is capped by the capacity of the channel from θ to X.

**Example 31.5 (pp. 600–601).** GLM with P_θ = N(θ,I_d)^{⊗n}, natural logs, ℓq-loss (1 ≤ q ≤ ∞).
- D(P_θ‖P_θ′) = (n/2)‖θ−θ′‖₂², so KL-balls are ℓ2-balls. Take T = B2(ρ). Then C(T) ≤ sup_T D(P_θ‖P_0) = nρ²/2.
- By the volume bound (Theorem 27.3) and the ℓq-ball volume formula (27.13): $M(B_2(\rho),\|\cdot\|_q,\epsilon)\ge\frac{\rho^d\mathrm{vol}(B_2)}{\epsilon^d\mathrm{vol}(B_q)}\ge\big(\frac{c_q\rho d^{1/q}}{\epsilon\sqrt d}\big)^d$.
- Choose ρ = √(d/n) and ε = (c_q/e²) ρ d^{1/q−1/2}. (added step) Then M ≥ e^{2d}, so log M ≥ 2d and C(T) ≤ d/2.
- Result: $R_q\ge C_q\,d^{1/q}/\sqrt n$ (31.12), the same bound as (30.9), obtained by MIM plus the Shannon lower bound.
- (31.12) is rate-optimal for every q ≥ 1, achieved by X̄. At q = ∞, C_q is still finite since vol(B_∞) = 2^d.
- For q = ∞ the bound has no dimension dependence, whereas the truth is √(log d / n) (Corollary 28.8). Assouad gave the same weak result. The cause is the volume bound on metric entropy, which can be ineffective when ε scales with dimension (Section 27.3).
- Using the tight bound (27.18) on M(B2,‖·‖∞,ε), with ε = √(c log d / n) and ρ = √(c′ log d / n), one gets R_∞ ≳ √(log d / n) (p. 601).

**Remarks (p. 601).** C(T) may be bounded by the KL diameter sup_{θ,θ′∈T} D(P_θ′‖P_θ) (Corollary 5.8); this suffices for Example 31.5. Fano lower-bounds the global risk by the risk on a subspace T chosen to control mutual information. For other models (covariance model, Exercise VI.16) the KL-neighbourhood T must be chosen carefully. Section 32.4 applies Fano to smooth density estimation.

## Toy example (ours)
One observation X ~ Bernoulli(θ), squared loss (α = 2), θ ∈ [0,1].
- **Le Cam.** Take θ0 = 0.4 and θ1 = 0.6. Then TV = |0.6 − 0.4| = 0.2 and ℓ(θ0,θ1) = 0.2² = 0.04. Bound: 0.04/(2·2) · (1 − 0.2) = 0.01 · 0.8 = 0.008. Check: the constant guess 0.5 has risk 0.01 on both points, which is ≥ 0.008, as required.
- **Assouad.** Now take d independent coordinates, X_i ~ Bern(θ_i), with θ_b ∈ {0.4,0.6}^d. Then ‖θ_b − θ_b′‖² = 0.04 d_H(b,b′), so β = 0.04. Adjacent vertices differ in one coordinate, so max TV = 0.2. Bound: 0.04·d/(4·2) · 0.8 = 0.004 d. This grows linearly in d, whereas the two-point bound stays at 0.008 for this pair.

## Concepts
- [[le-cam-two-point-method]] (new) — lower-bound the minimax risk by testing two hypotheses; bound ℓ/(2α)·(1−TV) (p. 594)
- [[assouad-lemma]] (new) — hypercube subfamily; risk ≥ βd/(4α)·(1−max adjacent TV) (p. 597)
- [[fano-method]] (new) — risk lower bound from an ε-packing and capacity/KL radius (p. 599)
- [[alpha-triangle-inequality]] (new) — ℓ(θ0,θ1) ≤ α(ℓ(θ0,θ)+ℓ(θ1,θ)), the loss condition used for the reduction (p. 594)
- [[channel capacity]] — here C(T) = sup I(θ;X) over priors on T; equals the KL radius (p. 599–600)
- [[relative entropy / KL divergence]] — in the Gaussian model D = (n/2)‖θ−θ′‖² (p. 600)
- [[Fano's inequality]] — bounds the testing error from I(θ;X) and log M (p. 600)
- [[rate–distortion function]] — Bernoulli rate–distortion gives (31.6) (p. 598)
- [[mutual information I(X;Y)]] — bounded via the chain rule and the Jensen–Shannon form (p. 599)
- [[chain rule]] — used to sum per-coordinate information in (31.7) (p. 599)

## Canonical instances
- [[gaussian-location-model]] — the 1-D rate c/n (Le Cam), d/n (Assouad), and the ℓ∞ puzzle resolved by Fano (pp. 595–601)
- [[uniform-0-theta-family]] — Ω(1/n²) via H² ≍ t; achieved by the max (p. 596)

## Bridges (candidates)
- [structural-analogy] Le Cam / Assouad / Fano as reduction to testing ↔ information theory: converse proofs of channel coding via Fano — in both, decoding error is bounded by mutual information (canon link; not stated in this unit).
- [same-math] Fano's method with capacity C(T) ↔ channel capacity: C(T) is literally the capacity of the channel θ → X (p. 599).
- [same-math] Bernoulli rate–distortion in (31.6) ↔ lossy source coding: the Hamming distortion bound is the one from Section 26.1.1 (p. 598).

## Questions this raises
- When is the Le Cam constant lost for functional estimation, and how should priors be chosen for composite hypotheses?
- How does the packing/KL-neighbourhood choice in Fano's method work for non-Gaussian models, such as the covariance model?
- Can Assouad's lemma be improved to give √(log d) factors, or is Fano needed for that?
- Why does MIM beat these methods on "better than chance" problems (Section 30.4)?

## Exercises worth doing
The unit refers to Exercises VI.12, VI.14 and VI.16 but does not print them, so no exercises are listed.

## Reading notes
- Page offset: printed = pdf − 25. The running heading shows "Chapter 31"; the metadata calls the unit "ch34-lower".
- Misprint (probable): in the proof of Thm 31.1 (p. 595) the display reads E[ℓ(θ̃,θ0)] = ℓ(θ0,θ1)E[…] ≥ (1/α)E[ℓ(θ̂,θ0)]. From (31.1) only "≤ α E[ℓ(θ̂,θ0)]" follows, and that is the direction needed for the next line. I wrote the version I could derive.
- Printed (31.9): f(t) has "(1−t) log 2 / 2" inside h⁻¹. From (31.6)–(31.7) I get a bound of the form (βd/2α)·h⁻¹((1−max TV) log 2). I could not reconcile the extra "/2" and copied the page as printed.
- In the proof of Thm 31.3 the page prints P[θ≠θ̃] ≤ P[d(θ,θ̃) ≥ ε/2]. By the stated argument the intended event is d(θ,θ̂) ≥ ε/2. The page image shows θ̃ in the second term, so this may be a misprint.
- Example 31.1, (31.3), is copied as printed; I found nothing to correct there.
