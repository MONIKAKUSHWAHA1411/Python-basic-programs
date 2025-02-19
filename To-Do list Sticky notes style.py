import tkinter as tk
from tkinter import messagebox

# List of colors for tasks
TASK_COLORS = ["#FFEB3B", "#FFCDD2", "#C8E6C9", "#BBDEFB", "#FFE0B2"]

def add_task():
    task = task_entry.get()
    if task:
        color_index = listbox.size() % len(TASK_COLORS)  # Cycle through colors
        listbox.insert(tk.END, task)
        listbox.itemconfig(tk.END, {'bg': TASK_COLORS[color_index]})
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#00FFFF")  # Light yellow background like sticky notes

task_entry = tk.Entry(root, width=40, font=("Arial", 12), bg="#FFFDE7")
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#64B5F6", fg="black", font=("Arial", 12, "bold"))
add_button.pack()

listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12), bg="#FFF9C4", selectbackground="black")
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#E57373", fg="black", font=("Arial", 12, "bold"))
remove_button.pack()

root.mainloop()
