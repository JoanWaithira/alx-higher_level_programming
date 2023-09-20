#!/usr/bin/python3
"""
    Test module for class BaseModel and methods in it
"""
import os
import unittest
import json
import csv

from models.base import BaseModel
from models.rectangle import Rectangle
from models.square import Square


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel"""

    def setUp(self):
        """Set up objects"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        self.base4 = BaseModel()

    def tearDown(self):
        """Delete created objects for test"""
        del self.base1
        del self.base2
        del self.base4

    def test_no_id(self):
        """Test for no args"""
        self.assertEqual(self.base1.id, self.base2.id - 1)
        self.assertEqual(self.base1.id, self.base4.id - 2)

    def test_unique_id(self):
        """Test for unique arg"""
        base3 = BaseModel(14)

        self.assertEqual(self.base1.id, self.base2.id - 1)
        self.assertEqual(self.base1.id, self.base4.id - 2)
        self.assertEqual(14, base3.id)

    def test_access_private_attribute(self):
        """Test for Error thrown if access to private class instance"""
        with self.assertRaises(AttributeError):
            print(BaseModel.__nb_objects)


class TestJson(unittest.TestCase):
    """Tests JSON representations"""

    def setUp(self):
        """Set up objects"""
        self.rect = Rectangle(23, 44)
        self.sqr = Square(23, 44)
        self.tuple_arg = (1, 3)

    def tearDown(self):
        """Delete created objects for test"""
        del self.rect
        del self.sqr
        del self.tuple_arg

    def test_to_json_string(self):
        """Test the to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3, 1, 4)

        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()

        list_dict = [r1_dict, r2_dict]

        json_dictionary = BaseModel.to_json_string(list_dict)
        json_empty_dict = BaseModel.to_json_string([])

        self.assertIsInstance(r1_dict, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(json_empty_dict, "[]")
        self.assertIsInstance(json_empty_dict, str)

    def test_save_to_file(self):
        """Test save_to_file for Rectangle class"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        rect = Rectangle(4, 10, 1, 0, 7)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r", encoding="utf-8") as m_file:
            content = m_file.read()

        res = [{"id": 7, "width": 4, "height": 10, "x": 1, "y": 0}]
        self.assertEqual(res, json.loads(content))

    def test_save_to_file_not_subclass(self):
        """Tests if objects' class are not subclasses of BaseModel"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([self.rect, self.tuple_arg])

    def test_save_to_file_none(self):
        """Test for saving empty or None argument"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as r_file:
            content1 = r_file.read()
        self.assertEqual("[]", content1)

        with open("Square.json", "r", encoding="utf-8") as s_file:
            content2 = s_file.read()
        self.assertEqual("[]", content2)

    def test_save_to_file_square(self):
        """Test save_to_file for Square class"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        sqr = Square(4, 10, 10, 67)
        Square.save_to_file([sqr])

        with open("Square.json", "r", encoding="utf-8") as m_file:
            content = m_file.read()

        res = [{"id": 67, "size": 4, "x": 10, "y": 10}]
        self

