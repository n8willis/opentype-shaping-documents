# Commands used to generate the images in [opentype-shaping-hebrew.md](../../opentype-shaping-hebrew.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-ccmp-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d5,05c1

hb-view --font-size=110 --margin=2,24,2,24 --output-file=hebrew-ccmp-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d5,05c1

svg_stack.py --direction=h hebrew-ccmp-before.svg right-arrow.svg hebrew-ccmp-after.svg > hebrew-ccmp.svg


## 2 Alphabetic Presentation Forms

> Note: Noto Sans Hebrew implements these compositions in a `ccmp`
> lookup. Noto Serif Hebrew does not.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d9,05b4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-apf-after.svg --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=fb1d

svg_stack.py --direction=h hebrew-apf-before.svg right-arrow.svg hebrew-apf-after.svg > hebrew-apf.svg


## 4.1 `liga`

hb-view --font-size=110 --margin=2,16,2,24 --output-file=hebrew-liga-before.svg --features=-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=25cc,05b1,200d,05bd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-liga-after.svg --features=+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=25cc,05b1,200d,05bd

svg_stack.py --direction=h hebrew-liga-before.svg right-arrow.svg hebrew-liga-after.svg > hebrew-liga.svg


## `calt`

> The `calt` feature clearly gets applied; it's unclear why it was
> left off of the list in the initial release of this document.

hb-view --font-size=110 --margin=2,16,2,24 --output-file=hebrew-calt-before.svg --features=-calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05dc,05b4,05b8,05dd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-calt-after.svg --features=+calt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05dc,05b4,05b8,05dd

svg_stack.py --direction=h hebrew-calt-before.svg right-arrow.svg hebrew-calt-after.svg > hebrew-calt.svg


## 4.2 `dlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-before.svg --features=-dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d0,05dc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-dlig-after.svg --features=+dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d0,05dc

svg_stack.py --direction=h hebrew-dlig-before.svg right-arrow.svg hebrew-dlig-after.svg > hebrew-dlig.svg


## 5.1 `kern`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-kern-before.svg --features=-kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d2,05e2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-kern-after.svg --features=+kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d2,05e2

svg_stack.py --direction=h hebrew-kern-before.svg right-arrow.svg hebrew-kern-after.svg > hebrew-kern.svg


## 5.2 `mark`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-before.svg --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d3,05b1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=hebrew-mark-after.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.otf --unicodes=05d3,05b1

svg_stack.py --direction=h hebrew-mark-before.svg right-arrow.svg hebrew-mark-after.svg > hebrew-mark.svg









































