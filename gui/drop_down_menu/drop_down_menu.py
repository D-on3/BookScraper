from Tkinter import StringVar, OptionMenu


# > A button that can be clicked to show a drop down menu


class DropDownButton:
    def __init__(self, root, values, width=1, column=4, row=7):
        self.values = values
        self._variable = StringVar(root)
        self._variable.set(values[0])  # default value
        self._create_widget(root, self._variable, column, row)
        self.selected_option = values[0]

    def save_selected_option(self, selection):
        if selection == self.values[0]:
            self.selected_option = None
        else:
            self.selected_option = selection

    def _create_widget(self, root, variable, column, row):
        """
        It creates a dropdown menu with two options, "descending" and "ascending",
        and places it in the grid at column 4, row 7.

        :param root: the root window
        :param variable: The variable that will be used to store the value of the
        option menu
        """

        type_of_sorting = OptionMenu(root, variable, *self.values, command=self.save_selected_option)
        type_of_sorting.grid(column=column, row=row)
