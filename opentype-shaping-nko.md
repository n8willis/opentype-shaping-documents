# N'Ko script shaping in OpenType #

This document details the general shaping procedure shared by all
N'Ko script styles, and defines the common pieces that style-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Joining properties](#joining-properties)
	  - [Mark classification](#mark-classification)
	  - [Character tables](#character-tables)
  - [The `<nko >` shaping model](#the-arab-shaping-model)
      - [1. Compound character composition and decomposition](#1-compound-character-composition-and-decomposition)
      - [2. Computing letter joining states](#2-computing-letter-joining-states)
      - [3. Applying the `stch` feature](#3-applying-the-stch-feature)
      - [4. Applying the language-form substitution features from GSUB](#4-applying-the-language-form-substitution-features-from-gsub)
      - [5. Applying the typographic-form substitution features from GSUB](#5-applying-the-typographic-form-substitution-features-from-gsub)
      - [6. Mark reordering](#6-mark-reordering)
      - [7. Applying the positioning features from GPOS](#7-applying-the-positioning-features-from-gpos)
  


## General information ##

The N'Ko script is used to write multiple languages in the Manding
language family, most commonly Maninka, Dyula, and Bambara. 

The N'Ko script uses features and rules derived from those of the
Arabic script, and OpenType defines N'Ko shaping features with a
subset of the features used in [Arabic](opentype-shaping-arabic.md) shaping.
Consequently, a shaping engine can support N'Ko and Arabic with a
[single shaping model](opentype-shaping-arabic-general.md).

N'Ko is a joining script that uses inter-word spaces, so each
codepoint in a text run may be substituted with one of several
contextual forms corresponding to what, if any, characters appear
before and after the codepoint. Most, but not all, letter sequences
join; shaping engines must track which positions trigger joining
behavior for each letter. 

N'Ko is written (and, therefore, rendered) from right to
left. Shaping engines must track the directionality of the text run
when scripts of different direction are mixed.

The N'Ko script tag defined in OpenType is `<nko >`. Because OpenType
script tags must be exactly four letters long, the `<nko >` tag
includes a trailing space. 


## Terminology ##

OpenType shaping uses a standard set of terms for elements of the
N'Ko script. The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Base** glyph or character is the standard term for a N'Ko
character that is capable of taking a diacritical mark. 

The base characters in N'Ko include both consonants and vowels.

**Kashida** (or **tatweel**) is the term for a glyph inserted into a
sequence for the purpose of elongating the baseline stroke of a
letter. Unicode documents use the term "tatweel" most frequently,
while OpenType documents use the term "kashida" most
frequently. Kashidas are typically inserted in order to justify lines
of text. 

In N'Ko, the kashida character is known as _lajanyalan_.


## Glyph classification ##

Because N'Ko is a joining (or cursive) script, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters to determine the contextually correct form for display.

### Joining properties ###

N'Ko characters are assigned a `JOINING_TYPE` property in the
Unicode standard that indicates how they join to adjacent
characters. There are six possible values: 

  - `JOINING_TYPE_LEFT` indicates that a character joins with
    the subsequent character, but does not join with the preceding
    character. 
	
  - `JOINING_TYPE_RIGHT` indicates that a character joins with the
    preceding character, but does not join with the subsequent character.	

  - `JOINING_TYPE_DUAL` indicates that a character joins with the
    preceding character and joins with the subsequent character.
	
  - `JOINING_TYPE_NON_JOINING` indicates that a character does not
    join with the preceding or with the subsequent character.
	
  - `JOINING_TYPE_TRANSPARENT` indicates that the character does not
    join with adjacent characters _and_ that the character must be
    skipped over when the shaping engine is evaluating the joining
    positions in a sequence of characters. When a
    `JOINING_TYPE_TRANSPARENT` character is encountered in a sequence,
    the `JOINING_TYPE` of the preceding character passes
    through. Diacritical marks are frequently assigned this value. 
	
  - `JOINING_TYPE_JOIN_CAUSING` indicates that the character forces
    the use of joining forms with the preceding and subsequent
    characters. Kashidas and the Zero Width Joiner (`U+200D`) are both
    `JOIN_CAUSING` characters.
  

In other scripts that use the general Arabic shaping model, letters
are also assigned to a `JOINING_GROUP` that indicates which
fundamental character they behave like with regard to joining
behavior.

Joining groups are not necessary in `<nko >` text shaping, so every
codepoint is assigned to the _null_ `JOINING_GROUP`.

### Mark classification ###

The Unicode standard defines a _canonical combining class_ for each
codepoint that is used whenever a sequence needs to be sorted into
canonical order. 

N'Ko marks all belong to standard combining classes:

| Codepoint | Combining class | Glyph                              |
|:----------|:----------------|:-----------------------------------|
|           | 220             | Other below-base combining marks   |
|           | 230             | Other above-base combining marks   |

The numeric values of these combining classes are used during Unicode
normalization.




			
			
### Character tables ###

Separate character tables are provided for the NKo block and for other miscellaneous
characters that are used in `<nko >` text runs:

  - [NKo character table](character-tables/character-tables-nko.md#nko-character-table)
  - [Miscellaneous character table](character-tables/character-tables-nko.md#miscellaneous-character-table)


The tables list each codepoint along with its Unicode general
category and its joining type. For letters, the table lists the
codepoint's joining group. For diacritical marks, the table lists the
codepoint's mark combining class. The codepoint's Unicode name and an example
glyph are also provided.

For example:

| Codepoint | Unicode category | Joining type | Joining group | Mark class | Glyph                        |
|:----------|:-----------------|:-------------|:--------------|:-----------|:-----------------------------|
|`U+07D3`   | Letter           | DUAL         | _null_        | _0_        | &#x07D3; Ba                  |
| | | | | |
|`U+07EB`   | Mark [Mn]        | TRANSPARENT  | _null_        | 230        | &#x07EB; Combining Short High Tone|



Codepoints with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 


#### Special-function codepoints ####

Other important characters that may be encountered when shaping runs
of N'Ko text include the dotted-circle placeholder (`U+25CC`), the
combining grapheme joiner (`U+034F`), the zero-width joiner (`U+200D`)
and zero-width non-joiner (`U+200C`), the left-to-right text marker
(`U+200E`) and right-to-left text marker (`U+200F`), and the no-break
space (`U+00A0`).

Each of these is of particular importance to shaping engines, because
these codepoints interact with the shaping engine, the text run, and
the active font, either to mediate non-default shaping behavior or to
relay information about the current shaping process.

The dotted-circle placeholder is frequently used when displaying a
combining mark in isolation. Real-world text documents may also use
other characters, such as hyphens or dashes, in a similar placeholder
fashion; shaping engines should cope with this situation gracefully.

Dotted-circle placeholder characters (like any Unicode codepoint) can
appear anywhere in text input sequences and should be rendered
normally. GPOS positioning lookups should attach mark glyphs to dotted
circles as they would to other non-mark characters. As visible glyphs,
dotted circles can also be involved in GSUB substitutions.

In addition to the default input-text handling process, shaping
engines may also insert dotted-circle placeholders into the text
sequence. Dotted-circle insertions are required when a non-spacing
mark or dependent sign is formed with no base character present.

This requirement covers:

  - Dependent signs that are assigned their own individual Unicode
    codepoints (such as most dependent-vowel marks or matras)
  
  - Dependent signs that are formed only by specific sequences of
    other codepoints (which is not common in N'Ko but can occur in
    other scripts)



The combining grapheme joiner (CGJ) is primarily used to alter the
order in which adjacent marks are positioned during the
mark-reordering stage, in order to adhere to the needs of a
non-default language orthography.

By default, OpenType shaping reorders sequences of adjacent marks by
sorting the sequence on the marks' Canonical_Combining_Class (Ccc)
values. The presence of a CGJ character within a sequence of marks has
the effect of splitting the sequence into two sequences of marks and,
therefore, halting any mark-reordering that would have occurred
between the marks on either side of the CGJ.

The zero-width joiner (ZWJ) is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for displaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.

The zero-width non-joiner (ZWNJ) is primarily used to prevent a
cursive connection between two adjacent characters that would, under
normal circumstances, form a join. 

The ZWJ and ZWNJ characters are, by definition, non-printing control
characters and have the _Default_Ignorable_ property in the Unicode
Character Database. In standard text-display scenarios, their function
is to signal a request from the user to the shaping engine for some
particular non-default behavior. As such, they are not rendered
visually.

> Note: Naturally, there are special circumstances where a user or
> document might need to request that a ZWJ or ZWNJ be rendered
> visually, such as when illustrating the OpenType shaping process, or
> displaying Unicode tables.

Because the ZWJ and ZWNJ are non-printing control characters, they can
be ignored by any portion of a software text-handling stack not
involved in the shaping operations that the ZWJ and ZWNJ are designed
to interface with. For example, spell-checking or collation functions
will typically ignore ZWJ and ZWNJ.

Similarly, the ZWJ and ZWNJ should be ignored by the shaping engine
when matching sequences of codepoints against the backtrack and
lookahead sequences of a font's GSUB or GPOS lookups.


The right-to-left mark (RLM) and left-to-right mark (LRM) are used by
the Unicode bidirectionality algorithm (BiDi) to indicate the points
in a text run at which the writing direction changes. Generally
speaking RLM and LRM codepoints do not interact with shaping.

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as vowel or diacritical marks and "Hamza") in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.


## The `<nko >` shaping model ##

Processing a run of `<nko >` text involves seven top-level stages:

1. Compound character composition and decomposition
2. Computing letter joining states
3. Applying the `stch` feature
4. Applying the language-form substitution features from GSUB
5. Applying the typographic-form substitution features from GSUB
6. Mark reordering
7. Applying the positioning features from GPOS


### 1. Compound character composition and decomposition ###

The `ccmp` feature allows a font to substitute

 - mark-and-base sequences with a pre-composed glyph including both
   the mark and the base (as is done in with a ligature substitution)
 - individual compound glyphs with the equivalent sequence of
   decomposed glyphs
 
If present, these composition and decomposition substitutions must be
performed before applying any other GSUB or GPOS lookups, because
those lookups may be written to match only the `ccmp`-substituted
glyphs. 


### 2. Computing letter joining states ###

In order to correctly apply the initial, medial, and final form
substitutions from GSUB during stage 5, the shaping engine must
tag every letter for possible application of the appropriate feature.

> Note: The following algorithm includes rules for processing `<syrc>`
> text in addition to `<nko >` text. Implementers concerned only with
> shaping `<nko >` text can omit the portions for `<syrc>`-specific
> rules. 

To determine which feature is appropriate, the shaping engine must
examine each word in turn and compute each letter's joining state from
the letter's `JOINING_TYPE` and the `JOINING_TYPE` of the
preceding character (if any).

> Note: Although N'Ko uses inter-word spaces, the `init` feature
> does _not_ refer to word-initial letters only and the `fina` feature
> does _not_ refer to word-final letters only.
>
> Rather, both of these terms are defined with respect to whether or
> not the preceding and subsequent letters form joins with the current
> letter. The letters at word boundaries will, naturally, take on
> initial and final forms, but initial and final forms of letters also
> occur regularly within words, when the letter in question is
> adjacent to a letter than does not form joins.

This computation starts from the first letter of the word, temporarily
tagging the letter for `isol` substitution. If the first
letter is the only letter in the word, the `isol` tag will remain unchanged.

From here, the algorithm consumes each character in the string, one at
a time, keeping track of the JOINING_TYPE of the previous character. 

If the current character is JOINING_TYPE_TRANSPARENT, move on to the next
character but preserve the currently-tracked JOINING_TYPE at its previous state.

If the preceding character's JOINING_TYPE is LEFT, DUAL, or
JOIN_CAUSING:
  - In `<syrc>` text, if the current character is "Alaph", tag the
    current character for `med2`, then update the tag for the
    preceding character:
	  - `isol` becomes `init`
	  - `fina` becomes `medi`
	  - `init` remains `init`
	  - `medi` remains `medi`
  - If the current character's JOINING_TYPE is RIGHT, DUAL, or
    JOIN_CAUSING, tag the current character for `fina`, then update
    the tag for the preceding character:
	  - `isol` becomes `init`
	  - `fina` becomes `medi`
	  - `init` remains `init`
	  - `medi` remains `medi`
  - If the current character's JOINING_TYPE is LEFT or NON_JOINING,
    tag the current character for `isol`, then update
    the tag for the preceding character:
	  - `medi` becomes `fina`
	  - `init` becomes `isol`
	  - `fina` remains `fina`
	  - `isol` remains `isol`

If the preceding character's JOINING_TYPE is RIGHT or NON_JOINING:
  - Tag the current character for `isol`, then update the tag for the
    preceding character:
	  - `medi` becomes `fina`
	  - `init` becomes `isol`
	  - `fina` remains `fina`
	  - `isol` remains `isol`
	  
After testing the final character of the word, if the text is in
`<syrc>` and current (final) character is "Alaph", perform an additional test:
  - If the preceding character's JOINING_GROUP is DALATH_RISH,
    tag the current character for `fin3`, then update the tag for the
    preceding character:
	  - `medi` becomes `fina`
	  - `init` becomes `isol`
	  - `fina` remains `fina`
	  - `isol` remains `isol`
  - If the preceding character's JOINING_GROUP is not DALATH_RISH, tag
    the current character for `fin2`, then update the tag for the
    preceding character:
	  - `medi` becomes `fina`
	  - `fin2` becomes `fina`
	  - `fin3` becomes `fina`
	  - `init` becomes `isol`
	  - `fina` remains `fina`
	  - `isol` remains `isol`
	  - `med2` remains `med2`


Once the last character of the word has been processed, proceed to the
next word and repeat the algorithm, starting at the beginning of the
next word.

> Note: Because the processing of the characters in the algorithm
> described above is deterministic, shaping engines may choose to
> implement the joining-state computation as a state machine, in a lookup
> table, or by any other means desirable.


At the end of this process, all letters should be tagged for possible
substitution by one of the `isol`, `init`, `medi`, or `fina` features.

### 3. Applying the `stch` feature ###

The `stch` feature decomposes and stretches special marks that are
meant to extend to the full width of words to which they are
attached. It was defined for use in `<syrc>` text runs for the "Syriac
Abbreviation Mark" (`U+070F`) but it can be used with similar marks in
other scripts.

> Note: N'Ko does not feature marks that require the `stch` feature;
> it is described here to maintain compatibility with other scripts
> that use the general Arabic shaping model.

To apply the `stch` feature, the shaping engine should first decompose the
`U+070F` glyph into components, which results in a beginning point,
midpoint, and endpoint glyphs plus one (or more) extension glyphs: at
least one extension between the beginning and midpoint glyphs and at
least one extension between the midpoint and endpoint glyphs. 

The shaping engine must then calculate the total length of the word to
which the mark applies. That length, minus the advance widths of the
beginning, middle, and endpoint glyphs of the mark, must be divided by
two. 

The result, divided by the advance width of the extension glyph
and rounded up to the next integer, tells the shaping engine how many
copies of the extension glyph must be placed between the midpoint and
each end of the mark.

Following this procedure ensures that the same number of extensions is
used on each side of the mark so that it remains symmetrical.

Finally, the decomposed mark must be reordered as follows: 

  - All of the glyphs in the sequence for the mark, _except_ for
    the final glyph, are repositioned as a group so that they precede
    the word to which the mark is attached.
  - The final glyph in the mark sequence is repositioned to the end of
    the word.
	

### 4. Applying the language-form substitution features from GSUB ###

The language-substitution phase applies mandatory substitution
features using the rules in the font's GSUB table. In preparation for
this stage, glyph sequences should be tagged for possible application 
of GSUB features.

The order in which these substitutions must be performed is fixed for
all scripts implemented in the N'Ko shaping model:

	locl
	isol
	fina
	fin2 (not used in N'Ko)
	fin3 (not used in N'Ko)
	medi
	med2 (not used in N'Ko)
	init
	rlig (not used in N'Ko)
	rclt (not used in N'Ko)
	calt
	

#### 4.1 locl ####

The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> GSUB substitutions in the following steps.

<!--- ![Localized form substitution](/images/nko/nko-locl.png) --->


#### 4.2 isol ####

The `isol` feature substitutes the default glyph for a codepoint with
the isolated form of the letter.

> Note: It is common for a font to use the isolated form of a letter
> as the default, in which case the `isol` feature would apply no
> substitutions. However, this is only a convention, and the active
> font may use other forms as the default glyphs for any or all
> codepoints.

<!--- ![Isolated form substitution](/images/nko/nko-isol.png) --->


#### 4.3 fina ####

The `fina` feature substitutes the default glyph for a codepoint with
the terminal (or final) form of the letter.

![Final form substitution](/images/nko/nko-fina.png)


#### 4.4 fin2 ####

This feature is not used in `<nko >` text.

#### 4.5 fin3 ####

This feature is not used in `<nko >` text.

#### 4.6 medi ####

The `medi` feature substitutes the default glyph for a codepoint with
the medial form of the letter.

![Medial form substitution](/images/nko/nko-medi.png)


#### 4.7 med2 ####

This feature is not used in `<nko >` text.

#### 4.8 init ####

The `init` feature substitutes the default glyph for a codepoint with
the initial form of the letter.

![Initial form substitution](/images/nko/nko-init.png)


#### 4.9 rlig ####

This feature is not used in `<nko >` text.



#### 4.10 rclt ####

This feature is not used in `<nko >` text.



#### 4.11 calt ####

The `calt` feature substitutes glyphs with contextual alternate
forms. In general, this involves replacing the default form of a
connecting glyph with an alternate that provides a preferable
connection to an adjacent glyph.

The `calt` feature, in contrast to `rclt` above, performs
substitutions that are not mandatory for orthographic
correctness. However, unlike `rclt`, the substitutions made by `calt`
can be disabled by application-level user interfaces.

<!--- ![Contextual alternate substitution](/images/nko/nko-calt.png) --->



### 5. Applying the typographic-form substitution features from GSUB ###

The typographic-substitution phase applies optional substitution
features using the rules in the font's GSUB table.

The order in which these substitutions must be performed is fixed for
all scripts implemented in the N'Ko shaping model:

    liga
	dlig
	cswh (not used in N'Ko)
	mset (not used in N'Ko)
	

#### 5.1 liga ####

The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.

<!--- ![Standard ligature substitution](/images/nko/nko-liga.png) --->



#### 5.2 dlig ####

The `dlig` feature substitutes additional optional ligatures that are
off by default. Substitutions made by `dlig` may be disabled by
application-level user interfaces.


#### 5.3 cswh ####

This feature is not used in `<nko >` text.



#### 5.4 mset ####

This feature is not used in `<nko >` text.


### 6. Mark reordering ###

<!--- http://www.unicode.org/reports/tr53/tr53-1.pdf --->

Sequences of adjacent marks must be reordered so that they appear in
canonical order before the mark-to-base and mark-to-mark positioning
features from GPOS can be correctly applied.

In particular, those marks that have strong affinity to the base
character must be placed closest to the base.

> Note: because N'Ko does not feature the "Shadda" mark or any
> marks that belong to _Modifier Combining Marks_ (MCM) classes, this
> stage should not involve any additional work when processing
> `<nko >` text runs. It is included here to maintain consistency with
> other scripts that utilize the general Arabic-based shaping model.

The algorithm for reordering a sequence of marks is:

  - First, move any "Shadda" (combining class `33`) characters to the
    beginning of the mark sequence.
	
  -	Second, move any subsequence of combining-class-`230` characters that begins
       with a `230_MCM` character to the beginning of the sequence,
       before all "Shadda" characters. The subsequence must be moved
       as a group.

  - Finally, move any subsequence of combining-class-`220` characters that begins
       with a `220_MCM` character to the beginning of the sequence,
       before all "Shadda" characters and before all class-`230`
       characters. The subsequence must be moved as a group.

### 7. Applying the positioning features from GPOS ###

The positioning stage adjusts the positions of mark and base
glyphs.

The order in which these features are applied is fixed for
all scripts implemented in the Arabic shaping model:

    curs (not used in N'Ko)
	kern
	mark
	mkmk

#### 7.1 `curs` ####


This feature is not used in `<nko >` text.


#### 7.2 `kern` ####

The `kern` adjusts glyph spacing between pairs of adjacent glyphs.


#### 7.3 `mark` ####

The `mark` feature positions marks with respect to base glyphs.

![Mark positioning](/images/nko/nko-mark.png)


#### 7.4 `mkmk` ####

The `mkmk` feature positions marks with respect to preceding marks,
providing proper positioning for sequences of marks that attach to the
same base glyph.


