# xml_builder.py
import xml.etree.ElementTree as ET

def dict_to_xml(tag, data):
    """Convert dict to XML recursively, skipping empty/null fields."""
    elem = ET.Element(tag)
    if isinstance(data, dict):
        for key, val in data.items():
            if val is None or val == "" or val == []:
                continue  # Skip empty/null fields
            if isinstance(val, (dict, list)):
                child = dict_to_xml(key, val)
                if len(child):  # Only add if child has non-empty content
                    elem.append(child)
            else:
                child = ET.SubElement(elem, key)
                child.text = str(val)
    elif isinstance(data, list):
        for item in data:
            child = dict_to_xml(tag[:-1], item)  # Singularize tag for list items
            if len(child):  # Only add if child has non-empty content
                elem.append(child)
    return elem

def save_xml(root, file_name):
    """Write XML tree to file."""
    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
