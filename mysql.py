from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone()
    if(id == "" or name ="" or phone == ""):
        MessageBox.showinfo("insert","all fields are required")
    else:
        con = mysql.connect(host ="localhost",user="root",password="abhi123",database="Information")
        c = con.cursor()
        c.execute("insert into information values('" + id + "',"','"+ name +"','"+ phone +"')")
        c.execute("commit")
        MessageBox.showinfo("Insert Status","Data inserted successfully")
        con.close
