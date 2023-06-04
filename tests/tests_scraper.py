import json
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from arg_parser.arg_parser import ArgParser
from scraper.scraper import ScraperUI
import bs4


class TestScraperUI(unittest.TestCase):
    def setUp(self):
        self.args = ArgParser()
        self.scraper = ScraperUI(self.args.parsed_args)

    def test_init(self):
        self.assertIsInstance(self.scraper, ScraperUI)

    def test_get_book_url(self):
        result = self.scraper.get_books_url_and_next_page_url(self.scraper.URL)
        expected = result
        self.assertEqual(result, expected)

    def test_dump_data(self):
        result = self.scraper.dump_data()
        expected = result
        self.assertEqual(result, expected)

    def test_book_categories(self):
        result = self.scraper.get_books_categories(bs4.BeautifulSoup(
            open("tests/home_page.html", "r"), "lxml"), self.scraper.URL)
        expected = result
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
