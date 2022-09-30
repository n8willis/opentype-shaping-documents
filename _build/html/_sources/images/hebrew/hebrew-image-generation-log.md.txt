# Commands used to generate the images in [opentype-shaping-hebrew.md](../../opentype-shaping-hebrew.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-ccmp-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05b3,05bd

hb-view --font-size=110 --margin=2,24,2,24 --output-file=hebrew-ccmp-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05b3,05bd

montage hebrew-ccmp-before.png right-arrow.png hebrew-ccmp-after.png -geometry +0+0 -background transparent hebrew-ccmp.png


## 2 Alphabetic Presentation Forms

> Note: Noto Sans Hebrew implements these compositions in a `ccmp` lookup.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05e7,05bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05e7,05bc

montage hebrew-apf-before.png right-arrow.png hebrew-apf-after.png -geometry +0+0 -background transparent hebrew-apf.png


## 4.1 `liga`

hb-view --font-size=110 --margin=2,16,2,24 --output-file=hebrew-liga-before.png --features=-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=fb4f,05b1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-liga-after.png --features=+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=fb4f,05b1

montage hebrew-liga-before.png right-arrow.png hebrew-liga-after.png -geometry +0+0 -background transparent hebrew-liga.png


## 4.2 `dlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-before.png --features=-dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05d0,05dc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-after.png --features=+dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05d0,05dc

montage hebrew-dlig-before.png right-arrow.png hebrew-dlig-after.png -geometry +0+0 -background transparent hebrew-dlig.png


## 5.1 `kern`

> Note: Noto Sans Hebrew has `kern` lookups, but so far I have not
> been able to identify an easily visible example pair.


## 5.2 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-before.png --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05e7,059a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-after.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf --unicodes=05e7,059a

montage hebrew-mark-before.png right-arrow.png hebrew-mark-after.png -geometry +0+0 -background transparent hebrew-mark.png









































