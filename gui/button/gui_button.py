from Tkinter import *
FONT = ("Times New Roman", 12)


class GuiButton:
    def __init__(self, root, text="", command=None, column=1):
        self.button = Button(root, text=text, font=FONT, command=command, width=15)
        self.button.grid(column=column, row=1, rowspan=1, columnspan=1, padx=10, pady=10)
