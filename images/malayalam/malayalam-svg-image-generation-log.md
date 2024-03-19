# Commands used to generate the images in [opentype-shaping-malayalam.md](../../opentype-shaping-malayalam.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-decompose-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-decompose-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d46,25cc,0d57

svg_stack --direction=h malayalam-matra-decompose-before.svg right-arrow.svg malayalam-matra-decompose-after.svg > malayalam-matra-decompose.svg


## 2.7 post-base consonants

### Ya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ya-before.svg --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ya-after.svg --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d2f

svg_stack --direction=h malayalam-pstf-ya-before.svg right-arrow.svg malayalam-pstf-ya-after.svg > malayalam-pstf-ya.svg

### Va

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-va-before.svg --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-va-after.svg --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d35

svg_stack --direction=h malayalam-pstf-va-before.svg right-arrow.svg malayalam-pstf-va-after.svg > malayalam-pstf-va.svg


## 3.2 `nukt`

> Note: Noto Serif Malayalam uses `U+0323` "Combining dot below" in
> its mark-placement lookups, not a Nukta (which does not exist in the
> Malayalam Unicode block).

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-nukt-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d18,25cc,0323

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-nukt-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d18,0323

svg_stack --direction=h malayalam-nukt-before.svg right-arrow.svg malayalam-nukt-after.svg > malayalam-nukt.svg


## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-kssa-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d15,0d4d,0d37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-kssa-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d15,0d4d,0d37

svg_stack --direction=h malayalam-akhn-kssa-before.svg right-arrow.svg malayalam-akhn-kssa-after.svg > malayalam-akhn-kssa.svg

### NnTta

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-nntta-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d23,0d4d,0d1f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-nntta-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d23,0d4d,0d1f

svg_stack --direction=h malayalam-akhn-nntta-before.svg right-arrow.svg malayalam-akhn-nntta-after.svg > malayalam-akhn-nntta.svg

> Note: The "Chillu R" is shown here because it may be implemented as
> an akhand form and that makes Malayalam distinct from several other
> Indic scripts.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-chillu-r-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d30,0d4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-chillu-r-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d7c

svg_stack --direction=h malayalam-akhn-chillu-r-before.svg right-arrow.svg malayalam-akhn-chillu-r-after.svg > malayalam-akhn-chillu-r.svg


## 3.4 `rphf`

> Note: Malayalam modern orthography does not use Reph. The dot-reph
> substitution here is shown with an accompanying note to that effect,
> and is accompanied by the Chillu-R image.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-dot-reph-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d30,0d4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-dot-reph-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4e

svg_stack --direction=h malayalam-dot-reph-before.svg right-arrow.svg malayalam-dot-reph-after.svg > malayalam-dot-reph.svg


## 3.6 `pref`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ra-before.svg --features=-pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifﬁMalayalam-Regular.ttf --unicodes=0d4d,0d30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ra-after.svg --features=+pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d30

svg_stack --direction=h malayalam-pstf-ra-before.svg right-arrow.svg malayalam-pstf-ra-after.svg > malayalam-pstf-ra.svg


## 3.7 `blwf`

> Note: Noto Serif Malayalam includes a `blwf`-form "La" but does not
> include a feature that accesses it. It is included in several `akhn`
> ligatures, though. Instead, use SMC Rachana font.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwf-before.svg --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/malayalam/Rachana-Regular.ttf --unicodes=0d4d,0d32

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwf-after.svg --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/malayalam/Rachana-Regular.ttf --unicodes=0d4d,0d32

svg_stack --direction=h malayalam-blwf-before.svg right-arrow.svg malayalam-blwf-after.svg > malayalam-blwf.svg

## 3.9 `half`

> Note: Added a note to the shaping text about using `half` for Chillu
> lookups.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-half-before.svg --features=+half --background=FFFFFF00 --preserve-default-ignorables /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d15,0d4d,2005,200d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-half-after.svg --features=+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d15,0d4d,200d

svg_stack --direction=h malayalam-half-before.svg right-arrow.svg malayalam-half-after.svg > malayalam-half.svg


## 3.10 `pstf`

> Note: Uses the same images as 2.7

## 3.12 `cjct`

> Note: Noto Serif Malayalam implements this as an `akhn` feature.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-cjct-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d38,0d4d,0d31,0d4d,0d31

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-cjct-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d38,0d4d,0d31,0d4d,0d31

svg_stack --direction=h malayalam-cjct-before.svg right-arrow.svg malayalam-cjct-after.svg > malayalam-cjct.svg


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-position-before.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d47,0d2c,0d4d,0d1e,0d4d,0d1c,0d3e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-position-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d2c,0d4d,0d1e,0d4d,0d1c,0d4b

svg_stack --direction=h malayalam-matra-position-before.svg right-arrow.svg malayalam-matra-position-after.svg > malayalam-matra-position.svg


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-repha-position-before.svg --features=+akhn,-abvm,-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d4e,200d,0d23,0d4d,200d,0d21,0d41

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-repha-position-after.svg --features=+akhn,+abvm,+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d4e,0d23,0d4d,200d,0d21,0d41

svg_stack --direction=h malayalam-repha-position-before.svg right-arrow.svg malayalam-repha-position-after.svg > malayalam-repha-position.svg


## 4.4 Pre-base reordering

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pref-position-before.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=25cc,0d4d,0d30,0d39,0d4d,0d23,0d4d,0d21,0d4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pref-position-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d39,0d4d,0d23,0d4d,0d21,0d4d,0d30,0d4c

svg_stack --direction=h malayalam-pref-position-before.svg right-arrow.svg malayalam-pref-position-after.svg > malayalam-pref-position.svg


## 5 `blws`

> Note: Noto Serif and Sans Malayalam have blws-like "La" features in
> other lookups, such as `akhn`. I have not been able to isolate one
> of them for usage.


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-psts-before.svg --features=-psts,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d35,0d4d,0d35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-psts-after.svg --features=+psts,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d35,0d4d,0d35

svg_stack --direction=h malayalam-psts-before.svg right-arrow.svg malayalam-psts-after.svg > malayalam-psts.svg

## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-haln-before.svg --features=-haln --background=FFFFFF00 --preserve-default-ignorables /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d33,0d4d,2005,200d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-haln-after.svg --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf --unicodes=0d33,0d4d,200d

svg_stack --direction=h malayalam-haln-before.svg right-arrow.svg malayalam-haln-after.svg > malayalam-haln.svg


## 6 `abvm`

hb-view --font-size=110 --margin=2,32,2,16 --output-file=malayalam-abvm-before.svg --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d0a,0d01

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-abvm-after.svg --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d0a,0d01

svg_stack --direction=h malayalam-abvm-before.svg right-arrow.svg malayalam-abvm-after.svg > malayalam-abvm.svg


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwm-before.svg --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d34,0d62

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwm-after.svg --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d34,0d62

svg_stack --direction=h malayalam-blwm-before.svg right-arrow.svg malayalam-blwm-after.svg > malayalam-blwm.svg







