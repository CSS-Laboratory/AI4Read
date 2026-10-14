---
id: mackay-2003-information/ch03-more
work: mackay-2003-information
unit: "3 More about Inference"
pages: 47-64
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# More about Inference

## L0 — One line
Bayes' theorem gives one complete answer to an inference problem: the posterior, built from explicit assumptions and the likelihood of the data actually observed; the same machinery handles prediction and model comparison.

## L1 — The gist (≤ 120 words)
How should we infer a parameter, predict, or compare theories without inventing ad hoc estimators? MacKay argues that the posterior distribution is the unique, complete solution once assumptions are stated. Predictions average over the posterior. Competing models are compared through their evidence, which is usually the normalizing constant of an earlier parameter inference. Worked examples (bent coin, blood traces, game-show doors, a coin spun 140 times heads in 250) show that what the data contribute is carried by the likelihood of the data actually observed (how probable they are under each hypothesis). Evidence for some hypotheses must be evidence against others. A p-value of 7% can coexist with almost no evidence against fairness.

**Prerequisites:** sum and product rules of probability; Bayes' theorem; integrating exponentials and powers; factorials and the Gamma function (Γ(n+1) = n!); likelihood vs. probability. Terms used before they are explained: posterior = belief about the parameter after seeing the data; likelihood = probability of the observed data under a given hypothesis; p-value = chance, if the null hypothesis is true, of a result at least as extreme as the one observed.

## L2 — Key ideas
- Treat the unknown parameter as a hypothesis with a probability distribution describing belief. The posterior (prior × likelihood, normalized) is, in the author's view, the unique and complete solution, and needs no estimators or estimator-comparison criteria (p. 50).
- Inference is conditional on assumptions. Making them explicit makes results reproducible given the same assumptions, shows how sensitive they are, lets alternatives be compared by Bayes' theorem, and lets predictions average over assumptions (pp. 50–51).
- Bent coin with a uniform prior: the posterior is ∝ $p_a^{F_a}(1-p_a)^{F_b}$ and the predictive probability of "a" is Laplace's rule $(F_a+1)/(F_a+F_b+2)$ (p. 52).
- Model comparison is Bayes' theorem applied to models. The evidence for a model is usually the normalizing constant of an earlier inference. A simple model can lose by large margins, whereas the flexible model never loses by a large margin (pp. 53–54).
- Legal evidence: only the likelihood ratio of the data is the data's contribution. Type-O blood at the scene weakly counts against Oliver (ratio 0.83). Evidence for some hypotheses must be evidence against others (pp. 55–57).
- Game-show problems show that the same visible scene supports different inferences under different data-generating processes. Advice: "Always write down the probability of everything" (pp. 60–61).
- Conditional probabilities must not be transposed. P(murder | beater) = 1/1000 says little about P(husband did it | beaten and murdered), which is about 95% under stated assumptions (pp. 61–62).
- A p-value of 7% (or 4.97%) for a coin spun 140 (or 141) heads in 250 gives likelihood ratios from about two to one in favour of the null (uniform prior, 140 heads) to at most about 2.3:1 in favour of the alternative (best prior, 141 heads), far from "very suspicious" (pp. 63–64).

## L3 — Walkthrough

### Preface to the chapter (p. 47)
The chapter can be skipped by readers eager for compression and channels, but data compression and data modelling are connected, so the reader will probably return by Chapter 6 (p. 47). Four warm-up exercises are listed: two dice (3.1, 3.2), the decay-constant problem (3.3) and forensic blood evidence (3.4) (p. 47).

### 3.1 A first inference problem (pp. 48–51)
**The problem (Exercise 3.3, a Tripos question).** Particles decay at distance $x$, which has an exponential distribution with characteristic length $\lambda$. Decays are observed only in the window 1 cm < x < 20 cm. $N$ decays are seen at $\{x_1,\dots,x_N\}$. What is $\lambda$? (p. 48)

**Orthodox attempts.** The sample mean $\bar x=\sum_n x_n/N$ suggested an estimator. The estimator $\hat\lambda=\bar x-1$ (as printed) suits $\lambda\ll 20$ cm but not when truncation on the right matters. With ad hoc bins one could build estimators for $\lambda\gg 20$ cm, but "no obvious estimator" worked under all conditions. Fitting $P(x|\lambda)$ to a histogram was not satisfactory either (p. 48).

**Gull's solution.** The probability of one data point given $\lambda$:
$$P(x\mid\lambda)=\begin{cases}\frac1\lambda e^{-x/\lambda}/Z(\lambda) & 1<x<20\\ 0&\text{otherwise}\end{cases}\tag{3.1}$$
$$Z(\lambda)=\int_1^{20}dx\,\tfrac1\lambda e^{-x/\lambda}=\left(e^{-1/\lambda}-e^{-20/\lambda}\right)\tag{3.2}$$
(The $Z$ renormalizes the exponential on the window.) Bayes' theorem then turns the data distribution around (p. 49):
$$P(\lambda\mid\{x_1,\dots,x_N\})=\frac{P(\{x\}\mid\lambda)P(\lambda)}{P(\{x\})}\tag{3.3}$$
$$\propto \frac{1}{(\lambda Z(\lambda))^N}\exp\!\Big(-\sum_1^N x_n/\lambda\Big)P(\lambda).\tag{3.4}$$
Figure 3.1 plots $P(x|\lambda)$ against $x$ for $\lambda=2,5,10$: each curve is an exponential of area 1. Plotted against $\lambda$ for fixed $x$ (figure 3.2) the same function is the **likelihood** of $\lambda$, and a peak emerges. Figure 3.3 shows the surface over $(x,\lambda)$; figures 3.1 and 3.2 are vertical sections of it. For several data points the likelihood is the product of the $N$ single-point functions $P(x_n|\lambda)$; figure 3.4 shows it for $\{1.5,2,3,4,5,12\}$ (p. 49).

**Gull's summary** (boxed): what you know about $\lambda$ after the data arrive is what you knew before, $P(\lambda)$, and what the data told you, $P(\{x\}|\lambda)$ (p. 50).

**Meaning of probability here.** Probabilities quantify degrees of belief. The true $\lambda$ is *not* a stochastic variable. The Bayesian does not think the world changes its nature between hypotheses. The probabilities represent beliefs about mutually exclusive hypotheses, of which only one is true (p. 50).

**Claim (author).** The posterior (3.4), the author says, is the unique and complete solution to the problem. There is no need to invent estimators or criteria to compare them. Orthodox statisticians offer many methods and many criteria, whereas Bayesian statistics offers one answer to a well-posed problem (p. 50).

> *Intuition note.* Instead of searching for a clever formula for $\lambda$, write down how likely the data are for each $\lambda$, multiply by what you believed before, and normalize. The whole curve is the answer; any single number is a summary of it.

**Assumptions in inference (author's four arguments, pp. 50–51).** Inference is conditional on assumptions such as the prior. Critics call priors "subjective"; the author sees no way to infer without assumptions and values that Bayesian methods make tacit assumptions explicit.
1. *Objectivity given assumptions.* Anyone with the same information and assumptions $\mathcal H$ reaches the same posterior (p. 50):
$$P(\lambda\mid D,\mathcal H)=\frac{P(D\mid\lambda,\mathcal H)P(\lambda\mid\mathcal H)}{P(D\mid\mathcal H)}\tag{3.5}$$
2. *Easier to criticize and to check sensitivity.* From figure 3.2, a single point at $x=5$ gives a less strongly peaked likelihood than $x=3$. The prior matters more as $\bar x$ approaches the middle of the window, 10.5. For $x=12$ there is no peak: the data only rule out small $\lambda$ and say nothing about the relative probability of large $\lambda$. So the prior matters at the large-$\lambda$ end and not at the small-$\lambda$ end (p. 50).
3. *Comparing assumptions is another inference.* With $I$ the highest assumptions, not questioned (pp. 50–51):
$$P(\mathcal H\mid D,I)=\frac{P(D\mid\mathcal H,I)P(\mathcal H\mid I)}{P(D\mid I)}\tag{3.6}$$
4. *Predictions can include assumption uncertainty*, by the sum rule (p. 51):
$$P(\mathbf t\mid D,I)=\sum_{\mathcal H}P(\mathbf t\mid D,\mathcal H,I)P(\mathcal H\mid D,I)\tag{3.7}$$
This contrasts with orthodox practice of testing a default model and, if the test accepts it at some significance level, using only that model for predictions (p. 51).

Gull's lesson (boxed): "probability theory reaches parts that ad hoc methods cannot reach." (p. 51)

### 3.2 The bent coin (pp. 51–52)
A bent coin is tossed $F$ times, giving a sequence $\mathbf s$ of a's and b's. We want the bias and the probability that the next toss is a. This is the original problem studied by Thomas Bayes (essay published 1763) (p. 51).

Assumptions $\mathcal H_1$: probability of a sequence with counts $\{F_a,F_b\}$, and a uniform prior (p. 51):
$$P(\mathbf s\mid p_a,F,\mathcal H_1)=p_a^{F_a}(1-p_a)^{F_b}\tag{3.8}$$
$$P(p_a\mid\mathcal H_1)=1,\quad p_a\in[0,1],\quad p_b\equiv1-p_a\tag{3.9}$$
Example: $P(\mathbf s=\texttt{aaba}\mid p_a,F=4,\mathcal H_1)=p_ap_a(1-p_a)p_a$. The author does not claim the uniform prior is fundamental. It is "a subjective assumption", and a theme of the book is that you can't do inference or data compression without making assumptions (p. 51).

**Posterior** (pp. 51–52):
$$P(p_a\mid\mathbf s,F,\mathcal H_1)=\frac{P(\mathbf s\mid p_a,F,\mathcal H_1)P(p_a\mid\mathcal H_1)}{P(\mathbf s\mid F,\mathcal H_1)}\tag{3.10}$$
$$=\frac{p_a^{F_a}(1-p_a)^{F_b}}{P(\mathbf s\mid F,\mathcal H_1)}\tag{3.11}$$
The normalizing constant is the beta integral:
$$P(\mathbf s\mid F,\mathcal H_1)=\int_0^1dp_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!\,F_b!}{(F_a+F_b+1)!}\tag{3.12}$$
Exercise 3.5 asks for the posterior shape, mode and mean for $\mathbf s=\texttt{aba}$ and $\texttt{bbb}$ with $F=3$ (answers in section 3.6).

**From inference to prediction.** Predictions are probabilities. Integrate over $p_a$ by the sum rule, so that uncertainty about $p_a$ is carried through (p. 52):
$$P(\texttt a\mid\mathbf s,F)=\int dp_a\,P(\texttt a\mid p_a)P(p_a\mid\mathbf s,F)\tag{3.13}$$
Since $P(\texttt a\mid p_a)=p_a$:
$$P(\texttt a\mid\mathbf s,F)=\int dp_a\,p_a\frac{p_a^{F_a}(1-p_a)^{F_b}}{P(\mathbf s\mid F)}\tag{3.14}$$
$$=\int dp_a\frac{p_a^{F_a+1}(1-p_a)^{F_b}}{P(\mathbf s\mid F)}\tag{3.15}$$
$$=\left[\frac{(F_a+1)!\,F_b!}{(F_a+F_b+2)!}\right]\Big/\left[\frac{F_a!\,F_b!}{(F_a+F_b+1)!}\right]=\frac{F_a+1}{F_a+F_b+2}\tag{3.16}$$
This is **Laplace's rule** (p. 52).

> *Intuition note.* (Our reading of (3.16), not stated in the text.) The rule is like having seen one extra a and one extra b before starting. Because the prediction averages over all plausible biases, it never says "certainly a" or "certainly b" after finitely many tosses.

### 3.3 The bent coin and model comparison (pp. 52–54)
A scientist proposes $\mathcal H_0$: the source is a fair die with one face painted a and five painted b, so $p_a=p_0=1/6$ is not a free parameter. The subscript on each model counts its free parameters (p. 52). We want to know how probable $\mathcal H_1$ is relative to $\mathcal H_0$.

**Model comparison as inference.** Apply Bayes' theorem with a model on the left (p. 53):
$$P(\mathcal H_1\mid\mathbf s,F)=\frac{P(\mathbf s\mid F,\mathcal H_1)P(\mathcal H_1)}{P(\mathbf s\mid F)}\tag{3.17}$$
$$P(\mathcal H_0\mid\mathbf s,F)=\frac{P(\mathbf s\mid F,\mathcal H_0)P(\mathcal H_0)}{P(\mathbf s\mid F)}\tag{3.18}$$
If only these two models are considered:
$$P(\mathbf s\mid F)=P(\mathbf s\mid F,\mathcal H_1)P(\mathcal H_1)+P(\mathbf s\mid F,\mathcal H_0)P(\mathcal H_0)\tag{3.19}$$
Priors might be set to 1/2 each. $P(\mathbf s\mid F,\mathcal H_1)$ is called the **evidence** for $\mathcal H_1$. It already appeared as the normalizing constant in (3.10). Boxed rule: the evidence for a model is usually the normalizing constant of an earlier Bayesian inference (p. 53).

For $\mathcal H_0$ there is nothing to infer:
$$P(\mathbf s\mid F,\mathcal H_0)=p_0^{F_a}(1-p_0)^{F_b}\tag{3.20}$$
Posterior ratio:
$$\frac{P(\mathcal H_1\mid\mathbf s,F)}{P(\mathcal H_0\mid\mathbf s,F)}=\frac{P(\mathbf s\mid F,\mathcal H_1)P(\mathcal H_1)}{P(\mathbf s\mid F,\mathcal H_0)P(\mathcal H_0)}\tag{3.21}$$
$$=\frac{F_a!\,F_b!}{(F_a+F_b+1)!}\Big/p_0^{F_a}(1-p_0)^{F_b}\tag{3.22}$$
(Added step: (3.22) is (3.21) with equal priors, so that $P(\mathcal H_1)/P(\mathcal H_0)=1$ cancels.)

**Table 3.5** (ratio $P(\mathcal H_1|\mathbf s,F)/P(\mathcal H_0|\mathbf s,F)$):

| F | Data $(F_a,F_b)$ | Ratio |
|---|---|---|
| 6 | (5,1) | 222.2 |
| 6 | (3,3) | 2.67 |
| 6 | (2,4) | 0.71 (=1/1.4) |
| 6 | (1,5) | 0.356 (=1/2.8) |
| 6 | (0,6) | 0.427 (=1/2.3) |
| 20 | (10,10) | 96.5 |
| 20 | (3,17) | 0.2 (=1/5) |
| 20 | (0,20) | 1.83 |

Observations (author): some outcomes favour one model and some the other. No outcome is completely incompatible with either. With small data (six tosses) one model is typically not overwhelmingly more probable. With more data, evidence against $\mathcal H_0$ accumulates for any data set whose $F_a:F_b$ differs from 1:5. One cannot predict in advance how much data are needed to be pretty sure which theory is true; it depends on $p_a$. The simpler model $\mathcal H_0$ can lose by the biggest margin (odds may be hundreds to one against it), whereas the more complex model can never lose out by a large margin, since no data set is actually unlikely given $\mathcal H_1$ (p. 53).

> *Intuition note.* $\mathcal H_1$ spreads its predictions over all possible biases, so no data set is very surprising to it. $\mathcal H_0$ bets everything on 1/6, so it can lose by a large margin when the data disagree. (Link to Bayesian Occam's razor; canon link, not stated in this unit.)

**Typical behaviour (figure 3.6, p. 54).** Simulated experiments show $\ln\frac{P(\mathbf s|F,\mathcal H_1)}{P(\mathbf s|F,\mathcal H_0)}$ against $F$ in three conditions: $\mathcal H_0$ true ($p_a=1/6$), and $\mathcal H_1$ true with $p_a=0.25$ or $0.5$. Exercises 3.6 and 3.7 ask about how the log evidence scales with $F$ and what range is plausible (see Exercises). Figure 3.8 (p. 60) shows the plausible range. Model comparison is to be discussed more in a later chapter (p. 54).

### 3.4 An example of legal evidence (pp. 55–57)
**Problem (Exercise 3.4).** Two people left blood at a crime scene, of types O (frequency 60%) and AB (frequency 1%). Suspect Oliver has type O. Do the data favour the proposition that Oliver was present? (p. 55)

**Careless-lawyer claim:** the suspect's type being at the scene is positive evidence he was there. The author says this is not so (p. 55).

Define $S$: the suspect and one unknown person were present; $\bar S$: two unknown people from the population were present. The prior odds of $S$ vs. $\bar S$ come from all other information. The contribution of the data $D$ is the likelihood ratio $P(D|S,\mathcal H)/P(D|\bar S,\mathcal H)$. **Author's view:** a jury should generally multiply carefully evaluated likelihood ratios for each independent piece of admissible evidence by an equally careful prior. He notes that many statisticians share this view, but that British appeal judges recently overturned a verdict because jurors had been taught to use Bayes' theorem for DNA evidence (p. 55).

Here $\mathcal H$ = two people were present and left blood, and unknown people's blood groups follow population frequencies.
$$P(D\mid S,\mathcal H)=p_{AB}\tag{3.24}$$
(given $S$, one trace is already known to be O),
$$P(D\mid\bar S,\mathcal H)=2p_Op_{AB}\tag{3.25}$$
(added step: the factor 2 counts which of the two unknown people has which type).
$$\frac{P(D\mid S,\mathcal H)}{P(D\mid\bar S,\mathcal H)}=\frac1{2p_O}=\frac1{2\times0.6}=0.83\tag{3.26}$$
So the data are weak evidence *against* Oliver's presence (p. 55).

**Checks of the result (pp. 55–57).**
- A suspect Alberto of type AB: ratio $=1/(2p_{AB})=50$ (3.27), in favour of $S'$ (p. 56).
- Change the population: 99% type O, the rest AB. Intuitively, the rare AB blood still favours Alberto. If O blood favoured Oliver, then whoever the suspect was, the data would make them more probable to have been present, which would be absurd. Evidence *for* some theories must be evidence *against* others (p. 56).
- Ten stains, population of 100 (90 O, 10 AB): prior chance for a given O suspect is 1 in 10. Finding nine AB stains and one O stain leaves a "one in ninety" chance for Oliver, since only one person present was type O (p. 56).
- General case: $n_O$ type-O stains and $n_{AB}$ type-AB stains, $N$ in total, unknowns drawn from a large population with fractions $p_O,p_{AB}$. Hypotheses: $S$ (Oliver plus $N-1$ unknowns) and $\bar S$ ($N$ unknowns). Then (p. 56)
$$P(n_O,n_{AB}\mid\bar S)=\frac{N!}{n_O!\,n_{AB}!}p_O^{n_O}p_{AB}^{n_{AB}}\tag{3.28}$$
$$P(n_O,n_{AB}\mid S)=\frac{(N-1)!}{(n_O-1)!\,n_{AB}!}p_O^{n_O-1}p_{AB}^{n_{AB}}\tag{3.29}$$
$$\frac{P(n_O,n_{AB}\mid S)}{P(n_O,n_{AB}\mid\bar S)}=\frac{n_O/N}{p_O}\tag{3.30}$$
(Added step: dividing, the factorial ratios give $n_O/N$ and the powers leave $1/p_O$.)

The likelihood ratio depends only on comparing the frequency of Oliver's type in the observed stains with its background frequency. It does not depend on the other types' counts or frequencies. More O stains than expected under $\bar S$ favour Oliver's presence, fewer reduce its probability, and when $n_O/N=p_O$ the data contribute no evidence either way, even though they are compatible with $S$ (pp. 56–57).

> *Intuition note.* Being compatible with a hypothesis is not the same as being evidence for it. Evidence is how much more likely the data are under one hypothesis than another. Matching a common type is what you would expect by chance.

### 3.5 Exercises (pp. 57–59)
The statements, in brief:
- **3.8 Three doors, normal rules.** The host opens an unchosen door that hides no prize. The contestant chose door 1 and the host opened door 3. Stick, switch or no difference? (p. 57)
- **3.9 Three doors, earthquake.** The same, but door 3 flies open by an earthquake and has no prize. Assume the prize is placed randomly and the host does not know where it is (p. 57). A variant has a confused host who opens an unchosen door at random.
- **3.10 Three children.** The two clues establish that at least one child is a girl and at least one is a boy. Probabilities of two girls and one boy, versus two boys and one girl (pp. 57–58).
- **3.11 Wife-beating lawyer.** Prosecution cites at least nine previous beatings. The lawyer replies that only 1 in 1000 wife-beaters murders his wife, so the history is not strong evidence. Is the lawyer right? (p. 58) The footnote gives US figures: 4739 women homicide victims in 1994, of whom 1326 (28%) were slain by husbands and boyfriends (p. 58).
- **3.12 Bag with one counter**, white or black. A white counter is added and a white one is drawn. What is the chance of drawing white now? (p. 58)
- **3.13 Phone number.** You dial 740511 and get a busy signal. Are you more sure of your number? (p. 58)
- **3.14 Two-coin prize game.** Fred points to a head and claims the prize. What is the probability that the other coin is a head? (pp. 58–59)
- **3.15 Belgian euro.** 140 heads in 250 spins; a statistician says that a result this extreme would have chance below 7% if the coin were fair. Do the data give evidence of bias rather than fairness? Hint: use (3.22) (p. 59).

### 3.6 Solutions (pp. 59–64)

**3.1 (p. 59).** With equal priors, $\frac{P(A|D)}{P(B|D)}=\frac{1}{2}\frac{3}{2}\frac{1}{1}\frac{3}{2}\frac{1}{2}\frac{2}{2}\frac{1}{2}=\frac{9}{32}$ (3.31), so $P(A|D)=9/41$.

**3.2 (p. 59).** $P(D|A)=18/20^7$, $P(D|B)=64/20^7$, $P(D|C)=1/20^7$ (3.32–3.34). Hence $P(A|D)=18/83$, $P(B|D)=64/83$, $P(C|D)=1/83$ (3.35).

**3.5 (pp. 59–60).** For $\texttt{aba}$: posterior $\propto p_a^2(1-p_a)$, mode $2/3$, mean $3/5$ (fig. 3.7a). For $\texttt{bbb}$: posterior $\propto(1-p_a)^3$, mode 0, mean $1/5$ (fig. 3.7b). (Added check: both means equal $(F_a+1)/(F_a+F_b+2)$, consistent with (3.16).)

**3.7 (p. 60).** Figure 3.8 was made by taking $F_a$ at its mean $p_aF$ (solid line) and at mean ± two standard deviations (dotted lines, roughly the 2.5th and 97.5th percentiles), and computing the log evidence ratio for each.

**3.8 (pp. 60–61).** Let $\mathcal H_i$ = prize behind door $i$, with prior $P(\mathcal H_i)=1/3$ (3.36). The datum $D$ is which door the host opens. If the prize is behind door 1 the host chooses at random between 2 and 3. Otherwise the choice is forced:
$$P(D{=}2|\mathcal H_1)=\tfrac12,\ P(D{=}2|\mathcal H_2)=0,\ P(D{=}2|\mathcal H_3)=1;\quad P(D{=}3|\mathcal H_1)=\tfrac12,\ P(D{=}3|\mathcal H_2)=1,\ P(D{=}3|\mathcal H_3)=0\tag{3.37}$$
$$P(\mathcal H_i|D{=}3)=\frac{P(D{=}3|\mathcal H_i)P(\mathcal H_i)}{P(D{=}3)}\tag{3.38}$$
with numerators $(1/2)(1/3)$, $(1)(1/3)$, $(0)(1/3)$ (3.39). The denominator $P(D{=}3)=1/2$ is the normalizing constant, so
$$P(\mathcal H_1|D{=}3)=1/3,\quad P(\mathcal H_2|D{=}3)=2/3,\quad P(\mathcal H_3|D{=}3)=0\tag{3.40}$$
The contestant should switch to door 2. To make it intuitive: play 30 times with a friend, or imagine a million doors where the host opens 999,998 of the others without revealing the prize, leaving door 1 and one other door (p. 61).

**3.9 (p. 61).** The data now are different: which doors the earthquake opened, $\mathbf d$ (eight possible outcomes), plus whether the prize was visible. The observed datum is $\mathbf d=(0,0,1)$ with no prize visible. Only the relative values of $P(D|\mathcal H_i)$ for this actual $D$ matter (the likelihood principle, section 2.3). $P(D|\mathcal H_3)=0$. By symmetry, $P(D|\mathcal H_1)=P(D|\mathcal H_2)$, assuming that earthquakes are not sensitive to the contestant's decisions. So
$$P(\mathcal H_1|D)=1/2,\quad P(\mathcal H_2|D)=1/2,\quad P(\mathcal H_3|D)=0\tag{3.41}$$
The doors are equally likely. If the host knows where the prize is and might act deceptively, his words would become part of the data and the answer might change. Gull's rule (boxed): "Always write down the probability of everything." From the joint probability (figure 3.9, a table of which doors the earthquake opened against where the prize is) any inference follows mechanically (p. 61).

> *Intuition note.* In both games door 3 is open and empty, but in the first the host's choice was *forced to avoid* the prize, whereas in the second it was independent of the prize. What matters is how the observation could have come about, not what the scene looks like.

**3.11 (pp. 61–62).** The lawyer's statistic is the probability that a random wife-beater goes on to murder his wife. The relevant quantity is the probability that the husband is the murderer *given that the wife has been murdered*, which the author says is a completely different quantity. It depends on the chance of murder by someone else (high in a neighbourhood with frequent random murders, lower in peaceful regions). With $m=1$: woman murdered; $h=1$: husband did it; $b=1$: he beat her in the preceding year. From the statistics, $P(h{=}1|m{=}1)=0.28$. If 2 million of 100 million women are beaten, $P(b{=}1|h{=}0,m{=}1)=0.02$. The author guesses $P(b{=}1|h{=}1,m{=}1)=0.9$ or larger (the author expects it to be pretty unlikely that a murder is the first violence). Then
$$P(h{=}1|b{=}1,m{=}1)=\frac{.9\times.28}{.9\times.28+.02\times.72}\simeq95\%\tag{3.42}$$
The author builds a same-structure argument that is clearly wrong: the lawyer could say that only one in a million wife-beaters murders his wife between 4.02pm and 4.03pm, which would make the evidence look weaker still (p. 62).

**3.13 (pp. 62–63).** $\mathcal H_0$: the number is 740511; $\mathcal H_1$: it is another number. $D$: dialling 740511 gave a busy signal. $P(D|\mathcal H_0)=1$. Under $\mathcal H_1$, $P(D|\mathcal H_1)=\alpha\beta$, where $\alpha$ is the probability that a random number similar to yours is a valid phone number and $\beta$ the probability of a busy signal on a valid number. The author's estimates: about 75 000 valid six-digit numbers in Cambridge, so 0.075 of all six-digit numbers; excluding those starting with 0, 1, 9, $\alpha\simeq75000/700000\simeq0.1$; with clustering $\alpha$ may be bigger, so it must lie somewhere between 0.1 and 1. $\beta\approx1\%$ by day (in use), maybe 0.1% or fewer at 4 am. So $P(D|\mathcal H_1)\approx0.1\times0.01=10^{-3}$ (or about $10^{-2}$ if numbers are strongly clustered, $10^{-4}$ in the small hours).
$$\frac{P(\mathcal H_0|D)}{P(\mathcal H_1|D)}=\frac{P(D|\mathcal H_0)}{P(D|\mathcal H_1)}\frac{P(\mathcal H_0)}{P(\mathcal H_1)}\tag{3.43}$$
The likelihood ratio is about 100:1 to 1000:1. With prior $P(\mathcal H_0)=0.5$:
$$P(\mathcal H_0|D)=\frac{1}{1+\frac{P(\mathcal H_1|D)}{P(\mathcal H_0|D)}}\simeq0.99\ \text{or}\ 0.999\tag{3.44}$$

**3.15 (pp. 63–64).** Compare $\mathcal H_0$ (fair) with $\mathcal H_1$ (biased, uniform prior $P(p|\mathcal H_1)=1$). The author reads $\mathcal H_0$ as fair to within one part in a thousand, $p\in0.5\pm0.001$, to answer the pedant who says no coin is exactly fair. He finds the uniform prior reasonable because some coins (American pennies) have severe biases when spun on edge. Likelihood ratio:
$$\frac{P(D|\mathcal H_1)}{P(D|\mathcal H_0)}=\frac{140!\,110!/251!}{1/2^{250}}=0.48\tag{3.45}$$
So the data give weak evidence, about two to one, in favour of $\mathcal H_0$ (figure 3.10).

**Objection (believer in bias):** the uniform prior does not reflect his expectation of only a small bias. To be generous to $\mathcal H_1$ the author allows a Beta prior, with $\alpha=1$ giving the uniform prior:
$$P(p|\mathcal H_1,\alpha)=\frac1{Z(\alpha)}p^{\alpha-1}(1-p)^{\alpha-1},\quad Z(\alpha)=\Gamma(\alpha)^2/\Gamma(2\alpha)\tag{3.46}$$
$$\frac{P(D|\mathcal H_1,\alpha)}{P(D|\mathcal H_0)}=\frac{\Gamma(140+\alpha)\Gamma(110+\alpha)\Gamma(2\alpha)2^{250}}{\Gamma(250+2\alpha)\Gamma(\alpha)^2}\tag{3.47}$$
**Figure 3.11** (α → ratio): .37 → .25; 1.0 → .48; 2.7 → .82; 7.4 → 1.3; 20 → 1.8; 55 → 1.9; 148 → 1.7; 403 → 1.3; 1096 → 1.1. Even the most favourable α (≃ 50) gives only two to one in favour of $\mathcal H_1$. The data are not "very suspicious": at most two-to-one for one or other hypothesis (p. 64).

**Strongest possible case.** The prior best matched to the data puts $p=f\equiv140/250$ with probability one (model $\mathcal H_*$). Then $P(D|\mathcal H_*)/P(D|\mathcal H_0)=2^{250}f^{140}(1-f)^{110}=6.1$. So six-to-one is the strongest evidence these data can muster against "no bias" (p. 64).

**p-values (author's sermon).** With 141 heads instead of 140 the p-value is 0.0497, below the "mystical" 0.05, and the sampling-theory statistician would reject the null at 5%. **Figure 3.12** ($D'$ = 141 heads; α → ratio): .37 → .32; 1.0 → .61; 2.7 → 1.0; 7.4 → 1.6; 20 → 2.2; 55 → 2.3; 148 → 1.9; 403 → 1.4; 1096 → 1.2. With the uniform prior the ratio is 1:0.61 in favour of $\mathcal H_0$, and the best α gives about 2.3:1 in favour of $\mathcal H_1$. A p-value of 0.05 is often read as odds of about twenty-to-one against the null, but here the evidence either slightly favours the null or disfavours it by at most 2.3 to one. Conclusion (the author's "sermon"): p-values and significance levels should be treated with extreme caution (p. 64).

> *Intuition note.* A p-value only asks how extreme the data are under the null. The Bayesian ratio also asks how well the alternative explains them. When the alternative cannot explain the data much better than the null does, an "extreme" result is not strong evidence for the alternative.

## Toy example (ours, not from the text)
Three tosses give $\mathbf s=\texttt{aab}$, so $F_a=2$, $F_b=1$, $F=3$. Compare $\mathcal H_1$ (uniform prior on $p_a$) with $\mathcal H_0$ ($p_a=1/6$), equal priors.

- Evidence for $\mathcal H_1$ by (3.12): $\frac{2!\,1!}{4!}=\frac{2}{24}=\frac1{12}=\frac{18}{216}$.
- Evidence for $\mathcal H_0$ by (3.20): $(1/6)^2(5/6)=\frac{5}{216}$.
- Ratio (3.22): $\frac{18/216}{5/216}=\frac{18}{5}=3.6$.
- Posterior of $\mathcal H_1$: $\frac{3.6}{1+3.6}=\frac{3.6}{4.6}=\frac{18}{23}\approx0.78$.
- Prediction under $\mathcal H_1$ alone by Laplace's rule (3.16): $\frac{2+1}{3+2}=\frac35$. Under $\mathcal H_0$ it would be $1/6$. Averaging by (3.7): $\frac{18}{23}\cdot\frac35+\frac{5}{23}\cdot\frac16=\frac{54}{115}+\frac{5}{138}$. With common denominator 690: $\frac{324}{690}+\frac{25}{690}=\frac{349}{690}\approx0.506$. (Here $P(\mathcal H_0|D)=1-\frac{18}{23}=\frac5{23}$.)

The model-averaged prediction lies between the two models' predictions, weighted by their posterior probabilities.

## Concepts
- [[bayes-theorem]] — posterior ∝ likelihood × prior, used for parameters ($\lambda$, $p_a$) and for models alike (p. 49, p. 53)
- [[prior-distribution]] — belief about the parameter before data; called a subjective assumption that must be explicit (p. 50, p. 51)
- [[likelihood]] — $P(\text{data}|\text{parameter})$ viewed as a function of the parameter (p. 49)
- [[posterior-distribution]] — what you know after the data; the author calls it the unique and complete solution (p. 50)
- [[marginal-likelihood-evidence]] — $P(\mathbf s|F,\mathcal H)$, usually the normalizing constant of an earlier parameter inference; used to compare models (p. 53)
- [[subjective-probability]] — probabilities as degrees of belief about hypotheses, not as randomness in the world (p. 50)
- [[posterior-predictive-distribution]] — predictions that integrate or sum over uncertainty about parameters and models (pp. 51–52)
- [[frequentist-vs-bayesian]] — author contrasts estimators, tests and p-values with the single Bayesian posterior (pp. 50–51, 64)
- [[bayesian-occams-razor]] — only the observed behaviour is stated: the simple model can lose by a large margin and the complex one cannot (p. 53). The name is canon, not used in this unit.
- [[laplace-rule]] (new) — $P(\texttt a|\mathbf s,F)=(F_a+1)/(F_a+F_b+2)$ from the uniform prior (p. 52)
- [[likelihood-ratio]] (new) — $P(D|\mathcal H_1)/P(D|\mathcal H_2)$, the data's contribution to the posterior odds (p. 55)
- [[likelihood-principle]] (new) — only the likelihoods of the observed data matter for inference; mentioned, referring to section 2.3 (p. 61)
- [[p-value-critique]] (new) — a "significant" p-value need not mean substantial evidence against the null (p. 64)

## Canonical instances
- [[decay-constant-problem]] — truncated exponential inference of $\lambda$ without estimators (pp. 48–51)
- [[bent-coin]] — posterior for the bias, Laplace's rule and model comparison with $p_a=1/6$ (pp. 51–54)
- [[blood-evidence]] — likelihood ratio 0.83 for Oliver, 50 for Alberto; general result $(n_O/N)/p_O$ (pp. 55–57)
- [[three-doors]] — normal rules give 1/3 vs 2/3; earthquake gives 1/2 vs 1/2 (pp. 60–61)
- [[wife-beater-lawyer]] — transposed conditionals; 95% under stated assumptions (pp. 61–62)
- [[phone-number-busy-signal]] — likelihood ratio of 100–1000 from a busy signal (pp. 62–63)
- [[euro-coin-spin]] — 140 and 141 heads in 250 spins; p-values vs. likelihood ratios (pp. 63–64)

## Bridges (candidates)
- [same-math] Laplace's rule (3.16) ↔ bayesian: Beta–Binomial conjugate updating with a Beta(1,1) prior, posterior mean $(F_a+1)/(F+2)$.
- [same-math] "Evidence" as normalizing constant, evidence ratio ↔ bayesian: marginal likelihood and model comparison.
- [structural-analogy] Host's rule for opening doors (forced vs. random vs. earthquake) ↔ bayesian: assignment mechanism / ignorability; how an observation arose determines what it means.
- [structural-analogy] Lawyer's mistake (P(murder | beater) vs. P(husband did it | murder, beater)) ↔ bayesian: base-rate neglect, ignoring how common alternative explanations are.
- [structural-analogy] Bent-coin inference ↔ information-theory: adaptive data compression, which the author says will use this same problem in Chapter 6 (p. 51).
- [metaphor] "Always write down the probability of everything" ↔ bayesian: the full joint distribution as a calculator for any conditional.

## Questions this raises
- If the evidence depends on the prior over parameters (as α shows in figures 3.11–3.12), how far can model comparison be trusted when the prior is arbitrary?
- How is the posterior (3.4) actually computed and summarized in practice, e.g. when no closed form exists, as for the decay-constant problem?
- The author says the "highest assumptions" $I$ are not questioned. Can an assumption set ever be fully tested without a still higher one?
- What other decision rules, beyond switching in the door problems, follow from a posterior, and how are posteriors turned into actions?

## Exercises worth doing
- Ex. 3.6 (p. 54) — log evidence ratio grows linearly in $F$ if $\mathcal H_1$ is more probable but at most as $\log F$ in favour of $\mathcal H_0$; builds intuition on how fast the evidence can grow for each model — difficulty: medium
- Ex. 3.7 (p. 54) — plausible range of log evidence as a function of $F$ and the true $p_a$, using the mean and standard deviation of $F_a$; links sampling theory to evidence — difficulty: hard
- Ex. 3.10 (pp. 57–58) — two evidence sources about children's sexes; an example the source says is not about priors — difficulty: medium
- Ex. 3.12 (p. 58) — bag with one counter; tests careful use of Bayes' theorem on a symmetric-looking setup — difficulty: medium
- Ex. 3.14 (pp. 58–59) — two coins, "that coin's a head"; asks for the probability that the other coin is a head, given what Fred says — difficulty: easy

## Reading notes
- Page offset: printed = pdf − 12 (pdf 59–76 = printed 47–64). The labels give printed numbers and all citations use them.
- Section 3.6 solutions and the figure captions are on printed pages 59–64. The answer pointer for exercise 3.3 is p. 48 (section 3.1); that section sets up the posterior (3.4) and its discussion but does not evaluate a final estimate of $\lambda$.
- The text layer of equations (3.1)–(3.4), (3.28)–(3.30) and (3.45)–(3.47) is garbled. Equations were checked against the page images.
- In the discussion of estimators (p. 48) the image shows "$\hat\lambda=\bar x-1$"; the source does not explain the subtraction, so no interpretation is given here.
- The 1-in-90 ten-stain argument (p. 56) is an informal finite-population count. The source does not tie it numerically to (3.30), which assumes a large population.
- Exercises 3.6, 3.10, 3.12 and 3.14 carry no solution pointer and have no printed solution on these pages. Exercises 3.1, 3.2, 3.5, 3.7, 3.8, 3.9, 3.11, 3.13 and 3.15 have solutions in section 3.6; exercise 3.4's pointer is p. 55, i.e. section 3.4 itself, and exercise 3.3's is p. 48.
- Copyright note on each page: Cambridge University Press 2003, on-screen viewing permitted.
