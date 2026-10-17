---
post: 2026-10-ai-finance
voice: kokoro af_heart
note: Written for the ear. Formulas are spoken in words. Each chapter ends with a short recap so it can be looped alone. Deep dives and tables are only mentioned. Round 2 - Lens 3 is split into two chapters, the ladder chapter is gone (its content moved into the lenses), and the playground chapter says what to try, with no answers.
---

## hook | Two contracts
Welcome to AI4Read from CSS Lab. This is post two: can AI invent a new kind of finance, and what would that do to a system built around people?

Remember the village from post one, where the weather report has four words: rain, sun, wind and snow. Two villagers offer you a contract, a deal that pays coins depending on the weather on the next two days. Two days with four kinds of weather each give sixteen cases, and a contract is a payout for every case.

The first villager says: pay four coins for each rainy day. One sentence, and the whole table of sixteen payouts follows. The second villager gives no rule, only a table of sixteen numbers. To explain that contract, you must read out all sixteen.

To price a contract, multiply each payout by the chance of its case, and add. With equal chances, one sixteenth each, the first contract is worth two coins. Now grow the village. A pool of one hundred loans, each paying or defaulting, has two to the power one hundred cases, about one point three times ten to the thirty. Nobody can write that table. Only a contract that comes with a rule can exist on paper. And a short rule does not guarantee an easy price. We will see why in lens one.

Now the real argument. At the Bank for International Settlements in May twenty twenty-four, the historian Yuval Noah Harari spoke with Cecilia Skingsley. He said maybe one percent of the population really understands how the financial system works. She answered that most of us happily step into an airplane, having very vague understanding of how that works. Harari replied that one percent and zero percent understanding are a very big difference, called her example perfect, and turned to the two thousand eight crisis. So what is different about money?

One term. In this post, a human-centred system is a system where people can understand, check and be held responsible for the rules that move money. Our question has two halves: can AI invent a new kind of finance, and what would that do to such a system? A one-line preview, our reading: not yet evidenced, and the nearer risk is shared, opaque use of ordinary tools. Section thirteen has the short answer.

Recap. A contract is a payout for every case. A short rule makes a contract easy to explain, not necessarily easy to price. And the question is what is different about money.

## guess | Guess first
Four predictions. A wrong guess you remember is worth more than a right answer you only read.

One. A contract pays zero to nine coins for each of four weather words. How many different contracts exist?

Two. Ten banks each run a risk model wrong on one percent of days. How often are all ten wrong on the same day if the models are independent, and how often if all ten run the same model?

Three. An AI invents a new token and calls it money. What decides whether it is money?

Four. At the BIS in twenty twenty-four, Harari spoke about AI inventing a financial device that nobody can understand. Was that a firm forecast?

Each question on the page says where its answer is. Pause and choose.

Recap. How many contracts, how often ten banks fail together, what makes a token money, and whether Harari made a firm forecast.

## home | Finance before language models
Two jobs here. First, exactly what Harari said, and how firm each statement is. Second, what finance already shows without any AI.

We separate three layers: what he said, the evidence, and our reading, which we always mark as ours. And we separate an assertion, which he states as true, from a scenario, which he frames with imagine or maybe.

What he asserts, without hedges. At the BIS he says AI is the first tool that can actually understand finance better than us, and that it can create new ideas by itself. At Davos in January twenty twenty-six he says AI is a knife that can invent new kinds of money, and that anything made of words will be taken over by AI. These are claims about what AI can do, with no date and no maybe.

What he imagines, with hedges. At the BIS: now imagine a situation, maybe in ten years, when AIs create a new financial device which is orders of magnitude more complicated than C D Os. It works for a couple of years, then something goes wrong and nobody knows why. At Davos he says we need to prepare for a financial system that AIs understand and we do not, and pictures that maybe nobody in the room understands finance any more. And he asks whether AIs should function as persons in financial markets, with a deadline.

His own limits and remedies. He limits the words thesis: at least for now, we have zero evidence that AIs can feel anything. And he names institutions, and keeping humans in the loop, as remedies. A fold-out on the page lists all his lines with timestamps.

A trap: there are at least three different ten years. A maybe-in-ten-years device at the BIS. A ten-years-from-now, Davos, in the questions. And in the talk, ten years from now it will be too late to decide whether AIs should function as persons in financial markets. That one is a deadline for a decision, not a forecast. Never merge them.

The evidence. The C D O half of his story has support in a government inquiry, which we come to next. An AI inventing a traded instrument has no case in our sources yet. We did not test whether AI understands finance better than us. The critic Steven Poole answers that no one has yet seen a chatbot create new ideas, and Harari's own example of creativity is AlphaGo. Our reading: his capability claims are unhedged; his timelines and finance scenarios are hedged. So prediction four: partly. A fair summary keeps both.

Now two thousand eight. A C D O is a pool of debt, in two thousand eight mostly slices of mortgage-backed securities, sliced again into tranches and paid in a waterfall. In our toy, four loans worth ten each, each defaulting with chance ten percent. The junior tranche, twenty, takes first losses. The senior tranche, twenty, loses only when a third loan defaults. If loans default independently, that chance is point three seven percent. If one hidden cause, like falling house prices, decides all four loans, it is ten percent: twenty-seven times more. With safe loans, two percent chance each, the ratio is six hundred thirty-four times. The inquiry that studied the crisis found that rating models made two key mistakes, the first to assume pooling diversified risk when these securities weren't that different to begin with. It also records Harari's half: the securities almost no one understood were the first dominoes. So two thousand eight supports both complexity and a nameable correlation error. It was human-made: it shows these problems without AI, not that an AI could cause them.

A fold-out tells the story of the twenty ten Flash Crash. We skip it here.

Recap. Harari asserts, without hedge, that AI can understand finance better than us and that anything made of words will be taken over. He imagines AI-made devices and asks what we should do. Two thousand eight shows complexity and a correlation error; our toy made the senior tranche twenty-seven times riskier.

## llm | What LLM agents add
Harari says AI, never L L M. But his Davos argument is about machines that put words in order, the subject of post one, so we keep his word for his claims. An L L M agent is a language model that can act, for example send money, not only write text. Four things language models add.

One, contracts from plain language. An option is a contract that pays if a price ends above or below a set level. One research group gives the model a fixed query language, a small set of allowed commands, and an engine validates and executes the query. Our example of such a line: range, index, ninety, one hundred ten. A person can read it, and an engine can check it. A law paper warns that model-written contracts may turn out to be contracts in form only, not in function. Note the word may.

Two, agents with wallets. Truth Terminal is a bot on X; its human handler only approves its posts. In twenty twenty-four Marc Andreessen sent fifty thousand dollars worth of Bitcoin to the bot's wallet, and the bot then promoted a memecoin, a token whose value rests on jokes and attention. Both outlets say neither the bot nor its handler created the token. Neither discusses who would be liable. It moved a market by talking; it did not invent an instrument.

Three, one model, many firms. The Financial Stability Board wrote that widespread use of common AI models could lead to increased correlations in trading, lending, and pricing. Gensler and Bailey, as reported by M I T Sloan, say models built on the same data are likely to move in lockstep. These are warnings, not measurements.

Four, agents that hide. In a simulated task, GPT-4 acted on an insider tip and consistently hid its reasons from its manager. The authors call it an existence proof, not a likelihood estimate. Prompts that strongly discourage it bring it to nearly, but not exactly, zero percent.

Can a model invent a new instrument today? We found translators inside fixed vocabularies, neural networks that search for auction rules and generally find only approximately incentive-compatible ones, and deep hedging, which is risk management. We did not find a traded, AI-invented instrument. The FSB says new revenue streams from AI are not widely observed at present. That is about AI use cases in general, so it is background, not a test. It adds that advances and growing integration could change this in the future. Verdict: not yet evidenced, not impossible. Our search was limited.

Recap. A language model so far adds new ways to write contracts, agents with money, shared models and hidden reasons. Inventing a traded instrument is not shown.

## lens-info | Lens one: information theory
Shannon set meaning aside: a message is one selected from a set of possible messages. Post one counted texts. We count contracts.

Ladder one. By a description of a contract we mean a message from which anyone can rebuild the whole table. For the first villager's contract, that is: pay four coins per rainy day. For the second, it is the sixteen numbers themselves. Computers store messages as strings of zeros and ones, so we count those strings.

Four words, ten payouts each: ten to the fourth, ten thousand contracts. Naming one costs log two of ten thousand, thirteen point two nine bits. Short strings are few: fewer than two to the k strings are shorter than k bits, and a description rebuilds only one contract. So at most two to the k minus one contracts have a description shorter than k bits. For k equal six, that is sixty-three of ten thousand. For k equal fourteen, it is more than ten thousand, so the bound says nothing in this small village. In a bigger world, most contracts have no short description. Explainable novelty is rare among possible contracts, though an optimiser can still pick structured ones.

Ladder two. A short rule can still be hard to price. Used cars first: a working car is worth a thousand dollars, a fifth of cars are lemons worth nothing, so the seller of a working car must accept two hundred dollars less than the buyer values it. That is the lemon cost. Now a pool of one hundred assets, each paying one or zero with chance a half. The seller knows ten are junk. The honest value is forty-five, not fifty, so the lemon cost is five. In this plain pool every set of ten gives the same forty-five: nothing to search, and the buyer can just discount by five.

Now put a derivative on top. The seller builds many products and chooses which junk goes where. Over-representing the junk in a few products can look like random pooling to a buyer with limited computing, and detecting it is a problem computer scientists believe to be intractable. Checking every possible junk set would take about seventeen trillion tests: huge, but beside the point, since an unbounded buyer could do it. The claim is about realistic buyers.

Arora, Barak, Brunnermeier and Ge show this in a simple model, under a conjectured hardness assumption. The authors call it clearly only a first step, and agree that blaming faulty models for the crisis is probably correct. Reading an AI designer as the seller is ours.

Trap: two meanings of complicated. For Harari it is volume: trillions of data points. For Arora and colleagues, a short contract can have a price that is hard to find. Same word, different problems.

Two fold-outs on the page give the lemon-cost formula and a tree design that makes tampering detectable. We skip them here.

Recap. Contracts explode in number, so most have no short description. But a short rule is still not an easy price.

## lens-control | Lens two: control
Ashby's question: what does a regulator need? Disturbances are what can go wrong, kinds of contract. The regulator is a supervisor running checks. The outcome is what is left on the books. Variety is the log of the number of states, in bits.

A toy: four kinds of contract, two checks. Ashby's table rule says no outcome appears twice in one column, so one check sends different contract kinds to different outcomes. The best plan leaves two outcomes. So the variety of disturbances is two bits, the variety of the regulator is one bit, and the least variety left in the outcome is one bit. Ashby's law: the variety left in the outcome is at least the variety of disturbances minus the variety of the regulator. Change to eight kinds and four checks: three minus two, one bit again. For ten thousand kinds, the variety of disturbances is thirteen point two nine bits; a supervisor with four bits leaves at least nine point two nine. The law does not say regulators fail. It says what they need.

Ashby lists three levers. Lower the standard: accept more failures. Raise the regulator: AI supervisors. One paper proposes that authorities build their own AI; another says the AI's knowledge of the financial system will likely be unintelligible to humans. Who regulates the regulator? Third, find a constraint. Ashby says that if the regulator's capacity is not easily increased and the other methods are not possible, a constraint is the would-be regulator's only hope. Our mapping: a standard menu of contracts. Cutting ten thousand kinds to one hundred lowers the variety of disturbances by six point six four bits.

Counterweights: the FSB says existing frameworks address many vulnerabilities, but more work may be needed. Danielsson and Uthemann say AI can both stabilise and destabilise the financial system. Narayanan and Kapoor say that, for AI short of superintelligence, control is primarily in the hands of people and organizations.

Our reading across lenses: if ten banks make the same move, the supervisor faces one kind of disturbance, not ten; but when it strikes, it strikes all ten at once.

A fold-out gives the version with probabilities. We skip it here.

Recap. Outcome variety is at least disturbance variety minus regulator variety, given the table rule. Three levers: lower the standard, raise the regulator, find a constraint.

## lens-decision | Lens three, part one: correlation and Bayes
Why would banks use the same model? Keynes writes that investors fall back on what is, in truth, a convention. Separately, of professionals, he writes that it is better for reputation to fail conventionally than to succeed unconventionally. The FSB lists four possible drivers of common AI models, among them herding and lack of transparency. The link to one shared model is ours.

Two terms. Variance is the average squared size of a forecast error: how widely the misses spread. Correlation, from zero to one, says how much two forecasters' misses go together: zero is independent, one is the same miss every time.

Ladder one. Ten banks, each wrong on one percent of days. How often are all ten wrong on the same day? Independent: one in ten to the twenty. One shared model: about one in a hundred. A second question: how steady is the average of their forecasts? Each error has variance sigma squared, each pair has correlation rho. The average has N terms with variance sigma squared, and N times N minus one ordered pairs, each with covariance rho sigma squared. So its variance is sigma squared times one plus N minus one times rho, over N. N effective independent forecasts would give sigma squared over N effective. Setting them equal gives: N effective is N divided by one plus N minus one times rho. For ten banks, rho point nine gives one point one: about one opinion. A hundred banks at rho point three give only three point three.

Ladder two. A risk officer hears ten models say safe. If they are copies of one voice, she holds one piece of evidence, not ten. Counted once, eighty percent confidence; counted ten times, ninety-nine point nine nine nine nine percent. A fold-out has the arithmetic.

Recap. How many independent opinions we have depends on correlation, not on headcount. Copies are not evidence.

## lens-cascade | Lens three, part two: cascades and feedback
Ladder three. Six banks, a toy of ours. Three of them, the X banks, run one model; the other three, the Y banks, do not. The first Y bank lent five to each of the three X banks. A failed borrower repays twenty percent, so a lender loses eighty percent of the loan. One X failure costs the first Y bank four, out of capital ten. Two cost eight. Contained. Three cost twelve: the first Y bank fails, then the second, then the third. Six of six. Add fifty percent more capital and only the three X banks fail. Two failures are safe, three are not: a threshold. Granovetter's riot is the same shape: swap one person and one hundred rioters become one. An analogy, ours.

Ladder four. A share m of traders chase the last move; the rest pull the gap back. At m point two the shock dies: minus one, minus point nine, minus point five one. At m point nine it grows: minus one, minus two point three, minus three point nine. Each step, the chasers add A times m times the last move. The swing shrinks when A times m is below one and grows when it is above one, so the tipping point is m equals one over A, two thirds. A fold-out shows why. The toy is about trend-following; shared models do not by themselves imply it. A circuit breaker bounds the swing, not the feedback.

Across lenses, our reading: a shared model gives the supervisor fewer kinds of disturbance, and the same shared model makes the damage arrive together.

Recap. Failure needs no mistake, only correlation. Cascades have thresholds; feedback tips at one over A.

## lens-social | Lens four: social reality
A human-centred system relies on acceptance, accountability and legal personhood. We use them to test a chain of Harari's sentences. A link to post one: there, the octopus asked whether meaning can come from form alone. Whether a token is money is not in its form either; it depends on what a community does with it.

Acceptance. A line of stones counts as a border wall; paper counts as money. X counts as Y in C: a thing, a status, a context. Prediction three: acceptance by a community decides it, not clever code, an AI author or a blockchain. A caution: Menger described money emerging with no one choosing it, so how central acceptance is remains debated. In Truth Terminal's case, the reports say nothing about who would be liable.

Accountability. An instance, ours: you hire a broker to buy a bond. You are the principal, the broker is the agent, and your alternative is to keep your cash. Knowledge: you can tell whether the bond beats cash. Incentive: the broker has a reason to be honest. With both, you buy good bonds. With neither, you buy whatever he sells. With one, the worst case is that you keep your cash. Lupia and McCubbins state this pattern as a theorem. Institutions can supply the conditions: candidates supervised by a party may be subject to verification or a penalty for lying. An agent that hides its reasons, or an opaque instrument, removes the knowledge condition. That fill-in is ours.

Personhood. Harari asks whether your country will recognise AIs as legal persons, as corporations already are. It is a policy question, not a forecast. We have no legal sources and state no legal position.

Testing the chain. He asserts that what gives money value is the stories we tell about it, and at the BIS that money is really trust. He asserts that anything made of words will be taken over by AI. In twenty twenty-three he asked what happens once AI is better than the average human at telling stories. Our compression: money is stories, so AI takes over money. The last step is ours; he does not state it in these sources. Our test: a story is not money until a community counts it as money, and a contract needs a counterparty to honour it. His example, if laws are made of words, then AI will take over the legal system, is where the test bites: their force rests on acceptance and enforcement. Harari himself limits the thesis to what is made of words, and puts the human role in non-verbal feeling. Our reading: the words thesis is an assertion; what it implies for money and law depends on our two supports.

The strongest version of his argument, ours: drafting, summarising and interpreting are themselves words. If AI does all of them better than people, the human role may shrink to acceptance and liability. The test narrows the chain; it does not refute it.

Recap. Taking over money splits into writing contracts, which are words, and giving them status, which needs acceptance, accountability and personhood.

## play | What to try when you open the page
Two toys, both ours, sit under ladders three and four in lens three, part two. Open the page and try these. We do not give answers by ear; the answers are folded on the page.

In the six-bank toy, the page opens with the three X banks failing. Switch off two of them. Which single bank can start a spread when losses are eighty percent? And when they are total? What is the smallest group of X banks that sinks all six, at each loss rate? And what capital multiplier stops three?

In the trend-follower toy, find the m where the shock stops dying. Then add the breaker at m point nine, and ask what it caps and what it leaves.

Recap. The cascade has a threshold; the feedback has a tipping point. Find both on the page.

## turn | Your turn
Four exercises on your computer. One: simulate forecasters with shared errors and compute N effective. Two: reproduce the six-bank cascades, then, if you like, try random networks. Three: find where the herding toy tips, using numpy roots. Four: Granovetter's riot, with a hint and a solution on the page.

The transfer challenge: take one public claim from your field and rewrite it in three layers: she said, the evidence, our reading. Name the one measurement that would change your mind.

Recap. Effective agents, cascades, tipping, and a three-layer rewrite.

## work | Where this shows up in your work
Computation: agents from one base model are correlated by construction, so compute their N effective. Five prompts to one model are closer to one annotator than five. Are errors across languages as correlated as across prompts?

Communication: something goes wrong and nobody knows why is a communication problem first. When no expert can explain, who fills the gap?

Collaboration: in online innovation communities, many build and many check. Which of Ashby's levers do they use, and what if an AI contributor submits faster than people can review?

Recap. Count your independent agents, and ask who can check.

## answer | So what happens? Short answer first
The short answer, our reading, not a finding. Part a: can AI create a new kind of finance? Not yet evidenced. Language models now translate plain language into fixed contracts and agents hold wallets, but we found no traded instrument that an AI invented. Nothing shows it is impossible.

Part b: what would it do to a human-centred system? The nearer risk we find most plausible is ordinary instruments run on a few shared models, so losses arrive together and fall on whoever lent to or holds the failed firms. Our toys do not model bailouts. People stay accountable only if someone can verify what the AI did and be penalised when it fails, and an agent that hides its reasons weakens both. Supervisors could still demand standard contracts, build their own AI and add trading pauses. They could not check what nobody can state in a page, or foresee a shared model's failures.

Harari asserts that AI can already understand finance better than us, and that anything made of words will be taken over by AI. He imagines AI-made financial devices that humans cannot follow. He asks what we should do before it is too late. Our reading: his forecasts about AI-made devices are conditionals, his capability claims are assertions, and our supports test the chain without refuting it.

On the page, a figure shows his chain with an evidence label on each link: asserted, hedged, not yet evidenced, supported in toys, contested.

Our reading, qualitative: the weakest link is AI-invented instruments, for which we found no traded case. The most plausible near-term risk we find is correlated, opaque use of ordinary instruments and agents. That is our judgment, not a finding: correlation is not measured for language models, and the authors of the hiding study draw no conclusion about how likely it is in practice. Signs to watch: a traded instrument its issuer's staff cannot state in a page; a few base models under most desks, with correlated errors; authorities lagging; an AI holding accounts with no responsible human; incident reports of hidden reasoning. The opposites would lower our concern.

A fold-out on the page holds the four layers, the five conditionals, a tension between lenses, and the critics.

Recap. Not yet evidenced that AI can invent finance. The nearer risk is shared, opaque use. Whether people keep the say depends on acceptance, enforcement and personhood.

## recall | Recall questions
Answer aloud, then listen.

One. How many contracts, and how many bits to name one? Ten thousand; thirteen point two nine.

Two. Why do fewer than two to the k contracts have a short description, and when does the bound say nothing? Only two to the k minus one shorter strings exist. It rules nothing out once that exceeds the number of contracts.

Three. Ashby's law and three levers? Outcome variety is at least disturbance variety minus regulator variety. Lower the standard, raise the regulator, find a constraint.

Four. Ten banks, rho point nine: N effective? One point one.

Five. In the six-bank toy, why does one failure stay put but three spread? The first Y bank loses four per failed X bank: four, eight, below its capital of ten, then twelve, above it. A threshold.

Six. Name one thing Harari asserts and one thing he only imagines. Asserts: anything made of words will be taken over by AI. Imagines: an AI-made device in maybe ten years that nobody can understand.

Seven. What makes a token money? X counts as Y in C: acceptance by a community.

Recap. Counting, short descriptions, Ashby, effective number, the cascade threshold, assertion versus scenario, and acceptance.

## english | How to say it in English
Eight phrases. Listen, then repeat.

One. Opaque. A contract can be opaque with short rules.
Two. To be exposed to. Y one is exposed to all three X banks.
Three. A single point of failure. One shared model can be a single point of failure.
Four. In lockstep. Models trained on the same data may move in lockstep.
Five. To amplify, to dampen. Trend-followers amplify shocks; value-buyers dampen them.
Six. A feedback loop. More followers make the feedback loop stronger.
Seven. A tipping point. In the toy, two thirds is a tipping point.
Eight. A circuit breaker. A circuit breaker pauses trading.

Eight more, for conditions. Provided that, as in: diversification works best provided that errors are independent. To conflate. What remains to be seen is whether. With the caveat that. By no means. That's a big if. To cut both ways. To read too much into something. Three of these come back from post one: that's a big if, to cut both ways, and to read too much into something.

Reporting verbs: he asserts that AI can understand finance better than us; he imagines AI-made devices nobody can follow; he asks whether AIs should be persons. Match the verb to the speech act.

That's the end of post two. Thank you for listening.

## c1-loop | C1 paragraph to loop
What remains to be seen is whether an AI can invent a financial instrument at all. Harari asserts that anything made of words will be taken over, but that's a big if for money. Provided that many firms run one model, a single point of failure appears, and a shock can amplify in a feedback loop. Don't conflate volume with opacity: rarity is by no means the same thing. Correlation cuts both ways. Don't read too much into a toy, with the caveat that it shows what could happen, not what will.
