---
post: 2026-12-surprise
voice: kokoro af_heart
status: written and checked at S4, revised at S5 round 1; audio NOT recorded (Kunhao reviews the text first)
note: Written for the ear. Formulas are spoken in words. Widgets are described, not read. Fold-outs and tables are only mentioned. Each chapter ends with a short recap so it can be looped alone. Page numbers are not read aloud. The post stands alone and never refers to another post. Chapter ids match the section ids of the page.
---

## hook | Counting messages, and what the count misses
Welcome to AI4Read from CSS Lab. This is post four: how much is a surprise worth?

Here is the answer in one line, so you can hold it while you listen. A surprise is worth the number of fair yes or no questions it saves you. The rarer the news, the more questions it saves. And the average over all the news a source can send is called its entropy.

Start with the pain, and this is our own point. Take a town where it rains most days. The weather office sends one report a day from a fixed list. It rained today, and it snowed in July, are each one pick from that list. So a measure that only counts the possible reports gives them the same number. Yet the first tells you almost nothing, and the second is news.

Counting is how engineers measured messages in the nineteen twenties. Pierce, in his nineteen sixty-one book, reports Nyquist's result of nineteen twenty-four: the speed of a telegraph line depends on how many different current values it can send. Three values, plus, zero and minus, raise it, in Pierce's words, by sixty per cent over two. In nineteen twenty-eight Hartley measured a message by the number of messages the sender could have picked. In fact he used a function of that number, which step one explains. Pierce says this is acceptable only if successive symbols are chosen independently, and each is equally likely to be selected. Hartley saw that some letters are chosen more often than others, E more than Z, and that this should govern the lengths of signals. What was missing, in our reading, was a number that weighs each message by how likely it is. This post builds it in a coffee shop, checks it in a village, and asks what it leaves out.

Now a guess, before you read on. A submarine hides in one of sixty-four squares, and every square is equally likely. You fire at one square and miss. Count news in yes or no questions: a piece of news is worth the questions it saves you. How many questions is that miss worth? Option one: almost nothing, a few hundredths of one question. Option two: about one question, because a plain no is still an answer. Option three: exactly nothing, because you still do not know where it is. Option four: about six questions, the same as finally finding it. Pause and choose. The answer comes in step four, the submarine.

Recap. Old measures counted possible messages, and they fit only independent, equally likely choices. A count cannot tell news from non-news. We want one number that weighs each message by how likely it is.

## cafe | The café with a hatch
Picture a loud café. The grinder drowns every word, so customers and barista cannot talk, and the barista works in a back room where she never sees a customer. Orders pass through a hatch on paper tickets. The same card hangs on the wall by the till and on the wall in the back room: a list of yes or no questions in a fixed order. The customer answers the card's questions on the ticket, one after another, and stops at the first yes. Every answer costs one second of the queue's time. The owner knows from the cash register's record that out of every eight regulars, four want a flat white, two a latte, one a mocha and one a matcha. What should the card say?

The old way: split the menu. The menu board is a grid with two drinks on top and two below. The card asks, is your drink on the left side of the board? And then, is it the top one? Every ticket has two answers, and the barista always knows the drink. But half of the regulars want the flat white and spend two answers each, and the one regular in eight who wants matcha spends the same two. The card split the drinks into equal halves, and ignored how many customers stand behind each drink.

The rule that changes: split the customers. The card now says: flat white? Latte? Mocha? And the customer stops at her first yes. A yes to the first question settles four customers out of eight with one answer. A no leaves four. A yes to the second settles two more. A no leaves two. A no to the third leaves only the matcha, so the card needs no fourth question. The flat white costs one answer, the latte two, the mocha and the matcha three each. Over eight customers that is four plus four plus three plus three: fourteen answers. One and three quarters for each customer, against two for the old way. The rare drinks cost more, and that is fair. A matcha order is unusual news. The rarer the order, the bigger the surprise, and the more questions it is worth.

On the page, two small diagrams show the two cards. In the old way every drink costs two questions. In the new way the costs are one, two, three and three.

Three checks. If the card began with matcha, most tickets would start with a no, which rules out only one customer in eight. A question helps most when both answers are likely. If all four drinks sold equally, the clever card would save nothing.

Who does what. The customer knows the drink and holds the card. Following it, she turns her drink into a row of yes and no on the ticket, for example no, no, yes. The ticket goes through the hatch. The barista never sees the customer. She sees only the ticket, and she holds the same card. She reads the ticket against the card and names the drink. The ticket alone says nothing. No, no, yes means mocha only under this card, so the same card must hang on both walls before the day starts. We call the card the script, and the row of answers on a ticket its string.

The parts of the café, which the next sections use by name: the four drinks; the share of regulars who want each drink; one question on the card; the script, which is the card, the same on both walls; the customer, who fills in the ticket; the ticket, the string of answers; the barista, who sees only the ticket; a drink's cost, the answers on its ticket; the day's average; and the menu-board card, the old way.

Check yourself. First: which customers get the longest tickets, and why? Pause. The mocha and matcha customers, three answers each. Each is one regular in eight. The card spends its questions where the customers are. Second: a day comes when all four drinks sell equally. Would the clever card still be best? Pause. No. The average would be one plus two plus three plus three, divided by four: two and a quarter. The plain board costs exactly two. A card is built for the shares it was made for.

Recap. Split the customers, not the menu. Common drinks get short tickets, rare drinks long ones, and the average falls from two to one and three quarters. The customer, holding the drink and the card, writes the ticket. The barista, holding only the ticket and the same card, names the drink.

## village | The weather village, equal chances first
Now leave the café for the field's own setting. A village radio sends one word a day: rain, sun, wind or snow. The shares of days are one half, one quarter, one eighth and one eighth, the owner's numbers with drinks swapped for weather words. Shannon's example uses these shares, and so do Cover and Thomas. We call each symbol a day, and we assume days are independent, though real weather is not like that. Each equation is followed by a line that starts, in the café, and names the café parts it stands for.

Three words need fixing. Worth means the number of fair yes or no questions an outcome saves you, not usefulness. A question is fair when its two answers are equally likely. Surprise means how unlikely an outcome was under a stated model of the source, a list of how likely each message is. It does not mean a feeling. Information is used in Shannon's engineering sense: one choice from a set of possible messages. Pierce says the confusion about how communication theory relates to physics is sometimes aggravated when more than one meaning of information creeps into a discussion.

Step one: equal chances, count the halvings. A guess first. One of thirty-two cups of water is poisoned. A rat that drinks any poisoned cup dies within the hour, and you have one hour. All the rats drink at the same time, each from any cups you choose. What is the smallest number of rats that is always enough? Four, five, six or eight? Pause. The answer is at the end of this chapter.

The cups and rats are our framing. In MacKay's version one of sixty-four integers is chosen. MacKay writes: intuitively, the best questions successively divide the sixty-four possibilities into equal sized sets. Six questions suffice.

With thirty-two cups, one good question halves them: thirty-two, sixteen, eight, four, two, one. That is five halvings. The rats ask all five questions at once, because each rat's fate, dead or alive, is one yes or no answer. Thirty-two is two multiplied by itself five times, and sixty-four is six times. One answer of a fair yes or no question is one bit, a word Shannon credits to J. W. Tukey. Here it is a unit of worth. From now on, questions and bits name the same unit.

The formula, equation one. For N equally likely options, where N is a power of two, the number of questions k satisfies: N equals two to the power k. So k is the log, base two, of N. In words: the number of questions is the number of times you must halve N to reach one. The log, base two, asks: two multiplied by itself how many times gives this number? For other N, MacKay's raw bit content is a lower bound for the number of binary questions that are always guaranteed to identify an outcome. Guaranteed means in the worst case, not on average. That gloss is ours.

The check. The log, base two, of thirty-two is five, and of sixty-four, six. Cover and Thomas open with the same case, five bits. What it does not say: four rats cannot decide thirty-two cups, because two to the fourth is sixteen, and sixteen is less than thirty-two. That is ours.

In the café. N is the number of drinks on the menu when all sell equally, each with the same share. k is the number of questions on a ticket. The two in two to the k is the two answers to one question. Halving the board is the menu-board card, the old way.

The answer to the guess. Five rats. Each rat gives one yes or no answer, so five rats give five answers at once, enough to tell thirty-two cups apart. Four rats give only sixteen outcomes.

A fold-out on the page, Nyquist and Hartley in symbols, goes deeper. It records that Pierce's eight values give four times the speed, an apparent slip: by Nyquist's rule it is three times, our computation.

Recap. With equal chances, the number of questions is the number of halvings, the log, base two, of the number of options. One answer is one bit. Thirty-two cups need five rats.

## surprisal | Step 2: unequal chances, surprisal
Step two. The village again: rain one half, sun one quarter, wind one eighth, snow one eighth. The best questions go like the card: rain? Then sun? Then wind? And then only snow is left. Rain costs one question, sun two, wind three and snow three. Write yes as zero and no as one, and the strings are zero, one-zero, one-one-zero and one-one-one.

What rule gives the number of questions an outcome costs? A share of one half means halving the crowd once, one quarter twice, one eighth three times. The cost is how many times you must halve the whole crowd to be left with a group the size of that share.

The formula, equation two. For an outcome x whose share is P of x, the cost, h of x, is the log, base two, of one over P of x. In words: the surprisal of x is the log, base two, of one over the share of x. MacKay calls it the Shannon information content. Gibson and colleagues say surprisal, and information content. We use the word surprisal.

The check. For snow, the share is one eighth, and the log, base two, of eight is three. The four words give one, two, three, three, as the questions did. On the page, a slider moves the chance of an event. Share zero point zero zero one is worth ten questions, zero point zero one gives six point six, zero point one gives three point three, and zero point five gives one. Those are MacKay's numbers. At share one, the worth is zero: a sure thing tells you nothing.

A second concept: independent days add. Rain today, snow tomorrow. The pair has share one half times one eighth, one sixteenth, and the log, base two, of sixteen is four. The separate costs are one and three, and one plus three is four. In general, for independent x and y, the chance of the pair is the product, and a log turns a product into a sum. That is equation three: the surprisal of the pair is the surprisal of x plus the surprisal of y. MacKay's reason is that we might want any measure of the amount of information gained to have the property of additivity. It needs independence, which the village assumes.

What it does not say. Only shares that are powers of one half, one half, one quarter, one eighth, one sixteenth and so on, cost a whole number of questions. That is ours. A share of zero point three would cost one point seven four, and a question cannot be asked one point seven four times. So Gibson and colleagues say the information content approximates the length of the shortest uniquely decipherable script: one whose rows of answers can be cut back into words in only one way. Step six returns to this.

In the café. x is a drink, here a weather word. P of x is its share. h of x is the drink's cost: the answers on its ticket. Additivity is two customers in a row, their tickets joined.

Recap. The surprisal of an outcome is the log, base two, of one over its share. Rain costs one, sun two, wind and snow three. Surprisals of independent events add.

## entropy | Step 3: the average, entropy
Step three. Take eight days that match the shares: four rain, two sun, one wind, one snow. Rain costs one question each, sun two, wind three, snow three. The total is four plus four plus three plus three, fourteen questions in eight days: one point seven five per day. What one number describes the source? Weigh each word's cost by how often it comes, and add.

The formula, equation four. The entropy H of a source is the sum, over all words, of the share of the word times its cost. That is the average surprisal. The sigma sign means add up. An outcome with share zero contributes zero, by a convention in MacKay's book. For the village: one half times one, plus one quarter times two, plus one eighth times three, plus one eighth times three, equals one point seven five.  Cover and Thomas get one point seven five for the same tree. Before and after the crucial change: two-question labels cost two questions a day, and the script built for the shares costs one point seven five.

On the page, a widget sets four weights, for rain, sun, wind and snow. The bars show each word's part of the average, its share times its surprisal, and they add up to the entropy. Try all equal: the entropy is two, the most possible for four words. Try only rain: the entropy is zero, and Shannon writes that no channel is required. Try reversed: the entropy is still one point seven five, because it depends only on the shares. A last button sets shares zero point seven and three times zero point one; keep it for step six.

A script has its own average, equation five. A script that spends L of x questions on word x averages the sum of the share times L of x. We write it E Q, short for the expected number of questions. The village script on the village: one point seven five, which equals H. On a village where all four words have share one quarter, the same script averages one quarter times one plus two plus three plus three, which is two point two five. That is worse than the two of plain labels. On only rain it averages one. The village script averages H only for its own shares, and it can cost more on others.

What it means. We measured the average number of fair questions per word, for a source whose shares we assume are known. It does not say what a word means, or how good the script is on other shares.

In the café. The sigma means go through the day's customers. P of x is a drink's share. The log of one over P of x is its cost. H is the day's average under the best script. E Q is the day's average for whatever script hangs on the wall.

Check yourself. Predict first: what does the village script cost on a day when all four words are equally likely? Pause. Two point two five. The script spends one, two, three, three questions, and with equal shares each count weighs one quarter. The script was built for the village shares.

Three fold-outs on the page go deeper: Shannon's grouping rule as a second route to one point seven five; MacKay's weighing puzzle with twelve balls, where the best first weighing has three outcomes most nearly equally likely; and the names for entropy.

Recap. Entropy is the average surprisal, the sum of share times cost. The village has entropy one point seven five. It is largest, two, when all four words are equally likely, and zero when one word is certain. A script averages the entropy only for its own shares.

## submarine | Step 4: the submarine, one answer, six bits
Step four. A submarine hides in one of the sixty-four squares of an eight by eight grid, all equally likely. You fire at squares one by one. The first shot hits with chance one in sixty-four. What are a hit and a miss worth, and what do many misses add up to?

A hit names the square among sixty-four: six halvings. A miss crosses off one square, a sliver of the options. After thirty-two misses half of the squares are gone, exactly one question's worth. A later hit names the square among the few left, so it is worth less. The total is the same whenever the hit comes.

A check by hand on four squares: the misses are worth zero point four one five, zero point five eight five and one. The sum is two, the log of four.

The formula, equation eight. With s squares left before a shot, a miss has chance s minus one over s, so it is worth the log of s over s minus one. A hit has chance one over s, so it is worth the log of s. Say the hit comes when n squares are left. Multiply the miss ratios from sixty-four squares down to n: each numerator cancels the next denominator, and only sixty-four over n is left. Add the hit's log of n, and the total is the log of sixty-four, which is six, whatever n is.

On the page, a slider chooses which shot hits, and the readout gives the misses before it, the hit, and the total. Hit on shot one: the hit is worth six. Shot two: one miss worth zero point zero two two seven, then a hit worth five point nine seven seven three. Shot thirty-three: thirty-two misses worth exactly one, then a hit worth five. Shot forty-nine: forty-eight misses worth exactly two, then a hit worth four. Shot sixty-four: sixty-three misses worth six, and a last hit worth nothing. The total is always six.

What it means. MacKay says it might seem a little strange that one binary outcome can convey six bits. His verdict, with his I think, is that the submarine example makes quite a convincing case. That is an argument, not a proof.

In the café. The squares are the drinks still possible. Suppose matcha is one order in sixty-four, which is our supposition, and the script begins with matcha. A no on the ticket costs zero point zero two two seven of a question. A yes costs six. Whichever path the customer takes, the total is the cost of that drink.

Check yourself. Five misses in a row from a fresh grid: is the fifth worth more or less than the first? Pause. Slightly more. The misses are worth zero point zero two two seven, zero point zero two three one, zero point zero two three five, zero point zero two three eight and zero point zero two four two, because fewer squares are left each time. MacKay cuts digits off and prints zero point zero two three zero for the second. We round.

The answer to the first guess. Almost nothing. A first miss is worth about zero point zero two two seven questions. A hit on the first shot would be worth six. One whole question's worth takes thirty-two misses.

A fold-out on the page, Wenglish, is MacKay's made-up language where each letter carries a different amount but the five letters of a word always add to fifteen bits.

Recap. A hit is worth six, a first miss about two hundredths, and the total for finding the target is always six. A single answer is worth the log of one over its share.

## roles | Step 5: who encodes and who decodes
Step five. In the café, the customer wants a mocha. On the card she answers flat white? with no, latte? with no, and mocha? with yes. Write a yes as zero and a no as one. The string on her ticket is one, one, zero. Which side encodes, and which decodes?

The encoder holds the original, here the drink, and the agreed script, and turns the original into a string. The decoder holds only the string and the same script, and turns the string back. In the café the customer encodes and the barista decodes. Nobody asks anything live. The card asks, the customer writes, and the ticket travels. Shannon's diagram has the same roles: the receiver ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the signal. The script is the codebook both sides hold before the day starts. MacKay writes that our questioning strategy defines a way of encoding the random variable as a binary file. That can sound as if the asker encodes. The strategy is the shared script. The one who knows the secret, applying it, makes the string.

On the page, a diagram in three steps shows it. The customer knows the drink and holds the card. Answering the card's questions turns mocha into a ticket: no, no, yes. The ticket goes through the hatch, and the barista, with only the ticket and the same card, names the drink.

In the café. The customer encodes. She holds the drink and the script. The ticket is the string. The barista decodes. She holds only the ticket and the same script.

Check yourself. A barista whose card lists the questions in a different order reads the ticket no, no, yes. What can go wrong, and what must both sides share? Pause. She may name the wrong drink, because the same ticket means different things under different cards. Both sides must hold the same script before the day starts. The string alone carries nothing.

A fold-out on the page, Shannon's twin game, shows the same two roles in his guessing experiments with printed English.

Recap. The side that holds the original and the script encodes. The side that holds only the string and the same script decodes. The script, agreed in advance, is what makes the string mean anything.

## nothalves | Step 6: when the shares are not halves
Step six. A guess first. A new village has shares rain zero point seven, sun, wind and snow zero point one each. With the best script of whole yes or no questions, how many questions does one day's word cost on average? One point zero zero, one point three six, one point five zero, or two point zero zero? Pause. The answer follows in this chapter.

The first village is too nice. Halves, quarters and eighths give whole numbers of questions, so the average equals H exactly. Do not take that as a rule. In general the best average of a script of whole questions lies between H and H plus one, equation nine. Here E Q star is the E Q of the best script. Cover and Thomas state it in their chapter on codes, where they show the equivalence of coding and the game of twenty questions: a sequence of questions is a code. We quote the bound and do not prove it.

The zero point seven village, ours, run in code. Set the village widget to weights seven, one, one, one. The entropy is one point three five seven bits. How do we build the best script? A rule, ours and not from our sources, which the notebook does in code: repeatedly join the two rarest outcomes into one group, and every outcome inside the group gets one more question. Two of the zero point one words join into a group of zero point two. That joins the third zero point one word. Only then does the zero point three group join rain. So rain gets one question, and the others two, three and three. Then E Q star is zero point seven times one, plus the three zero point one words times two, three and three, which is one point five. Check against the bound: one point three five seven is at most one point five, which is less than two point three five seven. The gap, zero point one four three, is the price of whole questions.

The answer to the guess. One point five zero. The entropy, one point three six, is the floor, and no script of whole questions can reach it here. Plain labels cost two. One question for rain is too few for the other three words, so they need two, three and three.

In the café. Only whole questions can be asked. A drink that seventy per cent of regulars want still costs one whole question, though only zero point five one five questions' worth of news arrives when it is ordered. The extra is the price of whole questions.

Recap. The best script averages at least H and less than H plus one. The gap is the price of whole questions. Join the two rarest, repeat.

## answer | Short answer, and what it really is
This is the abstract layer. First, a short answer, and it is our reading, not a finding.

How much? One outcome is worth the log, base two, of one over its share, in fair yes or no questions, under a stated model of the source. The average over everything the source can send is the entropy: one point seven five questions a day for the village. A surprise? Improbability under a model. The number belongs to the model, not to the event: two forecasters with different shares give the same snow different numbers. Worth? Questions saved, not importance, truth or meaning. Shannon sets meaning aside for the engineering problem. That is a decision about scope, not a claim that meaning does not matter. Our verdict: the measure is a good price for improbability under a stated model, and a poor price for anything else. What would change it: evidence that the number predicts something beyond improbability. Lens two, coming next, has one such claim, whose evidence we have not checked.

What it really is. Strip away the cafés, villages and submarines. Surprisal rewrites a share in units that add for independent events. Entropy is the average surprisal under the same shares, and depends only on the shares, not on what the outcomes are. It is zero only when one outcome is certain, and at most the log of the number of outcomes, with equality only when all are equally likely. Any change that moves the shares toward equality raises it: the village's one point seven five becomes two when its shares are made equal. A mere swap of shares between outcomes leaves it unchanged. The surprisal approximates the length of the shortest uniquely decipherable script for the outcome. Approximates is the authors' word. Uniquely decipherable means no string is the start of another, so a run of answers can be cut into words in only one way. This is equations two and four without the café.

A fold-out on the page gives Shannon's three properties and his Theorem two. Shannon himself writes that the theorem and its assumptions are in no way necessary for the present theory.

Recap. Surprisal is a re-coding of share into units that add. Entropy is its average. Neither says what a message means.

## lenses | The same idea elsewhere
Five lenses. For each, a link type, what it adds, and what it does not explain.

Lens one, statistical mechanics. The link is same math, in the form of the sum only. Shannon writes that the form of H will be recognized as that of entropy as defined in certain formulations of statistical mechanics. A toy, ours: a box of four cells. All in one cell gives zero. Spread equally gives two, the village's numbers in another story. Pierce says the ideas behind the two entropies are quite different. The lens adds that the sum is about distributions wherever shares exist. It does not explain that the two entropies are one thing.

Lens two, psycholinguistics. A structural analogy: surprisal is built from a share, and what a share does inside a mind is an empirical claim, not a theorem. Gibson and colleagues use the quantity directly: a listener's difficulty in picking a colour chip, given a colour word, is the surprisal of the color, given the word. For minds they write, as one premise in an argument about grammatical gender: since language processing effort is associated with predictability. Read the hedge. They cite two studies we have not seen, and their word is predictability, not surprisal. It adds the one lens whose claim is about behaviour, in our reading, though the post cites only a reported association. It does not explain cause. Associated with is not caused by.

Lens three, communication theory. A structural analogy. The customer is the transmitter, the ticket the signal and the barista the receiver, in Shannon's terms. That mapping is ours. The scope is narrow on purpose: these semantic aspects of communication are irrelevant to the engineering problem. It adds the roles, and an honest boundary. It does not explain meaning, truth or effect. We have not read Weaver's essay.

Lens four, Bayesian probability. A structural analogy: a share can be a degree of belief, so surprisal is relative to a believer. The village's shares come from a long record. A one-off event has none, which is our point. MacKay describes the Bayesian view, in which beliefs can be probabilities, and warns that it is not yet a globally held view. Our inference: different beliefs give different surprisal for the same event. It adds a way to price one-off events. It does not explain whether the beliefs are right.

Lens five, search and decision. Same math: a tree of yes or no questions is a code. In MacKay's tentative conclusion, we might conclude that to find something fast, you choose the experiment whose outcomes are most nearly equally likely. It adds the step from describing a source to choosing what to ask. It does not explain questions whose costs differ, or answers that can be misheard.

For your research, ours. In computation, a language model's next-word share gives a surprisal under that model. In communication, a headline's surprisal depends on whose model prices it. In collaboration, the same sum applies to shares of topics or ties. These are connections, not findings. A fold-out gives more hedges from Shannon, Pierce, and Gibson and colleagues.

Recap. Five lenses: same sum in physics, a claim about minds, the engineering boundary, beliefs as shares, and questions as a code. Each one says what it does not explain.

## fails | Where it fails
Each boundary is an assumption you can find in the concrete layer, with the place where the café breaks.

One, meaning. The formula has only the share in it, so two words with equal share get equal surprisal, understood or not. Shannon sets meaning aside. Gibson and colleagues say the theory as specified so far is entirely agnostic to the form and content of messages. The café breaks: the barista cares which drink it is. The script is blind to taste.

Two, a known, stable distribution. Shannon: these probabilities are known but that is all we know concerning which event will occur. For his model of a source, Pierce says the chances must not change with time if the source is to be ergodic. The café breaks: the cash register's record gets old, and the village script costs two point two five on a uniform day.

Three, independent days. Shannon's symbols are being chosen independently, and additivity needs it. The café breaks: a rainy morning makes hot drinks likelier.

Four, one-off events, and whose model. The formula needs a share, and the village takes it from a record. The café breaks: a single event has no record. On the page, a widget lets two forecasters, Ana and Ben, write two shares for the same snow. Ana says one eighth, Ben one half. Ana is surprised by three, Ben by one. The gap is two. Equal beliefs give equal numbers. The number belongs to the model, not to the snow.

Five, estimation. The village shares are given. In practice they are estimated, and as Gibson and colleagues write, it is difficult to get reliable estimates of these information-theoretic quantities without very large datasets. The bias is our computation from the notebook. Draw n village days, put the observed shares into the entropy formula, repeat two thousand times with a fixed seed. The true entropy is one point seven five. For ten days the mean estimate is one point five zero four. For thirty days, one point six seven five. For a hundred, one point seven two five. For a thousand, one point seven four seven. The estimate is biased low for small samples, partly because a rare word that never appears gets share zero, and partly because noisy observed shares lower the entropy on average. That second reason is ours. The bias shrinks as n grows.

Six, a fixed script, whole questions, no noise. The script is written before the day starts, and both sides hold it. The questions are whole. A ticket arrives intact. The café breaks: a real barista at the counter can ask live, change her next question after a surprising answer, or ask what the customer meant. Our card is fixed in advance. It stops at the first yes, but the whole tree is written down. A transmitter that sends a ticket cannot hear the receiver. That is ours. Noise is outside this post.

Check yourself. Label each statement as a theorem, a definition, an assumption, an empirical claim or a computation. One: the village's entropy is one point seven five bits. Two: the shares must be known. Three: language processing effort is associated with predictability. Four: the surprisal of two independent events adds. Pause. One is a computation. Two is an assumption. Three is an empirical claim by others, hedged, citing studies we have not seen. Four is a theorem: a consequence of the definition and of independence.

Recap. Six limits: meaning, stable shares, independence, one-off events and whose model, estimation, and a fixed script of whole noiseless questions. Each is an assumption of the village, and each breaks the café somewhere.

## imagination | The CSS imagination: whose model sets the price of a surprise?
This is the layer that turns the idea toward society. We use C. Wright Mills, in the two thousand Oxford edition of his nineteen fifty-nine book, The Sociological Imagination.

Mills hedges his advice: there are definite ways, I believe, of stimulating the sociological imagination. The move names below are ours. His word information means facts and news, not Shannon's sense.

Move one: trouble and issue. Mills called the distinction between the personal troubles of milieu and the public issues of social structure perhaps the most fruitful one. His example is hypothetical, not data: one man unemployed in a city of a hundred thousand is his personal trouble, while fifteen million men unemployed in a nation of fifty million employees is an issue. An issue, he says, unlike even widespread trouble, cannot be defined within everyday surroundings. There, he writes, the very structure of opportunities has collapsed. So, in our reading, an issue is not a trouble multiplied.

Our case, ours. One reader cannot tell which of her two hundred messages matters, and blames herself for what she misses: a trouble. A ranking that orders messages by how surprising they are under its own model would price every message for everyone. That it does so is a hypothesis, not a finding. A test, ours, in the spirit of Mills' distinction: if changing the ranking changes what many readers miss, and individual effort does not, the cause lies in an arrangement, not in the readers. Pierce, writing about art and its audiences, in the everyday sense of surprise, says we can be surprised repeatedly only by contrast with that which is familiar. Whose idea of the familiar prices the message? That link is our metaphor.

Move two: extremes and inverted scale. Mills writes that often you get the best insights by considering extremes. A village where it always rains has entropy zero. With all four words equally likely, the entropy is two, the most for four words. Now invert the scale. Mills asks: what would pre-literate villages look like with populations of thirty millions? Give the weather village thirty million listeners. Each listener's surprisal for snow is the same number. But one forecast now prices all of them. If its share for snow is wrong, it is wrong for thirty million people at once, and their surprise is correlated. That is ours. What changes is who writes the forecast, and who pays when it is wrong.

Move three: another discipline's eyes. Take one message, snow tomorrow. A psycholinguist asks whether a listener's processing effort tracks how predictable the word is, an association Gibson and colleagues state. A journalist asks what counts as news: a rumour and a budget can carry the same surprisal, and meaning and consequence are what the number leaves out. Neither asks who owns the model.

A fold-out gives Mills' two-sided view of counting.

Two open research questions. They are ours, invitations, not findings. One, computation and communication: do posts that are more surprising under a language model spread further, after controlling for topic and emotion? Data: posts with share counts and a topic label, plus token probabilities from one fixed language model. Method: turn the probabilities into one number per post, the sum of the words' surprisals or their mean, noting that post length is a confound. Then regress share counts on it with topic fixed effects, and report how the result moves when the model changes. We have not checked the prior work on novelty and spreading. Two, collaboration and communication: how does the entropy of a platform's daily topic mix change around a crisis? Data: posts labelled by topic, for example by a large language model used as a labeller. Method: plug-in entropy, which is the formula applied to the observed shares, with bias correction and bootstrap intervals, before and after a dated event. This is Mills' comparison move, and it means something only if one model prices every case.

Recap. Trouble becomes issue only when the cause lies in an arrangement, here whoever owns the model. Extremes and scale, and other disciplines' eyes, point to the same question: whose model prices a surprise?

## turn | A market stall and a notebook
Your turn. First, a transfer challenge. A market stall sells five items with shares one half, one quarter, one eighth, one sixteenth and one sixteenth. Build the script of questions. Compute the average number of questions and the entropy. Then change the shares to one quarter, one quarter, one quarter, one eighth and one eighth. What does the old script cost now, and what does the best script cost? A hint: halve the customers each time. The two rarest items get four questions each. Pause.

The solution, ours, run in code. The lengths are one, two, three, four, four, and the average equals the entropy, one point eight seven five, because every share is a power of one half. After the change, the old script costs two point five, while the entropy is two point two five and the new best lengths, two, two, two, three, three, cost two point two five. The old script was built for the old shares.

Second, the notebook. It has eight exercises that climb in difficulty, each with a hint and a folded solution. The reference run used Python three point twelve, with numpy and matplotlib. Python three point nine or later should work, but we did not test it. Every number from the reference run is in the results file.

Recap. The stall teaches that a script is right only for its own shares. The notebook lets you move one number at a time.

## recall | Test yourself
Eight questions. Answer aloud, then listen to the answer.

One. Why does the measure use a logarithm? Pause. The chances of independent days multiply, and a log turns a product into a sum, so surprisals add.

Two. What is the surprisal of an outcome whose share is one sixteenth? Pause. Four questions' worth.

Three. What does one point seven five bits mean for the village? Pause. The best script of fair yes or no questions needs one point seven five questions per day on average, in this village.

Four. Why is one point seven five lower than two, and when would the best script average exactly two? Pause. The shares are uneven, so common words get short strings. It averages exactly two, for example, when four words are equally likely. Then H is two, and no script of whole questions can do better.

Five. What does entropy not measure? Pause. Meaning, value, truth or importance. Shannon sets meaning aside for the engineering problem: scope, not denial.

Six. Who encodes and who decodes? Pause. The side with the original and the script encodes: it writes the string. The side with only the string and the same script decodes. In the café the customer writes the ticket and the barista reads it.

Seven. Name two assumptions the village model makes. Pause. Any two of: the shares are known, the shares are stable, the days are independent. A fourth, for real data: enough days to estimate the shares.

Eight. Which statement of Gibson and colleagues is an empirical claim, and what does it say? Pause. That language processing effort is associated with predictability, a premise they support with two studies we have not seen. Not a theorem, and not about surprisal.

Recap. A surprise is worth the log of one over its share. Entropy is the average. It depends on a stated model, and it leaves meaning out. That is the whole post.
