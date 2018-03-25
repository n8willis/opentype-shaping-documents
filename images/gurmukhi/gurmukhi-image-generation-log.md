# Commands used to generate the images in [opentype-shaping-gurmukhi.md](../../opentype-shaping-gurmukhi.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.

> Note: There is, at present, no Noto Serif for Gurmukhi; therefore
> (unlike the other Indic scripts) these examples use Noto Sans. Serif
> would be preferrable if it appears in the future, though, due to the
> increased stroke contrast.

## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-pstf-before.png --features=-init,-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-pstf-after.png --features=-init,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a2f

montage gurmukhi-pstf-before.png right-arrow.png gurmukhi-pstf-after.png -geometry +0+0 -background transparent gurmukhi-pstf.png


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-nukt-before.png --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a21,25cc,0a3c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-nukt-after.png --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a21,0a3c

montage gurmukhi-nukt-before.png right-arrow.png gurmukhi-nukt-after.png -geometry +0+0 -background transparent gurmukhi-nukt.png


## 3.3 `akhn`

> Note: Noto Sans Gurmukhi has no `akhn` feature implemented.


## 3.4 `rphf`

> Note: Noto Sans Gurmukhi has no `rphf` feature implemented.


## 3.7 `blwf`

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ra-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ra-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a30

montage gurmukhi-blwf-ra-before.png right-arrow.png gurmukhi-blwf-ra-after.png -geometry +0+0 -background transparent gurmukhi-blwf-ra.png

### Va

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-va-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-va-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a35

montage gurmukhi-blwf-va-before.png right-arrow.png gurmukhi-blwf-va-after.png -geometry +0+0 -background transparent gurmukhi-blwf-va.png

### Ha

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ha-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a39

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ha-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=25cc,0a4d,0a39

montage gurmukhi-blwf-ha-before.png right-arrow.png gurmukhi-blwf-ha-after.png -geometry +0+0 -background transparent gurmukhi-blwf-ha.png


## 3.9 `half`

> Note: Gurmukhi fonts seem to stick to explicit halant-forms.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-half-before.png --features=-init,-half,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a2d,0a4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-half-after.png --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a2d,0a4d

montage gurmukhi-half-before.png right-arrow.png gurmukhi-half-after.png -geometry +0+0 -background transparent gurmukhi-half.png


## 3.10 `pstf`

> Same as 2.7


## 3.11 `vatu`

> Note: Noto Gurmukhi has no `vatu` feature.


## 3.12 `cjct`

> Note: Noto Gurmukhi has no `cjct` feature.


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-matra-position-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a25,0a3f,0a4d,0a32,0a4d,0a35,0a4d,0a1a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-matra-position-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a25,0a4d,0a32,0a4d,0a35,0a4d,0a1a,0a3f

montage gurmukhi-matra-position-before.png right-arrow.png gurmukhi-matra-position-after.png -geometry +0+0 -background transparent gurmukhi-matra-position.png


## 4.3 Reph position

> Note: Noto Gurmukhi has no `rphf` feature and no Reph
> glyph. Therefore no illustration of Reph positioning is possible.


## 5 `init`

> Note: Noto Gurmukhi has no `init` feature, and it is unclear from
> the Microsoft specification whether `init` is defined for Gurmukhi.


## 5 `pres`

> Note: Noto Gurmukhi has no `pres` feature, even though it would be
> possible to implement one for the i-matra (`U+0A3F`).


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvs-before.png --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a13,0a71

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvs-after.png --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a13,0a71

montage gurmukhi-abvs-before.png right-arrow.png gurmukhi-abvs-after.png -geometry +0+0 -background transparent gurmukhi-abvs.png


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blws-before.png --features=-init,-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf --unicodes=0a15,25cc,0a4d,0a30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blws-after.png --features=-init,+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf --unicodes=0a15,0a4d,0a30

montage gurmukhi-blws-before.png right-arrow.png gurmukhi-blws-after.png -geometry +0+0 -background transparent gurmukhi-blws.png


## 5 `psts`

> Note: Noto Sans Gurmukhi has no `psts` feature.


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-haln-before.png --features=-init,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a32,0a3c,0a4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-haln-after.png --features=-init,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a32,0a3c,0a4d

montage gurmukhi-haln-before.png right-arrow.png gurmukhi-haln-after.png -geometry +0+0 -background transparent gurmukhi-haln.png


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvm-before.png --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a20,0a48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvm-after.png --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a20,0a48

montage gurmukhi-abvm-before.png right-arrow.png gurmukhi-abvm-after.png -geometry +0+0 -background transparent gurmukhi-abvm.png



## 6 `blwm`

 hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwm-before.png --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a06,0a42

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwm-after.png --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf --unicodes=0a06,0a42

montage gurmukhi-blwm-before.png right-arrow.png gurmukhi-blwm-after.png -geometry +0+0 -background transparent gurmukhi-blwm.png



















