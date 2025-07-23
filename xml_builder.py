import xml.etree.ElementTree as ET

def smart_dict_to_xml(data, root_tag="Account"):
    """
    Builds XML from either:
    - Flat dicts with 'table.column': value keys
    - Nested dicts/lists
    Automatically detects data shape.
    """
    root = ET.Element(root_tag)

    def add_element(parent, key, value):
        # Clean key names for XML tag
        tag = str(key).replace(".", "_").replace(" ", "_")
        
        if isinstance(value, dict):
            # Nested dict → recursive
            child = ET.SubElement(parent, tag)
            for subkey, subval in value.items():
                add_element(child, subkey, subval)
        elif isinstance(value, list):
            # List of dicts → repeated child tags
            for item in value:
                item_tag = tag[:-1] if tag.endswith("s") else tag  # e.g. Consumers → Consumer
                child = ET.SubElement(parent, item_tag)
                if isinstance(item, (dict, list)):
                    add_element(child, item_tag, item)
                else:
                    child.text = str(item)
        else:
            # Base case: primitive value
            child = ET.SubElement(parent, tag)
            child.text = str(value)

    def is_flat_dict(d):
        """
        Detects if dict is flat with 'table.column' keys
        """
        return all(isinstance(k, str) and "." in k for k in d.keys())

    # If flat dict, group by table
    if isinstance(data, dict) and is_flat_dict(data):
        grouped = {}
        for key, val in data.items():
            if val in (None, "", "NULL"):
                continue  # Skip empty values
            table, column = key.split('.', 1)
            if table not in grouped:
                grouped[table] = {}
            grouped[table][column] = val
        # Recurse into grouped dict
        for table, columns in grouped.items():
            add_element(root, table, columns)
    else:
        # Already nested dict or list
        add_element(root, root_tag, data)

    return ET.tostring(root, encoding="utf-8", method="xml").decode()
