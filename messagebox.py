from tkinter import *
from tkinter import messagebox
root=Tk()
#showinfo showwarning showerror askquestion askokcancle askyesno
def popup():
    respose = messagebox.askquestion("This is a Popup!!","Hello World!")
    lable = Label(root,text=respose).pack()


b = Button(root,text="To popup",command=popup).pack()
 
root.mainloop()