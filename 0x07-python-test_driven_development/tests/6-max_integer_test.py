#!/usr/bin/python3
"""
Unittests for max-integer
"""
import unittest
max_integer = __import('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """Test for max integer"""
    def test_max_integer(self):
        """Tests for the maximum lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_empty(self):
        """If the list is empty """
        self.assertEqual(max_integer([]), None)

    def test_max_negative(self):
        """Tests for negtive values"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_mixed(self):
        """Mixed both positive and negative"""
        self.assertEqual(max_integer([-1, -2, -3, 4]), 4)

    def test_max_one(self):
        """Containing only one item """
        self.assertEqual(max_integer([1]), 1)

if __name = '__main__':
    unittest.main()
