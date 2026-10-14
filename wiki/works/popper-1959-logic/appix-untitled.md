---
id: popper-1959-logic/appix-untitled
work: popper-1959-logic
unit: "Appendix *ix — Corroboration, the Weight of Evidence, and Statistical Tests"
pages: 402–439
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Appendix *ix: Corroboration, the Weight of Evidence, and Statistical Tests

## L0 — One line
Popper argues that the degree to which evidence supports or corroborates a theory cannot be its probability, and he proposes measures (E, C) that reward informative content and severe tests instead.

## L1 — The gist (≤ 120 words)
Popper asks whether the support evidence gives a theory can be measured by the theory's probability. He argues it cannot. A statement can be supported by the evidence while being less probable than a statement the evidence undermines, and that is self-contradictory if support equals probability. He proposes measures (E and C) built on explanatory power. They tie confirmability to a theory's content, which is its improbability. He then applies them to the "weight of evidence" paradox and to statistical tests. C counts as corroboration only if the evidence reports sincere, severe attempts to refute the theory. This separates testing a theory from making it probable.

**Prerequisites:** conditional probability, $p(a,b)=p(ab)/p(b)$; negation and conjunction of statements; sample frequencies and the idea of a binomial sequence of tosses; base-2 logarithms.

## L2 — Key ideas
- **Corroboration is not probability.** If support is defined as probability-raising, one can build cases where $x$ is supported by $z$, $y$ is undermined by $z$, and yet $x$ is less probable than $y$ given $z$. That is self-contradictory if degree of support is identified with probability (pp. 405–407, 413–414).
- **The target.** Popper says Carnap's theory contains both assumptions the refutation needs. He also says its contradictoriness is not a minor matter that can easily be repaired, and that any change of assumption (a) would be ad hoc (pp. 409–410).
- **Likelihood needs a new calculus.** For a universal theory $x$, $p(x)=0$, so the criterion "$p(x,y)>p(x)$" fails. Rewriting the criterion as (4), with $p(y,x)>p(y)$, avoids this, but using it needs a calculus in which $p(y,x)$ is a definite number even when $p(x)=0$ (pp. 404–405).
- **Content and confirmability.** Science does not aim primarily at high probability but at high informative content well backed by experience. Content is $P(\bar x)$, and confirmability should increase with it. A contradiction like $x\bar x$ should get $C=0$ even though $P(x\bar x,y)=1$ (p. 416).
- **Definitions and desiderata.** E measures explanatory power. C is built from E and satisfies a list of desiderata (i)–(ix). Popper calls the particular definition unimportant; what may be important are the desiderata and the fact that they can be satisfied together (pp. 416–419).
- **Weight of evidence.** A "paradox of ideal evidence" troubles the subjective theory. Treated objectively, evidence bears on the statistical hypothesis $h$, not on the single event, and, when the evidence is favourable, E and C can be large only for precise reports on large samples (pp. 425–430).
- **Statistical tests are hypothetical-deductive.** A full report of a long sequence of tosses is useless as evidence for a statistical hypothesis. A probabilistic hypothesis can be tested only by statistical abstracts. Fisher's likelihood is adequate only in the special case of very small $\delta$ (pp. 431–432).
- **Not induction in disguise.** C is a degree of corroboration only if $e$ reports sincere, severe attempts to refute $h$. Popper says the requirement of sincerity cannot be formalized (pp. 433, 437).

## L3 — Walkthrough

### Introduction (pp. 402–411)

**The problem (p. 402).** Popper reprints three notes from the *British Journal for the Philosophy of Science*. By "the problem of degree of corroboration" he means two tasks:
- (i) to show there is a measure of the *severity of the tests* a theory has undergone and of *how it passed or failed them*;
- (ii) to show this measure cannot be a probability, i.e. does not obey the formal laws of the probability calculus.

He says his book only outlined this, especially (ii). Earlier authors (Keynes, Jeffreys, Kaila, Reichenbach) could not show that a universal law could reach probability $>1/2$, or even a probability other than zero (pp. 402–403).

**A general probability calculus (p. 403).** Popper wanted a formal calculus open to several interpretations: absolute logical probability, Keynesian relative logical probability, relative frequencies in sequences, and measures of ranges or sets. The definition $p(a,b)=p(ab)/p(b)$ breaks down when $p(b)=0$. He needed $p(a,b)$ to be a definite number even then. The reason is that corroboration $C(x,y)$ (theory $x$, evidence $y$) needs the converse $p(y,x)$, which Fisher calls the "likelihood of $x$". Popper was convinced that $p(x)=0$ for a theory $x$ (p. 403).

**Why the criterion needs likelihood (pp. 404–405).** Write $Co(x,y)$ for "$x$ is supported, corroborated or confirmed by $y$". The obvious criterion is

$$Co(x,y)\iff p(x,y)>p(x). \tag{1}$$

But for a universal theory $x$ and empirical evidence $y$, previous appendices give

$$p(x)=0=p(x,y), \tag{2}$$

so $Co(x,y)$ would always be false. The same holds practically in a very large universe, where both are immeasurably small (p. 404). The way out is this. Whenever $p(x)\neq0\neq p(y)$,

$$p(x,y)>p(x)\iff p(y,x)>p(y), \tag{3}$$

so (1) can be rewritten as

$$Co(x,y)\iff p(x,y)>p(x)\ \text{ or }\ p(y,x)>p(y). \tag{4}$$

If $y$ follows from $x$, intuitively $p(y,x)=1$. If $y$ is empirical, $p(y)<1$. Then (4) gives $Co(x,y)$ (p. 404). So "$x$ may be corroborated by $y$ if $y$ follows from $x$, provided only that $p(y)<1$" (p. 405). Using (4) requires a calculus where $p(y,x)$ is a definite number (here 1) even if $p(x)=0$ (p. 405).

*Intuition note.* A universal law gets probability zero, so "raises the probability" can never hold for it. Popper switches to asking how well the law predicts the evidence. That needs a calculus that still gives a number for $p(y,x)$ when $p(x)=0$.

**Publication history (p. 405).** The first note appeared in 1954. An axiom system for relative probability followed about six months later; it is equivalent to, though less simple than, the one in appendix *iv. It gives definite $p(x,y)$ even if $p(y)=0$ (p. 405).

**The refutation of "$C=p$" (pp. 405–407).** The first note claims a mathematical refutation of all theories of induction that identify degree of support with probability. Such an identification would force the self-contradictory assertion:

(*) there are cases where $x$ is strongly supported by $z$, $y$ is strongly undermined by $z$, and yet $x$ is confirmed by $z$ to a lesser degree than $y$ (p. 405).

*Die example (p. 406).* Take the next throw of a fair die. $x$ = "six", $y=\bar x$, $z$ = "an even number". Then

$$p(x)=\tfrac16,\quad p(y)=\tfrac56,\quad p(z)=\tfrac12;\qquad p(x,z)=\tfrac13,\quad p(y,z)=\tfrac23.$$

$z$ raises $x$ from $1/6$ to $2/6$ and lowers $y$ from $5/6$ to $4/6$, yet $p(x,z)<p(y,z)$. This proves

$$\exists x,y,z:\ p(x,z)>p(x)\ \&\ p(y,z)<p(y)\ \&\ p(x,z)<p(y,z), \tag{5}$$

and "$<$" in the middle clause can be weakened to "$\le$". By (1), the corollary is

$$\exists x,y,z:\ Co(x,z)\ \&\ \sim Co(y,z)\ \&\ p(x,z)<p(y,z). \tag{6}$$

Popper says theorem (5) is far from being paradoxical. But if one identifies degree of confirmation $C(a,b)$ with probability $p(a,b)$, (6) becomes

$$Co(x,z)\ \&\ \sim Co(y,z)\ \&\ C(x,z)<C(y,z), \tag{**}$$

which is self-contradictory (p. 407). Here "degree of confirmation" just means degree to which $y$ supports $x$, not Popper's usual "severity of tests passed" (p. 407). The proof rests on only two assumptions:
- (a) formula (1);
- (b) any assertion of the form (***) $x$ has property $P$, $y$ has not, and $y$ has $P$ to a higher degree than $x$ (e.g. "warmer") is self-contradictory (p. 407).

*Intuition note.* If evidence helps $x$ and hurts $y$, then $x$ must come out better confirmed than $y$. Probability can still rank $y$ higher, because it also reflects how probable each statement was to begin with. So probability cannot be the measure of support.

**Targets and the dispute over Carnap (pp. 408–410).**
- *Popper's targets.* He says he aimed at Keynes, Jeffreys, Reichenbach, Kaila, Hosiasson and, more recently, Carnap. His ten-line footnote on Carnap objected that Carnap spoke of a consensus of practically all modern theories of degree of confirmation without mentioning Popper's dissent (p. 408). He also objected that Carnap's split into probability$_1$ (degree of confirmation) and probability$_2$ (frequency) was insufficient (p. 408).
- *Critics.* **Bar-Hillel** said the criticism was purely verbal and anticipated by Carnap. **Kemeny** summarized Popper's thesis as the claim that Carnap's measures, or any other assignment of logical probability, are unsuited to measure degrees of confirmation. Popper says this was not his principal thesis (p. 408).
- *Popper's claim about Carnap.* Both (a) and (b) are explicit in Carnap's book: (a) as Carnap's formula (4) on p. 464, and (b) on p. 73 with the "Warm/Warmer" example ($Pa.\sim Pb.Rba$ is self-contradictory) (p. 409). Popper therefore says Carnap's theory is self-contradictory and that this is not "a minor matter" (p. 409).
- *Explicanda.* By defining "confirmed" via $p(x,y)>p(x)$, Popper says, Carnap shows his explicandum is roughly Popper's own, the intuitive idea of support. Carnap had inadvertently, by Popper's account, two different and incompatible explicanda in mind with probability$_1$, one being Popper's $C$ and the other his $p$ (pp. 409–410).
- *Popper's conclusion.* Any change of (a) would be ad hoc, and it is the attempts to rescue the theory, not his criticism, that are "purely verbal" (p. 410).

**Aside on symbolism and induction (p. 410).** Popper (his own opinion) complains that symbolism almost seems to be becoming a value in itself. He says the only possible value of such formalism seems to be that a contradiction, once pinpointed, cannot be evaded verbally. He says he was disappointed to be met with evasions. He still thinks the identification $C=p$ will be abandoned one day (p. 410).

**The main doctrine (pp. 410–411).** Popper regards the doctrine that degree of corroboration cannot be a probability as one of the more interesting findings of the philosophy of knowledge. A test report can be summed up as a degree of corroboration, never as a probability. Probability does not express the severity of the tests passed. The reason: a theory's content, which is the same as its improbability, determines its testability and corroborability (p. 411). He believes content and degree of corroboration are the most important logical tools developed in his book. Footnote 8 is a priority claim: Popper says he took the idea of content from no one. Carnap told him his 1942 attribution to Wittgenstein was a memory error and that he had Popper's book in mind (p. 411, n. 8).

**Editorial note (p. 411).** The notes keep the word "confirmation" and the symbol $P$. Some misprints are corrected, starred footnotes are added, and points *13 and *14 are new (p. 411).

### First Note: Degree of Confirmation (pp. 412–419)

**§1–2 (p. 412).** The aim is a definition, in terms of probabilities, of the degree $C(x,y)$ to which $x$ is confirmed by $y$. $P(x,y)$ is relative probability and $P(x)$ is absolute probability; either would suffice for the definition. Footnote 1: $P(x)$ can be defined as $P(x,\bar z z)$, and $P(x,y)=P(xy)/P(y)$. It is often assumed that $C(x,y)=P(x,y)$; the first task is to show this is inadequate (p. 412).

**§3 (pp. 412–413).** For contingent $x,y$ there are three special cases: establishment ($x$ follows from $y$), disestablishment ($\bar x$ follows from $y$), and independence, $P(xy)=P(x)P(y)$. $C$ at independence lies below establishment and above disestablishment. Partial support and partial undermining lie between these. We say $y$ supports $x$ (undermines $x$) whenever $P(xy)$ (respectively $P(\bar x y)$) exceeds its value under independence. These three cases are exhaustive and exclusive (p. 413).

**§4 (pp. 413–414).** Suppose $x_1,x_2,y$ exist with $x_1,x_2$ each independent of $y$ (or undermined by $y$) while $y$ supports $x_1x_2$. Then $y$ would confirm $x_1x_2$ more than either part:

$$C(x_1,y)<C(x_1x_2,y)>C(x_2,y). \tag{4.1}$$

If $C(x,y)=P(x,y)$, i.e.

$$C(x,y)=P(x,y), \tag{4.2}$$

this contradicts the valid probability law

$$P(x_1,y)\ge P(x_1x_2,y)\le P(x_2,y). \tag{4.3}$$

(4.3) follows from the general multiplication principle together with $0\le P(x,y)\le1$. The special addition principle also fails, because it gives (using $P(x,y)\ge0$)

$$P(x_1x_2\ \text{or}\ x_1\bar x_2,\,y)\ge P(x_1x_2,y). \tag{4.4}$$

But "$x_1x_2$ or $x_1\bar x_2$" is equivalent to $x_1$, so substituting in (4.1) gives

$$C(x_1x_2\ \text{or}\ x_1\bar x_2,\,y)<C(x_1x_2,y), \tag{4.5}$$

which contradicts (4.4) under (4.2). Footnote 2: Carnap uses the multiplication and addition principles as "conventions on adequacy", arguing only that they are generally accepted for probability$_1$. Popper replies that he introduced "degree of confirmation" precisely because confirmability must increase with testability, thus with logical improbability and content (p. 414, n. 2).

**§5 (p. 414).** Counters have four exclusive, equally probable colours: blue, green, red, yellow. $x_1$ = "$a$ is blue or green"; $x_2$ = "$a$ is blue or red"; $y$ = "$a$ is blue or yellow". All conditions hold. $y$ follows from $x_1x_2$ and raises its probability to twice its value without $y$. (Added check: $P(x_1)=P(x_2)=P(y)=\tfrac12$, $P(x_1y)=P(\text{blue})=\tfrac14=P(x_1)P(y)$, so independence holds. $P(x_1x_2)=\tfrac14$ and $P(x_1x_2,y)=\tfrac12$.) Footnote 3: this satisfies (i) via independence; adding amber as a fifth colour and putting $y$ = "amber or blue or yellow" gives undermining (p. 414).

**§6 (p. 414).** A more striking example: $x_1$ = "$a$ is blue", $x_2$ = "$a$ is not red", $y$ = "$a$ is not yellow". Then $P(x_1)=\tfrac14$, $P(x_2)=\tfrac34$, and $\tfrac13=P(x_1,y)<P(x_2,y)=\tfrac23$. $y$ supports $x_1$ and undermines $x_2$ (clear from the figures, and from $y$ following from $x_1$ and from $\bar x_2$). We must demand $C(x_1,y)>C(x_2,y)$, yet $P$ gives the opposite. Footnote *1: $p(y,x_1)=p(y,\bar x_2)=1$, so Fisher's likelihood of $x_1$ in the light of $y$ is maximal (p. 414).

**§7 (p. 415).** Why were $C$ and $P$ confounded? Popper offers *suggestions*, not a known answer:
- the tendency to think the "likelihood" of a hypothesis must be a probability;
- the later use of "degree of confirmation" as a name for logical probability, perhaps under the mistaken view that science must settle for the highest attainable probability since it cannot reach certainty;
- the turning of "degree of confirmation of $x$ by $y$" into "the degree to which $y$ confirms $x$", which would make $C(x_1,y)<C(x_2,y)$ obviously absurd when $y$ supports $x_1$ and undermines $x_2$, although $P(x_1,y)<P(x_2,y)$ may be fine if $P(x_1)<P(x_2)$ to begin with;
- a tendency to confuse measures of *increase* with the measures that increase (velocity, acceleration, force).

**§8 (pp. 415–416).** The dispute is not verbal. Two arguments:
- Confirmation is supposed to estimate how far $x$ is backed by experience. But $P(x,y)$ depends strongly on $P(x)$, which has nothing whatever to do with the empirical evidence (pp. 415–416).
- Confirmation is supposed to bear on whether to accept a hypothesis tentatively. "Science does not aim, primarily, at high probabilities." It aims at high informative content well backed by experience; a hypothesis may be probable merely because it says little (p. 416).

So $C$ should be defined so that only hypotheses with high content reach high confirmation. Confirmability (the maximum degree of confirmation) should increase with the content $C(x)=P(\bar x)$, i.e. with testability. Thus while $P(x\bar x,y)=1$, $C(x\bar x,y)$ should be zero (p. 416).

**§9: definitions (pp. 416–417).** Let $E(x,y)$ be a non-additive measure of the explanatory power of $x$ with respect to $y$, bounded by $-1$ and $+1$. For consistent $x$ and $P(y)\ne0$:

$$E(x,y)=\frac{P(y,x)-P(y)}{P(y,x)+P(y)} \tag{9.1}$$

(Footnote 4: the consistency condition can be dropped if $P(x,y)=1$ whenever $y$ is inconsistent.) $E$ can also be read as a measure of the dependence of $y$ on $x$. It satisfies the most important desiderata but not all; it violates (viii, c), and satisfies (iii) and (iv) only approximately in special cases. To remedy this Popper defines, for consistent $x$ and $P(y)\ne0$:

$$C(x,y)=E(x,y)\bigl(1+P(x)P(x,y)\bigr) \tag{9.2}$$

The simpler $E(x,y)(1+P(xy))$ satisfies most desiderata but violates (iv). Footnote *2 gives a simpler alternative that also satisfies all the desiderata, first stated in 1954:

$$C(x,y)=\frac{P(y,x)-P(y)}{P(y,x)-P(xy)+P(y)} \tag{9.2*}$$

and in relativized form

$$C(x,y,z)=\frac{P(y,xz)-P(y,z)}{P(y,xz)-P(xy,z)+P(y,z)}. \tag{10.1*}$$

**The desiderata (pp. 417–418).** The theorem is that $C$ of (9.2) satisfies all of:
- (i) $C(x,y)\gtreqless0$ respectively iff $y$ supports $x$, is independent of $x$, or undermines $x$.
- (ii) $-1=C(\bar y,y)\le C(x,y)\le C(x,x)\le1$.
- (iii) $0\le C(x,x)=C(x)=P(\bar x)\le1$. $C(x)$ is an additive measure of content: the absolute probability that $x$ is false. "Thus confirmability equals refutability or testability."
- (iv) If $y$ entails $x$, then $C(x,y)=C(x,x)=C(x)$.
- (v) If $y$ entails $\bar x$, then $C(x,y)=C(\bar y,y)=-1$.
- (vi) Let $x$ have high content (so $C(x,y)$ approaches $E(x,y)$) and let $y$ support $x$ (e.g. $y$ the total empirical evidence). Then for given $y$, $C(x,y)$ increases with the power of $x$ to explain $y$, and so with the scientific interest of $x$.
- (vii) If $C(x)=C(y)\ne1$, then $C(x,u)\gtreqless C(y,w)$ whenever $P(x,u)\gtreqless P(y,w)$. (Footnote *3: the condition "$\ne1$" was missing in the original.)
- (viii) If $x$ entails $y$: (a) $C(x,y)\ge0$; (b) for given $x$, $C(x,y)$ and $C(y)$ increase together; (c) for given $y$, $C(x,y)$ and $P(x)$ increase together.
- (ix) If $\bar x$ is consistent and entails $y$: (a) $C(x,y)\le0$; (b) for given $x$, $C(x,y)$ and $P(y)$ increase together; (c) for given $y$, $C(x,y)$ and $P(x)$ increase together.

Footnote 6: (vii) and (viii) contain the only important desiderata that $P(x,y)$ satisfies (p. 418).

*Intuition note.* $E$ is positive when $y$ is more probable given $x$ than on its own, and it is scaled to lie between $-1$ and $1$. $C$ adjusts $E$ so that a theory with little content can never score high. That is how "says little" is penalized.

**§10 (p. 418).** Everything can be relativized to initial information $z$ (assuming $P(z,z\bar z)\ne0$):

$$C(x,y,z)=E(x,y,z)\bigl(1+P(x,z)P(x,yz)\bigr) \tag{10.1}$$
$$E(x,y,z)=\frac{P(y,xz)-P(y,z)}{P(y,xz)+P(y,z)} \tag{10.2}$$

Footnote 7 (Einstein vs. Newton): let $x_1$ be Einstein's theory, $x_2$ Newton's, $y$ today's interpreted evidence, and $z$ part of $y$ (e.g. last year's evidence). Since $x_1$ may be assumed to explain more of $y$ than $x_2$, we get $C(x_1,y,z)\ge C(x_2,y,z)$ for every $z$, and strict inequality for suitable $z$. This follows from (vi) "even if we have to assume that $P(x_1,yz)=P(x_2,yz)=P(x_1)=P(x_2)=0$" (p. 418, n. 7).

**§11 (pp. 418–419).** Popper believes some intuitive desiderata cannot be satisfied by any formal definition. Example: a theory is better confirmed the more ingenious our unsuccessful refutation attempts were. The definition captures something of this idea, though not as much as can be formalized; one cannot completely formalize a sincere and ingenious attempt (pp. 418–419). Footnote 8 gives one way of nearer approach: put a premium on crucial experiments with

$$C_{a,b}(h)=\Bigl(C(h,e_b)\prod_{i=1}^{n}C(h,c_i,e_a)\Bigr)^{1/(n+1)},$$

where $c_1,\dots,c_n$ are the experiments made between times $t_a$ and $t_b$. The text postulates $P(c_i,e_b)=1$, $P(c_i,e_a)\ne1$ and $P(c_i,U c_j)\ne1$ for $j<i$ (so that only new experiments count) (p. 419, n. 8). The later footnote (*) says Popper would now separate the formula from its *application*. $C(x,y)$ must not be interpreted as corroboration, or used for acceptability, unless $y$ represents the (total) results of sincere attempts to refute $x$. It also suggests relativizing to a field of application, $C_F$, and summing over independent fields (p. 419). Popper's verdict: he considers the particular way in which $C(x,y)$ is defined unimportant. What may be important are the desiderata and the fact that they can be satisfied together (p. 419).

### A Second Note on Degree of Confirmation (pp. 419–423)

**1. Logarithmic content (pp. 419–421).** Kemeny, and independently Hamblin, suggested measuring content by $-\log_2P(x)$ instead of $1-P(x)$. Then in desiderata (ii) and (v), $\pm1$ becomes $\pm\infty$, and (iii) becomes

$$0\le C(x,xy)=C(x,x)=C(x)=-\log_2P(x)\le+\infty,$$

the others unchanged (p. 420). Hamblin proposes

$$C(x,y)=\log_2\frac{P(xy)}{P(x)P(y)} \tag{1}$$
$$C(x,y)=\log_2\frac{P(y,x)}{P(y)} \tag{2}$$
$$C(x,y,z)=\log_2\frac{P(y,xz)}{P(y,z)} \tag{3}$$

(1) equals (2) for finite systems but not necessarily for infinite ones. (2) stays determinate when $P(x)=0$ (p. 420). These violate viii(c), as Hamblin observes, and ix(b) and (c) are also not satisfied. Popper holds that viii(c) marks the difference between explanatory power (which may be symmetrical in $x$ and $y$) and confirmation (which should not be). His example: let $y$ follow from $x$ and support $x$, and let $x$ be unconfirmed by $y$; then it does not seem satisfactory to say that $ax$ is always as well confirmed by $y$ as $x$ (the text leaves $a$ unspecified), although there seems no reason why $ax$ and $x$ should not explain $y$ equally well, since both completely explain $y$ (p. 420). So Popper prefers to read (2) and (3) as definitions of *explanatory power* $E$, and to define confirmation from E in ways satisfying viii(c). One way, with $n\ge1$ (large $n$ gives viii(c) a marked effect):

$$C(x,y)=\frac{E(x,y)}{(1+nP(x))\,P(\bar x,y)} \tag{4}$$
$$C(x,y,z)=\frac{E(x,y,z)}{(1+nP(x,z))\,P(\bar x,yz)} \tag{5}$$

For a universal theory with $P(x)=0$ and empirical $y$, the difference between $E$ and $C$ disappears, as it does if $x$ follows from $y$. The change from old to new definitions is order-preserving, so the difference is metrical only (p. 421).

**2. Weight of evidence (p. 421).** Popper says these definitions give full weight to the "weight of evidence" (Keynes's "weight of an argument"), especially the new ones (p. 421).

**3. The metric of $C$ depends on the metric of $P$ (pp. 421–423).** Popper claims no satisfactory metric of logical probability can rest on purely logical considerations. Take a measurable property like length, with logically necessary finite limits $l$ and $u$ and some distribution on $[l,u]$. An empirically motivated correction of the physical measure may be non-linear, and then "logical probability" must be corrected too. Its metric would depend on empirical knowledge, not be a priori (p. 422). Background knowledge $z$ can largely, but not entirely, overcome this (p. 422). Even without a metric, the usual axiom systems retain their significance, much as pure metrical geometry does without a yardstick. This matters for identifying logical independence with probabilistic independence. On a probabilistic theory of induction, it turns out that we cannot learn if we identify them in this way, but we can learn very well in the sense of Popper's $C$-functions (pp. 422–423). Footnote *2 says Popper now believes the difficulty is overcome for secondary probabilities (see *13), but is not exaggerated for primary properties (p. 422).

**4. (p. 423).** On Popper's axiom systems for relative probability, $P(x,y)$ can be considered defined for any $x,y$, including $P(y)=0$; in the logical interpretation it equals 1 whenever $x$ follows from $y$, even if $P(y)=0$. He sees no reason to doubt that the definitions work for languages with singular statements and universal laws, even if all laws have probability zero (as with Kemeny's measure $m$). Departing from equal weights for models would depart from a logical interpretation (p. 423).

**5. Tenth desideratum (p. 423).** (x) If $C(x,y)>0$, then (a) $C(\bar x,y)<0$ and (b) $C(x,\bar y)<0$. Popper says it seems clear to him that this is an indispensable adequacy condition; he notes it is not satisfied by all definitions proposed by other authors (p. 423).

### A Third Note on Degree of Corroboration or Confirmation (pp. 424–438)

**1–2. Problem and subjective theory (pp. 424–425).** The problem of the "weight of evidence" was first raised by Peirce and discussed by Keynes and Good. Popper says that within the subjective theory of probability it leads to paradoxes he thinks insoluble there, and that his theory solves it with ease. By "subjective theory" he means interpreting probability as a measure of ignorance, partial knowledge, or the degree of rationality of belief given the evidence. A parenthesis argues that the usual "degree of rational belief" should rather be the degree of rationality of a belief (pp. 424–425).

**3. The paradox of ideal evidence (pp. 425–426).** Let $a$ = "the $n$th (unobserved) toss of penny $z$ yields heads". On the subjective theory, $P(a)=\tfrac12$ (1). Let $e$ be a statistical report on thousands or millions of tosses, ideally favourable to the hypothesis that $z$ is symmetrical, e.g. "among a million tosses, heads occurred in $500{,}000\pm20$ cases". Popper says $e'$ with $500{,}000\pm1{,}350$ would still be ideal under $C$ and $E$, since $e$ entails $e'$. The subjective theory must then say

$$P(a,e)=\tfrac12 \tag{2}$$
$$P(a)=P(a,e) \tag{3}$$

so, according to the subjective theory, $e$ is on the whole (absolutely) irrelevant information with respect to $a$. That means the "degree of rational belief" in $a$ ought to be unaffected by the accumulated evidence, which Popper finds a little startling (p. 426).

**4. Why Popper thinks the paradox cannot be solved there (p. 426).** The fundamental postulate of the subjective theory is that degrees of rationality of belief form a linear order, measurable on one scale. All attempts from Peirce to Good solve the weight-of-evidence problem by adding another measure besides probability. That implicit admission, Popper says, shows that evidence may affect rationality of belief in more than one way, which is sufficient to overthrow the fundamental postulate (p. 426). He adds that the claim that the different measures explicate different "explicanda" stands or falls with that postulate (p. 426).

**5–6. The objective reading (pp. 426–428).** On an objective interpretation (statistical or propensity), introduce $b$, the statement of the experimental conditions (e.g. "a toss of $z$, randomized by spinning"), and the objective hypothesis $h$: "$P(a,b)=\tfrac12$". We are mainly interested in $h$. The ideal evidence $e$ bears on $h$ and is neutral to $a$. If tosses are independent or random, $P(a,be)=P(a,b)$ for any statistical $e$. The question becomes how $e$ corroborates $h$. If $e$ is ideally favourable, $E(h,e)$ and $C(h,e)$ approach 1 as the sample size goes to infinity. So no paradox arises, and we can measure the weight of evidence with respect to $h$ by $E(h,e)$ or $C(h,e)$, or, closer to Keynes, by their absolute values (p. 428). Footnote 5 recalls $E(h,e)=\frac{P(e,h)-P(e)}{P(e,h)+P(e)}$ and that $C$ approaches $E$ in most cases of importance. Footnote 6 expects the logarithmic functions of Hamblin and Good to improve numerically calculable cases (pp. 427–428).

*Intuition note.* The "ideal" data say nothing about the next single toss beyond what the setup already says. They say a lot about whether the coin is fair. Once the probability statement is itself the hypothesis under test, evidence can pile up for it without any paradox.

**7. What makes a good test statement (p. 428).** The key expression is

$$P(e,h)-P(e). \tag{4}$$

$E$ and $C$ are two ways of "normalizing" (4) and increase and decrease with it. To get a good test statement we need $e$ with (i) $P(e,h)$ (Fisher's likelihood of $h$) nearly 1, and (ii) $P(e)$ nearly 0. Then $e$ itself must be submitted to empirical tests (p. 428).

For a statistical hypothesis

$$P(a,b)=r \tag{5}$$

let $e$ be: "in a sample of size $n$ satisfying $b$, $a$ holds in $n(r\pm\delta)$ of the instances". Then, especially for small $\delta$,

$$P(e)\approx2\delta. \tag{6}$$

One may even put $P(e)=2\delta$. This assigns equal probability $1/(n+1)$ to each of the $n+1$ proportions $0/n,\dots,n/n$. A report "$m\pm d$ of $n$ have $a$" then gets $P(e)=(2d+1)/(n+1)$, and with $\delta=(d+\tfrac12)/(n+1)$ this is $2\delta$ (p. 429). This is Laplace's equidistribution (used for his rule of succession). It is adequate for the absolute probability $P(e)$ of a sample report, but inadequate for $P(e,h)$, where a Bernoullian (combinatorial) distribution is adequate (p. 429). Footnote *1: $\delta\ge1/2n$ for finite $n$. Footnote *2: (6) holds because content increases with precision (pp. 429, n. *1–*2).

$P(e,h)$ is close to 1 either if $\delta$ is comparatively large (roughly $\delta\approx\tfrac12$) or, for small $\delta$, if $n$ is large (pp. 429–430). So $P(e,h)-P(e)$, and thus $E$ and $C$, can be large only if $\delta$ is small and $n$ large, i.e. if $e$ is a statistical report asserting a good fit in a large sample (p. 430). A test statement is better the greater its precision ($\sim1/2\delta$), hence its content and refutability, and the larger $n$. Favourable accumulating evidence increases $E$ and $C$ (p. 430).

**8. Numbers (p. 430).** $P(e,h)$ comes from the binomial theorem (or Laplace's integral); $P(e)=2\delta$. For $n=1{,}000{,}000$, the $\delta$ maximizing $P(e,h)-P(e)$ is $0.0018$. The $\delta$ maximizing $E$ is $0.00135$, with $E(h,e)=0.9946$. For a universal law $h$ = "$P(a,b)=1$" that has passed $n$ severe tests all with result $a$: $C(h,e)=E(h,e)$ because $P(h)=0$; with Laplacean $P(e)$ and $d=0$,

$$C(h,e)=\frac{n}{n+2}=1-\frac{2}{n+2}.$$

(Added check: $P(e,h)=1$ and $P(e)=\frac1{n+1}$, so $E=\frac{1-\frac1{n+1}}{1+\frac1{n+1}}=\frac n{n+2}$.) Non-statistical theories usually have a very different form, and forced into this form their instances become "essentially non-observational" (p. 430). Footnote *3: a field-of-application approach could use this method, but it ignores fine-structure of content and probability and is very crude for non-statistical theories. The comparative method of footnote 7 (First Note) can be used instead (pp. 430–431, n. *3).

**9. Statistical testing is deductive (pp. 431–432).** A test statement $e$ is constructed to follow (or almost follow) from $h$ while having high content, then confronted with experience. A full report of a long sequence of tosses is useless as evidence for a statistical $h$: every actual sequence of length $n$ has the same probability given $h$. So $E=C=0$ whether the sequence is all heads or exactly half and half. A logically weaker statistical abstract (average frequency) can be used. "A probabilistic hypothesis can explain only statistically interpreted findings". It can be tested only by statistical abstracts, not by the "total available evidence" if that is a full observation report (p. 431). Footnote *4: for an abstract, $P(e)$ equals its width $2\delta$ without assuming independence of the individual reports. Statistical methods are therefore "essentially hypothetical-deductive", proceeding by the elimination of inadequate hypotheses (p. 432).

**10. Relation to Fisher's likelihood (pp. 432–433).** If $\delta$ is very small (hence $P(e)$ too, possible only for large samples), then

$$P(e,h)\approx P(e,h)-P(e). \tag{7}$$

"In this case, and only in this case" can Fisher's likelihood be accepted as an adequate measure of corroboration. Popper reads his measure as a *generalization* of the likelihood function, covering cases such as a comparatively large $\delta$. It is paradoxical that a million tosses with $\delta=0.00135$ and a hundred tosses with $\delta=0.135$ give the same likelihood $P(e,h)=0.9930$. But $E(h,e)=0.9946$ while $E(h,e')=0.7606$, which is satisfactory (pp. 432–433). Footnote *5: for a die and $x$ = "next throw is a six", the likelihood of $x$ is 1 for $y$ = "even", "$>4$", or "other than 2". The values of $C(x,y)$ are $3/8$, $4/7$ and $1/10$ (p. 433, n. *5).

**11. (p. 433).** For a universal law, $P(h)=0$ in an infinite universe. In most systems the likelihood $P(e,h)=P(eh)/P(h)$ is then $0/0$. A calculus is needed that gives definite values, and always $P(e,h)=1$ whenever $e$ follows (or "almost follows") from $h$. Popper's published system does this (p. 433).

**12. Interpretations (pp. 433–434).** $E(h,e)$ can be read as explanatory power even if $e$ is not a report of sincere attempts to refute $h$. $C(h,e)$ can be read as degree of corroboration (or of the rationality of belief in $h$ in the light of tests) only if $e$ consists of reports of the outcome of sincere attempts to refute $h$, rather than of attempts to verify it (p. 433). Popper suggests probability cannot measure the rationality of belief (excluded by the paradox of ideal evidence), but degree of corroboration may. The calculus of probability has many interpretations. Among them is a logical one taking probability as a generalization of deducibility, but this has little to do with estimates of chances. Probability statements express hypothetical appraisals of objective possibilities in the experimental set-up, never estimates of our own nescience (Popper cites Poincaré: the opposite view springs from a possibly unconscious determinism) (p. 434). A "rational gambler" estimates objective odds. The odds he accepts are the *object* of his belief in a hypothesis $h$, not a measure of his degree of belief (p. 434). Corroboration is "nothing but" a measure of how far $h$ has been tested and has stood up to tests. It is not a degree of rationality of belief in the truth of $h$; indeed $C(h,e)=0$ whenever $h$ is logically true. It measures the rationality of *tentatively accepting* a guess, knowing it is a guess that has undergone searching examination (p. 434).

**\*13. Primary and secondary probability statements (pp. 434–437).** (Added after the original note.) Popper's thesis is that on a *secondary* level Laplace's and Bernoulli's distributions provide a logical metric. Primary statements have the form $p(a,b)=r$, with elements from a system $S_1$. These statements are the elements of a secondary system $S_2=\{e,f,g,h,\dots\}$ (p. 435). Bernoulli's theorem, roughly: if $h$ is "$p(a,b)=r$" and is true, then in a long sequence of $n$ repetitions it is extremely probable that the frequency of $a$ is $r$ or nearly so. Let $\delta_r(a)_n$ denote "$a$ occurs with frequency $r\pm\delta$ in $n$ repetitions". Then, as a secondary relative probability statement,

$$\lim_{n\to\infty}p(g,h)=1,$$

with $g=\delta_r(a)_n$ and $h$ the information that $p(a,b)=r$. Also this probability goes to 0 if $p(a,b)=s$ with $s$ outside $r\pm\delta$, which matters for refuting probabilistic hypotheses (p. 435). Since $g$ is a frequency statement and $h$ a hypothetical probability estimate, Popper proposes (for a homogeneous $S_2$) a frequency interpretation of the primary statements, and a *logical* interpretation of the secondary statements $P(g,h)=r$ (pp. 435–436). Then the Laplacean distribution gives $P(g)=2\delta$ whether $g$ is observed or hypothesized, so the typical hypothesis $h$ ($\delta=0$) gets $P(h)=0$. Bernoulli's methods give $P(g,h)$ by pure mathematics. Thus, even with no logical metric for primary probabilities, there is one at the secondary level: Bernoulli's for relative probabilities (secondary likelihood of primary hypotheses), Laplace's for absolute probabilities (of reports on samples) (p. 436). Popper says Bernoulli and Laplace tended to identify $C$ with $p$ and were mistaken. Statistical hypotheses are tested by attempts to reduce their secondary likelihood to zero or near zero, and nothing is easier than selecting statistical evidence favourable to a statistical hypothesis if we wish to do so (pp. 436–437).

**\*14. Has Popper changed his creed? (pp. 437–438).**
- *The question.* An inductivist critic might say $C(h,e)$ could be called "inductive probability" or "degree of rationality of belief", and that Popper has solved the problem of induction positively (p. 437).
- *Popper's reply.* He is indifferent to terminology so long as it does not mislead. But $C(h,e)$ can be interpreted as degree of corroboration "only if $e$ is a report on the severest tests we have been able to design" (p. 437). This marks the difference from the inductivist or verificationist, who wants affirmation and "firmness". At best the inductivist demands that $e$ comprise our total observational knowledge, favourable or not. That demand cannot be formalized, and neither can the demand for sincerity. Without it we "simply deceive ourselves" (pp. 437–438).
- *Eliminative induction.* The critic may point to eliminative induction (Bacon, Whewell, Mill). Popper replies that its purpose was to establish the surviving theory as true (or highly probable) (p. 438). He thinks the number of competing theories remains infinite, so elimination cannot seriously reduce it. What we do, or should do, is hold for the time being to the most improbable of the surviving theories or, more precisely, the one that can be most severely tested. We "accept" it only as worthy of further criticism and severest tests. We may add that the survivor is the best theory, and the best tested theory, we know (p. 438).

**Addendum, 1972 (pp. 438–439).** (1) By "best" theory Popper means the surviving competitor with the greatest explanatory power, content and simplicity and the least ad hoc. It is also best testable, but it need not always be the best tested. (2) He points to Gillies (1971), "A Falsifying Rule for Probability Statements", as an important contribution on falsifying statistical tests (pp. 438–439).

## Toy example (ours, not from the text)
A fair die. Evidence $y$ = "the result is not 1", so $P(y)=\tfrac56$. Let $x_1$ = "the result is 2" and $x_2$ = "the result is not 2".

| Quantity | $x_1$ | $x_2$ |
|---|---|---|
| $P(x)$ | $\tfrac16$ | $\tfrac56$ |
| $P(x,y)$ | $\tfrac{1/6}{5/6}=\tfrac15$ | $\tfrac{4/6}{5/6}=\tfrac45$ |
| $P(y,x)$ | $1$ | $\tfrac45$ |

- *Support.* $P(x_1,y)=\tfrac15>\tfrac16$, so $y$ supports $x_1$. $P(x_2,y)=\tfrac45<\tfrac56$, so $y$ undermines $x_2$.
- *Probability ranking.* Yet $P(x_1,y)=0.2<0.8=P(x_2,y)$. If support were probability, $x_2$ would be "better confirmed", which is the paradox of (**).
- *E by (9.1).* $E(x_1,y)=\frac{1-5/6}{1+5/6}=\frac{1/6}{11/6}=\frac1{11}$. $E(x_2,y)=\frac{4/5-5/6}{4/5+5/6}=\frac{-1/30}{49/30}=-\frac1{49}$.
- *C by (9.2).* $C(x_1,y)=\frac1{11}\bigl(1+\tfrac16\cdot\tfrac15\bigr)=\frac1{11}\cdot\frac{31}{30}=\frac{31}{330}\approx0.094$. $C(x_2,y)=-\frac1{49}\bigl(1+\tfrac56\cdot\tfrac45\bigr)=-\frac1{49}\cdot\frac53=-\frac5{147}\approx-0.034$.
- *Result.* $C$ ranks $x_1$ above $x_2$, matching "supports vs. undermines", and the signs agree with desideratum (i).

## Concepts
- [[corroboration]] — degree to which a theory has passed severe tests; here measured by $C$, not a probability (p. 402)
- [[bayesian-confirmation]] — the criterion that $y$ supports $x$ iff $p(x,y)>p(x)$, formula (1): the obvious criterion of support, used as assumption (a) of Popper's refutation but failing for universal theories with $p(x)=0$ (pp. 404, 407)
- [[explication]] — Carnap's "explicandum/explication" talk; Popper claims Carnap's probability$_1$ had two incompatible explicanda (pp. 409, 426)
- [[falsifiability]] — content measured by improbability; testability and confirmability rise with it (p. 411, p. 416)
- [[content-as-improbability]] (new) — content of $x$ is $P(\bar x)$ (or $-\log_2P(x)$); high content means high testability (pp. 416, 419–420)
- [[explanatory-power-E]] (new) — $E(x,y)=\frac{P(y,x)-P(y)}{P(y,x)+P(y)}$, bounded by $\pm1$; positive when $x$ raises the probability of $y$ (p. 416)
- [[likelihood-fisher]] (new) — $p(y,x)$, Fisher's "likelihood of $x$"; needs a calculus defined even when $p(x)=0$ (p. 403)
- [[relative-probability-calculus]] (new) — Popper's calculus where $p(a,b)$ is defined also when $p(b)=0$ (pp. 403, 405)
- [[weight-of-evidence]] (new) — Keynes's and Good's notion, here measured by $E$, $C$ or their absolute values (pp. 424, 428)
- [[paradox-of-ideal-evidence]] (new) — on the subjective theory, $P(a,e)=P(a)$ although $e$ looks weighty (pp. 425–426)
- [[subjective-vs-objective-probability]] (new) — probability as degree of rational belief vs. probability of objective possibilities in a set-up (pp. 424, 426, 434)

## Canonical instances
- [[die-support-paradox]] — $x$="six", $y$="not six", $z$="even": supported yet less probable than the undermined statement (p. 406)
- [[colored-counters-example]] — four equiprobable colours showing independent parts whose conjunction is supported, and the example with $x_1$ = blue, $x_2$ = not red, $y$ = not yellow (p. 414)
- [[penny-ideal-evidence]] — million tosses with $500{,}000\pm20$ heads, $P(a,e)=\tfrac12$ (p. 425)
- [[universal-law-n-tests]] — $C(h,e)=n/(n+2)$ after $n$ passed tests (p. 430)
- [[einstein-newton-comparison]] — $C(x_1,y,z)\ge C(x_2,y,z)$ even when all four probabilities are zero (p. 418, n. 7)
- [[carnap-warm-warmer]] — Carnap's own self-contradiction example, used by Popper as assumption (b) (p. 409)

## Bridges (candidates)
- [same-math] Hamblin's $C(x,y)=\log_2\frac{P(xy)}{P(x)P(y)}$ ↔ information theory: pointwise mutual information. Popper says it is related to the fundamental idea of information theory (p. 421); the formula itself is the standard log-ratio.
- [structural-analogy] $E$ and $C$ as normalized forms of $P(e,h)-P(e)$ ↔ statistics: likelihood against a baseline. Both compare how well a hypothesis predicts the data with how well the data are predicted anyway.
- [structural-analogy] "Probability-raising" ↔ Bayesian confirmation: formula (1) is the standard relevance criterion. Popper's point is that the criterion defines support but fails as a measure, because $P(x,y)$ also carries the prior $P(x)$.
- [metaphor] Fisher's likelihood approaching maximum merely because $e$ is imprecise ↔ overfitting to vague data. The analogy is only loose.

## Questions this raises
- If $C$ only counts as corroboration when $e$ reports "sincere" severe tests, and sincerity cannot be formalized, how can a researcher or reader check it in practice?
- Popper says the particular definition of $C$ is unimportant and the desiderata matter. Are the desiderata jointly satisfied by essentially one family of measures, or by many incompatible ones? (He offers (9.2), (9.2*), (4)–(5) and the log forms.)
- The Laplacean absolute probability $P(e)=2\delta$ assumes equal weights across sample proportions. How sensitive are $E$ and $C$ to that choice when the true sampling process is different?
- Why would Popper hold to the "most improbable surviving theory" rather than the best-supported one when the number of rival theories is always infinite?

## Reading notes
- Printed page = pdf − 29 (pdf 431 = p.
- Running header: "new appendices"/"appendix *ix". Title page of the work is not in these pages. Edition details come from the unit metadata, not from these pages.
- Equations and numbers were compared with the page images. "ax" is printed in the Second Note (p. 420); the text does not say what $a$ is, so it is left unspecified here.
- Popper's own footnote *3 (p. 418) notes that the condition "$\ne1$" in (vii) was missing from the original text and published corrections.
- Footnote *5 (p. 433) gives $C$ values $3/8$, $4/7$, $1/10$. The text does not say which definition is used. (Added check: they match (9.2*), not (9.2).)
- On p. 409, "pp. 463 f.", "p. 464" and "p. 73" are page numbers in Carnap's book, not in this one.
- Page 435 prints "wheever s falls outsider r ± δ"; this looks like a typographical error for "whenever $s$ falls outside $r\pm\delta$".
- Page 439 gives the Gillies 1971 reference; the addendum is dated 1972 as printed.
- Sections such as "Introduction" and the notes' internal numbering follow the author's own numbering; no exercises appear in this unit.
