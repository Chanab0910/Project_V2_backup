import tkinter as tk
from tkinter import ttk

import project_code


class GUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1239x697")

        self.Argentina = tk.PhotoImage(file="../img/Argentina.png")
        self.Austria = tk.PhotoImage(file="../img/Austria.png")
        self.Belgium = tk.PhotoImage(file="../img/Belgium.png")
        self.Canada = tk.PhotoImage(file="../img/Canada.png")
        self.Croatia = tk.PhotoImage(file="../img/Croatia.png")
        self.Czech = tk.PhotoImage(file="../img/Czech.png")
        self.Denmark = tk.PhotoImage(file="../img/Denmark.png")
        self.England = tk.PhotoImage(file="../img/England.png")
        self.Finland = tk.PhotoImage(file="../img/Finland.png")
        self.France = tk.PhotoImage(file="../img/France.png")
        self.Germany = tk.PhotoImage(file="../img/Germany.png")
        self.Hungary = tk.PhotoImage(file="../img/Hungary.png")
        self.Iceland = tk.PhotoImage(file="../img/Iceland.png")
        self.Ireland = tk.PhotoImage(file="../img/Ireland.png")
        self.Italy = tk.PhotoImage(file="../img/Italy.png")
        self.Mexico = tk.PhotoImage(file="../img/Mexico.png")
        self.Ghana = tk.PhotoImage(file="../img/Ghana.png")
        self.Netherlands = tk.PhotoImage(file="../img/Netherlands.png")
        self.Morocco = tk.PhotoImage(file="../img/Morocco.png")
        self.Norway = tk.PhotoImage(file="../img/Norway.png")
        self.Poland = tk.PhotoImage(file="../img/Poland.png")
        self.Portugal = tk.PhotoImage(file="../img/Portugal.png")
        self.Romania = tk.PhotoImage(file="../img/Romania.png")
        self.Scotland = tk.PhotoImage(file="../img/Scotland.png")
        self.Spain = tk.PhotoImage(file="../img/Spain.png")
        self.Sweden = tk.PhotoImage(file="../img/Sweden.png")
        self.Ukraine = tk.PhotoImage(file="../img/Ukraine.png")
        self.USA = tk.PhotoImage(file="../img/USA.png")
        self.Wales = tk.PhotoImage(file="../img/Wales.png")
        self.Japan = tk.PhotoImage(file="../img/Japan.png")
        self.China = tk.PhotoImage(file="../img/Belgium.png")

        self.Argentina_button = tk.Button(self, image=self.Argentina, width=220, height=140)
        self.Austria_button = tk.Button(self, image=self.Austria, width=220, height=140)
        self.Belgium_button = tk.Button(self, image=self.Belgium, width=220, height=140)
        self.Canada_button = tk.Button(self, image=self.Canada, width=220, height=140)
        self.Croatia_button = tk.Button(self, image=self.Czech, width=220, height=140)
        self.Czech_button = tk.Button(self, image=self.Denmark, width=220, height=140)
        self.Denmark_button = tk.Button(self, image=self.England, width=220, height=140)
        self.England_button = tk.Button(self, image=self.Finland, width=220, height=140)
        self.Finland_button = tk.Button(self, image=self.France, width=220, height=140)
        self.Germany_button = tk.Button(self, image=self.Germany, width=220, height=140)
        self.Hungary_button = tk.Button(self, image=self.Hungary, width=220, height=140)
        self.Iceland_button = tk.Button(self, image=self.Iceland, width=220, height=140)
        self.Ireland_button = tk.Button(self, image=self.Ireland, width=220, height=140)
        self.Italy_button = tk.Button(self, image=self.Italy, width=220, height=140)
        self.Mexico_button = tk.Button(self, image=self.Mexico, width=220, height=140)
        self.Ghana_button = tk.Button(self, image=self.Ghana, width=220, height=140)
        self.Netherlands_button = tk.Button(self, image=self.Netherlands, width=220, height=140)
        self.Morocco_button = tk.Button(self, image=self.Morocco, width=220, height=140)
        self.Norway_button = tk.Button(self, image=self.Norway, width=220, height=140)
        self.Poland_button = tk.Button(self, image=self.Poland, width=220, height=140)
        self.Portugal_button = tk.Button(self, image=self.Portugal, width=220, height=140)
        self.Romania_button = tk.Button(self, image=self.Romania, width=220, height=140)
        self.Scotland_button = tk.Button(self, image=self.Scotland, width=220, height=140)
        self.Spain_button = tk.Button(self, image=self.Spain, width=220, height=140)
        self.Sweden_button = tk.Button(self, image=self.Sweden, width=220, height=140)
        self.Ukraine_button = tk.Button(self, image=self.Ukraine, width=220, height=140)
        self.USA_button = tk.Button(self, image=self.USA, width=220, height=140)
        self.Wales_button = tk.Button(self, image=self.Wales, width=220, height=140)
        self.Japan_button = tk.Button(self, image=self.Japan, width=220, height=140)
        self.China_button = tk.Button(self, image=self.China, width=220, height=140)

        self.title = tk.Label(self, text='Select the country whoms stats you would like to see', font='Helvetica 50')

        self.place_widgets()

    def place_widgets(self):
        # This project_code creates the widgets and grids them
        '''self.background.grid()'''
        self.title.grid(columnspan=10, row=0)
        self.Argentina_button.grid(column=0, row=1)
        self.Austria_button.grid(column=1, row=1)


    def when_pressed(self):
        print('hello')


if __name__ == '__main__':
    root = GUI()
    root.mainloop()
