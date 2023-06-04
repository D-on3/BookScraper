
from Tkinter import *
from tkFileDialog import askopenfilename

from button.gui_button import GuiButton
from menu_genres.menu_genres import MenuGenres
from menu_filters.menu_filters import MenuFilters
from argparse import Namespace
from json_operations.json_operations import JsonFile
from run_scraper.run_scraping import RunScraping
from gui.represent_menu.represent_menu import RepresentMenu


class GUI():

    def __init__(self, data_for_represent=None):
        self.root = Tk()
        self.root.geometry("1000x700")
        self.root.title("Web-Scraper")
        self.root.resizable(False, False)

        self.menu_filters = None
        self.menu_genres = None
        self.button_start = None
        self.button_open_json = None
        self.data = None
        self.data_for_represent = data_for_represent
        self.represent_menu = None

        self._create_widgets(self.root)

        self.input_arguments = Namespace()

    def _create_widgets(self, frame):
        """
        It creates:
        a menu_filters, a menu_genres,
        two buttons: "Open Json" and "Scrape"
        and a represent_menu
        """
        self.menu_filters = MenuFilters(frame)
        self.menu_genres = MenuGenres(frame)
        self.button_open_json = GuiButton(frame, text="Open Json",
                                          command=self._open_file, column=1)
        self.button_start = GuiButton(frame, text="SCRAPE",
                                      command=self._run_scraping, column=2)
        self.represent_menu = RepresentMenu(frame)

    def _open_file(self):
        """
        The function open_file() opens a file and reads it
        """
        file_types = [('Json files', '*.json'), ('All files', '*')]
        dialog = askopenfilename(parent=self.root, filetypes=file_types)
        current_file = JsonFile().read(dialog)
        if self.represent_menu:
            self.represent_menu = RepresentMenu(self.root, current_file)

    def _run_scraping(self):
        """
        The function is called when the user clicks on the button
        """

        self.gather_input_arguments()
        self.data = RunScraping().run(self.input_arguments)
        self.represent_menu = RepresentMenu(self.root, self.data)

    def gather_input_arguments(self):
        """
        It takes the input from the filters and genres menus and combines them
        into a single dictionary
        """
        input_from_filters = self.menu_filters.get_input_data()
        input_from_genres = self.menu_genres.get_input_data()
        input_arguments = {}
        input_arguments.update(input_from_filters)
        input_arguments.update(input_from_genres)
        input_arguments["titles"] = None
        self.input_arguments = Namespace(**input_arguments)

    def run_gui(self):
        """
        The function run_gui() is called when the user clicks the "Run" button
        """
        self.root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run_gui()
