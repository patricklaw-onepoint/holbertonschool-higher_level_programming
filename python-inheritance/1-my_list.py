#!/usr/bin/python3
"""Python - Inheritance"""


class MyList(list):

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
