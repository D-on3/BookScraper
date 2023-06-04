import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from json_operations.json_operations import JsonFile


class TestJsonFile(unittest.TestCase):
    def setUp(self):
        self.json = JsonFile()

    def test_init(self):
        self.assertIsInstance(self.json, JsonFile)

    def test_read(self):
        result = self.json.read("tests/book_dict.json")
        expected = result
        self.assertEqual(result, expected)

    def test_current_data(self):
        result = self.json.current_date()
        expected = result
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
