# Normalization in OpenType shaping #

## Unicode normalization ##

Unicode defines algorithms for normalizing a sequence of input
codepoints into either a canonical composed form or a canonical
decomposed form. The purpose of these algorithms and of the defined
normalization forms is to generate equivalent representations of input
sequences regardless of variations in the order of the input sequences.

For example, a base letter with an attached mark might exist in
Unicode as a single codepoint, but an input sequence might consist of
the base letter codepoint followed by the combining mark
codepoint. Unicode normalization can be used to determine that the
<samp>"Letter, Mark"</samp> sequence is equivalent to the single codepoint. This
simplifies sorting, searching, string comparison, and many other common
tasks.

OpenType shaping utilizes Unicode normalization, but OpenType
shaping has a distinctly different goal: to select the best or most
appropriate representation of the input codepoint sequence that is
available in the active font.


### Unicode equivalence and decomposition

Unicode defines two levels of _equivalence_: "canonical equivalence"
and "compatibility equivalence."

Both of these equivalence relationships are stored as
`Decomposition_Mapping` properties for codepoints in the Unicode
Character Database. In a canonical equivalence relationship, a
codepoint will have a `Decomposition_Mapping` that lists either one or
two other codepoints. In a compatibility equivalence relationship, a
codepoint will instead have a `Decomposition_Mapping` that starts with
a formatting tag which is followed by either one or two other
codepoints.

> Note: Decomposition mappings typically map one input codepoint to
> two output codepoints.
> 
> Decomposition mappings that produce one output codepoint are rare
> and are defined in order to handle particular, uncommon encoding
> circumstances. However, because such mappings exist, shaping engines
> should not assume that all decomposition mappings produce exactly
> two output codepoints.

For shaping purposes, canonical equivalence is generally of greatest
concern. Canonical equivalence defines that sequences such as
<samp>"Letter,Mark"</samp> (a standalone base character followed by a
combining-mark character) are to be treated the same as <samp>"Letter-with-mark"</samp> (a
codepoint that includes both the base and the mark).

The canonical `Decomposition_Mapping`s are required for Unicode
normalization and, even outside of the Unicode normalization
algorithm, help shaping engines make the correct matches between
codepoint sequences and glyphs.

Compatibility equivalence is more akin to defining fallback
relationships, such as defining that a superscript numeral has the
same underlying meaning as the full-size numeral. If the active font
has no glyph for the superscript numeral codepoint, any decision as to
whether substituting the full-size numeral glyph, artifically scaling
the full-size numeral glyph, or displaying a `.notdef` glyph is the 
desirable output is more likely to be a question left up to the
application layer or to the end user, rather than to be handled by the
shaping engine.

However, there may be compatibility equivalence relationships of
significant interest to shaping engines or to other components of a
text-rendering stack. For example, the Arabic Presentation Form
codepoints have defined compatibility equivalences that maps each one
to a codepoint in the Arabic block. Therefore, this information can be
used to enable fallback support for shaping older documents that
include Arabic Presentation Form text runs.


### Unicode normalization forms

Unicode defines four "normalization forms," two of which are focused
on canonical equivalence and two of which are focused on compatibility
equivalence.

The canonical equivalence forms are:

  - Normalization Form D = `NFD`
    - All codepoints have gone through full, recursive canonical
      decomposition
  - Normalization Form C = `NFC`
    - All codepoints have gone through full, recursive canonical
      decomposition, followed by full canonical composition

The compatibility equivalence forms are:

  - Normalization Form KD = `NFKD`
    - All codepoints have gone through full, recursive canonical
      decomposition and full, recursive compatibility decomposition
  - Normalization Form KC = `NFKC`
    - All codepoints have gone through full, recursive canonical
      decomposition and full, recursive compatibility decomposition,
      followed by full canonical composition


### Unicode canonical combining classes

The Unicode `Canonical_Combining_Class` (`Ccc`) property holds a
numerical value for every codepoint. It can be used to sort sequences
into canonical order.

Base letters, other non-mark codepoints, and spacing mark codepoints
will have `Ccc` of `0`, meaning that the codepoint is unaffected by
the reordering algorithm.

Combining marks can have `Ccc` values from `1` to `254`. The
reordering algorithm sorts subsequences of adjacent marks into order
of increasing `Ccc` values.


### Unicode normalization algorithm

The general Unicode normalization algorithm is structured to produce
output in the user's preference between the four normalization
forms. So the steps performed vary based on whether the desired output
is to be in form `NFD`, `NFC`, `NFKD`, or `NFKC`.

> Note: The end goal of OpenType shaping normalization is not to
> produce these Unicode-specified normalization forms, but to produce
> the optimal rendered output. That is why a modified normalization
> algorithm, as described in the next section, is used for shaping
> text.

The general Unicode normalization algorithm applies to all text except
Hangul syllables. It involves three stages:

1. Full decomposition:
  - If `NFD` or `NFC` is the desired output, recursively apply
    canonical decomposition mappings
  - If `NFKD` or `NFKC` is the desired output, recursively apply
    canonical decomposition mappings followed by compatibility
    decomposition mappings

2. Canonical reordering:
  - Sort all subsequences that consist of `Ccc` &gt; `0` codepoints
    into order of increasing `Ccc` value

3. Recomposition, if desired:
  - If either `NFD` or `NFKD` is the desired output, stop.
  - If either `NFC` or `NFKC` is the desired output, apply canonical
    recomposition
   
Canonical recomposition segments the text run into chunks that begin
with <samp>"Starter"</samp> codepoints (which have `Ccc` = `0`) and progressively
tests the subsequent codepoints in the chunk, recombining them, in
order, with the starter whenever all of the following is true:
  - there is a canonical `Decomposition_Mapping` for the
    <samp>"Starter,Subsequent_codepoint"</samp> pair
  - the codepoint of the canonical `Decomposition_Mapping` does not
    have the `Composition_Exclusion` or `Full_Composition_Exclusion`
    properties
  - there are no characters of `Ccc` = `0` or of a higher `Ccc` value
    than the starter between the starter and the subsequent codepoint
	
In conceptual terms, the recomposition algorithm applies the reverse
of the decomposition mappings, except that the now-reordered sequence
may enable different pairings to match first.

The additional test conditions enable pairs to potentially match on
several decomposition mappings in a sequence where one base is
followed by several combining marks that attach at different
positions.

For example, in the fully decomposed and reordered sequence
<samp>"Letter,Mark_1,Mark_2"</samp>, if <samp>"Letter,Mark_1"</samp>
is not part of a canonical 
`Decomposition_Mapping` but <samp>"Letter,Mark_2"</samp> is part of a canonical
`Decomposition_Mapping`, then <samp>"Letter,Mark_2"</samp> will recombine into
<samp>"Letter-and-Mark_2"</samp>, followed by <samp>"Mark_1"</samp>.


### Unicode normalization for Hangul syllables

Hangul syllables can be algorithmically composed and decomposed
because of the strict jamo-ordering of the codepoints that make up the
Hangul Syllables block.

Shaping engines can can use these algorithms to compose sequences of
individual jamo codepoints into precomposed-syllable codepoints, or to
compose individual jamo glyphs into a composite syllable when the
active font does not include a precomposed glyph for the required
syllable.

The algorithm used to normalize Hangul syllables is not related to the
Unicode normalization algorithm used for other scripts. The Hangul
algorithm is described in stage 2 of the [Hangul
shaping](opentype-shaping-hangul.md#stage-2-determining-if-the-syllable-can-be-composed-into-a-hangul-syllables-codepoint) document.



## OpenType shaping normalization ##

Normalization for OpenType shaping closely follows the Unicode
normalization model, but it takes place in the context of a known text
run and a specific active font.

As a result, OpenType shaping takes the text context and available
font contents into account, making decisions intended to result in the
best possible output to the shaping process.


### Goals ###

The OpenType shaping normalization algorithm also decomposes and
reorders the codepoints in a text run. But it differs from Unicode
normalization, particularly at the recomposition stage, in order to
offer the following features useful for shaping engines:

1. Different shaping models can request different preferred formats
   (composed or decomposed) as output
2. Individual decomposition and recomposition mappings will not be
   applied if doing so would result in a codepoint for which the
   active font does not provide a glyph
3. Additional decompositions and recompositions not included in
   Unicode are supported, including the decomposition of multi-part
   dependent vowels (matras) in several Indic and Brahmic-derived
   scripts as well as arbitrary decompositions and compositions
   implemented in `ccmp` and `locl` <abbr title="Glyph Substitution table">GSUB</abbr> lookups


### Shaping model preferences ###

Each shaping model supported by an OpenType shaping engine should
request its preferred normalization form: either fully composed or
fully decomposed.

> Note: in both cases, the preferred normalization form should be
> understood as considering only canonical decomposition mappings, not
> compatibility decomposition mappings.

Which form is preferred for the model primarily depends on the details
of the model, such as whether or not generic Unicode recomposition is
known to interfere with mark positioning, reordering, or other shaping
operations.

Complex shaping models, particularly those which may involve
reordering or the positioning of multi-part marks, tend to prefer
decomposed forms. Nevertheless, deciding which form is preferred for
which model is an implementation decision ultimately left up to the
shaping-engine implementor, who can take speed, complexity, and other
trade-offs into account.

The preferred form may also be specific to a language, such as when a
minority language employs different diacritic ordering than the
ordering encoded in Unicode's <abbr>Ccc</abbr> data. In this case, a font
targetting the minority language may be expected to handle
language-specific mark-to-mark positioning in <abbr title="Glyph Positioning table">GPOS</abbr>; as a result, the
shaping engine should allow for the positioning lookups by designating
a preference for decomposed forms.

Although a generic Unicode normalization implementation would target
the forms defined in Unicode (`NFD`, `NFC`, `NFKD`, or `NFKC`),
OpenType shaping preferred forms are not identical to these Unicode
forms and should not be advertized as being functionally equivalent.

Scripts and languages may also benefit from defining other preferred
forms beyond "fully decomposed" and "fully recomposed." For example,
it might be useful to define a preferred form in which all sequences
of marks are recomposed, but base-and-mark sequences are not
recomposed.


### OpenType shaping normalization algorithm ###

Opentype shaping normalization consists of four main stages.

1. Full decomposition
2. Canonical reordering
3. Selective recomposition
4. Applying font-specific normalization features

Distinctions from Unicode normalization at each stage are described
below.


#### Stage 1: Full decomposition ####

In the first stage, full `NFD` decomposition is performed, as in
Unicode normalization, except for a small set of exceptions required
by specific shapers:

  - recursively apply canonical decomposition mappings, except for:
      - Devanagari <samp>"Rra"</samp>
	  - Bengali <samp>"Rra"</samp> and <samp>"Rha"</samp>
	  - Tamil <samp>"Au"</samp>

After this decomposition, a second set of non-canonical and non-Unicode
mappings is applied:

  - Several scripts (including many covered in the Indic2 shaping
    model, as well as several other Brahmic-derived scripts) include
    multi-part dependent vowel (matra) characters that should be
    decomposed into multiple glyphs, so that those glyphs can be
    independently positioned around base letters.
	
	These additional decompositions are listed in the individual
	script-shaping documents.
	
  - Shaping engines implementing fallback support for older encodings
    should remap those older codepoints to their updated values.
    For example, a shaper that supports text using the Arabic
    Presentation Forms block should remap the Arabic Presentation
    Forms codepoints to the corresponding Arabic-block default
    codepoints and <abbr title="Glyph Substitution table">GSUB</abbr> positional features.
	
	These substitutions are defined in a set of Unicode compatibility
    decomposition mappings.

  - Certain punctuation and symbol codepoints should be remapped, such as
    remapping "non-breaking hyphen" codepoints to "hyphen".
  
Some of these additional decompositions and mappings may also be
implemented in and active font's <abbr title="Glyph Substitution table">GSUB</abbr> lookups, but that is not
guaranteed. Consequently, a normalization function must implement them
in order to fulfill the goal of providing stable output.


#### Stage 2: Canonical reordering ####

In the second stage, mark sequences are reordered into canonical
order:

  - Sort all subsequences that consist of `Ccc` &gt; `0` codepoints
    into order of increasing `Ccc` value

Several script-specific shapers require additional reordering to
compensate for limitations in the Unicode <abbr>Ccc</abbr> mark-reordering
model. For example, several Arabic mark sequences are reordered in
[stage 1](opentype-shaping-arabic.md#stage-1-transient-reordering-of-modifier-combining-marks) of the Arabic
shaping model and [stage 1](opentype-shaping-syriac.md#stage-1-transient-reordering-of-modifier-combining-marks)
of the Syriac shaping model.

These are listed briefly in stage 4, step 4, below, but full
discussion of each case can be found in each script's shaping
document.



#### Stage 3: Selective recomposition ####

The recomposition stage is selective and depends on the form requested
by the shaping model in use:

  - If the shaping model prefers composed forms, then proceed with
    recomposition as described in stage 3, step 1

  - If the shaping model prefers decomposed forms, then proceed with
    the recomposition as described in stage 3, step 2
	

##### Stage 3, step 1: Recomposition for composed-form preference #####

If composed forms have been requested, then proceed as in the Unicode
canonical recomposition algorithm: segment the text run into chunks
that begin with <samp>"Starter"</samp> codepoints (which have `Ccc` = `0`) and
progressively tests the subsequent codepoints in the chunk,
recombining them, in order, with the starter whenever all of the
test conditions are met.

The following test conditions must be true:
  - there is a canonical `Decomposition_Mapping` for the
    <samp>"Starter,Subsequent_codepoint"</samp> pair 
  - the codepoint of the canonical `Decomposition_Mapping` does not
    have the `Composition_Exclusion` or `Full_Composition_Exclusion`
    properties
  - there are no characters of `Ccc` = `0` or of a higher `Ccc` value
    than the starter between the starter and the subsequent codepoint
  - the starter and the subsequent codepoint are not both of `Ccc` = `0`
  - the glyph that results from applying the recomposition exists in
    the active font


##### Stage 3, step 2: Recomposition for decomposed-form preference #####

If decomposed forms have been requested, then a simple check is
performed to cope with any decomposed forms that are absent in the
active font.

Segment the text run into chunks that begin with <samp>"Starter"</samp> codepoints
(which have `Ccc` = `0`) and progressively tests the subsequent
codepoints in the chunk. 

- If there is no standalone glyph for the subsequent codepoint, but
  there is a `Decomposition_Mapping` for the
  <samp>"Starter,subsequent_codepoint"</samp> pair and a glyph exists for the
  recomposed codepoint, 
  then recombine the starter and the subsequent codepoint

<!---
HARFBUZZ logic here: https://github.com/harfbuzz/harfbuzz/src/hb-ot-shape-normalize.cc#L425
--->



#### Stage 4: Normalization-related <abbr title="Glyph Substitution table">GSUB</abbr> features and other font-specific considerations ####

After the decomposition, mark-reordering, and selective
recomposition stages, OpenType shaping normalization also takes
certain <abbr title="Glyph Substitution table">GSUB</abbr> lookups and complex-script shaping operations into
consideration.

These additional operations may produce final output that differs
from Unicode `NFD` and `NFC` forms. However, the output from stage
four should be identical for any two canonically-equivalent input
sequences in the same active font and script/language context.

> Note: the features discussed below are applied after the completion
> of the decomposition, mark-reordering, and recomposition
> stages. Furthermore, they are applied before any other <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr>
> features.
> 
> As a result, shaping engine implementors may choose to
> defer application of these features to the start of <abbr title="Glyph Substitution table">GSUB</abbr> and <abbr title="Glyph Positioning table">GPOS</abbr>
> processing for the sake of convenience.

The `ccmp` and `locl` features can involve normalization, as described
below. If they are present in the active font and match the text run,
all `ccmp` and `locl` features should be applied, and should be
applied in the order in which they are listed in the <abbr title="Glyph Substitution table">GSUB</abbr> table.


##### Stage 4, step 1: ccmp features #####

The `ccmp` feature is applied to all text runs. `ccmp` lookups are not
meant be to be disabled by end users in application code.

`ccmp` lookups can specify arbitrary decomposition mappings and
composition mappings, via one-to-many or many-to-one <abbr title="Glyph Substitution table">GSUB</abbr>
substitutions.

These lookups should be applied regardless of whether
they correspond to the expected decomposition and recomposition
mappings in Unicode, because `ccmp` is font-specific.

A common usage of `ccmp` is to decompose a single codepoint into two
or more glyphs representing discrete components, so that those
components can be more precisely positioned.

For example, many Arabic letters include ijam: dots that, while they
may visually resemble marks, are instead intrinsic components of the
letter and not diacritics. Because the ijam are not marks, a letter
with ijam does not decompose to separate Unicode codepoints. By
decomposing the letter into discrete base and ijam glyphs in `ccmp`, a
font can implement better contextual positioning of the ijam, and can
do so with considerably less work than including numerous alternate
glyphs.

<!--- comment from the HarfBuzz source code that I am not
      certain of the meeting of:
"When a font has a precomposed character for a sequence but the 'ccmp'
feature in the font is not adequate, use the precomposed character
which typically has better mark positioning."
--->


##### Stage 4, step 2: locl features #####

The `locl` feature is applied to text runs based on matching script
and language tags.

When the tags match, any lookups in `locl` are applied by default
during shaping, and these lookups are not meant be to be disabled by
end users in application code.

`locl` lookups often implement simple one-to-one substitutions to
replace default glyph forms with alternate shapes preferred in the
language/script combination.

However, `locl` lookups may also interact with normalization by
performing decompositions or compositions. These substitutions are
often used to preserve orthographic or linguistic features that are
not fully captured by Unicode normalization forms or <abbr>Ccc</abbr> ordering.

For example, in the Turkish alphabet, "dotted i" and "dotless i" are
two distinct letters. For runs of text in Turkish, a font may
deliberately substitute a generic "i" glyph with "dotted i" or the "i,
dot diacritic" sequence with `locl` lookups in order to ensure that
the dot diacritic is not lost as text is processed.

Or, for example, in a particular script and language pairing, readers
might expect or prefer certain sequences of diacritics to stack in a
different order than the order their Unicode <abbr>Ccc</abbr> values dictate. A
`locl` lookup could be used to implement the preferred reordering in a
many-to-one <abbr title="Glyph Substitution table">GSUB</abbr> substitution.



##### Stage 4, step 3: Variation Selectors #####

Unicode defines _standardized_variation_sequences_ as sequences of two
codepoints where the first codepoint is any base character or mark,
and the second character is a Variation Selector. Mapping a
standardized variation sequence to a glyph is not done via <abbr title="Glyph Substitution table">GSUB</abbr>,
however, but in the `cmap` table of a font.

Unicode normalization does not consider Variation Selector
codepoints.

When performing OpenType shaping normalization, however, if the
<samp>"_letter_,Variation Selector"</samp> is not mapped to a glyph in the active
font, a shaping engine may prefer to drop the Variation Selector
codepoint and render the default form of the character or to replace
the sequence with a `.notdef` glyph. Which option is preferred may be
language- or script-specific.


#### Stage 4, step 4: Interaction with script-specific shaping models ####

Reordering and composition are defined as shaping operations in
several script-specific shaping models. In some cases, a reordering
operation or composition may be designated by a particular <abbr title="Glyph Substitution table">GSUB</abbr> or
<abbr title="Glyph Positioning table">GPOS</abbr> feature tag.

Shaping-engine implementors should take care to note where completing
normalization early in the shaping process may reduce the need for
applying such operations later.

For example, in the Indic2 shaping model, sequences of marks are
reordered in stage 2, step 4. But this reordering is identical to the
Unicode canonical reordering, so a shaping-engine implementation that
normalizes all text runs before starting the Indic2 shaping process
will not need to perform any reordering at that step — assuming that
the Indic2 shaping model is configured to prefer decomposed forms.

Similarly, in stage 3, step 2 of the Indic2 shaping model, the `nukt`
feature composes <samp>"Base,Nukta"</samp> sequences into <samp>"Base-and-Nukta"</samp>
glyphs. A shaping engine that designates the Indic2 shaping model as
preferring composed forms could, therefore, have such <samp>"Base,Nukta"</samp>
sequences recomposed during Unicode normalization. However, such a
recomposition preference would likely cause other problems, such as
the unwanted recomposition of multi-part dependent vowels (matras).

Script-specific shaping models can also involve special exceptions to
the generic composition and reordering process of normalization. For
example:

  - In the Hebrew shaper, stage 2, Hebrew Alphabetic Presentation
    Forms, if available in the active font, are composed.

  - In the Arabic shaping model, stage 1, and in the Syriac shaping
    model, stage 1, certain marks are reordered after normalization
    and after <abbr title="Glyph Substitution table">GSUB</abbr> feature application.

  - In Bengali, <samp>"Ya,Nukta"</samp> is composed into <samp>"Yya"</samp> before <abbr title="Glyph Substitution table">GSUB</abbr> feature
    application, to avoid potential ambiguities during the application
    of later features.


#### Compatibility decompositions ####

As was mentioned in stage 1 of the OpenType shaping normalization
algorithm, the codepoints in the Arabic Presentation Forms blocks
have Unicode compatibility `Decomposition_Mapping`s that a shaping
engine can use to map codepoints from Arabic Presentation Forms to
codepoints in the Arabic block. Each Arabic Presentation Form
`Decomposition_Mapping` is tagged with a positional tag corresponding
to a positional <abbr title="Glyph Substitution table">GSUB</abbr> feature: `<final>`, `<initial>`,`<isolated>`, or
`<medial>`.

This tag information can be used to construct a set of synthetic <abbr title="Glyph Substitution table">GSUB</abbr>
lookups corresponding to `fina`, `init`, `isol`, and `medi`. However,
shaping engines should take care not to offer guarantees about the
expect output, unless explicit support for older files known to be
encoded with Arabic Presentation Forms codepoints is desired.

Similarly, several other compatibility `Decomposition_Mapping` tags
could theoretically be exploited to enable some level of fallback
support for shaping codepoints when the necessary glyphs are missing
in the active font, such as mapping `<fraction>` decompositions to
`frac`, `<super>` decompositions to `sups`,  `<sub>` to `subs` or
`sinf`, or `<compat>` to various generic list-item delimiter
sequences.

All such decompositions, however, should be implemented as
fallbacks and the decision to employ them is best left up to the
application layer or end user's preferences.
