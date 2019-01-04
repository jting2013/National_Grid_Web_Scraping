from tkinter import *
from tkinter import filedialog
import tkinter as ttk
from nation_grid_electric import National_Electric 
from nation_grid_gas import National_Gas 

root = Tk()
root.title("Get Utilities Bill")
root.geometry("400x400")

v = ttk.IntVar()

label1=Label(text="a",justify="center")
label1.pack()


nameLabel = Label(root, text="Name")
ent = Entry(root, bd=5)

def getName():
    print(ent.get())

submit = Button(root, text ="Submit", command = getName)


nameLabel.pack()
ent.pack()

submit.pack(side = BOTTOM)

def selectiondisplay():
    selection = "You selected the option " + str(v.get())
    label1.config(text = selection)
    if str(v.get()) == "1":
        eb = National_Electric()
    else:
        eb = National_Gas()

    eb.run()
        

def close_window (): 
    root.destroy()
    
radio1 = ttk.Radiobutton(root, 
              text="Electric",
              padx = 20, 
              variable=v, 
              value=1,command=selectiondisplay).pack(anchor=ttk.W)
radio2 = ttk.Radiobutton(root, 
              text="Gas",
              padx = 20, 
              variable=v, 
              value=2, command=selectiondisplay).pack(anchor=ttk.W)

button = Button (root, text = "Good-bye", command = close_window)
button.pack()
root.mainloop()
