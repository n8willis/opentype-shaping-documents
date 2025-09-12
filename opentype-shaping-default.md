# Default script shaping in OpenType #

This document details the default shaping procedure needed to display
text runs in non-complex scripts. It may also be used as a fallback
model for unrecognized scripts.


**Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Normalization](#normalization)
  - [The default shaping model](#the-default-shaping-model)
      - [Stage 1: Applying the basic substitution features from <abbr>GSUB</abbr>](#stage-1-applying-the-basic-substitution-features-from-gsub)
	  - [Stage 2: Applying typographic substitution features from <abbr>GSUB</abbr>](#stage-2-applying-typographic-substitution-features-from-gsub)
	  - [Stage 3: Applying the positioning features from <abbr>GPOS</abbr>](#stage-3-applying-the-positioning-features-from-gpos)
  
  
  
## General information ##

The default OpenType shaping model is used for scripts that are
considered _non-complex_ from the shaper's perspective. This
designation means that shaping a text run does not involve glyph
reordering, contextual joining behavior, or the substitution of
context-dependent forms for linguistic or orthographic correctness.

Text runs in non-complex scripts may, however, involve ligature
substitution, Unicode normalization, mark positioning, kerning, and
the application of other features from the active font's <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr>
tables.

The non-complex scripts covered by this model include Latin, Cyrillic,
Greek, Armenian, Georgian, Ethiopic, Cherokee, Tifinagh, and many others.


## Terminology ##

Many of these scripts support diacritics and other **marks**. Unicode may
contain **precomposed** mark-and-base codepoints for some or all
combinations of marks and base letters in the script. For combinations
without a codepoint, the desired form can be achieved by following the
**base** letter with a **combining mark** codepoint. 

The primary concern for the shaping engine is processing the text run into
the correct normalized form, so that the best glyphs from the active
font can be selected from among the available precomposed and
combining alternatives.

Fonts for non-complex scripts might not include a <abbr title="Glyph Substitution table">GSUB</abbr> or <abbr title="Glyph Positioning table">GPOS</abbr> table
at all. 

However, <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> may also be used to implement a variety of
OpenType smart features, including several classes of ligature,
contextual alternate, or contextual positioning rules. Because these
features are not required in order to render the text run
orthographically correct, the features are not considered shaping
features. Nevertheless, the shaping engine may be expected to apply
these features in order to simplify the overall text-rendering
architecture of the implementation.

## Normalization ##

Unicode defines algorithms for normalizing a sequence of input
codepoints into either a canonical composed form or a canonical
decomposed form. The purpose of these algorithms and of the defined
normalization forms is to determine equivalent representations of input
sequences regardless of variations in the input sequences.

For example, a base letter with an attached mark might exist in
Unicode as a single codepoint, but an input sequence might consist of
the base letter codepoint followed by the combining mark
codepoint. Unicode normalization can be used to determine that the
<samp>"letter, mark"</samp> sequence is equivalent to the single codepoint. This
simplifies sorting, searching, string comparison, and many other common
tasks.

OpenType shaping utilizes Unicode normalization, but OpenType
shaping has a distinctly different goal: to select the best or most
appropriate representation of the input codepoint sequence that is
available in the active font. A full description of the algorithm is
available in the [normalization](opentype-shaping-normalization.md) document. 

Shaping some complex scripts involves explicit composition or
decomposition steps. The default shaping model does not involve any
such steps, but it does proceed with the general assumption that text
runs have been normalized as part of input sanitization. 

For convenience, shaping engines may choose to implement a single
normalization routine for all scripts, default and complex. If
normalization is done before the shaping-model–specific processing is
done, then there may be no work required in certain shaping steps
(such as the processing of `ccmp` substitutions from <abbr title="Glyph Substitution table">GSUB</abbr>). However,
these steps will always be described in the relevant script's shaping
document. 


## The default shaping model ##

Processing a run of text in the default shaping model involves three
top-level stages:

1. Applying the basic substitution features from <abbr>GSUB</abbr>
2. Applying typographic substitution features from <abbr>GSUB</abbr>
3. Applying the positioning features from <abbr>GPOS</abbr>

Together, these stages cover the application of all <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr>
features that are required or that have been defined by OpenType as
being on by default.

For convenience, shaping engines may also choose to apply any optional
or off-by-default OpenType features that have been activated for the
text run (including those that have been
enabled by the user and those that have been enabled at the
application level). However, the order in which such features should
be applied and how they should interact with OpenType shaping features
is beyond the scope of this document.

The default shaping model does not involve syllable-identification,
word-identification, or other preprocessing of the input
sequence. Shaping engines may choose how to segment longer text runs
for processing, or may choose to rely on higher-level applications to
make segmentation decisions.


### Stage 1: Applying the basic substitution features from <abbr>GSUB</abbr> ###

The basic-substitution stage applies mandatory substitution features
using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this
stage, glyph sequences should be tagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features.

These substitutions include those features designed to provide
linguistic and orthographic correctness.

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.

	locl
	ccmp
	rlig
	
The `locl` feature replaces default glyphs with any language-specific
variants, based on examining the language setting of the text run.

> Note: Strictly speaking, the use of localized-form substitutions is
> not part of the shaping process, but of the localization process,
> and could take place at an earlier point while handling the text
> run. However, shaping engines are expected to complete the
> application of the `locl` feature before applying the subsequent
> <abbr title="Glyph Substitution table">GSUB</abbr> substitutions in the following steps.

The `ccmp` feature allows a font to substitute mark-and-base sequences
with a pre-composed glyph including the mark and the base, or to
substitute a single glyph into an equivalent decomposed sequence of
glyphs. 

If present, these composition and decomposition substitutions must be
performed before applying any other <abbr title="Glyph Substitution table">GSUB</abbr> lookups, because
those lookups may be written to match only the `ccmp`-substituted
glyphs.

> Note: The `ccmp` feature may perform compositions or decompositions
> of glyph sequences that do not have a canonical decomposition
> defined in Unicode. 

The `rlig` feature substitutes glyph sequences with mandatory
ligatures. Substitutions made by `rlig` cannot be disabled by
application-level user interfaces.


### Stage 2: Applying typographic substitution features from <abbr>GSUB</abbr> ###

The typographic-substitution phase applies all remaining substitution
features using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for
this stage, glyph sequences should be tagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features.

These substitutions include those features designed to provide
typographic consistency and correctness.

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.


	rclt
	calt
	clig
	liga
	

The `rclt` feature substitutes glyphs with contextual alternate
forms. In general, the `rclt` feature is used to perform such
substitutions that are required by the orthography of the active
script and language. Substitutions made by `rclt` cannot be disabled
by application-level user interfaces.

The `calt` feature substitutes glyphs with contextual alternate
forms. In general, the `calt` feature performs substitutions that are
not mandatory for orthographic correctness. However, unlike `rclt`,
the substitutions made by `calt` can be disabled by application-level
user interfaces.

The `clig` feature substitutes optional ligatures that are on by
default, but which are activated only in certain
contexts. Substitutions made by `clig` may be disabled by
application-level user interfaces. 

The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.


### Stage 3: Applying the positioning features from <abbr>GPOS</abbr> ###

The positioning stage adjusts the positions of mark and base
glyphs. In preparation for this stage, glyph sequences should be
tagged for possible application of <abbr title="Glyph Positioning table">GPOS</abbr> features.

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.


	curs
	dist
	kern
	mark
	mkmk

The `curs` feature perform cursive positioning. Each glyph has an
entry point and exit point; the `curs` feature positions glyphs so
that the entry point of the current glyph meets the exit point of the
preceding glyph.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software kerning features, if
such features are optional.

The `kern` adjusts glyph spacing between pairs of adjacent glyphs.

The `mark` feature positions marks with respect to base glyphs.

The `mkmk` feature positions marks with respect to preceding marks,
providing proper positioning for sequences of marks that attach to the
same base glyph.

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
