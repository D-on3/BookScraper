import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from scraper.scraper_arguments.scraper_arguments import ScraperArguments
from arg_parser.arg_parser import ArgParser


class TestArgumentScraper(unittest.TestCase):
    def setUp(self):
        self.argument_scraper = ScraperArguments(ArgParser().parsed_args)

    def test_init(self):
        self.assertIsInstance(self.argument_scraper, ScraperArguments)

    def test_genres(self):
        result = self.argument_scraper.genres
        expected = result
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()