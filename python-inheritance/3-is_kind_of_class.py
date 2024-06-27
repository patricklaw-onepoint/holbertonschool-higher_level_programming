#!/usr/bin/python3
"""Python - Inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class"""
    return isinstance(obj, a_class)
