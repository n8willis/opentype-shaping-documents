# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenType Shaping Documents'
copyright = '2022, Sponsored by YesLogic'
author = 'Sponsored by YesLogic'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

source_suffix = {'.md': 'markdown'}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

myst_heading_anchors = 6


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_options = {
    'page_width': '1040px',
    'github_user': 'n8willis',
    'github_repo': 'opentype-shaping-documents',
    'github_button': True,
    'github_type': 'watch',
    'github_count': True,
    'extra_nav_links': {
        'Scripts': 'README.html',
        'Character tables': 'character-tables/character-tables-index.html',
        'Normalization':'opentype-shaping-normalization.html',
        'Notes': 'notes/README.html',
        'Errata': 'errata.html',
        }
}
