# Malayalam shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Malayalam script.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Malayalam character tables](#malayalam-character-tables)
  - [The `<mlm2>` shaping model](#the-mlm2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The `<mlym>` shaping model](#the-mlym-shaping-model)
      - [Distinctions from `<mlm2>`](#distinctions-from-mlm2)
      - [Advice for handling fonts with `<mlym>` features only](#advice-for-handling-fonts-with-mlym-features-only)
      - [Advice for handling text runs composed in `<mlym>` format](#advice-for-handling-text-runs-composed-in-mlym-format)


## General information ##

The Malayalam script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the South Indic subgroup.

The Malayalam script is used to write multiple languages, most commonly
Malayalam and Paniya. In addition, Sanskrit may be written
in Malayalam, so Malayalam script runs may include glyphs from the Vedic
Extension block of Unicode. 

There are two extant Malayalam script tags defined in OpenType, `<mlym>`
and `<mlm2>`. The older script tag, `<mlym>`, was deprecated in 2005.
Therefore, new fonts should be engineered to work with the `<mlm2>`
shaping model. However, if a font is encountered that supports only
`<mlym>`, the shaping engine should deal with it gracefully.

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. 

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. In the Malayalam
language, this sign is known as the _chandrakkala_.

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel should be nasalized. In the Malayalam
language, this mark is known as the _candrabindu_.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Malayalam text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark. 

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Malayalam glyphs must additionally be classified by how they are treated
when shaping a run of text.

### Shaping classes and subclasses ###

The shaping classes listed in the tables that follow are defined so
that they capture the positioning rules used by Indic scripts. 

For most codepoints, the _Shaping class_ is synonymous with the `Indic
Syllabic Category` defined in Unicode. However, there are some
distinctions, where the defined category does not fully capture the
behavior of the character in the shaping process.

Several of the diacritic and syllable-modifying marks behave according
to their own rules and, thus, have a special class. These include
`BINDU`, `VISARGA`, `AVAGRAHA`, `NUKTA`, and `VIRAMA`. Some
less-common marks behave according to rules that are similar to these
common marks, and are therefore classified with the corresponding
common mark. The Vedic Extensions also include a `CANTILLATION`
class for tone marks.

Letters generally fall into the classes `CONSONANT`,
`VOWEL_INDEPENDENT`, and `VOWEL_DEPENDENT`. These classes help the
shaping engine parse and identify key positions in a syllable. For
example, Unicode categorizes dependent vowels as `Mark [Mn]`, but the
shaping engine must be able to distinguish between dependent vowels
and diacritical marks (which are categorized as `Mark [Mn]`).

Malayalam uses two sublcasses of consonant, `CONSONANT_DEAD` and
`CONSONANT_PRE_REPHA`. 

The `CONSONANT_DEAD` subclass is used for the Malayalam _chillu_
variants of certain consonants. It indicates that the characters
should match tests for consonants, such as when [identifying 
syllables](#1-identifying-syllables-and-other-sequences), but that, unlike
standard consonants, they carry no inherent vowel. The lack of an
inherent vowel is important during the [initial
reordering](#2-initial-reordering) stage.

The `CONSONANT_PRE_REPHA` subclass is used only for the "Dot Reph"
(`U+0D4E`), a dead-consonant version of "Reph" (or "Repha"). In modern
Malayalam orthography, "Dot Reph" is uncommon. As with
`CONSONANT_DEAD`, this subclass should match tests for
consonants. Because the "Dot Reph" character is a "Reph", however, it
must be treated as a "Reph" during the initial and final reordering stages.

Other characters, such as symbols and miscellaneous letters (for
example, letter-like symbols that only occur as standalone entities
and do not occur within syllables), need no special attention from the
shaping engine, so they are not assigned a shaping class.

Numbers are classified as `NUMBER`, even though they evoke no special
behavior from the Indic shaping rules, because there are OpenType features that
might affect how the respective glyphs are drawn, such as `tnum`,
which specifies the usage of tabular-width numerals, and `sups`, which
replaces the default glyphs with superscript variants.

Marks and dependent vowels are further labelled with a mark-placement
subclass, which indicates where the glyph will be placed with respect
to the base character to which it is attached. The actual position of
the glyphs is determined by the lookups found in the font's GPOS
table, however, the shaping rules for Indic scripts require that the
shaping engine be able to identify marks by their general
position. 

For example, left-side dependent vowels (matras), classified
with `LEFT_POSITION`, must frequently be reordered, with the final
position determined by whether or not other letters in the syllable
have formed ligatures or combined into conjunct forms. Therefore, the
`LEFT_POSITION` subclass of the character must be tracked throughout
the shaping process.

For most mark and dependent-vowel codepoints, the _Mark-placement
subclass_ is synonymous with the `Indic Positional Category` defined
in Unicode. However, there are some distinctions, where the defined
category does not fully capture the behavior of the character in the
shaping process. 

Malayalam includes two special marks that are classified as
`PURE_KILLER`, "Vertical Bar Virama" (`U+0D3B`) and "Circular Virama"
(`U+0D3C`). These marks, like the Virama or "Halant", suppress the
inherent vowel of a consonant. However, unlike "Halant", the use of a
`PURE_KILLER` prevents the formation of ligatures and conjuncts, and
the mark itself is always rendered explicitly. 

Consequently, these marks behave like dependent-vowel marks
(matras). Shaping engines may choose to treat them as matras for simplicity.

### Malayalam character tables ###

Separate character tables are provided for the Malayalam and Vedic
Extensions blocks as well as for other miscellaneous characters that
are used in `<mlm2>` text runs:

  - [Malayalam character table](character-tables/character-tables-malayalam.md#malayalam-character-table)
  - [Vedic Extensions character table](character-tables/character-tables-malayalam.md#vedic-extensions-character-table)
  - [Miscellaneous character table](character-tables/character-tables-malayalam.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0D01`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0D01; Candrabindu         |
| | | | |
|`U+0D15`   | Letter           | CONSONANT         | _null_                     | &#x0D15; Ka                  |


Codepoints with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine.

The _Mark-placement subclass_ column indicates mark-placement
positioning for codepoints in the _Mark_ category. Assigned, non-mark
codepoints have a _null_ in this column and evoke no special
mark-placement behavior. Marks tagged with [Mn] in the _Unicode
category_ column are categorized as non-spacing; marks tagged with
[Mc] are categorized as spacing-combining.

Some codepoints in the tables use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.


Other important characters that may be encountered when shaping runs
of Malayalam text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

The zero-width joiner is primarily used to prevent the formation of a conjunct
from a "_Consonant_,Halant,_Consonant_" sequence. The sequence
"_Consonant_,Halant,ZWJ,_Consonant_" blocks the formation of a
conjunct between the two consonants. 

Note, however, that the "_Consonant_,Halant" subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner must be used instead. The sequence
"_Consonant_,Halant,ZWNJ,_Consonant_" should produce the first
consonant in its standard form, followed by an explicit "Halant".

A secondary usage of the zero-width joiner is to prevent the formation of
"Reph". An initial "Ra,Halant,ZWJ" sequence should not produce a "Reph",
where an initial "Ra,Halant" sequence without the zero-width joiner
otherwise would.

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (marks, dependent vowels (matras),
below-base consonant forms, and post-base consonant forms) in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder. These sequences will match
"NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".

In addition to general punctuation, runs of Malayalam text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.



## The `<mlm2>` shaping model ##

Processing a run of `<mlm2>` text involves six top-level stages:

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying all remaining positioning features from GPOS


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve applying a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

Indic scripts follow many of the same shaping patterns, but they
differ in a few critical characteristics that the shaping engine must
track. These include:

  - The position of the base consonant in a syllable.
  
  - The final position of "Reph".
  
  - Whether "Reph" must be requested explicitly or if it is formed by
    a specific, implicit sequence.
	
  - Whether the below-base forms feature is applied only to consonants
    before the base consonant, only to consonants after the base
    consonant, or to both.
	
  - The ordering positions for dependent vowels
    (matras). Specifically, right-side, above-base, and below-base
    matras follow different rules in different scripts. 
	All Indic scripts position left-side matras in the same
    manner, in the ordering position `POS_PREBASE_MATRA`. 

With regard to these common variations, Malayalam's specific shaping
characteristics include:

  - `BASE_POS_LAST` = The base consonant of a syllable is the last
     consonant, not counting any special final-consonant forms.

  - `REPH_POS_AFTER_MAIN` = "Reph" is ordered after the base consonant.

  - `REPH_MODE_LOGICAL_REPHA` = "Reph" is encoded as its own Unicode
     codepoint ("Repha"), but it must still be reordered. Note that
     Malayalam text can also use the "Ra,Halant" sequence to invoke an
     implicit "Reph".

  - `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied both to
     pre-base consonants and to post-base consonants.

  - `MATRA_POS_TOP` = _null_  = Unlike most other Indic scripts, Malayalam
     does not use any above-base matras. Therefore, this shaping
     characteristic does not apply.

  - `MATRA_POS_RIGHT` = `POS_AFTER_POST` = Right-side matras are
     ordered after all post-base consonant forms.

  - `MATRA_POS_BOTTOM` = `POS_AFTER_POST` = Below-base matras are
     ordered after all post-base consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how "Reph"
should be encoded within a run of text.

> Note: Unlike most other Indic scripts, Malayalam does not use
> above-base matras. Therefore `MATRA_POS_TOP` can be set to _null_.

### 1: Identifying syllables and other sequences ###

A syllable in Malayalam consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Malayalam Unicode block enumerates five modifier signs,
> "Combining Anusvara Above" (`U+0D00`), "Candrabindu" (`U+0D01`),
> "Anusvara" (`U+0D02`), "Visarga" (`U+0D03`), and "Avagraha"
> (`U+0D3D`). In addition, Sanskrit text written in Malayalam may 
> include additional signs from Vedic Extensions block.

Each syllable contains exactly one vowel sound. Valid syllables may
begin with either consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that vowel is the
syllable's only vowel sound and, by definition, there is no "base"
consonant. 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

Generally speaking, the base consonant is the final consonant of the
syllable and its vowel sound designates the end of the syllable. This
rule is synonymous with the `BASE_POS_LAST` characteristic mentioned
earlier. 

Valid consonant-based syllables may include one or more additional 
consonants that precede the base consonant. Each of these
other, pre-base consonants will be followed by the "Halant" mark, which
indicates that they carry no vowel. They affect pronunciation by
combining with the base consonant (e.g., "_str_", "_pl_") but they
do not add a vowel sound.

Malayalam includes three consonants that can occur after the
base consonant: "Ya", "Va", and "Ra". Malayalam also includes one
consonant that can take on a below-base form, "La". 

When taking on post-base or below-base form, these consonants will
be separated from the base consonant by a "Halant" mark; the algorithm
for correctly identifying the base consonant includes a test to
recognize these sequences and not mis-identify the base consonant.

As with other Indic scripts, the consonant "Ra" receives special
treatment; in many circumstances it is replaced by a combining
mark-like form. 

  - A "Ra,Halant" sequence at the beginning of a syllable is replaced
    with an above-base mark called "Reph" (unless the "Ra" is the only
    consonant in the syllable). This rule is synonymous with the
    `REPH_MODE_IMPLICIT` characteristic mentioned earlier.
  
Malayalam text runs may also include the explicit variant of "Reph",
the "Dot Reph" (`U+0D4E`), also known as "Repha".
  
"Reph" and "Repha" characters must be reordered after the
syllable-identification stage is complete. 



In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Malayalam script, may
> not adhere to the syllable-formation rules described above. In
> particular, it is not uncommon to encounter foreign loanwords that
> contain a word-final suffix of consonants.
>
> Nevertheless, such word-final suffixes will be correctly matched by
> the regular expressions listed below. These loanwords are pronounced
> different, which raises issues for potential readers, but the
> character sequences do not affect the shaping process.



Syllables should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 

The following general-purpose Indic-shaping regular expressions can be
used to match Malayalam syllables. The regular expressions utilize the
shaping classifications from the tables above.


> Note: Malayalam does not include the Anudatta (`U+0952`). It is
> included in the following expressions in order to correctly match other Indic scripts.

	C	  Consonant
	V	  Independent vowel
	N	  Nukta
	H	  Halant/Virama
	ZWNJ	  Zero-width non-joiner
	ZWJ	  Zero-width joiner
	M	  Matra (up to one of each type: pre-base, below-base, or post-base)
	SM	  Syllable modifier signs
	VD	  Vedic signs
	A	  Anudatta
	NBSP	  No-break space
	      
	{ }	  zero or more occurences of the enclosed expression
	[ ]	  optional occurence of the enclosed expression
	<|>	  one of the options separated by the vertical bar
	( )	  one or two occurences of the enclosed expression

A consonant-based syllable will match the expression:
```
{C+[N]+<H+[<ZWNJ|ZWJ>]|<ZWNJ|ZWJ>+H>} + C+[N]+[A] + [< H+[<ZWNJ|ZWJ>] | {M}+[N]+[H]>]+[SM]+[(VD)]
```

A vowel-based syllable will match the expression:
```
[Ra+H]+V+[N]+[<[<ZWJ|ZWNJ>]+H+C|ZWJ+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A stand-alone sequence (which can only occur at the start of a word) will match the expression:
```
[Ra+H]+NBSP+[N]+[<[<ZWJ|ZWNJ>]+H+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A sequence that does not match any of these expressions should be
regarded as broken. The shaping engine may make a best-effort attempt
to shape the broken sequence, but making guarantees about the
correctness or appearance of the final result is out of scope for this
document.

After the syllables have been identified, each of the subsequent 
shaping stages occurs on a per-syllable basis.

### 2: Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text to the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs, 
> "Ra,Halant" glyph sequences, and other consonants that take special
> treatment in some circumstances. "Ra", "Va", "La", and "Ya" occasionally
> take on special forms, depending on their position in the syllable.
>
> These reordering moves are mandatory. The final-reordering stage
> may make additional moves, depending on the text and on the features
> implemented in the active font.

The syllable should be processed by tagging each glyph with its
intended position based on its ordering category. After all glyphs
have been tagged, the entire syllable should be sorted in stable order,
so that glyphs of the same ordering category remain in the same
relative position with respect to each other.

The final sort order of the ordering categories should be:


	POS_RA_TO_BECOME_REPH
	POS_PREBASE_MATRA
	POS_PREBASE_CONSONANT

	POS_BASE_CONSONANT
	POS_AFTER_MAIN

	POS_ABOVEBASE_CONSONANT

	POS_BEFORE_SUBJOINED
	POS_BELOWBASE_CONSONANT
	POS_AFTER_SUBJOINED

	POS_BEFORE_POST
	POS_POSTBASE_CONSONANT
	POS_AFTER_POST

	POS_FINAL_CONSONANT
	POS_SMVD


This sort order enumerates all of the possible final positions to
which a codepoint might be reordered, across all of the Indic
scripts. It includes some ordering categories not utilized in
Malayalam. 

The basic positions (left to right) are "Reph" (`POS_RA_TO_BECOME_REPH`), dependent
vowels (matras) and consonants positioned before the base
consonant (`POS_PREBASE_MATRA` and `POS_PREBASE_CONSONANT`), the base
consonant (`POS_BASE_CONSONANT`), above-base consonants
(`POS_ABOVEBASE_CONSONANT`), below-base consonants
(`POS_BELOWBASE_CONSONANT`), consonants positioned after the base consonant
(`POS_POSTBASE_CONSONANT`), syllable-final consonants (`POS_FINAL_CONSONANT`),
and syllable-modifying or Vedic signs (`POS_SMVD`).

In addition, several secondary positions are defined to handle various
reordering rules that deal with relative, rather than absolute,
positioning. `POS_AFTER_MAIN` means that a character must be
positioned immedately after the base consonant. `POS_BEFORE_SUBJOINED`
and `POS_AFTER_SUBJOINED` mean that a character must be positioned
before or after any below-base consonants, respectively. Similarly,
`POS_BEFORE_POST` and `POS_AFTER_POST` mean that a character must be
positioned before or after any post-base consonants, respectively. 

For shaping-engine implementers, the names used for the ordering
categories matter only in that they are unabiguous. 

For a definition of the "base" consonant, refer to step 2.1, which follows.

#### 2.1: Base consonant ####

The first step is to determine the base consonant of the syllable, if
there is one, and tag it as `POS_BASE_CONSONANT`.

The base consonant is defined as the consonant in a consonant-based
syllable that carries the syllable's vowel sound. That vowel sound
will either be provided by the script's inherent vowel (in which case
it is not written with a separate character) or the sound will be designated
by the addition of a dependent-vowel (matra) sign.

Vowel-based syllables, standalone-sequences, and broken text runs will
not have base consonants.

The algorithm for determining the base consonant is

  - If the syllable starts with "Ra,Halant" and the syllable contains
    more than one consonant, exclude the starting "Ra" from the list of
    consonants to be considered. 
  - Starting from the end of the syllable, move backwards until a consonant is found.
      * If the consonant has a below-base or post-base form or is a
        pre-base reordering "Ra", move to the previous consonant. If
        neither condition is true, stop. 
      * If the consonant is the first consonant, stop.
  - The consonant stopped at will be the base consonant.

Shaping engines may choose any method to identify consonants that have
below-base or post-base forms while executing the above algorithm. For
example, one implementation may choose to maintain a static table of
below-base and post-base consonants to compare again the text
run. Another implementation might examine the active font to see if it
includes a relevant `blwf` or `pstf` lookup in the GSUB table.

> Note: The algorithm is designed to work for all Indic
> scripts. However, Malayalam does not utilize pre-base reordering "Ra".


#### 2.2: Matra decomposition ####

Second, any two-part dependent vowels (matras) must be decomposed
into their left-side and right-side components. Malayalam has three
two-part dependent vowels, "O" (`U+0D4A`), "Oo" (`U+0D4B`), and "Au"
(`U+0D4C`). Each has a canonical decomposition, so this step is
unambiguous. 

> "O" (`U+0D4A`) decomposes to "`U+0D46`,`U+0D3E`"
>
> "Oo" (`U+0D4B`) decomposes to "`U+0D47`,`U+0D3E`"
>
> "Au" (`U+0D4C`) decomposes to "`U+0D46`,`U+0D57`"

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.

![Two-part matra decomposition](/images/malayalam/split-matra-decomposition.png)

#### 2.3: Tag matras ####

Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

All right-side dependent-vowel (matra) signs are tagged
`POS_AFTER_POST`.

All below-base dependent-vowel (matra) signs are tagged
`POS_AFTER_POST`.

For simplicity, shaping engines may choose to tag single-part matras
in an earlier text-processing step, using the information in the
_Mark-placement subclass_ column of the character tables. It is
critical at this step, however, that all decomposed matras are also
correctly tagged before proceeding to the next step.

#### 2.4: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. 

For `<mlm2>` text, the canonical ordering means that any "Nukta"s must
be placed before all other marks. No other marks in the subsequence
should be reordered.

#### 2.5: Pre-base consonants ####

Fifth, consonants that occur before the base consonant must be tagged
with `POS_PREBASE_CONSONANT`.

#### 2.6: Reph ####

Sixth, initial "Ra,Halant" sequences that will become "Reph"s must be tagged with
`POS_RA_TO_BECOME_REPH`.

> Note: an initial "Ra,Halant" sequence will always become a "Reph"
> unless the "Ra" is the only consonant in the syllable.

#### 2.7: Post-base consonants ####

Seventh, any non-base consonants that occur after a dependent vowel
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. Such
consonants will usually be preceded by a "Halant" glyph, with the
exception of two special-case consonants. 

  - "Khanda Ta" (`U+09CE`) is a "dead" consonant variant of "Ta",
    meaning that it carries no inherent vowel, therefore no "Halant"
    follows it.
  - The sequence "Halant,Ya" (`U+09CD`,`U+09AF`)  triggers
    the "Yaphala" form. "Yaphala" behaves like a modifier to the
    pronunciation of the preceding vowel, despite the fact that it is
    formed from a consonant. Because the "Halant" precedes the
    consonant when forming the "Yaphala", no "Halant" follows it.

	
#### 2.8: Mark tagging ####

Eighth, all marks must be tagged with the same positioning tag as the
closest non-mark character the mark has affinity with, so that they move together
during the sorting step.

For all marks preceding the base consonant, the mark must be tagged
with the same positioning tag as the closest preceding non-mark
consonant.

For all marks occuring after the base consonant, the mark must be
tagged with the same positioning tag as the closest subsequent consonant.

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.

<!--- EXCEPTION: Uniscribe does NOT move a halant with a preceding -->
<!--left-matra. HarfBuzz follows suit, for compatibility reasons. --->

<!--- HarfBuzz also tags everything between a post-base consonant or -->
<!--matra and another post-base consonant as belonging to the latter -->
<!--post-base consonant. --->


<!--- 2.9: Ninth, all post-base glyphs should be merged into a single
   substring that will sort as a single unit. --->
   
<!--- Unsure. This occurs after the stable sort. What happens is that -->
<!--HB looks at every glyph between the base consonant and the end, -->
<!--looking for a 'max' value, then merges everything between the base -->
<!--and the max. --->

<!--- Merging all post-base stuff into one unit is old-spec -->
<!--behavior. --->

With these steps completed, the syllable can be sorted into the final sort order.

### 3: Applying the basic substitution features from GSUB ###

The basic-substitution stage applies mandatory substitution features
using the rules in the font's GSUB table. In preparation for this
stage, glyph sequences should be tagged for possible application 
of GSUB features.

The order in which these substitutions must be performed is fixed for
all Indic scripts:

	locl
	nukt
	akhn
	rphf 
	rkrf (not used in Malayalam)
	pref (not used in Malayalam)
	blwf 
	abvf (not used in Malayalam)
	half
	pstf
	vatu
	cjct
	cfar (not used in Malayalam)

#### 3.1 locl ####

The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> GSUB substitutions in the following steps.

#### 3.2: nukt ####

The `nukt` feature replaces "_Consonant_,Nukta" sequences with a
precomposed nukta-variant of the consonant glyph. 


![Nukta composition](/images/malayalam/nukta-composition.png)

#### 3.3: akhn ####

The `akhn` feature replaces two specific sequences with required ligatures. 

  - "Ka,Halant,Ssa" is substituted with the "KSsa" ligature. 
  - "Ja,Halant,Nya" is substituted with the "JNya" ligature. 
  
These sequences can occur anywhere in a syllable. The "KSsa" and
"JNya" characters have orthographic status equivalent to full
consonants in some languages, and fonts may have `cjct` substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.

![KSsa ligation](/images/malayalam/kassa-ligation.png)

![JNya ligation](/images/malayalam/janya-ligation.png)

#### 3.4: rphf ####

The `rphf` feature replaces initial "Ra,Halant" sequences with the
"Reph" glyph.

  - An initial "Ra,Halant,ZWJ" sequence, however, must not be tagged for
    the `rphf` substitution.
	

![Reph composition](/images/malayalam/reph-composition.png)

#### 3.5: rkrf ####

> This feature is not used in Malayalam.

#### 3.6 pref ####

> This feature is not used in Malayalam.

<!--- 3.5: The `pref` feature replaces pre-base-consonant glyphs with -->
<!--any special forms. --->

#### 3.7: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Malayalam includes two below-base consonant
forms:

  - "Ra,Halant" in a non-syllable-initial position takes on the
    "Raphala" form.
  - "Ba,Halant" takes on the "Baphala" form. 

Because Malayalam incorporates the `BLWF_MODE_PRE_AND_POST` shaping
characteristic, any pre-base consonants and any post-base consonants
may potentially match a `blwf` substitution; therefore, both cases must
be tagged for comparison. Note that this is not necessarily the case in other
Indic scripts that use a different `BLWF_MODE_` shaping
characteristic. 


![Raphala composition](/images/malayalam/raphala-composition.png)

![Baphala composition](/images/malayalam/baphala-composition.png)

#### 3.8: abvf ####

> This feature is not used in Malayalam.

#### 3.9: half ####

The `half` feature replaces "_Consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs. There are
three exceptions to the default behavior, for which the shaping engine
must test:

  - Initial "Ra,Halant" sequences, which should have been tagged for
    the `rphf` feature earlier, must not be tagged for potential
    `half` substitutions.

  - A sequence matching "_Consonant_,Halant,ZWJ,_Consonant_" must be
    tagged for potential `half` substitutions, even though the presence of the
    zero-width joiner suppresses the `cjct` feature in a later step.

  - A sequence matching "_Consonant_,Halant,ZWNJ,_Consonant_" must not be
    tagged for potential `half` substitutions.


![Half-form formation](/images/malayalam/half-formation.png)

#### 3.10: pstf ####

The `pstf` feature replaces post-base-consonant glyphs with any special forms.


![Yaphala composition](/images/malayalam/yaphala-composition.png)

#### 3.11: vatu ####

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. 

"Vattu variants" are formed from glyphs followed by "Raphala"
(the below-base form of "Ra"); therefore, this feature must be applied after
the `blwf` feature.


![Vattu variant ligation](/images/malayalam/vattu-ligation.png)

#### 3.12: cjct ####

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match "_Consonant_,Halant,_Consonant_".

A sequence matching "_Consonant_,Halant,ZWJ,_Consonant_" or
"_Consonant_,Halant,ZWNJ,_Consonant_" must not be tagged to form a conjunct.

The font's GSUB rules might be implemented so that `cjct`
substitutions apply to half-form consonants; therefore, this feature
must be applied after the `half` feature. 


![Conjunct ligation](/images/malayalam/pata-conjunct.png)

#### 3.13: cfar ####

> This feature is not used in Malayalam.


### 4: Final reordering ###

The final reordering stage repositions marks, dependent-vowel (matra)
signs, and "Reph" glyphs to the appropriate location with respect to
the base consonant. Because multiple substitutions may have occurred
during the application of the basic-shaping features in the preceding
stage, these repositioning moves could not be performed during the
initial reordering stage.

Like the initial reordering stage, the steps involved in this stage
occur on a per-syllable basis.

<!--- Check that classifications have not been mangled. If the -->
<!--character is a Halant AND a ligature was formed AND a multiple
substitution was performed, restore the classification to VIRAMA
because it was almost certainly lost in the preceding GSUB stage.
--->

#### 4.1: Base consonant ####

The final reordering stage, like the initial reordering stage, begins
with determining the base consonant of each syllable, following the
same algorithm used in stage 2, step 1.

The codepoint of the underlying base consonant will not change between
the search performed in stage 2, step 1, and the search repeated
here. However, the application of GSUB shaping features in stage 3
means that several ligation and many-to-one substitutions may have
taken place. The final glyph produced by that process may, therefore,
be a conjunct or ligature form — in most cases, such a glyph will not
have an assigned Unicode codepoint.
   
#### 4.2: Pre-base matras ####

Pre-base dependent vowels (matras) that were reordered during the
initial reordering stage must be moved to their final position. This
position is defined as:
   
   - after the last standalone "Halant" glyph that comes after the
     matra's starting position and also comes before the main
     consonant.
   - If a zero-width joiner or a zero-width non-joiner follows this
     last standalone "Halant", the final matra position is moved to
     after the joiner or non-joiner.

This means that the matra will move to the right of all explicit
"consonant,Halant" subsequences, but will stop to the left of the base
consonant, all conjuncts or ligatures that contains the base
consonant, and all half forms.

#### 4.3: Reph ####

"Reph" must be moved from the beginning of the syllable to its final
position. Because Malayalam incorporates the `REPH_POS_AFTER_SUBJOINED`
shaping characteristic, this final position is immediately after the
base consonant and any subjoined (below-base consonant or below-base
dependent vowel) forms.

  - If the syllable does not have a base consonant (such as a syllable
    based on an independent vowel), then the final "Reph" position is
    immediately before the first character tagged with the
    `POS_BEFORE_POST` position or any later position in the sort
    order.

    -- If there are no characters tagged with `POS_BEFORE_POST` or
       later positions, then "Reph" is positioned at the end of the
       syllable.

Finally, if the final position of "Reph" occurs after a
"_matra_,Halant" subsequence, then "Reph" must be repositioned to the
left of "Halant", to allow for potential matching with `abvs` or
`psts` substitutions from GSUB.

#### 4.4: Pre-base consonants ####

Any pre-base reordering consonants must be moved to immediately before
the base consonant.
  
Malayalam does not use pre-base reordering consonants, so this step will
involve no work when processing `<mlm2>` text. It is included here in order
to maintain compatibility with the other Indic scripts.

<!---  *** Malayalam does not use pre-base reordering consonants *** *** This
  feature is exhibited by Javanese and Balinese. Possibly *** by
  Devanagari as well....  --->

#### 4.5: Initial matras ####

Any left-side dependent vowels (matras) that are at the start of a
word must be tagged for potential substitution by the `init` feature
of GSUB.

### 5: Applying all remaining substitution features from GSUB ###

In this stage, the remaining substitution features from the GSUB table
are applied. The order in which these features are applied is not
canonical; they should be applied in the order in which they appear in
the GSUB table in the font. 

	init
	pres
	abvs
	blws
	psts
	haln

The `init` feature replaces word-initial glyphs with special
presentation forms. Generally, these forms involve removing the
headline instroke from the left side of the glyph.

The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include consonant conjuncts, half-form
consonants, and stylistic variants of left-side dependent vowels
(matras). 

The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually includes replacing base consonants that
are adjacent to below-base-consonant forms like "Raphala" or
"Baphala" with contextual ligatures.

The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures. 

The `haln` feature replaces syllable-final "_Consonant_,Halant" pairs with
special presentation forms. This can include stylistic variants of the
consonant where placing the "Halant" mark on its own is
typographically problematic. 

> Note: The `calt` feature, which allows for generalized application
> of contextual alternate substitutions, is usually applied at this
> point. However, `calt` is not mandatory for correct Malayalam shaping
> and may be disabled in the application by user preference.

### 6: Applying remaining positioning features from GPOS ###

In this stage, mark positioning, kerning, and other GPOS features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the GPOS table in the font.

        dist
        abvm
        blwm

> Note: The `kern` feature is usually applied at this stage, if it is
> present in the font. However, `kern` (like `calt`, above) is not
> mandatory for shaping Malayalam text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

The `abvm` feature positions above-base marks for attachment to base
characters. In Malayalam, this includes "Reph" in addition to the
diacritical marks and Vedic signs. 

The `blwm` feature positions below-base marks for attachment to base
characters. In Malayalam, this includes below-base dependent vowels
(matras) as well as the below-base consonant forms "Raphala" and
"Baphala".


## The `<mlym>` shaping model ##

The older Malayalam script tag, `<mlym>`, has been deprecated. However,
shaping engines may still encounter fonts that were built to work with
`<mlym>` and some users may still have documents that were written to
take advantage of `<mlym>` shaping.

### Distinctions from `<mlm2>` ###

The most significant distinction between the shaping models is that the
sequence of "Halant" and consonant glyphs required to suppress the
inherent vowel (and, for the shaping engine's purposes, to trigger shaping
features) was swapped when migrating from `<mlym>` to
`<mlm2>`. 

Specifically, the inherent vowel of a consonant in a run of `<mlym>`
text was suppressed by the sequence "Halant,_Consonant_". In `<mlm2>`
text, as described above in this document, the correct sequence is
"_Consonant_,Halant".

Consequently, in `<mlym>` text, a "Reph" substitution was triggered by a
syllable-initial "Halant,Ra" sequence. In `<mlm2>` text, the sequence
must be "Ra,Halant". 

Similarly, in `<mlym>` text, a pre-base half-form or
consonant-conjunct substitution was triggered by
"Halant,_Consonant_,_Consonant_". In `<mlm2>` text, the sequence must
be "_Consonant_,Halant,_Consonant_".

### Advice for handling fonts with `<mlym>` features only ###

Shaping engines may choose to match "Halant,_Consonant_" sequences in
order to apply GSUB substitutions when it is known that the font in
use supports only the `<mlym>` shaping model.

### Advice for handling text runs composed in `<mlym>` format ###

Shaping engines may choose to match "Halant,_Consonant_" sequences for
GSUB substitutions or to reorder them to "_Consonant_,Halant" when
processing text runs that are tagged with the `<mlym>` script tag and
it is known that the font in use supports only the `<mlm2>` shaping
model.
