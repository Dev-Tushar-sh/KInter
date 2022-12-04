from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.geometry("500x500")
root.title("Tushar")
#root.iconbitmap('path') you can add a .ico file path for icon image

my_img = ImageTk.PhotoImage(Image.open("ima/1.png"))
my_lable = Label(image = my_img)
my_lable.pack()

root.mainloop()