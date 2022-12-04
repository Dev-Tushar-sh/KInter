from cProfile import label
from tkinter import *

root = Tk()
root.geometry("500x500")
clicked = StringVar()
option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "saturday",
    "Sunday"
       
]
clicked.set("Monday")
#drop = OptionMenu(root,clicked,"monday","Tuesday","Wednesday","Thursday","Friday","saturday")
drop = OptionMenu(root,clicked,*option)
drop.pack()
def show():
    lable = Label(root,text=clicked.get())
    lable.pack()
btn = Button(root,text="show Selection",command=show)
btn.pack()
root.mainloop()