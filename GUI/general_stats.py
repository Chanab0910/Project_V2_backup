import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Selecting_countries_page
from project_code.general_analysis import GeneralAnalysis
from project_code.analyse_results import Analyse


class GeneralStatsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Table')
        self.geometry('1400x770')
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
        self.pie_title = tk.Label(self,text = 'Pie chart that shows the distribution of how often each' '\n'' team won the World Cup',font='helvetica 20')
        self.place_widgets()
        self.num_wins()

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
        everything = ga.get_stats()
        place_list = everything[0]
        scored = everything[1]
        conceded = everything[2]

        for i,country in enumerate(place_list):
            countries.append((i+1,place_list[i], scored[country], conceded[country]))

        # add data to the treeview
        for country in countries:
            self.tree.insert('', tk.END, values=country)

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='wns')

    def num_wins(self):
        list_of_countries = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Canada', 'Croatia', 'Czech Republic',
                             'Denmark', 'England', 'Finland', 'France', 'Germany',
                             'Hungary', 'Iceland', 'Ireland', 'Italy', 'Mexico', 'Ghana', 'Netherlands', 'Morocco',
                             'Norway', 'Poland', 'Portugal', 'Romania', 'Scotland', 'Spain',
                             'Sweden', 'Ukraine', 'USA', 'Wales', 'Japan', 'China']
        analyse = Analyse()
        titles = []
        for country in list_of_countries:
            dict = analyse.furthest_got_and_average_place(country)
            if dict['Win'] != 0:
                titles.append(country)

        data = []
        for country in titles:
            dict = analyse.furthest_got_and_average_place(country)
            country_wins = dict['Win']
            data.append(country_wins)

        fig = Figure(figsize=(4.8,4))

        ax = fig.add_subplot(111)
        ax.pie(data, radius=1.3, labels=titles, autopct='%0.2f%%')
        pie = FigureCanvasTkAgg(fig)
        pie.get_tk_widget().place(x=910, y=230)

    def place_widgets(self):
        self.general_stats.grid(row=0, column=0)
        self.title.grid(row=1, column=0, padx=5, sticky='w')
        self.pie_title.grid(row=1, column=2, sticky='w')
        self.tree.grid(row=2, column=0, sticky='nsew')
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        self.description_ga1.grid(row=3,column=0, sticky='w')
        self.description_ga2.grid(row=4, column=0, sticky='w')
        self.space.grid(row=5,column=0)

        self.description_gc1.grid(row=5, column=0,sticky='w')
        self.description_gc2.grid(row=7, column=0, sticky='w')
        self.space.grid(row=8, column=0)
        self.back_to_home_screen.grid(row=9,column=0, sticky='w')

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.GUI()
        self.gui.mainloop()






if __name__ == "__main__":
    app = GeneralStatsGUI()
    app.mainloop()
