class ScraperDatabase:
    def __init__(self):
        self.urls_to_be_scraped = []
        self.pages_to_be_parsed = []
        self.roll_data = {}

    def fetch_all(self):
        """
        It returns the books_data attribute of the object that calls it
        :return: The books_data list is being returned.
        """
        return self.roll_data
