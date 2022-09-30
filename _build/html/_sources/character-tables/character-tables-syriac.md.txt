# Syriac character tables #

This document lists the per-character shaping information needed to
[shape Syriac text](../opentype-shaping-syriac.md).

**Table of Contents**

  - [Syriac character table](#syriac-character-table)
  - [Syriac Supplement character table](#syriac-supplement-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Syriac character table ##

Syriac glyphs should be classified as in the following
table. Codepoints in the Syriac block with no assigned meaning are
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

The _Mark class_ column indicates the Canonical Combining Class
for the codepoint.  Marks are assigned non-zero combining classes so
that sequences of adjacent marks can be reordered as required by the
orthography. 

For Syriac, a subset of marks in the 220 and 230 classes are also
designated _Modifier Combining Marks_ (MCM). These are denoted with
_220_MCM_ and _230_MCM_ in the _Mark class_ column. The MCM marks are
treated differently during the mark-reordering stage.



| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+0700`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0700; End of Paragraph                     |
|`U+0701`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0701; Supralinear Full Stop                |
|`U+0702`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0702; Sublinear Full Stop                  |
|`U+0703`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0703; Supralinear Colon                    |
|`U+0704`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0704; Sublinear Colon                      |
|`U+0705`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0705; Horizontal Colon                     |
|`U+0706`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0706; Colon Skewed Left                    |
|`U+0707`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0707; Colon Skewed Right                   |
|`U+0708`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0708; Supralinear Colon Skewed Left        |
|`U+0709`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0709; Sublinear Colon Skewed Right         |
|`U+070A`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x070A; Contraction                          |
|`U+070B`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x070B; Harklean Obelus                      |
|`U+070C`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x070C; Harklean Metobelus                   |
|`U+070D`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x070D; Harklean Asteriscus                  |
|`U+070E`   | _unassigned_     |              |                      |            |                                               |
|`U+070F`   | Other            | TRANSPARENT  | _null_               | _0_        | &#x070F; Syriac Abbreviation Mark             |
| | | | | |                                                                                                                      
|`U+0710`   | Letter           | RIGHT        | ALAPH                | _0_        | &#x0710; Alaph                                |
|`U+0711`   | Mark [Mn]        | TRANSPARENT  | _null_               | 36         | &#x0711; Superscript Alaph                    |
|`U+0712`   | Letter           | DUAL         | BETH                 | _0_        | &#x0712; Beth                                 |
|`U+0713`   | Letter           | DUAL         | GAMAL                | _0_        | &#x0713; Gamal                                |
|`U+0714`   | Letter           | DUAL         | GAMAL                | _0_        | &#x0714; Gamal Garshuni                       |
|`U+0715`   | Letter           | RIGHT        | DALATH_RISH          | _0_        | &#x0715; Dalath                               |
|`U+0716`   | Letter           | RIGHT        | DALATH_RISH          | _0_        | &#x0716; Dotless Dalath Rish                  |
|`U+0717`   | Letter           | RIGHT        | HE                   | _0_        | &#x0717; He                                   |
|`U+0718`   | Letter           | RIGHT        | SYRIAC_WAW           | _0_        | &#x0718; Waw                                  |
|`U+0719`   | Letter           | RIGHT        | ZAIN                 | _0_        | &#x0719; Zain                                 |
|`U+071A`   | Letter           | DUAL         | HETH                 | _0_        | &#x071A; Heth                                 |
|`U+071B`   | Letter           | DUAL         | TETH                 | _0_        | &#x071B; Teth                                 |
|`U+071C`   | Letter           | DUAL         | TETH                 | _0_        | &#x071C; Teth Garshuni                        |
|`U+071D`   | Letter           | DUAL         | YUDH                 | _0_        | &#x071D; Yudh                                 |
|`U+071E`   | Letter           | RIGHT        | YUDH_HE              | _0_        | &#x071E; Yudh He                              |
|`U+071F`   | Letter           | DUAL         | KAPH                 | _0_        | &#x071F; Kaph                                 |
| | | | | |                                                                                                                      
|`U+0720`   | Letter           | DUAL         | LAMADH               | _0_        | &#x0720; Lamadh                               |
|`U+0721`   | Letter           | DUAL         | MIM                  | _0_        | &#x0721; Mim                                  |
|`U+0722`   | Letter           | DUAL         | NUN                  | _0_        | &#x0722; Nun                                  |
|`U+0723`   | Letter           | DUAL         | SEMKATH              | _0_        | &#x0723; Semkath                              |
|`U+0724`   | Letter           | DUAL         | FINAL_SEMKATH        | _0_        | &#x0724; Final Semkath                        |
|`U+0725`   | Letter           | DUAL         | E                    | _0_        | &#x0725; E                                    |
|`U+0727`   | Letter           | DUAL         | PE                   | _0_        | &#x0727; Pe                                   |
|`U+0727`   | Letter           | DUAL         | REVERSED_PE          | _0_        | &#x0727; Reversed Pe                          |
|`U+0728`   | Letter           | RIGHT        | SADHE                | _0_        | &#x0728; Sadhe                                |
|`U+0729`   | Letter           | DUAL         | QAPH                 | _0_        | &#x0729; Qaph                                 |
|`U+072A`   | Letter           | RIGHT        | DALATH_RISH          | _0_        | &#x072A; Rish                                 |
|`U+072B`   | Letter           | DUAL         | SHIN                 | _0_        | &#x072B; Shin                                 |
|`U+072C`   | Letter           | RIGHT        | TAW                  | _0_        | &#x072C; Taw                                  |
|`U+072D`   | Letter           | DUAL         | BETH                 | _0_        | &#x072D; Persian Bheth                        |
|`U+072E`   | Letter           | DUAL         | GAMAL                | _0_        | &#x072E; Persian Ghamal                       |
|`U+072F`   | Letter           | RIGHT        | DALATH_RISH          | _0_        | &#x072F; Persian Dhalath                      |
| | | | | |                                                                                                                      
|`U+0730`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0730; Pthaha Above                         |
|`U+0731`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0731; Pthaha Below                         |
|`U+0732`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0732; Pthaha Dotted                        |
|`U+0733`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0733; Zqapha Above                         |
|`U+0734`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0734; Zqapha Below                         |
|`U+0735`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0735; Zqapha Dotted                        |
|`U+0736`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0736; Rbasa Above                          |
|`U+0737`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0737; Rbasa Below                          |
|`U+0738`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0738; Dotted Zlama Horizontal              |
|`U+0739`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0739; Dotted Zlama Angular                 |
|`U+073A`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x073A; Hbasa Above                          |
|`U+073B`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x073B; Hbasa Below                          |
|`U+073C`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x073C; Hbasa-Esasa Dotted                   |
|`U+073D`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x073D; Esasa Above                          |
|`U+073E`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x073E; Esasa Below                          |
|`U+073F`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x073F; Rwaha                                |
| | | | | |                                                                                                                      
|`U+0740`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0740; Feminine Dot                         |
|`U+0741`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0741; Qushshaya                            |
|`U+0742`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0742; Rukkakha                             |
|`U+0743`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0743; Two Vertical Dots Above              |
|`U+0744`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0744; Two Vertical Dots Below              |
|`U+0745`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0745; Three Dots Above                     |
|`U+0746`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0746; Three Dots Below                     |
|`U+0747`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0747; Oblique Line Above                   |
|`U+0748`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0748; Oblique Line Below                   |
|`U+0749`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0749; Music                                |
|`U+074A`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x074A; Barrekh                              |
|`U+074B`   | _unassigned_     |              |                      |            |                                               |
|`U+074C`   | _unassigned_     |              |                      |            |                                               |
|`U+074D`   | Letter           | RIGHT        | ZHAIN                | _0_        | &#x074D; Sogdian Zhain                        |
|`U+074E`   | Letter           | DUAL         | KHAPH                | _0_        | &#x074E; Sogdian Khaph                        |
|`U+074F`   | Letter           | DUAL         | FE                   | _0_        | &#x074F; Sogdian Fe                           |




## Syriac Supplement character table ##

The Syriac Supplement block includes letters needed to write Suriyani
Malayalam, also known as Garshuni or Syriac Malayalam.

| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+0860`   | Letter           | DUAL         | MALAYALAM_NGA        | _0_        | &#x0860; Malayalam Nga                        |
|`U+0861`   | Letter           | NON_JOINING  | MALAYALAM_JA         | _0_        | &#x0861; Malayalam Ja                         |
|`U+0862`   | Letter           | DUAL         | MALAYALAM_NYA        | _0_        | &#x0862; Malayalam Nya                        |
|`U+0863`   | Letter           | DUAL         | MALAYALAM_TTA        | _0_        | &#x0863; Malayalam Tta                        |
|`U+0864`   | Letter           | DUAL         | MALAYALAM_NNA        | _0_        | &#x0864; Malayalam Nna                        |
|`U+0865`   | Letter           | DUAL         | MALAYALAM_NNNA       | _0_        | &#x0865; Malayalam Nnna                       |
|`U+0866`   | Letter           | NON_JOINING  | MALAYALAM_BHA        | _0_        | &#x0866; Malayalam Bha                        |
|`U+0867`   | Letter           | RIGHT        | MALAYALAM_RA         | _0_        | &#x0867; Malayalam Ra                         |
|`U+0868`   | Letter           | DUAL         | MALAYALAM_LLA        | _0_        | &#x0868; Malayalam Lla                        |
|`U+0869`   | Letter           | RIGHT        | MALAYALAM_LLLA       | _0_        | &#x0869; Malayalam Llla                       |
|`U+086A`   | Letter           | RIGHT        | MALAYALAM_SSA        | _0_        | &#x086A; Malayalam Ssa                        |
|`U+086B`   | _unassigned_     |              |                      |            |                                               |
|`U+086C`   | _unassigned_     |              |                      |            |                                               |
|`U+086D`   | _unassigned_     |              |                      |            |                                               |
|`U+086E`   | _unassigned_     |              |                      |            |                                               |
|`U+086F`   | _unassigned_     |              |                      |            |                                               |



## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Syriac text include the dotted-circle placeholder (`U+25CC`), the
combining grapheme joiner (`U+034F`), the zero-width joiner (`U+200D`)
and zero-width non-joiner (`U+200C`), the left-to-right text marker
(`U+200E`) and right-to-left text marker (`U+200F`), and the no-break
space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
combining mark in isolation. Real-world text syllables may also use
other characters, such as hyphens or dashes, in a similar placeholder
fashion; shaping engines should cope with this situation gracefully.

In addition, Syriac text runs may include the "Tatweel" or kashida
codepoint (`U+0640`) from the Arabic block, because the Syriac block
does not encode a separate kashida character.


| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                          |
|:----------|:-----------------|:-------------|:---------------------|:-----------|--------------------------------|
|`U+00A0`   | Separator        | NON_JOINING  | _null_               | _0_        | &#x00A0; No-break space        |
|`U+034F`   | Other            | NON_JOINING  | _null_               | _0_        | &#x034F; Combining grapheme joiner |
|`U+0640`   | Letter modifier  | JOIN_CAUSING | _null_               | _0_        | &#x0640; Arabic Tatweel        |
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
| | | | | | |


The combining grapheme joiner (CGJ) is primarily used to alter the
order in which adjacent marks are positioned during the
mark-reordering stage, in order to adhere to the needs of a
non-default language orthography.
<!--- combining grapheme joiner explanation --->

The zero-width joiner (ZWJ) is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for dislaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.


<!--- Zero-Width Non Joiner explanation --->

The right-to-left mark (RLM) and left-to-right mark (LRM) are used by
the Unicode bidirectionality algorithm (BiDi) to indicate the points
in a text run at which the writing direction changes.


<!--- How shaping is affected by the LTR and RTL markers explanation --->


The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as vowel or diacritical marks and "Hamza") in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.
