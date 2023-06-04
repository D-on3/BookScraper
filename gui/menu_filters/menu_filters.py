from Tkinter import *
from gui.gui_constants.constants_and_defines import FONT, MAX_NUMBER_OF_BOOKS


class LabelWithText(object):
    def __init__(self, frame, label_text, row):
        self.label = Label(frame, text=label_text)
        self.text = Text(frame)
        self.__customize(row)

    def __customize(self, row):
        """
        It customizes the label and text of the row

        :param row: the row number of the widget
        """

        self.__customize_label(row)
        self._customize_text(row)

    def __customize_label(self, row):
        """
        The function configures the label widget to have a width of 20, a height
        of 2, and an anchor of "e" (east)

        :param row: The row number where the label will be placed
        """
        self.label.configure(width=20, height=2, anchor="e")
        self.label.grid(columnspan=2, column=0, row=row, padx=10, pady=3)

    def _customize_text(self, row):
        """
        The function _customize_text() is a method of the class _customize_text()
        and it takes two arguments, self and row.

        :param row: the row number of the widget
        """
        self.text.configure(width=4, height=1)
        self.text.grid(column=2, row=row)

    def disable_text(self):
        """
        It deletes the text in the text widget, inserts a space, and then disables
        the text widget.
        """
        self.text.delete('1.0', END)
        self.text.insert(END, " ")
        self.text.configure(state=DISABLED)

    def enable_text(self):
        """
        The function enables the text widget to be editable
        """
        self.text.insert(END, " ")
        self.text.configure(state=NORMAL)


class WideLabelWithText(LabelWithText):
    def __init__(self, frame, label_text, row):
        super(WideLabelWithText, self).__init__(frame, label_text, row)
        self.__expand_for_keywords(row)

    def __expand_for_keywords(self, row):
        """
        The function takes in a row number and configures the label and text
        widgets to span 3 columns and be placed in the first column of the row
        number passed in

        :param row: the row number of the grid
        """
        self.label.configure(width=20)
        self.label.grid(columnspan=3, column=0, pady=(20, 0))
        self.text.configure(width=30)
        self.text.grid(columnspan=3, column=0, row=row + 1)


class Filter(LabelWithText):
    def __init__(self, frame, label_text, row):
        super(Filter, self).__init__(frame, label_text, row)
        self.name = label_text
        self.filtering_option = None
        self.filter_selected_option = " "
        self.set_filter(frame, row)
        self.disable_text()

    def set_filter(self, frame, row):
        """
        It makes the label's columnspan=1, so that there is a free column for
        filtering_option. Then it adds filtering_option at column 1 (between
        self.label and self.text)

        :param frame: the frame where the widget is located
        :param row: the row number of the widget
        """

        self.label.grid(columnspan=1)

        n = StringVar()
        n.set(" ")
        self.filtering_option = OptionMenu(frame, n, " ", ">", "=", "<",
                                           command=self.save_selected_option)
        self.filtering_option.configure(width=1)
        self.filtering_option.grid(column=1, row=row)

    def save_selected_option(self, selection):
        """
        If the user selects a blank space, disable the text box. Otherwise, enable
        the text box

        :param selection: The option selected from the dropdown menu
        """
        if selection == " ":
            self.disable_text()
        else:
            self.enable_text()
        self.filter_selected_option = selection

    def __str__(self):
        repr_text = ""
        if self.filter_selected_option != " ":
            repr_text = self.name.lower() + self.filter_selected_option + self.text.get(
                1.0, "end-1c")
        return repr_text


class Filters:
    def __init__(self, frame):
        Label(frame, text="Filters:", font=FONT).grid(columnspan=2, row=1,
                                                      column=1, pady=(20, 0))
        self.filter_price = Filter(frame, "Price", 2)
        self.filter_rating = Filter(frame, "Rating", 3)
        self.filter_available = Filter(frame, "Available", 4)

    def get_active_filters(self):
        """
        It returns a list of strings that are the active filters
        :return: A list of strings.
        """
        filters = [self.filter_price, self.filter_rating,
                   self.filter_available]
        return [str(filter_option) for filter_option in filters if
                str(filter_option) != ""]


class MenuFilters:
    def __init__(self, root):
        self.number_of_books = None
        self.filters = None
        self.keywords = None
        self.title = None
        self.frame = Frame(root)
        self.__customize()
        self.__add_widgets()
        self.input_arguments = self.get_input_data()

    def __customize(self):
        """
        The function is called in init of current class
        """
        self.frame.configure(width=400, height=400, padx=0)
        self.frame.grid(column=0, columnspan=1, rowspan=2, row=0,
                        sticky="ewn")
        self.frame.grid_propagate(False)

    def __add_widgets(self):
        """
        It creates a label, a filter, and a keyword object, and adds them to the
        frame
        """
        self.number_of_books = LabelWithText(self.frame, "Number of books", 0)
        self.filters = Filters(self.frame)
        self.keywords = WideLabelWithText(self.frame,
                                          "Keywords in description:", 6)
        self.title = WideLabelWithText(self.frame, "Title of a book:", 8)

    def get_input_data(self):
        """
        It takes the user input from the GUI and returns it in a dictionary
        :return: A dictionary with the following keys:
            - number: the number of books to be returned
            - keywords: a list of keywords to be used in the search
            - filters: a string with the filters to be used in the search
        """
        input_data = dict()

        number_of_books = self.number_of_books.text.get(1.0, "end-1c")
        if number_of_books.isdigit():
            input_data["number"] = int(number_of_books)
        else:
            input_data["number"] = MAX_NUMBER_OF_BOOKS

        keywords = self.keywords.text.get(1.0, "end-1c")
        if not len(keywords):
            input_data["keywords"] = None
        else:
            input_data["keywords"] = str(keywords)

        title = self.title.text.get(1.0, "end-1c")
        input_data["title"] = title
        filters = self.filters.get_active_filters()
        input_data["filters"] = ", ".join(filters) if len(
            filters) > 0 else None

        return input_data
