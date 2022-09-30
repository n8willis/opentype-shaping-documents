# Commands used to generate the images in [opentype-shaping-syriac.md](../../opentype-shaping-syriac.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Dalath Rish group ##

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-dalath-rish.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0715,072a,0716


## 3. `stch`

> Note: Noto seems to implement this in a set of `calt` substitutions,
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-stch-before.png --features=-stch,-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0732,070f,0728,0721,0735,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-stch-after.png --features=+stch --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0732,070f,0728,0721,0735,0710

montage syriac-stch-before.png right-arrow.png syriac-stch-after.png -geometry +0+0 -background transparent syriac-stch.png


## 4.1 `locl`

> Note: None found in Noto fonts.


## 4.2 `isol`

> Note: none found in Noto fonts.


## 4.3 `fina`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-before.png --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722


## 4.4 `fin2`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-before.png --features=-fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-after.png --features=+fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

montage syriac-fin2-before.png right-arrow.png syriac-fin2-after.png -geometry +0+0 -background transparent syriac-fin2.png


## 4.5 `fin3`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-before.png --features=-fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-after.png --features=+fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

montage syriac-fin3-before.png right-arrow.png syriac-fin3-after.png -geometry +0+0 -background transparent syriac-fin3.png


## 4.6 `medi`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

montage syriac-medi-before.png right-arrow.png syriac-medi-after.png -geometry +0+0 -background transparent syriac-medi.png


## 4.7 `med2`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-med2-before.png --features=-med2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0710,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-med2-after.png --features=+med2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0710,25cc

montage syriac-med2-before.png right-arrow.png syriac-med2-after.png -geometry +0+0 -background transparent syriac-med2.png


## 4.8 `init`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-init-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0721,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-init-after.png --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0721,25cc

montage syriac-init-before.png right-arrow.png syriac-init-after.png -geometry +0+0 -background transparent syriac-init.png


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-rlig-before.png --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072a,25cc,0308

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-rlig-after.png --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072a,0308

montage syriac-rlig-before.png right-arrow.png syriac-rlig-after.png -geometry +0+0 -background transparent syriac-rlig.png


## 4.11 `calt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-calt-before.png --features=-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0720,071c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-calt-after.png --features=+calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0720,071c

montage syriac-calt-before.png right-arrow.png syriac-calt-after.png -geometry +0+0 -background transparent syriac-calt.png


## 5.1 `liga`

> Note: Noto Syriac implements this as a `calt` lookup for unknown reasons.
>
> This seems to be a known shortcoming. See
> [https://github.com/googlei18n/noto-fonts/issues/665](https://github.com/googlei18n/noto-fonts/issues/665)
> for more information.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-liga-before.png --features=-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0720,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-liga-after.png --features=+calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0720,0710

montage syriac-liga-before.png right-arrow.png syriac-liga-after.png -geometry +0+0 -background transparent syriac-liga.png


## 5.2 `dlig`

> Note: none found in Noto Syriac.
>
> This seems to be a known shortcoming. See
> [https://github.com/googlei18n/noto-fonts/issues/665](https://github.com/googlei18n/noto-fonts/issues/665)
> for more information.


## 7.3 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-mark-before.png --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0733

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-mark-after.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0733

montage syriac-mark-before.png right-arrow.png syriac-mark-after.png -geometry +0+0 -background transparent syriac-mark.png


## 7.4 `mkmk`

> Note: Noto Sans Syriac (all) fonts have a `mkmk` table but it does
> not seem to work.



























