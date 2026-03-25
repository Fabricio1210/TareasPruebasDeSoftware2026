import unittest
from unittest.mock import Mock
from FizzBuzz import fizzbuzz

class FizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_string(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_fizzbuzz_returns_same_instance(self):
        self.assertIsInstance(fizzbuzz(1), str)
