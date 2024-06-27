#!/usr/bin/python3
"""Python - Input/Output"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string info for square"""
        return (
            f"[{type(self).__name__}] ({self.id}) "  #
            f"{self.x}/{self.y} - {self.width}"
        )

    def __update(self, id=None, size=None, x=None, y=None):
        """Update instance attributes with args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update instance attributes with args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Dictionary representation of this square"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
