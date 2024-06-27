#!/usr/bin/python3
"""Python - Classes and Objects"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        """Print ASCII art representation of a square with #s
        Position moves the square based on a tuple:
            (num of space on the left, num of new line above)
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            square_line = " " * self.__position[0] + "#" * self.__size
            for _ in range(self.__size):
                print(square_line)
