# Commands used to generate the images in [opentype-shaping-oriya.md](../../opentype-shaping-oriya.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192




## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-decompose-before.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b4c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-decompose-after.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b47,25cc,0b57

svg_stack.py --direction=h oriya-matra-decompose-before.svg right-arrow.svg oriya-matra-decompose-after.svg > oriya-matra-decompose.svg


## 2.7 Below-base consonants

### Ra

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-ra-before.svg --features=-pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b30

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-ra-after.svg --features=+pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b30

svg_stack.py --direction=h oriya-blwf-ra-before.svg right-arrow.svg oriya-blwf-ra-after.svg > oriya-blwf-ra.svg


#### Duplicates for other subsections

cp oriya-blwf-ra.svg oriya-blwf-ra-1.svg

cluster_styles = [

cp oriya-blwf-ra.svg oriya-blwf-ra-2.svg

cluster_styles = [




## 2.7 Post-base consonants

### Ya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-ya-before.svg --features=-pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b2f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-ya-after.svg --features=+pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b2f

svg_stack.py --direction=h oriya-pstf-ya-before.svg right-arrow.svg oriya-pstf-ya-after.svg > oriya-pstf-ya.svg

### Yya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-yya-before.svg --features=-pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b5f

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pstf-yya-after.svg --features=+pstf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b5f

svg_stack.py --direction=h oriya-pstf-yya-before.svg right-arrow.svg oriya-pstf-yya-after.svg > oriya-pstf-yya.svg


#### Duplicates for other subsections

cp oriya-pstf-ya.svg oriya-pstf-ya-1.svg

cluster_styles = [


cp oriya-pstf-yya.svg oriya-pstf-yya-1.svg

cluster_styles = [


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-nukt-before.svg --features=-nukt --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b16,25cc,0b3c

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-nukt-after.svg --features=+nukt --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b16,0b3c

svg_stack.py --direction=h oriya-nukt-before.svg right-arrow.svg oriya-nukt-after.svg > oriya-nukt.svg


## 3.3 `akhn`

### KSsa

> Note: Noto Sans Oriya implements this in a `pres`+`blwf` combination
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-kssa-before.svg --features=-pres,-blwf,-akhn --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b15,0b4d,0b37

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-kssa-after.svg --features=+pres,+blwf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b15,0b4d,0b37

svg_stack.py --direction=h oriya-akhn-kssa-before.svg right-arrow.svg oriya-akhn-kssa-after.svg > oriya-akhn-kssa.svg

### JNya

> Note: Noto Sans Oriya implements this in a `blwf`+`cjct` combination
> for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-jnya-before.svg --features=-pres,-cjct,-blwf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b1c,0b4d,0b1e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-akhn-jnya-after.svg --features=+pres,+blwf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b1c,0b4d,0b1e

svg_stack.py --direction=h oriya-akhn-jnya-before.svg right-arrow.svg oriya-akhn-jnya-after.svg > oriya-akhn-jnya.svg


## 3.4 `rphf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-rphf-before.svg --features=-rphf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b30,0b4d,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-rphf-after.svg --features=+rphf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b30,0b4d,25cc

svg_stack.py --direction=h oriya-rphf-before.svg right-arrow.svg oriya-rphf-after.svg > oriya-rphf.svg


## 3.7 `blwf`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-before.svg --features=-blwf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b25

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwf-after.svg --features=+blwf --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=25cc,0b4d,0b25

svg_stack.py --direction=h oriya-blwf-before.svg right-arrow.svg oriya-blwf-after.svg > oriya-blwf.svg


## 3.9 `half`

> No examples found.

## 3.10 `pstf`

> Same as 2.7

## 3.12 `cjct`

> Not a perfect example....

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-cjct-before.svg --features=-pres --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-cjct-after.svg --features=+pres --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=

svg_stack.py --direction=h oriya-cjct-before.svg right-arrow.svg oriya-cjct-after.svg > oriya-cjct.svg


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-position-before.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b47,0b36,0b4d,0b24,0b4d,0b30,0b4d,0b2f,0b56

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-matra-position-after.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b36,0b4d,0b24,0b4d,0b30,0b4d,0b2f,0b48

svg_stack.py --direction=h oriya-matra-position-before.svg right-arrow.svg oriya-matra-position-after.svg > oriya-matra-position.svg


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-reph-position-before.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b30,0b4d,25cc,0b2a,0b4d,0b27,0b4d,0b30,0b4d,0b2f,0b3e,0b41

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-reph-position-after.svg --features= --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b30,0b4d,0b2a,0b4d,0b27,0b4d,0b30,0b4d,0b2f,0b3e,0b41

svg_stack.py --direction=h oriya-reph-position-before.svg right-arrow.svg oriya-reph-position-after.svg > oriya-reph-position.svg


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pres-before.svg --features=-pres --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-pres-after.svg --features=+pres --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2d

svg_stack.py --direction=h oriya-pres-before.svg right-arrow.svg oriya-pres-after.svg > oriya-pres.svg


## 5 `abvs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvs-before.svg --features=-abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b13,200d,0b01

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvs-after.svg --features=+abvs --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b13,200d,0b01

svg_stack.py --direction=h oriya-abvs-before.svg right-arrow.svg oriya-abvs-after.svg > oriya-abvs.svg


## 5 `blws`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blws-before.svg --features=-blws --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b28,0b4d,0b24,0b42

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blws-after.svg --features=+blws --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b28,0b4d,0b24,0b42

svg_stack.py --direction=h oriya-blws-before.svg right-arrow.svg oriya-blws-after.svg > oriya-blws.svg


## 5 `psts`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-psts-before.svg --features=-psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b23,0b4c,0b01

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-psts-after.svg --features=+psts --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b23,0b4c,0b01

svg_stack.py --direction=h oriya-psts-before.svg right-arrow.svg oriya-psts-after.svg > oriya-psts.svg


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-haln-before.svg --features=-haln,-blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b1d,0b4d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-haln-after.svg --features=+haln,+blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b1d,0b4d

svg_stack.py --direction=h oriya-haln-before.svg right-arrow.svg oriya-haln-after.svg > oriya-haln.svg


## 6 `dist`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-dist-before.svg --features=-dist --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b42,0b15

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-dist-after.svg --features=+dist --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b42,0b15

svg_stack.py --direction=h oriya-dist-before.svg right-arrow.svg oriya-dist-after.svg > oriya-dist.svg


## 6 `abvm`

> Note: Noto Serif Oriya implements this as `blwm` for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvm-before.svg --features=-blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b19,0b4d,0b18,0b48

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-abvm-after.svg --features=+abvm,+blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b19,0b4d,0b18,0b48

svg_stack.py --direction=h oriya-abvm-before.svg right-arrow.svg oriya-abvm-after.svg > oriya-abvm.svg


## 6 `blwm`

> Note: Noto Serif Oriya implements this as `abvm` for unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwm-before.svg --features=-abvm,-blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2b,0b44

hb-view --font-size=110 --margin=2,16,2,16 --output-file=oriya-blwm-after.svg --features=+blwm --background=FFFFFF00 /home/nate/SyncThing/fonts-external/temporary-and-testing/NotoSerifOriya-Regular.ttf --unicodes=0b2e,0b4d,0b2b,0b44

svg_stack.py --direction=h oriya-blwm-before.svg right-arrow.svg oriya-blwm-after.svg > oriya-blwm.svg

