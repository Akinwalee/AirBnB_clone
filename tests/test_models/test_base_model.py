#!usr/bin/env python3
"""Module for testing the BaseModel class"""

from .models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Class of tests for the amenity class"""

    def test_variables(self):
        """test the instance variables"""
        pass

    def test__str__(self):
        """tests the str method"""
        pass

    def test_save(self):
        """tests the save method"""
        pass

    def test_to_dict(self):
        """tests te to_dict method"""
        pass


if __name__ == '__main__':
    unittest.main()
