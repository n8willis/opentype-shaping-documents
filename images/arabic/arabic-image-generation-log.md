# Commands used to generate the images in [opentype-shaping-arabic.md](../../opentype-shaping-arabic.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 4.1 `locl`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-locl-before.png --features=-locl --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=06f4

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-locl-after.png --features=+locl --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=06f4

montage arabic-locl-before.png right-arrow.png arabic-locl-after.png -geometry +0+0 -background transparent arabic-locl.png


## 4.2 `isol`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-isol-before.png --features=-isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0647

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-isol-after.png --features=+isol --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0647

montage arabic-isol-before.png right-arrow.png arabic-isol-after.png -geometry +0+0 -background transparent arabic-isol.png


## 4.3 `fina`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-fina-before.png --features=-fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=25cc,0628

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-fina-after.png --features=+fina --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=25cc,0628

montage arabic-fina-before.png right-arrow.png arabic-fina-after.png -geometry +0+0 -background transparent arabic-fina.png


## 4.6 `medi`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-medi-before.png --features=-medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=25cc,062e,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-medi-after.png --features=+medi --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=25cc,062e,25cc

montage arabic-medi-before.png right-arrow.png arabic-medi-after.png -geometry +0+0 -background transparent arabic-medi.png


## 4.8 `init`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-init-before.png --features=-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=063a,25cc

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-init-after.png --features=+init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=063a,25cc

montage arabic-init-before.png right-arrow.png arabic-init-after.png -geometry +0+0 -background transparent arabic-init.png


## 4.9 `rlig`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-rlig-before.png --features=-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0623

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-rlig-after.png --features=+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf --unicodes=0644,0623

montage arabic-rlig-before.png right-arrow.png arabic-rlig-after.png -geometry +0+0 -background transparent arabic-rlig.png


## 4.10 `rclt`

> None found.


## 4.11 `calt`

> Note: Noto Nastaliq Urdu implements this as a `rlig` lookup for
> unknown reasons.

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-calt-before.png --features=-liga,-rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=062d,0645

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-calt-after.png --features=+liga,+rlig --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=062d,0645

montage arabic-calt-before.png right-arrow.png arabic-calt-after.png -geometry +0+0 -background transparent arabic-calt.png


## 5.1 `liga`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-liga-before.png --features=-liga,-fina,-medi,-init --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf --unicodes=0631,064a,0627,0644

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-liga-after.png --features=+liga --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf --unicodes=0631,064a,0627,0644

montage arabic-liga-before.png right-arrow.png arabic-liga-after.png -geometry +0+0 -background transparent arabic-liga.png


## 5.3 `cswh`

> None found.


## 5.4 `mset`

> None found. Could be emulated with `mark`, however.


## 7.1 `curs`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-curs-before.png --features=-curs --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0642,0633,0645

hb-view --font-size=110 --margin=2,16,2,16 --output-file=arabic-curs-after.png --features=+curs --language=urd --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0642,0633,0645

montage arabic-curs-before.png right-arrow.png arabic-curs-after.png -geometry +0+0 -background transparent arabic-curs.png


## 7.3 `mark`

hb-view --font-size=110 --margin=2,32,2,32 --output-file=arabic-mark-before.png --features=-mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0643,0653

hb-view --font-size=110 --margin=2,32,2,16 --output-file=arabic-mark-after.png --features=+mark  --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf --unicodes=0643,0653

montage arabic-mark-before.png right-arrow.png arabic-mark-after.png -geometry +0+0 -background transparent arabic-mark.png























