---
field: Complex systems
slug: complex-systems
layer: application
compiled: 2026-10-11
---
# Complex systems — Canon

## Scope
This catalog covers complex systems science as an application layer: the conceptual definition of complexity and emergence; nonlinear dynamics and chaos as the mathematical core; emergence of macro patterns from micro rules in social systems and agent-based models; criticality, tipping points and scaling laws; and the textbooks and courses that tie these together. Network science is included only to the extent it is load-bearing for complex-systems arguments (small worlds, preferential attachment, complex contagion), since the reader already knows it well; graduate network texts (e.g., Newman 2018) are deliberately left out. Statistical-physics treatments of social dynamics are included because they are the bridge to formal re-reading through information theory, linear algebra and game theory. Out of scope: complex adaptive systems in biology/ecology for their own sake, systems engineering/system dynamics (Forrester-style), and machine-learning-for-complex-systems. Syllabus triangulation used the Santa Fe Institute Complexity Explorer "Introduction to Complexity" syllabus, the UVM "Principles of Complex Systems" (PoCS) course description (scaling, simple vs. complicated models, micro mechanisms to macro phenomena, networks, contagion), the chapter structure of Sayama's open textbook (Binghamton), and Thurner, Hanel & Klimek (CSH Vienna).

## Canon

### Strand: What complexity is

#### weaver-1948-complexity
- **type:** paper
- **citation:** Weaver, W. (1948). *Science and Complexity*. American Scientist, 36, 536 ff. (adapted from ch. 1 of *The Scientists Speak*, 1947). Reprinted in Krakauer (ed.), *Foundational Papers in Complexity Science*, Vol. 1 (SFI Press, 2024).
- **tier:** deep
- **level:** UG
- **why:** The founding taxonomy: problems of simplicity (few variables), of disorganized complexity (many variables, tamed by statistics), and of organized complexity (many interacting variables that are neither). Almost every later definition of a "complex system" is a refinement of Weaver's middle ground, and it reads in under an hour.
- **focus:** whole
- **access:** need-copy
- **verified:** https://sfipress.org/books/foundational-papers-in-complexity-science ; https://www.academia.edu/29663527/SCIENCE_AND_COMPLEXITY

#### simon-1962-architecture
- **type:** paper
- **citation:** Simon, H. A. (1962). *The Architecture of Complexity*. Proceedings of the American Philosophical Society, 106(6), 467–482. JSTOR 985254.
- **tier:** core
- **level:** UG
- **why:** Argues that complex systems tend to be hierarchic and "nearly decomposable": strong interactions within subsystems, weak ones between them. The watchmaker parable (Tempus vs. Hora) explains why stable intermediate forms make evolution of complexity fast. This is the conceptual root of modularity, community structure and multi-scale modeling.
- **focus:** whole (the watchmaker parable and the near-decomposability section are the essentials)
- **access:** need-copy
- **verified:** https://apice.unibo.it/xwiki/bin/view/Publication/ComplexitySimon1962

#### anderson-1972-moreisdifferent
- **type:** paper
- **citation:** Anderson, P. W. (1972). *More Is Different*. Science, 177(4047), 393–396. https://doi.org/10.1126/science.177.4047.393
- **tier:** core
- **level:** UG
- **why:** A Nobel physicist's manifesto against naive constructionism: reductionism can be true while "reconstructing the universe from the laws" fails, because broken symmetry creates new levels with their own laws. It is the standard citation for emergence as a scientific (not mystical) claim.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1126/science.177.4047.393

#### mitchell-2009-guidedtour
- **type:** book
- **citation:** Mitchell, M. (2009). *Complexity: A Guided Tour*. Oxford University Press.
- **tier:** core
- **level:** HS
- **why:** The best single on-ramp to the whole field, written by an SFI researcher, covering dynamics/chaos, information, computation, evolution, cellular automata, networks and scaling in plain language. It also surveys the competing definitions of complexity, so the reader learns that the field has no single definition.
- **focus:** Part One "Background and History" (What is complexity?; Dynamics, chaos, and prediction; Information; Computation; Defining and measuring complexity); "Cellular automata, life, and the universe"; Part Four "Network Thinking" (The mystery of scaling); Conclusion "The past and future of the sciences of complexity"
- **access:** need-copy
- **translation:** 『ガイドツアー 複雑系の世界：サンタフェ研究所講義ノートから』メラニー・ミッチェル著、高橋洋訳、紀伊國屋書店
- **verified:** https://vufind.katalog.k.utb.cz/Record/53841/TOC ; https://shopping.bookoff.co.jp/new/0016743318

#### ladyman-2013-whatiscomplex
- **type:** paper
- **citation:** Ladyman, J., Lambert, J., & Wiesner, K. (2013). *What is a complex system?* European Journal for Philosophy of Science, 3(1), 33–67. https://doi.org/10.1007/s13194-012-0056-8
- **tier:** deep
- **level:** grad
- **why:** A philosophy-of-science audit of the many definitions of complexity, separating necessary from merely typical features (many interacting elements, disorder, robustness, emergence, hierarchy, memory, nonlinearity, feedback) and reviewing quantitative complexity measures. It is the go-to reference for writing a defensible definition in a paper.
- **focus:** whole
- **access:** free: https://philsci-archive.pitt.edu/id/eprint/8496/1/LLW-withoutFig-withAuthors.pdf
- **verified:** https://philsci-archive.pitt.edu/8496/ ; https://api.crossref.org/works/10.1007/s13194-012-0056-8

### Strand: Nonlinear dynamics and chaos

#### strogatz-2024-nonlinear
- **type:** book
- **citation:** Strogatz, S. H. (2024). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering* (3rd ed.). Chapman & Hall/CRC Press. (2nd ed. 2015 is equally usable.)
- **tier:** core
- **level:** UG
- **why:** The standard textbook for building geometric intuition about fixed points, stability, bifurcations, limit cycles and chaos, with applications drawn from many sciences. Almost every tipping-point or opinion-dynamics argument in social science silently relies on concepts taught in its first eight chapters.
- **focus:** Ch. 2 Flows on the Line; Ch. 3 Bifurcations; Ch. 5 Linear Systems; Ch. 6 Phase Plane; Ch. 8 Bifurcations Revisited; Ch. 9 Lorenz Equations; Ch. 10 One-Dimensional Maps; Ch. 13 Kuramoto Model (new in 3rd ed.)
- **access:** need-copy
- **translation:** 『ストロガッツ 非線形ダイナミクスとカオス：数学的基礎から物理・生物・化学・工学への応用まで』丸善出版（2015年頃、旧版の翻訳）
- **verified:** https://www.routledge.com/Nonlinear-Dynamics-and-Chaos-With-Applications-to-Physics-Biology-Chemistry-and-Engineering/Strogatz/p/book/9780367026509 ; https://synchro4.ee.uec.ac.jp/author/uec_tanaka/page/5/

#### may-1976-logistic
- **type:** paper
- **citation:** May, R. M. (1976). *Simple mathematical models with very complicated dynamics*. Nature, 261(5560), 459–467. https://doi.org/10.1038/261459a0
- **tier:** deep
- **level:** UG
- **why:** Shows that the one-line logistic difference equation passes through period-doubling into chaos, and pleads that every student meet it early. It is the canonical demonstration that deterministic simplicity does not imply predictable behavior, which is the lesson behind all "simple rules, complex outcomes" claims in social modeling.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1038/261459a0

#### lorenz-1963-nonperiodic
- **type:** paper
- **citation:** Lorenz, E. N. (1963). *Deterministic Nonperiodic Flow*. Journal of the Atmospheric Sciences, 20(2), 130–141. https://doi.org/10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2
- **tier:** reference
- **level:** grad
- **why:** The original discovery of sensitive dependence on initial conditions in a three-variable convection model (the Lorenz attractor). Read it after Strogatz Ch. 9 for the historical source of "chaos" and the limits of prediction.
- **focus:** whole (skim the derivation; focus on the numerical results and the discussion of predictability)
- **access:** free: https://wind.mit.edu/~emanuel/Lorenz/EdLorenz/Deterministic_63.pdf
- **verified:** https://wind.mit.edu/~emanuel/Lorenz/EdLorenz/publications_all.htm ; https://api.crossref.org/works/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2

### Strand: Emergence in social systems and agent-based models

#### schelling-1971-segregation
- **type:** paper
- **citation:** Schelling, T. C. (1971). *Dynamic models of segregation*. Journal of Mathematical Sociology, 1(2), 143–186. https://doi.org/10.1080/0022250X.1971.9989794
- **tier:** core
- **level:** UG
- **why:** The paradigm case of emergence in social science: mild individual preferences about neighbors produce stark macro segregation that nobody intended. It also introduced tipping and the "micromotives vs. macrobehavior" framing that defines agent-based social science. (The book-length treatment is Schelling's *Micromotives and Macrobehavior*, 1978.)
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1080/0022250X.1971.9989794

#### granovetter-1978-threshold
- **type:** paper
- **citation:** Granovetter, M. (1978). *Threshold Models of Collective Behavior*. American Journal of Sociology, 83(6), 1420–1443. https://doi.org/10.1086/226707
- **tier:** core
- **level:** UG
- **why:** Models each person as having a threshold (how many others must act before they do) and shows that the distribution of thresholds, not average preferences, decides whether a riot or adoption cascade happens. Small changes to one person's threshold can flip the collective outcome, which is the core intuition behind cascade and misinformation-spread models.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1086/226707

#### epstein-1996-growing
- **type:** book
- **citation:** Epstein, J. M., & Axtell, R. L. (1996). *Growing Artificial Societies: Social Science from the Bottom Up*. Brookings Institution Press / MIT Press. 228 pp.
- **tier:** deep
- **level:** UG
- **why:** The Sugarscape book: agents on a resource landscape generate wealth inequality, migration, trade, disease and conflict from local rules. It codified the "generative" standard of explanation ("if you didn't grow it, you didn't explain it") that underlies LLM-agent social simulation today.
- **focus:** whole
- **access:** need-copy
- **verified:** https://www.brookings.edu/books/growing-artificial-societies/

#### axelrod-1997-culture
- **type:** paper
- **citation:** Axelrod, R. (1997). *The Dissemination of Culture: A Model with Local Convergence and Global Polarization*. Journal of Conflict Resolution, 41(2), 203–226. https://doi.org/10.1177/0022002797041002001
- **tier:** deep
- **level:** UG
- **why:** Agents with multi-feature cultures interact more with similar neighbors and become more similar, yet the population can freeze into distinct cultural regions. It is the canonical explanation of how homophily plus influence can preserve polarization, and a staple model in the physics of social dynamics.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1177/0022002797041002001

#### macy-2002-factors
- **type:** paper
- **citation:** Macy, M. W., & Willer, R. (2002). *From Factors to Actors: Computational Sociology and Agent-Based Modeling*. Annual Review of Sociology, 28, 143–166. https://doi.org/10.1146/annurev.soc.28.110601.141117
- **tier:** deep
- **level:** UG
- **why:** The sociology-side manifesto for agent-based modeling: move from variable-centered regressions ("factors") to interacting adaptive agents ("actors"). It reviews emergent structure and emergent norms, and states the methodological principles (keep agents simple, test robustness) that reviewers still apply.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1146/annurev.soc.28.110601.141117

#### castellano-2009-socialdynamics
- **type:** paper
- **citation:** Castellano, C., Fortunato, S., & Loreto, V. (2009). *Statistical physics of social dynamics*. Reviews of Modern Physics, 81(2), 591–646. https://doi.org/10.1103/RevModPhys.81.591
- **tier:** core
- **level:** grad
- **why:** The definitive review of opinion, cultural, language and crowd dynamics as interacting-particle systems: order/disorder transitions, the role of network topology, voter, majority-rule, Sznajd, bounded-confidence and Axelrod models. It is the map of formal social-dynamics models and the most direct bridge from complexity to statistical mechanics and information theory.
- **focus:** Sec. II General framework (A. Order and disorder: the Ising paradigm; B. Role of topology; C. Dynamical systems approach; D. Agent-based modeling); Sec. III Opinion dynamics (voter, majority rule, social impact, Sznajd, bounded confidence, empirical data); Sec. IV Cultural dynamics (Axelrod model); Sec. IX Social spreading phenomena; Sec. X Coevolution of states and topology
- **access:** free: https://arxiv.org/pdf/0710.3256
- **verified:** https://export.arxiv.org/abs/0710.3256 ; https://api.crossref.org/works/10.1103/RevModPhys.81.591

#### centola-2007-complexcontagion
- **type:** paper
- **citation:** Centola, D., & Macy, M. (2007). *Complex Contagions and the Weakness of Long Ties*. American Journal of Sociology, 113(3), 702–734. https://doi.org/10.1086/521848
- **tier:** deep
- **level:** UG
- **why:** Distinguishes simple contagions (one contact suffices, like disease or news) from complex contagions (several reinforcing contacts needed, like risky behavior or norms). For complex contagions, the long-range ties that make small worlds fast can slow diffusion, overturning a naive reading of Granovetter's "strength of weak ties."
- **focus:** whole
- **access:** free: https://repository.upenn.edu/bitstreams/cf6e30c5-211d-4a6c-981b-ca61ea263dcc/download
- **verified:** https://repository.upenn.edu/asc_papers/590 ; https://api.crossref.org/works/10.1086/521848

### Strand: Networks (as complex-systems substrate)

#### watts-1998-smallworld
- **type:** paper
- **citation:** Watts, D. J., & Strogatz, S. H. (1998). *Collective dynamics of 'small-world' networks*. Nature, 393(6684), 440–442. https://doi.org/10.1038/30918
- **tier:** reference
- **level:** UG
- **why:** Shows that rewiring a few edges of a regular lattice gives short path lengths while keeping high clustering, and that this structure changes dynamics on the network. Listed as reference because the reader already knows network science; re-read it as a dynamics paper, not a topology paper.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1038/30918

#### barabasi-1999-scaling
- **type:** paper
- **citation:** Barabási, A.-L., & Albert, R. (1999). *Emergence of Scaling in Random Networks*. Science, 286(5439), 509–512. https://doi.org/10.1126/science.286.5439.509
- **tier:** reference
- **level:** UG
- **why:** Growth plus preferential attachment generates a power-law degree distribution, giving a mechanistic story for "scale-free" networks. Read alongside Clauset et al. (2009) for the necessary statistical skepticism about claimed power laws.
- **focus:** whole
- **access:** free: https://arxiv.org/pdf/cond-mat/9910332
- **verified:** https://export.arxiv.org/abs/cond-mat/9910332 ; https://api.crossref.org/works/10.1126/science.286.5439.509

#### barabasi-2016-networkscience
- **type:** book
- **citation:** Barabási, A.-L. (with Pósfai, M.) (2016). *Network Science*. Cambridge University Press. Free interactive edition at networksciencebook.com.
- **tier:** reference
- **level:** UG
- **why:** A free, well-illustrated reference textbook for the network concepts that complex-systems arguments use. It is useful mainly for looking up specific results (robustness, spreading) rather than reading cover to cover, given the reader's background.
- **focus:** Ch. 4 The Scale-Free Property; Ch. 5 The Barabási-Albert Model; Ch. 8 Network Robustness; Ch. 10 Spreading Phenomena
- **access:** free: https://networksciencebook.com/
- **verified:** https://networksciencebook.com/ (chapter titles from site bundle /js/app.js) ; https://api.openbd.jp/v1/get?isbn=9781107076266

### Strand: Criticality, scaling and tipping points

#### bak-1987-soc
- **type:** paper
- **citation:** Bak, P., Tang, C., & Wiesenfeld, K. (1987). *Self-organized criticality: An explanation of the 1/f noise*. Physical Review Letters, 59(4), 381–384. https://doi.org/10.1103/PhysRevLett.59.381
- **tier:** core
- **level:** grad
- **why:** Introduces the sandpile model: a slowly driven system organizes itself, with no parameter tuning, into a critical state where avalanches of all sizes follow power laws. Self-organized criticality became the field's flagship explanation for heavy tails and bursty cascades (including attention and information cascades). Bak's popular book *How Nature Works* (1996) is the gentle companion.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1103/PhysRevLett.59.381

#### scheffer-2009-earlywarning
- **type:** paper
- **citation:** Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., & Sugihara, G. (2009). *Early-warning signals for critical transitions*. Nature, 461(7260), 53–59. https://doi.org/10.1038/nature08227
- **tier:** core
- **level:** UG
- **why:** Shows that systems approaching a fold bifurcation recover more slowly from small shocks ("critical slowing down"), which shows up as rising variance and autocorrelation in time series. It turns tipping points from metaphor into something measurable, with direct use for climate, ecosystems, markets and opinion shifts.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1038/nature08227

#### bettencourt-2007-cities
- **type:** paper
- **citation:** Bettencourt, L. M. A., Lobo, J., Helbing, D., Kühnert, C., & West, G. B. (2007). *Growth, innovation, scaling, and the pace of life in cities*. PNAS, 104(17), 7301–7306. https://doi.org/10.1073/pnas.0610172104
- **tier:** deep
- **level:** UG
- **why:** City-level quantities scale as power laws of population: infrastructure sublinearly (economies of scale), and wages, patents and crime superlinearly, so larger cities are "faster." It is the core empirical paper behind West's popular book *Scale* and a model of how scaling exponents reveal social-network mechanisms.
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC1852329/pdf/zpq7301.pdf
- **verified:** https://pmc.ncbi.nlm.nih.gov/articles/PMC1852329/ ; https://api.crossref.org/works/10.1073/pnas.0610172104

#### clauset-2009-powerlaw
- **type:** paper
- **citation:** Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). *Power-Law Distributions in Empirical Data*. SIAM Review, 51(4), 661–703. https://doi.org/10.1137/070710111
- **tier:** deep
- **level:** grad
- **why:** The methodological corrective to the field's habit of seeing power laws everywhere: fit by maximum likelihood, choose x_min by minimizing the KS distance, test goodness-of-fit, and compare to lognormal and other alternatives with likelihood ratios. Many celebrated power laws fail the test, which is essential discipline for anyone measuring heavy-tailed social data.
- **focus:** Sec. 3 Fitting power laws to empirical data; Sec. 4 Testing the power-law hypothesis; Sec. 5 Alternative distributions; Sec. 6 Applications to real-world data
- **access:** free: https://arxiv.org/pdf/0706.1062
- **verified:** https://export.arxiv.org/abs/0706.1062 ; https://api.crossref.org/works/10.1137/070710111

### Strand: Textbooks and courses

#### sayama-2015-modeling
- **type:** book
- **citation:** Sayama, H. (2015). *Introduction to the Modeling and Analysis of Complex Systems*. Open SUNY Textbooks. ISBN 9781942341093. CC BY-NC-SA.
- **tier:** core
- **level:** UG
- **why:** A free, Python-based textbook that takes the reader from discrete and continuous dynamical systems through bifurcations, chaos, cellular automata, dynamical networks and agent-based models, with code throughout. It is the most efficient way for a daily Python user to turn the concepts in this canon into running models.
- **focus:** Ch. 4–5 Discrete-Time Models I–II; Ch. 7 Continuous-Time Models II: Analysis; Ch. 8 Bifurcations; Ch. 9 Chaos; Ch. 11–12 Cellular Automata I–II; Ch. 16–18 Dynamical Networks I–III; Ch. 19 Agent-Based Models
- **access:** free: https://knightscholar.geneseo.edu/cgi/viewcontent.cgi?article=1013&context=oer-ost
- **verified:** https://open.umn.edu/opentextbooks/textbooks/introduction-to-the-modeling-and-analysis-of-complex-systems ; https://knightscholar.geneseo.edu/oer-ost/14/

#### thurner-2018-theory
- **type:** book
- **citation:** Thurner, S., Hanel, R., & Klimek, P. (2018). *Introduction to the Theory of Complex Systems*. Oxford University Press. ISBN 9780198821939.
- **tier:** deep
- **level:** grad
- **why:** The most mathematical general textbook, treating complex systems through probability, scaling, networks, evolutionary processes and, distinctively, generalized entropies and information theory for non-ergodic, path-dependent systems. It is the natural graduate-depth bridge to the foundational information-theory and probability readings.
- **focus:** Ch. 1 Introduction to complex systems; Ch. 3 Scaling; Ch. 5 Evolutionary processes; Ch. 6 Statistical mechanics & information theory for complex systems
- **access:** need-copy
- **verified:** https://global.oup.com/academic/product/introduction-to-the-theory-of-complex-systems-9780198821939

#### page-2018-modelthinker
- **type:** book
- **citation:** Page, S. E. (2018). *The Model Thinker: What You Need to Know to Make Data Work for You*. Basic Books. ISBN 9780465094639.
- **tier:** reference
- **level:** UG
- **why:** A catalog of a few dozen core models (networks, diffusion, Markov processes, threshold and tipping models, game-theoretic models, and more) with the "many-model thinking" argument that combining models beats relying on any one. Useful as a lookup when deciding which model family fits a social phenomenon.
- **focus:** whole (use as a reference, model by model)
- **access:** need-copy
- **verified:** https://www.hachettebookgroup.com/titles/scott-e-page/the-model-thinker/9780465094639/

#### mitchell-nd-introcomplexity
- **type:** course
- **citation:** Mitchell, M. (instructor). *Introduction to Complexity*. Santa Fe Institute, Complexity Explorer (10 units, self-paced online course).
- **tier:** reference
- **level:** HS
- **why:** SFI's flagship free online course, effectively the video companion to Mitchell (2009), with NetLogo exercises. Its syllabus is a useful outside check on what the field considers introductory: what is complexity, dynamics and chaos, fractals, information, genetic algorithms, cellular automata, self-organization, cooperation, networks, and scaling.
- **focus:** Units "What is Complexity?", "Dynamics and Chaos", "Information, Order, and Randomness", "Models of Cooperation in Social Systems", "Scaling in Biology and Society"
- **access:** free: https://www.complexityexplorer.org/courses/185-introduction-to-complexity
- **verified:** https://www.complexityexplorer.org/courses/185-introduction-to-complexity

## Concept spine
- **complex system** — many interacting parts whose collective behavior is not obvious from the parts alone (UG)
- **organized vs. disorganized complexity** — Weaver's split between many-variable problems that statistics can average out and those with structured interactions that it cannot (UG)
- **emergence** — macro-level patterns or laws that arise from micro-level interactions and need their own description (UG)
- **more is different / constructionism** — reductionism can hold while rebuilding the whole from its parts still fails (UG)
- **hierarchy and near-decomposability** — systems built from subsystems that interact strongly inside and weakly between them (UG)
- **nonlinearity** — output not proportional to input, so the effect of the whole is not the sum of the effects of the parts (HS)
- **feedback (positive/negative)** — outputs loop back as inputs, amplifying or damping change (HS)
- **state space / phase space** — the space of all possible system states, where dynamics are trajectories (UG)
- **fixed point and stability** — a state that does not change, and whether small perturbations die out or grow (UG)
- **linear stability analysis** — judging a fixed point's stability from the eigenvalues of the Jacobian (UG)
- **attractor / basin of attraction** — the set the dynamics settle onto, and the initial states that lead there (UG)
- **bifurcation** — a qualitative change in dynamics as a parameter crosses a threshold (UG)
- **saddle-node (fold) bifurcation** — two fixed points collide and vanish, the mathematics of most tipping points (UG)
- **hysteresis** — the path back differs from the path forward, so reversing the cause need not reverse the effect (UG)
- **limit cycle** — an isolated periodic orbit, as in self-sustained oscillation (UG)
- **period-doubling route to chaos** — repeated doubling of a cycle's period as a parameter increases, ending in chaos (UG)
- **deterministic chaos** — bounded, aperiodic behavior from deterministic rules with sensitive dependence on initial conditions (UG)
- **Lyapunov exponent** — average exponential rate at which nearby trajectories separate (grad)
- **strange attractor / fractal** — an attractor with non-integer dimension and self-similar structure (grad)
- **synchronization** — coupled oscillators locking their rhythms, as in the Kuramoto model (UG)
- **agent-based model (ABM)** — simulation of autonomous agents following local rules, used to "grow" macro patterns (UG)
- **generative explanation** — explaining a pattern by showing that a population of agents can produce it (UG)
- **micromotives vs. macrobehavior** — individual intentions can produce collective outcomes nobody wants (UG)
- **tipping point** — a threshold beyond which a system shifts rapidly and often irreversibly to another state (UG)
- **threshold model** — each agent acts once enough others have acted, so cascades depend on the threshold distribution (UG)
- **cascade** — a chain reaction of adoptions or failures spreading through a population (UG)
- **simple vs. complex contagion** — spread that needs one exposure versus spread that needs multiple reinforcing exposures (UG)
- **homophily and social influence** — similar agents interact more, and interaction makes them more similar (UG)
- **order–disorder transition** — a phase transition between consensus/ordered and fragmented/disordered collective states (grad)
- **mean-field approximation** — replacing each agent's neighbors with the population average to get solvable equations (grad)
- **voter model / bounded confidence** — the canonical opinion-dynamics rules: copying a random neighbor, and interacting only with those close in opinion (grad)
- **small-world network** — high clustering combined with short average paths (UG)
- **preferential attachment** — new nodes link preferentially to already well-connected nodes ("rich get richer") (UG)
- **heavy tail / power law** — probability decays as a power of size, so extreme events are far more common than under a Gaussian (UG)
- **scale invariance** — no characteristic scale, so the system looks statistically similar across scales (UG)
- **self-organized criticality** — slowly driven systems that move on their own to a critical state with power-law avalanches (grad)
- **criticality / phase transition** — the boundary between qualitatively different collective phases, where fluctuations become large (grad)
- **critical slowing down** — slower recovery from perturbations near a tipping point, seen as rising autocorrelation and variance (UG)
- **early-warning signals** — statistical indicators in time series that warn of an approaching critical transition (UG)
- **allometric / urban scaling** — Y ∝ N^β relations, with β < 1 (economies of scale) or β > 1 (increasing returns) (UG)
- **robustness and fragility** — tolerance to random failure that can coexist with vulnerability to targeted shocks (UG)
- **path dependence** — history and early events lock in later outcomes (UG)
- **universality** — different microscopic systems share the same macro behavior near critical points (grad)
- **complexity measures** — quantitative proxies (algorithmic, statistical, logical depth, etc.), none universally accepted (grad)
- **many-model thinking** — using an ensemble of different simple models to reason about one phenomenon (UG)

## Canonical instances
- **Logistic map** — x_{t+1} = r x_t (1 − x_t): fixed point, period doubling, then chaos as r increases — may-1976-logistic
- **Lorenz attractor** — three coupled ODEs from convection that give the butterfly-shaped strange attractor and the limits of weather prediction — lorenz-1963-nonperiodic
- **Simon's watchmakers (Tempus and Hora)** — the watchmaker who builds from stable subassemblies wins when interrupted, an argument for why hierarchy evolves — simon-1962-architecture
- **Game of Life / elementary cellular automata** — grid cells with local update rules produce gliders and universal computation — mitchell-2009-guidedtour
- **Schelling segregation** — mildly picky agents relocate on a grid and produce stark segregation — schelling-1971-segregation
- **Granovetter riot threshold** — a uniform threshold distribution 0,1,2,…,99 produces a full riot; change one person's threshold and the cascade stops — granovetter-1978-threshold
- **Sugarscape** — agents harvesting sugar on a landscape grow skewed wealth, migration and trade — epstein-1996-growing
- **Axelrod culture model** — feature-vector cultures converge locally yet freeze into stable distinct regions globally — axelrod-1997-culture
- **Voter / Ising-type opinion models** — spins as opinions; consensus vs. disorder depends on dimension and network topology — castellano-2009-socialdynamics
- **Complex contagion on clustered lattices** — behaviors needing multiple exposures spread faster through clustered ties than through random long ties — centola-2007-complexcontagion
- **Small-world rewiring** — the Watts–Strogatz interpolation from lattice to random graph via rewiring probability p — watts-1998-smallworld
- **Preferential attachment** — the growth + rich-get-richer model that yields a power-law degree distribution — barabasi-1999-scaling
- **BTW sandpile** — grains added one at a time trigger toppling avalanches with power-law size distribution — bak-1987-soc
- **Fold bifurcation with critical slowing down** — a system nearing a saddle-node shows rising autocorrelation before a regime shift (lakes, climate, markets) — scheffer-2009-earlywarning
- **Urban scaling laws** — superlinear scaling of wages, patents and crime and sublinear scaling of infrastructure with city population — bettencourt-2007-cities

## Bridges
- [same-math] linear stability of fixed points ↔ linear algebra: eigenvalues of the Jacobian — whether a social equilibrium is stable is literally the sign (or modulus, for maps) of the eigenvalues of a linearized matrix.
- [same-math] epidemic/contagion threshold on networks ↔ linear algebra: spectral radius — in the standard mean-field SIS approximation the spreading threshold is 1/λ_max of the adjacency matrix.
- [same-math] critical slowing down ↔ linear algebra / time-series statistics: AR(1) autocorrelation — near a fold the dominant eigenvalue's real part approaches zero, so the lag-1 autocorrelation of a linearized noisy system rises toward 1.
- [same-math] Ising-type opinion models ↔ information theory: maximum-entropy distributions — the max-entropy distribution of binary states constrained by means and pairwise correlations is exactly the Ising/Boltzmann form.
- [same-math] Lyapunov exponents and chaos ↔ information theory: entropy rate — under suitable conditions Pesin's identity equates the Kolmogorov–Sinai entropy rate with the sum of positive Lyapunov exponents (chaos as information production).
- [same-math] power-law fitting ↔ Bayesian theory & causal inference: likelihood-based model comparison — Clauset et al.'s workflow is maximum likelihood plus likelihood-ratio tests; Bayesian model comparison is the direct extension.
- [structural-analogy] threshold cascades / complex contagion ↔ decision & game theory: information cascades and coordination games — similar cascade and tipping behavior can come from Bayesian observational learning or strategic complementarities, but the micro-mechanisms differ.
- [structural-analogy] Schelling segregation ↔ decision & game theory: potential games and inefficient equilibria — individually rational moves lead to a collectively unintended equilibrium, a micro-to-macro gap game theory formalizes.
- [structural-analogy] emergence / "more is different" ↔ analytic philosophy: reduction, supervenience and multiple realizability — Anderson's and Ladyman et al.'s claims are scientific versions of these philosophical debates.
- [structural-analogy] agent-based models ↔ communication theory and theory of mind: diffusion of innovations and agents' models of others — ABMs formalize two-step-flow and diffusion ideas, and LLM-based agents raise the question of how much theory of mind an agent needs before the macro pattern changes.
