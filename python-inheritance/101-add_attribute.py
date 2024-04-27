#!/usr/bin/python3
"""Python - Inheritance"""


def add_attribute(object, attribute, value):
    """Add a new attribute to the object if it's possible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
