import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt

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
    username = entry_username.get()
    password = entry_password.get()
    authenticate(username, password)

# Create the main window
root = tk.Tk()
root.title("Login")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
