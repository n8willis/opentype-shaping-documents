# Universal Shaping Engine script shaping in OpenType #

This document details the default shaping procedure needed to display
text runs in scripts supported by the Universal Shaping Engine (<abbr>USE</abbr>)
model. 


**Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
  - [The <abbr>USE</abbr> shaping model](#the-use-shaping-model)
      - [Stage 1: Split vowel decomposition](#stage-1-split-vowel-decomposition)
      - [Stage 2: Cluster identification](#stage-2-cluster-identification)
      - [Stage 3: Basic cluster formation](#stage-3-basic-cluster-formation)
	      - [Stage 3, step 1: Applying the basic pre-processing features from <abbr>GSUB</abbr>](#stage-3-step-1-applying-the-basic-pre-processing-features-from-gsub)
          - [Stage 3, step 2: Applying the basic reordering features from <abbr>GSUB</abbr>](#stage-3-step-2-applying-the-basic-reordering-features-from-gsub)
          - [Stage 3, step 3: Applying the basic orthographic features from <abbr>GSUB</abbr>](#stage-3-step-3-applying-the-basic-orthographic-features-from-gsub)
	  - [Stage 4: Glyph reordering](#stage-4-glyph-reordering)
	      - [Stage 4, step 1: Applying the reordering features from <abbr>GSUB</abbr>](#stage-4-step-1-applying-the-reordering-features-from-gsub)
	      - [Stage 4, step 2: Performing property-based reordering moves](#stage-4-step-2-performing-property-based-reordering-moves)
	  - [Stage 5: Final feature application](#stage-5-final-feature-application)
	      - [Stage 5, step 1: Applying the final topographic features from <abbr>GSUB</abbr>](#stage-5-step-1-applying-the-final-topographic-features-from-gsub)
	      - [Stage 5, step 2: Applying the final typographic-presentation features from <abbr>GSUB</abbr>](#stage-5-step-2-applying-the-final-typographic-presentation-features-from-gsub)
	      - [Stage 5, step 3: Applying the final positioning features from <abbr>GPOS</abbr>](#stage-5-step-3-applying-the-final-positioning-features-from-gpos)
  
  
  
## General information ##

The Universal Shaping Engine (<abbr>USE</abbr>) model is used for complex scripts
that are not already supported by a dedicated OpenType shaping
model. 

"Complex" scripts, in OpenType shaping terminology, are scripts that
require some combination of glyph reordering, contextual joining
behavior, or the substitution of context-dependent forms for
linguistic or orthographic correctness.

The scripts covered by this model include Javanese, Balinese,
Buginese, Batak, Chakma, Lepcha, Modi, Phags-pa, Tagalog, Siddham,
Sundanese, Tai Le, Tai Tham, Tai Viet, and many others.

In many ways, the <abbr title="Universal Shaping Engine">USE</abbr> model is a generalization of the
[Indic2](opentype-shaping-indic-general.md) OpenType 
shaping model, with adjustments made to correct shortfalls encountered
when using the Indic2 shaping model, as well as additional changes
designed to broaden the number of scripts that can be supported. For
example, the <abbr title="Universal Shaping Engine">USE</abbr> model includes a step applying contextual
joining-behavior features as is performed in the Arabic-like shaping
model. 

> Note: The term _Indic3_ is sometimes used in comparison to Indic2
> (or the corresponding increment of the script tags for existing
> OpenType shaping models, such as `<dev3>` in comparison to
> `<dev2>`).
>
> This terminology either indicates that a shaping engine has
> implemented support for one or more of the Indic2 scripts within the
> <abbr title="Universal Shaping Engine">USE</abbr> model or it is merely a conversational convention to discuss
> support for the Indic2-model scripts in <abbr title="Universal Shaping Engine">USE</abbr>.
>
> At the present time, there is no formal definition for an Indic3
> model, and there are not registered OpenType script tags for
> `<dev3>` or any other third generation of the scripts handled by the
> Indic2 model.

<abbr title="Universal Shaping Engine">USE</abbr> was introduced after the release of version 8.0 of the Unicode
specification. The intent is for <abbr title="Universal Shaping Engine">USE</abbr> to support complex scripts added
to future Unicode releases in addition to those already supported.


## Terminology ##

The <abbr title="Universal Shaping Engine">USE</abbr> shaping model uses a standard set of terms for the features of
supported scripts. These terms are similar to the standard terms used
for Indic scripts, but with several key distinctions.

A **cluster** is the fundamental unit used in shaping; it consists of
a sequence of Unicode codepoints that will be processed as an atomic
unit. An individual syllable typically corresponds to a single
cluster, but any particular cluster might involve multiple syllables
or a sequence that does not match the syllable-formation rules of the
script.

A **base** character in the <abbr title="Universal Shaping Engine">USE</abbr> model may be a consonant, an
independent vowel, a number, or any of several additional character
classes.

A cluster's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
cluster frequently take on secondary forms. Different <abbr title="Glyph Substitution table">GSUB</abbr>
substitutions may apply to a script's **pre-base** and **post-base**
consonants. Some of these substitutions create **above-base** or
**below-base** forms. The **Reph** form of the consonant "Ra" is an
example.

A **vowel** character in the <abbr title="Universal Shaping Engine">USE</abbr> model is a dependent vowel or any of
several additional marks with similar behavior. This class is similar
to the "matra" class used in Indic shaping.

**Halant** is the standard term for a "vowel-killer" sign.


## Glyph classification ##

The <abbr title="Universal Shaping Engine">USE</abbr> shaping model classifies characters based on a specific set of
properties defined for each codepoint in the Unicode Character
Database (<abbr>UCD</abbr>), augmented with a small set of pre-defined property
overrides.

The <abbr title="Unicode Character Database">UCD</abbr> properties used for <abbr title="Universal Shaping Engine">USE</abbr> character classification are:

	Unicode General Category (UGC)
	Unicode Indic Syllabic Category (UISC)
	Unicode Indic Positional Category (UIPC)

In addition, the Unicode Character Decomposition Mapping (<abbr>UCDM</abbr>) is used for
all split vowels.


### <abbr>USE</abbr> overrides ###

Although, in general, the <abbr title="Universal Shaping Engine">USE</abbr> shaping model relies on the <abbr title="Unicode General Category">UGC</abbr>, <abbr title="Unicode Indic Syllabic Category">UISC</abbr>,
and <abbr title="Unicode Indic Positional Category">UIPC</abbr> properties, the <abbr title="Universal Shaping Engine">USE</abbr> model makes a small set of standardized
overrides to the properties of certain specific characters.

The following table lists the complete set of <abbr title="Universal Shaping Engine">USE</abbr> overrides. Shaping
engines should implement the override properties in order to guarantee
correct results.

> Note: A _null_ in the following table indicates that the
> corresponding Unicode property is not overridden for the codepoint
> featured in that row. 


:::{table} Property overrides for <abbr>USE</abbr> shaping


| Codepoint | Unicode UISC               | USE override UISC | Unicode UIPC | USE override UIPC | Glyph                                   |
|:----------|:---------------------------|:------------------|:-------------|:------------------|:----------------------------------------|
| `U+AA29`  | Vowel_Dependent            | Bindu             | _null_       | _null_            | &#xAA29; Cham Vowel Sign Aa             |
| `U+0F71`  | Vowel_Dependent            | Nukta             | _null_       | _null_            | &#x0F71; Tibetan Vowel Sign Aa          |
| `U+A982`  | Consonant_Succeeding_Repha | Tone_Mark         | _null_       | _null_            | &#xA982; Javanese Sign Layar            |
| `U+0F7F`  | Visarga                    | Consonant_Dead    | _null_       | _null_            | &#x0F7F; Tibetan Sign Rnam Bcad         |
| `U+11134` | Pure_Killer                | Gemination_Mark   | _null_       | _null_            | &#x11134; Chakma Maayyaa                |
| `U+0F74`  | _null_                     | _null_            | Bottom       | Top               | &#x0F74; Tibetan Vowel Sign U           |
| `U+AA35`  | _null_                     | _null_            | Bottom       | Top               | &#xAA35; Cham Consonant Sign            |
| `U+1A18`  | _null_                     | _null_            | Bottom       | Top               | &#x1A18; Buginese Vowel Sign U          |
| `U+0F72`  | _null_                     | _null_            | Top          | Bottom            | &#x0F72; Tibetan Vowel Sign I           |
| `U+0F7A`  | _null_                     | _null_            | Top          | Bottom            | &#x0F7A; Tibetan Vowel Sign E           |
| `U+0F7B`  | _null_                     | _null_            | Top          | Bottom            | &#x0F7B; Tibetan Vowel Sign Ee          |
| `U+0F7C`  | _null_                     | _null_            | Top          | Bottom            | &#x0F7C; Tibetan Vowel Sign O           |
| `U+0F7D`  | _null_                     | _null_            | Top          | Bottom            | &#x0F7D; Tibetan Vowel Sign Oo          |
| `U+0F80`  | _null_                     | _null_            | Top          | Bottom            | &#x0F80; Tibetan Vowel Sign Reversed Ii |
| `U+11127` | _null_                     | _null_            | Top          | Bottom            | &#x11127; Chakma Vowel Sign A           |
| `U+11128` | _null_                     | _null_            | Top          | Bottom            | &#x11128; Chakma Vowel Sign I           |
| `U+11129` | _null_                     | _null_            | Top          | Bottom            | &#x11129; Chakma Vowel Sign Ii          |
| `U+1112D` | _null_                     | _null_            | Top          | Bottom            | &#x1112d; Chakma Vowel Sign Ai          |
| `U+11130` | _null_                     | _null_            | Top          | Bottom            | &#x11130; Chakma Vowel Sign Oi          |
| | | | | | |
:::


### <abbr>USE</abbr> classification table ###

The following table lists the classes utilized in the <abbr title="Universal Shaping Engine">USE</abbr> shaping
model, along with a definition for each class. The class definitions
refer to the <abbr title="Unicode General Category">UGC</abbr>, <abbr title="Unicode Indic Syllabic Category">UISC</abbr>, and <abbr title="Unicode Indic Positional Category">UIPC</abbr> categories in the Unicode standard,
or to specific Unicode codepoints.

The symbols given in the "Symbol" column for each class may be used to
express cluster-matching rules or other algorithms.

Vowels and modifiers may be further subclassified as described in the
[<abbr title="Universal Shaping Engine">USE</abbr> subclasses table](#use-subclasses-table) below.


:::{table} Class definitions for <abbr>USE</abbr> shaping

| USE classification        | Symbol | Definition                                                                                                    |
|:--------------------------|:-------|:--------------------------------------------------------------------------------------------------------------|
| BASE                      | `B`    | UISC = Number _or_ (UISC = Avagraha & UGC = Lo) _or_ (UISC = Bindu & UGC = Lo) _or_ UISC = Consonant _or_ (UISC = Consonant_Final & UGC = Lo) _or_ UISC = Consonant_Head_Letter _or_ (UISC = Consonant_Medial & UGC = Lo) _or_ (UISC = Consonant_Subjoined & UGC = Lo) _or_ UISC = Tone_Letter _or_ (UISC = Vowel & UGC = Lo) _or_ UISC = Vowel_Independent _or_ (UISC = Vowel_Dependent & UGC = Lo) |
| Combining grapheme joiner | `CGJ`  | `U+034F`                                                                                                      |
| CONS_MOD                  | `CM`   | UISC = Nukta _or_ Gemination_Mark _or_ Consonant_Killer                                                       |
| CONS_WITH_STACKER         | `CS`   | UISC = Consonant_With_Stacker                                                                                 |
| CONS_FINAL                | `F`    | (UISC = Consonant_Final & UGC != Lo) _or_ UISC = Consonant_Succeeding_Repha                                   |
| CONS_FINAL_MOD            | `FM`   | UISC = Syllable_Modifier                                                                                      |
| BASE_OTHER                | `GB`   | UISC = Consonant_Placeholder _or_ `U+2015`, `U+2022`, `U+25FB`–`U+25FE`                                       |
| HALANT                    | `H`    | UISC = Virama _or_ Invisible_Stacker                                                                          |
| HALANT_NUM                | `HN`   | UISC = Number_Joiner                                                                                          |
| BASE_IND                  | `IND`  | (UISC = Consonant_Dead _or_ Modifying_Letter) _or_ (UGC = Po != `U+104E`, `U+2022`) _or_ `U+002D`             |
| CONS_MED                  | `M`    | UISC = Consonant_Medial & UGC != Lo                                                                           |
| BASE_NUM                  | `N`    | UISC = Brahmi_Joining_Number                                                                                  |
| OTHER                     | `O`    | Any other SCRIPT_COMMON characters; White space characters, UGC=Zs                                            |
| REPHA                     | `R`    | UISC = Consonant_Preceding_Repha _or_ Consonant_Prefixed                                                      |
| Reserved character        | `Rsv`  | Any character not currently assigned or otherwise reserved in Unicode                                         |
| SYM                       | `S`    | UGC = Sc _or_ (UGC = So & != `U+25CC`)                                                                        |
| SYM_MOD                   | `SM`   | `U+1B6B`, `U+1B6C`, `U+1B6D`, `U+1B6E`, `U+1B6F`, `U+1B70`, `U+1B71`, `U+1B72`, `U+1B73`                      |
| CONS_SUB                  | `SUB`  | UISC = Consonant_Subjoined & UGC != Lo                                                                        |
| VOWEL                     | `V`    | (UISC = Vowel & UGC != Lo) _or_ (UISC = Vowel_Dependent & UGC != Lo) _or_ UISC = Pure_Killer                  |
| VOWEL_MOD                 | `VM`   | (UISC = Bindu & UGC != Lo) _or_ UISC = Tone_Mark _or_ Cantillation_Mark _or_ Register_Shifter _or_ Visarga    |
| VARIATION_SELECTOR        | `VS`   | `U+FE00`‒`U+FE0F`                                                                                             |
| Word joiner               | `WJ`   | `U+2060`                                                                                                      |
| Zero width joiner         | `ZWJ`  | UISC = Joiner                                                                                                 |
| Zero width nonjoiner      | `ZWNJ` | UISC = Non_Joiner                                                                                             |
| | | |
:::


### <abbr>USE</abbr> subclasses table ###

Vowels and modifiers may be further subclassified based on their
position relative to base characters. The subclasses incorporated in
the <abbr title="Universal Shaping Engine">USE</abbr> shaping model are defined in the table below.

Split-vowel subclasses are not assigned a symbol because each split
vowel must be decomposed into its components.


:::{table} Subclasses for <abbr>USE</abbr> shaping

| USE classification     | Symbol  | Definition                                                              |
|:-----------------------|:--------|:------------------------------------------------------------------------|
| CONS_MOD_ABOVE         | `CMAbv` | USE=CM & UIPC = Top                                                     |
| CONS_MOD_BELOW         | `CMBlw` | USE=CM & UIPC = Bottom                                                  |
| CONS_FINAL_ABOVE       | `FAbv`  | USE=F & UIPC = Top                                                      |
| CONS_FINAL_BELOW       | `FBlw`  | USE=F & UIPC = Bottom                                                   |
| CONS_FINAL_POST        | `FPst`  | USE=F & UIPC = Right                                                    |
| CONS_MED_ABOVE         | `MAbv`  | USE=M & UIPC = Top                                                      |
| CONS_MED_BELOW         | `MBlw`  | USE=M & UIPC = Bottom                                                   |
| CONS_MED_PRE           | `MPre`  | USE=M & UIPC = Left                                                     |
| CONS_MED_POST          | `MPst`  | USE=M & UIPC = Right                                                    |
| SYM_MOD_ABOVE          | `SMAbv` | `U+1B6B`,`U+1B6D`,`U+1B6E`,`U+1B6F`,`U+1B70`,`U+1B71`,`U+1B72`,`U+1B73` |
| SYM_MOD_BELOW          | `SMBlw` | `U+1B6C`                                                                |
| VOWEL_ABOVE            | `VAbv`  | USE=V & UIPC = Top                                                      |
| VOWEL_ABOVE_BELOW      | _null_  | USE=V & UIPC = Top_And_Bottom                                           |
| VOWEL_ABOVE_BELOW_POST | _null_  | USE=V & UIPC = Top_And_Bottom_And_Right                                 |
| VOWEL_ABOVE_POST       | _null_  | USE=V & UIPC = Top_And_Right                                            |
| VOWEL_BELOW            | `VBlw`  | USE=V & UIPC = Bottom _or_ Overstruck                                   |
| VOWEL_BELOW_POST       | _null_  | USE=V & UIPC = Bottom_And_Right                                         |
| VOWEL_PRE              | `VPre`  | USE=V & UIPC = Left                                                     |
| VOWEL_PRE_ABOVE        | _null_  | USE=V & UIPC = Top_And_Left                                             |
| VOWEL_PRE_ABOVE_POST   | _null_  | USE=V & UIPC = Top_And_Left_And_Right                                   |
| VOWEL_PRE_POST         | _null_  | USE=V & UIPC = Left_And_Right                                           |
| VOWEL_POST             | `VPst`  | USE=V & UIPC = Right                                                    |
| VOWEL_MOD_ABOVE        | `VMAbv` | USE=VM & UIPC = Top                                                     |
| VOWEL_MOD_BELOW        | `VMBlw` | USE=VM & UIPC = Bottom _or_ Overstruck                                  |
| VOWEL_MOD_PRE          | `VMPre` | USE=VM & UIPC = Left                                                    |
| VOWEL_MOD_POST         | `VMPst` | USE=VM & UIPC = Right                                                   |
| | | |
:::


## The <abbr>USE</abbr> shaping model ##

The <abbr title="Universal Shaping Engine">USE</abbr> shaping model consists of five top-level stages.

1. Decomposition of split vowels
2. Identifying clusters
3. Applying basic cluster formation features
4. Glyph reordering
5. Applying final features

All scripts supported by the <abbr title="Universal Shaping Engine">USE</abbr> model will be processed in this same
pattern. However, not every script requires that actions be taken in
every operation.

The first two stages take place for the entire text run being
shaped. Subsequently, stages 3, 4, and 5 are each conducted in order on a
per-cluster basis, until every cluster in the run has been processed.

The substitution features from <abbr title="Glyph Substitution table">GSUB</abbr> and the positioning features from
<abbr title="Glyph Positioning table">GPOS</abbr> are applied to the text run in predefined features groups. Which
features are applied at each step in the process are described below.


### Stage 1: Split vowel decomposition ###

Most split vowels have a canonical decomposition defined in the
Unicode specification. The <abbr title="Universal Shaping Engine">USE</abbr> shaping model requires that all such
split vowels be decomposed into their components before any further
processing is performed. 

For these vowels, the canonical decomposition must be performed prior
to cluster identification. Because this decomposition is a
character-level operation, the shaping engine may choose to perform it
earlier, such as during an initial Unicode-normalization stage. 

For any split vowels that do not have a canonical decomposition, the
active font should provide a decomposition via the `ccmp` substitution
feature in <abbr title="Glyph Substitution table">GSUB</abbr>. 

The cluster-identification rules detailed in stage two are based on
the canonical decompositions, and do not take non-canonical <abbr title="Glyph Substitution table">GSUB</abbr>
decomposition into account.


### Stage 2. Cluster identification ###

A cluster in the <abbr title="Universal Shaping Engine">USE</abbr> model is defined according to a generalized,
visual pattern that is common to all supported scripts. Consequently,
the cluster-identification expressions used do not enforce linguistic
or orthographic correctness.

An independent cluster will consist of a standalone codepoint that
does not require further shaping, optionally followed by a variation
selector. Independent clusters will match the expression:
```markdown
(IND | O | Rsv | WJ) VS?
```

A standard cluster features a required base character and may include
many optional elements. Standard clusters will match the expression:
```markdown
( R | CS )? ( B | GB ) VS? CMAbv* CMBlw* ( ((H B) | SUB) VS? CMAbv* CMBlw* )* MPre? MAbv? MBlw? MPst? VPre* VAbv* VBlw* VPst* VMPre* VMAbv* VMBlw* VMPst* FAbv* FBlw* FPst* FM?
```

A halant-terminated cluster occurs when any character other than a `B`
follows a `H`. Halant-terminated clusters will match the expression:
```markdown
( R | CS )? (B | GB) VS? CMAbv* CMBlw* ( ((H B) | SUB) VS? CMAbv* CMBlw*)* H
```

A number-joiner–terminated cluster will match the expression:
```markdown
N VS? (HN N VS?)* HN
```

A numeral cluster will match the expression:
```markdown
N VS? (HN N VS?)*
```

A symbol cluster will match the expression:
```markdown
(S | GB) VS? SMAbv* SMBlw*
```

> Note: Practically speaking, shaping engines are highly unlikely to
> encounter more than a small number of sequential vowel or modifiers
> in any real-world clusters. Thus, implementations may choose to
> limit occurrences by limiting some of the above expressions to a
> finite length, such as `VPre{0,4}` rather than `VPre*`.

The expressions above use state-machine syntax from the Ragel
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

Sequences not matching any of the above expressions should be regarded
as broken. The shaping engine may make a best-effort attempt
to shape the broken sequence, but making guarantees about the
correctness or appearance of the final result is out of scope for this
document.

After the clusters have been identified, each of the subsequent 
shaping stages occurs on a per-cluster basis.


### Stage 3: Basic cluster formation ###

The basic cluster formation stage is used to apply fundamental
substitutions necessary for script and language correctness.

#### Stage 3, step 1: Applying the basic pre-processing features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

The basic pre-processing step applies mandatory substitution features
using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this 
stage, glyph sequences should be tagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features. 

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.

	locl
	ccmp
	nukt
	akhn

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

> Note: The `ccmp` feature may perform decompositions of split vowels
> that do not have a canonical decomposition defined in Unicode. Split
> vowels that do have a canonical decomposition were decomposed in
> stage one.

The `nukt` feature replaces <samp>"_Consonant_,Nukta"</samp> sequences with a
precomposed nukta-variant of the consonant glyph. 

The `akhn` feature replaces specific sequences with required
ligatures. These sequences can occur anywhere in a cluster. 
Akhand characters have orthographic status equivalent to full
consonants in some languages, and fonts may have later substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.


#### Stage 3, step 2: Applying the basic reordering features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

The basic reordering step applies mandatory substitution features from
<abbr title="Glyph Substitution table">GSUB</abbr> that affect reordering elements.

For these features, the glyph substitutions themselves are applied at this
step. However, the actual reordering of the glyphs does not take place
until stage 4, step 1.

The order in which these substitutions must be performed is fixed for
all <abbr title="Universal Shaping Engine">USE</abbr> scripts:

	rphf
	pref

##### Stage 3, step 2.1: rphf #####

The `rphf` feature replaces cluster-initial <samp>"Ra,Halant"</samp> sequences with
the <samp>"Reph"</samp> glyph.

> Note: although the glyph substitution is performed in this step, the
> corresponding glyph reordering move is not performed until a later
> stage. 

##### Stage 3, step 2.2: pref #####

The `pref` feature replaces pre-base-consonant glyphs with any special
forms. 

> Note: although the glyph substitution is performed in this step, the
> corresponding glyph reordering move is not performed until a later
> stage. 


#### Stage 3, step 3: Applying the basic orthographic features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

The basic orthographic step applies substitution features using the
rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this stage, glyph
sequences should be tagged for possible application of <abbr title="Glyph Substitution table">GSUB</abbr> features. 

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.

	rkrf
	abvf
	blwf
	half
	pstf
	vatu
	cjct

The `rkrf` feature replaces <samp>"_Consonant_,Halant,Ra"</samp> sequences with the
"Rakaar"-ligature form of the consonant glyph.

The `abvf` feature replaces above-base-consonant glyphs with any
special forms. 

The `blwf` feature replaces below-base-consonant glyphs with any
special forms.

The `half` feature replaces <samp>"_Consonant_,Halant"</samp> sequences before the
base consonant with "half forms" of the consonant glyphs.

The `pstf` feature replaces post-base-consonant glyphs with any
special forms.

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. 

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match <samp>"_Consonant_,Halant,_Consonant_"</samp>.


### Stage 4: Glyph reordering ###

The glyph-reordering stage moves dependent vowels, diacritics, and
other mark glyphs in relation to the base consonant. All reordering is
performed in this stage, which is broken into two distinct steps:

1. Applying the reordering features from <abbr title="Glyph Substitution table">GSUB</abbr>
2. Performing property-based reordering moves


#### Stage 4, step 1: Applying the reordering features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

In this step, the reordering moves corresponding to the
glyph-reordering features in <abbr title="Glyph Substitution table">GSUB</abbr> are performed.

Any glyph substitutions that apply to characters involved in these
reordering moves were performed in stage 3, step 2. Therefore, this
step only requires moving glyphs to their final positions.

The order in which these substitutions must be performed is fixed for
all <abbr title="Universal Shaping Engine">USE</abbr> scripts:

	rphf
	pref

##### Stage 4, step 1.1: rphf #####

In stage 3, step 2, the `rphf` feature replaced cluster-initial
<samp>"Ra,Halant"</samp> sequences with the <samp>"Reph"</samp> glyph. The <samp>"Reph"</samp> glyph is now
reordered to its final position. The algorithm to determine the final
position of the <samp>"Reph"</samp> glyph is:

  - Move the <samp>"Reph"</samp> right one position at a time.
    - If the character immediately following the new position is an
      explicit <samp>"Halant"</samp>, stop.
    - If the character immediately before the new position is a full
      base (`B`) character, stop.
    - If the end of the cluster is reached, stop.

##### Stage 4, step 1.2: pref #####

In stage 3, step 2, the `pref` feature replaced pre-base-consonant
glyphs with special forms. The pre-base-consonant glyph is now
reordered to its final position. The algorithm to determine the final
position of the pre-base-reordering consonant is:

  - Move the pre-base-reordering consonant left one position at a
    time.
    - If the pre-base reordering consonant is to the left of the
	  first spacing glyph after an explicit <samp>"Halant"</samp>, stop.
    - When the pre-base reordering consonant is to the left of the
	  first spacing glyph in the cluster, stop. 
	- If the beginning of the cluster is reached, stop.
	
> Note: Each cluster may have only one pre-base-reordering consonant
> glyph. 
>
> Note: scripts that use pre-base medial consonants may also make use
> of the `pref` feature reordering.


#### Stage 4, step 2: Performing property-based reordering moves ####

In this step, any characters that match one of the <abbr title="Universal Shaping Engine">USE</abbr> reordering
classifications should be reordered into their final position. 

> Note: this classification-based reordering step ensures that
> reordering characters not addressed by the active font's <abbr title="Glyph Substitution table">GSUB</abbr>
> features are ordered correctly.

The character classes reordered in this step are:

```markdown
`R`		= `REPHA`
`VPre`		= `VOWEL_PRE`
`VMPre`		= `VOWEL_MOD_PRE`
```

Pre-base `REPHA` glyphs that occur before a full base are reordered
using the <samp>"Reph"</samp> reordering algorithm described in [Stage 4, step 1.1](#stage-4-step-11-rphf),
just as if the `rphf` feature had been applied to the glyph.

Pre-base `VOWEL_PRE` vowel glyphs, including both stand-alone `VOWEL_PRE` vowels
and `VOWEL_PRE` components of split vowels, are reordered to
   - before the base glyph
   - before any other pre-base glyphs that were reordered in earlier steps
   
Pre-base `VOWEL_MOD_PRE` vowel-modifier glyphs are reordered to
   - before the base glyph
   - before any pre-base `VOWEL_PRE` vowel glyphs
   - before any other pre-base glyphs that were reordered in earlier steps


### Stage 5: Final feature application ###

The final stage involves applying topographic joining features for
connected scripts, applying typographic-presentation features from
<abbr title="Glyph Substitution table">GSUB</abbr>, and applying positioning features from <abbr title="Glyph Positioning table">GPOS</abbr>.


#### Stage 5, step 1: Applying the final topographic features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

For connected scripts, this step applies the substitutions to select
the correct topographic form for each glyph, based on its position in
the syllable.

Whether or not each codepoint joins on the left or the right side is
determined by the `Unicode Joining Type` (<abbr>UJT</abbr>) property defined in <abbr title="Unicode Character Database">UCD</abbr>
for each codepoint.

> Note: <abbr title="Universal Shaping Engine">USE</abbr> does not support positional typographic features for any
> non-connected scripts.
	
	isol
	init
	medi
	fina

#### Stage 5, step 2: Applying the final typographic-presentation features from <abbr title="Glyph Substitution table">GSUB</abbr> ####

The final typographic-presentation step applies mandatory substitution
features using the rules in the font's <abbr title="Glyph Substitution table">GSUB</abbr> table. In preparation for this
stage, glyph sequences should be tagged for possible application 
of <abbr title="Glyph Substitution table">GSUB</abbr> features.

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the <abbr title="Glyph Substitution table">GSUB</abbr> table
in the font.

	abvs
	blws
	calt
	clig
	haln
	liga
	pres
	psts
	rclt
	rlig
	vert
	vrt2
	
The `abvs` feature replaces above-base-consonant glyphs with special
presentation forms. This usually includes contextual variants of
above-base marks or contextually appropriate mark-and-base ligatures.

The `blws` feature replaces below-base-consonant glyphs with special
presentation forms. This usually includes replacing consonants that
are adjacent to special consonant forms with contextual
ligatures.

The `calt` feature substitutes glyphs with contextual alternate
forms.  In contrast to `rclt`, the `calt` feature performs
substitutions that are not mandatory for orthographic
correctness. However, unlike `rclt`, the substitutions made by `calt`
can be disabled by application-level user interfaces.

The `clig` feature substitutes optional ligatures that are on by
default, but which are activated only in certain
contexts. Substitutions made by clig may be disabled by
application-level user interfaces. 

The `haln` feature replaces syllable-final <samp>"_Consonant_,Halant"</samp> pairs with
special presentation forms. This can include stylistic variants of the
consonant where placing the <samp>"Halant"</samp> mark on its own is
typographically problematic. 

The `liga` feature substitutes standard, optional ligatures that are on
by default. Substitutions made by `liga` may be disabled by
application-level user interfaces.

The `pres` feature replaces pre-base-consonant glyphs with special
presentations forms. This can include consonant conjuncts, half-form
consonants, and stylistic variants of left-side dependent vowels
(matras). 

The `psts` feature replaces post-base-consonant glyphs with special
presentation forms. This usually includes replacing right-side
dependent vowels (matras) with stylistic variants or replacing
post-base-consonant/matra pairs with contextual ligatures. 

The `rclt` feature substitutes glyphs with contextual alternate
forms. The `rclt` feature should be used to perform such substitutions
that are required by the orthography of the active script and
language. Substitutions made by `rclt` cannot be disabled by 
application-level user interfaces.

The `rlig` feature substitutes glyph sequences with mandatory
ligatures. Substitutions made by `rlig` cannot be disabled by
application-level user interfaces.



#### Stage 5, step 3: Applying the final positioning features from <abbr>GPOS</abbr> ####

	curs
	dist
	kern
	mark
	abvm
	blwm
	mkmk
	
The `curs` feature perform cursive positioning in connected scripts or
cursive styles. Each cursive glyph has an entry point and exit point;
the `curs` feature positions glyphs so that the entry point of the
current glyph meets the exit point of the preceding glyph.

The `dist` feature adjusts the horizontal positioning of
glyphs. Unlike `kern`, adjustments made with `dist` do not require the
application or the user to enable any software _kerning_ features, if
such features are optional. 

The `kern` adjusts glyph spacing between pairs of adjacent glyphs.

The `mark` feature positions marks with respect to base glyphs.

The `abvm` feature positions above-base marks for attachment to base
characters. This includes above-base dependent vowels (matras),
diacritical marks, syllable modifiers, and above-base consonant forms. 

The `blwm` feature positions below-base marks for attachment to base
characters. This includes below-base dependent vowels (matras),
diacritical marks, syllable modifiers, and below-base consonant forms.

The `mkmk` feature positions marks with respect to preceding marks,
providing proper positioning for sequences of marks that attach to the
same base glyph.
