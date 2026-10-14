---
id: jaynes-2003-probability/ch09-repetitive-p1
work: jaynes-2003-probability
unit: "9 Repetitive experiments: probability and frequency (part 1/2) — sections 9.1–9.9 (up to Eq. 9.77)"
pages: 270–291
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Repetitive experiments: probability and frequency (part 1/2)

## L0 — One line
A robot told only the number $N=m^n$ of possible outcomes (and so, by indifference, giving each probability $1/N$) reproduces the classical frequentist results (independent trials, binomial law, probability = frequency), so Jaynes concludes that frequentist theory is functionally the reasoning of a poorly informed robot, which helps explain why it has trouble with induction.

## L1 — The gist (≤ 120 words)
The chapter asks how probability-as-logic relates to the frequentist view of repeated experiments. Jaynes gives a robot only the number $N$ of possible outcomes of $n$ trials. Its answers make the trials logically independent, give the binomial and multinomial laws as exact combinatorial facts, and show no learning from past results. Counting outcomes leads to the partition function and to multiplicities (numbers of outcomes) $\sim e^{nH}$, so entropy appears, here, from the rules of probability. Knowing only a total $G$ makes the robot's probability for a result equal its frequency $f_j$ (for large $n$). Induction needs prior information linking the trials, and there is no single inductive rule. This helps clarify what frequentist theory can and cannot do.

**Prerequisites:** product and sum rules; principle of indifference; binomial and multinomial coefficients; Stirling's approximation; logarithm inequality $\log x\le x-1$; basic entropy.

## L2 — Key ideas (5–10 bullets)
- In general the number of results $m$ per trial is a working hypothesis in the robot's description, not a known physical fact; it sets up the sample space $S^n$ with $N=m^n$ outcomes (p. 272).
- With only $I_0$ (the count $N$), the robot assigns equal probability to every outcome; learning any trial results leaves the predictions for the others unchanged, so there is no induction (pp. 274–276).
- Induction (expecting a past regularity to continue) depends on prior information linking the trials, and this information varies widely, so Jaynes concludes there is no general inductive rule. Carnap's λ-continuum (a one-parameter family of induction rules) is identical to Laplace's rules (pp. 277–279).
- The partition function $Z(\lambda)=\sum_j e^{-\lambda g_j}$ generates multiplicities $M(n,G)$ (numbers of outcomes giving total $G$): $\sum_G e^{-\lambda G}M(n,G)=Z^n(\lambda)$. For success/failure counting this gives the exact binomial distribution on $I_0$ (pp. 281–284).
- Frequentist theory (independent trials, limit theorems, sampling distributions) coincides functionally with $I_0$ reasoning; for the robot independence is logical, not causal (pp. 284–285).
- For large $n$, if the frequencies tend to constants, $M(n,A)\sim e^{nH}$, where $H=-\sum f_j\log f_j$ is the entropy of the frequency distribution, maximised over the constraint region. Entropy and, at least in this case, the maximum-entropy principle arise from the rules of probability (pp. 286–287).
- Knowing only the total $G$ gives $p(r_i=j\,|\,G n I_0)=f_j$ (for large $n$, with $f_j$ the maximum-entropy frequencies): probability equals frequency without extra postulates (pp. 288–289).
- Gibbs' inequality (a bound from $\log x\le x-1$) gives $H\le\log m$; choosing $u_j=e^{-\lambda g_j}/Z(\lambda)$ then bounds $H$ on the constraint region, with equality iff $f_j=u_j$ (p. 291).

## L3 — Walkthrough

### Introduction (p. 270)
Most of conventional theory has confined attention to experiments repeatable indefinitely under what appear to be identical conditions yet give different results. Virtually all application-oriented expositions define probability as limiting frequency; the mathematically oriented often define it as an abstract additive measure but, in applications, tend to think in terms of frequency (p. 270). Jaynes says frequentist-solvable problems form a subclass of those solvable by probability-as-logic, and this chapter tries to say what subclass (p. 270). Failures of frequentist methods are postponed to Chapter 17 (p. 270).

### 9.1 Physical experiments (pp. 271–273)
- Any repetitive experiment obeys physical law, and competent inference must use what is known of it; generally, this knowledge will determine the "model" (p. 271).
- Factors that are the same at each trial are **systematic**. Factors that vary uncontrollably are better called **irreproducible by the technique used** than "random" (p. 271). Footnote 1: "random" is often taken to mean undetermined individual results plus a physically real "propensity" fixing long-run frequencies, which Jaynes calls self-contradictory (p. 271).
- Setup: $n$ trials, $m$ results per trial. The usual statement "$N=m^n$ conceivable outcomes" is ambiguous: is it physical fact or the robot's information? (p. 272)
- Jaynes's answer: $m$ always describes the state of knowledge, and may not match the real number of possibilities. It is "the number of results per trial that we shall take into account in the present calculation", i.e. a tentative working hypothesis (p. 272). Exercise 9.1 (Darwin, Galapagos: $n=122$ specimens, $m=19$ species; probability of unseen species?) illustrates when $m$ is unknown (p. 272).
- Two sample spaces: $S$ for one trial ($m$ points) and the extension space
$$S^n=S\otimes S\otimes\cdots\otimes S \tag{9.1}$$
A single trial has a **result**; the whole experiment has an **outcome** (p. 272).
- An outcome is a data set $D=\{r_1,\dots,r_n\}$, $1\le r_i\le m$. The most general assignment is
$$P(D|I)=p(r_1\ldots r_n)\tag{9.2}$$
$$\sum_{r_1=1}^m\cdots\sum_{r_n=1}^m p(r_1\ldots r_n)=1\tag{9.3}$$
(p. 273).
- **Base-$m$ trick:** treat the $r_i$ as digits of a base-$m$ number $R$, $0\le R\le N-1$, so the robot never learns it is describing repeated trials (p. 273). Example: four die tosses, $m=6$, $N=6^4=1296$. Outcome 836 satisfies
$$836=(3\times6^3)+(5\times6^2)+(1\times6^1)+(2\times6^0)\tag{9.4}$$
so the robot displays 3512, meaning tosses gave 3, 5, 1, 2. Digits count only modulo 6, so a displayed digit 0 stands for six spots (the text writes $5024\equiv5624$) (p. 273).

### 9.2 The poorly informed robot (pp. 274–276)
- **Information $I_0$:** the robot knows only the number $N$ of possible outcomes, not even that there are $n$ repetitions (p. 274).
- **Interlocutor's objection:** crucial information has been withheld. Jaynes agrees, but wants to see the consequences of neglecting it (p. 274).
- By indifference every outcome gets $1/N$. A proposition $A$ true on a subset has probability
$$P(A|I_0)=\frac{M(n,A)}{N}\tag{9.5}$$
where $M(n,A)$ is its multiplicity (number of outcomes where $A$ is true). So probability–frequency connections appear automatically as mathematical consequences (p. 274).
- For $n$ die tosses: $p(r_1\ldots r_n|I_0)=6^{-n}$ (9.6). Summing the $6^{n-1}$ mutually exclusive cases gives
$$P(r_1=3|I_0)=6^{n-1}p(r_1\ldots r_n|I_0)=1/6$$
(9.8), and by symmetry $P(r_i=k|I_0)=1/6$ (9.9). Likewise $P(r_1=k,r_2=j|I_0)=1/36$ (9.10) and, for any three tosses, $1/216$ (9.11) (p. 275).
- **Educating the robot.** Product rule: $p(r_2|r_1I_0)=p(r_1r_2|I_0)/p(r_1|I_0)$ (9.12), giving $\frac{1/36}{1/6}=1/6=p(r_2|I_0)$ (9.13), and $p(r_3|r_1r_2I_0)=\frac{1/216}{1/36}=1/6=p(r_3|I_0)$ (9.14). Telling it the results of any number of tosses does not change its predictions for the rest (p. 276).

*Intuition note:* On $I_0$ each toss is logically independent of every other. The robot gets nothing from the past because nothing tells it the digits are the same experiment repeated.

### 9.3 Induction (pp. 276–277)
- People "take the hint": after a dozen 3s, we bet on 3. Seeing a pattern and expecting it to continue is **induction** (not "mathematical induction", which is deductive). Our intuition gives only a qualitative direction, and the robot must be quantitative (p. 276).
- Hume found justifying induction hard. **Popper's** rhetorical question ("Are we rationally justified in reasoning from repeated instances … to instances of which we have no experience?") is "quite literally, the poorly informed robot speaking" (Jaynes's view). Jaynes wants to show that a better-informed robot will answer "Yes, if we have prior information providing a logical connection between the different trials" (pp. 276–277).
- The same problem arises in survey sampling (672 of 1000 favour A; why infer about the millions unsurveyed?), in physics (672 of 1000 atoms excited; the other $10^{23}$?), and in medicine (672 of 1000 recoveries; future patients?). On $I_0$ there is no justification for such inferences (p. 277).

### 9.4 Are there general inductive rules? (pp. 277–280)
- (9.13)–(9.14) show that, on $I_0$, results of different tosses are logically independent propositions. The robot can be educated out of this state only by information relevant to all tosses; for example, something, however slight, about some property, physical or logical, common to all trials (p. 277).
- Introspection shows there is no single hidden piece of information; our induction varies with prior knowledge (p. 277).
- **Coin example** (data $D=H_1H_2H_3$, asking $P(H_4|DI)$) (pp. 277–278):
  - $I_0$: $1/2$ whatever the data.
  - $I_1$ (coin examined, symmetric, nothing odd in tossing): the symmetry evidence will probably outweigh three tosses, so $1/2$ again.
  - $I_2$ (coin not examined, dubious honesty): the data are some evidence of systematic influence, so $P>1/2$. This is real induction. No numerical value is possible until $I_2$ is specified more clearly.
  - $I_3$ (two-headed or two-tailed coin, unknown which): $P=1$.
- **Paradox:** $I_1$ carries more information than $I_2$ yet agrees with the poorly informed robot. More knowledge does not necessarily mean disagreement (p. 278).
- **Reverse induction:** the hypergeometric distribution of Chapter 3 lowers the probability of red as more red balls are drawn. It disappears in the binomial limit (p. 278). Coin case $I_4$ (hidden mechanism forces exactly 50 heads and 50 tails in the next 100 tosses) is like an urn with 50 red and 50 white balls:
$$P(H_4|DI_4)=\frac{h(4|100,50,4)}{h(3|100,50,3)}=\frac{0.05873}{0.12121}=0.4845<\tfrac12\tag{9.15}$$
Directly: $(M-3)/(N-3)=47/97=0.4845$ (p. 279).
- Conclusion: no universal inductive rule, and a classification of all rules by parameters seems dubious (p. 279).
- **Carnap** (1952) found a one-parameter continuum of rules $\lambda\in(0,\infty)$. Jaynes says these are identical to Laplace's (rule of succession and generalisations), and that Johnson (1932), de Finetti (1937) and Jeffreys (1939) had better analyses. Jaynes's critique: Carnap never used the concept of prior information, which is the primary fact controlling induction (p. 279). Footnote 2 defers the claimed inconsistency of Laplace's rule to Chapter 18 (p. 279).
- Verdict: frequentist theory ignores prior information, and for that reason cannot account for induction (p. 280).

### 9.5 Multiplicity factors (pp. 280–281)
- Numbers are large: $6^{12}=2.18\times10^9$ (9.16); $6^{30}=2.21\times10^{23}$; the text compares these with minutes since the Great Pyramid and microseconds in the age of the universe, and mentions a famous 20 000-toss die experiment (p. 280). Exact counting involves number-theoretic details, but large-number approximations are easy (p. 280).
- Let $g_1,\dots,g_m$ be additive "gains" of each result. Total gain
$$G=\sum_{i=1}^n g(r_i)=\sum_{j=1}^m n_jg_j\tag{9.17}$$
with sample number $n_j$ = times result $j$ occurred (p. 280). Then
$$p(G|n,I_0)=f(G|n,I_0)=\frac{M(n,G)}{N},\quad N=m^n\tag{9.18}$$
where $M(n,G)$ is the number of outcomes yielding $G$ (p. 281).

### 9.6 Partition function algorithms (pp. 281–285)
- Conditioning on the $n$th trial:
$$M(n,G)=\sum_{j=1}^mM(n-1,G-g_j)\tag{9.19}$$
a linear difference equation with constant coefficients, so it has solutions
$$\exp\{\alpha n+\lambda G\}\tag{9.20}$$
Substituting into (9.19) gives (added step: $e^{\alpha n+\lambda G}=\sum_j e^{\alpha(n-1)+\lambda(G-g_j)}$, divide by $e^{\alpha(n-1)+\lambda G}$):
$$\exp\{\alpha\}=Z(\lambda)\equiv\sum_{j=1}^m\exp\{-\lambda g_j\}\tag{9.21}$$
$Z$ is the **partition function** (p. 281). A superposition $H(n,G)=\int d\lambda\,Z^n(\lambda)e^{\lambda G}h(\lambda)$ (9.22) is a formal solution. The true $M$ also satisfies $M(0,G)=\delta(G,0)$ and exists only for discrete $G$ (p. 281).
- Discrete Laplace transform: multiply by $e^{-\lambda G}$ and sum over $G$. Each outcome contributes once, so group by sample numbers:
$$\sum_G e^{-\lambda G}M(n,G)=\sum_{n_j\in U}W(n_1,\dots,n_m)\exp\Big\{-\lambda\sum n_jg_j\Big\}\tag{9.23}$$
$$W(n_1,\dots,n_m)\equiv\frac{n!}{n_1!\cdots n_m!}\tag{9.24}$$
(outcomes with given $\{n_j\}$). Multinomial expansion:
$$(x_1+\dots+x_m)^n=\sum_{n_j\in U}W\,x_1^{n_1}\cdots x_m^{n_m}\tag{9.25}$$
with $U:\ n_j\ge0,\ \sum n_j=n$ (9.26). With $x_j=e^{-g_j}$ (so $x_j^{n_j}=e^{-n_jg_j}$) comparison gives
$$\sum_Ge^{-\lambda G}M(n,G)=Z^n(\lambda)\tag{9.27}$$
$M(n,G)$ is the coefficient of $e^{-\lambda G}$ in $Z^n$: $Z^n$ shows how all outcomes are partitioned among values of $G$ (p. 282).

*Intuition note:* Raising $Z$ to the $n$th power does the counting for all $n$ trials at once. Each term in the expansion records one value of $G$ and how many outcomes give it.

**9.6.1 Solution by inspection (pp. 282–284).**
- Choose $g_j=\delta(j,1)$ (9.28), so $G=n_1$ (9.29), and $Z(\lambda)=e^{-\lambda}+m-1$ (9.30). By Newton's binomial theorem
$$Z^n=\sum_{s=0}^n\binom ns e^{-\lambda s}(m-1)^{n-s}\tag{9.31}$$
$$M(n,n_1)=\binom n{n_1}(m-1)^{n-n_1}\tag{9.32}$$
(p. 283). Direct counting gives the same, but the partition method also works for harder problems (p. 283).
- General split: $S'$ has $s$ "success" results, $\overline{S'}$ has $m-s$ ("failure"), the text writing $1<s<m$. Set $g_j=1$ for $j\in S'$, else 0 (9.33); $G=\sum n_jg_j\equiv r$ (9.34); $Z=s\,e^{-\lambda}+m-s$ (9.35);
$$Z^n=\sum_{r=0}^n\binom nr s^re^{-\lambda r}(m-s)^{n-r}\tag{9.36}$$
$$M(n,r)=\binom nr s^r(m-s)^{n-r}\tag{9.37}$$
and from (9.18), with $p=s/m$,
$$P(G=r|I_0)=\binom nr p^r(1-p)^{n-r},\quad 0\le r\le n\tag{9.38}$$
(p. 283).
- This is the **binomial distribution**, exact for a finite sample space. In Chapter 3 it was only a limit (infinite urn) or a randomised approximation (p. 284). It arises in the inference of a robot that lacks even the concept of repetition, so it has an exact combinatorial basis independent of "repetitive sampling" (p. 284). Bernoulli's classical derivation postulates equal, independent probabilities at each trial. The robot says the same out of complete ignorance (p. 284). The multinomial also follows (Exercise 9.2), and the usual sampling distributions follow as limiting forms (p. 284).
- **Jaynes's conclusion:** frequentist theory is "functionally, just the reasoning of the poorly informed robot", and since that robot cannot do inductive reasoning, we begin to understand why conventional theory has trouble with induction (p. 284). Its limit theorems depend entirely on strict independence; the slightest positive correlation makes them qualitatively wrong, and most sampling distributions of estimators would be incorrect (pp. 284–285). Conventional theory takes independence to mean causal physical independence; Jaynes has seen no discussion in the orthodox literature of how to judge this. For the robot it means logical independence, a stronger condition (p. 285).

### 9.7 Entropy algorithms (pp. 285–289)
- For a proposition $A(n_1,\dots,n_m)$ true on region $R\subset U$ (equal to $G$ if linear in the $n_j$):
$$M(n,A)=\sum_{n_j\in R}W(n_1,\dots,n_m)\tag{9.39}$$
- Number of terms (Bose–Einstein multiplicity, footnote 3):
$$T(n,m)=\binom{n+m-1}{n}=\frac{(n+m-1)!}{n!(m-1)!}\tag{9.40}$$
$$T(n,m)\sim\frac{n^{m-1}}{(m-1)!}\quad(n\to\infty)\tag{9.41}$$
(pp. 285–286).
- With $W_{\max}\equiv\max_R W$ (9.42), the sum is at least $W_{\max}$ and has at most $T$ terms:
$$W_{\max}\le M(n,A)\le W_{\max}T(n,m)\tag{9.43}$$
$$\tfrac1n\log W_{\max}\le\tfrac1n\log M(n,A)\le\tfrac1n\log W_{\max}+\tfrac1n\log T\tag{9.44}$$
Since $\tfrac1n\log T\to0$ (9.45),
$$\tfrac1n\log M(n,A)\to\tfrac1n\log W_{\max}\tag{9.46}$$
The single largest term dominates (p. 286).
- Hold frequencies $f_j=n_j/n$ fixed (9.47) and use Stirling:
$$\log n!\sim n\log n-n+\log\sqrt{2\pi n}+O(1/n)\tag{9.48}$$
$$\tfrac1n\log W\to H\equiv-\sum_{j=1}^mf_j\log f_j\tag{9.49}$$
the entropy of the frequency distribution. Hence
$$M(n,A)\sim\exp\{nH\}\tag{9.50}$$
meaning the ratio tends to 1, not the difference. The $f_j$ in $H$ are those maximising $H$ over $R$ (p. 286). So multiplicity is found by maximum entropy subject to the constraints defining $R$. Footnote 4: entropy is inherent in probability theory independently of Shannon, and in this case the maximum-entropy principle follows from the rules of probability without extra assumptions (p. 287).
- For linear $A=G$: $M(n,G)=\exp\{nH\}$ asymptotically (9.51), so
$$p(G|n,I_0)=m^{-n}\exp\{nH\}=\exp\{-n(H_0-H)\}\tag{9.52}$$
with $H_0=\log m$ the absolute maximum (derived in 9.74). $H_0-H$ measures how strong the constraints are (p. 287).

*Intuition note:* Among all frequency patterns allowed by the constraint, the one of maximum entropy dominates the count of outcomes. For large $n$ only that pattern matters, and counting reduces to maximising entropy on the single-trial space.

- **Effect of learning one trial's result.** Told that a specified trial gave $g_j$: the remaining $n-1$ trials must give $G-g_j$, with multiplicity $M(n-1,G-g_j)$ (p. 287). New frequencies:
$$f'_k=\frac{n_k-\delta_{jk}}{n-1}\tag{9.53}$$
$$\delta f_k=\frac{f_k-\delta_{jk}}{n-1}\tag{9.54}$$
(exact; $\sum f'_k=1$, $\sum\delta f_k=0$).
$$\delta H=\sum_k\frac{\partial H}{\partial f_k}\delta f_k+O(1/n^2)=\frac{H+\log f_j}{n-1}+O(1/n^2)\tag{9.55}$$
(added step: $\partial H/\partial f_k=-\log f_k-1$, and $\sum_kf_k=1$.) Hence
$$H'=\frac{nH+\log f_j}{n-1}+O(1/n^2)\tag{9.56}$$
$$M(n-1,G-g_j)=\exp\{(n-1)H'\}=f_j\exp\{nH\}[1+O(1/n)]\tag{9.57}$$
(pp. 287–288). The set $S^n$ has disappeared. What remains is to maximise $H$ on the single-trial space $S$ (p. 288).
- Bayes' theorem on $G$:
$$p(G|r_i{=}j,nI_0)=\frac{M(n-1,G-g_j)}{m^{n-1}}\tag{9.58}$$
$$p(r_i{=}j|nI_0)=1/m\tag{9.59}$$
$$p(r_i{=}j|GnI_0)=p(r_i{=}j|nI_0)\frac{p(G|r_i{=}j,nI_0)}{p(G|nI_0)}\tag{9.60}$$
$$=\frac1m\frac{M(n-1,G-g_j)/m^{n-1}}{M(n,G)/m^n}=\frac{M(n-1,G-g_j)}{M(n,G)}=f_j\tag{9.61}$$
(p. 288). Knowing $G$ moves the robot's probability for result $j$ from $1/m$ to the observed frequency $f_j$. This is not paradoxical because $G$ fixes the maximum-entropy frequency distribution (p. 288). Frequentism postulates this link; the robot derives it (p. 289). Exercise 9.3 asks for the joint probability (9.62) and whether $G$ induces correlations (p. 288).

### 9.8 Another way of looking at it (pp. 289–290)
- A number-theoretic trick, "useless in practice" (Jaynes). $M(n,G)=\sum_{\{n_j\}}W$ over non-negative integers with $\sum n_j=n$, $\sum n_jg_j=G$ (9.63–9.64). For two such sets, $\sum_jk_jg_j=0$ with $k_j=n_j-n'_j$ not all zero (9.65) (p. 289).
- Numbers $g_j$ are **jointly incommensurable** if none is a rational-coefficient linear combination of the others. Then all $k_j=0$ (9.66): $G$ determines every $n_j$, so the sum has one term, $M(n,G)=W(n_1,\dots,n_m)$ (9.67) and $M(n-1,G-g_j)=W(n'_1,\dots,n'_m)$ (9.68), with $n'_i=n_i-\delta_{ij}$ (pp. 289–290).
- Then (9.61) reduces to
$$p(r_k=j|GnI_0)=\frac{W(n')}{W(n)}=\frac{(n-1)!}{n!}\frac{n_j!}{(n_j-1)!}=\frac{n_j}{n}\tag{9.69}$$
equivalently Bernoulli's rule $P(r_k=j|n_jI_0)=n_j/(\text{total number of digits})$ (9.70) (p. 290). Probability equals the frequency with which a proposition is true in the set of equally possible hypotheses (p. 290).
- No "law of physics" is needed to explain why measured frequency approximates assigned probability (to relative accuracy "something like $1/\sqrt n$"). If the assigned probability includes all systematic effects, the great majority of possible outcomes have frequencies in a shrinking interval. This is a combinatorial theorem essentially due to de Moivre and Laplace. For Jaynes, the strong probability–frequency connection is only a special case (p. 290).

### 9.9 Entropy maximization (pp. 290–291, ends at Eq. 9.77)
- For linear $G$ the region $R$ is fixed by the average
$$\overline G=G/n=\sum_{j}f_jg_j\tag{9.71}$$
and the maximisation was solved by Gibbs (1902). Jaynes says Gibbs' algorithm was rejected for 75 years by those who saw probability as a physical phenomenon, and became understandable through Shannon (1948) and Jaynes (1957a). The full apparatus is deferred to Chapter 11 (pp. 290–291).
- **Gibbs inequality.** For frequency distributions $\{f_j\}$, $\{u_j\}$ (non-negative, summing to 1), use $\log x\le x-1$ (equality iff $x=1$):
$$\sum_jf_j\log(u_j/f_j)\le0\tag{9.72}$$
with equality iff $f_j=u_j$ for all $j$. Hence
$$H(f_1,\dots,f_m)\le-\sum_jf_j\log u_j\tag{9.73}$$
- Choose $u_j=1/m$:
$$H\le\log m\tag{9.74}$$
maximum attained iff $f_j=1/m$ for all $j$ (p. 291).
- Choose
$$u_j=\frac{\exp\{-\lambda g_j\}}{Z(\lambda)}\tag{9.75}$$
with $\lambda$ set so that $\sum u_jg_j=\overline G$. The printed Eq. (9.76) is $H\le\sum f_jg_j+\log Z(\lambda)$ (see Reading notes on the missing $\lambda$). For all $f_j$ with average (9.71) the right-hand side is constant, so $H$ attains
$$H_{\max}=\overline G+\log Z\tag{9.77}$$
on $R$ (p. 291). The text continues beyond Eq. (9.77) in part 2.

*Intuition note:* Weighting results by $e^{-\lambda g_j}$ makes Gibbs' inequality an equality exactly at the maximum-entropy distribution. The maximum value of $H$ is then $\overline G+\log Z$ (as printed; see Reading notes).

## Toy example (ours)
Coin, $m=2$, $n=3$, $g_1=1$ (heads), $g_2=0$. So $G=r$ = number of heads, and $N=2^3=8$.
- $Z(\lambda)=e^{-\lambda}+1$. $Z^3=e^{-3\lambda}+3e^{-2\lambda}+3e^{-\lambda}+1$, so $M(3,r)=1,3,3,1$ for $r=3,2,1,0$. These sum to $8=N$.
- $P(G=2|I_0)=3/8$. This matches (9.38): $\binom32(1/2)^2(1/2)=3\cdot\tfrac18$.
- Independence on $I_0$: $p(r_1{=}H)=4/8=1/2$ and $p(r_1{=}H,r_2{=}H)=2/8=1/4$, so $p(r_2{=}H|r_1{=}H)=\tfrac{1/4}{1/2}=1/2$. The first toss tells the robot nothing.
- Now tell it $G=2$. Then $p(r_1{=}H|G=2)=M(2,1)/M(3,2)$ with $M(2,1)=\binom21=2$, giving $2/3=f_H=n_H/n$. Check: the three outcomes HHT, HTH, THH have heads first in 2 of 3. Knowing only the total changed $1/2$ into the frequency $2/3$, as in (9.61) and (9.69).

## Concepts
- [[principle-of-indifference-maximum-entropy]] — equal probability to $N$ outcomes when nothing else is known; used for the robot on $I_0$ (p. 274)
- [[multiplicity-factor]] (new) — $M(n,A)$, the number of outcomes in $S^n$ on which $A$ is true; $P(A|I_0)=M/N$ (p. 274)
- [[poorly-informed-robot]] (new) — reasoning on $I_0$, knowing only $N$; functionally the same as frequentist reasoning, with logical independence of trials (pp. 274, 284)
- [[induction]] (new) — expecting past regularities to continue; quantitatively requires prior information linking trials; no general rule (pp. 276–279)
- [[extension-space]] (new) — $S^n$, the direct product of $n$ single-trial spaces (p. 272)
- [[partition-function]] (new) — $Z(\lambda)=\sum_je^{-\lambda g_j}$; $Z^n$ is the generating function for multiplicities (p. 281)
- [[entropy]] (maps to entropy H(X)) — here the entropy of the frequency distribution, $-\sum f_j\log f_j$, as the growth rate of multiplicity (p. 286)
- [[maximum-entropy-principle]] — multiplicity found by maximising $H$ over the constraint region; derived from probability rules, at least in this case (p. 287, footnote 4)
- [[exponential-family]] — form $u_j=e^{-\lambda g_j}/Z(\lambda)$ of the comparison distribution; the bound (9.76)–(9.77) is attained iff $f_j=u_j$ (p. 291)
- [[frequentist-vs-bayesian]] — Jaynes: frequentist theory is functionally $I_0$ reasoning and ignores prior information (pp. 280, 284)
- [[relative-entropy-kl]] — Gibbs inequality (9.72) is the non-negativity of KL divergence (canon link; not stated in this unit) (p. 291)

## Canonical instances
- [[base-m-die-encoding]] — four die tosses encoded as a base-6 number (836 → 3512) (p. 273)
- [[coin-three-heads-priors]] — $I_0$–$I_4$ give different $P(H_4|DI)$ from the same data (pp. 277–279)
- [[poll-672-of-1000]] — surveys, atoms, cancer patients as the induction problem (p. 277)
- [[darwin-galapagos-species]] — unknown-$m$ problem (Exercise 9.1) (p. 272)
- [[urn-50-50-reverse-induction]] — coin forced to 50/50: $47/97=0.4845$ (p. 279)

## Bridges (candidates)
- [same-math] Multiplicity $M\sim e^{nH}$ ↔ information-theory: number of sequences of a given type is $\approx 2^{nH}$ (method of types / typical set) — same counting by Stirling, in natural logs.
- [same-math] Partition function $Z(\lambda)$ and $u_j\propto e^{-\lambda g_j}$ ↔ statistical mechanics / exponential families: Gibbs distribution with normaliser $Z$.
- [same-math] Gibbs inequality (9.72) ↔ information-theory: non-negativity of KL divergence.
- [structural-analogy] Robot on $I_0$ (independent trials) ↔ bayesian: i.i.d. sampling versus exchangeability, where past trials inform future ones (canon link; not stated in this unit).
- [metaphor] "Different prior information, different inductive rules" ↔ bayesian: priors as the source of learning.

## Questions this raises
- Which kinds of prior information linking trials let the robot learn from past results, and what rules do they give?
- How exactly does knowledge of $G$ induce (or not) correlations between trials (Ex. 9.3)?
- Where does the "about $1/\sqrt n$" accuracy of frequency–probability agreement come from, quantitatively?
- What goes wrong when frequentist methods are applied where trials are not logically independent (Chapter 17)?

## Exercises worth doing
- Ex. 9.1 (p. 272) — unknown number of species: build a hypothesis space from judgment about the real world — difficulty: hard
- Ex. 9.2 (p. 284) — derive the multinomial distribution as a generalisation of (9.38) — difficulty: medium
- Ex. 9.3 (p. 288) — joint probability as a ratio of multiplicities; do correlations arise? — difficulty: medium

## Reading notes
- This is part 1 of Chapter 9: it starts at the chapter opening (printed p. 270) and ends mid-§9.9 at Eq. (9.77) (p. 291). The unit note says the split is at a section boundary, but the pages given end after Eq. (9.77) with the sentence continuing, i.e. inside §9.9.
- Page offset: printed = pdf − 30.
- Printed misprint(?): in (9.76) and (9.77) the images show $H\le\sum f_jg_j+\log Z(\lambda)$ and $H_{\max}=\overline G+\log Z$, with no factor $\lambda$. Substituting (9.75) into (9.73) gives (added step) $-\sum f_j\log u_j=\lambda\sum f_jg_j+\log Z$. I give the text as printed.
- §9.8 begins "From (9.28) and (9.29)", but the sums (9.63)–(9.64) follow from (9.23)–(9.26); the cross-reference looks loose. Also, on p. 282 the text sets $x_j^{n_j}=\exp\{-n_jg_j\}$ without $\lambda$; to match (9.23) one needs $x_j=e^{-\lambda g_j}$, which gives (9.27).
- Short quotes (each ≤ 25 words) are in quotation marks; everything else is paraphrased.
