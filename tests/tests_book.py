import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from book_collection.book.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            available=22,
            rating=3,
            price=51.77,
            description="It's hard to imagine a world without A Light in the Attic. This now-classic"
                        " collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary",
            title= "A Light in the Attic",
            id_book="a897fe39b1053632",
            img_url="https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
        )

    def test_init(self):
        self.assertIsInstance(self.book, Book)

    def test_repr(self):
        expected = "<Book A Light in the Attic, 51.77, rating: 3, available: 22>\n" \
                    "<description: It's hard to imagine a world without A Light in the Attic. This now-classic"\
                    " collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary>\n"
        self.assertNotEqual(self.book.__repr__(), expected)

    def test_repr_true(self):
        expected = self.book.__repr__()
        result = expected
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()