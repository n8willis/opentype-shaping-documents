# Commands used to generate the images in [opentype-shaping-mongolian.md](../../opentype-shaping-mongolian.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

> Add examples of FVS and MVS here


## 4.2 `isol`

### `isol` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-before.png --features=-isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-after.png --features=+isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826

montage mongolian-isol-before.png right-arrow.png mongolian-isol-after.png -geometry +0+0 -background transparent mongolian-isol.png


### `isol` FVS

> Note: uses larger right margin

hb-view --font-size=110 --margin=2,112,2,16 --output-file=mongolian-isol-fvs1-before.png --features=-isol --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826,180b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-fvs1-after.png --features=+isol --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826,180b

montage mongolian-isol-fvs1-before.png right-arrow.png mongolian-isol-fvs1-after.png -geometry +0+0 -background transparent mongolian-isol-fvs1.png 


## 4.3 `fina`

### `fina` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-before.png --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830

montage mongolian-fina-before.png right-arrow.png mongolian-fina-after.png -geometry +0+0 -background transparent mongolian-fina.png


### `fina` FVS

> Note: uses larger right margin

hb-view --font-size=110 --margin=2,112,2,16 --output-file=mongolian-fina-fvs2-before.png --features=-fina --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830,180c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-fvs2-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830,180c

montage mongolian-fina-fvs2-before.png right-arrow.png mongolian-fina-fvs2-after.png -geometry +0+0 -background transparent mongolian-fina-fvs2.png
















