# Notes on Emoji font implementation #

This document notes details on how common Emoji fonts implement
sequence, modifier, varation-selection, text-presentation 
fallback, and other behavior, for the purposes of testing and
debugging.

Emoji fonts are deployed by vendors using a variety of different
image formats (including the `SVG `, `COLR`v0/`CPAL`,
`COLR`v1/`CPAL`, `glyf`, and `cff ` vector formats and the `CBDT`
and `sbix` raster formats), which can make it difficult to
characterize Emoji font behavior.

Similarly, Emoji font vendors have employed a variety of
different OpenType features to implement support for standard
sequences, modifier-based sequences, <abbr title="Zero-Width Joiner">ZWJ</abbr>-based sequences and
permutations.

See the [Emoji shaping document](../opentype-shaping-emoji.md)
for more details on the sequences and definitions involved.

## Format, features, and control-codepoint visiblity table ##

This table lists the image format, the <abbr title="Glyph Substitution table">GSUB</abbr> feature(s) used for
basic Emoji sequence support and <abbr title="Zero-Width Joiner">ZWJ</abbr>-based sequence support, and
whether or not the font includes a visible glyph for the
presentation selector codepoints (VS15, `U+FE0E`; VS16, `U+FE0F`)
and modifier codepoints (`U+1F3FB`..`U+1F3FF`).


| Font                   | publisher | image format | sequence formation feature | ZWJ sequence feature | visible presentation selector | visible modifier |
|:-----------------------|:----------|:-------------|:---------------------------|:---------------------|:------------------------------|:-----------------|
| Source Emoji           | Adobe     | cff          | ccmp                       | ccmp, salt           | YES                           | YES              |
| Blobmoji               | C1710     | CBDT         | ccmp                       | ccmp                 | no                            | YES              |
| Twemoji                | Twitter   | SVG          | liga                       | liga                 | no                            | YES              |
| Noto Color Emoji       | Google    | CBDT         | ccmp                       | ccmp                 | no                            | YES              |
| Noto Color Emoji       | Google    | COLRv1       | ccmp                       | ccmp                 | no                            | YES              |
| EmojiTwo Android       | EmojiTwo  | CBDT         | ccmp                       | ccmp                 | no                            | YES              |
| EmojiTwo Apple         | EmojiTwo  | sbix         | morx                       | morx                 | no                            | YES              |
| EmojiTwo SVG          | EmojiTwo  | SVG          | ccmp                       | ccmp                 | no                            | YES              |
| Openmoji               | HfG Gmünd | SVG          | liga                       | liga                 | no                            | YES              |
| FirefoxEmoji           | Mozilla   | COLRv0       | rlig                       | rlig                 | no                            | no               |
| Noto Emoji             | Google    | glyf         | ccmp                       | ccmp                 | no                            | YES              |
| Old Noto B&amp;W Emoji | Google    | glyf         | ccmp                       | ccmp                 | no                            | no               |
| JoyPixels              | JoyPixels | CBDT         | ccmp                       | ccmp                 | no                            | YES              |
| Apple Color Emoji      | Apple    | sbix         | morx                       | morx                 | no                            | YES              |
| Samsung Color Emoji    | Samsung  | CBDT         | ccmp                       | ccmp                 | no                            | YES              |
| Segoe UI Emoji         | Microsoft| COLRv0       | ccmp                       | ccmp                 | YES                           | YES              |


### Contributing additional data ###

Volunteers or implementers who wish to contribute data for additional
Emoji fonts may need to collecting the information themselves by
inspecting font binaries.

Options available include:

1. **FontTools / TTX**
   - Users can run `ttx -l somefontfilename.ttf` (or `.otf` or `.ttc`
     or `.otc`) to get a short list of the tables. The presence of `SVG `,
     `CBDT`, `sbix`, or `COLR` indicates that whichever one of those exists
     is the image format. _If_ none of the above are there but `glyf` or `CFF `
     or `CFF2` _is_ there, then whichever of those three exists is the
     image format (and means it's a black-and-white emoji font, which users
     would probably know beforehand anyway). If there's more than one of
     `SVG `, `CBDT`, `sbix`, or `COLR` present in the same font file, that
     would likely mean unknown behavior; comments on such cases are welcome.
   - Users can run the `layout-features.py somefontfilename.ttf`
     script (which can be found in the `/Snippets/` directory of the
     `FontTools` package source) and it will print out an indented
     list of the <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> features
     used. All that matters for the table above is what the script
     reports on the `Feature: ` line. For a typical emoji font there's
     probably only one feature -- but, if there are several, listing
     them is useful.

2. **allsorts / allsorts-tools**
   - Users can use the `dump` tool from the `allsorts-tools` package
     to run `allsorts dump somefilename.ttf` and get a list of tables plus
     other metadata; the tables are the first output. Same interpretation
     as above.
   - At the moment it sounds like there isn't a single-command option in
     allsorts to list <abbr title="Glyph Substitution table">GSUB</abbr>/<abbr title="Glyph Positioning table">GPOS</abbr> features. Corrections are welcome.

3. **GUI font editors**
   - Users can also open up the font file in a font editor and look at what
     it presents. 
   - FontForge:
     - In FontForge, go to Element -> Font Info in the menu to open the
       font-info dialog box. It will show the <abbr title="Glyph Substitution table">GSUB</abbr>/<abbr title="Glyph Positioning table">GPOS</abbr> lookups in the
       "Lookups" tab (left-hand side).
     - FontForge does _not_ just show a convenient list of all the tables.
       However, when users open the font file, the "Warnings" dialog box will
       report if it finds `SVG `, `CBDT`, `sbix`, or `COLR` tables.
       Unfortunately, it will only actually open the font for
       editing/inspection if it finds a `glyf`, `CFF `, or `CFF2` table
       (which a `COLR` font would have) or an `SVG ` table. So users can't
       use it to inspect the features of the other formats.

(Further instructions will be added to this list for other editors if volunteers
can contribute them)

For determining if there's a printable glyph for the selectors/modifiers:
1. **GUI font editors**
   - Users can open up the font in an editor and look at the slots for the
     Unicode codepoints for the presentation selectors (`U+FE0E` and `U+FE0F`)
     and the modifiers (`U+1F3FB` through `U+1F3FF`), if they exist (they might not).
2. **HarfBuzz**
   - Users can run the `hb-view` utility to output glyph contents for specific
     Unicode codepoints, but one might have to try a couple of options, depending
     on the image format. Run `hb-view --preserve-default-ignorables somefontfilename.ttf --unicodes=fe0e`
     to start (for `U+FE0E`). Users may also try adding the `--font-funcs=ot`
     and/or `--shapers=ot` flags to that command if it gives trouble. 
