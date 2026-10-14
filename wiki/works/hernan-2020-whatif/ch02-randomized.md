---
id: hernan-2020-whatif/ch02-randomized
work: hernan-2020-whatif
unit: "2 Randomized experiments"
pages: 13-26
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Randomized experiments (Hernán & Robins, ch. 2)

## L0 — One line
In an ideal randomized experiment the treated and untreated are expected to be exchangeable, so association is causation; when randomization depends on a covariate $L$, standardization or inverse probability weighting recovers the same population-wide causal effect.

## L1 — The gist (≤ 120 words)
How can we compute causal effects when each person reveals only one potential outcome? Randomization makes the missing counterfactuals missing "by chance". Treatment is then independent of the potential outcomes (exchangeability), so observed risks equal counterfactual risks. If the coin's probability depends on a covariate $L$, exchangeability holds only within levels of $L$. Two methods then recover the population-wide effect: standardization (average the stratum-specific risks over the distribution of $L$) and inverse probability weighting (weight each person by 1 / probability of the treatment actually received). The two methods are mathematically equivalent. Randomized experiments are often unethical, impractical or too slow, which motivates observational studies.

**Prerequisites:** probability and conditional probability; independence; expectation as a weighted average; sums over categories; risk ratio and risk difference (from ch. 1).

## L2 — Key ideas
- Randomization makes the missing counterfactual outcomes occur by chance, so effect measures can be consistently estimated despite missing data (p. 13).
- Exchangeability, $Y^a \perp\!\!\!\perp A$ for all $a$, means treatment does not predict the counterfactual outcome. Randomization is expected to produce it. Under it, risk under treatment $a$ in the whole population equals the observed risk among those who received $a$ (pp. 14–15).
- $Y^a \perp\!\!\!\perp A$ differs from $Y \perp\!\!\!\perp A$. With a causal effect, the observed outcome is associated with treatment even under exchangeability (p. 15).
- Marginal randomization (one coin) gives marginal and conditional exchangeability. Conditional randomization (coin depends on $L$) gives only conditional exchangeability, $Y^a \perp\!\!\!\perp A \mid L$ (p. 18).
- Standardization: $\Pr[Y^a=1]=\sum_l \Pr[Y=1\mid L=l,A=a]\Pr[L=l]$ under conditional exchangeability. The counterfactual risk is then identified from observed data (pp. 19–20).
- IP weighting builds a pseudo-population in which $L$ is independent of $A$, using weights $W^A = 1/f[A\mid L]$ (pp. 21–23).
- Standardization and IP weighting give the same value under positivity (every level of $L$ that occurs has a nonzero probability of each treatment level). Both are said to "adjust for" $L$ (pp. 23, 25).
- Randomized experiments are often unethical, impractical or untimely, so observational studies are frequently the least bad option (pp. 23–24).

## L3 — Walkthrough

### Opening example (p. 13)
- The authors pose a causal question: does your looking up at the sky make other pedestrians look up? It has an action, an outcome and a population (p. 13).
- Proposed design: flip a coin for each approaching pedestrian. Heads: look up. Tails: look straight ahead. Compare the proportions who look up within 10 seconds. The result was 55% vs 1% (p. 13).
- This is an *experiment* because the investigator performs the action. It is *randomized* because a random device decides who gets it (p. 13).
- Not every experiment is randomized. If you looked up for men and straight ahead for women, assignment would follow a deterministic rule, and critics could say the groups are "noncomparable" (p. 13).

### 2.1 Randomization (pp. 13–16)
**Missing data.** In a real study we observe only $Y$ under the treatment $A$ actually received. Table 2.1 shows one known counterfactual per person and a "?" for the other (p. 13). Such data give association measures only. Randomization ensures the missing values occurred by chance, so effect measures can be (consistently) estimated (p. 13).

**Setup** (a near-infinite population, a coin flipped per person; p. 14):
- The white group (tails) gets treatment $A=1$. The grey group (heads, with probability below 50%) gets placebo $A=0$ (p. 14).
- Observed 5-day mortality risks: $\Pr[Y=1\mid A=1]=0.3$, $\Pr[Y=1\mid A=0]=0.6$. Associational risk ratio $0.3/0.6=0.5$; associational risk difference $0.3-0.6=-0.3$ (p. 14).
- Assume an *ideal randomized experiment*: no loss to follow-up, full adherence, a single version of treatment, double-blind assignment (p. 14).

**Thought experiment.** If assistants had treated the grey group instead of the white group, the risks would still be 0.3 and 0.6. Group membership was random, so which group got treatment is irrelevant to $\Pr[Y=1\mid A=a]$. The authors call the groups *exchangeable* (p. 14).

**Definition (exchangeability).** For both $a=0,1$ (p. 14):
$$\Pr[Y^a=1\mid A=1]=\Pr[Y^a=1\mid A=0]=\Pr[Y^a=1],\qquad Y^a\perp\!\!\!\perp A \text{ for all } a.$$
- In words: the white group would have had the same death risk as the grey group had it received the grey group's treatment (p. 14).
- The actual treatment $A$ does not predict the counterfactual outcome $Y^a$ (p. 14).
- Randomization is valued because it is *expected* to produce exchangeability (p. 14).
- When the groups are exchangeable, treatment is called *exogenous*. Exogeneity is a common synonym (p. 14).

**Result.** The treated risk is not counterfactual, since the white group was actually treated. Under exchangeability it equals the risk if everyone had been treated (p. 14, 15):
$$\Pr[Y^{a=1}=1]=\Pr[Y=1\mid A=1]=0.3,\qquad \Pr[Y^{a=0}=1]=\Pr[Y=1\mid A=0]=0.6.$$
The causal risk ratio is 0.5 and the causal risk difference is $-0.3$. "In ideal randomized experiments, association *is* causation." (p. 15)

*Intuition note.* Randomization works like shuffling a deck before dealing. The treated group is a random sample of everyone, so its outcome under a given treatment level tells us about everyone's outcome under that level. Observed risks can then stand in for the missing counterfactual risks.

**Second explanation** (p. 15). $Y^a$ is like one's genes: a fixed characteristic that exists before treatment is assigned, because it encodes what would happen under $a$. Randomized $A$ is independent of both genes and $Y^a$. The difference from genes is that $Y^a$ can be learned only after treatment, and only if $A=a$ (p. 15).

**Caution** (p. 15). $Y^a\perp\!\!\!\perp A$ is not $Y\perp\!\!\!\perp A$. If exchangeability holds and treatment has a causal effect, then $Y\perp\!\!\!\perp A$ fails. The reason (margin note): $Y=Y^A$ depends on $A$, so it is not independent of $A$ when $Y^{a=1}\neq Y^{a=0}$ for some individuals (p. 15).

**Technical Point 2.1: full vs mean exchangeability** (p. 15).
- Randomization makes the set of counterfactuals jointly independent of $A$: $Y^{\mathcal A}\perp\!\!\!\perp A$, where $\mathcal A$ is the set of treatment values in the population. This is *full exchangeability*. It implies, but is not implied by, $Y^a\perp\!\!\!\perp A$ for each $a$. For a dichotomous treatment it reads $(Y^{a=1},Y^{a=0})\perp\!\!\!\perp A$ (p. 15).
- For dichotomous outcomes, $Y^a\perp\!\!\!\perp A$ can be written $\Pr[Y^a=1\mid A=1]=\Pr[Y^a=1\mid A=0]$, or $\mathrm E[Y^a\mid A=1]=\mathrm E[Y^a\mid A=0]$ for all $a$ (*mean exchangeability*) (p. 15).
- For a continuous outcome, $Y^a\perp\!\!\!\perp A$ implies mean exchangeability $\mathrm E[Y^a\mid A=a']=\mathrm E[Y^a]$. The converse fails, because other distribution parameters (e.g. variance) may depend on treatment (p. 15).
- To prove $\mathrm E[Y^a]=\mathrm E[Y\mid A=a]$ neither full nor $Y^a\perp\!\!\!\perp A$ exchangeability is required. Mean exchangeability is sufficient. Step 1: $\mathrm E[Y\mid A=a]=\mathrm E[Y^a\mid A=a]$ by consistency. Step 2: $\mathrm E[Y^a\mid A=a]=\mathrm E[Y^a]$ by mean exchangeability (p. 15). For dichotomous outcomes the concepts coincide, so the chapter says just "exchangeability" (p. 15).

**Does exchangeability hold in the heart transplant data?** Using the counterfactual data of Table 1.1 (from chapter 1, not in this unit) (p. 16):
- Risk under no treatment among the 13 treated: $\Pr[Y^{a=0}=1\mid A=1]=7/13$. Among the 7 untreated: $\Pr[Y^{a=0}=1\mid A=0]=3/7$.
- Since $7/13>3/7$, the treated have a worse prognosis, so $Y^a\perp\!\!\!\perp A$ fails for $a=0$. The authors say it also fails for $a=1$ (p. 16).
- In the real world only Table 2.1 is available, which cannot give $\Pr[Y^{a=0}=1\mid A=1]$. So we generally cannot check exchangeability (p. 16).
- Even if it failed, we could not conclude the study was not randomized. First, with 20 people sampling variability could explain almost anything (chapter 10). The authors imagine each person represents 1 billion identical people. Second, a study can be randomized yet lack exchangeability in infinite samples if it uses more than one coin (p. 16).

**Fine Point 2.1: crossover experiments** (p. 16).
- Zeus calls a lightning strike ($a=1$) one morning and his blood pressure rises. The next morning he refrains ($a=0$) and it does not. Seeing both $Y^{a=1}=1$ and $Y^{a=0}=0$ does not generally prove an individual effect, unless strong conditions i)–iii) hold (p. 16).
- Notation: individual $i$ is observed at $t=0,1$ with treatment $A_{it}$. $Y_{i1}^{a_0a_1}$ is the counterfactual outcome at $t=1$ under $a_0$ at $t=0$ and $a_1$ at $t=1$ (p. 16).
- The individual effect $Y_{it}^{a_t=1}-Y_{it}^{a_t=0}$ is identified if: i) no carryover effect, $Y_{it=1}^{a_0,a_1}=Y_{it=1}^{a_1}$; ii) the effect does not depend on time, $Y_{it}^{a_t=1}-Y_{it}^{a_t=0}=\alpha_i$ for $t=0,1$; iii) the no-treatment outcome does not depend on time, $Y_{it}^{a_t=0}=\beta_i$ for $t=0,1$ (p. 16).
- If $A_{i1}=1$, $A_{i0}=0$, then by consistency
$$Y_{i1}-Y_{i0}=Y_{i1}^{a_1=1}-Y_{i0}^{a_0=0}=Y_{i1}^{a_1=1}-Y_{i1}^{a_1=0}+Y_{i1}^{a_1=0}-Y_{i0}^{a_0=0}=\alpha_i+\beta_i-\beta_i=\alpha_i.$$
Similarly if $A_{i1}=0$, $A_{i0}=1$, then $Y_{i0}-Y_{i1}=\alpha_i$ (p. 16).
- Condition (i) needs an abrupt outcome onset that fully resolves by the next period. So crossover designs cannot study an irreversible action (heart transplant) on an irreversible outcome (death) (p. 16).

### 2.2 Conditional randomization (pp. 17–18)
**Two designs** for the data in Table 2.2, which has $L$ (1 = critical condition, measured before assignment), $A$ and $Y$ (p. 17):
- *Design 1 (marginally randomized):* randomly select 65% of the population for transplant, with one loaded coin (probability 0.65). This would explain 13 of 20 treated. It is the design of Section 2.1 (p. 17).
- *Design 2 (conditionally randomized):* coin with probability 0.75 for $L=1$, another with 0.50 for $L=0$. This explains 9 of 12 treated in critical and 4 of 8 in noncritical condition (p. 17).
- Both are randomized experiments (p. 17).

**Exchangeability under each design.**
- A marginally randomized experiment is expected to give $Y^a\perp\!\!\!\perp A$. A conditionally randomized one will not generally, because each group may have a different proportion with bad prognosis (p. 17).
- Table 2.2 has 69% (9/13) of the treated but 43% (3/7) of the untreated in critical condition. The authors conclude these data could not have come from a marginally randomized experiment. Since the study was randomized, it was randomized conditional on $L$ (p. 17).
- A conditionally randomized experiment is the combination of separate marginally randomized experiments within $L=1$ and $L=0$ (p. 17). Within each stratum (p. 18):
$$\Pr[Y^a=1\mid A=1,L=1]=\Pr[Y^a=1\mid A=0,L=1],\quad\text{i.e. } Y^a\perp\!\!\!\perp A\mid L=1\text{ for all } a,$$
and likewise for $L=0$. Writing $Y^a\perp\!\!\!\perp A\mid L$ when this holds for all $l$ gives *conditional exchangeability* (p. 18).
- Marginal randomization produces both marginal and conditional exchangeability. Conditional randomization produces only conditional exchangeability (p. 18).

*Intuition note.* Conditional randomization is several fair experiments run side by side, one per level of $L$. Inside each level the treated and untreated are comparable. Across levels they are not, because $L$ changed the odds of treatment.

**Margin note on missing data** (p. 18). Missing completely at random (MCAR) means $\Pr[A=a\mid L,Y^{a=1},Y^{a=0}]=\Pr[A=a]$, which holds in a marginally randomized experiment. Missing at random (MAR) means the probability of $A=a$ given the full data depends only on the data that would be observed if $A=a$, namely $(L,Y^a)$. MAR implies $\Pr[A=a\mid L,Y^{a=1},Y^{a=0}]=\Pr[A=a\mid L]$, which holds in a conditionally randomized experiment (p. 18). The terms are from Rubin (1976) and Marini, Olsen and Rubin (1980) (p. 18).

**Two options for effects in a conditionally randomized experiment** (p. 18).
- Under marginal exchangeability, the causal ratio equals the associational ratio. Had Table 2.2 come from a marginal experiment, the causal risk ratio would be $\frac{7/13}{3/7}=1.26$ (p. 18).
- *Option 1, stratification:* compute the effect within each stratum. Association is causation within each stratum, so the stratum-specific causal risk ratio equals $\Pr[Y=1\mid L=1,A=1]/\Pr[Y=1\mid L=1,A=0]$, and likewise for $L=0$. If these ratios differ between strata, there is *effect modification* by $L$ (treatment effect heterogeneity). Chapter 4 covers this (p. 18).
- *Option 2:* compute the average causal effect $\Pr[Y^{a=1}=1]/\Pr[Y^{a=0}=1]$ in the entire population. As one example, one may be interested in this if one does not expect to have information on $L$ for future individuals, so the treatment decision cannot depend on $L$. The chapter focuses on this option until chapter 4 (p. 18).

**Fine Point 2.2: risk periods** (p. 19). A risk is the proportion who develop the outcome in a specified period. Example: in a randomized trial of antibiotics for plague, one investigator finds a causal risk ratio of 0.05 (1-year risks) and another finds 1 (100-year risks, which are 1 either way). Both are correct. A causal effect on mortality means death is delayed, not prevented (p. 19).

### 2.3 Standardization (pp. 19–20)
**Worked example** (heart transplant: 8 people with $L=0$ treated with probability 50%, 12 with $L=1$ treated with 75%; each person stands for a billion) (p. 19):
- Stratum risks equal counterfactual risks because $Y^a\perp\!\!\!\perp A\mid L$. For $L=0$: $\Pr[Y=1\mid L=0,A=1]=\Pr[Y^{a=1}=1\mid L=0]=\tfrac14$, and $\Pr[Y=1\mid L=0,A=0]=\Pr[Y^{a=0}=1\mid L=0]=\tfrac14$. For $L=1$: both are $\tfrac23$ (p. 19).
- Risk if all 20 were treated = weighted average with weights proportional to stratum size (40% and 60%): $\tfrac14\times0.4+\tfrac23\times0.6=0.5$. The same reasoning gives $\Pr[Y^{a=0}=1]=0.5$. The causal risk ratio is $0.5/0.5=1$ (p. 19).

**Formula** (p. 20):
$$\Pr[Y^a=1]=\sum_l \Pr[Y^a=1\mid L=l]\Pr[L=l]=\sum_l \Pr[Y=1\mid L=l,A=a]\Pr[L=l],$$
where the second equality uses conditional exchangeability. The left side is an unobserved counterfactual risk, while the right side uses only observed data on $L,A,Y$ (p. 20).

**Identification.** A counterfactual quantity that can be written as a function of the distribution of the observed data is *identified* (identifiable). Otherwise it is unidentified (p. 20).

**Standardization.** The method is called standardization in epidemiology and demography. $\sum_l\Pr[Y=1\mid L=l,A=1]\Pr[L=l]$ is the standardized risk in the treated, with the population as the standard. Under conditional exchangeability it is the risk had all been treated. The margin note defines the standardized mean as $\sum_l \mathrm E[Y\mid L=l,A=a]\Pr[L=l]$ (p. 20). The causal risk ratio is
$$\frac{\sum_l \Pr[Y=1\mid L=l,A=1]\Pr[L=l]}{\sum_l \Pr[Y=1\mid L=l,A=0]\Pr[L=l]}.$$

*Intuition note.* Standardization asks: what would the risk be if everyone were treated? Take the treated-group risk in each stratum, then re-weight the strata to the population's own mix of $L$. The population's mix of $L$ replaces the treated group's mix.

### 2.4 Inverse probability weighting (pp. 20–24)
**Tree of Table 2.2 (Figure 2.1)** (pp. 20–21):
- $\Pr[L=0]=8/20=0.4$, $\Pr[L=1]=12/20=0.6$.
- Within $L=0$: 4 untreated and 4 treated, so $\Pr[A=0\mid L=0]=\Pr[A=1\mid L=0]=0.5$. Within $L=1$: 3 untreated (probability 0.25) and 9 treated (0.75).
- Outcomes: $L=0$, $A=0$: 3 survive, 1 dies, so $\Pr[Y=1\mid L=0,A=0]=1/4$. The $L=0$, $A=1$ branch has the same split (3 survive, 1 dies). For $L=1$, $A=0$: 1 survives, 2 die. For $L=1$, $A=1$: 3 survive, 6 die (risk $2/3$) (Figure 2.1, p. 21).

**Counterfactual counts** (pp. 21–22):
- Everyone untreated: in $L=0$ only 4 of 8 were untreated, with 1 death. Doubling gives 2 deaths. In $L=1$ only 3 of 12 were untreated, with 2 deaths. Multiplying by 4 gives 8 deaths. Total $2+8=10$ deaths among 20, so $\Pr[Y^{a=0}=1]=10/20=0.5$ (p. 21).
- This relies on treated people with $L=0$, had they stayed untreated, having the same death probability as those who did stay untreated. That is exchangeability given $L=0$ (p. 22).
- Everyone treated gives $10/20=0.5$ as well, under exchangeability given $L=1$. The ratio is $0.5/0.5=1$ (p. 22). Figure 2.2 shows the two simulated populations: $L=0$ gives 6 and 2 (survive, die) and $L=1$ gives 4 and 8 (survive, die), in each tree (Figure 2.2, p. 21).

**Pseudo-population** (p. 22). Pool both trees into a hypothetical population twice the original size, where every individual appears both treated and untreated (Figure 2.3). Under $Y^a\perp\!\!\!\perp A\mid L$ in the original population, the treated and untreated in the pseudo-population are (unconditionally) exchangeable, because $L$ is independent of $A$ there. So the associational risk ratio in the pseudo-population equals the causal risk ratio in both populations (p. 22).

**Weights.**
- The 4 untreated with $L=0$ produce 8 pseudo-members, so each has weight $2=1/0.5$, where 0.5 is $\Pr[A=0\mid L=0]$. The 9 treated with $L=1$ produce 12 members, weight $1.33=1/0.75$ (pp. 22–23).
- Informally, each person is weighted by the inverse of the conditional probability of the treatment level she actually received. The weight is $W^A=1/f[A\mid L]$ (p. 23).
- Figure 2.3 weights: 2 for all four $L=0$ cells ($1/.5$), 4 for untreated $L=1$ ($1/.25$), 1.33 for treated $L=1$ ($1/.75$) (Figure 2.3, p. 22).
- IP weighted estimators were proposed by Horvitz and Thompson (1952) for surveys with unequal sampling probabilities (margin note, p. 22).

**Technical Point 2.2: formal IP weights** (p. 23).
- A treated individual with $L=l$ gets $1/\Pr[A=1\mid L=l]$. An untreated individual with $L=l'$ gets $1/\Pr[A=0\mid L=l']$. One expression covers both: $W^A=1/f[A\mid L]$, with $f[a\mid l]$ the conditional density of $A$ given $L$ (for discrete variables, $\Pr[A=a\mid L=l]$). The notation $f[A\mid L]$ is needed because $\Pr[A=A\mid L=L]$ is tautologically 1 (p. 23).
- In a conditionally randomized experiment, $f[a\mid l]>0$ for all $l$ with $\Pr[L=l]\neq0$ (p. 23).
- The mean of the outcome in the pseudo-population equals the IP weighted mean of the population. With $I(A=a)$ the indicator that $A=a$ (p. 23):
$$\begin{aligned}
\mathrm E_{ps}[Y\mid A=a]&=\mathrm E_{ps}[Y\,I(A=a)]/\mathrm E_{ps}[I(A=a)] &&\text{(laws of probability)}\\
&=\mathrm E[W^A Y I(A=a)]/\mathrm E[I(A=a)W^A] &&\text{(definition of }\mathrm E_{ps})\\
&=\mathrm E[Y I(A=a)/\Pr(A=a\mid L)]\big/\mathrm E[I(A=a)/\Pr(A=a\mid L)] &&\text{(since } I(A=a)/f(A\mid L)=I(A=a)/f(a\mid L))\\
&=\mathrm E[Y I(A=a)/\Pr(A=a\mid L)] &&\text{(since }\mathrm E[I(A=a)/\Pr(A=a\mid L)\mid L]=1).
\end{aligned}$$

**Standardization and IP weighting compared** (p. 23).
- They gave the same result here (risk ratio 1). The authors say this is no coincidence: the two are mathematically equivalent (Technical Point 2.3).
- Both build a new tree in which everyone receives treatment $a$, but from different probabilities. IP weighting uses the conditional probability of $A$ given $L$. Standardization uses the probability of $L$ and the conditional probability of $Y$ given $A$ and $L$ (p. 23).
- Both simulate what would have been seen if $L$ had not been used to decide treatment probability, so we say they *adjust for* $L$. "Control for" is a slight abuse: analytic control differs from the physical control of an experiment. Both can be generalized to continuous outcomes (p. 23).

*Intuition note.* IP weighting gives extra weight to people who were unlikely to get the treatment they got, so they stand in for the similar people who got the other treatment. After weighting, treatment no longer depends on $L$, as if $L$ had not been used to decide the probability of treatment (p. 23).

**Why not stop here?** Randomized experiments are often unethical, impractical or untimely (p. 23). For the heart transplant study (p. 24):
- Hearts are scarce, and society favours giving them to those likely to benefit rather than assigning them randomly.
- Double-blind assignment is impossible, patients may refuse to forgo transplant, and compatible hearts may be unavailable.
- It would take years while decisions must be made now.
- So an observational study is often "the least bad option" (the authors' wording, p. 24).

**Technical Point 2.3: equivalence of IP weighting and standardization** (p. 25).
- *Setting.* $A$ is discrete with finitely many values. *Positivity*: $f[a\mid l]>0$ for all $l$ with $\Pr[L=l]\neq0$. This is guaranteed to hold in conditionally randomized experiments (p. 25).
- Standardized mean for level $a$: $\sum_l \mathrm E[Y\mid A=a,L=l]\Pr[L=l]$. IP weighted mean: $\mathrm E\!\left[\dfrac{I(A=a)Y}{f[A\mid L]}\right]$ (p. 25).
- *Equality under positivity.* By definition of expectation (only $A=a$ contributes, since $I(a'=a)=0$ for other $a'$):
$$\mathrm E\!\left[\frac{I(A=a)Y}{f[A\mid L]}\right]=\sum_l \frac{1}{f[a\mid l]}\Big\{\mathrm E[Y\mid A=a,L=l]\,f[a\mid l]\Pr[L=l]\Big\}=\sum_l \Big\{\mathrm E[Y\mid A=a,L=l]\Pr[L=l]\Big\}.$$
  In the last step $f[a\mid l]$ cancels. $A$ and $L$ are treated as discrete. For continuous $L$ replace the sum with an integral (p. 25).
- This proof makes no reference to counterfactuals. If we also assume conditional exchangeability, both means equal $\mathrm E[Y^a]$. Two proofs (p. 25):
  - *Via standardization:*
$$\mathrm E[Y^a]=\sum_l \mathrm E[Y^a\mid L=l]\Pr[L=l]=\sum_l \mathrm E[Y^a\mid A=a,L=l]\Pr[L=l]=\sum_l \mathrm E[Y\mid A=a,L=l]\Pr[L=l].$$
    The second equality uses conditional exchangeability and positivity. The third uses consistency.
  - *Via IP weighting:* $\mathrm E[I(A=a)Y/f[A\mid L]]=\mathrm E[I(A=a)Y^a/f[A\mid L]]$ by consistency. Since positivity implies $f[a\mid L]$ is never 0:
$$\mathrm E\!\left[\frac{I(A=a)}{f[A\mid L]}Y^a\right]=\mathrm E\!\left\{\mathrm E\!\left[\frac{I(A=a)}{f[a\mid L]}Y^a\,\Big|\,L\right]\right\}=\mathrm E\!\left\{\mathrm E\!\left[\frac{I(A=a)}{f[a\mid L]}\,\Big|\,L\right]\mathrm E[Y^a\mid L]\right\}=\mathrm E\{\mathrm E[Y^a\mid L]\}=\mathrm E[Y^a],$$
    using conditional exchangeability in the second step and $\mathrm E[I(A=a)/f[a\mid L]\mid L]=1$ in the third.
- *Continuous treatment* (an unlikely design choice in conditionally randomized experiments). Then $\mathrm E[I(A=a)Y/f(A\mid L)]$ no longer equals the standardized mean and is biased for $\mathrm E[Y^a]$ even under exchangeability. If $f(a\mid l)$ is the conditional density, $\mathrm E[I(A=a)/f(a\mid l)\mid L=l]$ is 0, not 1. If $f(a\mid l)$ is taken as $\Pr[A=a\mid L=l]$, it is zero with probability 1 and positivity fails. Section 12.4 generalizes IP weighting to continuous treatments. Technical Point 3.1 discusses failure of the results without positivity, even for discrete $A$ (p. 25).

*Intuition note.* Standardization and IP weighting are two ways of computing the same average. In the proof, the factor $f[a\mid l]$ in the weight's denominator cancels against the treatment probability inside the expectation (p. 25). The equality is proved under positivity: $f[a\mid l]>0$ for every $l$ with $\Pr[L=l]\neq0$ (p. 25).

## Toy example (ours, not from the text)
A conditionally randomized trial with 10 people. $L=0$ ($n=4$): 2 treated, 1 death; 2 untreated, 1 death. $L=1$ ($n=6$): 4 treated, 3 deaths; 2 untreated, 1 death. $\Pr[L=0]=0.4$, $\Pr[L=1]=0.6$.

*Crude comparison (not causal here):* treated deaths $1+3=4$ of 6, risk $0.667$. Untreated deaths $1+1=2$ of 4, risk $0.5$. Ratio $1.333$. Treatment depends on $L$ ($\Pr[A=1\mid L=0]=0.5$, $\Pr[A=1\mid L=1]=4/6$), so marginal exchangeability is not guaranteed.

*Standardization:* stratum risks treated $=1/2$ ($L=0$), $3/4$ ($L=1$); untreated $=1/2$, $1/2$.
- $\Pr[Y^{a=1}=1]=0.5(0.4)+0.75(0.6)=0.2+0.45=0.65$.
- $\Pr[Y^{a=0}=1]=0.5(0.4)+0.5(0.6)=0.2+0.3=0.5$.
- Causal risk ratio $=0.65/0.5=1.3$.

*IP weighting:* weights $=1/\Pr[A=a\mid L]$.
- $L=0$: all four people have weight $1/0.5=2$.
- $L=1$: treated weight $1/(4/6)=1.5$, untreated weight $1/(2/6)=3$.
- Pseudo-population, treated: $L=0$ gives $2\times2=4$ people and $1\times2=2$ deaths. $L=1$ gives $4\times1.5=6$ people and $3\times1.5=4.5$ deaths. Total 10 people, 6.5 deaths, risk $0.65$.
- Pseudo-population, untreated: $L=0$ gives $2\times2=4$ people and 2 deaths. $L=1$ gives $2\times3=6$ people and $1\times3=3$ deaths. Total 10 people, 5 deaths, risk $0.5$.
- Ratio $0.65/0.5=1.3$, the same as standardization. Both pseudo-groups have 10 people, with 4 in $L=0$ and 6 in $L=1$ in each, so $L$ is independent of $A$ there.

## Concepts
- [[potential-outcomes]] — $Y^a$, the outcome had treatment been $a$; here, it can be thought of as a fixed characteristic of the person existing before treatment is assigned (pp. 13, 15)
- [[fundamental-problem-of-causal-inference]] — only one counterfactual outcome observed per person; the others are "?" in Table 2.1 (p. 13)
- [[assignment-mechanism-ignorability]] — the author's version is exchangeability, $Y^a\perp\!\!\!\perp A$, or conditional exchangeability given $L$; closest canon entry (p. 14, p. 18)
- [[exchangeability-causal]] (new) — $Y^a\perp\!\!\!\perp A$: treated and untreated would have had the same risk under the same treatment. (Our note, not in the text: this is a different notion from de Finetti exchangeability in the canon list.) (p. 14)
- [[full-vs-mean-exchangeability]] (new) — joint independence of all counterfactuals and $A$ vs equality of means $\mathrm E[Y^a\mid A]$; mean exchangeability suffices for $\mathrm E[Y^a]=\mathrm E[Y\mid A=a]$ (p. 15)
- [[marginal-vs-conditional-randomization]] (new) — one coin for all vs coin probability depending on $L$; the latter gives only conditional exchangeability (pp. 17–18)
- [[effect-modification]] (new) — stratum-specific causal effects differ across levels of $L$ (p. 18)
- [[identification]] (new) — a counterfactual quantity expressible via the observed-data distribution (p. 20)
- [[standardization]] (new) — $\sum_l\Pr[Y=1\mid L=l,A=a]\Pr[L=l]$; the population is the standard (p. 20)
- [[ip-weighting]] (new) — weight $W^A=1/f[A\mid L]$ to build a pseudo-population with $L\perp A$ (pp. 22–23)
- [[pseudo-population]] (new) — hypothetical population where each person appears under each treatment (p. 22)
- [[positivity]] (new) — $f[a\mid l]>0$ whenever $\Pr[L=l]\neq0$; guaranteed in conditionally randomized experiments (p. 25)
- [[consistency]] (new) — observed outcome under $A=a$ equals $Y^a$; used in TP 2.1, 2.3 (p. 15)
- [[mcar-mar]] (new) — MCAR/MAR missingness (Rubin) mapped to marginal/conditional randomization (p. 18)
- [[crossover-experiment]] (new) — one person observed under treatments in sequence; individual effect can be identified if conditions i)–iii) hold; the naive two-period argument is generally incorrect unless such strong assumptions hold (p. 16)

## Canonical instances
- [[looking-up-pedestrians]] — coin-flip experiment; 55% vs 1% (p. 13)
- [[heart-transplant-study-ch2]] — Tables 2.1/2.2; risk ratio 1.26 if marginal, 1 after adjusting for $L$ (pp. 17–22)
- [[plague-antibiotics-risk-period]] — risk ratio 0.05 at 1 year, 1 at 100 years (p. 19)
- [[zeus-lightning-crossover]] — crossover experiment with strong conditions (p. 16)

## Bridges (candidates)
- [structural-analogy] MAR (assignment depends only on observed $L$) ↔ bayesian: ignorable missing-data mechanism, so inference can ignore the assignment model — the text defines MAR and links it to conditional randomization (p. 18).
- [structural-analogy] Standardization $\sum_l P(Y\mid L,a)P(L)$ ↔ bayesian: marginalising over a nuisance variable, as in a posterior predictive average — both average a conditional distribution over another variable's distribution.
- [structural-analogy] IP weights $1/f[A\mid L]$ ↔ bayesian/Monte Carlo: importance weights that reweight a sample to a target distribution — the Horvitz–Thompson origin in unequal-probability sampling (p. 22) points the same way.
- [metaphor] Exchangeability of treated and untreated ↔ bayesian: de Finetti exchangeability — same word, different definitions; do not conflate.

## Questions this raises
- If conditional exchangeability cannot be verified from observed data (p. 16), how can an observational study justify assuming it?
- What happens to standardization and IP weighting when positivity fails (flagged for Technical Point 3.1, p. 25)?
- When is the stratum-specific effect more useful than the population-wide effect (p. 18), and how does effect modification enter?
- How does random sampling variability (chapter 10, p. 16) change the "each person represents a billion" idealisation?

## Reading notes
- Source is the online revision of the book dated 2026-08-19, not the 2020 print version. Chapter numbering may differ from older citations.
- Page offset: printed = pdf − 9 (pdf 22 = printed 13). Printed p. 26 contains only the running header.
- Figures 2.1–2.3 are images. I read their numbers (counts, probabilities, weights) from the images and checked them against the text.
- Table 1.1 and Figure 1.1 are in chapter 1 and not in this unit. Claims about them (e.g. 7/13 vs 3/7 on p. 16) are as the authors state them.
- The 0.3/0.6 risks (p. 14) belong to a hypothetical near-infinite randomized study, not to Table 2.1. From the Table 2.1 columns I count 7/13 deaths among treated and 3/7 among untreated.
- The text layer is garbled in several margin notes and equations (e.g. Technical Point 2.3). I checked each against the page image.
