import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("1400x1500")
root.resizable(False, False)

# Widgets
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add", command=add_task)
add_button.pack(side=tk.RIGHT)

task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.RIGHT, padx=10)

# Run the app
root.mainloop()
