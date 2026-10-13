---
id: godfreysmith-2003-theory/ch14-bayesianism
work: godfreysmith-2003-theory
unit: "14 Bayesianism and Modern Theories of Evidence"
pages: 202-218
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Bayesianism and Modern Theories of Evidence

## L0 — One line
Bayesianism treats evidence as something that raises a subjective probability via Bayes's theorem, but Godfrey-Smith holds that a full theory of evidence also needs eliminative inference and a focus on the reliability of testing procedures.

## L1 — The gist (≤ 120 words)
Logical empiricism failed to produce a theory of confirmation, so the question "what makes an observation evidence?" stayed open. Bayesianism is the current popular answer. Probabilities are degrees of belief. Evidence e confirms h if P(h|e) > P(h), and beliefs are updated by Bayes's theorem. Godfrey-Smith, who is not a Bayesian, explains the theory, the Dutch book defence (bets that guarantee a loss), and worries about priors (probabilities set before evidence). He argues that testing usually chooses between rival hypotheses about hidden structure. Eliminative inference (ruling out rivals) is probably part of the answer. His "procedural naturalism" says an observation is evidence only inside the right kind of procedure. He applies this to the ravens and grue puzzles.

**Prerequisites:** basic probability (conditional probability, P(not-h) = 1 − P(h)); the ravens and grue puzzles from chapter 3; simple betting odds.

## L2 — Key ideas (5–10 bullets)
- Bayesianism says e confirms h if P(h|e) > P(h). Belief should be updated by Bayes's theorem, Pnew(h) = Pold(h|e) (pp. 204, 208).
- Bayes's theorem is mathematically trivial, following from axiom 4. The philosophical weight lies in prior probabilities (probabilities of theories before the evidence). Many interpretations of probability cannot make sense of these, so Bayesians adopt a subjectivist reading (pp. 205, 207).
- Subjectivism reads probabilities as degrees of belief, revealed through fair betting odds. The Dutch book argument says that if beliefs break the probability axioms, there are possible sets of bets that guarantee a loss (pp. 205–208).
- Priors are a "free choice". Bayesians say convergence "washes out" priors. Godfrey-Smith replies that convergence can be slow and needs shared likelihoods (the probabilities P(e|h) of the evidence given each hypothesis) (pp. 209–210).
- The Bayesian answer to grue is a difference in priors. Bayesianism offers no criticism of someone who reverses them, provided that person's probabilities are coherent and updated properly (p. 210).
- Testing typically, not always, picks between hypotheses about hidden structure. So explanatory inference (inference from data to a structure or process that would explain them) matters more than traditional induction (pp. 211–212).
- Eliminative inference (support by ruling out alternatives) is common in science. Its chief difficulty is knowing that all relevant alternatives were considered (pp. 212–213).
- Procedural naturalism: an observation is evidence only within the right kind of procedure, one able to answer our questions reliably. The author offers a sketch of a solution to the ravens case, and part of an answer to the grue case, via sampling methods and confounding variables (variables that interfere with extrapolating from a sample) (pp. 214–217).

## L3 — Walkthrough

### 14.1 New Hope (p. 202–203)
- The problem of confirmation (what makes an observation evidence for a theory?) hung over twentieth-century philosophy of science. Logical empiricism tried to build an "inductive logic" from simple cases, such as black ravens confirming "all ravens are black", and failed (p. 202).
- Popper denied that confirmation is essential to science. Historical theories like Kuhn's did not focus on it. Yet the problem lurked, and the lack of a theory kept empiricists on the defensive (p. 202).
- Bayesianism now gives many philosophers hope. Earman's title *Bayes or Bust?* sums up the attitude (p. 202).
- Godfrey-Smith is not a Bayesian. He grants that some parts are "undeniably powerful" and warns that this is the hardest chapter (p. 203).

### 14.2 Understanding Evidence with Probability (pp. 203–205)
- The text now speaks of "evidence" rather than "confirmation" (p. 203). Using probability to understand evidence is old (Carnap; statistics; forensic evidence). The shared idea: evidence can sometimes raise or lower a hypothesis's probability (p. 203).
- Bayes's theorem, in two forms (p. 203):
$$P(h|e)=\frac{P(e|h)\,P(h)}{P(e)}\tag{1}$$
$$P(h|e)=\frac{P(e|h)\,P(h)}{P(e|h)\,P(h)+P(e|\text{not-}h)\,P(\text{not-}h)}\tag{2}$$
- $P(X|Y)$ is the probability of X given Y. $P(h)$ is the **prior probability**, which ignores e. $P(e|h)$ and $P(e|\text{not-}h)$ are **likelihoods**. They need not sum to any particular value. $P(h|e)$ is the **posterior probability**. $P(h)$ and $P(\text{not-}h)$ must sum to one (p. 204).
- Two central Bayesian ideas: e confirms h if $P(h|e) > P(h)$; probabilities should be updated as Bayes's theorem dictates (p. 204).
- Worked example (p. 204): h = "he is at the party", e = "his car is outside". $P(h)=0.5$, $P(e|h)=0.8$, $P(e|\text{not-}h)=0.1$.
$$P(h|e)=\frac{(0.5)(0.8)}{(0.5)(0.8)+(0.5)(0.1)}=\frac{0.40}{0.45}\approx 0.89$$
  The car raises the probability from 0.5 to almost 0.9: strong confirmation (p. 204).
- Likelihoods seem easier to interpret, since theories say what we are likely to see (some Bayesians underestimate problems here). Priors of theories are controversial. Many interpretations of probability cannot make sense of them, so Bayesians adopt the subjectivist one (p. 205).

*Intuition note:* Bayes's theorem compares how well h and not-h each predict the evidence, weighted by how likely each was beforehand. A surprising-under-not-h observation pushes h up.

### 14.3 The Subjectivist Interpretation of Probability (pp. 205–208)
- Most accounts treat probability as an objective feature of events. **Subjectivism** (Ramsey and de Finetti, 1920s–30s) treats probability as degree of belief. It is also central to decision theory (p. 205).
- Degrees of belief are read from gambling behaviour, actual and possible, not by asking people. Bayesianism seems to treat idealised rather than real people (p. 206).
- A person's **subjectively fair odds** for a bet are those at which she is equally willing to take either side. To bet on h at odds X:1 is to risk $X if h is false for a gain of $1 if h is true. If fair odds are X:1, degree of belief in h is $X/(X+1)$ (p. 206). Example in the text: at 3:1, a person who bets on h wins $1 if h is true and loses $3 if it is false (p. 206). (added step: this gives degree of belief $3/4$.)
- Belief in h&j, not-h, and so on are read the same way. A belief system is thus a network of subjective probabilities, which combine with utilities to produce behaviour (p. 206).
- Bayesians claim a coherent (rational) network must follow the rules of probability. Axioms, in the version used by subjectivists (p. 207):
  - Axiom 1: all probabilities are numbers between 0 and 1 inclusive.
  - Axiom 2: a tautology has probability 1.
  - Axiom 3: if h and h* are exclusive, $P(h\text{-or-}h^*)=P(h)+P(h^*)$.
  - Axiom 4: $P(h|j)=P(h\&j)/P(j)$, provided $P(j)>0$.
- Derivation of Bayes's theorem from axiom 4: $P(h\&j)$ equals both $P(h|j)P(j)$ and $P(j|h)P(h)$, so these are equal and Bayes's theorem follows (p. 207). (added step: with $j=e$, equate and divide by $P(e)>0$ to get (1). Form (2) follows if $P(e)$ is split as $P(e|h)P(h)+P(e|\text{not-}h)P(\text{not-}h)$; the text does not give this split.)
- **Dutch book argument** (p. 207): if your degrees of belief violate the probability calculus, there are possible combinations of bets that guarantee you a loss. This happens if you accept every bet that fits your beliefs. The bets cover both sides of a proposition at various odds.
- Coin example (p. 207): your belief in heads is 0.6 and in tails is 0.6. By axiom 3, P(heads or tails) = 1.2, which axiom 1 forbids. Conversion: $X=p/(1-p)$, so $0.6/0.4=1.5$. The bookie offers (1) $10 at 1.5:1 on heads, and (2) $10 at 1.5:1 on tails. If heads: win $10, lose $15, net −$5. If tails: also net −$5. Either way you lose (p. 207).
- The author says more complex arguments show that any violation of the probability rules leaves you open to a Dutch book. Bookies are rare, and refusing to bet avoids the threat. The point is supposed to be that such a person is irrational "in an important sense" (p. 208).
- **Updating**: Bayesianism gives a theory of rational belief change. After observing e (p. 208):
$$P_{new}(h)=P_{old}(h|e)\tag{3}$$
  "Today's posteriors are tomorrow's priors." A different set of Dutch book arguments is used to argue for (3). Special moves are needed for "old evidence", and a different formula applies when e is itself uncertain (p. 208).
- Under strict subjectivism, no coherent set of degrees of belief is "closer to the real facts about probability" than another. Some Bayesians want an additional objective sense, which needs extra arguments (p. 208).

*Intuition note:* The Dutch book argument tries to show that following the probability rules is required if you want to avoid a guaranteed betting loss. Probability here measures how you would bet, not a fact about the coin.

### 14.4 Assessing Bayesianism (pp. 208–210)
- Initial priors are a free choice, so long as the axioms hold. Some see this as a strength, some as a weakness: Bayesianism cannot criticise very strange priors, and the end point seems to depend on the start (p. 209).
- **Reply (Bayesians):** the starting point is "washed out" by evidence under rational updating. Condition: two people with very different priors for h but the same likelihoods for all possible evidence, and who see the same evidence. Their probabilities for h come closer. For any initial disagreement and any degree of closeness (e.g. within 0.001), some amount of evidence achieves it (p. 209).
- **Author's caveat and Kyburg's point:** the author notes that convergence could take a very long time. Kyburg's way of putting it: for any amount of evidence and any measure of agreement, some initial priors keep the two people from agreeing. The author concludes that these "in the limit" proofs may not help much, so some Bayesians try to constrain initial priors (p. 209).
- **Godfrey-Smith's more basic objection:** the proofs assume shared likelihoods. There is no general reason why people who disagree massively should agree on the relevance of possible observations. This is another aspect of holism. Textbook gambling and sampling examples are not typical. The author suggests that convergence results help little with theory choice in science. He adds that it is unclear how much "washing out" matters to Bayesianism (p. 210).
- **Grue (p. 210):** the standard Bayesian reply is that both inductions ("all emeralds are green" and "all emeralds are grue") are confirmed by observed green emeralds. The green hypothesis has a much higher prior for most people, so a higher posterior. The author then asks why the grue prior is low. Nothing prevents someone from setting the priors the other way. A prior usually reflects past experience with colours and minerals, but need not: the author imagines someone who has never thought about emeralds and arbitrarily sets a higher grue prior. Bayesianism offers no criticism if she is coherent and updates properly. He asks "Is this a bad result, or a good one?" and leaves it open here (p. 210).

### 14.5 Scientific Realism and Theories of Evidence (pp. 210–214)
- It is unclear which of the ideas below compete with Bayesianism rather than complement it (pp. 210–211).
- The old empiricist picture: testing confirms and disconfirms generalisations by observation. Disconfirmation needs only deduction. Confirmation needs a special inductive logic. This failed to connect with real science and failed on its own terms (p. 211).
- Author's better picture: testing is typically an attempt to choose between rival hypotheses about the hidden structure of the world. These may be mathematical models or descriptions, causal mechanisms or other structures. The aim may be a whole new explanation or only a parameter value. The patterns may be general or particular past events (e.g. "Where did HIV come from?") (p. 211). An analogy common in the Scientific Revolution was a clock watched from outside (Shapin 1996). The author calls it too restricted, but closer to the truth than the picture in much twentieth-century empiricism (p. 211).
- "Typically" does not mean "always". Kuhn and Laudan rightly stressed that theories and paradigms bring different accounts of what a good theory should do. So we may need a **pluralist** theory of evidence (pp. 211–212).
- **Explanatory inference** (chapter 3: inference from data to a structure or process that would explain them) is more important in real science than traditional induction. It can be argued that good inferences about what patterns will continue typically come via inferences about what the world is like (p. 212).
- **Eliminative inference**: supporting one option by ruling out the others. The author expects it "surely" to be part of the answer (p. 212). It is the Sherlock Holmes style of reasoning (p. 212).
  - It was neglected partly because philosophers assumed any theory has infinitely many rivals, so ruling out finitely many changes nothing. The author says this may not be a good argument, since relevant alternatives may be constrainable (p. 212).
  - Platt (1964) argued that good science is generally based on eliminative inference; the author says his view looked like a modified version of Popperian testing. Philosophers mostly ignored it. Earman (within Bayesianism, 1992) and Kitcher (1993, without Bayesianism) revived it (p. 212).
  - Deductive form: all options but one are decisively ruled out (the argument is only as good as its premises). Nondeductive forms: alternatives are ruled out less decisively, or most but not all are ruled out, giving partial support. Bayesianism fits the nondeductive cases because it handles evidence comparatively: for one hypothesis to gain credibility, another must lose (pp. 212–213).
  - Scientists clearly use it. It is also important for the hardest cases, where new kinds of theory won head-to-head contests (Darwin vs. creationism, Galileo vs. Aristotelian physics, Skinner vs. Chomsky). The chief difficulty is knowing that all relevant alternatives were considered. It can be argued (Stanford 2001) that scientists constantly tend toward overconfidence here: they often thought they had ruled out all feasible alternatives, but in hindsight they had not, because we now believe a theory they did not consider (p. 213).
  - It should not be central to everything. Support can also be more direct (p. 213).
- **Simplicity (parsimony):** scientists often prefer the simpler of two explanations. The author thinks little progress has been made in understanding or justifying this (p. 214).

*Intuition note:* Elimination works well when the list of suspects is trustworthy. Its weak point is the list itself, and history shows that a theory we now believe was sometimes missing from it.

### 14.6 Procedural Naturalism (Optional Section) (pp. 214–217)
- **Main idea:** analyse evidence, confirmation and testing by focusing on procedures. An observation supports a theory by virtue of the procedure it is embedded in. Procedures can be informal. One important source is Reichenbach, who was also influenced by statistical methods used in science; the author links his own version to naturalism. It uses reliability: a good procedure can reliably answer the questions put to it. Some ideas can be combined with Bayesianism and with eliminative inference (p. 214).
- **Ravens (p. 214–216).** The puzzle (chapter 3): if instances confirm generalisations and confirmation passes to logical equivalents, a white shoe (nonblack nonraven) confirms "all ravens are black" via "all nonblack things are nonravens" (p. 214).
  - Two questions (p. 215). General: what proportion of ravens are black? Specific: are 100 percent of ravens black? A random sample of reasonable absolute size answers them reliably.
  - Sampling procedures (p. 215):
    - Random sample of ravens, recording colour: answers both questions.
    - Random sample of nonblack things, recording whether each is a raven: useless for the general question, but reliably answers the specific one (it can find nonblack ravens).
    - Sample of black things, or of nonravens: answers neither, without further assumptions.
  - So a white shoe is evidence if found in a random sample of nonblack things. In a sample of nonravens it tells us nothing. A black raven is informative in a random sample of ravens, and tells nothing in a sample of black things (pp. 215–216).
  - Conclusion: an observation is evidence only if embedded in the right procedure. Hempel was wrong that instances always confirm. Deduction is an exception: a black raven refutes "no ravens are black" whatever the procedure (p. 216).
  - This extends the "order of observation" idea (Horwich 1982): what matters is procedure, not order (p. 216).
- **Grue (pp. 216–217).** The author thinks "the grue problem" combines several problems (including simplicity) and offers part of an answer.
  - Statistical methods require assumptions. They fail in simple form if collecting the data changes the objects in a relevant way (p. 216).
  - Grue: first observed before 2010 and green, or not observed before 2010 and blue. This is not a colour change at a date (p. 217).
  - Take a sample containing all previously observed emeralds, all grue. Had they not been observed before 2010, they would not be grue (they are green). So grueness depends on observation, and the observation process interferes with it. Hence grueness cannot be extrapolated from sampled to unsampled emeralds. The problem does not arise for greenness (p. 217).
  - This resembles a **confounding variable** problem: "grue" turns observation or sampling into a confounding variable. Jackson (1975) proposed a roughly similar solution without statistical framing (p. 217).

*Intuition note:* Whether a data point counts depends on how it was collected. The same shoe or raven can be evidence in one sampling scheme and worthless in another.

### Further Reading (pp. 217–218)
Suggestions on Bayesianism (Howson and Urbach; Earman; Skyrms; Resnik), eliminative inference (Earman chap. 7; Kitcher chap. 7), simplicity (Forster and Sober 1994), and procedural naturalism (Reichenbach; Goldman; work on causal structure inference by Pearl; Spirtes, Glymour and Sheines) (pp. 217–218).

## Toy example (ours, not from the text)
Hypothesis h: "this coin lands heads 80% of the time". Alternative not-h: a fair coin (50%). Both people agree on the likelihoods: $P(\text{head}|h)=0.8$, $P(\text{head}|\text{not-}h)=0.5$. Person A has prior $P(h)=0.1$; person B has prior 0.9. Both see two heads in a row.

Person A:
- After head 1: $\frac{0.1\times0.8}{0.1\times0.8+0.9\times0.5}=\frac{0.08}{0.53}\approx0.151$.
- After head 2 (the posterior becomes the prior): $\frac{0.151\times0.8}{0.151\times0.8+0.849\times0.5}=\frac{0.1208}{0.5453}\approx0.221$.

Person B:
- After head 1: $\frac{0.9\times0.8}{0.9\times0.8+0.1\times0.5}=\frac{0.72}{0.77}\approx0.935$.
- After head 2: $\frac{0.935\times0.8}{0.935\times0.8+0.065\times0.5}=\frac{0.748}{0.7805}\approx0.958$.

The gap shrinks from $0.9-0.1=0.8$ to $0.958-0.221\approx0.737$. Convergence happens but is slow, and it depends on the two people sharing likelihoods. If A thought a head was equally likely under h and not-h, the heads would not move A's belief at all.

## Concepts
- [[bayesian-confirmation]] — e confirms h if $P(h|e)>P(h)$; belief is updated by Bayes's theorem (p. 204)
- [[bayes-theorem]] (new) — $P(h|e)=P(e|h)P(h)/P(e)$, a consequence of axiom 4 (pp. 203, 207)
- [[prior-likelihood-posterior]] (new) — $P(h)$, $P(e|h)$, $P(h|e)$: the three kinds of probability in the theorem (p. 204)
- [[subjective-probability]] (new) — probability as degree of belief, read from fair betting odds (pp. 205–206)
- [[dutch-book-argument]] — incoherent degrees of belief permit bets with guaranteed loss (p. 207)
- [[washing-out-of-priors]] (new) — with shared likelihoods, differing priors converge given enough evidence (p. 209)
- [[confirmation-holism]] — the author links disagreement about likelihoods to "the problem of holism" (p. 210)
- [[explanatory-inference]] (new) — inference from data to a structure or process explaining them (p. 212)
- [[eliminative-inference]] (new) — supporting a hypothesis by ruling out alternatives; deductive or nondeductive (p. 212)
- [[procedural-naturalism]] (new) — evidence and confirmation analysed via the reliability of the procedure producing the observation (p. 214)
- [[confounding-variable]] (new) — a factor interfering with extrapolation from a sample; "grue" makes observation one (p. 217)
- [[scientific-realism-vs-constructive-empiricism]] — here, the realist picture of testing as choice among hidden-structure hypotheses (p. 211)

## Canonical instances
- [[car-at-party-example]] — worked Bayes update, 0.5 → about 0.89 (p. 204)
- [[coin-dutch-book]] — beliefs 0.6 and 0.6 lose $5 for sure (p. 207)
- [[ravens-paradox]] — a white shoe's evidential value depends on the sampling procedure (pp. 214–216)
- [[grue-paradox]] — Bayesian reply via priors (p. 210); author's reply via observation as confounder (p. 217)
- [[sherlock-holmes-elimination]] — eliminative inference in fiction (p. 212)
- [[scientific-head-to-head-contests]] — Darwin vs. creationism, Galileo vs. Aristotle, Skinner vs. Chomsky (p. 213)

## Bridges (candidates)
- [same-math] Subjective probability ↔ decision theory/economics: subjective probabilities plus utilities generate choices (pp. 205–206).
- [structural-analogy] Procedural naturalism ↔ epistemology of reliabilism: both judge support by the reliability of the process (the author cites Goldman's emphasis on reliability, p. 218).
- [structural-analogy] Grue as sampling-induced confounder ↔ statistics/causal inference: a variable that disturbs extrapolation from a sample (pp. 216–217).
- [metaphor] "Today's posteriors are tomorrow's priors" ↔ sequential learning in other fields; only a loose comparison.

## Questions this raises
- If priors are unconstrained, can Bayesianism say why the green hypothesis is better than the grue one, or only that most people prefer it?
- How can we constrain the set of relevant alternatives so that eliminative inference is not undermined by unconsidered theories?
- If evidence is procedure-relative, how would an informal, non-experimental procedure be judged reliable?
- Can the Bayesian "comparative" treatment of evidence and procedural reliability be combined, as the author suggests some ideas can?

## Reading notes
- Printed page = pdf page − 15 (for example, PDF page 217 is printed page 202). All page references here use printed numbers.
- Page images were checked for pdf 222 (axioms, Dutch book numbers) and pdf 232 (grue definition); the text layer matched them.
- The grue definition uses the year 2010, as printed.
- The unit's "Further Reading" is reported only briefly. Sections 14.1–14.6 are all covered.
- The author flags the chapter as the hardest in the book and 14.6 as optional (pp. 203, 214).
