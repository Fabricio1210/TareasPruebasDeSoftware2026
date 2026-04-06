import unittest
from unittest.mock import Mock
from StringCalculator import Add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_add_one_number(self):
        self.assertEqual(add("1"), 1)

    def test_add_two_numbers(self):
        self.assertEqual(add("1,2"), 3)