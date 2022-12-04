from gzip import _PaddedFile
from tkinter import *

root = Tk()

root.title("Calculator")
e = Entry(root,width=25,borderwidth=10,font=('Arial',20))
e.grid(row=0,column=0,columnspan=5,padx=20,pady=20)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add():
    first_number = e.get()
    global f_num 
    global fun 
    fun='add'
    f_num = int(first_number)
    e.delete(0,END)

def sub():
    first_number = e.get()
    e.delete(0,END)
    global fun
    global f_num
    fun='sub'
    f_num = int(first_number)
    e.delete(0,END)

def mul():
    first_number = e.get()
    e.delete(0,END)
    global fun
    global f_num
    fun='mul'
    f_num = int(first_number)
    e.delete(0,END)

def div():
    first_number = e.get()
    e.delete(0,END)
    global fun
    global f_num
    fun='div'
    f_num = int(first_number)
    e.delete(0,END)

def sq():
    x=int(e.get())
    e.delete(0,END)
    x=x*x
    e.insert(0,x)

def equal():
    global f_num
    x= f_num
    if(fun == 'add'):
        x = x + int(e.get())
        e.delete(0,END)
        e.insert(0,x)
    if(fun=='sub'):
        x = x - int(e.get())
        e.delete(0,END)
        e.insert(0,x)   
    if(fun == 'mul'):
        x = x * int(e.get())
        e.delete(0,END)
        e.insert(0,x)
    if(fun=='div'):
        y = float(x / int(e.get()))
        e.delete(0,END)
        e.insert(0,y)



button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))

button_square = Button(root,text="SQ",padx=40,pady=20,command=sq)
button_clear = Button(root,text="CLR",padx=85,pady=20,command=lambda:e.delete(0,END))
button_equal = Button(root,text="=",padx=40,pady=20,command=equal)
button_add = Button(root,text="+",padx=39,pady=20,command=add)
button_sub = Button(root,text="-",padx=40,pady=20,command=sub)
button_div = Button(root,text="/",padx=40,pady=20,command=div)
button_mul = Button(root,text="X",padx=40,pady=20,command=mul)


button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)

button_square.grid(row=1,column=3)
button_clear.grid(row=5,column=0,columnspan=2)
button_equal.grid(row=5,column=3)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_mul.grid(row=4,column=3)
button_div.grid(row=5,column=2,columnspan=1)

root.mainloop()