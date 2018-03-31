# Images #

This directory includes a separate subdirectory for each script,
containing the images included in the relevant script-shaping document.

Also included in each directory is a log file containing the exact
commands used to generate the images.

Glyph images are generated using the `hb-view` utility from Harfbuzz
and the `montage` utility from ImageMagick. The commands were run on a
Linux-based system but, apart from minor differences in the file-path
to the font file specified, should be completely reproducible on other
operating systems.

The font files used must be publicly and freely available, open-source
fonts. By default, the Noto fonts from Google are the starting point.

The image file names follow a simple, but important, pattern:
	_script_-_featureillustrated_.png
	
Intermediary images copy the pattern but append _-before_ or _-after_
when the before-or-after state of an applied OpenType feature, or some
other suffix as appropriate.

If you are suggesting an update to an image, please utilize the same
commands and general syntax. If you are suggesting adding a new image,
please also follow the file-name pattern. Patches to the image-generation log for
each script are appreciated, in order to keep the log up-to-date.

  - Indic
      - [Devanagari](devanagari/devanagari-image-generation-log.md)
      - [Bengali](bengali/bengali-image-generation-log.md)
      - [Gujarati](gujarati/gujarati-image-generation-log.md)
      - [Gurmukhi](gurmukhi/gurmukhi-image-generation-log.md)
      - [Kannada](kannada/kannada-image-generation-log.md)
      - [Malayalam](malayalam/malayalam-image-generation-log.md)
      - [Oriya](oriya/oriya-image-generation-log.md)
      - [Tamil](tamil/tamil-image-generation-log.md)
      - [Telugu](telugu/telugu-image-generation-log.md)
      - [Sinhala](sinhala/sinhala-image-generation-log.md)
  - Arabic
      - [Arabic](arabic/arabic-image-generation-log.md)
      - [Syriac](syriac/syriac-image-generation-log.md)
      - [N'Ko](nko/nko-image-generation-log.md)
      - [Mongolian](mongolian/mongolian-image-generation-log.md)
  - Hangul
      - [Hangul](hangul/hangul-image-generation-log.md)
