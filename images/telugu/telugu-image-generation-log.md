# Commands used to generate the images in [opentype-shaping-telugu.md](/[opentype-shaping-telugu.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-matra-decompose-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-matra-decompose-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c46,25cc,0c56

montage telugu-matra-decompose-before.png right-arrow.png telugu-matra-decompose-after.png -geometry +0+0 -background transparent telugu-matra-decompose.png


## 3.3 `akhn`

### KSsa

> Note: Noto Serif Telugu implements this as a `pres`+`blwf`
> substitution for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-akhn-kssa-before.png --features=-blwf,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c15,25cc,0c4d,0c37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-akhn-kssa-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c15,0c4d,0c37

montage telugu-akhn-kssa-before.png right-arrow.png telugu-akhn-kssa-after.png -geometry +0+0 -background transparent telugu-akhn-kssa.png

### JNya

> None found. Microsoft docs reference a "SsJa" akhand form, which is
> also not found.


## 3.4 `rphf`

> None found. 


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwf-before.png --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c17,25cc,0c4d,0c24

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwf-after.png --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c17,0c4d,0c24

montage telugu-blwf-before.png right-arrow.png telugu-blwf-after.png -geometry +0+0 -background transparent telugu-blwf.png


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-half-before.png --features=-half,-haln --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c22,25cc,0c4d,200d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-half-after.png --features=+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c22,0c4d,200d

montage telugu-half-before.png right-arrow.png telugu-half-after.png -geometry +0+0 -background transparent telugu-half.png


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

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-pres-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c39,0c4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-pres-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c39,0c4c

montage telugu-pres-before.png right-arrow.png telugu-pres-after.png -geometry +0+0 -background transparent telugu-pres.png


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-abvs-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c40

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-abvs-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c40

montage telugu-abvs-before.png right-arrow.png telugu-abvs-after.png -geometry +0+0 -background transparent telugu-abvs.png


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blws-before.png --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c46,0c56

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blws-after.png --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c16,0c46,0c56

montage telugu-blws-before.png right-arrow.png telugu-blws-after.png -geometry +0+0 -background transparent telugu-blws.png


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-psts-before.png --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c2b,0c42

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-psts-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf --unicodes=0c2b,0c42

montage telugu-psts-before.png right-arrow.png telugu-psts-after.png -geometry +0+0 -background transparent telugu-psts.png


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-haln-before.png --features=-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c2f,0c4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-haln-after.png --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c2f,0c4d

montage telugu-haln-before.png right-arrow.png telugu-haln-after.png -geometry +0+0 -background transparent telugu-haln.png


## `abvm`

> None found.


## `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwm-before.png --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c1d,0c62

hb-view --font-size=110 --margin=2,16,2,16 --output-file=telugu-blwm-after.png --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf --unicodes=0c1d,0c62

montage telugu-blwm-before.png right-arrow.png telugu-blwm-after.png -geometry +0+0 -background transparent telugu-blwm.png




















