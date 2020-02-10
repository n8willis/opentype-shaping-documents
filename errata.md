# OpenType shaping errata #

This document details errata that shaping engines may encounter, such
as ambiguities or omissions in the existing OpenType or Unicode
specification documents.


**Table of Contents**

  - [OpenType](#opentype)
      - [Null offsets in GSUB and GPOS](#null-offsets-in-gsub-and-gpos)
      - [Sorting of GSUB and GPOS lookups](#sorting-of-gsub-and-gpos-lookups)
      - [Lookup behavior](#lookup-behavior)
          - [Using MultipleSub for glyph deletion](#using-multiplesub-for-glyph-deletion)
          - [Flags in nested contextual lookups](#flags-in-nested-contextual-lookups)
  - [Adjacent-mark reordering ambiguities](#adjacent-mark-reordering-ambiguities)
  - [Merging of glyph properties](#merging-of-glyph-properties)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
  - [See also](#see-also)

  
  

## OpenType ##

This section lists errata pertaining to the OpenType specification.

### Null offsets in GSUB and GPOS ###

The headers of the GSUB and GPOS tables include fields that contain
the offsets at which other structures within the font binary are
found. For example, the value of the featureVariationsOffset field
indicates the byte value at which the featureVariations structure is
located.

The OpenType specification notes that featureVariationsOffset can be
`NULL`, but the specification does not indicate whether or any other
offset values can also be `NULL` (nor, conversely, does it indicate
whether `NULL` should be considered invalid).

In practice, fields such as scriptListOffset, featureListOffset, and
lookupListOffset may have `NULL` values.  In such situations, `NULL`
is usually intrepreted as meaning that the structure nominally pointed
to by the offset is empty.


### Sorting of GSUB and GPOS lookups ###

The OpenType specification requires that lookups in the GSUB table
must be sorted into numeric order before they are applied.

Lookups in the GPOS table, however, are not expected to be sorted
first, because GPOS lookups are applied in a specified order.

### Lookup behavior ###



#### Using MultipleSub for glyph deletion ####



#### Flags in nested contextual lookups ####



### Adjacent-mark reordering ambiguities ###



### Merging of glyph properties ###


## See also ##

Shaping engines may also want to offer explicit compatibility with
Microsoft Uniscribe, for the purpose of ensuring that users' existing
documents do not break. Therefore, implementors may wish to consult
the Uniscribe compatibility notes.

These compatibilty notes record test-driven observations about
Uniscribe's behavior, and they include any behavior that is a known
bug or a known deviation from specifications. Consequently, the issues
raised by offering Uniscribe compatiblity cannot be considered errata
in the sense that it is described above.
