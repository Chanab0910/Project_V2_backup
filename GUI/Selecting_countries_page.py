import tkinter as tk
from tkinter import ttk

import project_code


class GUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1239x697")
        self.bg_image = tk.PhotoImage(file="../img/bg.png")
        self.Argentina = tk.PhotoImage(file="../img/Argentina.png")

        self.background = tk.Label(self, image=self.bg_image, highlightthickness=0, borderwidth=0)
        self.button = tk.Button(self,image=self.Argentina,command=self.when_pressed())

        self.place_widgets()

    def place_widgets(self):
        # This project_code creates the widgets and grids them
        self.background.grid()
        self.button.place(x=270,y=23)

    def when_pressed(self):
        print('hello')



if __name__ == '__main__':
    root = GUI()
    root.mainloop()
        
