import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        
