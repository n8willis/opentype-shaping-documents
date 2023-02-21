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

extensions = ['myst_parser', 'sphinx_external_toc']

source_suffix = {'.md': 'markdown'}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'sphinx_root_doc' # Will need to be renamed, eventually....

myst_heading_anchors = 6

myst_enable_extensions = ['smartquotes',]

external_toc_path = "_toc.yml"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
        ]
    }
html_theme_options = {
    'page_width': '1040px',
    'github_user': 'n8willis',
    'github_repo': 'opentype-shaping-documents',
    'github_button': True,
    'github_type': 'watch',
    'github_count': True,
    'extra_nav_links': {
        'GitHub issues': 'https://github.com/n8willis/opentype-shaping-documents/issues',
        'Build process': 'https://github.com/n8willis/opentype-shaping-documents/blob/sphinx/BUILD.md', # Fix the directory path after PR merge; Add contributor-guide link
        }
}
