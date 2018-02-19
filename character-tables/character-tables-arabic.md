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

Assigned codepoints with a _null_ in the _Shaping class_
column evoke no special behavior from the shaping engine. Note that
this does include some valid codepoints in the Arabic block, such as
currency marks and other symbols.

The _Mark class_ column indicates the Canonical Combining Class
for the codepoint.  Marks are assigned non-zero combining classes so
that sequences of adjacent marks can be reordered as required by the
orthography. For Arabic,

Some codepoints in the following table use a _Shaping class_ that
differs from the codepoint's Unicode _General Category_. The _Shaping
class_ takes precedence during OpenType shaping, as it captures more
specific, script-aware behavior.

| Codepoint | Unicode category | Joining type | Joining group        | Mark class | Glyph                                         |
|:----------|:-----------------|:-------------|:---------------------|:-----------|-----------------------------------------------|
|`U+0600`   |                  | NON_JOINING  | _null_               | _0_        | &#x0600; Number Sign                          |
|`U+0601`   |                  | NON_JOINING  | _null_               | _0_        | &#x0601; Sign Sanah                           |
|`U+0602`   |                  | NON_JOINING  | _null_               | _0_        | &#x0602; Footnote Marker                      |
|`U+0603`   |                  | NON_JOINING  | _null_               | _0_        | &#x0603; Sign Safha                           |
|`U+0604`   |                  | NON_JOINING  | _null_               | _0_        | &#x0604; Sign Samvat                          |
|`U+0605`   |                  | NON_JOINING  | _null_               | _0_        | &#x0605; Number Mark Above                    |
|`U+0606`   |                  | NON_JOINING  | _null_               | _0_        | &#x0606; Cube Root                            |
|`U+0607`   |                  | NON_JOINING  | _null_               | _0_        | &#x0607; Fourth Root                          |
|`U+0608`   |                  | NON_JOINING  | _null_               | _0_        | &#x0608; Ray                                  |
|`U+0609`   |                  | NON_JOINING  | _null_               | _0_        | &#x0609; Per Mille                            |
|`U+060A`   |                  | NON_JOINING  | _null_               | _0_        | &#x060A; Per Ten Thousand                     |
|`U+060B`   |                  | NON_JOINING  | _null_               | _0_        | &#x060B; Afghani Sign                         |
|`U+060C`   |                  | NON_JOINING  | _null_               | _0_        | &#x060C; Comma                                |
|`U+060D`   |                  | NON_JOINING  | _null_               | _0_        | &#x060D; Date Separator                       |
|`U+060E`   |                  | NON_JOINING  | _null_               | _0_        | &#x060E; Poetic Verse Sign                    |
|`U+060F`   |                  | NON_JOINING  | _null_               | _0_        | &#x060F; Sign Misra                           |
| | | | | |                                                                                                                      
|`U+0610`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0610; Sign Sallallahou Alayhe Wassallam    |
|`U+0611`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0611; Sign Alayhe Assallam                 |
|`U+0612`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0612; Sign Rahmatullah Alayhe              |
|`U+0613`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0613; Sign Radi Allahou Anhu               |
|`U+0614`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0614; Sign Takhallus                       |
|`U+0615`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0615; Small High Tah                       |
|`U+0616`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x0616; Small High Alef Lam Yeh              |
|`U+0617`   | Mark [Mn]        | TRANSPARENT  | _null_               | 230        | &#x0617; Small High Zain                      |
|`U+0618`   | Mark [Mn]        | TRANSPARENT  | _null_               | 30         | &#x0618; Small Fatha                          |
|`U+0619`   | Mark [Mn]        | TRANSPARENT  | _null_               | 31         | &#x0619; Small Damma                          |
|`U+061A`   | Mark [Mn]        | TRANSPARENT  | _null_               | 32         | &#x061A; Small Kasra                          |
|`U+061B`   |                  | NON_JOINING  | _null_               | _0_        | &#x061B; Semicolon                            |
|`U+061C`   | Other [format]   | TRANSPARENT  | _null_               | _0_        | &#x061C; Arabic Letter Mark                   |
|`U+061D`   | _unassigned_     |              |                      |            |                                               |
|`U+061E`   |                  | NON_JOINING  | _null_               | _0_        | &#x061E; Triple Dot Punctuation Mark          |
|`U+061F`   |                  | NON_JOINING  | _null_               | _0_        | &#x061F; Question Mark                        |
| | | | | |                                                                                                                       
|`U+0620`   |                  | DUAL         | YEH                  | _0_        | &#x0620; Dotless Yeh With Separate Ring Below |
|`U+0621`   |                  | NON_JOINING  | _null_               | _0_        | &#x0621; Hamza                                |
|`U+0622`   |                  | RIGHT        | ALEF                 | _0_        | &#x0622; Alef With Madda Above                |
|`U+0623`   |                  | RIGHT        | ALEF                 | _0_        | &#x0623; Alef With Hamza Above                |
|`U+0624`   |                  | RIGHT        | WAW                  | _0_        | &#x0624; Waw With Hamza Above                 |
|`U+0625`   |                  | RIGHT        | ALEF                 | _0_        | &#x0625; Alef With Hamza Below                |
|`U+0626`   |                  | DUAL         | YEH                  | _0_        | &#x0626; Dotless Yeh With Hamza Above         |
|`U+0627`   |                  | RIGHT        | ALEF                 | _0_        | &#x0627; Alef                                 |
|`U+0628`   |                  | DUAL         | BEH                  | _0_        | &#x0628; Beh                                  |
|`U+0629`   |                  | RIGHT        | TEH_MARBUTA          | _0_        | &#x0629; Teh Marbuta                          |
|`U+062A`   |                  | DUAL         | BEH                  | _0_        | &#x062A; Dotless Beh With 2 Dots Above        |
|`U+062B`   |                  | DUAL         | BEH                  | _0_        | &#x062B; Dotless Beh With 3 Dots Above        |
|`U+062C`   |                  | DUAL         | HAH                  | _0_        | &#x062C; Hah With Dot Below                   |
|`U+062D`   |                  | DUAL         | HAH                  | _0_        | &#x062D; Hah                                  |
|`U+062E`   |                  | DUAL         | HAH                  | _0_        | &#x062E; Hah With Dot Above                   |
|`U+062F`   |                  | RIGHT        | DAL                  | _0_        | &#x062F; Dal                                  |
| | | | | |                                                                                                                      
|`U+0630`   |                  | RIGHT        | DAL                  | _0_        | &#x0630; Dal With Dot Above                   |
|`U+0631`   |                  | RIGHT        | REH                  | _0_        | &#x0631; Reh                                  |
|`U+0632`   |                  | RIGHT        | REH                  | _0_        | &#x0632; Reh With Dot Above                   |
|`U+0633`   |                  | DUAL         | SEEN                 | _0_        | &#x0633; Seen                                 |
|`U+0634`   |                  | DUAL         | SEEN                 | _0_        | &#x0634; Seen With 3 Dots Above               |
|`U+0635`   |                  | DUAL         | SAD                  | _0_        | &#x0635; Sad                                  |
|`U+0636`   |                  | DUAL         | SAD                  | _0_        | &#x0636; Sad With Dot Above                   |
|`U+0637`   |                  | DUAL         | TAH                  | _0_        | &#x0637; Tah                                  |
|`U+0638`   |                  | DUAL         | TAH                  | _0_        | &#x0638; Tah With Dot Above                   |
|`U+0639`   |                  | DUAL         | AIN                  | _0_        | &#x0639; Ain                                  |
|`U+063A`   |                  | DUAL         | AIN                  | _0_        | &#x063A; Ain With Dot Above                   |
|`U+063B`   |                  | DUAL         | GAF                  | _0_        | &#x063B; Keheh With 2 Dots Above              |
|`U+063C`   |                  | DUAL         | GAF                  | _0_        | &#x063C; Keheh With 3 Dots Below              |
|`U+063D`   |                  | DUAL         | FARSI_YEH            | _0_        | &#x063D; Farsi Yeh With Inverted V Above      |
|`U+063E`   |                  | DUAL         | FARSI_YEH            | _0_        | &#x063E; Farsi Yeh With 2 Dots Above          |
|`U+063F`   |                  | DUAL         | FARSI_YEH            | _0_        | &#x063F; Farsi Yeh With 3 Dots Above          |
| | | | | |                                                                                                                       
|`U+0640`   | Letter modifier  | JOIN_CAUSING | _null_               | _0_        | &#x0640; Tatweel                              |
|`U+0641`   |                  | DUAL         | FEH                  | _0_        | &#x0641; Feh                                  |
|`U+0642`   |                  | DUAL         | QAF                  | _0_        | &#x0642; Qaf                                  |
|`U+0643`   |                  | DUAL         | KAF                  | _0_        | &#x0643; Kaf                                  |
|`U+0644`   |                  | DUAL         | LAM                  | _0_        | &#x0644; Lam                                  |
|`U+0645`   |                  | DUAL         | MEEM                 | _0_        | &#x0645; Meem                                 |
|`U+0646`   |                  | DUAL         | NOON                 | _0_        | &#x0646; Noon                                 |
|`U+0647`   |                  | DUAL         | HEH                  | _0_        | &#x0647; Heh                                  |
|`U+0648`   |                  | RIGHT        | WAW                  | _0_        | &#x0648; Waw                                  |
|`U+0649`   |                  | DUAL         | YEH                  | _0_        | &#x0649; Dotless Yeh                          |
|`U+064A`   |                  | DUAL         | YEH                  | _0_        | &#x064A; Yeh                                  |
|`U+064B`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 27         | &#x064B; Fathatan                             |
|`U+064C`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 28         | &#x064C; Dammatan                             |
|`U+064D`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 29         | &#x064D; Kasratan                             |
|`U+064E`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 30         | &#x064E; Fatha                                |
|`U+064F`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 31         | &#x064F; Damma                                |
| | | | | |                                                                                                                      
|`U+0650`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 32         | &#x0650; Kasra                                |
|`U+0651`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 33         | &#x0651; Shadda                               |
|`U+0652`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 34         | &#x0652; Sukun                                |
|`U+0653`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x0653; Maddah Above                         |
|`U+0654`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230_MCM    | &#x0654; Hamza Above                          |
|`U+0655`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220_MCM    | &#x0655; Hamza Below                          |
|`U+0656`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220        | &#x0656; Subscript Alef                       |
|`U+0657`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x0657; Inverted Damma                       |
|`U+0658`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230_MCM    | &#x0658; Noon Ghunna                          |
|`U+0659`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x0659; Zwarakay                             |
|`U+065A`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x065A; Vowel Sign Small V Above             |
|`U+065B`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x065B; Vowel Sign Inverted Small V Above    |
|`U+065C`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220        | &#x065C; Vowel Sign Dot Below                 |
|`U+065D`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x065D; Reversed Damma                       |
|`U+065E`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x065E; Fatha with Two Dots                  |
|`U+065F`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220        | &#x065F; Wavy Hamza Below                     |
| | | | | |                                                                                                                      
|`U+0660`   |                  | NON_JOINING  | _null_               | _0_        | &#x0660; Digit Zero                           |
|`U+0661`   |                  | NON_JOINING  | _null_               | _0_        | &#x0661; Digit One                            |
|`U+0662`   |                  | NON_JOINING  | _null_               | _0_        | &#x0662; Digit Two                            |
|`U+0663`   |                  | NON_JOINING  | _null_               | _0_        | &#x0663; Digit Three                          |
|`U+0664`   |                  | NON_JOINING  | _null_               | _0_        | &#x0664; Digit Four                           |
|`U+0665`   |                  | NON_JOINING  | _null_               | _0_        | &#x0665; Digit Five                           |
|`U+0666`   |                  | NON_JOINING  | _null_               | _0_        | &#x0666; Digit Six                            |
|`U+0667`   |                  | NON_JOINING  | _null_               | _0_        | &#x0667; Digit Seven                          |
|`U+0668`   |                  | NON_JOINING  | _null_               | _0_        | &#x0668; Digit Eight                          |
|`U+0669`   |                  | NON_JOINING  | _null_               | _0_        | &#x0669; Digit Nine                           |
|`U+066A`   |                  | NON_JOINING  | _null_               | _0_        | &#x066A; Percent Sign                         |
|`U+066B`   |                  | NON_JOINING  | _null_               | _0_        | &#x066B; Decimal Separator                    |
|`U+066C`   |                  | NON_JOINING  | _null_               | _0_        | &#x066C; Thousands Separator                  |
|`U+066D`   |                  | NON_JOINING  | _null_               | _0_        | &#x066D; Five Pointed Star                    |
|`U+066E`   |                  | DUAL         | BEH                  | _0_        | &#x066E; Dotless Beh                          |
|`U+066F`   |                  | DUAL         | QAF                  | _0_        | &#x066F; Dotless Qaf                          |
| | | | | |                                                                                                                      
|`U+0670`   | Mark [Mn]        | TRANSPARENT  | _null_             ? | 35         | &#x0670; Superscript Alef                     |
|`U+0671`   |                  | RIGHT        | ALEF                 | _0_        | &#x0671; Alef With Wasla Above                |
|`U+0672`   |                  | RIGHT        | ALEF                 | _0_        | &#x0672; Alef With Wavy Hamza Above           |
|`U+0673`   |                  | RIGHT        | ALEF                 | _0_        | &#x0673; Alef With Wavy Hamza Below           |
|`U+0674`   |                  | NON_JOINING  | _null_               | _0_        | &#x0674; High Hamza                           |
|`U+0675`   |                  | RIGHT        | ALEF                 | _0_        | &#x0675; High Hamza Alef                      |
|`U+0676`   |                  | RIGHT        | WAW                  | _0_        | &#x0676; High Hamza Waw                       |
|`U+0677`   |                  | RIGHT        | WAW                  | _0_        | &#x0677; High Hamza Waw With Damma Above      |
|`U+0678`   |                  | DUAL         | YEH                  | _0_        | &#x0678; High Hamza Dotless Yeh               |
|`U+0679`   |                  | DUAL         | BEH                  | _0_        | &#x0679; Dotless Beh With Tah Above           |
|`U+067A`   |                  | DUAL         | BEH                  | _0_        | &#x067A; Dotless Beh With Vertical 2 Dots Above|
|`U+067B`   |                  | DUAL         | BEH                  | _0_        | &#x067B; Dotless Beh With Vertical 2 Dots Below|
|`U+067C`   |                  | DUAL         | BEH                  | _0_        | &#x067C; Dotless Beh With Attached Ring Below And 2 Dots Above|
|`U+067D`   |                  | DUAL         | BEH                  | _0_        | &#x067D; Dotless Beh With Inverted 3 Dots Above|
|`U+067E`   |                  | DUAL         | BEH                  | _0_        | &#x067E; Dotless Beh With 3 Dots Below        |
|`U+067F`   |                  | DUAL         | BEH                  | _0_        | &#x067F; Dotless Beh With 4 Dots Above        |
| | | | | |                                                                                                                      
|`U+0680`   |                  | DUAL         | BEH                  | _0_        | &#x0680; Dotless Beh With 4 Dots Below        |
|`U+0681`   |                  | DUAL         | HAH                  | _0_        | &#x0681; Hah With Hamza Above                 |
|`U+0682`   |                  | DUAL         | HAH                  | _0_        | &#x0682; Hah With Vertical 2 Dots Above       |
|`U+0683`   |                  | DUAL         | HAH                  | _0_        | &#x0683; Hah With 2 Dots Below                |
|`U+0684`   |                  | DUAL         | HAH                  | _0_        | &#x0684; Hah With Vertical 2 Dots Below       |
|`U+0685`   |                  | DUAL         | HAH                  | _0_        | &#x0685; Hah With 3 Dots Above                |
|`U+0686`   |                  | DUAL         | HAH                  | _0_        | &#x0686; Hah With 3 Dots Below                |
|`U+0687`   |                  | DUAL         | HAH                  | _0_        | &#x0687; Hah With 4 Dots Below                |
|`U+0688`   |                  | RIGHT        | DAL                  | _0_        | &#x0688; Dal With Tah Above                   |
|`U+0689`   |                  | RIGHT        | DAL                  | _0_        | &#x0689; Dal With Attached Ring Below         |
|`U+068A`   |                  | RIGHT        | DAL                  | _0_        | &#x068A; Dal With Dot Below                   |
|`U+068B`   |                  | RIGHT        | DAL                  | _0_        | &#x068B; Dal With Dot Below And Tah Above     |
|`U+068C`   |                  | RIGHT        | DAL                  | _0_        | &#x068C; Dal With 2 Dots Above                |
|`U+068D`   |                  | RIGHT        | DAL                  | _0_        | &#x068D; Dal With 2 Dots Below                |
|`U+068E`   |                  | RIGHT        | DAL                  | _0_        | &#x068E; Dal With 3 Dots Above                |
|`U+068F`   |                  | RIGHT        | DAL                  | _0_        | &#x068F; Dal With Inverted 3 Dots Above       |
| | | | | |                                                                                                                      
|`U+0690`   |                  | RIGHT        | DAL                  | _0_        | &#x0690; Dal With 4 Dots Above                |
|`U+0691`   |                  | RIGHT        | REH                  | _0_        | &#x0691; Reh With Tah Above                   |
|`U+0692`   |                  | RIGHT        | REH                  | _0_        | &#x0692; Reh With V Above                     |
|`U+0693`   |                  | RIGHT        | REH                  | _0_        | &#x0693; Reh With Attached Ring Below         |
|`U+0694`   |                  | RIGHT        | REH                  | _0_        | &#x0694; Reh With Dot Below                   |
|`U+0695`   |                  | RIGHT        | REH                  | _0_        | &#x0695; Reh With V Below                     |
|`U+0696`   |                  | RIGHT        | REH                  | _0_        | &#x0696; Reh With Dot Below And Dot Within    |
|`U+0697`   |                  | RIGHT        | REH                  | _0_        | &#x0697; Reh With 2 Dots Above                |
|`U+0698`   |                  | RIGHT        | REH                  | _0_        | &#x0698; Reh With 3 Dots Above                |
|`U+0699`   |                  | RIGHT        | REH                  | _0_        | &#x0699; Reh With 4 Dots Above                |
|`U+069A`   |                  | DUAL         | SEEN                 | _0_        | &#x069A; Seen With Dot Below And Dot Above    |
|`U+069B`   |                  | DUAL         | SEEN                 | _0_        | &#x069B; Seen With 3 Dots Below               |
|`U+069C`   |                  | DUAL         | SEEN                 | _0_        | &#x069C; Seen With 3 Dots Below And 3 Dots Above|
|`U+069D`   |                  | DUAL         | SAD                  | _0_        | &#x069D; Sad With 2 Dots Below                |
|`U+069E`   |                  | DUAL         | SAD                  | _0_        | &#x069E; Sad With 3 Dots Above                |
|`U+069F`   |                  | DUAL         | TAH                  | _0_        | &#x069F; Tah With 3 Dots Above                |
| | | | | |                                                                                                                      
|`U+06A0`   |                  | DUAL         | AIN                  | _0_        | &#x06A0; Ain With 3 Dots Above                |
|`U+06A1`   |                  | DUAL         | FEH                  | _0_        | &#x06A1; Dotless Feh                          |
|`U+06A2`   |                  | DUAL         | FEH                  | _0_        | &#x06A2; Dotless Feh With Dot Below           |
|`U+06A3`   |                  | DUAL         | FEH                  | _0_        | &#x06A3; Feh With Dot Below                   |
|`U+06A4`   |                  | DUAL         | FEH                  | _0_        | &#x06A4; Dotless Feh With 3 Dots Above        |
|`U+06A5`   |                  | DUAL         | FEH                  | _0_        | &#x06A5; Dotless Feh With 3 Dots Below        |
|`U+06A6`   |                  | DUAL         | FEH                  | _0_        | &#x06A6; Dotless Feh With 4 Dots Above        |
|`U+06A7`   |                  | DUAL         | QAF                  | _0_        | &#x06A7; Dotless Qaf With Dot Above           |
|`U+06A8`   |                  | DUAL         | QAF                  | _0_        | &#x06A8; Dotless Qaf With 3 Dots Above        |
|`U+06A9`   |                  | DUAL         | GAF                  | _0_        | &#x06A9; Keheh                                |
|`U+06AA`   |                  | DUAL         | SWASH_KAF            | _0_        | &#x06AA; Swash Kaf                            |
|`U+06AB`   |                  | DUAL         | GAF                  | _0_        | &#x06AB; Keheh With Attached Ring Below       |
|`U+06AC`   |                  | DUAL         | KAF                  | _0_        | &#x06AC; Kaf With Dot Above                   |
|`U+06AD`   |                  | DUAL         | KAF                  | _0_        | &#x06AD; Kaf With 3 Dots Above                |
|`U+06AE`   |                  | DUAL         | KAF                  | _0_        | &#x06AE; Kaf With 3 Dots Below                |
|`U+06AF`   |                  | DUAL         | GAF                  | _0_        | &#x06AF; Gaf                                  |
| | | | | |                                                                                                                     
|`U+06B0`   |                  | DUAL         | GAF                  | _0_        | &#x06B0; Gaf With Attached Ring Below         |
|`U+06B1`   |                  | DUAL         | GAF                  | _0_        | &#x06B1; Gaf With 2 Dots Above                |
|`U+06B2`   |                  | DUAL         | GAF                  | _0_        | &#x06B2; Gaf With 2 Dots Below                |
|`U+06B3`   |                  | DUAL         | GAF                  | _0_        | &#x06B3; Gaf With Vertical 2 Dots Below       |
|`U+06B4`   |                  | DUAL         | GAF                  | _0_        | &#x06B4; Gaf With 3 Dots Above                |
|`U+06B5`   |                  | DUAL         | LAM                  | _0_        | &#x06B5; Lam With V Above                     |
|`U+06B6`   |                  | DUAL         | LAM                  | _0_        | &#x06B6; Lam With Dot Above                   |
|`U+06B7`   |                  | DUAL         | LAM                  | _0_        | &#x06B7; Lam With 3 Dots Above                |
|`U+06B8`   |                  | DUAL         | LAM                  | _0_        | &#x06B8; Lam With 3 Dots Below                |
|`U+06B9`   |                  | DUAL         | NOON                 | _0_        | &#x06B9; Noon With Dot Below                  |
|`U+06BA`   |                  | DUAL         | NOON                 | _0_        | &#x06BA; Dotless Noon                         |
|`U+06BB`   |                  | DUAL         | NOON                 | _0_        | &#x06BB; Dotless Noon With Tah Above          |
|`U+06BC`   |                  | DUAL         | NOON                 | _0_        | &#x06BC; Noon With Attached Ring Below        |
|`U+06BD`   |                  | DUAL         | NYA                  | _0_        | &#x06BD; Nya                                  |
|`U+06BE`   |                  | DUAL         | KNOTTED_HEH          | _0_        | &#x06BE; Knotted Heh                          |
|`U+06BF`   |                  | DUAL         | HAH                  | _0_        | &#x06BF; Hah With 3 Dots Below And Dot Above  |
| | | | | |                                                                                                                      
|`U+06C0`   |                  | RIGHT        | TEH_MARBUTA          | _0_        | &#x06C0; Dotless Teh Marbuta With Hamza Above |
|`U+06C1`   |                  | DUAL         | HEH_GOAL             | _0_        | &#x06C1; Heh Goal                             |
|`U+06C2`   |                  | DUAL         | HEH_GOAL             | _0_        | &#x06C2; Heh Goal With Hamza Above            |
|`U+06C3`   |                  | RIGHT        | TEH_MARBUTA_GOAL     | _0_        | &#x06C3; Teh Marbuta Goal                     |
|`U+06C4`   |                  | RIGHT        | WAW                  | _0_        | &#x06C4; Waw With Attached Ring Within        |
|`U+06C5`   |                  | RIGHT        | WAW                  | _0_        | &#x06C5; Waw With Bar                         |
|`U+06C6`   |                  | RIGHT        | WAW                  | _0_        | &#x06C6; Waw With V Above                     |
|`U+06C7`   |                  | RIGHT        | WAW                  | _0_        | &#x06C7; Waw With Damma Above                 |
|`U+06C8`   |                  | RIGHT        | WAW                  | _0_        | &#x06C8; Waw With Alef Above                  |
|`U+06C9`   |                  | RIGHT        | WAW                  | _0_        | &#x06C9; Waw With Inverted V Above            |
|`U+06CA`   |                  | RIGHT        | WAW                  | _0_        | &#x06CA; Waw With 2 Dots Above                |
|`U+06CB`   |                  | RIGHT        | WAW                  | _0_        | &#x06CB; Waw With 3 Dots Above                |
|`U+06CC`   |                  | DUAL         | FARSI_YEH            | _0_        | &#x06CC; Farsi Yeh                            |
|`U+06CD`   |                  | RIGHT        | YEH_WITH_TAIL        | _0_        | &#x06CD; Yeh With Tail                        |
|`U+06CE`   |                  | DUAL         | FARSI_YEH            | _0_        | &#x06CE; Farsi Yeh With V Above               |
|`U+06CF`   |                  | RIGHT        | WAW                  | _0_        | &#x06CF; Waw With Dot Above                   |
| | | | | |                                                                                                                      
|`U+06D0`   |                  | DUAL         | YEH                  | _0_        | &#x06D0; Dotless Yeh With Vertical 2 Dots Below|
|`U+06D1`   |                  | DUAL         | YEH                  | _0_        | &#x06D1; Dotless Yeh With 3 Dots Below        |
|`U+06D2`   |                  | RIGHT        | YEH_BARREE           | _0_        | &#x06D2; Yeh Barree                           |
|`U+06D3`   |                  | RIGHT        | YEH_BARREE           | _0_        | &#x06D3; Yeh Barree With Hamza Above          |
|`U+06D4`   |                  | NON_JOINING  | _null_               | _0_        | &#x06D4; Full Stop                            |
|`U+06D5`   |                  | NON_JOINING  | TEH_MARBUTA          | _0_        | &#x06D5; Dotless Teh Marbuta                  |
|`U+06D6`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06D6; Small High Sad Lam Alef Maksura      |
|`U+06D7`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06D7; Small High Qaf Lam Alef Maksura      |
|`U+06D8`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06D8; Small High Meem Initial Form         |
|`U+06D9`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06D9; Small High Lam Alef                  |
|`U+06DA`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06DA; Small High Jeem                      |
|`U+06DB`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06DB; Small High Three Dots                |
|`U+06DC`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230_MCM    | &#x06DC; Small High Seen                      |
|`U+06DD`   |                  | NON_JOINING  | _null_               | _0_        | &#x06DD; End Of Ayah                          |
|`U+06DE`   |                  | NON_JOINING  | _null_               | _0_        | &#x06DE; Start Of Rub El Hizb                 |
|`U+06DF`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06DF; Small High Rounded Zero              |
| | | | | |                                                                                                                      
|`U+06E0`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06E0; Small High Upright Rectangular Zero  |
|`U+06E1`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06E1; Small High Dotless Head Of Khah      |
|`U+06E2`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06E2; Small High Meem Isolated Form        |
|`U+06E3`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220_MCM    | &#x06E3; Small Low Seen                       |
|`U+06E4`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06E4; Small High Madda                     |
|`U+06E5`   |                  | NON_JOINING  | _null_             ? | _0_        | &#x06E5; Small Waw                            |
|`U+06E6`   |                  | NON_JOINING  | _null_             ? | _0_        | &#x06E6; Small Yeh                            |
|`U+06E7`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230_MCM    | &#x06E7; Small High Yeh                       |
|`U+06E8`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230_MCM    | &#x06E8; Small High Noon                      |
|`U+06E9`   |                  | NON_JOINING  | _null_               | _0_        | &#x06E9; Place Of Sajdah                      |
|`U+06EA`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220        | &#x06EA; Empty Centre Low Stop                |
|`U+06EB`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06EB; Empty Centre High Stop               |
|`U+06EC`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 230        | &#x06EC; Rounded High Stop With Filled Centre |
|`U+06ED`   | Mark [Mn]        | TRANSPARENT  | _null_             * | 220        | &#x06ED; Small Low Meem                       |
|`U+06EE`   |                  | RIGHT        | DAL                  | _0_        | &#x06EE; Dal With Inverted V Above            |
|`U+06EF`   |                  | RIGHT        | REH                  | _0_        | &#x06EF; Reh With Inverted V Above            |
| | | | | |                                                                                                                      
|`U+06F0`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F0; Extended Digit Zero                  |
|`U+06F1`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F1; Extended Digit One                   |
|`U+06F2`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F2; Extended Digit Two                   |
|`U+06F3`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F3; Extended Digit Three                 |
|`U+06F4`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F4; Extended Digit Four                  |
|`U+06F5`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F5; Extended Digit Five                  |
|`U+06F6`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F6; Extended Digit Six                   |
|`U+06F7`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F7; Extended Digit Seven                 |
|`U+06F8`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F8; Extended Digit Eight                 |
|`U+06F9`   |                  | NON_JOINING  | _null_               | _0_        | &#x06F9; Extended Digit Nine                  |
|`U+06FA`   |                  | DUAL         | SEEN                 | _0_        | &#x06FA; Sheen With Dot Below                 |
|`U+06FB`   |                  | DUAL         | SAD                  | _0_        | &#x06FB; Dad With Dot Below                   |
|`U+06FC`   |                  | DUAL         | AIN                  | _0_        | &#x06FC; Ghain With Dot Below                 |
|`U+06FD`   |                  | NON_JOINING  | _null_               | _0_        | &#x06FD; Sign Sindhi Ampersand                |
|`U+06FE`   |                  | NON_JOINING  | _null_               | _0_        | &#x06FE; Sign Sindhi Postposition Men         |
|`U+06FF`   |                  | DUAL         | KNOTTED_HEH          | _0_        | &#x06FF; Knotted Heh With Inverted V Above    |          



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
