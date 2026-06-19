#!/usr/bin/python3

import sys
import yaml
from lxml import etree as ET

import vharfbuzz as vh
import svg_stack

# Margin value of hb-view is in points (1/72 in)
# https://github.com/harfbuzz/harfbuzz/issues/1186#issuecomment-424780696
#
# CSS pixels are 1/96 in
# https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units
#
# :. (72 / 96)pt = 1px
# pix_margin = pt_margin * (96/72)
def _pt_to_px(points):
    """Convert lengths in points to the equivalent in pixels."""
    return points * (72 / 96)


def _px_to_pt(pixels):
    """Convert lengths in pixels to the equivalent in points."""
    return pixels * (96 / 72)


class Illustration():

    def __init__(self, configfile):
        if configfile:
            with open(configfile, 'r') as file:
                config = yaml.safe_load(file)

                self.name = config["name"]
                self.components = config["components"]

                # Optional fill color, defaults to black
                if config["basecolor"]:
                    self.basecolor = config["basecolor"]
                else:
                    self.basecolor = "#000000"

                # Optional list of duplicates to generate
                if config["duplicates"]:
                    self.duplicates = config["duplicates"]
                else:
                    self.duplicates = None

                # Optional list of CSS color classes to assign
                # to <use> elements in output
                if config["colorclasses"]:
                    self.colorclasses = config["colorclasses"]
                else:
                    self.colorclasses = None

                return None

            
    def _build_component(component):
        """Generate an SVG from the defined component formula."""

        buf = vh.buffer
        # test if font exists
        # test if unicodes are provided
        # see if optional margins are provided
        # see if optional features are provided
        
        return svg


    # Can / should this be a property?
    #
    # I don't know why I'd need a getter....
    def set_name(self, new_name):
        """Insert the provided new_name as the prefix token
           for all necessary elements."""
        # I think making this a function will make it easier
        # to generate duplicates when necessary
        return None

    
    # Can / should this be a property?
    #
    # I don't know why I'd need a getter....
    def set_color_classes(self, colorclasses):
        """Assign the provided CSS color classes to the
           <use> elements in the image."""
        # I think making this a function will make it easier
        # to skip this step for PDF (or other noninteractive)
        # output formats.
        return None


    def build(self):
        """Generate all the components in the order defined."""
        sequence = []
        for component in self.components:
            sequence.add(_build_component(component))

        self.svg = svg_stack(sequence)

        # Modify self.svg to set correct viewbox
        # based on its internal width,height
        
        return None

    
    def write_file(self, outputfilename=None):
        """Write the SVG to file."""
        return None
        

def build_svg(configfile):
    """Reads in an illustration configfile and returns an SVG."""

    return svg


def extract_color_classes(filename):
    """Extracts an ordered list of the color classes in an SVG file."""
    from lxml import etree as ET

    namespace = "{http://www.w3.org/2000/svg}"
        
    with open(filename, 'r+t', encoding='utf-8') as svg:
        tree = ET.parse(svg)
        root = tree.getroot()

        d = root.nsmap
        if (root.tag != namespace + "svg"):
            raise Exception("Parsing trouble; it's unclear if the SVG file is compatible.")
        else:
            colorclasses = []
            elems =  list(root.iter())
            for elem in elems:
                if (elem.tag == namespace + "use"):
                    if "class" in elem.attrib:
                        colorclasses.append(elem.attrib["class"])
                    else:
                        print("Found <use> element with no classes:", elem)

    return colorclasses


def _build_colorclasslist(filename):
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

    
def _build_duplicates(filename):
    """Inserts YAML configuration for SVG images that are duplicates
       of another illustration.

       This is a bootstrapping function used solely to migrate the old,
       'SCRIPT-svg-generation-log.md' files to YAML configuration.

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
                print(line)
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
                print(f'Appending to {target}.yaml')
                yaml_out = (
                    f'duplicates:\n'
                )
                
                for duplicate in duplicate_list:
                    yaml_out += duplicate

                # Write to file
                outfile.write(yaml_out)

    return None
    
    
def _build_yaml(filename):
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
                    filename_parts = params["output-file"].rpartition("-")
                    if len(filename_parts) < 3:
                        params["target"] = params["output-file"]
                        params["name"] = params["output-file"][:-4]
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
                    print(params)
                    
            # The `line` processing is complete.
        
        # Processing all the lines is complete.
        
        # Iterate through the data, starting a new YAML file for each
        # `target`...
        for target, component_list in output_files.items():
            with open(target + ".yaml", 'w', encoding='utf-8') as outfile:
                # This overwrites the file entirely, which is OK because
                # we're just bootstrapping the old repo into the new format.
                print(f'Writing {target}.yaml')
                yaml_out = (
                    f'name: {target}\n'
                    f'basecolor: #000000\n'
                    f'SCRIPTFONT: {script_font}\n' # stray \n sneaks in here?
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
            print("Uh-oh; no arrow font.")
            arrow_font = ""

    return None

if __name__ == '__main__':
    #extract_color_classes(sys.argv[1])
    _build_yaml(sys.argv[1])
    _build_duplicates(sys.argv[1])
