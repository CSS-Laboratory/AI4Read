---
id: mcgrayne-2011-theory/ch16-eureka
work: mcgrayne-2011-theory
unit: "16. Eureka!"
pages: 213–232
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 22
pipeline_version: 0.1
---
# Eureka! (Chapter 16: how MCMC made Bayes practical)

## L0 — One line
Bayes' rule became widely usable around 1990 when Gelfand and Smith showed that Markov chain Monte Carlo (MCMC) sampling can replace the impossible integrals, with cheap computers arriving at the same time.

## L1 — The gist (≤ 120 words)
Why was Bayes' rule so little used in the 1980s, and what changed? Data sets now had many unknowns, and Bayesian calculations were too heavy for the computers of the day. A few pioneers used Bayes anyway. Image researchers produced the Gibbs sampler. Gelfand and Smith saw that long chains of simple draws could replace one huge calculation; in 1989 Smith showed it fits almost any problem. Physicists had used Markov chains for decades; statisticians knew of them but had not used them. Free software (BUGS) then spread the method into many fields, such as ecology and genetics. The chapter argues that Bayes finally "worked", which changed practice even though philosophies of science had not changed.

**Prerequisites:** Bayes' rule (prior × likelihood → posterior); the idea of random sampling; what a probability distribution is.

## L2 — Key ideas
- By the 1980s data had many variables, and the resulting plague of unknowns was called the curse of high-dimensionality. Bayesian computation of any complexity was essentially impossible, and a common criticism was its "sheer impracticability" (Dawid). Bayesians were a small, beleaguered group (pp. 213–214).
- Early civilian successes show what Bayes could do: a diesel/cancer meta-analysis (combining the results of similar studies), abrupt change in coal-mine accident rates, and sociologists' model comparison (pp. 215–217).
- Image-restoration work led to the Gibbs sampler (1984), a Monte Carlo variant (computing by random sampling) made for images with many pixels. The Gemans worked in a small niche field, spatial statistics, and image-processing specialists adopted the sampler first (pp. 218–219).
- Gelfand and Smith's synthesis: replace hard integration with long Markov chains of easy low-dimensional draws (in a Markov chain each value depends only on the one before). Smith showed in 1989 that it applies to almost any statistical problem (pp. 220–222).
- The ingredients were old. Markov chains, Monte Carlo, Metropolis (1953) and Hastings (1970) were known, but statisticians had not used them (pp. 222–223).
- BUGS software (1991) caused the biggest jump in Bayesian popularity and spread the method across many fields (p. 226).
- Bayes had real effects in medical testing, device applications, diagnostic tools and wildlife management, though little on basic clinical research or practice. The author says that when evidence was weak, only Bayes built uncertainty into the analysis (pp. 226–231).
- The author's conclusion: it appeared that pragmatism could drive a paradigm shift; philosophies of science had not changed, but Bayes finally worked (p. 232).

## L3 — Walkthrough
The chapter has no numbered sections. I group it by topic, in the author's order.

### Crisis: data grow, computing is slow (pp. 213–215)
- The author says Bayes had survived five near-fatal blows: Bayes shelved it, Price's publication was ignored, Laplace later favored frequency theory, frequentists virtually banned it, and the military kept it secret (p. 213).
- By 1980 researchers entered data into mainframe terminals, with dozens of measurements per patient or wine. They needed to study many unknowns and their relations. Real data did not fit tidy bell curves (p. 213).
- The author calls the resulting plague of unknowns the "curse of high-dimensionality". (Our gloss: unknowns are the quantities still to be inferred.) (p. 213)
- Bayesians numbered about a hundred or more. The 1982 meeting "Practical Bayesian Statistics" was seen as an oxymoron. Dawid, its organizer, admitted that Bayesian computation of any complexity was essentially impossible then (p. 214).
- The curse hit frequentists too. Many statisticians confused old calculators with electronic computers. Bayesians were strong in business schools and economics, frequentists in statistics departments (p. 214).
- Lindley and Smith's hierarchies (breaking a process into stages) fell flat at first. The models were too specialized and stylized for many scientific applications, and it was another 20 years before Bayesian textbooks taught hierarchical models (p. 214).
- **Challenger.** An air-force contractor, Teledyne, used a Bayesian analysis with prior experience of 32 confirmed failures in 1,902 rocket motor launches. It estimated booster failure at 1 in 35; NASA's estimate was 1 in 100,000. Challenger exploded on 28 January 1986 (p. 215).
- The author does not know why the military accepted Bayes more readily. Many sources are still classified (p. 215).

### Early civilian successes (pp. 215–217)
- **Diesel and cancer (DuMouchel and Harris, 1983).** They used hierarchical Bayes to borrow information from mice, hamster cells and chemicals. They also included experts' opinions about how relevant non-humans and cigarette smoke are to humans and diesel smoke. They concluded that, even if light-duty diesels reached 25% market share over 20 years, lung-cancer risk for a typical urban resident would be negligible next to a pack-a-day smoker, whose risk was 420,000 times worse (pp. 215–216).
- **Coal mines (Raftery).** Earlier work assumed that accident rates changed gradually. Raftery compared models Bayesianly. He found that rates plummeted suddenly in the late 1880s or early 1890s. A historian suggested the cause: the Miners' Federation, formed in 1889 (p. 216).
- Frequentism worked well when one hypothesis was a special case of the other and both were gradual. It helped less when hypotheses competed and neither was a special case, especially with abrupt change (p. 217).
- Raftery's short 1986 paper hit sociology. Sociologists applied frequentist methods developed for 50–200 cases to data on thousands of individuals, and the results were often bizarre. Raftery argued that we should be comparing models. Bayesian hypothesis testing swept sociology and demography (p. 217).

*Intuition note:* The author says researchers really want to know which of their models is more likely to be true, given the data. Bayes seemed to give results closer to sociologists' intuition. Raftery's point was to compare models, not just look for discrepancies between one model and the data (p. 217).

### Images and the Gibbs sampler (pp. 217–219)
- Images from aircraft, MRI and telescopes were blurry, so restoring them was an inverse problem suited to Bayes (pp. 217–218).
- Hunt used Bayes on nuclear-test images at Los Alamos in 1973–74. Besag worked on epidemics in diseased tomato plants on pixel-like lattices. Grenander's group at Brown faced about a million unknowns (p. 218).
- Stuart and Donald Geman invented a Monte Carlo variant for many-pixel problems, named Gibbs sampler after the physicist J. W. Gibbs. They tried to handle a 64 × 64-cell image "whole", which produced too many unknowns for the computers of the day (pp. 218–219).
- They published in 1984 in a very difficult paper. Image-processing specialists adopted it, and statisticians outside spatial imaging later saw that more general versions were useful. It became the most popular Monte Carlo algorithm. Turchin had found it in 1971 in Russian journals, without computers, and this was overlooked (p. 219).
- By 1985 the Bayesian–frequentist argument was losing its zing. Shafer called it "calcified", and Diaconis found the field noncompetitive (p. 219).

### Smith builds the tools (pp. 219–222)
- Lindley called Bayes "turning the Bayesian crank". Smith saw that computational ease, not more polished theory, was the key. Lindley later called missing this a major mistake of his professional life (pp. 219–220).
- Smith helped translate de Finetti's *Theory of Probability* and got it published, and he developed filters. With Lindley, Bernardo and DeGroot he organized Bayesian conferences in Valencia, held regularly since 1979 (p. 220).
- His 1984 manifesto: efficient numerical integration is the key to more widespread use of Bayesian methods (p. 220).
- Gelfand visited Nottingham. Smith gave him a Tanner and Wong paper. Wong had been adapting the EM algorithm (an iterative method, first developed secretly, then published by Dempster and Laird in 1977) for Bayesians. Clayton pointed to the Gemans' paper. Gelfand then saw that Bayes, Gibbs sampling, Markov chains and iterations fit together (pp. 220–221).
- Gelfand's account: to learn about a distribution, take samples from it, but "don't sample directly". Look at simple distributions one at a time, each depending only on the preceding value. Break the problem into tiny easy pieces and do millions of iterations, replacing one high-dimensional draw with many low-dimensional ones. In his words, that is how to break the curse (p. 221).
- Smith showed in Quebec (June 1989) that MCMC could apply to almost any statistical problem. Bayesians could finally compute realistic priors, likelihoods and posteriors (pp. 221–222).

*Intuition note:* Instead of solving one enormous integral, you walk through the space with small, easy random steps. After enough steps, the visited points behave like samples from the posterior (my reading of Gelfand's account, p. 221).

### Why so late: the history of the machinery (pp. 222–224)
- Markov invented chains in 1906. Fermi computed them in his head and with an adding machine and did not publish. The author reports that, according to Good, wartime censorship kept them secret (p. 222).
- Mayer simulated neutrons with Markov chains on ENIAC. Metropolis named Monte Carlo and described it for statisticians in 1949. His detailed algorithm appeared in 1953 in a physics-chemistry journal, covering only particles in a square (pp. 222–223).
- Statisticians were advised several more times to use Monte Carlo (1954), and Lindley described Markov chains in 1965 in a student text. Hastings generalized Metropolis in *Biometrika* in 1970, but Bayesians ignored it. He left research and learned of the importance of his work after retiring in 1992 (p. 223).
- The Hastings–Metropolis algorithm gives estimates, not exact numbers. Many statisticians wanted exact answers (p. 223).
- Gelfand says they "stumbled on it". The author notes that timing mattered: cheap, fast desktop computers had just arrived. The computing, not the theory, now looked like the problem (p. 224).
- Smith and Gelfand used "Bayes" only five times in 12 pages. A second paper six months later was exuberant. Tierney tied the method to Metropolis, and "MCMC" became its name (p. 224).

### Aftermath (pp. 224–226)
- About 80 scientists came to an Ohio State MCMC workshop in early 1991. After 1990, Bayesians no longer had to rely on oversimplified toy assumptions. The author calls it a paradigm shift in Kuhn's sense. "Exact" came to mean "simulated" (p. 225).
- Liu and Lawrence used MCMC to find motifs in protein and DNA. Particle filters and real-time applications followed. Thomas Bayes entered the *Dictionary of National Biography* in 1993 (p. 225).
- **BUGS** (Spiegelhalter, 1989–1991): free generic software linking Gibbs sampling to a graph. It caused the biggest single jump in Bayesian popularity and is still the most popular software for Bayesian analyses. It spread to ecology, genetics, machine learning and more (p. 226).

### Medicine (pp. 226–229)
- Green (1996) showed how to jump between models. Of 10 candidate stroke factors, he identified the top four: systolic blood pressure, exercise, diabetes and daily aspirin (pp. 226–227).
- **Screening.** Johnson and Gastwirth showed that screening the whole population for a rare disease like HIV would be counterproductive. A sensitive test would tell many people they were infected when they were not (p. 227).
- The author says Bayes also suggested that MRI for breast cancer may suit women with strong family history but not all women aged 40–50. A woman who has a mammogram each year for 10 years can be almost 100% sure of one false positive. PSA is highly accurate, yet the disease is so rare that almost everyone with a positive result lacks cancer (p. 227).
- Negative results are not fully reassuring. PSA is so insensitive that good news gives almost no assurance. Mammography's sensitivity is about 85–90% (pp. 227–228).
- A strict Bayesian gives patients probabilities rather than yes or no (p. 228).
- Spiegelhalter argued that health-care advances typically come by incremental gains, so this domain appears particularly amenable to a Bayesian perspective. Bayesian networks (graphs of nodes linked by cause-and-effect, updated by Bayes) were popularized by Pearl in 1988. Heckerman wrote a lymph-node diagnosis program that won an award in 1990 (p. 228).
- The FDA allows Bayes in device applications; the author says new models of a device should come with objective prior information. For drugs the FDA has long resisted, because potentially an industry could subjectively bias the prior. According to Spiegelhalter the same battle seems to have subsided in England, where drug companies use WinBUGS with judgmental priors for reimbursement submissions (p. 229).
- Outside diagnosis and devices, Bayes has had little effect on basic clinical research or practice. Doctors use it intuitively, and simple Bayesian questions began appearing on licensing exams in 1992 (p. 229).

### Wildlife (pp. 230–231)
- With weak evidence, the author says only Bayes incorporated uncertainty and showed when more information was needed. Taylor and Gerrodette (1993) wrote that at least part of the blame for past overexploitation lay with scientists being unable to agree on a clear way to treat uncertainty (p. 230).
- The 1991 bowhead problem: the committee chair's question "What can we do?" met silence. Zeh talked with Raftery, who thought Bayes might help: the committee could assign uncertainties to all the data and add hydrophone recordings to visual counts. The 1993 data showed the whales almost assuredly increasing. Full Bayesian analyses were then discontinued because they were expensive and confirmed earlier frequentist studies (pp. 230–231).
- **Belugas (Wade, Cook Inlet).** Frequentist methods needed seven years of data. Bayes showed in five years that the population was almost certainly declining substantially. A moratorium began in May 1999. A 1998 National Research Council committee urged aggressive Bayesian use for fish stocks (p. 231).

### Conclusion (p. 232)
- Lindley predicted a Bayesian twenty-first century through superior logic. Blackwell said any growth would come from users such as actuaries, engineers and business people. The author writes: "It appeared that Blackwell was right: pragmatism could drive a paradigm shift." Philosophies had not changed, but Bayes finally worked (p. 232).
- Diaconis decided in 1997 that "Our time is now" (p. 232). Smith became the first Bayesian president of the Royal Statistical Society in 1995 and left statistics in 1998. He told Lindley that all the problems of statistics had been solved: we have the paradigm, and with MCMC we know how to implement it (p. 232).

## Toy example (ours, not from the text)
Two unknown yes/no quantities $X, Y$ (each 0 or 1) have a joint posterior: $P(0,0)=0.4$, $P(0,1)=0.1$, $P(1,0)=0.2$, $P(1,1)=0.3$.

Easy one-variable conditionals, computed from the table:
- $P(Y{=}0\mid X{=}0)=0.4/0.5=0.8$; $P(Y{=}0\mid X{=}1)=0.2/0.5=0.4$.
- $P(X{=}0\mid Y{=}0)=0.4/0.6=2/3$; $P(X{=}0\mid Y{=}1)=0.1/0.4=0.25$.

Gibbs sampling alternates: draw $Y$ given $X$, then $X$ given $Y$. Starting at $X=0$:
- $P(X{:}0\to0)=0.8\cdot\tfrac23+0.2\cdot0.25=0.5333+0.05=7/12$, so $P(0\to1)=5/12$.
- From $X=1$: $P(1\to0)=0.4\cdot\tfrac23+0.6\cdot0.25=0.2667+0.15=5/12$, so $P(1\to1)=7/12$.
- After one step, $P(X{=}0)=7/12=0.583$. After two steps: $(7/12)^2+(5/12)^2=49/144+25/144=74/144=0.514$.
- The target marginal is $P(X{=}0)=0.4+0.1=0.5$. Check that 0.5 is stationary: $0.5\cdot\tfrac7{12}+0.5\cdot\tfrac5{12}=0.5$. The gap to 0.5 shrinks by a factor of 6 each step (1/12, then 1/72).

So two easy conditional draws, repeated, reproduce the joint distribution without ever sampling the joint directly.

## Concepts
- [[curse-of-dimensionality]] (new) — the plague of unknowns that appears as variables are refined; it hurt both Bayesians and frequentists (pp. 213–214)
- [[hierarchical-model]] — Lindley–Smith way of modelling a process in stages; used in the diesel meta-analysis (pp. 214, 216)
- [[markov-chain-monte-carlo]] — replace integration by long chains of simple draws, each depending on the previous value (p. 221)
- [[gibbs-sampling]] — the Geman brothers' variant of Monte Carlo for imaging problems with many pixels (pp. 218–219)
- [[metropolis-hastings]] — algorithm from Metropolis (1953), generalized by Hastings (1970); gives estimates, not exact answers (p. 223)
- [[monte-carlo-integration]] — learning about a distribution by sampling instead of exact calculation (p. 221)
- [[frequentist-vs-bayesian]] — here the author sees practice, not new philosophy, as the driver of change: Bayes "finally worked" (p. 232)
- [[base-rate-neglect]] — implicit in the screening cases: for PSA, the disease is so rare that almost everyone with a positive result lacks the cancer (p. 227)
- [[bayesian-network]] (new) — graph of nodes with cause-and-effect links, updated by Bayes' theorem (p. 228)
- [[em-algorithm]] (new) — iterative method that turns a small data sample into estimates likely true for a whole population (p. 221)
- [[bugs-software]] (new) — free generic program linking Gibbs sampling to graphs (p. 226)

## Canonical instances
- [[challenger-failure-estimate]] (new) — Teledyne 1 in 35 versus NASA 1 in 100,000 (p. 215)
- [[diesel-cancer-meta-analysis]] (new) — hierarchical borrowing across species (p. 216)
- [[coal-mine-accident-change]] (new) — Bayesian comparison finds an abrupt drop in accident rates (p. 216)
- [[hiv-mass-screening]] (new) — rare disease, false positives (p. 227)
- [[bowhead-whale-count]] (new) — Bayes combines visual and acoustic data (p. 231)
- [[cook-inlet-belugas]] (new) — Bayes decides in 5 years rather than 7 (p. 231)

## Bridges (candidates)
- [same-math] Gibbs/Metropolis–Hastings sampling ↔ the field's MCMC concepts: same algorithms as the Bayesian posterior-sampling toolkit.
- [same-math] screening results (HIV, PSA) ↔ Bayes' theorem and base-rate neglect: a positive result is weighed against disease prevalence.
- [structural-analogy] Bayesian networks ↔ causal DAGs: both are graphs of nodes with links, though the source treats the links as quantifiable belief.
- [metaphor] "paradigm shift" ↔ Kuhn's philosophy of science: here applied to a change in method driven by practice.

## Questions this raises
- What does the long run of a Markov chain have to do with the posterior? What conditions make a chain converge to it?
- Which Bayesian questions are still too slow to compute, and how would we know a chain has "mixed"?
- Why do the regulators distrust Bayes for drugs but accept it for devices? Can priors be protected from bias?
- Was the late adoption mostly about computers, culture or training? Does the evidence in the chapter distinguish these?

## Reading notes
- Printed page = pdf − 15 (pdf 228 = p. 213). Running headers read "Victory" (left pages) and "Eureka!" (right pages).
- Text layer was clean; no equations. The chapter has no headings, numbered sections or math (only a few blank-line breaks), so L3 headings are mine.
- Appendix B (breast-cancer calculation) is mentioned (p. 227) but is not in this unit.
- Dates and attributions follow the author's account. For example, p. 222 says Monte Carlo "began" in 1906 with Markov's chains. I report this as the author's phrasing.
