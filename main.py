from tkinter import *
import tkinter.messagebox as message
import mysql.connector as mysql

def insert():
  id=id_entry.get()
  name=name_entry.get()
  phone=phone_entry.get()
  age=age_entry.get()
  
  if(id=="" or name=="" or phone=="" or age==""):
    message.showinfo("ALERT", "please enter all fields")
  else:
    con=mysql.connect(host="localhost", user="root", password="", database="crud")
    cursor=con.cursor()
    cursor.execute("insert into person values('" + id +"', '" + name +"', '" + phone +"', '"+ age +"')")
    cursor.execute("commit")
    id_entry.delete(0,"end")
    name_entry.delete(0,"end")
    phone_entry.delete(0,"end")
    age_entry.delete(0,"end")
    
    message.showinfo("status","successfully inserted")
    con.close();
    
def Retrieve():
      if (id_entry.get()== ""):
        message.showinfo("Alert","Id is required to retrieve a row in your table")
      else:
        con=mysql.connect(host="localhost", user="root", password="", database="crud")
        cursor=con.cursor()
        cursor.execute(" select * from person where id='" + id_entry.get() + "'")
        rows=cursor.fetchall()
        for row in rows:
          name_entry.insert(0,row[1])
          phone_entry.insert(0,row[2])
          age_entry.insert(0,row[3])
        con.close();
def update():
  id=id_entry.get()
  name=name_entry.get()
  phone=phone_entry.get()
  age=age_entry.get()
  if (name ==" " or phone ==" " or age==" "):
    message.showinfo("Alert","please enter field you want to update")
  else:
    con=mysql.connect(host="localhost", user="root", password="", database="crud")
    cursor=con.cursor()
    cursor.execute("update person set name='" + name + "', phone='" + phone + "', age='" + age + "' where id='" + id + "'")
    cursor.execute("commit");
    message.showinfo("Status","Successfully Updated")
    con.close();
def Del():
  if (id_entry.get()==""):
    message.show("alert", "Id is requird to delete row form table")
  else:
    con=mysql.connect(host="localhost", user="root", password="", database="crud")
    cursor=con.cursor()
    cursor.execute("delete from person where id='" + id_entry.get() + "'")
    cursor.execute("commit");
    id_entry.delete(0,"end")
    name_entry.delete(0,"end")
    phone_entry.delete(0,"end")
    age_entry.delete(0,"end")
    
    message.showinfo("Status", "Successfully Deleted")
    
    con.close();
    
    
    
          
    
root=Tk()
root.geometry("500x500")
root.title("CRUD APPLICATION ")
root.configure(bg="pink")
id=Label(root, text="Enter Id", font="verdana 14")
id.place(x=50, y=30)
id_entry=Entry(root, font="verdan 14")
id_entry.place(x=150, y=30)

name=Label(root, text="Enter name", font="verdana 14")
name.place(x=50, y=80)
name_entry=Entry(root, font="verdan 14")
name_entry.place(x=180, y=80)

phone=Label(root, text="Enter phone", font="verdana 14")
phone.place(x=50, y=130)
phone_entry=Entry(root, font="verdan 14")
phone_entry.place(x=180, y=130)

age=Label(root, text="Enter age", font="verdana 14")
age.place(x=50, y=180)
age_entry=Entry(root, font="verdan 14")
age_entry.place(x=150, y=180)

btninsert=Button(root,text="Create", command=insert, font="verdana 14")
btninsert.place(x=100, y=230)
btnRetrieve=Button(root, text="Retrieve", command=Retrieve, font="verdana 14")
btnRetrieve.place(x=190, y=230)
btnUpdate=Button(root, text="Update", command=update, font="verdana 14")
btnUpdate.place(x=300, y=230)
btndel=Button(root,text="Delete", command=Del, font="verdana 14")
btndel.place(x=400,y=230)
  
     
root.mainloop()