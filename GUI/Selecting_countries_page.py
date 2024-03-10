import tkinter as tk
from tkinter import ttk
from project_code.analyse_results import Analyse
from table import GeneralStatsGUI
from PIL import Image, ImageTk
import results_page
from selecting_what_general_stats import SelectGUI

class SelectingCountriesPageGUI(tk.Tk):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""

    def __init__(self):
        super().__init__()
        im=Image.open("../img/Argentina.png")
        resized_image = im.resize((150,95))
        self.Argentina = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Australia.png")
        resized_image = im.resize((150, 95))
        self.Australia = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Austria.png")
        resized_image = im.resize((150, 95))
        self.Austria = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Belgium.png")
        resized_image = im.resize((150, 95))
        self.Belgium = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Brazil.png")
        resized_image = im.resize((150, 95))
        self.Brazil = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Colombia.png")
        resized_image = im.resize((150, 95))
        self.Colombia = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Croatia.png")
        resized_image = im.resize((150, 95))
        self.Croatia = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Denmark.png")
        resized_image = im.resize((150, 95))
        self.Denmark = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/England.png")
        resized_image = im.resize((150, 95))
        self.England = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Equador.png")
        resized_image = im.resize((150, 95))
        self.Equador = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/France.png")
        resized_image = im.resize((150, 95))
        self.France = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Germany.png")
        resized_image = im.resize((150, 95))
        self.Germany = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Hungary.png")
        resized_image = im.resize((150, 95))
        self.Hungary = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Iran.png")
        resized_image = im.resize((150, 95))
        self.Iran = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Italy.png")
        resized_image = im.resize((150, 95))
        self.Italy = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Japan.png")
        resized_image = im.resize((150, 95))
        self.Japan = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Mexico.png")
        resized_image = im.resize((150, 95))
        self.Mexico = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Korea.png")
        resized_image = im.resize((150, 95))
        self.Korea = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Netherlands.png")
        resized_image = im.resize((150, 95))
        self.Netherlands = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Morocco.png")
        resized_image = im.resize((150, 95))
        self.Morocco = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Nigeria.png")
        resized_image = im.resize((150, 95))
        self.Nigeria = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Poland.png")
        resized_image = im.resize((150, 95))
        self.Poland = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Portugal.png")
        resized_image = im.resize((150, 95))
        self.Portugal = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Senegal.png")
        resized_image = im.resize((150, 95))
        self.Senegal = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Serbia.png")
        resized_image = im.resize((150, 95))
        self.Serbia = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Spain.png")
        resized_image = im.resize((150, 95))
        self.Spain = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Sweden.png")
        resized_image = im.resize((150, 95))
        self.Sweden = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Switzerland.png")
        resized_image = im.resize((150, 95))
        self.Switzerland = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Ukraine.png")
        resized_image = im.resize((150, 95))
        self.Ukraine = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/USA.png")
        resized_image = im.resize((150, 95))
        self.USA = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Wales.png")
        resized_image = im.resize((150, 95))
        self.Wales = ImageTk.PhotoImage(resized_image)

        im = Image.open("../img/Uruguay.png")
        resized_image = im.resize((150, 95))
        self.Uruguay = ImageTk.PhotoImage(resized_image)



        self.Argentina_button = tk.Button(self, image=self.Argentina,command=lambda: [self.go_to_next_page('Argentina')])
        self.Australia_button = tk.Button(self, image=self.Australia,command=lambda: [self.go_to_next_page('Australia')])
        self.Austria_button = tk.Button(self, image=self.Austria,command=lambda: [self.go_to_next_page('Austria')])
        self.Belgium_button = tk.Button(self, image=self.Belgium,command=lambda: [self.go_to_next_page('Belgium')])
        self.Brazil_button = tk.Button(self, image=self.Brazil,command=lambda: [self.go_to_next_page('Brazil')])
        self.Croatia_button = tk.Button(self, image=self.Croatia,command=lambda: [self.go_to_next_page('Croatia')])
        self.Colombia_button = tk.Button(self, image=self.Colombia,command=lambda: [self.go_to_next_page('Colombia')])
        self.Denmark_button = tk.Button(self, image=self.Denmark,command=lambda: [self.go_to_next_page('Denmark')])
        self.England_button = tk.Button(self, image=self.England,command=lambda: [self.go_to_next_page('England')])
        self.Equador_button = tk.Button(self, image=self.Equador,command=lambda: [self.go_to_next_page('Equador')])
        self.France_button = tk.Button(self, image=self.France,command=lambda: [self.go_to_next_page('France')])
        self.Germany_button = tk.Button(self, image=self.Germany,command=lambda: [self.go_to_next_page('Germany')])
        self.Hungary_button = tk.Button(self, image=self.Hungary,command=lambda: [self.go_to_next_page('Hungary')])
        self.Iran_button = tk.Button(self, image=self.Iran,command=lambda: [self.go_to_next_page('Iran')])
        self.Italy_button = tk.Button(self, image=self.Italy, command=lambda: [self.go_to_next_page('Italy')])
        self.Japan_button = tk.Button(self, image=self.Japan, command=lambda: [self.go_to_next_page('Japan')])
        self.Korea_button = tk.Button(self, image=self.Korea, command=lambda: [self.go_to_next_page('Korea')])
        self.Mexico_button = tk.Button(self, image=self.Mexico,command=lambda: [self.go_to_next_page('Mexico')])
        self.Netherlands_button = tk.Button(self, image=self.Netherlands,command=lambda: [self.go_to_next_page('Netherlands')])
        self.Morocco_button = tk.Button(self, image=self.Morocco,command=lambda: [self.go_to_next_page('Morocco')] )
        self.Nigeria_button = tk.Button(self, image=self.Nigeria, command=lambda: [self.go_to_next_page('Nigeria')])
        self.Poland_button = tk.Button(self, image=self.Poland,command=lambda: [self.go_to_next_page('Poland')])
        self.Portugal_button = tk.Button(self, image=self.Portugal,command=lambda: [self.go_to_next_page('Portugal')])
        self.Senegal_button = tk.Button(self, image=self.Senegal,command=lambda: [self.go_to_next_page('Senegal')])
        self.Serbia_button = tk.Button(self, image=self.Serbia,command=lambda: [self.go_to_next_page('Serbia')])
        self.Spain_button = tk.Button(self, image=self.Spain, command=lambda: [self.go_to_next_page('Spain')])
        self.Sweden_button = tk.Button(self, image=self.Sweden, command=lambda: [self.go_to_next_page('Sweden')])
        self.Switzerland_button = tk.Button(self, image=self.Switzerland, command=lambda: [self.go_to_next_page('Switzerland')])
        self.Ukraine_button = tk.Button(self, image=self.Ukraine, command=lambda: [self.go_to_next_page('Ukraine')])
        self.USA_button = tk.Button(self, image=self.USA, command=lambda: [self.go_to_next_page('USA')])
        self.Wales_button = tk.Button(self, image=self.Wales,command=lambda: [self.go_to_next_page('Wales')])
        self.Uruguay_button = tk.Button(self, image=self.Uruguay,command=lambda: [self.go_to_next_page('Uruguay')])


        self.title = tk.Label(self, text="Select the country whos stats you would like to see",
                              font='FuturaStd-Medium 50')
        self.Argentina_label = tk.Label(self, text='Argentina', font='FuturaStd-Medium 20')
        self.Australia_label = tk.Label(self, text='Australia', font='FuturaStd-Medium 20')
        self.Austria_label = tk.Label(self, text='Austria', font='FuturaStd-Medium 20')
        self.Belgium_label = tk.Label(self, text='Belgium', font='FuturaStd-Medium 20')
        self.Brazil_label = tk.Label(self, text='Brazil', font='FuturaStd-Medium 20')
        self.Croatia_label = tk.Label(self, text='Croatia', font='FuturaStd-Medium 20')
        self.Colombia_label = tk.Label(self, text='Colombia', font='FuturaStd-Medium 20')
        self.Denmark_label = tk.Label(self, text='Denmark', font='FuturaStd-Medium 20')
        self.England_label = tk.Label(self, text='England', font='FuturaStd-Medium 20')
        self.Equador_label = tk.Label(self, text='Equador', font='FuturaStd-Medium 20')
        self.France_label = tk.Label(self, text='France', font='FuturaStd-Medium 20')
        self.Germany_label = tk.Label(self, text='Germany', font='FuturaStd-Medium 20')
        self.Hungary_label = tk.Label(self, text='Hungary', font='FuturaStd-Medium 20')
        self.Iran_label = tk.Label(self, text='Iran', font='FuturaStd-Medium 20')
        self.Italy_label = tk.Label(self, text='Italy', font='FuturaStd-Medium 20')
        self.Japan_label = tk.Label(self, text='Japan', font='FuturaStd-Medium 20')
        self.Korea_label = tk.Label(self, text='Korea', font='FuturaStd-Medium 20')
        self.Mexico_label = tk.Label(self, text='Mexico', font='FuturaStd-Medium 20')
        self.Morocco_label = tk.Label(self, text='Morocco', font='FuturaStd-Medium 20')
        self.Netherlands_label = tk.Label(self, text='Netherlands', font='FuturaStd-Medium 20')
        self.Nigeria_label = tk.Label(self, text='Nigeria', font='FuturaStd-Medium 20')
        self.Poland_label = tk.Label(self, text='Poland', font='FuturaStd-Medium 20')
        self.Portugal_label = tk.Label(self, text='Portugal', font='FuturaStd-Medium 20')
        self.Senegal_label = tk.Label(self, text='Senegal', font='FuturaStd-Medium 20')
        self.Serbia_label = tk.Label(self, text='Serbia', font='FuturaStd-Medium 20')
        self.Spain_label = tk.Label(self, text='Spain', font='FuturaStd-Medium 20')
        self.Sweden_label = tk.Label(self, text='Sweden', font='FuturaStd-Medium 20')
        self.Switzerland_label = tk.Label(self, text='Switzerland', font='FuturaStd-Medium 20')
        self.Ukraine_label = tk.Label(self, text='Ukraine', font='FuturaStd-Medium 20', pady=10)
        self.USA_label = tk.Label(self, text='USA', font='FuturaStd-Medium 20')
        self.Wales_label = tk.Label(self, text='Wales', font='FuturaStd-Medium 20')
        self.Japan_label = tk.Label(self, text='Japan', font='FuturaStd-Medium 20')
        self.Uruguay_label = tk.Label(self, text='Uruguay', font='FuturaStd-Medium 20')

        self.general_stats = tk.Button(self, text='General Stats', font='FuturaStd-Medium 25', command=self.go_to_general_stats)

        '''self.general_stats = tk.Button(self,text='General Statistics',font='FuturaStd-Medium 20', commmand=self.get_general_stats )'''

        self.place_widgets()

    def place_widgets(self):
        # This project_code creates the widgets and grids them
        '''self.background.grid()'''
        self.title.grid(columnspan=8, row=0, pady=10)

        self.Argentina_button.grid(column=0, row=1, padx=10)
        self.Australia_button.grid(column=1, row=1, padx=10)
        self.Austria_button.grid(column=2, row=1, padx=10)
        self.Belgium_button.grid(column=3, row=1, padx=10)
        self.Brazil_button.grid(column=4, row=1, padx=10)
        self.Colombia_button.grid(column=5, row=1, padx=10)
        self.Croatia_button.grid(column=6, row=1, padx=10)
        self.Denmark_button.grid(column=7, row=1, padx=10)

        self.Argentina_label.grid(column=0, row=2)
        self.Australia_label.grid(column=1, row=2)
        self.Austria_label.grid(column=2, row=2)
        self.Belgium_label.grid(column=3, row=2)
        self.Brazil_label.grid(column=4, row=2)
        self.Colombia_label.grid(column=5, row=2)
        self.Croatia_label.grid(column=6, row=2)
        self.Denmark_label.grid(column=7, row=2)

        self.England_button.grid(column=0, row=3, padx=10, )
        self.Equador_button.grid(column=1, row=3, padx=10, )
        self.France_button.grid(column=2, row=3, padx=10, )
        self.Germany_button.grid(column=3, row=3, padx=10, )
        self.Hungary_button.grid(column=4, row=3, padx=10, )
        self.Iran_button.grid(column=5, row=3, padx=10, )
        self.Italy_button.grid(column=6, row=3, padx=10, )
        self.Japan_button.grid(column=7, row=3, padx=10, )

        self.England_label.grid(column=0, row=4)
        self.Equador_label.grid(column=1, row=4)
        self.France_label.grid(column=2, row=4)
        self.Germany_label.grid(column=3, row=4)
        self.Hungary_label.grid(column=4, row=4)
        self.Iran_label.grid(column=5, row=4)
        self.Italy_label.grid(column=6, row=4)
        self.Japan_label.grid(column=7, row=4)

        self.Korea_button.grid(column=0, row=5, padx=10, )
        self.Mexico_button.grid(column=1, row=5, padx=10, )
        self.Morocco_button.grid(column=2, row=5, padx=10, )
        self.Netherlands_button.grid(column=3, row=5, padx=10, )
        self.Nigeria_button.grid(column=4, row=5, padx=10, )
        self.Poland_button.grid(column=5, row=5, padx=10, )
        self.Portugal_button.grid(column=6, row=5, padx=10, )
        self.Senegal_button.grid(column=7, row=5, padx=10, )

        self.Korea_label.grid(column=0, row=6)
        self.Mexico_label.grid(column=1, row=6)
        self.Morocco_label.grid(column=2, row=6)
        self.Netherlands_label.grid(column=3, row=6)
        self.Nigeria_label.grid(column=4, row=6)
        self.Poland_label.grid(column=5, row=6)
        self.Portugal_label.grid(column=6, row=6)
        self.Senegal_label.grid(column=7, row=6)

        self.Serbia_button.grid(column=0, row=7, padx=10, )
        self.Spain_button.grid(column=1, row=7, padx=10, )
        self.Sweden_button.grid(column=2, row=7, padx=10, )
        self.Switzerland_button.grid(column=3, row=7, padx=10, )
        self.USA_button.grid(column=4, row=7, padx=10, )
        self.Ukraine_button.grid(column=5, row=7, padx=10, )
        self.Uruguay_button.grid(column=6, row=7, padx=10, )
        self.Wales_button.grid(column=7, row=7, padx=10, )

        self.Serbia_label.grid(column=0, row=8)
        self.Spain_label.grid(column=1, row=8)
        self.Sweden_label.grid(column=2, row=8)
        self.Switzerland_label.grid(column=3, row=8)
        self.USA_label.grid(column=4, row=8)
        self.Ukraine_label.grid(column=5, row=8)
        self.Uruguay_label.grid(column=6, row=8)
        self.Wales_label.grid(column=7, row=8)

        self.general_stats.grid(columnspan=8,row=9)

    def go_to_next_page(self,country_name):
        a = Analyse()
        results = a.controller(country_name)

        self.destroy()
        self.gui = results_page.ResultGUI(country_name,results)
        self.gui.mainloop()

    def go_to_general_stats(self):
        g = SelectGUI()
        self.destroy()
        g.mainloop()



if __name__ == '__main__':
    root = SelectingCountriesPageGUI()
    root.mainloop()
