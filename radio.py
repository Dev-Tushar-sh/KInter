from tkinter import *

root = Tk()
#r= IntVar()

pizz = StringVar()
def checked(pizz):
        my_lable = Label(root,text=pizz).pack()

Modes = [
    ("peperoni","peperoni"),
    ("cheese","cheese"),
    ("capsicium","capsicium"),
    ("onion","onion")
]
for i,j in Modes:
    Radiobutton(root, text=i,variable=pizz,value=j).pack(anchor=W)
    
#Radiobutton(root, text="option 1",variable=r , value=1,command=lambda: checked(r.get())).pack()
#Radiobutton(root, text="option 2",variable=r , value=2,command=lambda: checked(r.get())).pack()

#my_lable = Label(root,text=r.get()).pack()

b=Button(root,text="OK",command=lambda: checked(pizz.get())).pack()


root.mainloop()