# Commands used to generate the images in [opentype-shaping-hangul.md](../../opentype-shaping-hangul.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-ljmo,-vjmo,-tjmo` in examples where
> the jamo features are not being explained. This may not be
> neccessary in all fonts.


## LV example

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-lv-syllable.svg --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110e,1166


## LVT example

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-lvt-syllable.svg --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110e,1166,11ae


## 3. Compose the syllable

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-compose-before.svg --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=1108,200b,1171,200b,11b8

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-compose-after.svg --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=1108,1171,11b8

svg_stack --direction=h hangul-compose-before.svg right-arrow.svg hangul-compose-after.svg > hangul-compose.svg


## 4. Decompose the syllable

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-decompose-before.svg --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=1106,1172,11af

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-decompose-after.svg --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=3141,200b,3160,200b,3139

svg_stack --direction=h hangul-decompose-before.svg right-arrow.svg hangul-decompose-after.svg > hangul-decompose.svg


## 5.2 `ljmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-ljmo-before.svg --features=-ljmo,-vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,200b,1169,200b,11bb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-ljmo-after.svg --features=+ljmo,-vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,200b,1169,200b,11bb

svg_stack --direction=h hangul-ljmo-before.svg right-arrow.svg hangul-ljmo-after.svg > hangul-ljmo.svg


## 5.3 `vjmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-vjmo-before.svg --features=+ljmo,-vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,200b,1169,200b,11bb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-vjmo-after.svg --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,1169,200b,11bb

svg_stack --direction=h hangul-vjmo-before.svg right-arrow.svg hangul-vjmo-after.svg > hangul-vjmo.svg


## 5.4 `tjmo`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tjmo-before.svg --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,1169,200b,11bb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tjmo-after.svg --features=+ljmo,+vjmo,+tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=110f,1169,11bb

svg_stack --direction=h hangul-tjmo-before.svg right-arrow.svg hangul-tjmo-after.svg > hangul-tjmo.svg


## 6. Tone marks

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tone-before.svg --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=1111,116b,11a8,200c,302f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hangul-tone-after.svg --features=+ljmo,+vjmo,-tjmo --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifKR-Regular.otf --unicodes=1111,116b,11a8,302f

svg_stack.py --direction=h hangul-tone-before.svg right-arrow.svg hangul-tone-after.svg > hangul-tone.svg
































