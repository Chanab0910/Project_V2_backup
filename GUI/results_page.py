import tkinter as tk
from tkinter import ttk
from GUI.Selecting_countries_page import GUI

class TestGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.title_country = ...
        self.percentage_they_won_wc = ...



        self.place_widgets()

    def place_widgets(self):





if __name__ == '__main__':
    root = TestGUI()
    root.mainloop()
