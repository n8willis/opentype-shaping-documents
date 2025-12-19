# SPDX-FileCopyrightText: Copyright 2025 Nathan Willis
#
# SPDX-License-Identifier: BSD-2-Clause

"""Sphinx extension to attach a color-toggle button to specified SVG elements in documents.

   This extension only affects the `html` builder.
"""

from __future__ import annotations

from docutils import nodes

from docutils.parsers.rst import directives

from sphinx.util import logging

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxTranslator, SphinxRole
#from sphinx.util.typing import ExtensionMetadata

from sphinx.writers.html import HTMLTranslator


# Directive to insert color-toggle button
#
#   Example output:
#     <p>
#        <button class="svg-color-toggle-button" id="button-bengali-akhn-kssa" onclick="toggleColor('bengali-akhn-kssa')">
#      Toggle cluster colors</button>
#     </p>
#


class svg_color_toggle_node(nodes.General, nodes.Element):
    """SVG color-toggle node."""

    pass


class SVGColorToggleButton(SphinxDirective):
    """A directive to insert a color-toggle switch for 
       an SVG element with the specified id."""

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    
    def run(self) -> list[svg_color_toggle_node]:

        # The sole argument is the CSS element id to build
        # the button for
        svg_element = self.arguments[0]
        
        return [
            svg_color_toggle_node(
                target_id = svg_element,
                button_id = "button-" + svg_element,
                button_klass = "svg-color-toggle-button",
                button_label = "Toggle cluster colors",
                )
            ]


def visit_svg_color_toggle_node_html(translator: HTMLTranslator, node: svg_color_toggle_node) -> None:
    """Entry point of the SVG color-toggle node."""
    html: str = ""

    if node["target_id"]:
        html += '<button class="' + node["button_klass"] + '" id="' + node["button_id"] + '" onclick=\'toggleColor(\"' + node["target_id"] + '\")\'>' + node["button_label"]
    else:
        pass

    translator.body.append(html)


def depart_svg_color_toggle_node_html(translator: HTMLTranslator, node: svg_color_toggle_node) -> None:
    """Exit from the SVG color-toggle node."""

    html: str = ""

    if node["target_id"]:
        html += '</button>'

    translator.body.append(html)


def visit_svg_color_toggle_node_unsupported(translator: SphinxTranslator, node: svg_color_toggle_node) -> None:
    """Entry point of the ignored SVG color-toggle node."""
    logger.warning(
        f"SVG color-toggle {node['target_id']}: unsupported output format (node skipped)"
    )
    raise nodes.SkipNode




def setup(app: Sphinx): # The ExtensionMetadata stuff is not available in this version of Sphinx. Sphinx's own docs are pretty terrible about clarifying these matters....
#def setup(app: Sphinx) -> ExtensionMetadata:

    app.add_node(
        svg_color_toggle_node,
        html=(visit_svg_color_toggle_node_html, depart_svg_color_toggle_node_html),
        epub=(visit_svg_color_toggle_node_unsupported, None),
        latex=(visit_svg_color_toggle_node_unsupported, None),
        man=(visit_svg_color_toggle_node_unsupported, None),
        texinfo=(visit_svg_color_toggle_node_unsupported, None),
        text=(visit_svg_color_toggle_node_unsupported, None),
    )
    app.add_directive("svg-color-toggle-button", SVGColorToggleButton)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }
