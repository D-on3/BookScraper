from run_scraping import RunScraping
from arg_parser.arg_parser import ArgParser
from gui.gui_tkinter import GUI


class RunWebScraper(RunScraping):
    def start(self):
        """
        It creates a ScraperUI object. and then calls the start_scraping()
        Depending on the passed arguments, there are two options:
        1. Opens GUI
        2. Runs scraping for passed args
        """
        print "                      WELCOME TO WEB SCRAPER!"

        parser = ArgParser()
        args = parser.parsed_args

        if args.gui:
            print "Run GUI"
            gui = GUI()
            gui.run_gui()
        else:
            self.run(args)
