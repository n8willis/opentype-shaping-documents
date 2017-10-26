# Indic script shaping in OpenType #

This document outlines the general shaping procedure shared by all
Indic scripts, and defines the common pieces that script-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Character tables](#character-tables)
  - [The Indic2 shaping model](#the-indic2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The old Indic shaping model](#the-beng-shaping-model)


## General information ##

The Indic (or Bhramic) family of scripts includes writing systems
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

### Shaping classes and subclasses ###

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

Specifically, certain consonants in every script are repositioned from
their logical position (that is, their position in the input
stream). The most common example is "Ra", which is frequently
converted into a combining mark-like form. 

The mark must be correctly positioned by attaching it to the correct
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
