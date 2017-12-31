# Commands used to generate the images in [opentype-shaping-devanagari.md](/[opentype-shaping-devanagari.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-nukt-before.png --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,25cc,093c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-nukt-after.png --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,093c

montage devanagari-nukt-before.png right-arrow.png devanagari-nukt-after.png -geometry +0+0 -background transparent devanagari-nukt.png



## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-kssa-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,25cc,094d,0937

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-kssa-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,094d,0937

montage devanagari-akhn-kssa-before.png right-arrow.png devanagari-akhn-kssa-after.png -geometry +0+0 -background transparent devanagari-akhn-kssa.png

### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-jnya-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091c,25cc,094d,091e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-jnya-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091c,094d,091e

montage devanagari-akhn-jnya-before.png right-arrow.png devanagari-akhn-jnya-after.png -geometry +0+0 -background transparent devanagari-akhn-jnya.png


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rphf-before.png --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,25cc,094d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rphf-after.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,25cc

montage devanagari-rphf-before.png right-arrow.png devanagari-rphf-after.png -geometry +0+0 -background transparent devanagari-rphf.png


## 3.5 `rkrf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rkrf-before.png --features=-init,-rkrf,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091d,25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rkrf-after.png --features=-init,+rkrf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091d,094d,0930

montage devanagari-rkrf-before.png right-arrow.png devanagari-rkrf-after.png -geometry +0+0 -background transparent devanagari-rkrf.png


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwf-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwf-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,094d,0930

montage devanagari-blwf-before.png right-arrow.png devanagari-blwf-after.png -geometry +0+0 -background transparent devanagari-blwf.png


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-half-before.png --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0932,094d,0930,25cc,094d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-half-after.png --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0932,094d,0930,094d

montage devanagari-half-before.png right-arrow.png devanagari-half-after.png -geometry +0+0 -background transparent devanagari-half.png


## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-vatu-before.png --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0936,25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-vatu-after.png --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0936,094d,0930

montage devanagari-vatu-before.png right-arrow.png devanagari-vatu-after.png -geometry +0+0 -background transparent devanagari-vatu.png


## 3.12 `cjct`

> Note: Noto Serif Devanagari implements this as `pres` for unknown
> reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-cjct-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0922,25cc,094d,0922

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-cjct-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0922,094d,0922

montage devanagari-cjct-before.png right-arrow.png devanagari-cjct-after.png -geometry +0+0 -background transparent devanagari-cjct.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-matra-position-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=093f,091e,094d,200c,091e,094d,0939,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-matra-position-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091e,094d,200c,091e,094d,0939,094d,0930,093f

montage devanagari-matra-position-before.png right-arrow.png devanagari-matra-position-after.png -geometry +0+0 -background transparent devanagari-matra-position.png


