import tkinter as tk
from tkinter import ttk
from project_code.analyse_results import Analyse

a = Analyse()
import Selecting_countries_page


class ResultGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, country_name, results):
        super().__init__()
        self.geometry("1450x650")

        self.title_country = tk.Label(self, text=f'{country_name}', font='helvetica 100', underline=True)
        self.came_dict = results[7]
        self.percentage_they_won_wc_label = tk.Label(self,
                                                     text=f"Percentage that they won they won the World Cup: {((self.came_dict['Win'] / 99)*100):.2f}%",
                                                     font='helvetica 30')
        self.furthest_place_got_label = tk.Label(self, text=f'Furthest place they got: {results[6]}',
                                                 font='helvetica 30')
        self.average_goals_scored_overall_label = tk.Label(self,
                                                           text=f'Average number of goals that they scored per game: {results[3]:.2f} '
                                                           , font='helvetica 30')
        self.average_goals_scored_group_label = tk.Label(self,
                                                         text=f'Average number of goals that they scored per game in the '
                                                              f'groups: {results[4]:.2f}', font='helvetica 30')
        self.average_goals_scored_knockouts_label = tk.Label(self,
                                                             text=f'Average number of goals that they scored per game '
                                                                  f'in the knockouts: {results[5]:.2f}',
                                                             font='helvetica 30')
        self.average_goals_conceded_overall_label = tk.Label(self,
                                                             text=f'Average number of goals that they conceded per game '
                                                                  f'overall: {results[0]:.2f}', font='helvetica 30')
        self.average_goals_conceded_group_label = tk.Label(self,
                                                           text=f'Average number of goals that they conceded per game '
                                                                f'in the groups: {results[1]:.2f}', font='helvetica 30')
        self.average_goals_conceded_knockouts_label = tk.Label(self,
                                                               text=f'Average number of goals that they conceded per game '
                                                                    f'in the knockouts: {results[2]:.2f}',
                                                               font='helvetica 30')
        self.won_most_to_and_percentage_won_most_label = tk.Label(self,
                                                                  text=f"They beat {results[8]} the most amount of times, "
                                                                       f"but they had the best win percentage "
                                                                       f"record to {results[9]}", font='helvetica 30')
        self.lost_most_to_and_percentage_lost_most_label = tk.Label(self,
                                                                    text=f"They lost to {results[10]} the most amount of times, "
                                                                         f"but they had the worst loss percentage "
                                                                         f"record to {results[11]}", font='helvetica 30')


        self.back_to_home_screen = tk.Button(self, text='Back to home screen', command=self.go_to_next_page)
        self.quit = tk.Button(self, text='Quit', command=quit)

        self.place_widgets()

    def place_widgets(self):
        self.title_country.grid(row=0, columnspan=10)
        self.percentage_they_won_wc_label.place(x=5, y=140)
        self.furthest_place_got_label.place(x=5, y=182)
        self.average_goals_scored_overall_label.place(x=5, y=227)
        self.average_goals_scored_group_label.place(x=5, y=272)
        self.average_goals_scored_knockouts_label.place(x=5, y=317)
        self.average_goals_conceded_overall_label.place(x=5, y=362)
        self.average_goals_conceded_group_label.place(x=5, y=407)
        self.average_goals_conceded_knockouts_label.place(x=5, y=452)
        self.won_most_to_and_percentage_won_most_label.place(x=5, y=497)
        self.lost_most_to_and_percentage_lost_most_label.place(x=5, y=542)
        self.back_to_home_screen.place(x=5, y=600)

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.GUI()
        self.gui.mainloop()


if __name__ == '__main__':
    root = ResultGUI('England')
    root.mainloop()
