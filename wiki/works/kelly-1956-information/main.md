---
id: kelly-1956-information/main
work: kelly-1956-information
unit: paper
pages: 917–926
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A New Interpretation of Information Rate

## L0 — One line
A gambler who receives a noisy "private wire" about a chance event and bets, each time, a fraction of capital set by his posterior beliefs can make his capital grow exponentially (the odds being fair). With fair odds, the best growth rate equals Shannon's information rate.

## L1 — The gist (≤ 120 words)
Shannon's transmission rate had meaning only through his coding theorem. Kelly asks whether the rate means anything when no coding is used. He models a gambler who gets noisy advance news of a chance event and bets repeatedly, reinvesting winnings. The gambler maximizes the exponential growth rate $G$ of his capital. With fair odds, maximum $G$ equals Shannon's rate $R=H(X)-H(X/Y)$. With unfair odds and no track take, $R$ is the extra growth due to the channel. With a track take (the house's cut), the formulas are more complex. The strategy is log-optimal: it maximizes the expected log of capital.

**Prerequisites:** logarithms (base 2); probability and the law of large numbers; conditional and joint probability; basic partial derivatives; Shannon entropy $H$.

## L2 — Key ideas (5–10 bullets)
- Shannon's rate had significance only via the coding theorem. Kelly gives it a meaning where no coding is contemplated (p. 917).
- An arbitrary combination of a channel and a cost function does not necessarily make a communication system. So Kelly analyses a real situation, a gambler with a private wire (p. 918).
- The growth rate is $G=\lim \frac1N\log\frac{V_N}{V_0}$. Betting everything maximizes expected capital but ruins the gambler with probability one if he continues indefinitely. Betting a fraction does better (pp. 919–920).
- For a noisy binary channel with fair odds, $G_{\max}=1+p\log p+q\log q=R$ (p. 920).
- In general with fair odds, betting $a(s/r)=q(s/r)$ gives $G_{\max}=H(X)-H(X/Y)$ (p. 922).
- With unfair odds and no track take, the bets are the same and the posted odds are ignored. $R$ is the gain due to the channel, and any deviation from fair odds helps the gambler (pp. 922–923).
- With a track take, the optimal bets come from setting the derivatives of $G$ equal to a constant $k$. Only outcomes with $p(s)\alpha_s$ above a threshold are bet on (pp. 923–925).
- The log criterion is justified by additivity and the law of large numbers, not by the gambler's value function. Optimality is proved only against fixed-fraction rules (pp. 925–926).

## L3 — Walkthrough

### Introduction (pp. 917–918)
Shannon's rate has meaning through his theorem on encoding binary digits at that rate with arbitrarily small error. Some workers assume it also has meaning without coding, for example in radar detectors designed for minimum equivocation. Kelly says this is unjustified without further analysis (p. 917).
For a system with errors, Kelly says the problem seems to have but one solution: a cost function on (signal, received symbol) pairs whose expected value is meaningful, for example obtained from von Neumann utility theory. That cost would depend on things outside the system, so its average could not be identified with Shannon's rate. Kelly believes such an approach is too general to shed light on the specific problems of communication theory. The distinguishing feature of a communication system is that the receiver can profit from knowing the input symbols or their probabilities better. An arbitrary pairing of channel and cost function need not be a communication system (p. 918). Kelly therefore picks a real situation: a gambler who bets using the received symbols (p. 918).

### The gambler with a private wire (pp. 918–920)
A channel carries the result of a chance event before it becomes common knowledge, so bets are still available at the original odds (p. 918).
- **Noiseless binary channel** (for example, results of games between equally matched teams): the gambler can get even-money bets although he already knows each result; he would probably bet all he has and then have $2^N V_0$ after $N$ bets (p. 919).
- **Growth rate:** $G=\lim_{N\to\infty}\frac1N\log\frac{V_N}{V_0}$, with $\log$ base 2. In the noiseless example $G=1$ (p. 919).
- **Noisy channel** (error probability $p$, correct $q$): betting everything maximizes $\langle V_N\rangle=(2q)^N V_0$. But the gambler is broke with probability one if he continues indefinitely (p. 919).
- **Fractional betting:** with fraction $\ell$ bet each time, $V_N=(1+\ell)^W(1-\ell)^L V_0$, with $W$ wins and $L$ losses. Then, with probability one,
$$G=\lim\Big[\tfrac WN\log(1+\ell)+\tfrac LN\log(1-\ell)\Big]=q\log(1+\ell)+p\log(1-\ell).$$
- **Maximizing:** the maximum of $Z=\sum X_i\log Y_i$ subject to $\sum Y_i=Y$ is at $Y_i=\frac YX X_i$, where $X=\sum X_i$. This follows directly from the convexity of the log (pp. 919–920).
- **Result:** put $1+\ell=2q$ and $1-\ell=2p$. Then $G_{\max}=1+p\log p+q\log q=R$, Shannon's rate (p. 920).
- **Objection:** one might say the gambler should bet everything to maximize expected win after $N$ bets. **Kelly replies:** he grants that for a game stopped after $N$ bets the answer would depend on the relative values (to the gambler) of being broke or having a fortune; but in a nonterminating game, the gambler using the $\ell$ found above eventually gets ahead of one using any other $\ell$, and stays ahead, with probability one. He assumes the gambler maximizes $G$ (p. 920).

*Intuition note:* Betting everything has a huge average but almost always ends in ruin. The strategy Kelly assumes maximizes $G$, the typical growth rate of the log of capital. With fair odds this typical growth rate is exactly the channel's information rate.

### The general case (pp. 920–922)
Notation: $p(s)$ is the probability that symbol $s$ is sent. $p(r/s)$ is the probability of receiving $r$ given $s$ was sent. $p(s,r)$ is the joint probability. $q(r)$ is the received-symbol probability, and $q(s/r)$ is the probability of $s$ given $r$. $\alpha_s$ is the odds, that is, dollars returned per one-dollar bet. $a(s/r)$ is the fraction of capital bet on $s$ after seeing $r$ (p. 920). Only independent transmitted symbols and independent noise are considered (p. 921).

**Fair odds** means $\alpha_s=1/p(s)$. Without a track take, $\sum 1/\alpha_s=1$ because all money collected is paid to the winner. If $\alpha_s>1/p(s)$ for some $s$, a bettor could insure a profit by repeated bets on $s$. The extra betting would lower $\alpha_s$. Kelly says that in parimutuel betting there is a tendency for the odds to be fair (ignoring the track take), and that the same feedback probably operates in more complicated cases such as stock market speculation (p. 921).

There is no loss of generality in setting $\sum_s a(s/r)=1$, since the gambler can hold back money by placing canceling bets (p. 921). With $W_{sr}$ the number of times $s$ is sent and $r$ received:
$$V_N=\prod_{r,s}[a(s/r)\alpha_s]^{W_{sr}}V_0,\qquad \log\frac{V_N}{V_0}=\sum_{rs}W_{sr}\log\alpha_s a(s/r),$$
$$G=\lim_{N\to\infty}\frac1N\log\frac{V_N}{V_0}=\sum_{rs}p(s,r)\log\alpha_s a(s/r)\ \text{with probability one.}\tag{1}$$
With $\alpha_s=1/p(s)$ (p. 922):
$$G=\sum_{rs}p(s,r)\log\frac{a(s/r)}{p(s)}=\sum_{rs}p(s,r)\log a(s/r)+H(X),$$
where $H(X)$ is Shannon's source rate. The first term is maximized by
$$a(s/r)=\frac{p(s,r)}{\sum_k p(k,r)}=\frac{p(s,r)}{q(r)}=q(s/r).$$
Then $G_{\max}=H(X)-H(X/Y)$, Shannon's rate (p. 922).

*Intuition note:* The gambler bets in proportion to his posterior probability of each symbol, after seeing what arrived. The uncertainty removed by the channel is what he converts into growth.

### When the odds are not fair (pp. 922–923)
Assume no track take, $\sum 1/\alpha_s=1$, but $\alpha_s$ not necessarily $1/p(s)$. Setting $\sum_s a(s/r)=1$ is still allowed. Then $G=\sum_{rs}p(s,r)\log a(s/r)+\sum_s p(s)\log\alpha_s$. $G$ is still maximized by $a(s/r)=q(s/r)$, and
$$G_{\max}=-H(X/Y)+\sum_s p(s)\log\alpha_s=H(\alpha)-H(X/Y),\qquad H(\alpha)=\sum_s p(s)\log\alpha_s.$$
Kelly lists three facts (pp. 922–923):
- (a) The gambler ignores the posted odds when placing bets.
- (b) $H(\alpha)$ subject to $\sum 1/\alpha_s=1$ is minimal at $\alpha_s=1/p(s)$, where $H(\alpha)=H(X)$. So any deviation from fair odds helps the gambler.
- (c) With no inside information the gain would be $H(\alpha)-H(X)$. So $R=H(X)-H(X/Y)$ is the increase of $G_{\max}$ due to the channel. With no channel, $H(X/Y)=H(X)$, and $G_{\max}$ is minimized (at zero) by $\alpha_s=1/p_s$. This gives further meaning to "fair odds."

### When there is a "track take" (pp. 923–925)
The gambler can no longer cancel bets, so $\sum_s a(s/r)=1$ cannot be assumed. Let $b_r=1-\sum_s a(s/r)$ be the fraction not bet. Maximize
$$G=\sum_{rs}p(s,r)\log[b_r+\alpha_s a(s/r)]\tag{2}$$
subject to $b_r+\sum_s a(s/r)=1$. Terms for different $r$ are independent, so it suffices to maximize, for each $r$, $G_r=q(r)\sum_s q(s/r)\log[b_r+\alpha_s a(s/r)]$ under the same constraint (p. 923). Each such term has the form of the no-channel gain
$$G=\sum_s p(s)\log[b+\alpha_s a(s)].\tag{3}$$
Kelly maximizes (3) and reads the result either as a typical term of the general problem or as the total gain with no channel (p. 924).

Let $\lambda$ be the set of $s$ with $a(s)>0$, and $\lambda'$ the set with $a(s)=0$. At the maximum, with $k$ a constant (p. 924):
$$\frac{\partial G}{\partial a(s)}=\frac{p(s)\alpha_s}{b+a(s)\alpha_s}\log e=k\ (s\in\lambda),\quad \frac{\partial G}{\partial b}=\sum_s\frac{p(s)}{b+a(s)\alpha_s}\log e=k,\quad \frac{\partial G}{\partial a(s)}=\frac{p(s)\alpha_s}{b}\log e\le k\ (s\in\lambda').$$
These give $k=\log e$, $b=\frac{1-p}{1-\sigma}$, and $a(s)=p(s)-\frac b{\alpha_s}$ for $s\in\lambda$. Here $p=\sum_\lambda p(s)$ and $\sigma=\sum_\lambda 1/\alpha_s$. The inequalities give $p(s)\alpha_s\le b=\frac{1-p}{1-\sigma}$ for $s\in\lambda'$. The conditions $\sigma<1$, $p(s)\alpha_s>\frac{1-p}{1-\sigma}$ on $\lambda$, and $\le$ on $\lambda'$ completely determine $\lambda$ (p. 924).

Order the indices so that $p(s)\alpha_s\ge p(s+1)\alpha_{s+1}$. Then $\lambda$ must consist of all $s\le t$, with $t$ a positive integer or zero. Define $F_t=\frac{1-p_t}{1-\sigma_t}$ with $p_t=\sum_1^t p(s)$, $\sigma_t=\sum_1^t 1/\alpha_s$, $F_0=1$ (p. 925).
- If $p(1)\alpha_1<1$, $F_t$ increases with $t$ until $\sigma_t\ge1$. Then $t=0$ works and $\lambda$ is empty.
- If $p(1)\alpha_1>1$, $F_t$ decreases with $t$ until $p(t+1)\alpha_{t+1}<F_t$ or $\sigma_t\ge1$. In the former case $F_{t+1}>F_t$, and $F$ then increases until $\sigma_t\ge1$.
- The desired $t$ gives $F_t$ its minimum positive value (the smallest such $t$ if there are several) (p. 925).

**Procedure** (p. 925):
- (a) Order indices as above.
- (b) Set $b$ to the minimum positive value of $\frac{1-p_t}{1-\sigma_t}$.
- (c) Set $a(s)=p(s)-b/\alpha_s$, or zero, whichever is larger. The $a(s)$ sum to $1-b$.

$$G_{\max}=\sum_1^t p(s)\log p(s)\alpha_s+(1-p_t)\log\frac{1-p_t}{1-\sigma_t},$$
with $t$ the smallest index giving the minimum. If $p(s)\alpha_s<1$ for all $s$, no bets are placed. If the largest $p(s)\alpha_s>1$, some bets might be made on events with $p(s)\alpha_s<1$, that is, with negative expected gain. This violates the criterion of the classical gambler, who never bets on such an event (p. 925).

*Skip path:* carry forward the rule "bet on outcome $s$ only if $p(s)\alpha_s>b$, with $b=\frac{1-p}{1-\sigma}$ minimized over $t$."

### Conclusion (pp. 925–926)
Kelly's gambler maximizes the expected log of capital at every bet. This is not because of his value function. It is because the log is additive over repeated bets and the law of large numbers applies to it (pp. 925–926).
- If the wife lets him bet one dollar a week but not reinvest, he should maximize expected capital on each bet. That means betting everything on the event with the highest expectation, and he then gets ahead of anyone dividing his money differently, with probability one (p. 926).
- **Limit of proof:** Kelly shows only that this gambler surpasses, with probability one, any gambler using a fixed rule per received symbol, independent of time or past events. Theorems remain to be proved showing in what sense, if any, his strategy is superior to others with non-constant $a(s/r)$ (p. 926).
- **Scope:** the model may fit other economic situations. It needs reinvestment of profits and the ability to vary the amount invested across categories. The "channel" may be a real channel or the totality of the investor's inside information (p. 926).
- **Summary (p. 926):** betting in the same proportion each time a given symbol is received makes capital grow (or shrink) exponentially. With fair odds the maximum rate equals the rate of transmission. With odds consistent with some other probabilities, the maximum rate exceeds the no-channel rate by the rate of transmission. With a track take, similar results hold, but the formulae are more complex and have less direct information-theoretic interpretations.

## Toy example (ours)
Binary channel with $p=0.1$ (error), $q=0.9$, fair odds of 2 per symbol.
- Optimal fraction: $\ell=q-p=0.8$, so $1+\ell=1.8=2q$ and $1-\ell=0.2=2p$.
- $G=0.9\log_2 1.8+0.1\log_2 0.2=0.9(0.8480)+0.1(-2.3219)=0.7632-0.2322=0.5310$ bits per bet.
- Check: $R=1+0.1\log_2 0.1+0.9\log_2 0.9=1-0.3322-0.1368=0.5310$. ✓.
- Try $\ell=0.5$: $0.9\log_2 1.5+0.1\log_2 0.5=0.9(0.5850)-0.1=0.4265<0.5310$.
- Try $\ell=1$: the first error gives $\log_2 0=-\infty$, so ruin. Yet $\langle V_N\rangle=1.8^N V_0$ is largest, as Kelly notes (p. 919).

## Concepts
- [[kelly-criterion]] — bet fractions chosen to maximize the exponential growth rate $G$, equivalently the expected log of capital (pp. 919, 925)
- [[rate-of-transmission]] (new) — Shannon's $R=H(X)-H(X/Y)$; here it equals the maximum growth rate at fair odds (p. 922)
- [[fair-odds]] (new) — odds $\alpha_s=1/p(s)$; with no channel, fair odds minimize $G_{\max}$ (at zero) (pp. 921, 923)
- [[asymmetric-information]] — the gambler's inside information (private wire, a noisy channel) gives him an edge (p. 918)
- [[track-take]] (new) — the percentage the track keeps; the gambler loses a percentage, so he cannot make canceling bets (p. 923)

## Canonical instances
- [[private-wire-gambler]] — gambler receives results through a noisy channel before the odds adjust (p. 918)
- [[baseball-noiseless-wire]] — equally matched teams; capital doubles each bet, $G=1$ (p. 919)
- [[wife-one-dollar-week]] — without reinvestment the gambler should bet all on the highest-expectation event (p. 926)

## Bridges (candidates)
- [same-math] Kelly growth rate $G_{\max}=H(X)-H(X/Y)$ ↔ information theory: Shannon's channel rate $R$ — same formula, a new interpretation.
- [structural-analogy] Gambler with a private wire ↔ asymmetric information: informed vs uninformed traders — the informed side profits from information.
- [structural-analogy] Odds adjusting as extra bets arrive (p. 921) ↔ price as signal: market feedback pushes odds toward fair.

## Questions this raises
- In what sense, if any, is the log-optimal strategy superior to strategies where $a(s/r)$ varies with time or history (p. 926)?
- How well does the model fit real investing, given the need to reinvest and to vary exposure across categories (p. 926)?
- How do the track-take formulas relate to information measures, given Kelly says they have less direct interpretations (p. 926)?

## Reading notes
- Printed page numbers are not in the page labels but are visible on the images (917–926). Offset: printed = pdf + 916.
- The text layer is empty; all content was read from the images.
- Misprints: p. 919 "probability, $p$, or error" (should read "of error"). On p. 925 "$p(1)\alpha_r<1$" should read $p(1)\alpha_1<1$.
- Kelly writes $p_s$ and $p(s)$ interchangeably (p. 923).
- Kelly's "log" is base 2 (p. 919); the $\log e$ factors on p. 924 convert the derivative.
