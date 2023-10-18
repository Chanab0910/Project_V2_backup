import tkinter as tk
from tkinter import ttk


class TestGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1239x697")

        self.bg_image = tk.PhotoImage(file="../img/bg.png")
        self.start_image = tk.PhotoImage(file=r"../img/start.png")
        self.quit_image = tk.PhotoImage(file=r"../img/quit.png")
        self.title_image = tk.PhotoImage(file=r"../img/title.png")

        self.background = tk.Label(self, image=self.bg_image, highlightthickness=0, borderwidth=0)
        self.title = tk.Label(self, image=self.title_image, highlightthickness=0, borderwidth=0)
        self.start = tk.Button(self, image=self.start_image, highlightthickness=0, borderwidth=0)
        self.quit = tk.Button(self, image=self.quit_image, highlightthickness=0, borderwidth=0, command=quit)

        self.Next_Page_Button = tk.Button(self, text='See Results', font='FuturaStd-Medium')

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.background.place(x=0, y=0)
        self.title.place(x=374, y=534)
        self.start.place(x=956, y=594)
        self.quit.place(x=1095, y=597)


if __name__ == '__main__':
    root = TestGUI()
    root.mainloop()
