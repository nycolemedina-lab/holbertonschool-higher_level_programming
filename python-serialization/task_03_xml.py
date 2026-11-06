#!/usr/bin/python3
"""
Module for serialization and deserialization using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The destination file name.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The input XML file name.

    Returns:
        dict: A dictionary containing the deserialized key-value pairs.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_dict = {}
    for child in root:
        deserialized_dict[child.tag] = child.text

    return deserialized_dict
