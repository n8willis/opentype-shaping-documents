# Bengali shaping in OpenType #

## General information ##

The Bengali or Bangla script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
clusters of consonants are often represented as conjuncts.

The Bengali script is used to write multiple languages, most commonly
Bengali, Assamese, and Manipuri. In addition, Sanskrit may be written
in Bengali, so Bengali script runs may include glyphs from the Vedic
Extension block of Unicode. 

There are two extant Bengali script tags, `<beng>` and `<bng2>`. The older
script tag, `<beng>`, was deprecated in 2008.  Therefore, new fonts
should be engineered to work with the `<bng2>` shaping model. However,
if a font is encountered that supports only `<beng>`, the shaping engine
should deal with it gracefully.

## Glyph classification ##

Shaping Bengali text depends on the shaping engine correctly
classifying each glyph in the run. As with most other scripts, the
classifications must distinguish between consonants, vowels
(independent and dependent), numerals, punctuation, and diacritic
marks. 

For most glyphs, the classifications assigned by Unicode are correct,
but are not sufficient to capture the expected shaping
behavior. Therefore, Bengali glyphs must additionally be classified by
how they are treated when shaping a run of text. 

Bengali glyphs should be classified as in the following
table. Codepoints in the Bengali block with no assigned meaning are
marked as _unassigned_ in the _Unicode class_ column. Assigned codepoints
marked with a _null_ in the _Shaping category_ column evoke no special
behavior from the shaping engine. Assigned codepoints marked with a
_null_ in the _Positioning subcategory_ column evoke no special
mark-positioning behavior.

| Codepoint | Unicode class | Shaping category | Positioning subcategory |
|:----------|:--------------|:-----------------|:------------------------|
|`U+0980`   | Letter | _null_ | _null_ |
|`U+0981`   | Mark [n] | BINDU | TOP_POSITION |
|`U+0982`   | Mark [sc] | BINDU | RIGHT_POSITION |
|`U+0983`   | Mark [sc] | VISARGA | RIGHT_POSITION     | 
|`U+0984`   | _unassigned_ | _null_ | _null_ |
|`U+0985`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+0986`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+0987`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+0988`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+0989`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+098A`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+098B`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+098C`   | Letter | VOWEL_INDEPENDENT | _null_     | 
|`U+098D`   | _unassigned_ | _null_ | _null_     | 
|`U+098E`   | _unassigned_ | _null_ | _null_ |
|`U+098F`   | Letter | VOWEL_INDEPENDENT | _null_ |
| | | |
|`U+0990`   | Letter | VOWEL_INDEPENDENT | _null_     | 
|`U+0991`   | _unassigned_ | _null_ | _null_     | 
|`U+0992`   | _unassigned_ | _null_ | _null_ |
|`U+0993`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+0994`   | Letter | VOWEL_INDEPENDENT | _null_     | 
|`U+0995`   | Letter | CONSONANT | _null_   | 
|`U+0996`   | Letter | CONSONANT | _null_     | 
|`U+0997`   | Letter | CONSONANT | _null_ |
|`U+0998`   | Letter | CONSONANT | _null_     | 
|`U+0999`   | Letter | CONSONANT | _null_     | 
|`U+099A`   | Letter | CONSONANT | _null_     | 
|`U+099B`   | Letter | CONSONANT | _null_     | 
|`U+099C`   | Letter | CONSONANT | _null_     | 
|`U+099D`   | Letter | CONSONANT | _null_     | 
|`U+099E`   | Letter | CONSONANT | _null_     | 
|`U+099F`   | Letter | CONSONANT | _null_ |
| | | |
|`U+09A0`   | Letter | CONSONANT | _null_     | 
|`U+09A1`   | Letter | CONSONANT | _null_     | 
|`U+09A2`   | Letter | CONSONANT | _null_     | 
|`U+09A3`   | Letter | CONSONANT | _null_     | 
|`U+09A4`   | Letter | CONSONANT | _null_     | 
|`U+09A5`   | Letter | CONSONANT | _null_     | 
|`U+09A6`   | Letter | CONSONANT | _null_     | 
|`U+09A7`   | Letter | CONSONANT | _null_ |
|`U+09A8`   | Letter | CONSONANT | _null_     | 
|`U+09A9`   | _unassigned_ | _null_ | _null_     | 
|`U+09AA`   | Letter | CONSONANT | _null_     | 
|`U+09AB`   | Letter | CONSONANT | _null_     | 
|`U+09AC`   | Letter | CONSONANT | _null_     | 
|`U+09AD`   | Letter | CONSONANT | _null_     | 
|`U+09AE`   | Letter | CONSONANT | _null_     | 
|`U+09AF`   | Letter | CONSONANT | _null_ |
| | | |
|`U+09B0`   | Letter | CONSONANT | _null_     | 
|`U+09B1`   | _unassigned_ | _null_ | _null_     | 
|`U+09B2`   | Letter | CONSONANT | _null_     | 
|`U+09B3`   | _unassigned_ | _null_ | _null_     | 
|`U+09B4`   | _unassigned_ | _null_ | _null_     | 
|`U+09B5`   | _unassigned_ | _null_ | _null_     | 
|`U+09B6`   | Letter | CONSONANT | _null_     | 
|`U+09B7`   | Letter | CONSONANT | _null_ |
|`U+09B8`   | Letter | CONSONANT | _null_     | 
|`U+09B9`   | Letter | CONSONANT | _null_     | 
|`U+09BA`   | _unassigned_ | _null_ | _null_     | 
|`U+09BB`   | _unassigned_ | _null_ | _null_     | 
|`U+09BC`   | Mark [n] | NUKTA | BOTTOM_POSITION     | 
|`U+09BD`   | Letter | AVAGRAHA | _null_     | 
|`U+09BE`   | Mark [sc] | VOWEL_DEPENDENT | RIGHT_POSITION     | 
|`U+09BF`   | Mark [sc] | VOWEL_DEPENDENT | LEFT_POSITION |
| | | |
|`U+09C0`   | Mark [sc] | VOWEL_DEPENDENT | RIGHT_POSITION     | 
|`U+09C1`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09C2`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09C3`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09C4`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09C5`   | _unassigned_ | _null_ | _null_     | 
|`U+09C6`   | _unassigned_ | _null_ | _null_     | 
|`U+09C7`   | Mark [sc] | VOWEL_DEPENDENT | LEFT_POSITION |
|`U+09C8`   | Mark [sc] | VOWEL_DEPENDENT | LEFT_POSITION     | 
|`U+09C9`   | _unassigned_ | _null_ | _null_     | 
|`U+09CA`   | _unassigned_ | _null_ | _null_ |
|`U+09CB`   | Mark [sc] | VOWEL_DEPENDENT | LEFT_AND_RIGHT_POSITION |
|`U+09CC`   | Mark [sc] | VOWEL_DEPENDENT | LEFT_AND_RIGHT_POSITION     | 
|`U+09CD`   | Mark [n] | VIRAMA | BOTTOM_POSITION |
|`U+09CE`   | Letter | CONSONANT_DEAD | _null_     | 
|`U+09CF`   | _unassigned_ | _null_ | _null_ |
| | | |
|`U+09D0`   | _unassigned_ | _null_ | _null_     | 
|`U+09D1`   | _unassigned_ | _null_ | _null_     | 
|`U+09D2`   | _unassigned_ | _null_ | _null_     | 
|`U+09D3`   | _unassigned_ | _null_ | _null_     | 
|`U+09D4`   | _unassigned_ | _null_ | _null_     | 
|`U+09D5`   | _unassigned_ | _null_ | _null_     | 
|`U+09D6`   | _unassigned_ | _null_ | _null_     | 
|`U+09D7`   | Mark [sc] | VOWEL_DEPENDENT | RIGHT_POSITION |
|`U+09D8`   | _unassigned_ | _null_ | _null_     | 
|`U+09D9`   | _unassigned_ | _null_ | _null_     | 
|`U+09DA`   | _unassigned_ | _null_ | _null_     | 
|`U+09DB`   | _unassigned_ | _null_ | _null_     | 
|`U+09DC`   | Letter | CONSONANT | _null_     | 
|`U+09DD`   | Letter | CONSONANT | _null_     | 
|`U+09DE`   | _unassigned_ | _null_ | _null_     | 
|`U+09DF`   | Letter | CONSONANT | _null_ |
| | | |
|`U+09E0`   | Letter | VOWEL_INDEPENDENT | _null_ |
|`U+09E1`   | Letter | VOWEL_INDEPENDENT | _null_     | 
|`U+09E2`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09E3`   | Mark [n] | VOWEL_DEPENDENT | BOTTOM_POSITION     | 
|`U+09E4`   | _unassigned_ | _null_ | _null_     | 
|`U+09E5`   | _unassigned_ | _null_ | _null_     |
|`U+09E6`   | Number | NUMBER | _null_ |
|`U+09E7`   | Number | NUMBER | _null_ |
|`U+09E8`   | Number | NUMBER | _null_ |
|`U+09E9`   | Number | NUMBER | _null_ |
|`U+09EA`   | Number | NUMBER | _null_ |
|`U+09EB`   | Number | NUMBER | _null_ |
|`U+09EC`   | Number | NUMBER | _null_ |
|`U+09ED`   | Number | NUMBER | _null_ |
|`U+09EE`   | Number | NUMBER | _null_ |
|`U+09EF`   | Number | NUMBER | _null_ |
| | | |
|`U+09F0`   | Letter | CONSONANT | _null_     | 
|`U+09F1`   | Letter | CONSONANT | _null_     | 
|`U+09F2`   | Symbol | _null_ | _null_     | 
|`U+09F3`   | Symbol | _null_ | _null_     | 
|`U+09F4`   | Number | _null_ | _null_     | 
|`U+09F5`   | Number | _null_ | _null_     | 
|`U+09F6`   | Number | _null_ | _null_     | 
|`U+09F7`   | Number | _null_ | _null_     |
|`U+09F8`   | Number | _null_ | _null_     | 
|`U+09F9`   | Number | _null_ | _null_     | 
|`U+09FA`   | Symbol | _null_ | _null_     | 
|`U+09FB`   | Symbol | _null_ | _null_     | 
|`U+09FC`   | Letter | _null_ | _null_     | 
|`U+09FD`   | Punctuation | _null_ | _null_     | 
|`U+09FE`   | _unassigned_ | _null_ | _null_     | 
|`U+09FF`   | _unassigned_ | _null_ | _null_     |
 
<!--- 
  /* Vedic Extensions */

  /* 1CD0 */ _(Ca,T), _(Ca,T), _(Ca,T),  _(x,x), _(Ca,O), _(Ca,B), _(Ca,B), _(Ca,B),
  /* 1CD8 */ _(Ca,B), _(Ca,B), _(Ca,T), _(Ca,T), _(Ca,B), _(Ca,B), _(Ca,B), _(Ca,B),
  /* 1CE0 */ _(Ca,T), _(Ca,R),  _(x,O),  _(x,O),  _(x,O),  _(x,O),  _(x,O),  _(x,O),
  /* 1CE8 */  _(x,O),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,B),  _(x,x),  _(x,x),
  /* 1CF0 */  _(x,x),  _(x,x), _(Vs,x), _(Vs,x), _(Ca,T),  _(x,x),  _(x,x),  _(x,x),
  /* 1CF8 */ _(Ca,x), _(Ca,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),


1cf5 and 1cf6 get reclassified as CONSONANT

1ce2 and 1ce8 get treated like tone marks, but SHOULD be allowed only after Visarga.

1ced gets treated like tone mark, but SHOULD be allowed only after U+1CE9..U+1CF1

1ce9 1cec 1cee 1cf1 all take marks in standalone clusters, similar to Avagraha.

U+2010 and U+2011 get treated like placeholders.

U+25CC is the dotted circle.

  /* General Punctuation */

  /* 2008 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),_(ZWNJ,x),_(ZWJ,x),  _(x,x),  _(x,x),
  /* 2010 */ _(CP,x), _(CP,x), _(CP,x), _(CP,x), _(CP,x),  _(x,x),  _(x,x),  _(x,x),

#define indic_offset_0x2070u 1672


  /* Superscripts and Subscripts */

  /* 2070 */  _(x,x),  _(x,x),  _(x,x),  _(x,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2078 */  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),  _(x,x),
  /* 2080 */  _(x,x),  _(x,x), _(SM,x), _(SM,x), _(SM,x),  _(x,x),  _(x,x),  _(x,x),
--->
## The `<bng2>` shaping model ##

Processing a run of `<bng2>` text involves six top-level stages:

1. Identifying syllables and other clusters
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying all remaining positioning features from GPOS


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve invoking a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

<!-- > Note: Bengali differs from Devanagari in that sequences of pre-base consonants
> are generally combined into conjuncts and only less frequently
> rendered in half-forms. -->

With regard to the common variations seen among Indic scripts, 
Bengali's specific shaping characteristics include:

1. `BASE_POS_LAST` = The base consonant of a syllable is the last
consonant, not counting any special final-consonant forms.

2. `REPH_POS_AFTER_SUB` = "Reph" is positioned after subjoined (i.e.,
   below-base) consonant forms.
3. `REPH_MODE_IMPLICIT` = "Reph" is formed by an initial "Ra,Halant" sequence.
4. `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied both to
   pre-base consonants and to post-base consonants.
5. `MATRA_POS_RIGHT` = `POS_AFTER_POST` = Right-side matras are
   positioned after post-base consonant forms.
6. `MATRA_POS_BOTTOM` = `POS_AFTER_SUB` = Below-base matras are
   positioned after subjoined (i.e., below-base) consonant forms.

These characteristics determine how the shaping engine must reorder
certain glyphs, how base consonants are determined, and how "Reph"
should be encoded within a run of text.

### (1) Identifying syllables and other clusters ###

A syllable cluster in Bengali consists of a valid orthographic cluster
that MAY be followed by a "tail" of modifier signs.

> Note: The Bengali Unicode block enumerates five modifier signs, "Candrabinu" (`U+0981`), "Anusvara" (`U+0982`), "Visarga"
> (`U+0983`), "Avagraha" (`U+09BD`), and "Vedic Anusvara" (`U+09FC`). In addition, Sanskrit text written in Bengali may include
> additional signs from Vedic Extensions block.

Each syllable contains exactly one vowel. The consonant (if any exists) that carries the vowel is the "base" consonant of the syllable. 

Valid syllables may begin with either a consonant or an independent
vowel.  Zero or more additional consonants may be present in the syllable; in a valid syllable these other consonants will be followed by the "Halant" mark, which indicates that they carry no vowel.

> Note: The consonant "Ra" receives special treatment; in many
> circumstances it is replaced with a combining mark-like form. 
> A "Ra,Halant" sequence at the beginning of a cluster is
> replaced with an above-base mark called "Reph" (unless the "Ra"
> is the only consonant in the cluster). 
>
> This requirement is synonymous with the `REPH_MODE_IMPLICIT`
> characteristic mentioned earlier.
>
> "Ra,Halant" sequences that occur elsewhere in the cluster may take on the
> below-base form "Raphala." "Reph" and "Raphala" sequences must be
> reordered after the syllable-identification stage is complete.
>
> `<bng2>` text contains two Unicode codepoints for "Ra." `U+09B0` and `U+09F0`.
>
> `U+09B0` is used in Bengali-language, Manipuri-language, and Sanskrit text. `U+09F0` is used in
> Assamese-language text.
>

In addition, stand-alone clusters may occur, such as when an isolated codepoint is shown in example text, sequences of numerals, and so on.

Clusters should be identified by examining the run and matching glyphs, based on their categorization, using regular expressions.


	C	consonant
	V	independent vowel
	N	nukta
	H	halant/virama
	ZWNJ	zero width non-joiner
	ZWJ	zero width joiner
	M	matra (up to one of each type: pre-base, below-base, or post-base)
	SM	syllable modifier signs
	VD	vedic signs
	A	anudatta (U+0952)
	NBSP	NO-BREAK SPACE

A consonant syllable will match the expression:
```
{C+[N]+<H+[<ZWNJ|ZWJ>]|<ZWNJ|ZWJ>+H>} + C+[N]+[A] + [< H+[<ZWNJ|ZWJ>] | {M}+[N]+[H]>]+[SM]+[(VD)]
```

A vowel-based syllable will match the expression:
```
[Ra+H]+V+[N]+[<[<ZWJ|ZWNJ>]+H+C|ZWJ+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A stand-alone cluster (at the start of the word only) will match the expression:
```
[Ra+H]+NBSP+[N]+[<[<ZWJ|ZWNJ>]+H+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]
```

A cluster that does not match any of these expressions should be
regarded as broken. The shaping engine may make a best-effort attempt
to shape the broken cluster, but making guarantees about the correctness or
appearance of the final result is out of scope for this document.

After the clusters have been identified, each of the subsequent 
shaping stages occurs on a per-cluster basis.

### (2) Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text to the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs, 
> "Ra,Halant" glyph sequences, and other consonants that take special
> treatment in some circumstances. "Ba", "Ta", and "Ya" occasionally
> take on special forms, depending on their position in the syllable.
>
> These reordering moves are mandatory. The final-reordering stage
> may make additional moves, depending on the text and on the features
> implemented in the active font.

The cluster should be processed by tagging each glyph with its
intended position based on its ordering category. After all glyphs
have been tagged, the entire cluster should be sorted in stable order,
so that glyphs of the same ordering category remain in the same
relative position with respect to each other.

The final sort order of the ordering categories should be:


	POS_RA_TO_BECOME_REPH
	POS_PREBASE_MATRA
	POS_PREBASE_CONSONANT

	POS_BASE_CONSONANT
	POS_AFTER_MAIN

	POS_ABOVEBASE_CONSONANT

	POS_BEFORE_SUB
	POS_BELOWBASE_CONSONANT
	POS_AFTER_SUB

	POS_BEFORE_POST
	POS_POSTBASE_CONSONANT
	POS_AFTER_POST

	POS_FINAL_CONSONANT
	POS_SMVD


1. The first step is to determine the base consonant of the cluster
and tag it as `POS_BASE_CONSONANT`.

The algorithm for determining the base consonant is

- If the syllable starts with "Ra,Halant" and the cluster contains more than one consonant, exclude the starting "Ra" from the list of consonants to be considered.
- Starting from the end of the syllable, move backwards until a consonant is found.
    * If the consonant has a below-base or post-base form or is a pre-base reordering "Ra", move to the previous consonant. If neither condition is true, stop.
    * If the consonant is the first consonant, stop.

The consonant stopped at will be the base consonant.

2. Second, any two-part dependent vowels (matras) must be decomposed into their
left-side and right-side components. Bengali has two
two-part dependent vowels, "O" (`U+09BC`) and "AU" (`U+09CC`). Each has a canonical decomposition, so this step is unambiguous.

> "O" (`U+09BC`) decomposes to "`U+09C7`,`U+09BE`"
>
> "AU" (`U+09CC`) decomposes to "`U+09C7`,`U+09D7`"

3. Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be  moved to the beginning of the
cluster, with `POS_PREBASE_MATRA`.

4. Fourth, any subsequences of adjacent marks ("Halant"s, "Nukta"s, syllable modifiers, and Vedic signs) must be reordered so that they appear in canonical order. "Nukta"s must be placed before all other marks. 

5. Fifth, consonants that will take on pre-base forms must be tagged
with `POS_PREBASE_CONSONANT`.

6. Sixth, initial "Ra,Halant" sequences that will become rephs must be tagged with
`POS_RA_TO_BECOME_REPH`.

7. Seventh, any consonants that occur after a dependent vowel (matra) sign must be tagged with
`POS_POSTBASE_CONSONANT`. Such consonants will usually be followed by a "Halant" glyph, with the 
exception of special final-consonants. Bengali includes two such final consonants, "Khanda Ta"
(`U+09CE`), and the sequence "Halant,Ya" (`U+09CD`,`U+09AF`), which triggers the "Yaphala" form. 

8. Eighth, all miscellaneous marks must be attached to the
preceding character, so that they move together during the sorting step.

9. Ninth, all post-base glyphs should be merged into a single substring that will sort as a single unit.

With these steps completed, the cluster can be sorted into the final sort order.

### (3) Applying the basic substitution features from GSUB ###

The basic-substitution stage applies mandatory substitution features using the rules in the font's
GSUB table. In preparation for this stage, glyph sequences should be tagged for possible application
of GSUB features.

The order in which these substitutions must be performed is fixed:

	nukt
	akhn
	rphf
<!-- rkrf -->
	pref
	blwf
<!-- abvf -->
	half
	pstf
	vatu
	cjct
	cfar

The `nukt` feature replaces "_consonant_,Nukta" sequences with a precomposed nukta-variant of the consonant glyph.

The `akhn` feature replaces two specific sequences with required ligatures. 
"Ka,Halant,Ssa" is substituted with the "KaSsa"
ligature. "Ja,Halant,Nya" is substituted with the "JaNya" ligature. 

The `rphf` feature replaces initial "Ra,Halant" sequences with the "Reph" glyph.

The `pref` feature replaces pre-base-consonant glyphs with any special forms.

The `blwf` feature replaces below-base-consonant glyphs with any
special forms. Bengali includes two below-base consonant
forms. "Ra,Halant" in a non-cluster-initial position takes on the
"Raphala" form; "Ba,Halant" takes on the "Baphala" form. 

The `half` feature replaces "_consonant_,Halant" sequences before the
base consonant with "half forms" of the consonant glyphs.

The `pstf` feature replaces post-base-consonant glyphs with any special forms.

The `vatu` feature replaces certain sequences with "Vattu variant"
forms. "Vattu variants" are formed by glyphs followed by "Raphala"
(the below-base form of "Ra"), so this feature must be applied after
the `blwf` feature.

The `cjct` feature replaces sequences of adjacent consonants with
conjunct ligatures. The font's GSUB rules might be implemented so that
`cjct` substitutions apply to half-form consonants; therefore, this
feature must be applied after the `half` feature.


### (4) Final reordering ###

The final reordering stage repositions marks, dependent-vowel (matra)
signs, and "Reph" glyphs to the appropriate location with respect to
the base consonant. Because multiple subsitutions may have occured
during the application of the basic-shaping features in the preceding
stage, these repositioning moves could not be performed during the
initial-reordering stage. 



### (5) Applying all remaining substitution features from GSUB ###

In this stage, the remaining substitution features from the GSUB table are applied. The order in which these features are applied is not canonical; they should be applied in the order in which they appear in the GSUB table in the font.

	init
	pres
	abvs
	blws
	psts
	haln

The `init` feature replaces word-initial glyphs with special presentation forms.

The `pres` feature replaces pre-base-consonant glyphs with special presentations forms. This can include consonant conjuncts, half-form consonants, and stylistic variants of left-side dependent vowels (matras).

The `abvs` feature replaces above-base-consonant glyphs with special presentation forms. This usually includes contextual variants of above-base marks or contextualy appropriate mark-and-base ligatures. 

The `blws` feature replaces below-base-consonant glyphs with special presentation forms. This usually includes replacing consonants that are followed by below-base-consonant forms like "Raphala" and "Baphalan" with contextual ligatures. 

The `psts` feature replaces post-base-consonant glyphs with special presenataion forms. This usually includes replacing right-side dependent vowels (matras) with stylistic variants or replacing post-base-consonant/matra pairs with contextual ligatures.

The `haln` feature replaces word-final "_consonant_,Halant" pairs with special presentation forms. This can include stylistic variants of the consonant where placing the "Halant" mark on its own is typographically problematic.



### (6) Applying remaining positioning features from GPOS ###

In this stage, mark positioning, kerning, and other GPOS features are
applied. As with the preceding stage, the order in which these
features are applied is not canonical; they should be applied in the
order in which they appear in the GPOS table in the font.

        dist
        abvm
        blwm

The `dist` feature adjusts the horizontal positioning of glyphs. Unlike `kern`, adjustments made with `dist` do not require the application or user to enable the _kerning_ feature, if that feature is optional.

The `abvm` feature positions above-base marks.

The `blwm` feature positions below-base marks.
