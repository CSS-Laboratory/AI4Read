---
id: mcgrayne-2011-theory/ch04-bayes
work: mcgrayne-2011-theory
unit: "4. Bayes Goes to War"
pages: 61-86
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Bayes Goes to War

## L0 — One line
In the Second World War, leading mathematicians and other non-statisticians used Bayes' rule in secret to break codes, aim guns and hunt U-boats, and secrecy then kept the story hidden for decades.

## L1 — The gist (≤ 120 words)
How could wartime leaders decide fast, without complete information? McGrayne says some of the century's greatest mathematicians used Bayes' rule in secret. Turing built Banburismus, a paper system that measured evidence in "bans" (units of weight of evidence) to attack the U-boat Enigma (a German cipher machine). Kolmogorov advised on Bayesian artillery fire. Koopman planned U-boat searches. Shannon tied Bayesian ideas to information and secrecy. Others attacked the Tunny (German teletype) and JN-25 (Japanese naval) ciphers. Churchill ordered the evidence destroyed and secrecy lasted for decades. It hurt Turing, Britain's credit for the Colossi (early electronic computers), and Bayes' reputation outside cryptography.

**Prerequisites:** Bayes' rule in odds form; logarithms (log of a product = sum of logs); basic idea of a prior and of independent clues.

## L2 — Key ideas
- By 1939 Bayes' rule was virtually taboo among statisticians in the know. Wartime data work was often done by non-statisticians (actuaries, biologists, physicists, pure mathematicians), few of whom knew this; the author says their ignorance proved fortunate (pp. 61, 64).
- Turing's Banburismus used "cribs" (guessed plain text) and Bayesian weighing of hunches. It aimed to cut the workload of the bombe (a code-testing machine) from 336 wheel settings to as few as 18 (pp. 66–67).
- One ban is odds of 10 to 1 in favour of a guess; Turing mostly used smaller units such as decibans (p. 67). Bans were used to judge sequential hypotheses as evidence arrived, and the author says Turing was thus one of the first to develop sequential analysis, where the tester stops once evidence is enough (pp. 67–69).
- Kolmogorov, who favoured frequency-based probability (a frequentist), told the Russian generals to start with 50–50 priors (equal odds before any data) when firing repeatedly at a small area. He said that, strictly speaking, this was arbitrary and surely wrong, but felt he had no choice (pp. 72–73).
- Koopman treated U-boat search as a "probability of causes" problem and wrote precomputed search recipes for commanders, who could update the plan with Bayes' rule every two hours (pp. 79–80).
- Shannon said he worked on information theory and cryptography together. Roughly speaking, if the posterior (updated belief) is quite different from the prior (starting belief), something has been learned (pp. 76–77).
- Bayesian scoring carried on into Tunny/Colossus work and into the JN-25 attack (pp. 74, 82–83).
- Postwar secrecy cost Turing and Britain, and Bayes' rule, the author says, emerged from the war as vilified as ever outside cryptography (pp. 83–86).

## L3 — Walkthrough
The chapter has no numbered sections. The headings below are ours and follow the author's order.

### A. Setting: the U-boat peril and Enigma (pp. 61–63)
- By 1939 Bayes' rule was "virtually taboo" for statisticians in the know. The open question was how leaders could decide quickly without complete information (p. 61).
- Britain fed only about one in three residents from its own farms. After France fell in 1940 it needed about 30 million tons of food and supplies a year by sea (p. 61).
- U-boats sank an estimated 2,780 Allied ships, and over 50,000 merchant seamen died. **Churchill** said the U-boat peril was the only thing that ever really frightened him during the war. **Hitler** said "U-boats will win the war" (p. 61).
- U-boats got their orders by radio. More than 49,000 coded messages are archived. They were encrypted by Enigma machines, and nobody in Britain or Germany thought the codes could be broken (pp. 61–62).
- The Poles saw first that mathematics could break the codes. Rejewski used guesswork and group theory to find how the Enigma wheels were wired. By early 1938 the Poles read 75% of German army and air force messages. They then gave their system to the French and British (p. 62).
- An Enigma looked like a typewriter with 26 keys and 26 lamps. Each key press sent current through three wheels and advanced one. Changing wiring, wheels and starting places gave millions of permutations (p. 62).
- About 40,000 military Enigmas were issued. Most German naval vessels, U-boats included, had one (pp. 62–63).

### B. Why Britain lacked mathematicians (pp. 63–65)
- The Government Code and Cypher School (GC&CS), Britain's code-breaking agency, hired linguists, art historians, crossword puzzlers and chess players. Mathematicians were "strange fellows" (p. 63).
- British schools and government treated applied mathematics and statistics as irrelevant. Mathematicians told colleagues to register as physicists to avoid combat. Lord Woolton found the War Office had no statistics on uniforms (p. 63).
- Probability experts were scarce. Doeblin killed himself in 1940 as a soldier. Jeffreys, Fisher and Neyman were sidelined, for reasons the author gives as presumed or partial (p. 64).
- Wartime data were therefore analyzed by actuaries, biologists, physicists and pure mathematicians. Few knew Bayes' rule was "unscientific" for sophisticated statistics. The author says this ignorance proved fortunate (p. 64).
- **Turing** (studied pure mathematics at Cambridge and Princeton) joined GC&CS at Bletchley Park on 4 September 1939. He was interested in logic, probability, machines and codes (pp. 64–65).
- He designed the "bombe", an electromechanical machine that tests every possible wheel arrangement of an Enigma. It tested 15-letter hunches and threw out wheel settings that could not produce them (p. 65).

### C. Banburismus and the ban (pp. 65–69)
- Hitler's navy used the most complex Enigma machines and security systems. A naval Enigma could use 1 of 4 reflector combinations, 3 of 8 rotors (up to 336 permutations), more than 150 billion plugboard combinations, 17,000 clip positions and 17,000 starting positions. Many settings changed every two days, sometimes every 8 or 24 hours (p. 66).
- Superiors said the naval codes were unbreakable. Birch, head of naval intelligence at GC&CS, thought they had to be broken. Turing chose them because no one else wanted them (p. 66).
- A bombe took 18 minutes per wheel setting, so, assuming the worst, testing all 336 wheel permutations would take four days. Turing invented a manual "Bayesian system", Banburismus, to cut this load (p. 66).
- Turing's hope (he said he was not sure it would work in practice): guess a stretch of letters, hedge bets, measure belief with Bayesian methods, and add clues as they come. It would identify the settings for 2 of Enigma's 3 wheels and cut the bombe tests from 336 to as few as 18 (pp. 66–67).
- **Cribs** are words predicted to occur in the plain text. They came from standardized weather reports and from British weather data. A prisoner's remark led Turing to find that "ein" appeared in 90% of messages. Clerks catalogued 17,000 ways it could be encrypted (p. 67).
- **The ban.** Turing saw that hunches could not be compared without a unit. He defined the ban as about the smallest change in weight of evidence "directly perceptible to human intuition" (p. 67).
  - One ban represents odds of 10 to 1 in favour of a guess. Turing usually worked with decibans and centibans (p. 67).
  - The author says the ban is basically the same as Shannon's bit (p. 67).
  - Each ban made a hypothesis 10 times more likely. When the odds reached 50 to 1, cryptanalysts could be close to certain they were right (p. 68).
- Because information arrived piecemeal, Turing used bans to discriminate between sequential hypotheses. He targeted the amount of evidence needed and stopped when he had it, instead of fixing the number of observations in advance (p. 67). The author says he was thus one of the first to develop what came to be called sequential analysis (p. 67). Bans were a manual paper-and-pencil system that automated the kind of subjective guessing Borel, Ramsey and de Finetti had tried to validate; Turing compiled reference tables of bans for technicians. The method was statistics-based and gave no absolute certainties (pp. 67–68).
- **Procedure.** Wrens punched each intercepted message letter by letter into 5–6 foot cardboard strips ("Banburies"). Strips were slid over each other, and repeats were recorded. A coincidence over several extra letters is a "fit" (p. 68).
- **Good** (Turing's statistical assistant) compared the game to reconstructing DNA sequences from many pieces of probabilistic information (p. 68).
- The author calls finding the Enigma settings a classic problem in the inverse probability of causes. No one is sure where Turing got Bayes. Neither he nor Good had been "sufficiently poisoned" by anti-Bayesian attitudes, because both had studied pure mathematics (pp. 68–69).
- Good asked Turing, "Aren't you essentially using Bayes' theorem?" Turing answered, "I suppose." Turing spoke of bans, not Bayes. Good concluded Turing knew the theorem existed, but the two may have been the only ones at Bletchley who realized Banburismus was heavily Bayesian (p. 69).
- Good told Barnard (breaking the rules) that they used Bayes factors and their logarithms sequentially to discriminate between two hypotheses. Barnard replied that the Ministry of Supply used a similar method on lots (p. 69).
  - Sequential analysis differs from frequency-based testing, where the number of tests is fixed in advance. Once a few tests clearly cleared or condemned a lot, the tester moved on, which almost halved the tests (p. 69).
  - Logarithms replaced multiplication by addition (p. 69).
  - Wald is generally credited with the method. Good concluded Turing had used it first and that Turing, Wald and Barnard all deserved credit (p. 69).

*Intuition note:* Each ban makes a hypothesis 10 times more likely (p. 68), and the author says logarithms replaced multiplication with addition (p. 69), so evidence could be tallied by adding. (Our reading: this works when clues are independent; the text does not say so.) The ban gave a shared scale for how strong a hunch was (p. 67).

### D. Waiting for a codebook; Churchill's intervention (pp. 69–72)
- By May 1940 Turing had the theory and method but could not read U-boat messages. Wolf packs were sinking ships. U-boats sank 2,177 merchant ships in the first 40 months (p. 69).
- Operators double-enciphered the three starting letters, once on the machine and once from codebook tables. Turing worked this out but needed a codebook, which had to be "pinched". The wait lasted ten months (p. 70).
- Morale fell. In August 1940 Birch pleaded for 10 bombes. The fight over bombes continued through 1940 (p. 70).
- Fleming's Operation Ruthless was planned and cancelled. Papers from two weather ships and a trawler gave clues (p. 71).
- By June 1941 Turing had reconstructed the codebooks from clues. Bletchley could read wolf-pack messages within an hour. For 23 days in June 1941 no North Atlantic convoy was attacked (p. 71).
- In October 1941 Turing and three others wrote directly to Churchill about staff shortages. Churchill ordered that they have "all they want on extreme priority" (pp. 71–72).

### E. Kolmogorov and Russian artillery (pp. 72–73)
- Kolmogorov showed in 1933 that probability is a mathematical branch founded on axioms, so frequentists and Bayesians alike could use it. He himself was a frequentist (p. 72).
- Russian artillery had used Bayesian firing tables for years. The generals were split over an esoteric point about aiming and asked his opinion (pp. 72–73).
- **Kolmogorov:** strictly speaking, starting with 50–50 prior odds was "not only arbitrary but surely wrong", because it contradicts the main requirements of probability theory. But with Germany at Moscow's door he felt he had to start with equal priors. Following Bertrand's reformed Bayes, he advised 50–50 odds when shooting repeatedly at a small area (p. 73).
- Since random shooting is sometimes better than precise aim, guns in a battery should aim slightly wide, like a hunter using pellets for dispersion (p. 73).
- His firing theory was printed in 1942, because censors did not see how it could help Germany (p. 73).

### F. Tunny-Lorenz and Turingery (pp. 73–74)
- Teletype-speed Lorenz machines (code name Tunny) carried high-level German strategy messages (p. 73).
- Codebreakers used Turing's bans, decibans and centibans, with a "spectrum of priors". Turing invented Turingery in July 1942 (p. 74).
  - Step one: guess and assume a 50% chance it is right, which the author says Bayes had suggested.
  - Then add clues, good and bad. When the odds reached 50 to 1, a pair of wheel settings was declared certain (p. 74).
- The effort began the first of ten Colossi, the first large-scale digital electronic computers (p. 74).

### G. The Great Blackout and the Atlantic (pp. 74–75)
- After Pearl Harbor, 15 U-boats hunted off the American East Coast. Convoys were silhouetted by shore lights until lights were ordered off (p. 74).
- The U-boats added a fourth Enigma wheel and the bombes were stymied. For most of 1942 no U-boat message was readable, which Bletchley called the Great Blackout (p. 74).
- In December 1942 three British crewmen swam to a sinking U-boat. Two drowned and Tommy Brown rescued the tables. Banburismus then became fully operational (p. 75).
- Turing went to the U.S. as liaison. He found the U.S. Navy ignoring Banburismus. He tried in vain to explain the general principle that confirming inferences drawn from a hypothesis would make the hypothesis itself more probable (pp. 75–76).

### H. Shannon and information (pp. 76–77)
- Turing and Shannon met regularly at tea at Bell Labs. Shannon was using Bayes' rule for wartime projects (p. 76).
- Shannon saw that noisy phone lines and coded messages could be analyzed by the same mathematics. The author states the purpose of information is to reduce uncertainty, and that of encryption is to increase it (p. 76).
- Shannon said he worked on both together from about 1941 (p. 77).
- **Author:** roughly speaking, if the Bayesian posterior is quite different from the prior, something has been learned. If the posterior is basically the prior, the information content is low (p. 77).
- A confidential 1949 report used Bayes' theorem and Kolmogorov's 1933 theory to show that in a perfectly secret system nothing is learned, because prior and posterior are equal (p. 77).
- The unit of information was the bit, a word suggested by Tukey (p. 77).
- Turing returned in March 1943, a very dangerous month for shipping (p. 77).

*Intuition note:* Roughly speaking, "learning" means the data moved your beliefs (p. 77). A perfect cipher gives an eavesdropper no reason to move from the prior.

### I. Operations research and Koopman's search theory (pp. 77–80)
- The Allies needed to find U-boats, not just evade them (pp. 77–78).
- British operational research (O.R.) used fairly elementary statistics that the author says were imbued with Bayesian ideas. Waddington reported that Bayes' "a priori Method" played a fairly large role, especially with few variables. Typical uses were the number of aircraft needed to protect a convoy and tour lengths (p. 78).
- Direction-finding stations could locate a U-boat to within about 10,000 square miles, a circle some 236 miles across. A method for narrowing the search was needed (p. 78).
- **Koopman** wanted to bridge subjective "intuitive" probability and objective frequency-based probability (p. 78).
  - He first asked what the U-boat's heading was likely to be, a classic Bayesian "probability of causes" problem. He gave prospectors, police and public health officials as examples of people who rely on prior knowledge (p. 79).
  - He assigned Bayes' 50–50 odds to the target being inside the 236-mile circle, then added data that were as objective as possible, as Jeffreys advised (p. 79).
  - He estimated most aircraft crews were only a quarter as efficient as lookouts under laboratory conditions (p. 79).
- **His worked example (p. 79):** find a U-boat within a 118-mile radius with 4 planes, each flying 5 hours at 130 knots over 5 lanes 5 miles wide. 
  - Three lanes had 10% probability of success, another 30%, a fourth 40%.
  - The officer should assign two planes each to the 40% and 30% lanes and none to the least probable areas (pp. 79–80).
  - He calculated by hand and said computers would have been irrelevant (p. 80).
- His manual: the effort for each subsection equals the logarithm of the probability there. Regions could have irregular shapes (p. 80).
- The commander could plan an eight-hour day, starting with an optimum search for the first four hours. Then, if the U-boat had not been found, he could use Bayes' rule to update its likely location and launch a new plan every two hours. All the two-hour planning could be done ahead of time (p. 80).
- Koopman called this a "continuous distribution of effort". The author says it is theoretically similar to Kolmogorov's artillery problem. Minesweepers adopted his techniques (p. 80).

### J. 1943–44: turning points and the Colossi (pp. 80–82)
- In 1943 the Soviets won in the East. The tide turned against U-boats (41 lost in May). Bletchley became a factory of almost 9,000 people. As more bombes came online, Banburismus cards were phased out (p. 80).
- Turing, Good and Michie discussed machine thinking and learning (p. 81).
- Newman, Michie and Good wanted automation. Mechanical switches were too slow, so Flowers built Colossus with vacuum tubes. It decrypted its first message on 5 February 1944. A second, more advanced Colossus was ready by 1 June (p. 81).
- Colossus II decoded Hitler's order to Rommel not to move for five days after any Normandy invasion. Eisenhower said "We go tomorrow". He later estimated Bletchley shortened the war in Europe by at least two years (p. 81).
- The Colossi replaced Turingery in August 1944. Michie reported that Turing's ban-based scoring grew from a "minor mental aid" into a "major aid" in wheel-pattern breaking (p. 82).

### K. Japanese naval code JN-25 and American spread (pp. 82–83)
- Cassels, Whitworth and Simpson worked on JN-25 from late 1943. Security stopped them consulting Turing or Good, so they adopted Bayes on their own (p. 82).
- JN-25 blocks were five-digit code groups plus a five-digit additive. The team judged candidate additives by how plausible the resulting code group was, assigning probabilities based on frequency in messages already deciphered (pp. 82–83).
- **Simpson:** for practical purposes one did not need to agonise over prior odds. The essential judgment was whether the collective evidence was convincing enough, and an inspired hunch could contribute most (p. 83).
- After October 1944 Alexander, Bletchley's finest Banburismus solver, developed an elaborate use of Bayes' theorem and decibans for the Japanese codes (p. 83).
- U.S. cryptanalysts wrote memos about Bayes by 1945. How they learned of it is unknown, and the author says the British government still refuses to declassify many wartime cryptography documents (p. 83).
- Gleason's textbook taught NSA cryptanalysts Bayes' theorem, decibans, Bayesian inference and hypothesis testing. It also covered Neyman's methods (p. 83).

### L. Secrecy and its costs (pp. 83–86)
- Churchill ordered destruction of evidence that decoding helped win the war. Most Colossi were dismantled (pp. 83–84).
- Participants were gagged. The story began emerging only after 1973 (p. 84).
- The likely reason, the author says ("seems to be"), was that Britain did not want the Soviets to know it could read Tunny-Lorenz. At least one surviving Colossus broke Soviet codes in the Cold War (p. 84).
- Costs the author names: families never knew; Colossus builders got little or no credit; the world assumed U.S. computers came first; Cold War attitudes favoured hardware and spies over decryption (p. 84).
- **Turing afterwards:** he joined the National Physical Laboratory, arrived as "a nobody" and was reprimanded for lateness by Darwin. His 1945 stored-program design was judged too ambitious, but built in 1950 it was the fastest computer in the world. At Manchester he proposed the Turing Test (pp. 84–85).
- In 1952 he was arrested for homosexual activity at home with a consenting adult. He lost his security clearance and chose estrogen injections over prison. He died by suicide on 7 June 1954. The British prime minister apologized in 2009 (pp. 85–86).
- Bayesian work lived on in cryptography. Good became one of three leaders of the 1950s–60s Bayesian renaissance, writing roughly 900 articles on Bayes (p. 86).
- Outside cryptography, no one knew Bayes had helped. The author says it emerged from the war as vilified as ever (p. 86).

## Toy example
*(Our own; not from the text. It assumes the clues are independent given the hypothesis, which the unit does not discuss.)*
Start with a hunch H at even odds (1 : 1, 0 bans). Three independent clues arrive, with likelihood ratios 3, 2 and 5 in favour of H.
- Multiplying: odds = 1 × 3 × 2 × 5 = 30, so 30 : 1.
- Using decibans, 10·log₁₀(LR): 10·log₁₀3 ≈ 4.77; 10·log₁₀2 ≈ 3.01; 10·log₁₀5 ≈ 6.99.
- Adding: 4.77 + 3.01 + 6.99 = 14.77 decibans, which is 1.477 bans. Check: 10^1.477 ≈ 30, so the two routes agree.
- Probability of H = 30/31 ≈ 0.97.
- Reaching Bletchley's 50 : 1 needs log₁₀50 ≈ 1.699 bans, i.e. 16.99 decibans. That is about 2.22 more decibans, i.e. a further clue with likelihood ratio about 1.67 (10^0.222).

## Concepts
- [[bayes-theorem]] — rule for turning evidence into updated odds, used here as hunch-weighing; Turing talked about bans, not Bayes (pp. 67–69).
- [[prior-distribution]] — starting belief. Used as 50–50 by Kolmogorov (reluctantly) and Koopman, and as a 50% starting guess in Turingery; Simpson said that for practical purposes one need not agonise over prior odds (pp. 73, 74, 79, 83).
- [[posterior-distribution]] — updated belief; information content is low if it is basically the same as the prior (p. 77).
- [[sequential-updating]] — add clues as they arrive and stop when evidence is enough (pp. 67, 80).
- [[subjective-probability]] — hunch-based belief that bans made measurable (pp. 67–68).
- [[ban-deciban]] (new) — Turing's unit of weight of evidence; one ban is 10 to 1 odds (p. 67).
- [[bayes-factor]] (new) — the factor by which evidence multiplies odds; Good used Bayes factors and their logarithms sequentially (p. 69).
- [[sequential-analysis]] (new) — stop testing once evidence is strong enough instead of fixing sample size (pp. 67, 69).
- [[crib]] (new) — guessed plain-text word used as a hunch for decryption (p. 67).
- [[operations-research]] (new) — British wartime scientific group improving military efficiency with Bayes-flavoured statistics (p. 78).
- [[information-theory-bit]] (new) — Shannon's logarithmic unit of information; in a perfect secrecy system prior equals posterior (pp. 76–77).

## Canonical instances
- [[banburismus]] — Turing's Bayesian card-strip system for reducing bombe workload (pp. 66–68).
- [[turingery]] — Bayesian paper-and-pencil method for Tunny wheel settings, with 50-to-1 certainty threshold (p. 74).
- [[kolmogorov-artillery-priors]] — 50–50 prior advice for repeated fire and aiming wide (p. 73).
- [[koopman-search-theory]] — probability-based search allocation, updated every two hours (pp. 79–80).
- [[jn-25-additive-scoring]] — probability of additives judged from frequency in deciphered text (pp. 82–83).
- [[shannon-secrecy-1949]] — in a perfectly secret system, prior and posterior are equal (p. 77).

## Bridges (candidates)
- [same-math] Turing's bans and decibans ↔ bayesian: log odds / weight of evidence, where evidence adds in log space.
- [same-math] Sequential analysis with stopping on enough evidence ↔ bayesian: sequential updating with a threshold on the posterior odds.
- [structural-analogy] Koopman's search effort allocation by posterior probability ↔ bayesian: posterior-guided decisions (choosing where to look next).
- [structural-analogy] Shannon's "learning" as posterior far from prior ↔ KL divergence (canon link; not stated in this unit).

## Questions this raises
- How exactly do cribs and cardboard "fits" produce a Bayes factor? The chapter gives no numerical example.
- What are the objective data that Koopman fed into his priors, and how sensitive were results to the 50–50 start?
- If Kolmogorov said that, strictly speaking, equal priors were "surely wrong", why did he recommend them? What justifies it in the repeated-fire case?
- How did Simpson's group avoid subjective bias without agreed priors?

## Reading notes
- Printed page = pdf − 15 (pdf 76 = printed 61). Source pages show no equations.
- Source misprint/oddity: "Bayesean artillery" (p. 73). "Molina's relay circuits" (p. 76) appears as printed.
- Figures such as "336" wheel permutations and the reduction to "as few as 18" are the author's (pp. 66–67). The chapter does not explain how the 18 is reached.
- Superlatives ("first", "fastest") reflect the author's claims, not independent checks.
