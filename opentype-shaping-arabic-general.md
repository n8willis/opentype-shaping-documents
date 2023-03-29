# Arabic-style shaping in OpenType #

This document details the general shaping procedure shared by Arabic, N'Ko,
Syriac, and Mongolian. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Joining properties](#joining-properties)
	  - [Mark classification](#mark-classification)
	  - [Character tables](#character-tables)
  - [The general Arabic-based shaping model](#the-general-arabic-based-shaping-model)
      - [1. Transient reordering of modifier combining marks](#1-transient-reordering-of-modifier-combining-marks)
      - [2. Compound character composition and decomposition](#2-compound-character-composition-and-decomposition)
      - [3. Computing letter joining states](#3-computing-letter-joining-states)
      - [4. Applying the `stch` feature](#4-applying-the-stch-feature)
      - [5. Applying the language-form substitution features from GSUB](#5-applying-the-language-form-substitution-features-from-gsub)
      - [6. Applying the typographic-form substitution features from GSUB](#6-applying-the-typographic-form-substitution-features-from-gsub)
      - [7. Applying the positioning features from GPOS](#7-applying-the-positioning-features-from-gpos)
  


## General information ##

Several scripts can be supported by the general OpenType shaping model
used for Arabic. These writing systems observe similar rules and
conventions, even if they are not historically related to
Arabic. Therefore, OpenType defines many of the same GSUB and GPOS
features as supported for the corresponding script tags. These scripts include:

  - [Arabic](opentype-shaping-arabic.md)
  - [N'Ko](opentype-shaping-nko.md)
  - [Syriac](opentype-shaping-syriac.md)
  - [Mongolian](opentype-shaping-mongolian.md)

The information found below is intended to serve as a general guide;
script-specific information can be found in the linked document for
each script.

Each of these writing systems uses a joining script that uses
inter-word spaces. Therefore, each codepoint in a text run may be
substituted with one of several contextual forms corresponding to
what, if any, characters appear before and after the codepoint. Most,
but not all, letter sequences join; shaping engines must track which
positions trigger joining behavior for each letter. 

Arabic, N'Ko, and Syriac are written (and, therefore, rendered) from right to
left. Mongolian is written vertically, from top to bottom. Shaping
engines must track the directionality of the text run when scripts of
different direction are mixed.

## Terminology ##

OpenType shaping uses a standard set of terms for elements of the
supported scripts. The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Base** glyph or character is the standard term for a
character that is capable of taking a diacritical mark. 

**Kashida** (or **tatweel**) is the term for a glyph inserted into a
sequence for the purpose of elongating the baseline stroke of a
letter. Unicode documents use the term "tatweel" most frequently,
while OpenType documents use the term "kashida" most
frequently. Kashidas are typically inserted in order to justify lines
of text. 



## Glyph classification ##

In joining (or cursive) scripts, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters to determine the contextually correct form for display.

### Joining properties ###

Characters are assigned a `JOINING_TYPE` property in the
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
  

In some scripts (such as Arabic and Syriac), letters are also assigned
to a `JOINING_GROUP` that indicates which fundamental character they
behave like with regard to joining behavior. Each of the basic letters
in the script typically belongs to its own `JOINING_GROUP`, while
supplemental and accented letters are usually assigned to the
`JOINING_GROUP` that corresponds to the underlying base letter, with
no diacritics or other marks. 

For example, the Persian letter "Peh" (`U+067E`) is visually
represented as the Arabic letter "Beh" (`U+0628`), but with two additional
below-base "ijam" marks. Consequently, "Peh" is assigned to the `BEH`
`JOINING_GROUP`.

Mongolian and N'Ko, notably, do not make use of joining groups. Every
letter in these scripts belongs to the _null_ or `NO_JOINING_GROUP`
group.


### Mark classification ###

The Unicode standard defines a _canonical combining class_ for each
codepoint that is used whenever a sequence needs to be sorted into
canonical order. 

The marks in most scripts belong to the standard combining
classes. For example:

| Codepoint | Combining class | Glyph                              |
|:----------|:----------------|:-----------------------------------|
|`U+064B`   | 27              | &#x064B; Fathatan / Open fathatan  |
|`U+064C`   | 28              | &#x064C; Dammatan / Open dammatan  |
|`U+064D`   | 29              | &#x064D; Kasratan / Open Kasratan  |
|`U+064E`   | 30              | &#x064E; Fatha / Small fatha       |
|`U+064F`   | 31              | &#x064F; Damma / Small damma       |
|`U+0650`   | 32              | &#x0650; Kasra / Small kasra       |
|`U+0651`   | 33              | &#x0651; Shadda                    |
|`U+0652`   | 34              | &#x0652; Sukun                     |
|`U+0670`   | 35              | &#x0670; Superscript Alef          |
|           | 220             | Other below-base combining marks   |
|           | 230             | Other above-base combining marks   |

The numeric values of these combining classes are used during Unicode
normalization. Sequences of marks are sorted by combining class,
reordering the sequence into increasing numerical order.

In addition, some Arabic and Syriac marks require special handling
when shaping Arabic text, during the mark-reordering stage. These
marks fall into two classes of _Modifier Combining Marks_ (MCM) that
may need to be repositioned closer to the base character, when they
occur in sequences of multiple marks. 

The sets are:
  - Below-base (class 220) MCMs
  - Above-base (class 230) MCMs
  
These classifications are used in the [mark-transient-reordering
stage](#1-transient-reordering-of-modifier-combining-marks).

Lists of the marks that belong to each MCM classes are included in the
script-specific shaping documents for Arabic and Syriac.
			
			
### Character tables ###

Character tables for all of the scripts, plus important miscellaneous
characters, are available here: 

  - [Arabic](character-tables/character-tables-arabic.md#arabic-character-table)
  - [Syriac](character-tables/character-tables-syriac.md#syriac-character-table)
  - [N'Ko](character-tables/character-tables-nko.md#nko-character-table)
  - [Mongolian](character-tables/character-tables-mongolian.md#mongolian-character-table)


## The general Arabic-based shaping model ##

Processing a run of text tagged with any of the scripts supported by
the general Arabic shaping model involves seven top-level stages:

1. Transient reordering of modifier combining marks
2. Compound character composition and decomposition
3. Computing letter joining states
4. Applying the `stch` feature
5. Applying the language-form substitution features from GSUB
6. Applying the typographic-form substitution features from GSUB
7. Applying the positioning features from GPOS


### 1. Transient reordering of modifier combining marks ###

<!--- http://www.unicode.org/reports/tr53/tr53-1.pdf --->
> Note: the transient reordering of modifier combining marks is
> necessary only for scripts that can feature the "Shadda" mark or
> marks that belong to _Modifier Combining Marks_ (MCM) classes.

Sequences of adjacent marks must be reordered so that they appear in
the appropriate visual order before the mark-to-base and mark-to-mark
positioning features from GPOS can be correctly applied.

In particular, those marks that have strong affinity to the base
character must be placed closest to the base.

This mark-reordering operation is distinct from the standard,
cross-script mark-reordering performed during Unicode
normalization. The standard Unicode mark-reordering algorithm is based
on comparing the _Canonical_Combining_Class_ (Ccc) properties of mark
codepoints, whereas this script-specific reordering utilizes the
_Modifier_Combining_Mark_ (`MCM`) subclasses specified in the
character tables.

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

> Note: Unicode describes this mark-reordering operation, the Arabic
> Mark Transient Reordering Algorithm (AMTRA), in Technical Report 53,
> which describes it in terms that are distinct from standard,
> Ccc-based mark reordering.
>
> Specifically, AMTRA is designated as an operation performed during
> text rendering only, which therefore does not impact other
> Unicode-compliance issues such as allowable input sequences or text
> encoding.
>
> However, shaping engines may choose to perform the reordering of
> modifier combining marks in conjunction with their Unicode
> normalization functionality for increased efficiency.

### 2. Compound character composition and decomposition ###

The `ccmp` feature allows a font to substitute

 - mark-and-base sequences with a pre-composed glyph including both
    the mark and the base (as is done in with a ligature substitution)
	
  - individual compound glyphs with the equivalent sequence of
    decomposed glyphs (such as decomposing a letter with ijam into a
    separate fundamental-letter glyph followed by an ijam-only glyph,
    to permit more precise positioning)
 
If present, these composition and decomposition substitutions must be
performed before applying any other GSUB or GPOS lookups, because
those lookups may be written to match only the `ccmp`-substituted
glyphs. 


### 3. Computing letter joining states ###

In order to correctly apply the initial, medial, and final form
substitutions from GSUB during stage 6, the shaping engine must
tag every letter for possible application of the appropriate feature.

> Note: not all of the rules detailed below apply to every script that
> is supported by the general Arabic shaping model.

To determine which feature is appropriate, the shaping engine must
examine each word in turn and compute each letter's joining state from
the letter's `JOINING_TYPE` and the `JOINING_TYPE` of the
preceding character (if any).

> Note: Although the supported scripts use inter-word spaces, the
> `init` feature does _not_ refer to word-initial letters only and the
> `fina` feature does _not_ refer to word-final letters only.
>
> Rather, both of these terms are defined with respect to whether or
> not the preceding and subsequent letters form joins with the current
> letter. The letters at word boundaries will, naturally, take on
> initial and final forms, but initial and final forms of letters also
> occur regularly within words, when the letter in question is
> adjacent to a letter that does not form joins.

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

Otherwise, tag the current character for `isol`.

After testing the final character of the word, if the text is in `<syrc>` and
if the last character that is not JOINING_TYPE_TRANSPARENT or
JOINING_TYPE_NON_JOINING is "Alaph", perform an additional test:
  - If the preceding character is JOINING_TYPE_LEFT, tag the current character
    for `fina`
  - If the preceding character's JOINING_GROUP is DALATH_RISH, tag the current
    character for `fin3`
  - Otherwise, tag the current character for `fin2`


Once the last character of the word has been processed, proceed to the
next word and repeat the algorithm, starting at the beginning of the
next word.

> Note: Because the processing of the characters in the algorithm
> described above is deterministic, shaping engines may choose to
> implement the joining-state computation as a state machine, in a lookup
> table, or by any other means desirable.

At the end of this process, all letters should be tagged for possible
substitution by one of the `isol`, `init`, `medi`, `med2`, `fina`, `fin2`, or
`fin3` features.

### 4. Applying the `stch` feature ###

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
	

### 5. Applying the language-form substitution features from GSUB ###

The language-substitution phase applies mandatory substitution
features using the rules in the font's GSUB table. In preparation for
this stage, glyph sequences should be tagged for possible application 
of GSUB features.

The order in which these substitutions must be performed is fixed for
all scripts implemented with the Arabic shaping model:

	locl
	isol
	fina
	fin2 (only used in Syriac)
	fin3 (only used in Syriac)
	medi
	med2 (only used in Syriac)
	init
	rlig
	rclt
	calt

> Note: `rlig` and `calt` need to be appled to the word as a whole before
> continuing to the next feature.
	
See the individual script pages for further detail on each feature and
for script-specific information.


> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> GSUB substitutions in the following steps.


### 6. Applying the typographic-form substitution features from GSUB ###

The typographic-substitution phase applies optional substitution
features using the rules in the font's GSUB table.

The order in which these substitution must be performed is fixed for
all scripts implemented in the Arabic shaping model:

    liga
	dlig
	cswh
	mset
	
See the individual script pages for further detail on each feature and
for script-specific information.


### 7. Applying the positioning features from GPOS ###

The positioning stage adjusts the positions of mark and base
glyphs.

The order in which these features are applied is fixed for
all scripts implemented in the Arabic shaping model:

    curs
	kern
	mark
	mkmk


See the individual script pages for further detail on each feature and
for script-specific information.

