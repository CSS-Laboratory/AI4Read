---
id: spielman-2025-sagt/ch29-expander
work: spielman-2025-sagt
unit: Chapter 29 — Expander Codes
pages: 236–242
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Expander Codes

## L0 — One line
Put one bit on each edge of a bipartite expander graph and make every vertex see a codeword of a small code: under suitable conditions on $r_0$ and on how well the graph approximates the complete bipartite graph, the result is a code with constant rate and relative distance, and alternating local corrections decode a constant fraction of errors.

## L1 — The gist (≤ 120 words)
How can a small good code $C_0$ of length $d$ be turned into a long good code? Place bits on the edges of a $d$-regular bipartite graph that approximates $\frac dnK_{n,n}$ within error $\epsilon$, and require the $d$ bits at every vertex to form a codeword of $C_0$ (rate $r_0$, minimum distance $\delta_0d$). Then the rate is at least $2r_0-1$. If $\epsilon\le\delta_0/2$, the relative distance is at least $\delta_0^2/2$. If $\epsilon\le\delta_0/3$ and the $C_0$ decoder corrects $\delta_0d/2$ errors, running it alternately on the two sides corrects up to $\delta_0^2dn/18$ errors in at most $\log_{4/3}n$ rounds. The distance and decoding proofs rest on one counting bound for edges between vertex sets.

**Prerequisites:** graph Laplacian eigenvalues and the order $\preceq$; adjacency matrix; linear codes over $\{0,1\}$ (rate, Hamming distance); rank–nullity counting.

## L2 — Key ideas
- A bipartite expander is a $d$-regular bipartite $G$ with $(1-\epsilon)\frac dnK_{n,n}\preceq G\preceq(1+\epsilon)\frac dnK_{n,n}$. It can be obtained as the double cover of an ordinary expander (p. 236).
- Such a graph has few "unexpected" edges between $S\subseteq U$ and $T\subseteq V$ (Thm 29.1.3), so the induced subgraph $G(S\cup T)$ has average degree at most $\frac{2d\sigma\tau}{\sigma+\tau}+\epsilon d$ (p. 237).
- Code: one bit per edge, with each vertex's $d$ bits forced into $C_0$. Counting constraints gives rate $\ge 2r_0-1$, which is positive when $r_0>1/2$ (p. 238).
- Encoding uses a generator matrix computed from the constraint matrix $M$ by elementary linear algebra (p. 239).
- If $\epsilon\le\delta_0/2$, then $\delta\ge\delta_0^2/2$. The proof compares a lower and an upper bound on the average degree of the subgraph carrying a codeword's 1-edges (pp. 239–240).
- Decoding alternates the $C_0$ decoder on $U$ and $V$. It tracks vertices touching errors, not the errors themselves (p. 240).
- If $\epsilon\le\delta_0/3$ and $|S|\le\delta_0n/9$, the set of erroneous vertices shrinks to at most $3/4$ of its size per step (pp. 240–241).
- Encoding is slower than decoding, because the generator matrix is dense (p. 242).

## L3 — Walkthrough

**29.1 Bipartite expander graphs (pp. 236–238).**
Parts $U,V$ each have $n$ vertices, every vertex has degree $d$, and every edge joins $U$ to $V$ (p. 236). The target is $(1-\epsilon)\frac dnK_{n,n}\preceq G\preceq(1+\epsilon)\frac dnK_{n,n}$, where $K_{n,n}$ is the complete bipartite graph (p. 236). The Laplacian eigenvalues of $\frac dnK_{n,n}$ are $0$ and $2d$ (multiplicity 1 each) and $d$ otherwise. So we want
$$\lambda_1=0,\quad \lambda_{2n}=2d,\quad |\lambda_i-d|\le\epsilon d\ \ (1<i<2n).$$

*Definition 29.1.1.* The double-cover of $G=(V,E)$ has vertex set $V\times\{0,1\}$ and edges $((a,0),(b,1))$ for $(a,b)\in E$ (p. 236). Figure 29.1 shows the 4-cycle and its double cover (p. 237).

*Proposition 29.1.2.* If $H$ is the double cover of $G$, then for each Laplacian eigenvalue $\lambda_i$ of $G$, $H$ has the pair $\lambda_i$ and $2d-\lambda_i$ (p. 237). The text gives only the hint that $H$ has adjacency matrix $\begin{pmatrix}\mathbf 0&A\\A&\mathbf 0\end{pmatrix}$ (p. 237).
(added step, assuming $G$ is $d$-regular, so $L=dI-A$: this block matrix has eigenvalues $\pm\mu$ for each eigenvalue $\mu$ of $A$. The Laplacian eigenvalues of $H$ are then $d\mp\mu$. With $\lambda=d-\mu$, the pair is $\lambda$ and $2d-\lambda$.)

*Intuition note.* Taking the double cover of a good ordinary expander makes the eigenvalues symmetric around $d$. That gives the spectrum we want (when the ordinary expander has $|\lambda_i-d|\le\epsilon d$ for $i>1$), including $0$ and $2d$.

*Theorem 29.1.3.* If $G=(U\cup V,E)$ is $d$-regular bipartite and $\epsilon$-approximates $\frac dnK_{n,n}$, then for all $S\subseteq U$, $T\subseteq V$,
$$\Big|\,|E(S,T)|-\tfrac dn|S||T|\,\Big|\le\epsilon d\sqrt{|S||T|}.$$
The proof is given only as "Similar to the proof of Theorem 27.3.1". The theorem is called analogous to Theorem 10.2.1 (p. 237).

*Corollary 29.1.4.* Let $|S|=\sigma n$ and $|T|=\tau n$. Then the average degree of $G(S\cup T)$ is at most $\frac{2d\sigma\tau}{\sigma+\tau}+\epsilon d$.
Proof: average degree = $2\times$edges / vertices, which is at most
$$\frac{2d}{n}\frac{|S||T|}{|S|+|T|}+2\epsilon d\frac{\sqrt{|S||T|}}{|S|+|T|}.$$
The first term equals $\frac{2d\sigma\tau}{\sigma+\tau}$. The second is at most $\epsilon d$ (pp. 237–238). (added step: $\sqrt{ab}\le (a+b)/2$.)

**29.2 Building codes (p. 238).**
Ingredients: a $d$-regular bipartite expander $G$ on $2n$ vertices, and a linear code $C_0$ of length $d$. Keep $d$ constant while $n$ grows. One bit sits on each of the $dn$ edges. Each vertex lists its edges in a fixed order and requires its $d$ bits to be a codeword of $C_0$.

$C_0$ has rate $r_0$, meaning its codewords form a space of dimension $r_0d$. Since $C_0$ is linear, its codewords are exactly the solutions of $d(1-r_0)$ linear equations. Over $2n$ vertices this gives $2nd(1-r_0)$ constraints. So the codeword space has dimension at least
$$dn-2dn(1-r_0)=dn(2r_0-1),$$
and the rate is at least $r=2r_0-1$. This is a nonzero constant if $r_0>1/2$. $C$ denotes the resulting code.

**29.3 Encoding (pp. 238–239).**
The constraints form a matrix $M$ with $dn$ columns and $2dn(1-r_0)$ rows, and the codewords are exactly the $y$ with $My=0$. There is a generator matrix $G$ ($dn$ rows, $dn(2r_0-1)$ columns) such that the codewords are precisely $Gx$ for $x\in\{0,1\}^{dn(2r_0-1)}$. Many such $G$ exist, and one can be computed from $M$ by elementary linear algebra.

**29.4 Minimum distance (pp. 239–240).**
Let $\delta_0d$ be the minimum distance of $C_0$.

*Theorem 29.4.1.* If $\epsilon\le\delta_0/2$, the minimum relative distance of $C$ satisfies $\delta\ge\delta_0^2/2$.

Proof. By linearity it suffices to bound the weight of nonzero codewords. Let $F$ be the set of edges carrying 1s, with $|F|=\phi dn$.
1. Every vertex touched by $F$ touches at least $\delta_0d$ edges of $F$. Let $S\subseteq U$ and $T\subseteq V$ be the touched vertices. Then every vertex of $G(S\cup T)$ has degree at least $\delta_0d$, so the average degree is at least $\delta_0d$.
2. Hence $|S|,|T|\le |F|/(\delta_0d)$, i.e. $\sigma,\tau\le\phi/\delta_0$.
3. Corollary 29.1.4 gives average degree at most $\frac{2d\sigma\tau}{\sigma+\tau}+\epsilon d$. Since $2\sigma\tau\le\sigma^2+\tau^2\le\frac{\phi}{\delta_0}(\sigma+\tau)$, this is at most $d\frac{\phi}{\delta_0}+\epsilon d$.
4. Combining: $\delta_0d\le d\frac\phi{\delta_0}+\epsilon d$, so $\delta_0(\delta_0-\epsilon)\le\phi$. With $\epsilon\le\delta_0/2$: $\phi\ge\delta_0^2/2$. ∎

*Intuition note.* Corollary 29.1.4 bounds the average degree of a small induced subgraph. So when $\epsilon\le\delta_0/2$, a small set of 1-edges cannot give every touched vertex degree at least $\delta_0d$. Nonzero codewords therefore need many 1s.

**29.5 Decoding (pp. 240–241).**
Assume an algorithm $A$ that, for any $r\in\{0,1\}^d$, outputs $c\in C_0$ whenever $\mathrm{dist}(c,r)\le\delta_0d/2$. Apply $A$ at every vertex of $U$, then every vertex of $V$, and alternate for a logarithmic number of iterations ($U$- and $V$-decoding steps). Claim: if $\epsilon\le\delta_0/3$, this corrects up to $\delta_0^2dn/18$ errors in at most $\log_{4/3}n$ iterations. The idea is to track vertices attached to erroneous edges; a vertex with few erroneous edges corrects them.

*Lemma 29.5.1.* Let $\epsilon\le\delta_0/3$ and $F\subset E$. Let $S\subseteq U$ be the vertices attached to $F$. Let $T\subseteq V$ be the vertices attached to at least $\delta_0d/2$ edges of $F$. If $|S|\le\delta_0n/9$, then $|T|\le\frac34|S|$.
Proof:
1. $|F|\ge(\delta_0d/2)|T|$. So the average degree of $G(S\cup T)$ is at least $\frac{\delta_0d|T|}{|S|+|T|}=\frac{\delta_0d\tau}{\sigma+\tau}$.
2. By Corollary 29.1.4, $\frac{\delta_0d\tau}{\sigma+\tau}\le\frac{2d\sigma\tau}{\sigma+\tau}+\epsilon d$. This gives $\delta_0\tau\le2\sigma\tau+\epsilon(\sigma+\tau)$, i.e. $\tau\le\frac{\epsilon\sigma}{\delta_0-2\sigma-\epsilon}$.
3. With $\sigma\le\delta_0/9$ and $\epsilon\le\delta_0/3$: $\tau\le\sigma\frac{\delta_0/3}{\delta_0(4/9)}\le\frac34\sigma$. ∎

*Lemma 29.5.2.* Let $F$ be the erroneous edges after a $U$-decoding step and $S\subseteq U$ the vertices attached to $F$. After the next $V$-decoding step, let $T$ be the vertices of $V$ attached to erroneous edges. If $|S|\le\delta_0n/9$, then $|T|\le\frac34|S|$.
Proof: a vertex of $V$ that still outputs an error must be attached to at least $\delta_0d/2$ edges of $F$, and these edges end in $S$. Apply Lemma 29.5.1. ∎

*Theorem 29.5.3.* If $\epsilon\le\delta_0/3$, the algorithm corrects every set of at most $\frac{\delta_0^2}{18}dn$ errors.
Proof: let $F$ be the initial errors and $S$ the vertices that output errors after the first $U$-step. Each vertex of $S$ is adjacent to at least $\delta_0d/2$ edges of $F$. So $|F|\le\frac{\delta_0^2}{18}dn\Rightarrow|S|\le\frac{|F|}{\delta_0d/2}\le\delta_0n/9$. Lemma 29.5.2 then gives convergence in at most $\log_{4/3}n$ iterations (p. 241). (added step: $|S|\le n$ and each step multiplies the size by at most $3/4$, so $(3/4)^kn<1$ once $k>\log_{4/3}n$.)

*Intuition note.* Once the set of vertices touching errors is below a threshold, each step shrinks it to at most $3/4$ of its size, so the decoding process converges in at most $\log_{4/3}n$ iterations.

**29.6 Historical notes (pp. 241–242).**
Gallager first used graphs for codes, with bits on one side and constraints on the other. Tanner was "the first to put the vertices on the edges" (the text's wording; the construction here puts bits on edges). Sipser and Spielman pioneered using expansion; this construction is due to Zemor, who gives a tighter analysis. Encoding costs $\Theta((dn)^2)$ because $G$ is dense. Lafferty–Rockmore (Ramanujan expanders, FFT) reduce it to $O(d^2n^{4/3})$. Spielman modifies the code to allow linear-time encoding. Related ideas give codes approaching channel capacity.

## Toy example (ours)
Take $G=K_{4,4}$ ($n=4$, $d=4$, so 16 edges). It is the perfect case $\epsilon=0$. Let $C_0$ be the even-weight code of length 4: one equation, so $r_0=3/4$, and minimum distance 2, so $\delta_0=1/2$.
- Bits form a $4\times4$ 0/1 matrix. Each row (a vertex of $U$) and each column (a vertex of $V$) must have even weight.
- Constraints: $2n\cdot d(1-r_0)=8\cdot1=8$. The bound is dimension $\ge16-8=8=dn(2r_0-1)$, so rate $\ge1/2$.
- Actual dimension: the sum of the row parities equals the sum of the column parities, so only 7 constraints are independent. Dimension is $16-7=9$ (a free $3\times3$ block fixes the rest). This is above the bound of 8.
- Distance: a nonzero codeword has weight at least 4 (a $2\times2$ rectangle of 1s). So $\delta=4/16=1/4\ge\delta_0^2/2=1/8$. ✓

## Concepts
- [[adjacency-matrix]] — here $A$ of $G$; the double cover has $\begin{pmatrix}0&A\\A&0\end{pmatrix}$ (p. 237)
- [[graph-laplacian]] — its spectrum defines "$\epsilon$-approximates $\frac dnK_{n,n}$" (p. 236)
- [[spectral-approximation]] (new) — $(1-\epsilon)H\preceq G\preceq(1+\epsilon)H$ for Laplacians (p. 236)
- [[bipartite-double-cover]] (new) — $V\times\{0,1\}$ with edges $((a,0),(b,1))$; eigenvalues $\lambda,2d-\lambda$ (pp. 236–237)
- [[expander-mixing-bound]] (new) — $\big|\,|E(S,T)|-\frac dn|S||T|\,\big|\le\epsilon d\sqrt{|S||T|}$ (p. 237)
- [[linear-code]] (new) — codewords are solutions of linear equations; rate = dimension/length (p. 238)
- [[null-space]] — codewords are $\{y: My=0\}$ (p. 238)
- [[column-space]] — codewords are $\{Gx\}$, with $G$ a generator matrix (p. 239)
- [[rank-nullity]] — constraint counting gives dimension $\ge dn-\#\text{constraints}$ (p. 238)
- [[expander-code]] (new) — bits on edges of a bipartite expander, vertex constraints from $C_0$ (p. 238)

## Canonical instances
- [[four-cycle-double-cover]] — the 4-cycle and its double cover (Figure 29.1) (p. 237)
- [[expander-code-construction]] — rate $\ge2r_0-1$, $\delta\ge\delta_0^2/2$, decoding of $\delta_0^2dn/18$ errors (pp. 238–241)

## Bridges (candidates)
- [structural-analogy] Theorem 29.1.3 ↔ Theorem 10.2.1 (the text calls Thm 29.1.3 analogous to it): edge counts between sets are near their random-graph values.
- [same-math] Counting dimension of $\{y:My=0\}$ ≥ unknowns − constraints ↔ rank–nullity (over $\mathbb F_2$ here).
- [structural-analogy] Shrinking the error set by a constant factor per round ↔ geometric convergence of iterative methods.

## Questions this raises
- Theorem 29.1.3's proof is only cited. How does the proof of Theorem 27.3.1 adapt to the bipartite case?
- What is Zemor's tighter analysis, and how much better are its constants?
- Can encoding be made as fast as decoding while keeping the code this simple (see the linear-time modification cited on p. 242)?
- Does a $C_0$ with $r_0>1/2$ and good $\delta_0$ exist for the chosen constant $d$? (The unit assumes one.)

## Reading notes
- Printed page = pdf page − 24.
- p. 239, §29.3: the text says the codewords "form a vector space of dimension $dn(2r_0-1)$". §29.2 only established "at least" this dimension. (Our observation, not the text's: in the toy example the constraints are dependent and the dimension is 9, above the bound 8.)
- p. 241: the proof of Theorem 29.5.3 writes "$\delta d/2$" where $\delta_0d/2$ is apparently meant.
- Proposition 29.1.2 does not say $G$ is $d$-regular, but the statement uses $2d$.
- The letter $G$ is used both for the graph and for the generator matrix.
- The text layer dropped some $\epsilon$ symbols; I checked the images.
- No exercises in this unit.
