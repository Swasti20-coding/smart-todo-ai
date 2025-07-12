import tkinter as tk
from tkinter import messagebox
import json
import datetime
from suggest import suggest_task

TASK_FILE = "../data/tasks.json"

def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showwarning("Warning", "Enter a task!")
        return

    now = datetime.datetime.now()
    entry = {
        "task": task,
        "day": now.strftime("%A"),
        "time": get_time_slot(now.hour),
        "status": "done"
    }

    try:
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

    tasks.append(entry)
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    messagebox.showinfo("Success", f"Task '{task}' added!")
    task_entry.delete(0, tk.END)

def get_time_slot(hour):
    if 5 <= hour < 9:
        return "Morning"
    elif 9 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night"

def show_suggestion():
    task = suggest_task()
    suggestion_label.config(text=f"Suggested Task: {task}")

# GUI Setup
root = tk.Tk()
root.title("Smart Daily To-Do List")

tk.Label(root, text="Enter Task:").pack()
task_entry = tk.Entry(root, width=40)
task_entry.pack()

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Suggest Task", command=show_suggestion).pack(pady=5)

suggestion_label = tk.Label(root, text="Suggested Task: --", fg="green", font=("Arial", 12))
suggestion_label.pack(pady=10)

root.mainloop()
