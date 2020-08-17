# Kannada character tables #

This document lists the per-character shaping information needed to
[shape Kannada text](../opentype-shaping-kannada.md).

**Table of Contents**

  - [Kannada character table](#kannada-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Kannada character table ##

Kannada glyphs should be classified as in the following
table. Codepoints in the Kannada block with no assigned meaning are
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
|`U+0C80`   | Letter           | PLACEHOLDER       | _null_                     | &#x0C80; Spacing Candrabindu |
|`U+0C81`   | Mark [Mn]        | BINDU             | TOP_POSITION               | &#x0C81; Candrabindu         |
|`U+0C82`   | Mark [Mc]        | BINDU             | RIGHT_POSITION             | &#x0C82; Anusvara            |
|`U+0C83`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x0C83; Visarga             |
|`U+0C84`   | Punctuation      | _null_            | _null_                     | &#x0C84; Siddham             |
|`U+0C85`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C85; A                   |
|`U+0C86`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C86; Aa                  |
|`U+0C87`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C87; I                   |
|`U+0C88`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C88; Ii                  |
|`U+0C89`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C89; U                   |
|`U+0C8A`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C8A; Uu                  |
|`U+0C8B`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C8B; Vocalic R           |
|`U+0C8C`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C8C; Vocalic L           |
|`U+0C8D`   | _unassigned_     |                   |                            |                              |
|`U+0C8E`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C8E; E                   |
|`U+0C8F`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C8F; Ee                  |
| | | | |																		
|`U+0C90`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C90; Ai                  |
|`U+0C91`   | _unassigned_     |                   |                            |                              |
|`U+0C92`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C92; O                   |
|`U+0C93`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C93; Oo                  |
|`U+0C94`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0C94; Au                  |
|`U+0C95`   | Letter           | CONSONANT         | _null_                     | &#x0C95; Ka                  |
|`U+0C96`   | Letter           | CONSONANT         | _null_                     | &#x0C96; Kha                 |
|`U+0C97`   | Letter           | CONSONANT         | _null_                     | &#x0C97; Ga                  |
|`U+0C98`   | Letter           | CONSONANT         | _null_                     | &#x0C98; Gha                 |
|`U+0C99`   | Letter           | CONSONANT         | _null_                     | &#x0C99; Nga                 |
|`U+0C9A`   | Letter           | CONSONANT         | _null_                     | &#x0C9A; Ca                  |
|`U+0C9B`   | Letter           | CONSONANT         | _null_                     | &#x0C9B; Cha                 |
|`U+0C9C`   | Letter           | CONSONANT         | _null_                     | &#x0C9C; Ja                  |
|`U+0C9D`   | Letter           | CONSONANT         | _null_                     | &#x0C9D; Jha                 |
|`U+0C9E`   | Letter           | CONSONANT         | _null_                     | &#x0C9E; Nya                 |
|`U+0C9F`   | Letter           | CONSONANT         | _null_                     | &#x0C9F; Tta                 |
| | | | |																		
|`U+0CA0`   | Letter           | CONSONANT         | _null_                     | &#x0CA0; Ttha                |
|`U+0CA1`   | Letter           | CONSONANT         | _null_                     | &#x0CA1; Dda                 |
|`U+0CA2`   | Letter           | CONSONANT         | _null_                     | &#x0CA2; Ddha                |
|`U+0CA3`   | Letter           | CONSONANT         | _null_                     | &#x0CA3; Nna                 |
|`U+0CA4`   | Letter           | CONSONANT         | _null_                     | &#x0CA4; Ta                  |
|`U+0CA5`   | Letter           | CONSONANT         | _null_                     | &#x0CA5; Tha                 |
|`U+0CA6`   | Letter           | CONSONANT         | _null_                     | &#x0CA6; Da                  |
|`U+0CA7`   | Letter           | CONSONANT         | _null_                     | &#x0CA7; Dha                 |
|`U+0CA8`   | Letter           | CONSONANT         | _null_                     | &#x0CA8; Na                  |
|`U+0CA9`   | _unassigned_     |                   |                            |                              |
|`U+0CAA`   | Letter           | CONSONANT         | _null_                     | &#x0CAA; Pa                  |
|`U+0CAB`   | Letter           | CONSONANT         | _null_                     | &#x0CAB; Pha                 |
|`U+0CAC`   | Letter           | CONSONANT         | _null_                     | &#x0CAC; Ba                  |
|`U+0CAD`   | Letter           | CONSONANT         | _null_                     | &#x0CAD; Bha                 |
|`U+0CAE`   | Letter           | CONSONANT         | _null_                     | &#x0CAE; Ma                  |
|`U+0CAF`   | Letter           | CONSONANT         | _null_                     | &#x0CAF; Ya                  |
| | | | |																		
|`U+0CB0`   | Letter           | CONSONANT         | _null_                     | &#x0CB0; Ra                  |
|`U+0CB1`   | Letter           | CONSONANT         | _null_                     | &#x0CB1; Rra                 |
|`U+0CB2`   | Letter           | CONSONANT         | _null_                     | &#x0CB2; La                  |
|`U+0CB3`   | Letter           | CONSONANT         | _null_                     | &#x0CB3; Lla                 |
|`U+0CB4`   | _unassigned_     |                   |                            |                              |
|`U+0CB5`   | Letter           | CONSONANT         | _null_                     | &#x0CB5; Va                  |
|`U+0CB6`   | Letter           | CONSONANT         | _null_                     | &#x0CB6; Sha                 |
|`U+0CB7`   | Letter           | CONSONANT         | _null_                     | &#x0CB7; Ssa                 |
|`U+0CB8`   | Letter           | CONSONANT         | _null_                     | &#x0CB8; Sa                  |
|`U+0CB9`   | Letter           | CONSONANT         | _null_                     | &#x0CB9; Ha                  |
|`U+0CBA`   | _unassigned_     |                   |                            |                              |
|`U+0CBB`   | _unassigned_     |                   |                            |                              |
|`U+0CBC`   | Mark [Mn]        | NUKTA             | BOTTOM_POSITION            | &#x0CBC; Nukta               |
|`U+0CBD`   | Letter           | AVAGRAHA          | _null_                     | &#x0CBD; Avagraha            |
|`U+0CBE`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CBE; Sign Aa             |
|`U+0CBF`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0CBF; Sign I              |
| | | | |																		
|`U+0CC0`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0CC0; Sign Ii             |
|`U+0CC1`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CC1; Sign U              |
|`U+0CC2`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CC2; Sign Uu             |
|`U+0CC3`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CC3; Sign Vocalic R      |
|`U+0CC4`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CC4; Sign Vocalic Rr     |
|`U+0CC5`   | _unassigned_     |                   |                            |                              |
|`U+0CC6`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0CC6; Sign E              |
|`U+0CC7`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0CC7; Sign Ee             |
|`U+0CC8`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0CC8; Sign Ai             |
|`U+0CC9`   | _unassigned_     |                   |                            |                              |
|`U+0CCA`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0CCA; Sign O              |
|`U+0CCB`   | Mark [Mc]        | VOWEL_DEPENDENT   | TOP_AND_RIGHT_POSITION     | &#x0CCB; Sign Oo             |
|`U+0CCC`   | Mark [Mn]        | VOWEL_DEPENDENT   | TOP_POSITION               | &#x0CCC; Sign Au             |
|`U+0CCD`   | Mark [Mn]        | VIRAMA            | TOP_POSITION               | &#x0CCD; Virama              |
|`U+0CCE`   | _unassigned_     |                   |                            |                              |
|`U+0CCF`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0CD0`   | _unassigned_     |                   |                            |                              |
|`U+0CD1`   | _unassigned_     |                   |                            |                              |
|`U+0CD2`   | _unassigned_     |                   |                            |                              |
|`U+0CD3`   | _unassigned_     |                   |                            |                              |
|`U+0CD4`   | _unassigned_     |                   |                            |                              |
|`U+0CD5`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CD5; Length Mark         |
|`U+0CD6`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x0CD6; Ai Length Mark      |
|`U+0CD7`   | _unassigned_     |                   |                            |                              |
|`U+0CD8`   | _unassigned_     |                   |                            |                              |
|`U+0CD9`   | _unassigned_     |                   |                            |                              |
|`U+0CDA`   | _unassigned_     |                   |                            |                              |
|`U+0CDB`   | _unassigned_     |                   |                            |                              |
|`U+0CDC`   | _unassigned_     |                   |                            |                              |
|`U+0CDD`   | _unassigned_     |                   |                            |                              |
|`U+0CDE`   | Letter           | CONSONANT         | _null_                     | &#x0CDE; Fa                  |
|`U+0CDF`   | _unassigned_     |                   |                            |                              |
| | | | |																		
|`U+0CE0`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0CE0; Vocalic Rr          |
|`U+0CE1`   | Letter           | VOWEL_INDEPENDENT | _null_                     | &#x0CE1; Vocalic Ll          |
|`U+0CE2`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0CE2; Sign Vocalic L      |
|`U+0CE3`   | Mark [Mn]        | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x0CE3; Sign Vocalic Ll     |
|`U+0CE4`   | _unassigned_     |                   |                            |                              |
|`U+0CE5`   | _unassigned_     |                   |                            |                              |
|`U+0CE6`   | Number           | NUMBER            | _null_                     | &#x0CE6; Digit Zero          |
|`U+0CE7`   | Number           | NUMBER            | _null_                     | &#x0CE7; Digit One           |
|`U+0CE8`   | Number           | NUMBER            | _null_                     | &#x0CE8; Digit Two           |
|`U+0CE9`   | Number           | NUMBER            | _null_                     | &#x0CE9; Digit Three         |
|`U+0CEA`   | Number           | NUMBER            | _null_                     | &#x0CEA; Digit Four          |
|`U+0CEB`   | Number           | NUMBER            | _null_                     | &#x0CEB; Digit Five          |
|`U+0CEC`   | Number           | NUMBER            | _null_                     | &#x0CEC; Digit Six           |
|`U+0CED`   | Number           | NUMBER            | _null_                     | &#x0CED; Digit Seven         |
|`U+0CEE`   | Number           | NUMBER            | _null_                     | &#x0CEE; Digit Eight         |
|`U+0CEF`   | Number           | NUMBER            | _null_                     | &#x0CEF; Digit Nine          |
| | | | |																		
|`U+0CF0`   | _unassigned_     |                   |                            |                              |
|`U+0CF1`   | Letter           | CONSONANT_WITH_STACKER | _null_                | &#x0CF1; Jihvamuliya         |
|`U+0CF2`   | Letter           | CONSONANT_WITH_STACKER | _null_                | &#x0CF2; Upadhmaniya         |
|`U+0CF3`   | _unassigned_     |                   |                            |                              |
|`U+0CF4`   | _unassigned_     |                   |                            |                              |
|`U+0CF5`   | _unassigned_     |                   |                            |                              |
|`U+0CF6`   | _unassigned_     |                   |                            |                              |
|`U+0CF7`   | _unassigned_     |                   |                            |                              |
|`U+0CF8`   | _unassigned_     |                   |                            |                              |
|`U+0CF9`   | _unassigned_     |                   |                            |                              |
|`U+0CFA`   | _unassigned_     |                   |                            |                              |
|`U+0CFB`   | _unassigned_     |                   |                            |                              |
|`U+0CFC`   | _unassigned_     |                   |                            |                              |
|`U+0CFD`   | _unassigned_     |                   |                            |                              |
|`U+0CFE`   | _unassigned_     |                   |                            |                              |
|`U+0CFF`   | _unassigned_     |                   |                            |                              |



## Vedic Extensions character table ##

Sanskrit runs written in the Kannada script may also include
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

In addition to general punctuation, runs of Kannada text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block. Kannada text can also incorporate the udatta
(`U+0951`) and anudatta (`U+0952`) signs from the Devanagari block.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                          |
|:----------|:-----------------|:------------------|:---------------------------|:-------------------------------|
|`U+0951`   | Mark [Mn]        | CANTILLATION      | TOP_POSITION               | &#x0951; Udatta              |
|`U+0952`   | Mark [Mn]        | CANTILLATION      | BOTTOM_POSITION            | &#x0952; Anudatta            |
|`U+0964`   | Punctuation      | _null_            | _null_                     | &#x0964; Danda               |
|`U+0965`   | Punctuation      | _null_            | _null_                     | &#x0965; Double Danda        |



Other important characters that may be encountered when shaping runs
of Kannada text include the dotted-circle placeholder (`U+25CC`), the
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

