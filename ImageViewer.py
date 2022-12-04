from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.title("Photos")
#root.iconbitmap('path') you can add a .ico file path for icon image
def back(image_number):
    global my_lable
    global button_back
    global button_forward
    my_lable.grid_forget()
    my_lable = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",padx=25,pady=5,command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",padx=25,pady=5,command=lambda: back(image_number-1))
    
    if(image_number==1):
        button_back = Button(root,text="<<",state=DISABLED)


    my_lable.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)    
    

def forward(image_number):
    global my_lable
    global button_back
    global button_forward    
    my_lable.grid_forget()
    my_lable = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",padx=25,pady=5,command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",padx=25,pady=5,command=lambda: back(image_number-1))
    
    if(image_number==3):
        button_forward = Button(root,text=">>",state=DISABLED)

    my_lable.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)


my_img1 = ImageTk.PhotoImage(Image.open("ima/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("ima/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("ima/3.png"))

image_list = [my_img1,my_img2,my_img3]

my_lable = Label(image=my_img1)
my_lable.grid(row=0,column=0,columnspan=3)

button_back = Button(root,text="<<",padx=25,pady=5,command=back,state=DISABLED)
button_exit = Button(root,text="EXIT",padx=40,pady=5,command=root.quit)
button_forward = Button(root,text=">>",padx=25,pady=5,command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()