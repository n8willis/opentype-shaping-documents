# Bengali shaping in OpenType #

## General information ##

The Bengali or Bangla script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
clusters of consonants are often represented as conjuncts.

The Bengali script is used to write multiple languages, most commonly
Bengali, Assamese, and Manipuri. In addition, Sanskrit may be written
in Bengali, so Bengali script runs may include glyphs from the Vedic
Extension block on Unicode. 

There are two extant Bengali script tags, `<beng>` and `<bng2>`. The older
script tag, `<beng>`, was deprecated in 2008.  Therefore, new fonts
should be engineered to work with the `<bng2>` shaping model. However,
if a font is encountered that supports only `<beng>`, the shaping engine
should deal with it gracefully.

## The `<bng2>` shaping model ##

Processing a run of `<bng2>` text involves six top-level stages:

1. Identifying syllables and other clusters
2. Initial reordering
3. Applying the basic substitution features from GSUB
4. Final reordering
5. Applying all remaining substitution features from GSUB
6. Applying positioning features from GPOS


As with other Indic scripts, the initial reordering stage and the
final reordering stage each involve invoking a set of several
script-specific rules. The basic substitution features must be applied
to the run in a specific order. The remaining substitution features in
stage five, however, do not have a mandatory order.

> Note: Bengali differs from Devanagari in that sequences of pre-base consonants
> are generally combined into conjuncts and only less frequently
> rendered in half-forms.

Bengali's specific shaping characteristics include:

1. `BASE_POS_LAST` = The base consonant of a syllable is the last
consonant, not counting any special final-consonant forms.

2. `REPH_POS_AFTER_SUB` = Reph is positioned after subjoined (i.e.,
   below-base) consonant forms.
3. `REPH_MODE_IMPLICIT` = Reph is formed by an initial Ra,Halant sequence.
4. `BLWF_MODE_PRE_AND_POST` = The below-forms feature is applied to
   pre-base and post-base consonants.
5. `MATRA_POS_RIGHT` = `POS_AFTER_POST` = Right-side matras are
   positioned after post-base consonant forms.
6. `MATRA_POS_BOTTOM` = `POS_AFTER_SUB` = Below-base matras are
   positioned after subjoined (i.e., below-base) consonant forms.


### (1) Identifying syllables and other clusters ###

A syllable cluster in Bengali consists of a valid orthographic cluster
that MAY be followed by a "tail" of modifier signs.

> Note: The Bengali Unicode block enumerates five modifier signs, "Candrabinu" (`U+0981`), "Anusvara" (`U+0982`), "Visarga"
> (`U+0983`), "Avagraha" (`U+09BD`), and "Vedic Anusvara" (`U+09FC`). In addition, Sanskrit text written in Bengali may include
> additional signs from Vedic Extensions block.

Each syllable contains exactly one vowel. Valid syllables may begin with either a consonant or an independent
vowel. The consonant (if any exists) that carries the vowel is the "base" consonant of the syllable. Zero or more additional consonants may be present in the syllable; in a valid syllable these other consonants will be followed by the "Halant" mark, which indicates that they carry no vowel.

> Note: The consonant "Ra" receives special treatment; in many
> circumstances it is replaced with a combining mark-like form. A "Ra,Halant" sequence at the beginning of a cluster is
> replaced with an above-base mark called "Reph" (unless the "Ra" is the only consonant in the cluster). "Ra,Halant" sequences that occur elsewhere in the cluster may take on the
> below-base form "Raphala." "Reph" and "Raphala" sequences must be
> reordered after the syllable-identification stage is complete.

In addition, stand-alone clusters can occur at the start of words.

Non-syllable clusters include independent codepoints, isolated
symbols, numeral sequences, and so on.


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
{C+[N]+<H+[<ZWNJ|ZWJ>]|<ZWNJ|ZWJ>+H>} + C+[N]+[A] + [< H+[<ZWNJ|ZWJ>] | {M}+[N]+[H]>]+[SM]+[(VD)]

A vowel-based syllable will match the expression:
[Ra+H]+V+[N]+[<[<ZWJ|ZWNJ>]+H+C|ZWJ+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]

A stand-alone cluster (at the start of the word only) will match the expression:
[Ra+H]+NBSP+[N]+[<[<ZWJ|ZWNJ>]+H+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]

After the clusters have been identified, each of the subsequent 
shaping stages occurs on a per-cluster basis.

### (2) Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text into the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel (matra) glyphs, "Ra,Halant" glyph sequences, and
> other consonants that take special treatment in some circumstances. "Ba", "Ta", and "Ya"
> occasionally take on special forms, depending on their position in the syllable.
>
> These reordering moves are mandatory. The final-reordering stage
> may make additional moves, depending on the content of the font.

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

2. Second, any two-part dependent vowels (matras) must be decomposed into their
canonical left-side and right-side components. Bengali has two
two-part dependent vowels. "O" (`U+09BC`) and "AU" (`U+09CC`). Each has a canonical decomposition, so this step is unambiguous.

3. Third, all left-side dependent-vowel (matra) signs, including those that
resulted from the preceding decomposition step, must be tagged to be  moved to the beginning of the
cluster, with `POS_PREBASE_MATRA`.

4. Fourth, any subsequences of marks must be reordered so that they appear in canonical
order. Nuktas must be placed before all other marks. 

5. Fifth, consonants that will take on pre-base forms must be tagged
with `POS_PREBASE_CONSONANT`.

6. Sixth, initial "Ra,Halant" sequences that will become rephs must be tagged with
`POS_RA_TO_BECOME_REPH`.

> `<bng2>` text contains two Unicode codepoints for "Ra." `U+09B0` and `U+09F0`.
>
> `U+09B0` is used in Bengali-language, Manipuri-language, and Sanskrit text. `U+09F0` is used in
> Assamese-language text.

7. Seventh, any final consonants must be tagged with
`POS_POSTBASE_CONSONANT`. Bengali includes two such final consonants, "Khanda Ta"
(`U+09CE`), and the sequence "Halant,Ya" (`U+09CD`,`U+09AF`), which usually
triggers the "Yaphala" presentation form. 

8. Eighth, all miscellaneous marks must be attached to the
preceding character, so that they move together during the sorting step.

9. Ninth, all post-base glyphs should be merged into a single substring that will sort as a single unit.

10. In preparation for the next stage, glyph sequences should be tagged for possible application of GSUB features.
+ find Halant,Ra sequence and tag it for PREF reordering^^


### (3) Applying the basic substitution features from GSUB ###

The basic-substitution phase applies mandatory substitution features using the rules in the fon'ts GSUB table. The order in which these substitutions must be performed is fixed:

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
"Ka,Halant,Ssa" is substituted with the "KaSsa" ligature. "Ja,Halant,Nya" is substituted with the "JaNya" ligature.

The `rphf` feature replaces initial "Ra,Halant" sequences with the "Reph" glyph.

The `pref` feature replaces pre-base-consonant glyphs with any special forms.

The `blwf` feature replaces below-base-consonant glyphs with any special forms.

The `half` feature replaces "_consonant_,Halant" sequences before the base consonant with "half forms" of the consonant glyphs.

The `pstf` feature replaces post-base-consonant glyphs with any special forms.

The `vatu` feature replaces certain sequences with "Vattu variant" forms. "Vattu variants" are formed by glyphs followed by the below-base form of "Ra", so this feature must be applied after the `blwf` feature.

The `cjct` feature replaces sequences of consonants with conjunct ligatures. The font's GSUB rules may be written so that the `cjct` substitutions apply to half-form consonants, therefore this feature must be applied after the `half` feature.

### (4) Final reordering ###

### (5) Applying all remaining substitution features from GSUB ###

	init
	pres
	abvs
	blws
	psts
	haln
	dist
	abvm
	blwm

### (6) Applying positioning features from GPOS ###
