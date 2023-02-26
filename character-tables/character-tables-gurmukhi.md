# Gurmukhi character tables #

This document lists the per-character shaping information needed to
[shape Gurmukhi text](../opentype-shaping-gurmukhi.md).

**Table of Contents**

  - [Gurmukhi character table](#gurmukhi-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Gurmukhi character table ##

Gurmukhi glyphs should be classified as in the following
table. Codepoints in the Gurmukhi block with no assigned meaning are
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
|`U+0A00`   | _unassigned_     |                   |                            |                              |
|`U+0A01`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0A01; Adak Bindi          |
|`U+0A02`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0A02; Bindi               |
|`U+0A03`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0A03; Visarga             |
|`U+0A04`   | _unassigned_     |                   |                            |                              |
|`U+0A05`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A05; A                   |
|`U+0A06`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A06; Aa                  |
|`U+0A07`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A07; I                   |
|`U+0A08`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A08; Ii                  |
|`U+0A09`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A09; U                   |
|`U+0A0A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A0A; Uu                  |
|`U+0A0B`   | _unassigned_     |                   |                            |                              |
|`U+0A0C`   | _unassigned_     |                   |                            |                              |
|`U+0A0D`   | _unassigned_     |                   |                            |                              |
|`U+0A0E`   | _unassigned_     |                   |                            |                              |
|`U+0A0F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A0F; Ee                  |
| | | | |
|`U+0A10`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A10; Ai                  |
|`U+0A11`   | _unassigned_     |                   |                            |                              |
|`U+0A12`   | _unassigned_     |                   |                            |                              |
|`U+0A13`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A13; Oo                  |
|`U+0A14`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A14; Au                  |
|`U+0A15`   | Letter           | CONSONANT         | _null_                     | &#x0A15; Ka                  |
|`U+0A16`   | Letter           | CONSONANT         | _null_                     | &#x0A16; Kha                 |
|`U+0A17`   | Letter           | CONSONANT         | _null_                     | &#x0A17; Ga                  |
|`U+0A18`   | Letter           | CONSONANT         | _null_                     | &#x0A18; Gha                 |
|`U+0A19`   | Letter           | CONSONANT         | _null_                     | &#x0A19; Nga                 |
|`U+0A1A`   | Letter           | CONSONANT         | _null_                     | &#x0A1A; Ca                  |
|`U+0A1B`   | Letter           | CONSONANT         | _null_                     | &#x0A1B; Cha                 |
|`U+0A1C`   | Letter           | CONSONANT         | _null_                     | &#x0A1C; Ja                  |
|`U+0A1D`   | Letter           | CONSONANT         | _null_                     | &#x0A1D; Jha                 |
|`U+0A1E`   | Letter           | CONSONANT         | _null_                     | &#x0A1E; Nya                 |
|`U+0A1F`   | Letter           | CONSONANT         | _null_                     | &#x0A1F; Tta                 |
| | | | |
|`U+0A20`   | Letter           | CONSONANT         | _null_                     | &#x0A20; Ttha                |
|`U+0A21`   | Letter           | CONSONANT         | _null_                     | &#x0A21; Dda                 |
|`U+0A22`   | Letter           | CONSONANT         | _null_                     | &#x0A22; Ddha                |
|`U+0A23`   | Letter           | CONSONANT         | _null_                     | &#x0A23; Nna                 |
|`U+0A24`   | Letter           | CONSONANT         | _null_                     | &#x0A24; Ta                  |
|`U+0A25`   | Letter           | CONSONANT         | _null_                     | &#x0A25; Tha                 |
|`U+0A26`   | Letter           | CONSONANT         | _null_                     | &#x0A26; Da                  |
|`U+0A27`   | Letter           | CONSONANT         | _null_                     | &#x0A27; Dha                 |
|`U+0A28`   | Letter           | CONSONANT         | _null_                     | &#x0A28; Na                  |
|`U+0A29`   | _unassigned_     |                   |                            |                              |
|`U+0A2A`   | Letter           | CONSONANT         | _null_                     | &#x0A2A; Pa                  |
|`U+0A2B`   | Letter           | CONSONANT         | _null_                     | &#x0A2B; Pha                 |
|`U+0A2C`   | Letter           | CONSONANT         | _null_                     | &#x0A2C; Ba                  |
|`U+0A2D`   | Letter           | CONSONANT         | _null_                     | &#x0A2D; Bha                 |
|`U+0A2E`   | Letter           | CONSONANT         | _null_                     | &#x0A2E; Ma                  |
|`U+0A2F`   | Letter           | CONSONANT         | _null_                     | &#x0A2F; Ya                  |
| | | | |
|`U+0A30`   | Letter           | CONSONANT         | _null_                     | &#x0A30; Ra                  |
|`U+0A31`   | _unassigned_     |                   |                            |                              |
|`U+0A32`   | Letter           | CONSONANT         | _null_                     | &#x0A32; La                  |
|`U+0A33`   | Letter           | CONSONANT         | _null_                     | &#x0A33; Lla                 |
|`U+0A34`   | _unassigned_     |                   |                            |                              |
|`U+0A35`   | Letter           | CONSONANT         | _null_                     | &#x0A35; Va                  |
|`U+0A36`   | Letter           | CONSONANT         | _null_                     | &#x0A36; Sha                 |
|`U+0A37`   | _unassigned_     |                   |                            |                              |
|`U+0A38`   | Letter           | CONSONANT         | _null_                     | &#x0A38; Sa                  |
|`U+0A39`   | Letter           | CONSONANT         | _null_                     | &#x0A39; Ha                  |
|`U+0A3A`   | _unassigned_     |                   |                            |                              |
|`U+0A3B`   | _unassigned_     |                   |                            |                              |
|`U+0A3C`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x0A3C; Nukta               |
|`U+0A3D`   | _unassigned_     |                   |                            |                              |
|`U+0A3E`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0A3E; Sign Aa             |
|`U+0A3F`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0A3F; Sign I              |
| | | | |
|`U+0A40`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0A40; Sign Ii             |
|`U+0A41`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0A41; Sign U              |
|`U+0A42`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0A42; Sign Uu             |
|`U+0A43`   | _unassigned_     |                   |                            |                              |
|`U+0A44`   | _unassigned_     |                   |                            |                              |
|`U+0A45`   | _unassigned_     |                   |                            |                              |
|`U+0A46`   | _unassigned_     |                   |                            |                              |
|`U+0A47`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0A47; Sign Ee             |
|`U+0A48`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0A48; Sign Ai             |
|`U+0A49`   | _unassigned_     |                   |                            |                              |
|`U+0A4A`   | _unassigned_     |                   |                            |                              |
|`U+0A4B`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0A4B; Sign Oo             |
|`U+0A4C`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0A4C; Sign Au             |
|`U+0A4D`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x0A4D; Virama              |
|`U+0A4E`   | _unassigned_     |                   |                            |                              |
|`U+0A4F`   | _unassigned_     |                   |                            |                              |
| | | | |
|`U+0A50`   | _unassigned_     |                   |                            |                              |
|`U+0A51`   | Mark [Mn]        | CANTILLATION      | _null_                     | &#x0A51; Udaat               |
|`U+0A52`   | _unassigned_     |                   |                            |                              |
|`U+0A53`   | _unassigned_     |                   |                            |                              |
|`U+0A54`   | _unassigned_     |                   |                            |                              |
|`U+0A55`   | _unassigned_     |                   |                            |                              |
|`U+0A56`   | _unassigned_     |                   |                            |                              |
|`U+0A57`   | _unassigned_     |                   |                            |                              |
|`U+0A58`   | _unassigned_     |                   |                            |                              |
|`U+0A59`   | Letter           | CONSONANT         | _null_                     | &#x0A59; Khha                |
|`U+0A5A`   | Letter           | CONSONANT         | _null_                     | &#x0A5A; Ghha                |
|`U+0A5B`   | Letter           | CONSONANT         | _null_                     | &#x0A5B; Za                  |
|`U+0A5C`   | Letter           | CONSONANT         | _null_                     | &#x0A5C; Rra                 |
|`U+0A5D`   | _unassigned_     |                   |                            |                              |
|`U+0A5E`   | Letter           | CONSONANT         | _null_                     | &#x0A5E; Fa                  |
|`U+0A5F`   | _unassigned_     |                   |                            |                              |
| | | | |
|`U+0A60`   | _unassigned_     |                   |                            |                              |
|`U+0A61`   | _unassigned_     |                   |                            |                              |
|`U+0A62`   | _unassigned_     |                   |                            |                              |
|`U+0A63`   | _unassigned_     |                   |                            |                              |
|`U+0A64`   | _unassigned_     |                   |                            |                              |
|`U+0A65`   | _unassigned_     |                   |                            |                              |
|`U+0A66`   | Number           | NUMBER            | _null_                     | &#x0A66; Digit Zero          |
|`U+0A67`   | Number           | NUMBER            | _null_                     | &#x0A67; Digit One           |
|`U+0A68`   | Number           | NUMBER            | _null_                     | &#x0A68; Digit Two           |
|`U+0A69`   | Number           | NUMBER            | _null_                     | &#x0A69; Digit Three         |
|`U+0A6A`   | Number           | NUMBER            | _null_                     | &#x0A6A; Digit Four          |
|`U+0A6B`   | Number           | NUMBER            | _null_                     | &#x0A6B; Digit Five          |
|`U+0A6C`   | Number           | NUMBER            | _null_                     | &#x0A6C; Digit Six           |
|`U+0A6D`   | Number           | NUMBER            | _null_                     | &#x0A6D; Digit Seven         |
|`U+0A6E`   | Number           | NUMBER            | _null_                     | &#x0A6E; Digit Eight         |
|`U+0A6F`   | Number           | NUMBER            | _null_                     | &#x0A6F; Digit Nine          |
| | | | |
|`U+0A70`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0A70; Tippi               |
|`U+0A71`   | Mark [Mn]        | GEMINATION_MARK   | TOP_POSITION               | &#x0A71; Addak               |
|`U+0A72`   | Letter           | CONSONANT         | _null_                     | &#x0A72; Iri                 |
|`U+0A73`   | Letter           | CONSONANT         | _null_                     | &#x0A73; Ura                 |
|`U+0A74`   | Letter           | _null_            | _null_                     | &#x0A74; Ek Onkar            |
|`U+0A75`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x0A75; Yakash              |
|`U+0A76`   | Punctuation      | _null_            | _null_                     | &#x0A76; Abbreviation Sign   |
|`U+0A77`   | _unassigned_     |                   |                            |                              |
|`U+0A78`   | _unassigned_     |                   |                            |                              |
|`U+0A79`   | _unassigned_     |                   |                            |                              |
|`U+0A7A`   | _unassigned_     |                   |                            |                              |
|`U+0A7B`   | _unassigned_     |                   |                            |                              |
|`U+0A7C`   | _unassigned_     |                   |                            |                              |
|`U+0A7D`   | _unassigned_     |                   |                            |                              |
|`U+0A7E`   | _unassigned_     |                   |                            |                              |
|`U+0A7F`   | _unassigned_     |                   |                            |                              |



## Vedic Extensions character table ##

Sanskrit runs written in the Gurmukhi script may also include
characters from the Vedic Extensions block. These characters should be
classified as follows.

> Note: See the [Vedic Extensions](../opentype-shaping-vedic-extensions.md) 
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
|`U+1CE9`   | Letter           | SYMBOL            | _null_                     | &#x1CE9; Sign Anusvara Antargomukha |
|`U+1CEA`   | Letter           | _null_            | _null_                     | &#x1CEA; Sign Anusvara Bahirgomukha |
|`U+1CEB`   | Letter           | _null_            | _null_                     | &#x1CEB; Sign Anusvara Vamagomukha |
|`U+1CEC`   | Letter           | SYMBOL            | _null_                     | &#x1CEC; Sign Anusvara Vamagomukha With Tail |
|`U+1CED`   | Mark [Mn]        | AVAGRAHA          | BOTTOM_POSITION            | &#x1CED; Sign Tiryak         |
|`U+1CEE`   | Letter           | SYMBOL            | _null_                     | &#x1CEE; Sign Hexiform Long Anusvara |
|`U+1CEF`   | Letter           | _null_            | _null_                     | &#x1CEF; Sign Long Anusvara  |
| | | | |																		
|`U+1CF0`   | Letter           | _null_            | _null_                     | &#x1CF0; Sign Rthang Long Anusvara |
|`U+1CF2`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x1CF2; Sign Ardhavisarga   |
|`U+1CF3`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x1CF3; Sign Rotated Ardhavisarga |
|`U+1CF3`   | Mark [Mc]        | VISARGA           | _null_                     | &#x1CF3; Sign Rotated Ardhavisarga |
|`U+1CF4`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x1CF4; Tone Candra Above   |
|`U+1CF5`   | Letter           | CONSONANT_WITH_STACKER | _null_                | &#x1CF5; Sign Jihvamuliya    |
|`U+1CF6`   | Letter           | CONSONANT_WITH_STACKER | _null_                | &#x1CF6; Sign Upadhmaniya    |
|`U+1CF7`   | Mark [Mc]        | _null_            | _null_                     | &#x1CF7; Sign Atikrama       |
|`U+1CF8`   | Mark [Mn]        | CANTILLATION      | _null_                     | &#x1CF8; Tone Ring Above     |
|`U+1CF9`   | Mark [Mn]        | CANTILLATION      | _null_                     | &#x1CF9; Tone Double Ring Above |
|`U+1CFA`   | Letter           | PLACEHOLDER       | _null_                     | &#x1CFA; Sign Double Anusvara Antargomukha |
|`U+1CFB`   | _unassigned_     |                   |                            |                              |
|`U+1CFC`   | _unassigned_     |                   |                            |                              |
|`U+1CFD`   | _unassigned_     |                   |                            |                              |
|`U+1CFE`   | _unassigned_     |                   |                            |                              |
|`U+1CFF`   | _unassigned_     |                   |                            |                              |



## Miscellaneous character table ##

In addition to general punctuation, runs of Gurmukhi text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Gurmukhi text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |



Other important characters that may be encountered when shaping runs
of Gurmukhi text include the dotted-circle placeholder (`U+25CC`), the
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


The zero-width joiner (<abbr>ZWJ</abbr>) is primarily used to prevent the formation
of a conjunct from a "_Consonant_,Halant,_Consonant_" sequence. The
sequence "_Consonant_,Halant,ZWJ,_Consonant_" blocks the formation of
a conjunct between the two consonants. 

Note, however, that the "_Consonant_,Halant" subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner (<abbr>ZWNJ</abbr>) must be used instead. The
sequence "_Consonant_,Halant,ZWNJ,_Consonant_" should produce the
first consonant in its standard form, followed by an explicit
"Halant".

A secondary usage of the zero-width joiner is to prevent the formation of
"Reph". An initial "Ra,Halant,ZWJ" sequence should not produce a "Reph",
where an initial "Ra,Halant" sequence without the zero-width joiner
otherwise would.

The no-break space (<abbr>NBSP</abbr>) is primarily used to display those
codepoints that are defined as non-spacing (marks, dependent vowels
(matras), below-base consonant forms, and post-base consonant forms)
in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match "NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".

