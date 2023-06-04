import json
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from book_collection.book_collection import BookCollection
from scraper.scraper_database.scraper_database import ScraperDatabase
from arg_parser.arg_parser import ArgParser
from scraper.scraper import ScraperUI


class TestBookCollection(unittest.TestCase):
    def setUp(self):
        self.args = ArgParser()
        self.db = ScraperDatabase()
        self.scraper = ScraperUI(self.args.parsed_args)
        self.db.roll_data = json.load(open("tests/book_dict.json"))
        self.book_collection = BookCollection(self.scraper.dump_data())

    def test_init(self):
        self.assertIsInstance(self.book_collection, BookCollection)

    def test_dump_data_to_json(self):
        expected = self.book_collection.dump_data_to_json()
        result = expected
        self.assertEqual(expected, result)

    def test_dump_list_of_images(self):
        expected = self.book_collection.dump_list_of_images()
        result = expected
        self.assertEqual(expected, result)

    def test_books_collection_mainloop(self):
        expected = self.book_collection.books_collection_mainloop(None)
        result = expected
        self.assertEqual(expected, result)

    def test_books_collection_mainloop_args(self):
        expected = self.book_collection.books_collection_mainloop(("rating", "descending"))
        result = expected
        self.assertEqual(expected, result)

    def test_requested_page_optimized(self):
        expected = self.book_collection.request_pages_optimised_urls(self.book_collection.books_imgs_urls)
        result = expected
        self.assertEqual(expected, result)

    def test_sort_books(self):
        expected = self.book_collection.sort_books(self.book_collection.books, "rating", "descending")
        result = expected
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
