import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class ResultsFigures(tk.Toplevel):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self,results):
        super().__init__()
        self.title = tk.Label(self,text='title')
        self.pie_chart(results[7])
        self.bar_chart(results[-1])
        self.place_widgets()


    def pie_chart(self, where_they_came):
        titles = ['Group', 'R16', 'Quarters', 'Semis', 'Final', 'Win']
        data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'],
                where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]
        fig = Figure(figsize=(4, 4))

        ax = fig.add_subplot(111)
        ax.pie(data, radius=1, labels=titles, autopct='%0.2f%%')
        pie = FigureCanvasTkAgg(fig,master=self)
        pie.get_tk_widget().grid(row=1,column=0)

    def bar_chart(self, where_they_came):
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

    def place_widgets(self):
        self.title.grid(row=0,column=0)


