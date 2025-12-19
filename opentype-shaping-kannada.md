```{include} /_global.md
```

# Kannada shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Kannada script.


**Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Kannada character tables](#kannada-character-tables)
  - [The `<knd2>` shaping model](#the-knd2-shaping-model)
      - [Stage 1: Identifying syllables and other sequences](#stage-1-identifying-syllables-and-other-sequences)
      - [Stage 2: Initial reordering](#stage-2-initial-reordering)
      - [Stage 3: Applying the basic substitution features from <abbr>GSUB</abbr>](#stage-3-applying-the-basic-substitution-features-from-gsub)
      - [Stage 4: Final reordering](#stage-4-final-reordering)
      - [Stage 5: Applying all remaining substitution features from <abbr>GSUB</abbr>](#stage-5-applying-all-remaining-substitution-features-from-gsub)
      - [Stage 6: Applying remaining positioning features from <abbr>GPOS</abbr>](#stage-6-applying-remaining-positioning-features-from-gpos)
  - [The `<knda>` shaping model](#the-knda-shaping-model)
      - [Distinctions from `<knd2>`](#distinctions-from-knd2)
      - [Advice for handling fonts with `<knda>` features only](#advice-for-handling-fonts-with-knda-features-only)
      - [Advice for handling text runs composed in `<knda>` format](#advice-for-handling-text-runs-composed-in-knda-format)


## General information ##

The Kannada script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the South Indic subgroup, in which
sequences of adjacent consonants are often represented as below-base forms.

The Kannada script is used to write multiple languages, most commonly
Kannada, plus several minority languages. In addition, Sanskrit may be written
in Kannada, so Kannada script runs may include glyphs from the Vedic
Extensions block of Unicode. 

There are two extant Kannada script tags defined in OpenType, `<knda>`
and `<knd2>`. The older script tag, `<knda>`, was deprecated in 2005.
Therefore, new fonts should be engineered to work with the `<knd2>`
shaping model. However, if a font is encountered that supports only
`<knda>`, the shaping engine should deal with it gracefully.

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. In the Kannada
language, dependent-vowel signs may also be referred to as _swara_ forms.

The term "matra" is also used to refer to the headline in other Indic
scripts, and may be used to describe the distinctive cap stroke above most
Kannada letters by comparison. To avoid ambiguity, the term **headline** is
used in most Unicode and OpenType shaping documents.

**Halant** and **Virama** are both standard terms for the above-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. In the Kannada
language, this sign is known as the _hrasva_.

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel should be nasalized. In the Kannada
language, this mark is known as the _candrabindu_.

The term **base consonant** is also critical to Indic shaping. The
base consonant of a syllable is the consonant that carries the
syllable's vowel sound, either the inherent vowel (for an unmarked
base consonant) or a dependent vowel (with the addition of a matra).

A syllable's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
syllable frequently take on secondary forms. Different <abbr title="Glyph Substitution table">GSUB</abbr>
substitutions may apply to a script's **pre-base** and **post-base**
consonants. Some of these substitutions create **above-base** or
**below-base** forms. The **Reph** form of the consonant "Ra" is an
example.

Syllables may also begin with an **independent vowel** instead of a
consonant. In these syllables, the independent vowel is rendered in
full-letter form, not as a matra, and the independent vowel serves as the
syllable base, similar to a base consonant.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Kannada text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark.

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Kannada glyphs must additionally be classified by how they are treated
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
and diacritical marks (some of which are also categorized as `Mark [Mn]`).

Kannada uses one subclass of consonant, `CONSONANT_WITH_STACKER`. This
subclass supports two consonants, <samp>"Jihvamuliya"</samp> (`U+0CF1`) and
<samp>"Upadhmaniya"</samp> (`U+0CF2`), that are used only for Sanskrit text
runs. These consonants may form stacked ligatures with subsequent
consonants without an intervening <samp>"Halant"</samp>. Such ligature formation,
if desired, must be implemented in the font.

The letters classified as `CONSONANT_WITH_STACKER` should be treated
as consonants when [identifying
syllables](#stage-1-identifying-syllables-and-other-sequences). No
additional behavior is required.


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
the glyphs is determined by the lookups found in the font's <abbr title="Glyph Positioning table">GPOS</abbr>
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
of OpenType <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> features. Shaping engines may, internally,
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

### Kannada character tables ###

Separate character tables are provided for the Kannada and Vedic
Extensions blocks as well as for other miscellaneous characters that
are used in `<knd2>` text runs:

  - [Kannada character table](character-tables/character-tables-kannada.md#kannada-character-table)
  - [Vedic Extensions character table](character-tables/character-tables-kannada.md#vedic-extensions-character-table)
  - [Miscellaneous character table](character-tables/character-tables-kannada.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

:::{table} Example character table

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0C81`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0C81; Candrabindu         |
| | | | |
|`U+0C95`   | Letter           | CONSONANT         | _null_                     | &#x0C95; Ka                  |
:::


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


#### Special-function codepoints ####

Other important characters that may be encountered when shaping runs
of Kannada text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

Each of these is of particular importance to shaping engines, because
these codepoints interact with the shaping engine, the text run, and
the active font, either to mediate non-default shaping behavior or to
relay information about the current shaping process.

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

Dotted-circle placeholder characters (like any Unicode codepoint) can
appear anywhere in text input sequences and should be rendered
normally. <abbr title="Glyph Positioning table">GPOS</abbr> positioning lookups should attach mark glyphs to dotted
circles as they would to other non-mark characters. As visible glyphs,
dotted circles can also be involved in <abbr title="Glyph Substitution table">GSUB</abbr> substitutions.

In addition to the default input-text handling process, shaping
engines may also insert dotted-circle placeholders into the text
sequence. Dotted-circle insertions are required when a non-spacing
mark or dependent sign is formed with no base character present.

This requirement covers:

  - Dependent signs that are assigned their own individual Unicode
    codepoints (such as most dependent-vowel marks or matras)
  
  - Dependent signs that are formed only by specific sequences of
    other codepoints (such as <samp>"Reph"</samp>)


The zero-width joiner (<abbr>ZWJ</abbr>) is primarily used to prevent the formation
of a conjunct from a <samp>"_Consonant_,Halant,_Consonant_"</samp> sequence. 

  - The sequence <samp>"_Consonant_,Halant,ZWJ,_Consonant_"</samp> blocks the
    formation of a conjunct between the two consonants. 

Note, however, that the <samp>"_Consonant_,Halant"</samp> subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner (<abbr>ZWNJ</abbr>) must be used instead. 

  - The sequence <samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp> should produce
    the first consonant in its standard form, followed by an explicit
    <samp>"Halant"</samp>.

A secondary usage of the zero-width joiner is to prevent the formation of
<samp>"Reph"</samp>. 

  - An initial <samp>"Ra,Halant,ZWJ"</samp> sequence should not produce a <samp>"Reph"</samp>,
    even where an initial <samp>"Ra,Halant"</samp> sequence without the zero-width
    joiner would otherwise produce a <samp>"Reph"</samp>.

The <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> characters are, by definition, non-printing control
characters and have the _Default_Ignorable_ property in the Unicode
Character Database. In standard text-display scenarios, their function
is to signal a request from the user to the shaping engine for some
particular non-default behavior. As such, they are not rendered
visually.

> Note: Naturally, there are special circumstances where a user or
> document might need to request that a <abbr title="Zero-Width Joiner">ZWJ</abbr> or <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> be rendered
> visually, such as when illustrating the OpenType shaping process, or
> displaying Unicode tables.

Because the <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> are non-printing control characters, they can
be ignored by any portion of a software text-handling stack not
involved in the shaping operations that the <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> are designed
to interface with. For example, spell-checking or collation functions
will typically ignore <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr>.

Similarly, the <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> should be ignored by the shaping engine
when matching sequences of codepoints against the backtrack and
lookahead sequences of a font's <abbr title="Glyph Substitution table">GSUB</abbr> or <abbr title="Glyph Positioning table">GPOS</abbr> lookups.

For example:

  - A lookup that substitutes an alternate version of a
    dependent-vowel (matra) glyph when it is preceded by <samp>"Ka,Halant,Tta"</samp>
    should still be applied if the dependent-vowel codepoint is preceded
    by <samp>"Ka,Halant,ZWJ,Tta"</samp> in the text run.

The no-break space (<abbr>NBSP</abbr>) is primarily used to display those
codepoints that are defined as non-spacing (marks, dependent vowels
(matras), below-base consonant forms, and post-base consonant forms)
in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match <samp>"NBSP,ZWJ,Halant,_Consonant_"</samp>, <samp>"NBSP,_mark_"</samp>, or <samp>"NBSP,_matra_"</samp>.

In addition to general punctuation, runs of Kannada text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.



## The `<knd2>` shaping model ##

Processing a run of `<knd2>` text involves six top-level stages:

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from <abbr>GSUB</abbr>
4. Final reordering
5. Applying all remaining substitution features from <abbr>GSUB</abbr>
6. Applying all remaining positioning features from <abbr>GPOS</abbr>


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve applying a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

Indic scripts follow many of the same shaping patterns, but they
differ in a few critical characteristics that the shaping engine must
track. These include:

  - The position of the base consonant in a syllable.
  
  - The final position of <samp>"Reph"</samp>.
  
  - Whether <samp>"Reph"</samp> must be requested explicitly or if it is formed by
    a specific, implicit sequence.
	
  - Whether the below-base forms feature is applied only to consonants
    before the syllable base, only to consonants after the base
    consonant, or to both.
	
  - The ordering positions for dependent vowels
    (matras). Specifically, right-side, above-base, and below-base
    matras follow different rules in different scripts. 
	All Indic scripts position left-side matras in the same
    manner, in the ordering position `POS_PREBASE_MATRA`. 

With regard to these common variations, Kannada's specific shaping
characteristics include:

  - `BASE_POS_LAST` = The base consonant of a syllable is the last
     consonant, not counting any consonants with post-base forms.
	 
	 - Kannada differs somewhat from other `BASE_POS_LAST` scripts in
       that all consonants can use post-base forms. Therefore, the
       general base-consonant search algorithm should identify the first
       non-<samp>"Reph"</samp> consonant as the base. This is the expected
       behavior, as it allows the same search algorithm to be used
       with all `BASE_POS_LAST` scripts.

  - `REPH_POS_AFTER_POST` = <samp>"Reph"</samp> is ordered after the last post-base
     consonant form.

  - `REPH_MODE_IMPLICIT` = <samp>"Reph"</samp> is formed by an initial <samp>"Ra,Halant"</samp> sequence.

  - `BLWF_MODE_POST_ONLY` = The below-forms feature is applied only to
     post-base consonants.

  - `MATRA_POS_TOP` = `POS_BEFORE_SUBJOINED`  = Above-base matras are
    ordered before any subjoined (i.e., below-base) consonant forms.

  - `MATRA_POS_RIGHT` = Kannada includes right-side matras that follow two
     different reordering rules. 
	 
	 - Matras <samp>"Sign Vocalic R"</samp> (`U+0CC3`), <samp>"Sign Vocalic Rr"</samp>
       (`U+0CC4`), <samp>"Sign Ee"</samp> (`U+0CC7`), <samp>"Sign Ai"</samp> (`U+0CC8`), <samp>"Sign
       O"</samp> (`U+0CCA`), <samp>"Sign Oo"</samp> (`U+0CCB`), <samp>"Length Mark"</samp> (`U+0CD5`),
       and <samp>"Ai Length Mark"</samp> (`U+0CD6`) use `POS_AFTER_SUBJOINED` =
       These right-side matras are ordered after all subjoined (i.e.,
       below-base) consonant forms. 
	   
	 - Matras <samp>"Sign Aa"</samp>(`U+0CBE`), <samp>"Sign Ii"</samp> (`U+0CC0`), <samp>"Sign U"</samp>
       (`U+0CC1`), and <samp>"Sign Uu"</samp> (`U+0CC2`) use
       `POS_BEFORE_SUBJOINED` = These right-side matras are ordered before
       all subjoined (i.e., below-base) consonant forms.

  - `MATRA_POS_BOTTOM` = `POS_BEFORE_SUBJOINED` = Below-base matras are
     ordered before the any subjoined (i.e., below-base) consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how <samp>"Reph"</samp>
should be encoded within a run of text.


### Stage 1: Identifying syllables and other sequences ###

A syllable in Kannada consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Kannada Unicode block enumerates four modifier signs,
> "Candrabindu" (`U+0C81`), "Anusvara" (`U+0C82`), "Visarga" 
> (`U+0C83`), and "Avagraha" (`U+0CBD`) In addition, Sanskrit text
> written in Kannada may include additional signs from Vedic
> Extensions block. 
>
> Note also that the "Spacing Candrabindu" (`U+0C80`) is a letter, not
> a modifier sign.

Each syllable contains exactly one vowel sound. Valid syllables may
begin with either a consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that independent vowel
is the syllable's only vowel sound and serves as the "base". 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

Kannada uses the `BASE_POS_LAST` characteristic mentioned
earlier. However, because all consonants in the script can potentially
take on post-base consonant forms, the outcome of the shaping
characteristic may be counterintuitive.

Generally speaking, the base consonant is the first consonant of the
syllable, which is rendered in full form, and any subsequent
consonants are rendered in special post-base forms. 

Each of these post-base consonants will be preceded by the <samp>"Halant"</samp> mark, which
indicates that they carry no vowel. They affect pronunciation by
combining with the base consonant (e.g., "_str_", "_pl_") but they
do not add a vowel sound.

As with other Indic scripts, the consonant <samp>"Ra"</samp> receives special
treatment; in many circumstances it is replaced by a combining
mark-like form. 

  - A <samp>"Ra,Halant"</samp> sequence at the beginning of a syllable is replaced
    with a right-side mark called <samp>"Reph"</samp> (unless the <samp>"Ra"</samp> is the only
    consonant in the syllable). This rule is synonymous with the
    `REPH_MODE_IMPLICIT` characteristic mentioned earlier.
  
<samp>"Reph"</samp> characters must be reordered after the syllable-identification
stage is complete.

> Note: Generally speaking, OpenType fonts will implement support for
> any below-base, post-base, and pre-base-reordering consonant forms
> by including the necessary substitution rules in their `blwf`,
> `pstf`, and `pref` lookups in <abbr title="Glyph Substitution table">GSUB</abbr>.
>
> Consequently, whenever shaping engines need to determine whether or 
> not a given consonant can take on such a special form, the most
> appropriate test is to check if the consonant is included in the
> relevant <abbr title="Glyph Substitution table">GSUB</abbr> lookup. Other implementations are possible, such as
> maintaining static tables of consonants, but checking for <abbr title="Glyph Substitution table">GSUB</abbr>
> support ensures that the expected behavior is implemented in the
> active font, and is therefore the most reliable approach.


In addition to valid syllables, standalone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Kannada script, may
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
used to match Kannada syllables. 

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
_placeholder_	= `PLACEHOLDER` | `CONSONANT_PLACEHOLDER` | `NUMBER`
_dottedcircle_	= `DOTTED_CIRCLE`
_repha_		= `CONSONANT_PRE_REPHA`
_consonantmedial_	= `CONSONANT_MEDIAL`
_symbol_	= `SYMBOL` | `AVAGRAHA`
_consonantwithstacker_	= `CONSONANT_WITH_STACKER`
_other_		= `OTHER` | `MODIFYING_LETTER`
```


> Note: the _ra_ identification class is mutually exclusive with 
> the _consonant_ class. The union of the _consonant_ and _ra_ classes
> is used in the regular expression elements below in order to
> correctly identify <samp>"Ra"</samp> characters that do not trigger <samp>"Reph"</samp> or
> <samp>"Rakaar"</samp> shaping behavior.
>
> Note, also, that the cantillation mark "combining Ra" in the
> Devanagari Extended block does _not_ belong to the _ra_
> identification class, and that the other "combining consonant"
> cantillation marks in the Devanagari Extended block do not belong to
> the _consonant_ identification class.

> Note: The _placeholder_ identification class includes codepoints
> that are often used in place of vowels or consonants when a document
> needs to display a matra, mark, or special form in isolation or
> in another context beyond a standard syllable. Examples of
> _placeholder_ codepoints include hyphens and non-breaking
> spaces. Sequences that utilize this approach should be identified as
> "standalone" syllables.
>
> The _placeholder_ identification class also includes numerals, which
> are commonly used as word substitutes within normal text. Examples
> include ordinals (e.g., "4th").

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
HALANT_OR_MATRA_GROUP	= FINAL_HALANT_GROUP | MATRA_GROUP*)
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

> Note: Although they are labeled as "standalone syllables" here,
> many sequences that match the standalone regular expression above
> are instances where a document needs to display a matra, combining
> mark, or special form in isolation. Such sequences might not have
> any significance with regard to the definition of syllables used in
> the language or orthography of the text.

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


The primary problem involved in shaping broken syllables is the lack
of a syllable base (either a base consonant or an independent
vowel). Without a syllable base, the shaping engine cannot perform
<abbr title="Glyph Positioning table">GPOS</abbr> positioning and other contextual operations that are required
later in the shaping process.

To make up for this limitation, shaping engines should insert a
dotted-circle placeholder (`U+25CC`) character into the text stream
where the missing syllable base was expected to occur. This
placeholder allows the shaping process to proceed on a best-effort
basis at handling the broken-syllable sequence, but making guarantees
about the orthographic correctness or preferred appearance of the
final result is out of scope for this document.

Shaping engines can perform this dotted-circle insertion at any point
after the broken syllable has been recognized and before <abbr title="Glyph Substitution table">GSUB</abbr> features
are applied. However, the best results will likely be attained by
performing the insertion immediately, before proceeding to
stage 2. This will enable the maximum number of <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> features
in the active font to be correctly applied to the text run by ensuring
that all reordering, tagging, and sorting algorithms are executed as
usual.

> Note: In software stacks where other text-handling operations, such
> as Unicode normalization and localization, are performed before the
> text run is passed to the shaping engine, there is a potential for
> the dotted-circle insertion to cause unexpected effects.
>
> For example, if a `ccmp` or `locl` feature substitutes the default
> dotted-circle placeholder glyph with a variant glyph of a different
> size or weight for the (`U+25CC`) codepoint, then any shaping engine
> which relies on another software component to handle that
> functionality must take additional care to ensure consistency.


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




After the syllables have been identified, each of the subsequent 
shaping stages occurs on a per-syllable basis.

### Stage 2: Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text to the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs, 
> <samp>"Ra,Halant"</samp> glyph sequences, and other consonants that take special
> treatment in some circumstances. 
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
scripts. It includes some ordering categories not utilized in
Kannada. 

The basic positions (left to right) are <samp>"Reph"</samp>
(`POS_RA_TO_BECOME_REPH`), dependent vowels (matras) and consonants
positioned before the base consonant or syllable base
(`POS_PREBASE_MATRA` and `POS_PREBASE_CONSONANT`), the base consonant
or syllable base (`POS_SYLLABLE_BASE`), above-base consonants
(`POS_ABOVEBASE_CONSONANT`), below-base consonants
(`POS_BELOWBASE_CONSONANT`), consonants positioned after the base
consonant or syllable base (`POS_POSTBASE_CONSONANT`), syllable-final
consonants (`POS_FINAL_CONSONANT`), and syllable-modifying or Vedic
signs (`POS_SMVD`).

In addition, several secondary positions are defined to handle various
reordering rules that deal with relative, rather than absolute,
positioning. `POS_AFTER_MAIN` means that a character must be
positioned immediately after the syllable base. `POS_BEFORE_SUBJOINED`
and `POS_AFTER_SUBJOINED` mean that a character must be positioned
before or after any below-base consonants, respectively. Similarly,
`POS_BEFORE_POST` and `POS_AFTER_POST` mean that a character must be
positioned before or after any post-base consonants, respectively. 

For shaping-engine implementers, the names used for the ordering
categories matter only in that they are unambiguous. 

For a definition of the "base" consonant, refer to stage 2, step 1, which
follows.

#### Stage 2, step 1: Base consonant ####

The first step is to determine the base consonant of the syllable, if
there is one, and tag it as `POS_SYLLABLE_BASE`.

In a syllable that begins with an independent vowel, the independent
vowel will always serve as the syllable base, and it should be tagged
as `POS_SYLLABLE_BASE`. The shaping engine can then proceed to step 2.

In a standalone sequence or other syllable that begins with a placeholder
or dotted circle, the placeholder or dotted circle will always serve
as the syllable base, and it should be tagged as
`POS_SYLLABLE_BASE`. The shaping engine can then proceed to step 2.

In a syllable that begins with a consonant, the shaping engine must
determine the base consonant by a script-specific algorithm.

> Note: Shaping engines may choose to treat independent-vowel bases 
> like base consonants for the sake of simplicity or code
> reuse.
>
> However, implementations that take this approach should note
> that removing the distinction between base consonants and
> independent-vowel bases entirely may have unintended
> consequences. Making guarantees about the correctness of the results
> or about language-specific tests is out of scope for this document.

The base consonant is defined as the consonant in a consonant-based
syllable that carries the syllable's vowel sound. That vowel sound
will either be provided by the script's inherent vowel (in which case
it is not written with a separate character) or the sound will be designated
by the addition of a dependent-vowel (matra) sign.


<!--- > Because vowel-based syllables will not include consonants and
> because independent vowels do not take on special forms or require
> reordering, many of the steps that follow will involve no
> work for a vowel-based syllable. However, vowel-based syllables must
> still be sorted and their marks handled correctly, and <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr>
> lookups must be applied. These steps of the shaping process follow
> the same rules that are employed for consonant-based syllables.
--->

While performing the base-consonant search, shaping engines may
also encounter special-form consonants, including below-base
consonants and post-base consonants. Each of these special-form
consonants must also be tagged (`POS_BELOWBASE_CONSONANT`,
`POS_POSTBASE_CONSONANT`, respectively). 

Any pre-base-reordering consonant (such as a pre-base-reordering <samp>"Ra"</samp>)
encountered during the base-consonant search must be tagged
`POS_POSTBASE_CONSONANT`. 
 
> Note: Shaping engines may choose any method to identify consonants that
> have below-base, post-base, or pre-base-reordering forms while
> executing the above algorithm. For example, one implementation may
> choose to maintain a static table of special-form consonants to
> compare against the text run. Another implementation might examine
> the active font to see if it includes a `blwf`, `pstf`, or `pref`
> lookup in the <abbr title="Glyph Substitution table">GSUB</abbr> table that affects the consonants encountered in
> the syllable.
>
> However, checking for <abbr title="Glyph Substitution table">GSUB</abbr> support ensures that the expected
> behavior is implemented in the active font, and is therefore the
> most reliable approach.


The algorithm for determining the base consonant is

  - If the syllable starts with <samp>"Ra,Halant"</samp> and the syllable contains
    more than one consonant, exclude the starting <samp>"Ra"</samp> from the list of
    consonants to be considered. 
  - Starting from the end of the syllable, move backwards until a consonant is found.
      * If the consonant is the first consonant, stop.
      * If the consonant is preceded by the sequence <samp>"Halant,ZWJ"</samp>, stop.
      * If the consonant has a below-base form, tag it as
        `POS_BELOWBASE_CONSONANT`, then move to the previous consonant. 
      * If the consonant has a post-base form, tag it as
        `POS_POSTBASE_CONSONANT`, then move to the previous consonant. 
      * If the consonant is a pre-base-reordering <samp>"Ra"</samp>, tag it as
        `POS_POSTBASE_CONSONANT`, then move to the previous consonant. 
      * If none of the above conditions is true, stop.
  - The consonant stopped at will be the base consonant.


> Note: The algorithm is designed to work for all Indic
> scripts. However, Kannada does not utilize pre-base-reordering <samp>"Ra"</samp>.
>
> Also, it is important to note that all consonants in Kannada have a
> post-base form, therefore the backwards-search step will
> automatically move past them until it reaches either a <samp>"Ra,Halant"</samp>
> sequence or the first consonant. However, this condition is not the
> same as the shaping characteristic `BASE_POS_FIRST`, which does not
> use the above search algorithm at all.

> Note: Because Kannada employs the `BLWF_MODE_POST_ONLY` shaping
> characteristic, consonants with below-base special forms will occur
> only after the base consonant or syllable base. 
> 
> During the base-consonant search, therefore, all of these below-base
> form sequences will be encountered and tagged correctly as
> <samp>"Halant,_consonant_"</samp> patterns. Stage 2, step 5 below exists to ensure that
> the <samp>"_consonant_,Halant"</samp> pattern preceding the base consonant or syllable base
> for below-base forms in other Indic scripts will also be tagged correctly.

#### Stage 2, step 2: Matra decomposition ####

Second, any multi-part dependent vowels (matras) must be decomposed
into their independent components. Kannada has five
multi-part dependent vowels, "Ii" (`U+0CC0`), "Ee" (`U+0CC7`), "Ai"
(`U+0CC8`), "O" (`U+0CCA`), and "Oo" (`U+0CCB`). Each
has a canonical decomposition, so this step is unambiguous. 

> "Ii" (`U+0CC0`) decomposes to "`U+0CBF`,`U+0CD5`"
>
> "Ee" (`U+0CC7`) decomposes to "`U+0CC6`,`U+0CD5`"
>
> "Ai" (`U+0CC8`) decomposes to "`U+0CC6`,`U+0CD6`"
>
> "O" (`U+0CCA`) decomposes to "`U+0CC6`,`U+0CC2`"
>
> "Oo" (`U+0CCB`) decomposes to "`U+0CCA`,`U+0CD5`"
>

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.

> Note: The decomposition of "Oo" (`U+0CCB`) is atypical; Unicode
> specifies that the codepoint decomposes to "O" (`U+0CCA`) followed
> by `U+0CD5`; the "O" codepoint is then decomposed to
> "`U+0CC6`,`U+0CC2`". Shaping engines must take care not to miss this
> second decomposition.


:::{figure-md}
![Multi-part matra decomposition](/images/kannada/kannada-matra-decomposition.svg "Multi-part matra decomposition"){.shaping-demo .inline-svg .greyscale-svg #kannada-matra-decomposition}

Multi-part matra decomposition
:::

```{svg-color-toggle-button} kannada-matra-decomposition
```


#### Stage 2, step 3: Tag matras ####

Third, all dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be
moved to the correct position in the syllable.

Left-side matras should be tagged with `POS_PREBASE_MATRA`.

Above-base matras should be tagged with `POS_BEFORE_SUBJOINED`.

Right-side matras should be tagged according to two rules.

  - Matras <samp>"Sign Vocalic R"</samp> (`U+0CC3`), <samp>"Sign Vocalic Rr"</samp>
       (`U+0CC4`), <samp>"Sign Ee"</samp> (`U+0CC7`), <samp>"Sign Ai"</samp> (`U+0CC8`), <samp>"Sign
       O"</samp> (`U+0CCA`), <samp>"Sign Oo"</samp> (`U+0CCB`), <samp>"Length Mark"</samp> (`U+0CD5`),
       and <samp>"Ai Length Mark"</samp> (`U+0CD6`) should be tagged with
       `POS_AFTER_SUBJOINED`.
	   
  - Matras <samp>"Sign Aa"</samp>(`U+0CBE`), <samp>"Sign Ii"</samp> (`U+0CC0`), <samp>"Sign U"</samp>
       (`U+0CC1`), and <samp>"Sign Uu"</samp> (`U+0CC2`) use
       `POS_BEFORE_SUBJOINED`.

> Note: the right-side matras <samp>"Sign Ee"</samp> (`U+0CC7`), <samp>"Sign Ai"</samp>
> (`U+0CC8`), <samp>"Sign O"</samp> (`U+0CCA`), and <samp>"Sign Oo"</samp> (`U+0CCB`) are
> multi-part matras and were decomposed into independent components
> during stage 2, step 2. They are listed here only to ensure that the
> two position-tagging rules used in Kannada are described completely.

Below-base matras should be tagged with `POS_BEFORE_SUBJOINED`.

For simplicity, shaping engines may choose to tag single-part matras
in an earlier text-processing step, using the information in the
_Mark-placement subclass_ column of the character tables. It is
critical at this step, however, that all decomposed matras are also
correctly tagged before proceeding to the next step.

#### Stage 2, step 4: Adjacent marks ####

Fourth, any subsequences of marks that include a <samp>"Nukta"</samp> and a
<samp>"Halant"</samp> or Vedic sign must be reordered so that the <samp>"Nukta"</samp> appears
first.

This means that the subsequence <samp>"Halant,Nukta"</samp> is reordered to
<samp>"Nukta,Halant"</samp> and that the subsequence <samp>"_Vedic_sign_,Nukta"</samp> is
reordered to <samp>"Nukta,_Vedic_sign"</samp>.

For subsequences of affected marks that are longer than two, the
reordering operation must be repeated until the <samp>"Nukta"</samp> is the first
character in the subsequence. No other marks in the subsequence
should be reordered.

This order is canonical in Unicode and is required so that
<samp>"_consonant_,Nukta"</samp> substitution rules from <abbr title="Glyph Substitution table">GSUB</abbr> will be correctly
matched later in the shaping process.

#### Stage 2, step 5: Pre-base consonants ####

Fifth, consonants that occur before the syllable base must be tagged
with `POS_PREBASE_CONSONANT`. Excluding initial <samp>"Ra,Halant"</samp> sequences
that will become <samp>"Reph"</samp>s: 

  - If the consonant has a below-base form, tag it as
          `POS_BELOWBASE_CONSONANT`. 
  - Otherwise, tag it as `POS_PREBASE_CONSONANT`.
  
> Note: Shaping engines may choose any method to identify consonants that
> have below-base, post-base, or pre-base-reordering forms while
> executing the above algorithm. For example, one implementation may
> choose to maintain a static table of special-form consonants to
> compare against the text run. Another implementation might examine
> the active font to see if it includes a `blwf`, `pstf`, or `pref`
> lookup in the <abbr title="Glyph Substitution table">GSUB</abbr> table that affects the consonants encountered in
> the syllable.
>
> However, checking for <abbr title="Glyph Substitution table">GSUB</abbr> support ensures that the expected
> behavior is implemented in the active font, and is therefore the
> most reliable approach.

Kannada does not use any pre-base consonants; this step is listed here
because it is part of the general processing scheme for shaping Indic scripts.

> Note: Because Kannada employs the `BLWF_MODE_POST_ONLY` shaping
> characteristic, consonants with below-base special forms will occur
> only after the base consonant or syllable base. 
> 
> During the base-consonant search in stage 2, step 1, therefore, all of these below-base
> form sequences will be encountered and tagged correctly as
> <samp>"Halant,_consonant_"</samp> patterns. The tagging is this step ensures that
> the <samp>"_consonant_,Halant"</samp> pattern preceding the base consonant or syllable base
> for below-base forms in other Indic scripts will also be tagged correctly.

#### Stage 2, step 6: Reph ####

Sixth, initial <samp>"Ra,Halant"</samp> sequences that will become <samp>"Reph"</samp>s must be tagged with
`POS_RA_TO_BECOME_REPH`.

> Note: an initial <samp>"Ra,Halant"</samp> sequence will always become a <samp>"Reph"</samp>
> unless the <samp>"Ra"</samp> is the only consonant in the syllable.

#### Stage 2, step 7: Final consonants ####

Seventh, all final consonants must be tagged. Consonants that occur
after the syllable base _and_ after a dependent vowel (matra) sign
must be tagged with  `POS_FINAL_CONSONANT`.

> Note: Final consonants occur only in Sinhala and should not be
> expected in `<knd2>` text runs. This step is included here to
> maintain compatibility across Indic scripts.


#### Stage 2, step 8: Mark tagging ####

Eighth, all marks must be tagged. 

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.

Marks in the `BINDU`, `VISARGA`, `AVAGRAHA`, `CANTILLATION`,
`SYLLABLE_MODIFIER`, `GEMINATION_MARK`, and `SYMBOL` categories should
be tagged with `POS_SMVD`. 

All <samp>"Nukta"</samp>s must be tagged with the same positioning tag as the
preceding consonant, independent vowel, placeholder, or dotted circle.

All remaining marks (not in the `POS_SMVD` category and not <samp>"Nukta"</samp>s)
must be tagged with the same positioning tag as the closest non-mark
character the mark has affinity with, so that they move together 
during the sorting step.

There are two possible cases: those marks before the syllable base
and those marks after the syllable base. In addition, an exception is
made for <samp>"Halant"</samp> marks that follow a left-side (pre-base) matra.

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
  
  3. Finally, <samp>"Halant"</samp> marks that follow a left-side dependent vowel
     (matra) should _not_ be tagged with the left-side matra's
     positioning tag. Instead, the <samp>"Halant"</samp> should be tagged with the
     positioning tag of the non-mark character preceding the left-side
     matra. This prevents the <samp>"Halant"</samp> mark from being moved with the
     left-side matra when the syllable is sorted.


<!--- HarfBuzz also tags everything between a post-base consonant or -->
<!--matra and another post-base consonant as belonging to the latter -->
<!--post-base consonant. --->


#### Stage 2, step 9: Sort syllable ####

With these steps completed, the syllable can be sorted into the final
sort order as listed at the beginning of stage 2.

The glyphs in the syllable should be sorted in stable order,
so that glyphs of the same ordering category remain in the same
relative position with respect to each other.


#### Stage 2, step 10: Flag sequences for possible feature applications ####

With the initial reordering complete, those glyphs in the syllable that
may have <abbr title="Glyph Substitution table">GSUB</abbr> or <abbr title="Glyph Positioning table">GPOS</abbr> features applied in stages 3, 5, and 6 should be
flagged for each potential feature. 

This flagging is preliminary; the set of potential features varies
between different scripts and which features are supported varies
between fonts. It is also possible that the application of
one feature on a glyph sequence will perform a substitution that makes
a later feature no longer applicable to the updated sequence.

Consequently, the flagging must be completed before shaping proceeds
to the stages during which features are applied.

Some shaping features, such as `locl`, can potentially apply to any
glyphs. Therefore it is not necessary to maintain a separate flag for
these features in the bitmask (or other data structure) used to track
the flags -- although shaping engines may do so if desired.

The sequences to flag are summarized in the list below; a full
description of each feature's function and interpretation is provided
in <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> application stages that follow.

  - `nukt` should match <samp>"_Consonant_,Nukta"</samp> sequences
  - `akhn` should match <samp>"Ka,Halant,Ssa"</samp> and <samp>"Ja,Halant,Nya"</samp>
  - `rphf` should match initial <samp>"Ra,Halant"</samp> sequences but _not_ match
            initial <samp>"Ra,Halant,ZWJ"</samp> sequences
  - `pref` should match <samp>"_Consonant_,Ra"</samp> in post-base positions
  - `blwf` should match <samp>"Halant,_Consonant_"</samp> in post-base positions
  - `half` should match <samp>"_Consonant_,Halant"</samp> in pre-base position but
           _not_ match <samp>"Ra,Halant"</samp> sequences flagged for `rphf` and
           _not_ match <samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp> sequences
  - `pstf` should match <samp>"Halant,_Consonant_"</samp> in post-base position
  - `cjct` should match <samp>"_Consonant_,Halant,_Consonant_"</samp> but _not_
            match <samp>"_Consonant_,Halant,ZWJ,_Consonant_"</samp> or
            <samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp>




### Stage 3: Applying the basic substitution features from <abbr>GSUB</abbr> ###

The basic-substitution stage applies mandatory substitution features
using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this
stage, glyph sequences should be flagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features in stage 2, step 10.

The order in which these substitutions must be performed is fixed for
all Indic scripts:

	locl
	nukt
	akhn
	rphf 
	rkrf (not used in Kannada)
	pref
	blwf 
	abvf (not used in Kannada)
	half
	pstf
	vatu (not used in Kannada)
	cjct
	cfar (not used in Kannada)

#### Stage 3, step 1: locl ####

The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> <abbr title="Glyph Substitution table">GSUB</abbr> substitutions in the following steps.

#### Stage 3, step 2: nukt ####

The `nukt` feature replaces <samp>"_Consonant_,Nukta"</samp> sequences with a
precomposed nukta-variant of the consonant glyph. 

  - The context defined for a `nukt` feature is:

:::{table} `nukt` feature context
    
| Backtrack     | Matching sequence             | Lookahead     |
|:--------------|:------------------------------|:--------------|
| _none_        | `_consonant_`(full),`_nukta_` | _none_        |
:::


:::{figure-md}
![Nukta composition](/images/kannada/kannada-nukt.svg "Nukta composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-nukt}

Nukta composition
:::

```{svg-color-toggle-button} kannada-nukt
```


#### Stage 3, step 3: akhn ####

The `akhn` feature replaces two specific sequences with required ligatures. 

  - <samp>"Ka,Halant,Ssa"</samp> is substituted with the <samp>"KSsa"</samp> ligature. 
  - <samp>"Ja,Halant,Nya"</samp> is substituted with the <samp>"JNya"</samp> ligature. 
  
These sequences can occur anywhere in a syllable. The <samp>"KSsa"</samp> and
<samp>"JNya"</samp> characters have orthographic status equivalent to full
consonants in some languages, and fonts may have `cjct` substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.

  - The context defined for an `akhn` feature is:

:::{table} `akhn` feature context
    
| Backtrack     | Matching sequence           | Lookahead     |
|:--------------|:----------------------------|:--------------|
| _none_        | `AKHAND_CONSONANT_SEQUENCE` | _none_        |
:::


:::{figure-md}
![KSsa ligation](/images/kannada/kannada-akhn-kssa.svg "KSsa ligation"){.shaping-demo .inline-svg .greyscale-svg #kannada-akhn-kssa}

KSsa ligation
:::

```{svg-color-toggle-button} kannada-akhn-kssa
```


:::{figure-md}
![JNya ligation](/images/kannada/kannada-akhn-jnya.svg "JNya ligation"){.shaping-demo .inline-svg .greyscale-svg #kannada-akhn-jnya}

JNya ligation
:::

```{svg-color-toggle-button} kannada-akhn-jnya
```


#### Stage 3, step 4: rphf ####

The `rphf` feature replaces initial <samp>"Ra,Halant"</samp> sequences with the
<samp>"Reph"</samp> glyph.

  - An initial <samp>"Ra,Halant,ZWJ"</samp> sequence, however, must not be flagged for
    the `rphf` substitution.
	

  - The context defined for a `rphf` feature is:

:::{table} `rphf` feature context
    
| Backtrack        | Matching sequence       | Lookahead     |
|:-----------------|:------------------------|:--------------|
| `SYLLABLE_START` | "Ra"(full),`_halant_`   | _none_        |
:::


:::{figure-md}
![Reph composition](/images/kannada/kannada-rphf.svg "Reph composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-rphf}

Reph composition
:::

```{svg-color-toggle-button} kannada-rphf
```


#### Stage 3, step 5: rkrf ####

> This feature is not used in Kannada.

#### Stage 3, step 6: pref ####

The `pref` feature replaces pre-base-reordering consonant glyphs with
any special forms.

The substitution of the nominal glyph for its special form takes place
at this stage. However, the actual reordering move is performed later,
in stage 4, step 4.

> Note: Kannada does not usually incorporate pre-base-reordering
> consonant forms, but it is possible for a font to implement them in
> order to provide for desired typographic variation.

#### Stage 3, step 7: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. All consonants in Kannada can take on a below-base consonant
form.


:::{figure-md}
![Below-base form composition](/images/kannada/kannada-blwf.svg "Below-base form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-blwf}

Below-base form composition
:::

```{svg-color-toggle-button} kannada-blwf
```


#### Stage 3, step 8: abvf ####

> This feature is not used in Kannada.

#### Stage 3, step 9: half ####

The `half` feature replaces <samp>"_Consonant_,Halant"</samp> sequences before the
base consonant or syllable base with "half forms" of the consonant
glyphs.

In the most common case, this substitution applies to
<samp>"_Consonant_,Halant"</samp> sequences that are followed by another
<samp>"_Consonant_"</samp>.

In addition, a sequence matching <samp>"_Consonant_,Halant,ZWJ"</samp> must also be
flagged for potential `half` substitutions.

> Note: The presence of the <samp>"ZWJ"</samp> at the end of the sequence means
> that the sequence may match the regular-expression test in stage 1
> as the end of a syllable, even without being followed by a base
> consonant or syllable base.
>
> The fact that the regular-expression tests identify a syllable break
> after the <samp>"_Consonant_,Halant,ZWJ"</samp> is a byproduct of OpenType
> shaping and Unicode encoding, however, and might not have any
> significance with regard to the definition of syllables used in the
> language or orthography of the text.

There are two exceptions to the default behavior, for which the
shaping engine must test:

  - Initial <samp>"Ra,Halant"</samp> sequences, which should have been flagged for
    the `rphf` feature earlier, must not be flagged for potential
    `half` substitutions.

  - A sequence matching <samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp> must not be
    flagged for potential `half` substitutions.

> Note: Kannada does not usually incorporate half forms, but it is
> possible for a font to implement them in order to provide for
> desired typographic variation.


#### Stage 3, step 10: pstf ####

The `pstf` feature replaces post-base-consonant glyphs with any special forms.


#### Stage 3, step 11: vatu ####

> This feature is not used in Kannada.

#### Stage 3, step 12: cjct ####

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match <samp>"_Consonant_,Halant,_Consonant_"</samp>.

A sequence matching <samp>"_Consonant_,Halant,ZWJ,_Consonant_"</samp> or
<samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp> must not be flagged to form a conjunct.

> Note: The presence of the <samp>"ZWJ"</samp> in a
> <samp>"_Consonant_,Halant,ZWJ,_Consonant_"</samp> sequence should automatically
> inhibit any `cjct` feature rules from matching the sequence as valid
> input, and thus prevent the `cjct` substitution from being applied.

> Note: The presence of the <samp>"ZWNJ"</samp> in a
> <samp>"_Consonant_,Halant,ZWNJ,_Consonant_"</samp> sequence means that the
> <samp>"_Consonant_,Halant,ZWNJ"</samp> subsequence will match the
> regular-expression test in stage 1 as the end of a syllable.
> 
> Because OpenType shaping features in `<knd2>` are defined as
> applying only within an individual syllable, this means that the
> presence of the <samp>"ZWNJ"</samp> will automatically prevent the application of
> a `cjct` feature by triggering the identification of a syllable
> break between the two consonants.
>
> The fact that the regular-expression tests identify a syllable break
> after the <samp>"_Consonant_,Halant,ZWNJ"</samp> is a byproduct of OpenType
> shaping and Unicode encoding, however, and might not have any
> significance with regard to the definition of syllables used in the
> language or orthography of the text.
>
> Note, also: The presence of the <samp>"ZWJ"</samp> means that a
> <samp>"_Consonant_,Halant,ZWJ"</samp> sequence may match the regular-expression
> test in stage 1 as the end of a syllable, even without being
> followed by a base consonant or syllable base. By definition,
> however, a <samp>"_Consonant_,Halant,ZWJ"</samp> syllable identified in stage 1
> cannot also include a <samp>"_Consonant_"</samp> after the <abbr title="Zero-Width Joiner">ZWJ</abbr>.

The font's <abbr title="Glyph Substitution table">GSUB</abbr> rules might be implemented so that `cjct`
substitutions apply to half-form consonants; therefore, this feature
must be applied after the `half` feature. 

> Note: Kannada does not usually incorporate conjuncts, but it is
> possible for a font to implement the `cjct` feature in order to
> provide for desired typographic variation.


#### Stage 3, step 13: cfar ####

> This feature is not used in Kannada.


### Stage 4: Final reordering ###

The final reordering stage repositions marks, dependent-vowel (matra)
signs, and <samp>"Reph"</samp> glyphs to the appropriate location with respect to
the base consonant or syllable base. Because multiple substitutions
may have occurred during the application of the basic-shaping features
in the preceding stage, these repositioning moves could not be
performed during the initial reordering stage.

Like the initial reordering stage, the steps involved in this stage
occur on a per-syllable basis.

<!--- Check that classifications have not been mangled. If the -->
<!--character is a Halant AND a ligature was formed AND a multiple
substitution was performed, restore the classification to VIRAMA
because it was almost certainly lost in the preceding <abbr title="Glyph Substitution table">GSUB</abbr> stage.
--->

#### Stage 4, step 1: Base consonant ####

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
search repeated here. However, the application of <abbr title="Glyph Substitution table">GSUB</abbr> shaping
features in stage 3 means that several ligation and many-to-one
substitutions may have taken place. The final glyph produced by that
process may, therefore, be a conjunct or ligature form — in most
cases, such a glyph will not have an assigned Unicode codepoint.
   
#### Stage 4, step 2: Pre-base matras ####

Pre-base dependent vowels (matras) that were reordered during the
initial reordering stage must be moved to their final position. This
position is defined as:
   
   - after the last standalone <samp>"Halant"</samp> glyph that comes after the
     matra's starting position and also comes before the main
     consonant.
   - If a zero-width joiner follows this last standalone <samp>"Halant"</samp>, the
     final matra position is moved to after the joiner.

This means that the matra will move to the right of all explicit
<samp>"consonant,Halant"</samp> subsequences, but will stop to the left of the base
consonant or syllable base, all conjuncts or ligatures that contain
the base consonant or syllable base, and all half forms.

Kannada does not use pre-base matras, so this step will
involve no work when processing `<knd2>` text. It is included here in
order to maintain compatibility with the other Indic scripts.

> Note: OpenType and Unicode both state that if the syllable includes
> a <abbr title="Zero-Width Joiner">ZWJ</abbr> immediately after the last <samp>"Halant"</samp>, then the final matra
> position should be after the <abbr title="Zero-Width Joiner">ZWJ</abbr>.
>
> However, there are several test sequences indicating that
> Microsoft's Uniscribe shaping engine did not follow this rule (in,
> at least, Devanagari and Bengali text), and in these circumstances
> Uniscribe instead makes the final matra position before the final
> <samp>"Consonant,Halant,ZWJ"</samp>.
>
> Subsequently, the HarfBuzz shaping engine has also followed the same
> pattern. If other shaping engine implementations prefer to maintain
> maximum compatibility with Uniscribe and HarfBuzz, then they should
> also follow suit.

> Note: The Microsoft script-development specifications for OpenType
> shaping also state that if a zero-width non-joiner follows the last
> standalone <samp>"Halant"</samp>, the final matra position is moved to after the
> non-joiner. However, it is unnecessary to test for this condition,
> because a <samp>"Halant,ZWNJ"</samp> subsequence is, by definition, the end of a
> syllable. Consequently, a <samp>"Halant,ZWNJ"</samp> cannot be followed by a
> pre-base dependent vowel.


#### Stage 4, step 3: Reph ####

<samp>"Reph"</samp> must be moved from the beginning of the syllable to its final
position. Because Kannada incorporates the `REPH_POS_AFTER_POST`
shaping characteristic, this final position is defined to be
immediately after any post-base consonant forms.


The algorithm for finding the final <samp>"Reph"</samp> position is

  - Move the <samp>"Reph"</samp> to the position immediately before
    the first post-base matra, syllable modifier, or Vedic sign that
    has a positioning tag after the script's <samp>"Reph"</samp> position in the
    syllable sort order (as listed in [stage
    2](#stage-2-initial-reordering)). This will be the final <samp>"Reph"</samp>
    position. 
	> Note: Because Kannada incorporates the
    > `REPH_POS_AFTER_POST` shaping characteristic, this means
    > any positioning tag of `POS_FINAL_CONSONANT` or later,
    > although a post-base matra, syllable modifier, or Vedic sign
    > would not typically be tagged with `POS_FINAL_CONSONANT`.
  - If no other location has been located in the previous step, move
    the <samp>"Reph"</samp> to the end of the syllable.


Finally, if the final position of <samp>"Reph"</samp> occurs after a
<samp>"_matra_,Halant"</samp> subsequence, then <samp>"Reph"</samp> must be repositioned to the
left of <samp>"Halant"</samp>, to allow for potential matching with `abvs` or
`psts` substitutions from <abbr title="Glyph Substitution table">GSUB</abbr>.

:::{figure-md}
![Reph positioning](/images/kannada/kannada-reph-position.svg "Reph positioning"){.shaping-demo .inline-svg .greyscale-svg #kannada-reph-position}

Reph positioning
:::

```{svg-color-toggle-button} kannada-reph-position
```


#### Stage 4, step 4: Pre-base-reordering consonants ####

Any pre-base-reordering consonants must be moved to immediately before
the base consonant or syllable base.
  
Kannada does not use pre-base-reordering consonants, so this step will
involve no work when processing `<knd2>` text. It is included here in order
to maintain compatibility with the other Indic scripts.


#### Stage 4, step 5: Initial matras ####

Any left-side dependent vowels (matras) that are at the start of a
word must be flagged for potential substitution by the `init` feature
of <abbr title="Glyph Substitution table">GSUB</abbr>.

Kannada does not use the `init` feature, so this step will
involve no work when processing `<knd2>` text. It is included here in
order to maintain compatibility with the other Indic scripts.


### Stage 5: Applying all remaining substitution features from <abbr>GSUB</abbr> ###

In this stage, the remaining substitution features from the <abbr title="Glyph Substitution table">GSUB</abbr> table
are applied. In preparation for this stage, glyph sequences should be
flagged for possible application of <abbr title="Glyph Substitution table">GSUB</abbr> features in stage 2,
step 10.

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.

	init (not used in Kannada)
	pres
	abvs
	blws
	psts
	haln

The `init` feature is not used in Kannada.

The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include consonant conjuncts, half-form
consonants, and stylistic variants of left-side dependent vowels
(matras). 

:::{figure-md}
![Pre-base form composition](/images/kannada/kannada-pres.svg "Pre-base form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-pres}

Pre-base form composition
:::

```{svg-color-toggle-button} kannada-pres
```


The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

:::{figure-md}
![Above-base form composition](/images/kannada/kannada-abvs.svg "Above-base form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-abvs}

Above-base form composition
:::

```{svg-color-toggle-button} kannada-abvs
```


The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually involves replacing multiple
below-base glyphs (substituted earlier with the `blwf`) feature with
ligatures or conjunct forms.

:::{figure-md}
![Below-base form composition](/images/kannada/kannada-blws.svg "Below-base form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-blws}

Below-base form composition
:::

```{svg-color-toggle-button} kannada-blws
```


The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures. 

:::{figure-md}
![Post-base form composition](/images/kannada/kannada-psts.svg "Post-base form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-psts}

Post-base form composition
:::

```{svg-color-toggle-button} kannada-psts
```


The `haln` feature replaces syllable-final <samp>"_Consonant_,Halant"</samp> pairs with
special presentation forms. This can include stylistic variants of the
consonant where placing the <samp>"Halant"</samp> mark on its own is
typographically problematic.

:::{figure-md}
![Halant form composition](/images/kannada/kannada-haln.svg "Halant form composition"){.shaping-demo .inline-svg .greyscale-svg #kannada-haln}

Halant form composition
:::

```{svg-color-toggle-button} kannada-haln
```

> Note: The `calt` feature, which allows for generalized application
> of contextual alternate substitutions, is usually applied at this
> point. However, `calt` is not mandatory for correct Kannada shaping
> and may be disabled in the application by user preference.

### Stage 6: Applying remaining positioning features from <abbr>GPOS</abbr> ###

In this stage, mark positioning, kerning, and other <abbr title="Glyph Positioning table">GPOS</abbr> features are
applied.

As with the preceding stage, the order in which these features are
applied is not canonical; they should be applied in the order in which
they appear in the <abbr title="Glyph Positioning table">GPOS</abbr> table in the font.

        dist
        abvm
        blwm

> Note: The `kern` feature is usually applied at this stage, if it is
> present in the font. However, `kern` (like `calt`, above) is not
> mandatory for shaping Kannada text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

:::{figure-md}
![dist feature application](/images/kannada/kannada-dist.svg "dist feature application"){.shaping-demo .inline-svg .greyscale-svg #kannada-dist}

Application of the `dist` feature
:::

```{svg-color-toggle-button} kannada-dist
```

The `abvm` feature positions above-base marks for attachment to base
characters. In Kannada, this includes above-base dependent vowels (matras),
diacritical marks, and Vedic signs. 

The `blwm` feature positions below-base marks for attachment to base
characters. In Kannada, this includes below-base dependent vowels
(matras) as well as below-base diacritical marks.

:::{figure-md}
![Below-base mark positioning](/images/kannada/kannada-blwm.svg "Below-base mark positioning"){.shaping-demo .inline-svg .greyscale-svg #kannada-blwm}

Below-base mark positioning
:::

```{svg-color-toggle-button} kannada-blwm
```


## The `<knda>` shaping model ##

The older Kannada script tag, `<knda>`, has been deprecated. However,
shaping engines may still encounter fonts that were built to work with
`<knda>` and some users may still have documents that were written to
take advantage of `<knda>` shaping.

### Distinctions from `<knd2>` ###

The most significant distinction between the shaping models is that the
sequence of <samp>"Halant"</samp> and consonant glyphs used to trigger shaping
features) was altered when migrating from `<knda>` to
`<knd2>`. 

Specifically, shaping engines were expected to reorder post-base
<samp>"Halant,_Consonant_"</samp> sequences to <samp>"_Consonant_,Halant"</samp>.

As a result, a font's <abbr title="Glyph Substitution table">GSUB</abbr> substitutions would be written to match
<samp>"_Consonant_,Halant"</samp> sequences in all pre-base and post-base positions.


The `<knda>` syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In `<knd2>` text, as described above in this document, there is no
such reordering. The correct sequence to match for <abbr title="Glyph Substitution table">GSUB</abbr> substitutions is
<samp>"_Consonant_,Halant"</samp> for pre-base consonants, but <samp>"Halant,_Consonant_"</samp>
for post-base consonants.

> Note: Uniscribe is known to make an exception to this reordering
> operation for `<knda>` syllables that end in a <samp>"Halant"</samp>
> codepoint. For example:
>
>     BaseC Halant Post-baseC Halant
>
> is _not_ reordered to <samp>"BaseC Post-baseC Halant Halant"</samp>. Further
> details are provided in the [Uniscribe compatibility](notes/uniscribe-bug-compatibility.md#kannada-final-double-halants) 
> document. 

In addition, for some scripts, left-side dependent vowel marks
(matras) were not repositioned during the final reordering
stage. For `<knda>` text, the left-side matra was always positioned
at the beginning of the syllable.

Finally, in `<knda>` text, the sequence <samp>"Ra,Halant,ZWJ,_consonant_"</samp>
was treated as equivalent to the sequence
<samp>"Ra,ZWJ,Halant,_consonant_"</samp>. The current version of the Unicode
standard states that <samp>"Ra,ZWJ,Halant,_consonant_"</samp> is the correct
sequence, which is meant to trigger the full form of <samp>"Ra"</samp> followed by
the subjoined form of <samp>"_consonant_"</samp>. 

However, Unicode 4.0 specified <samp>"Ra,Halant,ZWJ,_consonant_"</samp>
instead, which was inconsistent with the needs of other Indic
scripts. Even though this sequence was changed with the release of
Unicode 5.0, legacy documents and systems might still be encountered
that use the Unicode 4.0 sequence.

Consequently, shaping engines that encounter a
<samp>"Ra,Halant,ZWJ,_consonant_"</samp> sequence in `<knda>` text should reorder
the sequence to <samp>"Ra,ZWJ,Halant,_consonant_"</samp> or otherwise produce the
same behavior as <samp>"Ra,ZWJ,Halant,_consonant_"</samp>.


### Advice for handling fonts with `<knda>` features only ###

Shaping engines may choose to match post-base <samp>"_Consonant_,Halant"</samp>
sequences in order to apply <abbr title="Glyph Substitution table">GSUB</abbr> substitutions when it is known that
the font in use supports only the `<knda>` shaping model.

### Advice for handling text runs composed in `<knda>` format ###

Shaping engines may choose to match post-base <samp>"_Consonant_,Halant"</samp>
sequences for <abbr title="Glyph Substitution table">GSUB</abbr> substitutions or to reorder them to
<samp>"Halant,_Consonant_"</samp> when processing text runs that are tagged with
the `<knda>` script tag and it is known that the font in use supports
only the `<knd2>` shaping model.

Shaping engines may also choose to position left-side matras according
to the `<knda>` ordering scheme; however, doing so might interfere
with matching <abbr title="Glyph Substitution table">GSUB</abbr> or <abbr title="Glyph Positioning table">GPOS</abbr> features.
