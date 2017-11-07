# Khmer character tables #

This document lists the per-character shaping information needed to
[shape Khmer text](opentype-shaping-khmer.md).

**Table of Contents**

  - [Khmer character table](#khmer-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Khmer character table ##

Khmer glyphs should be classified as in the following
table. Codepoints in the Khmer block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Khmer block, such as
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
|`U+1780`   | Letter           | CONSONANT         | _null_                     | &#x1780; Ka                  |
|`U+1781`   | Letter           | CONSONANT         | _null_                     | &#x1781; Kha                 |
|`U+1782`   | Letter           | CONSONANT         | _null_                     | &#x1782; Ko                  |
|`U+1783`   | Letter           | CONSONANT         | _null_                     | &#x1783; Kho                 |
|`U+1784`   | Letter           | CONSONANT         | _null_                     | &#x1784; Ngo                 |
|`U+1785`   | Letter           | CONSONANT         | _null_                     | &#x1785; Ca                  |
|`U+1786`   | Letter           | CONSONANT         | _null_                     | &#x1786; Cha                 |
|`U+1787`   | Letter           | CONSONANT         | _null_                     | &#x1787; Co                  |
|`U+1788`   | Letter           | CONSONANT         | _null_                     | &#x1788; Cho                 |
|`U+1789`   | Letter           | CONSONANT         | _null_                     | &#x1789; Nyo                 |
|`U+178A`   | Letter           | CONSONANT         | _null_                     | &#x178A; Da                  |
|`U+178B`   | Letter           | CONSONANT         | _null_                     | &#x178B; Ttha                |
|`U+178C`   | Letter           | CONSONANT         | _null_                     | &#x178C; Do                  |
|`U+178D`   | Letter           | CONSONANT         | _null_                     | &#x178D; Ttho                |
|`U+178E`   | Letter           | CONSONANT         | _null_                     | &#x178E; Nno                 |
|`U+178F`   | Letter           | CONSONANT         | _null_                     | &#x178F; Ta                  |
| | | | |																	   
|`U+1790`   | Letter           | CONSONANT         | _null_                     | &#x1790; Tha                 |
|`U+1791`   | Letter           | CONSONANT         | _null_                     | &#x1791; To                  |
|`U+1792`   | Letter           | CONSONANT         | _null_                     | &#x1792; Tho                 |
|`U+1793`   | Letter           | CONSONANT         | _null_                     | &#x1793; No                  |
|`U+1794`   | Letter           | CONSONANT         | _null_                     | &#x1794; Ba                  |
|`U+1795`   | Letter           | CONSONANT         | _null_                     | &#x1795; Pha                 |
|`U+1796`   | Letter           | CONSONANT         | _null_                     | &#x1796; Po                  |
|`U+1797`   | Letter           | CONSONANT         | _null_                     | &#x1797; Pho                 |
|`U+1798`   | Letter           | CONSONANT         | _null_                     | &#x1798; Mo                  |
|`U+1799`   | Letter           | CONSONANT         | _null_                     | &#x1799; Yo                  |
|`U+179A`   | Letter           | CONSONANT         | _null_                     | &#x179A; Ro                  |
|`U+179B`   | Letter           | CONSONANT         | _null_                     | &#x179B; Lo                  |
|`U+179C`   | Letter           | CONSONANT         | _null_                     | &#x179C; Vo                  |
|`U+179D`   | Letter           | CONSONANT         | _null_                     | &#x179D; Sha                 |
|`U+179E`   | Letter           | CONSONANT         | _null_                     | &#x179E; Sso                 |
|`U+179F`   | Letter           | CONSONANT         | _null_                     | &#x179F; Sa                  |
| | | | |																	   
|`U+17A0`   | Letter           | CONSONANT         | _null_                     | &#x17A0; Ha                  |
|`U+17A1`   | Letter           | CONSONANT         | _null_                     | &#x17A1; La                  |
|`U+17A2`   | Letter           | CONSONANT         | _null_                     | &#x17A2; Qa                  |
|`U+17A3`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A3; Qaq                 |
|`U+17A4`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A4; Qaa                 |
|`U+17A5`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A5; Qi                  |
|`U+17A6`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A6; Qii                 |
|`U+17A7`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A7; Qu                  |
|`U+17A8`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A8; Quk                 |
|`U+17A9`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17A9; Quu                 |
|`U+17AA`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AA; Quuv                |
|`U+17AB`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AB; Ry                  |
|`U+17AC`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AC; Ryy                 |
|`U+17AD`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AD; Ly                  |
|`U+17AE`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AE; Lyy                 |
|`U+17AF`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17AF; Qe                  |
| | | | |																	    
|`U+17B0`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17B0; Qai                 |
|`U+17B1`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17B1; Qoo Type One        |
|`U+17B2`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17B2; Qoo Type Two        |
|`U+17B3`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x17B3; Qau                 |
|`U+17B4`   | Mark [Mn]        | _null_            | _null_                     | &#x17B4; Inherent Aq         |
|`U+17B5`   | Mark [Mn]        | _null_            | _null_                     | &#X17B5; Inherent Aa         |
|`U+17B6`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x17B6; Sign Aa             |
|`U+17B7`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x17B7; Sign I              |
|`U+17B8`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x17B8; Sign Ii             |
|`U+17B9`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x17B9; Sign Y              |
|`U+17BA`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x17BA; Sign Yy             |
|`U+17BB`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x17BB; Sign U              |
|`U+17BC`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x17BC; Sign Uu             |
|`U+17BD`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x17BD; Sign Ua             |
|`U+17BE`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_LEFT_POSITION      | &#x17BE; Sign Oe             |
|`U+17BF`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_LEFT_AND_RIGHT_POSITION| &#x17BF; Sign Ya             |
| | | | |																	   
|`U+17C0`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x17C0; Sign Ie             |
|`U+17C1`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x17C1; Sign E              |
|`U+17C2`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x17C2; Sign Ae             |
|`U+17C3`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x17C3; Sign Ai             |
|`U+17C4`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x17C4; Sign Oo             |
|`U+17C5`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x17C5; Sign Au             |
|`U+17C6`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x17C6; Nikahit             |
|`U+17C7`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x17C7; Reahmuk             |
|`U+17C8`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x17C8; Yuukaleapintu       |
|`U+17C9`   | Mark [Mn]        | REGISTER_SHIFTER  | TOP_POSITION               | &#x17C9; Muusikatoan         |
|`U+17CA`   | Mark [Mn]        | REGISTER_SHIFTER  | TOP_POSITION               | &#x17CA; Triisap             |
|`U+17CB`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CB; Bantoc              |
|`U+17CC`   | Mark [Mn]        | CONSONANT_POSTREPHA| TOP_POSITION              | &#x17CC; Robat               |
|`U+17CD`   | Mark [Mn]        | CONSONANT_KILLER  | TOP_POSITION               | &#x17CD; Toandakhiat         |
|`U+17CE`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CE; Kakabat             |
|`U+17CF`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CF; Ahsda               |
| | | | |																	   
|`U+17D0`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17D0; Samyok Sannya       |
|`U+17D1`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION               | &#x17D1; Viriam              |
|`U+17D2`   | Mark [Mn]        | INVISIBLE_STACKER | _null_                     | &#x17D2; Coeng               |
|`U+17D3`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17D3; Bathamasat          |
|`U+17D4`   | Punctuation      | _null_            | _null_                     | &#x17D4; Khan                |
|`U+17D5`   | Punctuation      | _null_            | _null_                     | &#x17D5; Bariyoosan          |
|`U+17D6`   | Punctuation      | _null_            | _null_                     | &#x17D6; Camnuc Pii Kuuh     |
|`U+17D7`   | Letter           | _null_            | _null_                     | &#x17D7; Lek Too             |
|`U+17D8`   | Punctuation      | _null_            | _null_                     | &#x17D8; Beyyal              |
|`U+17D9`   | Punctuation      | _null_            | _null_                     | &#x17D9; Phnaek Muan         |
|`U+17DA`   | Punctuation      | _null_            | _null_                     | &#x17DA; Koomuut             |
|`U+17DB`   | Symbol           | _null_            | _null_                     | &#x17DB; Riel                |
|`U+17DC`   | Letter           | ANUSVARA          | _null_                     | &#x17DC; Avakrahasanya       |
|`U+17DD`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17DD; Atthacan            |
|`U+17DE`   | _unassigned_     |                   |                            |                              |
|`U+17DF`   | _unassigned_     |                   |                            |                              |
| | | | |																	   	  
|`U+17E0`   | Number           | NUMBER            | _null_                     | &#x17E0; Digit Zero          |
|`U+17E1`   | Number           | NUMBER            | _null_                     | &#x17E1; Digit One           |
|`U+17E2`   | Number           | NUMBER            | _null_                     | &#x17E2; Digit Two           |
|`U+17E3`   | Number           | NUMBER            | _null_                     | &#x17E3; Digit Three         |
|`U+17E4`   | Number           | NUMBER            | _null_                     | &#x17E4; Digit Four          |
|`U+17E5`   | Number           | NUMBER            | _null_                     | &#x17E5; Digit Five          |
|`U+17E6`   | Number           | NUMBER            | _null_                     | &#x17E6; Digit Six           |
|`U+17E7`   | Number           | NUMBER            | _null_                     | &#x17E7; Digit Seven         |
|`U+17E8`   | Number           | NUMBER            | _null_                     | &#x17E8; Digit Eight         |
|`U+17E9`   | Number           | NUMBER            | _null_                     | &#x17E9; Digit Nine          |
|`U+17EA`   | _unassigned_     |                   |                            |                              |
|`U+17EB`   | _unassigned_     |                   |                            |                              |
|`U+17EC`   | _unassigned_     |                   |                            |                              |
|`U+17ED`   | _unassigned_     |                   |                            |                              |
|`U+17EE`   | _unassigned_     |                   |                            |                              |
|`U+17EF`   | _unassigned_     |                   |                            |                              |
| | | | |
|`U+17F0`   | Number           | _null_            | _null_                     | &#x17F0; Lek Attak Son       |
|`U+17F1`   | Number           | _null_            | _null_                     | &#x17F1; Lek Attak Muoy      |
|`U+17F2`   | Number           | _null_            | _null_                     | &#x17F2; Lek Attak Pii       |
|`U+17F3`   | Number           | _null_            | _null_                     | &#x17F3; Lek Attak Bei       |
|`U+17F4`   | Number           | _null_            | _null_                     | &#x17F4; Lek Attak Buon      |
|`U+17F5`   | Number           | _null_            | _null_                     | &#x17F5; Lek Attak Pram      |
|`U+17F6`   | Number           | _null_            | _null_                     | &#x17F6; Lek Attak Pram-Muoy |
|`U+17F7`   | Number           | _null_            | _null_                     | &#x17F7; Lek Attak Pram-Pii  |
|`U+17F8`   | Number           | _null_            | _null_                     | &#x17F8; Lek Attak Pram-Bei  |
|`U+17F9`   | Number           | _null_            | _null_                     | &#x17F9; Lek Attak Pram-Buon |
|`U+17FA`   | _unassigned_     |                   |                            |                              |
|`U+17FB`   | _unassigned_     |                   |                            |                              |
|`U+17FC`   | _unassigned_     |                   |                            |                              |
|`U+17FD`   | _unassigned_     |                   |                            |                              |
|`U+17FE`   | _unassigned_     |                   |                            |                              |
|`U+17FF`   | _unassigned_     |                   |                            |                              |
 

## Vedic Extensions character table ##

Sanskrit runs written in the Khmer script may also include
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
of Khmer text include the dotted-circle placeholder (`U+25CC`), the
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


The zero-width joiner is primarily used to prevent the formation of a
conjunct from a "_consonant_,Halant,_consonant_" sequence. The sequence
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

In addition to general punctuation, runs of Khmer text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.
