```{include} /_global.md
```

# OpenType shaping documents #

Sponsored by [YesLogic](https://yeslogic.com/) 

_<aside>Thanks also to the developers of HarfBuzz and AllSorts, plus many other font engineers and text-encoding experts for their generosity of time and insightful contributions.</aside>_

:::{admonition} &#127366; &#127344; &#127361; &#127357; &#127352; &#127357; &#127350;
:class: caution
These documents are an active WORK IN PROGRESS.

NONE of the documents you currently see here are complete
nor are they suitable for reference. PLEASE do not use
them as a guide or as a general information source.

As long as this warning text remains visible, the above 
holds true. 
:::


These documents are meant to provide a functional specification for
text shaping. The expectation is that an implementer of this
specification will be using fonts in the OpenType font format applied
to input text that complies with Unicode.

Because application software and end-user documents may utilize
non-OpenType fonts and non-Unicode text (in particular, when older
fonts or documents are encountered), these documents also provide
functional information that a shaping engine may use to implement a
reasonable best-effort attempt at producing useful output in the most
common of such scenarios.


## Shapers

The shaping behavior described here can be roughly divided into five
categories.

All non-complex scripts follow the same
[default](opentype-shaping-default.md) shaping model.


The _Indic Model_ is shared by ten individual scripts. These scripts
follow the same overall approach to shaping, described in the [Indic
general](opentype-shaping-indic-general.md) document, but each script
incorporates script-specific details, which are more fully described
in its own document:

  - [Devanagari](opentype-shaping-devanagari.md)
  - [Bengali](opentype-shaping-bengali.md)
  - [Gujarati](opentype-shaping-gujarati.md)
  - [Gurmukhi](opentype-shaping-gurmukhi.md)
  - [Kannada](opentype-shaping-kannada.md)
  - [Malayalam](opentype-shaping-malayalam.md)
  - [Oriya](opentype-shaping-oriya.md)
  - [Tamil](opentype-shaping-tamil.md)
  - [Telugu](opentype-shaping-telugu.md)
  - [Sinhala](opentype-shaping-sinhala.md)


The _Arabic Model_ is shared by four individual scripts. These scripts
follow the same overall approach to shaping, described in the [Arabic
general](opentype-shaping-arabic-general.md) document, but each script
incorporates script-specific details, which are more fully described
in its own document:

  - [Arabic](opentype-shaping-arabic.md)
  - [N'Ko](opentype-shaping-nko.md)
  - [Syriac](opentype-shaping-syriac.md)
  - [Mongolian](opentype-shaping-mongolian.md)


Five of the remaining scripts each use a distinct, script-specific
model, with two others (Thai and Lao) sharing enough details to be
handled by a common shaper:

  - [Hangul](opentype-shaping-hangul.md)
  - [Hebrew](opentype-shaping-hebrew.md)
  - [Khmer](opentype-shaping-khmer.md)
  - [Thai and Lao](opentype-shaping-thai-lao.md)
  - [Tibetan](opentype-shaping-tibetan.md)
  - [Myanmar](opentype-shaping-myanmar.md)
  

Finally, the Universal Shaping Engine (<abbr title="Universal Shaping
Engine">USE</abbr>) model is designed to shape all
complex scripts that are not handled by a dedicated
script-specific shaping model in the lists above:

  - [Universal Shaping Engine (<abbr>USE</abbr>)](opentype-shaping-use.md)


In addition, these documents describe the handling of emoji
sequences. Although emoji sequences do not constitute a separate
shaping model, handling emoji sequences can incorporate many of the
same shaping mechanisms and shaping engine implementations may be
expected to handle them:

  - [Emoji](opentype-shaping-emoji.md)
  

Shaping is just one part of the overall text-handling process. These
documents assume that other components in the software stack will be
responsible for details such as handling higher-level markup, layout,
font matching and loading, rasterization, and so on. Most importantly,
these documents assume that the input text has already been segmented
into text runs that consist of a single language, script, font, and
all other markup considerations (such as size or color, for example).

Within those assumptions, the shaping of a particular text run should
be consistent, regardless of whether the higher-level processes
involve a document, user-interface element, network stream, or any
other context for displaying text.


## Normalization

However, these documents also include a description of text
[normalization](opentype-shaping-normalization.md) in the OpenType
shaping context, which differs from Unicode normalization in several
respects. Shaping engine implementations may differ as to whether the
shaping engine itself is responsible for handling normalization or
whether normalization is handled by another component
in the stack. 


## Additional information

Various practical [notes](notes/index.md) about this document set and
the details of its scope, limitations, and quirks are also provided.

Some [errata](errata.md) about the "upstream" specifications and
reference documents are noted separately. 

In its final form, this repository will hold documentation describing
the shaping behavior used for layout of OpenType text. In particular,
it will focus on complex scripts.

In addition to the primary, per-script documents, implementers and
other interested readers are encouraged to check the
[character tables](character-tables/index.md) for correctness and to
examine the [image-generation logs](https://github.com/n8willis/opentype-shaping-documents/images/README.md) to identify
issues seen in the inline images.


## Feedback

Interested readers, font developers, and shaping-engine implementers
are encouraged to provide feedback, ask questions, and propose
improvements to any part of these documents. Shaping is the concern of
software developers and readers across the world, and all are welcome
to participate in recording and clarifying what is required to produce
the best and most accurate text output possible, both now and in the
future.

See the upstream git repository at
[github.com/n8willis/opentype-shaping-documents](https://github.com/n8willis/opentype-shaping-documents)
to raise issues, ask questions, or add comments.


## References

These documents cite the following informative references:

1. The Microsoft [Script development
   specifications](https://docs.microsoft.com/en-us/typography/script-development/standard),
   which document the behaviors expected for OpenType Layout fonts and
   provide guidance &amp; examples for type designers. OpenType is a
   registered trademark of Microsoft Corporation. 
2. Related portions of the Microsoft OpenType specification, such as the
   [OpenType Layout tag
   registry](https://docs.microsoft.com/en-us/typography/opentype/spec/ttoreg)
   and [OpenType Layout common table
   formats](https://docs.microsoft.com/en-us/typography/opentype/spec/chapter2),
   which list and define feature tags, script &amp; language tags, and
   other internals of compliant OpenType font binaries. OpenType is a
   registered trademark of Microsoft Corporation. 
3. The [HarfBuzz](https://github.com/harfbuzz/harfbuzz) project, which
   includes a free-software/open-source implementation of OpenType
   Layout shaping with full source code and documentation. 
4. The [AllSorts](https://github.com/yeslogic/allsorts) project, which
   includes a free-software/open-source implementation of OpenType
   Layout shaping with full source code and documentation.
5. The [Unicode
   Standard](http://www.unicode.org/standard/standard.html) and
   related Unicode Consortium projects such as the [Unicode Character
   Database](http://www.unicode.org/reports/tr44/), which defines
   Unicode code points and formal character properties used in
   shaping. Unicode and the Unicode Logo are registered trademarks of
   Unicode, Inc. in the United States and other countries.
6. The YesLogic [text corpus](https://github.com/yeslogic/corpus),
   which includes real-world text data for several Indic scripts,
   scraped from Wikipedia, Reddit, and multiple online news
   sources. This data is used to test shaping in AllSorts and Prince.
7. Known but unofficial information about other shaping-engine
   projects. Primarily this includes tests and reproducible issues
   found via [HarfBuzz](https://github.com/harfbuzz/harfbuzz), because
   HarfBuzz intentionally aims to produce results that will 100% match
   the output of Microsoft Uniscribe (not counting cases where
   Uniscribe's output is known to be incorrect, of course).
   > Note: occasionally, tests or issues documenting the behavior of
   > Apple CoreText are also included, but CoreText compatibility is
   > not an explicit goal for HarfBuzz.
   

---
Version {{ env.config.version }}, release {{ env.config.release }};
built {sub-ref}`today`.
