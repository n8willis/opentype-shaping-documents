# Universal Shaping Engine script shaping in OpenType #

This document details the default shaping procedure needed to display
text runs in scripts supported by the Universal Shaping Engine (USE)
model. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
  - [The USE shaping model](#the-use-shaping-model)
      - [1: Split vowel decomposition](#1-split-vowel-decomposition)
      - [2: Cluster identification](#2-cluster-identification)
      - [3: Basic cluster formation](#3-basic-cluster-formation)
	      - [3.1: Applying the basic pre-processing features from GSUB](#31-applying-the-basic-pre-processing-features-from-gsub)
          - [3.2: Applying the basic reordering features from GSUB](#32-applying-the-basic-reordering-features-from-gsub)
          - [3.3: Applying the basic orthographic features from GSUB](#33-applying-the-basic-orthographic-features-from-gsub)
	  - [4: Glyph reordering](#4-glyph-reordering)
	      - [4.1: Applying the reordering features from GSUB](#41-applying-the-reordering-features-from-gsub)
	      - [4.2: Performing property-based reordering moves](#42-performing-property-based-reordering-moves)
	  - [5: Final feature application](#5 -final-feature-application)
	      - [5.1: Applying the final topographic features from GSUB](#51-applying-the-final-topographic-features-from-gsub)
	      - [5.2: Applying the final typographic-presentation features from GSUB](#52-applying-the-final-typographic-presentation-features-from-gsub)
	      - [5.3: Applying the final positioning features from GPOS](#53-applying-the-final-positioning-features-from-gpos)
  
  
  
## General information ##

The Universal Shaping Engine (USE) model is used for complex scripts
that are not already supported by a dedicated OpenType shaping
model. 

"Complex" scripts, in OpenType shaping terminology, are scripts that
require some combination of glyph reordering, contextual joining
behavior, or the substitution or context-dependent forms for
linguistic or orthographic correctness.

The scripts covered by this model include Javanese, Balinese,
Buginese, Batak, Chakma, Lepcha, Modi, Phags-pa, Tagalog, Siddham,
Sundanese, Tai Le, Tai Tham, Tai Viet, and many others.

In many ways, the USE model is a generalization of the
[Indic2](opentype-shaping-indic-general.md) OpenType 
shaping model, with adjustments made to correct shortfalls encountered
when using the Indic2 shaping model, as well as additional changes
designed to broaden the number of scripts that can be supported. For
example, the USE model includes a step applyting contextual
joining-behavior features as is performed in the Arabic-like shaping
model. 

USE was introduced after the release of version 8.0 of the Unicode
specification. The intent is for USE to support complex scripts added
to future Unicode releases in addition to those already supported.


## Terminology ##

The USE shaping model uses a standard set of terms for the features of
supported scripts. These terms are similar to the standard terms used
for Indic scripts, but with several key distinctions.

A **cluster** is the fundamental unit used in shaping; it consists of
a sequence of Unicode codepoints that will be processed as an atomic
unit. An individual syllable typically corresponds to a single
cluster, but any particular cluster might involve multiple syllables
or a sequence that does not match the syllable-formation rules of the
script.

A **base** character in the USE model may be a consonant, an
independent vowel, a number, or any of several additional character
classes.

A cluster's base consonant is generally rendered in its full form
(although it may form ligatures), while other consonants in the
cluster frequently take on secondary forms. Different GSUB
substitutions may apply to a script's **pre-base** and **post-base**
consonants. Some of these substitutions create **above-base** or
**below-base** forms. The **Reph** form of the consonant "Ra" is an
example.

A **vowel** character in the USE model is a dependent vowel or any of
several additional marks with similar behavior. This class is similar
to the "matra" class used in Indic shaping.

**Halant** is the standard term for a "vowel-killer" sign.


## Glyph classification ##

The USE shaping model classifies characters based on a specific set of
properties defined for each codepoint in the Unicode Character
Database (UCD), augmented with a small set of pre-defined property
overrides.

The UCD properties used for USE character classification are:

	Unicode General Category (UGC)
	Unicode Indic Syllabic Category (UISC)
	Unicode Indic Positional Category (UIPC)

In addition, the Unicode Character Decomposition Mapping (UCDM) is used for
all split vowels.


### USE overrides ###

Although, in general, the USE shaping model relies on the UGC, UISC,
and UIPC properties, the USE model makes a small set of standardized
overrides to the properties of certain specific characters.

The following table lists the complete set of USE overrides. Shaping
engines should implement the override properties in order to guarantee
correct results.

> Note: A _null_ in the following table indicates that the
> corresponding Unicode property is not overridden for the codepoint
> featured in that row. 


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


### USE classification table ###

The following table lists the classes utilized in the USE shaping
model, along with a definition for each class. The class definitions
refer to the UGC, UISC, and UIPC categories in the Unicode standard,
or to specific Unicode codepoints.

The symbols given in the "Symbol" column for each class may be used to
express cluster-matching rules or other algorithms.

Vowels and modifiers may be further subclassified as described in the
[USE subclasses table](#use-subclasses-table) below.


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


### USE subclasses table ###

Vowels and modifiers may be further subclassified based on their
position relative to base characters. The subclasses incorporated in
the USE shaping model are defined in the table below.

Split-vowel subclasses are not assigned a symbol because each split
vowel must be decomposed into its components.


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



## The USE shaping model ##

The USE shaping model consists of five top-level stages.

1. Decomposition of split vowels
2. Identifying clusters
3. Applying basic cluster formation features
4. Glyph reordering
5. Applying final features

All scripts supported by the USE model will be processed in this same
pattern. However, not every script requires that actions be taken in
every operation.

The first two stages take place for the entire text run being
shaped. Subsequently, stages 3, 4, and 5 are each conducted in order on a
per-cluster basis, until every cluster in the run has been processed.

The substitution features from GSUB and the positioning features from
GPOS are applied to the text run in predefined features groups. Which
features are applied at each step in the process are described below.


### 1: Split vowel decomposition ###

Most split vowels have a canonical decomposition defined in the
Unicode specification. The USE shaping model requires that all such
split vowels be decomposed into their components before any further
processing is performed. 

For these vowels, the canonical decomposition must be performed prior
to cluster identification. Because this decomposition is a
character-level operation, the shaping engine may choose to perform it
earlier, such as during an initial Unicode-normalization stage. 

For any split vowels that do not have a canonical decomposition, the
active font should provide a decomposition via the `ccmp` substitution
feature in GSUB. 

The cluster-identification rules detailed in stage two are based on
the canonical decompositions, and do not take non-canonical GSUB
decomposition into account.


### 2. Cluster identification ###

A cluster in the USE model is defined according to a generalized,
visual pattern that is common to all supported scripts. Consequently,
the cluster-identification expressions used do not enforce linguistic
or orthographic correctness.

An independent cluster will consist of a standalone codepoint that
does not require further shaping, optionally followed by a variation
selector. Independent clusters will match the the expression:
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
> encoutner more than a small number of sequential vowel or modifiers
> in any real-world clusters. Thus, implementations may choose to
> limit occurences by limiting some of the above expressions to a
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

After the syllables have been identified, each of the subsequent 
shaping stages occurs on a per-syllable basis.


### 3: Basic cluster formation ###

The basic cluster formation stage is used to apply fundamental
substitutions necessary for script and language correctness.

#### 3.1: Applying the basic pre-processing features from GSUB ####

The basic pre-processing step applies mandatory substitution features
using the rules in the font's GSUB table. In preparation for this 
stage, glyph sequences should be tagged for possible application 
of GSUB features. 

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the GSUB table
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
> GSUB substitutions in the following steps.

The `ccmp` feature allows a font to substitute mark-and-base sequences
with a pre-composed glyph including the mark and the base, or to
substitute a single glyph into an equivalent decomposed sequence of
glyphs. 

If present, these composition and decomposition substitutions must be
performed before applying any other GSUB lookups, because
those lookups may be written to match only the `ccmp`-substituted
glyphs.

> Note: The `ccmp` feature may perform decompositions of split vowels
> that do not have a canonical decomposition defined in Unicode. Split
> vowels that do have a canonical decomposition were decomposed in
> stage one.

The `nukt` feature replaces "_Consonant_,Nukta" sequences with a
precomposed nukta-variant of the consonant glyph. 

The `akhn` feature replaces specific sequences with required
ligatures. These sequences can occur anywhere in a syllable. 
Akhand characters have orthographic status equivalent to full
consonants in some languages, and fonts may have later substitution
rules designed to match them in subsequences. Therefore, this
feature must be applied before all other many-to-one substitutions.


#### 3.2: Applying the basic reordering features from GSUB ####

The basic reordering step applies mandatory substitution features from
GSUB that affect reordering elements.

The glyph substitution from these features are applied at this
step. However, the actual reordering of the glyphs does not take place
until stage 4, step 1.

The order in which these substitutions must be performed is fixed for
all USE scripts:

	rphf
	pref

##### 3.2.1 `rphf` #####

The `rphf` feature replaces cluster-initial "Ra,Halant" sequences with
the "Reph" glyph.

> Note: also the glyph substitution is performed in this step, the
> corresponding glyph reordering move is not performed until a later
> stage. 

##### 3.2.2 `pref` #####

The `pref` feature replaces pre-base-consonant glyphs with any special
forms. 

> Note: also the glyph substitution is performed in this step, the
> corresponding glyph reordering move is not performed until a later
> stage. 


#### 3.3: Applying the basic orthographic features from GSUB ####

The basic orthographic step applies substitution features using the
rules in the font's GSUB table. In preparation for this stage, glyph
sequences should be tagged for possible application of GSUB features. 

The order in which these features are applied is not canonical; they
should be applied in the order in which they appear in the GSUB table
in the font.

	rkrf
	abvf
	blwf
	half
	pstf
	vatu
	cjct

The `rkrf` feature replaces "_Consonant_,Halant,Ra" sequences with the
"Rakaar"-ligature form of the consonant glyph.

The `abvf` feature replaces above-base-consonant glyphs with any
special forms. 

The `blwf` feature replaces below-base-consonant glyphs with any
special forms.

The `half` feature replaces "_Consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs.

The `pstf` feature replaces post-base-consonant glyphs with any
special forms.

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. 

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. These sequences must match "_Consonant_,Halant,_Consonant_".


### 4: Glyph reordering ###



#### 4.1 Applying the reordering features from GSUB ####

	rphf
	pref

#### 4.2 Performing property-based reordering moves ####

In this step, any characters that match one of the USE reordering
classifications should be reordered into their final position. 

> Note: this classification-based reordering step ensures that
> reordering characters not addressed by the active font's GSUB
> features are ordered correctly.

	`R`
	`VPre`
	`VMPre`

### 5: Final feature application ###



#### 5.1: Applying the final topographic features from GSUB ####

	isol
	init
	medi
	fina

#### 5.2: Applying the final typographic-presentation features from GSUB ####

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

#### 5.3: Applying the final positioning features from GPOS ####

	curs
	dist
	kern
	mark
	abvm
	blwm
	mkmk
	
