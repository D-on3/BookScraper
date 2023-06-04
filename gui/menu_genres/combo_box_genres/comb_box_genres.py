from Tkinter import StringVar
from ttk import Combobox

from gui.gui_constants.constants_and_defines import GENRES


class ComboBoxGenres():
    def __init__(self, inner_frame):
        # Combobox creation
        self.inner_frame = inner_frame
        self._genre_chosen_value = StringVar()

        self._creater_widgets()

    @property
    def genres_chosen_value(self):
        return self._genre_chosen_value

    @genres_chosen_value.setter
    def genres_chosen_value(self, value):
        self._genre_chosen_value = value

    def _creater_widgets(self):
        """
        It creates a Combobox widget and places it in the inner_frame.
        """
        self.genre_chosen = Combobox(self.inner_frame, width=18,
                                     textvariable=self._genre_chosen_value)
        self.genre_chosen['values'] = GENRES
        self.genre_chosen.grid(column=1, row=0, padx=15, pady=15)
        self.genre_chosen.current()
