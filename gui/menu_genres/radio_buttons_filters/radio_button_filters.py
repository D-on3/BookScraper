from Tkinter import Label, StringVar,Radiobutton
from gui.gui_constants.constants_and_defines import FONT


# This class is used to create a set of radio buttons that can be used to filter
# a dataframe

class RadioButtonsFilters():
    def __init__(self, inner_frame):
        """
        The function __init__() is a constructor that creates a new instance of
        the class

        :param inner_frame: the frame that the radio buttons will be placed in
        """
        self.inner_frame = inner_frame
        self._choice = StringVar()
        self.create_widgets()

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value

    def create_widgets(self):
        """
        It creates a label and three radio buttons
        """
        Label(self.inner_frame, text="Sort By").grid(column=1,
                                                                row=4,
                                                                padx=15,
                                                                pady=15)
        Radiobutton(self.inner_frame, text='Price', variable=self._choice,
                    value="price").grid(column=1, row=5)
        Radiobutton(self.inner_frame, text='Rating', variable=self._choice,
                    value="rating").grid(column=1, row=6)
        Radiobutton(self.inner_frame, text='Available', variable=self._choice,
                    value="available").grid(column=1, row=7)
