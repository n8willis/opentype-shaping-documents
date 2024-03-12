# Commands used to generate the images in [opentype-shaping-devanagari.md](../../opentype-shaping-devanagari.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 3.1 `locl`

> Note: Noto Devanagari has a 'MAR' locl feature. 



## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-nukt-before.svg --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,25cc,093c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-nukt-after.svg --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,093c

svg_stack --direction=h devanagari-nukt-before.svg right-arrow.svg devanagari-nukt-after.svg > devanagari-nukt.svg



## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-kssa-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,25cc,094d,0937

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-kssa-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,094d,0937

svg_stack --direction=h devanagari-akhn-kssa-before.svg right-arrow.svg devanagari-akhn-kssa-after.svg > devanagari-akhn-kssa.svg

### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-jnya-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091c,25cc,094d,091e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-akhn-jnya-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091c,094d,091e

svg_stack --direction=h devanagari-akhn-jnya-before.svg right-arrow.svg devanagari-akhn-jnya-after.svg > devanagari-akhn-jnya.svg


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rphf-before.svg --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,25cc,094d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rphf-after.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,25cc

svg_stack --direction=h devanagari-rphf-before.svg right-arrow.svg devanagari-rphf-after.svg > devanagari-rphf.svg


## 3.5 `rkrf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rkrf-before.svg --features=-init,-rkrf,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091d,25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-rkrf-after.svg --features=-init,+rkrf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091d,094d,0930

svg_stack --direction=h devanagari-rkrf-before.svg right-arrow.svg devanagari-rkrf-after.svg > devanagari-rkrf.svg


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwf-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwf-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,094d,0930

svg_stack --direction=h devanagari-blwf-before.svg right-arrow.svg devanagari-blwf-after.svg > devanagari-blwf.svg


## 3.9 `half`

### Half form

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-half-before.svg --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0932,094d,0930,25cc,094d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-half-after.svg --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0932,094d,0930,094d

svg_stack --direction=h devanagari-half-before.svg right-arrow.svg devanagari-half-after.svg > devanagari-half.svg

### Eyelash Ra

> Note that Noto Devanagari eyelash-Ra substitution does not appear to
> work when using `U+25cc` dotted circle as the "base consonant"
> substitute. Hence, a real consonant glyph is used instead. But it is
> important that "Ra" _not_ be used as the "base consonant", as this
> triggers "Rakaar".

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-eyelash-ra-before.svg --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0931,094d,0932

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-eyelash-ra-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0931,094d,0932

svg_stack --direction=h devanagari-eyelash-ra-before.svg right-arrow.svg devanagari-eyelash-ra-after.svg > devanagari-eyelash-ra.svg


## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-vatu-before.svg --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0936,25cc,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-vatu-after.svg --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0936,094d,0930

svg_stack --direction=h devanagari-vatu-before.svg right-arrow.svg devanagari-vatu-after.svg > devanagari-vatu.svg


## 3.12 `cjct`

> Note: Noto Serif Devanagari implements this as `pres` for unknown
> reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-cjct-before.svg --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0922,25cc,094d,0922

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-cjct-after.svg --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0922,094d,0922

svg_stack --direction=h devanagari-cjct-before.svg right-arrow.svg devanagari-cjct-after.svg > devanagari-cjct.svg


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-matra-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=093f,091e,094d,200c,091e,094d,0939,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-matra-position-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=091e,094d,200c,091e,094d,0939,094d,0930,093f

svg_stack --direction=h devanagari-matra-position-before.svg right-arrow.svg devanagari-matra-position-after.svg > devanagari-matra-position.svg


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-reph-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,25cc,092f,094d,0932,094d,092e,094d,0930

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-reph-position-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,092f,094d,0932,094d,092e,094d,0930

svg_stack --direction=h devanagari-reph-position-before.svg right-arrow.svg devanagari-reph-position-after.svg > devanagari-reph-position.svg


## 5 `init`

> Note: Noto Devanagari and Murty don't implement `init`.


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-pres-before.svg --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0916,093f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-pres-after.svg --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0916,093f

svg_stack --direction=h devanagari-pres-before.svg right-arrow.svg devanagari-pres-after.svg > devanagari-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-abvs-before.svg --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,25cc,0949

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-abvs-after.svg --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0930,094d,25cc,0949

svg_stack --direction=h devanagari-abvs-before.svg right-arrow.svg devanagari-abvs-after.svg > devanagari-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blws-before.svg --features=-init,-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0939,0944

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blws-after.svg --features=-init,+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0939,0944

svg_stack --direction=h devanagari-blws-before.svg right-arrow.svg devanagari-blws-after.svg > devanagari-blws.svg


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-psts-before.svg --features=-init,-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,093c,0940

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-psts-after.svg --features=-init,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,093c,0940

svg_stack --direction=h devanagari-psts-before.svg right-arrow.svg devanagari-psts-after.svg > devanagari-psts.svg


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-haln-before.svg --features=-init,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,095c,094d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-haln-after.svg --features=-init,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=25cc,095c,094d

svg_stack --direction=h devanagari-haln-before.svg right-arrow.svg devanagari-haln-after.svg > devanagari-haln.svg


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-abvm-before.svg --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,0948

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-abvm-after.svg --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=092b,0948

svg_stack --direction=h devanagari-abvm-before.svg right-arrow.svg devanagari-abvm-after.svg > devanagari-abvm.svg


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwm-before.svg --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,0943

hb-view --font-size=110 --margin=2,16,2,16 --output-file=devanagari-blwm-after.svg --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf --unicodes=0915,0943

svg_stack --direction=h devanagari-blwm-before.svg right-arrow.svg devanagari-blwm-after.svg > devanagari-blwm.svg
