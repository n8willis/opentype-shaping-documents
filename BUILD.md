# Building a local copy of these documents #

A local, static-HTML version of these documents can be built with the
[Sphinx](https://www.sphinx-doc.org/) generator.

The Sphinx-related files in the repository are:
```
config.py
index.rst
make.bat
Makefile
```

plus the directories
```
_build/
_static/
_templates/
_ext/
```

## Sphinx ##

Sphinx is a Python-based utility that you will need to install on your
local machine. The official [installation
guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
covers what is necessary for a variety of OSes and
environments. Perhaps the easiest approach is to install Sphinx in a
Python [virtual
environment](https://www.sphinx-doc.org/en/master/usage/installation.html#using-virtual-environments). 

After installing Sphinx itself, you will also need to install the
[MyST-Parser](https://myst-parser.readthedocs.io/en/latest/) package,
which enables Sphinx to process Markdown files. Using the
virtual-environment installation method, you can keep both of these
packages contained for this project.

At the moment there are three other dependencies involved, all of which
are Sphinx-extension packages:

1. [Sphinx-multitoc-numbering](https://sphinx-multitoc-numbering.readthedocs.io/),
   which is required to make Sphinx use a continuous numbering scheme
   across the files

2. [sphinx External TOC](https://sphinx-external-toc.readthedocs.io/),
   which is required to define the navigation sidebar declaratively
   (see the [TOCtrees](#toctrees) subsection below for more info)

3. [sphinx inline svg](https://pypi.org/project/sphinx-inline-svg/),
   which is used to implement the user-togglable cluster colors on the
   illustrations of feature application.

but a full `build-requirements.txt` file is included in the repository
that lists the packages in the author's virtual environment. You
shouldn't _need_ to utilize it, since just installing Sphinx,
MyST-Parser, and the extensions ought to suffice, but it is there if
required.

The build also uses a custom Sphinx extension, named
`shapingdocs_svg_color_toggles`, to generate the HTML elements used to
do the color toggling. This extension is included in the `_ext/`
directory of this repository and is called from that location,
however, so you do not need to install it separately.




## Building HTML documents ##

With the Sphinx and MyST-Parser packages installed, go to the
top-level directory of this repository in a shell or
terminal. Building the HTML documents should only take two steps:

1. Run `make clean` to clear out all temporary files from previous
   run. Do this every time.

2. Run `make html` to regenerate the HTML files. The output files will
   be written to the `_build/html/` subdirectory.


## Test suite ##

The `test/` directory contains test elements. At the moment, all of
the tests are run manually, but as the kinks are worked out they may
be rolled into either Git hooks or GitHub Actions, so it is advisable
to start using them. Currently there are two tests available as
Makefile targets: 

1. Run `make linktest` to run checks on all of the URLs found in the
   documents. 
   
2. Run `make spellcheck` to run spellchecking on the documents.

You can also run `make test` to run both tests in sequence.

The spell-checking is configured in `test/spellcheck.yaml`. It uses
the [PySpelling](https://facelessuser.github.io/pyspelling/) package
with the custom wordlist at `test/wordlist.txt`.

There are a few lingering peculiarities to PySpelling (most notably,
it supports excluding specified HTML elements, but cannot exclude
`<table>` elements because of a discrepancy between its built-in
Markdown converter and Sphinx, so at present the `character-tables/`
directory returns a great many false hits from the Unicode codepoint
names in the tables). The plan is to iron those out, then run both the
spell-checking and link-checking tests automatically on all pull
requests. When that is implemented, it will be documented here.



## Editing and bugfixing ##

The static-HTML version of the docs are a work-in-progress at the
moment, so please do poke around for problems and report any bugs.

Basic Sphinx configuration is done in the `config.py` file.

The HTML output documents are currently using the "Alabaster" theme,
which comes preinstalled. The Alabaster theme accepts several
configuration options which are also kept in `config.py`. Output
customization for the theme is also tweaked in the `custom.css` file
in the `_static/` subdirectory (just be sure you edit the one in
`_static/` itself; whenever the docs are rebuilt with `make`, that
file also gets copied into `_build/html/_static/`, so don't edit that
copy of the file since it gets overwritten).

To report a suspected typo or to suggest a general wording change,
please first synchronize your local repository with `git pull`. Then
do a `make clean`/`make html` as described in the section above.


### TOCtrees ###

Sphinx, by default, is hardcoded in a way that requires all documents
to be referenced in a separate, Sphinx-specific `toctree` structure,
after which the navigation sidebars (and other elements) are generated
on-the-fly at build-time by Sphinx itself.

The current documents are using a third-party extension that defines
the "TOCtree" in a declarative YAML file instead, to work around some
undesirable outputs -- mainly in the GitHub repository views -- that
Sphinx triggers with its on-the-fly `toctree` process.

But this approach isn't (yet?) perfect. Some files (namely this one,
`BUILD.md`, and the image-generation-log files) are manually excluded
from the build process so that they do not generate a flurry of
warning messages. That's deliberate, because the build instructions
and log files are metadata and aren't part of the final documentation
set itself.
