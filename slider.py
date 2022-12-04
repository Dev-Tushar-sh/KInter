from tkinter import *

root = Tk()
def slidewala():
    lblv = Label(root,text=verticla.get()).pack()
    lblh = Label(root,text=hori.get()).pack()
    root.geometry(str(verticla.get())+"x"+str(hori.get()))

verticla = Scale(root,from_=0,to=1000)
verticla.pack()
hori = Scale(root,from_=0,to=1000,orient=HORIZONTAL)
hori.pack()
root.geometry("500x500")



btn = Button(root,text="update",command=slidewala).pack()


root.mainloop()