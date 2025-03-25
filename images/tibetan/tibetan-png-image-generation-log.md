# Commands used to generate the images in [opentype-shaping-tibetan.md](../../opentype-shaping-tibetan.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Syllable identification

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-syllable.png --features=  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f51,0f54,0f7a,0f0b,0f56,0f66,0f90,0fb2,0f74,0f53


## 1.2 ccmp

hb-view --font-size=110 --margin=2,16,2,72 --output-file=tibetan-ccmp-before.png --features=-ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f77

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-ccmp-after.png --features=+ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0fb2,00a0,00a0,0f71,25cc,0f80

montage tibetan-ccmp-before.png right-arrow.png tibetan-ccmp-after.png -geometry +0+0 -background transparent tibetan-ccmp.png


## 2.1 abvs

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvs-before.png --features=-abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f49,0f7b,0f7e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvs-after.png --features=+abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f49,0f7b,0f7e

montage tibetan-abvs-before.png right-arrow.png tibetan-abvs-after.png -geometry +0+0 -background transparent tibetan-abvs.png


## 2.2 blws

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blws-before.png --features=-blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f4a,0f91

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blws-after.png --features=+blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f4a,0f91

montage tibetan-blws-before.png right-arrow.png tibetan-blws-after.png -geometry +0+0 -background transparent tibetan-blws.png


## 2.3 calt

> Note: Noto Sans Tibetan calls this substitution twice, in calt and
> in abvs.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-calt-before.png --features=-calt,-abvs  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f59,0f7d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-calt-after.png --features=+calt  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f59,0f7d

montage tibetan-calt-before.png right-arrow.png tibetan-calt-after.png -geometry +0+0 -background transparent tibetan-calt.png


## 2.4 liga

> Note: Noto Sans Tibetan implements this as a ccmp substitution for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-liga-before.png --features=-ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f97,0f39,0fb7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-liga-after.png --features=+ccmp  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f97,0f39,0fb7

montage tibetan-liga-before.png right-arrow.png tibetan-liga-after.png -geometry +0+0 -background transparent tibetan-liga.png


## 3 kern

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-kern-before.png --features=-kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f65,0f0b,0f62,0fa9

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-kern-after.png --features=+kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f65,0f0b,0f62,0fa9

montage tibetan-kern-before.png right-arrow.png tibetan-kern-after.png -geometry +0+0 -background transparent tibetan-kern.png


## 3 abvm

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvm-before.png --features=-abvm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f61,0f80,0f7e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-abvm-after.png --features=+abvm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f61,0f80,0f7e

montage tibetan-abvm-before.png right-arrow.png tibetan-abvm-after.png -geometry +0+0 -background transparent tibetan-abvm.png


## 3 blwm

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blwm-before.png --features=-blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f59,0fb3,0f71,0f74

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-blwm-after.png --features=+blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f59,0fb3,0f71,0f74

montage tibetan-blwm-before.png right-arrow.png tibetan-blwm-after.png -geometry +0+0 -background transparent tibetan-blwm.png


## 3 mkmk

> Note: Noto Sans Tibetan implements this is both blwm and mkmk for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-mkmk-before.png --features=-mkmk,-blwm  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f51,0f71,0f35

hb-view --font-size=110 --margin=2,16,2,16 --output-file=tibetan-mkmk-after.png --features=+mkmk  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf --unicodes=0f51,0f71,0f35

montage tibetan-mkmk-before.png right-arrow.png tibetan-mkmk-after.png -geometry +0+0 -background transparent tibetan-mkmk.png

































