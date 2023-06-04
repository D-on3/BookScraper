import json
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scraper.scraper import ScraperUI
from scraper.scraper_parsing.single_page_parsing.scraper_single_book_page import ScraperSingleBookPageMixin


class TestSingleBookPage(unittest.TestCase, ScraperSingleBookPageMixin):

    def setUp(self):
        self.soup = self.scrape_init(open("tests/a_light_in_the_attic.html"))
        self.book_from_json = json.load(open("tests/a_light_in_the_attic_dict.json"))
    def test_get_soup_of_pages_true(self):
        result = self.get_soup_of_page(ScraperUI.URL)
        expected = result
        self.assertEqual(result, expected)

    def test_get_soup_of_pages_false(self):
        result = self.get_soup_of_page(ScraperUI.URL)
        expected = None
        self.assertNotEqual(result, expected)

    def test_custom_request_invalid_url(self):
        result = str(self.get_soup_of_page("http://None.com"))
        expected = "<html>\n<head></head>\n<body></body>\n</html>\n"
        self.assertEqual(result, expected)

    def test_scrape_init(self):
        result = self.scrape_init(open("tests/home_page.html", "r"))
        expected = result
        self.assertEqual(result, expected)

    def test_scrape_init_false(self):
        result = self.scrape_init(open("tests/home_page.html", "r"))
        expected = None
        self.assertNotEqual(result, expected)

    def test_clean_collected_data_one_url_title(self):
        expected = self.clean_collected_data_one_url(self.soup)
        result = self.book_from_json
        self.assertEqual(result['title'], expected['title'])

    def test_clean_collected_data_one_url_title_false(self):
        expected = self.clean_collected_data_one_url(self.soup)
        self.assertNotEqual(expected['title'], None)

    def test_clean_collected_data_one_url_price(self):
        expected = self.clean_collected_data_one_url(self.soup)
        result = self.book_from_json
        self.assertEqual(result['price'], expected['price'])

    def test_clean_collected_data_one_url_price_false(self):
        expected = self.clean_collected_data_one_url(self.soup)
        self.assertNotEqual(expected['price'], None)

    def test_clean_collected_data_one_url_description(self):
        expected = self.clean_collected_data_one_url(self.soup)
        result = self.book_from_json
        self.assertEqual(result['description'], expected['description'])

    def test_clean_collected_data_one_url_description_false(self):
        expected = self.clean_collected_data_one_url(self.soup)
        self.assertNotEqual(expected['description'], None)

    def test_clean_collected_data_one_url_rating(self):
        expected = self.clean_collected_data_one_url(self.soup)
        result = self.book_from_json
        self.assertEqual(result['rating'], expected['rating'])

    def test_clean_collected_data_one_url_rating_false(self):
        expected = self.clean_collected_data_one_url(self.soup)
        self.assertNotEqual(expected['rating'], None)

    def test_clean_collected_data_one_url_available(self):
        expected = self.clean_collected_data_one_url(self.soup)
        result = self.book_from_json
        self.assertEqual(result['available'], expected['available'])

    def test_clean_collected_data_one_url_available_false(self):
        expected = self.clean_collected_data_one_url(self.soup)
        self.assertNotEqual(expected['available'], None)


if __name__ == '__main__':
    unittest.main()
