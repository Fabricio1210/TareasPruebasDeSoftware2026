import unittest
from SearchFunctionality import search
from hypothesis import given, strategies as st
import os
import json

class TestSearchFunctionality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
        with open(cities_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            cls.cities = data["cities"]

    @given(search_value=st.from_regex(r"[a-z]"))
    def test_search_few_chars(self, search_value):
        self.assertEqual(search(search_value), [])

    def test_search_multiple_cities_starts_with(self):
        result = search("Va")
        self.assertIn("Valencia", result)
        self.assertIn("Vancouver", result)

    def test_search_case_insensitive(self):
        result = search("vancouver")
        self.assertEqual(result, ["Vancouver"])

    def test_search_any_part_of_string(self):
        result = search("ape")
        self.assertEqual(result, ["Budapest"])

    def test_search_asterisk_returns_all(self):
        result = search("*")
        self.assertEqual(len(result), len(self.cities))
        self.assertEqual(result, self.cities)