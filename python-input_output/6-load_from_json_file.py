#!/usr/bin/python3
"""Python - Input/Output"""

import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file:"""
    with open(filename) as f:
        return json.load(f)
