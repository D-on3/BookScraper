from book.book import Book
from collections import OrderedDict
from operator import attrgetter
import grequests
from io import BytesIO
from PIL import Image


class BookCollection(object):
    def __init__(self, raw_data):
        self.books = self.__fill_books_collection(raw_data)
        self.sorted_books = []
        self.books_imgs_urls = self.__fill_books_url(raw_data)
        self.book_images = self.request_pages_optimised_urls(
            self.books_imgs_urls)
        self.sorted_books_dict = OrderedDict()

    @staticmethod
    def __fill_books_collection(data):
        """
        It takes a dictionary of dictionaries, and returns a list of Book objects

        :param data: a dictionary of dictionaries, where the keys are the book's
        id, and the values are the book's data
        :return: A list of Book objects.
        """
        return [
            Book(title=book_data["title"],
                 rating=book_data["rating"],
                 price=book_data["price"],
                 description=book_data["description"],
                 available=book_data["available"],
                 img_url=book_data["img_url"],
                 id_book=book_data["id"])
            for book_key, book_data in data.items()]

    @staticmethod
    def __fill_books_url(data):
        """
        It takes a dictionary of dictionaries, and returns a list of Book objects

        :param data: a dictionary of dictionaries, where the keys are the book's
        id, and the values are the book's data
        :return: A list of Book objects.
        """
        return [
            book_data["img_url"]
            for book_key, book_data in data.items()]

    def dump_data_to_json(self):
        """
        It takes a list of dictionaries, sorts them by the value of the key
        'price', and returns a new dictionary with the same keys as the original,
        but with the values sorted by price
        :return: The sorted_books_dict is being returned.
        """
        return self.sorted_books_dict

    def __convert_data_dict(self):
        """
        It takes the sorted_books list, which is a list of Book objects, and
        converts it into a dictionary of dictionaries
        :return: An ordered dictionary of the sorted books.
        """
        sorted_books_dict = OrderedDict()
        sorted_books_dict["books"] = []
        for book in self.sorted_books:
            sorted_books_dict["books"].append({"title": book.title,
                                              "rating": book.rating,
                                              "price": book.price,
                                              "availability": book.available,
                                              "description": book.description,
                                              "image_url": book.img_url,
                                              "id_upc": book.id_book})
        return OrderedDict(sorted_books_dict)

    @staticmethod
    def sort_books(data_to_be_sorted, sorting_value, sorting_direction):
        """
        "Sort the data by the given value in the given direction."

        :param data_to_be_sorted: The data that you want to sort
        :param sorting_value: the name of the attribute to sort by
        :param sorting_direction: "ascending" or "descending"
        :return: The sorted data.
        """
        is_direction_descending = (sorting_direction == "descending")
        data_to_be_sorted.sort(key=attrgetter(sorting_value),
                               reverse=is_direction_descending)

        return data_to_be_sorted

    def books_collection_mainloop(self, sorting_args):
        """
        It takes a list of books, sorts them, prints them, and returns a
        dictionary of the sorted books

        :param sorting_args: a tuple of two values, the first being the sorting
        value, the second being the sorting direction
        :return: a dictionary of the books in the collection.
        """
        if sorting_args:
            sorting_value, sorting_direction = sorting_args
            self.sorted_books = self.sort_books(self.books, sorting_value, sorting_direction)
        else:
            self.sorted_books = self.books
        self.__print_books()

        return self.__convert_data_dict()

    @staticmethod
    def request_pages_optimised_urls(list_of_complete_urls):
        """
        It takes a list of urls, makes a request to each of them, and returns
        a list of the html responses

        :param list_of_complete_urls: This is a list of urls that you want to
        scrape
        :return: A list of pages to be parsed.
        """
        request = [grequests.get(url) for url in list_of_complete_urls]
        urls_to_be_scraped = grequests.map(request)

        return [Image.open(BytesIO(current_image.content)) for
                current_image in urls_to_be_scraped]

    def dump_list_of_images(self):
        return self.book_images

    def __print_books(self):
        """
        For each book in the books list, print the book.
        """
        for book in self.books:
            print "{0},".format(book)
