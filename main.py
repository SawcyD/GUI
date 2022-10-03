from tkinter import *

# Create root window

root = Tk()


root.title("Application")

root.geometry('350x200')


menu = Menu(root)
item = Menu(menu)
item.add_command(label = 'New')
menu.add_cascade(label = 'File', menu = item)
root.config(menu=menu)






lbl = Label(root, text = "Are you a Geek?")

lbl.grid()


txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "You Wrote " + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Click me",
            fg = "red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()