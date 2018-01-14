# Commands used to generate the images in [opentype-shaping-malayalam.md](/[opentype-shaping-malayalam.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-decompose-before.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-decompose-after.png --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d46,25cc,0d57

montage malayalam-matra-decompose-before.png right-arrow.png malayalam-matra-decompose-after.png -geometry +0+0 -background transparent malayalam-matra-decompose.png


## 2.7 post-base consonants

### Ya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ya-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ya-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d2f

montage malayalam-pstf-ya-before.png right-arrow.png malayalam-pstf-ya-after.png -geometry +0+0 -background transparent malayalam-pstf-ya.png

### Va

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-va-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-va-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d35

montage malayalam-pstf-va-before.png right-arrow.png malayalam-pstf-va-after.png -geometry +0+0 -background transparent malayalam-pstf-va.png


## 3.2 `nukt`

> Note: Noto Serif Malayalam uses `U+0323` "Combining dot below" in
> its mark-placement lookups, not a Nukta (which does not exist in the
> Malayalam Unicode block).

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-nukt-before.png --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d18,25cc,0323

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-nukt-after.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d18,0323

montage malayalam-nukt-before.png right-arrow.png malayalam-nukt-after.png -geometry +0+0 -background transparent malayalam-nukt.png


## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-kssa-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d15,0d4d,0d37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-kssa-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d15,0d4d,0d37

montage malayalam-akhn-kssa-before.png right-arrow.png malayalam-akhn-kssa-after.png -geometry +0+0 -background transparent malayalam-akhn-kssa.png

### NnTta

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-nntta-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d23,0d4d,0d1f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-nntta-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d23,0d4d,0d1f

montage malayalam-akhn-nntta-before.png right-arrow.png malayalam-akhn-nntta-after.png -geometry +0+0 -background transparent malayalam-akhn-nntta.png

> Note: The "Chillu R" is shown here because it may be implemented as
> an akhand form and that makes Malayalam distinct from several other
> Indic scripts.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-chillu-r-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d30,0d4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-akhn-chillu-r-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d7c

montage malayalam-akhn-chillu-r-before.png right-arrow.png malayalam-akhn-chillu-r-after.png -geometry +0+0 -background transparent malayalam-akhn-chillu-r.png


## 3.4 `rphf`

> Note: Malayalam modern orthography does not use Reph. The dot-reph
> substitution here is shown with an accompanying note to that effect,
> and is accompanied by the Chillu-R image.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-dot-reph-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d30,0d4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-dot-reph-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4e

montage malayalam-dot-reph-before.png right-arrow.png malayalam-dot-reph-after.png -geometry +0+0 -background transparent malayalam-dot-reph.png


## 3.6 `pref`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ra-before.png --features=-pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-pstf-ra-after.png --features=+pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d4d,0d30

montage malayalam-pstf-ra-before.png right-arrow.png malayalam-pstf-ra-after.png -geometry +0+0 -background transparent malayalam-pstf-ra.png


## 3.7 `blwf`

> Note: Noto Serif Malayalam includes a `blwf`-form "La" but does not
> include a feature that accesses it. It is included in several `akhn`
> ligatures, though.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwf-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d2e,0d4d,0d32

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-blwf-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d2e,0d4d,0d32

montage malayalam-blwf-before.png right-arrow.png malayalam-blwf-after.png -geometry +0+0 -background transparent malayalam-blwf.png

## 3.10 `pstf`

> Note: Uses the same images as 2.7

## 3.12 `cjct`

> Note: Noto Serif Malayalam implements this as an `akhn` feature.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-cjct-before.png --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d38,0d4d,0d31,0d4d,0d31

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-cjct-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d38,0d4d,0d31,0d4d,0d31

montage malayalam-cjct-before.png right-arrow.png malayalam-cjct-after.png -geometry +0+0 -background transparent malayalam-cjct.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-position-before.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d47,0d2c,0d4d,0d1e,0d4d,0d1c,0d3e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-matra-position-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d2c,0d4d,0d1e,0d4d,0d1c,0d4b

montage malayalam-matra-position-before.png right-arrow.png malayalam-matra-position-after.png -geometry +0+0 -background transparent malayalam-matra-position.png


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-reph-position-before.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=25cc,0d4d,0d30,0d39,0d4d,0d23,0d4d,0d21,0d4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=malayalam-reph-position-after.png --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf --unicodes=0d39,0d4d,0d23,0d4d,0d21,0d4d,0d30,0d4c

montage malayalam-reph-position-before.png right-arrow.png malayalam-reph-position-after.png -geometry +0+0 -background transparent malayalam-reph-position.png

















