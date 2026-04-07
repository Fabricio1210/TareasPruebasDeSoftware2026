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
        self.assertEqual(add("1,2,\n3"),6)
    
    def test_add_with_separator_at_the_final(self):
        with self.assertRaises(ValueError):
            add("1,2,\n3,4,")

    def test_add_with_delimiters_1(self):
        self.assertEqual(add("//;\n1;3"), 4)

    def test_add_with_delimters_2(self):
        self.assertEqual(add("//sep\n2sep5"), 7)