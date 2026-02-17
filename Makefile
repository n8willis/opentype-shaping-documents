# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
PYSPELLING    = pyspelling
PYSPELLINGMARKDOWNCONF = test/spellcheck.yml
PYSPELLINGHTMLCONF = test/spellcheck_html.yml

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Run tests on links and spelling
test: linktest spellcheck

# Use Sphinx's built-in link checker
linktest:
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Use PySpelling
spellcheck:
	@$(PYSPELLING) -c "$(PYSPELLINGMARKDOWNCONF)"

# Use PySpelling
htmlspellcheck:
	@$(PYSPELLING) -c "$(PYSPELLINGHTMLCONF)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
