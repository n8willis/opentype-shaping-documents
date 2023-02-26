# N'Ko character tables #

This document lists the per-character shaping information needed to
[shape N'Ko text](../opentype-shaping-nko.md).

**Table of Contents**

  - [NKo character table](#nko-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## NKo character table ##

N'Ko glyphs should be classified as in the following
table. Codepoints in the NKo block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column.

The _Joining type_ column indicates whether each codepoint is defined
as joining with adjacent characters on the left side, right side, left
and right sides ("DUAL"), or neither side ("NON_JOINING"). Codepoints
designated TRANSPARENT in the _Joining type_ column do not join with
adjacent characters and, in addition, do not affect the joining
behavior of surrounding characters. Non-spacing marks are of type
TRANSPARENT. Codepoints designated JOIN_CAUSING force adjacent
characters to join.

The _Joining group_ column lists the fundamental letter that the
listed codepoint behaves like for joining purposes.

Assigned codepoints with a _null_ in the _Joining group_
column evoke no special behavior from the shaping engine during the
join-computation stage.

> Note: No codepoints in the NKo block are assigned a non-null _Joining group_.

The _Mark class_ column indicates the Canonical Combining Class
for the codepoint.  Marks are assigned non-zero combining classes so
that sequences of adjacent marks can be reordered as required by the
orthography. 




| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+07C0`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C0; Digit Zero                           |
|`U+07C1`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C1; Digit One                            |
|`U+07C2`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C2; Digit Two                            |
|`U+07C3`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C3; Digit Three                          |
|`U+07C4`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C4; Digit Four                           |
|`U+07C5`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C5; Digit Five                           |
|`U+07C6`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C6; Digit Six                            |
|`U+07C7`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C7; Digit Seven                          |
|`U+07C8`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C8; Digit Eight                          |
|`U+07C9`   | Number           | NON_JOINING  | _null_               | _0_        | &#x07C9; Digit Nine                           |
|`U+07CA`   | Letter           | DUAL         | _null_               | _0_        | &#x07CA; A                                    |
|`U+07CB`   | Letter           | DUAL         | _null_               | _0_        | &#x07CB; Ee                                   |
|`U+07CC`   | Letter           | DUAL         | _null_               | _0_        | &#x07CC; I                                    |
|`U+07CD`   | Letter           | DUAL         | _null_               | _0_        | &#x07CD; E                                    |
|`U+07CE`   | Letter           | DUAL         | _null_               | _0_        | &#x07CE; U                                    |
|`U+07CF`   | Letter           | DUAL         | _null_               | _0_        | &#x07CF; Oo                                   |
| | | | | |                                                                                                      			      
|`U+07D0`   | Letter           | DUAL         | _null_               | _0_        | &#x07D0; O                                    |
|`U+07D1`   | Letter           | DUAL         | _null_               | _0_        | &#x07D1; Dagbasinna                           |
|`U+07D2`   | Letter           | DUAL         | _null_               | _0_        | &#x07D2; N                                    |
|`U+07D3`   | Letter           | DUAL         | _null_               | _0_        | &#x07D3; Ba                                   |
|`U+07D4`   | Letter           | DUAL         | _null_               | _0_        | &#x07D4; Pa                                   |
|`U+07D5`   | Letter           | DUAL         | _null_               | _0_        | &#x07D5; Ta                                   |
|`U+07D6`   | Letter           | DUAL         | _null_               | _0_        | &#x07D6; Ja                                   |
|`U+07D7`   | Letter           | DUAL         | _null_               | _0_        | &#x07D7; Cha                                  |
|`U+07D8`   | Letter           | DUAL         | _null_               | _0_        | &#x07D8; Da                                   |
|`U+07D9`   | Letter           | DUAL         | _null_               | _0_        | &#x07D9; Ra                                   |
|`U+07DA`   | Letter           | DUAL         | _null_               | _0_        | &#x07DA; Rra                                  |
|`U+07DB`   | Letter           | DUAL         | _null_               | _0_        | &#x07DB; Sa                                   |
|`U+07DC`   | Letter           | DUAL         | _null_               | _0_        | &#x07DC; Gba                                  |
|`U+07DD`   | Letter           | DUAL         | _null_               | _0_        | &#x07DD; Fa                                   |
|`U+07DE`   | Letter           | DUAL         | _null_               | _0_        | &#x07DE; Ka                                   |
|`U+07DF`   | Letter           | DUAL         | _null_               | _0_        | &#x07DF; La                                   |
| | | | | |                                                                                                      			      
|`U+07E0`   | Letter           | DUAL         | _null_               | _0_        | &#x07E0; Na Woloso                            |
|`U+07E1`   | Letter           | DUAL         | _null_               | _0_        | &#x07E1; Ma                                   |
|`U+07E2`   | Letter           | DUAL         | _null_               | _0_        | &#x07E2; Nya                                  |
|`U+07E3`   | Letter           | DUAL         | _null_               | _0_        | &#x07E3; Na                                   |
|`U+07E4`   | Letter           | DUAL         | _null_               | _0_        | &#x07E4; Ha                                   |
|`U+07E5`   | Letter           | DUAL         | _null_               | _0_        | &#x07E5; Wa                                   |
|`U+07E6`   | Letter           | DUAL         | _null_               | _0_        | &#x07E6; Ya                                   |
|`U+07E7`   | Letter           | DUAL         | _null_               | _0_        | &#x07E7; Nya Woloso                           |
|`U+07E8`   | Letter           | DUAL         | _null_               | _0_        | &#x07E8; Jona Ja                              |
|`U+07E9`   | Letter           | DUAL         | _null_               | _0_        | &#x07E9; Jona Cha                             |
|`U+07EA`   | Letter           | DUAL         | _null_               | _0_        | &#x07EA; Jona Ra                              |
|`U+07EB`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07EB; Combining  Short High Tone           |
|`U+07EC`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07EC; Combining  Short Low Tone            |
|`U+07ED`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07ED; Combining  Short Rising Tone         |
|`U+07EE`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07EE; Combining  Long Descending Tone      |
|`U+07EF`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07EF; Combining  Long High Tone            |
| | | | | |                                                                                                     			      
|`U+07F0`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07F0; Combining  Long Low Tone             |
|`U+07F1`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07F1; Combining  Long Rising Tone          |
|`U+07F2`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x07F2; Combining  Nasalization Mark         |
|`U+07F3`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x07F3; Combining  Double Dot Above          |
|`U+07F4`   | Letter modifier  | NON_JOINING  | _null_               | _0_        | &#x07F4; High Tone Apostrophe                 |
|`U+07F5`   | Letter modifier  | NON_JOINING  | _null_               | _0_        | &#x07F5; Low Tone Apostrophe                  |
|`U+07F6`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x07F6; Symbol Oo Dennen                     |
|`U+07F7`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x07F7; Symbol Gbakurunen                    |
|`U+07F8`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x07F8; Comma                                |
|`U+07F9`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x07F9; Exclamation Mark                     |
|`U+07FA`   | Letter modifier  | JOIN_CAUSING | _null_               | _0_        | &#x07FA; Lajanyalan                           |
|`U+07FB`   | _unassigned_     |              |                      |            |                                               |
|`U+07FC`   | _unassigned_     |              |                      |            |                                               |
|`U+07FD`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x07FD; Dantalayan                           |
|`U+07FE`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x07FE; Dorome Sign                          |
|`U+07FF`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x07FF; Taman Sign                           |


## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Arabic text include the dotted-circle placeholder (`U+25CC`), the
combining grapheme joiner (`U+034F`), the zero-width joiner (`U+200D`)
and zero-width non-joiner (`U+200C`), the left-to-right text marker
(`U+200E`) and right-to-left text marker (`U+200F`), and the no-break
space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
combining mark in isolation. Real-world text syllables may also use
other characters, such as hyphens or dashes, in a similar placeholder
fashion; shaping engines should cope with this situation gracefully.


| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                          |
|:----------|:-----------------|:-------------|:---------------------|:-----------|--------------------------------|
|`U+00A0`   | Separator        | NON_JOINING  | _null_               | _0_        | &#x00A0; No-break space        |
|`U+034F`   | Other            | NON_JOINING  | _null_               | _0_        | &#x034F; Combining grapheme joiner |
|`U+200C`   | Other            | NON_JOINING  | _null_               | _0_        | &#x200C; Zero-width non-joiner |
|`U+200D`   | Other            | JOIN_CAUSING | _null_               | _0_        | &#x200D; Zero-width joiner     |
|`U+200E`   | Other            | NON_JOINING  | _null_               | _0_        | &#x200E; Left-to-Right marker  |
|`U+200F`   | Other            | NON_JOINING  | _null_               | _0_        | &#x200F; Right-to-Left marker  |
|`U+2010`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2010; Hyphen                |
|`U+2011`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2011; No-break hyphen       |
|`U+2012`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2012; Figure dash           |
|`U+2013`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2013; En dash               |
|`U+2014`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2014; Em dash               |
|`U+25CC`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x25CC; Dotted circle         |



The combining grapheme joiner (<abbr>CGJ</abbr>) is primarily used to alter the
order in which adjacent marks are positioned during the
mark-reordering stage, in order to adhere to the needs of a
non-default language orthography.
<!--- combining grapheme joiner explanation --->

The zero-width joiner (<abbr>ZWJ</abbr>) is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for dislaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.


<!--- Zero-Width Non Joiner explanation --->

The right-to-left mark (<abbr>RLM</abbr>) and left-to-right mark (<abbr>LRM</abbr>) are used by
the Unicode bidirectionality algorithm (BiDi) to indicate the points
in a text run at which the writing direction changes.


<!--- How shaping is affected by the <abbr>LTR</abbr> and <abbr>RTL</abbr> markers explanation --->


The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as vowel or diacritical marks and "Hamza") in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.
