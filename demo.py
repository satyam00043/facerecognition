# Import required modules
import tkinter as tk
from tkinter import messagebox
import mysql.connector # type: ignore

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Other initialization code...

    def connect_to_database(self):
        try:
            # Establish connection to MySQL database
            self.conn = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="your_database_name"
            )
            # Create cursor to execute queries
            self.cursor = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to MySQL database successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to connect to MySQL database: {err}")

    def close_database_connection(self):
        try:
            # Close cursor and connection
            self.cursor.close()
            self.conn.close()
            messagebox.showinfo("Success", "MySQL database connection closed.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to close MySQL database connection: {err}")

if __name__ == "__main__":
    # Create the main tkinter window
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
