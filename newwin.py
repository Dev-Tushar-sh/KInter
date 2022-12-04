from tkinter import *
from PIL import ImageTk,Image


root=Tk()
root.title("main")

def openup():
    global my_img   #if image is not global then python garbage collector trash the 
                     # local variable of any function 
    top = Toplevel()
    top.title("top")
    my_img = ImageTk.PhotoImage(Image.open("ima/1.png"))
    lbl = Label(top,image=my_img).pack()

btn = Button(root,text="OpenUp",command=openup).pack()


root.mainloop() 