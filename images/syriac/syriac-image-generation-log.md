# Commands used to generate the images in [opentype-shaping-syriac.md](../../opentype-shaping-syriac.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Dalath Rish group ##


## 4.1 `locl`

> Note: None found in Noto fonts.


## 4.2 `isol`

> Note: none found in Noto fonts.


## 4.3 `fina`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-before.png --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722


## 4.4 `fin2`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-before.png --features=-fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-after.png --features=+fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

montage syriac-fin2-before.png right-arrow.png syriac-fin2-after.png -geometry +0+0 -background transparent syriac-fin2.png


## 4.5 `fin3`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-before.png --features=-fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-after.png --features=+fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

montage syriac-fin3-before.png right-arrow.png syriac-fin3-after.png -geometry +0+0 -background transparent syriac-fin3.png


## 4.6 `medi`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

montage syriac-medi-before.png right-arrow.png syriac-medi-after.png -geometry +0+0 -background transparent syriac-medi.png


## 4.7 `med2`




































