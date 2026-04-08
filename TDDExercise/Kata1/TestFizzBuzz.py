import unittest
from unittest.mock import Mock
from FizzBuzz import fizzbuzz

class FizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_string(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_fizzbuzz_returns_same_instance(self):
        self.assertIsInstance(fizzbuzz(1), str)

    def test_fizzbuzz_is_multiple_of_3(self):
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_fizzbuzz_is_not_multiple_of_3(self):
        self.assertEqual(fizzbuzz(7), "7")

    def test_fizzbuzz_is_multiple_of_5(self):
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz_is_not_multiple_of_5(self):
        self.assertEqual(fizzbuzz(11), "11")
    
    def test_fizzbuzz_is_not_multiple_of_5_and_3(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")