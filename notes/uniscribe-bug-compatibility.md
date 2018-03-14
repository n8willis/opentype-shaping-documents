# Notes for preserving Uniscribe compatibility #

This document details behavior that shaping engines may wish to
implement in order to maintain srict shaping compatibility with
Microsoft's Uniscribe OpenType shaper, including behavior that may be
regarded as bugs by end users.

**Table of Contents**

  - [Indic standalone-syllable dotted circles](#indic-standalone-syllable-dotted-circles)
  - [Indic syllable cluster merging](#indic-syllable-cluster-merging)
  - [Indic fallback Reph reordering](#indic-fallback-reph-reordering)
  - [Khmer kerning](#khmer-kerning)
  - [Sinhala matra decomposition](#sinhala-matra-decomposition)
  - [Miscellaneous](#miscellaneous)

Compatibility notes in the "miscellaneous" category deal with
behaviors that are, incompletely documented, deal solely with
deprecated script tags, or do not violate known conventions. Thus, the
scenarios with which they deal may not be regarded as bugs.


## Indic standalone-syllable dotted circles ##

In Indic syllables that include a `PLACEHOLDER` or `DOTTED_CIRCLE`
codepoint, if a dotted-circle glyph is the last consonant of the
syllable, Uniscribe ignores the glyph when processing the syllable.

For example, the dotted-circle glyph is not counted as a consonant
when locating the syllable's base consonant. Therefore, the sequence
"Ra,Halant,Dotted_Circle" does not trigger Reph formation (which would
result in the sequence "Reph,Dotted_Circle").


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
position happens to occur immediately after a "Matra,Halant" sequence,
Uniscribe leaves the Reph in this position.

Other shaping engines, in this situation, will reorder the Reph to a
position immediately before the "Matra,Halant" sequence. This allows
for any GSUB substitutions that match "Reph,Matra" sequences to be
activated, if any such substitution rules are present in the active
font. 


## Khmer kerning ##

Uniscribe does not apply the `kern` feature to Khmer text, even if the
active font includes kerning tables for Khmer codepoints.


## Sinhala matra decomposition ##

Sinhala text in OpenType presents two possible methods for
decomposing multi-part matras. 

One is the canonical Unicode decompositions for the matra codepoints,
as is used in most other Indic scripts. This decomposition is usually
performed early in the shaping process.

The second is the `pstf` feature of GSUB, which is defined differently
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
Uniscribe-supported behavior might not include GPOS positioning
rules for the right-side matra components, relying instead on the
`pstf` substitution to provide a suitable replacement.



## Miscellaneous ##


### Old-model post-base Halant reordering ###

In old-model (Indic1) script tags, Uniscribe treats some
scripts differently when reordering the first post-base Halant. This
Halant-reordering is done in Indic1 scripts in order to prepare the
syllable for Indic1's different post-base GSUB substitution rules.

For example, the old-model Indic syllable

	Pre-baseC Halant BaseC Halant Post-baseC

would be reordered to

	Pre-baseC Halant BaseC Post-baseC Halant

before features are applied.

In Malayalam, Uniscribe always reorders the first post-base Halant in
a syllable to the position immediately after the syllable's last consonant.

In Kannada, and possibly in other scripts, Unicode reorders the first
post-base Halant only when there is not already a Halant after the
last consonant. 


### Halants and left matras ###

When reordering left-side matras, when a Halant occurs immediately
after a left-side matra, Uniscribe does not move the Halant with the matra.

Generally, marks (including "Halant") are tagged for reordering with
the same positioning tag as the closest non-mark character that the
mark has affinity with. 

In post-base position, where a yet-to-be-reordered left-side matra
would be found, the closest non-mark character with affinity for the
mark might be a post-base consonant. Uniscribe appears to make a check
ensuring that the Halant after a left-side matra is not tagged for
reordering with the matra.

This check is required for shaping Sinhala, because the `U+0DDA`
multi-part matra decomposes into the sequence "`U+0DD9`,Halant". The
decomposed Halant should remain where it is, serving as the right-side
matra component.
