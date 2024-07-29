# Commands used to generate the images in [opentype-shaping-tibetan.md](../../opentype-shaping-tibetan.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Syllable identification

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-syllable.svg --features=  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f51,0f54,0f7a,0f0b,0f56,0f66,0f90,0fb2,0f74,0f53


## 1.2 ccmp

hb-view --font-size=110 --margin=2,16,2,72 --output-file=tibetan-ccmp-before.svg --features=-ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f77

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-ccmp-after.svg --features=+ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0fb2,00a0,00a0,0f71,25cc,0f80

svg_stack --direction=h tibetan-ccmp-before.svg right-arrow.svg tibetan-ccmp-after.svg > tibetan-ccmp.svg


## 2.1 abvs

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvs-before.svg --features=-abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f49,0f7b,0f7e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvs-after.svg --features=+abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f49,0f7b,0f7e

svg_stack --direction=h tibetan-abvs-before.svg right-arrow.svg tibetan-abvs-after.svg > tibetan-abvs.svg


## 2.2 blws

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blws-before.svg --features=-blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f4a,0f91

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blws-after.svg --features=+blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f4a,0f91

svg_stack --direction=h tibetan-blws-before.svg right-arrow.svg tibetan-blws-after.svg > tibetan-blws.svg


## 2.3 calt

> Note: Noto Sans Tibetan calls this substitution twice, in calt and
> in abvs.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-calt-before.svg --features=-calt,-abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f59,0f7d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-calt-after.svg --features=+calt  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f59,0f7d

svg_stack --direction=h tibetan-calt-before.svg right-arrow.svg tibetan-calt-after.svg > tibetan-calt.svg


## 2.4 liga

> Note: Noto Sans Tibetan implements this as a ccmp substitution for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-liga-before.svg --features=-ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f97,0f39,0fb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-liga-after.svg --features=+ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f97,0f39,0fb7

svg_stack --direction=h tibetan-liga-before.svg right-arrow.svg tibetan-liga-after.svg > tibetan-liga.svg


## 3 kern

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-kern-before.svg --features=-kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f65,0f0b,0f62,0fa9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-kern-after.svg --features=+kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f65,0f0b,0f62,0fa9

svg_stack --direction=h tibetan-kern-before.svg right-arrow.svg tibetan-kern-after.svg > tibetan-kern.svg


## 3 abvm

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvm-before.svg --features=-abvm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f61,0f80,0f7e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvm-after.svg --features=+abvm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f61,0f80,0f7e

svg_stack --direction=h tibetan-abvm-before.svg right-arrow.svg tibetan-abvm-after.svg > tibetan-abvm.svg


## 3 blwm

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blwm-before.svg --features=-blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f59,0fb3,0f71,0f74

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blwm-after.svg --features=+blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f59,0fb3,0f71,0f74

svg_stack --direction=h tibetan-blwm-before.svg right-arrow.svg tibetan-blwm-after.svg > tibetan-blwm.svg


## 3 mkmk

> Note: Noto Sans Tibetan implements this is both blwm and mkmk for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-mkmk-before.svg --features=-mkmk,-blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f51,0f71,0f35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-mkmk-after.svg --features=+mkmk  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf --unicodes=0f51,0f71,0f35

svg_stack --direction=h tibetan-mkmk-before.svg right-arrow.svg tibetan-mkmk-after.svg > tibetan-mkmk.svg

































