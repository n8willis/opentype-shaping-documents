# CONTRIBUTING #

Everyone is welcome to contribute to these documents. On this page are
some resources and general advice for those wanting to participate.

## Information sources ##

Most of the information in these documents is drawn from the Microsoft
script-development spec pages
([https://docs.microsoft.com/en-us/typography/script-development/standard](https://docs.microsoft.com/en-us/typography/script-development/standard)
and following), the Unicode Standard
([http://www.unicode.org/standard/standard.html](http://www.unicode.org/standard/standard.html))
and Character Database
([http://www.unicode.org/ucd](http://www.unicode.org/ucd)), and the
source code for the HarfBuzz shaping engine ([https://github.com/harfbuzz/harfbuzz](https://github.com/harfbuzz/harfbuzz)).

You will likely also want to consult the specifications for OpenType,
TrueType, related font formats, and advice for type designers and fotn
engineers. A detailed list of those sources is maintained at
[fontspec.org](https://fontspec.org/), so we will point readers there
rather than duplicate it here.


## Filing issue reports ##

At the moment, we are using GitHub's issue tracker for bug reports,
pull requests, and discussions. That does mean that you will have to
have a GitHub account, but if you cannot create one, you can still
contact project participants via email or any other online forum if
you want.

It is perfectly acceptable to open an issue for discussion
purposes. However, if you open an issue than turns out to be better
suited for another project (e.g., the OpenType specification or a
particular font), do not be alarmed if your issue is referred
elsewhere. It's nothing personal.


## Style guide ##

See the [style guide](/style-guide.md) document for some detailed
advice on how to write additions or patches that will best match the
contents already here. The style of these documents is a bit unusual,
mostly because they attempt to bridge between several existing
specifications while also covering a wide range of writing systems, so
please be sure you read the style guide before writing any patches or
additions by pull-request.


## Images ##

Images illustrating shaping behavior are particularly valuable, so
there are some special considerations you should be aware of if you
wish to contribute an image or alter an existing image.

- We will only use free-software/open-source (FOSS) fonts in the
  images, so that the documents can be regenerated as-is by
  anyone. The _only_ exception to this fotn requirement is if there
  are _no_ FOSS fonts available that can display the illustration
  needed; in that case we will accept an image made with a
  freely-downloadable, publicly accessible font.
- All images must be raster images (not vectors) and must be generated
  with FOSS, command-line tools. This, also, is meant to guarantee
  that others will be able to generate the images and have
  pixel-identical results as much as possible.
- You must save the commands you used to generate the images and
  record them in a log file, and you must note the origin and filename
  of the font you used.
- If you must incorporate a work-around to display the illustration
  that you need (for example, if you need to show a non-printable code
  point like a Zero-Wdith Joiner), be sure to include a comment in
  your image-generation log.

See the image-generation logs in the `/images/` directory for examples
of the method to follow.


## Errata ##

The [Errata](/errata.md) document is different from the rest of the
documentation, because it is explicitly meant to record ambiguities
or unresolved problems in the various formal specifications needed
for OpenType shaping.

You can make a pull request against the errata.md file to request an
erratum be added. However, it is probably a good idea to always open
an issue to discuss the matter first.
