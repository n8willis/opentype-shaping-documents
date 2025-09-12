# Commands used to generate the images in [opentype-shaping-khmer.md](../../opentype-shaping-khmer.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### Coeng forms

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-coeng-kha-before.svg --features=-blwf,-pstf --preserve-default-ignorables --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17d2,1783

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-coeng-kha-after.svg --features=+blwf,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17d2,1783

svg_stack.py --direction=h khmer-coeng-kha-before.svg right-arrow.svg khmer-coeng-kha-after.svg > khmer-coeng-kha.svg


## The khmr shaping model

### Robat

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-robat.svg --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17cc


## 2.2 Matra decomposition

> Note: Noto Serif Khmer has decompositions for the
> non-canonical-in-Unicode multi-part matras implemented in `psts`
> features, but I have not figured out how to activate them in isolation.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-matra-decomposition-before.svg --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17c4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-matra-decomposition-after.svg --features=+ccmp,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=17c1,25cc,17b6

svg_stack.py --direction=h khmer-matra-decomposition-before.svg right-arrow.svg khmer-matra-decomposition-after.svg > khmer-matra-decomposition.svg


## 2.4 Pre-base-reordering Ro

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pref-before.svg --features=-pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1786,25cc,17d2,179a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pref-after.svg --features=+pref --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1786,17d2,179a

svg_stack.py --direction=h khmer-pref-before.svg right-arrow.svg khmer-pref-after.svg > khmer-pref.svg


#### Duplicates for other subsections

cp khmer-pref.svg khmer-pref-1.svg

cluster_styles = [



## 3.1 `locl`

No examples found in Noto Khmer.


## 3.2 `ccmp`

No examples found in Noto Khmer.


## 3.3 `pref`

Same as pre-base-reordering Ro.


## 3.4 `blwf`

> Note: altered bottom-margin number to fit.

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-blwf-before.svg --features=-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178c,25cc,17d2,17af

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-blwf-after.svg --features=+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178c,17d2,17af

svg_stack.py --direction=h khmer-blwf-before.svg right-arrow.svg khmer-blwf-after.svg > khmer-blwf.svg


## 3.5 `abvf`

> Note: Noto Serif Khmer implements this as a `abvs` lookup.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvf-before.svg --features=-abvf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17ca

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvf-after.svg --features=+abvf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17ca

svg_stack.py --direction=h khmer-abvf-before.svg right-arrow.svg khmer-abvf-after.svg > khmer-abvf.svg

## 3.6 `pstf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pstf-before.svg --features=-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17d2,179f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-pstf-after.svg --features=+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=25cc,17d2,179f

svg_stack.py --direction=h khmer-pstf-before.svg right-arrow.svg khmer-pstf-after.svg > khmer-pstf.svg

## 3.7 `cfar`

No examples found in Noto Khmer.


## 4 `pres`

> Note: Adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-pres-before.svg --features=-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17d2,179a,17d2,1781

hb-view --font-size=110 --margin=2,16,32,16 --output-file=khmer-pres-after.svg --features=+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17d2,179a,17d2,1781

svg_stack.py --direction=h khmer-pres-before.svg right-arrow.svg khmer-pres-after.svg > khmer-pres.svg


## 4 `blws`

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blws-before.svg --features=-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17d2,1780

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blws-after.svg --features=+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17d2,1780

svg_stack.py --direction=h khmer-blws-before.svg right-arrow.svg khmer-blws-after.svg > khmer-blws.svg


## 4 `abvs`

hb-view --font-size=110 --margin=32,16,2,16 --output-file=khmer-abvs-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1796,17b7,17cd

hb-view --font-size=110 --margin=32,16,2,16 --output-file=khmer-abvs-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1796,17b7,17cd

svg_stack.py --direction=h khmer-abvs-before.svg right-arrow.svg khmer-abvs-after.svg > khmer-abvs.svg


## 4 `psts`

> Note: Adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-psts-before.svg --features=-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1787,17d2,1785,17d2,1788

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-psts-after.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1787,17d2,1785,17d2,1788


## 4 `clig`

> Note: Noto Serif Khmer implements this twice, in clig and liga.
>
> Note: It is no longer possible to deactivate clig in HarfBuzz. See
> the issue at https://github.com/harfbuzz/harfbuzz/issues/1310 for
> more information.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-clig-before.svg --features=-clig,-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17b6

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-clig-after.svg --features=+clig,+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1780,17b6

svg_stack.py --direction=h khmer-clig-before.svg right-arrow.svg khmer-clig-after.svg > khmer-clig.svg


## 4 `liga`

> Note: because Noto Serif Khmer duplicates all of its liga
> substitutions in clig, which cannot be disabled in HarfBuzz (see the
> preceding section about clig), it is not possible to disable the
> liga substitutions either.

hb-view --font-size=110 --margin=2,16,8,24 --output-file=khmer-liga-before.svg --features=-clig,-liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17d2,1788,17c5

hb-view --font-size=110 --margin=2,16,8,24 --output-file=khmer-liga-after.svg --features=+clig,+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179c,17d2,1788,17c5

svg_stack.py --direction=h khmer-liga-before.svg right-arrow.svg khmer-liga-after.svg > khmer-liga.svg


## 5 `dist`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-dist-before.svg --features=-dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179e,17d2,1798,179a,17bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-dist-after.svg --features=+dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=179e,17d2,1798,179a,17bc

svg_stack.py --direction=h khmer-dist-before.svg right-arrow.svg khmer-dist-after.svg > khmer-dist.svg


## 5 `kern`

No examples found in Noto Khmer....


## 5 `blwm`

> Note: adjusted bottom margin.

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blwm-before.svg --features=-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17bc

hb-view --font-size=110 --margin=2,16,48,16 --output-file=khmer-blwm-after.svg --features=+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=1789,17bc

svg_stack.py --direction=h khmer-blwm-before.svg right-arrow.svg khmer-blwm-after.svg > khmer-blwm.svg


## 5 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvm-before.svg --features=-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178e,17b7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=khmer-abvm-after.svg --features=+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf --unicodes=178e,17b7

svg_stack.py --direction=h khmer-abvm-before.svg right-arrow.svg khmer-abvm-after.svg > khmer-abvm.svg


## 5 `mkmk`

No examples found in Noto Khmer.









