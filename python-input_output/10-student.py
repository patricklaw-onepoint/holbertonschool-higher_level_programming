#!/usr/bin/python3
"""Python - Input/Output"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)  # Break length
                for attr in attrs
                if hasattr(self, attr)
            }
