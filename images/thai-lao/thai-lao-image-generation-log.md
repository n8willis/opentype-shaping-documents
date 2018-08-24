# Commands used to generate the images in [opentype-shaping-thai-lao.md](../../opentype-shaping-thai-lao.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/opentype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192

## 1.1 `ccmp`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-ccmp-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4a,0e4d

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-ccmp-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4a,0e4d

montage thai-ccmp-before.png right-arrow.png thai-ccmp-after.png -geometry +0+0 -background transparent thai-ccmp.png

## 1.2 Decomposition

## 1.2 Am sign decomposition

## 1.2 Am sign decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-am-decomposition-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=25cc,0eb3

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-am-decomposition-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=25cc,0ecd,25cc,0eb2

montage lao-am-decomposition-before.png right-arrow.png lao-am-decomposition-after.png -geometry +0+0 -background transparent lao-am-decomposition.png

## 4 `kern`

## 4 `kern`

hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-kern-before.png --features=-kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=0ec1,0e9a

 hb-view --font-size=110 --margin=2,16,2,16 --output-file=lao-kern-after.png --features=+kern --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf --unicodes=0ec1,0e9a

montage lao-kern-before.png right-arrow.png lao-kern-after.png -geometry +0+0 -background transparent lao-kern.png

## 4 `mark`

## 4 `mark`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mark-before.png --features=-mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=0e0e,25cc,0e38

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mark-after.png --features=+mark --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=0e0e,0e38

montage thai-mark-before.png right-arrow.png thai-mark-after.png -geometry +0+0 -background transparent thai-mark.png


## 4 `mkmk`

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mkmk-before.png --features=-mkmk --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e31,0e48

hb-view --font-size=110 --margin=16,16,2,16 --output-file=thai-mkmk-after.png --features=+mkmk --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e31,0e48

montage thai-mkmk-before.png right-arrow.png thai-mkmk-after.png -geometry +0+0 -background transparent thai-mkmk.png


## PUA 1 - Sara Am decomposition

hb-view --font-size=110 --margin=2,16,2,16 --output-file=thai-am-decomposition-before.png --features=-ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e33

hb-view --font-size=110 --margin=2,16,2,16 --output-file=thai-am-decomposition-after.png --features=+ccmp --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf --unicodes=25cc,0e4d,25cc,0e32

montage thai-am-decomposition-before.png right-arrow.png thai-am-decomposition-after.png -geometry +0+0 -background transparent thai-am-decomposition.png
























