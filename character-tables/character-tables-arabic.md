# Arabic character tables #

This document lists the per-character shaping information needed to
[shape Arabic text](opentype-shaping-arabic.md).

**Table of Contents**

  - [Arabic character table](#arabic-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)


## Arabic character table ##

Arabic glyphs should be classified as in the following
table. Codepoints in the Arabic block with no assigned meaning are
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

For Arabic, a subset of marks in the 220 and 230 classes are also
designated _Modifier Combining Marks_ (MCM). These are denoted with
_220_MCM_ and _230_MCM_ in the _Mark class_ column. The MCM marks are
treated differently during the mark-reordering stage.



| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+0600`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0600; Number Sign                          |
|`U+0601`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0601; Sign Sanah                           |
|`U+0602`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0602; Footnote Marker                      |
|`U+0603`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0603; Sign Safha                           |
|`U+0604`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0604; Sign Samvat                          |
|`U+0605`   | Other            | NON_JOINING  | _null_               | _0_        | &#x0605; Number Mark Above                    |
|`U+0606`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x0606; Cube Root                            |
|`U+0607`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x0607; Fourth Root                          |
|`U+0608`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x0608; Ray                                  |
|`U+0609`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x0609; Per Mille                            |
|`U+060A`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x060A; Per Ten Thousand                     |
|`U+060B`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x060B; Afghani Sign                         |
|`U+060C`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x060C; Comma                                |
|`U+060D`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x060D; Date Separator                       |
|`U+060E`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x060E; Poetic Verse Sign                    |
|`U+060F`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x060F; Sign Misra                           |
| | | | | |                                                                                                                      
|`U+0610`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0610; Sign Sallallahou Alayhe Wassallam    |
|`U+0611`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0611; Sign Alayhe Assallam                 |
|`U+0612`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0612; Sign Rahmatullah Alayhe              |
|`U+0613`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0613; Sign Radi Allahou Anhu               |
|`U+0614`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0614; Sign Takhallus                       |
|`U+0615`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0615; Small High Tah                       |
|`U+0616`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0616; Small High Alef Lam Yeh              |
|`U+0617`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0617; Small High Zain                      |
|`U+0618`   | Mark [Mn]        | TRANSPARENT  | _null_               | 30         | &#x0618; Small Fatha                          |
|`U+0619`   | Mark [Mn]        | TRANSPARENT  | _null_               | 31         | &#x0619; Small Damma                          |
|`U+061A`   | Mark [Mn]        | TRANSPARENT  | _null_               | 32         | &#x061A; Small Kasra                          |
|`U+061B`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x061B; Semicolon                            |
|`U+061C`   | Other            | TRANSPARENT  | _null_               | _0_        | &#x061C; Arabic Letter Mark                   |
|`U+061D`   | _unassigned_     |              |                      |            |                                               |
|`U+061E`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x061E; Triple Dot Punctuation Mark          |
|`U+061F`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x061F; Question Mark                        |
| | | | | |                                                                                                                       
|`U+0620`   | Letter           | DUAL         | YEH                  | _0_        | &#x0620; Dotless Yeh With Separate Ring Below |
|`U+0621`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x0621; Hamza                                |
|`U+0622`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0622; Alef With Madda Above                |
|`U+0623`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0623; Alef With Hamza Above                |
|`U+0624`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0624; Waw With Hamza Above                 |
|`U+0625`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0625; Alef With Hamza Below                |
|`U+0626`   | Letter           | DUAL         | YEH                  | _0_        | &#x0626; Dotless Yeh With Hamza Above         |
|`U+0627`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0627; Alef                                 |
|`U+0628`   | Letter           | DUAL         | BEH                  | _0_        | &#x0628; Beh                                  |
|`U+0629`   | Letter           | RIGHT        | TEH_MARBUTA          | _0_        | &#x0629; Teh Marbuta                          |
|`U+062A`   | Letter           | DUAL         | BEH                  | _0_        | &#x062A; Dotless Beh With 2 Dots Above        |
|`U+062B`   | Letter           | DUAL         | BEH                  | _0_        | &#x062B; Dotless Beh With 3 Dots Above        |
|`U+062C`   | Letter           | DUAL         | HAH                  | _0_        | &#x062C; Hah With Dot Below                   |
|`U+062D`   | Letter           | DUAL         | HAH                  | _0_        | &#x062D; Hah                                  |
|`U+062E`   | Letter           | DUAL         | HAH                  | _0_        | &#x062E; Hah With Dot Above                   |
|`U+062F`   | Letter           | RIGHT        | DAL                  | _0_        | &#x062F; Dal                                  |
| | | | | |                                                                                                                       
|`U+0630`   | Letter           | RIGHT        | DAL                  | _0_        | &#x0630; Dal With Dot Above                   |
|`U+0631`   | Letter           | RIGHT        | REH                  | _0_        | &#x0631; Reh                                  |
|`U+0632`   | Letter           | RIGHT        | REH                  | _0_        | &#x0632; Reh With Dot Above                   |
|`U+0633`   | Letter           | DUAL         | SEEN                 | _0_        | &#x0633; Seen                                 |
|`U+0634`   | Letter           | DUAL         | SEEN                 | _0_        | &#x0634; Seen With 3 Dots Above               |
|`U+0635`   | Letter           | DUAL         | SAD                  | _0_        | &#x0635; Sad                                  |
|`U+0636`   | Letter           | DUAL         | SAD                  | _0_        | &#x0636; Sad With Dot Above                   |
|`U+0637`   | Letter           | DUAL         | TAH                  | _0_        | &#x0637; Tah                                  |
|`U+0638`   | Letter           | DUAL         | TAH                  | _0_        | &#x0638; Tah With Dot Above                   |
|`U+0639`   | Letter           | DUAL         | AIN                  | _0_        | &#x0639; Ain                                  |
|`U+063A`   | Letter           | DUAL         | AIN                  | _0_        | &#x063A; Ain With Dot Above                   |
|`U+063B`   | Letter           | DUAL         | GAF                  | _0_        | &#x063B; Keheh With 2 Dots Above              |
|`U+063C`   | Letter           | DUAL         | GAF                  | _0_        | &#x063C; Keheh With 3 Dots Below              |
|`U+063D`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x063D; Farsi Yeh With Inverted V Above      |
|`U+063E`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x063E; Farsi Yeh With 2 Dots Above          |
|`U+063F`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x063F; Farsi Yeh With 3 Dots Above          |
| | | | | |                                                                                                                       
|`U+0640`   | Letter modifier  | JOIN_CAUSING | _null_               | _0_        | &#x0640; Tatweel                              |
|`U+0641`   | Letter           | DUAL         | FEH                  | _0_        | &#x0641; Feh                                  |
|`U+0642`   | Letter           | DUAL         | QAF                  | _0_        | &#x0642; Qaf                                  |
|`U+0643`   | Letter           | DUAL         | KAF                  | _0_        | &#x0643; Kaf                                  |
|`U+0644`   | Letter           | DUAL         | LAM                  | _0_        | &#x0644; Lam                                  |
|`U+0645`   | Letter           | DUAL         | MEEM                 | _0_        | &#x0645; Meem                                 |
|`U+0646`   | Letter           | DUAL         | NOON                 | _0_        | &#x0646; Noon                                 |
|`U+0647`   | Letter           | DUAL         | HEH                  | _0_        | &#x0647; Heh                                  |
|`U+0648`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0648; Waw                                  |
|`U+0649`   | Letter           | DUAL         | YEH                  | _0_        | &#x0649; Dotless Yeh                          |
|`U+064A`   | Letter           | DUAL         | YEH                  | _0_        | &#x064A; Yeh                                  |
|`U+064B`   | Mark [Mn]        | TRANSPARENT  | _null_               | 27         | &#x064B; Fathatan                             |
|`U+064C`   | Mark [Mn]        | TRANSPARENT  | _null_               | 28         | &#x064C; Dammatan                             |
|`U+064D`   | Mark [Mn]        | TRANSPARENT  | _null_               | 29         | &#x064D; Kasratan                             |
|`U+064E`   | Mark [Mn]        | TRANSPARENT  | _null_               | 30         | &#x064E; Fatha                                |
|`U+064F`   | Mark [Mn]        | TRANSPARENT  | _null_               | 31         | &#x064F; Damma                                |
| | | | | |                                                                                                                      
|`U+0650`   | Mark [Mn]        | TRANSPARENT  | _null_               | 32         | &#x0650; Kasra                                |
|`U+0651`   | Mark [Mn]        | TRANSPARENT  | _null_               | 33         | &#x0651; Shadda                               |
|`U+0652`   | Mark [Mn]        | TRANSPARENT  | _null_               | 34         | &#x0652; Sukun                                |
|`U+0653`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0653; Maddah Above                         |
|`U+0654`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230_MCM    | &#x0654; Hamza Above                          |
|`U+0655`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220_MCM    | &#x0655; Hamza Below                          |
|`U+0656`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x0656; Subscript Alef                       |
|`U+0657`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0657; Inverted Damma                       |
|`U+0658`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230_MCM    | &#x0658; Noon Ghunna                          |
|`U+0659`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0659; Zwarakay                             |
|`U+065A`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x065A; Vowel Sign Small V Above             |
|`U+065B`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x065B; Vowel Sign Inverted Small V Above    |
|`U+065C`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x065C; Vowel Sign Dot Below                 |
|`U+065D`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x065D; Reversed Damma                       |
|`U+065E`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x065E; Fatha with Two Dots                  |
|`U+065F`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x065F; Wavy Hamza Below                     |
| | | | | |                                                                                                                      
|`U+0660`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0660; Digit Zero                           |
|`U+0661`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0661; Digit One                            |
|`U+0662`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0662; Digit Two                            |
|`U+0663`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0663; Digit Three                          |
|`U+0664`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0664; Digit Four                           |
|`U+0665`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0665; Digit Five                           |
|`U+0666`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0666; Digit Six                            |
|`U+0667`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0667; Digit Seven                          |
|`U+0668`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0668; Digit Eight                          |
|`U+0669`   | Number           | NON_JOINING  | _null_               | _0_        | &#x0669; Digit Nine                           |
|`U+066A`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x066A; Percent Sign                         |
|`U+066B`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x066B; Decimal Separator                    |
|`U+066C`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x066C; Thousands Separator                  |
|`U+066D`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x066D; Five Pointed Star                    |
|`U+066E`   | Letter           | DUAL         | BEH                  | _0_        | &#x066E; Dotless Beh                          |
|`U+066F`   | Letter           | DUAL         | QAF                  | _0_        | &#x066F; Dotless Qaf                          |
| | | | | |                                                                                                                      
|`U+0670`   | Mark [Mn]        | TRANSPARENT  | _null_               | 35         | &#x0670; Superscript Alef                     |
|`U+0671`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0671; Alef With Wasla Above                |
|`U+0672`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0672; Alef With Wavy Hamza Above           |
|`U+0673`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0673; Alef With Wavy Hamza Below           |
|`U+0674`   | Letter           | NON_JOINING  | _null_               | _0_        | &#x0674; High Hamza                           |
|`U+0675`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0675; High Hamza Alef                      |
|`U+0676`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0676; High Hamza Waw                       |
|`U+0677`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0677; High Hamza Waw With Damma Above      |
|`U+0678`   | Letter           | DUAL         | YEH                  | _0_        | &#x0678; High Hamza Dotless Yeh               |
|`U+0679`   | Letter           | DUAL         | BEH                  | _0_        | &#x0679; Dotless Beh With Tah Above           |
|`U+067A`   | Letter           | DUAL         | BEH                  | _0_        | &#x067A; Dotless Beh With Vertical 2 Dots Above|
|`U+067B`   | Letter           | DUAL         | BEH                  | _0_        | &#x067B; Dotless Beh With Vertical 2 Dots Below|
|`U+067C`   | Letter           | DUAL         | BEH                  | _0_        | &#x067C; Dotless Beh With Attached Ring Below And 2 Dots Above|
|`U+067D`   | Letter           | DUAL         | BEH                  | _0_        | &#x067D; Dotless Beh With Inverted 3 Dots Above|
|`U+067E`   | Letter           | DUAL         | BEH                  | _0_        | &#x067E; Dotless Beh With 3 Dots Below        |
|`U+067F`   | Letter           | DUAL         | BEH                  | _0_        | &#x067F; Dotless Beh With 4 Dots Above        |
| | | | | |                                                                                                                      
|`U+0680`   | Letter           | DUAL         | BEH                  | _0_        | &#x0680; Dotless Beh With 4 Dots Below        |
|`U+0681`   | Letter           | DUAL         | HAH                  | _0_        | &#x0681; Hah With Hamza Above                 |
|`U+0682`   | Letter           | DUAL         | HAH                  | _0_        | &#x0682; Hah With Vertical 2 Dots Above       |
|`U+0683`   | Letter           | DUAL         | HAH                  | _0_        | &#x0683; Hah With 2 Dots Below                |
|`U+0684`   | Letter           | DUAL         | HAH                  | _0_        | &#x0684; Hah With Vertical 2 Dots Below       |
|`U+0685`   | Letter           | DUAL         | HAH                  | _0_        | &#x0685; Hah With 3 Dots Above                |
|`U+0686`   | Letter           | DUAL         | HAH                  | _0_        | &#x0686; Hah With 3 Dots Below                |
|`U+0687`   | Letter           | DUAL         | HAH                  | _0_        | &#x0687; Hah With 4 Dots Below                |
|`U+0688`   | Letter           | RIGHT        | DAL                  | _0_        | &#x0688; Dal With Tah Above                   |
|`U+0689`   | Letter           | RIGHT        | DAL                  | _0_        | &#x0689; Dal With Attached Ring Below         |
|`U+068A`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068A; Dal With Dot Below                   |
|`U+068B`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068B; Dal With Dot Below And Tah Above     |
|`U+068C`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068C; Dal With 2 Dots Above                |
|`U+068D`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068D; Dal With 2 Dots Below                |
|`U+068E`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068E; Dal With 3 Dots Above                |
|`U+068F`   | Letter           | RIGHT        | DAL                  | _0_        | &#x068F; Dal With Inverted 3 Dots Above       |
| | | | | |                                                                                                                      
|`U+0690`   | Letter           | RIGHT        | DAL                  | _0_        | &#x0690; Dal With 4 Dots Above                |
|`U+0691`   | Letter           | RIGHT        | REH                  | _0_        | &#x0691; Reh With Tah Above                   |
|`U+0692`   | Letter           | RIGHT        | REH                  | _0_        | &#x0692; Reh With V Above                     |
|`U+0693`   | Letter           | RIGHT        | REH                  | _0_        | &#x0693; Reh With Attached Ring Below         |
|`U+0694`   | Letter           | RIGHT        | REH                  | _0_        | &#x0694; Reh With Dot Below                   |
|`U+0695`   | Letter           | RIGHT        | REH                  | _0_        | &#x0695; Reh With V Below                     |
|`U+0696`   | Letter           | RIGHT        | REH                  | _0_        | &#x0696; Reh With Dot Below And Dot Within    |
|`U+0697`   | Letter           | RIGHT        | REH                  | _0_        | &#x0697; Reh With 2 Dots Above                |
|`U+0698`   | Letter           | RIGHT        | REH                  | _0_        | &#x0698; Reh With 3 Dots Above                |
|`U+0699`   | Letter           | RIGHT        | REH                  | _0_        | &#x0699; Reh With 4 Dots Above                |
|`U+069A`   | Letter           | DUAL         | SEEN                 | _0_        | &#x069A; Seen With Dot Below And Dot Above    |
|`U+069B`   | Letter           | DUAL         | SEEN                 | _0_        | &#x069B; Seen With 3 Dots Below               |
|`U+069C`   | Letter           | DUAL         | SEEN                 | _0_        | &#x069C; Seen With 3 Dots Below And 3 Dots Above|
|`U+069D`   | Letter           | DUAL         | SAD                  | _0_        | &#x069D; Sad With 2 Dots Below                |
|`U+069E`   | Letter           | DUAL         | SAD                  | _0_        | &#x069E; Sad With 3 Dots Above                |
|`U+069F`   | Letter           | DUAL         | TAH                  | _0_        | &#x069F; Tah With 3 Dots Above                |
| | | | | |                                                                                                                      
|`U+06A0`   | Letter           | DUAL         | AIN                  | _0_        | &#x06A0; Ain With 3 Dots Above                |
|`U+06A1`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A1; Dotless Feh                          |
|`U+06A2`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A2; Dotless Feh With Dot Below           |
|`U+06A3`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A3; Feh With Dot Below                   |
|`U+06A4`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A4; Dotless Feh With 3 Dots Above        |
|`U+06A5`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A5; Dotless Feh With 3 Dots Below        |
|`U+06A6`   | Letter           | DUAL         | FEH                  | _0_        | &#x06A6; Dotless Feh With 4 Dots Above        |
|`U+06A7`   | Letter           | DUAL         | QAF                  | _0_        | &#x06A7; Dotless Qaf With Dot Above           |
|`U+06A8`   | Letter           | DUAL         | QAF                  | _0_        | &#x06A8; Dotless Qaf With 3 Dots Above        |
|`U+06A9`   | Letter           | DUAL         | GAF                  | _0_        | &#x06A9; Keheh                                |
|`U+06AA`   | Letter           | DUAL         | SWASH_KAF            | _0_        | &#x06AA; Swash Kaf                            |
|`U+06AB`   | Letter           | DUAL         | GAF                  | _0_        | &#x06AB; Keheh With Attached Ring Below       |
|`U+06AC`   | Letter           | DUAL         | KAF                  | _0_        | &#x06AC; Kaf With Dot Above                   |
|`U+06AD`   | Letter           | DUAL         | KAF                  | _0_        | &#x06AD; Kaf With 3 Dots Above                |
|`U+06AE`   | Letter           | DUAL         | KAF                  | _0_        | &#x06AE; Kaf With 3 Dots Below                |
|`U+06AF`   | Letter           | DUAL         | GAF                  | _0_        | &#x06AF; Gaf                                  |
| | | | | |                                                                                                                     
|`U+06B0`   | Letter           | DUAL         | GAF                  | _0_        | &#x06B0; Gaf With Attached Ring Below         |
|`U+06B1`   | Letter           | DUAL         | GAF                  | _0_        | &#x06B1; Gaf With 2 Dots Above                |
|`U+06B2`   | Letter           | DUAL         | GAF                  | _0_        | &#x06B2; Gaf With 2 Dots Below                |
|`U+06B3`   | Letter           | DUAL         | GAF                  | _0_        | &#x06B3; Gaf With Vertical 2 Dots Below       |
|`U+06B4`   | Letter           | DUAL         | GAF                  | _0_        | &#x06B4; Gaf With 3 Dots Above                |
|`U+06B5`   | Letter           | DUAL         | LAM                  | _0_        | &#x06B5; Lam With V Above                     |
|`U+06B6`   | Letter           | DUAL         | LAM                  | _0_        | &#x06B6; Lam With Dot Above                   |
|`U+06B7`   | Letter           | DUAL         | LAM                  | _0_        | &#x06B7; Lam With 3 Dots Above                |
|`U+06B8`   | Letter           | DUAL         | LAM                  | _0_        | &#x06B8; Lam With 3 Dots Below                |
|`U+06B9`   | Letter           | DUAL         | NOON                 | _0_        | &#x06B9; Noon With Dot Below                  |
|`U+06BA`   | Letter           | DUAL         | NOON                 | _0_        | &#x06BA; Dotless Noon                         |
|`U+06BB`   | Letter           | DUAL         | NOON                 | _0_        | &#x06BB; Dotless Noon With Tah Above          |
|`U+06BC`   | Letter           | DUAL         | NOON                 | _0_        | &#x06BC; Noon With Attached Ring Below        |
|`U+06BD`   | Letter           | DUAL         | NYA                  | _0_        | &#x06BD; Nya                                  |
|`U+06BE`   | Letter           | DUAL         | KNOTTED_HEH          | _0_        | &#x06BE; Knotted Heh                          |
|`U+06BF`   | Letter           | DUAL         | HAH                  | _0_        | &#x06BF; Hah With 3 Dots Below And Dot Above  |
| | | | | |                                                                                                                      
|`U+06C0`   | Letter           | RIGHT        | TEH_MARBUTA          | _0_        | &#x06C0; Dotless Teh Marbuta With Hamza Above |
|`U+06C1`   | Letter           | DUAL         | HEH_GOAL             | _0_        | &#x06C1; Heh Goal                             |
|`U+06C2`   | Letter           | DUAL         | HEH_GOAL             | _0_        | &#x06C2; Heh Goal With Hamza Above            |
|`U+06C3`   | Letter           | RIGHT        | TEH_MARBUTA_GOAL     | _0_        | &#x06C3; Teh Marbuta Goal                     |
|`U+06C4`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C4; Waw With Attached Ring Within        |
|`U+06C5`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C5; Waw With Bar                         |
|`U+06C6`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C6; Waw With V Above                     |
|`U+06C7`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C7; Waw With Damma Above                 |
|`U+06C8`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C8; Waw With Alef Above                  |
|`U+06C9`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06C9; Waw With Inverted V Above            |
|`U+06CA`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06CA; Waw With 2 Dots Above                |
|`U+06CB`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06CB; Waw With 3 Dots Above                |
|`U+06CC`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x06CC; Farsi Yeh                            |
|`U+06CD`   | Letter           | RIGHT        | YEH_WITH_TAIL        | _0_        | &#x06CD; Yeh With Tail                        |
|`U+06CE`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x06CE; Farsi Yeh With V Above               |
|`U+06CF`   | Letter           | RIGHT        | WAW                  | _0_        | &#x06CF; Waw With Dot Above                   |
| | | | | |                                                                                                                      
|`U+06D0`   | Letter           | DUAL         | YEH                  | _0_        | &#x06D0; Dotless Yeh With Vertical 2 Dots Below|
|`U+06D1`   | Letter           | DUAL         | YEH                  | _0_        | &#x06D1; Dotless Yeh With 3 Dots Below        |
|`U+06D2`   | Letter           | RIGHT        | YEH_BARREE           | _0_        | &#x06D2; Yeh Barree                           |
|`U+06D3`   | Letter           | RIGHT        | YEH_BARREE           | _0_        | &#x06D3; Yeh Barree With Hamza Above          |
|`U+06D4`   | Punctuation      | NON_JOINING  | _null_               | _0_        | &#x06D4; Full Stop                            |
|`U+06D5`   | Letter           | NON_JOINING  | TEH_MARBUTA          | _0_        | &#x06D5; Dotless Teh Marbuta                  |
|`U+06D6`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06D6; Small High Sad Lam Alef Maksura      |
|`U+06D7`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06D7; Small High Qaf Lam Alef Maksura      |
|`U+06D8`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06D8; Small High Meem Initial Form         |
|`U+06D9`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06D9; Small High Lam Alef                  |
|`U+06DA`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06DA; Small High Jeem                      |
|`U+06DB`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06DB; Small High Three Dots                |
|`U+06DC`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230_MCM    | &#x06DC; Small High Seen                      |
|`U+06DD`   | Other            | NON_JOINING  | _null_               | _0_        | &#x06DD; End Of Ayah                          |
|`U+06DE`   | Other            | NON_JOINING  | _null_               | _0_        | &#x06DE; Start Of Rub El Hizb                 |
|`U+06DF`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06DF; Small High Rounded Zero              |
| | | | | |                                                                                                                      
|`U+06E0`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06E0; Small High Upright Rectangular Zero  |
|`U+06E1`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06E1; Small High Dotless Head Of Khah      |
|`U+06E2`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06E2; Small High Meem Isolated Form        |
|`U+06E3`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220_MCM    | &#x06E3; Small Low Seen                       |
|`U+06E4`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06E4; Small High Madda                     |
|`U+06E5`   | Letter modifier  | NON_JOINING  | _null_               | _0_        | &#x06E5; Small Waw                            |
|`U+06E6`   | Letter modifier  | NON_JOINING  | _null_               | _0_        | &#x06E6; Small Yeh                            |
|`U+06E7`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230_MCM    | &#x06E7; Small High Yeh                       |
|`U+06E8`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230_MCM    | &#x06E8; Small High Noon                      |
|`U+06E9`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x06E9; Place Of Sajdah                      |
|`U+06EA`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x06EA; Empty Centre Low Stop                |
|`U+06EB`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06EB; Empty Centre High Stop               |
|`U+06EC`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x06EC; Rounded High Stop With Filled Centre |
|`U+06ED`   | Mark [Mn]        | TRANSPARENT  | _null_               | 220        | &#x06ED; Small Low Meem                       |
|`U+06EE`   | Letter           | RIGHT        | DAL                  | _0_        | &#x06EE; Dal With Inverted V Above            |
|`U+06EF`   | Letter           | RIGHT        | REH                  | _0_        | &#x06EF; Reh With Inverted V Above            |
| | | | | |                                                                                                                      
|`U+06F0`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F0; Extended Digit Zero                  |
|`U+06F1`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F1; Extended Digit One                   |
|`U+06F2`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F2; Extended Digit Two                   |
|`U+06F3`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F3; Extended Digit Three                 |
|`U+06F4`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F4; Extended Digit Four                  |
|`U+06F5`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F5; Extended Digit Five                  |
|`U+06F6`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F6; Extended Digit Six                   |
|`U+06F7`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F7; Extended Digit Seven                 |
|`U+06F8`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F8; Extended Digit Eight                 |
|`U+06F9`   | Number           | NON_JOINING  | _null_               | _0_        | &#x06F9; Extended Digit Nine                  |
|`U+06FA`   | Letter           | DUAL         | SEEN                 | _0_        | &#x06FA; Sheen With Dot Below                 |
|`U+06FB`   | Letter           | DUAL         | SAD                  | _0_        | &#x06FB; Dad With Dot Below                   |
|`U+06FC`   | Letter           | DUAL         | AIN                  | _0_        | &#x06FC; Ghain With Dot Below                 |
|`U+06FD`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x06FD; Sign Sindhi Ampersand                |
|`U+06FE`   | Symbol           | NON_JOINING  | _null_               | _0_        | &#x06FE; Sign Sindhi Postposition Men         |
|`U+06FF`   | Letter           | DUAL         | KNOTTED_HEH          | _0_        | &#x06FF; Knotted Heh With Inverted V Above    |          



## Arabic Supplement character table ##


| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                                           |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------------------------|
|`U+0750`   | Letter           | DUAL         | BEH                  | _0_        | &#x0750; Dotless Beh With Horizontal 3 Dots Below               |
|`U+0751`   | Letter           | DUAL         | BEH                  | _0_        | &#x0751; Beh With 3 Dots Above                                  |
|`U+0752`   | Letter           | DUAL         | BEH                  | _0_        | &#x0752; Dotless Beh With Inverted 3 Dots Below                 |
|`U+0753`   | Letter           | DUAL         | BEH                  | _0_        | &#x0753; Dotless Beh With Inverted 3 Dots Below And 2 Dots Above|
|`U+0754`   | Letter           | DUAL         | BEH                  | _0_        | &#x0754; Dotless Beh With 2 Dots Below And Dot Above            |
|`U+0755`   | Letter           | DUAL         | BEH                  | _0_        | &#x0755; Dotless Beh With Inverted V Below                      |
|`U+0756`   | Letter           | DUAL         | BEH                  | _0_        | &#x0756; Dotless Beh With V Above                               |
|`U+0757`   | Letter           | DUAL         | HAH                  | _0_        | &#x0757; Hah With 2 Dots Above                                  |
|`U+0758`   | Letter           | DUAL         | HAH                  | _0_        | &#x0758; Hah With Inverted 3 Dots Below                         |
|`U+0759`   | Letter           | RIGHT        | DAL                  | _0_        | &#x0759; Dal With Vertical 2 Dots Below And Tah Above           |
|`U+075A`   | Letter           | RIGHT        | DAL                  | _0_        | &#x075A; Dal With Inverted V Below                              |
|`U+075B`   | Letter           | RIGHT        | REH                  | _0_        | &#x075B; Reh With Bar                                           |
|`U+075C`   | Letter           | DUAL         | SEEN                 | _0_        | &#x075C; Seen With 4 Dots Above                                 |
|`U+075D`   | Letter           | DUAL         | AIN                  | _0_        | &#x075D; Ain With 2 Dots Above                                  |
|`U+075E`   | Letter           | DUAL         | AIN                  | _0_        | &#x075E; Ain With Inverted 3 Dots Above                         |
|`U+075F`   | Letter           | DUAL         | AIN                  | _0_        | &#x075F; Ain With Vertical 2 Dots Above                         |
| | | | | |                                                                                                              
|`U+0760`   | Letter           | DUAL         | FEH                  | _0_        | &#x0760; Dotless Feh With 2 Dots Below                          |
|`U+0761`   | Letter           | DUAL         | FEH                  | _0_        | &#x0761; Dotless Feh With Inverted 3 Dots Below                 |
|`U+0762`   | Letter           | DUAL         | GAF                  | _0_        | &#x0762; Keheh With Dot Above                                   |
|`U+0763`   | Letter           | DUAL         | GAF                  | _0_        | &#x0763; Keheh With 3 Dots Above                                |
|`U+0764`   | Letter           | DUAL         | GAF                  | _0_        | &#x0764; Keheh With Inverted 3 Dots Below                       |
|`U+0765`   | Letter           | DUAL         | MEEM                 | _0_        | &#x0765; Meem With Dot Above                                    |
|`U+0766`   | Letter           | DUAL         | MEEM                 | _0_        | &#x0766; Meem With Dot Below                                    |
|`U+0767`   | Letter           | DUAL         | NOON                 | _0_        | &#x0767; Noon With 2 Dots Below                                 |
|`U+0768`   | Letter           | DUAL         | NOON                 | _0_        | &#x0768; Noon With Tah Above                                    |
|`U+0769`   | Letter           | DUAL         | NOON                 | _0_        | &#x0769; Noon With V Above                                      |
|`U+076A`   | Letter           | DUAL         | LAM                  | _0_        | &#x076A; Lam With Bar                                           |
|`U+076B`   | Letter           | RIGHT        | REH                  | _0_        | &#x076B; Reh With Vertical 2 Dots Above                         |
|`U+076C`   | Letter           | RIGHT        | REH                  | _0_        | &#x076C; Reh With Hamza Above                                   |
|`U+076D`   | Letter           | DUAL         | SEEN                 | _0_        | &#x076D; Seen With Vertical 2 Dots Above                        |
|`U+076E`   | Letter           | DUAL         | HAH                  | _0_        | &#x076E; Hah With Tah Below                                     |
|`U+076F`   | Letter           | DUAL         | HAH                  | _0_        | &#x076F; Hah With Tah And 2 Dots Below                          |
| | | | | |                                                                                                                      
|`U+0770`   | Letter           | DUAL         | SEEN                 | _0_        | &#x0770; Seen With 2 Dots And Tah Above                         |
|`U+0771`   | Letter           | RIGHT        | REH                  | _0_        | &#x0771; Reh With 2 Dots And Tah Above                          |
|`U+0772`   | Letter           | DUAL         | HAH                  | _0_        | &#x0772; Hah With Tah Above                                     |
|`U+0773`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0773; Alef With Digit Two Above                              |
|`U+0774`   | Letter           | RIGHT        | ALEF                 | _0_        | &#x0774; Alef With Digit Three Above                            |
|`U+0775`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x0775; Farsi Yeh With Digit Two Above                         |
|`U+0776`   | Letter           | DUAL         | FARSI_YEH            | _0_        | &#x0776; Farsi Yeh With Digit Three Above                       |
|`U+0777`   | Letter           | DUAL         | YEH                  | _0_        | &#x0777; Dotless Yeh With Digit Four Below                      |
|`U+0778`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0778; Waw With Digit Two Above                               |
|`U+0779`   | Letter           | RIGHT        | WAW                  | _0_        | &#x0779; Waw With Digit Three Above                             |
|`U+077A`   | Letter           | DUAL         | BURUSHASKI_YEH_BARREE| _0_        | &#x077A; Burushaski Yeh Barree With Digit Two Above             |
|`U+077B`   | Letter           | DUAL         | BURUSHASKI_YEH_BARREE| _0_        | &#x077B; Burushaski Yeh Barree With Digit Three Above           |
|`U+077C`   | Letter           | DUAL         | HAH                  | _0_        | &#x077C; Hah With Digit Four Below                              |
|`U+077D`   | Letter           | DUAL         | SEEN                 | _0_        | &#x077D; Seen With Digit Four Above                             |
|`U+077E`   | Letter           | DUAL         | SEEN                 | _0_        | &#x077E; Seen With Inverted V Above                             |
|`U+077F`   | Letter           | DUAL         | KAF                  | _0_        | &#x077F; Kaf With 2 Dots Above                                  |                        



## Miscellaneous character table ##

Other important characters that may be encountered when shaping runs
of Arabic text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
combining mark in isolation. Real-world ext syllables may also use
other characters, such as hyphens or dashes, in a similar placeholder
fashion; shaping engines should cope with this situation gracefully.


| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                          |
|:----------|:-----------------|:-------------|:---------------------|:-----------|--------------------------------|
|`U+00A0`   | Separator        | PLACEHOLDER  | _null_               | _0_        | &#x00A0; No-break space        |
|`U+200C`   | Other            | NON_JOINER   | _null_               | _0_        | &#x200C; Zero-width non-joiner |
|`U+200D`   | Other            | JOINER       | _null_               | _0_        | &#x200D; Zero-width joiner     |
|`U+2010`   | Punctuation      | PLACEHOLDER  | _null_               | _0_        | &#x2010; Hyphen                |
|`U+2011`   | Punctuation      | PLACEHOLDER  | _null_               | _0_        | &#x2011; No-break hyphen       |
|`U+2012`   | Punctuation      | PLACEHOLDER  | _null_               | _0_        | &#x2012; Figure dash           |
|`U+2013`   | Punctuation      | PLACEHOLDER  | _null_               | _0_        | &#x2013; En dash               |
|`U+2014`   | Punctuation      | PLACEHOLDER  | _null_               | _0_        | &#x2014; Em dash               |
|`U+25CC`   | Symbol           | DOTTED_CIRCL | _null_               | _0_        | &#x25CC; Dotted circle         |


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
