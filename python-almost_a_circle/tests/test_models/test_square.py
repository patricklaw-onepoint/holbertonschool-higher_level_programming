#!/usr/bin/python3
"""Python - Input/Output"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Create instance and check id"""
        self.assertEqual(str(Square(10, 2)), "[Square] (1) 2/0 - 10")
        self.assertEqual(str(Square(1, 2, 3, 4)), "[Square] (4) 2/3 - 1")

    def test_error(self):
        """Test errors"""
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)

        s = Square(5)
        self.assertEqual(s.size, 5)

        with self.assertRaises(TypeError):
            s.size = "9"

    def test_area(self):
        """Test area"""
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_display(self):
        """Test display"""
        captured_output = (
            StringIO()
        )  # Create a string buffer to capture stdout
        sys.stdout = captured_output  # Redirect stdout to our buffer

        s1 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 3")
        self.assertEqual(s1.area(), 9)
        s1.display()
        sys.stdout = sys.__stdout__  # Reset stdout to its original state
        expected_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update(self):
        """Test update"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary()"""
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {"id": 1, "x": 2, "size": 10, "y": 1})
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertEqual(s1 == s2, False)

    def test_save_to_file(self):
        """Test save_to_file()"""
        Square.save_to_file(None)

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                "[]",
            )

        s1 = Square(1)
        Square.save_to_file([s1])

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                '[{"id": 1, "x": 0, "size": 1, "y": 0}]',
            )

        Square.save_to_file([])

        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                "[]",
            )


if __name__ == "__main__":
    unittest.main()
