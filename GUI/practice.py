import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomeScreen, SelectingCountries):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class WelcomeScreen(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.geometry("1239x697")

        self.bg_image = tk.PhotoImage(file="../img/bg.png")
        self.start_image = tk.PhotoImage(file=r"../img/start.png")
        self.quit_image = tk.PhotoImage(file=r"../img/quit.png")
        self.title_image = tk.PhotoImage(file=r"../img/title.png")

        self.background = tk.Label(self, image=self.bg_image, highlightthickness=0, borderwidth=0)
        self.title = tk.Label(self, image=self.title_image, highlightthickness=0, borderwidth=0)
        self.start = tk.Button(self, image=self.start_image, highlightthickness=0, borderwidth=0,
                               command=lambda: controller.show_frame("SelectingCountries"))
        self.quit = tk.Button(self, image=self.quit_image, highlightthickness=0, borderwidth=0, command=quit)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.background.place(x=0, y=0)
        self.title.place(x=374, y=534)
        self.start.place(x=956, y=594)
        self.quit.place(x=1095, y=597)


class SelectingCountries(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1239x697")
        self.bg_image = tk.PhotoImage(file="../img/bg.png")
        self.Argentina = tk.PhotoImage(file="../img/Argentina.png")

        self.background = tk.Label(self, image=self.bg_image, highlightthickness=0, borderwidth=0)
        self.button = tk.Button(self, image=self.Argentina, command=self.when_pressed())

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and grids them
        self.background.grid()
        self.button.grid(rowspan=2, columnspan=2)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
