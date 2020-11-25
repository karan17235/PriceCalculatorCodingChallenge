"""
readJson.py takes a JSON formatted file as an input
ans returns the Json file object.
"""

import json

def readJson(jsonObject):
    """The function takes a json file and read the file if it's valid,
    otherwise throw an error.

    Args:
        jsonObject: Reference to a json file or URL.

    Returns: Python Json object
    """

    try:
        with open(jsonObject) as f:
            json_data = json.load(f)
            return json_data

    except Exception as e:
        raise OSError("Please check the file path and file name")

    
    