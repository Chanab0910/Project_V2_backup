import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class ResultsFigures(tk.Toplevel):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self,results,country_name):
        super().__init__()
        self.title = tk.Label(self,text=f"{country_name}'s Figures",font='helvetica 70')
        self.pie_chart(results[7])
        self.bar_chart(results[-1])
        self.pie_title = tk.Label(self, text=f'Pie chart to illustrate the probability' '\n' f' that {country_name} '
                                             'gets knocked out in' '\n' ' each stage in the competition  ',
                                  font='helvetica 20 italic')
        self.bar_title = tk.Label(self, text=f'Bar chart to illustrate the probability' '\n' f' that {country_name} '
                                             'reach each individual' '\n' 'stage in the competition  ',
                                  font='helvetica 20 italic')
        self.quit= tk.Button(self,text='Quit',font='helvetica 20',command=self.quits)
        self.place_widgets()


    def pie_chart(self, where_they_came):
        """
        Creates a pie chart based on how many times they got to each section

        Parameters
        ----------
        where_they_came: This is a dictionary with the data of where they got to

        Returns
        -------
        None

        """
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]
        fig = Figure(figsize=(4, 4))

        ax = fig.add_subplot(111)
        ax.pie(data, radius=1, labels=titles, autopct='%0.2f%%')
        pie = FigureCanvasTkAgg(fig,master=self)
        pie.get_tk_widget().grid(row=1,column=0,padx=20)

    def bar_chart(self, where_they_came):
        """
        This creates a bar chart with the probability of a country getting to each stage
        Parameters
        ----------
        where_they_came: This is a dictionary with the data of where they got to

        Returns
        -------
        None
        """
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]

        f = Figure(figsize=(5, 5), dpi=100)
        ax = f.add_subplot(111)

        width = 0.5
        ax.bar(titles, data, width)
        canvas = FigureCanvasTkAgg(f,master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=1)

    def quits(self):
        self.destroy()

    def place_widgets(self):
        """
        places widgets
        Returns
        -------
        None
        """

        self.title.grid(row=0,columnspan=2)
        self.pie_title.grid(row=2,column=0)
        self.bar_title.grid(row=2,column=1)
        self.quit.grid(row=3,column=0,pady=20)


