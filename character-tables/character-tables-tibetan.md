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
this does include some valid codepoints in the Tibetan block, such as
currency marks and other symbols. 

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
| `U+0F00`  |                  |                   |                            | &#x0F00; Syllable Om                          |
| `U+0F01`  |                  |                   |                            | &#X0F01; Mark Gter Yig Mgo Truncated A        |
| `U+0F02`  |                  |                   |                            | &#X0F02; Mark Gter Yig Mgo -Um Rnam Bcad Ma   |
| `U+0F03`  |                  |                   |                            | &#X0F03; Mark Gter Yig Mgo -Um Gter Tsheg Ma  |
| `U+0F04`  |                  |                   |                            | &#X0F04; Mark Initial Yig Mgo Mdun Ma         |
| `U+0F05`  |                  |                   |                            | &#X0F05; Mark Closing Yig Mgo Sgab Ma         |
| `U+0F06`  |                  |                   |                            | &#X0F06; Mark Caret Yig Mgo Phur Shad Ma      |
| `U+0F07`  |                  |                   |                            | &#X0F07; Mark Yig Mgo Tsheg Shad Ma           |
| `U+0F08`  |                  |                   |                            | &#X0F08; Mark Sbrul Shad                      |
| `U+0F09`  |                  |                   |                            | &#X0F09; Mark Bskur Yig Mgo                   |
| `U+0F0A`  |                  |                   |                            | &#X0F0A; Mark Bka- Shog Yig Mgo               |
| `U+0F0B`  |                  |                   |                            | &#X0F0B; Mark Intersyllabic Tsheg             |
| `U+0F0C`  |                  |                   |                            | &#X0F0C; Mark Delimiter Tsheg Bstar           |
| `U+0F0D`  |                  |                   |                            | &#X0F0D; Mark Shad                            |
| `U+0F0E`  |                  |                   |                            | &#X0F0E; Mark Nyis Shad                       |
| `U+0F0F`  |                  |                   |                            | &#X0F0F; Mark Tsheg Shad                      |
| | | | | |																				   
| `U+0F10`  |                  |                   |                            | &#X0F10; Mark Nyis Tsheg Shad                    |
| `U+0F11`  |                  |                   |                            | &#X0F11; Mark Rin Chen Spungs Shad               |
| `U+0F12`  |                  |                   |                            | &#X0F12; Mark Rgya Gram Shad                     |
| `U+0F13`  |                  |                   |                            | &#X0F13; Mark Caret -Dzud Rtags Me Long Can      |
| `U+0F14`  |                  |                   |                            | &#X0F14; Mark Gter Tsheg                         |
| `U+0F15`  |                  |                   |                            | &#X0F15; Logotype Sign Chad Rtags                |
| `U+0F16`  |                  |                   |                            | &#X0F16; Logotype Sign Lhag Rtags                |
| `U+0F17`  |                  |                   |                            | &#X0F17; Astrological Sign Sgra Gcan -Char Rtags |
| `U+0F18`  |                  |                   |                            | &#X0F18; Astrological Sign -Khyud Pa             |
| `U+0F19`  |                  |                   |                            | &#X0F19; Astrological Sign Sdong Tshugs          |
| `U+0F1A`  |                  |                   |                            | &#X0F1A; Sign Rdel Dkar Gcig                     |
| `U+0F1B`  |                  |                   |                            | &#X0F1B; Sign Rdel Dkar Gnyis                    |
| `U+0F1C`  |                  |                   |                            | &#X0F1C; Sign Rdel Dkar Gsum                     |
| `U+0F1D`  |                  |                   |                            | &#X0F1D; Sign Rdel Nag Gcig                      |
| `U+0F1E`  |                  |                   |                            | &#X0F1E; Sign Rdel Nag Gnyis                     |
| `U+0F1F`  |                  |                   |                            | &#X0F1F; Sign Rdel Dkar Rdel Nag                 |
| | | | | |
| `U+0F20`  |                  |                   |                            | &#X0F20; Digit Zero                          |
| `U+0F21`  |                  |                   |                            | &#X0F21; Digit One                           |
| `U+0F22`  |                  |                   |                            | &#X0F22; Digit Two                           |
| `U+0F23`  |                  |                   |                            | &#X0F23; Digit Three                         |
| `U+0F24`  |                  |                   |                            | &#X0F24; Digit Four                          |
| `U+0F25`  |                  |                   |                            | &#X0F25; Digit Five                          |
| `U+0F26`  |                  |                   |                            | &#X0F26; Digit Six                           |
| `U+0F27`  |                  |                   |                            | &#X0F27; Digit Seven                         |
| `U+0F28`  |                  |                   |                            | &#X0F28; Digit Eight                         |
| `U+0F29`  |                  |                   |                            | &#X0F29; Digit Nine                          |
| `U+0F2A`  |                  |                   |                            | &#X0F2A; Digit Half One                      |
| `U+0F2B`  |                  |                   |                            | &#X0F2B; Digit Half Two                      |
| `U+0F2C`  |                  |                   |                            | &#X0F2C; Digit Half Three                    |
| `U+0F2D`  |                  |                   |                            | &#X0F2D; Digit Half Four                     |
| `U+0F2E`  |                  |                   |                            | &#X0F2E; Digit Half Five                     |
| `U+0F2F`  |                  |                   |                            | &#X0F2F; Digit Half Six                      |
| | | | | |
| `U+0F30`  |                  |                   |                            | &#X0F30; Digit Half Seven                    |
| `U+0F31`  |                  |                   |                            | &#X0F31; Digit Half Eight                    |
| `U+0F32`  |                  |                   |                            | &#X0F32; Digit Half Nine                     |
| `U+0F33`  |                  |                   |                            | &#X0F33; Digit Half Zero                     |
| `U+0F34`  |                  |                   |                            | &#X0F34; Mark Bsdus Rtags                    |
| `U+0F35`  |                  |                   |                            | &#X0F35; Mark Ngas Bzung Nyi Zla             |
| `U+0F36`  |                  |                   |                            | &#X0F36; Mark Caret -Dzud Rtags Bzhi Mig Can |
| `U+0F37`  |                  |                   |                            | &#X0F37; Mark Ngas Bzung Sgor Rtags          |
| `U+0F38`  |                  |                   |                            | &#X0F38; Mark Che Mgo                        |
| `U+0F39`  |                  |                   |                            | &#X0F39; Mark Tsa -Phru                      |
| `U+0F3A`  |                  |                   |                            | &#X0F3A; Mark Gug Rtags Gyon                 |
| `U+0F3B`  |                  |                   |                            | &#X0F3B; Mark Gug Rtags Gyas                 |
| `U+0F3C`  |                  |                   |                            | &#X0F3C; Mark Ang Khang Gyon                 |
| `U+0F3D`  |                  |                   |                            | &#X0F3D; Mark Ang Khang Gyas                 |
| `U+0F3E`  |                  |                   |                            | &#X0F3E; Sign Yar Tshes                      |
| `U+0F3F`  |                  |                   |                            | &#X0F3F; Sign Mar Tshes                      |
| | | | | |
| `U+0F40`  |                  |                   |                            | &#X0F40; Ka                      |
| `U+0F41`  |                  |                   |                            | &#X0F41; Kha                     |
| `U+0F42`  |                  |                   |                            | &#X0F42; Ga                      |
| `U+0F43`  |                  |                   |                            | &#X0F43; Gha                     |
| `U+0F44`  |                  |                   |                            | &#X0F44; Nga                     |
| `U+0F45`  |                  |                   |                            | &#X0F45; Ca                      |
| `U+0F46`  |                  |                   |                            | &#X0F46; Cha                     |
| `U+0F47`  |                  |                   |                            | &#x0F47; Ja                      |
| `U+0F48`  |                  |                   |                            |                	                   |
| `U+0F49`  |                  |                   |                            | &#X0F49; Nya 		                   |
| `U+0F4A`  |                  |                   |                            | &#X0F4A; Tta 		                   |
| `U+0F4B`  |                  |                   |                            | &#X0F4B; Ttha		                   |
| `U+0F4C`  |                  |                   |                            | &#X0F4C; Dda 		                   |
| `U+0F4D`  |                  |                   |                            | &#X0F4D; Ddha		                   |
| `U+0F4E`  |                  |                   |                            | &#X0F4E; Nna 		                   |
| `U+0F4F`  |                  |                   |                            | &#X0F4F; Ta  		               |
| | | | | |
| `U+0F50`  |                  |                   |                            | &#X0F50; Tha                     |
| `U+0F51`  |                  |                   |                            | &#X0F51; Da                      |
| `U+0F52`  |                  |                   |                            | &#X0F52; Dha                     |
| `U+0F53`  |                  |                   |                            | &#X0F53; Na                      |
| `U+0F54`  |                  |                   |                            | &#X0F54; Pa                      |
| `U+0F55`  |                  |                   |                            | &#X0F55; Pha                     |
| `U+0F56`  |                  |                   |                            | &#X0F56; Ba                      |
| `U+0F57`  |                  |                   |                            | &#X0F57; Bha                     |
| `U+0F58`  |                  |                   |                            | &#X0F58; Ma                      |
| `U+0F59`  |                  |                   |                            | &#X0F59; Tsa                     |
| `U+0F5A`  |                  |                   |                            | &#X0F5A; Tsha                    |
| `U+0F5B`  |                  |                   |                            | &#X0F5B; Dza                     |
| `U+0F5C`  |                  |                   |                            | &#X0F5C; Dzha                    |
| `U+0F5D`  |                  |                   |                            | &#X0F5D; Wa                      |
| `U+0F5E`  |                  |                   |                            | &#X0F5E; Zha                     |
| `U+0F5F`  |                  |                   |                            | &#X0F5F; Za                      |
| | | | | |
| `U+0F60`  |                  |                   |                            | &#X0F60; -A                               |
| `U+0F61`  |                  |                   |                            | &#X0F61; Ya                               |
| `U+0F62`  |                  |                   |                            | &#X0F62; Ra                               |
| `U+0F63`  |                  |                   |                            | &#X0F63; La                               |
| `U+0F64`  |                  |                   |                            | &#X0F64; Sha                              |
| `U+0F65`  |                  |                   |                            | &#X0F65; Ssa                              |
| `U+0F66`  |                  |                   |                            | &#X0F66; Sa                               |
| `U+0F67`  |                  |                   |                            | &#X0F67; Ha                               |
| `U+0F68`  |                  |                   |                            | &#X0F68; A                                |
| `U+0F69`  |                  |                   |                            | &#X0F69; Kssa                             |
| `U+0F6A`  |                  |                   |                            | &#X0F6A; Fixed-Form Ra                    |
| `U+0F6B`  |                  |                   |                            | &#X0F6B; Kka                              |
| `U+0F6C`  |                  |                   |                            | &#X0F6C; Rra                              |
| `U+0F6D`  |                  |                   |                            | 		                       |
| `U+0F6E`  |                  |                   |                            | 		                       |
| `U+0F6F`  |                  |                   |                            | 		                       |
| | | | | |
| `U+0F70`  |                  |                   |                            |                              |
| `U+0F71`  |                  |                   |                            | &#X0F71; Sign Aa                            |
| `U+0F72`  |                  |                   |                            | &#X0F72; Sign I                             |
| `U+0F73`  |                  |                   |                            | &#X0F73; Sign Ii                            |
| `U+0F74`  |                  |                   |                            | &#X0F74; Sign U                             |
| `U+0F75`  |                  |                   |                            | &#X0F75; Sign Uu                            |
| `U+0F76`  |                  |                   |                            | &#X0F76; Sign Vocalic R                     |
| `U+0F77`  |                  |                   |                            | &#X0F77; Sign Vocalic Rr                    |
| `U+0F78`  |                  |                   |                            | &#X0F78; Sign Vocalic L                     |
| `U+0F79`  |                  |                   |                            | &#X0F79; Sign Vocalic Ll                    |
| `U+0F7A`  |                  |                   |                            | &#X0F7A; Sign E                             |
| `U+0F7B`  |                  |                   |                            | &#X0F7B; Sign Ee                            |
| `U+0F7C`  |                  |                   |                            | &#X0F7C; Sign O                             |
| `U+0F7D`  |                  |                   |                            | &#X0F7D; Sign Oo                            |
| `U+0F7E`  |                  |                   |                            | &#X0F7E; Sign Rjes Su Nga Ro                      |
| `U+0F7F`  |                  |                   |                            | &#X0F7F; Sign Rnam Bcad                           |
| | | | | |
| `U+0F80`  |                  |                   |                            | &#X0F80; Sign Reversed I            |
| `U+0F81`  |                  |                   |                            | &#X0F81; Sign Reversed Ii           |
| `U+0F82`  |                  |                   |                            | &#X0F82; Sign Nyi Zla Naa Da              |
| `U+0F83`  |                  |                   |                            | &#X0F83; Sign Sna Ldan                    |
| `U+0F84`  |                  |                   |                            | &#X0F84; Mark Halanta                     |
| `U+0F85`  |                  |                   |                            | &#X0F85; Mark Paluta                      |
| `U+0F86`  |                  |                   |                            | &#X0F86; Sign Lci Rtags                   |
| `U+0F87`  |                  |                   |                            | &#X0F87; Sign Yang Rtags                  |
| `U+0F88`  |                  |                   |                            | &#X0F88; Sign Lce Tsa Can                 |
| `U+0F89`  |                  |                   |                            | &#X0F89; Sign Mchu Can                    |
| `U+0F8A`  |                  |                   |                            | &#X0F8A; Sign Gru Can Rgyings             |
| `U+0F8B`  |                  |                   |                            | &#X0F8B; Sign Gru Med Rgyings             |
| `U+0F8C`  |                  |                   |                            | &#X0F8C; Sign Inverted Mchu Can           |
| `U+0F8D`  |                  |                   |                            | &#X0F8D; Subjoined Sign Lce Tsa Can       |
| `U+0F8E`  |                  |                   |                            | &#X0F8E; Subjoined Sign Mchu Can          |
| `U+0F8F`  |                  |                   |                            | &#X0F8F; Subjoined Sign Inverted Mchu Can |
| | | | | |
| `U+0F90`  |                  |                   |                            | &#X0F90; Subjoined Ka                     |
| `U+0F91`  |                  |                   |                            | &#X0F91; Subjoined Kha                    |
| `U+0F92`  |                  |                   |                            | &#X0F92; Subjoined Ga                     |
| `U+0F93`  |                  |                   |                            | &#X0F93; Subjoined Gha                    |
| `U+0F94`  |                  |                   |                            | &#X0F94; Subjoined Nga                    |
| `U+0F95`  |                  |                   |                            | &#X0F95; Subjoined Ca                     |
| `U+0F96`  |                  |                   |                            | &#X0F96; Subjoined Cha                    |
| `U+0F97`  |                  |                   |                            | &#X0F97; Subjoined Ja                     |
| `U+0F98`  |                  |                   |                            | 		                       |
| `U+0F99`  |                  |                   |                            | &#X0F99; Subjoined Nya                     |
| `U+0F9A`  |                  |                   |                            | &#X0F9A; Subjoined Tta                     |
| `U+0F9B`  |                  |                   |                            | &#X0F9B; Subjoined Ttha                    |
| `U+0F9C`  |                  |                   |                            | &#X0F9C; Subjoined Dda                     |
| `U+0F9D`  |                  |                   |                            | &#X0F9D; Subjoined Ddha                    |
| `U+0F9E`  |                  |                   |                            | &#X0F9E; Subjoined Nna                     |
| `U+0F9F`  |                  |                   |                            | &#X0F9F; Subjoined Ta                      |
| | | | | |
| `U+0FA0`  |                  |                   |                            | &#X0FA0; Subjoined Tha                     |
| `U+0FA1`  |                  |                   |                            | &#X0FA1; Subjoined Da                      |
| `U+0FA2`  |                  |                   |                            | &#X0FA2; Subjoined Dha                     |
| `U+0FA3`  |                  |                   |                            | &#X0FA3; Subjoined Na                      |
| `U+0FA4`  |                  |                   |                            | &#X0FA4; Subjoined Pa                      |
| `U+0FA5`  |                  |                   |                            | &#X0FA5; Subjoined Pha                     |
| `U+0FA6`  |                  |                   |                            | &#X0FA6; Subjoined Ba                      |
| `U+0FA7`  |                  |                   |                            | &#X0FA7; Subjoined Bha                     |
| `U+0FA8`  |                  |                   |                            | &#X0FA8; Subjoined Ma                      |
| `U+0FA9`  |                  |                   |                            | &#X0FA9; Subjoined Tsa                     |
| `U+0FAA`  |                  |                   |                            | &#X0FAA; Subjoined Tsha                    |
| `U+0FAB`  |                  |                   |                            | &#X0FAB; Subjoined Dza                     |
| `U+0FAC`  |                  |                   |                            | &#X0FAC; Subjoined Dzha                    |
| `U+0FAD`  |                  |                   |                            | &#X0FAD; Subjoined Wa                      |
| `U+0FAE`  |                  |                   |                            | &#X0FAE; Subjoined Zha                     |
| `U+0FAF`  |                  |                   |                            | &#X0FAF; Subjoined Za                      |
| | | | | |
| `U+0FB0`  |                  |                   |                            | &#X0FB0; Subjoined -A                      |
| `U+0FB1`  |                  |                   |                            | &#X0FB1; Subjoined Ya                      |
| `U+0FB2`  |                  |                   |                            | &#X0FB2; Subjoined Ra                      |
| `U+0FB3`  |                  |                   |                            | &#x0FB3; Subjoined La                      |
| `U+0FB4`  |                  |                   |                            | &#X0FB4; Subjoined Sha                     |
| `U+0FB5`  |                  |                   |                            | &#X0FB5; Subjoined Ssa                     |
| `U+0FB6`  |                  |                   |                            | &#X0FB6; Subjoined Sa                      |
| `U+0FB7`  |                  |                   |                            | &#X0FB7; Subjoined Ha                      |
| `U+0FB8`  |                  |                   |                            | &#X0FB8; Subjoined A                       |
| `U+0FB9`  |                  |                   |                            | &#X0FB9; Subjoined Kssa                    |
| `U+0FBA`  |                  |                   |                            | &#X0FBA; Subjoined Fixed-Form Wa           |
| `U+0FBB`  |                  |                   |                            | &#X0FBB; Subjoined Fixed-Form Ya           |
| `U+0FBC`  |                  |                   |                            | &#X0FBC; Subjoined Fixed-Form Ra           |
| `U+0FBD`  |                  |                   |                            | 		                        |
| `U+0FBE`  |                  |                   |                            | &#X0FBE; Ku Ru Kha                               |
| `U+0FBF`  |                  |                   |                            | &#X0FBF; Ku Ru Kha Bzhi Mig Can                    |
| | | | | |
| `U+0FC0`  |                  |                   |                            | &#X0FC0; Cantillation Sign Heavy Beat  |
| `U+0FC1`  |                  |                   |                            | &#X0FC1; Cantillation Sign Light Beat  |
| `U+0FC2`  |                  |                   |                            | &#X0FC2; Cantillation Sign Cang Te-U   |
| `U+0FC3`  |                  |                   |                            | &#X0FC3; Cantillation Sign Sbub -Chal  |
| `U+0FC4`  |                  |                   |                            | &#X0FC4; Symbol Dril Bu                |
| `U+0FC5`  |                  |                   |                            | &#X0FC5; Symbol Rdo Rje                |
| `U+0FC6`  |                  |                   |                            | &#X0FC6; Symbol Padma Gdan             |
| `U+0FC7`  |                  |                   |                            | &#X0FC7; Symbol Rdo Rje Rgya Gram      |
| `U+0FC8`  |                  |                   |                            | &#X0FC8; Symbol Phur Pa                |
| `U+0FC9`  |                  |                   |                            | &#X0FC9; Symbol Nor Bu                 |
| `U+0FCA`  |                  |                   |                            | &#X0FCA; Symbol Nor Bu Nyis -Khyil     |
| `U+0FCB`  |                  |                   |                            | &#X0FCB; Symbol Nor Bu Gsum -Khyil     |
| `U+0FCC`  |                  |                   |                            | &#X0FCC; Symbol Nor Bu Bzhi -Khyil     |
| `U+0FCD`  |                  |                   |                            | 		                       |
| `U+0FCE`  |                  |                   |                            | &#X0FCE; Sign Rdel Nag Rdel Dkar |
| `U+0FCF`  |                  |                   |                            | &#X0FCF; Sign Rdel Nag Gsum      |
| | | | | |
| `U+0FD0`  |                  |                   |                            | &#x0FD0; Mark Bska- Shog Gi Mgo Rgyan             |
| `U+0FD1`  |                  |                   |                            | &#X0FD1; Mark Mnyam Yig Gi Mgo Rgyan              |
| `U+0FD2`  |                  |                   |                            | &#X0FD2; Mark Nyis Tsheg                          |
| `U+0FD3`  |                  |                   |                            | &#X0FD3; Mark Initial Brda Rnying Yig Mgo Mdun Ma |
| `U+0FD4`  |                  |                   |                            | &#X0FD4; Mark Closing Brda Rnying Yig Mgo Sgab Ma |
| `U+0FD5`  |                  |                   |                            | &#X0FD5; Right-Facing Svasti Sign           |
| `U+0FD6`  |                  |                   |                            | &#X0FD6; Left-Facing Svasti Sign            |
| `U+0FD7`  |                  |                   |                            | &#x0FD7; Right-Facing Svasti Sign With Dots |
| `U+0FD8`  |                  |                   |                            | &#x0FD8; Left-Facing Svasti Sign With Dots  |
| `U+0FD9`  |                  |                   |                            | &#x0FD9; Mark Leading Mchan Rtags   |
| `U+0FDA`  |                  |                   |                            | &#x0FDA; Mark Trailing Mchan Rtags  |
| `U+0FDB`  |                  |                   |                            | 		                       |
| `U+0FDC`  |                  |                   |                            | 		                       |
| `U+0FDD`  |                  |                   |                            | 		                       |
| `U+0FDE`  |                  |                   |                            | 		                       |
| `U+0FDF`  |                  |                   |                            | 		                       |
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

