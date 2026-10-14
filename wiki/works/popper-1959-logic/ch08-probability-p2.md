---
id: popper-1959-logic/ch08-probability-p2
work: popper-1959-logic
unit: "8 Probability (part 2/3): end of §57; §§58–65; start of §66"
pages: 158–183
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Probability, part 2: absolute freedom, Bernoulli's theorem, and the problem of decidability

## L0 — One line
Popper replaces von Mises's "no gambling system" axiom with the weaker "absolute freedom" (n-freedom for every n), derives the law of great numbers from it without a convergence axiom, and then faces the fact that probability statements are logically unfalsifiable.

## L1 — The gist (≤ 120 words)
Popper reworks von Mises's frequency theory of probability. He replaces the demand that no gambling system works with a weaker one, "absolute freedom", which lets one construct model sequences. From it he sketches a proof of the binomial formula for adjoining segments and derives Bernoulli's law of great numbers. He then drops the axiom of convergence, using "middle frequencies" and a uniqueness requirement. He argues that the subjective theory cannot interpret the law in terms of frequencies. Finally he notes that probability statements cannot be falsified, although physicists use them empirically. This threatens his demarcation criterion, and he says he will try to answer the problem by applying his own ideas.

**Prerequisites:** relative frequency and limits of sequences; binomial coefficients ${}^nC_m$; basic idea of independence of events; Popper's falsifiability criterion and demarcation criterion (from earlier chapters). Terms used below: *overlapping segments* of a sequence share elements, *adjoining segments* do not; a sequence is *$n$-free* (from after-effects) if its frequencies do not change when we select elements by the $n$ elements before them, and *absolutely free* if it is $n$-free for every $n$; a *middle frequency* is a point of accumulation of the relative frequencies; the *axiom of convergence* demands that frequency limits exist; *model sequences* are mathematical examples of such sequences.

## L2 — Key ideas (5–10 bullets)
- Estimates of frequencies, whether equal-chance or extrapolated from statistics, are hypotheses; nothing logically "derives" them from counted past cases (pp. 158–159).
- It may be impossible to show by an example that von Mises's axiom (no gambling system) is consistent, and Popper argues that it demands more than the theorems need. Popper replaces it with n-freedom for every n ("absolute freedom") (pp. 160–161).
- A sequence is chance-like iff its primary frequency limits are absolutely free. That limit is the objective probability (p. 163).
- From absolute freedom Popper sketches a proof of the third binomial formula for adjoining segments (Bernoulli's problem), in two steps (pp. 164–167).
- Bernoulli's theorem says disorder in the small gives stability in the large. The frequency theory can interpret it; Popper argues that the subjective theory cannot interpret it as the statistical law of great numbers (pp. 168–172).
- The theorem is not a trivial consequence of the axiom of convergence. Popper conjectures that it is independent of it, and he drops the axiom using "middle frequencies" plus a uniqueness requirement (pp. 173–179).
- This also resolves the "fundamental problem of the theory of chance": inference from irregularity in the small to regularity in the large is valid, provided the irregularity can be expressed as a hypothesis of freedom from after-effects (pp. 179–180).
- Probability statements are neither falsifiable nor verifiable, yet physics uses them. This is a problem for Popper's demarcation criterion, which he says he will try to answer by applying his own ideas (pp. 181–183).

## L3 — Walkthrough

### End of §57: kinds of frequency hypothesis (pp. 158–159)
- An **equal-chance hypothesis** says the probabilities of the various primary properties are equal. It is usually based on symmetry, e.g. the six faces of a die (p. 158).
- A **statistical extrapolation** carries known frequencies, such as mortality rates, over to unknown cases. It assumes that past trends stay nearly stable, at least in the period immediately ahead (p. 158).
- **Popper on inductivists:** they may confuse the hypothetical estimate with its empirical "source", the classifying and counting of past cases. Logically nothing is derived. What we advance is a non-verifiable conjecture that frequencies will stay constant (p. 158).
- Popper believes equal-chance estimates are often guided solely by reflections on the significance of symmetry and similar considerations. He gives little weight to questions about the "sources" of estimates (pp. 158–159).
- More important: every predictive frequency estimate, including one got by statistical extrapolation (and certainly all those about infinite empirical sequences), is pure conjecture. It always goes beyond what observations entitle us to affirm (p. 159).
- The distinction corresponds fairly well to "a priori" versus "a posteriori" probabilities. Popper avoids those terms because they are used in many senses (p. 159).

### §58 Examination of the axiom of randomness (pp. 159–163)
- Von Mises's axiom (the principle of the excluded gambling system) says that limits of frequencies in a collective are insensitive to any systematic selection. A gambling system counts as a systematic selection (pp. 159–160).
- **Superficial objection.** One selection picks the throws that come up five, and in it the frequency of fives obviously differs. So von Mises speaks of selections that are independent of the result of the throw in question. Popper says the attacks on this wording can be answered by stating the axiom without it (p. 160). The axiom then reads: limits are insensitive to ordinal selection (by position), to neighbourhood selection (by neighbouring elements), and to all combinations of the two that can be used as gambling systems (p. 160).
- **Deeper objection (Kamke).** It may be impossible to prove that collectives exist, i.e. that the class is not empty. An example would need a mathematical rule, but by definition no rule can exist for a collective, since any rule could serve as a gambling system. Popper says this criticism seems indeed unanswerable if all possible gambling systems are ruled out (pp. 160–161). Note *2 adds that it is answerable if any given denumerable set of gambling systems is to be ruled out (p. 161).
- **Too much demanded.** If we axiomatize, the axioms should be sufficient and, where possible, necessary. Excluding all selection systems is not needed for Bernoulli's theorem. It suffices to exclude selections according to arbitrary $n$-tuples of predecessors, i.e. that the sequence be **$n$-free from after-effects** for every $n$, "absolutely free" (p. 161).
- **Popper's proposal:** replace the excluded gambling system by absolute freedom, i.e. $n$-freedom for every $n$. Chance-like mathematical sequences are those that satisfy it. Not all gambling systems are excluded, so rules for constructing such sequences exist and the class is non-empty, hence consistent (p. 161; construction in appendix iv, not in this unit).
- It may seem odd to describe irregular sequences by strictly rule-bound ones. But if chance sequences are irregular, they are a fortiori not regular of one particular type, and absolute freedom excludes only one (important) type (p. 162).
- Three types of gambling system are implicitly excluded (p. 162):
  - normal ("pure") neighbourhood selections, i.e. by a constant characteristic of the neighbourhood;
  - normal ordinal selections of constant spacing (elements $k, n+k, 2n+k, \dots$);
  - many combinations of these.
- These are the systems that do not refer to an absolute first element. They are the "simple gambling systems" (p. 162).
- Only systems that use absolute distances from an initial element are not excluded. Footnote example: select all terms whose number is prime (pp. 162–163). Note *5 says "only" is correct only for predictive gambling systems (p. 162).
- Absolute freedom also seems to agree quite well with what most of us believe, namely that the next throw of a die does not depend on earlier ones. Shaking the die is meant to ensure that (p. 163).

> *Intuition note.* Von Mises ruled out every betting system, which seems to make it impossible to write down an example. Popper asks only for insensitivity to selection by the preceding elements ($n$ at a time, for every $n$). He says this is enough for Bernoulli's theorem, and that examples can now be built.

### §59 Chance-like sequences. Objective probability (p. 163)
- **Definition (Popper):** an event- or property-sequence, especially an alternative, is *chance-like* or *random* if and only if the limits of the frequencies of its primary properties are "absolutely free", i.e. insensitive to every selection based on the properties of any $n$-tuple of predecessors (p. 163).
- A frequency limit of a random sequence is its *objective probability*, written $F$. For a random sequence $\alpha$ with primary property $\beta$:
$$ {}_\alpha F(\beta) = {}_\alpha F'(\beta) $$
  ($F'$ is the frequency-limit symbol of earlier sections, not defined in these pages.) (p. 163)
- The next task is to show that this suffices for the main theorems, especially Bernoulli's. In §64 the definition is modified to avoid limits (p. 163).
- Note *1: Popper would now use "objective probability" more widely, covering all objective interpretations including the propensity interpretation. Here it is only an auxiliary concept (p. 163).

### §60 Bernoulli's problem (pp. 164–168)
- Formula (1) of §56 holds for finite sequences of *overlapping* segments $\alpha_{(n)}$, assuming $\alpha$ is at least $(n-1)$-free. The infinite analogue (2) holds under the same assumption (p. 164):
$$ {}_{\alpha_{(n)}}F''(m) = {}^nC_m\,p^m q^{n-m} \tag{1} $$
$$ {}_{\alpha_{(n)}}F'(m) = {}^nC_m\,p^m q^{n-m} \tag{2} $$
- Chance-like sequences are $n$-free for every $n$, so (2) applies to them for any $n$ (p. 164).
- Popper wants the **third binomial formula**, for *adjoining* segments $\alpha_n$ (p. 164):
$$ {}_{\alpha_n}F(m) = {}^nC_m\,p^m q^{n-m} \tag{3} $$
- (3) differs from (2) in two ways. It concerns adjoining, not overlapping, segments, and it uses $F$, not $F'$. So it also asserts that sequences of adjoining segments are themselves chance-like, since $F$ is defined only for chance-like sequences (p. 164).
- Von Mises's name for finding ${}_{\alpha_n}F(m)$ is **Bernoulli's problem** (p. 164). Assuming that $\alpha$ is chance-like suffices to derive (3). This is equivalent to showing that the special multiplication theorem holds for adjoining segments of a random sequence (p. 165).
- **Proof sketch** (Popper says it is only a sketch) (p. 165):
  - *Step order.* First show (2) also holds for $\alpha_n$. Then show $\alpha_n$ is absolutely free. The order cannot be reversed, because overlapping sequences $\alpha_{(n)}$ are not absolutely free; they are typical "sequences with after-effects" (p. 165).
  - *First step.* $\alpha_n$ is obtained from $\alpha_{(n)}$ by normal ordinal selection. So it suffices to show that the limits in $\alpha_{(n)}$ are insensitive to such selection, which yields (p. 165):
$$ {}_{\alpha_n}F'(m) = {}_{\alpha_{(n)}}F'(m) \tag{4} $$
  - Case $n=2$: show ${}_{\alpha_2}F'(m) = {}_{\alpha_{(2)}}F'(m)$ for $m\le 2$ (4a); generalization is "easy" (p. 165).
  - From $\alpha_{(2)}$ one can select exactly two distinct $\alpha_2$-sequences. (A) is the pairs 1,2; 3,4; 5,6;… and (B) is the pairs 2,3; 4,5; 6,7;… (p. 166).
  - Suppose the pair 0,0 occurs too often in (A) compared with the binomial formula. Then (B) must deviate in a complementary way, with 0,0 not often enough (p. 166).
  - Then in long segments of $\alpha$ the pair 0,0 would appear more often at some characteristic distances than at others. The more frequent distances are those that would obtain if the pairs belonged to one $\alpha_2$-sequence; the less frequent are those for both (p. 166).
  - That contradicts absolute freedom. By the second binomial formula, absolute freedom entails that the frequency of a particular sequence of length $n$ in any $\alpha_{(n)}$ depends only on its number of ones and zeros, not on their arrangement (p. 166). Footnote *2: such a distance pattern could found a simple gambling system, which absolute freedom excludes (p. 166).
  - *Second step.* Show the $\alpha_n$-sequences are absolutely free, again first for $\alpha_2$, and first only 1-free. Suppose (A) is not 1-free: after a segment 0,0, the segment 1,1 follows more often than the binomial formula gives (pp. 166–167).
  - Then (B) must deviate the opposite way. Otherwise the quadruple 0,0,1,1 would occur too often at some characteristic distances and not often enough at others. This is the same situation as before, hence incompatible with absolute freedom (p. 167).
  - Generalizing, the $\alpha_n$-sequences are $n$-free for every $n$, hence chance-like (p. 167).
- So $F'$ can be replaced by $F$ in (4), and (3) solves Bernoulli's problem (p. 167).
- Consequences (p. 167):
  - If $\alpha$ is absolutely free, $\alpha_{(n)}$ is insensitive to normal ordinal selection.
  - The same holds for $\alpha_n$, since $\alpha$ is identical with both $\alpha_{(1)}$ and $\alpha_1$.
  - Absolute freedom, i.e. insensitivity to a special neighbourhood selection, entails insensitivity to normal ordinal selection.
  - It then also entails insensitivity to any "pure" neighbourhood selection.
- It entails insensitivity to combinations of the two types (pp. 167–168). Note *3: "all" should be replaced by "all those … that might be used as gambling systems", a correction due to Wald in 1935 (p. 168).

> *Intuition note.* If some pair appeared more often in one of the two interleaved sub-sequences, it would show up at regular gaps in the original sequence. A gambler could exploit those gaps. Absolute freedom rules this out, so adjoining segments follow the same binomial law as overlapping ones.

### §61 The law of great numbers (Bernoulli's theorem) (pp. 168–171)
- The theorem is derived from (3) by arithmetic, assuming we may let $n\to\infty$. So it can be asserted only of infinite sequences, and only of absolutely free ones, since taking $n\to\infty$ needs $n$-freedom for every $n$ (p. 168).
- An $n$-segment has property $m$ if it contains exactly $m$ ones, so its relative frequency is $m/n$. It has property $\Delta p$ iff $\left|\frac{m}{n}-p\right|<\delta$, where $p={}_\alpha F(1)$ and $\delta>0$ is any small fraction. Otherwise it has $\overline{\Delta p}$ (p. 168).
- The theorem answers the value of ${}_{\alpha_n}F(\Delta p)$. Intuition suggests this rises monotonically with $n$ for fixed $\delta>0$ (p. 169). Bernoulli's proof uses the binomial formula and finds, for any fixed $\delta$, however small (p. 169):
$$ \lim_{n\to\infty}\, {}_{\alpha_n}F(\Delta p) = 1 \tag{61.1} $$
- This comes from transforming the third binomial formula (adjoining segments). The second formula (overlapping segments) would give by the same method (p. 169):
$$ \lim_{n\to\infty}\, {}_{\alpha_{(n)}}F'(\Delta p) = 1 \tag{61.2} $$
  valid for overlapping segments and normal ordinal selections from them, hence for sequences with after-effects (studied by Smoluchowski). Formula (61.2) yields (61.1) when non-overlapping, hence $n$-free, sequences are selected. It is a "variant" of Bernoulli's theorem, and what is said of the theorem applies to it mutatis mutandis (p. 169). (Numbering 61.1/61.2 is ours; the source numbers them (1), (2).)
- **In words.** Call a long finite segment of fixed length a *fair sample* iff its frequency of ones deviates from $p$ by no more than a freely chosen small fraction. The probability of chancing upon a fair sample approaches 1 as closely as we like if the segments are made long enough (pp. 169–170).
- **Frequency translation of "probability"** (it occurs twice in that sentence): the overwhelming majority of all sufficiently long finite segments are fair samples. The frequency $p$ is realized approximately in almost all sufficiently long segments. How $p$ is obtained is irrelevant here; it may be a hypothetical estimate (p. 170).
- Short segments often show large fluctuations. Longer ones mostly show smaller and smaller deviations. Great deviations become as rare as we like (p. 170).
- Taking a very long segment of a random sequence and counting, we get in the vast majority of cases a characteristic average frequency. The whole segment and almost all long sub-segments deviate only slightly from it, and shorter sub-segments deviate more, and more often. Popper calls this *quasi-convergent behaviour* or *statistical stability* (pp. 170–171). Note *2: Keynes suggested the name "Stability of Statistical Frequencies" (p. 171).
- Summary: disorder and randomness in the small, order and constancy in the great. This is what "law of great numbers" refers to (p. 171).

> *Intuition note.* Take a fair coin. Ten tosses can sometimes give 8 heads (about 4 times in 100). Ten thousand tosses almost never stray far from half. The theorem says that large deviations become rarer as segments grow.

### §62 Bernoulli's theorem and the interpretation of probability statements (pp. 171–172)
- The frequency theorist can translate "probability" consistently, in both occurrences (p. 171).
- **Subjective theorist** (probability = degree of rational belief): Popper grants that he is consistent when he reads the words about probability approaching 1 as meaning that it is almost certain. But Popper says he merely obscures his difficulties when he goes on to say that the relative frequency will deviate from its most probable value $p$ by less than a given amount. In Keynes's words, the proportion of occurrences will diverge from the most probable proportion by less than a given amount (pp. 171–172).
- **Popper's verdict:** translated fully, the sentence becomes "almost certain that the relative frequencies deviate from the value $p$ of the degree of rational belief by less than a given amount", which "seems to me complete nonsense" (p. 172). Relative frequencies can deviate only from relative frequencies. And $p$ must not get a new meaning after the deduction (p. 172). Footnote *1: Popper objects that $p$ is at one time a degree of rational belief and at another a frequency. He sees no reason why an empirical frequency should equal a degree of rational belief, or that a theorem could prove it (p. 172).
- Conclusion: the subjective theory cannot interpret Bernoulli's formula as the statistical law of great numbers. Statistical laws can be derived only within the frequency theory (p. 172). Note *2: Bernoulli's theorem can serve as a bridge from the propensity interpretation to statistics (p. 172).

### §63 Bernoulli's theorem and the problem of convergence (pp. 173–175)
- Popper finds his deduction epistemologically unsatisfactory because the role of the axiom of convergence is unclear. By restricting attention to sequences with frequency limits, he tacitly assumed such an axiom (p. 173).
- **Not trivial.** Von Mises has shown that some sequences satisfy the convergence axiom although Bernoulli's theorem fails for them. In them, segments of any length occur, with frequency close to 1, that deviate from $p$ to any extent; the limit exists only because the deviations cancel. Von Mises's example is the last digits of a six-figure table of square roots. So the axiom alone is insufficient, and absolute freedom cannot be dispensed with (p. 173).
- **Conjecture:** the law of great numbers may be independent of the convergence axiom. The first binomial formula holds for finite sequences, so no limit is used. It needs only that $\alpha$ be at least $(n-1)$-free. For the transition to the limit it is enough that $n$ can be made as large as we like (pp. 173–174).
- Hence Bernoulli's theorem is approximately true even for finite sequences that are $n$-free for sufficiently large $n$. The limit concept plays only a subordinate role. It extends relative frequency, defined first for finite classes, to indefinitely continuable sequences (p. 174).
- Bernoulli himself deduced his theorem in the classical theory, which has no convergence axiom. A limit-of-frequencies definition is only one possible interpretation of the classical formalism (p. 174).
- Popper will try to deduce the theorem from $n$-freedom alone and to show it holds even for sequences without frequency limits (p. 174). Note *1 (later): the doubt is still justified. Appendices show that randomness defined by "shortest random-like sequences" entails convergence. But Popper no longer agrees with the view implicit in the next sentence of the text, though he agrees with the remaining paragraphs (p. 174).
- **Epistemological stakes.** The "empirical fact" that chance-like empirical sequences are statistically stable is often taken as corroborating the law (p. 175).
  - *Inductivist-minded thinkers* treat it as a basic, irreducible law of nature and want to make it (e.g. as the convergence axiom) the basis of probability theory, which would become a natural science (p. 175).
  - *Popper* inclines to believe it is reducible to the chance-like character of the sequences, derivable from $n$-freedom. He sees Bernoulli's and Poisson's achievement in showing that this alleged fact of experience is a tautology: from disorder in the small, under a suitable $n$-freedom condition, order in the large follows logically (p. 175).
- If the deduction succeeds, the epistemological problem becomes one of axiomatic independence, a purely logical question. It would also explain why the convergence axiom works in practice (p. 175).

### §64 Elimination of the axiom of convergence; solution of the "fundamental problem" (pp. 176–180)
- So far limits only supplied a concept of relative frequency for infinite sequences, needed to define absolute freedom. Popper now removes the restriction to limit-sequences without replacing it by another (p. 176).
- **Point of accumulation:** a value $a$ such that after any given element there are elements within any given small distance of $a$ (p. 176). Relative frequencies lie between 0 and 1, so for every infinite alternative the sequence of relative frequencies has at least one such point, by the Bolzano–Weierstrass theorem (p. 176).
- Each point of accumulation of the relative-frequency sequence of $\alpha$ is a **middle frequency** of $\alpha$. If $\alpha$ has exactly one, it is the frequency limit. If it has no limit, it has more than one (pp. 176–177). Footnote 2: then the middle frequencies form a continuum (p. 177).
- We now estimate that $p$ is a middle frequency, and calculate with it analogously to limits, given "certain necessary precautions" (a stricter reading of "independent selection", footnote 3) (p. 177).
- **Difficulty:** middle frequencies are not unique. Postulating uniqueness at once would implicitly bring back the convergence axiom. Without it, probability would be ambiguous, since a sequence might have several absolutely free middle frequencies (appendix iv, section c). That is hardly acceptable (p. 177).
- **Solution:** introduce uniqueness as the last step, after postulating absolute freedom (p. 178).
- **Definition:** let $\alpha$ be an alternative with one or several middle frequencies. If its ones have one and only one middle frequency $p$ that is absolutely free, then $\alpha$ is chance-like and $p$ is the objective probability of the ones within $\alpha$ (p. 178). Two requirements (p. 178):
  1. *Randomness:* at least one absolutely free middle frequency, i.e. its objective probability $p$.
  2. *Uniqueness:* for one property of one chance-like alternative there is one and only one probability $p$.
- Consistency is ensured by the earlier example. Sequences exist with one and only one probability but no frequency limit (appendix iv, section b). So the new demands are less exacting than the old, which were (1), (2) and (2′) the *axiom of convergence*: no further middle frequency apart from $p$ (pp. 178–179).
- Bernoulli's theorem and all classical theorems follow. The formula and its interpretation are unchanged. In a chance-like sequence without a limit, almost all sufficiently long segments still deviate only slightly from $p$ (p. 179).
- Quasi-divergent segments, which deviate by any amount, do occur at times. But they are comparatively rare, because they must be compensated by extremely long stretches of quasi-convergent behaviour. By calculation these stretches are longer by several orders of magnitude, as it were (p. 179).
- **The fundamental problem of the theory of chance** (named in §49): the inference from unpredictable, irregular singular events to the applicability of the probability calculus is valid. The condition is that the irregularity be expressible, approximately, as the hypothesis that only one middle frequency occurs in any predecessor selection, so that no after-effects result (pp. 179–180). Under this assumption the law of great numbers is tautological (p. 180).
- It is not self-contradictory, as Feigl had asserted, to hold that in an irregular sequence a stability appears in very large sub-sequences. Model sequences show there is no incompatibility. Nor is it trivial, since it needs specific tools: Bolzano–Weierstrass, $n$-freedom, Bernoulli's theorem (p. 180).
- The apparent paradox, from ignorance to knowledge, disappears once the assumption of irregularity is put as a frequency hypothesis (freedom from after-effects). It must be put that way for the argument to be valid (p. 180).
- **Older theories.** The subjective theory can deduce Bernoulli's theorem but cannot interpret it in frequencies, so it cannot explain the statistical success of probability predictions. The older frequency theory postulates regularity in the large through the convergence axiom, so the problem does not arise there (p. 180).
- Conclusion: the axiom of convergence is not a necessary part of the foundations of the calculus (pp. 180–181). Footnote 7: Popper says he follows von Mises closely. The differences concern the limit axiom, replaced by uniqueness, and the randomness axiom, modified so that model sequences can be constructed. Kamke's objection is thereby met (p. 181).

> *Intuition note.* A sequence of frequencies can keep wandering and still be "predictable" in the sense that matters. Popper only needs one absolutely free middle frequency that is the unique one. Rare long stretches of odd behaviour are cancelled by far longer stretches of normal behaviour.

### §65 The problem of decidability (pp. 181–183)
- Popper turns back to methodological problems. As long as the binomial formula is derivable, probability statements are not falsifiable. They rule out nothing observable and cannot be contradicted by any finite number of basic statements or observations (p. 181).
- **Example:** we estimate that a coin gives "1" and "0" with equal frequency, ${}_\alpha F(1)={}_\alpha F(0)=\tfrac12$. Then "1" comes up every time. In practice we would abandon the estimate, but not by logical falsification: we observe only finite sequences. The binomial formula gives a very long segment with great deviations a tiny but always positive probability (p. 181).
- Even frequent occurrence of a deviating segment may be described as one occurrence of an even longer and more deviating one. So no finitely given sequence, and no finite $n$-tuple of basic statements, can falsify a probability statement (p. 182).
- Only an infinite sequence defined intensionally (by a rule) could contradict an estimate. So probability hypotheses are unfalsifiable because their dimension is infinite (cf. §§38, 43). Popper says they should therefore really be described as empirically uninformative, void of empirical content, though not void of logical content (§35, footnote 1) (p. 182).
- But that view is "clearly unacceptable" given the successes of physics with predictions from probability estimates (p. 182). A physicist can usually decide whether to accept a probability hypothesis as "empirically confirmed" or reject it as "practically falsified", i.e. useless for prediction (p. 182).
- Practical falsification needs a methodological decision to treat highly improbable events as ruled out. The questions follow: by what right, and where is the line drawn (p. 182)?
- Popper says the unfalsifiability and the empirical use together seem a "fatal blow" to his ideas on method, which depend on the demarcation criterion. He will try to answer by resolutely applying those ideas. First he must analyse the logical form of probability statements and their relations to basic statements (pp. 182–183).
- Note *1: emphasizing irrefutability was "healthy", because it exposed a problem not discussed earlier. His later reform (note *1 to §57) amounts to a methodological rule, like the one in §68, that makes probability hypotheses falsifiable. The problem then becomes how close an approximation to shortest random-like sequences is acceptable, a question of degree for mathematical statistics. A new solution by D. Gillies is added in 1972 (p. 183).

### §66 The logical form of probability statements (opening only, p. 183)
- Probability estimates are not falsifiable, and not verifiable either, for the same reasons as other hypotheses. No number of favourable results can finally establish that the frequency of heads is $\tfrac12$ and always will be (p. 183).
- So probability statements and basic statements neither contradict nor entail each other. Popper warns against two mistakes. One is to conclude that no logical relations hold between them. The other is to think that analysing these relations compels us to introduce a special probabilistic logic that "breaks the fetters" of classical logic (p. 183). The unit ends here.

## Toy example (ours, not from the text)
**Aim:** see Bernoulli's theorem and formula (3) with numbers. Take a fair coin sequence, $p=q=\tfrac12$, and $\delta=0.3$.

*Formula (3), $n=2$:* ${}^2C_0(\tfrac12)^2=\tfrac14$, ${}^2C_1(\tfrac12)^2=\tfrac24$, ${}^2C_2(\tfrac12)^2=\tfrac14$.

*Probability of property $\Delta p$ (deviation of $m/n$ from $0.5$ is $<0.3$):*
- $n=2$: $m/n\in\{0,0.5,1\}$. Only $m=1$ qualifies, so probability $=\tfrac{2}{4}=0.5$.
- $n=4$: $m/4$ is $0, 0.25, 0.5, 0.75, 1$. Deviation $<0.3$ for $m=1,2,3$. Counts are ${}^4C_1+{}^4C_2+{}^4C_3=4+6+4=14$, out of $2^4=16$. Probability $=0.875$.
- $n=10$: deviation $<0.3$ means $m/10>0.2$ and $<0.8$, so $m=3,\dots,7$. Counts are $120+210+252+210+120=912$, out of $1024$. Probability $=0.890625$.

These values rise towards 1, in line with formula (61.1), which says the probability tends to 1 as $n\to\infty$ for any fixed $\delta$.

*Overlapping versus adjoining:* for the sequence 0,1,1,0,1,… the overlapping pairs are 01, 11, 10, 01, …. Adjoining pairs are 01, 10, … (positions 1,2; 3,4). The overlapping pairs share elements and so are not independent; this is the kind of after-effect sequence mentioned in §60 (p. 165).

## Concepts
- [[chance-like-sequence]] (new) — a sequence whose primary frequency limits are absolutely free; Popper's replacement for von Mises's collective (p. 163)
- [[n-freedom-absolute-freedom]] (new) — frequencies insensitive to selection by any $n$-tuple of predecessors; absolute freedom means $n$-free for every $n$ (p. 161)
- [[excluded-gambling-system]] (new) — von Mises's axiom that no systematic selection changes the limits; Popper finds it too strong (pp. 159–161)
- [[objective-probability-frequency]] (new) — the frequency limit of a chance-like sequence; later its unique absolutely free middle frequency (pp. 163, 178)
- [[equal-chance-hypothesis]] (new) — hypothesis of equal probabilities, usually from symmetry (p. 158)
- [[bernoulli-law-of-great-numbers]] (new) — long segments of a random sequence are almost all fair samples; disorder in the small gives order in the large (pp. 169–171)
- [[middle-frequency]] (new) — a point of accumulation of the relative-frequency sequence; replaces the frequency limit (p. 176)
- [[axiom-of-convergence]] (new) — the demand that frequency limits exist; Popper shows it is not needed (p. 173)
- [[statistical-stability]] (new) — quasi-convergent behaviour of finite segments of random sequences (p. 171)
- [[fundamental-problem-of-chance]] (new) — validity of inferring regularity in the large from irregularity in the small (p. 179)
- [[falsifiability]] — Popper's criterion; probability statements fail it logically (p. 181)
- [[demarcation-problem]] — the criterion that the unfalsifiability of probability statements seems to threaten (p. 182)

## Canonical instances
- [[dice-equal-chance]] — symmetry of the cube as ground for an equal-chance hypothesis (p. 158)
- [[mortality-extrapolation]] — statistics extrapolated as a hypothesis, not derived (p. 158)
- [[von-mises-square-root-digits]] — last digits of a square-root table: convergent but not Bernoulli-stable (p. 173)
- [[brownian-movement-after-effects]] — Smoluchowski's theory built on overlapping, after-effect sequences (p. 165)
- [[coin-all-ones]] — a coin giving "1" repeatedly is practically, not logically, falsified (p. 181)

## Bridges (candidates)
- [structural-analogy] Absolute freedom (no predecessor-based system helps) ↔ probability theory: independence of successive trials — same intuition (next throw does not depend on earlier ones), though Popper's definition is frequency-based.
- [same-math] Middle frequency / point of accumulation (Bolzano–Weierstrass) ↔ real analysis: limit points of a bounded sequence — the same concept.
- [structural-analogy] Excluding gambling systems ↔ randomness tests in computer science: a sequence is random if no simple rule predicts it — loosely parallel.
- [structural-analogy] Practical falsification of probability hypotheses by a decision to treat improbable events as excluded ↔ statistics: rejection regions in hypothesis tests.

## Questions this raises
- Is "absolute freedom" really weaker than von Mises's axiom in every way that matters, or does it only look so because Popper restricts "gambling systems" to predecessor-based ones (cf. notes *3, *5)?
- If the law of great numbers is a "tautology" given $n$-freedom, what exactly does an empirical test of it test?
- Where should the line of "practical falsification" be drawn, and does a methodological decision there fit Popper's criterion of demarcation?
- Why can a frequency interpretation of $p$ be preserved in the theorem while a degree-of-belief reading cannot?

## Reading notes
- This unit starts mid-§57 (printed p. 158, the discussion of equal-chance hypotheses and statistical extrapolation) and ends mid-§66 (p. 183). §66 continues in the next part.
- Printed page numbers are given in the labels; no offset is needed (printed = pdf − 29).
- The text layer garbles formulas (subscripts such as ${}_{\alpha_{(n)}}F'$). I checked the images on pp. 163, 164, 165, 166, 167, 168, 169, 177 and 178. Equation labels (1)–(4a) in §60 and (1), (2) in §61 are the author's; I renumbered §61's as 61.1/61.2 to avoid clashes with §60.
- Footnotes marked * are, judging from the notes themselves (e.g. p. 160 note *1 on the German text; p. 183 "Added 1972"), later additions or translation remarks. I reported them as such.
- In §63, note *1 mentions a view implicit in the sentence that follows the note's marker; I take that to be the sentence about showing the result for sequences without frequency limits. This is my inference from where the marker stands.
- The source prints no exercises.
