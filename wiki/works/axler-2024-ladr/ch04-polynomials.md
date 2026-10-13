---
id: axler-2024-ladr/ch04-polynomials
work: axler-2024-ladr
unit: "4 Polynomials"
pages: 119–131
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Polynomials

## L0 — One line
Zeros of a polynomial correspond to degree-one factors; since every nonconstant complex polynomial has a zero, every nonconstant complex polynomial splits completely into degree-one factors, and every nonconstant real polynomial into factors of degree at most two.

## L1 — The gist (≤ 120 words)
Axler collects the facts about polynomials that later chapters use to study linear maps from a space to itself. A polynomial of degree m ≥ 1 has at most m zeros, so its coefficients and degree are unique. Each zero gives a factor (z − λ). Polynomials divide with a remainder of smaller degree; the proof uses a basis. Over the complex numbers every nonconstant polynomial has a zero, so it factors uniquely into degree-one pieces. Over the reals, nonreal zeros come in conjugate pairs, so the factors have degree one or two. The author says this failure of the theorem over **R** accounts for later differences between real and complex linear algebra.

**Prerequisites:** vector spaces, basis and dimension (a linearly independent list of length dim V is a basis), linear maps; complex numbers a + bi; induction; polar form of complex numbers.

## L2 — Key ideas
- Complex conjugate and absolute value obey a short list of rules (4.4), including the triangle inequality. These are used later in the real-factorization proof. (pp. 120–121)
- For deg p ≥ 1: p(λ) = 0 if and only if p(z) = (z − λ)q(z) with deg q = deg p − 1. This "factor theorem" is the basic tool. (p. 122)
- A degree-m polynomial has at most m zeros. Hence coefficients and degree are uniquely determined. (p. 123)
- Division algorithm: p = sq + r with deg r < deg s, q and r unique. The proof uses the basis 1, z, …, z^{m−1}, s, zs, …, z^{n−m}s of 𝒫_n(F). (pp. 123–124)
- Fundamental theorem of algebra: every nonconstant complex polynomial has a zero. This is an existence result; it gives no method for finding zeros. Every proof needs some analysis, because the result fails if **C** is replaced by the numbers c + di with c, d rational. (pp. 124–125)
- Consequence: every nonconstant complex polynomial factors uniquely, except for the order of the factors, as c(z − λ₁)⋯(z − λ_m). (p. 126)
- A real polynomial may have no real zeros, but its nonreal complex zeros come in conjugate pairs. (p. 127)
- Over **R**, every nonconstant real polynomial factors uniquely, except for the order of the factors, as a real constant times degree-one factors and quadratics with b² < 4c. (p. 128)

## L3 — Walkthrough

**Intro (p. 119).** F denotes **R** or **C**. The chapter is background for studying linear maps from a space to itself. Read the statements; proofs may be skimmed. The division-algorithm proof is worth reading because it uses linear algebra.

### Complex numbers (pp. 120–121)
- **4.1.** For z = a + bi with a, b real: Re z = a, Im z = b, so z = Re z + (Im z)i. (p. 120)
- **4.2.** Complex conjugate: $\bar z = \operatorname{Re} z - (\operatorname{Im} z)i$. Absolute value: $|z| = \sqrt{(\operatorname{Re} z)^2 + (\operatorname{Im} z)^2}$. (p. 120)
- **4.3 Example.** z = 3 + 2i gives Re z = 3, Im z = 2, $\bar z$ = 3 − 2i, |z| = √(3²+2²) = √13. (p. 120)
- Identifying z with (Re z, Im z) ∈ **R**² makes **C** a two-dimensional real vector space, though it is a one-dimensional complex space. |z| is the distance from the origin to that point. $z=\bar z$ if and only if z is real (left to the reader). (p. 120)
- **4.4 Properties.** For w, z ∈ **C**: (p. 121)
  - $z+\bar z = 2\operatorname{Re} z$; $z-\bar z = 2(\operatorname{Im} z)i$; $z\bar z = |z|^2$.
  - $\overline{w+z}=\bar w+\bar z$; $\overline{wz}=\bar w\,\bar z$; $\bar{\bar z}=z$.
  - $|\operatorname{Re} z|\le|z|$; $|\operatorname{Im} z|\le|z|$; $|\bar z|=|z|$; $|wz|=|w||z|$.
  - Triangle inequality: $|w+z|\le|w|+|z|$.
- Only the triangle inequality is proved; the rest is left to the reader (Ex. 1). Proof: (p. 121)
$$|w+z|^2=(w+z)(\bar w+\bar z)=w\bar w+z\bar z+w\bar z+z\bar w=|w|^2+|z|^2+w\bar z+\overline{w\bar z}$$
$$=|w|^2+|z|^2+2\operatorname{Re}(w\bar z)\le|w|^2+|z|^2+2|w\bar z|=|w|^2+|z|^2+2|w||z|=(|w|+|z|)^2.$$
Take square roots.

*Intuition note:* Conjugation flips the sign of the imaginary part and keeps the length. Multiplying z by $\bar z$ removes the imaginary part and leaves the squared length.

### Zeros of polynomials (pp. 122–123)
- A polynomial of degree m has the form $p(z)=a_0+a_1z+\cdots+a_mz^m$ with $a_m\ne0$. If the coefficients were not unique, a polynomial could have more than one degree; uniqueness is proved below. (p. 122)
- **4.5.** λ ∈ F is a zero (root) of p ∈ 𝒫(F) if p(λ) = 0. (p. 122)
- **4.6 (zero ⇔ degree-one factor).** Let m be a positive integer, p of degree m, and λ ∈ F. Then p(λ) = 0 if and only if there is q ∈ 𝒫(F) of degree m − 1 with p(z) = (z − λ)q(z) for all z ∈ F. (p. 122)
  - (⇒) If p(λ) = 0:
$$p(z)=p(z)-p(\lambda)=a_1(z-\lambda)+\cdots+a_m(z^m-\lambda^m)\tag{4.7}$$
  - Each term uses $z^k-\lambda^k=(z-\lambda)\sum_{j=1}^{k}\lambda^{j-1}z^{k-j}$. So (4.7) is (z − λ) times a polynomial of degree m − 1. (p. 122)
  - (⇐) If p(z) = (z − λ)q(z), then p(λ) = (λ − λ)q(λ) = 0. (p. 122)
- **4.8.** A polynomial of degree m ≥ 1 has at most m zeros in F. (p. 123)
  - Induction on m. For m = 1, a₀ + a₁z with a₁ ≠ 0 has the single zero −a₀/a₁.
  - For m > 1: if p has no zero, done. Otherwise take a zero λ and write p = (z − λ)q by 4.6.
  - By the induction hypothesis q has at most m − 1 zeros. The zeros of p are exactly the zeros of q together with λ, so there are at most m.
- **Consequences.** Two different coefficient lists for one function would give, on subtracting, a nonzero polynomial with infinitely many zeros. So coefficients are unique, and so is the degree. The 0 polynomial has degree −∞, so that deg(pq) = deg p + deg q holds without exceptions. (p. 123)

*Intuition note:* Each zero "uses up" one degree through a factor (z − λ). So a nonconstant polynomial cannot have more zeros than its degree.

### Division algorithm (pp. 123–124)
- For integers, p = sq + r with r < s. The polynomial analogue is not really an algorithm, only an existence-and-uniqueness result. 𝒫_n(F) is the (n+1)-dimensional space of polynomials of degree ≤ n. (p. 123)
- **4.9.** Let p, s ∈ 𝒫(F) with s ≠ 0. Then there are unique q, r ∈ 𝒫(F) with p = sq + r and deg r < deg s. (p. 124)
  - Let n = deg p and m = deg s. If n < m, take q = 0 and r = p. Assume n ≥ m.
  - The list
$$1,z,\dots,z^{m-1},\;s,\;zs,\dots,z^{n-m}s\tag{4.10}$$
  is linearly independent in 𝒫_n(F), because its members have different degrees. Its length is m + (n − m + 1) = n + 1 = dim 𝒫_n(F), so it is a basis (by 2.38).
  - Since p ∈ 𝒫_n(F), there are unique constants $a_0,\dots,a_{m-1}$ and $b_0,\dots,b_{n-m}$ with
$$p=\underbrace{a_0+a_1z+\cdots+a_{m-1}z^{m-1}}_{r}+s\underbrace{(b_0+b_1z+\cdots+b_{n-m}z^{n-m})}_{q}.\tag{4.11}$$
  - So p = sq + r with deg r < deg s. Uniqueness of q and r follows from uniqueness of the constants in (4.11).

*Intuition note:* The first m basis vectors span "everything of degree below deg s". The others are multiples of s. Splitting p along this basis separates the remainder from the quotient.

### Factorization over **C** (pp. 124–126)
- Margin notes: the fundamental theorem is an existence theorem and gives no method for finding zeros. Explicit formulas exist for degrees 2, 3, 4 but not for degree 5 and up. (p. 124)
- The proof uses analysis: a continuous real function on a closed disk in **R**² attains a minimum (used implicitly). Every proof needs some analysis, because the result fails if **C** is replaced by the numbers c + di with c, d rational. (pp. 124–125)
- **4.12 (first version).** Every nonconstant polynomial with complex coefficients has a zero in **C**. (p. 125)
  - *Roots exist.* De Moivre: $(\cos\theta+i\sin\theta)^k=\cos k\theta+i\sin k\theta$ for positive integer k and real θ. If $r(\cos\theta+i\sin\theta)=w$, then $\big(r^{1/k}(\cos\tfrac\theta k+i\sin\tfrac\theta k)\big)^k=w$. So every complex number has a kth root.
  - *Minimum.* Let p have highest-order nonzero term $c_mz^m$. Then |p(z)| → ∞ as |z| → ∞, because |p(z)|/|z^m| → |c_m|. So z ↦ |p(z)| has a global minimum at some ζ. Suppose p(ζ) ≠ 0.
  - Define q(z) = p(z + ζ)/p(ζ). Then |q| has global minimum 1 at z = 0. Write q(z) = 1 + a_k z^k + ⋯ + a_m z^m with k the smallest positive index where the coefficient is nonzero.
  - Pick β with β^k = −1/a_k. There is a constant c > 1 such that for t ∈ (0, 1)
$$|q(t\beta)|\le|1+a_kt^k\beta^k|+t^{k+1}c=1-t^k(1-tc).$$
  - (added step: $|1+a_kt^k\beta^k|=|1-t^k|=1-t^k$.)
  - Taking t = 1/(2c) gives |q(tβ)| < 1, contradicting that the minimum is 1. So p(ζ) = 0.
- Computers can approximate zeros even when no exact formula exists. Example: $p(x)=x^5-5x^4-6x^3+17x^2+4x-7$ has zeros approximately −1.87, −0.74, 0.62, 1.47, 5.51. (p. 126)
- **4.13 (second version).** If p ∈ 𝒫(**C**) is nonconstant, it has a unique factorization, up to order, $p(z)=c(z-\lambda_1)\cdots(z-\lambda_m)$ with c, λ₁, …, λ_m ∈ **C**. The λ's are the only zeros of p. (p. 126)
  - Induction on m = deg p; m = 1 is clear. *Existence:* by 4.12 p has a zero λ, and by 4.6 p = (z − λ)q with deg q = m − 1. Factor q by the induction hypothesis.
  - *Uniqueness:* c is the coefficient of z^m. Suppose $(z-\lambda_1)\cdots(z-\lambda_m)=(z-\tau_1)\cdots(z-\tau_m)$ for all z. The left side is 0 at λ₁, so some τ equals λ₁; relabel τ₁ = λ₁.
  - Divide by z − λ₁. This gives equality for z ≠ λ₁, and then for all z, since otherwise a nonzero polynomial would have infinitely many zeros. Apply the induction hypothesis.

*Intuition note:* Existence of one zero is the hard analytic step. After that, 4.6 peels off one factor at a time until nothing is left but degree-one factors.

### Factorization over **R** (pp. 127–129)
- A real polynomial may have no real zero, for example 1 + x². (p. 127)
- **4.14.** If p ∈ 𝒫(**C**) has real coefficients and λ ∈ **C** is a zero, so is $\bar\lambda$. Proof: conjugate $a_0+a_1\lambda+\cdots+a_m\lambda^m=0$ using 4.4. Since each $a_j$ is real, this gives $a_0+a_1\bar\lambda+\cdots+a_m\bar\lambda^m=0$. (p. 127)
- **4.15.** For b, c ∈ **R**: $x^2+bx+c=(x-\lambda_1)(x-\lambda_2)$ with λ₁, λ₂ ∈ **R** if and only if b² ≥ 4c. (p. 127)
  - Start from $x^2+bx+c=\left(x+\tfrac b2\right)^2+\left(c-\tfrac{b^2}{4}\right)$ (completing the square).
  - If b² < 4c, the right side is positive for all real x, so there is no real zero and no real factorization.
  - If b² ≥ 4c, choose real d with $d^2=\tfrac{b^2}{4}-c$. Then $x^2+bx+c=\left(x+\tfrac b2\right)^2-d^2=\left(x+\tfrac b2+d\right)\left(x+\tfrac b2-d\right)$. (p. 128)
- **4.16.** A nonconstant p ∈ 𝒫(**R**) has a unique factorization, up to order,
$$p(x)=c(x-\lambda_1)\cdots(x-\lambda_m)(x^2+b_1x+c_1)\cdots(x^2+b_Mx+c_M),$$
with all constants real and $b_k^2<4c_k$ for each k. Either m or M may be 0. The λ's are exactly the real zeros of p. (p. 128)
  - *Existence idea:* if (x − λ) is a factor with λ nonreal, then (x − $\bar\lambda$) is too. Their product is $x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2$. Caution: 4.14 does not say the two factors appear equally often, and the proof works around this. (p. 128)
  - *Proof of existence:* view p in 𝒫(**C**). If all zeros are real, use 4.13. Otherwise take nonreal λ; by 4.14 $\bar\lambda$ is also a zero, so
$$p(x)=(x-\lambda)(x-\bar\lambda)q(x)=(x^2-2(\operatorname{Re}\lambda)x+|\lambda|^2)\,q(x),$$
  with q ∈ 𝒫(**C**) of degree two less. (pp. 128–129)
  - Claim: q has real coefficients. For real x, q(x) = p(x)/(x² − 2(Re λ)x + |λ|²) is real. Write q(x) = a₀ + ⋯ + a_{n−2}x^{n−2}. Then $0=\operatorname{Im}q(x)=(\operatorname{Im}a_0)+\cdots+(\operatorname{Im}a_{n-2})x^{n-2}$ for all real x. By 4.8 all Im a_j = 0. Induction on the degree finishes existence. (p. 129)
  - *Uniqueness:* a factor x² + b_k x + c_k with b_k² < 4c_k can be uniquely written as (x − λ_k)(x − $\bar\lambda_k$) with λ_k ∈ **C**. Two different factorizations over **R** would give two different factorizations over **C**, contradicting 4.13. (p. 129)

*Intuition note:* Nonreal zeros of a real polynomial pair up as conjugates. Each pair multiplies into one real quadratic that has no real zero.

## Toy example (ours)
Take $p(x)=x^3-1$.
1. A zero is x = 1. By 4.7's identity, $x^3-1^3=(x-1)(1+x+x^2)$, so q = x² + x + 1, of degree 2 = 3 − 1.
2. For q: b = 1, c = 1, b² = 1 < 4 = 4c. By 4.15 there is no real factorization.
3. Over **C**, q has zeros ω = (−1 + i√3)/2 and its conjugate $\bar\omega$ (conjugate pair, 4.14). Check: Re ω = −1/2 and |ω|² = 1/4 + 3/4 = 1, so $x^2-2(\operatorname{Re}\omega)x+|\omega|^2=x^2+x+1$ ✓.
4. 4.13 gives $x^3-1=(x-1)(x-\omega)(x-\bar\omega)$. 4.16 gives $x^3-1=(x-1)(x^2+x+1)$ with m = 1, M = 1.

Division-algorithm check with p = z³ + 2z² + 3z + 4, s = z² + 1 (n = 3, m = 2). Basis (4.10): 1, z, z²+1, z³+z. Solve p = a₀ + a₁z + b₀(z²+1) + b₁(z³+z). Matching coefficients: z³: b₁ = 1; z²: b₀ = 2; z: a₁ + b₁ = 3, so a₁ = 2; constant: a₀ + b₀ = 4, so a₀ = 2. So r = 2 + 2z, q = 2 + z. Check: (z²+1)(z+2) = z³ + 2z² + z + 2, plus 2z + 2 gives z³ + 2z² + 3z + 4 ✓.

## Concepts
- [[basis]] — here the explicit basis (4.10) of 𝒫_n(F) used for division (p. 124)
- [[dimension]] — dim 𝒫_n(F) = n + 1 (p. 123)
- [[linear-independence]] — the list (4.10) is independent because its members have distinct degrees (p. 124)
- [[linear-map]] — appears only in the exercises (Ex. 10, 14) (pp. 130–131)
- [[complex-conjugate]] (new) — $\bar z=\operatorname{Re}z-(\operatorname{Im}z)i$; satisfies $z\bar z=|z|^2$ (p. 120)
- [[triangle-inequality]] (new) — |w + z| ≤ |w| + |z| for complex numbers (p. 121)
- [[polynomial-zero]] (new) — λ with p(λ) = 0; also called a root (p. 122)
- [[factor-theorem]] (new) — 4.6: p(λ) = 0 iff (z − λ) divides p with quotient of degree one less (p. 122)
- [[polynomial-division-algorithm]] (new) — 4.9: unique q, r with p = sq + r and deg r < deg s (p. 124)
- [[fundamental-theorem-of-algebra]] (new) — 4.12/4.13: nonconstant complex polynomials have a zero and factor uniquely into degree-one terms (pp. 125–126)
- [[conjugate-pair-zeros]] (new) — 4.14: nonreal zeros of real polynomials come with their conjugates (p. 127)

## Canonical instances
- [[quintic-numerical-zeros]] — x⁵ − 5x⁴ − 6x³ + 17x² + 4x − 7 has no exact formula for its zeros, but five numerical zeros (p. 126)
- [[one-plus-x-squared]] — 1 + x² is a real polynomial with no real zero (p. 127)
- [[rational-complex-counterexample]] — the fundamental theorem fails over the numbers c + di with c, d rational (p. 125)

## Bridges (candidates)
- [structural-analogy] polynomial division p = sq + r ↔ number theory: integer division with remainder — the author states the analogy himself (p. 123)
- [structural-analogy] zeros of a polynomial ↔ linear algebra: eigenvalues as zeros of the characteristic polynomial — the unit only says polynomials will be used for maps from a space to itself (p. 119); the link itself is not stated here
- [structural-analogy] conjugate pairs of nonreal zeros ↔ real matrices: complex eigenvalues of real matrices come in pairs — the author only says the failure of the theorem over **R** will matter later (p. 127)

## Questions this raises
- If the fundamental theorem gives no method for finding zeros, how do numerical methods locate them, and how reliable are they? (p. 126)
- How do multiplicities of zeros enter the unique factorizations in 4.13 and 4.16? (pp. 126, 128)
- Why does the order-of-factors uniqueness matter once p is replaced by a linear map? (p. 119)
- Is the quotient space 𝒫(F)/U in Ex. 13 a good way to think of "remainders"? (p. 131)

## Exercises worth doing
- Ex. 2 (p. 129) — reverse triangle inequality from the triangle inequality — easy
- Ex. 7 (p. 130) — unique polynomial of degree ≤ m through m + 1 given points, via linear algebra — medium
- Ex. 9 (p. 130) — real polynomials of odd degree have a real zero — medium
- Ex. 13 (p. 131) — dim 𝒫(F)/U = deg p for U = multiples of p (links division to quotient spaces) — hard
- Ex. 14 (p. 131) — rp + sq = 1 for polynomials with no common zero, via injective and surjective linear map T — hard

## Reading notes
- Printed page = pdf − 14. Page labels give printed numbers; I cite them.
- The text layer shows mathematical symbols as "��"; I read all formulas from the page images.
- The unit has margin remarks; I used only those reported above. Exercises 1–14 are on pp. 129–131; no solutions are printed here.
- The proof of 4.12 asserts "a constant c > 1" without proving it, and cites the minimum-on-a-closed-disk fact as known (pp. 124–125).
- No misprints noticed in the images.
