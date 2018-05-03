# Commands used to generate the images in [opentype-shaping-mongolian.md](../../opentype-shaping-mongolian.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### VS

#### No VS
#### VS dotted form


## 1. Kinzi

> Note: Noto Sans Myanmar does not implement the `rphf` feature for
> unknown reasons.

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-before.png --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,103a,1039,25cc

montage myanmar-kinzi-ra-before.png right-arrow.png myanmar-kinzi-ra-after.png -geometry +0+0 -background transparent myanmar-kinzi-ra.png


### Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-before.png --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,103a,1039,25cc

montage myanmar-kinzi-nga-before.png right-arrow.png myanmar-kinzi-nga-after.png -geometry +0+0 -background transparent myanmar-kinzi-nga.png


### Mon Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-before.png --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=105a,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-after.png --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=105a,103a,1039,25cc

montage myanmar-kinzi-monnga-before.png right-arrow.png myanmar-kinzi-monnga-after.png -geometry +0+0 -background transparent myanmar-kinzi-monnga.png





























