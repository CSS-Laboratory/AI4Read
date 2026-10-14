---
id: mackay-2003-information/ch36-decision
work: mackay-2003-information
unit: "36 Decision Theory"
pages: 451-456
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Decision Theory (MacKay, ch. 36)

## L0 — One line
Choose the action with the highest expected utility; the remaining difficulties are that choosing the utility function may be quite hard and that expected utility can be hard to compute, especially when actions bring information.

## L1 — The gist (≤ 120 words)
How should you act when outcomes are uncertain? MacKay says the principle is simple: maximize expected utility. Hard parts can be choosing a utility function (which may be quite difficult) and computing the expectations, especially when actions yield information that may affect later actions. His worked example is choosing a mine site among Gaussian-uncertain sites, where you may first pay to prospect at one site. With linear utility, prospecting is worthwhile if its expected gain, from possibly switching site, exceeds its cost. The chapter ends with exercises on the four doors, the Allais paradox, optimal stopping, minimax regret, Cover's log-wealth betting and dice bets.

**Prerequisites:** Gaussian distributions (mean, variance); Bayes' theorem; expectation as an integral; basic probability of discrete outcomes.

## L2 — Key ideas
- Decision theory: actions $a$, world states $x$ with $P(x\mid a)$, utility $U(x,a)$. Pick the $a$ that maximizes $\mathcal E[U\mid a]$ (p. 451).
- Remaining difficulties: choosing the utility function, handling sequences of informative actions, and exact computation. Decisions mix forward and inverse probability (p. 451).
- With linear utility and no prospecting, the best site is the one with the largest prior mean. In this no-prospecting choice, $\sigma_n$ plays no role with linear utility; the author says that if you think it should, the utility should be nonlinear (p. 452).
- Prospecting is valuable only because the datum may change the chosen site. Its value is computed by integrating over the distribution of the updated mean (p. 453).
- Gaussian mnemonics: independent variables add variances; multiplying Gaussians adds precisions (p. 452).
- Figure 36.1 gives a rule: prospect at site $n$ if the gain (a function of $\mu_n-\mu_1$ and $\sigma_n$) exceeds the cost $c_n$ (p. 453).
- Harder settings (repeated prospecting, uncertain costs) become exploration–exploitation problems; reinforcement learning gives approximate methods (p. 453).
- Exercises probe where utilities come from: the Allais paradox, regret-based objectives, and Cover's aim of maximizing $\mathbb E[\log m(T)]$ (pp. 454–456).

## L3 — Walkthrough

### Introduction (p. 451)
The author calls decision theory "trivial, apart from computational details" (p. 451).
- You choose an action $a$. The world is in one of many states $x$, with distribution $P(x\mid a)$. A utility function $U(x,a)$ gives your payoff.
- The task is to pick the action maximizing expected utility (p. 451):
$$\mathcal E[U\mid a]=\int d^Kx\; U(x,a)\,P(x\mid a). \tag{36.1}$$
- "Pessimists" may instead define a loss function $L$ and minimize expected loss (p. 451).
- Complications the author lists (p. 451):
  - choosing the utility function may be hard;
  - with a sequence of actions, each giving information about $x$, we have to take into account the effect that this anticipated information may have on later actions;
  - in a realistic problem, such as a board game, the tree of possible actions and "cogitations" is enormous, and 'doing the right thing' is not simple, because the expected utility of an action cannot be computed exactly.

### 36.1 Rational prospecting (pp. 451–453)
**Setup.** You must pick one of $N$ mine sites. Site $n$ has a net return $x_n$ (revenue minus costs), known exactly only after you choose it. The prior is $P(x_n)$ (p. 451).
- Before choosing you may prospect at site $n$. This costs $c_n$ and gives data $d_n$ that reduce uncertainty about $x_n$ (p. 451).
- Assumptions: site returns are unrelated, and prospecting at a site informs only about that site (p. 452).
- Decision problem: decide whether and where to prospect, then choose the site in the light of the results (p. 452).

**Gaussian model.** The author focuses on prospecting once or not at all, with utility linear in $x_n$ (p. 452). Here $n_a$ is the chosen site and $n_p$ the prospected site:
$$U=x_{n_a}\ \text{(no prospecting)}, \tag{36.2}$$
$$U=-c_{n_p}+x_{n_a}\ \text{(prospecting)}, \tag{36.3}$$
$$P(x_n)=\text{Normal}(x_n;\mu_n,\sigma_n^2), \tag{36.4}$$
$$P(d_n\mid x_n)=\text{Normal}(d_n;x_n,\sigma^2). \tag{36.5}$$

**Exercise 36.1 results (stated, to be shown by the reader; p. 452).**
$$P(d_n)=\text{Normal}(d_n;\mu_n,\sigma^2+\sigma_n^2), \tag{36.6}$$
$$P(x_n\mid d_n)=\text{Normal}(x_n;\mu_n',\sigma_n^{2\prime}), \tag{36.7}$$
$$\mu_n'=\frac{d_n/\sigma^2+\mu_n/\sigma_n^2}{1/\sigma^2+1/\sigma_n^2},\qquad \frac1{\sigma_n^{2\prime}}=\frac1{\sigma^2}+\frac1{\sigma_n^2}. \tag{36.8}$$
Mnemonics: independent variables add, so variances add; Gaussians multiply, so precisions (inverse variances) add (p. 452).

*Intuition note.* The posterior mean is an average of datum and prior mean, each weighted by its precision. The posterior is always narrower than the prior.

**No prospecting (Exercise 36.2 results; p. 452).** The optimal action is
$$n_a=\arg\max_n\mu_n, \tag{36.9}$$
with expected utility
$$\mathcal E[U\mid\text{optimal }n]=\max_n\mu_n. \tag{36.10}$$
Author's reply to the intuition that $\sigma_n$ should matter: "reasonable – if so, then the utility function should be nonlinear in $x$" (p. 452).

**Should we prospect? (p. 453).** After prospecting at $n_p$ we apply rule (36.9) with $\mu_{n_p}$ replaced by $\mu_n'$ from (36.8). We do not yet know $d_n$, so we do not know which action we will take. The whole value of prospecting comes from the outcome possibly changing the action. We therefore integrate over outcomes and their actions (p. 453).

**Exercise 36.3 result (p. 453).** $\mu_n'$ is Gaussian with mean $\mu_n$ and variance
$$s^2\equiv\sigma_n^2\,\frac{\sigma_n^2}{\sigma^2+\sigma_n^2}. \tag{36.11}$$

**Value of prospecting at $n$ (p. 453).** Let $\mu_1$ be the biggest mean among the other sites. If $\mu_n'>\mu_1$ we choose site $n$ and expect $\mu_n'$; if $\mu_n'<\mu_1$ we choose site 1 and expect $\mu_1$. So
$$\mathcal E[U\mid\text{prospect at }n]=-c_n+P(\mu_n'<\mu_1)\,\mu_1+\int_{\mu_1}^{\infty}d\mu_n'\,\mu_n'\,\text{Normal}(\mu_n';\mu_n,s^2). \tag{36.12}$$
Without prospecting, the best expected utility is $\mu_1$ if $\mu_1\ge\mu_n$ and $\mu_n$ if $\mu_1\le\mu_n$ (the printed (36.13) shows minus signs; see Reading notes). The gain depends on which case holds (p. 453):
$$\mathcal E[U\mid\text{prospect at }n]-\mathcal E[U\mid\text{no prospecting}]=\begin{cases}-c_n+\int_{\mu_1}^{\infty}d\mu_n'\,(\mu_n'-\mu_1)\,\text{Normal}(\mu_n';\mu_n,s^2)&\text{if }\mu_1\ge\mu_n\\[4pt]-c_n+\int_{-\infty}^{\mu_1}d\mu_n'\,(\mu_1-\mu_n')\,\text{Normal}(\mu_n';\mu_n,s^2)&\text{if }\mu_1\le\mu_n.\end{cases}\tag{36.14}$$
- (added step) Case $\mu_1\ge\mu_n$: subtract $\mu_1$ from (36.12) and use $P(\mu_n'<\mu_1)-1=-\int_{\mu_1}^\infty\text{Normal}$.
- (added step) Case $\mu_1\le\mu_n$: subtract $\mu_n=\int\mu_n'\,\text{Normal}$ and use $\int_{\mu_1}^\infty\mu_n'\,\text{Normal}-\mu_n=-\int_{-\infty}^{\mu_1}\mu_n'\,\text{Normal}$.

**Figure 36.1 (p. 453).** Contour plot of the gain without $c_n$, against $(\mu_n-\mu_1)$ on the horizontal axis and $\sigma_n$ on the vertical axis, with $\sigma^2=1$. Contours run from 0.1 to 1.2 in steps of 0.1. To decide, find the contour equal to $c_n$; all points above it are worthwhile (p. 453).

*Intuition note.* Prospecting pays only when the datum can overturn your current choice. It pays more when $\sigma_n$ is large or when site $n$ is close in mean to the best rival. The integrals in (36.14) are the expected size of the improvement.

### 36.2 Further reading (p. 453)
If multiple rounds of prospecting are possible, or the cost of prospecting is uncertain, finding the best balance between exploration and exploitation becomes much harder computationally. Reinforcement learning addresses approximate methods (Sutton and Barto, 1998) (p. 453).

### 36.3 Further exercises (pp. 454–456)
Set-ups only; no solutions are given in this unit.
- **36.4 Four doors** (p. 454): a three-doors-style game. After you point to a door, the host opens a non-winner. You may switch. He opens another non-winner, never the current pick, and you decide finally. Find the optimal strategy.
- **36.5 Allais paradox** (p. 454): many prefer A (£1M certain) to B (89% £1M, 10% £2.5M, 1% nothing), and D (10% £2.5M, else nothing) to C (11% £1M, else nothing). Prove these preferences are inconsistent with any utility function $U(x)$.
- **36.6 Optimal stopping** (pp. 454–455): $N$ partners arrive in random order, each with desirability $d_n$; you accept or reject on the spot. Three variants: (a) maximize $d_{\hat n}$; (b) maximize the chance of getting the best; (c) strategy $M$ (reject the first $M$, then take the first better than their maximum, else the last): find the optimal $M$.
- **36.7 Regret** (p. 455): Fred sells you a lottery ticket (win probability 1/100, worth £10) for £1. The regret table (Table 36.3) makes "buy" the minimax-regret action: maximum regret £1 if you buy, £9 if you don't. The author asks whether this can be philosophically justified. In the portfolio version, minimax regret puts $f_1=9/10$ in the lottery fund and $f_0=1/10$ in cash. The reader is asked to show this and to judge it.
- **36.8 Gambling oddities** (pp. 455–456; from Cover and Thomas, 1991): a repeated horse race. Bet vector $b$, money $m(t)$, return $m(t+1)=b_io_im(t)$ if horse $i$ wins, fair odds $\sum_i 1/o_i=1$ (36.15), win probabilities $p_i$. Maximize $\mathbb E[\log m(T)]$ ("Cover's aim"). The reader is to show that the optimum is $b=p$, independent of the odds $o$, and that the money is expected to grow exponentially as $2^{nW(b,p)}$ (36.16), with $W=\sum_ip_i\log b_io_i$. The author asks whether ignoring the odds is "optimal" in ordinary language.
- **36.9 Dice** (p. 456): Joe Shark bets even money that a 6 will be thrown before the first 7; then, separately, that an 8 will be thrown before the first 7; then he proposes a combined bet that an 8 and a 6 are thrown before two 7s have been thrown. Decide whether to take each bet and find your winning probabilities.

## Toy example (ours, not from the text)
Site 1 has known return $\mu_1=5$. Site $n$ has return $x_n=10$ or $0$, each with probability $1/2$ (mean 5). Prospecting at $n$ costs $c_n=1$ and reveals $x_n$ exactly. This is not Gaussian, but it has the same structure as (36.12)–(36.14).
- No prospecting: $\max(5,5)=5$.
- Prospect: with probability $1/2$ you see 10 and pick site $n$ (get 10). With probability $1/2$ you see 0 and pick site 1 (get 5). Expected utility $=-1+0.5\cdot10+0.5\cdot5=-1+7.5=6.5$.
- Gain over not prospecting: $6.5-5=1.5>0$, so prospect. If $c_n=3$, the gain is $7.5-3-5=-0.5$, so do not.
- Less uncertainty, same mean: if $x_n\in\{4,6\}$ with probability $1/2$ each, prospecting yields $0.5\cdot6+0.5\cdot5=5.5$ before cost. The gain is $0.5$ instead of $2.5$. Greater uncertainty makes prospecting more valuable, as Figure 36.1 indicates.

## Concepts
- [[expected-utility-maximization]] (new) — choose $a$ maximizing $\int U(x,a)P(x\mid a)\,d^Kx$ (p. 451)
- [[utility-function]] (new) — the payoff $U(x,a)$; may be hard to choose, may be nonlinear, and may not exist for some people's preferences (pp. 451, 454)
- [[loss-function]] (new) — the negative-side alternative: minimize expected loss instead (p. 451)
- [[value-of-information]] (new) — the expected gain from data that may change the action, here compared with the cost $c_n$ (p. 453)
- [[prior-distribution]] — $P(x_n)$, Gaussian with mean $\mu_n$ and variance $\sigma_n^2$ (p. 452)
- [[likelihood]] — $P(d_n\mid x_n)$, a noisy Gaussian measurement (p. 452)
- [[posterior-distribution]] — $P(x_n\mid d_n)$ with precision-weighted mean (p. 452)
- [[conjugate-prior]] — Gaussian prior with Gaussian likelihood gives a Gaussian posterior. The author does not use the term (p. 452).
- [[exploration-exploitation]] (new) — balancing information gathering against using what you know; handled approximately by reinforcement learning (p. 453)
- [[minimax-regret]] (new) — choose the action minimizing the largest possible regret; MacKay questions its justification (p. 455)
- [[kelly-criterion]] — Cover's aim of maximizing $\mathbb E[\log m(T)]$; the author does not name it so (p. 456)

## Canonical instances
- [[tanzanite-prospecting]] (new) — Gaussian mine-site choice with an optional prospecting step (p. 451)
- [[four-doors-problem]] (new) — a two-stage switching game (p. 454)
- [[allais-paradox]] (new) — common preferences that no utility function can represent (p. 454)
- [[optimal-stopping-marriage]] (new) — secretary-style stopping problem with three objectives (p. 454)
- [[lottery-ticket-minimax-regret]] (new) — regret tables and the 9/10 portfolio (p. 455)
- [[horse-race-cover-betting]] (new) — betting $b=p$ regardless of odds (p. 456)
- [[joe-shark-dice-bets]] (new) — dice bets on 6, 8 and 7 (p. 456)

## Bridges (candidates)
- [same-math] Cover's aim, maximizing $\mathbb E\log m(T)$ ↔ information-theory: Kelly criterion / doubling rate — the same objective and bets proportional to $p$.
- [same-math] Precision-weighted posterior mean (36.8) ↔ bayesian: conjugate Gaussian updating — the same formula.
- [structural-analogy] Value of prospecting data ↔ information-theory: mutual information — both measure what a signal is worth, though here in utility units rather than bits.

## Questions this raises
- When should utility be nonlinear so that $\sigma_n$ matters, and how would (36.14) change?
- How does the single-prospecting analysis extend to prospecting at several sites in sequence?
- If preferences like Allais's cannot be coherent utilities, which assumption should be dropped: the preferences or the expected-utility rule?
- When, if ever, is minimax regret a defensible objective?

## Exercises worth doing
- Ex. 36.1 (p. 452) — Gaussian prior and posterior algebra behind the whole chapter — difficulty: medium
- Ex. 36.4 (p. 454) — multi-stage decision with information from the host's choices — difficulty: medium
- Ex. 36.5 (p. 454) — proving the Allais preferences are inconsistent with any $U$ — difficulty: medium
- Ex. 36.6 (pp. 454–455) — optimal stopping under different utilities — difficulty: hard
- Ex. 36.7 (p. 455) — whether minimax regret is justifiable — difficulty: medium
- Ex. 36.8 (pp. 455–456) — log-wealth betting and "ignoring the odds" — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 463–468 are printed 451–456).
- The text layer is garbled in (36.12)–(36.14) and the Figure 36.1 axes. I checked them against the page image.
- **Apparent misprint in (36.13):** the image prints $-\mu_1$ if $\mu_1\ge\mu_n$ and $-\mu_n$ if $\mu_1\le\mu_n$. This conflicts with (36.10) and with (36.14), which follow only if the values are $+\mu_1$ and $+\mu_n$. I used the positive values (added step above).
- (36.16) is printed with exponent $nW(b,p)$, although the horizon was called $T$. It may be a misprint; reproduced as printed.
- Exercise 36.4 refers to exercise 3.8 (p. 57), which is outside this unit.
- Figure 36.1 shows only contours; I did not read values off it.
