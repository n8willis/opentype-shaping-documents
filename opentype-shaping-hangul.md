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
North Korea and South Korea as well as regions within China. It may
also be used to write the Cia-Cia language in Indonesia.

Hangul syllables are formed from individual alphabetic letters that
are arranged into square blocks using pre-defined patterns. The
syllables themselves are monospaced in a run of text, using interword
spacing and punctuation.

Korean text may, in practice, incorporate Chinese characters ("Hanja")
in addition to Hangul. Hanja characters are not affected by the
shaping model for Hangul.

Modern Korean text is typically written (and, therefore, rendered)
left to right. Classical and older texts, however, may be written
vertically, top to bottom.


## Terminology ##

OpenType shaping uuses a standard set of terms for elements of the
Hangul script. The terms used colloquially in any particular language
or country may vary, however, potentially causing confusion.

**Jamo** characters are the fundamental letters from which syllable
blocks are constructed.  There are three classes of jamo:

  - **L**eading consonants (choseong)
  - **V**owels (jungseong)
  - **T**railing consonants (jongseong)

Most, but not all, of the basic consonant letters can appear either in
leading or in trailing form. Nevertheless, the leading and trailing forms are
assigned distinct codepoints in Unicode. In addition, the set of valid
trailing consonants includes several compound-consonant pairs that can
never occur in leading form.

Old Korean featured a considerable number of additional jamo, which
are also defined in Unicode.  Many of these Old Korean jamo are
compound forms that concatenate two or three basic jamo. 
  
A **syllable** is formed by arranging a sequence of jamo into its
appropriate square-block form. The horizontal and vertical positioning
of each jamo in the block depends on the content of the syllable. The
exact shape and proportions of each jamo will also vary with its final
position in the block. 

Valid syllables must be either of the form "**`L`**,**`V`**" or of the form
"**`L`**,**`V`**,**`T`**". That is, each syllable must begin with one leading
consonant, must include one vowel in the second position, and may or may
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

Proper shaping of Hangul text runs involves determining when
sequences of jamo can be composed into syllable codepoints that are included in
the active font — in which case they should be replaced by the corresponding
syllable glyph — and when they cannot. 

Those jamo sequences that cannot be composed into a syllable codepoint
(or that compose into a syllable codepoint that is missing in the
active font) are then rendered by shaping and positioning each
individual jamo using GSUB substitution rules. 



### Jamo type ###

Each Hangul jamo is assigned a `JAMO_TYPE` property that indicates whether
it is a leading consonant (`L`), a vowel (`V`), or a trailing
consonant (`T`).

Most, but not all, of the basic consonant letters can appear either in
leading or in trailing form. Nevertheless, the leading and trailing
forms are assigned distinct codepoints in Unicode. In addition, the
set of valid trailing consonants includes several compound consonant
pairs that can never occur in leading form.

For example, the basic consonant "Kiyeok" (&#x1100;) is encoded as `U+1100`
in its leading (choseong) form and as `U+11A8` in its trailing
(jongseong) form. The tense or emphatic form of the consonant,
"Ssangkiyeok" (&#x1101;), is encoded in its leading (choseong) form as
`U+1101` and in its trailing (jongseong) form as `U+11A9`, and is
rendered as a doubled version of the basic consonant.

Two of the compound trailing consonants, "Kiyeok-sios" (&#11aa;
`U+11AA`) and "Rieul-kiyeok" (&#11b0; `U+11B0`) also incorporate the
Kiyeok basic consonant. But Kiyeok-sios and Rieul-kiyeok are never
used as leading consonants, so they are not encoded in leading
(choseong) forms.

> Note: compound consonant jamo are not written as sequences of basic
> jamo. That is, "Kiyeok,Kiyeok" (&#x1100;&#x1100;) is not equivalent
> to "Ssangkiyeok" (&#x1101;). 

The Hangul Jamo block also includes two "filler" codepoints. "Choseong
Filler" (`U+115F`) can take the place of a missing choseong (`L`
consonant), and "Jungseong Filler" (`U+1160`) can take the place of a
missing jungseong (`V` vowel). For shaping purposes, the fillers are
classified as type `Lf` and type `Vf`, respectively.


### Composing behavior ###

Modern Korean features 19 leading consonants (`L` forms), 21 vowels
(`V` forms), and 27 trailing consonants (`T` forms). 

Old Korean featured a considerable number of additional jamo, which
are also defined in Unicode.  Some of these Old Korean jamo are
distinct basic letters that are no longer used in Modern Korean. Many
others are compound forms that concatenate two or even three basic jamo. 

The Hangul Syllables block in Unicode only includes those syllables
that contain solely Modern jamo. Consequently, each jamo is assigned a
`COMPOSING_BEHAVIOR` property to indicate whether it can be composed
into a Hangul Syllable codepoint. 

An "`L`,`V`,`T`" sequence with the `COMPOSING_BEHAVIOR`s
"`YES`,`YES`,`YES`" or an "`L`,`V`" sequence with the
`COMPOSING_BEHAVIOR`s "`YES`,`YES`" will compose to a codepoint in the Hangul
Syllables block. A sequence containing any `NO`s will not compose to a
codepoint in the Hangul Syllables block.

> Note: the jamo filler codepoints are both designated with the
> `COMPOSING_BEHAVIOR` of `NO`.


<!--- ### Identification by Unicode range ### --->




### Character tables ###


Separate character tables are provided for the Hangul Jamo, Hangul
Jamo Extended-A, and Hangul Jamo Extended-B blocks, as well as for other miscellaneous
characters that are used in `<hang>` text runs:

  - [Hangul Jamo character table](character-tables/character-tables-hangul.md#hangul-jamo-character-table)
  - [Hangul Jamo Extended-A character table](character-tables/character-tables-hangul.md#hangul-jamo-extended-a-character-table)
  - [Hangul Jamo Extended-B character table](character-tables/character-tables-hangul.md#hangul-jamo-extended-b-character-table)
  - [Miscellaneous character table](character-tables/character-tables-hangul.md#miscellaneous-character-table)


The Hangul Jamo block contains all of the Modern Korean jamo, the two
jamo fillers, and the most common Old Korean jamo. 

The Hangul Jamo Extended-A block contains additional `L` (choseong)
jamo for Old Korean. The Hangul Jamo Extended-B block contains
additional `V` (jungseong) and `T` (jongseong) jamo for Old Korean.

The Hangul Syllables block contains all of the valid permutations of the
Modern Korean jamo. Due to the size of the block, no character table
is provided.

Unicode also defines a Hangul Compatibility Jamo block that implements
backward compatibility with a retired file-encoding format. Unless a
software application is required to support specific stores of
documents that are known to have used the older encoding, however, the 
shaping engine should not be expected to handle any text runs
incorporating codepoints from this block.

The tables list each codepoint along with its Unicode general
category, its jamo type, and its composing behavior. The codepoint's
Unicode name and an example glyph are also provided.

For example:

| Codepoint | Unicode category | Jamo type | Composing | Glyph                            |
|:----------|:-----------------|:----------|:----------|:---------------------------------|
|`U+1109`   | Letter           | L         | YES       | &#x1109; Sios                    |
| | | | | |
|`U+1182`   | Letter           | V         | NO        | &#x1182; O-O                     |


Codepoints with no assigned meaning are
designated as _unassigned_ in the _Unicode category_ column. 

In addition to general punctuation, runs of Hangul text may use
punctuation marks from the CJK Symbols And Punctuation block. 

Of particular note are the single-dot tone mark (single-dot bangjeom)
and double-dot tone mark (double-dot bangjeom), `U+302E` and
`U+302F`. These non-spacing marks are common in Old Korean.

Other important characters that may be encountered when shaping runs
of Hangul text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`), and zero-width non-joiner (`U+200C`).

The dotted-circle placeholder is frequently used when displaying a
mark in isolation. Real-world text may also use other characters, such
as hyphens or dashes, in a similar placeholder fashion; shaping
engines should cope with this situation gracefully.

The zero-width space (`U+200B`) or word joiner (`U+2060`) may be used
between two jamo to prevent them from being conjoined into a
syllable. The zero-width space allows a line break to happen between
the jamo, while the word joiner prevents the jamo from being separated
by a line break.


## The `<hang>` shaping model ##

Processing a run of `<hang>` text involves six top-level stages:

1. Identifying syllables
2. Determining if the syllable can be composed into a Hangul Syllable codepoint
3. Composing the syllable (if composition is possible)
4. Fully decomposing the syllable (if composition is not possible)
5. Shaping the fully decomposed syllable with GSUB features
6. Reordering tone marks


### 1. Identifying syllables ###

The precomposed syllable codepoints in the Hangul Syllable block come in
two forms: `LV` syllables (which represent an `L` jamo and a `V` jamo)
and `LVT` syllables (which represent an `L` jamo, a `V` jamo, and a `T` jamo).

A syllable consisting of a string of jamo must match either the
sequence "`L`,`V`" or the sequence "`L`,`V`,`T`".

The `L`, `V`, and `T` components must be a single jamo each. In Modern
Korean, all of the jamo must have a `COMPOSING_BEHAVIOR` of `YES`. In
Old Korean, `YES` and `NO` are both acceptable for
`COMPOSING_BEHAVIOR`. 

However, real-world input can also include syllables entered as a
precomposed `LV` Hangul Syllable codepoint followed by a standalone
`T` jamo.

Syllables in a text run can therefore be identified with the following
regular expression:

```
    Slvt |  <Slv | <L|Lf>+<V|Vf>> + [T]
```


    L	  L jamo
	V	  V jamo
	T	  T jamo
	Lf	  L jamo filler
	Vf	  V jamo filler
	Slv	  Precomposed "LV" syllable
	Slvt	  Precomposed "LVT" syllable
	
	[ ]	  optional occurence of the enclosed expression
	<|>	  one of the options separated by the vertical bar






<L> 
    <L,V> 
    <L,V,T>
    <LV>
    <LVT>
    <LV, T>



### 2. Determining if the syllable can be composed into a Hangul Syllable codepoint ###


### 3. Composing the syllable (if composition is possible) ###


### 4. Fully decomposing the syllable (if composition is not possible) ###


### 5. Shaping the fully decomposed syllable with GSUB features ###


#### 5.1 ccmp ####

#### 5.2 ljmo ####

#### 5.3 vjmo ####

#### 5.4 tjmo ####


### 6. Reordering tone marks ###







   
   
