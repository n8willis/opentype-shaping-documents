# Commands used to generate the images in [opentype-shaping-tamil.md](../../opentype-shaping-tamil.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192



## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-decompose-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bcc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-decompose-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bc6,25cc,0bd7

montage tamil-matra-decompose-before.png right-arrow.png tamil-matra-decompose-after.png -geometry +0+0 -background transparent tamil-matra-decompose.png


## 3.2 `nukt`

> None found.


## 3.3 `akhn`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-akhn-kssa-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0b95,0bcd,0bb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-akhn-kssa-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0b95,0bcd,0bb7

montage tamil-akhn-kssa-before.png right-arrow.png tamil-akhn-kssa-after.png -geometry +0+0 -background transparent tamil-akhn-kssa.png


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-half-before.png --features=-half,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b99,25cc,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-half-after.png --features=+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b99,0bcd

montage tamil-half-before.png right-arrow.png tamil-half-after.png -geometry +0+0 -background transparent tamil-half.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-position-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bc6,0bb0,0bcd,0b9a,0bcd,0b9c,0bbe

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-position-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb0,0bcd,0b9a,0bcd,0b9c,0bca

montage tamil-matra-position-before.png right-arrow.png tamil-matra-position-after.png -geometry +0+0 -background transparent tamil-matra-position.png


## 5 `pres`

> Note: Noto Serif Tamil implements this as an `akhn` feature for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-pres-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb6,0bcd,0bb0,0bc0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-pres-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb6,0bcd,0bb0,0bc0

montage tamil-pres-before.png right-arrow.png tamil-pres-after.png -geometry +0+0 -background transparent tamil-pres.png


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvs-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0baf,0bc0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvs-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0baf,0bc0

montage tamil-abvs-before.png right-arrow.png tamil-abvs-after.png -geometry +0+0 -background transparent tamil-abvs.png


## 5 `blws`

> None found.


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-psts-before.png --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb4,0bc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-psts-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb4,0bc2

montage tamil-psts-before.png right-arrow.png tamil-psts-after.png -geometry +0+0 -background transparent tamil-psts.png


## `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-haln-before.png --features=-haln,-half,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b9e,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-haln-after.png --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b9e,0bcd

montage tamil-haln-before.png right-arrow.png tamil-haln-after.png -geometry +0+0 -background transparent tamil-haln.png


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvm-before.png --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb9,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvm-after.png --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb9,0bcd

montage tamil-abvm-before.png right-arrow.png tamil-abvm-after.png -geometry +0+0 -background transparent tamil-abvm.png


## 6 `blwm`

> None found.


















































































