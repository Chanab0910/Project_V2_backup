import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt

from project_code.analyse_results import Analyse

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

analyse = Analyse()
import Selecting_countries_page


class ResultGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self, country_name, results):
        super().__init__()
        '''self.geometry("1810x650")'''

        self.title_country = tk.Label(self, text=f'{country_name}', font='helvetica 100', )
        self.came_dict = results[7]
        self.percentage_they_won_wc_label = tk.Label(self,
                                                     text=f"Percentage that they won the World Cup: {((self.came_dict['Win'] / 100) * 100):.2f}%",
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

        ''' self.pie_title = tk.Label(self, text=f'Pie chart to illustrate the probability' '\n' f' that {country_name} '
                                             'gets knocked out in' '\n' ' each stage in the competition  ',
                                  font='helvetica 20 italic')'''
        self.figures =tk.Button(self, text='Figures', font='helvetica 27',command=lambda: [self.get_figures(results)])
        '''self.pie_chart(results[7])'''
        '''self.bar_chart(results[-1])'''
        self.place_widgets()

    def get_figures(self,results):
        f = ResultsFigures(results)
        f.mainloop()


    def place_widgets(self):
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
        self.figures.grid(row=12,column=0)
        self.back_to_home_screen.grid(row=11, column=0, sticky='w')

    def pie_chart(self, where_they_came):
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]
        fig = Figure(figsize=(4, 4))

        ax = fig.add_subplot(111)
        ax.pie(data, radius=1, labels=titles, autopct='%0.2f%%')
        pie = FigureCanvasTkAgg(fig)
        pie.get_tk_widget().place(x=1310, y=0)

    def bar_chart(self, where_they_came):
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]

        f = Figure(figsize=(5, 5), dpi=100)
        ax = f.add_subplot(111)

        width = 0.5
        ax.bar(titles, data, width)
        canvas = FigureCanvasTkAgg(f)
        canvas.draw()
        canvas.get_tk_widget().place(x=1310, y=0)

    def go_to_next_page(self):
        self.destroy()
        self.gui = Selecting_countries_page.GUI()
        self.gui.mainloop()


class ResultsFigures(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self,results):
        super().__init__()
        self.title = tk.Label(self,text='title')
        self.bar_chart(results[-1])
        self.pie_chart(results[7])
        self.place_widgets()

    def pie_chart(self, where_they_came):
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]
        fig = Figure(figsize=(4, 4))

        ax = fig.add_subplot(111)
        ax.pie(data, radius=1, labels=titles, autopct='%0.2f%%')
        pie = FigureCanvasTkAgg(fig)
        pie.get_tk_widget().grid(row=1,column=1)

    def bar_chart(self, where_they_came):
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]

        f = Figure(figsize=(5, 5), dpi=100)
        ax = f.add_subplot(111)

        width = 0.5
        ax.bar(titles, data, width)
        canvas = FigureCanvasTkAgg(f)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=0)

    def place_widgets(self):
        self.title.grid(row=0,column=0)


if __name__ == '__main__':
    root = ResultGUI('England')
    root.mainloop()
