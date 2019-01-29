# Mongolian character tables #

This document lists the per-character shaping information needed to
[shape Mongolian text](../opentype-shaping-mongolian.md).

**Table of Contents**

  - [Mongolian character table](#mongolian-character-table)
  - [Mongolian Supplement character table](#mongolian-supplement-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Mongolian character table ##

Mongolian glyphs should be classified as in the following
table. Codepoints in the Mongolian block with no assigned meaning are
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

For Mongolian, a subset of marks in the 220 and 230 classes are also
designated _Modifier Combining Marks_ (MCM). These are denoted with
_220_MCM_ and _230_MCM_ in the _Mark class_ column. The MCM marks are
treated differently during the mark-reordering stage.



| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+1800`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1800; Mongolian Birga                      |
|`U+1801`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1801; Mongolian Ellipsis                   |
|`U+1802`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1802; Mongolian Comma                      |
|`U+1803`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1803; Mongolian Full Stop                  |
|`U+1804`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1804; Mongolian Colon                      |
|`U+1805`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1805; Mongolian Four Dots                  |
|`U+1806`   | Punctuation [Pd] | NON_JOINING  | _null_               | _0_        | &#x1806; Todo Soft Hyphen                     |
|`U+1807`   | Punctuation      | DUAL         | _null_               | _0_        | &#x1807; Sibe Syllable Boundary Mark          |
|`U+1808`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1808; Manchu Comma                         |
|`U+1809`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1809; Manchu Full Stop                     |
|`U+180A`   | Punctuation      | JOIN_CAUSING | _null_               | _0_        | &#x180A; Mongolian Nirugu                     |
|`U+180B`   | Mark [Mn]        | TRANSPARENT  | _null_               | _0_        | &#x180B; Free Variation Selector One          |
|`U+180C`   | Mark [Mn]        | TRANSPARENT  | _null_               | _0_        | &#x180C; Free Variation Selector Two          |
|`U+180D`   | Mark [Mn]        | TRANSPARENT  | _null_               | _0_        | &#x180D; Free Variation Selector Three        |
|`U+180E`   | Formatting       | NON_JOINING  | _null_               | _0_        | &#x180E; Mongolian Vowel Separator            |
|`U+180F`   | _unassigned_     |              |                      |            |                                               |
| | | | | |                                                                                  
|`U+1810`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1810; Digit Zero                           |
|`U+1811`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1811; Digit One                            |
|`U+1812`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1812; Digit Two                            |
|`U+1813`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1813; Digit Three                          |
|`U+1814`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1814; Digit Four                           |
|`U+1815`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1815; Digit Five                           |
|`U+1816`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1816; Digit Six                            |
|`U+1817`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1817; Digit Seven                          |
|`U+1818`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1818; Digit Eight                          |
|`U+1819`   | Number           | NON_JOINING  | _null_               | _0_        | &#x1819; Digit Nine                           |
|`U+181A`   | _unassigned_     |              |                      |            |                                               |
|`U+181B`   | _unassigned_     |              |                      |            |                                               |
|`U+181C`   | _unassigned_     |              |                      |            |                                               |
|`U+181D`   | _unassigned_     |              |                      |            |                                               |
|`U+181E`   | _unassigned_     |              |                      |            |                                               |
|`U+181F`   | _unassigned_     |              |                      |            |                                               |
| | | | | |                                                                                  
|`U+1820`   | Letter           | DUAL         | _null_               | _0_        | &#x1820; A                                    |
|`U+1821`   | Letter           | DUAL         | _null_               | _0_        | &#x1821; E                                    |
|`U+1822`   | Letter           | DUAL         | _null_               | _0_        | &#x1822; I                                    |
|`U+1823`   | Letter           | DUAL         | _null_               | _0_        | &#x1823; O                                    |
|`U+1824`   | Letter           | DUAL         | _null_               | _0_        | &#x1824; U                                    |
|`U+1825`   | Letter           | DUAL         | _null_               | _0_        | &#x1825; Oe                                   |
|`U+1827`   | Letter           | DUAL         | _null_               | _0_        | &#x1826; Ue                                   |
|`U+1827`   | Letter           | DUAL         | _null_               | _0_        | &#x1827; Ee                                   |
|`U+1828`   | Letter           | DUAL         | _null_               | _0_        | &#x1828; Na                                   |
|`U+1829`   | Letter           | DUAL         | _null_               | _0_        | &#x1829; Ang                                  |
|`U+182A`   | Letter           | DUAL         | _null_               | _0_        | &#x182A; Ba                                   |
|`U+182B`   | Letter           | DUAL         | _null_               | _0_        | &#x182B; Pa                                   |
|`U+182C`   | Letter           | DUAL         | _null_               | _0_        | &#x182C; Qa                                   |
|`U+182D`   | Letter           | DUAL         | _null_               | _0_        | &#x182D; Ga                                   |
|`U+182E`   | Letter           | DUAL         | _null_               | _0_        | &#x182E; Ma                                   |
|`U+182F`   | Letter           | DUAL         | _null_               | _0_        | &#x182F; La                                   |
| | | | | |                                                                                  
|`U+1830`   | Letter           | DUAL         | _null_               | _0_        | &#x1830; Sa                                   |
|`U+1831`   | Letter           | DUAL         | _null_               | _0_        | &#x1831; Sha                                  |
|`U+1832`   | Letter           | DUAL         | _null_               | _0_        | &#x1832; Ta                                   |
|`U+1833`   | Letter           | DUAL         | _null_               | _0_        | &#x1833; Da                                   |
|`U+1834`   | Letter           | DUAL         | _null_               | _0_        | &#x1834; Cha                                  |
|`U+1835`   | Letter           | DUAL         | _null_               | _0_        | &#x1835; Ja                                   |
|`U+1836`   | Letter           | DUAL         | _null_               | _0_        | &#x1836; Ya                                   |
|`U+1837`   | Letter           | DUAL         | _null_               | _0_        | &#x1837; Ra                                   |
|`U+1838`   | Letter           | DUAL         | _null_               | _0_        | &#x1838; Wa                                   |
|`U+1839`   | Letter           | DUAL         | _null_               | _0_        | &#x1839; Fa                                   |
|`U+183A`   | Letter           | DUAL         | _null_               | _0_        | &#x183A; Ka                                   |
|`U+183B`   | Letter           | DUAL         | _null_               | _0_        | &#x183B; Kha                                  |
|`U+183C`   | Letter           | DUAL         | _null_               | _0_        | &#x183C; Tsa                                  |
|`U+183D`   | Letter           | DUAL         | _null_               | _0_        | &#x183D; Za                                   |
|`U+183E`   | Letter           | DUAL         | _null_               | _0_        | &#x183E; Haa                                  |
|`U+183F`   | Letter           | DUAL         | _null_               | _0_        | &#x183F; Zra                                  |
| | | | | |                                                                                  
|`U+1840`   | Letter           | DUAL         | _null_               | _0_        | &#x1840; Lha                                  |
|`U+1841`   | Letter           | DUAL         | _null_               | _0_        | &#x1841; Zhi                                  |
|`U+1842`   | Letter           | DUAL         | _null_               | _0_        | &#x1842; Chi                                  |
|`U+1843`   | Letter           | DUAL         | _null_               | _0_        | &#x1843; Todo Long Vowel Sign                 |
|`U+1844`   | Letter           | DUAL         | _null_               | _0_        | &#x1844; Todo E                               |
|`U+1845`   | Letter           | DUAL         | _null_               | _0_        | &#x1845; Todo I                               |
|`U+1846`   | Letter           | DUAL         | _null_               | _0_        | &#x1846; Todo O                               |
|`U+1847`   | Letter           | DUAL         | _null_               | _0_        | &#x1847; Todo U                               |
|`U+1848`   | Letter           | DUAL         | _null_               | _0_        | &#x1848; Todo Oe                              |
|`U+1849`   | Letter           | DUAL         | _null_               | _0_        | &#x1849; Todo Ue                              |
|`U+184A`   | Letter           | DUAL         | _null_               | _0_        | &#x184A; Todo Ang                             |
|`U+184B`   | Letter           | DUAL         | _null_               | _0_        | &#x184B; Todo Ba                              |
|`U+184C`   | Letter           | DUAL         | _null_               | _0_        | &#x184C; Todo Pa                              |
|`U+184D`   | Letter           | DUAL         | _null_               | _0_        | &#x184D; Todo Qa                              |
|`U+184E`   | Letter           | DUAL         | _null_               | _0_        | &#x184E; Todo Ga                              |
|`U+184F`   | Letter           | DUAL         | _null_               | _0_        | &#x184F; Todo Ma                              |
| | | | | |                                                                                      
|`U+1850`   | Letter           | DUAL         | _null_               | _0_        | &#x1850; Todo Ta                              |
|`U+1851`   | Letter           | DUAL         | _null_               | _0_        | &#x1851; Todo Da                              |
|`U+1852`   | Letter           | DUAL         | _null_               | _0_        | &#x1852; Todo Cha                             |
|`U+1853`   | Letter           | DUAL         | _null_               | _0_        | &#x1853; Todo Ja                              |
|`U+1854`   | Letter           | DUAL         | _null_               | _0_        | &#x1854; Todo Tsa                             |
|`U+1855`   | Letter           | DUAL         | _null_               | _0_        | &#x1855; Todo Ya                              |
|`U+1856`   | Letter           | DUAL         | _null_               | _0_        | &#x1856; Todo Wa                              |
|`U+1857`   | Letter           | DUAL         | _null_               | _0_        | &#x1857; Todo Ka                              |
|`U+1858`   | Letter           | DUAL         | _null_               | _0_        | &#x1858; Todo Gaa                             |
|`U+1859`   | Letter           | DUAL         | _null_               | _0_        | &#x1859; Todo Haa                             |
|`U+185A`   | Letter           | DUAL         | _null_               | _0_        | &#x185A; Todo Jia                             |
|`U+185B`   | Letter           | DUAL         | _null_               | _0_        | &#x185B; Todo Nia                             |
|`U+185C`   | Letter           | DUAL         | _null_               | _0_        | &#x185C; Todo Dza                             |
|`U+185D`   | Letter           | DUAL         | _null_               | _0_        | &#x185D; Sibe E                               |
|`U+185E`   | Letter           | DUAL         | _null_               | _0_        | &#x185E; Sibe I                               |
|`U+185F`   | Letter           | DUAL         | _null_               | _0_        | &#x185F; Sibe Iy                              |
| | | | | |                                                                                     
|`U+1860`   | Letter           | DUAL         | _null_               | _0_        | &#x1860; Sibe Ue                              |
|`U+1861`   | Letter           | DUAL         | _null_               | _0_        | &#x1861; Sibe U                               |
|`U+1862`   | Letter           | DUAL         | _null_               | _0_        | &#x1862; Sibe Ang                             |
|`U+1863`   | Letter           | DUAL         | _null_               | _0_        | &#x1863; Sibe Ka                              |
|`U+1864`   | Letter           | DUAL         | _null_               | _0_        | &#x1864; Sibe Ga                              |
|`U+1865`   | Letter           | DUAL         | _null_               | _0_        | &#x1865; Sibe Ha                              |
|`U+1866`   | Letter           | DUAL         | _null_               | _0_        | &#x1866; Sibe Pa                              |
|`U+1867`   | Letter           | DUAL         | _null_               | _0_        | &#x1867; Sibe Sha                             |
|`U+1868`   | Letter           | DUAL         | _null_               | _0_        | &#x1868; Sibe Ta                              |
|`U+1869`   | Letter           | DUAL         | _null_               | _0_        | &#x1869; Sibe Da                              |
|`U+186A`   | Letter           | DUAL         | _null_               | _0_        | &#x186A; Sibe Ja                              |
|`U+186B`   | Letter           | DUAL         | _null_               | _0_        | &#x186B; Sibe Fa                              |
|`U+186C`   | Letter           | DUAL         | _null_               | _0_        | &#x186C; Sibe Gaa                             |
|`U+186D`   | Letter           | DUAL         | _null_               | _0_        | &#x186D; Sibe Haa                             |
|`U+186E`   | Letter           | DUAL         | _null_               | _0_        | &#x186E; Sibe Tsa                             |
|`U+186F`   | Letter           | DUAL         | _null_               | _0_        | &#x186F; Sibe Za                              |
| | | | | |                                                                                      
|`U+1870`   | Letter           | DUAL         | _null_               | _0_        | &#x1870; Sibe Raa                             |
|`U+1871`   | Letter           | DUAL         | _null_               | _0_        | &#x1871; Sibe Cha                             |
|`U+1872`   | Letter           | DUAL         | _null_               | _0_        | &#x1872; Sibe Zha                             |
|`U+1873`   | Letter           | DUAL         | _null_               | _0_        | &#x1873; Manchu I                             |
|`U+1874`   | Letter           | DUAL         | _null_               | _0_        | &#x1874; Manchu Ka                            |
|`U+1875`   | Letter           | DUAL         | _null_               | _0_        | &#x1875; Manchu Ra                            |
|`U+1876`   | Letter           | DUAL         | _null_               | _0_        | &#x1876; Manchu Fa                            |
|`U+1877`   | Letter           | DUAL         | _null_               | _0_        | &#x1877; Manchu Zha                           |
|`U+1878`   | Letter           | DUAL         | _null_               | _0_        | &#x1878; Cha With Two Dots                    |
|`U+1879`   | _unassigned_     |              |                      |            |                                               |
|`U+187A`   | _unassigned_     |              |                      |            |                                               |
|`U+187B`   | _unassigned_     |              |                      |            |                                               |
|`U+187C`   | _unassigned_     |              |                      |            |                                               |
|`U+187D`   | _unassigned_     |              |                      |            |                                               |
|`U+187E`   | _unassigned_     |              |                      |            |                                               |
|`U+187F`   | _unassigned_     |              |                      |            |                                               |
| | | | | |                                                                                  
|`U+1880`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x1880; Ali Gali Anusvara One                |
|`U+1881`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x1881; Ali Gali Visarga One                 |
|`U+1882`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x1882; Ali Gali Damaru                      |
|`U+1883`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x1883; Ali Gali Ubadama                     |
|`U+1884`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x1884; Ali Gali Inverted Ubadama            |
|`U+1885`   | Mark [Mn]        | TRANSPARENT  | _null_               | _0_        | &#x1885; Ali Gali Baluda                      |
|`U+1886`   | Mark [Mn]        | TRANSPARENT  | _null_               | _0_        | &#x1886; Ali Gali Three Baluda                |
|`U+1887`   | Letter           | DUAL         | _null_               | _0_        | &#x1887; Ali Gali A                           |
|`U+1888`   | Letter           | DUAL         | _null_               | _0_        | &#x1888; Ali Gali I                           |
|`U+1889`   | Letter           | DUAL         | _null_               | _0_        | &#x1889; Ali Gali Ka                          |
|`U+188A`   | Letter           | DUAL         | _null_               | _0_        | &#x188A; Ali Gali Nga                         |
|`U+188B`   | Letter           | DUAL         | _null_               | _0_        | &#x188B; Ali Gali Ca                          |
|`U+188C`   | Letter           | DUAL         | _null_               | _0_        | &#x188C; Ali Gali Tta                         |
|`U+188D`   | Letter           | DUAL         | _null_               | _0_        | &#x188D; Ali Gali Ttha                        |
|`U+188E`   | Letter           | DUAL         | _null_               | _0_        | &#x188E; Ali Gali Dda                         |
|`U+188F`   | Letter           | DUAL         | _null_               | _0_        | &#x188F; Ali Gali Nna                         |
| | | | | |                                                                                          
|`U+1890`   | Letter           | DUAL         | _null_               | _0_        | &#x1890; Ali Gali Ta                          |
|`U+1891`   | Letter           | DUAL         | _null_               | _0_        | &#x1891; Ali Gali Da                          |
|`U+1892`   | Letter           | DUAL         | _null_               | _0_        | &#x1892; Ali Gali Pa                          |
|`U+1893`   | Letter           | DUAL         | _null_               | _0_        | &#x1893; Ali Gali Pha                         |
|`U+1894`   | Letter           | DUAL         | _null_               | _0_        | &#x1894; Ali Gali Ssa                         |
|`U+1895`   | Letter           | DUAL         | _null_               | _0_        | &#x1895; Ali Gali Zha                         |
|`U+1896`   | Letter           | DUAL         | _null_               | _0_        | &#x1896; Ali Gali Za                          |
|`U+1897`   | Letter           | DUAL         | _null_               | _0_        | &#x1897; Ali Gali Ah                          |
|`U+1898`   | Letter           | DUAL         | _null_               | _0_        | &#x1898; Todo Ali Gali Ta                     |
|`U+1899`   | Letter           | DUAL         | _null_               | _0_        | &#x1899; Todo Ali Gali Zha                    |
|`U+189A`   | Letter           | DUAL         | _null_               | _0_        | &#x189A; Manchu Ali Gali Gha                  |
|`U+189B`   | Letter           | DUAL         | _null_               | _0_        | &#x189B; Manchu Ali Gali Nga                  |
|`U+189C`   | Letter           | DUAL         | _null_               | _0_        | &#x189C; Manchu Ali Gali Ca                   |
|`U+189D`   | Letter           | DUAL         | _null_               | _0_        | &#x189D; Manchu Ali Gali Jha                  |
|`U+189E`   | Letter           | DUAL         | _null_               | _0_        | &#x189E; Manchu Ali Gali Tta                  |
|`U+189F`   | Letter           | DUAL         | _null_               | _0_        | &#x189F; Manchu Ali Gali Ddha                 |
| | | | | |                                                                                                  
|`U+18A0`   | Letter           | DUAL         | _null_               | _0_        | &#x18A0; Manchu Ali Gali Ta                   |
|`U+18A1`   | Letter           | DUAL         | _null_               | _0_        | &#x18A1; Manchu Ali Gali Dha                  |
|`U+18A2`   | Letter           | DUAL         | _null_               | _0_        | &#x18A2; Manchu Ali Gali Ssa                  |
|`U+18A3`   | Letter           | DUAL         | _null_               | _0_        | &#x18A3; Manchu Ali Gali Cya                  |
|`U+18A4`   | Letter           | DUAL         | _null_               | _0_        | &#x18A4; Manchu Ali Gali Zha                  |
|`U+18A5`   | Letter           | DUAL         | _null_               | _0_        | &#x18A5; Manchu Ali Gali Za                   |
|`U+18A6`   | Letter           | DUAL         | _null_               | _0_        | &#x18A6; Ali Gali Half U                      |
|`U+18A7`   | Letter           | DUAL         | _null_               | _0_        | &#x18A7; Ali Gali Half Ya                     |
|`U+18A8`   | Letter           | DUAL         | _null_               | _0_        | &#x18A8; Manchu Ali Gali Bha                  |
|`U+18A9`   | Mark [Mn]        | TRANSPARENT  | _null_               | 228        | &#x18A9; Ali Gali Dagalga                     |
|`U+18AA`   | Letter           | DUAL         | _null_               | _0_        | &#x18AA; Manchu Ali Gali Lha                  |
|`U+18AB`   | _unassigned_     |              |                      |            |                                               |
|`U+18AC`   | _unassigned_     |              |                      |            |                                               |
|`U+18AD`   | _unassigned_     |              |                      |            |                                               |
|`U+18AE`   | _unassigned_     |              |                      |            |                                               |
|`U+18AF`   | _unassigned_     |              |                      |            |                                               |




## Mongolian Supplement character table ##

The Mongolian Supplement block includes variants of the _birga_ mark
used to denote the beginning of a text.

| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+11660`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11660; Birga with Ornament                 |
|`U+11661`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11661; Rotated Birga                       |
|`U+11662`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11662; Double Birga with Ornament          |
|`U+11663`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11663; Triple Birga with Ornament          |
|`U+11664`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11664; Birga with Double Ornament          |
|`U+11665`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11665; Rotated Birga with Ornament         |
|`U+11666`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11666; Rotated Birga with Double Ornament  |
|`U+11667`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11667; Inverted Birga                      |
|`U+11668`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11668; Inverted Birga with Double Ornament |
|`U+11669`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x11669; Swirl Birga                         |
|`U+1166A`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1166A; Swirl Birga with Ornament           |
|`U+1166B`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1166B; Swirl Birga with Double Ornament    |
|`U+1166C`  | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x1166C; Turned Swirl Birga with Double Ornament|
|`U+1166D`  | _unassigned_     |              |                      |            |                                               |
|`U+1166E`  | _unassigned_     |              |                      |            |                                               |
|`U+1166F`  | _unassigned_     |              |                      |            |                                               |
| | | | | |
|`U+11670`  | _unassigned_     |              |                      |            |                                               |
|`U+11671`  | _unassigned_     |              |                      |            |                                               |
|`U+11672`  | _unassigned_     |              |                      |            |                                               |
|`U+11673`  | _unassigned_     |              |                      |            |                                               |
|`U+11674`  | _unassigned_     |              |                      |            |                                               |
|`U+11675`  | _unassigned_     |              |                      |            |                                               |
|`U+11676`  | _unassigned_     |              |                      |            |                                               |
|`U+11677`  | _unassigned_     |              |                      |            |                                               |
|`U+11678`  | _unassigned_     |              |                      |            |                                               |
|`U+11679`  | _unassigned_     |              |                      |            |                                               |
|`U+1167A`  | _unassigned_     |              |                      |            |                                               |
|`U+1167B`  | _unassigned_     |              |                      |            |                                               |
|`U+1167C`  | _unassigned_     |              |                      |            |                                               |
|`U+1167D`  | _unassigned_     |              |                      |            |                                               |
|`U+1167E`  | _unassigned_     |              |                      |            |                                               |
|`U+1167F`  | _unassigned_     |              |                      |            |                                               |


## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Mongolian text include the dotted-circle placeholder (`U+25CC`), the
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
|`U+200C`   | Other            | NON_JOINING  | _null_               | _0_        | &#x200C; Zero-width non-joiner |
|`U+200D`   | Other            | JOIN_CAUSING | _null_               | _0_        | &#x200D; Zero-width joiner     |
|`U+2010`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2010; Hyphen                |
|`U+2011`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2011; No-break hyphen       |
|`U+2012`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2012; Figure dash           |
|`U+2013`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2013; En dash               |
|`U+2014`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x2014; Em dash               |
|`U+202F`   | Separator        | NON_JOINING  | _null_               | _0_        | &#x202F; Narrow No-Break Space |
|`U+25CC`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x25CC; Dotted circle         |
| | | | | | |


The zero-width joiner (ZWJ) is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for dislaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.


<!--- Zero-Width Non Joiner explanation --->

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as vowel or diacritical marks and "Hamza") in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.

The narrow no-break space is used in Mongolian to insert a small gap
between a word and its suffix. 
