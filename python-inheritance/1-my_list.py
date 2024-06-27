#!/usr/bin/python3
"""Python - Inheritance"""


class MyList(list):
    """Class that prints a sorted list"""

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
