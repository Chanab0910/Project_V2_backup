import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from project_code.analyse_results import Analyse



class GraphGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = tk.Label(self, text=f'A graph to show the percentage chance that each country has of winning the World Cup', font='helvetica 20')
        '''self.quit = tk.Button(self, text='Quit', command=self.quits)'''
        self.place_widgets()
        self.bar_chart()


    def bar_chart(self):
        list_of_countries = ['Argentina', 'France', 'England', 'Belgium', 'Brazil',
                             'Netherlands', 'Portugal', 'Spain',
                             'Italy', 'Croatia', 'Uruguay', 'Morocco', 'USA', 'Columbia',
                             'Mexico', 'Germany', 'Senegal', 'Japan',
                             'Switzerland', 'Iran', 'Denmark', 'Korea', 'Australia',
                             'Ukraine', 'Austria', 'Sweden', 'Hungary', 'Nigeria',
                             'Wales', 'Poland', 'Equador', 'Serbia']
        titles = []
        analyse = Analyse()
        for country in list_of_countries:
            dict = analyse.furthest_got_and_average_place(country)
            if dict['Win'] != 0:
                titles.append(country)

        data = []
        for country in titles:
            dict = analyse.furthest_got_and_average_place(country)
            country_wins = dict['Win']
            data.append(country_wins)

        for i in range(len(titles)):
            titles[i] = titles[i][:3]

        f = Figure(figsize=(12, 5), dpi=100)
        ax = f.add_subplot(111)

        width = 0.5
        rects1 = ax.bar(titles, data, width)
        canvas = FigureCanvasTkAgg(f)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=0)

    def place_widgets(self):
        self.title.grid(row=0,column=0)
        '''self.quit.grid(row=2, column=0, sticky='e')'''

    '''def quits(self):
        self.destroy()'''

if __name__ == '__main__':
    root = GraphGUI()
    root.mainloop()