---
id: frank-2012-rsa/main
work: frank-2012-rsa
unit: paper
pages: 1-10
fields: [theory-of-mind]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 6
---
# Predicting pragmatic reasoning in language games

## L0 — One line
If a listener assumes the speaker picks words in proportion to how specific they are, and combines this with how salient each object is, Bayes' rule predicts people's guesses about what a word refers to.

## L1 — The gist (≤ 120 words)
How can we make precise, quantitative predictions about pragmatic inference, that is, how listeners get intended meaning from context? The authors use simple reference games with three objects. The speaker is modelled as informative: they favour words that apply to fewer objects. The listener inverts this model with Bayes' rule and multiplies by a measured prior, the salience of each object. Predictions fit mean human bets very closely (r = .98 for speaker choices, r = .99 for listener choices), with no fitted parameters. This matters because informal accounts of pragmatic inference have seldom yielded quantitative predictions; here the idea of an informative speaker is formalised and tested.

**Prerequisites:** Bayes' rule (prior, likelihood, normalisation); logarithms and exponentials; correlation coefficient r; the idea of expected utility.

## L2 — Key ideas (5–10 bullets)
- The listener infers the intended referent by Bayes' rule: prior salience × speaker likelihood, normalised over the objects in context (p. 2).
- The prior is "contextual salience", measured empirically because no a priori method exists to compute it (p. 2).
- Speakers are modelled as rational: utility is informativeness (negative surprisal) minus a cost. With constant cost and α = 1, and informativeness measured against a literal listener, this gives the "size principle": among the words that apply to the referent, speakers should choose words in proportion to 1/(number of objects each word fits) (pp. 2–3, 10).
- Three participant groups (speaker, salience, listener) test the likelihood and the posterior and measure the prior, separately (p. 3).
- Speaker bets match the model (r = .98). Salience and listener bets are not correlated with each other (r = .19, p = .40). Combined via the model, they predict listener bets (r = .99; .87 without 0 and 100 predictions) (p. 3).
- The authors call the fit parameter-free (p. 1). In the derivation the noise parameter is set to α = 1 and word cost is held constant, and the prior comes from the salience data (pp. 9–10).
- The authors claim the model synthesises earlier work on disambiguation, signalling games (game-theory models of a sender choosing signals for a receiver) and referring-expression generation (systems that produce phrases picking out objects) (pp. 3–4).

## L3 — Walkthrough

### Introduction (pp. 1–2)
- Language conveys information efficiently in context. Listeners can infer meaning by assuming utterances carry only relevant information. These inferences rely on a shared assumption that speakers are informative, "but not more so than is necessary" given common knowledge and the task (p. 1).
- Informal theories exist (Grice, Sperber & Wilson, Clark). The authors say there have been few quantitative predictions, perhaps because "informativeness" and "common knowledge" are hard to formalise (pp. 1–2).
- The online abstract says the close, parameter-free fit suggests information-theoretic tools "may lead to more effective formal models" (p. 1).
- The setting is referential games like those described by Wittgenstein. Participants see objects and bet on which one a word refers to (p. 2).

### The model (pp. 2–3)
The listener recovers the speaker's intended referent $r_S$ in context $C$ from the word $w$:

$$P(r_S\mid w,C)=\frac{P(w\mid r_S,C)\,P(r_S)}{\sum_{r'\in C}P(w\mid r',C)\,P(r')}\tag{1}$$

Three terms (p. 2):
- **Prior** $P(r_S)$: how likely an object is to be referred to. It is defined as contextual salience (perceptual, social and conversational), which captures shared common knowledge. It is measured empirically.
- **Likelihood** $P(w\mid r_S,C)$: how likely the speaker is to say $w$ for that object.
- **Normaliser**: the sum of the products over all referents in $C$.

The likelihood comes from a rational-actor speaker whose utility is defined by surprisal, a measure of how much a word reduces uncertainty about the referent. The authors derive that speakers should choose words in proportion to their specificity (p. 2):

$$P(w\mid r_S,C)=\frac{|w|^{-1}}{\sum_{w'\in W}|w'|^{-1}}\tag{2}$$

Here $|w|$ is the number of objects to which $w$ could apply. $W$ is the set of words that apply to the intended referent (p. 3).

*Intuition note:* A speaker who wants to point to one object prefers words that fit few objects, because those words leave the listener less doubt. The listener knows this. So, other things (such as salience) being equal, a broad word is better evidence for an object that had no narrower word available than for one that did (compare the toy example).

### Experiment and results (p. 3)
- Three groups saw sets of objects varying on two dimensions. The distribution of features was varied systematically, and other aspects were randomised per participant (p. 3).
  - **Speaker** group: bet on which word a speaker would use for a given object. This tests the likelihood.
  - **Salience** group: told that a speaker used an unknown word. They bet on which object was meant. This measures the prior.
  - **Listener** group: told the speaker used one word (e.g. "blue"). They bet on objects. This tests the posterior.
- Speaker bets vs. model: r = .98, p < .001 (p. 3).
- Salience and listener judgments were not correlated with each other: r = .19, p = .40. Combined through the model, the prediction correlated with listener judgments at r = .99, p < .0001. With predictions of 0 and 100 removed, r = .87, p < .0001 (p. 3).
- Fig. 1C works through one object arrangement: salience data (prior) × model likelihood → posterior, plotted against listener data (p. 6).
- The authors say the model synthesises earlier traditions. They conclude that combining information-theoretic informativeness with measured common knowledge captures "some of the richness" of pragmatic inference (pp. 3–4).

*Intuition note:* Salience data alone do not track listener bets (r = .19, not significant), but the model's product of salience and informativeness does (r = .99). The paper does not report a test of informativeness alone against listener bets (p. 3).

### Materials and methods (p. 9)
- 745 US participants on Mechanical Turk: 206 speaker, 276 salience, 263 listener. Only a participant's first trial was kept. Trials needed a passed manipulation check (a question confirming the participant noticed the relevant features) and bets summing to 100. The check asked, e.g., "How many objects are blue?" (p. 9).
- Each page showed three objects with colour, shape and texture features. Two dimensions varied and the third was held constant (p. 9).
- The manipulation was how many objects shared the target's value on each of the two dimensions. The notation is "# sharing feature 1 / # sharing feature 2". There are seven context types: 1/1, 1/2, 1/3, 2/2 (both features overlapping on two objects), 2/2 (both features overlapping on one object, shown in Fig. 1C), 2/3 and 3/3. The two 2/2 types were separated because the model predicts different results for them (p. 9).
- Fifty random trials were generated for each of the 6 numerical conditions in each group (p. 9).
- In the speaker condition the target was marked with a dotted line (p. 9).

### Supplementary model derivation (pp. 9–10)
Setting: a shared context $C=\{o_1,\dots,o_n\}$ and a shared vocabulary $V=\{w_1,\dots,w_m\}$. Each word's meaning is a Boolean function on objects (a rule giving true or false for each object) (p. 9).

The speaker chooses words in proportion to exponentiated expected utility (Bayesian decision theory: choosing actions by their expected utility under uncertainty):

$$P(w\mid r_S,C)\propto e^{\alpha U(w;r_S,C)}\tag{S1}$$

The noise parameter $\alpha$ measures the speaker's deviation from optimal choice. Setting $\alpha=1$ gives a standard Luce choice rule (each option chosen with probability proportional to its weight) (p. 9).

Utility is informativeness minus cost (p. 10):

$$U(w;r_S,C)=I(w;r_S,C)-D(w)\tag{S2}$$

$D(w)$ is assumed constant, because words were randomised and roughly matched for complexity. The authors note that in other settings cost may depend on length, frequency and so on, and that future work should study cost in interpretation (p. 10).

Informativeness is minus surprisal. Surprisal is $I_p(x)=-\log p(x)$. So $I(w;r_S,C)=-I_{\tilde w_C}(r_S)$, where $\tilde w_C$ is the distribution from a literal interpretation of $w$ in $C$ (p. 10). A literal listener gives zero probability to objects where $w$ is false and equal probability to the rest:

$$\tilde w_C(o)=\begin{cases}\frac{1}{|w|}&\text{if } w(o)=\text{true}\\0&\text{otherwise}\end{cases}\tag{S3}$$

Combining S1–S3 (p. 10):

$$P(w\mid r_S,C)=\frac{e^{-(-\log(|w|^{-1}))}}{\sum_{w'\in V\ \mathrm{st.}\ w'(r_S)=\mathrm{true}}e^{-(-\log(|w'|^{-1}))}}\tag{S4}$$

(added step) Since $e^{-(-\log x)}=x$, the numerator is $|w|^{-1}$. A cost $D(w)$ that is the same for all words gives the same factor $e^{-D}$ in numerator and every denominator term, so it cancels. S4 therefore equals Eq. 2, the "size principle" (p. 10).

Conclusion of the derivation: in these experiments, the speaker's abstract goal of being informative reduces to choosing a word that applies to the referent and picks out a relatively smaller part of the context. Listeners may use this speaker model as the likelihood in Eq. 1 (p. 10).

*Intuition note:* Under the paper's assumptions in these experiments (constant cost, α = 1, a literal listener), the speaker model reduces to the "size principle": prefer words that fit fewer objects (p. 10).

## Toy example (ours, not from the text)
Context of 3 objects: 1 = blue square, 2 = blue circle, 3 = green circle. Words: blue = {1,2} so $|w|=2$; green = {3} so 1; square = {1} so 1; circle = {2,3} so 2.

Listener hears "blue". Compute the likelihood $P(\text{blue}\mid o)$ with Eq. 2:
- Object 1: words true of it are blue (weight 1/2) and square (weight 1). $P=\frac{1/2}{1/2+1}=\frac13$.
- Object 2: words true are blue (1/2) and circle (1/2). $P=\frac{1/2}{1}=\frac12$.
- Object 3: "blue" is false, so $P=0$.

With a uniform prior of $\frac13$, the normaliser is $\frac13(\frac13+\frac12)=\frac5{18}$; the prior cancels. Posterior: object 1 = $\frac{1/3}{5/6}=0.4$, object 2 = $\frac{1/2}{5/6}=0.6$, object 3 = 0.

Interpretation: a speaker meaning the blue square could have said the more specific "square", so "blue" is slightly better evidence for the blue circle.

With a salience prior (0.6, 0.2, 0.2): unnormalised values are 0.6·(1/3) = 0.2, 0.2·(1/2) = 0.1, 0. They sum to 0.3, so the posterior is 2/3, 1/3, 0. Salience can reverse the preference.

## Concepts
- [[Rational Speech Act (RSA)]] — the paper's model has this structure (a speaker chosen by informativeness, a listener who inverts it with Bayes), though the paper does not use the name (canon link; not stated in this unit) (pp. 2, 10)
- [[literal listener / pragmatic speaker / pragmatic listener]] — (canon link; the paper says "literal interpretation", not these names) here the literal listener is $\tilde w_C$ (S3), the speaker is Eq. 2, and the listener is Eq. 1 (pp. 2, 10)
- [[Boltzmann (softmax) rationality]] — (canon link; the paper says "Luce choice rule", not this name) speaker choice ∝ $e^{\alpha U}$ (S1). $\alpha$ is the decision-noise parameter and is set to 1, a Luce choice rule (p. 9)
- [[rational-agent assumption / principle of efficiency]] — the speaker is a rational actor maximising utility (informativeness minus cost) (pp. 2, 10)
- [[referential-communication-game]] (new) — participants bet which object a word refers to, as in Wittgenstein's games (p. 2)
- [[contextual-salience]] (new) — prior probability that an object is referred to; it covers perceptual, social and conversational salience and is measured empirically (p. 2)
- [[surprisal]] (new) — $-\log p(x)$, how much information is gained by observing $x$; the measure of informativeness (p. 10)
- [[size-principle]] (new) — among words that apply to the referent, a speaker should choose words ∝ $|w|^{-1}$, so more specific words are likelier (pp. 3, 10)

## Canonical instances
- [[reference-game-three-objects]] — "blue" vs "circle" for the middle object; the 1/1…3/3 context types (pp. 7, 9)
- [[wittgenstein-language-game]] — the betting games are described as like those of Wittgenstein (p. 2)

## Bridges (candidates)
- [same-math] Speaker softmax $e^{\alpha U}$ with $\alpha=1$ ↔ theory of mind (canon): Boltzmann rationality — the same exponentiated-utility choice rule.
- [structural-analogy] Listener inferring the referent via Bayes ↔ theory of mind: inverse planning — both invert a rational-agent model to recover what the agent intended.
- [structural-analogy] Speaker informativeness via a literal listener ↔ theory of mind: recursive mindreading — the speaker reasons about how a listener would interpret a word.

## Questions this raises
- What happens to the fit if $\alpha\neq1$ or if word cost $D(w)$ is not constant? The authors only flag cost as future work (p. 10).
- The paper models a speaker who reasons about a literal listener. Would a more deeply nested model of listeners predict the data better?
- How would the model handle words with graded, not Boolean, meanings, or contexts with more than three objects?
- Why are salience and listener bets uncorrelated (r = .19), yet salience still matters once combined with informativeness?

## Reading notes
- Printed page = pdf page for pp. 1–6; the figure page (pdf 7) has no number. The supplement pages (pdf 8–10) print their own numbers "1", "2" and "3"; this digest cites them by pdf number (pp. 8–10).
- The page 7 image (Fig. 1) was not provided; I used only its text layer and the legend on p. 6. I did not check the plotted values.
- Counts are given in different places: the legend (p. 6) says N = 206 (speaker) and N = 263 (listener) for Fig. 1B. Fig. 1C uses N = 20 (salience) and N = 24 (listener) for one context type. Methods list 276 in the salience condition (p. 9).
- Minor typos in the source: "probability of a choosing a term" (p. 6); "measures of how much" (p. 10); S1 uses lowercase $r_s$ while the other equations use $r_S$.
- Page 5 ("Supplementary Text") is a heading only.
