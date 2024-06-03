from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import datetime
import time
import mysql.connector
from main2 import Face_recognition_system
import bcrypt


def main():
    win=Tk()
    app=Login_Windows(win)
    win.mainloop()

class Login_Windows:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")

        frame=Frame(self.root,bg="black")
        frame.place(x=200,y=200,width=350,height=400)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white")
        get_str.place(x=90,y=80)

        User_str=Label(frame,text="User_Name",font=("times new roman",20,"bold"),fg="white")
        get_str.place(x=70,y=125)

        self.txtuser=StringVar()
        self.txtpass=StringVar()
        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",20,"bold"))
        txtuser.place(x=40,y=150,width=250)
        password=Label(frame,text="password",font=("times new roman",20,"bold"))
        password.place(x=70,y=195)
        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",20,"bold"))

        btn_login=Button(frame,text="Login",font=("times new roman",20,"bold"))
        btn_login.place(x=110,y=270,width=100)
    

    
def authenticate(username, password):
    # Connect to MySQL database
    try:
        connection=mysql.connector.connect(host="localhost",username="root",password="satyam",database="facerecognition")
        #my_cursor=conn.cursor()
        

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            # Authentication successful, show profile
            profile = user['profile']
            messagebox.showinfo("Login Successful", f"Welcome {username}!\nYour profile: {profile}")
        else:
            # Authentication failed
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    def login():
        username = txtuser.get()
        password = password.get()
        authenticate(username, password)






