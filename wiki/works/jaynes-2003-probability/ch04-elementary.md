---
id: jaynes-2003-probability/ch04-elementary
work: jaynes-2003-probability
unit: "4 Elementary hypothesis testing"
pages: 86-118
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Elementary hypothesis testing

## L0 — One line
Hypothesis testing needs no new principle beyond the product rule: compute the probability of the hypothesis given all the evidence, and (for two hypotheses) work in log-odds ("evidence" in decibels) so that independent data add up.

## L1 — The gist (≤ 120 words)
The chapter asks how a reasoning robot should weigh hypotheses against data using only the product rule. Answer: compute the posterior probability from prior and likelihood. For two hypotheses, work with log-odds ("evidence" in decibels), where independent data add up. With three or more hypotheses this additivity fails, and each hypothesis's evidence behaves approximately like a test against its currently strongest rival. An added low-prior "surprise" hypothesis makes the robot skeptical when data are extreme. Letting the hypothesis be a continuous parameter gives a beta posterior and a Gaussian approximation, and nuisance parameters are integrated out. This matters because one principle covers all hypothesis testing.

**Prerequisites:** product and sum rules; conditional probability; logarithms; binomial sampling (Ch. 3); basic calculus (derivatives, integrals, power series). **Terms used early:** prior = probability given only the background information $X$; posterior = probability after the data; likelihood = probability of the data given a hypothesis; log-odds = $\log[p/(1-p)]$; nuisance parameter = an unknown parameter we do not care about; beta and Gaussian posterior = two standard shapes for the distribution of an unknown fraction $f$ (both explained in L3).

## L2 — Key ideas
- The robot must use all its evidence; every probability is conditional on prior information $X$, and "prior" is a logical label, not necessarily a time label (pp. 86–88).
- Bayes' theorem (4.3) is just the product rule. Sampling probabilities and priors need the same principles, and, on a fundamental level, one person's sampling probability is another's prior probability (p. 89).
- For two hypotheses, evidence $e = 10\log_{10}(\text{odds})$ in decibels turns updating with independent data into addition: $+3$ db per bad widget, $-1$ db per good one. The author thinks a 1 db change is about the smallest plausibility step our intuition can perceive (pp. 90–95).
- Independence must be *logical* (about the robot's probabilities), not causal. Confusing the two is the mind projection fallacy (pp. 91–92, 108).
- With $n>2$ hypotheses, independent additivity fails. Each hypothesis's change in evidence is approximately that of a test against its currently most plausible rival, so slopes change (pp. 97–104).
- A "dead" low-prior hypothesis $C$ gives sensible skepticism: the evidence for $A$ peaks at about $m=7$ all-bad widgets and then falls, once $C$ becomes as plausible as $B$; $C$ itself passes 0 db after about 10–11 bad widgets (pp. 99–105).
- Continuous distributions are defined from finite sets of propositions; the continuum is an approximation to a finite problem. A uniform prior gives the beta posterior (4.67), which is approximately Gaussian with $\sigma^2=\hat f(1-\hat f)/N$ when $n\gg1$ and $N-n\gg1$. $\sigma$ describes the robot's knowledge, not $f$ (pp. 107–114).
- Composite hypotheses are handled by integrating out nuisance parameters (4.73). The author claims that orthodox methods lack this and any treatment of multiple hypothesis testing (pp. 115–118).

## L3 — Walkthrough

### Opening and 4.1 Prior probabilities (pp. 86–90)
**Principle (4.1).** To judge whether $A$ is true, calculate $P(A|E_1E_2\cdots)$, conditional on all the evidence at hand. Ignoring evidence, or presuming evidence we lack, violates honesty/objectivity (p. 86).

**Prior information $X$.** The robot always has other information $X$ (at least its past experience), so no probability is "absolute". Irrelevant parts of $X$ cancel out; the author says that is what "irrelevant" means (p. 87). $P(A|X)$ is a *prior probability*. "Prior" is purely logical: any information beyond the immediate data $D$ is prior information, even if it arrives later in time. The split into "data" and "prior information" is an arbitrary choice made for convenience, and all such organisations must give the same final results if they succeed at all (p. 87). $X$ is not a hidden major premise about Nature, and not Kant's "a-priori" (pp. 87–88).

**Assigning priors.** There is no single universal rule. Four fairly general principles are known: group invariance, maximum entropy, marginalization, coding theory (p. 88).

**Sampling versus inference.** Conventional sampling theory assumes the "urn" is known and predicts data. Real inference knows $D$ and asks which hypothesis is likely (p. 88). With $X$ = prior information, $H$ = hypothesis, $D$ = data:

$$P(DH|X)=P(D|HX)P(H|X)=P(H|DX)P(D|X)\tag{4.2}$$

$$P(H|DX)=P(H|X)\frac{P(D|HX)}{P(D|X)}\tag{4.3}$$

(4.2)–(4.3) are the same mathematics as (3.50)–(3.51). The apparent difference in logical status arose because sampling problems state $H$ precisely while priors were left unspecified. The author concludes there is no logical difference: the same principles assign both (p. 89).

$P(H|DX)$ is the *posterior*, again meaning "later in the chain of inference". $P(D|HX)$ is the *sampling distribution* as a function of $D$ for fixed $H$, and the *likelihood* $L(H)$ as a function of $H$ for fixed $D$. A likelihood is not a probability for $H$. Constant factors may be struck out: $L(H_i)=y(D)P(D|H_iX)$ for any positive $y$ independent of the $H_i$ (p. 89). If $P(H|DX)$ is very close to 1 (0), we may conclude $H$ is very likely true (false). If it is not far from $1/2$, the evidence is not sufficient for any very confident conclusion and more is needed (p. 90).

*Intuition note.* Bayes' theorem is not a separate axiom. It is the product rule read in the direction we need. "Prior" and "posterior" only say which pieces of information we have already used.

### 4.2 Testing binary hypotheses with binary data (pp. 90–96)
Writing (4.3) for $\overline H$ and dividing:

$$\frac{P(H|DX)}{P(\overline H|DX)}=\frac{P(H|X)}{P(\overline H|X)}\frac{P(D|HX)}{P(D|\overline HX)}\tag{4.5}$$

$P(D|X)$ drops out. The odds are

$$O(H|DX)\equiv\frac{P(H|DX)}{P(\overline H|DX)}\tag{4.6}$$

$$O(H|DX)=O(H|X)\frac{P(D|HX)}{P(D|\overline HX)}\tag{4.7}$$

Posterior odds = prior odds × likelihood ratio (p. 90).

**Evidence.** The author chooses base-10 logs because they are intuitively clear (pp. 90–91):

$$e(H|DX)\equiv10\log_{10}O(H|DX)\tag{4.8}$$

measured in decibels (db):

$$e(H|DX)=e(H|X)+10\log_{10}\!\left[\frac{P(D|HX)}{P(D|\overline HX)}\right]\tag{4.9}$$

For $D=D_1D_2D_3\cdots$ (4.10), the product rule gives

$$e(H|DX)=e(H|X)+10\log_{10}\!\left[\frac{P(D_1|HX)}{P(D_1|\overline HX)}\right]+10\log_{10}\!\left[\frac{P(D_2|D_1HX)}{P(D_2|D_1\overline HX)}\right]+\cdots\tag{4.11}$$

If $P(D_2|D_1HX)=P(D_2|HX)$ (4.12), the robot's probabilities for $D_1,D_2$ are independent. If this holds given both $(HX)$ and $(\overline HX)$:

$$e(H|DX)=e(H|X)+10\sum_i\log_{10}\frac{P(D_i|HX)}{P(D_i|\overline HX)}\tag{4.13}$$

**Logical versus causal independence.** Independence belongs to the robot's probabilities, not to events. Two events may be causally linked while the probabilities of a scientist who has not yet discovered this are independent. Causally unrelated events (apple and peach crops) may be logically connected for us. Attributing independence to events is the *mind projection fallacy* (confusing reality with a state of knowledge about it), and the author says that treating causal independence as logical independence, or the reverse, has led some to nonsensical conclusions in fields ranging from psychology to quantum theory (p. 92).

**Table 4.1.** $e=0$: odds 1:1, $p=1/2$; 3 db: 2:1, $2/3$; 6: 4:1, $4/5$; 10: 10:1, $10/11$; 20: 100:1, $100/101$; 30: 1000:1, 0.999; 40: $10^4$:1, 0.9999; and $-e \leftrightarrow 1/O \leftrightarrow 1-p$. Here 3 db is nearly a factor 2 and 10 db exactly 10 (p. 92). The author argues evidence is easier to grasp than probabilities near 0 or 1, as in the Weber–Fechner law; he does not claim it is a precise rule (pp. 92–93).

**Widget example (after Good 1950).** $X$: 11 machines; ten make 1/6 defective, the 11th makes 1/3 defective; each machine's output is in an unlabeled box; we pick a box (p. 93). $A$ = bad batch (1/3 defective), $B$ = good batch (1/6). Given $X$, $\overline A=B$ and $\overline B=A$ (4.14). By indifference $P(A|X)=1/11$:

$$e(A|X)=10\log_{10}\frac{1/11}{10/11}=-10\text{ db},\qquad e(B|X)=+10\text{ db}\tag{4.15}$$

Only these numbers matter to the robot. One machine with past experience giving the same prior would pose the same problem (p. 94).

Sampling probabilities (large batch $N$, so the binomial limit applies; the exact hypergeometric correction (4.20) is $\frac{N/3-1}{N-1}=\frac13-\frac{2}{3(N-1)}$) (p. 95):

$$P(\text{bad}|AX)=\tfrac13,\ P(\text{good}|AX)=\tfrac23;\qquad P(\text{bad}|BX)=\tfrac16,\ P(\text{good}|BX)=\tfrac56\tag{4.17, 4.18}$$

A bad widget adds $10\log_{10}\frac{1/3}{1/6}=10\log_{10}2=3$ db (4.19). A good one adds $10\log_{10}\frac{2/3}{5/6}=-0.97\approx-1$ db (4.21). After $n_b$ bad and $n_g$ good widgets:

$$e(A|DX)=e(A|X)+3n_b-n_g\tag{4.22}$$

Example (4.23): 12 widgets with 5 bad give $-10+3\times5-7=-2$ db, so $P(A|DX)$ rises from $1/11=0.09$ to about 0.4 (p. 95).

**Threshold.** Requiring at least 20 db: $3n_b-n_g=n(4f_b-1)\ge20$ (4.24), with $f_b=n_b/n$. If $f_b$ stays above $1/4$, any positive amount of evidence for $A$ accumulates. Since $+3,-1$ are approximate, the exact threshold is

$$f_t=\frac{\log(5/4)}{\log 2+\log(5/4)}=0.2435292\tag{4.25}$$

Near the threshold many tests are needed (p. 96).

**Decisions.** Probability theory alone does not fix the accept/reject levels. They come from value judgments about costs of errors and of more tests (decision theory, Chs. 13–14). Example rule: reject if evidence for $A$ exceeds $+0$ db; accept if it falls to $-13$ db (the author says this gives at least a 95% probability that the batch is good); otherwise keep testing. Each bad widget adds 3 db, each good one subtracts 1 db (p. 96). This is *sequential inference*: stop with acceptance, stop with rejection, or test again. It must not be confused with "sequential analysis with nonoptional stopping", which the author calls a serious misapplication (Chs. 6, 17) (p. 96).

*Intuition note.* In log-odds, with independent data, each observation just moves a running score up or down by a fixed amount (as in the widget example). Decibels make the gap between $+30$ and $+40$ db mean something to us, where the author says 0.999 versus 0.9999 does not.

### 4.3 Nonextensibility beyond the binary case (pp. 97–98)
*Independent additivity* means the increment from $D_i$ depends only on $D_i$ and $H$, not on other data. (4.11) always gives additivity, but independent additivity only if the probabilities are independent (p. 97). Take $n$ mutually exclusive, exhaustive hypotheses:

$$P(H_iH_j|X)=P(H_i|X)\delta_{ij},\qquad\sum_{i=1}^nP(H_i|X)=1\tag{4.26}$$

With data sets $D_1,\dots,D_m$:

$$O(H_i|D_1\dots D_mX)=O(H_i|X)\frac{P(D_1,\dots,D_m|H_iX)}{P(D_1,\dots,D_m|\overline H_iX)}\tag{4.27}$$

Typically the numerator factors (4.28); if the denominator also factors (4.29), the evidence is independently additive as in (4.13).

> **Exercise 4.1** (statement): show that if (4.28) and (4.29) hold with $n>2$, then at most one of the factors (4.30) $\frac{P(D_j|H_iX)}{P(D_j|\overline H_iX)}$ differs from unity, so at most one $D_j$ can update $H_i$.

When $n=2$, (4.29) follows from (4.28). For $n>2$, (4.29) is so strong the problem becomes trivial. Those who confuse logical with causal independence would assume (4.29) whenever no $D_i$ physically influences another, which the author calls folly (p. 98). By Cox's theorems the nonextensibility can be evaded only by committing demonstrable inconsistencies (p. 98).

Any two hypotheses can still be compared as a binary problem. With $A_1$ as null, if $A_5$ and $A_7$ are favored over $A_1$ by 22.3 and 31.9 db, then $A_7$ over $A_5$ is $9.6$ db. But this does not give a hypothesis's absolute status against the whole class (p. 98).

### 4.4 Multiple hypothesis testing (pp. 98–106)
**The puzzle.** If all 50 tested widgets are bad, (4.22) gives $-10+150=+140$ db, about one part in $10^{14}$ from certainty. Common sense rejects this. The author says the robot is "immature", like a child believing anything it is told. It was told dogmatically that only two possibilities exist (pp. 98–99). A robot that doubted its instructions on its own would be dangerous. Instead, the user should hint at skepticism by adding a hypothesis (p. 99).

**Three hypotheses.** Add $C$ = box with 99/100 defective, with prior $10^{-6}$ ($-60$ db). The robot's problem is defined by stating the priors given $X$ (pp. 99–100):

$$P(A|X)=\tfrac1{11}(1-10^{-6}),\quad P(B|X)=\tfrac{10}{11}(1-10^{-6}),\quad P(C|X)=10^{-6}\tag{4.31}$$

Initial evidence is practically $-10$ (A), $+10$ (B), $-60$ (C) db (4.32). Let $D$ be the statement that $m$ widgets were tested and every one was bad. Then

$$e(C|DX)=e(C|X)+10\log_{10}\frac{P(D|CX)}{P(D|\overline CX)}\tag{4.33}$$

$$P(D|CX)=(99/100)^m\tag{4.34}$$

Via the product rule: $P(D|\overline CX)=P(D|X)\,P(\overline C|DX)/P(\overline C|X)$ (4.35). Since $\overline C=A+B$ with $A,B$ exclusive: $P(\overline C|DX)=P(A|DX)+P(B|DX)$ (4.36), $P(\overline C|X)=P(A|X)+P(B|X)$ (4.37) (p. 101). Using $P(AD|X)=P(D|X)P(A|DX)=P(A|X)P(D|AX)$ and the same for $B$ (4.38):

$$P(D|\overline CX)=\frac{P(D|AX)P(A|X)+P(D|BX)P(B|X)}{P(A|X)+P(B|X)}\tag{4.39}$$

**4.4.1 Another derivation (pp. 101–102).** Resolve $D$ into exclusive, exhaustive pieces, $D=DP+DQ+DR+\cdots$ (4.40). The introduced propositions must be relevant. Here, $\overline C$ implies $A+B$:

$$P(D|\overline CX)=P(DA+DB|\overline CX)=P(DA|\overline CX)+P(DB|\overline CX)\tag{4.41}$$

$$=P(D|A\overline CX)P(A|\overline CX)+P(D|B\overline CX)P(B|\overline CX)\tag{4.42}$$

Here $P(D|A\overline CX)=P(D|AX)$ (and likewise for $B$), and $P(\overline C|AX)=1$, so $P(A|\overline CX)=P(A|X)/P(\overline C|X)$ (4.43). Substituting with (4.37) reproduces (4.39). The author calls this "a rather severe test" of the consistency of the rules (p. 102).

**Numbers.**

$$P(D|\overline CX)=\left(\tfrac13\right)^m\tfrac1{11}+\left(\tfrac16\right)^m\tfrac{10}{11}\tag{4.44}$$

$$e(C|DX)=-60+10\log_{10}\!\left[\frac{(99/100)^m}{\frac1{11}(1/3)^m+\frac{10}{11}(1/6)^m}\right]\tag{4.45}$$

$$e(C|DX)\simeq-49.6+4.73m\ (m>5);\qquad e(C|DX)\simeq-60+7.73m\ (m<3)\tag{4.46, 4.47}$$

$C$ starts at slope 7.73 db per bad widget, then 4.73 for $m>5$. It reaches 0 db at $m\simeq49.6/4.73=10.5$. Ten bad widgets raise it by 58 db and 11 take it over the threshold (p. 102). For $A$ and $B$ after $m$ bad widgets:

$$e(A|DX)=-10+10\log_{10}\!\left[\frac{(1/3)^m}{(1/6)^m+\frac{11}{10}\times10^{-6}(99/100)^m}\right]\simeq\begin{cases}-10+3m & m<7\\ +49.6-4.73m & m>8\end{cases}\tag{4.48}$$

$$e(B|DX)=+10+10\log_{10}\!\left[\frac{(1/6)^m}{(1/3)^m+11\times10^{-6}(99/100)^m}\right]\simeq\begin{cases}10-3m & m<10\\ 59.6-7.33m & m>11\end{cases}\tag{4.49}$$
(as printed; the slope $7.33$ looks like a misprint for $7.73$, see Reading notes).

**Fig. 4.1 (p. 103).** The $A$ and $B$ lines are initially as in the two-hypothesis problem. Once $C$ crosses $B$, the $A$ curve turns: at $m=7$ it peaks at 10 db and then falls, so the robot "has indeed learned how to become skeptical". The $B$ curve is unchanged until $A$ and $C$ have equal plausibility, then its slope changes and it falls faster (p. 103).

**Explanation (p. 104).** The change in $A$'s plausibility comes from testing $A$ against two alternatives. While $B$ is far more plausible than $C$, $A$ is, for practical purposes, tested against $B$ only. Once $C$ matches $B$, $A$ is effectively tested against $C$. For any discrete set, a change in plausibility of one hypothesis is approximately a test against the single most plausible remaining alternative at that time. That is the information lost if (4.13) is kept for $n>2$. When hypotheses are separated by about 10 db or more, multiple testing reduces approximately to pairwise testing (p. 104).

**Fig. 4.2, plausibility flow diagrams (p. 104).** For binary comparisons: GOOD widget: $A\to1.0\to B\leftarrow19.22\leftarrow C\to18.24\to A$. BAD widget: $A\leftarrow3.0\leftarrow B\to7.73\to C\leftarrow4.73\leftarrow A$. Examples: a good widget raises $B$ by 1 db against $A$ and by 19.22 db against $C$; a bad widget raises $A$ by 3 db against $B$ but lowers it by 4.73 db against $C$. A single good widget lowers $C$ by an amount two bad ones cannot recover, hence a "threshold of skepticism". The robot will never become skeptical about $A$ and $B$ while the observed bad fraction stays below $2/3$. Precisely, $f_t$ is the limiting fraction $f=m_b/m$ above which $e(C|DX)\to+\infty$ and below which it $\to-\infty$. It exceeds $2/3$: $f_t=0.793951$ (Exercise 4.2) (pp. 104–105).

> **Exercises 4.2, 4.3** (statements, p. 105): 4.2 asks for $f_t(x,y)$ for general prior $x$ and bad fraction $y$ of $C$, and a comparison with common sense. 4.3 asks how to make the robot skeptical of unexpectedly low or high numbers of bad widgets by adding a hypothesis $F$ with $P(\text{bad}|FX)\simeq1/4$.

**Role of $C$ (p. 105).** $C$ is meant only to be held in abeyance until needed (the author's image: a fire extinguisher): it is "dead" in normal testing, but very unexpected data can resurrect it (the subject returns in Ch. 5).

**Stopping.** In Fig. 4.1, a rule to accept $A$ once its evidence reaches $+6$ db would overshoot that value at the sixth trial and stop there, and never see the later fall. Stopping at any finite $n$ cannot guarantee the right decision. But the built-in safety is that if the critical level is large (e.g. $e(A|DX)\ge20$ db gives $P(A|DX)>0.99$), a wrong decision is very improbable (pp. 105–106). A hypothesis separated by more than 20 db from its best rival, among 1000 rivals, is still the best choice. Yet the whole class of alternatives may be about as probable as $A$, and the small value of $e(A|DX)$ warns of this (p. 106). The text says the sampling-theory literature gives little help here.

> **Exercises 4.4–4.5** (statements, p. 106): 4.4 asks how many tests give an additional 20 db for $B$ if $B$ is true, and to show that the sampling probability of ever reaching 20 db of evidence for $A$ is negligibly small, so that for all practical purposes a doctrinaire zealot cannot sample to a foregone false conclusion. 4.5 asks about Wald's conjecture that sequential probability-ratio tests minimize the average sample number.

### 4.5 Continuous probability distribution functions (pp. 107–109)
For a continuous real parameter $f$, the propositions $F'\equiv(f\le q)$, $F''\equiv(f>q)$ (4.50) are discrete, exclusive and exhaustive. Define $G(q)\equiv P(F'|Y)$ (4.51), monotonic increasing. With $A\equiv(f\le a)$, $B\equiv(f\le b)$, $W\equiv(a<f\le b)$ (4.52), Boolean algebra gives $B=A+W$ with $A,W$ exclusive, so $P(B|Y)=P(A|Y)+P(W|Y)$ (4.53) and

$$P(a<f\le b|Y)=G(b)-G(a)\tag{4.54}$$

If $G$ is differentiable, with $g=G'\ge0$ (the pdf):

$$P(a<f\le b|Y)=\int_a^b df\,g(f)\tag{4.55}$$

As long as continuous distributions are defined from finite sets of propositions, as here, Cox's theorems protect against inconsistency. Operating directly on infinite sets without this basis loses the protection and exposes us to "the paradoxes of infinite-set theory" (Ch. 15) (p. 108).

**Warning.** Do not call $g(f)$ the "posterior distribution of $f$". That implies $f$ is varying; it is an unknown constant, and what is distributed is probability. This is the mind projection fallacy. If $f$ varies with time, that is a different problem needing a different calculation (p. 108). Discontinuous $G$ (Appendix B): singular mathematics gets meaning as a limit of well-behaved mathematics. Here the density becomes a delta function $p_0\delta(q-q_0)$ for a discrete hypothesis (p. 108). Pragmatically, $f$ is a multiple of $10^{-8}$ if a machine makes $10^8$ widgets, so the continuum is an approximation to a finite theory (p. 109).

### 4.6 Testing an infinite number of hypotheses (pp. 109–114)
Return to probability form: $P(A|DX)=P(A|X)P(D|AX)/P(D|X)$ (4.56). Let $A$ be the proposition that the fraction of bad widgets is in $(f,f+df)$, with prior $P(A|X)=g(f|X)df$ (4.57), and $D$ = $N$ widgets tested in a given order, $n$ bad. Then

$$P(A|DX)=P(A|X)\frac{P(D|AX)}{P(D|X)}=g(f|DX)\,df\tag{4.58}$$

$$g(f|DX)=g(f|X)\frac{P(D|AX)}{P(D|X)}\tag{4.59}$$

The denominator is fixed by normalization:

$$\int_0^1df\,g(f|DX)=1\tag{4.60}$$

(an approximation to a sum over many discrete values) (p. 110).

**Is $P(D|AX)=P(D|H_fX)$?** $A$ specifies an interval, not a point. With a second parameter $\theta$, the limit $df\to0$ is ambiguous: setting $df=\epsilon h(\theta)$ and letting $\epsilon\to0$, conclusions may depend on $h$. This is the Borel–Kolmogorov paradox, said to be averted by strict use of the Chapter 2 rules (Ch. 15) (p. 110). Here $f$ is the only parameter and the likelihood is continuous. Still, the author checks directly by writing $A=A_1+\cdots+A_n$ (4.61), with $A_1=H_f$ and the $A_i$ the discrete values in $(f,f+df)$. Then

$$P(D|AX)=\frac{\sum_iP(A_i|X)P(D|A_iX)}{\sum_iP(A_i|X)}\tag{4.62}$$

a weighted average, generalizing (4.39). If all $P(D|A_iX)$ are equal it equals $P(D|H_fX)$. Even if not, as $df\to0$, $n\to1$ and $A=A_1$ (p. 110). The author says such care is needed in every new area (p. 111).

**Binomial likelihood and posterior.** Given $f$, trials are logically independent, and the order was recorded:

$$P(D|H_fX)=f^n(1-f)^{N-n}\tag{4.63}$$

$$g(f|DX)=\frac{f^n(1-f)^{N-n}g(f|X)}{\int_0^1df\,f^n(1-f)^{N-n}g(f|X)}\tag{4.64}$$

Everything earlier in the chapter is a special case. The three-hypothesis test corresponds to the prior

$$g(f|X)=\tfrac{10}{11}(1-10^{-6})\delta\!\left(f-\tfrac16\right)+\tfrac1{11}(1-10^{-6})\delta\!\left(f-\tfrac13\right)+10^{-6}\delta\!\left(f-\tfrac{99}{100}\right)\tag{4.65}$$

with the delta functions for $B,A,C$ and coefficients equal to (4.31). The posterior coefficients are the posterior probabilities from (4.45), (4.48), (4.49) (p. 111). Delta functions are a matter of notation (Appendix B) (pp. 111–112).

**Uniform prior.** For a robot with no knowledge beyond the possibility of good and bad widgets, it may seem, as it did to Laplace, that the robot has no basis for giving any interval $df$ higher probability than another of equal size. So

$$g(f|X)=1,\quad0\le f\le1\tag{4.66}$$

The author says better justification comes later. The integral is the complete beta function, and

$$g(f|DX)=\frac{(N+1)!}{n!\,(N-n)!}f^n(1-f)^{N-n}\tag{4.67}$$

(p. 112). **4.6.1 Historical digression:** it appears the result was first found by Rev. Thomas Bayes (1763). But the general result (4.3) is just the product rule, known earlier to Bernoulli and de Moivre. It was Laplace (1774) who saw it in generality. Probability as logic is wider than Bayes' theorem (p. 112).

**Peak and width.** (4.67) peaks at the observed fraction (4.68):

$$\hat f=n/N$$

With $L(f)\equiv\log g(f|DX)=n\log f+(N-n)\log(1-f)+\text{const}$ (4.69), expansion about $\hat f$ gives

$$L(f)=L(\hat f)-\frac{(f-\hat f)^2}{2\sigma^2}+\cdots,\qquad\sigma^2\equiv\frac{\hat f(1-\hat f)}{N}\tag{4.70, 4.71}$$

$$g(f|DX)\simeq K\exp\!\left\{-\frac{(f-\hat f)^2}{2\sigma^2}\right\}\tag{4.72}$$

(4.71)–(4.72) are the de Moivre–Laplace theorem. The difference of the two sides tends to zero on $0<f<1$ (the ratio need not tend to 1), provided $n\gg1$ and $N-n\gg1$ (p. 113). The robot assigns 50% probability to $\hat f\pm0.68\sigma$, 90% to $\hat f\pm1.65\sigma$, 99% to $\hat f\pm2.57\sigma$. The intervals shrink as $1/\sqrt N$ (p. 113).

**Cautions (pp. 113–114).** (1) This applies only if $f$ is known not to change with time. (2) $\sigma$ is not "the variance of $f$" and not a physical property of $f$. It is a property of the pdf representing the robot's knowledge; a better-informed robot will probably be able to use a smaller $\sigma$. If $f$ does vary, its mean-square variation $s^2$ is a real property. The author says later chapters will show: knowing $\sigma$ but with no data and no other prior information about $s$, the best prediction of $s$ is essentially $\sigma$; with data but unknown $\sigma$ and no other information, the best estimate of $\sigma$ is nearly $s$ (p. 114).

Possible extensions (drift in time, graded quality, several properties) need no new principles. Shewhart's (1931) methods are said to be intuitive approximations to what the robot would do, and equal to it in some normal-distribution cases (non-sequential). This is the same problem as detecting a signal in noise (p. 114).

*Intuition note.* With a flat prior, the posterior for the bad fraction is centred on the observed fraction and narrows like $1/\sqrt N$. The "spread" describes what the robot knows, not randomness in the machine.

### 4.7 Simple and compound hypotheses (pp. 115–116)
A *simple* hypothesis fixes a single point in the parameter space $\Omega$. A *composite* hypothesis says only that the parameter lies in a subset $\Omega_1\subset\Omega$; the value of $f$ within it is then a *nuisance parameter*. Example: act (readjust the machine) if $f>0.1$; $\Omega_1=[0.1,1]$ (p. 115). By the sum rule extended to integrals, the nuisance parameter is integrated out:

$$P(\Omega_1|DX)=\frac{\int_{\Omega_1}df\,f^n(1-f)^{N-n}g(f|X)}{\int_\Omega df\,f^n(1-f)^{N-n}g(f|X)}\tag{4.73}$$

With a uniform prior, the incomplete beta function:

$$P(a<f<b|DX)=\frac{(N+1)!}{n!(N-n)!}\int_a^bdf\,f^n(1-f)^{N-n}\tag{4.74}$$

easy to evaluate by computer. In general, for composite hypotheses sum or integrate out nuisance parameters with respect to appropriate priors; this uses all the evidence in data and prior information (pp. 115–116).

### 4.8 Comments (pp. 116–118)
**4.8.1 Etymology.** John Craig's (1699) work was ridiculed. Stigler notes that "probability" then lacked its technical (0–1) meaning, and if Craig's probability for an hypothesis is read as our log-odds measure, his reasoning was quite good and may be regarded as an anticipation of this chapter (p. 116). The quantity $u=\log[p/(1-p)]$ has had several names: Good (1950) "lods"; Turing and Good used it from 1941 in wartime cryptography, Turing coining "deciban"; the author's lectures (1955–64) "evidence", adopted by Tribus (1969). None caught on. "Logit" and "logistic regression" are mathematically similar, but $U=\log[y/(a-y)]$ for data $y_i$ is not a probability measure, so the conceptual relation is not obvious (p. 116). The author's terminology: *evidence* names the quantity; units are chosen separately, here decibels (p. 117).

**4.8.2 What have we accomplished?** The chapter introduced almost every kind of problem in hypothesis testing. The author claims that the orthodox literature contains neither an understanding of multiple hypothesis testing as in Fig. 4.1 nor the solution (4.73) (p. 117). Probability distributions are treated as carriers of information, with Cox's theorems preventing ad hoc inconsistency (Pratt 1961 is cited) (p. 117).

> **Exercise 4.6** (statement, p. 118): Ruelle's three rules (4.75): $p(\overline A)=1-p(A)$; $p(A+B)=p(A)+p(B)$ for exclusive $A,B$; $p(AB)=p(A)p(B)$ for independent $A,B$. How many Chapter 3–4 applications can be solved with these?

The author concludes that orthodox theory, recognizing only sampling probabilities, denies itself the tools to incorporate prior information, eliminate nuisance parameters, or recognize the information in a posterior probability. Later chapters are claimed to show that this treatment of compound hypotheses automatically generates the orthodox significance tests or superior ones (p. 118).

## Toy example (our own)
Two coins-in-a-bag problem. $B$ = coin lands heads with probability $3/4$; $F$ = fair coin.

*Binary case.* Prior 1:1 (0 db). Heads gives $10\log_{10}(0.75/0.5)=1.76$ db. Tails gives $10\log_{10}(0.25/0.5)=-3.01$ db. Data H,H,T: $e(B)=0+1.76+1.76-3.01=0.51$ db. Check by a direct likelihood ratio: $(0.75^2\cdot0.25)/0.5^3=0.140625/0.125=1.125$, and $10\log_{10}1.125=0.51$ db. Odds 1.125, so $P(B)=1.125/2.125=0.53$.

*Three hypotheses.* Add $T$ = two-headed coin. Priors: $P(F)=0.495$, $P(B)=0.495$, $P(T)=0.01$. Data = $m$ heads in a row; likelihoods $0.5^m$, $0.75^m$, $1$.

| $m$ | $F$: $0.495\cdot0.5^m$ | $B$: $0.495\cdot0.75^m$ | $T$ | $P(B\mid D)$ |
|---|---|---|---|---|
| 0 | — | — | — | 0.495 |
| 5 | 0.01547 | 0.11747 | 0.01 | $0.11747/0.14294=0.822$ |
| 10 | 0.00048 | 0.02788 | 0.01 | $0.02788/0.03836=0.727$ |
| 20 | $4.7\times10^{-7}$ | 0.00157 | 0.01 | $0.00157/0.01157=0.136$ |

The posterior for $B$ rises and then falls as the long-shot $T$ takes over, the same shape as curve $A$ in Fig. 4.1.

## Concepts
- [[bayes-theorem]] — (4.3) as the product rule rearranged; "prior" and "posterior" are logical, not temporal (pp. 87–89)
- [[prior-distribution]] — probability conditional on $X$ alone, where $X$ is all information beyond the data $D$; no universal assignment rule (pp. 87–88)
- [[likelihood]] — $P(D|HX)$ as a function of $H$ for fixed $D$; not a probability for $H$; constant factors irrelevant (p. 89)
- [[posterior-distribution]] — $P(H|DX)$, or the pdf $g(f|DX)$ for a continuous parameter (pp. 89, 109)
- [[evidence-decibels]] (new) — $e=10\log_{10}$(odds), in db; posterior = prior + log likelihood ratio (p. 91)
- [[odds-likelihood-ratio-form]] (new) — posterior odds = prior odds × likelihood ratio (4.7); $P(D|X)$ cancels (p. 90)
- [[logical-vs-causal-independence]] (new) — independence is a property of the robot's probabilities, not of events (pp. 91–92)
- [[mind-projection-fallacy]] (new) — treating a state of knowledge as a property of reality, e.g. calling $\sigma$ the "variance of $f$" (pp. 92, 108, 113)
- [[sequential-inference]] (new) — test count not fixed in advance; at each step accept, reject, or continue (p. 96)
- [[nonextensibility-multiple-hypotheses]] (new) — independent additivity (4.13) of evidence fails for $n>2$ (pp. 97–98, 104)
- [[dead-hypothesis-resurrection]] (new) — a tiny-prior hypothesis $C$ that revives under extreme data and induces skepticism (pp. 99–105)
- [[probability-as-extended-logic]] — conclusions come from $P(A|\text{all evidence})$; Cox's theorems forbid inconsistency (pp. 86, 98, 117)
- [[principle-of-indifference-maximum-entropy]] — indifference gives $P(A|X)=1/11$; a no-basis-for-preference argument (Laplace) motivates the uniform prior (4.66), with better justification promised later; maximum entropy listed as a principle for priors (pp. 88, 94, 112)
- [[nuisance-parameter-marginalization]] (new) — integrate out parameters not of interest, as in (4.73) (p. 115)
- [[composite-hypothesis]] (new) — hypothesis that the parameter lies in a subset of $\Omega$, as opposed to a simple point hypothesis (p. 115)
- [[de-moivre-laplace-gaussian-approximation]] (new) — posterior (4.67) ≈ Gaussian with $\hat f=n/N$, $\sigma^2=\hat f(1-\hat f)/N$ (p. 113)
- [[weber-fechner-law]] (new) — sensations roughly logarithmic in stimulus; used to motivate decibel evidence (pp. 92–93)

## Canonical instances
- [[widget-quality-control]] — 11 machines, boxes with 1/3 or 1/6 defective; $+3$/$-1$ db updates (pp. 93–96)
- [[three-hypothesis-widget-test]] — added $C$ (99% defective, prior $10^{-6}$); Fig. 4.1 and plausibility flow diagrams, Fig. 4.2 (pp. 99–105)
- [[uniform-prior-bad-fraction]] — Laplace/Bayes beta posterior (4.67) for unknown bad fraction (p. 112)
- [[borel-kolmogorov-paradox]] — ambiguity of $df\to0$ limits with an extra parameter (p. 110)
- [[machine-readjust-composite-test]] — $f>0.1$ as composite hypothesis (4.73) (p. 115)

## Bridges (candidates)
- [same-math] Evidence in db (log-likelihood ratio) ↔ information-theory: difference of surprisals $-\log P(D|\overline H)+\log P(D|H)$ (change of base and factor 10) — the same quantity.
- [structural-analogy] Additive log-odds updating ↔ logistic regression: log-odds linear in data; the author notes only a "mathematical similarity" (p. 116).
- [structural-analogy] $\sigma^{-2}=-L''(\hat f)$ in (4.70)–(4.71) ↔ Fisher information: curvature of log-likelihood sets the posterior width ($1/\sqrt N$ shrinkage), here with a flat prior.
- [structural-analogy] Sequential accept/reject thresholds on log-odds ↔ sequential probability ratio test (Wald, cited p. 106) — a random walk with $+3$/$-1$ steps.
- [metaphor] Dead hypothesis as "fire extinguisher" (p. 105) ↔ heavy-tailed or contamination components in robust models.

## Questions this raises
- How should the hint about skepticism (the prior $10^{-6}$ and the 99% bad fraction for $C$) be chosen in a real problem, and how sensitive is $f_t$ to them (Ex. 4.2)?
- What are the principles (group invariance, maximum entropy, marginalization, coding theory) that assign priors beyond indifference?
- When $f$ is allowed to drift, how does the robot's $\sigma$ relate to the real variation $s$ (the relations promised on p. 114)?
- How does stopping once the evidence reaches a chosen level (pp. 96, 105) differ from the "sequential analysis with nonoptional stopping" that the author calls a misapplication (p. 96; Chs. 6, 17)?

## Exercises worth doing
- Ex. 4.1 (p. 97) — why independent additivity cannot hold for $n>2$; a proof from (4.28)–(4.29) — difficulty: medium
- Ex. 4.2 (p. 105) — exact threshold of skepticism $f_t(x,y)$ and its fit to common sense — difficulty: medium
- Ex. 4.3 (p. 105) — make the robot skeptical of low as well as high bad fractions via hypothesis $F$ — difficulty: hard
- Ex. 4.4 (p. 106) — random-walk estimate: sampling to a foregone false conclusion is practically impossible — difficulty: hard
- Ex. 4.5 (p. 106) — Wald's conjecture on average sample number; define "reliability" to make it provable — difficulty: hard
- Ex. 4.6 (p. 118) — which applications of Chs. 3–4 can Ruelle's three rules solve — difficulty: easy

## Reading notes
- Printed page numbers are given in the page labels and visible in the images (printed = pdf − 30). Citations use printed numbers.
- The text layer loses overbars ($\overline A$, $\overline H$, $\overline C$) in many equations. Overbars are visible in the page images (e.g. pp. 90–91, 94, 97, 100–102), and equations were transcribed from the images.
- p. 98 writes "$e(A|E)$", where $E$ presumably stands for all the evidence, as in (4.1); the digest reads it as $e(A|DX)$.
- p. 111 says the multiple-hypothesis test "starts with (4.43)". The setup actually begins at (4.31) (p. 100); I take this as a loose reference.
- Ex. 4.3 (p. 105) refers to the threshold value as (4.24); the exact threshold fraction is given in (4.25).
- Footnote 3 begins at the foot of p. 116 and ends at the foot of p. 117. It says Alexander the Great only partly made the countries he conquered Greek, so they were called Hellenistic rather than Hellenic, and that likewise "logistic" implies something with some properties of logic, but not all (p. 117). It is not otherwise digested.
- Equation values are copied as printed. Eq. (4.49) prints the slope $7.33$ for $B$ at $m>11$, whereas Fig. 4.2 (p. 104) and (4.47) give $7.73$ for the step from $B$ to $C$; $7.33$ looks like a misprint for $7.73$. I did not otherwise recompute (4.46)–(4.49).
