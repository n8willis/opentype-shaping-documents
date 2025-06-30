# Vedic Extensions in OpenType #

This document outlines the shaping information needed to display
characters from the Unicode Vedic Extensions block, which may be used
within text runs in many Indic scripts.

**Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Vedic Extensions character table](#vedic-extensions-character-table)
  - [Shaping information](#shaping-information)



## General information ##

The Vedic Extensions block encodes letters and marks that are used in
a large body of ancient literature written in the Vedic Sanskrit
language.

Primarily an oral language in the time period when the key literature
originated, Vedic Sanskrit has no native script. Therefore, texts may
be typeset in any one of the Indic scripts, using the Vedic Extensions
to supplement the main script's character set.

## Terminology ##

Individual Vedic Extension characters may be named by a combination of
the Vedic text in which the mark is used, the regional or manuscript
tradition involved, or a simple visual or phonetic description of the
character. Some commonly used general categories are worth noting.

**Udatta** is the term for a high tone on a vowel.

**Anudatta** is the term for a low tone on a vowel.

**Svarita** is the term for a falling or mixed tone on a vowel.

**Anusvara** is the term for a nasalization sound that precedes a consonant.

**Visarga** is the term for a soft breathing sound that precedes a vowel.

> Note: In modern Indic languages, the terms _anusvara_ and _visarga_
> often refer to diacritical marks that have the above effects on
> pronunciation. In the Vedic Sanskrit language, however, they are
> generally considered independent letters.

## Glyph classification ##

For most codepoints, the `General Category` property defined in the Unicode
standard is correct, but it is not sufficient to fully capture the
expected shaping behavior (such as how the character is treated during
glyph reordering). Therefore, they must additionally be classified by
how they are treated when shaping a run of text.


### Vedic Extensions character table ###


Vedic Extension glyphs should be classified as in the following
table. Codepoints with no assigned meaning are
marked as _unassigned_ in the _Unicode category_ column. 

Assigned codepoints marked with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. 

The _Mark-placement subclass_ column indicates mark-placement
positioning. Assigned codepoints marked with a
_null_ in this column evoke no special mark-placement behavior. Marks
tagged with [Mn] in the _Unicode category_ column are categorized as
non-spacing; marks tagged with [Mc] are categorized as
spacing-combining.

Some codepoints in the following table use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific behavior.


:::{table} Vedic Extensions character table

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
|`U+1CF2`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x1CF2; Sign Ardhavisarga   |
|`U+1CF3`   | Letter           | CONSONANT_DEAD    | _null_                     | &#x1CF3; Sign Rotated Ardhavisarga |
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
:::


## Shaping information ##

31 of the characters in the block are categorized as marks. 27 of
these marks are subcategorized as non-spacing; the remaining four are
spacing-combining. 

Of the non-spacing marks, 20 are classified as `CANTILLATION` (or tone-marker)
indicators, which modify the pitch of vowels. Most of these marks are
generally positioned above or below the main character, using <abbr title="Glyph Positioning table">GPOS</abbr>
mark attachment, in a position that does not interact or interfere
with the main character. In Unicode, the `CANTILLATION` classification
is separate from the `TONE_MARKER` classification used in some scripts
for semantic reasons; the two classifications are identical for
shaping purposes.

Some of the marks (cantillation and non-cantillation) are classified
as `OVERSTRUCK` in the _Mark-placement subclass_ column.
This indicates that the mark is intended to be rendered on top of the
preceding character. During reordering, `OVERSTRUCK` marks are tagged
for the ordering position `POS_AFTER_MAIN`.

Some marks are classified, for shaping purposes, as `AVAGRAHA` or
`VISARGA`. This indicates that the mark behaves more like the Avagraha
or Visarga character than like a diacritic.

Characters that are categorized in Unicode as letters vary with
respect to whether or not they trigger special behavior in the shaping
process. These include letters that are classified as `CONSONANT` and
letters that are classified as `AVAGRAHA`.



<!--- 1cf5 and 1cf6 get reclassified as CONSONANT

1ce2 and 1ce8 get treated like tone marks, but SHOULD be allowed only after Visarga.

1ced gets treated like tone mark, but SHOULD be allowed only after U+1CE9..U+1CF1

1ce9 1cec 1cee 1cf1 all take marks in standalone clusters, similar to Avagraha.
--->
