---
id: jaynes-2003-probability/ch13-decision
work: jaynes-2003-probability
unit: "13 Decision theory, historical background"
pages: 397-425
fields: [information-theory, bayesian]
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
# Decision theory, historical background

## L0 — One line
Inference only gives a posterior; to act, add a loss (utility) function and minimise expected loss over that posterior. A sampling theorist who thinks his estimation problem through to the end ends up obliged to use this same Bayesian calculation, even if he rejects its rationale.

## L1 — The gist (≤ 120 words)
Probability theory yields the robot's state of knowledge, not an action. Jaynes asks how to turn a posterior into a decision, and what this says about the old dispute over the foundations of probability. He follows the line from Bernoulli and Laplace (expected utility, log utility) to Wald's risk and admissibility. He shows that averaging risk over a weight g(α) gives the expected loss over the posterior, when g is read as a prior density. Quadratic, absolute and 0–1 loss then give the posterior mean, median and mode. Rules are Bayesian whether one starts from frequencies or from information. Jaynes argues that loss functions are less well grounded than priors, so decision theory is not fundamental.

**Prerequisites:** expectation and variance; Bayes' theorem and posterior pdfs; first variation of an integral (calculus of variations); entropy and relative entropy.

## L2 — Key ideas
- Inference and decision are distinct. Probability theory gives only the posterior, and critical levels or estimates need a value judgment too. Jaynes says formal decision theory will "only legitimize – not change" what intuition already says (pp. 397–398, 405).
- Bernoulli replaced expected profit by expected "moral value" (utility ∝ log of wealth). With log utility the St Petersburg game gets a finite, sensible-looking fair fee, and insurance can suit both buyer and seller (pp. 399–401).
- Log utility links to entropy. For a bettor maximising expected log fortune, Exercise 13.1 asks the reader to show that the best growth rate is H₀ − H. A log-score pay scheme makes an honest forecast maximise expected pay, if the forecaster's utility is linear in the pay (pp. 402–403).
- Wald's risk and admissibility are sampling-theory notions. Jaynes argues that admissibility ignores prior information, and that a rule that always says θ* = 5 counts as admissible if θ = 5 is in the parameter space (pp. 408–409).
- Minimising risk at each fixed α gives no usable estimator: the best one for a given α depends on α, which is unknown, and the variational problem has no stationary solution. Averaging risk over a weight g(α) gives a solvable problem whose answer is the Bayes rule when g is read as the prior (pp. 411–415).
- The choice of loss decides the estimator: squared gives mean, absolute gives median, 0–1 gives mode (maximum likelihood, if g is flat enough). For an exponential posterior the optimal β ranges from 0 up to 2.025⟨α⟩ and beyond (pp. 414–416).
- The general recipe has four inference steps and three decision steps. Only the product g·L matters, so anyone who worries about arbitrary priors should, to be consistent, worry as much about arbitrary loss functions (pp. 417–419).
- Jaynes judges loss functions less firmly grounded than priors. In his view logical consistency, not betting coherence, is the right foundation (pp. 420, 424–425).

## L3 — Walkthrough

### 13.1 Inference vs. decision (pp. 397–398)
- Earlier chapters left gaps. In sequential testing (Ch. 4) probability theory cannot say where to put the thresholds for accept, reject or test again. Those thresholds depend on the costs of wrong decisions and of more tests (p. 397).
- In parameter estimation (Ch. 6) the posterior mean minimises expected squared error, but sometimes the median is preferred (p. 397).
- Probability theory alone solves only the inference problem. The robot still needs a rule converting its final probability assignment into action (p. 398).
- Jaynes says formal decision theory will "only legitimize – not change" what intuition already says (p. 398).
- Decision theory can be derived from two diametrically opposed views of probability. It therefore bridges them and may help resolve the controversy (p. 398).

### 13.2 Daniel Bernoulli's suggestion (pp. 398–400)
- Expectation of profit for outcomes $i=1..n$ with probabilities $p_i$ and profits $M_i$ is
$$E(M)=\bar M=\sum_{i=1}^{n}p_iM_i.\tag{13.1}$$
- Early workers found expectation of profit more intuitive than probability. The Amsterdam merchants traded expectations as goods (p. 398).
- Maximising expected profit gives paradoxes. Example: P(heads) = 0.51 and you may bet all your money $M_0$ at even money on heads. Then
$$\bar M=0.51M_0+0.49(-M_0)=0.02M_0>0,\tag{13.2}$$
  yet nobody sane bets everything. A second offer is a bet that loses with probability $1-10^{-6}$ and pays 1 000 001 times the stake with probability $10^{-6}$; common sense rejects it even more strongly (pp. 398–399).
- Bernoulli's resolution: the value of money depends on what one already has. "Moral expectation" differs from mathematical expectation, which is today's diminishing marginal utility (p. 399).
- St Petersburg game: toss a fair coin until the first head at toss $n$ and receive $2^n$ dollars. The expectation is infinite:
$$\sum_{k=1}^{\infty}(2^{-k})(2^{k})=\sum_{k=1}^{\infty}1=\infty.\tag{13.3}$$
- Laplace (paraphrased, p. 399): the relative value of an infinitely small sum is its absolute value divided by the person's total fortune. So utility of money $M$ is proportional to $\log M$.
- For fortune $m$, the fair fee $f(m)$ solves
$$\log m=\sum_{n=1}^{\infty}\frac{1}{2^n}\log(m-f+2^n).\tag{13.4}$$
  Numerically $f(200)=8.7204$, which agrees with Laplace's figure of about 9 francs as the most a person with 200 francs should reasonably stake. Also $f(10^3)=10.95$, $f(10^4)=14.24$, $f(10^6)=20.87$ (p. 400).
- Log utility is not to be taken literally at the extremes. Savage's example: at fortune \$1 000 000 a log-utility person would be indifferent to a coin-flip between \$1000 and \$10⁹. Most people find this bet clearly disadvantageous. So utility rises more slowly than log for very large sums. Chernoff and Moses claim it is bounded, which Jaynes finds theoretically plausible but not demonstrated (p. 400).
- Gist: act to maximise the expected value of a function of profit (the "moral value", i.e. utility). Equivalently minimise expected loss, with loss = −utility (p. 400).

*Intuition note:* A dollar matters less to a rich person, so utility bends. A bend as gentle as the logarithm already makes the St Petersburg game worth only about 9–21 francs, not infinity.

### 13.3 The rationale of insurance (pp. 400–402)
- Premiums give the company positive expected profit, yet customers still buy. The customer's utility for money can be strongly curved over \$1000 ranges. The company's utility is accurately linear over millions (p. 400).
- Setup: premium $P$; contingencies $i$ with probability $w_i$ and cost $L_i$ to the company; customer with log utility and net worth $M$. Table 13.1 (expected utilities):

| | Buy | Don't buy |
|---|---|---|
| Company | $P-\sum w_iL_i$ | $0$ |
| Customer | $\log(M-P)$ | $\sum w_i\log(M-L_i)$ |

- The company sells if $\langle L\rangle<P$. The customer buys if $\langle\log(M-L)\rangle<\log(M-P)$, which is equivalent to $P<M-\exp\langle\log(M-L)\rangle$ (added step). Both gain if
$$\langle L\rangle<P<\left[M-\exp\langle\log(M-L)\rangle\right].\tag{13.5}$$
- Exercise left to the reader: show from (13.5) that a poor man should buy, and a rich man should not unless his assessment of $\langle L\rangle$ is much greater than the company's. A rich man's utility is nearly linear, so he may as well act as his own insurer (p. 401).
- For $M\gg\langle L\rangle$, expanding in powers of $M^{-1}$ gives
$$M-\exp\langle\log(M-L)\rangle=\langle L\rangle+\frac{\mathrm{var}(L)}{2M}+\cdots,\tag{13.6}$$
  with $\mathrm{var}(L)=\langle L^2\rangle-\langle L\rangle^2$. A moderately rich man may pay slightly more than $\langle L\rangle$ to remove the uncertainty $\mathrm{var}(L)$ (p. 401).
- Rewriting the upper limit:
$$M-\exp\langle\log(M-L)\rangle=M-\prod_i\exp\{w_i\log(M-L_i)\}.\tag{13.7}$$
  Order $L_1\ge L_2\ge\cdots$. The expression needs $M>L_1$, and presumably $M<L_1$ is impossible because one cannot lose more than he has. As $M\to L_1$ the last factor is $\exp\{-\infty\}$ and drops out. Then (13.5) reduces to $\langle L\rangle<P<M$: the poor man should buy at any premium below his whole net worth $M$ (p. 401).
- This shows log utility is unrealistic for very small amounts, where utility is bounded. Jaynes suggests replacing $\log M$ by $\log(M+b)$ with $b$ practically worthless. How this modifies the conclusion from (13.7), and what $b$ to choose, is left to the reader (p. 402).

*Intuition note:* Insurance is a trade between two parties with different utility curves. One side wants to shed risk and the other can absorb it at almost linear cost, so both can gain even though one side's expected money falls.

### 13.4 Entropy and utility (p. 402)
- Bellman and Kalaba (1956, 1957): a gambler with partially reliable tips who maximises the expected logarithm of his fortune (1) never goes broke, unlike expected-profit maximisation, which eventually ruins him with probability one. They also show (2) the expected win per game is proportional to current fortune, so after $n$ games $M=M_0\exp\{\alpha n\}$. Log utility means maximising the expectation of $\alpha$ (p. 402).
- **Exercise 13.1:** show the maximum attainable $\alpha$ is $H_0-H$. Here $H$ is the entropy of the gambler's uncertainty about the truth of his tips, and $H_0$ is the maximum entropy if the tips were uninformative (p. 402).
- Jaynes speculates that entropy may guide businessmen and investors. He also notes one can manipulate others' utilities so they behave as wished (p. 402).

### 13.5 The honest weatherman (pp. 402–404)
- The forecaster's data give $p=P(\text{rain}\mid\text{data},I)$ but he announces $q$. Jaynes suspects forecasters announce $q>p$ because missed storms cost more criticism than false alarms (p. 403).
- Contract: pay $B\log(2q)$ if it rains, $B\log(2[1-q])$ if not. Expected pay:
$$B[p\log(2q)+(1-p)\log(2[1-q])]=B[\log 2+p\log q+(1-p)\log(1-q)].\tag{13.8}$$
- The first and second derivatives show a maximum at $q=p$ (p. 403). Check: $p/q-(1-p)/(1-q)=0$ gives $q=p$, and the second derivative $-p/q^2-(1-p)/(1-q)^2$ is negative (added step).
- Any continuous utility looks linear on a small segment. So if one day's pay is small, truth-telling is advantageous. Honesty is literally the best policy for some reward/utility combinations (p. 403).
- General case: events $A_1..A_n$ with true probabilities $p_i$, announced $q_i$, pay $B\log(nq_i)$ if $A_i$ occurs. The author's printed forms are
$$B[\log n-I(q;p)],\qquad I(q;p)\equiv\sum p_i\log q_i,\tag{13.9}$$
  which Jaynes calls essentially the relative entropy (Kullback–Leibler information), already proved and used by Gibbs (1902). (The sign and definition do not match (13.10) as printed; see Reading notes.) Directly, the expected pay is $B[\log n+\sum p_i\log q_i]$ (added step).
- It is best to announce $q_i=p_i$, giving maximum expected pay
$$B[\log n-H(p_1,\dots,p_n)],\qquad H=-\sum p_i\log p_i.\tag{13.10}$$
  The forecaster also gains by acquiring more information, which lowers $H$ (p. 403).
- Drug company example: drug A helps $10^6$ persons a year, drug B 1000. The company will prefer A. Jaynes says the profit motive here also benefits a much larger part of society (p. 404).

*Intuition note:* A pay scheme using the log of the probability you gave to what actually happened rewards exactly your honest belief. Any distortion of $q$ away from $p$ costs you expected pay by a relative-entropy amount.

### 13.6 Reactions to Daniel Bernoulli and Laplace (pp. 404–405)
- Jaynes finds it surprising that entropy was not discovered this way 100 years before Gibbs. For most of the 20th century the "frequentist" school ignored this line of reasoning or condemned it as metaphysical nonsense (p. 404).
- **Feller (1950, p. 199)** rejects Bernoulli's resolution without describing it. **Hirsch's review** calls such explanations hardly understandable. Jaynes replies that Feller "resolved" the paradox by analysing a different game. Since Feller rejects a curved utility, he concludes (as Jaynes reports) that insurance is always necessarily "unfair" to the insured (p. 404).
- Neyman–Pearson decision rules (1930s–40s) are now obsolete, in Jaynes's view, because they lack two features now seen as essential. Chapter 14 gives an example. Wald (1950) works at a more fundamental level and justifies Bernoulli's ideas (pp. 404–405).
- **Kendall (1963)** says Fisher would have maintained, rightly in Kendall's opinion, that inference in science is not a matter of decision, and describes the decision-theory view as the American as against the English point of view. **Fisher (1956)** says reinterpreting significance tests as acceptance procedures reflects lack of familiarity with natural science. Jaynes answers that Bernoulli and Laplace were natural scientists of comparable stature (p. 405).
- Jaynes agrees with Kendall that Wald's approach gives the impression that inference is a special case of decision, and deplores it. In the Bernoulli–Laplace formulation (and in his own) the two functions stay distinct. Yet inference not followed by decision is "largely idle" (p. 405).

### 13.7 Wald's decision theory (pp. 406–409)
- Basic objects: **states of nature** $\{\theta_1..\theta_N\}$ (finite in practice), **decisions** $\{D_1..D_k\}$, and the **loss function** $L(D_i,\theta_j)$, a loss matrix $L_{ij}$ if both are discrete (pp. 406–407).
- The states are not a verifiable property of nature, since only one is true. They describe a state of knowledge, so two robots with different information may enumerate them differently without inconsistency (p. 406).
- "Making a decision" means deciding to act as if it were correct. The list of $D_i$ describes which actions are feasible, and tolerable consequences prune it (p. 406).
- Quality-control example: $D_1$ accept, $D_2$ reject, $D_3$ test again. Particle-counter example: $D_i$ = estimate $n_1$ as $i$, an infinite set (p. 406).
- **Minimax:** for each $D_i$ take $M_i=\max_jL_{ij}$, then choose the $D_i$ with minimum $M_i$. This is reasonable if Nature is an intelligent adversary, as in some games (von Neumann–Morgenstern). For a scientist it is the pessimist's criterion (p. 407).
- **Minimin:** choose the $D_i$ minimising $m_i=\min_jL_{ij}$, the optimist's criterion. A reasonable criterion lies between the two, since Nature is neutral. Other proposals are maximin utility (Wald), α-optimism–pessimism (Hurwicz) and minimax regret (Savage). They are tested against about a dozen common-sense conditions, for example transitivity of preferences and strong domination (if $L_{ij}<L_{kj}$ for all $j$, prefer $D_i$). Jaynes says only one class of criteria passes all tests, and it is reached more easily by another route (pp. 407–408).
- Wald's detour: a **strategy** $S$ is a set of rules of the form: if new evidence $E_i$ arrives, make decision $D_k$. The sampling probability of $D_k$ if $\theta_j$ is true is
$$p(D_k|\theta_jS)=\sum_i p(D_k|E_i\theta_jS)\,p(E_i|\theta_j),\tag{13.11}$$
  and the **risk** is the expected loss over it:
$$R_j(S)=\langle L\rangle_j=\sum_k p(D_k|\theta_jS)L_{kj}.\tag{13.12}$$
- $S$ is **admissible** if no $S'$ exists with
$$R_j(S')\le R_j(S)\ \text{ for all } j.\tag{13.13}$$
  If some $S'$ satisfies this with strict inequality for at least one $\theta_j$, $S$ is **inadmissible**. These are sampling-theory criteria, since they use only the sampling distribution. Wald's aim was to characterise the admissible class via the **complete class theorem**, whose result shocked sampling theorists, Wald included (p. 408).
- Jaynes's critique (his view):
  - Admissibility ignores prior information. An "inadmissible" rule may be vastly preferable, as in medical or airline-safety decisions where ignoring cogent prior information would be criminal negligence (Ch. 17 returns to this) (p. 409).
  - A rule that ignores the data and always estimates $\theta^*=5$ is admissible if $\theta=5$ lies in the parameter space. Almost any "inadmissible" rule would beat it (p. 409).
  - Jaynes warns against noble-sounding names like "admissible" and "unbiased" (p. 409).
- What makes decisions hard: given the loss function, uncertainty about the best decision arises solely from uncertainty about the state of nature. The robot asks for $P_3$, the probability that $\theta_3$ is true. A sampling theorist holds that probability means long-run frequency and the state of nature is not a random variable, so this question is meaningless to him. That reasoning led early-20th-century statisticians to separate "statistical inference" from probability theory (p. 409).

### 13.8 Parameter estimation for minimum loss (pp. 410–412)
- Setting: unknown parameter $\alpha$, sample $x=\{x_1..x_n\}$, forced to pick one estimate and act on it (the driver at a blind intersection) (p. 410). Independent observations give
$$f(x|\alpha)=f(x_1|\alpha)\cdots f(x_n|\alpha),\tag{13.14}$$
  but independence is not needed for the general principles (p. 410).
- Estimator $\beta=\beta(x_1..x_n)$ and loss $L(\alpha,\beta)$. The **risk** is the pre-data expected loss, for someone who knows $\alpha$ but not the data:
$$R_\alpha\equiv\int dx\,L(\alpha,\beta)f(x|\alpha),\qquad \int dx(\,)=\int\!\cdots\!\int dx_1\cdots dx_n(\,).\tag{13.15, 13.16}$$
  For discrete data, $f$ is a sum of delta functions (p. 410).
- **Frequentist view (reported):** $f(x|\alpha)$ is an objective long-run frequency, and $R_\alpha$ is, with probability one, the limit of average actual losses over repeated samples at fixed $\alpha$. Finding the estimator best for the present specific sample is foreign to him; he speaks instead of the estimator that will prove best on average in the long run (p. 411).
- **Jaynes's reply:** one almost never knows true limiting frequencies, and no scientist knows what is "really true"; we know only our state of knowledge. It seems to Jaynes that believing probabilities to be realities in Nature is a mind projection fallacy; our equations describe and process our information about reality (p. 411).
- Minimising $R_\alpha$ as a variational problem: a change $\delta\beta(x)$ gives
$$\delta R_\alpha=\int dx\,\frac{\partial L(\alpha,\beta)}{\partial\beta}f(x|\alpha)\,\delta\beta(x).\tag{13.17}$$
  Requiring this to vanish for all $\delta\beta$ gives
$$\frac{\partial L}{\partial\beta}=0\ \text{ for all possible }\beta.\tag{13.18}$$
  So there is no stationary solution except the useless case of a loss independent of $\beta$. A "best" estimator by minimum risk, if any, cannot be found by variational methods (p. 411).
- For quadratic loss $L=(\alpha-\beta)^2$:
$$R_\alpha=\int dx\,(\alpha^2-2\alpha\beta+\beta^2)f(x|\alpha)\tag{13.19}$$
$$R_\alpha=(\alpha-\langle\beta\rangle)^2+\mathrm{var}(\beta),\tag{13.20}$$
  with $\langle\beta^n\rangle\equiv\int dx\,[\beta(x)]^nf(x|\alpha)$ (13.21) and $\mathrm{var}(\beta)=\langle\beta^2\rangle-\langle\beta\rangle^2$ (p. 412).
- The two terms are positive. A good estimator by minimum risk has (1) $\langle\beta\rangle=\alpha$ (unbiased; bias is $b(\alpha)=\langle\beta\rangle-\alpha$) and (2) minimum $\mathrm{var}(\beta)$. Fisher called (1)+(2) "efficient"; today it is unbiased minimum variance (UMV). Chapter 17 treats the Cramér–Rao inequality (p. 412).
- The weakness: sampling theory compares guesses but cannot construct the best estimator. A simple substitute for Wald's complete class theorem follows (p. 412).

*Intuition note:* Squared-error risk splits into bias² plus variance. These are just the two conditions sampling theory has considered most important. Minimising risk at a fixed $\alpha$ is still ill-posed.

### 13.9 Reformulation of the problem (pp. 412–415)
- The trouble: the solution of "minimise $R_\alpha$" depends on $\alpha$ itself. The best estimator for a known $\alpha$ is trivially $\beta=\alpha$, which is useless since $\alpha$ is unknown. The estimator must compromise over a range of $\alpha$ (pp. 412–413).
- So minimise a weighted risk, with $g(\alpha)\ge0$ expressing the importance of each $\alpha$:
$$\langle R\rangle=\int d\alpha\,g(\alpha)R_\alpha.\tag{13.22}$$
  This is a solvable variational problem with a unique, useful solution (p. 413). The first variation is
$$\delta\langle R\rangle=\int\!\cdots\!\int dx_1\cdots dx_n\Big\{\int d\alpha\,g(\alpha)\frac{\partial L(\alpha,\beta)}{\partial\beta}f(x_1..x_n|\alpha)\Big\}\delta\beta(x_1..x_n),\tag{13.23}$$
  which vanishes for arbitrary $\delta\beta$ if, for all possible samples,
$$\int d\alpha\,g(\alpha)\frac{\partial L(\alpha,\beta)}{\partial\beta}f(x_1..x_n|\alpha)=0.\tag{13.24}$$
- The second variation gives a true minimum if
$$\int d\alpha\,g(\alpha)\frac{\partial^2L}{\partial\beta^2}f(x_1..x_n|\alpha)>0.\tag{13.25}$$
  $\partial^2L/\partial\beta^2\ge0$ is sufficient but stronger than necessary (p. 413).
- **Quadratic loss** $L=K(\alpha-\beta)^2$: (13.24) becomes
$$\int d\alpha\,g(\alpha)(\alpha-\beta)f(x_1..x_n|\alpha)=0\tag{13.26}$$
$$\beta(x_1..x_n)=\frac{\int d\alpha\,g(\alpha)\,\alpha\,f(x_1..x_n|\alpha)}{\int d\alpha\,g(\alpha)f(x_1..x_n|\alpha)}.\tag{13.27}$$
  This is the mean of the posterior
$$f(\alpha|x_1..x_n,I)=\frac{g(\alpha)f(x_1..x_n|\alpha)}{\int d\alpha\,g(\alpha)f(x_1..x_n|\alpha)}\tag{13.28}$$
  if $g$ is read as a prior density. Bayes' theorem enters parameter estimation by mathematical necessity (pp. 413–414).
- **Absolute loss** $|\alpha-\beta|$:
$$\int_{-\infty}^{\beta}d\alpha\,g(\alpha)f(x|\alpha)=\int_{\beta}^{\infty}d\alpha\,g(\alpha)f(x|\alpha)\tag{13.29}$$
  so $\beta$ is the posterior median:
$$\int_{-\infty}^{\beta}d\alpha\,f(\alpha|x_1..x_n,I)=\int_\beta^\infty d\alpha\,f(\alpha|x_1..x_n,I)=\tfrac12.\tag{13.30}$$
- **Fourth-power loss** $(\alpha-\beta)^4$ gives the real root of
$$f(\beta)=\beta^3-3\langle\alpha\rangle\beta^2+3\langle\alpha^2\rangle\beta-\langle\alpha^3\rangle=0,\tag{13.31}$$
  $$\langle\alpha^n\rangle=\int d\alpha\,\alpha^nf(\alpha|x_1..x_nI)\tag{13.32}$$
  being posterior moments. Jaynes says there is only one real root, as seen by forming the discriminant; the condition $f'(\beta)\ge0$ for all real $\beta$ is just $\langle\alpha^2\rangle-\langle\alpha\rangle^2\ge0$ (p. 414). (Here $f'=3[(\beta-\langle\alpha\rangle)^2+\mathrm{var}(\alpha)]$, added step.)
- **0–1 loss** (limit of $|\alpha-\beta|^k$ as $k\to0$):
$$L(\alpha,\beta)=\begin{cases}0&\alpha=\beta\\1&\text{otherwise}\end{cases}\tag{13.33}$$
  gives the posterior mode. If $g$ is constant in the high-likelihood region and not much greater elsewhere, this is Fisher's maximum likelihood. Maximum likelihood is thus the right criterion only when we care about being exactly right and not how wrong we are, "a miss is as good as a mile" (p. 414).
- (13.24) can be written
$$\frac{\partial}{\partial\beta}\int d\alpha\,g(\alpha)L(\alpha,\beta)f(x_1..x_n|\alpha)=0.\tag{13.34}$$
  With $g$ read as a prior, this says to minimise the expected loss over the Bayesian posterior for $\alpha$, not over the sampling pdf of $\beta$ (pp. 414–415).
- Jaynes's comment: a sampling theorist who thinks it through is obliged to use the Bayesian algorithm, even if he rejects the Bayesian rationale. He calls this "chickens coming home to roost" (p. 415).
- **Wald's conclusion (as Jaynes reports it):** if the $\theta_j$ are discrete and none known to be impossible are listed, the admissible strategies are exactly the Bayes strategies (minimising expected loss over a posterior). For continuous $\theta_j$, admissible rules are Bayes rules from proper (normalisable) priors. Few have followed Wald's proof, and Berger (1985) gives only isolated special results (p. 415).
- Improper priors in infinite spaces cause "nitpicking", which Jaynes dismisses. Admissibility ignores prior information and so treats all points of an infinite domain as equivalent, and the resulting singularity is an artifact. His position: defensible rules are Bayes rules from proper priors and their well-behaved limits. Wald, once a proponent of von Mises' collective theory, accepted this and called admissible rules "Bayes strategies" in Wald (1950) (p. 415).

*Intuition note:* Minimising risk averaged over $\alpha$ with weight $g$ is the same as minimising loss averaged over the posterior with $g$ read as the prior. The posterior mean, median and mode are not separate tricks; they are the answers for three different loss functions.

### 13.10 Effect of varying loss functions (pp. 415–417)
- Example posterior:
$$f(\alpha|DI)=k\exp\{-k\alpha\},\ 0\le\alpha<\infty;\qquad\langle\alpha^n\rangle=\int_0^\infty d\alpha\,\alpha^nf=n!\,k^{-n}.\tag{13.35, 13.36}$$
- Squared loss: $\beta=\langle\alpha\rangle=k^{-1}$ (13.37). Absolute loss: $\tfrac12=1-\exp\{-k\beta\}$ (13.38), so
$$\beta=k^{-1}\ln2=0.693\langle\alpha\rangle.\tag{13.39}$$
- Fourth-power loss: (13.31) becomes $y^3-3y^2+6y-6=0$ with $y=k\beta$. Its real root is $y=1.59$, so
$$\beta=1.59\langle\alpha\rangle.\tag{13.40}$$
  Check with the moments: $n!k^{-n}$ in (13.31) gives this cubic after multiplying by $k^3$ (added step).
- Loss $(\alpha-\beta)^{s+1}$ with $s$ odd: (13.34) gives
$$\int_0^\infty d\alpha\,(\alpha-\beta)^s\exp\{-k\alpha\}=0\tag{13.41}$$
$$\sum_{m=0}^{s}\frac{(-k\beta)^m}{m!}=0.\tag{13.42}$$
  $s=3$ reproduces (13.40). $s=5$ (loss $(\alpha-\beta)^6$) gives $\beta=2.025\langle\alpha\rangle$ (13.43). As $s\to\infty$, $\beta$ grows without limit. Maximum likelihood (loss $-\delta(\alpha-\beta)$, or $\lim_{k\to0}|\alpha-\beta|^k$ (13.44)) gives $\beta=0$ (p. 416).
- Moral: when the posterior is not sharply peaked, the best estimate depends strongly on the loss function (p. 416).
- A loss need not increase monotonically with error. William Tell would rather make a large error than a small one, and then no decision has small expected loss (pp. 416–417).
- **Invariance:** the decision is unchanged under $L'(D_i,\theta_j)=a+bL(D_i,\theta_j)$ with $-\infty<a<\infty$, $0<b<\infty$ (13.45), for any priors and data. Example: the loss matrix
$$L_{ij}=\begin{pmatrix}10&19\\100&10\end{pmatrix}\tag{13.46}$$
  may be replaced by
$$L'_{ij}=\begin{pmatrix}0&1\\10&0\end{pmatrix}\tag{13.47}$$
  with $a=-10/9$, $b=1/9$ (p. 417).

### 13.11 General decision theory (pp. 417–418)
- Inference, four steps: (1) enumerate states of nature $\theta_j$; (2) assign priors $p(\theta_j|I)$; (3) assign sampling probabilities $p(E_i|\theta_j)$ for the measurement process; (4) apply Bayes' theorem to the evidence $E=E_1E_2\cdots$, getting $p(\theta_j|EI)$ (p. 417).
- Decision, three more steps: (5) enumerate decisions $D_i$; (6) assign the loss $L(D_i,\theta_j)$; (7) choose the $D_i$ minimising expected loss over the posterior for $\theta_j$ (p. 417).
- Jaynes says the theorems of Cox, Wald and Shannon lead to the rules of Laplace and Bernoulli, except that the entropy principle generalises the principle of indifference in step (2) (p. 418).
- Jaynes's claim: the rules are fixed uniquely by qualitative desiderata of rationality and consistency. Someone who denies having a prior or loss function is told that consistency requires acting as if he had them. For every strategy obeying the desiderata there are a prior and a loss that would produce it, and conversely any strategy derived from a prior and loss obeys them (p. 418).
- Pragmatically the rules include or improve on practically all known methods for hypothesis testing and point estimation. Applying them well needs practice, which Jaynes compares to learning a musical instrument (p. 418).

### 13.12 Comments
**13.12.1 "Objectivity" of decision theory (pp. 418–421).**
- Decision procedures can be derived from either of two opposed views of probability. Jaynes says there appears to be universal agreement on the procedures but not on the reason (p. 418).
- A sampling theorist holds that Bayes' theorem applies only if priors are known frequencies, and Jaynes doubts any real problem ever met that condition (pp. 418–419).
- Only the product $g(\alpha)L(\alpha,\beta)$ matters in (13.24) and (13.34). Three readings give the same decision: (1) prior $g$, loss $(\alpha-\beta)^2$; (2) uniform prior, loss $g(\alpha)(\alpha-\beta)^2$; (3) prior $h(\alpha)$, loss $g(\alpha)(\alpha-\beta)^2/h(\alpha)$ (p. 419).
- Sampling-theory expositions (Chernoff and Moses are cited) postpone priors and invent artificial frequency situations for them, yet pull completely arbitrary loss functions out of thin air. If one worries about arbitrary priors, consistency requires worrying just as much about arbitrary loss functions. Jaynes says this lopsided attitude is closely connected with a behaviouristic or positivistic philosophy. Jaynes holds that rational action needs rational thought, and that loss functions are purely subjective value judgments (pp. 419–420).
- Priors are usually more objective than losses. For priors there are formal principles (maximum entropy, transformation groups, marginalisation), while for loss functions there are none (p. 420).
- Utility via introspection (Savage, as described by Chernoff and Moses; Berger 1985 Ch. 2): find $r_3$ such that $r_3$ for sure is as good as a coin flip between $r_1$ and $r_2$. De Groot (1970) gives weak conditions guaranteeing a utility function exists. Jaynes finds the method no better than drawing a curve freehand, a "desperation move" (p. 420).
- Should the theory use only one function, the product? Jaynes decides no: (1) priors and losses play almost opposite roles; (2) inference with priors is more fundamental and loss theory needs more development (p. 420).
- Jaynes says validity rests on logical consistency. That real people do not always reason this way does not refute the theory, which is the normative goal (p. 420).
- Savage (1954) thinks the proverbs about looking before you leap and crossing a bridge when you come to it contradict each other. Jaynes thinks we obey both. Wald's plan of listing a decision for every conceivable data set is astronomically large, and Savage defends it. Jaynes takes the opposite view: only by delaying the decision until the actual data are known can complex problems be handled. Defensible inferences are post-data inferences, and Jaynes adds the proverb "Never make an irrevocable decision until you have to" (pp. 420–421).

**13.12.2 Loss functions in human society (pp. 421–422).** These are Jaynes's own opinions.
- People with similar priors get along, and radically different priors lead to conflict. For loss functions it is reversed: similar losses mean contention, different losses allow trade, as in insurance (p. 421).
- People know their priors fairly well, but in a dispute they may lose sight of their loss function. A labour mediator therefore explains to each side what its loss function is, since talk will not change priors (p. 421).
- Misjudging one's loss function is a major danger. Jaynes speculates that criminal behaviour may be poor reasoning leading to a wrongly perceived loss function. He cites Ramanujan's diet and Gödel's starvation as cases of failing to perceive one's own loss function (p. 422).
- Real problems exceed Wald's theory. For example, today's decision may influence tomorrow's state of nature, which points toward game theory or dynamic programming. Jaynes says treating this needs no departure from probability theory as logic, only a generalisation of what was done above (p. 422).
- Intuition often does well but can fail without mathematical understanding. Machol, Ladany and Morrison (1976) is cited for fallacies in sports strategy (p. 422).

**13.12.3 A new look at the Jeffreys prior (p. 423).**
- Jeffreys proposed prior density $\propto1/\alpha$ for a parameter known positive. Earlier, for a scale parameter, invariance under the scale group justified it (p. 423).
- New justification: with absolute loss $|\beta-\alpha|$, a constant $g(\alpha)$ demands constant absolute accuracy for all $\alpha$ in $0<\alpha<\infty$, which is too much for large $\alpha$. The median of the Jeffreys posterior is mathematically the optimal estimator for a uniform prior and loss $|\beta-\alpha|/\alpha$, i.e. constant percentage accuracy. So the $1/\alpha$ factor may be read as part of the loss function. This needs only $\alpha>0$, not that it be a scale parameter (p. 423).

**13.12.4 Decision theory is not fundamental (pp. 423–424).**
- It seems clear to Jaynes that there is something necessary and timeless in the inference methods, and he is convinced they cannot be substantively altered. Views of their foundation may change, e.g. toward desiderata of optimal information processing (Zellner, 1988). He holds that inference has fundamentally nothing to do with "randomness" or "chance" (p. 423).
- No such certainty holds for decision theory. Many applications need game theory or dynamic programming (state of nature chosen by another agent, or influenced by our decision, or several agents). Jaynes does not think these appropriate to scientific inference, since we do not play an adversary game against Nature (p. 424).
- Loss functions are less firmly grounded than priors, the opposite of the 1950s view. There are formal principles for priors but none for numerical losses, even economic ones, since the utility of money is ill-defined (p. 424).

**13.12.5 Another dimension? (pp. 424–425).**
- What we believe should not depend on what we want, but what we want may depend on what we know. Assigning a loss function is itself a description of prior information about consequences, so a change in priors could change the loss (p. 424).
- It therefore appears that value judgments need not enter as loss functions at all. Jaynes sees the way open to a future two-coordinate representation of a mental state, plausibility and value, instead of the one coordinate (plausibility) of present theory (pp. 424–425).
- Bayes explained probability through expectation, and this persisted in Wald and de Finetti (de Finetti's coherence in betting: choose probabilities so that you cannot be made a sure loser). Wald's and de Finetti's approaches share the premise that value judgments are in some way primary to inference. Jaynes dislikes basing probability on betting. A rule that is coherent but not consistent would give a well-posed question more than one "right" answer. This is for Jaynes another point in favour of Cox's logical-consistency approach (p. 425).

## Toy example (ours, not from the text)
Posterior over three parameter values: $P(\alpha=0)=0.4$, $P(\alpha=1)=0.35$, $P(\alpha=4)=0.25$.

Posterior mean: $0.35+0.25\cdot4=1.35$. Median: cumulative probability is 0.4 at $\alpha=0$ and 0.75 at $\alpha=1$, so the median is 1. Mode: 0.

Expected loss of candidate estimates $\beta$:
- Squared loss. $E[\alpha^2]=0.35+0.25\cdot16=4.35$ and $\mathrm{var}=4.35-1.35^2=2.5275$. Expected loss is $\mathrm{var}+(\beta-1.35)^2$. $\beta=1.35$: 2.5275. $\beta=1$: 2.65. $\beta=0$: 4.35. The mean wins.
- Absolute loss. $\beta=0$: $0.35\cdot1+0.25\cdot4=1.35$. $\beta=1$: $0.4\cdot1+0.25\cdot3=1.15$. $\beta=1.35$: $0.4\cdot1.35+0.35\cdot0.35+0.25\cdot2.65=1.325$. $\beta=4$: $0.4\cdot4+0.35\cdot3=2.65$. $\beta=1$ wins among these.
- 0–1 loss. Expected loss $=1-P(\alpha=\beta)$. $\beta=0$: 0.6. $\beta=1$: 0.65. $\beta=4$: 0.75. $\beta=1.35$: 1. The mode wins.

The same posterior gives three different "best" estimates because the loss differs. Scaling the 0–1 loss to $3+2\cdot$(loss) (i.e. $a=3$, $b=2$) multiplies every expected loss by 2 and adds 3, so the ranking is unchanged (13.45).

## Concepts
- [[bayes-theorem]] — turns prior and sampling distribution into posterior; here it appears from minimising averaged risk (p. 413)
- [[prior-distribution]] — g(α), first a weight on risk, then read as a prior density (pp. 413–414)
- [[posterior-distribution]] — expectation of the loss is always taken over it (p. 415)
- [[loss-function]] (new) — numbers L(D_i, θ_j) for the cost of decision D_i under state θ_j; equals −utility (pp. 400, 407)
- [[utility-function]] (new) — Bernoulli's "moral value" of money, taken ∝ log M; not to be taken literally at extremes (pp. 399–400)
- [[bayes-decision-rule]] (new) — choose the decision minimising expected loss over the posterior (p. 417)
- [[risk-function]] (new) — sampling-theory expected loss R_j(S) or R_α for fixed true state (pp. 408, 410)
- [[admissibility]] (new) — no strategy has risk ≤ for all j; Jaynes judges the notion flawed because it ignores prior information (pp. 408–409)
- [[complete-class-theorem]] (new) — Wald: admissible strategies are the (proper) Bayes strategies, per Jaynes's report (p. 415)
- [[minimax-criterion]] (new) — minimise the worst-case loss; treats Nature as an adversary (p. 407)
- [[mind-projection-fallacy]] (new) — treating probabilities as realities in Nature rather than descriptions of information (p. 411)
- [[maximum-likelihood-as-01-loss]] (new) — the posterior mode is optimal under 0–1 loss (p. 414)
- [[jeffreys-prior]] (new) — prior ∝ 1/α for positive α; reinterpreted as part of a percentage-accuracy loss (p. 423)
- [[kl-divergence]] — Jaynes's I(q;p) in the weatherman pay scheme (p. 403)
- [[entropy-hx]] — the pay-off ceiling B[log n − H] (p. 403)
- [[kelly-criterion-doubling-rate]] — maximise expected log fortune; Exercise 13.1 asks to show the best growth rate is H₀ − H (p. 402)
- [[frequentist-vs-bayesian-inference]] — the opposed views of what probability is; decision rules can apparently be derived from either (p. 418)
- [[principle-of-indifference-maximum-entropy]] — the entropy principle generalises indifference in step (2) (p. 418)
- [[cox-theorem]] — logical consistency as the foundation, preferred over betting coherence (p. 425)
- [[subjective-probability]] — de Finetti's coherence basis, which Jaynes rejects as foundation (p. 425)

## Canonical instances
- [[st-petersburg-paradox]] — infinite expected profit, but log utility gives fees of 9–21 francs (pp. 399–400)
- [[insurance-rationale]] — buying can serve both parties when utilities differ in curvature (pp. 400–401)
- [[honest-weatherman]] — log-score pay makes q = p optimal (pp. 402–403)
- [[exponential-posterior-estimators]] — mean, median and others β = 1, 0.693, 1.59, 2.025 times ⟨α⟩ (p. 416)
- [[constant-estimator-theta-5]] — an admissible rule that ignores the data (p. 409)
- [[savage-million-dollar-wager]] — counterexample to literal log utility (p. 400)

## Bridges (candidates)
- [same-math] weatherman log-pay expectation ↔ information-theory: cross-entropy / log scoring rule — expected pay B[log n + Σp_i log q_i] is maximised at q = p, a Gibbs-type inequality.
- [same-math] expected log fortune with tips ↔ information-theory: Kelly criterion — the growth-rate limit H₀ − H is the log-wealth/entropy link in the canon list.
- [same-math] posterior mean/median/mode as loss-minimisers ↔ bayesian: Bayes estimators — each is the minimiser of posterior expected loss.
- [structural-analogy] averaging risk over g(α) ↔ bayesian: hierarchical or marginal likelihood — a weighted average over unknowns turns an ill-posed pointwise problem into a solvable one.
- [structural-analogy] Jeffreys 1/α as percentage-accuracy loss ↔ information-theory: log-scale (relative) error — scale-invariant measurement.
- [metaphor] priors vs loss functions in social conflict ↔ economics: gains from trade between agents with different valuations.

## Questions this raises
- If only the product g·L matters, can any experiment distinguish "prior" from "loss"? What restores uniqueness, as Jaynes's maximum-entropy and transformation-group principles do for priors?
- Why is the 0–1 loss, which gives maximum likelihood, so common in practice if it is rarely a rational criterion?
- Jaynes says inference should not follow decision. Which pieces of a real pipeline (hypothesis-test thresholds, say) belong to the loss and which to the posterior?
- Can a two-coordinate (plausibility, value) calculus be built that keeps Cox-style consistency?

## Exercises worth doing
- Ex. 13.1 (p. 402) — show the maximum growth rate under log utility is H₀ − H; links utility to entropy — difficulty: medium
- Insurance exercise (p. 401) — from (13.5), show a poor man buys and a rich man does not unless his ⟨L⟩ is much greater than the company's — difficulty: easy
- Log(M+b) exercise (p. 402) — rework (13.7) with $\log(M+b)$ and suggest a value for $b$ — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 30 (the labels give printed numbers).
- **Likely misprint, (13.9):** the image shows $B[\log n-I(q;p)]$ with $I(q;p)\equiv\sum p_i\log(q_i)$. With that definition the sign is wrong: the expected pay from the stated rule is $B[\log n+\sum p_i\log q_i]$. This is consistent with (13.10) at $q=p$, which gives $B[\log n-H]$. I used the direct form, marked as an added step. The text also says $I$ is essentially (to within an additive constant) the relative entropy.
- Notation collision: in (13.31) $f(\beta)$ denotes a cubic, not the sampling density $f(x|\alpha)$.
- The text layer dropped angle brackets in places (e.g. ⟨L⟩, ⟨log(M−L)⟩). I restored them from the page images, which are clear.
- Several statements (criminal behaviour, Ramanujan, Gödel, "most violent criminals have very low intelligence") are Jaynes's personal opinions, not derived results. I reported them in his voice, compressed.
- Exercise 13.1 and the two "left to the reader" tasks are unsolved here, as required.
