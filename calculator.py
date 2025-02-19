import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("410x395")
root.configure(bg="#282C34")

entry_var = tk.StringVar()

# Function to evaluate expression safely
def evaluate_expression():
    try:
        expression = entry_var.get().strip()
        if not expression:
            return
        # Validate expression using regex (prevents multiple consecutive operators)
        if re.search(r"[+\-*/.]{2,}", expression) or expression[-1] in "+-*/.":
            messagebox.showerror("Error", "Invalid Expression!")
            return
        entry_var.set(str(eval(expression)))  # Show result in the entry field
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        entry_var.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid Input!")
        entry_var.set("")

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        evaluate_expression()
    elif text == "C":
        entry_var.set("")
    elif text == "←":  # Backspace functionality
        entry_var.set(entry_var.get()[:-1])
    else:
        entry_var.set(entry_var.get() + text)

# Function to handle keyboard input (Fixing Duplicate Input)
def key_press(event):
    key = event.char
    if key in "0123456789+-*/.":
        current_text = entry_var.get()
        # Append only if last character is not the same operator
        if not (len(current_text) > 0 and current_text[-1] in "+-*/." and key in "+-*/."):
            entry_var.set(current_text + key)
    elif key == "\r":  # Enter key for "="
        evaluate_expression()
    elif key == "\x08":  # Backspace key
        entry_var.set(entry_var.get()[:-1])
    return "break"  # Prevents Tkinter from inserting keypress into entry

# Entry field for input/output
entry = tk.Entry(root, textvariable=entry_var, font="Arial 20 bold", justify="right", bd=10, relief=tk.FLAT)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)
entry.bind("<Key>", key_press)

# Buttons layout
buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "←", "+", 
    "."
]

# Button colors
button_bg = "#454545"
button_fg = "black"
button_active = "#0000FF"

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 18 bold", width=5, height=2, bg=button_bg, fg=button_fg,
                    activebackground=button_active, relief=tk.RAISED)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Adjust "=" button to span two columns
equals_button = tk.Button(root, text="=", font="Arial 18 bold", width=11, height=2, bg="#98C379", fg="black",
                          activebackground="#FF0000", relief=tk.RAISED)
equals_button.grid(row=row, column=2, columnspan=2, padx=5, pady=5)
equals_button.bind("<Button-1>", click)

root.mainloop()
