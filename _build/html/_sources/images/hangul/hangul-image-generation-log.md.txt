# Commands used to generate the images in [opentype-shaping-hangul.md](../../opentype-shaping-hangul.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-ljmo,-vjmo,-tjmo` in examples where
> the jamo features are not being explained. This may not be
> neccessary in all fonts.


## LV example

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-lv-syllable.png --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110e,1166


## LVT example

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-lvt-syllable.png --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110e,1166,11a


## 3. Compose the syllable

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-compose-before.png --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1108,200b,1171,200b,11b8

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-compose-after.png --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1108,1171,11b8

montage hangul-compose-before.png right-arrow.png hangul-compose-after.png -geometry +0+0 -background transparent hangul-compose.png


## 4. Decompose the syllable

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-decompose-before.png --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1106,1172,11af

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-decompose-after.png --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1106,200d,1172,200d,11af

montage hangul-decompose-before.png right-arrow.png hangul-decompose-after.png -geometry +0+0 -background transparent hangul-decompose.png


## 5.2 `ljmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-ljmo-before.png --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-ljmo-after.png --features=+ljmo,-vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d9

montage hangul-ljmo-before.png right-arrow.png hangul-ljmo-after.png -geometry +0+0 -background transparent hangul-ljmo.png


## 5.3 `vjmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-vjmo-before.png --features=+ljmo,-vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-vjmo-after.png --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d

montage hangul-vjmo-before.png right-arrow.png hangul-vjmo-after.png -geometry +0+0 -background transparent hangul-vjmo.png


## 5.4 `tjmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tjmo-before.png --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tjmo-after.png --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=110f,200b,1169,200b,d7d9

montage hangul-tjmo-before.png right-arrow.png hangul-tjmo-after.png -geometry +0+0 -background transparent hangul-tjmo.png


## 6. Tone marks

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tone-before.png --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1111,116b,11a8,200c,302f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tone-after.png --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc --unicodes=1111,116b,11a8,302f


































