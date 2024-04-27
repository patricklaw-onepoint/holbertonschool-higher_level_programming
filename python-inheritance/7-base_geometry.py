#!/usr/bin/python3
"""Python - Inheritance"""


class BaseGeometry:
    """Class for a basic shape"""

    def area(self):
        """TODO"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""
        if type(value) != int or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
