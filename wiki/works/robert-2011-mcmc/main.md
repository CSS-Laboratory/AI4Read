---
id: robert-2011-mcmc/main
work: robert-2011-mcmc
unit: paper
pages: 1-14
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# A Short History of Markov Chain Monte Carlo: Subjective Recollections from Incomplete Data

## L0 — One line
The Metropolis algorithm (Los Alamos physics, early 1950s) can reasonably be seen as the first MCMC algorithm, but statisticians adopted MCMC widely only after Gelfand and Smith (1990), and it then changed the way statisticians approach problems.

## L1 — The gist (≤ 120 words)
The paper asks how MCMC came about and why it took until about 1990 to transform statistics. The authors follow two lines, Metropolis–Hastings and Gibbs sampling. Both have the same Markov-chain justification but different origins. They describe the physics roots, the "seeds" in spatial statistics and EM-type methods, and the 1990 turning point. After 1990 came advances in convergence theory and a flood of applications. They then cover later developments: particle filters, perfect sampling, reversible jump, and regeneration with CLT-based error assessment. Their conclusion is that MCMC shifted statistics from closed-form solutions to algorithms. This is a personal, selective history, not a technical survey.

**Prerequisites:** Markov chains (stationary distribution, reversibility), basic Bayesian posteriors, conditional distributions, Monte Carlo averages and the CLT.

## L2 — Key ideas
- Monte Carlo started in Los Alamos in the 1940s. What can reasonably be seen as the first MCMC algorithm (Metropolis et al., 1953) came from the same group; its primary focus was integrals against a high-dimensional Boltzmann distribution (pp. 2–3).
- Hastings (1970) generalised the acceptance rule. Peskun (1973) showed, in a discrete setup, that Metropolis's rule is optimal among the Metropolis and Barker forms in terms of asymptotic variance. Hastings's multivariate example was already Metropolis-within-Gibbs but was overlooked (pp. 3–4).
- Gibbs-sampling "seeds" include the Hammersley–Clifford theorem (the joint is recoverable from the conditionals only under positivity), simulated EM variants and Geman and Geman (1984) (pp. 4–5).
- Gelfand and Smith (1990) was the genuine starting point for mainstream use. Tanner and Wong (1987) had similar ingredients but had less impact (p. 5).
- The 1990s brought theory (Tierney 1994, convergence rates, the positivity pitfall with improper priors) and a flood of applications, for example hierarchical and latent-variable models (pp. 6–7).
- Later developments were particle filters, perfect sampling, reversible jump and regeneration/batch means for honest standard errors (pp. 7–9).
- The authors call MCMC a paradigm shift: from closed forms to algorithms, where "exact" now means "simulated" (pp. 9–10).

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 1–2)
- The paper traces MCMC from the late 1940s to today, and Monte Carlo (MC) before it. The authors claim the methodology changed how problems are solved and also how we think about them (p. 1).
- MCMC is almost as old as MC. Its impact on statistics was "not truly felt until the very early 1990s", except in spatial statistics and image analysis, where it appeared earlier (p. 1).
- The authors treat Metropolis–Hastings and Gibbs separately because their origins differ. The Markov-chain justification is the same (p. 1).
- They also mention a "second-generation revolution" from the mid-to-late 1990s. It covers particle filters, reversible jump and perfect sampling. They end with population/sequential MC and regeneration for "honest" standard errors (p. 1).
- Mainstream statisticians realised Markov chains were widely usable only with Gelfand and Smith (1990). Earlier papers existed: Hastings 1970, Geman and Geman 1984, Tanner and Wong 1987 (p. 1).
- Reasons offered for the delay: lack of computing machinery, lack of Markov-chain background, and hesitation to trust the method in practice. Papers showing it was easy to understand and implement helped. So did the BUGS software, presented at the Valencia meeting in 1991 (pp. 1–2).
- Footnote 2: BUGS development started from Geman and Geman (1984) and Pearl (1987), following the artificial-intelligence community, and predates Gelfand and Smith (1990) (p. 2).

### 2. Before the revolution (p. 2)
- Monte Carlo was born at Los Alamos during World War II. The Metropolis algorithm followed in the early 1950s. Hastings brought MCMC closer to statistical practice in the 1970s (p. 2).
- Ulam traced the idea to an intractable combinatorial computation in 1946: the probability of winning solitaire. Von Neumann adopted it for neutron diffusion. Metropolis suggested the name "Monte Carlo" (p. 2).
- The ENIAC computer came to life in February 1946. Von Neumann used MC on thermonuclear and fission problems from 1947 (p. 2).
- In 1947 Ulam and von Neumann invented inversion and accept–reject methods for nonuniform distributions. A rudimentary version by Fermi in the 1930s got no recognition, since there were no computers (p. 2).
- A 1949 symposium took place, and Metropolis and Ulam (1949) published the first paper on the Monte Carlo method (p. 2).

**2.1 The Metropolis et al. (1953) paper (pp. 2–3)**
- The authors say the Metropolis algorithm can reasonably be regarded as the first MCMC algorithm. It is tied to the MANIAC computer, built under Metropolis in early 1952 (p. 2).
- The paper was published in June 1953 in the *Journal of Chemical Physics*. Its main target is integrals over $\mathbb R^{2N}$, where $\theta$ is a set of $N$ particles in $\mathbb R^2$ (p. 2):
$$\mathfrak I=\int F(\theta)\exp\{-E(\theta)/kT\}\,d\theta\Big/\int \exp\{-E(\theta)/kT\}\,d\theta,$$
$$E(\theta)=\frac12\sum_{i=1}^N\sum_{j\ne i}V(d_{ij}),\qquad Z(T)=\int\exp\{-E(\theta)/kT\}\,d\theta.$$
- Here $V$ is a potential function and $d_{ij}$ the distance between particles $i$ and $j$. The Boltzmann distribution $\exp\{-E/kT\}$ depends on temperature $T$ ($k$ is Boltzmann's constant). $Z(T)$ is not available in closed form except in trivial cases. Numerical integration is impossible because $\theta$ is $2N$-dimensional (pp. 2–3).
- Standard MC fails: $\exp\{-E/kT\}$ is tiny for most uniformly drawn configurations (p. 3).
- Proposal: a random-walk move for each particle $i$, $x_i'=x_i+\sigma\xi_{1i}$ and $y_i'=y_i+\sigma\xi_{2i}$, with $\xi_{1i},\xi_{2i}\sim\mathcal U(-1,1)$. The energy difference $\Delta E$ between the new and old configuration is computed. The new configuration is accepted with probability
$$\min\{1,\exp(-\Delta E/kT)\}\tag{1}$$
- Otherwise the old configuration is replicated, meaning its count rises by one in the final average of $F(\theta_t)$ over $\tau$ moves (p. 3).
- (added step) Because $\exp(-E'/kT)/\exp(-E/kT)=\exp(-\Delta E/kT)$, the unknown $Z(T)$ cancels in the acceptance rule.
- The authors note that particles are moved one at a time. This makes the original algorithm appear to be a primitive kind of Gibbs sampler (p. 3).
- Validity proof: first irreducibility (called "ergodicity"), then convergence to the stationary distribution. The second part works via a discretisation of the space. The proposal is shown reversible, then $\exp\{-E/kT\}$ is shown invariant. The result is thus proven in full generality "minus the discretization" (p. 3).
- Run lengths seem limited: 16 burn-in steps and 48 to 64 further iterations, taking four to five hours (p. 3).
- Simulated annealing (Kirkpatrick, Gelatt and Vecchi, 1983) links optimisation to the cooling of a metal. It lets $T$ in (1) vary along a "cooling schedule". It "can be shown" to find the global maximum with probability 1. The analysis is complex because with varying $T$ the chain is no longer time-homogeneous (p. 3).

*Intuition note.* The sampler never needs the hard integral $Z(T)$, only energy differences. The authors show (after discretising the space) that the accept/reject rule leaves $\exp\{-E/kT\}$ invariant, which is why the chain targets the Boltzmann distribution. Moving one particle at a time is what makes the algorithm look like a primitive Gibbs sampler.

**2.2 The Hastings (1970) paper (pp. 3–4)**
- Hastings and his student Peskun generalised Metropolis as a statistical tool against the curse of dimensionality, a point already made in 1953 (p. 3).
- Hastings (in *Biometrika*) works with finite, reversible Markov chains and treats the continuous case by a discretisation analogy. His generic acceptance probability for a move from state $i$ to $j$ is
$$\alpha_{ij}=\frac{s_{ij}}{1+(\pi_i/\pi_j)(q_{ij}/q_{ji})},\qquad s_{ij}=s_{ji},$$
with $\pi$ the target and $q$ the proposal. It covers both the Metropolis et al. (1953) form and Barker's (1965) form (p. 3).
- **Hastings's statements (reported by the authors):** little is known about the relative merits of the two choices, though Metropolis's may be preferable. High rejection rates indicate a poor transition matrix. The authors add that he does not mention the opposite pitfall, low rejection rates, which go with slow exploration (p. 3).
- Examples: a Poisson target with a ±1 random-walk proposal. A normal target with a uniform random walk mixed with its reflection (uniform centred at $-\theta_t$). A multivariate target using one-component-at-a-time updates, where the composed transition is stationary because each component update leaves the target invariant (p. 3).
- Hastings cites Ehrman, Fosdick and Handscomb (1960) as a preliminary, specific instance. The authors say this is "Metropolis-within-Gibbs except for the name". This first Gibbs sampler was "completely overlooked". Its convergence proof is general, via a composition argument as in Tierney (1994) (p. 3).
- Footnote 4: Hastings starts by mentioning a decomposition of the target into one-dimensional conditionals, but the authors say this does not amount to an early Gibbs sampler (p. 3).
- The rest of Hastings's paper covers an importance-sampling version of MCMC, error assessment, and random orthogonal matrices with another Gibbs example (pp. 3–4).
- Peskun (1973) compared Metropolis and Barker acceptance forms in a discrete setup. The Metropolis choice is optimal for the asymptotic variance of any empirical average. The proof follows from Kemeny and Snell (1960) (p. 4).
- Peskun also shows the asymptotic variance can improve on the i.i.d. case if and only if all eigenvalues of $P-A$ are negative ($A$: i.i.d. transition matrix, $P$: Metropolis). He concludes that the trace of $P-A$ is always positive (p. 4). (added step) The trace is the sum of the eigenvalues, so a positive trace rules out all-negative eigenvalues.

### 3. Seeds of the revolution (p. 4)
- Hammersley and Clifford produced in 1970 a constructive argument for recovering a joint distribution from its conditionals. Besag (1974, 1986) later named it the Hammersley–Clifford theorem. Other papers with Gibbs "seeds": Hastings 1970, Geman and Geman 1984, Besag and Clifford 1989, Broniatowski et al. 1984, Qian and Titterington 1990, Tanner and Wong 1987 (p. 4).

**3.1 Besag's early work and the fundamental (missing) theorem (p. 4)**
- Hammersley, Clifford and Besag studied specifying joint distributions from conditionals, and conditions for compatibility (p. 4).
- The theorem as the authors state it: a joint distribution for a vector tied to a dependence graph (an edge means dependence, no edge means conditional independence) must be a product of functions over the cliques. A clique is a maximal set of mutually connected nodes (p. 4, fn. 6).
- Hammersley (1974) explains why it was published only through Besag. Clifford and Hammersley disliked the positivity constraint: the joint is recoverable from the full conditionals only when the joint's support is the product of the supports of the full conditionals. A student's counter-example (Moussouris, 1974) stopped their attempts to remove it (p. 4).
- Besag (1975) doubted his method's practicality, saying it was "unlikely to be particularly helpful in many other than binary situations" (p. 4). The authors say this understated his own work (p. 4).
- Hammersley and Handscomb (1964) covered "Conditional Monte Carlo", which "looks surprisingly like" missing-data completion. Their preface: "We are convinced nevertheless that Monte Carlo methods will one day reach an impressive maturity" (p. 4).

**3.2 EM and its simulated versions as precursors (pp. 4–5)**
- EM (Dempster, Laird and Rubin, 1977) is used for missing data and so connects early to Gibbs sampling (p. 4).
- Broniatowski, Celeux and Diebolt (1984) and Celeux and Diebolt (1985) replaced the E step by a simulation step. The missing data $z$ are drawn given $x$ and the current $\theta_m$. The M step maximises the simulated complete-data log-likelihood. This is a predecessor of the Gibbs step of Diebolt and Robert (1994) (p. 4).
- Convergence theory for these methods was limited. Celeux and Diebolt (1990) solved it with SAEM, where the amount of randomness decreases over iterations, ending as EM (pp. 4–5).
- Footnote 7: other, better-known EM–MCMC links exist, but the link with Gibbs is "more tenuous". The authors give as the reason that the simulation methods there are used to approximate quantities in a Monte Carlo fashion (p. 5).

**3.3 Gibbs and beyond (p. 5)**
- Geman and Geman (1984) brought Gibbs sampling into statistical application and gave it its name. They used it for the Bayesian study of Gibbs random fields, named after Josiah Willard Gibbs (1839–1903). Their application was discrete image processing and did not involve completion (p. 5).
- Gibbs and Metropolis methods were widely used in image analysis and point processes. Ripley (1987), Section 4.7, describes Metropolis for Markov random fields and bypassing the normalising constant. Besag, York and Mollié (1991) is another example (p. 5).

### 4. The revolution (pp. 5–6)
- The gap of over 30 years between Metropolis et al. (1953) and Gelfand and Smith (1990) is partly due to computing power. Still, by the mid-1980s "the pieces were all in place" (p. 5).
- After Peskun, MCMC in statistics lay dormant for about 10 years. Then papers showed its use in pattern recognition, image analysis and spatial statistics. Geman and Geman influenced Gelfand and Smith (1990), the "genuine starting point" for intensive mainstream use. This sparked interest in Bayesian methods, computing, algorithms and stochastic processes (p. 5).
- Footnote 8: the technical report of Casella and George (1992) was titled "Gibbs for Kids". A referee disliked the title, and an animal breeder later presented "Gibbs for Pigs" (p. 5).
- Tanner and Wong (1987) had essentially the same ingredients: simulating from conditionals suffices to simulate asymptotically from the joint. It was a JASA discussion paper but had less impact than Gelfand and Smith. Reasons given: the method seemed to apply only to missing-data problems (reinforced by the name "data augmentation"), and the authors focused on approximating the posterior (p. 5).
- Their approximation of $\pi(\theta|x)$ at each iteration used (p. 5)
$$\frac1m\sum_{k=1}^m\pi(\theta|x,z^{t,k}),\qquad z^{t,k}\sim\hat\pi_{t-1}(z|x),\ k=1,\dots,m,$$
that is, $m$ replicate draws from the current approximation of the posterior of the missing data. As Dempster pointed out in discussion, this tied Data Augmentation to EM (p. 5).
- Carl Morris's discussion comes very close to a two-stage Gibbs sampler for hierarchical models. He worried about the cost of $m$ iterations. Tanner and Wong mention taking $m=1$ at the end of their paper, calling it an "extreme case" (p. 6).
- Further reasons the authors give: the paper was still too close to Rubin's (1978) multiple imputation. Its theory used functional analysis, needing a uniformly bounded, equicontinuous Markov kernel, which may have discouraged users (p. 6).
- Personal recollections: Adrian Smith's lectures at Bowling Green (summer 1986) did not yet have a fully developed Gibbs sampler. In June 1989 in Sherbrooke, he revealed the generic features of the Gibbs sampler, with a shock to the audience. The authors call the development of Gibbs sampling and MCMC, and the resulting Gelfand and Smith (1990) paper, "an epiphany" for statistics (p. 6).
- Two years later, the Ohio State conference (organised by Gelfand, Goel and Smith) had three days of talks. Many became influential papers: Albert and Chib 1993, Gelman and Rubin 1992, Geyer 1992, Gilks 1992, Liu, Wong and Kong 1994/1995, Tierney 1994. The program is in the Appendix (p. 6).
- In May 1992 a Royal Statistical Society meeting on the Gibbs sampler and other MCMC methods yielded four papers in JRSSB (1993) with 49 pages of discussion. The authors say that theory and implementation were "not always perfectly understood" (p. 6).

*Intuition note.* The reasons the authors give for the lesser impact of Tanner and Wong are: the method seemed limited to missing-data problems, the authors focused on the posterior, the paper stayed close to multiple imputation, and (possibly) its functional-analysis theory demanded too much mathematics compared with Markov-chain theory.

**4.1 Advances in MCMC theory (pp. 6–7)**
- Tierney (1994) laid out the assumptions and properties for Markov chains: convergence of ergodic averages and CLTs. Chan and Geyer (1994) relaxed a condition in Tierney's CLT, and this plays an important role today (p. 6).
- Liu, Wong and Kong (1994, 1995) analysed the covariance structure of Gibbs sampling and established the validity of Rao–Blackwellization there. Gelfand and Smith had used it, but the original theorem applied only to i.i.d. sampling (p. 6).
- Rosenthal (1995) obtained early exact convergence rates. Mengersen and Tweedie (1996) set the tone for convergence-speed studies (p. 6).
- Roberts, Gelman and Gilks (1997) set explicit targets for the acceptance rate of random-walk Metropolis–Hastings. Roberts and Rosenthal (1999) gave an upper bound of 523 iterations to approximate the target to within 1% for a slice sampler (p. 7).
- Pitfall: a tendency to specify models only through conditionals, almost always without referring to the positivity conditions (Section 3). Legitimate-looking conditionals may correspond to no joint distribution, and then the Gibbs chain cannot converge. Hobert and Casella (1996) documented the conditions. The problem only arises with improper priors, which is frequent (p. 7).
- Other work: tempering and "ladders" of chains (Geyer and Thompson 1995; Neal 1996); verifiable convergence conditions (Athreya et al. 1996); parameter expansion for Data Augmentation (Meng and van Dyk 1999; Liu and Wu 1999). Hobert and Marchev (2008) show parameter expansion can uniformly improve the original chain (p. 7).

**4.2 Advances in MCMC applications (p. 7)**
- The authors say the real reason for the explosion was that many problems seen as computational "nightmares" now yielded easily (p. 7). Their example is the random effects model of Gelfand and Smith (1990):
$$Y_{ij}=\theta_i+\varepsilon_{ij},\quad i=1,\dots,K,\ j=1,\dots,J,\tag{2}$$
with $\theta_i\sim N(\mu,\sigma_\theta^2)$ and $\varepsilon_{ij}\sim N(0,\sigma_\varepsilon^2)$, independent of $\theta_i$.
- Variance components are hard for a frequentist (REML is typically preferred). They were a nightmare for a Bayesian because the integrals are intractable. With the usual priors on $\mu,\sigma_\theta^2,\sigma_\varepsilon^2$ the full conditionals are trivial to sample, and more variance components stay easy (p. 7).
- Applications built on this: linear mixed models (Wang, Rutledge and Gianola), generalised linear mixed models (Zeger and Karim), probit models via latent variables (Albert and Chib), and mixtures (Diebolt and Robert). Latent variables can be introduced artificially to run Gibbs in about every situation (Damien, Wakefield and Walker 1999), with the slice sampler as main example (p. 7).
- A "very incomplete" list: changepoints, genomics, capture–recapture, variable selection, spatial statistics, longitudinal studies. Adaptive rejection sampling and simulated tempering helped too (p. 7).

### 5. After the revolution (pp. 7–9)
The field is "more mature". Gibbs sampling lets amateurs do complex Bayesian analysis at little cost, as in BUGS, which now uses both Gibbs and Metropolis–Hastings (pp. 7–8, fn. 10).

**5.1 A brief glimpse at particle systems (p. 8)**
- Iterating importance sampling is about as old as Monte Carlo. It appears in 1950s molecular simulation (Hammersley and Morton 1954; Rosenbluth and Rosenbluth 1955; Marshall 1965), for example to simulate self-avoiding random walks, because regular importance sampling and rejection were very inefficient (p. 8).
- The term "particle" dates to Kitagawa (1996), "particle filter" to Carpenter, Clifford and Fernhead (1997) (spelling as printed). Early signal-processing versions: Handschin and Mayne (1969) (p. 8).
- Gordon, Salmond and Smith (1993) introduced the bootstrap filter. It is formally linked to importance sampling but involves past simulations and possible MCMC steps (p. 8).
- Particle filters are for sequential data (radar, telecommunications, financial volatility). They use state-space representations, and weights are updated against incoming data. Importance weights tend to degenerate (all but one near zero), so MCMC steps can restore variety (p. 8).
- Kong, Liu and Wong (1994) developed sequential imputation. Liu and Chen (1995) first stressed resampling and coined "sequential Monte Carlo". Recent literature bridges the gap between sequential Monte Carlo and MCMC more closely by making adaptive MCMC possible (p. 8).

**5.2 Perfect sampling (p. 8)**
- Propp and Wilson (1996): using MCMC to produce an exact draw from the target. It led to many papers, but the excitement "quickly dried out". The reason given is that building perfect samplers is most often close to impossible or impractical (p. 8).
- Activity continues for point processes and stochastic geometry (Møller, Kendall), for example horizontal CFTP (coupling from the past), which mainly applies to point processes (p. 8).

**5.3 Reversible jump and variable dimensions (pp. 8–9)**
- From many viewpoints, Green's (1995) reversible jump algorithm can be seen as the start of the second MCMC revolution. It formalises a Markov chain moving across models and parameter spaces. This enabled Bayesian processing of many new models and of model choice (pp. 8–9).
- Earlier alternatives existed (Gelfand and Dey 1994; Carlin and Chib 1995). Green's balance condition on cross-model kernels gives a generic setup, even for infinitely many models (p. 9).
- Impact: at the 1996 Rebild conference, a large majority of talks used RJMCMC. Richardson and Green (1997) applied it to mixture order estimation. Stephens (2000) proposed a continuous-time version (p. 9).
- **Authors' retrospective view:** reversible jump is somehow unavoidable for very many models, as in variable selection, but is "somewhat of an overkill" for a few models, where model-specific chains may exist (p. 9).

**5.4 Regeneration and the CLT (p. 9)**
- Ergodic Theorem: if $(\theta_t)$ is a Markov chain with stationary distribution $\pi$ and $h$ has finite variance, then under fairly mild conditions
$$\lim_{n\to\infty}\bar h_n=\int h(\theta)\pi(\theta)\,d\theta=\mathbb E_\pi h(\theta)\tag{3}$$
almost everywhere, where $\bar h_n=\frac1n\sum_{i=1}^n h(\theta_i)$.
- To monitor convergence with the CLT,
$$\frac{\sqrt n\,(\bar h_n-\mathbb E_\pi h(\theta))}{\sqrt{\operatorname{Var}h(\theta)}}\to N(0,1),\tag{4}$$
there are two roadblocks (p. 9).
- Roadblock 1: dependence affects normality. Options are Kipnis and Varadhan (1986), which requires a reversible chain (as for Metropolis–Hastings), or mixing conditions (hard to verify). Chan and Geyer (1994) used geometric ergodicity to get CLTs (p. 9).
- Roadblock 2: consistent variance estimation. The naive standard error is not consistent for dependent draws. The most promising paths seem to be regeneration and batch means (p. 9).
- Regeneration uses a split chain (Athreya and Ney 1978) to restart the chain independently while preserving the stationary distribution. The independent "tours" give consistent variance estimates and honest convergence monitoring through (4) (p. 9).
- Early work: Mykland, Tierney and Yu (1995), Robert (1995), Rosenthal (1995). Most practical developments: Hobert et al. (2002, using regeneration) and Jones et al. (2006, using cumulative batch means), with consistent estimators of $\operatorname{Var}h(X)$ for chains satisfying the CLT (p. 9).

*Intuition note.* Dependence between successive draws affects the normality of the CLT and makes the naive standard error inconsistent, so judging accuracy is hard. The authors say regeneration and batch means seem the most promising paths to consistent variance estimates.

### 6. Conclusion (pp. 9–10)
- The authors say MCMC changed the whole method of thinking and attacking problems, a "paradigm shift" (Kuhn). It moved emphasis from closed-form solutions to algorithms and extended impact to real applied problems. They add: a world "where 'exact' now means 'simulated'" (pp. 9–10).
- They call it a "quantum leap". The "explosion" is over, but current work goes deeper into theory and applications, e.g. genomics and climatology data sizes (p. 10).

### Appendix: Ohio State workshop program, 15–17 Feb 1991 (pp. 10–11)
Organisers: Gelfand, Goel, Smith. Sessions: theoretical aspects of iterative sampling (Tanner; Polson; Wong, Kong and Liu); applications; posterior simulation and Markov sampling (Tierney; Müller; Gelman and Rubin; Wakefield; Palettas); adaptive sampling (Evans; Gilks; West); generalised linear models; maximum likelihood and weighted bootstrapping (Raftery and Newton; Geyer; Thompson); and a panel on the future of Bayesian inference by stochastic simulation (Berger, Gelfand, Smith).

## Toy example (ours, not from the text)
Target on two states, $\pi=(\pi_1,\pi_2)=(1/4,\,3/4)$, with symmetric proposal $q_{12}=q_{21}=1$. Hastings's form is $\alpha_{ij}=s_{ij}/(1+(\pi_i/\pi_j)(q_{ij}/q_{ji}))$.
- $\alpha_{12}=s/(1+\frac{1/4}{3/4})=s/(4/3)=3s/4$; $\alpha_{21}=s/(1+3)=s/4$.
- Metropolis (rule (1)): $\alpha_{12}=\min\{1,3\}=1$, $\alpha_{21}=\min\{1,1/3\}=1/3$. This is $s=4/3$ (check: $3\cdot\frac43/4=1$ and $\frac43/4=\frac13$).
- Barker: $s=1$ gives $\alpha_{12}=3/4$, $\alpha_{21}=1/4$.
- Metropolis chain: $P_{11}=0$, $P_{12}=1$, $P_{21}=1/3$, $P_{22}=2/3$.
- Invariance: $(\pi P)_1=\frac14\cdot0+\frac34\cdot\frac13=\frac14$ ✓. $(\pi P)_2=\frac14\cdot1+\frac34\cdot\frac23=\frac14+\frac12=\frac34$ ✓.
- Reversibility: $\pi_1\alpha_{12}=\frac14\cdot1=\frac14$ and $\pi_2\alpha_{21}=\frac34\cdot\frac13=\frac14$. For Barker: $\frac14\cdot\frac34=\frac3{16}=\frac34\cdot\frac14$ ✓. So both leave $\pi$ invariant. Metropolis accepts more often in both directions. In the text, Peskun's result concerns asymptotic variance, not acceptance rates.
- Only the ratio $\pi_1/\pi_2=1/3$ was used, so a normalising constant would cancel.

## Concepts
- [[markov-chain-monte-carlo-mcmc]] — building a Markov chain whose stationary law is the target, to approximate integrals; traced here to 1953 (p. 2)
- [[metropolis-hastings]] — propose a move, accept with probability (1) or the generic $\alpha_{ij}$; Hastings (1970) generalised the rule (p. 3)
- [[gibbs-sampling]] — update components from conditionals; named after Gibbs random fields by Geman and Geman (1984) (p. 5)
- [[monte-carlo-integration]] — average random draws to approximate integrals; here born at Los Alamos (p. 2)
- [[hammersley-clifford-theorem]] (new) — a joint law on a dependence graph is a product over clique functions; recovering the joint from conditionals needs positivity (p. 4)
- [[positivity-condition]] (new) — the joint's support is the product of the conditionals' supports; needed to recover the joint (p. 4)
- [[data-augmentation-em-simulated]] (new) — missing data $z$ are simulated given $x$ and the current parameter; links EM to Gibbs (pp. 4–5)
- [[simulated-annealing]] (new) — Metropolis with changing $T$ ("cooling schedule") for optimisation (p. 3)
- [[rao-blackwellization]] (new) — technique used by Gelfand and Smith (1990); its validity for Gibbs sampling was established by Liu, Wong and Kong (p. 6)
- [[improper-prior-gibbs-pitfall]] (new) — conditionals not matching a joint, so no convergence; arises with improper priors (p. 7)
- [[hierarchical-model]] — random-effects model (2) as the paradigm case for Gibbs (p. 7)
- [[particle-filter-sequential-monte-carlo]] (new) — importance-sampling weights propagated through time, with resampling or MCMC steps (p. 8)
- [[perfect-sampling]] (new) — MCMC-based exact simulation from the target (Propp and Wilson); mostly impractical (p. 8)
- [[reversible-jump-mcmc]] (new) — a chain moving across models of different dimension (Green 1995) (p. 8)
- [[regeneration-batch-means]] (new) — split-chain "tours" and cumulative batch means for consistent variance estimates (p. 9)
- [[convergence-diagnostics]] — here via the ergodic theorem (3) and CLT (4), needing a consistent variance estimate (p. 9)

## Canonical instances
- [[metropolis-1953-particle-system]] — first MCMC algorithm, for the Boltzmann integral of $N$ particles (pp. 2–3)
- [[hastings-1970-generic-acceptance]] — generic $\alpha_{ij}$ with Metropolis and Barker as special cases (p. 3)
- [[peskun-1973-optimality]] — Metropolis's rule optimal for asymptotic variance in discrete setups (p. 4)
- [[tanner-wong-1987-data-augmentation]] — near-Gibbs scheme, limited impact (p. 5)
- [[gelfand-smith-1990-random-effects]] — the model in (2) solved by Gibbs sampling (p. 7)
- [[bugs-software]] — Gibbs-based software, 1991 (pp. 2, 8)
- [[ohio-state-workshop-1991]] — three-day MCMC conference and program (pp. 6, 10)

## Bridges (candidates)
- [structural-analogy] Simulated annealing (varying $T$ in (1)) ↔ optimisation: random search with decreasing randomness; also SAEM, which reduces simulation noise toward EM.
- [same-math] Metropolis–Hastings acceptance ↔ Markov-chain reversibility: acceptance probability makes $\pi$ invariant (detailed balance).
- [structural-analogy] Latent-variable augmentation (probit, mixtures, slice sampler) ↔ EM's missing-data completion: both add unobserved variables to make conditionals easy.
- [structural-analogy] Particle filter weight degeneracy ↔ importance sampling in high dimension: both have weights concentrating on one draw.
- [metaphor] Paradigm shift (Kuhn) ↔ philosophy of science: the authors' framing of MCMC replacing closed-form solutions.

## Questions this raises
- Why did Hastings's Metropolis-within-Gibbs example go unnoticed, while Gelfand and Smith's presentation succeeded?
- How exactly do regeneration and batch means give consistent variance estimates for MCMC averages?
- When is reversible jump worth its complexity compared with model-specific chains?
- What are the conditions, beyond avoiding improper priors, that make a Gibbs sampler converge?

## Reading notes
- Printed page numbers equal pdf numbers (offset 0). Pages 1–14 comprise the paper, appendix and references.
- Edition facts as printed: *Statistical Science* 2011, 26(1), 102–115; the printed page labels run 1–14. A footnote says a shorter version appears as Chapter 1 of the *Handbook of Markov Chain Monte Carlo* (2011). The first page says this is an electronic reprint that differs from the original in pagination and typographic detail (an arXiv stamp is also printed).
- Misprints/OCR: p. 9 reads "as is the case for holds for Metropolis–Hastings chains" (garbled); "RJMCMCt" and "thorough" (should be "through"). "Fernhead" (Carpenter et al.) is spelled this way in the text (p. 8) and in the reference list (p. 12). The appendix shows "Random Efleeds Model … Categorica!" (p. 10) and "Universlty" (p. 11); these garbles are visible in the page images too.
- I did not summarise the reference list in detail. The paper has no exercises.
- The title ("Subjective Recollections") signals that judgements, such as why papers had impact, are the authors' own opinions.
