from cgi import test
from tkinter import *
root = Tk()

root.title('frames')

my_frame = LabelFrame(root,text="this is my Frame",padx=50,pady=50)#padding for inside
my_frame.pack(padx=10,pady=10)#padding for outside

b=Button(my_frame,text="Button")
b.grid(row=0,column=0)
b2 = Button(my_frame,text="Button2")
b2.grid(row=1,column=1)

root.mainloop()