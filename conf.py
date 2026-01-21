# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenType<br>Shaping<br>Documents'
copyright = '2022, Sponsored by YesLogic'
author = 'Sponsored by YesLogic'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.append(str(Path('_ext').resolve()))

extensions = ['myst_parser', 'sphinx_external_toc', 'sphinx_multitoc_numbering', 'sphinx_inline_svg', 'shapingdocs_svg_color_toggles']

source_suffix = {'.md': 'markdown'}

templates_path = ['_templates']
exclude_patterns = ['_build', '_ext', 'test', 'Thumbs.db', '.DS_Store', 'BUILD.md', '**-image-generation-log.md', 'character-tables/README.md', 'images/images-index.md'] # Eventually need to remove the links to image-generation-logs from the root README.md

root_doc = 'README' # Will need to be renamed, eventually....

numfig = True
numfig_secnum_depth = 2

myst_heading_anchors = 6

# attrs_inline to specify HTML element attributes like img 'title' that are getting lost on build.
myst_enable_extensions = ['substitution', 'smartquotes', 'colon_fence', 'attrs_inline']

myst_substitutions = {
    'opentogglebutton': '<br><button onclick="toggleColor(',
    'closetogglebutton': ')">Substitution Toggle cluster colors</button><br>',
}

external_toc_path = "_toc.yml"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_js_files = ['toggleSvgColors.js']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
        'sourcelink.html',
        ]
    }
html_theme_options = {
    'page_width': '1200px',
    'sidebar_width': '300px',
    'github_user': 'n8willis',
    'github_repo': 'opentype-shaping-documents',
    'font_family': 'Source\ Serif\ 4',
    'head_font_family': 'Source\ Serif\ 4',
    'caption_font_family': 'Source\ Serif\ 4',
    'code_font_family': 'Source\ Code\ Pro',
    'github_button': True,
    'github_type': 'watch',
    'github_count': True,
    'extra_nav_links': {
        'GitHub issues': 'https://github.com/n8willis/opentype-shaping-documents/issues',
        'Build process': 'https://github.com/n8willis/opentype-shaping-documents/blob/master/BUILD.md', # Fix the directory path after PR merge; Add contributor-guide link
        }
}
