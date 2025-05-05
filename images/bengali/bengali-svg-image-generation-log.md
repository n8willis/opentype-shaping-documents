# Commands used to generate the images in [opentype-shaping-bengali.md](../../opentype-shaping-bengali.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-Regular.ttf --unicodes=2192

cluster_styles = None

> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-decompose-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-decompose-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09c7,200c,25cc,09d7

svg_stack.py --direction=h bengali-matra-decompose-before.svg right-arrow.svg bengali-matra-decompose-after.svg > bengali-matra-decompose.svg

cluster_styles = [c0,dc,c0,arrow,c0,dc,z,dc,c1]


## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-yaphala-before.svg --features=-init,-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09af

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-yaphala-after.svg --features=-init,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09af

svg_stack.py --direction=h bengali-yaphala-before.svg right-arrow.svg bengali-yaphala-after.svg > bengali-yaphala.svg

cluster_styles = [dc,c0,c1,arrow,dc,c1]


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-nukt-before.svg --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a1,25cc,09bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-nukt-after.svg --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a1,09bc

svg_stack.py --direction=h bengali-nukt-before.svg right-arrow.svg bengali-nukt-after.svg > bengali-nukt.svg

cluster_styles = [c0,dc,c1,arrow,c0]


## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-kssa-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,09b7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-kssa-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,09b7

svg_stack.py --direction=h bengali-akhn-kssa-before.svg right-arrow.svg bengali-akhn-kssa-after.svg > bengali-akhn-kssa.svg

cluster_styles = [c0,dc,c1,c2,arrow,c0]


### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-jnya-before.svg --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099c,25cc,09cd,099e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-jnya-after.svg --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099c,09cd,099e

svg_stack.py --direction=h bengali-akhn-jnya-before.svg right-arrow.svg bengali-akhn-jnya-after.svg > bengali-akhn-jnya.svg

cluster_styles = [c0,dc,c1,c2,arrow,c0]


## 3.4 `rphf`

### Bengali

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-before.svg --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,25cc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-after.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc

svg_stack.py --direction=h bengali-rphf-before.svg right-arrow.svg bengali-rphf-after.svg > bengali-rphf.svg

cluster_styles = [c0,dc,c1,arrow,dc,c0]


### Assamese

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-as-before.svg --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,25cc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-as-after.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,25cc

svg_stack.py --direction=h bengali-rphf-as-before.svg right-arrow.svg bengali-rphf-as-after.svg > bengali-rphf-as.svg

cluster_styles = [c0,dc,c1,arrow,dc,c0]


## 3.7 `blwf`

### Raphala

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-raphala-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09b0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-raphala-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09b0

svg_stack.py --direction=h bengali-raphala-before.svg right-arrow.svg bengali-raphala-after.svg > bengali-raphala.svg

cluster_styles = [dc,c0,c1,arrow,dc,c0]


### Baphala

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-baphala-before.svg --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09ac

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-baphala-after.svg --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09ac

svg_stack.py --direction=h bengali-baphala-before.svg right-arrow.svg bengali-baphala-after.svg > bengali-baphala.svg

cluster_styles = [dc,c0,c1,arrow,dc,c0]


## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-half-ka-before.svg --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,0998

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-half-ka-after.svg --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,0998

svg_stack.py --direction=h bengali-half-ka-before.svg right-arrow.svg bengali-half-ka-after.svg > bengali-half-ka.svg

cluster_styles = [c0,dc,c1,c2,arrow,c0,c2]


## 3.10 `pstf`

> Same as 2.7

## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-vatu-before.svg --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,09b0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-vatu-after.svg --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,09b0

svg_stack.py --direction=h bengali-vatu-before.svg right-arrow.svg bengali-vatu-after.svg > bengali-vatu.svg

cluster_styles = [c0,dc,c1,c2,arrow,c0]


## 3.12 `cjct`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-cjct-before.svg --features=-init,-cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09aa,25cc,09cd,09a4,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-cjct-after.svg --features=-init,+cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09aa,09cd,09a4,25cc

svg_stack.py --direction=h bengali-cjct-before.svg right-arrow.svg bengali-cjct-after.svg > bengali-cjct.svg

cluster_styles = [c0,dc,c1,c2,dc,arrow,c0,dc]


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-position-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09c8,09b8,09cd,09ae,099a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-position-after.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b8,09cd,09ae,099a,09c8

svg_stack.py --direction=h bengali-matra-position-before.svg right-arrow.svg bengali-matra-position-after.svg > bengali-matra-position.svg

cluster_styles = [c0,dc,c1,c2,arrow,c1,c0,c2]


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-reph-position-before.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,25cc,09a1,09cd,09a1,09cd,0996,09c1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-reph-position-after.svg --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,09a1,09cd,09a1,09cd,0996,09c1

svg_stack.py --direction=h bengali-reph-position-before.svg right-arrow.svg bengali-reph-position-after.svg > bengali-reph-position.svg

cluster_styles = [c0,c1,dc,c2,c3,c4,arrow,c0,c1,c2,c3]


## 5 `init`

> ?? Maybe there's a headline-using second character that would be
> better here....

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-init-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0999,09c7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-init-after.svg --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0999,09c7

svg_stack.py --direction=h bengali-init-before.svg right-arrow.svg bengali-init-after.svg > bengali-init.svg

cluster_styles = [c0,c1,arrow,c0,c1]


## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-pres-before.svg --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099f,09bf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-pres-after.svg --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099f,09bf

svg_stack.py --direction=h bengali-pres-before.svg right-arrow.svg bengali-pres-after.svg > bengali-pres.svg

cluster_styles = [c0,c1,arrow,c0]


## 5 `abvs`

> Note that Noto Bengali implements this feature in a pres lookup for
> unknown reasons.

> No more!

hb-view --font-size=110 --margin=2,25,2,16 --output-file=bengali-abvs-before.svg --features=-init,-abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc,09c0,0981

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvs-after.svg --features=-init,+abvs --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc,09c0,0981

svg_stack.py --direction=h bengali-abvs-before.svg right-arrow.svg bengali-abvs-after.svg > bengali-abvs.svg

cluster_styles = [c0,c1,dc,c2,c3,arrow,c0,c1,dc,c2,c3]


# 5 `blws`

> Note that Noto Bengali implements this feature in a pres lookup for
> unknown reasons.

> This now seems to require disablng -cjct and -blws, but -pres is no
> longer involved.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blws-before.svg --features=-init,-blws,-cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099d,09cd,09ac

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blws-after.svg --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099d,09cd,09ac

svg_stack.py --direction=h bengali-blws-before.svg right-arrow.svg bengali-blws-after.svg > bengali-blws.svg

cluster_styles = [c0,c1,arrow,c0]


## 5 `psts`

> Note that Noto Bengali implements this feature in a pres lookup for
> unknown reasons.

> No more!

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-psts-before.svg --features=-init,-psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a0,09c0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-psts-after.svg --features=-init,+psts --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a0,09c0

svg_stack.py --direction=h bengali-psts-before.svg right-arrow.svg bengali-psts-after.svg > bengali-psts.svg

cluster_styles = [c0,c1,arrow,c0,c1]


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-haln-before.svg --features=-init,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099b,09bc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-haln-after.svg --features=-init,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099b,09bc,09cd

svg_stack.py --direction=h bengali-haln-before.svg right-arrow.svg bengali-haln-after.svg > bengali-haln.svg

cluster_styles = [c0,c1,c2,arrow,c0,c1,c2]


## 6 `abvm`

> ????

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvm-before.svg --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0994,0981

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvm-after.svg --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0994,0981

svg_stack.py --direction=h bengali-abvm-before.svg right-arrow.svg bengali-abvm-after.svg > bengali-abvm.svg

cluster_styles = [c0,c1,arrow,c0,c1]


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blwm-after.svg --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09ad,09c2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blwm-before.svg --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09ad,09c2

svg_stack.py --direction=h bengali-blwm-before.svg right-arrow.svg bengali-blwm-after.svg > bengali-blwm.svg

cluster_styles = [c0,c1,arrow,c0,c1]

