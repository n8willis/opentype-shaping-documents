# Commands used to generate the images in [opentype-shaping-telugu.md](../../opentype-shaping-telugu.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-matra-decompose-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-matra-decompose-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c46,25cc,0c56

svg_stack --direction=h telugu-matra-decompose-before.svg right-arrow.svg telugu-matra-decompose-after.svg > telugu-matra-decompose.svg


## 3.3 `akhn`

### KSsa

> Note: Noto Serif Telugu implements this as a `pres`+`blwf`
> substitution for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-akhn-kssa-before.svg --features=-blwf,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c15,25cc,0c4d,0c37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-akhn-kssa-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c15,0c4d,0c37

svg_stack --direction=h telugu-akhn-kssa-before.svg right-arrow.svg telugu-akhn-kssa-after.svg > telugu-akhn-kssa.svg

### JNya

> None found. Microsoft docs reference a "SsJa" akhand form, which is
> also not found.


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-rphf-before.svg --features=-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --preserve-default-ignorables --unicodes=0c30,0c4d,200d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-rphf-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c30,0c4d,200d

svg_stack --direction=h telugu-rphf-before.svg right-arrow.svg telugu-rphf-after.svg > telugu-rphf.svg


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwf-before.svg --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c17,25cc,0c4d,0c24

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwf-after.svg --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c17,0c4d,0c24

svg_stack --direction=h telugu-blwf-before.svg right-arrow.svg telugu-blwf-after.svg > telugu-blwf.svg


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-half-before.svg --features=-half,-haln --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c22,25cc,0c4d,200d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-half-after.svg --features=+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c22,0c4d,200d

svg_stack --direction=h telugu-half-before.svg right-arrow.svg telugu-half-after.svg > telugu-half.svg


## 3.10 `pstf`

> None found.


## 3.12 `cjct`

> None found.


## 4.2 Pre-base matras

> Not applicable.


## 4.3 Reph position

> No examples found; existing fonts seem not to incorporate Reph for
> Telugu....


## 5 `pres`

> Note: Example from Noto Serif Telugu, but it looks like it should be
> a `abvs` substitution instead....

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-pres-before.svg --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c39,0c4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-pres-after.svg --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c39,0c4c

svg_stack --direction=h telugu-pres-before.svg right-arrow.svg telugu-pres-after.svg > telugu-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-abvs-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c40

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-abvs-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c40

svg_stack --direction=h telugu-abvs-before.svg right-arrow.svg telugu-abvs-after.svg > telugu-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blws-before.svg --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c46,0c56

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blws-after.svg --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c46,0c56

svg_stack --direction=h telugu-blws-before.svg right-arrow.svg telugu-blws-after.svg > telugu-blws.svg


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-psts-before.svg --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c2b,0c42

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-psts-after.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c2b,0c42

svg_stack --direction=h telugu-psts-before.svg right-arrow.svg telugu-psts-after.svg > telugu-psts.svg


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-haln-before.svg --features=-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c2f,0c4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-haln-after.svg --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c2f,0c4d

svg_stack --direction=h telugu-haln-before.svg right-arrow.svg telugu-haln-after.svg > telugu-haln.svg


## `abvm`

> None found.


## `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwm-before.svg --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c1d,0c4d,0c26

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwm-after.svg --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c1d,0c4d,0c26

svg_stack --direction=h telugu-blwm-before.svg right-arrow.svg telugu-blwm-after.svg > telugu-blwm.svg




















