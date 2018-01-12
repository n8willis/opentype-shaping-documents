# Commands used to generate the images in [opentype-shaping-devanagari.md](/[opentype-shaping-devanagari.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.

