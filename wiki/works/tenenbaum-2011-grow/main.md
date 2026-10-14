---
id: tenenbaum-2011-grow/main
work: tenenbaum-2011-grow
unit: paper
pages: 1279-1286
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# How to Grow a Mind: Statistics, Structure, and Abstraction

## L0 — One line
Human learning from sparse data can be modelled as Bayesian inference over hierarchies of structured generative models, in which abstract knowledge both constrains learning and is itself learned.

## L1 — The gist (≤ 120 words)
Children learn words and causal links from a few examples. How does abstract knowledge guide this, what form does it take, and how is it acquired? The authors answer with probabilistic generative models (mental models of how observations arise) over structured representations (trees, graphs, grammars, logic). Hierarchical Bayesian models (HBMs) add higher levels that supply the hypothesis spaces and priors of the levels below. Such abstractions can be learned fast, the "blessing of abstraction". This route contrasts with both nativism (abstractions present from birth) and associationism (abstractions built slowly from experience). Open problems remain: core intuitive theories, approximate algorithms, and a neural basis for symbols.

**Prerequisites:** Bayes' rule (prior, likelihood, posterior); probabilities over hypotheses; what a graph (nodes and edges) is.

## L2 — Key ideas (5–10 bullets)
- The central puzzle is how minds get so much from so little. Extra background knowledge ("constraints", "inductive bias", "priors") must fill the gap between data and conclusions (p. 1279).
- Abstract knowledge is encoded in a probabilistic generative model. Bayes' rule updates beliefs about its latent (hidden, unobserved) variables, and the hypothesis space and priors carry the knowledge (p. 1280).
- Generalization combines a likelihood that favours tight hypotheses ("suspicious coincidence") with a prior that favours coherent, distinctive ones (p. 1281).
- Abstract knowledge takes structured symbolic forms: trees, spaces, orders, directed graphs, graph schemas, grammars, logical laws. Restricting hypotheses to a suitable form can shrink the hypothesis space enormously, and this helps only while the true structure lies within or near it (p. 1281).
- HBMs put hypothesis spaces of hypothesis spaces, with priors on priors, so the forms and theories can be learned. Examples are the form of structure in a domain and the disease–symptom framework (pp. 1282–1283).
- Abstractions are learned from little data because each higher-level degree of freedom pools evidence from many variables below ("blessing of abstraction"). Nonparametric HBMs (unbounded structure, but finitely many active degrees of freedom) with an automatic Occam's razor (new structure only when the data require it) balance constraint and flexibility (p. 1284).
- The approach targets a view between Marr's computational level (what problem is solved) and algorithmic level (which procedures solve it). Open problems are intuitive theories, approximate (e.g. Monte Carlo, i.e. sampling-based) inference, and neural implementation of symbols (p. 1284).

## L3 — Walkthrough

### The Challenge: How Does the Mind Get So Much from So Little? (p. 1279)
- Inputs are sparse, noisy and ambiguous, yet we build causal models and abstractions (p. 1279).
- **Word learning:** typical 2-year-olds learn "horse" or "hairbrush" from a few examples. They generalize, which shows they grasp the meaning and not just the sound (p. 1279). Adults learning novel object concepts can do as well (Fig. 1) (p. 1279).
- **Causal learning:** correlation does not imply causation, yet children infer causal links from a handful of events, too few to compute a reliable correlation (p. 1279).
- Larger systems of knowledge (intuitive physics, psychology, biology; rule systems) take years to build, and the final product still outstrips the data (p. 1279).
- The authors say philosophers' answer is, in broad strokes, that some more abstract background knowledge must generate and delimit the hypotheses considered. Psychologists call it "constraints", machine learning "inductive bias", statistics "priors" (p. 1279).
- Three questions: (1) How does abstract knowledge guide learning from sparse data? (2) What forms does it take? (3) How is it acquired? (p. 1279).
- **Two earlier approaches** (their characterization): modelers had to choose between (a) powerful statistical learning over unstructured knowledge, such as matrices of associative weights in connectionism, and (b) richly structured symbolic knowledge with only simple non-statistical learning, as in nativist accounts of language. It appeared necessary to accept that choosing (a) meant knowledge is not very abstract, and choosing (b) meant it is essentially innate (p. 1279). Many developmental researchers rejected the choice and turned to "constructivism" or "theory theory" (p. 1279).
- Bayesian models combine structured representations (question 2) with powerful statistical inference (questions 1 and 3). The authors argue that only a synthesis of both can account for human intelligence (p. 1279).

### The Role of Abstract Knowledge (pp. 1279–1281)
- Bayesian analyses have illuminated similarity, representativeness, randomness, coincidences, causal strength, evidential support, diagnostic reasoning and predictions about everyday events (pp. 1279–1280).
- **Scope:** the claim is not that the mind can implement any Bayesian inference. Only computations the mind is designed to perform well (where biology had time and cause to engineer mechanisms) are likely to be understood in Bayesian terms. Examples are perception, language, memory and sensorimotor systems. Tasks needing explicit manipulation of numerical probabilities can be notoriously biased away from Bayesian norms (p. 1280).
- **Generative model:** a mental model of the causal processes behind observations, including unobserved (latent) variables. It must be probabilistic to handle uncertainty. It is abstract in two senses: it covers a broader class of situations, and it captures the essential world structure in parsimonious form (p. 1280).
- Background knowledge is a constrained hypothesis space $H$ of candidate world structures. The prior $P(h)$ is the degree of belief in $h$ before the data. Bayes' rule gives the posterior given data $d$:

$$P(h\mid d)=\frac{P(d\mid h)P(h)}{\sum_{h'\in H}P(d\mid h')P(h')}\;\propto\;P(d\mid h)P(h)\tag{1}$$

  The likelihood $P(d\mid h)$ measures how expected the data are under $h$, relative to the other hypotheses $h'$ in $H$ (p. 1280).
- **Cough example:** $d$ = John coughs; $h_1$ cold, $h_2$ lung disease, $h_3$ heartburn. The likelihood favours $h_1,h_2$ over $h_3$, because only colds and lung disease cause coughing. The prior favours $h_1,h_3$ over $h_2$, because colds and heartburn are much more common. Only $h_1$ scores highly on both (pp. 1280–1281).
- **Concept learning:** data are example objects, hypotheses are possible extensions of the concept. Given three different horses, why generalize "horse" to all and only horses ($h_1$), not "all horses except Clydesdales" ($h_2$) or "all animals" ($h_3$)? Likelihoods favour $h_1,h_2$: three random examples all falling in a small set would be a highly suspicious coincidence if drawn from the much larger $h_3$. The prior favours $h_1,h_3$ as more coherent, distinctive categories, more likely to be labelled by common words. Only $h_1$ scores highly on both (p. 1281).
- **Causal learning:** likelihoods favour links that make the co-occurrence more probable. Priors favour links fitting background knowledge, e.g. disease causes symptom rather than the reverse (p. 1281).
- **Fig. 1B:** word learning as inference over a tree. Objects sit at leaves, hypotheses are branches. Priors depend on branch length (distinctiveness). Likelihoods assume examples are drawn randomly from the labelled branch. The posterior favours the lowest distinctive branch spanning all examples (p. 1280).

*Intuition note:* Priors say which explanations are plausible before looking. Likelihoods say which explanations make the data unsurprising. A good explanation needs both. Few examples can be enough when the hypothesis space is small and the true structure lies within or near it.

### The Form of Abstract Knowledge (p. 1281)
- Listing every logically possible hypothesis with its prior and likelihood is impossible for complex tasks, so more sophisticated representations must underlie generative models (p. 1281).
- Associative and connectionist models define learning over large numerical vectors (weights, parameters of nonlinear functions). Bayesian cognitive models have had most success with structured symbolic forms: graphs, grammars, predicate logic, relational schemas, functional programs (p. 1281).
- Tree-structured models describe word learning and reasoning about natural kinds (e.g. cows and rhinos share protein X, so how likely do horses or squirrels?). Trees are not universal. Other forms fit other domains (Fig. 2): 2-D spaces or grids for geography, 1-D orders for values or abilities, directed networks for causally transmitted properties such as diseases (p. 1281).
- **Directed graphical models:** nodes are variables, directed edges are probabilistic causal links (e.g. colds tend to cause cough and fever but not chest pain) (Fig. 3A). This is a simple intuitive theory (p. 1281).
- Learning such networks from limited data depends on a **framework theory**: two classes of variables (diseases, symptoms), with edges tending to run from diseases to symptoms. It can be represented by graph schemas (templates for graphs based on node types) or probabilistic graph grammars (p. 1281). At the most abstract level, the concept of causality itself can be expressed as logical laws on directed graphs relating actions and events (Fig. 3D) (p. 1281).
- **Counting hypotheses.** The numbers below are the authors' (p. 1281):
  - $n$ objects give $2^n$ subsets, hence $2^n$ possible extensions of a novel concept. Restricting concepts to branches of a specific binary tree leaves only $n-1$ hypotheses.
  - Causal networks over 16 variables: roughly $10^{46}$ DAGs. A bipartite disease–symptom framework: roughly $10^{23}$. Also knowing which variables are diseases or symptoms: roughly $10^{18}$.
- The smaller the hypothesis space, the more accurately a learner can be expected to generalize, but only while the true structure stays within or near (probabilistically) that space (p. 1281). Useful constraint comes from a compact description approximating "how the grain of the world actually runs" (p. 1281).

*Intuition note:* Restricting the hypotheses is like narrowing a search. If the restriction is right, a few data points pick the answer. If the true structure lies far outside it, the benefit is lost.

### The Origins of Abstract Knowledge (pp. 1281–1284)
- Question 3 asks how learners know which structure (tree, space, other) suits a domain, or which framework theory is right (p. 1281).
- Children first assume a flat, mutually exclusive division of objects into nameable clusters, and only later discover tree-structured hierarchies. The authors give similar discoveries in science: Mendeleev's periodic structure, and Linnaeus's tree for species instead of the "great chain of being" (a linear order) (p. 1281).
- Conventional structure-discovery algorithms (hierarchical clustering, PCA, multidimensional scaling, clique detection) assume one fixed form of structure, so they cannot discover new forms (p. 1281).
- **Nativists** (the authors' characterization): if domains are represented in qualitatively different forms, the forms must be innate. **Connectionists:** representations may be learned, but in a generic associative system that at best approximates trees and networks (p. 1282).
- **Hierarchical Bayesian models (HBMs):** multiple levels, "hypothesis spaces of hypothesis spaces, with priors on priors". Each level generates a distribution over variables at the level below. Inference across all levels lets hypotheses and priors be learned at larger or longer time scales while constraining lower-level learning (p. 1282). In machine learning HBMs are mainly used for transfer learning (p. 1282).
- **Discovering the form of structure (Fig. 2; Kemp & Tenenbaum)** (pp. 1282–1283):
  - Levels: data $D$ (matrix of objects × features, or pairwise similarities); structure $S$, a graph over objects; form $F$, given by grammatical rules for growing a graph of a constrained form from a seed node.
  - Nearby objects in the graph should share feature values. Technically, the graph Laplacian parameterizes the inverse covariance of a gaussian with one dimension per object, and each feature is drawn independently from it.
  - Red arrows are $P(S\mid F)$ and $P(D\mid S)$. A search algorithm seeks $F$ and $S$ that jointly maximize the posterior $P(S,F\mid D)$, a function of the product of $P(D\mid S)$ and $P(S\mid F)$.
  - Results: animal features give a tree; U.S. Supreme Court votes give a linear left–right chain; color similarities give a ring; city proximities give ring × chain (a cylinder); face images varying in two dimensions give chain × chain (a grid).
  - Applied to the novel objects of Fig. 1A, the model infers that a hierarchy fits the similarities people see better than a 2-D space (p. 1283).
- **Learning causal framework theories (Fig. 3; Mansinghka et al.)** (p. 1283):
  - The task is to reconstruct a 16-variable network (variables 1–6 "diseases", 7–16 "symptoms") from patient data (Fig. 3A).
  - Two-level HBM (uninformative prior over networks, Fig. 3B): with $n=20$ patients almost none of the true structure is detected. With $n=80$ spurious links appear. Perfect recovery needs very many patients ($n=1000$).
  - Three-level nonparametric HBM (Fig. 3C): a graph schema assigns variables 1–6 to class $C_1$, 7–16 to $C_2$, and favours only $C_1\to C_2$ links. The number of classes is also inferred, via the Bayesian Occam's razor. It has many more degrees of freedom, yet learns faster and more accurately. With $n=80$ the network is identified near perfectly. With $n=20$ the schema is already learned, leaving uncertainty only about which diseases cause which symptoms.
  - The schema and network are learned from the same data (p. 1283).
- "Getting the big picture first" and then filling in details is described as a distinctively human mode of learning that did not previously fit rational or statistical learning models (p. 1284).
- **Flexibility** (p. 1284): the model can discover framework theories with any number of variable classes and any pattern of pairwise regularities. Nonparametric ("infinite") hierarchical models posit unbounded structure, but only finitely many degrees of freedom are active for a given data set. The automatic Occam's razor introduces new structure only when the data truly require it.
- **Chinese restaurant process (CRP)** (p. 1284): the nonparametric distribution on node classes in Fig. 3C. CRP models gave the first principled account of how people form new categories without supervision: each stimulus is assimilated to an existing category or assigned to a new one. Extensions named: CrossCat (divides domains into "views", each organizing objects differently); CRPs in language models for segmenting words, morphology and semantic networks; the Indian buffet process (IBP) for constructing new perceptual features.
- Nonparametric HBMs address the problem of balancing constraint and flexibility (p. 1284).
- **Blessing of abstraction** (p. 1284): across the case studies, abstractions in HBMs can be learned fast from relatively little data compared with lower levels. Each degree of freedom at a higher level influences and pools evidence from many variables below.
- This is a top-down route to the origins of knowledge. It contrasts with nativism (abstractions present from birth) and with empiricism or associationism (abstractions built only approximately and slowly, bottom-up, by layering experiences). The authors say only HBMs "seem suited" to explaining that abstract knowledge can be learned and can be engaged early in life (p. 1284).

*Intuition note:* One higher-level fact, such as "diseases cause symptoms", affects many specific links at once. So each observation tests it many times and it is learned quickly. Once known, it makes learning the specific links easier.

### Open Questions (pp. 1284–1285)
- **How does it all start?** Developmentalists argue that learning needs some innate abstract concepts ("agent", "object", "cause") (**developmentalists' view**). The Bayesian modelers do not dispute that some representation is innate, but argue even the most abstract concepts may in principle be learned. For example, an abstract concept of causality as logical constraints on directed graphs can be learned by an HBM generalizing across many causal systems (Fig. 3D), induced from small samples of each system. Whether this extends to "agent" or "object", and whether children actually learn them this way, remains open (p. 1284).
- **Hardest subjects:** HBMs have only touched framework theories for intuitive physics, psychology and biology. First steps: theory of mind (understanding false beliefs), individual differences in preferences, origins of essentialism, early beliefs about magnetism. The most daunting challenge is that formalizing intuitive theories appears to require Turing-complete compositional representations (probabilistic first-order logic, probabilistic programming languages), and it is unclear how to constrain learning with such flexible representations (p. 1284).
- **Levels of analysis (Marr):** computational (the problem and principles for solving it), algorithmic (procedures and representations), implementation (circuits). Many early Bayesian models addressed only the computational level. The HBMs here target a view between computational and algorithmic: approximately optimal inference over a learner's subjective, growing mental representations rather than objective fixed world statistics (p. 1284).
- Exact inference in large models is complex, so lower levels can at best approximate Bayesian computation. The key questions: which approximate algorithms does the mind use, how do they relate to AI approximations, and how are they neurally implemented? Monte Carlo (sampling) approximations are pointed to as a unifying framework. They work in structured models but are very slow (p. 1284).
- The biggest obstacle: how structured symbolic knowledge is represented in neural circuits. The authors say connectionist models sidestep this by denying that brains encode rich knowledge. This runs counter to the strong consensus (as the authors put it) that symbols and structures are essential for thought. Finding the neural basis is called arguably the greatest computational challenge in cognitive neuroscience (pp. 1284–1285).

### Conclusions (p. 1285)
- Benefits claimed: (i) a unifying mathematical language for cognition as solving inductive problems, with few free parameters and ad hoc assumptions; (ii) a framework for why the mind works as it does (rational inference adapted to real-world structure) and what it knows (abstract schemas and intuitive theories, revealed only indirectly through how they constrain generalizations) (p. 1285).
- It lets us move beyond dichotomies: empiricism vs nativism, domain-general vs domain-specific, logic vs probability, symbols vs statistics (p. 1285).
- Powerful abstractions can be learned surprisingly quickly, together with or prior to the concrete knowledge they constrain. Structured symbolic representations need not be rigid, static, hard-wired or brittle when embedded in a probabilistic framework (p. 1285).

## Toy example (ours, not from the text)
A word-learning model in the style of Fig. 1B. Three nested hypotheses for the word "tufa". The extension sizes (4, 8, 40 objects) and the priors are invented for illustration. Likelihood for 3 examples drawn at random from the extension: $(1/\text{size})^3$.

| h | size | prior | likelihood | prior × likelihood |
|---|---|---|---|---|
| $h_1$ | 4 | 0.3 | $(1/4)^3=0.015625$ | $0.3\times0.015625=0.0046875$ |
| $h_2$ | 8 | 0.3 | $(1/8)^3=0.001953125$ | $0.3\times0.001953125=0.0005859375$ |
| $h_3$ | 40 | 0.4 | $(1/40)^3=0.000015625$ | $0.4\times0.000015625=0.00000625$ |

Sum $=0.0046875+0.0005859375+0.00000625=0.0052796875$.
Posteriors: $h_1$: $0.0046875/0.0052796875\approx0.888$; $h_2\approx0.111$; $h_3\approx0.0012$.
Although $h_3$ has the highest prior, three examples all inside a small set make the broad hypothesis a "suspicious coincidence". The tight hypothesis $h_1$ wins.

## Concepts
- [[bayes-theorem]] — Eq. (1): posterior proportional to prior × likelihood, normalized over hypothesis space $H$ (p. 1280)
- [[prior-distribution]] — $P(h)$, degree of belief in $h$ before the data; carries finer-grained background knowledge (p. 1280)
- [[likelihood]] — $P(d\mid h)$, how expected the data are under $h$ relative to other hypotheses (p. 1280)
- [[posterior-distribution]] — $P(h\mid d)$, beliefs updated on the observed data (p. 1280)
- [[hierarchical-model]] — HBM: multiple levels, each generating a distribution for the level below; priors on priors (p. 1282)
- [[bayesian-occams-razor]] — automatic trade-off of complexity and fit; new structure only if data require it (p. 1284)
- [[learning-to-learn]] — here: transfer learning, acquiring inductive constraints from earlier related tasks (p. 1282)
- [[rational-analysis]] — here: cognition as approximately optimal inference in probabilistic models, between Marr's computational and algorithmic levels (p. 1284)
- [[monte-carlo-integration]] — sampling-based approximation proposed as a unifying account of practical Bayesian inference (p. 1284)
- [[generative-model]] (new) — probabilistic mental model of the causal processes and latent variables behind observations (p. 1280)
- [[hypothesis-space]] (new) — constrained set $H$ of candidate structures; encodes background knowledge (p. 1280)
- [[framework-theory]] (new) — abstract theory fixing variable classes and allowed causal link patterns, e.g. diseases → symptoms (p. 1281)
- [[graph-schema]] (new) — template for graphs based on types of nodes (p. 1281)
- [[blessing-of-abstraction]] (new) — higher-level HBM parameters pool evidence from many lower variables, so abstractions are learned from little data (p. 1284)
- [[nonparametric-bayes]] (new) — models with unbounded structure but finitely many active degrees of freedom; includes CRP, IBP (p. 1284)
- [[chinese-restaurant-process]] (new) — nonparametric prior on classes; assimilate to an existing category or create a new one (p. 1284)
- [[suspicious-coincidence]] (new) — examples all inside a small set are improbable if drawn from a much larger one; favours specific hypotheses (p. 1281)
- [[marr-levels]] (new) — computational, algorithmic and implementation levels of analysis (p. 1284)

## Canonical instances
- [[tufa-word-learning]] — a few examples of a novel object word; generalization modelled as inference over a tree (Fig. 1) (p. 1280)
- [[cough-diagnosis]] — John's cough: likelihood favours cold and lung disease, prior favours cold and heartburn (pp. 1280–1281)
- [[horse-generalization]] — why "horse" extends to all and only horses (p. 1281)
- [[structural-form-discovery]] — HBM finds tree, chain, ring, cylinder, grid forms (Fig. 2) (p. 1282)
- [[disease-symptom-schema]] — three-level HBM learns the diseases → symptoms framework from 16-variable data (Fig. 3) (p. 1283)

## Bridges (candidates)
- [structural-analogy] Top level of an HBM supplying the hypothesis space for the level below ↔ bayesian: hierarchical models and partial pooling — higher-level parameters shared across groups are informed by all groups.
- [structural-analogy] Automatic introduction of new classes only when data demand it (CRP/Occam's razor) ↔ bayesian: Bayesian Occam's razor via marginal likelihood — complexity is penalized without a hand-set cost.
- [structural-analogy] Causal structure learned as a directed graph with a schema prior ↔ causal inference: causal DAGs — nodes and directed edges encode causal assumptions; the paper also links this to interventions.
- [metaphor] "Suspicious coincidence" ↔ bayesian: likelihood penalizing broad hypotheses — specific hypotheses assign higher probability to tightly clustered data.

## Questions this raises
- How exactly does the marginal likelihood make a three-level HBM learn faster despite having more degrees of freedom?
- Which approximate inference algorithms, such as sampling, do human minds actually use, and how can we test them?
- If hypothesis-space restriction helps only when the truth lies near it, how can a learner detect that its framework is wrong?
- Can concepts like "agent" or "object" be learned the way causality is claimed to be, and do children learn them so?

## Reading notes
- Printed pages 1279–1285 are the article. Printed 1286 is a permissions/ordering page. pdf N = printed − 1278.
- The text layer is garbled for Eq. (1) and some Fig. 3 panel labels. I checked Eq. (1) against the page image of p. 1280.
- Misprints visible in the source: "ouputs" (p. 1279); an unclosed parenthesis in "(or connectionism." (p. 1279); reference 66 prints "(Publisher, City, Country, 2008)" as a placeholder; citations "(39, 38)" appear in this order (p. 1284).
- The $n-1$ hypothesis count for binary-tree branches (p. 1281) is reported as printed. Supporting Online Material (figs. S1–S5, mentioned on pp. 1282, 1284) was not provided.
- The unit has no exercises.
