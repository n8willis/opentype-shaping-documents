# Indic script shaping in OpenType #

This document outlines the general shaping procedure shared by all
Indic scripts, and defines the common pieces that script-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes](#shaping-classes)
	  - [Mark-placement subclasses](#mark-placement-subclasses)
      - [Character tables](#character-tables)
  - [The Indic2 shaping model](#the-indic2-shaping-model)
      - [Sort ordering](#sort-ordering)
      - [Script shaping characteristics](#script-shaping-characteristics)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The old Indic shaping model](#the-old-indic-shaping-model)


## General information ##

The Indic family of scripts includes writing systems
derived from the Bhrami script in ancient India. Although the scripts
vary considerably in appearance, their shared ancestry means that they
also share a number of important features and rules. 

This makes it possible (though, of course, not mandatory) for a
shaping engine to implement a single shaping model that covers all of
the scripts. 

The largest (by number of readers) scripts in the Indic family are:

  - Devanagari
  - Bengali
  - Gujarati
  - Gurmukhi
  - Kannada
  - Malayalam
  - Oriya
  - Tamil
  - Telugu
  - Sinhala
  - Khmer

Text runs in Indic scripts may also include characters from the Vedic
Extensions block in Unicode. This is a set of marks and punctuation
needed to accurately transcribe ancient documents in Sanskrit.

Text runs in Indic scripts also make use of joiner, non-joiner, and
placeholder characters from other Unicode blocks, in order to specify
certain alternate shaping options.

There are two sets of Indic script tags defined in OpenType. The older
set (including `<deva>`, `<beng>`, and `<mlym>` among others) was
deprecated in 2005. 

The new set (including `<dev2>`, `<bng2>`, and `<mlm2>`) was devised
to overcome shortcomings found in the original model. 
Therefore, new fonts should be engineered to work with the 
shaping model. However, if a font is encountered that supports only
an older script tag, the shaping engine should deal with it gracefully.

> Note: There are several other scripts derived from the Bhrami script
> that are often treated separately and not bundled into the "Indic"
> category by shaping engines. This is because these other scripts
> evolved to have significantly distinct rules for syllable
> construction, reordering, and shaping.
>
> The scripts include Buginese, Balinese, Javanese, Lao, Myanmar,
> Thai, and Tibetan.

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. 

The term "matra" is also used to refer to the headline above letters
in scripts like Devanagari, Bengali, and Gurmukhi. To avoid ambiguity,
the term **headline** is used in most Unicode and OpenType shaping
documents.

**Halant** and **Virama** are both standard terms for the below-base
"vowel-killer" sign. Unicode documents use the term "virama" most
frequently, while OpenType documents use the term "halant" most
frequently.

**Chandrabindu** (or simply **Bindu**) is the standard term for the
diacritical mark indicating that the preceding vowel should be
nasalized. 

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.


## Glyph classification ##

Shaping Indic text depends on the shaping engine correctly classifying
each glyph in the run. The classifications must distinguish between
consonants, vowels (independent and dependent), numerals, punctuation,
and various types of diacritical mark. 

For most codepoints, the `General Category` property defined in the
Unicode standard is correct, but it is not sufficient to fully capture
the expected shaping behavior (such as glyph reordering). Therefore,
Bengali glyphs must additionally be classified by how they are treated
when shaping a run of text.

### Shaping classes ###

The shaping classes listed in the tables that follow are defined so
that they capture the positioning rules used by Indic scripts. 

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

There are occasional special classes in use, such as
`CONSONANT_DEAD`, which indicates that a letter should match simple
tests for consonants, but that, unlike standard consonants, it carries
no inherent vowel. This lack of an inherent vowel means that the
letter is likely not accompanied by a `VIRAMA`; failure to recognize
this distinction could trick naive parsers into mis-identifying the
letter as the base consonant of a syllable.

Other characters, such as symbols and miscellaneous letters (for
example, letter-like symbols that only occur as standalone entities
and do not occur within syllables), need no special attention from the
shaping engine, so they are not assigned a shaping class.

Numbers are classified as `NUMBER`, even though they evoke no special
behavior from the Indic shaping rules, because there are OpenType
features that might affect how the respective glyphs are drawn, such
as `tnum`, which specifies the usage of tabular-width numerals, and
`sups`, which replaces the default glyphs with superscript variants.

### Mark-placement subclasses ###

Marks and dependent vowels are further labelled with a mark-placement
subclass, which indicates where the glyph will be placed with respect
to the base character to which it is attached. 

The actual attachment position of these glyphs is determined by the
lookups found in the font's GPOS table. However, the reordering rules for
Indic scripts require that the shaping engine be able to identify
marks by their general position. 

For example, left-side dependent vowels (matras), classified
with `LEFT_POSITION`, must frequently be reordered, with the final
position determined by whether or not other letters in the syllable
have formed ligatures or combined into conjunct forms. Therefore, the
`LEFT_POSITION` subclass of the character must be tracked throughout
the shaping process.


### Character tables ###

Character tables for all of the scripts, plus the Vedic Extensions and
important miscellaneous characters, are available here:

  - [Devanagari](opentype-shaping-devanagari.md#devanagari-character-table) (Including Devanagari Extended)
  - [Bengali](character-tables/character-tables-bengali.md)
  - [Vedic Extensions](opentype-shaping-vedic-extensions.md)
  - [Miscellaneous Indic Characters](opentype-shaping-miscellaneous-indic-characters.md) 
	
	
	
## The Indic2 shaping model ##

Processing a run of text in any of the modern Indic script tags
involves six top-level stages: 

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying all remaining positioning features from GPOS


The initial reordering and final reordering stages each involve a set
of script-specific rules that dictate how characters are reordered
from their sequence in the input stream into the correct ordering for
shaping rules to apply.

Specifically, certain consonants in each script are repositioned from
their logical position (that is, their position in the input
stream). The most common example is "Ra", which is frequently
converted into a combining mark-like form. 

The resulting mark must be correctly positioned by attaching it to the
correct base character using the active font's `mark` lookup from
`GPOS`. Therefore, the mark form of the "Ra" must be moved so that it
is adjacent to the correct base character. Which character in a
syllable is the correct base character differs from script to script,
and may involve several context-sensitive tests.

Similarly, certain other consonants in each script also take on
distinct forms that require reordering so that `mark` positioning
and other lookups function correctly. Dependent vowels (matras) may
also need to be reordered so that they are adjacent to the correct
consonant. These functions, too, involve script-specific rule sets.

Because of the script-specific rules involved, it is mandatory that
the basic substitution features in stage three be applied in the order
specified. 

The remaining substitution features in stage five and the positioning
features in stage six, however, do not have a mandatory order.

### Sort ordering ###

A single, canonical sequence of ordering positions exists that
captures all of the possible positions in an Indic syllable. 

Not every position is used in every script and not every sylable will
contain a character in every position. Whenever characters in a
syllable are reordered during the shaping process, 

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

Not every position is used in every script; the sequence merely
describes all of the possible positions at which a character in an
Indic syllable can exist. Using the same sequence for all scripts
could reduce an implementation's code size and complexity.

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
positions matter only in that they are unabiguous. 

The description of the general shaping process that follows will note
when a character needs to be marked for reordering into some of these
positions. The specifics for each script provide additional details,
especially for ordering positions that are only used in that script.


### Script shaping characteristics ###

Indic scripts follow many of the same shaping patterns, but they
differ in a few critical characteristics that the shaping engine must
track. These include:

  - The rules that determine the base consonant in a syllable.
  
  - The final position of "Reph".
  
  - How "Reph" is encoded or requested in a syllable.
	
  - Whether the below-base forms feature is applied only to consonants
    after the base consonant, or to consonants before the base
    consonant and those after the base consonant.
	
  - The ordering positions for dependent vowels
    (matras). Specifically, the ordering for left-side, right-side, 
    above-base, and below-base matras follow different rules. The
    rules employed vary between scripts, except for left-side matras,
    where all Indic scripts follow the same rule. 

In the lists that follow, the options for each characteristic are
mutually exclusive, and they are exhaustive for the set of Indic
scripts [listed](#general-information) at the beginning of this
document (Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam,
Oriya, Tamil, Telugu, Sinhala, and Khmer).

Implementers who wish to cover additional scripts using the same
method would first need to determine whether any additional options
are relevent for each characteristic.

#### Base consonant ####

Locating the base consonant of a syllable generally requires parsing
the syllable to catch and exclude certain special-treatment consonants
(such as "Ra"s that will form "Reph"s or consonants that take on
below-base forms). However, each script has a general base-consonant
position that determines the appropriate search method. The base
consonant may be, generally:

  - The first consonant. This is designated `BASE_POS_FIRST`.
  
  - The last consonant. This is designated `BASE_POS_LAST`.
  
  - The last consonant that is not preceded by a "ZWJ" (zero width
    joiner) character. This position is only used in Sinhala, and is
    designated `BASE_POS_LAST_SINHALA`.

#### Reph position ####

"Reph" may be positioned:

  - at the beginning of the syllable, in the ordering position
    `POS_RA_TO_BECOME_REPH`.
	
  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the base consonant, in the ordering position `POS_AFTER_MAIN`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately beforw the last post-base consonant, in the ordering
    position `POS_BEFORE_POST`.
	
  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.

#### Reph encoding ####

"Reph" may be:

  - requested explicitly, using the sequence "Ra,Halant,ZWJ". This is
    designated `REPH_MODE_EXPLICIT`.
  
  - Formed implicitly by the sequence "Ra,Halant" when used in certain positions
    in a syllable. This is designated `REPH_MODE_IMPLICIT`. Because a
    "Ra,Halant" does _not_ form a "Reph" in _every_ position in a
    syllable, script-specific tests are required.

  - encoded as a separate codepoint. This codepoint is generally
    called "Repha", which distinguishes it from the "Reph"s formed by
    other sequences. A "Repha" may need reordering based on script
    specific rules, in which case `REPH_MODE_LOGICAL_REPHA` is
    used. Alternatively, the script may not reorder "Repha"s at all,
    in which case `REPH_MODE_VISUAL_REPHA` is used.
  
#### Below-base forms ####

Below-base consonant forms (the `blwf` feature) may be applied:

  - Only to consonants after the base consonant. This is designated
    `BLWF_MODE_POST_ONLY`.
	
  - To consonants occuring before or after the base consonant. This is
    designated `BLWF_MODE_PRE_AND_POST`.

#### Left-side matras ####

All Indic scripts position left-side matras in the same
manner, in the ordering position `POS_PREBASE_MATRA`.

#### Right-side matras ####

Right-side matras may be positioned:

  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.

#### Above-base matras ####

Above-base matras may be positioned:

  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the base consonant, in the ordering position `POS_AFTER_MAIN`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.


#### Below-base matras ####

Below-base matras may be positioned:

  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.


### 1: Identifying syllables and other sequences ###

A syllable in an Indic consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

Generally speaking, each syllable contains exactly one vowel
sound. Valid syllables may begin with either consonant or an
independent vowel.

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

Valid consonant-based syllables may include one or more additional 
consonants that precede the base consonant. Each of these
other, pre-base consonants will be followed by the "Halant" mark, which
indicates that they carry no vowel. They affect pronunciation by
combining with the base consonant (e.g., "_str_", "_pl_") but they
do not add a vowel sound.

Some Indic scripts also include special consonants that can occur after the
base consonant. These post-base consonants and final consonants will
also be separated from the base consonant by a "Halant" mark; the
algorithm for correctly identifying the base consonant includes a test
to recognize these sequences and not mis-identify the base consonant.

In Indic scripts, the consonant "Ra" receives special treatment; in
many circumstances it is replaced by one of two combining mark-like forms. 

  - A "Ra,Halant" sequence at the beginning of a syllable may be replaced
    with an above-base mark called "Reph" (unless the "Ra" is the only
    consonant in the syllable). 

  - "Ra,Halant" sequences that occur elsewhere in the syllable may
    take on a below-base form (called "Rakaar" in Devanagari and most
    other scripts, and called "Raphala" in Bengali).

In addition, some scripts reorder post-base "Ra"s to a pre-base
position. These re-ordering "Ra"s may take on a different form, but
they are letter-like rather than mark-like forms.

"Reph", "Rakaar", "Raphala", and reordering "Ra" characters must be
reordered after the syllable-identification stage is complete. 


In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in Indic scripts, may
> not adhere to the syllable-formation rules described above. In
> particular, it is not uncommon to encounter foreign loanwords that
> contain a word-final suffix of consonants.
>
> Nevertheless, such word-final suffixes will be correctly matched by
> the regular expressions listed below. These words are pronounced
> different, which raises issues for potential readers, but the
> character sequences do not affect the shaping process.



Syllables should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 

The following general-purpose regular expressions can be
used to match Indic syllables. The regular expressions utilize the
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

This may mean moving dependent-vowel (matra) glyphs, "Ra,Halant"
sequences, and other consonants that take special 
treatment in some circumstances.

These reordering moves are mandatory. The final-reordering stage
may make additional moves, depending on the text and on the features
implemented in the active font.

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
scripts. Not every position will be utilized in every script.

Additional information about the ordering positions is available in
the [sort ordering](#sort-ordering) section of this document.

#### 2.1: Base consonant ####

The first step is to determine the base consonant of the syllable, if
there is one, and tag it as `POS_BASE_CONSONANT`.

The algorithm used to find the base consonant varies according to the
base-consonant shaping characteristic of the script.

For `BASE_POS_FIRST` scripts, the first consonant of the syllable is
the base consonant.

For `BASE_POS_LAST` scripts, the base consonant is the last consonant
in the syllable, excluding all consonants that will take on special
post-base, final, or below-base forms, and excluding all pre-base
reordering "Ra"s. For a detailed explanation of the search algorithm
employed, see the page for each specific script.

For Sinhala, which uses `BASE_POS_LAST_SINHALA`, the base consonant is
the last consonant that is not preceded by a zero-width joiner
("ZWJ").


#### 2.2: Matra decomposition ####

Second, any two-part or three-part dependent vowels (matras) must be decomposed
into their component parts.

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.


#### 2.3: Tag decomposed matras ####

Third, all dependent-vowel (matra) signs must be tagged with
their final position. 

All single-part matras can be tagged based on their Mark-positioning
subclass. The shaping engine may choose to perform this tagging
earlier, such as during an initial Unicode-normalization stage.

Matras that resulted from the preceding decomposition step, however,
may not have been tagged when they were decomposed. If not, they must
be tagged for reordering before proceeding to the next step.


<!--- Should this be ALL matras? Or all non-right. non-below-base -->
<!--  matras?                                                    --->

#### 2.4: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. 

The canonical ordering means that any "Nukta"s must
be placed before all other marks. No other marks in the subsequence
should be reordered.

#### 2.5: Pre-base consonants ####

Fifth, consonants that occur before the base consonant must be tagged
with `POS_PREBASE_CONSONANT`.

#### 2.6: Reph ####

Sixth, initial "Ra,Halant" sequences that will become "Reph"s must be tagged with
`POS_RA_TO_BECOME_REPH`.

#### 2.7: Post-base consonants ####

Seventh, any non-base consonants that occur after a dependent vowel
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. Such
consonants will either be followed by a "Halant" glyph or will be in
the `CONSONANT_DEAD` shaping class. 
	
  <!--- Double check: should this be "_consonant_,Halant" instead of
        "Halant,_consonant_"? --->
	
#### 2.8: Mark tagging ####

Eighth, all marks must be tagged with the same positioning tag as the
closest preceding non-mark character, so that they move together
during the sorting step.

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
	rkrf 
	pref 
	blwf 
	abvf 
	half
	pstf
	vatu
	cjct
	cfar


Not every feature is used in every script. See the individual script
pages for further script-specific information.


> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> GSUB substitutions in the following steps.


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
position. The correct final position depends on the script's
`REPH_MODE_`. See the individual script pages for more information.

#### 4.4: Pre-base consonants ####

Any pre-base reordering consonants must be moved to immediately before
the base consonant.
  

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

### 6: Applying remaining positioning features from GPOS ###

In this stage, mark positioning, kerning, and other GPOS features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the GPOS table in the font.

        dist
        abvm
        blwm

