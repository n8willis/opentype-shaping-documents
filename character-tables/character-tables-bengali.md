# Bengali character tables #

This document lists the per-character shaping information needed to
[shape Bengali text](../opentype-shaping-bengali.md).

**Table of Contents**

  - [Bengali character table](#bengali-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Bengali character table ##

Bengali glyphs should be classified as in the following
table. Codepoints in the Bengali block with no assigned meaning are
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
|`U+0980`   | Letter           | _null_            | _null_                     | &#x0980; Anji                |
|`U+0981`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0981; Candrabindu         |
|`U+0982`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0982; Anusvara            |
|`U+0983`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0983; Visarga             |
|`U+0984`   | _unassigned_     |                   |                            |                              |
|`U+0985`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0985; A                   |
|`U+0986`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0986; Aa                  |
|`U+0987`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0987; I                   |
|`U+0988`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0988; Ii                  |
|`U+0989`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0989; U                   |
|`U+098A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098A; Uu                  |
|`U+098B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098B; Vocalic R           |
|`U+098C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098C; Vocalic L           |
|`U+098D`   | _unassigned_     |                   |                            |                              |
|`U+098E`   | _unassigned_     |                   |                            |                              |
|`U+098F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x098F; E                   |
| | | | |																	   
|`U+0990`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0990; Ai                  |
|`U+0991`   | _unassigned_     |                   |                            |                              |
|`U+0992`   | _unassigned_     |                   |                            |                              |
|`U+0993`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0993; O                   |
|`U+0994`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0994; Au                  |
|`U+0995`   | Letter           | CONSONANT         | _null_                     | &#x0995; Ka                  |
|`U+0996`   | Letter           | CONSONANT         | _null_                     | &#x0996; Kha                 |
|`U+0997`   | Letter           | CONSONANT         | _null_                     | &#x0997; Ga                  |
|`U+0998`   | Letter           | CONSONANT         | _null_                     | &#x0998; Gha                 |
|`U+0999`   | Letter           | CONSONANT         | _null_                     | &#x0999; Nga                 |
|`U+099A`   | Letter           | CONSONANT         | _null_                     | &#x099A; Ca                  |
|`U+099B`   | Letter           | CONSONANT         | _null_                     | &#x099B; Cha                 |
|`U+099C`   | Letter           | CONSONANT         | _null_                     | &#x099C; Ja                  |
|`U+099D`   | Letter           | CONSONANT         | _null_                     | &#x099D; Jha                 |
|`U+099E`   | Letter           | CONSONANT         | _null_                     | &#x099E; Nya                 |
|`U+099F`   | Letter           | CONSONANT         | _null_                     | &#x099F; Tta                 |
| | | | |																	   
|`U+09A0`   | Letter           | CONSONANT         | _null_                     | &#x09A0; Ttha                |
|`U+09A1`   | Letter           | CONSONANT         | _null_                     | &#x09A1; Dda                 |
|`U+09A2`   | Letter           | CONSONANT         | _null_                     | &#x09A2; Ddha                |
|`U+09A3`   | Letter           | CONSONANT         | _null_                     | &#x09A3; Nna                 |
|`U+09A4`   | Letter           | CONSONANT         | _null_                     | &#x09A4; Ta                  |
|`U+09A5`   | Letter           | CONSONANT         | _null_                     | &#x09A5; Tha                 |
|`U+09A6`   | Letter           | CONSONANT         | _null_                     | &#x09A6; Da                  |
|`U+09A7`   | Letter           | CONSONANT         | _null_                     | &#x09A7; Dha                 |
|`U+09A8`   | Letter           | CONSONANT         | _null_                     | &#x09A8; Na                  |
|`U+09A9`   | _unassigned_     |                   |                            |                              |
|`U+09AA`   | Letter           | CONSONANT         | _null_                     | &#x09AA; Pa                  |
|`U+09AB`   | Letter           | CONSONANT         | _null_                     | &#x09AB; Pha                 |
|`U+09AC`   | Letter           | CONSONANT         | _null_                     | &#x09AC; Ba                  |
|`U+09AD`   | Letter           | CONSONANT         | _null_                     | &#x09AD; Bha                 |
|`U+09AE`   | Letter           | CONSONANT         | _null_                     | &#x09AE; Ma                  |
|`U+09AF`   | Letter           | CONSONANT         | _null_                     | &#x09AF; Ya                  |
| | | | |																	    
|`U+09B0`   | Letter           | CONSONANT         | _null_                     | &#x09B0; Ra                  |
|`U+09B1`   | _unassigned_     |                   |                            |                              |
|`U+09B2`   | Letter           | CONSONANT         | _null_                     | &#x09B2; La                  |
|`U+09B3`   | _unassigned_     |                   |                            |                              |
|`U+09B4`   | _unassigned_     |                   |                            |                              |
|`U+09B5`   | _unassigned_     |                   |                            |                              |
|`U+09B6`   | Letter           | CONSONANT         | _null_                     | &#x09B6; Sha                 |
|`U+09B7`   | Letter           | CONSONANT         | _null_                     | &#x09B7; Ssa                 |
|`U+09B8`   | Letter           | CONSONANT         | _null_                     | &#x09B8; Sa                  |
|`U+09B9`   | Letter           | CONSONANT         | _null_                     | &#x09B9; Ha                  |
|`U+09BA`   | _unassigned_     |                   |                            |                              |
|`U+09BB`   | _unassigned_     |                   |                            |                              |
|`U+09BC`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x09BC; Nukta               |
|`U+09BD`   | Letter           | AVAGRAHA          | _null_                     | &#x09BD; Avagraha            |
|`U+09BE`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09BE; Sign Aa             |
|`U+09BF`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09BF; Sign I              |
| | | | |																	   
|`U+09C0`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09C0; Sign Ii             |
|`U+09C1`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C1; Sign U              |
|`U+09C2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C2; Sign Uu             |
|`U+09C3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C3; Sign Vocalic R      |
|`U+09C4`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C4; Sign Vocalic Rr     |
|`U+09C5`   | _unassigned_     |                   |                            |                              |
|`U+09C6`   | _unassigned_     |                   |                            |                              |
|`U+09C7`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C7; Sign E              |
|`U+09C8`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C8; Sign Ai             |
|`U+09C9`   | _unassigned_     |                   |                            |                              |
|`U+09CA`   | _unassigned_     |                   |                            |                              |
|`U+09CB`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CB; Sign O              |
|`U+09CC`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CC; Sign Au             |
|`U+09CD`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x09CD; Virama              |
|`U+09CE`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x09CE; Khanda Ta           |
|`U+09CF`   | _unassigned_     |                   |                            |                              |
| | | | |																	   
|`U+09D0`   | _unassigned_     |                   |                            |                              |
|`U+09D1`   | _unassigned_     |                   |                            |                              |
|`U+09D2`   | _unassigned_     |                   |                            |                              |
|`U+09D3`   | _unassigned_     |                   |                            |                              |
|`U+09D4`   | _unassigned_     |                   |                            |                              |
|`U+09D5`   | _unassigned_     |                   |                            |                              |
|`U+09D6`   | _unassigned_     |                   |                            |                              |
|`U+09D7`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09D7; Au Length Mark      |
|`U+09D8`   | _unassigned_     |                   |                            |                              |
|`U+09D9`   | _unassigned_     |                   |                            |                              |
|`U+09DA`   | _unassigned_     |                   |                            |                              |
|`U+09DB`   | _unassigned_     |                   |                            |                              |
|`U+09DC`   | Letter           | CONSONANT         | _null_                     | &#x09DC; Rra                 |
|`U+09DD`   | Letter           | CONSONANT         | _null_                     | &#x09DD; Rha                 |
|`U+09DE`   | _unassigned_     |                   |                            |                              |
|`U+09DF`   | Letter           | CONSONANT         | _null_                     | &#x09DF; Yya                 |
| | | | |																	   
|`U+09E0`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x09E0; Vocalic Rr          |
|`U+09E1`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x09E1; Vocalic Ll          |
|`U+09E2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E2; Sign Vocalic L      |
|`U+09E3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E3; Sign Vocalic Ll     |
|`U+09E4`   | _unassigned_     |                   |                            |                              |
|`U+09E5`   | _unassigned_     |                   |                            |                              |
|`U+09E6`   | Number           | NUMBER            | _null_                     | &#x09E6; Digit Zero          |
|`U+09E7`   | Number           | NUMBER            | _null_                     | &#x09E7; Digit One           |
|`U+09E8`   | Number           | NUMBER            | _null_                     | &#x09E8; Digit Two           |
|`U+09E9`   | Number           | NUMBER            | _null_                     | &#x09E9; Digit Three         |
|`U+09EA`   | Number           | NUMBER            | _null_                     | &#x09EA; Digit Four          |
|`U+09EB`   | Number           | NUMBER            | _null_                     | &#x09EB; Digit Five          |
|`U+09EC`   | Number           | NUMBER            | _null_                     | &#x09EC; Digit Six           |
|`U+09ED`   | Number           | NUMBER            | _null_                     | &#x09ED; Digit Seven         |
|`U+09EE`   | Number           | NUMBER            | _null_                     | &#x09EE; Digit Eight         |
|`U+09EF`   | Number           | NUMBER            | _null_                     | &#x09EF; Digit Nine          |
| | | | |
|`U+09F0`   | Letter           | CONSONANT         | _null_                     | &#x09F0; Assamese Ra         |
|`U+09F1`   | Letter           | CONSONANT         | _null_                     | &#x09F1; Assamese Wa         |
|`U+09F2`   | Symbol           | SYMBOL            | _null_                     | &#x09F2; Rupee Mark          |
|`U+09F3`   | Symbol           | SYMBOL            | _null_                     | &#x09F3; Rupee Sign          |
|`U+09F4`   | Number           | NUMBER            | _null_                     | &#x09F4; Numerator One       |
|`U+09F5`   | Number           | NUMBER            | _null_                     | &#x09F5; Numerator Two       |
|`U+09F6`   | Number           | NUMBER            | _null_                     | &#x09F6; Numerator Three     |
|`U+09F7`   | Number           | NUMBER            | _null_                     | &#x09F7; Numerator Four      |
|`U+09F8`   | Number           | NUMBER            | _null_                     | &#x09F8; Numerator One Less Than Denominator |
|`U+09F9`   | Number           | NUMBER            | _null_                     | &#x09F9; Denominator Sixteen |
|`U+09FA`   | Symbol           | SYMBOL            | _null_                     | &#x09FA; Isshar              |
|`U+09FB`   | Symbol           | SYMBOL            | _null_                     | &#x09FB; Ganda Mark          |
|`U+09FC`   | Letter           | _null_            | _null_                     | &#x09FC; Vedic Anusvara      |
|`U+09FD`   | Punctuation      | _null_            | _null_                     | &#x09FD; Abbreviation Sign   |
|`U+09FE`   | _unassigned_     |                   |                            |                              |
|`U+09FF`   | _unassigned_     |                   |                            |                              |
 

## Vedic Extensions character table ##

Sanskrit runs written in the Bengali script may also include
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

In addition to general punctuation, runs of Bengali text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Bengali text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |


Other important characters that may be encountered when shaping runs
of Bengali text include the dotted-circle placeholder (`U+25CC`), the
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
conjunct from a "_Consonant_,Halant,_Consonant_" sequence. The sequence
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

