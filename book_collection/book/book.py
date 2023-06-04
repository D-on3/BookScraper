class Book(object):
    def __init__(self,
                 title,
                 rating,
                 price,
                 description,
                 available,
                 id_book,
                 img_url
                 ):
        self._title = title
        self._rating = rating
        self._price = price
        self._description = description
        self._available = available
        self._id_book = id_book
        self._img_url = img_url

    def __repr__(self):
        """
        The __repr__ function returns a string that represents the object
        :return: The return statement is returning a string that is formatted
        with the title, price, rating, available,
        and description of the book.
        """

        return "{{\n"\
                "\ttitle: {0},\n"\
                "\tprice: {1},\n"\
                "\trating: {2},\n"\
                "\tavailable: {3},\n"\
                "\tdescription: {4}\n"\
                "}}".format(self.title, self.price, self.rating, self.available, self.description)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    @property
    def id_book(self):
        return self._id_book

    @id_book.setter
    def id_book(self, value):
        self._id_book = value

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
