import tkinter as tk
from tkinter import messagebox

# -----------------------------
# To-Do List App with Tkinter
# -----------------------------

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = tasks[index] + " ✔️"
        tasks[index] = task
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to mark done!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# -----------------------------
# GUI Layout
# -----------------------------
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("350x400")
root.config(bg="#f2f2f2")

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333")
title_label.pack(pady=10)

# Entry Box
task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", width=12, bg="#4CAF50", fg="white", command=add_task)
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", width=12, bg="#2196F3", fg="white", command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=12, bg="#f44336", fg="white", command=delete_task)
delete_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Run App
root.mainloop()