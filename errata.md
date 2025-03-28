# OpenType shaping errata #

This document details errata that shaping engines may encounter, such
as ambiguities or omissions in the existing OpenType or Unicode
specification documents.


**Table of Contents**

  - [Unicode](#unicode)
      - [<abbr>ZWJ</abbr> and <abbr>ZWNJ</abbr>](#zwj-and-zwnj)
	      - [Scope of <abbr>ZWJ</abbr> and <abbr>ZWNJ</abbr>](#scope-of-zwj-and-zwnj)
	      - [<abbr>ZWJ</abbr> in redundant ligature lookups](#zwj-in-redundant-ligature-lookups)
      - [Emoji](#emoji)
	      - [Skin-tone permutations](#skin-tone-permutations)
		  - [Gender permutations](#gender-permutations)
  - [OpenType](#opentype)
      - [Null offsets in <abbr>GSUB</abbr> and <abbr>GPOS</abbr>](#null-offsets-in-gsub-and-gpos)
      - [Sorting of <abbr>GSUB</abbr> and <abbr>GPOS</abbr> lookups](#sorting-of-gsub-and-gpos-lookups)
	  - [Per-script applicability of feature tags](#per-script-applicability-of-feature-tags)
      - [Ordering of post-base and below-base consonants in Indic2 base-consonant determination](#ordering-of-post-base-and-below-base-consonants-in-indic2-base-consonant-determination)
      - [Lookup behavior](#lookup-behavior)
          - [Using MultipleSub for glyph deletion](#using-multiplesub-for-glyph-deletion)
		  - [Processing nested contextual lookups](#processing-nested-contextual-lookups)
      - [Adjacent-mark reordering ambiguities](#adjacent-mark-reordering-ambiguities)
      - [Merging of glyph properties](#merging-of-glyph-properties)
  - [See also](#see-also)

  
  
## Unicode ##

This section lists errata pertaining to the Unicode Standard.

### <abbr>ZWJ</abbr> and <abbr>ZWNJ</abbr> ###

#### Scope of <abbr>ZWJ</abbr> and <abbr>ZWNJ</abbr> ####

Unicode provides the Zero Width Joiner (<abbr>ZWJ</abbr>) and Zero Width Non-Joiner
(<abbr>ZWNJ</abbr>) control characters so that a text sequence can "request a
rendering system to have more or less of a connection between
characters than they would otherwise have."

The generic examples used in the standard show how <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr>
characters can affect the cursive-joining behavior between two
characters or the ligature-forming behavior between two
characters. However, the standard does not explicitly say whether or
not the presence of a <abbr title="Zero-Width Joiner">ZWJ</abbr> or <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> should influence the shaping
behavior of characters for characters not adjacent to the <abbr title="Zero-Width Joiner">ZWJ</abbr> or <abbr title="Zero-Width Non Joiner">ZWNJ</abbr>.

For example, in the sequence <samp>"a,b,ZWNJ,c,d"</samp> the <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> should prevent
the application of a ligature between <samp>"b"</samp> and <samp>"c"</samp> (if such a ligature
lookup exists in the active font).

However, if the active font contains a contextual ligature lookup for
<samp>"c,d"</samp> when preceded by <samp>"b"</samp>, it is not clear whether or not the <abbr title="Zero-Width Non Joiner">ZWNJ</abbr>
in the same <samp>"a,b,ZWNJ,c,d"</samp> sequence should inhibit the application of
the ligature between <samp>"c"</samp> and <samp>"d"</samp>.


#### <abbr>ZWJ</abbr> in redundant ligature lookups ####

An "Implementation Notes" section in chapter 23.2 of the Unicode
Standard says that font vendors should add <abbr title="Zero-Width Joiner">ZWJ</abbr> sequences to ligature
lookups. For example, if the sequence <samp>"f,i"</samp> triggers the <samp>"fi"</samp>
ligature, then the font should also include a lookup that triggers the
<samp>"fi"</samp> ligature for <samp>"f,ZWJ,i"</samp>. 

However, the text of chapter 23.2 prior to the "Implementation Notes"
says that <abbr title="Zero-Width Joiner">ZWJ</abbr> and <abbr title="Zero-Width Non Joiner">ZWNJ</abbr> "are not to be used in all cases where
ligatures or cursive connections are desired; instead, they are meant
only for over-riding the normal behavior of the text." That logic
makes the suggested <samp>"f,ZWJ,i"</samp> ligature lookup superfluous, because it
duplicates the effects of the existing <samp>"f,i"</samp> ligature lookup.

Using <abbr title="Zero-Width Joiner">ZWJ</abbr> within lookup patterns in the manner suggested by the
"Implementation Notes" is not common practice. 

### Emoji ###

#### Skin-tone permutations ####

It is unclear whether <abbr title="Zero-Width Joiner">ZWJ</abbr> multi-person group emoji sequences are
expected to include combinations where some emoji in the sequence are
followed by a Fitzpatrick skin-tone modifier but other emoji in the
sequence are not followed by a Fitzpatrick skin-tone modifier.

For example, it is unclear whether the sequence
<samp>"Man,ZWJ,Handshake,Man,SkinTone-2"</samp> constitues a valid
<abbr title="Zero-Width Joiner">ZWJ</abbr> "Couple holding hands" sequence.


#### Gender permutations ####

It is unclear whether <abbr title="Zero-Width Joiner">ZWJ</abbr> multi-person group emoji sequences are
expected to include combinations where some emoji in the sequence are
are an explicit gender but other emoji in the sequence are not
explicit gender.

For example, it is unclear whether the sequence
<samp>"Man,ZWJ,Handshake,Person"</samp> constitues a valid
<abbr title="Zero-Width Joiner">ZWJ</abbr> "Couple holding hands" sequence.

It is also unclear whether the <abbr title="Zero-Width Joiner">ZWJ</abbr> multi-person family sequence must
have explicit gender-ordering for the adult humans depicted.

For example, it is unclear whether the sequence
<samp>"Man,ZWJ,Woman,ZWJ,Girl"</samp> should be rendered identically to the
sequence <samp>"Woman,ZWJ,Man,ZWJ,Girl"</samp>.


## OpenType ##

This section lists errata pertaining to the OpenType specification.

### Null offsets in <abbr>GSUB</abbr> and <abbr>GPOS</abbr> ###

The headers of the <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr> tables include fields that contain
the offsets at which other structures within the font binary are
found. For example, the value of the `featureVariationsOffset` field
indicates the byte value at which the featureVariations structure is
located.

The OpenType specification notes that `featureVariationsOffset` can be
`NULL`, but the specification does not indicate whether or any other
offset values can also be `NULL` (nor, conversely, does it indicate
whether `NULL` should be considered invalid).

In practice, other fields -- such as `scriptListOffset`,
`featureListOffset`, and `lookupListOffset` -- may have `NULL` values.
In such situations, `NULL` is usually intrepreted as meaning that the
structure nominally pointed to by the offset is empty.

Furthermore, font-validation functions may overwrite a `NULL` into an
offset field if the original value encountered was invalid.


### Sorting of <abbr>GSUB</abbr> and <abbr>GPOS</abbr> lookups ###

The OpenType specification requires that lookups in the <abbr title="Glyph Substitution table">GSUB</abbr> table
must be sorted into numeric order before they are applied.

Lookups in the <abbr title="Glyph Positioning table">GPOS</abbr> table, however, are not expected to be sorted
first, because <abbr title="Glyph Positioning table">GPOS</abbr> lookups are applied in a specified order.

### Per-script applicability of feature tags ###

Some OpenType feature tags are defined only to apply to text runs in
specific scripts. Other feature tags are defined to apply to text in
any script.

However, the definitions of some feature tags list a limited number of
example scripts to which the feature should apply, but do not specify
every supported script.

For example, the `pstf` (post-base forms) tag is
[described](https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#tag-pstf)
as required for "scripts of south and southeast Asia that have
post-base forms for consonants eg: Gurmukhi, Malayalam, Khmer."


### Ordering of post-base and below-base consonants in Indic2 base-consonant determination ###

The Microsoft script-development specification for all Indic2-model
scripts
[states](https://docs.microsoft.com/en-us/typography/script-development/bengali#reorder-characters)
parenthetically that "post-base forms have to follow below-base forms". 

If this statement is taken to be a rule, it would affect the
base-consonant search algorithm.

For example, in the Bengali sequence <samp>"Ka,Halant,Ba,Halant,Ya"</samp>
(`U+0995`,`U+09CD`,`U+09AC`,`U+09CD`,`U+09AF`), <samp>"Ka"</samp> would be
identified as the syllable base, with <samp>"Ba"</samp> designated a below-base
form and <samp>"Ya"</samp> designated a post-base form. However, in the similar
sequence <samp>"Ka,Halant,Ya,Halant,Ba"</samp>
(`U+0995`,`U+09CD`,`U+09AF`,`U+09CD`,`U+09AC`), <samp>"Ya"</samp> would be
identified as the base consonant.

Real-world Bengali texts provide counterexamples that contradict the
assumption that "post-base forms follow below-base forms" is a
requirement.

In other scripts, such as Telugu, the "post-base forms have to follow
below-base forms" statement is, perhaps, statistically likely, but is
certainly not an orthographic rule.

Consequently, it is unclear if the statement should be enforced as a
rule or if it should be regarded as a suggestion, and it is unclear to
what degree that answer varies between the Indic2-model scripts.


### Lookup behavior ###

#### Using MultipleSub for glyph deletion ####

The <abbr title="Glyph Substitution table">GSUB</abbr> specification says that a `MultipleSubst` substitution cannot
be used to delete a glyph: it always substitutes at least one
replacement glyph. However, some implementations allow the
replacement-glyph array to be zero-length. 

#### Processing nested contextual lookups ####

The <abbr title="Glyph Substitution table">GSUB</abbr> specification allows contextual substitutions to invoke other
contextual substitutions. It is unclear how implementations ought to
handle certain cases of these nested lookups.

For example:
```
context: 'a'
subst index 0:
  context: 'ab'
  subst index 1: 'b' → 'ab'
```

This nested set of substitutions could cause an infinite loop on
certain input strings, if it is interpreted in a naive manner:
```
'[]ab' // begin at start of glyph sequence
'[a]b' // context matches
'[ab]' // nested context matches at index 0
'[aab]' // subst applies at index 1
'[a]ab' // return to parent context, uh oh!
'a[]ab' // move on to next glyph
'a[a]b' // context matches, infinite loop!
```

In short, if a nested contextual substitution can insert glyphs ahead
of its parent contextual substitution's context, then it creates a
"stack" that allows Turing-complete computation.



### Adjacent-mark reordering ambiguities ###

The Microsoft script-development specifications
[say](https://docs.microsoft.com/en-us/typography/script-development/devanagari#reorder-characters)
that marks should be reordered "to canonical order" (step 3 in the
linked Devanagari document) in the reordering phase. However, the same
step also describes this step as "Adjacent nukta and halant or nukta
and Vedic sign are always repositioned if necessary, so that the nukta
is first."

Together, it is somewhat ambiguous as to whether only <samp>"Halant,Nukta"</samp>
and <samp>"_Vedic_sign_,Nukta"</samp> sequences should be reordered by moving the
<samp>"Nukta"</samp> to the beginning, or all sequences of marks require reordering
into Unicode canonical combining class order, with <samp>"Nukta"</samp> moving to
the initial position as a special case.


### Merging of glyph properties ###

When the application of a shaping operation merges two or more
adjacent glyphs (for example, when two adjacent glyphs are substituted
with a single ligature glyph), the OpenType specification does not
dictate how shaping engines should combine (for example, merge,
replace, or drop) the properties of the input glyphs to determine the
properties of the output glyph.

This may result in ambiguities when a sequence of glyphs has several
substitutions applied in series.

For example, when shaping Indic scripts, glyphs may be tagged for the
possible application of multiple features, such as `half` and `rkrf`,
which are applied serially.

HarfBuzz and Uniscribe both take the approach of retaining the
properties of the first input glyph in a sequence, propagating those
properties to the merged output glyph.


## See also ##

Shaping engines may also want to offer explicit compatibility with
Microsoft Uniscribe, for the purpose of ensuring that users' existing
documents do not break. Therefore, implementors may wish to consult
the [Uniscribe compatibility notes](notes/uniscribe-bug-compatibility.md).

These compatibilty notes record test-driven observations about
Uniscribe's behavior, and they include any behavior that is a known
bug or a known deviation from specifications. Consequently, the issues
raised by offering Uniscribe compatiblity cannot be considered errata
in the sense that it is described above.
