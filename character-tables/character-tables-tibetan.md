# Tibetan character tables #

This document lists the per-character shaping information needed to
[shape Tibetan text](opentype-shaping-tibetan.md).

**Table of Contents**

  - [Tibetan character table](#tibetan-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Tibetan character table ##

Tibetan glyphs should be classified as in the following
table. Codepoints in the Tibetan block with no assigned meaning are
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

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                                            |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------------------------|
| `U+0F00`  | Letter           | _null_            | _null_                     | &#x0F00; Syllable Om                             |
| `U+0F01`  | Symbol           | SYMBOL            | _null_                     | &#x0F01; Gter Yig Mgo Truncated A                |
| `U+0F02`  | Symbol           | SYMBOL            | _null_                     | &#x0F02; Gter Yig Mgo -Um Rnam Bcad Ma           |
| `U+0F03`  | Symbol           | SYMBOL            | _null_                     | &#x0F03; Gter Yig Mgo -Um Gter Tsheg Ma          |
| `U+0F04`  | Punctuation      | _null_            | _null_                     | &#x0F04; Initial Yig Mgo Mdun Ma                 |
| `U+0F05`  | Punctuation      | _null_            | _null_                     | &#x0F05; Closing Yig Mgo Sgab Ma                 |
| `U+0F06`  | Punctuation      | _null_            | _null_                     | &#x0F06; Caret Yig Mgo Phur Shad Ma              |
| `U+0F07`  | Punctuation      | _null_            | _null_                     | &#x0F07; Yig Mgo Tsheg Shad Ma                   |
| `U+0F08`  | Punctuation      | _null_            | _null_                     | &#x0F08; Sbrul Shad                              |
| `U+0F09`  | Punctuation      | _null_            | _null_                     | &#x0F09; Bskur Yig Mgo                           |
| `U+0F0A`  | Punctuation      | _null_            | _null_                     | &#x0F0A; Bka- Shog Yig Mgo                       |
| `U+0F0B`  | Punctuation      | _null_            | _null_                     | &#x0F0B; Intersyllabic Tsheg                     |
| `U+0F0C`  | Punctuation      | _null_            | _null_                     | &#x0F0C; Delimiter Tsheg Bstar                   |
| `U+0F0D`  | Punctuation      | _null_            | _null_                     | &#x0F0D; Shad                                    |
| `U+0F0E`  | Punctuation      | _null_            | _null_                     | &#x0F0E; Nyis Shad                               |
| `U+0F0F`  | Punctuation      | _null_            | _null_                     | &#x0F0F; Tsheg Shad                              |
| | | | | |
| `U+0F10`  | Punctuation      | _null_            | _null_                     | &#x0F10; Nyis Tsheg Shad                         |
| `U+0F11`  | Punctuation      | _null_            | _null_                     | &#x0F11; Rin Chen Spungs Shad                    |
| `U+0F12`  | Punctuation      | _null_            | _null_                     | &#x0F12; Rgya Gram Shad                          |
| `U+0F13`  | Symbol           | SYMBOL            | _null_                     | &#x0F13; Caret -Dzud Rtags Me Long Can           |
| `U+0F14`  | Punctuation      | _null_            | _null_                     | &#x0F14; Gter Tsheg                              |
| `U+0F15`  | Symbol           | SYMBOL            | _null_                     | &#x0F15; Logotype Sign Chad Rtags                |
| `U+0F16`  | Symbol           | SYMBOL            | _null_                     | &#x0F16; Logotype Sign Lhag Rtags                |
| `U+0F17`  | Symbol           | SYMBOL            | _null_                     | &#x0F17; Astrological Sign Sgra Gcan -Char Rtags |
| `U+0F18`  | Mark [Mn]        | _null_            | BOTTOM_POSITION            | &#x0F18; Astrological Sign -Khyud Pa             |
| `U+0F19`  | Mark [Mn]        | _null_            | BOTTOM_POSITION            | &#x0F19; Astrological Sign Sdong Tshugs          |
| `U+0F1A`  | Symbol           | SYMBOL            | _null_                     | &#x0F1A; Sign Rdel Dkar Gcig                     |
| `U+0F1B`  | Symbol           | SYMBOL            | _null_                     | &#x0F1B; Sign Rdel Dkar Gnyis                    |
| `U+0F1C`  | Symbol           | SYMBOL            | _null_                     | &#x0F1C; Sign Rdel Dkar Gsum                     |
| `U+0F1D`  | Symbol           | SYMBOL            | _null_                     | &#x0F1D; Sign Rdel Nag Gcig                      |
| `U+0F1E`  | Symbol           | SYMBOL            | _null_                     | &#x0F1E; Sign Rdel Nag Gnyis                     |
| `U+0F1F`  | Symbol           | SYMBOL            | _null_                     | &#x0F1F; Sign Rdel Dkar Rdel Nag                 |
| | | | | |
| `U+0F20`  | Number           | NUMBER            | _null_                     | &#x0F20; Digit Zero                              |
| `U+0F21`  | Number           | NUMBER            | _null_                     | &#x0F21; Digit One                               |
| `U+0F22`  | Number           | NUMBER            | _null_                     | &#x0F22; Digit Two                               |
| `U+0F23`  | Number           | NUMBER            | _null_                     | &#x0F23; Digit Three                             |
| `U+0F24`  | Number           | NUMBER            | _null_                     | &#x0F24; Digit Four                              |
| `U+0F25`  | Number           | NUMBER            | _null_                     | &#x0F25; Digit Five                              |
| `U+0F26`  | Number           | NUMBER            | _null_                     | &#x0F26; Digit Six                               |
| `U+0F27`  | Number           | NUMBER            | _null_                     | &#x0F27; Digit Seven                             |
| `U+0F28`  | Number           | NUMBER            | _null_                     | &#x0F28; Digit Eight                             |
| `U+0F29`  | Number           | NUMBER            | _null_                     | &#x0F29; Digit Nine                              |
| `U+0F2A`  | Number           | NUMBER            | _null_                     | &#x0F2A; Digit Half One                          |
| `U+0F2B`  | Number           | NUMBER            | _null_                     | &#x0F2B; Digit Half Two                          |
| `U+0F2C`  | Number           | NUMBER            | _null_                     | &#x0F2C; Digit Half Three                        |
| `U+0F2D`  | Number           | NUMBER            | _null_                     | &#x0F2D; Digit Half Four                         |
| `U+0F2E`  | Number           | NUMBER            | _null_                     | &#x0F2E; Digit Half Five                         |
| `U+0F2F`  | Number           | NUMBER            | _null_                     | &#x0F2F; Digit Half Six                          |
| | | | | |
| `U+0F30`  | Number           | NUMBER            | _null_                     | &#x0F30; Digit Half Seven                        |
| `U+0F31`  | Number           | NUMBER            | _null_                     | &#x0F31; Digit Half Eight                        |
| `U+0F32`  | Number           | NUMBER            | _null_                     | &#x0F32; Digit Half Nine                         |
| `U+0F33`  | Number           | NUMBER            | _null_                     | &#x0F33; Digit Half Zero                         |
| `U+0F34`  | Symbol           | SYMBOL            | _null_                     | &#x0F34; Bsdus Rtags                             |
| `U+0F35`  | Mark [Mn]        | SYLLABLE_MODIFIER | BOTTOM_POSITION            | &#x0F35; Ngas Bzung Nyi Zla                      |
| `U+0F36`  | Symbol           | SYMBOL            | _null_                     | &#x0F36; Caret -Dzud Rtags Bzhi Mig Can          |
| `U+0F37`  | Mark [Mn]        | SYLLABLE_MODIFIER | BOTTOM_POSITION            | &#x0F37; Ngas Bzung Sgor Rtags                   |
| `U+0F38`  | Symbol           | SYMBOL            | _null_                     | &#x0F38; Che Mgo                                 |
| `U+0F39`  | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x0F39; Tsa -Phru                               |
| `U+0F3A`  | Punctuation [Ps] | _null_            | _null_                     | &#x0F3A; Gug Rtags Gyon                          |
| `U+0F3B`  | Punctuation [Pe] | _null_            | _null_                     | &#x0F3B; Gug Rtags Gyas                          |
| `U+0F3C`  | Punctuation [Ps] | _null_            | _null_                     | &#x0F3C; Ang Khang Gyon                          |
| `U+0F3D`  | Punctuation [Pe] | _null_            | _null_                     | &#x0F3D; Ang Khang Gyas                          |
| `U+0F3E`  | Mark [Mc]        | _null_            | RIGHT_POSITION             | &#x0F3E; Sign Yar Tshes                          |
| `U+0F3F`  | Mark [Mc]        | _null_            | LEFT_POSITION              | &#x0F3F; Sign Mar Tshes                          |
| | | | | |
| `U+0F40`  | Letter           | CONSONANT         | _null_                     | &#x0F40; Ka                                      |
| `U+0F41`  | Letter           | CONSONANT         | _null_                     | &#x0F41; Kha                                     |
| `U+0F42`  | Letter           | CONSONANT         | _null_                     | &#x0F42; Ga                                      |
| `U+0F43`  | Letter           | CONSONANT         | _null_                     | &#x0F43; Gha                                     |
| `U+0F44`  | Letter           | CONSONANT         | _null_                     | &#x0F44; Nga                                     |
| `U+0F45`  | Letter           | CONSONANT         | _null_                     | &#x0F45; Ca                                      |
| `U+0F46`  | Letter           | CONSONANT         | _null_                     | &#x0F46; Cha                                     |
| `U+0F47`  | Letter           | CONSONANT         | _null_                     | &#x0F47; Ja                                      |
| `U+0F48`  | _unassigned_     |                   |                            |                                                  |
| `U+0F49`  | Letter           | CONSONANT         | _null_                     | &#x0F49; Nya                                     |
| `U+0F4A`  | Letter           | CONSONANT         | _null_                     | &#x0F4A; Tta                                     |
| `U+0F4B`  | Letter           | CONSONANT         | _null_                     | &#x0F4B; Ttha                                    |
| `U+0F4C`  | Letter           | CONSONANT         | _null_                     | &#x0F4C; Dda                                     |
| `U+0F4D`  | Letter           | CONSONANT         | _null_                     | &#x0F4D; Ddha                                    |
| `U+0F4E`  | Letter           | CONSONANT         | _null_                     | &#x0F4E; Nna                                     |
| `U+0F4F`  | Letter           | CONSONANT         | _null_                     | &#x0F4F; Ta                                      |
| | | | | |						 
| `U+0F50`  | Letter           | CONSONANT         | _null_                     | &#x0F50; Tha                                     |
| `U+0F51`  | Letter           | CONSONANT         | _null_                     | &#x0F51; Da                                      |
| `U+0F52`  | Letter           | CONSONANT         | _null_                     | &#x0F52; Dha                                     |
| `U+0F53`  | Letter           | CONSONANT         | _null_                     | &#x0F53; Na                                      |
| `U+0F54`  | Letter           | CONSONANT         | _null_                     | &#x0F54; Pa                                      |
| `U+0F55`  | Letter           | CONSONANT         | _null_                     | &#x0F55; Pha                                     |
| `U+0F56`  | Letter           | CONSONANT         | _null_                     | &#x0F56; Ba                                      |
| `U+0F57`  | Letter           | CONSONANT         | _null_                     | &#x0F57; Bha                                     |
| `U+0F58`  | Letter           | CONSONANT         | _null_                     | &#x0F58; Ma                                      |
| `U+0F59`  | Letter           | CONSONANT         | _null_                     | &#x0F59; Tsa                                     |
| `U+0F5A`  | Letter           | CONSONANT         | _null_                     | &#x0F5A; Tsha                                    |
| `U+0F5B`  | Letter           | CONSONANT         | _null_                     | &#x0F5B; Dza                                     |
| `U+0F5C`  | Letter           | CONSONANT         | _null_                     | &#x0F5C; Dzha                                    |
| `U+0F5D`  | Letter           | CONSONANT         | _null_                     | &#x0F5D; Wa                                      |
| `U+0F5E`  | Letter           | CONSONANT         | _null_                     | &#x0F5E; Zha                                     |
| `U+0F5F`  | Letter           | CONSONANT         | _null_                     | &#x0F5F; Za                                      |
| | | | | |						 
| `U+0F60`  | Letter           | CONSONANT         | _null_                     | &#x0F60; -A                                      |
| `U+0F61`  | Letter           | CONSONANT         | _null_                     | &#x0F61; Ya                                      |
| `U+0F62`  | Letter           | CONSONANT         | _null_                     | &#x0F62; Ra                                      |
| `U+0F63`  | Letter           | CONSONANT         | _null_                     | &#x0F63; La                                      |
| `U+0F64`  | Letter           | CONSONANT         | _null_                     | &#x0F64; Sha                                     |
| `U+0F65`  | Letter           | CONSONANT         | _null_                     | &#x0F65; Ssa                                     |
| `U+0F66`  | Letter           | CONSONANT         | _null_                     | &#x0F66; Sa                                      |
| `U+0F67`  | Letter           | CONSONANT         | _null_                     | &#x0F67; Ha                                      |
| `U+0F68`  | Letter           | CONSONANT         | _null_                     | &#x0F68; A                                       |
| `U+0F69`  | Letter           | CONSONANT         | _null_                     | &#x0F69; Kssa                                    |
| `U+0F6A`  | Letter           | CONSONANT         | _null_                     | &#x0F6A; Fixed-Form Ra                           |
| `U+0F6B`  | Letter           | CONSONANT         | _null_                     | &#x0F6B; Kka                                     |
| `U+0F6C`  | Letter           | CONSONANT         | _null_                     | &#x0F6C; Rra                                     |
| `U+0F6D`  | _unassigned_     |                   |                            |                                                  |
| `U+0F6E`  | _unassigned_     |                   |                            |                                                  |
| `U+0F6F`  | _unassigned_     |                   |                            |                                                  |
| | | | | |
| `U+0F70`  | _unassigned_     |                   |                            |                                                  |
| `U+0F71`  | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0F71; Sign Aa                                 |
| `U+0F72`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F72; Sign I                                  |
| `U+0F73`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F73; Sign Ii                                 |
| `U+0F74`  | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0F74; Sign U                                  |
| `U+0F75`  | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0F75; Sign Uu                                 |
| `U+0F76`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F76; Sign Vocalic R                          |
| `U+0F77`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F77; Sign Vocalic Rr                         |
| `U+0F78`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F78; Sign Vocalic L                          |
| `U+0F79`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F79; Sign Vocalic Ll                         |
| `U+0F7A`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F7A; Sign E                                  |
| `U+0F7B`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F7B; Sign Ee                                 |
| `U+0F7C`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F7C; Sign O                                  |
| `U+0F7D`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F7D; Sign Oo                                 |
| `U+0F7E`  | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0F7E; Sign Rjes Su Nga Ro                     |
| `U+0F7F`  | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0F7F; Sign Rnam Bcad                          |
| | | | | |
| `U+0F80`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0F80; Sign Reversed I                         |
| `U+0F81`  | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0F81; Sign Reversed Ii                        |
| `U+0F82`  | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0F82; Sign Nyi Zla Naa Da                     |
| `U+0F83`  | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0F83; Sign Sna Ldan                           |
| `U+0F84`  | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x0F84; Halanta                                 |
| `U+0F85`  | Punctuation      | AVAGRAHA          | _null_                     | &#x0F85; Paluta                                  |
| `U+0F86`  | Mark [Mn]        | _null_            | TOP_POSITION               | &#x0F86; Sign Lci Rtags                          |
| `U+0F87`  | Mark [Mn]        | _null_            | TOP_POSITION               | &#x0F87; Sign Yang Rtags                         |
| `U+0F88`  | Letter           | CONSONANT_HEAD    | _null_                     | &#x0F88; Sign Lce Tsa Can                        |
| `U+0F89`  | Letter           | CONSONANT_HEAD    | _null_                     | &#x0F89; Sign Mchu Can                           |
| `U+0F8A`  | Letter           | CONSONANT_HEAD    | _null_                     | &#x0F8A; Sign Gru Can Rgyings                    |
| `U+0F8B`  | Letter           | CONSONANT_HEAD    | _null_                     | &#x0F8B; Sign Gru Med Rgyings                    |
| `U+0F8C`  | Letter           | CONSONANT_HEAD    | _null_                     | &#x0F8C; Sign Inverted Mchu Can                  |
| `U+0F8D`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F8D; Subjoined Sign Lce Tsa Can              |
| `U+0F8E`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F8E; Subjoined Sign Mchu Can                 |
| `U+0F8F`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F8F; Subjoined Sign Inverted Mchu Can        |
| | | | | |
| `U+0F90`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F90; Subjoined Ka                            |
| `U+0F91`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F91; Subjoined Kha                           |
| `U+0F92`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F92; Subjoined Ga                            |
| `U+0F93`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F93; Subjoined Gha                           |
| `U+0F94`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F94; Subjoined Nga                           |
| `U+0F95`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F95; Subjoined Ca                            |
| `U+0F96`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F96; Subjoined Cha                           |
| `U+0F97`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F97; Subjoined Ja                            |
| `U+0F98`  | _unassigned_     |                   |                            |                                                  |
| `U+0F99`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F99; Subjoined Nya                           |
| `U+0F9A`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9A; Subjoined Tta                           |
| `U+0F9B`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9B; Subjoined Ttha                          |
| `U+0F9C`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9C; Subjoined Dda                           |
| `U+0F9D`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9D; Subjoined Ddha                          |
| `U+0F9E`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9E; Subjoined Nna                           |
| `U+0F9F`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0F9F; Subjoined Ta                            |
| | | | | |						
| `U+0FA0`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA0; Subjoined Tha                           |
| `U+0FA1`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA1; Subjoined Da                            |
| `U+0FA2`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA2; Subjoined Dha                           |
| `U+0FA3`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA3; Subjoined Na                            |
| `U+0FA4`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA4; Subjoined Pa                            |
| `U+0FA5`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA5; Subjoined Pha                           |
| `U+0FA6`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA6; Subjoined Ba                            |
| `U+0FA7`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA7; Subjoined Bha                           |
| `U+0FA8`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA8; Subjoined Ma                            |
| `U+0FA9`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FA9; Subjoined Tsa                           |
| `U+0FAA`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAA; Subjoined Tsha                          |
| `U+0FAB`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAB; Subjoined Dza                           |
| `U+0FAC`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAC; Subjoined Dzha                          |
| `U+0FAD`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAD; Subjoined Wa                            |
| `U+0FAE`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAE; Subjoined Zha                           |
| `U+0FAF`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FAF; Subjoined Za                            |
| | | | | |						
| `U+0FB0`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB0; Subjoined -A                            |
| `U+0FB1`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB1; Subjoined Ya                            |
| `U+0FB2`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB2; Subjoined Ra                            |
| `U+0FB3`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB3; Subjoined La                            |
| `U+0FB4`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB4; Subjoined Sha                           |
| `U+0FB5`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB5; Subjoined Ssa                           |
| `U+0FB6`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB6; Subjoined Sa                            |
| `U+0FB7`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB7; Subjoined Ha                            |
| `U+0FB8`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB8; Subjoined A                             |
| `U+0FB9`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FB9; Subjoined Kssa                          |
| `U+0FBA`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FBA; Subjoined Fixed-Form Wa                 |
| `U+0FBB`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FBB; Subjoined Fixed-Form Ya                 |
| `U+0FBC`  | Mark [Mn]        |CONSONANT_SUBJOINED| BOTTOM_POSITION            | &#x0FBC; Subjoined Fixed-Form Ra                 |
| `U+0FBD`  | _unassigned_     |                   |                            |                                                  |
| `U+0FBE`  | Symbol           | SYMBOL            | _null_                     | &#x0FBE; Ku Ru Kha                               |
| `U+0FBF`  | Symbol           | SYMBOL            | _null_                     | &#x0FBF; Ku Ru Kha Bzhi Mig Can                  |
| | | | | |
| `U+0FC0`  | Symbol           | SYMBOL            | _null_                     | &#x0FC0; Cantillation Sign Heavy Beat            |
| `U+0FC1`  | Symbol           | SYMBOL            | _null_                     | &#x0FC1; Cantillation Sign Light Beat            |
| `U+0FC2`  | Symbol           | SYMBOL            | _null_                     | &#x0FC2; Cantillation Sign Cang Te-U             |
| `U+0FC3`  | Symbol           | SYMBOL            | _null_                     | &#x0FC3; Cantillation Sign Sbub -Chal            |
| `U+0FC4`  | Symbol           | SYMBOL            | _null_                     | &#x0FC4; Symbol Dril Bu                          |
| `U+0FC5`  | Symbol           | SYMBOL            | _null_                     | &#x0FC5; Symbol Rdo Rje                          |
| `U+0FC6`  | Mark [Mn]        | SYLLABLE_MODIFIER | BOTTOM_POSITION            | &#x0FC6; Symbol Padma Gdan                       |
| `U+0FC7`  | Symbol           | SYMBOL            | _null_                     | &#x0FC7; Symbol Rdo Rje Rgya Gram                |
| `U+0FC8`  | Symbol           | SYMBOL            | _null_                     | &#x0FC8; Symbol Phur Pa                          |
| `U+0FC9`  | Symbol           | SYMBOL            | _null_                     | &#x0FC9; Symbol Nor Bu                           |
| `U+0FCA`  | Symbol           | SYMBOL            | _null_                     | &#x0FCA; Symbol Nor Bu Nyis -Khyil               |
| `U+0FCB`  | Symbol           | SYMBOL            | _null_                     | &#x0FCB; Symbol Nor Bu Gsum -Khyil               |
| `U+0FCC`  | Symbol           | SYMBOL            | _null_                     | &#x0FCC; Symbol Nor Bu Bzhi -Khyil               |
| `U+0FCD`  | _unassigned_     |                   |                            |                                                  |
| `U+0FCE`  | Symbol           | SYMBOL            | _null_                     | &#x0FCE; Sign Rdel Nag Rdel Dkar                 |
| `U+0FCF`  | Symbol           | SYMBOL            | _null_                     | &#x0FCF; Sign Rdel Nag Gsum                      |
| | | | | |
| `U+0FD0`  | Punctuation      | _null_            | _null_                     | &#x0FD0; Bska- Shog Gi Mgo Rgyan                 |
| `U+0FD1`  | Punctuation      | _null_            | _null_                     | &#x0FD1; Mnyam Yig Gi Mgo Rgyan                  |
| `U+0FD2`  | Punctuation      | _null_            | _null_                     | &#x0FD2; Nyis Tsheg                              |
| `U+0FD3`  | Punctuation      | _null_            | _null_                     | &#x0FD3; Initial Brda Rnying Yig Mgo Mdun        |
| `U+0FD4`  | Punctuation      | _null_            | _null_                     | &#x0FD4; Closing Brda Rnying Yig Mgo Sgab        |
| `U+0FD5`  | Symbol           | SYMBOL            | _null_                     | &#x0FD5; Right-Facing Svasti Sign                |
| `U+0FD6`  | Symbol           | SYMBOL            | _null_                     | &#x0FD6; Left-Facing Svasti Sign                 |
| `U+0FD7`  | Symbol           | SYMBOL            | _null_                     | &#x0FD7; Right-Facing Svasti Sign With Dots      |
| `U+0FD8`  | Symbol           | SYMBOL            | _null_                     | &#x0FD8; Left-Facing Svasti Sign With Dots       |
| `U+0FD9`  | Punctuation      | _null_            | _null_                     | &#x0FD9; Leading Mchan Rtags                     |
| `U+0FDA`  | Punctuation      | _null_            | _null_                     | &#x0FDA; Trailing Mchan Rtags                    |
| `U+0FDB`  | _unassigned_     |                   |                            |                                                  |
| `U+0FDC`  | _unassigned_     |                   |                            |                                                  |
| `U+0FDD`  | _unassigned_     |                   |                            |                                                  |
| `U+0FDE`  | _unassigned_     |                   |                            |                                                  |
| `U+0FDF`  | _unassigned_     |                   |                            |                                                  |
| | | | | |


## Vedic Extensions character table ##

Sanskrit runs written in the Tibetan script may also include
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
|`U+1CFA`   | _unassigned_     |                   |                            |                              |
|`U+1CFB`   | _unassigned_     |                   |                            |                              |
|`U+1CFC`   | _unassigned_     |                   |                            |                              |
|`U+1CFD`   | _unassigned_     |                   |                            |                              |
|`U+1CFE`   | _unassigned_     |                   |                            |                              |
|`U+1CFF`   | _unassigned_     |                   |                            |                              |



## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Tibetan text include the dotted-circle placeholder (`U+25CC`), the
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
|`U+25CC`   | Symbol           | DOTTED_CIRCLE     | _null_                     | &#x25CC; Dotted circle         |
|`U+2638`   | Symbol           | SYMBOL            | _null_                     | &#x2638; Wheel of Dharma       |


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
