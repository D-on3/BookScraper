from scraper_arguments.scraper_arguments import ScraperArguments
from filters.books_filters import BookFilters
from scraper_database.scraper_database import ScraperDatabase
from scraper_parsing.multi_page_parsing.scraper_collective_books_page import \
    ScraperCollectiveBooksPage


class ScraperUI(object, ScraperCollectiveBooksPage):
    URL = "http://books.toscrape.com"

    def __init__(self, args):
        super(ScraperUI, self).__init__()
        self.arguments = ScraperArguments(args)
        self.scraper_db = ScraperDatabase()
        self.book_filter = BookFilters(self.arguments.filters, self.arguments.keywords,
                                       self.arguments.title, self.arguments.titles)

    def dump_data(self):
        """
        It returns the data that was scraped from the website
        :return: The books_data dictionary is being returned.
        """
        
        return self.scraper_db.fetch_all()

    def start_scraping(self):
        """
        It takes the number of books to be scraped from the command line, gets
        the soup of the base page, gets the categories of books, and then for
        each genre in the command line arguments, it adds the number of
        book links to be scraped to the database
        """

        data = self.get_soup_of_page(self.URL)
        categories = self.get_books_categories(data, self.URL)

        for genre in self.arguments.genres:
            if genre in categories.keys():
                page_to_scrape = categories[genre]
                while page_to_scrape and not len(self.scraper_db.roll_data) >= self.arguments.number_of_books:
                    page_to_scrape = self.get_books_url_and_next_page_url(page_to_scrape)

                    self.__gather_data()

    def __concat_url(self):
        """
        It takes a list of urls, and adds the base url to each of them
        :return: A list of complete urls
        """

        return ["/".join([self.URL, "catalogue", url]).replace("/..", "") for
                url in self.urls_of_books]

    def __unpack_data(self, list_of_complete_urls):
        """
        It takes a list of URLs, requests the HTML from each URL, parses the HTML,
        cleans the data, and returns a dictionary of the cleaned data

        :param list_of_complete_urls: a list of complete urls to scrape
        :return: A dictionary of dictionaries.
        """

        self.scraper_db.pages_to_be_parsed = self.request_pages_optimised(
            list_of_complete_urls)

        dict_for_show = {}
        counter = len(self.scraper_db.roll_data)
        for current_html in self.scraper_db.pages_to_be_parsed:
            if counter >= self.arguments.number_of_books:
                break
            soup = self.scrape_init(current_html)
            cleaned_book = self.clean_collected_data_one_url(
                soup)

            if self.book_filter.filtering(cleaned_book):
                book_id = cleaned_book["id"]
                dict_for_show[book_id] = cleaned_book
                counter += 1

        return dict_for_show

    def __gather_data(self):
        """
        This function scrapes the webpages, unpacks the data, and prints the
        result
        """
        
        list_of_complete_urls = self.__concat_url()
        self.scraper_db.roll_data.update(
            self.__unpack_data(list_of_complete_urls))
