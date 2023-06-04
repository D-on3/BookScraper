from jsonpath_ng import parse
from Tkinter import Label, NW
from io import BytesIO
from PIL import ImageTk, Image
import grequests


class RepresentMenuFunctionality(object):

    def __init__(self):
        self.current_row = 0

    @staticmethod
    def _get_title(idx, json_data):
        """
        The function takes in a json object and an index, and returns the title of
        the book at that index
        :param idx: the index of the book in the json_data
        :param json_data: The JSON data that we want to parse
        :return: A list of books
        """
        books_title = parse("$.books[{0}].title".format(idx)).find(json_data)
        if books_title[0]:
            return books_title[0].value

    @staticmethod
    def __get_rating(idx, json_data):
        """
        The function takes in a json object and an index, and returns the rating of the book
        at that index
        :param idx: the index of the book in the json file
        :param json_data: The json data that we want to parse
        :return: A list of books
        """
        books_title = parse("$.books[{0}].rating".format(idx)).find(json_data)

        if books_title[0]:
            return books_title[0].value

    @staticmethod
    def _get_availability(idx, json_data):
        """
        The function takes the index of the book and the json data as input and returns the
        availability of the book
        :param idx: The index of the book in the json data
        :param json_data: The json data that we got from the API
        :return: The availability of the book
        """

        book_available = parse("$.books[{0}].availability".format(idx)).find(
            json_data)

        if book_available[0]:
            return book_available[0].value

    @staticmethod
    def _get_description(idx, json_data):
        """
        The function takes in a json object and an index, and returns the
        description of the book at that index
        :param idx: the index of the book in the json_data
        :param json_data: The json data that we're going to parse
        :return: A list of all the book descriptions
        """
        book_description = parse("$.books[{0}].description".format(idx)).find(
            json_data)
        if book_description[0]:
            return book_description[0].value

    @staticmethod
    def _get_price(idx, json_data):
        """
        The function takes in a JSON string, and returns the price of the book
        at the index specified
        :param idx: the index of the book in the json data
        :param json_data: The JSON data that we want to parse
        :return: The price of the book
        """
        book_price = parse("$.books[{0}].price".format(idx)).find(json_data)
        if book_price[0]:
            return book_price[0].value

    def _create_label(self, current_text, data, frame):
        """
        The function creates a label in the second frame of the GUI, and places it in the
        current row and column
        :param current_text: The text that will be displayed on the left side of
        the label
        :param data: The data to be displayed in the label
        """

        Label(frame, text=current_text).grid(
            row=self.current_row, column=1, sticky=NW)

        Label(frame,
              text=data).grid(
            row=self.current_row, column=2, sticky=NW)
        self.current_row += 1

    @staticmethod
    def _request_images_optimised_urls(list_of_complete_urls):
        """
        The function takes a list of urls, makes a request to each of them, and returns
        a list of the html responses

        :param list_of_complete_urls: This is a list of urls that you want to
        scrape
        :return: A list of pages to be parsed.
        """

        request = [grequests.get(url) for url in list_of_complete_urls]
        urls_to_be_scraped = grequests.map(request)

        return [Image.open(BytesIO(current_image.content)) for
                current_image in urls_to_be_scraped]

    @staticmethod
    def _get_images(json_data):
        """
        It takes in a json object and an index, and returns the rating of the book
        at that index

        :param idx: the index of the book in the json file
        :param json_data: The json data that we want to parse
        :return: A list of books
        """
        books_image = parse("$.books[*].image_url").find(json_data)

        return [book_url.value for book_url in books_image]

    @staticmethod
    def _get_len_json_books(json_data):
        """
        The function returns the length of the first book in the json_data
        :param json_data: The json data that you want to parse
        :return: The length of the book array in the json_data dictionary.
        """
        if "books" in json_data:
            return len(json_data['books'])
        else:
            print "Invalid file"
            return False

    @staticmethod
    def _get_upc(idx, json_data):
        """
        The function takes in a JSON string, and returns the price of the book
        at the index specified
        :param idx: the index of the book in the json data
        :param json_data: The JSON data that we want to parse
        :return: The price of the book
        """
        book_price = parse("$.books[{0}].id_upc".format(idx)).find(json_data)
        if book_price[0]:
            return book_price[0].value

    def _create_image_label(self, raw_data, frame):
        """
        It takes a raw image, resizes it, and then displays it in a label.

        :param raw_data: The image data
        :param frame: the frame that the image will be placed in
        """

        im = raw_data.resize((150, 200))
        photo = ImageTk.PhotoImage(im)

        label = Label(frame, image=photo)
        label.image = photo
        label.grid(row=self.current_row, column=0, sticky=NW)
