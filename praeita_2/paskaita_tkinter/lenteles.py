from tkinter import *

main_window = Tk(className="My Program")

main_window.geometry("500x500")

# label1 = Label(main_window, text="Hello this is my gui")
# label1.place()

# label2 = Label(main_window, text="Hello this is my gui")
# label2.pack()

# label3 = Label(main_window, text="Hello this is my gui")
# label3.pack()

# header = Frame(main_window)
# header.pack()

# button1 = Button(header, text="press me",bg="blue")
# button1.pack(fill="both")

# footer = Frame(main_window)
# footer.pack(side=BOTTOM,fill="both")

# button2 = Button(footer, text="press me")
# button2.pack(side=LEFT,fill="both")

# button3 = Button(footer, text="press me")
# button3.pack()

# button1 = Button(main_window, text="press me",bg="red")
# button1.pack(fill="both")



label1 = Label(main_window, text="Please enter your name")
input_field = Entry(main_window)

label2 = Label(main_window, text="Please enter your name")
input_field2 = Entry(main_window)

submit_button = Button(main_window,text="submit")

label1.grid(row=0, column=0)
input_field.grid(row=1,column=0)

label2.grid(row=0, column=1)
input_field2.grid(row=1,column=1)

submit_button.grid(row=2,columnspan=2)

main_window.mainloop()