---
id: jaynes-2003-probability/appb-mathematical
work: jaynes-2003-probability
unit: Appendix B — Mathematical formalities and style
pages: 661-676
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Appendix B — Mathematical formalities and style

## L0 — One line
Jaynes fixes his notation and defends a "cautious approach": derive results on finite sets of propositions, then pass to infinite limits only at the end and only if the limit is well-behaved. He also defines "function" as the practical analyst does (good functions plus their well-behaved limits).

## L1 — The gist (≤ 120 words)
The appendix asks which mathematical conventions keep probability calculations free of error. Jaynes's answer has three parts. First, capital-P symbols take propositions only; ordinary functions get another symbol such as f. Second, work on finite sets and pass to infinite limits only after checking that they are well-behaved. Third, define "function" as good functions plus well-behaved limits of them, which admits delta-functions and excludes nondifferentiable "pathologies". He suggests that most, perhaps all, paradoxes of infinite sets come from passing to the limit too soon. He rejects measure-theoretic notation as a guarantee of rigor, and he asks readers for "mathematical courtesy" in place of nitpicking.

**Prerequisites:** Boolean logic of propositions; limits of sequences; Fourier transform and delta-function basics; derivative and continuity; variance of an estimator; Cox's theorems (probability rules derived from consistency desiderata).

## L2 — Key ideas
- Capital-P probability symbols take only propositions; a function of a number is written with another symbol (e.g. f). Jaynes says that replacing a proposition by a bare value inside the symbol led to the marginalization paradox (pp. 661–662).
- Finite sets are the safe harbor where Cox's theorems apply. A finite-set result may be extended to infinity only if its limit is well-behaved (pp. 662–663).
- Jaynes declines measure-theory notation. He holds that it assumes the infinite limit before the derivation starts, and that such notation does not make arguments rigorous (pp. 663–665).
- He sees Kronecker and Weierstrasz as differing in aesthetics, not substance. Both rest on the integers, and Kronecker's demand for algorithmic constructions is called valuable (pp. 665–666).
- "Function" means good functions plus well-behaved limits of sequences of them. What matters about the Fourier transform is the properties (B.10)–(B.12), not convergence of integrals (pp. 667–668).
- Under this definition delta-functions are legitimate and nondifferentiable functions are excluded. Jaynes argues that Cramér's apparent estimators of "abnormally high" precision come from omitting a delta-function term (pp. 668–671).
- Counting infinite sets by 1:1 correspondence gives contradictions. Counting finite sets and then taking limits gives consistent results (pp. 671–672).
- Jaynes treats the Hausdorff paradox as a mathematical disease to be quarantined. He argues that errors in infinite-set reasoning surface late (pp. 672–674).
- He asks for charitable reading ("Emancipation Proclamation") and denies that rigor guarantees correctness (pp. 674–676).

## L3 — Walkthrough

**Opening (p. 661).** Jaynes says careless notation has produced many erroneous results. Notation should be free to evolve for convenience, but needs a fixed "safe harbor" of normative rules to fall back on. Each chapter from Chapter 3 on starts from these standard forms and evolves from them (p. 661).

### B.1 Notation and logical hierarchy
- In $P(A|B)$ (B.1), $A$ and $B$ are always *propositions*, usable as elements of Aristotelian logic under a Boolean algebra. So $P(A|B)$ is not a "function" in the usual sense (p. 661).
- The symbol is undefined if the conditioning statement has zero probability (his example: $B = CD$ with $P(C|D)=0$). Ignoring this is like dividing by zero (p. 661).
- Let $A \equiv$ "the variable $q$ has the particular value $q'$" (B.2). Writing $P(q'|B)$ (B.3) is illegitimate, because $q'$ is not a proposition. For an ordinary function he writes $f(q'|B)$ (B.4) (pp. 661–662).
- Why it matters: a full proposition carries a qualifier, $A \equiv$ "$q$ has the value $q'$ if the proposition $B$ is true" (B.5). Replacing $A$ by $q'$ drops the qualifier. Later the same symbol can appear under a different qualifier $B_1$ and be mistaken for the same quantity (p. 662).
- Jaynes says this happened in the "marginalization paradox": one symbol stood for probabilities conditional on two different pieces of prior information. He refers to Jaynes (1980) and Chapter 15 (p. 662).
- Compromise: small-$p$ symbols may take propositions or numbers in any mix, e.g. $p(A|B)=p(q|B)$ (B.6). The reader must judge the meaning from context, and Jaynes warns that misreading them can cause errors (p. 662).
- Custom: Greek letters for parameters of a distribution, Latin letters for the corresponding data quantities, e.g. $\mu=\langle x\rangle=E(x)$ and $m=\bar x=n^{-1}\sum x_i$ (p. 662).

*Intuition note:* A proposition says "q = q′ given these conditions". A bare number q′ says nothing about conditions. Keeping the two apart helps you avoid treating two different conditional probabilities as one.

### B.2 The "cautious approach" policy
- Chapter 2 derived the probability rules for discrete, finite sets of propositions. Finite sets are the safe harbor: Cox's theorems apply and nobody has produced an inconsistency from the sum and product rules (p. 662).
- Extending to infinite sets needs the same caution as going from finite sums to infinite series. The "parlor game" at the start of Chapter 15 is cited as an illustration of the danger (p. 663).
- Procedure: Jaynes writes that it appears the only safe procedure known at present is to derive the result on a finite set by the strict rules, then see how it behaves as the number of propositions grows. Three outcomes are possible (p. 663):
  1. It tends smoothly to a finite limit (well-behaved). The limit is accepted as the solution on the infinite set.
  2. It blows up.
  3. It stays bounded but oscillates forever.
- In cases 2 and 3 the limit is ill-behaved and cannot be accepted as a valid solution, so he refuses to pass to the limit at all (p. 663). This is the "look before you leap" policy: in principle, pass to a limit only after verifying that it is well-behaved. In practice standard situations need not be re-tested each time, but in case of doubt the test must be done (p. 663).
- Even if the limit is well-behaved, operating directly on the infinite set may give the right answer, but one cannot count on it (p. 663).

*Intuition note:* The limiting process carries information that the bare limit hides. If the limit is ill-behaved, working directly on the infinite set would give nonsense with no visible cause.

### B.3 Willy Feller on measure theory
- Measure-theoretic treatments in effect assume the passage to an infinite set before probabilities are introduced; Feller (1966) is cited as an example (p. 663).
- **Feller's remark:** specialists deny the need for measure theory because they lack acquaintance with cases where vague reasoning gave wrong results. Jaynes notes that Feller cites no such case (p. 663).
- Jaynes knows of many documented absurdities from careless use of infinite sets (Chapter 15). He knows of no case where his policy leads to inconsistency or an unreasonable result (p. 663).
- He does not use measure-theory notation because it presupposes the limit at the start. He often passes to infinite limits at the end, which he describes as using Lebesgue measure in its original meaning (p. 663).
- Feller grudgingly calls the finite-then-limit approach "logically impeccable" and a good exercise for beginners (p. 664).
- **Kac's case:** the class of continuous functions is not measurable (inner measure zero, outer measure one). To get a measurable class, Kac enlarges it to include everywhere-discontinuous functions. Jaynes objects that the resulting measure then sits almost entirely on the class that physics excludes most strongly (p. 664).
- Jaynes's bypass in four steps (p. 664):
  1. Expand the continuous functions in $n$ orthogonal functions.
  2. Assign probabilities to the coefficients in $\mathbb R^n$.
  3. Do the calculation.
  4. Let $n\to\infty$ at the end.

  In real problems, beyond some $n$ the change is numerically negligible. Applications from statistical mechanics to radar detection are cited (p. 664).
- Claim, hedged by Jaynes (it appears to him): most, perhaps all, paradoxes of infinite sets are caused by passing to infinite limits too soon; usually this loses crucially important information (nonconglomerability, Chapter 15, is his example). His position is that such paradoxes belong to infinite-set theory and have no place in probability theory. He conjectures that perhaps all correct results in probability theory are combinatorial theorems on finite sets or well-behaved limits of them (p. 664).
- He still accepts set/measure language ("almost everywhere", "of measure zero") for compactness, never as a source of rigor. He says that giving every old notion a new impressive name has nothing to do with rigor and is, more often than not, gamesmanship that conceals triviality (pp. 664–665).

### B.4 Kronecker vs. Weierstrasz
- Does the emphasis on finite sets make analysis suspect? Jaynes says no. He says the Weierstrasz–Kronecker conflict was exaggerated by later commentators, and he cites Bell (1937) as an example of a distorted picture (p. 665).
- **Poincaré (1899):** equations about continuous magnitudes are symbols standing for an infinite collection of inequalities between whole numbers. **Edwards (1989):** both men based their mathematics entirely on whole numbers (p. 665).
- Bell tells, without supporting documentation according to Jaynes, that Kronecker asked what use Lindemann's proof of the transcendence of π could be, since irrational numbers do not exist. Kronecker himself praised Leibniz's series (p. 666)
$$\frac{\pi}{4}=1-\frac13+\frac15-\frac17+\cdots \tag{B.7}$$
  as determining a geometrical irrational by arithmetic of odd integers. Weierstrasz also defined irrationals from the integers (p. 666).
- Jaynes's verdict: the difference was *aesthetic*. Kronecker keeps first principles in view. Weierstrasz forgets the construction steps and uses the result as a new element. In computer terms, a higher-level language over the same "machine language" (p. 666).
- Kronecker's valuable complaint was that much of set theory is not algorithmic (no finite rule to construct or test membership). Jaynes thinks mathematics might be healthier had this been heeded (p. 666).

*Intuition note:* In the account Jaynes gives (via Poincaré and Edwards), both Kronecker and Weierstrasz based their mathematics on the whole numbers. What Jaynes finds valuable in Kronecker's complaint is that much of set theory gives no rule to construct an element or to decide membership in a finite number of operations.

### B.5 What is a legitimate mathematical function?
- Pure mathematics generalised "function" so that set-theory notions stay valid (arbitrary mappings between sets). Applied mathematics generalised it so that useful analytical operations stay valid (pp. 666–667).
- Fourier pair:
$$F(k)=\int dx\,e^{ikx}f(x),\qquad f(x)=\frac1{2\pi}\int dk\,e^{-ikx}F(k) \tag{B.8}$$
  written $[f(x)\leftrightarrow F(k)]$ (B.9). Properties (p. 667):
$$f(x-a)\leftrightarrow e^{ika}F(k) \tag{B.10}$$
$$\int dy\,f(x-y)g(y)\leftrightarrow F(k)G(k) \tag{B.11}$$
$$f'(x)\leftrightarrow ik\,F(k),\qquad -ix\,f(x)\leftrightarrow F'(k) \tag{B.12}$$
  So analytical operations on one function become algebraic operations on the other. A linear differential, difference or convolution-type integral equation becomes an algebraic equation for $F(k)$; solve it, then invert (p. 667).
- Early theory (Dirichlet form; Titchmarsh 1937) focused on convergence of the integral and denied a transform to any function whose integral diverged. Jaynes calls this an intolerable restriction (p. 667).
- Jaynes's physicist view: the usefulness lies in (B.10)–(B.12). If any means defines a mapping preserving them (for sufficiently well-behaved functions), the use of transforms is "perfectly rigorous", whether or not the integrals or series converge. A divergent Fourier series is still a unique ordered sequence of numbers, determined by and determining its transform (p. 667).

*Intuition note:* A transform is judged by what it lets you do (turn calculus into algebra), not by whether the defining integral converges.

**B.5.1 Delta-functions.**
- Dirac introduced $\delta(x-y)$, generalising $\delta_{ij}$. It is the "Fourier transform of a constant": as $F(k)\to1$, $f(x)\to\delta(x)$ (p. 668).
- Mathematicians using the set-theory definition said delta-functions do not "exist". Jaynes says a delta-function is not a mapping of one set onto another, so the objection comes from an inappropriate definition of "function". He calls Schwartz (1950) awkward for the same reason (p. 668).
- Temple (1955) and Lighthill (1957): "function" means good functions and limits of sequences of good functions. So a discontinuous function is *defined* as a limit of continuous ones. Lighthill saw that this definition is the one appropriate to Fourier theory; Jaynes says it is now clear that it is also the one appropriate to probability theory and all of analysis. For example, any Fourier series can be differentiated term by term any number of times, and the result identifies a unique function (p. 668).
- Lighthill's table contains transforms of functions formerly held not to have one. Jaynes reports Dyson's review, which said the book overturns Hardy's work and that Hardy would have enjoyed it more than anybody (p. 668). Footnote 5: Lighthill's "good function" is defined differently, and Jaynes has never seen a real problem where the underlying good functions could not be chosen analytic (p. 668).

**B.5.2 Nondifferentiable functions.**
- Aczel showed Cox's functional equations can be solved without assuming differentiability, at the cost of much longer derivations, and with the same solutions (p. 668).
- **Hermite (to Stieltjès):** he said he turned away in horror from this plague of functions that have no derivatives (p. 668).
- Weierstrasz function (p. 669), with $0<a<1$ and $m$ a positive odd integer:
$$f(x)\equiv\sum_{n=0}^{\infty}a^n\cos(m^n x). \tag{B.13}$$
  It is a Fourier series of period $2\pi$ and converges uniformly (as well as $\sum a^n$), so $f$ is continuous. If $ma>1$, term-by-term differentiation gives a badly divergent series. The derivative
$$f'(x)\equiv\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{B.14}$$
  then does not exist for any $x$, when $ma>1$ (the proof is tedious; footnote 6 cites Hardy 1911, and Titchmarsh 1939 gives only a shorter proof valid when $ma>1+3\pi/2$) (p. 669).
- It is a limit of good functions (partial sums), but not a well-behaved limit: it fails (B.12). Jaynes sees it as of no apparent use to him (p. 669).
- Jaynes says functions like this do arise in applications: in Chapter 7 the attempt to solve the integral equation (7.49) by Fourier methods ran up against this difficulty when the kernel was too broad, and the conclusion was that the equation has no usable solution unless the kernel $\phi(x-y)$ is at least as sharp as the driving force $f(x)$ (p. 669).

**B.5.3 Bogus nondifferentiable functions.**
- The commonly cited example is a sequence $f_n(x)$ of strings of isosceles right triangles with hypotenuse length $1/n$ on the real axis. The slope is $\pm1$ almost everywhere for finite $n$. The limit of the derivative does not exist, but the derivative of the limit does, because $f_\infty(x)\equiv0$. Calling $f_\infty$ nondifferentiable is a common error (p. 669).
- **Lebesgue's defence:** limiting oneself to well-behaved functions would mean renouncing many problems. Jaynes says he cannot cite any specific problem that was actually solved in the way Lebesgue claims, but he borrows Lebesgue's argument to defend his own position. Rejecting limits of good-function sequences also renounces real problems (p. 669).
- **Cramér's bound** (p. 670), for estimator $\theta^*$ from $n$ observations from $f(x|\theta)$, bias $b(\theta^*)\equiv E(\theta^*-\theta)$:
$$\operatorname{var}(\theta^*)\ge\frac{(1+db/d\theta)^2}{n\int dx\,(\partial\log f/\partial\theta)^2 f(x|\theta)}. \tag{B.15}$$
- **Cramér's claim:** if $f(x|\theta)$ has discontinuities, estimators of "abnormally high" precision may exist, with variance below this limit (p. 670).
- Jaynes's diagnosis: Cramér used the set-theory definition, so $\partial\log f/\partial\theta$ "does not exist" at discontinuities, and he integrated only over regions of continuity. In Jaynes's definition the derivative of a discontinuous $g$ contains $[g(y+)-g(y-)]\,\delta(x-y)$ at each discontinuity $y$. Including this term, (B.15) reduces in the limit to $\operatorname{var}(\theta^*)\ge0$. That is useless but anomaly-free, with no apparent violation of the Schwartz inequality (p. 670).
- Likewise the integral equation (p. 670)
$$\int_a^b dy\,K(x,y)f(y)=\lambda g(x) \tag{B.16}$$
  generally has delta-function terms like $\delta(y-a)$ or $\delta'(y-b)$ at the end-points. Those who reject delta-functions say it has no solution. Jaynes cites Middleton (1960) and irreversible processes in statistical mechanics as places where the terms are needed (p. 670).
- Jaynes calls it a "sick policy" to admit limits of bad-function sequences while refusing limits of good ones. He quotes Poincaré (1909): modern inventors of new functions make them to invalidate ancestors' reasoning. Jaynes adds that the "pathology" only arose from a different, surreptitious definition of "function" (pp. 670–671).
- His criterion: an "appropriate" definition lets theorems have the greatest validity without long lists of exceptions. In his work "function" includes good functions and well-behaved limits of them, but not nondifferentiable functions. Footnote 7: he defines "moving average" for a finite series so that the theorems are exact, with no end-effect corrections (p. 671).
- Jaynes also says he cannot conceive of any useful purpose for a nondifferentiable function, that the fad of artificial pathology seems nearly to have run its course, and that he stamps out this plague simply by defining "function" in the way appropriate to his subject (pp. 670–671).

*Intuition note:* A jump is the limit of ever-steeper smooth curves. The slope develops an ever-taller, ever-thinner spike, whose area is the jump size. Dropping it throws away real contribution to the integral.

### B.6 Counting infinite sets?
- Jaynes opens with Lewis Carroll's verse about an argument that turns out to be a bar of mottled soap. He recounts Hardy's reply to McTaggart's challenge to prove from 2+2=5 that McTaggart is the Pope (subtract 3 to get 1=2), and says infinite-set theory offers a superior grade of mottled soap (p. 671).
- Premise: two sets have the same number of elements if they can be put in 1:1 correspondence. Using $n\leftrightarrow 2n$ and $2n\leftrightarrow 2n-1$ one is led to (p. 671):
  - (A) integers = even integers;
  - (B) even integers = odd integers;
  - (C) integers = 2 × even integers.

  From (A) and (C), $1=2$ (p. 672), by reasoning like Eqs. (15.2)–(15.3).
- Jaynes's view: the "set of all integers" is undefined except as a limit of finite sets. With an explicit limiting process no contradiction arises, though the limiting ratio (even)/(integers) can be made any $x\in[0,1]$, with (odd)/(integers) $=1-x$ (p. 672).
- Example: the sequence $\{1,3,2,5,7,4,\dots\}$ (two odds, then one even) includes every integer once. Counting the first $n$ elements and then letting $n\to\infty$ gives consistent statements (p. 672):
  - (A′) integers = 3 × evens;
  - (B′) evens = ½ × odds;
  - (C′) integers = evens + odds.
- **Galileo (1638):** each integer has exactly one square, yet in a certain sense the great majority of integers are not squares. His conclusion, quoted: we cannot speak of infinite quantities as one greater, less or equal to another. Jaynes says Weyl (1949) judged almost the same (p. 672).

### B.7 The Hausdorff sphere paradox and mathematical diseases
- The above is structurally almost the same as the Hausdorff paradox, but promoted to uncountable sets. $X,Y,Z$ are disjoint sets nearly covering the sphere. $X$ is congruent to $Y$, $Y$ to $Z$, and extraordinarily $X$ is also congruent to $Y\cup Z$ (p. 672).
- **Savage (1962)** took this as literal fact: someone who says congruent sets are equally probable cannot actually hold that belief. **Jaynes's reply:** his belief that such a state of knowledge exists is vastly stronger than his belief in the soundness of the reasoning behind Hausdorff's result (p. 672).
- Jaynes presumes this paradox and Russell's barber paradox have similar explanations: self-contradictory weird sets, from which anything can be deduced (p. 673).
- He quotes **Poincaré's quip** that future generations will regard Mengenlehre as "a disease from which one has recovered". He cites a statistician's remark and Gell-Mann (1992), who thought the "Bourbaki plague" is dying out. Jaynes wishes he could feel that optimistic and finds the plague more serious than obscure language, because it infects content. Russell's theory of types disposes of only some paradoxes. Infinite-set theorists should put their own house in order and keep the disease out of applied fields (p. 673).
- **Weyl (via Kline 1980):** applying classical logic, built for finite sets, to infinite sets without justification is "the Fall and original sin of set theory". Jaynes adds that Brouwer and Weyl both noted this (p. 673).
- Why paradoxes appear late (Chapter 15): an erroneous argument that gives absurd results is abandoned at once. One that gives reasonable results on early tries gets used, first on similar problems, and fails only when stretched (p. 673).
- Parallel in orthodox statistics: confidence intervals worked at first on simple problems (no nuisance parameters, sufficient statistics available, no important prior information). Their numbers then matched Bayesian intervals under Jeffreys's uninformative priors. Jaynes (1976) showed they are satisfactory as inferences only where they agree with Bayesian intervals (pp. 673–674). Footnote 10: confidence intervals are correct as statements about sampling properties of estimators, but can be absurd as inferences, e.g. lying wholly in a region known to be impossible (p. 674).
- He quotes Gibbs (via Kline): "The pure mathematician can do what he pleases, but the applied mathematician must be at least partially sane." (p. 674)

### B.8 What am I supposed to publish?
- Savage's question: whatever he chose he was criticised. Jaynes pleads for tolerance. Those who study infinite sets or measure theory may do so without justifying applications; those who study useful aspects owe no apology either (p. 674).
- The level of the book is meant to let readers extract what they want. Brief reasons are given why favoured ideas are "obvious" and disliked ones not; gaps are partly filled by the Comments sections (p. 674).
- "Obvious" is used as gamesmanship in both directions: to wave through notions that do not stand up to examination (or to brush aside ones that stand up too well), and to feign deep critical faculties by doubting simple matters (p. 674).
- Jaynes calls it pathetically mistaken for an author in this field to claim that mathematical rigor guarantees the correctness of the results. Experience suggests that the more one concentrates on the appearance of rigor, the less one checks the real-world validity of premises, and the likelier absurd conclusions become (pp. 674–675).

### B.9 Mathematical courtesy
- Anecdote: a young Ph.D. could not finish defining his sets in an hour, and the audience never learned his theorem. Jaynes attributes this to "studied mathematical discourtesy", not higher rigor. A 19th-century mathematician like Poincaré, he says, would have been into the meat of the calculation within a few minutes (p. 675).
- Charges he lists: introducing $x$ without naming its set, differentiating without stating differentiability, using a natural special property (accused of lack of generality). The fanatic seeks fault with style, not understanding; length grows and content shrinks (p. 675).
- A courteous reader takes "variable $x$" to imply a set of values, and a twice-differentiated $f$ to be twice differentiable. The nitpicker also objects if anyone else ever used a term with a slightly different shade of meaning (pp. 675–676).
- **Emancipation Proclamation** (p. 676): every introduced variable has some set $X$ of possible values; every function is well-behaved enough for what is done with it; every proof is general enough for the application made. Finding the most general conditions is homework for the interested reader.
- He suggests such a Proclamation (with perhaps a sentence on sigma-algebras, Borel fields and Radon–Nikodym derivatives) could convert 19th-century works to 20th-century standards. Sources are listed: Bell (1937), Félix (1960), Kline (1980), Rowe and McCleary (1989) (p. 676).

## Toy example (ours)
Question: what is the "ratio of even integers to integers" in the finite-then-limit method? Take two orderings of the same integers.

- Ordering 1: $1,2,3,4,5,6,\dots$. First $n=6$ elements: evens $\{2,4,6\}$, so ratio $3/6=1/2$. For every $n=2k$: $k/2k=1/2$. Limit $1/2$.
- Ordering 2 (Jaynes's): $1,3,2,5,7,4,\dots$. First $n=6$ elements $\{1,3,2,5,7,4\}$: evens $\{2,4\}$, so ratio $2/6=1/3$. For every $n=3k$: $k/3k=1/3$. Limit $1/3$. Odds: $4$ of $6$, so evens/odds $=2/4=1/2$, matching (B′).
- Both orderings include every integer exactly once, yet the limits differ ($1/2$ vs $1/3$). Hence "the fraction of evens" is meaningless until the limiting process is stated. Once it is stated, each ordering is internally consistent: $1/3+2/3=1$, matching (C′). Matching 1:1 directly on the infinite sets, with no stated limiting process, is what produces the contradictory (A)–(C).

## Concepts
- [[cautious-approach-policy]] (new) — derive on finite sets, then pass to the limit only if it is well-behaved (the look-before-you-leap policy) (p. 663)
- [[probability-symbol-notation]] (new) — capital $P(A|B)$ takes propositions only; functions of numbers use another symbol; small $p$ allows mixing (pp. 661–662)
- [[marginalization-paradox]] (new) — confusion arising from one symbol denoting probabilities conditional on different information (p. 662)
- [[cox-theorem]] (Cox's theorem, in canon) — here only cited: it applies on finite sets, where no inconsistency has been found (p. 662)
- [[good-function-and-limits]] (new) — "function" = good function or well-behaved limit of good functions (pp. 668, 671)
- [[delta-function]] (new) — Fourier transform of a constant; legitimate as a limit of good functions; needed in derivatives of discontinuities (pp. 668, 670)
- [[fourier-operational-properties]] (new) — translation, convolution and derivative rules (B.10)–(B.12) as where the transform's usefulness lies (p. 667)
- [[cramer-lower-bound]] (new) — variance bound (B.15) for estimators; Jaynes traces Cramér's apparent exceptions to dropping a delta term (p. 670)
- [[frequentist-vs-bayesian]] (canon, "Frequentist vs Bayesian inference") — Jaynes says confidence intervals are satisfactory only where they match Bayesian intervals (p. 674)
- [[nonconglomerability]] (new) — named only as an example of a paradox from taking the infinite limit too early (p. 664)

## Canonical instances
- [[marginalization-paradox]] — a case of one symbol with two conditioning meanings (p. 662)
- [[weierstrasz-function]] — continuous series (B.13) with no derivative anywhere when $ma>1$ (p. 669)
- [[cramer-discontinuity-anomaly]] — estimators of "abnormally high" precision which Jaynes traces to ignoring the delta term in $\partial\log f/\partial\theta$ (p. 670)
- [[even-odd-counting-paradox]] — the (A)–(C) vs (A′)–(C′) contrast (pp. 671–672)
- [[hausdorff-sphere-paradox]] — $X\cong Y\cong Z$ yet $X\cong Y\cup Z$ (p. 672)

## Bridges (candidates)
- [structural-analogy] Cautious approach (finite first, then check limit) ↔ numerical analysis: truncated expansions whose results are accepted only if they stabilise as $n$ grows — the book's own example is the $n$-term orthogonal expansion (p. 664).
- [same-math] Denominator of (B.15) ↔ information-theory: Fisher information of $f(x|\theta)$ times $n$ (canon link; not stated in this unit).
- [structural-analogy] Capital-P propositions vs functions ↔ bayesian: all probabilities are conditional on background information (the marginalization paradox is a failure to track it).
- [same-math] Fourier rules (B.10)–(B.12) ↔ signal processing: convolution theorem and derivative rule (canon link; not stated in this unit).
- [metaphor] Confidence intervals working until stretched ↔ bayesian: acceptable only where they agree with Bayesian intervals (p. 674).

## Questions this raises
- What exactly makes a limit "well-behaved" in a given problem, and can that be checked mechanically beyond cases 1–3?
- If delta terms are always included, how does one treat the likelihood or Fisher-type integral in (B.15) for families with jumps in their support?
- Are there results in measure-theoretic probability that Jaynes's finite-then-limit method cannot reach, or does it always reproduce them?
- When is a "limit of good functions" so ill-behaved (as in B.13) that Jaynes rejects it? What is the criterion beyond "fails (B.12)"?

## Reading notes
- Page offset: printed = pdf − 30 (pdf 691 = p. 661).
- Misprint in (B.8) as shown in the image: the inverse transform is printed with "dx", but the integration variable should be $k$. I wrote $dk$.
- The text layer drops primes and symbols in places (e.g. $q'$, $f'$, $\delta'$). I checked against the images.
- Spelling "Weierstrasz" is as printed. Jaynes calls the inequality (B.15) the "Schwartz inequality" (as printed).
- Jaynes says many short quotations are given without references and points to Bell, Félix, Kline, Rowe & McCleary (p. 676). Historical claims about Kronecker, Weierstrasz and others are Jaynes's reading of those sources; I did not check them.
- (Ours) Checking (B.12) against (B.8) as printed: with $F(k)=\int dx\,e^{ikx}f(x)$, integration by parts gives $f'(x)\leftrightarrow -ik\,F(k)$ and $ix\,f(x)\leftrightarrow F'(k)$, so the signs in (B.12) as printed appear to belong to the opposite sign convention. I transcribed the page as printed.
- No exercises in this appendix.
