# SPDX-FileCopyrightText: Copyright 2025 Nathan Willis
#
# SPDX-License-Identifier: BSD-2-Clause
"""Dictionary of the acronyms or abbreviations and corresponding full-text expansions used in the documents.
"""

# Dictionary mapping the set of acronyms and abbreviations
# that get wrapped in <abbr> tags in the generated output
# to the corresponding full-expansion text for each.
#
# Perhaps obviously, the keys were used to identify and
# tag acronyms with <abbr> in the document source. In some,
# but not all, cases the full expansions are also used.
ABBR_STRING_MAP = {
    "AAT": "Apple Advanced Typography",
    "AJT": "Arabic Joining Type",
    "AMTRA": "Arabic Mark Transient Reordering Algorithm",
    "Ccc": "Canonical Combining Class",
    "CEK": "Combining Enclosing Keycap",
    "CGJ": "Combining Grapheme Joiner",
    "CLDR": "Common Locale Data Repository",
    "CSS": "Cascading Style Sheets",
    "GDEF": "Glyph Definition table",
    "GPOS": "Glyph Positioning table",
    "GSUB": "Glyph Substitution table",
    "LRM": "Left-to-Right Mark",
    "LTR": "Left-To-Right",
    "MCM": "Modifier Combining Mark",
    "NBSP": "No-Break Space",
    "NFC": "Normalization Form C",
    "NFD": "Normalization Form D",
    "NFKC": "Normalization Form KC",
    "NFKD": "Normalization Form KD",
    "PNG": "Portable Network Graphics",
    "PUA": "Private Use Area",
    "RGI": "Recommended for General Interchange",
    "RLM": "Right-to-Left Mark",
    "RTL": "Right-To-Left",
    "SHA": "Secure Hash Algorithm",
    "SVG": "Scalable Vector Graphics",
    "UCD": "Unicode Character Database",
    "UCDM": "Unicode Character Decomposition Mapping",
    "UGC": "Unicode General Category",
    "UIPC": "Unicode Indic Positional Category",
    "UISC": "Unicode Indic Syllabic Category",
    "UJT": "Unicode Joining Type",
    "URL": "Uniform Resource Locator",
    "USE": "Universal Shaping Engine",
    "ZWJ": "Zero-Width Joiner",
    "ZWNJ": "Zero-Width Non Joiner",
}
