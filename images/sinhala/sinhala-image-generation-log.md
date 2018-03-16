# Commands used to generate the images in [opentype-shaping-sinhala.md](../../opentype-shaping-sinhala.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-decompose-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dda

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-decompose-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dd9,25cc,0dca

montage sinhala-matra-decompose-before.png right-arrow.png sinhala-matra-decompose-after.png -geometry +0+0 -background transparent sinhala-matra-decompose.png


## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-va-before.png --features=-vatu --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dba

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-va-after.png --features=+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dba

montage sinhala-vatu-before.png right-arrow.png sinhala-vatu-after.png -geometry +0+0 -background transparent sinhala-vatu-va.png


## 3.3 `akhn`

### Ligature

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-ligature-before.png --features=-akhn --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9a,25cc,0dca,200d,0dc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-ligature-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9a,0dca,200d,0dc2

montage sinhala-akhn-ligature-before.png right-arrow.png sinhala-akhn-ligature-after.png -geometry +0+0 -background transparent sinhala-akhn-ligature.png

### Touching

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-touching-before.png --features=-akhn,-pres --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9c,200d,25cc,0dca,0d9d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-akhn-touching-after.png --features=+akhn,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9c,200d,0dca,0d9d

montage sinhala-akhn-touching-before.png right-arrow.png sinhala-akhn-touching-after.png -geometry +0+0 -background transparent sinhala-akhn-touching.png


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-rphf-before.png --features=-rphf --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc

hb-view --font-size=110 --margin=2,16,2,64 --output-file=sinhala-rphf-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc

montage sinhala-rphf-before.png right-arrow.png sinhala-rphf-after.png -geometry +0+0 -background transparent sinhala-rphf.png


## 3.10 `pstf`

> Not needed?

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pstf-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dde

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pstf-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0ddf

montage sinhala-pstf-before.png right-arrow.png sinhala-pstf-after.png -geometry +0+0 -background transparent sinhala-pstf.png


## 3.11 `vatu`

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-ra-before.png --features=-vatu --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dbb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-vatu-ra-after.png --features=+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dca,200d,0dbb

montage sinhala-vatu-ra-before.png right-arrow.png sinhala-vatu-ra-after.png -geometry +0+0 -background transparent sinhala-vatu-ra.png

### Va

> Same as 2.7


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-position-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=25cc,0dd9,0da0,0dca,0db1,0dca,200d,0daf,0dca,200d,0dbb,0dcf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-matra-position-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0da0,0dca,0db1,0dca,200d,0daf,0dca,200d,0dbb,0ddc

montage sinhala-matra-position-before.png right-arrow.png sinhala-matra-position-after.png -geometry +0+0 -background transparent sinhala-matra-position.png


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,64 --output-file=sinhala-reph-position-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,25cc,0dad,0dca,200d,0dae,0dca,200d,0dba,0dd1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-reph-position-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dad,0dca,200d,0dae,0dca,200d,0dba,0dd1

montage sinhala-reph-position-before.png right-arrow.png sinhala-reph-position-after.png -geometry +0+0 -background transparent sinhala-reph-position.png


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pres-before.png --features=-pres --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9b,200d,25cc,0dca,0da2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-pres-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9b,200d,0dca,0da2

montage sinhala-pres-before.png right-arrow.png sinhala-pres-after.png -geometry +0+0 -background transparent sinhala-pres.png


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvs-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0db6,0dd3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvs-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0db6,0dd3

montage sinhala-abvs-before.png right-arrow.png sinhala-abvs-after.png -geometry +0+0 -background transparent sinhala-abvs.png


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blws-before.png --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0db7,0dd6

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blws-after.png --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0db7,0dd6

montage sinhala-blws-before.png right-arrow.png sinhala-blws-after.png -geometry +0+0 -background transparent sinhala-blws.png


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-psts-before.png --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0daf,0dca,200d,0dba,0ddd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-psts-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0daf,0dca,200d,0dba,0ddd

montage sinhala-psts-before.png right-arrow.png sinhala-psts-after.png -geometry +0+0 -background transparent sinhala-psts.png


## 6 `abvm`

> Note: Noto Sans Sinhala implements this as an `abvs` substitution
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvm-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dae

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-abvm-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0dbb,0dca,200d,0dae

montage sinhala-abvm-before.png right-arrow.png sinhala-abvm-after.png -geometry +0+0 -background transparent sinhala-abvm.png


## 6 `blwm`

> Note: Noto Sans Sinhala double-implements this in both `blwm` and
> `abvs`, even though it is clearly not above-base.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blwm-before.png --features=-blwm,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9f,0dca,200d,0dbb

hb-view --font-size=110 --margin=2,16,2,16 --output-file=sinhala-blwm-after.png --features=+blwm,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf --unicodes=0d9f,0dca,200d,0dbb

montage sinhala-blwm-before.png right-arrow.png sinhala-blwm-after.png -geometry +0+0 -background transparent sinhala-blwm.png















































