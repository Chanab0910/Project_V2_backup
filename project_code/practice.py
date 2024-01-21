import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from project_code.analyse_results import Analyse
analyse = Analyse()

root = tk.Tk()
Pie_frame = tk.Frame(root)
Pie_frame.pack()
where_they_came = analyse.furthest_got_and_average_place('Spain')

titles = ['Group' , 'R16', 'Quarters', 'Semis', 'Final', 'Win']
data = [where_they_came['Group'], where_they_came['Round of 16'], where_they_came['Quarter-final'], where_they_came['Semi-final'], where_they_came['Final'], where_they_came['Win']]

fig = Figure() # create a figure object
ax = fig.add_subplot(111) # add an Axes to the figure

ax.pie(data, radius=1, labels=titles, autopct='%0.2f%%')

pie = FigureCanvasTkAgg(fig, Pie_frame)
pie.get_tk_widget().pack()

root.mainloop()