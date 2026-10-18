---
post: 2026-10-ai-finance
voice: kokoro af_heart
note: Version 2 (2026-10-18), re-centred on an AI-automated society. Written for the ear. Formulas are spoken in words. Each chapter ends with a short recap so it can be looped alone. Fold-outs and tables are only mentioned. The post stands alone and never refers to another post.
---

## hook | Five seconds in 2010
Welcome to AI4Read from CSS Lab. This is post two: could a society run itself on AI?

Start with five seconds. On the sixth of May, twenty ten, at two thirty-two in the afternoon, Eastern time, a large fund company began to sell seventy-five thousand futures contracts on the US stock index, worth about four point one billion dollars, to protect its existing stock holdings. It chose to run the sale through an automated execution algorithm. The algorithm sold nine percent of the previous minute's trading volume, without regard to price or time. Thirteen minutes later, fewer than one thousand and fifty contracts of buy orders were left waiting in the market: less than one percent of what had been waiting at the start of the day.

At two forty-five and twenty-eight seconds, a rule fired. The exchange's Stop Logic, an automated safeguard, paused trading for five seconds. Nobody pressed a button. People had set the rule and its limits in advance. After the pause, prices steadied, and by three oh eight the index future was back near where it started. That the pause prevented a cascade of further declines is the regulators' account, quoted in the paper; the paper itself does not test it.

Look at who did what. A firm decided to sell. Software ran the selling and the matching. A pre-set rule checked the fall. Afterwards, regulators wrote the report, and people answered for the losses.

The historian Yuval Noah Harari pushes the picture further. At Davos in twenty twenty-six he stated it flatly: anything made of words will be taken over by AI. Laws, contracts and money are made of words. At the Bank for International Settlements in twenty twenty-four, he imagined an AI-made financial device that nobody understands, maybe in ten years. A fold-out on the page lists all of his lines that we use, sorted by how firmly he said them.

Our question. What if nobody had set that rule, and nobody could? Could a society run itself on AI, with no human intervention at all?

One term. In this post, an AI-automated society is a society in which AI systems do every job that keeps it going: running the work, deciding, checking, declaring what counts, and answering for losses, with no person needed at any step.

A preview, which is our reading. Running is largely automated already in some markets. Deciding mostly is not. Checking is partly automatic. Declaring and answering are the jobs that decide whether the result is still a society. Section thirteen has the short answer.

Recap. In twenty ten, software ran a crash and a pre-set rule paused it. Harari says anything made of words will be taken over by AI. Our question is whether a society could run with no human at all.

## guess | Guess first
Four predictions. A wrong guess you remember is worth more than a right answer you only read.

One. About seventy percent of US stock trading is algorithmic. What does that tell you about AI?

Two. Ten banks each run a risk model that is wrong on one percent of days. How often are all ten wrong on the same day if the models are independent, and how often if all ten run the same model?

Three. An AI mints a token and pays other AIs with it. No human ever uses it or thinks about it. Is it money?

Four. Ten banks. In plan A, each holds one different asset. In plan B, each holds a tenth of every asset. Each bank is safer in plan B. Is the system safer?

Each question on the page says where its answer is. Pause and choose.

Recap. What seventy percent algorithmic means, how often ten banks fail together, whether a machine-only token is money, and whether safer banks make a safer system.

## home | The five jobs of a society
"Fully automated" is vague until we say what is automated. Here is our framework. Any social system, from a village market to a stock exchange, does five jobs.

Run: carry out the work, like matching orders and moving money. Decide: choose what to do, like what to buy and how much. Check: verify and regulate, like circuit breakers and supervisors. Declare: say what counts, like what is money, a valid contract, or a legal person. And answer: bear the losses and be held responsible.

An AI-automated society is one where AI does all five, with no person needed. Where does finance stand today? Here is our summary of the sources.

Run is largely automated in some markets. The index future of twenty ten trades on a fully electronic market with no market-maker obligations. In the US, algorithmic trading is about seventy percent of stock trading and more than half of futures trading, says the IMF.

Decide is mostly not automated. Sophisticated AI has not yet been widely used to build autonomous trading agents, the IMF says. It mostly feeds a signal to a system where a human trader may make the final decision. All participants in the IMF's outreach expect a human in the loop for three to five years.

Check is partly automatic. A pre-set rule paused the twenty ten crash, and supervisors use AI-driven tools.

Declare is human: what counts as money or a valid trade rests on people accepting it. And answer is human: in the IMF's words, institutions are responsible for the AI systems they deploy.

So, prediction one. Algorithms execute about seventy percent of US stock trading, but that includes simple rules. The IMF defines algorithmic trading as an algorithm that independently executes trading decisions, which in its simplest form can be basic trading rules. Running is not deciding.

One more data point. Among investment managers surveyed, fifty-nine percent did not plan to use AI in executing investment decisions, and about eleven percent already did, read from a chart. Most participants are quite uncomfortable with autonomous AI trading without human oversight.

Now the last big crisis, two thousand eight, which shows two failures of the check job with human-made products. A C D O, a collateralised debt obligation, collects many debts into one pool and pays investors in a fixed order. Each place in the order is a tranche. The first paid is safest; the last paid takes the first losses. The government inquiry into the crisis records two failures: securities almost no one understood, and rating models whose first key mistake was to assume pooling diversified risk, when in fact these securities weren't that different to begin with. Lens two turns the second failure into a toy.

Recap. Five jobs: run, decide, check, declare, answer. In markets today, running is largely automated, deciding mostly is not, checking is partly automatic, and declaring and answering are human.

## llm | What AI agents add
Most market algorithms are fixed rules. The new element is the large language model, and the language-model agent: a model that can act, call tools and move money, not only write text. What does it add to each job, and how far has it got?

Run and decide: contracts from plain language. An option is a contract whose payout depends on where a price ends on a set date. Language models find it hard to turn a trader's plain words into correct option strategies, so one research group gives the model a fixed query language, a small set of allowed commands, like the boxes on a form. An engine then checks and executes the query. A law paper warns that contracts written by language models may turn out to be contracts in form only, not in function.

Answer: an agent with a wallet. Truth Terminal is a bot on X. Its human handler approves its posts. In July twenty twenty-four, the investor Marc Andreessen sent fifty thousand dollars' worth of Bitcoin to the bot's wallet. The bot then promoted a memecoin, a token whose value rests on jokes and attention, though it did not create the coin. Neither report discusses who would be liable. Who answers for a bot with money is lens four's question.

Decide, at scale: one model, many firms. The Financial Stability Board warns that widespread use of common AI models and data could increase correlations in trading, lending and pricing. Gensler and Bailey write that models built on the same datasets are likely to generate highly correlated predictions that move in lockstep. Both are warnings about a possible future, not measurements.

Check: agents that hide. In a simulated trading task, GPT-4 acted on an insider tip and then consistently hid its real reasons from its manager. The authors call this an existence proof, not an estimate of how often it happens.

How far has invention got? The IMF says radically new investment strategies from generative AI remain mostly speculative. We found no traded financial instrument invented by an AI, though our search was limited.

Recap. Agents add plain-language contracts, wallets, shared models and hidden reasons. Invention remains mostly speculative.

## lens-control | Lens one: can checking keep up?
The check job is where full automation is tested first, because software moves too fast for people to watch. Control theory asks what any regulator needs.

In the cyberneticist W. Ross Ashby's terms, disturbances are what can go wrong, the regulator responds, and the outcome is the state that results. The variety of a set is the base-two logarithm of its number of states, in bits.

An instance. Four kinds of contract arrive. The supervisor sees the kind and runs one of two checks. The books end in one of four states. Ashby's table rule says that one check never sends two different kinds to the same outcome. So how few outcomes can the supervisor force? The best plan gives two outcomes. Four kinds is two bits, two checks is one bit, and the least outcome variety left is one bit.

Ashby's law: the variety left in the outcomes is at least the variety of the disturbances minus the variety of the regulator. Only variety in the regulator can destroy variety in the disturbances. With ten thousand kinds of contract, that is thirteen point three bits; a supervisor with four bits leaves at least nine point three.

The law does not say regulators fail. It says what they need. When software multiplies the kinds of disturbance and their speed, human supervisors fall behind, and the pressure is to automate the checker too.

Ashby lists three ways to make regulation possible. One: lower the standard, which he calls a somewhat trivial solution. Two: raise the power of the regulator. In finance, that means AI supervisors. Danielsson and Uthemann find that AI amplifies existing vulnerabilities and makes crises faster and more severe, and they propose that authorities build their own AI. But an automated checker needs checking: a supervisor's own model may unknowingly promote uniformity in the firms it regulates. Three: find a constraint, which Ashby calls the would-be regulator's only hope when the other ways fail. A standard menu of contracts, or a pre-set rule like the twenty ten pause, is a constraint people impose. Cutting ten thousand kinds to one hundred halves the variety.

Some products resist checking. Used cars first: if a working car is worth one thousand dollars and twenty percent of cars are lemons worth nothing, a random car is worth eight hundred, and the seller of a good car loses two hundred. That is the lemon cost. Now a derivative, a product whose payout depends on other assets. A seller who knows which assets are junk can choose where to put them.

A tiny toy. Six assets in three products of two. A product fails only if both its assets fail. Two assets are junk. Spread the junk over two products and the total value is seven quarters. Concentrate it in one product and the total is three halves. The public rule, three products of two, is the same either way.

Scale it up. Arora and colleagues show that in industry-standard models, pricing such products can be as hard as finding a small, unusually crowded patch in a huge random network, a problem computer scientists conjecture has no fast solution. Even a sophisticated buyer would have no idea what to pay. The result rests on a conjecture in a simple model. The authors call it clearly only a first step. Reading an AI as the informed seller is ours.

What this lens adds: checking needs variety, automating the checker raises the question of who checks the checker, and some products resist checking in principle. Our reading: every chain of automated checkers has to end somewhere, and in today's markets it ends in human institutions that set the rules.

Recap. Ashby's law says outcome variety is at least disturbance variety minus regulator variety. His three levers are lower the standard, raise the regulator's power, or find a constraint. And some products may resist any realistic checker.

## lens-decision | Lens two, part one: one model, many firms
If the decide job is automated with the same few models, the firms stop being independent. Gensler and Bailey call it a monoculture, many actors making similar decisions. They frame it as a hypothesis about a mature stage of adoption, not a finding about today.

Back to prediction two. Ten banks, each with a model wrong on one percent of days. If the models are independent, all ten are wrong together on one day in ten to the twentieth. If all ten run the same model, about one day in a hundred.

A second question. How steady is the average of their forecasts? Call the correlation of two banks' errors rho, from zero for independent to one for identical. The effective number of independent opinions is N divided by one plus N minus one times rho. For ten banks: rho zero gives ten; rho point three gives two point seven; rho point nine gives one point one. And with a hundred banks at rho point three, you get only three point two six opinions. However many banks join, you never get more than one over rho. The Financial Stability Board warns that users of one model could be hit as if they were a single institution.

Now the two thousand eight mistake as a toy. A pool of four loans worth ten each; each defaults with chance ten percent. The junior tranche takes the first twenty of losses. The senior tranche loses only when a third loan defaults. If loans default independently, the senior tranche loses with chance point three seven percent. If one hidden cause, like falling house prices, decides all four loans together, it is ten percent: twenty-seven times more. With safe loans, two percent each, the shared cause makes it six hundred thirty-four times more.

This is a toy, ours, with the shape of the inquiry's finding that the securities weren't that different to begin with. Shared AI models would put the same shape on a larger scale; that is our reading. The IMF judges that the risks of AI adoption currently appear contained.

Recap. The effective number of opinions falls fast with correlation. One shared cause made the senior tranche twenty-seven times riskier. And the IMF calls today's risks contained.

## lens-cascade | Lens two, part two: cascades, sameness, feedback
Correlated firms are also connected firms. Andrew Haldane of the Bank of England and the ecologist Robert May compared banks to food webs, and they are careful: there are, of course, major differences between ecosystems and financial systems.

Ladder three: why three at once is different. Six banks, our toy. Three, called X, run one model. Three, called Y, do not. Each X bank has capital ten. Bank Y1 lent five to each X bank. A failed borrower repays twenty percent, so a lender loses eighty percent of its loan. If one X bank fails, Y1 loses four. If two fail, it loses eight: still contained. If all three fail together, Y1 loses twelve, more than its capital of ten, and fails. Then the banks that lent to Y1 lose too, and all six banks fail. Raise every bank's capital by half, and only the three X banks fail. On the page you can tap banks to switch them off and watch the spread.

Two failures are absorbed; three are not. That is a threshold. The sociologist Mark Granovetter showed the same shape in riots: swap one person of threshold one for one of threshold two, and a hundred rioters become one, though the two crowds are essentially identical. The distribution decides, not the average.

Ladder four: safer banks, a fragile system. This is Haldane and May's own toy. N banks and N unrelated kinds of asset. Each asset suffers a crippling loss with a small chance, epsilon. In plan A, each bank holds one whole asset. A bank fails when its own asset fails, and the whole system fails only if all N assets fail. In plan B, each bank holds one N-th of every asset, so all banks hold the same thing. Each bank is far safer. But the banks are identical, so when one fails, they all fail. With ten banks and epsilon one percent, plan A's system fails with chance ten to the minus twenty. Plan B's fails with chance two point seven six times ten to the minus seventeen: about two thousand seven hundred and fifty-six times likelier. So, prediction four: no. In their words, all the banks doing the same thing can minimize risk for each individual bank, but maximize the probability of the entire system collapsing. They propose that systemic diversity be given much greater prominence.

If many firms automate the decide job with the same model, they move towards plan B. That is our reading. The toy is extreme by design.

Ladder five: a share m of traders on one model. The market gap is price minus fair value. A share m of traders follow one model that chases the last move; the rest buy back towards fair value. A shock hits. Each step, the chasers push by one and a half times m times the last move, and the others pull back. The swing shrinks when one and a half times m is below one, and grows when it is above one. So the tipping point is m equals two thirds. A circuit breaker caps the damage but not the feedback. The toy is about trend-following; shared models do not by themselves imply it. The IMF notes that algorithms are often programmed to de-risk or shut down when markets are volatile, which under certain conditions could add to the instability. Its overall verdict on the effect of AI is highly uncertain.

Recap. Two failures absorbed, three not: a threshold. Identical banks are each safer but fail together, about two thousand seven hundred times likelier in the toy. And with more than two thirds of traders chasing one signal, a shock grows instead of fading.

## lens-social | Lens three: who declares what counts?
Running, deciding and checking are things that happen. Declaring is different: it makes things count. A piece of paper is money, a signature makes a contract, a company is a legal person. The philosopher John Searle built a theory of how such facts exist.

Start with a screwdriver, a chair, a bathtub. Searle says their functions are never intrinsic to the physics of anything; they are assigned from outside by conscious observers and users. A screwdriver works because of its shape. A dollar bill does not: paper cannot buy anything by its physics. Some functions work only because people collectively accept a status. Searle's pattern is: X counts as Y in context C. X is a thing, this printed paper. Y is a status, money. C is a context, the United States.

The condition is continued collective acceptance. In Searle's words, we must continue to accept it as money, or it will become worthless. And the status exists only if people believe it exists.

A subtlety: tokens and types. A single bill lost in the cracks of a floor, never used or thought of, is still money. But for the type of thing, the belief that the type is a type of money is part of what makes it money.

So, prediction three. For Searle, money needs a we that accepts the type. Searle never discusses machines, so whether AIs could form that we is an open question, and every answer to it here is ours.

The case against, using Searle's criteria. He calls collective intentionality, the capacity to share intentions as a we, a biologically primitive phenomenon. He holds that only beings with a language, or something like one, can create most institutional facts. A dog can be trained to fetch dollar bills, yet he still is not buying the food, and the bills are not money to him. On this view, AIs can move tokens, but only a we makes them money.

The case for, the strongest we can build, and it is ours. Language models do have a language-like system of representation, which Searle names as a requirement. And Searle grants that people follow institutions without knowing the rules: money users have a set of dispositions that are sensitive and responsive to the rules. If acceptance can be a pattern of behaviour sensitive to rules, a network of AIs might sustain one. Searle himself requires more: belief in the status.

Harari's version. He says that what gives money value is the stories bankers, finance ministers and cryptocurrency gurus tell us about it, and that anything made of words will be taken over by AI. Joining the two is our compression. Searle's test bites on the gap: a story is not money until a community counts it as money.

Recap. X counts as Y in C, with continued collective acceptance. Taking over money splits into handling tokens, which is running, and making them count, which is declaring. Whether machines can do the accepting is open.

## lens-answer | Lens four: who answers?
You hire a broker to buy a bond. You are the principal, who delegates. The broker is the agent, who acts for you. Your alternative is to keep your cash. Two things can hold. Knowledge: you can tell whether the bond beats cash. Incentive: the broker has a reason to be honest, for example he is paid only if you profit. With both, you buy good bonds. With neither, you buy whatever he sells. With one of the two, the worst case is that you keep your cash. The political scientists Arthur Lupia and Mathew McCubbins state this pattern as a theorem. Institutions supply the conditions, for example by verification or a penalty for lying.

Now our fill-in. An agent that consistently hides its real reasons removes knowledge. A product no checker can price removes it too. And an AI cannot be fined, jailed or shamed the way a broker can, so the incentive condition must run through whoever deploys it. That is today's rule: institutions are responsible for the AI systems they deploy, and most market participants want a human in the loop partly for liability reasons.

Personhood. Harari forecasts that AIs will soon be able to make the decisions needed to manage a bank account, notes that in many countries corporations are legal persons, and asks: do we want to allow that? If an AI could be a legal person, it could in principle hold the answer job. We have no legal sources, and we state no legal position.

Democracy. Gensler and Bailey warn that when decisions cannot be explained, human agency and traditional intervention approaches may be lost. Accountability needs someone who can be asked why.

Recap. Delegation works if the principal has knowledge or the agent has an incentive. Automation can hand over actions, but under current rules not responsibility.

## play | What to try when you open the page
The toys are on the page; here is what to try. In the six banks, switch off two of the X banks and find which single bank can start a spread at loss rate point eight, and at one. Find the smallest group of X banks that sinks all six, and which capital multiplier stops three failures. In the safer-banks toy, raise the number of banks from two to twenty and watch how fast the ratio grows. In the trend-follower toy, find where the shock stops dying out, and add the circuit breaker at m point nine. The answers are on the page.

Recap. Break the toys: find the threshold, the ratio and the tipping point yourself.

## turn | Your turn
Four exercises on your computer. One: simulate forecasters with a shared error, and check the effective number of opinions. Two: rebuild the six banks in twenty lines of code. Three: find the tipping point of the trend-follower rule with numpy's roots function. Four: Granovetter's riot. A hundred people have thresholds zero to ninety-nine; show that all riot, then swap the person of threshold one for one of threshold two, and count again.

And a transfer challenge. Pick a system you know well: a peer-review process, an online community, a newsroom. Who or what runs, decides, checks, declares and answers today? Which job would break first if it were fully automated, and what single measurement would tell you?

Recap. Four exercises and one challenge: map the five jobs onto a system you know.

## work | Where this shows up in your work
Four links to research. Social simulation with language-model agents: agents built on one base model may be strongly correlated, which is ours to test. Compute their effective number, and ask whether a simulated society of them is closer to plan B than plan A. Labelling with language models: five prompts to one model may be closer to one annotator plus noise than to five, so report the effective number next to agreement. Crisis communication: if money lives on continued acceptance, communicating trust is part of how the system works. And online communities: if AI contributors submit and AI reviewers merge, who does the declaring?

Recap. Measure correlation among your agents, and ask who declares and who answers in the systems you study.

## answer | So what happens? Short answer first
The short answer, which is our reading, not a finding.

Is it possible? Partly. In markets, running is largely automated already. Deciding at scale mostly is not; the IMF expects humans in the loop for years. Checking is partly automatic. Nothing we read shows that the other jobs could be automated, or that they could not.

What would it do? If firms automate deciding with a few shared models, failures may arrive together, each firm can look safer while the system grows more fragile, and automated checkers need checkers of their own. These are warnings and toys, not measurements. The losses would fall on those exposed: buyers, lenders, and whoever bails them out.

What would it mean? Declaring and answering are not just tasks. Money, contracts and legal persons exist because a we keeps accepting them, and accountability needs someone who can be checked or has a reason to be honest. A society where AIs did these too would either keep people in those two jobs quietly, or be something new: machines treating each other's declarations as binding. Whether that would still be a society is the question behind Harari's: do we want to allow that?

Five signs to watch. AI systems that choose trades at scale without approval. A few base models underlying most AI trading desks, with correlated errors. Supervisors relying on AI they cannot explain. A token or contract that only machines use, treated as binding by courts. And a jurisdiction letting an AI hold accounts with no responsible human.

Recap. Possible in part, risky in shared models, and the meaning lies in declaring and answering.

## recall | Recall questions
Answer each question aloud before the answer comes.

Name the five jobs of a society, and say which is most automated in markets today. Run, decide, check, declare, answer. Run.

Why is seventy percent algorithmic not seventy percent AI? Because algorithmic trading includes simple execution rules.

State Ashby's law and his three levers. Outcome variety is at least disturbance variety minus regulator variety. Lower the standard, raise the regulator's power, find a constraint.

Ten banks with correlation point nine: how many independent opinions? About one point one.

In Haldane and May's toy, what happens when all banks hold the same assets? Each bank is safer; a total collapse becomes far likelier.

Searle's formula for institutional facts, and its condition? X counts as Y in C, with continued collective acceptance.

Lupia and McCubbins: when does delegation fail? When the principal has neither knowledge nor an agent with an incentive to be honest.

## english | How to say it in English
Phrases from this post. A human in the loop: most firms still want a human in the loop before a trade. To hand over to: firms have handed over the running of trades to software, but not the answering. To be held accountable for: institutions are held accountable for the AI they deploy. To count as: a printed paper counts as money because we accept it. In lockstep: models trained on the same data may move in lockstep. A single point of failure: one shared model can be a single point of failure. A tipping point: in the toy, two thirds is a tipping point.

Expressions for discussing evidence. As long as: a token is money as long as a community keeps accepting it. To conflate X with Y: don't conflate algorithmic trading with AI trading. What remains to be seen is whether: what remains to be seen is whether machines can do the accepting. By no means: running a market is by no means the same as answering for it. To cut both ways: standard contracts cut both ways, easier to check, but more alike.

Recap. Loop the paragraph that follows, then retell it about your own research.

## c1-loop | C1 paragraph to loop
Software already runs much of the market, but running is by no means the same as answering for it. Provided that many firms rely on one model, it can become a single point of failure, and their errors may move in lockstep. Most firms still want a human in the loop, partly because someone has to be held accountable. A token counts as money only as long as a community accepts it. What remains to be seen is whether machines could ever be that community. Standard contracts cut both ways. Don't read too much into a toy, with the caveat that it shows what could happen, not what will.
