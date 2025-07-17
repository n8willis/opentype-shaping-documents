# Commands used to generate the images in [opentype-shaping-gurmukhi.md](../../opentype-shaping-gurmukhi.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.

> Note: There is, at present, no Noto Serif for Gurmukhi; therefore
> (unlike the other Indic scripts) these examples use Noto Sans. Serif
> would be preferrable if it appears in the future, though, due to the
> increased stroke contrast.

## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-pstf-before.svg --features=-init,-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-pstf-after.svg --features=-init,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a2f

svg_stack.py --direction=h gurmukhi-pstf-before.svg right-arrow.svg gurmukhi-pstf-after.svg > gurmukhi-pstf.svg

#### Duplicates for other subsections

cp gurmukhi-pstf.svg gurmukhi-pstf-1.svg

cluster_styles = [


## 3.2 `nukt`

> Noto Serif replaces "Dda,Nukta" with "Rra". That sequence is chosen
> because it means the change in glyphs is easily seen, but perhaps it
> would be better to use an example that has an "-after" form that is
> more clearly nukta-bearing?

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-nukt-before.svg --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a21,25cc,0a3c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-nukt-after.svg --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a21,0a3c

svg_stack.py --direction=h gurmukhi-nukt-before.svg right-arrow.svg gurmukhi-nukt-after.svg > gurmukhi-nukt.svg


## 3.3 `akhn`

> Note: Noto Sans/Serif Gurmukhi have no `akhn` feature implemented.


## 3.4 `rphf`

> Note: Noto Sans/Serif Gurmukhi have no `rphf` feature implemented.


## 3.7 `blwf`

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ra-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ra-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a30

svg_stack.py --direction=h gurmukhi-blwf-ra-before.svg right-arrow.svg gurmukhi-blwf-ra-after.svg > gurmukhi-blwf-ra.svg

### Va

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-va-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-va-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a35

svg_stack.py --direction=h gurmukhi-blwf-va-before.svg right-arrow.svg gurmukhi-blwf-va-after.svg > gurmukhi-blwf-va.svg

### Ha

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ha-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a39

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwf-ha-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=25cc,0a4d,0a39

svg_stack.py --direction=h gurmukhi-blwf-ha-before.svg right-arrow.svg gurmukhi-blwf-ha-after.svg > gurmukhi-blwf-ha.svg


## 3.9 `half`

> Note: Gurmukhi fonts seem to stick to explicit halant-forms.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-half-before.svg --features=-init,-half,-mark,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a23,0a4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-half-after.svg --features=-init,+half,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a23,0a4d

svg_stack.py --direction=h gurmukhi-half-before.svg right-arrow.svg gurmukhi-half-after.svg > gurmukhi-half.svg


## 3.10 `pstf`

> Same as 2.7


## 3.11 `vatu`

> Note: Noto Gurmukhi has no `vatu` feature.


## 3.12 `cjct`

> Note: Noto Gurmukhi has no `cjct` feature.


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,24,16 --output-file=gurmukhi-matra-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a25,0a3f,0a4d,0a32,0a4d,0a35,0a4d,0a1a

hb-view --font-size=110 --margin=2,16,24,16 --output-file=gurmukhi-matra-position-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a25,0a4d,0a32,0a4d,0a35,0a4d,0a1a,0a3f

svg_stack.py --direction=h gurmukhi-matra-position-before.svg right-arrow.svg gurmukhi-matra-position-after.svg > gurmukhi-matra-position.svg


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

hb-view --font-size=110 --margin=2,32,2,16 --output-file=gurmukhi-abvs-before.svg --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a13,0a71

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvs-after.svg --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a13,0a71

svg_stack.py --direction=h gurmukhi-abvs-before.svg right-arrow.svg gurmukhi-abvs-after.svg > gurmukhi-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blws-before.svg --features=-init,-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a15,25cc,0a4d,0a30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blws-after.svg --features=-init,+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a15,0a4d,0a30

svg_stack.py --direction=h gurmukhi-blws-before.svg right-arrow.svg gurmukhi-blws-after.svg > gurmukhi-blws.svg


## 5 `psts`

> Note: Noto Sans Gurmukhi has no `psts` feature.


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-haln-before.svg --features=-init,-haln,-half,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a5c,0a4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-haln-after.svg --features=-init,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a5c,0a4d

svg_stack.py --direction=h gurmukhi-haln-before.svg right-arrow.svg gurmukhi-haln-after.svg > gurmukhi-haln.svg


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvm-before.svg --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a20,0a48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-abvm-after.svg --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a20,0a48

svg_stack.py --direction=h gurmukhi-abvm-before.svg right-arrow.svg gurmukhi-abvm-after.svg > gurmukhi-abvm.svg



## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwm-before.svg --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a17,0a51

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gurmukhi-blwm-after.svg --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.otf --unicodes=0a17,0a51

svg_stack.py --direction=h gurmukhi-blwm-before.svg right-arrow.svg gurmukhi-blwm-after.svg > gurmukhi-blwm.svg



















