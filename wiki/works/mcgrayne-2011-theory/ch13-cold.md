---
id: mcgrayne-2011-theory/ch13-cold
work: mcgrayne-2011-theory
unit: "13. The Cold Warrior"
pages: 163-175
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
# The Cold Warrior

## L0 — One line
According to colleagues and McGrayne, John Tukey used Bayesian methods for NBC's election forecasts for almost two decades while never admitting it, and his secrecy was one reason few statisticians realized how much Bayes' rule was being used.

## L1 — The gist (≤ 120 words)
Why did a famous Cold War scientist who publicly distrusted Bayes use it on live television? From 1960 John Tukey led NBC's election-night statistics. According to David Wallace and others, the system combined past voting records and expert opinion into priors, then updated them as returns arrived. Tukey called this "borrowing strength," not Bayesian, and refused to let colleagues write or speak about the methods. Tukey said the methods were proprietary to RCA; McGrayne questions that, raises other reasons including possible classified cryptography work, and says the answer is hard to know. The secrecy was one reason most statisticians never noticed this very public Bayesian success.

**Prerequisites:** the idea of updating a guess with new data (prior → posterior); what an opinion poll is; the names Fisher and Savage as rivals and allies of Bayes.

## L2 — Key ideas (5–10 bullets)
- NBC hired Tukey in 1960 because polling had a poor reputation and the Kennedy–Nixon race was too close to call (pp. 163–164, 166).
- Tukey was deeply embedded in Cold War military and intelligence research (the Nike missile, the U-2 spy plane, seismology for nuclear test bans, the cryptography think tank IDA, the National Security Agency) (pp. 164–165).
- His public stance was sceptical of Bayes and critical of Fisher. Friends say he opposed any single philosophy of inference, and he himself warned against a unified framework (pp. 168–170).
- Colleagues (Wallace, Brillinger, Pratt, Fienberg) say the NBC system was Bayesian: in Fienberg's words a form of empirical Bayes (the prior built from past results), and in Wallace's a hierarchical model with historically based priors (a prior is the starting estimate before new data arrive). Tukey called it "borrowing strength" (pp. 168, 170–171).
- On election night, forecasters built prior information from polls, expert opinion and voting history, then updated it as returns came in (p. 171).
- The system had limits: turnout was hard to predict, and early returns were biased samples (p. 172).
- McGrayne suggests several reasons for the secrecy (the word's inflammatory reputation, possible cryptography ties, and RCA, which was Tukey's own stated reason and which she questions) without settling them (pp. 173–174).
- The secrecy was one reason few statisticians realized how much Bayes was used, though it ran on TV for almost two decades. McGrayne suggests that had Tukey publicized the methods, polling history might have been different (pp. 174–175).

## L3 — Walkthrough
(The chapter has no numbered sections; I follow its order by theme.)

**Opening: the 1960 election and NBC (pp. 163–164).** The Mosteller–Wallace Federalist project impressed statisticians. Tukey's work for NBC would give Bayes the chance to show itself to 20 million viewers of the *Huntley–Brinkley Report*. The 1960 Kennedy–Nixon race was too close to call. The networks competed to declare the winner first, and NBC also wanted to show off RCA computers. Poor polling in 1936 and 1948 made executives nervous, so NBC approached Princeton professor Tukey (pp. 163–164).

**Tukey's Cold War career (pp. 164–165).** He worked at Princeton and at Bell Labs, and advised five presidents, the NSA and the CIA (p. 164).
- Wartime: gunfire aiming for B-29 bombers. Cold War: the Nike missile and the U-2 plane (p. 164).
- In 1959, as a delegate to the US–USSR test-ban talks, he showed that seismogram data could distinguish underground nuclear explosions from earthquakes. The Partial Test Ban Treaty followed in 1963 (p. 164).
- He served on the board of trustees of IDA, a cryptography think tank at Princeton, for decades. IDA left campus in 1970 after student protests (pp. 164–165).
- He evaluated the Teller–Ulam H-bomb design in 1951 and worked for the Forrestal Research Center from 1951 to 1956 (p. 165).
- Many faculty did classified work then; Fienberg recalls a safe in Chicago's statistics department (p. 165).

**Tukey the person (pp. 165–167).** He supervised over 50 students, put his name to about 800 publications, and had more than 105 coauthors, most often Mosteller (pp. 165–166). His lecture style was oblique, and his personal habits were eccentric (pp. 165–166).

**Why Tukey accepted (pp. 166–168).**
1. Polling's reputation was abysmal; Tukey said he would prefer a random sample of three to a Kinsey sample of 300 (pp. 166–167).
2. RCA computers. Tukey helped design the architecture of von Neumann's Princeton computer, yet his own tools were pencil and paper (p. 167).
3. Real data. Military research had made him a "data analyst" who preferred hard real problems to unreal assumptions (p. 167).
4. The thrill of the chase; he later called it the best education anyone could have in real-time statistics (pp. 167–168).

**Election night, 8 November 1960 (p. 168).** Kennedy won by 120,000 of 70 million votes. By 2:30 a.m. Tukey's team was ready to call him the winner. NBC executives locked the statisticians in a room without telephones until 8 a.m. Tukey had, in any case, prevented NBC from mistakenly declaring Nixon the winner. He then worked for NBC for 18 years (p. 168; see Reading notes). His handpicked team included Mauchly, Cornfield, Link, Abelson and Brillinger, and later Wallace (p. 168).

**Was it Bayesian? (pp. 168–169).**
- *Public stance:* Tukey is not known to have published anything using Bayes' rule. He said Bayesian analyses are reasonable for many classes of problems, mainly ones he knew little about (p. 168). The lack of a method for quantifying the initial prior irritated him (p. 168).
- *Wallace's view:* he found Bayes' rule "securely ensconced" in the program. He says he coded the models and was "using Bayesian things." Brillinger, Pratt and Fienberg agree. Fienberg: "a form of empirical Bayes, where the past results were used to construct the prior distribution" (p. 168).
- In almost two decades of election forecasting Tukey never admitted using Bayes' rule (pp. 168–169). Wallace says Tukey would deny anything Bayesian in the NBC polling (p. 169).
- Colleagues describe Tukey as private and enigmatic, and hard to read on any issue (p. 169).

*Intuition note:* In Fienberg's phrase, "empirical Bayes" means the prior was built from past results. The source does not say whether this met Tukey's complaint about quantifying the initial prior.

**Tukey's positions on inference (pp. 169–170).**
- He accepted subjectivity, calling objectivity "an heirloom" and "a fallacy" (p. 169).
- He was even tougher on Fisher. He argued that real data usually violate the standard assumptions, and wrote: "Far better an approximate answer to the right question… than an exact answer to the wrong question" (pp. 169–170).
- Brillinger thought Tukey was annoyed not with Bayesian arguments themselves but with some Bayesians. Tukey: discarding Bayesian techniques would be a real mistake, but trying to use them everywhere would be a considerably greater one (p. 170).
- He used almost the same language about Fisher's fiducial alternative to Bayes: after 64 pages seeking its logical foundations, he judged belief in a unified structure for inference a dangerous form of hubris. In one story Fisher stalked angrily away when Tukey questioned his methods (p. 170).
- His own approach was exploratory data analysis (EDA) (p. 170).

**The renaming (pp. 170–171).** Brillinger and Wallace called the NBC polling Bayesian; Tukey called it "borrowing strength" (p. 170). A colleague counted 50 terms he coined (p. 170). McGrayne's comment: "Bayes' rule by any other name is Bayes' rule" (p. 171).

**How the system worked (p. 171).**
- *Before election night:* Wallace built initial information from preelection polls, expert opinion of political scientists, and voting histories of precincts, counties, cities and states (p. 171).
- *On election night:* the team watched for swings and deviations from past behaviour and from expert opinion, then modified their initial odds with the new information (p. 171).
- *Wallace's county example:* with no returns from county A, a "strict non-Bayesian" would say nothing. A "slightly Bayesian person" would note that similar county B shows a 5% swing toward Republicans, and would guess A may go the same way without giving it great weight. Tukey's instruction: group similar counties, weight counties with data, give zero weight to counties without data, and keep updating continually (p. 171).
- Wallace: historical data from previous elections show the variability between counties, which is the source of the priors, so he calls it very Bayesian, with a hierarchical model and historically based prior variances (p. 171).

*Intuition note:* "Borrowing strength" means using information from similar places to fill gaps, and attaching wide error bounds to the borrowed numbers, as Wallace described (p. 171).

**Problems on air (p. 172).** In 1964 seven RCA computers sat unused on the set, either because the operating system was unfinished or because the studio lights' heat fried them, and the team used hand calculators. LBJ won 61%, so the work was easy (p. 172). In another election, early calls for California and New York were contradicted for two hours before the pattern returned (p. 172). Wallace found turnout harder to project than candidate percentage. He said the incoming data are of dubious quality: reporting biases, machine votes arriving faster than non-machine votes, and sometimes chicanery. Turnout is very hard to predict and has a startling effect, and he concluded, in odd wording, that Bayes was apparently not a complete answer (see Reading notes). He was appalled when a student consulting for another network called election night the one place in statistics where all assumptions are valid: the data are a highly biased sample, and ignoring that brings serious trouble (p. 172).

**Secrecy (pp. 172–174).** NBC moved to exit polls after 1980 (pp. 172–173). Tukey forbade colleagues to write or talk about the methods, saying they were proprietary to RCA (p. 173). Late in life he conceded that probably the best excuse for Bayesian analysis is combining outside information and expert views with the data in hand (p. 173). He also made a Bayesian-style argument to Congress that the Census should adjust undercounts using similar regions; as of 2010 it had not (p. 173).

McGrayne lists possible reasons without choosing one (p. 173):
- Brillinger: "Bayes is an inflammatory word." McGrayne adds that "borrowing strength" let Tukey avoid it, and perhaps gave him a neutral workspace or a personal stamp.
- RCA sold its computer division halfway through his NBC stint; McGrayne asks why RCA would then care whether his system went public.
- McGrayne asks whether RCA's military sponsors classified his methods, and whether he was using Bayes' rule in classified cryptographic research and distancing himself from Bayes to protect it.

Evidence on cryptography (p. 174):
- Wallace says secret coding agencies would show Bayes had a larger history, with I. J. Good the principal contributor to the Bayesian group, though he says he is not in a position to speak of it (p. 173).
- Bell Labs head William O. Baker said Tukey helped decrypt Enigma and Soviet codes. Tukey served on the NSA Science Advisory Board. Whether he did hands-on cryptography "is not known" (p. 174).
- Tukey hosted Good at Bell Labs in October 1955 and introduced him to Cornfield, who became a prominent Bayesian. Shannon was in the audience and had used Bayes' rule in wartime work. Tukey coined "bit" in 1946 (p. 174).
- Tanur, Link and Brillinger judge it probable or plausible that he used Bayes' rule for decoding at Bell Labs (p. 174).

**Consequences (pp. 174–175).** Wallace: "a lot was under wraps." McGrayne says Tukey's censorship of the NBC polling methods, like the highly classified status of Bayesian cryptography, is one reason so few realized how much Bayes' rule was being used (pp. 174–175). Mosteller–Wallace on *The Federalist* (1964) was the only large computerized Bayesian study of a practical problem in the public domain during the 1960s revival. The next major public one came 11 years later. After 1980, 28 years passed before a presidential poll used Bayesian techniques again (p. 175). In November 2008 Nate Silver used hierarchical Bayes. He borrowed from outside areas to strengthen small samples, weighted other pollsters by track record, sample size and recency, and combined historical polling data. He correctly called 49 states (p. 175). McGrayne suggests that publicity of Tukey's methods might have changed polling history and even American politics (p. 175).

## Toy example (ours, not from the text)
Illustration of "borrowing strength" for county A with no returns. Measure everything as the swing toward Republicans, in percentage points.
- Historical prior for A: mean 0, variance 4, so precision (1/variance) = 1/4.
- Similar counties B and C show swings +5 and +3, average +4. Because the borrowing is imperfect, assign this estimate a large variance, 12 (precision 1/12).
- Combine by precision-weighted average: weights are 1/4 = 3/12 and 1/12; total precision = 4/12 = 1/3.
- Mean = (3/12 × 0 + 1/12 × 4) / (1/3) = (1/3)/(1/3) = **+1**.
- Variance = 1/(1/3) = **3**.
A modest +1 swing results, with wide error bounds: the neighbours count, but without great weight (p. 171). This is a simple normal-normal combination, not Tukey's actual model.

## Concepts
- [[empirical-bayes]] (new) — prior built from past data, e.g. earlier election results (Fienberg's description of NBC polling) (p. 168)
- [[prior-distribution]] — initial information from polls, expert opinion and voting histories (p. 171)
- [[hierarchical-model]] — Wallace's description: historical data give between-county variation, which supplies the priors (p. 171)
- [[partial-pooling-shrinkage]] — Tukey's "borrowing strength": using similar units to inform sparse ones (pp. 170–171); the source does not use the statistical term
- [[sequential-updating]] — keep updating odds as returns arrive (p. 171)
- [[subjective-probability]] — Tukey's acceptance that analysts may reach different results from the same data (p. 169)
- [[frequentist-vs-bayesian]] — Tukey criticised Fisher's frequency methods even more sharply than Bayesian methods, and warned against using Bayes everywhere (pp. 169–170)
- [[exploratory-data-analysis]] (new) — Tukey's approach in which the data alone matter, shorn of computerization, mathematization, probability and theory (p. 170)

## Canonical instances
- [[nbc-election-night-1960]] — Tukey's first night: team ready to call Kennedy by 2:30 a.m., locked away until 8 a.m.; he had prevented a mistaken call for Nixon (p. 168)
- [[nbc-election-1964]] — computers failed on air; hand calculators used (p. 172)
- [[tukey-test-ban-seismograms]] — seismograms distinguish nuclear tests from earthquakes (p. 164)
- [[silver-2008-hierarchical-bayes]] — hierarchical Bayes polling; 49 states correct (p. 175)
- [[mosteller-wallace-federalist]] — the only large computerized public Bayesian study of a practical problem during the 1960s revival (p. 175)

## Bridges (candidates)
- [structural-analogy] "Borrowing strength" across similar counties ↔ bayesian: partial pooling in hierarchical models — both pull sparse units toward information from related units.
- [structural-analogy] Updating election odds as returns arrive ↔ bayesian: sequential updating — each batch of returns revises earlier beliefs.
- [metaphor] Tukey renaming Bayes ↔ science studies: how vocabulary shapes acceptance of a method.

## Questions this raises
- Did Tukey's classified cryptography really use Bayes' rule, and could that explain his silence?
- How well did the NBC models handle biased early returns, and how would a modern model correct them?
- How different would the history of Bayesian statistics be if the NBC methods had been published?
- Is "borrowing strength" exactly a hierarchical Bayes model, or only similar to one?

## Reading notes
- Printed page = pdf page − 15 (pdf 178 = p. 163). Source pages 163–175.
- The text layer is clean apart from stray spacing (e.g. "super visor", p. 165). Endnote numbers are embedded in the text and omitted here.
- Duration is given in different words: 18 years (p. 168), almost two decades (pp. 168–169, 175) and two decades (p. 173); the end point is the 1980 election (pp. 172, 175). I give each as printed.
- The cryptography link is presented as inference (the evidence convinces some colleagues that he probably used Bayes' rule at Bell Labs), not as established fact (p. 174).
- The Wallace quote on p. 172 about turnout is oddly worded ("Bayes was not a total serving"); I kept the sense only.
