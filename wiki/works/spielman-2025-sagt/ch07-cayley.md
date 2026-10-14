---
id: spielman-2025-sagt/ch07-cayley
work: spielman-2025-sagt
unit: Chapter 7 — Cayley Graphs
pages: 61-68
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
# Cayley Graphs

## L0 — One line
In a Cayley graph over an Abelian group the eigenvectors depend only on the group, which makes the eigenvalues much easier to compute; Paley graphs and (with high probability) random generalized hypercubes then have eigenvalues close enough together to approximate the complete graph.

## L1 — The gist (≤ 120 words)
Which graphs built from a group have eigenvalues we can compute and control? A Cayley graph has the group's elements as vertices and joins a to a∘s for generators s. For Paley graphs, the Laplacian satisfies a quadratic matrix identity, so its nonzero eigenvalues lie in {(p ± √p)/2}. For generalized hypercubes, the characters ψ_b are eigenvectors. With about cd random generators, a Chernoff bound shows that, with high probability, all nonzero eigenvalues are within k√(2/c) of k (the author says it works for c = 10). This gives sparse approximations of complete graphs. Constant-degree expanders cannot come from Abelian Cayley graphs (left to homework). For Z/n the eigenvectors are sines and cosines.

**Prerequisites:** graph Laplacian and adjacency matrix; eigenvectors; modular arithmetic; basic probability (independence, union bound).

## L2 — Key ideas
- A Cayley graph has group elements as vertices and edges a — a∘s for s in the generator set S. S must be closed under inverses so the graph is undirected (p. 61).
- Over Abelian groups the eigenvectors depend only on the group, not on S. The eigenvalues depend on S, and so do the eigenspaces when two characters share an eigenvalue (p. 61, p. 68).
- Paley graph on Z/p (p ≡ 1 mod 4): L² = pL + ((p−1)/4)J − (p(p−1)/4)I. Hence the nonzero Laplacian eigenvalues lie in {(p ± √p)/2} (p. 63–64).
- Generalized hypercube: ψ_b(x) = (−1)^{bᵀx} is an eigenvector with eigenvalue k − Σᵢ(−1)^{bᵀgᵢ} (p. 65).
- Random generators, k = cd: with high probability all nonzero eigenvalues are within k√(2/c) of k. The proof uses a Chernoff bound and a union bound (p. 66).
- After rescaling, with high probability this is essentially a (1+√(2/c))-approximation of the complete graph with degree c·log₂n. The author says a homework shows constant-degree expanders cannot be Cayley graphs of Abelian groups, and that explicit constructions need non-Abelian groups (p. 67).
- On Z/n, x_k = sin(2πku/n) has eigenvalue Σ_{g∈S}cos(2πkg/n), for any S (p. 68).

## L3 — Walkthrough

### 7.1 Cayley graphs
Vertices are elements of a group Γ. Generators S ⊂ Γ must satisfy s ∈ S ⇒ s⁻¹ ∈ S. Vertices a, b are adjacent if a∘s = b for some s ∈ S (p. 61).
- Ring: group Z/n, S = {1, −1}. Hypercube H_d: group (Z/2)^d, S = vectors with exactly one 1. Every element is its own inverse (p. 61).
- Closure under inverse makes the graph undirected: a+s=b ⇔ b+(−s)=a (p. 61).
- Footnote: the characters always form an orthonormal set of eigenvectors. If two characters share an eigenvalue, the eigenspace has dimension > 1, and such eigenspaces do depend on S (p. 61).

### 7.2 Paley graphs
Group Z/p, p prime, p ≡ 1 mod 4. Generators S = squares mod p (quadratic residues). Edge u—v iff u−v is a square (p. 62).
- **Fact 7.2.1:** there is g such that every x ∈ {1,…,p−1} equals gⁱ mod p for a unique i ∈ {1,…,p−1}. So g^{p−1} ≡ 1 and x ↔ i is a bijection (p. 62).
- **Corollary 7.2.2:** if p ≡ 1 mod 4, then −1 is a square. Proof: let gⁱ ≡ −1. Then g^{2i} ≡ 1, so 2i ≡ p−1, giving i = (p−1)/2. Since 4 | p−1, s = g^{(p−1)/4} is an integer power, and s² ≡ g^{(p−1)/2} ≡ −1 (p. 62).
- Squares are exactly the gⁱ with i even. Since gⁱgʲ = g^{i+j} and −1 is a square, s is a square iff −s is. So S = −S and the graph is undirected, regular of degree d = (p−1)/2 (p. 62).

*Intuition note:* "Square" means "even power of a generator", and −1 is a square when p ≡ 1 mod 4 (Corollary 7.2.2). That is why s is a square iff −s is, so the graph is undirected, for those primes.

### 7.3 Eigenvalues of Paley graphs
Claim:
$$L^2 = pL + \frac{p-1}{4}J - \frac{p(p-1)}{4}I \tag{7.1}$$
Define the quadratic character χ(x) = 1 if x is a nonzero square, 0 if x = 0, −1 otherwise. It satisfies χ(xy)=χ(x)χ(y). Define X(a,b) = χ(a−b) (p. 63).
- L(a,b) = (p−1)/2 if a=b; −1 if χ(a−b)=1; 0 otherwise. Hence
$$2L = pI - J - X \tag{7.2}$$
- Each row and column of X has (p−1)/2 entries 1, (p−1)/2 entries −1 and one 0. So XJ = JX = 0, and J² = pJ (p. 63).
- **Lemma 7.3.1:** X² = pI − J.
  - Diagonal: the squared column norm is p−1 (p. 63).
  - Off-diagonal: X is symmetric, so entry (a,b) is
$$\sum_{x=0}^{p-1}\chi(a-x)\chi(b-x)=\sum_{y=0}^{p-1}\chi(y)\chi(w+y),\quad y=a-x,\ w=b-a\neq 0.$$
  - The y=0 term is 0. For y≠0, χ(y)χ(w+y) = χ(w+y)/χ(y) = χ(w/y+1), because χ(y) = ±1 (p. 64).
  - As y runs over 1,…,p−1, so does w/y, so w/y+1 runs over all elements except 1. The sum is (Σ_z χ(z)) − χ(1) = 0 − 1 = −1 (p. 64).
- (7.1) follows from (7.2), Lemma 7.3.1, J² = pJ and XJ = JX = 0. (added step) Squaring (7.2): 4L² = (pI−J−X)² = p²I + pJ − 2pJ − 2pX + X² + (JX+XJ) = (p²+p)I − (p+1)J − 2pX. Substituting X = pI − J − 2L gives 4L² = (p−p²)I + (p−1)J + 4pL. Dividing by 4 gives (7.1).
- **Corollary 7.3.2:** nonzero Laplacian eigenvalues lie in {(p ± √p)/2}. Proof: let Lφ=λφ, λ≠0. Then φ ⟂ all-ones, so Jφ=0. By (7.1), λ²φ = (pλ − p(p−1)/4)φ, so λ² − pλ + p(p−1)/4 = 0 (p. 64). (added step) The discriminant is p² − p(p−1) = p, giving λ = (p ± √p)/2.
- Author's remarks: two nonzero eigenvalues means Paley graphs are strongly regular (Chapter 9). Twice a Paley graph is a (1+√(1/p))-approximation of the complete graph, up to a very small factor. Chung–Graham–Wilson showed they share many properties with random graphs (p. 64).

*Intuition note:* A matrix identity of degree 2 forces every nonzero eigenvalue to solve a quadratic. So at most two values are possible.

### 7.4 Generalizing hypercubes
Same group {0,1}^d, generators g₁,…,g_k (automatically closed under negation, since g+g=0). Edges: (x, x+gⱼ). For b ∈ {0,1}^d define ψ_b(x) = (−1)^{bᵀx}. The exponent may be computed over the reals or mod 2, with the same result. b should be seen as indexing a Fourier coefficient, not as a vertex (p. 65). The eigenvectors of $H_d$ were derived earlier via products of graphs (Theorem 5.3.2); here they are verified for all generalized hypercubes (p. 65).
- **Lemma 7.4.1:** ψ_b is a Laplacian eigenvector with eigenvalue k − Σᵢ(−1)^{bᵀgᵢ}. Proof: ψ_b(x+y) = ψ_b(x)ψ_b(y) (7.3). So
$$(L\psi_b)(x)=k\psi_b(x)-\sum_{i=1}^k\psi_b(x+g_i)=k\psi_b(x)-\sum_i\psi_b(x)\psi_b(g_i)=\psi_b(x)\Big(k-\sum_i\psi_b(g_i)\Big).$$
(p. 65). The graph is k-regular, so adjacency and Laplacian share eigenvectors (p. 65).

### 7.5 A random set of generators
Set k = cd, c > 1 (Alon–Roichman construction). For b ≠ 0 and g uniform in {0,1}^d, (−1)^{bᵀg} is uniform on ±1. With independent uniform gᵢ, λ_b = k − Σᵢ(−1)^{bᵀgᵢ} is k minus a sum of independent ±1 variables, so it concentrates near k (p. 66).
- **Theorem 7.5.1 (Chernoff):** for independent ±1 variables xᵢ and t>0, Pr[|Σxᵢ| ≥ t] ≤ 2e^{−t²/2k} (p. 66).
- **Theorem 7.5.2:** with high probability all nonzero eigenvalues differ from k by at most k√(2/c). Proof: take t = k√(2/c). Then t²/2k = k/c = d, so for each b ≠ 0, Pr[|k−λ_b| ≥ t] ≤ 2e^{−d}. Union bound over the 2^d − 1 nonzero b: Pr[∃b: |k−λ_b| ≥ t] ≤ (2^d−1)·2e^{−d}. The author says this is always < 1 and goes to 0 exponentially fast as d grows (p. 66).
- The bound works for c = 10. For c = 2 the analysis must be sharpened. A naive sharpening works down to c = 2 ln 2. Below that a stronger Chernoff bound is needed (p. 67).

*Intuition note:* Each nonzero b gives one "bad event". Each is very unlikely, and there are only 2^d of them, so with high probability none occurs.

### 7.6 Conclusion
Probably all nonzero Laplacian eigenvalues lie in [k(1−√(2/c)), k(1+√(2/c))]. Multiplying edge weights by n/k puts them in [n(1−√(2/c)), n(1+√(2/c))]. So the graph is essentially a (1+√(2/c))-approximation of the complete graph on n vertices, with degree only c·log₂n (p. 67).
- Expanders: infinite families of constant-degree graphs that are constant-factor approximations of complete graphs. Random regular graphs are probably expanders. The author says that if we want explicit constructions we need to go to non-Abelian groups. Error-correcting codes give explicit constructions approaching random generalized hypercubes. Chapter 31 uses such graphs for pseudo-random generators (p. 67).

### 7.7 Non-Abelian groups
The author says a homework shows constant-degree expanders cannot come from Abelian Cayley graphs (not proved here). The best expanders are constructed from Cayley graphs of 2-by-2 matrix groups; in particular the Ramanujan expanders are Cayley graphs over PSL(2,p), p prime: 2×2 matrices mod p with determinant 1, with A identified with −A (Margulis; Lubotzky–Phillips–Sarnak). Generators (it is known that there are p+1 such solutions) come from the solutions of a₁²+a₂²+a₃²+a₄²=p (a₁ odd, others even), as matrices (1/√p)[[a₀+ia₁, a₂+ia₃],[−a₂+ia₃, a₀−ia₁]], with i² ≡ −1 mod p (p. 67–68).

### 7.8 Eigenvectors for Abelian groups
For Z/n with generators S (generalized rings), eigenvectors depend only on the group. For the ring, x_k(u)=sin(2πku/n), y_k(u)=cos(2πku/n), 1 ≤ k ≤ n/2 (p. 68). Adjacency computation for x_k:
$$(Ax_k)(u)=\sum_{g\in S}x_k(u+g)=\tfrac12\sum_{g\in S}\big(x_k(u+g)+x_k(u-g)\big)=\tfrac12\sum_{g\in S}2\sin(2\pi ku/n)\cos(2\pi kg/n)=x_k(u)\sum_{g\in S}\cos(2\pi kg/n).$$
(added step) The second equality uses S = −S. The third uses sin(a+b)+sin(a−b)=2 sin a cos b. The eigenvalue is Σ_{g∈S}cos(2πkg/n) (p. 68). The y_k are "similar" (p. 68). Related results hold for arbitrary groups via representations (p. 68).

## Toy example (ours)
p = 5 ≡ 1 mod 4. Squares mod 5: 1²=1, 2²=4, 3²=9≡4, 4²=16≡1. So S={1,4}={1,−1}, the 5-cycle, with degree 2=(5−1)/2.
- By 7.8, Laplacian eigenvalue = 2 − 2cos(2πk/5) for k=1,2. cos72° = (√5−1)/4 ≈ 0.309, cos144° = −(√5+1)/4 ≈ −0.809. So λ = 2−0.618 = 1.382 and λ = 2+1.618 = 3.618.
- Corollary 7.3.2: (5±√5)/2 = (5±2.236)/2 = 1.382, 3.618. ✓.
- Check the quadratic: λ²−5λ+5=0. For 1.382: 1.910 − 6.910 + 5 = 0 ✓.

## Concepts
- [[cayley-graph]] (new) — vertices are group elements; a~a∘s for s in an inverse-closed S (p. 61)
- [[paley-graph]] (new) — Cayley graph on Z/p, p≡1 mod 4, generators = nonzero squares (p. 62)
- [[quadratic-character]] (new) — χ(x)=1, 0, −1 for nonzero square, zero, non-square; multiplicative (p. 63)
- [[generalized-hypercube]] (new) — Cayley graph on (Z/2)^d with k generators (p. 64)
- [[chernoff-bound]] (new) — tail bound 2e^{−t²/2k} for sums of ±1 variables (p. 66)
- [[expander]] (new) — infinite constant-degree family approximating complete graphs by a constant factor (p. 67)
- [[graph-laplacian]] — L=D−A; here L² is expanded in {L,J,I} (p. 63)
- [[eigenvector-eigenvalue]] — characters ψ_b, x_k are eigenvectors for all generator sets (p. 65, p. 68)
- [[adjacency-matrix]] — used in 7.8; Laplacian shares eigenvectors since graphs are regular (p. 68)

## Canonical instances
- [[ring-graph]] — Cayley graph on Z/n with S={±1} (p. 61)
- [[hypercube]] — Cayley graph on (Z/2)^d with unit-vector generators (p. 61)
- [[paley-graph-spectrum]] — nonzero eigenvalues (p±√p)/2 (p. 64)
- [[ramanujan-expanders-psl2p]] — Cayley graphs on PSL(2,p) (p. 67)

## Bridges (candidates)
- [same-math] ψ_b(x)=(−1)^{bᵀx} eigenvectors ↔ Fourier analysis on (Z/2)^d: the author calls b a Fourier coefficient index.
- [same-math] sin/cos eigenvectors of Z/n ↔ discrete Fourier transform: circulant structure.
- [structural-analogy] Paley character sums ↔ pseudo-randomness: the graph shares properties with random graphs (p. 64).
- [structural-analogy] Chernoff + union bound ↔ concentration arguments in random-matrix and randomized-algorithm proofs.

## Questions this raises
- Why can no Abelian Cayley graph family be a constant-degree expander (the homework claim)?
- Do both eigenvalues (p±√p)/2 actually occur, and with what multiplicities?
- Which sharper Chernoff bound gives the result for c < 2 ln 2?
- How do representations of non-Abelian groups replace characters in giving eigenvectors?

## Reading notes
- Printed = pdf − 24.
- p. 62: Corollary 7.2.2 proof writes "2i ≡ p−1 modulo p". The argument needs modulo p−1 (g has order p−1). This is our reading.
- p. 63: the proof of Lemma 7.3.1 writes "X(a,b)=Σ…" for the off-diagonal entry; it presumably means the entry of X² (our reading).
- p. 67: "prime q congruent to 1 modulo 4" but the text then uses p. The equation uses a₁…a₄ while the matrix uses a₀…a₃. The text is inconsistent; not resolved here.
- Source says "Laplacians matrix" (p. 63) and "Abeliean" (p. 61); typos.
