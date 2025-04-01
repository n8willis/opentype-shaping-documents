# Khmer shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Khmer script.


**Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Shaping classes and subclasses](#shaping-classes-and-subclasses)
      - [Khmer character tables](#khmer-character-tables)
  - [The `<khmr>` shaping model](#the-khmr-shaping-model)
      - [Stage 1: Identifying syllables and other sequences](#stage-1-identifying-syllables-and-other-sequences)
      - [Stage 2: Initial reordering](#stage-2-initial-reordering)
      - [Stage 3: Applying the basic substitution features from <abbr>GSUB</abbr>](#stage-3-applying-the-basic-substitution-features-from-gsub)
      - [Stage 4: Applying all remaining substitution features from <abbr>GSUB</abbr>](#stage-4-applying-all-remaining-substitution-features-from-gsub)
      - [Stage 5: Applying remaining positioning features from <abbr>GPOS</abbr>](#stage-5-applying-remaining-positioning-features-from-gpos)


## General information ##

The Khmer or Cambodian script is a descendant of the Brahmi script,
and follows many of the same general patterns found in [Indic
scripts](opentype-shaping-indic-general.md). However, Khmer
incorporates enough distinctions of its own that it is generally not
advisable to attempt supporting it in a general-purpose Indic shaping
engine. 

The Khmer script is used to write multiple languages, most commonly
Khmer, Tampuan, Krung, Cham, and Pali. In addition,
Sanskrit may be written in Khmer, but the Khmer script is not used
for Vedic texts, therefore Khmer text runs are not expected to
include any glyphs from the Vedic Extensions block of Unicode. 

The Khmer script tag defined in OpenType is `<khmr>`.


## Terminology ##

OpenType shaping uses a standard set of terms for Brahmi-derived and
Indic scripts.  The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. Syllables
in Khmer script can include sequences of multiple vowels and,
therefore, multiple matras.

**Halant** and **Virama** are both standard terms for the
vowel-killer" mark. Unicode documents use the term "virama" most 
frequently, while OpenType documents use the term "halant" most
frequently.

The Khmer block does include a version of "halant" mark, "Viriam"
(`U+17D1`). Its usage in Khmer text, however, differs significantly
from the usage of "halant" in other Brahmi-derived and Indic
orthographies.

**Chandrabindu** (or simply **Bindu**) is the standard term for the
diacritical mark indicating that the preceding vowel should be
nasalized. In Khmer, the chandrabindu mark is known as the "nikahit".

The term **base consonant** is also critical to Khmer shaping. The
base consonant of a syllable is the consonant that carries the
syllable's vowel sound, either the inherent vowel (for an unmarked
base consonant) or a dependent vowel (with the addition of a matra). 

Each consonant in Khmer bears one of two inherent vowels. The
two sets of letters that correspond to these inherent vowels are
referred to as **registers**. In Khmer text, a **register shifter**
mark can be used to replace the letter's inherent vowel with the
inherent vowel of the other register.

Some consonants in one register have a corresponding consonant in the
other register; for these consonant pairs, a register shifter is not
employed. 

A syllable's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
syllable frequently take on secondary forms. The **below-base**,
subscript forms of letters are the most frequently seen secondary 
forms.  However, some secondary forms are **post-base**, and the
secondary form of "Ro" is a **pre-base**-reordering form.

These secondary letter forms are known in Khmer as **coeng**
forms. Most coengs are consonants, although, in certain cases,
independent vowels may take on coeng forms. 

The Khmer block of Unicode does not encode the coeng forms of
letters as separate codepoints. Instead, the "Sign Coeng" (`U+17D2`)
codepoint is a control character used to indicate that the following
letter should be rendered in its coeng form. The "Sign Coeng" has no
visual representation of its own. 

> Note: Despite the potentially confusing name in the Unicode
> standard, "Sign Coeng" (`U+17D2`) itself should _not_ be referred to
> as a **coeng**. The term "coeng" refers to the form of the letter
> that follows the "Sign Coeng" control character.

:::{figure-md}
![Coeng form of Kha](images/khmer/khmer-coeng-kha.svg "Coeng form of Kha")

Coeng form of Kha
:::


Although coengs are typically attached to the base consonant of a
syllable, in certain circumstances coengs may also be attached to an
independent vowel. 

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.


## Glyph classification ##

Shaping Khmer text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark. 

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Khmer glyphs must additionally be classified by how they are treated
when shaping a run of text.

### Shaping classes and subclasses ###

The shaping classes listed in the tables that follow are defined so
that they capture the positioning rules used by Khmer script. 

For most codepoints, the _Shaping class_ is synonymous with the `Indic
Syllabic Category` defined in Unicode. However, there are some
distinctions, where the defined category does not fully capture the
behavior of the character in the shaping process.

Several of the diacritic and syllable-modifying marks behave according
to their own rules and, thus, have a special class. These include
`NUKTA` and `VISARGA`. Some less-common marks behave according to
rules that are similar to these common marks, and are therefore
classified with the corresponding common mark. 

> Note: In Khmer, the `NUKTA` class is used for the chandrabindu mark,
> <samp>"Nikahit"</samp> (U+17C6). This more correctly reflects the shaping
> behavior of the nikahit mark than does the `BINDU` class used in
> other scripts.

<samp>"Viriam"</samp> (`U+17D1`), Khmer's "halant"-like codepoint, is classified as
`PURE_KILLER` rather than the more common `VIRAMA`. This is to
indicate that the <samp>"Viriam"</samp> suppresses the inherent vowel of a
consonant but is not used between consonants to trigger the formation
of a subjoined form.

<samp>"Sign Coeng"</samp>, the coeng-form generator, is classified as
`INVISIBLE_STACKER`. This is to indicate that the <samp>"Sign Coeng"</samp>
codepoint itself is never rendered as a visible glyph. 

<samp>"Toandakhiat"</samp> (`U+17CD`) is classified as `CONSONANT_KILLER`. This
mark indicates that the previous consonant is not pronounced. Note
that <samp>"Toandakhiat"</samp> is a diacritic mark, and that its class,
`CONSONANT_KILLER` is not a subclass of consonant.

Letters generally fall into the classes `CONSONANT`,
`VOWEL_INDEPENDENT`, and `VOWEL_DEPENDENT`. These classes help the
shaping engine parse and identify key positions in a syllable. For
example, Unicode categorizes dependent vowels as `Mark [Mn]`, but the
shaping engine must be able to distinguish between dependent vowels
and diacritical marks (which are categorized as `Mark [Mn]`).

Khmer uses one subclass of consonant, `CONSONANT_POST_REPHA`. This
subclass is used only for <samp>"Robat"</samp>, the above-base form of <samp>"Ro"</samp>. The
<samp>"Robat"</samp> is similar to the <samp>"Reph"</samp> found in many Indic scripts but,
unlike <samp>"Reph"</samp>, <samp>"Robat"</samp> is encoded as a separate codepoint; therefore, it is
not formed by a special sequence of control characters.

:::{figure-md}
![Robat](images/khmer/khmer-robat.svg "Robat")

Robat
:::


<samp>"Robat"</samp> is a consonant, but it is classified as a combining mark in
Unicode. For shaping purposes, <samp>"Robat"</samp> behaves like the <samp>"Nukta"</samp> mark
found in many Indic scripts.

The Khmer glottal-stop consonant "Qa" (`U+17A2`) carries an inherent
vowel and is also capable of accepting dependent vowels (matras). It
is sometimes used in place of an independent vowel. For shaping
purposes, however, this usage of "Qa" does not demand any special
treatment.

Other characters, such as symbols and punctuation, need no special
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
the glyphs is determined by the lookups found in the font's <abbr title="Glyph Positioning table">GPOS</abbr>
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
of OpenType <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> features. Shaping engines may, internally,
use whichever terminology is preferred.

Multi-part dependent vowels (matras) may be designated with compound
mark-placement subclasses (such as `TOP_AND_LEFT_POSITION`) that
denote all of the mark-placement positions occupied.

For most mark and dependent-vowel codepoints, the _mark-placement
subclass_ is synonymous with the `Indic Positional Category` defined
in Unicode. However, there are some distinctions, where the defined
category does not fully capture the behavior of the character in the
shaping process. 


### Khmer character tables ###

The Khmer block in Unicode includes all of the codepoints necessary to
write Khmer language text. The Khmer Symbols block contains
miscellaneous symbols used for lunar-date calendars. The Khmer Symbols
codepoints do not evoke any special behavior from the shaping engine.

Separate character tables are provided for the Khmer and Khmer Symbols
blocks as well as for other miscellaneous characters that 
are used in `<khmr>` text runs:

  - [Khmer character table](character-tables/character-tables-khmer.md#khmer-character-table)
  - [Khmer Symbols character table](character-tables/character-tables-khmer.md#khmer-symbols-character-table)
  - [Miscellaneous character table](character-tables/character-tables-khmer.md#miscellaneous-character-table)

The tables list each codepoint along with its Unicode general
category, its shaping class, and its mark-placement subclass. The
codepoint's Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+1780`   | Letter           | CONSONANT         | _null_                     | &#x1780; Ka                  |
| | | | |
|`U+17C6`   | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x17C6; Nikahit             |


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
of Khmer text include the dotted-circle placeholder (`U+25CC`), 
the no-break space (`U+00A0`), and the zero-width space (`U+200B`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

<!--- The zero-width joiner is primarily used to prevent the formation of a
subjoining form from a <samp>"_Consonant_,Halant,_Consonant_"</samp> sequence. The sequence
<samp>"_Consonant_,Halant,ZWJ,_Consonant_"</samp> blocks the substitution of a
subjoined form for the second consonant. --->

<!---
A secondary usage of the zero-width joiner is to prevent the formation of
<samp>"Reph"</samp>. An initial <samp>"Ra,Halant,ZWJ"</samp> sequence should not produce a <samp>"Reph"</samp>,
where an initial <samp>"Ra,Halant"</samp> sequence without the zero-width joiner
otherwise would.
--->

The no-break space (<abbr>NBSP</abbr>) is primarily used to display
those codepoints that are defined as non-spacing (marks, dependent
vowels (matras), below-base consonant forms, and post-base consonant
forms) in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match <samp>"NBSP,ZWJ,Sign_Coeng,_Consonant_"</samp>, <samp>"NBSP,_mark_"</samp>, or
<samp>"NBSP,_matra_"</samp>.

The zero-width space may be used between words — even though no visual
word spacing results — in order to indicate word breaks within a text
that can be used by line-breaking algorithms in a hgher-level
typesetting environment.

Several codepoints in the Khmer block are deprecated and their usage
in new documents is officially discouraged. The deprecated codepoints
are:

  - "Qaq" (`U+17A3`)
  - "Qaa" (`U+17A4`)
  
Usage of three other codepoints is also discouraged, although the
codepoints have not been deprecated. These codepoints are:

  - "Inherent Aq" (`U+17B4`)
  - "Inherent Aaa" (`U+17B5`)
  - "Sign Beyyal" (`U+17D8`)

Although usage of these codepoints in text is discouraged, shaping
engines encountering them in a text run should handle the situation
gracefully.


## The `<khmr>` shaping model ##

Processing a run of `<khmr>` text involves five top-level stages:

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from <abbr>GSUB</abbr>
4. Applying all remaining substitution features from <abbr>GSUB</abbr>
5. Applying all remaining positioning features from <abbr>GPOS</abbr>


As with other Brahmi-derived and Indic scripts, the initial reordering
stage involves applying a set of several script-specific rules. The
basic substitution features must be applied to the run in a specific
order. The remaining substitution features in stage four, however, do
not have a mandatory order.

Khmer exhibits many of the same shaping patterns found in Indic
scripts, but it differs in a few critical characteristics. With regard
to these common variations, Khmer's specific shaping 
characteristics include:


  - The first consonant of a syllable is always the base consonant.

> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `BASE_POS_FIRST`.
  
  - The <samp>"Robat"</samp> form, which is analogous to <samp>"Reph"</samp> or <samp>"Repha"</samp> in Indic
    scripts, in separately encoded as a non-spacing mark
    codepoint. The <samp>"Robat"</samp> form does not require reordering.

> Note: For comparison with the General Indic shaping model, the Robat
> -encoding characteristic would correspond to `REPH_MODE_VISUAL_REPHA`,
> and the reordering characteristic would be _null_ or some other
> designation indicating that the <samp>"Robat"</samp> is not reordered. 
<!---Because 
> <samp>"Robat"</samp> is typically a syllable-initial feature, shaping engines may
> also choose to --->
  
  - The below-base forms feature is applied to consonants
    after the base consonant. 

> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `BLWF_MODE_POST_ONLY`.

  - The ordering position for left-side matras, as with Indic scripts,
    is `POS_PREBASE_MATRA`.

  - The ordering positions for right-side, below-base, and above-base matras is the
    same. All are reordered to immediately after the last post-base consonant.
   	
> Note: For comparison with the General Indic shaping model, this
> characteristic would correspond to `MATRA_POS_TOP`,
> `MATRA_POS_BOTTOM`, and `MATRA_POS_RIGHT` taking the ordering position 
> `POS_AFTER_POST`.


### Stage 1: Identifying syllables and other sequences ###

A syllable in Khmer consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs. 

> Note: The Khmer Unicode block enumerates eight modifier signs,
> "Nikahit" (`U+17C6`), "Reahmuk" (`U+17C7`), "Bantoc" (`U+17CB`),
> "Kakabat" (`U+17CE`),  "Ahsda" (`U+17CF`), "Samyok Sannya"
> (`U+17D0`), "Bathamasat" (`U+17D3`), and "Atthacan" (`U+17DD`). 

Because texts written in Khmer script do not generally employ
inter-word spaces, however, shaping engines must rely on
syllable-identification algorithms to recognize word-boundary
patterns — distinguishing numeric sequences, symbols, punctuation, and other
miscellaneous script characters from syllables within words.

Valid syllables may begin with either a consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that vowel is the
syllable's only vowel sound and, by definition, there is no "base"
consonant. 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the consonant's inherent vowel sound. This vowel sound can be changed
> by a dependent vowel (matra) sign or by a register shifter following the consonant.

For a syllable beginning with a consonant, the base consonant is the
first consonant of the syllable.

Unlike Indic scripts, where the vowel sound designates the end of the
syllable, Khmer syllables can end with final consonants that occur
after a dependent vowel (matra).

All post-base consonants in a valid syllable will be preceded by <samp>"Sign Coeng"</samp>
marks. This includes final consonants.

	BaseC Sign-Coeng Post-baseC Matra Sign-Coeng FinalC
	
In some Khmer words, an independent vowel can occur in a subjoined
position like a post-base consonant. In such instances, the
independent vowel will be preceded by <samp>"Sign Coeng"</samp>.

	BaseC Sign-Coeng IndependentVowel

The algorithms for identifying syllables and for correctly identifying
the base consonant include test to recognize these sequences.


As with other Brahmi-derived and Indic scripts, the consonant <samp>"Ro"</samp> receives
special treatment. 

  - A post-base <samp>"Ro"</samp> must be reordered to a visually pre-base
    position. This move is performed during the initial reordering
    stage.
  - <samp>"Robat"</samp>, the above-base variant of <samp>"Ro"</samp>, is encoded as a combining
    mark rather than as a full consonant. <samp>"Robat"</samp> does not, however,
    require reordering by the shaping engine.

In addition to valid syllables, standalone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Khmer script, may
> not adhere to the syllable-formation rules described above. 


Syllables should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 

The following regular expressions can be used to match Khmer-script
syllables. 

The regular expressions utilize the shaping classes from the tables
above. For the purpose of syllable identification, more general
classes can be used, as defined in the following table. This
simplifies the resulting expressions. 

```markdown
_ra_		= The consonant "Ro" 
_consonant_	= `CONSONANT` - _ra_
_vowel_		= `VOWEL_INDEPENDENT`
_nukta_	  	= `NUKTA` | `CONSONANT_POST_REPHA`
_zwj_		= `JOINER`
_zwnj_		= `NON_JOINER`
_matra_		= `VOWEL_DEPENDENT` | `PURE_KILLER` | `CONSONANT_KILLER`
_syllablemodifier_	= `SYLLABLE_MODIFIER` | `BINDU` | `VISARGA`
_placeholder_	= `PLACEHOLDER` | `CONSONANT_PLACEHOLDER`
_dottedcircle_	= `DOTTED_CIRCLE`
_registershifter_ = `REGISTER_SHIFTER`
_coeng_		= `INVISIBLE_STACKER`
_symbol_	= `SYMBOL` | `AVAGRAHA`
```

> Note: The `CONSONANT_POST_REPHA` shaping class is merged with the
> `NUKTA` shaping class to reflect the correct orthographic behavior
> of <samp>"Robat"</samp>.

These identification classes form the bases of the following regular
expression elements:

```markdown
C	= _consonant_ | _ra_ | _vowel_
N	= (_zwnj_? _registershifter_)? (_nukta_ _nukta_?)?
Z	= _zwj_ | _zwnj_
CN	= C N?
MATRA_GROUP	= Z? _matra_ N?
SYLLABLE_TAIL	= (_syllablemodifier_ _syllablemodifier_?)?
PARTIAL_CLUSTER	= N? (_coeng_ CN)* MATRA_GROUP* (_coeng_ CN)? SYLLABLE_TAIL
```

Using the above elements, the following regular expressions define the
possible syllable types:

A valid syllable will match the expression:
```markdown
(C | _placeholder_ | _dottedcircle_) PARTIAL_CLUSTER
```

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



A sequence that does not match any of these expressions should be
regarded as broken. The shaping engine may make a best-effort attempt
to shape the broken sequence, but making guarantees about the
correctness or appearance of the final result is out of scope for this
document.

After the syllables have been identified, each of the subsequent 
shaping stages occurs on a per-syllable basis.


### Stage 2: Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text to the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs
> and pre-base-reordering <samp>"Ro"</samp>. 
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
which a codepoint might be reordered in Khmer script. 

The position names mimic those used in the General Indic shaping
model, for ease of implementation. However, shaping engines are free
to use any naming scheme they choose. It includes some categories not
utilized in Khmer.

The basic positions (left to right) are <samp>"Reph"</samp> (`POS_RA_TO_BECOME_REPH`), dependent
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

For a definition of the "base" consonant, refer to stage 2, step 1, which follows.


#### Stage 2, step 1: Base consonant ####

The first step is to determine the base consonant of the syllable, if
there is one, and tag it as `POS_BASE_CONSONANT`.

The base consonant is defined as the consonant in a consonant-based
syllable that carries the syllable's vowel sound. That vowel sound
will either be provided by the script's inherent vowel (in which case
it is not written with a separate character) or the sound will be designated
by the addition of a dependent-vowel (matra) sign.

Vowel-based syllables, standalone sequences, and broken text runs will
not have base consonants.

The algorithm for determining the base consonant is

  - Starting from the beginning of the syllable, move forwards until a
    `CONSONANT` is found. 
  - The consonant stopped at will be the base consonant.



#### Stage 2, step 2: Matra decomposition ####

Second, any multi-part dependent vowels (matras) must be decomposed
into their left-side and right-side components. Khmer has five
two-part dependent vowels, "Oe" (`U+17BE`), "Ya" (`U+17BF`), "Ie"
(`U+17C0`), "Oo" (`U+17C4`), and "Au" (`U+17C5`).

Each of these dependent vowels decomposes into a left-side component
identical to the single-part dependent vowel "E" (`U+17C1`) plus a
right-side component.

Unlike many other scripts, the decompositions of multi-part dependent
vowels in Khmer are not defined as canonical in Unicode. Some of the
right-side components that would result from these decompositions do not
correspond to assigned Unicode codepoints.

Instead, fonts often substitute the default glyph with a
right-side-component glyph using <abbr title="Glyph Substitution table">GSUB</abbr> substitutions. The decomposition
step performed here allows the left-side component to be correctly
reordered by the shaping engine.

> "Oe" (`U+17BE`) decomposes to "`U+17C1`,`U+17BE`"
>
> "Ya" (`U+17BF`) decomposes to "`U+17C1`,`U+17BF`"
>
> "Ie" (`U+17C0`) decomposes to "`U+17C1`,`U+17C0`"
>
> "Oo" (`U+17C4`) decomposes to "`U+17C1`,`U+17C4`"
>
> "Au" (`U+17C5`) decomposes to "`U+17C1`,`U+17C5`"

Two of the multi-part dependent vowels, "Oe" (`U+17BE`) and "Oo"
(`U+17C4`), can be decomposed into existing Unicode codepoints. If
desired, the corresponding decompositions are: 

> "Oe" (`U+17BE`) decomposes to "`U+17C1`,`U+17B8`"
>
> "Oo" (`U+17C4`) decomposes to "`U+17C1`,`U+17B6`"

However, shaping engines should take note of the fact that these
decompositions are non-canonical and therefore, if the active font's
design employs non-standard stylistic choices, the results may not
appear as expected.

:::{figure-md}
![Multi-part matra decomposition](images/khmer/khmer-matra-decomposition.svg "Multi-part matra decomposition")

Multi-part matra decomposition
:::


Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.


#### Stage 2, step 3: Tag matras ####

Third, all left-side dependent-vowel (matra) signs must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

All right-side, above-base, and below-base dependent-vowel (matra)
signs are tagged `POS_AFTER_POST`.

For simplicity, shaping engines may choose to tag matras
in an earlier text-processing step, using the information in the
_Mark-placement subclass_ column of the character tables. It is
critical at this step, however, that all matras correctly tagged
before proceeding to the next step. 


<!--- #### Stage 2, step 4: Adjacent marks #### --->
<!--- This does not seem to happen in Khmer. --->
<!--- Commenting out & renumbering. --->


#### Stage 2, step 4: Pre-base-reordering consonants ####

Fourth, all pre-base-reordering consonants must be tagged with
`POS_PREBASE_CONSONANT`. 

Khmer has one pre-base-reordering consonant: <samp>"Ro"</samp>.

:::{figure-md}
![Pre-base-reordering Ro](images/khmer/khmer-pref.svg "Pre-base-reordering Ro")

Pre-base-reordering Ro
:::



#### Stage 2, step 5: Tag remaining consonants ####

Fifth, the remaining consonants and independent vowels should be
tagged with the appropriate positions.

  - All `VOWEL_INDEPENDENT`s and all `CONSONANT`s other than <samp>"Ro"</samp> occurring
    after the base consonant (found in step one) and must be tagged as 
    `POS_BELOWBASE_CONSONANT`. 
  - A `CONSONANT`s or `VOWEL_INDEPENDENT`s in the syllable occurring
    after a dependent vowel (matra) must be tagged as `POS_FINAL_CONSONANT`.

In a valid syllable, such post-base consonants (of class `CONSONANT`)
and independent vowels (of class `VOWEL_INDEPENDENT`) will be preceded by a
<samp>"Sign_Coeng"</samp> glyph. 

> Note: The consonant <samp>"Robat"</samp>, of class `CONSONANT_POST_REPHA`, is not
> included in the classes checked here and must not be tagged in this
> step. <samp>"Robat"</samp> should not appear in a post-base position in a valid
> syllable.



#### Stage 2, step 6: Mark tagging ####

<!--- not sure this is done!!! --->

Sixth, all marks must be tagged. 

Several Khmer marks that are categorized in Unicode as syllable
modifiers or that modify consonants are allowed to occur mid-syllable
in Khmer words. Therefore, they are not tagged for the `POS_SMVD`
position that is typically reserved for syllable modifiers and Vedic
signs.

| Codepoint | Sorting Position        | Glyph                  |
|:----------|:------------------------|:-----------------------|
|`U+17CB`   |`POS_ABOVEBASE_CONSONANT`| &#x17CB; Bantoc        |
|`U+17CD`   |`POS_ABOVEBASE_CONSONANT`| &#x17CD; Toandakhiat   |
|`U+17CE`   |`POS_ABOVEBASE_CONSONANT`| &#x17CE; Kakabat       |
|`U+17CF`   |`POS_ABOVEBASE_CONSONANT`| &#x17CF; Ahsda         |
|`U+17D0`   |`POS_ABOVEBASE_CONSONANT`| &#x17D0; Samyok Sannya |
|`U+17D1`   |`POS_ABOVEBASE_CONSONANT`| &#x17D1; Viriam        |
|`U+17D3`   |`POS_ABOVEBASE_CONSONANT`| &#x17D3; Bathamasat    |
|`U+17DD`   |`POS_ABOVEBASE_CONSONANT`| &#x17DD; Atthacan      |


All remaining marks, including <samp>"Sign Coeng"</samp>, must be tagged with the
same positioning tag as the closest non-mark character the mark has
affinity with, so that they move together during the sorting step.

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

> Note: In this step, joiner and non-joiner characters must also be
> tagged according to the same rules given for marks, even though
> these characters are not categorized as marks in Unicode.
>
> Note: No marks will precede the base consonant in a valid syllable.

With these steps completed, the syllable can be sorted into the final sort order.


### Stage 3: Applying the basic substitution features from <abbr>GSUB</abbr> ###

The basic-substitution stage applies mandatory substitution features
using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this
stage, glyph sequences should be tagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features.

The order in which these substitutions must be performed is fixed:

	locl
	ccmp 
	pref 
	blwf
	abvf
	pstf
	cfar


#### Stage 3, step 1: locl ####

The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> <abbr title="Glyph Substitution table">GSUB</abbr> substitutions in the following steps.

<!--- :::{figure-md}
![Local forms substitution](images/khmer/khmer-locl.svg "Local forms substitution")

Local forms substitution
::: --->



#### Stage 3, step 2: ccmp ####

The `ccmp` feature allows a font to substitute mark-and-base sequences
with a pre-composed glyph including the mark and the base, or to
substitute a single glyph into an equivalent decomposed sequence of glyphs. 
 
If present, these composition and decomposition substitutions must be
performed before applying any other <abbr title="Glyph Substitution table">GSUB</abbr> lookups, because
those lookups may be written to match only the `ccmp`-substituted
glyphs. 

> Note: `ccmp` usage is uncommon in Khmer fonts. Nevertheless,
> shaping engines must apply any `ccmp` substitutions if they are
> present in the active font.


#### Stage 3, step 3: pref ####

The `pref` feature replaces pre-base-consonant glyphs with
any special forms. In Khmer, this typically includes the
pre-base-reordering form of <samp>"Ro"</samp>.

:::{figure-md}
![Pre-base form substitution](/images/khmer/khmer-pref.svg "Pre-base form substitution")

Pre-base form substitution
:::


<!--- be sure to show initial form with Ro BEFORE the base consonant, --->
<!--- since initial reordering has been done already. --->


#### Stage 3, step 4: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. In Khmer, this usually means replacing the default
forms of letters with coeng (or subscript) forms.


<!--- Check below!  --->

The below-base forms feature is applied to glyphs occurring after the
base consonant.

:::{figure-md}
![Below-base form substitution](/images/khmer/khmer-blwf.svg "Below-base form substitution")

Below-base form substitution
:::



#### Stage 3, step 5: abvf ####

The `abvf` feature replaces above-base-consonant glyphs with any
special forms. In Khmer, this may include variant forms of above-base
dependent vowels and marks.
<!--- single-sub-lookup 25, 28 --->

:::{figure-md}
![Above-base form substitution](images/khmer/khmer-abvf.svg "Above-base form substitution")

Above-base form substitution
:::



#### Stage 3, step 6: pstf ####

The `pstf` feature replaces post-base-consonant glyphs with any
special forms. In Khmer, this can include coeng forms of certain
consonants that include an ascending "arm" on the right-hand side as
well as variant forms for right-side matras and marks.

:::{figure-md}
![Post-base form substitution](/images/khmer/khmer-pstf.svg "Post-base form substitution")

Post-base form substitution
:::



#### Stage 3, step 7: cfar ####

The `cfar` feature replaces any below-base-consonant or
post-base-consonant glyphs that occur immediately after a <samp>"Sign
Coeng,Ro"</samp> sequence with special presentation forms. This can include
contextual variants of post-base and below-base glyphs designed to
better interact, visually, with the final position of
pre-base-reordering <samp>"Ro"</samp>.

<!--- Try TRYo--->

<!--- ### 4: Final reordering ### --->
<!--- Is there any? --->

### Stage 4. Applying all remaining substitution features from <abbr>GSUB</abbr> ###

In this stage, the remaining substitution features from the <abbr title="Glyph Substitution table">GSUB</abbr> table
are applied. The order in which these features are applied is not
canonical; they should be applied in the order in which they appear in
the <abbr title="Glyph Substitution table">GSUB</abbr> table in the font. 

	pres
	blws
	abvs
	psts
	calt
	clig
	liga


The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. In Khmer, this can include stylistic variants
of left-side dependent vowels (matras) or of pre-base-reordering <samp>"Ro"</samp>. 

:::{figure-md}
![Pre-base presentation form substitution](/images/khmer/khmer-pres.svg "Pre-base presentation form substitution")

Pre-base presentation form substitution
:::


The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

:::{figure-md}
![Above-base presentation form substitution](/images/khmer/khmer-abvs.svg "Above-base presentation form substitution")

Above-base presentation form substitution
:::



The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. In Khmer, this can include contextual ligatures
involving below-base dependent vowel marks (matras) or subjoined letters.

:::{figure-md}
![Below-base presentation form substitution](/images/khmer/khmer-blws.svg "Below-base presentation form substitution")

Below-base presentation form substitution
:::



The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes stylistic variants of
right-side dependent vowels (matras) or of subjoined letters featuring
right-side ascenders.


:::{figure-md}
![Post-base presentation form substitution](/images/khmer/khmer-psts.svg "Post-base presentation form substitution")

Post-base presentation form substitution
:::


The `clig` feature substitutes optional ligatures that are on by
default, but which are activated only in certain contexts. 

> Note: In some other scripts, substitutions made by `clig` may be
> disabled by application-level user interfaces. For Khmer, however,
> application of `clig` substitutions in mandatory because these
> substitutions are important for typographic correctness, not merely
> for user preference.

:::{figure-md}
![Contextual ligature substitution](images/khmer/khmer-clig.svg "Contextual ligature substitution")

Contextual ligature substitution
:::



The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.

:::{figure-md}
![Standard ligature substitution](/images/khmer/khmer-liga.svg "Standard ligature substitution")

Standard ligature substitution
:::


### Stage 5: Applying remaining positioning features from <abbr>GPOS</abbr> ###

In this stage, mark positioning, kerning, and other <abbr title="Glyph Positioning table">GPOS</abbr> features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the <abbr title="Glyph Positioning table">GPOS</abbr> table in the font.

	dist
	kern
	blwm
	abvm
	mkmk

> Note: The `kern` feature is usually applied at this stage, if it is
> present in the font. However, `kern` is not mandatory for shaping
> Khmer text and may be disabled by user preference.
>
> Notably, the Microsoft Uniscribe shaping engine does not apply
> `kern` lookups even if they are present in the font. For more
> information on Uniscribe compatibility, see the
> [Uniscribe-bug-compatibility note](/notes/uniscribe-bug-compatibility.md).


The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

:::{figure-md}
![Application of the dist feature](/images/khmer/khmer-dist.svg "Application of the dist feature")

Application of the dist feature
:::


The `abvm` feature positions above-base glyphs for attachment to base
characters. In Khmer, this includes register shifters and syllable
modifiers, in addition to diacritical marks and above-base dependent
vowels (matras).

:::{figure-md}
![Above-base mark positioning](/images/khmer/khmer-abvm.svg "Above-base mark positioning")

Above-base mark positioning
:::


The `blwm` feature positions below-base glyphs for attachment to base
characters. In Khmer, this can include coeng forms of letters as well as
below-base dependent vowels (matras).

:::{figure-md}
![Below-base mark positioning](/images/khmer/khmer-blwm.svg "Below-base mark positioning")

Below-base mark positioning
:::


The `mkmk` feature positions marks with respect to preceding marks,
providing proper positioning for sequences of marks that attach to the
same base glyph.
