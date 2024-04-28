# Commands used to generate the images in [opentype-shaping-thai-lao.md](../../opentype-shaping-thai-lao.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-ccmp-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4a,0e4d

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-ccmp-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4a,0e4d

svg_stack --direction=h thai-ccmp-before.svg right-arrow.svg thai-ccmp-after.svg > thai-ccmp.svg

## 1.2 Decomposition

## 1.2 Am sign decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-am-decomposition-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=25cc,0eb3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-am-decomposition-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=25cc,0ecd,25cc,0eb2

svg_stack --direction=h lao-am-decomposition-before.svg right-arrow.svg lao-am-decomposition-after.svg > lao-am-decomposition.svg

## 4 `kern`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-kern-before.svg --features=-kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=0ec1,0e9a

 hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-kern-after.svg --features=+kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=0ec1,0e9a

svg_stack --direction=h lao-kern-before.svg right-arrow.svg lao-kern-after.svg > lao-kern.svg

## 4 `mark`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mark-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=0e0e,25cc,0e38

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mark-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=0e0e,0e38

svg_stack --direction=h thai-mark-before.svg right-arrow.svg thai-mark-after.svg > thai-mark.svg


## 4 `mkmk`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mkmk-before.svg --features=-mkmk --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e31,0e48

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mkmk-after.svg --features=+mkmk --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e31,0e48

svg_stack --direction=h thai-mkmk-before.svg right-arrow.svg thai-mkmk-after.svg > thai-mkmk.svg


## PUA 1 - Sara Am decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=thai-am-decomposition-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e33

hb-view --font-size=110 --margin=2,16,2,16 --output-file=thai-am-decomposition-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4d,25cc,0e32

svg_stack --direction=h thai-am-decomposition-before.svg right-arrow.svg thai-am-decomposition-after.svg > thai-am-decomposition.svg
























