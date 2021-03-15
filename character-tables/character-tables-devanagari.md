# Devanagari character tables #

This document lists the per-character shaping information needed to
[shape Devanagari text](../opentype-shaping-devanagari.md).

**Table of Contents**

  - [Devanagari character table](#devanagari-character-table)
  - [Devanagari Extended character table](#devanagari-extended-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Devanagari character table ##

Devanagari glyphs should be classified as in the following
table. Codepoints in the Devanagari block with no assigned meaning are
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
|`U+0953`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x0953; Grave accent        |
|`U+0954`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x0954; Acute accent        |
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
|`U+0966`   | Number           | NUMBER            | _null_                     | &#x0966; Digit Zero          |
|`U+0967`   | Number           | NUMBER            | _null_                     | &#x0967; Digit One           |
|`U+0968`   | Number           | NUMBER            | _null_                     | &#x0968; Digit Two           |
|`U+0969`   | Number           | NUMBER            | _null_                     | &#x0969; Digit Three         |
|`U+096A`   | Number           | NUMBER            | _null_                     | &#x096A; Digit Four          |
|`U+096B`   | Number           | NUMBER            | _null_                     | &#x096B; Digit Five          |
|`U+096C`   | Number           | NUMBER            | _null_                     | &#x096C; Digit Six           |
|`U+096D`   | Number           | NUMBER            | _null_                     | &#x096D; Digit Seven         |
|`U+096E`   | Number           | NUMBER            | _null_                     | &#x096E; Digit Eight         |
|`U+096F`   | Number           | NUMBER            | _null_                     | &#x096F; Digit Nine          |
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



## Devanagari Extended character table ##

> Note: the cantillation marks of the "combining consonant" variety in
> the Devanagari Extended block are _not_ considered consonants for
> shaping purposes (including syllable identification, the
> determination of the base consonant, or positioning "Reph").

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
|`U+A8F2`   | Letter           | SYMBOL            | _null_                     | &#xA8F2; Spacing Candrabindu |
|`U+A8F3`   | Letter           | BINDU             | _null_                     | &#xA8F3; Candrabindu Virama  |
|`U+A8F4`   | Letter           | _null_            | _null_                     | &#xA8F4; Double Candrabindu Virama|
|`U+A8F5`   | Letter           | _null_            | _null_                     | &#xA8F5; Candrabindu Two     |
|`U+A8F6`   | Letter           | _null_            | _null_                     | &#xA8F6; Candrabindu Three   |
|`U+A8F7`   | Letter           | SYMBOL            | _null_                     | &#xA8F7; Candrabindu Avagraha|
|`U+A8F8`   | Punctuation      | _null_            | _null_                     | &#xA8F8; Pushpika            |
|`U+A8F9`   | Punctuation      | _null_            | _null_                     | &#xA8F9; Gap Filler          |
|`U+A8FA`   | Punctuation      | _null_            | _null_                     | &#xA8FA; Caret               |
|`U+A8FB`   | Letter           | _null_            | _null_                     | &#xA8FB; Headstroke          |
|`U+A8FC`   | Punctuation      | _null_            | _null_                     | &#xA8FC; Siddham             |
|`U+A8FD`   | Letter           | _null_            | _null_                     | &#xA8FD; Jain Om             |
|`U+A8FE`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#xA8FE; Ay                  |
|`U+A8FF`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#xA8FF; Sign Ay             |



## Vedic Extensions character table ##

Sanskrit runs written in the Devanagari script may also include
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


The zero-width joiner (ZWJ) is primarily used to prevent the formation
of a conjunct from a "_Consonant_,Halant,_Consonant_" sequence. The
sequence "_Consonant_,Halant,ZWJ,_Consonant_" blocks the formation of
a conjunct between the two consonants. 

Note, however, that the "_Consonant_,Halant" subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner (ZWNJ) must be used instead. The
sequence "_Consonant_,Halant,ZWNJ,_Consonant_" should produce the
first consonant in its standard form, followed by an explicit
"Halant".

A secondary usage of the zero-width joiner is to prevent the formation of
"Reph". An initial "Ra,Halant,ZWJ" sequence should not produce a "Reph",
where an initial "Ra,Halant" sequence without the zero-width joiner
otherwise would.

The no-break space (NBSP) is primarily used to display those
codepoints that are defined as non-spacing (marks, dependent vowels
(matras), below-base consonant forms, and post-base consonant forms)
in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match "NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or "NBSP,_matra_".

