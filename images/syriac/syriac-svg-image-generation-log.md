# Commands used to generate the images in [opentype-shaping-syriac.md](../../opentype-shaping-syriac.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Dalath Rish group ##

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-dalath-rish.svg --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0715,072a,0716


## 3. `stch`

> Note: Noto seems to implement this in a set of `calt` substitutions,
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-stch-before.svg --features=-stch,-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0732,070f,0728,0721,0735,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-stch-after.svg --features=+stch --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0732,070f,0728,0721,0735,0710

svg_stack --direction=h syriac-stch-before.svg right-arrow.svg syriac-stch-after.svg > syriac-stch.svg


## 4.1 `locl`

> Note: None found in Noto fonts.


## 4.2 `isol`

> Note: none found in Noto fonts.


## 4.3 `fina`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-before.svg --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fina-after.svg --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0722


## 4.4 `fin2`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-before.svg --features=-fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin2-after.svg --features=+fin2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0717,0710

svg_stack --direction=h syriac-fin2-before.svg right-arrow.svg syriac-fin2-after.svg > syriac-fin2.svg


## 4.5 `fin3`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-before.svg --features=-fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-fin3-after.svg --features=+fin3 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072f,0710

svg_stack --direction=h syriac-fin3-before.svg right-arrow.svg syriac-fin3-after.svg > syriac-fin3.svg


## 4.6 `medi`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-before.svg --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-medi-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0724,25cc

svg_stack --direction=h syriac-medi-before.svg right-arrow.svg syriac-medi-after.svg > syriac-medi.svg


## 4.7 `med2`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-med2-before.svg --features=-med2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0710,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-med2-after.svg --features=+med2 --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=25cc,0710,25cc

svg_stack --direction=h syriac-med2-before.svg right-arrow.svg syriac-med2-after.svg > syriac-med2.svg


## 4.8 `init`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-init-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0721,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-init-after.svg --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0721,25cc

svg_stack --direction=h syriac-init-before.svg right-arrow.svg syriac-init-after.svg > syriac-init.svg


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-rlig-before.svg --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072a,25cc,0308

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-rlig-after.svg --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=072a,0308

svg_stack --direction=h syriac-rlig-before.svg right-arrow.svg syriac-rlig-after.svg > syriac-rlig.svg


## 4.11 `calt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-calt-before.svg --features=-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0720,071c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-calt-after.svg --features=+calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf --unicodes=0720,071c

svg_stack --direction=h syriac-calt-before.svg right-arrow.svg syriac-calt-after.svg > syriac-calt.svg


## 5.1 `liga`

> Note: Noto Syriac implements this as a `calt` lookup for unknown reasons.
>
> This seems to be a known shortcoming. See
> [https://github.com/googlei18n/noto-fonts/issues/665](https://github.com/googlei18n/noto-fonts/issues/665)
> for more information.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-liga-before.svg --features=-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0720,0710

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-liga-after.svg --features=+calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf --unicodes=0720,0710

svg_stack --direction=h syriac-liga-before.svg right-arrow.svg syriac-liga-after.svg > syriac-liga.svg


## 5.2 `dlig`

> Note: none found in Noto Syriac.
>
> This seems to be a known shortcoming. See
> [https://github.com/googlei18n/noto-fonts/issues/665](https://github.com/googlei18n/noto-fonts/issues/665)
> for more information.


## 7.3 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-mark-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0733

hb-view --font-size=110 --margin=2,16,2,16 --output-file=syriac-mark-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf --unicodes=0712,0733

svg_stack --direction=h syriac-mark-before.svg right-arrow.svg syriac-mark-after.svg > syriac-mark.svg


## 7.4 `mkmk`

> Note: Noto Sans Syriac (all) fonts have a `mkmk` table but it does
> not seem to work.



























