# Tamil character tables #

This document lists the per-character shaping information needed to
[shape Tamil text](../opentype-shaping-tamil.md).

**Table of Contents**

  - [Tamil character table](#tamil-character-table)
  - [Tamil Supplement character table](#tamil-supplement-character-table)
  - [Grantha marks character table](#grantha-marks-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Tamil character table ##

Tamil glyphs should be classified as in the following
table. Codepoints in the Tamil block with no assigned meaning are
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
|`U+0B80`   | _unassigned_     |                   |                            |                              |
|`U+0B81`   | _unassigned_     |                   |                            |                              |
|`U+0B82`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0B82; Anusvara            |
|`U+0B83`   | Letter           | MODIFYING_LETTER  | _null_                     | &#x0B83; Visarga             |
|`U+0B84`   | _unassigned_     |                   |                            |                              |
|`U+0B85`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B85; A                   |
|`U+0B86`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B86; Aa                  |
|`U+0B87`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B87; I                   |
|`U+0B88`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B88; Ii                  |
|`U+0B89`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B89; U                   |
|`U+0B8A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B8A; Uu                  |
|`U+0B8B`   | _unassigned_     |                   |                            |                              |
|`U+0B8C`   | _unassigned_     |                   |                            |                              |
|`U+0B8D`   | _unassigned_     |                   |                            |                              |
|`U+0B8E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B8E; E                   |
|`U+0B8F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B8F; Ee                  |
| | | | |																		
|`U+0B90`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B90; Ai                  |
|`U+0B91`   | _unassigned_     |                   |                            |                              |
|`U+0B92`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B92; O                   |
|`U+0B93`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B93; Oo                  |
|`U+0B94`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0B94; Au                  |
|`U+0B95`   | Letter           | CONSONANT         | _null_                     | &#x0B95; Ka                  |
|`U+0B96`   | _unassigned_     |                   |                            |                              |
|`U+0B97`   | _unassigned_     |                   |                            |                              |
|`U+0B98`   | _unassigned_     |                   |                            |                              |
|`U+0B99`   | Letter           | CONSONANT         | _null_                     | &#x0B99; Nga                 |
|`U+0B9A`   | Letter           | CONSONANT         | _null_                     | &#x0B9A; Ca                  |
|`U+0B9B`   | _unassigned_     |                   |                            |                              |
|`U+0B9C`   | Letter           | CONSONANT         | _null_                     | &#x0B9C; Ja                  |
|`U+0B9D`   | _unassigned_     |                   |                            |                              |
|`U+0B9E`   | Letter           | CONSONANT         | _null_                     | &#x0B9E; Nya                 |
|`U+0B9F`   | Letter           | CONSONANT         | _null_                     | &#x0B9F; Tta                 |
| | | | |																		
|`U+0BA0`   | _unassigned_     |                   |                            |                              |
|`U+0BA1`   | _unassigned_     |                   |                            |                              |
|`U+0BA2`   | _unassigned_     |                   |                            |                              |
|`U+0BA3`   | Letter           | CONSONANT         | _null_                     | &#x0BA3; Nna                 |
|`U+0BA4`   | Letter           | CONSONANT         | _null_                     | &#x0BA4; Ta                  |
|`U+0BA5`   | _unassigned_     |                   |                            |                              |
|`U+0BA6`   | _unassigned_     |                   |                            |                              |
|`U+0BA7`   | _unassigned_     |                   |                            |                              |
|`U+0BA8`   | Letter           | CONSONANT         | _null_                     | &#x0BA8; Na                  |
|`U+0BA9`   | Letter           | CONSONANT         | _null_                     | &#x0BA9; Nnna                |
|`U+0BAA`   | Letter           | CONSONANT         | _null_                     | &#x0BAA; Pa                  |
|`U+0BAB`   | _unassigned_     |                   |                            |                              |
|`U+0BAC`   | _unassigned_     |                   |                            |                              |
|`U+0BAD`   | _unassigned_     |                   |                            |                              |
|`U+0BAE`   | Letter           | CONSONANT         | _null_                     | &#x0BAE; Ma                  |
|`U+0BAF`   | Letter           | CONSONANT         | _null_                     | &#x0BAF; Ya                  |
| | | | |																		
|`U+0BB0`   | Letter           | CONSONANT         | _null_                     | &#x0BB0; Ra                  |
|`U+0BB1`   | Letter           | CONSONANT         | _null_                     | &#x0BB1; Rra                 |
|`U+0BB2`   | Letter           | CONSONANT         | _null_                     | &#x0BB2; La                  |
|`U+0BB3`   | Letter           | CONSONANT         | _null_                     | &#x0BB3; Lla                 |
|`U+0BB4`   | Letter           | CONSONANT         | _null_                     | &#x0BB4; Llla                |
|`U+0BB5`   | Letter           | CONSONANT         | _null_                     | &#x0BB5; Va                  |
|`U+0BB6`   | Letter           | CONSONANT         | _null_                     | &#x0BB6; Sha                 |
|`U+0BB7`   | Letter           | CONSONANT         | _null_                     | &#x0BB7; Ssa                 |
|`U+0BB8`   | Letter           | CONSONANT         | _null_                     | &#x0BB8; Sa                  |
|`U+0BB9`   | Letter           | CONSONANT         | _null_                     | &#x0BB9; Ha                  |
|`U+0BBA`   | _unassigned_     |                   |                            |                              |
|`U+0BBB`   | _unassigned_     |                   |                            |                              |
|`U+0BBC`   | _unassigned_     |                   |                            |                              |
|`U+0BBD`   | _unassigned_     |                   |                            |                              |
|`U+0BBE`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0BBE; Sign Aa             |
|`U+0BBF`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0BBF; Sign I              |
| | | | |																		
|`U+0BC0`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0BC0; Sign Ii             |
|`U+0BC1`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0BC1; Sign U              |
|`U+0BC2`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0BC2; Sign Uu             |
|`U+0BC3`   | _unassigned_     |                   |                            |                              |
|`U+0BC4`   | _unassigned_     |                   |                            |                              |
|`U+0BC5`   | _unassigned_     |                   |                            |                              |
|`U+0BC6`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0BC6; Sign E              |
|`U+0BC7`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0BC7; Sign Ee             |
|`U+0BC8`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0BC8; Sign Ai             |
|`U+0BC9`   | _unassigned_     |                   |                            |                              |
|`U+0BCA`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0BCA; Sign O              |
|`U+0BCB`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0BCB; Sign Oo             |
|`U+0BCC`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x0BCC; Sign Au             |
|`U+0BCD`   | Mark [Mn]        | VIRAMA            | TOP_POSITION               | &#x0BCD; Virama              |
|`U+0BCE`   | _unassigned_     |                   |                            |                              |
|`U+0BCF`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0BD0`   | Letter           | _null_            | _null_                     | &#x0BD0; Om                  |
|`U+0BD1`   | _unassigned_     |                   |                            |                              |
|`U+0BD2`   | _unassigned_     |                   |                            |                              |
|`U+0BD3`   | _unassigned_     |                   |                            |                              |
|`U+0BD4`   | _unassigned_     |                   |                            |                              |
|`U+0BD5`   | _unassigned_     |                   |                            |                              |
|`U+0BD6`   | _unassigned_     |                   |                            |                              |
|`U+0BD7`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0BD7; Au Length Mark      |
|`U+0BD8`   | _unassigned_     |                   |                            |                              |
|`U+0BD9`   | _unassigned_     |                   |                            |                              |
|`U+0BDA`   | _unassigned_     |                   |                            |                              |
|`U+0BDB`   | _unassigned_     |                   |                            |                              |
|`U+0BDC`   | _unassigned_     |                   |                            |                              |
|`U+0BDD`   | _unassigned_     |                   |                            |                              |
|`U+0BDE`   | _unassigned_     |                   |                            |                              |
|`U+0BDF`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0BE0`   | _unassigned_     |                   |                            |                              |
|`U+0BE1`   | _unassigned_     |                   |                            |                              |
|`U+0BE2`   | _unassigned_     |                   |                            |                              |
|`U+0BE3`   | _unassigned_     |                   |                            |                              |
|`U+0BE4`   | _unassigned_     |                   |                            |                              |
|`U+0BE5`   | _unassigned_     |                   |                            |                              |
|`U+0BE6`   | Number           | NUMBER            | _null_                     | &#x0BE6; Digit Zero          |
|`U+0BE7`   | Number           | NUMBER            | _null_                     | &#x0BE7; Digit One           |
|`U+0BE8`   | Number           | NUMBER            | _null_                     | &#x0BE8; Digit Two           |
|`U+0BE9`   | Number           | NUMBER            | _null_                     | &#x0BE9; Digit Three         |
|`U+0BEA`   | Number           | NUMBER            | _null_                     | &#x0BEA; Digit Four          |
|`U+0BEB`   | Number           | NUMBER            | _null_                     | &#x0BEB; Digit Five          |
|`U+0BEC`   | Number           | NUMBER            | _null_                     | &#x0BEC; Digit Six           |
|`U+0BED`   | Number           | NUMBER            | _null_                     | &#x0BED; Digit Seven         |
|`U+0BEE`   | Number           | NUMBER            | _null_                     | &#x0BEE; Digit Eight         |
|`U+0BEF`   | Number           | NUMBER            | _null_                     | &#x0BEF; Digit Nine          |
| | | | |																		
|`U+0BF0`   | Number           | NUMBER            | _null_                     | &#x0BF0; Number Ten          |
|`U+0BF1`   | Number           | NUMBER            | _null_                     | &#x0BF1; Number One Hundred  |
|`U+0BF2`   | Number           | NUMBER            | _null_                     | &#x0BF2; Number One Thousand |
|`U+0BF3`   | Symbol           | SYMBOL            | _null_                     | &#x0BF3; Day Sign            |
|`U+0BF4`   | Symbol           | SYMBOL            | _null_                     | &#x0BF4; Month Sign          |
|`U+0BF5`   | Symbol           | SYMBOL            | _null_                     | &#x0BF5; Year Sign           |
|`U+0BF6`   | Symbol           | SYMBOL            | _null_                     | &#x0BF6; Debit Sign          |
|`U+0BF7`   | Symbol           | SYMBOL            | _null_                     | &#x0BF7; Credit Sign         |
|`U+0BF8`   | Symbol           | SYMBOL            | _null_                     | &#x0BF8; As Above Sign       |
|`U+0BF9`   | Symbol           | SYMBOL            | _null_                     | &#x0BF9; Tamil Rupee Sign    |
|`U+0BFA`   | Symbol           | SYMBOL            | _null_                     | &#x0BFA; Number Sign         |
|`U+0BFB`   | _unassigned_     |                   |                            |                              |
|`U+0BFC`   | _unassigned_     |                   |                            |                              |
|`U+0BFD`   | _unassigned_     |                   |                            |                              |
|`U+0BFE`   | _unassigned_     |                   |                            |                              |
|`U+0BFF`   | _unassigned_     |                   |                            |                              |



## Tamil Supplement character table ##

Tamil text runs may also include historical symbols and fractions from
the Tamil Supplement block. These characters should be classified as
follows.

| Codepoint | Unicode category | Shaping class | Mark-placement subclass | Glyph                         |
|:----------|:-----------------|:--------------|:------------------------|:------------------------------|
| `U+11FC0` | Number           | NUMBER        | _null_                  | &#x11FC0; Fraction One Three-Hundred-And-Twentieth |
| `U+11FC1` | Number           | NUMBER        | _null_                  | &#x11FC1; Fraction One One-Hundred-And-Sixtieth |
| `U+11FC2` | Number           | NUMBER        | _null_                  | &#x11FC2; Fraction One Eightieth |
| `U+11FC3` | Number           | NUMBER        | _null_                  | &#x11FC3; Fraction One Sixty-Fourth |
| `U+11FC4` | Number           | NUMBER        | _null_                  | &#x11FC4; Fraction One Fortieth |
| `U+11FC5` | Number           | NUMBER        | _null_                  | &#x11FC5; Fraction One Thirty-Second |
| `U+11FC6` | Number           | NUMBER        | _null_                  | &#x11FC6; Fraction Three Eightieths |
| `U+11FC7` | Number           | NUMBER        | _null_                  | &#x11FC7; Fraction Three Sixty-Fourths |
| `U+11FC8` | Number           | NUMBER        | _null_                  | &#x11FC8; Fraction One Twentieth |
| `U+11FC9` | Number           | NUMBER        | _null_                  | &#x11FC9; Fraction One Sixteenth-1 |
| `U+11FCA` | Number           | NUMBER        | _null_                  | &#x11FCA; Fraction One Sixteenth-2 |
| `U+11FCB` | Number           | NUMBER        | _null_                  | &#x11FCB; Fraction One Tenth  |
| `U+11FCC` | Number           | NUMBER        | _null_                  | &#x11FCC; Fraction One Eighth |
| `U+11FCD` | Number           | NUMBER        | _null_                  | &#x11FCD; Fraction Three Twentieths |
| `U+11FCE` | Number           | NUMBER        | _null_                  | &#x11FCE; Fraction Three Sixteenths |
| `U+11FCF` | Number           | NUMBER        | _null_                  | &#x11FCF; Fraction One Fifth  |
| | | | |																			           
| `U+11FD0` | Number           | NUMBER        | _null_                  | &#x11FD0; Fraction One Quarter |
| `U+11FD1` | Number           | NUMBER        | _null_                  | &#x11FD1; Fraction One Half-1 |
| `U+11FD2` | Number           | NUMBER        | _null_                  | &#x11FD2; Fraction One Half-2 |
| `U+11FD3` | Number           | NUMBER        | _null_                  | &#x11FD3; Fraction Three Quarters |
| `U+11FD4` | Number           | NUMBER        | _null_                  | &#x11FD4; Fraction Downscaling Factor Kiizh |
| `U+11FD5` | Symbol           | SYMBOL        | _null_                  | &#x11FD5; Sign Nel            |
| `U+11FD6` | Symbol           | SYMBOL        | _null_                  | &#x11FD6; Sign Cevitu         |
| `U+11FD7` | Symbol           | SYMBOL        | _null_                  | &#x11FD7; Sign Aazhaakku      |
| `U+11FD8` | Symbol           | SYMBOL        | _null_                  | &#x11FD8; Sign Uzhakku        |
| `U+11FD9` | Symbol           | SYMBOL        | _null_                  | &#x11FD9; Sign Muuvuzhakku    |
| `U+11FDA` | Symbol           | SYMBOL        | _null_                  | &#x11FDA; Sign Kuruni         |
| `U+11FDB` | Symbol           | SYMBOL        | _null_                  | &#x11FDB; Sign Pathakku       |
| `U+11FDC` | Symbol           | SYMBOL        | _null_                  | &#x11FDC; Sign Mukkuruni      |
| `U+11FDD` | Symbol           | SYMBOL        | _null_                  | &#x11FDD; Sign Kaacu          |
| `U+11FDE` | Symbol           | SYMBOL        | _null_                  | &#x11FDE; Sign Panam          |
| `U+11FDF` | Symbol           | SYMBOL        | _null_                  | &#x11FDF; Sign Pon            |
| | | | |																			      
| `U+11FE0` | Symbol           | SYMBOL        | _null_                  | &#x11FE0; Sign Varaakan       |
| `U+11FE1` | Symbol           | SYMBOL        | _null_                  | &#x11FE1; Sign Paaram         |
| `U+11FE2` | Symbol           | SYMBOL        | _null_                  | &#x11FE2; Sign Kuzhi          |
| `U+11FE3` | Symbol           | SYMBOL        | _null_                  | &#x11FE3; Sign Veli           |
| `U+11FE4` | Symbol           | SYMBOL        | _null_                  | &#x11FE4; Wet Cultivation Sign |
| `U+11FE5` | Symbol           | SYMBOL        | _null_                  | &#x11FE5; Dry Cultivation Sign |
| `U+11FE6` | Symbol           | SYMBOL        | _null_                  | &#x11FE6; Land Sign           |
| `U+11FE7` | Symbol           | SYMBOL        | _null_                  | &#x11FE7; Salt Pan Sign       |
| `U+11FE8` | Symbol           | SYMBOL        | _null_                  | &#x11FE8; Traditional Credit Sign |
| `U+11FE9` | Symbol           | SYMBOL        | _null_                  | &#x11FE9; Traditional Number Sign |
| `U+11FEA` | Symbol           | SYMBOL        | _null_                  | &#x11FEA; Current Sign        |
| `U+11FEB` | Symbol           | SYMBOL        | _null_                  | &#x11FEB; And Odd Sign        |
| `U+11FEC` | Symbol           | SYMBOL        | _null_                  | &#x11FEC; Spent Sign          |
| `U+11FED` | Symbol           | SYMBOL        | _null_                  | &#x11FED; Total Sign          |
| `U+11FEE` | Symbol           | SYMBOL        | _null_                  | &#x11FEE; In Possession Sign  |
| `U+11FEF` | Symbol           | SYMBOL        | _null_                  | &#x11FEF; Starting From Sign  |
| | | | |
| `U+11FF0` | Symbol           | SYMBOL        | _null_                  | &#x11FF0; Sign Muthaliya      |
| `U+11FF1` | Symbol           | SYMBOL        | _null_                  | &#x11FF1; Sign Vakaiyaraa     |
| `U+11FF2` | _unassigned_     |               |                         |                               |
| `U+11FF3` | _unassigned_     |               |                         |                               |
| `U+11FF4` | _unassigned_     |               |                         |                               |
| `U+11FF5` | _unassigned_     |               |                         |                               |
| `U+11FF6` | _unassigned_     |               |                         |                               |
| `U+11FF7` | _unassigned_     |               |                         |                               |
| `U+11FF8` | _unassigned_     |               |                         |                               |
| `U+11FF9` | _unassigned_     |               |                         |                               |
| `U+11FFA` | _unassigned_     |               |                         |                               |
| `U+11FFB` | _unassigned_     |               |                         |                               |
| `U+11FFC` | _unassigned_     |               |                         |                               |
| `U+11FFD` | _unassigned_     |               |                         |                               |
| `U+11FFE` | _unassigned_     |               |                         |                               |
| `U+11FFF` | Punctuation      | _null_        | _null_                  | &#x11FFF; End Of Text         |



## Grantha marks character table ##

Tamil text runs may also include diacritical and syllable-modifier
marks from the Grantha block. These characters should be classified as
follows.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+11301`  | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x11301; Grantha Candrabindu|
|`U+11303`  | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x11303; Grantha Visarga    |
|`U+1133B`  | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x1133b; Combining Bindu Below |
|`U+1133C`  | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x1133c; Grantha Nukta      |


## Vedic Extensions character table ##

Sanskrit runs written in the Tamil script may also include
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

In addition to general punctuation, runs of Tamil text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Tamil text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |



Other important characters that may be encountered when shaping runs
of Tamil text include the dotted-circle placeholder (`U+25CC`), the
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
|`U+00B2`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x00B2; Superscript Two       |
|`U+00B3`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x00B3; Superscript Three     |
|`U+200C`   | Other            | NON_JOINER        | _null_                     | &#x200C; Zero-width non-joiner |
|`U+200D`   | Other            | JOINER            | _null_                     | &#x200D; Zero-width joiner     |
|`U+2010`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2010; Hyphen                |
|`U+2011`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2011; No-break hyphen       |
|`U+2012`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2012; Figure dash           |
|`U+2013`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2013; En dash               |
|`U+2014`   | Punctuation      | PLACEHOLDER       | _null_                     | &#x2014; Em dash               |
|`U+2074`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x2074; Superscript Four      |
|`U+2082`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x2082; Subscript Two       |
|`U+2083`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x2083; Subscript Three     |
|`U+2084`   | Number           | SYLLABLE_MODIFIER | TOP                        | &#x2084; Subscript Four      |
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

Tamil text sometimes uses the Latin numerals 2, 3, and 4 in
superscript or subscript positions to annotate Sanskrit. When used in
this fashion, the superscripts and subscripts are treated as
`SYLLABLE_MODIFIER` signs for shaping purposes.
