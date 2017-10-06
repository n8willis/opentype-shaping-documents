# Bengali shaping in OpenType #

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

  - [General information](#general-information)
  - [Glyph classification](#glyph-classification)
  - [Terminology](#terminology)
  - [The `<bng2>` shaping model](#the-bng2-shaping-model)
      - [(1) Identifying syllables and other clusters](#1-identifying-syllables-and-other-clusters)
      - [(2) Initial reordering](#2-initial-reordering)
      - [(3) Applying the basic substitution features from GSUB](#3-applying-the-basic-substitution-features-from-gsub)
      - [(4) Final reordering](#4-final-reordering)
      - [(5) Applying all remaining substitution features from GSUB](#5-applying-all-remaining-substitution-features-from-gsub)
      - [(6) Applying remaining positioning features from GPOS](#6-applying-remaining-positioning-features-from-gpos)

<!-- markdown-toc end -->


## General information ##

The Bengali or Bangla script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
clusters of consonants are often represented as conjuncts.

The Bengali script is used to write multiple languages, most commonly
Bengali, Assamese, and Manipuri. In addition, Sanskrit may be written
in Bengali, so Bengali script runs may include glyphs from the Vedic
Extension block of Unicode. 

There are two extant Bengali script tags, `<beng>` and `<bng2>`. The older
script tag, `<beng>`, was deprecated in 2008.  Therefore, new fonts
should be engineered to work with the `<bng2>` shaping model. However,
if a font is encountered that supports only `<beng>`, the shaping engine
should deal with it gracefully.

## Glyph classification ##

Shaping Bengali text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and diacritic
marks. 

For most glyphs, the classifications assigned by Unicode are correct,
but are not sufficient to capture the expected shaping
behavior. Therefore, Bengali glyphs must additionally be classified by
how they are treated when shaping a run of text. 

Bengali glyphs should be classified as in the following
table. Codepoints in the Bengali block with no assigned meaning are
marked as _unassigned_ in the _Unicode class_ column. 

Assigned codepoints marked with a _null_ in the _Shaping category_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Bengali block, such as
currency marks and other symbols. 

Numbers generally evoke no special behavior from the shaping engine,
but there are still OpenType feature tags that may affect how the
respective glyphs are drawn, such as `tnum`, which specifies the usage
of tabular widths.

The _Mark-placement subcategory_ column indicates mark-placement
positioning. Assigned codepoints marked with a
_null_ in this column evoke no special mark-placement behavior. Marks
tagged with [Mn] in the _Unicode class_ column are classified as
non-spacing; marks tagged with [Mc] are classified as spacing-combining.

| Codepoint | Unicode class | Shaping category  | Mark-placement subcategory | Glyph                        |
|:----------|:--------------|:------------------|:---------------------------|:-----------------------------|
|`U+0980`   | Letter        | _null_            | _null_                     | &#x0980; Anji                |
|`U+0981`   | Mark [Mn]     | BINDU             | TOP_POSITION               | &#x0981; Candrabindu         |
|`U+0982`   | Mark [Mc]     | BINDU             | RIGHT_POSITION             | &#x0982; Anusvara            |
|`U+0983`   | Mark [Mc]     | VISARGA           | RIGHT_POSITION             | &#x0983; Visarga             |
|`U+0984`   | _unassigned_  |                   |                            |                              |
|`U+0985`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0985; A                   |
|`U+0986`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0986; Aa                  |
|`U+0987`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0987; I                   |
|`U+0988`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0988; Ii                  |
|`U+0989`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0989; U                   |
|`U+098A`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x098A; Uu                  |
|`U+098B`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x098B; Vocalic R           |
|`U+098C`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x098C; Vocalic L           |
|`U+098D`   | _unassigned_  |                   |                            |                              |
|`U+098E`   | _unassigned_  |                   |                            |                              |
|`U+098F`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x098F; E                   |
| | | | |																	   
|`U+0990`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0990; Ai                  |
|`U+0991`   | _unassigned_  |                   |                            |                              |
|`U+0992`   | _unassigned_  |                   |                            |                              |
|`U+0993`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0993; O                   |
|`U+0994`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x0994; Au                  |
|`U+0995`   | Letter        | CONSONANT         | _null_                     | &#x0995; Ka                  |
|`U+0996`   | Letter        | CONSONANT         | _null_                     | &#x0996; Kha                 |
|`U+0997`   | Letter        | CONSONANT         | _null_                     | &#x0997; Ga                  |
|`U+0998`   | Letter        | CONSONANT         | _null_                     | &#x0998; Gha                 |
|`U+0999`   | Letter        | CONSONANT         | _null_                     | &#x0999; Nga                 |
|`U+099A`   | Letter        | CONSONANT         | _null_                     | &#x099A; Ca                  |
|`U+099B`   | Letter        | CONSONANT         | _null_                     | &#x099B; Cha                 |
|`U+099C`   | Letter        | CONSONANT         | _null_                     | &#x099C; Ja                  |
|`U+099D`   | Letter        | CONSONANT         | _null_                     | &#x099D; Jha                 |
|`U+099E`   | Letter        | CONSONANT         | _null_                     | &#x099E; Nya                 |
|`U+099F`   | Letter        | CONSONANT         | _null_                     | &#x099F; Tta                 |
| | | | |																	   
|`U+09A0`   | Letter        | CONSONANT         | _null_                     | &#x09A0; Ttha                |
|`U+09A1`   | Letter        | CONSONANT         | _null_                     | &#x09A1; Dda                 |
|`U+09A2`   | Letter        | CONSONANT         | _null_                     | &#x09A2; Ddha                |
|`U+09A3`   | Letter        | CONSONANT         | _null_                     | &#x09A3; Nna                 |
|`U+09A4`   | Letter        | CONSONANT         | _null_                     | &#x09A4; Ta                  |
|`U+09A5`   | Letter        | CONSONANT         | _null_                     | &#x09A5; Tha                 |
|`U+09A6`   | Letter        | CONSONANT         | _null_                     | &#x09A6; Da                  |
|`U+09A7`   | Letter        | CONSONANT         | _null_                     | &#x09A7; Dha                 |
|`U+09A8`   | Letter        | CONSONANT         | _null_                     | &#x09A8; Na                  |
|`U+09A9`   | _unassigned_  |                   |                            |                              |
|`U+09AA`   | Letter        | CONSONANT         | _null_                     | &#x09AA; Pa                  |
|`U+09AB`   | Letter        | CONSONANT         | _null_                     | &#x09AB; Pha                 |
|`U+09AC`   | Letter        | CONSONANT         | _null_                     | &#x09AC; Ba                  |
|`U+09AD`   | Letter        | CONSONANT         | _null_                     | &#x09AD; Bha                 |
|`U+09AE`   | Letter        | CONSONANT         | _null_                     | &#x09AE; Ma                  |
|`U+09AF`   | Letter        | CONSONANT         | _null_                     | &#x09AF; Ya                  |
| | | | |																	    
|`U+09B0`   | Letter        | CONSONANT         | _null_                     | &#x09B0; Ra                  |
|`U+09B1`   | _unassigned_  |                   |                            |                              |
|`U+09B2`   | Letter        | CONSONANT         | _null_                     | &#x09B2; La                  |
|`U+09B3`   | _unassigned_  |                   |                            |                              |
|`U+09B4`   | _unassigned_  |                   |                            |                              |
|`U+09B5`   | _unassigned_  |                   |                            |                              |
|`U+09B6`   | Letter        | CONSONANT         | _null_                     | &#x09B6; Sha                 |
|`U+09B7`   | Letter        | CONSONANT         | _null_                     | &#x09B7; Ssa                 |
|`U+09B8`   | Letter        | CONSONANT         | _null_                     | &#x09B8; Sa                  |
|`U+09B9`   | Letter        | CONSONANT         | _null_                     | &#x09B9; Ha                  |
|`U+09BA`   | _unassigned_  |                   |                            |                              |
|`U+09BB`   | _unassigned_  |                   |                            |                              |
|`U+09BC`   | Mark [Mn]     | NUKTA             | BOTTOM_POSITION            | &#x09BC; Nukta               |
|`U+09BD`   | Letter        | AVAGRAHA          | _null_                     | &#x09BD; Avagraha            |
|`U+09BE`   | Mark [Mc]     | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09BE; Sign Aa             |
|`U+09BF`   | Mark [Mc]     | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09BF; Sign I              |
| | | | |																	   
|`U+09C0`   | Mark [Mc]     | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09C0; Sign Ii             |
|`U+09C1`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C1; Sign U              |
|`U+09C2`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C2; Sign Uu             |
|`U+09C3`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C3; Sign Vocalic R      |
|`U+09C4`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09C4; Sign Vocalic Rr     |
|`U+09C5`   | _unassigned_  |                   |                            |                              |
|`U+09C6`   | _unassigned_  |                   |                            |                              |
|`U+09C7`   | Mark [Mc]     | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C7; Sign E              |
|`U+09C8`   | Mark [Mc]     | VOWEL_DEPENDENT   | LEFT_POSITION              | &#x09C8; Sign Ai             |
|`U+09C9`   | _unassigned_  |                   |                            |                              |
|`U+09CA`   | _unassigned_  |                   |                            |                              |
|`U+09CB`   | Mark [Mc]     | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CB; Sign O              |
|`U+09CC`   | Mark [Mc]     | VOWEL_DEPENDENT   | LEFT_AND_RIGHT_POSITION    | &#x09CC; Sign Au             |
|`U+09CD`   | Mark [Mn]     | VIRAMA            | BOTTOM_POSITION            | &#x09CD; Virama              |
|`U+09CE`   | Letter        | CONSONANT_DEAD    | _null_                     | &#x09CE; Khanda Ta           |
|`U+09CF`   | _unassigned_  |                   |                            |                              |
| | | | |																	   
|`U+09D0`   | _unassigned_  |                   |                            |                              |
|`U+09D1`   | _unassigned_  |                   |                            |                              |
|`U+09D2`   | _unassigned_  |                   |                            |                              |
|`U+09D3`   | _unassigned_  |                   |                            |                              |
|`U+09D4`   | _unassigned_  |                   |                            |                              |
|`U+09D5`   | _unassigned_  |                   |                            |                              |
|`U+09D6`   | _unassigned_  |                   |                            |                              |
|`U+09D7`   | Mark [Mc]     | VOWEL_DEPENDENT   | RIGHT_POSITION             | &#x09D7; Au Length Mark      |
|`U+09D8`   | _unassigned_  |                   |                            |                              |
|`U+09D9`   | _unassigned_  |                   |                            |                              |
|`U+09DA`   | _unassigned_  |                   |                            |                              |
|`U+09DB`   | _unassigned_  |                   |                            |                              |
|`U+09DC`   | Letter        | CONSONANT         | _null_                     | &#x09DC; Rra                 |
|`U+09DD`   | Letter        | CONSONANT         | _null_                     | &#x09DD; Rha                 |
|`U+09DE`   | _unassigned_  |                   |                            |                              |
|`U+09DF`   | Letter        | CONSONANT         | _null_                     | &#x09DF; Yya                 |
| | | | |																	   
|`U+09E0`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x09E0; Vocalic Rr          |
|`U+09E1`   | Letter        | VOWEL_INDEPENDENT | _null_                     | &#x09E1; Vocalic Ll          |
|`U+09E2`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E2; Sign Vocalic L      |
|`U+09E3`   | Mark [Mn]     | VOWEL_DEPENDENT   | BOTTOM_POSITION            | &#x09E3; Sign Vocalic Ll     |
|`U+09E4`   | _unassigned_  |                   |                            |                              |
|`U+09E5`   | _unassigned_  |                   |                            |                              |
|`U+09E6`   | Number        | NUMBER            | _null_                     | &#x09E6; Digit Zero          |
|`U+09E7`   | Number        | NUMBER            | _null_                     | &#x09E7; Digit One           |
|`U+09E8`   | Number        | NUMBER            | _null_                     | &#x09E8; Digit Two           |
|`U+09E9`   | Number        | NUMBER            | _null_                     | &#x09E9; Digit Three         |
|`U+09EA`   | Number        | NUMBER            | _null_                     | &#x09EA; Digit Four          |
|`U+09EB`   | Number        | NUMBER            | _null_                     | &#x09EB; Digit Five          |
|`U+09EC`   | Number        | NUMBER            | _null_                     | &#x09EC; Digit Six           |
|`U+09ED`   | Number        | NUMBER            | _null_                     | &#x09ED; Digit Seven         |
|`U+09EE`   | Number        | NUMBER            | _null_                     | &#x09EE; Digit Eight         |
|`U+09EF`   | Number        | NUMBER            | _null_                     | &#x09EF; Digit Nine          |
| | | | |
|`U+09F0`   | Letter        | CONSONANT         | _null_                     | &#x09F0; Assamese Ra         |
|`U+09F1`   | Letter        | CONSONANT         | _null_                     | &#x09F1; Assamese Wa         |
|`U+09F2`   | Symbol        | _null_            | _null_                     | &#x09F2; Rupee Mark          |
|`U+09F3`   | Symbol        | _null_            | _null_                     | &#x09F3; Rupee Sign          |
|`U+09F4`   | Number        | _null_            | _null_                     | &#x09F4; Numerator One       |
|`U+09F5`   | Number        | _null_            | _null_                     | &#x09F5; Numerator Two       |
|`U+09F6`   | Number        | _null_            | _null_                     | &#x09F6; Numerator Three     |
|`U+09F7`   | Number        | _null_            | _null_                     | &#x09F7; Numerator Four      |
|`U+09F8`   | Number        | _null_            | _null_                     | &#x09F8; Numerator One Less  |
|`U+09F9`   | Number        | _null_            | _null_                     | &#x09F9; Denominator Sixteen |
|`U+09FA`   | Symbol        | _null_            | _null_                     | &#x09FA; Isshar              |
|`U+09FB`   | Symbol        | _null_            | _null_                     | &#x09FB; Ganda Mark          |
|`U+09FC`   | Letter        | _null_            | _null_                     | &#x09FC; Vedic Anusvara      |
|`U+09FD`   | Punctuation   | _null_            | _null_                     | &#x09FD; Abbreviation Sign   |
|`U+09FE`   | _unassigned_  |                   |                            |                              |
|`U+09FF`   | _unassigned_  |                   |                            |                              |
 

Sanskrit runs written in the Bengali script may also include
characters from the Vedic Extensions block. These characters should be
classified as follows:

| Codepoint | Unicode class | Shaping category  | Mark-placement subcategory | Glyph                        |
|:----------|:--------------|:------------------|:---------------------------|:-----------------------------|
|`U+1CD0`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CD0; Tone Karshana       |
|`U+1CD1`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CD1; Tone Shara          |
|`U+1CD2`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CD2; Tone Prenkha        |
|`U+1CD3`   | Punctuation   | _null_            | _null_                     | &#x1CD3; Sign Nihshvasa      |
|`U+1CD4`   | Mark [Mn]     | CANTILLATION      | OVERSTRUCK                 | &#x1CD4; Tone Midline Svarita |
|`U+1CD5`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CD5; Tone Aggravated Independent Svarita |
|`U+1CD6`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CD6; Tone Independent Svarita |
|`U+1CD7`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CD7; Tone Kathaka Independent Svarita |
|`U+1CD8`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CD8; Tone Candra Below   |
|`U+1CD9`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CD9; Tone Kathaka Independent Svarita Schroeder |
|`U+1CDA`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CDA; Tone Double Svarita |
|`U+1CDB`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CDB; Tone Triple Svarita |
|`U+1CDC`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CDC; Tone Kathaka Anudatta |
|`U+1CDD`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CDD; Tone Dot Below      |
|`U+1CDE`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CDE; Tone Two Dots Below |
|`U+1CDF`   | Mark [Mn]     | CANTILLATION      | BOTTOM_POSITION            | &#x1CDF; Tone Three Dots Below |
| | | | |																		
|`U+1CE0`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CE0; Tone Rigvedic Kashmiri Independent Svarita |
|`U+1CE1`   | Mark [Mc]     | CANTILLATION      | RIGHT_POSITION             | &#x1CE1; Tone Atharavedic Independent Svarita |
|`U+1CE2`   | Mark [Mn]     | AVAGRAHA          | OVERSTRUCK                 | &#x1CE2; Sign Visarga Svarita |
|`U+1CE3`   | Mark [Mn]     | _null_            | OVERSTRUCK                 | &#x1CE3; Sign Visarga Udatta |
|`U+1CE4`   | Mark [Mn]     | _null_            | OVERSTRUCK                 | &#x1CE4; Sign Reversed Visarga Udatta |
|`U+1CE5`   | Mark [Mn]     | _null_            | OVERSTRUCK                 | &#x1CE5; Sign Visarga Anudatta |
|`U+1CE6`   | Mark [Mn]     | _null_            | OVERSTRUCK                 | &#x1CE6; Sign Reversed Visarga Anudatta |
|`U+1CE7`   | Mark [Mn]     | _null_            | OVERSTRUCK                 | &#x1CE7; Sign Visarga Udatta With Tail |
|`U+1CE8`   | Mark [Mn]     | AVAGRAHA          | OVERSTRUCK                 | &#x1CE8; Sign Visarga Anudatta With Tail |
|`U+1CE9`   | Letter        | AVAGRAHA          | _null_                     | &#x1CE9; Sign Anusvara Antargomukha |
|`U+1CEA`   | Letter        | _null_            | _null_                     | &#x1CEA; Sign Anusvara Bahirgomukha |
|`U+1CEB`   | Letter        | _null_            | _null_                     | &#x1CEB; Sign Anusvara Vamagomukha |
|`U+1CEC`   | Letter        | AVAGRAHA          | _null_                     | &#x1CEC; Sign Anusvara Vamagomukha With Tail |
|`U+1CED`   | Mark [Mn]     | AVAGRAHA          | BOTTOM_POSITION            | &#x1CED; Sign Tiryak         |
|`U+1CEE`   | Letter        | AVAGRAHA          | _null_                     | &#x1CEE; Sign Hexiform Long Anusvara |
|`U+1CEF`   | Letter        | _null_            | _null_                     | &#x1CEF; Sign Long Anusvara  |
| | | | |																		
|`U+1CF0`   | Letter        | _null_            | _null_                     | &#x1CF0; Sign Rthang Long Anusvara |
|`U+1CF1`   | Letter        | AVAGRAHA          | _null_                     | &#x1CF1; Sign Anusvara Ubhayato Mukha |
|`U+1CF2`   | Mark [Mc]     | VISARGA           | _null_                     | &#x1CF2; Sign Ardhavisarga   |
|`U+1CF3`   | Mark [Mc]     | VISARGA           | _null_                     | &#x1CF3; Sign Rotated Ardhavisarga |
|`U+1CF4`   | Mark [Mn]     | CANTILLATION      | TOP_POSITION               | &#x1CF4; Tone Candra Above   |
|`U+1CF5`   | Letter        | CONSONANT         | _null_                     | &#x1CF5; Sign Jihvamuliya    |
|`U+1CF6`   | Letter        | CONSONANT         | _null_                     | &#x1CF6; Sign Upadhmaniya    |
|`U+1CF7`   | Mark [Mc]     | _null_            | _null_                     | &#x1CF7; Sign Atikrama       |
|`U+1CF8`   | Mark [Mn]     | CANTILLATION      | _null_                     | &#x1CF8; Tone Ring Above     |
|`U+1CF9`   | Mark [Mn]     | CANTILLATION      | _null_                     | &#x1CF9; Tone Double Ring Above |
|`U+1CFA`   | _unassigned_  |                   |                            |                              |
|`U+1CFB`   | _unassigned_  |                   |                            |                              |
|`U+1CFC`   | _unassigned_  |                   |                            |                              |
|`U+1CFD`   | _unassigned_  |                   |                            |                              |
|`U+1CFE`   | _unassigned_  |                   |                            |                              |
|`U+1CFF`   | _unassigned_  |                   |                            |                              |


<!-- 1cf5 and 1cf6 get reclassified as CONSONANT

1ce2 and 1ce8 get treated like tone marks, but SHOULD be allowed only after Visarga.

1ced gets treated like tone mark, but SHOULD be allowed only after U+1CE9..U+1CF1

1ce9 1cec 1cee 1cf1 all take marks in standalone clusters, similar to Avagraha.

U+2010 and U+2011 get treated like placeholders.

U+25CC is the dotted circle. --->
<!---
  /* General Punctuation */

  /* 2008 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),_(ZWNJ,x),_(ZWJ,x),  _(x,x),  _(x,x),
  /* 2010 */ _(CP,x), _(CP,x), _(CP,x), _(CP,x), _(CP,x),  _(x,x),  _(x,x),  _(x,x),

#define indic_offset_0x2070u 1672


  /* Superscripts and Subscripts */

  /* 2070 */  _(x,x),  _(x,x),  _(x,x),  _(x,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2078 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2080 */  _(x,x),  _(x,x), _(SM,x), _(SM,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
--->

## Terminology ##

OpenType shaping uses a standard set of terms for Indic scripts.  The
terms used in any particular language may vary, causing potential
confusion.

**Matra** is the standard term for a dependent vowel sign. In the Bengali
language, dependent-vowel signs <!--- that are positioned below the base
consonant --> may also be referred to as _kar_ forms — e.g., "i-kar" or
"u-kar".

The term "matra" is also used to refer to the headline above most
Bengali letters. To avoid ambiguity, the term **headline** is
used in most Unicode and OpenType shaping documents.

**Halant** and **Virama** are both standard terms for the below-base "vowel-killer"
sign. In the Bengali language, this sign is known as the _hasanta_.

**Chandrabindu** (or simply **Bindu**) is the standard term for the diacritical mark
indicating that the preceding vowel shold be nasalized. In the Bengali
language, this mark is known as _candrabindu_.

Where possible, using the standard terminology is preferred, as the
use of a language-specific term necessitates choosing one language
over all of the others that share a common script.

## The `<bng2>` shaping model ##

Processing a run of `<bng2>` text involves six top-level stages:

1. Identifying syllables and other clusters
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying all remaining positioning features from GPOS


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve invoking a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

<!-- > Note: Bengali differs from Devanagari in that sequences of pre-base consonants
> are generally combined into conjuncts and only less frequently
> rendered in half-forms. -->

With regard to the common variations seen among Indic scripts, 
Bengali's specific shaping characteristics include:

1. `BASE_POS_LAST` = The base consonant of a syllable is the last
consonant, not counting any special final-consonant forms.

2. `REPH_POS_AFTER_SUB` = "Reph" is positioned after subjoined (i.e.,
   below-base) consonant forms.

3. `REPH_MODE_IMPLICIT` = "Reph" is formed by an initial "Ra,Halant" sequence.

4. `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied both to
   pre-base consonants and to post-base consonants.

5. `MATRA_POS_RIGHT` = `POS_AFTER_POST` = Right-side matras are
   positioned after post-base consonant forms.

6. `MATRA_POS_BOTTOM` = `POS_AFTER_SUB` = Below-base matras are
   positioned after subjoined (i.e., below-base) consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how "Reph"
should be encoded within a run of text.

### (1) Identifying syllables and other clusters ###

A syllable cluster in Bengali consists of a valid orthographic cluster
that MAY be followed by a "tail" of modifier signs.

> Note: The Bengali Unicode block enumerates five modifier signs,
> "Candrabinu" (`U+0981`), "Anusvara" (`U+0982`), "Visarga" 
> (`U+0983`), "Avagraha" (`U+09BD`), and "Vedic Anusvara"
> (`U+09FC`). In addition, Sanskrit text written in Bengali may
> include additional signs from Vedic Extensions block.

Each syllable contains exactly one vowel. The consonant (if any
exists) that carries the vowel is the "base" consonant of the
syllable.

Valid syllables may begin with either a consonant or an independent
vowel.  Zero or more additional consonants may be present in the
syllable; in a valid syllable these other consonants will be followed
by the "Halant" mark, which indicates that they carry no vowel. 

> Note: The consonant "Ra" receives special treatment; in many
> circumstances it is replaced with a combining mark-like form. 
> A "Ra,Halant" sequence at the beginning of a cluster is
> replaced with an above-base mark called "Reph" (unless the "Ra"
> is the only consonant in the cluster). 
>
> This requirement is synonymous with the `REPH_MODE_IMPLICIT`
> characteristic mentioned earlier.
>
> "Ra,Halant" sequences that occur elsewhere in the cluster may take on the
> below-base form "Raphala." "Reph" and "Raphala" sequences must be
> reordered after the syllable-identification stage is complete.
>
> `<bng2>` text contains two Unicode codepoints for "Ra." `U+09B0` and `U+09F0`.
>
> `U+09B0` is used in Bengali-language, Manipuri-language, and Sanskrit text. `U+09F0` is used in
> Assamese-language text.
>

In addition, stand-alone clusters may occur, such as when an isolated
codepoint is shown in example text.

Clusters should be identified by examining the run and matching
glyphs, based on their categorization, using regular expressions. 


	C	consonant
	V	independent vowel
	N	nukta
	H	halant/virama
	ZWNJ	zero width non-joiner
	ZWJ	zero width joiner
	M	matra (up to one of each type: pre-base, below-base, or post-base)
	SM	syllable modifier signs
	VD	vedic signs
	A	anudatta (U+0952)
	NBSP	NO-BREAK SPACE

A consonant syllable will match the expression:
```
{C+[N]+<H+[<ZWNJ|ZWJ>]|<ZWNJ|ZWJ>+H>} + C+[N]+[A] + [< H+[<ZWNJ|ZWJ>] | {M}+[N]+[H]>]+[SM]+[(VD)]
```

A vowel-based syllable will match the expression:
```
[Ra+H]+V+[N]+[<[<ZWJ|ZWNJ>]+H+C|ZWJ+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A stand-alone cluster (which can only occur at the start of a word) will match the expression:
```
[Ra+H]+NBSP+[N]+[<[<ZWJ|ZWNJ>]+H+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A cluster that does not match any of these expressions should be
regarded as broken. The shaping engine may make a best-effort attempt
to shape the broken cluster, but making guarantees about the correctness or
appearance of the final result is out of scope for this document.

After the clusters have been identified, each of the subsequent 
shaping stages occurs on a per-cluster basis.

### (2) Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text to the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs, 
> "Ra,Halant" glyph sequences, and other consonants that take special
> treatment in some circumstances. "Ba", "Ta", and "Ya" occasionally
> take on special forms, depending on their position in the syllable.
>
> These reordering moves are mandatory. The final-reordering stage
> may make additional moves, depending on the text and on the features
> implemented in the active font.

The cluster should be processed by tagging each glyph with its
intended position based on its ordering category. After all glyphs
have been tagged, the entire cluster should be sorted in stable order,
so that glyphs of the same ordering category remain in the same
relative position with respect to each other.

The final sort order of the ordering categories should be:


	POS_RA_TO_BECOME_REPH
	POS_PREBASE_MATRA
	POS_PREBASE_CONSONANT

	POS_BASE_CONSONANT
	POS_AFTER_MAIN

	POS_ABOVEBASE_CONSONANT

	POS_BEFORE_SUB
	POS_BELOWBASE_CONSONANT
	POS_AFTER_SUB

	POS_BEFORE_POST
	POS_POSTBASE_CONSONANT
	POS_AFTER_POST

	POS_FINAL_CONSONANT
	POS_SMVD


1. The first step is to determine the base consonant of the cluster
and tag it as `POS_BASE_CONSONANT`.

The algorithm for determining the base consonant is

- If the syllable starts with "Ra,Halant" and the cluster contains more than one consonant, exclude the starting "Ra" from the list of consonants to be considered.
- Starting from the end of the syllable, move backwards until a consonant is found.
    * If the consonant has a below-base or post-base form or is a pre-base reordering "Ra", move to the previous consonant. If neither condition is true, stop.
    * If the consonant is the first consonant, stop.

The consonant stopped at will be the base consonant.

2. Second, any two-part dependent vowels (matras) must be decomposed into their
left-side and right-side components. Bengali has two
two-part dependent vowels, "O" (`U+09BC`) and "AU" (`U+09CC`). Each has a canonical decomposition, so this step is unambiguous.

> "O" (`U+09BC`) decomposes to "`U+09C7`,`U+09BE`"
>
> "AU" (`U+09CC`) decomposes to "`U+09C7`,`U+09D7`"

3. Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be  moved to the beginning of the
cluster, with `POS_PREBASE_MATRA`.

4. Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s, syllable modifiers, and Vedic signs) must be reordered so that they appear in canonical order. "Nukta"s must be placed before all other marks. 

5. Fifth, consonants that will take on pre-base forms must be tagged
with `POS_PREBASE_CONSONANT`.

6. Sixth, initial "Ra,Halant" sequences that will become rephs must be tagged with
`POS_RA_TO_BECOME_REPH`.

7. Seventh, any consonants that occur after a dependent vowel (matra) sign must be tagged with
`POS_POSTBASE_CONSONANT`. Such consonants will usually be followed by a "Halant" glyph, with the 
exception of special final-consonants. Bengali includes two such final consonants, "Khanda Ta"
(`U+09CE`), and the sequence "Halant,Ya" (`U+09CD`,`U+09AF`), which triggers the "Yaphala" form. 

8. Eighth, all miscellaneous marks must be attached to the
preceding character, so that they move together during the sorting step.

9. Ninth, all post-base glyphs should be merged into a single substring that will sort as a single unit.

With these steps completed, the cluster can be sorted into the final sort order.

### (3) Applying the basic substitution features from GSUB ###

The basic-substitution stage applies mandatory substitution features using the rules in the font's
GSUB table. In preparation for this stage, glyph sequences should be tagged for possible application
of GSUB features.

The order in which these substitutions must be performed is fixed:

	nukt
	akhn
	rphf
<!-- rkrf -->
	pref
	blwf
<!-- abvf -->
	half
	pstf
	vatu
	cjct
	cfar

The `nukt` feature replaces "_consonant_,Nukta" sequences with a precomposed nukta-variant of the consonant glyph.

The `akhn` feature replaces two specific sequences with required ligatures. 
"Ka,Halant,Ssa" is substituted with the "KaSsa"
ligature. "Ja,Halant,Nya" is substituted with the "JaNya" ligature. 

The `rphf` feature replaces initial "Ra,Halant" sequences with the "Reph" glyph.

The `pref` feature replaces pre-base-consonant glyphs with any special forms.

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Bengali includes two below-base consonant
forms. "Ra,Halant" in a non-cluster-initial position takes on the
"Raphala" form; "Ba,Halant" takes on the "Baphala" form. 

The `half` feature replaces "_consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs.

The `pstf` feature replaces post-base-consonant glyphs with any special forms.

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. "Vattu variants" are formed by glyphs followed by "Raphala"
(the below-base form of "Ra"), so this feature must be applied after
the `blwf` feature.

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. The font's GSUB rules might be implemented so that
`cjct` substitutions apply to half-form consonants; therefore, this
feature must be applied after the `half` feature.


### (4) Final reordering ###

The final reordering stage repositions marks, dependent-vowel (matra)
signs, and "Reph" glyphs to the appropriate location with respect to
the base consonant. Because multiple subsitutions may have occured
during the application of the basic-shaping features in the preceding
stage, these repositioning moves could not be performed during the
initial-reordering stage. 



### (5) Applying all remaining substitution features from GSUB ###

In this stage, the remaining substitution features from the GSUB table are applied. The order in which these features are applied is not canonical; they should be applied in the order in which they appear in the GSUB table in the font.

	init
	pres
	abvs
	blws
	psts
	haln

The `init` feature replaces word-initial glyphs with special presentation forms.

The `pres` feature replaces pre-base-consonant glyphs with special presentations forms. This can include consonant conjuncts, half-form consonants, and stylistic variants of left-side dependent vowels (matras).

The `abvs` feature replaces above-base-consonant glyphs with special presentation forms. This usually includes contextual variants of above-base marks or contextualy appropriate mark-and-base ligatures. 

The `blws` feature replaces below-base-consonant glyphs with special presentation forms. This usually includes replacing consonants that are followed by below-base-consonant forms like "Raphala" and "Baphalan" with contextual ligatures. 

The `psts` feature replaces post-base-consonant glyphs with special presenataion forms. This usually includes replacing right-side dependent vowels (matras) with stylistic variants or replacing post-base-consonant/matra pairs with contextual ligatures.

The `haln` feature replaces word-final "_consonant_,Halant" pairs with special presentation forms. This can include stylistic variants of the consonant where placing the "Halant" mark on its own is typographically problematic.



### (6) Applying remaining positioning features from GPOS ###

In this stage, mark positioning, kerning, and other GPOS features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the GPOS table in the font.

        dist
        abvm
        blwm

The `dist` feature adjusts the horizontal positioning of glyphs. Unlike `kern`, adjustments made with `dist` do not require the application or user to enable the _kerning_ feature, if that feature is optional.

The `abvm` feature positions above-base marks.

The `blwm` feature positions below-base marks.
