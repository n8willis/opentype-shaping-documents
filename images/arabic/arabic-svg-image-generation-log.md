# Commands used to generate the images in [opentype-shaping-arabic.md](../../opentype-shaping-arabic.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.svg --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-Regular.ttf --unicodes=2192

## 2 `ccmp`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-ccmp-before.svg --features=-ccmp --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=067e

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-ccmp-after.svg --features=+ccmp --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=067e

svg_stack.py --direction=h arabic-ccmp-before.svg right-arrow.svg arabic-ccmp-after.svg > arabic-ccmp.svg



## 4.1 `locl`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-locl-before.svg --features=-locl --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=06f4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-locl-after.svg --features=+locl --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=06f4

svg_stack.py --direction=h arabic-locl-before.svg right-arrow.svg arabic-locl-after.svg > arabic-locl.svg


## 4.2 `isol`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-isol-before.svg --features=-isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0647

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-isol-after.svg --features=+isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0647

svg_stack.py --direction=h arabic-isol-before.svg right-arrow.svg arabic-isol-after.svg > arabic-isol.svg


## 4.3 `fina`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-fina-before.svg --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0626,200d,0628

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-fina-after.svg --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0626,0628

svg_stack.py --direction=h arabic-fina-before.svg right-arrow.svg arabic-fina-after.svg > arabic-fina.svg


## 4.6 `medi`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-medi-before.svg --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0626,200d,062e,200d,0637

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-medi-after.svg --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0626,062e,0637

svg_stack.py --direction=h arabic-medi-before.svg right-arrow.svg arabic-medi-after.svg > arabic-medi.svg


## 4.8 `init`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-init-before.svg --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=063a,200d,0626

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-init-after.svg --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=063a,0626

svg_stack.py --direction=h arabic-init-before.svg right-arrow.svg arabic-init-after.svg > arabic-init.svg


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-rlig-before.svg --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0623

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-rlig-after.svg --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0623

svg_stack.py --direction=h arabic-rlig-before.svg right-arrow.svg arabic-rlig-after.svg > arabic-rlig.svg


## 4.10 `rclt`

> None found.


## 4.11 `calt`

> Note: Noto Nastaliq Urdu implements this as a `rlig` lookup for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-calt-before.svg --features=-liga,-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=062d,0645

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-calt-after.svg --features=+liga,+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=062d,0645

svg_stack.py --direction=h arabic-calt-before.svg right-arrow.svg arabic-calt-after.svg > arabic-calt.svg


## 5.1 `liga`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-liga-before.svg --features=-liga,-fina,-medi,-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0627,0644,0644,0651,0670,06c1

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-liga-after.svg --features=+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0627,0644,0644,0651,0670,06c1

svg_stack.py --direction=h arabic-liga-before.svg right-arrow.svg arabic-liga-after.svg > arabic-liga.svg


## 5.2 `dlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-dlig-before.svg --features=-dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0644,0647

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-dlig-after.svg --features=+dlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0644,0647

svg_stack.py --direction=h arabic-dlig-before.svg right-arrow.svg arabic-dlig-after.svg > arabic-dlig.svg


## 5.3 `cswh`

> None found.


## 5.4 `mset`

> None found. Could be emulated with `mark`, however.


## 7.1 `curs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-curs-before.svg --features=-curs --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0642,0633,0645

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-curs-after.svg --features=+curs --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0642,0633,0645

svg_stack.py --direction=h arabic-curs-before.svg right-arrow.svg arabic-curs-after.svg > arabic-curs.svg


## 7.2 `dist` (not yet added to document)

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-dist-before.svg --features=-dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0628,062f,066e,062d

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-dist-after.svg --features=+dist --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0628,062f,066e,062d

svg_stack.py --direction=h arabic-dist-before.svg right-arrow.svg arabic-dist-after.svg > arabic-dist.svg


## 7.2 `kern`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-kern-before.svg --features=-kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0635,062f,0627

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-kern-after.svg --features=+kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0635,062f,0627

svg_stack.py --direction=h arabic-kern-before.svg right-arrow.svg arabic-kern-after.svg > arabic-kern.svg




## 7.3 `mark`

hb-view --font-size=110 --margin=2,32,2,32 --output-file=arabic-mark-before.svg --features=-mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0643,0653

hb-view --font-size=110 --margin=2,32,2,16 --output-file=arabic-mark-after.svg --features=+mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0643,0653

svg_stack.py --direction=h arabic-mark-before.svg right-arrow.svg arabic-mark-after.svg > arabic-mark.svg























