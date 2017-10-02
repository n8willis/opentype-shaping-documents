# Bengali shaping in OpenType #

## General information ##

The Bengali or Bangla script belongs to the Indic family, and follows
the same general patterns as the other Indic scripts. More
specifically, it belongs to the North Indic subgroup, in which
clusters of consonants are often represented as conjuncts.

The Bengali script is used to write multiple languages, most commonly
Bengali, Assamese, and Manipuri. In addition, Sanskrit may be written
in Bengali, so Bengali script runs may include signs from the Vedic
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
3. Applying the basic substitution features from GPOS
4. Final reordering
5. Applying all remaining substitution features from GPOS
6. Applying positioning features from GSUB


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

Valid syllables may begin with either a consonant or an independent
vowel. 

> Note: The consonant "Ra" receives special treatment; in many
> circumstances it is replaced with a combining mark-like form called "Reph" that must be
> reordered after the syllable-identification stage is complete.

Valid syllables in Bengali must end with either a dependent vowel or a
consonant that is NOT followed by a halant (thus, a consonant that retains the
inherent vowel, 'a').

In addition, stand-alone clusters can occur at the start of words.

Non-syllable clusters include independent codepoints, isolated
symbols, numeral sequences, and _____.


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

Consonant syllable:
{C+[N]+<H+[<ZWNJ|ZWJ>]|<ZWNJ|ZWJ>+H>} + C+[N]+[A] + [< H+[<ZWNJ|ZWJ>] | {M}+[N]+[H]>]+[SM]+[(VD)]

Vowel-based syllable:
[Ra+H]+V+[N]+[<[<ZWJ|ZWNJ>]+H+C|ZWJ+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]

Stand-alone cluster (at the start of the word only):
[Ra+H]+NBSP+[N]+[<[<ZWJ|ZWNJ>]+H+C>]+[{M}+[N]+[H]]+[SM]+[(VD)]

After the clusters have been identified, each of the subsequent 
shaping stages occurs on a per-cluster basis.

### (2) Initial reordering ###

The initial reordering stage is used to relocate glyphs from the
phonetic order in which they occur in a run of text into the
orthographic order in which they are presented visually.

> Note: Primarily, this means moving dependent-vowel glyphs, "Ra" glyphs, and
> other consonants that take special treatment, such as a "Ta" or "Ya"
> located at the end of the syllable.
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
	POS_PRE_M
	POS_PRE_C

	POS_BASE_C
	POS_AFTER_MAIN

	POS_ABOVE_C

	POS_BEFORE_SUB
	POS_BELOW_C
	POS_AFTER_SUB

	POS_BEFORE_POST
	POS_POST_C
	POS_AFTER_POST

	POS_FINAL_C
	POS_SMVD


1. The first step is to determine the base consonant of the cluster
and tag it as `POS_BASE_C`.

2. Second, any two-part dependent vowels must be decomposed into their
canonical left-side and right-side components. Bengali has two
two-part dependent vowels. "O" (`U+09BC`) and "AU" (`U+09CC`).

3. Third, all left-side dependent-vowel signs, including those that
resulted from the preceding decomposition step, must be tagged to be  moved to the beginning of the
cluster, with `POS_PRE_M`.

4. Fourth, any subsequences of marks must be reordered so that they appear in canonical
order. Nuktas must be placed before all other marks. 

5. Fifth, consonants that will take on pre-base forms must be tagged
with `POS_PRE_C`.

6. Sixth, initial "Ra"s that will become rephs must be tagged with
`POS_RA_TO_BECOME_REPH`.

> `<bng2>` text contains two Unicode codepoints for "Ra." `U+09B0` and `U+09F0`.
>
> `U+09B0` is used in Bengali-language, Manipuri-language, and Sanskrit text. `U+09F0` is used in
> Assamese-language text.

7. Seventh, any final consonants must be tagged with
`POS_POST_C`. Bengali includes two such final consonants, "Khanda Ta"
(`U+09CE`), and the sequence "Halant,Ya" (`U+09CD`,`U+09AF`), which usually
triggers the "Yaphala" presentation form. 

8. Eighth, all miscellaneous marks must be attached to the
preceding character, so that they move together during the sorting step.

9. Post-base glyphs should be merged.

set up masks (an array of which features apply to each position??? -
   at least REPH, HALF, BLWF, PSTF, and PREF. Plus CFAR for Khmer.)
 << Does below-base form tagging happen here?
  Halant,Ra -> Raphala
  Halant,Ba -> Baphala >>
<<Seems to be that everything is tagged with the masks for BLWF ABVF
PSTF>>
<< NO! Stuff gets marked early on! in update_consonant_position !!!!
Keep looking!!! >>
+ find Halant,Ra sequence and tag it for PREF reordering^^


 apply ZWJ/ZWNJ effects

initial reordering::
Treat the various syllable types differently: non-indic clusters (do
nothing), symbol clusters (also do nothing), standalone clusters
(which seem to be limited to dotted-circle settings and, perhaps,
other non-regular-text settings), broken clusters (who knows),
consonant clusters (the normal case, described below), and vowel
clusters (i.e., clusters with an initial vowel. HB treats these
initial vowels the same way it does consonants, though, so there's no
special case).


### (3) Applying the basic substitution features from GPOS ###

	nukt
	akhn
	rphf
	rkrf
	pref
	blwf
	abvf
	half
	pstf
	vatu
	cjct
	cfar

### (4) Final reordering ###

### (5) Applying all remaining substitution features from GPOS ###

	init
	pres
	abvs
	blws
	psts
	haln
	dist
	abvm
	blwm

### (6) Applying positioning features from GSUB ###
