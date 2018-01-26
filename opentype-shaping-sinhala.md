# Sinhala shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Sinhala script.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Sinhala character tables](#sinhala-character-tables)
  - [The `<sinh>` shaping model](#the-dev2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)

## General information ##

The Sinhala script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the South Indic subgroup.

The Sinhala script is used to write multiple languages, most commonly
Sinhalese and Pali. In addition, Sanskrit may be written
in Sinhala, so Sinhala script runs may include glyphs from the Vedic
Extension block of Unicode. 

Unlike many other Indic scripts, there is only one extant Sinhala
script tag defined in OpenType, `<sinh>`.


## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. In the
Sinhalese language, this sign is known as the _al-lakuna_ or _hal kirīma_.

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel should be nasalized. 

The term **base consonant** is also critical to Indic shaping. The
base consonant of a syllable is the consonant that carries the
syllable's vowel sound, either the inherent vowel (for an unmarked
base consonant) or a dependent vowel (with the addition of a matra).

A syllable's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
syllable frequently take on secondary forms. Different GSUB
substitutions may apply to a script's **pre-base** and **post-base**
consonants. Some of these substitutions create **above-base** or
**below-base** forms. The **Reph** form of the consonant "Ra" is an
example. In the Sinhalese language, the Reph form is known as _repaya_.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Sinhala text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark.

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Sinhala glyphs must additionally be classified by how they are treated
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

Other characters, such as symbols and miscellaneous letters (for
example, letter-like symbols that only occur as standalone entities
and do not occur within syllables), need no special attention from the
shaping engine, so they are not assigned a shaping class.

Numbers are classified as `NUMBER`, even though they evoke no special
behavior from the Indic shaping rules, because there are OpenType features that
might affect how the respective glyphs are drawn, such as `tnum`,
which specifies the usage of tabular-width numerals, and `sups`, which
replaces the default glyphs with superscript variants.

Marks and dependent vowels are further labeled with a mark-placement
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

### Sinhala character tables ###

Separate character tables are provided for the Sinhala, Sinhala
Archaic Numbers, and Vedic Extensions block as well as for other
miscellaneous characters that are used in `<sinh>` text runs:

  - [Sinhala character table](character-tables/character-tables-sinhala.md#sinhala-character-table)
  - [Sinhala Archaic Numbers character table](character-tables/character-tables-sinhala.md#sinhala-archaic-numbers-character-table)
  - [Vedic Extensions character table](character-tables/character-tables-sinhala.md#vedic-extensions-character-table)
  - [Miscellaneous character table](character-tables/character-tables-sinhala.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0D82`   | Mark [Mn]        | BINDU             | RIGHT_POSITION             | &#x0D82; Anusvara            |
| | | | |
|`U+0D9A`   | Letter           | CONSONANT         | _null_                     | &#x0D9A; Ka                  |



Codepoints with no assigned meaning are designated as _unassigned_ in
the _Unicode category_ column.

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. 

The _Mark-placement subclass_ column indicates mark-placement
positioning for codepoints in the _Mark_ category. Assigned, non-mark
codepoints have a_null_ in this column and evoke no special
mark-placement behavior. Marks tagged with [Mn] in the _Unicode
category_ column are categorized as non-spacing; marks tagged with
[Mc] are categorized as spacing-combining.

Some codepoints in the tables use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.



Other important characters that may be encountered when shaping runs
of Sinhala text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

In other Indic scripts, the zero-width joiner is used to prevent the
formation of conjuncts and to suppress the formation of "Reph".

Sinhala, however, differs considerably in its use of "ZWJ".

  - In `<sinh>` text, "Reph" is only formed by the use of an explicit
    "Ra,Halant,ZWJ" sequence.
  - In `<sinh>` text, the sequence
    "Consonant_1,Halant,ZWJ,Consonant_2" is used to specify the
    subjoined form of "Consonant_2".
 
![](sinhala-reph.png)


The no-break space is primarily used to display those codepoints that
are defined as non-spacing (marks, dependent vowels (matras),
below-base consonant forms, and post-base consonant forms) in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder. These sequences will match
"NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".




## The `<sinh>` shaping model ##

Processing a run of `<sinh>` text involves six top-level stages:

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

With regard to these common variations, Sinhala's specific shaping
characteristics include: 

  - `BASE_POS_LAST_SINHALA` = The base consonant of a syllable is the last
     consonant, not counting any special final-consonant
     forms. However, the algorithm used for locating the base
     consonant in `<sinh>` text differs from that used by other
     `BASE_POS_LAST` scripts.

  - `REPH_POS_AFTER_MAIN` = "Reph" is ordered after the base consonant.

  - `REPH_MODE_EXPLICIT` = "Reph" is formed by an initial "Ra,Halant,ZWJ" sequence.

  - `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied both to
     pre-base consonants and to post-base consonants.

  - `MATRA_POS_TOP` = `POS_AFTER_SUBJOINED` = Above-base matras are
     ordered after subjoined (i.e., below-base) consonant forms. 

  - `MATRA_POS_RIGHT` = `POS_AFTER_SUBJOINED` = Right-side matras are
     ordered after subjoined (i.e., below-base) consonant forms. 

  - `MATRA_POS_BOTTOM` = `POS_AFTER_SUBJOINED` = Below-base matras are
     ordered after all subjoined (i.e., below-base) consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how "Reph"
should be encoded within a run of text.

### 1: Identifying syllables and other sequences ###

A syllable in Sinhala consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Sinhala Unicode block enumerates two modifier signs,
> "Anusvara" (`U+0D82`) and "Visarga" (`U+0D83`). In addition,
> Sanskrit text written in Sinhala may include additional signs from
> Vedic Extensions block. 

Each syllable contains exactly one vowel sound. Valid syllables may
begin with either a consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that vowel is the
syllable's only vowel sound and, by definition, there is no "base"
consonant. 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

Generally speaking, the base consonant is the final consonant of the
syllable that does not take on a subjoined form, and its vowel sound
designates the end of the syllable. This rule is synonymous with the
`BASE_POS_LAST_SINHALA` characteristic mentioned earlier. 

Valid consonant-based syllables may include one or more additional 
consonants that precede the base consonant. Each of these
other, pre-base consonants will be followed by the "Halant" mark, which
indicates that they carry no vowel. They affect pronunciation by
combining with the base consonant (e.g., "_str_", "_pl_") but they
do not add a vowel sound.

As with other Indic scripts, the consonant "Ra" receives special
treatment; in many circumstances it is replaced by a combining
mark-like form. 

  - A "Ra,Halant,ZWJ" sequence at the beginning of a syllable
    is replaced with an above-base mark called "Reph" (unless the "Ra"
    is the only consonant in the syllable). 
    This rule is synonymous with the `REPH_MODE_EXPLICIT`
    characteristic mentioned earlier.

In addition, the subjoined form of a post-base-consonant "Ra" can be
explicitly requested with a "Halant,ZWJ,Ra" sequence. This form is called
"Rakaaraansaya".

"Reph" characters must be reordered after the syllable-identification
stage is complete. "Rakaaraansaya" is not reordered.


In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Sinhala script, may
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
used to match Sinhala syllables. The regular expressions utilize the
shaping classifications from the tables above.


	C	  Consonant
	V	  Independent vowel
	N	  Nukta
	H	  Halant/Virama
	ZWNJ	  Zero-width non-joiner
	ZWJ	  Zero-width joiner
	M	  Matra (up to one of each type: pre-base, above-base, below-base, or post-base)
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
> "Ra,Halant,ZWJ" glyph sequences, and other consonants that take special
> treatment in some circumstances. "Ya" may take on special forms,
> depending on its position in the syllable. 
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
Sinhala. 

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
positioned immediately after the base consonant. `POS_BEFORE_SUBJOINED`
and `POS_AFTER_SUBJOINED` mean that a character must be positioned
before or after any below-base consonants, respectively. Similarly,
`POS_BEFORE_POST` and `POS_AFTER_POST` mean that a character must be
positioned before or after any post-base consonants, respectively. 

For shaping-engine implementers, the names used for the ordering
categories matter only in that they are unambiguous. 

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

Due to the different usage of ZWJ characters in `<sinh>` text runs, a
different algorithm is required for the shaper to identify the base
consonant of a syllable. The algorithm for determining the base
consonant in Sinhala is

  - If the syllable starts with "Ra,Halant,ZWJ" and the syllable contains
    more than one consonant, exclude the starting "Ra" from the list of
    consonants to be considered. 
  - Starting from the end of the syllable, move backwards until a consonant is found.
      * If the consonant is immediately preceded by a ZWJ, move to the
        previous consonant. If the consonant is not immediately
        preceded by a ZWJ, stop.
      * If the consonant is the first consonant, stop.
  - The consonant stopped at will be the base consonant.


> Note: Unlike with many other Indic scripts, it is not necessary for
> the shaping engine to independently determine if any consonant has a
> post-base or below-base form in the active font. The use of a ZWJ
> character before a consonant in the search explicitly designates
> such a special form.


#### 2.2: Matra decomposition ####

Second, any multi-part dependent vowels (matras) must be decomposed
into their individual components. 

Sinhala has four multi-part dependent vowels, "Ee" (`U+0DDA`), "O"
(`U+0DDC`), "Oo" (`U+0DDD`), and "Au" (`U+0DDE`). Each
has a canonical decomposition, so this step is unambiguous. 

> "Ee" (`U+0DDA`) decomposes to "`U+0DD9`,`U+0DCA`"
>
> "O" (`U+0DDC`)  decomposes to "`U+0DD9`,`U+0DCF`"
>
> "Oo" (`U+0DDD`) decomposes to "`U+0DD9`,`U+0DCF`, `U+0DCA`"
>
> "Au" (`U+0DDE`) decomposes to "`U+0DD9`,`U+0DDF`"

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.

> Note: The decomposition of "Oo" (`U+0DDD`) is atypical; Unicode
> specifies that the codepoint decomposes to "O" (`U+0DDC`) followed
> by `U+0DCA`; the "O" codepoint is then decomposed to
> "`U+0DD9`,`U+0DCF`". Shaping engines must take care not to miss this
> second decomposition.


#### 2.3: Tag matras ####

Third, all left-side dependent-vowel (matra) signs must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

Above-base, right-side, and below-base dependent-vowel (matra) signs
must be tagged with `POS_AFTER_SUBJOINED`.

#### 2.4: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. 

For `<sinh>` text, the canonical ordering means that any "Nukta"s must
be placed before all other marks. No other marks in the subsequence
should be reordered.

> Note: Nukta usage in Sinhala is rare.

#### 2.5: Pre-base consonants ####

Fifth, consonants that occur before the base consonant must be tagged
with `POS_PREBASE_CONSONANT`.

#### 2.6: Reph ####

Sixth, initial "Ra,Halant,ZWJ" sequences that will become "Reph"s must be tagged with
`POS_RA_TO_BECOME_REPH`.

> Note: an initial "Ra,Halant,ZWJ" sequence will always become a "Reph"
> unless the "Ra" is the only consonant in the syllable.

#### 2.7: Post-base consonants ####

Seventh, any non-base consonants that occur after a dependent vowel
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. 

In Sinhala, the only consonants that can appear in this position are
"Ra" and "Ya". A "Halant,ZWJ,Ya" sequence after the base consonant will take on
the "Yansaya" form when the `vatu` feature is applied. A
"Halant,ZWJ,Ra" sequence after the base consonant will take on 
the "Rakaaraansaya" form when the `vatu` feature is applied.

![Yansaya ligation](/images/sinhala/sinhala-vatu-va.png)

![Rakaaraansaya ligation](/images/sinhala/sinhala-vatu-ra.png)


#### 2.8: Mark tagging ####

Eighth, all marks must be tagged with the same positioning tag as the
closest non-mark character the mark has affinity with, so that they
move together during the sorting step.

For all marks preceding the base consonant, the mark must be tagged
with the same positioning tag as the closest preceding non-mark
consonant.

For all marks occurring after the base consonant, the mark must be
tagged with the same positioning tag as the closest subsequent consonant.

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.


With these steps completed, the syllable can be sorted into the final sort order.

### 3: Applying the basic substitution features from GSUB ###

The basic-substitution stage applies mandatory substitution features
using the rules in the font's GSUB table. In preparation for this
stage, glyph sequences should be tagged for possible application 
of GSUB features.

The order in which these substitutions must be performed is fixed for
all Indic scripts:

	locl
	nukt (not used in Sinhala)
	akhn
	rphf 
	rkrf (not used in Sinhala)
	pref (not used in Sinhala)
	blwf (not used in Sinhala)
	abvf (not used in Sinhala)
	half (not used in Sinhala)
	pstf
	vatu
	cjct (not used in Sinhala)
	cfar (not used in Sinhala)

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

> This feature is not used in Sinhala.


#### 3.3: akhn ####

In Sinhala, the `akhn` feature provides two substitution types.

  - "Consonant,Halant,ZWJ,Consonant" sequences are used to specify a ligature. 
  - "Consonant,ZWJ,Halant,Consonant" sequences are used to specify
    "touching consonant" substitutions used in Pali and Sanskrit. 
  

![Ligature substitution](/images/sinhala/sinhala-akhn-ligature.png)

![Touching consonant substitution](/images/sinhala/sinhala-akhn-touching.png)

#### 3.4: rphf ####

The `rphf` feature replaces initial "Ra,Halant,ZWJ" sequences with the
"Reph" glyph.
	

![Reph composition](/images/sinhala/sinhala-rphf.png)
	
#### 3.5 rkrf ####

> This feature is not used in Sinhala.


#### 3.6 pref ####

> This feature is not used in Sinhala.


#### 3.7: blwf ####

> This feature is not used in Sinhala.


#### 3.8: abvf ####

> This feature is not used in Sinhala.


#### 3.9: half ####

> This feature is not used in Sinhala.


#### 3.10: pstf ####

In Sinhala, the `pstf` feature replaces multi-part dependent vowels
(matras) with the right-side matra component of the canonical
decomposition.

> Note: shaping engines that decomposed multi-part dependent vowels in
> [stage 2, step 2](#22-matra-decomposition) will not need to perform
> this substitution.

![Post-base form substitution](/images/sinhala/sinhala-pstf.png)



#### 3.11: vatu ####

In Sinhala, the `vatu` feature replaces certain sequences with
ligatures using the subjoined forms of "Ra" or "Ya".

  - The sequence "Consonant,Halant,ZWJ,Ra" triggers the
    "Rakaaraansaya" form of the consonant.
  - The sequence "Consonant,Halant,ZWJ,Ya" triggers the "Yansaya" form
    of the consonant.
  

![Rakaaraansaya ligation](/images/sinhala/sinhala-vatu-ra.png)

![Yansaya ligation](/images/sinhala/sinhala-vatu-va.png)

#### 3.12: cjct ####

> This feature is not used in Sinhala.


#### 3.13: cfar ####

> This feature is not used in Sinhala.


### 4: Final reordering ###

The final reordering stage repositions marks, dependent-vowel (matra)
signs, and "Reph" glyphs to the appropriate location with respect to
the base consonant. Because multiple substitutions may have occurred
during the application of the basic-shaping features in the preceding
stage, these repositioning moves could not be performed during the
initial reordering stage.

Like the initial reordering stage, the steps involved in this stage
occur on a per-syllable basis.


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

![Pre-base matra positioning](/images/sinhala/sinhala-matra-position.png)

#### 4.3: Reph ####

"Reph" must be moved from the beginning of the syllable to its final
position. Because Sinhala incorporates the `REPH_POS_AFTER_MAIN`
shaping characteristic, this final position is immediately after the
base consonant.


![Reph positioning](/images/sinhala/sinhala-reph-position.png)

#### 4.4: Pre-base-reordering consonants ####

Any pre-base-reordering consonants must be moved to immediately before
the base consonant.

Sinhala does not use pre-base-reordering consonants, so this step will
involve no work when processing `<sinh>` text. It is included here in order
to maintain compatibility with the other Indic scripts.
  
  
#### 4.5: Initial matras ####

Any left-side dependent vowels (matras) that are at the start of a
word must be tagged for potential substitution by the `init` feature
of GSUB.

Sinhala does not use the `init` feature, so this step will
involve no work when processing `<sinh>` text. It is included here in order
to maintain compatibility with the other Indic scripts.
  
   
### 5: Applying all remaining substitution features from GSUB ###

In this stage, the remaining substitution features from the GSUB table
are applied. The order in which these features are applied is not
canonical; they should be applied in the order in which they appear in
the GSUB table in the font. 

	init (not used in Sinhala)
	pres
	abvs
	blws
	psts
	haln (not used in Sinhala)

The `init` feature is not used in Sinhala.

The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include ligatures, "touching consonant" forms,
and stylistic variants of left-side dependent vowels (matras). 

![Pre-base substitutions](/images/sinhala/sinhala-pres.png)

The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

![Above-base substitutions](/images/sinhala/sinhala-abvs.png)

The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually includes replacing base consonants
and attached below-base marks with contextual ligatures.

![Below-base substitutions](/images/sinhala/sinhala-blws.png)

The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
base-consonant/matra pairs with contextual ligatures. 

![Post-base substitutions](/images/sinhala/sinhala-psts.png)

The `haln` feature is not used in Sinhala.

> Note: The `calt` feature, which allows for generalized application
> of contextual alternate substitutions, is usually applied at this
> point. However, `calt` is not mandatory for correct Sinhala shaping
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
> mandatory for shaping Sinhala text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

The `abvm` feature positions above-base marks for attachment to base
characters. In Sinhala, this includes "Reph" in addition to
above-base dependent vowels (matras), diacritical marks, and Vedic signs. 

![Above-base mark positioning](/images/sinhala/sinhala-abvm.png)

The `blwm` feature positions below-base marks for attachment to base
characters. In Sinhala, this includes below-base dependent vowels
(matras) and diacritical marks.

![Below-base mark positioning](/images/sinhala/sinhala-blwm.png)


