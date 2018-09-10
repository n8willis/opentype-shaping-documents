# Default script shaping in OpenType #

This document details the default shaping procedure needed to display
text runs in non-complex scripts. It may also be used as a fallback
model for unrecognized scripts.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
  - [Normalization](#normalization)
  - [The default shaping model](#the-default-shaping-model)
      - [1: Applying the basic substitution features from GSUB]
	  - [2: Applying typographic substitution features from GSUB]
	  - [3: Applying the positioning features from GPOS]
  
  
  
## General information ##

The default OpenType shaping model is used for scripts that are
considered _non-complex_ from the shaper's perspective. This
designation means that shaping a text run does not involve glyph
reordering, contextual joining behavior, or the substitution of
context-dependent forms for linguistic or orthographic correctness.

Text runs in non-complex scripts may, however, involve ligature
substitution, Unicode normalization, mark positioning, kerning, and
the application of other features from the active font's GSUB and GPOS
tables.

The non-complex scripts covered by this model include Latin, Cyrillic,
Greek, Armenian, Georgian, Ethiopic, Cherokee, Tifinagh, and many others.


## Terminology ##

Many of these scripts support diacritics and other **marks**. Unicode may
contain **precomposed** mark-and-base codepoints for some or all
combinations of marks and base letters in the script. For combinations
without a codepoint, the desired form can be acheived by following the
**base** letter with a **combining mark** codepoint. 

The primary concern for the shaping engine is processing the text run into
the correct normalized form, so that the best glyphs from the active
font can be selected from among the available precomposed and
combining alternatives.

Fonts for non-complex scripts might not include a GSUB or GPOS table
at all. 

However, GSUB and GPOS may also be used to implement a variety of
OpenType smart features, including several classes of ligature,
contextual alternate, or contextual positioning rules. Because these
features are not required in order to render the text run
orthographically correct, the features are not considered shaping
features. Nevertheless, the shaping engine may be expected to apply
these features in order to simplify the overall text-rendering
architecture of the implementation.

## Normalization ##

## The default shaping model ##

### 1: Applying the basic substitution features from GSUB ###

	locl
	ccmp
	rlig

### 2: Applying typographic substitution features from GSUB ###

	calt
	clig
	curs
	liga
	rclt

### 3: Applying the positioning features from GPOS ###

	dist
	kern
	mark
	mkmk

<!---
collect features
override features
data create
data destroy
preprocess text
postprocess glyphs
normalization mode default
decompose
compose
setup masks
disable otl
reorder marks
zero width marks by gdef late
fallback position
--->
