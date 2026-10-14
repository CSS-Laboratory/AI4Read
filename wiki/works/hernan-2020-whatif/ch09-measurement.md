---
id: hernan-2020-whatif/ch09-measurement
work: hernan-2020-whatif
unit: "9 Measurement bias and “Noncausal” diagrams"
pages: 125-136
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Measurement bias and “Noncausal” diagrams

## L0 — One line
Even without confounding or selection bias, measuring variables with error can bias effect estimates, and a DAG arrow only has causal meaning if a well-defined intervention exists for it.

## L1 — The gist (≤ 120 words)
Earlier chapters implicitly assumed perfectly measured variables and arrows that all have a well-defined causal meaning. This chapter makes both assumptions explicit and asks what happens when they fail. First, it asks how mismeasured treatment, outcome, confounders or colliders break the link between association and causation. It classifies measurement error as independent or dependent, and differential or nondifferential. Second, it asks what an arrow means for a variable such as obesity, where no well-defined intervention exists. Such DAGs are "noncausal". They can still give the right adjustment set, but they can also mislead. The chapter matters because exchangeability, positivity and consistency are not enough once variables are mismeasured, and because arrows without well-defined interventions can give false confidence.

**Prerequisites:** causal DAGs, d-separation, colliders, backdoor paths, exchangeability, confounding versus selection bias (Chapters 6–8), and counterfactuals for well-defined interventions (Chapter 3).

## L2 — Key ideas
- Measurement bias (information bias) is a change in the treatment–outcome association caused by how data are measured. It can occur in randomized and observational studies (p. 125).
- With only mismeasured $A^*$ and $Y^*$, exchangeability, positivity and consistency are not enough to compute the causal effect (p. 126).
- Measurement error has no single structure. It is classified by independence (of errors in $A$ and $Y$) and nondifferentiality (errors unrelated to the other variable), giving four types (pp. 126–127).
- Bias is not always toward the null. In general, measurement error results in bias. A notable exception is no $A$–$Y$ association with independent nondifferential error (p. 128). Fine Point 9.2 gives another setting where a mismeasured confounder causes no bias (p. 130).
- A mismeasured confounder generally cannot block the backdoor path, and can create apparent effect modification. A mismeasured collider, when conditioned on, generally introduces selection bias (pp. 129–130).
- Mismeasured confounders are harmless when the data contain as much information as the decision makers used (p. 130).
- An arrow out of a non-intervention variable like obesity has no causal interpretation. Such a DAG is "noncausal" (p. 132).
- A noncausal DAG may give the right identifying formula (Figure 9.13), but it may also give false confidence (Figure 9.15 versus 9.16) (pp. 133–134).

## L3 — Walkthrough

### Introduction (p. 125)
- Example: a randomized experiment asks whether the investigator's looking up makes other pedestrians look up. Confounding is not expected (randomization) and no selection bias was expected (all responses recorded). The collaborator, however, recorded half of the "looked up" responses as "did not look up" (p. 125).
- So even a strong true effect gives a diluted association between treatment and the *mismeasured* outcome (p. 125).
- **Definition:** *measurement bias* is when the treatment–outcome association is weakened or strengthened by the process by which study data are measured. It can arise under any study design (p. 125).

### 9.1 Measurement error (pp. 125–126)
- Earlier chapters implicitly assumed perfect measurement. Here the measured treatment is $A^*$, which need not equal the true $A$. Psychologists call $A$ the "construct" and $A^*$ the "measure" or "indicator" (p. 125).
- Figure 9.1: $A\to Y$, $A\to A^*$, $U_A\to A^*$. $U_A$ stands for all other factors determining $A^*$. The *measurement error* of $A$ is the difference between $A^*$ and $A$ for an individual. Its size and direction are determined by $U_A$ (pp. 125–126).
- $U_A$ is not strictly necessary on the DAG, because it is neither a shared cause nor conditioned on. It is drawn to show the error's source explicitly (p. 126). For discrete variables, measurement error is called *misclassification* (p. 126).
- Figure 9.2 adds $Y^*$ with $U_Y\to Y^*$ and $Y\to Y^*$. It has no confounding or selection bias, so association is causation for the true $A$ and $Y$. For instance, the associational risk ratio $\Pr[Y=1|A=1]/\Pr[Y=1|A=0]$ equals the causal risk ratio $\Pr[Y^{a=1}=1]/\Pr[Y^{a=0}=1]$ (p. 126).
- Earlier chapters implicitly assumed perfectly measured $A$ and $Y$. If only $A^*$ and $Y^*$ are available, $\Pr[Y^*=1|A^*=1]/\Pr[Y^*=1|A^*=0]$ will generally differ from the causal risk ratio. This is measurement bias, also called information bias. Exchangeability, positivity and consistency are then insufficient to compute the effect (p. 126).

**Technical Point 9.1 (p. 126).** Define $e_A = A^*-A$ and $e_Y = Y^*-Y$, with $f(\cdot)$ a probability density function.
- Independent errors: $f(e_Y,e_A)=f(e_Y)f(e_A)$.
- $e_A$ nondifferential: $f(e_A\mid Y)=f(e_A)$.
- $e_Y$ nondifferential: $f(e_Y\mid A)=f(e_Y)$.

*Intuition note:* "Independent" asks whether the two errors are related to each other. "Nondifferential" asks whether an error depends on the true value of the *other* variable.

### 9.2 The structure of measurement error (pp. 126–128)
- Confounding is common causes of treatment and outcome. Selection bias is conditioning on common effects. Measurement error has no single structure, so it is classified by independence and nondifferentiality (pp. 126–127).
- **Independent errors (Fig. 9.2).** By d-separation, $U_A$ and $U_Y$ are independent because the path between them is blocked by colliders ($A^*$ or $Y^*$). This is expected when data-entry errors in medical records occur haphazardly (p. 127).
- **Dependent errors (Fig. 9.3).** A common cause $U_{AY}$ of $U_A$ and $U_Y$. Example: retrospective phone interview where the person's ability to recall her history affects both $A$ and $Y$ measurements (p. 127).
- **Nondifferential** (Figs. 9.2, 9.3): $U_A$ is independent of the true $Y$, and $U_Y$ is independent of the true $A$ (p. 127).
- **Differential, treatment error (Fig. 9.4, arrow $Y\to U_A$).** Examples (p. 127):
  - Dementia as outcome with drug use recalled in interview. Dementia affects recall.
  - Alcohol in pregnancy recalled after delivery. The pregnancy outcome may affect recall. Both are called *recall bias*.
  - Blood drug levels used for $A^*$ and measured after liver toxicity is present. This is *reverse causation bias*.
- **Differential, outcome error (Fig. 9.5, arrow $A\to U_Y$).** Example: physicians who suspect the drug causes liver toxicity monitor treated patients more closely (p. 127).
- Figures 9.6 and 9.7 are both dependent and differential, which may result from combining the settings above (p. 127).
- **Four types:** independent nondifferential (9.2), dependent nondifferential (9.3), independent differential (9.4, 9.5), dependent differential (9.6, 9.7). The structure determines which correction methods can be used. A large literature exists for the independent nondifferential case (pp. 127–128).
- Correction methods generally rely on modeling assumptions plus validation samples (data subsets with key variables measured with little or no error). They are beyond the book's scope. The best defence is better measurement. Realistic DAGs need to represent confounding, selection and measurement together (p. 128).

**Fine Point 9.1 (p. 128): strength and direction of bias.**
- Measurement error in general results in bias. The notable exception is $A$ and $Y$ unassociated with independent nondifferential error. Without the $A\to Y$ arrow in Fig. 9.2, both the $A$–$Y$ and $A^*$–$Y^*$ associations are null (p. 128).
- In all other circumstances the $A^*$–$Y^*$ association may be further from or closer to the null than the $A$–$Y$ association (p. 128).
- Even under independent nondifferential error, non-extreme bias may reverse the *trend* for non-dichotomous ordinal and continuous treatments. This occurs when the conditional mean of $A^*$ given $A$ is a nonmonotonic function of $A$ (p. 128).
- Bias generally increases with the strength of the arrows $U_A\to A^*$ and $U_Y\to Y^*$. DAGs encode no quantitative information, so they cannot give the magnitude (p. 128).

*Intuition note:* Mismeasurement does not always shrink effects toward zero. The association may end up further from or closer to the null, and for non-dichotomous treatments the trend can even reverse when the mean of $A^*$ given $A$ is nonmonotonic in $A$.

### 9.3 Mismeasured confounders and colliders (pp. 128–129)
- Figure 9.8: $L$ (hepatitis history) $\to A$ (drug), $L\to Y$ (liver disease), $A\to Y$, $L\to L^*$. The backdoor path $A\leftarrow L\to Y$ is blocked by conditioning on the true $L$. Standardization or IP weighting then gives the causal risk ratio (p. 128).
- If only $L^*$ is available (e.g. self-reported by questionnaire), the backdoor path cannot generally be blocked by conditioning on $L^*$. The standardized or IP-weighted risk ratio based on $L^*$ will generally differ from the causal risk ratio. This is measurement bias (p. 129).
- Figure 9.9: confounding where $L$ is not the shared common cause ($U\to L$, $U\to Y$, $L\to A$). The backdoor path $A\leftarrow L\leftarrow U\to Y$ also cannot generally be blocked by conditioning on $L^*$ (p. 129).
- Alternative view: this is unmeasured confounding. Figure 9.8 is equivalent to Figure 7.8, with $L$ unmeasured and $L^*$ a surrogate confounder. The choice of terminology is irrelevant in practice (p. 129).
- **Apparent effect modification (author's example, p. 129).**
  - Everyone with $L^*=1$ truly has $L=1$. Half of those with $L^*=0$ have $L=1$.
  - Treatment has no effect on anyone (sharp null).
  - In stratum $L^*=1$ all have $L=1$, so there is no confounding by $L$ and no $A$–$Y$ association.
  - In stratum $L^*=0$, $L$ is mixed, so there is uncontrolled confounding and a non-null $A$–$Y$ association.
  - Investigators who naively read both as effect measures would conclude that $L^*$ modifies the effect, although no effect modification by the true $L$ exists.
- **Mismeasured collider (Fig. 9.10, equivalent to Fig. 8.2).** $A\to Y\to C$, $A\to C$, $C\to C^*$, with $C^*$ conditioned on. Conditioning on $C^*$ will generally introduce selection bias, because $C^*$ is a descendant of the collider $C$ and so a common effect of $A$ and $Y$ (pp. 129–130).

**Fine Point 9.2 (p. 130): when mismeasured confounders are not a problem.**
- Blood pressure $L$ affects antihypertensive therapy $A$ and stroke $Y$. Decisions use only the office measurement $L^*$ (p. 130).
- Figure 9.11: $L\to L^*\to A$, $L\to Y$. $L^*$ fully mediates $L$'s effect on $A$, so the backdoor path is blocked by either $L$ or $L^*$. Either is sufficient (p. 130).
- Figure 9.12 (more extreme): $U_1\to L$, $U_1\to Y$, $U_2\to L$, $U_2\to L^*$, $L\to L^*\to A\to Y$. The true $L$ is insufficient and $L^*$ is sufficient (p. 130). (added step) Conditioning on $L$ alone opens $A\leftarrow L^*\leftarrow U_2\to L\leftarrow U_1\to Y$, since $L$ is a collider on it. Conditioning on $L^*$ blocks every backdoor path.
- General point: effects are identifiable whenever the data hold as much information as the decision makers had, whether perfectly measured or not (p. 130).

*Intuition note:* In these examples, what matters is the information that actually drove treatment. If doctors acted only on $L^*$, then $L^*$ suffices to adjust for confounding (and in Fig. 9.12 the true $L$ does not).

### 9.4 Causal diagrams without mismeasured variables? (pp. 130–131)
- Earlier DAGs made two implicit assumptions. The first is that all variables are perfectly measured (p. 130).
- Measurement error of $A$ or $Y$ may induce a noncausal association between $A^*$ and $Y^*$ even when $A$ has a null effect and there is no confounding or selection bias. A mismeasured confounder may fail to block a path the true one would block (p. 130).
- Still, error may be judged too small to matter, and a DAG without the distinction may be simpler. If confounding and selection bias exist under perfect measurement, they will typically exist under error too, with exceptions (Fine Point 9.2) (p. 131).
- The book uses a 2-step approach: first draw DAGs without measurement error, then add measurement as an extra layer (p. 131).

### 9.5 Many proposed causal diagrams include noncausal arrows (pp. 131–133)
- Figure 9.13: $L\to A$, $L\to Y$, $A\to Y$. $A$ is antiviral treatment for COVID-19, $Y$ is death, $L$ is obesity (BMI above 30). No measurement error is assumed, so $L=L^*$ (p. 131).
- Treatment nodes have special status (Section 6.4). Quantitative causal inference needs well-defined counterfactuals $Y^a$, which need well-defined interventions on $A$. For antiviral treatment these exist, so the arrow $A\to Y$ is well defined (p. 131).
- For a non-intervention node like obesity, $Y^l$ is undefined unless well-defined ENDE interventions exist that change $L$ without directly affecting $Y$. The text says most experts would not accept that such interventions exist for obesity and mortality (Chapter 3 concept; ENDE not expanded in this unit). So the arrow $L\to Y$ cannot be assumed well defined (p. 131).
- **Arrow $L\to A$:** reasonable. Doctors treat obese patients upon learning they are obese. A well-defined intervention could present the physician with a patient whose BMI differs (p. 132).
- **Arrow $L\to Y$:** experts know obese patients are more likely to die. They cannot accept ENDE interventions for $L$ on $Y$, so this arrow has no causal interpretation for them (p. 132).
- The book restricts "causal DAG" to DAGs whose arrows all have causal interpretations. Figure 9.13 is therefore a "noncausal" diagram. The quotes remind the reader that many papers call such DAGs causal (p. 132).
- **A causal alternative (Fig. 9.14):** a hidden factor $H$ with $H\to L$, $H\to Y$, and $L\to A\to Y$. $H$ may include unmeasured, possibly unknown variables such as genetic and metabolic factors. $H$ affects $A$ only through $L$, which is reasonable if obesity is the only information used for decisions (pp. 132–133).
- The arrows $H\to L$ and $H\to Y$ have a causal interpretation if the experts are willing to assume that either (a) $H$ corresponds to a well-defined intervention, or (b) a well-defined ENDE intervention on $H$ exists that affects $L$ and $Y$ only through $H$. Current knowledge does not rule this out, so the arrows are "tentatively justified" and Fig. 9.14 is considered a causal diagram (p. 133).

**Fine Point 9.3 (p. 132): well-definedness depends on the outcome.**
- Puzzle: if we can intervene on $L$ to study $A$, why not use it to study $Y$?
- Resolution: $L$ was used for two concepts, (i) physical body weight and (ii) the weight perceived by the doctor. The well-defined intervention for $L$ on $A$ acts on (ii).
- Writing $L^*$ for the perception, the expanded DAG has a deterministic arrow $L\to L^*$ and a regular arrow $L^*\to A$. Intervening on $L^*$ while leaving $L$ unchanged gives the same doctor behaviour. So $A^l$ is well defined but $Y^l$ is not.

**Fine Point 9.4 (p. 133): "noncausal" diagrams with statistical interpretations.**
- For a DAG representing an FFRCISTG model (term not expanded here) where only $A$ has well-defined interventions and the variables' distribution factors according to the DAG, arrows need not be causal. They encode, via d-separation, conditional independencies. Then $L\to Y$ need not be removed in Fig. 9.13 (p. 133).
- **Richardson and Robins (2013) object:** if arrows have no causal interpretation, there is no reason to expect the variables' distribution to factor according to any (incomplete) DAG. This is worse with unmeasured $U$, because some independencies cannot be checked from observed data (p. 133).
- Example: the front door graph (Fig. 7.14) implies $Y\perp\!\!\!\perp A\mid M,U$. The text says many researchers might find it hard to imagine other reasons for postulating this than the belief that $A$ and $Y$ share a cause $U$ and $A$'s effect is fully mediated by $M$. That belief gives every arrow a causal interpretation (p. 133).
- **Alternative reading:** researchers skeptical that $M$-counterfactuals $Y^m$ exist can read Fig. 7.14 as the hypothesis $Y\perp\!\!\!\perp A\mid M$ in a future trial randomizing $A$. If it fails, the strong causal claim is falsified along with the structure (p. 133).

### 9.6 Does it matter that many proposed diagrams include noncausal arrows? (pp. 133–135)
- Figure 9.13 is causally wrong but adequate for the effect of $A$ on $Y$. Both Figs. 9.13 and 9.14 imply that conditioning on $L$ blocks all backdoor paths (p. 133).
- Reason: neither DAG has arrows from unmeasured variables into $A$. Adjusting for $L$ (standardization or IP weighting) is all the identifying formula needs. In both, the identifying formula is the same (pp. 133–134). The text says Fig. 9.13 "lacks the node $U$"; the missing node is $H$ (see Reading notes).
- In realistic settings expert knowledge is rarely good enough to draw a DAG with all components known. Many DAGs in health and social sciences are noncausal because they lack hidden variables $H$. Including a variable without well-defined interventions for its effect on its descendants declares the DAG noncausal (p. 134).
- **Misleading case.** Figure 9.15: $U\to L$, $U\to A$, $L\to Y$, $A\to Y$. If treated as causal, $L$ blocks the backdoor path. Figure 9.16 makes $L$ a surrogate of unknown $H$ ($U\to H$, $U\to A$, $H\to L$, $H\to Y$). There $L$ does not block the path. Investigators who propose Fig. 9.15 instead of 9.16 would wrongly conclude that $L$ suffices. We must check whether the measured variables are those with well-defined interventions (p. 134).
- General conclusion: a causal arrow $X\to Y$ cannot be meaningfully interpreted without well-defined interventions for $X$'s effect on $Y$. Blind acceptance of noncausal arrows may lead to incorrect conclusions. This scrutiny is unnecessary for an electrical circuit but indispensable in health and social sciences (p. 135).
- Well-definedness is fuzzy (Chapter 3): no intervention is perfectly well defined. For the rest of the book, except for sign-posted exceptions, all DAGs are assumed strictly causal. Each arrow has an intervention specified without meaningful vagueness given current knowledge. Beliefs may later prove wrong (p. 135).

**Fine Point 9.5 (p. 134): front door connection.**
- Figure 9.14 is the front door diagram (Fig. 7.14) with $L\to A$ in place of $A\to M$. So $\mathrm{E}[Y^l]$ is identified by the front door formula (Technical Point 7.4) with $L,l,l'$ for $A,a,a'$ and $A,a$ for $M,m$.
- If a direct $L\to Y$ arrow is added (e.g. unrecorded ancillary care for high $L$), $Y^l$ changes meaning. In the unmodified graph, $Y^l-Y^{l'}$ is the effect via $L\to A\to Y$. In the modified graph it is the total effect via both $L\to Y$ and $L\to A\to Y$. $\mathrm{E}[Y^l]$ is then not identified.
- The authors say it is true that the effect along $L\to A\to Y$ should remain identified by the front door formula. The proof is deferred to Chapter 23.

**Fine Point 9.6 (p. 136): from noncausal to causal diagrams.**
- Figure 9.17: $U\to A$, $U\to L$, $A\to L$, $L\to Y$, $A\to Y$. It is built from temporal order, $L$ associated with $Y$, and known unmeasured $U$ affecting $A$ and associated with $L$. $A$'s effect is not identifiable because $L$ is a descendant of $A$ (Fine Point 7.4) (p. 136).
- Since there are no well-defined interventions for $L$ on $Y$, they add hidden $H$ with $H\to Y$ and $L$ as surrogate of $H$ (Fig. 9.18). The effect is not identifiable, because $A\leftarrow U\to H\to Y$ cannot be blocked by any measured variable (p. 136).
- They kept $U\to A$ and redirected arrows into $L$ toward $H$. This implies that they believe $U$ and $A$ have well-defined effects on $H$, and that their effects on $L$ are fully mediated by $H$. Even if $L$ were a deterministic function of $H$, conditioning on $L$ would not block paths through $H$, because $H$ is not a deterministic function of $L$ (it is of higher dimensionality and complexity than $L$) (p. 136).
- This inheritance is not always warranted. In Fig. 9.19 $U$ has a direct effect on $L$ rather than on $H$. Then the effect of $A$ on $Y$ is identifiable, since no backdoor path is open. Here $L$ cannot be a deterministic function of $H$. Example: $U$ = physician's decision to order a test, $L$ = result, $H$ = biological determinants of the result (p. 136).

*Intuition note:* A causal arrow out of a variable needs well-defined interventions on that variable. Without them the arrow has no causal interpretation (under the "noncausal" reading it only encodes conditional independencies, p. 133). Whether that is harmless depends on whether the hidden causal structure leaves the adjustment set unchanged.

## Toy example (ours, not from the text)
Outcome misclassification (like the pedestrian example) with both missed cases and false alarms. Suppose a randomized experiment (no confounding, no selection bias). The true risks are $\Pr[Y=1|A=1]=0.4$ and $\Pr[Y=1|A=0]=0.2$, so the true risk ratio is $0.4/0.2=2$.
The recorder detects half of true events (sensitivity $0.5$) and wrongly records an event for 10% of non-events (specificity $0.9$). The error is independent of $A$, so it is nondifferential.
- $A=1$: $\Pr[Y^*=1|A=1]=0.5(0.4)+0.1(1-0.4)=0.20+0.06=0.26$.
- $A=0$: $\Pr[Y^*=1|A=0]=0.5(0.2)+0.1(0.8)=0.10+0.08=0.18$.
- Measured risk ratio $=0.26/0.18\approx1.44$, versus the true $2$.
Here the association is diluted toward the null. Check the null case: if both true risks are $0.3$, both measured risks are $0.5(0.3)+0.1(0.7)=0.22$, so the ratio is $1$. This matches the exception in Fine Point 9.1. This example shows dilution only for this dichotomous, independent nondifferential case. The text does not claim dilution in general (p. 128).

## Concepts
- [[measurement-bias]] (new) — association between treatment and outcome changed by how data are measured; also called information bias (pp. 125–126)
- [[measurement-error]] (new) — difference between measured and true value ($e_A=A^*-A$); called misclassification for discrete variables (pp. 125–126)
- [[independent-measurement-error]] (new) — errors of $A$ and $Y$ have a joint pdf equal to the product of marginals (p. 126)
- [[nondifferential-measurement-error]] (new) — error in one variable is independent of the true value of the other (pp. 126–127)
- [[surrogate-confounder]] (new) — a measured variable standing in for an unmeasured true confounder (p. 129)
- [[apparent-effect-modification]] (new) — stratum-specific differences caused by unequal mismeasurement of a confounder across strata of $L^*$ (p. 129)
- [[well-defined-intervention]] (new) — an intervention specified without meaningful vagueness; needed for counterfactuals and causal arrows (pp. 131, 135)
- [[noncausal-arrow]] (new) — a DAG arrow without well-defined interventions; a DAG with one is "noncausal" in this book's usage (p. 132)
- [[hidden-variable-causal-dag]] (new) — adding an unmeasured $H$ with causal arrows so a DAG compatible with known associations is causal (pp. 132–133)
- [[causal-dag]] — a DAG all of whose arrows have a causal interpretation, in this book's usage (p. 132)
- [[d-separation]] — used to show $U_A$ and $U_Y$ are independent (p. 127)
- [[fork-chain-collider]] — colliders $A^*$/$Y^*$ block the path between errors; a mismeasured collider conditioned on opens one (pp. 127, 129)
- [[confounding-vs-selection-bias]] — measurement is a third source of bias beside these two (pp. 127, 131)

## Canonical instances
- [[pedestrians-looking-up]] — outcome misclassification dilutes a randomized association (p. 125)
- [[statin-liver-disease-measurement]] — treatment $A$ and outcome $Y$ measured with error (pp. 125–127)
- [[recall-bias-dementia-pregnancy-alcohol]] — differential error, $Y\to U_A$ (p. 127)
- [[hepatitis-history-confounder]] — mismeasured confounder and apparent effect modification (pp. 128–129)
- [[blood-pressure-office-measurement]] — mismeasured confounder that is sufficient for adjustment (p. 130)
- [[obesity-covid-antiviral-dag]] — noncausal arrow $L\to Y$ and hidden $H$ (pp. 131–133)
- [[diagnostic-test-surrogate]] — $U$ affects the surrogate $L$ but not $H$ (p. 136)

## Bridges (candidates)
- [structural-analogy] Mismeasured confounder as surrogate for unmeasured confounder ↔ Bayesian latent-variable models: observed indicator of a latent true variable — both treat the data as noisy proxies of a hidden quantity.
- [metaphor] "Validation samples" for error correction ↔ Bayesian workflow: using small high-quality data to calibrate a noisy measurement model.
- [structural-analogy] Hidden factor $H$ making a DAG causal ↔ hierarchical models with latent parameters — both add unobserved variables to make the structure coherent.

## Questions this raises
- How do validation samples and modeling assumptions together correct independent nondifferential error (named but not covered, p. 128)?
- When does an unrecorded direct arrow (like $L\to Y$ in Fine Point 9.5) change identification, and when only the estimand's meaning?
- Can one test, from data, whether a measured variable is a surrogate rather than the true confounder?
- What is a path-specific effect, and how is it identified (promised for Chapter 23, p. 134)?

## Reading notes
- Page offset: printed = pdf − 9 (pdf 134–145 = printed 125–136). Page labels give printed numbers.
- Source is the online revision (per metadata); cross-references to later chapters (e.g. Chapter 23, Technical Point 21.12) may differ from older editions.
- Unexpanded terms: "ENDE interventions" (the text refers to Chapter 3 for the discussion) and "FFRCISTG" (p. 133) are not explained in this unit. I give only the author's usage.
- Likely misprints: p. 132 "the effect of L and Y" should read "of L on Y". Fine Point 9.6 (p. 136) says "effect of U and A" where "U on A" is meant. p. 133 says Fig. 9.13 "lacks the node U", but the missing node there is $H$ (Fig. 9.14).
- Equations are simple. All figures were checked against the page images.
