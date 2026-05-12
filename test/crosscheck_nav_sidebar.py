#!/usr/bin/python3
import sys

import re
#from lxml import etree as ET
from pathlib import Path

def _sidebar_path_list(sidebar_template):
    """Returns a list containing all internal hyperlink file paths."""

    with open(sidebar_template, 'r+t', encoding='utf-8') as f:
        # This leverages the {{ local_url_prefix }} Jinja template variable,
        # for simplicity. If the sidebar template is changed, this can break.
        path_list = re.findall(r'href="{{ local_url_prefix }}([-//\w]+).html"', f.read())

    return path_list

    
def _sidebar_path_list_lxml(sidebar_template):
    """Deprecated. Returns a list containing all internal hyperlink file paths."""
    path_list = []
    #namespace = 
    with open(sidebar_template, 'r+t', encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        elems = list(root.iter())

        for elem in elems:
            if (elem != root and elem.tag == "a"):
                if "href" not in elem.attrib:
                    print("Error: can't find an href link in this <a> tag!")
                    print(elem)
                elif elem.attrib["href"].startswith("https://github.com"):
                    print("Skipping external link " + elem.attrib["href"])
                else:
                    path_list.append(elem.attrib["href"][22:-5])

    return path_list
                
        
def _toc_path_list(tocfile):
    """Returns a list containing all 'file:' entry paths in the TOC."""
    path_list = []

    with open(tocfile, 'r+t', encoding='utf-8') as f:
        for line in f:
            lyne = line.strip()
            if lyne.startswith("- file: "):
                path_list.append(lyne[8:])

    return path_list


def main(sidebar_file, toc_file):
    sidebar_list = sorted(_sidebar_path_list(sidebar_file))
    #print(len(sidebar_list), "sidebar_list:", sidebar_list, "\n")
    toc_list = sorted(_toc_path_list(toc_file))
    #print(len(toc_list), "toc_list:", toc_list, "\n")
    
    toc_extras = [x for x in toc_list if x not in sidebar_list]
    sidebar_extras = [x for x in sidebar_list if x not in toc_list]
    
    if not toc_extras and not sidebar_extras:
        print("Sidebar and TOC match.")
        return 0
    elif len(toc_extras) == 1 and len(sidebar_extras) == 1 and "overview" in toc_extras and "index" in sidebar_extras:
        # Handle the special case of "overview" being an alias of "index"
        print("TOC uses 'overview' which is an alias of sidebar's 'index'.")
        print("Otherwise, sidebar and TOC match.")
        return 0
    elif len(toc_extras) == 1 and len(sidebar_extras) == 1 and "overview" in sidebar_extras and "index" in toc_extras:
        # Handle the special case of "overview" being an alias of "index"
        print("Sidebar uses 'overview' which is an alias of TOC's 'index'.")
        print("Otherwise, sidebar and TOC match.")
        return 0
    else:
        if toc_extras:
            print("TOC has extra entries not found in sidebar:", toc_extras)
        if sidebar_extras:
            print("Sidebar has extra entries not found in TOC:", sidebar_extras)
        return 1

        
if __name__ == '__main__':
    #args = sys.argv[1:]
    #
    #if not args:
    #    print("Usage: crosscheck_nav_sidebar sidebarfile tocfilename")
    #    sys.exit(1)

    main("_templates/static_nav.html","_toc.yml")
