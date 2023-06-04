import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from arg_parser.arg_parser import ArgParser


class TestArgParser(unittest.TestCase):
    def setUp(self):
        self.arg_parser = ArgParser()

    def test_init(self):
        self.assertIsInstance(self.arg_parser, ArgParser)
        
    def test_arg_parser(self):
        result = str(self.arg_parser.flag_sorting_arg_idx)
        expected = result
        self.assertEqual(result, expected)

    def test_args(self):
        result = self.arg_parser.parsed_args
        expected = result
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
