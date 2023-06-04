import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bs4 import BeautifulSoup
from scraper.scraper_parsing.multi_page_parsing.scraper_collective_books_page import ScraperCollectiveBooksPage
from arg_parser.arg_parser import ArgParser
from scraper.scraper import ScraperUI


class TestCollectiveBook(unittest.TestCase):
    def setUp(self):
        self.collective_books = ScraperCollectiveBooksPage()
        self.args = ArgParser()
        self.scraper = ScraperUI(self.args.parsed_args)
        self.data = BeautifulSoup(open("tests/home_page.html", "r"), "lxml")

    def test_init(self):
        self.assertIsInstance(self.collective_books, ScraperCollectiveBooksPage)

    def test_get_book_categories(self):
        expected = self.collective_books.get_books_categories(self.data, self.scraper.URL)
        result = expected
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
