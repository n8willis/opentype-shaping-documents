# Style Guide #

This document details the preferred approach to wording, phrasing, and
topical coverage used in the shaping documents. Please do your best to
follow this guidance if you write patches or other contributions, to
speed up reviews.

In the present version of the shaping documents, the text itself is
written in Markdown -- unmodified Markdown wherever possible, although
in certain cases there may be GitHub-specific details
employed. Usually, any such deviation from basic Markdown is done to
guarantee that a specific visual feature works as intended or as a
work-around for a specific display quirk.

However, this document is not a guide to Markdown annotation.

Instead, this document describes stylistic choices at a more abstract
level -- such as how to write with clarity, how much specificity is
expected, and what word choices to consider.


**Table of Contents**

  - [General Principles](#general-principles)
      - [Linearity](#linearity)
      - [Countability](#countability)
      - [Consistency](#consistency)
  - [Voice](#voice)
  - [Word choice and terminology](#word-choice-and-terminology)
  - [Inline Elements](#inline-elements)
  - [](#)
  
  
## General Principles ##

This section lists some broad principles you should keep in mind. 

The primary goal of the shaping documents as a whole is to clearly
explain how OpenType shaping behavior should be implemented in a
shaping engine.

Consequently, writing should avoid causing confusion for the reader at
all costs. The following principles are intended to support that goal,
even though they may not be considered "good writing" in other
circumstances (such as literature or persuasive writing).

### Linearity ###

The first principle is linearity. Ideally, a reader could trace
through the execution of an OpenType shaping call for a run of text
and simultaneously follow along reading all of the steps in the
corresponding script's shaping document, without having to jump back
and forth in the document.

Avoiding such non-linear jumps within the text makes it less likely
that a reader will accidentally miss a step or get lost.

At times, ensuring that the text is linear results in the text being
longer that it otherwise could be. But a slightly longer text is
preferrable to an incident of reader confusion.

There are a few places where complete linearity is not possible, such
as algorithms that require the shaping engine to loop through a text
run until it has processed every code point of a particular
variety. That is acceptable; if you are not sure whether or not the
situation you are trying to document can be expressed in an entirely
linear fashion, try to write it linearly and ask for feedback.

There are several steps you may be able to take to make your writing
more linear.

First, try to number every stage and step of the process you are
describing. Forcing a process into numbered-list form will likely
reveal some steps that are mutually-exclusive alternative branches;
you should combine these branches into a single step and explain why
the branching happens and what circumstances trigger it.

Second, mention how steps connect to each other, including
foreshadowing future steps. For example, if code points
should be flagged in a certain way during step 3, mention that the
tags will be read in step 6 (or whatever).

For the reader, this foreshadowing prevents minor confusion the first
time they read through the process. For you as a writer, it helps you
to avoid a situation where you are writing a later step but discover
that you omitted a detail during an early step that is now important.
 
Third, consciously look out for situations where the shaping engine
implementation has no choice for what action to take next, and be
careful not to omit a description of that step.



### Countability ###

The second principle is countability. It should always be clear
to the reader precisely how many steps, options, branches,
permutations, or potential options exist for a particular situation.

Whenever possible, try to explicitly state how many items or options
exist. For example, say "there are 6 possible outcomes" instead of
"there are several posible outcomes".

There may be circumstances where there are an infinite number of
possibilities, of course. But, if there are only a finite number of
options, is it always preferable to state the exact number. Doing so
helps readers double-check that their count agrees with yours and that
neither of you has overlooked something.

Explicitly listing all of the possibilities is the best idea. Unless
the number is extremely large, it is better to provide a bulleted list
(or enumerate the possiblities in a sentance) than to give only the
total.

For example, saying "the vowel letters in the English alphabet are A,
E, I, O, U, and Y" is clearer than saying that there are 6 such
letters. This especially holds true when the count requires some
explanation, such as "the vowel letters in the English alphabet are A,
E, I, O, U, and Y -- although Y is a vowel only in some words, and is
a consonant in other words." The explanation is a long sentence, but
the meaning is far clearer than a shorter version like "English has
five vowels, or six if you include Y."

There is no universal rule for how many possibilities should be
considered "extremely large" enough to be too many for an explicit
list. If you are unsure about a particular situation, just ask for
feedback.

It is easier for a reader to get confused about "computed" counts
(such as permutations or potential outcomes from an operation) than to
get confused about static lists and constants. You should take extra
care to ensure that you correctly count and state these numbers.

You should also consciously look out for outcomes or list items that
are NULLs or no-ops. It is easy to forget to include them, but
forgetting to include them can confuse readers.


### Consistency ###

The third principle is consistency, meaning that related items in the
documents (a term, a step, an algorithm, etc.) should be treated in
the same way each and every time they occur. By adhering to this
principle, the similarities between related items are reinforced. In
addition, any reader who happens to start reading in the middle is
less likely to be confused simply because they encounter the second
item before they encounter the first item.

The simplest example of this principle is that any term, step,
algorithm, or other item should be referred to by the exact same
terminology every time it occurs. For example, if you say "vowel marker"
in one paragraph, you should say "vowel marker" every time; do not
shorten the term to "the marker" or "vowel" on later occurrences.

Following this advice means that there will be quite a bit of
repetition, and repetition is often not regarded as desirable writing.
Repetition is good for specification documents, however: it reinforces
ideas and makes it possible for a new reader to jump into the document
at any section (as often happens when a reader finds the document
through search results). Repetition also helps to prevent readers from
wondering whether or not two similar-sounding terms are referring to
the same item.

It is also useful to repeat the "status" of an item every time it is
mentioned. For example, repeat whether the item is mandatory or
optional, or repeat the purpose of a flag or tag. As is the case with
terminology repetition, this helps readers who start reading in the
middle of a document.

Beyond individual terms, you should also employ repetition for sets
and sequences of related items. Repeat lists of options every time you
are dealing with one of the options.

For example, the `calt` and `rclt` GSUB features are similar, and
differ only in the fact that `calt` is optional for the user but
`rclt` is mandatory.  When discussing the `calt` feature, it is best
to also mention `rclt` and note the relationship between the two.
That repetition might help prevent the reader from becoming confused
over whether the two features are the same, or are mutually-exclusive
alternatives of each other, or one is a subset/special-case of the
other.

At a higher level, maintain consistency by structuring documents and
sections of documents the same way. Related scripts and related
sections should follow the same document outline (wherever possible).

For example, the Indic2-model documents list all of the features
defined for Indic2 shaping: those features that are unused in a
particular script are still listed, and the fact that they are unused
is explained in a comment.


 
## Voice  ##

Voice is a matter of how the subject matter is phrased, how the point
being made in a document is approached, and how the document is
positioned with respect to the reader.


### Grammar ###

The most basic voice issues are related to grammar, and many are
commonplace advice for general writing.

First, try to always use "active" voice, not passive
voice. Specifically, when you are describing actions that the shaping
engine takes, phrase them in such a way that the shaping engine is the
subject of the sentence and the data (such as code points or glyphs)
are the objects. For example, say "the shaping engine examines the
next character" and not "the next character is examined by the shaping
engine." 

Second, write instructions and steps in direct, definite terms, not in
hypothetical terms. For example, say "now process the next character";
do not say "the shaping engine will be able to process the next
character."

Third, write in the present tense: describe steps and actions in the
words that you would use as they happen, not in words you would use
after the process is completed (nor words you would use before
starting). For example, say "move to the next position", and do not
say things like "the shaping engine must have seen all the positions"
or "the shaping engine will tag the next character."

Finally, use the third person. Do not say "I" or "we", and do not
address readers as "you".


### Point of view ###

Point of view is an idea that is related to the use of third person
(as mentioned in the Grammar subsection), but it also requires you to
consider what the reader's goal and expectations are. The main idea is
to preserve the perspective that the reader of the documents is a
shaping-engine implementer.

Specifically, maintain the perspective that the reader is not a type
designer or the creator of a document that might be processed. A
shaping-engine implementer will be looking for specific information
on how to process a text run to display it with an available font;
neither the content of the text run nor the content of the font will
be under the implementer's control.

In real life, of course, individual people can (and do) play multiple
roles, but these documents are focused solely on the task of
describing shaping behavior. Consequently, jumping back and forth
between different perspectives would likely cause confusion.

On a related note, you should also ensure that you maintain the
distinction that the reader is the implementer of the shaping engine
and is not the shaping engine itself.

It is also important to write from a neutral perspective about the
languages, writing systems, standards, software, and fonts that are
involved in the shaping process. Do not criticize anyone, even when
describing a workaround or an older technology that has now been
deprecated or superceded.

Finally, make sure that your writing maintains a clear separation
between each of the following components involve in shaping:
- the shaping engine
- the active font
- the document
- the user who is reading the document
- the rasterization engine
- the operating system

In real life, of course, some software stacks may integrate several of
the components involved, or some project might develop a shaping
engine specifically for a particular document, but those cases are not
generalized, and it is clearer make no assumptions about whether
components are connected or how they are related.


### Scope ###

These documents are meant to describe how OpenType shaping _should_
function. That is a large topic, so, in order to remain focused on the
goal without becoming excessively long, it is important to keep your
writing limited to this intended scope.

Describe what is supposed to happen and what known problems a shaping
engine should expect to encounter. The documents do not need to cover
all possible uses or special cases, so your writing should not expend
time addressing possibilities that extend outside of the intended
functionality.

For example, you do not need to describe how font designers might
employ a GSUB or GPOS feature in an unusual manner in order to handle
a situation that Unicode does not address. It may not always be clear
exactly where the line is between "saying the right amount" and
"saying too much," and there can certainly be instances where
mentioning a special case will help the reader understand. If you are
not sure how much to say or what to cut, just ask for feedback.

Similarly, these documents are also not intended to duplicate
information already in the specification for OpenType fonts or in the
Unicode Standard and Unicode Character Database. Some of this
information will come up naturally, but your writing should not
usually need to re-explain data structures or file internals. Here
again, if you are unsure whether you are including too much, just ask
for feedback.


### Canonicity ###

These documents are not authoritative, but they do attempt to
distinguish between things that are mandatory for OpenType shaping and
things that are merely helpful advice. Your writing should do the
same. Try to be clear about whether a step, algorithm, or data
structure is required or not.

You can say "must" or "is required to" to emphasize mandatory
items. More important, however, is to always say "may" or "it is
advisable to" when you are mentioning optional items.

You should also provide context to the reader for why something is
done. This does not mean writing a lengthy background paragraph for
every step, but do describe the intent behind major sections and
behind algorithms. If there is a primary reason for something as well
as secondary use-cases, you can mention all of reaons, but be clear
about which is the primary intent and which are of secondary
importance.

Several of the documents include annotations in "Note:" blocks. Some
of these Note blocks are simple explanations, but you can also use a
Note block to further distinguish an optional item from the
surrounding text.



## Word choice and terminology ##

Word selection is tricky subject on which to make ironclad
rules. However, there are still several principles that you should try
to adhere to in writing contributions to these documents.


### General wording ###

First, there are several "connector words" that it is preferrable to
include in all places where you are making a transition. These include
"therefore" and "however". Although they are longer than the
alternatives (such as "so" and "but"), their meanings are clearer.

Put a "therefore" at the start of a sentence that explains the result
of the preceding item. Put a "however" at the start of a sentence
that explains a contradiction or a counterpoint to the preceding item.

Use "in addition" to make it clear that a sentence is a new, follow-up
point. Use "in other words" to make it clear that you are a rephrasing
or clarifying the preceding item.

Longer wording in these situations is typically preferrable because
many short connector words (like "so") can have other meanings and may
be misinterpreted. If you are not sure what to write, try the longer
option first, or just ask for feedback.

When you give example sequences or example text strings, use common
words and phrases if possible. This helps to avert the small (but real)
risk that some reader will misunderstand and assume that a shaping
feature is not important. When a single character or a
less-than-word-length example is enough to make the point, of course,
then you should use that example.


### Technical terminology ###

Exact terminology is important for the technical aspects of describing
shaping behavior. This is especially true because the linguistic,
type, and software-development worlds can use the same word to mean
considerably different things, as well as because existing
specifications and companies each have their own long-established
terminology traditions.

Perhaps the most important issue is balancing Unicode terminology with
OpenType terminology. If Unicode and OpenType use different terms for
the same item, the best approach for these documents is to provide
both of the terms and make it clear which term comes from which
source.

Mention the type of an item if it is something unique to OpenType,
Unicode, or shaping. For example, say "the GDEF table" rather than
just "GDEF". You do not need to mention the types of items that are
standard programming primitives, but you can (especially if would
improve clarity).

Also be aware that terminology can be a culturally sensitive
topic. For example, terminology can be associated with historical
events or political divisions (such as terms that were adopted into
Unicode when borders were different or before certain languages had an
official status). Here again, the best approach is to present more
than one term (when there are several) and note the plurality, or
acknowledge the source of the term.

For technical items, these documents frequently rely on the
terminology used in HarfBuzz. There are two reasons for this. First,
HarfBuzz is a widely-adopted, technically mature, and actively
maintained OpenType shaping implementation that is not controlled by
private entity. Second, the HarfBuzz source code is free and open for
everyone to consult and reference.

For terminology used to describe processes and elements of OpenType
shaping, you should look to be consistent in how you use generic terms
that are often interchangeable. For example, "step" and "stage" could
each be used to describe a sequential section of the shaping
process. Similarly, "flag", "mark", and "tag" could all be used to
describe the action of labeling or designating an item.

Where one of these easily-overloaded words is already in use in these
documents, you should use the same word for the same meaning to be
consistent. For new writing, the best approach is to pick one term,
and use it consistently.

"cluster"/"syllable",
"run" "active font" "shaper" "shaping model" "shaping engine"
"preceding"/"following" vs "front"/"behind"/"last"




## Formatting and elements ##

### Tables ###

In order to compactly present large chunks of data, these documents
employ the "table" element from GitHub's extensions to Markdown. You
can read [GitHub's documentation for the table
element](https://github.github.com/gfm/#tables-extension-) for
specifics. 

It is important that you always include a heading row in every
table and a delimiter row beneath beneath the header row. 

Tables that present long lists of Unicode code-point data should also
include an empty row between each block of sixteen rows.

These documents are also meant to remain readable in plain-text
form (in addition to how they are rendered by GitHub's web
site). Consequently, you should always keep table columns the same
width, padding any short or empty cells so that they remain aligned
when viewed in a plain-text, monospaced editor.

In some cases, a particular table cell's content will be so long that
it makes perfect alignment impractical. For example, some Unicode
character charts exhibit this issue because a few cells include
extra-long canonical Unicode code point names. In these cases, you can
align the columns for the more common widths and simply extend just
the columns with extra-long content.

In addition, it is best to put whichever column has the longest cell
content at the right-hand side of the table, so that only the final
column requires special treatment.



### Code and pseudocode ###

When writing about algorithms or detailed procedures, capture the
structure and flow of the algorithm or process in standard,
conversational English. Do not use reserved control words or
programming-language tokens (such as "WHILE X==Y, DO Z"). The goal
should be a human-readable explanation, not pseudocode.

There are several reasons for this. First, different programming
languages have different syntax, so what may seem like usable code for
one language might contain significant errors for another
language. Sticking to non-code descriptions prevents readers from
attempting to copy-and-paste and encountering unexpected syntax
problems.

Second, using explicit code blocks to explain algorithms can make it
tempting for writers to optimize the code block for speed or other
constraints. The goal of the documents is to explain the process for a
human readers, so excessive optimization can make the result more
difficult to understand.

The one exception to the "human readable" goal above is where the
documents need to include regular expressions. Because
regular-expression syntax is so formal, it is better to include exact
regular expressions than to attempt to describe them in words. Include
regular expressions in `backticks` or in multi-line Markdown code
blocks. Nevertheless, you should also do your best to describe what
the regular-expression section is for.

Put literal tokens from specifications or code in `backticks`. It is
not necessary to use backticks for the names of structures that are
simply wrappers around something else and do not get acted upon
directly.

For example, the documents do not put backticks around GSUB
and GPOS, but the documents to put backticks around specific lookups,
like `liga` and `mkmk`. That is because GSUB and GPOS are tables that
contain the items (the lookups) that the shaping engine acts upon.


### Directories ###

Always include a README.md file in each directory. If you add a new
text file to a directory, check the directory's README.md and see if
it should be updated as well.


### Marking up sections ###



Leave two blank lines between subsections. Leave three blank lines
between top-levl sections. These blank lines help reading through the
source. You should use them even when sections and subsections are
numbered or have header markup.
