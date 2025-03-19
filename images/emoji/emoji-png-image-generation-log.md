# Commands used to generate the images in [opentype-shaping-emoji.md](../../opentype-shaping-emoji.md)

## Arrow general

hb-view --font-size=110 --output-file=right-arrow.png --background=FFFFFF00 --margin=0,0,0,0 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-R.ttf --unicodes=2192


## Invisibles general

> Two options for VS15 and VS16 are included.
>
> Adobe Source Emoji includes non-color glyphs for both codepoints that
> offer a degree of visual communication to prevent confusion in the 
> sequence illustrations, but they are not immediately associated with
> the codepoint itself, like Gentium Plus's are.

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=text-pres-selector.png --font-funcs=ot --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=fe0e

hb-view --font-size=110 --margin=2,16,2,16 --features="ss06" --shapers=ot --preserve-default-ignorables --output-file=vs15.png --background=FFFFFF00 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-R.ttf --unicodes=fe0e

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=emoji-pres-selector.png --font-funcs=ot --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=fe0f

hb-view --font-size=110 --margin=2,16,2,16 --features="ss06" --shapers=ot --preserve-default-ignorables --output-file=vs16.png --background=FFFFFF00 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-R.ttf --unicodes=fe0f


> Gentium Plus's ZWJ and ZWNJ are visually preferrable:
hb-view --font-size=110 --margin=2,16,2,16 --features="ss06" --shapers=ot --preserve-default-ignorables --output-file=zwj.png --background=FFFFFF00 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-R.ttf --unicodes=200d

hb-view --font-size=110 --margin=2,16,2,16 --features="ss06" --shapers=ot --preserve-default-ignorables --output-file=zwnj.png --background=FFFFFF00 /usr/share/fonts/truetype/gentiumplus/GentiumPlus-R.ttf --unicodes=200c


## Human beings general

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fallback-boy.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f466

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fallback-girl.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f467

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fallback-man.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fallback-woman.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fallback-generalperson.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f9d1


## Presentation sequences

> Codepoints used are based on defaults in https://www.unicode.org/emoji/charts-14.0/text-style.html

> Invisibles:
montage vs15.png text-pres-selector.png -geometry +0+0 -background transparent -tile 2x1 text-presentation.png

montage vs16.png emoji-pres-selector.png -geometry +0+0 -background transparent -tile 2x1 emoji-presentation.png


> Default text-presentation: U+26A0, warning arrow:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=default-text-before.png --background=FFFFFF00 ./Noto\ Emoji\ BW-via-GoogleFonts/static/NotoEmoji-Regular.ttf --unicodes=26a0

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=default-text-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=26a0

montage default-text-before.png emoji-pres-selector.png right-arrow.png default-text-after.png -geometry +0+0 -background transparent -tile 4x1 emoji-pres-sequence.png


> Default emoji-presentation: U+231B, hourglass:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=default-emoji-before.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=231b

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=default-emoji-after.png --background=FFFFFF00 ./Noto\ Emoji\ BW-via-GoogleFonts/static/NotoEmoji-Regular.ttf --unicodes=231b

montage default-emoji-before.png text-pres-selector.png right-arrow.png default-emoji-after.png -geometry +0+0 -background transparent -tile 4x1 text-pres-sequence.png



## Modifier sequences

> Adobe Source Emoji for invisibles:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-2.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f3fb

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-3.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f3fc

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-4.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f3fd

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-5.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f3fe

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-6.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f3ff


> NotoColorEmoji squares for fallback skin-tone-squares:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=skintone-fallback-2.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3fb

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=skintone-fallback-3.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3fc

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=skintone-fallback-4.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3fd

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=skintone-fallback-5.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3fe

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=skintone-fallback-6.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3ff


> Symbola for text-mode fallback squares:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-2-text-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf --unicodes=1f3fb

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-3-text-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf --unicodes=1f3fc

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-4-text-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf --unicodes=1f3fd

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-5-text-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf --unicodes=1f3fe

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=skintone-6-text-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf --unicodes=1f3ff


> Fitzpatrick scale:
montage skintone-2.png skintone-fallback-2.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-2.png

montage skintone-3.png skintone-fallback-3.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-3.png

montage skintone-4.png skintone-fallback-4.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-4.png

montage skintone-5.png skintone-fallback-5.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-5.png

montage skintone-6.png skintone-fallback-6.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-6.png


> Fitzpatrick scale text fallback:
> (currently unused)
montage skintone-2.png skintone-2-text-fallback.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-2-text-fallback.png

montage skintone-3.png skintone-3-text-fallback.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-3-text-fallback.png

montage skintone-4.png skintone-4-text-fallback.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-4-text-fallback.png

ontage skintone-5.png skintone-5-text-fallback.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-5-text-fallback.png

montage skintone-6.png skintone-6-text-fallback.png -geometry +0+0 -background transparent -tile 2x1 fitzpatrick-6-text-fallback.png


> Sequence:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=modifier-before.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f44b

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=modifier-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f44b,1f3fd

montage modifier-before.png skintone-4.png right-arrow.png modifier-after.png -geometry +0+0 -background transparent -tile 4x1 modifier-sequence.png

montage modifier-before.png skintone-4.png right-arrow.png modifier-before.png skintone-fallback-4.png -geometry +0+0 -background transparent -tile 5x1 modifier-sequence-fallback.png


## Regional Indicator flag sequences

> UN chosen for maximum acheivable internationality

> Sequence
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --output-file=regional-flag-un-before.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=1f1fa,1f1f3

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=regional-flag-un-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f1fa,1f1f3

montage regional-flag-un-before.png right-arrow.png regional-flag-un-after.png -geometry +0+0 -background transparent regional-indicator-flag-sequence-un.png

> Fallbacks

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=regional-flag-un-fallback.png --background=FFFFFF00 ./Noto\ Emoji\ BW-via-GoogleFonts/static/NotoEmoji-Regular.ttf --unicodes=1f1fa,1f1f3

montage regional-flag-un-before.png right-arrow.png regional-flag-un-fallback.png -geometry +0+0 -background transparent regional-indicator-flag-sequence-un-fallback.png



## Tag flag sequences

> From https://unicode.org/reports/tr51/#valid-emoji-tag-sequences
>
> Wales chosen to be most distinctive example KNOWN to be widely implemented


> Tag pseudo-glyphs

> LastResort. This crops in, non-precisely, on the "tag" symbol itself:
hb-view --font-size=110 --margin=-42,-28,-44,-28 --preserve-default-ignorables --output-file=tag-isolate.png --background=FFFFFF00 ./unicode/Last-Resort/LastResort-Regular.ttf --unicodes=e007f

> Margin-adjusted versions:
hb-view --font-size=110 --margin=-20,-28,-48,-28 --preserve-default-ignorables --output-file=tag-isolate-high.png --background=FFFFFF00 ./unicode/Last-Resort/LastResort-Regular.ttf --unicodes=e007f

hb-view --font-size=110 --margin=-44,-28,-24,-28 --preserve-default-ignorables --output-file=tag-isolate-low.png --background=FFFFFF00 ./unicode/Last-Resort/LastResort-Regular.ttf --unicodes=e007f


> DejaVu empty dotted square, U+2B1A:
hb-view --font-size=110 --margin=-16,2,2,2 --preserve-default-ignorables --output-file=dotted-square.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=2b1a


> Letters and "end" components:
hb-view --font-size=40 --margin=16,2,2,2 --preserve-default-ignorables --output-file=g-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=0067

hb-view --font-size=40 --margin=16,2,2,2 --preserve-default-ignorables --output-file=b-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=0062

hb-view --font-size=40 --margin=16,2,2,2 --preserve-default-ignorables --output-file=w-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=0077

hb-view --font-size=40 --margin=16,2,2,2 --preserve-default-ignorables --output-file=l-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=006c

hb-view --font-size=40 --margin=16,2,2,2 --preserve-default-ignorables --output-file=s-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=0073

hb-view --font-size=32 --margin=2,2,16,2 --preserve-default-ignorables --output-file=end-isolate.png --background=FFFFFF00 /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf --unicodes=0045,004e,0044


> Composite tags:

composite -gravity north tag-isolate-high.png dotted-square.png blank-tag-high.png

composite -gravity south tag-isolate-low.png dotted-square.png blank-tag-low.png

composite -gravity north g-isolate.png blank-tag-low.png tag-g.png

composite -gravity north b-isolate.png blank-tag-low.png tag-b.png

composite -gravity north w-isolate.png blank-tag-low.png tag-w.png

composite -gravity north l-isolate.png blank-tag-low.png tag-l.png

composite -gravity north s-isolate.png blank-tag-low.png tag-s.png

composite -gravity south end-isolate.png blank-tag-high.png tag-end.png


> Completed sequence:

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=tag-flag-black.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3f4

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=tag-flag-wales-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3f4,e0067,e0062,e0077,e006c,e0073,e007f

montage tag-flag-black.png tag-g.png tag-b.png tag-w.png tag-l.png tag-s.png tag-end.png -geometry +0+0 -background transparent -tile 7x1 tag-flag-wales-before.png

montage tag-flag-wales-before.png right-arrow.png tag-flag-wales-after.png -geometry +0+0 -background transparent tag-flag-sequence-wales.png



## Keycap sequences

> Noto Sans Symbols has a visual CEK:
hb-view --font-size=110 --margin=2,64,2,64 --preserve-default-ignorables --output-file=keycap-cek.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf --unicodes=20e3


> Sequence:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=keycap-before.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf --unicodes=0034

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=keycap-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=0034,20e3

> Something off here; the -gravity and -geometry switches are *not* working as expected....
montage keycap-before.png keycap-cek.png right-arrow.png keycap-after.png -geometry +0+0 -background transparent -tile 4x1 keycap-sequence.png



## ZWJ sequences

### ZWJ hair sequences

> Hairstyles:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hair-red.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f9b0

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hair-curly.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f9b1

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hair-bald.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f9b2

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hair-white.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f9b3


> Sequence:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=woman-white-hair.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F469,200d,1f9b3

montage fallback-woman.png zwj.png hair-white.png right-arrow.png woman-white-hair.png -geometry +0+0 -background transparent -tile 5x1 hairstyle-sequence.png



### ZWJ gendered person sequences

> Gender signs, input (text-presentation style):
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendersign-female.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=2640

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendersign-male.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=2642

> Gender signs, output fallback (emoji-presentation style):
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendersign-female-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=2640

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendersign-male-fallback.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=2642


> Sequence:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendered-person-before.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F3c4

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=gendered-person-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F3c4,200d,2640,fe0f

montage gendered-person-before.png zwj.png gendersign-female.png emoji-pres-selector.png right-arrow.png gendered-person-after.png -geometry +0+0 -background transparent -tile 6x1 gendered-person-sequence.png


### ZWJ multi-person group sequences

>
> Couple with heart:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=heart.png --background=FFFFFF00 ./AdobeSourceEmoji/SourceEmoji-BnW.otf --unicodes=2764

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-man-heart-man-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,200d,2764,fe0f,200d,1f468

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-man-skintone-2-heart-man-skintone-2-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,1f3fb,200d,2764,fe0f,200d,1f468,1f3fb

> Sequence:
montage fallback-man.png zwj.png heart.png emoji-pres-selector.png zwj.png fallback-man.png right-arrow.png multi-person-man-heart-man-after.png -geometry +0+0 -background transparent -tile 8x1 multi-person-heart-sequence.png

montage fallback-man.png skintone-2.png zwj.png heart.png emoji-pres-selector.png zwj.png fallback-man.png skintone-2.png right-arrow.png multi-person-man-skintone-2-heart-man-skintone-2-after.png -geometry +0+0 -background transparent -tile 10x1 multi-person-heart-skintone-sequence.png


>
> Couple kiss:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=kiss-mark.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f48b

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-kiss-sequence-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,200d,2764,fe0f,200d,1f48b,200d,1f468

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-kiss-sequence-skintone-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,1f3ff,200d,2764,fe0f,200d,1f48b,200d,1f468,1f3fd

> Sequence:
montage fallback-woman.png zwj.png heart.png emoji-pres-selector.png zwj.png kiss-mark.png zwj.png fallback-man.png right-arrow.png multi-person-kiss-sequence-after.png -geometry +0+0 -background transparent -tile 10x1 multi-person-kiss-sequence.png

montage fallback-woman.png skintone-6.png zwj.png heart.png emoji-pres-selector.png zwj.png kiss-mark.png zwj.png fallback-man.png skintone-4.png right-arrow.png multi-person-kiss-sequence-skintone-after.png -geometry +0+0 -background transparent -tile 12x1 multi-person-kiss-skintone-sequence.png


>
> Couple holding hands:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=handshake.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f91d

> Noto Color Emoji does not support this sequence, perhaps because it expects
> fallback to `U+1F46D` to occur, e.g. at the keyboard/UI level....
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-holding-hands-sequence-woman-woman-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f46d

> This modifier sequence IS supported in Noto Color Emoji
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-holding-hands-sequence-woman-woman-skintone-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,1f3fc,200d,1f91d,200d,1f469,1f3fe

> Sequence:
montage fallback-woman.png zwj.png handshake.png zwj.png fallback-woman.png right-arrow.png multi-person-holding-hands-sequence-woman-woman-after.png -geometry +0+0 -background transparent -tile 7x1 multi-person-holding-hands-sequence.png

montage fallback-woman.png skintone-3.png zwj.png handshake.png zwj.png fallback-woman.png skintone-5.png right-arrow.png multi-person-holding-hands-sequence-woman-woman-skintone-after.png -geometry +0+0 -background transparent -tile 9x1 multi-person-holding-hands-skintone-sequence.png


>
> Family:
>
> Noto Color Emoji supports "Man,ZWJ,Woman,ZWJ,_child_" but not "Woman,ZWJ,Man,ZWJ,_child_".
>
> Noto Color Emoji supports "Woman,ZWJ,Woman,ZWJ,Girl,ZWJ,Boy" but not "Woman,ZWJ,Woman,ZWJ,Boy,ZWJ,Girl".
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-family-man-boy-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,200d,1f466

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-family-man-girl-girl-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,200d,1f467,200d,1f467

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-family-man-woman-girl-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,200d,1f469,200d,1f467

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-family-woman-woman-girl-boy-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,200d,1f469,200d,1f467,200d,1f466

> Sequence:
montage fallback-man.png zwj.png fallback-boy.png right-arrow.png multi-person-family-man-boy-after.png -geometry +0+0 -background transparent -tile 5x1 multi-person-family-man-boy-sequence.png

montage fallback-man.png zwj.png fallback-girl.png zwj.png fallback-girl.png right-arrow.png multi-person-family-man-girl-girl-after.png -geometry +0+0 -background transparent -tile 7x1 multi-person-family-man-girl-girl-sequence.png

montage fallback-man.png zwj.png fallback-woman.png zwj.png fallback-girl.png right-arrow.png multi-person-family-man-woman-girl-after.png -geometry +0+0 -background transparent -tile 7x1 multi-person-family-man-woman-girl-sequence.png

montage fallback-woman.png zwj.png fallback-woman.png zwj.png fallback-girl.png zwj.png fallback-boy.png right-arrow.png multi-person-family-woman-woman-girl-boy-after.png -geometry +0+0 -background transparent -tile 9x1 multi-person-family-woman-woman-girl-boy-sequence.png

>
> Noto Color Emoji does not seem to support skin-tone modifiers for family sequences,
> at least in the current release on my system.
>
>


>
> Shaking hands:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hand-left.png --background=FFFFFF00 ./blobmoji/Blobmoji.ttf --unicodes=1faf1

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=hand-right.png --background=FFFFFF00 ./blobmoji/Blobmoji.ttf --unicodes=1faf2

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=multi-person-shaking-hands-after.png --background=FFFFFF00 ./blobmoji/Blobmoji.ttf --unicodes=1faf1,1f3fd,200d,1faf2,1f3ff

> Sequence:
montage hand-left.png skintone-4.png zwj.png hand-right.png skintone-6.png right-arrow.png multi-person-handshake-after.png -geometry +0+0 -background transparent -tile 7x1 multi-person-shaking-hands-sequence.png



### ZWJ role sequences

> Firefighter (emoji-pres-by-default):
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=firetruck.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F692

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=role-firefighter-man-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,200d,1F692

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=role-firefighter-man-skintone-6-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f468,1f3ff,200d,1F692

montage fallback-man.png zwj.png firetruck.png right-arrow.png role-firefighter-man-after.png -geometry +0+0 -background transparent -tile 5x1 role-sequence-firefighter.png

montage fallback-man.png skintone-6.png zwj.png firetruck.png right-arrow.png role-firefighter-man-skintone-6-after.png -geometry +0+0 -background transparent -tile 6x1 role-sequence-firefighter-skintone-6.png



> Pilot (non-emoji-pres-by-default)
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=airplane.png --background=FFFFFF00 ./Noto\ Emoji\ BW-via-GoogleFonts/static/NotoEmoji-Regular.ttf --unicodes=2708,fe0e

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=role-pilot-woman-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,200d,2708,fe0f

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=role-pilot-woman-skintone-2-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f469,1f3fb,200d,2708,fe0f

montage fallback-woman.png zwj.png airplane.png emoji-pres-selector.png right-arrow.png role-pilot-woman-after.png -geometry +0+0 -background transparent -tile 6x1 role-sequence-pilot.png

montage fallback-woman.png skintone-2.png zwj.png airplane.png emoji-pres-selector.png right-arrow.png role-pilot-woman-skintone-2-after.png -geometry +0+0 -background transparent -tile 7x1 role-sequence-pilot-skintone-2.png



### ZWJ color sequences

> Noto Color Emoji, "black cat" seems to be the only widely-implemented sequence:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=color-before.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F408

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=color-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1F408,200d,2b1b

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=color-black.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=2b1b

montage color-before.png zwj.png color-black.png right-arrow.png color-after.png -geometry +0+0 -background transparent -tile 5x1 color-sequence.png


### ZWJ directionality sequences

> These are not widely implemented, and possible not implemented at all in open-source fonts.
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=running.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f3c3

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=direction-rightward.png --background=FFFFFF00 ./Noto\ Emoji\ BW-via-GoogleFonts/static/NotoEmoji-Regular.ttf --unicodes=27a1

convert -flop running.png running-rightward.png

montage running.png zwj.png direction-rightward.png emoji-pres-selector.png right-arrow.png running-rightward.png -geometry +0+0 -background transparent -tile 6x1 zwj-directionality-sequence.png



### ZWJ additional sequences

> 13 on the named list. Heart-on-fire is clearly not just an overlay, and not a flag:
hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=fire.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=1f525

hb-view --font-size=110 --margin=2,16,2,16 --preserve-default-ignorables --font-funcs=ot --output-file=heart-on-fire-after.png --background=FFFFFF00 /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf --unicodes=2764,fe0f,200d,1f525

montage heart.png emoji-pres-selector.png zwj.png fire.png right-arrow.png heart-on-fire-after.png -geometry +0+0 -background transparent -tile 6x1 zwj-sequence-heart-on-fire.png


## Other sequences and ligatures

> For non-standard ligatures (banana split?)

> Adobe SourceEmoji has a "hand + zwj + heart -> i-love-you-hand" ligature:


>Other possiblities:
> https://blog.emojipedia.org/emoji-flags-explained/ (discusses flag options for vendors that don't require Unicode pre-/formal-approval)
> Noto monochromatic emoji details: https://blog.emojipedia.org/exploring-googles-new-black-and-blobby-emoji-font/
> Are Noto's "Emoji Kitchen" emoji (beginning with magic wand) just ligatures, or all they all "stickers"? https://blog.emojipedia.org/emoji-kitchen-beta-magics-back-the-blobs/
