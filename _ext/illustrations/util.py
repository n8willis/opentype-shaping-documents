#!/usr/bin/python3
# SPDX-FileCopyrightText: Copyright 2026 Nathan Willis
#
# SPDX-License-Identifier: BSD-2-Clause
"""Auxillary utilities for illutsration-building."""

def sample_page(dirname):
    """Returns a before-and-after sample page comparing all SVG illustration
       pairs in the given directory. Any standalone SVG files are also
       rendered, in their own section."""
    import os
    import pathlib
    from lxml import etree as ET

    
    dir_short = os.path.basename(os.path.normpath(dirname)) # Keepin' the HTML tidy
    htmlpage = (
        f'<html>\n'
        f'<head>\n<title>SVG samples from {dir_short}</title>\n</head>\n'
        f'<body>\n'
        f'<h1>SVGs found in {dirname}</h1>\n<br>\n'
        f'<h2>Before-and-after pairs:</h2>\n'
        f'<table>\n<thead>\n<tr><th>Before</th><th>After</th></tr>\n</thead>\n'
        f'<tbody>\n'
        )

    svgs = list(pathlib.Path(dirname).glob('*.svg'))

    #svgs = list(pathlib.Path(dirname, pathlib.Path(dirname).glob('*.svg') ))
    #svgs2 = [pathlib.Path(dirname, s) for s in svgs]
    #print(svgs2)
    befores = sorted([s for s in svgs if "-before" in str(s)])
    afters = sorted([s for s in svgs if "-after" in str(s)])
    stubs = [str(s).rpartition("-before.svg")[0] for s in befores]
    #print(svgs)

    #
    # This pair-finding method fails if any of the expected component
    # SVG files is missing. It might also fail on `right-arrow.svg` in
    # the case where there are filenames alphabetically after it.
    svg_pairs = [ [b, a] for b,a in zip(befores, afters) if str(b).rpartition("-before.svg")[0] == str(a).rpartition("-after.svg")[0]]

    if len(svg_pairs) > 0:
        for pair in svg_pairs:
            print(f'pair: {pair}', file=sys.stderr)
            # update with _insert_ids() and _insert_viewbox() steps here
            # on pair[0] and pair[1]
            #
            # The immutability of the string variables here is why we need
            # to replace that with a svgComponent class that has a tree
            # representation attribute....
            #with open(pair[0], 'r+t', encoding='utf-8') as b, open(pair[1], 'r+t', encoding='utf-8') as a:
            b = Path(pair[0]).read_text()
            print(f'b:: {b}', file=sys.stderr) # debugging: somehow this isn't becoming a string?
            a = Path(pair[1]).read_text()
            bv = _insert_viewbox(b)
            av = _insert_viewbox(a)
            bi = _insert_ids(bv, str(os.path.basename(pair[0])))
            ai = _insert_ids(av, str(os.path.basename(pair[1])))
            
            htmlpage += (
                f'<tr><td>{str(os.path.basename(pair[0]))}<br>'
                #f'<img src="{pair[0]}">' # when we are inlining the SVGs, we'll replace the <img> element here
                f'{bi.decode('utf-8')}'
                f'</td><td>{str(os.path.basename(pair[1]))}<br>'
                #f'<img src="{pair[1]}">' # when we are inlining the SVGs, we'll replace the <img> element here
                f'{ai.decode('utf-8')}'
                f'</td></tr>\n'
            )
            svgs.remove(pair[0])
            svgs.remove(pair[1])
        
    htmlpage += (
        f'</tbody>\n'
        f'</table>\n'
        )

    if len(svgs) > 0:
        htmlpage += (
            f'<br>\n'
            f'<h2>Unpaired SVGs:</h2>\n'
            f'<table>\n<thead>\n<tr><th>Image</th></tr>\n</thead>\n'
            f'<tbody>\n'
        )

        for svg in svgs:
        # update with _insert_ids() and _insert_viewbox() steps here
            s = Path(svg).read_text()
            print(f"s:: {s}", file=sys.stderr)
            svgv = _insert_viewbox(s)
            svgi = _insert_ids(svgv, str(os.path.basename(svg)))
            htmlpage += (
                #f'<tr><td>{str(os.path.basename(svg))}<br><img src="{svg}"></td></tr>\n' #when we are inlining the SVGs, we'll replace the <img> element here
                f'<tr><td>{str(os.path.basename(svg))}<br>{svgi.decode('utf-8')}</td></tr>\n'
            )

        htmlpage += (
            f'</tbody>\n'
            f'</table>\n'
        )
        
    htmlpage += (
        f'</tbody>\n'
        f'</body>\n'
        f'</html>'
        )
    
    return htmlpage
    #print([str(s) for s in svgs])
    #print(befores)
    #print(afters)
    #print(stubs)
    #print(svg_pairs)
    #print(htmlpage)
    #print(svgs)
    #return None

def _bootstrap_colorclasslist(filename):
    """Inserts YAML configuration for SVG images, capturing the CSS
       color classes applied to each <use> element, in order.

       This is a bootstrapping function used solely to migrate the old,
       'SCRIPT-svg-generation-log.md' files to YAML configuration.

       Some of the log files already contain the necessary information.
       In those cases, it is written as-is into the .yaml configuration
       files on a per-image basis. For the other log files, the function
       bootstraps that information by extracting it from the current
       .svg files.

       Consequently, this function remains private, because in the long
       term, the build tool cannot rely on the "current as of now" files
       containing the necessary color classes.
    """

    return None

    
def _bootstrap_duplicates_to_line(filename):
    """Inserts YAML configuration for SVG images that are duplicates
       of another illustration.

       This is a bootstrapping function used solely to migrate the old,
       'SCRIPT-svg-generation-log.md' files to YAML configuration.

       This version inserts references to duplicates as a `duplicate`
       line within the YAML file for each original file.

       It is NOT clear at the time of writing whether or not such a
       configuration is ideal.

       For the alternative approach, see _bootstrap_duplicates_to_file().

       Args:
           filename: an svg-image-generation-log.md file containing the
             hb-view and svg_stack.py commands used to build the images
             in the current directory. This function only acts on `cp`
             commands found within the file. It has no function otherwise.
    
       Returns:
           None
    
       Appends:
           Adds lines to the end of set of *.yaml files, each of which
           is named for the script-feature combination that original
           SVG image should illustrate. This function adds a `duplicates`
           block, where needed, indicating that the image builder must
           make copies of the configured image (with the supplied list
           noting what the copies need to be named, and implicitly how
           many of them there will be."""
    from collections import defaultdict
    
    output_files = defaultdict(list)
    
    with open(filename, 'r+t', encoding='utf-8') as log:
        lines = log.readlines()
        for line in lines:
            
            params = {}
            if line[:2] == "cp":
                print(line, file=sys.stderr)
                # Hmm. We don't have params yet....
                #   ** fixed; the declaration up & out of the with() block
                p = line[2:].split()
                params["target"] = p[0][:-4]
                params["duplicate"] = p[1][:-4]

                # create a YAML `duplicate` element and add it
                # to the output_files collection
                #
                yaml_duplicate = (
                    f'- {params["duplicate"]}\n'
                )

                output_files[params["target"]].append(yaml_duplicate)

    # Iterate through all the output files,
    # 1. open the EXISTING "target" file in "append" mode
    # 2. Start a "duplicates" block
    # 3. Iterate through all the duplicates, adding each on its own line
    for target, duplicate_list in output_files.items():
            with open(target + ".yaml", 'a', encoding='utf-8') as outfile:
                print(f'Appending to {target}.yaml', file=sys.stderr)
                yaml_out = (
                    f'duplicates:\n'
                )
                
                for duplicate in duplicate_list:
                    yaml_out += duplicate

                # Write to file
                outfile.write(yaml_out)

    return None
    
    
def _bootstrap_duplicates_to_file(filename):
    """Generates YAML configuration for SVG images that are duplicates
       of another illustration.

       This is a bootstrapping function used solely to migrate the old,
       'SCRIPT-svg-generation-log.md' files to YAML configuration.

       This version creates a standalone YAML file for each duplicate
       image, with that YAML file containing a reference to the original
       file.

       It is NOT clear at the time of writing whether or not such a
       configuration is ideal.

       For the alternative approach, see _bootstrap_duplicates_to_line().

       Args:
           filename: an svg-image-generation-log.md file containing the
             hb-view and svg_stack.py commands used to build the images
             in the current directory. This function only acts on `cp`
             commands found within the file. It has no function otherwise.
    
       Returns:
           None
    
       Writes:
           A set of *.yaml files, each of which is named for the output filename
           of the duplicate SVG file that should be generated (with the .yaml
           extension replacing the .svg extension to be used in the final image),
           and each of which contains a one-line "duplicates: foo" line that
           designates the name of the original file that will be duplicated to
           result in the final image file."""

    base_dir = Path(filename).parents[0]
    
    with open(filename, 'r+t', encoding='utf-8') as log:
        lines = log.readlines()
        for line in lines:
            
            if line[:2] == "cp":
                print(f'File {filename}, line: {line}', file=sys.stderr)
                # Hmm. We don't have params yet....
                #   ** fixed; the declaration up & out of the with() block
                p = line[2:].split()
                target = p[0][:-4]
                duplicate = p[1][:-4]

                with open(Path(base_dir, duplicate + ".yaml"), 'w+t', encoding='utf-8') as outfile:
                    print(f'Writing {duplicate}.yaml', file=sys.stderr)
                    yaml_out = (
                        f'name: {duplicate}\n'
                        f'duplicates: {target}\n'
                        )

                    #print(yaml_out, file=sys.stderr) # Here we'd actually write the file
                    outfile.write(yaml_out)

    return None
    
    
def _bootstrap_yaml(filename):
    """Builds a YAML configuration file from an SVG generation log entry.

       This is a bootstrapping function used solely to migrate the old,
       'SCRIPT-svg-generation-log.md' files to YAML configuration.

       Args:
           filename: an svg-image-generation-log.md file containing the
             hb-view and svg_stack.py commands used to build the images
             in the current directory.
    
       Returns:
           None
    
       Writes:
           A set of *.yaml files, each named for the script-feature
           combination that the SVG image should illustrate."""

    from collections import defaultdict

    base_dir = Path(filename).parents[0]

    # Let's just collect the results as raw YAML, then sort them out later.
    output_files = defaultdict(list)

    # Might be more useful to pass in values as function parameters?
    arrow_font = ""
    script_font = ""
    params = {}
    
    with open(filename, 'r+t', encoding='utf-8') as log:
        lines = log.readlines()
        for line in lines:
            # Capture any existing filepath definitions...
            # - This won't be necessary in general, but some existing
            #   svg-generation-logs have already been touched.
            if line[:10] == "ARROWFONT=":
                arrow_font = line[10:]
            elif line[:11] == "SCRIPTFONT=":
                script_font = line[11:-1] # :-1 cuts off the newline

            # Handle hb-view lines...
            # - Each line can only represent one component.
            elif line[:8] == "hb-view ":
                # Start a new YAML 'component'...
                #
                # Convert command arguments into a dictionary.
                #
                # This doesn't work; the font parameter doesn't use '='
                #params = {k: v for k, v in map(lambda x: x.replace("$").replace()..split("="), cmd)}
                #params = [i for i in cmd if "=" in i]
                
                #params = {}
                for param in line[8:].split():
                    if "=" not in param:
                        if param[:2] == "--": # extra flags !
                            params["options"] += param # actually, there could be more than one of these....
                        else:
                            params["font"] = param
                    else:
                        p = param.split("=")
                        params[p[0][2:]] = p[1]
                #print(params) # debugging
                

                # Get the component name from 'output-file'...
                #
                if params["output-file"] == "right-arrow.svg":
                    # It's the right-arrow command, which is
                    # a special case we only need to generate
                    # once in the entire directory.
                    #params["target"] = "arrow" # The 'target' is not part of the right-arrow generation command.
                    yaml_component = (
                        f'- arrow:\n'
                        f'  - file: right-arrow.svg'
                        )
                else:
                    # This actually fails for the right-arrow SVG.
                    # But we actually only need that once. So we
                    # shouldn't re-generate it for every illustration
                    # anyway....
                    # [x] :. special-case 'right-arrow.svg'
                    #
                    # Actually, this also fails for the single-component
                    # images, too. E.g., khmer-robat.svg, tibetan-syllable.svg
                    # [ ] - :. add test for how many "-" there are?
                    #filename_parts = params["output-file"].rpartition("-")
                    filename_parts = params["output-file"].split("-")
                    #print(filename_parts) # Debug
                    if len(filename_parts) < 3:
                        params["target"] = params["output-file"][:-4]
                        #params["name"] = params["output-file"][:-4]
                                         # probably a different component-name is needed
                        params["name"] = "SOLE_COMPONENT" # special case in builder
                    else:
                        params["target"] = params["output-file"].rpartition("-")[0]
                        params["name"] = params["output-file"].rpartition("-")[2][:-4]

                    # `unicodes` is required; other parameters have defaults...
                    # - Pass through unicodes as-is...
                    # - Pass through margin as-is...
                    # - Pass through features as-is...

                    # The font is also required, but may be set already...
                    # Get font if it's not SCRIPTFONT...

                    yaml_component = (
                        f'- {params["name"]}:\n'
                        f'    unicodes: {params["unicodes"]}\n'
                        )

                    if params["font"] != "$SCRIPTFONT":
                        yaml_component += (
                            f'    font: {params["font"]}\n'
                            )

                    if params["margin"]:
                        yaml_component += (
                            f'    margin: {params["margin"]}\n'
                            )

                    if params["features"]:
                        yaml_component += (
                            f'    features: {params["features"]}\n'
                            )

                    # Add this component block to the collection for output
                    output_files[params["target"]].append(yaml_component)

                # Debugging to console output, because special cases happen....
                if params["font"] != "$SCRIPTFONT":
                    # This image needs a non-standard example font:
                    print(f"Warning, non-standard font {params}", file=sys.stderr)
                    
            # The `line` processing is complete.
        
        # Processing all the lines is complete.
        
        # Iterate through the data, starting a new YAML file for each
        # `target`...
        for target, component_list in output_files.items():
            with open(Path(base_dir, target + ".yaml"), 'w', encoding='utf-8') as outfile:
                # This overwrites the file entirely, which is OK because
                # we're just bootstrapping the old repo into the new format.
                print(f'Writing {outfile}', file=sys.stderr)
                yaml_out = (
                    f'name: {target}\n'
                    f'generator: hb-view\n'
                    f'font: {script_font}\n' # stray \n sneaks in here?
                    f'basecolor: 000000\n'
                    f'components:\n'
                ) 
                # Add each of the collected components in its own block...
                #
                # Actually, we need to do this in a specific
                # order: -before, -arrow, -after....
                #
                # Or else have the builder Just Know that order....
                #
                # That's probably fine, since the order in the un-converted
                # -log.md files is predictably correct.
                for component in component_list:
                    yaml_out += component

                # TODO (maybe?):
                #
                # handle CSS color-codes?
                # 1. must be run on 'target' final filename
                # 2. must be run AFTER all components.
                # 3. :. must be done outside _build_yaml() or at least
                #    outside this loop.
                #   3.1. have _build_yaml() return yaml string,
                #   3.2. make a _write_yaml() that takes yaml string input
                # 4. some existing files have cluster_styles lines already
                #
                # insert a right-arrow block?
                # 1. It's probably the same for every SVG illustration
                #    in the directory
                # 2. But we can't fully assume that every image needs it
                #    or places it in the correct order. There are some
                #    examples like alternate forms that JUST show some
                #    glyphs in sequence, with no arrow....
                # 3. Bigger question is whether to use a different YAML
                #    config file (and reference it) for each arrow use,
                #    or to generate every one.

                # Write to file
                outfile.write(yaml_out)

                
        if not arrow_font:
            print("Uh-oh; no arrow font.", file=sys.stderr)
            arrow_font = ""

    return None
