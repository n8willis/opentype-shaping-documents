# Commands used to generate the images in [opentype-shaping-bengali.md](/[opentype-shaping-bengali.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


> Note: always use `--features=-init` in examples where the `init`
> feature itself is not being explained.


## 2.2 Matra decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-decompose-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09cc

hb-view --font-size=110 --margin=2,16,2,16
--output-file=bengali-matra-decompose-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09c7,200c,25cc,09d7

montage bengali-matra-decompose-before.png right-arrow.png bengali-matra-decompose-after.png -geometry +0+0 -background transparent bengali-matra-decompose.png


## 2.7 Post-base consonants

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-yaphala-before.png --features=-init,-pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09af

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-yaphala-after.png --features=-init,+pstf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09af

montage bengali-yaphala-before.png right-arrow.png bengali-yaphala-after.png -geometry +0+0 -background transparent bengali-yaphala.png


## 3.2 `nukt`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-nukt-before.png --features=-init,-nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a1,25cc,09bc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-nukt-after.png --features=-init,+nukt --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a1,09bc

montage bengali-nukt-before.png right-arrow.png bengali-nukt-after.png -geometry +0+0 -background transparent bengali-nukt.png


## 3.3 `akhn`

### KSsa

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-kssa-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,09b7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-kssa-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,09b7

montage bengali-akhn-kssa-before.png right-arrow.png bengali-akhn-kssa-after.png -geometry +0+0 -background transparent bengali-akhn-kssa.png

### JNya

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-jnya-before.png --features=-init,-akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099c,25cc,09cd,099e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-akhn-jnya-after.png --features=-init,+akhn --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099c,09cd,099e

montage bengali-akhn-jnya-before.png right-arrow.png bengali-akhn-jnya-after.png -geometry +0+0 -background transparent bengali-akhn-jnya.png


## 3.4 `rphf`

### Bengali

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-before.png --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,25cc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-after.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc

montage bengali-rphf-before.png right-arrow.png bengali-rphf-after.png -geometry +0+0 -background transparent bengali-rphf.png


### Assamese

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-as-before.png --features=-init,-rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,25cc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-rphf-as-after.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,25cc

montage bengali-rphf-as-before.png right-arrow.png bengali-rphf-as-after.png -geometry +0+0 -background transparent bengali-rphf-as.png

## 3.7 `blwf`

### Raphala

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-raphala-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09b0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-raphala-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09b0

montage bengali-raphala-before.png right-arrow.png bengali-raphala-after.png -geometry +0+0 -background transparent bengali-raphala.png


### Baphala

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-baphala-before.png --features=-init,-blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09ac

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-baphala-after.png --features=-init,+blwf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=25cc,09cd,09ac

montage bengali-baphala-before.png right-arrow.png bengali-baphala-after.png -geometry +0+0 -background transparent bengali-baphala.png

## 3.9 `half`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-half-ka-before.png --features=-init,-half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,0998

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-half-ka-after.png --features=-init,+half --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,0998

montage bengali-half-ka-before.png right-arrow.png bengali-half-ka-after.png -geometry +0+0 -background transparent bengali-half-ka.png

## 3.10 `pstf`

> Same as 2.7

## 3.11 `vatu`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-vatu-before.png --features=-init,-vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,25cc,09cd,09b0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-vatu-after.png --features=-init,+vatu --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0995,09cd,09b0

montage bengali-vatu-before.png right-arrow.png bengali-vatu-after.png -geometry +0+0 -background transparent bengali-vatu.png


## 3.12 `cjct`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-cjct-before.png --features=-init,-cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09aa,25cc,09cd,09a4,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-cjct-after.png --features=-init,+cjct --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09aa,09cd,09a4,25cc

montage bengali-cjct-before.png right-arrow.png bengali-cjct-after.png -geometry +0+0 -background transparent bengali-cjct.png


## 4.2 Pre-base matras

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-position-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09c8,09b8,09cd,09ae,099a

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-matra-position-after.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b8,09cd,09ae,099a,09c8

montage bengali-matra-position-before.png right-arrow.png bengali-matra-position-after.png -geometry +0+0 -background transparent bengali-matra-position.png


## 4.3 Reph position

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-reph-position-before.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,25cc,09a1,09cd,09a1,09cd,0996,09c1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-reph-position-after.png --features=-init,+rphf --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09f0,09cd,09a1,09cd,09a1,09cd,0996,09c1

montage bengali-reph-position-before.png right-arrow.png bengali-reph-position-after.png -geometry +0+0 -background transparent bengali-reph-position.png

## 5 `init`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-init-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0999,09c7

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-init-after.png --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0999,09c7

montage bengali-init-before.png right-arrow.png bengali-init-after.png -geometry +0+0 -background transparent bengali-init.png

## 5 `pres`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-pres-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099f,09bf

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-pres-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099f,09bf

montage bengali-pres-before.png right-arrow.png bengali-pres-after.png -geometry +0+0 -background transparent bengali-pres.png


## 5 `abvs`

> Note that Noto Bengali implements this feature in a pres lookup for
unknown reasons.

hb-view --font-size=110 --margin=2,25,2,16 --output-file=bengali-abvs-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc,09c0,0981

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvs-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09b0,09cd,25cc,09c0,0981

montage bengali-abvs-before.png right-arrow.png bengali-abvs-after.png -geometry +0+0 -background transparent bengali-abvs.png


# 5 `blws`

> Note that Noto Bengali implements this feature in a pres lookup for
unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blws-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099d,09cd,09ac

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blws-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099d,09cd,09ac

montage bengali-blws-before.png right-arrow.png bengali-blws-after.png -geometry +0+0 -background transparent bengali-blws.png


## 5 `psts`

> Note that Noto Bengali implements this feature in a pres lookup for
unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-psts-before.png --features=-init,-pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a0,09c0

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-psts-after.png --features=-init,+pres --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09a0,09c0

montage bengali-psts-before.png right-arrow.png bengali-psts-after.png -geometry +0+0 -background transparent bengali-psts.png


## 5 `haln`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-haln-before.png --features=-init,-haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099b,09bc,09cd

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-haln-after.png --features=-init,+haln --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=099b,09bc,09cd

montage bengali-haln-before.png right-arrow.png bengali-haln-after.png -geometry +0+0 -background transparent bengali-haln.png


## 6 `abvm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvm-before.png --features=-init,-abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0994,0981

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-abvm-after.png --features=-init,+abvm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=0994,0981

montage bengali-abvm-before.png right-arrow.png bengali-abvm-after.png -geometry +0+0 -background transparent bengali-abvm.png


## 6 `blwm`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blwm-after.png --features=-init,+blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09ad,09c2

hb-view --font-size=110 --margin=2,16,2,16 --output-file=bengali-blwm-before.png --features=-init,-blwm --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf --unicodes=09ad,09c2

montage bengali-blwm-before.png right-arrow.png bengali-blwm-after.png -geometry +0+0 -background transparent bengali-blwm.png





