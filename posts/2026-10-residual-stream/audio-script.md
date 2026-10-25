---
post: 2026-10-residual-stream
voice: kokoro af_heart
note: Written for the ear. Formulas are spoken in words. Widgets are described, not read. Fold-outs and tables are only mentioned. Each chapter ends with a short recap so it can be looped alone. The post stands alone and never refers to another post.
---

## hook | The list in the middle
Welcome to AI4Read from CSS Lab. This is post three: what is a hidden state?

Stop a language model halfway through its work and copy out the list of numbers it holds for one word. Libraries call this list a hidden state. The list is long. GPT-2 small has seven hundred and sixty-eight numbers in it. Qwen3 one point seven billion base, a newer model, has two thousand and forty-eight. A list of numbers is called a vector, and the number of entries in it is its dimension.

People do three things with such lists. That is our summary of common practice. Say you copy the list at one layer. You can then train a small classifier on it, to see whether a property of the text can be read off. You can compare it with the list from another model. Or you can add a vector to it, to push the model somewhere. All three treat the list as a definite object. So what is it?

Three questions drive this post. What is the list? What can a part of the model read from it, and write into it? And what happens to a probe's score if every list is pushed by the same vector? Each answer is arithmetic you can do on paper. At the end we ask whether a concept such as calm is a direction in the list, and treat that as a bet, not a fact.

We check the first question on a real model in the two notebooks that come with this post. The vocabulary and the bets come from three published sources, which section four introduces.

Recap. A hidden state is a long list of numbers. People probe it, compare it and push it. The post asks what the list is, and answers with a running sum that we can check.

## guess | Three predictions
Three predictions. Commit to an answer before you read on. A wrong guess you remember is worth more than a right answer you only read. The answers come in the sections named on the page.

Question one. A model is a stack of rounds of work called blocks. You stop it after block six and copy the list it holds for one word. What is that list?
Pause.
Option one: the model's best guess so far, stored as a list of numbers. Option two: the word's starting list plus every addition made so far. Option three: only the newest block's output, with nothing kept from before. Option four: a summary of the whole sentence, shared by all of its words.

Question two. A shared list already holds two, two. Block three now writes minus two, minus two into it. What can a later block read from the list?
Pause.
Option one: both vectors, kept as two separate items in order of arrival. Option two: only minus two, minus two, because the newest write replaces the older one. Option three: only the sum, zero, zero: neither vector can be read back alone. Option four: only two, two, because the first write is kept and the second ignored.

Question three. A probe gives each point in a cloud a score: multiply its two coordinates by two fixed numbers and add the results. Now add the same vector to every point of the cloud. By how much does each score change?
Pause.
Option one: by the same amount, whichever point it is. Option two: by more for points far from the origin. Option three: only for points that lie near the probe's line. Option four: by an amount that depends on each point's length.

Recap. Three questions: what the list is after block six, what a later block can read after two writes cancel, and how a score moves when every point is pushed by the same vector. Keep your three guesses.

## sum | The stream is a running sum
Start from words. A language model reads text as tokens: whole words or pieces of words. Its first step is a lookup. A table holds one list of numbers for each token, and the model copies out the list for the token it is reading. GPT-2 adds to it a learned list for the token's position. We call the starting list, position list included, the embedding and write it x zero. We keep the word embedding for this one list, because the sources use it in four ways.

From that start, the model keeps one working list for the token, and every attention and MLP part of the model changes it by adding to it. We call it the residual stream, or the stream. GPT-2 small has seven hundred and sixty-eight numbers in it and twelve blocks. Our toy uses two numbers, so that every list can be drawn on paper.

Now add two vectors by hand, before any diagram. A part of the model adds the vector two, minus one to a stream that holds one, two. Add the first numbers: one plus two is three. Add the second numbers: two plus minus one is one. The answer is three, one. As a rule: the vector a, b plus the vector c, d is a plus c, b plus d. First plus first, second plus second. The same rule holds for seven hundred and sixty-eight numbers.

A model has a stack of blocks. Each block has two parts in a fixed order: first attention, then an MLP, short for multi-layer perceptron, a small network. We say block for the pair and sub-layer for each part, because the word layer is confusing. Each sub-layer looks at the stream, computes a vector, and adds it to the stream. It never overwrites it. We call the vector a sub-layer adds its write. Call a k the write of attention in block k, and f k the write of the MLP.

Now the toy. The embedding is one, two. Block one writes two, minus one and then minus one, one. Block two writes three, minus two and then minus one, two. In the stepper, tap Next to add each row. The stream goes one, two; then three, one; then two, two; then five, zero; and ends at four, two. In the bus diagram, the same five writers add into one shared stream, and the diagram shows the running total after each. The second number of the last write, plus two, undoes the minus two that attention two wrote. Writes add, so they can cancel.

The pattern: the stream after k blocks is the embedding plus every write up to block k. Elhage and colleagues put it this way: the residual stream is simply the sum of the output of all the previous layers and the original embedding. One everyday picture, as a picture only, and ours: a bank balance is the opening balance plus every deposit and withdrawal since, and a later withdrawal can cancel an earlier deposit. The rest of the post tests how far the picture holds.

The sum is bookkeeping. It tells you what is in the stream, not what any writer meant. It is exact in the account Elhage and colleagues give, which says: we also ignore layer normalization. Real models add a norm, short for normalisation: a rescaling step applied to the stream before each read. It subtracts the average of the list's numbers, divides by their typical distance from that average, the standard deviation, and then applies a learned scale and shift. Before that last step, a list and its double give the same result. The list four, two has average three, so it is centred as one, minus one; its standard deviation is one; the result is one, minus one. The list eight, four has average six, centred two, minus two, standard deviation two, so the result is again one, minus one. GPT-2 uses this version. Two fold-outs give more: a code reading at the end of this section and a norm table in section six.

One stream per position. Take the two-word input red car. The model keeps one stream for each word, at every depth. Only attention carries information between positions, and in a decoder-only model, which predicts text from left to right, only from earlier ones. So there is no single hidden state of a sentence. A summary of a sentence is a further step that someone must choose. That is ours.

Is the hidden state the stream? The Hugging Face transformers library, a Python library that loads language models, returns the list after each block under the name hidden states. None of the three sources uses the phrase hidden state, so we test the identity. Copy the list after k blocks. Separately, record every write inside the blocks and add them to the starting list. If the sum equals the copied list up to rounding, they are the same vector.

We ran this on GPT-2 small, with twelve blocks, on the sentence the cat sat on the mat because, in thirty-two-bit numbers, called float32, which keep about seven digits. Subtracting neighbouring entries of the library's list should give each block's two writes. Over the first eleven blocks they differed by at most six point two times ten to the minus six, relative to the size of the block's own two writes at that position. Measured against the stream instead, the same differences are about four times ten to the minus eight up to seven times ten to the minus seven. That is rounding. In the toy, whole numbers add exactly in any order, but a computer rounds after each addition, so another order rounds in other places.

So in GPT-2 small, entry k of the library's list, for k from zero to eleven, is the stream after k blocks, up to rounding, and entry zero is x zero. The last entry is the exception: the library replaces it with the model's final output, which has been through the final norm, so the hidden state at the last layer is not a stream vector. We ran no trained Qwen3, Llama, Gemma or Mistral model. A fold-out at the end of this section has the full table, which includes a TransformerLens comparison made with raw weights, the tiny test models, and a warning about Gemma 3.

There is a short term box on the three names, and a trap box on where the bus picture misleads: a computer bus has one writer at a time and addresses, and the stream has neither.

Prediction one. The answer is a running total. In GPT-2 small, the list after block k is the embedding plus every write so far, up to rounding. The other options fail: the list holds no answer, only a sum; earlier writes stay in the sum; each word has its own list. Limit: the library's last list is normed.

Recap. The stream is the embedding plus every write, one list per word. We checked it on GPT-2 small, up to rounding, with the last entry as the exception. The informative check is that neighbouring library entries differ by the block's writes only by rounding. We ran no trained Qwen3, Llama, Gemma or Mistral model.

## bets | Three bets
The lens we want to end with has three parts: concepts are directions, features connect through weights into circuits, and similar features recur across models. Olah and colleagues, writing in twenty twenty about an image-recognition network, called them deliberately speculative claims. We treat each as a bet: an instance first, then the claim and how firmly it was held.

Bet one: features are directions. The instance, a toy of ours. Take six points in a plane. Three calm points: the point three, one; the point four, two; and the point five, three. And three urgent points: one, three; two, four; and three, five. Neither coordinate alone separates them, but second number minus first does: minus two for every calm point, plus two for every urgent one. If a model stored calm like this, the concept would be a direction, the arrow minus one, one. Section six redoes this with dot products.

The claim: features are the fundamental unit of neural networks; they correspond to directions. A feature is, for Nanda, a property of an input to the model, or some subset of that input. A concept is our word for a feature we can name. For Olah and colleagues a direction is a weighted mix of neurons in a layer. A neuron is one small unit of a network; section five shows one. The stream has no neurons, Nanda writes, so for the stream a direction is a weighted mix of its coordinates. That is ours.

How firmly? On whether networks consist of meaningful, understandable features, Olah and colleagues concede that the community is divided on whether this is true. If concepts were directions, a concept's strength would be a dot product.

Bet two: features are connected by weights, forming circuits. The instance, ours. Part A feeds part B with weight two, and B feeds part C with weight minus one. In a linear chain, a rise of one in A reaches C as two times minus one, which is minus two, and the weights alone tell you. Section five builds a small table of weights of this kind.

The claim: features are connected by weights, forming circuits. A circuit is some features and the weighted connections between them, a subgraph of the network. It has nothing to do with electricity. The step to whole behaviours is hedged: it seems like, with sufficient effort, statements about model behavior could be broken down into statements about circuits. Their worked circuits are three, in image-recognition networks. Testing one by editing its weights is a plan, not a result.

Bet three: the same features and circuits recur across models. The instance, ours. Turn every axis of the six-point toy by ninety degrees. All the coordinates change, yet it is the same toy. Is the feature in the turned toy the same feature? Universality asks that of different models.

The claim: analogous features and circuits form across models and tasks. Their evidence is, in their words, anecdotal, from low-level features in vision models. They suspect that the universality hypothesis is likely true, but further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule. Unlike the first two claims, it wouldn't be completely fatal to circuits research if false.

A trap: three sources, three vintages. Olah and colleagues use an image-recognition network called InceptionV1, and believe these claims hold generally. Elhage and colleagues study attention-only transformers of two layers or fewer. They promise a forthcoming paper on larger ones, which is not among our sources. Nanda's glossary is mostly a description of how GPT-2 works, though the variants are all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM. This is the one place where we state the scope for the whole post: none of the three says anything about Qwen3, Llama three, Gemma three or Mistral AI's models, base versus instruct models, what post-training changes inside a model, or steering, and none tests concepts as directions in a language model's stream. There is a fold-out that sorts Olah's lines by firmness.

Recap. Three bets: features are directions, circuits are the way features connect, and the same things recur across models. All three are deliberately speculative. The third is the only one not completely fatal if false. The sources are about older and smaller models than the ones people use now.

## rw | Reads and writes
Every part of the model also reads the stream before it writes. Take one small reader inside block two's MLP: a neuron, one small unit of the MLP, with an input vector r equal to one, two. It looks at the stream after attention two, which holds five, zero. What single number does it get? Multiply matching numbers and add: one times five plus two times zero is five. The vector r says how much to care about each place. With r equal to one, zero the reader takes only the first number; with zero, one, only the second.

The formula: r dot x equals r one times x one plus r two times x two. First times first plus second times second. This is the dot product, and the rule is the same for seven hundred and sixty-eight numbers. Nanda says reading is a projection, and Elhage and colleagues say layers read by performing a linear projection. In our terms, a linear projection is a set of dot products, one for each number the reader produces. We call the number a score.

Who hears whom. The stream is a sum, and the dot product of a sum is the sum of the dot products. So a read splits into one share for each writer. With r equal to one, two, the shares are five for the embedding, zero for attention one, one for MLP one, and minus one for attention two. They add up to five, the same as the direct read. In the widget, you can change r and watch the shares. This reader cannot hear attention one. Can you find a reader that cannot hear the embedding? The answer is folded on the page.

Two things to notice. First, attention one wrote two, minus one and it sits in the stream, yet this reader hears none of it. Two vectors whose dot product is zero are called orthogonal, at right angles. Second, reading is not the opposite of writing. Nanda: these operations are not opposites. A reader along r does not get back what a writer put along r, unless the other writers are orthogonal to r.

It works on a real stream too. In notebook two, GPT-2 small's stream at the last position after six blocks, read by a random unit vector, gives seven point two one one five six one. The sum of its thirteen shares, the embedding and the twelve writes of six blocks, gives the same, and the difference is zero in this run. A real model also puts a norm in front of every read. There is a fold-out on what that does to the arithmetic, at the end of the next section.

A write adds, and writes can cancel. MLP two writes minus one, two into a stream that holds five, zero. Nothing is replaced: five, zero plus minus one, two is four, two. The extreme case is the second prediction. The list holds two, two and block three writes minus two, minus two. The sum is zero, zero, and every reader gets zero. Does this happen in real models? Elhage and colleagues write of hints, which they word with may: that some neurons and heads may perform a kind of memory management role. Our toy shows cancellation is possible by arithmetic, not that models do it.

Prediction two. Only the sum, zero, zero. A write adds, it does not replace, and it is not kept as a separate item. Whether real models cancel writes is, in the sources, a hint worded with may.

Cashing in bet two. The widget's table gives one number for every pair of writer and reader. That is the shape of a weighted connection in a circuit, so it is like an edge weight, in our words. It is not one of Olah's edges, which join features in adjacent layers. The word linear has three uses here, and only two are settled. The stream is a sum of writes. A read is linear in the stream, so it splits over the writers. And a concept can be read linearly is a bet. The norm's division step is not linear.

Recap. A read is a dot product. It splits into one share per writer. A writer whose vector is orthogonal to the reader goes unheard. Writes can cancel. All of this is exact arithmetic, and none of it shows that real models behave this way.

## dir | Probe and push
Now many streams at once. Take six streams at one depth, for six short prompts. These are toy numbers, ours. Three are labelled calm and three urgent. The calm points are the point three, one; the point four, two; and the point five, three. The urgent points are the point one, three; the point two, four; and the point three, five. Can one number per point tell the groups apart? Try the coordinates. Along the first axis the groups overlap at three, and along the second axis too. No single coordinate separates them.

Now turn a reading arrow. A direction is an arrow of length one, by our convention. The length of a, b is the square root of a squared plus b squared. The arrow minus one, one has length root two. Divide by it and you get u equal to minus zero point seven oh seven, zero point seven oh seven: second minus first, scaled. Why length one? Drop a perpendicular from a point onto the arrow's line. For an arrow of length one, the score is how far along the arrow the foot of that perpendicular lies, so scores from different arrows can be compared. Check: take u equal to zero point six, zero point eight, which has length one, and x equal to five, zero. The score is three. The foot is three u, which is one point eight, two point four. And x minus the foot is three point two, minus two point four, which has dot product one point nine two minus one point nine two, so zero, with u: the dotted line is at right angles.

The score of a point is u dot x. For the calm point four, two the score is minus one point four one four. Every calm point scores minus one point four one four, and every urgent point scores plus one point four one four. One number separates the groups. The gap between them, which we call the margin, is the lowest urgent score minus the highest calm score: two point eight two eight. A positive margin means the groups are separated, with urgent above calm. Zero means they touch. A negative margin means they overlap, or calm lies above urgent.

With the angle phi measured from the first axis, a unit arrow is cosine phi, sine phi, so the score is x one cosine phi plus x two sine phi. In the widget, drag the dark arrow and watch the margin. At zero degrees the margin is minus four, at forty-five degrees minus two point eight two eight, at ninety degrees zero, at one hundred and twenty degrees two, and at one hundred and thirty-five degrees two point eight two eight. At forty-five degrees both groups get the same three scores. That probe is blind.

A probe is a read whose direction was fitted on labelled examples. Nanda describes a one-dimensional linear map, corresponding to a direction in activation space, which likely corresponds to that feature. Keep the word likely. A high score shows that information is present along the direction. It does not show that the model uses it. Cashing in bet one: if concepts were directions, this is what it would look like. Nothing here shows that a language model stores calm this way.

Steering is a translation. Add the same vector v to every point; take v equal to minus two, two. The dot product of a sum is the sum of the dot products, so every score moves by the same amount, u dot v, here two point eight two eight. Calm scores go from minus one point four one four to one point four one four. The formula: s of x plus v equals s of x plus u dot v.

What is a push good for in the toy? A push along u shifts every score the probe reads and leaves the margin at two point eight two eight, because both groups travel together. A push at right angles to u, such as two, two, has u dot v equal to zero: every point moves and no score moves. A push is a translation. It is not linear, because a linear map sends zero to zero, and adding v sends zero to v. A linear step plus a constant is affine.

What this does not say. Nothing here says that adding a vector changes behaviour as intended. On a real stream only the arithmetic holds: in notebook two, u dot of h plus alpha u, minus u dot h, minus alpha, was zero for every alpha we tried.

Prediction three. By the same amount, whichever point it is. Each score moves by u dot v, whatever the point. It is the same for near and far points, and for points on or off the probe's line.

Turn everything. Rotate the whole toy by ninety degrees: each x, y becomes minus y, x, and so does the reader. Take the read of section five, r equal to one, two on the stream five, zero. The stream becomes zero, five, and r becomes minus two, one, and the read is still five. Every coordinate changed, but lengths and angles did not, so no dot product changed: the four shares are five, zero, one and minus one before and after. In symbols: the turned r, dotted with the turned x, equals r dotted with x. Check for ninety degrees: the turned r is minus r two, r one, and the turned x is minus x two, x one. Their dot product is minus r two times minus x two, plus r one times x one, which is r one x one plus r two x two, the original. In the widget, the shares stay put at every angle while the first coordinate of the stream moves.

A basis is the set of axes we write coordinates in. A basis is privileged if its single coordinates, such as dimension seventeen, mean something on their own. Elhage and colleagues assert, for their idealised linear stream, that it does not have a privileged basis. The neurons of an MLP are different: after the activation function, in the standard basis a ReLU acts on each coordinate independently. A ReLU turns every negative number into zero, one number at a time. So do not read dimension seventeen as a feature on that ground alone. Compare the vectors of one model by dot products among them. Nanda adds a caveat: the standard basis is always slightly privileged, because floating-point numbers and the Adam training method favour it, so he thinks of it as a spectrum, not a switch.

Cashing in bet three. Let model B be model A with everything rotated. Every coordinate differs, but every dot product in B equals the one in A. A comparison that used coordinates would call B different, so a fair comparison must not use them. That is a reason, not a result about real models.

There are two fold-outs. One shows what a norm does to a read, with a toy where doubling the stream changes nothing after the norm. The other shows the logit lens as one more read: the last step of a model is a set of dot products, one per token.

Recap. A probe is a dot product along a fitted direction. In the toy, a turn of the arrow separates the groups, and one angle is blind. A push shifts every score by u dot v. A push along the probe moves the scores and leaves the margin alone, and a push at right angles moves none. Rotating everything changes every coordinate and no dot product. None of this shows what real models do.

## answer | Short answer
Here is the short answer, our reading and not a finding.

What is the list? In GPT-2 small, the list a library returns after k blocks, for k from zero to eleven, is the embedding, that is the token's table row plus its position list, plus every earlier write, at one position, up to rounding. The library's last entry has been through the final norm, so it is the exception. For a trained Qwen3, Llama, Gemma or Mistral model we have no measurement. In code and tiny random models, Gemma 3 norms each sub-layer's output before adding it. What would change our mind: an additivity error above rounding with the hooks placed correctly.

What can you do with it? A part reads the list by dot products, which split into one share per writer, and a writer at right angles to the reader goes unheard. It writes by adding, so writes can cancel. A probe is a dot product. Steering is a translation: it moves every score by u dot v, so a push along the probe shifts the scores and leaves the margin alone, while a push at right angles changes none. To compare two models, use each model's own dot products, not coordinates. That is ours, and Elhage and colleagues assert that an idealised stream has no privileged basis. All this is exact arithmetic. What a score means, or whether a push changes behaviour, the algebra does not say.

How firm is the lens? All three of Olah and colleagues' claims are deliberately speculative, and their evidence comes from image-recognition networks, mostly one called InceptionV1. For the trained language models people use now, the three sources give no test. Elhage and colleagues report circuits only in attention-only transformers of two layers or fewer, and none of the three tests concepts as directions or behaviours such as refusal or trust. We hold all three claims as bets. The toys say what each bet would mean, not whether it is true.

Recap. The list is a running sum, checked in GPT-2 small. Probes and pushes are exact arithmetic. The lens is three bets, held lightly.

## lens-linalg | Lens one: linear algebra
The first lens is linear algebra, and the link is the same mathematics. The stream is a sum of vectors. A write is a vector addition. A read is a dot product. Steering is a translation. No privileged basis means a rotation leaves dot products unchanged. Only this bookkeeping is the same mathematics. The sub-layers themselves are not linear.

Seeing is not doing, in our words. A probe observes: it reads the stream. Steering intervenes: it writes into it. A high probe score shows that information is present along a direction, not that later parts of the model use it. Testing use takes further tests, which this post does not run. Nanda's glossary lists interventions such as ablation, which means deleting a part, and activation patching, which swaps in the activation from another input; and a gradient-based test, TCAV, which compares a probe-like direction with the direction that, intuitively, would most raise an output. Its example is a zebra in an image. He cautions that zero ablation is arguably unprincipled, because the model may be using that part as a bias term.

One more limit. Cosine similarity, the dot product divided by the two lengths, is not additive. In notebook two, with v equal to three u, the cosine of h plus v with u was zero point one three one eight, while the cosine of h with u plus the cosine of v with u was one point oh nine three five. A dot product splits over writers. A cosine does not.

Connection to your research, computation. Probing, similarity analysis and steering are three statements about one vector. This lens fixes what the vector is and which operations on it are exact.

Recap. Linear algebra gives exactness for the bookkeeping, and three habits: check the sum, split a read over its writers, distrust a coordinate. It does not explain why concepts would be directions, anything nonlinear, or whether a probe's direction is used by the model. By Nanda's caveat, always slightly privileged, no privileged basis is a habit, not a law. That is ours.

## lens-info | Lens two: information theory
The second lens is information theory, and here the link is weaker. It is a structural analogy, ours: many writers add into one shared vector, and a reader sees only the sum, as in MacKay's binary multiple access channel, whose output is the sum of two inputs. The words bus and bandwidth are metaphors. No theorem or number transfers.

This lens asks a question and does not answer it. A stream has d numbers, and a model may have more things to say than d. How many separate messages can one reader recover, if some interference is tolerated?

What the sources say. Elhage and colleagues call the stream's dimensions something like memory or bandwidth: the words count dimensions. Nanda defines superposition as the case when a model represents more than n features in an n-dimensional activation space, and argues that with fifty thousand tokens and seven hundred and sixty-eight dimensions there almost has to be more features than dimensions. Almost matters: it is an argument, not a measurement. Here writes add; superposition means only the model-side sense.

MacKay sets an exercise on a channel with two sets of inputs and one output. In the simple case the output is the arithmetic sum of the two inputs: zero, one or two, with no noise. If the output is one, it could be that the input state was zero, one or one, zero, and the receiver cannot tell who sent the one. We use no result from the exercise.

A toy, ours. The stream has two numbers. This toy is superposition in the sense above: three features in two dimensions. Three features are written along directions at zero, one hundred and twenty and two hundred and forty degrees. Each feature has a strength, and the stream is the sum. Three readers read along the same three directions. Write only feature one: the stream is one, zero and the readers hear one, minus one half and minus one half. Readers two and three hear something nobody wrote for them. Write all three: the stream is zero, zero, and the readers hear zero, as if nothing were written. The pattern: each direction dotted with itself is one, and two different directions give minus one half, the cosine of one hundred and twenty degrees. So read j equals c j minus one half of the other two strengths added. In the widget, find a setting that looks exactly like silence. The answer is folded on the page.

Where the analogy breaks. MacKay's users cannot hear the output of the channel, while later parts of a transformer read the stream before they write. The sources give no rate, capacity or interference bound for the stream, so we do not claim it is a multiple-access channel.

Across the two lenses, ours. Linear algebra tells us what is exact when many writers share one list: sums split, dot products split, a rotation changes nothing. It cannot say how many messages the list can carry. Information theory asks exactly that, but offers a question, not a number.

Connection to your research, computation. If features share a stream, one probe direction may pick up several at once: Nanda writes, as an intuition, of other features with non-zero dot product with that direction. So any claim that a probe isolates a concept should say what else lies on the same line.

Recap. Information theory adds the question of limits: d dimensions, many messages, interference when directions are not orthogonal, and a case, all three on, that looks like silence. It does not tell us how much a real model packs in.

## turn | Your turn
Two notebooks, five exercises, one open question. Run the two notebooks that come with this post on your own computer; they work offline once the models are cached. Notebook one uses GPT-2 small through TransformerLens, a library that lets you read the stream at each step. It checks the sum block by block, plots the stream's length by depth, and runs the logit lens. Notebook two uses plain Hugging Face with hooks: set the model path to a model you have, and it finds which modules write and tests additivity. Each ends with blank exercise cells.

What to look for. The stream's length grows with depth: the median over ordinary positions goes from about five before block one to four hundred and seventy-two after twelve. The start token at position zero is much larger in the middle layers and smaller after twelve; we do not explain this. For GPT-2, in its compatibility mode, TransformerLens gives the Hugging Face stream minus its mean coordinate. And notebook one prints the margin as the better of the two orientations, so at zero degrees it shows zero, not minus four.

Exercise one, add. With the toy, compute the stream after block one and after block two, then find the MLP write that makes block two leave the stream unchanged.
Exercise two, who hears whom. For r equal to one, two, compute the four shares. Which writer is inaudible, and why?
Exercise three, project. Score the six points on one, zero; zero, one; and minus one, one over root two. Which gives a gap? Which direction gives both groups the same scores?
Exercise four, steer. Add two, zero to every point. By how much does every score on u change, and what happens to the margin? Then find a push of length two that moves the scores as far as possible.
Exercise five, rotate. Turn everything by ninety degrees, including r. Show that the four shares do not change. What does that say about coordinate one of the stream?
The solutions are folded on the page.

The transfer challenge. Take a direction you have used, for example a trained probe's weight vector. Write one sentence each: the depth and position where it was read; whether a norm stood between the stream and the probe; what a shift of length alpha along it adds to every score; and which of these arithmetic settles and which needs a behavioural test.

One open question. Suppose, as a toy assumption, ours, with real blocks not linear, that a block acts on the stream as the matrix with rows two, one and one, two. To apply it to a vector, let each row be a reader: the first number of the answer is row one dotted with the vector, the second is row two dotted with it. So it turns one, zero into two times one plus one times zero, and one times one plus two times zero: two, one, a new direction. But it sends one, one to three, three and one, minus one to one, minus one: these two are only stretched, by three and by one. Are there always such directions, and could they be natural axes that the stream's coordinates do not give us? Left open.

Recap. Run both notebooks and compare their numbers with the post. Do the five exercises by hand. Answer the transfer challenge for a probe you use. Keep the open question.

## work | In your work
Where this shows up in your work, in three parts.

Computation, reading: probing. A probe score shows that information is present along a direction, not that the model uses it. With every probe result, state the depth, the position, and whether a norm stood between the stream and the probe. Run notebook two on your own model, and claim the identity only where its additivity check passes.

Computation, comparing and steering. Compare two models through each model's own dot products, not coordinates. A dot product taken across two models is not protected by the rotation argument. A steering vector is a translation, and the score shift is u dot v whatever the data. What it does to behaviour is an empirical question that this post does not test.

Communication, framing and priming. This is a candidate bridge. If a prime or a frame were added to the stream as a vector, it would be one more write along a direction. That is ours. Whether a frame behaves like a direction is a bet of the same kind as bet one. It is a candidate, not a finding. For collaboration, there is no link in this post.

A working assumption, untested here. It is tempting to assume that a base model and its instruction-tuned version share the same stream space and directions. Nanda defines fine-tuning, training a pretrained model on a more specific task, and RLHF, fine-tuning that uses human raters' feedback, only as training procedures. Nothing in the sources says what they change inside a model. Testing it is later work.

Recap. Report the depth, position and norm placement of every probe. Compare each model by its own dot products. Treat framing as a bridge to test, and the base-versus-instruct assumption as untested.

## recall | Test yourself
Eight questions. Answer aloud, then listen to the answer.

One. What is the list that a library returns at index k, and what did the notebook check?
Pause.
For GPT-2 small and k from zero to eleven, the stream after k blocks. Neighbouring entries differed by the block's two writes by at most six point two times ten to the minus six, relative to the size of those writes, which is rounding. The last entry is normed.

Two. What must MLP two write to undo attention two, which wrote three, minus two?
Pause.
Minus three, two. Writes add, so they can cancel.

Three. Why does a read split over the writers, and when does a writer go unheard?
Pause.
The dot product of a sum is the sum of the dot products: one share per writer. A writer is unheard when its vector is orthogonal to the reader.

Four. Why does no coordinate separate calm from urgent in the toy cloud, and what does the blind probe show?
Pause.
Both groups reach three on each axis. At forty-five degrees both groups score two point eight two eight, four point two four three and five point six five seven.

Five. A push v moves every score by what? Why is it affine, not linear?
Pause.
By u dot v. A linear map sends zero to zero, and adding v sends zero to v. A linear step plus a constant is affine.

Six. What does no privileged basis let you do, and what does it not cover?
Pause.
Turn the stream and every reader together without changing any dot product, so use a model's own dot products, not coordinates. It does not cover MLP neurons.

Seven. Which of Olah's three claims would not be completely fatal to circuits research if false?
Pause.
Universality. All three are deliberately speculative.

Eight. In the probe toy, what does the sign of the margin mean, and why does a push along u leave it unchanged?
Pause.
Positive: separated, urgent above calm. Zero: touching. Negative: overlapping, or calm above urgent. A push v moves every score by u dot v, so both groups shift together and the gap stays two point eight two eight.

Recap. The list is a running sum. Reads are dot products that split by writer. Pushes are translations. Coordinates mean nothing alone. The three claims are bets.
