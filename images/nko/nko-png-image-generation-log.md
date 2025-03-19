# Commands used to generate the images in [opentype-shaping-nko.md](../../opentype-shaping-nko.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 4.3 `fina`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-fina-before.png --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e5

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-fina-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e5

montage nko-fina-before.png right-arrow.png nko-fina-after.png -geometry +0+0 -background transparent nko-fina.png


## 4.6 `medi`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-medi-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e8,07fa

b-view --font-size=110 --margin=2,16,2,16 --output-file=nko-medi-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07e8,07fa

montage nko-medi-before.png right-arrow.png nko-medi-after.png -geometry +0+0 -background transparent nko-medi.png


## 4.8 `init`

> Note: Noto Sans NKo does not have a dotted-circle glyph. These
> images use `U+07fa`, the lajanyalan (N'Ko kashida) in its place.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-init-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07da,07fa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-init-after.png --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07da,07fa

montage nko-init-before.png right-arrow.png nko-init-after.png -geometry +0+0 -background transparent nko-init.png


## 7.3 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-mark-before.png --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07d5,07f1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=nko-mark-after.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf --unicodes=07fa,07d5,07f1

montage nko-mark-before.png right-arrow.png nko-mark-after.png -geometry +0+0 -background transparent nko-mark.png
















































