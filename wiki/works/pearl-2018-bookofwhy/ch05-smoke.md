---
id: pearl-2018-bookofwhy/ch05-smoke
work: pearl-2018-bookofwhy
unit: "Chapter 5 — The Smoke-Filled Debate: Clearing the Air"
pages: unknown (source pdf 157–176; printed numbers not visible)
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# The Smoke-Filled Debate: Clearing the Air

## L0 — One line
Lacking a formal theory of causation, scientists reached "smoking causes cancer" using many kinds of evidence and informal criteria, and a causal diagram later explained a leftover puzzle, the birth-weight paradox, as collider bias.

## L1 — The gist (≤ 120 words)
How did scientists show that smoking causes lung cancer when a randomized trial was impossible and skeptics (Fisher, Yerushalmy) blamed hidden confounders? Case-control and prospective studies built evidence. Cornfield's inequality showed that a confounder able to explain away the whole effect would have to be implausibly strongly linked to smoking. The 1964 surgeon general's committee then relied on informal "Hill's criteria", which each have exceptions. The authors say these were a historical success but inadequate as a method. Later, the birth-weight paradox, where smoking seemed to help low-weight babies, stayed unexplained for decades. A causal diagram shows it is collider bias. The lesson: causal models let us use scientific knowledge beyond RCTs.

**Prerequisites:** correlation vs causation; confounder (a hidden common cause of two variables); randomized controlled trial, RCT (people randomly assigned to treatment or control); case-control study (compares sick people with healthy controls, looking backward); prospective study (follows people forward in time); risk ratio (risk in one group divided by risk in another); collider (a variable with two arrows pointing into it); conditioning on a variable (looking only at cases with a given value of it); conditional probability; reading arrows in a diagram.

## L2 — Key ideas (5–10 bullets)
- Early medical discoveries (scurvy, cholera) had a one-to-one link between cause and effect (the cholera bacillus is necessary and sufficient; vitamin C deficiency is too, given enough time). Smoking and cancer broke this simple picture (pdf 158).
- Observational evidence stacked up: a time series, case-control studies, prospective studies and a dose-response pattern. Time series are poor evidence, case-control studies can be biased, and skeptics still rejected the prospective studies (pdf 162–164).
- Cornfield's inequality showed that a confounder that fully explained the extra cancer risk would have to be at least as many times more common in smokers as the smoking risk ratio. The authors call it an early causal argument and the seed of sensitivity analysis (pdf 165–166).
- Tobacco companies deliberately promoted doubt. The authors also fault Fisher's obstinacy and his methods, which "impose ignorance" on the scientist (pdf 167–168).
- The 1964 committee's report was a public-health landmark. As a roadmap for future causal discovery, its guidelines (and Hill's criteria) were "uncertain and flimsy", with no method to weigh the evidence (pdf 169–171).
- Birth-weight paradox: smokers' low-weight babies survive better. A diagram explains it as collider bias from conditioning on birth weight (pdf 172–173).
- Even without the Birth Weight → Mortality arrow, the collider remains. Causal diagrams also help separate science from culture on charged topics such as race (pdf 174–175).

## L3 — Walkthrough

### Opening: the debate (pdf 157–159)
- Late 1950s–early 1960s: Yerushalmy (a skeptic) and Abe Lilienfeld (a proponent) argued within one family (pdf 157).
- The main argument against the hypothesis was possible unmeasured factors causing both craving for nicotine and lung cancer, i.e. confounding (pdf 158). This was before the do-operator existed (pdf 158).
- Lind (scurvy) and Snow (cholera) worked with one-to-one cause and effect: the cholera bacillus is necessary and sufficient. Smoking breaks this pattern: many smokers never get cancer, and some non-smokers do (pdf 158).
- A randomized controlled trial (RCT) was neither feasible nor ethical here (pdf 158).
- Fisher and Yerushalmy held the association was spurious, e.g. a "smoking gene". The onus fell on proponents to prove a negative (pdf 159).
- The 1964 surgeon general's report said smoking is causally related to lung cancer in men. The authors call the outcome a triumph but also a missed opportunity: scientists relied on informal guidelines (Hill's criteria), each with exceptions (pdf 159).

### Tobacco: a manmade epidemic (pdf 159–162)
- Cigarettes rose from 2% of the US tobacco market (1902) to 81% (1952), driven by automation and advertising (pdf 159–160).
- Lung cancer quadrupled in frequency between 1900 and 1950 and by 1960 was the most common male cancer (pdf 160).
- Figure 5.2: the lung cancer curve is almost a replica of the smoking curve, delayed about thirty years. The authors call time series poor evidence of causality. Roads, leaded fumes and air pollution were also plausible culprits (pdf 162).

### Doll and Hill, case-control and prospective studies (pdf 163–164)
- 1948: Hill, who had been chief statistician on the streptomycin RCT, proposed comparing diagnosed lung cancer patients with healthy controls. Interviewers were not told who was a case (pdf 163).
- Result: of 649 lung cancer patients, all but two had smoked. They calculated odds against this by chance of 1.5 million to 1. Patients were heavier smokers on average but fewer said they inhaled (pdf 163).
- Drawbacks of case-control studies (pdf 163):
  - They are retrospective: they give P(smoker | cancer), not the P(cancer | smoker) that matters to a would-be smoker.
  - Recall bias: patients know their diagnosis.
  - Selection bias: hospital patients are unrepresentative.
- Nineteen case-control studies agreed. Fisher's reply (1957): repeating a biased study does not remove its bias (pdf 164).
- From 1951, Doll and Hill followed 60,000 British physicians forward. In five years heavy smokers had a lung-cancer death rate 24 times that of non-smokers. The American Cancer Society study found 29 times for smokers and 90 times for heavy smokers. Quitting halved the risk (pdf 164).
- This is a dose-response effect: if A causes B, then usually (not always) a larger dose gives a stronger response (pdf 164).
- Skeptics still objected: smokers self-select and may differ "constitutionally" (e.g. risk taking). This was almost untestable. After the genome was sequenced in 2000, genes linked to lung cancer were found, so Fisher was right "in a very limited way" (pdf 164).

### Cornfield's inequality (pdf 165–166)
- Cornfield, with Lilienfeld (1959), attacked the constitutional hypothesis mathematically (pdf 164–165).
- Suppose a confounder (e.g. a smoking gene) fully accounted for smokers' extra risk. If smokers have nine times the cancer risk, the confounder must be at least nine times more common among smokers (pdf 165).
- Authors' numbers: if 11% of non-smokers have the "smoking gene", 99% of smokers would need it. If even 12% of non-smokers have the "cancer gene" (as printed), it becomes mathematically impossible for it to explain the association fully (pdf 165).
- The authors call this a causal argument in embryonic form. It gives a criterion for adjudicating between Diagram 5.1 (the gene cannot fully explain the association) and Diagram 5.2 (it fully explains it). The diagram contents are not in the text layer (pdf 165–166).
- It also planted the seeds of sensitivity analysis: instead of assuming a causal link is absent, ask how strong it would need to be to explain the data, then judge plausibility (pdf 166).
- Extending this to models with more than three or four variables needs graphical tools (pdf 166).
- *Intuition note:* A hidden cause that is to explain the whole risk ratio must be far more common among smokers than non-smokers (at least as many times more common as the ratio). Cornfield turned "maybe a hidden factor" into a number that could be judged.
- "Only statistical" criticism: by that standard sailors would have kept dying of scurvy until the 1930s. Laboratory evidence also appeared (tar on rats, benzopyrenes in smoke) (pdf 166).

### Denialism (pdf 166–168)
- Tobacco company researchers privately accepted the link (e.g. Teague, 1953), while the 1954 "Frank Statement" denied harm. A front group, the Tobacco Industry Research Committee, avoided the central question. Fisher and Yerushalmy were paid consulting fees (pdf 166–167).
- Fisher fixed on the inhaling result, which barely reached significance and was never replicated. The authors say it is very unlikely tobacco money corrupted him: "His own obstinacy was sufficient" (pdf 167–168).
- In a 1960 poll only a third of US doctors agreed smoking was a major cause of lung cancer (pdf 168).
- The authors' diagnosis: Fisher was right to promote RCTs, but his methods assume the experimenter has no prior knowledge. A causal model instead leverages scientific knowledge, and the community lacked a definition of "cause" without an RCT (pdf 168).

### The surgeon general's commission and Hill's criteria (pdf 168–171)
- The committee had five smokers, five non-smokers, two industry-suggested members, and nobody who had taken a public stance. William Cochran was the statistician (pdf 169).
- Report (probably Cochran): statistical methods cannot prove causality; causal significance is a matter of judgment, using several criteria, none all-sufficient (pdf 169).
- Five criteria: consistency, strength of association (including dose-response), specificity, temporal relationship, coherence (pdf 169–170).
- In 1965 Hill added four more (nine in all). He called them "viewpoints", none a sine qua non (pdf 170).
- The authors' objections (pdf 170):
  - Consistency: thirty studies can all ignore the same confounder.
  - Strength: children's shoe sizes strongly track reading aptitude without causing it.
  - Specificity: fits infectious disease less well than environmental exposure; smoking also raises other diseases.
  - Temporal order: a rooster's crow always precedes sunrise but does not cause it.
  - Coherence: theories and lab findings are sometimes overturned.
- The criteria came with no method to implement them; apparently each scientist just decides for him- or herself, and gut decisions can be wrong (pdf 170).
- Public-health outcomes: warning labels within two years, 1971 broadcast ad ban, and smoking among US adults falling from 45% (1965) to 19.3% (2010). Some committee members changed their smoking habits (Terry, Schuman), Cochran did not, and Fieser got lung cancer (pdf 171).
- Authors' verdict: a landmark for public health, "at best a modest success" for causality. Hill's criteria are best read as a historical document (pdf 171).

### Smoking for newborns: the birth-weight paradox (pdf 172–174)
- Yerushalmy's data (15,000+ children, from 1959) showed (pdf 172):
  - Babies of smokers weighed 7 ounces less on average.
  - Yet low-birth-weight babies of smokers survived better than low-birth-weight babies of non-smokers.
- Low birth weight means under 5.5 pounds; such infants had a death rate more than twenty times higher than normal-weight infants (pdf 172).
- Yerushalmy wrote cautiously that the findings "argue against" smoking interfering with fetal development; the authors sum this up as no causal path from Smoking to Mortality. Most modern epidemiologists believe smoking does raise neonatal mortality (pdf 172).
- Explanation (pdf 173): the chain is Smoking → Low Birth Weight → Mortality, plus other causes of low weight (e.g. serious genetic abnormalities) that are much more harmful.
  - A smoking mother explains away the low weight and lowers the likelihood of a birth defect.
  - A non-smoking mother makes a defect more likely and the prognosis worse.
- Figure 5.4 (from the image): arrows Smoking → Birth Weight, Smoking → Mortality, Birth Weight → Mortality, Birth Defect → Birth Weight, Birth Defect → Mortality (pdf 173).
- The collider is Birth Weight. Looking only at low-weight babies conditions on it. This opens the noncausal path Smoking → Birth Weight ← Birth Defect → Mortality, creating spurious correlation that makes smoking look beneficial (pdf 173).
- *Intuition note:* Among light babies, a known cause (smoking) makes the dangerous cause (defect) less likely. So the smokers' light babies look healthier, though smoking itself hurts.
- Epidemiologists argued for forty years; VanderWeele's 2014 article gives this explanation. The narrator ("I") says he is "absolutely convinced" it took so long because the language of causality was not available from 1960 to 1990; the paradox was not satisfactorily explained until 2006 (pdf 172). The authors say the diagram is probably too simple but collider bias is robust, and they suggest many cases of collider bias may go undetected because the bias does not conflict with theory (pdf 173–174).

### Passionate debates: science vs. culture (pdf 174–175)
- Wilcox asks whether low birth weight directly causes mortality; the association might be entirely confounded. Even if the arrow Birth Weight → Mortality is deleted, the collider remains, so the paradox is still explained (pdf 174).
- The same paradox appears for black mothers vs white mothers. Smoking can be stopped; race cannot, so the aim should be to address societal causes (pdf 174).
- Many advocates for racial justice treated birth weight as a proxy for infant mortality (Race → Birth Weight → Mortality). Wilcox was accused of racism in the 1970s and published only in 2001. A commentator, Richard David, wrote of the difficulty of being neutral (pdf 174–175).
- Authors' view: cultural shocks from science are settled by cultural realignment, not concealment. Separate science from culture early; causal diagrams allow dispassion (pdf 175).

## Toy example (ours, not from the text)
**Cornfield-style check.** Smokers' lung-cancer risk is 9 times non-smokers'. Say 8% of non-smokers carry a hidden gene. To explain the whole risk ratio, at least $9 \times 8\% = 72\%$ of smokers would need it. At 12% it would need $9 \times 12\% = 108\% > 100\%$, which is impossible.

**Collider bias.** 1000 babies: 500 smoker, 500 non-smoker mothers. Assume 10% have a birth defect in each group, so 50 per group, independent of smoking. All defect babies are low weight. Among non-defect babies, 40% of smokers' babies are low weight and 0% of non-smokers'. Mortality: defect 60% for both groups; non-defect 3% (smokers) vs 2% (non-smokers).

- Smokers, low weight: 50 defect + $0.4 \times 450 = 180$ non-defect = 230 babies. Deaths: $50 \times 0.6 + 180 \times 0.03 = 30 + 5.4 = 35.4$. Rate: $35.4/230 \approx 15.4\%$.
- Non-smokers, low weight: 50 defect only. Deaths: $50 \times 0.6 = 30$. Rate: $30/50 = 60\%$.
- Among low-weight babies, smokers look far better (15.4% vs 60%).
- Overall: smokers $(30 + 450 \times 0.03)/500 = 43.5/500 = 8.7\%$; non-smokers $(30 + 450 \times 0.02)/500 = 39/500 = 7.8\%$. Smoking is harmful, and conditioning on low weight hid this.

## Concepts
- [[randomized-controlled-trial]] (new) — comparing randomly assigned treatment and control groups; an excellent way to establish causation, but neither feasible nor ethical for smoking (pdf 158)
- [[confounding-vs-selection-bias]] — confounding is a hidden common cause (the smoking gene); selection bias comes from a non-representative sample (pdf 158, 163)
- [[case-control-study]] (new) — retrospective comparison of people with a disease to controls; gives P(smoker | cancer), with recall and selection bias (pdf 163)
- [[dose-response-effect]] (new) — a larger dose of the cause usually, not always, gives a stronger effect (pdf 164)
- [[cornfield-inequality]] (new) — a confounder that fully accounted for the extra risk would have to be at least as many times more common in the exposed as the risk ratio (pdf 165)
- [[sensitivity-analysis]] (new) — ask how strong an omitted causal link must be to explain the data, then judge plausibility (pdf 166)
- [[hills-criteria]] (new) — nine informal "viewpoints" for judging causality; none is necessary or conclusive (pdf 169–170)
- [[fork-chain-collider]] — collider: a variable with two arrows into it; conditioning on it opens a spurious path (pdf 173)
- [[explaining-away]] (new) — in the example, learning that a mother smokes explains away a baby's low weight and lowers the likelihood of a birth defect (pdf 173)

## Canonical instances
- [[smoking-lung-cancer-debate]] — the observational case for causation without an RCT (pdf 157–171)
- [[birth-weight-paradox]] — collider bias from conditioning on birth weight (pdf 172–174)
- [[doll-hill-studies]] — case-control (649 patients) and prospective (60,000 physicians) designs (pdf 163–164)
- [[monty-hall-paradox]] — only a figure caption at the end of the unit; no discussion appears on these pages (pdf 176)

## Bridges (candidates)
- [structural-analogy] Cornfield's inequality ↔ Bayesian workflow: sensitivity checks on assumptions — vary an assumption to see how strong it must be to overturn the result.
- [structural-analogy] Collider bias ↔ Bayes' theorem/explaining away: learning one cause lowers belief in another cause of the same effect.
- [metaphor] Hill's criteria ↔ Cox's theorem/probability as extended logic: informal evidence-weighing versus a calculus that says how to weigh evidence.

## Questions this raises
- How can the strength of a hidden confounder be tested when the model has many variables?
- When we condition on a variable in real data, how can we tell it is not a collider?
- Which parts of Hill's criteria can be made precise using causal diagrams?
- How should a researcher handle findings with possible adverse social consequences?

## Reading notes
- Printed page numbers are not visible; all references use pdf pages 157–176.
- Diagrams 5.1 and 5.2 are not in the text layer or images supplied; their content is inferred only from the surrounding text.
- The text says "12 percent of nonsmokers happen to have the cancer gene"; it probably means the smoking gene. Reported as printed.
- Pdf 176 holds only a Monty Hall caption; the pages supplied contain no discussion of it.
- The text names four additional Hill criteria without listing them.
