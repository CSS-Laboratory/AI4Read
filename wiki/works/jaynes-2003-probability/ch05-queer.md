---
id: jaynes-2003-probability/ch05-queer
work: jaynes-2003-probability
unit: "5 Queer uses for probability theory"
pages: 119–148
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Queer uses for probability theory

## L0 — One line
Probability theory gives consistent answers only for the information you actually put in: reports of marvels, disagreements, scientific tests and uncertain evidence all go wrong when the relevant alternatives or the real form of the information are left out.

## L1 — The gist (≤ 120 words)
What happens when probability theory is applied to odd real problems: ESP, disagreement, planet discovery, uncertain evidence, courts? Jaynes's answer: model the information actually received. A report of a marvel is evidence of deception as well as of the marvel, so extreme data need not raise belief in it. The same data can push people apart when their prior information differs. Unless data are impossible on a theory, its support is meaningful only against specified alternatives. Rival rules (Jeffrey's rule, Hempel's premise) fail by dropping information. Full Bayesian analysis is often impractical, but Jaynes treats Bayes' theorem as the normative standard.

**Prerequisites:** Bayes' theorem; odds and log-odds (decibels); binomial distribution; sum and product rules; the idea of a likelihood ratio.

## L2 — Key ideas
- Good's device of imaginary results lets you read off a prior strength of belief in decibels by asking how much imagined evidence would make you take a hypothesis seriously (pp. 119–120, 125–126).
- Mrs Stewart's data are 25.8 standard deviations from chance, and the likelihood ratio of chance against the best-fitting telepathy hypothesis is about $6.6\times10^{-137}$. Once deception hypotheses (about as able as telepathy to produce the report) enter, Jaynes argues the posterior for ESP can approach 1 only if the reader's total deception prior is pushed below the ESP prior (pp. 121–124).
- The normal approximation is badly wrong far out in the tails (here by about $3\times10^{8}$). The entropy form of the binomial is just as easy (p. 122).
- Convergence of opinion is not a general theorem. "D supports S" is relative to prior information, so one datum can bring people together or push them apart. Assuming otherwise is a mind projection fallacy (pp. 126–131).
- A hypothesis cannot be confirmed or refuted by data "in themselves" unless the data are impossible on it; you need specified alternatives. Neptune, Arbuthnot and Bernoulli/Laplace illustrate this (pp. 134–138).
- Jeffrey's weighted-average rule fails because the real new information $C$ may bear on $A$ directly, not only via $B$. Bayes' theorem conditional on $C$ handles uncertain information correctly (pp. 140–142).
- Hempel's paradox rests on a premise that is not generally true. Good's two-worlds example shows an instance of a hypothesis can count against it (pp. 143–144).
- Bayesian jurisprudence: a motive is evidence only to the degree that innocent people would lack one, and the city's population cancels (pp. 144–146).
- Bayes' theorem is normative even when full analysis is impractical. The scientist's real bottleneck is inventing new hypotheses (pp. 142, 139).

## L3 — Walkthrough

### 5.1 Extrasensory perception (pp. 119–120)
- **Good's device** (Jaynes's use of it): measure your own strength of belief by imagining an experiment. Ask how much evidence would bring you just to the point of seriously considering the hypothesis, not to belief (p. 119).
- A prior of exactly zero would mean no evidence could ever change the robot's mind, which we do not want (p. 119).
- Test: Mr Smith guesses numbers from 1 to 10. Jaynes would still doubt after four correct guesses (below −40 db). He would start to consider ESP at about ten, so his belief is about −100 db (p. 120). (added step: ten correct guesses at chance 1/10 each have probability $10^{-10}$ under chance; against a perfect-ESP hypothesis, which gives them probability 1, that is a likelihood ratio of $10^{10}$, i.e. 100 db.)
- Jaynes adds that even after 1000 correct guesses he would not believe. A hypothesis $A$ at −100 db can hardly ever be believed, because alternatives $B_1, B_2,\dots$ perhaps near −60 db sit above it. Astonishing data resurrect those instead (p. 120). This is "resurrection of dead hypotheses" (Chapter 4).

*Intuition note.* Data do not raise a hypothesis in isolation. When an extremely implausible hypothesis meets astonishing data, more plausible alternatives that also fit the data are resurrected instead of it (p. 120).

### 5.2 Mrs Stewart's telepathic powers (pp. 120–125)
Jaynes states he cannot vouch that the experiment happened; he analyses what was reported (Soal and Bateman, 1954) (p. 120).

**Setup and likelihoods (pp. 120–122).**
- Design probability of a correct guess: $p=0.2$, independent trials. $H_p$ is the "null hypothesis" of pure chance. The binomial prediction is
$$(r)_{\rm est}=np\pm\sqrt{np(1-p)}.\tag{5.1}$$
- With $n=37\,100$ this is $7420\pm77$. Reported: $r=9410$, $f=0.2536$ (p. 120). The score is
$$\frac{9410-7420}{77}=25.8\ \text{standard deviations}\tag{5.2}$$
- Sampling probability under $H_p$, and its Stirling form (derived in Chapter 9):
$$P(D|H_p)=\binom{n}{r}p^r(1-p)^{n-r}\tag{5.3}$$
$$P(D|H_p)=A\exp\{nH(f,p)\}\tag{5.4}$$
$$H(f,p)=f\log\frac{p}{f}+(1-f)\log\frac{1-p}{1-f}=-0.008452\tag{5.5}$$
$$A\equiv\sqrt{\frac{n}{2\pi\,r(n-r)}}=0.00476\tag{5.6}$$
- $H(f,p)$ is the entropy of the observed distribution $(f,1-f)=(0.2536,0.7464)$ relative to the expected one $(p,1-p)=(0.2,0.8)$ (p. 121). (added step: this is minus the KL divergence of $(f,1-f)$ from $(p,1-p)$.)
- $$L_p=P(D|H_p)=0.00476\,e^{-313.6}=3.15\times10^{-139}\tag{5.7}$$
- The robot should ask whether the data are also improbable under a telepathy hypothesis. In the Bernoulli class $H_q$ ($0\le q\le1$, independent trials with success probability $q$), $H_f$ with $q=f=0.2536$ maximises $P(D|H_q)$. There the entropy is zero:
$$L_f=P(D|H_f)=A=0.00476\tag{5.8}$$
- The likelihood ratio depends only on the entropy factor:
$$\frac{L_p}{L_f}=\frac{P(D|H_p)}{P(D|H_f)}=e^{nH}=e^{-313.6}=6.61\times10^{-137}\tag{5.9}$$
- The data support $H_f$ over $H_p$ by an enormous factor (p. 122).

**5.2.1 Normal approximation (p. 122).**
- The normal approximation is
$$P(D|H_p,X)\simeq({\rm const.})\exp\Big\{\frac{-n(f-p)^2}{2p(1-p)}\Big\}\tag{5.10}$$
- Using it replaces $H(f,p)$ by the first term of its power series about the peak. It would give a likelihood ratio $e^{-333.1}$, i.e. an extra odds factor
$$\exp\{333.1-313.6\}=e^{19.5}=2.94\times10^{8}\tag{5.11}$$
- So normal approximations cannot be trusted far into the tails. Jaynes says the chi-squared test uses this approximation and can mislead when the null fits poorly. He adds that entropy and chi-squared agree within one or two standard deviations of the peak.

**5.2.2 Back to Mrs Stewart (pp. 122–125).**
- With prior probabilities $P_p, P_f$, and considering only $H_p$ and $H_f$:
$$P(H_f|DX)=P(H_f|X)\frac{P(D|H_fX)}{P(D|X)}=\frac{P_fL_f}{P_fL_f+P_pL_p}\tag{5.12}$$
- Because of (5.9), for an ESP researcher who does not consider $P_f$ particularly small, the posterior starts with over 100 nines (pp. 122–123).
- Jaynes calls this a naive application, because common sense also entertains other ways the *report* could arise. Examples: record-keeping error, a trick, selection of data, falsification. He lumps them as "deception" hypotheses $H_1,\dots,H_k$ with likelihoods and priors $L_i,P_i$ (p. 123).
- New posterior:
$$P(H_f|DX)=\frac{P_fL_f}{P_fL_f+P_pL_p+\sum P_iL_i}\tag{5.13}$$
- It is *necessary* for the posterior to be near 1 that
$$P_pL_p+\sum_iP_iL_i\ll P_fL_f\tag{5.14}$$
- If $L_i$ is of the order of $L_f$ and $P_pL_p$ is negligible by (5.7), this is roughly
$$\sum P_i\ll P_f\tag{5.15}$$
- **Jaynes's judgment:** each deception hypothesis is more likely than $H_f$, so (5.15) cannot be met. Such an experiment can never convince *him*, and not because he sets $P_f=0$ (p. 124).
- If the prior for deception exceeds that for ESP, the more improbable the data are under the hypothesis of no deception and no ESP, the more they favour deception. Advocates must push the reader's total deception prior below that of ESP (p. 124).
- Laplace saw this: he noted "the immense weight of testimonies necessary to admit a suspension of natural laws" (p. 124). Laplace also says such recitals reduce the belief of educated men (p. 124).
- Jaynes's examples (each presented as his own observation): Laigle meteorites in 1803 changed educated opinion, so the "uneducated" happened to be right (pp. 124–125). His own Bayesian frequency-estimation results (Bretthorst) were doubted because their claimed resolution gain was too large. Free programs and many analyses let doubters check for themselves (p. 125).
- Jaynes warns that the analysis neglects correlations (a persistent deviation suggests a systematic cause). This would change the numbers but, he says, not the general conclusions (p. 125).
- Why −100 db still holds: Good's device applies to whatever state of knowledge we choose to imagine. Knowing real-world alternatives exist does not change the imagined belief in ESP (p. 125).
- **Exercise 5.1** applies the device to nine propositions (p. 126).
- Jaynes notes that more evidence for the deception hypothesis exists (Hansel, Kurtz). He draws a general lesson: a person may tell the truth and not be believed even though the disbelievers reason rationally (p. 126).

*Intuition note.* Mrs Stewart's likelihood ratio against chance is huge, but chance is not the only rival. Under deception the data are no surprise, so, in Jaynes's judgment, deception hypotheses that are each more plausible a priori than ESP keep the posterior for ESP small.

### 5.3 Converging and diverging views (pp. 126–132)
- **Conjecture under test.** Mr A (believer) and Mr B (doubter) get the same data $D$:
$$P(S|I_A)\simeq1,\quad P(S|I_B)\simeq0\tag{5.16}$$
$$P(S|DI_A)=P(S|I_A)\frac{P(D|SI_A)}{P(D|I_A)},\quad P(S|DI_B)=P(S|I_B)\frac{P(D|SI_B)}{P(D|I_B)}\tag{5.17}$$
- If $D$ supports $S$: for A, $P(D|SI_A)\simeq P(D|I_A)$, so
$$P(S|DI_A)\simeq P(S|I_A)\tag{5.18}$$
- For B one would think $P(D|SI_B)>P(D|I_B)$, hence
$$P(S|DI_B)>P(S|I_B)\tag{5.19}$$
- This suggests the conjecture
$$|P(S|DI_A)-P(S|DI_B)|<|P(S|I_A)-P(S|I_B)|\tag{5.20}$$
- Jaynes says this can be verified in special cases but is not true in general. Even the log-ratio measure $\log[P(S|DI_A)/P(S|DI_B)]$ admits no general convergence theorem (p. 127).
- Observations (Jaynes's): small children converge, adults sometimes; scientists often converge on new evidence. Public debates often polarise instead (the Dreyfus affair; nuclear power, abortion) (pp. 127–128). Kahneman and Tversky (1972) read experimental divergence as an argument against Bayesian methods. Jaynes asks whether divergence is Bayesian after all (p. 128).
- **Key point.** The ESP information was not $S$ (adequate precautions were taken and she did deliver this performance, 5.21). It was that someone *claimed* $S$. If your prior for $S$ is below your prior for deception, hearing the claim has the opposite effect from that intended (p. 128).
- The same holds for scientists, politicians and news. Jaynes says scientists agree quickly because their prior for deception is very low (an erroneous report only about once in a decade, by his estimate). On political matters he says it is always very high (pp. 128–129).
- **Log form** (comparing two people with different priors on a fixed $S$):
$$\log\frac{P(S|DI_A)}{P(S|DI_B)}=\log\frac{P(S|I_A)}{P(S|I_B)}+\log\Big[\frac{P(D|SI_A)\,P(D|I_B)}{P(D|I_A)\,P(D|SI_B)}\Big]\tag{5.22}$$
$$\log\text{posterior}=\log\text{prior}+\log\text{likelihood}\tag{5.23}$$
- This differs from Chapter 4's log-odds equations: there the hypotheses differ and prior information is shared, so the $P(D|I)$ factors cancelled. Here they do not cancel (p. 129).
- With $\log(\text{prior})>0$ (A the believer):
  - monotone convergence if $-\log(\text{prior})<\log(\text{likelihood})<0$ (5.24);
  - monotone divergence if $\log(\text{likelihood})>0$ (5.25);
  - convergence with reversal if $-2\log(\text{prior})<\log(\text{likelihood})<-\log(\text{prior})$ (5.26);
  - divergence with reversal if $\log(\text{likelihood})<-2\log(\text{prior})$ (5.27).
- So probability theory appears to allow, in principle, a single $D$ to have every conceivable effect on their relative states of belief (p. 129).
- **Drug scenario** (monotone cases). $D$: Mr N claims on TV that a common drug is unsafe. Viewers A, B, C have priors that the drug is safe $P(S|I)=(0.9,0.1,0.9)$. All agree that if the drug were unsafe N would say so: $P(D|\bar SI)=(1,1,1)$. Probability that N says "unsafe" when the drug is safe: $P(D|SI)=(0.01,0.3,0.99)$ (p. 130).
- Using $P(D|I)=P(S|I)P(D|SI)+P(\bar S|I)P(D|\bar SI)$, posteriors for safety are $(0.083,0.032,0.899)$ (p. 130). (added step for A: $0.9\times0.01/(0.009+0.1)=0.0826$.)
- Reported evidence changes (Jaynes's verbal reasoning for each viewer): A lowered by 20.0 db; B strengthened by 5.3 db; C essentially unchanged (printed as 0.005 db; see Reading notes) (p. 130).
- A and B converge; A and C diverge although they have the same prior (0.9). Jaynes says one cause of divergence is not merely that priors of deception are large but that they are greatly different between people (p. 130).
- **Divergence without differing trust.** Mr X and Mr Y agree about N: $P(D|SI_X)=P(D|SI_Y)=a$ and $P(D|\bar SI_X)=P(D|\bar SI_Y)=b$ (5.28). Their priors are $x,y$ (5.29). Posteriors:
$$P(S|DI_X)=\frac{ax}{ax+b(1-x)},\quad P(S|DI_Y)=\frac{ay}{ay+b(1-y)}\tag{5.30}$$
$$\log\frac{P(S|DI_X)}{P(\bar S|DI_X)}=\log\frac{x}{1-x}+\log\frac ab,\quad \log\frac{P(S|DI_Y)}{P(\bar S|DI_Y)}=\log\frac{y}{1-y}+\log\frac ab\tag{5.31}$$
- Both move the same amount, $\log(a/b)$, on the evidence scale, but on the probability scale they can converge or diverge (Exercise 5.2: find exact conditions for $|P(S|DI_X)-P(S|DI_Y)|>|P(S|I_X)-P(S|I_Y)|$, 5.32).
- Special cases: $a=b$ means N is useless and views are unchanged. $a>b$ means they distrust N so much that opinions move opposite to what he intended. $b\to0$ drives both to $P(S|D\cdot)=1$ regardless of prior (p. 131).
- Exercise 5.3: the exercise notes from (5.31) that X and Y, who share $a$ and $b$, can never reverse ranking, so a necessary condition for reversal in a more general setting is $a_x\ne a_y$ and/or $b_x\ne b_y$ (different opinions of N). It does not claim reversal is possible and asks the reader to find out (p. 131).
- **Diagnosis.** The conjecture (5.20) commits a subtle mind projection fallacy: treating "$D$ supports $S$" as an absolute property of the propositions, when it depends on prior information (p. 131).
- **Psychology.** Jaynes suggests people reason by a more sophisticated Bayesian inference than the psychologists had in mind (p. 132). Wason and Johnson-Laird (1972): subjects test "$A$ implies $B$" as if it meant "$B$ implies $A$" instead of "not-$B$ implies not-$A$".
- Jaynes sees a tendency toward Bayesianity here. If $P(B|AX)>P(B|X)$, Bayes' theorem gives $P(A|BX)>P(A|X)$ and also $P(\bar A|\bar BX)>P(\bar A|X)$. As $P(B|AX)\to1$, $P(A|BX)$ need not $\to1$ but $P(\bar A|\bar BX)\to1$, the syllogism (p. 132).
- He suggests the subjects may have been pursuing goals different from the psychologists' and that Darwinian selection gives grounds to expect Bayesian reasoning (p. 132).

*Intuition note.* Updating always shifts the log-odds by the log likelihood ratio, but whether that ratio favours $S$ depends on what each person believes about how the data were produced. Different readers can therefore move in different directions.

### 5.4 Visual perception — evolution into Bayesianity? (pp. 132–133)
- Ames (and Cantril) built demonstrations that make people misjudge size, shape and distance; the Ames room makes a child walking across it seem to double in height (pp. 132–133).
- Jaynes's interpretation: the brain forms assumptions in infancy (nearer objects look larger, etc.) and keeps them while they work. Seeing is inference from incomplete information, and the "failures" are reactions of the inference process to data inconsistent with its prior information, where an alternative hypothesis is resurrected (p. 133).
- Jaynes *expects* detailed analysis to match Bayesian inference, and expects natural selection to favour it. By Cox's theorems, denying that we reason in a Bayesian way is, he says, to assert that we reason in a deliberately inconsistent way (p. 133).

### 5.5 The discovery of Neptune (pp. 133–139)
- Scientists' reasoning consists largely of two syllogisms, strong (if $A$ then $B$; $B$ false; so $A$ false) and weak (if $A$ then $B$; $B$ true; so $A$ more plausible) (5.33). They correspond to Bayes' theorem in the forms
$$P(A|\bar BX)=P(A|X)\frac{P(\bar B|AX)}{P(\bar B|X)},\qquad P(A|BX)=P(A|X)\frac{P(B|AX)}{P(B|X)}\tag{5.34}$$
- The question is whether the weak form is a satisfactory quantitative version, using Pólya's example (p. 134).
- **History (as told).** Uranus (found 1781) deviated from Newtonian predictions. Jaynes says "Newton's theory is false" was already at perhaps −50 db, so an alternative at perhaps −20 db (an extra planet) was resurrected. Leverrier and Adams worked independently. Galle found Neptune within about one degree of the prediction on 23 September 1846 (p. 134).
- With $T$ = Newtonian theory and $N$ = the verified part of Leverrier's prediction:
$$P(T|NX)=P(T|X)\frac{P(N|TX)}{P(N|X)}\tag{5.35}$$
$$P(N|X)=P(N|TX)P(T|X)+P(N|\bar TX)P(\bar T|X)\tag{5.36}$$
- $P(N|\bar TX)$ is undefined until an alternative to Newton is specified (p. 135).
- If the only alternative allows no planet beyond Uranus, then $P(N|\bar TX)=0$ and $P(T|NX)=1$ whatever $P(T|X)$. If Einstein's theory is the only alternative, its prediction here is about the same as Newton's, so $P(N|\bar TX)=P(N|TX)$ and $P(T|NX)=P(T|X)$. The verification might lift Newton to certainty or have no effect, depending on the alternatives (p. 135).
- Example (Jaynes, a scientist's reply): the Zilch experiment supported Wilson's theory against Watson's, but not after Woffson's new theory fits the points exactly (p. 135).

**5.5.1 Alternative hypotheses (pp. 135–137).**
- Statisticians' ad hoc tests (chi-squared etc.) make no reference to alternatives. Jeffreys (1939): there is no use rejecting $H_0$ unless in favour of a definite alternative $H_1$ that fits better (p. 135).
- This concerns hypotheses about what is not directly observable. A direct error-free measurement confirming $x<y$ would prove it independently of alternatives (pp. 135–136).
- **Jaynes's claim from Bayes' theorem:** unless the observed facts are absolutely impossible on $H_0$, it is meaningless to ask how much they confirm or refute $H_0$ "in themselves". Probability theory ranks hypotheses relative to the alternatives specified and does not invent new ones. Mere improbability, however great, is not by itself a reason to doubt $H_0$ (p. 136).
- **Arbuthnot (1710):** more boys than girls in each of 82 years. Under $H_0$ ($p_{\rm boy}=1/2$) this has probability $2^{-82}=10^{-24.7}$ (−247 db). He saw "Divine Providence". Jaynes's criticisms (p. 136):
  1. $H_1$ = "Divine Providence" makes no definite predictions known to us, so $P(D|H_1)$ cannot be assigned. The mere denial $\bar H_0$ is also unusable.
  2. Any particular sequence has equally small probability under $H_0$, so the reasoning would reject $H_0$ whatever the data.
  3. $H_0$ also tacitly assumed independence between years. An exchangeable $H_{\rm ex}$ allowing positive correlation could give $P(D|H_{\rm ex})$ far above $2^{-82}$ (pp. 136–137).
- **Daniel Bernoulli (1734)** on planetary orbit poles: there is a clearly implied $H_0$ of chance (poles spread over the sphere) and $H_1$ of "attraction", and the evidence rather clearly favours $H_1$. **Laplace (1812)** on comets found their poles much more scattered and concluded comets are not "regular members" of the solar system. Jaynes calls this a correct application of probability theory to two fairly well-defined hypotheses (p. 137). Cournot's later attack is called a setback (footnote 4).
- Jaynes states that a formal significance test can always be interpreted as a test of $H_0$ against a specified class of alternatives (a generalisation of Eqs. 4.31–4.49). He says orthodox statistics never noticed this (p. 137).

**5.5.2 Back to Newton (pp. 137–139).**
- Jaynes infers from Pólya's numbers that Pólya had in mind one alternative $H_1$: one more planet exists and all directions are equally likely. A 1° cone covers $\pi/(57.3)^2\approx10^{-3}$ steradian, so
$$P(N|H_1X)\simeq10^{-3}/4\pi=1/13\,000$$
- Pólya did not distinguish $P(N|X)$ from $P(N|\bar TX)$. The ratio he computed was
$$\frac{P(N|TX)}{P(N|\bar TX)}=\frac{P(N|TX)}{P(N|H_1X)}\tag{5.37}$$
- By Chapter 4 this is the ratio of posterior to prior *odds* (of $T$), not of probabilities:
$$\frac{O(N|TX)}{O(N|X)}=\frac{P(N|TX)}{P(N|\bar TX)}=13\,000\tag{5.38}$$
(printed notation; see Reading notes). Hence, whatever $P(T|X)$, the evidence for Newton increased by $10\log_{10}13\,000=41$ db if $H_1$ is the only alternative.
- With $H_2$ (the new planet's orbit lies in the ecliptic plane and all longitudes are equally likely) the gain drops to about $10\log_{10}180=23$ db. Jaynes says any value between these extremes seems reasonable, since the problem is not unambiguously defined (p. 138).
- Pólya was bothered: a probability increase by 13 000 would imply a prior below 1/13 000, which contradicts Newton's well-established status. He took this as an inconsistency in Bayes' theorem. Jaynes says that seeing the factor as an *odds* factor removes the objection (p. 138).
- Jaynes adds that Pólya attended his 1956 Stanford lectures and by then understood the point (pp. 138–139).
- Conclusion (Jaynes): the situation is too complicated for quantitative Bayesian ranking of theories to be practical. It is also unnecessary, because the scientist's real difficulty is formulating new alternatives. There is no formal theory of "optimal hypothesis formulation" (p. 139).
- Exercise 5.4 extends the story to Pluto (p. 139).

*Intuition note.* "Confirms Newton" has no number until you say confirms it against what. The 41 db figure is a gain in evidence against one stated alternative, not a probability.

### 5.6 Horse racing and weather forecasting (pp. 140–142)
- **RCJ (Richard C. Jeffrey, 1983)** is quoted via Jaynes. With uncertain new information (probability $q$ for $B$ rather than 1), Bayes' theorem (5.39) $P(A|BI)=P(A|I)P(B|AI)/P(B|I)$ is said to be insufficient. RCJ proposes
$$P(A)_J=q\,P(A|BI)+(1-q)\,P(A|\bar BI)\tag{5.40}$$
- **Jaynes's reply:** if you do not accept $B$, why use it in Bayes' theorem? (5.40) does not follow from the rules of probability unless $q=P(B|I)$, but then $P(A)_J=P(A|I)$ and there is no updating. Because many different things could all give the same $q$, it violates desideratum (1.39b): it uses only the part of the information that bears on $B$ (p. 140).
- **Jaynes's fix:** the information actually received is a proposition $C$ with $P(B|CI)=q$. Bayes' theorem conditional on $C$:
$$P(A|CI)=P(A|I)P(C|AI)/P(C|I)\tag{5.41}$$
$$P(A|CI)=P(AB|CI)+P(A\bar B|CI)=P(A|BCI)P(B|CI)+P(A|\bar BCI)P(\bar B|CI)\tag{5.42}$$
$$P(A|CI)=q\,P(A|BCI)+(1-q)P(A|\bar BCI),\quad q\equiv P(B|CI)\tag{5.43}$$
- (5.43) resembles (5.40) but equals it only if $P(A|BCI)$ and $P(A|\bar BCI)$ are independent of $C$. That is the logic flow $(C\to B\to A)$ (5.44) rather than also $(C\to A)$ (5.45). In that case RCJ's rule is the Bayesian result. In general (5.40) loses information in $C$ that bears directly on $A$ (p. 141).
- Analogy: moonlight (reflection only) versus direct sunlight. Jaynes says that, as he will show in the maximum-entropy discussion, this is more than a loose analogy: conditional information flow is in almost exact mathematical correspondence with the Huygens principle of optics (p. 141, a claim about later chapters).
- **Horse scenario** ($A$ = my horse wins, $B$ = track muddy, $I$ = background knowledge, $C$ = forecaster showed a map and announced probability $q'$ of rain): $C$ may affect $A$ other than through mud, e.g. glare for the jockey, or a rival that runs poorly on cloudy days. The full solution is far more complicated than (5.40) and depends on more than $q$ (p. 142).
- Exercise 5.5 asks whether $P(A|BI)\to P(A|CI)$ as $q\to1$ (p. 141).

**5.6.1 Discussion (pp. 142–143).** Jaynes's views:
- Everyday problems may be so complicated that full Bayesian analysis is impractical. Bayes' theorem is still the normative principle (p. 142).
- Generations of workers, he says, have made persistent attempts to replace it with intuitive ad hockeries; on analysis these prove satisfactory only where they agree with Bayes' theorem (pp. 142–143).
- After about 40 years of applying it to thousands of problems he has found no unsatisfactory result. Surprising results needed some meditation to be seen as correct (p. 143).
- He concludes that strict use of the rules of probability as extended logic is "the only sound way to conduct inference", and that failure to follow them causes errors, paradoxes and controversies (p. 143). He compares this with the wasted effort at squaring the circle (p. 143).

### 5.7 Paradoxes of intuition (pp. 143–144)
- **Hempel's paradox:** it starts from the premise that a case of a hypothesis supports the hypothesis. The argument then says that the hypothesis that all crows are black is logically equivalent to the statement that all non-black things are non-crows, and that this is supported by observing a white shoe; Jaynes calls the conclusion intolerable (p. 143).
- Jaynes: the premise is not generally true, and Hempel could not see this because he judged support without considering alternatives (pp. 143–144).
- **Good's counterexample (1967).** World 1: $10^6$ birds, 100 crows, all black. World 2: $2\times10^6$ birds, 200 000 black crows and 1 800 000 white crows. We see one bird, a black crow. The evidence for World 2 against World 1 is
$$10\log_{10}\frac{200\,000/2\,000\,000}{100/1\,000\,000}=30\ \text{db}\tag{5.46}$$
i.e. odds 1000:1. An instance of the hypothesis that all crows are black can count against it (p. 144).
- Hempel rejected the example as unfair background information (Jaynes's report) (p. 144).
- Jaynes's general remark: perhaps 100 such paradoxes and controversies arise from faulty intuition rather than faulty mathematics. Others discussed later: marginalisation paradox (Chapter 15) and harmful cases (Chapters 15, 17) (p. 144).

### 5.8 Bayesian jurisprudence (pp. 144–146)
- Murder in New York City, 10 million people, no other knowledge: $e(\text{guilty}|X)=-70$ db for any particular person (p. 144).
- Jaynes suggests perhaps +40 db as a conviction threshold, while allowing that a reader may think it should be higher. He argues, crudely, that this means not more than about one conviction in 10 000 is in error, and that releasing guilty men costs society more than a rare false conviction. This requires about 110 db of evidence from −70 db (pp. 144–145). (These are Jaynes's own claims.)
- **Motive:**
$$e(\text{guilty}|\text{motive})=e(\text{guilty}|X)+10\log_{10}\frac{P(\text{motive}|\text{guilty})}{P(\text{motive}|\text{not guilty})}\simeq-70-10\log_{10}P(\text{motive}|\text{not guilty})\tag{5.47}$$
- Here $P(\text{motive}|\text{guilty})\simeq1$. A motive is significant to the degree that innocent people would not have one (p. 145).
- If $N_m$ people have a motive:
$$P(\text{motive}|\text{not guilty})=\frac{N_m-1}{(\text{number of people in New York})-1}\simeq10^{-7}(N_m-1)\tag{5.48}$$
$$e(\text{guilty}|\text{motive})\simeq-10\log_{10}(N_m-1)\tag{5.49}$$
- The population cancels. (added step: $-70-10\log_{10}[10^{-7}(N_m-1)]=-70+70-10\log_{10}(N_m-1)$; for $N_m=2$ this is 0 db, and for $N_m=1$ the evidence is unbounded.) Jaynes says (5.49) stays right when $N_m$ is 1 or 2 (p. 146).
- Presence near the scene works the same way. Bayes' theorem tells which information is relevant even without numbers. Pólya's qualitative demonstrations suggested to Jaynes a deeper connection (p. 146).
- Footnote 5: the issue is an Aristotelian proposition (a fact). Cases like malpractice "reasonable judgment" are value judgments, deferred to Chapters 13 and 18 (p. 146).

### 5.9 Comments (pp. 146–147)
- **Misner's suggestion:** knowing a theory's limits of validity confirms it within them, so relativity should increase confidence in Newton, and thermodynamics in the caloric theory. Jaynes finds it attractive at first glance (p. 146).
- Jaynes's objections: no one has avowed that confidence rose because a theory was "overthrown". We trust momentum conservation because we know of *no* limits (p. 147).
- A speculative aside: combining $F=ma$ and $E=mc^2$ gives
$$F=(E/c^2)\,a\tag{5.50}$$
(added step: substitute $m=E/c^2$). Jaynes suggests, if "elementary" particles are extended structures, that $c$ sets how fast their parts communicate. Newtonian $F=ma$ might then hold only after a transient response time. He leaves the derivation as an exercise with a hint and says such a prediction might conceivably be tested (p. 147).
- He concludes that confidence in Newtonian theory depends on one's whole theoretical outlook. He says actual scientific practice involves instincts not yet analysed, and adds the sociology of science (p. 147).

### 5.9.1 What is queer? (p. 148)
Jaynes says applications now odd, notably Bayesian jurisprudence and more serious psychological tests, may become respectable and useful applications of tomorrow, and that future generations may regard Bayesian analysis as indispensable for them (p. 148).

## Toy example (our own, not from the text)
Three explanations of a report "X claims an astonishing result":
- $S$: result real. Prior $10^{-6}$. $P(\text{report}|S)=1$.
- $Dc$: deception. Prior $10^{-3}$. $P(\text{report}|Dc)=1$.
- $H_0$: honest report of ordinary chance. Prior $1-10^{-3}-10^{-6}=0.998999$. $P(\text{report}|H_0)=10^{-9}$.

**Naive version ($S$ vs $H_0$ only).** Priors $10^{-6}$ and $0.999999$. Products: $S$: $10^{-6}$; $H_0$: $0.999999\times10^{-9}\approx10^{-9}$. $P(S|\text{report})=10^{-6}/(10^{-6}+10^{-9})=1/1.001\approx0.999$.

**With deception.** Products: $S$: $10^{-6}$; $Dc$: $10^{-3}$; $H_0$: $0.998999\times10^{-9}\approx10^{-9}$. Sum $\approx0.001001001$.
- $P(S|\text{report})=10^{-6}/0.001001001\approx9.99\times10^{-4}$.
- $P(Dc|\text{report})=10^{-3}/0.001001001\approx0.999$.

Check: the ratio $S:Dc$ is $10^{-6}:10^{-3}=1:1000$ and does not depend on $P(\text{report}|H_0)$. Making the report even less probable under chance (say $10^{-12}$) pushes $H_0$ out, but the posterior of $S$ then only tends to $1/1001\approx9.99\times10^{-4}$, a ceiling set by the priors of $S$ and $Dc$ alone. This mirrors (5.13)–(5.15).

## Concepts
- [[bayes-theorem]] — update by likelihood ratio; used on reports, theories and testimony, always conditional on the information actually received (pp. 127, 134, 140).
- [[prior-distribution]] — prior information differs by person; this can make the same data support $S$ for one person and refute it for another (pp. 126–131).
- [[likelihood]] — $P(D|H)$; for hypotheses about reports it includes deception mechanisms (pp. 121, 123).
- [[posterior-distribution]] — result of (5.12)–(5.13); depends on the full hypothesis set (pp. 122–123).
- [[probability-as-extended-logic]] — Jaynes's view: the rules give consistent plausible reasoning from the information used, no more (p. 123).
- [[cox-theorem]] — cited to argue that non-Bayesian reasoning is deliberately inconsistent, and, separately, that Bayes' theorem is a valid theorem required by elementary desiderata of rationality and consistency (pp. 133, 142–143).
- [[relative-entropy-kl-divergence]] — Jaynes's $H(f,p)$, the entropy of the observed distribution relative to the expected one, in the likelihood $e^{nH}$ (p. 121). Under the canon, $-H$ is KL.
- [[exchangeability]] — $H_{\rm ex}$, an exchangeable sampling distribution allowing correlated years (p. 137).
- [[evidence-decibel]] (new) — evidence $=10\log_{10}$(odds), in db; used for −100 db, 41 db, 30 db, −70 db (pp. 120, 138, 144).
- [[device-of-imaginary-results]] (new) — Good's method for assigning a prior by imagining evidence to be received (pp. 119, 125–126).
- [[resurrection-of-hypotheses]] (new) — astonishing data revive more plausible alternatives rather than an extremely implausible hypothesis lying below them (pp. 120, 133–134).
- [[deception-hypothesis-testimony]] (new) — if deception is a priori more plausible than the claim, hearing the report counts against the claim rather than for it (pp. 123–124, 128).
- [[mind-projection-fallacy]] (new, term from the unit) — treating "$D$ supports $S$" as an absolute property rather than one relative to prior information (p. 131).
- [[alternatives-needed]] (new) — a theory cannot be tested in isolation unless data are impossible on it (p. 136).
- [[jeffrey-rule-critique]] (new) — Jaynes's critique of RCJ's weighted-average update (pp. 140–141).
- [[frequentist-vs-bayesian-inference]] — here: chi-squared and ad hoc tests criticised for ignoring alternatives (pp. 122, 135, 137).

## Canonical instances
- [[stewart-esp-experiment]] — 25.8 sd result and its likelihoods; why deception wins (pp. 120–124).
- [[neptune-discovery]] — resurrection of an alternative; 41 db vs 23 db (pp. 134–138).
- [[arbuthnot-sex-ratio]] — rejecting $H_0$ without a specified alternative (p. 136).
- [[bernoulli-laplace-orbit-tests]] — tests with implied alternatives that are acceptable (p. 137).
- [[drug-safety-divergence]] — Mr A, B, C; Mr X, Y; log-odds shift $\log(a/b)$ (pp. 129–131).
- [[ames-room-perception]] — vision as inference from incomplete data (pp. 132–133).
- [[rcj-horse-race-forecast]] — $C\to B\to A$ vs $C\to A$ (pp. 141–142).
- [[hempel-crows-good-worlds]] — instance can count against hypothesis; 30 db (p. 144).
- [[new-york-murder-motive]] — $-10\log_{10}(N_m-1)$ (pp. 144–146).
- [[wason-johnson-laird-implication]] — subjects confuse $A\Rightarrow B$ with $B\Rightarrow A$ (p. 132).

## Bridges (candidates)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$.
- [same-math] $P(N|X)=P(N|TX)P(T|X)+P(N|\bar TX)P(\bar T|X)$ (5.36) ↔ bayesian: marginal likelihood (evidence) as a prior-weighted average over hypotheses.
- [same-math] Evidence in db, $10\log_{10}$ odds ↔ information-theory: log-likelihood ratio in bits (change of log base).
- [structural-analogy] Logic flow $C\to B\to A$ with no direct $C\to A$ ↔ bayesian: chain in a causal DAG, $A\perp C\mid B$.
- [structural-analogy] Perception as inference with hypotheses resurrected when priors fail ↔ bayesian: rational analysis at the computational level.
- [structural-analogy] Polarisation from different trust in a source ↔ bayesian: different priors and likelihood models on the same data.
- [metaphor] Moonlight versus direct sunlight for information flow ↔ Huygens principle; Jaynes says later chapters will show an almost exact mathematical correspondence.

## Questions this raises
- When should one use a deception hypothesis explicitly, and how can its prior be estimated without using the data?
- In the "device of imaginary results", how robust is a −100 db figure to which alternative is imagined?
- How should several viewers' posteriors be combined when they disagree about the source's reliability?
- If new hypotheses cannot be derived by probability theory, can any formal account of hypothesis generation be built?

## Exercises worth doing
- Ex. 5.1 (p. 126) — apply Good's device to three propositions; builds feel for prior strengths in dB — difficulty: medium
- Ex. 5.2 (p. 131) — find exact conditions on $(x,y,a,b)$ for divergence on the probability scale — difficulty: medium
- Ex. 5.3 (p. 131) — decide whether reversal is possible with different opinions of N — difficulty: hard
- Ex. 5.4 (p. 139) — extend the Neptune analysis to Pluto and to a retracted datum — difficulty: hard
- Ex. 5.5 (p. 141) — does $P(A|BI)\to P(A|CI)$ as $q\to1$? — difficulty: medium

## Reading notes
- Printed page = pdf page − 30. The unit spans printed pp. 119–148.
- Running headers: "Part 1 Principles and elementary applications" and the chapter title.
- Page images were supplied only for some pages. On other pages (e.g. p. 132) the text layer drops overlines (negation bars). I restored them from context: on p. 132 the syllogism statement reads $P(\bar A|\bar BX)$.
- p. 130: the item for Mr C says "only 0.005 db". Computing $10\log_{10}0.99$ gives about −0.044 db, so the printed figure looks too small by a factor of about ten. I report the printed figure and flag it.
- p. 138, (5.38): the image prints $O(N|TX)/O(N|X)$. The surrounding text says it is a ratio of posterior to prior odds, so it presumably means the odds of $T$ given $N$ over the prior odds of $T$. I followed the text's description.
- The spelling "Cantril" (p. 132) vs "Cantrell" (p. 133) is inconsistent in the source.
- Numerical values such as $-0.008452$ and $e^{-313.6}$ are taken as printed; I did not recompute them.
- Direct quotations in the digest are kept to a few short phrases (the Laplace line and a few others).
