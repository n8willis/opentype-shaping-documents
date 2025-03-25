# Commands used to generate the images in [opentype-shaping-gujarati.md](../../opentype-shaping-gujarati.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-decompose-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ac9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-decompose-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ac5,25cc,0abe

svg_stack --direction=h gujarati-matra-decompose-before.svg right-arrow.svg gujarati-matra-decompose-after.svg > gujarati-matra-decompose.svg


## 2.7 Post-base consonants

> None


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-nukt-before.svg --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a97,25cc,0abc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-nukt-after.svg --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a97,0abc

svg_stack --direction=h gujarati-nukt-before.svg right-arrow.svg gujarati-nukt-after.svg > gujarati-nukt.svg

## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-kssa-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a95,25cc,0acd,0ab7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-kssa-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a95,0acd,0ab7

svg_stack --direction=h gujarati-akhn-kssa-before.svg right-arrow.svg gujarati-akhn-kssa-after.svg > gujarati-akhn-kssa.svg

### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-jnya-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,25cc,0acd,0a9e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-jnya-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,0acd,0a9e

svg_stack --direction=h gujarati-akhn-jnya-before.svg right-arrow.svg gujarati-akhn-jnya-after.svg > gujarati-akhn-jnya.svg


## 3.4 `rphf`


hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rphf-before.svg --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,25cc,0acd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rphf-after.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,25cc

svg_stack --direction=h gujarati-rphf-before.svg right-arrow.svg gujarati-rphf-after.svg > gujarati-rphf.svg


## 3.5 `rkrf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rkrf-before.svg --features=-init,-rkrf,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rkrf-after.svg --features=-init,+rkrf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,0acd,0ab0

svg_stack --direction=h gujarati-rkrf-before.svg right-arrow.svg gujarati-rkrf-after.svg > gujarati-rkrf.svg


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwf-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwf-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=25cc,0acd,0ab0

svg_stack --direction=h gujarati-blwf-before.svg right-arrow.svg gujarati-blwf-after.svg > gujarati-blwf.svg


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-half-before.svg --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aad,0acd,0ab0,25cc,0acd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-half-after.svg --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aad,0acd,0ab0,0acd,25cc

svg_stack --direction=h gujarati-half-before.svg right-arrow.svg gujarati-half-after.svg > gujarati-half.svg


## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-vatu-before.svg --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa4,25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-vatu-after.svg --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa4,0acd,0ab0

svg_stack --direction=h gujarati-vatu-before.svg right-arrow.svg gujarati-vatu-after.svg > gujarati-vatu.svg


## 3.12 `cjct`

> Note that Noto Serif Gujarati implements this in `pres` for unknown
> reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-cjct-before.svg --features=-init,-pres,-cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,25cc,0acd,0aae

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-cjct-after.svg --features=-init,+cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,0acd,0aae

svg_stack --direction=h gujarati-cjct-before.svg right-arrow.svg gujarati-cjct-after.svg > gujarati-cjct.svg


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0abf,0a9f,0acd,0a9d,0acd,0ab9,0acd,0aa4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-position-after.svg --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9f,0acd,0a9d,0acd,0ab9,0acd,0aa4,0abf

svg_stack --direction=h gujarati-matra-position-before.svg right-arrow.svg gujarati-matra-position-after.svg > gujarati-matra-position.svg


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-reph-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,25cc,0aab,0acd,0aa8,0acd,0a9a,0ac2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-reph-position-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aab,0acd,0aa8,0acd,0a9a,0ac2

svg_stack --direction=h gujarati-reph-position-before.svg right-arrow.svg gujarati-reph-position-after.svg > gujarati-reph-position.svg


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-pres-before.svg --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9e,0acd,0a9a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-pres-after.svg --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9e,0acd,0a9a,25cc

svg_stack --direction=h gujarati-pres-before.svg right-arrow.svg gujarati-pres-after.svg > gujarati-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvs-before.svg --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aa3,0abf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvs-after.svg --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aa3,0abf

svg_stack --direction=h gujarati-abvs-before.svg right-arrow.svg gujarati-abvs-after.svg > gujarati-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blws-before.svg --features=-init,-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa3,0ac1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blws-after.svg --features=-init,+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa3,0ac1

svg_stack --direction=h gujarati-blws-before.svg right-arrow.svg gujarati-blws-after.svg > gujarati-blws.svg


## 5 `psts`

> Note: Noto Serif Gujarati implements this as an `abvs` lookup for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-psts-before.svg --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,0acd,0ab0,0abe

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-psts-after.svg --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,0acd,0ab0,0abe

svg_stack --direction=h gujarati-psts-before.svg right-arrow.svg gujarati-psts-after.svg > gujarati-psts.svg


## 5 `haln`

> Note: Noto Serif Gujarati implements this as a `blwm` lookup in
> addition to `haln`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-haln-after.svg --features=-init,+haln,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa0,0acd

hb-view --font-size=110 --margin=2,24,2,16 --output-file=gujarati-haln-before.svg --features=-init,-haln,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa0,0acd

svg_stack --direction=h gujarati-haln-before.svg right-arrow.svg gujarati-haln-after.svg > gujarati-haln.svg


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvm-before.svg --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0ab9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvm-after.svg --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0ab9

svg_stack --direction=h gujarati-abvm-before.svg right-arrow.svg gujarati-abvm-after.svg > gujarati-abvm.svg


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwm-before.svg --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9f,0acd,0aa0,0ac4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwm-after.svg --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9f,0acd,0aa0,0ac4

svg_stack --direction=h gujarati-blwm-before.svg right-arrow.svg gujarati-blwm-after.svg > gujarati-blwm.svg



