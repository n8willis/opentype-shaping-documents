# Commands used to generate the images in [opentype-shaping-khmer.md](../../opentype-shaping-khmer.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### Coeng forms

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-coeng-kha-before.png --features=-blwf,-pstf --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17d2,1783

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-coeng-kha-after.png --features=+blwf,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17d2,1783

montage khmer-coeng-kha-before.png right-arrow.png khmer-coeng-kha-after.png -geometry +0+0 -background transparent khmer-coeng-kha.png


## The khmr shaping model

### Robat

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-robat.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17cc


## 2.2 Matra decomposition

> Note: Noto Serif Khmer has decompositions for the
> non-canonical-in-Unicode multi-part matras implemented in `psts`
> features, but I have not figured out how to activate them in isolation.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-matra-decomposition-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17c4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-matra-decomposition-after.png --features=+ccmp,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17c1,25cc,17b6

montage khmer-matra-decomposition-before.png right-arrow.png khmer-matra-decomposition-after.png -geometry +0+0 -background transparent khmer-matra-decomposition.png


## 2.4 Pre-base-reordering Ro

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pref-before.png --features=-pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1786,25cc,17d2,179a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pref-after.png --features=+pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1786,17d2,179a

montage khmer-pref-before.png right-arrow.png khmer-pref-after.png -geometry +0+0 -background transparent khmer-pref.png


## 3.1 `locl`

No examples found in Noto Khmer.


## 3.2 `ccmp`

No examples found in Noto Khmer.


## 3.3 `pref`

Same as pre-base-reordering Ro.


## 3.4 `blwf`

> Note: altered bottom-margin number to fit.

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-blwf-before.png --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178c,25cc,17d2,17af

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-blwf-after.png --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178c,17d2,17af

montage khmer-blwf-before.png right-arrow.png khmer-blwf-after.png -geometry +0+0 -background transparent khmer-blwf.png


## 3.5 `abvf`

> Note: Noto Serif Khmer implements this as a `abvs` lookup.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvf-before.png --features=-abvf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17ca

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvf-after.png --features=+abvf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17ca

montage khmer-abvf-before.png right-arrow.png khmer-abvf-after.png -geometry +0+0 -background transparent khmer-abvf.png

## 3.6 `pstf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pstf-before.png --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17d2,179f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pstf-after.png --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17d2,179f

montage khmer-pstf-before.png right-arrow.png khmer-pstf-after.png -geometry +0+0 -background transparent khmer-pstf.png

## 3.7 `cfar`

No examples found in Noto Khmer.


## 4 `pres`

> Note: Adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-pres-before.png --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17d2,179a,17d2,1781

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-pres-after.png --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17d2,179a,17d2,1781

montage khmer-pres-before.png right-arrow.png khmer-pres-after.png -geometry +0+0 -background transparent khmer-pres.png


## 4 `blws`

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blws-before.png --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17d2,1780

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blws-after.png --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17d2,1780

montage khmer-blws-before.png right-arrow.png khmer-blws-after.png -geometry +0+0 -background transparent khmer-blws.png


## 4 `abvs`

hb-view --font-size=110 --margin=32,16,2,16 --output-file=khmer-abvs-before.png --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1796,17b7,17cd

hb-view --font-size=110 --margin=32,16,2,16 --output-file=khmer-abvs-after.png --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1796,17b7,17cd

montage khmer-abvs-before.png right-arrow.png khmer-abvs-after.png -geometry +0+0 -background transparent khmer-abvs.png


## 4 `psts`

> Note: Adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-psts-before.png --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1787,17d2,1785,17d2,1788

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-psts-after.png --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1787,17d2,1785,17d2,1788


## 4 `clig`

> Note: Noto Serif Khmer implements this twice, in clig and liga.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-clig-before.png --features=-clig,-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17b6

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-clig-after.png --features=+clig,+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17b6

montage khmer-clig-before.png right-arrow.png khmer-clig-after.png -geometry +0+0 -background transparent khmer-clig.png


## 4 `liga`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-liga-before.png --features=-clig,-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17d2,1788,17c5

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-liga-after.png --features=+clig,+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17d2,1788,17c5

montage khmer-liga-before.png right-arrow.png khmer-liga-after.png -geometry +0+0 -background transparent khmer-liga.png


## 5 `dist`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-dist-before.png --features=-dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179e,17d2,1798,179a,17bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-dist-after.png --features=+dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179e,17d2,1798,179a,17bc

montage khmer-dist-before.png right-arrow.png khmer-dist-after.png -geometry +0+0 -background transparent khmer-dist.png


## 5 `kern`

No examples found in Noto Khmer....


## 5 `blwm`

> Note: adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blwm-before.png --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17bc

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blwm-after.png --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17bc

montage khmer-blwm-before.png right-arrow.png khmer-blwm-after.png -geometry +0+0 -background transparent khmer-blwm.png


## 5 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvm-before.png --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178e,17b7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvm-after.png --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178e,17b7

montage khmer-abvm-before.png right-arrow.png khmer-abvm-after.png -geometry +0+0 -background transparent khmer-abvm.png


## 5 `mkmk`

No examples found in Noto Khmer.









