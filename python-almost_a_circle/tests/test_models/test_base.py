#!/usr/bin/python3
"""Python - Input/Output"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Create instance and check id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b12 = Base(12)
        self.assertEqual(b12.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b89 = Base(89)
        self.assertEqual(b89.id, 89)
        bn999 = Base(-999)
        self.assertEqual(bn999.id, -999)
        b0 = Base(0)
        self.assertEqual(b0.id, 0)


if __name__ == "__main__":
    unittest.main()
