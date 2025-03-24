# Images #

This section includes a separate subdirectory for each script,
containing the images included in the relevant script-shaping document.

Also included in each directory is a log file containing the exact
commands used to generate the images.

PNG glyph images are generated using the `hb-view` utility from
Harfbuzz and the `montage` utility from ImageMagick. The commands were
run on a Linux-based system but, apart from minor differences in the
file-path to the font file specified, should be completely
reproducible on other operating systems.

SVG glyph images are generated using the `hb-view` utility from
Harfbuzz and the [`svg_stack`](https://github.com/astraw/svg_stack/)
Python utility. The commands were run on a Linux-based system but,
apart from minor differences in the file-path to the font file
specified, should be completely reproducible on other operating
systems.

Long-term, the PNG images will be replaced by SVG images &mdash;
although, at present, there are still some images that are generated
in PNG form (because kinks remain to be worked out in the SVG-image
alignment process and the corresponding CSS styling).

The font files used must be publicly and freely available, open-source
fonts. By default, the Noto fonts from Google are the starting point.

A list of the fonts used to generate the latest version of the images
is provided in the [example-fonts.txt](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/example-fonts.txt) file, with
URLs and SHA checksums for each file.

The image file names follow a simple, but important, pattern:

    _script_-_featureillustrated_.png
	
Intermediary images copy the pattern but append _-before_ or _-after_
when depicting the before-or-after state of an applied OpenType
feature, or some other suffix as appropriate.

If you are suggesting an update to an image, please utilize the same
commands and general syntax. If you are suggesting adding a new image,
please also follow the file-name pattern. Patches to the image-generation log for
each script are appreciated, in order to keep the log up-to-date.

  - Indic
      - [Devanagari](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/devanagari/devanagari-svg-image-generation-log.md)
      - [Bengali](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/bengali/bengali-svg-image-generation-log.md)
      - [Gujarati](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/gujarati/gujarati-svg-image-generation-log.md)
      - [Gurmukhi](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/gurmukhi/gurmukhi-svg-image-generation-log.md)
      - [Kannada](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/kannada/kannada-svg-image-generation-log.md)
      - [Malayalam](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/malayalam/malayalam-svg-image-generation-log.md)
      - [Oriya](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/oriya/oriya-svg-image-generation-log.md)
      - [Tamil](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/tamil/tamil-svg-image-generation-log.md)
      - [Telugu](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/telugu/telugu-svg-image-generation-log.md)
      - [Sinhala](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/sinhala/sinhala-svg-image-generation-log.md)
  - Brahmi-derived
	  - [Khmer](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/khmer/khmer-svg-image-generation-log.md)
	  - [Lao](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/thai-lao/thai-lao-svg-image-generation-log.md)
	  - [Myanmar](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/myanmar/myanmar-svg-image-generation-log.md)
	  - [Thai](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/thai-lao/thai-lao-svg-image-generation-log.md)
	  - [Tibetan](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/tibetan/tibetan-svg-image-generation-log.md)
  - Arabic
      - [Arabic](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/arabic/arabic-svg-image-generation-log.md)
      - [Syriac](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/syriac/syriac-svg-image-generation-log.md)
      - [N'Ko](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/nko/nko-svg-image-generation-log.md)
      - [Mongolian](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/mongolian/mongolian-svg-image-generation-log.md)
  - Hangul
      - [Hangul](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/hangul/hangul-svg-image-generation-log.md)
  - Hebrew
      - [Hebrew](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/hebrew/hebrew-svg-image-generation-log.md)
  - Emoji
      - [Emoji](https://github.com/n8willis/opentype-shaping-documents/blob/master/images/emoji/emoji-png-image-generation-log.md)
