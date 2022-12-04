from cProfile import label
from tkinter import *
wintab = Tk()

wintab.geometry("600x500")
wintab.minsize(300,250)
wintab.maxsize(500,400)

rootlabel = Label(wintab,text="Hi my name is Tushar sharma").grid(row=0,column=0)
#rootlabel.pack()#or we can use rooelabel.grid(row=0,column=0) it place the label 
               # in defined row and column instead of the center of window
#since python is object oriented we use them as class member
#rootlabe2 = Label(wintab,text="Hi my name is Tushar sharma").grid(row=1,column=1)
wintab.mainloop()