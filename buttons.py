from itertools import tee
from tkinter import *
root = Tk()
root.geometry("500x500")
def button4():
    mylable = Label(root,text="button clicked")
    mylable.grid(row=5,column=0)

my_button = Button(root,text="Click Me")
my_button2 = Button(root,text="Click Me",state=DISABLED)
my_button3 = Button(root,text="Click Me",padx=50)
my_button4 = Button(root,text="Click Me",padx=50,pady=50,command=button4,fg="white",bg="black")

my_button.grid(row=0,column=0)
my_button2.grid(row=1,column=1)
my_button3.grid(row=2,column=2)
my_button4.grid(row=3,column=3)

root.mainloop()