import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from project_code.general_analysis import GeneralAnalysis


class App(tk.Tk):
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

        for i in range(place_list):
            countries.append((place_list[i], scored[i], conceded[i]))

        # add data to the treeview
        for country in countries:
            self.tree.insert('', tk.END, values=country)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message on clicking
            showinfo(title='Information', message=','.join(record))


if __name__ == "__main__":
    app = App()
    app.mainloop()
