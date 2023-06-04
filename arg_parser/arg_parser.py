import argparse
import json
import os
from scraper.filters.books_filters import BookFilters

MAX_NUMBER_OF_BOOKS = 10
SORTING_VALUES = ["rating", "price", "available"]
SORTING_DIRECTIONS = ["ascending", "descending"]
COMPARE_SIGNS = ["<", ">", "="]


class ArgParser:
    flag_sorting_arg_idx = 1

    def __init__(self):
        self.__parser = self.__create_argparser()
        self.parsed_args = self.__get_arguments()

    @staticmethod
    def __create_argparser():
        # description = """Welcome to Web Scraper!
        #         You can use the following arguments:
        #         -b - number of books (Default value is 100)
        #         -g - list of genres to search through
        #         -s - list of sorting {ascending or descending}
        #         -f - list of filters
        #         -d - list of keywords to be searched in the description
        #         -t - title of a book to search for
        #         -F - list of book titles to search for (from given json)
        #         -X - open GUI """
        description = "Web Scraper"

        return argparse.ArgumentParser(description)

    def __get_arguments(self):
        """
        The function takes in a parser object and adds arguments to it
        """
        self.__parser.add_argument("-b", dest="number", type=self.__check_positive_number, default=MAX_NUMBER_OF_BOOKS,
                                   help="Number of books to be scraped")
        self.__parser.add_argument("-g", dest="genres", nargs="+",
                                   help="List of genres to search through")
        self.__parser.add_argument("-s", dest="sorting", nargs=2, type=self.__check_valid_sorting,
                                   help="list of sortings {ascending, descending}")
        self.__parser.add_argument("-f", dest="filters", type=self.__check_is_valid_filters, help="List of filters")
        self.__parser.add_argument("-d", dest="keywords",
                                   help="list of keywords for searching in the description")
        self.__parser.add_argument("-t", dest="title", type=str,
                                   help="search for a book by title")
        self.__parser.add_argument("-F", dest="titles", type=self.__check_is_valid_file_path, nargs=1,
                                   help="list of book titles to search for (from given json)")
        self.__parser.add_argument("-X", dest="gui", action="store_true",
                                   help="Start graphical user interface where you can set filter options")

        parsed_args = self.__parser.parse_args()

        return parsed_args

    @staticmethod
    def __check_positive_number(value):
        """
        It checks if the value is a positive number

        :param value: The string value that was passed to the argument
        :return: the value of the argument.
        """
        if not value.isdigit():
            raise argparse.ArgumentTypeError("should be positive integer")
        num_value = int(value)
        return num_value

    def __check_valid_sorting(self, sorting_args):
        """
        If the first argument is valid, set the flag to 2 and return the argument.
        If the second argument is valid, return the argument

        :param sorting_args: The argument that is passed to the function
        :return: The sorting_args are being returned.
        """
        if self.flag_sorting_arg_idx == 1:
            if sorting_args not in SORTING_VALUES:
                raise argparse.ArgumentTypeError("First argument should be one of these: {0}".format(SORTING_VALUES))
            else:
                self.flag_sorting_arg_idx = 2
                return sorting_args
        if sorting_args not in SORTING_DIRECTIONS:
            raise argparse.ArgumentTypeError("Second argument should be one of these: {0}".format(SORTING_DIRECTIONS))
        return sorting_args

    @staticmethod
    def __check_is_valid_filters(filters_data):
        filters_list = BookFilters().unpack_filters(filters_data)
        error = argparse.ArgumentTypeError("in filters you can compare only these values: {0}\n\
                                           use a compare sign: {1}\n\
                                           and number after it\n\
                                           HINT: rating is in range [1, 5]\n\
                                           EXAMPLE: \"rating>3, price<35\"".format(SORTING_VALUES, COMPARE_SIGNS))
        rating_error = argparse.ArgumentTypeError("rating is in range [1, 5]")
        for filter_el in filters_list:
            if filter_el[0] not in SORTING_VALUES or not filter_el[2].isdigit():
                raise error
        for filter_el in filters_list:
            if filter_el[0] == "rating" and int(filter_el[2]) not in range(1, 6):
                raise rating_error
        return filters_data

    @staticmethod
    def __check_is_valid_file_path(file_path):
        if not os.path.isfile(file_path):
            raise argparse.ArgumentTypeError("not valid file passed")
        try:
            with open(file_path) as json_file:
                json.load(json_file)
        except:
            raise argparse.ArgumentTypeError("not valid json file passed")
        return file_path
