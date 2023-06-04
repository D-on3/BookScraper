from Tkinter import Frame, Label

from gui.drop_down_menu.drop_down_menu import DropDownButton

from gui.menu_genres.combo_box_genres.comb_box_genres import ComboBoxGenres
from gui.menu_genres.radio_buttons_filters.radio_button_filters import \
    RadioButtonsFilters
from gui.gui_constants.constants_and_defines import GENRES


class MenuGenres:
    def __init__(self, root):
        self.root_frame = Frame(root, height=300, width=400)
        self.root_frame.grid(columnspan=2, column=9, row=0, sticky="nwe")

        self.combo_box_genres = None
        self.radio_buttons_filters = None
        self.sorting_direction = None
        self.create_widgets(self.root_frame)
        self.root_frame.grid_configure(column=1, row=0)

    def create_widgets(self, inner_frame):
        """
        I want to create a dropdown menu that will display the options of the
        radiobutton that is selected.

        :param inner_frame: the frame that the dropdown button will be placed in
        """
        inner_frame.grid_propagate(False)
        Label(inner_frame, text="Genres").grid(row=0, column=0, padx=15, pady=15)

        self.combo_box_genres = ComboBoxGenres(inner_frame)
        self.radio_buttons_filters = RadioButtonsFilters(inner_frame)

        sorting_directions = ["do not sort", "ascending", "descending"]
        self.sorting_direction = DropDownButton(inner_frame,
                                                sorting_directions)

    def get_input_data(self):
        """
        It takes the values from the GUI and returns them in a dictionary

        """
        input_data = {}
        sorting_value = self.radio_buttons_filters.choice.get()
        sorting_direction_selected = self.sorting_direction.selected_option
        if sorting_direction_selected == "do not sort" or sorting_value == "":
            input_data["sorting"] = None
        else:
            input_data["sorting"] = [sorting_value,
                                     sorting_direction_selected]

        genre_selected = self.combo_box_genres.genres_chosen_value.get()
        if genre_selected in ["", GENRES[0]]:
            input_data["genres"] = None
        else:
            input_data["genres"] = [genre_selected]

        return input_data
