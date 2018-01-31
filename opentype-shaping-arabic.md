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

Ijam

Tashkil

Hamza

Kashida

Maddah

Annotation marks


## Glyph classification ##

### Joining properties ###

Because Arabic is a joining (or cursive) script, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters.

Arabic characters are assigned a `JOINING_TYPE` property that indicates
how they join to adjacent characters. There are six possible values:

  - `JOINING_TYPE_LEFT` indicates that a character joins with
    the subsequent character, but does not join with the preceding
    character. 
	
  - `JOINING_TYPE_RIGHT` indicates that a character joins with the
    preceding character, but does not join with the subsequent character.	

  - `JOINING_TYPE_NON_JOINING` indicates that a character does not
    join with the preceding or the subsequent character.
	
  - `JOINING_TYPE_DUAL` indicates that a character joins with the
    preceding character and joins with the subsequent character.
	
  - `JOINING_TYPE_TRANSPARENT` indicates that the character does not
    join with adjacent characters _and_ that the character must be
    skipped over when the shaping engine is evaluating the joining
    positions in a sequence of characters. Diacritical marks are
    frequently assigned this property.
	
  - `JOINING_TYPE_JOIN_CAUSING` indicates that
  


The isolated form of a letter will frequently be designated
`JOINING_TYPE_NON_JOINING`, indicating that it does not join with
adjacent characters. Diacritic marks will frequently be designated
`JOINING_TYPE_TRANSPARENT`, which indicates that the mark glyph must
be skipped over when the shaping engine is evaluating joining behavior
of a sequence.

_RIGHT
_LEFT
_DUAL
_JOIN_CAUSING
_NON_JOINING
_TRANSPARENT

Arabic letters are also assigned to a `JOINING_GROUP` that indicates
which fundamental character they behave like, with regard to joining
behavior. Each of the basic letters in the Arabic block tends to
belong to its own `JOINING_GROUP`, while letters from the supplemental and
extended blocks are usually assigned to the `JOINING_GROUP` that
corresponds to the character's base letter, with no diacritics.

For example, 



_ALEF
_YEH
_WAW
_BEH
_HAH
_REH
_SEEN
_SAD
_TAH
...


Features
`isol`
`fina`
`fin2`
`fin3`
`medi`
`med2`
`init`


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
