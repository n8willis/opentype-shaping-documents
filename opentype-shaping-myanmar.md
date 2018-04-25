# Myanmar shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Myanmar script.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Myanmar character tables](#myanmar-character-tables)
  - [The `<mym2>` shaping model](#the-mym2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Applying all remaining substitution features from GSUB](#4-applying-all-remaining-substitution-features-from-gsub)
      - [5: Applying remaining positioning features from GPOS](#5-applying-remaining-positioning-features-from-gpos)
  - [The `<mymr>` shaping model](#the-mymr-shaping-model)
      - [Distinctions from `<mym2>`](#distinctions-from-mym2)
      - [Advice for handling fonts with `<mymr>` features only](#advice-for-handling-fonts-with-mymr-features-only)
      - [Advice for handling text runs composed in `<mymr>` format](#advice-for-handling-text-runs-composed-in-mymr-format)


## General information ##

The Myanmar or Burmese script is a descendant of the Brahmi script, and follows
many of the same general patterns found in [Indic
scripts](opentype-shaping-indic-general.md). However, Myanmar
incorporates enough distinctions of its own that it is generally not
advisable to attempt supporting it in a general-purpose Indic shaping engine.

The Myanmar script is used to write multiple languages, most commonly
Burmese, Mon, Karen, Kayah, Shan, Palaung, and Pali. In addition,
Sanskrit may be written in Myanmar, so Myanmar script runs may include 
glyphs from the Vedic Extension block of Unicode. 

There are two extant Myanmar script tags defined in OpenType, `<mymr>`
and `<mym2>`. The older script tag, `<mymr>`, was deprecated in 2005.
Therefore, new fonts should be engineered to work with the `<mym2>`
shaping model. However, if a font is encountered that supports only
`<mymr>`, the shaping engine should deal with it gracefully.

## Terminology ##

OpenType shaping uses a standard set of terms for Brahmi-derived and
Indic scripts.  The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. Syllables
in Myanmar script can include sequences of multiple vowels and,
therefore, mutiple matras.

**Halant** and **Virama** are both standard terms for the below-base
"vowel-killer" mark. Unicode documents use the term "virama" most
frequently, while OpenType documents use the term "halant" most
frequently.

**Asat** is the term for the "pure killer" character in Myanmar. An
asat after a consonant serves a similar function as a halant by
supressing the inherent vowel of the consonant, but the asat is
rendered visually, either as an above-base mark or in a substitution
form triggered by an adjacent codepoint.

An asat may be placed following a consonant to denote that the
consonant is doubled. An asat may also be followed by a halant, a
sequence that is used to trigger the "Kinzi" special form.

**Chandrabindu** (or simply **Bindu**) is the standard term for the
diacritical mark indicating that the preceding vowel should be
nasalized. Myanmar script does not use a chandrabindu; however, the
_BINDU_ category is used for other marks during the
syllable-identification stage in order to maintain compatibility with
other scripts. 

**Tone markers** are an important part of languages written in Myanmar
script. These markers may be either spacing-combining (`[Mc]`) or
non-spacing (`[Mn]`). Several tone markers may be used within a single
syllable.

The term **base consonant** is also critical to Myanmar shaping. The
base consonant of a syllable is the consonant that carries the
syllable's vowel sound, either the inherent vowel (for an unmarked
base consonant) or a dependent vowel (with the addition of a matra). 

A syllable's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
syllable frequently take on secondary forms. Different GSUB
substitutions may apply to a script's **pre-base** and **post-base**
consonants. Some of these substitutions create **above-base** or
**below-base** forms. The **Kinzi** form of certain consonants is an
example, akin to the "Reph" form of "Ra" in many Indic scripts.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Myanmar text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark. 

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Myanmar glyphs must additionally be classified by how they are treated
when shaping a run of text.

### Shaping classes and subclasses ###

The shaping classes listed in the tables that follow are defined so
that they capture the positioning rules used by Myanmar script. 

For most codepoints, the _Shaping class_ is synonymous with the `Indic
Syllabic Category` defined in Unicode. However, there are some
distinctions, where the defined category does not fully capture the
behavior of the character in the shaping process.

Several of the diacritic and syllable-modifying marks behave according
to their own rules and, thus, have a special class. These include
`BINDU`, `VISARGA`, `AVAGRAHA`, and `VIRAMA`. Some
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

Myanmar uses one subclass of consonant, `CONSONANT_MEDIAL`. This
subclass is used for special non-base variants of several consonants that
serve to modify the syllable's vowel sound. These medial consonants
are rendered as non-spacing marks attached to the base consonant.

> Note: The medial "Ra" is reordered to pre-base-consonant
> position. The other medial consonants do not require reordering.

> Note: The medial consonants are encoded in separate codepoints,
> distinguishing them from the standard (non-medial) variant of the
> corresponding consonant. 

In addition, the Myanmar and Myanmar Extended Unicode blocks include
several codepoints classified as `CONSONANT_PLACEHOLDER`. These
codepoints are used in verbal transcriptions to take tone
marks. However, these glyphs are not consonants in the true sense and
are unlikely to occur within normal words.

Other characters, such as symbols, need no special
attention from the shaping engine, so they are not assigned a shaping
class.

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
with `LEFT_POSITION`, must frequently be reordered. Therefore, the
`LEFT_POSITION` subclass of the character must be tracked throughout
the shaping process.

There are four basic _mark-placement subclasses_ for dependent vowels
(matras). Each corresponds to the visual position of the matra with
respect to the base consonant to which it is attached:

  - `LEFT_POSITION` matras are positioned to the left of the base consonant.
  - `RIGHT_POSITION` matras are positioned to the right of the base consonant.
  - `TOP_POSITION` matras are positioned above the base consonant.
  - `BOTTOM_POSITION` matras are positioned below base consonant.
  
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

For most mark and dependent-vowel codepoints, the _mark-placement
subclass_ is synonymous with the `Indic Positional Category` defined
in Unicode. However, there are some distinctions, where the defined
category does not fully capture the behavior of the character in the
shaping process. 

### Myanmar character tables ###

Separate character tables are provided for the Myanmar and Vedic
Extensions blocks as well as for other miscellaneous characters that
are used in `<mym2>` text runs:

  - [Myanmar character table](character-tables/character-tables-myanmar.md#myanmar-character-table)
  - [Myanmar Extended-A character table](character-tables/character-tables-myanmar.md#myanmar-extended-a-character-table)
  - [Myanmar Extended-B character table](character-tables/character-tables-myanmar.md#myanmar-extended-b-character-table)
  - [Vedic Extensions character table](character-tables/character-tables-myanmar.md#vedic-extensions-character-table)
  - [Miscellaneous character table](character-tables/character-tables-myanmar.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+1000`   | Letter           | CONSONANT         | _null_                     | &#x1000; Ka                  |
| | | | |
|`U+1036`   | Mark [Mn]        | BINDU             | TOP_POSITION
|| &#x1036; Anusvara          |


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
of Myanmar text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

The zero-width joiner is primarily used to prevent the formation of a
subjoining form from a "_Consonant_,Halant,_Consonant_" sequence. The sequence
"_Consonant_,Halant,ZWJ,_Consonant_" blocks the substitution of a
subjoined form for the second consonant. 

<!---
A secondary usage of the zero-width joiner is to prevent the formation of
"Reph". An initial "Ra,Halant,ZWJ" sequence should not produce a "Reph",
where an initial "Ra,Halant" sequence without the zero-width joiner
otherwise would.
--->

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (marks, dependent vowels (matras),
below-base consonant forms, and post-base consonant forms) in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder. These sequences will match
"NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".




## The `<mym2>` shaping model ##

Processing a run of `<mym2>` text involves six top-level stages:

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Applying all remaining substitution features from GSUB
5. Applying all remaining positioning features from GPOS


As with other Brahmic and Indic scripts, the initial reordering stage and the
final reordering stage each involve applying a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.


Myanmar exhibits many of the same shaping patterns found in Indic
scripts, but it differs in a few critical characteristics. With regard
to these common variations, Myanmar's specific shaping 
characteristics include:


  - The first consonant of a syllable is always the base consonant,
    excluding a consonant that is part of an initial "Kinzi"-forming
    sequence (if it is present).

> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `BASE_POS_FIRST`.
  
  - "Kinzi" is always encoded as a syllable-initial sequence, but it
    is reordered. The final position of "Kinzi" is immediately after
    the base consonant. 

> Note: For comparison with the General Indic shaping model, the Kinzi
> -encoding characteristic would correspond to `REPH_MODE_EXPLICIT`,
> and the reordering characteristic would correspond to `POS_AFTER_MAIN`.
  
  - The below-base forms feature is applied only to consonants
    before the base consonant. 

> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `BLWF_MODE_POST_ONLY`.

  - Medial Ra is reordered to pre-base position.

  - Pre-base matras are reordered to the beginning of the
    syllable. Multiple pre-base matras can occur; any such sequences
    must be moved together, as a block, at the reordering stage.

> Note: For comparison with the General Indic shaping model, this
> characteristic is distinct to Mynanmar script. Indic scripts apply 
> different reordering rules to pre-base matras that depend on the
> syllable's content.

	
  - The ordering positions for right-side, above-base, and below-base
    matras is the same. All are reorderd to immediately after all
    subjoined consonants.
	
> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `MATRA_POS_TOP`,
> `MATRA_POS_RIGHT`, and `MATRA_POS_BOTTOM` all taking the ordering
> position `POS_AFTER_SUBJOINED`.



### 1: Identifying syllables and other sequences ###

A syllable in Myanmar consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Myanmar Unicode block enumerates two modifier signs,
> "Anusvara" (`U+1036`) and "Visarga" (`U+1038`). There are also
> twenty-one tone markers in the Myanmar and Myanmar Extended-A
> blocks. In addition, Sanskrit text written in Myanmar may include
> additional signs from Vedic Extensions block.

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

Generally speaking, the base consonant is the first consonant of the
syllable and its vowel sound designates the end of the syllable. The
exception to this rule is consonants that are part of a
"Kinzi"-triggering sequence.

Post-base consonants in a valid syllable will be preceded by "Halant"
marks. 

	BaseC Halant Post-baseC
	
The algorithm for correctly identifying the base consonant includes a
test to recognize these sequences and not mis-identify the base
consonant.

Medial consonants will not be preceded by a "Halant". 

> Note: in the Myanmar script, all medial consonants have their own
> distinct codepoints. Therefore, they can be identfied by codepoint
> alone, and there is no need for a text run to identify them using
> any special sequences.


As with other Brahmic and Indic scripts, the consonant "Ra" receives
special treatment. 

  - A "Medial Ra" (`U+103C`) must be reordered to a position immediately
    before the syllable's base consonant. 
	
	Note, however, that "Medial Ra" is a separate codepoint from the
    standard "Ra" (`U+101B`). 
	
  - A syllable-initial "Ra" may be part of a "Kinzi"-triggering
    sequence. 
	
	Notably, however, although "Ra" alone will take on the "Reph" form
    in Indic scripts, the Myanmar script's "Kinzi" feature can be
    triggered for three consonants: "Ra" (`U+101B`), "Nga" (`U+1004`),
    and "Mon Nga" (`U+105A`). In each case, the "Kinzi" form is
    triggered by an explicit sequence: the consonant, followed by
    "Asat,Halant".
	
	There are, therefore, exactly three "Kinzi"-forming sequences to
    test for:
	  - "Ra,Asat,Halant"
	  - "Nga,Asat,Halant"
	  - "Mon Nga,Asat,Halant"
  


In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Myanmar script, may
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

The following regular expressions can be used to match Myanmar-script
syllables. 

The regular expressions utilize the shaping classes from the tables
above. For the purpose of syllable identification, more general
classes can be used, as defined in the following table. This
simplifies the resulting expressions. 

    _consonant_ = `CONSONANT` | `CONSONANT_PLACEHOLDER`
	_vowel_		= `VOWEL_INDEPENDENT`
    _ra_		= "Ra" | "Nga" | "Mon Nga"
    _halant_	= `INVISIBLE_STACKER`
	_asat_		= "Asat"
	_a_			= `ANUSVARA`
	_db_		= "Dot Below"
	_zwj_		= `JOINER`
	_zwnj_		= `NON_JOINER`
	_mh_		= "Medial Ha" | "Mon Medial La"
	_mr_		= "Medial Ra"
	_mw_		= "Medial Wa" | "Shan Medial Wa"
	_my_		= "Medial Ya" | "Mon Medial Na" | "Mon Medial Ma"
	_d_			= `NUMBER`
	_pt_		= "Tone Sgaw Karen Hathi" | "Tone Sgaw Karen Ke Pho" |
	              "Western Pwo Karen Tone 1" | "Western Pwo Karen Tone
				  2" | "Western Pwo Karen Tone 3" | "Western Pwo Karen
				  Tone 4" | "Western Pwo Karen Tone 5" | "Pao Karen
				  Tone" 
	_sm_		= "Visarga" | "Shan Tone 2" | "Shan Tone 3" | "Shan
	              Tone 5" | "Shan Tone 6" | "Shan Council Tone 2" |
				  "Shan Council Tone 3" | "Shan Council Emphatic Tone"
				  | "Rumai Palaung Tone 5" | "Khamti Tone 1" | "Khamti
				  Tone 3" | "Aiton A" 
    _punc_			= "Little Section" | "Section"
	_matrapre_	= `MATRA`,`LEFT_POSITION`
	_matrapost_	= `MATRA`,`RIGHT_POSITION`
	_matraabove_	= `MATRA`,`TOP_POSITION`
	_matrabelow_	= `MATRA`,`BOTTOM_POSITION`
	_gb_		= U+002D | 00A0 | 00D7 | 2012 | 2013 | 2014 | 2015 |
				  2022 | 25CC | 25FB | 25FC 25FD | 25FE
	_cs_		= `CONSONANT_WITH_STACKER`
	_v_			= `VISARGA`


> Note: the _ra_ identification class is mutually exclusive with 
> the _consonant_ class. The union of the _consonant_ and _ra_ classes
> is used in the regular expression elements below in order to
> correctly identify "Ra", "Nga", and "Mon Nga" characters that do not
> trigger "Kinzi" forms. 
>
> Note, also, that the `CONSONANT_PLACEHOLDER` class is unioned with
> the `CONSONANT` class for the purpose of syllable identification,
> even those these two classes should remain separate in general.

> Note: the _gb_ identification class includes several "generic base"
> codepoints that are often used in real-world text runs to act as
> placeholders for missing letters.

> Note: the tone marker codepoints are divided up between two
> identification classes, reflecting the differeing orthographic rules
> they follow. The _pt_ identification class constitutes the "Pwo
> tone" markers, while the _sm_ identification class includes the
> remaining tone markers and other syllable modifiers.

These idenfication classes form the bases of the following regular
expression elements:

    C	= (_consonant_ | _ra_)
	Z	= (_zwj_ | _zwnj_)
	K	= _ra_ _asat_ _halant_
	Med	= _my_? _mr_? _mw_? _mh_? _asat_?
	Vmain	= _matrapre_* _matraabove_* _matrabelow_* _a_* (_db_ _asat_?)?
	Vpost	= _matrapost_ _mh_? _asat_* _matraabove_* _a_* (_db_ _asat_?)?
    Pwo	= _pt_ _a_* _db_? _asat_?
    	
    Tcomplex	= _asat_* Med Vmain Vpost* Pwo* _v_* Z?
	Tail		= (_halant_ | Tcomplex)
	
Using the above elements, the following regular expressions define the
possible syllable types:

A consonant-based syllable will match the expression:
```
(K | _cs_)? (C | _vowel_ | _d_ | _gb_)._vs_? (_halant_ (C | _vowel_)._vs_?)* Tail
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
> treatment in some circumstances. "Ba", "Ta", and "Ya" occasionally
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
	
<!---	POS_PREBASE_CONSONANT --->

	POS_BASE_CONSONANT
	POS_AFTER_MAIN

<!---	POS_ABOVEBASE_CONSONANT --->

	POS_BEFORE_SUBJOINED
	POS_BELOWBASE_CONSONANT
	POS_AFTER_SUBJOINED

	POS_BEFORE_POST
	POS_POSTBASE_CONSONANT
	POS_AFTER_POST

<!---	POS_FINAL_CONSONANT --->
<!---	POS_SMVD --->

<!--- question: does Myanmar shape handle Vedic signs differently? --->
<!--- or am I looking at an incomplete version of the reordering --->
<!--- logic? --->


This sort order enumerates all of the possible final positions to
which a codepoint might be reordered in Myanmar script. 

The basic positions (left to right) are dependent
vowels (matras) and consonants positioned before the base
consonant (`POS_PREBASE_MATRA` and `POS_PREBASE_CONSONANT`), the base
consonant (`POS_BASE_CONSONANT`), below-base consonants
(`POS_BELOWBASE_CONSONANT`), consonants positioned after the base consonant
(`POS_POSTBASE_CONSONANT`), 
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

Vowel-based syllables, stand-alone sequences, and broken text runs will
not have base consonants.

The algorithm for determining the base consonant is

  - Starting from the beginning of the syllable, move forwards until a
    `CONSONANT` is found. 
      * If the consonant is part of a "Kinzi" sequence, move to the
        next consonant. 
  - The consonant stopped at will be the base consonant.

> Note: The algorithm considers only `CONSONANT` class consonants, 


#### 2.2: Tag matras ####

Third, all left-side dependent-vowel (matra) signs must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

All right-side, above-base, and below-base dependent-vowel (matra)
signs are tagged `POS_AFTER_SUBJOINED`.

For simplicity, shaping engines may choose to tag matras
in an earlier text-processing step, using the information in the
_Mark-placement subclass_ column of the character tables. It is
critical at this step, however, that all matras correctly tagged
before proceeding to the next step. 

#### 2.3: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. 

For `<mym2>` text, the canonical ordering means that any "Nukta"s must
be placed before all other marks. No other marks in the subsequence
should be reordered.

<!--- MS spec says Anusvara must be reordered to immediately before -->
<!--  right-side vowels.... What to do? --->


#### 2.5: Kinzi ####

Sixth, initial "Kinzi"-triggering sequences that will become "Kinzi"s
must be tagged with `POS_RA_TO_BECOME_REPH`.

The sequences are:

  - "Ra,Asat,Halant"
  - "Nga,Asat,Halant"
  - "Mon Nga,Asat,Halant"
  

#### 2.6: Post-base consonants ####

Seventh, any non-base consonants that occur after a dependent vowel
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. Such
consonants will usually be preceded by a "Halant" glyph. 



<!---  Not sure about Yya.... --->
	
#### 2.7: Mark tagging ####

Eighth, all marks must be tagged with the same positioning tag as the
closest non-mark character the mark has affinity with, so that they move together
during the sorting step.

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
	ccmp
	rphf 
	pref 
	blwf 
	pstf

#### 3.1 locl ####

The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> GSUB substitutions in the following steps.


#### 3.2: ccmp ####




#### 3.3: rphf ####

The `rphf` feature replaces initial "Kinzi"-triggering sequences with
the "Kinzi" glyph. The sequences are:

  - "Ra,Asat,Halant"
  - "Nga,Asat,Halant"
  - "Mon Nga,Asat,Halant"

![Kinzi composition](/images/myanmar/myanmar-rphf.png)


#### 3.4 pref ####

The `pref` feature replaces pre-base-consonant glyphs with
any special forms.

#### 3.5: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Myanmar includes two below-base consonant
forms:

  - "Halant,Ra" (after the base consonant) and "Ra,Halant" (in a
    non-syllable-initial position) take on the "Raphala" form.
  - "Ba,Halant" (before the base consonant) and "Halant,Ba" (after the
    base consonant) take on the "Baphala" form. 

Because Myanmar incorporates the `BLWF_MODE_PRE_AND_POST` shaping
characteristic, any pre-base consonants and any post-base consonants
may potentially match a `blwf` substitution; therefore, both cases must
be tagged for comparison. Note that this is not necessarily the case in other
Indic scripts that use a different `BLWF_MODE_` shaping
characteristic. 


![Raphala composition](/images/myanmar/myanmar-raphala.png)

![Baphala composition](/images/myanmar/myanmar-baphala.png)


#### 3.6: pstf ####

The `pstf` feature replaces post-base-consonant glyphs with any special forms.

![Yaphala composition](/images/myanmar/myanmar-yaphala.png)





### 4: Applying all remaining substitution features from GSUB ###

In this stage, the remaining substitution features from the GSUB table
are applied. The order in which these features are applied is not
canonical; they should be applied in the order in which they appear in
the GSUB table in the font. 

	pres
	abvs
	blws
	psts
	liga


The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include consonant conjuncts, half-form
consonants, and stylistic variants of left-side dependent vowels
(matras). 

![Application of the pres feature](/images/myanmar/myanmar-pres.png)


The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

![Application of the abvs feature](/images/myanmar/myanmar-abvs.png)


The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually includes replacing base consonants that
are adjacent to below-base-consonant forms like "Raphala" or
"Baphala" with contextual ligatures.

![Application of the blws feature](/images/myanmar/myanmar-blws.png)


The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures.

![Application of the psts feature](/images/myanmar/myanmar-psts.png)


The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.

![Application of the liga feature](/images/myanmar/myanmar-liga.png)



### 5: Applying remaining positioning features from GPOS ###

In this stage, mark positioning, kerning, and other GPOS features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the GPOS table in the font.

        dist
        abvm
        blwm

> Note: The `kern` feature is usually applied at this stage, if it is
> present in the font. However, `kern` is not mandatory for shaping
> Myanmar text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

In Myanmar text, `dist` is typically used to adjust the space of a
consonant glyph after a pre-base-reordering "Medial Ra", because the
"Medial Ra" codepoint is classified as being of zero width.

![Application of the dist feature](/images/myanmar/myanmar-dist.png)


The `abvm` feature positions above-base marks for attachment to base
characters. In Myanmar, this includes "Reph" in addition to the
diacritical marks and Vedic signs. 

![Application of the abvm feature](/images/myanmar/myanmar-abvm.png)

The `blwm` feature positions below-base marks for attachment to base
characters. In Myanmar, this includes below-base dependent vowels
(matras) as well as the below-base consonant forms "Raphala" and
"Baphala".

![Application of the blwm feature](/images/myanmar/myanmar-blwm.png)


## The `<mymr>` shaping model ##

The older Myanmar script tag, `<mymr>`, has been deprecated. However,
shaping engines may still encounter fonts that were built to work with
`<mymr>` and some users may still have documents that were written to
take advantage of `<mymr>` shaping.

### Distinctions from `<mym2>` ###

The most significant distinction between the shaping models is that the
sequence of "Halant" and consonant glyphs used to trigger shaping
features was altered when migrating from `<mymr>` to
`<mym2>`. 

Specifically, shaping engines were expected to reorder post-base
"Halant,_Consonant_" sequences to "_Consonant_,Halant".

As a result, a font's GSUB substitutions would be written to match
"_Consonant_,Halant" sequences in all pre-base and post-base positions.


The `<mymr>` syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In `<mym2>` text, as described above in this document, there is no
such reordering. The correct sequence to match for GSUB substitutions is
"_Consonant_,Halant" for pre-base consonants, but "Halant,_Consonant_"
for post-base consonants.

In addition, for some scripts, left-side dependent vowel marks
(matras) were not repositioned during the final reordering
stage. For `<mymr>` text, the left-side matra was always positioned
at the beginning of the syllable.


### Advice for handling fonts with `<mymr>` features only ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences in order to apply GSUB substitutions when it is known that
the font in use supports only the `<mymr>` shaping model.

### Advice for handling text runs composed in `<mymr>` format ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences for GSUB substitutions or to reorder them to
"Halant,_Consonant_" when processing text runs that are tagged with
the `<mymr>` script tag and it is known that the font in use supports
only the `<mym2>` shaping model.

Shaping engines may also choose to position left-side matras according
to the `<mymr>` ordering scheme; however, doing so might interfere
with matching GSUB or GPOS features.







locl
ccmp

Basic features
rphf
pref
blwf
pstf

liga

other features
pres
abvs
blws
psts

gpos features
dist
abvm
blwm
mark
mkmk
