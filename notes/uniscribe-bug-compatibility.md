# Notes for preserving Uniscribe compatibility #

This document details behavior that shaping engines may wish to
implement in order to maintain strict shaping compatibility with
Microsoft's Uniscribe OpenType shaper, including behavior that may be
regarded as bugs by end users.

**Table of Contents**

  - [Indic standalone-syllable dotted circles](#indic-standalone-syllable-dotted-circles)
  - [Indic syllable cluster merging](#indic-syllable-cluster-merging)
  - [Indic fallback Reph reordering](#indic-fallback-reph-reordering)
  - [Kannada legacy treatment of "Ra,Halant,ZWJ"](#kannada-legacy-treatment-of-ra-halant-zwj)
  - [Khmer kerning](#khmer-kerning)
  - [Sinhala matra decomposition](#sinhala-matra-decomposition)
  - [Miscellaneous](#miscellaneous)
      - [Bengali init feature matching](#bengali-init-feature-matching)
      - [Old-model post-base Halant reordering](#old-model-post-base-halant-reordering)
          - [Kannada final double Halants](#kannada-final-double-halants)
      - [Halants and left matras](#halants-and-left-matras)
	  - [Explicit half-forms followed by matras](#explicit-half-forms-followed-by-matras)


Compatibility notes in the "miscellaneous" category deal with
behaviors that are incompletely documented, deal solely with
deprecated script tags, or do not violate known conventions. Thus, the
scenarios with which they deal may not be regarded as bugs.



## Indic standalone-syllable dotted circles ##

In Indic syllables that include a `PLACEHOLDER` or `DOTTED_CIRCLE`
codepoint, if a dotted-circle glyph is the last consonant of the
syllable, Uniscribe ignores the glyph when processing the syllable.

For example, the dotted-circle glyph is not counted as a consonant
when locating the syllable's base consonant. Therefore, the sequence
<samp>"Ra,Halant,Dotted_Circle"</samp> does not trigger Reph formation (which would
result in the sequence <samp>"Reph,Dotted_Circle"</samp>).


## Indic syllable cluster merging ##

Other shaping engines, such as Harfbuzz, track the indivisible
components of a syllable in "clusters". Each individual letter usually
corresponds to a cluster; when two letters ligate or form a conjunct,
their clusters are merged. When a codepoint is decomposed, its
components remain part of the same, original cluster as the
precomposed version. Uniscribe appears to follow this pattern as well.

When shaping Indic text in most scripts, after shaping the entire
syllable, Uniscribe merges all of the clusters of the syllable into a
single, indivisible cluster. 

The exceptions to this behavior occur when Uniscribe is shaping Tamil
and Sinhala. In those cases, the full-syllable cluster merge is not
performed.

> Note: This full-syllable clustering makes it hard for application
> software to position the cursor within the word. It may also have
> other implications for software above the shaping engine in the
> stack.


## Indic fallback Reph reordering ##

When shaping Indic syllables, any one of several Reph-positioning
strategies may be required by the active script. In the event that no
correct position can be determined by the shaping engine for a
syllable, Uniscribe's ultimate fallback behavior is to reorder the
Reph to the end of the syllable.

If the Reph is reordered to the end of the syllable and this final
position happens to occur immediately after a <samp>"Matra,Halant"</samp> sequence,
Uniscribe leaves the Reph in this position.

Other shaping engines, in this situation, will reorder the Reph to a
position immediately before the <samp>"Matra,Halant"</samp> sequence. This allows
for any <abbr>GSUB</abbr> substitutions that match <samp>"Reph,Matra"</samp> sequences to be
activated, if any such substitution rules are present in the active
font. 

## Kannada legacy treatment of "Ra,Halant,ZWJ" ##

In the `<knda>` shaping model (which was deprecated in 2005 in favor
of `<knd2>`), the sequence <samp>"Ra,Halant,ZWJ"</samp> was treated as equivalent
to the sequence <samp>"Ra,ZWJ,Halant"</samp>.

## Khmer kerning ##

Uniscribe does not apply the `kern` feature to Khmer text, even if the
active font includes kerning tables for Khmer codepoints.


## Sinhala matra decomposition ##

Sinhala text in OpenType presents two possible methods for
decomposing multi-part matras. 

One is the canonical Unicode decompositions for the matra codepoints,
as is used in most other Indic scripts. This decomposition is usually
performed early in the shaping process.

The second is the `pstf` feature of <abbr>GSUB</abbr>, which is defined differently
for Sinhala. In Sinhala, the `pstf` feature replaces multi-part
dependent vowels (matras) with the right-side matra component of the
canonical decomposition. This substitution generally occurs late in
the shaping process.

Uniscribe supports the `pstf` behavior by handling the decomposition
of multi-part dependent vowels differently for Sinhala -- in a sense,
decomposing each matra into its left-side component followed by a
duplicate of the original matra, then substituting the duplicated
matra with the right-side matra component when the `pstf` feature is
applied.

Shaping engines may opt to decompose multi-part dependent
vowels into their canonical Unicode decompositions, as is done in
other scripts, and substitute the decomposed right-side matra
components at that point.
 
Doing so will negate the need to apply the `pstf` substitution.
However, fonts that were engineered to support the
Uniscribe-supported behavior might not include <abbr>GPOS</abbr> positioning
rules for the right-side matra components, relying instead on the
`pstf` substitution to provide a suitable replacement.



## Miscellaneous ##


### Bengali `init` feature matching ###

The `init` feature in Bengali is defined in the OpenType specification
as applying to word-initial left-side dependent vowels (matras).
However, Uniscribe specifically applies the feature whenever
the matra is preceded by any character that falls within the following
range in the Unicode `General Category` property:

- `GENERAL_CATEGORY_FORMAT` [Cf]
- `GENERAL_CATEGORY_UNASSIGNED` [Cn]
- `GENERAL_CATEGORY_PRIVATE_USE` [Co]
- `GENERAL_CATEGORY_SURROGATE` [Cs]
- `GENERAL_CATEGORY_LOWERCASE_LETTER` [Ll]
- `GENERAL_CATEGORY_MODIFIER_LETTER` [Lm]
- `GENERAL_CATEGORY_OTHER_LETTER` [Lo]
- `GENERAL_CATEGORY_TITLECASE_LETTER` [Lt]
- `GENERAL_CATEGORY_UPPERCASE_LETTER` [Lu]
- `GENERAL_CATEGORY_SPACING_MARK` [Mc]
- `GENERAL_CATEGORY_ENCLOSING_MARK` [Me]
- `GENERAL_CATEGORY_NON_SPACING_MARK` [Mn]


### Old-model post-base Halant reordering ###

In old-model (Indic1) script tags, Uniscribe treats some
scripts differently when reordering the first post-base <samp>"Halant"</samp>. This
Halant-reordering is done in Indic1 scripts in order to prepare the
syllable for Indic1's different post-base <abbr>GSUB</abbr> substitution rules.

For example, the old-model Indic syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In Malayalam, Uniscribe always reorders the first post-base <samp>"Halant"</samp> in
a syllable to the position immediately after the syllable's last consonant.

#### Kannada final double Halants ####

In old-model Kannada (`<knda>`) runs, Uniscribe is known to reorder
the first post-base <samp>"Halant"</samp> only when there is not already a <samp>"Halant"</samp>
after the last consonant.

For example, the old-model Indic syllable

	Pre-baseC Halant BaseC Halant Post-baseC Halant

would _not_ be reordered. 

This behavior is an exception to the general Indic1 post-base <samp>"Halant"</samp>
reordering operation. It is believed to be script-specific and has
only been observed for Kannada text runs. However, there may still be
undiscovered sequences in other Indic1-script text which trigger the
same behavior; implementers targeting full compatibility should
exercise caution.

If the standard post-base <samp>"Halant"</samp> reordering were performed, then the
likely result of the <abbr>GSUB</abbr> feature-application phase would be a
sequence of the form <samp>"BaseC,belowbaseC,Halant"</samp> which, in turn, might
trigger mark-attachment issues for correctly positioning the final
<samp>"Halant"</samp>.

This Uniscribe behavior is not documented, however; therefore the only
recommended workaround for maintaining compatibility is to define a
special-case exception for avoiding the creation of final double
<samp>"Halant"</samp>s in `<knda>` text.


### Halants and left matras ###

When reordering left-side matras, when a <samp>"Halant"</samp> occurs immediately
after a left-side matra, Uniscribe does not move the <samp>"Halant"</samp> with the matra.

Generally, marks (including <samp>"Halant"</samp>) are tagged for reordering with
the same positioning tag as the closest non-mark character that the
mark has affinity with. 

In post-base position, where a yet-to-be-reordered left-side matra
would be found, the closest non-mark character with affinity for the
mark might be a post-base consonant. Uniscribe appears to make a check
ensuring that the <samp>"Halant"</samp> after a left-side matra is not tagged for
reordering with the matra.

This check is required for shaping Sinhala, because the `U+0DDA`
multi-part matra decomposes into the sequence <samp>"`U+0DD9`,Halant"</samp>. The
decomposed <samp>"Halant"</samp> should remain where it is, serving as the right-side
matra component.


### Explicit half-forms followed by matras ###

As a general rule, Uniscribe and other shapers insert a dotted-circle
character before a non-spacing mark character (such as a matra in
Indic2-model scripts) when that non-spacing mark character is not
matched with a base character in a permitted syllable. In such
circumstances, the dotted-circle visually serves to communicate to
readers that a base character has not been found, and also
functionally serves as a surrogate base on which the mark character
can be positioned.

However, Uniscribe is known not to insert a dotted-circle before a
matra character when it is preceded by two sequential
explicit-half-form sequences (meaning two consecutive occurrences of
<samp>"_Consonant_,Halant,ZWJ"</samp>) in Indic2 runs.

Therefore, the sequence:

    `_Consonant_,Halant,ZWJ,_matra_`

would be transformed to:

    `_Consonant_,Halant,ZWJ,Dotted-Circle,_matra_`

but the sequence:

    `_Consonant_,Halant,ZWJ,_Consonant_,Halant,ZWJ,_matra_`

would _not_ be transformed with a dotted-circle insertion.

This exception is regarded as a likely bug.
