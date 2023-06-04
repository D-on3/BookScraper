import json
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scraper.filters.books_filters import BookFilters


class BookFiltersTest(unittest.TestCase):
    def setUp(self):
        self.book_filters = BookFilters()
        self.book = json.load(open("tests/book_dict.json"))

    def test_init(self):
        self.assertIsInstance(self.book_filters, BookFilters)

    def test_filtering_rating(self):
        self.book_filters.filters = "rating > 2"
        self.assertEqual(self.book_filters.filtering(self.book), True)

    def test_filtering_rating_false(self):
        self.book_filters.filters = "rating < 3"
        self.assertEqual(self.book_filters.filtering(self.book), False)

    def test_filtering_available(self):
        self.book_filters.filters = "available >10"
        self.assertEqual(self.book_filters.filtering(self.book), True)

    def test_filtering_false(self):
        self.book_filters.filters = "available =10"
        self.assertEqual(self.book_filters.filtering(self.book), False)

    def test_filtering_price(self):
        self.book_filters.filters = "price > 20"
        self.assertEqual(self.book_filters.filtering(self.book), True)

    def test_filtering_price_false(self):
        self.book_filters.filters = "price = 20"
        self.assertEqual(self.book_filters.filtering(self.book), False)

    def test_filtering_description(self):
        self.book_filters.words = "a"
        self.assertEqual(self.book_filters.filtering(self.book), True)

    def test_filtering_description_false(self):
        self.book_filters.words = "hi"
        self.assertEqual(self.book_filters.filtering(self.book), False)

    def test_filtering_title(self):
        self.book_filters.title = "Book"
        self.assertEqual(self.book_filters.filtering(self.book), True)

    def test_filtering_title_false(self):
        self.book_filters.title = "Hello, this is book"
        self.assertEqual(self.book_filters.filtering(self.book), False)


if __name__ == '__main__':
    unittest.main()
