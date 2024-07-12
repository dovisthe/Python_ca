import tkinter as tk

def print_name():
    name = e1.get()
    name2 = e2.get()
    print(name)
    print(name2)

master = tk.Tk()
tk.Label(master, text='First Name').grid(row=0, column=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
tk.Label(master, text='Last Name').grid(row=1, column=0)
e2 = tk.Entry(master)
e2.grid(row=1, column=1)

tk.Button(master, text='Print', command=print_name).grid(row=2, column=0, columnspan=2)

tk.mainloop()

