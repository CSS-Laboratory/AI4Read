---
id: sutton-2018-rl/ch02-multi
work: sutton-2018-rl
unit: "Chapter 2: Multi-armed Bandits"
pages: 25-45
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Multi-armed Bandits

## L0 — One line
When feedback only evaluates the action you took (it never says which action was best), you must trade off exploiting your current estimates against exploring, and a few simple methods work much better than always exploiting.

## L1 — The gist (≤ 120 words)
How should a learner choose repeatedly among k actions when each reward only tells it how good that action was? The chapter studies this "k-armed bandit" problem. It estimates action values by averages (computed incrementally), then compares four ways to keep exploring: ε-greedy choice (a random action with small probability ε), optimistic initial values, upper-confidence-bound (UCB) selection, and soft-max gradient bandits (probabilities from learned preferences). A constant step size suits nonstationary (changing) problems. On a 10-armed testbed, ε-greedy beats purely greedy choice and UCB seems best there. The need to balance exploration and exploitation is a distinctive challenge of reinforcement learning. Adding situation-dependent best actions (contextual bandits) leads toward the full problem.

**Prerequisites:** expected value and the law of large numbers; summation notation; partial derivatives and the quotient rule; the exponential function; the idea of a probability distribution.

## L2 — Key ideas
- In their pure forms, evaluative feedback depends entirely on the action taken, whereas instructive feedback does not. Evaluative feedback is what creates the need for active exploration (p. 25).
- The k-armed bandit has action values $q_*(a)=\mathbb E[R_t\mid A_t=a]$. Greedy actions (highest current estimate) exploit current estimates; other actions explore (p. 26).
- ε-greedy beats pure greedy on the 10-armed testbed because greedy often locks onto a suboptimal action (pp. 29–30).
- Sample averages can be computed with constant memory by $Q_{n+1}=Q_n+\frac1n[R_n-Q_n]$. This is an instance of NewEstimate ← OldEstimate + StepSize·[Target − OldEstimate] (p. 31).
- A constant step size α gives an exponential recency-weighted average (recent rewards weigh more), which suits nonstationary (changing) problems. It fails the second convergence condition in (2.7), so estimates keep varying (pp. 32–33).
- Optimistic initial values and UCB direct exploration without random choice. Optimistic values are not well suited to nonstationary problems, and UCB is harder than ε-greedy to extend beyond bandits (pp. 34–36).
- The gradient bandit's expected update equals the gradient of expected reward, so it is stochastic gradient ascent (noisy uphill steps on expected reward). The baseline (a reference reward) affects variance, not the expected update (pp. 37–40).
- A parameter study shows an inverted-U (best at an intermediate parameter value) for every method. On this testbed UCB seems to perform best (pp. 42–43).

## L3 — Walkthrough

### Chapter introduction (p. 25)
- Reinforcement learning (RL) uses training information that evaluates the action taken. It does not instruct by giving the correct action (p. 25).
- Purely evaluative feedback says how good the action was, not whether it was the best or worst possible. Purely instructive feedback gives the correct action regardless of the action taken. It underlies supervised learning (p. 25).
- The chapter uses a nonassociative setting: no more than one situation. The simple k-armed bandit problem introduces basic methods that later chapters extend (p. 25).

### 2.1 A k-armed Bandit Problem (pp. 25–27)
- You choose repeatedly among k actions. After each choice you get a numerical reward from a stationary distribution that depends on the chosen action. The goal is to maximize expected total reward over a period, e.g. 1000 time steps (pp. 25–26).
- Analogies: a slot machine with k levers, and a doctor choosing among experimental treatments (p. 26).
- Notation: the action at step $t$ is $A_t$ and the reward is $R_t$. The **value** of action $a$ is
$$q_*(a)\doteq\mathbb E[R_t\mid A_t=a].$$
- If the values were known, you would always pick the highest. They are not known. $Q_t(a)$ is the estimate at step $t$ (p. 26).
- A **greedy** action has the highest current estimate. Choosing it is **exploiting**. Choosing a nongreedy action is **exploring**, which can improve that action's estimate (p. 26).
- Exploiting is right for the one-step reward. Exploring may give more total reward in the long run, especially when many steps remain (p. 26).
- Whether to explore depends in a complex way on the estimates, their uncertainties and the steps remaining (p. 26).
- Most sophisticated balancing methods make strong assumptions about stationarity and prior knowledge. These are either violated or impossible to verify in most applications. The authors say "we worry only about balancing them at all" (pp. 26–27).

**Intuition note.** Estimates are uncertain, so a rarely tried action may actually be better than it looks. Trying it costs reward now but may find a better option for all later steps.

### 2.2 Action-value Methods (pp. 27–28)
- **Sample-average** estimate (default value, e.g. 0, if the action has not been taken):
$$Q_t(a)\doteq\frac{\sum_{i=1}^{t-1}R_i\cdot\mathbb 1_{A_i=a}}{\sum_{i=1}^{t-1}\mathbb 1_{A_i=a}}\tag{2.1}$$
Here $\mathbb 1_{predicate}$ is 1 if the predicate is true and 0 otherwise. As the denominator goes to infinity, the law of large numbers gives convergence to $q_*(a)$ (p. 27).
- **Greedy selection**, ties broken arbitrarily:
$$A_t\doteq\arg\max_a Q_t(a)\tag{2.2}$$
It never samples apparently inferior actions (p. 27).
- **ε-greedy**: with small probability ε choose uniformly among all actions, independent of the estimates. Otherwise act greedily (pp. 27–28).
- In the limit every action is sampled infinitely often, so all $Q_t(a)\to q_*(a)$. The probability of selecting the optimal action converges to more than $1-\varepsilon$. These are only asymptotic guarantees and say little about practical effectiveness (p. 28).

### 2.3 The 10-armed Testbed (pp. 28–30)
- **Testbed:** 2000 random bandit problems with $k=10$. Each $q_*(a)\sim\mathcal N(0,1)$. Each reward is $R_t\sim\mathcal N(q_*(A_t),1)$ (Fig. 2.1, pp. 28–29).
- One **run** is 1000 steps on one problem. Results average 2000 independent runs (p. 29).
- **Fig. 2.2** compares ε = 0 (greedy), 0.01 and 0.1, all with sample averages and initial estimate 0 (p. 29).
  - Greedy improves slightly faster than the others at the very beginning, then levels off at a lower level, about 1 per step. The best possible is about 1.54 (p. 29).
  - Greedy found the optimal action in only about one-third of the tasks. In the rest, early samples of the optimal action disappointed and it never returned to it (p. 30).
  - ε = 0.1 explores more and usually finds the optimal action earlier. It never selects it more than 91% of the time. ε = 0.01 improves more slowly but eventually would perform better than ε = 0.1 on both measures (p. 30).
  - Reducing ε over time might combine the benefits (p. 30).
- The advantage depends on the task (p. 30):
  - With reward variance 10, more exploration is needed, so ε-greedy should do even better relative to greedy.
  - With variance zero, greedy knows each tried action's true value after one try. It might then perform best.
  - If the task is nonstationary (true values change), exploration is needed even when rewards are deterministic. Nonstationarity is the case most commonly met in RL (p. 30).

**Intuition note.** Greedy can lock onto a suboptimal action after early disappointing samples of a better one. A little forced randomness lets mistaken estimates correct themselves.

### 2.4 Incremental Implementation (pp. 30–32)
- Goal: compute averages with constant memory and constant computation per step (p. 30).
- Focus on one action. $R_i$ is the reward after its $i$th selection. $Q_n\doteq\frac{R_1+\cdots+R_{n-1}}{n-1}$ is the estimate after $n-1$ selections (p. 31).
- Storing all rewards would make memory and computation grow (p. 31). The derivation:
$$\begin{aligned}Q_{n+1}&=\frac1n\sum_{i=1}^n R_i=\frac1n\Big(R_n+\sum_{i=1}^{n-1}R_i\Big)\\&=\frac1n\Big(R_n+(n-1)\frac1{n-1}\sum_{i=1}^{n-1}R_i\Big)=\frac1n\big(R_n+(n-1)Q_n\big)\\&=\frac1n\big(R_n+nQ_n-Q_n\big)=Q_n+\frac1n\big[R_n-Q_n\big]\end{aligned}\tag{2.3}$$
- (2.3) holds even for $n=1$: $Q_2=R_1$ for arbitrary $Q_1$. It needs memory only for $Q_n$ and $n$ (p. 31).
- General form, which recurs throughout the book:
$$NewEstimate\leftarrow OldEstimate+StepSize\,\big[Target-OldEstimate\big]\tag{2.4}$$
$[Target-OldEstimate]$ is an **error** in the estimate. The target is presumed to point in a desirable direction, though it may be noisy. Here the target is $R_n$ and the step size is $1/n$, which changes from step to step (pp. 31–32). The step size is written α or $\alpha_t(a)$ (p. 32).
- **Algorithm box** (p. 32): initialize $Q(a)\leftarrow0$, $N(a)\leftarrow0$. Loop: $A\leftarrow\arg\max_aQ(a)$ with probability $1-\varepsilon$ (ties random), else a random action. Then $R\leftarrow bandit(A)$, $N(A)\leftarrow N(A)+1$, $Q(A)\leftarrow Q(A)+\frac1{N(A)}[R-Q(A)]$.

**Intuition note.** The new average is the old average nudged toward the newest reward by $1/n$ of the gap. Nothing else needs to be stored.

### 2.5 Tracking a Nonstationary Problem (pp. 32–33)
- Sample averages suit stationary problems. When rewards drift, recent rewards should weigh more. A popular way is a constant step size $\alpha\in(0,1]$ (p. 32):
$$Q_{n+1}\doteq Q_n+\alpha\big[R_n-Q_n\big]\tag{2.5}$$
- Unrolling (p. 32):
$$\begin{aligned}Q_{n+1}&=\alpha R_n+(1-\alpha)Q_n\\&=\alpha R_n+(1-\alpha)[\alpha R_{n-1}+(1-\alpha)Q_{n-1}]\\&=\alpha R_n+(1-\alpha)\alpha R_{n-1}+(1-\alpha)^2Q_{n-1}\\&=\alpha R_n+(1-\alpha)\alpha R_{n-1}+(1-\alpha)^2\alpha R_{n-2}+\cdots+(1-\alpha)^{n-1}\alpha R_1+(1-\alpha)^nQ_1\\&=(1-\alpha)^nQ_1+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}R_i\end{aligned}\tag{2.6}$$
- The weights sum to 1: $(1-\alpha)^n+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}=1$. The weight on $R_i$ decays exponentially with how many rewards ago it arrived, so this is an **exponential recency-weighted average**. If $1-\alpha=0$, all weight is on $R_n$ (convention $0^0=1$) (p. 33).
- With a varying step size $\alpha_n(a)$, $\alpha_n=1/n$ gives sample averages. Convergence with probability 1 is assured by these conditions from stochastic approximation theory (a well-known result) (p. 33):
$$\sum_{n=1}^\infty\alpha_n(a)=\infty\quad\text{and}\quad\sum_{n=1}^\infty\alpha_n^2(a)<\infty\tag{2.7}$$
The first is required to guarantee that steps are eventually large enough to overcome initial conditions and random fluctuations. The second makes steps eventually small enough to converge (p. 33).
- $1/n$ meets both. Constant α fails the second, so estimates never fully converge and keep tracking recent rewards. This is desirable in nonstationary problems. Sequences meeting (2.7) often converge slowly or need tuning, and are seldom used in applications (p. 33).

**Intuition note.** With constant α the estimate "forgets" old rewards at a fixed rate. It keeps following a moving target, but it never settles down completely.

### 2.6 Optimistic Initial Values (pp. 34–35)
- All methods so far depend to some extent on the initial estimates $Q_1(a)$, i.e. they are statistically **biased** by them. For sample averages the bias disappears once every action has been chosen at least once. For constant α it is permanent but decreases over time, as in (2.6) (p. 34).
- The initial values are in effect parameters chosen by the user. They can also supply prior knowledge (p. 34).
- **Optimistic initialization:** set $Q_1(a)=+5$ in the testbed, where $q_*$ has mean 0 and variance 1. Every reward then disappoints, so the learner switches actions. All actions get tried several times even if choices are always greedy (p. 34).
- **Fig. 2.3:** greedy with $Q_1=5$ vs ε-greedy (ε = 0.1) with $Q_1=0$, both with $\alpha=0.1$. The optimistic method is worse at first because it explores more, then better because its exploration decreases (p. 34).
- The author calls it a simple trick, effective on stationary problems but far from generally useful. Its drive to explore is temporary, so it cannot help if the task changes. Sample averages also treat the beginning of time as special. Such simple methods are nevertheless often adequate in practice (pp. 34–35).

### 2.7 Upper-Confidence-Bound Action Selection (pp. 35–36)
- ε-greedy explores indiscriminately. Better to choose among nongreedy actions by their potential to be optimal (p. 35).
$$A_t\doteq\arg\max_a\left[Q_t(a)+c\sqrt{\frac{\ln t}{N_t(a)}}\right]\tag{2.10}$$
$N_t(a)$ is the number of times $a$ was selected before $t$. $c>0$ controls exploration. If $N_t(a)=0$, $a$ is treated as a maximizing action (pp. 35–36).
- The square-root term measures uncertainty in the estimate. The bracket is a sort of upper bound on the true value, with $c$ setting the confidence level. Selecting $a$ increases $N_t(a)$ and lowers its term. Selecting another action raises $t$ and so raises its term (p. 36).
- The logarithm makes increases get smaller over time but remain unbounded. All actions are eventually selected, but actions with lower value estimates or frequent past selection are chosen with decreasing frequency over time (p. 36).
- **Fig. 2.4:** UCB with $c=2$ generally beats ε-greedy (ε = 0.1), except in the first $k$ steps, when it selects among untried actions (p. 36).
- UCB is harder than ε-greedy to extend beyond bandits. Nonstationary problems need more complex methods. Large state spaces (with function approximation) make it usually impractical (p. 36).

### 2.8 Gradient Bandit Algorithms (pp. 37–40)
- Learn a numerical **preference** $H_t(a)\in\mathbb R$ instead of a value. Preferences have no reward interpretation. Only differences matter, so adding 1000 to all preferences has no effect on the action probabilities. Probabilities follow a **soft-max** (Gibbs/Boltzmann) distribution (p. 37):
$$\Pr\{A_t=a\}\doteq\frac{e^{H_t(a)}}{\sum_{b=1}^ke^{H_t(b)}}\doteq\pi_t(a)\tag{2.11}$$
Initially $H_1(a)=0$ for all $a$, so actions are equally likely (p. 37).
- Update after choosing $A_t$ and receiving $R_t$ (stochastic gradient ascent). Here $\alpha>0$, and $\bar R_t$ is the average of rewards up to but not including $t$ (with $\bar R_1\doteq R_1$) (p. 37):
$$\begin{aligned}H_{t+1}(A_t)&\doteq H_t(A_t)+\alpha\big(R_t-\bar R_t\big)\big(1-\pi_t(A_t)\big),\quad\text{and}\\H_{t+1}(a)&\doteq H_t(a)-\alpha\big(R_t-\bar R_t\big)\pi_t(a),\quad\text{for all }a\ne A_t\end{aligned}\tag{2.12}$$
- $\bar R_t$ is a **baseline**. A reward above it raises the future probability of $A_t$. A reward below it lowers that probability. Non-selected actions move the opposite way (p. 37). In the chapter's empirical results the baseline also included $R_t$ (footnote, p. 37).
- **Fig. 2.5:** with true values centred near +4, the shift has no effect when the baseline is used, since the baseline adapts. Omitting it (taking $\bar R_t=0$) significantly degrades performance (p. 37).

**Derivation: the algorithm is stochastic gradient ascent** (box, pp. 38–40).
- Exact gradient ascent, with performance measured by expected reward $\mathbb E[R_t]=\sum_x\pi_t(x)q_*(x)$ (p. 38):
$$H_{t+1}(a)\doteq H_t(a)+\alpha\frac{\partial\mathbb E[R_t]}{\partial H_t(a)}\tag{2.13}$$
It cannot be implemented exactly because the $q_*(x)$ are unknown. The claim is that (2.12) equals (2.13) in expected value (p. 38).
- Steps (p. 39):
$$\frac{\partial\mathbb E[R_t]}{\partial H_t(a)}=\frac{\partial}{\partial H_t(a)}\Big[\sum_x\pi_t(x)q_*(x)\Big]=\sum_xq_*(x)\frac{\partial\pi_t(x)}{\partial H_t(a)}=\sum_x\big(q_*(x)-B_t\big)\frac{\partial\pi_t(x)}{\partial H_t(a)}$$
$B_t$ is any scalar not depending on $x$. This is allowed because $\sum_x\frac{\partial\pi_t(x)}{\partial H_t(a)}=0$: the probabilities always sum to one, so their changes sum to zero.
- Multiply each term by $\pi_t(x)/\pi_t(x)$ to get an expectation over $x=A_t$. Then choose $B_t=\bar R_t$ and replace $q_*(A_t)$ by $R_t$ (allowed since $\mathbb E[R_t\mid A_t]=q_*(A_t)$):
$$=\mathbb E\Big[\big(q_*(A_t)-B_t\big)\frac{\partial\pi_t(A_t)}{\partial H_t(a)}\Big/\pi_t(A_t)\Big]=\mathbb E\Big[\big(R_t-\bar R_t\big)\frac{\partial\pi_t(A_t)}{\partial H_t(a)}\Big/\pi_t(A_t)\Big]$$
- Using the result proved below, $\frac{\partial\pi_t(x)}{\partial H_t(a)}=\pi_t(x)\big(\mathbb 1_{a=x}-\pi_t(a)\big)$:
$$=\mathbb E\big[(R_t-\bar R_t)\,\pi_t(A_t)\big(\mathbb 1_{a=A_t}-\pi_t(a)\big)/\pi_t(A_t)\big]=\mathbb E\big[(R_t-\bar R_t)\big(\mathbb 1_{a=A_t}-\pi_t(a)\big)\big]$$
- Sampling this expectation gives $H_{t+1}(a)=H_t(a)+\alpha(R_t-\bar R_t)(\mathbb 1_{a=A_t}-\pi_t(a))$ for all $a$, which is (2.12) (p. 39).
- **Proof of the derivative** (p. 40). Use the quotient rule $\frac{\partial}{\partial x}\frac{f}{g}=\frac{\frac{\partial f}{\partial x}g-f\frac{\partial g}{\partial x}}{g^2}$ and $\frac{\partial e^x}{\partial x}=e^x$:
$$\begin{aligned}\frac{\partial\pi_t(x)}{\partial H_t(a)}&=\frac{\partial}{\partial H_t(a)}\Big[\frac{e^{H_t(x)}}{\sum_{y=1}^ke^{H_t(y)}}\Big]\\&=\frac{\frac{\partial e^{H_t(x)}}{\partial H_t(a)}\sum_ye^{H_t(y)}-e^{H_t(x)}\frac{\partial\sum_ye^{H_t(y)}}{\partial H_t(a)}}{\big(\sum_ye^{H_t(y)}\big)^2}\\&=\frac{\mathbb 1_{a=x}e^{H_t(x)}\sum_ye^{H_t(y)}-e^{H_t(x)}e^{H_t(a)}}{\big(\sum_ye^{H_t(y)}\big)^2}\\&=\frac{\mathbb 1_{a=x}e^{H_t(x)}}{\sum_ye^{H_t(y)}}-\frac{e^{H_t(x)}e^{H_t(a)}}{\big(\sum_ye^{H_t(y)}\big)^2}\\&=\mathbb 1_{a=x}\pi_t(x)-\pi_t(x)\pi_t(a)=\pi_t(x)\big(\mathbb 1_{a=x}-\pi_t(a)\big)\quad\text{Q.E.D.}\end{aligned}$$
- Conclusion: the expected update equals the gradient of expected reward, so the algorithm is stochastic gradient ascent. The author says this assures robust convergence properties (p. 40).
- The baseline need only not depend on the selected action. It could be 0 or 1000. It does not change the expected update but affects its variance, hence the convergence rate. The average reward "may not be the very best, but it is simple and works well in practice" (p. 40).

**Intuition note.** The update raises the chosen action's preference when the reward beats the baseline, and lowers it otherwise. Averaged over choices, this moves preferences uphill on expected reward. A good baseline only reduces noise.

### 2.9 Associative Search (Contextual Bandits) (p. 41)
- General RL needs a **policy**: a mapping from situations to the actions best in them. Nonassociative tasks seek one best action or track it as it changes (p. 41).
- Example: several k-armed bandit tasks, one chosen at random each step. If you get a distinctive clue about which task you face (e.g. the color of the machine's display) but not its action values, you can learn a policy such as "if red, arm 1; if green, arm 2". This is **associative search** (today also "contextual bandits") (p. 41).
- Such tasks lie between bandits and full RL. They involve learning a policy, but each action affects only the immediate reward. If actions also affect the next situation, it is the full RL problem (p. 41).

### 2.10 Summary (pp. 42–43)
- Methods recap: ε-greedy explores randomly. UCB explores deterministically by favoring less-sampled actions. Gradient bandits use preferences and soft-max. Optimistic initialization makes even greedy methods explore (p. 42).
- **Parameter study (Fig. 2.6):** each algorithm's average reward over the first 1000 steps (proportional to area under the learning curve) is plotted against its own parameter ($\varepsilon$, $\alpha$, $c$, or $Q_0$) on a log scale. Every algorithm shows an inverted U, best at an intermediate parameter value (p. 42).
- All are fairly insensitive, performing well over a parameter range of about an order of magnitude. On this problem UCB seems to perform best (p. 43).
- In the authors' opinion the methods of this chapter can fairly be considered "the state of the art". More sophisticated methods exist, but their complexity and assumptions make them impractical for the full RL problem. The simple methods may be the best we can do at present, yet they are far from a fully satisfactory solution (p. 43).
- **Gittins index:** in certain important special cases it gives optimal solutions. It needs complete knowledge of the prior distribution of problems, and neither its theory nor its tractability seem to generalize to full RL (p. 43).
- **Bayesian methods** assume a known initial distribution over action values and update it exactly (for stationary values). With conjugate priors updates are easy. **Thompson (posterior) sampling** picks actions by their posterior probability of being best, and often performs like the best distribution-free methods here (p. 43).
- The evolving distribution is an **information state**. For a 1000-step horizon, with two actions and two rewards the tree of possibilities would have $2^{2000}$ leaves. Exact computation is generally infeasible. Approximating it would turn the bandit into a full RL problem (p. 43).

### Bibliographical and Historical Remarks (pp. 44–45)
- The exploration–exploitation conflict is called in control engineering the conflict between identification (estimation) and control. Feldbaum called it the dual control problem (p. 44).
- The UCB algorithm here is UCB1 (Auer, Cesa-Bianchi and Fischer, 2002). Gradient bandits are a special case of Williams's (1992) algorithms. The term soft-max is due to Bridle (1990) (pp. 44–45).

## Toy example (ours, not from the text)
Two arms with deterministic rewards: arm A pays 1 and arm B pays 3. Sample averages, default $Q=0$, and ties go to A.

**Greedy gets stuck.**
- Step 1: tie, pick A, $R=1$. $N(A)=1$ and $Q(A)=0+\frac11(1-0)=1$, so $Q=(1,0)$.
- From then on A is greedy (1 > 0), and B is never tried. Total over 10 steps = $10\times1=10$.

**One exploring step helps.** If step 2 is an ε-step that tries B, then $Q(B)=0+\frac11(3-0)=3>1$. Greedy picks B for steps 3–10. Total over 10 steps $=1+3+3\times8=28$.

**Optimistic start.**
- With $Q_1=5$ for both arms, step 1 picks A (tie) and gives $Q(A)=5+1\cdot(1-5)=1$, i.e. $Q_2=R_1$.
- Then $Q(B)=5>1$, so greedy tries B and gets $Q(B)=3$. It stays on B. Optimism forced the exploration.

**Constant vs. $1/n$ step on rewards 2, 4** (start $Q_1=0$):
- Sample average: $Q_2=0+\frac11(2-0)=2$; $Q_3=2+\frac12(4-2)=3$, the mean.
- Constant $\alpha=0.5$: $Q_2=0+0.5(2-0)=1$; $Q_3=1+0.5(4-1)=2.5$.
- Check with (2.6): $(0.5)^2\cdot0+0.5\cdot0.5\cdot2+0.5\cdot4=0.5+2=2.5$ ✓. The weights are $0.25$ (on $Q_1$), $0.25$ (on $R_1$) and $0.5$ (on $R_2$), which sum to 1 and favor the recent reward.

## Concepts
- [[evaluative-vs-instructive-feedback]] (new) — evaluative feedback scores the action taken. Instructive feedback gives the correct action regardless of the action taken (p. 25).
- [[exploration vs exploitation]] — exploit = choose a greedy action. Explore = choose a nongreedy one to improve estimates. They conflict at each step (p. 26).
- [[action-value]] (new) — $q_*(a)=\mathbb E[R_t\mid A_t=a]$. $Q_t(a)$ is its estimate (p. 26).
- [[sample-average-method]] (new) — estimate of an action's value as the mean of rewards received for it (p. 27).
- [[epsilon-greedy]] (new) — act greedily, except with probability ε choose uniformly at random (pp. 27–28).
- [[incremental-update-rule]] (new) — NewEstimate ← OldEstimate + StepSize[Target − OldEstimate], where the bracket is an error. Compare [[error signal]] in the canon (pp. 31–32).
- [[constant-step-size]] (new) — fixed α gives an exponential recency-weighted average. It suits nonstationary problems (pp. 32–33).
- [[nonstationarity]] (new) — true action values change over time. The author says this is the most common case in RL (p. 30).
- [[optimistic-initial-values]] (new) — high initial estimates make even greedy methods explore. The effect is temporary (p. 34).
- [[ucb-action-selection]] (new) — pick $\arg\max_a[Q_t(a)+c\sqrt{\ln t/N_t(a)}]$ (p. 35).
- [[gradient-bandit]] (new) — learn soft-max action preferences by stochastic gradient ascent on expected reward (pp. 37–40).
- [[reward-baseline]] (new) — a comparison reward that leaves the expected gradient update unchanged but changes its variance (p. 40).
- [[contextual-bandit]] (new) — associative search: the best action depends on a visible situation, but actions affect only immediate reward (p. 41).
- [[policy]] — here, a mapping from situations to the actions best in them (p. 41).
- [[gittins-index-and-thompson-sampling]] (new) — Bayesian approaches to the exploration balance, mentioned as alternatives (p. 43).

## Canonical instances
- [[ten-armed-testbed]] — 2000 random bandit problems with $q_*\sim\mathcal N(0,1)$. It is the benchmark used for comparing methods throughout the chapter (pp. 28–29, 42).
- [[slot-machine-bandit]] — the k-lever slot machine, and the doctor choosing treatments, as motivating analogies (p. 26).
- [[color-signalled-slot-machine]] — an associative search task where display color signals which bandit is active (p. 41).

## Bridges (candidates)
- [structural-analogy] Exploration vs exploitation ↔ control theory: identification (estimation) vs control, "dual control" — the text names this correspondence (p. 44).
- [structural-analogy] Incremental update ↔ control-theory observers: estimate corrected by the error between measurement and prediction, scaled by a gain.
- [structural-analogy] Constant step size α ↔ exponential forgetting in recursive estimation of a drifting quantity.
- [same-math] Two-action soft-max ↔ statistics: the logistic (sigmoid) function (the text poses this as Exercise 2.9, p. 37).
- [structural-analogy] Gradient bandit with baseline ↔ stochastic approximation: noisy-gradient ascent with variance reduction.

## Questions this raises
- When does the greedy method actually win (e.g. deterministic, stationary rewards), and how can the learner tell?
- How should ε, α, $c$ or $Q_0$ be chosen without running a parameter study first?
- Which simple methods survive when actions change the next situation (the full RL problem)?
- How could the Bayesian optimal balance be approximated, given the $2^{2000}$-leaf tree?

## Exercises worth doing
- Ex. 2.2 (p. 30) — reasoning about which steps definitely or possibly involved a random ε-choice — difficulty: easy
- Ex. 2.4 (p. 33) — the weights on past rewards for general step sizes $\alpha_n$ — difficulty: medium
- Ex. 2.5 (p. 33) — programming: sample-average vs constant step size on a drifting testbed — difficulty: medium
- Ex. 2.7 (p. 35) — the unbiased constant-step-size trick, analysis like (2.6) — difficulty: hard
- Ex. 2.9 (p. 37) — two-action soft-max equals the logistic function — difficulty: easy
- Ex. 2.10 (p. 41) — value of context information in a 2-armed associative task — difficulty: medium

## Reading notes
- Printed page = pdf page − 22. The unit covers printed pp. 25–45. The text layer for pdf 68 (printed 46) is empty.
- The text layer drops minus signs and special symbols in many places (e.g. "$R_1 = 1$" in Exercise 2.2 where the image shows $R_1=-1$ and $R_3=-2$). I checked equations against the page images.
- In Fig. 2.3 the text layer mixes axis labels ("Plays"/"Steps"). The image shows "Steps".
- Figure values (e.g. 91%, one-third, about 1.54) are as stated in the text. No misprints found in the pages given.
