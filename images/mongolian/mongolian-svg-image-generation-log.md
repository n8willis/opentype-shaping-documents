# Commands used to generate the images in [opentype-shaping-mongolian.md](../../opentype-shaping-mongolian.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### FVS

#### No FVS

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-none-before.svg --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-none-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180a,25cc

ontage mongolian-fvs-none-before.svg right-arrow.svg mongolian-fvs-none-after.svg > mongolian-fvs-none.svg


#### FVS1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs1-before.svg --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs1-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180b,180a,25cc

svg_stack --direction=h mongolian-fvs-fvs1-before.svg right-arrow.svg mongolian-fvs-fvs1-after.svg > mongolian-fvs-fvs1.svg


#### FVS2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs2-before.svg --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180c,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs2-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180c,180a,25cc

svg_stack --direction=h mongolian-fvs-fvs2-before.svg right-arrow.svg mongolian-fvs-fvs2-after.svg > mongolian-fvs-fvs2.svg


#### FVS3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs3-before.svg --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fvs-fvs3-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1873,180d,180a,25cc

svg_stack --direction=h mongolian-fvs-fvs3-before.svg right-arrow.svg mongolian-fvs-fvs3-after.svg > mongolian-fvs-fvs3.svg



## 4.2 `isol`

### `isol` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-before.svg --features=-isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-after.svg --features=+isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826

svg_stack --direction=h mongolian-isol-before.svg right-arrow.svg mongolian-isol-after.svg > mongolian-isol.svg


### `isol` FVS

> Note: uses larger right margin

hb-view --font-size=110 --margin=2,112,2,16 --output-file=mongolian-isol-fvs1-before.svg --features=-isol --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826,180b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-isol-fvs1-after.svg --features=+isol --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1826,180b

svg_stack --direction=h mongolian-isol-fvs1-before.svg right-arrow.svg mongolian-isol-fvs1-after.svg > mongolian-isol-fvs1.svg 


## 4.3 `fina`

### `fina` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-before.svg --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-after.svg --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830

svg_stack --direction=h mongolian-fina-before.svg right-arrow.svg mongolian-fina-after.svg > mongolian-fina.svg


### `fina` FVS

> Note: uses larger right margin

hb-view --font-size=110 --margin=2,112,2,16 --output-file=mongolian-fina-fvs2-before.svg --features=-fina --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830,180c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-fina-fvs2-after.svg --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,1830,180c

svg_stack --direction=h mongolian-fina-fvs2-before.svg right-arrow.svg mongolian-fina-fvs2-after.svg > mongolian-fina-fvs2.svg


## 4.6 `medi`

### `medi` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-before.svg --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180a,25cc

svg_stack --direction=h mongolian-medi-before.svg right-arrow.svg mongolian-medi-after.svg > mongolian-medi.svg


### `medi` FVS

> Note: uses ZWNJ and spaces to approximate correct spacing for FVS1
> (which is zero-width)

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-fvs1-before.svg --features=-medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-medi-fvs1-after.svg --features=+medi --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=25cc,180a,186f,180b,180a,25cc

svg_stack --direction=h mongolian-medi-fvs1-before.svg right-arrow.svg mongolian-medi-fvs1-after.svg > mongolian-medi-fvs1.svg


## 4.8 `init`

### `init` general

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-after.svg --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180a,25cc

svg_stack --direction=h mongolian-init-before.svg right-arrow.svg mongolian-init-after.svg > mongolian-init.svg


### `init` FVS

> Note: uses ZWNJ and spaces to approximate correct spacing for FVS1
> (which is zero-width)

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-fvs1-before.svg --features=-init --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180b,200d,0020,0020,0020,202f,180a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-init-fvs1-after.svg --features=+init --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=1821,180b,180a,25cc

svg_stack --direction=h mongolian-init-fvs1-before.svg right-arrow.svg mongolian-init-fvs1-after.svg > mongolian-init-fvs1.svg


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-rlig-before.svg --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=182a,1820

hb-view --font-size=110 --margin=2,16,2,16 --output-file=mongolian-rlig-after.svg --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf --unicodes=182a,1820

svg_stack --direction=h mongolian-rlig-before.svg right-arrow.svg mongolian-rlig-after.svg > mongolian-rlig.svg
















