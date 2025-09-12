# Commands used to generate the images in [opentype-shaping-tamil.md](../../opentype-shaping-tamil.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192



## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-decompose-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bcc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-decompose-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bc6,25cc,0bd7

svg_stack --direction=h tamil-matra-decompose-before.svg right-arrow.svg tamil-matra-decompose-after.svg > tamil-matra-decompose.svg


## 3.2 `nukt`

> None found. Testing with Grantha Nukta.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-nukt-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bf5,25cc,1133c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-nukt-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bf5,1133c

svg_stack --direction=h tamil-nukt-before.svg right-arrow.svg tamil-nukt-after.svg > tamil-nukt.svg


## 3.3 `akhn`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-akhn-kssa-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0b95,0bcd,0bb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-akhn-kssa-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0b95,0bcd,0bb7

svg_stack --direction=h tamil-akhn-kssa-before.svg right-arrow.svg tamil-akhn-kssa-after.svg > tamil-akhn-kssa.svg


## 3.9 `half`

> Simulated output using a `mark` lookup; no example found.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-half-before.svg --features=-half,-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b99,25cc,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-half-after.svg --features=+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b99,0bcd

svg_stack --direction=h tamil-half-before.svg right-arrow.svg tamil-half-after.svg > tamil-half.svg


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-position-before.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bc6,0bb0,0bcd,0b9a,0bcd,0b9c,0bbe

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-matra-position-after.svg --features= --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb0,0bcd,0b9a,0bcd,0b9c,0bca

svg_stack --direction=h tamil-matra-position-before.svg right-arrow.svg tamil-matra-position-after.svg > tamil-matra-position.svg


## 5 `pres`

> Note: Noto Serif Tamil implements this as an `akhn` feature for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-pres-before.svg --features=-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb6,0bcd,0bb0,0bc0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-pres-after.svg --features=+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb6,0bcd,0bb0,0bc0

svg_stack --direction=h tamil-pres-before.svg right-arrow.svg tamil-pres-after.svg > tamil-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvs-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0baf,0bc0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvs-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0baf,0bc0

svg_stack --direction=h tamil-abvs-before.svg right-arrow.svg tamil-abvs-after.svg > tamil-abvs.svg


## 5 `blws`

> None found.


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-psts-before.svg --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb4,0bc2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-psts-after.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb4,0bc2

svg_stack --direction=h tamil-psts-before.svg right-arrow.svg tamil-psts-after.svg > tamil-psts.svg


## `haln`

> Simulated output using a `mark` lookup; no example found.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-haln-before.svg --features=-haln,-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b9e,25cc,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-haln-after.svg --features=+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf --unicodes=0b9e,0bcd

svg_stack --direction=h tamil-haln-before.svg right-arrow.svg tamil-haln-after.svg > tamil-haln.svg


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvm-before.svg --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb9,0bcd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tamil-abvm-after.svg --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf --unicodes=0bb9,0bcd

svg_stack --direction=h tamil-abvm-before.svg right-arrow.svg tamil-abvm-after.svg > tamil-abvm.svg


## 6 `blwm`

> None found.


















































































