import tkinter as tk 
from databases import *
import mysql.connector
import tkinter.messagebox as message
def initializer_connection():
  con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
  )
  cursor=con.cursor()
  create_database(cursor)
  create_table(cursor)
  
  return con, cursor
def create_database(cursor):
  cursor.execute("show databases")
  temp=cursor.fetchall()
  databases= [item[0] for item in temp]
  
  if "login" not in databases:
    cursor.execute("CREATE DATABASE login")
    cursor.execute("USE login")
def create_table(cursor):
  cursor.execute("show tables")
  temp=cursor.fetchall()
  tables=[item[0] for item in temp]
  
  if "users" not in tables:
    cursor.execute("""CREATE TABLE users(
      id INT AUTO_INCREMENT PRIMARY KEY,
      firstName VARCHAR(100),
      lastName VARCHAR(100),
      password VARCHAR(30),
      email VARCHAR(100) UNIQUE,
      gender VARCHAR(1),
      age INT,
      address VARCHAR(200)
      )""")
def login(cursor, data):
  cursor.execute(f""" SELECT * FROM users WHERE email='{data['email']}' 
                 AND password='{data['password']}'""")
  if cursor.fetchone() != None:
    return True
  return False

def register(cursor, con, data):
  print(data)
  cursor.execute(f""" INSERT INTO users values(
    NULL,
    '{data["firstName"]}',
    '{data["lastName"]}',
    '{data["password"]}',
    '{data["email"]}',
    '{data["gender"]}',
    '{data["age"]}',
    '{data["address"]}'
  )""")
  con.commit()
  
con, cursor=initializer_connection()
def center_window(width, height):
  x=(root.winfo_screenwidth()//2)-(width//2)
  y=(root.winfo_screenheight()//2)-(height//2)
  root.geometry(f'{width}x{height}+{x}+{y}')
  
class WelcomeWindow(tk.Frame):
  def __init__(self, master):
    super().__init__()
    self.master=master
    self.master.title("Welcome to my login system")
    center_window(240,120)
    
    login_button=tk.Button(self, text="Login", width=10, command=self.open_login_window)
    login_button.pack(padx=20, pady=(20,10))
    
    register_button=tk.Button(self, text="Register", width=10, command=self.open_register_window)
    register_button.pack(pady=10)
    self.pack() 
  def open_login_window(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.destroy()
    LoginWindow(self.master)
  
  def open_register_window(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.destroy()
    RegisterWindow(self.master)

class LoginWindow(tk.Frame):
  def __init__(self, master):
    super().__init__()
    self.master=master
    self.master.title("Login")
    # self.master.resizable(False,Fuialse)
    center_window(240,150)
    tk.Label(self, text="UserName").grid(row=0, column=0)
    self.username_entry=tk.Entry(self)
    self.username_entry.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(self, text="Password").grid(row=1, column=0)
    self.password_entry=tk.Entry(self, show="*")
    self.password_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # tk.Label(self, text="UserName").grid(row=0, column=0)
    submit_button=tk.Button(self, text="Submit", width=8, command=self.submit)
    submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=10)
    
    back_button=tk.Button(self, text="Back", width=8, command=self.back)
    back_button.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    
    self.pack()
    
    # function for submit
  def submit(self):
    data={}
    data["email"]=self.username_entry.get()
    data["password"]=self.password_entry.get()
    
    if login(cursor,data)==True:
      print("successfully login")
      for widget in self.winfo_children():
        widget.destroy()
      self.destroy()
      mainWindow(self.master)
    else:
      print("unAuthorize user")
  def back(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.destroy()
    WelcomeWindow(self.master)
    
class RegisterWindow(tk.Frame):
  def __init__(self, master):
    super().__init__()
    self.master=master
    self.master.title("Registration")
    # self.master.resizable(False, False)
    center_window(320, 350)
    
    # Registration Widget
    tk.Label(self, text="FirstName").grid(row=0, column=0, sticky="w")
    self.first_name_entry=tk.Entry(self, width=26)
    self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="LastName").grid(row=1, column=0, sticky="w")
    self.last_name_entry=tk.Entry(self, width=26)
    self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="Password").grid(row=2, column=0, sticky="w")
    self.password_entry=tk.Entry(self, width=26, show="*")
    self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="Email").grid(row=3, column=0, sticky="w")
    self.email_entry=tk.Entry(self, width=26)
    self.email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="Gender").grid(row=4, column=0, sticky="w")
    self.gender_entry=tk.Entry(self, width=10)
    self.gender_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="Age").grid(row=5, column=0, sticky="w")
    self.age_entry=tk.Entry(self, width=10)
    self.age_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")
    
    tk.Label(self, text="Address").grid(row=6, column=0, sticky="w")
    self.address_entry=tk.Entry(self, width=26)
    self.address_entry.grid(row=6, column=1, padx=10, pady=10, sticky="e")
    
    submit_button=tk.Button(self, text="Submit", width=8, command=self.submit)
    submit_button.grid(row=7, column=1, sticky="e", padx=10, pady=10)
    
    back_button=tk.Button(self, text="Back", width=8, command=self.back)
    back_button.grid(row=7, column=0, sticky="w", padx=10, pady=(10,10))
    
    self.pack()
    
  def submit(self):
    data={}
    firstName=self.first_name_entry.get()
    lastName=self.last_name_entry.get()
    password=self.password_entry.get()
    email=self.email_entry.get()
    gender=self.gender_entry.get()
    age=self.age_entry.get()
    address=self.address_entry.get()
    if (firstName=="" and lastName=="" and password=="" and email=="" and age=="" and address==""):
      message.showinfo("alert", " Please fill the form")
    else:
      data["firstName"]=self.first_name_entry.get()
      data["lastName"]=self.last_name_entry.get()
      data["password"]=self.password_entry.get()
      data["email"]=self.email_entry.get()
      data["gender"]=self.gender_entry.get()
      data["age"]=self.age_entry.get()
      data["address"]=self.address_entry.get()
    
    
      register(cursor, con, data)
      
  def back(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.destroy()
    WelcomeWindow(self.master)
class mainWindow(tk.Frame):
  def __init__(self,master):
    super().__init__()
    self.master=master
    center_window(600,400)
    self.pack()
  
       
root=tk.Tk()
# root.geometry("500x500")
root.configure(bg="pink")
# root.title("Login system")
# root.eval('tk::PlaceWindow.center')
WelcomeWindow(root)
root.mainloop()