---
id: tishby-2000-bottleneck/main
work: tishby-2000-bottleneck
unit: paper
pages: 1-16
fields: [information-theory]
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
# The information bottleneck method

## L0 — One line
Compress a signal X into a short code X̃ that keeps as much information as possible about a second variable Y; the "distortion" then comes out of the joint statistics, as a KL divergence.

## L1 — The gist (≤ 120 words)
Rate distortion theory needs a distortion function chosen in advance, and that choice fixes which features of X count as relevant. The authors instead pick a relevance variable Y. They minimise $I(\tilde X;X)-\beta I(\tilde X;Y)$ over stochastic encoders $p(\tilde x|x)$ (random maps from x to codewords x̃). This gives exact self-consistent equations in which the effective distortion is $D_{KL}[p(y|x)\|p(y|\tilde x)]$, which is not assumed beforehand. A Blahut–Arimoto-style alternating iteration (the known way to compute rate distortion solutions) solves them. It converges, but the convergence proof does not show that the solution is unique. Varying β traces curves in an "information plane" (the plane of $I(X;\tilde X)$ against $I(\tilde X;Y)$), with phase-transition-like bifurcations.

**Prerequisites:** mutual information; KL divergence; Lagrange multipliers and functional derivatives; Markov chains; basic rate distortion idea.

## L2 — Key ideas (5–10 bullets)
- Shannon left "relevance" out of information theory. The authors argue that lossy compression gives a quantitative handle on it (p. 2).
- Rate distortion theory needs a distortion function d(x, x̃), which amounts to an arbitrary feature selection (pp. 2–3). Its solution is an exponential (Gibbs) form, computed by alternating iteration (pp. 5–8).
- Relevance is defined through a second variable Y with $I(X;Y)>0$. The joint p(x,y) is assumed known (p. 8).
- The bottleneck functional is $\mathcal L=I(\tilde X;X)-\beta I(\tilde X;Y)$. β sets the compression/information tradeoff (p. 9).
- The exact formal solution has the rate-distortion form, with $d(x,\tilde x)=D_{KL}[p(y|x)\|p(y|\tilde x)]$ (pp. 10–12).
- The equations are "formal": $p(y|\tilde x)$ depends implicitly on the encoder. They also optimise the representatives, which rate distortion theory treats separately (pp. 10, 12).
- Three alternating updates minimise one free-energy functional. This proves convergence, but not uniqueness (pp. 13–14).
- Solutions form convex curves in the $(I_X,I_Y)$ plane with slope $\beta^{-1}$ and bifurcate at critical β. This yields a hierarchy of quantizations (p. 15).

## L3 — Walkthrough

**Abstract and §1 Introduction (pp. 1–3).** Relevant information in x is the information x gives about y (p. 1).
- Shannon deliberately ignored the value of information to the recipient. The authors argue that lossy source compression gives a natural approach to "relevant information" (p. 2).
- Speech example: a transcript has much lower entropy than the waveform. So one can compress much further without losing information about the words (p. 2).
- Rate distortion theory trades rate R against expected distortion D, via R(D). Its main problem is that d must be specified first. An arbitrary d "is in fact an arbitrary feature selection" (pp. 2–3).
- The proposed fix: in many cases an additional variable determines relevance (transcription, speaker identity, structure, neural responses). All these cases share one structure: extract the information in one variable that is relevant for predicting another (p. 3).

**§2 Relevant quantization (p. 4).** Spaces are finite. A possibly stochastic map $p(\tilde x|x)$ gives a soft partition of X.
$$p(\tilde x)=\sum_x p(x)p(\tilde x|x)\tag{1}$$
- The average volume of the elements of X mapped to one codeword is $2^{H(X|\tilde X)}$ (p. 4), with
$$H(X|\tilde X)=-\sum_{x}p(x)\sum_{\tilde x}p(\tilde x|x)\log p(\tilde x|x)\tag{2}$$
- The rate (average bits per message to specify a codeword) is bounded below by
$$I(X;\tilde X)=\sum_{x,\tilde x}p(x,\tilde x)\log\frac{p(\tilde x|x)}{p(\tilde x)}\tag{3}$$
- Reason: the average number of blocks is $2^{H(X)}/2^{H(X|\tilde X)}=2^{I(X;\tilde X)}$, "via the standard asymptotic arguments". This differs from $H(\tilde X)$, which is normally not what we want to minimise (p. 4).
- Rate alone is not enough, since it can always be lowered by discarding detail (p. 5).

**§2.1 Rate distortion (pp. 5–6).** A distortion function $d:X\times\tilde X\to\mathbb R^+$ is presumed small for good representations (p. 5). Rate and expected distortion trade off monotonically: the larger the rate, the smaller the achievable distortion (p. 5).
$$\langle d(x,\tilde x)\rangle_{p(x,\tilde x)}=\sum_{x,\tilde x}p(x,\tilde x)d(x,\tilde x)\tag{4}$$
$$R(D)\equiv\min_{\{p(\tilde x|x):\langle d\rangle\le D\}}I(X;\tilde X)\tag{5}$$
- Introduce a Lagrange multiplier β and minimise over normalised $p(\tilde x|x)$:
$$\mathcal F[p(\tilde x|x)]=I(X;\tilde X)+\beta\langle d(x,\tilde x)\rangle_{p(x,\tilde x)}\tag{6}$$

**Theorem 1 (p. 6).** The solution of $\delta\mathcal F/\delta p(\tilde x|x)=0$ is
$$p(\tilde x|x)=\frac{p(\tilde x)}{Z(x,\beta)}\exp[-\beta d(x,\tilde x)]\tag{8}$$
with Z a partition function. The multiplier β is positive and $\delta R/\delta D=-\beta$ (9).
- Proof: the derivative (using $p(\tilde x)=\sum_{x'}p(x')p(\tilde x|x')$ and normalisation multipliers λ(x)) is
$$\frac{\delta\mathcal F}{\delta p(\tilde x|x)}=p(x)\Big[\log\frac{p(\tilde x|x)}{p(\tilde x)}+1-\frac1{p(\tilde x)}\sum_{x'}p(x')p(\tilde x|x')+\beta d(x,\tilde x)+\frac{\lambda(x)}{p(x)}\Big]\tag{10}$$
- Setting it to zero and writing $\log Z=\lambda(x)/p(x)$ gives (8). Since $\delta\mathcal F=\delta I+\beta\,\delta\langle d\rangle=0$ (11), Eq. (9) follows. Positivity of β follows from concavity of R(D) (cited from Ref. [2]) (p. 6).

*Intuition note:* each x is sent to the codewords with small distortion, with weights $e^{-\beta d}$ times the codeword's overall popularity. Large β makes the choice sharper.

**§2.2 Blahut–Arimoto (pp. 7–8).** Eqs. (8) and (1) must hold together, so one alternates between them.
- **Lemma 2 (Csiszár–Tusnády)**: for fixed $p(x,y)=p(x)p(y|x)$, the q(y) minimising $D_{KL}[p(x,y)\|p(x)q(y)]$ is the marginal $p(y)=\sum_xp(x)p(y|x)$. Hence $I(X;Y)=\min_{q}D_{KL}[p(x,y)\|p(x)q(y)]$. Equivalently, the marginal minimises $\sum_xp(x)D_{KL}[p(y|x)\|q(y)]$. The proof follows from non-negativity of relative entropy (p. 7).
- **Theorem 3**: Eqs. (1) and (8) hold simultaneously at the minimum of
$$F=-\langle\log Z(x,\beta)\rangle_{p(x)}=I(X;\tilde X)+\beta\langle d\rangle\tag{12}$$
minimised independently over the convex sets $\{p(\tilde x)\}$ and $\{p(\tilde x|x)\}$ (p. 7). This corresponds to the alternating iteration
$$\begin{cases}p_{t+1}(\tilde x)=\sum_xp(x)p_t(\tilde x|x)\\ p_t(\tilde x|x)=\frac{p_t(\tilde x)}{Z_t(x,\beta)}\exp(-\beta d(x,\tilde x))\end{cases}\tag{13}$$
- The iterations converge to a unique minimum (proof deferred to Refs. [2, 4]) (p. 8).
- BA optimises only the partition given the representatives, not the representatives themselves. Choosing them jointly is similar to EM and has no unique solution in general (p. 8).

**§3 Relevance through another variable (p. 8).** Y must not be independent of X: $I(X;Y)>0$. The joint p(x,y) is assumed available (p. 8).

**§3.1 New variational principle (p. 9).**
$$I(\tilde X;Y)=\sum_{y,\tilde x}p(y,\tilde x)\log\frac{p(y,\tilde x)}{p(y)p(\tilde x)}\le I(X;Y)\tag{14}$$
- Compression cannot convey more information than the original data (p. 9). Seek the assignment that keeps a fixed amount of information about Y while minimising bits from X. Footnote 2 says it is equivalent to maximise information about Y at fixed compression.
$$\mathcal L[p(\tilde x|x)]=I(\tilde X;X)-\beta I(\tilde X;Y)\tag{15}$$
- At β = 0 everything maps to one point. As β → ∞ the quantization becomes arbitrarily detailed. In special cases with sufficient statistics, almost all meaningful information can be kept at finite β with significant compression (stated, citing other work) (p. 9).

*Intuition note:* β is the price of keeping information about Y. Low β compresses hard. High β keeps detail.

**§3.2 Self-consistent equations (pp. 10–12).** The constraint is nonlinear in $p(\tilde x|x)$, so the problem is much harder than rate distortion. It still has an exact formal solution.

**Theorem 4 (p. 10).** The optimal assignment satisfies
$$p(\tilde x|x)=\frac{p(\tilde x)}{Z(x,\beta)}\exp\Big[-\beta\sum_yp(y|x)\log\frac{p(y|x)}{p(y|\tilde x)}\Big]\tag{16}$$
$$p(y|\tilde x)=\frac1{p(\tilde x)}\sum_xp(y|x)p(\tilde x|x)p(x)\tag{17}$$
- Eq. (17) follows from Bayes' rule and the Markov chain $\tilde X\leftarrow X\leftarrow Y$. The solution is formal, because $p(y|\tilde x)$ depends implicitly on the encoder. Eq. (1) must also hold (p. 10).
- Footnote 3: the Markov condition is not a modelling assumption. X̃ is not a hidden variable of a data model, where the chain would be $Y\leftarrow\tilde X\leftarrow X$ (p. 10).
- Proof. The chain gives
$$p(y|\tilde x)=\sum_xp(y|x)p(x|\tilde x)\tag{18}$$
$$p(\tilde x)=\sum_xp(\tilde x|x)p(x)\tag{19}$$
$$p(\tilde x|y)=\sum_xp(\tilde x|x)p(x|y)\tag{20}$$
- Hence $\delta p(\tilde x)/\delta p(\tilde x|x)=p(x)$ (21) and $\delta p(\tilde x|y)/\delta p(\tilde x|x)=p(x|y)$ (22) (pp. 10–11).
- With multipliers β and λ(x):
$$\mathcal L=I(X,\tilde X)-\beta I(\tilde X,Y)-\sum_{x,\tilde x}\lambda(x)p(\tilde x|x)\tag{23}$$
$$=\sum_{x,\tilde x}p(\tilde x|x)p(x)\log\frac{p(\tilde x|x)}{p(\tilde x)}-\beta\sum_{\tilde x,y}p(\tilde x,y)\log\frac{p(\tilde x|y)}{p(\tilde x)}-\sum_{x,\tilde x}\lambda(x)p(\tilde x|x)\tag{24}$$
- The derivative is
$$\frac{\delta\mathcal L}{\delta p(\tilde x|x)}=p(x)[1+\log p(\tilde x|x)]-\frac{\delta p(\tilde x)}{\delta p(\tilde x|x)}[1+\log p(\tilde x)]-\beta\sum_y\frac{\delta p(\tilde x|y)}{\delta p(\tilde x|x)}p(y)[1+\log p(\tilde x|y)]-\beta\frac{\delta p(\tilde x)}{\delta p(\tilde x|x)}[1+\log p(\tilde x)]-\lambda(x)\tag{25}$$
- Substituting (21) and (22) and rearranging:
$$\frac{\delta\mathcal L}{\delta p(\tilde x|x)}=p(x)\Big\{\log\frac{p(\tilde x|x)}{p(\tilde x)}-\beta\sum_yp(y|x)\log\frac{p(y|\tilde x)}{p(y)}-\frac{\lambda(x)}{p(x)}\Big\}\tag{26}$$
- $\sum_yp(y|x)\log\frac{p(y|x)}{p(y)}=I(x,Y)$ depends on x only, so it can be absorbed into a redefined multiplier $\tilde\lambda(x)$ (see Reading notes). Then
$$\frac{\delta\mathcal L}{\delta p(\tilde x|x)}=p(x)\Big[\log\frac{p(\tilde x|x)}{p(\tilde x)}+\beta\sum_yp(y|x)\log\frac{p(y|x)}{p(y|\tilde x)}-\tilde\lambda(x)\Big]=0\tag{27}$$
$$p(\tilde x|x)=\frac{p(\tilde x)}{Z(x,\beta)}\exp(-\beta D_{KL}[p(y|x)\|p(y|\tilde x)])\tag{28}$$
with $Z(x,\beta)=\sum_{\tilde x}p(\tilde x)\exp(-\beta D_{KL}[\cdot])$ (p. 12).
- Comment 1: $D_{KL}[p(y|x)\|p(y|\tilde x)]$ emerged as the effective distortion and is not assumed anywhere. The authors find it natural to treat it as the "correct" distortion for the bottleneck setting (p. 12).
- Comment 2: Eqs. (28), (18), (19) determine $p(\tilde x|x)$ and $p(\tilde x)$ self-consistently. They include the optimisation over representatives, unlike rate distortion theory (p. 12).

*Intuition note:* x is preferentially sent (stochastically) to clusters x̃ whose predicted distribution over y is close to x's own, in KL terms. The cluster's predictive distribution is itself re-computed from its members.

**§3.3 Algorithm (pp. 13–14).**

**Theorem 5 (p. 13).** Eqs. (18), (19), (28) hold simultaneously at the minima of
$$F[p(\tilde x|x);p(\tilde x);p(y|\tilde x)]=-\langle\log Z\rangle_{p(x)}\tag{29}$$
$$=I(X;\tilde X)+\beta\langle D_{KL}[p(y|x)\|p(y|\tilde x)]\rangle_{p(x,\tilde x)}\tag{30}$$
minimised independently over the three convex sets. The alternating iteration is
$$\begin{cases}p_t(\tilde x|x)=\frac{p_t(\tilde x)}{Z_t(x,\beta)}\exp(-\beta d(x,\tilde x))\\ p_{t+1}(\tilde x)=\sum_xp(x)p_t(\tilde x|x)\\ p_{t+1}(y|\tilde x)=\sum_yp(y|x)p_t(x|\tilde x)\end{cases}\tag{31}$$
with $d=D_{KL}[p(y|x)\|p(y|\tilde x)]$ (p. 13). (As printed, the sum in the last line is written over y. By (18) it should run over x; see Reading notes.)
- Proof outline (the authors say they had no space for more). Lemma 2 applies to $I(X;\tilde X)$ as in BA. Its second form applies to the expected relative entropy, which is minimised over $\{p(y|\tilde x)\}$ with normalisation multipliers λ(x̃):
$$\delta d(x,\tilde x)=\delta\Big(-\sum_yp(y|x)\log p(y|\tilde x)+\lambda(\tilde x)(\textstyle\sum_yp(y|\tilde x)-1)\Big)\tag{32}$$
$$=\sum_y\Big(-\frac{p(y|x)}{p(y|\tilde x)}+\lambda(\tilde x)\Big)\delta p(y|\tilde x)\tag{33}$$
$$\sum_x\sum_y\Big(-\frac{p(y|x)p(x|\tilde x)}{p(y|\tilde x)}+\lambda(\tilde x)\Big)\delta p(y|\tilde x)=0\tag{34}$$
- Since the δp(y|x̃) are independent for each x̃, the paper says this gives Eq. (28) (see Reading notes). It adds that Eq. (28) has the interpretation of a weighted average of the data conditional distributions that contribute to the representative x̃ (p. 14).
- Convergence: each step minimises the same functional, which is bounded below as a sum of two non-negative terms. With $p(y|\tilde x)$ fixed, the problem is rate distortion with a fixed distortion matrix. The third update minimises the expected relative entropy without affecting $I(X;\tilde X)$ (p. 14).
- F is convex in each distribution separately but not in the product space, as with EM. So convergence does not imply uniqueness (p. 14).

**§3.4 Structure of solutions (pp. 14–15).** The cardinality of X̃ must still be specified. For each β and cardinality there are $I_X\equiv I(X,\tilde X)$ and $I_Y\equiv I(\tilde X,Y)$, and
$$\frac{\delta I(\tilde X,Y)}{\delta I(X,\tilde X)}=\beta^{-1}>0\tag{35}$$
- This suggests deterministic annealing. Raising β moves along convex curves in the "information plane" $(I_X,I_Y)$, which start at (0,0) with infinite slope (p. 15).
- Every two curves in the family separate at some finite critical β through a "second order phase transition". These transitions form a hierarchy of quantizations for different cardinalities (cited to Refs. [1, 5, 6]) (p. 15).
- Further work (p. 15): the authors call the principle a unified framework for prediction, filtering and learning. They list applications to word clustering [6] and document classification [5] (cited), and to neural coding and spectral analysis (no citation given).

## Toy example (ours, not from the text)
Let X ∈ {1,2,3,4} be uniform, Y ∈ {0,1}, and $p(y{=}1|x)=0.9,0.9,0.1,0.1$. Then $p(y{=}1)=0.5$.
- $I(X;Y)=1-H(0.9)$, with $H(0.9)=0.9\log_2\tfrac1{0.9}+0.1\log_2\tfrac1{0.1}=0.1368+0.3322=0.469$. So $I(X;Y)=0.531$ bits.
- Option A (identity code): $I(X;\tilde X)=2$ bits, $I(\tilde X;Y)=0.531$. $\mathcal L=2-0.531\beta$.
- Option B (deterministic clusters {1,2}→a, {3,4}→b): $p(\tilde x)=\tfrac12$ each, and $p(y{=}1|a)=0.9$. So $I(\tilde X;Y)=0.531$ again, while $I(X;\tilde X)=H(\tilde X)=1$ bit. $\mathcal L=1-0.531\beta$, which is lower for every β>0.
- Eq. (28) at β = 1 in nats, with $p(\tilde x)=\tfrac12$, for x = 1: $D_{KL}$ to a is 0. $D_{KL}$ to b is $0.9\ln9+0.1\ln\tfrac19=0.8\ln9=1.758$. Unnormalised weights: $0.5\cdot e^0=0.5$ and $0.5e^{-1.758}=0.0862$. So $p(a|1)=0.5/0.5862=0.853$.
- This is one update with the representatives p(y|x̃) held fixed at Option B's values, not a self-consistent fixed point. With them fixed, larger β sharpens p(a|1) towards 1. Here clustering loses no information about Y, so the compression is free.

## Concepts
- [[information-bottleneck]] (new) — compress X to X̃ while maximising $I(\tilde X;Y)$; minimise $I(\tilde X;X)-\beta I(\tilde X;Y)$ (p. 9)
- [[rate-distortion-function]] — R(D), the minimal $I(X;\tilde X)$ under a bound on expected distortion (p. 5)
- [[mutual-information]] — $I(X;\tilde X)$ is the rate bound; $I(\tilde X;Y)$ is the relevant information (pp. 4, 9)
- [[relative-entropy-kl-divergence]] — emerges as the effective distortion $d(x,\tilde x)$ (p. 12)
- [[exponential-family-gibbs-distribution]] — form $p(\tilde x|x)\propto p(\tilde x)e^{-\beta d}$ of the optimal encoder (p. 6)
- [[blahut-arimoto-algorithm]] (new) — alternating iteration of (1) and (8) for R(D) (p. 8)
- [[deterministic-annealing]] (new) — raising β to move along information-plane curves (p. 15)
- [[information-plane]] (new) — the $(I_X,I_Y)$ plane in which solution curves live (p. 15)

## Canonical instances
- [[speech-compression-example]] — transcript vs waveform entropy shows relevance changes achievable compression (p. 2)
- [[relevance-variable-examples]] — transcription, speaker identity, part-of-speech labels, protein structures, stimulus–response pairs (p. 3)

## Bridges (candidates)
- [structural-analogy] Information bottleneck ↔ statistical inference: sufficient statistics — the paper says that in cases with sufficient statistics, almost all information can be kept at finite β (p. 9)
- [structural-analogy] BA / IB alternating iteration ↔ EM algorithm — the paper compares the non-uniqueness and convexity structure with EM (p. 14)
- [structural-analogy] Free energy F and annealing in β ↔ statistical physics: partition function, phase transitions (pp. 13, 15)
- [structural-analogy] Rate distortion with chosen d ↔ IB with data-derived d — the same exponential-form solution with a different distortion (pp. 6, 12)

## Questions this raises
- How should β and the cardinality of X̃ be chosen in practice, given non-unique solutions?
- How can p(x,y) be estimated well from finite samples? The authors call this beyond their scope (p. 8).
- What exactly happens at the critical β where curves bifurcate?
- When are there sufficient statistics, so that nearly all relevant information survives strong compression?

## Reading notes
- Printed page = pdf page (offset 0). The arXiv header shows "30 September 1999", with arXiv stamp 24 Apr 2000. The text is short and complete.
- The paper cites [1] "in preparation" for several of its larger claims. Those claims are reported here only as the authors' statements.
- Misprints (the images match the text layer). "Blauht–Arimoto" (p. 8). In the text after Eq. (31), $Z_t(\beta,\tilde x)$ appears where $Z_t(x,\beta)$ is meant (Eq. (31) itself prints $Z_t(x,\beta)$).
- Eq. (31), third line: the sum is written $\sum_y$ but, by Eq. (18), should run over x.
- My own check, not in the source: from (26) the absorbed term gives $\tilde\lambda=\lambda/p(x)+\beta I(x,Y)$. The printed definition has $-\beta$. Also, from (27), $Z=\exp(-\tilde\lambda)$. The page prints $Z=\exp[\beta\tilde\lambda(x)]$. The final result (28) is unaffected.
- On p. 14, after Eq. (34), the page says this "gives Eq. (28)" and that "Equation (28)" is a weighted average. My own reading, not in the source: the content of (34) is the weighted-average form of (18).
- The paper does not state the Y–X̃ data-processing property by name. Eq. (14) is stated as "obvious".
