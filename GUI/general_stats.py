import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from project_code.general_analysis import GeneralAnalysis


class GeneralStatsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Table')
        self.geometry('620x200')
        self.create_table()

    def create_table(self):
        # define columns
        columns = ('Country', 'GA', 'GC')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Country', text='Country')
        self.tree.heading('GA', text='GA')
        self.tree.heading('GC', text='GC')

        # generate sample data
        countries = []
        ga = GeneralAnalysis()
        everything = ga.get_stats()
        place_list = everything[0]
        scored = everything[1]
        conceded = everything[2]

        for i,country in enumerate(place_list):
            countries.append((place_list[i], scored[country], conceded[country]))

        # add data to the treeview
        for country in countries:
            self.tree.insert('', tk.END, values=country)



        self.tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')




if __name__ == "__main__":
    app = GeneralStatsGUI()
    app.mainloop()
