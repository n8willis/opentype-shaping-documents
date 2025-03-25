# Commands used to generate the images in [opentype-shaping-kannada.md](../../opentype-shaping-kannada.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-matra-decomposition-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cc8

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-matra-decomposition-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cc6,25cc,0cd6

svg_stack --direction=h kannada-matra-decomposition-before.svg right-arrow.svg kannada-matra-decomposition-after.svg > kannada-matra-decomposition.svg


## 3.2 `nukt`

> Note: Noto Serif Kannada implements this in `blwm` for unknown
> reasons.

hb-view --font-size=110 --margin=2,32,2,16 --output-file=kannada-nukt-before.svg --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,25cc,0cbc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-nukt-after.svg  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cbc

svg_stack --direction=h kannada-nukt-before.svg right-arrow.svg kannada-nukt-after.svg > kannada-nukt.svg


## 3.3 `akhn`

> Note: Noto Serif Kannada implements this in both `akhn` and in
> `blwf` for unknown reasons.

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-kssa-before.svg --features=-akhn,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-kssa-after.svg --features=+akhn, --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0cb7

svg_stack --direction=h kannada-akhn-kssa-before.svg right-arrow.svg kannada-akhn-kssa-after.svg > kannada-akhn-kssa.svg


### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-jnya-before.svg --features=-akhn,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c9c,0ccd,0c9e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-akhn-jnya-after.svg --features=+akhn, --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c9c,0ccd,0c9e

svg_stack --direction=h kannada-akhn-jnya-before.svg right-arrow.svg kannada-akhn-jnya-after.svg > kannada-akhn-jnya.svg


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-rphf-before.svg --features=-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-rphf-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc

svg_stack --direction=h kannada-rphf-before.svg right-arrow.svg kannada-rphf-after.svg > kannada-rphf.svg


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwf-before.svg --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ccd,0ca1

hb-view --font-size=110 --margin=2,24,2,16 --output-file=kannada-blwf-after.svg --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ccd,0ca1

svg_stack --direction=h kannada-blwf-before.svg right-arrow.svg kannada-blwf-after.svg > kannada-blwf.svg


## 4.3 Reph positioning

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-reph-position-before.svg  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,25cc,0cad,0ccd,0cb3,0cc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-reph-position-after.svg  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb0,0ccd,0cad,0ccd,0cb3,0cc2

svg_stack --direction=h kannada-reph-position-before.svg right-arrow.svg kannada-reph-position-after.svg > kannada-reph-position.svg


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-pres-before.svg --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb5,25cc,0cc1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-pres-after.svg --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cb5,0cc1

svg_stack --direction=h kannada-pres-before.svg right-arrow.svg kannada-pres-after.svg > kannada-pres.svg


## 5 `abvs`

> Note: Noto Serif Kannada has some abvs-like substituations in `pres`
> lookup 14 (via single-sub lookup 23), but I have not yet figured out
> whether they are,
> linguistically speaking, actually above-base features. Thus, they are
> included here, but might not be used in the shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-abvs-before.svg --features=-pres,-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0ca3,0ccc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-abvs-after.svg --features=+pres,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0ca3,0ccc

svg_stack --direction=h kannada-abvs-before.svg right-arrow.svg kannada-abvs-after.svg > kannada-abvs.svg


## 5 `blws`

> Note: Note Serif Kannada has some blws-like substitutions in 
> `pres` lookup 12 (via contextual chaining lookups 7 and 8 (via
> single-sub lookups 19 and 20)), but I have not yet figured out
> whether they are, linguistically speaking, actually above-base
> features. Thus, they are included here, but might not be used in the
> shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blws-before.svg --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0ca4,0ccd,0caf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blws-after.svg --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c95,0ccd,0ca4,0ccd,0caf

svg_stack --direction=h kannada-blws-before.svg right-arrow.svg kannada-blws-after.svg > kannada-blws.svg

## 5 `psts`

> Note: Noto Serif Kannada has some psts-like lookups in `pres` lookup 12 (via single-sub lookup 21 and 22 (via contextual chaining lookup
> 9 and 10)), but I have not yet figured out whether they are,
> linguistically speaking, actually post-base features. Thus, they are
> included here, but might not be used in the shaping document.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-psts-before.svg --features=-pres,-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ca4,0cbf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-psts-after.svg --features=+pres,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=25cc,0ca4,0cbf

svg_stack --direction=h kannada-psts-before.svg right-arrow.svg kannada-psts-after.svg > kannada-psts.svg


## 5 `haln`

> Note: Noto Serif Kannada does not include a `haln` feature. Similar
> behavior is found in `psts`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-haln-before.svg --features=-haln,-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c98,0ccd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-haln-after.svg --features=+haln,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0c98,0ccd

svg_stack --direction=h kannada-haln-before.svg right-arrow.svg kannada-haln-after.svg > kannada-haln.svg


## 6 `abvm`

> Note: Noto Serif Kannada does not include an `abvm` feature.


## 6 `blwm`

hb-view --font-size=110 --margin=2,32,2,16 --output-file=kannada-blwm-before.svg --features=-blwm,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cc1,0cbc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=kannada-blwm-after.svg --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf --unicodes=0cab,0cc1,0cbc

svg_stack --direction=h kannada-blwm-before.svg right-arrow.svg kannada-blwm-after.svg > kannada-blwm.svg
