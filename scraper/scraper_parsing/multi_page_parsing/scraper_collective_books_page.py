import re
import grequests

from scraper.scraper_parsing.single_page_parsing.scraper_single_book_page import \
    ScraperSingleBookPageMixin


class ScraperCollectiveBooksPage(ScraperSingleBookPageMixin):

    def __init__(self):
        self.urls_of_books = []

    @staticmethod
    def __get_next_page_url(current_page_url, current_page_soup):
        """
        It takes the current page's URL and the current page's soup, and
        returns the URL of the next page

        :param current_page_url: The URL of the current page
        :param current_page_soup: The BeautifulSoup object of the current page
        :return: The next page url
        """

        li_next = current_page_soup.find("li", {"class": "next"})

        if not li_next:
            return None

        next_page_url_short_href = li_next.find("a")["href"]
        current_page_base = "http://books.toscrape.com/"
        if current_page_url != "http://books.toscrape.com":
            current_page_base = re.match("^(.*[\\\/])",
                                         current_page_url).group(0)
        next_page_url = current_page_base + next_page_url_short_href

        return next_page_url

    # In use
    @staticmethod
    def __get_books_link(parsed_data, base_url):
        """
        It takes the parsed data and the base url and returns the title and
        url only of the "Books" genre. The purpose of this method is to
        get only "Books" section and his link

        :param parsed_data: This is the parsed data from the BeautifulSoup
        library
        :param base_url: The base url of the website
        :return: The title and url of the "Books" section of the website.
        """

        data = parsed_data.find('ul', attrs={'class': 'nav nav-list'})
        res = str(data).split()
        link = res[5].split('"')
        title = res[6]
        url = base_url + '/' + str(link[1]).replace("index.html", "")
        return title, url

    def get_books_categories(self, parsed_data, base_url):
        """
        It takes a parsed html page and a base url and returns a dictionary of
        genres and their corresponding urls

        :param parsed_data: The parsed data from the html page
        :param base_url: The base url of the website
        :return: A dictionary of genres and their corresponding urls.
        """

        genres = {}
        ul_nav_list = parsed_data.find("ul", {"class": "nav nav-list"})
        categories = ul_nav_list.find_all("li")

        for category in categories:
            urls = str(category).split('"')[1]
            name = re.findall(r"(?:[A-Za-z]+\s)?[A-Za-z]+", category.text)
            genres[str.join(" ", name).encode('ascii',
                                              errors='ignore')] = base_url + '/' + str(
                urls).replace(
                "index.html", "")
        # Add "Books" and his link in genres
        res = self.__get_books_link(parsed_data, base_url)
        genres[res[0]] = res[1]
        return genres

    @staticmethod
    def request_pages_optimised(list_of_complete_urls):
        """
        It takes a list of urls, makes a request to each of them, and returns
        a list of the html responses

        :param list_of_complete_urls: This is a list of urls that you want to
        scrape
        :return: A list of pages to be parsed.
        """

        request = [grequests.get(url) for url in list_of_complete_urls]
        urls_to_be_scraped = grequests.map(request)
        pages_to_be_parsed = list(map(lambda
                                      html_response: html_response.text if html_response else None,
                                      urls_to_be_scraped))
        return pages_to_be_parsed

    def get_books_url_and_next_page_url(self,
                                        url_of_collection_page):
        """
        It takes an url of a collection page, gets the soup of that page, finds
        all the h3 tags, finds the tags inside those h3 tags, and then
        appends the
        href attribute of those a tags to a list of urls of books

        :param url_of_collection_page: the url of the page that contains the
        collection of books
        :return: The next page url.
        """

        self.urls_of_books = []

        current_page_soup = self.get_soup_of_page(url_of_collection_page)
        h3_tags = current_page_soup.find_all("h3")
        tags_that_are_links_to_books = [h3.find("a") for h3 in
                                        h3_tags]

        for tag in tags_that_are_links_to_books:
            self.urls_of_books.append(tag["href"])

        return self.__get_next_page_url(url_of_collection_page,
                                        current_page_soup)
