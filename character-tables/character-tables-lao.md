# Lao character tables #

This document lists the per-character shaping information needed to
[shape Lao text](../opentype-shaping-thai-lao.md#the-thailao-shaping-model).

**Contents**

  - [Lao character table](#lao-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Lao character table ##

Lao glyphs should be classified as in the following
table. Codepoints in the Lao block with no assigned meaning are
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
|`U+0E80`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E81`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E81; Ko                   |
|`U+0E82`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E82; Kho Sung             |
|`U+0E83`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E84`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E84; Kho Tam              |
|`U+0E85`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E86`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E86; Pali Gha             |
|`U+0E87`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E87; Ngo                  |
|`U+0E88`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E88; Co                   |
|`U+0E89`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E89; Pali Cha             |
|`U+0E8A`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E8A; So Tam               |
|`U+0E8B`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0E8C`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E8C; Pali Jha             |
|`U+0E8D`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E8D; Nyo                  |
|`U+0E8E`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E8E; Pali Nya             |
|`U+0E8F`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E8F; Pali Tta             |
| | | | | | | |
|`U+0E90`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E90; Pali Ttha            |
|`U+0E91`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E91; Pali Dda             |
|`U+0E92`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E92; Pali Ddha            |
|`U+0E93`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E93; Pali Nna             |
|`U+0E94`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E94; Do                   |
|`U+0E95`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E95; To                   |
|`U+0E96`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E96; Tho Sung             |
|`U+0E97`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E97; Tho Tam              |
|`U+0E98`   | Letter           | CONSONANT         |  _null_                 | _0_             | _null_ | &#x0E98; Pali Dha             |
|`U+0E99`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E99; No                   |
|`U+0E9A`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9A; Bo                   |
|`U+0E9B`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9B; Po                   |
|`U+0E9C`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9C; Pho Sung             |
|`U+0E9D`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9D; Fo Tam               |
|`U+0E9E`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9E; Pho Tam              |
|`U+0E9F`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0E9F; Fo Sung              |
| | | | | | | |																      
|`U+0EA0`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA0; Pali Bha             |
|`U+0EA1`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA1; Mo                   |
|`U+0EA2`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA2; Yo                   |
|`U+0EA3`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA3; Lo Ling              |
|`U+0EA4`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EA5`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA5; Lo Loot              |
|`U+0EA6`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EA7`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA7; Wo                   |
|`U+0EA8`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA8; Sanskrit Sha         |
|`U+0EA9`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EA9; Sanskrit Ssa         |
|`U+0EAA`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EAA; So Sung              |
|`U+0EAB`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EAB; Ho Sung              |
|`U+0EAC`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EAC; Pali Lla             |
|`U+0EAD`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EAD; O                    |
|`U+0EAE`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EAE; Ho Tam               |
|`U+0EAF`   | Letter           | _null_            | _null_                  | _0_             | _null_ | &#x0EAF; Ellipsis             |
| | | | | | | |																      
|`U+0EB0`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | _null_ | &#x0EB0; Sign A               |
|`U+0EB1`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EB1; Sign Mai Kan         |
|`U+0EB2`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | _null_ | &#x0EB2; Sign Aa              |
|`U+0EB3`   | Letter           | VOWEL_DEPENDENT   | RIGHT_POSITION          | _0_             | _null_ | &#x0EB3; Sign Am              |
|`U+0EB4`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EB4; Sign I               |
|`U+0EB5`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EB5; Sign Ii              |
|`U+0EB6`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EB6; Sign Y               |
|`U+0EB7`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EB7; Sign Yy              |
|`U+0EB8`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION         | 118             | _null_ | &#x0EB8; Sign U               |
|`U+0EB9`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION         | 118             | _null_ | &#x0EB9; Sign Uu              |
|`U+0EBA`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION         | 9               | _null_ | &#x0EBA; Pali Virama          |
|`U+0EBB`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION            | _0_             | _null_ | &#x0EBB; Sign Mai Kon         |
|`U+0EBC`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION         | _0_             | _null_ | &#x0EBC; Semivowel Sign Lo    |
|`U+0EBD`   | Letter           | CONSONANT_MEDIAL  | _null_                  | _0_             | _null_ | &#x0EBD; Semivowel Sign Nyo   |
|`U+0EBE`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EBF`   | _unassigned_     |                   |                         |                 |        |                               |
| | | | | | | |
|`U+0EC0`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | _null_ | &#x0EC0; Sign E               |
|`U+0EC1`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | _null_ | &#x0EC1; Sign Ei              |
|`U+0EC2`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | _null_ | &#x0EC2; Sign O               |
|`U+0EC3`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | _null_ | &#x0EC3; Sign Ay              |
|`U+0EC4`   | Letter           | VOWEL_DEPENDENT   | VISUAL_ORDER_LEFT       | _0_             | _null_ | &#x0EC4; Sign Ai              |
|`U+0EC5`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EC6`   | Letter Modifier  | _null_            | _null_                  | _0_             | _null_ | &#x0EC6; Ko La                |
|`U+0EC7`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EC8`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 122             | _null_ | &#x0EC8; Tone Mai Ek          |
|`U+0EC9`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 122             | _null_ | &#x0EC9; Tone Mai Tho         |
|`U+0ECA`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 122             | _null_ | &#x0ECA; Tone Mai Ti          |
|`U+0ECB`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | 122             | _null_ | &#x0ECB; Tone Mai Catawa      |
|`U+0ECC`   | Mark [Mn]        | _null_            | TOP_POSITION            | _0_             | _null_ | &#x0ECC; Cancellation mark    |
|`U+0ECD`   | Mark [Mn]        | BINDU             | TOP_POSITION            | _0_             | _null_ | &#x0ECD; Niggahita            |
|`U+0ECE`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION            | _0_             | _null_ | &#x0ECE; Yamakkan             |
|`U+0ECF`   | _unassigned_     |                   |                         |                 |        |                               |
| | | | | | | |        														                    
|`U+0ED0`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED0; Digit Zero           |
|`U+0ED1`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED1; Digit One            |
|`U+0ED2`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED2; Digit Two            |
|`U+0ED3`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED3; Digit Three          |
|`U+0ED4`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED4; Digit Four           |
|`U+0ED5`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED5; Digit Five           |
|`U+0ED6`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED6; Digit Six            |
|`U+0ED7`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED7; Digit Seven          |
|`U+0ED8`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED8; Digit Eight          |
|`U+0ED9`   | Number           | NUMBER            | _null_                  | _0_             | _null_ | &#x0ED9; Digit Nine           |
|`U+0EDA`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EDB`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EDC`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EDC; Ho No                |
|`U+0EDD`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EDD; Ho Mo                |
|`U+0EDE`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EDE; Khmu Go              |
|`U+0EDF`   | Letter           | CONSONANT         | _null_                  | _0_             | _null_ | &#x0EDF; Khmu Nyo             |
| | | | | | | |
|`U+0EE0`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE1`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE2`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE3`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE4`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE5`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE6`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE7`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE8`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EE9`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EEA`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EEB`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EEC`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EED`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EEE`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EEF`   | _unassigned_     |                   |                         |                 |        |                               |
| | | | | | | |
|`U+0EF0`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF1`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF2`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF3`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF4`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF5`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF6`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF7`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF8`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EF9`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFA`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFB`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFC`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFD`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFE`   | _unassigned_     |                   |                         |                 |        |                               |
|`U+0EFF`   | _unassigned_     |                   |                         |                 |        |                               |



## Miscellaneous character table ##

In addition to general punctuation, runs of Lao text text typically do not
insert spaces between words. Consequently, the Zero-Width Space (`U+200B`)
character is often used to insert invisible break points that may be
converted to line breaks.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+200B`   | Separator        | PLACEHOLDER       | _null_                     | &#x200B; Zero-width space      |


Other important characters that may be encountered when shaping runs
of Lao text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
dependent vowel or a combining mark in isolation. Real-world
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
