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
```

## Sphinx ##

Sphinx is a Python-based utility that you will need to install on your
local machine. The official [installation
guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
covers what is necessary for a variety of OSes and
environments. Perhaps the easiest approach is to install Sphinx in a
Python [virtual
enviornment](https://www.sphinx-doc.org/en/master/usage/installation.html#using-virtual-environments). 

After installing Sphinx itself, you will also need to install the
[MyST-Parser](https://myst-parser.readthedocs.io/en/latest/) package,
which enables Sphinx to process Markdown files. Using the
virtual-environment installation method, you can keep both of these
packages contained for this project.

At the moment there are no other dependencies involved, but a
`build-requirements.txt` file is included in the repository that lists
the packages in the author's virtual environment. You shouldn't _need_
to utilize it, since just installing Sphinx and MyST-Parser ought to
suffice, but it is there if required.


## Building HTML documents ##

With the Sphinx and MyST-Parser packages installed, go to the
top-level directory of this repository in a shell or
terminal. Building the HTML documents should only take two steps:

1. Run `make clean` to clear out all temporary files from previous
   run. Do this every time.

2. Run `make html` to regenerate the HTML files. The output files will
   be written to the `_build/html/` subdirectory.


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
