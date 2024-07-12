import imp
import re
from tkinter import *

from sqlalchemy import CacheKey

# langas = Tk()

# def spausdink():
#     pasirinkta = sarasas[boksas.curselection()[0]]
#     uzrasas["text"] = pasirinkta
    

# scroll = Scrollbar(langas)
# boksas = Listbox(langas, yscrollcommand=scroll.set, selectmode=SINGLE)
# scroll.config(command=boksas.yview)
# mygtukas = Button(langas, text="Spausdink", command=spausdink)
# uzrasas = Label(langas, text="")

# sarasas = range(1, 200)

# boksas.insert(END, *sarasas)
# scroll.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)

# mygtukas.pack()
# uzrasas.pack()

# langas.mainloop()

#==============================================



# langas = Tk()


# def spausdink():
#     uzrasas["text"] = "Atspausdinau"


# meniu = Menu(langas)

# langas.config(menu=meniu)

# submenu = Menu(meniu, tearoff=0)

# uzrasas = Label(langas, text="")


# meniu.add_cascade(label="Submeniu", menu=submenu)
# submenu.add_command(label="Pirmas")
# submenu.add_command(label="Antras", command=spausdink)
# submenu.add_command(label="Trecias")
# uzrasas.pack()

# langas.mainloop()

# STATUS========================================================

import webbrowser

lengas = Tk()

def callback(link):
    webbrowser.open_new(link)

def spausdink():
    status["text"] = "Darau"

status = Label(lengas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)

nuoroda = Label(lengas, text="Google", fg="blue", cursor="hand2")

mygtukas = Button(lengas, text="Spausdink", command=spausdink)

mygtukas.pack()
nuoroda.pack()

status.pack(side=BOTTOM, fill=X)

nuoroda.bind("<Button-1>", lambda e: callback("google.com"))


lengas.mainloop()

#Nuotraukos===============================

# from PIL import Image, ImageTk
# import os

# langas = Tk()

# photo = ImageTk.PhotoImage(Image.open("paskaita_tkinter/Untitled.png"))

# blokas = Label(langas, image=photo)

# blokas.pack(side=BOTTOM, fill=BOTH, expand=True)


# langas= mainloop()