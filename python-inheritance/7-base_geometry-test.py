#!/usr/bin/python3
import unittest

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class TestBaseGeometry(unittest.TestCase):
    def test_area_not_implemented(self):
        with self.assertRaises(Exception):
            BaseGeometry().area()

    def test_integer_validator_type_error(self):
        with self.assertRaises(TypeError):
            BaseGeometry().integer_validator("size", "not an integer")

    def test_integer_validator_value_error(self):
        with self.assertRaises(ValueError):
            BaseGeometry().integer_validator("size", 0)

    def test_integer_validator_value_error(self):
        with self.assertRaises(ValueError):
            BaseGeometry().integer_validator("size", -1)

    def test_integer_validator_success(self):
        BaseGeometry().integer_validator("test", 5)


if __name__ == "__main__":
    unittest.main()
