# Tamil character tables #

This document lists the per-character shaping information needed to
[shape Tamil text](opentype-shaping-tamil.md).

**Table of Contents**

  - [Tamil character table](#tamil-character-table)
  - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Tamil character table ##

Tamil glyphs should be classified as in the following
table. Codepoints in the Tamil block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Tamil block, such as
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
|`U+0BF3`   | Symbol           | _null_            | _null_                     | &#x0BF3; Day Sign            |
|`U+0BF4`   | Symbol           | _null_            | _null_                     | &#x0BF4; Month Sign          |
|`U+0BF5`   | Symbol           | _null_            | _null_                     | &#x0BF5; Year Sign           |
|`U+0BF6`   | Symbol           | _null_            | _null_                     | &#x0BF6; Debit Sign          |
|`U+0BF7`   | Symbol           | _null_            | _null_                     | &#x0BF7; Credit Sign         |
|`U+0BF8`   | Symbol           | _null_            | _null_                     | &#x0BF8; As Above Sign       |
|`U+0BF9`   | Symbol           | _null_            | _null_                     | &#x0BF9; Tamil Rupee Sign    |
|`U+0BFA`   | Symbol           | _null_            | _null_                     | &#x0BFA; Number Sign         |
|`U+0BFB`   | _unassigned_     |                   |                            |                              |
|`U+0BFC`   | _unassigned_     |                   |                            |                              |
|`U+0BFD`   | _unassigned_     |                   |                            |                              |
|`U+0BFE`   | _unassigned_     |                   |                            |                              |
|`U+0BFF`   | _unassigned_     |                   |                            |                              |



## Vedic Extensions character table ##

Sanskrit runs written in the Tamil script may also include
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

