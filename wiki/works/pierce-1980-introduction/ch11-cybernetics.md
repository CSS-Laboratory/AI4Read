---
id: pierce-1980-introduction/ch11-cybernetics
work: pierce-1980-introduction
unit: "11 Cybernetics"
pages: 208–228
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Cybernetics (Pierce, Chapter XI)

## L0 — One line
Pierce argues that "cybernetics" is not one field but a loose umbrella over information theory, prediction and filtering, negative feedback, and computers and automata, so the word can add "a little glamor" but says little about anyone's field (pp. 208–209, 226–228).

## L1 — The gist (≤ 120 words)
Pierce asks what "cybernetics" covers. His answer: Wiener's book lumps together information theory, smoothing/filtering/prediction theory, negative feedback and servomechanisms, and complex machines (computers, telephone switching), plus life processes that resemble them. Each part is large and separate, so few scientists call themselves cyberneticists. Apart from information theory (treated in the rest of the book), he gives a small technical taste of the other parts: radar prediction, a feedback amplifier, the stored-program computer and compilers. He also treats whether machines "think". His conclusion is that calling oneself a cyberneticist says little about one's competence, and that if the word is over-extensive or vague, this does no real harm.

**Prerequisites:** basic arithmetic and ratios; the idea of signal and noise; Chapter III's idea of an ergodic source (a source whose long-run statistics are the same in every sample).

## L2 — Key ideas (5–10 bullets)
- Cybernetics, in Wiener's usage as Pierce reads it, spans information theory, prediction/filtering, negative feedback, and automata. Each is a big field alone, so the word is vague (pp. 208–209, 227–228).
- Linear prediction weights each past datum by a number that depends only on its age. It cannot both use old data well and react quickly to a change such as a plane turning (pp. 211–212).
- Nonlinear prediction covers all other methods, such as switching between predictors depending on the data. Much is known about linear prediction and very little about nonlinear (p. 213).
- Slepian's result: under stated conditions, exact measurement over any short interval would let us tell whether a signal is present, however faint. It is a theoretical, not practical, result (pp. 214–215).
- Negative feedback reduces departures from a goal. It can make a system unstable, and stronger feedback tends to raise that risk (pp. 215–216).
- A negative-feedback amplifier keeps gain nearly constant when its tubes change: in Pierce's figure, halving the inner gain cuts output only about 10% (pp. 217–218).
- Building complex computers needed components, interconnection (Boolean algebra, a branch of mathematical logic used to design relay circuits), and "spirit", meaning organization: a program, branching (the machine decides what to do next), and a stored program (kept in the machine's memory). Compilers (programs that write detailed programs from compact task statements) came later (pp. 219–224).
- Pierce reports Minsky's conclusion that people tend to regard as thinking only what they do not understand. Pierce himself thinks it probably impossible to specify a meaningful, explicitly defined goal that a man can attain and a computer cannot (p. 226).

## L3 — Walkthrough

### Opening: what is cybernetics? (pp. 208–210)
- Pierce notes that some words carry glamour without a clear meaning. He says cybernetics is not quite such a word but has "an elusive quality" and a romantic aura (p. 208).
- Wiener's 1948 book is subtitled *Control and Communication in the Animal and the Machine*. The word comes from the Greek for steersman (p. 208).
- Judging from Wiener's book, cybernetics includes at least the first three of these, and Pierce says we must also include the fourth (pp. 208–209):
  1. information theory;
  2. smoothing, filtering, detection and prediction theory (finding a signal in noise and predicting its future value);
  3. negative feedback and servomechanism theory, which Wiener traces to Maxwell's 1868 treatise on the governor;
  4. automata and complicated machines, including the design and programming of digital computers.
- It also includes life phenomena resembling these. **Wiener's view:** sociology and anthropology are primarily sciences of communication, so they fall under cybernetics, and economics is a branch of sociology (p. 209).
- Pierce's objection: each field has large scope on its own, so lumped together they form "a diverse universe of overwhelming magnitude". Hence few scientists regard themselves as cyberneticists. Pierce thinks that someone working in communication, computers or parts of psychology or neurophysiology, asked whether he works in cybernetics, might well reply "yes" if he judged the questioner a sincere and innocent outsider (p. 209).
- Plan: Pierce gives a brief résumé of the technical matters, so readers can judge their interest (p. 210).

### Smoothing, filtering and prediction (pp. 210–215)
- **Example: shooting down a plane with radar data.** The radar gives position measurements, each slightly wrong. From them the computer must deduce course and velocity and predict the future position (p. 210).
- If the plane flies at constant velocity and altitude, we can by eye draw a line AB that represents the course pretty well, though each radar point is a little in error. A computer using only the last two points (L and NL) draws a clearly wrong line (p. 210).
- Giving equal weight to all points fails when the plane turns at point T. The fitted straight line then "has little to do with the path" (pp. 210–211).
- **Linear prediction:** multiply each datum by a number depending on its age (smaller for older data) and add the products (p. 211).
- The result is slow to notice a turn, even though a human sees it by the next point. A linear predictor can use old data well but be slow to react, or react fast but waste old data (p. 212).
- **Nonlinear prediction** is every method that is not of this multiply-and-add form (p. 213).
- **Pierce's simple example:** two linear predictors, one using the last 100 data and one using the last 10. Use the 100-datum predictor only when it has beaten the 10-datum predictor three times in a row. Otherwise assume the aircraft is maneuvering and use the 10-datum predictor. The use made of past data then depends on the data received, so the method is nonlinear (p. 213).
- Pierce says a great deal is known about linear prediction and very little about nonlinear prediction (p. 213).
- **General statement:** there are possible signals (airplane paths, words) and noise or distortion. We estimate some aspect of the true signal (present or future position, the word just spoken or the next word). We use statistical knowledge of both signal and noise (pp. 213–214).
- Contrast with communication theory: the theorist, given a source and a noisy channel, asks how best to *encode* messages. In prediction, given noise-distorted signals, we ask how best to *detect or estimate* the true signal (p. 214).
- The "armory" is a general theory of linear prediction (Kolmogoroff and Wiener) and analyses of special nonlinear predictors (p. 214).
- **Slepian's result (a theoretical result Pierce finds startling).** Conditions (p. 214):
  - a faint signal may or may not be added to strong noise;
  - signal and noise are ergodic and band limited;
  - the noise spectrum is known exactly, and the signal spectrum is different;
  - the total voltage or sound pressure of signal plus noise can be measured exactly at every instant of any interval, however short.
- Under these conditions we could infallibly tell whether the signal is present, however faint it is (p. 214).
- Pierce calls this a sound theoretical, not a useful practical, conclusion. It shocked people who had claimed that a signal below a stated weakness could not be detected in a finite interval (pp. 214–215).
- **Why "filtering and smoothing":** if noise and signal have different spectra, a filter that cuts frequencies strongly present in the noise helps separate them. A filter that removes high frequencies makes the output vary less abruptly, which is smoothing (p. 215).

> *Intuition note.* Prediction means guessing the next value from noisy past values. Weighting old data heavily uses it well but slows the reaction to a change. Rules that depend on what the data show (nonlinear methods) are needed to predict well when circumstances change, and very little is known about them.

### Negative feedback and servomechanisms (pp. 215–219)
- A **servomechanism** is a device that acts continually on information to reach a goal despite changes. Example: steering a plane toward an enemy plane from radar data. The radar data change the plane's position, which changes later radar data (p. 215).
- This is **negative feedback**, because it is used to decrease, not increase, departures from the desired behavior (p. 215).
- Examples: the steam-engine governor (speed measurement adjusts the throttle) and the thermostat (p. 216).
- **Instability.** Carrying a tray of water and tilting to stop spilling can make the water slosh more wildly. Feedback can make deviations larger, not smaller (p. 216).
- Making corrections more complete means making the feedback stronger, but that tends to make the system unstable. Results include a wildly veering missile, an engine racing or stopping, or an amplifier "singing" with no input (p. 216).
- In **linear** feedback systems (present amplitude = past amplitudes times numbers depending only on remoteness), a system is stable or unstable regardless of the input. **Nonlinear** systems can be stable for some inputs and unstable for others. Example: a car that is stable on a smooth road but shimmies indefinitely after one bump (p. 216).
- **Negative feedback amplifier** (invented by Harold Black in 1927). Gain is output voltage divided by input voltage. Tubes and transistors have gains that drift with time and signal strength, and feedback reduces the effect of that drift (pp. 216–217).
- **Figure XI-4 numbers** (pp. 217–218):
  - Ordinary amplifier, gain 10: 1 V in gives 10 V out. If gain halves to 5, output halves to 5 V.
  - Feedback amplifier: the upper box has gain 100. The lower box is an accurate divider, with no tubes or transistors, returning 0.09 of the output. With 10 V out it returns 0.9 V, so the upper box receives $1-0.9 = 0.1$ V.
  - If the upper box gain falls to 50, the output falls only about 10 per cent. Pierce says the figure's numbers are approximate. With higher gain in the upper box the effect would be even less.
- Pierce calls the importance of negative feedback hard to overestimate. Uses: telephone amplifiers, thermostats, chemical plants, missile guidance, autopilots. In the body: eye-to-hand when writing, ear-to-tongue in speaking, and body temperature and blood chemistry (p. 218).
- **Homeostasis** is the body's ability to keep a narrow range of conditions despite environmental changes (p. 218).
- **Ashby's homeostat** has feedback circuits with two means of changing them: one controlled by the machine, one by a person acting as its "environment". If the environment makes it unstable, it readjusts its circuits by trial and error until stable (p. 218).
- Pierce says the homeostat may be likened to a child learning to walk and then to ride a bicycle. **Wiener's view:** negative feedback is central to nervous control. Disabilities such as hand tremors are ascribed to failures of a body feedback system (p. 219).

> *Intuition note.* Negative feedback uses the output to push against its own error. The more inner gain there is, the less the output changes when that gain drifts. The cost is the risk of instability.

### Automata and complicated machines (pp. 219–225)
- Pierce counts three constituents so far: information theory, detection and prediction, and negative feedback. Computers and similar complex devices ("automata") are the fourth (p. 219).
- Studying earlier mechanical automata would add little to understanding today's machines. The opportunities for doing, and hence for thinking, are far greater now (p. 219).
- **Telephone switching.** Early systems were step-by-step: each dialed digit set up a new section of the talking path. Later systems are **common-control**: the dialed number is first stored, and other apparatus then searches for a free circuit and connects the call (p. 219).
- Modern nationwide networks are "by far the most complicated construction of man". They find an economical path, ring, time and charge the call, disconnect, report malfunctions, and keep working despite failures (pp. 219–220).
- **Relay** (electromagnet plus contacts that open or close circuits). In the thirties Stibitz of Bell Labs built a relay calculator for complex numbers. Bell Labs built more complicated relay computers in World War II, and Aiken built one at Harvard in 1941 (p. 220).
- Eckert and Mauchly built the Eniac, a vacuum-tube computer, shortly after the war for speed. More recently transistors have been used in place of vacuum tubes (p. 220).
- Components together with the art of interconnecting them provided the "body" of the machine. Interconnection mattered: Stibitz's and Shannon's use of Boolean algebra to describe and design relay circuits was "exceedingly important" (p. 221).
- The "spirit" is organization. Stibitz's first calculator took pairs of numbers by teletype and returned a result. By 1943 he had a relay computer reading instructions from a paper tape (program) (p. 221).
- **Branching.** The machine could refer back in the tape or use subsidiary tapes, which requires it to make a decision (p. 221).
- Pierce's example: sum a series term by term (the formula is not legible in the text layer). Stop when a term is below $1/1{,}000{,}000$. Decide by subtracting the latest term from $1/1{,}000{,}000$. If the result is negative, compute another term. If positive, print the sum and consult the program for further instructions (p. 221).
- **Von Neumann's idea** (credited as the next big step): put the program in the machine's memory rather than on tape. Then instructions are easily available and can be modified according to computation results (pp. 221–222).
- **Memory.** Modern machines store binary digits as magnetized cores in one of two directions. A group of cores holds a multidigit number, read in or out in a few millionths of a second. Each group has a binary **address** (p. 222).
- For arithmetic, two numbers are moved from memory into a register (temporary storage). The operation is done and the result is sent back to a memory address (p. 222).
- A program uses "a hundred or more" commands. The programmer can make the machine do "literally anything", provided he knows clearly what he wants and the task is feasible in acceptable time (p. 222).
- **Table XV** is a hypothetical program computing $c_i = a_i + b_i$ for $i = 1,2,3$, with $a_i$ at address $9+i$, $b_i$ at $12+i$, and $c_i$ stored at $15+i$. It starts at address 1 and comes to rest at address 9. Steps: START sets a start register (address modifier) to 0. CLEAN sets the add register to 0. UPPIT loads and adds the two numbers. DELVR stores the result. UPSRT raises the start register by 1. IFSRT tests it and either continues or jumps to 9. A final transfer returns to instruction 2 (pp. 222–223).
- **Compiler.** A program that examines an explicit statement of a task in standard words or equations and writes the detailed program for the computer. It saves the tedious writing of programs (pp. 223–224).
- Examples: Fortran (notation resembling mathematics), Blodi (circuit diagram to program that imitates the circuit), Janet (note specifications to a magnetic tape that plays the music) (p. 224).
- Binary digits can encode numbers, words, notes or logical operations. Uses listed: a Bible concordance, simulating telephone switching, recognizing spoken digits 0–9, checkers and chess, proving theorems, composing counterpoint (p. 224).
- Letters can be numbered so that alphabetical order matches numerical order, enabling sorting. Differences between note numbers can match musical intervals, so forbidding an interval equals forbidding a numerical difference (p. 225).
- **Limits.** Complicated uses cannot be explained in a few words. A talented person with a master's degree in mathematics reaches a fair understanding after a few years (p. 225).
- Not yet done by computers: recognizing spoken digits as accurately as a human, satisfactory translation, expert-level chess or checkers, identifying an important theorem, composing very interesting music (p. 225).
- Reason: programmers do not really understand some tasks. Trying has stimulated thought about speech recognition, language structure, game strategy and music (p. 225).
- **Pierce's criterion of understanding.** If a man says he understands a behavior or problem, Pierce says it is fair to insist that he demonstrate this by programming a computer to imitate it. If he cannot, his understanding is certainly incomplete, and it "may be completely illusory" (pp. 225–226).

> *Intuition note.* A computer is components plus interconnection plus a program. Storing the program in memory lets the machine change its own instructions. A compiler lets a person state a task compactly and have the machine write the long instructions.

### Can computers think? (p. 226)
- **Pierce:** the question is meaningless unless "to think" is defined (p. 226).
- **Minsky's fable:** a man beats everyone at chess and is praised as clever. He explains that he follows a set of rules, and people say it is "just mechanical" (p. 226).
- **Minsky's conclusion (as Pierce reports it):** people tend to regard as thinking only what they do not understand. Pierce adds that people often call almost any grammatical jumble of "important" words thinking. He would settle for useful, problem-solving, even mechanical, "thinking" (p. 226).
- Pierce says it seems likely that philosophers and humanists will keep the definition of thinking a step ahead of anything a machine does. He thinks it "probably impossible" to specify a meaningful, explicitly defined goal that a man can attain and a computer cannot, even Turing's "imitation game" (p. 226).
- **Imitation game:** a man communicates by teletype with either a man or a computer. He tries to tell which, and the computer is programmed to deceive. Pierce says a computer with any chance of success is far beyond today's machines, "if to any" (p. 226).

### Summary and verdict (pp. 226–228)
- Pierce recaps: communication theory; smoothing and prediction (Wiener's greatest contribution, a linear-prediction theory with weights smaller for older data); negative feedback (thermostat, autopilot, hand control, instability, Wiener's account of tremor, amplifiers used before the "day of cybernetics"); and automata (pp. 226–227).
- If all this is cybernetics, it includes most of the essence of modern technology, excluding the brute production and use of power, and our knowledge of the organization and function of man. Wiener adds sociological, philosophical and ethical problems (p. 227).
- Hence calling oneself a cyberneticist says little about one's competence, "unless he was a universal genius". It does not necessarily mean much knowledge of information theory (pp. 227–228).
- Pierce's closing view: if cybernetics is over-extensive or vague, this will do no real harm, and the word can add "a little glamor" (p. 228).

## Toy example (ours, not from the text)
Feedback amplifier with forward gain $A$ and a divider returning a fraction $\beta$ of the output. The input to the forward box is $V_{in} - \beta V_{out}$, so $V_{out} = A(V_{in} - \beta V_{out})$.

(added step) Solving: $V_{out}(1 + A\beta) = A V_{in}$, so $V_{out}/V_{in} = A/(1+A\beta)$.

Take $A = 200$, $\beta = 0.045$, $V_{in} = 1$ V:
- $A\beta = 9$, so $V_{out} = 200/10 = 20$ V. Check: the box input is $1 - 0.045\cdot 20 = 0.1$ V, and $200 \times 0.1 = 20$ V.
- Now let the tubes weaken so $A = 100$: $A\beta = 4.5$, so $V_{out} = 100/5.5 \approx 18.18$ V.
- The output fell $(20 - 18.18)/20 \approx 9.1\%$, while a plain amplifier whose gain halved would fall 50%.
- Pierce's own numbers ($A = 100 \to 50$, $\beta = 0.09$) give $10 \to 9.09$ V, about a 9% fall; the text says "about 10 per cent" (p. 218).

## Concepts
- [[cybernetics]] (new) — loose umbrella: information theory, prediction/filtering, negative feedback, automata, and life analogues (pp. 208–209).
- [[linear-prediction]] (new) — forecast = sum of past data each multiplied by an age-dependent number (p. 211).
- [[nonlinear-prediction]] (new) — any prediction method not of that multiply-and-add form (p. 213).
- [[smoothing-filtering]] (new) — filtering out frequencies where noise dominates; removing fast variation smooths the output (p. 215).
- [[negative-feedback]] (new) — output used to reduce departures from a desired behavior (p. 215).
- [[servomechanism]] (new) — device acting continually on information to attain a goal despite changes (p. 215).
- [[feedback-stability]] (new) — strong feedback may amplify deviations; linear systems are stable or not regardless of input (p. 216).
- [[homeostasis]] (new) — body's ability to hold conditions in a narrow range (p. 218).
- [[stored-program-computer]] (new) — program held in the machine's memory so it can modify its instructions (pp. 221–222).
- [[compiler]] (new) — program that turns a compact task statement into detailed machine instructions (p. 224).
- [[noisy channel]] — here contrasted: communication theory encodes for a noisy channel, prediction estimates the signal (p. 214).

## Canonical instances
- [[radar-gun-prediction]] — predicting an airplane's position from noisy radar; linear vs nonlinear (pp. 210–213).
- [[slepian-detection]] — under stated conditions, a faint signal in noise is detectable in principle by exact measurement over any short interval (p. 214).
- [[black-feedback-amplifier]] — halving the inner gain cuts output only about 10% (pp. 217–218).
- [[ashby-homeostat]] — machine that readjusts its circuits by trial and error to regain stability (p. 218).
- [[minsky-chess-fable]] — people tend to regard as thinking only what they do not understand (p. 226).
- [[imitation-game]] — Turing's test between man and computer (p. 226).

## Bridges (candidates)
- [structural-analogy] Prediction from noisy data ↔ information theory: both use statistics of signal and noise, but one estimates the signal and the other designs a code (p. 214).
- [structural-analogy] Feedback gain-stabilization ↔ control engineering: the output feeds back to cancel error, at the risk of instability.
- [metaphor] Minsky's "thinking = what we don't understand" ↔ philosophy of mind: the criterion for thought moves as machines advance.

## Questions this raises
- Why does stronger negative feedback tend to destabilize a system, and how is a safe amount chosen?
- What would an optimal nonlinear predictor look like, given that so little is known about them?
- How can Slepian's result (detection by exact measurement) coexist with the practical limits that noise imposes?
- Is "demonstrate understanding by programming it" a good criterion, as Pierce suggests?

## Reading notes
- Page offset: printed = pdf − 16 (pdf 224 = p. 208). All citations use printed numbers.
- The unit metadata warns that the PDF is the 1961 first edition, not the Dover 1980 edition. The running header reads "Symbols, Signals and Noise", consistent with that. The chapter heading appears as "CHAPTER y Cybernetics" (OCR of XI).
- Text layer is garbled in places (e.g. "hi 1948" for "in 1948"). The series formula on p. 221 is missing from the text layer, so it is not reproduced. In Table XV, the text layer has no label for instruction 8 and renders "9 + i" as "9 + 4". The table's step list is reconstructed from the commentary and the closing paragraph. The figures (XI-1 to XI-4) were not usable from the text layer; the numbers for Fig. XI-4 come from the prose on pp. 217–218.
- The text dates Turing's imitation game to 1936, as printed (p. 226).
- The chapter has no exercises.
