import unittest
from unittest.mock import Mock
from StringCalculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_add_one_number(self):
        self.assertEqual(add("1"), 1)

    def test_add_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
    
    def test_add_unknown_quantity_of_numbers(self):
        self.assertEqual(add("1,2,3,4,5,6,7,8,9,10"), 55)

    def test_add_with_newline(self):
        self.assertEqual(add("1,2\n3"), 6)
    
    def test_add_with_newline_error(self):
        with self.assertRaises(Exception):
            add("1,2,\n3")
