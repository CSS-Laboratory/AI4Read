---
id: jaynes-2003-probability/ch11-discrete
work: jaynes-2003-probability
unit: "11 Discrete prior probabilities: the entropy principle"
pages: 343-371
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Discrete prior probabilities: the entropy principle

## L0 — One line
Jaynes argues that when the prior information is a set of average values, the "most honest" probability assignment is the one that maximizes the entropy $H=-\sum p_i\log p_i$ subject to those averages, and this has the exponential form $p_i \propto \exp(-\sum_j\lambda_j f_j(x_i))$, where the $f_j$ are the quantities whose averages are given and the $\lambda_j$ are constants fitted to them.

## L1 — The gist (≤ 120 words)
The robot so far has only the principle of indifference for assigning probabilities. What should it do when its prior information is a set of average values? Jaynes tries other "spread-out" measures, then derives entropy in two ways: Shannon's functional-equation argument and Wallis's random-quanta counting game. The maximum-entropy solution has an exponential form, and many predictions follow by differentiating $\log Z$, the log of the normalizing sum $Z$ (the partition function). This reproduces the formal structure of Gibbs's statistical mechanics. Jaynes then answers four objections. He argues that the principle is a rule for inductive reasoning, not an oracle. Maximum-entropy distributions are also the frequency distributions realizable in overwhelmingly the most ways, given the constraints.

**Prerequisites:** sums and logs; Lagrange multipliers; partial derivatives; expectation (mean) of a function; multinomial coefficient and Stirling's formula; variance, covariance; basic probability (Ch. 2 and Ch. 9 ideas).

## L2 — Key ideas (5–10 bullets)
- Averages give the robot a reason to prefer some possibilities over others, so indifference alone cannot be used, and nothing earlier in the theory answers the question. The robot needs a rule that uses the averages but commits to nothing more (pp. 343–345).
- Maximum variance and minimum $\sum p_i^2$ fail. Maximum variance puts all probability on extreme values. Minimum $\sum p_i^2$ gives negative probabilities for some averages (pp. 345–346).
- Shannon's theorem: if an uncertainty measure is continuous, increases with the number of equally likely options, and obeys the composition law (the value computed in one step must equal the value computed in stages), it must be $-\sum p_i\log p_i$ (pp. 347–350).
- Wallis's derivation gives the same entropy by counting how many ways random probability "quanta" can realize an allocation, with no talk of "amount of uncertainty" (pp. 351–353).
- Maximizing $H$ under expectation constraints (the given averages $\langle f_j\rangle=F_j$) gives $p_i=\exp(-\lambda_0-\sum_j\lambda_jf_j(x_i))$, with Lagrange multipliers $\lambda_j$ fitted to the constraints. A lemma proves that this distribution is the global maximum (pp. 355–358).
- Derivatives of $\log Z$ give many predictions: reciprocity laws (symmetric second derivatives), covariances, derivatives with respect to parameters in the $f_j$, and a variational law for $S$ (the maximum entropy as a function of the given averages). Jaynes says virtually all known thermodynamic relations appear as special cases (pp. 358–365).
- Frequency link: the maximum-entropy distribution can be realized in overwhelmingly more ways than any other that meets the constraints. Jaynes's weaker frequency statement is conditional on the information including all constraints actually operating (pp. 366–370).
- Redundant information drops out, contradictory information makes the equations unsolvable, and persistent disagreement with experiment points to a missing constraint. Jaynes says Gibbs's apparent "failures" gave the first clues pointing to quantum theory (pp. 369–371).

## L3 — Walkthrough

### Opening (p. 343)
The robot can currently translate information into probabilities only by indifference (2.95). Often prior information does not change the set of possibilities but gives a reason to prefer some of them. Jaynes says orthodoxy ignores prior information about fixed parameters and treats sampling probabilities as known frequencies. He claims that in about 40 years he never saw a real problem with prior information about sampling frequencies. In practice, sampling probabilities come from a standard model that starts from indifference (p. 343). This chapter and Ch. 12 add two new principles for assigning initial probabilities (p. 343).

### 11.1 A new kind of prior information (pp. 343–345)
Three examples, each with information only in the form of an average (p. 344):
- **Windows:** the average window broke into $\bar m = 9.76$ pieces. What is $P(m \text{ pieces})$?
- **Dice:** black dice with white spots photographed on a black table, with multiple exposure. The average number of spots is 4.5 instead of 3.5. What frequencies, or probability for the next toss, should be assigned (given exchangeability, Ch. 3)?
- **Cars on a ferry:** $N=1000$ cars, length $L=3$ miles, weight $W$ from the ferry's draught. Only $L/N$ and $W/N$ are known. What proportion of each make was present?

Treating $N, L, W$ as nuisance parameters with Bayes' theorem only moves the problem to assigning priors for them (p. 344). Estimating a frequency distribution and assigning a probability distribution are almost the same mathematically for an exchangeable sequence (p. 344).

Desiderata: use all the information, but do not jump to unwarranted conclusions. The distribution should be as uniform as possible while agreeing with the information. It must not give zero probability to anything the information does not rule out (p. 345). This is a variational problem: constraints fix some properties, and "honesty" resolves the rest (p. 345). The method is trial and error with candidate measures of spread (p. 345).

**Maximum variance fails.** For the windows, one can raise the variance without bound while keeping the mean at 9.76, by putting a huge probability on no breakage and a tiny one on billions of pieces. For the dice, the maximum-variance solution uses only faces 1 and 6, with $p_1+6p_6=4.5$, giving $p_1=0.3$, $p_6=0.7$. This rules out faces 2–5 without justification (p. 345).

### 11.2 Minimum $\sum p_i^2$ (pp. 345–346)
Minimize $\sum_m p_m^2$ subject to $\sum_m p_m=1$ and $\sum_m m\,p_m=\bar m$ (11.1):
$$\delta\Big[\sum_m p_m^2-\lambda\sum_m m p_m-\mu\sum_m p_m\Big]=\sum_m(2p_m-\lambda m-\mu)\,\delta p_m=0 \tag{11.2}$$
So $p_m$ is linear in $m$. The multipliers are fixed by (11.3) $\sum_m p_m=1$ and (11.4) $\sum_m m p_m=\bar m$. For $m\in\{1,2,3\}$:
$$p_1=\tfrac43-\tfrac{\bar m}{2},\quad p_2=\tfrac13,\quad p_3=\tfrac{\bar m}{2}-\tfrac23. \tag{11.5}$$
Here $p_1<0$ when $\bar m>8/3$ and $p_3<0$ when $\bar m<4/3$. Patching by setting negatives to zero would use different principles in different ranges of $\bar m$. It would also assign zero probability to cases the information does not exclude. Jaynes calls this unacceptable, though better than maximum variance. He examines it because some writers rejected the entropy solution and proposed minimum $\sum p_i^2$ on intuitive grounds, without checking its results (p. 346).

### 11.3 Entropy: Shannon's theorem (pp. 346–351)
The conditions on a measure $H_n(p_1,\dots,p_n)$ of "amount of uncertainty" (p. 347):
1. A numerical measure exists.
2. $H_n$ is continuous in the $p_i$.
3. For equal probabilities, $h(n)=H_n(1/n,\dots,1/n)$ (11.6) is monotonic increasing in $n$.
4. Consistency: if there are several ways to compute the value, they must agree.

Consistency takes the form of a hierarchy of functional equations. Suppose two alternatives have probabilities $p_1$ and $q=1-p_1$, and the second splits into two with probabilities $p_2,p_3$, $p_2+p_3=q$. Then
$$H_3(p_1,p_2,p_3)=H_2(p_1,q)+q\,H_2\!\Big(\tfrac{p_2}{q},\tfrac{p_3}{q}\Big). \tag{11.7}$$
Jaynes notes this also says $H_n$ is additive, so it is really an extra assumption that should have been listed (p. 347). **Exercise 11.1** asks whether a single monotonic function could relate the $H_n$ for different $n$ (p. 348).

*General composition law.* Group $A_1..A_k$ into a composite proposition with probability $w_1=p_1+\dots+p_k$, the next $m$ into $w_2$, and so on. Consistency requires
$$H(p_1,\dots,p_n)=H(w_1,\dots,w_r)+w_1H\!\Big(\tfrac{p_1}{w_1},\dots,\tfrac{p_k}{w_1}\Big)+w_2H\!\Big(\tfrac{p_{k+1}}{w_2},\dots,\tfrac{p_{k+m}}{w_2}\Big)+\cdots \tag{11.8}$$
Example:
$$H\big(\tfrac12,\tfrac13,\tfrac16\big)=H\big(\tfrac12,\tfrac12\big)+\tfrac12H\big(\tfrac23,\tfrac13\big). \tag{11.9}$$
(p. 348)

*Reduction to $h(n)$.* By continuity it suffices to treat rational $p_i=n_i/\sum n_i$ (11.10), with integers $n_i$. Choosing one of $\sum n_i$ equally likely alternatives can be done in two steps: first pick group $i$, then pick among its $n_i$ members (11.11). For $n_1=3,n_2=4,n_3=2$:
$$h(9)=H\big(\tfrac39,\tfrac49,\tfrac29\big)+\tfrac39h(3)+\tfrac49h(4)+\tfrac29h(2). \tag{11.12}$$
In general
$$h\Big(\sum n_i\Big)=H(p_1,\dots,p_n)+\sum_i p_i\,h(n_i). \tag{11.13}$$
With all $n_i=m$ ($n$ groups) we have $p_i=1/n$, so $H=h(n)$ (added step), and
$$h(mn)=h(m)+h(n). \tag{11.14}$$
This is solved by $h(n)=K\log n$ (11.15). For continuous $m,n$ this is the only solution (differentiate in $m$, set $m=1$, use $h(1)=0$). But (11.14) is required only for integers, which makes uniqueness a number-theory question. Every integer factors uniquely into primes, so $h(q_i)$ for the primes $q_i$ can be chosen arbitrarily. Then (11.14) is "just sufficient" to determine $h(N)$. So (11.15) is not the only solution of (11.14) (p. 349).

*Uniqueness using monotonicity.* By induction, $h(nmr\cdots)=h(n)+h(m)+h(r)+\cdots$ (11.16), hence $h(n^k)=k\,h(n)$ (11.17). For integers $t,s\ge2$ and arbitrarily large $n$, choose $m$ with
$$\frac mn\le\frac{\log t}{\log s}<\frac{m+1}{n},\ \text{ i.e. }\ s^m\le t^n<s^{m+1}. \tag{11.18}$$
Monotonicity and (11.17) give $m\,h(s)\le n\,h(t)\le(m+1)h(s)$ (11.19), so
$$\frac mn\le\frac{h(t)}{h(s)}\le\frac{m+1}n. \tag{11.20}$$
Comparing (11.18) and (11.20):
$$\Big|\frac{h(t)}{h(s)}-\frac{\log t}{\log s}\Big|\le\frac1n,\ \text{ or }\ \Big|\frac{h(t)}{\log t}-\frac{h(s)}{\log s}\Big|\le\epsilon,\quad \epsilon\equiv\frac{h(s)}{n\log t}. \tag{11.21, 11.22}$$
Since $\epsilon$ is arbitrarily small, $h(t)/\log t$ is a constant (p. 350). Different $K$ correspond to different logarithm bases, so take $h(n)=\log n$. Substituting into (11.13) gives $H=\log\sum n_i-\sum_i p_i\log n_i=-\sum_i p_i\log p_i$ (added step). This is **Shannon's theorem**: the only function satisfying the stated conditions is
$$H(p_1,\dots,p_n)=-\sum_{i=1}^n p_i\log p_i. \tag{11.23}$$
Accepting this interpretation, the distribution maximizing it under the constraints is, in Jaynes's words, the "most honest" description of what the robot knows. The log base only multiplies $H$ by a constant and does not change the maximizing $p_i$ (p. 350).

**Intuition note.** The requirement is that uncertainty computed in one step or in stages must agree. Together with continuity and "more options, more uncertainty", this leaves one formula, up to the choice of log base.

*Logic of what is proved.* Jaynes says (11.23) is shown to be a *necessary* condition for consistency. In accordance with Gödel's theorem, he says, one cannot prove that it actually is consistent unless one moves out into some as yet unknown region beyond that used in the proof. He conjectured, in an argument leaning heavily on Shannon, that any other information measure leads to inconsistencies if carried far enough. Shore and Johnson (1980) later gave an independent direct proof. Years of use have revealed no inconsistency (pp. 350–351).

*Terminology warning.* $H$ is the "information entropy", a property of any probability distribution. The thermodynamic "experimental entropy" is a property of a thermodynamic state and makes no reference to a probability distribution. Jaynes calls the shared name unfortunate. He says confusing the two is the field's "major occupational disease" and ruins many texts with "nonsense theorems". A relation between the two appears later (p. 351, with footnote 2).

**Exercise 11.2** (p. 351): any change that equalizes two probabilities increases $H$; $H$ is global, not local.

Jaynes says (11.7) "does not seem quite so intuitively compelling" as the earlier functional equations; he thinks the trouble is probably that he has not yet learned how to verbalize the argument convincingly, and he notes that other arguments, such as Shore and Johnson's, lead uniquely to the same (11.23) (p. 351).

### 11.4 The Wallis derivation (pp. 351–354)
Information $I$ is to be used to assign $\{p_1..p_m\}$ with $\sum p_i=1$ (11.24). Only $I$ and the rules of probability may be used (p. 352). Take $n\gg m$ quanta of probability, each of size $\delta=1/n$. Scatter them at random into $m$ equal boxes, so no box is favored. If box $i$ gets $n_i$ quanta, the assignment is $p_i=n_i\delta=n_i/n$ (11.25). Its probability is multinomial:
$$m^{-n}\,\frac{n!}{n_1!\cdots n_m!}. \tag{11.26}$$
Repeat the game, accepting only allocations consistent with $I$. The most likely accepted allocation maximizes
$$W=\frac{n!}{n_1!\cdots n_m!}\tag{11.27}$$
subject to $I$. With Stirling (as printed),
$$\log n!=n\log n-n+\sqrt{2\pi n}+\frac1{12n}+O(1/n^2), \tag{11.28}$$
and $n_i=np_i$, $n\to\infty$, $n_i/n\to p_i$:
$$\tfrac1n\log W\to-\sum_i p_i\log p_i=H(p_1..p_m). \tag{11.29}$$
So the most likely allocation is the maximum-entropy one (p. 353). To answer the objection that stopping at the first acceptable result is unfair, Jaynes states without proof (left as an exercise) that, for large $n$, the overwhelming majority of acceptable allocations are arbitrarily close to the maximum-entropy distribution. Footnote 3 refers to a later "entropy concentration theorem" (p. 353).

Jaynes sees these advantages of Wallis's derivation: it is independent of (11.8). It needs no postulate linking probability and frequency. It does not assume the possibilities come from a repeatable experiment. It yields "maximize $H$" directly, without interpreting $H$ as "amount of uncertainty". Anyone who accepts the game as fair is led to the principle (p. 353).

He warns against reading too much philosophical significance into theorems that lead to (11.23). He says Shannon himself played the theorem down, since the inequalities $H$ satisfies already justify its use. If one does accept $H$ literally as the uncertainty measure, Jaynes says the principle of indifference and many frequency connections become special cases of one method (pp. 353–354).

### 11.5 An example (pp. 354–355)
Values $m\in\{1,2,3\}$ with given $\bar m$. Lagrange conditions:
$$\delta\Big[H-\lambda\sum_{m=1}^3 m p_m-\mu\sum_{m=1}^3 p_m\Big]=\sum_{m=1}^3\Big[\frac{\partial H}{\partial p_m}-\lambda m-\mu\Big]\delta p_m=0, \tag{11.30}$$
with $\partial H/\partial p_m=-\log p_m-1$ (11.31). Hence
$$p_m=\exp\{-\lambda_0-\lambda m\},\quad \lambda_0\equiv\mu+1. \tag{11.32}$$
Define the partition function $Z(\lambda)\equiv\sum_{m=1}^3 e^{-\lambda m}$ (11.33). The constraints become
$$\lambda_0=\log Z(\lambda),\qquad \bar m=-\frac{\partial\log Z}{\partial\lambda}. \tag{11.34, 11.35}$$
In parametric form:
$$p_k=\frac{e^{-k\lambda}}{e^{-\lambda}+e^{-2\lambda}+e^{-3\lambda}}=\frac{e^{(3-k)\lambda}}{e^{2\lambda}+e^{\lambda}+1},\quad k=1,2,3;\qquad \bar m=\frac{e^{2\lambda}+2e^{\lambda}+3}{e^{2\lambda}+e^{\lambda}+1}. \tag{11.36, 11.37}$$
Eliminating $\lambda$ gives
$$p_1=\frac{3-\bar m-p_2}{2},\quad p_2=\frac13\Big[\sqrt{4-3(\bar m-2)^2}-1\Big],\quad p_3=\frac{\bar m-1-p_2}{2}. \tag{11.38}$$
$p_2$ is an arc of an ellipse; $p_1,p_3$ are slanted elliptic arcs (p. 355). The solution has $p_k\ge0$ automatically, because of the logarithmic singularity at zero. Probabilities reach zero only at $\bar m=1$ or $3$, where deduction forces it. Jaynes credits David Blackwell with stressing this property (p. 355, footnote 4).

### 11.6 Generalization: a more rigorous proof (pp. 355–358)
Setup: $x$ takes values $(x_1..x_n)$ with propositions $(A_1..A_n)$. There are $m<n$ functions $f_k(x)$ with given expectations
$$\langle f_k(x)\rangle=F_k=\sum_{i=1}^n p_if_k(x_i),\quad 1\le k\le m. \tag{11.39–11.41}$$
Variational solution with multipliers $(\lambda_0-1)$ and $\lambda_j$ (11.42) gives
$$p_i=\exp\Big\{-\lambda_0-\sum_{j=1}^m\lambda_jf_j(x_i)\Big\}. \tag{11.43}$$
Normalization (11.44) and the partition function
$$Z(\lambda_1..\lambda_m)\equiv\sum_{i=1}^n\exp\Big\{-\sum_{j}\lambda_jf_j(x_i)\Big\} \tag{11.45}$$
give
$$\lambda_0=\log Z, \tag{11.46}$$
$$F_k=e^{-\lambda_0}\sum_if_k(x_i)\exp\Big\{-\sum_j\lambda_jf_j(x_i)\Big\}\ \ (11.47)\ \Longleftrightarrow\ F_k=-\frac{\partial\log Z}{\partial\lambda_k}. \tag{11.48}$$
The maximum entropy is
$$H_{\max}=\Big[-\sum_ip_i\log p_i\Big]_{\max}=\lambda_0+\sum_{j=1}^m\lambda_jF_j \tag{11.49, 11.50}$$
(p. 356).

*Why a second proof.* Variational methods find rounded maxima but may miss a higher maximum at a cusp, so a "grain of doubt" remains (p. 357). The second proof needs a lemma. Let $p_i$ and $u_i$ both be probability distributions (11.51, 11.52). Since $\log x\le x-1$ for $0\le x<\infty$, with equality iff $x=1$ (11.53),
$$\sum_ip_i\log\frac{u_i}{p_i}\le\sum_ip_i\Big(\frac{u_i}{p_i}-1\Big)=0, \tag{11.54}$$
so
$$H(p_1..p_n)\le\sum_ip_i\log\frac1{u_i},\ \text{ with equality iff } p_i=u_i\ \forall i. \tag{11.55}$$
Now "pull out of the hat"
$$u_i\equiv\frac1{Z(\lambda_1..\lambda_m)}\exp\Big\{-\sum_j\lambda_jf_j(x_i)\Big\}. \tag{11.56}$$
Then $\log(1/u_i)=\log Z+\sum_j\lambda_jf_j(x_i)$, so
$$H\le\sum_ip_i\Big[\log Z+\sum_j\lambda_jf_j(x_i)\Big]\ (11.57)\ =\ \log Z+\sum_j\lambda_j\langle f_j(x)\rangle. \tag{11.58}$$
Over all $p_i$ satisfying the constraints (11.41), the right side is constant. By the lemma, $H$ reaches its absolute maximum, making (11.58) an equality, iff the $p_i$ equal the canonical distribution (11.56). (Added step: here the $\lambda_j$ are those fitted to the constraints via (11.60), which Jaynes leaves implicit.) This proof is strong where the variational one is weak, but weak where it is strong, because the answer had to be known first. Together they give "the whole story" (p. 358).

**Intuition note.** Among all distributions with the same constraint values, the exponential-form distribution whose $\lambda_j$ are fitted to those values has the largest entropy, and any other such distribution has strictly less. The lemma works because the constraint values pin down the right-hand side of (11.58).

### 11.7 Formal properties of maximum entropy distributions (pp. 358–365)
Jaynes chooses to list the formal relations first, with physical meanings to come later (p. 358).

*Entropy as a function of the data.*
$$H_{\max}=S(F_1..F_m)=\log Z(\lambda_1..\lambda_m)+\sum_k\lambda_kF_k. \tag{11.59}$$
$S$ is "objective": it depends only on the given data, not on anybody's personality or wishes (p. 358). The $\lambda$'s are fixed by
$$F_k=\langle f_k\rangle=-\frac{\partial\log Z}{\partial\lambda_k},\quad k=1..m, \tag{11.60}$$
which is $m$ nonlinear equations. These are usually left in parametric form (p. 359).

*Derivative of $S$.* Differentiating (11.59):
$$\frac{\partial S}{\partial F_k}=\sum_j\frac{\partial\log Z}{\partial\lambda_j}\frac{\partial\lambda_j}{\partial F_k}+\sum_j\frac{\partial\lambda_j}{\partial F_k}F_k+\lambda_k. \tag{11.61}$$
The first two terms cancel by (11.60) (the second sum should carry index $F_j$, as in the cancellation; see Reading notes), leaving
$$\lambda_k=\frac{\partial S(F_1..F_m)}{\partial F_k}. \tag{11.62}$$
$\log Z$ and $S$ each carry the full information, and (11.59) is a Legendre transformation between them (p. 359).

*Reciprocity laws.* Differentiating (11.60) in $\lambda_j$ (symmetric cross-derivatives), as printed (the printed form has no minus sign; see Reading notes):
$$\frac{\partial F_k}{\partial\lambda_j}=\frac{\partial^2\log Z}{\partial\lambda_j\partial\lambda_k}=\frac{\partial F_j}{\partial\lambda_k}. \tag{11.63}$$
Differentiating (11.62):
$$\frac{\partial\lambda_k}{\partial F_j}=\frac{\partial^2S}{\partial F_j\partial F_k}=\frac{\partial\lambda_j}{\partial F_k}. \tag{11.64}$$
These are not independent: the matrices $A_{jk}=\partial\lambda_j/\partial F_k$ and $B_{jk}=\partial F_j/\partial\lambda_k$ are inverses (p. 359).

*Parameter $\alpha$ inside $f_k$.* Examples: $\alpha$ the volume (energy levels depend on it) or the magnetic field (pp. 359–360). The best estimate of $\partial f_k/\partial\alpha$ by minimum mean-square error is its mean over the canonical distribution:
$$\Big\langle\frac{\partial f_k}{\partial\alpha}\Big\rangle=\frac1Z\sum_i\exp\{-\lambda_1f_1(x_i)-\dots-\lambda_kf_k(x_i;\alpha)-\dots-\lambda_mf_m(x_i)\}\frac{\partial f_k(x_i,\alpha)}{\partial\alpha}\tag{11.65}$$
$$=-\frac1{\lambda_k}\frac{\partial\log Z(\lambda_1..\lambda_m;\alpha)}{\partial\alpha}. \tag{11.66}$$
If $\alpha$ appears in several $f_k$:
$$\sum_{k=1}^m\lambda_k\Big\langle\frac{\partial f_k}{\partial\alpha}\Big\rangle=-\frac{\partial\log Z}{\partial\alpha}, \tag{11.67}$$
which includes the equation of state of any thermodynamic system. Also
$$\frac{\partial S(F_1..F_k;\alpha)}{\partial\alpha}=-\sum_k\lambda_k\Big\langle\frac{\partial f_k}{\partial\alpha}\Big\rangle=\frac{\partial\log Z}{\partial\alpha}. \tag{11.68}$$
On the left the $F_k$ are held fixed; on the right the $\lambda_k$ are held fixed. Equality follows from the Legendre transformation. If several parameters $\{\alpha_1..\alpha_r\}$ are present, a relation of the form (11.68) holds for each of them (p. 360).

*Fluctuation laws.* $F_k$ and $\langle f_k\rangle$ are the same number; the angle-bracket notation stresses the canonical-distribution mean, so (11.63) reads (as printed)
$$\frac{\partial\langle f_k\rangle}{\partial\lambda_j}=\frac{\partial\langle f_j\rangle}{\partial\lambda_k}=\frac{\partial^2\log Z}{\partial\lambda_j\partial\lambda_k}. \tag{11.69}$$
Varying $\lambda$ compares two slightly different maximum-entropy problems (p. 361). Within a single problem, the covariance is
$$\langle(f_j-\langle f_j\rangle)(f_k-\langle f_k\rangle)\rangle=\langle f_jf_k\rangle-\langle f_j\rangle\langle f_k\rangle, \tag{11.70}$$
which for $j=k$ is the variance $\langle f_k^2\rangle-\langle f_k\rangle^2\ge0$ (11.71). From the canonical distribution,
$$\langle f_jf_k\rangle=\frac1Z\sum_if_jf_k\,e^{-\sum\lambda f}=\frac1Z\frac{\partial^2Z}{\partial\lambda_j\partial\lambda_k}. \tag{11.72}$$
Using (11.60),
$$\langle f_jf_k\rangle-\langle f_j\rangle\langle f_k\rangle=\frac1Z\frac{\partial^2Z}{\partial\lambda_j\partial\lambda_k}-\frac1{Z^2}\frac{\partial Z}{\partial\lambda_j}\frac{\partial Z}{\partial\lambda_k}=\frac{\partial^2\log Z}{\partial\lambda_j\partial\lambda_k}, \tag{11.73}$$
$$\text{so}\quad\langle f_jf_k\rangle-\langle f_j\rangle\langle f_k\rangle=-\frac{\partial\langle f_j\rangle}{\partial\lambda_k}=-\frac{\partial\langle f_k\rangle}{\partial\lambda_j}. \tag{11.74}$$
For any function $q(x)$:
$$\langle qf_k\rangle-\langle q\rangle\langle f_k\rangle=-\frac{\partial\langle q\rangle}{\partial\lambda_k}. \tag{11.75}$$
(p. 361–362). **Exercise 11.3** asks whether higher derivatives of $\log Z$ give third and fourth central moments (hint: cumulants, Appendix C) (p. 362).

*Moments.* Define $\Phi(\beta_1..\beta_m)\equiv\langle\exp\{\sum_j\beta_jf_j\}\rangle$ (11.76). Then $\langle f_i^{m_i}f_j^{m_j}\cdots\rangle=\big(\partial^{m_i}_{\beta_i}\partial^{m_j}_{\beta_j}\cdots\Phi\big)\big|_{\beta=0}$ (11.77). Also $\Phi=Z(\lambda_1-\beta_1,\dots,\lambda_m-\beta_m)/Z(\lambda_1..\lambda_m)$ (11.78). So $Z$ itself serves as the generating function:
$$\langle f_i^{m_i}f_j^{m_j}\cdots\rangle=\frac1Z\Big(\frac{\partial^{m_i}}{\partial\lambda_i^{m_i}}\frac{\partial^{m_j}}{\partial\lambda_j^{m_j}}\cdots\Big)Z. \tag{11.79}$$
(p. 362).

*Derivatives with respect to $\alpha$.* Define $g_k\equiv\partial f_k/\partial\alpha$ (11.80); if $f_k$ is energy and $\alpha$ is volume, $-g_k$ is pressure. The text gives (as printed; see Reading notes on its second equality)
$$\frac{\partial\langle g_j\rangle}{\partial\lambda_k}=-\big[\langle g_jf_k\rangle-\langle g_j\rangle\langle g_k\rangle\big]=\frac{\partial\langle g_k\rangle}{\partial\lambda_j}, \tag{11.81}$$
$$\sum_{j=1}^m\lambda_j\big[\langle g_jg_k\rangle-\langle g_j\rangle\langle g_k\rangle\big]=\Big\langle\frac{\partial g_k}{\partial\alpha}\Big\rangle-\frac{\partial\langle g_k\rangle}{\partial\alpha}, \tag{11.82}$$
$$\frac{\partial^2\log Z}{\partial\alpha^2}=\sum_{jk}\lambda_j\lambda_k\big[\langle g_jg_k\rangle-\langle g_j\rangle\langle g_k\rangle\big]-\sum_k\lambda_k\Big\langle\frac{\partial g_k}{\partial\alpha}\Big\rangle, \tag{11.83}$$
$$\frac{\partial^2\log Z}{\partial\alpha\,\partial\lambda_k}=-\frac{\partial\langle f_k\rangle}{\partial\alpha}=\sum_j\lambda_j\big[\langle f_kg_j\rangle-\langle f_k\rangle\langle g_j\rangle\big]-\langle g_k\rangle. \tag{11.84}$$
With two parameters $\alpha_1,\alpha_2$ (as printed; see Reading notes):
$$\frac{\partial^2\log Z}{\partial\alpha_1\partial\alpha_2}=\sum_k\lambda_k\Big\langle\frac{\partial^2f_k}{\partial\alpha_1\partial\alpha_2}\Big\rangle-\sum_{kj}\lambda_j\lambda_k\Big[\Big\langle\frac{\partial f_k}{\partial\alpha_1}\frac{\partial f_j}{\partial\alpha_2}\Big\rangle-\Big\langle\frac{\partial f_k}{\partial\alpha_1}\Big\rangle\Big\langle\frac{\partial f_j}{\partial\alpha_2}\Big\rangle\Big]. \tag{11.85}$$
Jaynes says these theorems have, as special cases, Einstein's fluctuation laws for black-body radiation and for the density of a gas or liquid, and Nyquist noise. An infinite hierarchy of such moment relations follows by further differentiation. The relations between $\log Z$ and $S$ mean they can all also be stated as derivatives (variational properties) of $S$ (p. 363).

*General variational law for $S$.* Now let the functions themselves change: $\delta f_k(x_i)$ and $\delta\langle f_k\rangle$ are specified independently. Then
$$\delta\log Z=\frac1Z\sum_i\Big[\sum_k\big(-\lambda_k\delta f_k(x_i)-\delta\lambda_kf_k(x_i)\big)\Big]e^{-\sum_j\lambda_jf_j(x_i)}=-\sum_k\big[\lambda_k\langle\delta f_k\rangle+\delta\lambda_k\langle f_k\rangle\big]. \tag{11.86}$$
Applying $\delta$ to (11.59) gives (added step; the sign is mine, see Reading notes)
$$\delta S=\sum_k\lambda_k\big[\delta\langle f_k\rangle-\langle\delta f_k\rangle\big]=\sum_k\lambda_k\,\delta Q_k,\qquad \delta Q_k\equiv\delta\langle f_k\rangle-\langle\delta f_k\rangle=\sum_if_k(x_i)\,\delta p_i. \tag{11.87, 11.88}$$
So $S$ is stationary under small variations of the $f_k(x_i)$ when the $p_i$ are held fixed. Taking $\delta f_k(x_i,\alpha_j)=\sum_j\frac{\partial f_k}{\partial\alpha_j}\delta\alpha_j$ (11.89), $\delta Q_k$ is not in general an exact differential. But $\lambda_k$ is an integrating factor such that $\sum\lambda_k\delta Q_k$ is the exact differential of a state function $S$, as in thermodynamics. Jaynes leaves it to the reader to prove from (11.87) that
$$\sum_{k=1}^m\langle f_k\rangle\frac{\partial\lambda_k}{\partial\alpha}=0 \tag{11.90}$$
with the $\langle f\rangle$ held constant (p. 364).

**Intuition note.** The robot computes $\log Z$ once. Means, variances, covariances and responses to parameter changes then come out as derivatives of $\log Z$. Jaynes says these are Gibbs's statistical-mechanics equations "with all the physics removed", and that virtually all known thermodynamic relations are special cases (p. 364–365). He concludes that the thermodynamic relations are independent of particular physical assumptions and are properties of extended logic in general (p. 365).

*Other uses (p. 365).* Gibbs's statistical mechanics is the oldest and most used application. Ch. 14 gives an inventory-control problem and Ch. 22 an optimal-encoding problem. Uniform priors are maximum entropy. A Gaussian sampling distribution is maximum entropy for given first and second moments (Ch. 7). A binomial sampling distribution is mathematically equivalent to the uniform maximum-entropy distribution on a deeper hypothesis space (Ch. 9).

### 11.8 Conceptual problems – frequency correspondence (pp. 365–370)
The objections (p. 365–366):
- **(A)** If the only justification for the canonical distribution is "maximum uncertainty", that is a negative thing which cannot possibly lead to useful predictions; reliable results cannot come out of mere ignorance.
- **(B)** Maximum-entropy probabilities have nothing to do with frequencies, so there is no reason for observed distributions to agree with them.
- **(C)** The principle is restricted to constraints that are averages, but almost always the given data are not averages over anything; they are definite measured numbers. Setting $F_k=\langle f_k\rangle$ is a logical contradiction, since the resulting distribution gives nonzero probability to $f_k\ne F_k$.
- **(D)** Different people have different information and so get different distributions, so results are basically arbitrary.

**Jaynes replies to (A)** that it is a play on words. Maximizing entropy does not create uncertainty; it measures the uncertainty already present. Using a distribution that implies more knowledge than we have is what would lead to unreliable conclusions. The information put in as constraints may be so meager that no reliable predictions can be made; in that case the theory tells us so, since a very broad distribution for a quantity $\theta$ is the robot's way of saying "You haven't given me enough information". If the distribution is very sharp (his example: odds greater than $10^{10}:1$ that $\theta$ is within $\theta_0(1\pm10^{-6})$), the information sufficed for a definite prediction. Omitting additional cogent information is a misuse of the method, not a failure of it (p. 366).

**Reply to (B).** The principle fundamentally has nothing to do with a repeatable random experiment. Some applications, such as the ferry cars, are single situations. If the $x_i$ come from repeated trials, as in the dice, the relation to frequencies can be analysed mathematically. Jaynes says he will demonstrate three results: (1) a precise connection exists; (2) it is usually unnecessary for the method's usefulness; (3) the principle is most useful when observed frequencies disagree with the maximum-entropy probabilities (p. 366).

*The frequency argument.* Take $N$ trials with $n$ possible results each, so $n^N$ conceivable outcomes. Result $x_i$ occurs $n_i$ times:
$$\sum_{i=1}^nn_i=N, \tag{11.91}$$
and if the given means $F_k$ are observed,
$$\sum_{i=1}^nn_if_k(x_i)=NF_k,\quad k=1..m. \tag{11.92}$$
If $m<n-1$, these do not determine $f_i=n_i/N$. The number of outcomes giving the counts $\{n_i\}$ is
$$W=\frac{N!}{n_1!\cdots n_n!}=\frac{N!}{(Nf_1)!\cdots(Nf_n)!}. \tag{11.93}$$
Maximizing $N^{-1}\log W$ (monotonic in $W$), by (11.29):
$$\tfrac1N\log W\to-\sum_if_i\log f_i=H_f. \tag{11.94}$$
This is exactly the maximum-entropy problem, so the solutions coincide. Jaynes adds that it is reminiscent of the Wallis derivation, and that direct Bayes with a uniform prior over the $n^N$ outcomes, taking $N\to\infty$, gives the same result. This identity holds for any kind of constraint, not only means (p. 367–368).

*Sharpness.* For another admissible frequency set with entropy $H_{f'}<H_f$,
$$\frac W{W'}\to\exp\{N(H_f-H_{f'})\}, \tag{11.95}$$
which grows without bound. So the maximum-entropy frequency distribution can be realized in overwhelmingly more ways than any other satisfying the same constraints. Jaynes says this connection is a mathematical consequence of probability as extended logic, not part of its definition. A different connection appears in Ch. 12 (p. 368).

**Reply to (C).** The purpose of constraints is to incorporate information. A distribution "contains" information if it can be extracted by the usual rule for expectations. Usually the datum is of unknown accuracy, and using it only to fix $\langle f_k\rangle$ is, Jaynes says, just being honest. If independent information about its accuracy is available, a constraint on $\langle f_1(x_i)^2\rangle$ can be added. This seldom makes a substantive difference, because the variance of the maximum-entropy distribution is usually small compared with any reasonable experimental error (p. 368).

**Reply to (D).** Jaynes says the frequency connection does not justify predicting, in the sense of deductive proof, that the maximum-entropy distribution will be observed, since different people may have different information. Consider Mr A with constraints on $\langle f_1\rangle,\langle f_2\rangle$ and the better-informed Mr B with an extra constraint on $\langle f_3\rangle$. Then
$$S_B\le S_A. \tag{11.96}$$
- **Redundant extra information** (Mr B's datum is what Mr A would predict). Mr A's distribution also solves Mr B's problem, with $\lambda_3=0$, and equality holds in (11.96) in this case and only in this case. So two people with different information do not necessarily arrive at different distributions; they do so only when B's information is "surprising" to A. Redundant information is not counted twice, which agrees with $AA=A$ in Boolean algebra (p. 369).
- **Contradictory extra information** (e.g. $f_3=f_1+2f_2$ but $F_3\ne F_1+2F_2$). Then $Z(\lambda_1,\lambda_2,\lambda_3)=\sum_i\exp\{-(\lambda_1+\lambda_3)f_1(x_i)-(\lambda_2+2\lambda_3)f_2(x_i)\}$ (11.98), so $\partial Z/\partial\lambda_3=\partial Z/\partial\lambda_1+2\,\partial Z/\partial\lambda_2$ (11.99). Equations (11.97), $F_k=-\partial\log Z/\partial\lambda_k$, then have no real solution unless $F_3=F_1+2F_2$. The principle "breaks down, as it should", refusing to give any distribution (pp. 369–370).
- **Neither redundant nor contradictory.** The distributions differ and the inequality in (11.96) is strict. Then asymptotically
$$\frac{W_A}{W_B}\sim\exp\{N(S_A-S_B)\}, \tag{11.100}$$
so for large $N$ even a slight entropy decrease means an enormous decrease in the number of possibilities (p. 370).

*Weaker frequency statement.* If the information used includes all the constraints actually operating in the experiment, the maximum-entropy distribution is overwhelmingly the most likely to be observed. Jaynes adds that most frequency distributions observed in Nature are maximum-entropy ones, because they can be realized in so many more ways. If the disagreement persists indefinitely on repetition, then, since by hypothesis the data were true if incomplete, Jaynes concludes that the mechanism must contain a constraint not included, and the deviations are a clue to it (p. 370). Summary: the principle is a rule for inductive reasoning that tells which predictions "are most strongly indicated by our present information", not an oracle (p. 370).

**Intuition note.** Counting arrangements explains the frequency link: the maximum-entropy frequencies can occur in far more ways than any alternative. The link is conditional on having included every real constraint, and a persistent failure points to a missing one.

### 11.9 Comments (pp. 370–371)
Jaynes says the Mr A scenario is an accurate model of what happened to Gibbs. By 1901 it was known that Gibbs's canonical ensemble (his maximum-entropy distribution over classical phase space, given a mean energy) failed to predict some thermodynamic properties, such as heat capacities and the equation of state. Analysis of the data showed that the entropy of a real physical system was always less than the value predicted. The conclusion was that microscopic laws contain an additional constraint. Gibbs died in 1903. Planck (radiation), Einstein and Debye (solids) and Bohr (atoms) found the constraint: discrete energy levels. Heisenberg and Schrödinger developed the theory by 1927. Jaynes says the first clues for quantum theory came from a seemingly "unsuccessful" application of maximum entropy, hence the remark that the principle is most useful where it fails to predict the facts (p. 371). Gibbs (1902) wrote his phase-space density as
$$w(q_1..q_n;p_1..p_n)=\exp\eta(q_1..q_n), \tag{11.101}$$
the "index of probability of phase". He derived the canonical and grand canonical ensembles by choosing the distribution that gives the least average of $\eta$ under constraints. Jaynes says this is maximizing entropy. Gibbs left no clear explanation of why this function is to be maximized, so his procedure appeared arbitrary to many, and for 60 years there was confusion and controversy. Shannon (1948) opened the way to new thinking (p. 371).

## Toy example (ours)
Values $m\in\{1,2,3\}$, as in §11.5, with $\bar m=11/7$.

1. Guess $e^{\lambda}=2$. Then $Z=e^{-\lambda}+e^{-2\lambda}+e^{-3\lambda}=\tfrac12+\tfrac14+\tfrac18=\tfrac78$.
2. $p_m=e^{-\lambda m}/Z$: $p_1=\tfrac12/\tfrac78=\tfrac47$, $p_2=\tfrac14/\tfrac78=\tfrac27$, $p_3=\tfrac18/\tfrac78=\tfrac17$. The sum is 1.
3. Check (11.35): $\bar m=\dfrac{\tfrac12+2\cdot\tfrac14+3\cdot\tfrac18}{7/8}=\dfrac{11/8}{7/8}=\dfrac{11}{7}$. ✓. This agrees with (11.37): $(4+4+3)/(4+2+1)=11/7$.
4. Check (11.38): $p_2=\tfrac13\big[\sqrt{4-3(\tfrac{11}7-2)^2}-1\big]=\tfrac13\big[\sqrt{4-\tfrac{27}{49}}-1\big]=\tfrac13\big[\tfrac{13}7-1\big]=\tfrac27$ ✓. $p_1=\tfrac{3-11/7-2/7}2=\tfrac47$ ✓.
5. Entropy (natural log): by (11.50), $H_{\max}=\ln\tfrac78+\tfrac{11}7\ln2=-0.1335+1.0892=0.9557$. Direct: $-[\tfrac47\ln\tfrac47+\tfrac27\ln\tfrac27+\tfrac17\ln\tfrac17]=0.3198+0.3579+0.2780=0.9557$ ✓.
6. Compare the minimum-$\sum p^2$ solution (11.5): $p=(\tfrac{23}{42},\tfrac{14}{42},\tfrac5{42})$. Its mean is $(23+28+15)/42=11/7$, so it meets the same constraint. Its entropy is $0.3298+0.3662+0.2534=0.9493<0.9557$, as the lemma requires. It is valid here, but it would have gone negative for $\bar m>8/3$.

## Concepts
- [[maximum-entropy-principle]] — among distributions meeting the stated averages, pick the one maximizing $H$; the "most honest" assignment (p. 350)
- [[entropy]] — $H=-\sum p_i\log p_i$, here called information entropy, derived from the Shannon conditions (p. 350)
- [[exponential-family-gibbs]] — maximum-entropy solution under expectation constraints is $p_i=\exp(-\lambda_0-\sum\lambda_jf_j(x_i))$ (p. 356)
- [[principle-of-indifference-maxent]] — uniform assignment is a special case of maximum entropy; a Gaussian sampling distribution is maximum entropy for given first and second moments, and a binomial one is equivalent to a uniform maximum-entropy assignment on a deeper hypothesis space (p. 365)
- [[shannon-composition-law]] (new) — consistency requirement (11.7)/(11.8) that uncertainty is additive across stagewise choices (p. 347)
- [[wallis-derivation]] (new) — maximum entropy from counting random probability allocations, $\tfrac1n\log W\to H$ (p. 352–353)
- [[partition-function]] (new) — $Z(\lambda)=\sum_i\exp\{-\sum\lambda_jf_j(x_i)\}$; $\log Z$ generates means, covariances and responses by differentiation (p. 354, 356)
- [[legendre-duality-logZ-S]] (new) — $S=\log Z+\sum\lambda_kF_k$ links $\log Z(\lambda)$ and $S(F)$; $\lambda_k=\partial S/\partial F_k$ (p. 358–359)
- [[maxent-reciprocity-fluctuation-laws]] (new) — symmetry of second derivatives of $\log Z$ and covariance $=\partial^2\log Z/\partial\lambda_j\partial\lambda_k$ (p. 359–361)
- [[entropy-concentration]] (new) — sharpness of the maximum in $W$: $W/W'\to e^{N(H_f-H_{f'})}$ (11.95) (p. 368); the formal "entropy concentration theorem" is referred to as coming later (p. 353, footnote 3)
- [[information-vs-thermodynamic-entropy]] (new) — information entropy is a property of a distribution; thermodynamic entropy of a state; must not be conflated (p. 351)

## Canonical instances
- [[broken-windows-average]] — only the average number of pieces, 9.76, is known (p. 344)
- [[biased-die-mean-4.5]] — the die with average 4.5 spots; maximum variance would use only faces 1 and 6 (p. 344–345)
- [[cars-on-ferry]] — only average length and weight known; shows a non-frequency use (p. 344, 366)
- [[three-value-maxent-example]] — $m\in\{1,2,3\}$, solutions (11.36)–(11.38) vs minimum $\sum p^2$ (p. 346, 354–355)
- [[mr-a-mr-b-information]] — redundant, contradictory and useful extra constraints (p. 369–370)
- [[gibbs-quantum-clue]] — a failed maximum-entropy prediction pointed to discrete energy levels (p. 370–371)

## Bridges (candidates)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality
- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities
- [structural-analogy] Wallis counting, $\tfrac1n\log W\to H$ and (11.95) ↔ information-theory: typical set / AEP — counting sequences by their empirical distribution
- [structural-analogy] Mr A / Mr B: a persistent mismatch reveals a missing constraint ↔ Bayesian workflow: posterior predictive checks revealing misfit
- [metaphor] Redundant information "drops out" (p. 369) ↔ bayesian: sequential updating with data that add nothing

## Questions this raises
- Shannon's proof needs the composition law (11.7), which Jaynes says does not seem as compelling as the earlier functional equations. Could the Shore–Johnson or Wallis route replace it without loss?
- The "honest" assignment is justified here for constraints on averages. How should the principle be applied when the constraint set is not of the form $\langle f_k\rangle=F_k$, though (11.91–11.95) show the counting argument does not need mean-value form?
- What does the robot do when the maximum-entropy equations have no solution, other than refuse (p. 370)? How does one find the faulty datum?
- Ch. 12 is said to give a different probability–frequency connection (p. 368). How does it relate to (11.95)?

## Exercises worth doing
- Ex. 11.1 (p. 348) — whether one monotonic function can generalize the consistency equation across all $n$ — difficulty: hard
- Ex. 11.2 (p. 351) — equalizing two probabilities raises $H$ by an amount proportional to $\epsilon$; entropy is global, not local — difficulty: easy
- Ex. 11.3 (p. 362) — third and fourth central moments from derivatives of $\log Z$ (cumulants) — difficulty: medium
- Reader task (p. 353) — prove that most acceptable allocations in the Wallis game lie near the maximum-entropy distribution — difficulty: hard
- Reader task (p. 364) — prove (11.90) from (11.87) — difficulty: medium

## Reading notes
- Printed page = pdf page − 30 (pdf 373 = printed 343). The text layer garbles many symbols (sums, $\gg$, brackets); equations here were checked against the page images.
- Misprints seen in the images: p. 348 prose "$H(p_1/w_1,\dots,p_k/w_k)$" should read $w_1$ throughout, as (11.8) has it. (11.92) says "$d=1..m$" where $k$ is meant. (11.47) text says "$f_x(x)$", meaning $f_k$. (11.72) has "$i{-}1$" for $i=1$. Objection (C) writes $\{F_1..F_n\}$ where $m$ is meant. (11.61) prints the second sum with $F_k$ where $F_j$ is needed for the cancellation. (11.90) says $\langle f_1\rangle..\langle f_r\rangle$ held constant, probably meaning $m$. (11.68) writes $S(F_1..F_k;\alpha)$ where $m$ is meant.
- Sign in (11.63) and (11.69): as printed they have no minus sign, but differentiating (11.60), $F_k=-\partial\log Z/\partial\lambda_k$, with respect to $\lambda_j$ gives a minus sign, and (11.74) does carry it. I copied (11.63) and (11.69) as printed.
- Sign in (11.87): the printed first form is $\delta S=-\sum_k\lambda_k[\delta\langle f_k\rangle-\langle\delta f_k\rangle]$. It disagrees with the printed second form $\delta S=\sum\lambda_k\delta Q_k$, with (11.62), and with my derivation from (11.59) and (11.86). I used the $+$ form.
- (11.81): the printed covariance term is $\langle g_j\rangle\langle g_k\rangle$; by (11.75) one would expect $\langle g_j\rangle\langle f_k\rangle$. I could not verify the second equality, since the covariances of $g_j$ with $f_k$ and of $g_k$ with $f_j$ need not be equal. It is copied as printed.
- (11.85): the printed signs are opposite to those obtained by setting $\alpha_1=\alpha_2$ and comparing with (11.83). I copied it as printed.
- Footnote 3 points to a later "entropy concentration theorem", not in this unit. Chapters 12, 14, 15 and 22 are mentioned but not covered here.
