#!/usr/bin/python3
"""Python - Input/Output"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleSquare(unittest.TestCase):
    """Test cases for Rectangle and Square classes"""

    def setUp(self):
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.list_rectangles_input = [self.r1, self.r2]
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)
        self.list_squares_input = [self.s1, self.s2]

    def test_save_load_rectangle(self):
        # Save rectangles to file
        Rectangle.save_to_file(self.list_rectangles_input)

        # Load rectangles from file
        loaded_rectangles = Rectangle.load_from_file()

        # Assert that the loaded rectangles match the original ones
        self.assertEqual(
            len(loaded_rectangles), len(self.list_rectangles_input)
        )
        for i, rect in enumerate(loaded_rectangles):
            self.assertEqual(
                rect.__dict__, self.list_rectangles_input[i].__dict__
            )

    def test_save_load_square(self):
        # Save squares to file
        Square.save_to_file(self.list_squares_input)

        # Load squares from file
        loaded_squares = Square.load_from_file()

        # Assert that the loaded squares match the original ones
        self.assertEqual(len(loaded_squares), len(self.list_squares_input))
        for i, square in enumerate(loaded_squares):
            self.assertEqual(
                square.__dict__, self.list_squares_input[i].__dict__
            )


if __name__ == "__main__":
    unittest.main()
