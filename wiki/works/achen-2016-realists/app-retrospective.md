---
id: achen-2016-realists/app-retrospective
work: achen-2016-realists
unit: Appendix — Retrospective Voting as Selection and Sanctioning
pages: 329-333
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# Retrospective Voting as Selection and Sanctioning

## L0 — One line
Two simple formal models show that a voter who judges incumbents by past well-being learns less, or disciplines less, the more random luck clouds that well-being.

## L1 — The gist (≤ 120 words)
The appendix formalizes two ways retrospective voting could work. In *selection*, the voter infers a fixed incumbent competence from experienced well-being, which mixes competence with luck. The best estimate is the average experience, with variance σ²/T. In *sanctioning*, all leaders are identical. The voter reelects if well-being passes a threshold, and the incumbent chooses costly effort. The equilibrium effort is φ(0)/ψ, capped at 1.0. In both models, more randomness (σ or ψ) makes retrospection less effective. This matters because it shows, under these assumptions, how randomness limits what voters can learn or enforce.

**Prerequisites:** normal distribution (mean, variance, density φ, cumulative Φ); sample mean; expected-payoff maximization; basic derivatives.

## L2 — Key ideas
- Selection model: well-being is competence plus luck, $\omega_t=\theta_t+\delta_t$. The voter must infer competence from a noisy signal (p. 329).
- If competence is constant, the voter's task is to estimate a mean. The estimate is the average past well-being, and its variance falls as $\sigma^2/T$ (p. 330).
- How many past periods are informative depends on the party system. If parties are stable, several past periods may be informative (p. 331).
- Sanctioning model: leaders are identical, and well-being is effort plus luck, $\omega_t=\gamma_t+\epsilon_t$. The voter reelects only if $\omega_t$ reaches a threshold (pp. 331–332).
- The incumbent's effort choice solves $\gamma^*=\phi((\gamma^*-\tau^*)/\psi)/\psi$. It depends on the voter's threshold (pp. 332–333).
- The voter does best by setting $\tau^*=\gamma^*$. Then reelection probability is .5 and effort is $\phi(0)/\psi$ (p. 333).
- Effort is capped at 1.0, so equilibrium effort is 1.0 for small ψ and $\phi(0)/\psi$ otherwise. More randomness means less effective sanctioning (p. 333).
- The footnoted assumptions matter: independent luck, no strategic "show" competence, term-by-term incentives, and quadratic effort cost (pp. 329–332).

## L3 — Walkthrough

### Retrospective voting as selection (pp. 329–331)
**Setup.** A representative voter's well-being under the incumbent in period $t$ is

$$\omega_t=\theta_t+\delta_t,\qquad \delta_t\sim N(0,\sigma^2)\tag{A.1}$$

Here $\omega_t$ is subjective well-being, $\theta_t$ is intrinsic competence and $\delta_t$ is luck (p. 329). The voter knows the distribution of $\delta_t$ but not its realized value. So he must use $\omega_t$ to estimate $\theta_t$ (p. 329).

Footnotes on the assumptions:
- Fn 1: equation A.1 rules out incumbents showing "competence" in ways that do not raise well-being, such as impressive campaigns (p. 329).
- Fn 2: the same $\delta$ distribution each period rules out "rational retrospective" models. The footnote reports Hibbs (2006) saying such models have no empirical support. It reports Duch and Stevenson (2008) arguing that they do. It reports Achen (2012) arguing that they are not theoretically robust (pp. 329–330).
- Fn 3: in a two-party system, competence can be defined relative to the out-party "without loss of generality". Surprisingly good experience under the incumbent, or bad under the out-party, raises the chance of reelection (p. 330).
- Fn 4: the $\delta_t$ are assumed independent. If luck is correlated across periods, experience is less informative and the voter must adjust (p. 330).

**Voter's rule.** The prospectively rational voter cares about next-period competence $\theta_{T+1}$, not current $\theta_T$. He reelects if the expected $\theta_{T+1}$ exceeds that of his best alternative (p. 330).

**Simplest assumption:** competence is constant, $\theta_1=\dots=\theta_{T+1}=\theta$. The voter can use $\omega_T$ alone, but earlier experiences $\omega_1,\dots,\omega_{T-1}$ add information (p. 330). The task is formally equivalent to estimating a mean from a sample of size $T$ (Achen 1992) (p. 330). The best estimate and its uncertainty are:

$$\hat\theta_{T+1}=\sum_t\omega_t/T\tag{A.2}$$

$$\operatorname{var}(\hat\theta_{T+1})=\sigma^2/T\tag{A.3}$$

Uncertainty depends on experience $T$ and on how much luck obscures competence, $\sigma$ (p. 330).

*Intuition note.* Averaging over more periods cancels some luck, so more experience gives a sharper judgment. Larger luck variance blurs it.

**Which periods count.** A rational voter uses every relevant period, not only the current one. With stable party leadership and commitments, several past periods may be informative. In a less stable system, perhaps only one or a few (p. 331).

**Figure 4.1** (in the text, not reproduced here) shows selection efficacy against true $\theta$ and randomness. The blindness of retrospection is gauged by $\sigma/\sqrt T$, the square root of A.3 (p. 331).

### Retrospective voting as sanctioning (pp. 331–333)
**Setup.** All potential leaders are identical, so selection is impossible (p. 331). Well-being depends only on the incumbent's effort and on luck:

$$\omega_t=\gamma_t+\epsilon_t,\qquad \epsilon_t\sim N(0,\psi^2)\tag{A.4}$$

with $\gamma_t\ge0$ the incumbent's diligence (p. 331). The distribution of $\epsilon_t$ is known to voter and incumbent. Its value is unknown to the incumbent when she chooses effort, and never observed by the voter, even afterwards (p. 331).

**Reelection rule.** Following the usual principal–agent rule, the voter reelects if and only if well-being exceeds a threshold $\tau_t$ (p. 332). The reelection probability is:

$$\pi_t=\operatorname{prob}(\omega_t\ge\tau_t)\tag{A.5}$$

Substituting A.4 and rearranging:

$$\pi_t=\operatorname{prob}(-\epsilon_t\le\gamma_t-\tau_t)=\Phi\big((\gamma_t-\tau_t)/\psi\big)\tag{A.6}$$

where Φ is the cumulative normal distribution function (p. 332). Higher effort raises the reelection probability (p. 332).

Fn 5: more complex strategies conditioned on earlier periods are possible in principle. The authors limit the analysis to term-by-term incentives because coordination problems are already rampant (p. 332).

**Incumbent's problem.** Effort is costly, so she maximizes

$$\nu_t=\pi_t-\gamma_t^2/2=\Phi\big((\gamma_t-\tau_t)/\psi\big)-\gamma_t^2/2\tag{A.7}$$

Fn 6: the coefficient 1/2 loses no generality. But making cost depend on $\gamma_t^2$ rather than $\gamma_t$, so that marginal cost rises, has "a substantively important impact" on equilibrium (p. 332).

The equilibrium relationship is

$$\gamma_t^*=\phi\big((\gamma_t^*-\tau_t^*)/\psi\big)/\psi\tag{A.8}$$

where φ is the normal density (pp. 332–333). *(added step: this is the first-order condition $d\nu_t/d\gamma_t=\phi((\gamma_t-\tau_t)/\psi)/\psi-\gamma_t=0$; the text does not show it.)*

**Voter's threshold.** The voter wants to maximize his well-being. He cannot influence luck, only effort. So he picks the threshold that elicits the most effort (p. 333). By A.8, effort is largest when $\tau_t^*=\gamma_t^*$, because the density φ is maximal at 0 (p. 333, fn 7). Then A.8 becomes

$$\gamma_t^*=\phi(0)/\psi\tag{A.9}$$

so equilibrium effort depends on ψ, the standard deviation of the random factors (p. 333).

**Cap on effort.** With $\tau^*=\gamma^*$, $\gamma-\tau=0$ in A.6, so equilibrium reelection probability is .5 (p. 333). Effort above 1.0 would give a negative expected payoff, since she can always get a nonnegative payoff with zero effort (p. 333, fn 8). *(added step: at $\pi=.5$, $\nu=.5-\gamma^2/2<0$ iff $\gamma>1$.)* So equilibrium effort and threshold are either 1.0 (for sufficiently small ψ) or the value from A.9 (p. 333).

**Figure 4.2** (in the text) plots $\gamma^*$ against ψ. More randomness gives less effective sanctioning and lower voter well-being (p. 333).

*Intuition note.* If luck swamps effort, working harder barely changes the chance of reelection. So the incumbent has little reason to try. The voter's best threshold is exactly the effort level he expects, which makes reelection a coin flip.

## Toy example (ours, not from the text)
*Selection.* Let $\sigma=2$. Suppose the voter experiences $\omega=2,5,3,6$ over $T=4$ periods. Then $\hat\theta=(2+5+3+6)/4=16/4=4$. By A.3, $\operatorname{var}=2^2/4=1$, so the standard error is 1. With $T=1$ the standard error would stay at 2. Blindness $\sigma/\sqrt T$ falls from 2 to 1.

*Sanctioning.* Use $\phi(0)=1/\sqrt{2\pi}\approx0.399$ *(added step)*.
- $\psi=0.8$: $\gamma^*=0.399/0.8\approx0.50$.
- $\psi=1.6$: $\gamma^*\approx0.25$. Doubling the noise halves effort.
- $\psi=0.2$: A.9 gives $\approx1.99>1$, so the cap applies and $\gamma^*=1$.

The crossover is where $\phi(0)/\psi=1$, so $\psi\approx0.399$ *(added step)*.

## Concepts
- [[retrospective-voting]] — judging incumbents by past outcomes; here formalized as selection or sanctioning (p. 329)
- [[selection-model]] (new) — voter infers fixed incumbent competence from noisy well-being (pp. 329–330)
- [[sanctioning-model]] (new) — identical leaders; threshold rule gives costly effort incentives (pp. 331–333)
- [[principal-agent-problem]] — voter as principal using a threshold rule on an incumbent agent whose effort he cannot observe (p. 332)
- [[luck-noise-term]] (new) — random factors beyond the incumbent's control, $\delta_t$ or $\epsilon_t$ (pp. 329, 331)
- [[blindness-of-retrospection]] (new) — gauged by $\sigma/\sqrt T$; higher means less informative experience (p. 331)

## Canonical instances
- [[selection-model-normal-luck]] (new) — $\omega=\theta+\delta$ with sample-mean inference (pp. 329–330)
- [[sanctioning-model-quadratic-cost]] (new) — $\gamma^*=\phi(0)/\psi$, capped at 1 (pp. 332–333)

## Bridges (candidates)
- [same-math] Estimating $\theta$ by the sample mean with variance $\sigma^2/T$ ↔ statistics: standard error of a mean — the text says the problem is equivalent (p. 330)
- [structural-analogy] Voter's threshold rule and incumbent's effort ↔ principal–agent theory: incentive contract under unobservable noise (p. 332)
- [structural-analogy] More periods relevant under stable parties ↔ institutions: party-system stability shapes what voters can learn (p. 331)

## Questions this raises
- What happens to the selection estimate if competence changes over time or luck is correlated (fn 4)?
- Would a richer voter strategy, using several past periods, sustain more effort than the term-by-term rule (fn 5)?
- How sensitive is the capped equilibrium to the quadratic cost assumption (fn 6)?
- What empirical measure of ψ or σ could be compared with the figures?

## Reading notes
- Printed = pdf − 19. The unit's content ends on printed p. 333. Printed p. 334 (pdf 353) is blank.
- Figures 4.1 and 4.2 are referred to but are not on these pages.
- Footnotes 1–8 are summarized where they bear on the assumptions. The voice in fn 2 is the authors reporting Hibbs, Duch and Stevenson, and Achen.
- Equations A.1–A.9 were checked against the page images. In A.2 the estimate carries subscript $T+1$ and the sum runs over $t$ (index range not printed).
