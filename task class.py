import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

class Task:
    def __init__(self, description, due_date=None, priority="Normal", category="General", completed=False):
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.priority = priority
        self.category = category

    def __str__(self):
        status = "✓" if self.completed else "✗"
        due_date_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"[{status}] {self.description} | Due: {due_date_str} | Priority: {self.priority} | Category: {self.category}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority="Normal", category="General"):
        task = Task(description, due_date, priority, category)
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{'description': task.description, 'due_date': task.due_date.strftime("%Y-%m-%d") if task.due_date else None, 'priority': task.priority, 'category': task.category, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(data['description'], datetime.strptime(data['due_date'], "%Y-%m-%d") if data['due_date'] else None, data['priority'], data['category'], data['completed']) for data in tasks_data]
        except FileNotFoundError:
            print("No saved tasks found.")

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = ToDoList()
        self.filename = "tasks.json"
        self.todo_list.load_tasks(self.filename)

        self.setup_ui()

    def setup_ui(self):
        self.header_frame = tk.Frame(self.root, bg='#3b3b3b')
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.header_frame, text="ALL TASK", bg='#3b3b3b', fg='white', font=('Helvetica', 16, 'bold'))
        self.title_label.pack(pady=10)

        self.input_frame = tk.Frame(self.root, bg='#3b3b3b')
        self.input_frame.pack(fill=tk.X, pady=5)

        self.entry_task = tk.Entry(self.input_frame, width=40)
        self.entry_task.pack(side=tk.LEFT, padx=10, pady=10)

        self.add_button = tk.Button(self.input_frame, text="ADD", command=self.add_task, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.tasks_frame = tk.Frame(self.root, bg='#3b3b3b')
        self.tasks_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.task_listbox = tk.Listbox(self.tasks_frame, height=15, bg='#2b2b2b', fg='white', selectbackground='#4CAF50', font=('Helvetica', 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.load_tasks()

        self.footer_frame = tk.Frame(self.root, bg='#3b3b3b')
        self.footer_frame.pack(fill=tk.X, pady=10)

        self.delete_button = tk.Button(self.footer_frame, text="DELETE", command=self.delete_task, bg='#f44336', fg='white', font=('Helvetica', 10, 'bold'))
        self.delete_button.pack(pady=5)

        # Bind the window close event to save tasks
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        description = self.entry_task.get().strip()

        if description:
            self.todo_list.add_task(description)
            self.entry_task.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            self.task_listbox.insert(tk.END, task.description)

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.todo_list.delete_task(selected_task_index)
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def save_tasks(self):
        self.todo_list.save_tasks(self.filename)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
