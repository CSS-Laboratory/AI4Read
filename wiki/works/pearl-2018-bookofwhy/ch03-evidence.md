---
id: pearl-2018-bookofwhy/ch03-evidence
work: pearl-2018-bookofwhy
unit: "Chapter 3 — From Evidence to Causes: Reverend Bayes Meets Mr. Holmes"
pages: "pdf 92–129 (printed numbers not visible; cited as pdf N)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# From Evidence to Causes: Reverend Bayes Meets Mr. Holmes

## L0 — One line
Bayes's rule lets us turn easy "forward" probabilities (effect given cause) into the "inverse" probabilities we need (cause given effect), and Bayesian networks, built from chains, forks and colliders, extend this to many variables and form the probabilistic base of causal diagrams.

## L1 — The gist (≤ 120 words)
How can we reason from evidence back to causes? Bayes's rule answers this for one cause and one effect: it combines a forward probability with a prior. Pearl then scales it up to Bayesian networks, which pass messages between variables (belief propagation). The networks are used in DNA identification (Bonaparte) and in mobile-phone decoding. Their three basic junctions (chain, fork, collider) leave distinct fingerprints of dependence and independence in data. A causal diagram is a Bayesian network whose arrows signify causal relations (or at least the possibility of one). Data alone cannot tell some causal diagrams apart, for example a fork from a chain. The network also cannot say what happens under intervention.

**Prerequisites:** proportions and conditional probability ("given that"); multiplying fractions; the idea of a diagram with arrows.

## L2 — Key ideas
- Forward probability (effect given cause) is easier to judge than inverse probability (cause given effect). Bayes set out to show how to compute the inverse (pdf 97–99).
- Bayes's rule follows from computing P(S AND T) in two orders: $P(S\mid T)P(T)=P(T\mid S)P(S)$. It is a rule for updating belief in a hypothesis (pdf 100–101).
- The prior matters. With a prior of 1/700, a positive mammogram gives only about 1/116 probability of cancer. P(test | disease) is robust across patients, but P(disease | test) is not (pdf 103–106).
- Bayesian networks keep probability but make it computable. Nodes send messages: conditional probabilities downward, likelihood ratios upward. This is belief propagation (pdf 107–110).
- Chains and forks make end variables independent once the middle variable is known. A collider does the opposite and creates dependence when conditioned on. Pearl says these three junctions suffice to read off all independencies a network implies, but in isolation they give only a glimpse and the full key is d-separation (pdf 111–114).
- Networks need a diagram plus conditional probability tables. Tables grow fast, so sparse networks are needed (pdf 114–118).
- Real uses are Bonaparte DNA matching and turbo and Gallager codes in phones. Both rely on belief propagation (pdf 119–124).
- Bayesian network ≠ causal diagram. Causal assumptions can be falsified by data, but a fork and a chain cannot be told apart by data alone. Only causal diagrams address "wiggling" (intervention) (pdf 125–127).

## L3 — Walkthrough

### Opening and Bonaparte (pdf 92–94)
- **Induction** (evidence → hypothesis) is distinguished from **deduction** (hypothesis → conclusion). Holmes used induction to generate hypotheses, then deduction by elimination (pdf 92).
- Case: MH17 was shot down on 17 July 2014 with 298 people on board. The Netherlands Forensic Institute used the Bayesian-network program **Bonaparte** to combine DNA from several family members. By December 2014 it had identified remains of 294 of 298 victims (pdf 93).
- Bayesian networks are also used in speech recognition, spam filters, weather forecasting, Xbox skill ranking and phone decoding (pdf 94).
- Pearl's definition: a causal diagram is a Bayesian network in which every arrow signifies a direct causal relation, or at least the possibility of one. Not all Bayesian networks are causal. For a rung-two or rung-three query you must draw the network with careful attention to causality (pdf 94).

### Reverend Bayes and inverse probability (pdf 94–106)
- **Context.** Hume argued that eyewitness testimony could never prove a miracle. Bayes asked how much evidence it takes to make an improbable hypothesis probable (pdf 94–96). Price's introduction drew theological implications. Bayes himself did not discuss them (pdf 96–97).
- **Pool-table example.** Forward question: with table length $L$, the probability the ball stops within $x$ feet of the end is $x/L$ (12-ft table, 1 ft: 1/12; 8-ft: 1/8). Inverse question: given $x=1$ ft, what is the probability that $L=100$? Common sense says $L=50$ is more likely than $L=100$, but gives no number (pdf 97–99).
- **Why the asymmetry.** $L$ is the cause and $x$ the effect. People predict effects from causes easily. Going from effect to cause needs much more information (the broken window, pdf 99).
- **Teahouse (Table 3.1).** Of 12 customers, 8 order tea (customers 1, 5, 6, 7, 8, 9, 10, 12), 4 of those also order scones, and 5 order scones in total. Two routes to the same proportion: $(1/2)(2/3)=1/3$ and $(4/5)(5/12)=1/3$ (pdf 99–100).
- **Derivation.** The two routes give $P(S\text{ AND }T)=P(S\mid T)P(T)$ and $P(S\text{ AND }T)=P(T\mid S)P(S)$. Both equal the same quantity, so
$$P(S\mid T)\,P(T)=P(T\mid S)\,P(S)\tag{3.1}$$
This is Bayes's rule. Given the forward probability and the two marginals, the inverse follows (pdf 100).
- Numbers: $P(T\mid S)(5/12)=(1/2)(2/3)$, so $P(T\mid S)=4/5$. The prior chance of tea is 2/3 and rises to 4/5 after scones are ordered (pdf 101).
- *Intuition note:* Bayes's rule updates a belief with the evidence just seen. You judge the easy direction and let arithmetic give the hard one.
- **Two objections (Pearl's discussion).**
  - Philosophical: is "given that I know T" the same as "among cases where T occurred"? (pdf 101). Bayes gave the first formal definition $P(S\mid T)=P(S\text{ AND }T)/P(T)$. The vertical bar came in 1931 with Jeffreys (pdf 102).
  - Pearl says that, epistemologically, the rule works as a normative rule for updating belief. It implies that belief in S after learning T is never lower than the earlier belief in S AND T. It also implies that the smaller $P(T)$ is, the more convinced one should become of its cause S (pdf 102). Bayes and Price saw this as a reply to Hume.
  - Practical: the pool-table problem needs a prior for $L$, which varies by person (someone who has seen only snooker tables expects long tables). This is called subjectivity. Some see it as a flaw, others as an advantage because experience is combined with data transparently (pdf 102–103).
- **Mammogram.** Forward = sensitivity $P(\text{test}\mid\text{disease})$. Inverse = $P(\text{disease}\mid\text{test})$, the quantity we care about (pdf 103). Rewrite Bayes's rule as
$$P(D\mid T)=\text{(likelihood ratio)}\times P(D),\qquad \text{likelihood ratio}=\frac{P(T\mid D)}{P(T)}\tag{3.2}$$
(pdf 103). Pearl says the evidence $T$ augments $P(D)$ "by a fixed ratio, no matter what the prior probability was" (pdf 104).
- Numbers for a 40-year-old woman (BCSC data): prior 1/700; sensitivity 73%; false-positive rate about 12% (pdf 104).
  - $P(T)$ is a weighted average: $P(T)=\tfrac{1}{700}(73\%)+\tfrac{699}{700}(12\%)\approx 12.1\%$ (pdf 104).
  - Likelihood ratio $=73/12.1\approx 6$, so the updated probability is $6\times 1/700\approx 1/116$, less than 1% (pdf 104).
- Figure 3.3: of 3000 women, 4 have cancer (3 test positive, 1 negative); of 2996 without cancer, 360 test positive. So only 3 of 363 positives have the disease (pdf 105). Pearl says this confusion partially explains the outcry when a US task force in 2009 recommended against annual mammograms at 40 (pdf 105).
- For a woman with a one-in-twenty yearly risk, Pearl says a positive test raises the probability to almost one in three (pdf 106).
- **Robustness.** $P(\text{test}\mid\text{disease})$ stays relatively invariant across patients. $P(\text{disease}\mid\text{test})$ depends on risk. Pearl says this explains to some degree why physicians organize their knowledge and communicate with forward probabilities (pdf 106).
- *Intuition note:* in this example the disease is rare, so the few true positives are swamped by false positives. Pearl says our surprise comes from confusing the forward and the inverse probability.
- **Bayes's own handling of the prior.** Bayes was interested in the future consequence (where the next ball lands). He also assumed $L$ is set mechanically by shooting a ball from a greater distance $L^*$, which makes $P(L)$ estimable from data (pdf 106).
- Pearl: "in many ways" Bayes's rule is a distillation of the scientific method; it tells us how to perform step (4), updating belief in the hypothesis after evidence (pdf 106).

### From Bayes's rule to Bayesian networks (pdf 107–110)
- Early-1980s AI used rule-based expert systems, which struggled with uncertainty. Fuzzy logic (Zadeh), belief functions (Shafer) and certainty factors (Feigenbaum) "modeled the expert, not the world". They could not work in both diagnostic and predictive modes. In the certainty-factor approach, "If fire then smoke" combined with "if smoke then fire" gave a runaway buildup of belief (pdf 107).
- Pearl's 1982 proposal: keep probability, but represent it as a network of loosely coupled variables, each interacting with few neighbors, instead of huge tables (pdf 107–108).
- The inspiration was Rumelhart's 1976 reading model, in which many levels exchange information in parallel (Fig. 3.4, pdf 108–109).
- The messages are conditional probabilities from parent to child and likelihood ratios from child to parent. Applying these rules repeatedly is **belief propagation**, in strict compliance with Bayes's rule (pdf 109–110).
- The challenge was to make the network settle to an equilibrium that equals the "textbook" answer, whatever the order of messages. This took years. By the end of the 1980s networks were practical (pdf 110).

### Bayesian networks: what causes say about data (pdf 110–114)
- Bayes's rule is the simplest network (Tea → Scones, Disease → Test). A Bayesian network assumes no causal meaning for the arrow. It only marks the known forward probability (pdf 110).
- Three-node **junctions** are the building blocks (pdf 111).
- **1. Chain** $A\to B\to C$ (Fire → Smoke → Alarm).
  - The mediator $B$ "screens off" $A$ from $C$. Once Smoke is known, learning about Fire does not change belief in Alarm (pdf 111).
  - With a faulty alarm failing 5% of the time, $P(\text{Alarm}=1\mid\text{Smoke}=1)=95\%$ whatever Fire is (pdf 111).
  - Looking only at rows with Smoke = 1 is **conditioning**. Fire and Alarm are **conditionally independent** given Smoke (pdf 111–112).
- **2. Fork** $A\leftarrow B\to C$.
  - $B$ is a common cause (confounder). Example: Shoe Size ← Age → Reading Ability. It makes $A$ and $C$ correlated without a direct causal link (Pearson and Yule's "spurious correlation"). This can be eliminated by conditioning on age; for seven-year-olds only, we expect no relationship. $A$ and $C$ are conditionally independent given $B$ (pdf 112).
  - These independences hold for junctions in isolation. If other causal paths surround them, those must be considered too (pdf 112).
  - Pearl says the three junctions suffice for reading off all independencies implied by a network (pdf 113).
- **3. Collider** $A\to B\leftarrow C$ (Talent → Celebrity ← Beauty).
  - The two causes are unrelated in the general population, but conditioning on the middle variable makes them dependent. Among celebrities, an unattractive one is more likely talented (collider bias, "explain away") (pdf 113).
  - If, for simplicity, either trait alone suffices, a very good actor's success is explained and he need not be any more beautiful than the average person. A bad actor's success must be explained by looks. The effect persists in more realistic cases (pdf 113).
- *Intuition note:* in a chain or fork, conditioning on the middle cuts the link between the ends. In a collider, conditioning on the middle creates a link.
- The junctions are "keyholes" between rungs one and two. The full key is **d-separation**, which comes in Chapter 7 (pdf 114).

### Where is my bag? (pdf 114–118)
- A network has a diagram (the engine) and conditional probability tables (the fuel). Each node needs its probability given its parents. A root node needs only a prior (pdf 114).
- A root node does not mean "no causes". It means prior causes are summarized in $P(A)$. A cause of Disease that directly affects Test must appear in the diagram. Family history need not, if it does not affect Test once Disease is known (pdf 114–115).
- Table 3.2, with rows D, columns T (in %): D=0: T=0 88, T=1 12; D=1: T=0 27, T=1 73 (pdf 115).
- **Bag example** (Conrady–Jouffe). Two causes of "Bag on Carousel": Bag on Plane and Elapsed Time (Fig. 3.5). Assumptions: all bags unloaded within 10 minutes; $P(\text{bag on plane})=50\%$. If the bag is on the plane, $P(\text{carousel}=\text{true})$ is 10% per minute elapsed (50% at 5 min, 100% at 10). If it is not on the plane, the probability is 0 (pdf 116, Table 3.3, pdf 117).
- Inverse question: given that the bag has not appeared after $x$ minutes, what is the probability it was on the plane? Results: 47% after 1 min, 33% after 5, 0 after 10. The curve (Fig. 3.6) is not a straight line (pdf 117). Pearl's reading: only one-third of hope is abandoned in the first half of the allotted time (pdf 117).
- **Size problem.** This network has $2\times 11=22$ parent states. A node with ten two-state parents has more than 1,000 rows. With ten ten-state parents it has 10 billion rows. Networks are therefore kept **sparse**, and exploiting sparseness was a technical advance (pdf 118).

### Bayesian networks in the real world (pdf 118–124)
- **Bonaparte.** The Netherlands Forensic Institute uses it for missing persons, criminal and immigration cases. Paternity or sibling indices handle one close relation only. Bonaparte converts a pedigree into a Bayesian network (Figs 3.7–3.8, pdf 119–121). Each person's two alleles (gene copies from mother and father) are hidden nodes, since a genotype does not show which allele came from which parent (pdf 119, 121).
- Belief propagation then updates every node when new evidence enters anywhere, including DNA from an aunt or second cousin. It also learns from identifications already made. Its transparency contrasts with machine-learning "black boxes" (pdf 121).
- At present, no identification is made by the computer acting alone. It ranks candidates with likelihood ratios, and investigators add physical evidence and intuition (pdf 121–122).
- **Phone codes.** Noisy radio transmission flips bits. Simple repetition code: send 111 or 000. A received 101 is read as 111, the more likely single-error explanation. It makes messages three times longer (pdf 122).
- Decoding is an inverse-probability problem: message sent given message received (pdf 122).
- **Turbo codes** (Berrou, 1993). Encode the message twice, once directly and once after scrambling (Fig. 3.9b). No formula decodes this directly, but repeated belief propagation works empirically. About 99.999% of the time it recovers the correct bits, with much shorter codewords (pdf 123).
- Berrou did not know he was using Bayesian networks. MacKay noticed about five years later. Gallager's 1960 code used belief propagation too but needed thousands of processors on a chip, and was rediscovered by MacKay in 1998 (pdf 124).
- 2G phones used soft decoding without belief propagation, 3G used turbo codes, and 4G used Gallager's turbo-like codes. The consumer benefits are less energy use and more bars in more places (pdf 124).

### From Bayesian networks to causal diagrams (pdf 124–128)
- All probabilistic properties of Bayesian networks, including junctions and belief propagation, remain valid in causal diagrams (pdf 124–125).
- A Bayesian network is "a compact representation of a huge probability table". The arrows mean only that child probabilities are related to parent values by the table, and that this relation is sufficient. A missing arrow means independence once the parents are known (pdf 125).
- In a causal diagram the question is which variables a node "listens" to. $A\to B\to C$ means $B$ listens to $A$ only, $C$ to $B$ only, and $A$ to no one, since it is determined by external forces outside the model. Pearl says this listening metaphor encapsulates the entire knowledge a causal network conveys; the rest can be derived, sometimes by leveraging data (pdf 125).
- Reversing the chain to $A\leftarrow B\leftarrow C$ changes the causal reading but keeps the same independences. Two consequences:
  - Causal assumptions are testable. If $A$ and $C$ are not independent given $B$ in the data, the chain model is incompatible with the data (pdf 125).
  - Some models can never be told apart by data, however large. A fork and a chain imply the same independences (pdf 125–126).
- Hypothetical-experiment reading: an arrow $A\to C$ means that if we could wiggle only $A$, we would expect to see a change in the probability of $C$. A missing arrow means no change once $C$'s parents are held constant. "Hold constant" means physically blocking variation, which is different from "know the value of" (pdf 126).
- A Bayesian network answers only rung-one questions and cannot tell seeing from doing. The causal fork says wiggling $A$ would have no effect on $C$, whereas a Bayesian network treating chain and fork alike only predicts that observed changes in $A$ go with changes in $C$ (pdf 126).
- The graph–data relationships (discovered 1980–1988) let us emulate wiggling with a smart sequence of conditioning operations. For the fork, the correlation after conditioning on $B$ equals the experimental one, estimated as zero here (pdf 126–127).
- Mediation ("Why?") questions need two simultaneous interventions: wiggle $A$ and hold $B$ constant. The graph tells whether observations can emulate this (pdf 127).
- Pearl: in 1988 these capabilities lay in the future. Statistics has avoided causal language, except in randomized controlled trials. Chapter 4 turns to confounding and RCTs (pdf 127–128).

## Toy example (ours, not from the text)
**Bayes with a fire alarm.** Suppose $P(\text{Smoke})=0.1$, $P(\text{Alarm}\mid\text{Smoke})=0.9$ and $P(\text{Alarm}\mid\text{no Smoke})=0.2$.
- $P(\text{Alarm})=0.1(0.9)+0.9(0.2)=0.09+0.18=0.27$.
- Likelihood ratio $=0.9/0.27=3.33$, so $P(\text{Smoke}\mid\text{Alarm})=3.33\times0.1=1/3$. Check: $0.09/0.27=1/3$.

**Collider.** Let Talent and Beauty each be yes/no with probability 1/2, independent. Celebrity = yes if at least one is yes.
- The four combinations are each 1/4. Celebrities: (both), (T only), (B only), i.e., 3 cases.
- $P(T\mid C)=2/3$. Given also Beauty = no, $P(T\mid C,\neg B)=1$. Given Beauty = yes, $P(T\mid C,B)=1/2$.
- So among celebrities, knowing beauty changes belief about talent. In the full population it does not.

## Concepts
- [[bayes-theorem]] — Bayes's rule (3.1): reverse a conditional probability using the two marginals (pdf 100).
- [[prior-distribution]] — probability before the evidence, e.g., 1/700 for cancer (pdf 101, 104).
- [[likelihood]] — here $P(T\mid D)$, the forward probability, e.g., test sensitivity (pdf 103–104).
- [[posterior-distribution]] — updated probability after evidence, e.g., 1/116 (pdf 104).
- [[base-rate-neglect]] — surprise at the mammogram result, arising from confusing forward and inverse probability (pdf 105).
- [[inverse-probability]] (new) — Bayes-era name for P(cause | effect), the hard direction (pdf 97).
- [[likelihood-ratio]] (new) — $P(T\mid D)/P(T)$, the factor that multiplies the prior (3.2) (pdf 103).
- [[bayesian-network]] (new) — network of variables with conditional probability tables. Its arrows need not be causal (pdf 110).
- [[belief-propagation]] (new) — repeated message passing between nodes using Bayes's rule (pdf 110).
- [[conditional-probability-table]] (new) — a node's probabilities given each combination of its parents (pdf 114–115).
- [[conditional-independence]] (new) — independence after conditioning, i.e., screening off (pdf 111–112).
- [[fork-chain-collider]] — the three three-node junctions that Pearl says suffice for reading off all independencies implied by a network (pdf 113); the full rule is d-separation (pdf 114).
- [[collider-bias]] (new) — conditioning on a common effect makes independent causes dependent (explain-away) (pdf 113).
- [[causal-dag]] — Bayesian network whose arrows mean direct causation, with the "listening" reading (pdf 94, 125).
- [[d-separation]] — the full rule combining the three junctions, promised for Chapter 7 (pdf 114).
- [[ladder-of-causation]] — Bayesian networks answer rung one only. Causal diagrams reach rungs two and three (pdf 126).
- [[do-operator]] — only informally: "wiggling" and "holding constant", as opposed to conditioning (pdf 126–127).

## Canonical instances
- [[billiard-table-bayes]] — Bayes's inverse problem about table length $L$ (pdf 97–99).
- [[teahouse-scones]] — derives Bayes's rule from data (pdf 99–101).
- [[mammogram-bayes]] — prior 1/700, posterior 1/116 (pdf 103–106).
- [[fire-smoke-alarm-chain]] — screening off (pdf 111).
- [[shoe-size-age-reading-fork]] — spurious correlation (pdf 112).
- [[talent-celebrity-beauty-collider]] — explain-away (pdf 113).
- [[bag-on-carousel]] — two-parent table and curve of falling probability (pdf 115–118).
- [[bonaparte-dna-mh17]] — pedigree network for victim identification (pdf 119–121).
- [[turbo-codes]] — belief propagation in phone decoding (pdf 122–124).

## Bridges (candidates)
- [same-math] Bayes's rule (3.2) here ↔ bayesian: posterior ∝ likelihood × prior — Pearl's form is posterior = (likelihood/evidence) × prior.
- [same-math] Conditional independence in chains and forks ↔ causal inference: d-separation on paths.
- [structural-analogy] Bayesian network message passing ↔ cognition: Rumelhart's parallel layers in reading.
- [structural-analogy] Collider bias ↔ statistics: selection by conditioning on a common effect.
- [metaphor] "Listening" ↔ structural causal models: each variable determined by its parents plus external noise.

## Questions this raises
- If a fork and a chain give the same independences, what extra assumptions or experiments tell them apart?
- How exactly does conditioning on $B$ emulate an experiment on $A$ in a fork?
- When is a prior estimable from data (as Bayes assumed with $L^*$), and when is it purely personal?
- Which junction patterns stay distinguishable in larger networks? (Chapter 7)

## Reading notes
- No printed page numbers appear in the labels or images. All citations use PDF page numbers (pdf 92–129).
- Table 3.2 and Table 3.3 are empty in the text layer. I read them from the page images.
- Pearl says a one-in-twenty prior with a positive test gives "almost one in three" (pdf 106). Using his sensitivity and false-positive rate, my own check gives about 24% (0.0365/0.1505). This is not in the text.
- Pearl says the evidence augments the probability "by a fixed ratio, no matter what the prior" (pdf 104). The ratio $P(T\mid D)/P(T)$ itself uses $P(T)$, which is computed from the prior. This is my observation, not the author's.
- Figure 3.7 (pedigree) has no extractable text. The last page (pdf 129) holds only a captioned illustration (Daniel).
- Arrow symbols in the junction lists are lost in the text layer. I reconstructed them from the page image for pdf 111, and from the author's own names for the junctions (chain, fork, collider) for pdf 112–113 and 125–127, where no image was available to me.
