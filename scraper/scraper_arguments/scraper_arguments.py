from json_operations.json_operations import JsonFile
from jsonpath_ng import parse


class ScraperArguments(object):
    def __init__(self, args):
        self.genres = self.__get_genres(args.genres)
        self.number_of_books = args.number
        self.title = args.title
        self.filters = args.filters
        self.keywords = args.keywords
        self.sorting = args.sorting
        self.titles = self.__get_titles_from_json(args.titles)

    def __repr__(self):
        return "Genres: {0}\n" \
               "Number of books: {1}".format(self.genres,
                                             self.number_of_books)

    @staticmethod
    def __get_genres(genres):
        """
        If the genres parameter is not None, return the genres' parameter.
        Otherwise, return the list ["Books"]

        :param genres: A list of genres to search for
        :return: The genres list is being returned if it is not empty. If it is
        empty, then the list ["Books"] is returned.
        """
        return genres if genres else ["Books"]

    @staticmethod
    def __get_titles_from_json(json_with_titles):
        if not json_with_titles:
            return None
        json_data = JsonFile().read(json_with_titles[0])
        jsonpath_expression = parse('$..title')
        context_data = jsonpath_expression.find(json_data)
        titles = [title.value for title in context_data]
        return titles
