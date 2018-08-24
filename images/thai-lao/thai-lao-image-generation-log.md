# Commands used to generate the images in [opentype-shaping-thai-lao.md](../../opentype-shaping-thai-lao.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=2,16,2,32 --output-file=thai-ccmp-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf --unicodes=0e33

hb-view --font-size=110 --margin=2,16,2,32 --output-file=thai-ccmp-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf --unicodes=25cc,0e33


## 1.2 Decomposition






































