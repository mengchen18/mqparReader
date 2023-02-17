import xml.etree.ElementTree as ET
import re
import pandas as pd
import random

def parse(file):
    result_dict = xml_to_dict(file)
    design = {
      "filePaths" : list(result_dict["filePaths"].values()),
      "experiments" : list(result_dict["experiments"].values()),
      "fractions" : list(result_dict["fractions"].values()),
      "ptms" : list(result_dict["ptms"].values()),
      "paramGroupIndices" : list(result_dict["paramGroupIndices"].values()),
      "referenceChannel" : list(result_dict["referenceChannel"].values())
      }
    df = pd.DataFrame(design)
    res = {
        "fasta" : result_dict["fastaFiles"]["FastaFileInfo"]["fastaFilePath"],
        "experimental_design" : df
        }
    return res

def xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return _element_to_dict(root)


def _element_to_dict(element):
    # create an empty dictionary to store the element's attributes and child elements
    result = {}
    
    # add attributes to the dictionary
    for key, value in element.attrib.items():
        result[key] = value
    
    # add child elements to the dictionary
    for child in element:
        new_key = child.tag
        i = 1
        while new_key in result:
            ap = "".join(random.sample("abcdefghijklmnopqrstuvwxyz1234567890", 5))
            new_key = new_key + "_" + ap
            i += 1
        # if the child has no children, store the text value
        if not child:
            result[new_key] = child.text
        # if the child has children, recursively call _element_to_dict to store them as well
        else:
            result[new_key] = _element_to_dict(child)
    
    return result


