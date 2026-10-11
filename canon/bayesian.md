---
field: Bayesian theory & modeling (with causal inference)
slug: bayesian
layer: foundation
compiled: 2026-10-11
---
# Bayesian theory & modeling (with causal inference) — Canon

## Scope
This catalog covers probability as a logic of uncertain reasoning and the craft of building, fitting and criticizing probabilistic models, plus a second, equally weighted strand on causal inference. The Bayesian half has five strands: foundations and history (Bayes, Laplace, Cox, Jaynes, subjective probability), applied data analysis and workflow (hierarchical models, priors, model checking), computation (MCMC, HMC, variational inference), Bayesian models of cognition, and the classic frequentist–Bayesian debates. The causal half covers both of its main languages: potential outcomes (Rubin, Holland, Imbens & Rubin, Hernán & Robins) and structural causal models / DAGs (Pearl), with Morgan & Winship as the sociology-facing synthesis. Savage's axiomatization and expected-utility theory belong to the decision-theory catalog and are only cross-referenced here (see Bridges). De Finetti is covered through the SEP survey because no legal free primary text could be verified. Generic ML textbooks are limited to MacKay and Murphy, and Bishop's PRML is left out to stay within the size limit. The list was triangulated against three syllabi: Andrew Heiss's Bayesian Statistics course (Georgia State, Fall 2022; McElreath + *Bayes Rules!*), Berkeley Stat 256 causal inference (Fall 2024; Hernán & Robins, Holland 1986, Ding), and the MIT/CBMM Computational Cognitive Science (9.660) reading list (Tenenbaum et al. 2011; Griffiths & Tenenbaum 2006).

## Canon

### Strand: Foundations — probability as extended logic, history, subjective probability

#### bayes-1763-essay
- **type:** paper
- **citation:** Bayes, T. [communicated by R. Price] (1763). *An Essay towards Solving a Problem in the Doctrine of Chances*. Philosophical Transactions of the Royal Society of London, 53, 370–418. DOI: 10.1098/rstl.1763.0053
- **tier:** reference
- **level:** UG
- **why:** This is the founding text. Bayes asks how to infer the unknown chance of an event from observed successes and failures, and answers with a "billiard table" thought experiment that amounts to a uniform prior on that chance. Price's preface frames the result as a tool for reasoning from effects back to causes. Read it for the original framing more than the mathematics.
- **focus:** Price's covering letter and the problem statement; the billiard-table construction
- **access:** free: https://www2.isye.gatech.edu/isyebayes/bank/Essay.pdf (public-domain transcription)
- **verified:** https://en.wikipedia.org/wiki/An_Essay_Towards_Solving_a_Problem_in_the_Doctrine_of_Chances (+ Crossref record for DOI 10.1098/rstl.1763.0053)

#### laplace-1902-essay
- **type:** book
- **citation:** Laplace, P.-S. (1902). *A Philosophical Essay on Probabilities* (F. W. Truscott & F. L. Emory, Trans., from the 6th French ed.). New York: John Wiley & Sons; London: Chapman & Hall.
- **tier:** reference
- **level:** UG
- **why:** Laplace independently rebuilt and generalized Bayes's result, and this non-technical essay is where he lays out probability as "common sense reduced to calculation." It covers inverse probability (the probability of causes), the principle of insufficient reason, and his famous deterministic "intelligence" (later called Laplace's demon). It is the bridge between Bayes's narrow problem and the modern view of probability as reasoning under ignorance.
- **focus:** whole (short)
- **access:** free: https://www.gutenberg.org/ebooks/58881
- **verified:** https://www.gutenberg.org/ebooks/58881

#### cox-1946-probability
- **type:** paper
- **citation:** Cox, R. T. (1946). *Probability, Frequency and Reasonable Expectation*. American Journal of Physics, 14(1), 1–13. DOI: 10.1119/1.1990764
- **tier:** deep
- **level:** grad
- **why:** Cox shows that any system for grading degrees of plausibility that meets a few common-sense consistency requirements has to obey the sum and product rules of probability. This is "Cox's theorem," the formal backbone of the view that Bayesian probability is the unique extension of logic to uncertainty. Jaynes's Chapter 2 rebuilds the argument, so read Cox for the original and Jaynes for the exposition.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1119/1.1990764

#### jaynes-2003-probability
- **type:** book
- **citation:** Jaynes, E. T. (2003). *Probability Theory: The Logic of Science* (G. L. Bretthorst, Ed.). Cambridge University Press.
- **tier:** core
- **level:** grad
- **why:** This is the most forceful statement of probability as extended logic. Jaynes imagines building a "reasoning robot," derives the rules of probability from desiderata of consistency, and then uses them to handle sampling, hypothesis testing, maximum-entropy priors and model comparison. It is polemical against "orthodox" statistics in a way that sharpens your intuition even where you disagree.
- **focus:** Ch. 1 Plausible reasoning; Ch. 2 The quantitative rules; Ch. 4 Elementary hypothesis testing; Ch. 5 Queer uses for probability theory; Ch. 11 Discrete prior probabilities: the entropy principle; Ch. 17 Principles and pathology of orthodox statistics; Ch. 20 Model comparison
- **access:** need-copy
- **verified:** https://assets.cambridge.org/97805215/92710/sample/9780521592710ws.pdf

#### mcgrayne-2011-theory
- **type:** book
- **citation:** McGrayne, S. B. (2011). *The Theory That Would Not Die: How Bayes' Rule Cracked the Enigma Code, Hunted Down Russian Submarines, and Emerged Triumphant from Two Centuries of Controversy*. New Haven: Yale University Press.
- **tier:** core
- **level:** HS
- **why:** This is the accessible on-ramp: a narrative history of Bayes's rule from Bayes and Laplace, through its banishment by the frequentists, to codebreaking, actuarial work, submarine search and modern computing. It explains why the debate became so heated and gives every later technical text a human context. Read it first.
- **focus:** whole
- **access:** need-copy
- **translation:** 『異端の統計学 ベイズ』 シャロン・バーチュ・マグレイン著, 冨永星訳, 草思社 (2013; 草思社文庫版 2018)
- **verified:** https://catalogue.bnf.fr/ark:/12148/cb43600838t (JP: https://www.kinokuniya.co.jp/f/dsg-01-9784794220011)

#### hajek-2002-interpretations
- **type:** website
- **citation:** Hájek, A. (2002; substantive revision 2023). *Interpretations of Probability*. In E. N. Zalta & U. Nodelman (Eds.), *Stanford Encyclopedia of Philosophy*.
- **tier:** reference
- **level:** UG
- **why:** This is the authoritative map of what "probability" can mean: classical, logical, subjective, frequency, propensity and best-system interpretations. It is the best legal free entry point to de Finetti's subjectivism and the Dutch Book argument, which says incoherent betting odds can be exploited for a sure loss. It also places Jaynes's objective Bayesianism in context.
- **focus:** §3.2 Logical/Evidential Probability; §3.3 Subjective Interpretation (esp. 3.3.2 The betting analysis and the Dutch Book argument; 3.3.5 Objective Bayesianism); §3.4 Frequency Interpretations
- **access:** free: https://plato.stanford.edu/entries/probability-interpret/
- **verified:** https://plato.stanford.edu/entries/probability-interpret/

### Strand: Debates — frequentist vs Bayesian, and what Bayesian practice really is

#### efron-1986-bayesian
- **type:** paper
- **citation:** Efron, B. (1986). *Why Isn't Everyone a Bayesian?* The American Statistician, 40(1), 1–5. DOI: 10.1080/00031305.1986.10475342
- **tier:** core
- **level:** UG
- **why:** One of the twentieth century's leading statisticians, and the inventor of the bootstrap, explains in five pages why Bayesian theory's coherence had not won over practitioners. His reasons include the difficulty of specifying priors, the appeal of "objective" procedures, and the convenience of frequentist tools. It is the classic short statement of the case for pragmatic frequentism. Read it alongside Jaynes's polemics and Gelman & Shalizi's reconciliation.
- **focus:** whole (short, with published comments)
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1080/00031305.1986.10475342

#### gelman-2013-philosophy
- **type:** paper
- **citation:** Gelman, A., & Shalizi, C. R. (2013). *Philosophy and the Practice of Bayesian Statistics*. British Journal of Mathematical and Statistical Psychology, 66(1), 8–38. DOI: 10.1111/j.2044-8317.2011.02037.x
- **tier:** deep
- **level:** grad
- **why:** The paper argues that successful Bayesian practice is not inductive "belief updating" but hypothetico-deductive: you fit a model, check it against data, and revise it, which is closer to Popper (and to Mayo's error statistics) than to subjectivism. It is essential for a social scientist who wants a defensible philosophy behind posterior predictive checks and model revision.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/1006.3868
- **verified:** https://arxiv.org/abs/1006.3868

### Strand: Bayesian data analysis & workflow

#### johnson-2022-bayesrules
- **type:** book
- **citation:** Johnson, A. A., Ott, M. Q., & Dogucu, M. (2022). *Bayes Rules! An Introduction to Applied Bayesian Modeling*. Chapman & Hall/CRC. DOI: 10.1201/9780429288340
- **tier:** deep
- **level:** UG
- **why:** This is the gentlest rigorous on-ramp, written for undergraduates. It moves from Bayes' rule for events, through conjugate Beta-Binomial models and MCMC "under the hood," to regression and hierarchical models. It was a required text alongside McElreath in the Georgia State syllabus used for triangulation. The full text is free online.
- **focus:** Part I Bayesian Foundations (Ch. 1–5); Ch. 7 MCMC under the Hood; Part IV Hierarchical Bayesian Models (Ch. 15–17)
- **access:** free: https://www.bayesrulesbook.com/
- **verified:** https://www.bayesrulesbook.com/ (+ Crossref 10.1201/9780429288340)

#### mcelreath-2020-rethinking
- **type:** book
- **citation:** McElreath, R. (2020). *Statistical Rethinking: A Bayesian Course with Examples in R and Stan* (2nd ed.). Chapman & Hall/CRC. DOI: 10.1201/9780429029608
- **tier:** core
- **level:** UG
- **why:** This is the best book for building modeling intuition. It treats models as "golems," builds everything from simulation, and weaves causal DAGs into regression from the start, so confounding, colliders and post-treatment bias are part of the Bayesian workflow and not an afterthought. The free 20-lecture video course (CC0 materials) is canonical in its own right, and there are community translations of the code into Python (PyMC, NumPyro).
- **focus:** Ch. 1 The Golem of Prague; Ch. 2 Small Worlds and Large Worlds; Ch. 4 Geocentric Models; Ch. 5 The Many Variables & The Spurious Waffles; Ch. 6 The Haunted DAG & The Causal Terror; Ch. 7 Ulysses' Compass; Ch. 9 Markov Chain Monte Carlo; Ch. 13 Models With Memory; Ch. 14 Adventures in Covariance
- **access:** need-copy (book). Free sample Ch. 1–2: https://xcelab.net/rmpubs/sr2/statisticalrethinking2_chapters1and2.pdf. Free lectures, slides and homework: https://github.com/rmcelreath/stat_rethinking_2024
- **verified:** https://www.routledge.com/Statistical-Rethinking-A-Bayesian-Course-with-Examples-in-R-and-STAN/McElreath/p/book/9780367139919 (+ https://xcelab.net/rm/)

#### gelman-2013-bda3
- **type:** book
- **citation:** Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). Chapman & Hall/CRC. DOI: 10.1201/b16018
- **tier:** core
- **level:** grad
- **why:** This is the standard graduate reference for applied Bayesian statistics. It codifies the "three steps" (build a full probability model, condition on data, evaluate fit) and makes hierarchical (multilevel) models and posterior predictive checking central. Its later chapters are the reference for computation, regression, missing data, Gaussian processes and mixtures. The authors post a free PDF for non-commercial use.
- **focus:** Ch. 1 Probability and inference; Ch. 2 Single-parameter models; Ch. 5 Hierarchical models; Ch. 6 Model checking; Ch. 7 Evaluating, comparing, and expanding models; Ch. 8 Modeling accounting for data collection; Ch. 11 Basics of Markov chain simulation
- **access:** free: https://sites.stat.columbia.edu/gelman/book/BDA3.pdf
- **verified:** https://sites.stat.columbia.edu/gelman/book/ (+ Crossref 10.1201/b16018)

#### gelman-2020-workflow
- **type:** paper
- **citation:** Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., Kennedy, L., Gabry, J., Bürkner, P.-C., & Modrák, M. (2020). *Bayesian Workflow*. arXiv:2011.01808.
- **tier:** core
- **level:** grad
- **why:** The paper reframes Bayesian statistics from "compute the posterior" to an iterative process: prior predictive checks, fake-data simulation, computational diagnostics, model expansion and comparison, and dealing with many models at once. It is the modern statement of how Stan-era practitioners actually work, and the most directly useful item for Kunhao's own empirical modeling.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/2011.01808
- **verified:** https://arxiv.org/abs/2011.01808

### Strand: Computation — MCMC, HMC, variational inference

#### robert-2011-mcmc
- **type:** paper
- **citation:** Robert, C., & Casella, G. (2011). *A Short History of Markov Chain Monte Carlo: Subjective Recollections from Incomplete Data*. Statistical Science, 26(1), 102–115. DOI: 10.1214/10-STS351
- **tier:** deep
- **level:** grad
- **why:** The paper traces MCMC from the 1953 Metropolis algorithm at Los Alamos, through Hastings and the Gibbs sampler, to the 1990 Gelfand–Smith paper that turned Bayesian statistics into a practical discipline. It is the best single guide to the primary computational papers and shows why computation, more than philosophy, ended the Bayesian "winter."
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/0808.2902
- **verified:** https://arxiv.org/abs/0808.2902 (+ Crossref 10.1214/10-STS351)

#### betancourt-2017-hmc
- **type:** paper
- **citation:** Betancourt, M. (2017). *A Conceptual Introduction to Hamiltonian Monte Carlo*. arXiv:1701.02434 (v2, 2018).
- **tier:** deep
- **level:** grad
- **why:** This is the clearest geometric explanation of why random-walk samplers fail in high dimensions (concentration of measure and the "typical set") and how Hamiltonian dynamics let a sampler glide along that set. HMC/NUTS is the engine inside Stan and PyMC, and this paper turns divergences and other diagnostics from mysterious warnings into interpretable signals.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/1701.02434
- **verified:** https://arxiv.org/abs/1701.02434

#### blei-2017-variational
- **type:** paper
- **citation:** Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). *Variational Inference: A Review for Statisticians*. Journal of the American Statistical Association, 112(518), 859–877. DOI: 10.1080/01621459.2017.1285773
- **tier:** core
- **level:** grad
- **why:** The review explains the alternative to sampling: turn inference into optimization by finding the member of a tractable family closest (in KL divergence) to the posterior, which means maximizing the ELBO. It covers mean-field coordinate ascent and stochastic VI, and it is the conceptual link to topic models, VAEs and much of modern probabilistic deep learning.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/1601.00670
- **verified:** https://arxiv.org/abs/1601.00670 (+ Crossref 10.1080/01621459.2017.1285773)

#### mackay-2003-information
- **type:** book
- **citation:** MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.
- **tier:** deep
- **level:** grad
- **why:** A physicist's unification of information theory, Bayesian inference and neural networks, with famously intuitive exercises. Its treatment of the Bayesian Occam's razor (why the marginal likelihood automatically penalizes over-flexible models) and its Monte Carlo and variational chapters are classics. It is the natural bridge text to the AI4Read information-theory canon. CUP allows free on-screen viewing of the PDF.
- **focus:** Ch. 2 Probability, Entropy, and Inference; Ch. 3 More about Inference; Ch. 28 Model Comparison and Occam's Razor; Monte Carlo Methods (Ch. 29); Ch. 30 Efficient Monte Carlo Methods; Ch. 33 Variational Methods; Ch. 37 Bayesian Inference and Sampling Theory
- **access:** free: https://www.inference.org.uk/itprnn/book.pdf
- **verified:** https://www.inference.org.uk/itprnn/book.pdf (title page: "Cambridge University Press 2003. On-screen viewing permitted.")

#### murphy-2023-pml2
- **type:** book
- **citation:** Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
- **tier:** reference
- **level:** grad
- **why:** This is the encyclopedic modern reference connecting Bayesian inference to machine learning. It has chapters on inference algorithms, variational inference, MCMC, Bayesian neural networks, generative models and causality, all in one consistent notation with Python (JAX) code. Use it as a lookup, not a cover-to-cover read. The author posts a free draft PDF (CC BY-NC-ND).
- **focus:** Ch. 7 Inference algorithms: an overview; Ch. 10 Variational inference; Ch. 12 Markov chain Monte Carlo; Ch. 36 Causality
- **access:** free: https://github.com/probml/pml2-book/releases/latest/download/book2.pdf
- **verified:** https://probml.github.io/pml-book/book2.html

### Strand: Bayesian models of cognition

#### griffiths-2006-optimal
- **type:** paper
- **citation:** Griffiths, T. L., & Tenenbaum, J. B. (2006). *Optimal Predictions in Everyday Cognition*. Psychological Science, 17(9), 767–773. DOI: 10.1111/j.1467-9280.2006.01780.x
- **tier:** deep
- **level:** UG
- **why:** People were asked to predict totals from partial information, such as a movie's final gross from its earnings so far or a man's lifespan from his current age. Their median predictions closely matched optimal Bayesian predictions under the real-world prior distributions. This is the cleanest demonstration that everyday intuition embodies accurate priors, and that the form of the prior (power-law vs Gaussian vs Erlang) shapes judgment.
- **focus:** whole (short)
- **access:** free: https://cocosci.princeton.edu/tom/papers/predictions.pdf
- **verified:** https://cocosci.princeton.edu/publications.php (+ Crossref 10.1111/j.1467-9280.2006.01780.x)

#### tenenbaum-2011-grow
- **type:** paper
- **citation:** Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). *How to Grow a Mind: Statistics, Structure, and Abstraction*. Science, 331(6022), 1279–1285. DOI: 10.1126/science.1192788
- **tier:** core
- **level:** UG
- **why:** This is the manifesto of the "reverse-engineering" program. It asks how minds learn so much from so little data and answers with Bayesian inference over structured representations (graphs, grammars, programs), hierarchical models that learn their own priors ("learning to learn"), and nonparametric models that grow in complexity. It is the opening reading of MIT 9.660.
- **focus:** whole
- **access:** free: https://cocosci.princeton.edu/tom/papers/LabPublications/GrowMind.pdf
- **verified:** https://cbmm.mit.edu/lh-computational-cognitive-science-readings (+ Crossref 10.1126/science.1192788)

#### griffiths-2024-bayesian
- **type:** book
- **citation:** Griffiths, T. L., Chater, N., & Tenenbaum, J. B. (2024). *Bayesian Models of Cognition: Reverse Engineering the Mind*. Cambridge, MA: MIT Press. ISBN 9780262049412.
- **tier:** deep
- **level:** grad
- **why:** This is the field's definitive textbook, written by its three leading figures. Part I builds up the mathematics (Bayesian inference, graphical models, hierarchical and nonparametric models, sampling) with psychological examples. Part II covers advanced applications and also critiques of the reverse-engineering approach. It consolidates two decades of papers into one coherent framework.
- **focus:** Part I (core mathematical ideas); then Part II selectively, including the critique chapters
- **access:** need-copy
- **verified:** https://ci.nii.ac.jp/ncid/BD05660115 (+ https://tenlong.com.tw/products/9780262049412)

### Strand: Causal inference

#### rubin-1974-estimating
- **type:** paper
- **citation:** Rubin, D. B. (1974). *Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies*. Journal of Educational Psychology, 66(5), 688–701. DOI: 10.1037/h0037350
- **tier:** deep
- **level:** grad
- **why:** This is the founding paper of the modern potential-outcomes framework, often called the Rubin Causal Model. A causal effect is defined as the difference between the outcomes a unit would have under treatment and under control, and the paper asks when nonrandomized data can still estimate it. Everything in Imbens & Rubin and Hernán & Robins builds on this definition.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1037/h0037350

#### holland-1986-statistics
- **type:** paper
- **citation:** Holland, P. W. (1986). *Statistics and Causal Inference*. Journal of the American Statistical Association, 81(396), 945–960. DOI: 10.1080/01621459.1986.10478354
- **tier:** core
- **level:** UG
- **why:** This is the canonical exposition of the potential-outcomes view. It names the "Fundamental Problem of Causal Inference" (we never observe both potential outcomes for the same unit) and popularizes the slogan "no causation without manipulation." It contrasts this view with philosophical accounts of causation and is required reading in Berkeley's Stat 256.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1080/01621459.1986.10478354 (syllabus: https://stat156.berkeley.edu/fall-2024/stat256-syllabus.pdf)

#### pearl-2009-causality
- **type:** book
- **citation:** Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press. DOI: 10.1017/CBO9780511803161
- **tier:** deep
- **level:** grad
- **why:** This is the treatise behind structural causal models. It covers causal Bayesian networks, d-separation, the do-operator and do-calculus, identification criteria (back-door and front-door), structural counterfactuals and the probability of causation. It won the 2001 Lakatos Award, and it is the mathematical source for everything popularized in the Primer and *The Book of Why*.
- **focus:** Ch. 1 Introduction to Probabilities, Graphs, and Causal Models; Ch. 3 Causal Diagrams and the Identification of Causal Effects; Ch. 5 Causality and Structural Models in Social Science and Economics; Ch. 6 Simpson's Paradox, Confounding, and Collapsibility; Ch. 7 The Logic of Structure-Based Counterfactuals; Epilogue "The Art and Science of Cause and Effect"
- **access:** need-copy (Epilogue free from the author: https://bayes.cs.ucla.edu/BOOK-2K/causality2-epilogue.pdf)
- **translation:** 『統計的因果推論 ―モデル・推論・推測―』 黒木学訳, 共立出版 (2009) — a translation of the 1st edition (2000)
- **verified:** https://bayes.cs.ucla.edu/BOOK-2K/ (TOC: https://bayes.cs.ucla.edu/BOOK-09/book-toc-final.pdf; Crossref 10.1017/CBO9780511803161)

#### pearl-2016-primer
- **type:** book
- **citation:** Pearl, J., Glymour, M., & Jewell, N. P. (2016). *Causal Inference in Statistics: A Primer*. Chichester: Wiley.
- **tier:** core
- **level:** UG
- **why:** This is the compact (about 130-page) textbook version of Pearl's framework, written for students who know basic statistics. It covers Simpson's paradox, chains, forks and colliders, d-separation, interventions and the adjustment formula, the back-door and front-door criteria, mediation and counterfactuals, with exercises. It is the fastest route to working fluency with DAGs.
- **focus:** whole (4 chapters): Ch. 1 Preliminaries: Statistical and Causal Models; Ch. 2 Graphical Models and Their Applications; Ch. 3 The Effects of Interventions; Ch. 4 Counterfactuals and Their Applications
- **access:** need-copy (the author posts Ch. 1–2 in full: https://bayes.cs.ucla.edu/PRIMER/primer-ch1.pdf, https://bayes.cs.ucla.edu/PRIMER/primer-ch2.pdf)
- **translation:** 『入門 統計的因果推論』 落海浩訳, 朝倉書店 (2019)
- **verified:** https://bayes.cs.ucla.edu/PRIMER/ (TOC: https://bayes.cs.ucla.edu/PRIMER/primer-toc.pdf)

#### pearl-2018-bookofwhy
- **type:** book
- **citation:** Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. New York: Basic Books.
- **tier:** core
- **level:** HS
- **why:** This is the popular on-ramp to causal inference. Its organizing idea is the "Ladder of Causation" (association → intervention → counterfactuals): data alone cannot climb the ladder without a causal model. The book also tells the history of path analysis, the smoking–cancer controversy and causal paradoxes, so it gives strong intuitions before the formal Primer. It is opinionated about statistics' history, so read it with Holland and Imbens & Rubin as a counterweight.
- **focus:** whole
- **access:** need-copy
- **translation:** 『因果推論の科学 「なぜ?」の問いにどう答えるか』 夏目大訳, 松尾豊監修・解説, 文藝春秋 (2022)
- **verified:** https://bayes.cs.ucla.edu/WHY/ (JP: https://ja.wikipedia.org/wiki/ジューディア・パール)

#### imbens-2015-causal
- **type:** book
- **citation:** Imbens, G. W., & Rubin, D. B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction*. Cambridge University Press. DOI: 10.1017/CBO9781139025751
- **tier:** deep
- **level:** grad
- **why:** This is the definitive potential-outcomes textbook. It is built around assignment mechanisms: randomized experiments analyzed via Fisher, Neyman, regression and Bayesian model-based approaches, then observational studies under unconfoundedness with propensity scores, overlap, matching and trimming. Pearl's framework starts from graphs; this one starts from the design of the study. Imbens shared the 2021 economics Nobel for this tradition.
- **focus:** Part I (Ch. 1 Causality: The Basic Framework; Ch. 2 A Brief History of the Potential Outcomes Approach; Ch. 3 A Classification of Assignment Mechanisms); Ch. 5 Fisher's Exact P-Values; Ch. 6 Neyman's Repeated Sampling Approach; Ch. 8 Model-Based Inference; Ch. 12 Unconfounded Treatment Assignment; Ch. 13 Estimating the Propensity Score
- **access:** need-copy
- **verified:** https://www.cambridge.org/core/books/causal-inference-for-statistics-social-and-biomedical-sciences/71126BE90C58F1A431FE9B2DD07938AB

#### hernan-2020-whatif
- **type:** book
- **citation:** Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Boca Raton: Chapman & Hall/CRC.
- **tier:** core
- **level:** UG
- **why:** This is the clearest modern textbook that unifies potential outcomes with causal DAGs. It moves from the definition of a causal effect through confounding, selection and measurement bias, to IP weighting, the g-formula, g-estimation and time-varying treatments. Its "target trial emulation" idea (design the observational analysis as if it were a randomized trial) is now standard practice. The authors keep it free and updated online, and it is a core text at Berkeley.
- **focus:** Part I Causal inference without models (Ch. 1 A definition of causal effect through Ch. 10, esp. Ch. 6 Graphical representation of causal effects; Ch. 7 Confounding; Ch. 8 Selection bias); Part II Ch. 12 IP weighting and marginal structural models; Ch. 13 Standardization and the parametric g-formula; Part III Ch. 22 Target trial emulation
- **access:** free: https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf (the link changes with each revision; landing page https://miguelhernan.org/whatifbook)
- **verified:** https://miguelhernan.org/whatifbook

#### morgan-2014-counterfactuals
- **type:** book
- **citation:** Morgan, S. L., & Winship, C. (2014). *Counterfactuals and Causal Inference: Methods and Principles for Social Research* (2nd ed.). Cambridge University Press, Analytical Methods for Social Research. DOI: 10.1017/CBO9781107587991 (often cited as 2015)
- **tier:** reference
- **level:** grad
- **why:** This is the causal-inference synthesis written by and for sociologists. It uses both potential outcomes and causal graphs, then covers matching, regression, weighting, instrumental variables, mechanisms, panel data and partial identification, with social-science examples throughout. It is the closest fit to Kunhao's own disciplinary audience and the best guide to what regression coefficients in observational social research do and don't mean.
- **focus:** Ch. 1 Introduction; Ch. 2 Counterfactuals and the Potential Outcome Model; Ch. 3 Causal Graphs; Ch. 4 Models of Causal Exposure and Identification Criteria for Conditioning Estimators; Ch. 6 Regression Estimators of Causal Effects; Ch. 10 Mechanisms and Causal Explanation
- **access:** need-copy
- **verified:** https://www.cambridge.org/core/books/counterfactuals-and-causal-inference/5CC81E6DF63C5E5A8B88F79D45E1D1B7

## Concept spine
- **Bayes' theorem** — posterior ∝ likelihood × prior; how to turn P(data | hypothesis) into P(hypothesis | data) (HS)
- **Prior distribution** — what you believe about an unknown before seeing the current data, written as a probability distribution (UG)
- **Likelihood** — how probable the observed data are under each possible parameter value; a function of the parameter, not a probability over it (UG)
- **Posterior distribution** — updated beliefs about unknowns after conditioning on data; the full answer in Bayesian inference (UG)
- **Marginal likelihood (evidence)** — probability of the data averaged over the prior; the normalizing constant and the basis of model comparison (grad)
- **Base-rate neglect** — ignoring the prior (base rate) when judging the probability of a hypothesis from evidence, e.g., a positive medical test (HS)
- **Probability as extended logic** — probability as the unique consistent calculus of plausibility, generalizing true/false to degrees (Cox, Jaynes) (UG)
- **Cox's theorem** — consistency requirements on plausible reasoning force the sum and product rules (grad)
- **Subjective (personal) probability** — probability as a coherent degree of belief of an agent, measurable through betting (de Finetti) (UG)
- **Dutch book argument** — degrees of belief that violate probability axioms can be exploited by bets that guarantee a loss (UG)
- **Exchangeability** — a sequence whose joint distribution is unchanged under reordering; de Finetti's theorem says such sequences behave as i.i.d. given a latent parameter (grad)
- **Principle of indifference / maximum entropy** — with no information, spread probability evenly; more generally, choose the least-committal distribution consistent with constraints (grad)
- **Conjugate prior** — a prior family that yields a posterior in the same family (e.g., Beta–Binomial), giving closed-form updating (UG)
- **Sequential updating** — today's posterior is tomorrow's prior; the order of data doesn't matter (UG)
- **Posterior predictive distribution** — the distribution of new data averaging over posterior uncertainty in parameters (UG)
- **Credible interval** — an interval containing the parameter with a stated posterior probability, unlike a confidence interval's long-run coverage (UG)
- **Hierarchical (multilevel) model** — parameters for groups are themselves drawn from a population distribution, learned from data (UG)
- **Partial pooling / shrinkage** — group estimates are pulled toward the overall mean in proportion to how noisy they are (UG)
- **Prior predictive check** — simulate data from the prior to see whether the model's assumptions produce plausible data (grad)
- **Posterior predictive check** — compare replicated data from the fitted model with observed data to find misfit (grad)
- **Bayesian workflow** — the iterative cycle of model building, fake-data simulation, fitting, diagnosing, checking and expanding (grad)
- **Bayesian Occam's razor** — the marginal likelihood automatically penalizes models that spread probability over too many possible datasets (grad)
- **Cross-validation / LOO / WAIC** — estimating out-of-sample predictive accuracy to compare models without overfitting (grad)
- **Monte Carlo integration** — approximating expectations by averaging over random samples (UG)
- **Markov chain Monte Carlo (MCMC)** — constructing a random walk whose long-run distribution is the posterior, so its states are posterior samples (grad)
- **Metropolis–Hastings** — propose a move and accept it with a probability ratio that keeps the target distribution invariant (grad)
- **Gibbs sampling** — MCMC that updates one variable at a time from its full conditional distribution (grad)
- **Hamiltonian Monte Carlo (HMC/NUTS)** — uses gradients and simulated physics to make long, efficient moves through the typical set (grad)
- **Typical set** — the thin region of high-dimensional space where most probability mass actually lives, away from the mode (grad)
- **Convergence diagnostics (R-hat, ESS, divergences)** — checks that chains have mixed and that the sampler explored the posterior faithfully (grad)
- **Variational inference & ELBO** — approximate the posterior by optimizing a simpler distribution to maximize a lower bound on log evidence (grad)
- **KL divergence** — an asymmetric measure of how one distribution differs from another; the objective VI minimizes (grad)
- **Rational analysis / computational level** — explain cognition as the optimal solution to the problem the mind faces, given its environment (UG)
- **Learning to learn (overhypotheses)** — hierarchical models that learn abstract priors which then speed up learning of specific cases (grad)
- **Frequentist vs Bayesian inference** — probability as long-run frequency of procedures vs probability as degree of belief about unknowns (UG)
- **Potential outcomes** — each unit has an outcome under each possible treatment; a causal effect is their difference (UG)
- **Fundamental problem of causal inference** — for any unit we observe at most one potential outcome, so causal inference is a missing-data problem (UG)
- **Assignment mechanism / ignorability** — the process deciding who gets treated; if it is independent of potential outcomes given covariates, effects are identifiable (grad)
- **SUTVA** — one unit's treatment doesn't affect another's outcome and there is only one version of each treatment (grad)
- **Structural causal model (SCM)** — a set of equations, one per variable, each determined by its direct causes plus noise (grad)
- **Causal DAG** — a directed acyclic graph encoding qualitative causal assumptions about which variables affect which (UG)
- **Fork, chain, collider** — the three elementary path structures; conditioning on a collider *opens* a spurious path (UG)
- **d-separation** — a graphical rule that reads off which conditional independences a DAG implies (grad)
- **do-operator** — P(Y | do(X=x)), the distribution under intervention, as opposed to passive observation P(Y | X=x) (UG)
- **Back-door / front-door criterion** — graphical conditions telling which variables to adjust for to identify a causal effect (grad)
- **Ladder of causation** — association, intervention and counterfactual reasoning as strictly increasing levels of causal knowledge (HS)
- **Propensity score** — the probability of treatment given covariates; balancing on it removes measured confounding (grad)
- **Confounding vs selection bias** — bias from common causes of treatment and outcome vs bias from conditioning on common effects (UG)
- **Target trial emulation** — design an observational analysis by explicitly specifying the randomized trial it is trying to mimic (grad)
- **Simpson's paradox** — an association that reverses when data are split by a third variable; only causal assumptions say which answer to trust (HS)

## Canonical instances
- **Bayes's billiard table** — a ball is rolled to fix an unknown chance, then further balls test it; the original uniform-prior inference about a probability — bayes-1763-essay
- **The sunrise problem / rule of succession** — after n successes in n trials, how probable is the next? Laplace's (n+1)/(n+2) answer and its critics — laplace-1902-essay (and jaynes-2003-probability Ch. 18)
- **Jaynes's reasoning robot** — design a machine that reasons consistently under uncertainty, and the rules of probability fall out — jaynes-2003-probability
- **Turing and the Enigma; searching for lost submarines** — Bayes in the field: weighing evidence in codebreaking and updating search maps as areas come up empty — mcgrayne-2011-theory
- **Fake-news exclamation points** — Bayes' rule for events: how much should a "!" in the title raise the probability that an article is fake? — johnson-2022-bayesrules (Ch. 2)
- **Globe tossing** — estimate the proportion of water on Earth by tossing an inflatable globe, the "garden of forking data" and grid approximation — mcelreath-2020-rethinking (Ch. 2)
- **Waffle Houses and divorce** — a spurious state-level correlation used to teach confounding and multiple regression — mcelreath-2020-rethinking (Ch. 5)
- **Eight schools** — coaching effects in eight schools: the textbook demonstration of hierarchical partial pooling between "no pooling" and "complete pooling" — gelman-2013-bda3 (Ch. 5)
- **HMC as an orbiting satellite** — a sampler without momentum falls into the mode, and one with too much flies off; HMC is like putting a satellite into a stable orbit around the typical set — betancourt-2017-hmc
- **Everyday predictions** — predicting a movie's total gross, a lifespan or a pharaoh's reign from partial data; people match Bayes with real-world priors — griffiths-2006-optimal
- **Learning "tufa" from three examples** — children and adults generalize a new word from a handful of examples, showing strong structured priors — tenenbaum-2011-grow
- **Simpson's paradox and Berkeley admissions** — a treatment or admission pattern reverses when stratified; the causal graph decides which table is right — pearl-2016-primer (§1.2)
- **Smoking, tar and lung cancer (front-door)** — identifying an effect despite unmeasured confounding by going through a fully mediating variable — pearl-2016-primer (§3.4); pearl-2018-bookofwhy
- **"No causation without manipulation"** — why attributes like race or sex fit uneasily as "causes" in the potential-outcomes framework — holland-1986-statistics
- **LaLonde-type job-training evaluation** — an experimental labor-market program used as a benchmark for observational methods — imbens-2015-causal (Ch. 11)

## Bridges
- [same-math] variational inference / log evidence ↔ information theory: KL divergence & code length — log p(D) = ELBO + KL(q‖posterior), and −log p is a code length (MacKay's unifying theme)
- [same-math] maximum-entropy priors ↔ information theory: Shannon entropy — Jaynes's MaxEnt maximizes exactly Shannon's H subject to constraints
- [same-math] Bayesian decision theory ↔ decision & game theory: Savage expected utility — choose the action minimizing posterior expected loss; Savage's axioms justify the same subjective-probability-plus-utility representation
- [same-math] Gaussian prior + linear likelihood ↔ linear algebra: ridge regression / precision matrices — the MAP estimate is ridge regression; posterior precision = prior precision + XᵀX/σ²
- [same-math] Metropolis/Gibbs sampling ↔ complex systems: Ising model & Boltzmann distribution — MCMC was invented to sample statistical-mechanics systems; simulated annealing is the same algorithm with a temperature schedule
- [same-math] ELBO ↔ LLMs: variational autoencoders and likelihood training — VAEs maximize the ELBO, and next-token cross-entropy is negative log-likelihood (MLE, i.e., MAP with a flat prior)
- [structural-analogy] Bayesian models of cognition (inverse planning) ↔ theory of mind: mentalizing as inference — attributing goals and beliefs is modeled as Bayesian inversion of a rational-action model
- [structural-analogy] Bayesian confirmation & model checking ↔ analytic philosophy: induction vs falsification — Gelman & Shalizi recast Bayesian practice as hypothetico-deductive (Popper/Mayo), not Humean induction
- [structural-analogy] belief updating with source reliability ↔ communication theory: persuasion, framing & misinformation correction — messages act as evidence whose likelihoods depend on perceived source credibility
- [same-math] instrumental variables & potential outcomes ↔ economics & finance / political science: identification strategies — the IV/LATE, matching and regression-adjustment estimators are literally the same estimands used in econometrics and causal political science
