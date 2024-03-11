import tkinter as tk
from tkinter import ttk

import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Selecting_countries_page
from project_code.general_analysis import GeneralAnalysis
from project_code.analyse_results import Analyse

from collections import OrderedDict
import numpy as np



class GeneralStatsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Table')
        self.create_table()
        self.general_stats = tk.Label(self,text='General Statistics', font='helvetica 100')
        self.title = tk.Label(self,text='Table that shows the overall place each country came after' '\n''taking into account every simulation:',font='helvetica 20', pady=10,)
        self.description_ga1 = tk.Label(self, text='GA: The average goals scored per game (taking into account all group and',font='helvetica 15')
        self.description_ga2 = tk.Label(self,
                                        text='       knockout games in every simulation)',
                                        font='helvetica 15')
        self.description_gc1 = tk.Label(self,
                                    text='GC: The average goals conceded per game (taking into account all group and',
                                    font='helvetica 15')
        self.description_gc2 = tk.Label(self,
                                       text='       knockout games in every simulation)',
                                       font='helvetica 15')
        self.back_to_home_screen = tk.Button(self, text='Back to home screen', command=self.go_to_next_page)
        self.space = tk.Label(self,text = ' ')

        self.order_by_ga = tk.Button(self,text='Order by GA',command=self.create_GA_table)
        self.order_by_gc = tk.Button(self, text='Order by GC', command=self.create_GC_table)
        self.order_by_overall= tk.Button(self, text='Order by Overall', command=self.overall_table_so_no_reload)
        '''self.num_wins()'''
        self.quit = tk.Button(self, text='Quit', command=self.quits)
        self.place_widgets()


    def create_table(self):
        # define columns
        columns = ('Place','Country', 'GA', 'GC')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Place', text='Place')
        self.tree.heading('Country', text='Country')
        self.tree.heading('GA', text='GA')
        self.tree.heading('GC', text='GC')

        # generate sample data
        countries = []
        ga = GeneralAnalysis()
        self.everything = ga.get_stats()
        self.place_list = self.everything[0]
        self.scored = self.everything[1]
        self.conceded = self.everything[2]

        for i,country in enumerate(self.place_list):
            countries.append((i+1,self.place_list[i], self.scored[country], self.conceded[country]))

        # add data to the treeview
        for country in countries:
            self.tree.insert('', tk.END, values=country)

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.tree.grid(row=3, columnspan=3, sticky='nsew')


    def create_GA_table(self):
        columns = ('Place', 'Country', 'GA', 'GC')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Place', text='Place')
        self.tree.heading('Country', text='Country')
        self.tree.heading('GA', text='GA')
        self.tree.heading('GC', text='GC')

        countries = []

        self.list_ga_sorted = self.dictToList(self.scored)
        self.ga_sorted = self.merge_sort(self.list_ga_sorted, self.keyGoalScored)
        reversed_list = []
        for i,country in enumerate(self.ga_sorted[::-1]):
            reversed_list.append([country[0],country[1]])

        for i,country in enumerate(reversed_list):
            countries.append((i+1,country[0], reversed_list[i][1], self.conceded[country[0]]))

        for country in countries:
            self.tree.insert('', tk.END, values=country)

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.tree.grid(row=3, columnspan=3, sticky='nsew')


    def create_GC_table(self):
        columns = ('Place', 'Country', 'GA', 'GC')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Place', text='Place')
        self.tree.heading('Country', text='Country')
        self.tree.heading('GA', text='GA')
        self.tree.heading('GC', text='GC')

        countries = []


        self.list_gc_sorted = self.dictToList(self.conceded)
        self.gc_sorted = self.merge_sort(self.list_gc_sorted,self.keyGoalScored)
        reversed_list = []

        for i,country in enumerate(self.gc_sorted):
            countries.append((i+1,country[0], self.scored[country[0]], self.gc_sorted[i][1]))

        for country in countries:
            self.tree.insert('', tk.END, values=country)

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.tree.grid(row=3, columnspan=3, sticky='nsew')


    def overall_table_so_no_reload(self):
        columns = ('Place', 'Country', 'GA', 'GC')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Place', text='Place')
        self.tree.heading('Country', text='Country')
        self.tree.heading('GA', text='GA')
        self.tree.heading('GC', text='GC')

        # generate sample data
        countries = []

        for i, country in enumerate(self.place_list):
            countries.append((i + 1, self.place_list[i], self.scored[country], self.conceded[country]))

        # add data to the treeview
        for country in countries:
            self.tree.insert('', tk.END, values=country)

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.tree.grid(row=3, columnspan=3, sticky='nsew')

    def dictToList(self,dictionary):
        football = []
        keys = dictionary.keys()

        for key in keys:
            football.append([key, dictionary[key]])
        return football

    def merge(self,merged, list_1, list_2, key):
        index_1 = 0
        index_2 = 0
        index_merged = 0
        while index_1 < len(list_1) and index_2 < len(list_2):
            if key(list_1[index_1]) < key(list_2[index_2]):  # comparision line
                merged[index_merged] = list_1[index_1]
                index_1 = index_1 + 1
            else:
                merged[index_merged] = list_2[index_2]
                index_2 = index_2 + 1
            index_merged = index_merged + 1

        while index_1 < len(list_1):
            merged[index_merged] = list_1[index_1]
            index_1 = index_1 + 1
            index_merged = index_merged + 1

        while index_2 < len(list_2):
            merged[index_merged] = list_2[index_2]
            index_2 = index_2 + 1
            index_merged = index_merged + 1
        return merged

    def merge_sort(self,items, key):
        if len(items) < 2:
            return items
        else:
            midpoint = len(items) // 2
            left_half = items[:midpoint]
            right_half = items[midpoint:]

        left_half = self.merge_sort(left_half, key)
        right_half = self.merge_sort(right_half, key)
        result = self.merge(items, left_half, right_half, key)
        return result

    def keyGoalScored(self,country):
        return country[1]


    def place_widgets(self):
        self.general_stats.grid(row=0, columnspan=10)
        self.title.grid(row=1, column=0, padx=5, sticky='w')

        self.order_by_ga.grid(row=1, column=1)
        self.order_by_gc.grid(row=1, column=2)
        self.order_by_overall.grid(row=1, column=3)
        self.tree.grid(row=3, columnspan=4, sticky='nsew')
        self.scrollbar.grid(row=3, column=4, sticky='wns')
        self.description_ga1.grid(row=4,column=0, sticky='w')
        self.description_ga2.grid(row=5, column=0, sticky='w')


        self.description_gc1.grid(row=6, column=0,sticky='w')
        self.description_gc2.grid(row=7, column=0, sticky='w')
        self.space.grid(row=8, column=0)
        self.quit.grid(row=9,column=4,sticky='e')

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.SelectingCountriesPageGUI()
        self.gui.mainloop()

    def quits(self):
        self.destroy()






if __name__ == "__main__":
    app = GeneralStatsGUI()
    app.mainloop()
