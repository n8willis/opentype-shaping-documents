# Commands used to generate the images in [opentype-shaping-myanmar.md](../../opentype-shaping-myanmar.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## Terminology

### Variation Selector

#### No VS

> Note: SIL Padauk 3.x implements the dotted-form feature, but not
> using Variation Selectors, for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-before.png --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1022

#### VS dotted form

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dotted-after.png --features=+psts --preserve-default-ignorables --language=KHT --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1022,fe00


montage myanmar-dotted-before.png right-arrow.png myanmar-dotted-after.png -geometry +0+0 -background transparent myanmar-dotted.png


## 1. Kinzi

> Note: Noto Sans Myanmar does not implement the `rphf` feature for
> unknown reasons.

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-before.png --features=-rphf,-abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101b,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-ra-after.png --features=+rphf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101b,103a,1039,25cc

montage myanmar-kinzi-ra-before.png right-arrow.png myanmar-kinzi-ra-after.png -geometry +0+0 -background transparent myanmar-kinzi-ra.png


### Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-before.png --features=-rphf,-abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1004,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-nga-after.png --features=+rphf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1004,103a,1039,25cc

montage myanmar-kinzi-nga-before.png right-arrow.png myanmar-kinzi-nga-after.png -geometry +0+0 -background transparent myanmar-kinzi-nga.png


### Mon Nga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-before.png --features=-rphf,-abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=105a,200c,103a,1039,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-kinzi-monnga-after.png --features=+rphf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=105a,103a,1039,25cc

montage myanmar-kinzi-monnga-before.png right-arrow.png myanmar-kinzi-monnga-after.png -geometry +0+0 -background transparent myanmar-kinzi-monnga.png


## 2.4 Medial Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-before.png --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1017,200D,103C

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-medial-ra-after.png --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1017,103C

montage myanmar-medial-ra-before.png right-arrow.png myanmar-medial-ra-after.png -geometry +0+0 -background transparent myanmar-medial-ra.png


## 3.1 locl

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-before.png --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100f,103d,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-locl-after.png --features=+psts --language=KSW --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100f,103d,103e

montage myanmar-locl-before.png right-arrow.png myanmar-locl-after.png -geometry +0+0 -background transparent myanmar-locl.png


## 3.3 rphf

> Same as Kinzi


## 3.4 pref

> Note: Noto Sans Myanmar does not implement any pref features for
> unknown reasons. This example shows a basic-shaping feature to
> distinguish pref from the more stylistic applications of pres.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-before.png --features=-pref  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=103c,103f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pref-after.png --features=+pref  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=103f,103c

montage myanmar-pref-before.png right-arrow.png myanmar-pref-after.png -geometry +0+0 -background transparent myanmar-pref.png


## 3.5 blwf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-before.png --features=-blwf  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100f,1039,100a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwf-after.png --features=+blwf  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100f,1039,100a

montage myanmar-blwf-before.png right-arrow.png myanmar-blwf-after.png -geometry +0+0 -background transparent myanmar-blwf.png


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

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-before.png --features=-pstf  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101d,102c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pstf-after.png --features=+pstf  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101d,102b

montage myanmar-pstf-before.png right-arrow.png myanmar-pstf-after.png -geometry +0+0 -background transparent myanmar-pstf.png


## 4 pres 

> Note: Noto Sans Myanmar does not implement this as a pres feature.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pres-before.png --features=-pres,-blws --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100c,103c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-pres-after.png --features=+pres,+blws --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100c,103c

montage myanmar-pres-before.png right-arrow.png myanmar-pres-after.png -geometry +0+0 -background transparent myanmar-pres.png


## 4 abvs

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvs-before.png --features=-abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100b,102d,1032

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvs-after.png --features=+abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100b,102d,1032

montage myanmar-abvs-before.png right-arrow.png myanmar-abvs-after.png -geometry +0+0 -background transparent myanmar-abvs.png


## 4 blws

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blws-before.png --features=-blws  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=aa6b,103c,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blws-after.png --features=+blws  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=aa6b,103c,103e

montage myanmar-blws-before.png right-arrow.png myanmar-blws-after.png -geometry +0+0 -background transparent myanmar-blws.png


## 4 psts

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-psts-before.png --features=-blws  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100b,103b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-psts-after.png --features=+blws  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=100b,103b

montage myanmar-psts-before.png right-arrow.png myanmar-psts-after.png -geometry +0+0 -background transparent myanmar-psts.png


## 4 liga

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-liga-before.png --features=-liga,-blws,-blwf  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1016,103c,103d,103e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-liga-after.png --features=+liga  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1016,103c,103d,103e

montage myanmar-liga-before.png right-arrow.png myanmar-liga-after.png -geometry +0+0 -background transparent myanmar-liga.png


## 5 dist

> Note: Noto Sans Myanmar implements all distance adjustments in
> `kern`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dist-before.png --features=-kern  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101b,102b,103a,100f,103c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-dist-after.png --features=+kern  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=101b,102b,103a,100f,103c

montage myanmar-dist-before.png right-arrow.png myanmar-dist-after.png -geometry +0+0 -background transparent myanmar-dist.png


## 5 abvm

> Note: Noto Sans Myanmar implements this as `mark`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvm-before.png --features=-mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1004,103a,1039,1008

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-abvm-after.png --features=+mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1004,103a,1039,1008

montage myanmar-abvm-before.png right-arrow.png myanmar-abvm-after.png -geometry +0+0 -background transparent myanmar-abvm.png


## 5 blwm

> Note: Noto Sans Myanmar implements this as `mark`.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwm-before.png --features=-mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1009,1039,101b

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-blwm-after.png --features=+mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1009,1039,101b

montage myanmar-blwm-before.png right-arrow.png myanmar-blwm-after.png -geometry +0+0 -background transparent myanmar-blwm.png


## 5 mark

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mark-before.png --features=-mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=107e,108d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mark-after.png --features=+mark  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=107e,108d

montage myanmar-mark-before.png right-arrow.png myanmar-mark-after.png -geometry +0+0 -background transparent myanmar-mark.png


## 5 mkmk

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mkmk-before.png --features=-mkmk  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1000,1039,105d,105e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=myanmar-mkmk-after.png --features=+mkmk  --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/Noto_Serif_Myanmar/NotoSerifMyanmar-Regular.ttf --unicodes=1000,1039,105d,105e

montage myanmar-mkmk-before.png right-arrow.png myanmar-mkmk-after.png -geometry +0+0 -background transparent myanmar-mkmk.png





