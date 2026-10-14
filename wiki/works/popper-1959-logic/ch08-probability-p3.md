---
id: popper-1959-logic/ch08-probability-p3
work: popper-1959-logic
unit: "Chapter 8, Probability (part 3/3): end of §66, §§67–72"
pages: 184–208
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Probability, part 3: how non-falsifiable probability statements can serve empirical science

## L0 — One line
Probability statements are linked to basic statements only through their existential content, and they are used as falsifiable physical laws through a methodological rule that forbids explaining reproducible effects as accumulations of accidents.

## L1 — The gist (≤ 120 words)
Popper asks how probability hypotheses can act as natural laws when no basic statement can falsify them. His answer: they logically entail existential hypotheses, which gives them a graded, provisional link to observation. Applied without precautions, they can "explain" any regularity and so become metaphysics. A rule against explaining reproducible effects as accidents (neglecting extreme improbabilities) makes them falsifiable in practice. The unit then treats chance versus law, why statistical conclusions need statistical premises, and a definition of single-case probability that, Popper says, may eliminate the conflict between objective and subjective theories.

**Prerequisites:** the frequency interpretation of probability (reference sequences, relative frequency); Bernoulli's theorem; the falsifiability criterion; basic statements (reports of single observations); extensional (about observable cases) versus intensional (about how a sequence is defined mathematically); "all"- versus "there-is"-statements.

## L2 — Key ideas
- Every probability estimate entails infinitely many existential statements, but not conversely. Popper holds that this explains its graded confirmability (pp. 184–185).
- The randomness requirement has existential form and links probability statements to basic statements. The uniqueness requirement is universal, has no extensional consequences, and lets probability statements contradict each other. The convergence axiom has only intensional significance (pp. 186–188). (Extensional means concerning observable cases; intensional means concerning how a sequence is defined mathematically.)
- Used "without special precautions", probability estimates can "explain" any regularity as an accumulation of accidents. Popper says it seems clear that this is speculative metaphysics and that this goes with non-falsifiability (pp. 189–190).
- Popper proposes a methodological decision never to explain reproducible effects as accidents. For large $n$ this needs no exact "negligible" $\varepsilon$, because $\Delta p$ is insensitive to $\varepsilon$ (pp. 192–195). Here $\varepsilon$ is the small probability that a measured value falls outside the interval $\Delta p$ around the predicted value.
- Probability statements are empirical only as falsifiable statements. The rule forbids reproducible systematic deviations, not atypical segments (pp. 196–197).
- Chance is subjective in Popper's view here (it marks insufficient knowledge). A chance-like sequence implies nothing about lawlessness (pp. 198–200).
- Statistical conclusions need statistical premises. Deterministic micro laws never yield them alone (pp. 200–202).
- Formally singular probability (the probability of a single event) is defined as ${}_\alpha P_k(\beta)={}_\alpha F(\beta)$ for $k\in\alpha$. This dissolves "before/after" paradoxes and bridges to the subjective theory and the theory of range (pp. 203–208).

## L3 — Walkthrough

### §66 (end): probability statements and basic statements (pp. 184–188)
*(Part of the section lies before this unit.)*

**Logical relations.** Popper holds that the relations between probability statements and basic statements can be fully analysed with classical deducibility and contradiction (p. 184). A starred note says he now finds "almost deducible" and "almost contradictory" very useful (p. 184).

Probability statements are neither falsifiable nor verifiable. So they have no falsifiable consequences and are not consequences of verifiable statements. Two converse possibilities remain (p. 184):
- (a) They may have unilaterally verifiable consequences, i.e. purely existential "there-is" consequences.
- (b) They may be consequences of falsifiable universal statements.

Popper says (b) will scarcely help to clarify the relation: a non-falsifiable statement, which says very little, can easily belong to the consequence class of a falsifiable one. He finds (a) of greater interest and fundamental for the analysis (p. 184).

**Result.** From every probability statement an infinite class of existential statements can be deduced, but not vice versa (p. 184). Example: if $p$ is estimated, hypothetically, for an alternative with $0\neq p\neq 1$, one can deduce from this estimate that both ones and zeros will occur in the sequence. Also, after any element $x$ there will occur an element $y$ with property '1' and an element $z$ with '0' (pp. 184–185).

**Universalized existential statements.** A statement of the form "for every $x$ there is a $y$ with observable property $\beta$" is non-falsifiable, because it has no falsifiable consequences. It is non-verifiable, because of "for every". Still it can be better or less well "confirmed", depending on how many of its existential consequences are verified (p. 185). Popper calls such statements universalized existential statements, or existential hypotheses (p. 185).

**Qualification (starred note).** Not every statement of this form is non-falsifiable. Non-falsifiability comes from the unbounded "there is": $y$ may occur as late as it pleases. If the distance from $x$ to $y$ is bounded, the statement may be falsifiable (p. 185, note *2).

**The question.** Do probability statements themselves have the form of existential hypotheses? Every hypothetical estimate entails that the sequence is approximately chance-like, i.e. it entails the (approximate) applicability and the truth of the axioms of the calculus (p. 185). So the question becomes whether those axioms are existential hypotheses (p. 186).

**The requirements of §64 (as used here):**
- **Randomness** has the form of an existential hypothesis. Footnote 2: for every positive $\varepsilon$, every predecessor $n$-tuple and every element with ordinal $x$, there is an element selected by predecessor selection with ordinal $y>x$ such that the frequency up to $y$ deviates from a fixed $p$ by less than $\varepsilon$ (p. 186).
- **Uniqueness** cannot have this form. A statement saying that there is only one such thing is a universal statement, equivalent to saying there are not more than one (p. 186).

**Thesis.** Only the existential constituent, i.e. randomness, creates a logical relation to basic statements (p. 186).
- That a value $p$ with the required properties exists can be provisionally confirmed.
- That only one exists could be significant only if basic statements could establish more than one such value. They cannot, because non-falsifiability is tied to the binomial formula. So uniqueness is extensionally insignificant (p. 186).
- A starred note says this changes if requirement (+2) of note *2 to §64 is adopted. That requirement is empirically significant and makes probability hypotheses falsifiable (p. 186, note *3).

Dropping uniqueness would leave the logical relations and graded confirmability unchanged and give a pure existential hypothesis. But it would lose uniqueness of estimates, and so (so far as uniqueness is concerned) give something different from the usual calculus (p. 187). A starred note says any special requirement of uniqueness can be eliminated without sacrificing uniqueness (p. 187, note *4). Footnote 3 gives an example: Bernoulli's theorem would say only that, among the various probability values of ${}_{\alpha_n}F(\Delta p)$, at least one lies near 1 (pp. 186–187).

**Function of uniqueness.** Randomness relates probability statements to basic statements. Uniqueness regulates relations among probability statements (p. 187).
- Without uniqueness, some could be derivable from others but they could never contradict one another.
- With it, each takes the form of a conjunction of a universal statement and an existential hypothesis. These can stand in the usual relations (equivalence, derivability, compatibility, incompatibility), like ordinary universal theories (p. 187).

**Axiom of convergence.** Like uniqueness, it is a non-falsifiable universal statement, but it demands more. The extra demand has no extensional significance and no logical or formal significance, only intensional significance: it excludes intensionally (mathematically) defined sequences without frequency limits (p. 187).
- In applications we deal only with hypothetical estimates about empirical sequences. So the exclusion is insignificant even intensionally (p. 187).
- It could only warn us against treating as random those empirical sequences we assume have no limit. Popper asks what action we could take in response to this warning, given that criteria of convergence are no more applicable to empirical sequences than criteria of divergence (p. 188).
- These embarrassing questions disappear once the axiom is dropped (p. 188). Schlick had similar misgivings (note 5).

The analysis makes the form and function of the requirements transparent. But decidability now seems more menacing: the requirements look non-empirical, and Popper asks whether this description contradicts the main idea of his approach (p. 188).

> **Intuition note.** A probability statement entails statements such as: later cases of both kinds will keep turning up. No finite run can refute such a statement, because the next case may always come later. But finite runs can still support it to a greater or lesser degree.

### §67: A probabilistic system of speculative metaphysics (pp. 188–190)
Physics uses probability estimates to interpret observed regularities as "macro laws": mass effects of hypothetical micro events. The macro law is deduced by showing that observations agreeing with it have a probability very close to 1, deviating from 1 by an amount as small as we choose. The effect is then said to be "explained" (pp. 188–189).

Used without special precautions, this can lead to speculative metaphysics. Since probability statements are not falsifiable, any regularity can be "explained" this way (p. 189). Popper's example is the law of gravity:
1. Choose elementary events (e.g. the movement of a small particle) and a primary property (direction and velocity).
2. Assume a chance-like distribution.
3. Calculate the probability that all particles in a finite region, in a finite "cosmic period", move accidentally as the law requires. It is negligibly small but not zero (p. 189).
4. Ask how long an $n$-segment, i.e. how long a duration, is needed to expect with probability within $\varepsilon$ of 1 one such period. For any value near 1 the answer is a definite, extremely large finite number (p. 189).
5. If the "world" lasts that long, randomness entitles us to expect a period in which gravity seems to hold although "in reality" only random scattering occurs (p. 190).

The same works for any regularity, so we could "explain" the whole world as a phase in random chaos (p. 190). Popper says it seems clear to him that such speculation is metaphysical and without significance for science, and equally clear that this is connected with non-falsifiability. His demarcation criterion seems to agree here quite well with the ordinary use of the word metaphysical. Probability theories applied without special precautions are not scientific (p. 190).

A starred note adds that Popper regards Haldane's argument as a perfect example of such speculation. Haldane argued that on the probability theory of entropy the world will almost certainly wind itself up again accidentally if we wait long enough (p. 190, note *1).

> **Intuition note.** A hypothesis that can accommodate every possible outcome says nothing. Waiting "long enough" lets chance produce any pattern, so such an "explanation" cannot be tested.

### §68: Probability in physics (pp. 190–197)
Decidability troubles the methodologist, not the physicist (p. 190).

**The physicist's definition.** Some experiments give varying results even under controlled conditions. For the chance-like ones, relative frequencies approach a fixed value on repetition. That value is called the probability, and it is said to be empirically determinable by long series of experiments to any degree of approximation (a passage Popper quotes from Born–Jordan, p. 191). This explains why probability estimates can be falsified (p. 191).

**Objections from mathematicians and logicians** (p. 191–192):
1. By Bernoulli's theorem only *almost all* long segments are stable, and "almost all" just means "very probable". So the definition is circular.
2. When is a series "long"?
3. How do we know the approximation has been reached?

**Popper's reply.** He agrees the objections are justified but keeps the definition. He proposes a methodological decision never to explain physical effects, i.e. reproducible regularities, as accumulations of accidents (p. 192). This narrows the concept of probability. Objection (1) then does not touch him, because he denies that the physical and mathematical concepts are identical (p. 192). A new objection (1′) arises: when is a probability "small"? (p. 192).

**Setup (typical case: macro effects such as gas pressure, produced by many micro events).** Other cases (fluctuations, statistics of chance-like individual events) are said to reduce to this one; a starred note doubts "without much difficulty" (pp. 192–193).
- A well-corroborated law says a magnitude has value $p$. The effect is "precise": no deviation beyond $\pm\varphi$, the interval of imprecision set by measuring technique (p. 193).
- Hypothesis: $p$ is a probability in a micro-event sequence $\alpha$, and $n$ micro events produce the effect. For chosen $\delta$ (interval $\Delta p$), compute the probability that the measured value falls in $\Delta p$. Call the complement $\varepsilon$ (p. 193):

$$ {}_{\alpha_n}F(\overline{\Delta p}) = \varepsilon .$$

- By Bernoulli's theorem, $\varepsilon\to 0$ as $n\to\infty$ (p. 193).
- The three quantities $\varepsilon$, $n$, $\Delta p$ match questions (1′), (2), (3). Choose $\delta\le\varphi$, here $\delta\approx\varphi$. This reduces (3) to (1′) and (2) (p. 193).
- Fixing $\delta$ gives each $n$ a unique $\varepsilon$. So (2) reduces to (1′) and vice versa. All three are answered if we decide which $\varepsilon$ is negligible, but we will not fix one for ever (pp. 193–194).

**Physicist's answer.** He does not choose $\varepsilon$ but $n$, so that the link between $n$ and $\Delta p$ is largely independent of $\varepsilon$ (p. 194). This is justified by the Bernoulli distribution: for each large $n$ there is a characteristic $\Delta p$ near which $\Delta p$ is highly insensitive to $\varepsilon$. The insensitivity grows with $n$. For extreme mass phenomena, $\Delta p$ hardly changes even if $\varepsilon$ changes by orders of magnitude (pp. 194–195). Popper calls $n$ **large** when such changes of $\varepsilon$ move $\Delta p$ only within the condensation bounds of $\pm\varphi$ (p. 195). Then the decision to neglect a small $\varepsilon$ suffices, without stating what "small" is (p. 195).

A starred note says appendix *ix supersedes this. Almost all large samples give a hypothesis a strongly negative corroboration, which may be interpreted as falsification. Few samples are undecisive. Popper expects to refute a probabilistic hypothesis perhaps more confidently than a non-probabilistic one (p. 194, note *4).

**Objectivity and reproducibility.** *Objection:* even the greatest improbability is still a probability and will "some day happen". *Popper:* he does not deny improbable events may occur (e.g. gas molecules briefly withdrawing into part of a volume). But such events would not be physical effects, since they cannot be reproduced at will. A physicist observing one could not decide what happened or exclude an observational mistake (p. 195). If *reproducible* deviations from a deduced macro effect are found, the probability estimate must be taken as falsified (pp. 195–196).

Popper cites Eddington: "Some things never happen in the physical world because they are impossible; others because they are too improbable." (p. 196). He would prefer to avoid untestable claims about whether the extremely improbable occurs, but finds the formulation fits physicists' practice (p. 196).

**Fluctuations (e.g. Brownian movement).** Here $\pm\varphi$ is smaller than the characteristic $\Delta p$, so measurable deviations are highly probable. The fluctuation itself is a reproducible effect. Fluctuations beyond some $\Delta p$ must not be reproducible, nor long runs of fluctuations in one direction (p. 196).

**Summary (pp. 196–197).**
- Insofar as probability statements are not falsifiable, they are metaphysical and empirically empty. Insofar as they are used as empirical statements, they are used as falsifiable ones.
- Two tasks follow: explain this in terms of logical form (§66), and analyse the rules for using them as falsifiable statements.
- A rule can demand a minimum agreement between basic statements and the estimate. The dividing line need not be arbitrary or "tolerant". It can be set by attainable measurement precision.
- The rule does not forbid atypical segments or repeated deviations, which are typical of probability sequences. It forbids predictable, reproducible systematic deviations. It requires the best possible agreement for all reproducible, testable effects (p. 197).

> **Intuition note.** Strange runs of luck are allowed, but a "luck" that can be repeated on demand counts against the hypothesis. For large $n$ the cut-off hardly depends on how tiny "tiny" is, so one need not fix an exact $\varepsilon$.

### §69: Law and chance (pp. 198–200)
**Popper's view:** the difference between planets and dice lies in the fact that planetary motion has so far been predicted successfully and individual dice results have not. Prediction needs laws plus initial conditions. For dice, we lack sufficient knowledge of initial conditions, and the rules of dicing are chosen to prevent us from measuring them. These rules, with requirements such as true dice and good shaking, are the **frame conditions** (p. 198).

We can never say with finality that no laws exist in a field (this follows from the impossibility of verification). So chance is **subjective**: "chance" means our knowledge does not suffice for prediction (p. 198). A starred note says this is no concession to a subjective interpretation of probability (p. 198, note *1).

*The objective view,* as a metaphysical idea that events are or are not determined in themselves, is not examined here (p. 199). A starred note says that Popper later recommends such a metaphysical view in the Postscript (p. 199, note *2).

*A second objective view:* chance is encountered when probability estimates are corroborated, just as causal regularity is when law-based predictions are. Popper says the definition implicit in this view may not be altogether useless, but stresses that the concept so defined is not opposed to the concept of law; for this reason he called probability sequences chance-like (p. 199).
- A sequence will in general be chance-like if the frame conditions differ from the initial conditions (p. 199).
- He does not know whether chance-like sequences with wholly unpredictable elements exist (p. 199).
- That a sequence is chance-like does not imply its elements are unpredictable, nor "due to chance" in the subjective sense, nor that there are no laws (p. 199).

A starred note says Popper would now argue that no experiment can be repeated exactly, so that repetition of some aspects of results while others vary is no argument for objective fortuity. But there may be other arguments for it, and one, Landé's blade, is highly relevant (p. 199, note *3).

Nor does corroboration of probability estimates show the sequence is completely irregular. Chance-like sequences exist that are built by a mathematical rule (appendix iv). A Bernoulli distribution is no symptom of lawlessness. Success of probability predictions is only a symptom of the absence of simple laws in the *structure of the sequence*, not of its events. The assumption of freedom from after-effect, equivalent to the hypothesis that such simple laws cannot be found, is corroborated, and that is all (p. 200).

> **Intuition note.** In this section "chance" says something about what we know or can find, not about whether the world has laws. A regular-looking statistical pattern is compatible with fully lawful individual events.

### §70: Deducibility of macro laws from micro laws (pp. 200–202)
Popper criticises the doctrine that all observable events must be explained as macro events (averages or sums of micro events). He treats it as a metaphysical hardening of an unobjectionable rule: try to simplify or unify theories with such hypotheses (p. 200).

**Claim:** non-statistical hypotheses about micro events can never suffice to explain macro events. Hypothetical frequency estimates are also needed, since statistical conclusions come only from statistical premises. These estimates are independent hypotheses, never derivable from the micro laws. They are prohibitions concerning regularities in the large (pp. 200–201). Von Mises is cited: not even the smallest theorem of kinetic gas theory follows from classical physics without additional statistical assumptions (p. 201).

Deterministic laws need initial conditions to give predictions. So assumptions about the *statistical distribution of initial conditions* enter every such derivation (p. 201).

The frequency assumptions of theoretical physics are largely equal-chance hypotheses, but not self-evident or a priori. Classical, Bose–Einstein and Fermi–Dirac statistics combine special assumptions with equal chance differently, giving different reference sequences and primary properties (pp. 201–202). A starred note mentions critics (Jordan, Einstein). Popper replies that probabilistic conclusions need probabilistic premises, and that Jordan's examples support this (p. 201, note *1).

**Waterfall example.** In principle, given precise initial conditions, we could predict any group of molecules and deduce any one individual fluctuation of the waterfall. But we could not deduce the *recurring* statistical regularities, still less the overall distribution. For that we need statistical estimates, at least the assumption that certain initial conditions recur again and again for many groups of particles, which is a universal statement. A statistical result is obtained if, and only if, such specific statistical assumptions are made (p. 202).

### §71: Formally singular probability statements (pp. 202–205)
A probability statement is **formally singular** if it ascribes a probability to a single occurrence (e.g. "the probability of throwing five with the next throw of this die is 1/6"). Frequency theory as a rule regards such statements as not quite correct in formulation, since probabilities cannot be ascribed to single occurrences, only to infinite sequences. Popper makes such statements correct by definition (pp. 202–203). With $k\in\alpha$ ($k$ is an element of sequence $\alpha$):

$$ {}_\alpha P_k(\beta) = {}_\alpha F(\beta)\qquad (k\in\alpha) \tag{Definition} $$

The singular probability that $k$ has property $\beta$, given $k\in\alpha$, equals by definition the probability of $\beta$ in the reference sequence $\alpha$ (p. 203). Popper calls this "simple, almost obvious" and surprisingly useful, even for quantum theory (§§75–76) (p. 203).

**Reference class.**
- A formally singular statement is incomplete without a reference class, though it is often implicit (p. 203).
- An event may belong to several classes. A man's chance of dying in a period differs by age group or occupation. No general rule says which class to choose. The narrowest class is often most suitable if it is numerous enough for reasonable statistical extrapolation and corroborating evidence (p. 204).

**Dissolving a "paradox".** *Objection:* the probability of an event before it occurs (say 1/6) differs from its probability afterwards (1 or 0). *Popper:* this is mistaken. ${}_\alpha P_k(\beta)$ is the same before and after. What changes is that the information $k\in\beta$ (or $k\in\bar\beta$) lets us choose a new reference class. Then ${}_\beta P_k(\beta)=1$ and ${}_{\bar\beta} P_k(\beta)=0$. Statements about the outcome of a single occurrence do not change its probability. They may suggest another reference class (p. 204).

**Bridge to the subjective theory.** We may read formally singular probability as a degree of rational belief (following Keynes), provided belief is guided by an objective frequency statement. It then expresses all we know of the event, as an "indefinite prediction" (pp. 204–205). Popper does not object to this, as long as objective frequency statements are seen as fundamental because they alone are empirically testable. He rejects reading these statements as describing an objective state other than the statistical one, e.g. that the next throw is objectively both indeterminate and undetermined, something that as yet hangs undecided (a view discussed by Jeans, among others). Such readings import the metaphysical idea that nature is more or less "determined" (p. 205).

Starred notes record later changes. Popper now prefers a formal axiom system satisfied by the interpretations, regards most of §§71–72 as superseded, and believes probability theory can best be interpreted via propensities, though he still objects to saying it must be so interpreted and treats the propensity view as a conjecture about the world's structure (p. 205, notes *2–*3; p. 206, note *4).

> **Intuition note.** A "probability of this one event" is just the frequency of its reference class applied to that event. Learning the outcome does not alter that number; it only lets us choose a new reference class.

### §72: The theory of range (pp. 206–208)
From §34: a more falsifiable statement is logically more improbable, a less falsifiable one logically more probable. The less probable statement usually entails the more probable one. Bolzano, von Kries and Waismann tried to base the probability calculus on logical *range*, which coincides with logical probability (§37) (p. 206).

Waismann proposed measuring the ratios between ranges by corresponding relative frequencies. Popper thinks this is feasible and amounts to correlating frequencies with "indefinite predictions", as in §71 (p. 206). But:
- It works only after a frequency theory exists, and then the range theory is superfluous.
- It is still significant, because a comprehensive theory can bridge the subjective and objective views (pp. 206–207).

**Modification.** Waismann assumes that ranges which merely overlap (non-comparable statements) can be made comparable. Popper calls this assumption difficult and superfluous. In cases such as randomness, comparison of subclasses and comparison of frequencies lead to analogous results (p. 207). The sketch:

If $\gamma\subset\beta$, then

$$(k)\,[\,\mathrm{Fsb}(k\in\gamma)\ \ge\ \mathrm{Fsb}(k\in\beta)\,]\quad(\text{cf. §33}),$$

so the range of $(k\in\gamma)$ is smaller than or equal to that of $(k\in\beta)$. (The page refers to §33 for $\mathrm{Fsb}$; that section lies outside this part.) The ranges are equal only if some reference class $\alpha$ (possibly the universal class) obeys a "law of nature":

$$(x)\,\{[x\in(\alpha\cdot\beta)]\rightarrow(x\in\gamma)\}.$$

If no such law holds, so that randomness may be assumed, then, provided $\alpha$ is denumerable and acceptable as a reference sequence (p. 207–208):

$${}_\alpha F(\gamma) < {}_\alpha F(\beta).$$

So under randomness a comparison of ranges gives the same inequality as a comparison of frequencies. Hence frequencies may be correlated with ranges to make them measurable, which §71 did indirectly. One could infer immediately ${}_\alpha P_k(\gamma)<{}_\alpha P_k(\beta)$ (p. 208).

**Conclusion.** The apparently obdurate conflict between objective and subjective theories may be eliminated altogether by the "somewhat obvious" definition of formally singular probability (p. 208).

> **Intuition note.** A narrower claim ($\gamma\subset\beta$) cannot be more probable than the wider one. If nothing forces $\gamma$ to follow from $\beta$ (randomness), it is strictly less probable. Frequencies in a reference sequence then give the same ordering and can serve as a ruler for ranges.

## Toy example (ours, not from the text)
**Main idea: a small probability is never zero, so a rule is needed. Waiting makes any accident "expected" but not reproducible.**

Fair coin, $p=1/2$. Let the "effect" be a block of 10 heads, which has probability $(1/2)^{10}=1/1024\approx 0.00098$.
1. Never zero: $(1/2)^{20}=1/1{,}048{,}576\approx 9.5\times10^{-7}$ and $(1/2)^{30}\approx 9.3\times10^{-10}$. The probability shrinks fast but stays positive.
2. The "cosmic period" argument: with $N$ independent blocks, the chance of at least one all-heads block is $1-(1-1/1024)^N\approx 1-e^{-N/1024}$ (added step: approximation $\ln(1-x)\approx -x$).
   - For probability 0.5: $N\approx 1024\ln 2\approx 710$ blocks.
   - For probability 0.99: $N\approx 1024\ln 100\approx 1024\times 4.605\approx 4{,}716$ blocks.
   - So for any target below 1 there is a finite waiting length. Waiting long enough "explains" the run as an accident.
3. Popper's rule: if a student could produce a 10-head run on demand every time, that is a reproducible effect. It is not to be explained as accident, and the fair-coin hypothesis counts as falsified.
4. Formally singular probability: the die throw $k$ is in $\alpha$ = throws of this true die, and ${}_\alpha F(5)=1/6$. After seeing a five, use class $\beta$ = fives: ${}_\beta P_k(\beta)=1$. The value ${}_\alpha P_k(\beta)$ stays $1/6$.

## Concepts
- [[falsifiability]] — probability statements are not falsifiable in themselves; they are used as falsifiable ones through a rule (pp. 196–197)
- [[demarcation problem]] — the criterion classifies unrestricted probabilistic "explanation" as metaphysical (p. 190)
- [[corroboration]] — high negative corroboration of a large sample may be read as falsification (note *4, p. 194)
- [[deductive-nomological explanation]] — prediction needs laws plus initial conditions; here applied to dice vs planets (p. 198)
- [[existential-hypothesis]] (new) — a universalized existential statement: for every $x$ there is some $y$ with an observable property, where the occurrence of $y$ may be delayed without bound (p. 185)
- [[randomness-vs-uniqueness-requirement]] (new) — randomness links probability statements to basic statements; uniqueness lets them contradict each other (pp. 186–187)
- [[methodological-rule-neglect-extreme-improbability]] (new) — decision not to explain reproducible effects as accumulations of accidents (p. 192)
- [[reproducible-effect]] (new) — an effect that can be reproduced at will; an idea closely connected with objectivity, and improbable occurrences that are not reproducible at will are not physical effects (p. 195)
- [[formally-singular-probability]] (new) — ${}_\alpha P_k(\beta)={}_\alpha F(\beta)$, a single-case probability defined via a reference sequence (p. 203)
- [[reference-class]] (new) — the sequence $\alpha$ relative to which a single event's probability is defined (pp. 203–204)
- [[frame-conditions]] (new) — rules fixing the conditions of a random sequence, e.g. dicing rules (p. 198)
- [[logical-range]] (new) — logical probability of a statement, coinciding with its range (p. 206)

## Canonical instances
- [[law-of-gravity-as-cosmic-accident]] — probabilistic "explanation" of any regularity as metaphysics (p. 189)
- [[haldane-entropy-argument]] — the claim that the world will wind itself up again by accident; an example of unrestricted probabilistic speculation (p. 190, note *1)
- [[gas-pressure-bernoulli]] — macro effect derived from $n$ micro events; $\varepsilon$, $n$, $\Delta p$ (p. 193)
- [[brownian-movement]] — a fluctuation that is itself a reproducible effect (p. 196)
- [[dice-vs-planets]] — chance as lack of knowledge of initial conditions (p. 198)
- [[waterfall]] — individual fluctuations are deducible, recurring regularities need statistical assumptions (p. 202)
- [[mortality-reference-class]] — one man, different probabilities of dying by age or occupation group (p. 204)

## Bridges (candidates)
- [structural-analogy] Rule to neglect extreme improbability for reproducible effects ↔ statistics: rejecting a hypothesis when data fall in an extreme region — both treat very improbable data as counting against the hypothesis.
- [structural-analogy] Reference-class dependence of ${}_\alpha P_k(\beta)$ ↔ statistics: the reference-class problem — one case gets different probabilities from different groups.
- [structural-analogy] Waismann's frequencies as a measure of ranges ↔ measure theory: probability as a measure on sets — ordering of subclasses is preserved by the measure.
- [metaphor] Formally singular probability as "degree of rational belief" guided by frequency ↔ Bayesian epistemology: credence set by known frequency.

## Questions this raises
- If a probability hypothesis is falsified only by *reproducible* deviations, how should one treat a single dramatic, unrepeatable deviation?
- Does making "chance" subjective fit with the chance-like sequences that physics treats as objective? (Popper's starred notes later revise this.)
- Can the reference-class choice (§71) be settled without arbitrariness? Popper offers only the "narrowest, numerous enough" suggestion.
- How do the starred notes' later views (propensities, appendix *ix) change this chapter's argument?

## Reading notes
- This unit starts mid-§66 at p. 184. The section's title and opening are on earlier pages, outside this unit. It ends at the end of §72, p. 208, the last text on the page.
- Page offset: printed = pdf − 29.
- Notes marked with a star (*) read as later additions; several speak in the first person about what Popper now thinks. I summarise them as such.
- Page 188: the text layer says the analysis shows which reasons tell against the axiom of randomness and in favour of the requirement of uniqueness. The preceding argument speaks against the *convergence* axiom. No page image was available for p. 188, so I cannot tell whether this is a slip in the text or in the extraction.
- The notation for the $n$-segment probability is rendered ${}_{\alpha_n}F(\Delta p)$ following the p. 193 image, where a small $n$ sits beside $\alpha$. Fsb on p. 207 is as printed; the page refers the reader to §33, which is outside this part.
- Text layer problems are minor; no equation was unreadable.
