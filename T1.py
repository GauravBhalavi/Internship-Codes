import tkinter as tk
from tkinter import ttk

class TodoListGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Todo List Application")

        self.tasks = []

        # Task Input
        self.task_entry = ttk.Entry(self, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Time Input
        self.time_entry = ttk.Entry(self, width=20)
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(self, text="Time (optional, e.g., '12:00 PM')").grid(row=1, column=1, padx=10, pady=2)

        # Add Task Button
        self.add_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Task List
        self.task_listbox = tk.Listbox(self, width=50, height=10)
        self.task_listbox.grid(row=2, columnspan=3, padx=10, pady=10)

        # List Tasks Button
        self.list_button = ttk.Button(self, text="List Tasks", command=self.list_tasks)
        self.list_button.grid(row=3, column=0, padx=10, pady=10)

        # Update Task Button
        self.update_button = ttk.Button(self, text="Update Task", command=self.update_task)
        self.update_button.grid(row=3, column=1, padx=10, pady=10)

        # Delete Task Button
        self.delete_button = ttk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        time = self.time_entry.get()
        task_with_time = task if not time else f"{task} (Due: {time})"
        self.tasks.append(task_with_time)
        self.task_listbox.insert(tk.END, task_with_time)
        self.task_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def list_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            new_time = self.time_entry.get()
            updated_task = new_task if not new_time else f"{new_task} (Due: {new_time})"
            self.tasks[index] = updated_task
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, updated_task)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)

if __name__ == "__main__":
    app = TodoListGUI()
    app.mainloop()
