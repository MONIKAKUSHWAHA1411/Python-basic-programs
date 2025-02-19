import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load credentials from Excel
def load_credentials():
    try:
        df = pd.read_excel("credentials.xlsx")  # Ensure the file is in the same directory
        return {row["Username"]: row["Password"] for _, row in df.iterrows()}
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load credentials: {e}")
        return {}

credentials = load_credentials()

def login():
    username = user_entry.get()
    password = pass_entry.get()
    
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username:").pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
pass_entry = tk.Entry(root, show="*")
pass_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()
