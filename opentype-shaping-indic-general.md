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
derived from the Brahmi script in ancient India. Although the scripts
vary considerably in appearance, their shared ancestry means that they
also share a number of important features and rules. 

This makes it possible (though, of course, not mandatory) for a
shaping engine to implement a single shaping model that covers all of
the scripts. 

The largest (by number of readers) scripts in the Indic family are:

  - [Devanagari](opentype-shaping-devanagari.md)
  - [Bengali](opentype-shaping-bengali.md)
  - [Gujarati](opentype-shaping-gujarati.md)
  - [Gurmukhi](opentype-shaping-gurmukhi.md)
  - [Kannada](opentype-shaping-kannada.md)
  - [Malayalam](opentype-shaping-malayalam.md)
  - [Oriya](opentype-shaping-oriya.md)
  - [Tamil](opentype-shaping-tamil.md)
  - [Telugu](opentype-shaping-telugu.md)
  - [Sinhala](opentype-shaping-sinhala.md)

Text runs in Indic scripts may also include characters from the Vedic
Extensions block in Unicode. This is a set of marks and punctuation
needed to accurately transcribe ancient documents in Sanskrit.

Text runs in Indic scripts also make use of joiner, non-joiner, and
placeholder characters from other Unicode blocks, in order to specify
certain alternate shaping options.

There are two sets of Indic script tags defined in OpenType. Several
from the older set (`<deva>`, `<beng>`, `<gujr>`, `<guru>`, `<knda>`,
`<mlym>`, `<orya>`, `<taml>`, and `<telu>`) were deprecated and
replaced in 2005.

The new set of replacement tags for these scripts (`<dev2>`, `<bng2>`,
`<gjr2>`, `<gur2>`, `<knd2>`, `<mlm2>`, `<ory2>`, `<tml2>`, and
`<tel2>`) was devised to overcome shortcomings found in the original model. 
Therefore, new fonts should be engineered to work with the updated
shaping model. However, if a font is encountered that supports only
an older script tag, the shaping engine should deal with it gracefully.

The `<sinh>` tag, unlike the other Indic script tags,
was not deprecated in 2005 and is still used for Sinhala text.

> Note: There are several other scripts derived from the Bhrami script
> that are often treated separately and not bundled into the "Indic"
> category by shaping engines. This is because these other scripts
> evolved to have significantly distinct rules for syllable
> construction, reordering, and shaping.
>
> The scripts include Buginese, Balinese, Javanese,
> [Khmer](opentype-shaping-khmer.md),
> [Lao](opentype-shaping-thai-lao.md),
> [Myanmar](opentype-shaping-myanmar.md),
> [Thai](opentype-shaping-thai-lao.md), and
> [Tibetan](opentype-shaping-tibetan.md). 

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
example.

Syllables may also begin with an **indepedent vowel** instead of a
consonant. In these syllables, the independent vowel is rendered in
full-letter form, not as a matra, and the independent vowel serves as the
syllable base, similar to a base consonant.

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
Indic glyphs must additionally be classified by how they are treated
when shaping a run of text.

### Shaping classes ###

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
common mark. 

Less common mark classes include `TONE_MARKER`, `CANTILLATION`,
`GEMINATION_MARK`, `PURE_KILLER`,  and `SYLLABLE_MODIFIER`. An
explanation of each class is included in the shaping documentation of
each script in which the class occurs.

Letters generally fall into the classes `CONSONANT`,
`VOWEL_INDEPENDENT`, and `VOWEL_DEPENDENT`. These classes help the
shaping engine parse and identify key positions in a syllable. For
example, Unicode categorizes dependent vowels as `Mark [Mn]`, but the
shaping engine must be able to distinguish between dependent vowels
and diacritical marks (some of which are also categorized as `Mark [Mn]`).

There are several subclasses of consonants that arise on occasion, such as
`CONSONANT_DEAD`, `CONSONANT_MEDIAL`, `CONSONANT_PLACEHOLDER`,
`CONSONANT_WITH_STACKER`, and `CONSONANT_PRE_REPHA`. 

These subclasses indicate that the letter should match simple
tests for consonants (as in the regular expressions used during
syllable identification), but the subclass may factor into
script-specific rules encountered in later shaping stages.

For example, `CONSONANT_DEAD` indicates that, unlike standard
consonants, the dead consonant carries no inherent vowel. This lack of
an inherent vowel means that the letter is likely not accompanied by a
`VIRAMA`; failure to recognize this distinction could trick a naive
parser into mis-identifying the letter as the base consonant of a
syllable during the base-consonant-identification step. 

Not every script features an instance of each consonant subclass. A
full explanation of each subclass's behavior is explained in the
relevant stage of each script's shaping documentation.


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

Marks and dependent vowels are further labeled with a mark-placement
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

There are four basic _mark-placement subclasses_ for dependent vowels
(matras). Each corresponds to the visual position of the matra with
respect to the syllable base to which it is attached:

  - `LEFT_POSITION` matras are positioned to the left of the syllable base.
  - `RIGHT_POSITION` matras are positioned to the right of the syllable base.
  - `TOP_POSITION` matras are positioned above the syllable base.
  - `BOTTOM_POSITION` matras are positioned below syllable base.
  
These positions may also be referred to elsewhere in shaping documents as:

  - _Pre-base_ matras
  - _Post-base_ matras
  - _Above-base_ matras
  - _Below-base_ matras
  
respectively. The `LEFT`, `RIGHT`, `TOP`, and `BOTTOM` designations
corresponds to Unicode's preferred terminology. The _Pre_, _Post_,
_Above_, and _Below_ terminology is used in the official descriptions
of OpenType GSUB and GPOS features. Shaping engines may, internally,
use whichever terminology is preferred.

In addition, dependent-vowel codepoints that are composed of multiple
components will be designated in character tables as having a compound
_mark-placement subclass_, such as `TOP_AND_RIGHT` or `LEFT_AND_RIGHT`. 

However, these multi-part matras are decomposed into separate matra
components during the shaping process. After the decomposition, each
matra component will belong to exactly one of the four basic
_mark-placement subclasses_.

For most mark and dependent-vowel codepoints, the _mark-placement
subclass_ is synonymous with the `Indic Positional Category` defined
in Unicode. However, there are some distinctions, where the defined
category does not fully capture the behavior of the character in the
shaping process. 

### Character tables ###

Character tables for all of the scripts, plus the Vedic Extensions and
important miscellaneous characters, are available here:

  - [Devanagari](character-tables/character-tables-devanagari.md) (Including Devanagari Extended)
  - [Bengali](character-tables/character-tables-bengali.md)
  - [Gujarati](character-tables/character-tables-gujarati.md)
  - [Gurmukhi](character-tables/character-tables-gurmukhi.md)
  - [Kannada](character-tables/character-tables-kannada.md)
  - [Malayalam](character-tables/character-tables-malayalam.md)
  - [Oriya](character-tables/character-tables-oriya.md)
  - [Tamil](character-tables/character-tables-tamil.md)
  - [Telugu](character-tables/character-tables-telugu.md)
  - [Sinhala](character-tables/character-tables-sinhala.md)

	
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

Not every position is used in every script and not every syllable will
contain a character in every position. Whenever characters in a
syllable are reordered during the shaping process, 

	POS_RA_TO_BECOME_REPH
	POS_PREBASE_MATRA
	POS_PREBASE_CONSONANT

	POS_SYLLABLE_BASE
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
consonant or syllable base (`POS_PREBASE_MATRA` and `POS_PREBASE_CONSONANT`), the base
consonant or syllable base (`POS_SYLLABLE_BASE`), above-base consonants
(`POS_ABOVEBASE_CONSONANT`), below-base consonants
(`POS_BELOWBASE_CONSONANT`), consonants positioned after the base consonant or syllable base
(`POS_POSTBASE_CONSONANT`), syllable-final consonants (`POS_FINAL_CONSONANT`),
and syllable-modifying or Vedic signs (`POS_SMVD`).

In addition, several secondary positions are defined to handle various
reordering rules that deal with relative, rather than absolute,
positioning. `POS_AFTER_MAIN` means that a character must be
positioned immediately after the base consonant or syllable base. `POS_BEFORE_SUBJOINED`
and `POS_AFTER_SUBJOINED` mean that a character must be positioned
before or after any below-base consonants, respectively. Similarly,
`POS_BEFORE_POST` and `POS_AFTER_POST` mean that a character must be
positioned before or after any post-base consonants, respectively. 

For shaping-engine implementers, the names used for the ordering
positions matter only in that they are unambiguous. 

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
    after the base consonant or syllable base, or to consonants before the base
    consonant and those after the base consonant or syllable base.
	
  - The ordering positions for dependent vowels
    (matras). Specifically, the ordering for left-side, right-side, 
    above-base, and below-base matras follow different rules. The
    rules employed vary between scripts, except for left-side matras,
    where all Indic scripts follow the same rule. 

In the lists that follow, the options for each characteristic are
mutually exclusive, and they are exhaustive for the set of Indic
scripts [listed](#general-information) at the beginning of this
document (Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam,
Oriya, Tamil, Telugu, and Sinhala).

Implementers who wish to cover additional scripts using the same
method would first need to determine whether any additional options
are relevant for each characteristic.

#### Base consonant ####

Locating the base consonant of a syllable generally requires parsing
the syllable to catch and exclude certain special-treatment consonants
(such as "Ra"s that will form "Reph"s or consonants that take on
below-base forms). However, each script has a general base-consonant
position that determines the appropriate search method. The base
consonant may be, generally:

  - The first consonant. This is designated `BASE_POS_FIRST`. This is
    the simplest base-consonant rule. After eliminating any initial
    "Repha"s from consideration, the first consonant is always the
    base consonant, without exception.
  
  - The last consonant, not counting any special forms. This is
    designated `BASE_POS_LAST`. This is the most complicated
    base-consonant rule, because the type and variety of special forms
    vary considerably between scripts. 
	
	The `BASE_POS_LAST` search algorithm (described in each script's
    shaping document) accounts for these special forms in every
    script. The abundance of special forms in certain scripts may
    routinely cause the search algorithm to identify a base consonant
    that is not logically last in the syllable. This is expected
    behavior.
	
	This base-consonant position is used in Devanagari, Bengali,
	Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, and Telugu.
  
  - The last consonant that is not preceded by a "ZWJ" (zero width
    joiner) character. 
	
	This position is only used in Sinhala, and is designated
    `BASE_POS_LAST_SINHALA`.

The scripts currently described in the "Indic" script group  and their
corresponding base-consonant rules are summarized in the following
table:

| Script     | Base-consonant rule    |
|:-----------|:-----------------------|
| Devanagari | `BASE_POS_LAST`        |
| Bengali    | `BASE_POS_LAST`        |
| Gujarati   | `BASE_POS_LAST`        |
| Gurmukhi   | `BASE_POS_LAST`        |
| Kannada    | `BASE_POS_LAST`        |
| Malayalam  | `BASE_POS_LAST`        |
| Oriya      | `BASE_POS_LAST`        |
| Tamil      | `BASE_POS_LAST`        |
| Telugu     | `BASE_POS_LAST`        |
| Sinhala    | `BASE_POS_LAST_SINHALA`|


> Note: None of the specific scripts currently included in the "Indic"
> script group as it is enumerated in this document make use of the
> `BASE_POS_FIRST` base-consonant rule. However, the `BASE_POS_FIRST`
> rule is employed by several Brahmi-derived scripts also used in the
> region, including both [Myanmar](opentype-shaping-myanmar.md) and
> [Khmer](opentype-shaping-khmer.md). 
>
> Because these scripts share many other characteristics and
> conventions with the Indic group described by this document,
> `BASE_POS_FIRST` is included here for comparison. 

> Note: The `BASE_POS_LAST` search algorithm is used for Kannada and
> Telugu, although the unique properties of the Kannada and Telugu
> orthographies usually result in the search terminating at the first
> non-"Reph" consonant in a syllable. Namely, all consonants in
> Kannada and Telugu have a post-base form. 
>
> This is the expected behavior for Kannada and Telugu, and still
> differs from the `BASE_POS_FIRST` rule as used in the Brahmi-derived 
> scripts mentioned above. See those individual script pages for
> further detail.


#### Reph position ####

"Reph" may be positioned:

  - at the beginning of the syllable, in the ordering position
    `POS_RA_TO_BECOME_REPH`.
	
  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the base consonant or syllable base, in the ordering position `POS_AFTER_MAIN`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately before the last post-base consonant, in the ordering
    position `POS_BEFORE_POST`.
	
  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.

The scripts currently described in the "Indic" script group  and their
corresponding Reph-position rules are summarized in the following
table:

| Script     | Reph-position rule         |
|:-----------|:---------------------------|
| Devanagari | `REPH_POS_BEFORE_POST`     |
| Bengali    | `REPH_POS_AFTER_SUBJOINED` |
| Gujarati   | `REPH_POS_BEFORE_POST`     |
| Gurmukhi   | `REPH_POS_BEFORE_SUBJOINED`|
| Kannada    | `REPH_POS_AFTER_POST`      |
| Malayalam  | `REPH_POS_AFTER_MAIN`      |
| Oriya      | `REPH_POS_AFTER_MAIN`      |
| Tamil      | `REPH_POS_AFTER_POST`      |
| Telugu     | `REPH_POS_AFTER_POST`      |
| Sinhala    | `REPH_POS_AFTER_MAIN`      |




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


The scripts currently described in the "Indic" script group  and their
corresponding Reph-encoding rules are summarized in the following
table:

| Script     | Reph-encoding rule         |
|:-----------|:---------------------------|
| Devanagari | `REPH_MODE_IMPLICIT`       |
| Bengali    | `REPH_MODE_IMPLICIT`       |
| Gujarati   | `REPH_MODE_IMPLICIT`       |
| Gurmukhi   | `REPH_MODE_IMPLICIT`       |
| Kannada    | `REPH_MODE_IMPLICIT`       |
| Malayalam  | `REPH_MODE_LOGICAL_REPHA`  |
| Oriya      | `REPH_MODE_IMPLICIT`       |
| Tamil      | `REPH_MODE_IMPLICIT`       |
| Telugu     | `REPH_MODE_EXPLICIT`       |
| Sinhala    | `REPH_MODE_EXPLICIT`       |


> Note: None of the specific scripts currently included in the "Indic"
> group as it is enumerated in this document make use of the
> `REPH_MODE_VISUAL_REPHA` encoding. However, `REPH_MODE_VISUAL_REPHA`
> is used in the [Khmer](opentype-shaping-khmer.md) script. 
>
> Because Khmer shares many other characteristics and
> conventions with the Indic group described by this document,
> `REPH_MODE_VISUAL_REPHA` is included here for comparison. 



#### Below-base forms ####

Below-base consonant forms (the `blwf` feature) may be applied:

  - Only to consonants after the base consonant or syllable base. This is designated
    `BLWF_MODE_POST_ONLY`.
	
  - To consonants occurring before or after the base consonant or syllable base. This is
    designated `BLWF_MODE_PRE_AND_POST`.


The scripts currently described in the "Indic" script group  and their
corresponding below-base–forms rules are summarized in the following
table:

| Script     | Below-base–forms rule    |
|:-----------|:-------------------------|
| Devanagari | `BLWF_MODE_PRE_AND_POST` |
| Bengali    | `BLWF_MODE_PRE_AND_POST` |
| Gujarati   | `BLWF_MODE_PRE_AND_POST` |
| Gurmukhi   | `BLWF_MODE_PRE_AND_POST` |
| Kannada    | `BLWF_MODE_POST_ONLY`    |
| Malayalam  | `BLWF_MODE_PRE_AND_POST` |
| Oriya      | `BLWF_MODE_PRE_AND_POST` |
| Tamil      | `BLWF_MODE_PRE_AND_POST` |
| Telugu     | `BLWF_MODE_POST_ONLY`    |
| Sinhala    | `BLWF_MODE_PRE_AND_POST` |


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


The scripts currently described in the "Indic" script group  and their
corresponding right-side–matra positions are summarized in the following
table:

| Script     | Right-side–matra position |
|:-----------|:--------------------------|
| Devanagari | `POS_AFTER_SUBJOINED`     |
| Bengali    | `POS_AFTER_POST`          |
| Gujarati   | `POS_AFTER_POST`          |
| Gurmukhi   | `POS_AFTER_POST`          |
| Kannada    | _varies_                  |
| Malayalam  | `POS_AFTER_POST`          |
| Oriya      | `POS_AFTER_POST`          |
| Tamil      | `POS_AFTER_POST`          |
| Telugu     | _varies_                  |
| Sinhala    | `POS_AFTER_SUBJOINED`     |



> Note: In most scripts, all right-side matras are positioned in the
> same sort-order position. The Kannada and Telugu scripts, however,
> feature more complex positioning rules for right-side matras, in
> which different right-side matras must be sorted into different
> positions. See the script-specific shaping documents for full
> details.


#### Above-base matras ####

Above-base matras may be positioned:

  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the base consonant or syllable base, in the ordering position `POS_AFTER_MAIN`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.


The scripts currently described in the "Indic" script group  and their
corresponding above-base–matra positions are summarized in the following
table:

| Script     | Above-base–matra position |
|:-----------|:--------------------------|
| Devanagari | `POS_AFTER_SUBJOINED`     |
| Bengali    | _null_                    |
| Gujarati   | `POS_AFTER_SUBJOINED`     |
| Gurmukhi   | `POS_AFTER_POST`          |
| Kannada    | `POS_BEFORE_SUBJOINED`    |
| Malayalam  | _null_                    |
| Oriya      | `POS_AFTER_MAIN`          |
| Tamil      | `POS_AFTER_SUBJOINED`     |
| Telugu     | `POS_BEFORE_SUBJOINED`    |
| Sinhala    | `POS_AFTER_SUBJOINED`     |



#### Below-base matras ####

Below-base matras may be positioned:

  - immediately before the first subjoined (below-base) consonant, in
    the ordering position `POS_BEFORE_SUBJOINED`.
	
  - immediately after the last subjoined (below-base) consonant, in
    the ordering position `POS_AFTER_SUBJOINED`.

  - immediately after the last post-base consonant, in the ordering
    position `POS_AFTER_POST`.


The scripts currently described in the "Indic" script group  and their
corresponding below-base–matra positions are summarized in the following
table:

| Script     | Below-base–matra position |
|:-----------|:--------------------------|
| Devanagari | `POS_AFTER_SUBJOINED`     |
| Bengali    | `POS_AFTER_SUBJOINED`     |
| Gujarati   | `POS_AFTER_POST`          |
| Gurmukhi   | `POS_AFTER_POST`          |
| Kannada    | `POS_BEFORE_SUBJOINED`    |
| Malayalam  | `POS_AFTER_POST`          |
| Oriya      | `POS_AFTER_SUBJOINED`     |
| Tamil      | `POS_AFTER_POST`          |
| Telugu     | `POS_BEFORE_SUBJOINED`    |
| Sinhala    | `POS_AFTER_SUBJOINED`     |



### 1: Identifying syllables and other sequences ###

A syllable in an Indic script consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

The Nukta, Halant/Virama, and Anudatta marks can affect syllable
identification. All other signs are regarded as syllable modifier
signs, including those from the Vedic Extensions block.

Generally speaking, each syllable contains exactly one vowel
sound. Valid syllables may begin with either a consonant or an
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
base consonant or syllable base. These post-base consonants and final consonants will
also be separated from the base consonant or syllable base by a "Halant" mark; the
algorithm for correctly identifying the base consonant includes a test
to recognize these sequences and not mis-identify the base consonant.

In Indic scripts, the consonant "Ra" receives special treatment; in
many circumstances it is replaced by one of two combining mark-like forms. 

  - A "Ra,Halant" sequence at the beginning of a syllable may be replaced
    with an above-base mark called "Reph" (unless the "Ra" is the only
    consonant in the syllable). 

  - "Halant,Ra" sequences that occur elsewhere in the syllable may
    take on a below-base form (called "Rakaar" in Devanagari and most
    other scripts, and called "Raphala" in Bengali).

In addition, some scripts reorder post-base "Ra"s to a pre-base
position. These re-ordering "Ra"s may take on a different form, but
they are letter-like rather than mark-like forms.

"Reph", "Rakaar", "Raphala", and reordering "Ra" characters must be
reordered after the syllable-identification stage is complete. 

> Note: Generally speaking, OpenType fonts will implement support for
> any below-base, post-base, and pre-base-reordering consonant forms
> by including the necessary substitution rules in their `blwf`,
> `pstf`, and `pref` lookups in GSUB.
>
> Consequently, whenever shaping engines need to determine whether or 
> not a given consonant can take on such a special form, the most
> appropriate test is to check if the consonant is included in the
> relevant GSUB lookup. Other implementations are possible, such as
> maintaining static tables of consonants, but checking for GSUB
> support ensures that the expected behavior is implemented in the
> active font, and is therefore the most reliable approach.


In addition to valid syllables, standalone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in Indic scripts, may
> not adhere to the syllable-formation rules described above. In
> particular, it is not uncommon to encounter foreign loanwords that
> contain a word-final suffix of consonants.
>
> Nevertheless, such word-final suffixes will be correctly matched by
> the regular expressions listed below. These loanwords are pronounced
> different, which raises issues for potential readers, but the
> character sequences do not affect the shaping process.


Syllables should be identified by examining the run and matching
glyphs, based on their shaping class, using regular expressions. 

The following general-purpose regular expressions can be
used to match Indic syllables. 

The regular expressions utilize the shaping classes from the tables
above. For the purpose of syllable identification, more general
classes can be used, as defined in the following table. This
simplifies the resulting expressions. 

```markdown
_ra_		= The consonant "Ra" 
_consonant_	= ( `CONSONANT` | `CONSONANT_DEAD` ) - _ra_
_vowel_		= `VOWEL_INDEPENDENT`
_nukta_	  	= `NUKTA`
_halant_	= `VIRAMA`
_zwj_		= `JOINER`
_zwnj_		= `NON_JOINER`
_matra_		= `VOWEL_DEPENDENT` | `PURE_KILLER`
_syllablemodifier_	= `SYLLABLE_MODIFIER` | `BINDU` | `VISARGA` | `GEMINATION_MARK`
_vedicsign_	= `CANTILLATION`
_placeholder_	= `PLACEHOLDER` | `CONSONANT_PLACEHOLDER`
_dottedcircle_	= `DOTTED_CIRCLE`
_repha_		= `CONSONANT_PRE_REPHA`
_consonantmedial_	= `CONSONANT_MEDIAL`
_symbol_	= `SYMBOL` | `AVAGRAHA`
_consonantwithstacker_	= `CONSONANT_WITH_STACKER`
_other_		= `OTHER` | `NUMBER` | `MODIFYING_LETTER`
```


> Note: the _ra_ identification class is mutually exclusive with 
> the _consonant_ class. The union of the _consonant_ and _ra_ classes
> is used in the regular expression elements below in order to
> correctly identify "Ra" characters that do not trigger "Reph" or
> "Rakaar" shaping behavior.
>
> Note, also, that the cantillation mark "combining Ra" in the
> Devanagari Extended block does _not_ belong to the _ra_
> identification class, and that the other "combining consonant"
> cantillation marks in the Devanagari Extended block do not belong to
> the _consonant_ identification class.

> Note: The _placeholder_ identification class includes codepoints
> that are often used in place of vowels or consonants when a document
> needs to display a matra, mark, or special form in isolation or
> in another context beyond a standard syllable. Examples include
> hyphens and non-breaking spaces.

> Note: The _other_ identification class includes codepoints that
> do not interact with adjacent characters for shaping purposes. Even
> though some of these codepoints (such as `MODIFYING_LETTER`) can
> occur within words, they evoke no behavior from the shaping
> engine and do not factor into the regular expressions that
> follow. Therefore, the shaping engine may choose to ignore them
> during syllable identification; they are listed here for completeness.

These identification classes form the bases of the following regular
expression elements:

```markdown
C	= _consonant_ | _ra_
Z	= _zwj_ | _zwnj_
REPH	= (_ra_ _halant_) | _repha_
CN		= C _zwj_? _nukta_?
FORCED_RAKAR	= _zwj_ _halant_ _zwj_ _ra_
S	= _symbol_ _nukta_?
MATRA_GROUP	= Z{0,3} _matra_ _nukta_? (_halant_ | FORCED_RAKAR)?
SYLLABLE_TAIL	= (Z? _syllablemodifier_ _syllablemodifier_? _zwnj_?)? _vedicsign_{0,3}
HALANT_GROUP	= Z? _halant_ (_zwj_ _nukta_?)?
FINAL_HALANT_GROUP	= HALANT_GROUP | (_halant_ _zwnj_)
MEDIAL_GROUP	= _consonantmedial_?
HALANT_OR_MATRA_GROUP	= FINAL_HALANT_GROUP | ((_halant_ _zwj_)? MATRA_GROUP*)
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than 4 sequential `(MATRA_GROUP)`
> instances in any real-word syllables. Thus, implementations may
> choose to limit occurrences by limiting the above expressions to a
> finite length, such as `(MATRA_GROUP){0,4}` .


Using the above elements, the following regular expressions define the
possible syllable types:

A consonant-based syllable will match the expression:
```markdown
(_repha_|_consonantwithstacker_)? (CN HALANT_GROUP)* CN MEDIAL_GROUP HALANT_OR_MATRA_GROUP SYLLABLE_TAIL
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than 4 sequential `(CN HALANT_GROUP)`
> instances in any real-word syllables. Thus, implementations may
> choose to limit occurrences by limiting the above expressions to a
> finite length, such as `(CN HALANT_GROUP){0,4}` .

A vowel-based syllable will match the expression:
```markdown
REPH? _vowel_ _nukta_? (_zwj_ | (HALANT_GROUP CN)* MEDIAL_GROUP HALANT_OR_MATRA_GROUP SYLLABLE_TAIL)
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than 4 sequential `(HALANT_GROUP CN)`
> instances in any real-word syllables. Thus, implementations may
> choose to limit occurrences by limiting the above expressions to a
> finite length, such as `(HALANT_GROUP CN){0,4}` .

A standalone syllable will match the expression:
```markdown
((_repha_|_consonantwithstacker_)? _placeholder_ | REPH? _dottedcircle_) _nukta_? (HALANT_GROUP CN)* MEDIAL_GROUP HALANT_OR_MATRA_GROUP SYLLABLE_TAIL
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than 4 sequential `(HALANT_GROUP CN)`
> instances in any real-word syllables. Thus, implementations may
> choose to limit occurrences by limiting the above expressions to a
> finite length, such as `(HALANT_GROUP CN){0,4}` .

A symbol-based syllable will match the expression:
```markdown
S SYLLABLE_TAIL
```

A broken syllable will match the expression:
```markdown
REPH? _nukta_? (HALANT_GROUP CN)* MEDIAL_GROUP HALANT_OR_MATRA_GROUP SYLLABLE_TAIL
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than 4 sequential `(HALANT_GROUP CN)`
> instances in any real-word syllables. Thus, implementations may
> choose to limit occurrences by limiting the above expressions to a
> finite length, such as `(HALANT_GROUP CN){0,4}` .


The expressions above use state-machine syntax from the Ragel
state-machine compiler. The operators represent:

```markdown
a* = zero or more copies of a
b+ = one or more copies of b
c? = optional instance of c
d{n} = exactly n copies of d
d{,n} = zero to n copies of d
d{n,} = n or more copies of d
d{n,m} = n to m copies of d
!e = not e
^f = character-level not f
g.h = concatenation of g and h
i|j = i or j
( ) = grouping of expression elements
```





The shaping engine may make a best-effort attempt to shape broken
sequences, but making guarantees about the correctness or appearance
of the final result is out of scope for this document.

> Note: "standalone" syllables can be used to display examples of
> letters, marks, and other characters without requiring full
> syllables or words.

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

	POS_SYLLABLE_BASE
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
there is one, and tag it as `POS_SYLLABLE_BASE`.

The algorithm used to find the base consonant varies according to the
base-consonant shaping characteristic of the script.

For `BASE_POS_FIRST` scripts, the first consonant of the syllable is
the base consonant.

> Note: None of the specific scripts currently included in the "Indic"
> group as it is enumerated in this document make use of the
> `BASE_POS_FIRST` base-consonant rule. However, the `BASE_POS_FIRST`
> rule is employed by several Brahmi-derived scripts also used in the
> region, including both [Myanmar](opentype-shaping-myanmar.md) and
> [Khmer](opentype-shaping-khmer.md). 
>
> Because these scripts share many other characteristics and
> conventions with the Indic group described by this document,
> `BASE_POS_FIRST` is included here for comparison. 


For `BASE_POS_LAST` scripts, the base consonant is the last consonant
in the syllable, excluding all consonants that will take on special
post-base, final, or below-base forms, and excluding all pre-base
reordering "Ra"s. For a detailed explanation of the search algorithm
employed, see the page for each specific script.

For Sinhala, which uses `BASE_POS_LAST_SINHALA`, the base consonant is
the last consonant that is not preceded by a zero-width joiner
("ZWJ").

While performing the base-consonant search, shaping engines may
also encounter special-form consonants, including below-base
consonants and post-base consonants. Each of these special-form
consonants must also be tagged (`POS_BELOWBASE_CONSONANT`,
`POS_POSTBASE_CONSONANT`, respectively). 

Any pre-base-reordering consonant (such as a pre-base-reodering "Ra")
encountered during the base-consonant search must be tagged
`POS_POSTBASE_CONSONANT`. 
 
> Note: Shaping engines may choose any method to identify consonants that
> have below-base, post-base, or pre-base-reordering forms while
> executing the above algorithm. For example, one implementation may
> choose to maintain a static table of special-form consonants to
> compare against the text run. Another implementation might examine
> the active font to see if it includes a `blwf`, `pstf`, or `pref`
> lookup in the GSUB table that affects the consonants encountered in
> the syllable.
>
> However, checking for GSUB support ensures that the expected
> behavior is implemented in the active font, and is therefore the
> most reliable approach.


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

Single-part matras can be tagged with the appropriate sort-ordering
position based on the ordering position of the script's specific
script-shaping characteristics. 

In most cases, all matras of the same Mark-positioning subclass (such
as `LEFT_POSITION`) in a particular script are tagged with the same
final position (such as `POS_PREBASE_MATRA`). 

Some scripts, however, include matras that must be tagged according to
more involved rule sets. In the set of Indic scripts described here,
this includes [Kannada](opentype-shaping-kannada.md) and
[Telugu](opentype-shaping-telugu.md). See the individual
script-shaping document of each script to find a complete description
of the applicable matra-tagging rules.

> Note: The shaping engine may, as an alternative, choose to perform
> this tagging earlier, such as during an initial Unicode-normalization
> stage. 
>
> Matras that resulted from the preceding decomposition step, however,
> may not have been tagged when they were decomposed. If not, they must
> be tagged for reordering before proceeding to the next step.


#### 2.4: Adjacent marks ####

Fourth, any subsequences of marks that include a "Nukta" and a
"Halant" or Vedic sign must be reordered so that the "Nukta" appears
first.

This means that the subsequence "Halant,Nukta" is reordered to
"Nukta,Halant" and that the subsequence "_Vedic_sign_,Nukta" is
reordered to "Nukta,_Vedic_sign".

For subsequences of affected marks that are longer than two, the
reordering operation must be repeated until the "Nukta" is the first
character in the subsequence. No other marks in the subsequence
should be reordered.

This order is canonical in Unicode and is required so that
"_consonant_,Nukta" substitution rules from GSUB will be correctly
matched later in the shaping process.

#### 2.5: Pre-base consonants ####

Fifth, consonants that occur before the syllable base must be tagged
with `POS_PREBASE_CONSONANT`. Excluding initial "Ra,Halant" sequences
that will become "Reph"s: 

  - If the consonant has a below-base form, tag it as
          `POS_BELOWBASE_CONSONANT`. 
  - Otherwise, tag it as `POS_PREBASE_CONSONANT`.
  
> Note: Shaping engines may choose any method to identify consonants that
> have below-base, post-base, or pre-base-reordering forms while
> executing the above algorithm. For example, one implementation may
> choose to maintain a static table of special-form consonants to
> compare against the text run. Another implementation might examine
> the active font to see if it includes a `blwf`, `pstf`, or `pref`
> lookup in the GSUB table that affects the consonants encountered in
> the syllable.
>
> However, checking for GSUB support ensures that the expected
> behavior is implemented in the active font, and is therefore the
> most reliable approach.

#### 2.6: Reph ####

Sixth, initial "Ra,Halant" sequences that will become "Reph"s must be tagged with
`POS_RA_TO_BECOME_REPH`.

#### 2.7: Post-base consonants ####

Seventh, any non-base consonants that occur after a dependent vowel
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. Such
consonants will either be followed by a "Halant" glyph or will be in
the `CONSONANT_DEAD` shaping class. 
	
  <!--- Double check: should this be "_Consonant_,Halant" instead of
        "Halant,_Consonant_"? --->
	
#### 2.8: Mark tagging ####

Eighth, all marks must be tagged. 

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.

Marks in the `BINDU`, `VISARGA`, `AVAGRAHA`, `CANTILLATION`,
`SYLLABLE_MODIFIER`, `GEMINATION_MARK`, and `SYMBOL` categories should
be tagged with `POS_SMVD`. 

All "Nukta"s must be tagged with the same positioning tag as the
preceding consonant, independent vowel, placeholder, or dotted circle.

All remaining marks (not in the `POS_SMVD` category and not "Nukta"s)
must be tagged with the same positioning tag as the closest non-mark
character the mark has affinity with, so that they move together 
during the sorting step.

There are two possible cases: those marks before the syllable base
and those marks after the syllable base.

  1. Initially, all remaining marks should be tagged with the same
  positioning tag as the closest preceding consonant.

  2. For each consonant after the syllable base (such as post-base
  consonants, below-base consonants, or final consonants), all
  remaining marks located between that current consonant and any
  previous consonant should be tagged with the same positioning tag as
  the current (later) consonant.
  
In other words, all consonants preceding the syllable base "own" the
marks that follow them, while all consonants after the syllable base
"own" the marks that come before them. When a syllable does not have
any consonants after the syllable base, the syllable base should
"own" all the marks that follow it.

<!--- EXCEPTION: Uniscribe does NOT move a halant with a preceding -->
<!--left-matra. HarfBuzz follows suit, for compatibility reasons. --->

<!--- HarfBuzz also tags everything between a post-base consonant or -->
<!--matra and another post-base consonant as belonging to the latter -->
<!--post-base consonant. --->


#### 2.9: Sort syllable ####

With these steps completed, the syllable can be sorted into the final
sort order as listed at the beginning of stage 2.

The glyphs in the syllable should be sorted in stable order,
so that glyphs of the same ordering category remain in the same
relative position with respect to each other.


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
the base consonant or syllable base. Because multiple substitutions
may have occurred during the application of the basic-shaping features
in the preceding stage, these repositioning moves could not be
performed during the initial reordering stage.

Like the initial reordering stage, the steps involved in this stage
occur on a per-syllable basis.

<!--- Check that classifications have not been mangled. If the -->
<!--character is a Halant AND a ligature was formed AND a multiple
substitution was performed, restore the classification to VIRAMA
because it was almost certainly lost in the preceding GSUB stage.
--->

#### 4.1: Base consonant ####

The final reordering stage, like the initial reordering stage, begins
with determining the syllable base of each syllable, following the
same algorithm used in stage 2, step 1.

In a syllable that begins with an independent vowel, the independent
vowel will always serve as the syllable base. In a standalone sequence or
other syllable that begins with a placeholder or a dotted circle, the
placeholder or dotted circle will always serve as the syllable base.

In a syllable that begins with a consonant, the shaping engine must
repeat the base-consonant search algorithm used in stage 2, step 1.

The codepoint of the underlying base consonant or syllable base will
not change between the search performed in stage 2, step 1, and the
search repeated here. However, the application of GSUB shaping
features in stage 3 means that several ligation and many-to-one
substitutions may have taken place. The final glyph produced by that
process may, therefore, be a conjunct or ligature form — in most
cases, such a glyph will not have an assigned Unicode codepoint.
   
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
consonant or syllable base, all conjuncts or ligatures that contain
the base consonant or syllable base, and all half forms.

#### 4.3: Reph ####

"Reph" must be moved from the beginning of the syllable to its final
position. The correct final position depends on the script's
Reph-position shaping characteristic, and is conditional upon the
presence or absence of certain characters (such as post-base
consonants or "matra,Halant" sequences) in the syllable. 

The full algorithm for determining the final Reph position has seven steps.

(a) If the script uses Reph-position rule `REPH_POS_AFTER_POST`, jump
immediately to step (e). Otherwise, proceed to step (b).

(b) Find the first explicit "Halant" between the syllable base
consonant and the first post-Reph consonant. If there is a ZWJ or ZWNJ
following this "Halant", move the "Reph" to a position immediately
after the ZWJ or ZWNJ, then proceed to step (mH). Otherwise, move the
"Reph" to a position immediately after the "Halant", then proceed to
step (mH). If no such explicit "Halant" is found, proceed to step
(c).

(c) If the script uses Reph-position rule `REPH_POS_AFTER_MAIN`, find
the first consonant not ligated with the syllable base, and that is
not a potential pre-base reordering "Ra". If such a consonant is
found, move the "Reph" to a position immediately after the
consonant, then proceed to step (mH). If no such consonant is found,
proceed to step (d). If the script uses a different Reph-position
rule, proceed to step (d).

(d) If the script uses Reph-position rule `REPH_POS_BEFORE_POST`, find
the first post-base consonant not ligated with the syllable base. If
such a consonant is found, move the "Reph" to a position immediately
before the consonant, then proceed to step (mH). If no such consonant
is found, proceed to step (e). If the script uses a different
Reph-position rule, proceed to step (e).

(e) Move the "Reph" to a position immediately before the first
post-base matra, syllable modifier sign or Vedic sign that has a
reordering class after the intended Reph position in the syllable sort
order (as listed in [stage 2](#2-initial-reordering)). This will be
the final "Reph" position. , then proceed to step (mH). If no such
matra or sign is found, proceed to step (f).

(f) Move the "Reph" to the end of the syllable. 

(mH) Finally, if the "Reph" position arrived at in the preceding steps
is immediately after a "matra,Halant" sequence, move the "Reph" so
that it is before the "Halant". 


Taking the Reph-position–rule conditionals in the above algorithm into
account, the position-finding steps that may be executed in each
script are summarized in the following table:

| Script     | Reph-position rule        | a | b | c | d | e | f | mH |
|:-----------|:--------------------------|:--|:--|:--|:--|:--|:--|:---|
| Devanagari |`REPH_POS_BEFORE_POST`     |   | • |   | • | • | • | •  |
| Bengali    |`REPH_POS_AFTER_SUBJOINED` |   | • |   |   |   | • | •  |
| Gujarati   |`REPH_POS_BEFORE_POST`     |   | • |   | • | • | • | •  |
| Gurmukhi   |`REPH_POS_BEFORE_SUBJOINED`|   | • |   |   |   | • | •  |
| Kannada    |`REPH_POS_AFTER_POST`      |   |   |   |   | • | • | •  |
| Malayalam  |`REPH_POS_AFTER_MAIN`      |   | • | • |   | • | • | •  |
| Oriya      |`REPH_POS_AFTER_MAIN`      |   | • | • |   | • | • | •  |
| Tamil      |`REPH_POS_AFTER_POST`      |   |   |   |   | • | • | •  |
| Telugu     |`REPH_POS_AFTER_POST`      |   |   |   |   | • | • | •  |
| Sinhala    |`REPH_POS_AFTER_MAIN`      |   | • | • |   | • | • | •  |

#### 4.4: Pre-base reordering consonants ####

Any pre-base-reordering consonants must be moved to immediately before
the base consonant or syllable base.
  

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

## The old Indic shaping model ##


The older Indic script tags (`<deva>`, `<beng>`, `<gujr>`, `<guru>`, `<knda>`,
`<mlym>`, `<orya>`, `<taml>`, and `<telu>`) have been deprecated. However,
shaping engines may still encounter fonts that were built to work with
these tags and some users may still have documents that were written to
take advantage of the original shaping rules.

### Distinctions from the Indic2 model ###

The most significant distinction between the shaping models is that the
sequence of "Halant" and consonant glyphs used to trigger shaping
features) was altered when migrating from the old to the new shaping model. 

Specifically, shaping engines were expected to reorder post-base
"Halant,_Consonant_" sequences to "_Consonant_,Halant".

As a result, a font's GSUB substitutions would be written to match
"_Consonant_,Halant" sequences in all pre-base and post-base positions.


The old-model Indic syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In Indic2 text, as described above in this document, there is no
such reordering. The correct sequence to match for GSUB substitutions is
"_Consonant_,Halant" for pre-base consonants, but "Halant,_Consonant_"
for post-base consonants.

The old Indic shaping model also did not recognize the
`BLWF_MODE_PRE_AND_POST` shaping characteristic. Instead, all scripts
were treated as if they followed the `BLWF_MODE_POST_ONLY`
characteristic. In other words, below-base form substitutions were
only applied to consonants after the base consonant or syllable base.

In addition, left-side dependent vowel marks
(matras) were not repositioned during the final reordering
stage. For `<deva>`, `<beng>`, `<gujr>`, `<guru>`, `<knda>`,
`<orya>`, and `<telu>` text, the left-side matra was always positioned
at the beginning of the syllable. For `<mlym>` and `<taml>` text, the
left-side matra was positioned immediately before the base consonant or syllable base.


### Advice for handling fonts with old Indic features only ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences in order to apply GSUB substitutions when it is known that
the font in use supports only the old shaping model.

### Advice for handling text runs composed in the old Indic format ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences for GSUB substitutions or to reorder them to
"Halant,_Consonant_" when processing text runs that are tagged with
one of the old Indic script tags and it is known that the font in use supports
only the Indic2 shaping model.

Shaping engines may also choose to position left-side matras according
to the old-model Indic ordering scheme; however, doing so might interfere
with matching GSUB or GPOS features.
