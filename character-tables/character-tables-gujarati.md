# Gujarati character tables #

This document lists the per-character shaping information needed to
[shape Gujarati text](/opentype-shaping-gujarati.md).

**Table of Contents**

  - [Gujarati character table](#gujarati-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Gujarati character table ##

Gujarati glyphs should be classified as in the following
table. Codepoints in the Gujarati block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Gujarati block, such as
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
|`U+0A80`   | _unassigned_     |                   |                            |                              |
|`U+0A81`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0A81; Candrabindu         |
|`U+0A82`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0A82; Anusvara            |
|`U+0A83`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0A83; Visarga             |
|`U+0A84`   | _unassigned_     |                   |                            |                              |
|`U+0A85`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A85; A                   |
|`U+0A86`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A86; Aa                  |
|`U+0A87`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A87; I                   |
|`U+0A88`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A88; Ii                  |
|`U+0A89`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A89; U                   |
|`U+0A8A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A8A; Uu                  |
|`U+0A8B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A8B; Vocalic R           |
|`U+0A8C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A8C; Vocalic L           |
|`U+0A8D`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A8D; Candra E            |
|`U+0A8E`   | _unassigned_     |                   |                            |                              |
|`U+0A8F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A8F; E                   |
| | | | |																	   
|`U+0A90`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A90; Ai                  |
|`U+0A91`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A91; Candra O            |
|`U+0A92`   | _unassigned_     |                   |                            |                              |
|`U+0A93`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A93; O                   |
|`U+0A94`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0A94; Au                  |
|`U+0A95`   | Letter           | CONSONANT         | _null_                     | &#x0A95; Ka                  |
|`U+0A96`   | Letter           | CONSONANT         | _null_                     | &#x0A96; Kha                 |
|`U+0A97`   | Letter           | CONSONANT         | _null_                     | &#x0A97; Ga                  |
|`U+0A98`   | Letter           | CONSONANT         | _null_                     | &#x0A98; Gha                 |
|`U+0A99`   | Letter           | CONSONANT         | _null_                     | &#x0A99; Nga                 |
|`U+0A9A`   | Letter           | CONSONANT         | _null_                     | &#x0A9A; Ca                  |
|`U+0A9B`   | Letter           | CONSONANT         | _null_                     | &#x0A9B; Cha                 |
|`U+0A9C`   | Letter           | CONSONANT         | _null_                     | &#x0A9C; Ja                  |
|`U+0A9D`   | Letter           | CONSONANT         | _null_                     | &#x0A9D; Jha                 |
|`U+0A9E`   | Letter           | CONSONANT         | _null_                     | &#x0A9E; Nya                 |
|`U+0A9F`   | Letter           | CONSONANT         | _null_                     | &#x0A9F; Tta                 |
| | | | |																	   
|`U+0AA0`   | Letter           | CONSONANT         | _null_                     | &#x0AA0; Ttha                |
|`U+0AA1`   | Letter           | CONSONANT         | _null_                     | &#x0AA1; Dda                 |
|`U+0AA2`   | Letter           | CONSONANT         | _null_                     | &#x0AA2; Ddha                |
|`U+0AA3`   | Letter           | CONSONANT         | _null_                     | &#x0AA3; Nna                 |
|`U+0AA4`   | Letter           | CONSONANT         | _null_                     | &#x0AA4; Ta                  |
|`U+0AA5`   | Letter           | CONSONANT         | _null_                     | &#x0AA5; Tha                 |
|`U+0AA6`   | Letter           | CONSONANT         | _null_                     | &#x0AA6; Da                  |
|`U+0AA7`   | Letter           | CONSONANT         | _null_                     | &#x0AA7; Dha                 |
|`U+0AA8`   | Letter           | CONSONANT         | _null_                     | &#x0AA8; Na                  |
|`U+0AA9`   | _unassigned_     |                   |                            |                              |
|`U+0AAA`   | Letter           | CONSONANT         | _null_                     | &#x0AAA; Pa                  |
|`U+0AAB`   | Letter           | CONSONANT         | _null_                     | &#x0AAB; Pha                 |
|`U+0AAC`   | Letter           | CONSONANT         | _null_                     | &#x0AAC; Ba                  |
|`U+0AAD`   | Letter           | CONSONANT         | _null_                     | &#x0AAD; Bha                 |
|`U+0AAE`   | Letter           | CONSONANT         | _null_                     | &#x0AAE; Ma                  |
|`U+0AAF`   | Letter           | CONSONANT         | _null_                     | &#x0AAF; Ya                  |
| | | | |																	    
|`U+0AB0`   | Letter           | CONSONANT         | _null_                     | &#x0AB0; Ra                  |
|`U+0AB1`   | _unassigned_     |                   |                            |                              |
|`U+0AB2`   | Letter           | CONSONANT         | _null_                     | &#x0AB2; La                  |
|`U+0AB3`   | Letter           | CONSONANT         | _null_                     | &#x0AB3; Lla                 |
|`U+0AB4`   | _unassigned_     |                   |                            |                              |
|`U+0AB5`   | Letter           | CONSONANT         | _null_                     | &#x0AB5; Va                  |
|`U+0AB6`   | Letter           | CONSONANT         | _null_                     | &#x0AB6; Sha                 |
|`U+0AB7`   | Letter           | CONSONANT         | _null_                     | &#x0AB7; Ssa                 |
|`U+0AB8`   | Letter           | CONSONANT         | _null_                     | &#x0AB8; Sa                  |
|`U+0AB9`   | Letter           | CONSONANT         | _null_                     | &#x0AB9; Ha                  |
|`U+0ABA`   | _unassigned_     |                   |                            |                              |
|`U+0ABB`   | _unassigned_     |                   |                            |                              |
|`U+0ABC`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x0ABC; Nukta               |
|`U+0ABD`   | Letter           | AVAGRAHA          | _null_                     | &#x0ABD; Avagraha            |
|`U+0ABE`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0ABE; Sign Aa             |
|`U+0ABF`   | Mark [Mc]        | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x0ABF; Sign I              |
| | | | |																	   
|`U+0AC0`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0AC0; Sign Ii             |
|`U+0AC1`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AC1; Sign U              |
|`U+0AC2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AC2; Sign Uu             |
|`U+0AC3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AC3; Sign Vocalic R      |
|`U+0AC4`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AC4; Sign Vocalic Rr     |
|`U+0AC5`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0AC5; Sign Candra E       |
|`U+0AC6`   | _unassigned_     |                   |                            |                              |
|`U+0AC7`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0AC7; Sign E              |
|`U+0AC8`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0AC8; Sign Ai             |
|`U+0AC9`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0AC9; Sign Candra O       |
|`U+0ACA`   | _unassigned_     |                   |                            |                              |
|`U+0ACB`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0ACB; Sign O              |
|`U+0ACC`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0ACC; Sign Au             |
|`U+0ACD`   | Mark [Mn]        | VIRAMA            | BOTTOM_POSITION            | &#x0ACD; Virama              |
|`U+0ACE`   | _unassigned_     |                   |                            |                              |
|`U+0ACF`   | _unassigned_     |                   |                            |                              |
| | | | |																	   
|`U+0AD0`   | Letter           | _null_            | _null_                     | &#x0AD0; Om                  |
|`U+0AD1`   | _unassigned_     |                   |                            |                              |
|`U+0AD2`   | _unassigned_     |                   |                            |                              |
|`U+0AD3`   | _unassigned_     |                   |                            |                              |
|`U+0AD4`   | _unassigned_     |                   |                            |                              |
|`U+0AD5`   | _unassigned_     |                   |                            |                              |
|`U+0AD6`   | _unassigned_     |                   |                            |                              |
|`U+0AD7`   | _unassigned_     |                   |                            |                              |
|`U+0AD8`   | _unassigned_     |                   |                            |                              |
|`U+0AD9`   | _unassigned_     |                   |                            |                              |
|`U+0ADA`   | _unassigned_     |                   |                            |                              |
|`U+0ADB`   | _unassigned_     |                   |                            |                              |
|`U+0ADC`   | _unassigned_     |                   |                            |                              |
|`U+0ADD`   | _unassigned_     |                   |                            |                              |
|`U+0ADE`   | _unassigned_     |                   |                            |                              |
|`U+0ADF`   | _unassigned_     |                   |                            |                              |
| | | | |																	   
|`U+0AE0`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0AE0; Vocalic Rr          |
|`U+0AE1`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0AE1; Vocalic Ll          |
|`U+0AE2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AE2; Sign Vocalic L      |
|`U+0AE3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0AE3; Sign Vocalic Ll     |
|`U+0AE4`   | _unassigned_     |                   |                            |                              |
|`U+0AE5`   | _unassigned_     |                   |                            |                              |
|`U+0AE6`   | Number           | NUMBER            | _null_                     | &#x0AE6; Digit Zero          |
|`U+0AE7`   | Number           | NUMBER            | _null_                     | &#x0AE7; Digit One           |
|`U+0AE8`   | Number           | NUMBER            | _null_                     | &#x0AE8; Digit Two           |
|`U+0AE9`   | Number           | NUMBER            | _null_                     | &#x0AE9; Digit Three         |
|`U+0AEA`   | Number           | NUMBER            | _null_                     | &#x0AEA; Digit Four          |
|`U+0AEB`   | Number           | NUMBER            | _null_                     | &#x0AEB; Digit Five          |
|`U+0AEC`   | Number           | NUMBER            | _null_                     | &#x0AEC; Digit Six           |
|`U+0AED`   | Number           | NUMBER            | _null_                     | &#x0AED; Digit Seven         |
|`U+0AEE`   | Number           | NUMBER            | _null_                     | &#x0AEE; Digit Eight         |
|`U+0AEF`   | Number           | NUMBER            | _null_                     | &#x0AEF; Digit Nine          |
| | | | |
|`U+0AF0`   | Symbol           | _null_            | _null_                     | &#x0AF0; Abbreviation        |
|`U+0AF1`   | Symbol           | _null_            | _null_                     | &#x0AF1; Rupee Sign          |
|`U+0AF2`   | _unassigned_     |                   |                            |                              |
|`U+0AF3`   | _unassigned_     |                   |                            |                              |
|`U+0AF4`   | _unassigned_     |                   |                            |                              |
|`U+0AF5`   | _unassigned_     |                   |                            |                              |
|`U+0AF6`   | _unassigned_     |                   |                            |                              |
|`U+0AF7`   | _unassigned_     |                   |                            |                              |
|`U+0AF8`   | _unassigned_     |                   |                            |                              |
|`U+0AF9`   | Letter           | CONSONANT         | _null_                     | &#x0AF9; Zha                 |
|`U+0AFA`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0AFA; Sukun               |
|`U+0AFB`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0AFB; Shadda              |
|`U+0AFC`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0AFC; Maddah              |
|`U+0AFD`   | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x0AFD; Three-Dot Nukta Above|
|`U+0AFE`   | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x0AFE; Circle Nukta Above  |
|`U+0AFF`   | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x0AFF; Two-Circle Nukta Above|
 

## Vedic Extensions character table ##

Sanskrit runs written in the Gujarati script may also include
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
of Gujarati text include the dotted-circle placeholder (`U+25CC`), the
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

In addition to general punctuation, runs of Gujarati text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.
