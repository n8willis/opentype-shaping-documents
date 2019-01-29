# Normalization in OpenType shaping #

## Unicode normalization ##

Unicode defines algorithms for normalizing a sequence of input
codepoints into either a canonical composed form or a canonical
decomposed form. The purpose of these algorithms and of the defined
normalization forms is to determine equivalent representations of input
sequences regardless of variations in the input sequences.

For example, a base letter with an attached mark might exist in
Unicode as a single codepoint, but an input sequence might consist of
the base letter codepoint followed by the combining mark
codepoint. Unicode normalization can be used to determine that the
"letter, mark" sequence is equivalent to the single codepoint. This
simplifies sorting, searching, string comparison, and many other common
tasks.

OpenType shaping utilizes Unicode normalization, but OpenType
shaping has a distinctly different goal: to select the best or most
appropriate representation of the input codepoint sequence that is
available in the active font.

## OpenType normalization ##

The OpenType shaping normalization algorithm attempts to 

1. completely decompose codepoint sequences at the grapheme level
2. correct the ordering of adjacent marks
3. completely recompose the codepoint sequence _if_ the active
   script's shaping model prefers composed forms. 
   
At each step, however, the shaping normalization algorithm will not
perform a decomposition or composition operation if the result will
produce a codepoint not available in the active font. 

Furthermore, the recomposition stage is optional and depends on the
active script settings in the text run. Individual script-shaping
models will prefer either decomposed or composed forms.


### 1. Decomposition ###



### 2. Mark Reordering ###



### 3. Recomposition ###




## Other considerations ##

Nukta forms - turns Indic2 step into no-op.

CCMP

LOCL
