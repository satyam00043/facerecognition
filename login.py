# import tkinter as tk
# from tkinter import messagebox

# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     # Here you can add logic to validate the username and password
#     if username == "admin" and password == "password":
#         messagebox.showinfo("Login", "Login Successful!")
#     else:
#         messagebox.showerror("Login", "Invalid Username or Password")

# # Initialize the main window
# root = tk.Tk()
# root.title("Login Page")
# root.geometry("400x300")
# root.config(bg="#F0F0F0")

# # Title Label
# title_label = tk.Label(root, text="Login", font=('Helvetica', 18, 'bold'), bg="#F0F0F0", fg="#333333")
# title_label.pack(pady=20)

# # Username Label and Entry
# username_label = tk.Label(root, text="Username", font=('Helvetica', 12), bg="#F0F0F0", fg="#333333")
# username_label.pack(pady=5)
# username_entry = tk.Entry(root, font=('Helvetica', 12), width=30)
# username_entry.pack(pady=5)

# # Password Label and Entry
# password_label = tk.Label(root, text="Password", font=('Helvetica', 12), bg="#F0F0F0", fg="#333333")
# password_label.pack(pady=5)
# password_entry = tk.Entry(root, font=('Helvetica', 12), width=30, show='*')
# password_entry.pack(pady=5)

# # Login Button
# login_button = tk.Button(root, text="Login", font=('Helvetica', 12, 'bold'), bg="#4CAF50", fg="white", command=login)
# login_button.pack(pady=20)

# # Run the application
# root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import datetime
import time
import mysql.connector

# Dummy Face Recognition System for the sake of this example
class Face_recognition_system:
    pass

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1520x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=520, y=200, width=450, height=500)

        get_str = Label(frame, text="Get Started", font=("times new roman", 30, "bold"), fg="white", bg="black")
        get_str.place(x=120, y=80)

        user_str = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        user_str.place(x=70, y=155)

        self.txtuser = StringVar()
        self.txtpass = StringVar()
        txtuser = ttk.Entry(frame, textvariable=self.txtuser, font=("times new roman", 15, "bold"))
        txtuser.place(x=70, y=190, width=300)

        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=235)
        txtpass = ttk.Entry(frame, textvariable=self.txtpass, font=("times new roman", 15, "bold"), show='*')
        txtpass.place(x=70, y=270, width=300)

        btn_login = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        btn_login.place(x=150, y=320, width=150, height=35)

        btn_register = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 12, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        btn_register.place(x=70, y=370, width=160)

        btn_forgot = Button(frame, text="Forgot Password?", command=self.forgot_password_window, font=("times new roman", 12, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        btn_forgot.place(x=240, y=370, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
            messagebox.showinfo("Success", "Welcome")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def forgot_password_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Forgot_Password(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x400+450+150")

        label = Label(self.root, text="Registration Form", font=("times new roman", 20, "bold"))
        label.pack(pady=20)

        username_label = Label(self.root, text="Username", font=("times new roman", 15))
        username_label.pack(pady=5)
        self.username_entry = Entry(self.root, font=("times new roman", 15))
        self.username_entry.pack(pady=5)

        password_label = Label(self.root, text="Password", font=("times new roman", 15))
        password_label.pack(pady=5)
        self.password_entry = Entry(self.root, font=("times new roman", 15), show='*')
        self.password_entry.pack(pady=5)

        confirm_password_label = Label(self.root, text="Confirm Password", font=("times new roman", 15))
        confirm_password_label.pack(pady=5)
        self.confirm_password_entry = Entry(self.root, font=("times new roman", 15), show='*')
        self.confirm_password_entry.pack(pady=5)

        register_btn = Button(self.root, text="Register", command=self.register, font=("times new roman", 15, "bold"), bg="green", fg="white")
        register_btn.pack(pady=20)

    def register(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "" or self.confirm_password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Passwords do not match")
        else:
            messagebox.showinfo("Success", "Registration Successful")

class Forgot_Password:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("400x300+450+150")

        label = Label(self.root, text="Forgot Password", font=("times new roman", 20, "bold"))
        label.pack(pady=20)

        username_label = Label(self.root, text="Username", font=("times new roman", 15))
        username_label.pack(pady=5)
        self.username_entry = Entry(self.root, font=("times new roman", 15))
        self.username_entry.pack(pady=5)

        reset_btn = Button(self.root, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        reset_btn.pack(pady=20)

    def reset_password(self):
        if self.username_entry.get() == "":
            messagebox.showerror("Error", "Please enter your username")
        else:
            messagebox.showinfo("Success", "Password reset instructions sent to your email")

if __name__ == "__main__":
    main()

