import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt

from project_code.analyse_results import Analyse

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import Selecting_countries_page
import results_figures

analyse = Analyse()


class ResultGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own
    widgets to the Frame"""

    def __init__(self, country_name, results):
        super().__init__()

        self.title_country = tk.Label(self, text=f'{country_name}', font='helvetica 100', )
        self.came_dict = results[7]
        self.percentage_they_won_wc_label = tk.Label(self,
                                                     text=f"Percentage that they won the World Cup: {self.came_dict['Win']}%",
                                                     font='helvetica 27')
        self.furthest_place_got_label = tk.Label(self, text=f'Furthest place they got: {results[6]}',
                                                 font='helvetica 27')
        self.average_goals_scored_overall_label = tk.Label(self,
                                                           text=f'Average number of goals that they scored per game: {results[3]:.2f} '
                                                           , font='helvetica 27')
        self.average_goals_scored_group_label = tk.Label(self,
                                                         text=f'Average number of goals that they scored per game in the '
                                                              f'groups: {results[4]:.2f}', font='helvetica 27')
        self.average_goals_scored_knockouts_label = tk.Label(self,
                                                             text=f'Average number of goals that they scored per game '
                                                                  f'in the knockouts: {results[5]:.2f}',
                                                             font='helvetica 27')
        self.average_goals_conceded_overall_label = tk.Label(self,
                                                             text=f'Average number of goals that they conceded per game '
                                                                  f'overall: {results[0]:.2f}', font='helvetica 27')
        self.average_goals_conceded_group_label = tk.Label(self,
                                                           text=f'Average number of goals that they conceded per game '
                                                                f'in the groups: {results[1]:.2f}', font='helvetica 27')
        self.average_goals_conceded_knockouts_label = tk.Label(self,
                                                               text=f'Average number of goals that they conceded per game '
                                                                    f'in the knockouts: {results[2]:.2f}',
                                                               font='helvetica 27')
        self.won_most_to_and_percentage_won_most_label = tk.Label(self,
                                                                  text=f"They beat {results[8]} the most amount of times, "
                                                                       f"but they had the best win percentage "
                                                                       f"record to {results[9]}", font='helvetica 27')
        self.lost_most_to_and_percentage_lost_most_label = tk.Label(self,
                                                                    text=f"They lost to {results[10]} the most amount of times, "
                                                                         f"but they had the worst loss percentage "
                                                                         f"record to {results[11]}",
                                                                    font='helvetica 27')

        self.back_to_home_screen = tk.Button(self, text='Back to home screen', command=self.go_to_next_page)
        self.quit = tk.Button(self, text='Quit', command=quit)

        self.figures = tk.Button(self, text='Figures', font='helvetica 27',
                                 command=lambda: [self.go_to_figures(results, country_name)])

        self.place_widgets()

    def go_to_figures(self, results, country_name):
        """
        creates a new frame with the figures
        Parameters
        ----------
        results: All the data from the Analyse class
        country_name: The name of the country

        Returns
        -------
        None
        """

        self.gui = results_figures.ResultsFigures(results, country_name)
        self.gui.mainloop()

    def place_widgets(self):
        """Places the widgets"""
        self.title_country.grid(row=0, column=0, sticky='w')
        self.percentage_they_won_wc_label.grid(row=1, column=0, sticky='w')
        self.furthest_place_got_label.grid(row=2, column=0, sticky='w')
        self.average_goals_scored_overall_label.grid(row=3, column=0, sticky='w')
        self.average_goals_scored_group_label.grid(row=4, column=0, sticky='w')
        self.average_goals_scored_knockouts_label.grid(row=5, column=0, sticky='w')
        self.average_goals_conceded_overall_label.grid(row=6, column=0, sticky='w')
        self.average_goals_conceded_group_label.grid(row=7, column=0, sticky='w')
        self.average_goals_conceded_knockouts_label.grid(row=8, column=0, sticky='w')
        self.won_most_to_and_percentage_won_most_label.grid(row=9, column=0, sticky='w')
        self.lost_most_to_and_percentage_lost_most_label.grid(row=10, column=0, sticky='w')
        '''self.pie_title.place(x=1230, y=400)'''
        self.figures.grid(row=12, column=0)
        self.back_to_home_screen.grid(row=11, column=0, sticky='w')

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.SelectingCountriesPageGUI()
        self.gui.mainloop()


if __name__ == '__main__':
    root = ResultGUI('England')
    root.mainloop()
