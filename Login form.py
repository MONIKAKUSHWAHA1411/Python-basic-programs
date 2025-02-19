import tkinter as tk
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()
    
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome Admin!")
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
