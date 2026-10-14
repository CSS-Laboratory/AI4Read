---
id: polyanskiy-2025-information/ch15-universal
work: polyanskiy-2025-information
unit: "Chapter 13 (file id ch15): Universal compression"
pages: 244–272
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Universal compression

## L0 — One line
Compressing without knowing the source distribution is the same problem as sequential prediction under log-loss: pick a good probability assignment $Q_{X^n}$ for the whole class of sources, and its redundancy equals a channel capacity.

## L1 — The gist (≤ 120 words)
The question: how can we compress when the source law is unknown and only a class of laws is given? The chapter turns every code into a probability assignment $Q_{X^n}$ (length ≈ $\log 1/Q$). The best worst-case redundancy then equals the capacity $\sup_\pi I(\theta;X^n)$. For i.i.d. classes the near-optimal $Q$ is a Jeffreys-prior mixture, whose sequential form is the Krichevsky–Trofimov "add-½" rule. Universal assignments also give online prediction and, via online-to-batch conversion, density estimation; the Shtarkov distribution handles individual-sequence regret. Lempel–Ziv reaches the entropy rate with no model at all, using recurrence times. This links compression to learning and to language-model training.

**Prerequisites:** KL divergence, mutual information and capacity (minimax = maximin), Kraft inequality, Fisher information, Stirling's formula, Gaussian integrals, stationary ergodic processes.

## L2 — Key ideas
- A code built from $Q_{X^n}$ (sorted code, Kraft prefix code, or arithmetic code) has length $\log 1/Q_{X^n}(x^n)$ up to a constant. A universal compressor is therefore just a universal probability assignment (pp. 244–245).
- Factorizing $Q_{X^n}=\prod_t Q_{X_t|X^{t-1}}$ shows universal compression equals sequential prediction under log-loss. Arithmetic coding makes this practical, since it codes bit-by-bit from the conditionals (pp. 245–246).
- Fitingof's type-class construction is universal for all i.i.d. sources, with expected excess length $(|\mathcal X|-1)\log n+O(1)$. It extends to Markov chains, and the Shtarkov/NML code for product distributions recovers it up to $O(\log n)$ differences (pp. 246–249).
- Minimax redundancy $\mathcal R_n^*=\sup_\pi I(\theta;X^n)$ is a channel capacity (the capacity–redundancy theorem). The asymptotically maximin prior is Jeffreys, $\propto\sqrt{\det J_F}$ (pp. 248, 251–253).
- Krichevsky–Trofimov (KT, "add-½") is the Jeffreys mixture. It is $O(1)$-optimal in redundancy and also has $\tfrac12\log n+O(1)$ pointwise regret, in the binary case. Laplace's add-1 rule loses at the endpoints $\theta=0,1$ (pp. 254–255, 260–261).
- Online (average) regret equals the minimax redundancy. Density estimation is the batch problem: it is bounded through online-to-batch conversion, but batch minimizers differ from those of compression. Individual-sequence regret is optimized by the Shtarkov distribution and is $\mathcal R_n^*+O(1)$ for the i.i.d. class treated there (pp. 256–261).
- Lempel–Ziv codes by pointers to the last occurrence of a block. Kac's lemma makes the recurrence time an unbiased estimate of $1/P$. A theorem (with the past known to the decoder) shows that this reaches the entropy rate for every stationary ergodic source (pp. 262–264).

## L3 — Walkthrough

### Chapter introduction (pp. 244–245)
Earlier results need the source law $P_{X^n}$, which is not given for, say, English text. Here the compressor $X^n\to\{0,1\}^*$ faces a class of laws, so compression becomes intertwined with density estimation (p. 244). Plan: (1) Fitingof's distribution-free algorithm; (2) a minimax model $Q_{X^n}$ for a class; (3) Lempel–Ziv, which adapts automatically (p. 244).

All logs are binary. Three constructions turn a $Q_{X^n}$ into a code (pp. 244–245):
- sort $x^n$ by decreasing $Q$ and assign strings as in Theorem 10.2, giving $\ell(f(x^n))\le\log\frac1{Q(x^n)}$;
- set $\ell=\lceil\log\frac1{Q}\rceil$ and use Kraft to build a prefix code;
- arithmetic coding.

In all cases $\ell(f(x^n))=\log\frac1{Q_{X^n}(x^n)}\pm$ universal constant (p. 245). In this architecture the only task is to specify $Q_{X^n}$, called a *universal probability assignment*. With $Q_{X^n}=\prod_{t=1}^nQ_{X_t|X^{t-1}}$, universal compression is equivalent to sequential prediction under log-loss, a form of density estimation (p. 245). As of 2022 the best text compressors use a transformer whose parameters are updated by SGD as the text is processed (p. 245).

> **Intuition note.** A code length is a hidden probability. Choosing a compressor for an unknown source means choosing a probability model that is never badly wrong on any source in the class.

### 13.1 Arithmetic coding (pp. 245–246)
A full encoder table for $Q_{X^n}$ is costly for large $n$. Arithmetic coding outputs bits sequentially. It needs $Q_{X^n}$ and its marginals $Q_{X_1},Q_{X_2},\dots$ to be easy to compute. Shtarkov distributions (13.12)–(13.14) do not have this property, since they are not compatible across $n$ (p. 245).

Order the alphabet and extend lexicographically to $\mathcal X^n$. Define
$$F_n(x^n)=\sum_{y^n<x^n}Q_{X^n}(y^n),\qquad I_{x^n}=[F_n(x^n),\,F_n(x^n)+Q_{X^n}(x^n)).$$
These are disjoint subintervals of $[0,1)$. Encode
$$x^n\mapsto \text{largest dyadic interval }D_{x^n}\subseteq I_{x^n}\tag{13.1}$$
(leftmost if two are possible). A dyadic interval $[m2^{-k},(m+1)2^{-k})$ is written as the $k$-bit binary expansion $0.b_1\dots b_k$ of $m2^{-k}$. Examples: $[3/4,7/8)\mapsto110$, $[3/4,13/16)\mapsto1100$ (p. 246). This is a prefix code with
$$\log_2\tfrac1{Q_{X^n}(x^n)}\le\ell(f(x^n))\le\Big\lceil\log_2\tfrac1{Q_{X^n}(x^n)}\Big\rceil+1\tag{13.2}$$
(proved in Ex. II.13, p. 246). Sequential computation:
$$F_n(x^n)=F_{n-1}(x^{n-1})+Q_{X^{n-1}}(x^{n-1})\sum_{y<x_n}Q_{X_n|X^{n-1}}(y|x^{n-1}),$$
so $F_n$ is computable sequentially if $Q_{X^{n-1}}$ and $Q_{X_n|X^{n-1}}$ are. The learned conditionals can be updated on the fly (e.g. switching to an English model inside an executable) (p. 246). Implementation depends on number-theoretic properties of the denominators when the interval is renormalized. J. Duda's asymmetric numeral systems (ANS) brought large speed gains and were adopted by most compression libraries (p. 246).

### 13.2 Combinatorial construction of Fitingof (pp. 246–247)
Fitingof assigns to $x^n$ the information $\Phi_0(x^n)$ = log of the size of its type class (all permutations of $x^n$). By Proposition 1.5 (p. 246):
$$\Phi_0(x^n)=nH(x_T)+O(\log n)=nH(\hat P_{x^n})+O(\log n),\quad T\sim\mathrm{Unif}([n]),\tag{13.3–13.4}$$
$$\hat P_{x^n}(a)=\tfrac1n\sum_{i=1}^n\mathbf 1\{x_i=a\}.\tag{13.5}$$
He argues a prefix code exists with $\ell(f(x^n))=\Phi_0(x^n)+O(\log n)$ (13.6). Define
$$Q_{X^n}(x^n)\triangleq\exp\{-\Phi_0(x^n)\}\,c_n,\qquad c_n=1\Big/\tbinom{n+|\mathcal X|-1}{|\mathcal X|-1}=O(n^{-(|\mathcal X|-1)}).\tag{13.7}$$
The constant $c_n$ is the reciprocal of the number of types. Kraft then gives the code (p. 247). Footnote 1 gives a two-part encoding: first the type class ($(|\mathcal X|-1)\log n$ bits), then the element ($\Phi_0$ bits). Taking expectations under any i.i.d. source:
$$\mathbb E[\ell(f(X^n))]=nH(P_X)+(|\mathcal X|-1)\log n+O(1).$$

**Markov chains.** Define $\Phi_1(x^n)$ as the log of the number of rearrangements of $x^n$ with the same digram statistics. Asymptotically $\Phi_1=nH(x_T|x_{T-1})+O(\log n)$, with $T-1$ taken mod $n$. A code with $\ell=\Phi_1+O(\log n)$ exists, so for every first-order stationary Markov chain $\mathbb E[\ell(f(X^n))]=nH(X_2|X_1)+O(\log n)$. Continuing with $\Phi_2,\dots$ handles higher orders (p. 247).

> **Intuition note.** Fitingof counts how many sequences look statistically like $x^n$ and pays the log of that count, with no probabilities involved. The overhead is only about $\log n$ per free parameter.

### 13.3 Optimal compressors for a class; redundancy (pp. 247–250)
So far $\mathbb E[\ell(f(X^n))]\le H(X^n)+o(n)$ simultaneously for all i.i.d. (or $r$-th order Markov) sources (p. 247). Krichevsky proposed the next target: minimize the redundancy $\mathbb E[\ell(f(X^n))]-H(X^n)$ over a class (p. 247). For a class $\{P_{X^n|\theta}\}$, the redundancy of $f$ is $\sup_{\theta_0}\mathbb E[\ell(f(X^n))|\theta_0]-H(X^n|\theta_0)$. Replacing lengths by $\log\frac1Q$, the redundancy of $Q$ is $\sup_{\theta_0}D(P_{X^n|\theta_0}\|Q_{X^n})$ (p. 248).

**Definition 13.1.** The minimax redundancy is
$$\mathcal R_n^*(\Theta)\triangleq\min_{Q_{X^n}}\sup_{\theta_0\in\Theta}D(P_{X^n|\theta=\theta_0}\|Q_{X^n}).\tag{13.8}$$
If $\mathcal R_n^*<\infty$, Theorem 5.9 gives
$$\mathcal R_n^*=\sup_\pi\min_{Q_{X^n}}D(P_{X^n|\theta}\|Q_{X^n}|\pi)\tag{13.9}$$
$$=\sup_\pi I(\theta;X^n),\tag{13.10}$$
over priors $\pi\in\mathcal P(\Theta)$. Thus redundancy is the capacity of the channel $\theta\to X^n$ (the *capacity–redundancy theorem*), which was surprising in the early days (p. 248).

Finding the exact minimizer is daunting even for Bernoulli ($\Theta=[0,1]$). For smooth families the capacity-achieving prior is discrete with $k_n$ atoms, $k_n$ growing slowly. Physicists conjectured a universal relation $\mathcal R_n^*=\frac34\log k_n+o(\log k_n)$ for all parametric families; for Bernoulli it would give $k_n\asymp n^{2/3}$, "but even this is open" (p. 248). These unwieldy priors do converge to the Jeffreys prior (p. 248).

**Remark 13.1 (Shtarkov, individual sequences).** Choose $Q$ to minimize the worst-case redundancy for each realization (not on average):
$$\mathcal R_n^{**}(\Theta)\triangleq\min_{Q_{X^n}}\max_{x^n}\sup_{\theta_0\in\Theta}\log\frac{P_{X^n|\theta}(x^n|\theta_0)}{Q_{X^n}(x^n)}.\tag{13.11}$$
The minimizer is the Shtarkov (normalized maximal likelihood, NML) distribution
$$Q^{(S)}_{X^n}(x^n)=\frac1Z\sup_{\theta_0}P_{X^n|\theta}(x^n|\theta_0),\qquad Z=\sum_{x^n}\sup_{\theta_0}P_{X^n|\theta}(x^n|\theta_0)\ \text{(Shtarkov sum)}.\tag{13.12–13.13}$$
For the class of all product distributions:
$$Q^{(S)}_{X^n}(x^n)=\frac{\exp\{-nH(\hat P_{x^n})\}}{\sum_{x^n}\exp\{-nH(\hat P_{x^n})\}}.\tag{13.14}$$
This recovers Fitingof's $\Phi_0$ up to $O(\log n)$ differences between $nH(\hat P_{x^n})$ and $\Phi_0(x^n)$. First-order Markov chains give $\Phi_1$, and so on (p. 249). Problem (13.11) is the per-sequence regret
$$\min_{Q}\max_{x^n}\Big\{\log\frac1{Q_{X^n}(x^n)}-\inf_{\theta_0}\log\frac1{P_{X^n|\theta}(x^n|\theta_0)}\Big\}.\tag{13.15}$$
So Shtarkov's $Q$ compresses any $x^n$ almost as well as the best compressor tailored to the class, whether or not $x^n$ came from the class (p. 249).

**Remark 13.2 (two redundancies).** $\mathcal R_n^{**}$ is the worst-case (pointwise) minimax redundancy. $\mathcal R_n^*$ in (13.8) is the average-case one. For many classes (i.i.d., finite-order Markov) they agree in the leading term, but not in general (Ex. II.21 gives $\mathcal R_n^*<\infty$, $\mathcal R_n^{**}=\infty$). Since $\mathcal R_n^*\le\mathcal R_n^{**}$, one typically upper-bounds $\mathcal R_n^{**}$ combinatorially and lower-bounds $\mathcal R_n^*$ via (13.10) with a chosen prior (pp. 249–250).

**Remark 13.3 (single-shot codes).** A prefix code defines $Q_{X^n}=2^{-\ell(f(x^n))}$, assuming a full code tree. For single-shot codes without the prefix constraint the optimal answers differ slightly. For example, the optimal universal single-shot code for all i.i.d. sources has excess $\approx\frac{|\mathcal X|-3}{2}\log n$, versus $\frac{|\mathcal X|-1}{2}\log n$ for prefix codes (p. 250).

### 13.4* Asymptotic maximin solution: Jeffreys prior (pp. 250–253)
**Setting.** Class: all i.i.d. laws on $\mathcal X=\{0,\dots,d\}$ ($d$-parameter family). $\Theta=\{(\theta_1,\dots,\theta_d):\sum\theta_j\le1,\theta_j\ge0\}$, $\theta_0=1-\sum_{j\ge1}\theta_j$, and
$$P_{X^n|\theta}(x^n|\theta)=\prod_j\theta_{x_j}=\exp\Big\{-n\sum_a\theta_a\log\frac1{\hat P_{x^n}(a)}\Big\}\quad\text{(as printed; see Reading notes)}.$$
Dirichlet$(\alpha_0,\dots,\alpha_d)$ has density $c(\alpha)\prod_{j=0}^d\theta_j^{\alpha_j-1}$ on $(\theta_1,\dots,\theta_d)$, with $c=\Gamma(\sum\alpha_j)/\prod\Gamma(\alpha_j)$ (13.16). Search for $\pi$ among smooth densities and set
$$Q_{X^n}(x^n)\triangleq\int_\Theta P_{X^n|\theta}(x^n|\theta')\pi(\theta')d\theta'.\tag{13.17}$$

**Laplace method.** Suppose $f$ has a unique minimum at an interior point $\hat\theta$ and its $d\times d$ Hessian is uniformly lower-bounded by a multiple of the identity. Taylor-expanding $\pi$ and $f$:
$$\int_\Theta\pi(\theta)e^{-nf(\theta)}d\theta=\int(\pi(\hat\theta)+O(\|t\|))e^{-n(f(\hat\theta)-\frac12t^T\mathrm{Hess}f(\hat\theta)t+o(\|t\|^2))}dt\tag{13.18}$$
$$=\pi(\hat\theta)e^{-nf(\hat\theta)}\int_{\mathbb R^d}e^{-x^T\mathrm{Hess}f(\hat\theta)x}\frac{dx}{\sqrt{n^d}}(1+O(n^{-1/2}))\tag{13.19}$$
$$=\pi(\hat\theta)e^{-nf(\hat\theta)}\Big(\frac{2\pi}n\Big)^{d/2}\frac1{\sqrt{\det\mathrm{Hess}f(\hat\theta)}}(1+O(n^{-1/2})),\tag{13.20}$$
the last step being a Gaussian integral (p. 251; sign in (13.18) as printed, see Reading notes).

Now $P_{X^n|\theta}(x^n|\theta')=\exp\{-n(D(\hat P_{x^n}\|P_{X|\theta=\theta'})+H(\hat P_{x^n}))\}$. Write $\hat\theta(x^n)=\hat P_{x^n}$. Applying (13.20) to (13.17), and using $\mathrm{Hess}_{\theta'}D(\hat P\|P_{X|\theta=\theta'})|_{\theta'=\hat\theta}=\frac1{\log e}J_F(\hat\theta)$ (Fisher information matrix, $d\times d$, from (2.34)):
$$\log Q_{X^n}(x^n)=-nH(\hat\theta)+\frac d2\log\frac{2\pi}{n\log e}+\log\frac{P_\theta(\hat\theta)}{\sqrt{\det J_F(\hat\theta)}}+O(n^{-1/2}).$$
Under $X^n\sim P_{X^n|\theta=\theta'}$, $\hat\theta=\theta'+O(n^{-1/2})$, so
$$D(P_{X^n|\theta=\theta'}\|Q_{X^n})=n(\mathbb E[H(\hat\theta)]-H(X|\theta=\theta'))+\frac d2\log n-\log\frac{P_\theta(\theta')}{\sqrt{\det J_F(\theta')}}+C+O(n^{-1/2}),\tag{13.21}$$
with $C$ independent of the prior and of $\theta'$ (p. 251).

**Lemma 13.2.** Let $X^n$ be i.i.d. $\sim P$ on a finite $\mathcal X$ with $P(x)>0$ for all $x$, and $\hat P=\hat P_{X^n}$. Then $\mathbb E[D(\hat P\|P)]=\frac{|\mathcal X|-1}{2n}\log e+o(1/n)$. In fact $nD(\hat P\|P)\to\frac{\log e}2\chi^2(|\mathcal X|-1)$ in distribution (p. 251).
*Proof (p. 252).* By the CLT, $\sqrt n(\hat P-P)\to\mathcal N(0,\Sigma)$ with $\Sigma=\mathrm{diag}(P)-PP^T$ ($P$ an $|\mathcal X|\times1$ vector). A second-order Taylor expansion of $D(\cdot\|P)$ (cf. (2.34), (2.37)) gives the result. Exchanging limit and expectation needs conditioning on $\hat P_n(x)\in(\epsilon,1-\epsilon)$; this is left as an exercise.

(added step) Since $\mathbb E[H(\hat P)]-H(P)=-\mathbb E[D(\hat P\|P)]$ for i.i.d. data, the first term of (13.21) becomes the constant $-\frac d2\log e+o(1)$. The text only says this term "is handled" by the lemma and then gives
$$D(P_{X^n|\theta=\theta'}\|Q_{X^n})=\frac d2\log n-\log\frac{\pi(\theta')}{\sqrt{\det J_F(\theta')}}+\text{constant}+O(n^{-1/2}),\tag{13.22}$$
assuming $\pi$ smooth and $\theta'$ not on the boundary. For $\pi$ to be the saddle point we need $\pi(\theta')\propto\sqrt{\det J_F(\theta')}$, provided the right side is integrable. This is the **Jeffreys prior**. With the explicit Fisher information (2.39) it is Dirichlet$(1/2,\dots,1/2)$:
$$\pi^*(\theta)=c_d\frac1{\sqrt{\prod_{j=0}^d\theta_j}},\quad c_d=\frac{\Gamma(\frac{d+1}2)}{\Gamma(1/2)^{d+1}},\tag{13.23}$$
$$\mathcal R_n^*=\frac d2\log\frac n{2\pi e}-\log\frac{\Gamma(\frac{d+1}2)}{\Gamma(1/2)^{d+1}}+o(1).\tag{13.24}$$
Making this rigorous is "far from trivial" and was done in [460]. For $d=1$, Ex. II.15–II.16 show $\mathcal R_n^*=\frac12\log n+O(1)$ (p. 252). Jeffreys prior maximizes $\sup_\pi I(\theta;X^n)$ within $o(1)$, so it is the *asymptotically maximin* solution. The corresponding mixture $Q^{(KT)}_{X^n}$ is, surprisingly [405], *not* asymptotically minimax: for some constants $c_1,c_2$ (printed as $c_1>c_2>0$; see Reading notes)
$$\mathcal R_n^*+c_1+o(1)\le\sup_{\theta_0}D(P_{X^n|\theta_0}\|Q^{(KT)}_{X^n})\le\mathcal R_n^*+c_2+o(1).$$
It is optimal up to $O(1)$. Patching Jeffreys near the simplex boundary, or mixing Dirichlets, gives asymptotically minimax assignments [460] (p. 252).

**General smooth families (p. 253).** That Jeffreys maximizes $I(\theta;X^n)$ was conjectured in [46] and proved in [95, 96]. Let $\{P_\theta:\theta\in\Theta_0\}$ be smooth with continuous bounded Fisher information on the interior of $\Theta_0\subset\mathbb R^d$. For every compact $\Theta$ in the interior:
$$\mathcal R_n^*(\Theta)=\frac d2\log\frac n{2\pi e}+\log\int_\Theta\sqrt{\det J_F(\theta)}\,d\theta+o(1).\tag{13.25}$$
To get an approximate capacity-achieving $Q_{X^n}$, one mixes with Jeffreys prior on a slightly larger set $\Theta_\epsilon=\{\theta:d(\theta,\Theta)\le\epsilon\}$, with $\epsilon\to0$ slowly with $n$. This achieves optimal redundancy up to $o(1)$.

**Remark 13.4 (Laplace's law of succession).** For "will the sun rise tomorrow", Laplace modelled sunrise as i.i.d. Bernoulli with uniform prior on $\theta$. The author calls this "not very logical", since uniformity of $\alpha=\theta^{10}$ or $\beta=\sqrt\theta$ is equally postulable. Jeffreys prior $\frac1{\sqrt{\theta(1-\theta)}}$ is invariant under reparametrization: $\sqrt{\det J_F(\alpha)}$ in the $\alpha=\theta^{10}$ parametrization is exactly the pushforward of $\frac1{\sqrt{\theta(1-\theta)}}$ along $\theta\mapsto\theta^{10}$ (p. 253).

> **Intuition note.** A mixture over $\theta$ pays about $\frac d2\log n$ bits for "learning" $d$ parameters. The prior only changes the constant, and Jeffreys makes that constant the same for every true $\theta$ away from the boundary. That is why it is the worst-case-optimal choice.

### 13.5 Sequential probability assignment: Krichevsky–Trofimov (pp. 253–255)
Bernoulli case ($d=1$). Jeffreys prior and mixture:
$$P^*_\theta=\frac1{\pi\sqrt{\theta(1-\theta)}},\qquad Q^{(KT)}_{X^n}(x^n)=\frac{(2t_0-1)!!\,(2t_1-1)!!}{2^nn!},\quad t_a=\#\{j\le n:x_j=a\}.\tag{13.26–13.27}$$
(Footnote 4: from $\int_0^1\frac{\theta^a(1-\theta)^b}{\sqrt{\theta(1-\theta)}}d\theta=\pi\frac{(2a-1)!!(2b-1)!!}{2^{a+b}(a+b)!}$, derived by a keyhole contour; $(2a-1)!!=1\cdot3\cdots(2a-1)$.) Because $P_\theta$ does not depend on $n$, $Q_{X^{n-1}}$ is the marginal of $Q_{X^n}$ (true for any such mixture). The conditionals are elegant:
$$Q^{(KT)}_{X_n|X^{n-1}}(1|x^{n-1})=\frac{t_1+\frac12}n,\quad Q^{(KT)}_{X_n|X^{n-1}}(0|x^{n-1})=\frac{t_0+\frac12}n,\tag{13.28–13.29}$$
with $t_a$ counted over the first $n-1$ symbols: the "add-½" rule. Let $f_{KT}$ have length $\lceil\log_2 1/Q^{(KT)}(x^n)\rceil$. Then $\sup_{0\le\theta\le1}\{\mathbb E[\ell(f_{KT}(S_n^\theta))]-nh(\theta)\}=\frac12\log n+O(1)$ ($h$ = binary entropy). This follows from (13.24); since (13.24) was not shown rigorously, the upper bound is proved independently in Ex. II.15 (p. 254).

**Remark 13.5 (Laplace add-1).** With uniform prior,
$$Q^{(Lap)}_{X^n}=\frac1{\binom nw(n+1)},\quad w=\#\{j:x_j=1\},\tag{13.30}$$
with conditional $\frac{t_1+1}{n+1}$. This is exactly Fitingof's (13.7). For i.i.d. Ber($\theta$), with $W\sim\mathrm{Bin}(n,\theta)$ (p. 254):
$$\mathbb E\log\frac1{Q^{(Lap)}(X^n)}-H(X^n)=\log(n+1)+\mathbb E\log\tbinom nW-nh(\theta).\tag{13.31}$$
By Stirling this is $\frac12\log n+O(1)$ uniformly on compact subsets of $(0,1)$. At $\theta=0$ or $1$ it equals $\log(n+1)$, so the supremum is near the endpoints and gives suboptimal redundancy $\log n+O(1)$. Jeffreys/KT fixes the endpoint problem (p. 254).

General alphabet:
$$Q^{(KT)}_{X_n|X^{n-1}}(a|x^{n-1})=\frac{t_a+\frac12}{n+\frac{|\mathcal X|-2}2},\quad t_a=\#\{j\le n-1:x_j=a\}.\tag{13.32}$$
Recipe (p. 255): the learner sets $Q_{X_1}=\mathrm{Unif}[\mathcal X]$; the arithmetic encoder subdivides $[0,1]$ and selects the cell of $x_1$; the learner computes $Q_{X_2|X_1=x_1}$ by (13.32); the encoder subdivides the selected cell, and so on. Only the encoder state produces bits, but the learner's $Q_{X_n|X^{n-1}}$ is itself an online density estimator (next section).

### 13.6 Online prediction and density estimation (pp. 255–259)
A universal probability assignment automatically solves online prediction and density estimation (p. 255). Fix a model class $\{P^{(\theta)}_{X^n}\}$ (not necessarily i.i.d.; $\mathcal X$ discrete).

**Online prediction.** Given $X^n\sim P^{(\theta^*)}_{X^n}$, the learner sees $X^{t-1}$, outputs $Q_t(\cdot)$ and suffers log-loss $\ell(Q_t,X_t)=\log\frac1{Q_t(X_t)}$. Average cumulative loss:
$$\ell_n^{(a)}(\{Q_t\},\theta^*)=\mathbb E_{P^{(\theta^*)}_{X^n}}\Big[\sum_{t=1}^n\log\frac1{Q_t(X_t|X^{t-1})}\Big].$$
Since $Q_t$ depends on $x^{t-1}$, it is a kernel $Q_{X_t|X^{t-1}}$, giving the joint
$$Q_{X^n}(x^n)\triangleq\prod_{t=1}^nQ_t(x_t;x^{t-1}),\tag{13.33}$$
and conversely any $Q_{X^n}$ factorizes into a predictor (p. 256).

Minimizing $\min_{\{Q_t\}}\sup_{\theta^*}\ell_n^{(a)}$ is a bad problem: if $\mathrm{Unif}[\mathcal X^n]$ is in the class, no predictor beats $n\log|\mathcal X|$, and $Q_t=\mathrm{Unif}[\mathcal X]$ attains it exactly. With oracle knowledge of $\theta^*$, the best predictor is the factorization of $P^{(\theta^*)}_{X^n}$ (Cor. 2.4), with loss $H(P^{(\theta^*)}_{X^n})$ (Bayes loss), of order $n$ for i.i.d. classes. So measure the excess, the *average regret*:
$$\mathrm{AvgReg}_n(\{Q_t\},\theta^*)=\mathbb E_{P^{(\theta^*)}_{X^n}}\Big[\sum_t\log\frac1{Q_t(X_t|X^{t-1})}\Big]-H(P^{(\theta^*)}_{X^n}),\qquad \mathrm{AvgReg}_n^*(\Theta)=\inf_{\{Q_t\}}\sup_{\theta^*\in\Theta}\mathrm{AvgReg}_n.\tag{13.34}$$

**Theorem 13.3.** $\mathrm{AvgReg}_n^*(\Theta)=\mathcal R_n^*(\Theta)=\min_{Q_{X^n}}\sup_{\theta^*}D(P^{(\theta^*)}_{X^n}\|Q_{X^n})$. The minimum is achieved at a unique $Q^*_{X^n}$, and the optimal predictor is $Q_t=Q^*_{X_t|X^{t-1}=x^{t-1}}$. With a prior $\pi$ on $\theta$, $\mathrm{AvgReg}_n^*(\Theta)=\sup_\pi I(\theta;X^n)$. If a maximizer $\pi^*$ exists, then $Q^*_{X^n}=\int\pi^*(d\theta)\prod_iP_\theta(x_i)$ (p. 257).
*Proof.* "Almost nothing to prove": $\mathrm{AvgReg}_n=\mathbb E\log\frac{P^{(\theta^*)}_{X^n}}{Q_{X^n}}=D(P^{(\theta^*)}_{X^n}\|Q_{X^n})$. The rest follows from Theorems 5.9 and 5.4 (using $I(\theta;X^n)\le n\log|\mathcal X|<\infty$).

Application: for i.i.d. $X^n\sim P$, KT gives $\sum_t\mathbb E\log\frac1{Q^{(KT)}(X_t|X^{t-1})}\le nH(P)+\frac{|\mathcal X|-1}2\log n+c_{\mathcal X}$, with $c_{\mathcal X}$ independent of $P,n$. This excess is optimal among online estimators up to a constant (p. 257).

Large language models solve precisely this feature-less task, minimizing log-loss (cross-entropy) on word sequences; learning is feasible there because the sequence is non-i.i.d. A supervised version, predicting $Y_t$ from features $X_t$, has an analogue of Theorem 13.3 (Ex. II.20, II.22) (p. 257).

**Batch regret.** Here the first $n-1$ observations are training data and only the new sample is assessed:
$$\mathrm{BatchReg}_n^*(\Theta)\triangleq\inf_{Q_n(\cdot;x^{n-1})}\sup_{\theta^*}\mathbb E\Big[\log\frac1{Q_n(X_n;X^{n-1})}\Big]-H(P^{(\theta^*)}_{X_n|X^{n-1}}).\tag{13.35}$$
This is the KL loss of estimating the next-symbol conditional, as in GPT-type models (p. 258). There is a max-information formula (Ex. II.19) and an online-to-batch bound:
$$\mathrm{AvgReg}_n^*-\mathrm{AvgReg}_{n-1}^*\le\mathrm{BatchReg}_n^*\le\frac1n\mathrm{AvgReg}_n^*,\tag{13.36}$$
where the upper bound is guaranteed only for i.i.d. models (footnote 5: for stationary $m$-th order Markov models the denominator is $n-m$). It is achieved by averaging the conditionals of a $Q^*_{X^n}$:
$$Q_n(x_n;x^{n-1})\triangleq\frac1n\sum_{t=1}^nQ_{X_t|X^{t-1}}(x_n|x^{t-1}).\tag{13.37}$$
Batch minimizers differ from compression minimizers. For i.i.d. laws over $k$ symbols, KT is optimal for cumulative regret but not for batch loss (note at end of Ex. VI.10). The optimal batch regret is $O(\frac{k-1}n)$ while online-to-batch gives only $O(\frac{(k-1)\log n}n)$. For first-order Markov chains with $k\ge3$ states, $\mathrm{BatchReg}_n^*\asymp\frac1n\mathrm{AvgReg}_n^*\asymp\frac{k^2}n\log\frac n{k^2}$ when $n\gg k^2$ [213], so the bound is order-optimal there (p. 258).

**Density estimation.** Given $X_1,\dots,X_{n-1}$ i.i.d. $\sim P^{(\theta)}_X$, find $\hat P$ minimizing $\sup_{\theta^*}\mathbb E[D(\hat P\|P_X^{(\theta^*)})]$. Interpreting $\hat P$ as $Q_n$ in batch regret:
$$\inf_{\hat P}\sup_{\theta^*}\mathbb E\,D(\hat P\|P^{(\theta^*)}_X)=\mathrm{BatchReg}_n^*(\Theta)\le\frac1n\sup_\pi I(\theta;X^n).$$
So the minimax KL density-estimation rate is bounded by a channel capacity. The estimator (13.37) is improper ($\hat P\ne P_X^{(\theta)}$ for every $\theta$). This is the Yang–Barron approach (Section 32.1) (p. 259).

> **Intuition note.** The learner's one-step-ahead guess $Q_{X_t|X^{t-1}}$ both drives the arithmetic coder and is the best worst-case predictor. Total expected log-loss beyond the entropy equals the redundancy of the ideal code lengths $\log 1/Q$ (an actual arithmetic code adds less than 2 bits, p. 246).

### 13.7 Individual sequence and worst-case regret (pp. 259–261)
Criticism of Section 13.6: the real data may come from no process in the model class. The individual-sequence approach predicts any $x^n$, even adversarial. Nature picks $x^n$; at each $t$ we output $Q_t(\cdot|x^{t-1})$ and pay $\log\frac1{Q_t(x_t|x^{t-1})}$; the cumulative loss is $\ell(\{Q_t\},x^n)=\sum_t\log\frac1{Q_t(x_t|x^{t-1})}$ (p. 259).

Worst-case loss $\min\max_{x^n}\ell$ is hopeless: each $Q_t$ has an atom of weight at most $1/|\mathcal X|$, so $\max_{x^n}\ell\ge n\log|\mathcal X|$, attained iff $Q_t\equiv1/|\mathcal X|$ (pp. 259–260). The idea of Feder–Merhav–Gutman is to use *regret against a static oracle* that sees the whole $x^n$ and outputs a constant $Q$. By non-negativity of divergence it achieves $\ell_{\text{oracle}}(x^n)=\min_Q\sum_t\log\frac1{Q(x_t)}=nH(\hat P_{x^n})$. Then
$$\mathrm{reg}(\{Q_t\},x^n)\triangleq\ell(\{Q_t\},x^n)-nH(\hat P_{x^n}),\qquad \mathrm{Reg}_n^*\triangleq\min_{\{Q_t\}}\max_{x^n}\mathrm{reg}.\tag{13.38}$$
For $\mathcal X=\{0,1\}$, designing $\{Q_t\}$ is equivalent to choosing $Q_{X^n}$, so $\mathrm{Reg}_n^*=\min_{Q}\max_{x^n}\log\frac1{Q(x^n)}-nH(\hat P_{x^n})$. The optimizer is the Shtarkov distribution, so the regret is the log of the Shtarkov sum. In the i.i.d. case, by (13.14),
$$\mathrm{Reg}_n^*=\log\sum_{x^n}\max_Q\prod_iQ(x_i)=\log\sum_{x^n}\exp\{-nH(\hat P_{x^n})\}.$$
This is hard to analyze directly, so use bounds (p. 260):
- Lower: replace $\max_{x^n}$ by the average over $X^n\sim\mathrm{Ber}(\theta)^n$ and apply Lemma 13.2: $\mathrm{Reg}_n^*\ge\mathcal R_n^*+\frac{|\mathcal X|-1}2\log e+o(1)$.
- Upper: for KT (13.27), "after some algebra and Stirling", $\max_{x^n}\log\frac1{Q^{(KT)}(x^n)}-nH(\hat P_{x^n})=\frac12\log n+O(1)$.

Conclusion:
$$\mathrm{Reg}_n^*=\mathcal R_n^*+O(1)=\frac{|\mathcal X|-1}2\log n+O(1),$$
so the per-letter regret $\frac1n\mathrm{Reg}_n^*\to0$ (p. 261). A causal predictor can match the best constant predictor even if that predictor was fitted non-causally to the sequence. KT's add-½ rules are asymptotically optimal and "horizon-free" (independent of $n$); the sequential predictors from factorizing Shtarkov's distribution lack this property (p. 261).

**General parametric families.** Define $\mathrm{Reg}_n^*(\Theta)=\min_Q\sup_{x^n}\big[\log\frac1{Q(x^n)}-\inf_{\theta_0}\log\frac1{P_{X^n|\theta_0}(x^n)}\big]$. Under smoothness conditions [362]:
$$\mathrm{Reg}_n^*(\Theta)=\mathcal R_n^*(\Theta)+\frac d2\log e+o(1)=\frac d2\log\frac n{2\pi}+\log\int_\Theta\sqrt{\det J_F(\theta)}d\theta+o(1).$$
In machine-learning terms, $\mathcal R_n^*$ is cumulative regret in the well-specified setting and $\mathrm{Reg}_n^*$ in the fully mis-specified one. Intermediate settings exist, e.g. i.i.d. data not from the class [162] (p. 261).

### 13.8 Lempel–Ziv compressor (pp. 261–264)
For classes beyond i.i.d. (e.g. $r$-th order Markov), the sequential rules from Jeffreys-type priors become complex. Lempel–Ziv (LZ) skips "design $Q_{X^n}$, convert to conditionals, extract compressor" and builds a simple sequential compressor directly. The implied $Q_{X^n}$ is hard to imagine and its redundancy is hard to derive, but the algorithm is transparent (p. 261).

Learn-then-compress could work: estimate $\hat P_{X_n|X_{n-r}^{n-1}}$ and use it for arithmetic coding, attaining the entropy rate if $\hat P$ converges. KT is itself learning the distribution, so, the author says, "in some sense the converse is also true: any good universal compression scheme is inherently learning the true distribution" (p. 262; the KT estimator converges to $P_X$ if the sequence is i.i.d.). The drawback: learning the law of $r$-blocks needs a sample size exponential in $r$. LZ works around this (p. 262):
- Rare substrings take longest to estimate but are least useful, since they almost never appear.
- Most crucial: an unbiased estimate of $P_{X^r}(x^r)$ is the reciprocal of the time since the last occurrence of $x^r$ in the stream.
- There is a prefix code for integers with
$$f_{int}:\mathbb Z_+\to\{0,1\}^+,\quad\ell(f_{int}(n))=\log_2n+O(\log\log n).\tag{13.39}$$
(Footnote 6: $\sum_k2^{-\log_2k-2\log_2\log(k+1)}<\infty$, then Kraft; see Ex. II.18.) A pointer to the last occurrence of $x^r$ thus costs about $\log\frac1{P_{X^r}(x^r)}$ bits automatically.

The text gives only a rough explanation, analyzing no particular algorithm (p. 262).

**Lemma 13.4 (Kac).** Let $\dots,X_{-1},X_0,X_1,\dots$ be finite-alphabet, stationary and ergodic, and $L=\inf\{t>0:X_{-t}=X_0\}$. For any $u$ with $\mathbb P[X_0=u]>0$,
$$\mathbb E[L|X_0=u]=\frac1{\mathbb P[X_0=u]};\quad\text{in particular }\mathbb E[L]=|\mathrm{supp}(P_X)|.$$
*Proof (pp. 262–263).* By stationarity $\mathbb P[\exists t\ge k:X_t=u]$ does not depend on $k$, so by continuity take $k=-\infty$: $\mathbb P[\exists t\ge0:X_t=u]=\mathbb P[\exists t\in\mathbb Z:X_t=u]$. This event is shift-invariant, so by ergodicity its probability is 0 or 1; it is not 0 since $\mathbb P[X_0=u]>0$. Hence
$$\mathbb P[\exists t\ge0:X_t=u]=1.\tag{13.40}$$
Then
$$\begin{aligned}\mathbb E[L|X_0=u]&=\sum_{t\ge1}\mathbb P[L\ge t|X_0=u]&(13.41)\\&=\tfrac1{\mathbb P[X_0=u]}\sum_{t\ge1}\mathbb P[L\ge t,X_0=u]&(13.42)\\&=\tfrac1{\mathbb P[X_0=u]}\sum_{t\ge1}\mathbb P[X_{-t+1}\ne u,\dots,X_{-1}\ne u,X_0=u]&(13.43)\\&=\tfrac1{\mathbb P[X_0=u]}\sum_{t\ge1}\mathbb P[X_0\ne u,\dots,X_{t-2}\ne u,X_{t-1}=u]&(13.44)\\&=\tfrac1{\mathbb P[X_0=u]}\mathbb P[\exists t\ge0:X_t=u]&(13.45)\\&=\tfrac1{\mathbb P[X_0=u]}.&(13.46)\end{aligned}$$
(13.44) uses stationarity; (13.45) holds because events for different $t$ are disjoint; (13.46) uses (13.40).

**Theorem 13.5.** Let the process be finite-alphabet, stationary and ergodic with entropy rate $H$, and suppose $X_{-\infty}^{-1}$ is known to the decoder. Then there are prefix codes $f_n(x_0^{n-1},x_{-\infty}^{-1})$ with $\frac1n\mathbb E[\ell(f_n(X_0^{n-1},X_{-\infty}^{-1}))]\to H$.
*Proof (pp. 263–264).* Let $L_n=\inf\{t>0:x_{-t}^{-t+n-1}=x_0^{n-1}\}$ be the last occurrence of the block in the past. Kac's lemma for $Y_t^{(n)}=X_t^{t+n-1}$ gives $\mathbb E[L_n|X_0^{n-1}=x_0^{n-1}]=1/\mathbb P[X_0^{n-1}=x_0^{n-1}]$. Encode $L_n$ with (13.39). Subtlety: even when $L_n<n$ and the two windows overlap, $x_0^{n-1}$ can be decoded from $L_n$. Applying Jensen's inequality twice, with $\frac1nH(X_0^{n-1})\searrow H$ and $\frac1n\log H(X_0^{n-1})\to0$:
$$\frac1n\mathbb E[\ell(f_{int}(L_n))]\le\frac1n\mathbb E\Big[\log\frac1{P_{X_0^{n-1}}(X_0^{n-1})}\Big]+o(1)\to H.$$
Conversely, by Kraft's inequality any prefix code has $\frac1n\mathbb E[\ell(f_{int}(L_n))]\ge\frac1nH(X_0^{n-1}|X_{-\infty}^{-1})=H$.

> **Intuition note.** A block that appeared $L$ steps ago has probability roughly $1/L$, so naming "$L$ steps back" costs about $\log\frac1P$ bits. Kac's lemma makes this exact on average, with no model needed.

**Optimality claim.** The author concludes that the result shows the LZ algorithm has asymptotically optimal compression rate for every stationary ergodic process (p. 264); Theorem 13.5 itself concerns a pointer code with the past known to the decoder.

**Individual-sequence guarantees.** KT is at most $O(\frac{\log n}{n})$ per letter worse than the best static arithmetic coder (Section 13.7). LZ is also special here: in [331] (see [160, Thm 4]) its rate on every input is shown to be better than that of any finite-state machine (FSM) up to $O(\frac{\log\log n}{\log n})$. Consequently, investing via LZ achieves capital growth competitive with any FSM investor [160]. So LZ enjoys certain optimality guarantees in both the stochastic and individual-sequence senses (p. 264).

### Exercises for Part II (pp. 265–272)
The pages include Exercises II.1–II.22 of Part II; those relevant to this chapter are II.13–II.22 (pp. 268–272). Solutions are not printed here.

## Toy example (ours; not from the text)
Encode $x^3=011$ over $\{0,1\}$ with KT add-½ and arithmetic coding (order $0<1$).

Sequential probabilities, using (13.28)–(13.29) (counts over previous symbols, denominator $n$):
- $n=1$: $Q(0)=\frac{0+1/2}{1}=\frac12$.
- $n=2$, after "0": $Q(1|0)=\frac{0+1/2}{2}=\frac14$, $Q(0|0)=\frac{1+1/2}2=\frac34$.
- $n=3$, after "01" ($t_0=t_1=1$): $Q(1|01)=\frac{1+1/2}{3}=\frac12$.

Product: $\frac12\cdot\frac14\cdot\frac12=\frac1{16}$. Check with (13.27): $t_0=1,t_1=2$, $(2\cdot1-1)!!=1$, $(2\cdot2-1)!!=3\cdot1=3$, $2^3\cdot3!=48$, so $3/48=\frac1{16}$ ✓.

Intervals: $[0,1)\to$ symbol 0 gets $[0,\frac12)$. Split $[0,\frac12)$ with $Q(0|0)=\frac34$: $0\to[0,\frac38)$, $1\to[\frac38,\frac12)$. Split $[\frac38,\frac12)$ (width $\frac18$) with $\frac12,\frac12$: $0\to[\frac38,\frac7{16})$, $1\to[\frac7{16},\frac12)=[\frac7{16},\frac8{16})$.

This final interval has width $\frac1{16}$ and is itself dyadic ($m=7,k=4$), so the codeword is the 4-bit expansion of $7/16$: **0111**. Length $4=\log_2 16$, matching (13.2).

Regret against the oracle: $nH(\hat P)=3h(2/3)\approx3(0.9183)=2.755$ bits, so the pointwise regret is $4-2.755\approx1.245$ bits. For comparison, Laplace (13.30) gives $Q=\frac1{\binom32\cdot4}=\frac1{12}$, i.e. $\log_2 12\approx3.585$ bits.

## Concepts
- [[universal-coding]] — one code (equivalently one $Q_{X^n}$) that performs nearly as well as the best code in a class, without knowing the true source (p. 244)
- [[universal-probability-assignment]] (new) — choosing $Q_{X^n}$ for a class; code length is $\log\frac1Q\pm$ constant (p. 245)
- [[huffman-arithmetic-coding]] — arithmetic coding: sequential encoding of $x^n$ as the largest dyadic interval inside its $Q$-interval, length at most $\lceil\log\frac1Q\rceil+1$ (pp. 245–246)
- [[minimax-redundancy]] (new) — $\mathcal R_n^*=\min_Q\sup_\theta D(P_{X^n|\theta}\|Q)$ (p. 248)
- [[capacity-redundancy-theorem]] (new) — $\mathcal R_n^*=\sup_\pi I(\theta;X^n)$, the capacity of the channel $\theta\to X^n$ (p. 248)
- [[normalized-maximum-likelihood]] — Shtarkov distribution $\propto\sup_\theta P(x^n|\theta)$; minimizes worst-case pointwise redundancy (p. 249)
- [[jeffreys-prior]] (new) — prior $\propto\sqrt{\det J_F}$; asymptotically maximin for smooth families and reparametrization-invariant (pp. 252–253)
- [[krichevsky-trofimov]] (new) — add-½ sequential rule, the Jeffreys mixture for i.i.d. classes (p. 254)
- [[individual-sequence-regret]] (new) — loss minus that of the best static predictor for the actual $x^n$; no stochastic assumption (p. 260)
- [[online-to-batch]] (new) — (13.36): batch regret bounded by average cumulative regret divided by $n$, for i.i.d. models (p. 258)
- [[lempel-ziv]] (new) — compressor that codes pointers to previous occurrences; model-free, reaches entropy rate (pp. 261–264)
- [[kac-lemma]] (new) — mean recurrence time of a symbol equals $1/$its probability (p. 262)
- [[fisher-information]] — Hessian of KL; enters via $\sqrt{\det J_F}$ and $\frac1{\log e}J_F$ (p. 251)
- [[mutual-information]], [[channel-capacity]], [[relative-entropy]], [[entropy-rate]], [[redundancy]] — used with the meanings of the canon list (pp. 248, 251, 263)

## Canonical instances
- [[bernoulli-class-redundancy]] — Bernoulli class: $\mathcal R_n^*=\frac12\log n+O(1)$, KT and Laplace rules (pp. 252–254)
- [[laplace-sunrise-problem]] — Laplace's uniform prior versus Jeffreys' invariance (p. 253)
- [[transformer-text-compression]] — leaderboard compressors that train a transformer online (p. 245)
- [[llm-log-loss-training]] — LLM training as the feature-less prediction task (p. 257)
- [[fsm-investor-competitiveness]] — LZ-based investing vs finite-state-machine investors (p. 264)

## Bridges (candidates)
- [same-math] $\mathcal R_n^*=\sup_\pi I(\theta;X^n)$ ↔ channel capacity: the "channel" is $\theta\to X^n$ — Theorem 5.9's minimax = maximin.
- [same-math] Jeffreys mixture / KT ↔ Bayesian statistics: sequential predictive posterior mean with Dirichlet(½) prior.
- [structural-analogy] Online-to-batch (13.36) ↔ statistical learning: cumulative regret controls test error via averaging.
- [structural-analogy] Individual-sequence regret ↔ adversarial online learning / no-regret algorithms: competing with the best static predictor in hindsight.
- [same-math] Log-loss on next-token prediction ↔ LLM cross-entropy training: the text states they solve the same task.
- [structural-analogy] Lempel–Ziv recurrence-time coding ↔ Kac's lemma in ergodic theory.

## Questions this raises
- The text says the Jeffreys mixture $Q^{(KT)}$ is not asymptotically minimax, yet patching the prior near the simplex boundary fixes this. Why exactly does the patching help?
- Can the "$\frac34\log k_n$" universality conjecture (p. 248) be tested for other parametric families?
- Since optimal batch estimators differ from KT, what do optimal batch estimators look like for $k$-symbol i.i.d. laws?
- How fast does LZ's redundancy decay for Markov sources compared with KT-type rules (the text says it is "not easy to derive")?

## Exercises worth doing
- Ex. II.13 (p. 268) — arithmetic coding: sequential computation of $F_n$, prefix property, decoding, encode "etoo", the $nH+2$ bound — difficulty: medium
- Ex. II.14 (p. 268) — enumerative codes: why a natural universal code loses $\log n$ instead of $\frac12\log n$ — difficulty: medium
- Ex. II.15 (p. 269) — KT pointwise bound $\le nh(\cdot)+\frac12\log n+2$, which proves the upper bound of (13.24) for $d=1$ — difficulty: medium
- Ex. II.16 (p. 269) — redundancy lower bound via $I(\theta;\hat\theta)$ with a uniform and a Beta(½) prior — difficulty: hard
- Ex. II.18 (p. 270) — Elias $\gamma$/$\delta$ integer codes, underlying (13.39) — difficulty: medium
- Ex. II.21 (p. 271) — an example where $\mathcal R_n^*<\infty$ but $\mathcal R_n^{**}=\infty$ — difficulty: hard

## Reading notes
- Printed chapter number is 13 (file id says ch15); printed pages 244–272 correspond to pdf 269–297 (printed = pdf − 25). Pages 265–272 are "Exercises for Part II", containing exercises from earlier chapters too (II.1–II.12 not digested).
- (13.18), as printed, shows $f(\hat\theta)-\frac12t^T\mathrm{Hess}f\,t$ in the exponent. For a minimum the Taylor term should carry a plus sign, so this is probably a sign misprint. The scaling in (13.19)–(13.20) is consistent with a plus.
- The KT-not-minimax inequality (p. 252) is printed "for some $c_1>c_2>0$" with lower bound $\mathcal R_n^*+c_1$ and upper bound $\mathcal R_n^*+c_2$. That would be contradictory; presumably $c_2>c_1>0$ is intended. I reproduced the printed statement.
- The step turning (13.21) into (13.22) via Lemma 13.2 is summarized in the source in one sentence. The (added step) in L3 spells it out.
- Page 254 says (13.24) "was not shown rigorously"; the exercise II.15 gives the independent proof of the upper bound.
- The class formula on p. 250 is printed $\exp\{-n\sum_a\theta_a\log\frac1{\hat P_{x^n}(a)}\}$. Since $\prod_j\theta_{x_j}=\exp\{-n\sum_a\hat P_{x^n}(a)\log\frac1{\theta_a}\}$, the roles of $\theta$ and $\hat P$ look swapped, so this is probably a misprint. I reproduced the printed form.
- Typos: "We know encode" (p. 263, "now"); "Jeffrey's prior" (p. 253). Text-layer extraction of equations was garbled in places; all equations were checked against the images.
