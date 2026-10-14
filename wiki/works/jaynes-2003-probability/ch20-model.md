---
id: jaynes-2003-probability/ch20-model
work: jaynes-2003-probability
unit: "20 Model comparison"
pages: 601-614
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 23
pipeline_version: 0.1
---
# Model comparison (Ockham factors)

## L0 — One line
Comparing models is compound hypothesis testing: each model is scored by its prior-averaged likelihood, which equals its maximum likelihood times an Ockham factor, and that factor reflects prior plausibility rather than "simplicity" as such.

## L1 — The gist (≤ 120 words)
Within one model, the normalising constant $p(D|MI)$ tends to cancel. When several models are compared, it becomes the central quantity. It is the prior expectation of the likelihood. It splits into the maximum likelihood times an "Ockham factor" $W$, which, for a broad prior, is roughly the prior probability sitting in the data's high-likelihood region. A model that spreads its prior over a larger parameter space is generally penalised unless the data demand the extra freedom. Jaynes argues that "simplicity" was a poorly chosen word that hid an essential component, prior plausibility. He works out a linear-versus-quadratic response example and closes with remarks on scientific practice and on "final causes".

**Prerequisites:** Bayes' theorem and odds ratios; Gaussian integrals; maximum-likelihood estimation; least squares; the idea of a composite hypothesis (Ch. 4).

## L2 — Key ideas (5–10 bullets)
- Model comparison uses the same quantity $p(D|M_jI)$ that is only a normaliser in parameter estimation; here it must be correctly normalised, because normalisers no longer cancel (pp. 602–603).
- $p(D|MI)=L_{\max}W$ defines the Ockham factor $W\le 1$. It is the penalty paid for non-optimal prior information about the parameters (pp. 604–605, 610).
- If the prior is so broad that it is essentially constant over the high-likelihood region, $W\simeq V(\Omega')\,p(\hat\theta|MI)$: the volume $V(\Omega')$ of that region times the prior density at the maximum-likelihood point $\hat\theta$, i.e. the prior probability in the region (p. 605).
- Fair judge versus cruel realist: the Ockham factors convert the "best-performance" comparison into one that charges for the prior information we actually have (p. 603).
- Jaynes argues that "simplicity" alone is not the criterion: intuition asks how plausible the assumptions are. He suggests that "more plausible hypotheses tend to be simpler", not the reverse; Bayes' theorem does still recognise simplicity as one component (pp. 606–607).
- Adding a parameter spreads the prior over a larger space. If the old model already fits, the old model is usually preferred. This is the Ockham phenomenon (p. 607).
- In the Gaussian linear example, with the prior (width $\sigma_0$) centred on the least-squares estimate and much wider than the data's half-width $\delta\alpha$ ($\sigma_0\gg\delta\alpha$), $W_1\simeq\delta\alpha/\sigma_0$ (pp. 610–611).
- Orthodox statistics lacked even the vocabulary for this problem. Jaynes calls it a "total failure" on this problem and blames its ideology (p. 606).

## L3 — Walkthrough

### Introduction (pp. 601–602)
Inference inside a fixed model cannot remove a false premise built into that model. Scientists must therefore compare models (p. 601). Jaynes credits Ockham with seeing the mind projection fallacy, and sees his epigram "Entities are not to be multiplied without necessity" as a good start that only Bayesian analysis has made clear (p. 601). He says the problem is the compound hypothesis testing of Ch. 4. Conventional significance tests are then model comparison in which one picks the best alternative in a prescribed class (p. 601). Within one model normalisers tend to cancel. When two models appear in one equation, they do not, so all probabilities must be correctly normalised (p. 602).

### 20.1 Formulation of the problem (pp. 602–603)
For a model $M$ with parameters $\theta$, data $D$ and prior information $I$:
$$p(\theta|DMI)=p(\theta|MI)\frac{p(D|\theta MI)}{p(D|MI)}\tag{20.1}$$
$$p(D|MI)=\int d\theta\,p(D\theta|MI)=\int d\theta\,p(D|\theta MI)\,p(\theta|MI)\tag{20.2}$$
This normaliser is the prior expectation of the likelihood $L(\theta)=p(D|\theta MI)$ (p. 602). For models $\{M_1,\dots,M_r\}$:
$$p(M_j|DI)=p(M_j|I)\frac{p(D|M_jI)}{p(D|I)},\quad 1\le j\le r\tag{20.3}$$
$$\frac{p(M_j|DI)}{p(M_k|DI)}=\frac{p(M_j|I)}{p(M_k|I)}\frac{p(D|M_jI)}{p(D|M_kI)}\tag{20.4}$$
The factor $p(D|M_jI)$ now determines the status of model $j$ relative to the others. It is always the prior expectation of the likelihood over $p(\theta_j|M_jI)$, and these priors are generally different for different models (pp. 602–603).

Footnote 2 notes the same structure in maximum entropy. In statistical mechanics the relative probability of two phases is the ratio of partition functions $Z_j/Z_k$. A phase transition sits where the two are equal, and chemical thermodynamics states indifference between phases as equality of "free energies" $F_j\propto\log Z_j$, where Bayesian analysis usually prefers log-odds form (p. 602).

Intuitively, the favoured model assigns the highest probability to the data. This is the likelihood principle repeated at a higher level (p. 603). Jaynes says the Ockham principle has never been stated in exact terms, and that centuries of philosophical discussion brought no appreciable clarification of "simplicity". His point is that a model with unspecified parameters is a composite hypothesis and needs the Ch. 4 analysis (p. 603).

*Intuition note.* The "evidence" for a model is its average fit over everything its prior allows. A model that assigns high probability to the observed data is the one the data favour (p. 603).

### 20.2 The fair judge and the cruel realist (p. 603)
- **Fair judge:** gives each model the best possible prior for its parameters, so each performs at its best.
- **Cruel realist:** judges each model with the prior information we actually have.

The Ockham factors express the cruel realist's position. They convert the fair comparison into one that accounts for what is possible "here and now". A potentially superior model can be unusable if our prior places its parameters far from their maximum-likelihood values (p. 603).

**20.2.1 Parameters known in advance.** Suppose $\theta_j=\theta_j'$ is known exactly. The prior is $p(\theta_j|M_jI)=\delta(\theta_j-\theta_j')$, and (20.2) gives
$$p(D|M_jI)=p(D|\theta_j'M_jI)=L_j(\theta_j').\tag{20.5}$$
This is maximal if $\theta_j'=\hat\theta_j$, the maximum-likelihood estimate. The fair judge's odds are then
$$\frac{p(M_j|DI)}{p(M_k|DI)}=\frac{p(M_j|I)}{p(M_k|I)}\frac{(L_j)_{\max}}{(L_k)_{\max}}.\tag{20.6}$$
This case is unrealistic. In problems "amenable to reason" the prior on the parameters must be good enough for useful inference (p. 604). With a reasonable amount of data most models give sharply peaked likelihoods, so the prior matters little for parameters. It still matters for models, so Ockham factors remain important. Jaynes says this is the type of Fisher's simple biological problems. When the prior matters even for parameters (loose model or sparse data), Ockham factors make a crucial difference. In the harder problems of Jeffreys and of modern scientists and economists, "we ignore these factors at our peril" (p. 604).

**20.2.2 Parameters unknown.** For $\theta=\{\theta_1,\dots,\theta_m\}$, comparing (20.4) and (20.6) defines the Ockham factor $W$:
$$p(D|MI)=L_{\max}W\tag{20.7}$$
$$W\equiv\int d\theta\,\frac{L(\theta)}{L_{\max}}\,p(\theta|MI)\tag{20.8}$$
$W$ is the amount by which $M$ is penalised by non-optimal prior information (p. 604). If the data are much more informative than the prior, the likelihood is sharply peaked. Define the volume $V(\Omega')$ of a high-likelihood region by
$$\int d\theta\,L(\theta)=L_{\max}V(\Omega').\tag{20.9}$$
$\Omega'$ is the region of that volume holding the maximum integrated likelihood. Inside it the likelihood exceeds a threshold $L_0$ reached on its boundary (p. 605). If the prior is essentially constant over $\Omega'$,
$$W\simeq V(\Omega')\,p(\hat\theta|MI),\tag{20.10}$$
so $W$ is essentially the amount of prior probability in $\Omega'$. In general the model comparison rule becomes
$$\frac{p(M_j|DI)}{p(M_k|DI)}=\frac{p(M_j|I)}{p(M_k|I)}\frac{(L_j)_{\max}}{(L_k)_{\max}}\frac{W_j}{W_k}.\tag{20.11}$$
If two models reach the same $(L)_{\max}$, orthodox theory seems to give no basis for choice. Bayes' theorem says the prior information may still give strong grounds, and $W_j/W_k$ "may be so strong that it reverses the likelihood judgment" (p. 605).

*Intuition note.* $L_{\max}$ asks how well the best-tuned version of the model fits. $W$ asks, roughly, what fraction of the prior's probability sits near that best-tuned region. A vague prior wastes most of its probability elsewhere, so $W$ is small.

### 20.3 But where is the idea of simplicity? (pp. 605–607)
For informative data, relative merit depends on (1) the height of attainable likelihood, and (2) the prior probability in each high-likelihood region. Neither seems concerned with the intuitive notion of simplicity (p. 605).

**Historian example.** Explanations A and B fit the facts equally well. A makes four assumptions, each already highly plausible. B makes two, but they are strained and unlikely. Historians choose A. So intuition asks how plausible the hypotheses are, not how simple (p. 606).

There is a loose connection: the more complicated a set of hypotheses, the larger the manifold of alternatives, so the smaller the prior of any one. Jaynes suggests turning the old slogan around: "more plausible hypotheses tend to be simpler". A simpler hypothesis is one with fewer equally plausible alternatives (p. 606).

**On orthodoxy (author's view).** Orthodox statistics did not allow probabilities for models or for fixed unknown parameters. It tried to compare models only through sampling distributions. Within a model all parameters were then nuisance parameters, with no way to treat them. Jaynes calls it a "total failure" here (p. 606). Footnote 4 says one author, for whom Ockham's razor was by definition about simplicity, rejected Bayesian analysis because it failed to exhibit what Jaynes calls that error (p. 606).

**Mechanism (nested models).** Let $M_n$ have $\theta=\{\theta_1,\dots,\theta_n\}$ in $\Omega_n$. Define $M_{n+1}$ by adding $\theta_{n+1}$, with $\theta_{n+1}=0$ giving $M_n$ (p. 607).
- On $\Omega_n$ the likelihood is unchanged: $p(D|\theta M_{n+1}I)=p(D|\theta M_nI)$.
- The prior is spread over a larger space, so in general it gives a neighbourhood of a point in $\Omega_n$ lower probability than before.
- For an informative experiment, if the maximum-likelihood point of $M_{n+1}$ is at or near $\theta_{n+1}=0$, then $\Omega'_{n+1}$ gets less prior probability than $\Omega'_n$ did. So $p(D|M_nI)>p(D|M_{n+1}I)$. This is the Ockham phenomenon (p. 607).
- The inequality generally reverses only if the maximum-likelihood point is far from $\theta_{n+1}=0$ (a significance test would call for the parameter). Then the likelihood on $\Omega'_n$ is so much smaller that it more than compensates (p. 607).

Intuition does not give the needed size of that discrepancy. One can also invent cases, for example by redistributing prior probability on the old subspace, in which Bayes contradicts Ockham. Hence explicit calculations are needed (p. 607).

*Intuition note.* Adding a parameter dilutes the prior over more room. If the extra room is not needed, that dilution generally counts against the model.

### 20.4 An example: linear response models (pp. 607–613)
**Setup.** Data $D=\{(x_1,y_1),\dots,(x_n,y_n)\}$. The $x_i$ need not be evenly spaced or monotone. The example is the dose of a medicine ($x_i$) and the rise in blood pressure ($y_i$) in the $i$th patient (p. 608).
$$M_1:\ y_i=\alpha x_i+e_i,\qquad 1\le i\le n\tag{20.12}$$
$$M_2:\ y_i=\alpha x_i+\beta x_i^2+e_i\tag{20.13}$$
Negative $\beta$ means incipient saturation; positive $\beta$ means incipient instability. The $x_i$ are assumed to be measured with negligible error. The error distribution for $y$ is the same under both models, with $w\equiv1/\sigma^2$:
$$p(e_1\cdots e_n|I)=\prod_{i=1}^n\frac1{\sqrt{2\pi\sigma^2}}\exp\Big\{-\frac{e_i^2}{2\sigma^2}\Big\}=\Big(\frac w{2\pi}\Big)^{n/2}\exp\Big\{-\frac w2\sum_ie_i^2\Big\}\tag{20.14}$$
Everything can then be done exactly (p. 608).

**20.4.1 Digression.** Jaynes holds that this sampling distribution describes our prior state of knowledge about the errors. It is not a claim about a real frequency distribution, and he asks how anyone could acquire information about the long-run results of an experiment never performed (p. 609). The absence of correlations in (20.14) is not an assertion that none exist. It records that we know of none, and it is the safest, most conservative choice. Known correlations would allow somewhat better inference, because details otherwise dismissed as noise could count as evidence of systematic effects (p. 609).

**Model $M_1$.** With bars denoting averages over $i$:
$$p(D|\alpha M_1)=\Big(\frac w{2\pi}\Big)^{n/2}\exp\Big\{-\frac{nw}2Q_1(\alpha)\Big\}\tag{20.15}$$
$$Q_1(\alpha)\equiv\frac1n\sum_i(y_i-\alpha x_i)^2=\overline{y^2}-2\alpha\overline{xy}+\alpha^2\overline{x^2}\tag{20.16}$$
$\partial Q_1/\partial\alpha=0$ gives the ordinary least squares (maximum-likelihood) estimate $\hat\alpha$, printed as (20.17); see Reading notes for its denominator. With $w$ known:
$$L_1(\alpha)=\Big(\frac w{2\pi}\Big)^{n/2}\exp\Big\{-\frac{nw}2\Big[\overline{y^2}+\overline{x^2}(\alpha-\hat\alpha)^2-\overline{x^2}\hat\alpha^2\Big]\Big\}\tag{20.18}$$
The data alone give
$$(\alpha)_{\rm est}=\hat\alpha\pm\frac1{\sqrt{nw\overline{x^2}}}=\hat\alpha\pm\frac1{\sqrt n}\frac\sigma{x_{\rm rms}}=\hat\alpha\pm\delta\alpha,\tag{20.19}$$
with $x_{\rm rms}=\sqrt{\overline{x^2}}$. So $V(\Omega')\approx2\,\delta\alpha$ (p. 610). Then
$$p(D|M_1I)=\int d\alpha\,p(D|\alpha M_1)p(\alpha|M_1I)=L_{\max}(M_1)W_1\tag{20.20}$$
$$L_{\max}(M_1)=L_1(\hat\alpha)\tag{20.21}$$
$$W_1=\int d\alpha\,\frac{L_1(\alpha)}{L_1(\hat\alpha)}p(\alpha|M_1I)\tag{20.22}$$
$$\frac{L_1(\alpha)}{L_1(\hat\alpha)}=\exp\Big[-\frac{nw\overline{x^2}}2(\alpha-\hat\alpha)^2\Big]\tag{20.23}$$
Since this ratio cannot exceed 1 and the prior is normalised, $W_1\le1$ (p. 610).

**Prior for $\alpha$.** We usually have a guess $\alpha_0$ of the order of magnitude, are not confident of its accuracy, and think $|\alpha-\alpha_0|$ cannot be enormous. So:
$$p(\alpha|M_1I)=\sqrt{\frac{w_0}{2\pi}}\exp\Big\{-\frac{w_0}2(\alpha-\alpha_0)^2\Big\},\quad\sigma_0=1/\sqrt{w_0}\tag{20.24}$$
Jaynes says the central limit theorem (Ch. 7) and maximum entropy (Ch. 11) prefer a Gaussian "in principle" as the representation of our actual knowledge in virtually all real problems. It also allows exact integration (p. 610):
$$W_1=\sqrt{\frac{w_0}{nw\overline{x^2}+w_0}}\exp\Big\{-\frac{nw\overline{x^2}w_0}{2(nw\overline{x^2}+w_0)}(\hat\alpha-\alpha_0)^2\Big\}\tag{20.25}$$
$$W_1=\frac1{\sqrt{1+(\sigma_0/\delta\alpha)^2}}\exp\Big\{-\frac{(\hat\alpha-\alpha_0)^2}{2\sigma_0^2}\Big\}\tag{20.26}$$
Here $\delta\alpha=1/\sqrt{nw\overline{x^2}}$ is the half-width of the high-likelihood region. Limits (p. 611):
- If $\alpha_0=\hat\alpha$: $$W_1=\frac1{\sqrt{1+(\sigma_0/\delta\alpha)^2}}\tag{20.27}$$
- If also $\sigma_0\gg\delta\alpha$: $$W_1\simeq\frac{\delta\alpha}{\sigma_0}\tag{20.28}$$ This is the prior probability in the high-likelihood region, and it measures how much vague prior information hurts $M_1$. It stays approximately correct if $\alpha_0$ differs from $\hat\alpha$ by less than $\sigma_0$.
- In (20.27), if $\sigma_0\to0$ then $W_1\to1$, the maximum: the prior already gives the least-squares estimate exactly, so $M_1$ is not penalised at all. In all other cases there is some penalty. If $|\alpha_0-\hat\alpha|\gg\sigma_0$, the data strongly contradict the prior and the model is severely penalised.

**Model $M_2$.** The sampling distribution is (20.15) with
$$Q_2(\alpha,\beta)\equiv\frac1n\sum(y_i-\alpha x_i-\beta x_i^2)^2=\overline{y^2}+\alpha^2\overline{x^2}+\beta^2\overline{x^4}-2\alpha\overline{xy}-2\beta\overline{x^2y}+2\alpha\beta\overline{x^3}\tag{20.29}$$
Setting $\partial Q_2/\partial\alpha=\partial Q_2/\partial\beta=0$ gives a $2\times2$ linear system for $(\hat\alpha,\hat\beta)$:
$$\overline{x^2}\hat\alpha+\overline{x^3}\hat\beta=\overline{xy},\qquad\overline{x^3}\hat\alpha+\overline{x^4}\hat\beta=\overline{x^2y}\tag{20.30}$$
$$\hat\alpha=\frac{\overline{x^4}\,\overline{xy}-\overline{x^3}\,\overline{x^2y}}{\overline{x^2}\,\overline{x^4}-(\overline{x^3})^2},\qquad\hat\beta=\frac{\overline{x^2}\,\overline{x^2y}-\overline{x^3}\,\overline{xy}}{\overline{x^2}\,\overline{x^4}-(\overline{x^3})^2}\tag{20.31}$$
As $\overline{x^3}\to0$:
$$\hat\alpha\to\frac{\overline{xy}}{\overline{x^2}},\qquad\hat\beta\to\frac{\overline{x^2y}}{\overline{x^4}}\tag{20.32}$$
Here $\hat\alpha$ is the $M_1$ least-squares estimate (p. 612). The Ockham factor is
$$W_2=\int d\alpha\int d\beta\,\frac{L_2(\alpha,\beta)}{L_2(\hat\alpha,\hat\beta)}p(\alpha\beta|M_2I)\tag{20.33}$$
After "rather tedious algebra" the likelihood ratio is
$$\frac{L_2(\alpha,\beta)}{L_2(\hat\alpha,\hat\beta)}=\exp\Big\{-\frac{nw}2Q(\alpha,\beta)\Big\}\tag{20.34}$$
$$Q(\alpha,\beta)\equiv Q_2(\alpha,\beta)-Q_2(\hat\alpha,\hat\beta)=\overline{x^2}(\alpha-\hat\alpha)^2+2\overline{x^3}(\alpha-\hat\alpha)(\beta-\hat\beta)+\overline{x^4}(\beta-\hat\beta)^2\tag{20.35}$$
The joint prior is a product of Gaussians:
$$p(\alpha\beta|M_2I)=\sqrt{\frac{w_0}{2\pi}}e^{-\frac{w_0}2(\alpha-\alpha_0)^2}\sqrt{\frac{w_1}{2\pi}}e^{-\frac{w_1}2(\beta-\beta_0)^2}\tag{20.36}$$
The $\alpha$ prior is the same as in $M_1$ (the book prints "$w_0,a_0$"; this is $w_0,\alpha_0$). This keeps one circumstance changing between models, so results stay interpretable:
$$p(\alpha|M_1I)=p(\alpha|M_2I)\tag{20.37}$$
$$W_2=\frac{\sqrt{w_0w_1}}{2\pi}\int d\alpha\int d\beta\exp\Big\{-\tfrac12\big[nwQ(\alpha,\beta)+w_0(\alpha-\alpha_0)^2+w_1(\beta-\beta_0)^2\big]\Big\}\tag{20.38}$$
$$W_2=\sqrt{\frac{w_0w_1}{(w_0+nw\overline{x^2})(w_1+nw\overline{x^4})}}\,\exp\{x\}\tag{20.39}$$
The exponent is written as $x$; its definition is left to Editor's Exercise 20.1. The editor notes that the printed denominator is correct only if $\overline{x^3}\to0$ (p. 613). The net Ockham factor for $M_1$ over $M_2$, from (20.27) and (20.39), is
$$\frac{W_1}{W_2}=\frac{1/\sqrt{1+(\sigma_0/\delta\alpha)^2}}{\sqrt{(w_0w_1)/[(w_0+nw\overline{x^2})(w_1+nw\overline{x^4})]}\,\exp\{x\}}\tag{20.40}$$
Editor's Exercise 20.2 asks for the conditions under which $M_2$ is favoured (p. 613).

*Intuition note.* For a vague prior ($\sigma_0\gg\delta\alpha$) the penalty in $M_1$ is roughly "data width over prior width", $\delta\alpha/\sigma_0$. $W_2$ in (20.39) contains a corresponding factor for $\beta$. (Added step) By (20.11), $M_2$ is favoured exactly when its prior odds times its maximum-likelihood ratio exceed $W_1/W_2$; Exercise 20.2 asks for the explicit conditions.

### 20.5 Comments (p. 613)
Jaynes says actual science does not really obey Ockham's razor in either form. Attractive, plausible new models are often rejected by the Establishment, and progress comes mostly from a few dissenting innovators, whom he lists (Copernicus to Jeffreys). He explains this as the sociology of scholarship: the Establishment is "composed of those who sincerely believe that they are already in possession" of the truth. He adds that scholars who ignore Ockham's split between issues amenable to reason and those amenable only to faith are "doomed to a lifetime of generating nonsense" (p. 613).

**20.5.1 Final causes (p. 614).** Jaynes says debates on final causes usually assume a supernatural force overriding natural law. In his view, a final cause does not imply control of molecular details. Examples are an author's purpose in writing a book, a chemist fixing a system's volume and temperature, and a bricklayer or cook. These causes are macroscopic. Had the fine details differed in any of billions of ways, the purpose would have been satisfied just as well. A final cause may be said to "possess an entropy", indicating the number of microscopic ways of realising it, and the larger that entropy the greater the probability it is realised, so maximum entropy applies. A macroscopic final cause is familiar and carries no supernatural implication. The wielder of the cause is "merely choosing the Hamiltonian" under which a system evolves by physical law (p. 614).

## Toy example (ours)
Two models fit the data equally well, with the same $L_{\max}$ and equal prior odds. Each has one parameter $\theta$. The high-likelihood region has width $V(\Omega')=0.1$ and lies inside $[0,1]$.
- Model A has a uniform prior on $[0,1]$, so $p(\hat\theta|A)=1$. By (20.10), $W_A\simeq0.1\times1=0.1$.
- Model B has a uniform prior on $[0,10]$, so $p(\hat\theta|B)=0.1$. $W_B\simeq0.1\times0.1=0.01$.
- By (20.11), the odds for A over B are $1\times1\times(0.1/0.01)=10$.

Gaussian check with (20.27), taking $\alpha_0=\hat\alpha$ and $\delta\alpha=0.1$:
- $\sigma_0=1$: $W_1=1/\sqrt{1+100}=1/10.05\approx0.0995$, close to $\delta\alpha/\sigma_0=0.1$ as in (20.28).
- $\sigma_0=0.1$: $W_1=1/\sqrt2\approx0.707$.

A sharper prior centred on the right place is penalised less.

## Concepts
- [[marginal-likelihood]] — $p(D|MI)$, prior expectation of the likelihood; here the fundamental quantity for ranking models (p. 602)
- [[bayesian-occams-razor]] — the Ockham factor $W$ in $p(D|MI)=L_{\max}W$ penalises models whose prior is spread beyond the data's high-likelihood region (pp. 604–607)
- [[ockham-factor]] (new) — $W=\int d\theta\,(L/L_{\max})\,p(\theta|MI)\le1$ (pp. 604, 610)
- [[high-likelihood-region]] (new) — $\Omega'$, smallest region carrying the integrated likelihood $L_{\max}V(\Omega')$ (p. 605)
- [[fair-judge-vs-cruel-realist]] (new) — comparing models at their best priors versus with the priors we actually have (p. 603)
- [[composite-hypothesis]] (new) — a model with unspecified parameters; Jaynes treats model comparison as this problem (p. 603)
- [[posterior-odds-for-models]] (new) — prior odds × likelihood ratio × Ockham-factor ratio, as in (20.11) (p. 605)
- [[maximum-entropy-principle]] — cited for the Gaussian prior and for final causes; also the partition-function analogy (pp. 602, 610, 614)
- [[prior-distribution]], [[likelihood]], [[bayes-theorem]] — as used throughout (p. 602)

## Canonical instances
- [[linear-vs-quadratic-response]] — model $M_1$ ($\alpha x$) versus $M_2$ ($\alpha x+\beta x^2$), with dose and blood-pressure example and Gaussian priors (p. 608)
- [[phase-transition-partition-functions]] — relative probability of two phases is $Z_j/Z_k$; indifference where they are equal (p. 602)
- [[historian-explanations-A-B]] — four plausible assumptions beat two strained ones (p. 606)
- [[nested-model-parameter-addition]] — $M_n\subset M_{n+1}$ via $\theta_{n+1}=0$ (p. 607)
- [[final-cause-and-entropy]] — macroscopic purpose, entropy as the number of ways of realising it (p. 614)

## Bridges (candidates)
- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data.
- [same-math] Ratio of model evidences $p(D|M_j)/p(D|M_k)$ ↔ statistical mechanics: ratio of partition functions $Z_j/Z_k$ — both are ratios of normalisation constants of sub-problems (author, fn. 2, p. 602).
- [structural-analogy] $W\approx V(\Omega')\,p(\hat\theta)$ ↔ information-theory: typical-set volume — the fraction of prior mass in the region the data single out.
- [metaphor] Fair judge vs cruel realist ↔ bayesian: maximised (profile) likelihood versus prior-averaged evidence.

## Questions this raises
- How does the Ockham factor behave as $n\to\infty$ with a fixed prior? (It is written as $\delta\alpha/\sigma_0$, which shrinks as $\delta\alpha\propto1/\sqrt n$.)
- What should one do when the prior on the shared parameter changes between models, which (20.37) deliberately avoids?
- Can $W$ be computed when the likelihood is not Gaussian or the prior is not conjugate?
- How should the Gaussian-prior choice be justified when $\sigma_0$ itself is uncertain?

## Exercises worth doing
- Ex. 20.1 (p. 613) — derive $W_2$ with $\overline{x^3}\to0$ and identify the exponent $x$ — difficulty: medium
- Ex. 20.2 (p. 613) — rewrite $W_1/W_2$ in half-widths $\delta\alpha,\sigma_0,\delta\beta,\sigma_1$ and find when $M_2$ wins — difficulty: medium

## Reading notes
- Printed page = pdf − 30 (pdf 631 = p. 601).
- (20.17): the extracted text and image seem to show a bar over a single $x$ in the denominator, with no square visible. Minimising (20.16) gives $\overline{xy}/\overline{x^2}$, which agrees with (20.18) and (20.32) (added check). The digest does not reproduce (20.17).
- (20.26): the printed exponent has denominator $2\sigma_0^2$. Reducing (20.25) with $nw\overline{x^2}=1/\delta\alpha^2$ and $w_0=1/\sigma_0^2$ gives $2(\sigma_0^2+\delta\alpha^2)$ instead (added check). The two agree only when $\delta\alpha\ll\sigma_0$. The (20.27)–(20.28) limits are unaffected, since $\alpha_0=\hat\alpha$.
- After (20.36), "$w_0,a_0$" is printed; $\alpha_0$ is meant.
- The symbol $x$ in $\exp\{x\}$ (20.39–20.40) is not defined in the text. The editor leaves it to Ex. 20.1.
- The text layer drops many symbols (e.g. $\Omega'$, square roots, some overbars), so the equations were checked against the images. In (20.40) the brackets around the product in the denominator are added to match (20.39); the printed form has none.
