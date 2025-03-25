# Commands used to generate the images in [opentype-shaping-hebrew.md](../../opentype-shaping-hebrew.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-ccmp-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05b3,05bd

hb-view --font-size=110 --margin=2,24,2,24 --output-file=hebrew-ccmp-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05b3,05bd

svg_stack --direction=h hebrew-ccmp-before.svg right-arrow.svg hebrew-ccmp-after.svg > hebrew-ccmp.svg


## 2 Alphabetic Presentation Forms

> Note: Noto Sans Hebrew implements these compositions in a `ccmp` lookup.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05e7,05bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05e7,05bc

svg_stack --direction=h hebrew-apf-before.svg right-arrow.svg hebrew-apf-after.svg > hebrew-apf.svg


## 4.1 `liga`

hb-view --font-size=110 --margin=2,16,2,24 --output-file=hebrew-liga-before.svg --features=-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=fb4f,05b1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-liga-after.svg --features=+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=fb4f,05b1

svg_stack --direction=h hebrew-liga-before.svg right-arrow.svg hebrew-liga-after.svg > hebrew-liga.svg


## 4.2 `dlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-before.svg --features=-dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05d0,05dc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-after.svg --features=+dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05d0,05dc

svg_stack --direction=h hebrew-dlig-before.svg right-arrow.svg hebrew-dlig-after.svg > hebrew-dlig.svg


## 5.1 `kern`

> Note: Noto Sans Hebrew has `kern` lookups, but so far I have not
> been able to identify an easily visible example pair.


## 5.2 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05e7,059a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf --unicodes=05e7,059a

svg_stack --direction=h hebrew-mark-before.svg right-arrow.svg hebrew-mark-after.svg > hebrew-mark.svg









































