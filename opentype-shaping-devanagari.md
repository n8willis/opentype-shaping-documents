# Devanagari shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Devanagari script.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Devanagari character tables](#devanagari-character-tables)
  - [The `<dev2>` shaping model](#the-dev2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The `<deva>` shaping model](#the-deva-shaping-model)
      - [Distinctions from `<dev2>`](#distinctions-from-dev2)
      - [Advice for handling fonts with `<deva>` features only](#advice-for-handling-fonts-with-deva-features-only)
      - [Advice for handling text runs composed in `<deva>` format](#advice-for-handling-text-runs-composed-in-deva-format)


## General information ##

The Devanagari script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
sequences of adjacent consonants are often represented as conjuncts.

The Devanagari script is used to write multiple languages, most commonly
Hindi, Marathi, Maithili, and Nepali. In addition, Sanskrit may be written
in Devanagari, so Devanagari script runs may include glyphs from the Vedic
Extensions block of Unicode. 

There are two extant Devanagari script tags defined in OpenType, `<deva>`
and `<dev2>`. The older script tag, `<deva>`, was deprecated in 2005.
Therefore, new fonts should be engineered to work with the `<dev2>`
shaping model. However, if a font is encountered that supports only
`<deva>`, the shaping engine should deal with it gracefully.

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. 

The term "matra" is also used to refer to the headline above most
Devanagari letters. To avoid ambiguity, the term **headline** is
used in most Unicode and OpenType shaping documents.

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. 

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
example.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Devanagari text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark.

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Devanagari glyphs must additionally be classified by how they are treated
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

### Devanagari character tables ###

Separate character tables are provided for the Devanagari, Devanagari
Extended, and Vedic Extensions block as well as for other
miscellaneous characters that are used in `<dev2>` text runs:

  - [Devanagari character table](character-tables/character-tables-devanagari.md#devanagari-character-table)
  - [Devanagari Extended character table](character-tables/character-tables-devanagari.md#devanagari-extended-character-table)
  - [Vedic Extensions character table](character-tables/character-tables-devanagari.md#vedic-extensions-character-table)
  - [Miscellaneous character table](character-tables/character-tables-devanagari.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0901`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0901; Candrabindu         |
| | | | |
|`U+0915`   | Letter           | CONSONANT         | _null_                     | &#x0915; Ka                  |



Codepoints with no assigned meaning are designated as _unassigned_ in
the _Unicode category_ column.

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
of Devanagari text include the dotted-circle placeholder (`U+25CC`), the
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




## The `<dev2>` shaping model ##

Processing a run of `<dev2>` text involves six top-level stages:

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

With regard to these common variations, Devanagari's specific shaping
characteristics include: 

  - `BASE_POS_LAST` = The base consonant of a syllable is the last
     consonant, not counting any special final-consonant forms.

  - `REPH_POS_BEFORE_POST` = "Reph" is ordered before all post-base consonant forms.

  - `REPH_MODE_IMPLICIT` = "Reph" is formed by an initial "Ra,Halant" sequence.

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

A syllable in Devanagari consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Devanagari Unicode block enumerates nine modifier signs,
> "Inverted Candrabindu" (`U+0900`), "Candrabindu" (`U+0901`),
> "Anusvara" (`U+0902`), "Visarga" (`U+0903`), "Avagraha" (`U+093D`),
> "Udatta" (`U+0951`), "Anudatta" (`U+0952`), "Grave Accent"
> (`U+0953`) and "Acute Accent" (`U+0954`). In addition, Sanskrit text
> written in Devanagari may include additional signs from Vedic
> Extensions block. 

Each syllable contains exactly one vowel sound. Valid syllables may
begin with either a consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that independent vowel
is the syllable's only vowel sound and serves as the "base". 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

From the shaping engine's perspective, the main distinctions between a
syllable with a base consonant and a syllable with an
independent-vowel base are that a syllable with a base consonant may
also contain multiple other consonants, including consonants that take
on special forms depending on where in the syllable they
appear, and that a syllable with an independent-vowel base will not
include any depedendent vowel signs (matras).

Because of these distinctions, consonant-based syllables require
significantly more processing than vowel-based syllables. 

> Note: Shaping engines may choose to treat independent-vowel bases
> like base consonants for the sake of simplicity or code
> reuse.
>
> Because valid vowel-based syllables are generally simpler,
> processing a vowel-based syllable should follow all of the logic
> described for consonant-based syllables in the steps that follow,
> but only trigger actions where mark-handling is involved.
>
> Implementations taking this approach, however, should recognize that
> making guarantees about the correctness of the results or about
> language-specific tests is out of scope for this document.

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

As with other Indic scripts, the consonant "Ra" receives special
treatment; in many circumstances it is replaced by one of two combining
mark-like forms. 

  - A "Ra,Halant" sequence at the beginning of a syllable
    is replaced with an above-base mark called "Reph" (unless the "Ra"
    is the only consonant in the syllable). 
    This rule is synonymous with the `REPH_MODE_IMPLICIT`
    characteristic mentioned earlier.

  - "Halant,Ra" sequences that occur elsewhere in the syllable may take on the
    below-base form "Rakaar." 
	
	
In addition, "Rra,Halant" sequences that precede the base consonant
may take on a form known as the "eyelash Ra." 

> Note: In `<dev2>` text runs, this substitution is canonically
> implemented as a [half form](#39-half). See the [`<deva>`
> shaping](#the-deva-shaping-model) section for a discussion of the
> "eyelash Ra" implementation that was used in the `<deva>` model.

"Reph" and "Rakaar" characters must be reordered after the
syllable-identification stage is complete. 

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

> Note: Foreign loanwords, when written in the Devanagari script, may
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
used to match Devanagari syllables. 

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
_symbol_	= `SYMBOL`
_avagraha_	= `AVAGRAHA`
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
SYLLABLE_TAIL	= (Z? _syllablemodifier_ _syllablemodifier_? _zwnj_?)? _avagraha_{0,3} _vedicsign_{0,2}
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


The shaping engine may make a best-effort attempt
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
> treatment in some circumstances. "Ra" and "Rra" may
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
Devanagari. 

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

> Note: For consistency with consonant-based syllables, shaping
> engines may choose to treat the independent vowel of a vowel-based
> syllable as a "pseudo-base" or surrogate base consonant.
>
> Because vowel-based syllables will not include consonants and
> because independent vowels do not take on special forms or require
> reordering, many of the steps that follow will involve no
> work for a vowel-based syllable. However, vowel-based syllables must
> still be sorted and their marks handled correctly, and GSUB and GPOS
> lookups must be applied. These steps of the shaping process follow
> the same rules that are employed for consonant-based syllables.


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


The algorithm for determining the base consonant is

  - If the syllable starts with "Ra" and the syllable contains
    more than one consonant, exclude the starting "Ra" from the list of
    consonants to be considered. 
  - Starting from the end of the syllable, move backwards until a consonant is found.
      * If the consonant is the first consonant, stop.
      * If the consonant has a below-base form, tag it as
        `POS_BELOWBASE_CONSONANT`, then move to the previous consonant. 
      * If the consonant has a post-base form, tag it as
        `POS_POSTBASE_CONSONANT`, then move to the previous consonant. 
      * If the consonant is a pre-base-reordering "Ra", tag it as
        `POS_POSTBASE_CONSONANT`, then move to the previous consonant. 
      * If none of the above conditions is true, stop.
  - The consonant stopped at will be the base consonant.

> Note: The algorithm is designed to work for all Indic
> scripts. However, Devanagari does not utilize pre-base-reordering "Ra".

Devanagari includes one below-base consonant form.

  - Halant,Ra" (occurring after the base consonant) and "Ra,Halant"
    (before the base consonant, but in a non-syllable-initial
    position) will take on the "Rakaar" form. 
	
> Note: the sequence "Rra,Halant" (occurring before the base
> consonant) will take on the "eyelash Ra" special form. However, this
> special form is not a below-base form. Instead, it is canonically
> defined as belonging to the half-form substitutions, so it is
> addressed by the `half` feature in stage 3, step 9, and is not
> addressed in this step.

> Note: Because Devanagari employs the `BLWF_MODE_PRE_AND_POST` shaping
> characteristic, consonants with below-base special forms may occur
> before or after the base consonant. 
> 
> During the base-consonant search, only the "Halant,_consonant_" 
> pattern following the base consonant for these below-base forms will
> be encountered. Step 2.5 below ensures that the "_consonant_,Halant"
> pattern preceding the base consonant for these below-base forms will
> also be tagged correctly.


#### 2.2: Matra decomposition ####

Second, any two-part dependent vowels (matras) must be decomposed
into their left-side and right-side components. 

Devanagari does not have any two-part dependent vowels; this step is
listed here because it is part of the general processing scheme for
shaping Indic scripts.

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.

#### 2.3: Tag matras ####

Third, all left-side dependent-vowel (matra) signs must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

Above-base, right-side, and below-base dependent-vowel (matra) signs
must be tagged with `POS_AFTER_SUBJOINED`.

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

Fifth, consonants that occur before the base consonant must be tagged
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

Devanagari includes one below-base consonant form.

  - Halant,Ra" (occurring after the base consonant) and "Ra,Halant"
    (before the base consonant, but in a non-syllable-initial
    position) will take on the "Rakaar" form. 
	
> Note: the sequence "Rra,Halant" (occurring before the base
> consonant) will take on the "eyelash Ra" special form. However, this
> special form is not a below-base form. Instead, it is canonically
> defined as belonging to the half-form substitutions, so it is
> addressed by the `half` feature in stage 3, step 9, and is not
> addressed in this step.

> Note: Because Devanagari employs the `BLWF_MODE_PRE_AND_POST` shaping
> characteristic, consonants with below-base special forms may occur
> before or after the base consonant. 
> 
> During the base-consonant search in 2.1, any instances of the
> "Halant,_consonant_"  pattern following the base consonant for these
> below-base forms will be encountered. The tagging in this step
> ensures that the "_consonant_,Halant" pattern preceding the base
> consonant for these below-base forms will also be tagged correctly.


#### 2.6: Reph ####

Sixth, initial "Ra,Halant" sequences that will become "Reph"s must be tagged with
`POS_RA_TO_BECOME_REPH`.

> Note: an initial "Ra,Halant" sequence will always become a "Reph"
> unless the "Ra" is the only consonant in the syllable.

#### 2.7: Final consonants ####

Seventh, all final consonants must be tagged. Consonants that occur
after the base consonant _and_ after a dependent vowel (matra) sign
must be tagged with  `POS_FINAL_CONSONANT`.

> Note: Final consonants occur only in Sinhala and should not be
> expected in `<dev2>` text runs. This step is included here to
> maintain compatibility across Indic scripts.


#### 2.8: Mark tagging ####

Eighth, all marks must be tagged. 

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.

Marks in the `BINDU`, `VISARGA`, `AVAGRAHA`, `CANTILLATION`,
`SYLLABLE_MODIFIER`, `GEMINATION_MARK`, and `SYMBOL` categories should
be tagged with `POS_SMVD`. 

All "Nukta"s must be tagged with the same positioning tag as the
preceding consonant.

All remaining marks (not in the `POS_SMVD` category and not "Nukta"s)
must be tagged with the same positioning tag as the closest non-mark
character the mark has affinity with, so that they move together 
during the sorting step.

There are two possible cases: those marks before the base consonant
and those marks after the base consonant.

  1. Initially, all remaining marks should be tagged with the same
  positioning tag as the closest preceding consonant.

  2. For each consonant after the base consonant (such as post-base
  consonants, below-base consonants, or final consonants), all
  remaining marks located between that current consonant and any
  previous consonant should be tagged with the same positioning tag as
  the current (later) consonant.
  
In other words, all consonants preceding the base consonant "own" the
marks that follow them, while all consonants after the base consonant
"own" the marks that come before them. When a syllable does not have
any consonants after the base consonant, the base consonant should
"own" all the marks that follow it.

With these steps completed, the syllable can be sorted into the final sort order.

<!--- EXCEPTION: Uniscribe does NOT move a halant with a preceding -->
<!--left-matra. HarfBuzz follows suit, for compatibility reasons. --->

<!--- HarfBuzz also tags everything between a post-base consonant or -->
<!--matra and another post-base consonant as belonging to the latter -->
<!--post-base consonant. --->


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
	pref (not used in Devanagari)
	blwf 
	abvf (not used in Devanagari)
	half
	pstf
	vatu
	cjct
	cfar (not used in Devanagari)

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

![Nukta composition](/images/devanagari/devanagari-nukt.png)



#### 3.3: akhn ####

The `akhn` feature replaces two specific sequences with required ligatures. 

  - "Ka,Halant,Ssa" is substituted with the "KSsa" ligature. 
  - "Ja,Halant,Nya" is substituted with the "JNya" ligature. 
  
These sequences can occur anywhere in a syllable. The "KSsa" and
"JNya" characters have orthographic status equivalent to full
consonants in some languages, and fonts may have `cjct` substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.


![KSsa ligation](/images/devanagari/devanagari-akhn-kssa.png)

![JNya ligation](/images/devanagari/devanagari-akhn-jnya.png)

#### 3.4: rphf ####

The `rphf` feature replaces initial "Ra,Halant" sequences with the
"Reph" glyph.

  - An initial "Ra,Halant,ZWJ" sequence, however, must not be tagged for
    the `rphf` substitution.
	

![Reph composition](/images/devanagari/devanagari-rphf.png)
	
#### 3.5 rkrf ####

The `rkrf` feature replaces "_Consonant_,Halant,Ra" sequences with the
"Rakaar"-ligature form of the consonant glyph.


![Rakaar composition](/images/devanagari/devanagari-rkrf.png)

#### 3.6 pref ####

> This feature is not used in Devanagari.

<!--- 3.5: The `pref` feature replaces pre-base-consonant glyphs with -->
<!--any special forms. --->

#### 3.7: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Devanagari includes one below-base consonant
form:

  - "Halant,Ra" (occurring after the base consonant) or "Ra,Halant"
    (before the base consonant, but in a non-syllable-initial position) will
    take on the "Rakaar" form.
	
If the active font contains ligatures for the consonant adjacent to
the "Halant" (i.e., "_Consonant_,Halant,Ra"), then that ligature is
normally applied with the `rkrf` feature in step 3.5. The `blwf`
feature allows the "Ra" to be substituted with a standalone "Rakaar"
mark, to work with all consonants that do not have a `rkrf` ligature
in the font.

Because Devanagari incorporates the `BLWF_MODE_PRE_AND_POST` shaping
characteristic, any pre-base consonants and any post-base consonants
may potentially match a `blwf` substitution; therefore, both cases must
be tagged for comparison. Note that this is not necessarily the case in other
Indic scripts that use a different `BLWF_MODE_` shaping
characteristic. 

![Below-base form](/images/devanagari/devanagari-blwf.png)

#### 3.8: abvf ####

> This feature is not used in Devanagari.

#### 3.9: half ####

The `half` feature replaces "_Consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs. There are
four exceptions to the default behavior, for which the shaping engine
must test:

  - Initial "Ra,Halant" sequences, which should have been tagged for
    the `rphf` feature earlier, must not be tagged for potential
    `half` substitutions.

  - Non-initial "Ra,Halant" sequences, which should have been tagged
    for the `rkrf` or `blwf` features earlier, must not be tagged for
    potential `half` substitutions.
  
  - A sequence matching "_Consonant_,Halant,ZWJ,_Consonant_" must be
    tagged for potential `half` substitutions, even though the presence of the
    zero-width joiner suppresses the `cjct` feature in a later step.

  - A sequence matching "_Consonant_,Halant,ZWNJ,_Consonant_" must not be
    tagged for potential `half` substitutions.

![Half-form formation](/images/devanagari/devanagari-half.png)

In addition, the sequence "Rra,Halant" (occurring before the base
consonant) will take on the "eyelash Ra" form. Because this
substitution is defined as the canonical half form of "Rra" in `<dev2>`, the
shaping engine does not need to implement any special handling to
support it. 

![Eyelash Ra formation](/images/devanagari/devanagari-eyelash-ra.png)

#### 3.10: pstf ####

> This feature is not used in Devanagari.


#### 3.11: vatu ####

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. 

"Vattu variants" are formed from glyphs followed by "Rakaar"
(the below-base form of "Ra"); therefore, this feature must be applied after
the `blwf` feature.

![Vattu ligation](/images/devanagari/devanagari-vatu.png)

#### 3.12: cjct ####

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match "_Consonant_,Halant,_Consonant_".

A sequence matching "_Consonant_,Halant,ZWJ,_Consonant_" or
"_Consonant_,Halant,ZWNJ,_Consonant_" must not be tagged to form a conjunct.

The font's GSUB rules might be implemented so that `cjct`
substitutions apply to half-form consonants; therefore, this feature
must be applied after the `half` feature. 

![Conjunct ligation](/images/devanagari/devanagari-cjct.png)

#### 3.13: cfar ####

> This feature is not used in Devanagari.


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

![Pre-base matra positioning](/images/devanagari/devanagari-matra-position.png)

#### 4.3: Reph ####

"Reph" must be moved from the beginning of the syllable to its final
position. Because Devanagari incorporates the `REPH_POS_BEFORE_POST`
shaping characteristic, this final position is immediately before any
independent post-base consonant forms (meaning the first post-base
consonant that has not formed a ligature with the base consonant).

  - If the syllable does not have any post-base consonants, then the
    final "Reph" position is immediately before the first post-base
    matra, syllable modifier, or Vedic sign.


![Reph positioning](/images/devanagari/devanagari-reph-position.png)

#### 4.4: Pre-base-reordering consonants ####

Any pre-base-reordering consonants must be moved to immediately before
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

	init (not used in Devanagari)
	pres
	abvs
	blws
	psts
	haln

The `init` feature is not used in Devanagari.

The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include consonant conjuncts, half-form
consonants, and stylistic variants of left-side dependent vowels
(matras). 

![Pre-base substitutions](/images/devanagari/devanagari-pres.png)

The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

![Above-base substitutions](/images/devanagari/devanagari-abvs.png)

The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually includes replacing base consonants that
are adjacent to the below-base-consonant form "Rakaar" with contextual
ligatures.

![Below-base substitutions](/images/devanagari/devanagari-blws.png)

The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures. 

![Post-base substitutions](/images/devanagari/devanagari-psts.png)

The `haln` feature replaces syllable-final "_Consonant_,Halant" pairs with
special presentation forms. This can include stylistic variants of the
consonant where placing the "Halant" mark on its own is
typographically problematic. 

![Halant substitutions](/images/devanagari/devanagari-haln.png)

> Note: The `calt` feature, which allows for generalized application
> of contextual alternate substitutions, is usually applied at this
> point. However, `calt` is not mandatory for correct Devanagari shaping
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
> mandatory for shaping Devanagari text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

The `abvm` feature positions above-base marks for attachment to base
characters. In Devanagari, this includes "Reph" in addition to
above-base dependent vowels (matras), diacritical marks, and Vedic signs. 

![Above-base mark positioning](/images/devanagari/devanagari-abvm.png)

The `blwm` feature positions below-base marks for attachment to base
characters. In Devanagari, this includes below-base dependent vowels
(matras) and diacritical marks as well as the below-base consonant form "Rakaar".

![Below-base mark positioning](/images/devanagari/devanagari-blwm.png)


## The `<deva>` shaping model ##

The older Devanagari script tag, `<deva>`, has been deprecated. However,
shaping engines may still encounter fonts that were built to work with
`<deva>` and some users may still have documents that were written to
take advantage of `<deva>` shaping.

### Distinctions from `<dev2>` ###

The most significant distinction between the shaping models is that the
sequence of "Halant" and consonant glyphs used to trigger shaping
features was altered when migrating from `<deva>` to
`<dev2>`. 


Specifically, shaping engines were expected to reorder post-base
"Halant,_Consonant_" sequences to "_Consonant_,Halant".

As a result, a font's GSUB substitutions would be written to match
"_Consonant_,Halant" sequences in all pre-base and post-base positions.


The `<deva>` syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In `<dev2>` text, as described above in this document, there is no
such reordering. The correct sequence to match for GSUB substitutions is
"_Consonant_,Halant" for pre-base consonants, but "Halant,_Consonant_"
for post-base consonants.

The old Indic shaping model also did not recognize the
`BLWF_MODE_PRE_AND_POST` shaping characteristic. Instead, `<deva>`
was treated as if it followed the `BLWF_MODE_POST_ONLY`
characteristic. In other words, below-base form substitutions were
only applied to consonants after the base consonant.

In addition, for some scripts, left-side dependent vowel marks
(matras) were not repositioned during the final reordering
stage. For `<deva>` text, the left-side matra was always positioned
at the beginning of the syllable.

Finally, in `<deva>` text, the "eyelash Ra" form was encoded as the
sequence "Ra,Halant,ZWJ". 

In `<dev2>`, the required encoding for "eyelash Ra" is now
"Rra,Halant", and the substitution is implemented using the `half`
feature of GSUB.


### Advice for handling fonts with `<deva>` features only ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences in order to apply GSUB substitutions when it is known that
the font in use supports only the `<deva>` shaping model.

### Advice for handling text runs composed in `<deva>` format ###

Shaping engines may choose to match post-base "_Consonant_,Halant"
sequences for GSUB substitutions or to reorder them to
"Halant,_Consonant_" when processing text runs that are tagged with
the `<deva>` script tag and it is known that the font in use supports
only the `<dev2>` shaping model.

Shaping engines may also choose to apply `blwf` substitutions to
below-base consonants occuring before the base consonant when it is
known that the font in use supports an applicable substitution lookup.

Shaping engines may also choose to position left-side matras according
to the `<deva>` ordering scheme; however, doing so might interfere
with matching GSUB or GPOS features.
