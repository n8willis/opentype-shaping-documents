# Bengali shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Bengali script.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Bengali character table](#bengali-character-table)
      - [Vedic Extensions character table](#vedic-extensions-character-table)
      - [Miscellaneous character table](#miscellaneous-character-table)
  - [The `<bng2>` shaping model](#the-bng2-shaping-model)
      - [1: Identifying syllables and other sequences](#1-identifying-syllables-and-other-sequences)
      - [2: Initial reordering](#2-initial-reordering)
      - [3: Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [4: Final reordering](#4-final-reordering)
      - [5: Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [6: Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)
  - [The `<beng>` shaping model](#the-beng-shaping-model)
      - [Distinctions from `<bng2>`](#distinctions-from-bng2)
      - [Advice for handling fonts with `<beng>` features only](#advice-for-handling-fonts-with-beng-features-only)
      - [Advice for handling text runs composed in `<beng>` format](#advice-for-handling-text-runs-composed-in-beng-format)

<!-- markdown-toc end -->


## General information ##

The Bengali or Bangla script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
sequences of adjacent consonants are often represented as conjuncts.

The Bengali script is used to write multiple languages, most commonly
Bengali, Assamese, and Manipuri. In addition, Sanskrit may be written
in Bengali, so Bengali script runs may include glyphs from the Vedic
Extension block of Unicode. 

There are two extant Bengali script tags defined in OpenType, `<beng>`
and `<bng2>`. The older script tag, `<beng>`, was deprecated in 2008.
Therefore, new fonts should be engineered to work with the `<bng2>`
shaping model. However, if a font is encountered that supports only
`<beng>`, the shaping engine should deal with it gracefully.

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used colloquially in any particular language may vary, however,
potentially causing confusion.

**Matra** is the standard term for a dependent vowel sign. In the Bengali
language, dependent-vowel signs <!--- that are positioned below the base
consonant --> may also be referred to as _kar_ forms — e.g., "i-kar" or
"u-kar".

The term "matra" is also used to refer to the headline above most
Bengali letters. To avoid ambiguity, the term **headline** is
used in most Unicode and OpenType shaping documents.

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. Unicode documents use the term "virama" most frequently, while
OpenType documents use the term "halant" most frequently. In the Bengali
language, this sign is known as the _hasanta_.

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel should be nasalized. In the Bengali
language, this mark is known as the _candrabindu_.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## Glyph classification ##

Shaping Bengali text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and various types
of diacritical mark. 

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as glyph reordering). Therefore,
Bengali glyphs must additionally be classified by how they are treated
when shaping a run of text.


### Bengali character table ###

Bengali glyphs should be classified as in the following
table. Codepoints in the Bengali block with no assigned meaning are
marked as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints marked with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Bengali block, such as
currency marks and other symbols. 

> Symbols, punctuation, and numbers generally evoke no special behavior
> from the shaping engine, but there are OpenType features that
> might affect how the respective glyphs are drawn, such as `tnum`,
> which specifies the usage of tabular-width numerals.

The _Mark-placement subclass_ column indicates mark-placement
positioning. Assigned codepoints marked with a
_null_ in this column evoke no special mark-placement behavior. Marks
tagged with [Mn] in the _Unicode category_ column are categorized as
non-spacing; marks tagged with [Mc] are categorized as
spacing-combining.

Some codepoints in the following table use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.


| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0980`   | Letter           | _null_            | _null_                     | &#x0980; Anji                |
|`U+0981`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0981; Candrabindu         |
|`U+0982`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0982; Anusvara            |
|`U+0983`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0983; Visarga             |
|`U+0984`   | _unassigned_     |                   |                            |                              |
|`U+0985`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0985; A                   |
|`U+0986`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0986; Aa                  |
|`U+0987`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0987; I                   |
|`U+0988`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0988; Ii                  |
|`U+0989`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0989; U                   |
|`U+098A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098A; Uu                  |
|`U+098B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098B; Vocalic R           |
|`U+098C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098C; Vocalic L           |
|`U+098D`   | _unassigned_     |                   |                            |                              |
|`U+098E`   | _unassigned_     |                   |                            |                              |
|`U+098F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098F; E                   |
| | | | |																	   
|`U+0990`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0990; Ai                  |
|`U+0991`   | _unassigned_     |                   |                            |                              |
|`U+0992`   | _unassigned_     |                   |                            |                              |
|`U+0993`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0993; O                   |
|`U+0994`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0994; Au                  |
|`U+0995`   | Letter           | CONSONANT         | _null_                     | &#x0995; Ka                  |
|`U+0996`   | Letter           | CONSONANT         | _null_                     | &#x0996; Kha                 |
|`U+0997`   | Letter           | CONSONANT         | _null_                     | &#x0997; Ga                  |
|`U+0998`   | Letter           | CONSONANT         | _null_                     | &#x0998; Gha                 |
|`U+0999`   | Letter           | CONSONANT         | _null_                     | &#x0999; Nga                 |
|`U+099A`   | Letter           | CONSONANT         | _null_                     | &#x099A; Ca                  |
|`U+099B`   | Letter           | CONSONANT         | _null_                     | &#x099B; Cha                 |
|`U+099C`   | Letter           | CONSONANT         | _null_                     | &#x099C; Ja                  |
|`U+099D`   | Letter           | CONSONANT         | _null_                     | &#x099D; Jha                 |
|`U+099E`   | Letter           | CONSONANT         | _null_                     | &#x099E; Nya                 |
|`U+099F`   | Letter           | CONSONANT         | _null_                     | &#x099F; Tta                 |
| | | | |																	   
|`U+09A0`   | Letter           | CONSONANT         | _null_                     | &#x09A0; Ttha                |
|`U+09A1`   | Letter           | CONSONANT         | _null_                     | &#x09A1; Dda                 |
|`U+09A2`   | Letter           | CONSONANT         | _null_                     | &#x09A2; Ddha                |
|`U+09A3`   | Letter           | CONSONANT         | _null_                     | &#x09A3; Nna                 |
|`U+09A4`   | Letter           | CONSONANT         | _null_                     | &#x09A4; Ta                  |
|`U+09A5`   | Letter           | CONSONANT         | _null_                     | &#x09A5; Tha                 |
|`U+09A6`   | Letter           | CONSONANT         | _null_                     | &#x09A6; Da                  |
|`U+09A7`   | Letter           | CONSONANT         | _null_                     | &#x09A7; Dha                 |
|`U+09A8`   | Letter           | CONSONANT         | _null_                     | &#x09A8; Na                  |
|`U+09A9`   | _unassigned_     |                   |                            |                              |
|`U+09AA`   | Letter           | CONSONANT         | _null_                     | &#x09AA; Pa                  |
|`U+09AB`   | Letter           | CONSONANT         | _null_                     | &#x09AB; Pha                 |
|`U+09AC`   | Letter           | CONSONANT         | _null_                     | &#x09AC; Ba                  |
|`U+09AD`   | Letter           | CONSONANT         | _null_                     | &#x09AD; Bha                 |
|`U+09AE`   | Letter           | CONSONANT         | _null_                     | &#x09AE; Ma                  |
|`U+09AF`   | Letter           | CONSONANT         | _null_                     | &#x09AF; Ya                  |
| | | | |																	    
|`U+09B0`   | Letter           | CONSONANT         | _null_                     | &#x09B0; Ra                  |
|`U+09B1`   | _unassigned_     |                   |                            |                              |
|`U+09B2`   | Letter           | CONSONANT         | _null_                     | &#x09B2; La                  |
|`U+09B3`   | _unassigned_     |                   |                            |                              |
|`U+09B4`   | _unassigned_     |                   |                            |                              |
|`U+09B5`   | _unassigned_     |                   |                            |                              |
|`U+09B6`   | Letter           | CONSONANT         | _null_                     | &#x09B6; Sha                 |
|`U+09B7`   | Letter           | CONSONANT         | _null_                     | &#x09B7; Ssa                 |
|`U+09B8`   | Letter           | CONSONANT         | _null_                     | &#x09B8; Sa                  |
|`U+09B9`   | Letter           | CONSONANT         | _null_                     | &#x09B9; Ha                  |
|`U+09BA`   | _unassigned_     |                   |                            |                              |
|`U+09BB`   | _unassigned_     |                   |                            |                              |
|`U+09BC`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x09BC; Nukta               |
|`U+09BD`   | Letter           | AVAGRAHA          | _null_                     | &#x09BD; Avagraha            |
|`U+09BE`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09BE; Sign Aa             |
|`U+09BF`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09BF; Sign I              |
| | | | |																	   
|`U+09C0`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09C0; Sign Ii             |
|`U+09C1`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C1; Sign U              |
|`U+09C2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C2; Sign Uu             |
|`U+09C3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C3; Sign Vocalic R      |
|`U+09C4`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C4; Sign Vocalic Rr     |
|`U+09C5`   | _unassigned_     |                   |                            |                              |
|`U+09C6`   | _unassigned_     |                   |                            |                              |
|`U+09C7`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C7; Sign E              |
|`U+09C8`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C8; Sign Ai             |
|`U+09C9`   | _unassigned_     |                   |                            |                              |
|`U+09CA`   | _unassigned_     |                   |                            |                              |
|`U+09CB`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CB; Sign O              |
|`U+09CC`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CC; Sign Au             |
|`U+09CD`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x09CD; Virama              |
|`U+09CE`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x09CE; Khanda Ta           |
|`U+09CF`   | _unassigned_     |                   |                            |                              |
| | | | |																	   
|`U+09D0`   | _unassigned_     |                   |                            |                              |
|`U+09D1`   | _unassigned_     |                   |                            |                              |
|`U+09D2`   | _unassigned_     |                   |                            |                              |
|`U+09D3`   | _unassigned_     |                   |                            |                              |
|`U+09D4`   | _unassigned_     |                   |                            |                              |
|`U+09D5`   | _unassigned_     |                   |                            |                              |
|`U+09D6`   | _unassigned_     |                   |                            |                              |
|`U+09D7`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09D7; Au Length Mark      |
|`U+09D8`   | _unassigned_     |                   |                            |                              |
|`U+09D9`   | _unassigned_     |                   |                            |                              |
|`U+09DA`   | _unassigned_     |                   |                            |                              |
|`U+09DB`   | _unassigned_     |                   |                            |                              |
|`U+09DC`   | Letter           | CONSONANT         | _null_                     | &#x09DC; Rra                 |
|`U+09DD`   | Letter           | CONSONANT         | _null_                     | &#x09DD; Rha                 |
|`U+09DE`   | _unassigned_     |                   |                            |                              |
|`U+09DF`   | Letter           | CONSONANT         | _null_                     | &#x09DF; Yya                 |
| | | | |																	   
|`U+09E0`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x09E0; Vocalic Rr          |
|`U+09E1`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x09E1; Vocalic Ll          |
|`U+09E2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E2; Sign Vocalic L      |
|`U+09E3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E3; Sign Vocalic Ll     |
|`U+09E4`   | _unassigned_     |                   |                            |                              |
|`U+09E5`   | _unassigned_     |                   |                            |                              |
|`U+09E6`   | Number           | NUMBER            | _null_                     | &#x09E6; Digit Zero          |
|`U+09E7`   | Number           | NUMBER            | _null_                     | &#x09E7; Digit One           |
|`U+09E8`   | Number           | NUMBER            | _null_                     | &#x09E8; Digit Two           |
|`U+09E9`   | Number           | NUMBER            | _null_                     | &#x09E9; Digit Three         |
|`U+09EA`   | Number           | NUMBER            | _null_                     | &#x09EA; Digit Four          |
|`U+09EB`   | Number           | NUMBER            | _null_                     | &#x09EB; Digit Five          |
|`U+09EC`   | Number           | NUMBER            | _null_                     | &#x09EC; Digit Six           |
|`U+09ED`   | Number           | NUMBER            | _null_                     | &#x09ED; Digit Seven         |
|`U+09EE`   | Number           | NUMBER            | _null_                     | &#x09EE; Digit Eight         |
|`U+09EF`   | Number           | NUMBER            | _null_                     | &#x09EF; Digit Nine          |
| | | | |
|`U+09F0`   | Letter           | CONSONANT         | _null_                     | &#x09F0; Assamese Ra         |
|`U+09F1`   | Letter           | CONSONANT         | _null_                     | &#x09F1; Assamese Wa         |
|`U+09F2`   | Symbol           | _null_            | _null_                     | &#x09F2; Rupee Mark          |
|`U+09F3`   | Symbol           | _null_            | _null_                     | &#x09F3; Rupee Sign          |
|`U+09F4`   | Number           | _null_            | _null_                     | &#x09F4; Numerator One       |
|`U+09F5`   | Number           | _null_            | _null_                     | &#x09F5; Numerator Two       |
|`U+09F6`   | Number           | _null_            | _null_                     | &#x09F6; Numerator Three     |
|`U+09F7`   | Number           | _null_            | _null_                     | &#x09F7; Numerator Four      |
|`U+09F8`   | Number           | _null_            | _null_                     | &#x09F8; Numerator One Less Than Denominator |
|`U+09F9`   | Number           | _null_            | _null_                     | &#x09F9; Denominator Sixteen |
|`U+09FA`   | Symbol           | _null_            | _null_                     | &#x09FA; Isshar              |
|`U+09FB`   | Symbol           | _null_            | _null_                     | &#x09FB; Ganda Mark          |
|`U+09FC`   | Letter           | _null_            | _null_                     | &#x09FC; Vedic Anusvara      |
|`U+09FD`   | Punctuation      | _null_            | _null_                     | &#x09FD; Abbreviation Sign   |
|`U+09FE`   | _unassigned_     |                   |                            |                              |
|`U+09FF`   | _unassigned_     |                   |                            |                              |
 

### Vedic Extenstions character table ###

Sanskrit runs written in the Bengali script may also include
characters from the Vedic Extensions block. These characters should be
classified as follows:

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+1CD0`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CD0; Tone Karshana       |
|`U+1CD1`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CD1; Tone Shara          |
|`U+1CD2`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CD2; Tone Prenkha        |
|`U+1CD3`   | Punctuation      | _null_            | _null_                     | &#x1CD3; Sign Nihshvasa      |
|`U+1CD4`   | Mark [Mn]        | CANTILLATION      | OVERSTRUCK                 | &#x1CD4; Tone Midline Svarita |
|`U+1CD5`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CD5; Tone Aggravated Independent Svarita |
|`U+1CD6`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CD6; Tone Independent Svarita |
|`U+1CD7`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CD7; Tone Kathaka Independent Svarita |
|`U+1CD8`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CD8; Tone Candra Below   |
|`U+1CD9`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CD9; Tone Kathaka Independent Svarita Schroeder |
|`U+1CDA`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CDA; Tone Double Svarita |
|`U+1CDB`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CDB; Tone Triple Svarita |
|`U+1CDC`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CDC; Tone Kathaka Anudatta |
|`U+1CDD`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CDD; Tone Dot Below      |
|`U+1CDE`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CDE; Tone Two Dots Below |
|`U+1CDF`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x1CDF; Tone Three Dots Below |
| | | | |																		
|`U+1CE0`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CE0; Tone Rigvedic Kashmiri Independent Svarita |
|`U+1CE1`   | Mark [Mc]        | CANTILLATION      | RIGHT_POSITION             | &#x1CE1; Tone Atharavedic Independent Svarita |
|`U+1CE2`   | Mark [Mn]        | AVAGRAHA          | OVERSTRUCK                 | &#x1CE2; Sign Visarga Svarita |
|`U+1CE3`   | Mark [Mn]        | _null_            | OVERSTRUCK                 | &#x1CE3; Sign Visarga Udatta |
|`U+1CE4`   | Mark [Mn]        | _null_            | OVERSTRUCK                 | &#x1CE4; Sign Reversed Visarga Udatta |
|`U+1CE5`   | Mark [Mn]        | _null_            | OVERSTRUCK                 | &#x1CE5; Sign Visarga Anudatta |
|`U+1CE6`   | Mark [Mn]        | _null_            | OVERSTRUCK                 | &#x1CE6; Sign Reversed Visarga Anudatta |
|`U+1CE7`   | Mark [Mn]        | _null_            | OVERSTRUCK                 | &#x1CE7; Sign Visarga Udatta With Tail |
|`U+1CE8`   | Mark [Mn]        | AVAGRAHA          | OVERSTRUCK                 | &#x1CE8; Sign Visarga Anudatta With Tail |
|`U+1CE9`   | Letter           | AVAGRAHA          | _null_                     | &#x1CE9; Sign Anusvara Antargomukha |
|`U+1CEA`   | Letter           | _null_            | _null_                     | &#x1CEA; Sign Anusvara Bahirgomukha |
|`U+1CEB`   | Letter           | _null_            | _null_                     | &#x1CEB; Sign Anusvara Vamagomukha |
|`U+1CEC`   | Letter           | AVAGRAHA          | _null_                     | &#x1CEC; Sign Anusvara Vamagomukha With Tail |
|`U+1CED`   | Mark [Mn]        | AVAGRAHA          | BOTTOM_POSITION            | &#x1CED; Sign Tiryak         |
|`U+1CEE`   | Letter           | AVAGRAHA          | _null_                     | &#x1CEE; Sign Hexiform Long Anusvara |
|`U+1CEF`   | Letter           | _null_            | _null_                     | &#x1CEF; Sign Long Anusvara  |
| | | | |																		
|`U+1CF0`   | Letter           | _null_            | _null_                     | &#x1CF0; Sign Rthang Long Anusvara |
|`U+1CF1`   | Letter           | AVAGRAHA          | _null_                     | &#x1CF1; Sign Anusvara Ubhayato Mukha |
|`U+1CF2`   | Mark [Mc]        | VISARGA           | _null_                     | &#x1CF2; Sign Ardhavisarga   |
|`U+1CF3`   | Mark [Mc]        | VISARGA           | _null_                     | &#x1CF3; Sign Rotated Ardhavisarga |
|`U+1CF4`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CF4; Tone Candra Above   |
|`U+1CF5`   | Letter           | CONSONANT         | _null_                     | &#x1CF5; Sign Jihvamuliya    |
|`U+1CF6`   | Letter           | CONSONANT         | _null_                     | &#x1CF6; Sign Upadhmaniya    |
|`U+1CF7`   | Mark [Mc]        | _null_            | _null_                     | &#x1CF7; Sign Atikrama       |
|`U+1CF8`   | Mark [Mn]        | CANTILLATION      | _null_                     | &#x1CF8; Tone Ring Above     |
|`U+1CF9`   | Mark [Mn]        | CANTILLATION      | _null_                     | &#x1CF9; Tone Double Ring Above |
|`U+1CFA`   | _unassigned_     |                   |                            |                              |
|`U+1CFB`   | _unassigned_     |                   |                            |                              |
|`U+1CFC`   | _unassigned_     |                   |                            |                              |
|`U+1CFD`   | _unassigned_     |                   |                            |                              |
|`U+1CFE`   | _unassigned_     |                   |                            |                              |
|`U+1CFF`   | _unassigned_     |                   |                            |                              |



### Miscellaneous character table ###

Other important characters that may be encountered when shaping runs
of Bengali text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel (matra) or a combining mark in isolation. Real-world
text syllables may also use other characters, such as hyphens or dashes,
in a similar placeholder fashion; shaping engines should cope with
this situation gracefully.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+00A0`   | Separator        | PLACEHOLDER       | _null_                     | &#x00A0; No-break space        |
|`U+200C`   | Other            | NON_JOINER        | _null_                     | &#x200C; Zero-width non-joiner |
|`U+200D`   | Other            | JOINER            | _null_                     | &#x200D; Zero-width joiner     |
|`U+2010`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2010; Hyphen                |
|`U+2011`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2011; No-break hyphen       |
|`U+2012`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2012; Figure dash           |
|`U+2013`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2013; En dash               |
|`U+2014`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2014; Em dash               |
|`U+25CC`   | Symbol           | DOTTED_CIRCLE     | _null_                     | &#x25CC; Dotted circle         |


The zero-width joiner is primarily used to prevent the formation of a conjunct
from a "_consonant_,Halant,_consonant_" sequence. The sequence
"_consonant_,Halant,ZWJ,_consonant_" blocks the formation of a
conjunct between the two consonants. 

Note, however, that the "_consonant_,Halant" subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner must be used instead. The sequence
"_consonant_,Halant,ZWNJ,_consonant_" should produce the first
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
"NBSP,ZWJ,Halant,_consonant_", "NBSP,_mark_", or "NBSP,_matra_".

In addition to general punctuation, runs of Bengali text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.



<!-- 1cf5 and 1cf6 get reclassified as CONSONANT

1ce2 and 1ce8 get treated like tone marks, but SHOULD be allowed only after Visarga.

1ced gets treated like tone mark, but SHOULD be allowed only after U+1CE9..U+1CF1

1ce9 1cec 1cee 1cf1 all take marks in standalone clusters, similar to Avagraha.

U+2010 and U+2011 get treated like placeholders.

U+25CC is the dotted circle. --->
<!---
  /* General Punctuation */

  /* 2008 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),_(ZWNJ,x),_(ZWJ,x),  _(x,x),  _(x,x),
  /* 2010 */ _(CP,x), _(CP,x), _(CP,x), _(CP,x), _(CP,x),  _(x,x),  _(x,x),  _(x,x),

#define indic_offset_0x2070u 1672


  /* Superscripts and Subscripts */

  /* 2070 */  _(x,x),  _(x,x),  _(x,x),  _(x,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2078 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2080 */  _(x,x),  _(x,x), _(SM,x), _(SM,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
--->

## The `<bng2>` shaping model ##

Processing a run of `<bng2>` text involves six top-level stages:

1. Identifying syllables and other sequences
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying all remaining positioning features from GPOS


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve invoking a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

<!-- > Note: Bengali differs from Devanagari in that sequences of pre-base consonants
> are generally combined into conjuncts and only less frequently
> rendered in half-forms. -->

With regard to the common variations seen among Indic scripts, 
Bengali's specific shaping characteristics include:

  - `BASE_POS_LAST` = The base consonant of a syllable is the last
     consonant, not counting any special final-consonant forms.

  - `REPH_POS_AFTER_SUBJOINED` = "Reph" is ordered after all subjoined (i.e.,
     below-base) consonant forms.

  - `REPH_MODE_IMPLICIT` = "Reph" is formed by an initial "Ra,Halant" sequence.

  - `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied both to
     pre-base consonants and to post-base consonants.

  - `MATRA_POS_RIGHT` = `POS_AFTER_POST` = Right-side matras are
     ordered after all post-base consonant forms.

  - `MATRA_POS_BOTTOM` = `POS_AFTER_SUBJOINED` = Below-base matras are
     ordered after all subjoined (i.e., below-base) consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how "Reph"
should be encoded within a run of text.

### 1: Identifying syllables and other sequences ###

A syllable in Bengali consists of a valid orthographic sequence
that may be followed by a "tail" of modifier signs.

> Note: The Bengali Unicode block enumerates five modifier signs,
> "Candrabindu" (`U+0981`), "Anusvara" (`U+0982`), "Visarga" 
> (`U+0983`), "Avagraha" (`U+09BD`), and "Vedic Anusvara"
> (`U+09FC`). In addition, Sanskrit text written in Bengali may
> include additional signs from Vedic Extensions block.

Valid syllables may begin with either a consonant or an independent
vowel.

Each syllable contains exactly one vowel. A consonant that is not
accompanied by a dependent vowel (matra) sign carries the script's
inherent vowel. The inherent vowel is suppressed when the consonant is
accompanied by the "Halant" mark. 

The consonant (if any exists) that carries the vowel is the "base"
consonant of the syllable. Zero or more additional consonants may be
present in the syllable; in a valid syllable these other consonants
will be followed by the "Halant" mark, which indicates that they carry
no vowel.

As with other Indic scripts, the consonant "Ra" receives special
treatment; in many circumstances it is replaced with a combining
mark-like form. A "Ra,Halant" sequence at the beginning of a syllable
is replaced with an above-base mark called "Reph" (unless the "Ra"
is the only consonant in the syllable). 

This requirement is synonymous with the `REPH_MODE_IMPLICIT`
characteristic mentioned earlier.

"Ra,Halant" sequences that occur elsewhere in the syllable may take on the
below-base form "Raphala." "Reph" and "Raphala" syllables must be
reordered after the syllable-identification stage is complete.

> Note: `<bng2>` text contains two Unicode codepoints for "Ra."
> `U+09B0` and `U+09F0`. 
>
> `U+09B0` is used in Bengali-language, Manipuri-language, and
> Sanskrit text. `U+09F0` is used in Assamese-language text.
>

In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

Syllables should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 

The following general-purpose Indic-shaping regular expressions can be
used to match Bengali syllables.

> Note: Bengali does not include the Anudatta (`U+0952`). It is
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

A consonant syllable will match the expression:
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

The above sort order is the same for all Indic scripts and,
consequently, includes some ordering categories not utilized in
Bengali.

#### 2.1: Base consonant ####

The first step is to determine the base consonant of the syllable
and tag it as `POS_BASE_CONSONANT`.

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

> Note: The algorithm is designed to work for all Indic
> scripts. However, Bengali does not utilize pre-base reordering "Ra".


#### 2.2: Matra decomposition ####

Second, any two-part dependent vowels (matras) must be decomposed
into their left-side and right-side components. Bengali has two
two-part dependent vowels, "O" (`U+09BC`) and "AU" (`U+09CC`). Each
has a canonical decomposition, so this step is unambiguous. 

> "O" (`U+09BC`) decomposes to "`U+09C7`,`U+09BE`"
>
> "AU" (`U+09CC`) decomposes to "`U+09C7`,`U+09D7`"

Because this decomposition is a character-level operation, the shaping
engine may choose to perform it earlier, such as during an initial
Unicode-normalization stage. However, all such decompositions must be
completed before the shaping engine begins step three, below.

![Two-part matra decomposition](/images/bengali/split-matra-decomposition.png)

#### 2.3: Left matras ####

Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.

#### 2.4: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. For `<bng2>` text, this ordering means that any
"Nukta"s must be placed before all other marks. No other marks in the
subsequence should be reordered.

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
consonants will usually be followed by a "Halant" glyph, with the
exception of two special-case consonants. 

  - "Khanda Ta" (`U+09CE`) is a "dead" consonant variant of "Ta",
    meaning that it carries no inherent vowel, therefore no "Halant"
    follows it.
  - The sequence "Halant,Ya" (`U+09CD`,`U+09AF`)  triggers
    the "Yaphala" form. "Yaphala" behaves like a modifier to the
    pronunciation of the preceding vowel, despite the fact that it is
    formed from a consonant. Because the "Halant" precedes the
    consonant when forming the "Yaphala", no "Halant" follows it.

<!--- and "Halant,Yya"
    (`U+09CD`,`U+09DF`) both ** Not sure about Yya.... --->
	
#### 2.8: Mark tagging ####

Eighth, all marks must be tagged with the same positioning tag as the
closest preceding non-mark character, so that they move together
during the sorting step.

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
	rkrf (not used in Bengali)
	pref (not used in Bengali)
	blwf 
	abvf (not used in Bengali)
	half
	pstf
	vatu
	cjct
	cfar (not used in Bengali)

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

The `nukt` feature replaces "_consonant_,Nukta" sequences with a
precomposed nukta-variant of the consonant glyph. 


![Nukta composition](/images/bengali/nukta-composition.png)

#### 3.3: akhn ####

The `akhn` feature replaces two specific sequences with required ligatures. 

  - "Ka,Halant,Ssa" is substituted with the "KaSsa" ligature. 
  - "Ja,Halant,Nya" is substituted with the "JaNya" ligature. 
  
These sequences can occur anywhere in a syllable. The "KaSsa" and
"JaNya" characters have orthographic status equivalent to full
consonants in some languages, and fonts may have `cjct` substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.

![KaSaa ligation](/images/bengali/kassa-ligation.png)

![JaNya ligation](/images/bengali/janya-ligation.png)

#### 3.4: rphf ####

The `rphf` feature replaces initial "Ra,Halant" sequences with the
"Reph" glyph.

  - An initial "Ra,Halant,ZWJ" sequence, however, must not be tagged for
    the `rphf` substitution.
	

![Reph composition](/images/bengali/reph-composition.png)

#### 3.5: rkrf ####

> This feature is not used in Bengali.

#### 3.6 pref ####

> This feature is not used in Bengali.

<!--- 3.5: The `pref` feature replaces pre-base-consonant glyphs with -->
<!--any special forms. --->

#### 3.7: blwf ####

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Bengali includes two below-base consonant
forms:

  - "Ra,Halant" in a non-syllable-initial position takes on the
    "Raphala" form.
  - "Ba,Halant" takes on the "Baphala" form. 

Because Bengali incorporates the `BLWF_MODE_PRE_AND_POST` shaping
characteristic, any pre-base consonants and any post-base consonants
may potentially match a `blwf` substitution; therefore, both cases must
be tagged for comparison. Note that this is not necessarily the case in other
Indic scripts that use a different `BLWF_MODE_` shaping
characteristic. 


![Raphala composition](/images/bengali/raphala-composition.png)

![Baphala composition](/images/bengali/baphala-composition.png)

#### 3.8: abvf ####

> This feature is not used in Bengali.

#### 3.9: half ####

The `half` feature replaces "_consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs. There are
three exceptions to the default behavior, for which the shaping engine
must test:

  - Initial "Ra,Halant" sequences, which should have been tagged for
    the `rphf` feature earlier, must not be tagged for potential
    `half` substitutions.

  - A sequence matching "_consonant_,Halant,ZWJ,_consonant_" must be
    tagged for potential `half` substitutions, even though the presence of the
    zero-width joiner suppresses the `cjct` feature in a later step.

  - A sequence matching "_consonant_,Halant,ZWNJ,_consonant_" must not be
    tagged for potential `half` substitutions.


![Half-form formation](/images/bengali/half-formation.png)

#### 3.10: pstf ####

The `pstf` feature replaces post-base-consonant glyphs with any special forms.


![Yaphala composition](/images/bengali/yaphala-composition.png)

#### 3.11: vatu ####

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. 

"Vattu variants" are formed from glyphs followed by "Raphala"
(the below-base form of "Ra"); therefore, this feature must be applied after
the `blwf` feature.


![Vattu variant ligation](/images/bengali/vattu-ligation.png)

#### 3.12: cjct ####

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match "_consonant_,Halant,_consonant_".

A sequence matching "_consonant_,Halant,ZWJ,_consonant_" or
"_consonant_,Halant,ZWNJ,_consonant_" must not be tagged to form a conjunct.

The font's GSUB rules might be implemented so that `cjct`
substitutions apply to half-form consonants; therefore, this feature
must be applied after the `half` feature. 


![Conjunct ligation](/images/bengali/pata-conjunct.png)

#### 3.13: cfar ####

> This feature is not used in Bengali.


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
   
#### 4.2: Pre-base matras ####

Pre-base dependent vowels (matras) that were reordered during the
initial reordering stage must be moved to their final position. This
position is defined as:
   
   - after the last standalone "Halant" glyph that comes after the 
     matra's starting position and also comes before the main consonant.
   - If a zero-width joiner or a zero-width non-joiner follows this last
     standalone "Halant", the final matra position is moved to after
     the joiner or non-joiner.

This means that the matra will move to the right of all explicit
"consonant,Halant" subsequences, but will stop to the left of the base
consonant, all conjuncts or ligatures that contains the base
consonant, and all half forms. 

#### 4.3: Reph ####

"Reph" must be moved from the beginning of the syllable to its final
position. Because Bengali incorporates the
`REPH_POS_AFTER_SUBJOINED` shaping characteristic, this final
position is immediately after the base consonant and any subjoined
(below-base consonant or below-base dependent vowel) forms. 

  - If the syllable does not have a base consonant (such as a syllable
    based on an independent vowel), then the final "Reph" position is
    immediately before the first character tagged with the
   `POS_BEFORE_POST` position or any later position in the sort order.

    -- If there are no characters tagged with `POS_BEFORE_POST` or later
       positions, then "Reph" is positioned at the end of the syllable.

Finally, if the final position of "Reph" occurs after a "_matra_,Halant"
subsequence, then "Reph" must be repositioned to the left of "Halant",
to allow for potential matching with `abvs` or `psts` substitutions
from GSUB.

<!--- #### 4.4: Pre-base consonants ####

Any pre-base reordering consonants must be moved to immediately
before the base consonant.
  
  *** Bengali does not use pre-base reordering consonants *** 
  *** This feature is exhibited by Javanese and Balinese. Possibly 
  *** by Devanagari as well....
--->

#### 4.4: Initial matras ####

Any left-side dependent vowels (matras) that are at the start of a
word must be tagged for potential substitution by the `init`
feature of GSUB.
   
<!--- #### 4.6: Cluster merging ####

Clusters must be merged (?) if compatibility with Microsoft
Uniscribe is required.

--->

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
presentation forms. This usually includes replacing consonants that
are followed by below-base-consonant forms like "Raphala" or
"Baphala" with contextual ligatures.

The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures. 

The `haln` feature replaces word-final "_consonant_,Halant" pairs with
special presentation forms. This can include stylistic variants of the
consonant where placing the "Halant" mark on its own is
typographically problematic. 

> Note: The `calt` feature, which allows for generalized application
> of contextual alternate substitutions, is usually applied at this
> point. However, `calt` is not mandatory for correct Bengali shaping
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
> mandatory for shaping Bengali text and may be disabled by user preference.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

The `abvm` feature positions above-base marks for attachment to base
characters. In Bengali, this includes "Reph" in addition to the
diacritical marks and Vedic signs. 

The `blwm` feature positions below-base marks for attachment to base
characters. In Bengali, this includes below-base dependent vowels
(matras) as well as the below-base consonant forms "Raphala" and
"Baphala".


## The `<beng>` shaping model ##

The older Bengali script tag, `<beng>`, has been deprecated. However,
shaping engines may still encounter fonts that were built to work with
`<beng>` and some users may still have documents that were written to
take advantage of `<beng>` shaping.

### Distinctions from `<bng2>` ###

The most significant distinction between the shaping models is that the
sequence of "Halant" and consonant glyphs required to suppress the
inherent vowel (and, for the shaping engine's purposes, to trigger shaping
features) was swapped when migrating from `<beng>` to
`<bng2>`. 

Specifically, the inherent vowel of a consonant in a run of `<beng>`
text was suppressed by the sequence "Halant,_consonant_". In `<bng2>`
text, as described above in this document, the correct sequence is
"_consonant_,Halant".

Consequently, in `<beng>` text, a "Reph" substitution was triggered by a
syllable-initial "Halant,Ra" sequence. In `<bng2>` text, the sequence
must be "Ra,Halant". 

Similarly, in `<beng>` text, a pre-base half-form or
consonant-conjunct substitution was triggered by
"Halant,_consonant_,_consonant_". In `<bng2>` text, the sequence must
be "_consonant_,Halant,_consonant_".

### Advice for handling fonts with `<beng>` features only ###

Shaping engines may choose to match "Halant,_consonant_" sequences in
order to apply GSUB substitutions when it is known that the font in
use supports only the `<beng>` shaping model.

### Advice for handling text runs composed in `<beng>` format ###

Shaping engines may choose to match "Halant,_consonant_" sequences for
GSUB substitutions or to reorder them to "_consonant_,Halant" when
processing text runs that are tagged with the `<beng>` script tag and
it is known that the font in use supports only the `<bng2>` shaping
model.
