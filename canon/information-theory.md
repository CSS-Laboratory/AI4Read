---
field: Information theory
slug: information-theory
layer: foundation
compiled: 2026-10-11
---
# Information theory — Canon

## Scope
This catalog covers five strands: (1) Shannon's theory proper (entropy, mutual information, source coding, channel capacity, rate–distortion); (2) relative entropy (KL divergence), cross-entropy and the basics of information geometry, including the information bottleneck; (3) algorithmic information (Kolmogorov complexity) and the Minimum Description Length principle; (4) maximum entropy as a rule of inference (Jaynes), with Landauer's link between information and physics; and (5) information theory applied to language, cognition, networks and economics. It leaves out heavy coding theory (LDPC and polar codes), network/multi-user information theory and quantum information, except where they appear inside the core textbooks. Syllabi used for triangulation: MIT 6.441 (Polyanskiy, Spring 2016), Stanford EE376A (Weissman, Winter 2018–19) and R. Futrell's "Information-Theoretic Approaches to Linguistics" (UC Davis, summer 2019). The two engineering syllabi anchor on Cover & Thomas. The linguistics syllabus anchors on Gleick Ch. 7, Shannon 1951 and the efficiency literature.

## Canon

### Strand: Shannon's theory and on-ramps

#### shannon-1948-mathematical
- **type:** paper
- **citation:** Shannon, C. E. (1948). *A Mathematical Theory of Communication*. Bell System Technical Journal, 27(3), 379–423 and 27(4), 623–656. DOI 10.1002/j.1538-7305.1948.tb01338.x (Part 1); 10.1002/j.1538-7305.1948.tb00917.x (Part 2).
- **tier:** core
- **level:** UG
- **why:** This is the founding document. It defines information as reduction of uncertainty (entropy), separates the source from the channel, and proves that error-free communication is possible at any rate below capacity. Its "approximations to English" (random text generated from letter and word statistics) are an ancestor of n-gram and neural language models.
- **focus:** Part I (Discrete Noiseless Systems: entropy, the approximations to English, source coding); Part II (The Discrete Channel with Noise: equivocation, capacity, the fundamental theorem). Part V (The Rate for a Continuous Source) introduces rate–distortion; skim Part IV (The Continuous Channel) on a first pass.
- **access:** free: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
- **verified:** https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication ; https://api.crossref.org/works/10.1002/j.1538-7305.1948.tb01338.x

#### shannon-1949-mathematical-theory
- **type:** book
- **citation:** Shannon, C. E., & Weaver, W. (1949). *The Mathematical Theory of Communication*. University of Illinois Press (paperback 1963).
- **tier:** deep
- **level:** UG
- **why:** The book reprints Shannon 1948 with an introductory essay by Weaver for general readers. Weaver's essay is where communication studies picked up the "Shannon–Weaver model" and his three levels of communication problems (technical, semantic, effectiveness). For a communication scholar it shows exactly where the engineering theory stops and the metaphor begins.
- **focus:** Weaver's introductory essay; the Shannon paper itself is covered by shannon-1948-mathematical.
- **access:** need-copy
- **translation:** 『通信の数学的理論』 クロード・E・シャノン, ワレン・ウィーバー著, 植松友彦訳, ちくま学芸文庫 (筑摩書房), 2009.
- **verified:** https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication ; https://chikumashobo.co.jp/product/9784480092229/

#### pierce-1980-introduction
- **type:** book
- **citation:** Pierce, J. R. (1980). *An Introduction to Information Theory: Symbols, Signals and Noise* (2nd rev. ed.). Dover Publications. xii + 305 pp. (First published as *Symbols, Signals and Noise*, 1961.)
- **tier:** core
- **level:** HS
- **why:** Pierce was Shannon's colleague at Bell Labs. He explains entropy, coding, channel capacity and the limits of the theory with almost no formulas, and he is careful about what "information" does *not* mean (meaning, value). It is the classic first read for building intuition before the mathematics.
- **focus:** whole
- **access:** need-copy
- **verified:** https://ci.nii.ac.jp/ncid/BA0391560X ; https://www.dsprelated.com/books/408.php

#### stone-2022-information
- **type:** book
- **citation:** Stone, J. V. (2022). *Information Theory: A Tutorial Introduction* (2nd ed.). Sebtel Press. ISBN 9781739672706. (1st ed. 2015.)
- **tier:** core
- **level:** UG
- **why:** A worked-example on-ramp written by a University of Sheffield psychologist. It is rigorous but gentle, and it bridges Pierce's prose and Cover & Thomas's proofs. The 2nd edition adds chapters on rate–distortion theory and transfer entropy, the latter relevant for information flow between time series (e.g., between media and public attention).
- **focus:** whole. Start with the author's free condensed tutorial (arXiv:1802.05968), which follows the book's arc.
- **access:** need-copy (free condensed version by the author: https://arxiv.org/pdf/1802.05968)
- **verified:** https://it.mathworks.com/academia/books/information-theory-stone.html ; https://arxiv.org/abs/1802.05968v1

#### gleick-2011-information
- **type:** book
- **citation:** Gleick, J. (2011). *The Information: A History, a Theory, a Flood*. Pantheon. ISBN 9780375423727.
- **tier:** deep
- **level:** HS
- **why:** A narrative history running from talking drums and the telegraph to Shannon, Kolmogorov and the information flood. It gives the cultural and intellectual context the textbooks skip. Futrell's information-theoretic linguistics course assigns its Shannon chapter (Ch. 7) as the introduction.
- **focus:** Ch. 7 (the Shannon chapter, as assigned in Futrell's syllabus); then the rest as leisure reading.
- **access:** need-copy
- **translation:** 『インフォメーション―情報技術の人類史―』 ジェイムズ・グリック著, 楡井浩一訳, 新潮社, 2013.
- **verified:** https://www.tenlong.com.tw/products/9780375423727 ; https://www.shinchosha.co.jp/book/506411/ ; https://sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/

#### cover-2006-elements
- **type:** book
- **citation:** Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience. ISBN 9780471241959.
- **tier:** core
- **level:** grad
- **why:** The standard graduate textbook, used or recommended by both the MIT 6.441 and Stanford EE376A syllabi. Its coverage is unusually broad for a social scientist: gambling, statistics, maximum entropy, Kolmogorov complexity and portfolio theory each get a chapter. The precise definitions and inequalities here are what you cite in papers.
- **focus:** Ch. 2 (Entropy, Relative Entropy, and Mutual Information), 3 (AEP), 5 (Data Compression), 6 (Gambling and Data Compression), 7 (Channel Capacity), 10 (Rate Distortion Theory), 11 (Information Theory and Statistics), 12 (Maximum Entropy), 14 (Kolmogorov Complexity), 16 (Information Theory and Portfolio Theory).
- **access:** need-copy
- **translation:** 『情報理論 基礎と広がり』 T.M.カバー, J.A.トーマス著, 山本博資・古賀弘樹・有村光晴ほか訳, 共立出版, 2012.
- **verified:** https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0471241954,descCd-tableOfContents.html ; https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/syllabus/ ; https://www.maruzenjunkudo.co.jp/products/9784320123007

#### mackay-2003-information
- **type:** book
- **citation:** MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. ISBN 9780521642989.
- **tier:** core
- **level:** UG
- **why:** It unites information theory with Bayesian inference and machine learning, which is the best fit for a computational social scientist. MacKay teaches through puzzles and exercises, and the book is free to view on screen from the author's site. His Cambridge course lecture videos accompany it: https://www.inference.org.uk/itprnn_lectures/
- **focus:** Ch. 1 (Introduction to Information Theory), 2 (Probability, Entropy, and Inference), 4 (The Source Coding Theorem), 5 (Symbol Codes), 6 (Stream Codes), 8 (Dependent Random Variables), 9 (Communication over a Noisy Channel), 10 (The Noisy-Channel Coding Theorem), 28 (Model Comparison and Occam's Razor), 33 (Variational Methods).
- **access:** free: https://www.inference.org.uk/itprnn/book.pdf
- **verified:** https://www.inference.org.uk/itprnn/book.html

#### polyanskiy-2025-information
- **type:** book
- **citation:** Polyanskiy, Y., & Wu, Y. (2025). *Information Theory: From Coding to Learning* (1st ed.). Cambridge University Press. DOI 10.1017/9781108966351.
- **tier:** reference
- **level:** grad
- **why:** The modern graduate treatment, grown out of MIT 6.441. It pairs classical Shannon theory with f-divergences, variational characterizations and statistical learning (hypothesis testing, minimax lower bounds). Use it to look up a rigorous modern statement of a result.
- **focus:** Part I (Information measures: Ch. 1 Entropy, 2 Divergence, 3 Mutual information); Part VI (Statistical applications) for learning-theory links.
- **access:** free: https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf (authors' prepublication version, free for personal use)
- **verified:** https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf ; https://api.crossref.org/works/10.1017/9781108966351

#### 3blue1brown-2022-wordle
- **type:** video
- **citation:** 3Blue1Brown [G. Sanderson] (2022, Feb 6). *Solving Wordle using information theory*. YouTube / 3blue1brown.com lesson.
- **tier:** deep
- **level:** HS
- **why:** Probably the best visual intuition pump for entropy as "expected bits of information from a guess." It builds a Wordle solver that picks the guess with maximal expected information. Watch it before or alongside Pierce.
- **focus:** whole
- **access:** free: https://www.youtube.com/watch?v=v68zYyaEmEA
- **verified:** https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=v68zYyaEmEA&format=json ; https://www.3blue1brown.com/lessons/wordle

### Strand: KL divergence, cross-entropy, information geometry

#### kullback-1951-information
- **type:** paper
- **citation:** Kullback, S., & Leibler, R. A. (1951). *On Information and Sufficiency*. The Annals of Mathematical Statistics, 22(1), 79–86. DOI 10.1214/aoms/1177729694.
- **tier:** core
- **level:** grad
- **why:** It introduces the "mean information for discrimination" now called KL divergence (relative entropy) and ties it to sufficient statistics. KL is the quantity behind maximum likelihood, cross-entropy loss, variational inference, RLHF's KL penalty and model comparison. The paper is short and readable.
- **focus:** whole
- **access:** free: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-1/On-Information-and-Sufficiency/10.1214/aoms/1177729694.full
- **verified:** https://api.crossref.org/works/10.1214/aoms/1177729694

#### nielsen-2020-elementary
- **type:** paper
- **citation:** Nielsen, F. (2020). *An Elementary Introduction to Information Geometry*. Entropy, 22(10), 1100. DOI 10.3390/e22101100.
- **tier:** deep
- **level:** grad
- **why:** An open-access tutorial on the geometric view of families of probability distributions: the Fisher metric, dual connections and Bregman divergences. It shows that KL divergence is locally a squared distance, and it is the shortest legitimate route into Amari-style information geometry.
- **focus:** whole (read after Cover & Thomas Ch. 2 and 11).
- **access:** free: https://arxiv.org/pdf/1808.08271
- **verified:** https://api.crossref.org/works/10.3390/e22101100

#### tishby-2000-bottleneck
- **type:** paper
- **citation:** Tishby, N., Pereira, F. C., & Bialek, W. (2000). *The information bottleneck method*. arXiv:physics/0004057.
- **tier:** deep
- **level:** grad
- **why:** It defines "relevant information" as finding a compressed code for X that keeps as much information as possible about Y, a rate–distortion problem where the distortion measure is itself information. This framework now underlies work on efficient semantic categories (Zaslavsky et al., assigned in Futrell's course) and on representation learning.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/physics/0004057
- **verified:** https://arxiv.org/abs/physics/0004057

### Strand: Algorithmic information and MDL

#### kolmogorov-1965-three
- **type:** paper
- **citation:** Kolmogorov, A. N. (1965). Three approaches to the definition of the concept "quantity of information." *Problemy Peredachi Informatsii*, 1(1), 3–11. English translation: *Three approaches to the quantitative definition of information*. International Journal of Computer Mathematics, 2(1–4), 157–168 (1968). DOI 10.1080/00207166808803030.
- **tier:** deep
- **level:** grad
- **why:** Kolmogorov contrasts combinatorial, probabilistic (Shannon) and algorithmic definitions of information. The algorithmic one, the length of the shortest program that outputs an object, measures information in a single object without any probability distribution. It is the primary source for Kolmogorov complexity.
- **focus:** whole
- **access:** need-copy (English); the Russian original is free at https://www.mathnet.ru/eng/ppi68
- **verified:** https://www.mathnet.ru/eng/ppi68 ; https://api.crossref.org/works/10.1080/00207166808803030

#### rissanen-1978-modeling
- **type:** paper
- **citation:** Rissanen, J. (1978). *Modeling by shortest data description*. Automatica, 14(5), 465–471. DOI 10.1016/0005-1098(78)90005-5.
- **tier:** deep
- **level:** grad
- **why:** This founding paper of MDL argues that the best model is the one giving the shortest total description of the model plus the data encoded with it. It turns Occam's razor into a computable criterion and shows that model selection is data compression.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1016/0005-1098(78)90005-5

#### grunwald-2007-minimum
- **type:** book
- **citation:** Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press. ISBN 978-0-262-07281-6. 570 pp.
- **tier:** deep
- **level:** grad
- **why:** The definitive modern treatment of MDL. It covers crude two-part codes, refined MDL, normalized maximum likelihood and the relations to Bayes and prequential prediction. It is the right depth for judging model-selection claims (e.g., MDL-based community detection or topic-number selection).
- **focus:** Part I (Ch. 1 Learning, Regularity, and Compression; Ch. 2–5 preliminaries and Crude Two-Part Code MDL); Ch. 14 (MDL Model Selection); Ch. 17 (MDL in Context).
- **access:** need-copy (Ch. 1 and Ch. 17 are free samples at https://homepages.cwi.nl/~pdg/book/book.html; the author's free 80-page tutorial is https://arxiv.org/pdf/math/0406077)
- **verified:** https://homepages.cwi.nl/~pdg/book/book.html ; https://arxiv.org/abs/math/0406077

#### li-2019-kolmogorov
- **type:** book
- **citation:** Li, M., & Vitányi, P. (2019). *An Introduction to Kolmogorov Complexity and Its Applications* (4th ed.). Springer, Texts in Computer Science. DOI 10.1007/978-3-030-11298-1.
- **tier:** reference
- **level:** grad
- **why:** The encyclopedic reference on algorithmic information: plain and prefix complexity, algorithmic probability (Solomonoff), inductive reasoning and the incompressibility method. Consult it when you need a precise statement rather than reading it cover to cover.
- **focus:** chapters "Preliminaries", "Algorithmic Complexity", "Algorithmic Probability", "Inductive Reasoning".
- **access:** need-copy
- **verified:** https://link.springer.com/book/9783030112981

#### rosvall-2008-maps
- **type:** paper
- **citation:** Rosvall, M., & Bergstrom, C. T. (2008). *Maps of random walks on complex networks reveal community structure*. Proceedings of the National Academy of Sciences, 105(4), 1118–1123. DOI 10.1073/pnas.0706851105.
- **tier:** deep
- **level:** grad
- **why:** The "map equation" (Infomap) finds network communities by minimizing the description length of a random walk under a two-level code. It is MDL and Shannon source coding applied directly to network science, the most direct bridge from this field to Kunhao's own network work.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/0707.0609
- **verified:** https://api.crossref.org/works/10.1073/pnas.0706851105 ; https://arxiv.org/abs/0707.0609

### Strand: Maximum entropy, inference and physics

#### jaynes-1957-information
- **type:** paper
- **citation:** Jaynes, E. T. (1957). *Information Theory and Statistical Mechanics*. Physical Review, 106(4), 620–630. DOI 10.1103/PhysRev.106.620. (Part II: Physical Review, 108, 171.)
- **tier:** core
- **level:** grad
- **why:** Jaynes recasts statistical mechanics as inference. Given only some constraints (e.g., average energy), the least-biased distribution is the one with maximum entropy, which yields the Gibbs/Boltzmann distribution. This MaxEnt principle underlies logit models, exponential-family models and ERGMs.
- **focus:** the opening sections that set out the maximum-entropy argument, before the physics applications.
- **access:** free: https://bayes.wustl.edu/etj/articles/theory.1.pdf
- **verified:** https://bayes.wustl.edu/etj/node1.html ; https://api.crossref.org/works/10.1103/PhysRev.106.620

#### jaynes-2003-probability
- **type:** book
- **citation:** Jaynes, E. T. (2003). *Probability Theory: The Logic of Science* (G. L. Bretthorst, Ed.). Cambridge University Press. DOI 10.1017/CBO9780511790423.
- **tier:** reference
- **level:** grad
- **why:** Jaynes's magnum opus derives probability as extended logic and places maximum entropy inside Bayesian reasoning. It is polemical and deep. This catalog uses it for the entropy-principle and communication-theory chapters; the Bayesian canon will use more of it.
- **focus:** Ch. 11 (Discrete prior probabilities: the entropy principle); Ch. 22 (Introduction to communication theory); Ch. 1–2 for the framing.
- **access:** need-copy
- **verified:** https://www.cambridge.org/core/books/probability-theory/9CA08E224FF30123304E6D8935CF1A99

#### landauer-1961-irreversibility
- **type:** paper
- **citation:** Landauer, R. (1961). *Irreversibility and Heat Generation in the Computing Process*. IBM Journal of Research and Development, 5(3), 183–191. DOI 10.1147/rd.53.0183.
- **tier:** deep
- **level:** grad
- **why:** Landauer shows that logically irreversible operations, such as erasing a bit, must dissipate at least kT ln 2 of heat ("information is physical"). This principle resolves Maxwell's demon and fixes the physical meaning of Shannon/Gibbs entropy.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1147/rd.53.0183

### Strand: Language, cognition, economics and philosophy

#### shannon-1951-prediction
- **type:** paper
- **citation:** Shannon, C. E. (1951). *Prediction and Entropy of Printed English*. Bell System Technical Journal, 30(1), 50–64. DOI 10.1002/j.1538-7305.1951.tb01366.x.
- **tier:** core
- **level:** UG
- **why:** Shannon used human subjects guessing the next letter to bound the entropy of English at about 1 bit per letter. This is the ancestor of language modeling and of today's perplexity and surprisal metrics. Futrell's information-theoretic linguistics syllabus assigns it.
- **focus:** whole
- **access:** free: https://sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/readings/shannon1951prediction.pdf
- **verified:** https://api.crossref.org/works/10.1002/j.1538-7305.1951.tb01366.x ; https://archive.org/details/bstj30-1-50

#### kelly-1956-new
- **type:** paper
- **citation:** Kelly, J. L., Jr. (1956). *A New Interpretation of Information Rate*. Bell System Technical Journal, 35(4), 917–926. DOI 10.1002/j.1538-7305.1956.tb03809.x.
- **tier:** core
- **level:** UG
- **why:** A gambler with a noisy private tip can grow wealth exponentially at a rate equal to the mutual information of the tip channel. This gives "information rate" an economic meaning and founded the Kelly criterion and log-optimal investing. Cover & Thomas Ch. 6 and 16 develop it.
- **focus:** whole
- **access:** free: https://homepage.sns.it/marmi/esameIUE/kelly.pdf
- **verified:** https://archive.org/details/bstj35-4-917 ; https://api.crossref.org/works/10.1002/j.1538-7305.1956.tb03809.x

#### gibson-2019-efficiency
- **type:** paper
- **citation:** Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How Efficiency Shapes Human Language*. Trends in Cognitive Sciences, 23(5), 389–407. DOI 10.1016/j.tics.2019.02.003.
- **tier:** core
- **level:** UG
- **why:** The synthesis review of information-theoretic linguistics. It argues that lexicon, syntax and processing are shaped by efficient communication under noise and effort constraints (word length vs. predictability, surprisal, dependency-length minimization, information-bottleneck semantics). It is the gateway from Shannon to cognition and to evaluating LLMs as models of language.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1016/j.tics.2019.02.003 ; https://sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/

#### sims-2003-implications
- **type:** paper
- **citation:** Sims, C. A. (2003). *Implications of rational inattention*. Journal of Monetary Economics, 50(3), 665–690. DOI 10.1016/S0304-3932(03)00029-1.
- **tier:** deep
- **level:** grad
- **why:** Sims models economic agents as having finite Shannon channel capacity for processing information, which explains sluggish, smoothed responses to news. Rational inattention is now the main way economics brings information theory into models of attention, which is relevant to attention-fatigue and media-attention research.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1016/S0304-3932(03)00029-1

#### adriaans-2012-information
- **type:** website
- **citation:** Adriaans, P. (2012; substantive revision 2023). *Information*. In E. N. Zalta (Ed.), *Stanford Encyclopedia of Philosophy*.
- **tier:** reference
- **level:** UG
- **why:** A philosophical map of the concept of information: Shannon's probabilistic measure, Kolmogorov's program-length measure, and the problems of semantic information and meaning. Use it to keep the technical and everyday senses of "information" apart, especially when writing on misinformation.
- **focus:** §1 (Concepts of Information); §4.2 (Shannon); §4.3 (Solomonoff, Kolmogorov, Chaitin); §6.4 (Model Selection and Data Compression); §6.6 (Logic and Semantic Information).
- **access:** free: https://plato.stanford.edu/entries/information/
- **verified:** https://plato.stanford.edu/entries/information/

## Concept spine
- **bit** — the unit of information: the uncertainty resolved by one fair yes/no question (HS)
- **self-information / surprisal** — −log p(x): how surprising one outcome is, so rare events carry more bits (HS)
- **entropy H(X)** — average surprisal; the irreducible uncertainty of a source in bits per symbol (HS)
- **joint and conditional entropy** — uncertainty of a pair, and what remains about X once Y is known (UG)
- **chain rule** — H(X,Y) = H(X) + H(Y|X); uncertainty adds up step by step (UG)
- **mutual information I(X;Y)** — how much knowing Y reduces uncertainty about X; symmetric, and zero iff X and Y are independent (UG)
- **redundancy** — the gap between maximum possible entropy and actual entropy; it is what makes compression and error correction possible (HS)
- **entropy rate** — entropy per symbol of a process with memory, such as English text (UG)
- **typical set / AEP** — long sequences almost always fall in a set of about 2^{nH} roughly equiprobable sequences (grad)
- **source coding theorem** — data cannot be losslessly compressed below H bits per symbol on average, and H is achievable (UG)
- **prefix code & Kraft inequality** — instantaneously decodable codes exist iff Σ 2^{−ℓ_i} ≤ 1; code lengths and probabilities are interchangeable (UG)
- **Huffman / arithmetic coding** — practical codes that approach the entropy bound (UG)
- **noisy channel** — a conditional distribution p(y|x) that corrupts transmitted symbols (UG)
- **channel capacity** — the maximum mutual information between input and output; the highest rate of reliable communication (UG)
- **noisy-channel coding theorem** — below capacity the error probability can be made arbitrarily small; above it, it cannot (UG)
- **Shannon–Hartley formula** — C = W log2(1 + S/N) for a band-limited Gaussian channel (UG)
- **error-correcting code** — adding structured redundancy so errors can be detected and corrected (UG)
- **rate–distortion function** — the minimum bits needed to describe a source within a given average distortion; the theory of lossy compression (grad)
- **source–channel separation** — compression and transmission can be designed separately without loss, under standard conditions (grad)
- **data processing inequality** — no processing of Y can increase its information about X (UG)
- **Fano's inequality** — a lower bound on error probability from the residual conditional entropy (grad)
- **relative entropy / KL divergence** — the expected extra bits paid for coding data from p with a code built for q; non-negative and asymmetric (UG)
- **cross-entropy** — the average code length when coding p with q's code, equal to H(p) + KL(p‖q); the standard training loss for classifiers and LLMs (UG)
- **perplexity** — 2^{cross-entropy}: the effective number of equally likely choices a model faces per token (UG)
- **f-divergence** — a family of divergences including KL, total variation, χ² and Hellinger (grad)
- **Fisher information** — the curvature of log-likelihood; the local, second-order form of KL divergence (grad)
- **Fisher–Rao metric / information geometry** — treating a family of distributions as a curved space whose distance is set by Fisher information (grad)
- **differential entropy** — entropy for continuous variables; it can be negative and depends on coordinates (grad)
- **maximum entropy principle** — among distributions consistent with what you know, choose the one with maximum entropy (UG)
- **exponential family / Gibbs distribution** — the form of every MaxEnt solution under expectation constraints: p ∝ exp(Σ λ_i f_i) (grad)
- **Landauer's principle** — erasing one bit dissipates at least kT ln 2 of heat; information processing has a physical cost (grad)
- **Kolmogorov complexity K(x)** — the length of the shortest program that outputs x; information content of an individual object (grad)
- **incompressibility / algorithmic randomness** — a string is random if it has no description shorter than itself (grad)
- **algorithmic probability (Solomonoff)** — a universal prior weighting hypotheses by 2^{−program length} (grad)
- **Minimum Description Length (MDL)** — pick the model that minimizes the bits for model plus data; formalized Occam's razor (grad)
- **normalized maximum likelihood (NML)** — refined MDL's minimax-optimal universal code for a model class (grad)
- **universal coding** — a single code that performs nearly as well as the best code in a class, without knowing the true source (grad)
- **Kelly criterion / doubling rate** — betting fractions that maximize the long-run growth rate of wealth; side information raises growth by its mutual information (UG)
- **information bottleneck** — compress X into T while preserving as much information as possible about a relevance variable Y (grad)
- **transfer entropy** — directed, time-lagged information flow from one process to another (grad)
- **rational inattention** — agents with a channel-capacity limit on how much information they can absorb (grad)
- **uniform information density / efficient communication** — speakers spread information evenly and languages trade word length against predictability (UG)

## Canonical instances
- **Twenty questions / binary search** — the minimum expected number of yes/no questions to identify an item is about its entropy in bits — mackay-2003-information
- **The 12-ball weighing puzzle** — choosing weighings that maximize expected information solves it in three weighings; MacKay presents it as "designing informative experiments" — mackay-2003-information
- **Binary symmetric channel with repetition vs. Hamming (7,4) codes** — shows the trade-off between rate and reliability that the coding theorem says can be beaten — mackay-2003-information
- **Shannon's approximations to English** — random text built from first-order, second-order and word-level statistics grows more English-like, an n-gram language model in 1948 — shannon-1948-mathematical
- **Shannon's guessing game** — humans guessing the next letter imply roughly 1 bit per letter for English — shannon-1951-prediction
- **Kelly's gambler with a private wire** — a bettor with a noisy tip on horse races grows wealth at a rate equal to the tip's information rate — kelly-1956-new
- **Wordle solver** — rank guesses by expected information gained over remaining candidate words — 3blue1brown-2022-wordle
- **MaxEnt derivation of the Boltzmann distribution** — knowing only the mean energy, maximum entropy yields p ∝ e^{−βE} — jaynes-1957-information
- **Landauer erasure / Maxwell's demon** — the demon's measurements must eventually be erased, and erasure costs kT ln 2 per bit, which saves the second law — landauer-1961-irreversibility
- **Regular vs. random strings** — "0101…01" has a short program while a coin-flip string does not; incompressibility as the definition of randomness — li-2019-kolmogorov
- **Map equation's city-and-street code** — like maps that reuse street names across cities, a two-level codebook describes random walks briefly when the network has communities — rosvall-2008-maps
- **Word length vs. predictability** — words that are more predictable in context tend to be shorter, as efficient coding predicts — gibson-2019-efficiency
- **Sluggish prices under inattention** — capacity-limited agents respond to monetary shocks gradually and smoothly — sims-2003-implications

## Bridges
- [same-math] cross-entropy / perplexity ↔ LLMs: next-token training loss — LLM pretraining minimizes exactly the cross-entropy Shannon estimated in 1951, and perplexity is 2^{that}
- [same-math] KL divergence ↔ Bayesian theory & causal inference: variational inference / ELBO — the ELBO gap is a KL divergence, and Bayesian marginal likelihood equals a code length in MDL (MacKay Ch. 28, Grünwald Ch. 8)
- [same-math] Kelly doubling rate ↔ economics & finance: log-optimal portfolio — the growth rate of log-utility investing is the information-theoretic quantity of Kelly 1956 and Cover & Thomas Ch. 16
- [same-math] maximum entropy ↔ complex systems: exponential random graph models — an ERGM is the MaxEnt distribution over graphs subject to expected sufficient statistics, the same Gibbs form as Jaynes 1957
- [same-math] Fisher information / KL Hessian ↔ linear algebra: positive semidefinite matrices — the local quadratic form of KL is the Fisher matrix, so information geometry is linear algebra on tangent spaces
- [same-math] mutual information ↔ political science: Theil segregation index — the entropy-based Theil index of group segregation across units is a (normalized) mutual information between group and unit
- [structural-analogy] channel capacity / rational inattention ↔ decision & game theory: bounded rationality — information-processing limits enter choice models as a capacity constraint on what the agent can know
- [structural-analogy] surprisal ↔ theory of mind: prediction-based comprehension — surprisal is computed with the same formula, but its role as processing cost is an empirical claim (Gibson et al. 2019), not a theorem
- [metaphor] Shannon–Weaver transmission model ↔ communication theory: sender–channel–receiver — communication studies borrowed the diagram, but Shannon's theory deliberately excludes meaning, which is Weaver's "semantic level"
- [structural-analogy] Shannon vs. semantic information ↔ analytic philosophy: meaning and truth — whether false content ("misinformation") is information at all is a philosophical question that the SEP entry separates from Shannon's measure
