---
field: Decision & game theory
slug: decision-game-theory
layer: foundation
compiled: 2026-10-11
---
# Decision & game theory — Canon

## Scope
This canon covers how agents should choose, and how they actually choose, alone and when other agents' choices matter. It has seven strands. (1) Axiomatic expected-utility theory and the paradoxes that challenge it. (2) Behavioral decision research: heuristics, prospect theory and framing, bounded rationality, and Gigerenzer's ecological-rationality counterpoint. (3) Non-cooperative game theory from Nash and Harsanyi, with textbooks, an on-ramp and a lecture course. (4) Common knowledge, conventions and focal points. (5) Behavioral and level-k game theory, plus quantal response. (6) Cooperation and evolutionary game theory. (7) A short entry point to mechanism design.

Some works are deliberately left to other canons. Lewis's *Convention* (1969) lives in analytic-philosophy. Arrow's social choice (1951) and Ostrom (1990) live in political-science. Ramsey's "Truth and Probability" (1926/1931) was dropped because its 1931 edition details could not be fully verified this round. Fudenberg & Tirole was dropped for space; Osborne & Rubinstein serves as the graduate reference.

The reading list was checked against three syllabi: Yale ECON 159 (Polak), MIT 14.12 (Gibbons text) and MIT 14.13 Psychology & Economics (Schilbach).

## Canon

### Strand: Rational choice & expected utility

#### vonneumann-1944-games
- **type:** book
- **citation:** von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press. 60th Anniversary Commemorative Edition (2004/2007), with an introduction by H. W. Kuhn and an afterword by A. Rubinstein, 776 pp.
- **tier:** reference
- **level:** grad
- **why:** This is the founding text of game theory. It proposed treating economic interaction as a "game of strategy" and proved the zero-sum minimax machinery. Its utility appendix gave the axioms behind von Neumann–Morgenstern (cardinal) expected utility. Read it for its framing and its axioms, not as a textbook.
- **focus:** Ch. I "Formulation of the Economic Problem"; Appendix "The Axiomatic Treatment of Utility"; skim Ch. III "Zero-Sum Two-Person Games: Theory".
- **access:** need-copy
- **translation:** JA: 『ゲームの理論と経済行動』 (銀林浩ほか訳, 東京図書); ZH: 《博弈论与经济行为》 (王文玉、王宇译, 生活·读书·新知三联书店)
- **verified:** https://press.princeton.edu/books/paperback/9780691130613/theory-of-games-and-economic-behavior

#### savage-1954-foundations
- **type:** book
- **citation:** Savage, L. J. (1954). *The Foundations of Statistics*. Wiley. 2nd rev. ed., Dover Publications, 1972, 310 pp.
- **tier:** deep
- **level:** grad
- **why:** Savage derives subjective probability and expected utility together from postulates about preferences over acts. One of them is the "sure-thing principle" that Allais and Ellsberg later attacked. This is the standard axiomatic basis for Bayesian decision theory, and the book every later decision paradox is measured against.
- **focus:** whole (chapter-level table of contents not verified; the opening chapters, which build the postulates, are the essential part)
- **access:** need-copy
- **verified:** https://openlibrary.org/works/OL6612530W (Wiley 1954 / Dover 1972 editions); https://store.doverpublications.com/products/9780486623498

#### allais-1953-paradox
- **type:** paper
- **citation:** Allais, M. (1953). Le Comportement de l'Homme Rationnel devant le Risque: Critique des Postulats et Axiomes de l'Ecole Americaine. *Econometrica*, 21(4), 503 ff. DOI: 10.2307/1907921
- **tier:** deep
- **level:** grad
- **why:** This paper gives the original "common consequence" choice problems. Most people's answers violate the independence axiom of expected utility. The Allais paradox is the founding anomaly behind non-expected-utility theories, including prospect theory's probability weighting. The paper is in French; most readers meet the paradox through textbook restatements.
- **focus:** the choice examples that state the paradox
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.2307/1907921 (start page verified; end page not confirmed)

#### ellsberg-1961-ambiguity
- **type:** paper
- **citation:** Ellsberg, D. (1961). Risk, Ambiguity, and the Savage Axioms. *The Quarterly Journal of Economics*, 75(4), 643–669. DOI: 10.2307/1884324
- **tier:** deep
- **level:** UG
- **why:** Ellsberg used urn thought-experiments to show that people prefer known odds to unknown odds. This "ambiguity aversion" cannot be squared with any single subjective probability, so it breaks Savage's framework. It separates *risk* (known probabilities) from *ambiguity* (unknown probabilities), which matters for how publics react to uncertain science communication.
- **focus:** whole (short)
- **access:** need-copy
- **verified:** https://ideas.repec.org/a/oup/qjecon/v75y1961i4p643-669..html

### Strand: Behavioral decision & bounded rationality

#### simon-1955-behavioral
- **type:** paper
- **citation:** Simon, H. A. (1955). A Behavioral Model of Rational Choice. *The Quarterly Journal of Economics*, 69(1), 99–118. DOI: 10.2307/1884852
- **tier:** core
- **level:** UG
- **why:** Simon replaced the omniscient maximizer with an agent who has limited computation and information. That agent searches until an option meets an aspiration level ("satisficing"). Bounded rationality starts here, and both the heuristics-and-biases school and the ecological-rationality school claim this paper.
- **focus:** whole
- **access:** need-copy
- **verified:** https://ideas.repec.org/a/oup/qjecon/v69y1955i1p99-118..html

#### tversky-1974-heuristics
- **type:** paper
- **citation:** Tversky, A., & Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. *Science*, 185(4157), 1124–1131. DOI: 10.1126/science.185.4157.1124
- **tier:** core
- **level:** UG
- **why:** This paper names three judgment heuristics: representativeness, availability, and anchoring-and-adjustment. It shows the systematic biases each one produces. It is the manifesto of the heuristics-and-biases program and the vocabulary behind most work on misinformation susceptibility.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1126/science.185.4157.1124

#### kahneman-1979-prospect
- **type:** paper
- **citation:** Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. *Econometrica*, 47(2), 263–291. DOI: 10.2307/1914185
- **tier:** core
- **level:** grad
- **why:** Prospect theory is the leading descriptive alternative to expected utility. People value gains and losses relative to a reference point, with losses looming larger (loss aversion). They also weight probabilities non-linearly. This is one of the most-cited papers in economics, and the MIT 14.13 syllabus assigns it as required reading.
- **focus:** whole; the empirical "effects" sections first, then the value and weighting functions
- **access:** need-copy
- **verified:** https://ideas.repec.org/a/ecm/emetrp/v47y1979i2p263-91.html

#### tversky-1981-framing
- **type:** paper
- **citation:** Tversky, A., & Kahneman, D. (1981). The Framing of Decisions and the Psychology of Choice. *Science*, 211(4481), 453–458. DOI: 10.1126/science.7455683
- **tier:** deep
- **level:** UG
- **why:** This paper introduces the "Asian disease" problem. Logically equivalent descriptions ("200 saved" versus "400 die") reverse people's preferences, which violates description invariance. It is the bridge between decision theory and framing research in communication.
- **focus:** whole (short)
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1126/science.7455683

#### gigerenzer-2009-homo-heuristicus
- **type:** paper
- **citation:** Gigerenzer, G., & Brighton, H. (2009). Homo Heuristicus: Why Biased Minds Make Better Inferences. *Topics in Cognitive Science*, 1(1), 107–143. DOI: 10.1111/j.1756-8765.2008.01006.x
- **tier:** deep
- **level:** grad
- **why:** This is the counterweight to heuristics-and-biases. Simple heuristics can out-predict complex models when matched to the structure of the environment ("ecological rationality", "less-is-more"). The authors argue this through the bias–variance dilemma familiar from machine learning. It reframes "bias" as a possible adaptive trade-off rather than an error.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1111/j.1756-8765.2008.01006.x

#### kahneman-2011-thinking
- **type:** book
- **citation:** Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux, 1st ed., 499 pp.
- **tier:** core
- **level:** HS
- **why:** Kahneman's own popular synthesis of the heuristics-and-biases and prospect-theory programs, built around the System 1/System 2 metaphor. Use it as the on-ramp before the 1974, 1979 and 1981 papers. Read the priming material in Part I critically, because several studies cited there have since failed to replicate.
- **focus:** Part II "Heuristics and Biases"; Part IV "Choices" (includes "Bernoulli's Errors", "Prospect Theory", "The Fourfold Pattern", "Frames and Reality"); Part I "Two Systems" for the framing metaphor.
- **access:** need-copy
- **translation:** JA: 『ファスト＆スロー：あなたの意思はどのように決まるか？』
- **verified:** https://openlibrary.org/isbn/9780374275631

### Strand: Non-cooperative game theory

#### nash-1950-equilibrium
- **type:** paper
- **citation:** Nash, J. F. (1950). Equilibrium Points in n-Person Games. *Proceedings of the National Academy of Sciences*, 36(1), 48–49. DOI: 10.1073/pnas.36.1.48
- **tier:** core
- **level:** grad
- **why:** In two pages, Nash defines the equilibrium point (each player best-responds to the others) and proves via Kakutani's fixed-point theorem that every finite game has one in mixed strategies. Almost everything in non-cooperative game theory rests on this. The fuller version is Nash (1951), "Non-Cooperative Games", *Annals of Mathematics* 54(2), 286–295.
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC1063129/
- **verified:** https://api.crossref.org/works/10.1073/pnas.36.1.48

#### harsanyi-1967-incomplete
- **type:** paper
- **citation:** Harsanyi, J. C. (1967–68). Games with Incomplete Information Played by "Bayesian" Players, I–III. *Management Science*: Part I "The Basic Model", 14(3), 159–182; Part II "Bayesian Equilibrium Points", 14(5), 320–334; Part III "The Basic Probability Distribution of the Game", 14(7), 486–502. DOI (Part I): 10.1287/mnsc.14.3.159
- **tier:** deep
- **level:** grad
- **why:** Harsanyi turned uncertainty about other players' payoffs into "types" drawn by Nature from a common prior. This made incomplete-information games analysable as Bayesian games, the basis of signaling, auctions and mechanism design. It is the formal home of "beliefs about beliefs".
- **focus:** Part I first; Part II for Bayesian equilibrium
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1287/mnsc.14.3.159 ; https://api.crossref.org/works/10.1287/mnsc.14.5.320 ; https://api.crossref.org/works/10.1287/mnsc.14.7.486

#### osborne-2004-introduction
- **type:** book
- **citation:** Osborne, M. J. (2004). *An Introduction to Game Theory*. Oxford University Press.
- **tier:** core
- **level:** UG
- **why:** The clearest rigorous undergraduate text. It builds each concept from many worked examples (Prisoner's Dilemma, BoS, Stag Hunt, Hawk–Dove, public goods). It assumes only basic maths, so it is the right primary textbook to work through with exercises.
- **focus:** Ch. 1 Introduction; Ch. 2 Nash Equilibrium: Theory; Ch. 3 Nash Equilibrium: Illustrations; Ch. 4 Mixed Strategy Equilibrium; Ch. 5 Extensive Games with Perfect Information: Theory; Ch. 9 Bayesian Games; Ch. 13 Evolutionary Equilibrium; Ch. 14 Repeated Games: The Prisoner's Dilemma.
- **access:** need-copy (penultimate-draft chapters 1–3 are free on the author's site: https://www.economics.utoronto.ca/osborne/igt/nash.pdf and https://www.economics.utoronto.ca/osborne/igt/INDEXR.HTM)
- **verified:** https://www.economics.utoronto.ca/osborne/igt/TOC.HTM

#### osborne-1994-course
- **type:** book
- **citation:** Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press, 352 pp.
- **tier:** reference
- **level:** grad
- **why:** A compact, rigorous graduate text, unusually careful about what solution concepts *mean*. It has a whole chapter on knowledge and equilibrium. The authors distribute it free, so it serves as the graduate reference in place of Fudenberg & Tirole.
- **focus:** Ch. 2 Nash Equilibrium; Ch. 3 Mixed, Correlated, and Evolutionary Equilibrium; Ch. 4 Rationalizability and Iterated Elimination of Dominated Actions; Ch. 5 Knowledge and Equilibrium; Ch. 8 Repeated Games; Ch. 10 Implementation Theory.
- **access:** free: https://books.osborne.economics.utoronto.ca/ (free PDF after registration with the authors)
- **translation:** ZH: 《博弈论教程》 (魏玉根译, 中国社会科学出版社)
- **verified:** https://www.economics.utoronto.ca/osborne/cgt/TOC.HTM

#### dixit-2008-art-strategy
- **type:** book
- **citation:** Dixit, A. K., & Nalebuff, B. J. (2008). *The Art of Strategy: A Game Theorist's Guide to Success in Business and Life*. W. W. Norton, 512 pp. (Successor to their *Thinking Strategically*, Norton, 1991, which the Yale ECON 159 syllabus lists.)
- **tier:** core
- **level:** HS
- **why:** The best non-technical on-ramp, written by two leading theorists. It teaches backward induction, commitment, credible threats, mixed strategies and brinkmanship through stories, giving strategic intuition before the formal apparatus.
- **focus:** whole
- **access:** need-copy
- **translation:** JA: 『戦略的思考をどう実践するか：エール大学式「ゲーム理論」の活用法』 (嶋津祐一・池村千秋訳, 阪急コミュニケーションズ)
- **verified:** https://openlibrary.org/isbn/9780393062434

#### polak-2007-econ159
- **type:** course
- **citation:** Polak, B. (2007). *ECON 159: Game Theory* (24 video lectures, Fall 2007). Open Yale Courses, Yale University.
- **tier:** core
- **level:** UG
- **why:** A widely used free lecture course that builds the theory from applied examples (soccer, dating, voting, bank runs, auctions). It covers dominance, Nash equilibrium, mixed strategies, evolutionary stability, backward induction, subgame perfection, repeated games and asymmetric information. Pair it with Osborne for exercises.
- **focus:** L1 "Introduction: Five First Lessons"; L2 "Putting Yourselves into Other People's Shoes"; L5–6 Nash equilibrium; L9 "Mixed Strategies in Theory and Tennis"; L11–12 Evolutionary Stability; L17 "Backward Induction: Ultimatums and Bargaining"; L21–22 Repeated Games; L23 "Asymmetric Information: Silence, Signaling and Suffering Education".
- **access:** free: https://oyc.yale.edu/node/668
- **verified:** https://oyc.yale.edu/node/668

### Strand: Common knowledge, conventions & focal points

#### schelling-1960-conflict
- **type:** book
- **citation:** Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press. (Paperback reissue with a new preface by the author, Harvard University Press, 1981, 328 pp.)
- **tier:** core
- **level:** UG
- **why:** Schelling's "reorientation of game theory" toward mixed-motive bargaining. It introduces focal points (tacit coordination on salient solutions), commitment, and "the threat that leaves something to chance". Game theory meets communication here: what is *said* and what is *salient* changes equilibria.
- **focus:** Part I "Elements of a Theory of Strategy" (esp. "An Essay on Bargaining"; "Bargaining, Communication, and Limited War"); Part II "A Reorientation of Game Theory" (esp. "Toward a Theory of Interdependent Decision"); Part III "The Threat That Leaves Something to Chance".
- **access:** need-copy
- **translation:** JA: 『紛争の戦略：ゲーム理論のエッセンス』 (河野勝監訳, 勁草書房); ZH: 《冲突的战略》 (赵华等译, 华夏出版社)
- **verified:** https://openlibrary.org/isbn/9780674840317 ; https://openlibrary.org/works/OL2259845W (1960 HUP first edition)

#### aumann-1976-agreeing
- **type:** paper
- **citation:** Aumann, R. J. (1976). Agreeing to Disagree. *The Annals of Statistics*, 4(6), 1236–1239. DOI: 10.1214/aos/1176343654
- **tier:** deep
- **level:** grad
- **why:** In four pages, Aumann gives the first formal definition of common knowledge (via information partitions). It proves that Bayesians with a common prior cannot have commonly known posteriors that differ. This is the formal anchor for every later discussion of persistent disagreement and polarization among "rational" agents.
- **focus:** whole
- **access:** free: https://projecteuclid.org/journals/annals-of-statistics/volume-4/issue-6/Agreeing-to-Disagree/10.1214/aos/1176343654.full
- **verified:** https://api.crossref.org/works/10.1214/aos/1176343654 ; https://plato.stanford.edu/entries/convention/ (bibliography)

#### rubinstein-1989-email
- **type:** paper
- **citation:** Rubinstein, A. (1989). The Electronic Mail Game: Strategic Behavior under "Almost Common Knowledge." *American Economic Review*, 79(3), 385–391.
- **tier:** deep
- **level:** grad
- **why:** Players coordinate through a chain of confirmation messages, and any message can be lost. No finite number of confirmations ever produces common knowledge, and coordination can unravel completely. It shows that "almost common knowledge" behaves very differently from common knowledge, a sharp result for any theory of communication and coordination.
- **focus:** whole (short)
- **access:** need-copy
- **verified:** https://ideas.repec.org/a/aea/aecrev/v79y1989i3p385-91.html

#### geanakoplos-1992-common-knowledge
- **type:** paper
- **citation:** Geanakoplos, J. (1992). Common Knowledge. *Journal of Economic Perspectives*, 6(4), 53–82. DOI: 10.1257/jep.6.4.53
- **tier:** core
- **level:** UG
- **why:** The best expository survey. It starts from puzzles (the hats, envelopes and detectives puzzles), builds the partition model of knowledge, and then derives agreeing-to-disagree, no-speculation results and the coordinated-attack problem studied by Rubinstein. Read this before Aumann and Rubinstein.
- **focus:** whole; sections "Puzzles About Reasoning Based on the Reasoning of Others", "Interactive Epistemology", "Characterizing Common Knowledge of Events and Actions", "Speculation", "Infinite State Spaces and Knowledge about Knowledge to Level N"
- **access:** free: https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.6.4.53
- **verified:** https://api.crossref.org/works/10.1257/jep.6.4.53

### Strand: Behavioral game theory & level-k

#### nagel-1995-guessing
- **type:** paper
- **citation:** Nagel, R. (1995). Unraveling in Guessing Games: An Experimental Study. *American Economic Review*, 85(5), 1313–1326.
- **tier:** deep
- **level:** UG
- **why:** This is the first systematic experiment on the "guess p times the average" game, Keynes's beauty contest made precise. Choices cluster at one or two steps of iterated reasoning rather than at the Nash equilibrium of zero. It is the empirical seed of level-k and cognitive-hierarchy models.
- **focus:** whole
- **access:** need-copy
- **verified:** https://ideas.repec.org/a/aea/aecrev/v85y1995i5p1313-26.html

#### camerer-2004-cognitive-hierarchy
- **type:** paper
- **citation:** Camerer, C. F., Ho, T.-H., & Chong, J.-K. (2004). A Cognitive Hierarchy Model of Games. *The Quarterly Journal of Economics*, 119(3), 861–898. DOI: 10.1162/0033553041502225
- **tier:** deep
- **level:** grad
- **why:** This paper formalizes bounded strategic depth. Level-k players best-respond to a (Poisson) mix of lower-level players, and a single parameter (average thinking steps) fits many games better than Nash equilibrium. It is a ready-made template for modeling or benchmarking LLM agents' depth of strategic reasoning.
- **focus:** whole
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1162/0033553041502225

#### mckelvey-1995-qre
- **type:** paper
- **citation:** McKelvey, R. D., & Palfrey, T. R. (1995). Quantal Response Equilibria for Normal Form Games. *Games and Economic Behavior*, 10(1), 6–38. DOI: 10.1006/game.1995.1023
- **tier:** deep
- **level:** grad
- **why:** QRE replaces exact best responses with noisy, probabilistic ones (typically a logit rule with a precision parameter λ), each consistent with the others' noisy play. It recovers Nash as λ→∞ and fits experimental deviations, and it is the standard stochastic-choice equilibrium for structural estimation.
- **focus:** whole; the logit QRE definition first
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1006/game.1995.1023

#### camerer-2003-bgt
- **type:** book
- **citation:** Camerer, C. F. (2003). *Behavioral Game Theory: Experiments in Strategic Interaction*. Princeton University Press / Russell Sage Foundation (Roundtable Series in Behavioral Economics), 544 pp.
- **tier:** deep
- **level:** grad
- **why:** The standard synthesis of experimental game theory. It covers what people actually do in ultimatum, dictator, trust, coordination, bargaining and dominance-solvable games, and which models (social preferences, learning, limited thinking) explain it. Use it as the evidence base against which textbook equilibria are checked.
- **focus:** whole (chapter list not verified)
- **access:** need-copy
- **translation:** ZH: 《行为博弈：对策略互动的实验研究》 (贺京同等译, 中国人民大学出版社)
- **verified:** https://openlibrary.org/isbn/9780691090399 ; https://press.princeton.edu/books/hardcover/9780691090399/behavioral-game-theory

### Strand: Cooperation & evolution

#### axelrod-1984-cooperation
- **type:** book
- **citation:** Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books. (Revised ed., Basic Books, 2006, 241 pp.)
- **tier:** core
- **level:** HS
- **why:** Axelrod ran computer tournaments of the iterated Prisoner's Dilemma, which TIT FOR TAT won. He drew lessons about when cooperation emerges without a central authority: be nice, retaliatory, forgiving and clear, and keep "the shadow of the future" long. This is the classic computational-social-science demonstration of cooperation through repeated interaction. (Core paper: Axelrod & Hamilton 1981, *Science* 211(4489), 1390–1396.)
- **focus:** whole
- **access:** need-copy
- **translation:** JA: 『つきあい方の科学：バクテリアから国際関係まで』 (松田裕之訳, ミネルヴァ書房); ZH: 《合作的进化》 (吴坚忠译, 上海人民出版社)
- **verified:** https://openlibrary.org/works/OL2620286W

#### maynardsmith-1973-animal-conflict
- **type:** paper
- **citation:** Maynard Smith, J., & Price, G. R. (1973). The Logic of Animal Conflict. *Nature*, 246(5427), 15–18. DOI: 10.1038/246015a0
- **tier:** deep
- **level:** UG
- **why:** This paper introduces the evolutionarily stable strategy (ESS): a strategy that, once common, cannot be invaded by rare mutants. The authors use it to explain why animal contests are often "limited wars". It founded evolutionary game theory, where equilibrium comes from selection rather than rationality.
- **focus:** whole (short)
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1038/246015a0

#### nowak-2006-five-rules
- **type:** paper
- **citation:** Nowak, M. A. (2006). Five Rules for the Evolution of Cooperation. *Science*, 314(5805), 1560–1563. DOI: 10.1126/science.1133755
- **tier:** core
- **level:** UG
- **why:** A compact unifying map of five mechanisms that sustain cooperation: kin selection, direct reciprocity, indirect reciprocity (reputation), network reciprocity, and group selection. Each comes with a simple benefit-to-cost threshold. Network reciprocity links directly to network science.
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC3279745/ (author manuscript)
- **verified:** https://api.crossref.org/works/10.1126/science.1133755 ; Europe PMC record PMC3279745

### Strand: Mechanism design (entry point)

#### myerson-2008-mechanism
- **type:** paper
- **citation:** Myerson, R. B. (2008). Perspectives on Mechanism Design in Economic Theory. *American Economic Review*, 98(3), 586–603. DOI: 10.1257/aer.98.3.586 (Nobel Prize Lecture, 8 December 2007)
- **tier:** deep
- **level:** grad
- **why:** One of the 2007 laureates explains "reverse game theory": designing the rules so that self-interested agents with private information produce a desired outcome. The lecture covers incentive compatibility and the revelation principle. It is the most readable entry from the Hurwicz/Maskin/Myerson prize. Companion: Maskin (2008), *AER* 98(3), 567–576, and the Prize Committee's scientific background "Mechanism Design Theory" (2007).
- **focus:** whole
- **access:** free: https://www.nobelprize.org/uploads/2018/06/myerson_lecture.pdf (companion background: https://www.nobelprize.org/uploads/2018/06/advanced-economicsciences2007.pdf)
- **verified:** https://www.nobelprize.org/prizes/economic-sciences/2007/myerson/lecture/ ; https://api.crossref.org/works/10.1257/aer.98.3.586

## Concept spine
- **preference relation** — a complete, transitive ranking of options; the primitive of rational choice (UG)
- **utility function** — a number assigned to options that represents a preference ranking (UG)
- **expected utility** — valuing a gamble as the probability-weighted average of the utilities of its outcomes (UG)
- **independence axiom** — mixing two gambles with a common third gamble should not reverse which one you prefer; the axiom Allais attacks (grad)
- **subjective expected utility** — Savage's result that consistent preferences over acts imply both a personal probability and a utility (grad)
- **sure-thing principle** — if you prefer A to B whether or not event E happens, you should prefer A to B without knowing E (grad)
- **risk vs. ambiguity** — known probabilities vs. unknown probabilities; Ellsberg shows people treat them differently (UG)
- **risk aversion** — preferring a sure amount to a gamble with the same expected value; concave utility (UG)
- **bounded rationality** — decision-making limited by information, time and computation (UG)
- **satisficing** — stopping search at the first option that meets an aspiration level (UG)
- **heuristic** — a mental shortcut that trades accuracy for speed and effort (HS)
- **representativeness / availability / anchoring** — judging by similarity, by ease of recall, and by adjusting from a starting number (HS)
- **reference dependence** — outcomes are coded as gains or losses relative to a reference point, not as final wealth (UG)
- **loss aversion** — losses hurt more than equal-sized gains please (UG)
- **probability weighting** — overweighting small probabilities and underweighting moderate and large ones (grad)
- **framing effect** — logically equivalent descriptions produce different choices (HS)
- **ecological rationality** — a heuristic is rational to the degree it fits the structure of its environment (UG)
- **bias–variance trade-off** — simpler models err systematically but vary less across samples, and can predict better (grad)
- **strategic (normal-form) game** — players, actions, and payoffs that depend on everyone's actions (UG)
- **dominant / dominated strategy** — a strategy that is best (or never best) whatever others do (UG)
- **iterated elimination of dominated strategies** — repeatedly deleting dominated strategies, assuming common knowledge of rationality (UG)
- **best response** — the action that maximizes your payoff given others' actions (UG)
- **Nash equilibrium** — a profile in which everyone is best-responding to everyone else (UG)
- **mixed strategy** — randomizing over actions; guarantees equilibrium existence (UG)
- **zero-sum game & minimax** — one player's gain is the other's loss; each guarantees the best worst case (UG)
- **extensive-form game** — a game tree showing order of moves and information (UG)
- **backward induction** — solving a sequential game from the end backwards (UG)
- **subgame-perfect equilibrium** — Selten's refinement requiring optimal play in every subgame, ruling out non-credible threats (UG)
- **credible commitment** — limiting your own options to change others' expectations (Schelling) (UG)
- **information set** — the set of nodes a player cannot tell apart when moving (UG)
- **Bayesian game / types** — Harsanyi's model of incomplete information as private "types" drawn from a common prior (grad)
- **Bayesian Nash equilibrium** — each type best-responds given beliefs about others' types (grad)
- **signaling** — informed players take costly actions that reveal private information (UG)
- **repeated game & folk theorem** — with enough patience, many cooperative outcomes are sustainable as equilibria (grad)
- **shadow of the future** — the weight placed on future interaction, which makes cooperation pay (HS)
- **focal point** — a salient solution people coordinate on without communicating (HS)
- **convention** — a self-sustaining regularity that solves a recurring coordination problem (UG)
- **mutual vs. common knowledge** — everyone knows X, versus everyone knows that everyone knows ... ad infinitum (UG)
- **common prior** — the assumption that differences in beliefs come only from differences in information (grad)
- **agreement theorem** — with a common prior, commonly known posteriors must be equal (grad)
- **level-k / cognitive hierarchy** — players reason only a limited number of steps about others' reasoning (UG)
- **quantal response equilibrium** — equilibrium with noisy, probabilistic best responses (often logit/softmax) (grad)
- **social preferences** — caring about others' payoffs (fairness, reciprocity), as shown in ultimatum and dictator data (UG)
- **evolutionarily stable strategy** — a strategy that cannot be invaded by a rare mutant (UG)
- **replicator dynamics** — strategies grow in proportion to how much better than average they do (grad)
- **reciprocity (direct, indirect, network)** — cooperation sustained by repeated play, reputation, or local network structure (UG)
- **mechanism design** — choosing game rules so that self-interested play yields a target outcome (grad)
- **incentive compatibility & revelation principle** — truth-telling is optimal; any implementable outcome can be achieved by a truthful direct mechanism (grad)

## Canonical instances
- **Prisoner's Dilemma** — individually dominant defection yields a collectively worse outcome — osborne-2004-introduction (§2.2)
- **Iterated PD tournament / TIT FOR TAT** — simple reciprocal strategy wins Axelrod's computer tournaments — axelrod-1984-cooperation
- **Stag Hunt** — two equilibria, safe vs. efficient; coordination under strategic risk — osborne-2004-introduction (§2.5)
- **Battle of the Sexes ("Bach or Stravinsky")** — coordination with conflicting preferences over which equilibrium — osborne-2004-introduction (§2.3)
- **Matching Pennies** — pure conflict with no pure equilibrium; only mixed equilibrium — osborne-2004-introduction (§2.4)
- **Hawk–Dove** — contests with escalation costs; mixed/ESS outcome — maynardsmith-1973-animal-conflict; osborne-2004-introduction (§2.7.5)
- **Focal-point coordination (meeting without communicating)** — people coordinate on salient choices — schelling-1960-conflict
- **p-beauty contest (guess 2/3 of the average)** — iterated reasoning stops after 1–2 steps — nagel-1995-guessing
- **Ultimatum game** — responders reject "unfair" positive offers, contradicting subgame-perfect prediction — camerer-2003-bgt; polak-2007-econ159 (L17)
- **Allais paradox** — common-consequence choices violate the independence axiom — allais-1953-paradox
- **Ellsberg urns** — preference for known over unknown odds (ambiguity aversion) — ellsberg-1961-ambiguity
- **Asian disease problem** — "saved" vs. "die" framing reverses risk preference — tversky-1981-framing
- **Linda problem (conjunction fallacy)** — a conjunction is judged more probable than one of its parts — kahneman-2011-thinking ("Linda: Less is More")
- **Hats puzzle (muddy-children family)** — a public announcement of something everyone already knows changes what can be inferred — geanakoplos-1992-common-knowledge
- **Coordinated attack / electronic mail game** — no finite chain of confirmations creates common knowledge — rubinstein-1989-email

## Bridges
- [same-math] logit quantal response ↔ LLMs: softmax sampling with temperature — the logit QRE choice rule P(a) ∝ exp(λ·u(a)) is the same Boltzmann/softmax function as LLM token sampling, with 1/λ playing the role of temperature.
- [same-math] subjective expected utility ↔ Bayesian theory & causal inference: Bayesian decision theory — Savage's representation is exactly posterior-expected-loss minimization with a personal prior.
- [same-math] zero-sum minimax ↔ linear algebra: linear-programming duality — solving a finite zero-sum game is a linear program, and the minimax theorem corresponds to LP duality.
- [same-math] ecological rationality ↔ LLMs: bias–variance trade-off — Gigerenzer & Brighton use the same error decomposition that underlies model selection in machine learning.
- [structural-analogy] level-k / cognitive hierarchy ↔ theory of mind: orders of mentalizing ("I think you think...") — recursive belief modeling with bounded depth; the game-theoretic version adds payoffs and best responses.
- [structural-analogy] common knowledge & focal points ↔ communication theory: public vs. private messages — public broadcasts can create common knowledge, while private ones only create mutual knowledge, which changes what coordination is possible (see also analytic-philosophy: lewis-1969-convention).
- [structural-analogy] framing effect (equivalence framing) ↔ communication theory: media framing — related but not identical; Tversky–Kahneman frames are logically equivalent descriptions, while media frames usually select and emphasize different facts.
- [structural-analogy] reciprocity & network reciprocity ↔ complex systems: cooperation on networks — evolutionary games on graphs turn structural position into strategic advantage (cf. political-science: ostrom-1990-commons for institutional solutions to commons dilemmas).
- [structural-analogy] mechanism design ↔ political science: social choice and voting rules — both study aggregating private preferences under incentive constraints (see political-science: arrow-1951-socialchoice).
- [metaphor] Keynesian beauty contest ↔ economics & finance: investors guessing others' guesses — Nagel's experiment formalizes the metaphor; real markets are much richer than the p-beauty game.
