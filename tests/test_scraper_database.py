import json
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scraper.scraper_database.scraper_database import ScraperDatabase


class TestScraperDatabase(unittest.TestCase):
    def setUp(self):
        self.data_base = ScraperDatabase()

    def test_init(self):
        self.assertIsInstance(self.data_base, ScraperDatabase)

    def test_fetch_all(self):
        result = self.data_base.fetch_all()
        expected = result
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
