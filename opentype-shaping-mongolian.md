# Mongolian script shaping in OpenType #

This document the general shaping procedure shared by all 
Mongolian script styles, and defines the common pieces that style-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Joining properties](#joining-properties)
	  - [Mark classification](#mark-classification)
	  - [Character tables](#character-tables)
  - [The `<mong>` shaping model](#the-arab-shaping-model)
      - [1. Compound character composition and decomposition](#1-compound-character-composition-and-decomposition)
      - [2. Computing letter joining states](#2-computing-letter-joining-states)
      - [3. Applying the `stch` feature](#3-applying-the-stch-feature)
      - [4. Applying the language-form substitution features from GSUB](#4-applying-the-language-form-substitution-features-from-gsub)
      - [5. Applying the typographic-form substitution features from GSUB](#5-applying-the-typographic-form-substitution-features-from-gsub)
      - [6. Mark reordering](#6-mark-reordering)
      - [7. Applying the positioning features from GPOS](#7-applying-the-positioning-features-from-gpos)
  


## General information ##

The Mongolian script is used to write multiple languages, most commonly
Mongolian, Sibe (or Xibe), and Manchu.  In addition, extensions to the
character set may be used to write Tibetan and Sanskrit. 

The classical Mongolian alphabet includes several letters that differ
phonetically but are identical in their visual appearance, such as "O"
(`U+1823`, &#x1823;) and "U" (`U+1824`, &#x1824;). A variant of the
classical alphabet, called Todo (or "clear") Mongolian, was developed
in the 17th Century to remove such ambiguous forms. The Todo
characters are also included in the Mongolian Unicode block.

Due to the common shaping features that the Mongolian script shares
with Arabic, a shaping engine can support Mongolian with the same
shaping model [used for Arabic and related writing systems](opentype-shaping-arabic-general.md).

However, several other, unrelated scripts are also used to write
Mongolian, including 'Phags-Pa, Soyombo, Zanabazar Square, Cyrillic, and
Latin. Each of these scripts has its own OpenType shaping rules and its
Unicode block, and does not use the general Arabic shaping model.

Mongolian is a joining script that uses inter-word spaces, so each
codepoint in a text run may be substituted with one of several
contextual forms corresponding to what, if any, characters appear
before and after the codepoint. Most, but not all, letter sequences
join; shaping engines must track which positions trigger joining
behavior for each letter. 

Mongolian is normally written (and, therefore, rendered) vertically,
from top to bottom. Isolated words or short phrases in Mongolian that
are included in text blocks of horizontal scripts are generally
rotated 90 degrees counterclockwise, so that the letters run
left-to-right. On systems that do not support vertical text setting,
this left-to-right rendering is a common fallback strategy for full
runs of Mongolian text.


## Terminology ##

OpenType shaping uses a standard set of terms for elements of the
Mongolian script. The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Base** glyph or character is the standard term for a Mongolian
character that is capable of taking a diacritical mark. 

All consonants and vowels are base characters in
Mongolian. Diacritical marks are not used in the Mongolian, Sibe, or
Manchu languages, but may be encountered in Tibetan or Sanskrit.

A number of consonants in Mongolian take on different forms depending
on the vowels used elsewhere in the word. In addition, some letters
take on different forms when depending on whether they occur in the
first syllable of a word or whether they are used in a native
Mongolian word versus a foreign word. Mongolian fonts implement
substitutions capturing most of these form rules using GSUB. However,
there are occasions where the correct form may not be determined from
context alone.

To indicate the correct form, the text run can include a **free
variation selector** immediately after the letter in
question. There are three free variation selectors in the Mongolian
block (FVS1, FVS2, and FVS3), although some letters have alternate
forms defined only for FVS1 or only for FVS1 and FVS2.

In addition, letters vary as to whether alternate forms exist for the
isolated, initial, medial, or final position, or for several
positions. The forms that each selector triggers for each letter is
defined in the Unicode Mongolian block. 

For example, the letter "Manchu I" (`U+1873`) has three alternate
forms defined for the medial position:

![Non FVS form substitution](/images/mongolian/mongolian-fvs-none.png)

![FVS1 form substitution](/images/mongolian/mongolian-fvs-fvs1.png)

![FVS2 form substitution](/images/mongolian/mongolian-fvs-fvs2.png)

![FVS3 form substitution](/images/mongolian/mongolian-fvs-fvs3.png)


Free variation selectors have no visual appearance and no advance
width; they are used only to trigger the proper substitution in the
active font's GSUB tables. 




In some Mongolian words, a word-final "A" or "E" is written
disconnected from the preceding letter. In such situations, the
**Mongolian vowel separator** formatting character can be included
between the two letters to trigger such a space.

Sibe text may use the **Sibe syllable boundary marker** (`U+1807`) to
denote syllable boundaries in foreign loanwords.

**Kashida** (or **tatweel**) is the Arabic term for a glyph inserted
into a sequence for the purpose of elongating the baseline stroke of
an Arabic letter. Mongolian features a similar character, called
**nirugu**, in the Mongolian Unicode block.



## Glyph classification ##

Because Mongolian is a joining (or cursive) script, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters to determine the contextually correct form for display.

### Joining properties ###

Mongolian characters are assigned a `JOINING_TYPE` property in the
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
  
  
> Note: Almost all characters in Mongolian are of joining type
> `DUAL`. The exceptions are `TRANSPARENT`, `NON_JOINING`, and
> `JOIN_CAUSING`. Thus, the ambiguity that might be encountered due to
> the usage of `LEFT` and `RIGHT` in the names of the other joining
> types (which are so named in reference to the relative positions as
> used in Arabic and related scripts) is avoided.

In other scripts using the Arabic shaping model, letters are also
assigned to a `JOINING_GROUP` that indicates which fundamental
character they behave like with regard to joining behavior. Mongolian,
however, does not use joining groups; all characters are assigned to
the _null_ joining group.


### Mark classification ###

The Unicode standard defines a _canonical combining class_ for each
codepoint that is used whenever a sequence needs to be sorted into
canonical order. 

Only one Mongolian mark belongs to a standard combining
class:

| Codepoint | Combining class | Glyph                              |
|:----------|:----------------|:-----------------------------------|
|`U+18A9`   | 228             | &#x18A9; Ali Gali Dagalga          |


All other codepoints in the Mongolian block belong to class _0_.

The numeric values of these combining classes are used during Unicode
normalization.
	
			
### Character tables ###

Separate character tables are provided for the Mongolian and Mongolian
Supplement blocks, as well as for other miscellaneous
characters that are used in `<mong>` text runs:

  - [Mongolian character table](character-tables/character-tables-mongolian.md#mongolian-character-table)
  - [Mongolian Supplement character table](character-tables/character-tables-mongolian.md#mongolian-supplement-character-table)
  - [Miscellaneous character table](character-tables/character-tables-mongolian.md#miscellaneous-character-table)


The tables list each codepoint along with its Unicode general
category and its joining type. For letters, the table lists the
codepoint's joining group. For diacritical marks, the table lists the
codepoint's mark combining class. The codepoint's Unicode name and an example
glyph are also provided.

For example:

| Codepoint | Unicode category | Joining type | Joining group | Mark class | Glyph                        |
|:----------|:-----------------|:-------------|:--------------|:-----------|:-----------------------------|
|`U+1828`   | Letter           | DUAL         | _null_        | _0_        | &#x1828; Na                  |
| | | | | |
|`U+1885`   | Mark [Mn]        | TRANSPARENT  | _null_        | _0_        | &#x1885; Ali Gali Baluda     |



Codepoints with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 


Other important characters that may be encountered when shaping runs
of Mongolian text include the dotted-circle placeholder (`U+25CC`),
the zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`),
the no-break space (`U+00A0`) and the narrow no-break space(`U+202F`).

The dotted-circle placeholder is frequently used when displaying a
diacritical mark in isolation. Real-world text documents may
also use other characters, such as hyphens or dashes, in a similar
placeholder fashion; shaping engines should cope with this situation
gracefully.

The zero-width joiner (ZWJ) is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for displaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.


<!--- Zero-Width Non Joiner explanation --->

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as diacritical marks) in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.

The narrow no-break space serves a different function in Mongolian. It
is used to visually separate the main body of a word from the word's
suffix. Not all Mongolian words incorporate a narrow no-break space.


## The `<mong>` shaping model ##

Processing a run of `<mong>` text involves seven top-level stages:

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
> text in addition to `<mong>` text. Implementers concerned only with
> shaping `<mong>` text can omit the portions for `<syrc>`-specific
> rules. 

To determine which feature is appropriate, the shaping engine must
examine each word in turn and compute each letter's joining state from
the letter's `JOINING_TYPE` and the `JOINING_TYPE` of the
preceding character (if any).

> Note: Although Mongolian uses inter-word spaces, the `init` feature
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
all scripts implemented in the Arabic shaping model:

	locl
	isol
	fina
	fin2 (not used in <mong>)
	fin3 (not used in <mong>)
	medi
	med2 (not used in <mong>)
	init
	rlig
	rclt
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


#### 4.2 isol ####

The `isol` feature substitutes the default glyph for a codepoint with
the isolated form of the letter.

> Note: It is common for a font to use the isolated form of a letter
> as the default, in which case the `isol` feature would apply no
> substitutions. However, this is only a convention, and the active
> font may use other forms as the default glyphs for any or all
> codepoints.

![Isolated form substitution](/images/mongolian/mongolian-isol.png)


The Mongolian free-variation selectors can also be used in conjunction
with `isol` to trigger alternate forms of certain letters as required
by the orthography.

![Isolated FVS1 form substitution](/images/mongolian/mongolian-isol-fvs1.png)


#### 4.3 fina ####

The `fina` feature substitutes the default glyph for a codepoint with
the terminal (or final) form of the letter.

![Final form substitution](/images/mongolian/mongolian-fina.png)


The Mongolian free-variation selectors can also be used in conjunction
with `fina` to trigger alternate forms of certain letters as required
by the orthography.

![Final FVS2 form substitution](/images/mongolian/mongolian-fina-fvs2.png)


#### 4.4 fin2 ####

This feature is not used in `<mong>` text.

#### 4.5 fin3 ####

This feature is not used in `<mong>` text.

#### 4.6 medi ####

The `medi` feature substitutes the default glyph for a codepoint with
the medial form of the letter.

![Medial form substitution](/images/mongolian/mongolian-medi.png)


The Mongolian free-variation selectors can also be used in conjunction
with `medi` to trigger alternate forms of certain letters as required
by the orthography.

![Medial FVS1 form substitution](/images/mongolian/mongolian-medi-fvs1.png)


#### 4.7 med2 ####

This feature is not used in `<mong>` text.

#### 4.8 init ####

The `init` feature substitutes the default glyph for a codepoint with
the initial form of the letter.

![Initial form substitution](/images/mongolian/mongolian-init.png)


The Mongolian free-variation selectors can also be used in conjunction
with `init` to trigger alternate forms of certain letters as required
by the orthography.

![Initial FVS1 form substitution](/images/mongolian/mongolian-init-fvs1.png)


#### 4.9 rlig ####

The `rlig` feature substitutes glyph sequences with mandatory
ligatures. Substitutions made by `rlig` cannot be disabled by
application-level user interfaces.

![Required ligature substitution](/images/mongolian/mongolian-rlig.png)


#### 4.10 rclt ####

The `rclt` feature substitutes glyphs with contextual alternate
forms. In general, this involves replacing the default form of a
connecting glyph with an alternate that provides a preferable
connection to an adjacent glyph.

The `rclt` feature should be used to perform such substitutions that
are required by the orthography of the active script and
language. Substitutions made by `rclt` cannot be disabled by 
application-level user interfaces.

#### 4.11 calt ####

The `calt` feature substitutes glyphs with contextual alternate
forms. In general, this involves replacing the default form of a
connecting glyph with an alternate that provides a preferable
connection to an adjacent glyph.

The `calt` feature, in contrast to `rclt` above, performs
substitutions that are not mandatory for orthographic
correctness. However, unlike `rclt`, the substitutions made by `calt`
can be disabled by application-level user interfaces.

<!--- ![Contextual alternate substitution](/images/mongolian/mongolian-calt.png) --->



### 5. Applying the typographic-form substitution features from GSUB ###

The typographic-substitution phase applies optional substitution
features using the rules in the font's GSUB table.

The order in which these substitutions must be performed is fixed for
all scripts implemented in the Arabic shaping model:

    liga
	dlig
	cswh
	mset
	

#### 5.1 liga ####

The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.

<!--- ![Standard ligature substitution](/images/mongolian/mongolian-liga.png) --->



#### 5.2 dlig ####

The `dlig` feature substitutes additional optional ligatures that are
off by default. Substitutions made by `dlig` may be disabled by
application-level user interfaces.


#### 5.3 cswh ####

The `cswh` feature substitutes contextual swash variants of
glyphs. 

<!--- For example, the active font might substitute a longer variant
of "Noon" when a certain number of subsequent glyphs do not descend
below the baseline. --->


#### 5.4 mset ####

The `mset` feature performs mark positioning by substituting sequences
of bases and marks with precomposed base-and-mark glyphs.

> Note: Positioning marks with the `mark` and `mkmk` features of GPOS is
> preferred, because `mset` can interfere with the OpenType shaping
> process. For example, substitution rules contained in `mset` may not be able to
> account for necessary mark-reordering adjustments conducted in the
> next stage.
> 
> Nevertheless, when the active font uses `mset` substituions, the
> shaping engine must deal with the situation gracefully.

### 6. Mark reordering ###

<!--- http://www.unicode.org/reports/tr53/tr53-1.pdf --->

Sequences of adjacent marks must be reordered so that they appear in
canonical order before the mark-to-base and mark-to-mark positioning
features from GPOS can be correctly applied.

> Note: because Mongolian does not feature the "Shadda" mark or any
> marks that belong to _Modifier Combining Marks_ (MCM) classes, this
> stage should not involve any additional work when processing
> `<mong>` text runs. It is included here to maintain consistency with
> other scripts that utilize the general Arabic-based shaping model.

In particular, those marks that have strong affinity to the base
character must be placed closest to the base.

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

    curs
	kern
	mark
	mkmk

#### 7.1 `curs` ####

The `curs` feature perform cursive positioning. Each glyph has an
entry point and exit point; the `curs` feature positions glyphs so
that the entry point of the current glyph meets the exit point of the
preceding glyph.

<!--- ![Cursive positioning](/images/mongolian/mongolian-curs.png) --->


#### 7.2 `kern` ####

The `kern` adjusts glyph spacing between pairs of adjacent glyphs.


#### 7.3 `mark` ####

The `mark` feature positions marks with respect to base glyphs.

<!--- ![Mark positioning](/images/mongolian/mongolian-mark.png) --->


#### 7.4 `mkmk` ####

The `mkmk` feature positions marks with respect to preceding marks,
providing proper positioning for sequences of marks that attach to the
same base glyph.


