#!/usr/bin/python3
"""Python - Input/Output"""


def class_to_json(obj):
    """Function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:"""

    return getattr(obj, "__dict__")
