---
id: jaynes-2003-probability/ch14-simple
work: jaynes-2003-probability
unit: "14 Simple applications of decision theory"
pages: 426-450
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Simple applications of decision theory

## L0 — One line
Signal-detection decision theory is ordinary Bayesian inference plus a loss function, so the classical criteria discussed here all reduce to a likelihood-ratio test whose threshold is the only thing they disagree about; the "widget problem" shows maximum-entropy priors, with no new data, can drive a decision.

## L1 — The gist (≤ 120 words)
Jaynes asks how the 1950s decision-theory literature on detecting a signal in noise relates to plain Bayesian inference. He argues that the minimax, Bayes, Neyman–Pearson and ideal-observer criteria all lead to a likelihood-ratio test (compare $p(V|S_1)/p(V|S_0)$ with a threshold) and differ only in the threshold. A "robot" that computes posterior odds and minimises expected loss reaches the same rule in two lines. The second application, the widget problem, uses maximum-entropy priors with no new data. It leads to the mathematics of statistical mechanics (harmonic oscillators, a Bose–Einstein gas). Jaynes concludes that the Laplace–Jeffreys interpretation of probability, not the frequency one, widens the range of problems it can treat.

**Prerequisites:** product rule and Bayes' theorem; expected loss; Gaussian cdf; maximum entropy with Lagrange multipliers (Ch. 11); geometric series; central limit theorem.

## L2 — Key ideas
- A decision rule is designed to depend on the data $V$ alone, $p(D|V)=p(D|VY)$; this is a fact about the apparatus, not a relaxation of Bayesian rules (p. 428).
- A decision $D$ is as good as $V$ for judging $Y$ iff $p(V|D)=p(V|YD)$ (sufficiency: $D$ carries all that $V$ says about $Y$). In expected entropy, zero information loss from $V$ to $D$ is equivalent to sufficiency. This holds only on average, not for every outcome (pp. 429–430).
- With a fixed loss function, the Bayes rule picks, for each $V$, the decision minimising $K(D,V)$ (the loss of that decision weighted by the joint probability of $V$ and each signal). In general it is non-random; at threshold values of $V$ (ties) randomised rules are equally good (p. 432).
- For two signals the optimum receiver computes the likelihood ratio $p(V|S_1)/p(V|S_0)$ and compares it with $qL_a/(pL_r)$. Losses and priors move only the threshold (p. 433).
- In the single-sample Gaussian example, the minimax rule is the Bayes rule for a worst-case prior ratio. The Neyman–Pearson rule is the Bayes rule for the prior/loss ratio that gives the chosen false-alarm rate (the probability of deciding "signal" when none is present) (pp. 434–437).
- The robot computes posterior odds and thresholds them at $L_a/L_r$, which is identical to (14.32). Jaynes's reading is that Wald's theory contains nothing beyond probability theory plus a loss function (p. 438).
- The classical matched filter and the Bayesian rule coincide for a linear system with Gaussian noise; the log-odds is linear in $V$ (p. 440).
- Widget Stages 2–3: maximum entropy gives geometric (exponential) priors on demand, with the same equations as the harmonic oscillator and the Bose–Einstein gas. Expected losses select yellow, then red (pp. 443–449).
- Stage 4 (a specific order for 40 green) keeps decision red, but the margin is small, which is why common sense fails (p. 450).

## L3 — Walkthrough

**Introduction (p. 426).** Jaynes says detecting a signal in noise is the same problem as Laplace's search for unknown systematic influences and Shewhart's search for drift in machine characteristics. Statisticians call it a "significance test". The tools needed are Chapters 2 and 4, a loss function to turn probabilities into decisions, and maximum entropy for priors if needed. The literature (Middleton and Van Meter, Middleton 1960) uses older vocabulary, so this chapter is a condensed translation (p. 426).

### 14.1 Definitions and preliminaries
- Everything follows from the product rule (p. 427):
$$p(AB|C)=p(A|BC)p(B|C)=p(B|AC)p(A|C)\tag{14.2}$$
- If $B$ and $C$ are not mutually contradictory, Bayes' theorem follows (p. 427):
$$p(A|BC)=p(A|C)\frac{p(B|AC)}{p(B|C)}=p(A|B)\frac{p(C|AB)}{p(C|B)}\tag{14.3}$$
- For mutually exclusive, exhaustive $B_i$ (p. 427):
$$p(A|C)=\sum_i p(A|B_iC)p(B_i|C)\tag{14.4}$$
- Notation (14.6)–(14.8): $X$ = prior knowledge, $S$ = signal, $N$ = noise, $V=V(S,N)$ = observed voltage, $D$ = decision. $p(N|X)=W(N)$. In a linear system $V=S+N$ and $p(V|S)=W(V-S)$ (p. 427).
- A decision rule $p(D|V)$ is 0/1-valued if always made in a definite way. It may also be "randomized", a true probability distribution (pp. 427–428).
- The decision must use $V$ alone. For any other proposition $Y\neq D$,
$$p(D|V)=p(D|VY)\tag{14.9}$$
Jaynes says this is part of the prior information $X$: our design makes $Y$ irrelevant. The robot has not relaxed its rules (p. 428).
- Equivalently, $D$ depends on $Y$ only through $V$:
$$p(D|Y)=\sum_V p(D|V)p(V|Y)\tag{14.10}$$
Jaynes calls this a "Huygens principle" for logic: $p(V|Y)$ are amplitudes and $p(D|V)$ the wavelets (p. 428).

*Intuition note.* The apparatus passes only $V$ onwards, so everything else can influence the decision only by changing $V$. This is a built-in conditional-independence assumption.

### 14.2 Sufficiency and information
- From the product rule and (14.9) (p. 428):
$$p(DY|V)=p(Y|VD)p(D|V)=p(D|VY)p(Y|V)\tag{14.11}$$
$$p(Y|VD)=p(Y|V)\tag{14.12}$$
So once $V$ is known, $D$ is redundant for any other quantity (p. 428).
- Using the product rule the other way (p. 429):
$$p(VY|D)=p(Y|VD)p(V|D)=p(Y|D)p(V|YD)\tag{14.13}$$
- **Theorem.** If $D$ is a possible decision given $V$, then $p(V|D)\neq0$ and
$$p(Y|V)=p(Y|D)\iff p(V|D)=p(V|YD)\tag{14.14}$$
Combining (14.12) and (14.13) gives this (p. 429). In words, $D$ is as good as $V$ for judging $Y$ iff $Y$ is irrelevant to $V$ given $D$. Equivalently, given $D$, $Y$ and $V$ are independent (p. 429):
$$p(YV|D)=p(Y|D)p(V|D)\tag{14.15}$$
This is called "sufficient statistic" in the literature. Jaynes says the link to his Chapter 8 definition is still to be checked (p. 429).
- Such a rule need not exist: (14.15) must hold for all $Y$, $V$ and all $D$ with $p(D|V)\neq0$ (p. 429).
- Information in Shannon's sense (p. 429):
$$H_D(Y)=-\sum_Y p(Y|D)\log p(Y|D),\qquad \overline H_D(Y)=\sum_D p(D|X)H_D(Y)\tag{14.16, 14.17}$$
If $\overline H_C(Y)<\overline H_D(Y)$, then "on the average" $C$ carries more information about $Y$ than $D$. This may fail for specific values of $C$, $D$ (p. 430).
- Extra data cannot raise $\overline H$ on average (p. 430):
$$\overline H_V(Z)-\overline H_{DV}(Z)=\sum_{DVZ}p(DV|X)p(Z|DV)\log\frac{p(Z|DV)}{p(Z|V)}\tag{14.19}$$
Use $\log x\ge 1-x^{-1}$, with equality iff $x=1$:
$$\overline H_V(Z)-\overline H_{DV}(Z)\ge\sum_{DVZ}p(DV|X)[p(Z|DV)-p(Z|V)]=0\tag{14.20}$$
So $\overline H_{DV}(Z)\le\overline H_V(Z)$, with equality iff (14.12) holds for all $D,V,Z$ with $p(DV|X)\ne0$ (p. 430).
- The inequality holds regardless of the meaning of $D$ and $V$. Printed as (14.21): $\overline H_D(Y)\ge\overline H_{DV}(Z)\le\overline H_V(Z)$. Take $Z=Y$. By (14.12), $\overline H_V(Y)=\overline H_{DV}(Y)$ (added step: (14.20) with the roles of $D$ and $V$ exchanged gives $\overline H_D(Y)\ge\overline H_{DV}(Y)$), so
$$\overline H_V(Y)\le\overline H_D(Y)\tag{14.22}$$
with equality iff (14.15) holds, i.e. iff $D$ is sufficient (p. 430).
- Conclusion: if "information" means minus the expected entropy of $Y$, zero information loss from $V$ to $D$ is equivalent to sufficiency of $D$. The inequality holds for expectations only. A specific observation that an improbable event occurred may raise the entropy of $Y$. Jaynes says that is "less certainty", not less information in the colloquial sense, so "information" is "not a happy choice of words" (p. 430).

*Intuition note.* Processing $V$ into a decision can lose information about $Y$. It loses none exactly when, given the decision, $V$ tells nothing more about $Y$. On average, new data never leave you more uncertain, though a single surprising observation (an event previously thought improbable) can.

### 14.3 Loss functions and criteria of optimum performance
- A loss function $L(D,S)$ says how serious it is to decide $D$ when $S$ is present. With two signals $S_0=0$ and $S_1>0$ and two decisions, there are two errors: the *false alarm* $A=(D_1,S_0)$ and the *false rest* $R=(D_0,S_1)$ (p. 431).
- Example: a false rest is ten times as serious as a false alarm, correct decisions cost nothing (p. 431):
$$L_{ij}=\begin{pmatrix}0&10\\1&0\end{pmatrix}\tag{14.23}$$
- Jaynes also mentions an information loss $L(D,S)=-\log p(S|D)$. This depends on the decision rule, and he says it seems never to have been clarified in what sense the minimising rule is "as close as possible" to sufficient (p. 431).
- Conditional loss and average loss (p. 431):
$$L(S)=\sum_D L(D,S)p(D|S)\tag{14.24}$$
$$\langle L\rangle=\sum_S L(S)p(S|X)\tag{14.25}$$
- **Minimax criterion:** minimise $[L(S)]_{\max}$. Jaynes calls it "in a sense too conservative", but it needs no prior $p(S|X)$ (p. 431).
- **Bayes criterion:** minimise $\langle L\rangle$; needs a prior (p. 431).
- Earlier ad hoc criteria: Neyman–Pearson fixes one error probability $\epsilon$ and minimises the other, $\delta$. Siegert's "ideal observer" minimises $\epsilon+\delta$. Jaynes says their mathematical identity surprised early workers: all are special cases of the Bayes criterion for particular priors (p. 432).
- Bayes solution: substituting (14.24), (14.10), (14.9) into (14.25) gives (p. 432)
$$\langle L\rangle=\sum_{DV}\Big[\sum_S L(D,S)p(VS|X)\Big]p(D|V)\tag{14.26}$$
If $L(D,S)$ does not depend on $p(D|V)$, no $p(D|V)$ makes this stationary in the calculus-of-variations sense. So $\langle L\rangle$ is minimised by choosing, for each $V$, the decision $D_1(V)$ with the smallest coefficient (p. 432):
$$K(D,V)\equiv\sum_S L(D,S)p(VS|X)\tag{14.27}$$
(the page prints $L(D_1,S)$ inside the sum). The rule is $p(D|V)=\delta(D,D_1)$ (14.28). It is generally nonrandom. In the degenerate case $K(D_1,V)=K(D_2,V)$, any $p(D|V)=a\delta(D,D_1)+b\delta(D,D_2)$ with $a+b=1$ is equally good (14.29). Degeneracy occurs at threshold values of $V$ (p. 432).

*Intuition note.* Minimising average loss is done outcome by outcome: for each $V$, pick the cheapest decision given how likely each signal is with that $V$. At ties, randomised rules are just as good.

### 14.4 A discrete example
- Two signals, loss matrix $L_{ij}=\begin{pmatrix}0&L_r\\L_a&0\end{pmatrix}$ (14.30), where $L_a$ is the false-alarm loss and $L_r$ the false-rest loss. Then $K(D_0,V)=L_rp(VS_1|X)$ and $K(D_1,V)=L_ap(VS_0|X)$ (14.31) (p. 433).
- Decision rule: choose $D_1$ if $p(VS_1|X)/p(VS_0|X)>L_a/L_r$, choose $D_0$ if less, choose at random if equal (14.32). With priors $p(S_1|X)=p$ and $p(S_0|X)=q=1-p$ (14.33) (p. 433):
$$\text{choose }D_1\text{ if }\frac{p(V|S_1)}{p(V|S_0)}>\frac{qL_a}{pL_r}\tag{14.34}$$
- The left side is a likelihood ratio, which depends only on the noise pdf. Loss and prior affect only the threshold. A receiver that outputs the ratio gives all the information needed for optimum Bayes decisions. No assumption about signal type, linearity or noise was needed (p. 433).
- **Gaussian single-sample case.** Voltage observed at one instant; signal amplitude is $S_1$ or $0$. Noise has pdf $W(N)=(2\pi\sigma^2)^{-1/2}\exp\{-N^2/2\sigma^2\}$ (14.35). The ratio is
$$\frac{p(V|S_1)}{p(V|S_0)}=\frac{W(V-S_1)}{W(V)}=\exp\Big\{\frac{2VS_1-S_1^2}{2\sigma^2}\Big\}\tag{14.36}$$
This is monotonic in $V$, so the rule is "choose $D_1$ when $V>V_b$, $D_0$ when $V<V_b$" (14.37), with $s\equiv S_1/\sigma$ (signal-to-noise ratio) and $v\equiv V/\sigma$ (p. 434):
$$\frac{V_b}{\sigma}=\frac1{2s}\Big[2\log\Big(\frac{qL_a}{pL_r}\Big)+s^2\Big]=v_b\tag{14.38}$$
- Error probabilities, with $\Phi$ the cumulative normal distribution (p. 434):
$$p(R|X)=p\int_{-\infty}^{V_b}dV\,W(V-S_1)=p\,\Phi(v_b-s)\tag{14.40}$$
$$p(A|X)=q\int_{V_b}^{\infty}dV\,W(V)=q[1-\Phi(v_b)]\tag{14.41}$$
$\Phi(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}dt=\frac12[1+\operatorname{erf}(x)]$ (14.42) as printed. For $x>2$, $1-\Phi(x)\approx e^{-x^2/2}/(x\sqrt{2\pi})$ (14.43) (p. 434).
- Numerical case $L_r=10L_a$, $q=10p$: the log term vanishes, so $v_b=s/2$ and
$$p(A|X)=10\,p(R|X)=\tfrac{10}{11}[1-\Phi(s/2)]\tag{14.44}$$
Jaynes states: false alarm below 0.027 and false rest below 0.0027 for $s>4$. For $s>6$ the numbers are $1.48\times10^{-3}$ and $1.48\times10^{-4}$ (p. 435).
- **Minimax in this example.** With $f(V)\equiv p(D_1|V)\in[0,1]$, the conditional losses are (p. 435)
$$L(S_0)=L_a\!\int dV\,p(D_1|V)W(V),\quad L(S_1)=L_r\!\int dV\,p(D_0|V)W(V-S_1)\tag{14.45}$$
Any change $\delta f(V)$ raises one of these and lowers the other. So at the minimax solution $L(S_0)=L(S_1)$ (p. 435).
- If some prior makes the Bayes rule give $L(S_0)=L(S_1)$, then $\langle L\rangle=[L(S)]_{\max}$. Since the Bayes rule minimises $\langle L\rangle$ over all rules, it also does so over the smaller class keeping $L(S_0)=L(S_1)$, so it is the minimax rule. Hence the minimax rule is a threshold rule, $f(V)=0$ for $V<V_m$ and $1$ for $V>V_m$ (14.46), with
$$L_a\int_{V_m}^\infty dV\,W(V)=L_r\int_{-\infty}^{V_m}dV\,W(V-S_1)\tag{14.47}$$
$$L_a[1-\Phi(v_m)]=L_r\Phi(v_m-s)\tag{14.48}$$
(p. 435).
- For any threshold $V_0$, $p(R|S_1)=\Phi(v_0-s)$ and $p(A|S_0)=\frac12[1-\Phi(v_0)]$ as printed (14.49) (p. 435).
- Some ratio $p/q$ gives $V_b=V_m$ (from 14.38). For other ratios the Bayes rule has lower expected loss than minimax, though one of $L(S_0)$, $L(S_1)$ then exceeds the minimax value (p. 435).
- Fig. 14.1 plots $L(S_0)$, $L(S_1)$ and $\langle L\rangle$ against the threshold. The minimax threshold is the common crossing point and the Bayes threshold is the minimum of $\langle L\rangle$. The $p/q$ giving $V_b=V_m$ also gives the largest $\langle L\rangle_{\min}$. So "maximin" (find the Bayes rule for each prior, then take the worst prior) yields the same rule as minimax (p. 436).
- **Neyman–Pearson.** Fix $p(D_1|S_0)=\epsilon$ and minimise $p(D_0|S_1)$. The Bayes rule minimises $\langle L\rangle=pL_rp(D_0|S_1)+qL_ap(D_1|S_0)$ (14.50) over all rule variations, hence also over those holding $p(D_1|S_0)$ fixed. So it solves the Neyman–Pearson problem if $qL_a/pL_r$ is chosen to give the assumed $\epsilon$ (pp. 436–437). Then
$$\Phi(v_{np})=1-\epsilon,\qquad p(D_1|S_1)=\Phi(s-v_{np})\tag{14.51, 14.52}$$
For $\epsilon=10^{-3}$, detection probability is at least 99% for $s>6$ (p. 437).
- These numbers depend critically on the Gaussian noise assignment. Jaynes says it is well known that in one sense Gaussian noise is the worst kind: because of its maximum entropy properties it can obscure a weak signal more completely than any other noise of the same average power. It is favourable for a strong signal, since large excursions beyond a few $\sigma$ are very rare. Wider-tailed noise would not give the reliability found for $s>6$. When noise results from many small independent effects, the Landon derivation (Ch. 7) and the central limit theorem make Gaussian by far the most likely (p. 437).
- Jaynes's conclusion: all criteria lead to a probability ratio test and differ only in how the threshold is chosen. Any decision process can be broken into successive binary decisions (p. 437).

*Intuition note.* The likelihood ratio is the data's whole message. Costs and prior odds only decide how large the ratio must be before you act. Minimax and Neyman–Pearson are Bayes rules for specially chosen prior/loss ratios.

### 14.5 How would our robot do it?
Jaynes says the orthodox route looks at the problem "backwards", starting from the decision. The robot first computes the posterior odds, using (4.7):
$$O(S_1|VX)=O(S_1|X)\frac{p(V|S_1)}{p(V|S_0)}\tag{14.53}$$
With loss (14.31), it chooses $D_1$ if
$$O(S_1|V)=\frac{p(S_1|V)}{p(S_0|V)}>\frac{L_a}{L_r}\tag{14.54}$$
Since $p(VS_i|X)=p(S_i|V)p(V|X)$, (14.54) is identical to (14.32). Jaynes's conclusion is that strategies, admissibility and conditional losses were unnecessary: apart from the loss function, Wald's theory contains nothing beyond probability theory used as Laplace and Jeffreys used it (p. 438).

### 14.6 Historical remarks
- Jaynes's view: decision theory did more than any other single factor to start the "Bayesian revolution". Wald's orthodox work gave, after long arguments, the results Laplace's methods give at once. The supposed distinction between statistical inference and probability theory was "entirely artificial" and wasted perhaps 1000 man-years (p. 438).
- He reports that he tried to persuade Middleton of the straight Bayesian approach, and invites the reader to judge the success by comparing Middleton (1960, Ch. 18), particularly its length, with his own derivation of (14.54). He says it seems that persons with orthodox training, though unable to deny Bayesian results on any specific problem, could never believe the methods would work on the next problem until that solution was also presented to them (pp. 438–439).

#### 14.6.1 The classical matched filter
- In the 1930s receiver design maximised signal-to-noise ratio by trial and error. The ratio (peak signal)² / mean-square noise, maximised by a variational principle, gave the "classical matched filter", discovered independently many times. Jaynes credits W. W. Hansen's 1941 memorandum as the first derivation he knows of. Peter Elias (1958) satirised the repeated rediscoveries (p. 439).
- In the 1950s, decision theory applied to a linear system with Gaussian noise gave exactly the same filter. Jaynes says this is obvious from the robot's viewpoint. In logarithmic Bayes form, the evidence for $S_1$ is increased by
$$\log\frac{p(V|S_1)}{p(V|S_0)}=\frac{(V-S_0)^2-(V-S_1)^2}{2\sigma^2}=\text{const.}+\frac{(S_1-S_0)}{\sigma^2}V\tag{14.55}$$
The posterior log-odds is linear in $V$, so the two formulations are the same problem (p. 440).
- He cites P. M. Woodword (spelled so in the text; 1953 book) as having seen much of this in the 1940s. Realistic problems have time-dependent, multichannel data, many signals and parameter estimation, but, from the Bayesian viewpoint, these need only mathematical generalisation, no new principles (p. 440).

### 14.7 The widget problem
- Origin: a 1960 Purdue symposium; solved in Jaynes (1963c), with numerical work by Tribus and Fitts (1968) (p. 440). It is a "no data" decision problem, with no new evidence and so no use of Bayes' theorem. Increasing prior information is digested by maximum entropy into a sequence of priors. It is close to a real oil-prospecting problem (pp. 440–441).
- **Setting.** Mr A decides each morning whether the day's run of 200 widgets is red, yellow or green (one colour per day). His job is to protect the advertising manager's reputation for veracity, since the factory advertises 24-hour delivery on any size order (p. 441).
- **Stage 1.** Stock is 100 red, 150 yellow, 50 green. Jaynes says common sense will probably tell Mr A to build up the green stock (p. 441).
- **Stage 2.** Last year's sales were 13 000 red, 26 000 yellow, 2600 green over 260 days, i.e. 50, 100, 10 per day. Intuitive decision: yellow (p. 442).
- **Stage 3.** Last year's orders were 173 red, 2600 yellow, 130 green. Average order sizes are $13\,000/173=75$, $26\,000/2600=10$, $2600/130=20$. Intuitive decision: red (p. 442).
- **Stage 4.** An emergency order for 40 green is coming. Decision unclear to intuition (p. 442). Table 14.1 summarises the data (p. 442).
- Tribus's informal votes, as quoted from Tribus and Fitts (1968): near-unanimity on $D_1$, about 85% on $D_2$, about 70% on $D_3$, almost none on $D_4$. The majority always agreed with the formal solution for $D_1$–$D_3$, but people disagreed on why (p. 443).

#### 14.7.1 Solution for Stage 2
- Truncated problem: day-to-day decisions, no dynamic programming (p. 443). States of nature are triples $\{n_1,n_2,n_3\}$ of non-negative integers (orders for red, yellow, green). The maximum-entropy prior with fixed $\langle n_i\rangle=50,100,10$ has partition function (p. 443)
$$Z(\lambda_1,\lambda_2,\lambda_3)=\sum_{n_1,n_2,n_3=0}^\infty e^{-\lambda_1n_1-\lambda_2n_2-\lambda_3n_3}=\prod_{i=1}^3(1-e^{-\lambda_i})^{-1}\tag{14.56}$$
$$\langle n_i\rangle=-\frac{\partial\log Z}{\partial\lambda_i}=\frac1{e^{\lambda_i}-1}\tag{14.57}$$
- The prior factors, $p(n_1n_2n_3)=p_1(n_1)p_2(n_2)p_3(n_3)$ (14.58), with (p. 444)
$$p_i(n_i)=(1-e^{-\lambda_i})e^{-\lambda_in_i}=\frac1{\langle n_i\rangle+1}\Big[\frac{\langle n_i\rangle}{\langle n_i\rangle+1}\Big]^{n_i}\tag{14.59}$$
giving
$$p_1=\tfrac1{51}\big(\tfrac{50}{51}\big)^{n_1},\quad p_2=\tfrac1{101}\big(\tfrac{100}{101}\big)^{n_2},\quad p_3=\tfrac1{11}\big(\tfrac{10}{11}\big)^{n_3}\tag{14.60}$$
- Decisions: $D_1$ red, $D_2$ yellow, $D_3$ green. Mr A's judgment is that loss is zero if all orders are filled; otherwise it is proportional to, and may be taken equal to, the total number of unfilled orders, in view of the invariance of the decision rule under proper linear transformations (end of Ch. 13). With stocks $S_1=100$, $S_2=150$, $S_3=50$ and ramp $R(x)=x$ for $x\ge0$, $0$ for $x\le0$ (14.62) (p. 444):
$$L(D_1;n)=R(n_1-S_1-200)+R(n_2-S_2)+R(n_3-S_3)\tag{14.61}$$
and likewise (14.63), (14.64) with the $200$ added to $S_2$ or $S_3$.
- Expected loss (14.65) is summed term by term. The sums are elementary (p. 445):
$$\langle L\rangle_1=\langle n_1\rangle e^{-\lambda_1(S_1+200)}+\langle n_2\rangle e^{-\lambda_2S_2}+\langle n_3\rangle e^{-\lambda_3S_3}\tag{14.66}$$
and cyclically for $\langle L\rangle_2$, $\langle L\rangle_3$. Numerically
$$\langle L\rangle_1=0.131+22.48+0.085=22.70,\quad\langle L\rangle_2=6.902+3.073+0.085=10.6,\quad\langle L\rangle_3=6.902+22.48+4\times10^{-10}=29.38\tag{14.67}$$
Strong preference for $D_2$, yellow, as common sense said (p. 445).
- Jaynes remarks that Stage 2 is mathematically the harmonic oscillator of quantum statistical mechanics, which also appears in message encoding (p. 445).

*Intuition note.* Knowing only the mean, maximum entropy gives a geometric distribution of demand. The expected unfilled orders for a colour with stock $S$ is $\langle n\rangle e^{-\lambda S}$. Yellow is chosen because, in (14.67), leaving yellow unmade carries by far the largest expected unfilled orders (22.48, against 6.902 for red and 0.085 for green).

#### 14.7.2 Solution for Stage 3
- Deeper hypothesis space: $u_r$ = number of orders for $r$ red widgets each, $v_y$ for yellow, $w_g$ for green; a state is $\theta=\{u_1\cdots;v_1\cdots;w_1\cdots\}$ (14.68). Total demands are $n_1=\sum ru_r$, etc. (14.69). Numbers of orders are $m_1=\sum u_r$, etc. (14.70). Now $\langle m_i\rangle$ are also known; e.g. "average individual order 75" means $\langle n_1\rangle=75\langle m_1\rangle$ (p. 446).
- Six constraints give six multipliers. The maximum-entropy form is $p=\exp\{-\lambda_0-\lambda_1n_1-\mu_1m_1-\cdots\}$ (14.71), which factors by colour (14.72), (14.73). For red (p. 446):
$$Z_1(\lambda_1\mu_1)=\prod_{r=1}^\infty\frac1{1-e^{-r\lambda_1-\mu_1}}\tag{14.74}$$
- Then (p. 447)
$$\langle n_1\rangle=\sum_r\frac r{e^{r\lambda_1+\mu_1}-1}\ (14.75),\qquad\langle m_1\rangle=\sum_r\frac1{e^{r\lambda_1+\mu_1}-1}\ (14.76),\qquad\langle u_r\rangle=\frac1{e^{r\lambda_1+\mu_1}-1}\ (14.77)$$
Jaynes says this is the ideal Bose–Einstein gas in the Gibbs grand canonical ensemble. $r$ is the $r$th energy level, $u_r$ its occupation, and $\lambda_1,\mu_1$ play the roles of temperature and chemical potential (p. 447).
- Since $\langle u_r\rangle\ll1$, $\mu_1$ is large and $\lambda_1$ small, so the series converge slowly. Expanding $1/(e^x-1)=\sum_n e^{-nx}$ gives rapidly converging sums (14.78), (14.79) in $n$. The first term is an excellent approximation, giving (p. 447)
$$\langle n_1\rangle=\frac{e^{-\mu_1}}{\lambda_1^2},\quad\langle m_1\rangle=\frac{e^{-\mu_1}}{\lambda_1}\tag{14.80, 14.81}$$
$$\lambda_1=\frac{\langle m_1\rangle}{\langle n_1\rangle}=\frac1{75}=0.0133,\quad e^{\mu_1}=112.5,\quad\mu_1=4.722\tag{14.82–14.84}$$
Tribus and Fitts' computer sums give $\lambda_1=0.0131$, $\mu_1=4.727$ (pp. 447–448).
- Each $u_r$ is geometric (14.85) with the mean in (14.77). (added step) The variance is $\langle u_r\rangle(1+\langle u_r\rangle)=e^{x}/(e^{x}-1)^2$, $x=r\lambda_1+\mu_1$; the page prints (14.86) with the denominator unsquared. The variance of the total demand $n_1=\sum ru_r$ (14.87) is
$$\mathrm{var}(n_1)=\sum_r r^2\mathrm{var}(u_r)=\sum_r\frac{r^2e^{r\lambda_1+\mu_1}}{(e^{r\lambda_1+\mu_1}-1)^2}\tag{14.88}$$
which is converted to a rapidly convergent sum (14.89) and approximated by
$$\mathrm{var}(n_1)=\frac{2e^{-\mu_1}}{\lambda_1^3}=\frac2{\lambda_1}\langle n_1\rangle\tag{14.90}$$
(p. 448).
- Because $n_1$ is a sum of many small independent terms, its distribution is nearly Gaussian (p. 448):
$$p(n_1)\approx A\exp\Big\{-\frac{\lambda_1(n_1-\langle n_1\rangle)^2}{4\langle n_1\rangle}\Big\}\tag{14.91}$$
(added step: the exponent matches variance $2\langle n_1\rangle/\lambda_1$). This holds for values of $n_1$ that can arise in many ways (e.g. $n_1=150$), but not for small $n_1$ (e.g. $n_1=2$ arises only as $u_1=2$ or $u_2=1$) (p. 448).
- Expected loss from red orders if red is not made (p. 449):
$$\sum_{n_1}p(n_1)R(n_1-S_1)\simeq(\langle n_1\rangle-S_1)\Phi\big[\alpha_1\sqrt2(\langle n_1\rangle-S_1)\big]+\frac1{2\alpha_1\sqrt\pi}\exp\{-\alpha_1^2(\langle n_1\rangle-S_1)^2\}\tag{14.92}$$
with $\alpha_1^2=\lambda_1/4\langle n_1\rangle$. If red is made, replace $S_1$ by $S_1+200$. Same for yellow and green (p. 449).
- With $S=(100,150,50)$, $\langle n\rangle=(50,100,10)$, $\alpha=(0.0082,0.0160,0.035)$ (14.93), the expected losses in unfilled orders are
$$\langle L\rangle_1=(0)+2.86+0.18=3.04,\quad\langle L\rangle_2=14.9+(0)+0.18=15.1,\quad\langle L\rangle_3=14.9+2.86+(0)=17.8\tag{14.94}$$
$(0)$ means a term orders of magnitude smaller than the others. Red ($D_1$) is strongly preferred: the information about average order size makes yellow much safer than it seemed in Stage 2 (p. 449).

*Intuition note.* Many small orders (yellow, 10 per order) make total demand more predictable than a few big ones (red, 75 per order). The same mean demand carries a different risk once order size is known, and maximum entropy turns this into numbers.

#### 14.7.3 Solution for Stage 4
- The 40-widget green order is handled by reducing the green stock $S_3$ from 50 to 10, with all other equations unchanged. Now $\langle n_3\rangle-S_3=0$, so (14.92) reduces to $1/(2\alpha_3\sqrt\pi)=8.08$ (14.95). Hence (p. 450)
$$\langle L\rangle_1=(0)+2.86+8.08=10.9,\quad\langle L\rangle_2=14.9+(0)+8.08=23.0,\quad\langle L\rangle_3=17.8\tag{14.96}$$
- Jaynes concludes that Mr A should still make red. Common sense fails because $\langle L\rangle_1$ and $\langle L\rangle_3$ now differ little (p. 450).

### 14.8 Comments
Jaynes says he has tried to show that probability theory in Laplace's sense with maximum-entropy priors gives a reasonable method for decision problems, with results in good correspondence with common sense. Mathematically it is the Gibbs formalism of statistical mechanics, whose wider applicability is the new recognition. Interpretation matters: it cannot change numerical results in an established application, but it can change one's judgement of a formalism's range of validity. Jaynes holds that the "probability = frequency" interpretation has needlessly restricted the problems to which probability theory is applied (p. 450).

## Toy example (ours, not from the text)
One observation $V$; noise Gaussian with $\sigma=1$; signal amplitude $S_1=2$ or none, so $s=2$. Priors $p=q=\tfrac12$. Losses $L_a=1$, $L_r=3$.

- Threshold on the likelihood ratio: $qL_a/(pL_r)=1/3$.
- Likelihood ratio (14.36): $\exp\{(2V\cdot2-4)/2\}=\exp\{2V-2\}$.
- Solve $\exp\{2V-2\}=1/3$: $2V-2=\ln(1/3)=-1.0986$, so $V_b=0.451$. Formula (14.38) agrees: $(1/4)[2(-1.0986)+4]=0.451$.
- Decisions: $V=0.3$ gives ratio $e^{-1.4}=0.247<1/3$, so $D_0$ (no signal). $V=1.0$ gives ratio $e^0=1>1/3$, so $D_1$.
- Error rates (standard normal table values, rounded): $p(R)=0.5\,\Phi(0.451-2)=0.5(0.0607)=0.0303$ and $p(A)=0.5[1-\Phi(0.451)]=0.5(0.326)=0.163$.
- Expected loss $=3(0.0303)+1(0.163)=0.254$.
- Compare the midpoint threshold $V_0=1$: $p(R)=0.5\Phi(-1)=0.5(0.1587)=0.0794$ and $p(A)=0.5(1-0.8413)=0.0794$. Loss $=3(0.0794)+0.0794=0.317>0.254$.

Shifting the threshold to account for the costly false rest lowers expected loss. The test statistic stayed the same; only the threshold moved.

## Concepts
- [[likelihood-ratio-test]] (new) — compare $p(V|S_1)/p(V|S_0)$ with a threshold set by prior odds and losses; the quantity the optimum receiver computes; it gives all the information needed for Bayes decisions (p. 433)
- [[decision-rule]] (new) — a map $p(D|V)$ from observed data to decisions; 0/1-valued or randomized; uses $V$ alone (pp. 427–428)
- [[loss-function]] (new) — $L(D,S)$, the judged seriousness of deciding $D$ when $S$ is present; a loss matrix when discrete (p. 431)
- [[bayes-decision-criterion]] (new) — choose the rule minimising expected loss $\langle L\rangle$ under a prior (pp. 431–432)
- [[minimax-criterion]] (new) — minimise the worst conditional loss; equals the Bayes rule for the worst prior in the example (pp. 431, 435–436)
- [[neyman-pearson-criterion]] (new) — fix the false-alarm probability $\epsilon$, minimise the false-rest probability; a Bayes rule for a particular prior/loss ratio (pp. 432, 436–437)
- [[sufficient-statistic]] — here: $D$ with $p(Y|V)=p(Y|D)$, equivalently $p(V|D)=p(V|YD)$; equal to zero loss of expected entropy information (pp. 429–430)
- [[entropy H(X)]] — used as expected entropy $\overline H_D(Y)$; extra conditioning never raises it on average (pp. 429–430)
- [[Bayes' theorem]] — posterior odds = prior odds × likelihood ratio, (14.53) (p. 438)
- [[maximum entropy principle]] — used to assign priors from mean-demand constraints (pp. 443, 446)
- [[exponential family / Gibbs distribution]] — the geometric/exponential priors (14.59) and the Bose–Einstein form (14.77) (pp. 443–447)
- [[matched-filter]] (new) — receiver design maximising (peak signal)²/mean-square noise; coincides with the Bayes rule for linear Gaussian systems (pp. 439–440)
- [[false-alarm-false-rest]] (new) — the two error types in binary detection: deciding signal when absent, and no signal when present (p. 431)

## Canonical instances
- [[single-sample-gaussian-detection]] — one-voltage Gaussian detection; threshold (14.38), error rates (14.40–14.41) (pp. 433–435)
- [[widget-problem]] — four-stage factory decision; maximum-entropy priors, no new data (pp. 441–450)
- [[bose-einstein-gas-analogy]] — Stage 3 equations match the ideal Bose–Einstein gas (p. 447)
- [[harmonic-oscillator-analogy]] — Stage 2 equations match quantum harmonic oscillators (p. 445)
- [[matched-filter-rediscovery]] — repeated independent discovery of the same filter (p. 439)

## Bridges (candidates)
- [same-math] Likelihood-ratio threshold test (14.34) ↔ bayesian: posterior odds = prior odds × likelihood ratio, thresholded at loss ratio — literally the same rule (14.54).
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics.
- [same-math] Stage 3 occupation numbers (14.77) ↔ statistical mechanics: Bose–Einstein occupation $1/(e^{\epsilon}-1)$ — the text states the equations are identical.
- [structural-analogy] Neyman–Pearson ε-constraint ↔ constrained optimisation with a Lagrange multiplier: the threshold plays the multiplier's role.
- [metaphor] Huygens principle for $p(D|Y)=\sum_V p(D|V)p(V|Y)$ ↔ optics: intermediate points act as secondary sources.

## Questions this raises
- How does the choice of noise distribution (heavier tails than Gaussian) change the $s>6$ reliability numbers in the Gaussian example (p. 437)?
- How would the widget decision change if tomorrow's stock were included (dynamic programming, mentioned but not done) (p. 443)?
- In what precise sense is a rule minimising information loss $-\log p(S|D)$ "close to sufficient", which Jaynes says seems never to have been clarified (p. 431)?
- How good is the Gaussian approximation (14.91) for the yellow and green decisions, where Jaynes says the approximations are "not equally good" (p. 449)?

## Reading notes
- Printed page = pdf − 30. No exercises appear in this unit.
- **Misprints and oddities seen in the page images** (the digest uses the corrected form where stated):
  - (14.27): $K(D,V)$ is defined with $L(D_1,S)$; it should be $L(D,S)$.
  - (14.32), first line: the numerator reads "(V S₁|X)" with $p$ missing.
  - Fig. 14.1 caption says $L_r=1$, $L_a=2$, but the text says $L_a=(3/2)L_r$ and $p=q=1/2$; the plotted figure shows several $p$ values. The axis label reads $v=V/S$ rather than $V/\sigma$.
  - (14.21) as printed mixes $Y$ and $Z$ in one chain, $\overline H_D(Y)\ge\overline H_{DV}(Z)\le\overline H_V(Z)$. The step to (14.22) needs $\overline H_D(Y)\ge\overline H_{DV}(Y)$, which I marked as an added step.
  - (14.49) prints $p(A|S_0)=\tfrac12[1-\Phi(v_0)]$, inconsistent with (14.41) and (14.51), which have no factor ½.
  - (14.42) prints $\Phi(x)=\frac12[1+\operatorname{erf}(x)]$. I did not check this against the erf convention of (7.2), which is outside this unit.
  - After (14.44): $\tfrac{10}{11}[1-\Phi(3)]\approx1.2\times10^{-3}$ by my arithmetic, but the text prints $1.48\times10^{-3}$ for $s>6$. I did not trace the source of the difference.
  - (14.59): "$n_i=1,2,3\ldots$" should start at 0, consistent with (14.56).
  - (14.67): $6.902+3.073+0.085=10.06$, but 10.6 is printed.
  - (14.74): the sum limits are printed as starting at $u_1=1$ (should be 0), and $\mu$ lacks its subscript.
  - (14.78) and (14.79): the right sides carry a stray $r$ in (14.79). Summing the geometric series over $r\ge1$ also leaves a factor $e^{-n\lambda}$ in the numerator. This is negligible for small $\lambda$ and does not affect (14.80)–(14.81).
  - (14.83): I read it as $e^{\mu_1}=\langle n_1\rangle/\langle m_1\rangle^2=112.5$. The exponent of $\langle m_1\rangle$ is unclear in the text layer, and this reading is consistent with (14.80), (14.81) and 112.5.
  - (14.85): the exponent is printed as $(-r\lambda_1+\mu_1)u_r$; the sign of $\mu_1$ should be negative.
  - (14.86): the denominator should be squared, consistent with (14.88).
- The block quote on p. 443 is attributed to Tribus and Fitts (1968).
