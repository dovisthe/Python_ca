from tkinter import *

main_window = Tk(className="Uzduotis1")
main_window.geometry("260x65")

last_text = StringVar()

def sveikinam(event=None):
    name = field.get()
    last_text.set(name)
    greeting_label.config(text=f"Labas, {name}!")
    sukurta()

def clear_text():  
    field.delete(0, END)
    greeting_label.config(text="")
    status.config(text="Ištrinta")

def restore_text():
    field.delete(0, END)
    field.insert(0, last_text.get())
    greeting_label.config(text=f'Labas, {last_text.get()}!')
    status.config(text="Atkurta")

def sukurta():
    status.config(text="Sukurta")

def iseiti(event=None):
    main_window.quit()

main_window.bind("<Escape>", iseiti)

status = Label(main_window, text="", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=2, columnspan=3, sticky=W+E)

label = Label(main_window, text="iveskite varda")
label.grid(row=0, column=0)

field = Entry(main_window)
field.grid(row=0, column=1)
field.bind("<Return>", sveikinam)

greeting_label = Label(main_window, text="")
greeting_label.grid(row=1, columnspan=3)

knopke = Button(main_window, text="Patvirtinti", command=sveikinam)
knopke.grid(row=0, column=2)

# MENIU------------------------------
meniu = Menu(main_window)
main_window.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=clear_text)
submeniu.add_command(label="Atkurti paskutini", command=restore_text)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

main_window.mainloop()