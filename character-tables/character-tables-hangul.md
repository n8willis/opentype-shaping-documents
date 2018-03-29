# Hangul character tables #

This document lists the per-character shaping information needed to
[shape Hangul text](../opentype-shaping-hangul.md).

**Table of Contents**

  - [Hangul Jamo character table](#hangul-jamo-character-table)
  - [Hangul Jamo Extended-A character table](#hangul-jamo-extended-a-character-table)
  - [Hangul Jamo Extended-B character table](#hangul-jamo-extended-b-character-table)
  - [Miscellaneous character table](#miscellaneous-character-table)
      

## Hangul Jamo character table ##

Hangul Jamo should be classified as in the following
table. Codepoints in the Hangul Jamo block with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

The _Jamo type_ column indicates the syllable-component type of the
jamo. "L" for leading consonants (choseong), "V" for vowels
(jungseong), and "T" for trailing consonants (jongseong).

In addition, the filler codepoints `U+115F` (Choseong Filler) and `U+1160`
(Jungseong Filler) are classified as type "Lf" and "Vf", respectively.


| Codepoint | Unicode category | Jamo type | Glyph                            |
|:----------|:-----------------|:----------|:---------------------------------|
|`U+1100`   | Letter           | L         | &#x1100; Kiyeok                  |
|`U+1101`   | Letter           | L         | &#x1101; Ssangkiyeok             |
|`U+1102`   | Letter           | L         | &#x1102; Nieun                   |
|`U+1103`   | Letter           | L         | &#x1103; Tikeut                  |
|`U+1104`   | Letter           | L         | &#x1104; Ssangtikeut             |
|`U+1105`   | Letter           | L         | &#x1105; Rieul                   |
|`U+1106`   | Letter           | L         | &#x1106; Mieum                   |
|`U+1107`   | Letter           | L         | &#x1107; Pieup                   |
|`U+1108`   | Letter           | L         | &#x1108; Ssangpieup              |
|`U+1109`   | Letter           | L         | &#x1109; Sios                    |
|`U+110A`   | Letter           | L         | &#x110A; Ssangsios               |
|`U+110B`   | Letter           | L         | &#x110B; Ieung                   |
|`U+110C`   | Letter           | L         | &#x110C; Cieuc                   |
|`U+110D`   | Letter           | L         | &#x110D; Ssangcieuc              |
|`U+110E`   | Letter           | L         | &#x110E; Chieuch                 |
|`U+110F`   | Letter           | L         | &#x110F; Khieukh                 |
| | | | |
|`U+1110`   | Letter           | L         | &#x1110; Thieuth                 |
|`U+1111`   | Letter           | L         | &#x1111; Phieuph                 |
|`U+1112`   | Letter           | L         | &#x1112; Hieuh                   |
|`U+1113`   | Letter           | L         | &#x1113; Nieun-Kiyeok            |
|`U+1114`   | Letter           | L         | &#x1114; Ssangnieun              |
|`U+1115`   | Letter           | L         | &#x1115; Nieun-Tikeut            |
|`U+1116`   | Letter           | L         | &#x1116; Nieun-Pieup             |
|`U+1117`   | Letter           | L         | &#x1117; Tikeut-Kiyeok           |
|`U+1118`   | Letter           | L         | &#x1118; Rieul-Nieun             |
|`U+1119`   | Letter           | L         | &#x1119; Ssangrieul              |
|`U+111A`   | Letter           | L         | &#x111A; Rieul-Hieuh             |
|`U+111B`   | Letter           | L         | &#x111B; Kapyeounrieul           |
|`U+111C`   | Letter           | L         | &#x111C; Mieum-Pieup             |
|`U+111D`   | Letter           | L         | &#x111D; Kapyeounmieum           |
|`U+111E`   | Letter           | L         | &#x111E; Pieup-Kiyeok            |
|`U+111F`   | Letter           | L         | &#x111F; Pieup-Nieun             |
| | | | |
|`U+1120`   | Letter           | L         | &#x1120; Pieup-Tikeut            |
|`U+1121`   | Letter           | L         | &#x1121; Pieup-Sios              |
|`U+1122`   | Letter           | L         | &#x1122; Pieup-Sios-Kiyeok       |
|`U+1123`   | Letter           | L         | &#x1123; Pieup-Sios-Tikeut       |
|`U+1124`   | Letter           | L         | &#x1124; Pieup-Sios-Pieup        |
|`U+1125`   | Letter           | L         | &#x1125; Pieup-Ssangsios         |
|`U+1126`   | Letter           | L         | &#x1126; Pieup-Sios-Cieuc        |
|`U+1127`   | Letter           | L         | &#x1127; Pieup-Cieuc             |
|`U+1128`   | Letter           | L         | &#x1128; Pieup-Chieuch           |
|`U+1129`   | Letter           | L         | &#x1129; Pieup-Thieuth           |
|`U+112A`   | Letter           | L         | &#x112A; Pieup-Phieuph           |
|`U+112B`   | Letter           | L         | &#x112B; Kapyeounpieup           |
|`U+112C`   | Letter           | L         | &#x112C; Kapyeounssangpieup      |
|`U+112D`   | Letter           | L         | &#x112D; Sios-Kiyeok             |
|`U+112E`   | Letter           | L         | &#x112E; Sios-Nieun              |
|`U+112F`   | Letter           | L         | &#x112F; Sios-Tikeut             |
| | | | |
|`U+1130`   | Letter           | L         | &#x1130; Sios-Rieul              |
|`U+1131`   | Letter           | L         | &#x1131; Sios-Mieum              |
|`U+1132`   | Letter           | L         | &#x1132; Sios-Pieup              |
|`U+1133`   | Letter           | L         | &#x1133; Sios-Pieup-Kiyeok       |
|`U+1134`   | Letter           | L         | &#x1134; Sios-Ssangsios          |
|`U+1135`   | Letter           | L         | &#x1135; Sios-Ieung              |
|`U+1136`   | Letter           | L         | &#x1136; Sios-Cieuc              |
|`U+1137`   | Letter           | L         | &#x1137; Sios-Chieuch            |
|`U+1138`   | Letter           | L         | &#x1138; Sios-Khieukh            |
|`U+1139`   | Letter           | L         | &#x1139; Sios-Thieuth            |
|`U+113A`   | Letter           | L         | &#x113A; Sios-Phieuph            |
|`U+113B`   | Letter           | L         | &#x113B; Sios-Hieuh              |
|`U+113C`   | Letter           | L         | &#x113C; Chitueumsios            |
|`U+113D`   | Letter           | L         | &#x113D; Chitueumssangsios       |
|`U+113E`   | Letter           | L         | &#x113E; Ceongchieumsios         |
|`U+113F`   | Letter           | L         | &#x113F; Ceongchieumssangsios    |
| | | | |
|`U+1140`   | Letter           | L         | &#x1140; Pansios                 |
|`U+1141`   | Letter           | L         | &#x1141; Ieung-Kiyeok            |
|`U+1142`   | Letter           | L         | &#x1142; Ieung-Tikeut            |
|`U+1143`   | Letter           | L         | &#x1143; Ieung-Mieum             |
|`U+1144`   | Letter           | L         | &#x1144; Ieung-Pieup             |
|`U+1145`   | Letter           | L         | &#x1145; Ieung-Sios              |
|`U+1146`   | Letter           | L         | &#x1146; Ieung-Pansios           |
|`U+1147`   | Letter           | L         | &#x1147; Ssangieung              |
|`U+1148`   | Letter           | L         | &#x1148; Ieung-Cieuc             |
|`U+1149`   | Letter           | L         | &#x1149; Ieung-Chieuch           |
|`U+114A`   | Letter           | L         | &#x114A; Ieung-Thieuth           |
|`U+114B`   | Letter           | L         | &#x114B; Ieung-Phieuph           |
|`U+114C`   | Letter           | L         | &#x114C; Yesieung                |
|`U+114D`   | Letter           | L         | &#x114D; Cieuc-Ieung             |
|`U+114E`   | Letter           | L         | &#x114E; Chitueumcieuc           |
|`U+114F`   | Letter           | L         | &#x114F; Chitueumssangcieuc      |
| | | | |
|`U+1150`   | Letter           | L         | &#x1150; Ceongchieumcieuc        |
|`U+1151`   | Letter           | L         | &#x1151; Ceongchieumssangcieuc   |
|`U+1152`   | Letter           | L         | &#x1152; Chieuch-Khieukh         |
|`U+1153`   | Letter           | L         | &#x1153; Chieuch-Hieuh           |
|`U+1154`   | Letter           | L         | &#x1154; Chitueumchieuch         |
|`U+1155`   | Letter           | L         | &#x1155; Ceongchieumchieuch      |
|`U+1156`   | Letter           | L         | &#x1156; Phieuph-Pieup           |
|`U+1157`   | Letter           | L         | &#x1157; Kapyeounphieuph         |
|`U+1158`   | Letter           | L         | &#x1158; Ssanghieuh              |
|`U+1159`   | Letter           | L         | &#x1159; Yeorinhieuh             |
|`U+115A`   | Letter           | L         | &#x115A; Kiyeok-Tikeut           |
|`U+115B`   | Letter           | L         | &#x115B; Nieun-Sios              |
|`U+115C`   | Letter           | L         | &#x115C; Nieun-Cieuc             |
|`U+115D`   | Letter           | L         | &#x115D; Nieun-Hieuh             |
|`U+115E`   | Letter           | L         | &#x115E; Tikeut-Rieul            |
|`U+115F`   | Letter           | Lf        | &#x115F; Choseong Filler         |
| | | | |
|`U+1160`   | Letter           | Vf        | &#x1160; Jungseong Filler        |
|`U+1161`   | Letter           | V         | &#x1161; A                       |
|`U+1162`   | Letter           | V         | &#x1162; Ae                      |
|`U+1163`   | Letter           | V         | &#x1163; Ya                      |
|`U+1164`   | Letter           | V         | &#x1164; Yae                     |
|`U+1165`   | Letter           | V         | &#x1165; Eo                      |
|`U+1166`   | Letter           | V         | &#x1166; E                       |
|`U+1167`   | Letter           | V         | &#x1167; Yeo                     |
|`U+1168`   | Letter           | V         | &#x1168; Ye                      |
|`U+1169`   | Letter           | V         | &#x1169; O                       |
|`U+116A`   | Letter           | V         | &#x116A; Wa                      |
|`U+116B`   | Letter           | V         | &#x116B; Wae                     |
|`U+116C`   | Letter           | V         | &#x116C; Oe                      |
|`U+116D`   | Letter           | V         | &#x116D; Yo                      |
|`U+116E`   | Letter           | V         | &#x116E; U                       |
|`U+116F`   | Letter           | V         | &#x116F; Weo                     |
| | | | |
|`U+1170`   | Letter           | V         | &#x1170; We                      |
|`U+1171`   | Letter           | V         | &#x1171; Wi                      |
|`U+1172`   | Letter           | V         | &#x1172; Yu                      |
|`U+1173`   | Letter           | V         | &#x1173; Eu                      |
|`U+1174`   | Letter           | V         | &#x1174; Yi                      |
|`U+1175`   | Letter           | V         | &#x1175; I                       |
|`U+1176`   | Letter           | V         | &#x1176; A-O                     |
|`U+1177`   | Letter           | V         | &#x1177; A-U                     |
|`U+1178`   | Letter           | V         | &#x1178; Ya-O                    |
|`U+1179`   | Letter           | V         | &#x1179; Ya-Yo                   |
|`U+117A`   | Letter           | V         | &#x117A; Eo-O                    |
|`U+117B`   | Letter           | V         | &#x117B; Eo-U                    |
|`U+117C`   | Letter           | V         | &#x117C; Eo-Eu                   |
|`U+117D`   | Letter           | V         | &#x117D; Yeo-O                   |
|`U+117E`   | Letter           | V         | &#x117E; Yeo-U                   |
|`U+117F`   | Letter           | V         | &#x117F; O-Eo                    |
| | | | |
|`U+1180`   | Letter           | V         | &#x1180; O-E                     |
|`U+1181`   | Letter           | V         | &#x1181; O-Ye                    |
|`U+1182`   | Letter           | V         | &#x1182; O-O                     |
|`U+1183`   | Letter           | V         | &#x1183; O-U                     |
|`U+1184`   | Letter           | V         | &#x1184; Yo-Ya                   |
|`U+1185`   | Letter           | V         | &#x1185; Yo-Yae                  |
|`U+1186`   | Letter           | V         | &#x1186; Yo-Yeo                  |
|`U+1187`   | Letter           | V         | &#x1187; Yo-O                    |
|`U+1188`   | Letter           | V         | &#x1188; Yo-I                    |
|`U+1189`   | Letter           | V         | &#x1189; U-A                     |
|`U+118A`   | Letter           | V         | &#x118A; U-Ae                    |
|`U+118B`   | Letter           | V         | &#x118B; U-Eo-Eu                 |
|`U+118C`   | Letter           | V         | &#x118C; U-Ye                    |
|`U+118D`   | Letter           | V         | &#x118D; U-U                     |
|`U+118E`   | Letter           | V         | &#x118E; Yu-A                    |
|`U+118F`   | Letter           | V         | &#x118F; Yu-Eo                   |
| | | | |
|`U+1190`   | Letter           | V         | &#x1190; Yu-E                    |
|`U+1191`   | Letter           | V         | &#x1191; Yu-Yeo                  |
|`U+1192`   | Letter           | V         | &#x1192; Yu-Ye                   |
|`U+1193`   | Letter           | V         | &#x1193; Yu-U                    |
|`U+1194`   | Letter           | V         | &#x1194; Yu-I                    |
|`U+1195`   | Letter           | V         | &#x1195; Eu-U                    |
|`U+1196`   | Letter           | V         | &#x1196; Eu-Eu                   |
|`U+1197`   | Letter           | V         | &#x1197; Yi-U                    |
|`U+1198`   | Letter           | V         | &#x1198; I-A                     |
|`U+1199`   | Letter           | V         | &#x1199; I-Ya                    |
|`U+119A`   | Letter           | V         | &#x119A; I-O                     |
|`U+119B`   | Letter           | V         | &#x119B; I-U                     |
|`U+119C`   | Letter           | V         | &#x119C; I-Eu                    |
|`U+119D`   | Letter           | V         | &#x119D; I-Araea                 |
|`U+119E`   | Letter           | V         | &#x119E; Araea                   |
|`U+119F`   | Letter           | V         | &#x119F; Araea-Eo                |
| | | | |
|`U+11A0`   | Letter           | V         | &#x11A0; Araea-U                 |
|`U+11A1`   | Letter           | V         | &#x11A1; Araea-I                 |
|`U+11A2`   | Letter           | V         | &#x11A2; Ssangaraea              |
|`U+11A3`   | Letter           | V         | &#x11A3; A-Eu                    |
|`U+11A4`   | Letter           | V         | &#x11A4; Ya-U                    |
|`U+11A5`   | Letter           | V         | &#x11A5; Yeo-Ya                  |
|`U+11A6`   | Letter           | V         | &#x11A6; O-Ya                    |
|`U+11A7`   | Letter           | V         | &#x11A7; O-Yae                   |
|`U+11A8`   | Letter           | T         | &#x11A8; Kiyeok                  |
|`U+11A9`   | Letter           | T         | &#x11A9; Ssangkiyeok             |
|`U+11AA`   | Letter           | T         | &#x11AA; Kiyeok-Sios             |
|`U+11AB`   | Letter           | T         | &#x11AB; Nieun                   |
|`U+11AC`   | Letter           | T         | &#x11AC; Nieun-Cieuc             |
|`U+11AD`   | Letter           | T         | &#x11AD; Nieun-Hieuh             |
|`U+11AE`   | Letter           | T         | &#x11AE; Tikeut                  |
|`U+11AF`   | Letter           | T         | &#x11AF; Rieul                   |
| | | | |
|`U+11B0`   | Letter           | T         | &#x11B0; Rieul-Kiyeok            |
|`U+11B1`   | Letter           | T         | &#x11B1; Rieul-Mieum             |
|`U+11B2`   | Letter           | T         | &#x11B2; Rieul-Pieup             |
|`U+11B3`   | Letter           | T         | &#x11B3; Rieul-Sios              |
|`U+11B4`   | Letter           | T         | &#x11B4; Rieul-Thieuth           |
|`U+11B5`   | Letter           | T         | &#x11B5; Rieul-Phieuph           |
|`U+11B6`   | Letter           | T         | &#x11B6; Rieul-Hieuh             |
|`U+11B7`   | Letter           | T         | &#x11B7; Mieum                   |
|`U+11B8`   | Letter           | T         | &#x11B8; Pieup                   |
|`U+11B9`   | Letter           | T         | &#x11B9; Pieup-Sios              |
|`U+11BA`   | Letter           | T         | &#x11BA; Sios                    |
|`U+11BB`   | Letter           | T         | &#x11BB; Ssangsios               |
|`U+11BC`   | Letter           | T         | &#x11BC; Ieung                   |
|`U+11BD`   | Letter           | T         | &#x11BD; Cieuc                   |
|`U+11BE`   | Letter           | T         | &#x11BE; Chieuch                 |
|`U+11BF`   | Letter           | T         | &#x11BF; Khieukh                 |
| | | | |
|`U+11C0`   | Letter           | T         | &#x11C0; Thieuth                 |
|`U+11C1`   | Letter           | T         | &#x11C1; Phieuph                 |
|`U+11C2`   | Letter           | T         | &#x11C2; Hieuh                   |
|`U+11C3`   | Letter           | T         | &#x11C3; Kiyeok-Rieul            |
|`U+11C4`   | Letter           | T         | &#x11C4; Kiyeok-Sios-Kiyeok      |
|`U+11C5`   | Letter           | T         | &#x11C5; Nieun-Kiyeok            |
|`U+11C6`   | Letter           | T         | &#x11C6; Nieun-Tikeut            |
|`U+11C7`   | Letter           | T         | &#x11C7; Nieun-Sios              |
|`U+11C8`   | Letter           | T         | &#x11C8; Nieun-Pansios           |
|`U+11C9`   | Letter           | T         | &#x11C9; Nieun-Thieuth           |
|`U+11CA`   | Letter           | T         | &#x11CA; Tikeut-Kiyeok           |
|`U+11CB`   | Letter           | T         | &#x11CB; Tikeut-Rieul            |
|`U+11CC`   | Letter           | T         | &#x11CC; Rieul-Kiyeok-Sios       |
|`U+11CD`   | Letter           | T         | &#x11CD; Rieul-Nieun             |
|`U+11CE`   | Letter           | T         | &#x11CE; Rieul-Tikeut            |
|`U+11CF`   | Letter           | T         | &#x11CF; Rieul-Tikeut-Hieuh      |
| | | | |
|`U+11D0`   | Letter           | T         | &#x11D0; Ssangrieul              |
|`U+11D1`   | Letter           | T         | &#x11D1; Rieul-Mieum-Kiyeok      |
|`U+11D2`   | Letter           | T         | &#x11D2; Rieul-Mieum-Sios        |
|`U+11D3`   | Letter           | T         | &#x11D3; Rieul-Pieup-Sios        |
|`U+11D4`   | Letter           | T         | &#x11D4; Rieul-Pieup-Hieuh       |
|`U+11D5`   | Letter           | T         | &#x11D5; Rieul-Kapyeounpieup     |
|`U+11D6`   | Letter           | T         | &#x11D6; Rieul-Ssangsios         |
|`U+11D7`   | Letter           | T         | &#x11D7; Rieul-Pansios           |
|`U+11D8`   | Letter           | T         | &#x11D8; Rieul-Khieukh           |
|`U+11D9`   | Letter           | T         | &#x11D9; Rieul-Yeorinhieuh       |
|`U+11DA`   | Letter           | T         | &#x11DA; Mieum-Kiyeok            |
|`U+11DB`   | Letter           | T         | &#x11DB; Mieum-Rieul             |
|`U+11DC`   | Letter           | T         | &#x11DC; Mieum-Pieup             |
|`U+11DD`   | Letter           | T         | &#x11DD; Mieum-Sios              |
|`U+11DE`   | Letter           | T         | &#x11DE; Mieum-Ssangsios         |
|`U+11DF`   | Letter           | T         | &#x11DF; Mieum-Pansios           |
| | | | |
|`U+11E0`   | Letter           | T         | &#x11E0; Mieum-Chieuch           |
|`U+11E1`   | Letter           | T         | &#x11E1; Mieum-Hieuh             |
|`U+11E2`   | Letter           | T         | &#x11E2; Kapyeounmieum           |
|`U+11E3`   | Letter           | T         | &#x11E3; Pieup-Rieul             |
|`U+11E4`   | Letter           | T         | &#x11E4; Pieup-Phieuph           |
|`U+11E5`   | Letter           | T         | &#x11E5; Pieup-Hieuh             |
|`U+11E6`   | Letter           | T         | &#x11E6; Kapyeounpieup           |
|`U+11E7`   | Letter           | T         | &#x11E7; Sios-Kiyeok             |
|`U+11E8`   | Letter           | T         | &#x11E8; Sios-Tikeut             |
|`U+11E9`   | Letter           | T         | &#x11E9; Sios-Rieul              |
|`U+11EA`   | Letter           | T         | &#x11EA; Sios-Pieup              |
|`U+11EB`   | Letter           | T         | &#x11EB; Pansios                 |
|`U+11EC`   | Letter           | T         | &#x11EC; Ieung-Kiyeok            |
|`U+11ED`   | Letter           | T         | &#x11ED; Ieung-Ssangkiyeok       |
|`U+11EE`   | Letter           | T         | &#x11EE; Ssangieung              |
|`U+11EF`   | Letter           | T         | &#x11EF; Ieung-Khieukh           |
| | | | |
|`U+11F0`   | Letter           | T         | &#x11F0; Yesieung                |
|`U+11F1`   | Letter           | T         | &#x11F1; Yesieung-Sios           |
|`U+11F2`   | Letter           | T         | &#x11F2; Yesieung-Pansios        |
|`U+11F3`   | Letter           | T         | &#x11F3; Phieuph-Pieup           |
|`U+11F4`   | Letter           | T         | &#x11F4; Kapyeounphieuph         |
|`U+11F5`   | Letter           | T         | &#x11F5; Hieuh-Nieun             |
|`U+11F6`   | Letter           | T         | &#x11F6; Hieuh-Rieul             |
|`U+11F7`   | Letter           | T         | &#x11F7; Hieuh-Mieum             |
|`U+11F8`   | Letter           | T         | &#x11F8; Hieuh-Pieup             |
|`U+11F9`   | Letter           | T         | &#x11F9; Yeorinhieuh             |
|`U+11FA`   | Letter           | T         | &#x11FA; Kiyeok-Nieun            |
|`U+11FB`   | Letter           | T         | &#x11FB; Kiyeok-Pieup            |
|`U+11FC`   | Letter           | T         | &#x11FC; Kiyeok-Chieuch          |
|`U+11FD`   | Letter           | T         | &#x11FD; Kiyeok-Khieukh          |
|`U+11FE`   | Letter           | T         | &#x11FE; Kiyeok-Hieuh            |
|`U+11FF`   | Letter           | T         | &#x11FF; Ssangnieun              |


## Hangul Jamo Extended-A character table ##

Hangul Jamo should be classified as in the following
table. Codepoints in the Hangul Jamo Extended-A block with no assigned
meaning are designated as _unassigned_ in the _Unicode category_ column. 

The _Jamo type_ column indicates the syllable-component type of the
jamo. All assigned codepoints in the Hangul Jamo Extended-A block are
classified as type "L" for leading consonants (choseong).


| Codepoint | Unicode category | Jamo type | Glyph                            |
|:----------|:-----------------|:----------|:---------------------------------|
|`U+A960`   | Letter           | L         | &#xA960; Tikeut-Mieum            |
|`U+A961`   | Letter           | L         | &#xA961; Tikeut-Pieup            |
|`U+A962`   | Letter           | L         | &#xA962; Tikeut-Sios             |
|`U+A963`   | Letter           | L         | &#xA963; Tikeut-Cieuc            |
|`U+A964`   | Letter           | L         | &#xA964; Rieul-Kiyeok            |
|`U+A965`   | Letter           | L         | &#xA965; Rieul-Ssangkiyeok       |
|`U+A966`   | Letter           | L         | &#xA966; Rieul-Tikeut            |
|`U+A967`   | Letter           | L         | &#xA967; Rieul-Ssangtikeut       |
|`U+A968`   | Letter           | L         | &#xA968; Rieul-Mieum             |
|`U+A969`   | Letter           | L         | &#xA969; Rieul-Pieup             |
|`U+A96A`   | Letter           | L         | &#xA96A; Rieul-Ssangpieup        |
|`U+A96B`   | Letter           | L         | &#xA96B; Rieul-Kapyeounpieup     |
|`U+A96C`   | Letter           | L         | &#xA96C; Rieul-Sios              |
|`U+A96D`   | Letter           | L         | &#xA96D; Rieul-Cieuc             |
|`U+A96E`   | Letter           | L         | &#xA96E; Rieul-Khieukh           |
|`U+A96F`   | Letter           | L         | &#xA96F; Mieum-Kiyeok            |
| | | | |
|`U+A970`   | Letter           | L         | &#xA970; Mieum-Tikeut            |
|`U+A971`   | Letter           | L         | &#xA971; Mieum-Sios              |
|`U+A972`   | Letter           | L         | &#xA972; Pieup-Sios-Thieuth      |
|`U+A973`   | Letter           | L         | &#xA973; Pieup-Khieukh           |
|`U+A974`   | Letter           | L         | &#xA974; Pieup-Hieuh             |
|`U+A975`   | Letter           | L         | &#xA975; Ssangsios-Pieup         |
|`U+A976`   | Letter           | L         | &#xA976; Ieung-Rieul             |
|`U+A977`   | Letter           | L         | &#xA977; Ieung-Hieuh             |
|`U+A978`   | Letter           | L         | &#xA978; Ssangcieuc-Hieuh        |
|`U+A979`   | Letter           | L         | &#xA979; Ssangthieuth            |
|`U+A97A`   | Letter           | L         | &#xA97A; Phieuph-Hieuh           |
|`U+A97B`   | Letter           | L         | &#xA97B; Hieuh-Sios              |
|`U+A97C`   | Letter           | L         | &#xA97C; Ssangyeorinhieuh        |
|`U+A97D`   | _unassigned_     |           |                                  |
|`U+A97E`   | _unassigned_     |           |                                  |
|`U+A97F`   | _unassigned_     |           |                                  |



## Hangul Jamo Extended-B character table ##

Hangul Jamo should be classified as in the following
table. Codepoints in the Hangul Jamo Extended-B block with no assigned
meaning are designated as _unassigned_ in the _Unicode category_ column. 

The _Jamo type_ column indicates the syllable-component type of the
jamo. "V" for vowels (jungseong) and "T" for trailing consonants (jongseong).


| Codepoint | Unicode category | Jamo type | Glyph                            |
|:----------|:-----------------|:----------|:---------------------------------|
|`U+D7B0`   | Letter           | V         | &#xD7B0; O-Yeo                   |
|`U+D7B1`   | Letter           | V         | &#xD7B1; O-O-I                   |
|`U+D7B2`   | Letter           | V         | &#xD7B2; Yo-A                    |
|`U+D7B3`   | Letter           | V         | &#xD7B3; Yo-Ae                   |
|`U+D7B4`   | Letter           | V         | &#xD7B4; Yo-Eo                   |
|`U+D7B5`   | Letter           | V         | &#xD7B5; U-Yeo                   |
|`U+D7B6`   | Letter           | V         | &#xD7B6; U-I-I                   |
|`U+D7B7`   | Letter           | V         | &#xD7B7; Yu-Ae                   |
|`U+D7B8`   | Letter           | V         | &#xD7B8; Yu-O                    |
|`U+D7B9`   | Letter           | V         | &#xD7B9; Eu-A                    |
|`U+D7BA`   | Letter           | V         | &#xD7BA; Eu-Eo                   |
|`U+D7BB`   | Letter           | V         | &#xD7BB; Eu-E                    |
|`U+D7BC`   | Letter           | V         | &#xD7BC; Eu-O                    |
|`U+D7BD`   | Letter           | V         | &#xD7BD; I-Ya-O                  |
|`U+D7BE`   | Letter           | V         | &#xD7BE; I-Yae                   |
|`U+D7BF`   | Letter           | V         | &#xD7BF; I-Yeo                   |
| | | | |
|`U+D7C0`   | Letter           | V         | &#xD7C0; I-Ye                    |
|`U+D7C1`   | Letter           | V         | &#xD7C1; I-O-I                   |
|`U+D7C2`   | Letter           | V         | &#xD7C2; I-Yo                    |
|`U+D7C3`   | Letter           | V         | &#xD7C3; I-Yu                    |
|`U+D7C4`   | Letter           | V         | &#xD7C4; I-I                     |
|`U+D7C5`   | Letter           | V         | &#xD7C5; Araea-A                 |
|`U+D7C6`   | Letter           | V         | &#xD7C6; Araea-E                 |
|`U+D7C7`   | _unassigned_     |           |                                  |
|`U+D7C8`   | _unassigned_     |           |                                  |
|`U+D7C9`   | _unassigned_     |           |                                  |
|`U+D7CA`   | _unassigned_     |           |                                  |
|`U+D7CB`   | Letter           | T         | &#xD7CB; Nieun-Rieul             |
|`U+D7CC`   | Letter           | T         | &#xD7CC; Nieun-Chieuch           |
|`U+D7CD`   | Letter           | T         | &#xD7CD; Ssangtikeut             |
|`U+D7CE`   | Letter           | T         | &#xD7CE; Ssangtikeut-Pieup       |
|`U+D7CF`   | Letter           | T         | &#xD7CF; Tikeut-Pieup            |
| | | | |
|`U+D7D0`   | Letter           | T         | &#xD7D0; Tikeut-Sios             |
|`U+D7D1`   | Letter           | T         | &#xD7D1; Tikeut-Sios-Kiyeok      |
|`U+D7D2`   | Letter           | T         | &#xD7D2; Tikeut-Cieuc            |
|`U+D7D3`   | Letter           | T         | &#xD7D3; Tikeut-Chieuch          |
|`U+D7D4`   | Letter           | T         | &#xD7D4; Tikeut-Thieuth          |
|`U+D7D5`   | Letter           | T         | &#xD7D5; Rieul-Ssangkiyeok       |
|`U+D7D6`   | Letter           | T         | &#xD7D6; Rieul-Kiyeok-Hieuh      |
|`U+D7D7`   | Letter           | T         | &#xD7D7; Ssangrieul-Khieukh      |
|`U+D7D8`   | Letter           | T         | &#xD7D8; Rieul-Mieum-Hieuh       |
|`U+D7D9`   | Letter           | T         | &#xD7D9; Rieul-Pieup-Tikeut      |
|`U+D7DA`   | Letter           | T         | &#xD7DA; Rieul-Pieup-Phieuph     |
|`U+D7DB`   | Letter           | T         | &#xD7DB; Rieul-Yesieung          |
|`U+D7DC`   | Letter           | T         | &#xD7DC; Rieul-Yeorinhieuh-Hieuh |
|`U+D7DD`   | Letter           | T         | &#xD7DD; Kapyeounrieul           |
|`U+D7DE`   | Letter           | T         | &#xD7DE; Mieum-Nieun             |
|`U+D7DF`   | Letter           | T         | &#xD7DF; Mieum-Ssangnieun        |
| | | | |
|`U+D7E0`   | Letter           | T         | &#xD7E0; Ssangmieum              |
|`U+D7E1`   | Letter           | T         | &#xD7E1; Mieum-Pieup-Sios        |
|`U+D7E2`   | Letter           | T         | &#xD7E2; Mieum-Cieuc             |
|`U+D7E3`   | Letter           | T         | &#xD7E3; Pieup-Tikeut            |
|`U+D7E4`   | Letter           | T         | &#xD7E4; Pieup-Rieul-Phieuph     |
|`U+D7E5`   | Letter           | T         | &#xD7E5; Pieup-Mieum             |
|`U+D7E6`   | Letter           | T         | &#xD7E6; Ssangpieup              |
|`U+D7E7`   | Letter           | T         | &#xD7E7; Pieup-Sios-Tikeut       |
|`U+D7E8`   | Letter           | T         | &#xD7E8; Pieup-Cieuc             |
|`U+D7E9`   | Letter           | T         | &#xD7E9; Pieup-Chieuch           |
|`U+D7EA`   | Letter           | T         | &#xD7EA; Sios-Mieum              |
|`U+D7EB`   | Letter           | T         | &#xD7EB; Sios-Kapyeounpieup      |
|`U+D7EC`   | Letter           | T         | &#xD7EC; Ssangsios-Kiyeok        |
|`U+D7ED`   | Letter           | T         | &#xD7ED; Ssangsios-Tikeut        |
|`U+D7EE`   | Letter           | T         | &#xD7EE; Sios-Pansios            |
|`U+D7EF`   | Letter           | T         | &#xD7EF; Sios-Cieuc              |
| | | | |
|`U+D7F0`   | Letter           | T         | &#xD7F0; Sios-Chieuch            |
|`U+D7F1`   | Letter           | T         | &#xD7F1; Sios-Thieuth            |
|`U+D7F2`   | Letter           | T         | &#xD7F2; Sios-Hieuh              |
|`U+D7F3`   | Letter           | T         | &#xD7F3; Pansios-Pieup           |
|`U+D7F4`   | Letter           | T         | &#xD7F4; Pansios-Kapyeounpieup   |
|`U+D7F5`   | Letter           | T         | &#xD7F5; Yesieung-Mieum          |
|`U+D7F6`   | Letter           | T         | &#xD7F6; Yesieung-Hieuh          |
|`U+D7F7`   | Letter           | T         | &#xD7F7; Cieuc-Pieup             |
|`U+D7F8`   | Letter           | T         | &#xD7F8; Cieuc-Ssangpieup        |
|`U+D7F9`   | Letter           | T         | &#xD7F9; Ssangcieuc              |
|`U+D7FA`   | Letter           | T         | &#xD7FA; Phieuph-Sios            |
|`U+D7FB`   | Letter           | T         | &#xD7FB; Phieuph-Thieuth         |
|`U+D7FC`   | _unassigned_     |           |                                  |
|`U+D7FD`   | _unassigned_     |           |                                  |
|`U+D7FE`   | _unassigned_     |           |                                  |
|`U+D7FF`   | _unassigned_     |           |                                  |



## Miscellaneous character table ##

In addition to general punctuation, runs of Hangul text may use
punctuation marks from the CJK Symbols And Punctuation block. 

Of particular note are the single-dot tone mark (single-dot bangjeom)
and double-dot tone mark (double-dot bangjeom), `U+302E` and
`U+302F`. These non-spacing marks are common in Old Korean.


| Codepoint | Unicode category | Jamo type | Glyph                            |
|:----------|:-----------------|:----------|:---------------------------------|
|`U+302E`   | Mark [Mn]        | _null_    | &#x302E; Single Dot Tone Mark    |
|`U+302F`   | Mark [Mn]        | _null_    | &#x302F; Double Dot Tone Mark    |


Other important characters that may be encountered when shaping runs
of Hangul text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`), and zero-width non-joiner (`U+200C`).

The dotted-circle placeholder is frequently used when displaying a
mark in isolation. Real-world text may also use other characters, such
as hyphens or dashes, in a similar placeholder fashion; shaping
engines should cope with this situation gracefully.

The zero-width space (`U+200B`) or word joiner (`U+2060`) may be used
between two jamo to prevent them from being conjoined into a
syllable. The zero-width space allows a line break to happen between
the jamo, while the word joiner prevents the jamo from being separated
by a line break.


| Codepoint | Unicode category | Jamo type | Glyph                            |
|:----------|:-----------------|:----------|:---------------------------------|
|`U+200B`   | Separator        | _null_    | &#x200B; Zero-width space        |
|`U+200C`   | Other            | _null_    | &#x200C; Zero-width non-joiner   |
|`U+200D`   | Other            | _null_    | &#x200D; Zero-width joiner       |
|`U+2060`   | Other            | _null_    | &#x2060; Word joiner             |
|`U+25CC`   | Symbol           | _null_    | &#x25CC; Dotted circle           |
