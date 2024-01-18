import tkinter as tk
from tkinter import ttk
from project_code.analyse_results import Analyse
a = Analyse()
from Selecting_countries_page import GUI
gui = GUI()

class ResultGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.geometry("1300x697")
        self.country_name = gui.country_name
        self.title_country = tk.Label(self, textvariable=self.country_name, font='helvetica 100', underline=True)
        self.percentage_they_won_wc_label = tk.Label(self, text=f'Percentage that they won they won the World Cup: ',
                                               font='helvetica 25')
        self.furthest_place_got_label = tk.Label(self, text=f'Furthest place they got: ', font='helvetica 25')
        self.average_goals_scored_overall_label = tk.Label(self, text=f'Average number of goals that they scored per game '
                                                                f'overall: ', font='helvetica 25')
        self.average_goals_scored_group_label = tk.Label(self,
                                                   text=f'Average number of goals that they scored per game in the '
                                                        f'groups: ', font='helvetica 25')
        self.average_goals_scored_knockouts_label = tk.Label(self, text=f'Average number of goals that they scored per game '
                                                                  f'in the knockouts: ', font='helvetica 25')
        self.average_goals_conceded_overall_label = tk.Label(self,
                                                       text=f'Average number of goals that they conceded per game '
                                                            f'overall: ', font='helvetica 25')
        self.average_goals_conceded_group_label = tk.Label(self,
                                                     text=f'Average number of goals that they conceded per game '
                                                          f'in the groups: ', font='helvetica 25')
        self.average_goals_conceded_knockouts_label = tk.Label(self,
                                                         text=f'Average number of goals that they conceded per game '
                                                              f'in the knockouts: ', font='helvetica 25')
        self.lost_most_to_and_percentage_lost_most_label = tk.Label(self, text=f'They lost to ... the most amount of times, '
                                                                         f'but they had the worst loss percentage '
                                                                         f'record to ...', font='helvetica 25')

        self.won_most_to_and_percentage_won_most_label = tk.Label(self, text=f'They beat ... the most amount of times, '
                                                                       f'but they had the best win percentage '
                                                                       f'record to ...', font='helvetica 25')
        self.back_to_home_screen = tk.Button(self, text='Back to home screen',command=self.go_to_next_page, font='helvetica 15')
        self.quit = tk.Button(self, text='Quit', command=quit)

        self.place_widgets()

    def place_widgets(self):
        self.title_country.grid(row=0, columnspan=10)
        self.percentage_they_won_wc_label.place(x=5, y=148)
        self.furthest_place_got_label.place(x=5, y=190)
        self.average_goals_scored_overall_label.place(x=5, y=235)
        self.average_goals_scored_group_label.place(x=5, y=280)
        self.average_goals_scored_knockouts_label.place(x=5, y=325)
        self.average_goals_conceded_overall_label.place(x=5, y=370)
        self.average_goals_conceded_group_label.place(x=5, y=415)
        self.average_goals_conceded_knockouts_label.place(x=5, y=460)
        self.won_most_to_and_percentage_won_most_label.place(x=5, y=505)
        self.lost_most_to_and_percentage_lost_most_label.place(x=5, y=550)
        self.back_to_home_screen.place(x=5, y=653)

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.GUI()
        self.gui.mainloop()





if __name__ == '__main__':
    root = ResultGUI()
    root.mainloop()
