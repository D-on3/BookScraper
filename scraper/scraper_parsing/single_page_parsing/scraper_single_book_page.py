import re
import unidecode
import requests
from bs4 import BeautifulSoup


class ScraperSingleBookPageMixin:

    @staticmethod
    def __request_custom(url):
        """
        It takes an url as an argument, and returns the html of the page at
        that url

        :param url: The URL to request
        :return: The requested html is being returned.
        """

        requested_html = ""
        try:
            req = requests.get(url, verify=True)
            req.raise_for_status()
            requested_html = req.text

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
        return requested_html

    def get_soup_of_page(self, page_url):
        """
        It takes an url, makes a request, and returns a BeautifulSoup object

        :param page_url: The url of the page you want to scrape
        :return: A soup object
        """

        request = self.__request_custom(page_url)
        current_page_soup = BeautifulSoup(request, "lxml")

        return current_page_soup

    @staticmethod
    def __get_description(book_data):
        """
        It takes a book's data, finds the description, and returns it

        :param book_data: the book's page
        :return: The description of the book.
        """

        for_convert = book_data.find(
            "div",
            {"id": "product_description"})

        if for_convert:
            for_return = for_convert.findNextSibling("p").text
            return for_return.encode('ascii', errors='ignore')
        return ""

    @staticmethod
    def __get_title(book_data):
        """
        It takes a BeautifulSoup object, finds the h1 tag, gets the text, and
        returns the text

        :param book_data: the book's data, which is a BeautifulSoup object
        :return: The title of the book.
        """

        book_title = book_data.find("h1").text
        return book_title.encode('ascii',
                                 errors='ignore') if book_title else None

    @staticmethod
    def __get_price(book_data):
        """
        It takes a BeautifulSoup object as an argument, finds the price tag,
        converts it to ASCII, and then uses a regular expression to extract
        the price

        :param book_data: the book data that we're going to be scraping
        :return: The price of the book.
        """

        book_price = book_data.find("p", attrs={"class": "price_color"}).text
        for_covert = unidecode.unidecode(
            book_price)

        match = re.search(r"[\d]+\W[\d]+", for_covert)

        return float(match.group()) if match else None

    @staticmethod
    def __get_availability(book_data):
        """
        We're looking for the first `<p>` tag in the `<div>` tag with the
        class` product_main` and then we're looking for the next tag after
        that

        :param book_data: This is the HTML data for the book
        :return: The number of books available.
        """

        html_data = book_data.find("div",
                                   attrs={"class": "col-sm-6 product_main"})

        tag_found = html_data.find("p").findNext().text
        available = re.search(r"[\d]+", tag_found.strip())

        return int(available.group()) if available else None

    @staticmethod
    def __convert_rating(rating_value):
        """
        If the rating value is "One", return 1. If the rating value is "Two",
        return 2. If the rating value is "Three", return 3. If the rating
        value is "Four", return 4. If the rating value is "Five", return 5.
        Otherwise, return None.

        :param rating_value: The rating value that the user has selected
        :return: the rating value.
        """

        if rating_value == "One":
            return 1
        elif rating_value == "Two":
            return 2
        elif rating_value == "Three":
            return 3
        elif rating_value == "Four":
            return 4
        elif rating_value == "Five":
            return 5
        else:
            return None

    def __get_rating(self, book_data):
        """
        It takes a book data object, finds the rating tag, extracts the rating,
        and returns the rating

        :param book_data: The book data that we get from the BeautifulSoup object
        :return: The rating of the book.
        """

        regex_for_tag = r"p\Wclass=\W[a-z]+\W[A-Za-z]+\W[A-Za-z]+[^$]"
        regex_for_rating = r"[A-Z][a-z]+"

        data = book_data.find("div", attrs={
            "class": "col-sm-6 product_main"}).findParent()
        match = re.search(regex_for_tag, str(data))
        match_rating = re.search(regex_for_rating, match.group())
        return self.__convert_rating(match_rating.group())

    @staticmethod
    def scrape_init(scraped_data):
        """
        It takes in a string of HTML and returns a BeautifulSoup object

        :param scraped_data: This is the data that we scraped from the website
        :return: BeautifulSoup object
        """
        
        return BeautifulSoup(scraped_data, "lxml")

    def clean_collected_data_one_url(self, url):
        """
        It takes a URL, and returns a dictionary with the title, price,
        availability, description, and rating of the book

        :param url: The URL of the book's page on Amazon
        :return: A dictionary with the title, price, availability,
        description, and rating of the book.
        """

        cleaned_data = {

            "price": self.__get_price(url),
            "available": self.__get_availability(url),
            "description": self.__get_description(url),
            "rating":
                self.__get_rating(url),
            "title": self.__get_title(url),
            "img_url": self.__get_img(url),
            "id": self.__get_upc(url)
        }
        
        return cleaned_data
    @staticmethod
    def __get_img( book_data):
        """
        We're using the `find` method to find the `img` tag in the `book_data`
        variable. Then we're using the `["src"]` notation to get the `src`
        attribute of the `img` tag. Then we're using the `[5:]` notation to get
        the value of the `src` attribute, but we're starting at the 5th character

        :param book_data: The book data that we're going to be parsing
        :return: The image of the book
        """

        thumbnail_elements = book_data.find("img")
        return "https://books.toscrape.com{0}".format(thumbnail_elements["src"][5:])

    @staticmethod
    def __get_upc(book_data):
        """
        It finds the first table with the class "table table-striped" and then
        finds the first td tag within that table

        :param book_data: the html data from the page
        """
        current_tag = book_data.find("table",class_="table table-striped").find("td")
        return current_tag.text


