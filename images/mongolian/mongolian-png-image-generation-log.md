# Commands used to generate the images in [opentype-shaping-mongolian.md](../../opentype-shaping-mongolian.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### FVS

#### No FVS

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-none-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-none-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180a,25cc

ontage mongolian-fvs-none-before.png right-arrow.png mongolian-fvs-none-after.png -geometry +0+0 -background transparent mongolian-fvs-none.png


#### FVS1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs1-before.png --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs1-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180b,180a,25cc

montage mongolian-fvs-fvs1-before.png right-arrow.png mongolian-fvs-fvs1-after.png -geometry +0+0 -background transparent mongolian-fvs-fvs1.png


#### FVS2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs2-before.png --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180c,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs2-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180c,180a,25cc

montage mongolian-fvs-fvs2-before.png right-arrow.png mongolian-fvs-fvs2-after.png -geometry +0+0 -background transparent mongolian-fvs-fvs2.png


#### FVS3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs3-before.png --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs3-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,180a,25cc

montage mongolian-fvs-fvs3-before.png right-arrow.png mongolian-fvs-fvs3-after.png -geometry +0+0 -background transparent mongolian-fvs-fvs3.png



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


## 4.6 `medi`

### `medi` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180a,25cc

montage mongolian-medi-before.png right-arrow.png mongolian-medi-after.png -geometry +0+0 -background transparent mongolian-medi.png


### `medi` FVS

> Note: uses ZWNJ and spaces to approximate correct spacing for FVS1
> (which is zero-width)

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-fvs1-before.png --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-fvs1-after.png --features=+medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180b,180a,25cc

montage mongolian-medi-fvs1-before.png right-arrow.png mongolian-medi-fvs1-after.png -geometry +0+0 -background transparent mongolian-medi-fvs1.png


## 4.8 `init`

### `init` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-after.png --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180a,25cc

montage mongolian-init-before.png right-arrow.png mongolian-init-after.png -geometry +0+0 -background transparent mongolian-init.png


### `init` FVS

> Note: uses ZWNJ and spaces to approximate correct spacing for FVS1
> (which is zero-width)

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-fvs1-before.png --features=-init --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-fvs1-after.png --features=+init --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180b,180a,25cc

montage mongolian-init-fvs1-before.png right-arrow.png mongolian-init-fvs1-after.png -geometry +0+0 -background transparent mongolian-init-fvs1.png


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-rlig-before.png --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=182a,1820

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-rlig-after.png --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=182a,1820

montage mongolian-rlig-before.png right-arrow.png mongolian-rlig-after.png -geometry +0+0 -background transparent mongolian-rlig.png
















