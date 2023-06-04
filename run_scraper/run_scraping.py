from scraper.scraper import ScraperUI
from book_collection.book_collection import BookCollection
from json_operations.json_operations import JsonFile


class RunScraping:

    def __init__(self):
        self.return_data = None

    @staticmethod
    def run(args):
        """
            The function takes in the arguments from the command line and uses them to
            scrape the books from the website

            :param args: The arguments passed to the script
            """
        scraper = ScraperUI(args)

        number_of_books_str = str(args.number)
        print " \n---------------------------------------------------------------------\
                \n------- Here are the books that meet the input requirements:---------\
                \n---------------------------------------------------------------------\n" \
            .format(
            number_of_books_str)

        scraper.start_scraping()
        current_books = BookCollection(
            scraper.dump_data())
        new_json = JsonFile()
        new_json.create(current_books.books_collection_mainloop(args.sorting))

        print " \n---------------------------------------------------------------------\
                       \n------------------------ {0} books were scraped.---------------------\
                       \n---------------------------------------------------------------------\n" \
            .format(len(scraper.scraper_db.roll_data))

        return new_json.read(new_json.output_file)
