#!/usr/bin/python3
"""Python - Input/Output"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value, True)
        self.__y = value

    def integer_validator(self, name, value, can_equal):
        """Check validity of variables"""
        if type(value) is not int or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if can_equal and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not can_equal and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle with #"""
        output = [""] * self.__y + [
            " " * self.__x + "#" * self.__width
        ] * self.__height
        print("\n".join(output))

    def __str__(self):
        """Returns string info for rectangle"""
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Update instance attributes with args"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update instance attributes with args"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Dictionary representation of this rectangle"""
        return {
            "x": self.__x,
            "width": self.__width,
            "id": self.id,
            "height": self.__height,
            "y": self.__y,
        }
