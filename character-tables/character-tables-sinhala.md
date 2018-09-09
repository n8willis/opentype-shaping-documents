# Sinhala character tables #

This document lists the per-character shaping information needed to
[shape Sinhala text](../opentype-shaping-sinhala.md).

**Table of Contents**

  - [Sinhala character table](#sinhala-character-table)
  - [Sinhala Archaic Numbers character table](#sinhala-archaic-numbers-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Sinhala character table ##

Sinhala glyphs should be classified as in the following
table. Codepoints in the Sinhala block with no assigned meaning are
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
|`U+0D80`   | _unassigned_     |                   |                            |                              |
|`U+0D81`   | _unassigned_     |                   |                            |                              |
|`U+0D82`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0D82; Anusvara            |
|`U+0D83`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0D83; Visarga             |
|`U+0D84`   | _unassigned_     |                   |                            |                              |
|`U+0D85`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D85; A                   |
|`U+0D86`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D86; Aa                  |
|`U+0D87`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D87; Ae                  |
|`U+0D88`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D88; Aae                 |
|`U+0D89`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D89; I                   |
|`U+0D8A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8A; Ii                  |
|`U+0D8B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8B; U                   |
|`U+0D8C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8C; Uu                  |
|`U+0D8D`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8D; Vocalic R           |
|`U+0D8E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8E; Vocalic Rr          |
|`U+0D8F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D8F; Vocalic L           |
| | | | |																		
|`U+0D90`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D90; Vocalic Ll          |
|`U+0D91`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D91; E                   |
|`U+0D92`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D92; Ee                  |
|`U+0D93`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D93; Ai                  |
|`U+0D94`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D94; O                   |
|`U+0D95`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D95; Oo                  |
|`U+0D96`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0D96; Au                  |
|`U+0D97`   | _unassigned_     |                   |                            |                              |
|`U+0D98`   | _unassigned_     |                   |                            |                              |
|`U+0D99`   | _unassigned_     |                   |                            |                              |
|`U+0D9A`   | Letter           | CONSONANT         | _null_                     | &#x0D9A; Ka                  |
|`U+0D9B`   | Letter           | CONSONANT         | _null_                     | &#x0D9B; Kha                 |
|`U+0D9C`   | Letter           | CONSONANT         | _null_                     | &#x0D9C; Ga                  |
|`U+0D9D`   | Letter           | CONSONANT         | _null_                     | &#x0D9D; Gha                 |
|`U+0D9E`   | Letter           | CONSONANT         | _null_                     | &#x0D9E; Nga                 |
|`U+0D9F`   | Letter           | CONSONANT         | _null_                     | &#x0D9F; Nnga                |
| | | | |																		
|`U+0DA0`   | Letter           | CONSONANT         | _null_                     | &#x0DA0; Ca                  |
|`U+0DA1`   | Letter           | CONSONANT         | _null_                     | &#x0DA1; Cha                 |
|`U+0DA2`   | Letter           | CONSONANT         | _null_                     | &#x0DA2; Ja                  |
|`U+0DA3`   | Letter           | CONSONANT         | _null_                     | &#x0DA3; Jha                 |
|`U+0DA4`   | Letter           | CONSONANT         | _null_                     | &#x0DA4; Nya                 |
|`U+0DA5`   | Letter           | CONSONANT         | _null_                     | &#x0DA5; Jnya                |
|`U+0DA6`   | Letter           | CONSONANT         | _null_                     | &#x0DA6; Nyja                |
|`U+0DA7`   | Letter           | CONSONANT         | _null_                     | &#x0DA7; Tta                 |
|`U+0DA8`   | Letter           | CONSONANT         | _null_                     | &#x0DA8; Ttha                |
|`U+0DA9`   | Letter           | CONSONANT         | _null_                     | &#x0DA9; Dda                 |
|`U+0DAA`   | Letter           | CONSONANT         | _null_                     | &#x0DAA; Ddha                |
|`U+0DAB`   | Letter           | CONSONANT         | _null_                     | &#x0DAB; Nna                 |
|`U+0DAC`   | Letter           | CONSONANT         | _null_                     | &#x0DAC; Nndda               |
|`U+0DAD`   | Letter           | CONSONANT         | _null_                     | &#x0DAD; Ta                  |
|`U+0DAE`   | Letter           | CONSONANT         | _null_                     | &#x0DAE; Tha                 |
|`U+0DAF`   | Letter           | CONSONANT         | _null_                     | &#x0DAF; Da                  |
| | | | |																		
|`U+0DB0`   | Letter           | CONSONANT         | _null_                     | &#x0DB0; Dha                 |
|`U+0DB1`   | Letter           | CONSONANT         | _null_                     | &#x0DB1; Na                  |
|`U+0DB2`   | _unassigned_     |                   |                            |                              |
|`U+0DB3`   | Letter           | CONSONANT         | _null_                     | &#x0DB3; Nda                 |
|`U+0DB4`   | Letter           | CONSONANT         | _null_                     | &#x0DB4; Pa                  |
|`U+0DB5`   | Letter           | CONSONANT         | _null_                     | &#x0DB5; Pha                 |
|`U+0DB6`   | Letter           | CONSONANT         | _null_                     | &#x0DB6; Ba                  |
|`U+0DB7`   | Letter           | CONSONANT         | _null_                     | &#x0DB7; Bha                 |
|`U+0DB8`   | Letter           | CONSONANT         | _null_                     | &#x0DB8; Ma                  |
|`U+0DB9`   | Letter           | CONSONANT         | _null_                     | &#x0DB9; Mba                 |
|`U+0DBA`   | Letter           | CONSONANT         | _null_                     | &#x0DBA; Ya                  |
|`U+0DBB`   | Letter           | CONSONANT         | _null_                     | &#x0DBB; Ra                  |
|`U+0DBC`   | _unassigned_     |                   |                            |                              |
|`U+0DBD`   | Letter           | CONSONANT         | _null_                     | &#x0DBD; La                  |
|`U+0DBE`   | _unassigned_     |                   |                            |                              |
|`U+0DBF`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0DC0`   | Letter           | CONSONANT         | _null_                     | &#x0DC0; Va                  |
|`U+0DC1`   | Letter           | CONSONANT         | _null_                     | &#x0DC1; Sha                 |
|`U+0DC2`   | Letter           | CONSONANT         | _null_                     | &#x0DC2; Ssa                 |
|`U+0DC3`   | Letter           | CONSONANT         | _null_                     | &#x0DC3; Sa                  |
|`U+0DC4`   | Letter           | CONSONANT         | _null_                     | &#x0DC4; Ha                  |
|`U+0DC5`   | Letter           | CONSONANT         | _null_                     | &#x0DC5; Lla                 |
|`U+0DC6`   | Letter           | CONSONANT         | _null_                     | &#x0DC6; Fa                  |
|`U+0DC7`   | _unassigned_     |                   |                            |                              |
|`U+0DC8`   | _unassigned_     |                   |                            |                              |
|`U+0DC9`   | _unassigned_     |                   |                            |                              |
|`U+0DCA`   | Mark [MN]        | VIRAMA            | TOP_POSITION               | &#x0DCA; Virama              |
|`U+0DCB`   | _unassigned_     |                   |                            |                              |
|`U+0DCC`   | _unassigned_     |                   |                            |                              |
|`U+0DCD`   | _unassigned_     |                   |                            |                              |
|`U+0DCE`   | _unassigned_     |                   |                            |                              |
|`U+0DCF`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DCF; Sign Aa             |
| | | | |																	 	
|`U+0DD0`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DD0; Sign Ae             |
|`U+0DD1`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DD1; Sign Aae            |
|`U+0DD2`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0DD2; Sign I              |
|`U+0DD3`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0DD3; Sign Ii             |
|`U+0DD4`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0DD4; Sign U              |
|`U+0DD5`   | _unassigned_     |                   |                            |                              |
|`U+0DD6`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0DD6; Sign Uu             |
|`U+0DD7`   | _unassigned_     |                   |                            |                              |
|`U+0DD8`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DD8; Sign Vocalic R      |
|`U+0DD9`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0DD9; Sign E              |
|`U+0DDA`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_LEFT_POSITION      | &#x0DDA; Sign Ee             |
|`U+0DDB`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0DDB; Sign Ai             |
|`U+0DDC`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0DDC; Sign O              |
|`U+0DDD`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_LEFT_AND_RIGHT_POSITION| &#x0DDD; Sign Oo             |
|`U+0DDE`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0DDE; Sign Au             |
|`U+0DDF`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DDF; Sign Vocalic L      |
| | | | |																		
|`U+0DE0`   | _unassigned_     |                   |                            |                              |
|`U+0DE1`   | _unassigned_     |                   |                            |                              |
|`U+0DE2`   | _unassigned_     |                   |                            |                              |
|`U+0DE3`   | _unassigned_     |                   |                            |                              |
|`U+0DE4`   | _unassigned_     |                   |                            |                              |
|`U+0DE5`   | _unassigned_     |                   |                            |                              |
|`U+0DE6`   | Number           | NUMBER            | _null_                     | &#x0DE6; Digit Zero          |
|`U+0DE7`   | Number           | NUMBER            | _null_                     | &#x0DE7; Digit One           |
|`U+0DE8`   | Number           | NUMBER            | _null_                     | &#x0DE8; Digit Two           |
|`U+0DE9`   | Number           | NUMBER            | _null_                     | &#x0DE9; Digit Three         |
|`U+0DEA`   | Number           | NUMBER            | _null_                     | &#x0DEA; Digit Four          |
|`U+0DEB`   | Number           | NUMBER            | _null_                     | &#x0DEB; Digit Five          |
|`U+0DEC`   | Number           | NUMBER            | _null_                     | &#x0DEC; Digit Six           |
|`U+0DED`   | Number           | NUMBER            | _null_                     | &#x0DED; Digit Seven         |
|`U+0DEE`   | Number           | NUMBER            | _null_                     | &#x0DEE; Digit Eight         |
|`U+0DEF`   | Number           | NUMBER            | _null_                     | &#x0DEF; Digit Nine          |
| | | | |																		
|`U+0DF0`   | _unassigned_     |                   |                            |                              |
|`U+0DF1`   | _unassigned_     |                   |                            |                              |
|`U+0DF2`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DF2; Sign Vocalic Rr     |
|`U+0DF3`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0DF3; Sign Vocalic Ll     |
|`U+0DF4`   | Punctuation      | _null_            | _null_                     | &#x0DF4; Kunddaliya          |
|`U+0DF5`   | _unassigned_     |                   |                            |                              |
|`U+0DF6`   | _unassigned_     |                   |                            |                              |
|`U+0DF7`   | _unassigned_     |                   |                            |                              |
|`U+0DF8`   | _unassigned_     |                   |                            |                              |
|`U+0DF9`   | _unassigned_     |                   |                            |                              |
|`U+0DFA`   | _unassigned_     |                   |                            |                              |
|`U+0DFB`   | _unassigned_     |                   |                            |                              |
|`U+0DFC`   | _unassigned_     |                   |                            |                              |
|`U+0DFD`   | _unassigned_     |                   |                            |                              |
|`U+0DFE`   | _unassigned_     |                   |                            |                              |
|`U+0DFF`   | _unassigned_     |                   |                            |                              |



## Sinhala Archaic Numbers character table ##

Sinhala text runs may also include glyphs from the Sinhala Archaic
Numbers block. These characters should be classified as follows.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+111E0`  | _unassigned_     |                   |                            |                              |
|`U+111E1`  | Number           | NUMBER            | _null_                     | &#x111E1; Archaic Digit One  |
|`U+111E2`  | Number           | NUMBER            | _null_                     | &#x111E2; Archaic Digit Two  |
|`U+111E3`  | Number           | NUMBER            | _null_                     | &#x111E3; Archaic Digit Three|
|`U+111E4`  | Number           | NUMBER            | _null_                     | &#x111E4; Archaic Digit Four |
|`U+111E5`  | Number           | NUMBER            | _null_                     | &#x111E5; Archaic Digit Five |
|`U+111E6`  | Number           | NUMBER            | _null_                     | &#x111E6; Archaic Digit Six  |
|`U+111E7`  | Number           | NUMBER            | _null_                     | &#x111E7; Archaic Digit Seven|
|`U+111E8`  | Number           | NUMBER            | _null_                     | &#x111E8; Archaic Digit Eight|
|`U+111E9`  | Number           | NUMBER            | _null_                     | &#x111E9; Archaic Digit Nine |
|`U+111EA`  | Number           | NUMBER            | _null_                     | &#x111EA; Archaic Number Ten |
|`U+111EB`  | Number           | NUMBER            | _null_                     | &#x111EB; Archaic Number 20  |
|`U+111EC`  | Number           | NUMBER            | _null_                     | &#x111EC; Archaic Number 30  |
|`U+111ED`  | Number           | NUMBER            | _null_                     | &#x111ED; Archaic Number 40  |
|`U+111EE`  | Number           | NUMBER            | _null_                     | &#x111EE; Archaic Number 50  |
|`U+111EF`  | Number           | NUMBER            | _null_                     | &#x111EF; Archaic Number 60  |
| | | | |																		
|`U+111F0`  | Number           | NUMBER            | _null_                     | &#x111F0; Archaic Number 70  |
|`U+111F1`  | Number           | NUMBER            | _null_                     | &#x111F1; Archaic Number 80  |
|`U+111F2`  | Number           | NUMBER            | _null_                     | &#x111F2; Archaic Number 90  |
|`U+111F3`  | Number           | NUMBER            | _null_                     | &#x111F3; Archaic Number 100 |
|`U+111F4`  | Number           | NUMBER            | _null_                     | &#x111F4; Archaic Number 1000|
|`U+111F5`  | _unassigned_     |                   |                            |                              |
|`U+111F6`  | _unassigned_     |                   |                            |                              |
|`U+111F7`  | _unassigned_     |                   |                            |                              |
|`U+111F8`  | _unassigned_     |                   |                            |                              |
|`U+111F9`  | _unassigned_     |                   |                            |                              |
|`U+111FA`  | _unassigned_     |                   |                            |                              |
|`U+111FB`  | _unassigned_     |                   |                            |                              |
|`U+111FC`  | _unassigned_     |                   |                            |                              |
|`U+111FD`  | _unassigned_     |                   |                            |                              |
|`U+111FE`  | _unassigned_     |                   |                            |                              |
|`U+111FF`  | _unassigned_     |                   |                            |                              |


## Vedic Extensions character table ##

Sanskrit runs written in the Sinhala script may also include
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
|`U+1CE9`   | Letter           | SYMBOL            | _null_                     | &#x1CE9; Sign Anusvara Antargomukha |
|`U+1CEA`   | Letter           | _null_            | _null_                     | &#x1CEA; Sign Anusvara Bahirgomukha |
|`U+1CEB`   | Letter           | _null_            | _null_                     | &#x1CEB; Sign Anusvara Vamagomukha |
|`U+1CEC`   | Letter           | SYMBOL            | _null_                     | &#x1CEC; Sign Anusvara Vamagomukha With Tail |
|`U+1CED`   | Mark [Mn]        | AVAGRAHA          | BOTTOM_POSITION            | &#x1CED; Sign Tiryak         |
|`U+1CEE`   | Letter           | SYMBOL            | _null_                     | &#x1CEE; Sign Hexiform Long Anusvara |
|`U+1CEF`   | Letter           | _null_            | _null_                     | &#x1CEF; Sign Long Anusvara  |
| | | | |																		
|`U+1CF0`   | Letter           | _null_            | _null_                     | &#x1CF0; Sign Rthang Long Anusvara |
|`U+1CF1`   | Letter           | SYMBOL            | _null_                     | &#x1CF1; Sign Anusvara Ubhayato Mukha |
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



## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Sinhala text include the dotted-circle placeholder (`U+25CC`), the
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

