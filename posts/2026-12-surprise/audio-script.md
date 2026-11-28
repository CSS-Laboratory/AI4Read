---
post: 2026-12-surprise
voice: kokoro af_heart
status: written and checked at S4, revised at S5 round 1 and round 2; audio NOT recorded (Kunhao reviews the text first)
note: Written for the ear. Formulas are spoken in words. Widgets are described, not read. Fold-outs and tables are only mentioned. Each chapter ends with a short recap so it can be looped alone. Page numbers are not read aloud. The post stands alone and never refers to another post. Chapter ids match the section ids of the page.
---

## hook | Counting messages, and what the count misses
Welcome to AI4Read from CSS Lab. This is post four: how much is a surprise worth?

Here is the answer in one line, so you can hold it while you listen. A surprise is worth the number of fair yes or no questions it saves you. The rarer the news, the more questions it saves. And the average over all the news a source can send is called its entropy.

Start with the pain, and this is our own point. In a town where it rains most days, the weather office sends one report a day from a fixed list. It rained today, and it snowed in July, are each one pick from that list. So a measure that only counts the possible reports gives them the same number. Yet the first tells you almost nothing, and the second is news.

Counting was how engineers measured messages in the nineteen twenties. In nineteen twenty-eight Hartley measured a message by how many different messages the sender could have picked. In fact he used a logarithm of that number, which step one explains. Pierce says this count is acceptable only if each symbol is equally likely to be selected. Hartley himself saw that E is chosen more often than Z, and that this should govern the lengths of Morse signals, if messages are to be sent most swiftly. What was missing, in our reading, was a number that weighs each message by how likely it is. We build it in a coffee shop, check it in a village, and ask what it leaves out.

Now a guess, before you read on. A submarine hides in one of sixty-four squares, and every square is equally likely. You fire at one square and miss. Count news in yes or no questions: a piece of news is worth the questions it saves you. How many questions is that miss worth? Option one: almost nothing, because one miss rules out only one square of sixty-four. Option two: about one question, because a plain no is still an answer. Option three: exactly nothing, because you still do not know where it is. Option four: about six questions, because a miss is as big as the hit. Pause and choose. The answer comes in step four, the submarine.

Recap. Old measures counted possible messages, and they fit only equally likely choices. A count cannot tell news from non-news. We want one number that weighs each message by how likely it is.

## cafe | The café with a hatch
Picture a loud café. The grinder drowns every word, so customers and barista cannot talk, and the barista works in a back room where she never sees a customer. Orders pass through a hatch on paper tickets. The same card hangs on the wall by the counter and on the wall in the back room: a list of yes or no questions in a fixed order. The customer answers them on the ticket, one after another, and every answer costs one second of the queue's time. The owner knows from the cash register's record that out of every eight regulars, four want a flat white, two a latte, one a mocha and one a matcha. What should the card say?

The old way: split the menu. The menu board is a grid with two drinks on top and two below. The card asks, is your drink on the left side of the board? And then, is it the top one? Every ticket has two answers, and the barista always knows the drink. But half of the regulars want the flat white and spend two answers each, and the one regular in eight who wants matcha spends the same two. The card split the drinks into equal halves, and ignored how many customers stand behind each drink.

The rule that changes: split the customers. The card now says: flat white? Latte? Mocha? And the customer stops at her first yes. A yes to the first question settles four customers out of eight with one answer. A no leaves four. A yes to the second settles two more. A no leaves two. A no to the third leaves only the matcha, so the card needs no fourth question. The flat white costs one answer, the latte two, the mocha and the matcha three each. Over eight customers that is four plus four plus three plus three: fourteen answers. One and three quarters for each customer, against two for the old way. The rare drinks cost more, and that is fair. A matcha order is unusual news. The rarer the order, the bigger the surprise, and the more questions it is worth.

On the page, two small diagrams show the two cards. In the old way every drink costs two questions. In the new way the costs are one, two, three and three.

Three checks. If the card began with matcha, most tickets would start with a no, which rules out only one customer in eight. A question helps most when both answers are likely. If all four drinks sold equally, the clever card would save nothing, and a card built for the old shares would do worse than the plain board.

Who does what. The customer knows the drink and holds the card. Following it, she turns her drink into a row of yes and no on the ticket, for example no, no, yes. The ticket goes through the hatch. The barista never sees the customer. She sees only the ticket, and she holds the same card. She reads the ticket against the card and names the drink. The ticket alone says nothing. No, no, yes means mocha only under this card, so the same card must hang on both walls before the day starts. We call the card the script, and the row of answers on a ticket its string.

The parts of the café, which the next sections use by name: the four drinks; the share of regulars who want each drink; one question on the card; the script, which is the card, the same on both walls; the customer, who fills in the ticket; the ticket, the string of answers; the barista, who sees only the ticket; a ticket's length, how many answers are on it, always a whole number; an order's worth, how much news the order carries, counted in questions, so that a rare order is worth more than a common one; for the four drinks above, worth and ticket length agree, and the next section shows when they do not; the day's average; and the menu-board card, the old way.

Check yourself. First: which customers get the longest tickets, and why? Pause. The mocha and matcha customers, three answers each. The card spends its questions where the customers are. Second: a day comes when all four drinks sell equally. Would the clever card still be best? Pause. No. The average would be one plus two plus three plus three, divided by four: two and a quarter. The plain board costs exactly two.

Recap. Split the customers, not the menu. Common drinks get short tickets, rare drinks long ones, and the average falls from two to one and three quarters. The customer, holding the drink and the card, writes the ticket. The barista, holding only the ticket and the same card, names the drink.

## village | The weather village, equal chances first
Now leave the café for the field's own setting. A village radio sends one word a day: rain, sun, wind or snow. The shares of days are one half, one quarter, one eighth and one eighth, the owner's numbers with drinks swapped for weather words. Shannon, and Cover and Thomas, use these shares. We call each day's word a symbol. Shannon has successive symbols chosen independently, and so do we, though real weather is not like that. Each equation is followed by a line that starts, in the café, and names the café parts it stands for.

Three words need fixing. Worth means the number of fair yes or no questions an outcome saves you, not usefulness. A question is fair when its two answers are equally likely. Surprise means how unlikely an outcome was under a stated model of the source, a list of how likely each message is. It does not mean a feeling. Information is used in Shannon's engineering sense: one choice from a set of possible messages. Pierce says the confusion about how communication theory relates to physics is sometimes aggravated when more than one meaning of information creeps into a discussion.

Step one: equal chances, count the halvings. A guess first. One of thirty-two cups of water is poisoned. A rat that drinks any poisoned cup dies within the hour, and you have one hour. All the rats drink at the same time, each from any cups you choose. What is the smallest number of rats that is always enough? Four, five, six or eight? Pause. The answer is at the end of this chapter.

The cups and rats are our framing. MacKay has one of sixty-four integers, and says six questions suffice.

With thirty-two cups, one good question halves them: thirty-two, sixteen, eight, four, two, one. That is five halvings. The rats ask all five questions at once, because each rat's fate, dead or alive, is one yes or no answer. Thirty-two is two multiplied by itself five times, and sixty-four is six times. One answer of a fair yes or no question is one bit, a word Shannon credits to J. W. Tukey. Here it is a unit of worth. From now on, questions and bits name the same unit.

The formula, equation one. For N equally likely options, where N is a power of two, the number of questions k satisfies: N equals two to the power k. So k is the log, base two, of N. In words: the number of questions is the number of times you must halve N to reach one. The log, base two, asks: two multiplied by itself how many times gives this number? For other N, think of the worst case, the most questions you could ever need. That is ours. MacKay's raw bit content is a lower bound for the number of binary questions that are always guaranteed to identify an outcome.

The check. The log, base two, of thirty-two is five, and of sixty-four, six. Cover and Thomas open with the same case, five bits. What it does not say: four rats cannot decide thirty-two cups, because two to the fourth is sixteen, and sixteen is less than thirty-two. That is ours.

In the café. N is the number of drinks on the menu when all sell equally, each with the same share. k is the number of questions on a ticket. The two in two to the k is the two answers to one question. Halving the board is the menu-board card, the old way. The rats are a ticket filled in all at once: five rats, five answers. That is ours.

The answer to the guess. Five rats. Each rat gives one yes or no answer, so five rats give five answers at once, enough to tell thirty-two cups apart. Four rats give only sixteen outcomes.

A fold-out on the page, Nyquist and Hartley in symbols, goes deeper. It gives Nyquist's result of nineteen twenty-four for the speed of a telegraph line, and Pierce's conditions for Hartley's count: successive symbols chosen independently, each equally likely. It also records that Pierce's eight values give four times the speed, an apparent slip: by Nyquist's rule it is three times, our computation.

Recap. With equal chances, the number of questions is the number of halvings, the log, base two, of the number of options. One answer is one bit. Thirty-two cups need five rats.

## surprisal | Step 2: unequal chances, surprisal
Step two. The village again: rain one half, sun one quarter, wind one eighth, snow one eighth. The best questions go like the card: rain? Then sun? Then wind? And then only snow is left. The ticket lengths are one, two, three and three answers. Write yes as zero and no as one, and the strings are zero, one-zero, one-one-zero and one-one-one.

How much news does one outcome carry, in questions? A share of one half means halving the crowd once, one quarter twice, one eighth three times. The worth of an outcome is how many times you must halve the whole crowd to be left with a group the size of its share. For these shares, worth and ticket length are the same number.

The formula, equation two. For an outcome x whose share is P of x, the worth, h of x, is the log, base two, of one over P of x. In words: the surprisal of x is the log, base two, of one over the share of x. MacKay calls it the Shannon information content. Gibson and colleagues say surprisal, and information content. We use the word surprisal for the worth.

The check. For snow, the share is one eighth, and the log, base two, of eight is three. The four words give one, two, three, three, as the tickets did. On the page, a slider moves the chance of an event. Share zero point zero zero one is worth ten questions, zero point one gives three point three, and zero point five gives one. Those are MacKay's numbers. At share one, the worth is zero: a sure thing tells you nothing. A share of zero point one is worth three point three questions, but no ticket has three point three answers: a ticket's length is whole, and a worth need not be.

A second concept: independent days add. Rain today, snow tomorrow. The pair has share one half times one eighth, one sixteenth, and the log, base two, of sixteen is four. The separate worths are one and three, and one plus three is four. In general, for independent x and y, the chance of the pair is the product, and a log turns a product into a sum, because two to the a times two to the b is two to the a plus b: multiplying the crowds adds the halvings. That is equation three: the surprisal of the pair is the surprisal of x plus the surprisal of y. MacKay says we might want a measure of the amount of information gained to have the property of additivity. It needs independence, which the village assumes.

What it does not say. Only shares that are powers of one half, one half, one quarter, one eighth, one sixteenth and so on, are worth a whole number of questions. That is ours. A share of zero point three is worth one point seven four. So Gibson and colleagues say the information content approximates the length of the shortest uniquely decipherable script: one whose rows of answers can be cut back into words in only one way. Step six returns to this.

In the café. x is a drink, here a weather word. P of x is its share. h of x is the order's worth, in questions. A ticket's length is whole, so it can equal the worth only for shares one half, one quarter, one eighth and so on. That is ours. The log of one over the share counts how often you must halve the crowd. Additivity is two customers in a row, their tickets joined.

Recap. The surprisal of an outcome is the log, base two, of one over its share. Rain is worth one, sun two, wind and snow three. Surprisals of independent events add.

## entropy | Step 3: the average, entropy
Step three. Take eight days that match the shares: four rain, two sun, one wind, one snow. Rain costs one question each, sun two, wind three, snow three. The total is four plus four plus three plus three, fourteen questions in eight days: one point seven five per day. What one number describes the source? Weigh each word's worth by how often it comes, and add.

The formula, equation four. The entropy H of a source is the sum, over all words, of the share of the word times its worth. That is the average surprisal. The sigma sign means add up. An outcome with share zero contributes zero, by a convention in MacKay's book. For the village: one half times one, plus one quarter times two, plus one eighth times three, plus one eighth times three, equals one point seven five.  Cover and Thomas get one point seven five for the same tree. Before and after the crucial change: two-question labels cost two questions a day, and the script built for the shares costs one point seven five.

On the page, a widget sets four weights, for rain, sun, wind and snow. The bars show each word's part of the average, its share times its surprisal, and they add up to the entropy. Try all equal: the entropy is two, the most possible for four words. Try only rain: the entropy is zero, and Shannon writes that no channel is required. Try reversed: the entropy is still one point seven five, because it depends only on the shares. 

A script has its own average, equation five. A script that spends L of x questions on word x averages the sum of the share times L of x. We write it E Q, short for the expected number of questions. The village script on the village: one point seven five, which equals H. On only rain it averages one, and on the equal-shares day of section two's check it cost two point two five. The village script averages H only for its own shares, and it can cost more on others.

What it means. We measured the average number of fair questions per word, for a source whose shares we assume are known. For the best script of whole questions, the average equals H exactly when every share is a power of one half. Step six gives the general case. It does not say what a word means, or how good the script is on other shares.

In the café. The sigma means go through the drinks, each weighted by its share. P of x is how often that drink is ordered. The log of one over P of x is the worth of that order. H is the day's average worth. Where the shares are halves it is also the day's average ticket length under the best script. Step six shows the general case. E Q is the day's average ticket length for whatever script hangs on the wall.

Check yourself. Predict first, then press reversed in the widget: rain and sun are now an eighth of the days each, wind a quarter, snow a half. What does the village script cost a day now, and what is H? Why is the script not at H? Pause. The script costs two point six two five a day, while H stays one point seven five. The script puts its short tickets on rain and sun, which are now rare, and its long tickets on snow, which is now half the days. It was built for the village shares.

Three fold-outs on the page go deeper: Shannon's grouping rule as a second route to one point seven five; MacKay's weighing puzzle with twelve balls, where the best first weighing has three outcomes most nearly equally likely; and the names for entropy.

Recap. Entropy is the average surprisal, the sum of share times worth. The village has entropy one point seven five. It is largest, two, when all four words are equally likely, and zero when one word is certain. A script averages the entropy only for its own shares.

## submarine | Step 4: the submarine, one answer, six bits
Step four. A submarine hides in one of the sixty-four squares of an eight by eight grid, all equally likely. You fire at squares one by one. The first shot hits with chance one in sixty-four. What are a hit and a miss worth, and what do many misses add up to?

A hit names the square among sixty-four: six halvings. A miss crosses off one square, a sliver of the options. After thirty-two misses half of the squares are gone, exactly one question's worth. A later hit names the square among the few left, so it is worth less. The total is the same whenever the hit comes.

A check by hand on four squares: the misses are worth zero point four one five, zero point five eight five and one. The sum is two, the log of four.

The formula, equation eight. With s squares left before a shot, a miss has chance s minus one over s, so it is worth the log of s over s minus one. A hit has chance one over s, so it is worth the log of s. Say the hit comes when n squares are left. Multiply the miss ratios from sixty-four squares down to n: each numerator cancels the next denominator, and only sixty-four over n is left. Add the hit's log of n, and the total is the log of sixty-four, which is six, whatever n is.

On the page, a slider chooses which shot hits, and the readout gives the misses before it, the hit, and the total. Hit on shot one: the hit is worth six. Shot two: one miss worth zero point zero two two seven, then a hit worth five point nine seven seven three. Shot thirty-three: thirty-two misses worth exactly one, then a hit worth five. Shot forty-nine: forty-eight misses worth exactly two, then a hit worth four. Shot sixty-four: sixty-three misses worth six, and a last hit worth nothing. The total is always six.

What it means. MacKay says it might seem a little strange that one binary outcome can convey six bits. His verdict, with his I think, is that the submarine example makes quite a convincing case. That is an argument, not a proof.

In the café. The squares are the drinks still possible. Suppose matcha is one order in sixty-four, which is our supposition, and the script begins with matcha. A no on the ticket is worth zero point zero two two seven of a question. A yes is worth six. For any one customer, the worths of her answers add up to the worth of her drink, whatever order the card asks in. That is ours: the same chain of fractions as equation eight.

Check yourself. Five misses in a row from a fresh grid: is the fifth worth more or less than the first? Pause. Slightly more. The misses are worth zero point zero two two seven, zero point zero two three one, zero point zero two three five, zero point zero two three eight and zero point zero two four two, because fewer squares are left each time. MacKay prints zero point zero two three zero for the second, which matches cutting the digits off, in our reading. We round.

The answer to the first guess. Almost nothing. A first miss is worth about zero point zero two two seven questions. A hit on the first shot would be worth six. One whole question's worth takes thirty-two misses.

A fold-out on the page, Wenglish, is MacKay's made-up language where each letter carries a different amount but the five letters of a word always add to fifteen bits.

Recap. A hit on the first shot is worth six, a first miss about two hundredths, and the total for finding the target is always six. A single answer is worth the log of one over its share.

## roles | Step 5: who encodes and who decodes
Step five. In the café, the customer wants a mocha. On the card she answers flat white? with no, latte? with no, and mocha? with yes. Write a yes as zero and a no as one. The string on her ticket is one, one, zero. Which side encodes, and which decodes?

The encoder holds the original, here the drink, and the agreed script, and turns the original into a string. The decoder holds only the string and the same script, and turns the string back. In the café the customer encodes and the barista decodes. Nobody asks anything live. The card asks, the customer writes, and the ticket travels. Shannon's diagram has the same roles, in our mapping, a structural analogy. The customer is the transmitter, the ticket the signal, and the barista the receiver, which, in Shannon's words, ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the signal. MacKay writes that our questioning strategy defines a way of encoding the random variable as a binary file. That can sound as if the asker encodes. The strategy is the shared script. The one who knows the secret, applying it, makes the string.

On the page, a diagram in three steps shows it. The customer knows the drink and holds the card. Answering the card's questions turns mocha into a ticket: no, no, yes. The ticket goes through the hatch, and the barista, with only the ticket and the same card, names the drink.

In the café. The customer encodes. She holds the drink and the script. The ticket is the string. The barista decodes. She holds only the ticket and the same script.

Check yourself. A barista whose card lists the questions in a different order reads the ticket no, no, yes. What can go wrong, and what must both sides share? Pause. She may name the wrong drink, because the same ticket means different things under different cards. Both sides must hold the same script before the day starts. The string alone carries nothing.

A fold-out on the page, Shannon's twin game, shows the same two roles in his guessing experiments with printed English.

Recap. The side that holds the original and the script encodes. The side that holds only the string and the same script decodes. The script, agreed in advance, is what makes the string mean anything.

## nothalves | Step 6: when the shares are not halves
Step six. A guess first. A new village has shares rain zero point seven, sun, wind and snow zero point one each. With the best script of whole yes or no questions, how many questions does one day's word cost on average? One point zero zero, one point three six, one point five zero, or two point zero zero? Pause. The answer follows in this chapter.

So far the best card came easily, because every share was a power of one half. Now build one. On the page, a widget lets you tap two groups to put them under one question. Every word in the two groups gets one more question on its ticket. When one group is left, the card is done. A table gives each word's share, its ticket, which is whole questions, and its worth, which can be a fraction. A button joins the two rarest groups for you.

What happens. The village day: press the button three times. Wind and snow join into a quarter. That joins sun. That joins rain. Tickets one, two, three, three, average one point seven five, which is H. Start again and always join the first two groups: the average rises to two point six two five. The zero point seven day, ours, run in code, with H one point three five seven. Two zero point one words join into zero point two. That joins the third zero point one word, into zero point three. Then zero point three joins rain. Tickets one, two, three, three. Which zero point one word gets two is a tie, and any choice costs the same. The average is zero point seven times one, plus the three zero point one words times two, three and three, which is one point five zero zero. Rain is worth zero point five one five questions, but its ticket cannot be shorter than one. The gap, zero point one four three, is the price of whole questions. The equal day: tickets two, two, two, two, average two point zero zero zero, which is H.

The rule is Huffman's. Join the two rarest outcomes, adding their shares, give everything in the group one more question, and repeat until one group is left. Cover and Thomas give this simple algorithm. They prove that it gives the shortest average length among scripts in which no string is the start of another, as on our card: Huffman coding is optimal. They also say the best series of questions is the one the Huffman code gives. MacKay states the same rule as his Algorithm five point four. Only the worked zero point seven day is ours. We do not reproduce the proof. Notebook exercise seven runs the rule in code.

Where it holds. It needs shares that are known and fixed, and one word at a time. Best means the shortest average. One word can get a ticket longer than its worth, as rain did. The best card is not unique: swapping yes and no on a question gives another. The rule builds from the rarest up. Splitting the words into two nearly equal groups, again and again, is not always best. In MacKay's seven-outcome example five point eighteen, it gives two point five three, against one point nine seven for the best card.

The formula, equation nine. Call the average of the best card E Q star. With the entropy H, Cover and Thomas give: H is at most E Q star, which is less than H plus one. E Q star equals H exactly when every share is a power of one half. Cover and Thomas show the equivalence of coding and the game of twenty questions: a sequence of questions is a code. We quote the bound without proof. The check, on the three days: one point seven five equals H. One point three five seven is at most one point five zero zero, which is less than two point three five seven. Two point zero zero zero equals H.

The answer to the guess. One point five zero. The entropy, one point three six, is the floor, and no card of whole questions can reach it here. Plain labels cost two.

In the café. Only whole questions can be asked. A drink that seventy per cent of regulars want still gets one whole question, though only zero point five one five questions' worth of news arrives with it: its ticket is longer than its worth. E Q star is the day's average under the best card the owner could write. H is the day's average worth.

Recap. The best card averages at least H and less than H plus one. The gap is the price of whole questions. The rule is Huffman's: join the two rarest, repeat. Splitting evenly from the top is not always best.

## answer | Short answer, and what it really is
This is the abstract layer. First, a short answer, and it is our reading, not a finding.

How much? One outcome is worth the log, base two, of one over its share, in fair yes or no questions, under a stated model of the source. The average over everything the source can send is the entropy: one point seven five questions a day for the village. A surprise? Improbability under a model. The number belongs to the model, not to the event: two forecasters with different shares give the same snow different numbers. Worth? Questions saved, not importance, truth or meaning. Shannon sets meaning aside for the engineering problem. That is scope, not a claim that meaning does not matter. Our verdict: the measure is a good price for improbability under a stated model, and a poor price for anything else. What would change it: evidence that the number predicts something beyond improbability. Lens two, coming next, has one such claim, hedged. We have not checked its evidence.

What it really is. Strip away the cafés, villages and submarines. Surprisal rewrites a share in units that add for independent events. Entropy is the average surprisal under the same shares, and depends only on the shares, not on what the outcomes are. It is zero only when one outcome is certain, and at most the log of the number of outcomes, with equality only when all are equally likely. Any change that moves the shares toward equality raises it: the village's one point seven five becomes two when its shares are made equal. The surprisal approximates the length of the shortest uniquely decipherable script for the outcome. Approximates is the authors' word. Uniquely decipherable means a run of answers can be cut into words in only one way. Scripts in which no string is the start of another, like our card, are one kind of these. This is equations two and four without the café.

A fold-out on the page gives Shannon's three properties and his Theorem two. Shannon himself writes that the theorem and its assumptions are in no way necessary for the present theory.

Recap. Surprisal is a re-coding of share into units that add. Entropy is its average. Neither says what a message means.

## lenses | The same idea elsewhere
Four lenses. For each, a link type, what it adds, and what it does not explain.

Lens one, statistical mechanics. The link is same math, in the form of the sum only. Shannon writes that the form of H will be recognized as that of entropy as defined in certain formulations of statistical mechanics. Pierce says the ideas behind the two entropies are quite different. The lens adds that the sum is about distributions wherever shares exist. It does not explain that the two entropies are one thing.

Lens two, psycholinguistics. A structural analogy: surprisal is built from a share, and what a share does inside a mind is an empirical claim, not a theorem. Gibson and colleagues use the quantity directly: a listener's difficulty in picking a colour chip, given a colour word, is the surprisal of the color, given the word. For minds they write, as one premise in an argument about grammatical gender: since language processing effort is associated with predictability. Read the hedge. They cite two studies we have not seen, and their word is predictability, not surprisal. It adds the one lens whose claim is about behaviour, in our reading, though the post cites only a reported association. It does not explain cause. Associated with is not caused by.

Lens three, Bayesian probability. A structural analogy: a share can be a degree of belief, so surprisal is relative to a believer. The village's shares come from a long record. A one-off event has none, which is our point. MacKay describes the Bayesian view, in which beliefs can be probabilities, even for a single proposition, and notes that it is not yet a globally held view. Our inference: different beliefs give different surprisal for the same event. It adds a way to price one-off events. It does not explain whether the beliefs are right.

Lens four, search and decision. Same math: a tree of yes or no questions is a code. For one experiment, MacKay's tentative conclusion, we might conclude, is that it is most informative when its outcomes are equally likely. A whole search differs. Splitting every group as evenly as possible is not always the fastest script, and step six's rule is. It adds the step from describing a source to choosing what to ask. It does not explain a whole search built by even splits, questions whose costs differ, or answers that can be misheard.

Compared, in our reading. Lens two is a claim to test. Lens three says a share belongs to a believer. Lens four takes the shares as fixed and the average as the thing to minimise.

For your research, ours. In computation, a language model's next-word share gives a surprisal under that model. In communication, a headline's surprisal depends on whose model prices it. In collaboration, the same sum applies to shares of topics or ties. Connections, not findings. A fold-out gives more hedges from Shannon, Pierce, and Gibson and colleagues.

Recap. Four lenses: same sum in physics, a claim about minds, beliefs as shares, and questions as a code. Each one says what it does not explain.

## fails | Where it fails
Each boundary is an assumption you can find in the concrete layer, with the place where the café breaks.

One, meaning. The formula has only the share in it, so two words with equal share get equal surprisal, understood or not. Shannon sets meaning aside. The café breaks: the barista cares which drink it is. The script is blind to taste.

Two, a known, stable distribution. Shannon: these probabilities are known but that is all we know concerning which event will occur. Pierce says the chances must not change with time if the source is to be ergodic. Ergodic, in our gloss, means its long-run averages do not depend on which run you watch. The café breaks: the cash register's record gets old, and the village script costs two point two five on a uniform day.

Three, independent days. Shannon's symbols are being chosen independently, and additivity needs it. The café breaks: a rainy morning makes hot drinks likelier.

Four, one-off events, and whose model. The formula needs a share, and the village takes it from a record. The café breaks: a single event has no record. On the page, a widget lets two forecasters, Ana and Ben, write two shares for the same snow. Ana says one eighth, Ben one half. Ana is surprised by three, Ben by one. The gap is two. Equal beliefs give equal numbers. The number belongs to the model, not to the snow.

Five, estimation. The village shares are given. In practice they are estimated, and as Gibson and colleagues write, it is difficult to get reliable estimates of these information-theoretic quantities without very large datasets. The bias is our computation from the notebook. Draw n village days, put the observed shares into the entropy formula, and repeat two thousand times. The true entropy is one point seven five. For ten days the mean estimate is one point five zero four. For thirty days, one point six seven five. For a hundred, one point seven two five. For a thousand, one point seven four seven. The estimate is biased low for small samples, because noisy observed shares lower the entropy on average. That is ours. The extreme case is a rare word that never appears and gets share zero. The bias shrinks as n grows.

Six, a fixed script and whole questions. The script is written before the day starts, and both sides hold it. The shares are known. Only whole questions. The café breaks: a real barista can update the shares as the day goes on, ask a question that is on no card, or ask what the customer meant. With the shares known, choosing the next question from the last answer is already what a written card does.

Seven, no noise. A ticket arrives intact. The café breaks: a smudged ticket, or a transmitter that sends a ticket and cannot hear the receiver. That is ours. Noise is outside this post.

Check yourself. Label each statement as a theorem, a definition, an assumption, an empirical claim or a computation. One: the village's entropy is one point seven five bits. Two: the shares must be known. Three: language processing effort is associated with predictability. Four: the surprisal of two independent events adds. Pause. One is a computation. Two is an assumption. Three is an empirical claim by others, hedged, citing studies we have not seen. Four is a theorem: a consequence of the definition and of independence.

Recap. Seven limits: meaning, stable shares, independence, one-off events and whose model, estimation, a fixed script of whole questions, and no noise. Each is an assumption of the village, and each breaks the café somewhere.

## imagination | The CSS imagination: whose model sets the price of a surprise?
This is the layer that turns the idea toward society. We use C. Wright Mills, in the two thousand Oxford edition of his nineteen fifty-nine book, The Sociological Imagination.

Mills argued that people need a quality of mind that shows how a life and its time fit together. His advice is not findings, and he hedges it: there are definite ways, I believe, of stimulating the sociological imagination. The names of the moves are ours. His word information means, in our reading, facts. He calls his time this Age of Fact. It is not Shannon's sense.

Move one: extremes and inverted scale. Mills writes that often you get the best insights by considering extremes. A village where it always rains has entropy zero. Four equal words give entropy two. Now invert the scale. Mills asks: what would pre-literate villages look like with populations of thirty millions? Give the weather village thirty million listeners. Each listener's surprisal for snow is the same number, but one forecast now prices all of them. If its share for snow is wrong, it is wrong for thirty million people at once. That is ours. What changes is who writes the forecast, and who pays when it is wrong.

Move two: trouble and issue. Mills called the distinction between the personal troubles of milieu and the public issues of social structure perhaps the most fruitful one. His example is hypothetical, not data: one man unemployed in a city of a hundred thousand is his personal trouble, while fifteen million men unemployed in a nation of fifty million employees is an issue. An issue, he says, unlike even widespread trouble, cannot very well be defined within everyday surroundings. In his unemployment example, he writes, the very structure of opportunities has collapsed. So, in our reading, an issue is not a trouble multiplied.

Our case, ours. One reader misses an important message among her two hundred, and blames herself: a trouble. A ranking that orders messages by how surprising they are under its own model would price every message for everyone, which is equation two with a single model. That it does so is a hypothesis, not a finding. A test, ours: if changing the ranking changes what many readers miss, and individual effort does not, the cause lies in an arrangement, not in the readers.

Move three: another discipline's eyes. Mills suggests asking how a political scientist, a psychologist or a historian would see a problem. Take snow tomorrow. A psycholinguist asks whether language processing effort is associated with how predictable an element is in context, a link Gibson and colleagues state. A journalist asks what counts as news: a rumour and a budget can carry the same surprisal; meaning and consequence are what the number leaves out. Neither asks who owns the model.

A fold-out gives Mills' two-sided view of counting.

Two open research questions. They are ours, invitations, not findings. One, computation and communication: do posts that are more surprising under a language model spread further, after controlling for topic and emotion? Data: posts with share counts and a topic label, plus token probabilities from one fixed language model. Method: one number per post, the sum or the mean of the words' surprisals, noting that length is a confound. Then regress share counts on it with topic fixed effects, repeated with another model. We have not checked the prior work. Two, collaboration and communication: how does the entropy of a platform's daily topic mix change around a crisis? Data: posts labelled by topic, for example by a large language model used as a labeller. Method: plug-in entropy, which is the formula applied to the observed shares, with bias correction and bootstrap intervals, before and after a dated event. This is Mills' comparison move, his search for comparable cases, and it means something only if one model prices every case.

Recap. In Mills' terms, trouble and issue differ by where the cause lies. Our hypothesis, not a finding: for a ranking that prices messages under its own model, part of the cause may lie in whose model prices them. Extremes and scale, and other disciplines' eyes, point to the same question: whose model prices a surprise?

## turn | A market stall and a notebook
Your turn. First, a transfer challenge. A market stall sells five items with shares one half, one quarter, one eighth, one sixteenth and one sixteenth. Build the script of questions. Compute the average number of questions and the entropy. Then change the shares to one quarter, one quarter, one quarter, one eighth and one eighth. What does the old script cost now, and what does the best script cost? A hint: join the two rarest items each time, as in step six. The two rarest items get four questions each. Pause.

The solution, ours, run in code. The lengths are one, two, three, four, four, and the average equals the entropy, one point eight seven five, because every share is a power of one half. After the change, the old script costs two point five, while the entropy is two point two five and the new best lengths, from step six's rule, two, two, two, three, three, cost two point two five. The old script was built for the old shares.

Second, the notebook. It has eight exercises that climb in difficulty, each with a hint and a folded solution. The reference run used Python three point twelve, with numpy and matplotlib. Python three point nine or later should work, but we did not test it. Every number from the reference run is in the results file.

Recap. The stall teaches that a script is right only for its own shares. The notebook lets you move one number at a time.

## recall | Test yourself
Eight questions. Answer aloud, then listen to the answer.

One. Why does the measure use a logarithm? Pause. The chances of independent days multiply, and a log turns a product into a sum, so surprisals add.

Two. What is the surprisal of an outcome whose share is one sixteenth? Pause. Four questions' worth.

Three. What does one point seven five bits mean for the village? Pause. The best script of fair yes or no questions needs one point seven five questions per day on average, in this village.

Four. Why is one point seven five lower than two, and when would the best script average exactly two? Pause. The shares are uneven, so common words get short strings. With four equally likely words, H is two.

Five. What does entropy not measure? Pause. Meaning, value, truth or importance. Shannon sets meaning aside for the engineering problem: scope, not denial.

Six. Who encodes and who decodes? Pause. The side with the original and the script encodes: it writes the string. The side with only the string and the same script decodes. In the café: customer, then barista.

Seven. Two forecasters see the same snow. Why do they get different numbers, and which assumption of the village breaks? Pause. A surprisal is built from a share, and a share belongs to a model. The village assumes known, stable shares. A one-off event has no record, so each forecaster writes her own.

Eight. How do you build the best card for any shares, and what does it cost? Pause. Join the two rarest outcomes, give everything in the group one more question, and repeat. This is Huffman's rule. The best average is at least H and below H plus one. For shares zero point seven, and three times zero point one, it is one point five zero zero, with H one point three five seven.

Recap. A surprise is worth the log of one over its share. Entropy is the average. It depends on a stated model, and it leaves meaning out. That is the whole post.
