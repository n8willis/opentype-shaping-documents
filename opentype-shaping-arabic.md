# Arabic script shaping in OpenType ~

This document the general shaping procedure shared by all
Arabic script styles, and defines the common pieces that style-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Joining properties](#joining-properties)
	  - [Character tables](#character-tables)
  - [The `<arab>` shaping model](#the-arab-shaping-model)
  
  


## General information ##

The Arabic script encompasses multiple distinct styles, including Naskh,
Nataliq, and Kufi, that share a number of common features and rules,
but that differ considerably in final appearance. 

The Arabic script is used to write multiple languages, most commonly
Arabic, Persian, Urdu, Pashto, Kurdish, and Azerbaijani.

A shaping engine can support all styles of Arabic in a single shaping
model. In addition, several related scripts that follow similar rules
and conventions can be supported using the same model. These scripts
include N'Ko, Syriac, and Mongolian.

Arabic is a joining script that uses inter-word spaces, so each
codepoint in a text run may be substituted with one of several
contextual forms though corresponding to its position in a
word. Most, but not all, letter sequences join; shaping engines must
track which positions trigger joining behavior for each letter.

Arabic is written (and, therefore, rendered) from right to
left. Shaping engines must track the directionality of the text run
when scripts of different direction are mixed.

## Terminology ##

OpenType shaping uses a standard set of terms for elements of the
Arabic script. The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Base** glyph or character is the standard term for a Arabic
character that is capable of taking a diacritical mark. 

Most of the base characters in Arabic are **consonants**, but there
are several **vowel** base letters. 

Vowels that are not base characters are frequently omitted from the
text run entirely. Alternatively, such a vowel may appear as a
diacritical mark called a **ḥarakah**.

**Ijam** is the standard term for an above- or below-base dot that
distinguishes one consonant from another. Ijam are not considered
diacritics; they are integral to the consonant of which they are a part.

**Shadda** and **tashdid** are both standard terms for the "consonant
doubling" diacritical mark.

**Hamza** is the standard term for the glottal stop
semi-consonant. The hamza is not regarded as a full letter in most
languages, although it can appear as a stand-alone letter within
words. In some sequences, the hamza attaches to an adjacent letter;
when a hamza-supporting letter is not adjacent, however, the hamza can
appear on its own.

**Kashida** (or **tatweel**) is the term for a glyph inserted into a
sequence for the purpose of elongating the baseline stroke of a
letter. Unicode documents use the term "tatweel" most frequently,
while OpenType documents use the term "kashida" most
frequently. Kashidas are typically inserted in order to justify lines
of text. 


## Glyph classification ##

Because Arabic is a joining (or cursive) script, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters to determine the contextually correct form for display.

### Joining properties ###

Arabic characters are assigned a `JOINING_TYPE` property in the
Unicode standard that indicates how they join to adjacent
characters. There are six possible values: 

  - `JOINING_TYPE_LEFT` indicates that a character joins with
    the subsequent character, but does not join with the preceding
    character. 
	
  - `JOINING_TYPE_RIGHT` indicates that a character joins with the
    preceding character, but does not join with the subsequent character.	

  - `JOINING_TYPE_DUAL` indicates that a character joins with the
    preceding character and joins with the subsequent character.
	
  - `JOINING_TYPE_NON_JOINING` indicates that a character does not
    join with the preceding or with the subsequent character.
	
  - `JOINING_TYPE_TRANSPARENT` indicates that the character does not
    join with adjacent characters _and_ that the character must be
    skipped over when the shaping engine is evaluating the joining
    positions in a sequence of characters. When a
    `JOINING_TYPE_TRANSPARENT` character is encountered in a sequence,
    the `JOINING_TYPE` of the preceding character passes
    through. Diacritical marks are frequently assigned this property. 
	
  - `JOINING_TYPE_JOIN_CAUSING` indicates that the character forces
    the use of joining forms with the preceding and subsequent
    characters. Kashidas and the Zero Width Joiner (`U+200D`) are both
    `JOIN_CAUSING` characters.
  

Arabic letters are also assigned to a `JOINING_GROUP` that indicates
which fundamental character they behave like with regard to joining
behavior. Each of the basic letters in the Arabic block tends to
belong to its own `JOINING_GROUP`, while letters from the supplemental and
extended blocks are usually assigned to the `JOINING_GROUP` that
corresponds to the character's base letter, with no diacritics or ijam.

For example, the Persian letter "Peh" (`U+067E`) is visually
represented as the Arabic letter "Beh" (`U+0628`), but with two additional
below-base ijam. Consequently, "Peh" is assigned to the `BEH` `JOINING_GROUP`.


Diacritic classes: No more than one mark of each class on a base;
DIAC1 and DIAC2 are mutually exclusive:
<!--- From MS Uniscribe web docs --->

  - DIAC1 - above-base U+064B, U+064C, U+064E, U+064F, U+0652, U+0657, U+0658, U+06E1
  - DIAC2 - below-base U+064D, U+0650, U+0656
  - DIAC3 - seat shadda U+0651
  - DIAC4 - Qur'anic above-base U+0610 - U+0614, U+0659, U+06D6 - U+06DC, U+06DF, U+06E0, U+06E2, U+06E4, U+06E7, U+06E8, U+06EB, U+06EC
  - DIAC5 - Qur'anic below-base U+06E3, U+06EA, U+06ED
  - DIAC6 - superscript alef U+0670
  - DIAC7 - madda U+0653
  - DIAC8 - hamza <!--- MS site calls this madda !?! ---> U+0654, U+0655

Additional codepoints: "Dotted circle" (`U+25CC`), "ZWNJ" (`U+200C`),
"ZWJ" (`U+200D`), "LTR" (`U+200E`), "RTL" (`U+200F`).



## The `<arab>` shaping model ##

Decomposition

Mark reordering

GSUB::
Language-form features:

`isol` to get isolated forms
`fina` to get final forms
`fin2` Syriac special case
`fin3` Syriac special case #2
`medi` to get medial forms
`med2` Syriac special case
`init` to get initial forms

`rlig` substitutes mandatory ligatures

Typographic-form features:
`liga` substitutes optional, on-by-default ligatures
`dlig` substitutes optional, off-by-default ligatures
`cswh` substitutes contextual swash variants (eg, long-noon when X
        subsequent glyphs do not descend below the baseline)
`mset` performs mark positioning by substitution (`mark` is
preferred!)

GPOS:
`curs` to perform cursive positioning
`kern` to perform kerning
`mark` to position marks to bases
`mkmk` to position marks to marks


Character blocks:
Arabic
Arabic Supplement
Arabic Extended-A
Arabic Presentation Forms A amd B
Rumi Numeral Symbols
Arabic Mathematical Symbols
N'Ko
Syriac
Mongolian
