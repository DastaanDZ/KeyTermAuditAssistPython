import json
import os

def load_keyterms(filename=None):
    if filename is None:
        # Default to the expected path
        filename = os.path.join(os.path.dirname(__file__), 'keyterms.json')
    with open(filename, 'r') as f:
        return json.load(f)

def get_term_data(keyterms_data, keyterm):
    entry = keyterms_data.get(keyterm)
    if not entry:
        return None
    result = {
        "regex": entry.get("regex"),
        "description": entry.get("description"),
        "must": entry.get("must"),
    }
    if "must_not" in entry:
        result["must_not"] = entry["must_not"]
    return result