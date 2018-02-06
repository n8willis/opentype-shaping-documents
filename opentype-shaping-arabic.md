# Arabic script shaping in OpenType #

This document the general shaping procedure shared by all 
Arabic script styles, and defines the common pieces that style-specific
implementations share. 


**Table of Contents**

  - [General information](#general-information)
  - [Terminology](#terminology)
  - [Glyph classification](#glyph-classification)
      - [Joining properties](#joining-properties)
	  - [Mark classification](#mark-classification)
	  - [Character tables](#character-tables)
  - [The `<arab>` shaping model](#the-arab-shaping-model)
  
  


## General information ##

The Arabic script is used to write multiple languages, most commonly
Arabic, Persian, Urdu, Pashto, Kurdish, and Azerbaijani. 

The Arabic script encompasses multiple distinct styles, including Naskh, 
Nataliq, and Kufi, that share a number of common features and rules,
but that differ considerably in their final appearance. Due to the
common features found between the styles, a shaping engine can support
all styles of Arabic with a single shaping model.

In addition, several other writing systems that observe similar rules
and conventions can be supported using the same shaping model, even if
they are not historically related to Arabic. These scripts include:

  - N'Ko
  - Syriac
  - Mongolian

Note that each of these scripts has its own independent
script tag defined in OpenType. N'Ko uses `<nko>`, Syriac uses `<syrc>`, and
Mongolian uses `<mong>`. The information found below about the `<arab>`
script shaping model can serve as a general guide; script-specific
information can be found in the linked document for each script. 

<!--- Guessing on the script tags above; MS OpenType pages went --->
<!--- offline unexpectedly, and the network is down so IA Wayback --->
<!--- isn't available at the moment either.... --->

Arabic is a joining script that uses inter-word spaces, so each
codepoint in a text run may be substituted with one of several
contextual forms corresponding to its position in a
word. Most, but not all, letter sequences join; shaping engines must
track which positions trigger joining behavior for each letter.

Arabic is written (and, therefore, rendered) from right to
left. Shaping engines must track the directionality of the text run
when scripts of different direction are mixed.

## Terminology ##

OpenType shaping uses a standard set of terms for elements of the
Arabic script. The terms used colloquially in any particular language
may vary, however, potentially causing confusion.

**Base** glyph or character is the standard term for a Arabic
character that is capable of taking a diacritical mark. 

Most of the base characters in Arabic are **consonants**, but there
are several **vowel** base letters. 

Vowels that are not base characters are frequently omitted from the
text run entirely. Alternatively, such a vowel may appear as a
diacritical mark called a **ḥarakah**.

**Ijam** is the standard term for an above- or below-base dot that
distinguishes one consonant from another. Ijam are not considered
diacritics; they are integral to the consonant of which they are a part.

**Shadda** and **tashdid** are both standard terms for the "consonant
doubling" diacritical mark.

**Hamza** is the standard term for the glottal stop
semi-consonant. The hamza is not regarded as a full letter in most
languages, although it can appear as a stand-alone letter within
words. In some sequences, the hamza attaches to an adjacent letter;
when a hamza-supporting letter is not adjacent, however, the hamza can
appear on its own.

**Kashida** (or **tatweel**) is the term for a glyph inserted into a
sequence for the purpose of elongating the baseline stroke of a
letter. Unicode documents use the term "tatweel" most frequently,
while OpenType documents use the term "kashida" most
frequently. Kashidas are typically inserted in order to justify lines
of text. 


## Glyph classification ##

Because Arabic is a joining (or cursive) script, proper shaping of
text runs involves identifying the joining behavior of each character,
then combining that information with any preceding or subsequent
characters to determine the contextually correct form for display.

### Joining properties ###

Arabic characters are assigned a `JOINING_TYPE` property in the
Unicode standard that indicates how they join to adjacent
characters. There are six possible values: 

  - `JOINING_TYPE_LEFT` indicates that a character joins with
    the subsequent character, but does not join with the preceding
    character. 
	
  - `JOINING_TYPE_RIGHT` indicates that a character joins with the
    preceding character, but does not join with the subsequent character.	

  - `JOINING_TYPE_DUAL` indicates that a character joins with the
    preceding character and joins with the subsequent character.
	
  - `JOINING_TYPE_NON_JOINING` indicates that a character does not
    join with the preceding or with the subsequent character.
	
  - `JOINING_TYPE_TRANSPARENT` indicates that the character does not
    join with adjacent characters _and_ that the character must be
    skipped over when the shaping engine is evaluating the joining
    positions in a sequence of characters. When a
    `JOINING_TYPE_TRANSPARENT` character is encountered in a sequence,
    the `JOINING_TYPE` of the preceding character passes
    through. Diacritical marks are frequently assigned this property. 
	
  - `JOINING_TYPE_JOIN_CAUSING` indicates that the character forces
    the use of joining forms with the preceding and subsequent
    characters. Kashidas and the Zero Width Joiner (`U+200D`) are both
    `JOIN_CAUSING` characters.
  

Arabic letters are also assigned to a `JOINING_GROUP` that indicates
which fundamental character they behave like with regard to joining
behavior. Each of the basic letters in the Arabic block tends to
belong to its own `JOINING_GROUP`, while letters from the supplemental and
extended blocks are usually assigned to the `JOINING_GROUP` that
corresponds to the character's base letter, with no diacritics or ijam.

For example, the Persian letter "Peh" (`U+067E`) is visually
represented as the Arabic letter "Beh" (`U+0628`), but with two additional
below-base ijam. Consequently, "Peh" is assigned to the `BEH` `JOINING_GROUP`.

### Mark classification ###

Arabic diacritical marks are grouped into classes. Multiple diacritics
may be placed on the same base, subject to two conditions:

  - No more than one mark from each class is permitted
  - The DIAC1 and DIAC2 classes are mutually exclusive: a base glyph cannot
    accept both a DIAC1 mark and a DIAC2 mark.
	
Mark-and-base combinations that violate these conditions should be
regarded as ivalid. Shapers may attempt to deal gracefully with
such sequences, but no guarantees should be provided as to how the
sequence are shaped.
  
<!--- From MS Uniscribe web docs --->

  - `DIAC1` - Above-base (`U+064B`, `U+064C`, `U+064E`, `U+064F`,
            `U+0652`, `U+0657`, `U+0658`, `U+06E1`)
  - `DIAC2` - Below-base (`U+064D`, `U+0650`, `U+0656`)
  - `DIAC3` - Seat "Shadda" (`U+0651`)
  - `DIAC4` - Qur'anic above-base (`U+0610 - U+0614`, `U+0659`, `U+06D6`,
            `U+06DC`, `U+06DF`, `U+06E0`, `U+06E2`, `U+06E4`,
            `U+06E7`, `U+06E8`, `U+06EB`, `U+06EC`)
  - `DIAC5` - Qur'anic below-base (`U+06E3`, `U+06EA`, `U+06ED`)
  - `DIAC6` - Superscript "Alef" `U+0670`)
  - `DIAC7` - Madda (`U+0653`)
  - `DIAC8` - Hamza (`U+0654`, `U+0655`)
            <!--- MS site calls this group(8) madda too !?! --->
			
			
### Character tables ###

Separate character tables are provided for the Arabic, Arabic
Supplement, Arabic Extended-A, Rumi Numeral Symbols, and Arabic
Mathematical Symbols blocks, as well as for other miscellaneous
characters that are used in `<arab>` text runs:

  - [Arabic character table](character-tables/character-tables-arabic.md#arabic-character-table)
  - [Arabic Supplement character table](character-tables/character-tables-arabic-supplement.md#arabic-supplement-character-table)
  - [Arabic Extended-A character table](character-tables/character-tables-arabic-extended-a.md#arabic-extended-a-character-table)
  - [Rumi Numeral Symbols character table](character-tables/character-tables-rumi-numeral-symbols.md#rumi-numeral-symbols-character-table)
  - [Arabic Mathematical Symbols character table](character-tables/character-tables-arabic-mathematical-symbols.md#arabic-mathematical-symbols-character-table)
  - [Miscellaneous character table](character-tables/character-tables-arabic.md#miscellaneous-character-table)

Unicode also defines two blocks that implement backward compatibility
with retired file-encoding formats:

  - Arabic Presentation Forms-A
  - Arabic Presentation Forms-B
  
Unless a software application is required to support specific stores  of
documents that are known to have used these older encodings, however, the
shaping engine should not be expected to handle any text runs
incorporating codepoints from these blocks.

<!--- Character table example and explanation --->

Other important characters that may be encountered when shaping runs
of Arabic text include the dotted-circle placeholder (`U+25CC`), the
zero-width joiner (`U+200D`) and zero-width non-joiner (`U+200C`), the
left-to-right text marker (`U+200E`) and right-to-left text marker (`U+200F`), and
the no-break space (`U+00A0`).

The dotted-circle placeholder is frequently used when displaying a
vowel or diacritical mark in isolation. Real-world text syllables may
also use other characters, such as hyphens or dashes, in a similar
placeholder fashion; shaping engines should cope with this situation
gracefully.

The zero-width joiner is primarily used to force the usage of the
cursive connecting form of a letter even when the context of the
adjoining letters would not trigger the connecting form. 

For example, to show the initial form of a letter in isolation (such
as for dislaying it in a table of forms), the sequence "_Letter_,ZWJ"
would be used. To show the medial form of a letter in isolation, the
sequence "ZWJ,_Letter_,ZWJ" would be used.


<!--- Zero-Width Non Joiner explanation --->

<!--- LTR and RTL marker explanation --->

The no-break space is primarily used to display those codepoints that
are defined as non-spacing (such as vowel or diacritical marks and "Hamza") in an
isolated context, as an alternative to displaying them superimposed on
the dotted-circle placeholder.


## The `<arab>` shaping model ##

Processing a run of `<arab>` text involves five top-level stages:

1. Compound character composition and decomposition
2. Mark reordering
3. Applying the language-form substitution features from GSUB
4. Applying the typographic-form substitution features from GSUB
5. Applying the positioning features from GPOS


### 1. Compound character composition and decomposition ###

The `ccmp` feature allows a font to substitute pre-composed

### 2. Mark reordering ###


### 3. Applying the language-form substitution features from GSUB ###

`isol` to get isolated forms
`fina` to get final forms
`fin2` Syriac special case
`fin3` Syriac special case #2
`medi` to get medial forms
`med2` Syriac special case
`init` to get initial forms
`rlig` substitutes mandatory ligatures
`calt` substitutes alternative connection forms


### 4. Applying the typographic-form substitution features from GSUB ###

`liga` substitutes optional, on-by-default ligatures
`dlig` substitutes optional, off-by-default ligatures
`cswh` substitutes contextual swash variants (eg, long-noon when X
        subsequent glyphs do not descend below the baseline)
`mset` performs mark positioning by substitution (`mark` is
preferred!)

### 5. Applying the positioning features from GPOS ###

`curs` to perform cursive positioning
`kern` to perform kerning
`mark` to position marks to bases
`mkmk` to position marks to marks


