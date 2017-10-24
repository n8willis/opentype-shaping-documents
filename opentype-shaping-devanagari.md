# Devanagari shaping in OpenType #

This document details the shaping procedure needed to display text
runs in the Devanagari script.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Devanagari character table](#devanagari-character-table)
      - [Devanagari Extended character table](#devanagari-extended-character-table)
      - [Vedic Extensions character table](#vedic-extensions-character-table)
      - [Miscellaneous character table](#miscellaneous-character-table)
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
Extension block of Unicode. 

There are two extant Devanagari script tags defined in OpenType, `<deva>`
xand `<dev2>`. The older script tag, `<deva>`, was deprecated in 2005.
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

### Devanagari character table ###

Devanagari glyphs should be classified as in the following
table. Codepoints in the Devanagari and Devanagari Extended blocks
with no assigned meaning are designated as _unassigned_ in the
_Unicode category_ column.  

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Devanagari blocks, such as
currency marks and other symbols. 

> Symbols, punctuation, and numbers generally evoke no special behavior
> from the shaping engine, but there are OpenType features that
> might affect how the respective glyphs are drawn, such as `tnum`,
> which specifies the usage of tabular-width numerals.

The _Mark-placement subclass_ column indicates mark-placement
positioning for codepoints in the _Mark_ category. Assigned, non-mark
codepoints have a_null_ in this column and evoke no special
mark-placement behavior. Marks tagged with [Mn] in the _Unicode
category_ column are categorized as non-spacing; marks tagged with
[Mc] are categorized as spacing-combining.

Some codepoints in the following table use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0900`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0900; Inverted Candrabindu|
|`U+0901`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0901; Candrabindu         |
|`U+0902`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0902; Anusvara            |
|`U+0903`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0903; Visarga             |
|`U+0904`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0904; Short A             |
|`U+0905`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0905; A                   |
|`U+0906`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0906; Aa                  |
|`U+0907`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0907; I                   |
|`U+0908`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0908; Ii                  |
|`U+0909`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0909; U                   |
|`U+090A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090A; Uu                  |
|`U+090B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090B; Vocalic R           |
|`U+090C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090C; Vocalic L           |
|`U+090D`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090D; Candra E            |
|`U+090E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090E; Short E             |
|`U+090F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x090F; E                   |
| | | | |
|`U+0910`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0910; Ai                  |
|`U+0911`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0911; Candra O            |
|`U+0912`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0912; Short O             |
|`U+0913`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0913; O                   |
|`U+0914`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0914; Au                  |
|`U+0915`   | Letter           | CONSONANT         | _null_                     | &#x0915; Ka                  |
|`U+0916`   | Letter           | CONSONANT         | _null_                     | &#x0916; Kha                 |
|`U+0917`   | Letter           | CONSONANT         | _null_                     | &#x0917; Ga                  |
|`U+0918`   | Letter           | CONSONANT         | _null_                     | &#x0918; Gha                 |
|`U+0919`   | Letter           | CONSONANT         | _null_                     | &#x0919; Nga                 |
|`U+091A`   | Letter           | CONSONANT         | _null_                     | &#x091A; Ca                  |
|`U+091B`   | Letter           | CONSONANT         | _null_                     | &#x091B; Cha                 |
|`U+091C`   | Letter           | CONSONANT         | _null_                     | &#x091C; Ja                  |
|`U+091D`   | Letter           | CONSONANT         | _null_                     | &#x091D; Jha                 |
|`U+091E`   | Letter           | CONSONANT         | _null_                     | &#x091E; Nya                 |
|`U+091F`   | Letter           | CONSONANT         | _null_                     | &#x091F; Tta                 |
| | | | |
|`U+0920`   | Letter           | CONSONANT         | _null_                     | &#x0920; Ttha                |
|`U+0921`   | Letter           | CONSONANT         | _null_                     | &#x0921; Dda                 |
|`U+0922`   | Letter           | CONSONANT         | _null_                     | &#x0922; Ddha                |
|`U+0923`   | Letter           | CONSONANT         | _null_                     | &#x0923; Nna                 |
|`U+0924`   | Letter           | CONSONANT         | _null_                     | &#x0924; Ta                  |
|`U+0925`   | Letter           | CONSONANT         | _null_                     | &#x0925; Tha                 |
|`U+0926`   | Letter           | CONSONANT         | _null_                     | &#x0926; Da                  |
|`U+0927`   | Letter           | CONSONANT         | _null_                     | &#x0927; Dha                 |
|`U+0928`   | Letter           | CONSONANT         | _null_                     | &#x0928; Na                  |
|`U+0929`   | Letter           | CONSONANT         | _null_                     | &#x0929; Nnna                |
|`U+092A`   | Letter           | CONSONANT         | _null_                     | &#x092A; Pa                  |
|`U+092B`   | Letter           | CONSONANT         | _null_                     | &#x092B; Pha                 |
|`U+092C`   | Letter           | CONSONANT         | _null_                     | &#x092C; Ba                  |
|`U+092D`   | Letter           | CONSONANT         | _null_                     | &#x092D; Bha                 |
|`U+092E`   | Letter           | CONSONANT         | _null_                     | &#x092E; Ma                  |
|`U+092F`   | Letter           | CONSONANT         | _null_                     | &#x092F; Ya                  |
| | | | |
|`U+0930`   | Letter           | CONSONANT         | _null_                     | &#x0930; Ra                  |
|`U+0931`   | Letter           | CONSONANT         | _null_                     | &#x0931; Rra                 |
|`U+0932`   | Letter           | CONSONANT         | _null_                     | &#x0932; La                  |
|`U+0933`   | Letter           | CONSONANT         | _null_                     | &#x0933; Lla                 |
|`U+0934`   | Letter           | CONSONANT         | _null_                     | &#x0934; Llla                |
|`U+0935`   | Letter           | CONSONANT         | _null_                     | &#x0935; Va                  |
|`U+0936`   | Letter           | CONSONANT         | _null_                     | &#x0936; Sha                 |
|`U+0937`   | Letter           | CONSONANT         | _null_                     | &#x0937; Ssa                 |
|`U+0938`   | Letter           | CONSONANT         | _null_                     | &#x0938; Sa                  |
|`U+0939`   | Letter           | CONSONANT         | _null_                     | &#x0939; Ha                  |
|`U+093A`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x093A; Sign Oe             |
|`U+093B`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x093B; Sign Ooe            |
|`U+093C`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x093C; Nukta               |
|`U+093D`   | Letter           | AVAGRAHA          | _null_                     | &#x093D; Avagraha            |
|`U+093E`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x093E; Sign Aa             |
|`U+093F`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x093F; Sign I              |
| | | | |
|`U+0940`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0940; Sign Ii             |
|`U+0941`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0941; Sign U              |
|`U+0942`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0942; Sign Uu             |
|`U+0943`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0943; Sign Vocalic R      |
|`U+0944`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0944; Sign Vocalic Rr     |
|`U+0945`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0945; Sign Candra E       |
|`U+0946`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0946; Sign Short E        |
|`U+0947`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0947; Sign E              |
|`U+0948`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0948; Sign Ai             |
|`U+0949`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0949; Sign Candra O       |
|`U+094A`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x094A; Sign Short O        |
|`U+094B`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x094B; Sign O              |
|`U+094C`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x094C; Sign Au             |
|`U+094D`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x094D; Virama              |
|`U+094E`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x094E; Sign Prishthamatra E|
|`U+094F`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x094F; Sign Aw             |
| | | | |
|`U+0950`   | Mark [Mc]        | _null_            | _null_                     | &#x0950; Om                  |
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0953`   | Mark [Mn]        | _null_            | TOP_POSITION               | &#x0953; Grave accent        |
|`U+0954`   | Mark [Mn]        | _null_            | TOP_POSITION               | &#x0954; Acute accent        |
|`U+0955`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0955; Sign Candra Long E  |
|`U+0956`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0956; Sign Ue             |
|`U+0957`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0957; Sign Uue            |
|`U+0958`   | Letter           | CONSONANT         | _null_                     | &#x0958; Qa                  |
|`U+0959`   | Letter           | CONSONANT         | _null_                     | &#x0959; Khha                |
|`U+095A`   | Letter           | CONSONANT         | _null_                     | &#x095A; Ghha                |
|`U+095B`   | Letter           | CONSONANT         | _null_                     | &#x095B; Za                  |
|`U+095C`   | Letter           | CONSONANT         | _null_                     | &#x095C; Dddha               |
|`U+095D`   | Letter           | CONSONANT         | _null_                     | &#x095D; Rha                 |
|`U+095E`   | Letter           | CONSONANT         | _null_                     | &#x095E; Fa                  |
|`U+095F`   | Letter           | CONSONANT         | _null_                     | &#x095F; Yya                 |
| | | | |
|`U+0960`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0960; Vocalic Rr          |
|`U+0961`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0961; Vocalic Ll          |
|`U+0962`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0962; Sign Vocalic L      |
|`U+0963`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0963; Sign Vocalic Ll     |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |
|`U+0966`   | Number           | _null_            | _null_                     | &#x0966; Digit Zero          |
|`U+0967`   | Number           | _null_            | _null_                     | &#x0967; Digit One           |
|`U+0968`   | Number           | _null_            | _null_                     | &#x0968; Digit Two           |
|`U+0969`   | Number           | _null_            | _null_                     | &#x0969; Digit Three         |
|`U+096A`   | Number           | _null_            | _null_                     | &#x096A; Digit Four          |
|`U+096B`   | Number           | _null_            | _null_                     | &#x096B; Digit Five          |
|`U+096C`   | Number           | _null_            | _null_                     | &#x096C; Digit Six           |
|`U+096D`   | Number           | _null_            | _null_                     | &#x096D; Digit Seven         |
|`U+096E`   | Number           | _null_            | _null_                     | &#x096E; Digit Eight         |
|`U+096F`   | Number           | _null_            | _null_                     | &#x096F; Digit Nine          |
| | | | |
|`U+0970`   | Punctuation      | _null_            | _null_                     | &#x0970; Abbreviation Sign   |
|`U+0971`   | Punctuation      | _null_            | _null_                     | &#x0971; Sign High Spacing Dot|
|`U+0972`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0972; Candra Aa           |
|`U+0973`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0973; Oe                  |
|`U+0974`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0974; Ooe                 |
|`U+0975`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0975; Aw                  |
|`U+0976`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0976; Ue                  |
|`U+0977`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0977; Uue                 |
|`U+0978`   | Letter           | CONSONANT         | _null_                     | &#x0978; Marwari Dda         |
|`U+0979`   | Letter           | CONSONANT         | _null_                     | &#x0979; Zha                 |
|`U+097A`   | Letter           | CONSONANT         | _null_                     | &#x097A; Heavy Ya            |
|`U+097B`   | Letter           | CONSONANT         | _null_                     | &#x097B; Gga                 |
|`U+097C`   | Letter           | CONSONANT         | _null_                     | &#x097C; Jja                 |
|`U+097D`   | Letter           | CONSONANT         | _null_                     | &#x097D; Glottal Stop        |
|`U+097E`   | Letter           | CONSONANT         | _null_                     | &#x097E; Ddda                |
|`U+097F`   | Letter           | CONSONANT         | _null_                     | &#x097F; Bba                 |



### Devanagari Extended character table ###


| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+A8E0`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E0; Combining Zero      |
|`U+A8E1`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E1; Combining One       |
|`U+A8E2`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E2; Combining Two       |
|`U+A8E3`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E3; Combining Three     |
|`U+A8E4`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E4; Combining Four      |
|`U+A8E5`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E5; Combining Five      |
|`U+A8E6`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E6; Combining Six       |
|`U+A8E7`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E7; Combining Seven     |
|`U+A8E8`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E8; Combining Eight     |
|`U+A8E9`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8E9; Combining Nine      |
|`U+A8EA`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8EA; Combining A         |
|`U+A8EB`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8EB; Combining U         |
|`U+A8EC`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8EC; Combining Ka        |
|`U+A8ED`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8ED; Combining Na        |
|`U+A8EE`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8EE; Combining Pa        |
|`U+A8EF`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8EF; Combining Ra        |
| | | | |
|`U+A8F0`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8F0; Combining Vi        |
|`U+A8F1`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#xA8F1; Combining Avagraha  |
|`U+A8F2`   | Letter           | BINDU             | _null_                     | &#xA8F2; Spacing Candrabindu |
|`U+A8F3`   | Letter           | BINDU             | _null_                     | &#xA8F3; Candrabindu Virama  |
|`U+A8F4`   | Letter           | _null_            | _null_                     | &#xA8F4; Double Candrabindu Virama|
|`U+A8F5`   | Letter           | _null_            | _null_                     | &#xA8F5; Candrabindu Two     |
|`U+A8F6`   | Letter           | _null_            | _null_                     | &#xA8F6; Candrabindu Three   |
|`U+A8F7`   | Letter           | _null_            | _null_                     | &#xA8F7; Candrabindu Avagraha|
|`U+A8F8`   | Punctuation      | _null_            | _null_                     | &#xA8F8; Pushpika            |
|`U+A8F9`   | Punctuation      | _null_            | _null_                     | &#xA8F9; Gap Filler          |
|`U+A8FA`   | Punctuation      | _null_            | _null_                     | &#xA8FA; Caret               |
|`U+A8FB`   | Letter           | _null_            | _null_                     | &#xA8FB; Headstroke          |
|`U+A8FC`   | Punctuation      | _null_            | _null_                     | &#xA8FC; Siddham             |
|`U+A8FD`   | Letter           | _null_            | _null_                     | &#xA8FD; Jain Om             |
|`U+A8FE`   | _unassigned_     |                   |                            |                              |
|`U+A8FF`   | _unassigned_     |                   |                            |                              |


### Vedic Extensions character table ###

Sanskrit runs written in the Devanagari script may also include
characters from the Vedic Extensions block. These characters should be
classified as follows.

> Note: See the [Vedic Extensions](opentype-shaping-vedic-extensions.md) 
> document for additional infomation.

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
of Devanagari text include the dotted-circle placeholder (`U+25CC`), the
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

With regard to the common variations seen among Indic scripts, 
Devanagari's specific shaping characteristics include:

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
begin with either consonant or an independent vowel. 

If the syllable begins with a consonant, then the consonant that
provides the vowel sound is referred to as the "base" consonant. If
the syllable begins with an independent vowel, that vowel is the
syllable's only vowel sound and, by definition, there is no "base"
consonant. 

> Note: A consonant that is not accompanied by a dependent vowel (matra) sign
> carries the script's inherent vowel sound. This vowel sound is changed
> by a dependent vowel (matra) sign following the consonant.

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
treatment; in many circumstances it is replaced by a combining
mark-like form. A "Ra,Halant" sequence at the beginning of a syllable
is replaced with an above-base mark called "Reph" (unless the "Ra"
is the only consonant in the syllable). 

This rule is synonymous with the `REPH_MODE_IMPLICIT`
characteristic mentioned earlier.

"Ra,Halant" sequences that occur elsewhere in the syllable may take on the
below-base form "Rakaar." "Reph" and "Rakaar" syllables must be
reordered after the syllable-identification stage is complete.



In addition to valid syllables, stand-alone sequences may occur, such
as when an isolated codepoint is shown in example text.

> Note: Foreign loanwords, when written in the Devanagari script, may
> not adhere to the syllable-formation rules described above. In
> particular, it is not uncommon to encounter foregin loanwords that
> contain a word-final suffix of consonants.
>
> Nevertheless, such word-final suffixes will be correctly matched by
> the regular expressions listed below. These words are pronounced
> different, which raises issues for potential readers, but the
> character sequences do not affect the shaping process.



Syllables should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 

The following general-purpose Indic-shaping regular expressions can be
used to match Devanagari syllables. The regular expressions utilize the
shaping classifications from the tables above.


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

The above sort order is the same for all Indic scripts and,
consequently, includes some ordering categories not utilized in
Devanagari.

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

Shaping engines may choose any method to identify consonants that have
below-base or post-base forms while executing the above algorithm. For
example, one implementation may choose to maintain a static table of
below-base and post-base consonants to compare again the text
run. Another implementation might examine the active font to see if it
includes a relevant `blwf` or `pstf` lookup in the GSUB table.

> Note: The algorithm is designed to work for all Indic
> scripts. However, Devanagari does not utilize pre-base reordering "Ra".


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

#### 2.3: Left matras ####

Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be
moved to the beginning of the syllable, with `POS_PREBASE_MATRA`.



#### 2.4: Adjacent marks ####

Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s,
syllable modifiers, and Vedic signs) must be reordered so that they
appear in canonical order. 

For `<dev2>` text, the canonical ordering means that any "Nukta"s must
be placed before all other marks. No other marks in the subsequence
should be reordered.

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
(matra) sign must be tagged with `POS_POSTBASE_CONSONANT`. 

In Devanagari, the only consonant that can appear in this position is
a "Ra,Halant" sequence, which will take on the "Rakaar" form when the
`blwf` feature is applied.

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

