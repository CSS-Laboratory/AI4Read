---
id: pearl-2018-bookofwhy/ch02-buccaneers
work: pearl-2018-bookofwhy
unit: "Chapter 2 — From Buccaneers to Guinea Pigs: The Genesis of Causal Inference"
pages: "pdf 58–91 (printed page numbers not visible)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# From Buccaneers to Guinea Pigs: The Genesis of Causal Inference

## L0 — One line
Galton went looking for a causal law of heredity and found correlation, which has no causal direction. Pearson then worked to remove causation from statistics, and Sewall Wright's path diagrams were the first direct challenge to that culture.

## L1 — The gist (≤ 120 words)
How did statistics come to ignore causation, and how did one geneticist start to bring it back? Galton sought a causal law of heredity but found regression to the mean and correlation, which carry no causal direction. Pearson treated causation as a special case of correlation, and his school avoided causal language. From 1920, Wright's path diagrams combined qualitative causal assumptions with data to estimate causal quantities. Statisticians neglected them for decades. Pearl argues that causal conclusions need causal hypotheses, and that these are partly subjective. This matters because data alone stay on the first rung of the Ladder of Causation.

**Prerequisites:** mean and normal ("bell-shaped") distribution; scatter plots and best-fit lines; the three rungs of the Ladder of Causation (Chapter 1); the idea of a coefficient in an equation.

## L2 — Key ideas
- Regression to the mean is a statistical fact, not a physical force. It also works backward in time, so it cannot be a causal process (pdf 61–62).
- Correlation measures cross-predictability. It is the same whether X causes Y, Y causes X, or both have a common cause (pdf 65).
- Pearson reduced causation to a limiting case of correlation, and Pearl reads his view as: data is all there is to science. Pearl notes that even Pearson and Yule wrote about "spurious" correlation, a concept he says needs causal ideas (pdf 70, 72).
- Wright's path diagrams link causal quantities (rung two) to correlations (rung one) by a path-tracing rule. This showed that "some correlations do imply causation" (pdf 76–77).
- Wright's birth-weight example separates a direct causal effect (3.34 g/day) from a confounded association (5.66 g/day) (pdf 82–84).
- You cannot draw causal conclusions without some causal hypotheses. This is not circular, because mild qualitative assumptions plus data yield non-obvious quantitative answers (pdf 80).
- Path analysis was hardly used from 1920 to 1960 and was later partly distorted. Possible reasons given: it does not suit canned software (Crow), and Fisher's hostility to Wright may have mattered (Provine). Economists later avoided diagrams (pdf 84–86).
- Causal assumptions are subjective and may not wash out as data grow. Once assumptions are agreed, inference from new data is fully objective (pdf 89–90).

## L3 — Walkthrough

### Galton's quincunx (pdf 58–62)
- **Setting.** Galton lectured at the Royal Institution on 9 Feb 1877 with a "quincunx" (Galton board): a triangular array of pegs through which balls fall into slots (pdf 58–59).
- **Pattern.** Each ball's path looks random, but many balls pile up into a rough bell-shaped curve (pdf 59).
- **Explanation.** A ball's path is like independent coin flips. Its slot is set by the excess of rights over lefts. By the central limit theorem (Laplace, 1810) a sum of many coin flips gives the normal distribution (pdf 59).
- **Heights.** French military recruits' heights follow the same bell shape (pdf 59).
- **Galton's causal reading.** The balls "inherit" their position as humans inherit stature (pdf 59–60).
- **The puzzle.** The curve's width depends on the number of rows. Doubling the rows models two generations and gives more variation. Actual human heights keep a roughly constant width (pdf 60).
- **Eminence.** In *Hereditary Genius* (1869) Galton compiled 605 "eminent" Englishmen. Their sons and fathers were somewhat less eminent, and more distant relatives less eminent still (pdf 60). Pearl asks, as questions, what "eminence" means and whether eminent families succeed because of privilege rather than talent (pdf 60).
- **Regression.** Sons of tall men tend to be taller than average but less tall than their fathers. Galton first called this "reversion", later "regression toward mediocrity". Students' scores on two tests and baseball's "sophomore slump" show the same pattern (pdf 60–61).
- **Galton's mechanism.** He added sloping chutes between two peg arrays (Figure 2.1). They pulled balls back toward the centre and kept the width constant. He treated regression as a physical process, like Hooke's law (pdf 61).
- **Pearl's verdict.** Galton was mistaken. Pearl says the sophomore slump needs no causal explanation and will happen more often than not by chance alone, though he allows that experts' causal stories may be right (pdf 62). He quotes Kahneman: success = talent + luck, and great success = a little more talent + a lot of luck (pdf 62).

> **Intuition note.** An extreme result usually combines some real advantage with some luck. Luck does not repeat, so the next result tends to be less extreme. No hidden force is needed.

### Galton's step from regression to correlation (pdf 62–66)
- **Other pairs of traits.** By 1889 Galton saw the same regression for height against forearm length. Neither causes the other. If anything, both come from inheritance. He called such traits "co-related", later "correlated" (pdf 62).
- **Reversal in time.** Fathers of tall sons also regress: they are taller than average but shorter than their sons. So Galton had to give up a causal explanation, because sons' heights cannot cause fathers' heights (pdf 62).
- **Resolution: two populations.** Six-foot fathers (all exactly six feet) have sons averaging, say, 5′11″. The pairs with 5′11″ sons form a different group, whose fathers vary and average below 5′11″ (pdf 63–64).
- **Scatter plot (Figure 2.2).** Each father–son pair is a dot, and the cloud is roughly elliptical.
  - The vertical slice for 72″ fathers is centred near 71″.
  - The horizontal slice for 71″ sons is centred near 70.3 by eye (pdf 64). The legend says ≈ 70 (pdf 63).
  - The centres of all vertical slices fall on a line, the regression line. It is less steep than the ellipse's major axis (pdf 64).
  - There are two such lines, one for each direction of prediction. The situation is symmetric, so, Pearl says, where regression to the mean is concerned, cause and effect make no difference (pdf 64).
- **Slope.** A slope of 0.5 means each extra inch for the father goes with an extra half inch for the son, on average. A slope of 1 is perfect, deterministic correlation (pdf 64–65).
- **Slope bound.** Provided the height distribution stays the same across generations, the slope cannot exceed 1. Otherwise the distribution would widen and "9-foot people" would appear (pdf 65).
- **Different quantities.** The law also applies to height against IQ. After the axes are properly rescaled, the best-fit slope equals 1 only when one quantity predicts the other precisely. It is 0 when prediction is no better than a random guess. It is the same whichever variable is plotted on which axis (pdf 65).
- **Objectivity.** Correlation was the first objective measure of how two variables relate, whether the relation is causal, neutral or reverse-causal (pdf 65–66). Pearson later derived a formula for the rescaled slope and called it the correlation coefficient (pdf 66).

> **Intuition note.** Predicting a son from a father and a father from a son are two separate prediction problems. Each regresses toward the mean. The slope tells you how well one number predicts the other, not which one causes the other.

### Galton and the abandoned quest (pdf 66–69)
- Galton's 1889 text still hinted at causes: he wrote that correlation between two organs must follow from their variations being partly due to common causes (pdf 66).
- After eight years he dropped the chutes and the search for a biological restoring force. Stigler calls it "supreme irony" that the essence of Darwin was discarded as unnecessary (pdf 66).
- **Pearl's diagnosis (Figure 2.4).** Galton's machine was wrongly built. In it, each ball's displacement inherits the sum of all variations from the pegs above, so luck accumulates. This contradicts Kahneman's equations, where luck is transitory and not inherited (pdf 66–67).
  - Model (a), Galton's: success passes from generation to generation and luck accumulates. This may be natural for wealth or eminence.
  - Model (b), genetic: only talent is passed down, and each generation's luck is independent (pdf 67–68).
- Both models fit a bell-shaped distribution. Of the two, only (b) is compatible with a stable distribution of heights. In (b), the stability of the genetic endowment explains the stability of heights. This stability was explained mathematically by Hardy and Weinberg (1908) with the Mendelian causal model (pdf 68).
- Galton could not have known this: Mendel's 1866 work was forgotten until 1900. Pearl says the causal diagram makes it easy to locate his mistaken assumption: transmitting luck across generations (pdf 68–69).
- **Whig history.** Pearl accepts the label "Whig historian", meaning he reads history through modern science. He argues that there is no other way to understand how statistics became a data-reduction enterprise blind to models (pdf 69).

### Pearson: the wrath of the zealot (pdf 69–74)
- **Pearson's creed.** Pearson wrote in 1934 that Galton freed him from the prejudice that sound mathematics applies to nature only within the category of causation. He saw causation as the limiting case of correlation (|r| = 1, deterministic) (pdf 69–70).
- **Grammar of Science (1892).** Causation records a sequence that has recurred. Science cannot show an inherent necessity or prove with certainty that it must repeat (pdf 70). Any relation can be "thrown back upon" a contingency table. Pearl reads this as: only the first rung of the Ladder is needed (pdf 70).
- **Roots.** Pearson's skepticism predated Galton's book. Pearl links it to positivism, a school Pearson belonged to, which holds that the universe is a product of human thought and that science only describes those thoughts. On this view, objective causation could have no scientific meaning; meaningful thoughts reflect patterns of observation, which correlations describe completely (pdf 70).
- **Institutions.** Pearson's first statistics paper came in 1893, *Biometrika* in 1901, a lab in 1903 and a department in 1911. Porter says he drove dissenters from the "church biometric". Yule's obituary says that after expressed criticism, friendly relations became "impossible" (pdf 70–71).
- **"Spurious correlation."** Pearson and Yule wrote about "spurious correlation", a concept Pearl says cannot be understood without causation. Pearson separated genuine "organic" relationships from spurious ones. Pearl asks whether "organic" is causality by another name (pdf 72).
  - *Confounding.* The chocolate–Nobel correlation (a later example) probably comes from common causes, wealth and location (pdf 72).
  - *Time trends.* Yule found a correlation of 0.95 between England's mortality rate and the share of Church of England marriages. Both were falling over the period (pdf 72).
  - *Mixed populations.* Pearson had 806 male and 340 female skulls from the Paris Catacombs. Within each sex, length and breadth were negligibly correlated. Combined, the correlation was 0.197. Pearson called it a statistical artifact (pdf 72–73).
- **Pearl's comment.** The skull case is an instance of Simpson's paradox (Chapter 6). It was a missed opportunity to ask when to aggregate. Pearl says Pearson's only guidance to followers was that an "artificial" mixture is bad. Pearl says that in some cases the aggregated data, not the partitioned data, are correct (pdf 73).
- **Yule's out-relief study (1899).** Districts with more out-relief had more poverty. Yule suspected more elderly people explained this. The correlation remained among districts with equal proportions of elderly. He then wrote "due to", but added a footnote: "for 'due to' read 'associated with'". Pearl says scientists thereafter would think "due to" and say "associated with" (pdf 74).

### Sewall Wright, guinea pigs and path diagrams (pdf 74–81)
- **Background.** Wright studied genetics at Harvard from 1912. After his 1915 doctorate he took charge of guinea pigs at the USDA. Later he held a faculty post at Chicago (pdf 74–75).
- **The problem.** Guinea pig coat color defied Mendelian prediction. Even after many generations of brother–sister mating, the amount of white varied widely. Wright postulated "developmental factors" in the womb. Pearl says hindsight shows he was right (pdf 75).
- **The method.** Wright named the unknown (d, the effect of developmental factors on white fur; h, hereditary factors), wrote equations, and solved them (pdf 76). His key step: if the causal quantities in Figure 2.7 were known, a simple graphical rule predicts the correlations in the data (pdf 76).
- **The bridge.** This was the first bridge between causality and probability, between rungs two and one. Wright crossed it backward, from measured correlations (rung one) to d and h (rung two). It was the first proof that the mantra that correlation does not imply causation should give way to "Some correlations do imply causation" (pdf 77).
- **Results.**
  - In a randomly bred population, 42% of variation in coat pattern was due to heredity and 58% developmental.
  - In a highly inbred family, 3% was hereditary and 92% developmental (pdf 77).
  - Twenty generations of inbreeding had nearly eliminated genetic variation, but not developmental variation (pdf 77).
- **Reading Figure 2.7 (pdf 77–79).**
  - Each animal has D (developmental), E (environmental) and H (hereditary) factors.
  - Every arrow runs from cause to effect, except a two-headed arrow between the parents' heredity H″ and H‴. It marks the correlated heredity of an inbred family.
  - A missing arrow, for example from G to H′, says one offspring's sperm cell has no causal effect on the sibling's heredity.
  - Each arrow has a path coefficient (a, b, c…), which Wright interpreted as the share of variability in the target accounted for by the source. For heredity from each parent, a = 1/√2 and a² = 1/2.
  - The modern interpretation is the result of a hypothetical intervention on the source. The two agree in the simple models Wright analysed.
- **The computing rule.** To get the correlation between two variables, trace the paths connecting them and multiply the coefficients along each path (pdf 78–79).
- **Omitted arrows.** An omitted arrow forces the causal effect to zero, so it carries a stronger assumption than a present arrow. A present arrow leaves the size of the effect open (pdf 79).
- **Landmark.** This is the first published causal diagram. A more general paper, "Correlation and Causation", followed in 1921 (pdf 79).
- **Niles's rebuttal (1921).** Niles was a student of Raymond Pearl, himself a student of Pearson.
  - He cited Pearson and Galton on the redundancy of "cause".
  - He wrote that causation is "simply perfect correlation".
  - He called it a fallacy to set up a priori a simple graphic system of action among variables.
  - He called the method "wholly unreliable". Pearl says Niles bungled the computations (pdf 79).
- **Why it matters.** The paper shows the attitude of Pearson's generation, and Niles's objections are still heard today (pdf 80).
- **Wright's defence, with Pearl's commentary.**
  - *Exploratory use.* When the full web of relations is unknown, postulate some causal relations, compute the predicted correlations, and compare them with the data. A contradiction is evidence that the assumptions are false. Simon rediscovered this in 1953 (pdf 80).
  - *No causal conclusions without causal hypotheses.* Pearl says Wright makes this point with absolute clarity, and that it echoes Chapter 1: rung two cannot be answered from rung-one data alone (pdf 80).
  - *Not circular (Pearl's reply to people who ask this).* Mild, obvious qualitative assumptions plus twenty years of data gave a non-obvious quantitative result (42% heritability). Pearl adds that the diagram information and the data information are in two different mathematical languages (pdf 80).
  - *Causal discovery versus causal queries.* Wright's focus, and the book's, is to represent plausible causal knowledge, combine it with data, and answer causal queries. That differs from causal discovery. Wright wrote that combining knowledge of correlations with knowledge of causal relations differs from deducing causal relations from correlations (pdf 80–81).

> **Intuition note.** Wright treated the diagram as a set of assumptions about who affects whom. The data then fix the sizes of the effects. Predicted correlations that contradict the data count as evidence that the assumed relationships are false (pdf 80).

### E pur si muove: courage and the birth-weight example (pdf 81–84)
- **Pearl on Wright's courage.** Pearl contrasts Wright with Galileo, who at least had observations, whereas Wright had "untested conclusions" and no theorem. Pearl says one solace to Wright must have been his understanding that he could answer questions that no other method can answer (pdf 82).
- **The question.** How much does a guinea pig's birth weight change if it spends one more day in the womb? (pdf 82).
- **Naive reading.** Pups born one day later weigh on average 5.66 g more, so growth might be 5.66 g/day. Wright says this is wrong. Later pups usually have fewer litter-mates, hence a better growth environment throughout (pdf 82–83).
- **Diagram (Figure 2.8).**
  - X = birth weight.
  - P = gestation period.
  - Q = prenatal growth rate (not measured).
  - L = litter size, which affects both P and Q.
  - A and C = other causes of growth rate and gestation time, not measured and assumed independent of each other, so no arrow or common ancestor links them (pdf 83).
  - Path coefficients: l on L→Q, l′ on L→P, q on Q→X, p on P→X (pdf 83). X, P and L can be measured for each pup (pdf 83).
- **Computation.** The direct effect is p. The bias runs along $P \leftarrow L \rightarrow Q \rightarrow X$ and equals $l \times l' \times q$ (pdf 83–84). The measured association is the sum over both paths:
$$p + (l \times l' \times q) = 5.66 \text{ g/day}$$
- The coefficients l, l′ and q are unknown because Q is unmeasured. But each measured correlation, for the pairs (P, X), (L, X) and (L, P), can be written in terms of path coefficients. This gives three equations, solvable for $p$, $l'$ and $l \times q$ (pdf 84).
- **Result.** $p = 3.34$ g/day. This is the average gain if A, L, C, Q were held constant and only gestation grew by a day (pdf 84). The leftover bias term is $5.66 - 3.34 = 2.32$ g/day (added step).
- **Lessons (Pearl).** (1) Causal analysis quantifies processes in the real world, not just patterns in data. The 5.66 conflates two processes, one of them "anticausal (or diagnostic)" in P ← L. (2) Conclusions about individual causal links come from examining the diagram as a whole; the entire structure may be needed to estimate each parameter (pdf 84).

> **Intuition note.** The raw difference mixes two stories: a pup that stays longer, and a pup that had more room. Wright used the diagram to subtract the second story, even though one of its links (growth rate) was never measured.

### Why path analysis was neglected (pdf 84–88)
- **Neglect.**
  - Crow calls the absence of use from 1920 to 1960, except by Wright and animal breeders, a "mystery" (pdf 84).
  - Goldberger (1972) lamented a "scandalous neglect" (pdf 85).
  - Crow's explanation: the method does not suit "canned" programs, because the user needs a hypothesis and a diagram. Pearl adds that statistics, as often practiced, encourages canned procedures (pdf 85).
- **Fisher's definition.** Fisher (1925) called statistics the "reduction of data". Pearl comments that once causation is removed, data reduction is all that remains (pdf 85).
- **Fisher–Wright feud.** Provine says that from the mid-1930s Fisher saw Wright as an enemy. The feud centred on evolutionary biology (genetic drift), not path analysis, but Fisher was the oracle of statistics until the 1950s (pdf 85–86).
- **Revival and distortion.**
  - In the 1960s, Duncan, Blalock and Goldberger rediscovered path analysis. Wright had failed to explain it to the Cowles Commission in 1947 (pdf 86).
  - Sociologists renamed it structural equation modeling (SEM). Once LISREL (1970) automated the coefficients, it became rote. In the late 1980s Freedman's public challenge to state SEM's assumptions went unanswered, and some experts disavowed any link to causality (pdf 86).
  - Economists kept the algebra as simultaneous equation models and avoided diagrams. Because algebraic equations are non-directional (x = y is the same as y = x), they lacked notation to separate causal from regression equations. As late as 1995 most refrained from giving their equations causal meaning (pdf 86).
- **1983 debate.** Karlin and coauthors criticised path analysis in the *American Journal of Human Genetics*, and Wright, past ninety, replied (pdf 86–87).
  - *Linearity.* Karlin objected that all relationships are assumed linear, so one number can describe each effect. Pearl notes that a general nonlinear theory came three years later from his student Thomas Verma (pdf 87).
  - *Model-free alternative.* Karlin favored a "model-free approach" with displays, indices and contrasts. Pearl reads this as Pearson's ideology: the data hold all the wisdom (pdf 87).
- **Wright's reply (pdf 88).** Wright said Karlin et al. were urging an abandonment of the purpose of path analysis, and added that there can be no such analysis without a model. Pearl agrees that a model-free approach may reach the first rung but no farther (pdf 88).

### From objectivity to subjectivity: the Bayesian connection (pdf 88–91)
- **Why statisticians resist.** Wright wanted path analysis to stay "unstereotyped": based on the user's own field knowledge, not routines. Wright, as Pearl reads him, traces the allure of "model-free" methods to their objectivity. The Statistical Society of London (founded 1834) gave data priority over opinion. Causal analysis requires a subjective commitment, a diagram of the researcher's (or the field's consensus) belief (pdf 88–89).
- **Bayesian statistics.** Prototype: Prior Belief + New Evidence → Revised Belief. Take a coin that shows nine heads in ten tosses (pdf 89).
  - The orthodox statistician would bet nine to one on heads next.
  - The Bayesian also asks where the coin came from. A grocery-store quarter would not shift belief as much as a coin already suspected of being weighted (pdf 89).
  - Frequentists disliked subjective probabilities. Bayesian analysis won over mainstream statisticians for applications such as weather prediction and tracking submarines. In many cases the influence of the prior vanishes as data grow (pdf 89–90).
- **Why this did not help causality.** Bayesians state their subjective assumptions in the language of probability. Causal assumptions need a richer language, such as diagrams, that is foreign to both camps. Pearl calls this a "linguistic barrier", harder to cross than a philosophical one (pdf 90).
- **Subjectivity that persists.** The subjective part of causal information does not necessarily shrink with more data. Two people with different causal diagrams may never agree on the same data, however big (pdf 90).
- **Objectivity regained.** Once two people agree on their assumptions, causal inference is "100 percent objective" for interpreting new evidence, like Bayesian inference. Pearl says his own route to causality went through Bayesian networks, the topic of Chapter 3 (pdf 90).

## Toy example (ours, not from the text)
Six father–son pairs, heights as inches above the population mean (father, son): (2,2), (2,0), (0,2), (0,−2), (−2,0), (−2,−2).
- Means: fathers $(2+2+0+0-2-2)/6 = 0$. Sons $(2+0+2-2+0-2)/6 = 0$.
- Fathers at +2 have sons +2 and 0, so the average is $(2+0)/2 = +1$, less than 2. This is regression.
- Sons at +2 have fathers 2 and 0, so the average is $(2+0)/2 = +1$, again less than 2. Regression appears backward in time, so it is not a causal push.
- Fathers at −2 have sons 0 and −2, average −1. Sons at −2 have fathers 0 and −2, average −1.
- Slope of son on father = covariance ÷ variance. Covariance $= (4+0+0+0+0+4)/6 = 8/6$. Father variance $= (4+4+0+0+4+4)/6 = 16/6$. Slope $= (8/6)/(16/6) = 0.5$. Son variance is also 16/6, so the slope of father on son is also 0.5.
- The same slope in both directions shows that correlation does not say which variable is the cause.

## Concepts
- [[regression-to-the-mean]] (new) — extreme values tend to be followed by less extreme ones; statistical, not causal; symmetric in time (pdf 61–62).
- [[correlation-coefficient]] (new) — Pearson's formula for the rescaled regression slope; 1 means exact prediction, 0 means no better than guessing; blind to causal direction (pdf 65–66).
- [[spurious-correlation]] (new) — association without "organic" meaning: confounding, shared time trends, or mixed populations (pdf 72–73).
- [[simpsons-paradox]] — Pearl calls the skull-data aggregation effect a case of it; Chapter 6 treats it (pdf 73).
- [[confounding-vs-selection-bias]] — here confounders are common causes of two variables (pdf 72).
- [[causal-dag]] — Wright's path diagram: one-way arrows from cause to effect, two-headed arrows for correlated causes (pdf 77–78).
- [[path-coefficient]] (new) — number on an arrow giving the strength of a causal effect; originally "variability accounted for", now an intervention effect (pdf 78).
- [[path-analysis]] (new) — computing correlations by multiplying and adding path coefficients along diagram paths, and inverting these equations to estimate effects (pdf 78–79, 83–84).
- [[ladder-of-causation]] — Pearson's world has only rung one; Wright's bridge connects rungs one and two (pdf 70, 77).
- [[positivism]] (new) — view that science only describes thoughts and patterns of observation, so objective causation lacks scientific meaning (pdf 70).
- [[frequentist-vs-bayesian]] — Bayesians admit subjective probabilities. Frequentists resisted, and Bayesian analysis was later accepted (pdf 89–90).
- [[prior-distribution]] — "prior belief" about the coin, which combines with evidence. Its influence may vanish as data grow (pdf 89–90).

## Canonical instances
- [[galton-board]] — bell curve from many random bounces; Galton's causal model of heredity and its flaw (pdf 59–68).
- [[father-son-heights]] — regression in both directions; two populations; regression lines (pdf 62–65).
- [[sophomore-slump]] — regression to the mean read as a causal story (pdf 61–62).
- [[paris-skulls]] — correlation of 0.197 appears only after combining sexes (pdf 72–73).
- [[yule-out-relief]] — "due to" retreats to "associated with" (pdf 74).
- [[guinea-pig-coat-color]] — Wright's first path diagram; 42%/58% and 3%/92% (pdf 77).
- [[guinea-pig-birth-weight]] — 5.66 g/day association versus 3.34 g/day direct effect (pdf 82–84).
- [[nine-heads-coin]] — Bayesian versus orthodox reading of nine heads in ten tosses (pdf 89).

## Bridges (candidates)
- [same-math] Galton board as a sum of coin flips ↔ central limit theorem: the text itself says the board is a demonstration of Laplace's theorem (pdf 59).
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average.
- [structural-analogy] Wright's bias path P ← L → Q → X ↔ back-door path and confounding: a common cause makes an association differ from the direct effect.
- [structural-analogy] Pearson's mixed skull populations ↔ Simpson's paradox: aggregation creates or reverses an association.
- [structural-analogy] Prior influence vanishing with more data ↔ Bayesian updating: the text says this holds "in many cases", while causal assumptions need not wash out (pdf 90).
- [metaphor] Wright's "bridge" between rung two and rung one ↔ identifiability: translating causal assumptions into testable statements about data.

## Questions this raises
- When is the aggregated data, not the partitioned data, the correct one (pdf 73)?
- How does Wright's path-tracing rule connect to the intervention-based meaning of coefficients (pdf 78)?
- If two researchers hold different causal diagrams, how can data ever decide between them (pdf 90)?
- How can causal assumptions be written in a language richer than probability (pdf 90)?

## Reading notes
- The page labels give no printed page numbers, so all references are pdf numbers. Printed numbers are not visible in the page images either.
- The text layer drops arrows and symbols. Examples: "path P X" for P → X, the ← and → in the bias path on pdf 84, and the arrow in "Prior Belief + New Evidence → Revised Belief". I restored them from the surrounding sentences and the Figure 2.8 image.
- On pdf 78 the text layer reads "a = 1/ and a2 = 1/2". I wrote $1/\sqrt{2}$ because the text says Wright "preferred to take the square root". The image for that page was not provided.
- The text says the centre of the 71″-sons slice is about 70.3 (pdf 64). The Figure 2.2 legend says ≈ 70 (pdf 63).
- The inbred-family figures (3% heredity, 92% developmental) do not add to 100%. The text does not say what accounts for the rest (pdf 77).
- The Figure 2.8 legend in the image has typos ("groth", "periond"). The text refers once to the "Royal Institute" (pdf 59) and elsewhere to the "Royal Institution".
- The text layer of the last page (pdf 91) holds only a caption describing a drawing (Sherlock Holmes and a robot with a Bayesian network; Bayes's rule on its screen); no image of that page was provided.
- The unit has no exercises.
