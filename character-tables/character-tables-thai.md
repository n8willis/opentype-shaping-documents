# Thai character tables #

This document lists the per-character shaping information needed to
[shape Thai text](../opentype-shaping-thai-lao.md#the-thai-lao-shaping-model).

**Table of Contents**

  - [Thai character table](#thai-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Thai character table ##

Thai glyphs should be classified as in the following
table. Codepoints in the Thai block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column.

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints, such as currency marks,
punctuation, and other symbols.

> Note: the `NUMBER` and `SYMBOL` _Shaping classes_ are important
> during syllable identification, but generally evoke no further
> special behavior during the rest of the shaping process.

The _Mark-placement subclass_ column indicates mark-placement
positioning for codepoints in the _Mark_ category. Assigned, non-mark
codepoints have a _null_ in this column and evoke no special
mark-placement behavior. Marks tagged with [Mn] in the _Unicode
category_ column are categorized as non-spacing; marks tagged with
[Mc] are categorized as spacing-combining.

Some codepoints in the following table use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass | Combining class | PUA    | Glyph                         |
|:----------|:-----------------|:------------------|:------------------------|:----------------|:-------|:------------------------------|
|`U+0E00`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E01`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E01; Ko Kai               |
|`U+0E02`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E02; Kho Khai             |
|`U+0E03`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E03; Kho Khuat            |
|`U+0E04`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E04; Kho Khwai            |
|`U+0E05`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E05; Kho Khon             |
|`U+0E06`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E06; Kho Rakhang          |
|`U+0E07`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E07; Ngo Ngu              |
|`U+0E08`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E08; Cho Chan             |
|`U+0E09`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E09; Cho Ching            |
|`U+0E0A`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E0A; Cho Chang            |
|`U+0E0B`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E0B; So So                |
|`U+0E0C`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E0C; Cho Choe             |
|`U+0E0D`   | Letter           | CONSONANT         | _null_                  | _0_             | RC     | &#x0E0D; Yo Ying              |
|`U+0E0E`   | Letter           | CONSONANT         | _null_                  | _0_             | DC     | &#x0E0E; Do Chada             |
|`U+0E0F`   | Letter           | CONSONANT         | _null_                  | _0_             | DC     | &#x0E0F; To Patak             |
| | | | | | | |   
|`U+0E10`   | Letter           | CONSONANT         | _null_                  | _0_             | RC     | &#x0E10; Tho Than             |
|`U+0E11`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E11; Tho Nangmontho       |
|`U+0E12`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E12; Tho Phuthao          |
|`U+0E13`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E13; No Nen               |
|`U+0E14`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E14; Do Dek               |
|`U+0E15`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E15; To Tao               |
|`U+0E16`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E16; Tho Thung            |
|`U+0E17`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E17; Tho Thahan           |
|`U+0E18`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E18; Tho Thong            |
|`U+0E19`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E19; No Nu                |
|`U+0E1A`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E1A; Bo Baimai            |
|`U+0E1B`   | Letter           | CONSONANT         | _null_                  | _0_             | AC     | &#x0E1B; Po Pla               |
|`U+0E1C`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E1C; Pho Phung            |
|`U+0E1D`   | Letter           | CONSONANT         | _null_                  | _0_             | AC     | &#x0E1D; Fo Fa                |
|`U+0E1E`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E1E; Pho Phan             |
|`U+0E1F`   | Letter           | CONSONANT         | _null_                  | _0_             | AC     | &#X0e1f; Fo Fan               |
| | | | | | | |   
|`U+0E20`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#X0e20; Pho Samphao          |
|`U+0E21`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E21; Mo Ma                |
|`U+0E22`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E22; Yo Yak               |
|`U+0E23`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E23; Ro Rua               |
|`U+0E24`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E24; Ru                   |
|`U+0E25`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E25; Lo Ling              |
|`U+0E26`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E26; Lu                   |
|`U+0E27`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E27; Wo Waen              |
|`U+0E28`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E28; So Sala              |
|`U+0E29`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E29; So Rusi              |
|`U+0E2A`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E2A; So Sua               |
|`U+0E2B`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E2B; Ho Hip               |
|`U+0E2C`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E2C; Lo Chula             |
|`U+0E2D`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E2D; O Ang                |
|`U+0E2E`   | Letter           | CONSONANT         | _null_                  | _0_             | NC     | &#x0E2E; Ho Nokhuk            |
|`U+0E2F`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E2F; Paiyannoi            |
| | | | | | | |
|`U+0E30`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | CV     | &#x0E30; Sara A               |
|`U+0E31`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E31; Mai Han-akat         |
|`U+0E32`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | CV     | &#x0E32; Sara Aa              |
|`U+0E33`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | _null_ | &#x0E33; Sara Am              |
|`U+0E34`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E34; Sara I               |
|`U+0E35`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E35; Sara Ii              |
|`U+0E36`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E36; Sara Ue              |
|`U+0E37`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E37; Sara Uee             |
|`U+0E38`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION         | 3               | BV     | &#x0E38; Sara U               |
|`U+0E39`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION         | 3               | BV     | &#x0E39; Sara Uu              |
|`U+0E3A`   | Mark [Mn]        | PURE_KILLER       | BOTTOM_POSITION         | 9               | BV     | &#x0E3A; Phinthu              |
|`U+0E3B`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E3C`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E3D`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E3E`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E3F`   | Symbol           | SYMBOL            | _null_                  | _0_             | _null_ | &#x0E3F; Currency symbol Baht |
| | | | | | | |
|`U+0E40`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | CV     | &#x0E40; Sara E               |
|`U+0E41`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | CV     | &#x0E41; Sara Ae              |
|`U+0E42`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | CV     | &#x0E42; Sara O               |
|`U+0E43`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | CV     | &#x0E43; Sara Ai Maimuan      |
|`U+0E44`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | CV     | &#x0E44; Sara Ai Maimalai     |
|`U+0E45`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | CV     | &#x0E45; Lakkhangyao          |
|`U+0E46`   | Letter Modifier  | _null_            | _null_                  | _0_             | _null_ | &#x0E46; Maiyamok             |
|`U+0E47`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | AV     | &#x0E47; Maitaikhu            |
|`U+0E48`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 107             | TV     | &#x0E48; Mai Ek               |
|`U+0E49`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 107             | TV     | &#x0E49; Mai Tho              |
|`U+0E4A`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 107             | TV     | &#x0E4A; Mai Tri              |
|`U+0E4B`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 107             | TV     | &#x0E4B; Mai Chattawa         |
|`U+0E4C`   | Mark [Mn]        | CONSONANT_KILLER  | TOP_POSITION            | _0_             | TV     | &#x0E4C; Thanthakhat          |
|`U+0E4D`   | Mark [Mn]        | BINDU             | TOP_POSITION            | _0_             | AV     | &#x0E4D; Nikhahit             |
|`U+0E4E`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION            | _0_             | AV     | &#x0E4E; Yamakkan             |
|`U+0E4F`   | Punctuation      | _null_            | _null_                  | _0_             | _null_ | &#x0E4F; Fongman              |
| | | | | | | |
|`U+0E50`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E50; Digit zero           |
|`U+0E51`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E51; Digit one            |
|`U+0E52`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E52; Digit two            |
|`U+0E53`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E53; Digit three          |
|`U+0E54`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E54; Digit four           |
|`U+0E55`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E55; Digit five           |
|`U+0E56`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E56; Digit six            |
|`U+0E57`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E57; Digit seven          |
|`U+0E58`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E58; Digit eight          |
|`U+0E59`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0E59; Digit nine           |
|`U+0E5A`   | Punctuation      | _null_            | _null_                  | _0_             | _null_ | &#x0E5A; Angkhankhu           |
|`U+0E5B`   | Punctuation      | _null_            | _null_                  | _0_             | _null_ | &#x0E5B; Khomut               |
|`U+0E5C`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E5D`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E5E`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E5F`   | _unassigned_     |                   |                         |                 |        |                               |
| | | | | | | |
|`U+0E60`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E61`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E62`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E63`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E64`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E65`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E66`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E67`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E68`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E69`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6A`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6B`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6C`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6D`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6E`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E6F`   | _unassigned_     |                   |                         |                 |        |                               |
| | | | | | | |
|`U+0E70`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E71`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E72`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E73`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E74`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E75`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E76`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E77`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E78`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E79`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7A`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7B`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7C`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7D`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7E`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E7F`   | _unassigned_     |                   |                         |                 |        |                               |
