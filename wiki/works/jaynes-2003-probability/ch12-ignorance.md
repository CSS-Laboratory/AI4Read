---
id: jaynes-2003-probability/ch12-ignorance
work: jaynes-2003-probability
unit: "12 Ignorance priors and transformation groups"
pages: 372–396
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
audited: 2026-10-15
audit_fixes: 9
---
# Ignorance priors and transformation groups

## L0 — One line
A prior for "complete ignorance" is restricted, and in many cases fully determined, by naming the transformations (shift, rescaling, and so on) that turn the problem into an equivalent one, and demanding that the prior keep the same form under them.

## L1 — The gist (≤ 120 words)
Maximum entropy for continuous variables needs an invariant measure m(x), which is, up to a constant factor, the "complete ignorance" prior. Jaynes asks how to find it. His answer: state which transformations leave the problem unchanged, then require that equivalent problems get the same prior. This yields functional equations (equations whose unknown is the prior function itself). Location and scale under the shift-and-rescale group give the Jeffreys prior dσ/σ; another group gives 1/σ². A Poisson rate gives dλ/λ. A Bernoulli probability gives 1/[θ(1−θ)]. Bertrand's chord problem gets a unique answer. Indifference is thus applied between problems, not between events. The result is often not normalizable, so it is a "pre-prior" that supplies the measure for maximum entropy.

**Prerequisites:** Shannon entropy; change of variables with Jacobians; Lagrange multipliers; Bayes' theorem; simple functional and differential equations.

## L2 — Key ideas
- Priors must come from logical analysis of stated prior information. Two people with the same information must assign the same prior; unspecified prior information makes a problem ill-posed (A–C, p. 373).
- The continuous entropy is the limit of the discrete one after subtracting the infinite term $\log n$: $H^c=-\int p\log(p/m)$. It is invariant under reparametrization, and the measure $m(x)$ must still be found (p. 375–376).
- "Complete ignorance" is made precise by naming a transformation group under which the state of knowledge is unchanged. Different groups give different priors: $1/\sigma$ versus $1/\sigma^2$ (p. 379–381).
- The method has two steps. First, a transformation equation relates two problems. Second, a symmetry equation says they are equivalent. Together they lead, in most cases, to a functional equation for the prior (p. 389).
- Bernoulli trials: the group is the Bayes-update map of a population of beliefs. It gives $f(\theta)\propto[\theta(1-\theta)]^{-1}$. With at least one success and one failure ($r\ge1$, $n-r\ge1$), the posterior mean is $r/n$. The Bayes–Laplace uniform prior can be read as the state of knowledge after one success and one failure have been observed (p. 384–385).
- Bertrand's problem: invariance under rotation, size and position of the circle gives $f(r,\theta)=1/(2\pi Rr)$, so $p(x)\,dx=x\,dx/\sqrt{1-x^2}$. A small experiment agreed (p. 392–394).
- In Jaynes's view the principle of indifference may be applied legitimately between problems, because the problem statement fixes the symmetries. He agrees with most writers that it is dangerous between events (p. 395).
- Group-derived priors usually cannot be normalized. They are idealizations that give the invariant measure for maximum entropy (p. 395–396).

## L3 — Walkthrough

### 12.1 What are we trying to do? (p. 372–374)
- **Subjective Bayesians (voice: Jaynes describing them):** they keep orthodox habits ("orthodox": frequency-based, non-Bayesian statistics). Sampling probabilities are "frequencies of random variables", while priors and posteriors are private opinions updated by de Finetti's coherence (a consistency rule for an individual's betting-style degrees of belief). This leads to the same Bayesian algorithm (p. 372). If priors are only opinions, they look arbitrary, yet the language still implies a "true prior" (p. 373).
- **Jaynes's three requirements (p. 373):**
  - (A) Priors represent prior information. They are found by logical analysis, not introspection.
  - (B) Prior information must be specified as fully as the data.
  - (C) Inference should be "objective": the same prior information gives the same prior.
- Translating information into a prior is, in his view, half of probability theory. The natural starting point is complete ignorance, like zero in addition (p. 373).
- For discrete sets, maximum entropy gives the uniform prior. For continuous variables intuition fails, so formal principles are needed (p. 373).
- **Objection:** complete ignorance does not exist. **Reply:** neither does a perfect triangle; it is an ideal limit of real prior information (p. 373).
- Other tools besides maximum entropy: transformation groups, marginalization theory, coding theory (p. 374).

### 12.2 Ignorance priors (p. 374)
- The maximum-entropy distribution is read as the most "honest" description of knowledge, whether or not a random experiment exists (p. 374).
- Jaynes (1963a) treated an inventory-control decision problem with no sampling distribution. Successive pieces of information narrowed the priors, and the decisions matched common sense where intuition could see the answer (p. 374).
- To the author's knowledge no other general method for setting up discrete priors has been proposed, and maximum entropy "may prove to be the final solution" for discrete priors (p. 374).

### 12.3 Continuous distributions (p. 374–378)
**The continuous information measure.** Jaynes sets aside the well-known fact that $H'=-\int dx\,p\log p$ \tag{12.1} lacks invariance under $x\to y(x)$, because (12.1) is not the result of any derivation; it turns out not to be the correct information measure (p. 375). Shannon's theorem holds only for discrete distributions. Pass to the limit from

$$H_I^d=-\sum_{i=1}^n p_i\log p_i \tag{12.2}$$

as the points $x_i$ become dense, with

$$\lim_{n\to\infty}\frac1n(\text{number of points in }a<x<b)=\int_a^b dx\,m(x) \tag{12.3}$$

$$\lim_{n\to\infty}\,n(x_{i+1}-x_i)=[m(x_i)]^{-1} \tag{12.4}$$

$$p_i=p(x_i|I)(x_{i+1}-x_i)\ \to\ p(x_i|I)[n\,m(x_i)]^{-1} \tag{12.5, 12.6}$$

Then

$$H_I^d\to\int dx\,p(x|I)\log\frac{p(x|I)}{n\,m(x)} \tag{12.7}$$

(as printed, without a leading minus sign; see Reading notes). This contains an infinite term $\log n$. Subtracting it gives, in the cases of interest, a definite limit:

$$H_I^c\equiv\lim_{n\to\infty}\left[H_I^d-\log n\right]=-\int dx\,p(x|I)\log\frac{p(x|I)}{m(x)} \tag{12.8}$$

The "invariant measure" $m(x)$ is proportional to the limiting density of points (p. 375). $p$ and $m$ transform alike under a change of variables, so $H^c_I$ is invariant (p. 376).

**Maximization (p. 376).** Constraints are $\int dx\,p=1$ \tag{12.9} and $F_k=\int dx\,p\,f_k(x)$ \tag{12.10}. Maximizing (12.8) gives

$$p(x|I)=Z^{-1}m(x)\exp\{\lambda_1f_1(x)+\dots+\lambda_mf_m(x)\} \tag{12.11}$$

$$Z(\lambda_1,\dots,\lambda_m)=\int dx\,m(x)\exp\{\lambda_1f_1+\dots+\lambda_mf_m\} \tag{12.12}$$

$$F_k=-\frac{\partial\log Z}{\partial\lambda_k} \tag{12.13}$$

($Z$ is the partition function, the normalizing constant; the $\lambda_k$ are Lagrange multipliers.)

The quadratic-loss best estimate is $\langle q\rangle=\int dx\,q(x)p(x|I)$ \tag{12.14}. The conclusions, $Z$ and the $\lambda_k$ are all invariant under $x\to y(x)$ (p. 376). (The sign in (12.13) is as printed; see Reading notes.)

*Intuition note.* Measuring entropy relative to a reference density $m$ removes the coordinate dependence of the naive formula. The cost is that we must now say what $m$ is.

**The remaining problem.** If there is no limiting process, what fixes $m(x)$? With only $a<x<b$ known, (12.11) gives

$$p(x|I)=\left[\int_a^b dx\,m(x)\right]^{-1}m(x) \tag{12.15}$$

So $m$ is, up to a constant, the "complete ignorance" prior (p. 376–377).

**Earlier attempts (p. 377).**
- Bayes: a uniform density. It was useful (Laplace in celestial mechanics) but is not invariant under reparametrization and gives no rule for choosing the parametrization. Jaynes says unbiased estimators, efficient estimators and shortest confidence intervals have the same ambiguity.
- Jeffreys: $d\sigma/\sigma$ for positive $\sigma$, because then $\sigma$ and $\sigma^m$ give the same statement. This is a step forward but does not extend to general parameter changes.
- Jaynes: we want invariance of *content*, not of form, and probability rules already say how a prior transforms. The right question is: for which choice of parameters does a given form (Bayes, Jeffreys) apply? Parameter spaces are "mollusk-like" and need "rigidity" (p. 377).
- Analogies: the invariant line element in Riemannian geometry, and invariant group measure (Haar, Pontryagin, Wigner). The method is developed largely from Wigner and Weyl (p. 377–378).

### 12.4 Transformation groups (p. 378–394)

#### 12.4.1 Location and scale parameters (p. 378–382)
Sampling distribution $p(x|\nu\sigma)=\phi(x,\nu,\sigma)\,dx$ \tag{12.16}. **Problem A:** estimate $\nu,\sigma$ from a sample, which needs a prior $p(\nu\sigma|I)\,d\nu\,d\sigma=f(\nu,\sigma)\,d\nu\,d\sigma$ \tag{12.17}.

Change variables, with $0<a<\infty$, $-\infty<b<\infty$:

$$\nu'=\nu+b,\quad \sigma'=a\sigma,\quad x'-\nu'=a(x-\nu) \tag{12.18}$$

The sampling density becomes $\psi(x',\nu',\sigma')=\phi(x,\nu,\sigma)\,dx$ \tag{12.19}, that is $\psi=a^{-1}\phi$ \tag{12.20}. The Jacobian gives the prior transformation $g(\nu',\sigma')=a^{-1}f(\nu,\sigma)$ \tag{12.21}. Both hold for any $\phi,f$ (p. 378–379).

*Invariance of the sampling distribution.* If $\psi=\phi$ \tag{12.22}, then

$$\phi(x,\nu,\sigma)=a\,\phi(ax-a\nu+\nu+b,\ \nu+b,\ a\sigma) \tag{12.23}$$

Differentiating in $a,b$ and solving gives the general solution

$$\phi(x,\nu,\sigma)=\frac1\sigma\,h\!\left(\frac{x-\nu}{\sigma}\right) \tag{12.24}$$

with $h$ arbitrary. So the usual definition of location and scale parameters is equivalent to invariance under (12.18) (p. 379).

*Ignorance as invariance.* If a change of scale or shift of location could make the problem look different, we would have had information about absolute scale or location. So complete ignorance means that scale change and location shift do not change the state of knowledge (p. 379). **Problem B** is the problem for $\nu',\sigma'$. Under this ignorance it is equivalent to A, so the same prior must be assigned: $f=g$ \tag{12.25}. With (12.21) this gives

$$f(\nu,\sigma)=a\,f(\nu+b,a\sigma) \tag{12.26}$$

$$f(\nu,\sigma)=\frac{\text{const.}}{\sigma} \tag{12.27}$$

This is the Jeffreys rule (p. 380).

*Intuition note.* Demanding the same prior in two equivalent problems turns "ignorance" into an equation. Under group (12.18) the only prior that survives is $1/\sigma$ (group (12.30) gives $1/\sigma^2$).

*It is the group, not the form of $\phi$, that fixes the prior.* The composition law of (12.18) is $(a_2,b_2)(a_1,b_1)=(a_2a_1,\,b_2+b_1)$ \tag{12.28}. The group is Abelian (the order of two operations does not matter), the direct product of two one-parameter groups, with faithful matrix representation (matrices that multiply exactly like the group elements) $\begin{pmatrix}a&0\\0&e^{b}\end{pmatrix}$ \tag{12.29}. Alternative group: scale first, then translate:

$$\nu'=a\nu+b,\quad\sigma'=a\sigma,\quad x'=ax+b \tag{12.30}$$

Its law is $(a_2,b_2)(a_1,b_1)=(a_2a_1,\,a_2b_1+b_2)$ \tag{12.31}. It is non-Abelian, with representation $\begin{pmatrix}a&b\\0&1\end{pmatrix}$ \tag{12.32}, which cannot be diagonalized. So the groups differ (p. 380–381). Under (12.30), (12.21) and (12.23) become $g=a^{-2}f$ \tag{12.33} and $\phi(x,\nu,\sigma)=a\,\phi(ax+b,a\nu+b,a\sigma)$ \tag{12.34}. The general solution of (12.34) is still (12.24), so both groups define location and scale parameters. But

$$f(\nu,\sigma)=a^2f(a\nu+b,a\sigma)\ \Rightarrow\ f(\nu,\sigma)=\frac{\text{const.}}{\sigma^2} \tag{12.35, 12.36}$$

So one must specify a definite group, not just "ignorance" (p. 381).

*Which group?* (12.30) rescales about the fixed points $x=0,\nu=0$. If we are ignorant of location, nothing singles these out. In every problem Jaynes can imagine, (12.18) and the Jeffreys prior seem appropriate, because scaling involves only $x-\nu$. He invites others to find cases where $x=0$ is special, which would justify (12.36) (p. 381). Specifying a set of operations that make an equivalent problem defines the state of knowledge far more precisely, and consistency then restricts the prior (p. 381–382).

#### 12.4.2 A Poisson rate (p. 382)
$p(n|\lambda t)=\exp\{-(\lambda t)^n/n!\}$ \tag{12.37} (as printed). The rate $\lambda$ has dimensions (seconds)$^{-1}$. We are completely ignorant of the absolute time scale. Two observers have watches with $t=qt'$, so $\lambda'=q\lambda$. They assign $f(\lambda)\,d\lambda$ \tag{12.38} and $g(\lambda')\,d\lambda'$ \tag{12.39}. Consistency gives $f(\lambda)=q\,g(\lambda')$. Both are ignorant, so $f=g$. Then $f(\lambda)=q\,f(q\lambda)$ and

$$p(d\lambda|X)\sim\lambda^{-1}d\lambda \tag{12.40}$$

Any other prior would change form when the time scale changes (p. 382).

#### 12.4.3 Unknown probability for success (p. 382–386)
Bernoulli trials: $p(r|n\theta)=\binom nr\theta^r(1-\theta)^{n-r}$ \tag{12.41}. What $f(\theta)\,d\theta$ describes ignorance of $\theta$?

- Bayes and Laplace used $f_B=1$. Jeffreys and Carnap noted that its rule of succession (the predicted probability of success on the next trial) does not seem to correspond well with intuitive inductive reasoning, and Jeffreys suggested more weight at $\theta=0,1$ (p. 383).
- **Chemical example:** after one sample dissolves, we infer that all samples dissolve; this does not carry quite the force of deductive proof, but we feel strongly it is justified. The Bayes–Laplace rule gives a negligible probability for that and only $2/3$ for the next sample dissolving (p. 383).

*Constructing the group.* The conceptual difficulty is "a probability for a probability". Jaynes removes it by imagining a population of individuals with different beliefs $\theta$, each reasoning by probability rules but holding different information. A common piece of evidence $E$ is given to all. Mr $X$ with $\theta=p(S|X)$ \tag{12.42} updates to

$$\theta'=p(S|EX)=\frac{p(S|X)p(E|SX)}{p(E|SX)p(S|X)+p(E|FX)p(F|X)} \tag{12.43}$$

This maps $[0,1]$ onto itself:

$$\theta'=\frac{a\theta}{1-\theta+a\theta},\qquad a=\frac{p(E|SX)}{p(E|FX)} \tag{12.44, 12.45}$$

*Definition of total confusion.* The population is in "total confusion" or "complete ignorance" if, after (12.44), the number of individuals with $\theta_1<\theta<\theta_2$ is unchanged (p. 384). Then $f(\theta)\,d\theta=g(\theta')\,d\theta'$ \tag{12.46} and $f=g$ \tag{12.47}, which gives

$$a\,f\!\left(\frac{a\theta}{1-\theta+a\theta}\right)=(1-\theta+a\theta)^2f(\theta) \tag{12.48}$$

(printed with "$-a\theta$" in the denominator; see Reading notes). Differentiate in $a$ and set $a=1$:

$$\theta(1-\theta)f'(\theta)=(2\theta-1)f(\theta) \tag{12.49}$$

$$f(\theta)=\frac{\text{const.}}{\theta(1-\theta)} \tag{12.50}$$

*Intuition note.* Evidence of strength $a$ pushes everyone's belief the same way. A population that "learns nothing" must keep its distribution under all such pushes. This singles out $1/[\theta(1-\theta)]$, which piles weight at 0 and 1.

*Consequences (p. 385–386).* The imaginary population has served its purpose and merges back into one statistician. For $r\ge1$, $n-r\ge1$ the posterior is

$$p(d\theta|rn)=\frac{(n-1)!}{(r-1)!(n-r-1)!}\theta^{r-1}(1-\theta)^{n-r-1}d\theta \tag{12.51}$$

$$\langle\theta\rangle=\frac rn=f,\qquad \sigma^2=\frac{f(1-f)}{n+1} \tag{12.52, 12.53}$$

- The best estimate equals the observed frequency $f$ and the next-trial probability. The Bayes–Laplace prior gives $(r+1)/(n+2)$ instead.
- Interval estimates from (12.51) are, by numerical analysis, practically equal to confidence intervals (the orthodox interval estimates). For $r\gg1$, $n-r\gg1$ the $100P\%$ interval is $f\pm q\sigma$, with $q=1.645,1.960,2.576$ for 90%, 95%, 99%.
- If $r=n-r=1$, (12.51) is uniform. So Bayes–Laplace describes having seen one success and one failure. It thus appears to be the appropriate prior when prior information assures that both outcomes are physically possible. (12.50) is a "pre-prior" state in which even that is unknown.
- For $r=0$ or $r=n$ the posterior is unnormalizable, with weight concentrated on $\theta=0$ or $1$. This accounts for the chemical inference. After one success and one failure, all posteriors are normalized.

Which prior is appropriate depends on the exact prior information (p. 386).

#### 12.4.4 Bertrand's problem (p. 386–394)
**Problem.** A long straw falls so that it intersects a circle. What is the probability that the chord is longer than the side of the inscribed equilateral triangle? Three "equally possible" assignments (uniform in (A) distance of chord center from circle center, (B) angles of intersection on the circumference, (C) chord center over the area) give $p_A=1/2$, $p_B=1/3$, $p_C=1/4$ (p. 386).

**Literature (voices).** Only Borel prefers a solution, without proof. Von Mises says such problems are outside probability theory. Most others (Bertrand included) call the problem ill-posed. This is usually read as a reason to reject indifference and to insist on frequencies (p. 386).

**Jaynes's objections.**
- Physicists have used indifference successfully, for example to predict gas viscosity (p. 387).
- When the tosser's "region of uncertainty" is large compared with the circle, chord lengths must surely go into one unique function obtainable by "pure thought" (p. 387).
- Poincaré's argument asks for lines $ux+vy=1$ whose density $p(u,v)$ is invariant under rotations and translations of the plane. The answer is $p(u,v)=(u^2+v^2)^{-3/2}$. Later authors ignored it; Jaynes finds this understandable, since the problem does not say the straw distribution has that invariance (p. 387).

**Jaynes's viewpoint (p. 388).** Ask which distribution describes our state of knowledge given only the problem statement. Consistency demands equal probabilities for equal knowledge. The statement leaves unspecified the circle's size and position. If the problem is to have any definite solution at all, it must be indifferent to them. The result may then be used as a prior, and frequency correspondence is a bonus. Jaynes grants that the conventional ill-posed reading clearly represents one valid way of interpreting the problem; it would perhaps overstate the case to call his viewpoint more correct in principle, but it will surely be more useful in practice.

*Rotational invariance (p. 388–389).* Use polar coordinates $(r,\theta)$ of the chord center. Chord-length statistics depend only on $g(r)=\int_0^{2\pi}d\theta\,f(r,\theta)$ \tag{12.54}. Observers $X,Y$ with lines of sight at angle $\alpha$ satisfy $f(r,\theta)=g(r,\theta-\alpha)$ \tag{12.55} (transformation equation). Symmetry says the problem looks the same, so $f=g$ \tag{12.56}. This must hold for all $\alpha$, so $f=f(r)$. Jaynes says the argument always has two steps, a transformation equation and a symmetry equation, and that combining them leads in most cases to a functional equation (p. 389).

*Scale invariance (p. 390–391).* Normalization: $\int_0^{2\pi}d\theta\int_0^Rr\,dr\,f(r)=1$ \tag{12.57}. Take a concentric circle of radius $aR$, $0<a\le1$, with density $h(r)$. Conditioning (a straw hitting the small circle also hits the large one) gives

$$f(r)=2\pi h(r)\int_0^{aR}r\,dr\,f(r),\quad 0<a\le1,\ 0\le r\le aR \tag{12.58}$$

(the upper limit is printed "$\alpha R$"). Scale invariance (the small problem is a scaled-down copy) gives $h(ar)(ar)\,d(ar)\,d\theta=f(r)\,r\,dr\,d\theta$ \tag{12.59}, i.e. $a^2h(ar)=f(r)$ \tag{12.60}. Combined:

$$a^2f(ar)=2\pi f(r)\int_0^{aR}u\,du\,f(u),\quad 0<a\le1,\ 0\le r\le R \tag{12.61}$$

Differentiating in $a$ at $a=1$, with normalization (12.57), gives

$$f(r)=\frac{q\,r^{q-2}}{2\pi R^q},\quad 0<q<\infty \tag{12.62}$$

with $q$ undetermined. Solution B corresponds to $f\sim1/\sqrt{R^2-r^2}$, which is not of this form, so B is eliminated. A ($q=1$) and C ($q=2$) survive (p. 390–391).

*Translational invariance (p. 391–392).* A straw hits two circles $C,C'$ of radius $R$ displaced by $b$ (Fig. 12.1). Its chord midpoints are $P=(r,\theta)$ and $P'=(r',\theta')$:

$$r'=|r-b\cos\theta| \tag{12.63}$$

$$\theta'=\begin{cases}\theta & r>b\cos\theta\\ \theta+\pi & r<b\cos\theta\end{cases} \tag{12.64}$$

The straws give a 1:1 map of region $\Gamma$ onto $\Gamma'$. Both observers use form (12.62) with the same $q$ and must assign equal probability to $\Gamma$ and $\Gamma'$. The two probabilities are

$$\frac{q}{2\pi R^q}\int_\Gamma dr\,d\theta\,r^{q-1}\tag{12.65}$$

$$\frac{q}{2\pi R^q}\int_{\Gamma'}dr'd\theta'(r')^{q-1}=\frac{q}{2\pi R^q}\int_\Gamma dr\,d\theta\,|r-b\cos\theta|^{q-1}\tag{12.66}$$

The Jacobian is unity. They are equal for arbitrary $\Gamma$ if and only if $q=1$ (p. 392). So C is eliminated, and

$$f(r,\theta)=\frac{1}{2\pi Rr},\quad 0\le r\le R,\ 0\le\theta\le2\pi \tag{12.67}$$

which is solution A. The singularity at the center is explained as follows: once a small region includes the center, all chord directions are suddenly allowed (p. 392). Translational invariance alone already determines (12.67), and (12.67) passes the scale test, so the problem has a unique solution (p. 392).

*Chord lengths.* $L=2\sqrt{R^2-r^2}$. With $x\equiv L/2R$:

$$p(x)\,dx=\frac{x\,dx}{\sqrt{1-x^2}},\quad 0\le x\le1 \tag{12.68}$$

This agrees with Borel's conjecture (p. 392–393). (Added step: $x^2=1-r^2/R^2$ gives $x\,dx=-r\,dr/R^2$. From (12.67), $p(r)\,dr=dr/R$, so $p(x)dx=x\,dx/\sqrt{1-x^2}$. Integrating from $x=\sqrt3/2$ to $1$ gives $1/2$, matching A.)

*Intuition note.* We cannot guess what a "random" straw does, but we can ask what the problem statement leaves unspecified. Size and position are unspecified, and requiring indifference to them leaves one answer.

*Frequency correspondence (p. 393–394).* The result is a state of knowledge, and in general no pure-thought argument forces real frequencies. But the derivation proves one fact: any rain of straws whose chord distribution differs from (12.68) will produce different distributions on different circles. If the tosser's uncertainty region is large compared with the circle, he lacks the skill to do that. So (12.68) should be observed in the limit of "zero skill". Jaynes and Dr Tyler tossed broom straws onto a 5-inch circle. 128 successful tosses in ten length categories confirmed (12.68) with "an embarrassingly low value of chi-squared" (a goodness-of-fit statistic; low means close agreement). Jaynes adds that experimental results will no doubt be more convincing if reported by others (p. 394). He says these conclusions seem to be in direct contradiction to von Mises; it appears to him that von Mises' philosophy, applied strictly, would reduce physical applications almost to the vanishing point (p. 393).

### 12.5 Comments (p. 394–396)
- Bertrand's problem is a model of a broader pattern: real problems look underspecified. Example: for a gas of $N$ molecules with known forces and total energy, predict velocity distribution, pressure, viscosity, etc. Maxwell predicted these by recognizing "equally possible" cases. The viscosity prediction seemed to contradict common sense but was confirmed by experiment. Poker calculations rest on the same kind of judgment (p. 394).
- **Dilemma:** the principle of indifference leads to paradoxes and also to successful predictions, so it appears that it can be neither wholly accepted nor wholly rejected (p. 395).
- **Jaynes's resolution:** apply indifference between *problems*, not between *events*. Every circumstance left unspecified defines an invariance that a unique solution must have. Not all invariances are useful: time of day or the luminosity of Betelgeuse are irrelevant, but this only helps if we already thought them germane. He suggests that the successful past uses are just those that can be "reverbalized" as indifference between problems (p. 395).
- **Jeffreys rule reinterpreted:** Jaynes says it appears that the fundamental justification is that the parameter is a *scale* parameter, not merely positive. If $\mu$ is a location parameter, both intuition and the analysis agree that a uniform prior is the appropriate way to express complete ignorance of it. For $\mu=\theta-\theta^{-1}$ mapping onto $0<\theta<\infty$, the prior is $\propto d\mu=(1+\theta^{-2})\,d\theta$, not $d\theta/\theta$ (p. 395).
- **Non-normalizability:** one reading is that complete ignorance is an idealization; shifts from St Louis to Andromeda do not give equivalent problems. So the group parameters $(a,b)$ cannot truly range over infinite intervals, and the transformations do not strictly form a group. Over the range expressing ignorance, the arguments still hold (p. 395–396).
- **Constructive reading:** the pre-prior does not strictly represent a realistic state of knowledge. It does define the invariant measure, without which finding a realistic prior by maximum entropy is mathematically indeterminate (p. 396).

## Toy example (ours)
*Poisson rate, time scale.* Prior A: $f(\lambda)\propto1/\lambda$. Prior B: uniform. Observer X measures in seconds and says λ ∈ [1, 2] per second. Observer X′ measures in minutes ($q=60$) and λ′ ∈ [60, 120] per minute (same event).

- Prior A: $\int_1^2 d\lambda/\lambda=\ln2=0.693$, and $\int_{60}^{120}d\lambda'/\lambda'=\ln120-\ln60=0.693$. Same probability.
- Prior B: widths are $2-1=1$ and $120-60=60$. Equal-content intervals get weights in ratio $1:60$ (before normalization), so the prior's content depends on the units.

Only $1/\lambda$ gives equal weight under the rescaling, as in (12.40).

*Bernoulli check (our numbers).* With $n=4$, $r=3$ and prior (12.50): $\langle\theta\rangle=3/4$ and $\sigma^2=(0.75)(0.25)/5=0.0375$ (12.52–12.53). Bayes–Laplace gives $4/6=2/3$.

*Group check (added step).* With $a=3$ and $\theta=0.5$, (12.44) gives $\theta'=1.5/(0.5+1.5)=0.75$. Since $d\theta/[\theta(1-\theta)]=d(\ln\frac{\theta}{1-\theta})$, (12.50) is uniform in log-odds. The map adds $\ln3\approx1.0986$ to the log-odds: $0\to\ln3$.

## Concepts
- [[maximum-entropy-principle]] — choose the max-entropy distribution given constraints, here relative to an invariant measure $m(x)$ (p. 374–376)
- [[differential-entropy]] — $-\int p\log p$ is not derived and not the correct measure (it also lacks invariance); $-\int p\log(p/m)$ is the continuous measure (p. 375)
- [[exponential-family-gibbs]] — the solution form (12.11) with partition function $Z$ (p. 376)
- [[principle-of-indifference-maximum-entropy]] — Jaynes defends indifference between *problems*, not events (p. 395)
- [[invariant-measure]] (new) — $m(x)$, proportional to the limiting density of discrete points; it is the ignorance prior up to a constant (p. 375–377)
- [[ignorance-prior]] (new) — prior for complete ignorance, defined as invariant under a stated transformation group (p. 379–381)
- [[transformation-group-prior]] (new) — transformation equation plus symmetry equation give a functional equation for the prior (p. 389)
- [[jeffreys-prior]] (new) — $d\sigma/\sigma$, justified here by $\sigma$ being a scale parameter under group (12.18) (p. 380, 395)
- [[pre-prior]] (new) — the usually unnormalizable ignorance distribution; it supplies the invariant measure for maximum entropy (p. 385, 396)
- [[subjective-probability]] — the view Jaynes criticizes: priors as private opinions, coherence only (p. 372–373)

## Canonical instances
- [[location-scale-problem]] — group (12.18) gives $1/\sigma$; group (12.30) gives $1/\sigma^2$ (p. 378–381)
- [[poisson-rate-prior]] — $\lambda^{-1}d\lambda$ from time-scale ignorance (p. 382)
- [[rule-of-succession]] — Bayes–Laplace $(r+1)/(n+2)$ versus $r/n$ under prior (12.50) (p. 383–386)
- [[bertrands-paradox]] — three "equally possible" answers; invariance picks $1/(2\pi Rr)$, $p(x)=x/\sqrt{1-x^2}$ (p. 386–393)
- [[maxwell-kinetic-theory]] — indifference successfully predicting gas viscosity (p. 394)

## Bridges (candidates)
- [same-math] $H^c=-\int p\log(p/m)$ ↔ information-theory: negative KL divergence $-D(p\|m)$ — same functional form; this identification is ours, not stated in the unit.
- [structural-analogy] Invariant measure $m(x)$ ↔ Haar measure / Riemannian line element — the author draws this analogy himself (p. 377–378).
- [structural-analogy] Group-invariant prior ↔ objective-Bayes reference priors — equivalence is not claimed in this unit.
- [metaphor] "Mollusk-like" parameter space ↔ coordinate freedom in general relativity — the text uses it to motivate "rigidity".
- [structural-analogy] (12.44) as multiplication of odds by $a$ ↔ Bayes' theorem in odds form — consistent with the log-odds check above.

## Questions this raises
- If group-derived priors are unnormalizable, when does a proper posterior exist? (12.51) needs $r\ge1$ and $n-r\ge1$.
- How should one decide, in a practical problem, between groups like (12.18) and (12.30)? Jaynes invites counterexamples (p. 381).
- How would a multi-parameter problem choose its group, and does the invariant measure remain unique?
- How can the group-derived "pre-prior" be combined with maximum-entropy constraints (12.11) to build realistic priors?

## Reading notes
- Page offset: printed = pdf − 30 (pdf 402–426 ↔ printed 372–396).
- No exercises are in this unit.
- Misprints visible in the images/text:
  - (12.7) is printed without the minus sign that (12.2) carries; with $p_i\to p\,[nm]^{-1}$ the limit is $-\int p\log[p/(nm)]=-\int p\log(p/m)+\log n$, which is what (12.8) requires (by my check). I kept the printed form above.
  - (12.13) prints $F_k=-\partial\log Z/\partial\lambda_k$ while $Z$ in (12.12) is defined with $\exp(+\lambda f)$. With that definition $\langle f_k\rangle=+\partial\log Z/\partial\lambda_k$ (checked by differentiating); I kept the printed sign above.
  - (12.31) prints $(a_2,b_2)(a_1,b_2)$, presumably $b_1$.
  - p. 381 prints "$\nu'=ax+b$" for the shift of $\nu$; (12.30) has $\nu'=a\nu+b$.
  - (12.48) prints $1-\theta-a\theta$ in the argument of $f$; (12.44) has $1-\theta+a\theta$, which is what the Jacobian requires.
  - (12.37) is printed as $\exp\{-(\lambda t)^n/n!\}$, which is not the Poisson formula. It should be $e^{-\lambda t}(\lambda t)^n/n!$.
  - (12.58) has "$\alpha R$" for $aR$.
  - On p. 396, "the transformations (12.50)" presumably refers to the group (12.18), since (12.50) is a prior.
  - "Harr" is printed for Haar; "James Clark Maxwell" appears as printed.
  - The citation list on p. 386 prints "Kendell"; p. 387 has "Kendall".
- The text layer was clean enough to cross-check against the page images for pdf 405–406 and 407–425; the equations above were checked against them.
