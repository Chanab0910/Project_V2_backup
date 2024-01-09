import tkinter as tk
from tkinter import ttk


class TestGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        self.title_country = tk.Label(self, text='Country', font='helvetica 100')
        self.percentage_they_won_wc = tk.Label(self, text=f'Percentage that they won they won the World Cup: ',
                                               font='helvetica 30')
        self.furthest_place_got = tk.Label(self, text=f'Furthest place they got: ', font='helvetica 30')
        self.average_goals_scored_overall = tk.Label(self, text=f'Average number of goals that they scored per game '
                                                                f'overall: ', font='helvetica 30')
        self.average_goals_scored_group = tk.Label(self,
                                                   text=f'Average number of goals that they scored per game in the '
                                                        f'groups: ', font='helvetica 30')
        self.average_goals_scored_knockouts = tk.Label(self, text=f'Average number of goals that they scored per game '
                                                                  f'in the knockouts: ', font='helvetica 30')
        self.average_goals_conceded_overall = tk.Label(self,
                                                       text=f'Average number of goals that they conceded per game '
                                                            f'overall: ', font='helvetica 30')
        self.average_goals_conceded_group = tk.Label(self,
                                                     text=f'Average number of goals that they conceded per game '
                                                          f'in the groups: ', font='helvetica 30')
        self.average_goals_conceded_knockouts = tk.Label(self,
                                                         text=f'Average number of goals that they conceded per game '
                                                              f'in the knockouts: ', font='helvetica 30')
        self.lost_most_to_and_percentage_lost_most = tk.Label(self, text=f'They lost to ... the most amount of times, '
                                                                         f'but they had the worst loss percentage '
                                                                         f'record to ...', font='helvetica 30')

        self.won_most_to_and_percentage_won_most = tk.Label(self, text=f'They beat ... the most amount of times, '
                                                                       f'but they had the best win percentage '
                                                                       f'record to ...', font='helvetica 30')
        self.back_to_home_screen = tk.Button(self, text='Back to home screen')
        self.quit = tk.Button(self, text='Quit', command=quit)

        self.place_widgets()

    def place_widgets(self):
        self.title_country.grid(row=0, columnspan=10)
        self.percentage_they_won_wc.grid(row=1, columnspan=3)
        self.furthest_place_got.grid(row=2, column=0)
        self.average_goals_scored_overall.grid(row=3, columnspan=5)
        self.average_goals_scored_group.grid(row=4, columnspan=5)
        self.average_goals_scored_knockouts.grid(row=5, columnspan=5)
        self.average_goals_conceded_overall.grid(row=6, columnspan=5)
        self.average_goals_conceded_group.grid(row=7, columnspan=5)
        self.average_goals_conceded_knockouts.grid(row=8, columnspan=5)
        self.won_most_to_and_percentage_won_most.grid(row=9, columnspan=10)
        self.lost_most_to_and_percentage_lost_most.grid(row=10, columnspan=10)
        self.back_to_home_screen.grid(row=12, column=0)
        self.quit.grid(row=12, column=10)


if __name__ == '__main__':
    root = TestGUI()
    root.mainloop()
