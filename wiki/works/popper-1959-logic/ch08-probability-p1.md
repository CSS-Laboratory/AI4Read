---
id: popper-1959-logic/ch08-probability-p1
work: popper-1959-logic
unit: "8 Probability (part 1/3): sections 47–57 (to the start of the discussion of sources of frequency estimates)"
pages: 133–157
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
# Probability (part 1 of 3): interpretations, finite frequencies, n-freedom

## L0 — One line
Popper wants a consistent, objective frequency theory of probability whose relation to experience he also wants to clarify, and he begins it with finite classes, selection, n-freedom and the first binomial formula.

## L1 — The gist (≤ 120 words)
Popper asks how probability statements about events can get a consistent meaning, and how they can relate to experience although they are in principle impervious to strict falsification. He rejects subjective and logical readings, which he says make such statements non-empirical (tautologies). He chooses a modified frequency theory of von Mises's kind: he plans to eliminate the axiom of convergence (frequencies tend to a limit) and to weaken the axiom of randomness (no gambling system wins). This part builds the frequency calculus for finite classes, defines n-freedom (insensitivity to selection by predecessors), derives the first binomial formula, and begins on infinite sequences. It matters because physics uses probability without a consistent definition of it.

**Prerequisites:** sets and counting; ratios; binomial coefficients; the idea of a limit of a sequence; reading simple 0/1 sequences.

## L2 — Key ideas (5–10 bullets)
- Probability statements are central to physics, yet they cannot be strictly falsified. Popper turns this into a test of his methodology. He sets two tasks: new foundations for the calculus, and the decidability of probability statements (pp. 133–134).
- He sorts interpretations into subjective (psychological, or Keynes's logical one) and objective (frequency). He chooses the objective one chiefly because he believes only an objective theory can explain how probability is used in empirical science (pp. 135–137).
- The fundamental problem of the theory of chance: from the incalculability of single chance events we draw conclusions about frequencies that are brilliantly corroborated. The subjective theory dissolves the paradox but cannot explain this (p. 138).
- Von Mises defines probability as the limit of relative frequency in a "collective". A collective (a never-ending chance-like sequence) obeys an axiom of convergence (frequencies tend to a limit) and an axiom of randomness (no successful gambling system). Popper is inclined to blame convergence no less than randomness, and plans to eliminate convergence (pp. 139–142).
- For finite classes, relative frequency is a plain ratio (Definition 1). Independence means that selecting by one property leaves the frequency of the other property unchanged (pp. 144–146).
- A sequence is n-free if its frequencies are insensitive to selection by predecessor n-tuples. The impression of irregularity grows with n, and the repeating block (generating period) of an n-free 0/1 sequence with equal distribution has at least $2^{n+1}$ terms (pp. 148–152).
- Any finite alternative (a 0/1 sequence) that is at least (n−1)-free obeys the first binomial formula for the number of ones in its overlapping n-segments (blocks of n neighbouring terms, shifted by one step each time). This is the base for discussing randomness (pp. 153–154).
- Infinite sequences are tied to mathematical rules and limits. Frequency estimates for empirical sequences are hypotheses, and the calculus does not care where they come from (pp. 155–157).

## L3 — Walkthrough

### Chapter introduction (pp. 133–134)
- Scope: only the probability of events, as in games of chance and the probabilistic laws of physics. The "probability of hypotheses" is left to sections 79–85 ("Corroboration") (p. 133).
- Popper says probability plays a decisive part in modern physics, yet there is still no satisfactory, consistent definition of probability, which (he says) amounts to much the same as lacking a satisfactory axiom system. The relation between probability and experience also needs clarifying (p. 133).
- A stumbling block: probability statements are "in principle impervious to strict falsification". Popper says this will become a touchstone for testing his theory (p. 133).
- Two tasks (pp. 133–134):
  1. New foundations: a frequency theory along von Mises's lines, without the "axiom of convergence" (limit axiom) and with a somewhat weakened "axiom of randomness".
  2. Explain the relation between probability and experience: the problem of the *decidability of probability statements*.
- Footnote *1 (p. 134, later addition) lists three later changes. The first is a formal axiomatic calculus open to many interpretations. The second is a simplified frequency theory. The third is the propensity interpretation and a measure-theoretic formalism, developed in the Postscript.

### 47 The problem of interpreting probability statements (pp. 134–135)
- Numerical probability statements give a number. Example: the probability of throwing eleven with two true dice is 1/18 (p. 134).
- Non-numerical ones come in kinds. Saying it is very probable that mixing water and alcohol gives a homogeneous mixture might perhaps, suitably interpreted, be turned into a numerical statement (a probability very near to 1) (pp. 134–135).
- Saying that the discovery of a physical effect contradicting the quantum theory is highly improbable is a very different kind of statement. Popper believes it cannot be made numerical without distorting its meaning (p. 135).
- Numerical statements come first; non-numerical ones, which Popper thinks less important, come later. The question for each numerical statement is how to interpret it, especially its number (p. 135).

### 48 Subjective and objective interpretations (pp. 135–137)
- **Classical (Laplacean) definition:** probability = (number of favourable cases) / (number of equally possible cases). Popper says we might disregard the logical objection that "equally possible" is only another expression for "equally probable"; but even then he could hardly accept the definition as unambiguously applicable, since several interpretations are latent in it, which he classifies as subjective and objective (p. 135).
- **Subjective, psychologistic form:** probability measures feelings of certainty or doubt. Popper finds this tolerable for some non-numerical statements, but not very satisfactory for numerical ones (pp. 135–136).
- **Logical variant (Keynes is the principal exponent):** probability is a logical relation between statements, "logical proximity". If p follows from q, q "gives" p probability 1. If p and q contradict, q gives p probability 0. In between, roughly speaking, the numerical probability of p given q is greater the less p's content goes beyond what q already contains. Keynes defines probability as the degree of rational belief (the amount of trust proper to give p in the light of q). Popper counts this as a variant of the subjective view (p. 136 and fn *1).
- **Objective (frequency) interpretation:** every numerical probability statement is about the relative frequency of an event type in a sequence of occurrences. On this view, the statement that the next throw with this die being a five has probability 1/6 is really about a whole class of throws. It says only that the relative frequency of fives in that class is 1/6. Numerical statements without a frequency interpretation, and non-numerical ones, are usually shunned by frequency theorists (p. 137).
- **Popper's choice:** a modified frequency theory, "chiefly because I believe that only an objective theory can explain the application of the probability calculus within empirical science" (p. 137).
- Popper grants that the subjective theory gives a consistent solution to deciding probability statements and meets fewer logical difficulties. But its solution is that such statements are non-empirical, tautologies, which he calls "utterly unacceptable" given physics's use of probability (p. 137).
- He rejects the variant that derives objective frequency statements from subjective assumptions with Bernoulli's theorem as a "bridge". He regards it as logically unrealizable. A later footnote adds that Bernoulli's theorem may serve as a bridge inside an objective theory, from propensities to statistics (p. 137, fns 6 and *).

*Intuition note.* Is a probability of 1/6 about this throw or about a class of throws? The frequency theory says the class. Popper prefers this kind of theory chiefly because he believes only an objective theory can explain how probability is used in empirical science. The subjective readings make it about our belief or about logical relations.

### 49 The fundamental problem of the theory of chance (pp. 138–139)
- Chance-like or random events seem to show a peculiar kind of incalculability: after many failed attempts we are disposed to believe that all known rational prediction methods fail for them. Yet this incalculability is what leads us to apply the probability calculus (p. 138).
- The paradox, from incalculability to calculability, disappears on the subjective theory. But then the calculus is no method of calculating predictions. It only transforms what we already know, or rather do not know, logically (p. 138).
- This does not explain how a statement of ignorance, read as a frequency statement, can be empirically tested and corroborated. Popper calls this the **fundamental problem of the theory of chance** (p. 138).
- Even the frequency theory has not solved it. Popper says it is tied to the axiom of convergence (section 67). He claims a solution is possible inside the frequency theory once that axiom is eliminated. It will come from analysing the assumptions that let us argue from irregular single occurrences to stable frequencies (pp. 138–139).

### 50 The frequency theory of von Mises (pp. 139–141)
- The calculus of probability is a theory of chance-like sequences of repeatable events. Two axioms define them: the axiom of convergence and the axiom of randomness. A sequence satisfying both is a **collective** (p. 139).
- **Relative frequency sequence.** For a property (say "five"), divide the number of throws with it up to each element by that element's ordinal number. The result is a *frequency sequence*, distinct from the *event* or *property sequence* (pp. 139–140).
- **Example of an "alternative"** (two properties only; heads = 1, tails = 0) (p. 140):
  - Event sequence (A): 0 1 1 0 0 0 1 1 1 0 1 0 1 0 …
  - Frequency sequence (A′), for property 1: 0/1, 1/2, 2/3, 2/4, 2/5, 2/6, 3/7, 4/8, 5/9, 5/10, 6/11, 6/12, 7/13, 7/14 … (first term, here 0/1, is garbled in the text layer; see Reading notes).
  - The sequence for 0 is complementary (terms add to 1), so one sequence suffices (fn 2).
- **Axiom of convergence:** as the event sequence lengthens, the frequency sequence tends to a definite limit. Von Mises needs one fixed value to work with, even though actual frequencies fluctuate. The limits for all properties together give the *distribution* (p. 140).
- **Axiom of randomness** (the "principle of excluded gambling system"): no gambling system can be successfully applied. For any rule that selects supposedly favourable tosses, the relative frequencies in the selected sub-sequence approach the same limit as in the whole sequence, if play goes on long enough. A sequence with a profitable gambling system is not a collective (pp. 140–141).
- **Probability** for von Mises is another term for the limit of relative frequency in a collective. It is therefore applicable only to sequences of events, a restriction likely to be quite unacceptable from a point of view such as Keynes's. Von Mises answered critics that a scientific term need not match inexact pre-scientific usage (p. 141).
- **Task of the calculus:** to infer "derived collectives" with derived distributions from given "initial collectives", that is, to calculate probabilities which are not given from those which are (p. 141).
- Von Mises's four distinctive points: the collective comes before probability; probability is the limit of relative frequencies; there is an axiom of randomness; the task of the calculus is defined as above (p. 141).

*Intuition note.* A collective is a never-ending sequence in which each property's frequency settles down (convergence) and no selection rule can beat the average (randomness). Probability is then just that settled-down value.

### 51 Plan for a new theory of probability (pp. 141–143)
- **Objection to combining the axioms (fn 1 cites Waismann).** A limit is a property of the mathematical rule that determines a sequence. Applying it to a sequence that by the randomness axiom may follow no mathematical rule seems inadmissible (p. 142).
- Proposals: keep only convergence and drop randomness (Kamke) or replace it by a weaker requirement (Reichenbach). These assume randomness is the culprit (p. 142).
- **Popper's view:** he is inclined to blame the axiom of convergence no less than the axiom of randomness. Two tasks: (i) improve the axiom of randomness, mainly mathematical; (ii) eliminate the axiom of convergence completely, which is the epistemologist's concern (cf. section 66) (p. 142).
- **Mathematical aim:** derive Bernoulli's theorem (the first Law of Great Numbers) from a randomness axiom modified to demand no more than needed. More precisely, derive the Binomial Formula in its "third form". Bernoulli's theorem and the other limit theorems follow from it in the usual way (pp. 142–143).
- **Plan** (p. 143):
  1. A frequency theory for finite classes, up to the first Binomial Formula. It is elementary class theory, built to give a basis for discussing randomness.
  2. Infinite sequences, using the old convergence axiom provisionally, then Bernoulli's theorem.
  3. How the convergence axiom might be eliminated, and what axiom system remains.
- **Symbols:** $F''$ = relative frequency in finite classes; $F'$ = limit of relative frequencies of an infinite frequency sequence; $F$ = objective probability, i.e. relative frequency in an "irregular", "random" or "chance-like" sequence (p. 143).
- Footnote 2 (p. 142, later): the two tasks were satisfactorily completed only in appendix *vi.

### 52 Relative frequency within a finite class (pp. 143–145)
- **Terms.** A finite, non-empty class $\alpha$ is the *reference-class*, e.g. yesterday's throws with this die. $N(\alpha)$ is the number of its elements. $\beta$ is the *property-class*, finite or not, e.g. all throws showing five. The *product-class* $\alpha.\beta$ holds the elements in both. It is a subclass of $\alpha$, so finite (possibly empty) (pp. 143–144).
- **Definition 1** (p. 144):
$$ {}_{\alpha}F''(\beta)=\frac{N(\alpha.\beta)}{N(\alpha)} \tag{Def. 1}$$
  Read: the $\alpha$-frequency of $\beta$.
- Popper calls the definition "rather trivial". Footnote *1 says it is related to the classical definition but differs: no assumption that the elements of $\alpha$ are "equally possible".
- The theorems of the finite frequency calculus follow easily: the general multiplication theorem, the addition theorem and the division theorems (Bayes's rules, appendix ii). The theorems contain only relative frequencies (ratios), never cardinal numbers $N$. The $N$ appear only in the proofs of a few fundamental theorems derived directly from the definition (p. 144).
- **Example** (p. 145). Let $\bar\beta$ be the complement of $\beta$. Then
$$ {}_{\alpha}F''(\beta)+{}_{\alpha}F''(\bar\beta)=1 .$$
  Proof: from Definition 1 and the class theorem $N(\alpha.\beta)+N(\alpha.\bar\beta)=N(\alpha)$ (dividing both sides by $N(\alpha)$, an added step).
- Footnote *2 (p. 144): choosing a set of F-formulae from which the others derive gives a formal axiom system (appendices ii, *ii, *iv, *v).

### 53 Selection, independence, insensitiveness, irrelevance (pp. 145–146)
- **Selection.** Take $\alpha$ (buttons in a box), $\beta$ (red) and $\gamma$ (large). The product-class $\alpha.\beta$ is a new reference-class: the selection from $\alpha$ according to $\beta$. One can ask for ${}_{\alpha.\beta}F''(\gamma)$ (p. 145; answer from the division theorem, fn 2).
- **Independence (Hausdorff).** If
$$ {}_{\alpha.\beta}F''(\gamma)={}_{\alpha}F''(\gamma),$$
  then $\beta$ and $\gamma$ are *mutually independent within $\alpha$*. The relation has three terms and is symmetrical in $\beta$ and $\gamma$. Equivalent wording: $\gamma$ is *insensitive* to selection of $\beta$-elements within $\alpha$ (pp. 145–146).
- **Subjective reading.** If independent, learning that an element has $\beta$ is *irrelevant* to whether it has $\gamma$. If $\gamma$ is more (or less) frequent in $\alpha.\beta$, the information is *relevant* (p. 146).
- Footnote 4: Popper originally claimed triple symmetry (in $\alpha$, $\beta$, $\gamma$) if $\beta$ and $\gamma$ are finite. In a later note he says the condition is insufficient. He says he may have intended the condition that $\beta$ and $\gamma$ are bounded by the finite $\alpha$, or, most likely, that $\alpha$ should be the finite universe of discourse; he notes these are sufficient conditions. His counter-example uses 5 buttons: 4 round ($\alpha$); 2 round and black; 2 round and large; 1 round, black and large; 1 square, black and large. (Added check, not in the footnote, reading the counts inclusively: within the round buttons, black ($\beta$) and large ($\gamma$) are independent, ${}_{\alpha.\beta}F''(\gamma)=1/2={}_{\alpha}F''(\gamma)$.) But ${}_{\alpha}F''(\gamma)\neq{}_{\beta}F''(\gamma)$ (the footnote asserts this; added check: among the 3 black buttons, 2 are large, so ${}_{\beta}F''(\gamma)=2/3$).
- Footnote *1: information about properties is relevant iff the properties are dependent, and irrelevant iff independent. Relevance can be defined from dependence, but not the reverse. Footnote 5: the subjective theory cannot define objective independence, which Popper calls a serious objection (see the Postscript).

### 54 Finite sequences: ordinal selection and neighbourhood selection (p. 147)
- Number the elements of finite $\alpha$ and arrange them in a sequence. Two selections matter (p. 147):
  - **Ordinal selection:** by a property depending on ordinal number (e.g. "even"). The chosen elements form a *selected sub-sequence*.
  - **Neighbourhood selection:** by properties of neighbours, e.g. elements whose immediate predecessor, or first and second predecessors, or second successor, have property $\gamma$.
- **Primary properties** (heads, tails) belong to an element independently of position. **Secondary properties** ("even", "successor of tails") come from position (p. 147).
- An *alternative* is a sequence with two primary properties, written as 1s and 0s. Von Mises showed (with care) that the essentials of probability theory can be developed for alternatives without loss of generality. The structure of an alternative can be regular or more or less irregular (pp. 147–148). Footnote *1 (p. 148) suggests skipping sections 55–64 (or 56–64) at first reading, or turning to chapter 10.

### 55 N-freedom in finite sequences (pp. 148–152)
- **Worked example.** Let $\alpha$ be 1000 terms: 1 1 0 0 1 1 0 0 … It has equal distribution (p. 148):
$$ {}_{\alpha}F''(1)={}_{\alpha}F''(0)=\tfrac12 \tag{1}$$
- Select the elements with $\beta$ = "immediately succeeding a one". The selection $\alpha.\beta$ is 1 0 1 0 1 0 … Frequencies are unchanged (p. 148):
$$ {}_{\alpha.\beta}F''(1)={}_{\alpha}F''(1);\qquad {}_{\alpha.\beta}F''(0)={}_{\alpha}F''(0) \tag{2}$$
  So $\alpha$ is insensitive to selection according to $\beta$.
- Selecting $\bar\beta$ (successor of a zero) gives 0 1 0 1 0 … This begins and ends with 0. With 2000 elements it has 500 zeros and 499 ones. Such end-deviations come only from first or last elements, can be made as small as we please, and vanish for infinite sequences. They are neglected. So $\alpha$ is insensitive to selection by *every* immediate predecessor property (p. 149).
- The insensitivity depends on the structure of $\alpha$. The sub-sequences $\alpha.\beta$ and $\alpha.\bar\beta$ are *not* insensitive to selection by predecessor (p. 149).
- **Pairs of predecessors.** Selecting successors of any of the pairs 1,1; 1,0; 0,1; 0,0 never gives equal distribution. Each selected sub-sequence is an uninterrupted block of one symbol. So $\alpha$ is not insensitive to pairs (p. 149).
- **Subjective gloss.** One predecessor is irrelevant, but a pair is of highest relevance. Given the law constructing $\alpha$, the pair supplies the "initial conditions" for deducing the element. One predecessor is irrelevant only because it is not composite enough to serve as an initial condition (p. 150). Footnote *1: it is surprising that $p$ and $q$ can each be irrelevant while $p.q$ is highly relevant. Popper calls "relevant/irrelevant" "grossly misleading".
- **Terminology** (causality is closely tied to deducing predictions): "insensitive to selection by a single predecessor" becomes "free from after-effect of single predecessors", or *1-free*. Likewise *2-free* for pairs (p. 150).
- **n-freedom** (p. 151). A sequence is *n-free* if and only if its relative frequencies of primary properties are n-insensitive, i.e. insensitive to selection according to single predecessors, pairs, triplets, … and $n$-tuples of predecessors. Footnote 1 (Dr. Schiff): it suffices to demand insensitivity to selection by any predecessor $n$-tuple for the given $n$. Insensitivity for shorter tuples then follows.
- **Generating periods, equal distribution** (p. 151):
  - (A) 1 1 0 0 — repeated, gives a 1-free alternative.
  - (B) 1 0 1 1 1 0 0 0 — 2-free.
  - (C) 1 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 — 3-free.
  - (D) 0 1 1 0 0 0 1 1 1 0 1 0 1 0 0 1 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 1 — 4-free.
  - Popper: the impression of irregularity grows with $n$.
- **Length.** The generating period of an $n$-free alternative with equal distribution has at least $2^{n+1}$ elements (the periods above have 4, 8, 16, 32). Periods may start elsewhere, e.g. (C′) 1 0 0 0 0 1 1 1 1 0 1 0 0 1 0 1 …, and other transformations preserve $n$-freedom. A method for every $n$ will be described elsewhere (fn *3; see appendix iv) (p. 152).
- Adding the first $n$ elements of the next period gives length $2^{n+1}+n$. Every possible $(n+1)$-tuple of 0s and 1s then occurs in it at least once (p. 152).
- Footnote *4 (p. 152, later): for a long finite equidistributed alternative $A$ of length $N$, let $n$ be the greatest integer with $2^{n+1}\le N$. $A$ is *perfectly random* if and only if the relative number of occurrences of any $m$-tuplet ($m\le n$) deviates from that of any other $m$-tuplet by not more than, say, $m/N^{1/2}$. Popper says this definition "seems appropriate". This also allows "approximately random" and degrees of approximation.
- Footnote *2 (p. 150) on priority: the neighbourhood-size idea and the recursive 1-, 2-, … $n$-freedom are Popper's. The term "free from after-effect" is Reichenbach's, used then in an absolute sense ("any preceding group"). An "Added 1968" note says Smoluchowski used the term earlier.

*Intuition note.* "n-free" means: knowing the last $n$ results does not change the frequency of what comes next. Higher $n$ needs a longer generating period (at least $2^{n+1}$ for equal distribution), and the impression of irregularity grows with $n$.

### 56 Sequences of segments: the first form of the binomial formula (pp. 152–154)
- An *$n$-segment* of $\alpha$ is a sub-sequence of $n$ consecutive elements. The *overlapping* $n$-segments, written $\alpha_{(n)}$, have as $x$th element the segment of elements $x$ to $x+n-1$. Consecutive segments share $n-1$ elements. *Adjoining* $n$-segments (written $\alpha_n$) follow each other without overlap, e.g. elements 1 to $n$, then $n+1$ to $2n$, …, or starting from the $k$th element (pp. 152–153).
- The primary property of a segment can be taken as $m$, its number of ones ($m\le n$). Choosing a particular $m$ gives an alternative: "$m$" versus "non-$m$" (p. 153).
- **Setting.** Let $\alpha$ be a finite alternative with ${}_{\alpha}F''(1)=p$ and ${}_{\alpha}F''(0)=q$. Equal distribution is not assumed ($p=q$ is not required). Let $\alpha$ be at least $(n-1)$-free (pp. 153–154).
- **Result (first form of the binomial formula)**, proof in appendix iii (p. 154):
$$ {}_{\alpha_{(n)}}F''(m)={}^{n}C_{m}\,p^{m}q^{\,n-m}\tag{1}$$
  Only the $(n-1)$-freedom is assumed. It is settled "by elementary arithmetic". Newton gave the right-hand side in another connection.
- Footnote 1: the same problem for infinite sequences of adjoining segments is "Bernoulli's problem"; for overlapping segments, "the quasi-Bernoulli problem". The present problem is the quasi-Bernoulli problem for finite sequences. Popper now leaves finite reference-classes. The formula is the foundation for discussing the axiom of randomness (p. 154).
- ${}^{n}C_{m}$ is the binomial coefficient, the number of ways to choose $m$ places out of $n$ (added gloss).

*Intuition note.* In an (n−1)-free sequence, the pattern of ones in short windows follows the same formula as for $n$ independent tosses with chances $p$ and $q$ (added gloss). Popper assumes nothing beyond $(n-1)$-freedom (and the frequencies $p$ and $q$) and settles the question by elementary arithmetic.

### 57 Infinite sequences: hypothetical estimates of frequency (pp. 154–157)
- Results for $n$-free finite sequences extend easily to infinite $n$-free sequences defined by a generating period. An infinite *reference-sequence* more or less corresponds to von Mises's collective (pp. 154–155).
- $n$-freedom presupposes relative frequency. For infinite sequences Popper uses, *provisionally up to section 64*, the limit $F'$ in place of $F''$. This causes no problem for sequences built by a mathematical rule, since one can always decide whether their frequency sequence converges. Trouble comes only for sequences given by an empirical rule (e.g. linked to coin tosses), where the limit is not defined (cf. section 51) (p. 155).
- Footnote *1 (p. 155, later): Popper did not fully carry out his intuitive programme. He meant to analyse randomness within finite sequences first, then go to infinite ones in a theory where the existence of limits follows from randomness. He says this would have been easy, using shortest $n$-free sequences with growing $n$ (old appendix iv, new appendix *vi). Limits would then become demonstrable. Under a propensity interpretation these improvements become unnecessary, except as a way to define an ideal standard of objective disorder. Even then, speaking of frequency hypotheses and their statistical tests remains necessary, so the section stays relevant.
- **Mathematical sequence:** one defined by a mathematical rule. Example: the $n$th element is 0 iff $n$ is divisible by four. This gives 1 1 1 0 1 1 1 0 …, with ${}_{\alpha}F'(1)=3/4$ and ${}_{\alpha}F'(0)=1/4$ (p. 156).
- **Empirical sequence:** defined by an empirical rule, e.g. the $n$th element is 0 iff the $n$th toss of coin $c$ shows tails. Empirical rules need not give random sequences. For example, "the $n$th element is 1 iff the pendulum $p$ is to the left of a mark at the $n$th second" is also empirical (p. 156).
- Sometimes an empirical rule can be replaced by a mathematical one, using hypotheses and measurements about the pendulum. The mathematical sequence then approximates the empirical one to a degree of precision that may or may not suit our purposes. Of particular interest is obtaining a mathematical sequence whose frequencies approximate those of an empirical one (p. 156).
- The mathematical/empirical split is *intensional* (by the construction rule), not *extensional* (by listing elements). From a finite segment, however long, one cannot tell which kind the sequence is. Only a rule decides (p. 156).
- Because limits are used, only mathematical sequences with convergent frequency sequences are considered. Popper says this restriction amounts to introducing an axiom of convergence; its problems come in sections 63–66 (pp. 156–157).
- Within these, only those mathematical sequences are of interest which we expect or conjecture to approximate, in frequencies, empirical chance-like sequences. To expect this is nothing else than to frame a *hypothesis* about the empirical sequence's frequencies (p. 157). Decidability of such hypotheses (testable? falsifiable?) comes in sections 65–68 (fn 1).
- That estimates are hypotheses does not affect calculation. In finite classes, the starting frequencies may come from counting, a rule, a hypothesis, or invention. The calculus takes some frequencies as given and derives others. The same holds for infinite sequences. The "sources" of the estimates are not a problem *of the calculus*, but will still be discussed (p. 157).
- Two main sources of hypothetical frequency estimates for infinite empirical sequences: an *equal-chance (equiprobability) hypothesis*, and *extrapolation of statistical findings* (p. 157). The unit breaks off here.

## Toy example (ours, not from the text)
Take the 16-term alternative $\alpha$ = 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 (the pattern of Popper's example, p. 148).

1. Definition 1: ${}_{\alpha}F''(1)=N(\alpha.1)/N(\alpha)=8/16=1/2$.
2. Select successors of a 1. The predecessor 1s sit at positions 1, 2, 5, 6, 9, 10, 13, 14. Their successors (positions 2, 3, 6, 7, 10, 11, 14, 15) hold 1, 0, 1, 0, 1, 0, 1, 0. So ${}_{\alpha.\beta}F''(1)=4/8=1/2={}_{\alpha}F''(1)$. This is insensitivity to a single predecessor (1-free).
3. Select successors of the pair 1,1. The pairs sit at positions (1,2), (5,6), (9,10), (13,14). The successors at 3, 7, 11, 15 are all 0. So ${}_{\alpha.\beta}F''(1)=0/4=0\neq 1/2$. Not 2-free. A gambler who bets "0" after each 1,1 always wins, which is exactly what a random sequence should forbid.
4. Binomial formula with $n=2$ (needs at least 1-free; $p=q=1/2$). The overlapping 2-segments in one period are 11, 10, 00, 01, with $m=2,1,0,1$ ones. Observed frequencies: $m=1$: $2/4=1/2$; $m=2$: $1/4$; $m=0$: $1/4$. The formula gives ${}^{2}C_{1}\cdot\tfrac12\cdot\tfrac12=2\cdot\tfrac14=\tfrac12$; ${}^{2}C_{2}(\tfrac12)^2=\tfrac14$; ${}^{2}C_{0}(\tfrac12)^2=\tfrac14$. They match (end effects over several periods are neglected, as Popper does).

## Concepts
- [[frequency-interpretation]] (new) — probability statements are about relative frequency in a class or sequence of events, not about single events or belief (p. 137)
- [[subjective-vs-objective-probability]] (new) — subjective: probability measures belief or logical proximity; objective: it is a statement about frequencies. Popper counts Keynes's logical view as subjective (pp. 135–137)
- [[classical-definition-of-probability]] (new) — favourable cases divided by equally possible cases; Popper finds latent subjective and objective readings (p. 135)
- [[collective]] (new) — von Mises: a sequence, indefinitely continuable, obeying the axioms of convergence and randomness (p. 139)
- [[axiom-of-convergence]] (new) — the frequency sequence tends to a limit; Popper wants to eliminate it (pp. 140, 142)
- [[axiom-of-randomness]] (new) — no gambling system can succeed; Popper wants a weaker version (pp. 140–142)
- [[fundamental-problem-of-chance]] (new) — why incalculability of single events yields empirically corroborated frequency conclusions (p. 138)
- [[relative-frequency-finite-class]] (new) — ${}_{\alpha}F''(\beta)=N(\alpha.\beta)/N(\alpha)$ (p. 144)
- [[independence-insensitiveness]] (new) — ${}_{\alpha.\beta}F''(\gamma)={}_{\alpha}F''(\gamma)$; a three-termed relation, symmetric in $\beta,\gamma$ (p. 146)
- [[ordinal-vs-neighbourhood-selection]] (new) — selecting by ordinal number vs. by neighbours' properties (p. 147)
- [[n-freedom]] (new) — frequencies insensitive to selection by predecessor $k$-tuples for all $k\le n$ (p. 151)
- [[first-binomial-formula]] (new) — for $(n-1)$-free $\alpha$: ${}_{\alpha_{(n)}}F''(m)={}^nC_m p^m q^{n-m}$ (p. 154)
- [[mathematical-vs-empirical-sequence]] (new) — distinguished by the (intensional) construction rule (p. 156)
- [[decidability-of-probability-statements]] (new) — whether and how probability statements can be tested; task announced here (p. 134)
- [[falsifiability]] — probability statements are said to be impervious to strict falsification (p. 133)
- [[corroboration]] — the corroboration of hypotheses is deferred to sections 79–85 (p. 133)

## Canonical instances
- [[two-dice-eleven]] — numerical probability 1/18 for throwing eleven (p. 134)
- [[die-five-next-throw]] — 1/6 read as frequency in a class of throws (p. 137)
- [[coin-alternative-sequence]] — the 0/1 sequence (A) and its frequency sequence (A′) (p. 140)
- [[buttons-in-a-box]] — red/large buttons illustrate selection and independence (p. 145)
- [[five-button-counterexample]] — shows that finiteness does not suffice for triple symmetry (p. 146 fn 4)
- [[period-1100-alternative]] — the 1-free sequence that is not 2-free (pp. 148–149)
- [[divisible-by-four-sequence]] — a mathematical sequence with limits 3/4 and 1/4 (p. 156)
- [[pendulum-sequence]] — an empirical but non-random sequence that can be approximated mathematically (p. 156)

## Bridges (candidates)
- [structural-analogy] $n$-freedom (insensitivity to the last $n$ elements) ↔ stochastic processes: Markov-chain order — both ask how many past elements matter for the next one.
- [same-math] Definition 1 and the multiplication and Bayes-type division theorems for finite classes ↔ elementary probability: counting proportions and conditional proportions.
- [structural-analogy] Axiom of randomness (no profitable selection rule) ↔ probability/finance: no-arbitrage or Dutch-book-type arguments — both say that no betting rule can beat the stated odds.
- [structural-analogy] Independence as "selection leaves the frequency unchanged" ↔ statistics: conditional independence, $P(\gamma\mid\beta)=P(\gamma)$.
- [same-math] First binomial formula ↔ probability: the binomial distribution $\binom{n}{m}p^mq^{n-m}$.

## Questions this raises
- If probability statements cannot be strictly falsified, how can empirical evidence ever count against them? What is "decidability" supposed to mean?
- Can the axiom of convergence really be dropped, so that frequency limits follow from the random character of a sequence (sections 63–67)?
- Is Popper's n-freedom a good definition of randomness, given that an $n$-free sequence still has a short, regular generating period?
- How do equal-chance hypotheses and extrapolations of statistics justify frequency hypotheses in the first place?

## Reading notes
- This is part 1 of 3 of chapter 8. It starts at the chapter's opening (printed p. 133) and ends at printed p. 157, in the middle of section 57, just after the two "sources" of frequency estimates are announced. Printed page numbers are in the labels; pdf = printed + 29.
- Many footnotes marked with an asterisk (*) were added by Popper later. One note on p. 150 carries "Added 1968". I report them as Popper's later notes.
- Text-layer problems:
  - On p. 140 the first term of the frequency sequence (A′) shows as "O". Computing from sequence (A) gives 0/1. No page image was supplied for this page.
  - On p. 152 the text layer garbles the exponent in "2n + 1". The image shows $2^{n+1}$ (also $2^{n+1}+n$, and $2^n+n-1$ in fn *3).
  - On p. 154 the question about frequency in "the sequence α_n" appears with α_n (adjoining) in the image. The formula and footnote 1 concern overlapping segments α_(n). I read α_(n) as intended.
- Footnote 4 (p. 146): I added the checks that ${}_{\alpha.\beta}F''(\gamma)=1/2={}_{\alpha}F''(\gamma)$ and ${}_{\beta}F''(\gamma)=2/3$, reading the counts inclusively. The footnote itself only asserts the inequality ${}_{\alpha}F''(\gamma)\neq{}_{\beta}F''(\gamma)$.
