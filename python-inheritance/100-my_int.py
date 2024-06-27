#!/usr/bin/python3
"""Python - Inheritance"""


class MyInt(int):
    """Inherit from int but swap == and !="""

    def __eq__(self, value):
        """Override == with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != with =="""
        return self.real == value
