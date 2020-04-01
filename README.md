# OpenType shaping documents #

> ## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#127366; &#127344; &#127361; &#127357; &#127352; &#127357; &#127350; ##
>
> This repository is an active WORK IN PROGRESS.
>
> NONE of the documents you currently see here are complete
> nor are they suitable for reference. PLEASE do not use
> them as a guide or as a general information source.
>
> As long as this warning text remains visible, the above 
> holds true. 

At present, we are seeking comments and bugfixes on the Indic-script,
Arabic-like, Hangul, Hebrew, Thai/Lao, Tibetan, Khmer, Myanmar,
default, and USE documents. Interested readers and contributors can
begin at the

  - [Indic General](opentype-shaping-indic-general.md) 
    - (Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam,
      Oriya, Tamil, Telugu, Sinhala) 
  - [Arabic General](opentype-shaping-arabic-general.md)
    - (Arabic, N'Ko, Syriac, Mongolian)
  - [Hangul](opentype-shaping-hangul.md)
  - [Hebrew](opentype-shaping-hebrew.md)
  - [Khmer](opentype-shaping-khmer.md)
  - [Thai and Lao](opentype-shaping-thai-lao.md)
  - [Tibetan](opentype-shaping-tibetan.md)
  - [Myanmar](opentype-shaping-myanmar.md)
  - [Universal Shaping Engine (USE)](opentype-shaping-use.md)
    - All complex scripts that are not handled by a dedicated
      script-specific shaping model
  - [Default](opentype-shaping-default.md)
    - All non-complex scripts
  
shaping documents and are encouraged to submit their feedback
on the text or images of any of the linked scripts.

In its final form, this repository will hold documentation describing
the shaping behavior used for layout of OpenType text. In particular,
it will focus on complex scripts.

These documents draw from the following existing resources:

1. The Microsoft [Script development
   specifications](https://docs.microsoft.com/en-us/typography/script-development/standard),
   which document the behaviors expected for OpenType Layout fonts and
   provide guidance &amp; examples for type designers.
2. Related portions of the OpenType specification, such as the
   [OpenType Layout tag
   registry](https://docs.microsoft.com/en-us/typography/opentype/spec/ttoreg)
   and [OpenType Layout common table
   formats](https://docs.microsoft.com/en-us/typography/opentype/spec/chapter2),
   which list and define feature tags, script &amp; language tags, and
   other internals of compliant OpenType font binaries.
3. The [HarfBuzz](https://github.com/harfbuzz/harfbuzz) project, which
   includes a free-software/open-source implementation of OpenType
   Layout shaping with full source code and documentation. 
4. The [Allsorts](https://github.com/yeslogic/allsorts) project, which
   includes a free-software/open-source implementation of OpenType
   Layout shaping with full source code and documentation.
5. The [Unicode
   Standard](http://www.unicode.org/standard/standard.html) and
   related Unicode Consortium projects such as the [Unicode Character
   Database](http://www.unicode.org/reports/tr44/), which defines
   Unicode code points and formal character properties used in
   shaping.
6. The YesLogic [text corpus](https://github.com/yeslogic/corpus),
   which includes real-world text data for several Indic scripts,
   scraped from Wikipedia, Reddit, and multiple online news
   sources. This data is used to test shaping in Allsorts and Price.
7. Known but unofficial information about other shaping-engine
   projects. Primarily this includes tests and reproducible issues
   found via [HarfBuzz](https://github.com/harfbuzz/harfbuzz), because
   HarfBuzz intentionally aims to produce results that will 100% match
   the output of Microsoft Uniscribe.
   > Note: occasionally, tests or issues documenting the behavior of
   > Apple CoreText are also included, but CoreText compatibility is
   > not an explicit goal for HarfBuzz.
   
