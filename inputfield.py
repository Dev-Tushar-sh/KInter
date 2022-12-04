from tkinter import *
root = Tk()

e= Entry(root)
e.insert(0,"Enter your name")
e.pack()

def button4():
    mylable = Label(root,text=e.get())
    mylable.pack()

my_button = Button(root,text="Name Entered",command=button4)
my_button.pack()


root.mainloop()