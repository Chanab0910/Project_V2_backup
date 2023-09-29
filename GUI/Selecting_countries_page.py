import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1239x697")
        self.bg_image = tk.PhotoImage(file=r"C:/Users/chanab0910/OneDrive - Highgate School/Project_V2/img/bg.png")

        self.background = tk.Label(self, image=self.bg_image, highlightthickness=0, borderwidth=0)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.background.place(x=0, y=0)



if __name__ == '__main__':
    root = GUI()
    root.mainloop()
        
