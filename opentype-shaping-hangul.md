# Hangul script shaping in OpenType #

This document the general shaping procedure shared by all 
Hangul script styles, and defines the common pieces that style-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Jamo type](#jamo-type)
	  - [Composing behavior](#composing-behavior)
	  - [Character tables](#character-tables)
  - [The `<hang>` shaping model](#the-arab-shaping-model)
      - [1. Compound character composition and decomposition](#1-compound-character-composition-and-decomposition)
      - [2. Computing letter joining states](#2-computing-letter-joining-states)



## General information ##

The Hangul script is used to write Korean. It may also be referred to
as the Choseongul script or Jeongum script, and is in use in both
North Korea and South Korea as well as within China. It may also be
used to write the Cia-Cia language.

Hangul syllables are formed from individual alphabetic letters that
are arranged into square blocks using pre-defined patterns. The
syllables themselves are monospaced in a run of text, using interword
spacing and punctuation.

Korean text may, in practice, incorporate Chinese characters ("Hanja")
in addition to Hangul. Hanja characters are not affected by the
shaping rules for Hangul.

Modern Korean text is typically written (and, therefore, rendered)
left to right. Classical and older texts, however, may be written
vertically, top to bottom.


## Terminology ##

OpenType shaping uuses a standard set of terms for elements of the
Hangul script. The terms used colloquially in any particular language
or country may vary, however, potentially causing confusion.

**Jamo** characters are the fundamental letters from which syllable
blocks are composed.  There are three classes of jamo:

  - **L**eading consonants (choseong)
  - **V**owels (jungseong)
  - **T**railing consonants (jongseong)
  
Modern Korean features 19 leading consonants, 21 vowels, and 27
trailing consonants.

Old Korean featured a considerable number of additional jamo, which
are also defined in Unicode.  Many of these Old Korean jamo are
compound forms that concatenate two or three basic jamo. 
  
A **syllable** is formed by arranging a sequence of jamo into its
appropriate square-block form. The horizontal and vertical positioning
of each jamo in the block depends on the content of the syllable. The
exact shape and proportions of each jamo will also vary with its final
position in the block. 

Valid syllables must be either of the form <**LV**> or of the form
<**LVT**>. That is, each syllable must begin with one leading
consonant, include one vowel in the second position, and may or may
not end with one trailing consonant. 

All possible syllables for Modern Korean are defined in the Hangul
Syllables block of Unicode. A sequence of individual jamo codepoints
that corresponds to a valid Modern Korean syllable can therefore be
**composed** into a syllable codepoint. 

Sequences of codepoints that involve Old Korean jamo cannot be
composed into syllable codepoints and are handled separately by the
shaping engine.

Two tone marks are common in Old Korean, the **single-dot bangjeom**
and the **double-dot bangjeom**. Both bangjeom marks are rendered to
the left of the syllable to which they are applied.



## Glyph classification ##



### Jamo type ###


### Composing behavior ###
