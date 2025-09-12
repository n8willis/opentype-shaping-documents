# Malayalam character tables #

This document lists the per-character shaping information needed to
[shape Malayalam text](../opentype-shaping-malayalam.md).

**Contents**

  - [Malayalam character table](#malayalam-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Malayalam character table ##

Malayalam glyphs should be classified as in the following
table. Codepoints in the Malayalam block with no assigned meaning are
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
|`U+0D00`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0D00; Combining Anusvara Above |
|`U+0D01`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0D01; Candrabindu         |
|`U+0D02`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0D02; Anusvara            |
|`U+0D03`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0D03; Visarga             |
|`U+0D04`   | Letter           | BINDU             | _null_                     | &#x0D04; Vedic Anusvara      |
|`U+0D05`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D05; A                   |
|`U+0D06`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D06; Aa                  |
|`U+0D07`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D07; I                   |
|`U+0D08`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D08; Ii                  |
|`U+0D09`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D09; U                   |
|`U+0D0A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D0A; Uu                  |
|`U+0D0B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D0B; Vocalic R           |
|`U+0D0C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D0C; Vocalic L           |
|`U+0D0D`   | _unassigned_     |                   |                            |                              |
|`U+0D0E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D0E; E                   |
|`U+0D0F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D0F; Ee                  |
| | | | |																		
|`U+0D10`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D10; Ai                  |
|`U+0D11`   | _unassigned_     |                   |                            |                              |
|`U+0D12`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D12; O                   |
|`U+0D13`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D13; Oo                  |
|`U+0D14`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D14; Au                  |
|`U+0D15`   | Letter           | CONSONANT         | _null_                     | &#x0D15; Ka                  |
|`U+0D16`   | Letter           | CONSONANT         | _null_                     | &#x0D16; Kha                 |
|`U+0D17`   | Letter           | CONSONANT         | _null_                     | &#x0D17; Ga                  |
|`U+0D18`   | Letter           | CONSONANT         | _null_                     | &#x0D18; Gha                 |
|`U+0D19`   | Letter           | CONSONANT         | _null_                     | &#x0D19; Nga                 |
|`U+0D1A`   | Letter           | CONSONANT         | _null_                     | &#x0D1A; Ca                  |
|`U+0D1B`   | Letter           | CONSONANT         | _null_                     | &#x0D1B; Cha                 |
|`U+0D1C`   | Letter           | CONSONANT         | _null_                     | &#x0D1C; Ja                  |
|`U+0D1D`   | Letter           | CONSONANT         | _null_                     | &#x0D1D; Jha                 |
|`U+0D1E`   | Letter           | CONSONANT         | _null_                     | &#x0D1E; Nya                 |
|`U+0D1F`   | Letter           | CONSONANT         | _null_                     | &#x0D1F; Tta                 |
| | | | |																		
|`U+0D20`   | Letter           | CONSONANT         | _null_                     | &#x0D20; Ttha                |
|`U+0D21`   | Letter           | CONSONANT         | _null_                     | &#x0D21; Dda                 |
|`U+0D22`   | Letter           | CONSONANT         | _null_                     | &#x0D22; Ddha                |
|`U+0D23`   | Letter           | CONSONANT         | _null_                     | &#x0D23; Nna                 |
|`U+0D24`   | Letter           | CONSONANT         | _null_                     | &#x0D24; Ta                  |
|`U+0D25`   | Letter           | CONSONANT         | _null_                     | &#x0D25; Tha                 |
|`U+0D26`   | Letter           | CONSONANT         | _null_                     | &#x0D26; Da                  |
|`U+0D27`   | Letter           | CONSONANT         | _null_                     | &#x0D27; Dha                 |
|`U+0D28`   | Letter           | CONSONANT         | _null_                     | &#x0D28; Na                  |
|`U+0D29`   | Letter           | CONSONANT         | _null_                     | &#x0D29; Nnna                |
|`U+0D2A`   | Letter           | CONSONANT         | _null_                     | &#x0D2A; Pa                  |
|`U+0D2B`   | Letter           | CONSONANT         | _null_                     | &#x0D2B; Pha                 |
|`U+0D2C`   | Letter           | CONSONANT         | _null_                     | &#x0D2C; Ba                  |
|`U+0D2D`   | Letter           | CONSONANT         | _null_                     | &#x0D2D; Bha                 |
|`U+0D2E`   | Letter           | CONSONANT         | _null_                     | &#x0D2E; Ma                  |
|`U+0D2F`   | Letter           | CONSONANT         | _null_                     | &#x0D2F; Ya                  |
| | | | |																		
|`U+0D30`   | Letter           | CONSONANT         | _null_                     | &#x0D30; Ra                  |
|`U+0D31`   | Letter           | CONSONANT         | _null_                     | &#x0D31; Rra                 |
|`U+0D32`   | Letter           | CONSONANT         | _null_                     | &#x0D32; La                  |
|`U+0D33`   | Letter           | CONSONANT         | _null_                     | &#x0D33; Lla                 |
|`U+0D34`   | Letter           | CONSONANT         | _null_                     | &#x0D34; Llla                |
|`U+0D35`   | Letter           | CONSONANT         | _null_                     | &#x0D35; Va                  |
|`U+0D36`   | Letter           | CONSONANT         | _null_                     | &#x0D36; Sha                 |
|`U+0D37`   | Letter           | CONSONANT         | _null_                     | &#x0D37; Ssa                 |
|`U+0D38`   | Letter           | CONSONANT         | _null_                     | &#x0D38; Sa                  |
|`U+0D39`   | Letter           | CONSONANT         | _null_                     | &#x0D39; Ha                  |
|`U+0D3A`   | Letter           | CONSONANT         | _null_                     | &#x0D3A; Ttta                |
|`U+0D3B`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION               | &#x0D3B; Vertical Bar Virama |
|`U+0D3C`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION               | &#x0D3C; Circular Virama     |
|`U+0D3D`   | Letter           | AVAGRAHA          | _null_                     | &#x0D3D; Avagraha            |
|`U+0D3E`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D3E; Sign Aa             |
|`U+0D3F`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D3F; Sign I              |
| | | | |																		
|`U+0D40`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D40; Sign Ii             |
|`U+0D41`   | Mark [Mn]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D41; Sign U              |
|`U+0D42`   | Mark [Mn]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D42; Sign Uu             |
|`U+0D43`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0D43; Sign Vocalic R      |
|`U+0D44`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0D44; Sign Vocalic Rr     |
|`U+0D45`   | _unassigned_     |                   |                            |                              |
|`U+0D46`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0D46; Sign E              |
|`U+0D47`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0D47; Sign Ee             |
|`U+0D48`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0D48; Sign Ai             |
|`U+0D49`   | _unassigned_     |                   |                            |                              |
|`U+0D4A`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0D4A; Sign O              |
|`U+0D4B`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0D4B; Sign Oo             |
|`U+0D4C`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0D4C; Sign Au             |
|`U+0D4D`   | Mark [Mn]        | VIRAMA            | TOP_POSITION               | &#x0D4D; Virama              |
|`U+0D4E`   | Letter           | CONSONANT_PRE_REPHA| _null_                    | &#x0D4E; Dot Reph            |
|`U+0D4F`   | Symbol           | SYMBOL            | _null_                     | &#x0D4F; Para                |
| | | | |																		
|`U+0D50`   | _unassigned_     |                   |                            |                              |
|`U+0D51`   | _unassigned_     |                   |                            |                              |
|`U+0D52`   | _unassigned_     |                   |                            |                              |
|`U+0D53`   | _unassigned_     |                   |                            |                              |
|`U+0D54`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D54; Chillu M            |
|`U+0D55`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D55; Chillu Y            |
|`U+0D56`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D56; Chillu Lll          |
|`U+0D57`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0D57; Au Length Mark      |
|`U+0D58`   | Number           | NUMBER            | _null_                     | &#x0D58; Fraction 1/160      |
|`U+0D59`   | Number           | NUMBER            | _null_                     | &#x0D59; Fraction 1/40       |
|`U+0D5A`   | Number           | NUMBER            | _null_                     | &#x0D5A; Fraction 3/80       |
|`U+0D5B`   | Number           | NUMBER            | _null_                     | &#x0D5B; Fraction 1/20       |
|`U+0D5C`   | Number           | NUMBER            | _null_                     | &#x0D5C; Fraction 1/10       |
|`U+0D5D`   | Number           | NUMBER            | _null_                     | &#x0D5D; Fraction 3/20       |
|`U+0D5E`   | Number           | NUMBER            | _null_                     | &#x0D5E; Fraction 1/5        |
|`U+0D5F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D5F; Archaic Ii          |
| | | | |																		
|`U+0D60`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D60; Vocalic Rr          |
|`U+0D61`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D61; Vocalic Ll          |
|`U+0D62`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0D62; Sign Vocalic L      |
|`U+0D63`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0D63; Sign Vocalic Ll     |
|`U+0D64`   | _unassigned_     |                   |                            |                              |
|`U+0D65`   | _unassigned_     |                   |                            |                              |
|`U+0D66`   | Number           | NUMBER            | _null_                     | &#x0D66; Digit Zero          |
|`U+0D67`   | Number           | NUMBER            | _null_                     | &#x0D67; Digit One           |
|`U+0D68`   | Number           | NUMBER            | _null_                     | &#x0D68; Digit Two           |
|`U+0D69`   | Number           | NUMBER            | _null_                     | &#x0D69; Digit Three         |
|`U+0D6A`   | Number           | NUMBER            | _null_                     | &#x0D6A; Digit Four          |
|`U+0D6B`   | Number           | NUMBER            | _null_                     | &#x0D6B; Digit Five          |
|`U+0D6C`   | Number           | NUMBER            | _null_                     | &#x0D6C; Digit Six           |
|`U+0D6D`   | Number           | NUMBER            | _null_                     | &#x0D6D; Digit Seven         |
|`U+0D6E`   | Number           | NUMBER            | _null_                     | &#x0D6E; Digit Eight         |
|`U+0D6F`   | Number           | NUMBER            | _null_                     | &#x0D6F; Digit Nine          |
| | | | |																		
|`U+0D70`   | Number           | NUMBER            |                            | &#x0D70; Number Ten          |
|`U+0D71`   | Number           | NUMBER            |                            | &#x0D71; Number One Hundred  |
|`U+0D72`   | Number           | NUMBER            |                            | &#x0D72; Number One Thousand |
|`U+0D73`   | Number           | NUMBER            |                            | &#x0D73; Fraction 1/4        |
|`U+0D74`   | Number           | NUMBER            |                            | &#x0D74; Fraction 1/2        |
|`U+0D75`   | Number           | NUMBER            |                            | &#x0D75; Fraction 3/4        |
|`U+0D76`   | Number           | NUMBER            |                            | &#x0D76; Fraction 1/16       |
|`U+0D77`   | Number           | NUMBER            |                            | &#x0D77; Fraction 1/8        |
|`U+0D78`   | Number           | NUMBER            | _null_                     | &#x0D78; Fraction 3/16       |
|`U+0D79`   | Symbol           | SYMBOL            | _null_                     | &#x0D79; Date Mark           |
|`U+0D7A`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7A; Chillu Nn           |
|`U+0D7B`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7B; Chillu N            |
|`U+0D7C`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7C; Chillu Rr           |
|`U+0D7D`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7D; Chillu L            |
|`U+0D7E`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7E; Chillu Ll           |
|`U+0D7F`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x0D7F; Chillu K            |



## Vedic Extensions character table ##

Sanskrit runs written in the Malayalam script may also include
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

In addition to general punctuation, runs of Malayalam text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Malayalam text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |



Other important characters that may be encountered when shaping runs
of Malayalam text include the dotted-circle placeholder (`U+25CC`), the
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

The no-break space (<abbr>NBSP</abbr>) is primarily used to display
those codepoints that are defined as non-spacing (marks, dependent
vowels (matras), below-base consonant forms, and post-base consonant
forms) in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match "NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".

