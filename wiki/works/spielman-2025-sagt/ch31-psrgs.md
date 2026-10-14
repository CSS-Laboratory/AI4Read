---
id: spielman-2025-sagt/ch31-psrgs
work: spielman-2025-sagt
unit: "Chapter 31 — PSRGs via Random Walks on Graphs"
pages: 251–256
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# PSRGs via Random Walks on Graphs

## L0 — One line
A random walk on an expander graph can feed a randomized algorithm correlated inputs that need only about 9 fresh random bits per run, and the majority-vote error still falls exponentially, proved by a 2-norm bound on $D_X W$.

## L1 — The gist (≤ 120 words)
Question: if a randomized algorithm (a "black box") is right at least 99% of the time, can we repeat it and take the majority without fresh random bits for every run? Answer: take one truly random start vertex on a $d$-regular $1/10$-expander (a graph whose walk matrix has all eigenvalues after the top one of absolute value at most $1/10$) with $2^r$ vertices. Then walk, using about 9 new bits per step (here $d=400$). With $t+1$ runs, the probability that the majority is wrong is at most $(2/\sqrt5)^{t+1}$. The proof writes the probability as a product of matrices and bounds the operator norm $\|D_XW\|\le 1/5$. It matters because random bits are scarce. The analysis is deliberately crude.

**Prerequisites:** operator (2-norm) of a matrix; eigenvalues of symmetric matrices; random-walk matrix $W=M/d$; diagonal indicator matrices; Cauchy–Schwarz-style norm inequalities.

## L2 — Key ideas
- Pseudo-random generators (PSRGs) turn a random seed into a long string of bits meant to act random; here they are proved to work for a specific kind of algorithm. Reasons to want them: random bits are scarce, and a fixed seed allows re-running (pp. 251–252).
- Setting: a box on $r$ bits, whose minority answer occurs on a set $X$ with $|X|\le 2^r/100$. The generator is a random walk on a $1/10$-expander with vertex set $\{0,1\}^r$ (pp. 252–253).
- Cost: $r$ truly random bits for the first run, then $\log_2 400\approx 9$ bits per further run (p. 253).
- Target: $\Pr[|S|>t/2]\le(2/\sqrt5)^{t+1}$, where $S$ is the set of times the walk is in $X$ (p. 253).
- The probability of being in $X$ exactly at the times in $R$ is a matrix product, $\mathbf 1^T D_{Z_t}W\cdots D_{Z_0}p_0$ (p. 254).
- Key lemma: $\|D_XW\|\le 1/5$, where the operator norm is the largest stretch factor $\max_v\|Mv\|/\|v\|$. With submultiplicativity ($\|M_1M_2\|\le\|M_1\|\|M_2\|$) this gives probability $\le(1/5)^{|R|}$ (p. 255).
- The lemma proof splits $x=c\mathbf 1+y$. The constant part is shrunk because $X$ is small. The orthogonal part is shrunk by the spectral gap, i.e. the eigenvalues other than the top one have absolute value at most $1/10$ (p. 256).
- The author notes the proof is strange: it uses 2-norms of probability vectors rather than sums of probabilities (p. 256).

## L3 — Walkthrough

**31.1–31.2 Why PSRGs.** Three approaches: quick procedures that seem good enough; cryptographers' and complexity theorists' attempts to design PSRGs that work for every polynomial-time algorithm; and PSRGs proved for specific algorithms. This chapter takes the third, following Impagliazzo–Zuckerman: random walks on expanders to rerun one algorithm. The analysis is "very crude"; tighter ones exist (p. 251). Reasons for PSRGs: (1) random bits are scarce; (2) re-running with the same seed helps debugging (pp. 251–252). The author says default generators such as C's `rand` are usually terrible. Cryptographic-function-based ones can give bits that act random for most purposes unless the cryptography is broken, but are usually much slower than the fastest generators. It is a time-versus-quality tradeoff (p. 252).

**31.3 Expanders needed.** We need an infinite family of $d$-regular $1/10$-expanders. $d$ is constant. We require the graphs to have $2^r$ vertices for all sufficiently large $r$. Neighbours of a vertex are computable in time polynomial in $r$. Ramanujan graphs of degree $d=400$ are $1/10$-expanders. The explicit Ramanujan graphs exist only in certain sizes, none exactly $2^r$, but some have just a little more than $2^r$ vertices; they can be trimmed, say by ignoring steps where the vertex does not correspond to $r$ bits (p. 252).

**31.4 Application.** The box takes $r$ bits and returns 0 or 1. It returns the same answer at least 99% of the time, so it is a "0-box" or a "1-box". We want to decide which, with more than 99% confidence, by taking the majority over many runs. Naively each run needs fresh bits. The claim is that 9 new bits per run suffice (p. 252). The first test uses truly random bits. The error probability decreases exponentially in $t$ (p. 253). The box models a randomized algorithm on a fixed problem (p. 253).

**31.5 The generator.** $X\subset\{0,1\}^r$ is where the box gives the minority answer, and $Y$ is where it gives the majority answer. The first input is a truly random vertex. Each later input is a uniformly random neighbour of the current vertex, chosen by $i\in\{1,\dots,400\}$ (p. 253).

**31.6 Formalizing.** Test $t+1$ times. The walk is $v_0,\dots,v_t$ with $v_0$ uniform. Assume $|X|\le 2^r/100$. The majority is correct if the walk is in $X$ less than half the time. Let $S=\{i: v_i\in X\}$. To prove:
$$\Pr[|S|>t/2]\le\Big(\tfrac{2}{\sqrt5}\Big)^{t+1}.$$
Here $p_0=\mathbf 1/n$ is the uniform start, $D_X=\mathrm{diag}(\chi_X)$, $D_Y=\mathrm{diag}(\chi_Y)$, and
$$W=\tfrac1d M \tag{31.1}$$
is the ordinary (not lazy) walk matrix. Its eigenvalues are $\omega_1,\dots,\omega_n$, and $|\omega_i|\le1/10$ for $i\ge2$ (p. 254).

For a probability vector $p$: $\Pr[\text{in }X]=\chi_X^Tp=\mathbf 1^TD_Xp$. $D_Xp$ zeroes the mass outside $X$. One step is a multiplication by $W$, so $q=WD_Xp_0$. The probability of being in $X$ at exactly the times in $R$ is
$$\mathbf 1^TD_{Z_t}WD_{Z_{t-1}}W\cdots D_{Z_1}WD_{Z_0}p_0,\qquad Z_i=\begin{cases}X& i\in R\\ Y&\text{otherwise.}\end{cases}$$
The author will show this is $\le(1/5)^{|R|}$. Then
$$\Pr[|S|>t/2]\le\sum_{|R|>t/2}(1/5)^{|R|}\le 2^{t+1}(1/5)^{(t+1)/2}=(2/\sqrt5)^{t+1}.$$
(p. 254)

*Intuition note.* Each time the walk lands in the bad set, it costs a factor of at most $1/5$ in probability. Staying bad for more than half the times then beats the number of possible subsets $R$, which is at most $2^{t+1}$.

**31.7 Matrix norms.** The operator norm is $\|M\|=\max_v\|Mv\|/\|v\|$. For symmetric $M$ it is the largest absolute eigenvalue (the author asks the reader to prove it). Also $\|M_1M_2\|\le\|M_1\|\|M_2\|$. $D_X,D_Y,W$ are symmetric, so each has norm 1 (p. 255).

Warning 31.7.1: an asymmetric walk matrix can have norm above 1, though its top eigenvalue is 1. The author says the 3-vertex path has norm $\sqrt2$ (p. 255).

**Lemma 31.7.2.** $\|D_XW\|\le1/5$ (p. 255).

How it implies the bound: since $p_0=Wp_0$,
$$\mathbf 1^TD_{Z_t}WD_{Z_{t-1}}W\cdots D_{Z_0}Wp_0=\mathbf 1^T(D_{Z_t}W)(D_{Z_{t-1}}W)\cdots(D_{Z_0}W)p_0.$$
Each factor has norm $\le1/5$ if its index is in $R$ and $\le1$ otherwise. So the product has norm $\le(1/5)^{|R|}$. With $\|p_0\|=1/\sqrt n$ and $\|\mathbf 1\|=\sqrt n$, the value is at most $\|\mathbf 1^T\|\,(1/5)^{|R|}\|p_0\|=(1/5)^{|R|}$ (p. 255).

**31.8 Proof of the lemma.** Write $x=c\mathbf 1+y$ with $\mathbf 1^Ty=0$. Show $\|D_XWx\|\le\|x\|/5$.
- $W\mathbf 1=\mathbf 1$, so $D_XW\mathbf 1=\chi_X$. Hence $\|D_XWc\mathbf 1\|=c\|\chi_X\|=c\sqrt{|X|}\le c\sqrt n/10$ (pp. 255–256).
- $\|Wy\|\le\|y\|/10$. Reason: $W-J/n$ is symmetric with eigenvalues of absolute value at most $1/10$, so its norm is at most $1/10$. Moreover $(W-J/n)y=Wy$ ($J$ is the all-ones matrix), which gives the bound. The author also mentions another proof: expand $y$ in the eigenbasis of $W$, as in the proof of Lemma 2.1.3 (p. 256).
- Orthogonality gives $\|x\|=\sqrt{c^2n+\|y\|^2}$, so $c\sqrt n\le\|x\|$ and $\|y\|\le\|x\|$ (added step). Then
$$\|D_XWx\|\le\|D_XWc\mathbf 1\|+\|D_XWy\|\le c\sqrt n/10+\|y\|/10\le\|x\|/10+\|x\|/10\le\|x\|/5.$$
The second term uses $\|D_X\|\le1$ (added step) (p. 256).

*Intuition note.* Any vector is a constant part plus a part with sum zero. The constant part lands mostly outside $X$, because $X$ is small. The sum-zero part is shrunk by the spectral gap before $D_X$ acts. Both are cut by $1/10$, giving $1/5$ together.

**31.9–31.10.** The author calls the proof "very strange": when considering probabilities, it seems much more natural to sum them, but here 2-norms of probability vectors are used. Notes point to Gillman for tighter concentration results on expander walks, and to other work for the best bit counts (p. 256).

## Toy example (ours)
Take $n=4$, $W=J/4$ (complete graph with self-loops; eigenvalues $1,0,0,0$, so the gap is even better than $1/10$). Take $X=\{1\}$, so $|X|=n/4$. This is not the chapter's $1/100$ regime, but it shows the mechanism.
- $D_XW=e_1\cdot\tfrac14\mathbf 1^T$ is rank one. Its norm is $\|e_1\|\cdot\|\tfrac14\mathbf 1\|=1\cdot\tfrac14\cdot2=\tfrac12$.
- Take $t=1$, $R=\{0,1\}$. Then $p_0=\tfrac14\mathbf 1$ and $Wp_0=p_0$. $D_Xp_0=\tfrac14e_1$. $WD_Xp_0=\tfrac1{16}\mathbf 1$. $D_X$ of that is $\tfrac1{16}e_1$. $\mathbf 1^T$ of that is $\tfrac1{16}$. This is the true probability, $\tfrac14\cdot\tfrac14$.
- Norm bound: $\|\mathbf 1\|\,\|D_XW\|^2\,\|p_0\|=2\cdot\tfrac14\cdot\tfrac12=\tfrac14\ge\tfrac1{16}$. The bound holds, but it is loose.

## Concepts
- [[expander-graph]] (new) — $d$-regular graph; for a $1/10$-expander the walk-matrix eigenvalues satisfy $|\omega_i|\le1/10$ for $i\ge2$ (pp. 252, 254)
- [[pseudo-random-generator]] (new) — takes a seed that is presumably random (or has a lot of randomness in it) and generates a long string of bits that are supposed to act random (p. 251)
- [[norm]] — here the operator (2-norm) $\max_v\|Mv\|/\|v\|$ (p. 254)
- [[spectral-theorem]] — used implicitly: for symmetric $M$, the norm equals the largest $|$eigenvalue$|$ (p. 255)
- [[markov-matrix]] — $W=M/d$, the ordinary random-walk transition matrix (p. 254)
- [[eigenvector-eigenvalue]] — $W\mathbf 1=\mathbf 1$; the other eigenvalues have $|\omega_i|\le1/10$ (pp. 254–255)

## Canonical instances
- [[black-box-amplification]] (new) — majority vote over $t+1$ correlated runs has error $\le(2/\sqrt5)^{t+1}$ (p. 253)
- [[path-on-3-vertices-norm]] (new) — an asymmetric walk matrix with norm $\sqrt2>1$ (p. 255)

## Bridges (candidates)
- [structural-analogy] Lemma $\|D_XW\|\le1/5$ ↔ linear algebra: the gap on $\mathbf 1^\perp$ shrinks non-constant parts, as in the Fiedler and spectral-gap theory.
- [metaphor] Product of projections-with-damping ↔ probability: each "bad" visit multiplies by at most $1/5$, like independent trials.

## Questions this raises
- The author calls the proof strange. What is lost or gained by bounding probabilities through $\ell_2$ norms rather than sums?
- How tight is $(2/\sqrt5)^{t+1}$? What would better-than-crude counting of the sets $R$ give?
- What if the box were wrong on a larger fraction than $1/100$, or the expander gap were weaker than $1/10$?

## Exercises worth doing
Unnumbered "do for yourself" tasks (p. 255):
- Prove that for symmetric $M$ the 2-norm is the largest absolute eigenvalue — easy.
- Verify $\|M_1M_2\|\le\|M_1\|\|M_2\|$ — easy.
- Verify that the 3-vertex path's walk matrix has norm $\sqrt2$ — medium.
- Check that running the box only twice does not help (footnote, p. 252) — easy.

## Reading notes
- Printed page = pdf − 24.
- Text layer drops superscripts ("2r" means $2^r$). On p. 251 the text layer shows a stray "w" before "Impagliazzo".
- The alternative proof of $\|Wy\|\le\|y\|/10$ refers to "the proof of Lemma 2.1.3", which is not in these pages. Reference [?] in 31.10 is unresolved in the source.
- The step $\sum_{|R|>t/2}\le2^{t+1}(1/5)^{(t+1)/2}$ is given without detail. I read it as counting at most $2^{t+1}$ subsets $R$ of $T$.
- The section 31.8 chain tacitly uses $c\sqrt n\le\|x\|$ and $\|y\|\le\|x\|$.
- The unit metadata (not these pages) describes the work as an incomplete draft dated April 2, 2025.
