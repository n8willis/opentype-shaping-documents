# Emoji shaping in OpenType #

This document details the default shaping procedure needed to shape
emoji sequences.


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Normalization](#normalization)
  - [Sequence identification](#sequence-identification)
  - [The default shaping model](#the-default-shaping-model)
  
  
  
## General information ##

The emoji OpenType shaping model is used for correctly displaying
sequences from the Emoji block in Unicode as well as for numerous
emoji codepoints found in other blocks.

Emoji codepoints originated from a variety of pre-Unicode standards,
including mobile-phone carriers in Japan, from typographic characters
sets such as Zapf Dingbats and Wingdings, and from various symbols in
common usage.

Emoji shaping follows the default OpenType shaping model used for
scripts that are considered _non-complex_ from the shaper's
perspective. However, emoji fonts typically use GSUB tables to
implement a variety of OpenType smart features, including several
classes of ligature, contextual alternates, or variant forms to
support emoji sequences.

In addition to standalone image glyphs, emoji shaping is also used to
display flag sequences and "keycap" sequences, both of which involve a
combination of emoji and non-emoji codepoints in order.

The default emoji glyph for a given codepoint may be substituted by
the addition of selectors, modifiers, or joiners after the emoji
codepoint.

Many of these emoji sequences carry important semantic meaning,
such as specifying gender, skin tone, object colors, and
directions. Shaping engines should therefore make a best effort to
correctly identify and display these sequences.

Fallback presentation is possible for some emoji sequences by
displaying the sequence of default emoji glyphs for the
codepoints. For other emoji sequences, however, the most appropriate
fallback approach is less clearly defined and may vary between
implementations.

Emoji glyphs may be stored in any of several color formats, or in any
of the monochrome Bézier formats typically used for standard text
codepoints. Correctly retrieving and displaying the glyph data for
the format used by the active font is outside the scope of this
document.

> Note: "shortcut codes" for emoji like `:smile:` are text mark-up
> and are _not_ handled by OpenType shaping. The set of shortcut codes
> supported by any particular application is specific to that
> application alone.
>
> Text-processing stacks typically support a set of shortcut codes
> that includes Unicode's official `Short_Name` property from the CLDR
> database, plus additional shortcodes, but the shortcut-code mapping
> is not otherwise linked to Unicode data.

Runs of emoji might be tagged with the `<Zsye>` or `<Zsym>` script
subtags, or with the `-em-emoji`, `-em-text`, or `-em-default` locale
extensions. However, these subtags and extensions are primarily
intended to control which presentation form is preferred by the
application, and must not be relied on for the purpose of identifying
emoji.



## Terminology ##

A codepoint is considered an **emoji** only if it has the `Emoji`
property in the Unicode Character Database (UCD). Although many
codepoints that have this property are pictographic in nature, some
codepoints that are pictographic do not have the `Emoji` property
(such as most chess, playing-card, and game-piece symbols), and some
codepoints that do have the `Emoji` property show typographic
characters rather than pictographic images.

All emoji codepoints — as well as several non-emoji codepoints — have
the `Extended_Pictographic` property. When a non-emoji codepoint has
the `Extended_Pictographic` property, this indicates that future
revisions of Unicode may incorporate the codepoint in a valid emoji
sequence, or may (for a currently-unassigned codepoint) assign an
emoji character to the codepoint.

The emoji codepoints also include two distinct sets of alphanumeric
character codepoints that are used to implement specific substitution
sequences.

The **regional indicator** set includes the 26 lower-case
Basic Latin letters ("a" to "z"), which are used to support the
predefined set of regional flags. The regional indicator set is found
within the Enclosed Alphanumeric Supplement block of Unicode.

The **tag character** set includes codepoints that correspond to the
printable characters in the ASCII set, as well as an "End" control
tag. The tag characters are used to support a more general mechanism
for local and sub-national flags that are not covered by the
predefined regional-indicator flag set. The tag characters set is
found within the Tags block of Unicode.

**Presentation style** describes whether an emoji codepoint is
shown in emoji style (for example, with a full-color bitmap or SVG
glyph) or text style (such as a monochrome, Bézier glyph). Every emoji
codepoint defaults to either emoji-style or text-style
presentation.

An emoji codepoint might be followed by a **presentation selector**.
This selector requests that either emoji-style or text-style be used
for the preceding emoji codepoint, potentially overriding that
codepoint's default. There are two presentation selectors:

  - `Variation Selector 15` (VS15, `U+FE0E`) requests text
    presentation style.
  - `Variation Selector 16` (VS16, `U+FE0F`) requests emoji
    presentation style.

An emoji codepoint might also be followed by an emoji
**modifier**. This modifier requests an alternate version of the emoji
glyph. Currently, there are five emoji modifiers defined, all of which
are assigned to a skin-tone designation from the Fitzpatrick scale:

  - `U+1F3FB` "Light skin tone"
  - `U+1F3FC` "Medium-light skin tone"
  - `U+1F3FD` "Medium skin tone"
  - `U+1F3FE` "Medium-dark skin tone"
  - `U+1F3FF` "Dark skin tone"


Emoji **sequences** consist of one or more emoji codepoints,
optionally followed by presentation selectors, modifiers, or other
special characters. A font can implement custom ligatures for any
sequence of emoji. However, Unicode also designates specific sequences
that should be supported. These sequences can involve two special
codepoints in addition to the selectors and modifiers mentioned above:

  - The Combining Enclosing Keycap (CEK, `U+20E3`) is used to form
    **keycap** sequences corresponding to telephone keypad keys.

  - The Zero-Width Joiner (ZWJ, `U+200D`) is used to form emoji
    sequences for multi-person groups, gendered forms, hair-color
    variants, and directionality.



## Normalization ##

Emoji sequences are not generally affected by Unicode or OpenType
normalization. However, Unicode does specify an order to be used when
representing ZWJ-using emoji sequences.

The correct order should be:

    Base emoji codepoint
	Emoji modifier OR Emoji presentation selector
	Hair subsequence
	Color subsequence
	Gender-sign or object subsequence
	Directionality indicator


Although this ordering is not designated a Unicode normalization form,
shaping engine implementers may find it a useful target if attempting
to correct invalid mis-ordered emoji ZWJ sequences.

Shaping engines should also note that the `Emoji` and
`Extended_Pictographic` properties may require tracking in any Unicode
normalization routines.

The `Emoji` property of a codepoint can be unintentionally lost when
certain string transformations are performed. For example, the
upper-case versions of the Circled Latin Letters have the `Emoji`
property, but the lower-case version of the Circled Latin do
not. Therefore, a case-transformation rule must take care not to
unintentionally break the desired output by losing the property.

The `Extended_Pictographic` property of a codepoint should be tracked
because it is set on several non-emoji codepoints that may be updated
to have the `Emoji` property in a future release of Unicode.

Furthermore, Unicode does define the full set of emoji sequences that
should be expected under the predefined set of base emoji and valid
emoji sequences. This is designated the "Recommended for General
Interchange" (RGI) set and can be tracked with the `RGI_Emoji`
property. Fonts are not required to implement the entire RGI set.



## Sequence identification ##

There are six varieties of emoji sequence defined by Unicode:

1. Presentation sequences
2. Modifier sequences
3. Regional Indicator flag sequences
4. Tag flag sequences
5. Keycap sequences
6. Zero-width joiner (ZWJ) sequences

> Note: The ZWJ sequence variety incorporates several subsets, but all
> of the ZWJ sequences are implemented using the same mechanism.

This set includes the major categories of sequences that shaping
engines are likely to encounter and that can convey important
contextual information to users. Note, however, that fonts may
implement additional sequences via ligature substitution or other
existing mechanisms.

Sequences should be identified by examining the run and matching
characters, based on their categorization, using regular expressions. 

The following general-purpose identifcation classes can be used to
match emoji sequences in regular expressions.

```markdown
_emoji_             = `EMOJI`
_modifier_          = "U+1F3BF" | "U+1F3CF" | "U+1F3DF" | "U+1F3EF" | "U+1F3FF"
_presentation_      = `VS15` | `VS16`
_zwj_               = `ZWJ`
_cek_               = `CEK`
_blackflag_         = "U+1F3F4"
_key_               = "#" | "*" | ["0".."9"]
_color_             = "U+2B1B" | "U+2B1C" | "U+1F7E5" | "U+1F7E6" | "U+1F7E7" | "U+1F7E8" | "U+1F7E9" | "U+1F7EA" | "U+1F7EB"
_multipersongroup_ = "U+1F91D" | "U+1F46F" | "U+1F93C" | "U+1F46B" | "U+1F46C" | "U+1F46D" | "U+1F48F" | "U+1F491" | "U+1F46A"
_gendersign_        = "U+2640" | "U+2642"
_genderperson_      = "U+1F468" | "U+1F469" | "U+1F9D1"
_hairstyle_         = "U+1F9B0" | "U+1F9B1" | "U+1F9B2" | "U+1F9B3"
_direction_         = "U+2B05" | "U+27A1"
_regionalindicator_ = `REGIONAL_INDICATOR`
_tagchar_           = `TAG_CHARACTER`
_endtag_            = "U+E007F"
```

The expressions below use state-machine syntax from the Ragel
state-machine compiler. The operators represent:

```markdown
a* = zero or more copies of a
b+ = one or more copies of b
c? = optional instance of c
d{n} = exactly n copies of d
d{,n} = zero to n copies of d
d{n,} = n or more copies of d
d{n,m} = n to m copies of d
!e = not e
^f = character-level not f
g.h = concatenation of g and h
i|j = i or j
( ) = grouping of expression elements
```


### Presentation sequences ###

A presentation sequence is used to request a specific presentation
style ("text" or "emoji"), potentially overriding the default
presentation style of the codepoint.

A presentation sequence must match:

```markdown
_emoji_ _presentation_
```


### Modifier sequences ###

A modifier sequence is used to request an alternate glyph for an emoji
codepoint. 

A modifier sequence must match:

```markdown
_emoji_ _modifier_
```

Currently, there are five emoji modifier codepoints defined by
Unicode. Each corresponds to a different human skin-tone based on the
Fitzpatrick scale. Fonts are expected to implement modifier sequences
for emoji codepoints that depict human beings, and are expected not to
implement modifier sequences for other emoji codepoints.

Modifier sequences use emoji presentation style by default, and cannot
include a presentation selector. However, an implementation may choose
to display text-presentation versions of sequences if emoji
presentation style is not possible in the environment.



### Regional Indicator flag sequences ###

A Regional Indicator flag sequence is used to request a flag
emoji. All Regional Indicator flag sequences are two codepoints long,
using codepoints from the `REGIONAL_INDICATOR` alphabetical set.

A Regional Indicator flag sequence must match:

```markdown
_regionalindicator_ _regionalindicator_
```

In addition, the only two-codepoint sequences that are considered
valid Regional Indicator flag sequences are those that correspond to
the `unicode_region_subtag` field in the CLDR database.

Regional Indicator flag sequences use emoji presentation by default,
and cannot include a presentation selector.  However, an
implementation may choose to display text-presentation versions of
sequences if emoji presentation style is not possible in the
environment.



### Tag flag sequences ###

A Tag flag sequence is used to request a flag emoji for any flag not
defined by the Regional Indicator flag sequence mechanism.

A Tag flag sequence must match:

```markdown
_blackflag_ _tagchar_+ _endtag_
```



### Keycap sequences ###

A Keycap sequence is used to request an emoji that depicts a
telephone-keypad button.

A Keycap sequence must match:

```markdown
_key_ _presentation_ _cek_
```


### ZWJ sequences ###

A Zero-Width Joiner (ZWJ) sequence can be used to request specific
variants of an emoji glyph or to request the combined form of a
sequence of emoji glyphs.

Because the ZWJ codepoint itself is invisible, users will expect ZWJ
sequences to fall back gracefully as sequences of standalone emoji
glyphs that convey the original meaning. For example, a ZWJ
multi-person group sequence would be rendered as a single multi-person
emoji glyph if one is available in the active font, but would fall
back to a set of individual-person emoji glyphs.


#### ZWJ multi-person group sequences ####

A ZWJ multi-person group sequence is used to request a multi-person
emoji glyph. The fallback for a ZWJ multi-person group sequence is a
sequence of individual-person emoji glyphs.

A ZWJ multi-person group sequence must match:

```markdown
_emoji_ ( _zwj_ _emoji_ ){1,3}
```


#### ZWJ role sequences ####

A ZWJ role (or profession) sequence is used to request a
specific-gendered version of an emoji codepoint that depicts a human
being performing a task or job. The fallback for a ZWJ role sequence
is a generic "person" emoji followed by an emoji depicting a task or job.

A ZWJ role sequence must match:

```markdown
_genderperson_ _zwj_ _emoji_
```

#### ZWJ gendered person sequences ####

A ZWJ gendered person sequence is used to request a specific-gendered
version of an emoji codepoint that depicts a single human being. The
fallback for a ZWJ gendered person sequence is a generic "person"
emoji followed by a gender symbol.

A ZWJ gendered person sequence must match:

```markdown
_emoji_ _zwj_ _gendersign_
```

#### ZWJ hair sequences ####

A ZWJ hair sequence is used to request a specific hairstyle version of
an emoji codepoint that depicts a single human being.

A ZWJ hair sequence must match:

```markdown
_emoji_ _zwj_ _hairstyle_
```

#### ZWJ directionality sequences ####

A ZWJ directionality sequence is used to request a version of an emoji
codepoint facing a specific cardinal direction.

A ZWJ directionality sequence must match:

```markdown
_emoji_ _zwj_ _direction_ _presentation_
```

#### ZWJ additional sequences ####


### Other sequences and ligatures ###










## The default shaping model ##

Emoji should be shaped using the
[default](opentype-shaping-default.md) shaping model. 

Processing a run of text in the default shaping model involves three
top-level stages:

1. Applying the basic substitution features from GSUB
2. Applying typographic substitution features from GSUB
3. Applying the positioning features from GPOS

Emoji sequences as described above will generally be implemented in
the active font as a GSUB lookup feature. However, there are no
definitively invalid GSUB or GPOS features that must or must _not_ be
employed for this purpose.

Consequently, shaping engines should not assume (for example) that
emoji sequences will be implemented in the `liga` feature of GSUB.

A font may also employ contextual features, such as using `locl`, that
affects the emoji glyph shown, or use GPOS positioning for some emoji
glyphs. 


<!---
Uses DEFAULT shaping; replicate that but describe emojiness

presentation -  text-default vs emoji-default vs text-only = VS15 or VS16
- locale extension "-em": -em-emoji, -em-text, -em-default
- script codes Zsye (emoji preferred), Zsym (text preferred)
- there are characters that have the `Extended_Pictographic` UCD
property but which are not emoji because they lack the `Emoji`
property

emoji and text presentation sequences = "emoji,selector"

FALLBACK ??

modifiers = skintone
- fallback recommended to shown skintone patch, even though modifier
  not normally visible codepoint??

emoji sequences - flags, keycaps, possibly zwj & multi-person?
- Regional Indicators Symbols: alphabetic char codepoints; sequences
  produce flags
  - might produce flags OR as a 'country code'
  - limited to predefined list; has some deprecated code (eg, east germany)
  - shaping: flags have different aspect ratios and may therefore need
    to be padded if it is desirable to preserve equal widths.
  - HB trickiness:
    https://github.com/harfbuzz/harfbuzz/commit/2b0ced28b685de4edbd22cf5f59be30075984dfb
	https://github.com/harfbuzz/harfbuzz/issues/2265
- keycap sequences
  - separate block of base alphanumeric(?) chars
- tag sequences: flags again? is this a subset??
  - extends region-sequences to sub-national-level
  - uses 'tag characters' rather than regional-indicator codepoints;
    separate alphanumeric block
  - there is a predefined list that seems to support sub-UK only; technically different from 'flag
    sequences'
- modifier sequences
  - used for skintone
- ZWJ sequences
  - "family" used for multi-person emojis; I guess these decompose to sequences
  of individual emoji if the combo is not supported
  - "role" used for gender+job,etc
  - "gendered" used for activities+gender+skintone or
    action(shrug,frown)+gender+skintone
  - "hair"
  - "other" = misc; heart-on-fire, pirate flag; 13 named.

emoji ligatures can exist for codepoints outside the predefined ones
(like flags) so shaping engines should not assume otherwise.

--->
