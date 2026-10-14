---
id: polyanskiy-2025-information/ch17-information
work: polyanskiy-2025-information
unit: "Chapter 15 (printed numbering): Information projection and large deviations"
pages: 291-312
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Information projection and large deviations

## L0 — One line
For E[X] < γ < B (B = top of the range of X), the exponent of the probability that an empirical mean exceeds γ is the smallest KL divergence D(Q‖P) over distributions Q with mean ≥ γ, and the minimiser is the exponentially tilted P.

## L1 — The gist (≤ 120 words)
For iid sums, how fast does a tail probability such as P[(1/n)ΣXₖ ≥ γ] decay? For γ above the mean, the chapter shows the exponent equals the rate function ψ*(γ), the convex conjugate of the log moment generating function. It also equals min D(Q‖P), the KL divergence, over Q with E_Q[X] ≥ γ (an "information projection"). The minimiser is P tilted by exp(λX), which explains why the Chernoff bound (Markov's inequality on e^{λΣXₖ}) is sharp. For Q with the same mean as the tilt Q*, D(Q‖P) = D(Q‖Q*) + D(Q*‖P). The chapter then states Sanov's theorem for convex sets and treats several linear constraints, where the minimiser is a tilt (exponential family). This prepares the Chernoff regime of hypothesis testing.

**Prerequisites:** KL divergence and its convexity, data-processing inequality, Markov inequality, convex conjugates, basic measure theory (absolute continuity, dominated convergence), gradients/Hessians. "Tilting" (reweighting a distribution by e^{λx}) is defined in L3.

## L2 — Key ideas
- Chernoff bound as a change of measure: Markov applied to e^{λΣXᵢ} gives P[ΣXᵢ ≥ nγ] ≤ exp(−n sup_{λ≥0}(λγ − ψ(λ))) for every n (p. 292).
- Rate function ψ*: the conjugate of the log MGF ψ. For non-constant X it is strictly convex, strictly positive except ψ*(E[X]) = 0, and equals +∞ outside the range [A, B] of X (at the endpoints it equals log 1/P(X=γ)). Its derivative inverts ψ′ (pp. 296–297).
- Tilting P_λ ∝ e^{λx}P moves the mean to ψ′(λ) and costs divergence D(P_λ‖P) = ψ*(ψ′(λ)) (p. 298).
- Large-deviation exponent = information projection: (1/n) log 1/P[mean ≥ γ] → inf_{E_Q[X]≥γ} D(Q‖P). A non-asymptotic upper bound exp(−n·inf D) holds for every n (p. 299).
- The I-projection onto the half-space {E_Q[X] ≥ γ} equals the tilt P_λ with ψ′(λ) = γ when E_P[X] ≤ γ < B (and is P itself when γ < E_P[X]); the value is ψ*(γ)·1{γ ≥ E_P X} (p. 304).
- Pythagorean geometry: for a convex set only D(Q‖P) ≥ D(Q‖Q*) + D(Q*‖P) is shown (p. 303). For any Q with the same mean as the tilt P_λ, equality D(Q‖P) = D(Q‖P_λ) + D(P_λ‖P) holds (p. 305). The author argues informally that the tilted family is a KL "geodesic" meeting each mean-slice orthogonally (pp. 303–306).
- Sanov: P[P̂ ∈ E] = exp(−n min_{Q∈E} D(Q‖P) + o(n)) for convex E under regularity conditions (p. 307).
- With d linear constraints (under assumptions (a),(b) of Thm 15.16), a tilt exp(λᵀφ − ψ) with the required mean exists iff γ lies in the interior of the convex support of φ(X). Sinkhorn's coupling problem is an example (pp. 309, 311–312).

## L3 — Walkthrough

### Chapter overview (p. 291)
Goal: tools for error exponents in hypothesis testing (Chernoff regime). The chapter says the next chapter will give the (E₀,E₁) region (E₀(θ)=ψ*_P(θ), E₁(θ)=ψ*_P(θ)−θ), with ψ*_P the rate function of log dP/dQ under P. Large deviations seeks sharp estimates P[P̂ₙ ∈ E] = exp{−nE + o(n)}, where P̂ₙ = (1/n)Σδ_{Xᵢ} is the empirical distribution. Only a simple special case is treated (p. 291).

### 15.1 Basics of large deviations theory
**Theorem 15.1** (p. 292). Let ψ_X(λ)=log E[exp(λX)] be finite for all λ∈ℝ, B = esssup X, E[X] < γ < B. Then
$$P\Big[\sum_{i=1}^n X_i \ge n\gamma\Big]=\exp\{-nE(\gamma)+o(n)\},\qquad E(\gamma)=\sup_{\lambda\ge0}\lambda\gamma-\psi_X(\lambda)=\psi_X^*(\gamma).$$

*Upper bound (p. 292).* For λ ≥ 0, Markov's inequality gives
$$P\Big[\sum X_i\ge n\gamma\Big]=P\Big[e^{\lambda\sum X_i}\ge e^{n\lambda\gamma}\Big]\le e^{-n\lambda\gamma}E\Big[e^{\lambda\sum X_i}\Big]=\exp(-n\lambda\gamma+n\psi_X(\lambda)).$$
Optimising over λ ≥ 0 gives, for every n,
$$P\Big[\sum X_i\ge n\gamma\Big]\le\exp\Big\{-n\sup_{\lambda\ge0}(\lambda\gamma-\psi_X(\lambda))\Big\}.\tag{15.1}$$
The lower bound is deferred: first express E(γ) as a KL minimisation (Thm 15.9), then solve it (15.26). The author says (15.1) is a change of measure to the Q closest to P in KL among Q with E_Q[X] ≥ γ, and that this Q turns out to be the tilted P_λ (p. 292). *(added step: combining (15.10) with (15.26) gives, for E[X] < γ < B, the exponent ψ*(γ); this is the plan the author states on p. 292.)*

#### 15.1.1 Log MGF and rate function
**Definition 15.2.** ψ_X(λ) = log E[exp(λX)], λ∈ℝ (the cumulant generating function). Write ψ_P if X∼P. Example: standard Gaussian gives ψ_Z(λ)=λ²/2; X=Z³ has ψ_X(λ)=∞ for all λ≠0 (p. 293).

**Assumption 15.1 (Cramér's condition).** ψ_X(λ)<∞ for all λ∈ℝ. The author says most results hold when the domain of ψ_X merely has non-empty interior, but avoids that for clarity. The assumption implies all moments are finite (p. 293).

**Theorem 15.3 (properties of ψ_X)**, under Assumption 15.1 (p. 293):
(a) ψ_X is convex; (b) continuous; (c) infinitely differentiable with
$$\psi_X'(\lambda)=\frac{E[Xe^{\lambda X}]}{E[e^{\lambda X}]}=e^{-\psi_X(\lambda)}E[Xe^{\lambda X}],$$
so ψ_X(0)=0, ψ_X′(0)=E[X]; (d) if a ≤ X ≤ b a.s. then a ≤ ψ′_X ≤ b; (e) conversely, with A = inf_λ ψ′_X(λ), B = sup_λ ψ′_X(λ), we have A ≤ X ≤ B a.s.; (f) if X is not constant, ψ_X is strictly convex, so ψ′_X is strictly increasing; (g) Chernoff bound P(X ≥ γ) ≤ exp(−λγ+ψ_X(λ)), λ ≥ 0 (15.2).

**Remark 15.1** (pp. 293–294). By (d) and (e), the smallest closed interval containing the support of P_X equals (the closure of) the range of ψ′_X; so A = essinf X ≜ sup{a: X ≥ a a.s.} and B = esssup X ≜ inf{b: X ≤ b a.s.}. Figure 15.1 plots ψ for X=±1 with P[X=1]=1/3; slopes tend to A and B at the ends, and the slope at 0 is E[X] (p. 294).

*Proof sketch* (pp. 294–296; base e):
- (g) is (15.1). Parts (e)–(f) use Theorem 15.8.
- (a) Hölder's inequality E|UV| ≤ ‖U‖ₚ‖V‖_q with 1/p+1/q=1, applied with p=1/θ, q=1/θ̄ to E[e^{(θλ₁+θ̄λ₂)X}], gives $e^{\psi_X(\theta\lambda_1+\bar\theta\lambda_2)}\le e^{\psi_X(\lambda_1)\theta}e^{\psi_X(\lambda_2)\bar\theta}$.
- (b) A convex function is continuous on the interior of its domain, which is ℝ here.
- (c) Differentiation under E needs care. Assume w.l.o.g. λ ≥ 0. Use |Xe^{λX}| ≤ e^{|(λ+1)X|} ≤ e^{(λ+1)X}+e^{−(λ+1)X} and dominated convergence, so E|Xe^{λX}| exists and is continuous. Then by Fubini, $e^{\psi_X(\lambda)}=1+\int_0^\lambda E[Xe^{uX}]du$. Differentiating gives ψ′e^ψ=E[Xe^{λX}] (p. 295). Extending to complex λ shows holomorphy, hence infinite differentiability.
- (d) ψ′ is a ratio of E[Xe^{λX}] to E[e^{λX}], so it lies in [a,b].
- (e) By contradiction. Suppose P[X>B]>0, so P[X>B+2ε]>0. Then P_λ[X ≤ B+ε]→0 as λ→∞ (Thm 15.8(d)), while E_{P_λ}[X]=ψ′(λ) ≤ B. Assume B−ε>0 (otherwise replace X by X−2B). Splitting the expectation gives (15.3): B ≥ −E_{P_λ}[|X|1{X<B−ε}] + (B+ε)P_λ[X>B+ε], the last probability →1. It remains to show the first term →0. Since ψ′↗B, for λ ≥ λ₀ we have ψ(λ) ≥ c + λ(B−ε/2) (15.4). Then E_{P_λ}[|X|1{X<B−ε}] ≤ E|X|·e^{−λε/2−c}→0. This is a contradiction.
- (f) If ψ_X were affine near some λ₀, i.e. ψ_X(λ₀+u)=ψ_X(λ₀)+ur, then E_{P_λ₀}[e^{u(X−r)}]=1 for small u. Lemma 15.4 gives X=r a.s., contradicting non-constancy (p. 296).

**Lemma 15.4.** If E[e^{uS}]=1 for all u∈(−ε,ε), then S=0. Proof: Taylor expansion gives E[S]=0, E[S²]=0 (or use holomorphy and uniqueness) (p. 296).

**Definition 15.5 (rate function).** The Fenchel–Legendre (convex) conjugate of ψ_X:
$$\psi_X^*(\gamma)=\sup_{\lambda\in\mathbb R}\lambda\gamma-\psi_X(\lambda).\tag{15.5}$$
The objective is concave in λ, so one finds the maximum from the stationary point (p. 296).

**Theorem 15.6 (properties of ψ*_X)**, X non-constant, Assumption 15.1 (p. 296):
(a) With A = essinf X, B = esssup X:
ψ*_X(γ) = λγ − ψ_X(λ) for the λ with γ=ψ′_X(λ), when A<γ<B; = log 1/P(X=γ) when γ=A or B; = +∞ when γ<A or γ>B.
(b) ψ*_X is strictly convex and strictly positive except ψ*_X(E[X])=0.
(c) ψ*_X decreases on (A, E[X]) and increases on [E[X], B).

*Proof* (p. 297). For γ∈(A,B), the strictly concave map λ↦λγ−ψ_X(λ) has one stationary point, the unique maximum. For γ>B (resp. <A) it grows without bound. For γ=B: $\psi^*_X(B)=-\log\inf_\lambda E[e^{\lambda(X-B)}]=-\log\lim_{\lambda\to\infty}E[e^{\lambda(X-B)}]=-\log P(X=B)$ by monotone convergence. Since ψ_X is strictly convex, ψ′_X and the derivative of ψ*_X are inverse to each other, so ψ* is strictly convex. ψ_X(0)=0 gives ψ* ≥ 0, and ψ*(E[X])=0 follows from ψ′(0)=E[X].

*Intuition note.* ψ is a convex curve. The tangent line of slope γ to this curve crosses the vertical axis at height −ψ*(γ), i.e. ψ*(γ) below the origin (Fig. 15.2). Equivalently, ψ*(γ) is the largest amount by which the line λγ rises above the curve. It is zero at the mean and grows as γ moves toward the edges of the range.

#### 15.1.2 Tilted distribution
**Definition 15.7 (tilting).** For X∼P, λ∈ℝ,
$$P_\lambda(dx)=\frac{e^{\lambda x}}{E[e^{\lambda X}]}P(dx)=e^{\lambda x-\psi_X(\lambda)}P(dx).\tag{15.6}$$
The text notes tilting was used in the Donsker–Varadhan proof (Thm 4.6) (p. 297). The family {P_λ} is a standard one-parameter exponential family (p. 298).

Examples (p. 298):
- P=N(0,1): P_λ=N(λ,1).
- P=Ber(1/2): P_λ=Ber(e^λ/(e^λ+1)); P_λ→δ₁ as λ→∞ and →δ₀ as λ→−∞.
- P=Unif[0,1]: p_λ(x)=λe^{λx}/(e^λ−1); P_λ→δ₁ as λ→∞, →δ₀ as λ→−∞.

**Theorem 15.8 (properties of P_λ)**, under Assumption 15.1 (p. 298):
(a) ψ_{P_λ}(u)=ψ_X(λ+u)−ψ_X(λ).
(b) Tilting trades mean for divergence: E_{P_λ}[X]=ψ′_X(λ) ≷ E_P[X] if λ ≷ 0 (15.7), and
$$D(P_\lambda\|P)=\psi_X^*(\psi_X'(\lambda))=\psi_X^*(E_{P_\lambda}[X]).\tag{15.8}$$
(c) Var_{P_λ}(X)=ψ″_X(λ) log e.
(d) If P(X>b)>0 then for all ε>0, P_λ(X ≤ b−ε)→0 as λ→∞; if P(X<a)>0 then P_λ(X ≥ a+ε)→0 as λ→−∞. Hence X_λ ⇒ A as λ→−∞ and X_λ ⇒ B as λ→∞ (in distribution).

*Proof* (pp. 298–299). (a) by definition. (b) E_{P_λ}[X]=E[Xe^{λX}]/E[e^{λX}]=ψ′(λ), strictly increasing with ψ′(0)=E_P[X]. Also
$$D(P_\lambda\|P)=E_{P_\lambda}\log\frac{e^{\lambda X}}{E e^{\lambda X}}=\lambda E_{P_\lambda}[X]-\psi_X(\lambda)=\lambda\psi'_X(\lambda)-\psi_X(\lambda)=\psi_X^*(\psi_X'(\lambda)),$$
the last step by Thm 15.6(a). (c) ψ″=(E[X²e^{λX}]−(E[Xe^{λX}])²)/(E[e^{λX}])² = Var_{P_λ}(X). (d) P_λ(X ≤ b−ε) ≤ E_P[e^{λ(b−ε)−ψ(λ)}1{X ≤ b−ε}] ≤ e^{−λε}e^{λb−ψ(λ)} ≤ e^{−λε}/P[X>b], using the Chernoff bound P[X>b] ≤ exp(−λb+ψ(λ)).

*Intuition note.* Tilting reweights outcomes by e^{λx}, so large values gain weight and the mean rises. The KL price of reaching mean γ this way is exactly ψ*(γ), the same number that appears in the Chernoff bound.

### 15.2 Large-deviations exponents and KL divergence
**Theorem 15.9** (p. 299). Let X₁,X₂,… iid ∼P. For any γ∈ℝ,
$$\lim_{n\to\infty}\frac1n\log\frac{1}{P[\frac1n\sum X_k>\gamma]}=\inf_{Q:E_Q[X]>\gamma}D(Q\|P)\tag{15.9}$$
$$\lim_{n\to\infty}\frac1n\log\frac{1}{P[\frac1n\sum X_k\ge\gamma]}=\inf_{Q:E_Q[X]\ge\gamma}D(Q\|P)\tag{15.10}$$
and for every n the firm bound
$$P\Big[\frac1n\sum X_k\ge\gamma\Big]\le\exp\Big\{-n\inf_{Q:E_Q[X]\ge\gamma}D(Q\|P)\Big\},\tag{15.11}$$
and similarly with > in place of ≥.

**Remark 15.2.** The author notes that existence of the limits follows from subadditivity and Fekete's lemma, without computing the value (p. 299). (See Reading notes on a notation issue.)

*Proof* (pp. 300–301). If P[(1/n)ΣXₖ>γ]=0 then P[X>γ]=0, so every Q with E_Q[X]>γ has Q[X>γ]>0, hence Q⋠P and D(Q‖P)=∞; both sides are ∞. Otherwise let Eₙ={(1/n)ΣXₖ>γ}.

*Lower bound on P[Eₙ].* Fix Q with E_Q[X]>γ. By the weak law of large numbers, Q[Eₙ]=1−o(1). Data processing gives d(Q[Eₙ]‖P[Eₙ]) ≤ D(Q_{Xⁿ}‖P_{Xⁿ}) = nD(Q‖P). The binary-divergence bound is d(Q[Eₙ]‖P[Eₙ]) ≥ −h(Q[Eₙ]) + Q[Eₙ] log(1/P[Eₙ]). Combining,
$$P[E_n]\ge\exp\Big(\frac{-nD(Q\|P)-\log2}{Q[E_n]}\Big).\tag{15.12}$$
Optimising over Q: limsup (1/n) log(1/P[Eₙ]) ≤ inf_{E_Q[X]>γ} D(Q‖P).

*Upper bound on P[Eₙ].* For any event E with P_X(E)>0, log 1/P_X(E) = D(P_{X|X∈E}‖P_X). With P̃_{Xⁿ}=P_{Xⁿ|ΣXᵢ>nγ},
$$\log\frac1{P[E_n]}=D(\tilde P_{X^n}\|P_{X^n})\ge\inf_{Q_{X^n}:E_Q[\sum X_i]>n\gamma}D(Q_{X^n}\|P_{X^n}).\tag{15.13}$$
The last problem "single-letterises" (reduces to n=1; a special case of Ex. III.12). With $P_{X^n}=P^n$, inequality (2.27) of Theorem 2.16 and convexity of divergence (Thm 5.1) give
$$D(Q_{X^n}\|P_{X^n})\ge\sum_{j=1}^nD(Q_{X_j}\|P)\ge nD(\bar Q\|P),\quad\bar Q\triangleq\frac1n\sum_jQ_{X_j}.\tag{15.14}$$
*(added step: E_{Q̄}[X]=(1/n)E_Q[ΣXᵢ], so the constraint E_Q[ΣXᵢ]>nγ becomes E_{Q̄}[X]>γ.)* The author concludes
$$\inf_{Q_{X^n}:E_Q[\sum X_i]>n\gamma}D(Q_{X^n}\|P_{X^n})=n\inf_{Q:E_Q[X]>\gamma}D(Q\|P),\tag{15.15}$$
and the same with ≥ (15.16) (p. 301). Together with (15.13) this gives the lower bound on the exponent in (15.9).

*Proof of (15.10).* The argument (15.13) applies verbatim, giving (1/n) log 1/P[…≥γ] ≥ inf_{E_Q[X]≥γ} D(Q‖P). For the matching upper bound:
- *Case I: P[X>γ]=0.* If P[X≥γ]=0 both sides are +∞. If P[X=γ]>0, then P[ΣXₖ ≥ nγ]=P[X=γ]ⁿ. On the right, D(Q‖P)<∞ forces Q≪P and so Q(X≤γ)=1; E_Q[X]≥γ then forces Q=δ_γ, and the infimum is log 1/P(X=γ).
- *Case II: P[X>γ]>0.* From (15.9), limsup ≤ inf_{E_Q[X]>γ} D(Q‖P). It remains to show (15.17): inf over {>γ} equals inf over {≥γ}. Let P̃=P_{X|X>γ}. For Q with E_Q[X]≥γ set Q̃=ε̄Q+εP̃, which has E_{Q̃}[X]>γ. By convexity D(Q̃‖P) ≤ ε̄D(Q‖P)+ε log(1/P[X>γ]). Let ε→0.

**Remark 15.3.** The bound (15.11) also holds for independent non-identically distributed Xᵢ. Replace (15.14) by D(Q_{Xⁿ}‖P_{Xⁿ}) ≥ ΣD(Q_{Xᵢ}‖P_{Xᵢ}) ≥ nD(Q̄‖P̄), where P̄=(1/n)ΣP_{Xᵢ}, and use P̄ in (15.11) (p. 301).

*Intuition note.* A rare event under P is cheapest if it happens as a typical event under some other distribution Q. The exponent cost is about n·D(Q‖P) (in the units of the log used), and the cheapest Q sets the exponent.

**Example 15.1 (Poisson–Binomial tails)** (pp. 301–302). Let X be a sum of n independent Bernoullis with E[X]=np. Then
$$P[X\ge k]\le\exp\{-nd(k/n\|p)\}\ (k/n>p),\qquad P[X\le k]\le\exp\{-nd(k/n\|p)\}\ (k/n<p),$$
(15.18)–(15.19), using min_{E_Q[X]≥k/n} D(Q‖Ber(p)) = min_{q≥k/n} d(q‖p) = d(k/n‖p). Consequences:
- *Bennett:* P[X ≥ uE[X]] ≤ exp{−E[X]f(u)} for u>1, and P[X ≤ uE[X]] ≤ exp{−E[X]f(u)} for 0 ≤ u<1, with f(u)=u log u−(u−1) log e ≥ 0. It uses d(up‖p) ≥ p f(u) (15.20), which follows from x log(x/y) ≥ (x−y) log e with x=1−up, y=1−p.
- *Bernstein:* P[X>np+t] ≤ e^{−t²/(2(t+np))} for t>0. It follows from Bennett for u>1 via f(u)/log e = ∫₁^u (u−x)/x dx ≥ (1/u)∫₁^u (u−x)dx = (u−1)²/(2u).
- *Okamoto:* P[√X−√(np) ≥ t] ≤ e^{−t²} (15.21) and P[√X−√(np) ≤ −t] ≤ e^{−t²} (15.22). They follow from d(x‖p) ≥ H²(Ber(x),Ber(p)) ≥ (√x−√p)² (7.33), with x=(√(np)+t)²/n. The author notes that [316] shows a stronger bound e^{−2t²} in (15.21). The bounds do not depend on n or p, which the author attributes to the variance-stabilising effect of the square-root transformation. The author also remarks that √X−√(np) has a self-normalising form (p. 302).

### 15.3 Information projection
**Problem.** For a convex set E of distributions and a distribution P, compute inf_{Q∈E} D(Q‖P). Call the minimiser Q* (pp. 302–303).

**Theorem 15.10 (Pythagorean inequality)** (p. 303). If Q*∈E attains min_{Q∈E} D(Q‖P) < ∞, then for all Q∈E
$$D(Q\|P)\ge D(Q\|Q^*)+D(Q^*\|P).$$
*Proof idea.* Assume D(Q‖P)<∞ (this also gives D(Q*‖P)<∞). Take Q^{(λ)}=λ̄Q*+λQ∈E. Since Q* is the minimiser, $0\le\frac{d}{d\lambda}\big|_{\lambda=0}D(Q^{(\lambda)}\|P)=D(Q\|P)-D(Q\|Q^*)-D(Q^*\|P)$. Interchanging derivative and integral needs dominated convergence, with details in [114] (p. 303).

**Remark 15.4.** In the Euclidean analogy the triangle formed by P, Q*, Q (for Q*, Q in a convex set, P outside it) is always obtuse, and is a right triangle only when the convex set has a "flat face". Divergence is similar to the squared Euclidean distance (p. 303).

**Theorem 15.11** (pp. 303–305). Under Assumption 15.1, with A = essinf X, B = esssup X (15.23)–(15.24):
1. $$\min_{Q:E_Q[X]\ge\gamma}D(Q\|P)=\begin{cases}0&\gamma<E_P[X]\\ \psi_P^*(\gamma)&E_P[X]\le\gamma<B\\ \log\frac1{P(X=B)}&\gamma=B\\ +\infty&\gamma>B\end{cases}=\psi_P^*(\gamma)\mathbf 1\{\gamma\ge E_P[X]\}\tag{15.25–15.26}$$
2. Whenever the minimum is finite, the minimiser is unique and equals the tilt $dP_\lambda=\exp\{\lambda X-\psi(\lambda)\}dP$ (15.27). Here P, P_λ live on an abstract space Ω.
3. For γ∈[E_P[X], B): min_{E_Q[X]≥γ} = inf_{E_Q[X]>γ} = min_{E_Q[X]=γ} of D(Q‖P).

*Proof of (15.25).*
- First case: take Q=P.
- Fourth case (γ>B): E_Q[X]>B implies Q[X ≥ B+ε]>0 while P[X ≥ B+ε]=0, so Q⋠P and D=∞.
- Third case (γ=B): if P(X=B)=0 then X<B P-a.s., any feasible Q has Q⋠P, and the minimum is ∞. If P(X=B)>0, finite D forces Q≪P so Q(X≤B)=1; E_Q[X] ≥ B then forces Q=δ_B, with D=log 1/P(X=B).
- Second case: for E_P[X] ≤ γ<B choose the unique λ (≥0) with ψ′(λ)=γ=E_{P_λ}[X], so ψ*(γ)=λγ−ψ(λ). For any Q with E_Q[X] ≥ γ:
$$D(Q\|P)=E_Q\Big[\log\frac{dQ\,dP_\lambda}{dP\,dP_\lambda}\Big]=D(Q\|P_\lambda)+E_Q[\lambda X-\psi_X(\lambda)]\ge D(Q\|P_\lambda)+\lambda\gamma-\psi_X(\lambda)=D(Q\|P_\lambda)+\psi_X^*(\gamma)\ge\psi_X^*(\gamma),\tag{15.28–15.29}$$
with the last inequality an equality iff Q=P_λ (this gives uniqueness). At γ=B with P(X=B)>0 the minimiser δ_B is the limit P_∞ of tilts (Thm 15.8(d)).
- Claim 3 (p. 305): nothing to prove for γ<E_P[X]. For γ ≥ E_P[X], Corollary 15.12 gives inf_{E_Q[X]>γ} D = inf_{γ′>γ} ψ*(γ′), which equals ψ*(γ) since ψ* is increasing and continuous (Thm 15.6). The case min_{E_Q[X]=γ} is handled similarly.

**Remark 15.5 (left tail).** Apply the results to −Xᵢ: for γ<E[X], (1/n) log 1/P[(1/n)ΣXₖ<γ] → inf_{E_Q[X]<γ} D(Q‖P) = ψ*_X(γ); the exponent is again given by the rate function, with negative optimal λ (p. 304).

**Corollary 15.12** (p. 305). For any Q with E_Q[X]∈(A,B) there is a unique λ with E_{P_λ}[X]=E_Q[X] and D(P_λ‖P) ≤ D(Q‖P). The gap is D(Q‖P_λ)=D(Q‖P)−D(P_λ‖P). *Proof:* choose λ with ψ′(λ)=E_Q[X], so D(P_λ‖P)=ψ*(E_Q[X])=λE_Q[X]−ψ(λ), and repeat (15.28)–(15.29) to get D(Q‖P)=D(Q‖P_λ)+D(P_λ‖P). The author remarks that for any Q one can thus find a tilt with the same mean and smaller (or equal) divergence to P, and that the same can be done under multiple linear constraints (Section 15.6*) (p. 305).

*Intuition note.* Among all distributions with a given mean, the tilt of P is the one closest to P. Any other distribution with that mean pays an extra D(Q‖P_λ) on top. This is the author's explanation of why the Chernoff bound is tight: it optimises over exactly this family (p. 292).

### 15.4 I-projection and KL geodesics
Figure 15.4 (p. 306), with a fixed baseline P:
- Each set {Q: E_Q[X]=γ} is a slice of 𝒫(ℝ), the space of distributions on ℝ. As γ varies from −∞ to +∞ the union of these slices fills the space of distributions with finite first moment. For γ<A or γ>B every Q in the slice has Q⋠P.
- For γ between A and B, the slices fill {Q: Q≪P}. By Cor. 15.12 each slice has one tilted element P_λ minimising D(Q‖P).
- The P_λ trace a curve (the exponential family of Def. 15.7). The "geodesic" distance from P to P_λ is measured by ψ*(γ)=D(P_λ‖P).
- The curve meets each slice "orthogonally" at Q*: Thm 15.10 gives D(Q‖P) ≥ D(Q‖Q*)+D(Q*‖P), and Cor. 15.12 turns this into equality with Q*=P_λ.

*Why "geodesic" (intuitive, non-rigorous, p. 306).* Suppose another curve {Q_μ} from P to P_λ also minimised KL distance. E_{Q_μ}[X] changes continuously from E_P[X] to E_{P_λ}[X]. For an intermediate value γ′, the closest point to P in that slice is some P_{μ′}, so connecting P to P_{μ′} instead of Q_μ shortens the distance.

*Abstract version (p. 307).* The tilt can be written dP_μ/dP = (1/Z(μ))(dP_λ/dP)^{μ/λ}. For arbitrary P̃, Q̃ on an abstract measurable space 𝒳 the author defines the geodesic
$$\frac{d\tilde P_\mu}{d\tilde P}\triangleq\frac1{\tilde Z(\mu)}\Big(\frac{d\tilde Q}{d\tilde P}\Big)^{\mu},\quad\mu\in[0,1],\tag{15.30}$$
with Z̃(μ)=exp{(μ−1)D_μ(Q̃‖P̃)} (Rényi divergence). The author attributes the formal justification (finite underlying space) to Cencov [85, Thm 12.3]. His argument: require the connection to be equivariant under (a) permutations, (b) splitting atoms into several atoms, (c) conditioning on an event. A one-parameter family of connections satisfies (a)–(b), including the Levi-Civita connection of the Fisher–Rao metric. Only one connection satisfies (a)–(c); it differs from Fisher–Rao and its geodesics are exactly given by (15.30). Geodesically complete submanifolds in this metric are exactly the exponential families (p. 307).

### 15.5 Sanov's theorem
**Theorem 15.13 (Sanov)** (p. 307). Let X₁,…,Xₙ iid ∼P on 𝒳, P̂=(1/n)Σδ_{Xⱼ}, and E a convex set of distributions. Then, under regularity conditions on E and P,
$$P[\hat P\in E]=\exp\Big\{-n\min_{Q\in E}D(Q\|P)+o(n)\Big\}.$$
Regularity examples (pp. 307–308): (a) 𝒳 finite, P fully supported, E closed with non-empty interior (full proof: Exercise III.23); (b) 𝒳 Polish and inf over int(E) equals inf over cl(E) [120, Thm 6.2.10].

*Intuition note.* Sanov's theorem has the same shape as Theorem 15.9 (the half-space {Q: E_Q[X] ≥ γ} is the set relevant there, p. 303): the empirical distribution lands in a set at an exponential cost set by the KL-closest member of the set.

### 15.6* Information projection with multiple constraints
**Problem** (p. 308). With P on 𝒳 and φ=(φ₁,…,φ_d): 𝒳→ℝ^d,
$$F(\gamma)\triangleq\inf\{D(Q\|P):E_Q[\phi(X)]=\gamma\},\quad\gamma\in\mathbb R^d.\tag{15.31}$$
Taking P uniform corresponds to max-entropy problems. Tilted measures: $P_\lambda(dx)=\exp\{\lambda^\top\phi(x)-\psi(\lambda)\}P(dx)$, λ∈ℝ^d, with ψ the multi-dimensional log MGF (15.32).

**Proposition 15.14.** If some λ has ψ(λ)<∞ and E_{P_λ}[φ(X)]=γ, then P_λ is the unique minimiser of (15.31), and for any Q with E_Q[φ(X)]=γ
$$D(Q\|P)=D(Q\|P_\lambda)+D(P_\lambda\|P).\tag{15.33}$$
*Proof.* D(P_λ‖P)=λᵀγ−ψ(λ)<∞. If D(Q‖P) or D(Q‖P_λ) is finite then Q≪P, and D(Q‖P)−D(Q‖P_λ)=E_Q[log exp{λᵀφ−ψ}]=λᵀγ−ψ(λ)=D(P_λ‖P) (p. 308).

The author notes that Prop. 15.14 does not say for which γ a tilt exists. For d=1, Thm 15.8 showed the means of the P_λ fill (A,B); for d>1 the analogue is the convex support of the push-forward P̃ of P along φ (p. 309).

**Definition 15.15 (convex support)** (p. 309). csupp(P̃)≜∩{S: P̃[S]=1, S closed and convex}, and csupp(P̃)=cl(co(supp P̃)) (15.34). The author shows ⊂ because the right side is closed and convex, and ⊃ by taking any closed half-space H of full measure (so supp P̃ ⊂ H) and intersecting over all such H.

**Theorem 15.16 (I-projection on hyperplane)** (p. 309). Assume (a) (1,φ₁,…,φ_d) are linearly independent P-a.s., and (b) ψ(λ)<∞ for all λ∈ℝ^d. Then:
1. If some Q has E_Q[φ]=γ and D(Q‖P)<∞, then γ∈csupp(P̃).
2. There is a solution λ of E_{P_λ}[φ]=γ iff γ∈int(csupp(P̃)).

**Corollary 15.17.** If γ∈int(csupp(P̃)), problem (15.31) is solved by some P_λ, (15.33) holds, F(γ)=ψ*(γ) and λ=∇F(γ).

**Remark 15.6.** Assumption (b) can be relaxed to the domain of ψ being open ([85, Thm 23.1], [77, Thm 3.6]). Applying Thm 15.16, whenever γ∈int csupp(P̃) the I-projection can be sought in the tilted family P_λ, and only in such case. If γ∉csupp(P̃), every Q with that expectation has D(Q‖P)=∞. If γ∈∂csupp(P̃), a minimiser may exist and be finite but not be a tilt, or every feasible Q may have D=∞ (p. 309).

**Example (p. 310).** P=N(0,1), φ(x)=(x,x²). Then csupp(P̃)={γ₂ ≥ γ₁²}. If γ₂>γ₁², the optimal Q is N(γ₁,γ₂−γ₁²), a tilt of P. If γ₂=γ₁², the only feasible Q is δ_{γ₁}, with D=∞. If γ₂<γ₁², no Q is feasible.

*Exponential-family facts* (p. 310). φ is the vector of statistics, λ the natural parameter, and all P_λ are mutually absolutely continuous. Linear independence gives Cov_{P_λ}[φ]≻0 (15.35). Moments: $E_{P_\lambda}[\phi]=\nabla\psi(\lambda)$, $\mathrm{Cov}_{P_\lambda}[\phi]=\mathrm{Hess}\,\psi(\lambda)\log e$ (15.36). So ψ is strictly convex and ∇ψ strictly monotone: (λ₁−λ₂)ᵀ(∇ψ(λ₁)−∇ψ(λ₂))>0 (15.37). The map λ↦μ(λ)=E_{P_λ}[φ] has Jacobian det Hess ψ>0, so by the inverse function theorem μ(ℝ^d) is open with a smooth inverse. The non-trivial claim is that it is convex and equals int csupp(P̃).

*Proof of Theorem 15.16* (pp. 310–311), with C=csupp(P̃), C_o=int C:
- *Claim 1.* Suppose Q≪P with t=E_Q[φ]∉C. A separating hyperplane gives b, c with bᵀt<c ≤ bᵀp for all p∈C. Since P[φ(X)∈C]=1, Q[bᵀφ ≥ c]=1, contradicting E_Q[bᵀφ]<c.
- *μ(λ)∈C_o.* By claim 1, μ(λ)∈C. The map is smooth and one-to-one with smooth inverse, so the image of a small ball is open, hence μ(λ)∈int C.
- *Every γ∈C_o is attained.* Consider inf_λ ψ(λ)−λᵀγ (15.38). If a minimiser λ* exists, first-order optimality gives ∇ψ(λ*)=γ. It suffices to restrict to a ball ‖λ‖≤R. For γ∈C_o there is ε>0 with
$$c_\epsilon\triangleq\inf_{\|v\|=1}P[v^\top(\phi(X)-\gamma)>\epsilon]>0\tag{15.39}$$
(otherwise compactness yields v* with P[v*ᵀ(φ−γ)>0]=0, so γ is not interior). With v=λ/‖λ‖, $\exp\{\psi(\lambda)-\lambda^\top\gamma\}\ge c_\epsilon\exp\{\epsilon\|\lambda\|\}$, i.e. ψ(λ)−λᵀγ ≥ log c_ε+ε‖λ‖, which justifies the restriction (p. 311).

**Example 15.2 (Sinkhorn's problem)** (pp. 311–312). For P_{X,Y} on finite 𝒳×𝒴, solve min{D(Q_{X,Y}‖P_{X,Y}): Q_X=V_X, Q_Y=V_Y}. Assume P_{X,Y}>0. Take |𝒳|+|𝒴| indicator functions φ_a=1{x=a}, φ_b=1{y=b}; they are linearly independent, and csupp(P̃)=𝒫(𝒳)×𝒫(𝒴). If V_X, V_Y have no zeros they lie in the interior, so the solution is a tilt of P, of the form
$$Q^*_{X,Y}(x,y)=A(x)P_{X,Y}(x,y)B(y).\tag{15.40}$$
The author says the projection also exists on the boundary and with zeros in P, but this needs different treatment [114] (p. 312).

## Toy example (ours)
Fair coin, X∼Ber(1/2), γ=0.75; use natural logs.
- ψ(λ)=ln((1+e^λ)/2); ψ′(λ)=e^λ/(1+e^λ). Setting ψ′(λ)=0.75 gives e^λ=3, λ=ln 3≈1.0986.
- The tilt is P_λ=Ber(e^λ/(e^λ+1))=Ber(3/4) (Example, p. 298).
- Rate: ψ*(0.75)=λγ−ψ(λ)=0.75·1.0986−ln 2=0.8240−0.6931=0.1308.
- Check via KL (Thm 15.11): D(Ber(3/4)‖Ber(1/2))=0.75 ln 1.5+0.25 ln 0.5=0.75·0.4055−0.25·0.6931=0.3041−0.1733=0.1308. ✓
- Chernoff bound (15.11): P[mean ≥ 0.75] ≤ e^{−0.1308n}. For n=4 the exact value is P[ΣXᵢ ≥ 3]=(4+1)/16=0.3125, bound e^{−0.5232}=0.593. For n=20 the exact value is (15504+4845+1140+190+20+1)/2²⁰=21700/1048576≈0.0207, bound e^{−2.616}≈0.073.
- Exact (1/n)ln(1/P) is ≈0.194 at n=20, above 0.1308 as the upper bound requires. The theorem says the gap closes as n→∞, since the bound is sharp to first order in the exponent.

## Concepts
- [[relative-entropy-kl-divergence]] — D(Q‖P); here it is the cost of making a rare event typical under Q (p. 299)
- [[log-mgf-cumulant-generating-function]] (new) — ψ_X(λ)=log E[e^{λX}]; convex, smooth under Cramér's condition, slope range = range of X (pp. 293–294)
- [[cramer-condition]] (new) — ψ_X(λ)<∞ for all λ; simplifying assumption of the chapter (p. 293)
- [[rate-function]] (new) — ψ*_X, convex conjugate of ψ_X; the exponent of the right-tail probability (pp. 292, 296)
- [[chernoff-bound]] (new) — Markov on e^{λΣXᵢ}, optimised over λ≥0; non-asymptotic (pp. 292–293)
- [[exponential-tilting]] (new; canon: exponential family / Gibbs distribution) — P_λ ∝ e^{λx}P; trades mean for divergence D(P_λ‖P)=ψ*(E_{P_λ}X) (pp. 297–298)
- [[information-projection]] (new) — minimiser of D(Q‖P) over a convex set of Q; also called I-projection (pp. 302–303)
- [[pythagorean-identity-for-kl]] (new) — D(Q‖P) ≥ D(Q‖Q*)+D(Q*‖P) for convex E; equality for any Q whose mean matches that of the tilt P_λ (pp. 303, 305–306)
- [[kl-geodesic]] (new) — the tilted curve P_μ treated (informally) as a geodesic; abstract form (15.30) via Rényi divergence (pp. 306–307)
- [[sanov-theorem]] (new) — P[P̂∈E]=exp(−n min_E D(Q‖P)+o(n)) for convex E under regularity (p. 307)
- [[convex-support]] (new) — csupp(P̃)=cl(co(supp P̃)); analogue of [A,B]; its interior is the set of means of the tilts P_λ (pp. 309–310)
- [[data-processing-inequality]] — used to lower-bound P[Eₙ] via binary divergence (p. 300)

## Canonical instances
- [[gaussian-tilt]] — tilting N(0,1) gives N(λ,1) (p. 298)
- [[bernoulli-tilt]] — tilting Ber(1/2) gives Ber(e^λ/(e^λ+1)) (p. 298)
- [[poisson-binomial-tail-bounds]] — Chernoff–KL bound yields Bennett, Bernstein, Okamoto (pp. 301–302)
- [[gaussian-two-moment-projection]] — P=N(0,1), φ=(x,x²): optimal Q=N(γ₁,γ₂−γ₁²) for γ₂>γ₁² (p. 310)
- [[sinkhorn-coupling]] — for P_{X,Y}>0 and marginals without zeros, minimiser has form A(x)P(x,y)B(y) (pp. 311–312)

## Bridges (candidates)
- [structural-analogy] Pythagorean inequality for KL ↔ Euclidean projection onto a convex set: D behaves like (is similar to) squared distance, with obtuse/right triangles (p. 303).
- [same-math] Tilted family P_λ with sufficient statistic φ ↔ statistics: standard exponential family with natural parameter λ and mean parameter μ=∇ψ(λ) (p. 310).
- [same-math] ψ* as convex conjugate of ψ ↔ convex analysis: Fenchel–Legendre transform, as the author notes (cf. (7.84), p. 296).
- [structural-analogy] I-projection with P uniform ↔ maximum entropy principle: the author notes this link (p. 308).
- [structural-analogy] Geodesics (15.30) with Rényi normaliser ↔ information geometry: Cencov's connection differs from Fisher–Rao (p. 307).

## Questions this raises
- What exactly is the "regularity condition" in Sanov's theorem when 𝒳 is infinite, and what goes wrong without it?
- At the boundary γ∈∂csupp(P̃), when does a finite non-tilted I-projection exist?
- How does the one-parameter exponent ψ*(γ) become the two-exponent (E₀,E₁) tradeoff in Chernoff-regime hypothesis testing (next chapter)?
- How are the boundary cases of Sinkhorn's problem (marginals or P with zeros) treated in [114]?

## Reading notes
- Printed pages 291–312; pdf = printed + 25. The unit metadata says "ch17", but the printed chapter number is 15 (title page p. 291).
- Each page carries the header "itbook-export CUP/HE2-design August 16, 2024".
- Theorem 15.1 defines E(γ)=sup_{λ≥0}…, Definition 15.5 uses sup over all λ∈ℝ; Theorem 15.1 states both equal ψ*(γ) for E[X]<γ<B.
- Remark 15.2 (p. 299) as printed defines pₙ ≜ log 1/P[…] and then uses log(1/pₙ). This appears to be a notational slip (presumably pₙ is meant to be the probability itself). I give only the conclusion (existence of the limit).
- (15.32) as printed omits the "log" in ψ(λ) and a closing brace; the definition of P_λ and the proof (p. 308) require ψ to be the log MGF. Section 15.4 text says the distance is "ψ*(λ)", whereas Fig. 15.4 and the bullet before say ψ*(γ).
- Remark 15.5 has a missing word ("simply these results to −Xᵢ", presumably "apply"). The sentence in 15.2's intro ("In the subsequent chapter (information projection).") is garbled.
- The text-layer equations were checked against the page images; no unreadable equations. This unit contains no exercises (exercises III.12, III.23, III.25 are only cited).
