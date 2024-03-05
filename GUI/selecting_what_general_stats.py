import tkinter as tk
from tkinter import ttk
from tkinter import *
import Selecting_countries_page
from table import GeneralStatsGUI
from graph import GraphGUI
class SelectGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.title = tk.Label(self, text=f'General Analysis', font='helvetica 100')
        self.description1 = tk.Label(self, text=f'Pick whether you would like to see a table that ranks each country on ', font='helvetica 20', )
        self.description2 = tk.Label(self, text=f'their overall performance, or a graph to show the World Cup win ', font='helvetica 20')
        self.description3 = tk.Label(self, text=f'distributions between the countries. ',
                                    font='helvetica 20')
        self.table_button = tk.Button(self, text='Table', font='helvetica 20', command=self.table)
        self.graph_button = tk.Button(self, text='Graph', font='helvetica 20', command=self.graph)
        self.space = tk.Label(self, text=' ')
        self.back_to_home_screen = tk.Button(self, text='Back to home screen', command=self.back_to_home)
        self.quit = tk.Button(self, text='Quit', command=quit)
        self.place_widgets()

    def place_widgets(self):
        self.title.grid(row=0, columnspan=2, )
        self.description1.grid(row=1, columnspan=2, sticky='')
        self.description2.grid(row=2, columnspan=2, sticky='')
        self.description3.grid(row=3, columnspan=2, sticky='')
        self.space.grid(row=4)
        self.table_button.grid(row=5, column=0,pady=20)
        self.graph_button.grid(row=5, column=1)
        self.back_to_home_screen.grid(row=6,column=0,sticky='w')
        self.quit.grid(row=6,column=1,sticky='e')


    def table(self):
        g = GeneralStatsGUI()
        g.mainloop()

    def graph(self):
        g = GraphGUI()
        g.mainloop()

    def back_to_home(self):
        self.destroy()
        self.gui = Selecting_countries_page.GUI()
        self.gui.mainloop()

if __name__ == '__main__':
    root = SelectGUI()
    root.mainloop()