---
id: mcgrayne-2011-theory/ch08-jerome
work: mcgrayne-2011-theory
unit: "8. Jerome Cornfield, Lung Cancer, and Heart Attacks"
pages: 108–118
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Jerome Cornfield, Lung Cancer, and Heart Attacks

## L0 — One line
Jerome Cornfield, a history graduate, used Bayes' rule to link case-control data to the risk among smokers, which helped advance the hypothesis that smoking causes lung cancer, and later became a Bayesian by conviction.

## L1 — The gist (≤ 120 words)
How can patient-history studies say anything about a person's risk, or about causes? Cornfield took the population rate of a disease as a prior (his starting probability). He combined it with the share of smokers among patients with and without the disease. This linked population risk to risk among smokers (1951). In 1959 he and five coauthors answered Fisher's alternative explanations for the smoking–cancer link. In the Framingham heart study, Bayes' rule gave a logistic risk function and identified the main cardiovascular risk factors (1962). Frequentist rigidity in drug trials then moved Cornfield from using Bayes as a tool toward treating it as a philosophy. Most other NIH statisticians did not follow him.

**Prerequisites:** percentages; conditional probability and Bayes' rule at high-school level; the idea of a controlled study.

## L2 — Key ideas (5–10 bullets)
- Hill and Doll's 1950 case-control study (people with and without a disease are interviewed about their past) found a strong smoking–lung cancer link, but it did not show that smoking causes lung cancer (p. 109).
- Case-control studies give the share of smokers among patients and controls, not the answer to the question people actually ask, "what is my risk?" (p. 111).
- Cornfield's 1951 Bayesian calculation, which used the population disease rate as its prior (starting probability), linked population risk to subgroup risk. This justified case-control studies as a way to measure strength of link, under certain conditions (pp. 111–112).
- Prospective studies in Britain and the US in the mid-1950s confirmed his judgment (p. 112).
- Fisher and Neyman objected. Cornfield's 1959 paper answered Fisher's hypotheses, including by arguing that a hidden genetic factor would have to be larger than anything ever seen (pp. 112–113).
- Bayes' rule with Framingham data gave a logistic risk function (a formula giving a person's probability of disease from risk-factor values) and four main cardiovascular risk factors (p. 115).
- Frequentist rules on stopping, monitoring and subgroups pushed Cornfield to Bayes as a philosophy (p. 116). NIH did not use Bayes for clinical trials until about 30 years later (p. 117).

## L3 — Walkthrough

**Lung cancer appears (pp. 108–109).** Lung cancer was rare before 1900 and uncommon in 1930. By 1952 it killed 321 people per million per year in England and Wales (p. 108). Suspected causes: better diagnosis, an ageing population, exhaust, asphalt tar, coal smog, cigarettes. Animal studies had not shown tobacco tar to be carcinogenic (carcinogenic = cancer-causing). A 1937 German study pointed tentatively at cigarettes (p. 108).

**Hill and Doll (p. 109).** Austin Bradford Hill brought randomization into medical research and showed that pertussis vaccine cut whooping cough cases by 78% (p. 109). With Richard Doll he interviewed patients with and without lung cancer in 20 London hospitals. Of 649 men with lung cancer, only 2 were nonsmokers. Heavy smokers' death rate was 20 times that of nonsmokers (p. 109). Wynder and Graham confirmed this in the US. The author calls it the first sophisticated case-control study of a noninfectious disease. It did not show that smoking causes lung cancer (p. 109).

**Cornfield's background (pp. 109–111).** He was the son of Russian Jewish immigrants. His only degree was a 1933 B.A. from NYU. He worked as a government statistician and took his only statistics courses at the USDA Graduate School, whose director Deming published Bayes' essay (p. 110). He moved to NIH in 1947 (p. 110).

**The 1951 Bayesian step (p. 111).**
- The studies gave percentages of smokers among people with and without cancer, not what share of smokers and nonsmokers develop cancer (p. 111).
- Prospective studies (follow groups forward) answer that directly but are costly and slow for rare diseases. Hill and Doll therefore used a retrospective study (start from patients, ask about the past) (p. 111).
- Cornfield used the population incidence of lung cancer as prior and combined it with NIH data on smoking among patients with and without lung cancer. Bayes' rule was the "bridge" between population risk and subgroup risk (p. 111).
- The author says he used Bayes as a "philosophy-free" calculation step, not yet as a philosophy (p. 111).

*Intuition note:* Case-control data run "backwards", from disease to exposure. Bayes' rule reverses the direction. With the overall disease rate, it turns "how many cases smoke" into "how many smokers get the disease".

**Effect on epidemiology (pp. 112–113).** The paper showed that, when subjects are carefully matched with controls, patient histories can help measure the strength of a link between a disease and its possible cause (p. 112). Prospective studies agreed. Hill and Doll followed 40,000 British doctors for five years. Hammond and Horn followed 187,783 New York men for over 3½ years. Heavy smokers were 22 to 24 times more likely to get lung cancer. They were also 42% more likely to get heart disease and 57% more likely to get circulatory disease, respectively (p. 112). The author notes that case-control studies would later help identify thalidomide as a cause of birth defects (1961, p. 112).

**Fisher's counterattack and Cornfield's reply (pp. 112–113).**
- **Fisher and Neyman (1955):** they pointed out (correctly, says the author) that tobacco could be associated with cancer without causing it. They argued that only controlled experiments could predict disease rates. Berkson joined them. The author notes Fisher was a tobacco-industry consultant (p. 112).
- **Fisher's two hypotheses:** lung cancer might cause smoking; or a latent genetic factor might cause both (p. 113).
- **Cornfield's 1959 paper (with five coauthors):** if smokers were nine times as likely to get lung cancer, Fisher's genetic factor "must be even larger", which had never been seen (p. 113).
- On cancer causing smoking, he saw no evidence that cancer diagnosed after 50 began before 18, the median age of starting to smoke (p. 113).
- The gene would also have to show many other unobserved properties: more common among smokers, causing tumors on mouse skin but not on human lungs, and so on (p. 113).
- Cornfield wrote that a "continuously modified hypothesis" becomes hard to take seriously (p. 113).
- The author's reading: a single viable explanation probably marks the cause; alternatives mean it has probably not been found (p. 113).
- The 1964 surgeon general's report cited his work. The author says case-control studies are now epidemiologists' primary tool for likely causes of chronic disease (pp. 113–114).

**Heart disease and Framingham (pp. 115–116).** Cornfield helped design Framingham in 1948. He followed 1,329 men for a decade. 92 had myocardial infarction (heart attack) or angina (chest pain from the heart) (p. 115). Cross-tabulating risk factors fails: 10 factors at 3 levels give 59,049 cells. At 10 people per cell this needs about 600,000 people (p. 115). Cornfield used Bayes' rule with cardiovascular death rates as prior. He had two groups (died of heart disease or not) and seven risk factors per group. The posterior came out as a logistic regression function. It picked four main factors besides age: cholesterol, smoking, heart abnormalities, blood pressure (p. 115). No critical level of cholesterol or blood pressure separated safe from ill. People with both high were "23% more at risk" than those with both low (p. 116). The author dates Cornfield's identification of the critical risk factors to 1962 and links it to a 60% fall in cardiovascular death rates between 1960 and 1996 (p. 116).

*Intuition note:* Instead of reading a huge table, the model gives each person a probability of disease from their risk-factor values. It handles many factors at once.

**Conversion to a Bayesian philosophy (pp. 116–117).** Cornfield introduced Jeffreys's relative betting odds, now the Bayes factor: the probability of the data under one hypothesis divided by that under another (p. 116). In mouse drug screening, frequentist rules forced six more observations even after disproving results. They also barred interim monitoring, subgroup analyses and treatment switching (p. 116). Bayesian methods let him reject hypotheses after two solidly adverse observations (p. 116). He wrote that if the significance level blocked interim results, "so much the worse for the significance level" (p. 116). Most NIH statisticians stayed frequentist. NIH used Bayes for trials about 30 years later (p. 117). In one paper he proved, to the satisfaction of many Bayesians, that any procedure not stemming from a prior can be improved upon, according to frequency rules (p. 117).

**Later life (pp. 117–118).** He retired from NIH in 1967 and chaired statistics at George Washington University. He was American Statistical Association president in 1974 and died after pancreatic cancer diagnosed in 1979 (pp. 117–118). Other details: he used humour and an easygoing manner to reassure physicians and committees (p. 114); Savage thought many researchers were content to reap the benefits of Bayes' theorem without embracing the method, and Cornfield said Bayes' theorem "has come back from the cemetery" (p. 117); he consulted for the Army, the Department of Justice and others (p. 117).

## Toy example (ours, not from the text)
Assume a population with lung cancer incidence 0.001. Assume 90% of cancer cases smoke and 50% of non-cases smoke. The numbers are invented.
- P(smoker) = 0.9×0.001 + 0.5×0.999 = 0.0009 + 0.4995 = 0.5004.
- P(cancer | smoker) = 0.0009 / 0.5004 ≈ 0.0018.
- P(cancer | nonsmoker) = (0.1×0.001) / (0.1×0.001 + 0.5×0.999) = 0.0001 / 0.4996 ≈ 0.0002.
- Ratio ≈ 0.0018/0.0002 ≈ 9.

Case-control percentages plus the population rate give risk for smokers versus nonsmokers.

## Concepts
- [[bayes-theorem]] — used by Cornfield as a calculation linking population risk and subgroup risk (p. 111)
- [[prior-distribution]] — here the population incidence of disease, or cardiovascular death rates (pp. 111, 115)
- [[posterior-distribution]] — in Framingham, a logistic regression function giving risk (p. 115)
- [[frequentist-vs-bayesian]] — Cornfield saw frequentist trial rules as rigid (p. 116)
- [[case-control-study]] (new) — start from people with and without a disease; ask about the past (p. 109)
- [[prospective-vs-retrospective-study]] (new) — follow groups forward versus look back at patients (p. 111)
- [[bayes-factor]] (new) — probability of data under one hypothesis divided by that under another (p. 116)
- [[confounding-by-hidden-factor]] (new) — Fisher's latent genetic factor behind both smoking and cancer (p. 113)
- [[bayes-as-tool-vs-philosophy]] (new) — Cornfield's move from using Bayes for calculation to using it as foundation (pp. 111, 116)

## Canonical instances
- [[hill-doll-1950]] — 649 lung cancer men, only 2 nonsmokers (p. 109)
- [[cornfield-1951-risk-bridge]] — Bayes' rule from case-control data to risk (p. 111)
- [[fisher-genetic-factor-argument]] — Fisher's alternative hypothesis and Cornfield's reply (p. 113)
- [[framingham-heart-study]] — 1,329 men; four main risk factors (p. 115)

## Bridges (candidates)
- [structural-analogy] Fisher's hidden genetic factor ↔ causal inference: unmeasured confounder — it offers a non-causal reason for an association.
- [structural-analogy] Interim monitoring allowed under Bayes ↔ sequential updating — current results can be used without a fixed stopping plan.
- [structural-analogy] Bayes factor ↔ marginal-likelihood model comparison — both compare how well hypotheses predict data.

## Questions this raises
- Under what conditions can a case-control study give valid risk estimates? The text says only "carefully matched" (p. 112).
- How exactly does Bayes' rule yield a logistic regression function?
- Is Cornfield's size argument against a hidden genetic factor a general test for confounding?
- Why did most NIH statisticians stay frequentist (p. 117)?

## Reading notes
- Printed page = pdf − 15.
- No equations appear. The text layer is readable but uses ligature characters (e.g. "ﬁ").
- Footnote numbers appear in the text. The notes themselves are not in these pages.
- p. 111 says "the Hill and Wynder studies". Context suggests the Hill–Doll and Wynder–Graham studies (p. 109).
- The "23% more at risk" figure (p. 116) is as printed. The text does not say how it is measured.
