# Commands used to generate the images in [opentype-shaping-mongolian.md](../../opentype-shaping-mongolian.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### VS

#### No VS

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-before.png --features=+psts --background=FFFFFF00 /home/nate/Dropbox/fonts-external/temporary-and-testing/padauk-3.003/PadaukBook-Regular.ttf --unicodes=1022

#### VS dotted form

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-after.png --features=+psts --preserve-default-ignorables --language=KHT --background=FFFFFF00 /home/nate/padauk-3.003/PadaukBook-Regular.ttf --unicodes=1022,fe00


montage myanmar-dotted-before.png right-arrow.png myanmar-dotted-after.png -geometry +0+0 -background transparent myanmar-dotted.png


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


## 2.4 Medial Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-before.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1017,200D,103C

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1017,103C

montage myanmar-medial-ra-before.png right-arrow.png myanmar-medial-ra-after.png -geometry +0+0 -background transparent myanmar-medial-ra.png


## 3.1 locl

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-before.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,103d,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-after.png --features=+psts --language=KSW --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,103d,103e

montage myanmar-locl-before.png right-arrow.png myanmar-locl-after.png -geometry +0+0 -background transparent myanmar-locl.png


## 3.3 rphf

> Same as Kinzi


## 3.4 pref

> Note: Noto Sans Myanmar does not implement any pref features for
> unknown reasons. This example shows a basic-shaping feature to
> distinguish pref from the more stylistic applications of pres.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-before.png --features=-pref  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=103c,103f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-after.png --features=+pref  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=103f,103c

montage myanmar-pref-before.png right-arrow.png myanmar-pref-after.png -geometry +0+0 -background transparent myanmar-pref.png


## 3.5 blwf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-before.png --features=-blwf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,1039,100a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-after.png --features=+blwf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,1039,100a

montage myanmar-blwf-before.png right-arrow.png myanmar-blwf-after.png -geometry +0+0 -background transparent myanmar-blwf.png


## 3.6 pstf

> Note: Noto Sans Myanmar does not include a pstf feature for unknown
> reasons. This example shows an orthographically-selected variant, as
> referred to on
> https://r12a.github.io/scripts/myanmar/block#charTALL%20AA to
> distinguish pstf as an initial-shaping feature from the more
> stylistic applications of psts.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-before.png --features=-pstf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101d,102c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-after.png --features=+pstf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101d,102b

montage myanmar-pstf-before.png right-arrow.png myanmar-pstf-after.png -geometry +0+0 -background transparent myanmar-pstf.png


## 4 pres 














