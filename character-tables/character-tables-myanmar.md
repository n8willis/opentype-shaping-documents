# Myanmar character tables #

This document lists the per-character shaping information needed to
[shape Myanmar text](../opentype-shaping-myanmar.md).

**Table of Contents**

  - [Myanmar character table](#myanmar-character-table)
  - [Myanmar Extended character tables](#myanmar-extended-character-tables)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Myanmar character table ##

Myanmar glyphs should be classified as in the following
table. Codepoints in the Myanmar block with no assigned meaning are
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
|`U+1000`   | Letter           | CONSONANT         | _null_                     | &#x1000; Ka                  |
|`U+1001`   | Letter           | CONSONANT         | _null_                     | &#x1001; Kha                 |
|`U+1002`   | Letter           | CONSONANT         | _null_                     | &#x1002; Ga                  |
|`U+1003`   | Letter           | CONSONANT         | _null_                     | &#x1003; Gha                 |
|`U+1004`   | Letter           | CONSONANT         | _null_                     | &#x1004; Nga                 |
|`U+1005`   | Letter           | CONSONANT         | _null_                     | &#x1005; Ca                  |
|`U+1006`   | Letter           | CONSONANT         | _null_                     | &#x1006; Cha                 |
|`U+1007`   | Letter           | CONSONANT         | _null_                     | &#x1007; Ja                  |
|`U+1008`   | Letter           | CONSONANT         | _null_                     | &#x1008; Jha                 |
|`U+1009`   | Letter           | CONSONANT         | _null_                     | &#x1009; Nya                 |
|`U+100A`   | Letter           | CONSONANT         | _null_                     | &#x100A; Nnya                |
|`U+100B`   | Letter           | CONSONANT         | _null_                     | &#x100B; Tta                 |
|`U+100C`   | Letter           | CONSONANT         | _null_                     | &#x100C; Ttha                |
|`U+100D`   | Letter           | CONSONANT         | _null_                     | &#x100D; Dda                 |
|`U+100E`   | Letter           | CONSONANT         | _null_                     | &#x100E; DDha                |
|`U+100F`   | Letter           | CONSONANT         | _null_                     | &#x100F; Nna                 |
| | | | |
|`U+1010`   | Letter           | CONSONANT         | _null_                     | &#x1010; Ta                  |
|`U+1011`   | Letter           | CONSONANT         | _null_                     | &#x1011; Tha                 |
|`U+1012`   | Letter           | CONSONANT         | _null_                     | &#x1012; Da                  |
|`U+1013`   | Letter           | CONSONANT         | _null_                     | &#x1013; Dha                 |
|`U+1014`   | Letter           | CONSONANT         | _null_                     | &#x1014; Na                  |
|`U+1015`   | Letter           | CONSONANT         | _null_                     | &#x1015; Pa                  |
|`U+1016`   | Letter           | CONSONANT         | _null_                     | &#x1016; Pha                 |
|`U+1017`   | Letter           | CONSONANT         | _null_                     | &#x1017; Ba                  |
|`U+1018`   | Letter           | CONSONANT         | _null_                     | &#x1018; Bha                 |
|`U+1019`   | Letter           | CONSONANT         | _null_                     | &#x1019; Ma                  |
|`U+101A`   | Letter           | CONSONANT         | _null_                     | &#x101A; Ya                  |
|`U+101B`   | Letter           | CONSONANT         | _null_                     | &#x101B; Ra                  |
|`U+101C`   | Letter           | CONSONANT         | _null_                     | &#x101C; La                  |
|`U+101D`   | Letter           | CONSONANT         | _null_                     | &#x101D; Wa                  |
|`U+101E`   | Letter           | CONSONANT         | _null_                     | &#x101E; Sa                  |
|`U+101F`   | Letter           | CONSONANT         | _null_                     | &#x101F; Ha                  |
| | | | |
|`U+1020`   | Letter           | CONSONANT         | _null_                     | &#x1020; Lla                 |
|`U+1021`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1021; A                   |
|`U+1022`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1022; Shan A              |
|`U+1023`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1023; I                   |
|`U+1024`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1024; Ii                  |
|`U+1025`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1025; U                   |
|`U+1026`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1026; Uu                  |
|`U+1027`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1027; E                   |
|`U+1028`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1028; Mon E               |
|`U+1029`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1029; O                   |
|`U+102A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x102A; Au                  |
|`U+102B`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x102B; Sign Tall Aa        |
|`U+102C`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x102C; Sign Aa             |
|`U+102D`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x102D; Sign I              |
|`U+102E`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x102E; Sign Ii             |
|`U+102F`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x102F; Sign U              |
| | | | |
|`U+1030`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x1030; Sign Uu             |
|`U+1031`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x1031; Sign E              |
|`U+1032`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1032; Sign Ai             |
|`U+1033`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1033; Sign Mon Ii         |
|`U+1034`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1034; Sign Mon O          |
|`U+1035`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1035; Sign E Above        |
|`U+1036`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x1036; Anusvara            |
|`U+1037`   | Mark [Mn]        | TONE_MARKER       | BOTTOM_POSITION            | &#x1037; Dot Below           |
|`U+1038`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x1038; Visarga             |
|`U+1039`   | Mark [Mn]        | INVISIBLE_STACKER | _null_                     | &#x1039; Virama              |
|`U+103A`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION               | &#x103A; Asat                |
|`U+103B`   | Mark [Mc]        | CONSONANT_MEDIAL  | RIGHT_POSITION             | &#x103B; Sign Medial Ya      |
|`U+103C`   | Mark [Mc]        | CONSONANT_MEDIAL  | _null_                     | &#x103C; Sign Medial Ra      |
|`U+103D`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x103D; Sign Medial Wa      |
|`U+103E`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x103E; Sign Medial Ha      |
|`U+103F`   | Letter           | CONSONANT         | _null_                     | &#x103F; Great Sa            |
| | | | |
|`U+1040`   | Number           | NUMBER            | _null_                     | &#x1040; Digit Zero          |
|`U+1041`   | Number           | NUMBER            | _null_                     | &#x1041; Digit One           |
|`U+1042`   | Number           | NUMBER            | _null_                     | &#x1042; Digit Two           |
|`U+1043`   | Number           | NUMBER            | _null_                     | &#x1043; Digit Three         |
|`U+1044`   | Number           | NUMBER            | _null_                     | &#x1044; Digit Four          |
|`U+1045`   | Number           | NUMBER            | _null_                     | &#x1045; Digit Five          |
|`U+1046`   | Number           | NUMBER            | _null_                     | &#x1046; Digit Six           |
|`U+1047`   | Number           | NUMBER            | _null_                     | &#x1047; Digit Seven         |
|`U+1048`   | Number           | NUMBER            | _null_                     | &#x1048; Digit Eight         |
|`U+1049`   | Number           | NUMBER            | _null_                     | &#x1049; Digit Nine          |
|`U+104A`   | Punctuation      | _null_            | _null_                     | &#x104A; Little Section      |
|`U+104B`   | Punctuation      | _null_            | _null_                     | &#x104B; Section             |
|`U+104C`   | Punctuation      | _null_            | _null_                     | &#x104C; Locative            |
|`U+104D`   | Punctuation      | _null_            | _null_                     | &#x104D; Completed           |
|`U+104E`   | Punctuation      | CONSONANT_PLACEHOLDER| _null_                  | &#x104E; Aforementioned      |
|`U+104F`   | Punctuation      | _null_            | _null_                     | &#x104F; Genitive            |
| | | | |
|`U+1050`   | Letter           | CONSONANT         | _null_                     | &#x1050; Sha                 |
|`U+1051`   | Letter           | CONSONANT         | _null_                     | &#x1051; Ssa                 |
|`U+1052`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1052; Vocalic R           |
|`U+1053`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1053; Vocalic Rr          |
|`U+1054`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1054; Vocalic L           |
|`U+1055`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x1055; Vocalic Ll          |
|`U+1056`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1056; Sign Vocalic R      |
|`U+1057`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1057; Sign Vocalic Rr     |
|`U+1058`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x1058; Sign Vocalic L      |
|`U+1059`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x1059; Sign Vocalic Ll     |
|`U+105A`   | Letter           | CONSONANT         | _null_                     | &#x105A; Mon Nga             |
|`U+105B`   | Letter           | CONSONANT         | _null_                     | &#x105B; Mon Jha             |
|`U+105C`   | Letter           | CONSONANT         | _null_                     | &#x105C; Mon Bba             |
|`U+105D`   | Letter           | CONSONANT         | _null_                     | &#x105D; Mon Bbe             |
|`U+105E`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x105E; Sign Mon Medial Na  |
|`U+105F`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x105F; Sign Mon Medial Ma  |
| | | | |
|`U+1060`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x1060; Sign Mon Medial La  |
|`U+1061`   | Letter           | CONSONANT         | _null_                     | &#x1061; Sgaw Karen Sha      |
|`U+1062`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1062; Sign Sgaw Karen Eu  |
|`U+1063`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1063; Tone Sgaw Karen Hathi|
|`U+1064`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1064; Tone Sgaw Karen Ke Pho|
|`U+1065`   | Letter           | CONSONANT         | _null_                     | &#x1065; Western Pwo Karen Tha|
|`U+1066`   | Letter           | CONSONANT         | _null_                     | &#x1066; Western Pwo Karen Pwa|
|`U+1067`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1067; Sign Western Pwo Karen Eu|
|`U+1068`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1068; Sign Western Pwo Karen Ue|
|`U+1069`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1069; Sign Western Pwo Karen Tone 1|
|`U+106A`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x106A; Sign Western Pwo Karen Tone 2|
|`U+106B`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x106B; Sign Western Pwo Karen Tone 3|
|`U+106C`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x106C; Sign Western Pwo Karen Tone 4|
|`U+106D`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x106D; Sign Western Pwo Karen Tone 5|
|`U+106E`   | Letter           | CONSONANT         | _null_                     | &#x106E; Eastern Pwo Karen Nna|
|`U+106F`   | Letter           | CONSONANT         | _null_                     | &#x106F; Eastern Pwo Karen Ywa|
| | | | |
|`U+1070`   | Letter           | CONSONANT         | _null_                     | &#x1070; Eastern Pwo Karen Ghwa|
|`U+1071`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1071; Sign Geba Karen I   |
|`U+1072`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1072; Sign Kayah Oe       |
|`U+1073`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1073; Sign Kayah U        |
|`U+1074`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1074; Sign Kayah Ee       |
|`U+1075`   | Letter           | CONSONANT         | _null_                     | &#x1075; Shan Ka             |
|`U+1076`   | Letter           | CONSONANT         | _null_                     | &#x1076; Shan Kha            |
|`U+1077`   | Letter           | CONSONANT         | _null_                     | &#x1077; Shan Ga             |
|`U+1078`   | Letter           | CONSONANT         | _null_                     | &#x1078; Shan Ca             |
|`U+1079`   | Letter           | CONSONANT         | _null_                     | &#x1079; Shan Za             |
|`U+107A`   | Letter           | CONSONANT         | _null_                     | &#x107A; Shan Nya            |
|`U+107B`   | Letter           | CONSONANT         | _null_                     | &#x107B; Shan Da             |
|`U+107C`   | Letter           | CONSONANT         | _null_                     | &#x107C; Shan Na             |
|`U+107D`   | Letter           | CONSONANT         | _null_                     | &#x107D; Shan Pha            |
|`U+107E`   | Letter           | CONSONANT         | _null_                     | &#x107E; Shan Fa             |
|`U+107F`   | Letter           | CONSONANT         | _null_                     | &#x107F; Shan Ba             |
| | | | |
|`U+1080`   | Letter           | CONSONANT         | _null_                     | &#x1080; Shan Tha            |
|`U+1081`   | Letter           | CONSONANT         | _null_                     | &#x1081; Shan Ha             |
|`U+1082`   | Mark [Mn]        | CONSONANT_MEDIAL  | BOTTOM_POSITION            | &#x1082; Sign Shan Medial Wa |
|`U+1083`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x1083; Sign Shan Aa        |
|`U+1084`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x1084; Sign Shan E         |
|`U+1085`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1085; Sign Shan E Above   |
|`U+1086`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x1086; Sign Shan Final Y   |
|`U+1087`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1087; Sign Shan Tone 2    |
|`U+1088`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1088; Sign Shan Tone 3    |
|`U+1089`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x1089; Sign Shan Tone 5    |
|`U+108A`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x108A; Sign Shan Tone 6    |
|`U+108B`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x108B; Sign Shan Council Tone 2|
|`U+108C`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x108C; Sign Shan Council Tone 3|
|`U+108D`   | Mark [Mn]        | TONE_MARKER       | BOTTOM_POSITION            | &#x108D; Sign Shan Council Emphatic Tone|
|`U+108E`   | Letter           | CONSONANT         | _null_                     | &#x108E; Rumai Palaung Fa    |
|`U+108F`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x108F; Sign Rumai Palaung Tone 5|
| | | | |
|`U+1090`   | Number           | NUMBER            | _null_                     | &#x1090; Shan Digit Zero     |
|`U+1091`   | Number           | NUMBER            | _null_                     | &#x1091; Shan Digit One      |
|`U+1092`   | Number           | NUMBER            | _null_                     | &#x1092; Shan Digit Two      |
|`U+1093`   | Number           | NUMBER            | _null_                     | &#x1093; Shan Digit Three    |
|`U+1094`   | Number           | NUMBER            | _null_                     | &#x1094; Shan Digit Four     |
|`U+1095`   | Number           | NUMBER            | _null_                     | &#x1095; Shan Digit Five     |
|`U+1096`   | Number           | NUMBER            | _null_                     | &#x1096; Shan Digit Six      |
|`U+1097`   | Number           | NUMBER            | _null_                     | &#x1097; Shan Digit Seven    |
|`U+1098`   | Number           | NUMBER            | _null_                     | &#x1098; Shan Digit Eight    |
|`U+1099`   | Number           | NUMBER            | _null_                     | &#x1099; Shan Digit Nine     |
|`U+109A`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x109A; Sign Khamti Tone 1  |
|`U+109B`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#x109B; Sign Khamti Tone 3  |
|`U+109C`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x109C; Sign Aiton A        |
|`U+109D`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x109D; Sign Aiton Ai       |
|`U+109E`   | Symbol           | SYMBOL            | _null_                     | &#x109E; Shan One            |
|`U+109F`   | Symbol           | SYMBOL            | _null_                     | &#x109F; Shan Exclamation    |



## Myanmar Extended character tables ##

### Myanmar Extended A character table ###

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+AA60`   | Letter           | CONSONANT         | _null_                     | &#xAA60; Khamti Ga           |
|`U+AA61`   | Letter           | CONSONANT         | _null_                     | &#xAA61; Khamti Ca           |
|`U+AA62`   | Letter           | CONSONANT         | _null_                     | &#xAA62; Khamti Cha          |
|`U+AA63`   | Letter           | CONSONANT         | _null_                     | &#xAA63; Khamti Ja           |
|`U+AA64`   | Letter           | CONSONANT         | _null_                     | &#xAA64; Khamti Jha          |
|`U+AA65`   | Letter           | CONSONANT         | _null_                     | &#xAA65; Khamti Nya          |
|`U+AA66`   | Letter           | CONSONANT         | _null_                     | &#xAA66; Khamti Tta          |
|`U+AA67`   | Letter           | CONSONANT         | _null_                     | &#xAA67; Khamti Ttha         |
|`U+AA68`   | Letter           | CONSONANT         | _null_                     | &#xAA68; Khamti Dda          |
|`U+AA69`   | Letter           | CONSONANT         | _null_                     | &#xAA69; Khamti Ddha         |
|`U+AA6A`   | Letter           | CONSONANT         | _null_                     | &#xAA6A; Khamti Dha          |
|`U+AA6B`   | Letter           | CONSONANT         | _null_                     | &#xAA6B; Khamti Na           |
|`U+AA6C`   | Letter           | CONSONANT         | _null_                     | &#xAA6C; Khamti Sa           |
|`U+AA6D`   | Letter           | CONSONANT         | _null_                     | &#xAA6D; Khamti Ha           |
|`U+AA6E`   | Letter           | CONSONANT         | _null_                     | &#xAA6E; Khamti Hha          |
|`U+AA6F`   | Letter           | CONSONANT         | _null_                     | &#xAA6F; Khamti Fa           |
| | | | |
|`U+AA70`   | Letter           | _null_            | _null_                     | &#xAA70; Khamti Reduplication|
|`U+AA71`   | Letter           | CONSONANT         | _null_                     | &#xAA71; Khamti Xa           |
|`U+AA72`   | Letter           | CONSONANT         | _null_                     | &#xAA72; Khamti Za           |
|`U+AA73`   | Letter           | CONSONANT         | _null_                     | &#xAA73; Khamti Ra           |
|`U+AA74`   | Letter           | CONSONANT_PLACEHOLDER| _null_                  | &#xAA74; Khamti Oay          |
|`U+AA75`   | Letter           | CONSONANT_PLACEHOLDER| _null_                  | &#xAA75; Khamti Qn           |
|`U+AA76`   | Letter           | CONSONANT_PLACEHOLDER| _null_                  | &#xAA76; Khamti Hm           |
|`U+AA77`   | Symbol           | SYMBOL            | _null_                     | &#xAA77; Khamti Aiton Exclamation|
|`U+AA78`   | Symbol           | SYMBOL            | _null_                     | &#xAA78; Khamti Aiton One    |
|`U+AA79`   | Symbol           | SYMBOL            | _null_                     | &#xAA79; Khamti Aiton Two    |
|`U+AA7A`   | Letter           | CONSONANT         | _null_                     | &#xAA7A; Khamti Aiton Ra     |
|`U+AA7B`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#xAA7B; Sign Pao Karen Tone |
|`U+AA7C`   | Mark [Mn]        | TONE_MARKER       | TOP_POSITION               | &#xAA7C; Sign Tai Laing Tone 2|
|`U+AA7D`   | Mark [Mc]        | TONE_MARKER       | RIGHT_POSITION             | &#xAA7D; Sign Tai Laing Tone 5|
|`U+AA7E`   | Letter           | CONSONANT         | _null_                     | &#xAA7E; Shwe Palaung Cha    |
|`U+AA7F`   | Letter           | CONSONANT         | _null_                     | &#xAA7F; Shwe Palaung Sha    |

### Myanmar Extended B character table ###

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+A9E0`   | Letter           | CONSONANT         | _null_                     | &#xA9E0; Shan Gha            |
|`U+A9E1`   | Letter           | CONSONANT         | _null_                     | &#xA9E1; Shan Cha            |
|`U+A9E2`   | Letter           | CONSONANT         | _null_                     | &#xA9E2; Shan Jha            |
|`U+A9E3`   | Letter           | CONSONANT         | _null_                     | &#xA9E3; Shan Nna            |
|`U+A9E4`   | Letter           | CONSONANT         | _null_                     | &#xA9E4; Shan Bha            |
|`U+A9E5`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#xA9E5; Sign Shan Saw       |
|`U+A9E6`   | Letter           | _null_            | _null_                     | &#xA9E6; Shan Reduplication  |
|`U+A9E7`   | Letter           | CONSONANT         | _null_                     | &#xA9E7; Tai Laing Nya       |
|`U+A9E8`   | Letter           | CONSONANT         | _null_                     | &#xA9E8; Tai Laing Fa        |
|`U+A9E9`   | Letter           | CONSONANT         | _null_                     | &#xA9E9; Tai Laing Ga        |
|`U+A9EA`   | Letter           | CONSONANT         | _null_                     | &#xA9EA; Tai Laing Gha       |
|`U+A9EB`   | Letter           | CONSONANT         | _null_                     | &#xA9EB; Tai Laing Ja        |
|`U+A9EC`   | Letter           | CONSONANT         | _null_                     | &#xA9EC; Tai Laing Jha       |
|`U+A9ED`   | Letter           | CONSONANT         | _null_                     | &#xA9ED; Tai Laing Dda       |
|`U+A9EE`   | Letter           | CONSONANT         | _null_                     | &#xA9EE; Tai Laing Ddha      |
|`U+A9EF`   | Letter           | CONSONANT         | _null_                     | &#xA9EF; Tai Laing Nna       |
| | | | |
|`U+A9F0`   | Number           | NUMBER            | _null_                     | &#xA9F0; Tai Laing Digit Zero|
|`U+A9F1`   | Number           | NUMBER            | _null_                     | &#xA9F1; Tai Laing Digit One |
|`U+A9F2`   | Number           | NUMBER            | _null_                     | &#xA9F2; Tai Laing Digit Two |
|`U+A9F3`   | Number           | NUMBER            | _null_                     | &#xA9F3; Tai Laing Digit Three|
|`U+A9F4`   | Number           | NUMBER            | _null_                     | &#xA9F4; Tai Laing Digit Four|
|`U+A9F5`   | Number           | NUMBER            | _null_                     | &#xA9F5; Tai Laing Digit Five|
|`U+A9F6`   | Number           | NUMBER            | _null_                     | &#xA9F6; Tai Laing Digit Six |
|`U+A9F7`   | Number           | NUMBER            | _null_                     | &#xA9F7; Tai Laing Digit Seven|
|`U+A9F8`   | Number           | NUMBER            | _null_                     | &#xA9F8; Tai Laing Digit Eight|
|`U+A9F9`   | Number           | NUMBER            | _null_                     | &#xA9F9; Tai Laing Digit Nine|
|`U+A9FA`   | Letter           | CONSONANT         | _null_                     | &#xA9FA; Tai Laing Lla       |
|`U+A9FB`   | Letter           | CONSONANT         | _null_                     | &#xA9FB; Tai Laing Da        |
|`U+A9FC`   | Letter           | CONSONANT         | _null_                     | &#xA9FC; Tai Laing Dha       |
|`U+A9FD`   | Letter           | CONSONANT         | _null_                     | &#xA9FD; Tai Laing Ba        |
|`U+A9FE`   | Letter           | CONSONANT         | _null_                     | &#xA9FE; Tai Laing Bha       |
|`U+A9FF`   | _unassigned_     |                   |                            |                              |



## Vedic Extensions character table ##

Sanskrit runs written in the Myanmar script may also include
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
of Myanmar text include the dotted-circle placeholder (`U+25CC`), the
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

