#!/usr/bin/python3
"""Python - Input/Output"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Create instance and check id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r12 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r12.id, 12)
        r89 = Rectangle(10, 2, 0, 0, 89)
        self.assertEqual(r89.id, 89)
        rn999 = Rectangle(10, 2, 0, 0, -999)
        self.assertEqual(rn999.id, -999)
        r0 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r0.id, 0)
        r5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r5), "[Rectangle] (5) 3/4 - 1/2")

    def test_error(self):
        """Test errors"""

        # Test initializing Rectangle with invalid type.
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "2", 10)
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

        # Test modifying width to negative value.
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

        # Test modifying x attribute with a dictionary.
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}

        # Test initializing Rectangle with extra arguments.
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display"""
        captured_output = (
            StringIO()
        )  # Create a string buffer to capture stdout
        sys.stdout = captured_output  # Redirect stdout to our buffer

        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__  # Reset stdout to its original state
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_pos(self):
        """Test display"""
        captured_output = (
            StringIO()
        )  # Create a string buffer to capture stdout
        sys.stdout = captured_output  # Redirect stdout to our buffer

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__  # Reset stdout to its original state
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """Test update"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(1, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test to_dictionary()"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary, {"x": 1, "width": 10, "id": 1, "height": 2, "y": 9}
        )
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(r1 == r2, False)

    def test_save_to_file(self):
        """Test save_to_file()"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                "[]",
            )

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                + '{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]',
            )

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(
                file.read(),
                "[]",
            )

    def test_to_and_from_json_string(self):
        """Test to_json_string() and from_json_string()"""
        list_input = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(
            f"[{type(list_input)}] {list_input}",
            "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, "
            + "{'id': 7, 'width': 1, 'height': 7}]",
        )
        self.assertEqual(
            f"[{type(json_list_input)}] {json_list_input}",
            '[<class \'str\'>] [{"id": 89, "width": 10, "height": 4}, '
            + '{"id": 7, "width": 1, "height": 7}]',
        )
        self.assertEqual(
            f"[{type(list_output)}] {list_output}",
            "[<class 'list'>] [{'id': 89, 'width': 10, 'height': 4}, "
            + "{'id': 7, 'width': 1, 'height': 7}]",
        )


if __name__ == "__main__":
    unittest.main()
