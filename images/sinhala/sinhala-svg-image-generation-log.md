# Commands used to generate the images in [opentype-shaping-sinhala.md](../../opentype-shaping-sinhala.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-decompose-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dda

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-decompose-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dd9,25cc,0dca

svg_stack --direction=h sinhala-matra-decompose-before.svg right-arrow.svg sinhala-matra-decompose-after.svg > sinhala-matra-decompose.svg


## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-va-before.svg --features=-vatu --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dba

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-va-after.svg --features=+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dba

svg_stack --direction=h sinhala-vatu-va-before.svg right-arrow.svg sinhala-vatu-va-after.svg > sinhala-vatu-va.svg


## 3.3 `akhn`

### Ligature

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-ligature-before.svg --features=-akhn --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9a,25cc,0dca,200d,0dc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-ligature-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9a,0dca,200d,0dc2

svg_stack --direction=h sinhala-akhn-ligature-before.svg right-arrow.svg sinhala-akhn-ligature-after.svg > sinhala-akhn-ligature.svg

### Touching

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-touching-before.svg --features=-akhn,-pres --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9c,200d,25cc,0dca,0d9d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-touching-after.svg --features=+akhn,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9c,200d,0dca,0d9d

svg_stack --direction=h sinhala-akhn-touching-before.svg right-arrow.svg sinhala-akhn-touching-after.svg > sinhala-akhn-touching.svg


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-rphf-before.svg --features=-rphf --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc

hb-view --font-size=110 --margin=2,16,2,64 --output-file=sinhala-rphf-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc

svg_stack --direction=h sinhala-rphf-before.svg right-arrow.svg sinhala-rphf-after.svg > sinhala-rphf.svg


## 3.10 `pstf`

> Not needed?

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pstf-before.svg --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dde

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pstf-after.svg --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0ddf

svg_stack --direction=h sinhala-pstf-before.svg right-arrow.svg sinhala-pstf-after.svg > sinhala-pstf.svg


## 3.11 `vatu`

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-ra-before.svg --features=-vatu --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dbb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-ra-after.svg --features=+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dbb

svg_stack --direction=h sinhala-vatu-ra-before.svg right-arrow.svg sinhala-vatu-ra-after.svg > sinhala-vatu-ra.svg

### Va

> Same as 2.7


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-position-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=25cc,0dd9,0da0,0dca,0db1,0dca,200d,0daf,0dca,200d,0dbb,0dcf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-position-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0da0,0dca,0db1,0dca,200d,0daf,0dca,200d,0dbb,0ddc

svg_stack --direction=h sinhala-matra-position-before.svg right-arrow.svg sinhala-matra-position-after.svg > sinhala-matra-position.svg


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,64 --output-file=sinhala-reph-position-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc,0dad,0dca,200d,0dae,0dca,200d,0dba,0dd1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-reph-position-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dad,0dca,200d,0dae,0dca,200d,0dba,0dd1

svg_stack --direction=h sinhala-reph-position-before.svg right-arrow.svg sinhala-reph-position-after.svg > sinhala-reph-position.svg


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pres-before.svg --features=-pres --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9b,200d,25cc,0dca,0da2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pres-after.svg --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9b,200d,0dca,0da2

svg_stack --direction=h sinhala-pres-before.svg right-arrow.svg sinhala-pres-after.svg > sinhala-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvs-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0db6,0dd3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvs-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0db6,0dd3

svg_stack --direction=h sinhala-abvs-before.svg right-arrow.svg sinhala-abvs-after.svg > sinhala-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blws-before.svg --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0db7,0dd6

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blws-after.svg --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0db7,0dd6

svg_stack --direction=h sinhala-blws-before.svg right-arrow.svg sinhala-blws-after.svg > sinhala-blws.svg


## 5 `psts`

> Note: this lookup only works in Noto Sans. Needs more investigation.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-psts-before.svg --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0daf,0dca,200d,0dba,0ddd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-psts-after.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0daf,0dca,200d,0dba,0ddd

svg_stack --direction=h sinhala-psts-before.svg right-arrow.svg sinhala-psts-after.svg > sinhala-psts.svg


## 6 `abvm`

> Note: Noto Sans Sinhala implements this as an `abvs` substitution
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvm-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dae

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvm-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dae

svg_stack --direction=h sinhala-abvm-before.svg right-arrow.svg sinhala-abvm-after.svg > sinhala-abvm.svg


## 6 `blwm`

> Note: Noto Sans Sinhala double-implements this in both `blwm` and
> `abvs`, even though it is clearly not above-base.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blwm-before.svg --features=-blwm,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9f,0dca,200d,0dbb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blwm-after.svg --features=+blwm,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf --unicodes=0d9f,0dca,200d,0dbb

svg_stack --direction=h sinhala-blwm-before.svg right-arrow.svg sinhala-blwm-after.svg > sinhala-blwm.svg















































