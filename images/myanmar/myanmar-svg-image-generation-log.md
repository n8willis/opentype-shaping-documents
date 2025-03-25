# Commands used to generate the images in [opentype-shaping-myanmar.md](../../opentype-shaping-myanmar.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### Variation Selector

#### No VS

> Note: SIL Padauk 3.x implements the dotted-form feature, but not
> using Variation Selectors, for unknown reasons.
ﬁ
hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-before.svg --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/padauk-3.003/PadaukBook-Regular.ttf --unicodes=1022

#### VS dotted form

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-after.svg --features=+psts --preserve-default-ignorables --language=KHT --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/padauk-3.003/PadaukBook-Regular.ttf --unicodes=1022,fe00


svg_stack --direction=h myanmar-dotted-before.svg right-arrow.svg myanmar-dotted-after.svg > myanmar-dotted.svg


## 1. Kinzi

> Note: Noto Sans Myanmar does not implement the `rphf` feature for
> unknown reasons.

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-before.svg --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,103a,1039,25cc

svg_stack --direction=h myanmar-kinzi-ra-before.svg right-arrow.svg myanmar-kinzi-ra-after.svg > myanmar-kinzi-ra.svg


### Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-before.svg --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,103a,1039,25cc

svg_stack --direction=h myanmar-kinzi-nga-before.svg right-arrow.svg myanmar-kinzi-nga-after.svg > myanmar-kinzi-nga.svg


### Mon Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-before.svg --features=-rphf,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=105a,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-after.svg --features=+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=105a,103a,1039,25cc

svg_stack --direction=h myanmar-kinzi-monnga-before.svg right-arrow.svg myanmar-kinzi-monnga-after.svg > myanmar-kinzi-monnga.svg


## 2.4 Medial Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-before.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1017,200D,103C

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-after.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1017,103C

svg_stack --direction=h myanmar-medial-ra-before.svg right-arrow.svg myanmar-medial-ra-after.svg > myanmar-medial-ra.svg


## 3.1 locl

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-before.svg --features=+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,103d,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-after.svg --features=+psts --language=KSW --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,103d,103e

svg_stack --direction=h myanmar-locl-before.svg right-arrow.svg myanmar-locl-after.svg > myanmar-locl.svg


## 3.3 rphf

> Same as Kinzi


## 3.4 pref

> Note: Noto Sans Myanmar does not implement any pref features for
> unknown reasons. This example shows a basic-shaping feature to
> distinguish pref from the more stylistic applications of pres.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-before.svg --features=-pref  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=103c,103f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-after.svg --features=+pref  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=103f,103c

svg_stack --direction=h myanmar-pref-before.svg right-arrow.svg myanmar-pref-after.svg > myanmar-pref.svg


## 3.5 blwf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-before.svg --features=-blwf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,1039,100a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-after.svg --features=+blwf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100f,1039,100a

svg_stack --direction=h myanmar-blwf-before.svg right-arrow.svg myanmar-blwf-after.svg > myanmar-blwf.svg


## 3.6 pstf

> Note: Noto Sans Myanmar does not include a pstf feature for unknown
> reasons. This example shows an orthographically-selected variant, as
> referred to on
> https://r12a.github.io/scripts/myanmar/block#charTALL%20AA to
> distinguish pstf as an initial-shaping feature from the more
> stylistic applications of psts.
>
> Note: The example linked to above is used in the Microsoft
> script-development spec for Myanmar:
> https://docs.microsoft.com/en-us/typography/script-development/myanmar#feature-tag-pstf 
> but this usage is not well-attested in real-world Myanmar
> fonts. Instead, the "Aa"/"Tall Aa" distinction is made at the
> encoding level and is expected to happen during text
> entry. Consequently, this image has been removed from the
> script-specific shaping document. See issue #85 for the discussion.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-before.svg --features=-pstf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101d,102c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-after.svg --features=+pstf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101d,102b

svg_stack --direction=h myanmar-pstf-before.svg right-arrow.svg myanmar-pstf-after.svg > myanmar-pstf.svg


## 4 pres 

> Note: Noto Sans Myanmar does not implement this as a pres feature.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pres-before.svg --features=-pres,-blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100c,103c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pres-after.svg --features=+pres,+blws --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100c,103c

svg_stack --direction=h myanmar-pres-before.svg right-arrow.svg myanmar-pres-after.svg > myanmar-pres.svg


## 4 abvs

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvs-before.svg --features=-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100b,102d,1032

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvs-after.svg --features=+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100b,102d,1032

svg_stack --direction=h myanmar-abvs-before.svg right-arrow.svg myanmar-abvs-after.svg > myanmar-abvs.svg


## 4 blws

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blws-before.svg --features=-blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=aa6b,103c,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blws-after.svg --features=+blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=aa6b,103c,103e

svg_stack --direction=h myanmar-blws-before.svg right-arrow.svg myanmar-blws-after.svg > myanmar-blws.svg


## 4 psts

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-psts-before.svg --features=-blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100b,103b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-psts-after.svg --features=+blws  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=100b,103b

svg_stack --direction=h myanmar-psts-before.svg right-arrow.svg myanmar-psts-after.svg > myanmar-psts.svg


## 4 liga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-liga-before.svg --features=-liga,-blws,-blwf  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1016,103c,103d,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-liga-after.svg --features=+liga  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1016,103c,103d,103e

svg_stack --direction=h myanmar-liga-before.svg right-arrow.svg myanmar-liga-after.svg > myanmar-liga.svg


## 5 dist

> Note: Noto Sans Myanmar implements all distance adjustments in
> `kern`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dist-before.svg --features=-kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,102b,103a,100f,103c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dist-after.svg --features=+kern  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=101b,102b,103a,100f,103c

svg_stack --direction=h myanmar-dist-before.svg right-arrow.svg myanmar-dist-after.svg > myanmar-dist.svg


## 5 abvm

> Note: Noto Sans Myanmar implements this as `mark`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvm-before.svg --features=-mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,103a,1039,1008

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvm-after.svg --features=+mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1004,103a,1039,1008

svg_stack --direction=h myanmar-abvm-before.svg right-arrow.svg myanmar-abvm-after.svg > myanmar-abvm.svg


## 5 blwm

> Note: Noto Sans Myanmar implements this as `mark`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwm-before.svg --features=-mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1009,1039,101b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwm-after.svg --features=+mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1009,1039,101b

svg_stack --direction=h myanmar-blwm-before.svg right-arrow.svg myanmar-blwm-after.svg > myanmar-blwm.svg


## 5 mark

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mark-before.svg --features=-mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=107e,108d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mark-after.svg --features=+mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=107e,108d

svg_stack --direction=h myanmar-mark-before.svg right-arrow.svg myanmar-mark-after.svg > myanmar-mark.svg


## 5 mkmk

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mkmk-before.svg --features=-mkmk  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1000,1039,105d,105e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mkmk-after.svg --features=+mkmk  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf --unicodes=1000,1039,105d,105e

svg_stack --direction=h myanmar-mkmk-before.svg right-arrow.svg myanmar-mkmk-after.svg > myanmar-mkmk.svg





