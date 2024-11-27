import tkinter as tk
from tkinter import messagebox
import json

# Sample task list
tasks = []

# Load tasks from a file
def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Save tasks to a file
def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

# Add a new task to the list
def add_task_gui():
    task_name = task_entry.get()
    if task_name:
        tasks.append({'task': task_name, 'completed': False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

# Delete the selected task from the list
def delete_task_gui():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark the selected task as completed
def mark_task_completed_gui():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Update the task list in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = 'Completed' if task['completed'] else 'Pending'
        task_listbox.insert(tk.END, f"{task['task']} - {status}")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Load tasks from the file at the start
load_tasks()

# Task entry widget
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", width=15, command=add_task_gui)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Task listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Buttons for actions
mark_button = tk.Button(root, text="Mark as Completed", width=20, command=mark_task_completed_gui)
mark_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task_gui)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Save tasks before exiting
def on_closing():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Initial update of the task list
update_task_list()

# Start the Tkinter event loop
root.mainloop()
