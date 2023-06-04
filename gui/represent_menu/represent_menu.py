import textwrap
from Tkinter import RIGHT, Y, LEFT, Frame, Canvas, GROOVE, VERTICAL
from ttk import Scrollbar

from represent_menu_functionality.represent_menu_functionality import \
    RepresentMenuFunctionality


class RepresentMenu(RepresentMenuFunctionality):
    def __init__(self, root, json_data=None):
        # crate a frame
        super(RepresentMenu, self).__init__()

        self.dict_for_show = json_data
        self.current_row = 0
        self.images_list_url = []
        self.images_list = []

        self.root_frame = Frame(root, relief=GROOVE, borderwidth=1)
        self.root_frame.grid_propagate(False)
        self.root_frame.grid_configure(column=0, columnspan=3, row=9)
        self.canvas_for_show = Canvas(self.root_frame, height=300, width=980)

        self.my_scrollbar = Scrollbar(self.root_frame, orient=VERTICAL,
                                      command=self.canvas_for_show.yview)
        self.inner_frame_scroll = Frame(self.canvas_for_show,height=300, width=1300)
        self.canvas_for_show.create_window((0, 0),
                                           window=self.inner_frame_scroll)


        self.__create_widgets()

    def __create_widgets(self):
        """
        The function creates a canvas, then creates a scrollbar, then creates
        a frame, then creates a window in the canvas, then creates a bunch of
        labels in the frame
        """

        self.canvas_for_show.pack(side=LEFT, expand=1)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas_for_show.configure(yscrollcommand=self.my_scrollbar.set)
        self.canvas_for_show.bind("<Configure>",
                                  lambda e: self.canvas_for_show.configure(
                                      scrollregion=self.canvas_for_show.bbox(
                                          "all")))

        if self.dict_for_show:
            self.__unpack_serialized_data(self.dict_for_show,
                                          self._get_len_json_books(
                                              self.dict_for_show))

    def _image_data(self, json_data):
        """
        It takes a json object, extracts the image urls from it, and then requests
        the optimised urls for each image

        :param json_data: This is the json data that we got from the previous
        function
        """

        self.images_list_url = self._get_images(json_data)
        self.images_list = self._request_images_optimised_urls(
            self.images_list_url)

    def __unpack_serialized_data(self, json_data, limit):
        """
        The function takes in a json object, and a limit, and then creates a label
        for each of the items in the json object, up to the limit

        :param json_data: The JSON data that was returned from the API call
        :param limit: The number of items to display
        """

        self._image_data(json_data)

        for idx in range(0, limit):
            self._create_image_label(self.images_list[idx],
                                     self.inner_frame_scroll)
            self._create_label("Title", self._get_title(idx, json_data),
                               self.inner_frame_scroll)
            self._create_label("Id|UPC", self._get_upc(idx, json_data),
                               self.inner_frame_scroll)
            self._create_label("Price", self._get_price(idx, json_data),
                               self.inner_frame_scroll)
            self._create_label("Availability",
                               self._get_availability(idx, json_data),
                               self.inner_frame_scroll)
            description_text = textwrap.fill(
                self._get_description(idx, json_data), 100)
            self._create_label("Description", description_text,
                               self.inner_frame_scroll)
