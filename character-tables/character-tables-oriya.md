# Oriya character tables #

This document lists the per-character shaping information needed to
[shape Oriya text](../opentype-shaping-oriya.md).

**Table of Contents**

  - [Oriya character table](#oriya-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Oriya character table ##

Oriya glyphs should be classified as in the following
table. Codepoints in the Oriya block with no assigned meaning are
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

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+0B00`   | _unassigned_     |                   |                            |                              |
|`U+0B01`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0B01; Candrabindu         |
|`U+0B02`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0B02; Anusvara            |
|`U+0B03`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0B03; Visarga             |
|`U+0B04`   | _unassigned_     |                   |                            |                              |
|`U+0B05`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B05; A                   |
|`U+0B06`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B06; Aa                  |
|`U+0B07`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B07; I                   |
|`U+0B08`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B08; Ii                  |
|`U+0B09`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B09; U                   |
|`U+0B0A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B0A; Uu                  |
|`U+0B0B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B0B; Vocalic R           |
|`U+0B0C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B0C; Vocalic L           |
|`U+0B0D`   | _unassigned_     |                   |                            |                              |
|`U+0B0E`   | _unassigned_     |                   |                            |                              |
|`U+0B0F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B0F; E                   |
| | | | |
|`U+0B10`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B10; Ai                  |
|`U+0B11`   | _unassigned_     |                   |                            |                              |
|`U+0B12`   | _unassigned_     |                   |                            |                              |
|`U+0B13`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B13; O                   |
|`U+0B14`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B14; Au                  |
|`U+0B15`   | Letter           | CONSONANT         | _null_                     | &#x0B15; Ka                  |
|`U+0B16`   | Letter           | CONSONANT         | _null_                     | &#x0B16; Kha                 |
|`U+0B17`   | Letter           | CONSONANT         | _null_                     | &#x0B17; Ga                  |
|`U+0B18`   | Letter           | CONSONANT         | _null_                     | &#x0B18; Gha                 |
|`U+0B19`   | Letter           | CONSONANT         | _null_                     | &#x0B19; Nga                 |
|`U+0B1A`   | Letter           | CONSONANT         | _null_                     | &#x0B1A; Ca                  |
|`U+0B1B`   | Letter           | CONSONANT         | _null_                     | &#x0B1B; Cha                 |
|`U+0B1C`   | Letter           | CONSONANT         | _null_                     | &#x0B1C; Ja                  |
|`U+0B1D`   | Letter           | CONSONANT         | _null_                     | &#x0B1D; Jha                 |
|`U+0B1E`   | Letter           | CONSONANT         | _null_                     | &#x0B1E; Nya                 |
|`U+0B1F`   | Letter           | CONSONANT         | _null_                     | &#x0B1F; Tta                 |
| | | | |
|`U+0B20`   | Letter           | CONSONANT         | _null_                     | &#x0B20; Ttha                |
|`U+0B21`   | Letter           | CONSONANT         | _null_                     | &#x0B21; Dda                 |
|`U+0B22`   | Letter           | CONSONANT         | _null_                     | &#x0B22; Ddha                |
|`U+0B23`   | Letter           | CONSONANT         | _null_                     | &#x0B23; Nna                 |
|`U+0B24`   | Letter           | CONSONANT         | _null_                     | &#x0B24; Ta                  |
|`U+0B25`   | Letter           | CONSONANT         | _null_                     | &#x0B25; Tha                 |
|`U+0B26`   | Letter           | CONSONANT         | _null_                     | &#x0B26; Da                  |
|`U+0B27`   | Letter           | CONSONANT         | _null_                     | &#x0B27; Dha                 |
|`U+0B28`   | Letter           | CONSONANT         | _null_                     | &#x0B28; Na                  |
|`U+0B29`   | _unassigned_     |                   |                            |                              |
|`U+0B2A`   | Letter           | CONSONANT         | _null_                     | &#x0B2A; Pa                  |
|`U+0B2B`   | Letter           | CONSONANT         | _null_                     | &#x0B2B; Pha                 |
|`U+0B2C`   | Letter           | CONSONANT         | _null_                     | &#x0B2C; Ba                  |
|`U+0B2D`   | Letter           | CONSONANT         | _null_                     | &#x0B2D; Bha                 |
|`U+0B2E`   | Letter           | CONSONANT         | _null_                     | &#x0B2E; Ma                  |
|`U+0B2F`   | Letter           | CONSONANT         | _null_                     | &#x0B2F; Ya                  |
| | | | |
|`U+0B30`   | Letter           | CONSONANT         | _null_                     | &#x0B30; Ra                  |
|`U+0B31`   | _unassigned_     |                   |                            |                              |
|`U+0B32`   | Letter           | CONSONANT         | _null_                     | &#x0B32; La                  |
|`U+0B33`   | Letter           | CONSONANT         | _null_                     | &#x0B33; Lla                 |
|`U+0B34`   | _unassigned_     |                   |                            |                              |
|`U+0B35`   | Letter           | CONSONANT         | _null_                     | &#x0B35; Va                  |
|`U+0B36`   | Letter           | CONSONANT         | _null_                     | &#x0B36; Sha                 |
|`U+0B37`   | Letter           | CONSONANT         | _null_                     | &#x0B37; Ssa                 |
|`U+0B38`   | Letter           | CONSONANT         | _null_                     | &#x0B38; Sa                  |
|`U+0B39`   | Letter           | CONSONANT         | _null_                     | &#x0B39; Ha                  |
|`U+0B3A`   | _unassigned_     |                   |                            |                              |
|`U+0B3B`   | _unassigned_     |                   |                            |                              |
|`U+0B3C`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x0B3C; Nukta               |
|`U+0B3D`   | Letter           | AVAGRAHA          | _null_                     | &#x0B3D; Avagraha            |
|`U+0B3E`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0B3E; Sign Aa             |
|`U+0B3F`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0B3F; Sign I              |
| | | | |
|`U+0B40`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0B40; Sign Ii             |
|`U+0B41`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B41; Sign U              |
|`U+0B42`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B42; Sign Uu             |
|`U+0B43`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B43; Sign Vocalic R      |
|`U+0B44`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B44; Sign Vocalic Rr     |
|`U+0B45`   | _unassigned_     |                   |                            |                              |
|`U+0B46`   | _unassigned_     |                   |                            |                              |
|`U+0B47`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0B47; Sign E              |
|`U+0B48`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_LEFT_POSITION      | &#x0B48; Sign Ai             |
|`U+0B49`   | _unassigned_     |                   |                            |                              |
|`U+0B4A`   | _unassigned_     |                   |                            |                              |
|`U+0B4B`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0B4B; Sign O              |
|`U+0B4C`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_LEFT_AND_RIGHT_POSITION| &#x0B4C; Sign Au             |
|`U+0B4D`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x0B4D; Virama              |
|`U+0B4E`   | _unassigned_     |                   |                            |                              |
|`U+0B4F`   | _unassigned_     |                   |                            |                              |
| | | | |
|`U+0B50`   | _unassigned_     |                   |                            |                              |
|`U+0B51`   | _unassigned_     |                   |                            |                              |
|`U+0B52`   | _unassigned_     |                   |                            |                              |
|`U+0B53`   | _unassigned_     |                   |                            |                              |
|`U+0B54`   | _unassigned_     |                   |                            |                              |
|`U+0B55`   | _unassigned_     |                   |                            |                              |
|`U+0B56`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0B56; Ai Length Mark      |
|`U+0B57`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0B57; Au Length Mark      |
|`U+0B58`   | _unassigned_     |                   |                            |                              |
|`U+0B59`   | _unassigned_     |                   |                            |                              |
|`U+0B5A`   | _unassigned_     |                   |                            |                              |
|`U+0B5B`   | _unassigned_     |                   |                            |                              |
|`U+0B5C`   | Letter           | CONSONANT         | _null_                     | &#x0B5C; Rra                 |
|`U+0B5D`   | Letter           | CONSONANT         | _null_                     | &#x0B5D; Rha                 |
|`U+0B5E`   | _unassigned_     |                   |                            |                              |
|`U+0B5F`   | Letter           | CONSONANT         | _null_                     | &#x0B5F; Yya                 |
| | | | |
|`U+0B60`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B60; Vocalic Rr          |
|`U+0B61`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B61; Vocalic Ll          |
|`U+0B62`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B62; Sign Vocalic L      |
|`U+0B63`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0B63; Sign Vocalic Ll     |
|`U+0B64`   | _unassigned_     |                   |                            |                              |
|`U+0B65`   | _unassigned_     |                   |                            |                              |
|`U+0B66`   | Number           | NUMBER            | _null_                     | &#x0B66; Digit Zero          |
|`U+0B67`   | Number           | NUMBER            | _null_                     | &#x0B67; Digit One           |
|`U+0B68`   | Number           | NUMBER            | _null_                     | &#x0B68; Digit Two           |
|`U+0B69`   | Number           | NUMBER            | _null_                     | &#x0B69; Digit Three         |
|`U+0B6A`   | Number           | NUMBER            | _null_                     | &#x0B6A; Digit Four          |
|`U+0B6B`   | Number           | NUMBER            | _null_                     | &#x0B6B; Digit Five          |
|`U+0B6C`   | Number           | NUMBER            | _null_                     | &#x0B6C; Digit Six           |
|`U+0B6D`   | Number           | NUMBER            | _null_                     | &#x0B6D; Digit Seven         |
|`U+0B6E`   | Number           | NUMBER            | _null_                     | &#x0B6E; Digit Eight         |
|`U+0B6F`   | Number           | NUMBER            | _null_                     | &#x0B6F; Digit Nine          |
| | | | |
|`U+0B70`   | Symbol           | SYMBOL            | _null_                     | &#x0B70; Isshar              |
|`U+0B71`   | Letter           | CONSONANT         | _null_                     | &#x0B71; Wa                  |
|`U+0B72`   | Number           | NUMBER            | _null_                     | &#x0B72; Fraction 1/4        |
|`U+0B73`   | Number           | NUMBER            | _null_                     | &#x0B73; Fraction 1/2        |
|`U+0B74`   | Number           | NUMBER            | _null_                     | &#x0B74; Fraction 3/4        |
|`U+0B75`   | Number           | NUMBER            | _null_                     | &#x0B75; Fraction 1/16       |
|`U+0B76`   | Number           | NUMBER            | _null_                     | &#x0B76; Fraction 1/8        |
|`U+0B77`   | Number           | NUMBER            | _null_                     | &#x0B77; Fraction 3/16       |
|`U+0B78`   | _unassigned_     |                   |                            |                              |
|`U+0B79`   | _unassigned_     |                   |                            |                              |
|`U+0B7A`   | _unassigned_     |                   |                            |                              |
|`U+0B7B`   | _unassigned_     |                   |                            |                              |
|`U+0B7C`   | _unassigned_     |                   |                            |                              |
|`U+0B7D`   | _unassigned_     |                   |                            |                              |
|`U+0B7E`   | _unassigned_     |                   |                            |                              |
|`U+0B7F`   | _unassigned_     |                   |                            |                              |



## Vedic Extensions character table ##

Sanskrit runs written in the Oriya script may also include
characters from the Vedic Extensions block. These characters should be
classified as follows.

> Note: See the [Vedic Extensions](opentype-shaping-vedic-extensions.md) 
> document for additional information.

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
|`U+1CFA`   
|`U+1CFB`   | _unassigned_     |                   |                            |                              |
|`U+1CFC`   | _unassigned_     |                   |                            |                              |
|`U+1CFD`   | _unassigned_     |                   |                            |                              |
|`U+1CFE`   | _unassigned_     |                   |                            |                              |
|`U+1CFF`   | _unassigned_     |                   |                            |                              |



## Miscellaneous character table ##

In addition to general punctuation, runs of Oriya text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Oriya text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |



Other important characters that may be encountered when shaping runs
of Oriya text include the dotted-circle placeholder (`U+25CC`), the
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

