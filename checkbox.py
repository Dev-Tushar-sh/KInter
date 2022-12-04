from tkinter import *
from turtle import onclick

root = Tk()
root.geometry("500x500")

var = StringVar()
def show():
    my_lable = Label(root,text=var.get()).pack()
c= Checkbutton(root,text="check this !!",variable=var,onvalue="ON",offvalue="Off")
c.deselect()
c.pack()
b=Button(root,text="Update",command=show).pack()

root.mainloop()