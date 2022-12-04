from cProfile import label
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
root = Tk()


def openfile():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="Study",
                     title="select a file",filetypes=(("png files","*.png"),
                                                  ("all files","*.*")))
    my_lable = Label(root,text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_Image_lable = Label(root,text="Hi",image=my_img).pack()

my_btn = Button(root,text="open file",command=openfile).pack()
root.mainloop()