---
id: jaynes-2003-probability/ch08-sufficiency
work: jaynes-2003-probability
unit: "8 Sufficiency, ancillarity, and all that"
pages: 243–269
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
# Sufficiency, ancillarity, and all that

## L0 — One line
Jaynes argues that sufficiency, the likelihood principle, ancillarity and the rules for combining data are all handled automatically by the Chapter 2 rules (product rule, Bayes' theorem), with the principle that redundant information is not counted twice ($AA=A$) behind several of them.

## L1 — The gist (≤ 120 words)
Some earlier posteriors used only part of the data. Does the unused part really not matter? If the sampling density factors in Fisher's way, the posterior depends on the data only through a sufficient statistic (a summary carrying all the information about the parameter); for some priors, other statistics can do this. The likelihood principle follows from the product rule; conditioning on a Fisher ancillary statistic (a function of the data) changes nothing for a Bayesian. Combining experiments needs conditions such as logical independence; pooling is not permissible if other parameters can differ between experiments. Sample re-use, a folk theorem and clever tricks are also discussed; the Chapter 2 rules handle it all automatically.

**Prerequisites:** product rule and Bayes' theorem; likelihood vs sampling density; change of variables and Jacobians; Gaussian likelihood; Taylor expansion; orthogonality of functions.

## L2 — Key ideas
- If the sampling density factors as $p(\mathbf x|\theta)=p(r|\theta)\,b(\mathbf x)$, then $r$ is a sufficient statistic for every prior; the posterior is $\propto f(\theta)p(r|\theta)$ (pp. 245–246).
- Fisher's "for all priors" proviso is essential. For particular priors, other statistics can act as sufficient, because a prior can duplicate information in the data (pp. 248–249).
- The likelihood principle (within a specified model, the likelihood $L(\theta)$ carries all the information about $\theta$ in the data) is for Jaynes a trivial consequence of the product rule. Orthodox procedures built on long-run sampling properties, the width of the estimator's sampling distribution, or randomization violate it; so does appeal to imaginary data sets (pp. 250–254).
- A Fisher ancillary statistic $z$ has a sampling distribution independent of $\theta$. When $z$ is a function of the data, conditioning on it leaves the likelihood unchanged, so for a Bayesian "ancillarity never comes up" (pp. 253–254). In the model $d_i=f(t_i,\theta)+e_i$, the effect of generalized ancillary data is to update the noise pdf (the distribution of the errors $e_i$) (pp. 255–256).
- Evidence from several experiments may be combined when the prior information is the same and each prior includes the earlier results (chain consistency). If a later prior lacks the earlier results, combining conclusions works when the data sets are logically independent (knowing one tells nothing about the other, given $H,I$). Causal independence is not enough (pp. 258–260).
- Pooling data over experiments with a hidden extra parameter can reverse the conclusion. The new/old treatment example shows this (pp. 260–261).
- Fine-grained propositions need enumerating only when the breakdown contains information relevant to the question. Sam's thermometer reduces to a single "broken" probability if the failure modes do not change $p(D|H_iI)$ (pp. 263–264).
- Re-using data as if independent squares the likelihood and is, for Jaynes, a fraud. The remaining comments rebut the "$m$ observations, at most $m$ parameters" folk theorem and defend systematic calculation over tricks (pp. 264–269).

## L3 — Walkthrough

### Introduction (p. 243)
Jaynes says it is useful to understand these features for tactical reasons: ad hoc devices used instead of probability theory would not work acceptably unless some special circumstances were present, so these features were of major theoretical importance in orthodox statistics. None of the chapter is really needed in his applications. If the Chapter 2 rules are applied strictly and consistently, they lead automatically to the optimal inference. For us these things have "general cultural value" (p. 243).

### 8.1 Sufficiency (pp. 243–245)
In some earlier examples the posterior did not seem to use all the data.
- Binomial: only $n,r$ (order ignored).
- Rectangular: only $x_{\min},x_{\max}$.
- Gaussian: only $n,\overline x,\overline{x^2}$; the other $n-2$ properties of the data went unused (p. 243).

Chapter 2 rules out the idea that probability theory is failing here, so it seems that the unused parts of the data must be irrelevant. Jaynes asks whether the theory can confirm this directly (p. 244). Footnote 1: "irrelevant" means only that we do not need the information for our present purpose. Terminology notes: special cases go back to Laplace; Fisher (1922) generalized the idea and named it; Jeffreys noted its Bayesian significance; the marginalization paradox (Chapter 15) clarified it later (p. 244).

**Property R.** The posterior depends on $D$ only through a function $r(x_1,\dots,x_n)$ (p. 244). The posterior is
$$p(\theta|DI)=h(\theta|D)=\frac{f(\theta)\,p(x_1\ldots x_n|\theta)}{\int d\theta'\,f(\theta')\,p(x_1\ldots x_n|\theta')}\tag{8.1}$$
with no independence or exchangeability assumed. Change variables $(x_i)\to(y_i)$ with $y_1=r(\mathbf x)$ and $y_2,\dots,y_n$ chosen so the Jacobian
$$J=\frac{\partial(y_1,\dots,y_n)}{\partial(x_1,\dots,x_n)}\tag{8.2}$$
is bounded and nonvanishing. Then
$$g(y_1,\dots,y_n|\theta)=J^{-1}p(x_1\ldots x_n|\theta)\tag{8.3}$$
$$h(\theta|D)=\frac{f(\theta)\,g(y|\theta)}{\int d\theta'\,f(\theta')\,g(y|\theta')}\tag{8.4}$$
because $J$ does not depend on $\theta$ and cancels (p. 244).

Property R means (8.4) is independent of $(y_2,\dots,y_n)$ for all $\theta\in S_\theta$. Writing this as derivatives set to zero gives $n-1$ orthogonality conditions on the prior (pp. 244–245):
$$\int_{S_\theta} d\theta'\,K_i(\theta,\theta')f(\theta')=0,\qquad \theta\in S_\theta,\ 2\le i\le n\tag{8.5}$$
$$K_i(\theta,\theta')\equiv g(y|\theta)\frac{\partial g(y|\theta')}{\partial y_i}-g(y|\theta')\frac{\partial g(y|\theta)}{\partial y_i}\tag{8.6}$$
The kernel is antisymmetric: $K_i(\theta,\theta')=-K_i(\theta',\theta)$ (p. 245).

### 8.2 Fisher sufficiency (pp. 245–246)
If (8.5) holds only for one particular prior, $K_i$ need only be orthogonal to that function. Fisher (1922) in effect required it for all $f(\theta)$, by never mentioning a prior. Then $K_i$ must vanish almost everywhere (p. 245). Using
$$K_i(\theta,\theta')=g(y|\theta)g(y|\theta')\frac{\partial}{\partial y_i}\log\frac{g(y|\theta')}{g(y|\theta)}\tag{8.7}$$
the condition says: for all possible samples, the ratio $g(y|\theta')/g(y|\theta)$ is independent of $(y_2,\dots,y_n)$. Hence
$$g(y_1,\dots,y_n|\theta)=q(y_1|\theta)\,m(y_2,\dots,y_n)\tag{8.8}$$
where $q$ is, up to normalization, the marginal sampling pdf of $y_1$. In the original variables, Fisher sufficiency requires
$$p(x_1\ldots x_n|\theta)=p(r|\theta)\,b(x_1,\dots,x_n)\tag{8.9}$$
with $p(r|\theta)$ the marginal density of $r$ (p. 245).

Under (8.9) the sampling pdf of $(y_2,\dots,y_n)$ is independent of $\theta$. Fisher felt intuitively that these then carry no information about $\theta$ and called $r$ a sufficient statistic. Jaynes says Fisher's reasoning was only a conjecture within sampling theory, and "we do not see how it could be proved" in that limited context, which used no priors or posteriors (p. 245). Probability as logic demonstrates it directly: put (8.9) in (8.1), $b$ cancels, and
$$h(\theta|D)\propto f(\theta)\,p(r|\theta)\tag{8.10}$$
So in Bayesian inference with the assumed model (8.1), $r$ tells us everything about $\theta$ that is in the full data, for all priors (p. 246).

Generalization (p. 246): if $g(y|\theta)=h(y_1,y_2|\theta)m(y_3,\dots,y_n)$, then $y_1,y_2$ are jointly sufficient ($\theta$ may be multidimensional). If, in some coordinates,
$$g(y_1,\dots,y_n|\theta_1\theta_2)=h(y_1|\theta_1)k(y_2|\theta_2)m(y_3,\dots,y_n)\tag{8.11}$$
then $y_1$ is sufficient for $\theta_1$ and $y_2$ for $\theta_2$.

*Intuition note.* The part of the data that does not depend on $\theta$ is a constant multiplier of the likelihood. It cancels when the posterior is normalized, so it cannot change the answer.

#### 8.2.1 Examples (pp. 246–247)
For $n$ independent Gaussian observations,
$$p(D|\mu\sigma I)=\Big(\frac1{2\pi\sigma^2}\Big)^{n/2}\exp\Big\{-\frac{n}{2\sigma^2}\big[(\mu-\overline y)^2+s^2\big]\Big\}\tag{8.12}$$
with $\overline y,s^2$ the sample mean and variance. Only these enter the sampling distribution and the joint posterior, so they are jointly sufficient for $\mu,\sigma$. Testing sufficiency by Bayes' theorem is often easier than testing the factorization (8.11), and the two amount to the same thing (p. 246).

For $\sigma$ known, $p(\mu|\sigma DI)=A\,p(\mu|I)p(D|\mu\sigma I)/\int d\mu\,p(\mu|I)p(D|\mu I)$ (8.13). The likelihood factors as
$$p(x_1\ldots x_n|\mu\sigma I)=A\exp\Big\{-\frac{ns^2}{2\sigma^2}\Big\}\exp\Big\{-\frac{n}{2\sigma^2}(\overline x-\mu)^2\Big\}$$
(printed as a second "(8.1)", i.e. (8.14); the first line of that block prints $1/\sigma^2$ rather than $1/2\sigma^2$, see Reading notes), with sample moments (8.15): $\overline x=\frac1n\sum x_i$, $\overline{x^2}=\frac1n\sum x_i^2$, $s^2=\overline{x^2}-\overline x^2$. The factor containing $s^2$ cancels, so (8.16): $p(\mu|\sigma DI)\propto p(\mu|I)\exp\{-\frac{n}{2\sigma^2}(\overline x-\mu)^2\}$. For $\mu$ known,
$$p(\sigma|\mu DI)\propto p(\sigma|I)\,\sigma^{-n}\exp\Big\{-\frac{n}{2\sigma^2}\big(\overline{x^2}-2\mu\overline x+\mu^2\big)\Big\}\tag{8.17}$$
(p. 247).

Orthodox statistics valued Fisher sufficiency because it had so few criteria for choosing an estimator and because it brought the notion of information into orthodox thinking. If a sufficient statistic exists, Jaynes says it is hard to justify using any other; from a Bayesian standpoint one would be deliberately throwing away some of the relevant information (p. 247). Footnote 2 says that, measuring information by entropy, zero information loss in going from $D$ to $r$ is equivalent to sufficiency of $r$. It cites the Pitman–Koopman theorem and a modern version in Chapter 11 (p. 247, note 2).

#### 8.2.2 The Blackwell–Rao theorem (pp. 247–248)
Let $r$ be Fisher sufficient and $\beta(\mathbf x)$ any estimator. By (8.9),
$$p(x_1\ldots x_n|r\theta)=b(\mathbf x)\,p(r|\mathbf x\theta)=b(\mathbf x)\,\delta(r-r(\mathbf x))\tag{8.18}$$
is independent of $\theta$. So $\beta_0(r)\equiv\langle\beta|r\theta\rangle=E(\beta|r\theta)$ (8.19) is independent of $\theta$ and is itself an estimator, depending on the data only through $r$. With quadratic risk (as printed)
$$R(\theta,\beta)\equiv E[(\beta-\theta)^2|\theta]=\int dx_1\cdots dx_n\,[\beta(x_1,\dots,x_n)-\theta]^2\tag{8.20}$$
the theorem is
$$R(\theta,\beta_0)\le R(\theta,\beta)\ \text{for all }\theta\tag{8.21}$$
If $R(\theta,\beta)$ is bounded, equality holds if and only if $\beta_0=\beta$, i.e. $\beta$ already depends on the data only through $r$ (p. 248). Proof is in de Groot (cited). Jaynes's comments (p. 248):
- If no sufficient statistic exists, orthodox estimation theory "is in real trouble": no single estimator can take note of all relevant information.
- **Jaynes's view:** the Blackwell–Rao argument is not compelling to a Bayesian, since risk is a sampling-theory notion that ignores prior information.
- A better Bayesian justification: if a sufficient statistic exists, Bayes' theorem leads to it automatically, and optimal inference follows whether or not one exists. For a Bayesian, sufficiency is "a pleasant convenience", not a fundamental consideration (p. 248).

**Cauchy counterexample.** The Cauchy sampling density
$$p(x_1\ldots x_n|\theta I)=\prod_{i=1}^n\frac1\pi\frac1{1+(x_i-\theta)^2}\tag{8.22}$$
does not factor as (8.9), so no sufficient statistic exists. With Cauchy sampling it appears that no part of the data is irrelevant; every scrap is used in Bayesian inference. Jaynes concludes there can then be no satisfactory orthodox estimator, since one function conveys one piece of information and misses $n-1$ others (p. 248).

*Intuition note.* When a sufficient statistic exists, summarizing loses nothing. When it does not (Cauchy), a single summary appears to throw away relevant information, whereas the full Bayesian posterior uses all of the data.

### 8.3 Generalized sufficiency (pp. 248–249)
Fisher could not have realized that "for all priors" is essential, because he used no priors. Property R may hold under weaker conditions that depend on the prior assigned (p. 248).

Since (8.5) is linear, think of priors as spanning a Hilbert space $H$. If property R holds only for priors in a subspace $H'\subset H$, then only the projection of $K_i$ onto $H'$ must vanish. $K_i$ may be arbitrary on the complement $H-H'$ (p. 249).

For a given $r(\mathbf x)$ and sampling density, (8.6) determines $K_i$. If this kernel is incomplete (as $(\theta,\theta',i)$ vary, the functions of $\theta'$ do not span $H$), then (8.5) has nonvanishing solutions $f(\theta)$. Any non-negative solutions form a subclass of priors for which $r$ acts as a sufficient statistic: an "effective sufficient statistic" (p. 249).

So the possibility is open that different priors make different aspects of the data irrelevant; one unprepared for this may think a paradox has been found (p. 249). Jaynes says it is mysterious only if probability is seen as frequency. It "amounts to no more than" $AA=A$: redundant information is not counted twice. Information in the prior matters only if the data do not already say it, and vice versa. A prior can make an aspect of the data irrelevant by conveying information that is also in the data (p. 249). An extreme example is the binomial monkey prior in urn sampling (Chapter 6). It made all the data irrelevant, whereas other priors made all of it relevant (p. 249).

*Intuition note.* In the generalized sense, sufficiency depends on both the prior and the data, not just on the data. If the prior already contains what a statistic would tell us, that statistic adds nothing.

### 8.4 Sufficiency plus nuisance parameters (pp. 249–250)
Suppose there are parameters $\theta,\eta$ but only $\theta$ is of interest. Factor the prior as $p(\theta\eta|I)=f(\theta)g(\eta|\theta)$. Then
$$h(\theta|D)=\frac{\int d\eta\,p(\theta\eta)f(x_1,\dots,x_n|\theta\eta)}{\iint d\theta\,d\eta\,p(\theta\eta)f(x_1,\dots,x_n|\theta\eta)}=\frac{f(\theta)F(x_1,\dots,x_n|\theta)}{\int d\theta\,f(\theta)F(x_1,\dots,x_n|\theta)}\tag{8.23}$$
$$F(x_1,\dots,x_n|\theta)\equiv\int d\eta\,p(\eta|\theta I)\,f(x_1,\dots,x_n|\theta,\eta)\tag{8.24}$$
(the printed letter $f$ inside the integrand is, as we read it, the sampling density, not the prior). This has the form of (8.1), so (8.5)–(8.9) may be repeated. Given $p(\eta|\theta I)$ for which (8.24) converges, if the marginal posterior for $\theta$ has property R for all priors $f(\theta)$, then
$$F(x_1,\dots,x_n|\theta)=F^*(r|\theta)\,B(x_1,\dots,x_n)\tag{8.25}$$
But $F$ is no longer a sampling density. It is a different function for each $p(\eta|\theta I)$, so $\{F,F^*,B\}$ are functionals of that prior. Nuisance parameters change the details; the general phenomenon of sufficiency is retained (p. 250).

### 8.5 The likelihood principle (pp. 250–252)
The posterior is always a product of prior and likelihood $L(\theta)\propto p(D|\theta I)$, and the data appear only in the likelihood. So Jaynes says it is manifest that, within the context of the specified model, $L(\theta)$ contains all the information about $\theta$ in $D$. For him this is an immediate, mathematically trivial consequence of the product rule. Two data sets with $L=aL'$ ($a$ independent of $\theta$) have the same import for point estimation, interval estimation, and testing (p. 250). Those who treat a probability distribution as a physical phenomenon arising from "randomness" call this the "likelihood principle", whose validity has been controversial (p. 250).

**Barnard (1947).** Add a coin flip $Z$ to data $D$, so
$$p(DZ|\theta)=p(D|\theta)\,p(Z)\tag{8.26}$$
Barnard reasoned that the flip can tell us nothing more about $\theta$, so inference from $DZ$ should equal that from $D$. From this he concluded that only likelihood ratios matter:
$$\frac{L_1}{L_2}=\frac{p(DZ|\theta_1I)}{p(DZ|\theta_2I)}=\frac{p(D|\theta_1I)}{p(D|\theta_2I)}\tag{8.27}$$
This is commonly held to be the first statement of the likelihood principle by an orthodox statistician. Jaynes notes it is what he considered obvious in Chapter 4, where a likelihood was not a probability because its normalization is arbitrary. Not all orthodox statisticians found Barnard's argument convincing (p. 251).

**Birnbaum (1962).** The first attempted proof generally accepted by orthodox statisticians. It uses Fisher sufficiency plus a **conditionality principle**: if a coin flip picks one of two experiments $E_1,E_2$ for estimating $\theta$, the information about $\theta$ depends only on the experiment actually performed (p. 251). Jaynes says Birnbaum's argument was not accepted by all orthodox statisticians and Birnbaum himself seems to have had later doubts (p. 251).

**Jaynes's criticisms (pp. 251–252):**
- The conditionality principle ignores how $E_1,E_2$ were chosen. If $E_1,E_2$ are both accurate for small $\theta$ and an $E_3$ accurate for large $\theta$ exists, including $E_2$ at all implies prior knowledge favoring small $\theta$. So the unperformed $E_2$ need not be irrelevant (p. 251).
- Kempthorne and Folks (1971) and Fraser (1980) still attack the principle. Jaynes infers that Fisher probably accepted it, since he did not attack it, although his procedures did not respect it (pp. 251–252).
- Orthodoxy violates the principle for three reasons: (1) the dogma that an estimator's merit is set by its long-run sampling properties; (2) the dogma that accuracy is set by the width of the estimator's sampling distribution; (3) procedures where "randomization" generates the probability distribution used (p. 252).
- Coin-flip arguments cannot be accepted unconditionally if taken literally. If there is any logical connection between $\theta$ and the coin, the flip result must tell us something about $\theta$ (example: a pendulum measuring gravity, with a coin tossed in the same field). Barnard and Birnbaum assume hidden detachment but never defined the binary experiment (p. 252).
- In Jaynes's system the principle is already proved from the product rule, independent of coin flips (p. 252).
- The principle is "local, not global": it refers to a specified model not being questioned. Doubts about the apparatus or the model (a new parameter $\lambda$) do not refute it (p. 252).

### 8.6 Ancillarity (pp. 253–254)
For a location parameter, $p(x|\theta I)=f(x-\theta|I)$. **Fisher's difficulty (1934):** two data sets may give the same estimate $\theta^*$ but very different configurations (range, fourth moments), so seem to call for different conclusions about accuracy. Yet if accuracy is the width of the sampling distribution of the estimator, all estimates from one estimator have the same accuracy (p. 253).

**Fisher's remedy** (Jaynes calls it ad hockery): condition on an "ancillary" statistic $z(\mathbf x)$ that carries configuration information not in the estimator; fully describing the configuration could take as many as $n-1$ ancillary statistics. Fisher required $p(z|\theta I)=p(z|I)$. Often no ancillary statistic exists (p. 253). Bayesian view:
$$p(D|z\theta I)=\frac{p(zD|\theta I)}{p(z|\theta I)}=p(D|\theta I)\frac{p(z|D\theta I)}{p(z|\theta I)}\tag{8.28}$$
If $z=z(D)$ is a function of the data, $p(z|D\theta I)=\delta[z-z(D)]$. With $p(z|\theta I)$ independent of $\theta$, the conditioned distribution has the same $\theta$-dependence, i.e. the same likelihood. So Fisher's procedure accomplishes "nothing at all" for a Bayesian, and likelihood-respecting methods give the same inference with or without conditioning (p. 253). The value of $z$ is already known from the data, so it is redundant ($AA=A$) (p. 253).

Different answers from Fisher's conditioned and unconditioned procedures indicate only that the unconditioned one violated the likelihood principle. If $Z$ is not just a function of the data, it carries extra information and in general will alter inference (p. 254). Orthodoxy also departs from the principle when it judges accuracy by the sampling distribution over imaginary data sets. For Jaynes, the width of the likelihood from the actual data gives the accuracy. So "the question of ancillarity never comes up at all" for a Bayesian (p. 254).

### 8.7 Generalized ancillary information (pp. 254–256)
Now let $Z$ be any additional quantity not in the prior information or data. Notation (8.29): $\theta$ parameters (interesting or uninteresting), $E=e_1,\dots,e_n$ noise, $D=d_1,\dots,d_n$ data, $d_i=f(t_i\theta)+e_i$. Add (8.30) $Z=z_1,\dots,z_m$ (ancillary data). Then
$$p(\theta|DZI)=p(\theta|I)\frac{p(DZ|\theta I)}{p(DZ|I)}\tag{8.31}$$
Suppose $Z$ has, by itself, no direct relevance to $\theta$:
$$p(\theta|ZI)=p(\theta|I)\tag{8.32}$$
Jaynes says this is the essence of what Fisher meant. Fisher would say instead $p(Z|\theta I)=p(Z|I)$ (8.33), i.e. $\theta$ has no causal physical influence on $Z$. The product rule
$$p(\theta Z|I)=p(\theta|ZI)p(Z|I)=p(Z|\theta I)p(\theta|I)\tag{8.34}$$
shows (8.32) and (8.33) are equivalent as logic (p. 255). Then
$$\frac{p(DZ|\theta I)}{p(DZ|I)}=\frac{p(D|\theta ZI)}{p(D|ZI)}\tag{8.35}$$
$$p(\theta|DZI)=p(\theta|ZI)\frac{p(D|\theta ZI)}{p(D|ZI)}\tag{8.36}$$
so $Z$ now appears as part of the prior information (p. 255). The relation is reciprocal: (8.32)–(8.33) are equivalent to the factorization $p(\theta Z|I)=p(\theta|I)p(Z|I)$ (8.37), so if we estimated $Z$ with $\theta$ known, $\theta$ would be a generalized ancillary statistic (p. 255).

Likelihood (8.38) $L_0(\theta)\propto p(D|\theta I)$. By the model, $e_i=d_i-f(t_i,\theta)$ (8.39). With noise pdf $p(E|\theta I)=u(e_1,\dots,e_n,\theta)$ (8.40), $p(D|\theta I)=u(\{d_i-f(t_i,\theta)\},\theta)$ (8.41). For white Gaussian noise independent of $\theta$ this led to (7.28) (p. 255). The effect of ancillary data is simply to update the noise pdf:
$$p(E|\theta I)\to p(E|\theta ZI)\tag{8.42}$$
In general, ancillary data relevant to the noise affect estimates of all parameters through the changed noise estimate (p. 256). In the cases examined in the orthodox literature $\theta$ would not be relevant to estimating the noise, so what was actually done was $p(E|I)\to p(E|ZI)$ (8.43). In the cases Jaynes analyzed, the updating is naturally regarded as arising from a joint sampling distribution $p(DZ|I)=w(e_1,\dots,e_n,z_1,\dots,z_m)$ (8.44), with marginals
$$p(D|I)=u(e_1\cdots e_n)=\int dz_1\cdots dz_m\,w\tag{8.45}$$
$$p(Z|I)=\int de_1\cdots de_n\,w\tag{8.46}$$
(called $v(z_j)$ in (8.47)) and
$$p(D|ZI)=\frac{p(DZ|I)}{p(Z|I)}=\frac{w(e_i,z_j)}{v(z_j)}\tag{8.47}$$
Fisher's original application is said to be explained in Section 8.12 (p. 256); see Reading notes.

### 8.8 Asymptotic likelihood: Fisher information (pp. 256–257)
The normalized log likelihood is
$$\frac1n\log L(\theta)=\frac1n\sum_{i=1}^n\log p(x_i|\theta)\tag{8.48}$$
The usual assumption is that as $n\to\infty$ the sampling distribution equals the limiting relative frequencies. Jaynes knows of no case where this could be known in the real world, so the argument is only heuristic (pp. 256–257). If it held,
$$\frac1n\log L(\theta)\to\int dx\,p(x|\theta_0)\log p(x|\theta)\tag{8.49}$$
with $\theta_0$ the "true" value. With $H_0=-\int dx\,p(x|\theta_0)\log p(x|\theta_0)$ (8.50),
$$\frac1n\log L(\theta)+H_0=\int dx\,p(x|\theta_0)\log\frac{p(x|\theta)}{p(x|\theta_0)}\le0\tag{8.51}$$
The inequality uses $\log q\le q-1$ for positive real $q$, with equality iff $q=1$; the page defines $q=p(x|\theta_0)/p(x|\theta)$ (see Reading notes). Equality holds iff $p(x|\theta)=p(x|\theta_0)$ for all $x$ with $p(x|\theta_0)>0$. If different $\theta$ always give different sampling distributions ("identified"), equality holds iff $\theta=\theta_0$, so the asymptotic likelihood has a unique maximum at $\theta_0$. Non-identified values are confounded: the data cannot distinguish them (p. 257).

For multidimensional $\theta=\{\theta_1,\dots,\theta_m\}$, expand about the maximum:
$$\log p(x|\theta)=\log p(x|\theta_0)-\frac12\sum_{i,j=1}^m\frac{\partial^2\log p(x|\theta)}{\partial\theta_i\partial\theta_j}\delta\theta_i\delta\theta_j\tag{8.52}$$
$$\frac1n\log\Big[\frac{L(\theta)}{L(\theta_0)}\Big]=-\frac12\sum_{ij}I_{ij}\,\delta\theta_i\delta\theta_j\tag{8.53}$$
$$I_{ij}\equiv\int d^nx\,p(x|\theta_0)\frac{\partial^2\log p(x|\theta)}{\partial\theta_i\partial\theta_j}\tag{8.54}$$
$I_{ij}$ is the **Fisher information matrix**, a useful measure of the experiment's "resolving power": how far apart must two close values $\theta,\theta'$ be for the experiment to distinguish them (p. 257). (Sign issue: see Reading notes.)

*Intuition note.* Under Jaynes's heuristic assumption, the data-averaged log likelihood is largest at the true parameter (if it is identified). The Fisher information, built from the second derivatives at that point, is offered as a measure of how well the experiment can tell nearby parameter values apart.

### 8.9 Combining evidence from different sources (pp. 257–260)
Epigraph (Poincaré): one master's experiment can outweigh many bad ones (p. 257). **Naive claim:** 25 experiments each accurate to $\pm10\%$ give $\pm10/\sqrt{25}=\pm2\%$. Jaynes says meta-analysis (Hedges and Olkin, 1985) in psychology and sociology seems to suppose this (p. 258).

**Emperor of China fable.** If each of $N=10^9$ people knows the height to $\pm1$ m, naive averaging gives
$$\frac1{\sqrt{1\,000\,000\,000}}\ \text{m}=3\times10^{-5}\ \text{m}=0.03\ \text{mm}\tag{8.55}$$
The absurdity shows the $\sqrt N$ rule is not always valid even for causally independent data; it is essential that they be *logically* independent. Most people never saw the Emperor but share folklore, so one answer tells us about another, and folklore has almost surely generated a systematic error that survives the averaging (p. 258). Rough rule:
$$\text{error in estimate}=S\pm\frac{R}{\sqrt N}\tag{8.56}$$
with $S$ the common systematic error and $R$ the RMS random error per datum. Unless we *know* $S$ is below about one-third of $R$, we cannot be sure that the average of a million data values is more reliable than the average of ten (p. 258). The warning is well recognized by experimental physicists but missing from statisticians' textbooks (pp. 258–259).

**Chain consistency.** With prior information $I$ and data sets $A,B$ for hypothesis $H$:
$$p(H|AI)=p(H|I)\frac{p(A|HI)}{p(A|I)}\tag{8.57}$$
$$p(H|ABI)=p(H|AI)\frac{p(B|AHI)}{p(B|AI)}=p(H|I)\frac{p(A|HI)\,p(B|AHI)}{p(A|I)\,p(B|AI)}\tag{8.58}$$
Using $p(A|HI)p(B|AHI)=p(AB|HI)$ and $p(A|I)p(B|AI)=p(AB|I)$ (8.59),
$$p(H|ABI)=p(H|I)\frac{p(AB|HI)}{p(AB|I)}\tag{8.60}$$
This equals a single application with total evidence $C=AB$. So combining is valid if (1) the prior information $I$ is the same in all, and (2) the prior for each experiment includes the earlier results (p. 259). Violating (1) is left as an exercise.

If (2) is violated, so that we have only $p(H|BI)=p(H|I)\,p(B|HI)/p(B|I)$ (8.61), then from (8.58) one cannot in general write $p(H|ABI)=f[p(H|AI),p(H|BI)]$ (8.62). But if $p(B|AHI)=p(B|HI)$, the product rule (printed with $p(AB|I)$ on the left, see Reading notes)
$$p(AB|I)=p(A|BHI)p(B|HI)=p(B|AHI)p(A|HI)\tag{8.63}$$
gives $p(A|BHI)=p(A|HI)$, and combining works. For this, $A,B$ must be logically independent: given $H,I$, knowing either would tell nothing about the other (pp. 259–260). Then combining is valid and in general improves inference. Meta-analysis applied without regard to these conditions "can be utterly misleading" (p. 260).

### 8.10 Pooling the data (pp. 260–261)
The data are real, but the circumstances were more complicated than this scenario (p. 260). Old vs new treatment; entries are $100\times[p\pm\sqrt{p(1-p)/n}]$.

| | Old fail | Old succ | Old % | New fail | New succ | New % |
|---|---|---|---|---|---|---|
| A (Table 8.1) | 16 519 | 4343 | 20.8 ± 0.28 | 742 | 122 | 14.1 ± 1.10 |
| B (Table 8.2) | 3876 | 14 488 | 78.9 ± 0.30 | 1233 | 3907 | 76.0 ± 0.60 |
| Pooled (Table 8.3) | 20 395 | 18 831 | 48.0 ± 0.25 | 1975 | 4029 | 67.1 ± 0.61 |

In each experiment the old treatment is slightly but significantly better. Pooled, the new treatment looks better by over 20 times the sum of the standard deviations, and the researchers publish only the pooled table (pp. 260–261).

Jaynes's diagnosis: an extra parameter is clearly present. Both treatments did much better two years later, evidently a factor far more important than the treatment difference. Nothing in the data per se tells the reason, and only prior information about the circumstances of the tests can suggest one. Pooling introduces a very misleading bias because in B about six times as many patients received the new treatment and fewer the old. The correct conclusion is that the old treatment remains noticeably better (p. 261).

Conclusion: pooling to estimate $\theta$ is not permissible if the experiments involve other parameters that can differ between experiments. Real experiments almost always have such nuisance parameters, which are eliminated separately in drawing conclusions. Meta-analysis as a procedure is not necessarily wrong, but needs these qualifications, which Jaynes does not see how anyone could find by intuition alone. The safe course is to apply the Chapter 2 rules strictly. Whenever meta-analysis is appropriate, the full Bayesian procedure automatically reduces to it (p. 261).

*Intuition note.* Adding counts treats two sources as draws from the same situation. If a hidden factor differs between them and is unevenly mixed with the treatment, the pooled counts can reflect that factor and give a misleading comparison of the treatments.

#### 8.10.1 Fine-grained propositions (pp. 261–262)
**Objection (Venn-diagram mentality):** assigning a prior to $W\equiv$ "the dog walks" would require resolving it into atomic sub-propositions $W=W_1+W_2+\cdots$. The objectors say no principle tells which resolution is right or which parts get equal prior probability. Savage thought this made it impossible to assign priors by the principle of indifference. In this passage Jaynes replies with an observation: those who object seem never to have been concerned about how the orthodox probabilist defines his own "universal set" of atoms (p. 262). His fuller answer is in 8.11 (p. 264).

### 8.11 Sam's broken thermometer (pp. 262–264)
Let $A\equiv$ Sam's pet theory, $H_0\equiv$ thermometer works, $H_i\equiv$ broken in the $i$th way, $1\le i\le n$ (perhaps $n=1000$). The calculation Sam would like is
$$p(A|DH_0I)=p(A|H_0I)\frac{p(D|AH_0I)}{p(D|H_0I)}\tag{8.64}$$
Honesty seems to require
$$p(A|DI)=\sum_{i=0}^np(AH_i|DI)=p(A|H_0DI)p(H_0|I)+\sum_{i=1}^np(A|H_iDI)p(H_i|DI)\tag{8.65}$$
Expand by Bayes:
$$p(A|H_iDI)=p(A|H_iI)\frac{p(D|AH_iI)}{p(D|H_iI)}\tag{8.66}$$
$$p(H_i|DI)=p(H_i|I)\frac{p(D|H_iI)}{p(D|I)}\tag{8.67}$$
Presumably the thermometer's condition says nothing about the theory: $p(A|H_iI)=p(A|I)$, $0\le i\le n$ (8.68). If it were broken, the data would say nothing about the theory: $p(A|H_iDI)=p(A|H_iI)=p(A|I)$, $1\le i\le n$ (8.69). Then (8.66), (8.68), (8.69) give
$$p(D|AH_iI)=p(D|H_iI),\qquad1\le i\le n\tag{8.70}$$
and (8.65) becomes
$$p(A|DI)=\frac{p(A|I)}{p(D|I)}\Big[p(D|AH_0I)p(H_0|I)+\sum_{i=1}^np(D|H_iI)p(H_i|I)\Big]\tag{8.71}$$
If the ways of being broken do not tell different things about the data,
$$p(D|H_iI)=p(D|H_1I),\qquad1\le i\le n\tag{8.72}$$
the calculation reduces to the likelihood
$$L\equiv p(D|AH_0I)p(H_0|I)+p(D|H_1I)[1-p(H_0|I)]\tag{8.73}$$
and only the total probability of being broken matters:
$$p(\overline H_0|I)=\sum_{i=1}^np(H_i|I)=1-p(H_0|I)\tag{8.74}$$
Sam need not enumerate 1000 possibilities. If $p(D|H_iI)$ does depend on $i$, the sum should be over those $H_i$ giving different $p(D|H_iI)$ (p. 263).

General lesson: enumerating fine-grained propositions and assigning priors to all of them is necessary only if the breakdown contains information relevant to the question. Otherwise only their disjunction is relevant and needs a prior. In real problems the refinement ends naturally, and the difficulty feared by Savage does not arise (p. 264).

### 8.12 Comments (pp. 264–269)
Many persist in adding ad hoc devices to probability theory without adding information. Jaynes offers "three observations" against this (p. 264); the pages contain four subsections.

**8.12.1 The fallacy of sample re-use (pp. 264–266).** By Cox's theorems, any procedure giving a conclusion different from Bayes' theorem violates some elementary desideratum of consistency and rationality. A single application extracts all the relevant information in $D,I$, and redundant information cancels (p. 264; footnote 7 says this holds for any algorithm derived from a constrained variational principle). After $p(\theta|DI)=p(\theta|I)p(D|\theta I)/p(D|I)$ (8.75), new evidence $E$ gives
$$p(\theta|EDI)=p(\theta|DI)\frac{p(E|\theta DI)}{p(E|DI)}\tag{8.76}$$
The necessary and sufficient condition for $E$ to change conclusions is that, on some region of positive measure, the likelihood ratio differs from unity:
$$p(E|\theta DI)\ne p(E|DI)\tag{8.77}$$
If $E$ is already implied by $D,I$, then $p(E|\theta DI)=p(E|DI)=1$ (8.78), and nothing changes ($AA=A$) (p. 265).

**The famous apparent exception:** take $E=D$, call it $D^*$, but treat it as independent, in violation of the rules:
$$p(D^*|DI)=p(D^*|I)\quad\text{and}\quad p(D^*|\theta DI)=p(D^*|\theta I)\tag{8.79}$$
This squares the likelihood and seems to sharpen the posterior. Jaynes calls it fraud: the same argument would allow raising the likelihood to an arbitrarily high power. If $D,D^*$ were truly logically independent but numerically identical, squaring would be correct; the fraudulent procedure claims twice as many observations as we have (pp. 265–266). It appears in the literature as a "data dependent prior" (Akaike, 1980). Randomization tests treat each of the $n!$ permutations as new evidence; Chapter 17 examines this (p. 266).

**8.12.2 A folk theorem (pp. 266–267).** In algebra, $m<n$ equations (8.80) $y_k=f_k(x_1,\dots,x_n)$ leave the $x_i$ underdetermined. Many authors state that from $m$ observations one cannot estimate more than $m$ parameters. **Jaynes:** probability theory places no such limit. As data tend to zero, estimates relax back to the prior (p. 266). But there may be a grain of truth when the number of parameters varies at fixed data. If the posteriors are independent, estimating one parameter does not depend on how many others there are. If they become correlated, uncertainty can "leak over" and a function of the parameters may be estimated better than any one of them. For example, with high negative posterior correlation, the sum is estimated much better than the difference (pp. 266–267). Jaynes says orthodox statistics does not recognize even the concept of correlations in a posterior pdf (p. 267).

**8.12.3 Effect of prior information (p. 267).** Data make a difference only when they tell something the prior does not, and prior information makes a difference only when it tells something the data do not. So the importance of the prior can depend on the data obtained. Example: if $\theta<6$ is known and the likelihood is negligible for $\theta>6$, the constraint has no effect. If nearly all the likelihood lies at $\theta>6$, the estimate is pushed to about $\theta^*=6$, but the data then contradict the prior information and we would become skeptical of the prior, the model, or the data. The "robot" believes literally what it is told and crashes if the data and prior become logically contradictory (p. 267). In principle one data point could determine a million parameters (example: $f=\sqrt2$ at a single point). A parameter known to 12 digits could map to six parameters at two digits each. This belongs to "algorithmic complexity", not discussed here (p. 267).

**8.12.4 Clever tricks and gamesmanship (pp. 267–269).** Euler complained about results "not based on a systematic method" (pp. 267–268). Jaynes says Feller and de Finetti revel in isolated clever tricks. Example: Peter and Paul toss a coin alternately, Peter first; first head wins. Direct sum:
$$p=\sum_{n=0}^\infty\frac1{2^{2n+1}}=\frac23,\qquad p'=\sum_{n=1}^\infty\frac1{2^{2n}}=\frac13\tag{8.81}$$
Trick: if Peter fails on the first toss, Paul is in Peter's shoes, so $p'=p/2$, giving $p=2/3$, $p'=1/3$ (p. 268). Jaynes doubts that anyone saw the trick on first looking at the problem. Giving only tricks leaves readers with the impression that probability theory has no systematic methods, that Feller had superhuman cleverness, and that only such cleverness yields new results. Jaynes will continue to present systematic methods because they are the only ones guaranteed to find the solution, stressing general techniques (group invariance, partition functions, entropy, Bayes' theorem). He learned this policy from Pólya (p. 268). Tricks are useful for convincing quickly and for understanding a result already found. But "maturity" for a teacher is largely "overcoming the urge to gamesmanship" (p. 269).

## Toy example (ours, not from the text)
**Part A: sufficiency.** Three coin-flip data, success $=1$: sequence $S_1=(1,0,1)$ and $S_2=(0,1,1)$, uniform prior $f(\theta)=1$ on $[0,1]$.
- Likelihood of either sequence: $\theta\cdot(1-\theta)\cdot\theta=\theta^2(1-\theta)$.
- Factorization (8.9) with $r=$ number of successes $=2$: $p(r{=}2|\theta)=3\theta^2(1-\theta)$ and $b(\mathbf x)=1/3$ (three sequences have $r=2$). Check: $3\theta^2(1-\theta)\cdot\frac13=\theta^2(1-\theta)$ ✓.
- Normalizer: $\int_0^1\theta^2(1-\theta)\,d\theta=\frac13-\frac14=\frac1{12}$. Posterior: $12\theta^2(1-\theta)$ for both sequences.
- Mean: $12\int\theta^3(1-\theta)\,d\theta=12(\frac14-\frac15)=0.6$.
So order is irrelevant; only $r$ matters.

**Part B: sample re-use.** Treat the same data as a second, "independent" data set, as in (8.79). The likelihood is squared: $\theta^4(1-\theta)^2$.
- Normalizer: $\int_0^1\theta^4(1-\theta)^2\,d\theta=\frac15-\frac26+\frac17=\frac1{105}$. Posterior: $105\,\theta^4(1-\theta)^2$.
- This is the posterior for 6 trials with 4 successes (a Beta(5,3) density). Its mean is $5/8=0.625$.
- Variance for a Beta($a,b$) density is $\frac{ab}{(a+b)^2(a+b+1)}$ (added step; standard formula). Part A (Beta(3,2)): $\frac{6}{25\cdot6}=0.04$, sd $0.20$. Part B: $\frac{15}{64\cdot9}\approx0.026$, sd $\approx0.16$.
The apparent gain in precision is false: only 3 observations exist.

## Concepts
- [[sufficient-statistic]] (new) — a function $r$ of the data such that $p(\mathbf x|\theta)=p(r|\theta)b(\mathbf x)$; the posterior then depends on the data only through $r$, for every prior (pp. 245–246)
- [[generalized-sufficiency]] (new) — for a restricted class of priors, a statistic $r$ may play the sufficiency role even if Fisher sufficiency fails; this depends on the prior (pp. 248–249)
- [[likelihood-principle]] (new) — within a specified model, $L(\theta)$ carries all the information about $\theta$ in $D$; for Jaynes, a trivial consequence of the product rule (p. 250)
- [[conditionality-principle]] (new) — Birnbaum's principle: information depends only on the experiment actually performed; criticized by Jaynes (p. 251)
- [[ancillary-statistic]] (new) — $z$ with $p(z|\theta I)=p(z|I)$; equivalent to $p(\theta|ZI)=p(\theta|I)$; conditioning on it leaves the likelihood unchanged if $z$ is a function of the data (pp. 253–255)
- [[blackwell-rao-theorem]] (new) — conditioning an estimator on a sufficient statistic does not raise quadratic risk (pp. 247–248)
- [[nuisance-parameter]] (new) — a parameter not of interest, integrated out; sufficiency is then defined via the marginalized $F$ of (8.24) (p. 250)
- [[chain-consistency]] (new) — sequential Bayes updating equals one update on the total evidence, if $I$ is the same and later priors include earlier results (p. 259)
- [[logical-independence]] (new) — given $H,I$, knowing one data set tells nothing about the other; distinct from causal independence, which is not enough for the $\sqrt N$ rule or for combining conclusions (pp. 258–260)
- [[sample-reuse-fallacy]] (new) — treating the same data as independent a second time squares the likelihood; claims twice as many observations as one has (pp. 265–266)
- [[Fisher information]] — $I_{ij}$ defined in (8.54) as an average of second derivatives of $\log p$; a useful measure of the "resolving power" of an experiment (p. 257)
- [[Likelihood]] — the only place data enter the posterior (p. 250)
- [[Bayes' theorem]] — used here to prove sufficiency and ancillarity results (p. 246)
- [[Sequential updating]] — corresponds to chain consistency (p. 259)
- [[Principle of indifference]] — Savage's objection via fine-grained propositions (pp. 261–262)

## Canonical instances
- [[gaussian-sufficient-statistics]] — $\overline y,s^2$ jointly sufficient for $\mu,\sigma$ (pp. 246–247)
- [[cauchy-no-sufficient-statistic]] — Cauchy sampling has no sufficient statistic; it appears that no part of the data is irrelevant (p. 248)
- [[emperor-of-china-fable]] — naive averaging of $10^9$ non-independent opinions gives an absurd 0.03 mm precision (p. 258)
- [[simpsons-paradox]] — Tables 8.1–8.3: the old treatment wins in each experiment but loses when pooled (pp. 260–261). The text does not use this name.
- [[sams-broken-thermometer]] — only the total probability of "broken" is needed when the failure modes do not change $p(D|H_i I)$ (p. 263)
- [[peter-and-paul-coin-game]] — direct sum vs clever trick, $p=2/3$ (p. 268)

## Bridges (candidates)
- [same-math] Sufficiency factorization (8.9) ↔ information-theory: zero information loss (in entropy) from $D$ to $r$ iff $r$ sufficient — the text states this only in footnote 2, with the proof deferred to Chapter 11.
- [same-math] Integral in (8.51) ↔ information-theory: minus the KL divergence $D(p_{\theta_0}\|p_\theta)$; non-positivity is Gibbs' inequality. The unit does not name KL.
- [same-math] Fisher information matrix (8.54) ↔ information-theory: local curvature of KL divergence / Fisher–Rao metric (up to the sign issue in Reading notes).
- [structural-analogy] Pooling reversal (8.10) ↔ bayesian: Simpson's paradox and confounding by an unmodelled variable.
- [structural-analogy] Prior making data irrelevant ($AA=A$) ↔ information-theory: conditional mutual information is zero when the prior already contains the information.
- [structural-analogy] Systematic error $S$ in (8.56) ↔ bayesian: shared hierarchical level (common effect) limiting how much partial pooling can reduce uncertainty.

## Questions this raises
- If a prior makes part of the data irrelevant, how should one check whether that prior really encoded what the data say, rather than ignoring the data in error?
- How can one detect, from data alone, that an extra parameter (like the "two years later" effect) is present, and how would a hierarchical model handle it?
- How does the heuristic argument for asymptotic likelihood change when the model is misspecified, so there is no "true" $\theta_0$?
- Which exponential-family structure follows from Fisher factorization (the Pitman–Koopman result deferred to Chapter 11)?

## Exercises worth doing
The unit has no numbered exercises. Two tasks are explicitly left to the reader:
- (p. 259) — examine the effect of violating condition (1), different prior information in the two experiments — difficulty: medium
- (p. 266) — write the detailed equations showing how the accuracy of one parameter's estimate depends on the number of other parameters, for independent vs correlated posteriors — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 30 (pdf 273 = printed 243).
- Misprints visible in the images:
  - The second equation block on p. 246 is labelled "(8.1)" but is the (8.14) of the sequence; its first line prints $-\frac1{\sigma^2}\sum(x_i-\mu)^2$ without the factor 2 that the next line implies.
  - It contains $\exp\{-ns^2/2\overline{s}^2\}$ on p. 247 where $\sigma^2$ is evidently intended.
  - (8.16) prints $p(u|I)$ for $p(\mu|I)$, and its exponent shows $(\overline x-\mu)$ without the square seen in (8.14).
  - As printed, the integrand in (8.20) does not contain the sampling density.
  - (8.63) prints $p(AB|I)$ where $p(AB|HI)$ is needed.
  - (8.65) has $p(H_0|I)$ in the first term, while the sum has $p(H_i|DI)$.
  - (8.71) writes $p(H_0I)$ for $p(H_0|I)$.
  - The p. 252 clause "again takes note of the likelihood principle" appears to mean "takes no note", since it is listed among violations.
- With $q\equiv p(x|\theta_0)/p(x|\theta)$ as defined on p. 257, $\log q\le q-1$ does not directly give the bound in (8.51); the bound follows with $q=p(x|\theta)/p(x|\theta_0)$. The inequality (8.51) itself is stated correctly.
- Sign issue: as printed, (8.52)–(8.54) read $-\frac12\sum I_{ij}\delta\theta_i\delta\theta_j$ with $I_{ij}=\int p\,\partial^2\log p$. At a maximum those second derivatives are non-positive, so a minus sign appears to be missing from (8.54) (or the sign in (8.52)). Also $d^nx$ appears where a single-sample $x$ is used.
- Section 8.7 refers to "Comments at the end of this chapter, Section 8.12" for Fisher's original application and its "ironic lesson". Sections 8.12.1–8.12.4 in these pages do not contain it.
- Cited proofs and results (de Groot, Pitman–Koopman, Chapters 11, 15, 17, 18) are not in this unit and are not reproduced.
