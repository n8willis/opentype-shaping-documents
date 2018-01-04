# Commands used to generate the images in [opentype-shaping-bengali.md](/[opentype-shaping-bengali.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-decompose-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ac9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-decompose-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ac5,25cc,0abe

montage gujarati-matra-decompose-before.png right-arrow.png gujarati-matra-decompose-after.png -geometry +0+0 -background transparent gujarati-matra-decompose.png


## 2.7 Post-base consonants

> None


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-nukt-before.png --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a97,25cc,0abc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-nukt-after.png --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a97,0abc

montage gujarati-nukt-before.png right-arrow.png gujarati-nukt-after.png -geometry +0+0 -background transparent gujarati-nukt.png

## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-kssa-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a95,25cc,0acd,0ab7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-kssa-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a95,0acd,0ab7

montage gujarati-akhn-kssa-before.png right-arrow.png gujarati-akhn-kssa-after.png -geometry +0+0 -background transparent gujarati-akhn-kssa.png

### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-jnya-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,25cc,0acd,0a9e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-akhn-jnya-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9c,0acd,0a9e

montage gujarati-akhn-jnya-before.png right-arrow.png gujarati-akhn-jnya-after.png -geometry +0+0 -background transparent gujarati-akhn-jnya.png


## 3.4 `rphf`


hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rphf-before.png --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,25cc,0acd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rphf-after.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,25cc

montage gujarati-rphf-before.png right-arrow.png gujarati-rphf-after.png -geometry +0+0 -background transparent gujarati-rphf.png


## 3.5 `rkrf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rkrf-before.png --features=-init,-rkrf,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-rkrf-after.png --features=-init,+rkrf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,0acd,0ab0

montage gujarati-rkrf-before.png right-arrow.png gujarati-rkrf-after.png -geometry +0+0 -background transparent gujarati-rkrf.png


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwf-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-blwf-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=25cc,0acd,0ab0

montage gujarati-blwf-before.png right-arrow.png gujarati-blwf-after.png -geometry +0+0 -background transparent gujarati-blwf.png


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-half-before.png --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aad,0acd,0ab0,25cc,0acd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-half-after.png --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aad,0acd,0ab0,0acd,25cc

montage gujarati-half-before.png right-arrow.png gujarati-half-after.png -geometry +0+0 -background transparent gujarati-half.png


## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-vatu-before.png --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa4,25cc,0acd,0ab0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-vatu-after.png --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa4,0acd,0ab0

montage gujarati-vatu-before.png right-arrow.png gujarati-vatu-after.png -geometry +0+0 -background transparent gujarati-vatu.png


## 3.12 `cjct`

> Note that Noto Serif Gujarati implements this in `pres` for unknown
> reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-cjct-before.png --features=-init,-pres,-cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,25cc,0acd,0aae

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-cjct-after.png --features=-init,+cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0aa6,0acd,0aae

montage gujarati-cjct-before.png right-arrow.png gujarati-cjct-after.png -geometry +0+0 -background transparent gujarati-cjct.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-position-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0abf,0a9f,0acd,0a9d,0acd,0ab9,0acd,0aa4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-matra-position-after.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9f,0acd,0a9d,0acd,0ab9,0acd,0aa4,0abf

montage gujarati-matra-position-before.png right-arrow.png gujarati-matra-position-after.png -geometry +0+0 -background transparent gujarati-matra-position.png


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-reph-position-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,25cc,0aab,0acd,0aa8,0acd,0a9a,0ac2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-reph-position-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aab,0acd,0aa8,0acd,0a9a,0ac2

montage gujarati-reph-position-before.png right-arrow.png gujarati-reph-position-after.png -geometry +0+0 -background transparent gujarati-reph-position.png


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-pres-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9e,0acd,0a9a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-pres-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0a9e,0acd,0a9a,25cc

montage gujarati-pres-before.png right-arrow.png gujarati-pres-after.png -geometry +0+0 -background transparent gujarati-pres.png


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvs-before.png --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aad,0ac0,0a82

hb-view --font-size=110 --margin=2,16,2,16 --output-file=gujarati-abvs-after.png --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf --unicodes=0ab0,0acd,0aad,0ac0,0a82

montage gujarati-abvs-before.png right-arrow.png gujarati-abvs-after.png -geometry +0+0 -background transparent gujarati-abvs.png







