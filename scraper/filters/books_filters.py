class BookFilters(object):

    def __init__(self, filters=None, keywords=None, title=None, titles=None):
        self._filters = self.unpack_filters(filters)
        self.words = self.__get_list_of_words_from_str(keywords)
        self.title = title
        self.titles = titles

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def filters(self, value):
        self._filters = self.unpack_filters(value)

    @staticmethod
    def __check_filter(data):
        """
        It takes a string like "age > 30" and returns a tuple of ("age", ">",
        "30")
        :param data: The data to be filtered
        :return: A tuple of three values.
        """
        operator = ""
        if "<" in data:
            operator = "<"
        elif ">" in data:
            operator = ">"
        elif "=" in data:
            operator = "="

        criteria, value = data.split(operator)

        return criteria.strip(), operator, value.strip()

    def unpack_filters(self, data):
        """
        It takes a string of comma separated values, splits them into a list, and
        then checks each value to see if it's a valid filter
        :param data: The data to be filtered
        :return: A list of elements that have been checked to see if they are
        valid filters.
        """
        elements = []
        if data:
            for el in data.split(","):
                elements.append(self.__check_filter(el))
            return elements
        return None

    @staticmethod
    def __check_is_match(book, filter_by):
        """
        This method check is the given book match to the given filter.
        :param book: a dictionary containing the book's information
        :param filter_by: tuple
        :return: bool
        """
        criteria = filter_by[0]
        operator = filter_by[1]
        value = float(filter_by[2])
        if operator == "<":
            return book[criteria] < value
        elif operator == "=":
            return book[criteria] == value
        elif operator == ">":
            return book[criteria] > value
        return

    def __check_book(self, book):
        """
        It checks if a book matches the filters
        :param book: a dictionary containing the book's information
        :return: bool
        """

        for filter_by in self.filters:
            if not self.__check_is_match(book, filter_by):
                return False
        return True

    def __check_title(self, title):
        """
        This method check is the given title is equal to the title that we are searching for
        :param title: string
        :return: bool
        """
        return True if self.title.lower() == title.lower() else False

    def __check_titles(self, title):
        """
        This method check is the given title is equal to the title that we are searching for
        :param title: string
        :return: bool
        """
        for title_wanted in self.titles:
            if title.lower() == title_wanted.lower():
                return True
        return False

    @staticmethod
    def __get_list_of_words_from_str(keywords):
        if not keywords:
            return None
        words = keywords.split(",")
        stripped_words = [word.strip() for word in words]
        return stripped_words

    def __check_description(self, description):
        """
        This method search is they are word/words in the given string.
        :param description: string
        :return: bool
        """
        res = description.lower().split()
        for word in self.words:
            if word.lower() not in res:
                return False
        return True

    def filtering(self, book):
        """
        This method check is the given book match to the given filters(if there are any)
        :param book: dictionary
        :return: bool
        """
        res_keywords, res_title, res_filters, res_titles = True, True, True, True
        if self.words:
            res_keywords = self.__check_description(book["description"])
        if self.title:
            res_title = self.__check_title(book["title"])
        if self.titles:
            res_titles = self.__check_titles(book["title"])
        if self.filters:
            res_filters = self.__check_book(book)
        return res_keywords and res_title and res_filters and res_titles
