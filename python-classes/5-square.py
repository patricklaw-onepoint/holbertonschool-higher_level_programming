#!/usr/bin/python3
"""Python - Classes and Objects"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        """Print ASCII art representation of a square with #s"""
        if self.__size == 0:
            print()
        else:
            square_line = "#" * self.__size
            for _ in range(self.__size):
                print(square_line)
