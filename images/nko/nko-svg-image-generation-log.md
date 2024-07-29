# Commands used to generate the images in [opentype-shaping-nko.md](../../opentype-shaping-nko.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 4.3 `fina`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-fina-before.svg --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e5

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-fina-after.svg --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e5

svg_stack --direction=h nko-fina-before.svg right-arrow.svg nko-fina-after.svg > nko-fina.svg


## 4.6 `medi`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-medi-before.svg --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e8,07fa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-medi-after.svg --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e8,07fa

svg_stack --direction=h nko-medi-before.svg right-arrow.svg nko-medi-after.svg > nko-medi.svg


## 4.8 `init`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-init-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07da,07fa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-init-after.svg --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07da,07fa

svg_stack --direction=h nko-init-before.svg right-arrow.svg nko-init-after.svg > nko-init.svg


## 7.3 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-mark-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07d5,07f1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-mark-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07d5,07f1

svg_stack --direction=h nko-mark-before.svg right-arrow.svg nko-mark-after.svg > nko-mark.svg
















































