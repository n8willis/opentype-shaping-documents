# Telugu character tables #

This document lists the per-character shaping information needed to
[shape Telugu text](/opentype-shaping-telugu.md).

**Table of Contents**

  - [Telugu character table](#telugu-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Telugu character table ##

Telugu glyphs should be classified as in the following
table. Codepoints in the Telugu block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Telugu block, such as
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
|`U+0C00`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0C00; Combining Candrabindu Above |
|`U+0C01`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0C01; Candrabindu         |
|`U+0C02`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0C02; Anusvara            |
|`U+0C03`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0C03; Visarga             |
|`U+0C04`   | _unassigned_     |                   |                            |                              |
|`U+0C05`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C05; A                   |
|`U+0C06`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C06; Aa                  |
|`U+0C07`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C07; I                   |
|`U+0C08`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C08; Ii                  |
|`U+0C09`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C09; U                   |
|`U+0C0A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C0A; Uu                  |
|`U+0C0B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C0B; Vocalic R           |
|`U+0C0C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C0C; Vocalic L           |
|`U+0C0D`   | _unassigned_     |                   |                            |                              |
|`U+0C0E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C0E; E                   |
|`U+0C0F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C0F; Ee                  |
| | | | |																		
|`U+0C10`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C10; Ai                  |
|`U+0C11`   | _unassigned_     |                   |                            |                              |
|`U+0C12`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C12; O                   |
|`U+0C13`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C13; Oo                  |
|`U+0C14`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C14; Au                  |
|`U+0C15`   | Letter           | CONSONANT         | _null_                     | &#x0C15; Ka                  |
|`U+0C16`   | Letter           | CONSONANT         | _null_                     | &#x0C16; Kha                 |
|`U+0C17`   | Letter           | CONSONANT         | _null_                     | &#x0C17; Ga                  |
|`U+0C18`   | Letter           | CONSONANT         | _null_                     | &#x0C18; Gha                 |
|`U+0C19`   | Letter           | CONSONANT         | _null_                     | &#x0C19; Nga                 |
|`U+0C1A`   | Letter           | CONSONANT         | _null_                     | &#x0C1A; Ca                  |
|`U+0C1B`   | Letter           | CONSONANT         | _null_                     | &#x0C1B; Cha                 |
|`U+0C1C`   | Letter           | CONSONANT         | _null_                     | &#x0C1C; Ja                  |
|`U+0C1D`   | Letter           | CONSONANT         | _null_                     | &#x0C1D; Jha                 |
|`U+0C1E`   | Letter           | CONSONANT         | _null_                     | &#x0C1E; Nya                 |
|`U+0C1F`   | Letter           | CONSONANT         | _null_                     | &#x0C1F; Tta                 |
| | | | |																		
|`U+0C20`   | Letter           | CONSONANT         | _null_                     | &#x0C20; Ttha                |
|`U+0C21`   | Letter           | CONSONANT         | _null_                     | &#x0C21; Dda                 |
|`U+0C22`   | Letter           | CONSONANT         | _null_                     | &#x0C22; Ddha                |
|`U+0C23`   | Letter           | CONSONANT         | _null_                     | &#x0C23; Nna                 |
|`U+0C24`   | Letter           | CONSONANT         | _null_                     | &#x0C24; Ta                  |
|`U+0C25`   | Letter           | CONSONANT         | _null_                     | &#x0C25; Tha                 |
|`U+0C26`   | Letter           | CONSONANT         | _null_                     | &#x0C26; Da                  |
|`U+0C27`   | Letter           | CONSONANT         | _null_                     | &#x0C27; Dha                 |
|`U+0C28`   | Letter           | CONSONANT         | _null_                     | &#x0C28; Na                  |
|`U+0C29`   | _unassigned_     |                   |                            |                              |
|`U+0C2A`   | Letter           | CONSONANT         | _null_                     | &#x0C2A; Pa                  |
|`U+0C2B`   | Letter           | CONSONANT         | _null_                     | &#x0C2B; Pha                 |
|`U+0C2C`   | Letter           | CONSONANT         | _null_                     | &#x0C2C; Ba                  |
|`U+0C2D`   | Letter           | CONSONANT         | _null_                     | &#x0C2D; Bha                 |
|`U+0C2E`   | Letter           | CONSONANT         | _null_                     | &#x0C2E; Ma                  |
|`U+0C2F`   | Letter           | CONSONANT         | _null_                     | &#x0C2F; Ya                  |
| | | | |																		
|`U+0C30`   | Letter           | CONSONANT         | _null_                     | &#x0C30; Ra                  |
|`U+0C31`   | Letter           | CONSONANT         | _null_                     | &#x0C31; Rra                 |
|`U+0C32`   | Letter           | CONSONANT         | _null_                     | &#x0C32; La                  |
|`U+0C33`   | Letter           | CONSONANT         | _null_                     | &#x0C33; Lla                 |
|`U+0C34`   | Letter           | CONSONANT         | _null_                     | &#x0C34; Llla                |
|`U+0C35`   | Letter           | CONSONANT         | _null_                     | &#x0C35; Va                  |
|`U+0C36`   | Letter           | CONSONANT         | _null_                     | &#x0C36; Sha                 |
|`U+0C37`   | Letter           | CONSONANT         | _null_                     | &#x0C37; Ssa                 |
|`U+0C38`   | Letter           | CONSONANT         | _null_                     | &#x0C38; Sa                  |
|`U+0C39`   | Letter           | CONSONANT         | _null_                     | &#x0C39; Ha                  |
|`U+0C3A`   | _unassigned_     |                   |                            |                              |
|`U+0C3B`   | _unassigned_     |                   |                            |                              |
|`U+0C3C`   | _unassigned_     |                   |                            |                              |
|`U+0C3D`   | Letter           | AVAGRAHA          | _null_                     | &#x0C3D; Avagraha            |
|`U+0C3E`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C3E; Sign Aa             |
|`U+0C3F`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C3F; Sign I              |
| | | | |																		
|`U+0C40`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C40; Sign Ii             |
|`U+0C41`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0C41; Sign U              |
|`U+0C42`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0C42; Sign Uu             |
|`U+0C43`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0C43; Sign Vocalic R      |
|`U+0C44`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0C44; Sign Vocalic Rr     |
|`U+0C45`   | _unassigned_     |                   |                            |                              |
|`U+0C46`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C46; Sign E              |
|`U+0C47`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C47; Sign Ee             |
|`U+0C48`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_AND_BOTTOM_POSITION    | &#x0C48; Sign Ai             |
|`U+0C49`   | _unassigned_     |                   |                            |                              |
|`U+0C4A`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C4A; Sign O              |
|`U+0C4B`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C4B; Sign Oo             |
|`U+0C4C`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C4C; Sign Au             |
|`U+0C4D`   | Mark [Mn]        | VIRAMA            | TOP_POSITION               | &#x0C4D; Virama              |
|`U+0C4E`   | _unassigned_     |                   |                            |                              |
|`U+0C4F`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0C50`   | _unassigned_     |                   |                            |                              |
|`U+0C51`   | _unassigned_     |                   |                            |                              |
|`U+0C52`   | _unassigned_     |                   |                            |                              |
|`U+0C53`   | _unassigned_     |                   |                            |                              |
|`U+0C54`   | _unassigned_     |                   |                            |                              |
|`U+0C55`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0C55; Length Mark         |
|`U+0C56`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0C56; Ai Length Mark      |
|`U+0C57`   | _unassigned_     |                   |                            |                              |
|`U+0C58`   | Letter           | CONSONANT         | _null_                     | &#x0C58; Tsa                 |
|`U+0C59`   | Letter           | CONSONANT         | _null_                     | &#x0C59; Dza                 |
|`U+0C5A`   | Letter           | CONSONANT         | _null_                     | &#x0C5A; Rrra                |
|`U+0C5B`   | _unassigned_     |                   |                            |                              |
|`U+0C5C`   | _unassigned_     |                   |                            |                              |
|`U+0C5D`   | _unassigned_     |                   |                            |                              |
|`U+0C5E`   | _unassigned_     |                   |                            |                              |
|`U+0C5F`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0C60`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C60; Vocalic Rr          |
|`U+0C61`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C61; Vocalic Ll          |
|`U+0C62`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0C62; Sign Vocalic L      |
|`U+0C63`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0C63; Sign Vocalic Ll     |
|`U+0C64`   | _unassigned_     |                   |                            |                              |
|`U+0C65`   | _unassigned_     |                   |                            |                              |
|`U+0C66`   | Number           | NUMBER            | _null_                     | &#x0C66; Digit Zero          |
|`U+0C67`   | Number           | NUMBER            | _null_                     | &#x0C67; Digit One           |
|`U+0C68`   | Number           | NUMBER            | _null_                     | &#x0C68; Digit Two           |
|`U+0C69`   | Number           | NUMBER            | _null_                     | &#x0C69; Digit Three         |
|`U+0C6A`   | Number           | NUMBER            | _null_                     | &#x0C6A; Digit Four          |
|`U+0C6B`   | Number           | NUMBER            | _null_                     | &#x0C6B; Digit Five          |
|`U+0C6C`   | Number           | NUMBER            | _null_                     | &#x0C6C; Digit Six           |
|`U+0C6D`   | Number           | NUMBER            | _null_                     | &#x0C6D; Digit Seven         |
|`U+0C6E`   | Number           | NUMBER            | _null_                     | &#x0C6E; Digit Eight         |
|`U+0C6F`   | Number           | NUMBER            | _null_                     | &#x0C6F; Digit Nine          |
| | | | |																		
|`U+0C70`   | _unassigned_     |                   |                            |                              |
|`U+0C71`   | _unassigned_     |                   |                            |                              |
|`U+0C72`   | _unassigned_     |                   |                            |                              |
|`U+0C73`   | _unassigned_     |                   |                            |                              |
|`U+0C74`   | _unassigned_     |                   |                            |                              |
|`U+0C75`   | _unassigned_     |                   |                            |                              |
|`U+0C76`   | _unassigned_     |                   |                            |                              |
|`U+0C77`   | _unassigned_     |                   |                            |                              |
|`U+0C78`   | Number           | NUMBER            | _null_                     | &#x0C78; Fraction Zero Odd P |
|`U+0C79`   | Number           | NUMBER            | _null_                     | &#x0C79; Fraction One Odd P  |
|`U+0C7A`   | Number           | NUMBER            | _null_                     | &#x0C7A; Fraction Two Odd P  |
|`U+0C7B`   | Number           | NUMBER            | _null_                     | &#x0C7B; Fraction Three Odd P|
|`U+0C7C`   | Number           | NUMBER            | _null_                     | &#x0C7C; Fraction One Even P |
|`U+0C7D`   | Number           | NUMBER            | _null_                     | &#x0C7D; Fraction Two Even P |
|`U+0C7E`   | Number           | NUMBER            | _null_                     | &#x0C7E; Fraction Three Even P|
|`U+0C7F`   | Symbol           | _null_            | _null_                     | &#x0C7F; Tuumu               |



## Vedic Extensions character table ##

Sanskrit runs written in the Telugu script may also include
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
of Telugu text include the dotted-circle placeholder (`U+25CC`), the
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

