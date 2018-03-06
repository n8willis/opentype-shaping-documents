# Commands used to generate the images in
[opentype-shaping-kannada.md](../../opentype-shaping-kannada.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-matra-decomposition-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cc8

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-matra-decomposition-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cc6,25cc,0cd6

montage kannada-matra-decomposition-before.png right-arrow.png kannada-matra-decomposition-after.png -geometry +0+0 -background transparent kannada-matra-decomposition.png


## 3.2 `nukt`

> Note: Noto Serif Kannada implements this in `blwm` for unknown
> reasons.

hb-view --font-size=110 --margin=2,32,2,16 --output-file=kannada-nukt-before.png --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,25cc,0cbc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-nukt-after.png  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cbc

montage kannada-nukt-before.png right-arrow.png kannada-nukt-after.png -geometry +0+0 -background transparent kannada-nukt.png


## 3.3 `akhn`

> Note: Noto Serif Kannada implements this in both `akhn` and in
> `blwf` for unknown reasons.

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-kssa-before.png --features=-akhn,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-kssa-after.png --features=+akhn, --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7

montage kannada-akhn-kssa-before.png right-arrow.png kannada-akhn-kssa-after.png -geometry +0+0 -background transparent kannada-akhn-kssa.png


### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-jnya-before.png --features=-akhn,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c9c,0ccd,0c9e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-jnya-after.png --features=+akhn, --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c9c,0ccd,0c9e

montage kannada-akhn-jnya-before.png right-arrow.png kannada-akhn-jnya-after.png -geometry +0+0 -background transparent kannada-akhn-jnya.png


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-rphf-before.png --features=-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-rphf-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc

montage kannada-rphf-before.png right-arrow.png kannada-rphf-after.png -geometry +0+0 -background transparent kannada-rphf.png


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwf-before.png --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ccd,0ca1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwf-after.png --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ccd,0ca1

montage kannada-blwf-before.png right-arrow.png kannada-blwf-after.png -geometry +0+0 -background transparent kannada-blwf.png


## 4.3 Reph positioning

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-reph-position-before.png  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc,0cad,0ccd,0cb3,0cc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-reph-position-after.png  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,0cad,0ccd,0cb3,0cc2

montage kannada-reph-position-before.png right-arrow.png kannada-reph-position-after.png -geometry +0+0 -background transparent kannada-reph-position.png


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-pres-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb5,25cc,0cc1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-pres-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb5,0cc1

montage kannada-pres-before.png right-arrow.png kannada-pres-after.png -geometry +0+0 -background transparent kannada-pres.png


## 5 `abvs`

> Note: Noto Serif Kannada has some abvs-like substituations in `pres`
> lookup 14 (via single-sub lookup 23), but I have not yet figured out
> whether they are,
> linguistically speaking, actually above-base features. Thus, they are
> included here, but might not be used in the shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-abvs-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0ca3,0ccc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-abvs-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0ca3,0ccc

montage kannada-abvs-before.png right-arrow.png kannada-abvs-after.png -geometry +0+0 -background transparent kannada-abvs.png


## 5 `blws`

> Note: Note Serif Kannada has some blws-like substitutions in 
> `pres` lookup 12 (via contextual chaining lookups 7 and 8 (via
> single-sub lookups 19 and 20)), but I have not yet figured out
> whether they are, linguistically speaking, actually above-base
> features. Thus, they are included here, but might not be used in the
> shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blws-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7,0cc1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blws-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7,0cc1

montage kannada-blws-before.png right-arrow.png kannada-blws-after.png -geometry +0+0 -background transparent kannada-blws.png

## 5 `psts`

> Note: Noto Serif Kannada has some psts-like lookups in `pres` lookup 12 (via single-sub lookup 21 and 22 (via contextual chaining lookup
> 9 and 10)), but I have not yet figured out whether they are,
> linguistically speaking, actually post-base features. Thus, they are
> included here, but might not be used in the shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-psts-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0cbe

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-psts-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0cbe

montage kannada-psts-before.png right-arrow.png kannada-psts-after.png -geometry +0+0 -background transparent kannada-psts.png


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-haln-before.png --features=-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c98,0ccd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-haln-after.png --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c98,0ccd

montage kannada-haln-before.png right-arrow.png kannada-haln-after.png -geometry +0+0 -background transparent kannada-haln.png


## 6 `abvm`

> Note: Noto Serif Kannada does not include an `abvm` feature.


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwm-before.png --features=-blwm,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cc1,0cbc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwm-after.png --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cc1,0cbc

montage kannada-blwm-before.png right-arrow.png kannada-blwm-after.png -geometry +0+0 -background transparent kannada-blwm.png
