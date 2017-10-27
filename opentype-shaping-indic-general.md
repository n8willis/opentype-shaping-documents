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
      - [Script shaping characteristics](#script-shaping-characteristics)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The old Indic shaping model](#the-beng-shaping-model)


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
in scripts like Devanagari, Bengali, and Gurmukhi. To avoid ambiguity, the term **headline** is
used in most Unicode and OpenType shaping documents.

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. 

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel should be nasalized. 

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.


## Glyph classification ##

Shaping Indic text depends on the shaping engine correctly
classifying each glyph in the run. The classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark. 

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
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
letter is likely not accompanied by a `VIRAMA`; failure to recognize this
distinction could trick naive parsers into mis-identifying the letter
as the base consonant of a syllable.

Other characters, such as symbols and miscellaneous letters (for
example, letter-like symbols that only occur as standalone entities
and do not occur within syllables), need no special attention from the
shaping engine, so they are not assigned a shaping class.

Numbers are classified as `NUMBER`, even though they evoke no special
behavior from the Indic shaping rules, because there are OpenType features that
might affect how the respective glyphs are drawn, such as `tnum`,
which specifies the usage of tabular-width numerals, and `sups`, which
replaces the default glyphs with superscript variants.

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
  - [Bengali](opentype-shaping-bengali.md#bengali-character-table)
  - [Vedic Extensions](opentype-shaping-vedic-extensions.md)
  - [Miscellaneous Indic Characters](opentype-shaping-miscellaneous-indic-characters.md) 
	
	
	
## The Indic2 shaping model ##

Processing a run of text in any of the modern Indic script tags involves six top-level stages:

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

The resulting mark must be correctly positioned by attaching it to the correct
base character using the active font's `mark` lookup from
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
the basic substitution features in stage 3 be applied in the order
specified. 

The remaining substitution features in stage 5 and the positioning
features in stage 6, however, do not have a mandatory order.


### Script shaping characteristics ###

Indic scripts follow many of the same shaping patterns, but they
differ in a few critical characteristics that the shaping engine must
track. These include:

  - The rules that determine the base consonant in a syllable.
  
  - The final position of "Reph".
  
  - How "Reph" is encoded or requested in a syllable.
	
  - Whether the below-base forms feature is applied only to consonants
    before the base consonant, only to consonants after the base
    consonant, or to both.
	
  - The ordering positions for dependent vowels
    (matras). Specifically, the ordering for left-side, right-side,
    above-base, and below-base matras follow different rules. The
    rules employed vary between scripts, except for left-side matras,
    where all Indic scripts follow the same rule. 

#### Base consonant ####

Locating the base consonant of a syllable generally requires parsing
the syllable to catch and exclude certain special-treatment consonants
(such as "Ra"s that will form "Reph"s or consonants that take on
below-base forms). However, each script has a general base-consonant
position that determines the appropriate search method. The base
consonant may be, generally:

  - The first consonant. This is designated `BASE_POS_FIRST`.
  
  - The last consonant. This is designated `BASE_POS_LAST`.
  
  - The last consonant that is not preceded by a "ZWJ". This position
    is only used in Sinhala, and is designated `BASE_POS_LAST_SINHALA`.

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
