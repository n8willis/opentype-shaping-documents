# Commands used to generate the images in [opentype-shaping-oriya.md](/[opentype-shaping-oriya.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192




## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-decompose-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-decompose-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b47,25cc,0b56

montage oriya-matra-decompose-before.png right-arrow.png oriya-matra-decompose-after.png -geometry +0+0 -background transparent oriya-matra-decompose.png


## 2.7 Post-base consonants

### Ya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-ya-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-ya-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b2f

montage oriya-pstf-ya-before.png right-arrow.png oriya-pstf-ya-after.png -geometry +0+0 -background transparent oriya-pstf-ya.png

### Yya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-yya-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b5f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-yya-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b5f

montage oriya-pstf-yya-before.png right-arrow.png oriya-pstf-yya-after.png -geometry +0+0 -background transparent oriya-pstf-yya.png


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-nukt-before.png --features=-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b16,25cc,0b3c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-nukt-after.png --features=+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b16,0b3c

montage oriya-nukt-before.png right-arrow.png oriya-nukt-after.png -geometry +0+0 -background transparent oriya-nukt.png


## 3.3 `akhn`

### KSsa

> Note: Noto Sans Oriya implements this in a `pres`+`blwf` combination
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-kssa-before.png --features=-pres,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b15,0b4d,0b37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-kssa-after.png --features=+pres,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b15,0b4d,0b37

montage oriya-akhn-kssa-before.png right-arrow.png oriya-akhn-kssa-after.png -geometry +0+0 -background transparent oriya-akhn-kssa.png

### JNya

> Note: Noto Sans Oriya implements this in a `blwf`+`cjct` combination
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-jnya-before.png --features=-pres,-cjct,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b1c,0b4d,0b1e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-jnya-after.png --features=+pres,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b1c,0b4d,0b1e

montage oriya-akhn-jnya-before.png right-arrow.png oriya-akhn-jnya-after.png -geometry +0+0 -background transparent oriya-akhn-jnya.png


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-rphf-before.png --features=-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b30,0b4d,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-rphf-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b30,0b4d,25cc

montage oriya-rphf-before.png right-arrow.png oriya-rphf-after.png -geometry +0+0 -background transparent oriya-rphf.png


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-before.png --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b25

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-after.png --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=25cc,0b4d,0b25

montage oriya-blwf-before.png right-arrow.png oriya-blwf-after.png -geometry +0+0 -background transparent oriya-blwf.png


## 3.9 `half`

> No examples found.

## 3.10 `pstf`

> Same as 2.7

## 3.12 `cjct`

> Not a perfect example....

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-cjct-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b38,0b4d,25cc,0b4d,0b2a,0b4d,0b5d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-cjct-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b38,0b4d,0b2a,0b4d,0b5d

montage oriya-cjct-before.png right-arrow.png oriya-cjct-after.png -geometry +0+0 -background transparent oriya-cjct.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-position-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b47,0b28,0b4d,200d,0b2d,0b4d,0b27,0b57

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-position-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b28,0b4d,200d,0b2d,0b4d,0b27,0b4c

montage oriya-matra-position-before.png right-arrow.png oriya-matra-position-after.png -geometry +0+0 -background transparent oriya-matra-position.png


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-reph-position-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b30,0b4d,25cc,0b2a,0b4d,0b2a,0b4d,0b26,0b4d,0b2f,0b3e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-reph-position-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b30,0b4d,0b2a,0b4d,0b2a,0b4d,0b26,0b4d,0b2f,0b3e

montage oriya-reph-position-before.png right-arrow.png oriya-reph-position-after.png -geometry +0+0 -background transparent oriya-reph-position.png


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pres-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pres-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2d

montage oriya-pres-before.png right-arrow.png oriya-pres-after.png -geometry +0+0 -background transparent oriya-pres.png


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvs-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b13,200d,0b01

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvs-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b13,200d,0b01

montage oriya-abvs-before.png right-arrow.png oriya-abvs-after.png -geometry +0+0 -background transparent oriya-abvs.png


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blws-before.png --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b28,0b4d,0b24,0b42

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blws-after.png --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b28,0b4d,0b24,0b42

montage oriya-blws-before.png right-arrow.png oriya-blws-after.png -geometry +0+0 -background transparent oriya-blws.png


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-psts-before.png --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b23,0b4c,0b01

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-psts-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b23,0b4c,0b01

montage oriya-psts-before.png right-arrow.png oriya-psts-after.png -geometry +0+0 -background transparent oriya-psts.png


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-haln-before.png --features=-haln,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b1d,0b4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-haln-after.png --features=+haln,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b1d,0b4d

montage oriya-haln-before.png right-arrow.png oriya-haln-after.png -geometry +0+0 -background transparent oriya-haln.png


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvm-before.png --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b19,0b4d,0b18,0b48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvm-after.png --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b19,0b4d,0b18,0b48

montage oriya-abvm-before.png right-arrow.png oriya-abvm-after.png -geometry +0+0 -background transparent oriya-abvm.png


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwm-before.png --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2b,0b44

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwm-after.png --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2b,0b44

montage oriya-blwm-before.png right-arrow.png oriya-blwm-after.png -geometry +0+0 -background transparent oriya-blwm.png









