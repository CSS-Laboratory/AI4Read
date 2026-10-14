---
id: grimmer-2022-textasdata/ch06-multinomial
work: grimmer-2022-textasdata
unit: Chapter 6. The Multinomial Language Model
pages: 112-126
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Multinomial Language Model

## L0 — One line
A document can be modelled as a bag of words drawn from a multinomial with author-specific word rates, and a Dirichlet prior works much like simple "pseudo-count" smoothing and keeps estimates away from exactly zero.

## L1 — The gist (≤ 120 words)
How can we turn the bag-of-words representation into a probability model? The chapter tells a generative story: each token is an independent draw from a word-probability vector $\mu$, so the counts are multinomial. The authors use it for the Federalist Papers: estimate each author's $\mu$, then compare how probable the disputed essay is under each. Maximum likelihood gives a word that Jay never used probability zero under his $\mu$, so Jay's authorship of the disputed essay gets probability zero. A Dirichlet prior avoids this: it works like $\alpha$ pseudo-data (extra counts) per word. The same hierarchical building blocks recur in later clustering, admixture and classification models.

**Prerequisites:** probability mass function; factorials; independence; maximum likelihood (intuitively); vectors and matrix columns; Bayes' rule at the level of "prior → posterior".

## L2 — Key ideas
- Probabilistic models tell a data-generating story with unknown parameters (and unobserved "latent" variables). The book says the gap to algorithmic (objective-function) models is often overstated (p. 112–113).
- One-hot coding (a vector with a single 1 marking the word) makes a one-token document a categorical draw (one draw among $J$ word types). Longer documents are multinomial, i.e. independent token draws that ignore order (p. 114–115).
- The multinomial has fixed mean, variance and covariance formulas. Its MLE (maximum likelihood estimate: the $\mu$ that makes the observed counts most probable) is the observed word proportion (p. 115).
- $\mu$ lives on the simplex (non-negative, sums to 1). For estimating $\mu$, documents sharing it can be treated as one big document (p. 115–117).
- Authorship: author-specific $\mu$'s give likelihoods for the disputed essay, which favour Madison. This is a mixture model (each document comes from one of several components, here known authors) (p. 118–120).
- MLE gives zero probability to a word an author never used in his attributed texts; the authors call the resulting conclusion overly strong. Laplace smoothing adds pseudo-data (fake extra counts) (p. 121).
- The Dirichlet prior is conjugate to the multinomial (the posterior stays in the Dirichlet family), so the posterior is $\text{Dirichlet}(W+\alpha)$ and $\alpha$ works as pseudo-counts (p. 122–125).
- Putting a model on $\alpha$ gives hierarchical models (stacked layers of unknowns) that can borrow information and extend to corpus structure (p. 125).

## L3 — Walkthrough

### Opening (pp. 112–113)
- Probabilistic models posit a data-generating process with unknown parameters or latent variables, then infer them from observed data. In the Federalist example, each author generates function words at his own rates; attributed papers let us infer those rates (p. 112).
- Their appeal: assumptions are explicit, extensions are easy, and statistics offers ready tools for optimisation and uncertainty. Blei (2014) advocates a loop: build, compute, critique, repeat (p. 112).
- Algorithmic models specify steps or an objective. Linear regression can be a normal model or "minimize squared errors". A probability model implies an objective function, and many objective functions imply an algorithmic model. The book calls the two foundations "a different language for describing a similar thing" and says the difference between them is often overstated (p. 112–113).
- Plan: multinomial, language model, hierarchical extension (p. 113).

### 6.1 Multinomial distribution (pp. 114–117)
- Vocabulary (cat, dog, fish), one token per document. Each token is a one-hot vector: cat $=(1,0,0)$, dog $=(0,1,0)$, fish $=(0,0,1)$. (One-hot = "dummy variable" for social scientists.) (p. 114)
- One-token document: $W_{i,}\sim\text{Categorical}(\mu)$. Example: cat twice as likely as dog or fish gives $\mu=(.5,.25,.25)$ (p. 114).
$$p(W_{i,}\mid\mu)=\prod_{j=1}^{J}\mu_j^{W_{ij}}\tag{6.1.1}$$
- Longer documents: $W_{i,}\sim\text{Multinomial}(M_i,\mu)$, where $M_i$ is the number of tokens. $M_i=1$ gives the categorical case (p. 114).
$$p(W_{i,}\mid\mu)=\frac{M_i!}{\prod_{j=1}^{J}W_{ij}!}\prod_{j=1}^{J}\mu_j^{W_{ij}}\tag{6.1.2}$$
- Worked example: (fish, cat, fish) $=(1,0,2)$ in (cat, dog, fish) order. Then $p=\frac{3!}{1!\,0!\,2!}(.5)^1(.25)^0(.25)^2=.09375$ (p. 115).
- Each word is generated independently. This equals summing $M$ independent one-hot categorical draws, and it matches the bag-of-words idea that order is irrelevant (p. 115).
- $\mu$ must lie in the $(J-1)$-dimensional simplex: $J$ non-negative values summing to 1, i.e. a set of proportions. Figure 6.1 draws the 3-word simplex as a triangle. Its corners are $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ and its centre is $(\tfrac13,\tfrac13,\tfrac13)$ (p. 115–116).
- Properties (p. 115):
$$E[W_{ij}]=M_i\mu_j\tag{6.1.3}$$
$$\mathrm{Var}(W_{ij})=M_i\mu_j(1-\mu_j)\tag{6.1.4}$$
$$\mathrm{Cov}(W_{ij},W_{ij'})=-M_i\mu_j\mu_{j'}\tag{6.1.5}$$
  The variance and covariance are fixed functions of the parameters that determine the mean.
- We observe $W_{i,}$ and $M_i=\sum_{j'}W_{ij'}$. The MLE is the word's share of all tokens (p. 115):
$$\hat\mu_j=\frac{W_{ij}}{M_i}\tag{6.1.6}$$
- $\mu$ can be read as the word fractions in an infinite-length document (p. 116).
- $N$ documents share one $\mu$: $W_{i,}\sim\text{Multinomial}(M_i,\mu)$. Plate notation: a plate with index $N$ means $N$ replicates; $W$ is inside (shaded = observed), $\mu$ is outside, so there is one $\mu$ (Fig. 6.2, p. 116–117).
- Pooling: $\sum_iW_{i,}\sim\text{Multinomial}(\sum_iM_i,\mu)$. For estimating $\mu$, documents sharing it can be treated as one large document (p. 117).

*Intuition note.* Think of the author as rolling one weighted die per word position and tallying the faces. The model's parameters are the weights $\mu$, and the data are the counts. Because rolls are independent, for the purpose of estimating $\mu$ many documents from one author can be treated as one long document.

### 6.2 Basic language modeling (pp. 118–120)
- A language model assigns a probability to a sequence of tokens given parameters. Here we treat only unordered sets; ordered sequences come later (p. 118).
- Data (Table 6.1; vocabulary by, man, upon): Hamilton (859, 102, 374); Jay (82, 0, 1); Madison (474, 17, 7); disputed Federalist 49 (15, 2, 0) (p. 118).
- Each author has his own multinomial (Fig. 6.3). Pooling gives $W_{\mathcal H}\sim\text{Mult}(1335,\mu_{\mathcal H})$, $W_{\mathcal J}\sim\text{Mult}(83,\mu_{\mathcal J})$, $W_{\mathcal M}\sim\text{Mult}(498,\mu_{\mathcal M})$ (p. 119).
- By (6.1.6): $\hat\mu_{\mathcal H}=(.64,.08,.28)$, $\hat\mu_{\mathcal J}=(.99,0,.01)$, $\hat\mu_{\mathcal M}=(.95,.035,.015)$ (p. 119).
- The disputed essay has $M=17$, so the coefficient is $\frac{17!}{15!\,2!\,0!}$ (p. 119):
  - Hamilton: $\approx0.001$.
  - Jay: $0$, because $(0)^2=0$.
  - Madison: $\approx0.077$.
- This favours Madison, the same conclusion as Mosteller and Wallace (1963). The zero for Jay is called overly confident (p. 119).
- One model for all authors: an indicator $\pi_i$ (one-hot, length 3) says who wrote document $i$. Stack the $\mu$'s as columns of a matrix $\mu$ (shape $J\times K$, here $3\times3$):
$$W_{i,}\sim\text{Multinomial}(M_i,\mu\pi_i)\tag{6.2.1}$$
  $\pi_i$ selects a column of $\mu$ (p. 119–120).
- This is a mixture model whose component is known (Fig. 6.4). Inference on $\pi_{\text{Disputed}}$ returns in Chapter 19 (supervised classification). An unobserved $\pi$ gives a clustering model (Chapter 12) (p. 120).

*Intuition note.* Each author's word habits are a fingerprint $\mu$. We ask which fingerprint makes the disputed essay's counts most probable. Here that is Madison's.

### 6.3 Regularization and smoothing (p. 121)
- Jay never uses "man" in his five attributed papers, so $\hat\mu_{\mathcal J,\text{man}}=0$. Jay's authorship of the disputed essay then becomes a probability-zero event. The authors say this "seems" an overly strong conclusion: Jay has fewer documents than the others, so it seems more likely that the missing word is chance than that he would "never" use it (p. 121).
- Rare words are common in language, so this problem is common (p. 121).
- Regularization = non-data information or a constraint that draws estimates toward a value, helping prevent overfitting (p. 121).
- Laplace smoothing: add a fixed $\alpha$ to each word count for each author (pseudo-data). With $\alpha=1$, Jay's counts become $(83,1,2)$. The text says $P(\text{man})$ moves from 0 to .02 and the disputed text's probability under Jay from 0 to .008: unlikely, not impossible (p. 121). The effect is larger for Jay than for Hamilton or Madison because the pseudo-data stays fixed while real data grows (p. 121).
- Laplace smoothing sits outside the model. A prior on $\mu$ gives a Bayesian hierarchical model with a similar effect. Since $\mu$ must lie on the simplex, we need a distribution on the simplex; the usual choice is the Dirichlet (p. 121).

### 6.4 The Dirichlet distribution (pp. 122–125)
- Full generative process (p. 122):
$$\mu_k\sim\text{Dirichlet}(\alpha),\quad k\in\{1,2,3\}\tag{6.4.1}$$
$$\mu=[\mu_1,\mu_2,\mu_3]\tag{6.4.2}$$
$$W_{i,}\mid\mu,\pi_i\sim\text{Multinomial}(M_i,\mu\pi_i)\tag{6.4.3}$$
- $\alpha$ has the same length as $\mu$ (3 here); each $\alpha_j>0$ and is otherwise unconstrained (p. 122).
- With $\alpha_0=\sum_{j=1}^J\alpha_j$ and $\Gamma$ the gamma function (p. 122):
$$p(\mu\mid\alpha)=\frac{\Gamma(\alpha_0)}{\prod_{j=1}^{J}\Gamma(\alpha_j)}\prod_{j=1}^{J}\mu_j^{\alpha_j-1}\tag{6.4.4}$$
$$E[\mu_j]=\frac{\alpha_j}{\alpha_0}\tag{6.4.5}$$
$$\mathrm{Var}(\mu_j)=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)}\tag{6.4.6}$$
$$\mathrm{Cov}(\mu_j,\mu_{j'})=-\frac{\alpha_{j'}\alpha_j}{\alpha_0^3+\alpha_0^2}\tag{6.4.7}$$
  (The page prints the denominator as $\alpha_0^3+\alpha_0$; the exponent 2 is my reconstruction, see Reading notes.)
$$\mathrm{Mode}(\mu_j)=\frac{\alpha_j-1}{\alpha_0-J}\tag{6.4.8}$$
- Roughly, the relative sizes of the $\alpha_j$ set the typical proportions, and the size of $\alpha_0$ controls the variance. Figure 6.5 shows $\alpha=(2,2,2)$, $(20,20,20)$, $(1.2,1.2,4)$, $(4,3,2)$. A large $\alpha_0$ concentrates draws, and a larger $\alpha_j$ pushes draws toward that corner (p. 122–124).
- The Dirichlet is the conjugate prior of the multinomial: the posterior has the same form as the prior. Computation is comparatively simple, and $\alpha$ is interpretable as pseudo-data (p. 122–123).
- With $\alpha=(1,1,1)$ (Fig. 6.6), the posterior and its mean are (p. 124):
$$\mu_k\mid\alpha,W_{i,}\sim\text{Dirichlet}(W_{i,}+\alpha),\qquad E[\mu_k\mid\alpha,W_{i,}]=\frac{W_{i,}+\alpha}{\sum_{j=1}^{J}(W_{i,j}+\alpha_j)}$$
- Estimates (p. 125): $\hat\mu_{\mathcal H}=(.64,.08,.28)$; $\hat\mu_{\mathcal J}=(.97,.01,.02)$; $\hat\mu_{\mathcal M}=(.95,.035,.015)$. This is like one extra count per word type. It barely changes Hamilton and Madison but keeps Jay's "man" estimate above 0. Estimates are drawn toward $\alpha/\alpha_0$, and the effect becomes negligible as real data grows (p. 125).
- Final probabilities of the disputed text: Hamilton .001, Jay .008, Madison 0.077. Jay now has positive probability, but Madison is still the conclusion (p. 125).
- Giving $\alpha$ its own probability model stacks latent layers into a hierarchical model. Advantages: borrow information across documents and shrink toward a point; include known corpus structure (author, time); build discovery and measurement models later (p. 125).

*Intuition note.* A Dirichlet prior is like starting every author with $\alpha_j$ "free" tokens of each word. With little data these tokens matter; with much data their effect becomes negligible.

### 6.5 Conclusion (p. 126)
Specifying a probability model gives access to results from statistics and computer science on computation and theory. The authors say probabilistic and algorithmic models, such as the next chapter's vector space model, are often two quite different languages for describing a common set of techniques (p. 126).

## Toy example (ours, not from the text)
Vocabulary (tax, jobs, war). Party X's speeches have counts $(8,2,0)$, total 10. Party Y's have $(2,3,5)$, total 10. New speech $W=(1,1,1)$, $M=3$, so the coefficient is $3!/(1!1!1!)=6$.
- MLE: $\hat\mu_X=(.8,.2,0)$ gives $6\cdot.8\cdot.2\cdot0=0$. $\hat\mu_Y=(.2,.3,.5)$ gives $6\cdot.2\cdot.3\cdot.5=.18$.
- With $\alpha=(1,1,1)$ the posterior mean divides by $10+3=13$. $X$: $(9,3,1)/13$ gives $6\cdot\frac{9\cdot3\cdot1}{13^3}=\frac{162}{2197}=.074$. $Y$: $(3,4,6)/13$ gives $6\cdot\frac{72}{2197}=\frac{432}{2197}=.197$.
- Result: $X$ goes from impossible to unlikely. $Y$ is still favoured, as in the Federalist case.

## Concepts
- [[multinomial-distribution]] (new) — counts of $J$ word types in $M$ independent categorical draws with probability vector $\mu$ (p. 114)
- [[categorical-distribution]] (new) — one-token multinomial; a one-hot vector with probabilities $\mu$ (p. 114)
- [[one-hot-encoding]] (new) — length-$J$ vector with a single 1 marking the word; "dummy variable" (p. 114)
- [[simplex]] (new) — set of $J$ non-negative proportions summing to 1; the space of $\mu$ (p. 115)
- [[language-model]] (new) — model giving a probability to a token sequence (here an unordered set) given parameters (p. 118)
- [[mixture-model]] (new) — $W_i\sim\text{Mult}(M_i,\mu\pi_i)$ with indicator $\pi_i$; known labels here, unknown in clustering (p. 120)
- [[regularization]] (new) — non-data information drawing estimates toward a value to curb overfitting (p. 121)
- [[laplace-smoothing]] (new) — add $\alpha$ pseudo-counts to each word type (p. 121)
- [[dirichlet-distribution]] (new) — distribution on the simplex with parameter $\alpha$; prior for $\mu$ (p. 122)
- [[conjugate-prior]] (new) — prior whose posterior has the same form; the Dirichlet for the multinomial (p. 122)
- [[hierarchical-model]] (new) — model with stacked layers of latent variables, e.g. a prior on $\alpha$ (p. 125)
- [[text-as-data-validation]] — only loosely related here: authorship probabilities are compared with Mosteller–Wallace's conclusion (p. 119)

## Canonical instances
- [[federalist-papers-authorship]] (new) — Hamilton/Jay/Madison word rates; disputed Federalist 49 favours Madison (p. 118–119, 125)
- [[cat-dog-fish-vocabulary]] (new) — three-word toy vocabulary illustrating one-hot, categorical and multinomial probabilities (p. 114–115)

## Bridges (candidates)
- [same-math] Laplace smoothing ↔ Bayesian statistics: posterior mean under a Dirichlet($\alpha$) prior adds $\alpha_j$ pseudo-counts (p. 123–125).
- [structural-analogy] Mixture model with observed $\pi_i$ ↔ supervised classification of documents by group (the book defers it to Ch. 19); unobserved $\pi$ ↔ clustering (Ch. 12).
- [metaphor] Pseudo-data shrinking sparse authors toward $\alpha/\alpha_0$ ↔ borrowing strength across units in hierarchical models of political data.

## Questions this raises
- The multinomial's variance is tied to its mean (6.1.4). How does real text, where word use clusters in documents, depart from this?
- How should $\alpha$ be chosen or learned, and how much does the answer depend on it for small authors like Jay?
- How can the model handle word order, which the bag of words ignores?
- With an unobserved $\pi$ (Ch. 12), what can the data tell us about the groups?

## Reading notes
- Printed page = pdf page (112–126).
- The text layer garbles equations; I checked them against the page images where possible. In (6.4.7) the denominator reads "$\alpha_0^3+\alpha_0$" in both the text layer and the page image. I wrote $\alpha_0^3+\alpha_0^2$ because it equals $\alpha_0^2(\alpha_0+1)$, as in (6.4.6); treat the exponent as my reconstruction.
- (6.4.8), the mode, is given with no condition on $\alpha_j$.
- p. 121 says Jay's $P(\text{man})$ becomes .02 after $\alpha=1$, but counts $(83,1,2)$ give $1/86\approx.012$. The p. 125 estimate $(.97,.01,.02)$ agrees with this arithmetic. The .008 is closer to what the rounded vector $(.97,.01,.02)$ gives (my arithmetic: $\approx.0086$) than to what the unrounded $(83,1,2)/86$ gives ($\approx.011$).
- The text writes the author subscripts as script letters ($\mathcal H$, $\mathcal J$, $\mathcal M$, the authors' initials); I keep script letters in LaTeX.
