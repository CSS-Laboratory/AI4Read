---
id: spielman-2025-sagt/ch16-lov
work: spielman-2025-sagt
unit: "Chapter 16 — The Lovàsz–Simonovits Approach to Random Walks"
pages: 142–146
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Lovàsz–Simonovits Approach to Random Walks

## L0 — One line
After one lazy-walk step, the "sum of the k largest entries" curve of a vector lies below a chord of the old curve whose width grows with the graph's conductance; the same tool gives a variant of Cheeger's inequality.

## L1 — The gist (≤ 120 words)
How fast does a lazy random walk (it stays put with probability ½) on a regular graph mix, and how does this relate to conductance (edges leaving a set, relative to its size)? For a vector f, let f{k} be the sum of its k largest entries. Theorem 16.1.1 (Lovàsz–Simonovits) says that if the graph has conductance at least φ, then g = Wf satisfies g{k} ≤ ½(f{k−φh} + f{k+φh}), with h = min(k, n−k). So the curves p_t{x} sit under each other and under chords of the previous curve. Andersen's argument then applies the theorem to the second eigenvector (eigenvalue 1−λ) and gives a set S with φ(S) ≤ √(8λ), a variant of Cheeger's inequality. The notes are a rough draft.

**Prerequisites:** eigenvectors of a symmetric matrix; convex vs concave functions; edge boundary and conductance; Taylor series of √(1±φ).

## L2 — Key ideas
- Define f{k} as the sum of the k largest entries of f, extended piecewise linearly to real x. The result is a concave function, because its slopes do not increase (p. 142).
- Main theorem: for a lazy walk on a d-regular graph with conductance at least φ, g{k} ≤ ½(f{k−φh}+f{k+φh}) (p. 142).
- Reading the theorem: the curves p_t{x} lie under each other and under chords of the previous curve. The walk is uniformly mixed when the curve is the line from (0,0) to (n,1) (p. 143).
- Warm-up: with no conductance assumption, g{x} ≤ f{x}. The proof uses that the graph is regular and Claim 16.2.2 (p. 144).
- Key lemma: the sum over a ∉ S of γ(a,S) (the chance that a walk at a steps into S) equals (φ(S)/2)·min(k, n−k). This is where conductance enters (p. 144).
- Laziness (γ(a) ≥ ½ on S) allows the split γ = α + β with coefficients in [0,½]. With z = Σ_{a∉S}γ(a) ≥ φh/2, this produces a chord of half-width 2z ≥ φh (p. 145; the source prints z, see Reading notes).
- Andersen's proof of Cheeger: test the theorem on the second eigenvector ψ and obtain a set S with φ(S) ≤ √(8λ) (p. 146).

## L3 — Walkthrough

### 16.1 Introduction (pp. 142–143)
- **Definition.** Let π sort f so that f(π(1)) ≥ … ≥ f(π(n)). Then $f\{k\}=\sum_{i=1}^k f(\pi(i))$, and f{0} = 0 (p. 142).
- For real x in [0,n], f{x} is piecewise linear between integers. On (k, k+1) its slope is f(π(k+1)). The slopes do not increase, so f{x} is concave (p. 142).
- **Theorem 16.1.1.** Let W be the transition matrix of the lazy random walk on a d-regular graph with conductance at least φ, and g = Wf. Then for integers 0 ≤ k ≤ n,
$$g\{k\}\le \tfrac12\big(f\{k-\phi h\}+f\{k+\phi h\}\big),\quad h=\min(k,n-k).$$
(p. 142). The author says the theorem extends cleanly to irregular weighted graphs, but presents only the regular case (p. 143).
- **Use.** Let p_t be the distribution after t steps. The theorem says the curves p_t{x} lie beneath each other and beneath chords of the previous curve. Mixing is complete at the line from (0,0) to (n,1) (p. 143).

*Intuition note.* One step of the walk cannot raise the "top-k sum" curve (Lemma 16.3.1, p. 144). The theorem also bounds it by a chord average whose width grows with φ, so a larger conductance gives a lower bound (the author expects this: larger conductance "should" give lower curves, p. 143).

### 16.2 Definitions and elementary observations (p. 143)
- Larger conductance should mean faster mixing, i.e. lower curves, because wider chords lie beneath narrower ones (p. 143).
- **Claim 16.2.1.** For z > y > 0, ½(h(x−z)+h(x+z)) ≤ ½(h(x−y)+h(x+y)). The source says "convex", but the argument needs concave (see Reading notes). It is used for f{x}, which is concave (p. 143).
- **Claim 16.2.2.** If 0 ≤ α_i ≤ 1 and Σα_i = k, then Σα_i f(i) ≤ f{k}. The author calls it obvious: the sum is maximised by putting weight 1 on the largest values (p. 143).
- **γ(a,S)** is the probability that a walk at a moves into S in one step. For a ∉ S it is half the fraction of a's edges going to S. For a ∈ S it is ½ plus half the fraction of a's edges ending in S (p. 143).

### 16.3 Warm-up (pp. 143–144)
- Write $f(S)=\sum_{a\in S}f(a)$. For each k there is a set S with f(S) = f{k}; it is unique if the values of f are distinct (p. 144).
- **Lemma 16.3.1.** If g = Wf, then g{x} ≤ f{x} for all x in [0,n] (p. 144).
- *Proof.* Piecewise linearity means integers k suffice. Take S of size k with f(S) = f{k}. Then $g(S)=\sum_a\gamma(a,S)f(a)$. By regularity, $\sum_a\gamma(a,S)=k$. Claim 16.2.2 gives $\sum_a\gamma(a,S)f(a)\le f\{k\}$ (p. 144).

### 16.4 The proof (pp. 144–145)
- Conductance of S in a d-regular graph: $\phi(S)=\dfrac{|\partial(S)|}{d\min(|S|,n-|S|)}$ (p. 144).
- **Lemma 16.4.1.** For |S| = k, $\sum_{a\notin S}\gamma(a,S)=(\phi(S)/2)\min(k,n-k)$. *Proof:* for a ∉ S, γ(a,S) is half the fraction of a's edges landing in S, and the number of edges leaving S is dφ(S)min(k, n−k) (p. 144).
- **Lemma 16.4.2.** For S of size k with conductance at least φ, $g(S)\le\frac12(f\{k-\phi h\}+f\{k+\phi h\})$ (p. 144).
- *Proof* (p. 145). Write γ(a) = γ(a,S), so $g(S)=\sum_a\gamma(a)f(a)$ and $\sum_a\gamma(a)=k$. Define
$$\alpha(a)=\begin{cases}\gamma(a)-\tfrac12 & a\in S\\ 0 & a\notin S\end{cases},\qquad \beta(a)=\begin{cases}\tfrac12 & a\in S\\ \gamma(a)& a\notin S.\end{cases}$$
  - Then α+β = γ, so $g(S)=\sum\alpha(a)f(a)+\sum\beta(a)f(a)$.
  - Laziness gives γ(a) ≥ ½ on S. Hence 0 ≤ α ≤ ½, and likewise 0 ≤ β ≤ ½, and $g(S)=\tfrac12\sum(2\alpha)f+\tfrac12\sum(2\beta)f$ with coefficients in [0,1].
  - Since $\sum_a\beta(a)=k/2+\sum_{a\notin S}\gamma(a)$, set $z=\sum_{a\notin S}\gamma(a)$. Then $\sum 2\alpha=k-2z$ and $\sum 2\beta=k+2z$.
  - Lemma 16.4.1 gives z ≥ φh/2.
  - Claim 16.2.2 gives $g(S)\le\frac12(f\{k-2z\}+f\{k+2z\})$ (added step: the source prints z, not 2z; see Reading notes).
  - Since 2z ≥ φh, Claim 16.2.1 gives the stated bound.
- Theorem 16.1.1 follows by applying Lemma 16.4.2 to sets with f(S) = f{k}, for each integer k (p. 145).

*Intuition note.* A walker in S either stays (the lazy half) or leaves and is replaced by walkers entering. The mass entering is at least φh/2, so the top-k sum is replaced by an average of a "smaller" and a "larger" top-k sum. By concavity, wider chords lie lower (Claim 16.2.1), so this average is at most the one with half-width φh.

### 16.5 Andersen's proof of Cheeger's inequality (p. 146)
- **Theorem 16.5.1.** Let G be d-regular with lazy walk matrix W, and let ω₂ = 1−λ be the second-largest eigenvalue of W. Then some S has $\phi(S)\le\sqrt{8\lambda}$ (p. 146).
- *Proof.*
  - Let ψ be the eigenvector for ω₂. It is orthogonal to constant vectors, so ψ{n} = 0.
  - Choose $k=\arg\max_{0\le k\le n}\psi\{k\}/\sqrt{\min(k,n-k)}$ and let γ be the maximum value.
  - WLOG k ≤ n/2: otherwise replace ψ by −ψ, which gives the same γ. Then ψ{k} = γ√k.
  - Let S satisfy ψ(S) = ψ{k}. Since the eigenvalue is positive, (Wψ)(S) = Wψ{k}. Also (Wψ)(S) = (1−λ)ψ(S) = (1−λ)γ√k.
  - Let φ = φ(S). Lemma 16.4.2 gives $(W\psi)(S)\le\frac12(\psi\{k-\phi k\}+\psi\{k+\phi k\})$.
  - By the choice of k and γ, this is at most $\frac12(\gamma\sqrt{k-\phi k}+\gamma\sqrt{k+\phi k})=\gamma\sqrt k\,\frac12(\sqrt{1-\phi}+\sqrt{1+\phi})$.
  - Combining the inequalities and dividing by γ√k (added step: γ > 0 is implicit in the source), $1-\lambda\le\frac12(\sqrt{1-\phi}+\sqrt{1+\phi})$. The source prints a stray γ here (see Reading notes).
  - "An examination of the Taylor series" shows the right side is ≤ 1 − φ²/8. Hence λ ≥ φ²/8, so φ(S) ≤ √(8λ) (p. 146). The source gives no further steps.

*Intuition note.* If the walk barely shrinks the eigenvector (λ small), the chosen set S cannot have large conductance: φ(S) ≤ √(8λ). The reason is that the argument gives 1−λ ≤ 1−φ²/8, so a large φ would force a large λ.

## Toy example (ours)
Take the 4-cycle 1–2–3–4–1 (d = 2, n = 4). The lazy walk is $(Wf)(a)=\tfrac12 f(a)+\tfrac14\,(\text{sum of } f \text{ over the 2 neighbours})$. Conductances:
- singletons: 2/(2·1) = 1;
- adjacent pairs: ∂ = 2, so 2/(2·2) = ½;
- opposite pairs: ∂ = 4, so 4/(2·2) = 1.

Hence φ = ½.

Take f = (1,1,0,0). Then g(1) = ½+¼(1+0) = 0.75, g(2) = ½+¼(1+0) = 0.75, g(3) = 0+¼(1+0) = 0.25, g(4) = 0.25.

Top-k sums, with f{k} for k = 1..4 equal to 1, 2, 2, 2 and g{k} equal to 0.75, 1.5, 1.75, 2.

Check k = 2: h = 2, φh = 1, and the bound is ½(f{1}+f{3}) = ½(1+2) = 1.5. Since g{2} = 1.5, the bound is tight here.

Check k = 1: h = 1, φh = 0.5. f{0.5} = 0.5 and f{1.5} = 1+0.5·1 = 1.5, so the bound is 1 ≥ g{1} = 0.75.

Check k = 3: h = 1, f{2.5} = 2 and f{3.5} = 2, so the bound is 2 ≥ g{3} = 1.75.

## Concepts
- [[top-k-sum-curve]] (new) — f{x}: sum of the k largest entries, piecewise linear, concave (p. 142)
- [[conductance]] (new) — φ(S) = |∂(S)| / (d·min(|S|, n−|S|)) on a d-regular graph (p. 144)
- [[lazy-random-walk]] (new) — walk that stays put with probability ½; here γ(a) ≥ ½ on S (pp. 143, 145)
- [[markov-stochastic-matrix]] — W, the walk's transition matrix, acting as g = Wf (p. 142)
- [[eigenvector-eigenvalue]] — ψ with Wψ = (1−λ)ψ, orthogonal to constants (p. 146)
- [[cheeger-inequality]] (new) — for the lazy walk on a d-regular graph with second-largest eigenvalue 1−λ, some set S has φ(S) ≤ √(8λ), in this variant (p. 146)

## Canonical instances
- [[lazy-walk-on-regular-graph]] — the setting assumed throughout the lecture (p. 143)
- [[andersen-cheeger-proof]] — the theorem applied to the second eigenvector (p. 146)

## Bridges (candidates)
- [structural-analogy] top-k-sum curve f{x} and chords ↔ probability: cumulative "mass in the top x states" curve of a distribution, compared to the uniform line — concave curves ordered by chords measure how far from uniform.
- [structural-analogy] φ(S) ≤ √(8λ) ↔ linear-algebra: Cheeger-type relation between the spectral gap and a graph cut (Fiedler-vector partitioning) — an eigenvector yields a good cut.

## Questions this raises
- How do repeated applications of the theorem bound the number of steps t until p_t{x} is close to the line from (0,0) to (n,1)? The source only says the theorem "tells us how quickly" (p. 143).
- How does the irregular, weighted extension mentioned on p. 143 change the definitions of f{k}, W and φ?
- Does the Lemma 16.3.1 argument need S to maximise f, or does it hold for any size-k set (see Reading notes)?
- Where does the Taylor-series bound 1 − φ²/8 come from, and is the constant 8 tight?

## Reading notes
- Printed page = pdf page − 24. The unit is a rough draft: the page says "This Chapter Needs Editing" and "These notes are still very rough" (p. 142). Title as printed: "Lovàsz" (with a grave accent on the à).
- **Claim 16.2.1** says "convex" (p. 143). The inequality as written fails for convex functions (e.g. h(x)=x², x=0: z² ≤ y² is false for z>y). It holds for concave h, matching the text "wider chords lie beneath narrower ones" and the concave f{x}.
- Below Claim 16.2.2 the text says "setting x to 1"; presumably α_i is meant (p. 143).
- p. 145: the line after "By Claim 16.2.2" shows f{k−z}+f{k+z}. With the sums k∓2z just derived, it should be f{k−2z}+f{k+2z}. Then z ≥ φh/2 gives 2z ≥ φh, as needed.
- p. 146: the displayed inequalities "(1−λ) ≤ ½(√(1−φ) + γ√(1+φ))" and "≤ 1 − φ²/8" contain a stray γ. Dividing the previous line by γ√k leaves no γ.
- The proof of Lemma 16.3.1 (and the closing sentence of 16.4) takes S maximising f(S), whereas g{k} is the maximum of g(S′) over sets of size k. The argument works for any set of size k, so it covers the maximiser of g. The source does not say this.
- Section 16.5 uses "γ" both for γ(a,S) earlier and for the maximum value; it also uses φ for φ(S).
- The source gives no steps for the Taylor-series bound. For the step "at most γ√(k±φk)" it says only "By the construction of k and γ", with no detail on non-integer points or on min(k, n−k).
- The source states no exercises.
