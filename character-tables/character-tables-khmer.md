# Khmer character tables #

This document lists the per-character shaping information needed to
[shape Khmer text](../opentype-shaping-khmer.md).

**Contents**

  - [Khmer character table](#khmer-character-table)
  - [Khmer Symbols character table](#khmer-symbols-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
	  

## Khmer character table ##

Khmer glyphs should be classified as in the following
table. Codepoints in the Khmer block with no assigned meaning are
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
|`U+17C6`   | Mark [Mn]        | NUKTA             | TOP_POSITION               | &#x17C6; Nikahit             |
|`U+17C7`   | Mark [Mc]        | VISARGA           | RIGHT_POSITION             | &#x17C7; Reahmuk             |
|`U+17C8`   | Mark [Mc]        | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x17C8; Yuukaleapintu       |
|`U+17C9`   | Mark [Mn]        | REGISTER_SHIFTER  | TOP_POSITION               | &#x17C9; Muusikatoan         |
|`U+17CA`   | Mark [Mn]        | REGISTER_SHIFTER  | TOP_POSITION               | &#x17CA; Triisap             |
|`U+17CB`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CB; Bantoc              |
|`U+17CC`   | Mark [Mn]        | CONSONANT_POST_REPHA| TOP_POSITION             | &#x17CC; Robat               |
|`U+17CD`   | Mark [Mn]        | CONSONANT_KILLER  | TOP_POSITION               | &#x17CD; Toandakhiat         |
|`U+17CE`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CE; Kakabat             |
|`U+17CF`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17CF; Ahsda               |
| | | | |																	   
|`U+17D0`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17D0; Samyok Sannya       |
|`U+17D1`   | Mark [Mn]        | PURE_KILLER       | TOP_POSITION               | &#x17D1; Viriam              |
|`U+17D2`   | Mark [Mn]        | INVISIBLE_STACKER | _null_                     | &#x17D2; Sign Coeng          |
|`U+17D3`   | Mark [Mn]        | SYLLABLE_MODIFIER | TOP_POSITION               | &#x17D3; Bathamasat          |
|`U+17D4`   | Punctuation      | _null_            | _null_                     | &#x17D4; Khan                |
|`U+17D5`   | Punctuation      | _null_            | _null_                     | &#x17D5; Bariyoosan          |
|`U+17D6`   | Punctuation      | _null_            | _null_                     | &#x17D6; Camnuc Pii Kuuh     |
|`U+17D7`   | Letter           | _null_            | _null_                     | &#x17D7; Lek Too             |
|`U+17D8`   | Punctuation      | _null_            | _null_                     | &#x17D8; Beyyal              |
|`U+17D9`   | Punctuation      | _null_            | _null_                     | &#x17D9; Phnaek Muan         |
|`U+17DA`   | Punctuation      | _null_            | _null_                     | &#x17DA; Koomuut             |
|`U+17DB`   | Symbol           | SYMBOL            | _null_                     | &#x17DB; Riel                |
|`U+17DC`   | Letter           | AVAGRAHA          | _null_                     | &#x17DC; Avakrahasanya       |
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
 

## Khmer Symbols character table ##

The Khmer Symbols block contains miscellaneous symbols used for
lunar-date calendars. None evoke any special behavior from the shaping engine.

| Codepoint | Unicode category | Shaping class     | Mark-placement subclass    | Glyph                        |
|:----------|:-----------------|:------------------|:---------------------------|:-----------------------------|
|`U+19E0`   | Symbol           | _null_            | _null_                     | &#x19E0; Pathamasat          |
|`U+19E1`   | Symbol           | _null_            | _null_                     | &#x19E1; Muoy Koet           |
|`U+19E2`   | Symbol           | _null_            | _null_                     | &#x19E2; Pii Koet            |
|`U+19E3`   | Symbol           | _null_            | _null_                     | &#x19E3; Bei Koet            |
|`U+19E4`   | Symbol           | _null_            | _null_                     | &#x19E4; Buon Koet           |
|`U+19E5`   | Symbol           | _null_            | _null_                     | &#x19E5; Pram Koet           |
|`U+19E6`   | Symbol           | _null_            | _null_                     | &#x19E6; Pram-Muoy Koet      |
|`U+19E7`   | Symbol           | _null_            | _null_                     | &#x19E7; Pram-Pii Koet       |
|`U+19E8`   | Symbol           | _null_            | _null_                     | &#x19E8; Pram-Bei Koet       |
|`U+19E9`   | Symbol           | _null_            | _null_                     | &#x19E9; Pram-Buon Koet      |
|`U+19EA`   | Symbol           | _null_            | _null_                     | &#x19EA; Dap Koet            |
|`U+19EB`   | Symbol           | _null_            | _null_                     | &#x19EB; Dap-Muoy Koet       |
|`U+19EC`   | Symbol           | _null_            | _null_                     | &#x19EC; Dap-Pii Koet        |
|`U+19ED`   | Symbol           | _null_            | _null_                     | &#x19ED; Dap-Bei Koet        |
|`U+19EE`   | Symbol           | _null_            | _null_                     | &#x19EE; Dap-Buon Koet       |
|`U+19EF`   | Symbol           | _null_            | _null_                     | &#x19EF; Dap-Pram Koet       |
| | | | |
|`U+19F0`   | Symbol           | _null_            | _null_                     | &#x19F0; Tuteyasat           |
|`U+19F1`   | Symbol           | _null_            | _null_                     | &#x19F1; Muoy ROC            |
|`U+19F2`   | Symbol           | _null_            | _null_                     | &#x19F2; Pii Roc             |
|`U+19F3`   | Symbol           | _null_            | _null_                     | &#x19F3; Bei Roc             |
|`U+19F4`   | Symbol           | _null_            | _null_                     | &#x19F4; Buon Roc            |
|`U+19F5`   | Symbol           | _null_            | _null_                     | &#x19F5; Pram Roc            |
|`U+19F6`   | Symbol           | _null_            | _null_                     | &#x19F6; Pram-Muoy Roc       |
|`U+19F7`   | Symbol           | _null_            | _null_                     | &#x19F7; Pram-Pii Roc        |
|`U+19F8`   | Symbol           | _null_            | _null_                     | &#x19F8; Pram-Bei Roc        |
|`U+19F9`   | Symbol           | _null_            | _null_                     | &#x19F9; Pram-Buon Roc       |
|`U+19FA`   | Symbol           | _null_            | _null_                     | &#x19FA; Dap Roc             |
|`U+19FB`   | Symbol           | _null_            | _null_                     | &#x19FB; Dap-Muoy Roc        |
|`U+19FC`   | Symbol           | _null_            | _null_                     | &#x19FC; Dap-Pii Roc         |
|`U+19FD`   | Symbol           | _null_            | _null_                     | &#x19FD; Dap-Bei Roc         |
|`U+19FE`   | Symbol           | _null_            | _null_                     | &#x19FE; Dap-Buon Roc        |
|`U+19FF`   | Symbol           | _null_            | _null_                     | &#x19FF; Dap-Pram Roc        |


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


The zero-width joiner (<abbr>ZWJ</abbr>) is primarily used to prevent the formation of a
conjunct from a "_Consonant_,Halant,_Consonant_" sequence. The sequence
"_Consonant_,Halant,ZWJ,_Consonant_" blocks the formation of a
conjunct between the two consonants. 

Note, however, that the "_Consonant_,Halant" subsequence in the above
example may still trigger a half-forms feature. To prevent the
application of the half-forms feature in addition to preventing the
conjunct, the zero-width non-joiner (<abbr>ZWNJ</abbr>) must be used instead. The sequence
"_Consonant_,Halant,ZWNJ,_Consonant_" should produce the first
consonant in its standard form, followed by an explicit "Halant".

A secondary usage of the zero-width joiner is to prevent the formation of
"Reph". An initial "Ra,Halant,ZWJ" sequence should not produce a "Reph",
where an initial "Ra,Halant" sequence without the zero-width joiner
otherwise would.

The no-break space (<abbr>NBSP<.abbr>) is primarily used to display
those codepoints that are defined as non-spacing (marks, dependent
vowels (matras), below-base consonant forms, and post-base consonant
forms) in an isolated context, as an alternative to displaying them
superimposed on the dotted-circle placeholder. These sequences will
match "NBSP,ZWJ,Halant,_Consonant_", "NBSP,_mark_", or
"NBSP,_matra_".

In addition to general punctuation, runs of Khmer text often use the
danda (`U+0964`) and double danda (`U+0965`) punctuation marks from
the Devanagari block.
