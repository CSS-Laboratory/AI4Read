---
id: murphy-2023-pml2/ch05-information-p2
work: murphy-2023-pml2
unit: "Chapter 5 — Information theory (part 2/2: end of §5.2, then §§5.3–5.7)"
pages: 238–259
fields: [bayesian]
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
# Information theory, part 2: mutual information, compression, bottlenecks, algorithmic information

## L0 — One line
Mutual information is the KL divergence between a joint distribution and the product of its marginals; it measures dependence and appears in variational bounds, rate–distortion and bits-back compression, and bottleneck objectives; the part ends with Kolmogorov complexity, an alternative notion of information for individual sequences.

## L1 — The gist (≤ 120 words)
This part of Chapter 5 asks how to measure dependence between variables and what information theory says about learning and compression. Mutual information (MI) is the KL divergence between a joint distribution and the product of its marginals. It obeys the data processing inequality, gives a definition of sufficient statistics, has multivariate versions, and can be bounded variationally. The part then covers rate–distortion and bits-back for compression, parity codes for noisy channels, and the information bottleneck (VIB, CEB). It ends with Kolmogorov complexity and Solomonoff induction, which treat individual sequences. It matters because several ML objectives (VAE, VIB, InfoNCE) are built from information-theoretic quantities.

**Prerequisites:** entropy, cross entropy and KL divergence; conditional entropy; Markov chains and conditional independence; expectations; Bayesian mixtures; basic directed graphical models. Names used above and defined in L3: VAE (variational autoencoder objective); BA, NWJ/DV and InfoNCE (named lower bounds on MI); VIB and CEB (variational and conditional entropy bottleneck); rate–distortion (trade-off between code size and reconstruction error); bits-back (an argument about the true cost of the code); Kolmogorov complexity (length of the shortest program that outputs a string).

## L2 — Key ideas
- MI $\mathbb I(X;Y)=D_{KL}(p(x,y)\|p(x)p(y))\ge 0$, zero iff $X,Y$ are independent. It equals the reduction in entropy of one variable after observing the other (p. 239).
- Data processing inequality: if $X\to Y\to Z$ is a Markov chain, $\mathbb I(X;Y)\ge\mathbb I(X;Z)$. Equality in $\mathbb I(\theta;s(X))\le\mathbb I(\theta;X)$ defines a sufficient statistic (pp. 239–240).
- Two generalisations of MI to many variables are discussed: total correlation (non-negative) and co-information (can be positive or negative). Its sign separates redundancy from synergy and relates to fork, collider and chain structures (pp. 241–243).
- When the joint is intractable, MI can be bounded variationally: an upper bound, and the BA, NWJ/DV and InfoNCE lower bounds. InfoNCE is capped at $\log K$ (pp. 244–246).
- Compression: the source coding theorem sets the entropy as the minimum expected bits. Lossy coding trades rate against distortion, and $\beta=1$ gives the VAE objective. Bits-back coding explains why the rate is a KL term (pp. 247–250).
- Information bottleneck: maximise $\mathbb I(z;y)$ while minimising $\mathbb I(z;x)$. VIB makes this tractable with variational bounds; CEB uses $\mathbb I(x;z|y)$ instead (pp. 252–256).
- Algorithmic information theory defines information of an individual string by Kolmogorov complexity (uncomputable). Solomonoff induction uses it as a universal prior with a total-error bound $K(\mu)\ln 2$ (pp. 256–258).

## L3 — Walkthrough

### 5.2 (end): empirical cross entropy and perplexity (p. 238)
Approximate the true distribution by the empirical distribution of $N$ samples from $p$:
$$p_{\mathcal D}(x|\mathcal D)=\frac1N\sum_{n=1}^N \mathbb I(x=x_n)\tag{5.105}$$
The cross entropy is then
$$H=-\frac1N\sum_{n=1}^N\log p(x_n)=-\frac1N\log\prod_{n=1}^N p(x_n)\tag{5.106}$$
and the perplexity (2 raised to the cross entropy) is
$$\text{perplexity}(p_{\mathcal D},p)=2^{-\frac1N\log(\prod_n p(x_n))}=2^{\log(\prod_n p(x_n))^{-1/N}}\tag{5.107}$$
$$=\Big(\prod_{n=1}^N p(x_n)\Big)^{-1/N}=\sqrt[N]{\prod_{n=1}^N\frac1{p(x_n)}}\tag{5.108}$$
The **branching factor** of a language model is the number of words that can follow a given word. If $p(x_n|x_{n-1})=1/K$ for all contexts, the perplexity is $((1/K)^N)^{-1/N}=K$. If the model correctly reflects that some symbols are more likely, the perplexity is lower than $K$. Since $\mathbb H(p^*)\le\mathbb H_{ce}(p^*,p)$, the perplexity cannot be pushed below a floor set by the true entropy (p. 238; see Reading notes on the printed exponent).

### 5.3 Mutual information
**5.3.1 Definition.** MI measures dependence by comparing the joint with the product of marginals (p. 238):
$$\mathbb I(X;Y)\triangleq D_{KL}(p(x,y)\|p(x)p(y))=\sum_{y}\sum_{x}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{5.109}$$
$X$ or $Y$ may be sets of variables (e.g. $\mathbb I(X;Y,Z)$); for continuous variables sums become integrals (p. 238). MI is non-negative even for continuous variables, with equality iff $p(x,y)=p(x)p(y)$ (p. 239):
$$\mathbb I(X;Y)=D_{KL}(p(x,y)\|p(x)p(y))\ge0\tag{5.110}$$

**5.3.2 Interpretation.** MI is the information gain from updating a model that treats the variables as independent, $p(x)p(y)$, to one with the true joint (p. 239). In entropy terms:
$$\mathbb I(X;Y)=\mathbb H(X)-\mathbb H(X|Y)=\mathbb H(Y)-\mathbb H(Y|X)\tag{5.111}$$
So MI is the reduction in uncertainty about $X$ after observing $Y$, and vice versa. Since $0\le\mathbb I(X;Y)$, this gives $\mathbb H(X|Y)\le\mathbb H(X)$ (conditioning on average reduces entropy) (p. 239). The author also states, without derivation:
$$\mathbb I(X;Y)=\mathbb H(X,Y)-\mathbb H(X|Y)-\mathbb H(Y|X)\tag{5.112}$$
$$\mathbb I(X;Y)=\mathbb H(X)+\mathbb H(Y)-\mathbb H(X,Y)\tag{5.113}$$
Figure 5.6 shows these as information diagrams (a signed measure mapping set expressions to information quantities) (pp. 239–240).

*Intuition note.* MI is "how much knowing one variable shrinks your uncertainty about the other". It is zero exactly when the variables carry no information about each other.

**5.3.3 Data processing inequality (DPI).** Processing a noisy observation cannot add information about the unknown (p. 239).

**Theorem 5.3.1.** If $X\to Y\to Z$ is a Markov chain ($X\perp Z|Y$), then $\mathbb I(X;Y)\ge\mathbb I(X;Z)$.

*Proof* (p. 239). By the chain rule for MI:
$$\mathbb I(X;Y,Z)=\mathbb I(X;Z)+\mathbb I(X;Y|Z)\tag{5.114}$$
$$=\mathbb I(X;Y)+\mathbb I(X;Z|Y)\tag{5.115}$$
Because $X\perp Z|Y$, $\mathbb I(X;Z|Y)=0$, so
$$\mathbb I(X;Z)+\mathbb I(X;Y|Z)=\mathbb I(X;Y)\tag{5.116}$$
and $\mathbb I(X;Y|Z)\ge0$ gives the result. Similarly $\mathbb I(Y;Z)\ge\mathbb I(X;Z)$. ∎

**5.3.4 Sufficient statistics.** For the chain $\theta\to X\to s(X)$ the DPI gives (p. 240)
$$\mathbb I(\theta;s(X))\le\mathbb I(\theta;X)\tag{5.117}$$
If equality holds, $s(X)$ is a **sufficient statistic** of $X$ for inferring $\theta$. Then one can equivalently write $\theta\to s(X)\to X$. The data itself is sufficient but does not summarise anything. A **minimal sufficient statistic** is sufficient and satisfies $s(X)=f(s'(X))$ for some $f$ and all sufficient $s'$, giving
$$\theta\to s(X)\to s'(X)\to X\tag{5.118}$$
Examples: for $N$ Bernoulli trials, $N$ and $N_1=\sum_n\mathbb I(X_n=1)$ form a minimal sufficient statistic, so the order of heads and tails is not needed (pp. 240–241). To infer a Gaussian mean with known variance, the empirical mean and sample count suffice (p. 241). The author recalls the exponential family (§5.1.8, earlier in this chapter) and says it makes sense that the statistics used to generate exponential-family distributions are sufficient. He also cites the Pitman–Koopman–Darmois theorem: for a distribution with fixed domain, only the exponential family admits sufficient statistics of bounded dimension as the sample size grows (p. 241).

**5.3.5 Multivariate MI** (p. 241).

*5.3.5.1 Total correlation (multi-information).*
$$\mathbb{TC}(\{X_1,\dots,X_D\})\triangleq D_{KL}\Big(p(\boldsymbol x)\Big\|\prod_d p(x_d)\Big)=\sum_{\boldsymbol x}p(\boldsymbol x)\log\frac{p(\boldsymbol x)}{\prod_{d}p(x_d)}=\sum_d\mathbb H(x_d)-\mathbb H(\boldsymbol x)\tag{5.119–5.120}$$
For three variables, $\mathbb{TC}(X,Y,Z)=\mathbb H(X)+\mathbb H(Y)+\mathbb H(Z)-\mathbb H(X,Y,Z)$ (5.121), with $\mathbb H(X,Y,Z)=-\sum_x\sum_y\sum_z p\log p$ (5.122). TC is non-negative and zero iff $p(\boldsymbol x)=\prod_d p(x_d)$. A drawback: it is non-zero even if only a pair interacts. For $p(X,Y,Z)=p(X,Y)p(Z)$ it is non-zero though there is no 3-way interaction (p. 241).

*5.3.5.2 Interaction information (co-information).* An inductive definition uses conditional MI (p. 241):
$$\mathbb I(X_1;\cdots;X_D)=\mathbb I(X_1;\cdots;X_{D-1})-\mathbb I(X_1;\cdots;X_{D-1}|X_D)\tag{5.123}$$
This is the multiple mutual information (MMI), or co-information, and equals the interaction information up to a sign. For three variables (p. 242):
$$\mathbb I(X;Y;Z)=\mathbb I(X;Y)-\mathbb I(X;Y|Z)=\mathbb I(X;Z)-\mathbb I(X;Z|Y)=\mathbb I(Y;Z)-\mathbb I(Y;Z|X)\tag{5.124–5.126}$$
It is the change in MI between a pair when conditioning on the third, and it is symmetric in its arguments. Using $\mathbb I(X;Z|Y)=\mathbb I(Z;X,Y)-\mathbb I(Y;Z)$ (5.127) in (5.125):
$$\mathbb I(X;Y;Z)=\mathbb I(X;Z)+\mathbb I(Y;Z)-\mathbb I(X,Y;Z)\tag{5.128}$$
This is how much we learn about $Z$ from $X$ and $Y$ individually versus jointly. In Figure 5.7, the area of a shaded region including circles $A,B,C,\dots$ and excluding $F,G,H,\dots$ is $\mathbb I(A;B;C;\dots|F,G,H,\dots)$ (p. 242).

*5.3.5.3 Synergy and redundancy.* By (5.128), the MMI can be positive, zero or negative. If part of the information about $Z$ from $X$ is also provided by $Y$, there is **redundancy**: $\mathbb I(X;Z)+\mathbb I(Y;Z)>\mathbb I(X,Y;Z)$, so MMI $>0$. If we learn more about $Z$ from $X,Y$ together, there is **synergy**: the inequality reverses, so MMI $<0$ (p. 242).

*5.3.5.4 MMI and causality.* The sign of MMI can distinguish directed graphical models, which "can sometimes be interpreted causally" (p. 243).
- **Common cause** $X\leftarrow Z\rightarrow Y$ (example: $X$ = raining, $Y$ = sky dark, $Z$ = cloudy). Conditioning on $Z$ makes $X,Y$ independent, so $\mathbb I(X;Y|Z)\le\mathbb I(X;Y)$ and $\mathbb I(X;Y;Z)\ge0$.
- **Common effect** $X\rightarrow Z\leftarrow Y$. Conditioning on $Z$ makes $X,Y$ dependent (explaining away). Example: $X,Y$ independent random bits, $Z=\mathrm{XOR}(X,Y)$; observing $Z=1$ gives $p(X\ne Y|Z=1)=1$. So $\mathbb I(X;Y|Z)\ge\mathbb I(X;Y)$ and $\mathbb I(X;Y;Z)\le0$.
- **Chain** $X\to Y\to Z$: $\mathbb I(X;Z|Y)\le\mathbb I(X;Z)$, so the author says the MMI "must be positive" (p. 243).

*5.3.5.5 MMI and entropy.* With $\mathbb I(X;Y)=\mathbb H(X)+\mathbb H(Y)-\mathbb H(X,Y)$ (5.129) and $\mathbb I(X;Y|Z)=\mathbb H(X,Z)+\mathbb H(Y,Z)-\mathbb H(Z)-\mathbb H(X,Y,Z)$ (5.130), eq. (5.124) becomes
$$\mathbb I(X;Y;Z)=[\mathbb H(X)+\mathbb H(Y)+\mathbb H(Z)]-[\mathbb H(X,Y)+\mathbb H(X,Z)+\mathbb H(Y,Z)]+\mathbb H(X,Y,Z)\tag{5.131}$$
which differs from (5.121). In general (p. 243):
$$\mathbb I(X_1,\dots,X_D)=-\sum_{\mathcal T\subseteq\{1,\dots,D\}}(-1)^{|\mathcal T|}\mathbb H(\mathcal T)\tag{5.132}$$
Sizes 1–3 expand to $I_1=H_1$, $I_{12}=H_1+H_2-H_{12}$, $I_{123}=H_1+H_2+H_3-H_{12}-H_{13}-H_{23}+H_{123}$ (5.133–5.135). Möbius inversion gives the dual $\mathbb H(\mathcal S)=-\sum_{\mathcal T\subseteq\mathcal S}(-1)^{|\mathcal T|}\mathbb I(\mathcal T)$ (5.136) (pp. 243–244). The chain rule for entropy gives $\mathbb I(X;Y;Z)=\mathbb H(Z)-\mathbb H(Z|X)-\mathbb H(Z|Y)+\mathbb H(Z|X,Y)$ (5.137) (p. 244).

*Intuition note.* Total correlation asks "is the whole joint different from independence?" Co-information asks "does the third variable change how much the other two tell each other?". The first is never negative; the second can be negative (synergy, as in XOR).

**5.3.6 Variational bounds on MI** (p. 244). These use approximations to intractable distributions and are useful for representation learning (first suggested in [BA03]).

*5.3.6.1 Upper bound.* Assume we can sample $p(\boldsymbol x)$ and evaluate $p(\boldsymbol y|\boldsymbol x)$, but not the joint. Approximate $p(\boldsymbol y)$ by $q(\boldsymbol y)$:
$$\mathbb I(\boldsymbol x;\boldsymbol y)=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{p(\boldsymbol y|\boldsymbol x)q(\boldsymbol y)}{p(\boldsymbol y)q(\boldsymbol y)}\Big]\tag{5.138}$$
$$=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{p(\boldsymbol y|\boldsymbol x)}{q(\boldsymbol y)}\Big]-D_{KL}(p(\boldsymbol y)\|q(\boldsymbol y))\tag{5.139}$$
$$\le\mathbb E_{p(\boldsymbol x)}\mathbb E_{p(\boldsymbol y|\boldsymbol x)}\Big[\log\frac{p(\boldsymbol y|\boldsymbol x)}{q(\boldsymbol y)}\Big]\tag{5.140}$$
$$=\mathbb E_{p(\boldsymbol x)}[D_{KL}(p(\boldsymbol y|\boldsymbol x)\|q(\boldsymbol y))]\tag{5.141}$$
The bound is tight if $q(\boldsymbol y)=p(\boldsymbol y)$. Reason: $\mathbb I=\mathbb H(Y)-\mathbb H(Y|X)$. We know $p(y|x)$, so $\mathbb H(Y|X)$ is estimated well. A model $q$ cannot beat $p(y)$ (KL non-negativity), so the entropy estimate errs too large (p. 244).

*5.3.6.2 BA lower bound.* Assume we can evaluate $p(\boldsymbol x)$ and approximate $p(\boldsymbol x|\boldsymbol y)$ by $q(\boldsymbol x|\boldsymbol y)$:
$$\mathbb I(\boldsymbol x;\boldsymbol y)=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{p(\boldsymbol x|\boldsymbol y)}{p(\boldsymbol x)}\Big]\tag{5.142}$$
$$=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{q(\boldsymbol x|\boldsymbol y)}{p(\boldsymbol x)}\Big]+\mathbb E_{p(\boldsymbol y)}[D_{KL}(p(\boldsymbol x|\boldsymbol y)\|q(\boldsymbol x|\boldsymbol y))]\tag{5.143}$$
$$\ge\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{q(\boldsymbol x|\boldsymbol y)}{p(\boldsymbol x)}\Big]=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}[\log q(\boldsymbol x|\boldsymbol y)]+h(\boldsymbol x)\tag{5.144}$$
with $h(\boldsymbol x)$ the differential entropy (Barber–Agakov bound) (p. 244).

*5.3.6.3 NWJ lower bound* (p. 245). BA needs a normalised, pointwise-evaluable $q$. Reparameterise
$$q(\boldsymbol x|\boldsymbol y)=\frac{p(\boldsymbol x)e^{f(\boldsymbol x,\boldsymbol y)}}{Z(\boldsymbol y)},\quad Z(\boldsymbol y)=\mathbb E_{p(\boldsymbol x)}[e^{f(\boldsymbol x,\boldsymbol y)}]\tag{5.145}$$
Plugging into BA:
$$\mathbb E_{p(\boldsymbol x,\boldsymbol y)}\Big[\log\frac{p(\boldsymbol x)e^{f}}{p(\boldsymbol x)Z(\boldsymbol y)}\Big]=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}[f]-\mathbb E_{p(\boldsymbol y)}[\log Z(\boldsymbol y)]\tag{5.146}$$
$$=\mathbb E_{p(\boldsymbol x,\boldsymbol y)}[f]-\mathbb E_{p(\boldsymbol y)}\big[\log\mathbb E_{p(\boldsymbol x)}[e^{f}]\big]\triangleq I_{DV}(X;Y)\tag{5.147–5.148}$$
This is the Donsker–Varadhan bound. Using the line bound $\log x\le x/a+\log a-1$ (5.149) with $a=e$ (added step: then $\log a-1=0$, so $\log x\le x/e$, applied with $x=Z(\boldsymbol y)$):
$$\mathbb I(X;Y)\ge\mathbb E_{p(\boldsymbol x,\boldsymbol y)}[f(\boldsymbol x,\boldsymbol y)]-e^{-1}\mathbb E_{p(\boldsymbol y)}Z(\boldsymbol y)\triangleq I_{NWJ}(X;Y)\tag{5.150}$$
Also called f-GAN KL or MINE-f.

*5.3.6.4 InfoNCE lower bound* (pp. 245–246). A multi-sample extension of DV (derivation in [Poo+19b], not given here), with expectation over $K$ paired samples from $p(X,Y)$:
$$\mathbb I_{NCE}=\mathbb E\Big[\frac1K\sum_{i=1}^K\log\frac{e^{f(\boldsymbol x_i,\boldsymbol y_i)}}{\frac1K\sum_{j=1}^Ke^{f(\boldsymbol x_i,\boldsymbol y_j)}}\Big]\tag{5.151}$$
$$=\log K-\mathbb E\Big[\frac1K\sum_{i=1}^K\log\Big(1+\sum_{j\ne i}^Ke^{f(\boldsymbol x_i,\boldsymbol y_j)-f(\boldsymbol x_i,\boldsymbol y_i)}\Big)\Big]\tag{5.152}$$
The intuition: MI measures how distinguishable jointly drawn pairs are from independently drawn $x$'s and $y$'s, and the bound trains a model to tell them apart. It is a valid lower bound, but since $\mathbb I_{NCE}\le\log K$ a large batch $K$ may be needed when the MI is large (p. 246). A multi-label classifier has been proposed to overcome this (p. 246).

*Intuition note.* We cannot compute MI when the joint is hard. Each bound swaps an unknown distribution for a model and keeps one side of the inequality. The upper bound errs because the model entropy is too large. The BA lower bound drops a non-negative KL term; the NWJ bound further replaces $\log$ by a straight line (5.149); the InfoNCE derivation is not given here.

**5.3.7 Relevance networks** (pp. 246–247). Add an $i-j$ edge if $\mathbb I(X_i;X_j)$ exceeds a threshold. In the Gaussian case $\mathbb I(X_i;X_j)=-\frac12\log(1-\rho_{ij}^2)$, with $\rho_{ij}$ the correlation, and the graph is a covariance graph. They are popular in systems biology; Fig. 5.9 shows one for 20-newsgroups words (Fig. 5.8) with edges at MI $\ge20\%$ of the maximum, and "the results seem intuitively reasonable". Main problem: the graphs are usually very dense. If $X_1\!-\!X_2\!-\!X_3$ is a chain of direct influences, $X_1$ and $X_3$ still have non-zero MI, so a 1–3 edge appears. A probabilistic graphical model represents conditional independence instead ($X_1\perp X_3|X_2$), so it is usually much sparser (Chapter 30) (p. 247).

### 5.4 Data compression (source coding)
Compression is related to probabilistic ML: if we can model data probabilities, we can give short codewords to frequent samples. So compressing well requires finding patterns and their frequencies. Hutter proposes compression as an objective measure of progress to general AI; the Hutter prize offers 50,000 Euros for compressing the first 100MB of English Wikipedia better than a baseline (p. 247).

**5.4.1 Lossless compression** (p. 247). Discrete data can be compressed so the original is uniquely recoverable. **Source coding theorem** (Shannon): the expected number of bits to losslessly encode data from $p$ is at least $\mathbb H(p)$. Since $\mathbb H_{ce}(p,q)\ge\mathbb H(p)$, coding with a model $q\ne p$ costs excess bits, and the number of excess bits is exactly $D_{KL}(p\|q)$. Techniques: Huffman coding, arithmetic coding, asymmetric numeral systems; their input is a probability distribution over strings, often a latent variable model.

**5.4.2 Lossy compression and rate–distortion** (pp. 248–250). Real-valued signals are first quantised (e.g. vector quantisation) and then losslessly coded, which loses information. The unit uses the variational information bottleneck vocabulary (§5.6.2, unsupervised here): stochastic encoder $e(\boldsymbol z|\boldsymbol x)$, decoder $d(\boldsymbol x|\boldsymbol z)$, marginal $m(\boldsymbol z)$. **Distortion**:
$$D=-\int d\boldsymbol x\,p(\boldsymbol x)\int d\boldsymbol z\,e(\boldsymbol z|\boldsymbol x)\log d(\boldsymbol x|\boldsymbol z)\tag{5.153}$$
For a deterministic encoder $e(\boldsymbol z|\boldsymbol x)=\delta(\boldsymbol z-f_e(\boldsymbol x))$ and Gaussian decoder $d(\boldsymbol x|\boldsymbol z)=\mathcal N(\boldsymbol x|f_d(\boldsymbol z),\sigma^2)$:
$$D=\frac1{\sigma^2}\mathbb E_{p(\boldsymbol x)}\big[\|f_d(f_e(\boldsymbol x))-\boldsymbol x\|^2\big]\tag{5.154}$$
the expected reconstruction error. **Rate**:
$$R=\int d\boldsymbol x\,p(\boldsymbol x)\int d\boldsymbol z\,e(\boldsymbol z|\boldsymbol x)\log\frac{e(\boldsymbol z|\boldsymbol x)}{m(\boldsymbol z)}=\mathbb E_{p(\boldsymbol x)}[D_{KL}(e(\boldsymbol z|\boldsymbol x)\|m(\boldsymbol z))]=\int\!\!\int p(\boldsymbol x,\boldsymbol z)\log\frac{p(\boldsymbol x,\boldsymbol z)}{p(\boldsymbol x)m(\boldsymbol z)}\ge\mathbb I(\boldsymbol x,\boldsymbol z)\tag{5.155–5.157}$$
This is the excess bits paid for coding with $m(\boldsymbol z)$ rather than the aggregate posterior $p(\boldsymbol z)=\int d\boldsymbol x\,p(\boldsymbol x)e(\boldsymbol z|\boldsymbol x)$. The trade-off: $e(\boldsymbol z|\boldsymbol x)=\delta(\boldsymbol z-\boldsymbol x)$ gives zero distortion but high rate (no compression). $e=\delta(\boldsymbol z-\mathbf 0)$ gives rate 0 but high distortion. Using the bounds of §5.3.6 (the lower bound is $\mathbb H-D$ with $\mathbb H$ the differential entropy of $\boldsymbol x$):
$$\mathbb H-D\le\mathbb I(\boldsymbol x;\boldsymbol z)\le R,\qquad \mathbb H=-\int d\boldsymbol x\,p(\boldsymbol x)\log p(\boldsymbol x)\tag{5.158–5.159}$$
For discrete data $\mathbb H\ge0$ and $D\ge0$; $R\ge0$ for discrete or continuous $\boldsymbol z$. Figure 5.10 (rate–distortion curve):
- The $D=0$ line has $R\ge\mathbb H$ (source coding theorem). A suboptimal $m(\boldsymbol z)$ raises the rate without changing the distortion.
- The $R=0$ line has $D\ge\mathbb H$; a latent-free model such as an autoregressive one can still learn $p(\boldsymbol x)$.
- The diagonal $D=\mathbb H-R$ needs both bounds tight, i.e. perfect $e,d$ (the "non-parametric limit"). In practice with finite data the curve is shifted up.

Points along the curve come from minimising
$$J=D+\beta R=\int d\boldsymbol x\,p(\boldsymbol x)\int d\boldsymbol z\,e(\boldsymbol z|\boldsymbol x)\Big[-\log d(\boldsymbol x|\boldsymbol z)+\beta\log\frac{e(\boldsymbol z|\boldsymbol x)}{m(\boldsymbol z)}\Big]\tag{5.160}$$
With $\beta=1$, $q=e$, $p(\boldsymbol x|\boldsymbol z)=d$, $p(\boldsymbol z)=m$, this matches the VAE objective (§21.2), since the ELBO is
$$\mathcal L=-(D+R)=\mathbb E_{p(\boldsymbol x)}\Big[\mathbb E_{e}[\log d(\boldsymbol x|\boldsymbol z)]-\mathbb E_{e}\Big[\log\frac{e(\boldsymbol z|\boldsymbol x)}{m(\boldsymbol z)}\Big]\Big]\tag{5.161}$$
i.e. reconstruction term minus $D_{KL}(e\|m)$. With $\beta\ne1$ one gets the β-VAE objective. The β-VAE cannot distinguish solutions on the diagonal, which have the same marginal likelihood (ELBO) but differ radically in whether the latent representation is interesting. So likelihood is not a sufficient metric for comparing unsupervised representation learners (p. 250).

**5.4.3 Bits-back coding** (p. 250). The rate is $R(\boldsymbol x)=\int d\boldsymbol z\,p(\boldsymbol z|\boldsymbol x)\log\frac{p(\boldsymbol z|\boldsymbol x)}{m(\boldsymbol z)}=\mathbb H_{ce}(p(\boldsymbol z|\boldsymbol x),m(\boldsymbol z))-\mathbb H(p(\boldsymbol z|\boldsymbol x))$ (5.162). This charges only the excess bits, not the cross entropy. The argument: Alice sends $\boldsymbol x$ to Bob; both share $p(\boldsymbol z|\boldsymbol x)$, $m(\boldsymbol z)$, $d(\boldsymbol x|\boldsymbol z)$. She samples $\boldsymbol z\sim p(\boldsymbol z|\boldsymbol x)$ and sends it at cost $-\log_2m(\boldsymbol z)$, then sends the residual at cost $-\log_2d(\boldsymbol x|\boldsymbol z)$. The expected total is
$$\mathbb E_{p(\boldsymbol z|\boldsymbol x)}[-\log_2d(\boldsymbol x|\boldsymbol z)-\log_2m(\boldsymbol z)]=D+\mathbb H_{ce}(p(\boldsymbol z|\boldsymbol x),m(\boldsymbol z))\tag{5.163}$$
which is distortion plus cross entropy, not plus rate. The bits come back because Bob, knowing $\boldsymbol z$ and the encoder, can reverse-engineer the random bits Alice used to sample $\boldsymbol z$. (Her entropy source is e.g. a compressed copy of Moby Dick, which Bob recovers.) So the extra randomness in choosing $\boldsymbol z$ carries more information. The author says the argument was originally a thought experiment, and that several practical algorithms now achieve it (p. 250).

*Intuition note.* Rate is a price paid for the information the code carries about $\boldsymbol x$ beyond what $m(\boldsymbol z)$ already predicts. Rate and distortion pull in opposite directions, and $\beta$ picks a point between them.

### 5.5 Error-correcting codes (channel coding) (pp. 251–252)
Add redundancy to a signal so the receiver can recover from noise. Source message $\boldsymbol x\in\{0,1\}^m$ ($m$ = block length) is sent over a noisy channel giving $\boldsymbol y$. Bit-flip channel: $p(\boldsymbol y|\boldsymbol x)=\prod_i p(y_i|x_i)$ with $p(y_i|x_i=0)=[1-\alpha,\alpha]$, $p(y_i|x_i=1)=[\alpha,1-\alpha]$. Alternatively Gaussian noise $\mathcal N(y_i|\mu_b,\sigma^2)$. The receiver computes $\arg\max_{\boldsymbol x}p(\boldsymbol x|\boldsymbol y)$. **Parity check bits** (deterministic functions saying whether the sum of bits is odd or even) add redundancy; this helps because multiple flips are less likely than one.

Example: two message bits plus one parity bit (Fig. 5.11a):
$$p(\boldsymbol x,\boldsymbol y)=p(x_1)p(x_2)p(x_3|x_1,x_2)\prod_{i=1}^3p(y_i|x_i)\tag{5.164}$$
Priors uniform, $p(x_3|x_1,x_2)$ the deterministic parity, $\alpha=0.2$. Observing $\boldsymbol y=(1,0,0)$ violates the parity constraint. The three posterior modes are 000, 110, 101 (one flipped bit each); 011 (three flips) has small non-zero posterior; 001, 010, 100 are inconsistent with the code (Fig. 5.11b). Practical codes add fewer redundant bits but still correct errors (§9.4.8, not covered here).

### 5.6 The information bottleneck
Discriminative models $p(\boldsymbol y|\boldsymbol x)$ with a stochastic bottleneck aim to prevent overfitting and improve robustness and calibration (p. 252).

**5.6.1 Vanilla IB** (p. 252). $\boldsymbol z$ is a *representation* of $\boldsymbol x$ if it is a (possibly stochastic) function of $\boldsymbol x$, described by $p(\boldsymbol z|\boldsymbol x)$. It is *sufficient* for $\boldsymbol y$ if $\boldsymbol y\perp\boldsymbol x|\boldsymbol z$, equivalently $\mathbb I(\boldsymbol z;\boldsymbol y)=\mathbb I(\boldsymbol x;\boldsymbol y)$, i.e. $\mathbb H(\boldsymbol y|\boldsymbol z)=\mathbb H(\boldsymbol y|\boldsymbol x)$. It is a *minimal sufficient statistic* if sufficient and no other $\boldsymbol z$ has smaller $\mathbb I(\boldsymbol z;\boldsymbol x)$. The **information bottleneck principle** optimises over $p(\boldsymbol z|\boldsymbol x)$ and $p(\boldsymbol y|\boldsymbol z)$:
$$\min\ \beta\,\mathbb I(\boldsymbol z;\boldsymbol x)-\mathbb I(\boldsymbol z;\boldsymbol y),\quad\beta\ge0\tag{5.165}$$
$\beta$ is a Lagrange multiplier trading sufficiency against minimality. Assume the graphical model $Z\leftarrow X\leftrightarrow Y$:
$$p(\boldsymbol x,\boldsymbol y,\boldsymbol z)=p(\boldsymbol z|\boldsymbol x)p(\boldsymbol y|\boldsymbol x)p(\boldsymbol x)\tag{5.166}$$
So $Z$ cannot contain information unique to $Y$ (Fig. 5.12a); the optimal $Z$ keeps only the information about $X$ useful for $Y$ (Fig. 5.12b). Exact solution: the algorithm of [TPB99] if all variables are discrete and $\boldsymbol z=e(\boldsymbol x)$ is deterministic; analytically if all are jointly Gaussian (a form of supervised PCA); in general intractable.

**5.6.2 Variational IB (VIB)** (pp. 253–254). Key trick, from KL non-negativity, for any $q$:
$$\int d\boldsymbol x\,p(\boldsymbol x)\log p(\boldsymbol x)\ge\int d\boldsymbol x\,p(\boldsymbol x)\log q(\boldsymbol x)\tag{5.167}$$
Notation: encoder $e(\boldsymbol z|\boldsymbol x)=p(\boldsymbol z|\boldsymbol x)$; backwards encoder $b(\boldsymbol z|\boldsymbol y)\approx p(\boldsymbol z|\boldsymbol y)$; classifier $d(\boldsymbol y|\boldsymbol z)\approx p(\boldsymbol y|\boldsymbol z)$; marginal $m(\boldsymbol z)\approx p(\boldsymbol z)$; $\langle\cdot\rangle$ is expectation under the joint $p(\boldsymbol x,\boldsymbol y,\boldsymbol z)$.

*Lower bound on $\mathbb I(\boldsymbol z;\boldsymbol y)$:*
$$\mathbb I(\boldsymbol z;\boldsymbol y)=\int d\boldsymbol y\,d\boldsymbol z\,p(\boldsymbol y,\boldsymbol z)\log\frac{p(\boldsymbol y,\boldsymbol z)}{p(\boldsymbol y)p(\boldsymbol z)}=\int p(\boldsymbol y,\boldsymbol z)\log p(\boldsymbol y|\boldsymbol z)-\int p(\boldsymbol y,\boldsymbol z)\log p(\boldsymbol y)\tag{5.168–5.169}$$
$$=\int d\boldsymbol y\,d\boldsymbol z\,p(\boldsymbol z)p(\boldsymbol y|\boldsymbol z)\log p(\boldsymbol y|\boldsymbol z)-\text{const}\ \ge\int p(\boldsymbol y,\boldsymbol z)\log d(\boldsymbol y|\boldsymbol z)=\langle\log d(\boldsymbol y|\boldsymbol z)\rangle\tag{5.170–5.172}$$
The constant is $\mathbb H(p(\boldsymbol y))$, independent of the representation. Samples come from $p(\boldsymbol y,\boldsymbol z)=\int d\boldsymbol x\,p(\boldsymbol x,\boldsymbol y)e(\boldsymbol z|\boldsymbol x)$ (5.173), the empirical distribution pushed through the encoder.

*Upper bound on $\mathbb I(\boldsymbol z;\boldsymbol x)$:*
$$\mathbb I(\boldsymbol z;\boldsymbol x)=\int p(\boldsymbol x,\boldsymbol z)\log\frac{p(\boldsymbol z,\boldsymbol x)}{p(\boldsymbol x)p(\boldsymbol z)}=\int p(\boldsymbol x,\boldsymbol z)\log p(\boldsymbol z|\boldsymbol x)-\int d\boldsymbol z\,p(\boldsymbol z)\log p(\boldsymbol z)\tag{5.174–5.175}$$
$$\le\int p(\boldsymbol x,\boldsymbol z)\log p(\boldsymbol z|\boldsymbol x)-\int d\boldsymbol z\,p(\boldsymbol z)\log m(\boldsymbol z)=\int p(\boldsymbol x,\boldsymbol z)\log\frac{e(\boldsymbol z|\boldsymbol x)}{m(\boldsymbol z)}=\langle\log e(\boldsymbol z|\boldsymbol x)\rangle-\langle\log m(\boldsymbol z)\rangle\tag{5.176–5.178}$$
Combining:
$$\beta\,\mathbb I(\boldsymbol x;\boldsymbol z)-\mathbb I(\boldsymbol z;\boldsymbol y)\le\beta(\langle\log e(\boldsymbol z|\boldsymbol x)\rangle-\langle\log m(\boldsymbol z)\rangle)-\langle\log d(\boldsymbol y|\boldsymbol z)\rangle\tag{5.179}$$
$$\mathcal L_{VIB}=\beta\,\mathbb E_{p_{\mathcal D}(\boldsymbol x)e(\boldsymbol z|\boldsymbol x)}[\log e(\boldsymbol z|\boldsymbol x)-\log m(\boldsymbol z)]-\mathbb E_{p_{\mathcal D}e\,d}[\log d(\boldsymbol y|\boldsymbol z)]\tag{5.180}$$
$$=-\mathbb E_{p_{\mathcal D}(\boldsymbol x)e(\boldsymbol z|\boldsymbol x)d(\boldsymbol y|\boldsymbol z)}[\log d(\boldsymbol y|\boldsymbol z)]+\beta\,\mathbb E_{p_{\mathcal D}(\boldsymbol x)}[D_{KL}(e(\boldsymbol z|\boldsymbol x)\|m(\boldsymbol z))]\tag{5.181}$$
Minimise by SGD over encoder, decoder and marginal, assuming reparameterisable distributions (§6.3.5). Typical choices: conditional Gaussian encoder, softmax decoder. $m(\boldsymbol z)$ should be flexible (e.g. a Gaussian mixture), since it must approximate the aggregated posterior $p(\boldsymbol z)=\int d\boldsymbol x\,p(\boldsymbol x)e(\boldsymbol z|\boldsymbol x)$, a mixture of $N$ Gaussians when $p(\boldsymbol x)$ is an empirical distribution with $N$ samples and $e(\boldsymbol z|\boldsymbol x)$ is Gaussian. In the MNIST example (2-d bottleneck, Fig. 5.13), the deterministic encoder maps each image to a point. The stochastic encoder keeps classes well separated, but individual instances are no longer distinguishable, since that information is irrelevant for prediction.

*Intuition note.* VIB is a classifier loss plus $\beta$ times a KL "rate" that charges for how much the encoder's code distribution differs from the marginal $m(\boldsymbol z)$. $\beta$ sets the trade-off between sufficiency and minimality (p. 252); in the MNIST example the stochastic encoder discards instance detail that is not relevant for prediction (p. 254).

**5.6.3 Conditional entropy bottleneck (CEB)** (pp. 254–256). IB can be written $\min\mathbb I(\boldsymbol x;\boldsymbol z)-\lambda\,\mathbb I(\boldsymbol y;\boldsymbol z)$ (5.182), but $\mathbb I(Z;X)$ contains some information relevant to $Y$ (Fig. 5.12b). The author proposes instead minimising the residual MI:
$$\min\ \mathbb I(\boldsymbol x;\boldsymbol z|\boldsymbol y)-\lambda'\,\mathbb I(\boldsymbol y;\boldsymbol z),\quad\lambda'\ge0\tag{5.183}$$
Since $\mathbb I(\boldsymbol x;\boldsymbol z|\boldsymbol y)=\mathbb I(\boldsymbol x;\boldsymbol z)-\mathbb I(\boldsymbol y;\boldsymbol z)$, the author states that CEB is equivalent to IB with $\lambda'=\lambda+1$ (as printed; see Reading notes). But the conditional term is easier to bound. Using $p(\boldsymbol z|\boldsymbol x,\boldsymbol y)=p(\boldsymbol z|\boldsymbol x)$:
$$\mathbb I(\boldsymbol x;\boldsymbol z|\boldsymbol y)=\mathbb I(\boldsymbol x;\boldsymbol z)-\mathbb I(\boldsymbol y;\boldsymbol z)=\mathbb H(\boldsymbol z)-\mathbb H(\boldsymbol z|\boldsymbol x)-[\mathbb H(\boldsymbol z)-\mathbb H(\boldsymbol z|\boldsymbol y)]=-\mathbb H(\boldsymbol z|\boldsymbol x)+\mathbb H(\boldsymbol z|\boldsymbol y)\tag{5.184–5.186}$$
$$=\int p(\boldsymbol x,\boldsymbol z)\log p(\boldsymbol z|\boldsymbol x)-\int p(\boldsymbol z,\boldsymbol y)\log p(\boldsymbol z|\boldsymbol y)\le\int p(\boldsymbol x,\boldsymbol z)\log e(\boldsymbol z|\boldsymbol x)-\int p(\boldsymbol z,\boldsymbol y)\log b(\boldsymbol z|\boldsymbol y)=\langle\log e(\boldsymbol z|\boldsymbol x)\rangle-\langle\log b(\boldsymbol z|\boldsymbol y)\rangle\tag{5.187–5.189}$$
The final CEB objective is
$$\min\ \beta(\langle\log e(\boldsymbol z|\boldsymbol x)\rangle-\langle\log b(\boldsymbol z|\boldsymbol y)\rangle)-\langle\log d(\boldsymbol y|\boldsymbol z)\rangle\tag{5.190}$$
The author notes the conditional backwards encoder $b(\boldsymbol z|\boldsymbol y)$ is generally easier to learn than the marginal $m(\boldsymbol z)$. The bound is tightest when $\mathbb I(\boldsymbol x;\boldsymbol z|\boldsymbol y)=0$, and the corresponding $\beta$ marks an optimal representation. For IB it is "not clear" how to measure distance from optimality (p. 256).

### 5.7 Algorithmic information theory
Shannon information depends on a distribution. For $n$ i.i.d. fair bits the coding length is $-\log_2p(\mathcal D|\theta)=n$ (entropy 1 bit per element), yet intuitively "such a sequence does not contain very much information at all". Algorithmic information theory instead quantifies the information in a given sequence (roots in [Sol64; Kol65; Cha66; Cha69]) (p. 256).

**5.7.1 Kolmogorov complexity** (pp. 256–257). For a bit string $\boldsymbol x$, with $U$ a universal Turing machine and $\ell(p)$ the program length:
$$K(\boldsymbol x)=\min_{p\in\mathcal B^*}[\ell(p):U(p)=\boldsymbol x]$$
It has properties analogous to Shannon entropy; ignoring additive constants, $K(\boldsymbol x|\boldsymbol y)\le K(\boldsymbol x)\le K(\boldsymbol x,\boldsymbol y)$, analogous to $\mathbb H(X|Y)\le\mathbb H(X)\le\mathbb H(X,Y)$. $K$ is not computable. **Levin complexity** adds a log running-time term and is computable:
$$L(\boldsymbol x)=\min_p[\ell(p)+\log(\mathrm{time}(p)):U(p)=\boldsymbol x]$$
It is computed by **Levin (universal) search**, which runs all programs time-sliced (time $2^{-\ell(p)}$ to program $p$) until the first halts, taking time $2^{L(\boldsymbol x)}$. It is still inefficient. For a distribution $q$ over bit strings, $K(\boldsymbol x)\le-\log q(\boldsymbol x)+K(q)$. For a parametric $q$, approximating $K(q)$ by the coding length of its parameters is equivalent to the MDL objective (§3.8.7.1).

*Randomness.* A string is **compressible** if $K(\boldsymbol x)<\ell(\boldsymbol x)=n$, otherwise **algorithmically random** (Martin-Löf randomness). Examples: $10101010\cdots$ is compressible (repeats "10"); $11001001\cdots$ is compressible, though less so (binary expansion of $\pi$ in the source's example; see Reading notes); $10110110\cdots$ is "truly random", derived from quantum fluctuations in the vacuum. A footnote says program length depends on the language, but the difference is an additive constant that becomes negligible as $n\to\infty$ (p. 257).

*Applications.* The individual-sequence approach underlies Lempel–Ziv compression (basis of zip). It also yields a universal similarity metric (5.191), where each $K$ is approximated by the cost of a compressor such as LZ (the normalized compression distance):
$$d(\boldsymbol x,\boldsymbol y)=\frac{\max[K(\boldsymbol x|\boldsymbol y),K(\boldsymbol y|\boldsymbol x)]}{\max[K(\boldsymbol x),K(\boldsymbol y)]}$$
[Jia+23] showed NCD with $K$-nearest neighbours can outperform BERT for text classification in the low-resource setting. The author adds that bag-of-words classifiers also do well there and are faster.

**5.7.2 Solomonoff induction** (pp. 257–259). Online prediction: we observe $\boldsymbol x_{1:t}$ from unknown $\mu$ and approximate it by $\nu\in\mathcal M$ (countable) to predict $\nu(x_{t+1}|\boldsymbol x_{1:t})$ (the problem of induction). Solomonoff takes $\mathcal M$ = all computable functions and prior $w_\nu=2^{-K(\nu)}$, a "universal prior" for any computable $\mu$, motivated by Occam's razor. For this (or any other) prior, the Bayesian mixture is
$$\xi(\boldsymbol x_{1:t})=\sum_{\nu\in\mathcal M}w_\nu\nu(\boldsymbol x_{1:t})\tag{5.192}$$
$$\xi(x_t|\boldsymbol x_{<t})=\frac{\xi(\boldsymbol x_{1:t})}{\xi(\boldsymbol x_{<t})}=\sum_\nu w_\nu\frac{\nu(\boldsymbol x_{1:t})}{\xi(\boldsymbol x_{<t})}=\sum_\nu w_\nu\frac{\nu(\boldsymbol x_{<t})}{\xi(\boldsymbol x_{<t})}\nu(x_t|\boldsymbol x_{<t})=\sum_\nu w(\nu|\boldsymbol x_{<t})\nu(x_t|\boldsymbol x_{<t})\tag{5.193–5.194}$$
using the posterior weight
$$w(\nu|\boldsymbol x_{1:t})=\frac{p(\nu)p(\boldsymbol x_{1:t}|\nu)}{p(\boldsymbol x_{1:t})}=\frac{w_\nu\nu(\boldsymbol x_{1:t})}{\xi(\boldsymbol x_{1:t})}\tag{5.195}$$
Accuracy is compared to the truth by the squared error at step $t$ and the expected total error to time $n$:
$$s_t(\boldsymbol x_{<t})=\sum_{x_t\in\mathcal X}(\mu(x_t|\boldsymbol x_{<t})-\xi(x_t|\boldsymbol x_{<t}))^2\tag{5.196}$$
$$S_n=\sum_{t=1}^n\sum_{\boldsymbol x_{<t}\in\mathcal X^{t-1}}\mu(\boldsymbol x_{<t})s_t(\boldsymbol x_{<t})\tag{5.197}$$
Solomonoff [Sol78] proved, in the limit,
$$S_\infty\le\ln(w_\mu^{-1})=K(\mu)\ln2\tag{5.198}$$
So the total error is bounded by the complexity of the data-generating environment: simple environments are easy to learn, and an optimal predictor's predictions rapidly approach the truth.

*Program view.* Suppose the data come from an unknown deterministic program $p$ with $U(p)=\boldsymbol x*$ (infinite extension of the prefix $\boldsymbol x=\boldsymbol x_{1:t}$), with prior $\Pr(p)=2^{-\ell(p)}$. The prior predictive distribution is
$$M(\boldsymbol x)=\sum_{p:U(p)=\boldsymbol x*}2^{-\ell(p)}\tag{5.199}$$
Remarkably $M(\boldsymbol x)=\xi(\boldsymbol x)$ (citing [WSH13]). Then $M(x_t|\boldsymbol x_{<t})=M(\boldsymbol x_{1:t})/M(\boldsymbol x_{<t})$. This is a convex combination of deterministic distributions, so it can also model stochastic environments. The scheme is uncomputable, but can be approximated: [GM+24] trained a transformer or LSTM by meta-learning on data from random Turing machines to approximate a universal predictor. [HQC24] apply Solomonoff induction to optimal online decision agents (AIXI).

*Intuition note.* Solomonoff induction is ordinary Bayesian mixing with a prior that favours short programs. The error bound says the cost of learning is at most the (log) prior weight of the true model, in nats.

## Toy example (ours, not from the text): XOR and co-information
Let $X,Y$ be independent fair bits and $Z=X\oplus Y$. All logs are base 2.
- Marginals: $H(X)=H(Y)=H(Z)=1$ ($Z$ is uniform).
- Pairs: $(X,Y)$ is uniform on 4 outcomes, so $H(X,Y)=2$. Given $X$, $Z$ determines $Y$ and vice versa, so $(X,Z)$ and $(Y,Z)$ are also uniform on 4 outcomes: $H(X,Z)=H(Y,Z)=2$. The triple has the same 4 outcomes, $H(X,Y,Z)=2$.
- Pairwise MI via (5.113): $\mathbb I(X;Y)=1+1-2=0$; $\mathbb I(X;Z)=1+1-2=0$; $\mathbb I(Y;Z)=0$.
- $\mathbb I(X,Y;Z)=H(Z)-H(Z|X,Y)=1-0=1$ ($Z$ is determined).
- Co-information by (5.128): $0+0-1=-1$.
- Check with (5.131): $[1+1+1]-[2+2+2]+2=3-6+2=-1$. ✓
- Check with (5.124): $\mathbb I(X;Y|Z)=1$ (given $Z$, $Y=X\oplus Z$ is a function of $X$, and $H(X|Z)=1$), so $0-1=-1$. ✓
- Total correlation (5.121): $3-2=1$.

So the MMI is negative (synergy: $X,Y$ together tell us about $Z$, individually nothing). This is the common-effect case of §5.3.5.4. Total correlation is positive here, since the three variables are not jointly independent.

## Concepts
- [[mutual-information]] (new) — KL divergence between joint and product of marginals; reduction in uncertainty about one variable from observing the other (p. 238).
- [[kl-divergence]] — used here as the base quantity for MI, rate, and excess code length $D_{KL}(p\|q)$ (pp. 238, 247).
- [[cross-entropy-perplexity]] (new) — perplexity is 2 to the empirical cross entropy; for a uniform model it equals the branching factor $K$ (p. 238).
- [[data-processing-inequality]] (new) — post-processing along a Markov chain $X\to Y\to Z$ cannot increase MI about $X$ (p. 239).
- [[sufficient-statistic]] (new) — $s(X)$ with $\mathbb I(\theta;s(X))=\mathbb I(\theta;X)$; minimal if a function of every other sufficient statistic (p. 240).
- [[total-correlation]] (new) — $D_{KL}(p(\boldsymbol x)\|\prod_dp(x_d))$; non-negative (p. 241).
- [[multivariate-mutual-information]] (new) — co-information, defined inductively through conditional MI; may be negative (p. 241).
- [[synergy-redundancy]] (new) — sign of the 3-way MMI: positive = redundancy, negative = synergy (p. 242).
- [[fork-chain-collider]] — sign of MMI differs for common cause, common effect and chain (p. 243).
- [[variational-mi-bounds]] (new) — upper bound, BA, DV/NWJ and InfoNCE bounds on MI (pp. 244–246).
- [[variational-inference-elbo]] — the rate–distortion Lagrangian $D+\beta R$ at $\beta=1$ is the negative of the VAE ELBO, $\mathcal L=-(D+R)$ (p. 249).
- [[source-coding-theorem]] (new) — expected lossless code length is at least $\mathbb H(p)$; excess is $D_{KL}(p\|q)$ (p. 247).
- [[rate-distortion]] (new) — trade-off between $R=\mathbb E[D_{KL}(e\|m)]$ and reconstruction distortion $D$; $\mathbb H-D\le\mathbb I\le R$ (p. 248).
- [[bits-back-coding]] (new) — argument that randomness used to sample the code can be recovered, so the cost is a KL rate (p. 250).
- [[information-bottleneck]] (new) — $\min\beta\,\mathbb I(z;x)-\mathbb I(z;y)$; VIB and CEB are its tractable variants (pp. 252–256).
- [[kolmogorov-complexity]] (new) — length of the shortest program producing a string on a universal Turing machine; uncomputable (p. 256).
- [[solomonoff-induction]] (new) — Bayesian mixture over computable models with prior $2^{-K(\nu)}$; total error $\le K(\mu)\ln2$ (p. 258).
- [[bayesian-occams-razor]] — the prior $2^{-K(\nu)}$ is motivated by Occam's razor (author's words) (p. 258).
- [[prior-predictive-distribution]] / [[posterior-predictive-distribution]] — $\xi(\boldsymbol x_{1:t})$ and $\xi(x_t|\boldsymbol x_{<t})$ in the Solomonoff mixture (p. 258).

## Canonical instances
- [[xor-collider-example]] — independent bits and their XOR become dependent given the XOR; MMI $\le0$ (p. 243).
- [[rain-cloud-fork]] — rain and dark sky independent given cloudiness (p. 243).
- [[bernoulli-sufficient-statistic]] — $N$ and the success count are a minimal sufficient statistic for $N$ Bernoulli trials (p. 240).
- [[parity-bit-code]] — 2 message bits + 1 parity bit, $\alpha=0.2$, $\boldsymbol y=(1,0,0)$; modes 000, 110, 101 (pp. 251–252).
- [[newsgroups-relevance-network]] — MI graph over words in 20-newsgroups; dense-graph problem (pp. 246–247).
- [[vib-mnist]] — 2-d bottleneck, deterministic vs stochastic encoder (p. 254).
- [[hutter-prize]] — compression of Wikipedia as a measure of AI progress (p. 247).
- [[ncd-text-classification]] — compression distance + kNN vs BERT (p. 257).

## Bridges (candidates)
- [same-math] $\mathbb I(X;Y)=D_{KL}(\text{joint}\|\text{product})$ ↔ bayesian: expected information gain from updating "independent" to "dependent" model — same KL form, as the author states (p. 239).
- [same-math] VAE ELBO $=-(D+R)$ ↔ bayesian: variational inference ELBO — the author shows the objectives coincide at $\beta=1$ (p. 249).
- [structural-analogy] Co-information sign for fork/collider/chain ↔ causal inference: conditioning on a collider opens a path, conditioning on a common cause blocks it.
- [structural-analogy] Parity-bit decoding ↔ bayesian: posterior over codewords from a likelihood (bit-flip noise) and a deterministic prior constraint.
- [same-math] Solomonoff mixture $\xi$ and posterior weights (5.195) ↔ bayesian: posterior predictive of a Bayesian model average.
- [structural-analogy] Prior $2^{-K(\nu)}$ ↔ bayesian: Occam-style complexity penalty / MDL.

## Questions this raises
- The InfoNCE bound is capped at $\log K$; what does that imply for estimating large MI, and how does the multi-label alternative [SE20a] avoid it?
- If $\beta=1$ solutions on the rate–distortion diagonal all have the same ELBO, what evaluation criteria can tell good unsupervised representations from bad ones?
- How do co-information signs behave for larger sets, and can a negative value always be read as a collider structure (the text only discusses 3 variables)?
- How far can practical approximations of Solomonoff induction (e.g. meta-learned transformers) retain the $K(\mu)\ln2$ error guarantee?

## Reading notes
- This part begins mid-§5.2 (empirical cross entropy and perplexity, printed p. 238) and ends at the end of §5.7.2 (printed p. 259). The final page (pdf 294, printed 260) is blank. Offset: printed = pdf − 34.
- Even-numbered pages carry the footer "Online version. December 10, 2025"; odd pages carry the author/licence line.
- **Possible misprint, p. 238:** the text says perplexity cannot be reduced below $2^{-\mathbb H(p^*)}$. By (5.107) perplexity is $2^{\text{cross entropy}}$, so a floor from $\mathbb H(p^*)\le\mathbb H_{ce}$ would have exponent $+\mathbb H(p^*)$. I report only the qualitative statement.
- **Possible misprint, p. 248:** "the latent code is independent of $z$" in the zero-rate setting is presumably meant to say independent of $\boldsymbol x$. p. 243: for the chain the author says MMI "must be positive"; the argument given supports non-negative.
- **Footnote mark, p. 257:** "$\pi^2$" in the text layer (binary expansion of "$\pi^2$") is the digit-sequence example with footnote mark 2 (which concerns the binary expansion of $\pi$). In the page image the superscript 2 after $\pi$ is a footnote mark (footnote 2 concerns the binary expansion of $\pi$); only the text layer renders it as $\pi^2$.
- Derivations of InfoNCE (5.151–5.152), the claim $M=\xi$, and Solomonoff's bound (5.198) are cited, not proved, in this text. §5.3.2 states (5.112)–(5.113) without proof.
- Possible error, p. 255: the text says CEB (5.183) is equivalent to IB with $\lambda'=\lambda+1$. Since $\mathbb I(x;z|y)-\lambda'\mathbb I(y;z)=\mathbb I(x;z)-(1+\lambda')\mathbb I(y;z)$, matching (5.182) gives $\lambda=1+\lambda'$, i.e. $\lambda'=\lambda-1$. The digest reports the author's statement only.
- No exercises appear in this part.
