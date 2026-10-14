---
id: spielman-2025-sagt/ch28-brief
work: spielman-2025-sagt
unit: "Chapter 28 — A brief introduction to Coding Theory"
pages: 228–235
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# A brief introduction to Coding Theory

## L0 — One line
A linear error-correcting code is a subspace of $\mathbb F_2^n$, and a randomly chosen generator matrix gives, with high probability, a code with good rate and minimum distance (when $H(\delta)<1-r$, see 28.6).

## L1 — The gist (≤ 120 words)
How can $m$ message bits be sent as $n>m$ bits so that flipped bits can be corrected? The chapter treats codes in the worst-case, combinatorial way. Hamming's $[7,4]$ code corrects one flip using parity checks. A code's rate $m/n$ and minimum distance $d$ (the fewest positions in which two codewords differ) measure its quality, and $d$ larger than twice the number of flips guarantees correction. Random linear codes are, with high probability, asymptotically good (rate and $d/n$ stay bounded below as $n$ grows; Gilbert–Varshamov bound), but this gives no efficient construction. Reed–Solomon codes have large distance but are not asymptotically good. Good codes give high-expansion generalized hypercubes, and the next chapter builds good codes from expanders.

**Prerequisites:** vectors and matrices over $\mathbb F_2$ (arithmetic mod 2); binomial coefficients; the union bound; polynomials; generalized hypercube eigenvalues (Section 7.4, recalled on p. 229); the idea of an expander graph.

## L2 — Key ideas
- Only bit flips are modelled. The naive 3-fold repetition costs 12 bits for 4 message bits (pp. 228–230).
- A parity bit detects one error but cannot locate it. Hamming's code sends 7 bits for 4 and corrects any single flip (p. 230).
- In the Hamming code, if exactly one bit is flipped, the check matrix applied to the received word gives the column of the flipped bit. The columns are the binary numbers of their positions (p. 230).
- Rate $r=m/n$ (higher is more efficient) and minimum distance $d$ (larger is good) are the two measures of code quality used here. Any number of errors below $d/2$ is correctable (p. 231).
- For a linear code, minimum distance equals the minimum weight of a nonzero codeword (p. 232).
- Generalized-hypercube eigenvalues are $d-2|Gb|$. A code with relative distances in $[\delta,1-\delta]$ gives a $1-2\delta$ expander (pp. 229, 232).
- Random linear codes satisfy a union-bound lemma. It yields the Gilbert–Varshamov bound $H(\delta)<1-r$, but no efficient construction (pp. 232–234).
- Reed–Solomon codes have distance at least $p-m$ but are not asymptotically good (pp. 234–235).

## L3 — Walkthrough

**Intro and 28.1 Coding (pp. 228–229).** The chapter is motivated twofold: good codes give high-expansion generalized hypercubes, and the next chapter builds codes from expanders. The author warns that this worst-case view served the early decades of the field, while error correction is "at its heart probabilistic" (p. 228). The model: a message in $\mathbb F_2^m$ is sent as $n>m$ bits, and noise only flips bits (p. 228). Naive scheme: send each bit 3 times; this corrects one flip but is inefficient (p. 229).

**28.2 Notation (p. 229).** Hamming weight: $|x|\stackrel{def}{=}|\{a: x(a)\neq 0\}|$, also written $\|x\|_0$. $\mathbb F_p$ (integers mod prime $p$) is a field: addition, multiplication, additive inverses, and inverses for all nonzero elements (p. 229).

**28.3 Connection with generalized hypercubes (p. 229).** Vertex set $\mathbb F_2^k$, generators $g_1,\dots,g_d\in\mathbb F_2^k$. The adjacency eigenvalue for $b\in\mathbb F_2^k$ is $\mu_b=\sum_{i=1}^d(-1)^{g_i^Tb}$. Let $G$ be the $d\times k$ matrix with rows $g_i^T$. Since $(-1)^x=1-2x$ for $x\in\{0,1\}$,
$$\mu_b=\sum_{i=1}^d(-1)^{g_i^Tb}=d-2|Gb|.$$
$b=0$ gives eigenvalue $d$. The author says: if $|Gb|$ is small for every other $b$, the other eigenvalues are small (p. 229; see Reading notes). The author claims the condition holds when $G$ generates a good code (p. 229).

**28.4 Hamming codes (pp. 229–230).** Parity bit: send $b_{m+1}=\sum_{i=1}^m b_i \bmod 2$ (28.1). This detects one error but cannot locate it, and cannot detect 2 errors (p. 230). The Hamming code sends 4 bits as 7. Message bits are $b_3,b_5,b_6,b_7$ and the parity bits are
$b_4=b_5+b_6+b_7$, $b_2=b_3+b_6+b_7$, $b_1=b_3+b_5+b_7$ (mod 2). Equivalently, a codeword $b$ satisfies
$$\begin{pmatrix}0&0&0&1&1&1&1\\0&1&1&0&0&1&1\\1&0&1&0&1&0&1\end{pmatrix}b=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$
The $3\times 7$ matrix has columns that are the binary representations of the indices (p. 230).
Example: message 1010 means $b_3=1,b_5=0,b_6=1,b_7=0$, giving $b_1=1,b_2=0,b_4=1$ (p. 230).
If the received word $c$ equals $b$ except $c_6=0$, the product is $(1,1,0)^T$, which is column 6. In general, with one flipped bit, the product is the column of that bit. The columns are distinct, so the position is identified (p. 230).

*Intuition note.* Each row of the matrix is one parity test. A flipped bit breaks exactly the tests that include it. The pattern of broken tests spells out the bit's position in binary.

**28.5 Terminology and linear codes (pp. 231–232).** A code is a map $C:\mathbb F_2^m\to\mathbb F_2^n$; its image points are codewords. Rate $r=m/n$. Hamming distance $\mathrm{dist}(c^1,c^2)=|c^1-c^2|$. Minimum distance $d=\min_{c^1\ne c^2\in C}\mathrm{dist}(c^1,c^2)$ (p. 231).

Claim: any $e<d/2$ errors can be corrected. Let $r$ be $c$ with $e<d/2$ flips. For every codeword $c^1\neq c$,
$$d\le \mathrm{dist}(c^1,c)\le \mathrm{dist}(c^1,r)+\mathrm{dist}(r,c)<\mathrm{dist}(c^1,r)+d/2\ \Rightarrow\ d/2<\mathrm{dist}(c^1,r).$$
So $c$ is the closest codeword to $r$ (p. 231).

Minimum relative distance $\delta=d/n$. A sequence of codes with increasing message lengths is *asymptotically good* if there are absolute constants $r,\delta$ with $r(C_i)\ge r$ and $\delta(C_i)\ge\delta$ for all $i$. The author also asks for concise description and efficient encoding and decoding (p. 231).

Linear code: $\{c: Mc=0\}$ for an $(n-m)\times n$ matrix $M$. The chapter instead uses the generator matrix: for $n\times m$ $G$, $C_G=\{Gb: b\in\mathbb F_2^m\}$ (p. 232). The codewords form a vector space, so sums and differences of codewords are codewords. Over $\mathbb F_2$ they coincide, $\mathrm{dist}(c^1,c^2)=|c^1-c^2|=|c^1+c^2|$. So the minimum distance equals the minimum weight of a nonzero codeword (p. 232).

Link to hypercubes (stated without proof): if $C_G$ has minimum relative distance $\delta$ and maximum relative distance $1-\delta$, the generalized hypercube is a $1-2\delta$ expander (p. 232). (added step) From $\mu_b=d-2|Gb|$ and $\delta d\le|Gb|\le(1-\delta)d$ for $b\ne0$, we get $|\mu_b|\le(1-2\delta)d$ (pp. 229, 232). Here $d,k$ of 28.3 correspond to $n,m$.

**28.6 Random linear codes (pp. 232–234).** Shannon proved random codes asymptotically good; Elias suggested random linear codes (p. 232). Take $G$ $n\times m$ with independent uniform $\mathbb F_2$ entries. Then the minimum distance is $\min_{0\ne b}|Gb|$ (p. 232).

**Lemma 28.6.1.** For any $d$, $\Pr[C_G$ has minimum distance at least $d]\ \ge\ 1-\frac{2^m}{2^n}\sum_{i=0}^d\binom ni$ (p. 232).
Proof steps (p. 233): it suffices to bound the probability that some nonzero $b$ has $|Gb|\le d$. For fixed $b\ne0$, each entry of $Gb$ is uniform in $\mathbb F_2$ and the entries are independent, so $Gb$ is uniform in $\mathbb F_2^n$. Thus $\Pr[|Gb|\le d]=2^{-n}\sum_{i=0}^d\binom ni$. By the union bound,
$$\Pr_G[\exists b\ne0:|Gb|\le d]\le\sum_{0\ne b}\Pr[|Gb|\le d]\le(2^m-1)\frac1{2^n}\sum_{i=0}^d\binom ni\le\frac{2^m}{2^n}\sum_{i=0}^d\binom ni.$$

Asymptotics: for $0<p<1$, $\sum_{i=1}^{pn}\binom ni\le 2^{nH(p)}$, with $H(p)=-p\log_2p-(1-p)\log_2(1-p)$ the binary entropy function. The author says the bound is very tight, with a lower bound differing only in low-order terms, and cites [MS77] for a proof (p. 233). Set $m=rn$, $d=\delta n$. Then $C_G$ probably has rate $r$ and minimum relative distance $\delta$ if $\frac{2^{rn}}{2^n}2^{nH(\delta)}<1$, which happens when $H(\delta)<1-r$. For any constant $r<1$ some $\delta$ satisfies this, so asymptotically good sequences exist for every nonzero rate. This is the Gilbert–Varshamov bound (pp. 233–234). Whether binary codes exist with $H(\delta)>1-r$ is stated to be a big open question (p. 234). This argument does not say how to pick such a code, check its distance efficiently, or decode it (p. 234).

*Intuition note.* There are few low-weight words, and a random nonzero message maps to a uniform word. So the chance that some message lands on a low-weight word is small when the rate is low enough that $H(\delta)<1-r$ (p. 233). That shows good codes exist, not how to find them.

**28.7 Reed–Solomon codes (pp. 234–235).** Symbols are elements of a finite field; here only prime fields $\mathbb F_p$ are used, and RS codes are not binary (p. 234). A message $f_1,\dots,f_m$ gives $Q(x)=\sum_{i=0}^{m-1}f_{i+1}x^i$. The codeword is $Q(0),Q(1),\dots,Q(p-1)$, sometimes on a subset of field elements (p. 234).

**Lemma 28.7.1** (a standard fact; no proof given). If $Q$ has degree at most $m-1$ and vanishes at $m$ distinct field elements, then $Q$ is identically zero (p. 234).

**Theorem 28.7.2.** The minimum distance is at least $p-m$ (p. 234). Proof (p. 235): for distinct $Q^1,Q^2$ of degree at most $m-1$, if $\mathrm{dist}(E(Q^1),E(Q^2))\le p-k$, they agree on at least $k$ field elements. Then $Q^1-Q^2$ has degree at most $m-1$ and $k$ zeros. By the lemma, if $k\ge m$ then $Q^1=Q^2$. So for distinct $Q^1,Q^2$, $\mathrm{dist}>p-m$.

Not asymptotically good: with $\log_2p$ bits per field element the length is $p\log_2p$, but at most $p$ errors can be corrected. The author adds that one can find an asymptotically good family by encoding each field element with its own small error-correcting code (p. 235). The next chapter builds good codes from expanders; the following one uses good codes to build graphs (p. 235).

**28.8 Caution (p. 235).** The section contains only a placeholder: "Explain defects of the worst-case view."

## Toy example (ours)
Message bits $b_3=0,b_5=0,b_6=0,b_7=1$. Parity bits: $b_4=0+0+1=1$, $b_2=0+0+1=1$, $b_1=0+0+1=1$. Codeword: $1101001$. Flip bit 3: $c=1111001$. Check rows (positions of 1s: $\{4,5,6,7\}$, $\{2,3,6,7\}$, $\{1,3,5,7\}$):
- row 1: $c_4+c_5+c_6+c_7=1+0+0+1=0$;
- row 2: $c_2+c_3+c_6+c_7=1+1+0+1=1$;
- row 3: $c_1+c_3+c_5+c_7=1+1+0+1=1$.

The result is $(0,1,1)$, binary for 3, so flip bit 3 back.

## Concepts
- [[null-space-kernel]] — a linear code defined by $Mc=0$ is the null space of $M$ over $\mathbb F_2$ (p. 232)
- [[column-space-range]] — $C_G=\{Gb\}$ is the column space of $G$ over $\mathbb F_2$ (p. 232)
- [[hamming-weight]] (new) — $|x|$, the number of nonzero entries, also $\|x\|_0$ (p. 229)
- [[hamming-distance]] (new) — number of positions where two words differ, $|c^1-c^2|$ (p. 231)
- [[minimum-distance]] (new) — smallest distance between distinct codewords; for linear codes, the smallest nonzero weight (pp. 231–232)
- [[code-rate]] (new) — $r=m/n$, message bits per codeword bit (p. 231)
- [[linear-code]] (new) — code whose codewords form a vector space; defined by $M$ or $G$ (p. 232)
- [[asymptotically-good-codes]] (new) — a sequence with rate and relative distance bounded below by constants (p. 231)
- [[gilbert-varshamov-bound]] (new) — random linear codes work when $H(\delta)<1-r$ (p. 233)
- [[binary-entropy]] (new) — $H(p)=-p\log_2p-(1-p)\log_2(1-p)$; bounds binomial sums (p. 233)
- [[reed-solomon-code]] (new) — evaluate a degree-$(m-1)$ polynomial over $\mathbb F_p$ at all points (p. 234)
- [[finite-field]] (new) — a set with $+,\times$, inverses; $\mathbb F_p$ is integers mod prime $p$ (p. 229)

## Canonical instances
- [[hamming-7-4-code]] — corrects one flip using columns as binary indices (p. 230)
- [[repetition-code]] — 3-fold repetition: corrects one flip at rate 1/3 (pp. 229–230)
- [[parity-bit-code]] — detects one error, cannot locate it (p. 230)
- [[random-linear-code]] — good with the stated probability bound (pp. 232–233)
- [[reed-solomon-code]] — distance above $p-m$, not asymptotically good (pp. 234–235)

## Bridges (candidates)
- [same-math] Hamming weight of $Gb$ in $\mu_b=d-2|Gb|$ ↔ spectral graph theory: eigenvalues of generalized hypercubes (p. 229)
- [same-math] linear code as column space or null space ↔ linear algebra: range and kernel, here over $\mathbb F_2$ (p. 232)
- [structural-analogy] union bound over all $2^m-1$ messages ↔ the Chernoff-plus-union-bound argument of Section 7.5 (p. 232)

## Questions this raises
- Which graph properties let expanders give codes with efficient decoding (next chapter, p. 235)?
- Is there a binary code with $H(\delta)>1-r$ (open, p. 234)?
- How does the probabilistic view of noise replace the worst-case view (p. 228)?
- Can the check matrix of a code with larger distance still identify error positions as simply as the Hamming code does?

## Reading notes
- Printed = pdf − 24.
- p. 229 says that small $|Gb|$ for all $b\ne0$ makes the other eigenvalues small. With $\mu_b=d-2|Gb|$ as printed, small $|Gb|$ gives $\mu_b$ near $d$. $\mu_b$ is small only when $|Gb|$ is near $d/2$, which fits the condition on p. 232 (relative distances in $[\delta,1-\delta]$).
- Misprints in the images: in Lemma 28.6.1's proof (p. 233), entries of $Gb$ are called inner products with a column of $G$; for $n\times m$ $G$ they are rows. The displayed chain also has a period after its second line, followed by one more (valid) "≤" step. In Theorem 28.7.2 (p. 234), $E(Q)$ runs to $Q(p)$ rather than $Q(p-1)$, and the proof switches between $k$ and $m$. The proof proves $>p-m$ although the statement says "at least".
- p. 232 says the code is a vector space "over $\mathbb F_2^m$"; $\mathbb F_2$ is meant. p. 229 reads "$\mathbb F_2$, which we write $\mathbb F_2$", presumably a notation glitch.
- The binomial-sum bound starts at $i=1$ (p. 233), while the lemma's sum starts at $i=0$.
- Section 28.8 is an unfinished stub (incomplete draft).
