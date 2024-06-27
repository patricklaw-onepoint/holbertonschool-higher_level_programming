#!/usr/bin/python3
"""Python - Input/Output"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        from json import dumps

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        from json import loads

        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with dummy (1s) mandatory attributes"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        else:
            new = Square(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads string from file and returns a list of instances"""
        from os import path

        file = f"{cls.__name__}.json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**i) for i in cls.from_json_string(f.read())]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        import turtle
        import random

        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        random.shuffle(colors)
        color_index = 0
        turtle.Screen().bgcolor("black")
        t = turtle.Turtle()
        t.hideturtle()

        for i in list_rectangles + list_squares:
            t.pensize(color_index)
            t.color(colors[color_index])
            t.penup()
            t.goto(i.x, i.y)
            t.pendown()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()
            color_index = (color_index + 1) % len(colors)

        turtle.done()  # Keep the window open
