---
id: murphy-2023-pml2/ch34-decision
work: murphy-2023-pml2
unit: "34 Decision making under uncertainty"
pages: 1105–1144
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Decision making under uncertainty (Murphy, PML2, ch. 34)

## L0 — One line
Once you have a posterior, the best action (or policy) is the one that minimises posterior expected loss; the chapter works this out for one-shot choices, A/B tests, bandits, MDPs and active learning.

## L1 — The gist (≤ 120 words)
How do we turn beliefs into actions? Statistical decision theory picks the policy with the lowest expected loss. Under Bayesian expectation this means minimising posterior expected loss. It gives the MAP estimate (the most probable value) for 0-1 loss and the posterior mean for squared loss. The chapter then applies this idea in several settings: influence diagrams and value of information, A/B testing with optimal test size, bandits (UCB, Thompson sampling, regret), Markov decision processes (Bellman equations, value iteration, policy iteration, linear programming), and active learning (uncertainty sampling, BALD, BatchBALD). It matters because it connects Bayesian inference to acting, including sequential choices and the choice of which data to collect.

**Prerequisites:** expectation and conditional probability; Bayes' rule for Gaussians and Beta–Bernoulli; basic entropy and mutual information; matrix–vector notation; derivative of a quadratic.

## L2 — Key ideas
- **Bayes-optimal decisions.** The optimal policy picks, for each observed $x$, the action with minimum posterior expected loss. Equivalently, if utility is defined as $U=-\ell$, it maximises expected utility (p. 1107).
- **Bayesian and frequentist risk agree on Bayes risk.** Swapping the order of integration shows the per-observation Bayesian rule also minimises the Bayes (integrated) risk. Wald's theorem says every admissible policy (one not strictly dominated by another) is Bayes for some, possibly improper, prior (p. 1107).
- **The loss function picks the summary.** 0-1 loss gives the MAP/mode, squared loss the posterior mean, Hamming loss (the number of wrong coordinates) the vector of posterior marginal maxima (MPM), and a general loss gives minimum Bayes risk decoding (pp. 1108–1110).
- **Value of information.** In an influence diagram (a graph with chance, decision and utility nodes), the value of perfect information (VPI) is the gain in maximum expected utility from observing a variable before acting. In the oil example, testing is worth doing if it costs less than the VPI (pp. 1112–1114).
- **A/B testing as a decision problem.** With Gaussian priors the optimal rule is simple, and in the symmetric case the expected total reward gives a closed-form optimal test size. More test data bring better decisions but an opportunity cost, an example of the exploration–exploitation tradeoff (pp. 1115–1119).
- **Bandits.** The exact Bayes-optimal policy is intractable in general. UCB (upper confidence bound: act greedily on optimistic reward estimates) and Thompson sampling (act greedily on one posterior sample) get sublinear regret (regret = reward lost relative to an oracle that knows the true rewards). Under mild assumptions, an asymptotic lower bound shows regret cannot grow slower than $\log T$ (pp. 1122–1128).
- **MDPs and planning.** Bellman's equations characterise the optimal value function, and value iteration (each update cuts the worst-case error to at most $\gamma$ times its size), policy iteration and linear programming solve a known MDP (pp. 1128–1137).
- **Active learning.** Acquisition functions (scores that rank candidate points: entropy, margin, QBC = query by committee, BALD = Bayesian active learning by disagreement) pick labels to query. BatchBALD scores a batch jointly so queries overlap less (pp. 1137–1144).

## L3 — Walkthrough

### 34.1 Statistical decision theory

**34.1.1 Basics (p. 1105).** An *agent* chooses an *action* $a\in\mathcal A$ given data $x$. The environment has an unknown *state of nature* $h\in\mathcal H$. A known *loss function* $\ell(h,a)$ gives the loss for action $a$ in state $h$. A *policy* (decision procedure) is $a=\delta(x)$. The goal is to minimise expected loss, the *risk*:
$$\delta^*(\cdot)=\arg\min_\delta R(\delta)\tag{34.1}$$
$$R(\delta)=\mathbb E\,[\ell(h,\delta(X))]\tag{34.2}$$
The open question is which distribution the expectation uses. Footnote 1: if $h$ is a parameter vector $\theta$, the action is an estimate $\hat\theta$ and $\delta$ is an *estimator*. The footnote says that in ML we usually focus on how well future observations are predicted, and a continued footnote on p. 1106 says performance is evaluated in data space (which can be measured) rather than parameter space (which cannot) (pp. 1105–1106).

**34.1.2 Frequentist decision theory (p. 1106).** Here $h$ is fixed but unknown and $X$ is random:
$$r(\delta|h)=\mathbb E_{p(x|h)}[\ell(h,\delta(x))]=\int p(x|h)\,\ell(h,\delta(x))\,dx\tag{34.3}$$
This cannot be computed because $h$ is unknown. Two escapes are given.
- Put a prior $\pi(h)$ on $h$ and use the *Bayes (integrated) risk*:
$$R_\pi(\delta)\triangleq\mathbb E_{p(h)}[r(\delta|h)]=\int \pi(h)p(x|h)\ell(h,\delta(x))\,dh\,dx\tag{34.4}$$
A minimiser is a *Bayes estimator*. It need not be built with Bayesian principles (p. 1106).
- Use the *maximum risk*, which gives the *minimax estimator*:
$$R_{\max}(\delta)=\max_h r(\delta|h)\tag{34.5}$$
$$\delta^*=\min_\delta\max_h r(\delta|h)\tag{34.6}$$
Minimax is hard to compute and very pessimistic. The author says minimax estimators are equivalent to Bayes estimators under a *least favourable prior*, since $\max_\pi R_\pi(\delta)=\max_h R(h,\delta)=R_{\max}(\delta)$. The author says that in most statistical situations (excluding game-theoretic ones) assuming nature is an adversary is not a reasonable assumption (p. 1106).

**34.1.3 Bayesian decision theory (pp. 1106–1107).** Now the data $x$ are a constant and $h$ is random. The *posterior expected loss* (posterior risk) of action $a$ is
$$\rho_\pi(a|x)\triangleq\mathbb E_{p_\pi(h|x)}[\ell(h,a)]=\int\ell(h,a)\,p_\pi(h|x)\,dh\tag{34.7}$$
with $p_\pi(h|x)\propto\pi(h)p(x|h)$. For an estimator, $\rho_\pi(\delta|x)=\rho_\pi(\delta(x)|x)=\mathbb E_{p_\pi(h|x)}[\ell(h,\delta(x))]$ (34.8). The optimal policy minimises posterior risk, so it only needs the best action for each observed $x$:
$$\delta^*(x)=\arg\min_\delta\rho_\pi(\delta|x)=\arg\min_{a\in\mathcal A}\rho_\pi(a|x)\tag{34.9}$$
With a *utility* $U(h,a)=-\ell(h,a)$ this is the *maximum expected utility principle*:
$$\delta^*(x)=\arg\max_{a\in\mathcal A}\mathbb E_h[U(h,a)]\tag{34.10}$$

*Intuition note.* Because the best rule decides separately for each observation, you do not need to optimise over whole rules. You only ask, for the data you actually have, which action hurts least on average under your posterior.

**34.1.4 Frequentist optimality of the Bayesian approach (p. 1107).** By Fubini's theorem (equivalently, the law of iterated expectation) the Bayes risk can be computed in either order:
$$R_B(\delta)=\mathbb E_{p(x)}[\rho(\delta|x)]=\mathbb E_{p(h|x)p(x)}[\ell(h,\delta(x))]\tag{34.11}$$
$$=\mathbb E_{p(h)}[r(\delta|h)]=\mathbb E_{p(h)p(x|h)}[\ell(h,\delta(x))]\tag{34.12}$$
(Figure 34.1 illustrates this.) So the rule that is best for each $x$ also minimises the Bayes risk, i.e. the author concludes that the Bayesian approach has optimal frequentist properties. Wald's theorem: any *admissible* policy (one not strictly dominated by another, footnote 2) is a Bayes policy for some, possibly improper, prior. The author says we "arguably lose nothing" by restricting to Bayesian procedures, provided the modelling assumptions are adequate. The Bayesian approach is also *constructive*: it tells you how to build the estimator, whereas the frequentist approach lets you use any estimator and then studies its properties (p. 1107).

**34.1.5 One-shot examples (pp. 1107–1111).**
- *Classification (p. 1108).* With $\mathcal H=\mathcal A=\{1,\dots,C\}$ and zero-one loss $\ell_{01}(y^*,\hat y)=\mathbb I(y^*\ne\hat y)$ (34.13–34.14), the posterior risk is $\rho(\hat y|x)=1-p(y^*=\hat y|x)$ (34.15). The optimal action is the posterior mode (MAP):
$$\delta(x)=\arg\max_{y}p(y|x)\tag{34.16}$$
Different costs for false positives and negatives are possible. A "reject" action gives selective prediction (Section 19.3.3).
- *Regression (pp. 1108–1109).* For scalar $h$ and action $y$, take squared loss $\ell_2(h,y)=(h-y)^2$ (34.17). Then
$$\rho(y|x)=\mathbb E[h^2|x]-2y\,\mathbb E[h|x]+y^2\tag{34.18}$$
$$\frac{\partial}{\partial y}\rho(y|x)=-2\mathbb E[h|x]+2y=0\Rightarrow\delta(x)=\mathbb E[h|x]=\int h\,p(h|x)\,dh\tag{34.19}$$
This is the posterior mean, also called the MMSE estimate.
- *Parameter estimation (p. 1109).* For $\mathcal H=\mathcal A=\Theta=\mathbb R^D$, quadratic loss gives the posterior mean and 0-1 loss gives the MAP: $\hat\theta=\arg\max_\theta p(\theta|\mathcal D)$ (34.20).
- *Discrete parameters (pp. 1109–1110).* 0-1 loss gives no partial credit. The *Hamming loss* $\ell(\theta,\hat\theta)=\sum_{d=1}^D\mathbb I(\theta_d\ne\hat\theta_d)$ (34.21) leads to the vector of max marginals (MPM, "maximizer of posterior marginals"):
$$\hat\theta=\Big[\arg\max_{\theta_d}\int_{\theta_{-d}}p(\theta|\mathcal D)\,d\theta_{-d}\Big]_{d=1}^D\tag{34.22}$$
It uses marginalisation plus maximisation, so it depends on the whole distribution. The author says this tends to be more robust than MAP.
 Example (Figure 34.2): a distribution on $\{0,1\}^3$. The state $L=(1,1,1)$ has probability $p_1$ and is the MAP. Four gray states have probability $p_2<p_1$, and three white states have probability 0. $L$ is isolated (all its neighbours have probability 0), while the gray states are connected and hold more total mass. Marginals: $p(\theta_j=0)=3p_2$ and $p(\theta_j=1)=p_2+p_1$. If $2p_2>p_1$, the MPM is $(0,0,0)$. The MPM is a *centroid estimator*: it minimises squared distance to the posterior mean, yet is (usually) a valid configuration, unlike the fractional mean (p. 1110).
- *Structured prediction (pp. 1110–1111).* In some problems (e.g. NLP, vision) the desired action is an output $y$ (e.g. a word sequence) that is probable given $x$ and also internally consistent. In the speech example, "How to wreck a nice beach" may fit the sounds word by word, but under a language-model prior "How to recognize speech" can be more likely overall (Figure 34.3). *Minimum Bayes risk decoding* picks
$$\hat y=\min_{\hat y\in\mathcal Y}\sum_{y\in\mathcal Y}p(y|x)\,\ell(y,\hat y)\tag{34.23}$$
(printed "min"; the intended operation is presumably argmin). Using $M$ posterior samples $y^m\sim p(y|x)$, ideally diverse, gives *empirical MBR*:
$$\hat y\approx\min_{y^i,\,i\in\{1..M\}}\sum_{j\in\{1..M\}}p(y^j|x)\,\ell(y^j,y^i)\tag{34.24}$$
It was applied to vision [Pre+17a] and to neural machine translation [Fre+22] (p. 1111).
- *Fairness (pp. 1111–1112).* Binary label $Y$, prediction $\hat Y$, sensitive attribute $S$. *Equal opportunity*: equal true-positive rates, $p(\hat Y{=}1|Y{=}1,S{=}0)=p(\hat Y{=}1|Y{=}1,S{=}1)$. *Equalised odds*: equal true-positive and false-positive rates across subgroups. *Statistical parity*: positive predictions unaffected by $S$, $p(\hat Y{=}1|S{=}0)=p(\hat Y{=}1|S{=}1)$. Many proposed definitions entail conflicting goals; the few common ones listed here can all be interpreted decision-theoretically (p. 1111).

*Intuition note.* The "best single answer" depends on what you penalise. Penalise any mistake equally and you report the most probable value. Penalise squared distance and you report the average. Penalise per-coordinate errors and you pick each coordinate's most probable value separately.

### 34.2 Decision (influence) diagrams (p. 1112)
An *influence diagram* extends a directed graphical model with *decision nodes* (rectangles), *utility nodes* (diamonds) and the usual *chance nodes* (ovals).

**34.2.1 Oil wildcatter (pp. 1112–1113).** Action $d=1$ means drill, $d=0$ means don't. State $o\in\{0,1,2\}$ = dry, wet, soaking. Prior $p(o)=[0.5,0.3,0.2]$. Utilities $U(d,o)$ (Figure 34.4a):

| | $o=0$ | $o=1$ | $o=2$ |
|---|---|---|---|
| $d=0$ | 0 | 0 | 0 |
| $d=1$ | −70 | 50 | 200 |

$$\mathrm{EU}(d)=\sum_{o=0}^2p(o)U(d,o)\tag{34.25}$$
$\mathrm{EU}(0)=0$ and $\mathrm{EU}(1)=20$, so
$$\mathrm{MEU}=\max\{\mathrm{EU}(0),\mathrm{EU}(1)\}=\max\{0,20\}=20\tag{34.26}$$
and the optimal action is to drill.

**34.2.2 Information arcs (pp. 1113–1114).** Add a noisy "sounding" $S$ with arc $O\to S$, and an *information arc* $S\to D$ (the sounding is seen before deciding; Figure 34.4b). Utility depends on $d$ and $o$, not on $s$. The sensor model $p(s|o)$ (rows $o=0,1,2$; columns $s=0,1,2$) is:

| | $s=0$ | $s=1$ | $s=2$ |
|---|---|---|---|
| $o=0$ | 0.6 | 0.3 | 0.1 |
| $o=1$ | 0.3 | 0.4 | 0.3 |
| $o=2$ | 0.1 | 0.4 | 0.5 |

$$\mathrm{EU}(d|s)=\sum_{o=0}^2p(o|s)U(o,d)\tag{34.27}$$
For $s=0$ the posterior is $p(o|s{=}0)=[0.732,0.219,0.049]$, giving $\mathrm{EU}(1|0)=-30.5$. For $s=1$, $\mathrm{EU}(1|1)=32.9$, and for $s=2$, $\mathrm{EU}(1|2)=87.5$. $\mathrm{EU}(0|s)=0$ in all cases. The optimal policy is: $s=0$: don't drill ($0); $s=1$: drill ($32.9); $s=2$: drill ($87.5). Then
$$\mathrm{MEU}=\sum_sp(s)\,\mathrm{EU}(d^*(s)|s)\tag{34.28}$$
with $p(s)=\sum_op(o)p(s|o)=[0.41,0.35,0.24]$, so
$$\mathrm{MEU}=0.41\times0+0.35\times32.9+0.24\times87.5=32.2\tag{34.29}$$
(as printed; see Reading notes). Figure 34.5 shows the decision tree.

**34.2.3 Value of information (p. 1114).** Add a test node $T$ (Figure 34.4c). Without the test, MEU = 20. With the test and optimal use of its outcome, MEU = 32.2. The gain, $12.2, is the *value of perfect information* (VPI), so do the test if it costs less than $12.2. In graph terms, with $G$ the base diagram of Figure 34.4b:
$$\mathrm{VPI}=\mathrm{MEU}(G+S\to D)-\mathrm{MEU}(G)\tag{34.30}$$
(pp. 1114–1115).

**34.2.4 Computing the optimal policy (p. 1115).** Modify variable elimination to work backwards from the final action, choosing each decision optimally given optimal later ones. For a simple chain structure such as an MDP, the result is equivalent to Bellman's equation (p. 1115).

*Intuition note.* Information is valuable only if it can change your action. VPI measures how much better you do on average when you may choose after seeing the data.

### 34.3 A/B testing (pp. 1115–1120)
Versions A (control) and B (treatment) are the "arms". An A/B test randomly assigns actions to subsets, measures accumulated reward, and picks the winner ("test and roll"). Two questions: the decision rule, and the group sizes $n_1,n_0$. Bigger samples give more confidence but have an *opportunity cost*, because testing uses actions that may not be best. This is an explore–exploit tradeoff (p. 1115). The analysis follows [FB19].

**34.3.1 Bayesian approach (p. 1115).** Rewards: $Y_{ij}\sim\mathcal N(\mu_j,\sigma_j^2)$, $i=1{:}n_j$, $j\in\{0,1\}$, with $\sigma_j^2$ known. Priors: $\mu_j\sim\mathcal N(m_j,\tau_j^2)$ with known prior parameters. (In practice, empirical Bayes.)

*34.3.1.1 Optimal policy (p. 1116).* For known $n_1,n_0$, the optimal rule deploys the arm with the larger posterior mean:
$$\pi^*(y_1,y_0)=\begin{cases}1&\mathbb E[\mu_1|y_1]\ge\mathbb E[\mu_0|y_0]\\0&\mathbb E[\mu_1|y_1]<\mathbb E[\mu_0|y_0]\end{cases}\tag{34.31}$$
The Gaussian posterior is $p(\mu_j|y_j,n_j)=\mathcal N(\mu_j|\hat m_j,\hat\tau_j^2)$ (34.32) with
$$1/\hat\tau_j^2=n_j/\sigma_j^2+1/\tau_j^2\tag{34.33}$$
$$\hat m_j/\hat\tau_j^2=n_j\bar y_j/\sigma_j^2+m_j/\tau_j^2\tag{34.34}$$
Posterior precision is prior precision plus $n_j$ units of measurement precision. In the fully symmetric case ($n_1=n_0$, equal $m,\tau,\sigma$) the rule is "pick the winner":
$$\pi^*(y_1,y_0)=\mathbb I\Big(\tfrac m{\tau^2}+\tfrac{\bar y_1}{\sigma^2}>\tfrac m{\tau^2}+\tfrac{\bar y_0}{\sigma^2}\Big)=\mathbb I(\bar y_1>\bar y_0)\tag{34.35}$$
In asymmetric cases one must account for different sample sizes and priors.

*34.3.1.2 Optimal sample size (pp. 1116–1117).* Population size $N$, no reuse of test subjects. The prior expected test-phase reward is
$$\mathbb E[R_{\text{test}}]=n_0m_0+n_1m_1\tag{34.36}$$
and the roll-phase reward under rule $\pi$ is
$$\mathbb E_\pi[R_{\text{roll}}]=\int_{\mu_1}\!\int_{\mu_0}\!\int_{y_1}\!\int_{y_0}(N-n_1-n_0)\big(\pi\mu_1+(1-\pi)\mu_0\big)\,p(y_0|\mu_0)p(y_1|\mu_1)p(\mu_0)p(\mu_1)\,dy_0dy_1d\mu_0d\mu_1\tag{34.37–34.38}$$
For $\pi=\pi^*$ "one can show" that, with $\phi,\Phi$ the Gaussian pdf and cdf and $e=m_0-m_1$,
$$\mathbb E[R_{\text{roll}}]=(N-n_1-n_0)\Big(m_1+e\,\Phi(\tfrac ev)+v\,\phi(\tfrac ev)\Big)\tag{34.39}$$
$$v=\sqrt{\frac{\tau_1^4}{\tau_1^2+\sigma_1^2/n_1}+\frac{\tau_0^4}{\tau_0^2+\sigma_0^2/n_0}}\tag{34.40}$$
In the symmetric case this becomes
$$\mathbb E[R_{\text{roll}}]=\underbrace{(N-2n)m}_{R_a}+\underbrace{(N-2n)\frac{\sqrt2\,\tau^2}{\sqrt\pi\sqrt{2\tau^2+\frac2n\sigma^2}}}_{R_b}\tag{34.41}$$
$R_a$ is the reward expected before learning anything. $R_b$ is the reward from picking the better arm. Writing $R_b=(N-2n)R_i$, the incremental gain $R_i$ grows with $n$, but it applies to fewer people ($N-2n$). Adding (34.36) and (34.41):
$$\mathbb E[R]=Nm+(N-2n)\frac{\sqrt2\,\tau^2}{\sqrt\pi\sqrt{2\tau^2+\frac2n\sigma^2}}\tag{34.42}$$
Setting $\frac{d}{dn^*}\mathbb E[R]=0$ gives, with $u^2=\sigma^2/\tau^2$,
$$n^*=\sqrt{\tfrac N4u^2+\big(\tfrac34u^2\big)^2}-\tfrac34u^2\;\le\;\sqrt N\,\frac{\sigma}{2\tau}\tag{34.43}$$
So $n^*$ increases with noise $\sigma$ and decreases with $\tau$. A prior belief that the effect size $\delta=\mu_1-\mu_0$ is large means less data are needed (p. 1117).

*Intuition note.* More testing buys better decisions but shrinks the number of people who get the winning arm. The best $n$ balances the two. It is large when measurements are noisy and small when the arms are expected to differ a lot.

*34.3.1.3 Regret (pp. 1117–1118).* *Regret* is the expected reward under perfect information (PI) about the best action, minus the policy's expected reward. For $\mu_j\sim\mathcal N(m,\tau^2)$:
$$\mathbb E[R|PI]=N\Big(m+\frac\tau{\sqrt\pi}\Big)\tag{34.44}$$
The regret of the optimal policy is
$$\mathbb E[R|PI]-(\mathbb E[R_{\text{test}}|\pi^*]+\mathbb E[R_{\text{roll}}|\pi^*])=N\frac\tau{\sqrt\pi}\Big(1-\frac\tau{\sqrt{\tau^2+\sigma^2/n^*}}\Big)+\frac{2n^*\tau^2}{\sqrt\pi\sqrt{\tau^2+\sigma^2/n^*}}\tag{34.45}$$
This is $O(\sqrt N)$, which is optimal for this problem [AG13] (p. 1118).

*34.3.1.4 Expected error rate (p. 1118).* *Best arm identification* asks whether $\delta>0$, which is a hypothesis test. The author argues this is "arguably the wrong objective": it is usually not worth paying for a large sample to be sure about a small $\delta$. Maximising total reward is better. Still, in the symmetric case the chance of picking the wrong arm, for known $\mu$, is
$$\Pr(\pi(y_1,y_0)=1|\mu_1<\mu_0)=\Pr(Y_1-Y_0>0|\mu_1<\mu_0)=1-\Phi\Big(\frac{\mu_1-\mu_0}{\sigma\sqrt{1/n_1+1/n_0}}\Big)\tag{34.46}$$
Averaging over the prior, the expected error rate is
$$\text{Prob. error}=\frac14-\frac1{2\pi}\arctan\Big(\frac{\sqrt2\,\tau}\sigma\sqrt{\frac{n_1n_0}{n_1+n_0}}\Big)\tag{34.47}$$
It falls with $n_1,n_0$ and with $\tau$ and rises with $\sigma$. A policy minimising classification error also maximises expected reward, but may choose an overly large sample because it ignores the size of $\delta$ (p. 1118).

**34.3.2 Example: website testing (pp. 1119–1120).** Click data are Bernoulli, $y_{ij}\sim\mathrm{Ber}(\mu_j)$, with a Beta prior. The exact solution is harder, so the Gaussian approximation is used: $\bar y_{ij}\sim\mathcal N(\mu_j,\sigma^2)$, $\mu_j\sim\mathcal N(m,\tau^2)$, with $m=\frac\alpha{\alpha+\beta}$, $\tau^2=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$, $\sigma^2=m(1-m)$. [FB19] fitted a hierarchical model to about 2000 earlier A/B tests, giving $\mu_j\sim\mathcal N(m=0.68,\tau=0.03)$, i.e. small expected effects (the text says $\mathbb E|\mu_1-\mu_0|=0.023$). With $N=100{,}000$:

| Quantity | Value |
|---|---|
| Optimal $n_1^*=n_0^*$ from (34.43) | 2284 |
| $\mathbb E[R_{\text{test}}]$ | 3106 |
| $\mathbb E[R_{\text{roll}}]$ | 66,430 |
| Total reward | 69,536 |
| Expected error rate | 10% |

Figure 34.6a: reward rises sharply up to $n^*$ and falls more slowly after, so a slightly too-large test is better than one too small by the same amount. With a heavy-tailed model, [Aze+20] find many smaller tests better. Figure 34.6b: larger-than-optimal tests reduce error only marginally. When $\mu_1-\mu_0$ is small, error is hard to reduce but also matters little. The author says this explains why frequentist hypothesis-testing designs may recommend much larger samples than necessary (pp. 1119–1120).

### 34.4 Contextual bandits (pp. 1120–1128; co-authored with Lihong Li)
Letting the decision maker act, see reward $r_t$, and adapt at $t+1$ turns a one-stage problem into a *sequential decision problem*. The simplest kind is a *bandit problem* (p. 1120).

**34.4.1 Types of bandit (pp. 1120–1121).**
- *Multi-armed bandit (MAB).* At each step the agent picks $a_t\sim\pi_t$ and gets $r_t\sim p_R(a_t)$ with mean $R(a)$. Think of $K$ slot machines. The setting described is the stochastic bandit; footnote 4 notes that reward (and possibly state) could instead be chosen adversarially (an adversarial bandit).
- *Contextual bandit.* A context $s_t$ is drawn by a process independent of the agent's actions. The policy is $a_t\sim\pi_t(a_t|s_t)$ and the reward $r_t\sim p_R(r_t|s_t,a_t)$ with mean $R(s,a)$. The agent updates its policy from $\mathcal D_{1:t}$, $\mathcal D_t=(s_t,a_t,r_t)$.
- *Finite-horizon objective:* maximise cumulative reward $J\triangleq\sum_{t=1}^T\mathbb E[r_t]$ (34.48), accrued even while learning ("earning while learning").
- *Infinite horizon* needs a discount $0<\gamma<1$:
$$J\triangleq\sum_{t=1}^\infty\gamma^{t-1}\mathbb E[r_t]\tag{34.49}$$
$1-\gamma$ can be read as the per-step termination probability. Equivalently
$$J=\sum_{t=1}^\infty\gamma^{t-1}\mathbb E\Big[\sum_{a=1}^KR_a(s_t,a_t)\Big],\quad R_a(s_t,a_t)=\begin{cases}R(s_t,a)&a_t=a\\0&\text{otherwise}\end{cases}\tag{34.50–34.51}$$
- *Multiple plays:* choose $M\le K$ arms; $r_t=\sum_aR_a(s_t,\mathbf a_t)$ with $R_a=R(s_t,a)$ if $a\in\mathbf a_t$, else 0 (34.52–34.53). This models resource allocation.
- *Restless bandit:* each arm has its own state $s_t^a$ that evolves whether or not the arm is chosen, $r_t=\sum_aR_a(s_t^a,\mathbf a_t)$ (34.54), with $s_t^a\sim p(s_t^a|s^a_{1:t-1})$, often Markovian (p. 1121).

**34.4.2 Applications (p. 1122).** Online advertising: the state is features of the page, the action is which ad to show, and the reward is a click (CTR). Clinical trials: the state is patient features, the action is the treatment, and the reward is a cure. An alternative goal is best-arm identification (p. 1122).

**34.4.3 Exploration–exploitation (p. 1122).** The agent must try state–action pairs (exploration) to learn $R(s,a)$ before exploiting. Exploiting a wrong model too early yields suboptimal data and a negative feedback loop (Figure 34.7). This differs from supervised learning, where data are iid from a fixed distribution (p. 1122).

**34.4.4 The optimal solution (pp. 1122–1124).** The *belief state* $b_t=p(\theta|h_t)$, with $h_t=\{s_{1:t-1},a_{1:t-1},r_{1:t-1}\}$, is a finite sufficient statistic of the history. It updates deterministically: $b_t=\text{BayesRule}(b_{t-1},a_t,r_t)$ (34.55), equivalently $p(b_t|b_{t-1},a_t,r_t)=\mathbb I(b_t=\text{BayesRule}(b_{t-1},a_t,r_t))$ (34.59).
- *Beta–Bernoulli example.* A context-free Bernoulli bandit has $p_R(r|a)=\mathrm{Ber}(r|\mu_a)$, $\mu_a=R(a)$, with factored prior $p_0(\theta)=\prod_a\mathrm{Beta}(\mu_a|\alpha_0^a,\beta_0^a)$ (34.56). The posterior (as printed) is
$$p(\theta|\mathcal D_t)=\prod_a\mathrm{Beta}\big(\mu_a\,|\,\alpha_0^a+N_t^0(a),\ \beta_0^a+N_t^1(a)\big),\qquad N_t^r(a)=\sum_{s=1}^{t-1}\mathbb I(a_s=a,r_s=r)\tag{34.57–34.58}$$
(see Reading notes on the placement of $N^0,N^1$). Figure 34.8 shows this for two arms.
- Gaussian bandit: use conjugate results (Section 3.4.3). Linear-regression bandit: Bayesian linear regression (Section 15.2). Logistic bandit: Bayesian logistic regression (Section 15.3.5). Neural bandit: harder, but e.g. the extended Kalman filter can be applied (p. 1124).
- The predicted reward is $p(r_t|b_t)=\int p_R(r_t|s_t,a_t;\theta)p(\theta|b_t)d\theta$ (34.60). This is a *belief-state MDP*.
- For context-free bandits with finitely many arms, dynamic programming gives the optimal policy of this MDP; it is called the *Gittins index*. For general contextual bandits, the optimal policy is intractable [PT87], so approximations are needed (p. 1124).

**34.4.5 Upper confidence bounds (UCB) (pp. 1124–1126).** Principle: *optimism in the face of uncertainty*. Keep an optimistic estimate $\tilde R_t(s,a)\ge R(s,a)$ with high probability and act greedily:
$$a_t=\arg\max_a\tilde R_t(s_t,a)\tag{34.61}$$
The optimism $\tilde R_t-R$ acts as an exploration bonus and typically shrinks over time. With properly built estimates, UCB has near-optimal regret in many bandit variants [LS19].
- *Frequentist.* A concentration inequality gives $|\hat R_t-R_t|\le\delta_t(s,a)$ and $\tilde R_t=\hat R_t+\delta_t$. For the Bernoulli bandit, the MLE is
$$\hat\mu_t(a)=\frac{N_t^1(a)}{N_t(a)}=\frac{N_t^1(a)}{N_t^0(a)+N_t^1(a)},\qquad N_t(a)=\sum_{s=1}^{t-1}\mathbb I(a_t=a)\tag{34.62–34.63}$$
and the Chernoff–Hoeffding inequality gives $\delta_t(a)=c/\sqrt{N_t(a)}$ for a suitable constant $c$, so $\tilde R_t(a)=\hat\mu_t(a)+c/\sqrt{N_t(a)}$ (34.64).
- *Bayesian.* With a Beta prior the posterior mean is $\hat\mu_t(a)=\alpha_t^a/(\alpha_t^a+\beta_t^a)$ and the posterior standard deviation is approximately
$$\hat\sigma_t(a)=\sqrt{\mathbb V[\mu(a)|h_t]}\approx\sqrt{\frac{\hat\mu_t(a)(1-\hat\mu_t(a))}{N_t(a)}}\tag{34.65}$$
For a Gaussian bandit with an uninformative conjugate prior, the posterior mean is the empirical mean and the posterior sd is the standard error $\hat\sigma_t(a)/\sqrt{N_t(a)}$. Then
$$\tilde R_t(a)=\hat\mu_t(a)+c\,\hat\sigma_t(a)\tag{34.66}$$
where $c$ controls how greedy the policy is. The author notes this is similar to the frequentist form but more general (p. 1125).
- Figure 34.9: three Gaussian posteriors with means $\mu(a)$ and bars $c\sigma(a)$ (p. 1126).

**34.4.6 Thompson sampling (p. 1126).** Also called probability matching. The policy plays arm $a$ with probability $p_a$ that $a$ is optimal:
$$p_a=\Pr(a=a_*|s_t,h_t)=\int\mathbb I\Big(a=\arg\max_{a'}R(s_t,a';\theta)\Big)p(\theta|h_t)\,d\theta\tag{34.67}$$
Implement it with one posterior sample $\tilde\theta_t\sim p(\theta|h_t)$ and act greedily:
$$a_t=\arg\max_{a'}R(s_t,a';\tilde\theta_t)\tag{34.68}$$
This chooses actions with exactly probability $p_a$ (34.69). It explores while the posterior is uncertain and exploits as uncertainty falls. It "can be shown to achieve optimal (logarithmic) regret" and is easy to implement. Example (Figure 34.10): linear-Gaussian bandit with $s_t=(1,t,t^2)$ and $R(s_t,a)=w_a^\top s_t$. The weights are $w_0=(-5,2,0.5)$, $w_1=(0,0,0)$, $w_2=(5,-1.5,-1)$ and $\sigma^2=1$. So arm 0 starts bad and improves, arm 1 is useless, and arm 2 starts good and worsens. With a conjugate Gaussian–gamma prior, Thompson sampling quickly drops arm 1, pulls arm 2 more at first, then switches to arm 0 (p. 1126).

**34.4.7 Regret (pp. 1127–1128).** The oracle policy $\pi_*$ knows the true reward function, and is in general better than the Bayes-optimal policy. Per-step regret:
$$l_t\triangleq\mathbb E_{p(s_t)}[R(s_t,\pi_*(s_t))]-\mathbb E_{\pi_t(a_t|s_t)p(s_t)}[R(s_t,a_t)]\tag{34.70}$$
The *simple regret* is $l_T$; optimising it leads to the problem called *pure exploration*. The usual measure is cumulative regret
$$L_T\triangleq\mathbb E\Big[\sum_{t=1}^Tl_t\Big]\tag{34.71}$$
For bounded rewards $L_T$ is at most linear in $T$. If the policy converges to the optimal one, $L_T=o(T)$. For a context-free bandit,
$$L_T=\mathbb E\Big[\sum_{t=1}^TR_*-R(a_t)\Big]=\sum_{a}\mathbb E[N_{T+1}(a)](R_*-R(a))=\sum_a\mathbb E[N_{T+1}(a)]\Delta_a\tag{34.72}$$
with gap $\Delta_a=R_*-R(a)$. Under-exploring (settling on a suboptimal arm) or over-exploring both give linear regret. Thompson sampling has $O(\sqrt{KT\log T})$ regret [RR14] (Figure 34.10c). The author says both UCB and Thompson sampling are essentially not improvable. The lower bound of [LR85] (under mild assumptions not given) is
$$\liminf_{T\to\infty}L_T\ge\log T\sum_{a:\Delta_a>0}\frac{\Delta_a}{D_{\mathrm{KL}}(p_R(a)\,\|\,p_R(a_*))}\tag{34.73}$$
so the best achievable is logarithmic growth. The reason: similar reward distributions need more samples to tell apart, since estimation error decays like $1/\sqrt N$ (p. 1128).

*Intuition note.* A bandit agent pays for every wrong pull. Stopping too early locks in a mistake forever, and exploring forever wastes pulls. UCB and Thompson sampling both explore more when they are more unsure, so exploration tends to fade as evidence grows.

### 34.5 Markov decision problems (pp. 1128–1133)
An MDP lets the state change in response to actions. It is the foundation of reinforcement learning (Chapter 35) (p. 1128).

**34.5.1 Basics (pp. 1128–1129).** An MDP is a tuple $\langle\mathcal S,\mathcal A,p,p_R,p_0\rangle$: states, actions, transition model, reward model, initial state distribution. Start with $s_0\sim p_0$. At each $t\ge0$ the agent sees $s_t$, takes $a_t\sim\pi(s_t)$, gets $r_t\sim p_R(s_t,a_t,s_{t+1})$, and the state moves to $s_{t+1}\sim p(s_t,a_t)$. One such step is a *transition* $(s_t,a_t,r_t,s_{t+1})$. A trajectory of length $T$ has probability
$$p(\tau)=p_0(s_0)\prod_{t=0}^{T-1}\pi(a_t|s_t)\,p(s_{t+1}|s_t,a_t)\,p_R(r_t|s_t,a_t,s_{t+1})\tag{34.74}$$
The reward function marginalises the next state:
$$R(s,a)\triangleq\mathbb E_{p(s'|s,a)}\big[\mathbb E_{p_R(r|s,a,s')}[r]\big]\tag{34.75}$$
This loses no generality for total expected reward, so an MDP is often $\langle\mathcal S,\mathcal A,p,R,p_0\rangle$. With finite sets we get a *tabular representation* and a finite state machine (Figure 34.11: 3 states, 2 actions). Control theory uses different names: plant = environment, controller = agent, state $x_t$, action $u_t$, cost $c_t$ for reward. It tends to focus on provable optimality under strong assumptions such as linearity, whereas RL uses heuristics on harder problems (p. 1129).

**34.5.2 POMDPs (p. 1130).** The agent sees only noisy observations $o_t\sim p(\cdot|s_t,a_t)$. The policy maps history $h_t=(a_1,o_1,\dots,a_{t-1},o_t)$ to actions, $a_t\sim\pi(h_t)$ (Figure 34.12). MDPs are the special case $o_t=s_t$. POMDPs are much harder. The optimal approach computes the belief state $b_t=p(s_t|h_t)$ and a belief-state MDP, but solving it is intractable. A common approximation uses the last few observations $o_{t-k:t}$ as if they were the state (p. 1130).

**34.5.3 Episodes and returns (pp. 1130–1131).** A *continuing task* may run forever. An *episodic task* ends on entering a terminal (absorbing) state, where $s$ is absorbing if the next state is always $s$ with reward 0. An episodic MDP can be turned into a continuing one by making the transition from absorbing states equal $p_0$. A fixed known $T$ gives a *finite horizon problem*. The *return* (reward-to-go) with discount $\gamma\in[0,1]$ is
$$G_t\triangleq r_t+\gamma r_{t+1}+\dots+\gamma^{T-t-1}r_{T-1}\tag{34.76}$$
$$=\sum_{k=0}^{T-t-1}\gamma^kr_{t+k}=\sum_{j=t}^{T-1}\gamma^{j-t}r_j\tag{34.77}$$
$$G_t=r_t+\gamma(r_{t+1}+\gamma r_{t+2}+\cdots)=r_t+\gamma G_{t+1}\tag{34.78}$$
with $G_t=0$ for $t\ge T$ in episodic tasks. The discount (i) keeps the return finite for $T=\infty$ if $\gamma<1$ and rewards are bounded, and (ii) favours short-term rewards. If $\gamma=0$ the agent is *myopic*; if $\gamma$ is too small the agent is too greedy. For finite horizons one can use $\gamma=1$ (p. 1131).

**34.5.4 Value functions (pp. 1131–1132).** For policy $\pi$:
$$V_\pi(s)\triangleq\mathbb E_\pi[G_0|s_0=s]=\mathbb E_\pi\Big[\sum_{t=0}^\infty\gamma^tr_t\,\Big|\,s_0=s\Big]\tag{34.79}$$
$$Q_\pi(s,a)\triangleq\mathbb E_\pi[G_0|s_0=s,a_0=a]=\mathbb E_\pi\Big[\sum_{t=0}^\infty\gamma^tr_t\,\Big|\,s_0=s,a_0=a\Big]\tag{34.80}$$
$$A_\pi(s,a)\triangleq Q_\pi(s,a)-V_\pi(s)\tag{34.81}$$
$A_\pi$ (advantage) can be positive or negative, and $\mathbb E_{\pi(a|s)}[A_\pi(s,a)]=0$ because $V_\pi(s)=\mathbb E_{\pi(a|s)}[Q_\pi(s,a)]$ (pp. 1131–1132).

**34.5.5 Optimal value functions and policies (p. 1132).** $\pi_*$ is optimal if $V_{\pi_*}\ge V_\pi$ for all $s$ and all $\pi$. Optimal policies may be several, but they share $V_*,Q_*$. Any finite MDP has at least one deterministic optimal policy [Put94]. *Bellman's optimality equations:*
$$V_*(s)=\max_aR(s,a)+\gamma\,\mathbb E_{p(s'|s,a)}[V_*(s')]\tag{34.82}$$
$$Q_*(s,a)=R(s,a)+\gamma\,\mathbb E_{p(s'|s,a)}\Big[\max_{a'}Q_*(s',a')\Big]\tag{34.83}$$
Conversely, the optimal value functions are the only solutions of these equations. The gap between the two sides is the *Bellman error (residual)*. An optimal policy follows by acting greedily:
$$\pi_*(s)=\arg\max_aQ_*(s,a)\tag{34.84}$$
$$=\arg\max_a\big[R(s,a)+\gamma\,\mathbb E_{p(s'|s,a)}[V_*(s')]\big]\tag{34.85}$$
*Policy optimisation* solves for $V_*,Q_*,\pi_*$; *policy evaluation* solves for $V_\pi,Q_\pi$ using Bellman equations with $\max_a$ replaced by $\mathbb E_{\pi(a|s)}$. The greedy action is easy for small finite $\mathcal A$. For continuous actions the text mentions optimising one dimension at a time, the cross-entropy method (QT-Opt), mixed integer programming (CAQL), or training a policy to amortise the argmax (p. 1132).

*34.5.5.1 Example (p. 1133, Figure 34.13).* A 1-d grid world has non-absorbing states $s_1,s_2,s_3$ and absorbing end states $S_{T1}$ (top) and $S_{T2}$ (bottom, reward 1 on entering). The actions are Up and Down, so Down is optimal everywhere. Optimal $Q_*$ values (rows $s_1,s_2,s_3$; columns Up, Down) read from the figure:

| $\gamma$ | $s_1$ | $s_2$ | $s_3$ |
|---|---|---|---|
| 0 | (0, 0) | (0, 0) | (0, 1.0) |
| 1 | (0, 1.0) | (1.0, 1.0) | (1.0, 1.0) |
| 0.9 | (0, 0.81) | (0.73, 0.9) | (0.81, 1.0) |

With $\gamma=0$ the agent is completely myopic. With $\gamma=1$ it is infinitely far-sighted, and the Q-values give no short-term guidance (both actions in $s_2$ tie). $\gamma=0.9$ encourages the shortest path. Choosing $\gamma$ is the designer's job, like designing the reward (p. 1133).

### 34.6 Planning in an MDP (pp. 1134–1137)
*Planning* means computing an optimal policy when the model is known. It uses dynamic programming (DP) and linear programming (LP). The *curse of dimensionality* makes exact methods intractable for large product state spaces, so approximate DP/LP is used (p. 1134).

**34.6.1 Value iteration (pp. 1134–1135).** From $V_0$, iterate the *Bellman backup* (right side of (34.82) with $V_k$ in place of $V_*$):
$$V_{k+1}(s)=\max_a\Big[R(s,a)+\gamma\sum_{s'}p(s'|s,a)V_k(s')\Big]\tag{34.86}$$
The update is a contraction (the author says this can be verified):
$$\max_s|V_{k+1}(s)-V_*(s)|\le\gamma\max_s|V_k(s)-V_*(s)|\tag{34.87}$$
so $V_k\to V_*$, and one can often stop when $V_k$ is close enough, since the greedy policy is then near optimal. For shortest-path problems the author uses an episodic MDP with $R(s,a)=-1$ except at absorbing goal states. *Real-time DP (RTDP)* does the backup $V(s)\leftarrow\max_a\mathbb E_{p(s'|s,a)}[R(s,a)+\gamma V(s')]$ only along visited states. It computes a *partial policy* for reachable states, and is a form of asynchronous value iteration (pp. 1134–1135).

**34.6.2 Policy iteration (pp. 1135–1136).** Alternate *policy evaluation* and *policy improvement* over deterministic policies. Let $v(s)=V_\pi(s)$, $r(s)=\sum_a\pi(a|s)R(s,a)$ and $\mathbf T(s'|s)=\sum_a\pi(a|s)p(s'|s,a)$. Evaluation solves a linear system in $|\mathcal S|$ unknowns:
$$v=r+\gamma\mathbf Tv,\qquad v=(\mathbf I-\gamma\mathbf T)^{-1}r\tag{34.88}$$
(or iterate $v_{t+1}=r+\gamma\mathbf Tv_t$). Improvement takes the greedy policy $\pi'(s)=\arg\max_a\{R(s,a)+\gamma\mathbb E[V_\pi(s')]\}$. Proof that $V_{\pi'}\ge V_\pi$: the definition of $\pi'$ gives $r'+\gamma\mathbf T'v\ge r+\gamma\mathbf Tv=v$ (equality by Bellman). Repeatedly substituting,
$$v\le r'+\gamma\mathbf T'v\le r'+\gamma\mathbf T'(r'+\gamma\mathbf T'v)\le\cdots\tag{34.89}$$
$$=(\mathbf I+\gamma\mathbf T'+\gamma^2\mathbf T'^2+\cdots)r'=(\mathbf I-\gamma\mathbf T')^{-1}r'=v'\tag{34.90}$$
(added step: each substitution keeps the inequality because $\gamma\mathbf T'$ has nonnegative entries.) The sequence is
$$\pi_0\xrightarrow{E}V_{\pi_0}\xrightarrow{I}\pi_1\xrightarrow{E}V_{\pi_1}\cdots\xrightarrow{I}\pi_*\xrightarrow{E}V_*\tag{34.91}$$
It stops when the policy is greedy for its own value function, which means it is optimal. There are at most $|\mathcal A|^{|\mathcal S|}$ deterministic policies and each iteration strictly improves, so it terminates in finitely many steps. PI evaluates to convergence between improvements; VI does one evaluation step per improvement step. *Generalized policy improvement (GPI)* mixes the two in any order, and converges once the policy is greedy for its own value function. *Policy improvement theorem* [SB18]: if $Q_\pi(s,\pi'(s))\ge V_\pi(s)$ for deterministic $\pi,\pi'$, then $V_{\pi'}\ge V_\pi$. It is a strict improvement if the inequality is strict in some state. Policy evaluation averages over actions by $\pi$; value iteration takes the max over actions (Figure 34.14) (p. 1136).

**34.6.3 Linear programming (pp. 1136–1137).** Primal form (as printed; see Reading notes), with $p_0(s)>0$ for all $s$:
$$\min_V\sum_sp_0(s)V(s)\ \text{ s.t. }\ V(s)\ge R(s,a)+\gamma\sum_{s'}p(s'|s,a)V(s),\ \forall(s,a)\tag{34.92}$$
Any feasible $V$ is optimistic ($V\ge V_*$) [Put94]. Minimising pushes it down to $V_*$, and any action making the constraint tight in $s$ is optimal there. Dual form:
$$\max_{d\ge0}\sum_{s,a}d(s,a)R(s,a)\ \text{ s.t. }\ \sum_ad(s,a)=(1-\gamma)p_0(s)+\gamma\sum_{\bar s,\bar a}p(s|\bar s,\bar a)d(\bar s,\bar a),\ \forall s\tag{34.93}$$
Any feasible nonnegative $d$ is the normalised occupancy distribution of the policy $\pi_d(a|s)=d(s,a)/\sum_{a'}d(s,a')$:
$$d(s,a)=(1-\gamma)\sum_{t=0}^\infty\gamma^t\,p\big(s_t=s,a_t=a\,|\,s_0\sim p_0,a_t\sim\pi_d(s_t)\big)\tag{34.94}$$
So the dual objective is the average per-step reward under $d$, and $\pi_*(a|s)=d_*(s,a)/\sum_{a'}d_*(s,a')$. Both LPs have many variables or constraints, so approximations are needed (p. 1137).

*Intuition note.* Because $V_*$ obeys a one-step recursion, a problem that sums infinitely many rewards can be solved by repeated local backups. Each backup cuts the worst-case error to at most $\gamma$ times its previous size.

### 34.7 Active learning (pp. 1137–1144; co-authored with Zeel B Patel)
In *active learning* (AL) the agent chooses which data to label so as to learn the predictive function with as little labeled data as possible. Figure 34.15 (3-class logistic regression): initial accuracy 0.818; after 11 random points 0.848; after 11 margin-sampled points 0.969 (p. 1137).

**34.7.1 Scenarios (p. 1138).** *Membership query synthesis*: the agent generates any query $x$ and asks an oracle for $y=f(x)$ (mostly theoretical). *Stream-based selective sampling*: for each incoming $x_t$, decide whether to ask for the label (mostly theoretical). *Pool-based sampling*: an unlabeled pool is available. An *acquisition function* scores candidates, and the chosen one is labeled, the model updated, and the loop repeated. This is the widely used setting and the one the chapter follows (p. 1138).

**34.7.2 Relation to BO and bandits (pp. 1138–1139).** Table 34.1 compares the goals:

| Problem | Goal | Action space |
|---|---|---|
| Active learning | $\arg\min_f\mathbb E_{p(x)}[\ell(f^*(x),f(x))]$ | choose $x$ at which to get $y=f^*(x)$ |
| Bayesian optimisation | $\arg\max_{x}f^*(x)$ | choose $x$ at which to evaluate $f^*(x)$ |
| Contextual bandits | $\arg\max_\pi\mathbb E_{p(x)\pi(a|x)}[R^*(x,a)]$ | choose $a$ at which to evaluate $R^*(x,a)$ |

In bandits the agent chooses only the action, not the state, so it has partial control over where the reward function is evaluated. All three need exploration–exploitation. A common approach is to model $p(f|\mathcal D_{1:t})$ (e.g. with a Gaussian process) and pick $x_{t+1}=\arg\max_x\alpha(x)$. BO often uses probability of improvement; AL for regression can use posterior predictive variance. AL queries "all over the place", while BO "zooms in" on promising regions (Figure 34.16) (p. 1139).

**34.7.3 Acquisition strategies (pp. 1139–1141).**
- *Uncertainty sampling (p. 1139).* Pick the example the model is most unsure about. For class probabilities $p_n=[p(y=c|x_n)]_{c=1}^C$ and uncertainty $U_n=\alpha(p_n)$:
 – entropy: $\alpha(p)=-\sum_cp_c\log p_c$;
 – margin: $\alpha(p)=p_2-p_1$ ($p_1,p_2$ the top two class probabilities);
 – least confident: $\alpha(p)=1-p_{c^*}$.
 Margin sampling often works best [Chu+19]. In Figure 34.17 (three MNIST candidates), least confident scores are 0.76, 0.75, 0.53 (pick the first). Entropy scores are 1.63, 1.78, 0.89 (pick the second). Margin gaps are 0.0303, 0.0236, 0.0002 (pick the third) (pp. 1139–1140).
- *Query by committee, QBC (pp. 1140–1141).* For models that give only point predictions (e.g. SVMs), form an ensemble of $K$ diverse members. Let $v_{nc}=\sum_k\mathbb I(c_n^k=c)$ be the votes for class $c$, and $q_{nc}$ the induced distribution (printed $v_{nc}/C$). Apply margin or entropy sampling to $q_n$ (for regression, use the sd across members). QBC can often outperform single-model uncertainty sampling (Figure 34.18).
- *Information-theoretic (p. 1141).* The *information gain* criterion picks points whose label most reduces uncertainty about parameters $w$ [Lin56]:
$$\alpha(x)\triangleq\mathbb H(p(w|\mathcal D))-\mathbb E_{p(y|x,\mathcal D)}[\mathbb H(p(w|\mathcal D,x,y))]\tag{34.95}$$
This equals the expected change in the posterior,
$$\alpha'(x)\triangleq\mathbb E_{p(y|x,\mathcal D)}[D_{\mathrm{KL}}(p(w|\mathcal D,x,y)\,\|\,p(w|\mathcal D))]\tag{34.96}$$
Using symmetry of mutual information,
$$\alpha(x)=\mathbb H(w|\mathcal D)-\mathbb E_{p(y|x,\mathcal D)}[\mathbb H(w|\mathcal D,x,y)]\tag{34.97}$$
$$=\mathbb I(w,y|\mathcal D,x)\tag{34.98}$$
$$=\mathbb H(y|x,\mathcal D)-\mathbb E_{p(w|\mathcal D)}[\mathbb H(y|x,w,\mathcal D)]\tag{34.99}$$
This is *BALD* (Bayesian active learning by disagreement). Only the predictive distribution over $y$ is needed, not over $w$. The first term alone is uncertainty sampling, which can be misled by inherently ambiguous or mislabeled examples. The second term penalises points whose predictive distribution is entropic even when the parameters are known. So BALD ignores aleatoric (intrinsic) uncertainty and focuses on epistemic uncertainty.

*Intuition note.* Raw uncertainty can come from noise that no label will fix. BALD asks for the part of the uncertainty that would shrink if we learned the parameters, which is the part a new label can reduce.

**34.7.4 Batch active learning (pp. 1141–1144).** When labels are requested in batches, the queries must be diverse. The chapter follows BatchBALD [KAG19].
- *34.7.4.1 BatchBALD (p. 1142).* The naive score sums individual BALD scores:
$$\alpha_{\text{BALD}}(x_{1:B},p(w|\mathcal D))=\sum_{i=1}^B\mathbb I(y_i;w|x_i,\mathcal D)\tag{34.100}$$
This may pick similar points. BatchBALD uses the joint mutual information:
$$\alpha_{\text{BBALD}}=\mathbb I(y_{1:B};w|x_{1:B},\mathcal D)=\mathbb H(y_{1:B}|x_{1:B},\mathcal D)-\mathbb E_{p(w|\mathcal D)}[\mathbb H(y_{1:B}|x_{1:B},w,\mathcal D)]\tag{34.101}$$
With an information diagram and a signed measure $\mu^*$ [Yeu91a], BALD is $\sum_i\mu^*(y_i\cap w)$, which double counts overlaps (Figure 34.19a). BatchBALD is
$$\mathbb I(y_{1:B};w|x_{1:B},\mathcal D)=\mu^*(\cup_iy_i\cap w)=\mu^*(\cup_iy_i)-\mu^*(\cup_iy_i\setminus w)\tag{34.102}$$
so $\alpha_{\text{BBALD}}\le\alpha_{\text{BALD}}$. One can show (footnote 7)
$$\mathbb I(y_{1:B},w|x_{1:B},\mathcal D)=\sum_{i=1}^B\mathbb I(y_i,w|x_{1:B},\mathcal D)-\mathbb{TC}(y_{1:B}|x_{1:B},\mathcal D)\tag{34.103}$$
with $\mathbb{TC}$ the total correlation.
- *34.7.4.2 Optimising (p. 1142).* To avoid scoring all subsets, build the batch greedily. Given partial batch $\mathcal A_{n-1}$,
$$x_n=\arg\max_{x\in\mathcal D_{\text{pool}}\setminus\mathcal A_{n-1}}\alpha_{\text{BBALD}}(\mathcal A_{n-1}\cup\{x\},p(w|\mathcal D))\tag{34.104}$$
The function is submodular [KAG19], so greedy selection is within $1-1/e\approx0.63$ of optimal.
- *34.7.4.3 Computing (p. 1143).* Dropping conditioning, $\alpha_{\text{BBALD}}=\mathbb H(y_1,\dots,y_B)-\mathbb E_{p(w)}[\mathbb H(y_1,\dots,y_B|w)]$ (34.105). The $y_i$ are conditionally independent given $w$, so $\mathbb H(y_{1:B}|w)=\sum_i\mathbb H(y_i|w)$, and with samples $\hat w_s\sim p(w|\mathcal D)$,
$$\mathbb E_{p(w)}[\mathbb H(y_{1:B}|w)]\approx\frac1S\sum_{i=1}^{n}\sum_s\mathbb H(y_i|\hat w_s)\tag{34.106}$$
The joint entropy is harder. Using $p(y)=\mathbb E_{p(w)}[p(y|w)]$ and summing over all label sequences,
$$\mathbb H(y_{1:B})=\mathbb E_{p(w)p(y_{1:B}|w)}[-\log p(y_{1:B}|w)]\tag{34.107}$$
$$\approx\sum_{\hat y_{1:B}}\Big(\tfrac1S\sum_{s}p(\hat y_{1:B}|\hat w_s)\Big)\log\Big(\tfrac1S\sum_sp(\hat y_{1:B}|\hat w_s)\Big)\tag{34.108}$$
(as printed; see Reading notes for the sign). Since $p(y_{1:n}|w)=p(y_n|w)p(y_{1:n-1}|w)$, the greedy algorithm can reuse earlier computations (p. 1143).
- *34.7.4.4 MNIST experiment (p. 1144).* A CNN on MNIST, batch size 4, with $p(w|\mathcal D)$ approximated by MC dropout. BALD picks very similar images, and BatchBALD picks more diverse ones (Figure 34.20a,b). The author reports that BatchBALD learns more efficiently than BALD, which beats random sampling (Figure 34.20c).

*Intuition note.* If two candidate labels carry the same information about the parameters, buying both is wasteful. BatchBALD subtracts that overlap, so a batch covers different aspects of the model.

## Toy example (ours, not from the text)
**Setup.** A test for a disease. States $h\in\{\text{sick},\text{healthy}\}$, prior $p(\text{sick})=0.1$. Test: $p(+|\text{sick})=0.9$, $p(+|\text{healthy})=0.2$. Actions: treat or don't. Loss: treat a healthy person = 1, don't treat a sick person = 10, correct action = 0.

**No data.** Treat: $0.9\times1=0.9$. Don't treat: $0.1\times10=1.0$. Best action: treat, risk 0.9.

**Positive test.**
- $p(+)=0.1\cdot0.9+0.9\cdot0.2=0.09+0.18=0.27$.
- $p(\text{sick}|+)=0.09/0.27=1/3$.
- Posterior risk of treat $=\tfrac23\times1=0.667$. Of don't treat $=\tfrac13\times10=3.333$. So treat (34.9).

**Negative test.**
- $p(-)=0.73$.
- $p(\text{sick}|-)=0.01/0.73=0.0137$.
- Risk of treat $=0.9863\times1=0.986$. Of don't treat $=0.0137\times10=0.137$. So don't treat.

**Bayes risk of this rule** (34.11): $0.27\times0.667+0.73\times0.137=0.18+0.10=0.28$.

**Frequentist route** (34.3, 34.12): $r(\delta|\text{sick})=p(-|\text{sick})\times10=0.1\times10=1.0$ and $r(\delta|\text{healthy})=p(+|\text{healthy})\times1=0.2$. Then $R_\pi=0.1\times1.0+0.9\times0.2=0.28$. The two orders of integration agree.

**Value of information** (loss version of (34.30)): $0.9-0.28=0.62$. A test costing less than 0.62 loss units is worth doing. Here the rule's maximum frequentist risk is $1.0$ (when the patient is sick), while its Bayes risk is $0.28$; the two criteria weigh the states differently.

## Concepts
- [[bayes-risk]] (new) — expected frequentist risk averaged over a prior $\pi(h)$; minimiser is a Bayes estimator (p. 1106)
- [[posterior-expected-loss]] (new) — $\rho_\pi(a|x)=\mathbb E_{p(h|x)}[\ell(h,a)]$; minimised per observation by the Bayes-optimal policy (p. 1106)
- [[minimax-estimator]] (new) — minimises maximum frequentist risk; equals Bayes under a least favourable prior; pessimistic (p. 1106)
- [[maximum-expected-utility]] (new) — pick the action maximising expected utility $U=-\ell$ (p. 1107)
- [[posterior-distribution]] — the object over which decision risk is averaged in the Bayesian approach (p. 1106)
- [[frequentist-vs-bayesian-inference]] — here: expectation over data with $h$ fixed vs over $h$ with data fixed (pp. 1106–1107)
- [[admissibility-wald-theorem]] (new) — admissible policies are Bayes for some, possibly improper, prior (p. 1107)
- [[map-vs-mean-vs-mpm]] (new) — 0-1 loss → mode, squared loss → mean, Hamming loss → marginal maxima (pp. 1108–1110)
- [[minimum-bayes-risk-decoding]] (new) — choose the output minimising expected loss under $p(y|x)$, possibly via samples (p. 1110)
- [[influence-diagram]] (new) — graphical model with chance, decision and utility nodes (p. 1112)
- [[value-of-information]] (new) — gain in MEU from observing a variable before acting (VPI) (p. 1114)
- [[ab-test-decision-theory]] (new) — Bayesian choice of rule and test size to maximise total reward (pp. 1115–1117)
- [[multi-armed-bandit]] (new) — sequential choice among arms with unknown reward distributions; contextual if a state is given (p. 1120)
- [[exploration-exploitation-tradeoff]] (new) — need to try actions to learn vs using the current best (p. 1122)
- [[belief-state-mdp]] (new) — MDP whose state is the posterior $b_t$, updated by Bayes' rule (p. 1124)
- [[upper-confidence-bound]] (new) — act greedily on optimistic reward estimates (p. 1124)
- [[thompson-sampling]] (new) — act greedily on one posterior sample; plays each arm with probability of being optimal (p. 1126)
- [[regret]] (new) — gap between oracle reward and agent reward; cumulative $L_T$; lower bound $\log T$ order (p. 1127)
- [[markov-decision-process]] (new) — $\langle\mathcal S,\mathcal A,p,R,p_0\rangle$ with state changing under actions (p. 1128)
- [[bellman-equation]] (new) — recursive characterisation of $V_*$, $Q_*$ (p. 1132)
- [[value-iteration-policy-iteration]] (new) — DP planning: Bellman backups (contraction) vs evaluate–improve (pp. 1134–1135)
- [[active-learning]] (new) — agent chooses which points to label (p. 1137)
- [[bald-batchbald]] (new) — mutual information between labels and parameters; batch version avoids double counting (pp. 1141–1142)
- [[monte-carlo-integration]] — single posterior sample in Thompson sampling; samples in MBR and BatchBALD (pp. 1111, 1126, 1143)
- [[conjugate-prior]] — Beta–Bernoulli and Gaussian updates give closed-form belief states (pp. 1116, 1123)
- [[kl-divergence]] — appears in the expected posterior change (34.96) and the regret lower bound (34.73) (pp. 1128, 1141)

## Canonical instances
- [[oil-wildcatter]] — drill/don't with prior $[0.5,0.3,0.2]$, sounding, MEU 20 vs ≈32, VPI (pp. 1112–1114)
- [[mpm-cube-example]] — a distribution on $\{0,1\}^3$ where MAP is isolated and MPM is $(0,0,0)$ if $2p_2>p_1$ (pp. 1109–1110)
- [[wreck-a-nice-beach]] — structured prediction where sequence-level probability may beat word-level fit (p. 1110)
- [[website-ab-test]] — $N=100{,}000$, $m=0.68$, $\tau=0.03$, optimal $n^*=2284$ (p. 1119)
- [[thompson-linear-bandit]] — three arms with drifting rewards, $s_t=(1,t,t^2)$ (p. 1126)
- [[grid-world-q-star]] — 1-d grid with $\gamma=0,1,0.9$ (p. 1133)
- [[mnist-batchbald]] — BALD vs BatchBALD with MC dropout, batch size 4 (p. 1144)

## Bridges (candidates)
- [same-math] Fubini swap giving $R_B(\delta)$ two ways ↔ probability: law of iterated expectation — the author states they are equivalent (p. 1107).
- [same-math] Thompson sampling's one-sample estimate of $p_a$ ↔ Monte Carlo integration: the integral of an indicator under the posterior is estimated by a sample.
- [same-math] BALD's $\alpha(x)=\mathbb I(w;y|\mathcal D,x)$ ↔ information theory: mutual information, with the KL form (34.96).
- [structural-analogy] Belief-state MDP in bandits ↔ sequential updating: today's posterior is tomorrow's prior, now used as the decision state.
- [structural-analogy] Optimism in the face of uncertainty ($\hat\mu+c\hat\sigma$) ↔ credible intervals: the bonus is a scaled posterior sd, i.e. an upper bound on the interval.
- [structural-analogy] Aleatoric vs epistemic split in BALD (34.99) ↔ posterior predictive distribution: predictive entropy minus expected entropy given parameters.

## Questions this raises
- If the Bayes-optimal bandit policy (Gittins index) exists for context-free arms, how far do UCB and Thompson sampling fall short of it in finite samples? (The text gives only order-of-magnitude regret.)
- How sensitive are the optimal A/B sample size (34.43) and the 10% error figure to the Gaussian approximation and to the prior fitted from past tests?
- In POMDPs, which approximations to the belief-state MDP work best, beyond using the last few observations?
- Does BatchBALD's gain over BALD persist for large batches, given the greedy approximation and the cost of summing over label sequences?

## Reading notes
- Printed page numbers are given on every page; printed = pdf − 34. The text layer is clean enough. All equations were checked against the page images.
- **Misprints and inconsistencies I found (I report the source as printed in L3):**
 - (34.29)/VPI: $0.35\times32.9+0.24\times87.5\approx32.5$ (exact: 11.5 + 21), not the printed 32.2. So VPI would be ≈12.5, not 12.2.
 - (34.46): the argument is printed $(\mu_1-\mu_0)$. With $\mu_1<\mu_0$ this gives a value above ½, so $(\mu_0-\mu_1)$ is presumably intended.
 - (34.47): with $m=0.68$, $\tau=0.03$, $\sigma^2=m(1-m)$, $n=2284$ I get ≈0.05 from the printed formula. The text reports 10%. The formula may be a joint probability, which is half the total error, or it may be mis-scaled. The reader should not rely on it unchecked.
 - §34.3.2: with $\tau=0.03$, $\mathbb E|\mu_1-\mu_0|=2\tau/\sqrt\pi\approx0.034$ (my calculation), not the printed 0.023. The other printed figures (3106; total 69,536) are consistent with $m=0.68$, $\tau=0.03$.
 - (34.57): $N_t^0$ is added to $\alpha$ and $N_t^1$ to $\beta$. With $\mu_a=p(r{=}1|a)$, (34.62) and (34.65) and Figure 34.8 suggest successes ($N^1$) belong with $\alpha$.
 - (34.23)–(34.24): "min" is printed where argmin is presumably meant. Also, (34.24) weights samples by $p(y^j|x)$ although they are described as samples from the posterior, so the weighting may be redundant.
 - (34.73): "$\liminf L_T\ge\log T\sum\dots$" is presumably meant as $\liminf L_T/\log T\ge\sum\dots$.
 - §34.5.5.1: the text says $Q_*(s,a)=1$ for all pairs when $\gamma=1$, but Figure 34.13(c) shows 0 for $(s_1,\text{Up})$.
 - (34.92): the last term is printed $V(s)$, where $V(s')$ is required.
 - (34.106): the sum runs to $n$, where $B$ is meant. (34.107) shows "$p(y_{1:B}|vw)$", which should be $p(y_{1:B}|w)$.
 - (34.108): the leading minus sign of the entropy appears to be missing.
 - QBC: $q_{nc}=v_{nc}/C$, where $K$ (number of members) is presumably meant.
 - (34.44): the text writes $\max(\mu_1,\mu_2)$ while arms are indexed 0,1.
 - Fairness: $p(\hat Y|S=1)$ is printed without "$=1$" in the statistical parity definition.
 - Figure 34.11 caption: "$p(s'=s_0|a=a_0,s'=s_1)$" should presumably read $s=s_1$ in the conditioning.
- Margin sampling is listed as $\alpha(p)=p_2-p_1$, while Figure 34.17 reports the gap $p_1-p_2$ and picks the smallest gap.
- The unit has no exercises. Running footer: Probabilistic Machine Learning: Advanced Topics, online version, December 10, 2025; MIT Press, CC-BY-NC-ND.
